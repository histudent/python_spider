# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/11/1 14:27'
import time
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from lxml import etree
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class UniversityofCalgary_USpider(scrapy.Spider):
    name = 'UniversityofCalgary_U'
    # allowed_domains = ['ucalgary.ca/']
    start_urls = []
    C= [
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/accounting',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/actuarial-science',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/ancient-medieval-history',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/anthropology-biological',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/anthropology-social-cultural',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/archaeology',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/art-history',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/astrophysics',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/biochemistry',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/bioinformatics',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/biological-sciences',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/biomechanics',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/biomedical-sciences',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/business-analytics',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/business-technology-management',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/canadian-studies',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/cellular-molecular-microbial-biology',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/chemical-engineering',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/chemistry',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/civil-engineering',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/communication-media-studies',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/community-rehabilitation',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/computer-science',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/dance',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/development-studies',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/drama',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/earth-science',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/east-asian-language-studies',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/east-asian-studies',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/ecology',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/economics',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/education',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/electrical-engineering',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/energy-engineering',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/energy-management',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/english',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/entrepreneurship-innovation',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/environmental-science',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/exercise-health-physiology',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/film-studies',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/finance',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/french',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/general-commerce',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/general-mathematics',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/geography',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/geology',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/geomatics-engineering',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/geophysics',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/german',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/greek-roman-studies',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/health-society',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/history',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/international-business-strategy',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/international-indigenous-studies',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/international-relations',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/italian-studies',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/kinesiology',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/latin-american-studies',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/law-society',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/leadership-pedagogy-coaching',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/linguistics',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/linguistics-language',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/marketing',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/mathematics',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/mechanical-engineering',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/mind-sciences-kinesiology',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/multidisciplinary-studies-bachelor-arts',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/music-bachelor-arts',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/music-bachelor-music',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/natural-sciences',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/neuroscience-0',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/nursing',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/oil-gas-engineering',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/operations-management',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/organizational-behaviour-human-resources',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/personal-financial-planning',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/petroleum-land-management',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/philosophy',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/physics',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/plant-biology',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/political-science',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/psychology-bachelor-arts',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/psychology-bachelor-science',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/real-estate',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/religious-studies',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/risk-management-insurance',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/risk-management-insurance-finance',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/russian',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/social-work',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/sociology',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/software-engineering',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/spanish',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/supply-chain-management',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/urban-studies',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/visual-studies',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/womens-studies',
        'https://www.ucalgary.ca/future-students/undergraduate/explore-programs/zoology-0'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)

        #1.school_name
        school_name = 'University of Calgary'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.major_name_en
        major_name_en = response.xpath("//h1").extract()
        major_name_en = ''.join(major_name_en)
        major_name_en = remove_tags(major_name_en).strip()
        # print(major_name_en)

        #4.degree_name
        degree_name = response.xpath("//div[@class='cta-content cta-content-left']//h4").extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        degree_name = clear_space_str(degree_name).replace('Bachelor',' Bachelor').strip()
        # print(degree_name)

        #5.overview_en
        overview_en = response.xpath("//h2[contains(text(),'What you will learn in this program')]//following-sibling::*").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #6.career_en
        career_en = response.xpath("//h3[contains(text(),'Career opportunities')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #7.modules_en
        try:
            modules_en_url = response.xpath("//a[contains(text(),'List of Courses in the Program​')]//@href").extract()[0]
        except:
            modules_en_url = []
        # print(modules_en_url)
        if len(modules_en_url)>0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            try:
                data = requests.get(modules_en_url, headers=headers,verify=False)
                response1 = etree.HTML(data.text)
                modules_en = response1.xpath("/html[1]/body[1]/table[1]//tr[1]/td[2]/table[1]")
                doc = ""
                if len(modules_en) > 0:
                    for a in modules_en:
                        doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                        doc = remove_class(doc)
                        modules_en = doc
            except:
                modules_en = None
        else:
            modules_en = None
        if modules_en == []:
            modules_en = None
        # print(modules_en)

        #8.department
        department = response.xpath('//*[@id="views-form-requirements-block-1"]/div/div[4]/div/text()').extract()
        department = ''.join(department)
        department = clear_space_str(remove_tags(department).strip())
        # print(department)

        #9.deadline
        deadline = '2019-03-01'

        #10.ielts_desc 1112131415
        ielts_desc = 'Education:8.0 with no bands below a 7.0,Nursing:7.0 with no bands below a 7.0,All Other Undergraduate Programs:6.5'
        if 'Nursing' in major_name_en:
            ielts = 8.0
            ielts_s = 7.0
            ielts_l = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
        elif 'Education' in major_name_en:
            ielts = 7.0
            ielts_s = 7.0
            ielts_l = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
        else:
            ielts =6.5
            ielts_s = None
            ielts_l = None
            ielts_r = None
            ielts_w = None

        #16.toefl_desc 1718192021
        toefl_desc = 'Education:100 with a minimum of 27 in each sub-score,Nursing:92 with a minimum of 23 in each sub-score,All Other Undergraduate Programs:86'
        if 'Nursing' in major_name_en:
            toefl = 100
            toefl_r = 27
            toefl_w = 27
            toefl_s = 27
            toefl_l = 27
        elif 'Education' in major_name_en:
            toefl = 92
            toefl_r = 23
            toefl_w = 23
            toefl_s = 23
            toefl_l = 23
        else:
            toefl = 86
            toefl_r = None
            toefl_w = None
            toefl_s = None
            toefl_l = None

        #22.toefl_code 23.sat_code
        toefl_code = '0813'
        sat_code = '0813'

        #24.tuition_fee #25.tuition_fee_pre
        if 'law' in major_name_en:
            tuition_fee = '1,136.94/per 3 Units'
        else:
            tuition_fee = '611.28/per 3 Units'
        tuition_fee_pre = '$'

        #26.apply_fee  27.apply_pre
        apply_fee = 125
        apply_pre = '$'

        #28.ap
        ap = "AP students automatically receive advanced credit or advanced placement in approved courses where they present grades of 4 or higher. In the case of advanced credit, a grade of 'CR' will be recorded on the student's record. Official AP transcripts are required as part of the evaluation process."

        #29.alevel #30.sat #31.act #32.require_chinese_en #33.entry_requirements_en #34.ib

        item['school_name'] = school_name
        item['url'] = url
        item['major_name_en'] = major_name_en
        item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['career_en'] = career_en
        item['modules_en'] = modules_en
        item['department'] = department
        item['deadline'] = deadline
        item['ielts_desc'] = ielts_desc
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl_desc'] = toefl_desc
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['toefl_code'] = toefl_code
        item['sat_code'] = sat_code
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_fee'] = apply_fee
        item['apply_pre'] = apply_pre
        item['ap'] = ap
        yield  item

