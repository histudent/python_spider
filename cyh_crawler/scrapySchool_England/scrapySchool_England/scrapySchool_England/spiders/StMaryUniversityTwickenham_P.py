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

class StmaryuniversitytwickenhamPSpider(scrapy.Spider):
    name = 'StMaryUniversityTwickenham_P'
    allowed_domains = ['stmarys.ac.uk']
    start_urls = []
    pro_url=["/postgraduate-courses-london/applied-linguistics-english-language",
"/postgraduate-courses-london/applied-sport-and-exercise-physiology",
"/postgraduate-courses-london/applied-sport-psychology",
"/postgraduate-courses-london/applied-sports-nutrition",
"/postgraduate-courses-london/biblical-studies",
"/postgraduate-courses-london/bioethics-and-medical-law",
"/postgraduate-courses-london/catholic-school-leadership",
"/postgraduate-courses-london/catholic-social-teaching",
"/postgraduate-courses-london/charity-management",
"/postgraduate-courses-london/christian-spirituality",
"/postgraduate-courses-london/chronic-disease-management",
"/postgraduate-courses-london/creative-writing-first-novel",
"/postgraduate-courses-london/diplomacy",
"/postgraduate-courses-london/education-culture-and-society",
"/postgraduate-courses-london/leading-innovation-and-change-education",
"/postgraduate-courses-london/physical-education-and-sport-leadership",
"/postgraduate-courses-london/education-pedagogy-for-teachers",
"/postgraduate-courses-london/gothic-studies-and-culture",
"/postgraduate-courses-london/human-nutrition",
"/postgraduate-courses-london/human-trafficking",
"/postgraduate-courses-london/international-and-european-business-law",
"/postgraduate-courses-london/international-business-law",
"/postgraduate-courses-london/international-business-management",
"/postgraduate-courses-london/international-business-practice",
"/postgraduate-courses-london/international-relations",
"/postgraduate-courses-london/international-sports-journalism",
"/postgraduate-courses-london/international-tourism-management",
"/postgraduate-courses-london/london-theatre",
"/postgraduate-courses-london/nutrition-and-genetics",
"/postgraduate-courses-london/performance-football-coaching",
"/postgraduate-courses-london/physiotherapy",
"/postgraduate-courses-london/playwriting",
"/postgraduate-courses-london/pgce-primary",
"/postgraduate-courses-london/public-history",
"/postgraduate-courses-london/pgce-secondary-english",
"/postgraduate-courses-london/pgce-secondary-geography",
"/postgraduate-courses-london/pgce-secondary-history",
"/postgraduate-courses-london/pgce-secondary-maths",
"/postgraduate-courses-london/pgce-secondary-mfl",
"/postgraduate-courses-london/pgce-secondary-pe",
"/postgraduate-courses-london/pgce-secondary-re",
"/postgraduate-courses-london/pgce-secondary-science",
"/postgraduate-courses-london/sport-rehabilitation",
"/postgraduate-courses-london/sport-health-applied-science-research",
"/postgraduate-courses-london/sports-journalism",
"/postgraduate-courses-london/strength-and-conditioning",
"/postgraduate-courses-london/teaching-and-learning",
"/postgraduate-courses-london/theatre-directing",
"/postgraduate-courses-london/theology",
"/postgraduate-courses-london/sport-health-applied-science-research"]
    for i in pro_url:
        full_url='https://www.stmarys.ac.uk'+i
        start_urls.append(full_url)
    def parse(self, response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)

        item['university']="St Mary's University, Twickenham"
        item['url']=response.url
        item['location']='London'

        rntry=response.xpath('//h2[contains(text(),"Entry requirements")]/following-sibling::div').extract()
        rntry=remove_class(rntry)
        # print(rntry)
        item['rntry_requirements']=rntry

        modules=response.xpath('//h2[contains(text(),"Course")]/../following-sibling::div//ul').extract()
        modules=remove_class(modules)
        # print(modules)
        item['modules_en']=modules

        overview=response.xpath('//div[@id="overview"]//div[@class="large-8 columns content"]').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en']=overview

        duration=response.xpath('//p[contains(text(),"uration")]/preceding-sibling::p/text()').extract()
        duration=clear_duration(duration)
        # print(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']

        programme=response.xpath('//h1/text()').extract()
        # print(programme)
        if len(programme)==2:
            prog=programme[0]
            degr=programme[1]
            item['programme_en']=prog
            item['degree_name']=degr
            degree_name=degr

        else:
            prog=''.join(programme).strip()
            item['programme_en']=prog
        # print(prog)

        career=response.xpath('//section[@id="careers"]').extract()
        career=remove_class(career)
        # print(career)
        item['career_en']=career

        #13650
        fee=response.xpath('//h2[contains(text(),"Tuition")]/following-sibling::*/text()').extract()
        tuition_fee=getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee']=tuition_fee
        item['tuition_fee_pre']='£'

        item['deadline']='2019-7-31'

        apply_d=["<ul><li>Copies of academic transcripts and certificates</li>",
"<li>A Copy of your English language requirements (if needed)</li>",
"<li>A Copy of your passport</li>",
"<li>Visa history questionnaire</li></ul>",]
        apply_d='\n'.join(apply_d)
        item['apply_documents_en']=apply_d

        # print(item)
        ielts=response.xpath('//h4[contains(text(),"International re")]/following-sibling::p[1]/text()').extract()
        ielts=''.join(ielts).strip()
        # print(ielts)
        ielts=get_ielts(ielts)
        try:
            if ielts!=[] or ielts!={}:
                item['ielts_l']=ielts['IELTS_L']
                item['ielts_s'] = ielts['IELTS_S']
                item['ielts_r'] = ielts['IELTS_R']
                item['ielts_w'] = ielts['IELTS_W']
                item['ielts'] = ielts['IELTS']
        except:
            pass

        assessment=response.xpath('//h2[contains(text(),"ssessment")]/following-sibling::p[position()<=5]').extract()
        if assessment==[]:
            print(response.url)
        else:
            print('sssssssssssssssssssssss')
        item['assessment_en']=remove_class(assessment)

        yield item