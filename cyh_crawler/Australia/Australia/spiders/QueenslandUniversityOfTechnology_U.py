# -*- coding: utf-8 -*-
import scrapy,json
import requests
from lxml import etree
import json
from Australia.middlewares import *
from Australia.items import AustraliaItem
class QueenslanduniversityoftechnologyUSpider(scrapy.Spider):
    name = 'QueenslandUniversityOfTechnology_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.qut.edu.au/courses/bachelor-of-creative-industries',
'https://www.qut.edu.au/courses/bachelor-of-fine-arts-acting',
'https://www.qut.edu.au/courses/bachelor-of-fine-arts-animation',
'https://www.qut.edu.au/courses/bachelor-of-fine-arts-creative-writing',
'https://www.qut.edu.au/courses/bachelor-of-fine-arts-dance-performance',
'https://www.qut.edu.au/courses/bachelor-of-fine-arts-dance',
'https://www.qut.edu.au/courses/bachelor-of-fine-arts-drama',
'https://www.qut.edu.au/courses/bachelor-of-fine-arts-film-screen-and-new-media',
'https://www.qut.edu.au/courses/bachelor-of-fine-arts-music',
'https://www.qut.edu.au/courses/bachelor-of-fine-arts-technical-production',
'https://www.qut.edu.au/courses/bachelor-of-fine-arts-visual-arts',
'https://www.qut.edu.au/courses/bachelor-of-communication-advertising-and-public-relations',
'https://www.qut.edu.au/courses/bachelor-of-communication-digital-media',
'https://www.qut.edu.au/courses/bachelor-of-communication-entertainment-industries',
'https://www.qut.edu.au/courses/bachelor-of-communication-journalism',
'https://www.qut.edu.au/courses/bachelor-of-communication-professional-communication',
'https://www.qut.edu.au/courses/bachelor-of-creative-industries',
'https://www.qut.edu.au/courses/bachelor-of-fine-arts-creative-writing',
'https://www.qut.edu.au/courses/bachelor-of-creative-industries',
'https://www.qut.edu.au/courses/bachelor-of-design-architecture',
'https://www.qut.edu.au/courses/bachelor-of-design-fashion',
'https://www.qut.edu.au/courses/bachelor-of-design-honours-architectural-studies-advanced-standing-entry',
'https://www.qut.edu.au/courses/bachelor-of-design-industrial-design',
'https://www.qut.edu.au/courses/bachelor-of-design-interaction-design',
'https://www.qut.edu.au/courses/bachelor-of-design-interior-architecture',
'https://www.qut.edu.au/courses/bachelor-of-design-landscape-architecture',
'https://www.qut.edu.au/courses/bachelor-of-design-visual-communication',
'https://www.qut.edu.au/courses/bachelor-of-design-international-architecture',
'https://www.qut.edu.au/courses/bachelor-of-design-international-fashion',
'https://www.qut.edu.au/courses/bachelor-of-design-international-industrial-design',
'https://www.qut.edu.au/courses/bachelor-of-design-international-interaction-design',
'https://www.qut.edu.au/courses/bachelor-of-design-international-interior-architecture',
'https://www.qut.edu.au/courses/bachelor-of-design-international-landscape-architecture',
'https://www.qut.edu.au/courses/bachelor-of-design-international-visual-communication',
'https://www.qut.edu.au/courses/bachelor-of-fine-arts-animation',
'https://www.qut.edu.au/courses/bachelor-of-games-and-interactive-environments-animation',
'https://www.qut.edu.au/courses/bachelor-of-games-and-interactive-environments-game-design',
'https://www.qut.edu.au/courses/bachelor-of-design-architecture',
'https://www.qut.edu.au/courses/bachelor-of-design-honours-architectural-studies-advanced-standing-entry',
'https://www.qut.edu.au/courses/bachelor-of-design-interior-architecture',
'https://www.qut.edu.au/courses/bachelor-of-design-landscape-architecture',
'https://www.qut.edu.au/courses/bachelor-of-design-international-architecture',
'https://www.qut.edu.au/courses/bachelor-of-design-international-interior-architecture',
'https://www.qut.edu.au/courses/bachelor-of-design-international-landscape-architecture',
'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-civil',
'https://www.qut.edu.au/courses/bachelor-of-property-economics',
'https://www.qut.edu.au/courses/bachelor-of-urban-development-honours-construction-management',
'https://www.qut.edu.au/courses/bachelor-of-urban-development-honours-quantity-surveying-and-cost-engineering',
'https://www.qut.edu.au/courses/bachelor-of-urban-development-honours-urban-and-regional-planning',
'https://www.qut.edu.au/courses/bachelor-of-business-accountancy',
'https://www.qut.edu.au/courses/bachelor-of-business-deans-honours',
'https://www.qut.edu.au/courses/bachelor-of-business-economics',
'https://www.qut.edu.au/courses/bachelor-of-business-finance',
'https://www.qut.edu.au/courses/bachelor-of-business-financial-planning',
'https://www.qut.edu.au/courses/bachelor-of-business-international',
'https://www.qut.edu.au/courses/bachelor-of-property-economics',
'https://www.qut.edu.au/courses/bachelor-of-business-advertising',
'https://www.qut.edu.au/courses/bachelor-of-business-deans-honours',
'https://www.qut.edu.au/courses/bachelor-of-business-international-business',
'https://www.qut.edu.au/courses/bachelor-of-business-marketing',
'https://www.qut.edu.au/courses/bachelor-of-business-public-relations',
'https://www.qut.edu.au/courses/bachelor-of-business-international',
'https://www.qut.edu.au/courses/bachelor-of-communication-advertising-and-public-relations',
'https://www.qut.edu.au/courses/bachelor-of-business-deans-honours',
'https://www.qut.edu.au/courses/bachelor-of-business-public-relations',
'https://www.qut.edu.au/courses/bachelor-of-business-international',
'https://www.qut.edu.au/courses/bachelor-of-communication-advertising-and-public-relations',
'https://www.qut.edu.au/courses/bachelor-of-communication-digital-media',
'https://www.qut.edu.au/courses/bachelor-of-communication-entertainment-industries',
'https://www.qut.edu.au/courses/bachelor-of-communication-journalism',
'https://www.qut.edu.au/courses/bachelor-of-communication-professional-communication',
'https://www.qut.edu.au/courses/bachelor-of-business-deans-honours',
'https://www.qut.edu.au/courses/bachelor-of-business-international-business',
'https://www.qut.edu.au/courses/bachelor-of-business-international',
'https://www.qut.edu.au/courses/bachelor-of-business-deans-honours',
'https://www.qut.edu.au/courses/bachelor-of-business-human-resource-management',
'https://www.qut.edu.au/courses/bachelor-of-business-management',
'https://www.qut.edu.au/courses/bachelor-of-business-international',
'https://www.qut.edu.au/courses/bachelor-of-behavioural-science-psychology',
'https://www.qut.edu.au/courses/bachelor-of-clinical-exercise-physiology',
'https://www.qut.edu.au/courses/bachelor-of-health-information-management',
'https://www.qut.edu.au/courses/bachelor-of-medical-imaging-honours',
'https://www.qut.edu.au/courses/bachelor-of-nursing',
'https://www.qut.edu.au/courses/bachelor-of-nursing-graduate-entry',
'https://www.qut.edu.au/courses/bachelor-of-nutrition-science',
'https://www.qut.edu.au/courses/bachelor-of-nutrition-and-dietetics-honours',
'https://www.qut.edu.au/courses/bachelor-of-pharmacy-honours',
'https://www.qut.edu.au/courses/bachelor-of-podiatry',
'https://www.qut.edu.au/courses/bachelor-of-podiatry-graduate-entry',
'https://www.qut.edu.au/courses/bachelor-of-social-work',
'https://www.qut.edu.au/courses/bachelor-of-sport-and-exercise-science',
'https://www.qut.edu.au/courses/bachelor-of-vision-science',
'https://www.qut.edu.au/courses/bachelor-of-health-information-management',
'https://www.qut.edu.au/courses/bachelor-of-human-services',
'https://www.qut.edu.au/courses/bachelor-of-nursing',
'https://www.qut.edu.au/courses/bachelor-of-nursing-graduate-entry',
'https://www.qut.edu.au/courses/bachelor-of-nutrition-science',
'https://www.qut.edu.au/courses/bachelor-of-nutrition-and-dietetics-honours',
'https://www.qut.edu.au/courses/bachelor-of-public-health',
'https://www.qut.edu.au/courses/bachelor-of-social-work',
'https://www.qut.edu.au/courses/bachelor-of-behavioural-science-psychology',
'https://www.qut.edu.au/courses/bachelor-of-biomedical-science',
'https://www.qut.edu.au/courses/bachelor-of-clinical-exercise-physiology',
'https://www.qut.edu.au/courses/bachelor-of-medical-imaging-honours',
'https://www.qut.edu.au/courses/bachelor-of-medical-laboratory-science',
'https://www.qut.edu.au/courses/bachelor-of-nursing',
'https://www.qut.edu.au/courses/bachelor-of-nursing-graduate-entry',
'https://www.qut.edu.au/courses/bachelor-of-nutrition-science',
'https://www.qut.edu.au/courses/bachelor-of-pharmacy-honours',
'https://www.qut.edu.au/courses/bachelor-of-podiatry',
'https://www.qut.edu.au/courses/bachelor-of-sport-and-exercise-science',
'https://www.qut.edu.au/courses/bachelor-of-vision-science',
'https://www.qut.edu.au/courses/bachelor-of-laws-honours',
'https://www.qut.edu.au/courses/bachelor-of-laws-honours-graduate-entry',
'https://www.qut.edu.au/courses/bachelor-of-justice',
'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-computer-and-software-systems',
'https://www.qut.edu.au/courses/bachelor-of-games-and-interactive-environments-animation',
'https://www.qut.edu.au/courses/bachelor-of-games-and-interactive-environments-game-design',
'https://www.qut.edu.au/courses/bachelor-of-games-and-interactive-environments-software-technologies',
'https://www.qut.edu.au/courses/bachelor-of-health-information-management',
'https://www.qut.edu.au/courses/bachelor-of-information-technology-computer-science',
'https://www.qut.edu.au/courses/bachelor-of-information-technology-information-systems',
'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-chemical-process',
'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-civil',
'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-computer-and-software-systems',
'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-electrical-and-aerospace',
'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-electrical',
'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-mechanical',
'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-mechatronics',
'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-medical',
'https://www.qut.edu.au/courses/bachelor-of-games-and-interactive-environments-animation',
'https://www.qut.edu.au/courses/bachelor-of-games-and-interactive-environments-game-design',
'https://www.qut.edu.au/courses/bachelor-of-games-and-interactive-environments-software-technologies',
'https://www.qut.edu.au/courses/bachelor-of-health-information-management',
'https://www.qut.edu.au/courses/bachelor-of-information-technology-information-systems',
'https://www.qut.edu.au/courses/bachelor-of-mathematics-applied-and-computational-mathematics',
'https://www.qut.edu.au/courses/bachelor-of-mathematics-operations-research',
'https://www.qut.edu.au/courses/bachelor-of-mathematics-statistics',
'https://www.qut.edu.au/courses/bachelor-of-science-biological-sciences',
'https://www.qut.edu.au/courses/bachelor-of-science-chemistry',
'https://www.qut.edu.au/courses/bachelor-of-science-earth-science',
'https://www.qut.edu.au/courses/bachelor-of-science-environmental-science',
'https://www.qut.edu.au/courses/bachelor-of-science-physics',
'https://www.qut.edu.au/courses/bachelor-of-education-early-childhood',
'https://www.qut.edu.au/courses/bachelor-of-education-primary',
'https://www.qut.edu.au/courses/bachelor-of-education-secondary',]
    start_urls = list(set(start_urls))

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

        item['degree_type']='1'
        # print(item)
        yield item
