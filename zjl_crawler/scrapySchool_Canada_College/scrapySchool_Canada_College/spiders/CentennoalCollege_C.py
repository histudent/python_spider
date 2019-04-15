# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/12/19 9:35'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.getItem import get_item
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from lxml import etree
import requests
class CentennoalCollege_CSpider(scrapy.Spider):
    name = 'CentennoalCollege_C'
    allowed_domains = ['centennialcollege.ca/']
    start_urls = []
    C= [
        'https://www.centennialcollege.ca/programs-courses/full-time/advertising-and-marketing-communications-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/aerospace-manufacturing-engineering-technology/',
        'https://www.centennialcollege.ca/programs-courses/full-time/architectural-technology-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/architectural-technology/',
        'https://www.centennialcollege.ca/programs-courses/full-time/aviation-technology-aircraft-maintenance-mgmt/',
        'https://www.centennialcollege.ca/programs-courses/full-time/aviation-technology-avionics-maintenance-mgmt/',
        'https://www.centennialcollege.ca/programs-courses/full-time/biomedical-engineering-technology-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/biomedical-engineering-technology/',
        'https://www.centennialcollege.ca/programs-courses/full-time/biotechnology-advanced-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/biotechnology-advanced/',
        'https://www.centennialcollege.ca/programs-courses/full-time/radio-television-film-digital-media/',
        'https://www.centennialcollege.ca/programs-courses/full-time/business-administration-leadership-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/business-operations-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/business-administration-accounting-3-semesters/',
        'https://www.centennialcollege.ca/programs-courses/full-time/business-administration-accounting/',
        'https://www.centennialcollege.ca/programs-courses/full-time/business-administration-finance/',
        'https://www.centennialcollege.ca/programs-courses/full-time/business-human-resources/',
        'https://www.centennialcollege.ca/programs-courses/full-time/business-administration-international-business/',
        'https://www.centennialcollege.ca/programs-courses/full-time/business-administration-marketing/',
        'https://www.centennialcollege.ca/programs-courses/full-time/child-youth-care/',
        'https://www.centennialcollege.ca/programs-courses/full-time/computer-systems-technology-networking-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/computer-systems-technology-networking/',
        'https://www.centennialcollege.ca/programs-courses/full-time/electrical-engineering-technology/',
        'https://www.centennialcollege.ca/programs-courses/full-time/electrical-engineering-technology-1/',
        'https://www.centennialcollege.ca/programs-courses/full-time/automation-and-robotics-technology-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/automation-and-robotics-technology/',
        'https://www.centennialcollege.ca/programs-courses/full-time/electronics-engineering-technology-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/electronics-engineering-technology/',
        'https://www.centennialcollege.ca/programs-courses/full-time/energy-systems-engineering-technology-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/energy-systems-engineering-technology/',
        'https://www.centennialcollege.ca/programs-courses/full-time/environmental-technology-coop/',
        'https://www.centennialcollege.ca/programs-courses/full-time/environmental-technology-fast-track-coop/',
        'https://www.centennialcollege.ca/programs-courses/full-time/environmental-technology-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/environmental-technology/',
        'https://www.centennialcollege.ca/programs-courses/full-time/food-science-technology-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/food-science-technology/',
        'https://www.centennialcollege.ca/programs-courses/full-time/game-development/',
        'https://www.centennialcollege.ca/programs-courses/full-time/game-programming-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/game-programming/',
        'https://www.centennialcollege.ca/programs-courses/full-time/graphic-design/',
        'https://www.centennialcollege.ca/programs-courses/full-time/health-informatics-technology-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/health-informatics-technology/',
        'https://www.centennialcollege.ca/programs-courses/full-time/hospitality-tourism-administration/',
        'https://www.centennialcollege.ca/programs-courses/full-time/journalism/',
        'https://www.centennialcollege.ca/programs-courses/full-time/massage-therapy/',
        'https://www.centennialcollege.ca/programs-courses/full-time/massage-therapy-compressed/',
        'https://www.centennialcollege.ca/programs-courses/full-time/mechanical-engineering-technology-design-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/mechanical-engineering-technology-design/',
        'https://www.centennialcollege.ca/programs-courses/full-time/mechanical-engineering-technology-industrial-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/mechanical-engineering-technology-industrial/',
        'https://www.centennialcollege.ca/programs-courses/full-time/music-industry-arts-performance/',
        'https://www.centennialcollege.ca/programs-courses/full-time/product-design-and-development/',
        'https://www.centennialcollege.ca/programs-courses/full-time/software-engineering-technology-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/software-engineering-technology/',
        'https://www.centennialcollege.ca/programs-courses/full-time/theatre-arts-performance/',
        'https://www.centennialcollege.ca/programs-courses/full-time/bachelor-of-information-technology/',
        'https://www.centennialcollege.ca/programs-courses/full-time/bachelor-public-relations-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/nursing-bscn/',
        'https://www.centennialcollege.ca/programs-courses/full-time/addiction-mental-health-worker/',
        'https://www.centennialcollege.ca/programs-courses/full-time/aerospace-manufacturing-engineering-technician/',
        'https://www.centennialcollege.ca/programs-courses/full-time/animation-3d/',
        'https://www.centennialcollege.ca/programs-courses/full-time/architectural-technician/',
        'https://www.centennialcollege.ca/programs-courses/full-time/auto-body-repair-technician/',
        'https://www.centennialcollege.ca/programs-courses/full-time/automotive-motive-power-technician-technical/',
        'https://www.centennialcollege.ca/programs-courses/full-time/automotive-parts-service-operations/',
        'https://www.centennialcollege.ca/programs-courses/full-time/automotive-service-technician-coop-apprenticeship-partnered-chrysler/',
        'https://www.centennialcollege.ca/programs-courses/full-time/automotive-service-technician-coop-diploma-apprenticeship-partnered-tada/',
        'https://www.centennialcollege.ca/programs-courses/full-time/aviation-technician-aircraft-maintenance/',
        'https://www.centennialcollege.ca/programs-courses/full-time/aviation-technician-avionics-maintenance/',
        'https://www.centennialcollege.ca/programs-courses/full-time/baking-pastry-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/biotechnology/',
        'https://www.centennialcollege.ca/programs-courses/full-time/biotechnology-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/business/',
        'https://www.centennialcollege.ca/programs-courses/full-time/business-international-business/',
        'https://www.centennialcollege.ca/programs-courses/full-time/business-operations/',
        'https://www.centennialcollege.ca/programs-courses/full-time/business-accounting/',
        'https://www.centennialcollege.ca/programs-courses/full-time/business-marketing/',
        'https://www.centennialcollege.ca/programs-courses/full-time/community-and-justice-services/',
        'https://www.centennialcollege.ca/programs-courses/full-time/community-development-work/',
        'https://www.centennialcollege.ca/programs-courses/full-time/computer-systems-technician-networking/',
        'https://www.centennialcollege.ca/programs-courses/full-time/computer-systems-technician-networking-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/culinary-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/dance-performance/',
        'https://www.centennialcollege.ca/programs-courses/full-time/developmental-services-worker/',
        'https://www.centennialcollege.ca/programs-courses/full-time/digital-visual-effects/',
        'https://www.centennialcollege.ca/programs-courses/full-time/early-childhood-education-ashtonbee/',
        'https://www.centennialcollege.ca/programs-courses/full-time/early-childhood-education-progress/',
        'https://www.centennialcollege.ca/programs-courses/full-time/electrical-engineering-technician/',
        'https://www.centennialcollege.ca/programs-courses/full-time/electrician-construction-maintenance-electrical-engineering-technician/',
        'https://www.centennialcollege.ca/programs-courses/full-time/automation-and-robotics-technician/',
        'https://www.centennialcollege.ca/programs-courses/full-time/automation-robotics-technician-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/electronics-engineering-technician/',
        'https://www.centennialcollege.ca/programs-courses/full-time/electronics-engineering-technician-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/energy-systems-engineering-technician/',
        'https://www.centennialcollege.ca/programs-courses/full-time/energy-systems-engineering-technician-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/environmental-technician/',
        'https://www.centennialcollege.ca/programs-courses/full-time/environmental-technician-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/esthetician/',
        'https://www.centennialcollege.ca/programs-courses/full-time/fashion-business-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/financial-services/',
        'https://www.centennialcollege.ca/programs-courses/full-time/fine-arts-studio/',
        'https://www.centennialcollege.ca/programs-courses/full-time/fitness-and-health-promotion/',
        'https://www.centennialcollege.ca/programs-courses/full-time/food-beverage-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/game-art/',
        'https://www.centennialcollege.ca/programs-courses/full-time/healthcare-environmental-services-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/heating-refrigeration-and-ac-technician/',
        'https://www.centennialcollege.ca/programs-courses/full-time/hospitality-hotel-operations-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/law-clerk/',
        'https://www.centennialcollege.ca/programs-courses/full-time/liberal-arts/',
        'https://www.centennialcollege.ca/programs-courses/full-time/liberal-arts-trent/',
        'https://www.centennialcollege.ca/programs-courses/full-time/liberal-arts-utsc/',
        'https://www.centennialcollege.ca/programs-courses/full-time/liberal-arts-york/',
        'https://www.centennialcollege.ca/programs-courses/full-time/mechanical-engineering-technician-design/',
        'https://www.centennialcollege.ca/programs-courses/full-time/mechanical-engineering-technician-design-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/heavy-duty-equipment-motive-power-technician/',
        'https://www.centennialcollege.ca/programs-courses/full-time/truck-and-coach-motive-power-technician/',
        'https://www.centennialcollege.ca/programs-courses/full-time/nutrition-and-food-service-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/occupational-therapist-assistant-physiotherapist-assistant/',
        'https://www.centennialcollege.ca/programs-courses/full-time/office-administration-executive/',
        'https://www.centennialcollege.ca/programs-courses/full-time/office-administration-health-services/',
        'https://www.centennialcollege.ca/programs-courses/full-time/office-administration-legal/',
        'https://www.centennialcollege.ca/programs-courses/full-time/paramedic/',
        'https://www.centennialcollege.ca/programs-courses/full-time/pharmacy-technician/',
        'https://www.centennialcollege.ca/programs-courses/full-time/photography/',
        'https://www.centennialcollege.ca/programs-courses/full-time/police-foundations/',
        'https://www.centennialcollege.ca/programs-courses/full-time/practical-nursing/',
        'https://www.centennialcollege.ca/programs-courses/full-time/practical-nursing-flexible/',
        'https://www.centennialcollege.ca/programs-courses/full-time/practical-nursing-internationally-educated-nurses/',
        'https://www.centennialcollege.ca/programs-courses/full-time/recreation-and-leisure-services/',
        'https://www.centennialcollege.ca/programs-courses/full-time/mechanic-heating-refrigeration-air-conditioning-technician/',
        'https://www.centennialcollege.ca/programs-courses/full-time/social-service-worker/',
        'https://www.centennialcollege.ca/programs-courses/full-time/software-engineering-technician/',
        'https://www.centennialcollege.ca/programs-courses/full-time/software-engineering-technician-fast-track/',
        'https://www.centennialcollege.ca/programs-courses/full-time/special-event-planning/',
        'https://www.centennialcollege.ca/programs-courses/full-time/tourism-travel/',
        'https://www.centennialcollege.ca/programs-courses/full-time/business-management-alcoholic-beverages/',
        'https://www.centennialcollege.ca/programs-courses/full-time/advanced-television-film-script-to-screen/',
        'https://www.centennialcollege.ca/programs-courses/full-time/advertising-account-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/advertising-creative-digital-strategy/',
        'https://www.centennialcollege.ca/programs-courses/full-time/advertising-media-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/aece/',
        'https://www.centennialcollege.ca/programs-courses/full-time/arts-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/bridging-to-university-nursing/',
        'https://www.centennialcollege.ca/programs-courses/full-time/bridging-to-university-nursing-flexible/',
        'https://www.centennialcollege.ca/programs-courses/full-time/bridging-to-university-nursing-ien/',
        'https://www.centennialcollege.ca/programs-courses/full-time/childrens-media/',
        'https://www.centennialcollege.ca/programs-courses/full-time/communications-professional-writing/',
        'https://www.centennialcollege.ca/programs-courses/full-time/construction-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/contemporary-journalism/',
        'https://www.centennialcollege.ca/programs-courses/full-time/cybersecurity/',
        'https://www.centennialcollege.ca/programs-courses/full-time/event-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/financial-planning/',
        'https://www.centennialcollege.ca/programs-courses/full-time/food-media/',
        'https://www.centennialcollege.ca/programs-courses/full-time/food-tourism/',
        'https://www.centennialcollege.ca/programs-courses/full-time/global-business-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/hotel-resort-and-restaurant-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/human-resources-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/insurance-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/interactive-media-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/international-business-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/international-business-management-transnational/',
        'https://www.centennialcollege.ca/programs-courses/full-time/international-development/',
        'https://www.centennialcollege.ca/programs-courses/full-time/arts-and-entertainment-journalism/',
        'https://www.centennialcollege.ca/programs-courses/full-time/lifestyle-media/',
        'https://www.centennialcollege.ca/programs-courses/full-time/marketing-corporate-account-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/marketing-digital-engagement-strategy/',
        'https://www.centennialcollege.ca/programs-courses/full-time/marketing-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/marketing-research-analytics/',
        'https://www.centennialcollege.ca/programs-courses/full-time/mobile-applications-development/',
        'https://www.centennialcollege.ca/programs-courses/full-time/museum-and-cultural-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/paralegal/',
        'https://www.centennialcollege.ca/programs-courses/full-time/project-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/project-mgmt/',
        'https://www.centennialcollege.ca/programs-courses/full-time/public-relations-corporate-communications/',
        'https://www.centennialcollege.ca/programs-courses/full-time/publishing-book-magazine-electronic/',
        'https://www.centennialcollege.ca/programs-courses/full-time/sports-journalism/',
        'https://www.centennialcollege.ca/programs-courses/full-time/strategic-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/strategic-management-pls/',
        'https://www.centennialcollege.ca/programs-courses/full-time/strategic-management-accounting/',
        'https://www.centennialcollege.ca/programs-courses/full-time/logistics-management/',
        'https://www.centennialcollege.ca/programs-courses/full-time/television-film-business/',
        'https://www.centennialcollege.ca/programs-courses/full-time/workplace-wellness-and-health-promotion/',
        'https://www.centennialcollege.ca/programs-courses/full-time/workplace-wellness-and-health-promotion-PLS/'
    ]
    for i in C:
        start_urls.append(i)

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaCollegeItem)

        #1.school_name
        school_name = 'Centennoal College'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.location
        location = 'Ontario, Canada'

        #4.major_name_en
        major_name_en = response.xpath('//*[@id="programBannerTitle"]').extract()
        major_name_en = ''.join(major_name_en)
        major_name_en = remove_tags(major_name_en).replace('&amp; ','')
        # print(major_name_en)

        #5.programme_code
        programme_code = response.xpath("//span[contains(text(),'Program Code:')]//following-sibling::*").extract()
        programme_code = ''.join(programme_code)
        programme_code = remove_tags(programme_code)
        # print(programme_code)

        #6.department
        department = response.xpath("//span[contains(text(),'School:')]//following-sibling::*").extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #7.degree_name
        degree_name = response.xpath("//span[contains(text(),'Credential:')]//following-sibling::*").extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #8.duration #9.duration_per
        duration = response.xpath("//span[contains(text(),'Program Length:')]//following-sibling::*").extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        if 'year' in duration:
            duration = re.findall('\d',duration)[0]
            duration_per = 1
        else:
            duration = re.findall('\d',duration)[0]
            duration_per = 2
        # print(duration,'####',duration_per)

        #10.start_date
        start_date = response.xpath("//span[contains(text(),'Start Date:')]//following-sibling::*").extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        if 'Fall, Winter, Summer' in start_date:
            start_date = '2019-01,2019-05,2019-09'
        elif 'Fall, Winter' in start_date:
            start_date = '2019-01,2019-09'
        else:
            start_date = '2019-09'
        # print(start_date)

        #11.campus
        campus = response.xpath("//span[contains(text(),'Location:')]//following-sibling::*").extract()
        campus = ''.join(campus)
        campus = remove_tags(campus)
        # print(campus)

        #12.overview_en
        overview_en = response.xpath("//div[@id='tab-1']").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en).replace('<span>Printer Friendly</span>','')
        # print(overview_en)

        #13.modules_en
        modules_en = response.xpath("//div[@id='tab-2']").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #14.career_en
        career_en = response.xpath("//div[@id='tab-3']").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #15.degree_level
        if 'Diploma' in degree_name:
            degree_level = 3
        elif 'Degree' in degree_name:
            degree_level = 1
        elif 'Graduate Certificate' in degree_name:
            degree_level = 2
        else:
            degree_level  = None
        #16.entry_requirements_en
        entry_requirements_en = response.xpath("//div[@id='tab-4']").extract()
        entry_requirements_en = ''.join(entry_requirements_en)
        entry_requirements_en = remove_class(entry_requirements_en).replace('<span>Printer Friendly</span>','')
        # print(entry_requirements_en)

        #17.tuition_fee
        tuition_fee = response.xpath("//td[contains(text(),'International')]//following-sibling::td[1]").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee).replace('$','').replace('.00','')
        # print(tuition_fee)

        #18.tuition_fee_pre
        tuition_fee_pre = '$'

        #19.deadline
        deadline = '2019-01-11,2019-05-10,2019-09-06'

        #20.toefl_desc 2122232425
        toefl_desc = 'Certificate and Diploma Programs *:80+ minimums of 20 for the Internet-based test,Degree and Diploma Programs **:84+ minimums of 21 for the Internet-based test,Other Programs ***:88+ minimums of 22 for the Internet based test'
        if 'Advanced Diploma' in degree_name:
            toefl = 84
            toefl_r = 21
            toefl_w = 21
            toefl_s = 21
            toefl_l = 21
        elif 'Degree' in degree_name:
            toefl = 84
            toefl_r = 21
            toefl_w = 21
            toefl_s = 21
            toefl_l = 21
        else:
            toefl = 80
            toefl_r = 20
            toefl_w = 20
            toefl_s = 20
            toefl_l = 20

        #26.ielts_desc 2728293031
        ielts_desc = 'Certificate and Diploma Programs *:6.0 with no band score less than 5.5,Degree and Diploma Programs **:6.5 with no band score less than 6.0'
        if 'Advanced Diploma' in degree_name:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_l = 6.0
            ielts_s = 6.0
        elif 'Degree' in degree_name:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_l = 6.0
            ielts_s = 6.0
        else:
            ielts = 6
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_l = 5.5
            ielts_s = 5.5

        #32other
        other = '1.degree_name是本科学位的需要修改。2.中国学生要求待确认'

        #33.apply_pre
        apply_pre = '$'

        #34.apply_fee
        apply_fee = 95

        item['school_name'] = school_name
        item['url'] = url
        item['location'] = location
        item['major_name_en'] = major_name_en
        item['programme_code'] = programme_code
        item['department'] = department
        item['degree_name'] = degree_name
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['start_date'] = start_date
        item['campus'] = campus
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['degree_level'] = degree_level
        item['entry_requirements_en'] = entry_requirements_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['deadline'] = deadline
        item['toefl_desc'] = toefl_desc
        item['toefl'] = toefl
        item['toefl_s'] = toefl_s
        item['toefl_w'] = toefl_w
        item['toefl_l'] = toefl_l
        item['toefl_r'] = toefl_r
        item['ielts_desc'] = ielts_desc
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['other'] = other
        item['apply_pre'] = apply_pre
        item['apply_fee'] = apply_fee
        yield item