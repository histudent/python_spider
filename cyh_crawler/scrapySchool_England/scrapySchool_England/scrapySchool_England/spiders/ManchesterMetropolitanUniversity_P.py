# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.clearSpace import clear_same_s
from scrapySchool_England.middlewares import clear_duration,tracslateDate
class ManchestermetropolitanuniversityPSpider(scrapy.Spider):
    name = 'ManchesterMetropolitanUniversity_P'
    allowed_domains = ['mmu.ac.uk']
    def parse(self, response):
        list_url=response.xpath('//ul[@class="atoz--listing course--atoz"]/li/a/@href').extract()
        for i in list_url:
            # print(i)
            urls='https://www2.mmu.ac.uk/study/postgraduate/taught/atoz/'+i
            yield scrapy.Request(urls,callback=self.parse_2)
    def parse_2(self,response):
        # print(response.url)
        # print('获取到一个列表页')
        # pro_list=response.xpath('//p[contains(text(),"Full Time")]/../@href').extract()
        pro_list=response.xpath('//li[@class="listing--results__item"]/a/@href').extract()
        # pro_list=response.xpath('//ul[@class="listing listing--results course--listing"]/li/a/@href').extract()
        for j in pro_list:
            full_urls='https://www2.mmu.ac.uk'+j
            # print('传递了')
            print(full_urls)
            yield scrapy.Request(full_urls,callback=self.parses)
    # start_urls=[]
    # for i in start_urls:
    #     if 'pgcert-'not in i and 'pgce-' not in i:
    #         start_urls.append(i)
    # def parsess(self, response):
    #     # pro_list = response.xpath('//li[@class="listing--results__item"]/a/@href').extract()
    #     yield scrapy.Request(response.url,callback=self.parses, errback=self.parse_error_url)
    # def parse_error_url(self, response):
    #     print("*******************")
    #     with open("errorurl.txt", 'a+') as f:
    #         f.write(response.url+"\n")
    def parses(self, response):
       item=get_item1(ScrapyschoolEnglandItem1)
       # print('接受了')
       print('开始下载',response.url,'的数据')
       # print(response.status)
       item['university'] = 'Manchester Metropolitan University'
       item['url'] = response.url
       item['location'] = 'Manchester'
       degree_name=response.xpath('//h1/span/text()').extract()
       degree_name=''.join(degree_name)
       item['degree_name'] = degree_name
       programme=response.xpath('//h1/text()').extract()
       # print(programme)
       programme=''.join(programme).strip()
       item['programme_en'] = programme
       # print(degree_name)
       # print(programme)
       item['degree_type']=2
       overview=response.xpath('//h2[contains(text(),"Overview")]/following-sibling::article').extract()
       overview=remove_class(overview)
       # print(overview)
       item['overview_en'] = overview

       career=response.xpath('//h2[contains(text(),"Career")]/following-sibling::p').extract()
       career=remove_class(career)
       item['career_en'] = career

       rntry=response.xpath('//h2[contains(text(),"Entry")]/following-sibling::p').extract()
       ieltssss=re.findall('\d\.?\d?',''.join(rntry))
       print(ieltssss)
       rntry=remove_class(rntry)
       item['rntry_requirements'] = rntry

       modules=response.xpath('//h2[contains(text(),"Course")]/following-sibling::div').extract()
       modules=remove_class(modules)
       item['modules_en'] = modules

       fee=response.xpath('//*[contains(text(),"£")]//text()').extract()
       tuition=getTuition_fee(fee)
       # print(tuition)
       item['tuition_fee'] = tuition
       item['tuition_fee_pre'] = '£'

       item['ielts_l'] = '5.5'
       item['ielts_s'] = '5.5'
       item['ielts_r'] = '5.5'
       item['ielts_w'] = '5.5'
       item['ielts'] = '6.5'
       item['ielts_desc'] = 'For Postgraduate courses, we usually ask for IELTS 6.5 (No less than 5.5 in any section) or equivalent.'

       item['toefl_desc'] = 'Overall score: 89 With no individual test score below: Listening: 17 Reading: 18 Speaking: 20 Writing : 17'
       item['toefl'] = '89'
       item['toefl_l']='17'
       item['toefl_s']='20'
       item['toefl_r']='18'
       item['toefl_w']='17'

       turation=response.xpath('//li[contains(text(),"Length")]/span//text()').extract()
       duration=clear_duration(turation)
       item['duration'] = duration['duration']
       item['duration_per'] = duration['duration_per']
       ieltsopen=response.xpath('//*[contains(text(),"IELTS")]//text()').extract()
       # print(ieltsopen)
       start_date=response.xpath('//li[contains(text(),"Start")]/span//text()').extract()
       start_date=tracslateDate(start_date)
       start_date=','.join(start_date)
       item['start_date'] = start_date
       item['department'] = ''.join(response.xpath('//span[@id="department_name"]/text()').extract()).strip()
       if response.status == 404:
           print("****404****")
           with open("errorurl.txt", 'a+') as f:
               f.write(response.url + "\n")
       else:
           yield item