# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
from scrapySchool_England_U.middlewares import *

class CityuniversityoflondonUSpider(scrapy.Spider):
    name = 'CityUniversityOfLondon_U'
    # allowed_domains = ['city.ac.uk']
    start_urls = ['https://www.city.ac.uk/courses/postgraduate/english?dm_i=1J82,620XU,TYHWJF,NRG0M,1']

    #补抓
    # def parse(self, response):
    #     item=get_item1(ScrapyschoolEnglandItem)
    #     item['university'] = "City, University of London"
    #     item['url'] = response.url
    #     assessment=response.xpath('//h3[contains(text(),"Assessment methods")]/following-sibling::*|//h2[contains(text(),"Assessment")]/following-sibling::*').extract()
    #     item['assessment_en']=remove_class(assessment)
    #     yield item
    #正式
    def parses(self, response):
        # print(response.url)
        url_list = response.xpath(
            '//h2/a/@href').extract()
        programme = response.xpath(
            '//h2/a/text()').extract()
        degree_name = response.xpath('//h2/following-sibling::div/text()').extract()
        ucascode=response.xpath('//span[contains(text(),"Course")]/following-sibling::span[1]/text()').extract()
        duration=response.xpath('//div[contains(@class,"duration")]/div/span[2]//text()').extract()
        for url, pro, deg ,ucascode,dura in zip(url_list, programme, degree_name,ucascode,duration):
            department_xpath = '//a[contains(text(),"' + pro + '")]/../../../following-sibling::div//span[@class="fa fa-building-o"]/following-sibling::div//text()'
            department = response.xpath(department_xpath).extract()
            # print(url,pro,deg,department)
            yield scrapy.Request(url, meta={'programme': pro, 'duration':dura,'degree_name': deg, 'department': department,'ucascode':ucascode},
                                 callback=self.parse_main)
        next_page = response.xpath('//a[@class="after enabled"]/@href').extract()
        # print(next_page)
        if len(next_page) == 2:
            next_page_url = 'https://www.city.ac.uk/courses' + next_page[0]
            yield scrapy.Request(next_page_url, callback=self.parse)
    def parse(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = "City, University of London"
        item['url'] = response.url
        item['location'] = 'London'
        # item['programme_en'] = response.meta['programme']
        # item['degree_name'] = response.meta['degree_name']
        item['tuition_fee_pre'] = '£'

        # department = response.meta['department']
        # department = set(department)
        # department = ' '.join(department)
        # item['department'] = department

        fee = response.xpath('//h3[contains(text(),"Fee")]/../../following-sibling::div//text()').extract()
        tuition_fee = getTuition_fee(fee)
        if tuition_fee == 0:
            fee = response.xpath('//span[contains(text(),"£")]//text()').extract()
            tuition_fee = getTuition_fee(fee)
        item['tuition_fee'] = tuition_fee
        # print(item['tuition_fee'])

        overview = response.xpath('//h2[contains(text(),"Who is it")]/following-sibling::*|'
                                  '//h2[contains(text(),"Overview")]/following-sibling::*').extract()
        overview = remove_class(overview)
        overview = clear_same_s(overview)
        # print(overview)
        item['overview_en'] = overview

        modules = response.xpath('//h2[contains(text(),"Structure")]/following-sibling::*|'
                                 '//h2[contains(text(),"Modules")]/following-sibling::*').extract()
        modules = remove_class(modules)
        modules = clear_same_s(modules)
        # print(modules)
        item['modules_en'] = modules

        rntry_requirement = response.xpath(
            '//h3[contains(text(),"Entry")]/following-sibling::*|//div[@id="entryreq"]').extract()
        rntry_requirement = remove_class(rntry_requirement)
        rntry_requirement = clear_same_s(rntry_requirement)
        # print(rntry_requirement)
        item['require_chinese_en'] = rntry_requirement

        ielts = response.xpath('//*[contains(text(),"IELTS")]//text()|//*[contains(text(),"IELTS")]/../text()').extract()
        ielts = get_ielts(ielts)
        # print(ielts)
        if ielts != {} and ielts != []:
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            item['ielts'] = ielts['IELTS']

        career = response.xpath('//h2[contains(text(),"Career")]/following-sibling::*').extract()
        # print(career)
        career = remove_class(career)
        career = clear_same_s(career)
        item['career_en'] = career
        # print(career)

        # duration = response.xpath('//span[contains(text(),"Duration")]/../following-sibling::div//text()|'
        #                           '//h3[contains(text(),"Duration")]/following-sibling::*//text()').extract()
        # if duration==[]:
        # duration=response.meta['duration'].replace('Three','3').replace('Four','4').replace('five','5').replace('three','3')
        # duration=response.meta['duration']
        # dura=re.findall('\d',''.join(duration))
        # ucas=re.findall('[A-Z0-9]{4}',response.meta['ucascode'])
        # item['duration']=duration
        # duration = clear_duration(duration)
        # item['duration_per'] = duration['duration_per']
        # for i in ucas:
        #     item['ucascode']=i
        #     yield item

        yield item