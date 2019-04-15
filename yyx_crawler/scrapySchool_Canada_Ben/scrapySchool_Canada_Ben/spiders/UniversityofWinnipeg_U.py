# -*- coding:utf-8 -*-
"""
# @PROJECT: scrapySchool_Canada_Ben
# @Author: admin
# @Date:   2018-11-14 16:13:09
# @Last Modified by:   admin
# @Last Modified time: 2018-11-14 16:13:09
"""
import scrapy
import re
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from w3lib.html import remove_tags
from lxml import etree
import requests

class UniversityofWinnipeg_USpider(scrapy.Spider):
    name = "UniversityofWinnipeg_U"
    # start_urls = ["https://www.uwinnipeg.ca/academics/programs/undergraduate-degree.html"]
    start_urls = ["https://www.uwinnipeg.ca/factsheets/"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        major_name_list = response.xpath("//div[@id='contentBody']//ul[1]//li/a//text()").extract()
        clear_space(major_name_list)
        print("major_name_list==len:", len(major_name_list))

        # alllinks = response.xpath("//div[@id='contentBody']//ul//li/a/@href").extract()
        alllinks = response.xpath("//div[@id='contentBody']//ul[1]//li/a/@href").extract()
        print(len(alllinks))
        # print(alllinks)
        # alllinks = list(set(alllinks))
        print(len(list(set(alllinks))))

        major_dict = {}
        if len(major_name_list) == len(alllinks):
            # 将PDF链接和专业名对应起来存进字典major_dict
            for i in range(len(major_name_list)):
                if "/factsheets" not in alllinks[i]:
                    alllinks[i] = "https://www.uwinnipeg.ca/factsheets/" + alllinks[i]
                else:
                    alllinks[i] = "https://www.uwinnipeg.ca" + alllinks[i]
                # if ":" in major_dict[i]:
                major_name_list[i] = major_name_list[i].replace(":", " ").strip()
                major_dict[alllinks[i]] = major_name_list[i]
            print(major_dict)
            print(alllinks)
        #
        #     # 将PDF文件下载下来放到本地
        #     for j in range(len(major_name_list)):
        #         if major_dict.get(alllinks[j]) is not None:
        #             res = requests.get(alllinks[j])
        #             with open("D:/pycharm/hooli_scrapy_project/scrapySchool_Canada_Ben/scrapySchool_Canada_Ben/UniversityofWinnipeg/"+major_dict.get(alllinks[j])+".pdf", 'wb') as f:
        #                 f.write(res.content)
        #
        #
        #     # 将下载下来的本地文件转换成HTML文件
        #     for j in range(len(major_name_list)):
        #         if major_dict.get(alllinks[j]) is not None:
        #             try:
        #                 path = r"D:/pycharm/hooli_scrapy_project/scrapySchool_Canada_Ben/scrapySchool_Canada_Ben/UniversityofWinnipeg/"+major_dict.get(alllinks[j])+".pdf"
        #                 toPath = r"D:/pycharm/hooli_scrapy_project/scrapySchool_Canada_Ben/scrapySchool_Canada_Ben/UniversityofWinnipeg/programm_html/"+major_dict.get(alllinks[j])+".html"
        #                 self.readPDF(path, toPath)
        #             except Exception as e:
        #                 print("转换HTML失败：",str(e))


        # 找出本地专业HTML文件的路径，循环访问
        import os
        html_path = r"D:\pycharm\hooli_scrapy_project\scrapySchool_Canada_Ben\scrapySchool_Canada_Ben\UniversityofWinnipeg\programm_html"
        major_html_list =os.listdir(html_path)
        # print("==", major_html_list)
        for html_title in major_html_list:
            print("===========================")
            # 拼接每个专业的本地HTML文件的路径
            elem_path = html_path + "\\" + html_title
            print(elem_path)
            item = get_item(ScrapyschoolCanadaBenItem)

            # 公共字段
            self.parse_data(item)

            # 将HTML文件转成Element html，方便使用xpath获取数据
            # major_html = ""
            # major_text = ""
            with open(elem_path, 'r', encoding="utf-8") as f:
                major_html = etree.HTML(f.read())

            with open(elem_path, 'r', encoding="utf-8") as f:
                major_text = f.read()
            # print(major_html)

            # item['major_name']
            item['department'] = None
            department = major_html.xpath("//p[contains(text(), 'FACULTY OF')]//text()")
            clear_space(department)
            # print("department: ", department)
            if len(department) > 0:
                item['department'] = department[0].replace("GUPTA FACULTY OF K INES IOLOGY AND APPL IED HEALTH", "Gupta Faculty of Kinesiology and Applied Health") \
                    .replace("EDUCAT ION", "EDUCATION").replace("SC IENCE", "SCIENCE")\
                    .replace("BUS INESS & ECONOM ICS", "BUSINESS and ECONOMICS").title().strip()
                item['department'] = item['department'].replace("Of", "of").replace("And", "and")
            # print("item['department']: ", item['department'])

            major_name_en = major_html.xpath("//p[contains(text(), 'FACULTY OF')]/following-sibling::p[1]//text()")
            clear_space(major_name_en)
            # print("major_name_en: ", major_name_en)
            if len(major_name_en) > 0:
                item['major_name_en'] = major_name_en[0].title().strip()
                item['major_name_en'] = item['major_name_en'].replace("Of", "of").replace("And", "and").replace("(Bsc)", "").strip()
            if item['major_name_en'] is None:
                item['major_name_en'] = html_title.replace(".html", "").replace("(Bsc)", "").strip()
            print("item['major_name_en']: ", item['major_name_en'])

            url_dict = {'Anthropology':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-anthropology.pdf',
'Applied Computer Science':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-applied-computer-sci.pdf',
'Bioanthropology':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-bioanthropology.pdf',
'Biochemistry':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-biochemistry.pdf',
'Biology':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-biology.pdf',
'Biopsychology':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-biopsychology.pdf',
'Business & Administration':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-business-admin.pdf',
'Chemistry':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-chemistry.pdf',
'Classics':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-classics.pdf',
'Conflict Resolution Studies':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-conflict-res-studies.pdf',
'Co-operative Education':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-co-op-education.pdf',
'Criminal Justice':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-criminal-justice.pdf',
'Dance Program':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-dance.pdf',
'Developmental Studies':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-developmental-studies.pdf',
'Disability Studies':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-disability-studies.pdf',
'East Asian Languages & Cultures':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-east-asian-languages-cultures.pdf',
'Economics':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-economics.pdf',
'Economics & Finance':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-economics-finance.pdf',
'Education':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-education.pdf',
'English':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-english.pdf',
'Environmental Studies Ba':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-env-studies-ba.pdf',
'Environmental Sciences':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-env-science-bsc.pdf',
'Student Designed Major':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-flexible-major.pdf',
'French Studies':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-french-studies.pdf',
'Geography':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-geography.pdf',
'German Studies':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-german-studies.pdf',
'German-Canadian Studies':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-german-cdn-studies.pdf',
'History':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-history.pdf',
'History of Art':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-history-of-art.pdf',
'Human Rights':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-human-rights.pdf',
'Indigenous Studies':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-indigenous-studies.pdf',
'Interdisciplinary Linguistics':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-interdisc-linguistics.pdf',
'International Development Studies':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-international-dev-studies.pdf',
'Bachelor of Kinesiology':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-kinesiology.pdf',
'Mathematics':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-mathematics.pdf',
'Mennonite Studies':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-mennonite-studies.pdf',
'Philosophy':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-philosophy.pdf',
'Bachelor of Physical and Health Education':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-physical-and-health-education.pdf',
'Physics':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-physics.pdf',
'Medical Physics':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-medical-physics.pdf',
'Radiation Health and Safety':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-radiation-health-and-safety.pdf',
'Political Science':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-political-science.pdf',
'Psychology':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-psychology.pdf',
'Radiation Therapy':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-radiation-therapy.pdf',
'Religion & Culture':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-religion-culture.pdf',
'Rhetoric and Communications':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-rhetoric-and-communications.pdf',
'Science-Business Stream':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-science-business-stream.pdf',
'Sociology':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-sociology.pdf',
'Spanish Studies':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-spanish-studies.pdf',
'Statistics':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-statistics.pdf',
'Theatre and Film':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-theatre-and-film-stream.pdf',
'Urban and Inner-City Studies':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-urban-and-inner-city-studies.pdf',
'Women’S & Gender Studies':'https://www.uwinnipeg.ca/factsheets/docs/factsheet-women-and-gender-studies.pdf',}
            item['url'] = url_dict.get(item['major_name_en'])
            print("item['url']: ", item['url'])

            if "Education" in item['major_name_en'] and item['department'] is None:
                item['department'] = "Faculty of Education"
            print("item['department']: ", item['department'])

            department_fee = {"Faculty of Arts": "13,695",
                              "Faculty of Business and Economics": "17,010",
                              "Faculty of Education": "14,259",
                              "Gupta Faculty of Kinesiology and Applied Health": "14,589",
                              "Faculty of Science": "16,372.5", }
            item['tuition_fee_pre'] = 'CAD$'
            item['tuition_fee'] = department_fee.get(item['department'])
            print("item['tuition_fee']: ", item['tuition_fee'])

            # 专业描述
            overview_en = major_html.xpath("//p[contains(text(), 'SAMPLE CAREERS')]/preceding-sibling::p[position()<last()-1]")
            if len(overview_en) == 0:
                overview_en = major_html.xpath(
                    "//p[contains(text(), 'SAMPLE COURSES')]/preceding-sibling::p[position()<last()-1]|//p[contains(text(), 'CAREER OPPORTUNITIES')]/preceding-sibling::p[position()<last()-1]")
            # print("overview_en", overview_en)
            overview_en_str = ""
            if len(overview_en) > 0:
                for m in overview_en:
                    overview_en_str += etree.tostring(m, encoding='unicode', method='html')
                item['overview_en'] = remove_class(clear_lianxu_space([overview_en_str]))
            # print("item['overview_en']: ", item['overview_en'])


            '''就业信息'''
            # print("===", major_text)
            key1 = "<p>SAMPLE CAREERS"
            if key1 not in major_text:
                key1 = "<p>CAREER OPPORTUNITIES "

            key2 = "<p>YOUR EDUCATION"
            if key2 not in major_text:
                key2 = "<p>SAMPLE COURSES"
            if key1 in major_text and key2 in major_text:
                item['career_en'] = remove_class(getContentToXpath(major_text, key1, key2))
            # print("item['career_en']: ", item['career_en'])

            '''课程设置'''
            major_name_key = ["Indigenous Studies",
"Anthropology",
"Classics",
"Conflict Resolution Studies",
"Criminal Justice",
"English",
"Filmmaking",
"French Studies",
"German Studies",
"History",
"Interdisciplinary Linguistics",
"International Development Studies",
"Philosophy",
"Political Science",
"Psychology",
"Religion & Culture",
"Rhetoric and Communications",
"Sociology",
"Spanish Studies",
"Theatre and Film",
"Urban and Inner-City Studies",
"Women’S & Gender Studies",
"Business & Administration",
"Economics",
"Economics & Finance",
"Bachelor of Kinesiology",
"Applied Computer Science",
"Bioanthropology",
"Biochemistry",
"Biology",
"Biopsychology",
"Chemistry",
"Environmental Sciences",
"Environmental Studies",
"Geography",
"Mathematics",
"Physics",
"Statistics", ]
            modules_url_value = ["http://uwinnipeg.ca/sample-first-year-programs/arts/aboriginal-gov.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/anthropology.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/classics.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/conflict-res.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/criminal-justice.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/english.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/filmmaking.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/french.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/german.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/history.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/id-linguistics.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/intl-dev.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/philosophy.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/poli-sci.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/psychology.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/religion-culture.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/rhet-writing-comm.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/sociology.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/spanish.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/theatre.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/uic.html",
"http://uwinnipeg.ca/sample-first-year-programs/arts/wgs.html",
"http://uwinnipeg.ca/sample-first-year-programs/bus-econ/business.html",
"http://uwinnipeg.ca/sample-first-year-programs/bus-econ/economics.html",
"http://uwinnipeg.ca/sample-first-year-programs/bus-econ/econ-finance.html",
"http://uwinnipeg.ca/sample-first-year-programs/kinesiology/index.html",
"http://uwinnipeg.ca/sample-first-year-programs/science/acs.html",
"http://uwinnipeg.ca/sample-first-year-programs/science/bioanthro.html",
"http://uwinnipeg.ca/sample-first-year-programs/science/biochemistry.html",
"http://uwinnipeg.ca/sample-first-year-programs/science/biology.html",
"http://uwinnipeg.ca/sample-first-year-programs/science/biopsychology.html",
"http://uwinnipeg.ca/sample-first-year-programs/science/chemistry.html",
"http://uwinnipeg.ca/sample-first-year-programs/science/env-studies.html",
"http://uwinnipeg.ca/sample-first-year-programs/science/env-studies.html",
"http://uwinnipeg.ca/sample-first-year-programs/science/geography.html",
"http://uwinnipeg.ca/sample-first-year-programs/science/mathematics.html",
"http://uwinnipeg.ca/sample-first-year-programs/science/physics.html",
"http://uwinnipeg.ca/sample-first-year-programs/science/statistics.html", ]
            modules_dict = {}
            for i in range(len(major_name_key)):
                modules_dict[major_name_key[i]] = modules_url_value[i]

            modules_url = modules_dict.get(item['major_name_en'])
            if modules_url is not None:
                item['modules_en'] = self.parse_modules(modules_url)
            # print("item['modules_en']: ", item['modules_en'])

            '''学位名称和课程长度'''
            if item['overview_en'] is not None:
                degree_name_re = re.findall(r"Bachelor\sof.*?\)", item['overview_en'].replace("Bache lor", "Bachelor").replace("Sc ience", "Science"))
                print("degree_name_re； ", degree_name_re)

                ''' 2种情况：（1）只有一个学位但是，课程长度有多个
                                (2)有多个学位，并且每个学位可分多个课程长度或者一个    
                '''

                if len(degree_name_re) == 1:
                    degree_name = re.findall(r"Bachelor\sof.*?\(", ''.join(degree_name_re))
                    # print("degree_name: ", degree_name)
                    item['degree_name'] = ''.join(degree_name).replace("degree", "").replace("(", "").strip()
                    if len(item['degree_name']) > 30:
                        item['degree_name'] = ''.join(re.findall(r"Bachelor\sof\sBusiness\sAdministration|Bachelor\sof\s\w+", ''.join(degree_name_re)))
                    print("item['degree_name']: ", item['degree_name'])

                    # 正则匹配课程长度
                    duration_re = re.findall(r"\d-year\sHonours|\d-year|\d\syear\sHonours|or\sHonours\)", ''.join(degree_name_re))
                    print("duration_re: ", duration_re)
                    if len(duration_re) > 0:
                        item['duration_per'] = 1
                        for duration in duration_re:
                            if "Honours" in duration:
                                item['degree_name'] = item['degree_name'] + " Honours"
                                item['duration'] = '4'
                            else:
                                item['duration'] = ''.join(re.findall(r"\d", duration))
                            print("item['degree_name']: ", item['degree_name'])
                            print("item['duration']: ", item['duration'])
                            print("item['duration_per']: ", item['duration_per'])
                            if item['department'] is None:
                                item['department'] = "Faculty of " + item['degree_name'].replace("Bachelor of ", "").strip()
                                if item['tuition_fee'] is None:
                                    item['tuition_fee'] = department_fee.get(item['department'])
                            yield item
                    else:
                        if item['department'] is None:
                            item['department'] = "Faculty of " + item['degree_name'].replace("Bachelor of ", "").strip()
                            if item['tuition_fee'] is None:
                                item['tuition_fee'] = department_fee.get(item['department'])
                        yield item



                elif len(degree_name_re) > 1:
                    for degree_name_duration in degree_name_re:
                        degree_name = re.findall(r"Bachelor\sof.*?\(", remove_tags(degree_name_duration))
                        # print("degree_name--: ", degree_name)
                        item['degree_name'] = ''.join(degree_name).replace("Degree", "").replace("degree", "").replace("(", "").strip()
                        if len(item['degree_name']) > 30:
                            item['degree_name'] = ''.join(re.findall(r"Bachelor\sof\sBusiness\sAdministration|Bachelor\sof\s\w+", degree_name_duration.replace("Adm in istration", "Administration").replace("</p><p>", " ")))
                        print("item['degree_name']2: ", item['degree_name'])

                        # 正则匹配课程长度
                        duration_re = re.findall(r"\d-year\sHonours|\d-year|\d\syear\sHonours|or\sHonours\)",
                                                 remove_tags(degree_name_duration))
                        print("duration_re2: ", duration_re)
                        if len(duration_re) > 0:
                            item['duration_per'] = 1
                            for duration in duration_re:
                                if "Honours" in duration:
                                    item['degree_name'] = item['degree_name'] + " Honours"
                                    item['duration'] = '4'
                                else:
                                    item['duration'] = ''.join(re.findall(r"\d", duration))
                                print("item['degree_name']2: ", item['degree_name'])
                                print("item['duration']2: ", item['duration'])
                                print("item['duration_per']2: ", item['duration_per'])
                                if item['department'] is None:
                                    item['department'] = "Faculty of " + item['degree_name'].replace("Bachelor of ","").strip()
                                    if item['tuition_fee'] is None:
                                        item['tuition_fee'] = department_fee.get(item['department'])
                                yield item
                        else:
                            if item['department'] is None:
                                item['department'] = "Faculty of " + item['degree_name'].replace("Bachelor of ", "").strip()
                                if item['tuition_fee'] is None:
                                    item['tuition_fee'] = department_fee.get(item['department'])
                            yield item
                else:
                    if "Bachelor of" in item['major_name_en']:
                        item['degree_name'] = item['major_name_en']
                    yield item
            else:
                yield item


    # 匹配多个modules的需要拆分
    def parse_modules(self, modules_a_url):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(modules_a_url, headers=headers_base)
        response = etree.HTML(data.text)

        modules_en = response.xpath(
            "//h2[@class='subtitle']/following-sibling::*")
        modules_en_str = ""
        if len(modules_en) > 0:
            for m in modules_en:
                modules_en_str += etree.tostring(m, encoding='unicode', method='html')
        modules_en = remove_class(clear_lianxu_space([modules_en_str]))
        return modules_en

    # 公共字段
    def parse_data(self, item):
        item['school_name'] = "University of Winnipeg"
        item['other'] = '''问题描述：1.课程设置在https://www.uwinnipeg.ca/sample-first-year-programs/index.html上面匹配专业名获取的，有个别的没匹配上，导致为空，PDF上面有课程设置，但是使用代码采集下来格式不对，各个单词中间存在空格，需要手动抓取
			2.就业为空的是PDF页面上没有的
			3.专业描述和课程设置、就业为空的是详情页没有的'''

        '''公共字段'''
        item['campus'] = 'Winnipeg'
        item['location'] = 'Winnipeg'
        item['sat_code'] = item['toefl_code'] = '9379'


        # https://www.uwinnipeg.ca/future-student/apply/index.html#deadlines
        item['start_date'] = '1月,5月,9月'
        item['deadline'] = '2019-03-01,2019-07-02,2019-11-01'
        item['apply_pre'] = 'CAD$'
        item['apply_fee'] = '120'


        item['ielts_desc'] = 'Minimum band score of 6.5 based on the Academic Module'
        item['ielts'] = '6.5'
        item['toefl_desc'] = 'Achieve a minimum score of 80 with no less than 19 in each component.'
        item['toefl'] = '80'
        item['toefl_l'] = '19'
        item['toefl_s'] = '19'
        item['toefl_r'] = '19'
        item['toefl_w'] = '19'
        # item['entry_requirements_en'] = ""

        # https://www.uwinnipeg.ca/future-student/international/countries-a-to-z/-c-.html
        item['require_chinese_en'] = '''<p><strong>Country: </strong>China, People's Republic of<br/>
<strong>Secondary School Credential:</strong> Senior High School Graduation Examination<br/>
<strong>Secondary School Grade:</strong> 70%<br/><strong>University or College Transfer Grade:</strong> 70 - 79% or C<br/>
</p>'''
        item['average_score'] = '70'


    # 读取PDF文件写成本地HTML文件
    def readPDF(self, path, toPath):
        import sys
        import importlib
        importlib.reload(sys)

        from pdfminer.pdfparser import PDFParser, PDFDocument
        from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
        from pdfminer.converter import PDFPageAggregator
        from pdfminer.layout import LTTextBoxHorizontal, LAParams
        from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

        # 以二进制形式打开PDF文件
        f = open(path, "rb")
        # 创建一个PDF文档分析器
        parser = PDFParser(f)

        # 创建PDF文档
        pdfFile = PDFDocument()

        # 连接分析器与文档对象
        parser.set_document(pdfFile)
        pdfFile.set_parser(parser)
        # 提供初始化密码
        pdfFile.initialize()

        # 检测文档是否提供txt转换
        if not pdfFile.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            # 解析数据
            # 数据管理器
            manager = PDFResourceManager()
            # 创建一个PDF设备对象
            laparams = LAParams()
            device = PDFPageAggregator(manager, laparams=laparams)
            # 解释器对象
            interpreter = PDFPageInterpreter(manager, device)


            # 开始循环处理， 每次处理一页
            for page in pdfFile.get_pages():
                interpreter.process_page(page)
                layout = device.get_result()
                for x in layout:
                    if (isinstance(x, LTTextBoxHorizontal)):
                        with open(toPath, "a", encoding='utf-8') as f:
                            str = x.get_text()
                            # print("===", str)
                            f.write("<p>" + str + "</p>\n")
