# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/16 11:35'
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
from scrapySchool_England.TranslateMonth import translate_month
from scrapySchool_England.getTuition_fee import getT_fee
class UniversityofSouthWalesSpider(scrapy.Spider):
    name = 'UniversityofSouthWales_p'
    allowed_domains = ['southwales.ac.uk/']
    start_urls = []
    C= [
        'https://www.southwales.ac.uk/courses/llm-laws/',
        'https://www.southwales.ac.uk/courses/ma-animation/',
        'https://www.southwales.ac.uk/courses/ma-drama/',
        'https://www.southwales.ac.uk/courses/ma-arts-practice-art-health-and-wellbeing/',
        'https://www.southwales.ac.uk/courses/ma-documentary-photography/',
        'https://www.southwales.ac.uk/courses/ma-camh-child-and-adolescent-mental-health/',
        'https://www.southwales.ac.uk/courses/ma-arts-practice-fine-art/',
        'https://www.southwales.ac.uk/courses/ma-leadership-management-education/',
        'https://www.southwales.ac.uk/courses/ma-english-by-research/',
        'https://www.southwales.ac.uk/courses/ma-education-innovation-in-learning-and-teaching/',
        'https://www.southwales.ac.uk/courses/ma-history-by-research/',
        'https://www.southwales.ac.uk/courses/ma-graphic-communication/',
        'https://www.southwales.ac.uk/courses/ma-games-enterprise/',
        'https://www.southwales.ac.uk/courses/ma-leadership-in-sport/',
        'https://www.southwales.ac.uk/courses/ma-working-for-children-and-young-people-youth-work-initial-qualifying/',
        'https://www.southwales.ac.uk/courses/ma-senaln-autism/',
        'https://www.southwales.ac.uk/courses/ma-senaln-additional-learning-needs-/',
        'https://www.southwales.ac.uk/courses/ma-tesol-teaching-english-to-speakers-of-other-languages/',
        'https://www.southwales.ac.uk/courses/mba-master-of-business-administration/',
        'https://www.southwales.ac.uk/courses/ma-songwriting-and-production/',
        'https://www.southwales.ac.uk/courses/msc-advanced-performance-football-coaching/',
        'https://www.southwales.ac.uk/courses/msc-aeronautical-engineering/',
        'https://www.southwales.ac.uk/courses/msc-aviation-engineering-and-management/',
        'https://www.southwales.ac.uk/courses/msc-analytical-and-forensic-science/',
        'https://www.southwales.ac.uk/courses/msc-clinical-and-abnormal-psychology/',
        'https://www.southwales.ac.uk/courses/msc-civil-and-structural-engineering/',
        'https://www.southwales.ac.uk/courses/msc-civil-engineering-and-environmental-management/',
        'https://www.southwales.ac.uk/courses/msc-behaviour-analysis-and-therapy/',
        'https://www.southwales.ac.uk/courses/msc-computer-systems-security/',
        'https://www.southwales.ac.uk/courses/msc-computer-forensics/',
        'https://www.southwales.ac.uk/courses/msc-construction-project-management/',
        'https://www.southwales.ac.uk/courses/msc-computing-and-information-systems/',
        'https://www.southwales.ac.uk/courses/msc-data-science/',
        'https://www.southwales.ac.uk/courses/msc-crime-and-justice/',
        'https://www.southwales.ac.uk/courses/msc-cyber-security/',
        'https://www.southwales.ac.uk/courses/msc-engineering-management/',
        'https://www.southwales.ac.uk/courses/msc-electronics-and-information-technology/',
        'https://www.southwales.ac.uk/courses/msc-finance-and-investment/',
        'https://www.southwales.ac.uk/courses/msc-human-resource-management/',
        'https://www.southwales.ac.uk/courses/msc-forensic-audit-and-accounting/',
        'https://www.southwales.ac.uk/courses/msc-health-and-public-service-management/',
        'https://www.southwales.ac.uk/courses/msc-global-governance/',
        'https://www.southwales.ac.uk/courses/msc-hazard-and-disaster-management/',
        'https://www.southwales.ac.uk/courses/msc-international-logistics-and-supply-chain-management/',
        'https://www.southwales.ac.uk/courses/msc-international-business-and-enterprise/',
        'https://www.southwales.ac.uk/courses/msc-marketing/',
        'https://www.southwales.ac.uk/courses/msc-management/',
        'https://www.southwales.ac.uk/courses/msc-mechanical-engineering/',
        'https://www.southwales.ac.uk/courses/msc-mobile-and-satellite-communications-without-internship/',
        'https://www.southwales.ac.uk/courses/msc-music-engineering-and-production/',
        'https://www.southwales.ac.uk/courses/msc-public-relations/',
        'https://www.southwales.ac.uk/courses/msc-professional-accounting-with-acca-tuition/',
        'https://www.southwales.ac.uk/courses/msc-project-management/',
        'https://www.southwales.ac.uk/courses/msc-psychology-by-research/',
        'https://www.southwales.ac.uk/courses/msc-professional-practice/',
        'https://www.southwales.ac.uk/courses/msc-public-health/',
        'https://www.southwales.ac.uk/courses/msc-safety-health-and-environmental-management/',
        'https://www.southwales.ac.uk/courses/msc-specialist-community-public-health-nursing-health-visiting/',
        'https://www.southwales.ac.uk/courses/msc-renewable-energy-and-resource-management/',
        'https://www.southwales.ac.uk/courses/msc-sports-coaching-and-performance/',
        'https://www.southwales.ac.uk/courses/msc-sport-health-and-exercise-science/',
        'https://www.southwales.ac.uk/courses/msc-strategic-digital-marketing/',
        'https://www.southwales.ac.uk/courses/msc-strategic-procurement-management/',
        'https://www.southwales.ac.uk/courses/msc-working-with-adult-and-young-offenders/',
        'https://www.southwales.ac.uk/courses/msc-wildlife-and-conservation-management/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of South Wales'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="uni"]/section[1]/div//h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        degree_name = programme_en.split()[0]
        programme_en = programme_en.replace(degree_name,'').strip()
        # print(degree_name)

        #6.overview_en
        overview_en = response.xpath('//*[@id="uni"]/section[1]/div[2]//p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #7.teach_time #8.duration #9.duration_per #10.start_date
        teach_time_list= response.xpath('//*[@id="2018"]/div/table/tbody/tr[1]').extract()
        teach_time_list = ''.join(teach_time_list)
        teach_time_list = remove_tags(teach_time_list)
        teach_time_list= clear_space_str(teach_time_list)
        # print(teach_time)
        try:
            duration = re.findall('\d+',teach_time_list)[0]
        except:
            duration = 1
        duration_per = 1
        if 'Full-time' in  teach_time_list:
            teach_time = 'Full-time'
        else:
            teach_time = 'Part-time'
        try:
            start_date = translate_month(teach_time_list)
        except:
            start_date = 9
        try:
            if int(start_date)>8:
                start_date = '2018-'+str(start_date)
            else:
                start_date = '2019-'+str(start_date)
        except:
            start_date = '2018-9'
        # print(start_date)
        # print(duration,teach_time,duration_per)

        #11.modules_en
        modules_en = response.xpath('//*[@id="eleven"]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)


        #12.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'Assessment')]//following-sibling::div[1]").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #13.rntry_requirements
        rntry_requirements = response.xpath('//*[@id="odin"]/div').extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        rntry_requirements = clear_space_str(rntry_requirements)
        # print(rntry_requirements)

        #14.career_en
        career_en = response.xpath('//*[@id="careers_panel"]/div').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #15.tuition_fee #16.tuition_fee_pre
        tuition_fee = response.xpath("//*[contains(text(),'Full-time International')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getT_fee(tuition_fee)
        # print(tuition_fee,response.url)
        tuition_fee_pre = '£'

        #17.ielts 18192021
        ielts = 6.5
        ielts_l = 5.5
        ielts_w = 5.5
        ielts_s = 5.5
        ielts_r = 5.5
        #22.apply_pre
        apply_pre = '£'
        item['apply_pre'] =  apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['teach_time'] = teach_time
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['start_date'] = start_date
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['rntry_requirements'] = rntry_requirements
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['ielts_w'] = ielts_w
        yield  item