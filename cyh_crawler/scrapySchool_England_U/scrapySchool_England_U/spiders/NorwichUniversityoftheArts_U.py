# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
from scrapySchool_England_U.middlewares import *

class NorwichuniversityoftheartsUSpider(scrapy.Spider):
    name = 'NorwichUniversityoftheArts_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.nua.ac.uk/']

    def parse(self, response):
        urls=['https://www.nua.ac.uk/study-at-nua/courses/ba-hons-animation/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-architecture/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-design-publishing/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-fashion-communication-promotion/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-fashion/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-film-moving-image-production/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-film-moving-image-production/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-fine-art/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-fine-art/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-games-art-design/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-games-art-design/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-graphic-communication/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-graphic-design/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-graphic-design/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-illustration/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-illustration/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-interior-design/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-photography/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-photography/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-textile-design/',
'https://www.nua.ac.uk/study-at-nua/courses/ba-hons-vfx/',
'https://www.nua.ac.uk/study-at-nua/courses/bsc-hons-games-development/',
'https://www.nua.ac.uk/study-at-nua/courses/bsc-hons-interaction-design/',
'https://www.nua.ac.uk/study-at-nua/courses/bsc-hons-user-experience-design/',]
        urls=set(urls)
        for u in urls:
            yield scrapy.Request(url=u,callback=self.parsesss,meta={'url':u})
    def parsesss(self,response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.meta['url']
        item['university']='Norwich University of the Arts'

        alevel=response.xpath('//strong[contains(text(),"A / AS Levels – GCE")]/../text()').extract()
        print(alevel)
        item['alevel']=remove_class(alevel)
        ib=response.xpath('//strong[contains(text(),"International Baccalaureate")]/../text()').extract()
        item['ib']=remove_class(ib)

        yield item







    def parsess(self,response):
        pro_url=response.xpath('//h2[contains(text(),"Undergraduate")]/following-sibling::ul/li/a/@href').extract()
        for i in pro_url:
            yield scrapy.Request(i,callback=self.parses)
    #//h2[contains(text(),"Undergraduate")]/following-sibling::ul/li/a/@href
    def parses(self, response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        programme=response.xpath('//div[contains(@class,"contentRow")]/h1/text()').extract()
        deg=re.findall('[A-Za-z]+\s\(Hons\)',''.join(programme))
        # print(programme)
        # print(deg)
        programme=''.join(programme).replace(''.join(deg),'').strip()
        # print(programme)
        item['programme_en']=programme
        item['degree_name']=''.join(deg).strip()
        item['university'] = 'Norwich University of the Arts'
        item['url'] = response.url
        item['location'] = 'Norfolk'

        overview = response.xpath('//div[@class="headline"]').extract()
        overview = remove_class(overview)
        # print(overview)
        modules=response.xpath('//h2[contains(text(),"content")]/following-sibling::div').extract()
        modules=remove_class(modules)
        item['modules_en']=modules
        item['overview_en'] = overview
        career = response.xpath('//h3[contains(text(),"career")]/following-sibling::*[1]').extract()
        career = remove_class(career)
        item['career_en'] = career
        item['ielts_desc'] = "BA and MA applicants are required to have a minimum UKVI approved IELTS exam score of 6.0 overall, with a minimum of 5.5 in each section"
        item['ielts_l'] = '5.5'
        item['ielts_s'] = '5.5'
        item['ielts_r'] = '5.5'
        item['ielts_w'] = '5.5'
        item['ielts'] = '6.0'
        rntry = response.xpath('//div[@id="tabs-entry-requirements"]').extract()
        rntry = remove_class(rntry)
        # print(rntry)
        item['rntry_requirements'] = rntry
        portfolio_desc_en = response.xpath('//div[@id="tabs-portfolio-guidance"]').extract()
        portfolio_desc_en = remove_class(portfolio_desc_en)
        # print(portfolio_desc_en)
        item['apply_proces_en'] = portfolio_desc_en
        fee = response.xpath('//div[@id="tabs-fees-funding"]//text()').extract()
        tuition_fee = getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = '£'
        how_to_apply = response.xpath('//div[@id="how-to-apply"]').extract()
        item['apply_proces_en'] = remove_class(how_to_apply)
        # duration = response.xpath('//strong[contains(text(),"Course length")]/../text()').extract()
        # duration = clear_duration(duration)
        # # print(duration)
        # item['duration'] = duration['duration']
        item['duration_per'] = 1
        alevel=response.xpath('//strong[contains(text(),"A / AS Levels – GCE")]/../text()').extract()
        item['alevel']=''.join(alevel).strip()
        ib=response.xpath('//div[@id="tabs-entry-requirements"]//strong[contains(text(),"International Baccalaureate Diploma")]/../text()').extract()
        item['ib']=''.join(ib).strip()
        information=response.xpath('//div[contains(@class,"contentRow")]/h1/following-sibling::p//text()').extract()
        # print(information)
        ucas=re.findall('[A-Z0-9]{4}',''.join(information).replace('UCAS',''))
        # print(ucas)
        if len(ucas)==2:
            item['ucascode']=ucas[1]
            item['duration']=3
            yield item
        elif len(ucas)==3:
            for i in ucas:
                if i !='N39C':
                    item['ucascode']=i
                    if ucas.index(i)==1:
                        item['duration']=3
                    else:
                        item['duration']=4
                    yield item
        # print(item)