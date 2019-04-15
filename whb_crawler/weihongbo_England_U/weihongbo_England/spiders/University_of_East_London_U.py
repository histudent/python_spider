import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'University_of_East_London_U'
    allowed_domains = []
    base_url= 'https://www.uel.ac.uk%s'
    start_urls = []
    C = ['/undergraduate/courses/ba-hons-accounting-and-finance',
'/undergraduate/courses/maccfin-hons-accounting-and-finance',
'/undergraduate/courses/ba-hons-accounting-and-finance-with-foundation-year',
'/undergraduate/courses/ba-hons-advertising',
'/undergraduate/courses/ba-hons-advertising-with-foundation-year',
'/undergraduate/courses/ba-hons-animation',
'/undergraduate/courses/ba-hons-animation-with-foundation-year',
'/undergraduate/courses/fdsci-applied-community-sport',
'/undergraduate/courses/bsc-hons-architectural-design-technology',
'/undergraduate/courses/bsc-hons-architectural-design-technology-with-foundation-year',
'/undergraduate/courses/bsc-hons-architecture-arbriba-part-1-with-foundation-year',
'/undergraduate/courses/bsc-hons-architecture-arbriba-part-1',
'/undergraduate/courses/bsc-hons-biochemistry',
'/undergraduate/courses/bsc-hons-biochemistry-with-foundation-year',
'/undergraduate/courses/bsc-hons-biomedical-science',
'/undergraduate/courses/bsc-hons-biomedical-science-with-foundation-year',
'/undergraduate/courses/llb-hons-business-law',
'/undergraduate/courses/bsc-hons-business-management',
'/undergraduate/courses/bsc-hons-business-management-with-foundation-year',
'/undergraduate/courses/bsc-hons-business-psychology',
'/undergraduate/courses/bsc-hons-chemistry',
'/undergraduate/courses/bsc-hons-chemistry-with-foundation-year',
'/undergraduate/courses/bsc-hons-child-psychology',
'/undergraduate/courses/beng-hons-civil-engineering',
'/undergraduate/courses/bsc-hons-civil-engineering',
'/undergraduate/courses/meng-civil-engineering',
'/undergraduate/courses/bsc-hons-civil-engineering-with-foundation-year',
'/undergraduate/courses/fdsc-civil-engineering-and-construction-management',
'/undergraduate/courses/beng-hons-civil-engineering-with-foundation-year',
'/undergraduate/courses/bsc-hons-clinical-and-community-psychology',
'/undergraduate/courses/bsc-hons-computer-game-development',
'/undergraduate/courses/bsc-hons-computer-game-development-with-foundation-year',
'/undergraduate/courses/ba-hons-computer-games-design-story-development',
'/undergraduate/courses/ba-hons-computer-games-design-story-development-with-foundation-year',
'/undergraduate/courses/bsc-hons-computer-science',
'/undergraduate/courses/bsc-hons-computer-science-with-foundation-year',
'/undergraduate/courses/bsc-hons-computer-science-with-qualified-teacher-status',
'/undergraduate/courses/bsc-hons-computing-for-business',
'/undergraduate/courses/bsc-hons-computing-for-business-with-foundation-year',
'/undergraduate/courses/bsc-hons-construction-management',
'/undergraduate/courses/bsc-hons-construction-management-with-foundation-year',
'/undergraduate/courses/bsc-hons-counselling',
'/undergraduate/courses/ba-hons-creative-and-professional-writing',
'/undergraduate/courses/ba-hons-creative-and-professional-writing-with-foundation-year',
'/undergraduate/courses/ba-hons-criminology-and-criminal-justice',
'/undergraduate/courses/ba-hons-criminology-and-criminal-justice-with-foundation-year',
'/undergraduate/courses/ba-hons-criminology-and-law',
'/undergraduate/courses/ba-hons-criminology-and-psychology',
'/undergraduate/courses/ba-hons-dance-urban-practice',
'/undergraduate/courses/beng-hons-design-engineering',
'/undergraduate/courses/beng-hons-design-engineering-with-foundation-year',
'/undergraduate/courses/ba-hons-drama-applied-theatre-and-performance',
'/undergraduate/courses/ba-hons-early-childhood-and-special-education',
'/undergraduate/courses/ba-hons-early-childhood-studies',
'/undergraduate/courses/ba-hons-early-childhood-studies-with-foundation-year',
'/undergraduate/courses/ba-hons-early-childhood-with-cache-level-3-with-foundation-year',
'/undergraduate/courses/ba-hons-early-childhood-wih-education-and-qts',
'/undergraduate/courses/bsc-hons-economics',
'/undergraduate/courses/bsc-hons-economics-with-foundation-year',
'/undergraduate/courses/beng-hons-engineering-management',
'/undergraduate/courses/beng-hons-engineering-management-with-foundation-year',
'/undergraduate/courses/ba-hons-event-management',
'/undergraduate/courses/ba-hons-fashion-design',
'/undergraduate/courses/ba-hons-fashion-design-with-foundation-year',
'/undergraduate/courses/ba-hons-fashion-marketing',
'/undergraduate/courses/ba-hons-fashion-marketing-with-foundation-year',
'/undergraduate/courses/ba-hons-fashion-textiles',
'/undergraduate/courses/ba-hons-fashion-textiles-with-foundation-year',
'/undergraduate/courses/ba-hons-film',
'/undergraduate/courses/ba-hons-film-with-foundation-year',
'/undergraduate/courses/ba-hons-fine-art',
'/undergraduate/courses/ba-hons-fine-art-with-foundation-year',
'/undergraduate/courses/bsc-hons-forensic-psychology',
'/undergraduate/courses/beng-hons-general-engineering',
'/undergraduate/courses/beng-hons-general-engineering-with-foundation-year',
'/undergraduate/courses/ba-hons-graphic-design',
'/undergraduate/courses/ba-hons-graphic-design-with-foundation-year',
'/undergraduate/courses/ba-hons-hospitality-management',
'/undergraduate/courses/ba-hons-hospitality-management-with-foundation-year',
'/undergraduate/courses/bsc-hons-human-resource-management',
'/undergraduate/courses/bsc-hons-human-resource-management-with-foundation-year',
'/undergraduate/courses/ba-hons-illustration',
'/undergraduate/courses/ba-hons-illustration-with-foundation-year',
'/undergraduate/courses/ba-hons-interior-design',
'/undergraduate/courses/ba-hons-interior-design-with-foundation-year',
'/undergraduate/courses/ba-hons-international-development',
'/undergraduate/courses/ba-hons-international-development-with-foundation-year',
'/undergraduate/courses/ba-hons-international-development-with-ngo-management',
'/undergraduate/courses/ba-hons-international-development-with-ngo-management-with-foundation-year',
'/undergraduate/courses/ba-hons-journalism',
'/undergraduate/courses/ba-hons-journalism-with-foundation-year',
'/undergraduate/courses/llb-hons-law',
'/undergraduate/courses/llb-hons-law-with-criminology',
'/undergraduate/courses/llb-hons-law-with-foundation-year',
'/undergraduate/courses/llb-hons-law-with-international-relations',
'/undergraduate/courses/bsc-hons-marketing',
'/undergraduate/courses/bsc-hons-marketing-with-foundation-year',
'/undergraduate/courses/beng-hons-mechanical-engineering',
'/undergraduate/courses/meng-mechanical-engineering-integrated-masters',
'/undergraduate/courses/beng-hons-mechanical-engineering-with-foundation-year',
'/undergraduate/courses/ba-hons-media-and-communication',
'/undergraduate/courses/ba-hons-media-and-communication-with-foundation-year',
'/undergraduate/courses/bsc-hons-medical-physiology',
'/undergraduate/courses/bsc-hons-medical-physiology-with-foundation-year',
'/undergraduate/courses/diphe-medical-sciences',
'/undergraduate/courses/fda-montessori-pedagogy',
'/undergraduate/courses/ba-hons-music-performance-and-production',
'/undergraduate/courses/ba-hons-music-technology-and-production',
'/undergraduate/courses/bsc-hons-adult-nursing',
'/undergraduate/courses/ba-hons-performing-arts',
'/undergraduate/courses/bsc-hons-pharmaceutical-science',
'/undergraduate/courses/bsc-hons-pharmaceutical-science-with-foundation-year',
'/undergraduate/courses/bsc-hons-pharmacology',
'/undergraduate/courses/bsc-hons-pharmacology-with-foundation-year',
'/undergraduate/courses/ba-hons-photography',
'/undergraduate/courses/ba-hons-photography-with-foundation-year',
'/undergraduate/courses/bsc-hons-physiotherapy',
'/undergraduate/courses/bsc-hons-podiatry',
'/undergraduate/courses/ba-hons-policing',
'/undergraduate/courses/ba-hons-politics-and-international-relations',
'/undergraduate/courses/ba-hons-politics-and-international-relations-with-foundation-year',
'/undergraduate/courses/bsc-hons-product-design',
'/undergraduate/courses/bsc-hons-product-design-with-foundation-year',
'/undergraduate/courses/bsc-hons-psychology',
'/undergraduate/courses/bsc-hons-psychology-with-foundation-year',
'/undergraduate/courses/ba-hons-psychosocial-theory-and-practice',
'/undergraduate/courses/ba-hons-psychosocial-theory-and-practice-with-foundation-year',
'/undergraduate/courses/bsc-hons-public-health',
'/undergraduate/courses/bsc-hons-public-health-with-foundation-year',
'/undergraduate/courses/bsc-hons-public-health-and-health-promotion',
'/undergraduate/courses/bsc-hons-public-health-and-health-promotion-with-foundation-year',
'/undergraduate/courses/bsc-hons-public-health-and-health-services-management',
'/undergraduate/courses/bsc-hons-public-health-and-health-services-management-with-foundation-year',
'/undergraduate/courses/ba-hons-social-and-community-work',
'/undergraduate/courses/ba-hons-social-work',
'/undergraduate/courses/ba-hons-sociology',
'/undergraduate/courses/ba-hons-sociology-with-foundation-year',
'/undergraduate/courses/ba-hons-sociology-with-criminology',
'/undergraduate/courses/ba-hons-special-education',
'/undergraduate/courses/bsc-hons-sport-and-exercise-science',
'/undergraduate/courses/bsc-hons-sport-and-exercise-science-with-foundation-year',
'/undergraduate/courses/bsc-hons-sport-physical-education-and-development',
'/undergraduate/courses/bsc-hons-sport-physical-education-and-development-with-foundation-year',
'/undergraduate/courses/bsc-hons-sports-coaching',
'/undergraduate/courses/bsc-hons-sports-coaching-with-foundation-year',
'/undergraduate/courses/ba-hons-sports-journalism',
'/undergraduate/courses/ba-hons-sports-journalism-with-foundation-year',
'/undergraduate/courses/bsc-hons-sports-therapy',
'/undergraduate/courses/bsc-hons-sports-therapy-with-foundation-year',
'/undergraduate/courses/bsc-hons-surveying-and-mapping-sciences',
'/undergraduate/courses/bsc-hons-surveying-and-mapping-sciences-with-foundation-year',
'/undergraduate/courses/ba-hons-tourism-management',
'/undergraduate/courses/ba-hons-tourism-management-with-foundation-year',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'University of East London'
        try:
            location = response.xpath('//*[@id="course-summary-0"]/section[1]/div/div[4]/div[2]/p').extract()[0]
            location = remove_tags(location)
            #location = remove_tags(location)
            #print(location)
        except:
            location = 'N/A'
            #print(location)
        try:
            department = response.xpath('//*[@id="course-summary-0"]/section[1]/div/div[2]/div[2]/p').extract()[0]
            department = remove_tags(department)
            #print(department)
        except:
            department = 'N/A'
            #print(department)


        try:
            degree_name = response.xpath('/html/body/main/div/div[2]/section[1]/div[2]/div[1]/div/h2').extract()[0]
            degree_name = remove_tags(degree_name)
            degree_name = degree_name.split()[0]

            #degree_name = re.findall('(.*)\n.*',degree_name)[0]
            #degree_name = re.findall('(.*)                    .*',degree_name)[0]
            #degree_name = re.findall('\((.*)\)',degree_name)[0]
            #degree_name = degree_name.replace('\n',degree_name)
            #print(degree_name)
        except:
            degree_name = 'N/A'
            #print(degree_name)

        try:
            degree_overview_en = ''
            degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = "<div><p>" + degree_overview_en + "</p></div>"
            #print(degree_overview_en)
        except:
            degree_overview_en = ''

        try:
            programme_en = response.xpath('//h2').extract()[0]
            programme_en = remove_tags(programme_en)
            programme_en = programme_en.replace(degree_name,'')
            programme_en = programme_en.replace('  ','')
            programme_en = programme_en.replace('\n', '')
            #programme_en = re.findall(('                    '),'')[0]
            #programme_en = re.findall("(.*)\(.*\)",programme_en)[0]
            #programme_en = programme_en.replace('\n','')
            #programme_en = programme_en.replace('  ','')
            #print(programme_en)
        except:
            programme_en = 'N/A'

            #print(programme_en)

        try:
            overview_en = response.xpath('//*[@id="course-summary-0"]/div[2]/div/div[1]/div/div/div').extract()[0]
            overview_en = remove_tags(overview_en)
            overview_en = '<div>'+overview_en +'</div>'
            overview_en = overview_en.replace('  ','')
            #overview_en = overview_en.replace('\n\n','\n')
            overview_en = overview_en.replace('\n\n','')
            overview_en = overview_en.replace('\r\n','')
            overview_en = overview_en.replace('\n','')
            #overview_en = remove_tags(overview_en)
            #print(overview_en)
        except:
            overview_en = 'N/A'
            #print(overview_en)


        try:
            start_date = '9'

            #print(start_date)
        except:
            start_date = ''


        try:
            modules_en = response.xpath('//*[@id="what-youll-learn-3"]/div[2]/div|//*[@id="what-youll-learn-1"]/div/div|//*[@id="what-youll-learn-3"]/div/div').extract()[0]
            modules_en = remove_tags(modules_en)
            modules_en = modules_en.replace('\n\n','\n')
            modules_en = modules_en.replace('\r\n','')
            modules_en = modules_en.replace('	','')
            modules_en = modules_en.replace('  ','')
            modules_en = modules_en.replace('\n','')
            modules_en = "<div><p>" + modules_en + "</p></div>"
            #print(modules_en)
        except:
            modules_en = 'N/A'
            #print(modules_en)



        try:
            degree_requirements = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[2]/div[2]/div[1]/div[2]').extract()[0]
            degree_requirements = remove_tags(degree_requirements)
            degree_requirements = degree_requirements.replace('  ','')
            #print(degree_requirements)
        except:
            degree_requirements = ''
            #print(degree_requirements)

        try:
            rntry_requirements_en = response.xpath('//*[@id="entry-requirements-tab-0"]/div[1]').extract()[0]
            rntry_requirements_en = remove_tags(rntry_requirements_en)
            rntry_requirements_en = "<div>"+rntry_requirements_en+"</div>"
            rntry_requirements_en = rntry_requirements_en.replace('\n\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\r\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('  ','')
            #rntry_requirements_en =rntry_requirements_en.replace('		                        ','')
            #print(rntry_requirements_en)
        except:
            rntry_requirements_en = 'N/A'
            #print(rntry_requirements_en)

        try:
            professional_background = response.xpath('').extract()
            professional_background = remove_tags(professional_background)
        except:
            professional_background = ''

        try:
            ielts_desc = response.xpath('//*[@id="entry-requirements-tab-0"]').extract()[0]
            ielts_desc = remove_tags(ielts_desc)
            ielts_desc = re.findall('(Overall IELTS.*)',ielts_desc)[0]
            #print(ielts_desc)

        except:
            ielts_desc = 'N/A'

            #print(ielts_desc)

        try:
            ielts = re.findall('(\d\.\d)',ielts_desc)[0]
            #print(ielts)

        except:

            ielts = 6.0
            #print(ielts)
        try:
            ielts_l = re.findall('(\d.\d)',ielts_desc)[1]
            #print(ielts_l)
            #ielts_l = remove_tags(ielts_l)
        except:
            ielts_l = 5.5

        try:
            ielts_s = ielts_l

        except:
            ielts_s = 0

        try:
            ielts_r = ielts_l
        except:
            ielts_r = 0

        try:
            ielts_w = ielts_l
        except:
            ielts_w = 0

        try:
            toefl_code = response.xpath('').extract()
            toefl_code = remove_tags(toefl_code)
        except:
            toefl_code = 0

        try:
            toefl_desc = response.xpath('').extract()
            toefl_desc = remove_tags(toefl_desc)
        except:
            toefl_desc = 0

        try:
            toefl = response.xpath('').extract()
            toefl = remove_tags(toefl)

        except:
            toefl = 0

        try:
            toefl_l = response.xpath('').extrcat()
            toefl_l = remove_tags(toefl_l)

        except:
            toefl_l = 0

        try:
            toefl_s = response.xpath('').extract()
            toefl_s = remove_tags(toefl_s)

        except:
            toefl_s = 0

        try:
            toefl_r = response.xpath('').extract()
            toefl_r = remove_tags(toefl_r)
        except:
            toefl_r = 0

        try:
            toefl_w = response.xpath('').extract()
            toefl_w = remove_tags(toefl_w)
        except:
            toefl_w = 0

        try:
            interview_desc_en = response.xpath('//*[@id="entry-requirements-accordion-0"]/div[1]').extract()[0]
            interview_desc_en = remove_tags(interview_desc_en)
            interview_desc_en = interview_desc_en.replace('\n\n', '\n')
            interview_desc_en = interview_desc_en.replace('\r\n', '')
            interview_desc_en = interview_desc_en.replace('	', '')
            interview_desc_en = interview_desc_en.replace('  ', '')
            interview_desc_en = interview_desc_en.replace('\n', '')
            interview_desc_en = "<div>" + interview_desc_en + "</div>"
            #print(interview_desc_en)
        except:
            interview_desc_en = 'N/A'
            #print(interview_desc_en)
        try:
            work_experience_desc_en = response.xpath('').extract()
            work_experience_desc_en = remove_tags(work_experience_desc_en)
        except:
            work_experience_desc_en = ''

        try:
            portfolio_desc_en = response.xpath('').extract()
            portfolio_desc_en = remove_tags(portfolio_desc_en)
        except:
            portfolio_desc_en = ''

        try:
            career_en = response.xpath('//*[@id="your-future-career-5"]/div[1]/div').extract()[0]
            career_en = remove_tags(career_en)
            career_en = career_en.replace('\r\n','')
            career_en = career_en.replace('  ','')
            career_en = career_en.replace('\n','')
            career_en = "<div><span>" + career_en + "</span></div>"
            #print(career_en)
        except:
            career_en = 'N/A'
            #print(career_en)
        try:
            apply_desc_en = '<p>Applicants from outside the UK and those students for whom English is not their first language must have a good standard of English, as evidenced by internationally recognised qualifications such as IELTS. These requirements vary by course so you’ll need to check the course pages for further information. We accept a wide range of qualifications from across the world – from individual countries as well as internationally recognised qualifications such as the International Baccalaureate. When applying, don’t try to convert your qualifications to a UK equivalent. Simply give us the full award title, subject and grades/scores as they appear on your certificate(s). If your qualification is from an EU country, please contact our Applicant Enquiries team by phone on +44 (0)20 8223 3333 or by email at study@uel.ac.uk to find out whether it meets the requirements of UEL. If your qualification is from outside of the EU, our country pages contain information about acceptable qualifications. Our course pages list entry requirements specific to individual courses.</p>'
            #apply_desc_en = remove_tags(apply_desc_en)
            #apply_desc_en = "<div>" + apply_desc_en + "</div>"
            #print(apply_desc_en)
        except:
            apply_desc_en = ''

        try:
            apply_documents_en = '<p>We accept a wide range of qualifications from across the world – from individual countries as well as internationally recognised qualifications such as the International Baccalaureate. When applying, don’t try to convert your qualifications to a UK equivalent. Simply give us the full award title, subject and grades/scores as they appear on your certificate(s).</p>'
            #apply_documents_en = remove_tags(apply_documents_en)
        except:
            apply_documents_en = ''


        apply_fee = 0


        #other = ''
        try:
            apply_proces_en = response.xpath('').extract()
        except:
            apply_proces_en = ''


        try:
            duration =  3
            #duration = remove_tags(duration)
            #duration = re.findall('(\d) Years',duration)[0]
            #print(duration)
        except:
            duration = ''
            #print(duration)



        try:
            other = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/a').extract()[0]
            other = remove_tags(other)
            #print('成功'+ other + response.url)
        except:
            other = ''
           #print('失败' + other)

        try:
            ib = response.xpath('//*[@id="entry-requirements-tab-0"]/div[1]/div[2]/div[3]/div[3]').extract()[0]
            ib = remove_tags(ib)
            #print(ib)
        except:
            ib = ''
            #print(ib)

        try:
            alevel = response.xpath('//*[@id="entry-requirements-tab-0"]/div[1]/div[2]/div[1]/div[3]').extract()[0]
            alevel = remove_tags(alevel)
            #alevel = re.findall("(\w\w\w) at A Level",alevel)[0]
            #print(alevel)
        except:
            alevel = 'N/A'
            #print(alevel)
        try:
            ucascode = response.xpath('//*[@id="course-summary-0"]/div[2]/div/div[1]/div/section/div/div[3]/p').extract()[0]
            ucascode = remove_tags(ucascode)
            #print(ucascode)
            #print(ucascode)
        except:
            ucascode = 'N/A'
            #print(ucascode)

        try:
            tuition_fee = response.xpath('//*[@id="fees-and-funding-tab-5"]/div[2]/div[3]').extract()[0]
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = tuition_fee.replace('£','')
            tuition_fee = tuition_fee.replace(',','')
            tuition_fee = tuition_fee.replace('*','')
            tuition_fee = tuition_fee.replace(' ','')
            tuition_fee = tuition_fee.replace('\r\n','')
            tuition_fee = tuition_fee.replace('\n','')

            #tuition_fee = re.findall('(\d\d\d\d\d)',tuition_fee)[0]

            # tuition_fee = tuition_fee.replace('  ','')
            # tuition_fee = tuition_fee.replace('\n','')
            # tuition_fee = re.findall('Full-time international students: £(.*) paStudents',tuition_fee)[0]
            # tuition_fee = int(tuition_fee)
            #print(tuition_fee)
        except:
            tuition_fee = 0
            #print(tuition_fee)


        try:
            assessment_en =  response.xpath('//*[@id="what-youll-learn-3"]/div[2]/div/div[2]|//*[@id="what-youll-learn-1"]/div[2]/div/div[2]|//*[@id="what-youll-learn-3"]/div/div/div[2]').extract()[0]
            assessment_en = remove_tags(assessment_en)
            assessment_en = assessment_en.replace('\r\n', '')
            assessment_en = assessment_en.replace('  ', '')
            assessment_en = assessment_en.replace('\n', '')
            assessment_en = assessment_en.replace('			','')
            assessment_en = assessment_en.replace('		','')
            assessment_en = "<div>"+assessment_en+'</div>'
            #print(assessment_en)
        except:
            assessment_en = 'N/A'
            #print(assessment_en)
        item["university"] = university
        item["location"] = location
        item["department"] = department
        item["degree_type"] = 1
        item["degree_name"] = degree_name
        #item["degree_overview_en"] = degree_overview_en
        item["programme_en"] = programme_en
        item["overview_en"] = overview_en
        item["teach_time"] = 1
        item["start_date"] = start_date
        item["modules_en"] = modules_en
        item["career_en"] = career_en
        item["application_open_date"] = '9'
        item["deadline"] = ''
        item["apply_pre"] = '£'
        item["apply_fee"] = apply_fee
        #item["rntry_requirements_en"] = rntry_requirements_en
        item["degree_requirements"] = degree_requirements
        item["tuition_fee_pre"] = '£'
        #item["major_requirements"] = rntry_requirements_en
        item["professional_background"] = professional_background
        item["ielts_desc"] = ielts_desc
        item["ielts"] = ielts
        item["ielts_l"] = ielts_l
        item["ielts_s"] = ielts_l
        item["ielts_r"] = ielts_l
        item["ielts_w"] = ielts_l
        item["toefl_code"] = toefl_code
        item["toefl_desc"] = toefl_desc
        item["toefl"] = toefl
        item["toefl_l"] = toefl_l
        item["toefl_s"] = toefl_s
        item["toefl_r"] = toefl_r
        item["toefl_w"] = toefl_w
        item["work_experience_desc_en"] = work_experience_desc_en
        item["interview_desc_en"] = interview_desc_en
        item["portfolio_desc_en"] = portfolio_desc_en
        item["apply_desc_en"] = apply_desc_en
        item["apply_documents_en"] = apply_documents_en
        item["other"] = other
        item["url"] = response.url
        item["gatherer"] = 'weihongbo'
        item["apply_proces_en"] = apply_proces_en
        item["batch_number"] = 5

        item["finishing"] = 0
        stime = time.time()
        create_time = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(float(stime)))
        #print(create_time)
        item["create_time"] = create_time
        item["import_status"] = 0
        item["duration"] = duration
        item["tuition_fee"] = tuition_fee
        item["update_time"] = create_time
        item["alevel"] = alevel
        item["ib"] = ib
        item["ucascode"] = ucascode
        item["rntry_requirements"] = rntry_requirements_en
        item["assessment_en"] = assessment_en
        item["require_chinese_en"] = ''
        #item["apply_pre"] = ''
        yield item


