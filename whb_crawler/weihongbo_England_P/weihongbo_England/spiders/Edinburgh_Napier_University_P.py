import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'Edinburgh_Napier_University_P'
    allowed_domains = []
    base_url= 'https://www.napier.ac.uk%s'
    start_urls = []
    C = ['/courses/ma-creative-writing-postgraduate-fulltime',
'/courses/msc-creative-advertising-postgraduate-fulltime',
'/courses/mfa-directing-postgraduate-fulltime',
'/courses/ma-film-postgraduate-fulltime',
'/courses/mfa-playwriting-postgraduate-fulltime',
'/courses/ma-journalism-postgraduate-fulltime',
'/courses/mm-masters-of-midwifery-postgraduate-fulltime',
'/courses/mn-masters-in-nursing-adult-postgraduate-fulltime',
'/courses/mn-masters-in-nursing-child-postgraduate-fulltime',
'/courses/msc-advanced-materials-engineering-postgraduate-fulltime',
'/courses/mn-masters-in-nursing-mental-health-postgraduate-fulltime',
'/courses/msc-computing-postgraduate-fulltime',
'/courses/msc-computing-with-professional-placement-postgraduate-fulltime',
'/courses/msc-business-information-technology-postgraduate-fulltime',
'/courses/mn-masters-in-nursing-learning-disability-postgraduate-fulltime',
'/courses/msc-environmental-sustainability-postgraduate-fulltime',
'/courses/msc-renewable-energy-postgraduate-fulltime',
'/courses/msc-timber-architectural-design-and-technology-postgraduate-fulltime',
'/courses/msc-transport-planning-and-engineering-postgraduate-fulltime',
'/courses/ma-screenwriting-postgraduate-fulltime',
'/courses/mscpgdippgcert-advanced-structural-engineering-postgraduate-fulltime',
'/courses/msc-publishing-postgraduate-fulltime',
'/courses/pgdip-career-guidance-and-development-postgraduate-fulltime',
'/courses/msc-wildlife-biology-and-conservation-postgraduate-fulltime',
'/courses/mba-mba-leadership-practice-lpu-postgraduate-fulltime',
'/courses/msc-sport-performance-enhancement-postgraduate-fulltime',
'/courses/msc-ecotourism-postgraduate-fulltime',
'/courses/mba-mba-postgraduate-fulltime',
'/courses/msc-business-management-entrepreneurship-postgraduate-fulltime',
'/courses/msc-biomedical-science-postgraduate-fulltime',
'/courses/msc-business-management-human-resource-management-postgraduate-fulltime',
'/courses/msc-biotechnology-for-environmental-sustainability-postgraduate-fulltime',
'/courses/msc-business-management-marketing-postgraduate-fulltime',
'/courses/msc-business-management-sales-postgraduate-fulltime',
'/courses/msc-clinical-exercise-science-postgraduate-fulltime',
'/courses/msc-business-management-postgraduate-fulltime',
'/courses/msc-drug-design-and-biomedical-science-postgraduate-fulltime',
'/courses/msc-pharmaceutical-science-postgraduate-fulltime',
'/courses/msc-marketing-postgraduate-fulltime',
'/courses/msc-financial-technology-postgraduate-fulltime',
'/courses/msc-flexible-managed-programme-business-school-postgraduate-fulltime',
'/courses/msc-marketing-with-sales-management-postgraduate-fulltime',
'/courses/msc-intercultural-business-communication-postgraduate-fulltime',
'/courses/msc-international-tourism-marketing-postgraduate-fulltime',
'/courses/msc-intercultural-business-communication-with-tesol-postgraduate-fulltime',
'/courses/msc-international-banking-and-finance-postgraduate-fulltime',
'/courses/msc-international-business-management-postgraduate-fulltime',
'/courses/msc-international-festival-and-event-management-postgraduate-fulltime',
'/courses/msc-international-finance-postgraduate-fulltime',
'/courses/msc-international-hospitality-management-postgraduate-fulltime',
'/courses/msc-international-human-resource-management-postgraduate-fulltime',
'/courses/ma-environmental-graphics-postgraduate-fulltime',
'/courses/msc-international-tourism-destination-management-postgraduate-fulltime',
'/courses/ma-exhibition-design-postgraduate-fulltime',
'/courses/ma-interaction-design-postgraduate-fulltime',
'/courses/ma-product-design-prototyping-postgraduate-fulltime',
'/courses/ma-lighting-design-postgraduate-fulltime',
'/courses/ma-motion-graphics-postgraduate-fulltime',
'/courses/msc-medical-biotechnology-postgraduate-fulltime',
'/courses/msc-automation-and-control-postgraduate-fulltime',
'/courses/msc-construction-project-management-postgraduate-fulltime',
'/courses/msc-marketing-with-festival-and-event-management-postgraduate-fulltime',
'/courses/msc-architectural-technology--building-performance-postgraduate-fulltime',
'/courses/msc-business-event-management-postgraduate-fulltime',
'/courses/msc-advanced-security-and-digital-forensics-postgraduate-fulltime',
'/courses/msc-applied-criminology-and-forensic-psychology-postgraduate-fulltime',
'/courses/msc-real-estate-management-and-investment-postgraduate-fulltime',
'/courses/mfa-advanced-film-practice-postgraduate-fulltime',
'/courses/msc-human-resource-management-postgraduate-fulltime',
'/courses/msc-healthcare-management-postgraduate-fulltime',
'/courses/ma-digital--public-humanities-postgraduate-fulltime',
'/courses/msc-international-marketing-postgraduate-fulltime',
'/courses/msc-international-heritage-and-cultural-tourism-management-postgraduate-fulltime',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'Edinburgh Napier University'
        try:
            location = 'Merchiston'
            #location = remove_tags(location)
            #location = remove_tags(location)
            #print(location)
        except:
            location = 'n/a'
            #print(location)
        try:
            department = response.xpath('').extract()
            department = remove_tags(department)
        except:
            department = ''

        try:
            degree_name = response.xpath('//*[@id="ctl22_centerdiv"]/div/h1/span[1]').extract()[0]
            degree_name = remove_tags(degree_name)
            #degree_name = re.findall('\((.*)\)',degree_name)[0]
            #degree_name = degree_name.replace('\n',degree_name)
            #print(degree_name)
        except:
            degree_name = ''

        try:
            degree_overview_en = ''
            degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = "<div><p>" + degree_overview_en + "</p></div>"
            #print(degree_overview_en)
        except:
            degree_overview_en = ''

        try:
            programme_en = response.xpath('//*[@id="ctl22_centerdiv"]/div/h1/span[2]').extract()[0]
            programme_en = remove_tags(programme_en)
            #programme_en = re.findall("(.*)\(.*\)",programme_en)[0]
            #programme_en = programme_en.replace('\n','')
            #programme_en = programme_en.replace('  ','')
            #print(programme_en)
        except:
            programme_en = ''
            #print(programme_en)

        try:
            overview_en = response.xpath('//*[@id="tab-overview1"]/section/div[1]').extract()[0]
            overview_en = remove_tags(overview_en)
            overview_en = '<div>'+overview_en +'</div>'
            overview_en = overview_en.replace('  ','')
            #overview_en = overview_en.replace('\n\n','\n')
            overview_en = overview_en.replace('\n\n','')
            overview_en = overview_en.replace('\r\n','')
            #overview_en = remove_tags(overview_en)
            #print(overview_en)
        except:
            overview_en = ''

        try:
            start_date = '9'

            #print(start_date)
        except:
            start_date = ''


        try:
            modules_en = response.xpath('//*[@id="pnlDetails"]').extract()[0]
            modules_en = remove_tags(modules_en)
            modules_en = modules_en.replace('\n\n','\n')
            modules_en = modules_en.replace('\r\n','')
            modules_en = modules_en.replace('	','')
            modules_en = modules_en.replace('  ','')
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
            rntry_requirements_en = response.xpath('//*[@id="tab0"]').extract()[0]
            rntry_requirements_en = remove_tags(rntry_requirements_en)
            rntry_requirements_en = "<div>"+rntry_requirements_en+"</div>"
            rntry_requirements_en = rntry_requirements_en.replace('\r\n','')
            rntry_requirements_en =rntry_requirements_en.replace('		                        ','')
            #print(rntry_requirements_en)
        except:
            rntry_requirements_en = ''

        try:
            professional_background = response.xpath('').extract()
            professional_background = remove_tags(professional_background)
        except:
            professional_background = ''

        try:
            ielts_desc = ''
            #ielts_desc = remove_tags(ielts_desc)

            #ielts_desc = ielts_desc.replace('\'','')
            #ielts_desc = ielts_desc.replace('"','')
            #ielts_desc = ielts_desc.replace('\xa0','')
            # ielts_desc = ielts_desc.replace('                        \n','')
            # ielts_desc = ielts_desc.replace('\t\t','')
            # ielts_desc = ielts_desc.replace('\\\n','')
            #print(ielts_desc)
        except:
            ielts_desc = ''

        try:
            aa = response.xpath('//*[@id="tab4"]').extract()[0]
            aa = remove_tags(aa)
        except:
            aa = 0
        try:
            ielts = re.findall('(\d.\d)',aa)[0]
            #i#elts = remove_tags(ielts)
            print(ielts)
        except:
            ielts = 0

        try:
            ielts_l = re.findall('(\d.\d)',aa)[1]
            print(ielts_l)
            #ielts_l = remove_tags(ielts_l)
        except:
            ielts_l = 0

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
            work_experience_desc_en = response.xpath('//*[@id="content"]/div[13]/div/a/div/div[1]/p').extract()[0]
            work_experience_desc_en = remove_tags(work_experience_desc_en)
            #print(work_experience_desc_en)
        except:
            work_experience_desc_en = ''

        try:
            interview_desc_en = response.xpath('').extract()
            interview_desc_en = remove_tags(interview_desc_en)
        except:
            interview_desc_en = ''

        try:
            portfolio_desc_en = response.xpath('').extract()
            portfolio_desc_en = remove_tags(portfolio_desc_en)
        except:
            portfolio_desc_en = ''

        try:
            career_en = response.xpath('//*[@id="careers"]/section[2]/div[1]').extract()[0]
            career_en = remove_tags(career_en)
            career_en = career_en.replace('\r\n','')
            career_en = career_en.replace('        ','')
            career_en = "<div><span>" + career_en + "</span></div>"
            #print(career_en)
        except:
            career_en = ''

        try:
            apply_desc_en = 'https://evision.napier.ac.uk/si/sits.urd/run/siw_ipp_lgn.login?'
            apply_desc_en = remove_tags(apply_desc_en)
            #apply_desc_en = "<div>" + apply_desc_en + "</div>"
            #print(apply_desc_en)
        except:
            apply_desc_en = ''

        try:
            apply_documents_en = '<p>Your personal statement on your UCAS form is your chance to shine. It’s crucial to your application and can determine what offers you receive. When writing your statement: make sure it\'s styled in a formal manner and reads well write in a precise way using small paragraphs focus on your strengths, achievements and aspirations write about your skills and give examples explain why the course is interesting to you show that you\'ve done your research be truthful, accurate and enthusiastic check your spelling and grammar Be sure to include: your reasons for choosing the course relevant work or academic experience and skills personal interests that relate to the course your career goals any plans for taking a year out (if applicable)</p>'
            apply_documents_en = remove_tags(apply_documents_en)
        except:
            apply_documents_en = ''


        apply_fee = 13


        #other = ''
        try:
            apply_proces_en = response.xpath('').extract()
        except:
            apply_proces_en = ''


        try:
            duration =  '1'
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
            ucascode = response.xpath('/html/body/div[3]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[2]').extract()[0]
            ucascode = remove_tags(ucascode)

            #print(ucascode)
        except:
            ucascode = ''
            #print(ucascode)

        try:
            tuition_fee = response.xpath('//*[@id="tab-fees"]/table/tbody/tr[2]/td[2]').extract()[0]
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = tuition_fee.replace('£','')
            tuition_fee = tuition_fee.replace(',','')
            tuition_fee = tuition_fee.replace('*','')
            tuition_fee = re.findall('(\d\d\d\d\d)',tuition_fee)[0]

            # tuition_fee = tuition_fee.replace('  ','')
            # tuition_fee = tuition_fee.replace('\n','')
            # tuition_fee = re.findall('Full-time international students: £(.*) paStudents',tuition_fee)[0]
            # tuition_fee = int(tuition_fee)
            #print(tuition_fee)
        except:
            tuition_fee = 0

        try:
            teach_time = response.xpath('//*[@id="tab-overview1"]/section/div[2]/div').extract()[0]
            teach_time = remove_tags(teach_time)
            if 'full' in teach_time:
                teach_time = 'fulltime'
            elif 'Full' in teach_time:
                teach_time = 'fulltime'
            else:
                teach_time = 'parttime'
            print(teach_time)
        except:
            teach_time = 'N/A'
            print(teach_time)

        teach_type = 'taught'
        item["university"] = university
        item["location"] = location
        item["department"] = department
        item["degree_type"] = 2
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
        item["batch_number"] = 2
        item["finishing"] = 0
        stime = time.time()
        create_time = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(float(stime)))
        #print(create_time)
        item["create_time"] = create_time
        item["import_status"] = 0
        item["duration"] = duration
        item["tuition_fee"] = tuition_fee
        item["update_time"] = create_time
        #item["alevel"] = alevel
        #item["ib"] = ib
        #item["ucascode"] = ucascode
        item["rntry_requirements"] = rntry_requirements_en
        item["teach_time"] = teach_time
        item["teach_type"] = teach_type
        item["require_chinese_en"] = ''
        item["assessment_en"] = ''
        #item["apply_pre"] = ''
        yield item


