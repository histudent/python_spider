# -*- coding: utf-8 -*-
import scrapy
from Australia.items import AustraliaItem
from Australia.middlewares import *
import requests
from lxml import etree
class QueenslanduniversityoftechnologyPSpider(scrapy.Spider):
    name = 'QueenslandUniversityOfTechnology_P'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.qut.edu.au/courses/master-of-applied-law',
'https://www.qut.edu.au/courses/master-of-laws',
'https://www.qut.edu.au/courses/master-of-laws-in-intellectual-property',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-advanced-practice-nursing',
'https://www.qut.edu.au/courses/master-of-clinical-psychology',
'https://www.qut.edu.au/courses/master-of-counselling',
'https://www.qut.edu.au/courses/master-of-nurse-practitioner',
'https://www.qut.edu.au/courses/master-of-optometry',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-psychology-educational-and-developmental',
'https://www.qut.edu.au/courses/master-of-social-work-qualifying',
'https://www.qut.edu.au/courses/master-of-advanced-practice-nursing',
'https://www.qut.edu.au/courses/master-of-counselling',
'https://www.qut.edu.au/courses/master-of-health-management',
'https://www.qut.edu.au/courses/master-of-health-safety-and-environment',
'https://www.qut.edu.au/courses/master-of-nurse-practitioner',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-public-health',
'https://www.qut.edu.au/courses/master-of-social-work-qualifying',
'https://www.qut.edu.au/courses/master-of-advanced-practice-nursing',
'https://www.qut.edu.au/courses/master-of-applied-science-medical-physics',
'https://www.qut.edu.au/courses/master-of-clinical-psychology',
'https://www.qut.edu.au/courses/master-of-diagnostic-genomics',
'https://www.qut.edu.au/courses/master-of-nurse-practitioner',
'https://www.qut.edu.au/courses/master-of-optometry',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-psychology-educational-and-developmental',
'https://www.qut.edu.au/courses/master-of-teaching-early-childhood',
'https://www.qut.edu.au/courses/master-of-teaching-primary',
'https://www.qut.edu.au/courses/master-of-teaching-secondary',
'https://www.qut.edu.au/courses/master-of-education-double-major',
'https://www.qut.edu.au/courses/master-of-education-early-childhood-teaching',
'https://www.qut.edu.au/courses/master-of-education-early-years',
'https://www.qut.edu.au/courses/master-of-education-general-studies',
'https://www.qut.edu.au/courses/master-of-education-inclusive-education',
'https://www.qut.edu.au/courses/master-of-education-leadership-and-management',
'https://www.qut.edu.au/courses/master-of-education-stem-in-education',
'https://www.qut.edu.au/courses/master-of-education-school-guidance-and-counselling-general',
'https://www.qut.edu.au/courses/master-of-education-teaching-english-to-speakers-of-other-languages-tesol',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-digital-communication',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-architecture-DE83',
'https://www.qut.edu.au/courses/master-of-architecture',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-business-accounting',
'https://www.qut.edu.au/courses/master-of-business-applied-finance',
'https://www.qut.edu.au/courses/master-of-business-professional-accounting',
'https://www.qut.edu.au/courses/master-of-business-administration-digital',
'https://www.qut.edu.au/courses/master-of-business-administration-mba',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-business-integrated-marketing-communication',
'https://www.qut.edu.au/courses/master-of-business-marketing',
'https://www.qut.edu.au/courses/master-of-business-public-relations',
'https://www.qut.edu.au/courses/master-of-business-strategic-advertising',
'https://www.qut.edu.au/courses/master-of-business-administration-digital',
'https://www.qut.edu.au/courses/master-of-business-administration-mba',
'https://www.qut.edu.au/courses/master-of-business-master-of-business',
'https://www.qut.edu.au/courses/master-of-digital-communication',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-business-integrated-marketing-communication',
'https://www.qut.edu.au/courses/master-of-business-public-relations',
'https://www.qut.edu.au/courses/master-of-business-administration-digital',
'https://www.qut.edu.au/courses/master-of-business-administration-mba',
'https://www.qut.edu.au/courses/master-of-digital-communication',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-business-international-business',
'https://www.qut.edu.au/courses/master-of-business-administration-digital',
'https://www.qut.edu.au/courses/master-of-business-administration-mba',
'https://www.qut.edu.au/courses/master-of-business-master-of-business',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-business-administration-digital',
'https://www.qut.edu.au/courses/master-of-business-administration-mba',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-business-human-resource-management',
'https://www.qut.edu.au/courses/master-of-business-management',
'https://www.qut.edu.au/courses/master-of-business-administration-digital',
'https://www.qut.edu.au/courses/master-of-business-administration-mba',
'https://www.qut.edu.au/courses/master-of-business-process-management',
'https://www.qut.edu.au/courses/master-of-business-master-of-business',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-project-management',
'https://www.qut.edu.au/courses/master-of-business-philanthropy-and-nonprofit-studies',
'https://www.qut.edu.au/courses/master-of-business-administration-mba',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-architecture-DE83',
'https://www.qut.edu.au/courses/master-of-architecture',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-engineering-management',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-project-management',
'https://www.qut.edu.au/courses/master-of-business-process-management',
'https://www.qut.edu.au/courses/master-of-data-analytics',
'https://www.qut.edu.au/courses/master-of-information-technology',
'https://www.qut.edu.au/courses/master-of-information-technology-graduate-entry',
'https://www.qut.edu.au/courses/master-of-laws-in-intellectual-property',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-engineering',
'https://www.qut.edu.au/courses/master-of-engineering-management',
'https://www.qut.edu.au/courses/master-of-laws-in-intellectual-property',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-professional-engineering',
'https://www.qut.edu.au/courses/master-of-project-management',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-business-process-management',
'https://www.qut.edu.au/courses/master-of-data-analytics',
'https://www.qut.edu.au/courses/master-of-information-technology',
'https://www.qut.edu.au/courses/master-of-information-technology-graduate-entry',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-data-analytics',
'https://www.qut.edu.au/courses/master-of-philosophy',
'https://www.qut.edu.au/courses/master-of-applied-science-medical-physics',
'https://www.qut.edu.au/courses/master-of-philosophy',]
    start_urls = set(start_urls)
    def parse(self, response):
        item=get_item(AustraliaItem)
        item['university'] = 'Queensland University of Technology'
        item['url'] = response.url
        print(response.url)
        degree_name=response.xpath('//h1/span/text()').extract()
        # print(degree_name)
        duration=response.xpath('//dt[text()="Duration"]/following-sibling::dd[@data-course-audience="INT" and @class="col-sm-12"]/text()').extract()
        # print(duration)
        dura=re.findall('\d+\.?\d?',''.join(duration))
        # print(dura)
        item['duration']=','.join(dura)
        if 'year' in ''.join(duration):
            item['duration_per']='2'
        else:
            item['duration_per']='1'
        item['degree_name']=''.join(degree_name)
        programme=''.join(degree_name).split('Master of')[-1].strip()
        # print(programme)
        item['programme_en']=programme
        start_date=response.xpath('//dt[text()="Entry"]/following-sibling::dd[@data-course-audience="INT" and @class="col-sm-12"]/text()').extract()
        # print(start_date)
        start_date=tracslateDate(start_date)
        item['start_date']=','.join(start_date)
        location=response.xpath('//dt[text()="Campus"]/following-sibling::dd[@class="col-sm-12"]/text()').extract()
        item['location']=''.join(set(location))
        overview=response.xpath('//h2[@id="why-choose-this-course"]/following-sibling::p').extract()
        item['overview_en']=remove_class(overview)
        career=response.xpath('//div[@id="career-outcomes-tab"]').extract()
        item['career_en']=remove_class(career)
        modules=response.xpath('//div[@id="details-and-units-tab"]').extract()
        item['modules_en']=remove_class(modules)
        requirements=response.xpath('//div[@id="requirements-tab"]//div[contains(@class,"right")]').extract()
        item['rntry_requirements_en']=remove_class(requirements)
        ielts=response.xpath('//td[contains(text(),"IELTS")]/following-sibling::td[@id="elt-overall"]//text()').extract()
        # print(ielts)
        item['ielts']=remove_class(ielts)
        item['ielts_l']=remove_class(response.xpath('//td[contains(text(),"IELTS")]/following-sibling::td[@id="elt-listening"]//text()').extract())
        item['ielts_s']=remove_class(response.xpath('//td[contains(text(),"IELTS")]/following-sibling::td[@id="elt-speaking"]//text()').extract())
        item['ielts_r']=remove_class(response.xpath('//td[contains(text(),"IELTS")]/following-sibling::td[@id="elt-reading"]//text()').extract())
        item['ielts_w']=remove_class(response.xpath('//td[contains(text(),"IELTS")]/following-sibling::td[@id="elt-writing"]//text()').extract())
        item['toefl']=remove_class(response.xpath('//td[contains(text(),"TOEFL")]/following-sibling::td[@id="elt-overall"]//text()').extract())
        item['toefl_l']=remove_class(response.xpath('//td[contains(text(),"TOEFL")]/following-sibling::td[@id="elt-listening"]//text()').extract())
        item['toefl_s']=remove_class(response.xpath('//td[contains(text(),"TOEFL")]/following-sibling::td[@id="elt-speaking"]//text()').extract())
        item['toefl_r']=remove_class(response.xpath('//td[contains(text(),"TOEFL")]/following-sibling::td[@id="elt-reading"]//text()').extract())
        item['toefl_w']=remove_class(response.xpath('//td[contains(text(),"TOEFL")]/following-sibling::td[@id="elt-writing"]//text()').extract())

        tuition_fee=response.xpath('//div[@data-course-audience="INT"]//p[contains(text(),"$")]/text()').extract()
        # print(tuition_fee)
        item['tuition_fee']=''.join(tuition_fee).strip()
        item['tuition_fee_pre']='AUD$'

        item['degree_type']='2'
        yield item