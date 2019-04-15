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

class ConcordiaUniversity_USpider(scrapy.Spider):
    name = "ConcordiaUniversity_U"
    start_urls = ["https://www.concordia.ca/academics/undergraduate.html"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        # 所有的专业链接
        alllinks = response.xpath("//table[@id='degree_program_table']/tbody/tr/td[1]/a/@href").extract()
        # print(len(alllinks))

        for link in alllinks:
            url = "https://www.concordia.ca" + link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)
        item['school_name'] = "Concordia University"
        # item['campus'] = 'Antigonish'
        # item['location'] = 'Antigonish'
        item['url'] = response.url
        print("===========================")
        print(response.url)
        item['other'] = '''1.Concordia申请专业没有校区，根据选课的课程所在的校区上课
        2.开学时间空着是详情页上没有的'''
        try:
            # degree_type
            department = response.xpath(
                "//div[@class='span8 ordinal-group-1']/a[contains(text(), 'Faculty of')]//text()|"
                "//div[@class='span8 ordinal-group-1']/a[contains(text(), 'Gina Cody School of Engineering and Computer Science')]//text()|"
                "//div[@class='span8 ordinal-group-1']/a[contains(text(), 'John Molson School of Business')]//text()").extract()
            print(department)
            # if len(department) > 0:
            #     item['department'] = department[0]
            item['department'] = ', '.join(department)
            print("item['department']: ", item['department'])

            # 专业
            programme = response.xpath(
                "//div[@class='span8 ordinal-group-1']/h1//text()").extract()
            programme = ''.join(programme)
            degree_type = re.findall(r"\([\w\s,/]+\)", programme)
            degree_type = ''.join(degree_type)
            # print("degree_type: ", degree_type)
            degree_type_str = degree_type.strip().strip("(").strip(")")
            # print("degree_type_str: ", degree_type_str)

            programme = programme.strip()
            if degree_type != "":
                programme = programme.split(degree_type)
            item['major_name_en'] = ''.join(programme).replace("(BA)", "").replace("(BFA)", "").replace("(BA. Cert)", "").replace(" (BEd)", "").strip()
            print("item['major_name_en']: ", item['major_name_en'])

            if "Minor" not in degree_type_str:
                # AP
                # apDict = {'Art History': 'ARTH 200 (6)* or GFAR (6)', 'Biology': 'BIOL 201 (3) and BIOL 1st year level (3)',
                #           'Calculus AB\xa0': 'MATH 203 (3), with exemption from MATH 201, 206 and 209*',
                #           'Calculus BC': 'MATH 203 (3) and MATH 205 (3), with exemption from MATH 201, 206 and 209*',
                #           'Chemistry': 'CHEM 205 (3) and CHEM 206 (3)', 'Chinese': 'MCHI 1st year level (6)',
                #           'Computer Science A': 'COMP 248 (3)', 'Economics: Macroeconomics': 'ECON 203 (3)',
                #           'Economics: Microeconomics': 'ECON 201 (3)',
                #           'English Language and Composition': 'ENGL 1st year level (6)\xa0',
                #           'English Literature and Composition': 'ENGL 1st year level (6)\xa0',
                #           'Environmental Science': 'GEOG 1st year level (3)', 'French Language': 'FRAN 211 (6)\xa0',
                #           'French Literature': 'FRAN 1st year level (6)',
                #           'German Language and Culture': 'GERM 200 (6) with exemptions for GERM 201 and GERM 202',
                #           'Government and Politics: Comparative': 'POLI 203 (3)',
                #           'Government and Politics: United States': 'POLI 1st year level (3), with an exemption for POLI\xa0310',
                #           'History: European': 'HIST 1st year level (6)',
                #           'History: United States': 'HIST 251 (3) and HIST 253 (3)',
                #           'Human Geography': 'GEOG 1st year level (3)',
                #           'Italian Language and Culture': 'ITAL 200 (6) with exemptions for ITAL 201 and ITAL 202',
                #           'Japanese': 'MODL 1st year level (6)', 'Latin': 'CLAS 1st year level (6)',
                #           'Music Theory': 'MUSI A (3)\xa0', 'Physics 1': 'No transfer credit awarded',
                #           'Physics 2': 'No transfer credit awarded',
                #           'Physics 1 and Physics 2': 'No transfer credit awarded', 'Physics C (Mechanics)': 'PHYS 204 (3)',
                #           'Physics C\xa0(Electricity and Magnetics)': 'PHYS 205 (3)', 'Psychology': 'PSYC 200 (6)',
                #           'Spanish Language and Culture': 'SPAN 200 (6) with exemptions for SPAN 201 and SPAN 202',
                #           'Spanish Literature and Culture': 'SPAN 200 (6) with exemptions for SPAN 201 and SPAN 202',
                #           'Statistics': 'MATH 1st year level (6)', 'Studio Art: Drawing': 'SFAR A (6)',
                #           'Studio Art :2-D Design:': 'SFAR A (6)', 'Studio Art: 3-D Design:': 'SFAR A (6)',
                #           'World History': 'HIST 1st year level (6)'}
                # item['ap'] = apDict.get(item['major_name_en'])
                # print("item['ap']: ", item['ap'])

                # overview  //h4[contains(text(),'Why study')]/..
                overview = response.xpath(
                    "//h4[contains(text(),'Program details')]/../../preceding-sibling::*[position()<last()]|"
                    "//h4[contains(text(),'Program Details')]/../../preceding-sibling::*[position()<last()]").extract()
                if len(overview) == 0:
                    overview = response.xpath(
                        "//h4[contains(text(),'Why study')]/..").extract()
                item['overview_en'] = remove_class(clear_lianxu_space(overview))
                # if item['overview_en'] == "":
                #     print("overview_en 为空")
                # print("item['overview_en']: ", item['overview_en'])

                # 正则从全文中匹配duration
                duration_dict = {"One": "1", "Two": "2", "Three": "3", "Four": "4", "Five": "5", "Six": "6", "Seven": "7",
                          "Eight": "8", "Nine": "9", "Ten": "10", "one": "1", "two": "2", "three": "3", "four": "4",
                          "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10", }
                duration_re = re.findall(r"[a-z]+\sor\s[a-z]+\syears|[a-z]+\sto\s[a-z]+\syears|of\s[a-z]+\syears", remove_tags(response.text))
                # print("duration_re: ", duration_re)
                duration_re_1 = re.findall(r"three|four|five", ''.join(duration_re))
                # print(duration_re_1)
                if len(duration_re_1) > 0:
                    item['duration_per'] = '1'
                    d_tmp_str = ""
                    for duration in duration_re_1:
                        d_tmp_str += duration_dict.get(duration) + "-"
                    item['duration'] = d_tmp_str.strip().strip('-').strip()
                # print("item['duration']: ", item['duration'])


                # portfolio作品集描述
                # //a[@name='legend-expand'][contains(text(),'Portfolio')]/../../following-sibling::div[1]
                portfolio = response.xpath(
                    "//a[@name='legend-expand'][contains(text(),'Portfolio')]/../../following-sibling::div[1]").extract()
                # clear_space(entry_requirements)
                portfolio = remove_class(clear_lianxu_space(portfolio))
                item['portfolio_desc_en'] = portfolio
                # print("item['portfolio_desc_en']: ", item['portfolio_desc_en'])


                # 开学日期
                # //a[@name='legend-expand'][contains(text(),'Application deadlines')]/../../following-sibling::div[1]//table//tr[1]/td[position()>1]
                start_date = response.xpath(
                    "//a[@name='legend-expand'][contains(text(),'Application deadlines')]/../../following-sibling::div[1]//table//tr[1]/td[position()>1]//text()|//a[@name='legend-expand'][contains(text(),'Application deadlines')]/../../following-sibling::div[1]//table//th//text()|//a[@name='legend-expand'][contains(text(),'Applications deadlines')]/../../following-sibling::div[1]//table//tr[1]/td[position()>1]//text()").extract()
                start_date = ', '.join(start_date).strip()
                # print(start_date)
                sd = ""
                if len(start_date) != 0:
                    if "Winter" in start_date:
                        sd += "1月"
                    if "Fall" in start_date:
                        sd += ",9月"
                item['start_date'] = sd
                # print("item['start_date']: ", item['start_date'])


                # 截止日期
                # //a[@name='legend-expand'][contains(text(),'Application deadlines')]/../../following-sibling::div[1]//table//tr[3]/td[position()>1]
                deadline = response.xpath(
                    "//a[@name='legend-expand'][contains(text(),'Application deadlines')]/../../following-sibling::div[1]//table//tr[3]/td[position()>1]//text()|"
                    "//a[@title='Open Applications deadlines']/../../following-sibling::div[1]//table//tr[3]/td[position()>1]//text()|"
                    "//b[contains(text(),'outside')]/../following-sibling::td//b//text()").extract()
                deadline_str = ', '.join(deadline).strip()
                # print(deadline_str)
                monthDict = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06",
                             "july": "07", "august": "08", "september": "09", "october": "10", "november": "11",
                             "december": "12",
                             "jan": "01", "feb": "02", "mar": "03", "apr": "04", "jun": "06",
                             "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12",
                             "sept": "09", }
                month_re = re.findall(r"january|february|march|april|may|june|july|august|september|october|november|december",deadline_str, re.I)
                # print("month_re: ", month_re)
                day_re = re.findall(r"\d+", deadline_str)
                # print("day_re: ", day_re)

                deadline_tmp_str = ""
                if len(month_re) > 0:
                    for m in range(len(month_re)):
                        month_re1 = monthDict.get(month_re[m].strip().lower())
                        # print("month_re1: ", month_re1)


                        day_re1 = day_re[m]
                        if day_re1 != "" and int(day_re1) < 10:
                            day_re1 = "0" + day_re1
                        # print("day_re1: ", day_re1)

                        deadline_tmp_str += "2019" + "-" + month_re1 + "-" + day_re1 +","
                item['deadline'] = deadline_tmp_str.strip().strip(',').strip()
                # print("item['deadline']: ", item['deadline'])

                # 就业
                # //a[@name='legend-expand'][contains(text(),'Application deadlines')]/../../following-sibling::div[1]//table//tr[3]/td[position()>1]
                career = response.xpath(
                    "//a[@name='legend-expand'][contains(text(),'Career opportunities')]/../../following-sibling::div[1]|"
                    "//a[@name='legend-expand'][contains(text(),'After your degree')]/../../following-sibling::div[1]").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career))
                # if item['career_en'] == "":
                #     print("career 为空")
                # print("item['career_en']: ", item['career_en'])

                '''课程设置不跳转'''
                # modules_url = response.xpath("//a[contains(text(),'Consult the Undergraduate Calendar')]/@href|"
                #                              "//a[contains(text(),'consult the Undergraduate Calendar')]/@href|"
                #                              "//a[contains(text(),'Consult the undergraduate calendar')]/@href").extract()
                # modules_url = response.xpath("//a[contains(@href,'/academics/undergraduate/calendar/current/sec')]/@href|"
                #                              "//a[contains(@adhocenable,'false')][contains(@href,'/jmsb/programs/undergraduate/bachelor/majors/')]/@href").extract()
                # print("modules_url: ", modules_url)
                # if len(modules_url) > 0:
                #     modules_url_parse = "https://www.concordia.ca" + modules_url[0]
                #     print("**************", modules_url_parse)
                #     item['modules_en'] = self.parse_modules(modules_url_parse, item['major_name_en'])
                modules_en = response.xpath("//a[contains(@title,'Open Course curriculum')]/../../following-sibling::div|"
                                            "//a[contains(@title,'Open Sample classes')]/../../following-sibling::div|"
                                            "//a[contains(@title,'Open Curriculum')]/../../following-sibling::div").extract()
                item['modules_en'] = remove_class(clear_lianxu_space(modules_en))
                if item['modules_en'] == "":
                    # print("modules_en 为空")
                    modules_url = response.xpath("//a[contains(@adhocenable,'false')][contains(@href,'/jmsb/programs/undergraduate/bachelor/majors/')]/@href").extract()
                    if len(modules_url) == 0:
                        modules_url = response.xpath(
                            "//a[contains(@adhocenable,'false')][contains(@href,'/jmsb/programs/undergraduate/bachelor/program-structure/core-courses')]/@href").extract()

                    # print("modules_url: ", modules_url)
                    if len(modules_url) > 0:
                        modules_url_parse = "https://www.concordia.ca" + modules_url[0]
                        print("**************", modules_url_parse)
                        item['modules_en'] = self.parse_modules(modules_url_parse, item['major_name_en'])
                print("item['modules_en']: ", item['modules_en'])

                # //b[contains(text(),'Jazz Studies:')]/../b
                # 商学院   //div[@class='content-main parsys']//div//div[1]//div[1]//div[1]//div[1]//h3[1]
                '''公共字段'''
                # https://www.concordia.ca/admissions/undergraduate/requirements/international.html
                item['ap'] = "If you have successfully passed Advanced Placement examinations in appropriate subjects with a grade of 3* or better (exceptions noted with *), you may be granted some advanced standing. We will notify you if you’ve been given advanced standing in your Offer of Admission."
                item['require_chinese_en'] = "<p>Senior Middle School Diploma plus Chinese National University Entrance Examinations (if available)</p>"
                item['apply_fee'] = "100"
                item['apply_pre'] = "$"

                # https://www.concordia.ca/admissions/undergraduate/requirements/english-language-proficiency.html
                item['ielts_desc'] = "IELTS score of 7 or higher"
                item['ielts'] = "7"
                item['toefl_desc'] = "TOEFL iBT score 90 or higher"
                item['toefl'] = "90"
                item['sat_code'] = item['toefl_code'] = "0956"


                # 学位名称
                degree_name = response.xpath("//div[@class='span8 ordinal-group-1']/h5//text()").extract()
                # degree_name_str = ''.join(degree_name).strip()

                if "," in ''.join(degree_name).strip():
                    degree_name = ''.join(degree_name).strip().split(',')
                print(degree_name)

                if len(degree_name) > 0:
                    for degree in degree_name:
                        degree_del = re.findall(r"\([\w\s,]+\)", degree)
                        item['degree_name'] = degree.replace(''.join(degree_del), '').strip()
                        print("item['degree_name']: ", item['degree_name'])
                        if item['degree_name'] != "Certificate":

                            # 有多个学位的专业有多个entry_requirements、ib
                            is_entry_ib = response.xpath(
                                "//a[@name='legend-expand'][contains(text(),'Admission requirements')]/span[contains(text(), 'BA')]//text()|"
                                "//a[@name='legend-expand'][contains(text(),'Admission requirements')]/span[contains(text(), 'BSc')]//text()").extract()
                            print("is_entry_ib: ", is_entry_ib)
                            entry_requirements = response.xpath(
                                "//a[@name='legend-expand'][contains(text(),'Admission requirements')]/../../following-sibling::div[1]").extract()
                            entry_requirements_str = remove_tags(''.join(entry_requirements))
                            if len(is_entry_ib) == 2:
                                if item['degree_name'] == "Bachelor of Science":
                                    item['entry_requirements_en'] = remove_class(clear_lianxu_space([entry_requirements[0]]))
                                elif item['degree_name'] == "Bachelor of Arts":
                                    item['entry_requirements_en'] = remove_class(clear_lianxu_space([entry_requirements[-1]]))
                            else:
                                item['entry_requirements_en'] = remove_class(clear_lianxu_space(entry_requirements))
                            print("item['entry_requirements_en']: ", item['entry_requirements_en'])

                            IB = re.findall(r"International\sBacc.\s\(IB\):.{1,300}", entry_requirements_str)
                            # print("IB: ", IB)
                            IB_str = ''.join(IB)
                            if len(is_entry_ib) == 2:
                                if item['degree_name'] == "Bachelor of Science":
                                    IB_str = IB[0]
                                elif item['degree_name'] == "Bachelor of Arts":
                                    IB_str = IB[-1]
                            ib_re = re.findall(r":[\w\W].*", IB_str)
                            item['ib'] = ''.join(ib_re).strip().strip(":").strip()
                            item['ib'] = item['ib'].replace("International Bacc. (IB):", ";")
                            # print("item['ib']: ", item['ib'])

                            # 判断获取item['alevel']
                            item['alevel'] = self.get_alevel(item['degree_name'], item['department'])
                            # print("item['alevel']: ", item['alevel'])

                            # 判断获取学费
                            item['tuition_fee_pre'] = "$"
                            item['tuition_fee'] = self.get_tuition_fee(item['degree_name'], item['department'], item['major_name_en'])
                            # print("item['tuition_fee']: ", item['tuition_fee'])

                            if item['degree_name'] == "Bachelor of Computer Science" and "Gina Cody School of Engineering and Computer Science" in item['department']:
                                item['department'] = "Gina Cody School of Engineering and Computer Science"
                            elif item['degree_name'] == "Bachelor of Science" and "Faculty of Arts & Science" in item['department']:
                                item['department'] = "Faculty of Arts & Science"
                            elif item['degree_name'] == "Bachelor of Artse" and "Faculty of Arts & Science" in item['department']:
                                item['department'] = "Faculty of Arts & Science"

                            yield item

        except Exception as e:
            with open("scrapySchool_Canada_Ben/error/" + item['school_name'] + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    # 判断获取item['alevel']函数
    def get_alevel(self, degree_name, department):
        alevel = ""
        if "Faculty of Arts & Science" in department:
            if degree_name == "Bachelor of Arts" or degree_name == "Bachelor of Education":
                alevel = "General admission requirements as stated above"
            elif degree_name == "Bachelor of Science":
                alevel = "General admission requirements as stated above"
        elif "Gina Cody School of Engineering and Computer Science" in department:
            if degree_name == "Bachelor of Engineering":
                alevel = """Average grade of C and C in A-level math and physics
                Grades of B may be required for more competitive programs"""
            elif degree_name == "Bachelor of Computer Science":
                alevel = "Average grade of C and C in A-level math"
        elif "John Molson School of Business" in department:
            alevel = """Average grade of C and C in A-level math."""
        elif "Faculty of Fine Arts" in department:
            alevel = """General admission requirements as stated above
            BFA Computational Arts with Computer Applications: A level Math with grade of C
            Certain programs require additional materials."""
        return alevel

    def get_tuition_fee(self, degree_name, department, major_name_en):
        tuition_fee = ""
        if "Faculty of Arts & Science" in department or "Faculty of Fine Arts" in department:
            if degree_name == "Bachelor of Education" or "Education" in major_name_en:
                tuition_fee = "560.52 per credit"
            else:
                tuition_fee = "626.09 per credit"
        elif "John Molson School of Business" in department:
            tuition_fee = "761.25 per credit"
        elif "Gina Cody School of Engineering and Computer Science" in department:
            tuition_fee = "696.04 per credit"
        return tuition_fee

    def parse_modules(self, modules_url_parse, major_name_en):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(modules_url_parse, headers=headers)
        response = etree.HTML(data.text)

        modules_xpath = "//b[contains(text(),'"+major_name_en.strip()+":')]/../b|" \
                                                                      "//div[@class='content-main parsys']//div//div[1]//div[1]//div[1]//div[1]//h3[1]|" \
                                                                      "//h6[contains(text(),'Required courses')]/following-sibling::p[1]"
        if major_name_en == "Film Studies":
            modules_xpath = "//b[contains(text(),'Film Studies:')]/../following-sibling::p/b"
        modules_en = response.xpath(modules_xpath)
        # print("***", modules_en)
        if len(modules_en) == 0:
            key_major = major_name_en[0:4].upper()
            print("key_major: ", key_major)
            modules_xpath = "//b[contains(text(),'" + key_major.strip() + " ')]/../b"
            modules_en = response.xpath(modules_xpath)
            if len(modules_en) == 0:
                modules_xpath = "//b[contains(text(),'" + major_name_en.strip() + " Core')]/../../.."
                modules_en = response.xpath(modules_xpath)

        modules_en_str = ""
        if len(modules_en) > 0:
            for m in modules_en:
                modules_en_str += etree.tostring(m, encoding='unicode', method='html')
        modules_en = remove_class(clear_lianxu_space([modules_en_str]))
        return modules_en








