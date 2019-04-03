# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
import requests
# from scrapyNewAustralia.middlewares import *
# from scrapyNewAustralia.items import ScrapynewaustraliaItem
from scrapySchool_Australian_yan.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_yan.getItem import get_item
from scrapySchool_Australian_yan.getTuition_fee import getTuition_fee
from scrapySchool_Australian_yan.items import ScrapyschoolAustralianYanItem
from scrapySchool_Australian_yan.remove_tags import remove_class
from scrapySchool_Australian_yan.getStartDate import getStartDate
from scrapySchool_Australian_yan.getDuration import getIntDuration
import re

class LatrobeuniversityPSpider(scrapy.Spider):
    name = 'LaTrobeUniversity_P'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.latrobe.edu.au/courses/master-of-sports-analytics',
'https://www.latrobe.edu.au/courses/master-of-educational-leadership-and-management',
'https://www.latrobe.edu.au/courses/master-of-applied-linguistics2',
'https://www.latrobe.edu.au/courses/master-of-arts',
'https://www.latrobe.edu.au/courses/master-of-arts2',
'https://www.latrobe.edu.au/courses/master-of-business-research',
'https://www.latrobe.edu.au/courses/master-of-clinical-neuropsychology',
'https://www.latrobe.edu.au/courses/master-of-clinical-psychology',
'https://www.latrobe.edu.au/courses/master-of-communication-journalism-innovation',
'https://www.latrobe.edu.au/courses/master-of-communication-public-relations',
'https://www.latrobe.edu.au/courses/master-of-community-planning-and-development',
'https://www.latrobe.edu.au/courses/master-of-economics-research',
'https://www.latrobe.edu.au/courses/master-of-education-research',
'https://www.latrobe.edu.au/courses/master-of-international-development',
'https://www.latrobe.edu.au/courses/master-of-international-relations',
'https://www.latrobe.edu.au/courses/master-of-international-relations-research-studies',
'https://www.latrobe.edu.au/courses/master-of-planning',
'https://www.latrobe.edu.au/courses/master-of-professional-archaeology',
'https://www.latrobe.edu.au/courses/master-of-psychological-science',
'https://www.latrobe.edu.au/courses/master-of-social-work',
'https://www.latrobe.edu.au/courses/master-of-business-administration',
'https://www.latrobe.edu.au/courses/master-of-business-analytics',
'https://www.latrobe.edu.au/courses/master-of-cybersecurity-business-operations',
'https://www.latrobe.edu.au/courses/master-of-cybersecurity-computer-science',
'https://www.latrobe.edu.au/courses/master-of-cybersecurity-law',
'https://www.latrobe.edu.au/courses/bachelor-of-accounting-master-of-financial-analysis',
'https://www.latrobe.edu.au/courses/bachelor-of-business-master-of-management',
'https://www.latrobe.edu.au/courses/master-of-accounting-and-financial-management',
'https://www.latrobe.edu.au/courses/master-of-arts2',
'https://www.latrobe.edu.au/courses/master-of-biotechnology-management',
'https://www.latrobe.edu.au/courses/master-of-business-research',
'https://www.latrobe.edu.au/courses/master-of-business-administration-advanced',
'https://www.latrobe.edu.au/courses/master-of-business-administration-and-master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-business-information-management-and-systems',
'https://www.latrobe.edu.au/courses/master-of-commerce-research',
'https://www.latrobe.edu.au/courses/master-of-economics-research',
'https://www.latrobe.edu.au/courses/master-of-engineering-management',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis-financial-risk-management',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis-investment',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis-master-of-business-administration',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis-master-of-international-business',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis-master-of-professional-accounting',
'https://www.latrobe.edu.au/courses/master-of-international-business',
'https://www.latrobe.edu.au/courses/master-of-management',
'https://www.latrobe.edu.au/courses/master-of-management-corporate-governance-and-risk',
'https://www.latrobe.edu.au/courses/master-of-management-entrepreneurship-and-innovation',
'https://www.latrobe.edu.au/courses/master-of-management-human-resource-management',
'https://www.latrobe.edu.au/courses/master-of-management-human-resource-management-online',
'https://www.latrobe.edu.au/courses/master-of-management-project-management',
'https://www.latrobe.edu.au/courses/master-of-management-project-management-online',
'https://www.latrobe.edu.au/courses/master-of-management-sport-management',
'https://www.latrobe.edu.au/courses/master-of-marketing',
'https://www.latrobe.edu.au/courses/master-of-professional-accounting',
'https://www.latrobe.edu.au/courses/master-of-professional-accounting-business-analytics',
'https://www.latrobe.edu.au/courses/master-of-professional-accounting-cpa-australia-extension',
'https://www.latrobe.edu.au/courses/master-of-professional-accounting-information-systems-management',
'https://www.latrobe.edu.au/courses/master-of-teaching-primary',
'https://www.latrobe.edu.au/courses/master-of-teaching-secondary',
'https://www.latrobe.edu.au/courses/master-of-applied-linguistics',
'https://www.latrobe.edu.au/courses/master-of-applied-linguistics2',
'https://www.latrobe.edu.au/courses/master-of-arts',
'https://www.latrobe.edu.au/courses/master-of-education',
'https://www.latrobe.edu.au/courses/master-of-education-research',
'https://www.latrobe.edu.au/courses/master-of-educational-leadership-and-management',
'https://www.latrobe.edu.au/courses/master-of-outdoor-education-and-environment',
'https://www.latrobe.edu.au/courses/master-of-special-education',
'https://www.latrobe.edu.au/courses/master-of-nursing',
'https://www.latrobe.edu.au/courses/master-of-sports-analytics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-clinical-audiology',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-clinical-prosthetics-and-orthotics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-dietetic-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-occupational-therapy-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-orthoptics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-physiotherapy-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-podiatric-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-speech-pathology',
'https://www.latrobe.edu.au/courses/bachelor-of-exercise-science-and-master-of-exercise-physiology',
'https://www.latrobe.edu.au/courses/bachelor-of-health-sciences-in-dentistry-master-of-dentistry',
'https://www.latrobe.edu.au/courses/bachelor-of-human-services-and-master-of-social-work',
'https://www.latrobe.edu.au/courses/master-of-applied-science',
'https://www.latrobe.edu.au/courses/master-of-art-therapy',
'https://www.latrobe.edu.au/courses/master-of-business-administration-and-master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-clinical-audiology',
'https://www.latrobe.edu.au/courses/master-of-clinical-family-therapy',
'https://www.latrobe.edu.au/courses/master-of-clinical-prosthetics-and-orthotics',
'https://www.latrobe.edu.au/courses/master-of-dietetic-practice',
'https://www.latrobe.edu.au/courses/master-of-ergonomics-safety-and-health',
'https://www.latrobe.edu.au/courses/master-of-exercise-physiology',
'https://www.latrobe.edu.au/courses/master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-health-information-management',
'https://www.latrobe.edu.au/courses/master-of-health-sciences',
'https://www.latrobe.edu.au/courses/master-of-mental-health',
'https://www.latrobe.edu.au/courses/master-of-mental-health-nursing',
'https://www.latrobe.edu.au/courses/master-of-midwifery',
'https://www.latrobe.edu.au/courses/master-of-musculoskeletal-physiotherapy',
'https://www.latrobe.edu.au/courses/master-of-nursing-research',
'https://www.latrobe.edu.au/courses/master-of-nursing-nurse-practitioner',
'https://www.latrobe.edu.au/courses/master-of-nursing-science',
'https://www.latrobe.edu.au/courses/master-of-occupational-therapy-practice',
'https://www.latrobe.edu.au/courses/master-of-orthoptics',
'https://www.latrobe.edu.au/courses/master-of-physiotherapy-practice',
'https://www.latrobe.edu.au/courses/master-of-podiatric-practice',
'https://www.latrobe.edu.au/courses/master-of-public-health',
'https://www.latrobe.edu.au/courses/master-of-science',
'https://www.latrobe.edu.au/courses/master-of-social-work',
'https://www.latrobe.edu.au/courses/master-of-social-work-research',
'https://www.latrobe.edu.au/courses/master-of-speech-pathology',
'https://www.latrobe.edu.au/courses/master-of-sports-physiotherapy',
'https://www.latrobe.edu.au/courses/master-of-teaching-english-to-speakers-of-other-languages-tesol',
'https://www.latrobe.edu.au/courses/master-of-business-analytics',
'https://www.latrobe.edu.au/courses/master-of-cybersecurity-business-operations',
'https://www.latrobe.edu.au/courses/master-of-cybersecurity-computer-science',
'https://www.latrobe.edu.au/courses/master-of-cybersecurity-law',
'https://www.latrobe.edu.au/courses/master-of-data-science',
'https://www.latrobe.edu.au/courses/master-of-sports-analytics',
'https://www.latrobe.edu.au/courses/master-of-computer-science',
'https://www.latrobe.edu.au/courses/master-of-electronic-engineering',
'https://www.latrobe.edu.au/courses/master-of-engineering',
'https://www.latrobe.edu.au/courses/master-of-engineering-civil',
'https://www.latrobe.edu.au/courses/master-of-engineering-electronics',
'https://www.latrobe.edu.au/courses/master-of-engineering-manufacturing',
'https://www.latrobe.edu.au/courses/master-of-engineering-management',
'https://www.latrobe.edu.au/courses/master-of-information-and-communication-technology',
'https://www.latrobe.edu.au/courses/master-of-information-technology',
'https://www.latrobe.edu.au/courses/master-of-information-technology-computer-networks',
'https://www.latrobe.edu.au/courses/master-of-professional-accounting-information-systems-management',
'https://www.latrobe.edu.au/courses/master-of-science',
'https://www.latrobe.edu.au/courses/master-of-telecommunication-and-network-engineering',
'https://www.latrobe.edu.au/courses/master-of-cybersecurity-law',
'https://www.latrobe.edu.au/courses/master-of-arts2',
'https://www.latrobe.edu.au/courses/master-of-laws',
'https://www.latrobe.edu.au/courses/master-of-laws-research',
'https://www.latrobe.edu.au/courses/master-of-laws-in-global-business-law',
'https://www.latrobe.edu.au/courses/master-of-data-science',
'https://www.latrobe.edu.au/courses/master-of-agricultural-science',
'https://www.latrobe.edu.au/courses/master-of-biotechnology-and-bioinformatics',
'https://www.latrobe.edu.au/courses/master-of-biotechnology-management',
'https://www.latrobe.edu.au/courses/master-of-chemical-sciences',
'https://www.latrobe.edu.au/courses/master-of-nanotechnology',
'https://www.latrobe.edu.au/courses/master-of-science',
'https://www.latrobe.edu.au/courses/master-of-science-in-physical-sciences',]
    # print(len(start_urls))
    start_urls=list(set(start_urls))
    # print(len(start_urls))


    def parse(self, response):
        # print(response.url)
        pro_url=re.findall('https?://www.latrobe.edu.au/courses/data/2019/international/[a-z\-/]+', response.text,re.S)
        print(pro_url)
        # if pro_url!=[]:
        #     for pu in pro_url:
                # print(pu)
                # yield scrapy.Request(url=pu,callback=self.parses)
        # print(pro_url)

    def parses(self, response):
        print(response.url)
        item=get_item(ScrapyschoolAustralianYanItem)
        item['university']='La Trobe University'
        item['url']=response.url
        item['location']='Melbourne'
        degree_name=response.xpath('//h1/text()').extract()
        print(degree_name)
        degree_name=''.join(degree_name)
        item['degree_name']=degree_name
        degree_name_list=response.xpath('//p[contains(text(),"Our Majors are:")]/following-sibling::ul/li//text()|'
                                        '//p[contains(text(),"Choose from five majors")]/following-sibling::ul[1]/li/text()|'
                                        '//h3[contains(text(),"Specialisations, majors and minors")]/following-sibling::table/tbody/tr/td[1]//text()').extract()
        print(degree_name_list)
        modules_url = response.xpath('//ul[@class="list-arrows"]/li[1]/a/@href').extract()
        if modules_url!=[]:
            try:
                modules = self.getResponse(modules_url[0]).xpath('//h3[contains(text(),"Course structure")]/following-sibling::div/div/table//tr/td/text()')
                # print('modules', modules)
                item['modules_en']=clear_long_text(modules)
            except:
                item['modules_en']=None

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
        item['tuition_fee']=tuition[0:99]
        item['tuition_fee_pre']='AUD'

        duration=response.xpath('//div[contains(text(),"uration")]/following-sibling::div//text()').extract()
        # print('duration',duration)
        dura=re.findall('\d\.?\d?',''.join(duration))
        dura=list(map(float,dura))
        item['duration']=min(dura)
        item['duration_per']=1


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
        if degree_name_list!=[]:
            for url in degree_name_list:
                deg_res = self.getResponse(''.join(url))
                deg_overview = deg_res.xpath('//div[@id="overview"]//text()')
                deg_overview = clear_long_text(deg_overview)
                item['overview_en'] = deg_overview
                item['programme_en']=''.join(deg_res.xpath('//h1/text()'))
                if '/' not in degree_name:
                    yield item
        else:
            programme = re.findall('\(.*\)', degree_name)
            programme = ''.join(programme).replace('(', '').replace(')', '').strip()
            if programme != '':
                item['programme_en'] = programme
            else:
                item['programme_en'] = degree_name.replace('Master of', '').replace('Bachelor of','').strip()
            if '/' not in degree_name:
                yield item

    def getResponse(self,url):
        try:
            res=requests.get(url).content
            res=etree.HTML(res)
            return res
        except:
            return ''
