# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/29 12:24'

import scrapy, json
import re
from scrapy.spiders import CrawlSpider, Rule
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
    name = 'SwinburneUniversityofTechnology_u'
    allowed_domains = ['swinburne.edu.au/']
    start_urls = []
    C = [
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-information-and-communication-technology/business-systems/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/japanese/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/creative-writing-and-literature/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication/digital-advertising-technology/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-engineering-honours/construction/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/politics-and-international-relations/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-design/ux-interaction-design/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-computer-science/software-design/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/philosophy/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/digital-advertising-technology/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business/sports-management/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-computer-science-professional/internet-of-things/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication-professional/journalism/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication/public-relations/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication-professional/cinema-and-screen-studies%20/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science-professional/psychology-and-psychophysiology/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/professional-writing-and-editing/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-accounting/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-computer-science-professional/games-development/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/chinese/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science/neuroscience/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-animation/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-engineering-honours/robotics-and-mechatronics/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/chinese/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-psychology-honours/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/games-interactivity/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-computer-science-professional/data-science/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-engineering-practice-honours/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-engineering-honours/architectural/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science/psychology-and-psychophysiology/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/history/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-design/photomedia/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication-professional/digital-advertising-technology/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business/entrepreneurship-and-innovation/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-information-and-communication-technology/systems-analysis/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business-professional/business-administration/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/politics-and-international-relations/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-computer-science-professional/software-design/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication/advertising/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business-professional/information-systems/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-science/chemistry/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-science-professional/applied-mathematics/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-engineering-honours/telecommunications/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-information-and-communication-technology/software-technology/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-laws-graduate-entry/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-science-professional/environmental-science/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business/international-business/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-science-professional/physics/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/advertising/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/social-media/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-design/digital-media-design/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-science/environmental-science/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-computer-science/games-development/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/media-industries/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-design/communication-design/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-engineering-honours/product-design/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science-professional/nutrition/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication/cinema-and-screen-studies%20/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication/games-interactivity/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-sport-and-exercise-science/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business/human-resource-management/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science/psychology-and-forensic-science/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-computer-science/cybersecurity/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science/applied-statistics/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-computer-science-professional/software-development/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/digital-advertising-technology/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-screen-production/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/social-media/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-engineering-honours/Civil/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/sociology/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science-professional/neuroscience/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-film-and-television-honours/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication/social-media/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business-professional/marketing/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/sociology/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business/financial-planning/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business-professional/human-resource-management/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication-professional/creative-writing-and-literature/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business/accounting-and-finance/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/philosophy/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-aviation-management/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-science-professional/biotechnology/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/professional-writing-and-editing/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-science/applied-mathematics/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science-professional/applied-statistics/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/japanese/',
        'https://www.swinburne.edu.au/study/course/bachelor-of-arts-professional/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication-professional/advertising/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication/creative-writing-and-literature/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/games-interactivity/',
        'https://www.swinburne.edu.au/study/course/bachelor-of-health-science/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business/economics/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business-professional/management/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-computer-science-professional/cybersecurity/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/criminology/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business/logistics-and-supply-chain-management/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business/marketing/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-computer-science/software-development/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-information-and-communication-technology/systems-management/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-computer-science/internet-of-things/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business-professional/finance/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-science/biochemistry/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-computer-science-professional/network-design/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business-professional/financial-planning/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business-administration/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business-professional/entrepreneurship-and-innovation/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science/biomedical-science/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/advertising/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/environmental-sustainability/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication-professional/media-industries/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-engineering-honours/software/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-computer-science/data-science/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-psychological-sciences/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-games-and-interactivity/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-science/physics/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-engineering-honours/mechanical/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-science/biotechnology/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication-professional/professional-writing-and-editing/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication/journalism/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business-professional/economics/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/environmental-sustainability/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/journalism/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-computer-science/network-design/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/cinema-and-screen-studies%20/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication-professional/public-relations/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-aviation-and-piloting/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business-professional/international-business/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-engineering-honours/biomedical/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-design-industrial-design-honours/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication-professional/games-interactivity/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business-professional/sports-management/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-design-interior-architecture-honours/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business/finance/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/media-industries/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science-professional/applied-statistics/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-innovation-and-design/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science-professional/neuroscience/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science-professional/biomedical-science/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business/business-administration/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science-professional/psychology-and-psychophysiology/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science-professional/psychology-and-forensic-science/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/creative-writing-and-literature/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science-professional/nutrition/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science-professional/clinical-technologies/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-information-and-communication-technology/network-technology/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science-professional/health-promotion/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science-professional/digital-health-and-informatics',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/journalism/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication/media-industries/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-design-architecture/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business-professional/accounting/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-science-professional/biochemistry/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business/information-systems/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-design/branded-environments/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-education-early-childhood/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science-professional/psychology-and-forensic-science/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication-professional/social-media/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts/criminology/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science/nutrition/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-media-and-communication/professional-writing-and-editing/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business-professional/logistics-and-supply-chain-management/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-health-science-professional/biomedical-science/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/cinema-and-screen-studies%20/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business/management/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business/accounting/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-business-information-systems/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-engineering-honours/electrical-and-electronic/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-science-professional/chemistry/',
        'https://www.swinburne.edu.au/study/course/international/bachelor-of-arts-professional/history/'
    ]
    for i in C:
        start_urls.append(i)

    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        # 1.university
        university = 'Swinburne University of Technology'
        # print(university)

        # 2.url
        url = response.url
        # print(url)

        # 3.department
        try:
            department = response.xpath("//*[contains(text(),'Faculty')]//following-sibling::*").extract()
            department = ''.join(department)
            department = remove_tags(department).strip()
            # print(department)
        except:
            department = 'N/A'
        # print(department,response.url)

        # 4.programme_en
        try:
            programme_en = response.xpath('//*[@id="course-subtitle"]').extract()
            programme_en = ''.join(programme_en)
            programme_en = remove_tags(programme_en).replace('with a major in ','')
            if len(programme_en)==0:
                programme_en = response.xpath('//*[@id="content"]/main/section[1]/header/div[1]/h1').extract()
                programme_en = ''.join(programme_en)
                programme_en = remove_tags(programme_en)
                if ' (Honours)' in programme_en:
                    programme_en = programme_en.replace(' (Honours)','').strip()
                elif ' (Professional)' in programme_en:
                    programme_en = programme_en.replace(' (Professional)','').strip()
                elif '(Early Childhood)' in programme_en:
                    programme_en = programme_en
            else:
                if'(' in programme_en:
                    programme_en = re.findall(r'\((.*)\)',programme_en)
                else:programme_en = programme_en
                # print(programme_en)
        except:
            programme_en = 'N/A'
        if 'Bachelor of ' in programme_en:
            programme_en = programme_en.replace('Bachelor of ','')
        # print(programme_en)

        # 5.degree_name
        degree_name = response.xpath('//*[@id="content"]/main/section[1]/header/div[1]/h1').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        # 6.start_date
        start_date = response.xpath("//*[contains(text(),'Start')]//following-sibling::*").extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        if 'March' in start_date and 'August' in start_date:
            start_date = '3,8'
        elif 'February' in start_date and 'July' in start_date:
            start_date = '2,7'
        elif 'March' in start_date:
            start_date = '3'
        elif 'February' in start_date:
            start_date = '2'
        else: start_date = '2,6,10'
        # print(start_date)

        # 7.degree_overview_en
        try:
            degree_description = response.xpath('//*[@id="content"]/main/section[1]/div/div[2]/div[1]/div[1]/p').extract()
            degree_description = ''.join(degree_description)
            degree_description = remove_class(degree_description)
            degree_overview_en = degree_description
            # print(degree_description)
        except:
            degree_overview_en = 'N/A'
        # print(degree_overview_en)

        # 8.apply_pre
        apply_pre = 'A$'

        # 9.duration
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
            modules_en = response.xpath('//h3[contains(text(),"Course structure")]/following-sibling::div/table[position()<2]').extract()
            modules_en = ''.join(modules_en)
            modules_en = remove_class(modules_en)
        except:
            modules_en = 'N/A'
        # print(modules_en)


        # 11.career_en
        try:
            career_en = response.xpath('//h3[contains(text(),"Career")]/following-sibling::div[1]//text()').extract()
            career_en = ''.join(career_en).strip()
            career_en = '<p>' + career_en + '</p>'
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

        # 13.rntry_requirements_en
        try:
            rntry_requirements_en = \
            response.xpath('//*[contains(text(),"Entry requirements")]/following-sibling::*').extract()[0]
            rntry_requirements_en = remove_class(rntry_requirements_en)
            #
        except:
            rntry_requirements_en = 'N/A'
        # print(rntry_requirements_en)


        # 14.ielts 15161718 19.toefl 20212223
        ielts_text = response.xpath(
            '//*[contains(text(),"English language requirements")]/following-sibling::div').extract()
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

        # 24.apply_proces_en
        apply_proces_en = 'https://www.swinburne.edu.au/study/international/apply/'


        # 25.apply_desc_en
        apply_desc_en ='Before you start your application, make sure you have followed these important steps. After checking these details, you will be ready to start your application to study at Swinburne.You can also read about the Australian Government’s Education Services for Overseas Students (ESOS) regulatory framework so that you understand your rights and responsibilities as an international student before and during your study.1. Check that you are an international student2. Select your course3. Check entry requirements4. Check to see if you are eligible for credit5. Review tuition fees6. Compile education and employment history7. Prepare your documents8. Begin your application'

        # 26.url
        url = response.url

        # 27.location
        location = 'Melbourne'

        # 28.tuition_fee_pre
        tuition_fee_pre = 'A$'

        # 29.degree_type
        degree_type = 1

        #30.overview_en
        overview_en = response.xpath("//*[contains(text(),'Selected major:')]/../following-sibling::p[1]").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        item['overview_en'] = overview_en
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