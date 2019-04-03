# -*- coding: utf-8 -*-
import scrapy
from Australia.middlewares import *
from Australia.items import AustraliaItem
import requests
from lxml import etree
class TheuniversityofqueenslandUSpider(scrapy.Spider):
    name = 'TheUniversityofQueensland_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://future-students.uq.edu.au/study/find-a-program/listing/undergraduate']
    def parse(self, response):
        pro_list=response.xpath('//div[contains(text(),"Bachelor")]/../preceding-sibling::div[@class="column medium-4"]/a/@href').extract()
        for pl in pro_list:
            fullurl='https://future-students.uq.edu.au/set-location/international?destination='+pl
            yield scrapy.Request(url=fullurl,callback=self.parse_main)
    def parse_main(self,response,):
        item=get_item(AustraliaItem)
        item['url']=response.url
        print(response.url)
        item['university'] = 'The University of Queensland'
        item['degree_type'] = 1
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
        dura=re.findall('\d\.?\d{0,2}',duraiotn[0])
        # print(dura)
        item['duration']=dura[0]
        start_date = response.xpath('//div[contains(text(),"Commencing")]/following-sibling::div/text()').extract()
        start_date = tracslateDate(start_date)
        start_date = ','.join(set(start_date)).strip()
        # print(start_date)
        item['start_date'] = start_date
        rntry_requirements_en = response.xpath('//div[@id="entry-requirements"]').extract()
        rntry_requirements_en = remove_class(rntry_requirements_en)
        # print(rntry_requirements_en)
        item['rntry_requirements_en'] = rntry_requirements_en
        tuition_fee = response.xpath('//div[@class="program__section-indicative-fee-price-amt"]//text()').extract()
        tuition_fee = re.findall('\d+,\d+', ''.join(tuition_fee))
        tuition_fee = ''.join(tuition_fee).replace(',', '').strip()
        print(tuition_fee)
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = 'AUD'
        deadline = response.xpath('//h3[contains(text(),"Important dates")]/following-sibling::*//text()').extract()
        deadline = tracslateDate(deadline)
        deadline = ','.join(set(deadline))
        # print(deadline)
        item['deadline'] = deadline
        ielts = response.xpath('//p[contains(text(),"IELTS")]//text()').extract()
        item['ielts_desc'] = remove_class(ielts)
        iel = re.findall('\d\.?\d?', ''.join(ielts))
        if len(iel) == 5:
            item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w'] = iel[0], iel[4].strip(
                '.'), iel[3], iel[1], iel[2]
        major_url = response.xpath('//div[@id="majors"]//h3/../following-sibling::div/h3/a/@href').extract()
        # 如果有专业，逐条存入数据库
        # print(major_url)
        if major_url != []:
            for MajorUrl in major_url:
                MajorRes = self.GetRes(MajorUrl)
                # 专业页面上有可能有一个课程设置的链接
                ModuleUrl = MajorRes.xpath(
                    '//h1[contains(text(),"Courses")]/following-sibling::p/a[contains(text(),"course list")]/@href')
                if ModuleUrl != []:
                    ModuleUrl = 'https://my.uq.edu.au' + ModuleUrl[0]
                    ModuleRes = self.GetRes(ModuleUrl)
                    modules = ModuleRes.xpath('//div[@id="content-primary"]')
                    Modules = ''
                    for modules_part in modules:
                        Modules += etree.tostring(modules_part, method='html', encoding='unicode')
                    item['modules_en'] = remove_class(Modules)
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
    def GetRes(self, url):
        modules_res = requests.get(url)
        modules_res = etree.HTML(modules_res.content)
        return modules_res