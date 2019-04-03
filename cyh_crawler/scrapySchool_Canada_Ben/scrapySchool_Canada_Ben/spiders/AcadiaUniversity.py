# -*- coding: utf-8 -*-
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import *
from scrapySchool_Canada_Ben.items import *

class AcadiauniversitySpider(scrapy.Spider):
    name = 'AcadiaUniversity'
    # allowed_domains = ['a.b']
    start_urls = ['https://www2.acadiau.ca/programs_undergrad.html']

    #$40 CDN application processing fee
    #TOEFL - 90 IBT with no subtest score below 20 IELTS - 6.5 with no subtest score below 6.0
    #China - Senior/Upper Middle School Graduation Certificate with minimum 85%
    #3月1日是接受申请的截止日期
    # IB Diploma including IB English with an overall score of 24 or better.
    # Students admitted to Acadia University with a score of 30 or higher on the IB Diploma will receive 30 hours of university credit.
    # Students who have completed IB courses but do not possess the Diploma will be considered based on their coursework. Acadia gives individual credit for IB courses completed at the higher level with grades of 5, 6 or 7.
    # $ 17,363.00
    def parse(self, response):
        urls=response.xpath('//table[@id="programs_list"]/tbody/tr/td/span/a/@href').extract()
        # print(urls)
        department=response.xpath('//table[@id="programs_list"]/tbody/tr/td[1]//span[contains(text(),"Faculty")][1]/text()').extract()
        for ul,dep in zip(urls,department):
            if ul[0]!='h':
                ul='https://www2.acadiau.ca/'+ul
            yield scrapy.Request(url=ul,callback=self.parses,meta={'department':dep})
    def parses(self, response):
        item=get_item(ScrapyschoolCanadaBenItem)
        item['url']=response.url
        item['school_name']='Acadia University'
        item['tuition_fee']='17,363.00'
        item['tuition_fee_pre']='$'
        item['deadline']='2019-03-01'
        item['apply_fee']='40'
        item['apply_pre']='CAD$'
        item['toefl'],item['toefl_l'],item['toefl_s'],item['toefl_r'],item['toefl_w']='90','20','20','20','20'
        item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']='6.5','6.0','6.0','6.0','6.0'
        item['toefl_desc']='TOEFL - 90 IBT with no subtest score below 20'
        item['ielts_desc']='IELTS - 6.5 with no subtest score below 6.0'
        item['ib']='<p>IB Diploma including IB English with an overall score of 24 or better.</p><p>Students admitted to Acadia University with a score of 30 or higher on the IB Diploma will receive 30 hours of university credit.</p><p>Students who have completed IB courses but do not possess the Diploma will be considered based on their coursework. Acadia gives individual credit for IB courses completed at the higher level with grades of 5, 6 or 7.</p>'
        item['alevel']='<p>GCE Advanced level with minimum two grades of C or better</p>'
        item['require_chinese_en']='<p>China - Senior/Upper Middle School Graduation Certificate with minimum 85%</p>'
        print(response.url)
        department=response.meta['department']
        prog=response.xpath('//h1/text()').extract()
        prog=''.join(prog).strip()
        # print(prog)
        item['department']=department
        overview=response.xpath('//div[@class="col-sm-8"]/div[position()<3]').extract()
        item['overview_en']=remove_class(overview)
        career=response.xpath('//h2[contains(text(),"areer")]/following-sibling::div[1]').extract()
        item['career_en']=remove_class(career)
        modules=response.xpath('//h2[contains(text(),"irst")]/following-sibling::div').extract()
        item['modules_en']=remove_class(modules)

        major_name=prog.split('(')[0].strip()
        # print(major_name)
        item['major_name_en']=major_name
        if '(' in prog:
            degree_name=prog.split('(')[1].strip().replace(')','')
            # print(degree_name)
            degree_name=degree_name.split(',')
            for dn in degree_name:
                item['degree_name']=dn.strip()
                yield item
        else:
            yield item
