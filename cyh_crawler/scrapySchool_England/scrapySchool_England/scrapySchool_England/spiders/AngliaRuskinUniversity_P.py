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
from lxml import etree
import requests
import json

class AngliaruskinuniversityPSpider(scrapy.Spider):
    name = 'AngliaRuskinUniversity_P'
    allowed_domains = ['anglia.ac.uk']
    start_urls=['https://www.anglia.ac.uk/study/course-search?keywords=&levelofstudy=postgraduate&levelofstudy=&location=&modeofstudy=Full-time&faculty=&availability=']
    def parse(self, response):
        # print(response.url)
        pro_url=response.xpath('//h3[@class="listing--common__title"]/a/@href').extract()
        for i in pro_url:
            URL='https://www.anglia.ac.uk'+i
            yield scrapy.Request(url=URL,callback=self.parse_main)
        next_page=response.xpath('//a[contains(text(),"Next")]/@href').extract()
        if next_page!=[]:
            full_url='https://www.anglia.ac.uk'+next_page[0]
            yield scrapy.Request(url=full_url,callback=self.parse)
    def parse_main(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university']='Anglia Ruskin University'
        item['url']=response.url
        item['teach_time']='1'
        programme=response.xpath('//h1/text()').extract()
        programme=''.join(programme).split('\r\n')
        if len(programme)==4:
            prog=programme[1].strip()
            degr=programme[2].strip()
            item['degree_name'] = degr
        else:
            prog=''.join(programme)
        item['programme_en']=prog


        location=response.xpath('//div[@class="course-summary__text"]/p[@class="course-summary__locations"]/a/text()').extract()
        location=set(location)
        # print(location)
        location=','.join(location)
        item['location']=location

        start_date=response.xpath('//div[@class="course-summary__text"]/p[@class="course-summary__entry"]/text()').extract()
        start_date=tracslateDate(start_date)
        # print(start_date)
        start_date=','.join(start_date)
        item['start_date']=start_date

        duration=response.xpath('//div[@class="course-summary__teaching"]/p[1]/text()').extract()
        try:
            duration=clear_duration(duration)
            item['duration']=duration['duration']
            item['duration_per']=duration['duration_per']
        except:
            pass

        overview=response.xpath('//div[@id="overview"]').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en']=overview

        career=response.xpath('//div[@id="careers"]').extract()
        career=remove_class(career)
        # print(career)
        item['career_en']=career

        modules=response.xpath('//div[@id="modulesassessment"]').extract()
        modules=remove_class(modules)
        item['modules_en']=remove_class(modules)

        item['ielts']='6.5'
        item['ielts_l']='5.5'
        item['ielts_s'] = '5.5'
        item['ielts_r'] = '5.5'
        item['ielts_w'] = '5.5'
        item['ielts_desc']='Our standard entry criteria for postgraduate courses is IELTS 6.5 or equivalent, with nothing lower than 5.5 in any of the four elements (listening, speaking, reading and writing).'
        item['toefl']='88'
        item['toefl_l']='17'
        item['toefl_s'] = '20'
        item['toefl_r'] = '18'
        item['toefl_w'] = '17'
        item['toefl_desc']="TOEFL iBT with 88 overall and a minimum of 17 in Writing and Listening, 18 in Reading and 20 in Speaking"

        fee=response.xpath('//div[@id="feesfunding"]//text()').extract()
        tuition_fee=getTuition_fee(fee)
        # print(tuition_fee)
        if tuition_fee==2018:
            tuition_fee=0
        item['tuition_fee']=tuition_fee
        item['tuition_fee_pre']='£'

        department=response.xpath('//a[contains(text(),"Visit your")]/@href').extract()
        # print(department)
        department=''.join(department).split('/')[-1]
        # print(department)
        department=department.title().replace('-',' ')
        # print(department)
        item['department']=department

        how_to_apply=["<p>Step 1 - Choose your course</p>",
"<p>Step 2 - Submit your application form</p>",
"<p>Step 3 - Check your email regularly</p>",
"<p>Step 5 - Start your visa application</p>",
"<p>Step 4 - Receive our decision on your application</p>",]
        how_to_apply='\n'.join(how_to_apply)
        item['apply_proces_en']=how_to_apply

        apply_d=["<ul><li>Qualification certificates and transcripts, including certified translations, where applicable</li>",
"<li>A personal statement. You can download and complete our Personal Statement Form.</li>",
"<li>References/recommendation letters</li>",
"<li>Curriculum vitae/resume</li>",
"<li>Passport</li>",
"<li>Current and previous visa(s) (if applicable)</li>",
"<li>Proof of name change (if applicable)</li>",
"<li>Portfolio (if applicable)</li></ul>",]
        apply_d='\n'.join(apply_d)
        item['apply_documents_en']=apply_d

        courseid=response.xpath('//input[@id="erastracode"]/@value').extract()
        # print(courseid)
        if courseid==['']:
            rntry=response.xpath('//h4[contains(text(),"ain")]/following-sibling::*').extract()
            rntry=remove_class(rntry)
            # print(rntry)
            item['rntry_requirements'] = rntry
        else:
            cid=re.findall('[A-Z0-9]+',courseid[0])
            courseid='%20'.join(cid)
            rntry_url='https://www.anglia.ac.uk/api/coursewidget/multipleentryrequirements?academicYears=2017%2C2018&moaCode=FT&astraCode='+courseid
            # print(rntry_url)
            try:
                rntry_content=json.loads(requests.get(rntry_url).text)[0]['GroupItems'][0]['Text'][0]
                rntry_content='<div>'+rntry_content+'</div>'
            except:
                rntry_content=''

            item['rntry_requirements'] = rntry_content
            # print(rntry_content)
        # yield item