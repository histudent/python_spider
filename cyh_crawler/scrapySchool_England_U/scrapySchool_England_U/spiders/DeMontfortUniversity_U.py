# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
import re
class DemontfortuniversityUSpider(scrapy.Spider):
    name = 'DeMontfortUniversity_U'
    # allowed_domains = ['dmu.ac.uk']
    start_urls = ['https://www.dmu.ac.uk/study/courses/undergraduate-courses/undergraduate-courses.aspx']
    def parse(self, response):
        print('列表页链接',response.url)
        pro_url=response.xpath('//td[@class="sys_col-one"]/a/@href').extract()
        # print(pro_url)
        pro_name=response.xpath('//td[@class="sys_col-one"]/a/text()').extract()
        degree_name=response.xpath('//td[@class="sys_col-two"]/text()').extract()
        for pu,pa,dn in zip(pro_url,pro_name,degree_name):
            pus='https://www.dmu.ac.uk'+pu
            # print(pus)
            yield scrapy.Request(url=pus,callback=self.parses,meta={'programme':pa,'degree_name':dn})
        next_page=response.xpath('//a[contains(text(),"Next")]/@href').extract()
        # print(next_page)
        if next_page!=[]:
            next_url='https://www.dmu.ac.uk'+''.join(next_page)
            print(next_page)
            yield scrapy.Request(url=next_url,callback=self.parse)

    #补抓
    # def parse(self, response):
    #     item=get_item1(ScrapyschoolEnglandItem)
    #     item['url']=response.url
    #     item['university']='De Montfort University'
    #
    #     alevel=response.xpath('//li[contains(text(),"A-level")]/text()|'
    #                           '//li[contains(text(),"level")]/text()|'
    #                           '//li[contains(text(),"Level")]/text()|'
    #                           '//b[contains(text(),"A level")]/../following-sibling::*[1]//text()').extract()
    #
    #     ib = response.xpath('//li[contains(text(),"International Baccalaureate")]/text()|'
    #                         '//b[contains(text(),"International Baccalaureate")]/../following-sibling::*[1]//text()|'
    #                         '//span[contains(text(),"International Baccalaureate")]|'
    #                         '//p[contains(text(),"International Baccalaureate")]/text()').extract()
    #     item['ib']=remove_class(ib)
    #     item['alevel']=remove_class(alevel)
    #     yield item
    #正式开始
    def parses(self, response):
        print('专业链接',response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['university']='De Montfort University'
        item['url']=response.url
        item['location']='Leicester'

        programme=response.xpath('//h1/text()').extract()
        programme=''.join(programme).strip()
        deg=re.findall('[A-Za-z]+\s?\(Hons\)',programme)
        deg=''.join(deg).strip()
        programme=programme.replace(deg,'')
        # print(deg)
        deg=deg.replace('(','').replace(')','')
        # print(programme)
        item['degree_name']=deg
        item['programme_en']=programme
        # item['degree_name']=response.meta['degree_name']
        # item['programme_en']=response.meta['programme'].replace(response.meta['degree_name'],'')
        overview=response.xpath('//div[@class="block large-8 columns course-col2"]').extract()
        overview=remove_class(overview)
        item['overview_en']=overview

        rntry=response.xpath('//div[@class="row row--block course-section course-section--criteria"]').extract()
        rntry=remove_class(rntry)
        item['apply_desc_en']=rntry

        rntry=['<p>A-levels or a recognised Foundation Course.</p>',
'<p>Equivalent to Diploma of Higher Education (DipHE Standard (including BTEC and SQA HND Diploma) will be considered for second or third year entry, with a 75% average or GPA 2.</p>']
        item['require_chinese_en']=remove_class(rntry)

        modules=response.xpath('//div[@id="cycle-slideshow_course"]/div[position()=1]').extract()
        modules=remove_class(modules)
        item['modules_en']=modules

        assesssment=response.xpath('//div[@id="cycle-slideshow_course"]/div[position()=2]').extract()
        # print(assesssment)
        item['assessment_en']=remove_class(assesssment)
        career = response.xpath('//div[@class="row row--block course-section course-section--opps"]').extract()
        career = remove_class(career)
        item['career_en']=career

        IELTS = response.xpath('//*[contains(text(),"IELTS")]//text()').extract()
        item['ielts_desc']=''.join(IELTS).strip()
        ielts = get_ielts(IELTS)
        # print(ielts)
        try:
            if ielts != []:
                item['ielts_l'] = ielts['IELTS_L']
                item['ielts_s'] = ielts['IELTS_S']
                item['ielts_r'] = ielts['IELTS_R']
                item['ielts_w'] = ielts['IELTS_W']
                item['ielts'] = ielts['IELTS']
            else:
                ielts = re.findall('\d', ''.join(IELTS))
                ielts = list(set(ielts))
                ielts = list(map(int, ielts))
                item['ielts'] = min(ielts)
                item['ielts_l'] = min(ielts)
                item['ielts_s'] = min(ielts)
                item['ielts_r'] = min(ielts)
                item['ielts_w'] = min(ielts)
        except:
            pass
        # print('IELTS',item['ielts'])

        apply_d=["<div>A copy of your qualifications",
"A copy of your English language certificate  ",
"A photocopy of your passport",
"1 reference</div>",]
        apply_d='\n'.join(apply_d)
        item['apply_documents_en']=apply_d

        tuition_fee = response.xpath('//*[contains(text(),"£")]//text()').extract()
        tuition_fee = getTuition_fee(tuition_fee)
        item['tuition_fee']=tuition_fee

        duration=response.xpath('//*[contains(text(),"uration")]/..//text()').extract()
        try:
            duration=clear_duration(duration)
        except:
            duration={'duration_per': None, 'duration': None}
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']

        ib=response.xpath('//li[contains(text(),"International Baccalaureate")]/text()|'
                          '//b[contains(text(),"International Baccalaureate")]/../following-sibling::*[1]//text()|'
                          '//span[contains(text(),"International Baccalaureate")]').extract()
        ib=''.join(ib).strip()
        item['ib']=ib

        alevel=response.xpath('//li[contains(text(),"A-level")]/text()|//li[contains(text(),"level")]/text()|//li[contains(text(),"Level")]/text()|//p[contains(text(),"Level")]/..//text()|//b[contains(text(),"A level")]/../following-sibling::*[1]//text()').extract()
        # if alevel==[]:
        #     print(response.url)
        alevel=''.join(alevel).strip()
        item['alevel']=alevel


        ucascode=response.xpath('//b[contains(text(),"UCAS")]/../text()|//b[contains(text(),"UCAS")]/../following-sibling::*[1]//text()').extract()
        uca=re.findall('[A-Z0-9]{4}',''.join(ucascode))
        uca=list(set(uca))
        # if uca==[]:
        #     print(response.url)
        # else:
        #     print(uca)
        for ucas in uca:
            item['ucascode']=ucas.strip()
            yield item