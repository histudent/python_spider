# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/11/7 10:34'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from lxml import etree
import requests
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
class CapeBretonUniversity_USpider(scrapy.Spider):
    name = 'CapeBretonUniversity_U'
    allowed_domains = ['cbu.ca/']
    start_urls = []
    C= [
        'https://www.cbu.ca/academic-programs/program/emergency-management-2/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)

        #1.school_name
        school_name = 'Cape Breton University'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.major_name_en
        major_name_en = response.xpath("/html/body/section[1]/div/div[2]/h1").extract()
        major_name_en = ''.join(major_name_en)
        major_name_en = remove_tags(major_name_en).strip()
        # print(major_name_en)

        #5.department
        department = response.xpath("/html/body/section[1]/div/div[2]/ul/li[2]").extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #6.overview_en
        overview_en = response.xpath(
            "//span[contains(text(),'What is the')]/../following-sibling::*|//span[contains(text(),'What Is The')]/../following-sibling::*|//b[contains(text(),'What is the')]/../following-sibling::*|//b[contains(text(),'What Is The')]/../following-sibling::*|//span[contains(text(),'What Is')]/../following-sibling::*|//b[contains(text(),'What Is')]/../following-sibling::*").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        end = overview_en.find('Why Study')
        # print(end)
        overview_en = overview_en[:end].replace('<h2><b>','').replace('<h2><span>','')

        #7.career_en
        career_en = response.xpath("//*[contains(text(),'Possible Career Paths')]/../following-sibling::*|//*[contains(text(),'Career Path')]/../following-sibling::*|//strong[contains(text(),'Chemistry opens doors to career opportunities in')]/../following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)

        #8.modules_en
        driver = webdriver.Chrome()
        try:
            driver.get("http://calendar.cbu.ca/")
            input = driver.find_element_by_id('searchwords')
            input.send_keys(major_name_en)
            time.sleep(1)
            s1 = Select(driver.find_element_by_id('what'))
            s1.select_by_value('Catalog')
            time.sleep(1)
            button = driver.find_element_by_id('searchBtn')
            button.click()
            time.sleep(10)
            modules_en = driver.find_element_by_xpath('//*[@id="sis-wrap"]').text
            modules_en = re.findall('([A-Z\d\s]+-[A-Z\s:&,"?I]+)',modules_en)
            doc = ''
            for i in modules_en:
                i = i.replace('\n','').strip()
                doc+= '<p>' + i +'</p>'
                modules_en = doc
        except:
            modules_en = None

        driver.quit()
        if modules_en == []:
            modules_en = None

        #9.location
        location = 'Sydney, Nova Scotia'

        #10.entry_requirements_en
        entry_requirements_en = '<p>An overall average of 65% is required for all students applying to most CBU credit programs based on high school performance. Additional requirements may apply to specific programs.</p>'

        #11.require_chinese_en
        require_chinese_en = '<p>Senior Middle School Graduation Certificate and Transcript</p><p>Applications from international students will be reviewed on an individual basis.We require graduation from an academic secondary school program or equivalent with an average of “C” in five, senior academic-level/university preparatory courses.</p>'

        #12.toefl_desc 13.toefl
        toefl_desc = 'Internet-Based Test: 80'
        toefl = 80

        #14.ielts_desc 1516171819
        ielts_desc = 'Overall Score: 6.5,No Band Below: 6.0'
        ielts = 6.5
        ielts_r = 6.0
        ielts_w = 6.0
        ielts_s = 6.0
        ielts_l = 6.0

        #20.tuition_fee #21.tuition_fee_pre
        tuition_fee = '8,476.30'
        tuition_fee_pre = '$'

        #22.apply_fee #23.apply_pre
        apply_fee = '103'
        apply_pre = '$'

        #24.alevel
        alevel = 'General Certificate of Education; including a minimum of two Advanced Level courses (A Level) or four Advanced Supplementary levels (AS level) subjects and 5 GCSE subjects (O Level).'

        #25.deadline
        deadline = '2019-03-01'

        #26.toefl_code  #27.sat_code
        toefl_code = '9142'
        sat_code =toefl_code

        item['school_name'] = school_name
        item['url'] = url
        item['major_name_en'] = major_name_en
        item['department'] = department
        item['overview_en'] = overview_en
        item['career_en'] = career_en
        item['modules_en'] = modules_en
        item['location'] = location
        item['entry_requirements_en'] = entry_requirements_en
        item['require_chinese_en'] = require_chinese_en
        item['toefl_desc'] = toefl_desc
        item['toefl'] = toefl
        item['ielts_desc'] = ielts_desc
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_fee'] = apply_fee
        item['apply_pre'] = apply_pre
        item['alevel'] = alevel
        item['deadline'] = deadline
        item['toefl_code'] = toefl_code
        item['sat_code'] = sat_code



        #4.degree_name 要拆开
        degree_name = response.xpath("/html/body/section[1]/div/div[2]/ul/li[1]").extract()[0]
        degree_name = remove_tags(degree_name)
        if 'Bachelor of Arts and Bachelor of Arts Community Studies' in degree_name:
            degree_name = ['Bachelor of Arts','Bachelor of Arts Community Studies']
        elif 'Bachelor of Arts, Bachelor of Science, and Bachelor of Arts Community Studies' in degree_name:
            degree_name = ['Bachelor of Arts','Bachelor of Science','Bachelor of Arts Community Studies']
        elif 'Bachelor of Arts, Bachelor of Arts Community Studies and Bachelor of Science' in degree_name:
            degree_name = ['Bachelor of Arts','Bachelor of Arts Community Studies','Bachelor of Science']
        elif 'Bachelor of Arts, Bachelor of Arts Community Studies and Bachelor of Arts in Environment' in degree_name:
            degree_name = ['Bachelor of Arts','Bachelor of Arts Community Studies','Bachelor of Arts in Environment']
        elif 'Bachelor of Business Administration' in degree_name:
            degree_name = ['Bachelor of Business Administration']
        elif 'Bachelor of Arts Community Studies' in degree_name:
            degree_name = ['Bachelor of Arts Community Studies']
        elif 'Bachelor of Engineering Technology' in degree_name:
            degree_name = ['Bachelor of Engineering Technology']
        elif 'Bachelor of Science' in degree_name:
            degree_name = ['Bachelor of Science']
        else:
            degree_name = ['Bachelor of Arts']
        for i in degree_name:
            degree_name = i
            item['degree_name'] = degree_name
            try:
                major = response.xpath("//strong[contains(text(),'Degree Options:')]/../preceding-sibling::li//following-sibling::li").extract()[-1]
            except:
                major = 'Major'
            if 'Honours' in major and 'Major' in major:
                other = ['Major','Honours']
            elif 'Honours' in major:
                other = ['Honours']
            elif 'Major' in major:
                other = ['Major']
            else:
                other = ['Major']
            for j in other:
                other = j
                item['other'] = other
                yield item

