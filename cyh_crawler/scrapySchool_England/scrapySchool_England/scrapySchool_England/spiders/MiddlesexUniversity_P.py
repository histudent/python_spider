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
class MiddlesexuniversityPSpider(scrapy.Spider):
    name = 'MiddlesexUniversity_P'
    allowed_domains = ['mdx.ac.uk']
    start_urls = ['https://www.mdx.ac.uk/_resources/funnelback/outputs/london-course-finder?collection=mdx-courses&f.Course_level%7CI=Postgraduate%20Taught&query=&start_rank=1']
    start_rank = 1
    def parse(self, response):
        # print(response.url)
        pro_url=response.xpath('//ul[@class="search-results"]/li/h3/a/@href').extract()
        last_page=response.xpath('//a[contains(text(),"Last")]/@href').extract()
        # print(pro_url)
        for i in pro_url:
            yield scrapy.Request(i,callback=self.parse_main)
        # print(last_page)
        num_rank=re.findall('start_rank=\d+',''.join(last_page))
        num_rank=''.join(num_rank).replace('start_rank=','')
        try:
            num_rank=int(num_rank)
        except:
            num_rank=self.start_rank
        # print(num_rank)
        while self.start_rank<num_rank:
            self.start_rank=self.start_rank+10
            next_page='https://www.mdx.ac.uk/_resources/funnelback/outputs/london-course-finder?collection=mdx-courses&f.Course_level%7CI=Postgraduate%20Taught&query=&start_rank='+str(self.start_rank)
            yield scrapy.Request(next_page,callback=self.parse)
    def parse_main(self,response):
        item=get_item1(ScrapyschoolEnglandItem1)
        print(response.url)

        item['university'] = 'Middlesex University'
        item['url'] = response.url
        item['location'] = 'London'

        programme=response.xpath('//div[@class="course-page-banner__texts"]/h1/text()').extract()
        # print(programme)
        programme=''.join(programme)
        degree_name=re.findall('[A-Z]{2,}.*',programme)
        # print(degree_name)
        degree_name=''.join(degree_name)
        if degree_name!=programme:
            programme=programme.replace(degree_name,'')
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


        start_date=response.xpath('//span[contains(text(),"Start")]/../following-sibling::div//text()').extract()
        # print(start_date)
        start_date=tracslateDate(start_date)
        # print(start_date)
        start_date=','.join(start_date)
        item['start_date'] = start_date

        duration=response.xpath('//span[contains(text(),"Duration")]/../following-sibling::div//text()').extract()
        mode=re.findall('(?i)full',''.join(duration))
        duration=clear_duration(duration)
        # print(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']
        if mode !=[]:
            item['teach_time']='1'
        else:
            item['teach_time']='2'

        fee = response.xpath('//span[contains(text(),"Fees")]/../following-sibling::div//text()').extract()
        tuition_fee=getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = '£'

        overview=response.xpath('//h2[contains(text(),"Overview")]/following-sibling::*').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        modules=response.xpath('//h2[contains(text(),"Course content")]/following-sibling::*').extract()
        modules=remove_class(modules)
        # print(modules)
        item['modules_en'] = modules

        rntry=response.xpath('//h2[contains(text(),"Entry requirements")]/following-sibling::*').extract()
        rntry=remove_class(rntry)
        # print(rntry)
        item['rntry_requirements'] = rntry

        ielts=response.xpath('//p[contains(text(),"IELTS")]//text()').extract()
        ielts=''.join(ielts)
        item['ielts_desc']=ielts
        ielts=get_ielts(ielts)
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

        career=response.xpath('//h2[contains(text(),"Careers")]/following-sibling::*').extract()
        career=remove_class(career)
        # print(career)
        item['career_en'] = career

        yield item

