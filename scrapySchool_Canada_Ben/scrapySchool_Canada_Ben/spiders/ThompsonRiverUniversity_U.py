# -*- coding:utf-8 -*-
"""
# @PROJECT: scrapySchool_Canada_Ben
# @Author: admin
# @Date:   2018-12-14 15:24:55
# @Last Modified by:   admin
# @Last Modified time: 2018-12-14 15:24:55
"""

__author__ = 'yangyaxia'
__date__ = '2018/10/31 15:15'
import scrapy
import re
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from w3lib.html import remove_tags
from lxml import etree
import requests

class ThompsonRiverUniversity_USpider(scrapy.Spider):
    name = "ThompsonRiverUniversity_U"
    start_urls = ["https://www.tru.ca/programs.html"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        # //div[@class='small-12 medium-6 mix campus major degree international']/div[@class='accordion programBox']/div[@class='nameWrap']/div[@class='accordion-content']/div[@class='contentPad']/a[@class='button tealbg nomargin']
        links = response.xpath("""//div[contains(@class, "small-12 medium-6 mix campus major degree international")]//a[contains(text(), 'Learn more about this program')]/@href""").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))
        # print(links)

        # links = ["https://www.tru.ca/programs/catalogue/bachelor-of-arts-year1.html"]
        # links = ["https://www.tru.ca/programs/catalogue/engineering-transfer-year-1-and-2.html"]
        for url in links:
            yield scrapy.Request(url, self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)
        item['school_name'] = "Thompson River University"
        item['url'] = response.url
        print("===========================")
        print(response.url)
        item['other'] = '''问题描述：1.课程设置在https://www.tru.ca/distance/courses/?p=subject&c=ab上面匹配的，有些专业为空
2.没有找到ap、ib、sat、act、toefl code，所以为空'''

        '''公共字段'''
        item['location'] = '805 TRU Way Kamloops, BC V2C 0C8'
        # item['sat_code'] = item['toefl_code'] = '5076'
        # item['act_code'] = '0719'

        # https://www.tru.ca/future/admissions/undergrad.html
        item['apply_pre'] = 'CAD$'
        item['apply_fee'] = '100'
        # https://www.tru.ca/future/admissions/international/application-deadlines.html
        item['deadline'] = '2019-10-01,2019-02-01,2019-05-01'

        # https://www.tru.ca/future/tuition/details.html
        item['tuition_fee_pre'] = 'CAD$'
        item['tuition_fee'] = '17,847'

        # https://www.tru.ca/future/admissions/international/admission-requirements.html
        item['ielts_desc'] = '6.5+ with no bands below 6.0'
        item['ielts'] = '6.5'
        item['ielts_l'] = '6.0'
        item['ielts_s'] = '6.0'
        item['ielts_r'] = '6.0'
        item['ielts_w'] = '6.0'
        item['toefl_desc'] = '88+ with no section below 20'
        item['toefl'] = '88'
        item['toefl_l'] = '20'
        item['toefl_s'] = '20'
        item['toefl_r'] = '20'
        item['toefl_w'] = '20'
#         item['ap'] = item['ib'] = """Advanced Placement, International Baccalaureate and GCE Advanced Level applicants presenting official documentation of grades of 4 or 5 on Advanced Placement (AP) tests, grades of 5, 6 or 7 on individual higher-level International Baccalaureate (IB) subjects, or final grades of “C” or higher on GCE Advanced-Level courses are eligible for transfer credit. AP students are eligible for a maximum of 18 credit hours in transfer credit while IB diploma and GCE Advanced- Level students are eligible for a maximum of 30 credit hours on a 120 credit-hour degree programme.
# Students granted transfer credit for AP, IB, and GCE Advanced-Level courses are advised to consult graduate and professional schools to determine the impact that this non-university credit award will have on their future academic plans."""

