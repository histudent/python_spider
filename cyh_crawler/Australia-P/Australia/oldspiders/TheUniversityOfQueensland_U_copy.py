# -*- coding: utf-8 -*-
import scrapy
from Australia.middlewares import *
from Australia.items import AustraliaItem
import requests
from lxml import etree
import json
class TheuniversityofqueenslandUSpider(scrapy.Spider):
    name = 'TheUniversityOfQueensland_U'
    start_urls = ['https://future-students.uq.edu.au/study/find-a-program/listing/undergraduate']
    # career=response.xpath('//h1[contains(text(),"Employment opportunities")]|//h1[contains(text(),"Employment opportunities")]/following-sibling::div[1]').extract()
    def parse(self, response):
        pro_list = response.xpath('//a[@class="program__secondary-link"]/@href').extract()
        for i in pro_list:
            full_url = 'https://future-students.uq.edu.au' + i
            yield scrapy.Request(url=full_url, callback=self.parses)
    def parses(self, response):
        item = get_item(AustraliaItem)
        print(response.url)
        item['url'] = response.url
        item['university'] = 'The University of Queensland'
        item['degree_type']=1
        programme = response.xpath('//h1/text()').extract()
        programme = ''.join(programme).strip()
        master = response.xpath('//h1/span/text()').extract()
        master = ''.join(master).strip()
        degree_name=master + ' ' + programme
        item['degree_name'] =  degree_name
        item['apply_fee'] = '100'
        item['apply_pre'] = 'AUD'
        location = response.xpath('//div[contains(text(),"Delivery location")]/following-sibling::div/text()').extract()
        location = ''.join(location).strip()
        item['location'] = location
        duraiotn = response.xpath('//div[@class="program__duration-value"]/span/text()').extract()
        try:
            dura = min(list(map(float,re.findall('\d\.?\d?', ''.join(duraiotn)))))
        except:
            dura = None
        duraiotn = clear_duration(duraiotn)
        item['duration'] = dura
        item['duration_per'] = duraiotn['duration_per']
        start_date = response.xpath('//div[@class="program__commencement-value"]/span/text()').extract()
        start_date = tracslateDate(start_date)
        start_date = ','.join(set(start_date)).strip()
        item['start_date'] = start_date
        department = response.xpath('//div[contains(text(),"Faculty")]/following-sibling::div//text()').extract()
        department = ''.join(department).strip()
        item['department'] = department
        degree_overview = response.xpath('//div[@id="why-study"]|//div[@id="program-overview"]').extract()
        degree_overview = remove_class(degree_overview)
        clear_do=re.findall('\* Class.+-->',degree_overview,re.S)
        degree_overview=degree_overview.replace(''.join(clear_do),'').replace('<!--','').strip()
        degree_overview=remove_class(degree_overview)
        item['degree_overview_en'] = degree_overview
        rntry_requirements_en = response.xpath('//div[@id="entry-requirements"]').extract()
        rntry_requirements_en = remove_class(rntry_requirements_en)
        item['rntry_requirements_en'] = rntry_requirements_en
        tuition_fee = response.xpath('//div[@class="program__section-indicative-fee-price-amt"]//text()').extract()
        tuition_fee = re.findall('\d+,\d+', ''.join(tuition_fee))
        tuition_fee = ''.join(tuition_fee).replace(',', '').strip()
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = 'AUD'
        deadline = response.xpath('//h3[contains(text(),"Important dates")]/following-sibling::*//text()').extract()
        deadline = tracslateDate(deadline)
        deadline = ','.join(set(deadline))
        item['deadline'] = deadline
        apply_proces_en=['<h3>Your senior schooling is from Australia</h3>',
'			<p>If you’re currently studying Year 12 (either in Australia or offshore) or the International Baccalaureate (IB) in Australia, submit your application online through the Queensland Tertiary Admissions Centre (QTAC).</p>',
'			<a class="button button--primary" href="http://www.qtac.edu.au/Applications/apply-here" target="_blank">Apply to QTAC</a></div>',
'		<div class="columns large-6">&nbsp;',
'			<h3>All other international applicants</h3>',
'			<p>If you’re <span>an international student&nbsp;</span><strong>not</strong> currently studying Year 12 or the International Baccalaureate (IB) in Australia, submit your application directly to UQ.</p>',]
        apply_proces_en=remove_class(apply_proces_en)
        item['apply_proces_en']=apply_proces_en
        ielts = response.xpath('//p[contains(text(),"IELTS")]//text()').extract()
        item['ielts_desc']=remove_class(ielts)
        iel=re.findall('\d\.?\d?',''.join(ielts))
        if len(iel)==5:
            item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']=iel[0],iel[4].strip('.'),iel[3],iel[1],iel[2]
        major_url = response.xpath('//div[@id="majors"]//h3/../following-sibling::div/h3/a/@href').extract()
        #如果有专业，逐条存入数据库
        if major_url!=[]:
            for MajorUrl in major_url:
                MajorRes=self.GetRes(MajorUrl)
                #专业页面上有可能有一个课程设置的链接
                ModuleUrl=MajorRes.xpath('//h1[contains(text(),"Courses")]/following-sibling::p/a[contains(text(),"course list")]/@href')
                if ModuleUrl!=[]:
                    ModuleUrl='https://my.uq.edu.au'+ModuleUrl[0]
                    ModuleRes=self.GetRes(ModuleUrl)
                    modules=ModuleRes.xpath('id="content-primary"')
                    Modules=''
                    for modules_part in modules:
                        Modules+=etree.tostring(modules_part,method='html',encoding='unicode')
                    item['modules_en']=Modules
                else:
                    item['modules_en']=''
                item['programme_en']=''.join(MajorRes.xpath('//div[@id="page-head"]/h1//text()')).strip()
                overview=MajorRes.xpath('//div[@id="description"]')
                item['overview_en']=remove_class(overview)
        #         yield item
        # else:
        #     yield item

    def GetRes(self, url):
        modules_res=requests.get(url)
        modules_res=etree.HTML(modules_res.content)
        return modules_res
