# -*- coding: utf-8 -*-
import scrapy
import requests
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.clearSpace import clear_same_s
from scrapySchool_England.middlewares import clear_duration,tracslateDate
class LondonsouthbankuniversityPSpider(scrapy.Spider):
    name = 'LondonSouthBankUniversity_P'
    allowed_domains = ['lsbu.ac.uk']
    start_urls = ['http://www.lsbu.ac.uk/courses/course-finder']
    def parse(self, response):
        pro_url=response.xpath('//span[contains(text(),"View")]/../@href').extract()
        for i in pro_url:
            urls=requests.get(i)
            yield scrapy.Request(urls.url,callback=self.pro_parse)
        next_page=response.xpath('//span[@class="link_next_page"]/a/@href').extract()
        if len(next_page)==1:
            yield scrapy.Request(next_page[0],callback=self.parse)
    def pro_parse(self,response):
        item=get_item1(ScrapyschoolEnglandItem1)
        print(response.url)
        item['url'] = response.url
        item['university'] = 'London South Bank University'
        item['location'] = 'London'
        item['tuition_fee_pre'] = '£'
        pro=response.xpath('//div[@id="breadcrumbs"]//span/text()').extract()
        prog=pro[-1].split('-')
        if len(prog)==2:
            programme=prog[0]
            degree_type=prog[1]
            degree_type=degree_type.strip()
            item['degree_name'] = degree_type
            if degree_type[0]=='M':
                item['degree_type'] ='2'
            elif degree_type[0]=='P':
                item['degree_type'] ='3'
        else:
            programme=prog
        item['programme_en'] = programme
        fee=response.xpath('//div[@id="tab_fees_and_funding"]//*[contains(text(),"£")]//text()').extract()
        # print(fee)
        tuition_fee=getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee

        overview=response.xpath('//div[@id="tab_overview"]').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        modules=response.xpath('//div[@id="tab_modules"]').extract()
        modules=remove_class(modules)
        # print(modules)
        item['modules_en'] = modules

        career=response.xpath('//div[@id="tab_employability"]').extract()
        career=remove_class(career)
        item['career_en'] = career

        rntry=response.xpath('//div[@id="tab_entry_requirements"]').extract()
        rntry=remove_class(rntry)
        item['rntry_requirements'] = rntry

        ielts=get_ielts(rntry)
        # print(ielts)
        if ielts!=[] and ielts!={}:
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            item['ielts'] = ielts['IELTS']

        apply_desc_en=response.xpath('//div[@id="tab_how_to_apply"]').extract()
        apply_desc_en=remove_class(apply_desc_en)
        item['apply_desc_en'] = apply_desc_en

        duration=response.xpath('//td/span[contains(text(),"Duration")]/following-sibling::div/text()').extract()
        duration=clear_duration(duration)
        # print(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']

        mode=response.xpath('//td/span[contains(text(),"Mode")]/following-sibling::div/text()').extract()
        mode=set(mode)
        mode=''.join(mode)
        # print(mode)
        mode=re.findall('(?i)full',mode)
        if mode != []:
            item['teach_time'] = '1'
        else:
            item['teach_time'] = '2'
        start_date=response.xpath('//td/span[contains(text(),"Start")]/following-sibling::div/text()').extract()
        # start_date=tracslateDate(start_date)
        # start_date=set(start_date)
        try:
            start_date=tracslateDate(start_date)
            start_date=list(set(start_date))
            start_list=[]
            for i in start_date:
                start_list.append('2019'+'-'+i)
            start_date=','.join(start_list)
            item['start_date'] = start_date
        except:
            pass

        item['department'] = ''.join(response.xpath('//a[contains(text(),"School of")]/text()').extract())
        yield item