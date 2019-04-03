# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
from scrapySchool_England_U.middlewares import *

class BuckinghamshirenewuniversityUSpider(scrapy.Spider):
    name = 'BuckinghamshireNewUniversity_U'
    # allowed_domains = ['a.b']
    # start_urls = ['https://bucks.ac.uk/ugcourses']
    def parse(self, response):
        # print('获取到一个列表页',response.url)
        pro_url=response.xpath('//h4/strong/a/@href').extract()
        for i in pro_url:
            if '-pt' in i:
                print('跳过一个兼职链接',i)
            else:
                print('抓取',i)
                yield scrapy.Request(i,callback=self.parses)
        next_page=response.xpath('//a[contains(text(),"Next")]/@href').extract()
        if next_page!=[]:
            next_url=next_page[0]
            yield scrapy.Request(next_url,callback=self.parse)
    #补抓课程设置
    # def parses(self, response):
    #     item=get_item1(ScrapyschoolEnglandItem)
    #     item['url']=response.url
    #     item['university']='Buckinghamshire New University'
    #     modules=response.xpath('//h2[text()="Course Modules"]/following-sibling::*').extract()
    #     if modules==[]:
    #         print(response.url)
    #     else:
    #         print(modules)
    #     modules=remove_class(modules)
    #     item['modules_en']=modules
    #     yield item
    def parses(self,response):
        # print(response.url)
        # print('进入专业链接页面')
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.url
        item['university']='Buckinghamshire New University'
        location=response.xpath('//ul[@class="course-details"]/li[contains(text(),"Location")]/text()').extract()
        location=''.join(location).replace('Location:','').strip()
        # print(location)
        programme=response.xpath('//h1[@class="banner-title"]/text()').extract()
        item['programme_en']=''.join(programme).strip()
        degree_name=response.xpath('//p[@class="school-code"]/text()').extract()
        item['degree_name']=''.join(degree_name).strip()
        item['location']=location
        duration=response.xpath('//ul[@class="course-details"]/li[contains(text(),"Duration")]/text()').extract()
        duration=clear_duration(duration)
        # print(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']
        start_date=response.xpath('//ul[@class="course-details"]/li[contains(text(),"Start Date")]/text()').extract()
        start_date=tracslateDate(start_date)
        # print(start_date)
        start_date=','.join(start_date).strip()
        item['start_date']=start_date
        ucascode=response.xpath('//h3[contains(text(),"UCAS CODE")]/text()').extract()
        ucascode=''.join(ucascode).replace('UCAS CODE:','').strip()
        # print(ucascode)
        # if ucascode=='':
        #     print('异常专业链接',response.url)
        item['ucascode']=ucascode
        overview=response.xpath('//h2[contains(text(),"Course Overview")]/..').extract()
        item['overview_en']=remove_class(overview)
        modules=response.xpath('//h2[contains(text(),"Course Modules")]/..').extract()
        item['modules_en']=remove_class(modules)
        career=response.xpath('//h2[contains(text(),"Employability")]/..').extract()
        item['career_en']=remove_class(career)
        entry=response.xpath('//h3[contains(text(),"What are the course entry requirements?")]/following-sibling::p').extract()
        # item['r']
        alevel=response.xpath('//p[contains(text(),"A Level")]//text()|//p[contains(text(),"A-level")]//text()').extract()
        item['alevel']=remove_class(alevel)
        fee=response.xpath('//p[contains(text(),"Full Time International: ")]/span/text()').extract()
        if fee!=[]:
            item['tuition_fee']='11000'
        else:
            item['tuition_fee']='10500'
        chi=['<div>  ',
' <p>Academic entry requirements</p ><p>We require successful completion of 高中毕业证书 (Senior Middle School 3) with a minimum average of 60% and a recognised foundation programme.</p ><p>If you do not meet these requirements you may be eligible to study our foundation programme. Please send copies of your qualifications directly to us at < a>admissions@bucks.ac.uk</ a>.</p ><p>Mathematics entry Requirements</p ><p>Students need the equivalent of GCSE Mathematics grade C/4.</p >  ',
' </div>  ',]
        item['require_chinese_en']=remove_class(chi)
        item['ielts']='6.0'
        item['ielts_l']='5.5'
        item['ielts_s'] = '5.5'
        item['ielts_r'] = '5.5'
        item['ielts_w'] = '5.5'

        assessment=response.xpath('//strong[contains(text(),"Assessment")]/../following-sibling::p[position()<=5]').extract()
        if assessment==[]:
            print(response.url)
        else:
            print('GG')
        item['assessment_en']=remove_class(assessment)
        yield item
        # print(item)