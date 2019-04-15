# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/10/23 11:52'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from lxml import etree
import requests

class UniversityofPrinceEdwardIsland_USpider(scrapy.Spider):
    name = 'UniversityofPrinceEdwardIsland_U'
    allowed_domains = ['upei.ca/']
    start_urls = []
    C= [
        'http://upei.ca/programsandcourses/acadian-studies',
        'http://upei.ca/programsandcourses/sociologyanthropology',
        'http://www.upei.ca/programsandcourses/applied-communication-leadership-and-culture',
        'http://upei.ca/programsandcourses/arts-seminars',
        'http://upei.ca/programsandcourses/asian-studies',
        'http://upei.ca/programsandcourses/canadian-studies',
        'http://upei.ca/programsandcourses/classics',
        'http://upei.ca/programsandcourses/diversity-social-justice-studies',
        'http://upei.ca/programsandcourses/economics',
        'http://upei.ca/programsandcourses/english',
        'http://upei.ca/programsandcourses/fine-arts',
        'http://upei.ca/programsandcourses/french',
        'http://upei.ca/programsandcourses/german',
        'http://upei.ca/programsandcourses/History',
        'http://upei.ca/programsandcourses/integrated-studies',
        'http://upei.ca/programsandcourses/international-studies',
        'http://upei.ca/programsandcourses/applied-arts-journalism',
        'http://upei.ca/programsandcourses/modern-languages',
        'http://upei.ca/programsandcourses/music',
        'http://upei.ca/programsandcourses/bachelor-music',
        'http://upei.ca/programsandcourses/music-education',
        'http://upei.ca/programsandcourses/philosophy',
        'http://upei.ca/programsandcourses/political-science',
        'http://upei.ca/programsandcourses/psychology',
        'http://upei.ca/programsandcourses/religious-studies',
        'http://upei.ca/programsandcourses/sociologyanthropology',
        'http://upei.ca/programsandcourses/sociologyanthropology',
        'http://upei.ca/programsandcourses/spanish',
        'http://upei.ca/programsandcourses/theatre-studies',
        'http://upei.ca/programsandcourses/bachelor-business-administration',
        'http://upei.ca/programsandcourses/accounting',
        'http://upei.ca/programsandcourses/entrepreneurship',
        'http://upei.ca/programsandcourses/finance',
        'http://upei.ca/programsandcourses/international-business',
        'http://upei.ca/programsandcourses/marketing',
        'http://upei.ca/programsandcourses/organizational-management',
        'http://upei.ca/programsandcourses/tourism-and-hospitality',
        'http://upei.ca/programsandcourses/accelerated-bachelor-business-administration',
        'http://upei.ca/programsandcourses/bachelor-business-tourism-and-hospitality',
        'http://upei.ca/programsandcourses/bachelor-business-studies',
        'http://upei.ca/programsandcourses/bachelor-education',
        'http://upei.ca/programsandcourses/accelerated-nursing',
        'http://upei.ca/programsandcourses/nursing',
        'http://upei.ca/programsandcourses/applied-climate-change-and-adaptation',
        'http://upei.ca/programsandcourses/biology',
        'http://upei.ca/programsandcourses/biotechnology',
        'http://upei.ca/programsandcourses/chemistry',
        'http://upei.ca/programsandcourses/child-and-family-studies',
        'http://www.upei.ca/programsandcourses/mathematical-and-computational-sciences',
        'http://www.upei.ca/programsandcourses/dietetic-internship',
        'http://upei.ca/programsandcourses/environmental-studies',
        'http://upei.ca/programsandcourses/family-science',
        'http://upei.ca/programsandcourses/foods-and-nutrition',
        'http://upei.ca/programsandcourses/kinesiology',
        'http://www.upei.ca/programsandcourses/mathematical-and-computational-sciences',
        'http://www.upei.ca/programsandcourses/medical-and-biological-physics',
        'http://upei.ca/programsandcourses/paramedicine',
        'http://upei.ca/programsandcourses/physics',
        'http://upei.ca/programsandcourses/pre-veterinary-medicine-stream',
        'http://upei.ca/programsandcourses/psychology',
        'http://upei.ca/programsandcourses/bachelor-applied-science-radiography',
        'http://upei.ca/programsandcourses/engineering',
        'http://upei.ca/programsandcourses/bachelor-wildlife-conservation'
    ]
    C = set(C)
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)

        #1.school_name
        school_name = 'University of Prince Edward Island'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.major_name_en
        major_name_en = response.xpath('/html[1]/body[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]//h2').extract()
        major_name_en = ''.join(major_name_en)
        major_name_en = remove_tags(major_name_en).strip()
        # print(major_name_en)

        #4.overview_en
        overview_en = response.xpath("//div[@id='quicktabs-tabpage-view__flex_tabs__block_1-0']//div[@class='tabcontent']").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en).strip()
        # print(overview_en,'-----------------------------')

        #5.career_en
        career_en = response.xpath("//div[contains(@class,'view-programpageinfo')]//span[@class='views-label views-label-field-careers'][contains(text(),'Careers:')]//../div").extract()
        try:
            career_en = remove_class(career_en[0]).strip()
        except:
            career_en = None
        # print(career_en)

        #6.modules_en
        modules_en = response.xpath("//div[contains(@id,'quicktabs-tabpage-view__coursefields__block')]//div[@class='views-field views-field-field-courses']").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en).strip()
        # print(modules_en)
        if len(modules_en)<50:
            modules_en = response.xpath("//div[@class='tabcontent']").extract()
            try:
                modules_en = modules_en[1]
                modules_en = remove_class(modules_en)
            except:
                modules_en = None

        #7.department
        if 'Sustainable Design Engineering' in major_name_en:
            department = 'Faculty of Sustainable Design Engineering'
        elif 'Psychology' in major_name_en or 'Pre-Veterinary Medicine Stream' in major_name_en or 'Wildlife Conservation' in major_name_en or 'Sustainable Design Engineering' in major_name_en or 'Radiography' in major_name_en or 'Physics' in major_name_en or 'Paramedicine' in major_name_en or 'Medical and Biological Physics' in major_name_en or 'Mathematical and Computational Sciences' in major_name_en or 'Kinesiology' in major_name_en or 'Foods and Nutrition' in major_name_en or 'Family Science' in major_name_en or 'Environmental Studies' in major_name_en or 'Dietetic Internship (Foods and Nutrition)' in major_name_en or 'Child and Family Studies' in major_name_en or 'Chemistry' in major_name_en or 'Biotechnology' in major_name_en or 'Biology' in major_name_en or 'Applied Climate Change and Adaptation' in major_name_en:
            department = 'Faculty of Science'
        elif 'Nursing' in major_name_en:
            department  = 'Faculty of Nursing'
        elif 'Bachelor of Education' in major_name_en:
            department = 'Faculty of Education'
        elif 'Bachelor of Business Studies' in major_name_en or 'Bachelor of Business in Tourism and Hospitality' in major_name_en or 'Accelerated Bachelor of Business Administration' in major_name_en or 'Tourism and Hospitality' in major_name_en or 'Organizational Management' in major_name_en or 'Marketing' in major_name_en or 'International Business' in major_name_en or 'Finance' in major_name_en or 'Entrepreneurship' in major_name_en or 'Accounting' in major_name_en or 'Bachelor of Business Administration' in major_name_en:
            department = 'Faculty of Business'
        else:
            department = 'Faculty of Arts'
        # print(department)

        #8.tuition_fee
        if 'Education' in department:
            tuition_fee = '10,692'
        else:
            tuition_fee = '7,176'

        #9.tuition_fee_pre
        tuition_fee_pre = '$'

        #10.entry_requirements_en
        entry_requirements_en = '<p>Average of 75-80% on 5 academic subjects from Grade 11 and 12, and average B on the Huikao.</p>'

        #11.require_chinese_en
        require_chinese_en = '<p>Average of 75-80% on 5 academic subjects from Grade 11 and 12, and average B on the Huikao.</p>'

        #12.13.sat1_desc act_desc
        sat1_desc = "Minimum overall 'B' average (GPA 2.8 on a 4.0 scale) in a recognized academic grade 12 program. At least 4 different subjects at the matriculation level must be represented in the high school diploma. SAT or ACT results are not required, but can be used for scholarship reference.  "
        act_desc = sat1_desc

        #14.alevel
        alevel = 'General Certificate of Secondary Education (GCSE or IGSCE) with five O-level subjects with minimum C grade or better; General Certificate of Education Advanced or Advanced Supplementary Levels (GCE-A or AICE or GCE-AS) with at least 2 A-levels (two AS subjects may be substituted for one A-level). Minimum C in each and all AS and A-levels.'

        #15.location
        location = 'Prince Edward Island'

        #16.ielts_desc 1718192021
        ielts_desc = 'arts,science,business Overall score of 6.5 with 6.5 in writing no other band below 6;nursing,education Overall score of 7 with 7 in writing and speaking; 6.5 in reading and listening'
        if 'Arts' in department or 'Business' in department or 'Science' in department:
            ielts = 6.5
            ielts_w = 6.5
            ielts_r = 6
            ielts_l = 6
            ielts_s = 6
        else:
            ielts = 7
            ielts_w = 7
            ielts_r = 6.5
            ielts_l = 6.5
            ielts_s = 7

        #22.toefl_desc 2324252627
        toefl_desc = 'arts,science,business 80 with minimum of 20 in each category; nursing,education 100 with a minimum of 25 in speaking and writing, 22 in reading and listening'
        if 'Arts' in department or 'Business' in department or 'Science' in department:
            toefl = 80
            toefl_w = 20
            toefl_s = 20
            toefl_l = 20
            toefl_r = 20
        else:
            toefl = 100
            toefl_w = 25
            toefl_s = 25
            toefl_l = 20
            toefl_r = 20

        #28.29.toefl_code,sat_code
        toefl_code = '0941'
        sat_code ='0941'

        #30.act_code
        act_code ='7935'

        #31.apply_fee
        apply_fee = 50

        #32.apply_pre
        apply_pre = '$'

        item['school_name'] = school_name
        item['url'] = url
        item['major_name_en'] = major_name_en
        item['overview_en'] = overview_en
        item['career_en'] = career_en
        item['modules_en'] = modules_en
        item['department'] = department
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['entry_requirements_en'] = entry_requirements_en
        item['require_chinese_en'] = require_chinese_en
        item['sat1_desc'] = sat1_desc
        item['act_desc'] = act_desc
        item['alevel'] = alevel
        item['location'] = location
        item['ielts_desc'] = ielts_desc
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl_desc'] = toefl_desc
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['toefl_w'] = toefl_w
        item['toefl_code'] = toefl_code
        item['sat_code'] = sat_code
        item['act_code'] = act_code
        item['apply_fee'] = apply_fee
        item['apply_pre'] = apply_pre
        yield  item