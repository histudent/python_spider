# -*- coding:utf-8 -*-
"""
# @PROJECT: scrapySchool_Canada_Ben
# @Author: admin
# @Date:   2018-11-07 11:21:44
# @Last Modified by:   admin
# @Last Modified time: 2018-11-07 11:21:44
"""
__author__ = 'yangyaxia'
__date__ = '2018/11/07 11:21'
import scrapy
import re
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from w3lib.html import remove_tags
from lxml import etree
import requests

class UniversityofManitoba_USpider(scrapy.Spider):
    name = "UniversityofManitoba_U"
    start_urls = ["http://umanitoba.ca/student/admissions/programs/"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        # print("*********")
        links = response.xpath("//div[@id='centerInfo']/dl/blockquote/p/a/@href").extract()
        print(len(links))
        links = list(set(links))
        # 76
        print(len(links))
        for link in links:
            if "/student/admissions/programs/" in link:
                url = "http://umanitoba.ca" + link
                yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)
        item['school_name'] = "University of Manitoba"
        item['url'] = response.url
        print("===========================")
        print(response.url)
        item['other'] = '''问题描述：1.学位展示不规律，拆分可能存在不准确的情况
        2.有课程设置和就业信息、课程长度为空的是详情页没有的
        3.学费为空是没有匹配上的专业'''

        '''公共字段'''
        # item['campus'] = 'Hamilton'
        # item['location'] = 'Fredericton, NB, Canada'
        item['sat_code'] = item['toefl_code'] = '0973'

        # http://umanitoba.ca/student/admissions/finances/tuition-fees.html
        item['apply_pre'] = 'CAD$'
        item['apply_fee'] = '120'

        # http://umanitoba.ca/student/records/deadlines/index.html
        # item['start_date'] = '1月,5月,9月'
        # item['deadline'] = '2018-12-31,2019-03-01'
        # http://umanitoba.ca/student/admissions/international/asia.html
        item['tuition_fee_pre'] = 'CAD$'
        # item['tuition_fee'] = ''

        # http://umanitoba.ca/student/admissions/media/pdf/Requirement_sheet_-_General.pdf
        item['ielts_desc'] = '6.5 overall band score'
        item['ielts'] = '6.5'
        item['toefl_desc'] = '(86 total score with a min. of 20 in each component) '
        item['toefl'] = '86'
        item['toefl_l'] = '20'
        item['toefl_s'] = '20'
        item['toefl_r'] = '20'
        item['toefl_w'] = '20'
        item['entry_requirements_en'] = """<strong>IF YOU ARE A HIGH SCHOOL STUDENT</strong>
<p>If you’re coming to university directly from high school or have completed less than one year of university studies, you’ll take the direct entry route into a faculty or program: this means beginning in University 1 (U1), or applying to a program that offers a direct entry option. U1 is a unique approach to your first year at the U of M, giving you the opportunity to design an individualized schedule that meets the admission and/or first year requirements for one or more target degree programs. U1 will not add any time or cost to your degree; it serves as year 1 of any 3 or 4 year degree program</p>"""

        # http://umanitoba.ca/student/admissions/international/common-international-curriculums.html
        item['alevel'] = 'Minimum 2 courses at Advanced (A) level and 3 courses at Ordinary (O) level: no grades below a ‘D’ (GCE)'
        item['ib'] = "An IB diploma with 3 courses at the higher level (HL) and 3 courses at the standard level (SL): no grades below a ‘4’ (IB)"

        # http://umanitoba.ca/student/admissions/media/pdf/Requirement_sheet_-_USA.pdf
        item['act_desc'] = item['sat1_desc'] = "NO ACT/SAT REQUIRED"
        item['ap'] = """Advanced Placement (Ap) And International Baccalaureate (IB)
        The University of Manitoba recognizes the Advanced Placement (AP) and International Baccalaureate (IB) programs for admission, scholarships, and university transfer credit. Credits will be transferred as follows:
        AP: 4=B; 5=A; 5 and 95% on the final exam=A+
        IB: 4=B; 5=B+; 6=A; 7=A+"""

        # http://umanitoba.ca/student/admissions/media/pdf/Requirement_sheet_-_General.pdf
        item['require_chinese_en'] = '<p>High school graduation with a minimum average of 70% in three (3) senior level courses, with at least 60% in first language literature. </p>'
        try:
            departmentMajor = response.xpath("//div[@id='centerHeader']//text()").extract()
            departmentMajor_str = ''.join(departmentMajor).strip()
            print(departmentMajor_str)
            if "Diploma" not in departmentMajor_str:
                if "- " in departmentMajor_str:
                    programmeDepartment = departmentMajor_str.split("- ")
                    # 专业
                    item['major_name_en'] = programmeDepartment[-1]
                    # 学院
                    item['department'] = programmeDepartment[0]
                elif ":" in departmentMajor_str:
                    programmeDepartment = departmentMajor_str.split(":")
                    # 专业
                    item['major_name_en'] = programmeDepartment[-1]
                    # 学院
                    item['department'] = programmeDepartment[0]
                elif "&" in departmentMajor_str:
                    programmeDepartment = departmentMajor_str.split("&")
                    # 专业
                    item['major_name_en'] = programmeDepartment[-1]
                    # 学院
                    item['department'] = programmeDepartment[0]
                else:
                    item['department'] = item['major_name_en'] = departmentMajor_str
                item['department'] = item['department'].strip()
                print("item['department']: ", item['department'])

                item['major_name_en'] = item['major_name_en'].strip()
                print("item['major_name_en']: ", item['major_name_en'])


                overview = response.xpath("//*[contains(text(),'Program description')]/../../following-sibling::p[1]").extract()
                item['overview_en'] = remove_class(clear_lianxu_space(overview)).replace("<p></p>", "").strip()
                if item['overview_en'] == "<p><strong><span>Program options</span></strong></p>":
                    overview_xpath = "//span[contains(text(),'Program description')]/../../../text()"
                    overview = response.xpath(overview_xpath).extract()
                    item['overview_en'] = "<p>" + remove_class(clear_lianxu_space(overview)).strip() + "</p>"
                if item['overview_en'] == "":
                    overview_xpath = "//span[contains(text(),'Program description')]/../following-sibling::p[1]"
                    overview = response.xpath(overview_xpath).extract()
                    item['overview_en'] = remove_class(clear_lianxu_space(overview)).replace("<p></p>", "").strip()
                if item['overview_en'] == "":
                    item['overview_en'] = None
                # print("item['overview_en']: ", item['overview_en'])

                tmp_html = response.text
                # 就业
                career = response.xpath("//strong[contains(text(),'Professional opportunities')]/..|"
                                        "//strong[contains(text(),'Professional opportunities')]/../following-sibling::ul[1]").extract()
                if len(career) == 0:
                    career = response.xpath("//*[contains(text(),'Professional opportunities')]/../..|"
                                                "//*[contains(text(),'Professional opportunities')]/../../following-sibling::ul[1]").extract()
                career_end = remove_class(clear_lianxu_space(career))
                # print("career_end: ", career_end)
                if ''.join(career_end).replace("<ul></ul>", "").strip() == '<p><strong><span>Professional opportunities</span></strong></p>' or '>Program description' in career_end or ''.join(career_end) == '<span><strong>Professional opportunities</strong></span>':
                    career_key1 = r'<p><strong><span style="font-size: 14pt">Professional opportunities'
                    if career_key1 not in tmp_html:
                        career_key1= r'<strong><span style="font-size: 14pt">Professional opportunities'
                        if career_key1 not in tmp_html:
                            career_key1 = r'<p><span style="font-size: 14pt"><strong>Professional opportunities'
                    career_key2 = r'<p><strong><span style="font-size: 14pt">Admission '
                    if career_key2 not in tmp_html:
                        career_key2 = r'<p><span style="font-size: 14pt"><strong>Admission '
                    career_end = getContentToXpath(tmp_html, career_key1, career_key2)
                    career_end = remove_class(clear_lianxu_space([career_end]))

                    if len(career_end) == 0:
                        career = response.xpath("//*[contains(text(),'Professional opportunities')]/../..|"
                                                "//*[contains(text(),'Professional opportunities')]/../../following-sibling::*[1]").extract()
                        career_end = remove_class(clear_lianxu_space(career))
                # print("career_end2: ", career_end)
                if career_end == "":
                    item['career_en'] = None
                else:
                    item['career_en'] = career_end
                # print("item['career_en']: ", item['career_en'])

                '''modules'''
                modules_key1 = r'<p><strong><span style="font-size: 14pt">Interesting courses and unique opportunities'
                modules_key2 = r'<p><strong><span style="font-size: 14pt">Professional opportunities'
                if modules_key2 not in tmp_html:
                    modules_key2 = r'<p><span style="font-size: 14pt"><strong>Professional opportunities'
                if modules_key1 in tmp_html and modules_key2 in tmp_html:
                    modules_list1 = getContentToXpath(tmp_html, modules_key1, modules_key2)
                    if len(modules_list1) > 0:
                        item['modules_en'] = remove_class(clear_lianxu_space([modules_list1]))
                if item['modules_en'] is None:
                    modules = response.xpath("//span[contains(text(),'Interesting courses and unique opportunities')]/..|"
                                             "//span[contains(text(),'Interesting courses and unique opportunities')]/../../following-sibling::ul[1]").extract()
                    if len(modules) > 1:
                        item['modules_en'] = remove_class(clear_lianxu_space(modules))
                if item['modules_en'] is None:
                    modules = response.xpath("//span[contains(text(),'Interesting courses and unique opportunities')]/..|"
                                             "//span[contains(text(),'Interesting courses and unique opportunities')]/../following-sibling::ul[1]|"
                                             "//strong[contains(text(),'Interesting courses and unique opportunities')]/..|"
                                             "//strong[contains(text(),'Interesting courses and unique opportunities')]/../../following-sibling::ul[1]").extract()
                    if len(modules) > 0:
                        item['modules_en'] = remove_class(clear_lianxu_space(modules))
                # print("item['modules_en']: ", item['modules_en'])

                '''学费'''
                tuition_fee_dict = {}
                tuition_fee_key = ["University 1",
                                   "Faculty of Agricultural",
                                   "Faculty of Agricultural & Food Sciences",
                                   "Faculty of Architecture",
                                   "Faculty of Arts",
                                   "Asper School of Business",
                                   "Faculty of Education",
                                   "Faculty of Engineering",
                                   "Clayton H. Riddell Faculty of  Environment, Earth, & Resources",
                                   "School of Art",
                                   "Health Studies",
                                   "Health Sciences",
                                   "Faculty of Kinesiology & Recreation Management",
                                   "Faculty of Law",
                                   "Desautels Faculty of Music",
                                   "Nursing",
                                   "Faculty of Science",
                                   "Faculty of Social Work", ]
                tuition_fee_value = ["16,000",
                                     "18,000","18,000",
                                     "18,500",
                                     "14,500",
                                     "20,000",
                                     "16,000",
                                     "21,500",
                                     "17,500",
                                     "18,500",
                                     "16,500",
                                     "16,500",
                                     "19,500",
                                     "26,500",
                                     "18,000",
                                     "18,500",
                                     "17,500",
                                     "19,000", ]
                for i in range(len(tuition_fee_key)):
                    tuition_fee_dict[tuition_fee_key[i]] = tuition_fee_value[i]
                item['tuition_fee'] = tuition_fee_dict.get(item['department'])
                if item['major_name_en'] == "College of Nursing":
                    item['tuition_fee'] = "18,500"
                # print("item['tuition_fee']: ", item['tuition_fee'])

                if item['major_name_en'] == "Health Sciences" or item['major_name_en'] == "Health Studies" or item['major_name_en'] == "Family Social Sciences":
                    item['department'] = "Rady Faculty of Health Sciences"
                '''start_date'''
                start_date_dict = {"University 1": "1月,5月,9月",
"Faculty of Agricultural & Food Sciences": "9月",
"Faculty of Architecture": "9月",
"Faculty of Arts": "1月,5月,9月",
"Asper School of Business": "9月",
"Faculty of Education": "9月",
"Faculty of Engineering": "9月",
"Clayton H. Riddell Faculty of  Environment, Earth, & Resources": "1月,5月,9月",
"School of Art": "9月",
"Rady Faculty of Health Sciences": "9月",
"Faculty of Kinesiology & Recreation Management": "9月",
"Faculty of Law": "9月",
"Desautels Faculty of Music": "9月",
"Faculty of Science": "1月,5月,9月",
"Faculty of Social Work": "9月", }
                item['start_date'] = start_date_dict.get(item['department'])
                print("item['start_date']: ", item['start_date'])

                '''deadline'''
                deadline_dict = {"University 1": "2019-12-01,2019-04-01,2019-03-01",
"Faculty of Agricultural & Food Sciences": "2019-03-01",
"Faculty of Architecture": "2019-03-01",
"Faculty of Arts": "2019-10-01,2019-03-01,2019-03-01",
"Asper School of Business": "2019-03-01",
"Faculty of Education": "2019-03-01",
"Faculty of Engineering": "2019-03-01",
"Clayton H. Riddell Faculty of  Environment, Earth, & Resources": "2019-10-01,2019-03-01,2019-03-01",
"School of Art": "2019-03-01",
"Rady Faculty of Health Sciences": "2019-03-01",
"Faculty of Kinesiology & Recreation Management": "2019-03-01",
"Faculty of Law": "2019-03-01",
"Desautels Faculty of Music": "2019-01-15",
"Faculty of Science": "2019-10-01,2019-03-01,2019-03-01",
"Faculty of Social Work": "2019-03-01", }
                item['deadline'] = deadline_dict.get(item['department'])
                print("item['deadline']: ", item['deadline'])

                # degree_name_list = response.xpath("//strong[contains(text(),'Degree options')]/..//text()").extract()
                # print("degree_name_list: ", degree_name_list)
                # 学位名称

                d_key1 = r"<p><strong>Degree options"
                d_key2 = r"<p><strong>Program options"
                if d_key2 not in tmp_html:
                    d_key2 = r'<p><strong><span style="font-size: 14pt">Interesting courses and unique opportunities'
                degree_name_list1 = getContentToXpath(tmp_html, d_key1, d_key2)
                # print(degree_name_list1)
                degree_name_list_str = remove_tags(degree_name_list1).replace("Degree options", "").strip()
                # print("degree_name_list_str: ", degree_name_list_str)
                degree_name_list = degree_name_list_str.split('\n')
                # print("degree_name_list===: ", degree_name_list)
                if len(degree_name_list_str) == 0:
                    degree_name_list = response.xpath(
                        "//strong[contains(text(),'Degree options')]/..//text()").extract()
                    if ''.join(degree_name_list).strip() == "Degree options":
                        degree_name_list = response.xpath(
                            "//strong[contains(text(),'Degree options')]/../following-sibling::p[1]//text()").extract()
                    if len(degree_name_list) == 0:
                        degree_name_list = response.xpath(
                            "//strong[contains(text(),'Degree options')]/../following-sibling::ul[1]//text()").extract()
                    clear_space(degree_name_list)
                    # degree_name_list.remove('Degree options')
                print("degree_name_list: ", degree_name_list)

                if len(degree_name_list) > 0:
                    for d in degree_name_list:
                        # 两种情况，一种包含bachelor of，一种不包含只有学位简写
                        if "Bachelor of" in d or "B." in d:
                            print("d===========", d)
                            degree_name_pre = re.findall(r"[\w\W]+Bachelor\sof", d)
                            # print(degree_name_pre, "---")
                            if "–" in d:
                                duration_degree_name = d.split('– ')
                                duration_re = re.findall(r"[\.\w\s]+year", duration_degree_name[-1])
                                print(duration_re, "===")
                                if len(duration_re) > 0:
                                    item['duration'] = ''.join(duration_re).replace("year", "").replace(" or", ",").strip()
                                    item['duration_per'] = 1
                                item['degree_name'] = duration_degree_name[0].replace(''.join(degree_name_pre).replace("Bachelor of", "").strip(), "").strip()
                            elif "- " in d or "- ":
                                duration_degree_name = d.split('- ')
                                duration_re = re.findall(r"[\.\w\s]+year|[\.\w\s]+Year", duration_degree_name[-1])
                                print(duration_re, "===")
                                if len(duration_re) > 0:
                                    item['duration'] = ''.join(duration_re).replace("year", "").replace(" or",
                                                                                                        ",").strip()
                                    item['duration_per'] = 1
                                item['degree_name'] = duration_degree_name[0].replace(
                                    ''.join(degree_name_pre).replace("Bachelor of", "").strip(), "").strip()
                            else:
                                item['degree_name'] = d.replace(''.join(degree_name_pre).replace("Bachelor of", "").strip(), "").strip()
                            if item['major_name_en'] == "Bachelor of Education":
                                item['degree_name'] = "Bachelor of Education"
                            if item['major_name_en'] == "Health Studies":
                                item['degree_name'] = "Bachelor of Health Studies"
                            print("item['degree_name']: ", item['degree_name'])
                            print("item['duration']: ", item['duration'])
                            print("item['duration_per']: ", item['duration_per'])

                            yield item
                # else:
                #     if item['major_name_en'] == "Bachelor of Education":
                #         item['degree_name'] = "Bachelor of Education"
                #     if item['major_name_en'] == "Health Studies":
                #         item['degree_name'] = "Bachelor of Health Studies"
                #     yield item
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