# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re
class DemontfortuniversityUSpider(scrapy.Spider):
    # name = 'DeMontfortUniversity_U'
    # allowed_domains = ['dmu.ac.uk']
    start_urls = ['https://www.dmu.ac.uk/study/courses/undergraduate-courses/undergraduate-courses.aspx']
    rules = (
        Rule(LinkExtractor(
            allow=r'https://www.dmu.ac.uk/study/courses/undergraduate-courses/undergraduate-courses.aspx\?courselisting1_List_GoToPage=\d+'),
            follow=True),
        Rule(LinkExtractor(restrict_xpaths='//td[@class="sys_col-one"]/a'), follow=False, callback='parses'),
    )

    def parses(self, response):
        print('专业链接',response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['university']='De Montfort University'
        item['url']=response.url
        item['location']='Leicester'

        item['degree_name']=response.meta['degree_name']
        item['programme_en']=response.meta['programme'].replace(response.meta['degree_name'],'')

        overview=response.xpath('//div[@class="block large-8 columns course-col2"]').extract()
        overview=remove_class(overview)
        item['overview_en']=overview

        rntry=response.xpath('//div[@class="row row--block course-section course-section--criteria"]').extract()
        rntry=remove_class(rntry)
        item['require_chinese_en']=rntry

        modules=response.xpath('//div[@id="cycle-slideshow_course"]').extract()
        modules=remove_class(modules)
        item['modules_en']=modules

        career = response.xpath('//div[@class="row row--block course-section course-section--opps"]').extract()
        career = remove_class(career)
        item['career_en']=career

        IELTS = response.xpath('//*[contains(text(),"IELTS")]//text()').extract()
        item['ielts_desc']=''.join(IELTS).strip()
        ielts = get_ielts(IELTS)
        try:
            if ielts != {} and ielts != []:
                item['ielts_l'] = float(ielts['IELTS_L'])
                item['ielts_s'] = float(ielts['IELTS_S'])
                item['ielts_r'] = float(ielts['IELTS_R'])
                item['ielts_w'] = float(ielts['IELTS_W'])
                item['ielts'] = float(ielts['IELTS'])
            else:
                item['ielts'] = ''
                item['ielts_l'] = ''
                item['ielts_s'] = ''
                item['ielts_r'] = ''
                item['ielts_w'] = ''
        except:
            pass

        apply_d=["<div>A copy of your qualifications",
"A copy of your English language certificate  ",
"A photocopy of your passport",
"1 reference</div>",]
        apply_d='\n'.join(apply_d)
        item['apply_documents_en']=apply_d

        tuition_fee = response.xpath('//*[contains(text(),"£")]//text()').extract()
        tuition_fee = getTuition_fee(tuition_fee)
        item['tuition_fee']=tuition_fee

        duration=response.xpath('//*[contains(text(),"uration")]/..//text()').extract()
        try:
            duration=clear_duration(duration)
        except:
            duration={'duration_per': None, 'duration': None}
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']

        ib=response.xpath('//li[contains(text(),"International Baccalaureate")]/text()').extract()
        ib=''.join(ib).strip()
        item['ib']=ib

        alevel=response.xpath('//li[contains(text(),"A-level")]/text()').extract()
        alevel=''.join(alevel).strip()
        item['alevel']=alevel

        ucascode=response.xpath('//b[contains(text(),"UCAS")]/../text()').extract()
        if ucascode==[]:
            print(response.url)
        else:
            print(ucascode)

        # yield item
        # print(item)