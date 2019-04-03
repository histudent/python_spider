# -*- coding: utf-8 -*-
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.getItem import *
from scrapySchool_Canada_College.items import *
import requests
from lxml import etree
class ConfederationcolleageSpider(scrapy.Spider):
    name = 'ConfederationColleage'
    # allowed_domains = ['a.b']
    start_urls = ['http://www.confederationcollege.ca/program/aerospace-manufacturing-engineering-technician',
'http://www.confederationcollege.ca/program/aerospace-manufacturing-engineering-technology',
'http://www.confederationcollege.ca/program/aviation-technician-aircraft-maintenance',
'http://www.confederationcollege.ca/program/business',
'http://www.confederationcollege.ca/program/business-accounting',
'http://www.confederationcollege.ca/program/business-human-resources',
'http://www.confederationcollege.ca/program/business-marketing',
'http://www.confederationcollege.ca/program/business-administration-accounting',
'http://www.confederationcollege.ca/program/business-administration-human-resources',
'http://www.confederationcollege.ca/program/business-administration-marketing',
'http://www.confederationcollege.ca/program/business-fundamentals',
'http://www.confederationcollege.ca/program/carpentry-and-renovation-techniques',
'http://www.confederationcollege.ca/program/child-and-youth-care',
'http://www.confederationcollege.ca/program/child-and-youth-care-accelerated',
'http://www.confederationcollege.ca/program/civil-engineering-technician',
'http://www.confederationcollege.ca/program/civil-engineering-technology',
'http://www.confederationcollege.ca/program/computer-programmer',
'http://www.confederationcollege.ca/program/culinary-management',
'http://www.confederationcollege.ca/program/dental-assisting-levels-i-and-ii',
'http://www.confederationcollege.ca/program/dental-hygiene',
'http://www.confederationcollege.ca/program/developmental-services-worker',
'http://www.confederationcollege.ca/program/developmental-services-worker-accelerated',
'http://www.confederationcollege.ca/program/digital-marketing-and-marketing-analytics',
'http://www.confederationcollege.ca/program/digital-media-production',
'http://www.confederationcollege.ca/program/early-childhood-education',
'http://www.confederationcollege.ca/program/electrical-engineering-technology',
'http://www.confederationcollege.ca/program/electronics-engineering-technician-computers',
'http://www.confederationcollege.ca/program/embedded-systems',
'http://www.confederationcollege.ca/program/engineering-business-and-safety-management',
'http://www.confederationcollege.ca/program/english-second-language-esl',
'http://www.confederationcollege.ca/program/english-academic-purposes-eap',
'http://www.confederationcollege.ca/program/environmental-technician',
'http://www.confederationcollege.ca/program/film-production',
'http://www.confederationcollege.ca/program/forestry-technician-ecosystem-management',
'http://www.confederationcollege.ca/program/general-arts-and-science-certificate',
'http://www.confederationcollege.ca/program/general-arts-and-science-diploma',
'http://www.confederationcollege.ca/program/human-resources-management-full-time',
'http://www.confederationcollege.ca/program/information-communication-technology',
'http://www.confederationcollege.ca/program/industrial-manufacturing-processes',
'http://www.confederationcollege.ca/program/instrumentation-engineering-technician-process-automation-and-control',
'http://www.confederationcollege.ca/program/interactive-media-development',
'http://www.confederationcollege.ca/program/international-business-management',
'http://www.confederationcollege.ca/program/international-business-management-winter-start',
'http://www.confederationcollege.ca/program/leadership-healthcare-professionals',
'http://www.confederationcollege.ca/program/mechanical-engineering-technician',
'http://www.confederationcollege.ca/program/mechanical-techniques',
'http://www.confederationcollege.ca/program/medical-laboratory-assistant',
'http://www.confederationcollege.ca/program/mining-techniques',
'http://www.confederationcollege.ca/program/motive-power-techniques-automotive',
'http://www.confederationcollege.ca/program/motive-power-techniques-heavy-equipment',
'http://www.confederationcollege.ca/program/native-child-and-family-services',
'http://www.confederationcollege.ca/program/native-child-and-family-services-accelerated',
'http://www.confederationcollege.ca/program/office-administration-general-ft',
'http://www.confederationcollege.ca/program/personal-support-worker',
'http://www.confederationcollege.ca/program/personal-support-worker-compressed',
'http://www.confederationcollege.ca/program/power-engineering-technician',
'http://www.confederationcollege.ca/program/pre-health-sciences-pathways-to-advanced-diplomas-and-degrees',
'http://www.confederationcollege.ca/program/pre-health-sciences-pathways-to-certificates-and-diplomas',
'http://www.confederationcollege.ca/program/pre-technology-technologyaviation-stream',
'http://www.confederationcollege.ca/program/pre-technology-trades-stream',
'http://www.confederationcollege.ca/program/recreation-therapy',
'http://www.confederationcollege.ca/program/recreation-therapy-accelerated',
'http://www.confederationcollege.ca/program/tourism-travel-and-eco-adventure',
'http://www.confederationcollege.ca/program/welding-techniques',]

    def parse(self, response):
        item=get_item(ScrapyschoolCanadaCollegeItem)
        item['school_name']='Confederation College'
        item['url']=response.url
        print(response.url)
        majorname=response.xpath('//h1[@id="page-title"]/text()').extract()
        # print(majorname)
        item['major_name_en']=''.join(majorname).strip()
        item['apply_fee']='95.00'
        item['apply_pre']='$'
        item['ielts_desc']='6.0 (no band lower than 5.5)'
        item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']='6.0','5.5','5.5','5.5','5.5'
        item['toefl']='79'
        degree_name=response.xpath('//div[text()="Credential"]/following-sibling::span/text()').extract()
        # print(degree_name)
        item['degree_name']=''.join(degree_name)

        item['other']='1.没有平均分 2.课程设置和入学要求专业页面上不一定有 3.课程长度、学费、校区、学院和课程代码不一定有'

        code=response.xpath('//div[text()="Program Code"]/following-sibling::span/text()').extract()
        # print(code)
        item['programme_code']=''.join(code)

        department=response.xpath('//div[text()="Area of Interest"]/following-sibling::span/text()').extract()
        # print(department)
        item['department']=''.join(department)

        location=response.xpath('//div[text()="Location"]/following-sibling::span/text()').extract()
        # print(location)
        location=''.join(location).replace('Distance Education,','').strip()
        item['location']=location

        duration=response.xpath('//div[text()="Duration"]/following-sibling::span/text()').extract()
        # print(duration)
        duration=clear_duration(''.join(duration).replace('-',' '))
        # print(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']

        tuition=response.xpath('//div[text()="Tuition"]/following-sibling::span/text()').extract()
        # print(tuition)
        tuition_fee=''.join(tuition).replace('$2,988.00','12,300').replace('$4,482.00','18,450').replace('$3,735.00','14,739').replace('$3,090.00','14,994').replace('$5,308.00','13,838').replace('$3,296.00','12,814').replace('$4,120.00','14,196').replace('$4,278.00','16,830').replace('$8,682.00','18,206')
        # print(tuition_fee)
        item['tuition_fee']=tuition_fee
        item['tuition_fee_pre']='$'

        overview=response.xpath('//h2[contains(text(),"verview")]/following-sibling::div[2]').extract()
        # print(overview)
        item['overview_en']=remove_class(overview)

        career=response.xpath('//h3[contains(text(),"Employment Opportunities")]/following-sibling::div[1]').extract()
        # print(career)
        item['career_en']=remove_class(career)

        modulesurl=response.url+'/courses'
        modules=etree.HTML(requests.get(modulesurl).content).xpath('//h2[contains(text(),"Courses")]/following-sibling::*')
        mod=[]
        for mo in modules:
            mod+=etree.tostring(mo,method='html',encoding='unicode')
        item['modules_en']=remove_class(mod)

        entryurl=response.url+'/admission-requirements'
        entryrequire = etree.HTML(requests.get(entryurl).content).xpath('//h2[contains(text(),"dmission Requirement")]/following-sibling::*')
        entry = []
        for ent in entryrequire:
            entry += etree.tostring(ent, method='html', encoding='unicode')
        item['entry_requirements_en']=remove_class(entry)

        yield item