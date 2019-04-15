# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/29 10:47'
import scrapy,json
import re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from w3lib.html import remove_tags
from scrapySchool_England.clearSpace import clear_space_str
import requests
from lxml import etree
class SwinburneUniversityofTechnologySpider(scrapy.Spider):
    name = 'SwinburneUniversityofTechnology_p'
    allowed_domains = ['swinburne.edu.au/']
    start_urls = []
    C = [
        'https://www.swinburne.edu.au/study/course/Master-of-Architecture-MA-ARC/international',
        'https://www.swinburne.edu.au/study/course/Master-of-Architecture-and-Urban-Design-MA-ARCUD/international',
        'https://www.swinburne.edu.au/study/course/Master-of-Business-Administration-(Advanced)-MA-MBAADV/international',
        'https://www.swinburne.edu.au/study/course/Master-of-Cybersecurity-MA-CYBSEC/international',
        'https://www.swinburne.edu.au/study/course/Master-of-Occupational-Therapy-MA-OCC/international',
        'https://www.swinburne.edu.au/study/course/Master-of-Physiotherapy-MA-PHYS/international',
        'https://www.swinburne.edu.au/study/course/Master-of-Teaching-(Primary)-MA-TEAPRI3/international',
        'https://www.swinburne.edu.au/study/course/Master-of-Urban-Design-MA-UD/international'
    ]
    C= set(C)
    # print(len(C))
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Swinburne University of Technology'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.department
        try:
            department = response.xpath('//*[@id="content"]/main/section[1]/div[2]/div/comment()').extract()
            department = ''.join(department).replace('Faculty', '')
            department = clear_space_str(department)
            department = remove_tags(department).replace(' -->','').strip()
            department = 'Faculty ' + department
            # print(department)
        except:
            department = 'N/A'

        #4.programme_en
        try:
            programme_en = response.xpath('//*[@id="content"]/main/section[1]/header/div[1]/h1').extract()[0]
            programme_en = remove_tags(programme_en )
            programme_en = programme_en .replace('Master of ','').strip()
        except:
            programme_en = 'N/A'
        if '(International)'in programme_en :
            programme_en = programme_en
        elif ' (Professional)' in programme_en:
            programme_en = programme_en
        elif '(Advanced)' in programme_en :
            programme_en = programme_en
        elif '(Executive)' in programme_en :
            programme_en = programme_en
        else:
            if '(' in programme_en :
                programme_en = re.findall(r'\((.*)\)',programme_en)[0]
            else:
                programme_en = programme_en
        # print(programme_en)

        #5.degree_name
        degree_name = response.xpath('//*[@id="content"]/main/section[1]/header/div[1]/h1').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #6.start_date
        start_date = '2,7'

        #7.degree_overview_en
        try:
            degree_description = response.xpath('//*[@id="content"]/main/section[1]/div[2]/div[1]').extract()
            degree_description = ''.join(degree_description)
            degree_description = remove_class(degree_description)
            degree_overview_en = degree_description
            # print(degree_description)
        except:
            degree_overview_en = 'N/A'

        #8.apply_pre
        apply_pre = 'A$'

        #9.duration
        try:
            duration = response.xpath('//h3[contains(text(),"Duration")]/following-sibling::p').extract()[0]
            duration = remove_tags(duration)
            # duration=re.findall('\d\.?\d?',duration)
            # duration=''.join(duration)
            # print(duration)
        except:
            duration = 'N/A'
        # print(duration)


        # 10.modules_en
        try:
            modules_en = response.xpath('//h3[contains(text(),"Course description")]/following-sibling::div').extract()
            modules_en = ''.join(modules_en)
            modules_en = remove_class(modules_en)
        except:
            modules_en = 'N/A'
        # print(modules_en)


        # 11.career_en
        try:
            career_en = response.xpath('//h3[contains(text(),"Career")]/following-sibling::div[1]//text()').extract()
            career_en = ''.join(career_en).strip()
            career_en = '<p>'+career_en+'</p>'
            #
        except:
            career_en = ''
        # print(career_en)


        # 12.tuition_fee
        try:
            tuition_fee = response.xpath('//h3[contains(text(),"Fee")]/following-sibling::p').extract()[0]
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = re.findall('\$\d{4,6}', tuition_fee)
            tuition_fee = ''.join(tuition_fee).replace('$', '')
            # print(tuition_fee,response.url)
        except:
            tuition_fee = 0

        #13.rntry_requirements_en
        try:
            rntry_requirements_en =response.xpath('//h3[contains(text(),"Entry requirements")]/following-sibling::div').extract()[0]
            rntry_requirements_en = remove_class(rntry_requirements_en)
            #
        except:
            rntry_requirements_en = 'N/A'
        # print(rntry_requirements_en)


        # 14.ielts 15161718 19.toefl 20212223
        ielts_text = response.xpath(
            '//h3[contains(text(),"English language requirements")]/following-sibling::div').extract()
        ielts_text = ''.join(ielts_text)
        # print(ielts_text)
        ielts = re.findall('[567]\.\d', ielts_text)
        ielts = ''.join(ielts)
        toefl = re.findall('score of [6-9]\d[\sa-zA-Z\,]*[0-2]\d[\sa-zA-Z]*[0-2]?\d?', ielts_text)
        toefl = ''.join(toefl)
        # print(ielts)
        toefls = re.findall('\d{2}', toefl)
        # print(toefls)
        if len(toefls) == 3:
            toefl = toefls[0]
            toefl_r = toefls[1]
            toefl_w = toefls[1]
            toefl_s = toefls[2]
            toefl_l = toefls[2]
        else:
            toefl_r = None
            toefl_w = None
            toefl_s = None
            toefl_l = None
        ieltss = re.findall('\d.\d', ielts)
        if ieltss:
            ielts = max(ieltss)
            ielts_l, ielts_s, ielts_r, ielts_w = min(ieltss), min(ieltss), min(ieltss), min(ieltss)
        else:
            ielts_l, ielts_s, ielts_r, ielts_w = '', '', '', ''
        # 检查后面的托福成绩toefl =response.xpath('//h3[contains(text(),"English language requirements")]/following-sibling::div').extract()
        # print(toefl,toefl_r,toefl_w,toefl_s,toefl_l)
        # print(ielts,ielts_w,ielts_r,ielts_s,ielts_l)
        # ielts = ''
        # toefl = ''
        # ielts_l, ielts_s, ielts_R, ielts_w ='','','',''
        # toefl_r = ''
        # toefl_w = ''

        #24.apply_proces_en
        apply_proces_en = [
            "Before you start your application, make sure you have followed these important steps. After checking these details, you will be ready to start your application to study at Swinburne.",
            "You can also read about the Australian Government’s Education Services for Overseas Students (ESOS) regulatory framework so that you understand your rights and responsibilities as an international student before and during your study.",
            "1. Check that you are an international student",
            "2. Select your course",
            "3. Check entry requirements",
            "4. Check to see if you are eligible for credit",
            "5. Review tuition fees",
            "6. Compile education and employment history",
            "7. Prepare your documents",
            "8. Begin your application"]
        apply_proces_en = ''.join(apply_proces_en)
        apply_proces_en = '<p>'+apply_proces_en+'</p>'

        # 25.apply_desc_en
        apply_desc_en = ["You may also be required to submit documents to support your application.",
                                 "certified academic documents",
                                 "certified copy of your passport",
                                 "English proficiency test results",
                                 "certified copy of unit outlines and academic transcripts",
                                 "portfolio (for most design courses)",
                                 "English translations of all documents, if not already in English"]
        apply_desc_en = ''.join(apply_desc_en)
        apply_desc_en = '<p>'+apply_desc_en+'</p>'

        #26.url
        url = response.url

        #27.location
        location = 'Hawthorn'

        #28.tuition_fee_pre
        tuition_fee_pre = 'A$'

        #29.degree_type
        degree_type = 2

        item['tuition_fee_pre'] = tuition_fee_pre
        item['degree_type'] = degree_type
        item['university'] = university
        item['url'] = url
        item['department'] = department
        item['programme_en'] = programme_en
        item['degree_name'] = degree_name
        item['start_date'] = start_date
        item['degree_overview_en'] = degree_overview_en
        item['duration'] = duration
        item['apply_pre'] = apply_pre
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['rntry_requirements_en'] = rntry_requirements_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['apply_proces_en'] = apply_proces_en
        item['apply_desc_en'] = apply_desc_en
        item['url'] = url
        item['location'] = location
        yield item