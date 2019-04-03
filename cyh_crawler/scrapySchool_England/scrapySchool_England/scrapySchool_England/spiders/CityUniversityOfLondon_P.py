# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.middlewares import clear_duration,tracslateDate
from scrapySchool_England.clearSpace import clear_same_s

class CityuniversityoflondonPSpider(scrapy.Spider):
    name = 'CityUniversityOfLondon_P'
    allowed_domains = ['city.ac.uk']
    start_urls = ['https://www.city.ac.uk/courses?query=&p=1&level=Postgraduate']
    def parse(self, response):
        # print(response.url)
        url_list=response.xpath('//div[@class="course-finder__results__item course-finder__results__item--postgraduate"]//h2/a/@href').extract()
        programme=response.xpath('//div[@class="course-finder__results__item course-finder__results__item--postgraduate"]//h2/a/text()').extract()
        degree_name=response.xpath('//h2/following-sibling::div/text()').extract()
        #//a[contains(text(),"Actuarial Management")]/../../../following-sibling::div//span[@class="fa fa-building-o"]/following-sibling::div//text()
        for url,pro,deg in zip(url_list,programme,degree_name):
            department_xpath='//a[contains(text(),"'+pro+'")]/../../../following-sibling::div//span[@class="fa fa-building-o"]/following-sibling::div//text()'
            department=response.xpath(department_xpath).extract()
            # print(url,pro,deg,department)
            yield scrapy.Request(url,meta={'programme':pro,'degree_name':deg,'department':department},callback=self.parse_main)
        next_page=response.xpath('//a[@class="after enabled"]/@href').extract()
        # print(next_page)
        if len(next_page)==2:
            next_page_url='https://www.city.ac.uk/courses'+next_page[0]
            yield scrapy.Request(next_page_url,callback=self.parse)
    def parse_main(self,response):
        item=get_item1(ScrapyschoolEnglandItem1)
        # print(response.url)
        item['university'] = "City, University of London"
        item['url'] = response.url
        item['location'] = 'London'
        item['programme_en'] = response.meta['programme']
        item['degree_name'] = response.meta['degree_name']
        item['tuition_fee_pre'] = '£'
        item['teach_type']='taught'
        department=response.meta['department']
        department=set(department)
        department=' '.join(department)
        item['department'] = department

        fee=response.xpath('//h3[contains(text(),"Fee")]/../../following-sibling::div//text()').extract()
        tuition_fee=getTuition_fee(fee)
        if tuition_fee==0:
            fee = response.xpath('//span[contains(text(),"£")]//text()').extract()
            tuition_fee = getTuition_fee(fee)
        item['tuition_fee'] = tuition_fee
        # print(item['tuition_fee'])

        overview=response.xpath('//h2[contains(text(),"Who is it")]/following-sibling::*|'
                                '//h2[contains(text(),"Overview")]/following-sibling::*').extract()
        overview=remove_class(overview)
        overview=clear_same_s(overview)
        # print(overview)
        item['overview_en'] = overview

        modules=response.xpath('//h2[contains(text(),"Structure")]/following-sibling::*|'
                               '//h2[contains(text(),"Modules")]/following-sibling::*').extract()
        modules=remove_class(modules)
        modules=clear_same_s(modules)
        # print(modules)
        item['modules_en'] = modules

        rntry_requirement=response.xpath('//h3[contains(text(),"Entry")]/following-sibling::*|//div[@id="entryreq"]').extract()
        rntry_requirement=remove_class(rntry_requirement)
        rntry_requirement=clear_same_s(rntry_requirement)
        # print(rntry_requirement)
        item['rntry_requirements'] = rntry_requirement

        ielts=response.xpath('//*[contains(text(),"IELTS")]//text()').extract()
        ielts=get_ielts(ielts)
        # print(ielts)
        if ielts != {} and ielts != []:
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            item['ielts'] = ielts['IELTS']

        career=response.xpath('//h2[contains(text(),"Career")]/following-sibling::*').extract()
        # print(career)
        career=remove_class(career)
        career=clear_same_s(career)
        item['career_en'] = career
        # print(career)

        duration=response.xpath('//span[contains(text(),"Duration")]/../following-sibling::div//text()|'
                                '//h3[contains(text(),"Duration")]/following-sibling::*//text()').extract()
        mode=re.findall('(?i)full',''.join(duration))
        if mode!=[]:
            item['teach_time']='1'
        else:
            item['teach_time']='2'
        # print(''.join(duration))
        duration=clear_duration(duration)
        # print(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']

        start_date=response.xpath('//h3[contains(text(),"Start date")]/following-sibling::p/text()').extract()
        start_date=tracslateDate(start_date)
        start_date=','.join(start_date)
        item['start_date']=start_date
        # print(start_date)

        apply_desc_en=response.xpath('//h3[contains(text(),"How to apply")]/following-sibling::*|//div[@id="howtoapply"]').extract()
        apply_desc_en=remove_class(apply_desc_en)
        item['apply_proces_en']=apply_desc_en

        require_chinese="<p>Applicants will be considered for most postgraduate courses with a good Chinese bachelor’s degree from a recognised University.Students who don’t meet the requirements for direct entry may have the option to undertake our Graduate Diploma programme at INTO City, which then offers the opportunity for guaranteed entry into City’s Masters programmes.</p>"
        item['require_chinese_en']=require_chinese

        assessment=response.xpath('//h2[contains(text(),"Teaching and learning")]/following-sibling::*|//h3[contains(text(),"ssessment")]/following-sibling::*').extract()
        # if assessment==[]:
        #     print(response.url)
        # else:
        #     print('不为空')
        item['assessment_en']=remove_class(assessment)

        # print(item)
        # yield (item)