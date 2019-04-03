# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
from scrapySchool_England_U.middlewares import *

class StmaryuniversitytwickenhamUSpider(scrapy.Spider):
    name = 'StMaryUniversityTwickenham_U'
    # allowed_domains = ['a.b']
    start_urlss = ['https://www.stmarys.ac.uk/undergraduate/politics-policy-and-public-management',
'https://www.stmarys.ac.uk/undergraduate/drama-education',
'https://www.stmarys.ac.uk/undergraduate/english-with-celta-ba',
'https://www.stmarys.ac.uk/undergraduate/applied-physics',
'https://www.stmarys.ac.uk/undergraduate/communications-and-marketing',
'https://www.stmarys.ac.uk/undergraduate/acting',
'https://www.stmarys.ac.uk/undergraduate/business-law',
'https://www.stmarys.ac.uk/undergraduate/business-management-and-entrepreneurship',
'https://www.stmarys.ac.uk/undergraduate/business-and-finance',
'https://www.stmarys.ac.uk/undergraduate/business-management-and-marketing',
'https://www.stmarys.ac.uk/undergraduate/business-management',
'https://www.stmarys.ac.uk/undergraduate/communications-design-and-marketing',
'https://www.stmarys.ac.uk/undergraduate/communications-data-analytics-and-marketing',
'https://www.stmarys.ac.uk/postgraduate-courses-london/sport-health-applied-science-research',
'https://www.stmarys.ac.uk/postgraduate-courses-london/biblical-studies',
'https://www.stmarys.ac.uk/postgraduate-courses-london/applied-sports-nutrition',
'https://www.stmarys.ac.uk/postgraduate-courses-london/christian-spirituality',
'https://www.stmarys.ac.uk/postgraduate-courses-london/chronic-disease-management',
'https://www.stmarys.ac.uk/postgraduate-courses-london/charity-management',
'https://www.stmarys.ac.uk/postgraduate-courses-london/creative-writing-first-novel',
'https://www.stmarys.ac.uk/postgraduate-courses-london/leading-innovation-and-change-education',
'https://www.stmarys.ac.uk/postgraduate-courses-london/education-culture-and-society',
'https://www.stmarys.ac.uk/postgraduate-courses-london/physical-education-and-sport-leadership',
'https://www.stmarys.ac.uk/postgraduate-courses-london/diplomacy',
'https://www.stmarys.ac.uk/postgraduate-courses-london/catholic-school-leadership',
'https://www.stmarys.ac.uk/postgraduate-courses-london/applied-sport-and-exercise-physiology',
'https://www.stmarys.ac.uk/postgraduate-courses-london/international-and-european-business-law',
'https://www.stmarys.ac.uk/postgraduate-courses-london/international-business-law',
'https://www.stmarys.ac.uk/postgraduate-courses-london/international-business-practice',
'https://www.stmarys.ac.uk/postgraduate-courses-london/applied-linguistics-english-language',
'https://www.stmarys.ac.uk/postgraduate-courses-london/education-pedagogy-for-teachers',
'https://www.stmarys.ac.uk/postgraduate-courses-london/international-relations',
'https://www.stmarys.ac.uk/postgraduate-courses-london/international-business-management',
'https://www.stmarys.ac.uk/postgraduate-courses-london/london-theatre',
'https://www.stmarys.ac.uk/postgraduate-courses-london/bioethics-and-medical-law/',
'https://www.stmarys.ac.uk/postgraduate-courses-london/nutrition-and-genetics',
'https://www.stmarys.ac.uk/postgraduate-courses-london/gothic-studies-and-culture/',
'https://www.stmarys.ac.uk/postgraduate-courses-london/applied-sport-psychology',
'https://www.stmarys.ac.uk/postgraduate-courses-london/playwriting',
'https://www.stmarys.ac.uk/postgraduate-courses-london/human-trafficking/',
'https://www.stmarys.ac.uk/postgraduate-courses-london/human-nutrition/',
'https://www.stmarys.ac.uk/postgraduate-courses-london/international-sports-journalism/',
'https://www.stmarys.ac.uk/postgraduate-courses-london/teaching-and-learning',
'https://www.stmarys.ac.uk/postgraduate-courses-london/theology',
'https://www.stmarys.ac.uk/postgraduate-courses-london/international-tourism-management/',
'https://www.stmarys.ac.uk/postgraduate-courses-london/public-history/',
'https://www.stmarys.ac.uk/postgraduate-courses-london/sport-rehabilitation/',
'https://www.stmarys.ac.uk/postgraduate-courses-london/theatre-directing/',
'https://www.stmarys.ac.uk/postgraduate-courses-london/sports-journalism/',
'https://www.stmarys.ac.uk/postgraduate-courses-london/physiotherapy/',
'https://www.stmarys.ac.uk/undergraduate/creative-and-professional-writing',
'https://www.stmarys.ac.uk/undergraduate/design-and-visual-communication',
'https://www.stmarys.ac.uk/undergraduate/drama-creative-writing',
'https://www.stmarys.ac.uk/undergraduate/communications-media-and-marketing',
'https://www.stmarys.ac.uk/undergraduate/education-and-social-science',
'https://www.stmarys.ac.uk/undergraduate/english-literature',
'https://www.stmarys.ac.uk/undergraduate/film-and-digital-production',
'https://www.stmarys.ac.uk/undergraduate/film-and-screen-media',
'https://www.stmarys.ac.uk/undergraduate/history',
'https://www.stmarys.ac.uk/undergraduate/nutrition',
'https://www.stmarys.ac.uk/undergraduate/criminology-and-sociology/',
'https://www.stmarys.ac.uk/undergraduate/health-and-exercise-science/',
'https://www.stmarys.ac.uk/undergraduate/sport-rehabilitation',
'https://www.stmarys.ac.uk/undergraduate/english-and-drama/',
'https://www.stmarys.ac.uk/undergraduate/international-business-management/',
'https://www.stmarys.ac.uk/undergraduate/law/',
'https://www.stmarys.ac.uk/undergraduate/law-with-criminology/',
'https://www.stmarys.ac.uk/undergraduate/sport-science',
'https://www.stmarys.ac.uk/undergraduate/physical-and-sport-education/',
'https://www.stmarys.ac.uk/undergraduate/strength-and-conditioning-science',
'https://www.stmarys.ac.uk/undergraduate/sports-communications-and-marketing',
'https://www.stmarys.ac.uk/undergraduate/sports-coaching-science',
'https://www.stmarys.ac.uk/undergraduate/drama-technical-theatre',
'https://www.stmarys.ac.uk/undergraduate/psychology/',
'https://www.stmarys.ac.uk/undergraduate/sports-management',
'https://www.stmarys.ac.uk/undergraduate/theology-religion-and-ethics',
'https://www.stmarys.ac.uk/undergraduate/tourism-management',
'https://www.stmarys.ac.uk/undergraduate/tourism',
'https://www.stmarys.ac.uk/undergraduate/politics-and-communications',
'https://www.stmarys.ac.uk/undergraduate/politics-and-international-relations',]
    start_urls = ['https://www.stmarys.ac.uk/undergraduate/politics-policy-and-public-management']
    def parse(self, response):
        url=['https://www.stmarys.ac.uk/undergraduate/psychology/',
'https://www.stmarys.ac.uk/undergraduate/politics-policy-and-public-management',
'https://www.stmarys.ac.uk/undergraduate/drama-education',
'https://www.stmarys.ac.uk/undergraduate/english-with-celta-ba',
'https://www.stmarys.ac.uk/undergraduate/communications-and-marketing',
'https://www.stmarys.ac.uk/undergraduate/acting',
'https://www.stmarys.ac.uk/undergraduate/communications-design-and-marketing',
'https://www.stmarys.ac.uk/undergraduate/communications-data-analytics-and-marketing',
'https://www.stmarys.ac.uk/undergraduate/creative-and-professional-writing',
'https://www.stmarys.ac.uk/undergraduate/design-and-visual-communication',
'https://www.stmarys.ac.uk/undergraduate/drama-creative-writing',
'https://www.stmarys.ac.uk/undergraduate/communications-media-and-marketing',
'https://www.stmarys.ac.uk/undergraduate/english-literature',
'https://www.stmarys.ac.uk/undergraduate/film-and-digital-production',
'https://www.stmarys.ac.uk/undergraduate/film-and-screen-media',
'https://www.stmarys.ac.uk/undergraduate/history',
'https://www.stmarys.ac.uk/undergraduate/criminology-and-sociology/',
'https://www.stmarys.ac.uk/undergraduate/sport-rehabilitation',
'https://www.stmarys.ac.uk/undergraduate/english-and-drama/',
'https://www.stmarys.ac.uk/undergraduate/law/',
'https://www.stmarys.ac.uk/undergraduate/law-with-criminology/',
'https://www.stmarys.ac.uk/undergraduate/sport-science',
'https://www.stmarys.ac.uk/undergraduate/physical-and-sport-education/',
'https://www.stmarys.ac.uk/undergraduate/strength-and-conditioning-science',
'https://www.stmarys.ac.uk/undergraduate/sports-communications-and-marketing',
'https://www.stmarys.ac.uk/undergraduate/sports-coaching-science',
'https://www.stmarys.ac.uk/undergraduate/drama-technical-theatre',
'https://www.stmarys.ac.uk/undergraduate/theology-religion-and-ethics',
'https://www.stmarys.ac.uk/undergraduate/politics-and-communications',
'https://www.stmarys.ac.uk/undergraduate/politics-and-international-relations',
'https://www.stmarys.ac.uk/undergraduate/applied-physics',
'https://www.stmarys.ac.uk/undergraduate/business-law',
'https://www.stmarys.ac.uk/undergraduate/business-management-and-entrepreneurship',
'https://www.stmarys.ac.uk/undergraduate/business-and-finance',
'https://www.stmarys.ac.uk/undergraduate/business-management-and-marketing',
'https://www.stmarys.ac.uk/undergraduate/business-management',
'https://www.stmarys.ac.uk/undergraduate/education-and-social-science',
'https://www.stmarys.ac.uk/undergraduate/nutrition',
'https://www.stmarys.ac.uk/undergraduate/health-and-exercise-science/',
'https://www.stmarys.ac.uk/undergraduate/international-business-management/',
'https://www.stmarys.ac.uk/undergraduate/sports-management',
'https://www.stmarys.ac.uk/undergraduate/tourism-management',
'https://www.stmarys.ac.uk/undergraduate/tourism',]
        url=set(url)
        for u in url:
            yield scrapy.Request(url=u,callback=self.parsesss,meta={'url':u})
    def parsesss(self, response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = "St Mary's University, Twickenham"
        item['url'] = response.url
        alevel=response.xpath('//span[text()="A Levels"]/preceding-sibling::span/h3/text()').extract()
        print(alevel)
        item['alevel']=alevel[0]
        yield item
    def parsess(self, response):
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)

        item['university'] = "St Mary's University, Twickenham"
        item['url'] = response.url
        item['location'] = 'London'

        rntry = response.xpath('//h2[contains(text(),"Entry requirements")]/following-sibling::div').extract()
        rntry = remove_class(rntry)
        # print(rntry)
        # item['rntry_requirements'] = rntry

        modules = response.xpath('//h2[contains(text(),"Course")]/../../following-sibling::div[1]//ul/li').extract()
        modules = remove_class(modules)
        # print(modules)
        item['modules_en'] = modules

        overview = response.xpath('//div[@id="overview"]//div[@class="large-8 columns content"]').extract()
        overview = remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        duration = response.xpath('//p[contains(text(),"Attendance")]/preceding-sibling::p/text()').extract()
        duration = clear_duration(duration)
        # print(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']

        programme = response.xpath('//h1/text()').extract()
        # print(programme)
        programme=''.join(programme).strip()
        degree_name=re.findall('[A-Z][A-Za-z]*\s*\(Hons\)',programme)
        degree_name=''.join(degree_name).strip()
        programme=programme.replace(degree_name,'').strip()
        # print(programme)
        # print(degree_name)
        item['degree_name']=degree_name
        item['programme_en']=programme

        career = response.xpath('//section[@id="careers"]').extract()
        career = remove_class(career)
        # print(career)
        item['career_en'] = career

        # 13650
        fee = response.xpath('//*[contains(text(),"£")]//text()').extract()
        tuition_fee = getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = '£'

        item['deadline'] = '2019-9'

        apply_d = ["<p>Copies of academic transcripts and certificates</p>",
                   "<p>A Copy of your English language requirements (if needed)</p>",
                   "<p>A Copy of your passport</p>",
                   "<p>Visa history questionnaire</p>", ]
        apply_d = '\n'.join(apply_d)
        item['apply_documents_en'] = apply_d

        # print(item)
        ielts = response.xpath('//h4[contains(text(),"International re")]/following-sibling::p[1]/text()').extract()
        ielts = ''.join(ielts).strip()
        # print(ielts)
        ielts = get_ielts(ielts)
        try:
            if ielts != [] or ielts != {}:
                item['ielts_l'] = ielts['IELTS_L']
                item['ielts_s'] = ielts['IELTS_S']
                item['ielts_r'] = ielts['IELTS_R']
                item['ielts_w'] = ielts['IELTS_W']
                item['ielts'] = ielts['IELTS']
        except:
            pass

        ucascode=response.xpath('//p[contains(text(),"UCAS code")]/preceding-sibling::p[1]/text()').extract()
        ucascode=','.join(ucascode).strip()
        item['ucascode']=ucascode

        alevel=response.xpath('//span[contains(text(),"A Levels")]/preceding-sibling::span//text()').extract()
        alevel='/'.join(set(alevel)).strip()
        item['alevel']=alevel

        require_chinese_en='<p>Students who have completed the National College Entrance Examination (Gaokao, 高考 ) with an average total score of 70%, will normally be accepted for undergraduate entry.</p>'
        item['require_chinese_en']=require_chinese_en

        assessment=response.xpath('//h2[contains(text(),"Assessment methods")]/following-sibling::p').extract()
        if assessment!=[]:
            assessment='<h2>Assessment methods</h2>'+remove_class(assessment)
            item['assessment_en']=assessment
            print('GG')
        else:
            print(response.url)


        # print(item)
        yield item