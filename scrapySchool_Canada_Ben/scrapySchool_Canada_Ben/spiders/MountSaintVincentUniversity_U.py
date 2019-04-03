# -*- coding:utf-8 -*-
"""
# @PROJECT: scrapySchool_Canada_Ben
# @Author: admin
# @Date:   2018-11-12 10:25:03
# @Last Modified by:   admin
# @Last Modified time: 2018-11-12 10:25:03
"""

__author__ = 'yangyaxia'
__date__ = '2018/11/12 10:25'
import scrapy
import re
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from w3lib.html import remove_tags
from lxml import etree
import requests

class MountSaintVincentUniversity_USpider(scrapy.Spider):
    name = "MountSaintVincentUniversity_U"
    start_urls = ["http://www.msvu.ca/en/home/programsdepartments/education/bachelorofeducationprograms/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/professionalstudies/appliedhumannutrition/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/bachelorofscience/biology/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/bachelorofscience/chemistry/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/bachelorofscience/computerscience/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/bachelorofscience/mathematics/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/bachelorofscience/psychology/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/BA/canadianstudies/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/BA/chinese.aspx",
"http://www.msvu.ca/en/home/programsdepartments/professionalstudies/Department_of_Communication_Studies/bacommunication.aspx",
"http://www.msvu.ca/en/home/programsdepartments/bachelorofscience/computerscience/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/BA/culturalstudies/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/BA/economics/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/BA/english/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/BA/familystudies/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/BA/french/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/BA/gerontology/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/BA/history/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/bachelorofscience/mathematics/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/BA/philosophy/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/BA/politicalstudies/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/bachelorofscience/psychology/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/BA/publicpolicystudies/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/BA/religiousstudies/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/BA/sociologyanthropology/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/BA/spanish.aspx",
"http://www.msvu.ca/en/home/programsdepartments/bachelorofscience/statistics/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/BA/womensstudies/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/professionalstudies/appliedhumannutrition/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/professionalstudies/businessadministration/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/professionalstudies/childandyouthstudy/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/professionalstudies/familystudiesgerontology/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/professionalstudies/Department_of_Communication_Studies/publicrelations/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/professionalstudies/tourismhospitality/default.aspx",
"http://www.msvu.ca/en/home/programsdepartments/professionalstudies/Department_of_Communication_Studies/Bachelor_of_Science_Science_Communication/default.aspx",]
#     start_urls = ["http://www.msvu.ca/en/home/programsdepartments/professionalstudies/Department_of_Communication_Studies/Bachelor_of_Science_Science_Communication/default.aspx",]
#     print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)
        item['school_name'] = "Mount Saint Vincent University"
        item['url'] = response.url
        print("===========================")
        print(response.url)

        item['other'] = '''问题描述：1. 没有课程长度，申请要求
        2.专业描述和课程设置、就业为空的是页面没有的'''

        '''公共字段'''
        # item['campus'] = 'Hamilton'
        item['location'] = 'Halifax, Nova Scotia,Canada'
        # item['sat_code'] = item['toefl_code'] = '5076'
        # item['act_code'] = '0719'

        # item['duration'] = '4'
        # item['duration_per'] = 1
        # http://www.msvu.ca/en/home/beamountstudent/money/tuitionfees/detailedfeeinformation.aspx
        item['apply_pre'] = 'CAD$'
        item['apply_fee'] = '40'

        # http://www.msvu.ca/en/home/beamountstudent/internationaleducationcentre/AdmissionRequirements/ApplicationDeadlines.aspx
        item['start_date'] = '9月'
        item['deadline'] = '2019-06-21'

        # http://www.msvu.ca/en/home/beamountstudent/money/tuitionfees/default.aspx
        item['tuition_fee_pre'] = 'CAD$'
        item['tuition_fee'] = '16,586 - 16,969'

        # http://www.msvu.ca/en/home/programsdepartments/academiccalendars/undergradprograms/admissions/requirements/internationalrequirements.aspx#lang
        item['ielts_desc'] = '6.5 (no individual score below 6.0)'
        item['ielts'] = '6.5'
        item['ielts_l'] = '6.0'
        item['ielts_s'] = '6.0'
        item['ielts_r'] = '6.0'
        item['ielts_w'] = '6.0'
        item['toefl_desc'] = '86 - 92 (no individual score below 21)'
        item['toefl'] = '86-92'
        item['toefl_l'] = '21'
        item['toefl_s'] = '21'
        item['toefl_r'] = '21'
        item['toefl_w'] = '21'

        # http://www.msvu.ca/en/home/programsdepartments/academiccalendars/undergradprograms/admissions/requirements/highschoolrequirements.aspx
        item['ap'] = """Advanced Placement Program (AP)
Mount Saint Vincent University participates in the Advanced Placement Program administered by the College Board (Princeton, New Jersey).
Upon presentation of Advanced Placement credentials, students may receive up to a maximum of 5.0 units of transfer credits for Advanced Placement Examinations provided that they have achieved grades of 4 or 5."""
        item['ib'] = """International Baccalaureate (IB)
Mount Saint Vincent University welcomes applicants holding the International Baccalaureate (IB) diploma. Students enrolled in the IB program may receive transfer credits for a maximum of 5.0 units for a combination of the following:
 Course Type	            Value
Higher Level IB 	        1.0 unit at the 1000 level for each with a final grade of five or higher upon presentation of the final transcript or completed diploma. 
Standard Level IB	        0.5 unit at the 1000 level for each with a final grade of five or higher upon presentation of the final transcript or completed diploma.
Theory of Knowledge (ToK)	1.0 unit of ARTS elective at the 1000 level with a final grade of “B” or higher upon presentation of the final transcript or completed diploma.
Students receiving transfer credit for IB courses are advised to contact the departments or academic advising to determine the effect of those credits on their plans for future study and their career goals."""
        # item['act_desc'] = item['sat1_desc'] = "SAT or ACT scores will also be considered"

        # http://www.msvu.ca/en/home/beamountstudent/internationaleducationcentre/AdmissionRequirements/default.aspx
        item['require_chinese_en'] = '<p>Senior Middle Two and Three results as well as a graduation certificate. Students may also be asked to report scores from the National College Entrance Examination with grades of 70% or above.</p><p>English Language test scores required</p>'
        item['average_score'] = '70'
        item['specific_requirement_en'] = "70% with no mark below 60%"
        item['entry_requirements_en'] = """<div>
<h3>International Applicants</h3>
<p>International applicants are expected to have completed a preparatory program that
leads to university entrance in their own country. <br /> In general,&nbsp;secondary school&nbsp;applicants have an average of 70% (5 best scoring academic subjects&nbsp;considered) during their final year of schooling. Applicants looking to transfer from another post-secondary institution must demonstrate an overall GPA of 2.0. Refer to chart below for program specific requirements.</p><p>Possession of minimum entrance requirements does not
guarantee admission to the University. Applicants must submit proof of
ability to follow a university program taught entirely in English.
If English is not your first language, please submit official reports with acceptable scores.</p><p>Applications are considered on an individual basis.</p></div>"""
        try:

            major_name_en = response.xpath("//h1[@class='no-margin']//text()").extract()
            clear_space(major_name_en)
            item['major_name_en'] = ''.join(major_name_en).replace('Bachelor of Arts -', '').strip()
            # print("item['major_name_en']: ", item['major_name_en'])

            degree_name = response.xpath("//div[@class='breadcrumbs']//ul//a[@href='http://www.msvu.ca/en/home/programsdepartments/BA/default.aspx'][contains(text(),'Bachelor of Arts')]//text()|"
                                         "//div[@class='breadcrumbs']//ul//a[@href='http://www.msvu.ca/en/home/programsdepartments/bachelorofscience/default.aspx'][contains(text(),'Bachelor of Science')]//text()").extract()
            clear_space(degree_name)
            item['degree_name'] = ''.join(degree_name).strip()
            if "BSc" in item['major_name_en']:
                item['degree_name'] = "BSc"
                item['major_name_en'] = item['major_name_en'].replace("BSc", "").strip()
            if "Bachelor of Arts" in ''.join(major_name_en):
                item['degree_name'] = "Bachelor of Arts"
            print("item['major_name_en']: ", item['major_name_en'])
            print("item['degree_name']: ", item['degree_name'])

            '''overview_en'''
            # //span[@class='h2_inside']
            # overview_en = response.xpath("//span[@class='h2_inside']|//div[contains(@id,'tmpl_cbins')]").extract()
            overview_en = response.xpath("//h1[contains(text(),'Highlights')]/following-sibling::p[position()<3]|"
                                         "//span[@class='h1_inside']/../following-sibling::p[position()<3]|"
                                         "//h2[contains(text(),'French Program Highlights')]/preceding-sibling::h4[1]|"
                                         "//h2[contains(text(),'Program Highlights')]/following-sibling::p[1]").extract()
            if len(overview_en) == 0:
                overview_en = response.xpath("//span[contains(text(),'Program Highlights')]/../following-sibling::p[position()<3]").extract()
            if len(overview_en) > 0:
                item['overview_en'] = remove_class(clear_lianxu_space(overview_en)).replace("<p>Admissions Requirements »Tuition &amp; Fees »</p>", "").strip()
            print("item['overview_en']: ", item['overview_en'])

            '''modules'''
            modules_url = response.xpath("//a[contains(text(),'Courses')]/@href").extract()
            # print(modules_url)
            if len(modules_url) > 0:
                item['modules_en'] = self.parse_modules(modules_url[0])
            # print("item['modules_en']: ", item['modules_en'])

            '''career_en'''
            career_en = response.xpath("//h1[contains(text(),'Future Possibilities')]/following-sibling::p[1]|"
                                       "//h1[contains(text(),'Our Graduates')]/following-sibling::p[position()<3]|"
                                       "//h1[contains(text(),'Advancing your Career')]/following-sibling::p[1]|"
                                       "//h1[contains(text(),'Career Options')]/..").extract()
            if len(career_en) == 0:
                career_en = response.xpath(
                    "//span[contains(text(),'Program Highlights')]/../following-sibling::p[position()<3]").extract()
            if len(career_en) > 0:
                item['career_en'] = remove_class(clear_lianxu_space(career_en)).replace("Read what our students say »", "") \
                    .replace("Read about some of their", "").replace("career paths »", "").strip()
            print("item['career_en']: ", item['career_en'])
            yield item

        except Exception as e:
            with open("scrapySchool_Canada_Ben/error/" + item['school_name'] + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_modules(self, modules_url):
        headers_base = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(modules_url, headers=headers_base)
        response = etree.HTML(data.text)

        modules_en = response.xpath(
            "//div[@id='tmpl_cbins_main']//h2")
        modules_en_str = ""
        if len(modules_en) > 0:
            for m in modules_en:
                modules_en_str += etree.tostring(m, encoding='unicode', method='html')
        modules_en = remove_class(clear_lianxu_space([modules_en_str])).replace("<h2>", "<h4>").replace("</h2>", "</h4>")
        return modules_en