# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
from scrapySchool_England_U.middlewares import *
import requests
from lxml import etree

class NorthumbriauniversityUSpider(scrapy.Spider):
    name = 'NorthumbriaUniversity_U'
    # allowed_domains = ['a.b']
    # start_urls = ['https://www.northumbria.ac.uk/study-at-northumbria/?cq=&ls=undergraduate&ms=&l=&d=&sm=']
    feeRes=etree.HTML(requests.get('https://www.northumbria.ac.uk/study-at-northumbria/fees-funding/international-fees-funding/international-fees/').content)
    def parse(self, response):
        print(response.url)
        pro_list=response.xpath('//div[@id="result-listing-items"]//a[contains(text(),"More details")]/@href').extract()
        # print(pro_list)
        for i in pro_list:
            full_url='https://www.northumbria.ac.uk' + i
            yield scrapy.Request(full_url,callback=self.parses)
    def parses(self, response):
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['location'] = 'Newcastle'
        item['university'] = 'Northumbria University'
        item['url'] = response.url
        programme = response.xpath(
            '//div[@class="col-sm-6"]/h1/text()|//div[@class="hero-content"]/h1/text()|//header[@class="course-heading"]/h1/text()').extract()
        programme = ''.join(programme).strip()
        degree_name = re.findall('[A-Z]{2,}.*', programme)
        degree_name = ''.join(degree_name)
        if degree_name != programme:
            programme = programme.replace(degree_name, '')
        item['programme_en'] = programme
        item['degree_name'] = degree_name
        dur = response.xpath(
            '//strong[contains(text(),"Mode")]/../text()|//span[contains(text(),"uration")]/../text()').extract()
        # print(dur)
        duration = clear_duration(dur)
        # print(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']
        # item['teach_time'] = '1'
        start_date = response.xpath(
            '//strong[contains(text(),"Start")]/../text()|//span[contains(text(),"Start")]/../text()').extract()
        start_date = set(start_date)
        # print(start_date)
        start_date = tracslateDate(start_date)
        # print(start_date)
        start_date = ','.join(start_date)
        item['start_date'] = start_date
        deadline = response.xpath('//span[contains(text(),"deadline")]/../text()').extract()
        deadline = set(deadline)
        deadline = tracslateDate(deadline)
        # print(deadline)
        deadline = ''.join(deadline)
        item['deadline'] = deadline
        ielts = response.xpath('//*[contains(text(),"IELTS")]/text()').extract()
        item['ielts_desc'] = ''.join(ielts).strip()
        ielts = get_ielts(ielts)
        try:
            if ielts != [] or ielts != {}:
                item['ielts_l'] = ielts['IELTS_L']
                item['ielts_s'] = ielts['IELTS_S']
                item['ielts_r'] = ielts['IELTS_R']
                item['ielts_w'] = ielts['IELTS_W']
                item['ielts'] = ielts['IELTS']
        except:
            pass
        if ielts == []:
            ielts = response.xpath('//*[contains(text(),"English Language requirements")]/../text()').extract()
            ielts = get_ielts(ielts)
            try:
                if ielts != [] or ielts != {}:
                    item['ielts_l'] = ielts['IELTS_L']
                    item['ielts_s'] = ielts['IELTS_S']
                    item['ielts_r'] = ielts['IELTS_R']
                    item['ielts_w'] = ielts['IELTS_W']
                    item['ielts'] = ielts['IELTS']
            except:
                pass
            # print(ielts)
        overview = response.xpath(
            '//div[@id="tab-0"]//div[@class="rich-text"]|//h3[contains(text(),"Overview")]/following-sibling::p').extract()
        if overview==[]:
            overview=response.xpath('//span[contains(text(),"2019")]/../following-sibling::div/p').extract()
        if overview==[]:
            overview=response.xpath('//h2[contains(text(),"About this course")]/following-sibling::div').extract()
        # if overview==[]:
        #     print(response.url)
        # else:
        #     print('GG')
        overview = remove_class(overview)
        # print(overview)
        item['overview_en'] = overview
        modules = response.xpath('//div[@id="tab-1"]//div[@class="rich-text"]|//div[@id="modules"]|'
                                 '//h1[contains(text(),"Modules Overview")]/following-sibling::*').extract()
        # if modules==[]:
        #     print(response.url)
        modules = remove_class(modules)
        # print(modules)
        item['modules_en'] = modules
        rntry = response.xpath('//*[contains(text(),"English Language requirements")]/..').extract()
        rntry = remove_class(rntry)
        # print(rntry)
        item['require_chinese_en'] = rntry
        howtoapply = response.xpath('//div[@id="how-to-apply"]').extract()
        howtoapply = remove_class(howtoapply)
        item['apply_proces_en'] = howtoapply
        department = response.xpath('//strong[contains(text(),"Department")]/../text()').extract()
        #学院正常
        # if department==[]:
        #     print(response.url)
        department = ''.join(department).strip()
        # print(department)
        item['department'] = department
        if department!='':
            fee_xpath='//div[@class="overview 2018-19 open"]//h1[contains(text(),"Fees for Undergraduate Courses")]/../following-sibling::div/table/tbody/tr/td[contains(text(),"'+str(department)+'")]/following-sibling::td//text()'
            fee=self.feeRes.xpath(fee_xpath)
            item['tuition_fee']=getTuition_fee(fee)
            # print(item['tuition_fee'])
            item['tuition_fee_pre'] = '£'

        ucascode=response.xpath('//strong[contains(text(),"UCAS Code")]/../text()').extract()
        ucascode=''.join(ucascode).strip()
        # print(ucascode)
        item['ucascode']=ucascode

        career=response.xpath('//h1[contains(text(),"career")]/../following-sibling::div|//div[@id="tab-5"]').extract()
        if career==[]:
            career=response.xpath('//h1[contains(text(),"areer")]/../following-sibling::*').extract()
        career=remove_class(career)
        # print(career)
        item['career_en']=career

        # print(item)
        yield item
