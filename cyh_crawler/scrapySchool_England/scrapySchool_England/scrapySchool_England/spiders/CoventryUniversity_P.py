# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.middlewares import clear_duration,tracslateDate
from scrapySchool_England.clearSpace import clear_lianxu_space,clear_same_s
class CoventryuniversitySpider(scrapy.Spider):
    name = 'CoventryUniversity_P'
    allowed_domains = ['coventry.ac.uk']
    start_urls = ['https://www.coventry.ac.uk/study-at-coventry/az-course-list/?tab=2']
    def parse(self, response):
        urllist=response.xpath('//div[@class="break"]/a/@href').extract()
        for i in urllist:
            fullurl='https://www.coventry.ac.uk'+i+'?visitor=international'
            yield scrapy.Request(fullurl,callback=self.parses)

    def parses(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "Coventry University"
        item['url'] = response.url
        item['location'] = 'Coventry'
        item['tuition_fee_pre'] = '£'
        progremme=response.xpath('//h2[@class="padded-multiline"]//text()').extract()
        progremme=''.join(progremme).strip()
        # print(progremme)

        degree_name=re.findall('M[A-Z]+[a-z]*',progremme)
        # print(degree_name)
        degree_name=''.join(degree_name)
        item['degree_name'] = degree_name
        progremme=progremme.replace(degree_name,'').strip()
        item['programme_en'] = progremme

        duration=response.xpath('//h5[contains(text(),"Study options")]/../following-sibling::div[1]//text()').extract()

        item['duration'] = clear_duration(duration)['duration']
        item['duration_per'] = clear_duration(duration)['duration_per']

        mode=re.findall('full',''.join(duration))
        if mode!=[]:
            item['teach_time'] = 'fulltime'
        else:
            item['teach_time'] = 'parttime'
        fee=response.xpath('//h5[contains(text(),"Fee")]/../following-sibling::div[1]//text()').extract()
        tuition_fee=getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee

        start_date=response.xpath('//h5[contains(text(),"Start")]/../following-sibling::div[1]//text()').extract()
        start_date=tracslateDate(start_date)
        # print(start_date)
        start_date=','.join(start_date)
        item['start_date'] = start_date

        deparment=response.xpath('//h5[contains(text(),"Faculty")]/../following-sibling::div[1]//text()').extract()
        deparment=' '.join(deparment).strip()
        # print(deparment)
        item['department'] = deparment

        overview=response.xpath('//div[@id="overview-tab-pane"]/div[@class="container"]').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        modules=response.xpath('//h2[contains(text(),"Modules")]/following-sibling::*').extract()
        modules=remove_class(modules)
        # print(modules)
        item['modules_en'] = modules

        career=response.xpath('//div[@id="career-tab-pane"]').extract()
        career=remove_class(career)
        # print(career)
        item['career_en'] = career

        assessment=response.xpath('//div[@id="assessment-hide-reveal"]').extract()
        if assessment==[]:
            assessment=['  <div class="col-xs-12">',
'                                <p>Assessment will be through written coursework and a dissertation/portfolio.</p>',
'<p>Formative feedback opportunities will be provided throughout the course.</p>',
'                            </div>',
]
        item['assessment_en']=remove_class(assessment)
        rntry_requirement=response.xpath('//div[@id="offerInfo-international"]').extract()
        rntry_requirement=remove_class(rntry_requirement)
        # print(rntry_requirement)
        ielts=response.xpath('//strong[contains(text(),"English as a Foreign Language")]/../text()|//*[contains(text(),"IELTS")]//text()').extract()
        ielts = get_ielts(ielts)
        # print(ielts)
        if ielts != {} and ielts != []:
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            item['ielts'] = ielts['IELTS']
        item['rntry_requirements'] = rntry_requirement
        # print(item)
        yield item
