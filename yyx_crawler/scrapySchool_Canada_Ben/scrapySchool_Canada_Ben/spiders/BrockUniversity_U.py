# -*- coding:utf-8 -*-
"""
# @PROJECT: scrapySchool_Canada_Ben
# @Author: admin
# @Date:   2018-11-05 10:15:44
# @Last Modified by:   admin
# @Last Modified time: 2018-11-05 10:15:44
"""
__author__ = 'yangyaxia'
__date__ = '2018/11/05 10:15'
import scrapy
import re
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from w3lib.html import remove_tags
from lxml import etree
import requests

class BrockUniversity_USpider(scrapy.Spider):
    name = "BrockUniversity_U"
    start_urls = ["https://brocku.ca/programs/"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        links = response.xpath("//div[@id='content']/div[@id='grid']/div/div[@class='content']/a/@href").extract()
        print(len(links))
        links = list(set(links))
        # 76
        print(len(links))
        for url in links:
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)
        item['school_name'] = "Brock University"
        item['url'] = response.url
        print("===========================")
        print(response.url)
        item['other'] = '''问题描述：1.没有课程设置和课程长度
        2.专业描述和就业为空的是详情页没有的'''

        '''公共字段'''
        # item['campus'] = 'Hamilton'
        item['location'] = 'St. Catharines, Ontario, Canada'
        item['sat_code'] = item['toefl_code'] = '0895'

        # item['duration'] = '4'
        # item['duration_per'] = 1
        # https://www.stu.ca/future-students/how-to-apply/
        item['apply_pre'] = 'CAD$'
        item['apply_fee'] = '150'
        item['start_date'] = '1月,5月,9月'
        item['deadline'] = '2018-10-01,2019-02-01,2019-05-01'
        # https://brocku.ca/safa/undergraduate-tuition-and-fees-2018-academic-year/#2017-ug-ancillary-fees7420-ef5cf380-e567
        item['tuition_fee_pre'] = 'CAD$'
        item['tuition_fee'] = '21154.24'


        # https://brocku.ca/admissions/international/international-secondary-school-student/
        item['ap'] = """Advanced placement (AP)
Advanced placement courses may be used to determine admissibility and also granting of transfer credits or exemption. If you have completed advanced placement courses as part of an appropriate secondary school credential, and submit an examination grade of 4 on individual results, you may be eligible to receive university credit to a maximum of 2.0 Brock credits. An official AP transcript is required for the evaluation process. """
        item['ib'] = """International Baccalaureate (IB)
Applicants who have successfully completed the IB diploma with the appropriate prerequisite subjects will be considered for admission and may be awarded a maximum of 3.0 transfer credits for HL examinations completed at a minimum grade of 5. A scholarship worth $1,000 will also be granted. Applicants who successfully complete an IB certificate program with a minimum of six subjects, including prerequisites, may also be considered for admission and transfer credit."""
        item['entry_requirements_en'] = """<h2>General admission requirements:</h2>
<ul>
<li>Senior Secondary school credential appropriate for entry to university in your home country;</li>
<li>Academically rigorous grade 12 year</li>
<li>Minimum B- average (higher for some programs);</li>
<li>English Language proficiency requirements must be satisfied</li>
</ul>"""

        # https://brocku.ca/admissions/international/requirements-by-country/
        item['require_chinese_en'] = '<p>(Grade 12) Senior High School Graduation Certificate (3 Years) plus final transcript showing Grade 12 first and second term grades</p>'
        item['alevel'] = "Five GCE/GCSE/IGCSE subjects with at least two at A-level (GCSE grades at C or above). One GCSE/IGCSE/O-level subject (graded C or above) and four AS-level subjects will be considered provided the AS-levels do not duplicate subject matter at the GCSE/IGCSE or O level. VCE A-level, VCE A-level Double Award and BTEC Certificate/Diploma qualifications."
        try:
            department = response.xpath("//a[contains(@class, 'btn faculty')]//text()").extract()
            item['department'] = ', '.join(department).strip()
            print("item['department']: ", item['department'])

            major_name_en = response.xpath("//h1[@class='entry-title']/text()").extract()
            clear_space(major_name_en)
            item['major_name_en'] = ''.join(major_name_en).strip()
            print("item['major_name_en']: ", item['major_name_en'])


            overview = response.xpath("//div[@class='entry-content']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview)).replace("<p></p>", "").strip()
            if item['overview_en'] == "":
                item['overview_en'] = None
                print("***overview_en 为空")
            print("item['overview_en']: ", item['overview_en'])


            career = response.xpath("//h2[contains(text(),'Career outcomes')]/..").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            if item['career_en'] == "":
                item['career_en'] = None
            print("item['career_en']: ", item['career_en'])

            # https://brocku.ca/admissions/english-proficiency/
            if item['major_name_en'] == "Accounting":
                item['ielts_desc'] = 'overall 7.0 with no band below 6.5'
                item['ielts'] = '7.0'
                item['ielts_l'] = '6.5'
                item['ielts_s'] = '6.5'
                item['ielts_r'] = '6.5'
                item['ielts_w'] = '6.5'
                item['toefl_desc'] = 'overall 100, minimum 27 on writing, 27 on speaking'
                item['toefl'] = '100'
                item['toefl_s'] = '27'
                item['toefl_w'] = '27'
            elif 'Teacher education' in item['major_name_en']:
                item['ielts_desc'] = 'overall 7.0'
                item['ielts'] = '7.0'
                item['toefl_desc'] = 'overall 100, minimum 27 on writing, 27 on speaking'
                item['toefl'] = '100'
                item['toefl_s'] = '27'
                item['toefl_w'] = '27'
            else:
                item['ielts_desc'] = 'overall 6.5, no band below 6.0'
                item['ielts'] = '6.5'
                item['ielts_l'] = '6.0'
                item['ielts_s'] = '6.0'
                item['ielts_r'] = '6.0'
                item['ielts_w'] = '6.0'
                item['toefl_desc'] = 'overall 88, with minimum 21 on speaking and 21 on writing'
                item['toefl'] = '88'
                item['toefl_s'] = '21'
                item['toefl_w'] = '21'

            degree_name = response.xpath("//a[contains(@class, 'btn bachelor-of')]//text()").extract()
            if len(degree_name) > 0:
                for de in degree_name:
                    item['degree_name'] = de.strip()
                    print("item['degree_name']: ", item['degree_name'])
                    if item['degree_name'] is not None:
                        yield item
            else:
                if item['degree_name'] is not None:
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