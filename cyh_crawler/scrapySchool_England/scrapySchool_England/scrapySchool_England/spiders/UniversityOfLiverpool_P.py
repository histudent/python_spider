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
# import numpy
from lxml import etree
import requests
class UniversityofliverpoolPSpider(scrapy.Spider):
    name = 'UniversityOfLiverpool_P'
    # allowed_domains = ['liverpool.ac.uk']

    start_urls = [
        'https://www.liverpool.ac.uk/london/programmes/finance-accounting-business-and-communication/msc-accounting/entry-requirements/',
        'https://www.liverpool.ac.uk/london/programmes/design/msc-advanced-transdisciplinary-design/entry-requirements/',
        'https://www.liverpool.ac.uk/london/programmes/finance-accounting-business-and-communication/msc-banking-and-finance/entry-requirements/entry-requirements/',
        'https://www.liverpool.ac.uk/london/programmes/finance-accounting-business-and-communication/msc-finance-and-investment-management/entry-requirements/',
        'https://www.liverpool.ac.uk/london/programmes/finance-accounting-business-and-communication/msc-financial-and-actuarial-mathematics/entry-requirements/',
        'https://www.liverpool.ac.uk/london/programmes/finance-accounting-business-and-communication/msc-international-accounting/entry-requirements/',
        'https://www.liverpool.ac.uk/london/programmes/finance-accounting-business-and-communication/msc-strategic-communication/entry-requirements/',
        'https://www.liverpool.ac.uk/london/programmes/design/msc-urban-design-and-property-development/entry-requirements/',
        'https://www.liverpool.ac.uk/london/programmes/design/msc-urban-planning/entry-requirements/', ]
    # feeRes = etree.HTML(requests.get('https://www.liverpool.ac.uk/study/international/tuition-fees-and-scholarships/undergraduate-fees/').content)
    # 补抓的parse
    def parse(self, response):
        item=get_item1(ScrapyschoolEnglandItem1)
        rentry = response.xpath('//article[@class="content"]').extract()
        item['university'] = 'University of Liverpool'
        item['url']=response.url.replace('entry-requirements/','').strip()
        # if rentry==[]:
        #     print(response.url)
        rntry = remove_class(rentry)
        item['rntry_requirements']=rntry
        # print(rntry)
        career_url = response.url.replace('entry-requirements/', 'careers/')
        carRs = self.getTag(self.getRes(career_url).xpath('//article[@class="content"]'))
        if carRs==[]:
            print(response.url)
        item['career_en']=remove_class(carRs)
        # print(carRs)
        yield item

    def getRes(self,urls):
        return etree.HTML(requests.get(urls).content)
    def getTag(self,text):
        var=''
        for i in text:
            var+=etree.tostring(i,method='html',encoding='unicode')
        var=remove_class(var)
        return var

    def parsesss(self, response):
        department_url=response.xpath('//div[@id="departments"]/table[@id="courseslist"]/tbody/tr/td[1]/a/@href').extract()
        for i in department_url:
            full_url='https://www.liverpool.ac.uk/study/postgraduate-taught/courses/'+i
            yield scrapy.Request(full_url,callback=self.parse_2)
    def parse_2(self,response):
        # print(response.url)
        department=response.xpath('//h1/text()').extract()
        url_list=response.xpath('//h1/following-sibling::ul//a/@href').extract()
        for url in url_list:
            try:
                yield scrapy.Request(url,meta={'department':''.join(department)},callback=self.parses)
            except:
                pass
