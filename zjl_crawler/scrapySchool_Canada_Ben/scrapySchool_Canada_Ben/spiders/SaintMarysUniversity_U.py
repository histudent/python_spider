# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/10/24 16:04'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from lxml import etree
import requests
class SaintMarysUniversity_USpider(scrapy.Spider):
    name = 'SaintMarysUniversity_U'
    allowed_domains = ['smu.ca/']
    start_urls = []
    C= [
        'https://smu.ca/academics/accounting.html',
        'https://smu.ca/academics/anthropology.html',
        'https://smu.ca/academics/asian-studies.html',
        'https://smu.ca/academics/astrophysics.html',
        'https://smu.ca/academics/atlantic-canada-studies.html',
        'https://smu.ca/academics/biology.html',
        'https://smu.ca/academics/chemistry.html',
        'https://smu.ca/academics/chinese-studies.html',
        'https://smu.ca/academics/classics.html',
        'https://smu.ca/academics/computing-and-information-systems.html',
        'https://smu.ca/academics/computing-science.html',
        'https://smu.ca/academics/computing-science-and-business-administration.html',
        'https://smu.ca/academics/criminology.html',
        'https://smu.ca/academics/economics.html',
        'https://smu.ca/academics/english.html',
        'https://smu.ca/academics/engineering.html',
        'https://smu.ca/academics/entrepreneurship.html',
        'https://smu.ca/academics/environmental-science.html',
        'https://smu.ca/academics/environmental-studies.html',
        'https://smu.ca/academics/film-studies.html',
        'https://smu.ca/academics/finance.html',
        'https://smu.ca/academics/french.html',
        'https://smu.ca/academics/forensic-science.html',
        'https://smu.ca/academics/general-business-studies.html',
        'https://smu.ca/academics/geography.html',
        'https://smu.ca/academics/geology.html',
        'https://smu.ca/academics/german.html',
        'https://smu.ca/academics/global-business-management.html',
        'https://smu.ca/academics/history.html',
        'https://smu.ca/academics/human-resource-management.html',
        'https://smu.ca/academics/intercultural-studies.html',
        'https://smu.ca/academics/international-development-studies.html',
        'https://smu.ca/academics/irish-studies.html',
        'https://smu.ca/academics/japanese-studies.html',
        'https://smu.ca/academics/linguistics.html',
        'https://smu.ca/academics/management.html',
        'https://smu.ca/academics/marketing.html',
        'https://smu.ca/academics/mathematics.html',
        'https://smu.ca/academics/philosophy.html',
        'https://smu.ca/academics/physics.html',
        'https://smu.ca/academics/political-science.html',
        'https://smu.ca/academics/psychology.html',
        'https://smu.ca/academics/religious-studies.html',
        'https://smu.ca/academics/social-justice-community-studies.html',
        'https://smu.ca/academics/sociology.html',
        'https://smu.ca/academics/hispanic-studies.html'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)

        #1.school_name
        school_name = "Saint Mary's University"
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.major_name_en
        major_name_en = response.xpath("//h1[@class='pageTitle']").extract()
        major_name_en = ''.join(major_name_en)
        major_name_en = remove_tags(major_name_en).strip()
        # print(major_name_en)

        #4.overview_en
        overview_en = response.xpath("//h2[contains(text(),'Why')]//following-sibling::hr[1]//preceding-sibling::p").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        if len(overview_en) < 20:
            overview_en = response.xpath("//h2[contains(text(),'Why')]//following-sibling::p[position()<3]|//h2[contains(text(),'About')]//following-sibling::p[position()<3]").extract()
            overview_en = ''.join(overview_en)
            overview_en = remove_class(overview_en)
            overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #5.department
        department = response.xpath("//a[contains(text(),'Faculty of')]|//a[contains(text(),'Sobey')]").extract()[0]
        department = remove_tags(department)
        if 'Sobey School of Business' in department:
            department = 'Sobey School of Business'
        department = department.strip()
        # print(department)

        #6.career_en
        career_en = response.xpath("//strong[contains(text(),'areer')]/../following-sibling::ul").extract()
        if len(career_en)==0:
            career_en = response.xpath("//p[contains(text(),'Future career opportunities')]//following-sibling::ul|//strong[contains(text(),'Career opportunities')]/../following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en,url)

        #7.modules_en
        modules_en = response.xpath("//span[contains(text(),'Program Courses')]/../following-sibling::ul").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        modules_en = clear_space_str(modules_en)
        # print(modules_en)
        if len(modules_en)==0:
            modules_en_url = response.xpath("//a[contains(text(),'Course')]//@href").extract()
            if len(modules_en_url)>0:
                modules_en_url = modules_en_url[0]
                modules_en_url = 'https://smu.ca'+modules_en_url
                # print(modules_en_url)
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
                try:
                    data = requests.get(modules_en_url, headers=headers)
                    response1 = etree.HTML(data.text)
                    modules_en = response1.xpath("//h2[contains(text(),'Course Descriptions')]//following-sibling::*|//h2[contains(text(),'Course Descriptions')]/../following-sibling::*")
                    doc = ""
                    if len(modules_en) > 0:
                        for a in modules_en:
                            doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                            doc = remove_class(doc)
                            modules_en = doc

                except:
                    modules_en = None
        if len(modules_en)==0:
            modules_en = None
        # print(modules_en)

        #8.ap
        ap = 'Credit for AP examined subjects, not listed above but with a grade of 4 or 5, will be determined on a case-by-case basis.'

        #9.toefl_desc 1011121314
        toefl_desc = 'minimum score of 80 overall with no band score below 20'
        toefl = 80
        toefl_r = 20
        toefl_w = 20
        toefl_s = 20
        toefl_l = 20

        #15.ielts_desc 1617181920
        ielts_desc = 'minimum score of 6.5 with no score below 6.0'
        ielts = 6.5
        ielts_r = 6
        ielts_w = 6
        ielts_s = 6
        ielts_l = 6

        #21.entry_requirements_en
        entry_requirements_en = 'National Senior High School - Graduation Examination with average of 65%'

        #22.require_chinese_en
        require_chinese_en = 'National Senior High School - Graduation Examination with average of 65%'

        #23.tuition_fee_pre
        tuition_fee_pre = '$'

        #24.tuition_fee
        if 'Arts' in department:
            tuition_fee = '1,727'
        elif 'commerce' in department or 'Business' in department:
            tuition_fee = '1,917'
        elif 'Science' in department:
            tuition_fee = '1,863'
        elif 'Engineering' in department:
            tuition_fee = '1,863'
        else:
            tuition_fee = None
        # print(tuition_fee,department)

        #25.start_date
        start_date = '2019-1,2019-5,2019-7,2019-9'

        #26.apply_fee
        apply_fee = 40

        #27.apply_pre
        apply_pre = '$CAD'

        #28.location
        location = 'Halifex, Nova Scotia'

        item['school_name'] = school_name
        item['url'] = url
        item['major_name_en'] = major_name_en
        item['overview_en'] = overview_en
        item['department'] = department
        item['career_en'] = career_en
        item['modules_en'] = modules_en
        item['ap'] = ap
        item['toefl_desc'] = toefl_desc
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_w'] = toefl_w
        item['toefl_l'] = toefl_l
        item['ielts_desc'] = ielts_desc
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['entry_requirements_en'] = entry_requirements_en
        item['require_chinese_en'] = require_chinese_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['start_date'] = start_date
        item['apply_fee'] = apply_fee
        item['apply_pre'] = apply_pre
        item['location'] = location
        yield item