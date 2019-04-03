# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.middlewares import clear_duration,tracslateDate
from scrapySchool_England.clearSpace import clear_lianxu_space,clear_same_s

class LeedstrinityuniversityPSpider(scrapy.Spider):
    name = 'LeedsTrinityUniversity_P'
    allowed_domains = ['leedstrinity.ac.uk']
    start_urls = []
    pro_url=["/PG/18/203",
"/PG/18/221",
"/PG/18/137",
"/PG/18/223",
"/PG/18/139",
"/PG/18/110",
"/PG/18/215",
"/PG/18/N1X1",
"/PG/18/2LYD",
"/PG/18/Q3X1",
"/PG/18/2TPG",
"/PG/18/V1X1",
"/PG/18/G1X1",
"/PG/18/R1X1 (French) R2X1 (German) R4X1 (Spanish)",
"/PG/18/2VLT",
"/PG/18/X104",
"/PG/18/V6X1",
"/PG/18/2NLP",
"/PG/18/2CCQ",
"/PG/18/2CCR",
"/PG/18/217",
"/PG/18/219",
"/PG/18/112",]
    for i in pro_url:
        fullURL='http://www.leedstrinity.ac.uk/Courses'+i
        start_urls.append(fullURL)
    def parse(self, response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        item['location']='Leeds'
        item['university']='Leeds Trinity University'
        item['url']=response.url
        # item['start_date']='2019-8'
        # item['application_open_date']='2019-7'
        programme=response.xpath('//h1[@class="course-title"]/text()').extract()
        programme=''.join(programme).strip()
        degree_name=response.xpath('//h2[@class="course-title"]/text()').extract()
        degree_name=''.join(degree_name).strip()
        item['degree_type']='2'
        item['programme_en']=programme
        item['degree_name']=degree_name
        # print(programme)
        # print(degree_name)

        overview=response.xpath('//h2/a[contains(text(),"Overview")]/../following-sibling::*').extract()
        overview=remove_class(overview)
        item['overview_en']=overview
        # print(overview)
        duration=response.xpath('//div[contains(text(),"Course type")]/span/text()').extract()
        duration=clear_duration(duration)
        # print(duration
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']

        modules=response.xpath('//div[contains(@class,"structure")]').extract()
        modules=remove_class(modules)
        # print(modules)
        item['modules_en']=modules

        fee=response.xpath('//div[contains(@class,"fees")]//text()').extract()
        tuition_fee=getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee']=tuition_fee
        item['tuition_fee_pre']='£'

        rntry=response.xpath('//div[contains(@class,"entry")]').extract()
        ielts=get_ielts(rntry)
        rntry=remove_class(rntry)
        # print(rntry)
        item['rntry_requirements']=rntry
        # print(ielts)
        try:
            if ielts!=[] or ielts!={}:
                item['ielts_l']=ielts['IELTS_L']
                item['ielts_s'] = ielts['IELTS_S']
                item['ielts_r'] = ielts['IELTS_R']
                item['ielts_w'] = ielts['IELTS_W']
                item['ielts'] = ielts['IELTS']
        except:
            pass

        career=response.xpath('//div[contains(@class,"graduate")]').extract()
        career=remove_class(career)
        # print(career)
        item['career_en']=career

        apply_p=["Choose a course and check its entry requirements using our course finder. You can find out more about us and your chosen course by coming to an Open Day.",
"Apply for your chosen course by downloading the relevant application form below. Complete the application form and return it, along with your references (if they’re required) to the Admissions team at admissions@leedstrinity.ac.uk or by post to: Admissions Team, Leeds Trinity University, Horsforth, Leeds, LS18 5HD",
"The Admissions team will acknowledge receipt of your application by email, process your application and forward it to the relevant Programme Leader within three days of receipt.",
"The Programme Leader will review your application and either make a decision based on your application or invite you to attend an Interview Day at Leeds Trinity University. Those selected for an interview will be contacted with the details of the interview within ten days of your application being processed.",
"The Admissions team will notify you of your interview outcome in writing within five working days of receiving a decision from the Programme Leader.",
"Made an offer? You should reply to accept or decline your offer at admissions@leedstrinity.ac.uk. If you accept, you’ll need to prove that you satisfy the conditions outlined in your offer letter, usually by presenting the relevant supporting documentation in person to Leeds Trinity University, Student Administration Office (AM36).",]
        apply_p='<ul><li>'+'</li><li>'.join(apply_p)+'</li></ul>'
        item['apply_proces_en']=apply_p

        # print(item)
        yield item
