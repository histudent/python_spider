# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem

class LondonsouthbankuniversityUSpider(scrapy.Spider):
    name = 'LondonSouthBankUniversity_U'
    # allowed_domains = ['a.b']
    start_urls = ['http://www.lsbu.ac.uk/resources-course-finder/course-finder-for-ajax?meta_L_orsand[]=%22Undergraduate%22&']
    #补抓
    def parse(self, response):
        urls=['http://www.lsbu.ac.uk/courses/course-finder/marketing-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/petroleum-engineering-beng-hons',
'http://www.lsbu.ac.uk/courses/course-finder/information-technology-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/photography-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/operating-department-practice-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/petroleum-engineering-meng-hons',
'http://www.lsbu.ac.uk/courses/course-finder/midwifery-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/music-sound-design-ba-bsc',
'http://www.lsbu.ac.uk/courses/course-finder/mechanical-engineering-beng-hons',
'http://www.lsbu.ac.uk/courses/course-finder/mechanical-engineering-meng-hons',
'http://www.lsbu.ac.uk/courses/course-finder/marketing-supply-chain-procurement-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/marketing-law-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/marketing-human-resources-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/international-relations-sociology-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/international-relations-criminology-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/mental-health-nursing-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/marketing-advertising-digital-communications-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/marketing-enterprise-entrepreneurship-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/international-relations-politics-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/commercial-management-quantity-surveying-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/marketing-economics-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/human-nutrition-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/human-rights-llb-hons',
'http://www.lsbu.ac.uk/courses/course-finder/international-relations-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/human-nutrition-psychology-bsc',
'http://www.lsbu.ac.uk/courses/course-finder/human-geography-tourism-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/human-nutrition-exercise-science-bsc',
'http://www.lsbu.ac.uk/courses/course-finder/human-geography-planning-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/human-geography-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/history-sociology-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/history-politics-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/health-social-care-administration-management-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/history-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/economics-human-resources-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/forensic-science-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/film-studies-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/film-practice-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/family-law-llb-hons',
'http://www.lsbu.ac.uk/courses/course-finder/history-criminology-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/events-entertainment-management-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/english-creative-writing-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/housing-policy-and-practice',
'http://www.lsbu.ac.uk/courses/course-finder/engineering-product-design-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/entertainment-media-law-llb-hons',
'http://www.lsbu.ac.uk/courses/course-finder/electrical-engineering-and-power-electronics-meng-hons',
'http://www.lsbu.ac.uk/courses/course-finder/engineering-extended-degree',
'http://www.lsbu.ac.uk/courses/course-finder/education-studies',
'http://www.lsbu.ac.uk/courses/course-finder/economics-project-management-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/economics-marketing-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/economics-business-management-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/economics-law-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/electrical-engineering-and-power-electronics-beng-hons',
'http://www.lsbu.ac.uk/courses/course-finder/economics-accounting-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/drama-performance-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/bsc-hons-economics',
'http://www.lsbu.ac.uk/courses/course-finder/digital-design-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/diagnostic-radiography-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/drama-and-applied-theatre-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/criminology-law-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/data-science-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/criminology-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/criminal-law-llb-hons',
'http://www.lsbu.ac.uk/courses/course-finder/creative-advertising-marketing-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/construction-management-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/baking-science-and-technology-nutrition-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/music-industry-management-with-marketing-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/sport-exercise-science-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/quantity-surveying-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/urban-environmental-planning-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/sociology-with-politics-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/web-development-it-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/vfx-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/marketing-accounting-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/sports-coaching-analysis-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/sport-rehabilitation-integrated-masters',
'http://www.lsbu.ac.uk/courses/course-finder/tourism-hospitality-leisure-management-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/sociology-criminology-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/sociology-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/therapeutic-radiography-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/sport-rehabilitation-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/applied-sciences-extended-degree-programme',
'http://www.lsbu.ac.uk/courses/course-finder/marketing-finance-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/real-estate-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/psychology-forensic-psychology-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/psychology-with-criminology',
'http://www.lsbu.ac.uk/courses/course-finder/psychology-clinical-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/psychology-child-development-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/psychology-addiction-psychology-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/psychology-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/social-work-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/psychological-counselling-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/game-design-development-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/electrical-and-electronic-engineering-meng-hons',
'http://www.lsbu.ac.uk/courses/course-finder/psychology-health-and-nutrition-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/sport-psychology-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/applied-computing-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/advanced-vehicle-engineering-beng',
'http://www.lsbu.ac.uk/courses/course-finder/architectural-technology-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/adult-nursing-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/architectural-engineering-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/accounting-finance-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/baking-science-technology-new-product-development-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/architecture-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/chiropractic-masters',
'http://www.lsbu.ac.uk/courses/course-finder/business-management-human-resources',
'http://www.lsbu.ac.uk/courses/course-finder/childrens-nursing-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/built-environment-extended-degree',
'http://www.lsbu.ac.uk/courses/course-finder/chemical-process-engineering-beng-hons',
'http://www.lsbu.ac.uk/courses/course-finder/business-management-marketing-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/business-management-project-management-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/computer-systems-management-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/computer-systems-networks-engineering-meng-hons',
'http://www.lsbu.ac.uk/courses/course-finder/business-management-finance',
'http://www.lsbu.ac.uk/courses/course-finder/computer-systems-networks-engineering-beng-hons',
'http://www.lsbu.ac.uk/courses/course-finder/computer-engineering-meng-hons',
'http://www.lsbu.ac.uk/courses/course-finder/chemical-process-engineering-meng-hons',
'http://www.lsbu.ac.uk/courses/course-finder/computer-science-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/building-surveying-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/business-management-enterprise-entrepreneurship-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/civil-engineering-beng-hons',
'http://www.lsbu.ac.uk/courses/course-finder/computer-engineering-beng-hons',
'http://www.lsbu.ac.uk/courses/course-finder/business-information-technology-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/building-services-engineering-beng-hons',
'http://www.lsbu.ac.uk/courses/course-finder/bioscience-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/civil-engineering-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/business-management-accounting-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/business-management-with-law-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/criminology-with-politics-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/business-law-llb-hons',
'http://www.lsbu.ac.uk/courses/course-finder/economics-finance-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/business-management-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/economics-enterprise-entrepreneurship-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/electrical-electronic-engineering-beng-hons',
'http://www.lsbu.ac.uk/courses/course-finder/business-management-with-economics-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/criminology-psychology-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/education-studies-work-based',
'http://www.lsbu.ac.uk/courses/course-finder/health-visiting-community-public-health-nursing-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/fashion-promotion-marketing-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/human-geography-housing-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/learning-disability-nursing-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/law-criminology-llb-hons',
'http://www.lsbu.ac.uk/courses/course-finder/journalism-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/law-llb-hons',
'http://www.lsbu.ac.uk/courses/course-finder/marketing-public-relations-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/marketing-luxury-brand-management-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/marketing-project-management-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/occupational-therapy-bsc-hons-full-time',
'http://www.lsbu.ac.uk/courses/course-finder/physiotherapy-integrated-masters',
'http://www.lsbu.ac.uk/courses/course-finder/product-design-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/politics-ba-hons',
'http://www.lsbu.ac.uk/courses/course-finder/property-management-building-surveying-bsc-hons',
'http://www.lsbu.ac.uk/courses/course-finder/physiotherapy-bsc-hons',]
        urls=set(urls)
        for u in urls:
            yield scrapy.Request(url=u,callback=self.parsesss,meta={'url':u})
    def parsesss(self, response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.meta['url']
        item['university']='London South Bank University'
        print(response.url)
        alevel=response.xpath('//li[contains(text(),"A Level")]/text()').extract()
        print(alevel)
        alevel=' '.join(alevel).replace(':',' ').replace(' or',' ').strip()
        item['alevel']=remove_class(alevel)
        yield item
    def parsess(self, response):
        # print(response.url)
        pro_url=response.xpath('//span[contains(text(),"View course")]/../@href').extract()
        for i in pro_url:
            yield scrapy.Request(url=i,callback=self.parses)
        next_url=response.xpath('//a[contains(text(),"Next")]/@href').extract()
        if next_url!=[]:
            yield scrapy.Request(url=next_url[0],callback=self.parse)
    def parses(self,response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url'] = response.url
        item['university'] = 'London South Bank University'
        item['location'] = 'London'
        item['tuition_fee_pre'] = '£'
        pro = response.xpath('//div[@id="breadcrumbs"]//span/text()').extract()
        prog = pro[-1].split('-')
        if len(prog) == 2:
            programme = prog[0]
            degree_type = prog[1]
            degree_type = degree_type.strip()
            item['degree_name'] = degree_type
        else:
            programme = prog
        item['programme_en'] = programme
        tuition_fee=response.xpath('//td[contains(text(),"International")]//text()').extract()
        if tuition_fee==[]:
            print(response.url)
        else:
            print(response.url)
            print(tuition_fee)
            tuition_fee=tuition_fee[1]
        item['tuition_fee'] = getTuition_fee(tuition_fee)

        overview = response.xpath('//div[@id="tab_overview"]').extract()
        overview = remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        modules = response.xpath('//div[@id="tab_modules"]').extract()
        modules = remove_class(modules)
        # print(modules)
        item['modules_en'] = modules

        career = response.xpath('//div[@id="tab_employability"]').extract()
        career = remove_class(career)
        item['career_en'] = career

        rntry = response.xpath('//div[@id="tab_entry_requirements"]').extract()
        rntry = remove_class(rntry)
        item['rntry_requirements'] = rntry

        ielts = get_ielts(rntry)
        # print(ielts)
        if ielts != [] and ielts != {}:
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            item['ielts'] = ielts['IELTS']

        apply_desc_en = response.xpath('//div[@id="tab_how_to_apply"]').extract()
        apply_desc_en = remove_class(apply_desc_en)
        item['apply_desc_en'] = apply_desc_en

        duration = response.xpath('//td/span[contains(text(),"Duration")]/following-sibling::div/text()').extract()
        duration = clear_duration(duration)
        # print(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']

        start_date = response.xpath('//td/span[contains(text(),"Start")]/following-sibling::div/text()').extract()
        # start_date=tracslateDate(start_date)
        start_date=set(start_date)
        # print(start_date)
        star=[]
        for i in list(start_date):
            star.append(''.join(tracslateDate(i)))
        # print(star)
        star=','.join(star).strip()
        item['start_date']=star
        item['department'] = ''.join(response.xpath('//a[contains(text(),"School of")]/text()').extract())

        ucascode=response.xpath('//span[contains(text(),"Application code")]/following-sibling::div/text()').extract()
        ucascode=set(ucascode)
        ucascode=','.join(ucascode)
        # print(ucascode)
        item['ucascode']=ucascode

        apply_d='<ul><li>passport (photo and ID page)</li><li>copies of all UK visas (if applicable)</li><li>academic qualifications (transcripts and certificates)&nbsp;</li><li>reference letter(s)</li><li>personal statement</li></ul>'
        apply_d=remove_class(apply_d)
        item['apply_documents_en']=apply_d

        # print(item)
        yield item