#     start_urls=['https://www.liverpool.ac.uk/london/programmes/finance-accounting-business-and-communication/msc-accounting/',
# 'https://www.liverpool.ac.uk/london/programmes/design/msc-advanced-transdisciplinary-design/',
# 'https://www.liverpool.ac.uk/london/programmes/finance-accounting-business-and-communication/msc-banking-and-finance/entry-requirements/',
# 'https://www.liverpool.ac.uk/london/programmes/finance-accounting-business-and-communication/msc-finance-and-investment-management/',
# 'https://www.liverpool.ac.uk/london/programmes/finance-accounting-business-and-communication/msc-financial-and-actuarial-mathematics/',
# 'https://www.liverpool.ac.uk/london/programmes/finance-accounting-business-and-communication/msc-international-accounting/',
# 'https://www.liverpool.ac.uk/london/programmes/finance-accounting-business-and-communication/msc-strategic-communication/',
# 'https://www.liverpool.ac.uk/london/programmes/design/msc-urban-design-and-property-development/',
# 'https://www.liverpool.ac.uk/london/programmes/design/msc-urban-planning/']
#     start_urls=[]
    def parses(self,response):
        # print(response.url)
        department=response.meta['department']
        # department='University of Liverpool in London'
        overview=response.xpath('//section[@class="content"]').extract()
        overview=remove_class(overview)
        overview=clear_same_s(overview)
        # print(overview)
        tabs=response.xpath('//div[@id="course-tabs"]/ul/li//text()').extract()
        # print(tabs)
        modules_url=response.url.replace('overview','module-details')
        if tabs!=[]:
            yield scrapy.Request(modules_url,meta={'overview':overview,'department':department},callback=self.parse_modules)
    def parse_modules(self,response):
        overview=response.meta['overview']
        department=response.meta['department']
        modules=response.xpath('//section[@class="content"]').extract()
        modules=remove_class(modules)
        # modules=clear_same_s(modules)
        # print(modules)
        rntry_url=response.url.replace('module-details','entry-requirements')
        yield scrapy.Request(rntry_url,meta={'overview':overview,'department':department,'modules':modules},callback=self.parse_rntry)
    def parse_rntry(self,response):
        overview=response.meta['overview']
        modules=response.meta['modules']
        department = response.meta['department']
        rntry1=response.xpath('//h1[contains(text(),"Entry requirements")]/following-sibling::p').extract()
        # print(rntry1)
        rntry2=response.xpath('//h3[contains(text(),"International qualifications")]/preceding-sibling::p').extract()
        # rntry2=response.xpath('//h3[contains(text(),"International qualifications")]/following-sibling::p').extract()
        rntry = list((set(rntry1).union(set(rntry2))) ^ (set(rntry1) ^ set(rntry2)))
        # rntry=numpy.array_str(rntry1)-numpy.array_str(rntry2)
        # rntry=[ i for i in rntry2 if i not in rntry1 ]
        # print(rntry)
        rntry=remove_class(rntry)
        ielts=response.xpath('//th[contains(text(),"IELTS")]/following-sibling::td//text()').extract()
        # rntry=remove_class()
        toefl=response.xpath('//th[contains(text(),"TOEFL")]/following-sibling::td//text()').extract()

        fee_url=response.url.replace('entry-requirements','fees')
        yield scrapy.Request(fee_url,meta={'overview':overview,'ielts':ielts,'toefl':toefl,'department':department,'modules':modules,'rntry_requirements':rntry},callback=self.parse_fee)
    def parse_fee(self,response):
        overview = response.meta['overview']
        modules = response.meta['modules']
        department = response.meta['department']
        ielts=response.meta['ielts']
        rntry_requirements=response.meta['rntry_requirements']
        tuition_fee=getTuition_fee(response.xpath('//section[@class="content"]').extract())
        toefl=response.meta['toefl']
        # print(tuition_fee)
        apply_url=response.url.replace('fees','applying')
        yield scrapy.Request(apply_url,meta={'overview':overview,'ielts':ielts,'toefl':toefl,'department':department,'modules':modules,'rntry_requirements':rntry_requirements,
                                             'tuition_fee':tuition_fee},callback=self.parse_apply)
    def parse_apply(self,response):
        overview = response.meta['overview']
        modules = response.meta['modules']
        department = response.meta['department']
        ielts=response.meta['ielts']
        rntry_requirements = response.meta['rntry_requirements']
        tuition_fee=response.meta['tuition_fee']
        toefl=response.meta['toefl']
        apply=response.xpath('//section[@class="content"]').extract()
        apply=remove_class(apply)
        career_url=response.url.replace('applying','career-prospects')
        yield scrapy.Request(career_url,
                             meta={'overview': overview,'ielts':ielts,'toefl':toefl, 'department':department,'modules': modules, 'rntry_requirements': rntry_requirements,
                                   'tuition_fee': tuition_fee,'apply':apply}, callback=self.parse_career)
    def parse_career(self,response):
        print(response.url)
        item = get_item1(ScrapyschoolEnglandItem1)
        overview = response.meta['overview']
        item['overview_en'] = overview
        modules = response.meta['modules']
        item['modules_en'] = modules
        ielts=response.meta['ielts']
        # department = response.meta['department']
        # item['department'] = department
        toefls=response.meta['toefl']
        rntry_requirements = response.meta['rntry_requirements']
        item['rntry_requirements'] = rntry_requirements
        tuition_fee = response.meta['tuition_fee']
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = '£'
        apply_documents_en = response.meta['apply']
        item['apply_documents_en'] = apply_documents_en
        career=response.xpath('//section[@class="content"]').extract()
        career=remove_class(career)
        item['career_en'] = career
        # print(career)
        department=response.xpath('//a[contains(text(),"Faculty")]/text()').extract()
        # print(department)
        department=''.join(department)
        department = response.xpath('//nav[@id="breadcrumb"]/ul/li/a/text()').extract()
        if department != []:
            department = department[-1]
        item['department'] = department
        item['university'] = 'University of Liverpool'
        item['url'] = response.url.replace('career-prospects','overview')
        item['location'] = 'Liverpool'
        programme= response.url.split('/')[-3]
        programme=programme.replace('-',' ').title()
        degree_name=re.findall('\sM[sarbm][a-z]{0,2}',programme)
        # print(degree_name)
        degree_name=' '.join(degree_name).strip()
        degree_name=degree_name.strip()
        programme=programme.replace(degree_name,'').strip()
        item['programme_en'] = programme
        item['degree_name'] = degree_name.replace('Mana','')
        # print(item['programme_en'])
        item['toefl_desc'] = ''.join(toefls)
        item['ielts_desc'] = ''.join(ielts)
        ielts=get_ielts(ielts)
        if ielts != {} and ielts != []:
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            item['ielts'] = ielts['IELTS']
        toefl=re.findall('\d{1,3}',''.join(toefls))
        if len(toefl)==4:
            item['toefl'] = toefl[0]
            item['toefl_l']=toefl[1]
            item['toefl_w'] = toefl[1]
            item['toefl_r'] = toefl[2]
            item['toefl_s'] = toefl[3]
        elif len(toefl)==2:
            toefl=list(map(int,toefl))
            item['toefl'] = max(toefl)
            item['toefl_l'] = min(toefl)
            item['toefl_w'] = min(toefl)
            item['toefl_r'] = min(toefl)
            item['toefl_s'] = min(toefl)
        duration=response.xpath('//li[contains(text(),"duration")]/span/text()').extract()
        # print(duration)
        for i in duration:
            if 'Full' not in i:
                del duration[duration.index(i)]
        duration=clear_duration(duration)
        # print(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']
        # yield item
        # print(item)