#         item['act_desc'] = item['sat1_desc'] = "SAT or ACT scores will also be considered"

        #  (R' F R F') R U2' R' U (R U2' R')
        item['require_chinese_en'] = '''<h1>International Student Admission Requirements</h1>
<h2>English language proficiency requirements for academic study</h2>
<p>Applicants are required to meet minimum English language proficiency requirements for direct entry into academic programs.</p>
<p>Students may meet this condition by either providing an acceptable English language proficiency test score (TOEFL, IELTS, etc.) or by achieving an acceptable score on the TRU English Placement Test (EPT). Students are strongly encouraged to complete an acceptable test prior to arriving to improve course selection options, but this is not mandatory.</p>
<p>In order to verify all English language proficiency test scores, students must have an official copy sent directly to TRU Admissions from the testing agency. Copies of test scores, provided to the ESAL department upon arrival, will not be accepted.</p>
<p>Students who fail to achieve the results for direct entry into academic programs will be placed in the appropriate level of English language study as indicated below.</p>'''
        try:

            major_name_en_degree = response.xpath("//div[@class='large-9 columns pageTitle h3pad']//h1//text()").extract()
            clear_space(major_name_en_degree)
            print(major_name_en_degree)
            if len(major_name_en_degree) == 2:
                item['major_name_en'] = major_name_en_degree[0].strip()
                if "Major" in item['major_name_en']:
                    item['major_name_en'] = item['major_name_en'].replace("Major", "").strip().strip(",").strip()
                # if "," in item['major_name_en']:
                #     item['major_name_en'] = item['major_name_en'].replace(",", "").strip()
                item['degree_name'] = major_name_en_degree[-1]
            print("item['major_name_en']: ", item['major_name_en'])
            print("item['degree_name']: ", item['degree_name'])


            major_key = ["Accounting",
"Animal Biology",
"Biology",
"Cellular, Molecular and Microbial Biology",
"Chemical Biology",
"Chemistry",
"Communication",
"Computing Science",
"Computing Science and Mathematics",
"Ecology and Environmental Biology",
"Economic and Political Studies",
"Economics",
"Economics",
"Economics and Mathematics",
"English",
"Entrepreneurship",
"Environmental Chemistry",
"Finance",
"General Science",
"Geography and Environmental Studies",
"History",
"Human Resource Management",
"International Business",
"Marketing",
"Mathematical Sciences",
"Mathematics",
"Mathematics",
"Mathematics and Economics",
"Philosophy",
"Physics",
"Psychology",
"Public Relations",
"Sociology",
"Supply Chain Management",
"Theatre Arts", ]
            department_value = ["School of Business and Economics",
"Faculty of Science",
"Faculty of Science",
"Faculty of Science",
"Faculty of Science",
"Faculty of Science",
"Bachelor of Arts",
"Faculty of Science",
"Faculty of Science",
"Faculty of Science",
"Faculty of Arts",
"School of Business and Economics",
"Faculty of Arts",
"Faculty of Science",
"Faculty of Arts",
"School of Business and Economics",
"Faculty of Science",
"School of Business and Economics",
"Faculty of Science",
"Faculty of Arts",
"Faculty of Arts",
"School of Business and Economics",
"School of Business and Economics",
"School of Business and Economics",
"Faculty of Science",
"Faculty of Science",
"Faculty of Arts",
"Faculty of Arts",
"Faculty of Arts",
"Faculty of Science",
"Faculty of Arts",
"Faculty of Arts",
"Faculty of Arts",
"School of Business and Economics",
"Faculty of Arts", ]
            department_dict = {}
            for i in range(len(major_key)):
                department_dict[major_key[i]] = department_value[i]
            item['department'] = department_dict.get(item['major_name_en'])
            print("item['department']: ", item['department'])

            campus = response.xpath("//dt[contains(text(),'Delivery')]/following-sibling::dd[1]//text()").extract()
            clear_space(campus)
            item['campus'] = ''.join(campus).strip()
            if item['campus'] == "":
                item['campus'] = None
            print("item['campus']: ", item['campus'])

            duration = response.xpath("//dt[contains(text(),'Length')]/following-sibling::dd[1]//text()").extract()
            if len(duration) == 0:
                duration = response.xpath("//strong[contains(text(),'Length:')]/../text()").extract()

            clear_space(duration)
            # print("duration: ", duration)
            item['duration'] = ''.join(duration).strip().strip("years").strip()
            if "year" in ''.join(duration):
                item['duration_per'] = 1
            # print("item['duration']: ", item['duration'])

            start_date = response.xpath("//dt[contains(text(),'Intake dates')]/following-sibling::dd[1]//text()").extract()
            clear_space(start_date)
            # print(start_date)
            start_date_str = ""
            if "Jan" in ''.join(start_date):
                start_date_str += "2019-01,"
            if "May" in ''.join(start_date):
                start_date_str += "2019-05,"
            if "Sep" in ''.join(start_date):
                start_date_str += "2019-09,"

            item['start_date'] = start_date_str.strip().strip(",").strip()
            # print("item['start_date']: ", item['start_date'])

            overview = response.xpath("//h4[contains(text(),'Careers')]/preceding-sibling::*|//h4[contains(text(),'Prospects')]/preceding-sibling::*").extract()
            if len(overview) > 0:
                item['overview_en'] = remove_class(clear_lianxu_space(overview)).replace("<p></p>", "").strip()
            # if item['overview_en'] is None:
            #     print("***overview_en 为空")
            # print("item['overview_en']: ", item['overview_en'])

            # career
            tmp_html = response.text
            key = r'<h4>Careers</h4>'
            key1 = '<h4>Admission Requirements</h4>'
            item['career_en'] = remove_class(getContentToXpath(tmp_html, key, key1))
            if item['career_en'] == "":
                item['career_en'] = None
            # print("item['career_en']: ", item['career_en'])

            requirement_url = response.xpath("//li[contains(text(), 'Admission to')]/a/@href").extract()
            # print("requirement_url: ", requirement_url)
            if len(requirement_url) > 0:
                degree_data = self.parse_requirement("https://www.tru.ca" + ''.join(requirement_url))
                item['degree_overview_en'] = degree_data.get('degree_overview_en')
                item['entry_requirements_en'] = degree_data.get('entry_requirements_en')
            # print("item['degree_overview_en']: ", item['degree_overview_en'])
            # print("item['entry_requirements_en']: ", item['entry_requirements_en'])


            # if len(modules_url) == 0:
            modules_url = response.xpath(
                "//div[contains(@class,'small-12 medium-4 columns sidbar-container')]//ul[@class='side-nav']//a[contains(@href,'courses/')]/@href").extract()
            # print(modules_url)

            item['modules_en'] = None
            # print("***modules_en 为空")
            # print("item['modules_en']: ", item['modules_en'])

            yield item

        except Exception as e:
            with open("scrapySchool_Canada_Ben/error/" + item['school_name'] + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    # 学术要求
    def parse_requirement(self, requirement_url):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(requirement_url, headers=headers_base)
        response = etree.HTML(data.text)

        degree_data = {}
        entry_requirements_en_key1 = r"<h4>Admission Requirements</h4>"
        entry_requirements_en_key2 = r"<h4>Next Steps</h4>"

        entry_requirements_en = remove_class(getContentToXpath(data.text, entry_requirements_en_key1, entry_requirements_en_key2))
        degree_data["entry_requirements_en"] = entry_requirements_en

        degree_overview_en = response.xpath("//h6[contains(text(),'Majors:')]/preceding-sibling::*")
        if len(degree_overview_en) == 0:
            degree_overview_en = response.xpath("//h4[contains(text(),'Careers')]/preceding-sibling::*")
        degree_overview_en_str = ""
        if len(degree_overview_en) > 0:
            for m in degree_overview_en:
                degree_overview_en_str += etree.tostring(m, encoding='unicode', method='html')
        degree_overview_en = remove_class(degree_overview_en_str)
        degree_data['degree_overview_en'] = degree_overview_en
        return degree_data
