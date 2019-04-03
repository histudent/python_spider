# -*- coding: utf-8 -*-
import scrapy
from Australia.items import AustraliaItem
from Australia.middlewares import *
import requests
from lxml import etree

class LatrobeuniversityUSpider(scrapy.Spider):
    name = 'LaTrobeUniversity_U'
    pro_list=['http://www.latrobe.edu.au/courses/bachelor-of-business-accounting-and-finance',
'http://www.latrobe.edu.au/courses/bachelor-of-business',
'http://www.latrobe.edu.au/courses/bachelor-of-pharmacy-honours',
'http://www.latrobe.edu.au/courses/bachelor-of-biological-sciences',
'http://www.latrobe.edu.au/courses/bachelor-of-politics-philosophy-and-economics',
'http://www.latrobe.edu.au/courses/bachelor-of-media-and-communication',
'http://www.latrobe.edu.au/courses/bachelor-of-commerce',
'https://www.latrobe.edu.au/courses/bachelor-of-criminology',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce-bachelor-of-laws',
'https://www.latrobe.edu.au/courses/bachelor-of-criminology-bachelor-of-laws',
'https://www.latrobe.edu.au/courses/bachelor-of-criminology-bachelor-of-psychological-science',
'https://www.latrobe.edu.au/courses/bachelor-of-cybersecurity-bachelor-of-psychological-science',
'https://www.latrobe.edu.au/courses/bachelor-of-laws',
'https://www.latrobe.edu.au/courses/bachelor-of-laws-graduate-entry',
'https://www.latrobe.edu.au/courses/bachelor-of-laws-bachelor-of-arts',
'https://www.latrobe.edu.au/courses/bachelor-of-laws-bachelor-of-business',
'https://www.latrobe.edu.au/courses/bachelor-of-laws-bachelor-of-international-relations',
'https://www.latrobe.edu.au/courses/bachelor-of-laws-bachelor-of-media-and-communication',
'https://www.latrobe.edu.au/courses/bachelor-of-laws-bachelor-of-psychological-science',
'https://www.latrobe.edu.au/courses/bachelor-of-laws-bachelor-of-science',
'https://www.latrobe.edu.au/courses/bachelor-of-arts',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce',
'https://www.latrobe.edu.au/courses/bachelor-of-criminology',
'https://www.latrobe.edu.au/courses/bachelor-of-media-and-communication',
'https://www.latrobe.edu.au/courses/bachelor-of-psychological-science',
'https://www.latrobe.edu.au/courses/bachelor-of-science',
'https://www.latrobe.edu.au/courses/bachelor-of-arts-bachelor-of-health-sciences',
'https://www.latrobe.edu.au/courses/bachelor-of-arts-bachelor-of-science',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce-bachelor-of-arts',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce-bachelor-of-international-relations',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce-bachelor-of-laws',
'https://www.latrobe.edu.au/courses/bachelor-of-creative-arts',
'https://www.latrobe.edu.au/courses/bachelor-of-criminology-bachelor-of-laws',
'https://www.latrobe.edu.au/courses/bachelor-of-criminology-bachelor-of-psychological-science',
'https://www.latrobe.edu.au/courses/bachelor-of-international-relations',
'https://www.latrobe.edu.au/courses/bachelor-of-laws',
'https://www.latrobe.edu.au/courses/bachelor-of-laws-bachelor-of-arts',
'https://www.latrobe.edu.au/courses/bachelor-of-laws-bachelor-of-business',
'https://www.latrobe.edu.au/courses/bachelor-of-laws-bachelor-of-international-relations',
'https://www.latrobe.edu.au/courses/bachelor-of-laws-bachelor-of-media-and-communication',
'https://www.latrobe.edu.au/courses/bachelor-of-laws-bachelor-of-psychological-science',
'https://www.latrobe.edu.au/courses/bachelor-of-politics-philosophy-and-economics',
'https://www.latrobe.edu.au/courses/bachelor-of-psychology-honours',
'https://www.latrobe.edu.au/courses/bachelor-of-urban-rural-and-environmental-planning',
'https://www.latrobe.edu.au/courses/bachelor-of-accounting',
'https://www.latrobe.edu.au/courses/bachelor-of-business',
'https://www.latrobe.edu.au/courses/bachelor-of-business-event-management',
'https://www.latrobe.edu.au/courses/bachelor-of-business-marketing',
'https://www.latrobe.edu.au/courses/bachelor-of-business-sport-management',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce',
'https://www.latrobe.edu.au/courses/bachelor-of-finance',
'https://www.latrobe.edu.au/courses/bachelor-of-accounting-master-of-financial-analysis',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-business',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-business-management',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-business-marketing',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-information-technology',
'https://www.latrobe.edu.au/courses/bachelor-of-business-accounting-and-finance',
'https://www.latrobe.edu.au/courses/bachelor-of-business-accounting',
'https://www.latrobe.edu.au/courses/bachelor-of-business-agribusiness',
'https://www.latrobe.edu.au/courses/bachelor-of-business-event-management-marketing',
'https://www.latrobe.edu.au/courses/bachelor-of-business-human-resource-management',
'https://www.latrobe.edu.au/courses/bachelor-of-business-sport-development-and-management',
'https://www.latrobe.edu.au/courses/bachelor-of-business-tourism-and-hospitality',
'https://www.latrobe.edu.au/courses/bachelor-of-business-information-systems',
'https://www.latrobe.edu.au/courses/bachelor-of-business-information-systems-honours',
'https://www.latrobe.edu.au/courses/bachelor-of-business-bachelor-of-arts',
'https://www.latrobe.edu.au/courses/bachelor-of-business-master-of-management',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce-bachelor-of-agricultural-sciences',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce-bachelor-of-arts',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce-bachelor-of-biomedicine',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce-bachelor-of-computer-science',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce-bachelor-of-health-sciences',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce-bachelor-of-international-relations',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce-bachelor-of-laws',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce-bachelor-of-science',
'https://www.latrobe.edu.au/courses/bachelor-of-international-business',
'https://www.latrobe.edu.au/courses/bachelor-of-laws-bachelor-of-business',
'https://www.latrobe.edu.au/courses/bachelor-of-politics-philosophy-and-economics',
'https://www.latrobe.edu.au/courses/bachelor-of-science-bachelor-of-business',
'https://www.latrobe.edu.au/courses/bachelor-of-arts',
'https://www.latrobe.edu.au/courses/bachelor-of-arts-bachelor-of-health-sciences',
'https://www.latrobe.edu.au/courses/bachelor-of-arts-bachelor-of-science',
'https://www.latrobe.edu.au/courses/bachelor-of-early-childhood-and-primary-education',
'https://www.latrobe.edu.au/courses/bachelor-of-early-learning',
'https://www.latrobe.edu.au/courses/bachelor-of-education-primary',
'https://www.latrobe.edu.au/courses/bachelor-of-education-secondary',
'https://www.latrobe.edu.au/courses/bachelor-of-educational-studies',
'https://www.latrobe.edu.au/courses/bachelor-of-outdoor-education',
'https://www.latrobe.edu.au/courses/bachelor-of-outdoor-recreation-education',
'https://www.latrobe.edu.au/courses/bachelor-of-physical-health-and-outdoor-education',
'https://www.latrobe.edu.au/courses/bachelor-of-technology-education',
'https://www.latrobe.edu.au/courses/bachelor-of-biomedical-science',
'https://www.latrobe.edu.au/courses/bachelor-of-biomedicine',
'https://www.latrobe.edu.au/courses/bachelor-of-health-sciences',
'https://www.latrobe.edu.au/courses/bachelor-of-science',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-clinical-audiology',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-clinical-prosthetics-and-orthotics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-dietetic-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-occupational-therapy-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-orthoptics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-physiotherapy-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-podiatric-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-speech-pathology',
'https://www.latrobe.edu.au/courses/bachelor-of-arts-bachelor-of-health-sciences',
'https://www.latrobe.edu.au/courses/bachelor-of-community-services',
'https://www.latrobe.edu.au/courses/bachelor-of-exercise-science',
'https://www.latrobe.edu.au/courses/bachelor-of-exercise-science-and-master-of-exercise-physiology',
'https://www.latrobe.edu.au/courses/bachelor-of-food-and-nutrition',
'https://www.latrobe.edu.au/courses/bachelor-of-health-sciences-medical-classification-bachelor-of-health-information-management',
'https://www.latrobe.edu.au/courses/bachelor-of-health-sciences-in-dentistry-master-of-dentistry',
'https://www.latrobe.edu.au/courses/bachelor-of-healthcare',
'https://www.latrobe.edu.au/courses/bachelor-of-human-nutrition',
'https://www.latrobe.edu.au/courses/bachelor-of-human-services-and-master-of-social-work',
'https://www.latrobe.edu.au/courses/bachelor-of-nursing-enrolled-nurse-entry',
'https://www.latrobe.edu.au/courses/bachelor-of-nursing-graduate-entry',
'https://www.latrobe.edu.au/courses/bachelor-of-nursing-pre-registration',
'https://www.latrobe.edu.au/courses/bachelor-of-nursing-bachelor-of-midwifery',
'https://www.latrobe.edu.au/courses/bachelor-of-oral-health-science',
'https://www.latrobe.edu.au/courses/bachelor-of-paramedic-practice-with-honours',
'https://www.latrobe.edu.au/courses/bachelor-of-pharmacy-honours',
'https://www.latrobe.edu.au/courses/bachelor-of-sports-and-exercise-science',
'https://www.latrobe.edu.au/courses/bachelor-of-cybersecurity',
'https://www.latrobe.edu.au/courses/bachelor-of-engineering-honours-industrial',
'https://www.latrobe.edu.au/courses/bachelor-of-information-technology',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-information-technology',
'https://www.latrobe.edu.au/courses/bachelor-of-business-information-systems',
'https://www.latrobe.edu.au/courses/bachelor-of-business-information-systems-honours',
'https://www.latrobe.edu.au/courses/bachelor-of-civil-engineering-honours',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce-bachelor-of-computer-science',
'https://www.latrobe.edu.au/courses/bachelor-of-computer-science',
'https://www.latrobe.edu.au/courses/bachelor-of-computer-science-honours',
'https://www.latrobe.edu.au/courses/bachelor-of-cybersecurity-bachelor-of-psychological-science',
'https://www.latrobe.edu.au/courses/bachelor-of-information-technology-honours',
'https://www.latrobe.edu.au/courses/bachelor-of-information-technology-professional',
'https://www.latrobe.edu.au/courses/bachelor-of-laws-bachelor-of-science',
'https://www.latrobe.edu.au/courses/bachelor-of-biomedical-science',
'https://www.latrobe.edu.au/courses/bachelor-of-science',
'https://www.latrobe.edu.au/courses/bachelor-of-agricultural-sciences',
'https://www.latrobe.edu.au/courses/bachelor-of-agriculture-and-technology',
'https://www.latrobe.edu.au/courses/bachelor-of-animal-and-veterinary-biosciences',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-information-technology',
'https://www.latrobe.edu.au/courses/bachelor-of-biological-sciences',
'https://www.latrobe.edu.au/courses/bachelor-of-business-agribusiness',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce-bachelor-of-agricultural-sciences',
'https://www.latrobe.edu.au/courses/bachelor-of-commerce-bachelor-of-biomedicine',
'https://www.latrobe.edu.au/courses/bachelor-of-cybersecurity-bachelor-of-psychological-science',
'https://www.latrobe.edu.au/courses/bachelor-of-laws-bachelor-of-science',
'https://www.latrobe.edu.au/courses/bachelor-of-politics-philosophy-and-economics',
'https://www.latrobe.edu.au/courses/bachelor-of-science-wildlife-and-conservation-biology',
'https://www.latrobe.edu.au/courses/bachelor-of-science-double-degree-program',
'https://www.latrobe.edu.au/courses/bachelor-of-science-bachelor-of-business',
'https://www.latrobe.edu.au/courses/bachelor-of-veterinary-nursing',]
    start_urls=[]
    pro_list = list(set(pro_list))
    for i in pro_list:
        start_urls.append(i)
    def parse(self, response):
        # print(response.url)
        pro_url=re.findall('https?://www.latrobe.edu.au/courses/data/2019/international/[a-z\-/]+',response.text,re.S)
        if pro_url!=[]:
            for pu in pro_url:
                # print(pu)
                yield scrapy.Request(url=pu,callback=self.parses)
    def parses(self, response):
        print(response.url)
        item=get_item(AustraliaItem)
        item['university']='La Trobe University'
        item['url']=response.url
        degree_name=response.xpath('//h1/text()').extract()
        degree_name=''.join(degree_name)
        # print(degree_name)
        item['degree_name']=degree_name
        modules_url = response.xpath('//ul[@class="list-arrows"]/li[1]/a/@href').extract()
        if modules_url != []:
            try:
                modules = self.getResponse(modules_url[0]).xpath(
                    '//h3[contains(text(),"Course structure")]/following-sibling::div/div/table//tr/td/text()')
                item['modules_en'] = clear_long_text(modules)
            except:
                pass
        location=response.xpath('//ul[@class="list-arrows"]/li[1]/a/text()').extract()
        location=''.join(location).strip()
        item['location']=location

        overview = response.xpath('//section[@id="overview"]/div[@class="block"]').extract()
        # print('overview', overview)
        item['degree_overview_en']=remove_class(overview)
        rntry=response.xpath('//section[@id="entry-requirements"]').extract()
        # print('rntry',rntry)
        item['rntry_requirements_en']=remove_class(rntry)
        career=response.xpath('//section[@id="career-outcomes"]').extract()
        # print('career',career)
        item['career_en']=remove_class(career)
        htp=response.xpath('//section[@id="how-to-apply"]').extract()
        # print('htp',htp)
        item['apply_proces_en']=remove_class(htp)
        fee=response.xpath('//h3[contains(text(),"tuition fee")]/following-sibling::p[1]/text()').extract()
        # print('fee',fee)
        fee=''.join(fee).strip()
        tuition=fee.replace(' ','')
        # print('tuition_fee',tuition)
        item['tuition_fee']=tuition
        item['tuition_fee_pre']='AUD'
        duration=response.xpath('//div[contains(text(),"uration")]/following-sibling::div//text()').extract()
        # print('duration',duration)
        dura=re.findall('\d\.?\d?',''.join(duration))
        if dura!=[]:
            dura=list(map(float,dura))
            item['duration']=min(dura)
            item['duration_per']=1
        else:
            duration=clear_duration(duration)
            item['duration']=duration['duration']
            item['duration_per']=duration['duration_per']
        start_date=response.xpath('//div[contains(text(),"tart")]/following-sibling::div//text()').extract()
        # print('start_date',start_date)
        start_date=tracslateDate(start_date)
        # print(start_date)
        item['start_date']=','.join(start_date)
        ielts=response.xpath('//p[contains(text(),"IELTS")]/text()').extract()
        ielts=get_ielts(ielts)
        if ielts!=[]:
            item['ielts'] = ielts['IELTS']
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
        # degree_name_list=response.xpath('//p[contains(text(),"Our Majors are:")]/following-sibling::ul/li//a/@href|//p[contains(text(),"Choose from five majors")]/following-sibling::ul[1]/li//a/@href|//h3[contains(text(),"Specialisations, majors and minors")]/following-sibling::table/tbody/tr/td[1]//a/@href').extract()
        degree_name_list = response.xpath(
            '//p[contains(text(),"Our Majors are:")]/following-sibling::ul/li//text()|//p[contains(text(),"Choose from five majors")]/following-sibling::ul[1]/li//text()|//h3[contains(text(),"Specialisations, majors and minors")]/following-sibling::table/tbody/tr/td[1]//text()').extract()
        major_xpaths = '//section[@id="overview"]//a[contains(text(),"%s")]/@href'
        if degree_name_list != []:
            # print(degree_name_list)
            for name in degree_name_list:
                major_xpath = major_xpaths % name
                major_url = response.xpath(major_xpath).extract()
                # print(major_url)
                item['programme_en'] = name.strip()
                if major_url != []:
                    URL = major_url[0]
                    majRep = self.getResponse(URL)
                    modules = majRep.xpath('//div[@id="overview"]|//div[@id="why_study"]')
                    mod = ''
                    for i in modules:
                        mod += etree.tostring(i, method='html', encoding='unicode')
                    item['overview_en'] = remove_class(mod)
                print(item['degree_name'],'的专业')
                # yield item
        else:
                programme = re.findall('\(.*\)', degree_name.replace('(Honours)',''))
                programme = ''.join(programme).replace('(', '').replace(')', '').strip()
                if programme != '':
                    item['programme_en'] = programme
                else:
                    item['programme_en'] = degree_name.replace('Bachelor of', '').replace('Master of', '').strip()
                print(item['degree_name'],'没有专业')
                # yield item
    def getResponse(self,url):
        try:
            res=requests.get(url).content
            res=etree.HTML(res)
            return res
        except:
            return ''
