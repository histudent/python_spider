# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
from scrapySchool_England_U.middlewares import *
import requests
from lxml import etree
import requests
from lxml import etree
class HarperadamsuniveristyUSpider(scrapy.Spider):
    name = 'HarperAdamsUniveristy_U'
    allowed_domains = ['harper-adams.ac.uk']
    start_urls = ['https://www.harper-adams.ac.uk']
    base_url='https://www.harper-adams.ac.uk/courses/courses.cfm?layout=33&q=&type=foundation%20undergraduate&title=&area=&yoe=2019&cpd=&max=12&start='
    Title = ['1', '13', '25', '37','49']
    for i in Title:
        full_url=base_url+i
        # start_urls.append(full_url)
    def parse(self, response):
        urls=['https://www.harper-adams.ac.uk/courses/undergraduate/12/2019/animal-health-and-welfare',
'https://www.harper-adams.ac.uk/courses/undergraduate/13/2019/animal-production-science',
'https://www.harper-adams.ac.uk/courses/undergraduate/201097/2019/agrifood-marketing-with-business',
'https://www.harper-adams.ac.uk/courses/undergraduate/201141/2019/zoology-with-environmental-management',
'https://www.harper-adams.ac.uk/courses/undergraduate/201142/2019/zoology-with-entomology',
'https://www.harper-adams.ac.uk/courses/undergraduate/201136/2019/animal-behaviour-and-welfare-nonclinical',
'https://www.harper-adams.ac.uk/courses/undergraduate/201001/2019/wildlife-conservation-and-environmental-management',
'https://www.harper-adams.ac.uk/courses/undergraduate/201002/2019/veterinary-physiotherapy',
'https://www.harper-adams.ac.uk/courses/undergraduate/11/2019/animal-behaviour-and-welfare-clinical',
'https://www.harper-adams.ac.uk/courses/undergraduate/16/2019/veterinary-nursing-with-small-animal-rehabilitation',
'https://www.harper-adams.ac.uk/courses/undergraduate/201132/2019/veterinary-nursing-with-companion-animal-behaviour',
'https://www.harper-adams.ac.uk/courses/undergraduate/24/2019/countryside-and-environmental-management',
'https://www.harper-adams.ac.uk/courses/undergraduate/19/2019/business-management-with-marketing',
'https://www.harper-adams.ac.uk/courses/undergraduate/201061/2019/automotive-engineering-offhighway',
'https://www.harper-adams.ac.uk/courses/undergraduate/15/2019/bioveterinary-science',
'https://www.harper-adams.ac.uk/courses/undergraduate/201140/2019/applied-zoology',
'https://www.harper-adams.ac.uk/courses/undergraduate/201091/2019/bioveterinary-science',
'https://www.harper-adams.ac.uk/courses/undergraduate/201149/2019/applied-biology-with-biotechnology',
'https://www.harper-adams.ac.uk/courses/undergraduate/119/2019/veterinary-nursing',
'https://www.harper-adams.ac.uk/courses/undergraduate/75/2019/rural-property-management',
'https://www.harper-adams.ac.uk/courses/undergraduate/201062/2019/automotive-engineering-offhighway',
'https://www.harper-adams.ac.uk/courses/undergraduate/201052/2019/geography-and-environmental-management',
'https://www.harper-adams.ac.uk/courses/undergraduate/36/2019/rural-enterprise-and-land-management-realm',
'https://www.harper-adams.ac.uk/courses/undergraduate/201143/2019/real-estate',
'https://www.harper-adams.ac.uk/courses/undergraduate/201054/2019/mechanical-engineering',
'https://www.harper-adams.ac.uk/courses/undergraduate/26/2019/product-support-engineering',
'https://www.harper-adams.ac.uk/courses/undergraduate/201053/2019/mechanical-engineering',
'https://www.harper-adams.ac.uk/courses/undergraduate/201059/2019/food-technology-with-nutrition',
'https://www.harper-adams.ac.uk/courses/undergraduate/201056/2019/food-technology-and-product-development',
'https://www.harper-adams.ac.uk/courses/undergraduate/23/2019/countryside-management',
'https://www.harper-adams.ac.uk/courses/undergraduate/9/2019/agriculture-with-mechanisation',
'https://www.harper-adams.ac.uk/courses/undergraduate/7/2019/agriculture-with-farm-business-management',
'https://www.harper-adams.ac.uk/courses/undergraduate/4/2019/agriculture-with-crop-management',
'https://www.harper-adams.ac.uk/courses/undergraduate/3/2019/agriculture-with-animal-science',
'https://www.harper-adams.ac.uk/courses/undergraduate/201060/2019/food-manufacture-with-marketing',
'https://www.harper-adams.ac.uk/courses/undergraduate/1/2019/agriculture',
'https://www.harper-adams.ac.uk/courses/undergraduate/201013/2019/agricultural-engineering',
'https://www.harper-adams.ac.uk/courses/undergraduate/201012/2019/agricultural-engineering',
'https://www.harper-adams.ac.uk/courses/undergraduate/69/2019/agribusiness',
'https://www.harper-adams.ac.uk/courses/undergraduate/201146/2019/applied-biology',
'https://www.harper-adams.ac.uk/courses/undergraduate/201089/2019/animal-production-science',]
        urls=set(urls)
        for u in urls:
            yield scrapy.Request(url=u,callback=self.parsesss,meta={'url':u})
    def parsesss(self,response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.meta['url']
        item['university']='Harper Adams University'
        print(response.url)
        #https://www.harper-adams.ac.uk/courses/undergraduate/get-entry-requirements.cfm?id=12&qualification=alevels&year_of_entry=2019
        pro_id = response.url.split('/')[5]
        # print(pro_id)
        alevel_url='https://www.harper-adams.ac.uk/courses/undergraduate/get-entry-requirements.cfm?id=%s&qualification=alevels&year_of_entry=2019' % pro_id
        ib_url='https://www.harper-adams.ac.uk/courses/undergraduate/get-entry-requirements.cfm?id=%s&qualification=ib&year_of_entry=2019' % pro_id
        alevel_res=etree.HTML(requests.get(alevel_url).content)
        ib_res=etree.HTML(requests.get(ib_url).content)
        alevel=alevel_res.xpath('//ul//text()')
        ib=ib_res.xpath('//ul//text()')
        item['alevel']=remove_class(alevel)
        item['ib']=remove_class(ib)
        yield item
    def parsess(self, response):
        programme_url=response.xpath('//article/a/@href').extract()
        for i in programme_url:
            full_url='https://www.harper-adams.ac.uk'+i
            yield scrapy.Request(full_url,callback=self.parses)
    def parses(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['university']='Harper Adams University'
        item['url']=response.url
        item['location'] = 'Edgmond'
        duration = response.xpath('//h4[contains(text(),"Duration")]/following-sibling::p[1]//text()').extract()
        duration=clear_duration(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']
        StartDate = response.xpath('//h4[contains(text(),"Start")]/following-sibling::p/text()').extract()
        try:
            StartDate = tracslateDate(StartDate)
            StartDate = ','.join(StartDate)
            item["start_date"] = StartDate
        except:
            pass
        ucascode=response.xpath('//h4[contains(text(),"UCAS")]/following-sibling::p/text()').extract()[0]
        item['ucascode']=ucascode
        programme=response.xpath('//div[@class="page-heading"]/h1/text()').extract()
        programme=''.join(programme).strip()
        item['programme_en']=programme

        degree_name=response.xpath('//div[@id="course-title"]/h2/text()').extract()
        degree_name=''.join(degree_name).strip()
        # print(degree_name)
        item['degree_name']=degree_name

        pro_id=response.url.split('/')[5]
        # print(pro_id)
        modules_url='https://www.harper-adams.ac.uk/courses/undergraduate/get-module-table.cfm?year_of_entry=2019&route=1&id='+pro_id
        # print(modules_url)
        try:
            muRs=etree.HTML(requests.get(modules_url).content).xpath('//div/table')
            mo=''
            for i in muRs:
                mo+=etree.tostring(i,method='html',encoding='unicode')
            # print(mo)
            item['modules_en']=remove_class(mo)
        except:
            print(modules_url,'出现错误')
        overview=response.xpath('//div[@id="overview"]//div[@class="flex-width-eight"]').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en']=overview
        career=response.xpath('//div[@id="careers"]').extract()
        career=remove_class(career)
        # print(career)
        item['career_en']=career

        Assessment = response.xpath('//div[@id="teaching"]').extract()
        Assessment = remove_class(Assessment)
        item['assessment_en']=Assessment

        item['ielts'] = '6.0'
        item['ielts_l'] = '5.5'
        item['ielts_s'] = '5.5'
        item['ielts_r'] = '5.5'
        item['ielts_w'] = '5.5'
        item['toefl_r'] = '18'
        item['toefl_l'] = '18'
        item['toefl_s'] = '22'
        item['toefl_w'] = '20'
        item['toefl'] = '80'

        # print(item)
        yield item