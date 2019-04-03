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

class LiverpooljohnmooresuniversityPSpider(scrapy.Spider):
    name = 'LiverpoolJohnMooresUniversity_P'
    allowed_domains = ['ljmu.ac.uk']
    start_urls = ['https://www.ljmu.ac.uk/courses/searchresults?terms=&EntryYears=2019&CourseTypes=postgraduate&CourseTypes=pgt&CourseTypes=pgde&CourseTypes=pgr&PageSize=10&Searching=True&page=1&_=1531276935313']
    def parse(self, response):
        # print(response.url)
        pro_url=response.xpath('//a[contains(text(),"Find out more")]/@href').extract()
        for i in pro_url:
            fullurl='https://www.ljmu.ac.uk'+i
            yield scrapy.Request(url=fullurl,callback=self.parse_main)
        next_page=response.xpath('//span[contains(text(),"Next Page")]/../@href').extract()
        # print(next_page)
        if next_page!=[]:
            full_url='https://www.ljmu.ac.uk/courses/searchresults'+''.join(next_page)
            yield scrapy.Request(url=full_url,callback=self.parse)
    def parse_main(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university']='Liverpool John Moores University'
        item['url']=response.url
        item['location']='Liverpool'

        programme=response.xpath('//h1/text()').extract()
        programme=''.join(programme).strip()
        degree_name=response.xpath('//h3[contains(text(),"Course type")]/following-sibling::div/p/strong/text()').extract()
        degree_name='/'.join(degree_name).strip()
        # print(programme)
        # print(degree_name)
        item['programme_en'] = programme
        item['degree_name'] = degree_name
        try:
            if degree_name[0] == 'M':
                item['degree_type'] = '2'
            elif degree_name[0] == 'P':
                item['degree_type'] = '3'
        except:
            pass

        fee=response.xpath('//td[contains(text(),"International")]/following-sibling::td/text()').extract()
        # print(fee)
        tuition_fee=getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee']=tuition_fee
        item['tuition_fee_pre']='£'

        department=response.xpath('//h3[contains(text(),"School")]/following-sibling::div/p/text()').extract()
        department=''.join(department)
        # print(department)
        item['department']=department

        mode=response.xpath('//h3[contains(text(),"Study")]/following-sibling::div/p/text()').extract()
        mode=''.join(mode)
        mode=re.findall('(?i)full',mode)
        if mode!=[]:
            item['teach_time']='1'
        else:
            item['teach_time']='2'

        overview=response.xpath('//section[@id="course-overview"]').extract()
        overview=remove_class(overview)
        item['overview_en']=overview

        modules=response.xpath('//section[@id="course-outline"]').extract()
        modules=remove_class(modules)
        item['modules_en']=modules

        rntry=response.xpath('//section[@id="course-process"]').extract()
        rntry=remove_class(rntry)
        item['rntry_requirements']=rntry
        # print(rntry)

        career=response.xpath('//section[@id="course-employment"]').extract()
        career=remove_class(career)
        item['career_en'] = career
        # print(career)

        ielts=response.xpath('//section[@id="course-process"]//p[contains(text(),"IELTS")]/text()').extract()
        ielts=''.join(ielts)
        item['ielts_desc']=ielts
        ielts=get_ielts(ielts)
        try:
            if ielts!=[] or ielts!={}:
                item['ielts_l']=ielts['IELTS_L']
                item['ielts_s'] = ielts['IELTS_S']
                item['ielts_r'] = ielts['IELTS_R']
                item['ielts_w'] = ielts['IELTS_W']
                item['ielts'] = ielts['IELTS']
        except:
            pass

        print(item)
        # yield item