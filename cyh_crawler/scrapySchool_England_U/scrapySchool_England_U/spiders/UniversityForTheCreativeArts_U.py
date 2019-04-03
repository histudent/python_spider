# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
from scrapySchool_England_U.middlewares import *

class UniversityforthecreativeartsUSpider(scrapy.Spider):
    name = 'UniversityForTheCreativeArts_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.uca.ac.uk/study/courses/?subject=&campus=&studyLevel=undergraduate']

    def parse(self, response):
        urls=['https://www.uca.ac.uk/study/courses/ba-acting-farnham/',
'https://www.uca.ac.uk/study/courses/ba-acting-rochester/',
'https://www.uca.ac.uk/study/courses/ba-advertising/',
'https://www.uca.ac.uk/study/courses/ba-animation-4-year/',
'https://www.uca.ac.uk/study/courses/ba-animation/',
'https://www.uca.ac.uk/study/courses/ba-architecture/',
'https://www.uca.ac.uk/study/courses/ba-business-management/',
'https://www.uca.ac.uk/study/courses/ba-computer-animation-arts/',
'https://www.uca.ac.uk/study/courses/ba-fashion-4-year/',
'https://www.uca.ac.uk/study/courses/ba-fashion-atelier/',
'https://www.uca.ac.uk/study/courses/ba-fashion-design-4-year/',
'https://www.uca.ac.uk/study/courses/ba-fashion-design/',
'https://www.uca.ac.uk/study/courses/ba-fashion-journalism/',
'https://www.uca.ac.uk/study/courses/ba-fashion-management-marketing/',
'https://www.uca.ac.uk/study/courses/ba-fashion-media-promotion-4-year/',
'https://www.uca.ac.uk/study/courses/ba-fashion-media-promotion/',
'https://www.uca.ac.uk/study/courses/ba-fashion-photography/',
'https://www.uca.ac.uk/study/courses/ba-fashion-promotion-imaging/',
'https://www.uca.ac.uk/study/courses/ba-fashion-textiles/',
'https://www.uca.ac.uk/study/courses/ba-fashion/',
'https://www.uca.ac.uk/study/courses/ba-film-and-digital-arts/',
'https://www.uca.ac.uk/study/courses/ba-film-production-4-year/',
'https://www.uca.ac.uk/study/courses/ba-film-production/',
'https://www.uca.ac.uk/study/courses/ba-fine-art-4-year-canterbury/',
'https://www.uca.ac.uk/study/courses/ba-fine-art-canterbury/',
'https://www.uca.ac.uk/study/courses/ba-fine-art-farnham/',
'https://www.uca.ac.uk/study/courses/ba-games-art/',
'https://www.uca.ac.uk/study/courses/ba-games-design/',
'https://www.uca.ac.uk/study/courses/ba-glass-ceramics-jewellery-metalwork/',
'https://www.uca.ac.uk/study/courses/ba-graphic-design-canterbury/',
'https://www.uca.ac.uk/study/courses/ba-graphic-design-epsom-4-year/',
'https://www.uca.ac.uk/study/courses/ba-graphic-design-epsom/',
'https://www.uca.ac.uk/study/courses/ba-graphic-design-farnham/',
'https://www.uca.ac.uk/study/courses/ba-hand-embroidery/',
'https://www.uca.ac.uk/study/courses/ba-illustration-4-year/',
'https://www.uca.ac.uk/study/courses/ba-illustration-animation/',
'https://www.uca.ac.uk/study/courses/ba-illustration/',
'https://www.uca.ac.uk/study/courses/ba-interior-architecture-design-canterbury/',
'https://www.uca.ac.uk/study/courses/ba-interior-architecture-design-farnham/',
'https://www.uca.ac.uk/study/courses/ba-journalism-media-production/',
'https://www.uca.ac.uk/study/courses/ba-make-up-hair-design/',
'https://www.uca.ac.uk/study/courses/ba-marketing/',
'https://www.uca.ac.uk/study/courses/ba-music-composition-technology/',
'https://www.uca.ac.uk/study/courses/ba-music-journalism/',
'https://www.uca.ac.uk/study/courses/ba-music-marketing/',
'https://www.uca.ac.uk/study/courses/ba-photography-4-year/',
'https://www.uca.ac.uk/study/courses/ba-photography-farnham/',
'https://www.uca.ac.uk/study/courses/ba-photography-rochester/',
'https://www.uca.ac.uk/study/courses/ba-product-design/',
'https://www.uca.ac.uk/study/courses/ba-television-media-production/',
'https://www.uca.ac.uk/study/courses/ba-television-production/',
'https://www.uca.ac.uk/study/courses/ba-textile-design/',
'https://www.uca.ac.uk/study/courses/ba-theatre-design/',
'https://www.uca.ac.uk/study/courses/bsc-creative-computing/',
'https://www.uca.ac.uk/study/courses/bsc-games-technology/',]
        urls=set(urls)
        for u in urls:
            yield scrapy.Request(url=u,callback=self.parsess,meta={'url':u})
    def parsess(self,response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.meta['url']
        print(response.url)
        item['university']='University for the Creative Arts'
        alevel=response.xpath('//li[contains(text(),"tariff points")]/text()').extract()
        # print(alevel)
        if len(alevel)==2:
            item['alevel']=alevel[1]
        ib=response.xpath('//li[contains(text(),"International Baccalaureate")]/text()').extract()
        # print(ib)
        item['ib']=remove_class(ib).replace(', see more information about .','.')
        yield item
    def parses(self, response):
        pro_url=response.xpath('//div[@class="course-list js-course-list"]/div/a/@href').extract()
        # print(pro_url)
        for i in pro_url:
            full_url='https://www.uca.ac.uk'+i
            yield scrapy.Request(url=full_url,callback=self.parse_main)
    def parse_main(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'University for the Creative Arts'
        item['url'] = response.url
        programme = response.xpath('//h1/text()').extract()
        programme = ''.join(programme)
        # print(programme)
        item['programme_en'] = programme
        degree=response.xpath('//div[@class="cell heading"]/p/text()').extract()
        # print(degree)
        degree=''.join(degree).split(' - ')[0]
        # print(degree)
        item['degree_name']=degree
        duration = response.xpath('//p[contains(text(),"Length of study")]/following-sibling::p/text()').extract()
        duration = clear_duration(duration)
        # print(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']
        location = response.xpath('//p[contains(text(),"Campus")]/following-sibling::p/text()').extract()
        location = ''.join(location)
        item['location'] = location
        start_date = response.xpath('//p[contains(text(),"Start month")]/following-sibling::p/text()').extract()
        start_date = tracslateDate(start_date)
        # print(start_date)
        start_date = ','.join(start_date)
        item['start_date'] = start_date
        overview = response.xpath('//div[@class="cell overview"]').extract()
        overview = remove_class(overview)
        # print(overview)
        item['overview_en'] = overview
        modules = response.xpath(
            '//div[@id="syllabus"]/following-sibling::section[@class="article-content-area"][1]').extract()
        modules = remove_class(modules)
        # print(modules)
        item['modules_en'] = modules
        career = response.xpath('//div[contains(text(),"Career")]/following-sibling::div').extract()
        career = remove_class(career)
        # print(career)
        item['career_en'] = career
        item['ielts'] = '6'
        item['ielts_l'] = '5.5'
        item['ielts_s'] = '5.5'
        item['ielts_r'] = '5.5'
        item['ielts_w'] = '5.5'
        rntry = '<div><p>Chinese Senior School graduation with 12 years of completed school study, plus a recognised Foundation course.A transcript showing successful completion of one year of university study at a recognised Chinese university with average of 70%.</p></div>'
        # rntry = '\n'.join(rntry)
        item['require_chinese_en'] = rntry
        item['tuition_fee'] = '13540'
        item['tuition_fee_pre'] = '£'
        alevel=response.xpath('//*[contains(text(),"level")]/text()').extract()
        alevel=''.join(alevel)
        item['alevel']=alevel
        ib=response.xpath('//*[contains(text(),"nternational Baccalaureate")]/text()').extract()
        ib=''.join(ib)
        item['ib']=ib
        ucascode=response.xpath('//p[contains(text(),"UCAS code")]/following-sibling::p/text()').extract()
        ucascode=' '.join(ucascode).strip()
        item['ucascode']=ucascode
        portfolio=response.xpath('//h3[contains(text(),"Your portfolio")]/following-sibling::*').extract()
        item['portfolio_desc_en']=remove_class(portfolio)
        imgsrc=response.xpath('//h2[contains(text(),"This course is part of")]/../../following-sibling::div//img/@src').extract()
        # print(imgsrc)
        if imgsrc!=[]:
            department='Business School'
            item['department']=department

        # print(item)
        yield item