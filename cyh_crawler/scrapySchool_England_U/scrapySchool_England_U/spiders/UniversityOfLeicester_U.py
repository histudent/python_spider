# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
from scrapySchool_England_U.middlewares import *
class UniversityofleicesterUSpider(scrapy.Spider):
    name = 'UniversityOfLeicester_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://le.ac.uk/courses?level=Undergraduate+2019&location=Campus-based&mode=Full-time&q=']

    def parse(self, response):
        urls=['https://le.ac.uk/courses/accounting-bsc/2019',
'https://le.ac.uk/courses/accounting-and-finance-bsc/2019',
'https://le.ac.uk/courses/aerospace-engineering-beng/2019',
'https://le.ac.uk/courses/aerospace-engineering-meng/2019',
'https://le.ac.uk/courses/aerospace-engineering-beng/2019',
'https://le.ac.uk/courses/aerospace-engineering-meng/2019',
'https://le.ac.uk/courses/aerospace-engineering-beng/2019',
'https://le.ac.uk/courses/aerospace-engineering-meng/2019',
'https://le.ac.uk/courses/american-studies-ba/2019',
'https://le.ac.uk/courses/american-studies-ba/2019',
'https://le.ac.uk/courses/ancient-history-ba/2019',
'https://le.ac.uk/courses/ancient-history-and-archaeology-ba/2019',
'https://le.ac.uk/courses/ancient-history-and-history-ba/2019',
'https://le.ac.uk/courses/applied-and-environmental-geology-mgeol/2019',
'https://le.ac.uk/courses/applied-and-environmental-geology-bsc/2019',
'https://le.ac.uk/courses/applied-psychology-bsc/2019',
'https://le.ac.uk/courses/archaeology-bsc/2019',
'https://le.ac.uk/courses/archaeology-ba/2019',
'https://le.ac.uk/courses/banking-and-finance-bsc/2019',
'https://le.ac.uk/courses/banking-and-finance-ba/2019',
'https://le.ac.uk/courses/biological-sciences-bsc/2019',
'https://le.ac.uk/courses/biological-sciences-biochemistry-bsc/2019',
'https://le.ac.uk/courses/biological-sciences-genetics-bsc/2019',
'https://le.ac.uk/courses/biological-sciences-microbiology-bsc/2019',
'https://le.ac.uk/courses/biological-sciences-neuroscience-bsc/2019',
'https://le.ac.uk/courses/biological-sciences-physiology-with-pharmacology-bsc/2019',
'https://le.ac.uk/courses/biological-sciences-zoology-bsc/2019',
'https://le.ac.uk/courses/business-economics-ba/2019',
'https://le.ac.uk/courses/business-economics-bsc/2019',
'https://le.ac.uk/courses/chemistry-mchem/2019',
'https://le.ac.uk/courses/chemistry-bsc/2019',
'https://le.ac.uk/courses/chemistry-with-forensic-science-bsc/2019',
'https://le.ac.uk/courses/chemistry-with-forensic-science-mchem/2019',
'https://le.ac.uk/courses/chemistry-with-forensic-science-mchem/2019',
'https://le.ac.uk/courses/chemistry-with-forensic-science-mchem/2019',
'https://le.ac.uk/courses/chemistry-mchem/2019',
'https://le.ac.uk/courses/chemistry-mchem/2019',
'https://le.ac.uk/courses/computer-science-bsc/2019',
'https://le.ac.uk/courses/computer-science-mcomp/2019',
'https://le.ac.uk/courses/computer-science-bsc/2019',
'https://le.ac.uk/courses/computer-science-bsc/2019',
'https://le.ac.uk/courses/contemporary-history-ba/2019',
'https://le.ac.uk/courses/criminology-bsc/2019',
'https://le.ac.uk/courses/economics-bsc/2019',
'https://le.ac.uk/courses/economics-ba/2019',
'https://le.ac.uk/courses/economics-and-accounting-ba/2019',
'https://le.ac.uk/courses/economics-and-accounting-bsc/2019',
'https://le.ac.uk/courses/electrical-and-electronic-engineering-beng',
'https://le.ac.uk/courses/electrical-and-electronic-engineering-meng/2019',
'https://le.ac.uk/courses/electrical-and-electronic-engineering-beng',
'https://le.ac.uk/courses/electrical-and-electronic-engineering-meng/2019',
'https://le.ac.uk/courses/electrical-and-electronic-engineering-beng',
'https://le.ac.uk/courses/electrical-and-electronic-engineering-meng/2019',
'https://le.ac.uk/courses/english-ba/2019',
'https://le.ac.uk/courses/english-and-american-studies-ba/2019',
'https://le.ac.uk/courses/english-and-french-law-llb/2019',
'https://le.ac.uk/courses/english-and-history-ba/2019',
'https://le.ac.uk/courses/european-studies-ba/2019',
'https://le.ac.uk/courses/film-and-media-studies-ba/2019',
'https://le.ac.uk/courses/film-studies-and-the-visual-arts-ba/2019',
'https://le.ac.uk/courses/film-studies-and-english-ba/2019',
'https://le.ac.uk/courses/financial-economics-bsc/2019',
'https://le.ac.uk/courses/financial-economics-ba/2019',
'https://le.ac.uk/courses/french-and-english-ba/2019',
'https://le.ac.uk/courses/french-and-italian-ba/2019',
'https://le.ac.uk/courses/french-and-spanish-ba/2019',
'https://le.ac.uk/courses/general-engineering-meng/2019',
'https://le.ac.uk/courses/general-engineering-beng/2019',
'https://le.ac.uk/courses/general-engineering-meng/2019',
'https://le.ac.uk/courses/general-engineering-beng/2019',
'https://le.ac.uk/courses/general-engineering-meng/2019',
'https://le.ac.uk/courses/general-engineering-beng/2019',
'https://le.ac.uk/courses/geography-ba/2019',
'https://le.ac.uk/courses/geography-bsc/2019',
'https://le.ac.uk/courses/geology-bsc/2019',
'https://le.ac.uk/courses/geology-mgeol/2019',
'https://le.ac.uk/courses/geology-with-geophysics-mgeol/2019',
'https://le.ac.uk/courses/geology-with-geophysics-bsc/2019',
'https://le.ac.uk/courses/geology-with-palaeontology-bsc/2019',
'https://le.ac.uk/courses/geology-with-palaeontology-mgeol/2019',
'https://le.ac.uk/courses/history-ba/2019',
'https://le.ac.uk/courses/history-and-american-studies-ba/2019',
'https://le.ac.uk/courses/history-and-archaeology-ba/2019',
'https://le.ac.uk/courses/history-and-politics-ba/2019',
'https://le.ac.uk/courses/history-of-art-ba/2019',
'https://le.ac.uk/courses/history-of-art-and-english-ba/2019',
'https://le.ac.uk/courses/human-geography-ba/2019',
'https://le.ac.uk/courses/human-resource-management-ba/2019',
'https://le.ac.uk/courses/international-relations-ba/2019',
'https://le.ac.uk/courses/international-relations-and-history-ba/2019',
'https://le.ac.uk/courses/italian-and-english-ba/2019',
'https://le.ac.uk/courses/italian-and-spanish-ba/2019',
'https://le.ac.uk/courses/journalism-ba/2019',
'https://le.ac.uk/courses/law-llb/2019',
'https://le.ac.uk/courses/law-with-a-modern-language-llb/2019',
'https://le.ac.uk/courses/law-and-criminology-llb/2019',
'https://le.ac.uk/courses/law-with-politics-llb/2019',
'https://le.ac.uk/courses/major-in-accounting-and-finance-bsc/2019',
'https://le.ac.uk/courses/major-in-archaeology-ba/2019',
'https://le.ac.uk/courses/major-in-computer-science-bsc/2019',
'https://le.ac.uk/courses/major-in-criminology-ba/2019',
'https://le.ac.uk/courses/major-in-english-literature-ba/2019',
'https://le.ac.uk/courses/major-in-film-studies-ba/2019',
'https://le.ac.uk/courses/major-in-french-studies-ba/2019',
'https://le.ac.uk/courses/major-in-history-ba/2019',
'https://le.ac.uk/courses/major-in-history-of-art-ba/2019',
'https://le.ac.uk/courses/major-in-human-geography-ba/2019',
'https://le.ac.uk/courses/major-in-human-resource-management-ba/2019',
'https://le.ac.uk/courses/major-in-international-relations-ba/2019',
'https://le.ac.uk/courses/major-in-italian-studies-ba/2019',
'https://le.ac.uk/courses/major-in-journalism/2019',
'https://le.ac.uk/courses/major-in-management-studies-ba/2019',
'https://le.ac.uk/courses/major-in-marketing-ba/2019',
'https://le.ac.uk/courses/major-in-mathematics-bsc/2019',
'https://le.ac.uk/courses/major-in-media-studies-ba/2019',
'https://le.ac.uk/courses/major-in-politics-ba/2019',
'https://le.ac.uk/courses/major-in-sociology-ba/2019',
'https://le.ac.uk/courses/major-in-spanish-and-latin-american-studies-ba/2019',
'https://le.ac.uk/courses/management-studies-ba/2019',
'https://le.ac.uk/courses/marketing-ba/2019',
'https://le.ac.uk/courses/mathematics-mmath/2019',
'https://le.ac.uk/courses/mathematics-ba-bsc/2019',
'https://le.ac.uk/courses/mathematics-and-actuarial-science-bsc/2019',
'https://le.ac.uk/courses/mathematics-ba-bsc/2019',
'https://le.ac.uk/courses/mathematics-mmath/2019',
'https://le.ac.uk/courses/mathematics-ba-bsc/2019',
'https://le.ac.uk/courses/mechanical-engineering-meng/2019',
'https://le.ac.uk/courses/mechanical-engineering-beng/2019',
'https://le.ac.uk/courses/mechanical-engineering-meng/2019',
'https://le.ac.uk/courses/mechanical-engineering-beng/2019',
'https://le.ac.uk/courses/mechanical-engineering-meng/2019',
'https://le.ac.uk/courses/mechanical-engineering-beng/2019',
'https://le.ac.uk/courses/media-and-communication-ba/2019',
'https://le.ac.uk/courses/media-and-society-ba/2019',
'https://le.ac.uk/courses/medical-biochemistry-bsc/2019',
'https://le.ac.uk/courses/medical-genetics-bsc/2019',
'https://le.ac.uk/courses/medical-microbiology-bsc/2019',
'https://le.ac.uk/courses/medical-physiology-bsc/2019',
'https://le.ac.uk/courses/medicine-mbchb/2019',
'https://le.ac.uk/courses/midwifery-msci/2019',
'https://le.ac.uk/courses/modern-language-studies-ba/2019',
'https://le.ac.uk/courses/modern-languages-and-translation-ba/2019',
'https://le.ac.uk/courses/modern-languages-with-film-studies-ba/2019',
'https://le.ac.uk/courses/modern-languages-with-management-ba/2019',
'https://le.ac.uk/courses/modern-languages-with-translation-ba/2019',
'https://le.ac.uk/courses/natural-sciences-bsc/2019',
'https://le.ac.uk/courses/natural-sciences-msci/2019',
'https://le.ac.uk/courses/nursing-msci-adult/2019',
'https://le.ac.uk/courses/nursing-msci-child/2019',
'https://le.ac.uk/courses/operating-department-practice-bsc/2019',
'https://le.ac.uk/courses/pharmaceutical-chemistry-mchem/2019',
'https://le.ac.uk/courses/pharmaceutical-chemistry-bsc/2019',
'https://le.ac.uk/courses/pharmaceutical-chemistry-mchem/2019',
'https://le.ac.uk/courses/pharmaceutical-chemistry-mchem/2019',
'https://le.ac.uk/courses/physical-geography-bsc/2019',
'https://le.ac.uk/courses/physics-mphys/2019',
'https://le.ac.uk/courses/physics-bsc/2019',
'https://le.ac.uk/courses/physics-with-astrophysics-mphys/2019',
'https://le.ac.uk/courses/physics-with-astrophysics-bsc/2019',
'https://le.ac.uk/courses/physics-with-space-science-bsc/2019',
'https://le.ac.uk/courses/physics-with-space-science-mphys/2019',
'https://le.ac.uk/courses/physiotherapy-bsc/2019',
'https://le.ac.uk/courses/politics-ba/2019',
'https://le.ac.uk/courses/politics-and-economics-ba/2019',
'https://le.ac.uk/courses/politics-and-international-relations-ba/2019',
'https://le.ac.uk/courses/politics-and-sociology-ba/2019',
'https://le.ac.uk/courses/psychology-bsc/2019',
'https://le.ac.uk/courses/psychology-with-cognitive-neuroscience-bsc/2019',
'https://le.ac.uk/courses/sociology-ba/2019',
'https://le.ac.uk/courses/software-engineering-bsc/2019',
'https://le.ac.uk/courses/software-engineering-bsc/2019',
'https://le.ac.uk/courses/software-engineering-bsc/2019',
'https://le.ac.uk/courses/spanish-and-english-ba/2019',]
        urls=set(urls)
        for u in urls:
            yield scrapy.Request(url=u,callback=self.parsess,meta={'url':u})
    def parsess(self,response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.meta['url']
        item['university']='University of Leicester'
        print(response.url)
        alevel=response.xpath('//strong[contains(text(),"A/AS-levels")]/..//text()|//strong[contains(text(),"EPQ with A-levels")]/..//text()').extract()
        ib=response.xpath('//strong[contains(text(),"International Baccalaureate")]/..//text()').extract()
        item['alevel']=remove_class(alevel)
        item['ib']=remove_class(ib)
        yield item


    def parses(self, response):
        # print('列表页',response.url)
        pro_url=response.xpath('//h4/a/@href').extract()
        for i in pro_url:
            yield scrapy.Request(url=i, callback=self.parse_main)
        next_page = response.xpath('//a[@aria-label="Next"]/@href').extract()
        if next_page != []:
            next_url = 'https://le.ac.uk/courses' + next_page[0]
            yield scrapy.Request(url=next_url, callback=self.parse)
    def parse_main(self, response):
        item=get_item1(ScrapyschoolEnglandItem)
        print('详情页',response.url)

        item['university'] = 'University of Leicester'
        item['url'] = response.url
        item['tuition_fee_pre'] = '£'

        department = response.xpath('//dt[contains(text(),"Department")]/following-sibling::dd/text()').extract()
        department = ''.join(department).strip()
        # print(department)
        item['department'] = department

        overview = response.xpath('//h2[contains(text(),"Course description")]/following-sibling::*').extract()
        overview = remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        chinese_require = ["<p>If you are studying A-levels or the International Baccalaureate (IB) then you can begin from the first year of a Bachelors degree. Please see individual course pages for entry requirements.</p>",
"<p>If you have already completed the first year of an undergraduate degree at a Chinese university, you may be considered for entry to the first year of a Bachelors degree if you have studied relevant subjects.</p>",]
        chinese_require = remove_class(chinese_require)
        item['require_chinese_en'] = chinese_require

        alevels=response.xpath('//strong[contains(text(),"levels")]/..//text()').extract()
        alevels=remove_class(alevels)
        # print(alevels)
        item['alevel']=alevels

        ib=response.xpath('//strong[contains(text(),"International")]/..//text()').extract()
        ib=remove_class(ib)
        # print(ib)
        item['ib']=ib

        career = response.xpath('//div[@id="careers"]').extract()
        career = remove_class(career)
        # print(career)
        item['career_en'] = career

        modules = response.xpath('//div[@id="course-structure"]').extract()
        modules = remove_class(modules)
        # print(modules)
        item['modules_en'] = modules

        fee = response.xpath('//h3[contains(text(),"International Students")]/following-sibling::*//text()').extract()
        tuition_fee = getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee

        assessment = response.xpath('//h2[contains(text(),"Teaching and learning")]/following-sibling::div').extract()
        assessment = remove_class(assessment)
        # print(assessment)
        item['assessment_en'] = assessment

        ielts = response.xpath('//*[contains(text(),"IELTS")]//text()').extract()
        ielts = get_ielts(ielts)
        # print(ielts)
        if ielts != []:
            item['ielts'] = ielts['IELTS']
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']

        # print(item['ielts'],type(item['ielts']))
        if item['ielts']==6.0:
            item['toefl']=80
        elif item['ielts']==6.5:
            item['toefl']=90
        elif item['ielts']==7.0:
            item['toefl']=100
        if item['toefl']!=None:
            item['toefl_l']='17'
            item['toefl_s']='20'
            item['toefl_r']='18'
            item['toefl_w']='17'

        programme = response.xpath('//span[contains(text(),"Course")]/following-sibling::span/text()').extract()
        # print(programme)
        degree_name = response.xpath(
            '//span[contains(text(),"Qualification")]/following-sibling::span/text()').extract()
        # print(degree_name)
        duration = response.xpath('//span[contains(text(),"Duration")]/following-sibling::span/text()').extract()
        # print(duration)
        start_date = response.xpath('//span[contains(text(),"UCAS Code")]/following-sibling::span/text()').extract()
        # print(start_date)
        for pro, deg, dur, sta in zip(programme, degree_name, duration, start_date):
            item['programme_en'] = pro
            item['degree_name'] = deg
            dura = clear_duration(dur)
            item['duration'] = dura['duration']
            item['duration_per'] = dura['duration_per']
            sta = ''.join(sta)
            item['ucascode'] = sta
            # print(item)
            yield item
