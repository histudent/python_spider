# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/11 15:31'
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
from scrapySchool_England.clearSpace import  clear_space_str
from scrapySchool_England.translate_date import  tracslateDate
from scrapySchool_England.translate_date import tracslateDate
class UniversityofEastAngliaSpider(scrapy.Spider):
    name = 'UniversityofEastAnglia_p'
    allowed_domains = ['uea.ac.uk/']
    start_urls = []
    C = [
        'https://www.uea.ac.uk/norwich-business-school/mba-programme/full-time'
    ]

    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of East Anglia'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        # programme_en_list = response.xpath('//*[@id="course-title"]/div/div/div/h1').extract()
        # programme_en_list = ''.join(programme_en_list)
        # programme_en_list = remove_tags(programme_en_list)
        # # programme_en_list2 = programme_en_list.split()[0]
        # a = re.findall(r'[A-Za-z]',programme_en_list2)[0]
        # if a =='M':
        #     programme_en = programme_en_list.split()[1:]
        #     programme_en = ' '.join(programme_en).strip()
        # elif a =='L':
        #     programme_en = programme_en_list.split()[1:]
        #     programme_en = ' '.join(programme_en).strip()
        # elif a =='P':
        #     programme_en = programme_en_list.split()[1:]
        #     programme_en = ' '.join(programme_en).strip()
        # else:programme_en = programme_en_list
        # print(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type=2

        #5.degree_name
        degree_name = response.xpath('//*[@id="course-spec-left"]/dd[2]').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # programme_en = programme_en.replace(degree_name,'').strip()
        # print(degree_name)

        #6.teach_time
        teach_time = response.xpath('//*[@id="course-spec-left"]/dd[1]').extract()
        teach_time = ''.join(teach_time)
        teach_time = remove_tags(teach_time)
        # print(teach_time)

        #7.department
        department = response.xpath('//*[@id="faculty-and-school"]/li[1]/a').extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #8.overview_en
        overview_en = response.xpath('//*[@id="course-about"]/div/div[2]').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #9.modules_en
        modules_en = response.xpath('//*[@id="course-profile-modules"]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #10.rntry_requirements
        rntry_requirements = response.xpath('//*[@id="course-entry-requirements"]').extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #11.ielts 12131415
        ielts = response.xpath('//*[@id="course-entry-requirements"]/ul[2]/li[1]').extract()
        ielts = ''.join(ielts)
        ielts = remove_tags(ielts)
        # print(ielts)
        try:
            ielts = re.findall('\d\.\d',ielts)
        except:
            ielts = None
        if len(ielts)>1:
            a=ielts[0]
            b=ielts[1]
            ielts = a
            ielts_w = b
            ielts_r = b
            ielts_s = b
            ielts_l = b
        else:
            ielts = 6.5
            ielts_w = 6.0
            ielts_r = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
        # print(ielts,ielts_r,ielts_w,ielts_s,ielts_l)

        #16.teach_type
        teach_type = 'taught'

        #17.tuition_fee
        tuition_fee = response.xpath('//*[@id="course-fees-and-funding"]/ul/li[2]').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        if tuition_fee ==0:
            tuition_fee =15800
        # print(tuition_fee)

        #18.tuition_fee_pre
        tuition_fee_pre = '£'

        #19.apply_proces_en
        apply_proces_en = 'http://www.uea.ac.uk/study/postgraduate/apply'

        #20.location
        location = 'Norwich'

        #21.apply_pre
        apply_pre = '£'

        #22.assessment_en
        assessment_en = response.xpath("//h4[contains(text(),'ssessment')]//following-sibling::div").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #23.career_en
        career_en = response.xpath("//h4[contains(text(),'areer')]//following-sibling::div").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #24.require_chinese_en
        require_chinese_en = '<p>Holders of a Bachelor Degree from a recognised university will be considered for entry to graduate study.</p>'

        item['require_chinese_en'] = require_chinese_en
        item['career_en'] = career_en
        item['assessment_en'] = assessment_en
        item['teach_time'] = teach_time
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        # item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['department'] = department
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['rntry_requirements'] = rntry_requirements
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['teach_type'] = teach_type
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_proces_en'] = apply_proces_en
        item['location'] = location
        # yield item