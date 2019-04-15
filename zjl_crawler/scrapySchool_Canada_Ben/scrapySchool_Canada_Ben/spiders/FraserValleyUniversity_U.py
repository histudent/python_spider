# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/12/17 10:46'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from lxml import etree
import requests
class FraserValleyUniversity_USpider(scrapy.Spider):
    name = 'FraserValleyUniversity_U'
    allowed_domains = ['ufv.ca/']
    start_urls = []
    C= [
'https://www.ufv.ca/adult-education/programs/adult-education-ba/',
'https://www.ufv.ca/agriculture/programs/agricultural-science/',
'https://www.ufv.ca/scms/programs/anthropology-ba/',
'https://www.ufv.ca/visual-arts/programs/bfa/',
'https://www.ufv.ca/business/programs/aviation--bachelor-of-business-administration/',
'https://www.ufv.ca/biology/',
'https://www.ufv.ca/chemistry/',
'https://www.ufv.ca/cis/programs/bachelor-cis/',
'https://www.ufv.ca/computing-science/',
'https://www.ufv.ca/english/programs/creative-writing/',
'https://www.ufv.ca/economics.htm',
'https://www.ufv.ca/teacher-education/find-your-program/bachelor-of-education/',
'https://www.ufv.ca/english/programs/bachelor-of-arts-english/',
'https://www.ufv.ca/mola/find-your-program/french--bachelor-of-arts/',
'https://www.ufv.ca/general-studies/program-options/bachelor-general-studies/',
'https://www.ufv.ca/geography/programs/geography-ba/',
'https://www.ufv.ca/gds/',
'https://www.ufv.ca/indigenous-studies/program/ba-indigenous-studies/',
'https://www.ufv.ca/kinesiology/',
'https://www.ufv.ca/math/programs/major-extended-minor/',
'https://www.ufv.ca/media-arts/',
'https://www.ufv.ca/nursing/programs/bachelor-of-science-in-nursing/',
'https://www.ufv.ca/peace-and-conflict/',
'https://www.ufv.ca/philosophy/programs/philosophy-ba/',
'https://ufv.ca/geography/programs/physical-geography-bsc/',
'https://www.ufv.ca/physics.htm',
'https://www.ufv.ca/politicalscience/programs/political-science--bachelor-of-arts/',
'https://www.ufv.ca/psychology/',
'https://www.ufv.ca/swhs/programs/bachelor-of-social-work/',
'https://www.ufv.ca/scms/programs/sociology/',
'https://www.ufv.ca/theatre/programs/ba-theatre/']
    for i in C:
        start_urls.append(i)

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)

        #1.school_name
        school_name = 'Fraser Valley University'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.major_name_en
        major_name_en_a = response.xpath('//*[@id="pl_inner"]/div/div[2]/h1').extract()
        major_name_en_a = ''.join(major_name_en_a)
        major_name_en_a = remove_tags(major_name_en_a)
        major_dict = {"Bachelor of Agricultural Science, Horticulture major":"Horticulture",
"Bachelor of Arts in Adult Education (BA AE)":"Adult Education",
"Anthropology — Bachelor of Arts":"Anthropology",
"Biology":"Biology",
"Bachelor of Fine Arts, Visual Arts":"Visual Arts",
"Aviation — Bachelor of Business Administration":"Aviation",
"Chemistry":"Chemistry",
"Bachelor of Computer Information Systems":"Computer Information Systems",
"Education — bachelor's degree":"Education",
"Computing Science":"Computing Science",
"Bachelor of General Studies":"General Studies",
"Creative Writing — Bachelor of Arts":"Creative Writing",
"Economics":"Economics",
"French — Bachelor of Arts":"French",
"Global Development Studies":"Global Development Studies",
"Indigenous Studies — Bachelor of Arts degree":"Indigenous Studies",
"Kinesiology":"Kinesiology",
"English — Bachelor of Arts":"English",
"Mathematics major (BA/BSc), extended minor (BA), or minor (BA/BSc/BCIS/BGS)":"Mathematics",
"Media Arts":"Media Arts",
"Geography — Bachelor of Arts":"Geography",
"Bachelor of Science in Nursing":"Nursing",
"Peace and Conflict Studies":"Peace and Conflict Studies",
"Physics":"Physics",
"Political Science — Bachelor of Arts":"Political Science",
"Media &amp; Communications — Bachelor of Arts":"Media &amp; Communications",
"Psychology":"Psychology",
"Sociology — Bachelor of Arts":"Sociology",
"Bachelor of Arts in Theatre":"Theatre",
"Philosophy — Bachelor of Arts":"Philosophy",
"Social Work — bachelor's degree":"Social Work",
"Physical Geography — Bachelor of Science":"Physical Geography"}
        major_name_en = major_dict.get(major_name_en_a).replace('&amp; ','')
        # print(major_name_en)

        #4.degree_name
        degree_name_dict = {"Bachelor of Agricultural Science, Horticulture major":"Bachelor of Agricultural Science",
"Bachelor of Arts in Adult Education (BA AE)":"Bachelor of Arts",
"Anthropology — Bachelor of Arts":"Bachelor of Arts",
"Biology":"Bachelor of Science",
"Bachelor of Fine Arts, Visual Arts":"Bachelor of Fine Arts",
"Aviation — Bachelor of Business Administration":"Bachelor of Business Administration",
"Chemistry":"Bachelor of Science",
"Bachelor of Computer Information Systems":"Bachelor of Computer Information Systems",
"Education — bachelor's degree":"Bachelor of Education",
"Computing Science":"Bachelor of Science",
"Bachelor of General Studies":"Bachelor of General Studies",
"Creative Writing — Bachelor of Arts":"Bachelor of Arts",
"Economics":"Bachelor of Arts",
"French — Bachelor of Arts":"Bachelor of Arts",
"Global Development Studies":"Bachelor of Arts",
"Indigenous Studies — Bachelor of Arts degree":"Bachelor of Arts",
"Kinesiology":"Bachelor of Kinesiology",
"English — Bachelor of Arts":"Bachelor of Arts",
"Mathematics major (BA/BSc), extended minor (BA), or minor (BA/BSc/BCIS/BGS)":"Bachelor of Arts/Bachelor of Science",
"Media Arts":"Bachelor of Arts",
"Geography — Bachelor of Arts":"Bachelor of Arts",
"Bachelor of Science in Nursing":"Bachelor of Science",
"Peace and Conflict Studies":"Bachelor of Arts",
"Physics":"Bachelor of Sciense",
"Political Science — Bachelor of Arts":"Bachelor of Arts",
"Media &amp; Communications — Bachelor of Arts":"Bachelor of Arts",
"Psychology":"Bachelor of Arts",
"Sociology — Bachelor of Arts":"Bachelor of Arts",
"Bachelor of Arts in Theatre":"Bachelor of Arts",
"Philosophy — Bachelor of Arts":"Bachelor of Arts",
"Social Work — bachelor's degree":"Bachelor of Social Work",
"Physical Geography — Bachelor of Science":"Bachelor of Science"
        }
        degree_name = degree_name_dict.get(major_name_en_a).replace('&amp; ','')
        # print(major_name_en,'****',degree_name)

        #5.location
        location = 'Vancouver'

        #6.campus
        campus = response.xpath('//*[@id="pl_inner"]/div/div[2]/div/div[3]/div[2]/p').extract()
        campus = ''.join(campus)
        campus = remove_tags(campus)
        campus = re.findall('Location:\s(.*)Cost',campus,re.S)[0].replace('\r','').replace('\n','').strip()
        # print(campus)

        #7.start_date
        start_date = response.xpath('//*[@id="pl_inner"]/div/div[2]/div/div[3]/div[2]/p').extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        start_date = re.findall('Start date:(.*)',start_date)[0].replace('\xa0\r','')
        if 'January, May, September' in start_date:
            start_date = '2019-1,2019-5,2019-9'
        elif 'September, January, May' in start_date:
            start_date = '2019-1,2019-5,2019-9'
        elif 'September, May, January' in start_date:
            start_date = '2019-1,2019-5,2019-9'
        elif 'May, January, September' in start_date:
            start_date = '2019-1,2019-5,2019-9'
        elif 'January, September' in start_date:
            start_date = '2019-1,2019-9'
        elif 'September, January' in start_date:
            start_date = '2019-1,2019-9'
        elif 'August' in start_date:
            start_date = '2019-8'
        else:
            start_date = '2019-9'
        # print(start_date)

        #8.duration
        duration = 4

        #9.duration_per
        duration_per = 1

        #10.overview_en
        overview_en = response.xpath("//h2[contains(text(),'PROGRAM DESCRIPTION')]/../following-sibling::*[1]").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #11.career_en
        career_en = response.xpath("//h2[contains(text(),'CAREER EXPECTATIONS')]/../following-sibling::*[1]").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #12.tuition_fee
        tuition_fee = '17,160'

        #13.tuition_fee_pre
        tuition_fee_pre = '$'

        #14.tuition_fee_per
        tuition_fee_per = 1

        #15.ap
        ap  = 'A C+ final grade in one of English 12, English 12 First Peoples, AP English, or IB English.'

        #16.ib
        ib = 'A C+ final grade in one of English 12, English 12 First Peoples, AP English, or IB English.'

        #17.ielts_desc 1819202122
        ielts_desc = 'IELTS (Academic) - score of 6.5 or higher with a minimum band score of 6.0'
        ielts = 6.5
        ielts_w = 6
        ielts_r = 6
        ielts_l = 6
        ielts_s = 6

        #23.toefl_desc 2425262728
        toefl_desc = 'TOEFL - score of 88 or higher (iBT) with no section below 20'
        toefl = 88
        toefl_r = 20
        toefl_w = 20
        toefl_s = 20
        toefl_l = 20

        #29.toefl_code
        toefl_code = '9736'

        #30.sat_code
        sat_code = '9736'

        #31.apply_fee
        apply_fee = 150

        #32.apply_pre
        apply_pre = '$'

        #33.entry_requirements_en
        entry_requirements_en = '<p>The following are the minimum requirements for admission to UFV.</p><p></p><p>All applicants must meet ONE of the following:</p><p></p><p>B.C. high school graduation or equivalent;</p><p>Or completion of a minimum of nine UFV or transferable post-secondary credits with a minimum 2.00 GPA (C average) based on all credits </p>attempted;<p>Or a minimum of 19 years of age by the start of the first class;</p><p>Or, for admission into preparatory level programs only, a minimum of 17 years of age and out of high school for at least one year by the </p>start of the semester.<p>English requirements</p><p>English is the language of instruction at UFV. To be successful, applicants must demonstrate language proficiency by meeting the </p>following requirement:<p></p><p>A C+ final grade in one of English 12, English 12 First Peoples, AP English, or IB English.</p>'

        #34.require_chinese_en
        require_chinese_en = entry_requirements_en

        #35.deadline
        deadline = '2019-05-01,2019-10-01'

        # 以下用于抓取课程设置字段
        # department = response.xpath('//*[@id="sb-site"]/div[2]/div/div[1]/h1/a').extract()
        # department = ''.join(department)
        # department = remove_tags(department)
        # # print(department)
        # other = response.xpath('//h2').extract()[:-2]
        # other = ''.join(other)
        # other = remove_class(other)
        # # print(other,response.url)
        # item['department'] = department
        # item['other'] = other
        # item['school_name'] = 'sss'
        # yield item


        item['school_name'] = school_name
        item['url'] = url
        item['major_name_en'] = major_name_en
        item['degree_name'] = degree_name
        item['location'] = location
        item['campus'] = campus
        item['start_date'] = start_date
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['overview_en'] = overview_en
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        # item['tuition_fee_per'] = tuition_fee_per
        item['ap'] = ap
        item['ib'] = ib
        item['ielts_desc'] = ielts_desc
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['toefl_desc'] = toefl_desc
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['toefl_w'] = toefl_w
        item['toefl_code'] = toefl_code
        item['sat_code'] = sat_code
        item['apply_fee'] = apply_fee
        item['apply_pre'] = apply_pre
        item['entry_requirements_en'] = entry_requirements_en
        item['require_chinese_en'] = require_chinese_en
        item['deadline'] = deadline
        # yield item