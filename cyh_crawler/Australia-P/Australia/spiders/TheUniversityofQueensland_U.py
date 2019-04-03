# -*- coding: utf-8 -*-
import scrapy
from Australia.middlewares import *
from Australia.items import AustraliaItem
import requests
from lxml import etree
class TheuniversityofqueenslandUSpider(scrapy.Spider):
    name = 'TheUniversityofQueensland_P'
    # allowed_domains = ['a.b']
    start_urls = ['https://future-students.uq.edu.au/study/find-a-program/listing/postgraduate']
    def parse(self, response):
        pro_list=response.xpath('//div[contains(text(),"asters")]/../preceding-sibling::div[@class="column medium-4"]/a/@href').extract()
        for pl in pro_list:
            fullurl='https://future-students.uq.edu.au/set-location/international?destination='+pl
            yield scrapy.Request(url=fullurl,callback=self.parse_main)
    def parse_main(self,response,):
        item=get_item(AustraliaItem)
        item['url']=response.url
        print(response.url)
        item['university'] = 'The University of Queensland'
        item['degree_type'] = 2
        programme = response.xpath('//h1/text()').extract()
        programme = ''.join(programme).strip()
        master = response.xpath('//h1/span/text()').extract()
        master = ''.join(master).strip()
        degree_name = master + ' ' + programme
        item['degree_name'] = degree_name
        item['apply_fee'] = '100'
        item['apply_pre'] = 'AUD'
        location = response.xpath('//div[contains(text(),"Delivery location")]/following-sibling::div/text()').extract()
        location = ''.join(location).strip()
        item['location'] = location
        duraiotn = response.xpath('//div[contains(text(),"Duration")]/following-sibling::div/text()').extract()
        # print(duraiotn)
        item['duration_per']='1'
        dura=re.findall('\d\.?\d{0,2}',''.join(duraiotn))
        # print(dura)
        item['duration']=''.join(dura)
        start_date = response.xpath('//div[contains(text(),"Commencing")]/following-sibling::div/text()').extract()
        start_date = tracslateDate(start_date)
        start_date = ','.join(set(start_date)).strip()
        # print(start_date)
        item['start_date'] = start_date
        item['overview_en']=remove_class(response.xpath('//div[@class="columns large-centered large-11 drupal-field"]').extract())
        rntry_requirements_en = response.xpath('//div[@id="entry-requirements"]').extract()
        rntry_requirements_en = remove_class(rntry_requirements_en)
        # print(rntry_requirements_en)
        item['career_en']=remove_class(response.xpath('//div[@class="program__career-outcomes-content"]').extract())
        item['rntry_requirements_en'] = rntry_requirements_en
        tuition_fee = response.xpath('//div[@class="program__section-indicative-fee-price-amt"]//text()').extract()
        tuition_fee = re.findall('\d+,\d+', ''.join(tuition_fee))
        tuition_fee = ''.join(tuition_fee).replace(',', '').strip()
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = 'AUD'
        deadline = response.xpath('//h3[contains(text(),"Important dates")]/following-sibling::*//text()').extract()
        deadline = tracslateDate(deadline)
        deadline = ','.join(set(deadline))
        # print(deadline)
        item['deadline'] = deadline
        ielts = response.xpath('//p[contains(text(),"IELTS")]//text()').extract()
        item['ielts_desc'] = remove_class(ielts)
        iel = re.findall('IELTS overall[ 567\.a-zA-Z;]+', ''.join(ielts))
        iel=re.findall('\d\.?\d?',''.join(iel))
        if len(iel) == 5:
            item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w'] = iel[0], iel[4].strip(
                '.'), iel[3], iel[1], iel[2]

        major_url = response.xpath('//a[contains(text(),"Courses") and contains(@class,"show")]/@href').extract()
        if len(major_url)==1:
            MajorRes = etree.HTML(requests.get(major_url[0]).content)
            modules = MajorRes.xpath('//div[@id="content-primary"]')
            Modules = ''
            for modules_part in modules:
                Modules += etree.tostring(modules_part, method='html', encoding='unicode')
            item['modules_en'] = remove_class(Modules)
        # yield item
        # 如果有专业，逐条存入数据库
        major_url=response.xpath('//h3[text()="Fields of study"]/../following-sibling::div/h3/a/@href').extract()
        # print(major_url)
        if major_url != []:
            for MajorUrl in major_url:
                MajorRes = etree.HTML(requests.get(MajorUrl).content)
                ModuleUrl = MajorRes.xpath(
                    '//h1[contains(text(),"Courses")]/following-sibling::p/a[contains(text(),"course list")]/@href')
                if ModuleUrl != []:
                    ModuleUrl = 'https://my.uq.edu.au' + ModuleUrl[0]
                    ModuleRes = etree.HTML(requests.get(ModuleUrl).content)
                    modules = ModuleRes.xpath('//div[@id="content-primary"]')
                    Modules = ''
                    for modules_part in modules:
                        Modules += etree.tostring(modules_part, method='html', encoding='unicode')
                    item['modules_en'] = Modules
                else:
                    item['modules_en'] = ''
                item['programme_en'] = ''.join(MajorRes.xpath('//div[@id="page-head"]/h1//text()')).strip()
                overview = MajorRes.xpath('//h1[contains(text(),"Why study")]/following-sibling::div[1]')
                ove=''
                for over in overview:
                    ove += etree.tostring(over, method='html', encoding='unicode')
                # print(ove)
                item['overview_en'] = remove_class(ove)
                department=MajorRes.xpath('//p[@id="plan-field-school"]//text()')
                item['department']=remove_class(department)
                yield item
        else:
            item['programme_en']=programme
            yield item
