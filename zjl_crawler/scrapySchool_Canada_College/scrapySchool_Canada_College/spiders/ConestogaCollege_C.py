# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/12/19 11:42'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.getItem import get_item
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from lxml import etree
import requests
class ConestogaCollege_CSpider(scrapy.Spider):
    name = 'ConestogaCollege_C'
    allowed_domains = ['conestogac.on.ca/']
    start_urls = []
    C= [
        'https://www.conestogac.on.ca/fulltime/bachelor-of-business-administration-honours-accounting-audit-and-information-technology',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-applied-health-information-science-honours',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-applied-technology-honours-architecture-project-and-facility-management',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-applied-health-information-science-honours',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-applied-technology-honours-architecture-project-and-facility-management',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-business-administration-honours-accounting-audit-and-information-technology',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-business-administration-honours-international-business-management',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-community-and-criminal-justice-honours',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-design-honours',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-early-learning-program-development-honours',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-engineering-building-systems-engineering',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-engineering-electronic-systems-engineering',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-engineering-mechanical-systems-engineering',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-engineering-power-systems-engineering',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-environmental-public-health-honours',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-interior-design-honours',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-public-relations-honours',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-engineering-building-systems-engineering',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-community-and-criminal-justice-honours',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-design-honours',
        'https://www.conestogac.on.ca/fulltime/diploma-registered-practical-nurse-to-b-sc-n--mcmaster',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-early-learning-program-development-honours',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-engineering-electronic-systems-engineering',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-environmental-public-health-honours',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-interior-design-honours',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-business-administration-honours-international-business-management',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-engineering-mechanical-systems-engineering',
        'https://www.conestogac.on.ca/fulltime/nursing-bscn-mcmaster',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-engineering-power-systems-engineering',
        'https://www.conestogac.on.ca/fulltime/bachelor-of-public-relations-honours',
        'https://www.conestogac.on.ca/fulltime/architecture-construction-engineering-technology',
        'https://www.conestogac.on.ca/fulltime/business-administration-accounting',
        'https://www.conestogac.on.ca/fulltime/business-administration-accounting-accelerated',
        'https://www.conestogac.on.ca/fulltime/business-administration-financial-planning',
        'https://www.conestogac.on.ca/fulltime/business-administration-management',
        'https://www.conestogac.on.ca/fulltime/business-administration-marketing',
        'https://www.conestogac.on.ca/fulltime/business-administration-marketing-co-op',
        'https://www.conestogac.on.ca/fulltime/business-administration-supply-chain-and-operations-management',
        'https://www.conestogac.on.ca/fulltime/business-administration-supply-chain-and-operations-management-co-op',
        'https://www.conestogac.on.ca/fulltime/civil-engineering-technology',
        'https://www.conestogac.on.ca/fulltime/computer-engineering-technology',
        'https://www.conestogac.on.ca/fulltime/computer-programmer-analyst',
        'https://www.conestogac.on.ca/fulltime/electrical-engineering-technology',
        'https://www.conestogac.on.ca/fulltime/electronics-engineering-technology',
        'https://www.conestogac.on.ca/fulltime/energy-systems-engineering-technology-electrical',
        'https://www.conestogac.on.ca/fulltime/environmental-civil-engineering-technology',
        'https://www.conestogac.on.ca/fulltime/graphic-design',
        'https://www.conestogac.on.ca/fulltime/it-innovation-and-design',
        'https://www.conestogac.on.ca/fulltime/manufacturing-engineering-technology-welding-and-robotics',
        'https://www.conestogac.on.ca/fulltime/mechanical-engineering-technology-automated-manufacturing',
        'https://www.conestogac.on.ca/fulltime/mechanical-engineering-technology-design-and-analysis',
        'https://www.conestogac.on.ca/fulltime/mechanical-engineering-technology-robotics-and-automation',
        'https://www.conestogac.on.ca/fulltime/respiratory-therapy',
        'https://www.conestogac.on.ca/fulltime/software-engineering-technology',
        'https://www.conestogac.on.ca/fulltime/welding-engineering-technology-inspection',
        'https://www.conestogac.on.ca/fulltime/woodworking-technology',
        'https://www.conestogac.on.ca/fulltime/advertising-and-marketing-communications',
        'https://www.conestogac.on.ca/fulltime/animation',
        'https://www.conestogac.on.ca/fulltime/aviation-general-arts-and-science',
        'https://www.conestogac.on.ca/fulltime/aviation-general-arts-and-science-fast-track',
        'https://www.conestogac.on.ca/fulltime/biotechnology-technician',
        'https://www.conestogac.on.ca/fulltime/biotechnology-technician-fast-track',
        'https://www.conestogac.on.ca/fulltime/broadcast-radio',
        'https://www.conestogac.on.ca/fulltime/broadcasting-television-and-independent-production',
        'https://www.conestogac.on.ca/fulltime/business',
        'https://www.conestogac.on.ca/fulltime/business-finance',
        'https://www.conestogac.on.ca/fulltime/business-marketing',
        'https://www.conestogac.on.ca/fulltime/business-marketing-accelerated',
        'https://www.conestogac.on.ca/fulltime/business-purchasing',
        'https://www.conestogac.on.ca/fulltime/carpentry-and-renovation-technician',
        'https://www.conestogac.on.ca/fulltime/computer-programmer',
        'https://www.conestogac.on.ca/fulltime/culinary-management-co-op',
        'https://www.conestogac.on.ca/fulltime/early-childhood-education',
        'https://www.conestogac.on.ca/fulltime/early-childhood-education-fast-track-ece',
        'https://www.conestogac.on.ca/fulltime/educational-support',
        'https://www.conestogac.on.ca/fulltime/electrical-engineering-technician',
        'https://www.conestogac.on.ca/fulltime/electrical-technician-industrial',
        'https://www.conestogac.on.ca/fulltime/electro-mechanical-maintenance',
        'https://www.conestogac.on.ca/fulltime/electronics-engineering-technician',
        'https://www.conestogac.on.ca/fulltime/fitness-and-health-promotion',
        'https://www.conestogac.on.ca/fulltime/food-processing-technician',
        'https://www.conestogac.on.ca/fulltime/game-design',
        'https://www.conestogac.on.ca/fulltime/general-arts-and-science-diploma-option',
        'https://www.conestogac.on.ca/fulltime/health-office-administration',
        'https://www.conestogac.on.ca/fulltime/hearing-instrument-specialist',
        'https://www.conestogac.on.ca/fulltime/heating-refrigeration-and-air-conditioning-technician',
        'https://www.conestogac.on.ca/fulltime/hospitality-and-tourism-management',
        'https://www.conestogac.on.ca/fulltime/information-technology-support-services',
        'https://www.conestogac.on.ca/fulltime/insurance-property-and-casualty',
        'https://www.conestogac.on.ca/fulltime/interior-decorating',
        'https://www.conestogac.on.ca/fulltime/journalism',
        'https://www.conestogac.on.ca/fulltime/mechanical-engineering-technician-automated-manufacturing',
        'https://www.conestogac.on.ca/fulltime/mechanical-technician-cnc',
        'https://www.conestogac.on.ca/fulltime/mechanical-technician-general-machinist',
        'https://www.conestogac.on.ca/fulltime/mechanical-technician-tool-and-die-tool-maker',
        'https://www.conestogac.on.ca/fulltime/motive-power-technician-automotive-service',
        'https://www.conestogac.on.ca/fulltime/motive-power-technician-heavy-duty-equipment',
        'https://www.conestogac.on.ca/fulltime/motive-power-technician-truck-and-coach',
        'https://www.conestogac.on.ca/fulltime/nutrition-and-food-service-management',
        'https://www.conestogac.on.ca/fulltime/occupational-therapist-assistant-physiotherapist-assistant',
        'https://www.conestogac.on.ca/fulltime/office-administration-executive',
        'https://www.conestogac.on.ca/fulltime/office-administration-legal',
        'https://www.conestogac.on.ca/fulltime/packaging-engineering-technician',
        'https://www.conestogac.on.ca/fulltime/paramedic',
        'https://www.conestogac.on.ca/fulltime/police-foundations',
        'https://www.conestogac.on.ca/fulltime/powerline-technician',
        'https://www.conestogac.on.ca/fulltime/practical-nursing',
        'https://www.conestogac.on.ca/fulltime/protection-security-and-investigation',
        'https://www.conestogac.on.ca/fulltime/public-relations',
        'https://www.conestogac.on.ca/fulltime/recreation-and-leisure-services',
        'https://www.conestogac.on.ca/fulltime/recreation-and-leisure-services-fast-track',
        'https://www.conestogac.on.ca/fulltime/social-service-worker',
        'https://www.conestogac.on.ca/fulltime/software-engineering-technician',
        'https://www.conestogac.on.ca/fulltime/visual-merchandising-arts',
        'https://www.conestogac.on.ca/fulltime/welding-and-fabrication-technician',
        'https://www.conestogac.on.ca/fulltime/woodworking-technician',
        'https://www.conestogac.on.ca/fulltime/administrative-business-management',
        'https://www.conestogac.on.ca/fulltime/advanced-police-studies',
        'https://www.conestogac.on.ca/fulltime/applied-electrical-motion-and-control-management',
        'https://www.conestogac.on.ca/fulltime/applied-energy-management',
        'https://www.conestogac.on.ca/fulltime/applied-manufacturing-management',
        'https://www.conestogac.on.ca/fulltime/applied-network-infrastructure-and-system-administration',
        'https://www.conestogac.on.ca/fulltime/autism-and-behavioural-science',
        'https://www.conestogac.on.ca/fulltime/big-data-solution-architecture',
        'https://www.conestogac.on.ca/fulltime/broadcasting-performance-and-digital-media',
        'https://www.conestogac.on.ca/fulltime/business-development-and-sales',
        'https://www.conestogac.on.ca/fulltime/career-development-professional',
        'https://www.conestogac.on.ca/fulltime/community-and-social-service-management',
        'https://www.conestogac.on.ca/fulltime/computer-application-security',
        'https://www.conestogac.on.ca/fulltime/computer-applications-development',
        'https://www.conestogac.on.ca/fulltime/construction-management',
        'https://www.conestogac.on.ca/fulltime/construction-project-management',
        'https://www.conestogac.on.ca/fulltime/embedded-systems-development',
        'https://www.conestogac.on.ca/fulltime/enhanced-nursing-practice-clinical-and-critical-care',
        'https://www.conestogac.on.ca/fulltime/enhanced-professional-practice-gerontology-and-chronic-illness',
        'https://www.conestogac.on.ca/fulltime/enterprise-content-management',
        'https://www.conestogac.on.ca/fulltime/entrepreneurship-management',
        'https://www.conestogac.on.ca/fulltime/environmental-building-sciences',
        'https://www.conestogac.on.ca/fulltime/environmental-engineering-applications',
        'https://www.conestogac.on.ca/fulltime/event-management',
        'https://www.conestogac.on.ca/fulltime/financial-planning-services',
        'https://www.conestogac.on.ca/fulltime/food-safety-and-quality-assurance-food-processing',
        'https://www.conestogac.on.ca/fulltime/global-business-management',
        'https://www.conestogac.on.ca/fulltime/global-hospitality-management',
        'https://www.conestogac.on.ca/fulltime/health-care-administration-and-service-management',
        'https://www.conestogac.on.ca/fulltime/human-resources-management',
        'https://www.conestogac.on.ca/fulltime/information-technology-business-analysis-operations',
        'https://www.conestogac.on.ca/fulltime/information-technology-network-security',
        'https://www.conestogac.on.ca/fulltime/integrated-marketing-communications',
        'https://www.conestogac.on.ca/fulltime/interactive-media-management-interaction-design',
        'https://www.conestogac.on.ca/fulltime/mental-health-and-substance-abuse-at-risk-populations',
        'https://www.conestogac.on.ca/fulltime/mobile-solutions-development',
        'https://www.conestogac.on.ca/fulltime/occupational-health-safety-and-wellness',
        'https://www.conestogac.on.ca/fulltime/operations-leadership-in-food-manufacturing',
        'https://www.conestogac.on.ca/fulltime/paralegal',
        'https://www.conestogac.on.ca/fulltime/process-quality-engineering',
        'https://www.conestogac.on.ca/fulltime/project-management',
        'https://www.conestogac.on.ca/fulltime/public-service',
        'https://www.conestogac.on.ca/fulltime/robotics-and-industrial-automation',
        'https://www.conestogac.on.ca/fulltime/social-media-marketing',
        'https://www.conestogac.on.ca/fulltime/software-quality-assurance-and-test-engineering',
        'https://www.conestogac.on.ca/fulltime/structural-packaging-design-and-management',
        'https://www.conestogac.on.ca/fulltime/structural-steel-management-and-detailing',
        'https://www.conestogac.on.ca/fulltime/supply-chain-management-global',
        'https://www.conestogac.on.ca/fulltime/sustainable-business-management',
        'https://www.conestogac.on.ca/fulltime/teaching-english-as-a-second-language-tesl',
        'https://www.conestogac.on.ca/fulltime/web-design-and-development',
        'https://www.conestogac.on.ca/fulltime/wireless-network-infrastructure',
        'https://www.conestogac.on.ca/fulltime/food-and-beverage-management-hotel-and-restaurant-operations--co-op-formerly-hospitality-management-hotel-and-restaurant-D'
    ]
    C = set(C)
    for i in C:
        start_urls.append(i)

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaCollegeItem)

        #1.school_name
        school_name = 'Conestoga College'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.location
        location = 'Ontario, Canada'

        #4.major_name_en
        major_name_en = response.xpath('//*[@id="maincontent"]/h1').extract()
        major_name_en = ''.join(major_name_en)
        major_name_en = remove_tags(major_name_en).strip()
        # print(major_name_en)

        #5.degree_name #6.degree_level
        degree_name = response.xpath("//dt[contains(text(),'Credential:')]//following-sibling::dd[1]").extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        if 'Advanced Diploma' in degree_name:
            degree_name = 'Advanced Diploma'
            degree_level = 3
        elif 'Graduate Certificate' in degree_name:
            degree_name = 'Graduate Certificate'
            degree_level = 2
        elif 'Diploma' in degree_name:
            degree_name = 'Diploma'
            degree_level = 3
        else:
            degree_name = degree_name
            degree_level = 1
        # print(degree_name)

        #7.campus
        campus = response.xpath("//*[@id='program-status']/table//tr[2]/td[2]").extract()
        campus = ''.join(campus)
        campus = remove_tags(campus).strip()
        # print(campus,url)

        #8.programme_code
        programme_code = response.xpath("//dt[contains(text(),'Program Code:')]//following-sibling::*[1]").extract()
        programme_code = ''.join(programme_code)
        programme_code = remove_tags(programme_code).strip()
        # print(programme_code)

        #9.department
        department = response.xpath("//dt[contains(text(),'School:')]//following-sibling::*[1]").extract()
        department = ''.join(department)
        department = remove_tags(department).replace('&amp; ','')
        # print(department)

        #10.start_date
        start_date = response.xpath('//*[@id="program-status"]/table//tr/td[1]').extract()
        start_date = ''.join(start_date).strip()
        start_date = remove_tags(start_date)
        start_date = clear_space_str(start_date)
        start_date = re.findall('[A-Z]{3},\s\d+',start_date)
        start_date = ','.join(start_date).replace('\xa0','').replace('JAN,2019','2019-01').replace('MAY,2019','2019-05').replace('SEP,2019','2019-09').replace('JAN,2020','2020-01').replace('MAY,2020','2020-05')
        start_date = start_date.replace('AUG,2019','2019-08')
        # print(start_date)

        #11.overview_en
        overview_en_a = response.xpath('//*').extract()
        overview_en_a = ''.join(overview_en_a)
        # print(overview_en_a)
        overview_en = re.findall('<h2[\sA-Za-z\'\"=><-]+About the Program</h2>\s(.*?)\s <!-- The follow session is for program content information -->',overview_en_a,re.S)[0]
        overview_en = remove_class(overview_en).replace('\t','').replace('\r','').replace('\n','')
        # print(overview_en,url)

        #12.modules_en
        modules_en = response.xpath('//*[@id="pc-noncoop"]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #13.career_en
        career_en =  response.xpath("//*[contains(text(),'Program Outcomes')]//following-sibling::*[1]").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #14.tuition_fee
        tuition_fee = 6000

        #15.tuition_fee_pre
        tuition_fee_pre = '$'

        #16.entry_requirements_en
        entry_requirements_en = response.xpath("//*[contains(text(),'Admission Requirements')]//following-sibling::*[1]").extract()
        entry_requirements_en = ''.join(entry_requirements_en)
        entry_requirements_en = remove_class(entry_requirements_en)
        # print(entry_requirements_en)

        #17.specific_requirement_en
        specific_requirement_en = response.xpath("//*[contains(text(),'Program Requirements')]//following-sibling::*[1]").extract()
        specific_requirement_en = ''.join(specific_requirement_en)
        specific_requirement_en = remove_class(specific_requirement_en)
        # print(specific_requirement_en)

        #18.ielts_desc 19.toefl_desc 20-25
        ielts_desc = '<p>DIPLOMA/CERTIFICATE (EXCLUDING Practical Nursing Diploma) 6.0 IELTS (with no band less than 5.5) 80 TOEFL DEGREE (INCLUDING Practical Nursing Diploma) 6.5 IELTS (with no band less than 6.0)  88 TOEFL GRADUATE CERTIFICATE (Some IT/engineering program required test scores may vary)6.5 IELTS (with no band less than 6.0) 88 TOEFL</p>'
        toefl_desc = ielts_desc
        if degree_level == 1:
            ielts = 6.5
            ielts_r = 6
            ielts_w = 6
            ielts_s = 6
            ielts_l = 6
            toefl = 88
        elif degree_level ==2:
            ielts = 6.5
            ielts_r = 6
            ielts_w = 6
            ielts_s = 6
            ielts_l = 6
            toefl = 88
        else:
            ielts = 6
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
            toefl = 80

        item['school_name'] = school_name
        item['url'] = url
        item['location'] = location
        item['major_name_en'] = major_name_en
        item['degree_name'] = degree_name
        item['degree_level'] = degree_level
        item['campus'] = campus
        item['programme_code'] = programme_code
        item['department'] = department
        item['start_date'] = start_date
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['entry_requirements_en'] = entry_requirements_en
        item['specific_requirement_en'] = specific_requirement_en
        item['ielts_desc'] = ielts_desc
        item['toefl_desc'] = toefl_desc
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl'] = toefl
        yield item