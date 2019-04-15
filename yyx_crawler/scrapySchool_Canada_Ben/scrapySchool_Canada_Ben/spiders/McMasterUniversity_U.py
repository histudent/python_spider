# -*- coding:utf-8 -*-
"""
# @PROJECT: scrapySchool_Canada_Ben
# @Author: admin
# @Date:   2018-10-29 10:15:44
# @Last Modified by:   admin
# @Last Modified time: 2018-10-29 10:15:44
"""
__author__ = 'yangyaxia'
__date__ = '2018/10/29 09:00'
import scrapy
import re
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from w3lib.html import remove_tags
from lxml import etree
import requests

class McMasterUniversity_USpider(scrapy.Spider):
    name = "McMasterUniversity_U"
    start_urls = ["https://future.mcmaster.ca/programs/"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        # 所有的专业链接
        alllinks = response.xpath("//div[@id='programs-row']/div//a/@href").extract()
        # print(len(alllinks))

        for url in alllinks:
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)
        item['school_name'] = "McMaster University"
        item['url'] = response.url
        print("===========================")
        print(response.url)
        item['other'] = '''问题描述：1.学院和学费是根据先前的表格匹配获得的，不是所有的专业都有，能够匹配上
        2.没有entry_requirements
        3.课程长度是根据先前的表格赋值的
        4.专业描述和课程设置、就业为空的是详情页没有的'''

        '''公共字段'''
        item['campus'] = 'Hamilton'
        item['location'] = 'Hamilton'
        item['sat_code'] = item['toefl_code'] = '0936'
        item['act_code'] = '5326'
        item['start_date'] = '9月'
        item['duration'] = '4'
        item['duration_per'] = 1
        item['apply_pre'] = 'CAD$'
        item['apply_fee'] = '100'
        item['tuition_fee_pre'] = 'CAD$'

        # https://future.mcmaster.ca/admission/language-2/
        item['ielts_desc'] = '6.5 Overall with a minimum of 6.0 in each of the four components (Reading, Writing, Speaking, Listening); results valid for 2 years'
        item['ielts'] = '6.5'
        item['ielts_l'] = '6.0'
        item['ielts_s'] = '6.0'
        item['ielts_r'] = '6.0'
        item['ielts_w'] = '6.0'
        item['toefl_desc'] = 'IBT: 86 Overall with a minimum score of 20 in each of the four components (Reading, Writing, Speaking, Listening); valid for 2 years'
        item['toefl'] = '86'
        item['toefl_l'] = '20'
        item['toefl_s'] = '20'
        item['toefl_r'] = '20'
        item['toefl_w'] = '20'

        # https://future.mcmaster.ca/admission/requirements/
        item['require_chinese_en'] = '''<p>Senior High School (Upper Middle School) Graduation Diploma and Academic Proficiency test/Huikao and Gaokao.</p>
<p>NOTE: Applicants who do not present Gaokao must provide a letter stating the reason(s) for not sitting Gaokao. We require transcripts for the last three years of Upper Middle School, results of standardized tests (eg. SAT, ACT, IB, AP, GCE) and school profile.</p>
<p>NOTE: Applicants presenting a combination of Chinese curriculum and British Pattered A Levels must present three different A(2) Level subjects required for the program of application.</p>'''
        try:
            major_name = response.xpath("//h1[@class='banner-title banner-title-lg banner-title-line banner-text-rev']//text()").extract()
            item['major_name_en'] = ''.join(major_name).replace("(BHSc)", "").replace("(Bachelor Fine Arts)", "").strip()
            print("item['major_name_en']: ", item['major_name_en'])

            department_res = response.xpath("//h2[contains(text(),'Web Links')]/following-sibling::ul//a[contains(text(),'Faculty of')]//text()|"
                                            "//h2[contains(text(),'Web Links')]/following-sibling::ul//a[contains(text(),'DeGroote School of Medicine')]//text()").extract()
            print("department_res: ", department_res)
            if len(department_res) > 0:
                item['department'] = department_res[0].replace("Book a", "").replace("Tour", "").strip()
            department_list = ["DeGroote School of Business",
"DeGroote School of Business",
"Faculty of Engineering",
"Faculty of Engineering",
"Faculty of Engineering",
"Faculty of Engineering",
"Faculty of Engineering",
"Faculty of Engineering",
"Faculty of Engineering",
"Faculty of Engineering",
"Faculty of Engineering",
"Faculty of Health Sciences",
"Faculty of Health Sciences",
"Faculty of Humanities",
"Faculty of Humanities",
"Faculty of Humanities",
"Faculty of Science",
"Faculty of Science",
"Faculty of Science",
"Faculty of Science",
"Faculty of Science",
"Faculty of Science",
"Faculty of Social Sciences", ]
            major_name_list = ["Business",
"Integrated Business & Humanities",
"Engineering",
"Engineerin",
"Integrated Biomedical Engineering & Health Sciences",
"Integrated Biomedical Engineering & Health Sciences",
"Computer Science",
"Computer Science-Co op",
"Automotive & Vehicle Engineering Technology",
"Bachelor of Technology",
"Automation Engineering Technology",
"Health Sciences",
"Nursing",
"Humanities",
"Music",
"Studio Art",
"Chemical and Physical Sciences",
"Environmental & Earth Sciences Gateway",
"Integrated Science",
"Kinesiology",
"Life Sciences Gateway",
"Mathematics & Statistics Gateway",
"Social Sciences", ]
            department_dict = {}
            for d in range(len(department_list)):
                department_dict[major_name_list[d]] = department_list[d]
            if item['department'] is None:
                item['department'] = department_dict.get(item['major_name_en'])
            print("item['department']: ", item['department'])

            tuition_fee_list = ["34119",
"34119",
"40008",
"40008",
"40008",
"40008",
"30691",
"30691",
"31373",
"31373",
"31373",
"28484",
"31433",
"27151",
"27151",
"27151",
"28505",
"28505",
"24902",
"28505",
"28505",
"28505",
"27156",
"28000", ]
            major_name_tuition_fee_list = ["Business",
"Integrated Business & Humanities",
"Engineering",
"Engineerin",
"Integrated Biomedical Engineering & Health Sciences",
"Integrated Biomedical Engineering & Health Sciences",
"Computer Science",
"Computer Science-Co op",
"Automotive & Vehicle Engineering Technology",
"Bachelor of Technology",
"Automation Engineering Technology",
"Health Sciences",
"Nursing",
"Humanities",
"Music",
"Studio Art",
"Chemical and Physical Sciences",
"Environmental & Earth Sciences Gateway",
"Integrated Science",
"Kinesiology",
"Life Sciences Gateway",
"Mathematics & Statistics Gateway",
"Social Sciences",
"Arts & Science",]
            tuition_fee_dict = {}
            for d in range(len(tuition_fee_list)):
                tuition_fee_dict[major_name_tuition_fee_list[d]] = tuition_fee_list[d]
            item['tuition_fee'] = tuition_fee_dict.get(item['major_name_en'])
            print("item['tuition_fee']: ", item['tuition_fee'])

            overview_en = response.xpath(
                "//div[@class='entry-content']//div//*[contains(text(),'Why ')]/preceding-sibling::*").extract()
            if len(overview_en) == 0:
                overview_en = response.xpath(
                    "//h2[contains(text(),'Overview')]/following-sibling::div[1]/p").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
            if item['overview_en'] == "":
                item['overview_en'] = None
                print("overview_en 为空")
            # print("item['overview_en']: ", item['overview_en'])

            # modules_en    //h5[@class='mb-0']//button[contains(@class,'btn btn-link')]
            modules_en = response.xpath(
                "//div[@id='first-year-courses-content']//h5[@class='mb-0']//button[contains(@class,'btn btn-link')]").extract()
            modules_en = ''.join(modules_en).replace("<button", '<p').replace("</button>", '</p>')
            item['modules_en'] = remove_class(clear_lianxu_space([modules_en]))
            if item['modules_en'] == "":
                item['modules_en'] = None
                print("modules_en 为空")
            # print("item['modules_en']: ", item['modules_en'])

            # career_en     //h3[contains(text(),'Careers or Options Beyond This Program')]/following-sibling::*[1]
            career_en = response.xpath(
                "//h3[contains(text(),'Careers or Options Beyond This Program')]/following-sibling::*[1]|"
                "//h3[contains(text(),'Career or Options Beyond This Program')]/following-sibling::*[1]|"
                "//h3[contains(text(),'Careers/Options Beyond This Program')]/following-sibling::*[1]|"
                "//h3[contains(text(),'Careers/Opportunities Beyond This Program')]/following-sibling::*[1]").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            if item['career_en'] == "":
                item['career_en'] = None
                print("career_en 为空")
            # print("item['career_en']: ", item['career_en'])



            # 以下值不一样
            # "student-program-preference": "450",
            post_dict = {"student-status": "attending-international",
    "student-province-territory": "alberta",
    "student-filterby": "filterby-curriculum",
    "student-background": "cegep",
    "student-type-as": "american_style_curriculum",
    "student-type-gce": "general_certificate_education",
    "student-type-ib": "international_baccalaureate",
    "student-type--ap": "advanced_placement",
    "action": "admission_form_process", }
            key_value = response.xpath('//input[@name="student-program-preference"]/@value').extract()
            key_value = ''.join(key_value).strip()
            # print(key_value)
            post_dict['student-program-preference'] = key_value

            '''post 请求详细信息'''
            detail_dict = self.parse_detail_data(post_dict)

            item['deadline'] = detail_dict['deadline']
            # print("item['deadline']: ", item['deadline'])

            item['act_desc'] = detail_dict['act_desc'].replace("Submit an ACT composite score of at least", "").strip()
            # print("item['act_desc']: ", item['act_desc'])

            item['sat1_desc'] = detail_dict['sat1_desc']
            print("item['sat1_desc']: ", item['sat1_desc'])

            item['alevel'] = detail_dict['alevel']
            # print("item['alevel']: ", item['alevel'])

            item['ib'] = detail_dict['IB']
            # print("item['ib']: ", item['ib'])

            item['ap'] = detail_dict['ap']
            # print("item['ap']: ", item['ap'])

            degree_name = detail_dict['degree_name']
            print("degree_name: ", degree_name)
            if "," in degree_name:
                degree_name_list = degree_name.split(',')
                for d in degree_name_list:
                    item['degree_name'] = d.strip()
                    print("item['degree_name']: ", item['degree_name'])
                    yield item
            else:
                item['degree_name'] = degree_name
                print("item['degree_name']: ", item['degree_name'])
                # Bachelor of Technology的特殊情况
                if response.url == "https://future.mcmaster.ca/programs/btech/":
                    item['degree_name'] = item['major_name_en'] = "Bachelor of Technology"
                    # spe_major_name_list = ["Automotive and Vehicle Engineering Technology", "Biotechnology", "Automation Engineering Technology"]
                    spe_career_en_list = ["<p>Graduates could be involved in the automotive industry with research and technology applications related to:</p> <ul> <li>development of new automotive products and revision of existing ones</li> <li>collaboration in research and development</li> <li>production planning and designing new production processes</li> <li>conducting and developing test procedures</li> <li>automotive product design, manufacturing and quality improvement</li> </ul> <p>Some careers our recent grads are pursuing include:</p> <ul> <li>Design Engineer (Honda)</li> <li>Research Engineer (Ford)</li> <li>Management Associate (US Steel)</li> <li>M.Eng Design, McMaster University</li> <li>MASc, Mechanical Engineering, McMaster University</li> </ul>",
                                          "<p>Graduates will qualify for positions in government, university and industry. They will also strengthen the competitiveness of businesses in biotechnology with research and technology applications related to:</p> <ul> <li>biotechnology</li> <li>genetic engineering</li> <li>pharmaceuticals</li> <li>food production</li> <li>analytical and testing services</li> <li>policies and regulations</li> </ul> <p>Some careers our recent grads are pursuing include:</p> <ul> <li>Chemist, Esteè Lauder</li> <li>Production Supervisor, (Bungee)</li> <li>M.Sc. Ontario Institute for Cancer Research, UOIT</li> <li>Master of Biotechnology, University of Toronto</li> <li>PhD in Biomedical Engineering, McMaster University</li> </ul>",
                                          "<p>Graduates can work for companies in various industrial processing and manufacturing sectors related to:</p> <ul> <li>primary steel</li> <li>chemicals</li> <li>petrochemicals</li> <li>pharmaceuticals</li> <li>power generation</li> </ul> <p>Some careers our recent grads are pursuing include:</p> <ul> <li>Process Controls Specialist, GE Water and Process Technologies</li> <li>Senior Automation Analyst, Arcelor-Mittal Dofasco</li> <li>M.A.Sc. Electrical &amp; Computer Engineering, McMaster University</li> <li>M.Eng Manufacturing, McMaster University</li> </ul>"]
                    # for i in range(len(spe_major_name_list)):
                    #     item['major_name_en'] = spe_major_name_list[i]
                    item['career_en'] = ''.join(spe_career_en_list)
                    yield item
                else:
                    if item['degree_name'] == "":
                        item['degree_name'] = None
                    yield item

        except Exception as e:
            with open("scrapySchool_Canada_Ben/error/" + item['school_name'] + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_detail_data(self, post_dict):
        # 请求网址：https://future.mcmaster.ca/wp-admin/admin-ajax.php
        data = requests.post("https://future.mcmaster.ca/wp-admin/admin-ajax.php", data=post_dict)
        res = etree.HTML(data.text)


        # 申请截止日期
        deadline = res.xpath("//strong[contains(text(),'Application Deadline:')]/../text()")
        deadline_str = ""
        if len(deadline) > 0:
            deadline_str = deadline[0].strip()
        # print("deadline_str: ", deadline_str)
        monthDict = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06",
                     "july": "07", "august": "08", "september": "09", "october": "10", "november": "11",
                     "december": "12",
                     "jan": "01", "feb": "02", "mar": "03", "apr": "04", "jun": "06",
                     "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12",
                     "sept": "09", }
        month_re = re.findall(r"january|february|march|april|may|june|july|august|september|october|november|december",
                              deadline_str, re.I)
        # print("month_re: ", month_re)
        month_re = monthDict.get(''.join(month_re).strip().lower())
        # print("month_re: ", month_re)

        day_re = re.findall(r"\d+,", deadline_str)
        day_re = ''.join(day_re).replace(',', '').strip()
        if day_re != "" and int(day_re) < 10:
            day_re = "0" + day_re
        # print("day_re: ", day_re)

        year_re = re.findall(r"201\d", deadline_str)
        year_re = ''.join(year_re).strip()
        # print("year_re: ", year_re)

        deadline_end = None
        if year_re != "":
            deadline_end = year_re + "-" + month_re + "-" + day_re

        # degree_name
        degree_name = res.xpath("//strong[contains(text(),'Degrees:')]/../text()")
        degree_name_str = ''.join(degree_name).strip()

        # SAT1  SAT2    ACT
        # item['sat1_desc'] = None
        # item['sat2_desc'] = None
        # item['act_desc'] = None
        ACT = res.xpath("//li[contains(text(),'ACT')]//text()")
        act_desc = ''.join(ACT).strip()

        sat1 = res.xpath("//li[contains(text(),'SAT I')]//text()")
        sat1_desc = ''.join(sat1).strip()
        if "Submit a combined SAT I score of at least 1200" in sat1_desc:
            sat1_desc = "1200"
        # print(sat1_desc)

        # entry_requirements    //h2[contains(text(),'General Certificate of Education Student:')]
        tmp_html = data.text
        key = re.findall(r'<p><h2>General Certificate of Education Student:</h2>', tmp_html)
        # print(key)
        key1 = re.findall(r'<h2>International Baccalaureate Requirements:</h2>', tmp_html)
        # print(key1)
        key2 = re.findall(r'<h2>Advanced Placement \(AP\) Requirements</h2>', tmp_html)
        # print(key2)
        key3 = re.findall(r'<h2>English Language Proficiency \(ELP\) Requirements</h2>', tmp_html)
        # print(key3)

        # entry_requirements
        # entry_html = tmp_html.replace(''.join(key), '<div id="container">'+''.join(key)).replace(''.join(key1), '</div>'+''.join(key1))
        # entry_html_response = etree.HTML(entry_html)
        # # 可以使用xpath匹配需要的内容了
        # admisson = entry_html_response.xpath("//div[@id='container']")
        # # 转化成带标签的数据内容
        # entry_requirements = remove_class(clear_lianxu_space([etree.tostring(admisson[0], encoding='unicode', method='html')]))
        # # print(entry_requirements)

        # IB

        alevel_str = res.xpath("//p[contains(text(),'‘A’ Level')]//text()")
        alevel = ""
        if len(alevel_str) > 0:
            alevel = 'A'
        # print(alevel)

        IB_html = tmp_html.replace(''.join(key1), '<div id="container">' + ''.join(key1)).replace(''.join(key2), '</div>' + ''.join(key2))
        IB_html_response = etree.HTML(IB_html)
        # print(IB_html)
        # 可以使用xpath匹配需要的内容了
        admisson = IB_html_response.xpath("//div[@id='container']//text()")
        # 转化成带标签的数据内容
        IB = clear_lianxu_space(admisson)
        # print(IB)

        # ap
        ap_html = tmp_html.replace(''.join(key2), '<div id="container">' + ''.join(key2)).replace(''.join(key3), '</div>' + ''.join(key3))
        ap_html_response = etree.HTML(ap_html)
        # 可以使用xpath匹配需要的内容了
        admisson = ap_html_response.xpath("//div[@id='container']//text()")
        # 转化成带标签的数据内容
        ap = clear_lianxu_space(admisson)
        # print(ap)

        detail_dict = {}
        detail_dict['deadline'] = deadline_end
        detail_dict['degree_name'] = degree_name_str
        detail_dict['act_desc'] = act_desc
        detail_dict['sat1_desc'] = sat1_desc
        detail_dict['alevel'] = alevel
        detail_dict['IB'] = IB
        detail_dict['ap'] = ap
        return detail_dict













