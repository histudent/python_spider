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
    # start_urls = ["https://www.stu.edu/program-catalog.html"]
    start_urls = ["https://www.stu.edu/science/Programs/Pre-Engineering-2-2",
"https://www.stu.edu/slec/Programs/ba-communication-mediastudies.html",
"https://www.stu.edu/biscayne/programs/ba-criminal-justice.html",
"https://www.stu.edu/biscayne/Programs/ba-juris-doctor-three-plus-three",
"http://www.stu.edu/biscayne/Programs/ba-economics",
"http://www.stu.edu/biscayne/Programs/ba-english",
"http://www.stu.edu/biscayne/Programs/ba-juris-doctor-three-plus-three",
"http://www.stu.edu/biscayne/Programs/ba-english",
"http://www.stu.edu/biscayne/Programs/ba-liberal-studies",
"https://www.stu.edu/science/programs/nursing/index.html",
"https://www.stu.edu/biscayne/Programs/ba-juris-doctor-three-plus-three",
"http://www.stu.edu/biscayne/Programs/ba-political-science",
"https://www.stu.edu/biscayne/Programs/ba-juris-doctor-three-plus-three",
"http://www.stu.edu/biscayne/Programs/ba-psychology",
"http://www.stu.edu/biscayne/Programs/ba-psychology",
"https://www.stu.edu/biscayne/Programs/ba-juris-doctor-three-plus-three",
"http://www.stu.edu/theology/Programs/ba-religious-studies",
"https://www.stu.edu/business/programs/ba-sports-administration.html",
"https://www.stu.edu/business/Programs/bba-international-business",
"https://www.stu.edu/business/Programs/bba-management-cyber-security",
"https://www.stu.edu/business/Programs/bba-marketing",
"https://www.stu.edu/business/Programs/Bachelor-of-Business-Administration-in-Accounting",
"https://www.stu.edu/business/programs/bba-sports-administration.html",
"http://www.stu.edu/business/Programs/bba-finance",
"http://www.stu.edu/business/Programs/bba-management",
"http://www.stu.edu/business/Programs/bba-marketing",
"https://www.stu.edu/business/Programs/bba-management",
"http://www.stu.edu/business/Programs/bba-management-cyber-security",
"http://www.stu.edu/science/Programs/BS-in-Biology",
"http://www.stu.edu/science/Programs/Chemistry",
"http://www.stu.edu/science/Programs/Computer-Science",
"https://www.stu.edu/science/Programs/Mathematics",
"http://www.stu.edu/science/Programs/Nursing",
"https://www.stu.edu/biscayne/Programs/ba-juris-doctor-three-plus-three", ]
    print(len(start_urls))
    start_urls = list(set(start_urls))
    print(len(start_urls))

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)
        item['school_name'] = "St. Francis Xavier University"
        item['campus'] = 'Antigonish'
        item['location'] = 'Antigonish'
        item['url'] = response.url
        print("===========================")
        print(response.url)
        item['other'] = '''问题描述：1.'''

        '''公共字段'''
        # https://www.stu.edu/admissions/undergraduate.html
        # item['campus'] = 'Hamilton'
        # item['location'] = 'Hamilton'
        item['sat_code'] = item['toefl_code'] = '5076'
        item['act_code'] = '0719'
        # item['start_date'] = '9月'
        # item['duration'] = '4'
        # item['duration_per'] = 1
        item['apply_pre'] = 'CAD$'
        item['apply_fee'] = '40'
        item['tuition_fee_pre'] = 'CAD$'

        # https://www.stu.edu/students/Student-Affairs/International-Student-Services/international-admissions.html
        item['ielts_desc'] = 'IELTS: 5.5'
        item['ielts'] = '5.5'
        item['toefl_desc'] = 'TOEFL iBT®Test: 71'
        item['toefl'] = '71'
        try:
            department = response.xpath("//h1[contains(text(),'Biscayne College')]//text()|"
                                        "//h1[contains(text(),'School of Business')]//text()|"
                                        "//h1[contains(text(),'School of Law')]//text()|"
                                        "//h1[contains(text(),'School of Leadership, Education & Communication')]//text()|"
                                        "//h1[contains(text(),'School of Science')]//text()|"
                                        "//h1[contains(text(),'School of Tech')]//text()|"
                                        "//h1[contains(text(),'School of Engineering')]//text()|"
                                        "//h1[contains(text(),'School of Theology & Ministry')]//text()").extract()
            item['department'] = remove_class(clear_lianxu_space(department))
            # if item['department'] == "":
            #     print("***department 为空")
            # print("item['department']: ", item['department'])

            major_name_en = response.xpath("//h1[contains(text(),'Bachelor of')]//text()|//h1[contains(text(),'Pre')]//text()").extract()
            clear_space(major_name_en)
            major_name_en_str = ''.join(major_name_en).strip()
            if " in " in major_name_en_str:
                m_d_list = major_name_en_str.split(" in ")
                item['major_name_en'] = m_d_list[-1].replace("(BSN)", "").strip()
                item['degree_name'] = m_d_list[0].strip()
            else:
                item['major_name_en'] = major_name_en_str
            if item['major_name_en'] == "Bachelor of Arts / Juris Doctor 3 + 3":
                item['degree_name'] = "Bachelor of Arts"
                item['department'] = "Biscayne College"
            print("item['degree_name']: ", item['degree_name'])
            print("item['major_name_en']: ", item['major_name_en'])
            print("item['department']: ", item['department'])


            overview = response.xpath("//h3[contains(text(),'Program Highlights')]/preceding-sibling::p").extract()
            if len(overview) == 0:
                overview = response.xpath("//h3[contains(text(),'Featured Professors')]/../h3[1]/preceding-sibling::p|"
                                          "//span[contains(text(),'Featured Professors')]/../../h3[1]/preceding-sibling::p").extract()
                if len(overview) == 0:
                    overview = response.xpath(
                        "//span[contains(text(),'BA in Sports Management Degree Highlights')]/../preceding-sibling::*[position()<last()-2]").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview)).replace("<p></p>", "").strip()
            if item['overview_en'] == "":
                item['overview_en'] = None
                # print("***overview_en 为空")
            # print("item['overview_en']: ", item['overview_en'])

            career = response.xpath("//h3[contains(text(),'Career Opportunities')]|//h3[contains(text(),'Career Opportunities')]/following-sibling::*[1]|"
                                    "//h3[contains(text(),'Career Landscape')]|//h3[contains(text(),'Career Landscape')]/following-sibling::*[1]").extract()
            if len(career) == 0:
                career = response.xpath(
                    "//span[contains(text(),'Career Landscape')]/..|//span[contains(text(),'Career Landscape')]/../following-sibling::*[position()<3]").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career)).replace("<h3><span>Alumni Highlights</span></h3>", "").strip()
            if item['career_en'] == "":
                item['career_en'] = None
                # print("***career_en 为空")
            # print("item['career_en']: ", item['career_en'])

            # modules1 = response.xpath("//em[contains(text(),'Course Sampling')]/..").extract()
            modules2 = response.xpath("//em[contains(text(),'Course Sampling)')]/../following-sibling::p/strong|"
                                      "//h3[contains(text(),'Curriculum')]/following-sibling::p/strong|"
                                      "//span[contains(text(),'Curriculum (Course Sampling)')]/../following-sibling::p[1]").extract()
            print(modules2)
            modules3 = response.xpath("//em[contains(text(),'Course Sampling')]/../../text()|//h3[contains(text(),'Curriculum')]/../text()").extract()
            if len(modules3) != 0:
                modules3 = clear_lianxu_space(modules3)
                print("modules3: ",modules3)
            # if len(modules) == 0:
            #     modules = response.xpath(
            #         "//span[contains(text(),'Career Landscape')]/..|//span[contains(text(),'Career Landscape')]/../following-sibling::*[position()<3]").extract()
            # print(modules)
            # item['modules_en'] = remove_class(clear_lianxu_space(modules)).replace("<h3><span>Alumni Highlights</span></h3>", "").strip()
            # if item['modules_en'] == "":
            #     item['modules_en'] = None
            #     print("***modules_en 为空")
            # print("item['modules_en']: ", item['modules_en'])

            yield item

        except Exception as e:
            with open("scrapySchool_Canada_Ben/error/" + item['school_name'] + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_modules(self, major_modules_url):
        from selenium import webdriver
        # import time
        # os.chdir(r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Lib\site-packages\selenium")
        driver = webdriver.Chrome(r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Lib\site-packages\selenium\chromedriver.exe")
        driver.get(major_modules_url)
        # time.sleep(3)
        modules_en = driver.find_element_by_xpath("//table[@cellpadding='3']").get_attribute('outerHTML')
        modules_en = remove_class(clear_lianxu_space([modules_en]))
        driver.quit()
        return modules_en