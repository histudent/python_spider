# -*- coding:utf-8 -*-
"""
# @PROJECT: scrapySchool_Canada_College
# @Author: admin
# @Date:   2018-12-22 14:10:25
# @Last Modified by:   admin
# @Last Modified time: 2018-12-22 14:10:25
"""
__author__ = 'yangyaxia'
__date__ = '2018/12/22 13:39'
import scrapy
import re, time
from scrapySchool_Canada_College.getItem import get_item
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from w3lib.html import remove_tags
from lxml import etree
import requests

class SenecaCollege_USpider(scrapy.Spider):
    name = "SenecaCollege_U"
    start_urls = ["http://www.senecacollege.ca/international/programs/list.html"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        # 获取每个校区full time的专业
        links = response.xpath("//div/div[@class='table-component table-responsive  ']/table[@class='table']/tbody/tr/td[2]/a/@href").extract()
        # print("=========", response.url)
        print(len(links))
        links = list(set(links))
        print(len(links))

        time.sleep(1)
        for link in links:
            url = "http://www.senecacollege.ca" + link
            yield scrapy.Request(url, self.parse_data)


    def parse_data(self, response):
        item = get_item(ScrapyschoolCanadaCollegeItem)
        item['school_name'] = "Seneca College"
        item['url'] = response.url
        print("===========================")
        print(response.url)

        item['location'] = '1750 Finch Avenue East Toronto, Ontario, Canada M2J 2X5'

        item['other'] = """问题描述： 1.没有找到截止日期"""

        # http://www.senecacollege.ca/international/apply/how-to-apply.html
        item['apply_pre'] = "CAD$"
        item['apply_fee'] = '65'


        try:
            major_name_en = response.xpath("//div[@class='carousel-complementary-box']//h1/text()").extract()
            clear_space(major_name_en)
            # major_del = re.findall(r"\([A-Z]*\)", ''.join(major_name_en))
            if len(major_name_en) > 0:
                item['major_name_en'] = ''.join(major_name_en).strip()
            print("item['major_name_en']: ", item['major_name_en'])

            programme_code = response.xpath("//div[@class='carousel-complementary-box']//h1/span//text()").extract()
            clear_space(programme_code)
            if len(programme_code) > 0:
                item['programme_code'] = ''.join(programme_code).replace("(", "").replace(")", "").strip()
            print("item['programme_code']: ", item['programme_code'])

            start_date = response.xpath("//p[contains(text(),'Starts:')]/text()").extract()
            clear_space(start_date)
            # print(start_date)

            start_date_end = ""
            if len(start_date) > 0:
                start_date_str = ''.join(start_date).replace("Starts:", "").strip()
                if "May" in start_date_str:
                    start_date_end += "2019-05,"
                if "September" in start_date_str:
                    start_date_end += "2019-09,"
                if "January" in start_date_str:
                    start_date_end += "2020-01,"
            item['start_date'] = start_date_end.strip().strip(',').strip()
            # print("item['start_date']: ", item['start_date'])

            campus = response.xpath("//h5[contains(text(),'Campus')]/following-sibling::*//a//text()").extract()
            clear_space(campus)
            if len(campus) > 0:
                item['campus'] = ''.join(campus).strip()
            # print("item['campus']: ", item['campus'])

            department = response.xpath("//h5[contains(text(),'School')]/following-sibling::*//text()").extract()
            clear_space(department)
            if len(department) > 0:
                item['department'] = ''.join(department).strip()
            # print("item['department']: ", item['department'])

            duration = response.xpath("//h5[contains(text(),'Duration')]/following-sibling::*//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration_re = re.findall(r"\d+\syear|\d+\smonth|\d+\sweek", ''.join(duration), re.I)
            # print("duration_re: ", duration_re)
            if len(duration_re) > 0:
                if "year" in ''.join(duration_re[0]).lower():
                    item['duration_per'] = 1
                if "month" in ''.join(duration_re[0]).lower():
                    item['duration_per'] = 3
                if "week" in ''.join(duration_re[0]).lower():
                    item['duration_per'] = 4
                item['duration'] = ''.join(re.findall(r"\d+", ''.join(duration_re))).strip()
            # print("item['duration']: ", item['duration'])
            # print("item['duration_per']: ", item['duration_per'])

            degree_name = response.xpath("//h5[contains(text(),'Credential Awarded')]/following-sibling::*//text()").extract()
            clear_space(degree_name)
            if len(degree_name) > 0:
                item['degree_name'] = ''.join(degree_name).replace("Ontario College", "").replace("Seneca College", "").strip()
            # print("item['degree_name']: ", item['degree_name'])

            if item['degree_name'] is not None:
                if "diploma" in item['degree_name'].lower():
                    item['degree_level'] = 3
                elif "degree" in item['degree_name'].lower():
                    if "Bachelor" in item['major_name_en']:
                        item['degree_name'] = item['major_name_en']
                    item['degree_level'] = 1
                elif "graduate" in item['degree_name'].lower():
                    item['degree_level'] = 2
            # print("item['degree_name']: ", item['degree_name'])
            # print("item['degree_level']: ", item['degree_level'])

            # 排除certificate的课程类型
            if item['degree_level'] is not None:
                if item['degree_level'] == 1:
                    item['ielts_desc'] = "Overall band of 6.5. No single test score below 6.0"
                    item['ielts'] = '6.5'
                    item['ielts_l'] = '6.0'
                    item['ielts_s'] = '6.0'
                    item['ielts_r'] = '6.0'
                    item['ielts_w'] = '6.0'
                    item['toefl_desc'] = 'Overall 84 with Writing, Reading, Listening and Speaking minimums of 21'
                    item['toefl'] = '84'
                    item['toefl_l'] = '21'
                    item['toefl_s'] = '21'
                    item['toefl_r'] = '21'
                    item['toefl_w'] = '21'
                    item['require_chinese_en'] = """<p>When applying to a Seneca degree program you must submit:</p>
<ul>
<li>High school transcripts for grades 10, 11 and 12 showing all program specific pre-requisite courses.</li>
<li>Transcripts must include six (6) senior level courses equivalent to Ontario university preparatory credits with an overall average of 65%.</li>
<li>High school/secondary school diploma (certificate of completion).</li>
<li>You may submit transcripts or certificates for any completed university/postsecondary college courses or programs taken inside or outside of Canada.</li>
<li>Academic records that are in a language other than English must include an official/certified English translation.</li>
<li>Seneca reserves the right to verify submitted transcripts at any time. For courses and credentials earned inside of Canada, Seneca reserves the right to request original transcripts be sent directly to Seneca from the issuing institution. Applicants will be notified if this is needed.</li>
</ul>"""
                elif item['degree_level'] == 2:
                    item['ielts_desc'] = "Overall band of 6.5. No single test score below 6.0"
                    item['ielts'] = '6.5'
                    item['ielts_l'] = '6.0'
                    item['ielts_s'] = '6.0'
                    item['ielts_r'] = '6.0'
                    item['ielts_w'] = '6.0'
                    item['toefl_desc'] = 'Overall 88 with Writing, Reading, Listening and Speaking minimums of 22'
                    item['toefl'] = '88'
                    item['toefl_l'] = '22'
                    item['toefl_s'] = '22'
                    item['toefl_r'] = '22'
                    item['toefl_w'] = '22'
                    item['require_chinese_en'] = """<p>When applying to a Seneca graduate certificate program you must submit:</p>
<ul>
<li>Complete university and college transcripts for all years of study.</li>
<li>University or college credential (degree, diploma or certificate).</li>
<li>A credential assessment from a recognized agency such as WES (World Education Services) may be required for some programs. Applicants will be informed by email if this is needed.</li>
<li>Academic records that are in a language other than English must include an official/certified English translation.</li>
<li>Seneca reserves the right to verify submitted transcripts at any time. For courses and credentials earned inside of Canada, Seneca reserves the right to request original transcripts be sent directly to Seneca from the issuing institution. Applicants will be informed by email if this is needed.</li>
</ul>"""
                elif item['degree_level'] == 3:
                    item['ielts_desc'] = "Overall band of 6.0. No single test score below 5.5"
                    item['ielts'] = '6.0'
                    item['ielts_l'] = '5.5'
                    item['ielts_s'] = '5.5'
                    item['ielts_r'] = '5.5'
                    item['ielts_w'] = '5.5'
                    item['toefl_desc'] = 'Overall 80 with Writing, Reading, Listening and Speaking minimums of 20'
                    item['toefl'] = '80'
                    item['toefl_l'] = '20'
                    item['toefl_s'] = '20'
                    item['toefl_r'] = '20'
                    item['toefl_w'] = '20'
                    item['require_chinese_en'] = """<p>When applying to a Seneca two- or three-year diploma program you must submit:</p>
<ul>
<li>High school transcripts for grades 10, 11 and 12 showing all program specific pre-requisite courses.</li>
<li>High school/secondary school diploma (certificate of completion).</li>
<li>You may submit transcripts or certificates for any completed university/postsecondary college courses or programs taken inside or outside of Canada.</li>
<li>Academic records that are in a language other than English must include an official/certified English translation.</li>
<li>Seneca reserves the right to verify submitted transcripts at any time. For courses and credentials earned inside of Canada, Seneca reserves the right to request original transcripts be sent directly to Seneca from the issuing institution. Applicants will be notified if this is needed.</li>
</ul>"""
                overview = response.xpath("//h2[contains(text(),'About the Program')]/../../..").extract()
                if len(overview) > 0:
                    item['overview_en'] = remove_class(clear_lianxu_space(overview))
                # print("item['overview_en']: ", item['overview_en'])

                career_en = response.xpath("//h3[contains(text(),'Related Careers')]/../../preceding-sibling::*").extract()
                if len(career_en) > 0:
                    item['career_en'] = remove_class(clear_lianxu_space(career_en))
                # print("item['career_en']: ", item['career_en'])

                #
                entry_requirements_en_url = response.xpath(
                    "//a[contains(text(),'Admission requirements')]/@href").extract()
                # print("entry_requirements_en_url: ", entry_requirements_en_url)
                if len(entry_requirements_en_url) > 0:
                    entry_requirements_interview = self.parse_entry_requirements_en(
                        "http://www.senecacollege.ca" + entry_requirements_en_url[0])
                    item['entry_requirements_en'] = entry_requirements_interview[0]
                    item['interview_desc_en'] = entry_requirements_interview[-1]

                # print("item['entry_requirements_en']: ", item['entry_requirements_en'])

                modules_url = response.xpath(
                    "//a[contains(text(),'Courses')]/@href").extract()
                # print("modules_url: ", modules_url)
                if len(modules_url) > 0:
                    item['modules_en'] = self.parse_modules(
                        "http://www.senecacollege.ca" + modules_url[0])
                # print("item['modules_en']: ", item['modules_en'])


                item['tuition_fee_per'] = "1"
                item['tuition_fee_pre'] = "CAD$"
                tuition_fee_url = response.xpath(
                    "//a[contains(text(),'Costs')]/@href").extract()
                print("tuition_fee_url: ", tuition_fee_url)
                if len(tuition_fee_url) > 0:
                    item['tuition_fee'] = self.parse_tuition_fee("http://www.senecacollege.ca" + tuition_fee_url[0])
                print("item['tuition_fee']: ", item['tuition_fee'])

                yield item
        except Exception as e:
                with open("scrapySchool_Canada_College/error/" + item['school_name'] + ".txt", 'a', encoding="utf-8") as f:
                    f.write(str(e) + "\n" + response.url + "\n========================\n")
                print("异常：", str(e))
                print("报错url：", response.url)

    def parse_modules(self, modules_url):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(modules_url, headers=headers_base)
        response = etree.HTML(data.text)

        modules_en = response.xpath(
            "//div[@class='panel panel-default white']//span[contains(@class,'panel-title')]/../..")
        modules_en_str = ""
        if len(modules_en) > 0:
            for m in modules_en:
                modules_en_str += etree.tostring(m, encoding='unicode', method='html')
        modules_en = remove_class(clear_lianxu_space([modules_en_str]))

        return modules_en

    def parse_entry_requirements_en(self, entry_requirements_en_url):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(entry_requirements_en_url, headers=headers_base)
        response = etree.HTML(data.text)

        entry_requirements_en = response.xpath(
            "//body[contains(@class,'page admission-requirements-page')]/div/section[contains(@class,'container')]/div/div[contains(@class,'column-control column-control-new parbase')]/div[contains(@class,'')]/div[contains(@class,'row')]/div[1]")
        entry_requirements_en_str = ""
        if len(entry_requirements_en) > 0:
            for m in entry_requirements_en:
                entry_requirements_en_str += etree.tostring(m, encoding='unicode', method='html')
        entry_requirements_en = remove_class(clear_lianxu_space([entry_requirements_en_str]))

        interview = response.xpath("//div[contains(@class,'column-control-wrapper vertical-border')]//div[2]//div[2]")
        interview_str = ""
        if len(interview) > 0:
            for m in interview:
                interview_str += etree.tostring(m, encoding='unicode', method='html')
        interview_en = remove_class(clear_lianxu_space([interview_str]))

        return [entry_requirements_en, interview_en]

    def parse_tuition_fee(self, modules_url):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(modules_url, headers=headers_base)
        response = etree.HTML(data.text)

        tuition_fee = response.xpath(
            "//p[@class='tuition-international hidden']//text()")
        clear_space(tuition_fee)
        tuition_fee = ''.join(tuition_fee).replace("$", "").strip()

        return tuition_fee