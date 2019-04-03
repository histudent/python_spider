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

class NorwichuniversityoftheartsPSpider(scrapy.Spider):
    name = 'NorwichUniversityoftheArts_P'
    allowed_domains = ['nua.ac.uk']
    start_urls = ['https://www.nua.ac.uk/study-at-nua/courses/']
    def parse(self, response):
        pro_url=response.xpath('//div[@id="postgraduate"]//ul//a/@href').extract()
        # print(pro_url)
        for i in pro_url:
            yield scrapy.Request(url=i,callback=self.parse_main)
    def parse_main(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university']='Norwich University of the Arts'
        item['url'] = response.url
        item['location'] ='Norfolk'
        programme=response.xpath('//span[contains(text(),"Course")]/../../following-sibling::span/span/text()').extract()
        programme=set(programme)
        programme=''.join(programme).strip()
        # print(programme)
        degree_name=re.findall('[A-Z]{2,}',programme)
        degree_name=''.join(degree_name).strip()
        programme=programme.replace(degree_name,'').strip()
        item['programme_en']=programme
        item['degree_name'] =degree_name
        try:
            if degree_name[0] == 'M':
                item['degree_type'] = '2'
            elif degree_name[0] == 'P':
                item['degree_type'] = '3'
        except:
            pass

        duration=response.xpath('//strong[contains(text(),"Course length")]/../text()').extract()
        mode=re.findall('(?i)full',''.join(duration))
        duration=clear_duration(duration)
        # print(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']
        if mode!=[]:
            item['teach_time']='1'
        else:
            item['teach_time']='2'

        overview=response.xpath('//strong[contains(text(),"Course length")]/../../following-sibling::*').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en']=overview

        career=response.xpath('//h3[contains(text(),"career")]/following-sibling::ul').extract()
        career=remove_class(career)
        item['career_en']=career

        item['ielts_desc']="BA and MA applicants are required to have a minimum UKVI approved IELTS exam score of 6.0 overall, with a minimum of 5.5 in each section"
        item['ielts_l']='5.5'
        item['ielts_s']='5.5'
        item['ielts_r']='5.5'
        item['ielts_w']='5.5'
        item['ielts']='6.0'

        rntry=response.xpath('//div[@id="entry-requirements"]').extract()
        rntry=remove_class(rntry)
        # print(rntry)
        item['rntry_requirements'] = rntry

        portfolio_desc_en=response.xpath('//div[@id="portfolio-guidance"]').extract()
        portfolio_desc_en=remove_class(portfolio_desc_en)
        # print(portfolio_desc_en)
        item['apply_proces_en']=portfolio_desc_en

        fee=response.xpath('//div[@id="fees-funding"]//text()').extract()
        tuition_fee=getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee']=tuition_fee
        item['tuition_fee_pre']='£'

        how_to_apply=response.xpath('//div[@id="how-to-apply"]').extract()
        item['apply_proces_en']=remove_class(how_to_apply)

        yield item


