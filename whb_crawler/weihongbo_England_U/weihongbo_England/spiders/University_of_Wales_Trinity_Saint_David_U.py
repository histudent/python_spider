import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'University_of_Wales_Trinity_Saint_David_U'
    allowed_domains = []
    base_url= 'https://www.uwtsd.ac.uk%s'
    start_urls = []
    C = ['/ba-ancient-civilisations/',
'/ba-ancient-history/',
'/undergraduate/applied-computing/meng-computer-systems-electronics-applied-environmental-engineering/',
'/ba-archaeology/',
'/ba-ancient-history-ancient-egyptian-culture/',
'/bsc-architecture/',
'/beng-automotive-engineering/',
'/beng-automotive-engineering-4-yr/',
'/ba-accounting/',
'/ba-applied-drama/',
'/ba-business-and-management/',
'/ba-business-management/',
'/ba-performing-arts-contemporary-performance/',
'/ba-cultural-industries-management/',
'/ba-design-crafts/',
'/ba-architectural-glass-arts/',
'/ba-international-business/',
'/ba-law-and-business/',
'/ba-rural-enterprise-management/',
'/ba-3d-computer-animation/',
'/ba-acting/',
'/ba-adventure-filmmaking/',
'/ba-advertising-brand-design/',
'/ba-advocacy/',
'/ba-ancient-history-archaeology/',
'/ba-ancient-history-history/',
'/ba-ancient-history-education-studies/',
'/ba-ancient-history-latin/',
'/ba-anthropology/',
'/ba-anthropology-psychology/',
'/ba-archaeology-anthropology/',
'/ba-art-gallery-museum-studies/',
'/ba-automotive-design/',
'/ba-business-management-events-festivals/',
'/ba-business-management-finance/',
'/ba-business-management-human-resource-management/',
'/ba-business-management-marketing/',
'/ba-chinese-civilisation-and-medieval-studies/',
'/ba-chinese-studies-education-studies/',
'/ba-classical-studies-heritage-studies/',
'/ba-classical-studies-archaeology/',
'/ba-classical-studies-creative-writing/',
'/ba-classical-studies-theology/',
'/ba-classical-studies-ancient-egyptian-culture/',
'/ba-classical-studies-with-education-studies/',
'/undergraduate/classics/ba-classical-civilisation-with-greek/',
'/ba-english-classical-studies/',
'/ba-classical-studies-religious-studies/',
'/ba-classical-studies-heritage-management/',
'/ba-creative-computer-games-design/',
'/bsc-music-technology/',
'/ba-dance/',
'/ba-digital-marketing/',
'/ba-early-years-education-and-care/',
'/ba-early-years-education-and-care-early-years-practitioner-2-years/',
'/undergraduate/early-years/ba-early-years-education-and-care-early-years-practitioner-status---2-years/',
'/ba-early-years-education-and-care-early-years-practitioner/',
'/ba-education-studies/',
'/ba-education-studies-additional-learning-needs-inclusion/',
'/ba-education-studies-contemporary-learners-learning/',
'/ba-education-studies-international-perspectives/',
'/ba-primary-education-studies/',
'/ba-english-classical-studies/',
'/ba-english-education-studies/',
'/ba-english-tefl/',
'/ba-ethical-political-studies/',
'/ba-event-management/',
'/ba-film-tv/',
'/ba-filmmaking/',
'/ba-fine-art-site-context/',
'/ba-graphic-design/',
'/ba-heritage-studies-digital-humanities/',
'/ba-history-education-studies/',
'/ba-humanistic-counselling/',
'/ba-illustration/',
'/ba-international-hotel-management/',
'/ba-international-sports-management/',
'/ba-international-travel-and-tourism-management/',
'/ba-law-criminology/',
'/ba-law-policing/',
'/ba-law-and-public-service/',
'/ba-management-skills-for-the-workplace/',
'/ba-leisure-management/',
'/ba-medieval-studies-classical-studies/',
'/ba-medieval-studies-modern-historical-studies/',
'/ba-medieval-studies-latin/',
'/ba-modern-historical-studies-heritage-management/',
'/ba-music-performance-production/',
'/ba-outdoor-education/',
'/cbc/ba-perfformio/',
'/ba-philosophy-classical-studies/',
'/ba-philosophy-psychology/',
'/ba-philosophy-education-studies/',
'/ba-philosophy-religion-applied-psychology/',
'/ba-photography-in-the-arts/',
'/ba-photojournalism/',
'/ba-physical-education/',
'/ba-primary-education-qts/',
'/ba-product-design/',
'/ba-public-services/',
'/ba-religion-ethics-applied-psychology/',
'/ba-religion-philosophy-ethics/',
'/ba-religion-theology-ethics/',
'/ba-religion-theology-philosophy/',
'/ba-religious-studies-theology/',
'/ba-religious-studies-psychology/',
'/ba-religious-studies-education-studies/',
'/ba-religious-studies-islamic-studies/',
'/ba-set-design/',
'/ba-sinology/',
'/ba-social-studies-additional-needs/',
'/ba-social-studies-communities-families-individuals/',
'/ba-social-studies-health-social-care/',
'/ba-sport-health/',
'/ba-sports-management/',
'/ba-stadium-sports-facility-management/',
'/ba-surface-pattern-design-fashion-object/',
'/ba-surface-pattern-design-contemporary-applied-arts-practice/',
'/ba-surface-pattern-design-textiles-for-fashion/',
'/ba-surface-pattern-design-textiles-for-interiors/',
'/ba-theatre-design-production/',
'/ba-theology/',
'/ba-theology-education-studies/',
'/ba-theology-philosophy-ethics/',
'/ba-tourism-management/',
'/ba-transport-design/',
'/ba-vocal-studies/',
'/ba-watersports-management/',
'/ba-youth-community-work/',
'/beng-electrical-electronic-engineering/',
'/bsc-psychology/',
'/bsc-counselling-studies-psychology/',
'/bsc-applied-psychology/',
'/bsc-health-care-children-young-people/',
'/bsc-health-social-care/',
'/bsc-health-management/',
'/bsc-health-nutrition-lifestyle/',
'/bsc-mental-health/',
'/bsc-police-sciences/',
'/bsc-policing-criminology/',
'/bsc-product-design-technology/',
'/bsc-public-health/',
'/bsc-sports-exercise-science/',
'/sport-and-exercise-science/',
'/bsc-outdoor-fitness/',
'/bsc-personal-training/',
'/bsc-sports-exercise-science-sports-nutrition/',
'/bsc-sport-therapy/',
'/cert-he-art-and-design-foundation/',
'/cert-he/certificate-of-higher-education-in-advocacy/',
'/cert-he-care/',
'/cert-he-chinese/',
'/cert-he-nursing-studies-health/',
'/cert-he/certificate-of-higher-education-in-stem/',
'/certhe-young-peoples-health-wellbeing/',
'/certificate-of-higher-education-skills-for-the-workplace/',
'/ba-chinese-studies/',
'/ba-chinese-studies-history/',
'/ba-classical-civilisation/',
'/ba-classics/',
'/bsc-computing/',
'/bsc-computer-networks/',
'/bsc-computing-information-systems-foundation/',
'/bsc-computer-games-development/',
'/bsc-software-engineering/',
'/bsc-web-development/',
'/bsc-web-development-foundation/',
'/bsc-applied-computing-foundation/',
'/ba-conflict-and-war/',
'/ba-creative-writing/',
'/hnd-electronics-engineering/',
'/beng-energy-environmental-engineering-4-year/',
'/beng-energy-environmental-engineering/',
'/ba-english/',
'/bsc-environmental-conservation/',
'/beng-extreme-sports-engineering-4-year/',
'/beng-extreme-sports-engineering/',
'/fdsc-health-care-children-young-people/',
'/fda-events-management/',
'/fda-sports-management/',
'/fda-tourism-management/',
'/cert-he/gateway-to-the-humanities/',
'/graduate-diploma-bible-theology/',
'/ba-heritage-studies/',
'/ba-history/',
'/hnd-business-management/',
'/hnd-events-management/',
'/hnd-health-social-care/',
'/hnd-health-management/',
'/hnd-public-services/',
'/hnd-sports-management/',
'/hnd-tourism-management/',
'/foundation/humanities-foundation/',
'/integrated-masters-humanistic-counselling/',
'/msocstud-social-studies-additional-needs/',
'/msocstud-social-studies-health-social-care/',
'/ba-international-development-and-global-politics/',
'/ba-humanities/',
'/bsc-logistics-supply-chain-management/',
'/mtour-tourism-management/',
'/marts-ancient-civilisations/',
'/marts-3d-computer-animation/',
'/marts-art-gallery-museum-studies/',
'/marts-classical-languages/',
'/marts-creative-computer-games-design/',
'/marts-digital-film-television-production/',
'/mart-fine-art/',
'/undergraduate/international-development-and-global-politics/marts-international-development-humanitarianism-and-law/',
'/marts-photography-in-the-arts/',
'/marts-photojournalism/',
'/mdes-advertising-brand-design/',
'/mdes-automotive-design/',
'/mdes-graphic-design/',
'/mdes-illustration/',
'/mdes-product-design/',
'/mdes-product-design-technology/',
'/mdes-set-design/',
'/mdes-surface-pattern-design-fashion-object/',
'/mdes-surface-pattern-design-maker/',
'/mdes-surface-pattern-design-textile-for-interiors/',
'/mdes-surface-pattern-design-textile-for-fashion/',
'/mdes-transport-design/',
'/meach-early-childhood/',
'/beng-mechanical-manufacturing-engineering-4-year/',
'/beng-mechanical-engineering-four-year-including-foundation-entry/',
'/beng-mechanical-engineering/',
'/ba-medieval-studies/',
'/marts-music-technology/',
'/ba-modern-historical-studies/',
'/beng-motorcycle-engineering/',
'/beng-motorcycle-engineering-4yr/',
'/beng-motorsport-engineering/',
'/beng-motorsport-engineering-4yrs/',
'/bsc-motorsport-management/',
'/dip-he-nursing-studies-health/',
'/ba-philosophy/',
'/undergraduate/philosophy-politics-and-economics/',
'/undergraduate/political-ecology/',
'/ba-religious-studies/',
'/certhe-health-and-wellbeing-for-carers/',
'/cert-he/certificate-of-higher-education-workplace-health-and-wellbeing/',
'/cert-he/certificate-of-higher-education-workplace-health-and-wellbeing/',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'University of Wales Trinity Saint David'
        try:
            location = response.xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/p[2]/a[2]/strong').extract()[0]
            location = remove_tags(location)
            #print(location)
        except:
            location = 'N/A'
            #print(location)
        try:
            department = response.xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/p[2]/a[3]/strong').extract()[0]
            department = remove_tags(department)
            department = department.replace('\n\n', '\n')
            department = department.replace('\r\n', '')
            department = department.replace('	', '')
            department = department.replace('  ', '')
            department = department.replace('\n', '')
            department = department.replace('Our Staff', '')
            #print(department)
        except:
            department = ''
            #print(department)


        try:
            degree_name = response.xpath('/html/body/div[2]/section/div/div[2]/div/h1').extract()[0]
            degree_name = remove_tags(degree_name)

            degree_name = degree_name.split()[0]

            #degree_name = re.findall('(.*)\n.*',degree_name)[0]
            #degree_name = re.findall('(.*)                    .*',degree_name)[0]
            #degree_name = re.findall('\((.*)\)',degree_name)[0]
            #degree_name = degree_name.replace('\n',degree_name)
            #degree_name = degree_name.replace(' ','')
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
            programme_en = response.xpath('//h1').extract()[0]
            programme_en = remove_tags(programme_en)
            #programme_en = re.findall(' (.*)',programme_en)[0]
            programme_en = programme_en.replace(degree_name+' ','')
            #programme_en = programme_en.replace('  ','')
            #programme_en = programme_en.replace('\n', '')
            #programme_en = re.findall(('                    '),'')[0]
            #programme_en = re.findall("(.*)\(.*\)",programme_en)[0]
            #programme_en = programme_en.replace('\n','')
            #programme_en = programme_en.replace('  ','')
            print(programme_en)
        except:
            programme_en = 'N/A'
            print(programme_en)

        try:
            overview_en = response.xpath('//*[@id="collapseCourseOverview"]/div').extract()[0]
            overview_en = remove_tags(overview_en)
            overview_en = overview_en.replace('  ','')
            #overview_en = overview_en.replace('\n\n','\n')
            overview_en = overview_en.replace('\n\n','')
            overview_en = overview_en.replace('\r\n','')
            overview_en = overview_en.replace('\n','')
            overview_en = '<div>' + overview_en + '</div>'
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
            modules_en = response.xpath('//*[@id="collapseModules"]/div').extract()[0]
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
            rntry_requirements_en = response.xpath('//*[@id="collapseEntryCriteria"]/div').extract()[0]
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
            require_chinese_en = ''
        except:
            require_chinese_en = ''
        try:
            ielts_desc = 'An overall English Language level equivalent to an IELTS score of 6.5 (or equivalent) with no lower than 6.5 in reading and writing, and with no lower than 5.5 in listening or speaking.'
            #print(ielts_desc)

        except:
            ielts_desc = 'N/A'

            #print(ielts_desc)

        try:
            ielts = '6.5'
            #ielts =remove_tags(ielts)
            #ielts = re.findall('IELTS(.*)',ielts)[0]
            #ielts = re.findall('(\d\.\d)',ielts)[0]
            #print(ielts)

        except:

            ielts = 6.5
            #print(ielts)
        try:
            ielts_l = 5.5
            #print(ielts_l)
            ielts_l = remove_tags(ielts_l)
        except:
            ielts_l = 5.5

        try:
            ielts_s = 5.5

        except:
            ielts_s = 5.5

        try:
            ielts_r = 6.5
        except:
            ielts_r = 6.5

        try:
            ielts_w = 6.5
        except:
            ielts_w = 6.5

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
            career_en = response.xpath('//*[@id="collapseCareerOpportunities"]/div').extract()[0]
            career_en = remove_tags(career_en)
            career_en = career_en.replace('\r\n','')
            career_en = career_en.replace('  ','')
            career_en = career_en.replace('\n','')
            career_en = "<div><span>" + career_en + "</span></div>"
            #print(career_en)
        except:
            career_en = ''
            #print(career_en)
        try:
            apply_desc_en = '<p>The Global Education Unit and academic staff frequently visit China throughout the year to meet prospective students and work with our academic partners. The university also work with International Student Recruitment Representatives and Recruitment Agents who can assist you in your application process. Alternatively, you can apply to the university directly, where an allocated international officer will help you through the applications process.</p>'
            #apply_desc_en = remove_tags(apply_desc_en)
            #apply_desc_en = "<div>" + apply_desc_en + "</div>"
            #print(apply_desc_en)
        except:
            apply_desc_en = ''

        try:
            apply_documents_en = '<p>Undergraduate Programmes, applicants must have one of the following: Graduation Certificate from a Specialised College / School (Zhongzhuan) Chinese University / College Entrance Examination (Gaokao) Graduation Certificate (Zhuanke / Dazhuan / Gaozhi) – (may be considered for advanced entry to certain programmes) Successful completion of a recognised Foundation programme Postgraduate Programmes, applicants must have a Bachelor Degree. School certificates and certified transcripts must accompany your application.</p>'
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
            duration =  response.xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/p[1]/strong[3]|/html/body/div[1]/div/div/div[2]/div[1]/div[2]/p[1]').extract()[0]
            duration = remove_tags(duration)
            #duration = remove_tags(duration)
            #duration = re.findall('(\d) Years',duration)[0]
            if '3 years' in duration:
                duration = '3'
            elif '4 years' in duration:
                duration = '4'
            elif '5 years' in duration:
                duration = '5'
            elif '6 years' in duration:
                duration = '6'
            elif '2 years' in duration:
                duration = '2'
            elif '1 year' in duration:
                duration = '1'
            elif 'two' in duration:
                duration = '2'
            else:
                duration = '3'
            #print(duration)
        except:
            duration = '0'
            #print(duration)



        try:
            other = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/a').extract()[0]
            other = remove_tags(other)
            #print('成功'+ other + response.url)
        except:
            other = ''
           #print('失败' + other)

        try:
            ib = response.xpath('//*[@id="tab-Entry_Requirements"]/div/div[1]/div[1]/table[1]/tbody/tr[11]/td[2]').extract()[0]
            ib = remove_tags(ib)
            #print(ib)
        except:
            ib = ''
            #print(ib)

        try:
            alevel = response.xpath('//*[@id="tab-Entry_Requirements"]/div/div[1]/div/table[1]').extract()[0]
            alevel = remove_tags(alevel)
            alevel = re.findall("(\w\w\w) at A Level",alevel)[0]
            #print(alevel)
        except:
            alevel = 'CC'
            #print(alevel)
        try:
            ucascode = response.xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/p[1]/strong[1]|/html/body/div[1]/div/div/div[2]/div[1]/div[2]/p[1]/strong[1]').extract()[0]
            ucascode = remove_tags(ucascode)

            #print(ucascode)
        except:
            ucascode = 'N/A'
            #print(ucascode)

        try:
            tuition_fee = response.xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/p[2]').extract()[0]
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = tuition_fee.replace('£','')
            tuition_fee = tuition_fee.replace(',','')
            tuition_fee = tuition_fee.replace('*','')
            tuition_fee = tuition_fee.replace(' ','')
            tuition_fee = tuition_fee.replace('\r\n','')
            tuition_fee = tuition_fee.replace('\n','')
            tuition_fee = re.findall('(\d\d\d\d\d)',tuition_fee)[0]

            # tuition_fee = tuition_fee.replace('  ','')
            # tuition_fee = tuition_fee.replace('\n','')
            # tuition_fee = re.findall('Full-time international students: £(.*) paStudents',tuition_fee)[0]
            # tuition_fee = int(tuition_fee)
            #print(tuition_fee)
        except:
            tuition_fee = 0
            #print(tuition_fee)

        try:
            assessment_en = response.xpath('//*[@id="collapseAssessment"]/div').extract()[0]
            assessment_en = remove_tags(assessment_en)
            assessment_en = assessment_en.replace('\n','')
            assessment_en = assessment_en.replace('\r\n','')
            assessment_en = assessment_en.replace('  ',' ')
            assessment_en = "<p>" + assessment_en + "</p>"
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
        item["batch_number"] = 9
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
        item["require_chinese_en"] = require_chinese_en
        item["assessment_en"] = assessment_en
        #item["apply_pre"] = ''
        yield item


