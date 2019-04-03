# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem

class BirkbeckuniversityoflondonUSpider(scrapy.Spider):
    name = 'BirkbeckUniversityOfLondon_U'
    # allowed_domains = ['a.b']
    start_urls = ['http://www.bbk.ac.uk/study/2019/undergraduate/']
    def parse(self, response):
        pro_list=response.xpath('//h2[contains(text(),"ubject")]/following-sibling::ol/li/ol/li/a/@href').extract()
        pro_list=list(set(pro_list))
        for i in pro_list:
            yield scrapy.Request(i,callback=self.pro_area)
    def pro_area(self,response):
        pro_url=response.xpath('//h1/following-sibling::ol[1]/li/a/@href').extract()
        for j in pro_url:
            yield scrapy.Request(j,callback=self.programme)
    def programme(self,response):
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        programme=response.xpath('//h1/text()').extract()
        # print(programme)
        deg=re.findall('\(.*\)',''.join(programme))
        clears=re.findall(':.*',''.join(programme))
        # print(deg)
        deg=''.join(deg)
        programme=''.join(programme).replace(''.join(clears),'').replace(deg,'').strip()
        # print(programme)
        item['programme_en']=programme
        item['degree_name']=deg.replace('(','').replace(')','').strip()
        item['url']=response.url
        start_date=response.xpath('//dt[contains(text(),"tart date")]/following-sibling::dd[1]//text()').extract()
        start_date=tracslateDate(start_date)
        item['start_date']=','.join(start_date)
        item['university']='Birkbeck, University of London'
        # item['tuition_fee_pre']='£'
        item['location']=''.join(response.xpath('//dt[contains(text(),"ocation")]/following-sibling::dd[1]//text()').extract())
        duration=response.xpath('//dt[contains(text(),"uration")]/following-sibling::dd[1]//text()').extract()
        # print(duration)
        mode=re.findall('(?i)full',''.join(duration))

        dura=re.findall('[a-zA-Z0-9\s]+full',''.join(duration))
        dura=clear_duration(dura)
        # print(dura)
        item['duration']=dura['duration']
        item['duration_per']=dura['duration_per']
        item['ucascode']=''.join(response.xpath('//dt[contains(text(),"UCAS")]/following-sibling::dd[1]//text()').extract())
        overview=response.xpath('//h2[contains(text(),"Highlights")]/preceding-sibling::div[1]').extract()
        # print(overview)
        overview=remove_class(overview)
        # print(overview)
        item['overview_en']=overview
        modules=response.xpath('//h2[contains(text(),"Course structure")]/following-sibling::section').extract()
        modules=remove_class(modules)
        item['modules_en']=modules
        # print(modules)
        # if modules=='':
        #     print(response.url)
        # entry=response.xpath('//h2[contains(text(),"ntry requirements")]/following-sibling::*').extract()
        entry=response.xpath('//h3[contains(text(),"International entry requirements")]/preceding-sibling::*|'
                             '//h3[contains(text(),"INTERNATIONAL ENTRY REQUIREMENTS")]/preceding-sibling::*|'
                             '//h3/*[contains(text(),"International entry requirements")]/../preceding-sibling::*|'
                             '//h3/*/*[contains(text(),"International entry requirements")]/../../preceding-sibling::*').extract()
        # print(entry)
        # if entry==[]:
        #     print(response.url)
        entry=remove_class(entry)
        item['alevel']=entry
        # print(entry)
        chinese=['<h3 class="content-show">Undergraduate entry requirements</h3>',
"<ul><li>To be considered for direct entry onto a 3-year Bachelor's degree at Birkbeck, applicants from China must have:</li><ul><li>a 2- or 3-year Diploma (<i>Zhuanke</i> or <i>Da Zhuan</i>) with a minimum final grade of at least 80% or equivalent</li><li>OR, at the discretion of the department, a Vocational Diploma (<i>Gaozhi</i>) with a minimum final grade of at least 80% or equivalent</li><li>OR to have completed the first year of a Bachelor's degree (<i>Xueshi</i>) with an average grade of at least 80% or equivalent. Students from higher-tiered universities may be accepted with an average grade of 75%.</li></ul><li>Applicants from China who have only completed the Senior Secondary School Certificate will normally need to apply as <span>Foundation year students (see above)</span>.</li><li>Applicants with the International Baccalaureate (IB) Diploma or A-levels will be considered for direct admission to our undergraduate degree programmes. IB requirements range from 28 to 30, depending on the course.</li></ul>",]
        item['require_chinese_en']=remove_class(chinese)
        item['toefl_desc']='overall score of 92, with 22 in Reading, 21 in Listening, 23 in Speaking, 24 in Writing.'
        item['toefl_l'],item['toefl_s'],item['toefl_r'],item['toefl_w']='22','23','22','24'
        ielts='overall score of 6.5, with 6.0 in each subtest'
        ielts=response.xpath('//*[contains(text(),"IELTS")]//text()').extract()
        # print(ielts)
        ies=re.findall('\d\.?\d?',''.join(ielts))
        # print(ies)
        if len(ies)==2:
            ies=list(map(float,ies))
            item['ielts'] = max(ies)
            item['ielts_l'] = min(ies)
            item['ielts_s'] = min(ies)
            item['ielts_r'] = min(ies)
            item['ielts_w'] = min(ies)
        item['ielts_desc']='\n'.join(ielts).strip()
        fee=response.xpath('//h2[contains(text(),"Fees")]/following-sibling::p/text()').extract()
        # print(fee)
        assessment=response.xpath('//h2[contains(text(),"Assessment")]/following-sibling::*').extract()
        assessment=remove_class(assessment)
        item['assessment_en']=assessment
        department=response.xpath('//a[contains(text(),"isit the")]/text()').extract()
        # print(department)
        department=''.join(department).replace('Visit the','').strip()
        # print(department)
        item['department']=department
        howtoapply=response.xpath('//h2[contains(text(),"How to apply")]/following-sibling::*').extract()
        howtoapply=remove_class(howtoapply)
        # print(howtoapply)
        item['apply_proces_en']=howtoapply
        # print(item)
        if mode!=[]:
            print('这个专业要')
            yield item
        else:
            print('这个专业只有兼职，不要！！！')
