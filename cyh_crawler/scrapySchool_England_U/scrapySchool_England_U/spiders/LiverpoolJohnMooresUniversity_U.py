# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem

class LiverpooljohnmooresuniversityUSpider(scrapy.Spider):
    name = 'LiverpoolJohnMooresUniversity_U'
    # allowed_domains = ['a.b']
    start_urls=['https://www.ljmu.ac.uk/study/courses?coursetypes=undergraduate']
    def parse(self, response):
        programme=response.xpath('//h3/a/text()').extract()
        degree_name=response.xpath('//h2/text()').extract()
        ucascode=response.xpath('//strong[contains(text(),"UCAS")]/text()').extract()
        pro_url = response.xpath('//a[contains(text(),"Find out more")]/@href').extract()
        for i,pro,deg,uca in zip(pro_url,programme,degree_name,ucascode):
            fullurl = 'https://www.ljmu.ac.uk' + i
            yield scrapy.Request(url=fullurl, callback=self.parses,meta={'programme':pro,'degree_name':deg,'ucascode':uca})
        next_page = response.xpath('//span[contains(text(),"Next Page")]/../@href').extract()
        if next_page != []:
            full_url = 'https://www.ljmu.ac.uk/courses/searchresults' + ''.join(next_page)
            yield scrapy.Request(url=full_url, callback=self.parse)
    def parses(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'Liverpool John Moores University'
        item['url'] = response.url
        item['location'] = 'Liverpool'
        programme=response.xpath('//h1[@id="google-course-markup-name"]/text()').extract()
        programme=''.join(programme)
        deg=re.findall('[A-Za-z].*\(Hons\)',programme)
        prog=programme.replace(''.join(deg),'').strip()
        item['degree_name']=''.join(deg)
        item['programme_en']=prog
        ucascode=response.xpath('//div[@class="m-course-options-content"]/p[contains(text(),"UCAS")]/text()').extract()
        ucascode=''.join(ucascode).replace('UCAS code:','').strip()
        item['ucascode']=ucascode
        duration=response.xpath('//h3[contains(text(),"Study mode")]/following-sibling::div//text()').extract()
        dura=clear_duration(duration)
        duration=''.join(duration).strip()
        item['duration']=duration
        item['duration_per']=dura['duration_per']
        overview=response.xpath('//div[@data-mh="course-overview"]').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en']=overview
        modules=response.xpath('//h2[contains(text(),"What you will study on this degree")]/../following-sibling::div').extract()
        modules=remove_class(modules)
        # print(modules)
        item['modules_en']=modules
        assessment=response.xpath('//h2[contains(text(),"Teaching and learning")]/following-sibling::*').extract()
        assessment=remove_class(assessment)
        item['assessment_en']=assessment
        item['application_open_date']='2019-10'
        ielts=response.xpath('//strong[contains(text(),"IELTS")]/following-sibling::p[1]/text()').extract()
        item['ielts_desc']=remove_class(ielts)
        ielts=get_ielts(ielts)
        try:
            if ielts!=[]:
                item['ielts']=ielts['IELTS']
                item['ielts_l']=ielts['IELTS_L']
                item['ielts_s']=ielts['IELTS_S']
                item['ielts_r']=ielts['IELTS_R']
                item['ielts_w']=ielts['IELTS_W']
        except:
            pass
        alevel=response.xpath('//h3[contains(text(),"A Levels")]/following-sibling::div[1]//text()').extract()
        alevel=remove_class(alevel)
        item['alevel']=alevel
        ib=response.xpath('//h3[contains(text(),"International Bacc")]/following-sibling::div[1]//text()').extract()
        ib=remove_class(ib)
        # print(ib)
        item['ib']=ib
        career=response.xpath('//h2[contains(text(),"Career prospects")]/../following-sibling::*').extract()
        career=remove_class(career)
        item['career_en']=career

        yield item


