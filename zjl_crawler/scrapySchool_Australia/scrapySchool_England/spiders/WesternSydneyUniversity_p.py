# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/1 9:41'
import scrapy,json
import re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from w3lib.html import remove_tags
from scrapySchool_England.clearSpace import clear_space_str
import requests
from lxml import etree
from scrapySchool_England.translate_date import tracslateDate
from scrapySchool_England.getTuition_fee import getT_fee
class WesternSydneyUniversitySpider(scrapy.Spider):
    name = 'WesternSydneyUniversity_p'
    allowed_domains = ['westernsydney.edu.au/']
    start_urls = []
    C=[
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-applied-finance.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-business-marketing.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-business-operations-management.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-science-food-science.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-laws-international-governance.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/executive-master-of-business-administration.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-property-investment-and-development.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-professional-accounting.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-human-resource-management.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-arts-tesol.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-health-science-health-services-management.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-chinese-medicine.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-interpreting-and-translation.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-arts-in-literature-and-creative-writing.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-arts-in-continental-philosophy.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-arts-translation-and-interpreting-studies.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-nursing.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-nursing-professional-studies.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-translation-and-tesol.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-teaching-birth-5-years-birth-12-years.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-teaching-secondary.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-teaching-primary.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-epidemiology.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-teaching-secondary-stem.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-education-leadership-and-management.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-data-science.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-accountancy.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-finance.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-accountancy.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-information-and-communications-technology-advanced.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-business-administration.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-business-administration.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-information-governance.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-information-and-communications-technology.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-psychotherapy-and-counselling.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-information-and-communications-technology.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-health-science-aged-care-management.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-health-science-aged-care-management.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-social-science.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-accountancy.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-social-science-development-security-and-sustainability.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-accountancy.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-social-science-difference-and-diversity.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-social-science-digital-research-and-social-data-analytics.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-social-science-international-criminology.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-engineering.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-engineering.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-social-science-religion-and-society.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-urban-management-and-planning.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-engineering.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-engineering.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-social-work-qualifying.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-creative-industries.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-engineering.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-engineering.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-planning.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-management.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-art-therapy.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-creative-music-therapy.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-business-analytics.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-digital-humanities.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-sciencepublichealthnutrition.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-international-criminology.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-humanitarian-and-development-studies.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-marketing.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-project-management.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-chinese-cultural-relations.html',
        'https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-social-science--policing-leadership-.html'
    ]
    C = set(C)
    # print(len(C))
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Western Sydney University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.degree_name
        degree_name = response.xpath('//*[@id="wrapper"]/div/div[3]//div[2]/h1').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #4.duration
        duration = response.xpath('//*[@id="wrapper"]/div/div[3]/div/div[2]//div[1]/div/div[2]/div[2]/div/div[1]/div[2]').extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        duration = clear_space_str(duration).replace('FULL TIME','')
        # print(duration)

        #5.degree_overview_en
        degree_overview_en = response.xpath('//*[@id="wrapper"]/div/div[3]/div/div[2]//div[1]/div/div[1]/p').extract()
        degree_overview_en = ''.join(degree_overview_en)
        degree_overview_en = remove_class(degree_overview_en)
        # print(degree_overview_en)

        #6.start_date
        start_date = response.xpath('//*[@id="wrapper"]/div/div[3]/div/div[2]//div[1]/div/div[2]/div[2]/div/div[2]').extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        start_date = clear_space_str(start_date)
        if 'Start timesQ1January(2018)Q2April(2018)Q3June(2018)Q4September(2018)' in start_date:
            start_date = '1,4,6,9'
        elif 'Start timesAutumnMarch(2018)SpringJuly(2018)' in start_date:
            start_date = '3,7'
        elif 'Start timesQ1(2018)Q2(2018)Q3(2018)Q4(2018)' in start_date:
            start_date = ''
        elif 'Start timesAutumnFebruary(2018)SpringJuly(2018)' in start_date:
            start_date = '2,7'
        elif 'Start timesAutumnMarch(2018)' in start_date:
            start_date = '3'
        elif 'Start times1HJanuary(2018)2HJune(2018)' in start_date:
            start_date = '1,6'
        elif 'Start times1HJanuary(2018)SpringJuly(2018)' in start_date:
            start_date = '1,7'
        elif 'Start timesQ3June(2018)Q4September(2018)' in start_date:
            start_date = '6,9'
        elif 'Start timesQ2April(2018)Q3June(2018)Q4September(2018)' in start_date:
            start_date = '4,6,9'
        elif 'Start timesSpringJuly(2018)' in start_date:
            start_date = '7'
        # print(start_date)

        #7.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'Fee')]//..").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #8.tuition_fee_pre
        tuition_fee_pre = 'AU$'

        #9.apply_pre
        apply_pre = 'AU$'

        #10.location
        location = response.xpath('//div/a/div/div/h3').extract()
        location = ','.join(location)
        location = remove_tags(location)
        location = clear_space_str(location)
        # print(location)

        #11.career_en
        career_en = response.xpath("//*[contains(text(),'Your career')]/../following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #12.degree_type
        degree_type = 2

        #13.modules_en
        modules_en_url = response.xpath("//h3[contains(text(),'Course structure')]/../../following-sibling::*//@href").extract()
        modules_en_url = ''.join(modules_en_url)
        if len(modules_en_url) != 0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            try:
                data = requests.get(modules_en_url, headers=headers)
                response_modules_en = etree.HTML(data.text)
                # print(response_modules_en)
                modules_en = response_modules_en.xpath('//*[@id="hbcontent"]/table//td/span')
                doc = ""
                if len(modules_en) > 0:
                    for a in modules_en:
                        doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                        doc = remove_class(doc)
                        modules_en = doc
                else:
                    modules_en = None
            except:
                modules_en = None
        else:
            modules_en = None
            # print(modules_en)

        #14.apply_fee
        apply_fee = 68

        #15.programme_en
        if 'Executive Master of ' in degree_name:
            programme_en = degree_name.replace('Executive Master of ','')
        elif 'Master of ' in degree_name:
            programme_en = degree_name.replace('Master of ','')
        elif 'Masters ' in degree_name:
            programme_en = degree_name.replace('Masters ','')
        else:programme_en =degree_name
        if '(Secondary)' in programme_en:
            programme_en = programme_en
        elif '(Advanced)' in programme_en:
            programme_en = programme_en
        elif '(Birth-5 Years/Birth-12 Years)' in programme_en:
            programme_en = programme_en
        elif '(Qualifying)' in programme_en:
            programme_en = programme_en
        elif '(Primary)' in programme_en:
            programme_en = programme_en
        elif '(' in programme_en:
            programme_en = re.findall(r'\((.*)\)',programme_en)[0]
        if 'Arts in ' in programme_en:
            programme_en = programme_en.replace('Arts in ','')
        elif 'Arts ' in programme_en:
            programme_en = programme_en.replace('Arts ','')
        # print(degree_name,'*****',programme_en)

        #16.ielts 17181920 #21.toefl 22232425
        if 'Master of Teaching' in degree_name:
            ielts = 7.5
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_s = 8.0
            ielts_l = 8.0
            toefl = 105
            toefl_w = 24
            toefl_s = 26
            toefl_r = 13
            toefl_l = 13
        elif 'Master of Social Work' in degree_name:
            ielts = 7.0
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_s = 6.5
            ielts_l = 6.5
            toefl = 100
            toefl_w = 24
            toefl_r = 22
            toefl_l = 22
            toefl_s = 22
        elif 'Master of Clinical Psychology' in degree_name:
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_s = 7.0
            ielts_l = 7.0
            toefl = 100
            toefl_w = 27
            toefl_r = 22
            toefl_l = 22
            toefl_s = 22
        else:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
            toefl = 82
            toefl_w = 21
            toefl_r = 13
            toefl_l = 13
            toefl_s = 18


        #26.average_score
        average_score = 70

        #27.rntry_requirements_en
        modules_en_url = response.xpath('//*[@id="wrapper"]/div/div[3]/div/div[5]/div/div/div/div/div[2]/div/p/a//@href').extract()
        modules_en_url = ''.join(modules_en_url)
        if len(modules_en_url) != 0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data2 = requests.get(modules_en_url, headers=headers)
            response_rntry_requirements_en = etree.HTML(data2.text)
            # print(response_modules_en)
            rntry_requirements_en = response_rntry_requirements_en.xpath("//span[contains(text(),'Admission')]/../following-sibling::p[position()<5]//text()")
            rntry_requirements_en = ' '.join(rntry_requirements_en)
            rntry_requirements_en = '<p>' + rntry_requirements_en + '</p>'
        else:rntry_requirements_en = 'N/A'
            # print(rntry_requirements_en,modules_en_url)

        #28.apply_documents_en

        apply_documents_en = '本科毕业证 本科学位证 本科在读证明 本科成绩单 护照 语言成绩 个人简历(可选) 个人陈述(可选) 推荐信(可选) 工作经验证明(可选) 作品集(可选)'

        #29.apply_desc_en
        apply_desc_en = '"International students can apply direct to Western Sydney University. Apply early! As a guide you should apply by 15th November for courses commencing in the Autumn Session (February/March) and by 15th May for courses commencing in the Spring Session (July/August).Apply Online For a fast and efficient service apply online  (opens in new window) .Apply via an agent You may submit all completed forms and certified documents through an authorised agent representative of the University."'

        #30.overview_en
        overview_en = ''

        item['university'] = university
        item['url'] = url
        item['degree_name'] = degree_name
        item['duration'] = duration
        item['degree_overview_en'] = degree_overview_en
        item['start_date'] = start_date
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_pre'] = apply_pre
        item['location'] = location
        item['career_en'] = career_en
        item['degree_type'] = degree_type
        item['modules_en'] = modules_en
        item['apply_fee'] = apply_fee
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['toefl_l'] = toefl_l
        item['toefl_s'] = toefl_s
        item['average_score'] = average_score
        item['rntry_requirements_en'] = rntry_requirements_en
        item['apply_documents_en'] = apply_documents_en
        item['apply_desc_en'] = apply_desc_en

        if url =='https://www.westernsydney.edu.au/future/study/courses/postgraduate/master-of-engineering.html':
            major = response.xpath('//select//option').extract()
            for i in major[1:7]:
                major = i
                major = re.findall(r'>(.*)</option>',major)[0]
                major = major.capitalize()
                if 'Civil' in major:
                    overview_en = 'Civil engineering covers the fields of structural design, geotechnical engineering and water engineering, together with infrastructure design and environmental engineering. Graduates will work in the fields of design, construction and management of engineering structures. Projects may cover residential and commercial buildings, highways and airports, water supply and sewerage schemes, etc. You may be an engineer in private industry, government departments, or in city, municipal or shire councils.'
                elif 'Electrical' in major:
                    overview_en = 'This program includes core subjects from all branches of electrical engineering. Graduates will work in the fields of electronic components, computers, electro-magnetics, power generation and distribution systems, power and control in public utilities, telecommunications, manufacturing, and electrical systems.'
                elif 'Mechanical' in major:
                    overview_en = 'In addition to providing training in conventional mechanical engineering subjects, the course structure introduces students to units of study that address sustainability including sustainable design and sustainable energy engineering. Graduates will be well equipped with broad-based skills that meet the demand of Australian industries and are conscious of the need to promote sustainable design and practices. Examples include mechanical and machinery design; manufacturing; energy production; and marketing and management activities. Skills gained are required in industries such as manufacturing, materials handling, automobile, aerospace, mining, building services and infrastructure development.'
                elif 'Mechatronic' in major:
                    overview_en = 'Mechatronics (and robotics) provides the skills necessary for the design of smart machines of all types: cruise control in automobiles, pilotless spacecraft, automated factories and medical telerobotics. The course, accompanied by an extensive and integrated hands-on laboratory program, is essentially concerned with the design of intelligent mechanical systems and automation, and includes the study of robotics, computer control, automated manufacturing, microprocessor applications and machine design. Graduates in the program acquire the combined skills of mechanical and computer/electrical engineering that are needed in leading-edge industries such as aerospace systems, the car industry, automation and robotic applications, biomedical engineering, laser systems, and building materials manufacture.'
                elif 'Telecommunication' in major:
                    overview_en = 'Recent advances in computer and telecommunications networked systems have increased the importance of network technologies in the discipline of computer science. This major gives you a thorough technical understanding of modern networked computer systems, how they work and the principles that govern them.'
                elif 'Environmental' in major:
                    overview_en = 'In the Environmental specialisation you will study Sustainable systems, Advanced Waste Management, Advanced Water and Wastewater Treatment, Sustainability and Risk Engineering, Planning and Environmental Regulation, Safety and Risk Management, Building in Bushfire Prone Areas'
                item['programme_en'] = major
                item['overview_en'] = overview_en
                yield item
        else:
            item['programme_en'] = programme_en
            item['overview_en'] = overview_en
            yield item