# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/29 14:52'
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
import urllib.request
class JamesCookUniversitySpider(scrapy.Spider):
    name = 'JamesCookUniversity_u'
    allowed_domains = ['jcu.edu.au/']
    start_urls = []
    C= ['https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-advanced-science',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-arts',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-arts-bachelor-of-business',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-arts-bachelor-of-laws',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-arts-bachelor-of-science',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-biomedical-sciences',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-business',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-business-and-environmental-science',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-business-bachelor-of-laws',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-business-bachelor-of-psychological-science',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-creative-arts-and-media',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-dental-surgery',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-economics-honours',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-education-primary',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-education-early-childhood-education',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-education-secondary',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-education-professional-development',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-engineering-honours',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-environmental-practice',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-exercise-physiology-clinical',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-geology',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-health-science-physician-assistant',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-information-technology',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-laws-graduate-entry',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-laws',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-marine-science',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-medical-laboratory-science-honours',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-medicine,-bachelor-of-surgery',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-nursing-science',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-nursing-science-bachelor-of-midwifery',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-occupational-therapy-honours',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-pharmacy',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-physiotherapy',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-planning',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-psychological-science',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-psychology-honours',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-science',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-science-bachelor-of-laws',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-social-work',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-speech-pathology',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-sport-and-exercise-science',
'https://www.jcu.edu.au/courses-and-study/international-courses/bachelor-of-veterinary-science']
    # print(len(C))
    C= set(C)
    # print(len(C))
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'James Cook University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.degree_name
        degree_name = response.xpath('//*[@id="main"]/div/div[2]/div[2]/div[1]/div/h1').extract()
        degree_name = ''.join(degree_name)
        degree_name= remove_tags(degree_name)
        # print(degree_name)

        #4.degree_overview_en
        degree_overview_en = response.xpath('//*[@id="main"]/div/div[2]/div[3]/div/div/div[2]/div[2]/div[1]/p').extract()
        degree_overview_en = ''.join(degree_overview_en)
        degree_overview_en = remove_class(degree_overview_en)
        # print(degree_overview_en)

        #5.location
        location = response.xpath("//*[contains(text(),'Campus')]//following-sibling::div").extract()
        location = ''.join(location)
        location = remove_tags(location).strip()
        # print(location)

        #6.start_date
        start_date = response.xpath("//*[contains(text(),'Start date')]//following-sibling::*").extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date).strip()
        if 'February, July' in start_date:
            start_date = '2,7'
        elif 'February' in start_date:
            start_date = '2'
        elif 'March,  July,  November' in start_date:
            start_date = '3,7,11'
        # print(start_date)

        #7.duration
        duration = response.xpath("//*[contains(text(),'Duration')]//following-sibling::*").extract()
        duration = ''.join(duration)
        duration = remove_tags(duration).strip().replace('full-time','').strip()
        # print(duration)

        #8.career_en
        career_en = response.xpath('//*[@id="accordion__career"]').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #9.modules_en
        modules_en = response.xpath('//*[@id="accordion__subjects"]/div').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #10.apply_proces_en
        apply_proces_en = response.xpath('//*[@id="accordion__internationalapply"]').extract()
        apply_proces_en = ''.join(apply_proces_en)
        apply_proces_en = remove_class(apply_proces_en)
        # print(apply_proces_en)



        #12.ielts 13141516 17.toefl 18192021
        ielts_list = response.xpath("//*[contains(text(),'Minimum')]/../../following-sibling::*").extract()
        if len(ielts_list)==0:
            ielts_list = response.xpath("//*[contains(text(),'Minimum')]/../following-sibling::*").extract()
        ielts_list = ''.join(ielts_list)
        ielts_list = remove_tags(ielts_list)
        # print(ielts_list)
        if 'Band 2' in ielts_list:
            ielts =6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_l = 6.0
            ielts_s = 6.0
            toefl = 90
            toefl_r = 21
            toefl_w = 21
            toefl_s = 21
            toefl_l = 21
        elif 'Band 3a' in ielts_list:
            ielts = 7.0
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
            ielts_s = 6.5
            toefl = 100
            toefl_r = 23
            toefl_w = 23
            toefl_s = 23
            toefl_l = 23
        elif 'Band 1' in ielts_list:
            ielts = 6.0
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_l = 6.0
            ielts_s = 6.0
            toefl = 79
            toefl_r = 19
            toefl_w = 19
            toefl_s = 19
            toefl_l = 19
        elif 'Band 3c' in ielts_list:
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 7.0
            ielts_s = 7.0
            toefl = 100
            toefl_r = 23
            toefl_w = 23
            toefl_s = 23
            toefl_l = 23
        else:
            ielts = 7.5
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 8.0
            ielts_s = 8.0
            toefl = 100
            toefl_r = 23
            toefl_w = 23
            toefl_s = 23
            toefl_l = 23
        # print(ielts,ielts_r,ielts_w,ielts_l,ielts_s,toefl,toefl_w,toefl_s,toefl_l,toefl_r)

        #22.deadline
        deadline = response.xpath('//*[@id="accordion__internationaldeadlines"]').extract()
        deadline = ''.join(deadline)
        deadline = remove_tags(deadline).strip()
        if '31 January' in deadline and '30 June' in deadline:
            deadline = '2019-1-31,2019-6-30'
        elif '31 October' in deadline:
            deadline = '2018-10-31'
        elif '31 January' in deadline:
            deadline = '2019-1-31'
        elif '15 December' in deadline:
            deadline = '2018-12-15'
        elif '31 December' in deadline:
            deadline = '2018-12-31'
        else:deadline = '2019-1-31,2019-6-30'
        # print(deadline)



        #24.apply_pre
        apply_pre = '$'

        #25，tuition_fee_pre
        tuition_fee_pre = '$'

        #26.rntry_requirements_en
        rntry_requirements_en = response.xpath('//*[@id="accordion__internationalrequirements"]').extract()
        rntry_requirements_en = ''.join(rntry_requirements_en)
        rntry_requirements_en = remove_class(rntry_requirements_en)
        # print(rntry_requirements_en)

        #27.tuition_fee
        tuition_fee = response.xpath('//*[@id="accordion__internationalcosts"]').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        # 11.overview_en
        overview_en = response.xpath('//*[@id="accordion__highlights"]/*').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)


        item['university'] = university
        item['degree_name'] = degree_name
        item['degree_overview_en'] = degree_overview_en
        item['location'] = location
        item['start_date'] = start_date
        item['duration'] = duration
        item['career_en'] = career_en
        item['modules_en'] = modules_en
        item['apply_proces_en'] = apply_proces_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl'] = toefl
        item['toefl_w'] = toefl_w
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['deadline'] = deadline
        item['apply_pre'] = apply_pre
        item['tuition_fee_pre'] = tuition_fee_pre
        item['rntry_requirements_en'] = rntry_requirements_en
        item['tuition_fee'] = tuition_fee

        # 23.programme_en
        programme_en = degree_name.replace('Bachelor of','').strip()
        major = response.xpath('//*[@id="accordion__majors"]/h3').extract()

        if len(major)!=0:
            for i in major:
                programme_en_a = i
                url = response.url
                programme_en_a = programme_en_a.replace('<h3>','').replace('</h3>','').strip()
                data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
                pat = '<h3>'+ programme_en_a +'</h3><p>[a-zA-Z\s,0-9\.’]+</p>'
                overview_en_a = ''.join(re.findall(pat,data))
                item['programme_en'] = programme_en_a
                item['overview_en'] = overview_en_a
                item['url'] = url
                yield item
        else:
            item['programme_en'] = programme_en
            item['overview_en'] = overview_en
            item['url'] = url
            yield item

