# -*- coding:utf-8 -*-
"""
# @PROJECT: scrapySchool_Canada_Ben
# @Author: admin
# @Date:   2018-10-31 15:15:44
# @Last Modified by:   admin
# @Last Modified time: 2018-10-31 15:15:44
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

class StThomasUniversity_USpider(scrapy.Spider):
    name = "StThomasUniversity_U"
    # start_urls = ["https://www.stu.ca/academics/bachelor-of-arts/"]
    start_urls = ["https://www.stu.ca/catholicstudies/",
"https://www.stu.ca/copp/",
"https://www.stu.ca/english/",
"https://www.stu.ca/international/english-as-a-second-language/",
"https://www.stu.ca/finearts/",
"https://www.stu.ca/french/",
"https://www.stu.ca/greatbooks/",
"https://www.stu.ca/history/",
"https://www.stu.ca/humanrights/",
"https://www.stu.ca/interdisciplinarystudies/",
"https://www.stu.ca/irishstudies/",
"https://www.stu.ca/italian/",
"https://www.stu.ca/japanese/",
"https://www.stu.ca/journalism/",
"https://www.stu.ca/latin/",
"https://www.stu.ca/mediastudies/",
"https://www.stu.ca/nativestudies/",
"https://www.stu.ca/philosophy/",
"https://www.stu.ca/religiousstudies/",
"https://www.stu.ca/romancelanguages/",
"https://www.stu.ca/academics/bachelor-of-arts/spanish-and-latin-american-studies/",
"https://www.stu.ca/anthropology/",
"https://www.stu.ca/criminology/",
"https://www.stu.ca/economics/",
"https://www.stu.ca/envs/",
"https://www.stu.ca/gerontology/",
"https://www.stu.ca/ir/",
"https://www.stu.ca/laps/",
"https://www.stu.ca/mathematics/",
"https://www.stu.ca/politicalscience/",
"https://www.stu.ca/psychology/",
"https://www.stu.ca/sts/",
"https://www.stu.ca/sociology/",
"https://www.stu.ca/wsgs/", ]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)
        item['school_name'] = "St. Thomas University"
        item['url'] = response.url
        print("===========================")
        print(response.url)
        item['other'] = '''问题描述：1.专业描述和课程设置、就业为空的是页面没有的'''

        '''公共字段'''
        # item['campus'] = 'Hamilton'
        item['location'] = 'Fredericton, NB, Canada'
        # item['sat_code'] = item['toefl_code'] = '5076'
        # item['act_code'] = '0719'

        # item['duration'] = '4'
        # item['duration_per'] = 1
        # https://www.stu.ca/future-students/how-to-apply/
        item['apply_pre'] = 'CAD$'
        item['apply_fee'] = '55'
        item['start_date'] = '1月,9月'
        item['deadline'] = '2018-12-31,2019-03-01'
        # https://www.stu.ca/future-students/tuition_fees/
        item['tuition_fee_pre'] = 'CAD$'
        item['tuition_fee'] = '15,230'

        # https://www.stu.ca/admissions/bachelor-of-arts/
        item['ielts_desc'] = 'IELTS 6.5'
        item['ielts'] = '6.5'
        item['toefl_desc'] = 'TOEFL 88-89 (Internet-based)'
        item['toefl'] = '88-89'
        item['ap'] = item['ib'] = """Advanced Placement, International Baccalaureate and GCE Advanced Level applicants presenting official documentation of grades of 4 or 5 on Advanced Placement (AP) tests, grades of 5, 6 or 7 on individual higher-level International Baccalaureate (IB) subjects, or final grades of “C” or higher on GCE Advanced-Level courses are eligible for transfer credit. AP students are eligible for a maximum of 18 credit hours in transfer credit while IB diploma and GCE Advanced- Level students are eligible for a maximum of 30 credit hours on a 120 credit-hour degree programme.
