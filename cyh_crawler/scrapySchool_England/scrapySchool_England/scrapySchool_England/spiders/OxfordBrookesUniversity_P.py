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
class OxfordbrookesuniversityPSpider(scrapy.Spider):
    name = 'OxfordBrookesUniversity_P'
    allowed_domains = ['brookes.ac.uk']
    start_urls = ['https://www.brookes.ac.uk/templates/pages/coursefinder.aspx?q=&searchtype=postgraduate&filter=0&out=xml&getfields=*&requiredfields=contenttype:course.courselevel:postgraduate&partialfields=&client=dynamic_course_frontend&site=dynamic_course_collection&start=1']
    def parse(self, response):
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university'] = 'Oxford Brookes University'
        item['url'] = response.url
        tall=response.xpath('//h2[contains(text(),"Approach to assessment")]/following-sibling::*').extract()
        tnext=response.xpath('//h2[contains(text(),"Approach to assessment")]/following-sibling::h2[1]/self::*').extract()
        if tnext!=[]:
            assessment=tall[0:tall.index(tnext[0])]
        else:
            assessment=tall
        # print(assessment)
        if assessment==[]:
            assessment=response.xpath('//h2[contains(text(),"Approach to assessment")]/../text()').extract()
            item['assessment_en']='<div>'+remove_class(assessment)+'</div>'
        else:
            item['assessment_en']=remove_class(assessment)
        yield item
    def parses(self, response):
        print('进入一个列表页')
        proURL=response.xpath('//h2[contains(text(),"Search results")]/following-sibling::ul//h3//a/@href').extract()
        next_page=response.xpath('//a[contains(text(),"Next")]/@href').extract()
        # print(proURL)
        for i in proURL:
            yield scrapy.Request(url=i,callback=self.parse_main)
        if next_page!=[]:
            full_url='https://www.brookes.ac.uk'+next_page[0]
            yield scrapy.Request(url=full_url,callback=self.parse)
    def parse_main(self,response):
        print('进入一个详情页')
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university']='Oxford Brookes University'
        item['url'] = response.url
        item['location'] ='London'
        programme=response.xpath('//h1/text()').extract()
        programme=''.join(programme).strip()
        # print(programme)
        item['programme_en']=programme
        degree_name=response.xpath('//h1/following-sibling::h2/text()').extract()
        degree_name=''.join(degree_name).strip()
        # print(degree_name)
        item['degree_name']=degree_name
        department=response.xpath('//h1/following-sibling::h2/following-sibling::p/a/text()').extract()
        department=''.join(department).strip()
        # print(department)
        item['department'] = department
        start_date=response.xpath('//h3[contains(text(),"Available")]/following-sibling::p[1]/text()').extract()
        start_date=tracslateDate(start_date)
        start_date=','.join(start_date)
        # print(start_date)
        item['start_date']=start_date
        duration = response.xpath('//h3[contains(text(),"Course length")]/following-sibling::ul//text()').extract()
        # print(duration)
        mode=re.findall('(?i)full',''.join(duration))
        if mode!=[]:
            item['teach_time']='fulltime'
        else:
            item['teach_time']='parttime'
        try:
            duration=clear_duration(duration)
            # print(duration)
            item['duration'] = duration['duration']
            item['duration_per'] = duration['duration_per']
        except:
            pass
        overview=response.xpath('//h1/following-sibling::h2/following-sibling::p/following-sibling::*').extract()
        overview=remove_class(overview)
        item['overview_en'] = overview
        modules=response.xpath('//div[@id="section-two"]').extract()
        modules=remove_class(modules)
        item['modules_en']=modules
        fee=response.xpath('//p[contains(text(),"£")]/text()').extract()
        tuition_fee=getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee']=tuition_fee
        item['tuition_fee_pre']='£'
        rntry=response.xpath('//div[@id="section-four"]').extract()
        rntry=remove_class(rntry)
        item['rntry_requirements'] = rntry
        career=response.xpath('//div[@id="section-five"]').extract()
        career=remove_class(career)
        item['career_en'] = career
        ielts=response.xpath('//*[contains(text(),"IELTS")]/text()').extract()
        ielts=''.join(ielts)
        IELTS=ielts
        ielts=re.findall('\d\.\d',ielts)
        if len(ielts)==2:
            # print('长度为二的ielts',ielts)
            ielts=list(map(float,ielts))
            item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']=max(ielts),min(ielts),min(ielts),min(ielts),min(ielts)
        elif len(ielts)==3:
            # print('长度为三的ielts',ielts,IELTS)
            item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']=ielts[0],ielts[2],ielts[2],ielts[1],ielts[1]
        elif len(ielts)==0:
            pass
        elif len(ielts)==1:
            # print('长度为一的ielts',ielts)
            item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']=ielts[0],ielts[0],ielts[0],ielts[0],ielts[0]
        else:
            # print('其他长度的ielts',ielts,response.url)
            item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']=max(ielts),min(ielts),min(ielts),min(ielts),min(ielts)
        # print(item)
        yield item