Students granted transfer credit for AP, IB, and GCE Advanced-Level courses are advised to consult graduate and professional schools to determine the impact that this non-university credit award will have on their future academic plans."""
        item['entry_requirements_en'] = """<p>Canadian high school applicants must meet the following minimum requirements:</p>
<ul>
<li>high school graduation</li>
<li>minimum average of 70% on five successfully completed Grade 12 academic courses including Grade 12 academic English (or French for applicants from Francophone schools)</li>
<li>four Grade 12 academic electives from the list below</li>
</ul>"""

        item['act_desc'] = item['sat1_desc'] = "SAT or ACT scores will also be considered"

        # https://www.stu.ca/admissions/bachelor-of-arts/international-students/
        item['require_chinese_en'] = '<p>Senior High School Graduation Examination and Chinese National University Entrance Examinations.</p>'
        try:

            major_name_en = response.xpath("//div[@class='small-12 medium-12 large-8 columns']//h1//text()").extract()
            clear_space(major_name_en)
            item['major_name_en'] = ''.join(major_name_en).strip()
            print("item['major_name_en']: ", item['major_name_en'])

            item['degree_name'] = 'Bachelor of Arts'
            item['degree_overview_en'] = """<p>The St. Thomas University Bachelor of Arts is unique in Canada. As the core academic program, the Bachelor of Arts is the heart of our academic community. All 1,800 undergraduates are Bachelor of Arts students—connected by their interest in the social sciences and humanities.</p>"""
            if item['major_name_en'] == "Criminology and Criminal Justice":
                item['degree_name'] = "Bachelor of Applied Arts"
                item['degree_overview_en'] = """<p>The Bachelor of Applied Arts in Criminal Justice prepares students for work in various sectors of the criminal justice system through practical training and a liberal arts education. Offered in conjunction with the New Brunswick Community College-Miramichi, the Bachelor of Applied Arts in Criminal Justice is a four-year articulated program that prepares entry-level practitioners to work in sectors of the criminal justice system such as community correctional practice and public safety.</p>
                <p>The first two years are offered at NBCC-Miramichi where students earn a diploma in Criminal Justice. The third and fourth years of the program are offered by St. Thomas, where compulsory courses further develop theoretical and conceptual understanding of the Canadian  criminal justice system and a more concentrated academic focus in the liberal arts. Upon  completion of the second stage of the program, students are awarded a Bachelor of Applied Arts in Criminal Justice.</p>"""
            if item['major_name_en'] == "Gerontology":
                item['degree_name'] = "Bachelor of Applied Arts"
                item['degree_overview_en'] = """<p>The Bachelor of Applied Arts in Gerontology examines aging and issues that affect the elderly.</p>
                                <p>Developed in response to demands for graduates with applied practice in the field, it combines a theoretical foundation in Gerontology and liberal arts with human services training and hands-on experience in the design and delivery of services to the elderly. This four-year program is offered in collaboration with the New Brunswick Community College in Saint John.</p>"""
            print("item['degree_name']: ", item['degree_name'])


            department_dict = {"Catholic Studies": "Humanities",
                               "Communications and Public Policy": "Humanities",
                               "English Language and Literature": "Humanities",
                               "English as a Second Language": "Humanities",
                               "Fine Arts": "Humanities",
                               "French": "Humanities",
                               "Great Books": "Humanities",
                               "History": "Humanities",
                               "Human Rights": "Humanities",
                               "Interdisciplinary Studies": "Humanities",
                               "Irish Studies": "Humanities",
                               "Italian": "Humanities",
                               "Japanese": "Humanities",
                               "Journalism": "Humanities",
                               "Latin": "Humanities",
                               "Media Studies": "Humanities",
                               "Native Studies": "Humanities",
                               "Philosophy": "Humanities",
                               "Religious Studies": "Humanities",
                               "Romance Languages": "Humanities",
                               "Spanish and Latin American Studies": "Humanities",
                               "Anthropology": "Social Sciences",
                               "Criminology and Criminal Justice": "Social Sciences",
                               "Economics": "Social Sciences",
                               "Environment and Society": "Social Sciences",
                               "Gerontology": "Social Sciences",
                               "International Relations": "Social Sciences",
                               "Law, Politics, and Society": "Social Sciences",
                               "Mathematics": "Social Sciences",
                               "Political Science": "Social Sciences",
                               "Psychology": "Social Sciences",
                               "Science and Technology Studies": "Social Sciences",
                               "Sociology": "Social Sciences",
                               "Women's Studies and Gender Studies": "Social Sciences", }
            item['department'] = department_dict.get(item['major_name_en'])
            print("item['department']: ", item['department'])

            overview = response.xpath("//div[@class='content']//h2[2]/preceding-sibling::p").extract()
            if len(overview) == 0:
                overview = response.xpath("//div[@class='column general']//div[@class='content']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview)).replace("<p></p>", "").strip()
            if item['overview_en'] == "":
                item['overview_en'] = None
            #     print("***overview_en 为空")
            # print("item['overview_en']: ", item['overview_en'])

            # career
            tmp_html = response.text
            key = re.findall(r'<h2><strong>Careers and Graduate Pathways</strong></h2>|<h2><strong>Careers and Transferable Skills</strong></h2>', tmp_html)
            # print(key)
            key1 = re.findall(r'<h2><strong>Related Fields of Study</strong></h2>|<h2><strong>Related Areas of Study</strong></h2>|'
                              r'<h2><strong>Related Areas Study&nbsp;</strong></h2>|<h2><strong>Related Areas of Study&nbsp;</strong></h2>', tmp_html)
            # print(key1)

            career_html = tmp_html.replace(''.join(key), '<div id="container">'+''.join(key)).replace(''.join(key1), '</div>'+''.join(key1))
            career_html_response = etree.HTML(career_html)
            # 可以使用xpath匹配需要的内容了
            admisson = career_html_response.xpath("//div[@id='container']")
            # 转化成带标签的数据内容
            if len(admisson) > 0:
                item['career_en'] = remove_class(clear_lianxu_space([etree.tostring(admisson[0], encoding='unicode', method='html')]))
            if item['career_en'] is None:
                # item['career_en'] = None
                career1 = response.xpath("//strong[contains(text(),'After Graduation')]/../following-sibling::p").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career1))
                if item['career_en'] == "":
                    item['career_en'] = None
                # print("***career_en 为空")
            # print("item['career_en']: ", item['career_en'])

            # modules_url = response.xpath("//div[contains(@class,'small-12 medium-4 columns sidbar-container')]//ul[@class='side-nav']//li[1]/a[contains(@href, 'program-structure')]/@href").extract()
            # if len(modules_url) == 0:
            modules_url = response.xpath(
                "//div[contains(@class,'small-12 medium-4 columns sidbar-container')]//ul[@class='side-nav']//a[contains(@href,'courses/')]/@href").extract()
            print(modules_url)

            if len(modules_url) > 0:
                modules_url_end = "https://www.stu.ca" + modules_url[0].strip()
                item['modules_en'] = self.parse_modules(modules_url_end)
            if item['modules_en'] == "":
                item['modules_en'] = None
                # print("***modules_en 为空")
            print("item['modules_en']: ", item['modules_en'])

            yield item

        except Exception as e:
            with open("scrapySchool_Canada_Ben/error/" + item['school_name'] + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_modules(self, modules_url_end):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(modules_url_end, headers=headers_base)
        response = etree.HTML(data.text)

        modules_en = response.xpath(
            "//div[@class='small-12 medium-12 large-8 columns']//div[@class='stu-course-listing']/h3")
        # if len(modules_en) == 0:
        #     entrey_requirements_en = response.xpath(
        #         "//div[@id='admission']//div[@class='panel-body']")
        modules_en_str = ""
        if len(modules_en) > 0:
            for m in modules_en:
                modules_en_str += etree.tostring(m, encoding='unicode', method='html')
                modules_en = remove_class(clear_lianxu_space([modules_en_str]))
        # print(entrey_requirements_en)
        return modules_en