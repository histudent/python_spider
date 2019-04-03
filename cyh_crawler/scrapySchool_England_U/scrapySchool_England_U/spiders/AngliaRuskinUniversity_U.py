# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
import json
import requests
from lxml import etree
import json
class AngliaruskinuniversityUSpider(scrapy.Spider):
    name = 'AngliaRuskinUniversity_U'
    # allowed_domains = ['anglia.ac.uk']
    start_urls = ['https://www.anglia.ac.uk/study/course-search?keywords=&levelofstudy=undergraduate&modeofstudy=Full-time']
    #补抓alevel
    def parse(self, response):
        url=['https://www.anglia.ac.uk/study/undergraduate/media-studies',
'https://www.anglia.ac.uk/study/undergraduate/business-and-human-resource-management',
'https://www.anglia.ac.uk/study/undergraduate/computer-science',
'https://www.anglia.ac.uk/study/undergraduate/performing-arts',
'https://www.anglia.ac.uk/study/undergraduate/computer-gaming-technology-with-foundation-year',
'https://www.anglia.ac.uk/study/undergraduate/building-surveying',
'https://www.anglia.ac.uk/study/undergraduate/policing-and-criminal-justice',
'https://www.anglia.ac.uk/study/undergraduate/forensic-science-with-foundation-year',
'https://www.anglia.ac.uk/study/undergraduate/architectural-technology',
'https://www.anglia.ac.uk/study/undergraduate/computer-networks',
'https://www.anglia.ac.uk/study/undergraduate/drama',
'https://www.anglia.ac.uk/study/undergraduate/psychology',
'https://www.anglia.ac.uk/study/undergraduate/politics',
'https://www.anglia.ac.uk/study/undergraduate/pharmaceutical-science-with-foundation-year',
'https://www.anglia.ac.uk/study/undergraduate/philosophy',
'https://www.anglia.ac.uk/study/undergraduate/criminology',
'https://www.anglia.ac.uk/study/undergraduate/drama-and-english-literature',
'https://www.anglia.ac.uk/study/undergraduate/philosophy-and-english-literature',
'https://www.anglia.ac.uk/study/undergraduate/computing-and-information-systems-peterborough',
'https://www.anglia.ac.uk/study/undergraduate/archaeology-and-landscape-history-peterborough',
'https://www.anglia.ac.uk/study/undergraduate/media-studies-peterborough',
'https://www.anglia.ac.uk/study/undergraduate/paramedic-science',
'https://www.anglia.ac.uk/study/undergraduate/zoology',
'https://www.anglia.ac.uk/study/undergraduate/accounting-and-finance',
'https://www.anglia.ac.uk/study/undergraduate/applied-computer-science-west-anglia',
'https://www.anglia.ac.uk/study/undergraduate/international-nursing-studies',
'https://www.anglia.ac.uk/study/undergraduate/ophthalmic-dispensing-with-foundation-year',
'https://www.anglia.ac.uk/study/undergraduate/education',
'https://www.anglia.ac.uk/study/undergraduate/bioscience-peterborough',
'https://www.anglia.ac.uk/study/undergraduate/operating-department-practice',
'https://www.anglia.ac.uk/study/undergraduate/law',
'https://www.anglia.ac.uk/study/undergraduate/illustration-and-animation',
'https://www.anglia.ac.uk/study/undergraduate/english-language',
'https://www.anglia.ac.uk/study/undergraduate/biomedical-science-with-foundation-year',
'https://www.anglia.ac.uk/study/undergraduate/interior-design',
'https://www.anglia.ac.uk/study/undergraduate/business-economics',
'https://www.anglia.ac.uk/study/undergraduate/illustration',
'https://www.anglia.ac.uk/study/undergraduate/architecture',
'https://www.anglia.ac.uk/study/undergraduate/sports-coaching-and-physical-education-peterborough',
'https://www.anglia.ac.uk/study/undergraduate/zoology-with-foundation-year',
'https://www.anglia.ac.uk/study/undergraduate/civil-engineering-meng',
'https://www.anglia.ac.uk/study/undergraduate/veterinary-nursing-and-applied-animal-behaviour',
'https://www.anglia.ac.uk/study/undergraduate/drama-and-film-studies',
'https://www.anglia.ac.uk/study/undergraduate/film-studies-and-media-studies',
'https://www.anglia.ac.uk/study/undergraduate/sports-coaching-and-physical-education',
'https://www.anglia.ac.uk/study/undergraduate/photography',
'https://www.anglia.ac.uk/study/undergraduate/social-work',
'https://www.anglia.ac.uk/study/undergraduate/mechanical-engineering-meng',
'https://www.anglia.ac.uk/study/undergraduate/accounting-and-finance-peterborough',
'https://www.anglia.ac.uk/study/undergraduate/osteopathy-most',
'https://www.anglia.ac.uk/study/undergraduate/nursing-mental-health',
'https://www.anglia.ac.uk/study/undergraduate/medical-science',
'https://www.anglia.ac.uk/study/undergraduate/english-language-and-linguistics',
'https://www.anglia.ac.uk/study/undergraduate/construction-management',
'https://www.anglia.ac.uk/study/undergraduate/business-management-and-finance',
'https://www.anglia.ac.uk/study/undergraduate/banking-and-finance',
'https://www.anglia.ac.uk/study/undergraduate/osteopathy',
'https://www.anglia.ac.uk/study/undergraduate/international-business-management',
'https://www.anglia.ac.uk/study/undergraduate/history',
'https://www.anglia.ac.uk/study/undergraduate/english-literature-peterborough',
'https://www.anglia.ac.uk/study/undergraduate/crime-and-investigative-studies-with-foundation-year',
'https://www.anglia.ac.uk/study/undergraduate/mechanical-engineering',
'https://www.anglia.ac.uk/study/undergraduate/psychology-and-criminology',
'https://www.anglia.ac.uk/study/undergraduate/abnormal-and-clinical-psychology',
'https://www.anglia.ac.uk/study/undergraduate/early-childhood-studies-west-anglia',
'https://www.anglia.ac.uk/study/undergraduate/primary-education-studies',
'https://www.anglia.ac.uk/study/undergraduate/graphic-design',
'https://www.anglia.ac.uk/study/undergraduate/ophthalmic-dispensing',
'https://www.anglia.ac.uk/study/undergraduate/nursing-adult',
'https://www.anglia.ac.uk/study/undergraduate/history-and-english-west-anglia',
'https://www.anglia.ac.uk/study/undergraduate/music',
'https://www.anglia.ac.uk/study/undergraduate/criminology-and-policing',
'https://www.anglia.ac.uk/study/undergraduate/popular-music',
'https://www.anglia.ac.uk/study/undergraduate/marine-biology-with-conservation-and-biodiversity',
'https://www.anglia.ac.uk/study/undergraduate/electronic-music',
'https://www.anglia.ac.uk/study/undergraduate/film-and-television-production',
'https://www.anglia.ac.uk/study/undergraduate/writing-and-english-literature',
'https://www.anglia.ac.uk/study/undergraduate/film-studies',
'https://www.anglia.ac.uk/study/undergraduate/animal-behaviour-with-foundation-year',
'https://www.anglia.ac.uk/study/undergraduate/applied-nutritional-science',
'https://www.anglia.ac.uk/study/undergraduate/finance-and-business-analytics',
'https://www.anglia.ac.uk/study/undergraduate/crime-and-investigative-studies',
'https://www.anglia.ac.uk/study/undergraduate/animal-behaviour',
'https://www.anglia.ac.uk/study/undergraduate/sports-science',
'https://www.anglia.ac.uk/study/undergraduate/early-childhood-studies',
'https://www.anglia.ac.uk/study/undergraduate/tourism-management',
'https://www.anglia.ac.uk/study/undergraduate/crime-and-investigative-studies-peterborough',
'https://www.anglia.ac.uk/study/undergraduate/cyber-security',
'https://www.anglia.ac.uk/study/undergraduate/criminology-peterborough',
'https://www.anglia.ac.uk/study/undergraduate/pharmaceutical-science',
'https://www.anglia.ac.uk/study/undergraduate/midwifery',
'https://www.anglia.ac.uk/study/undergraduate/computer-games-art',
'https://www.anglia.ac.uk/study/undergraduate/business-management-and-leadership',
'https://www.anglia.ac.uk/study/undergraduate/civil-engineering-beng',
'https://www.anglia.ac.uk/study/undergraduate/healthcare-science',
'https://www.anglia.ac.uk/study/undergraduate/professional-dance-and-musical-theatre',
'https://www.anglia.ac.uk/study/undergraduate/sociology-peterborough',
'https://www.anglia.ac.uk/study/undergraduate/journalism-multimedia-peterborough',
'https://www.anglia.ac.uk/study/undergraduate/criminology-and-sociology',
'https://www.anglia.ac.uk/study/undergraduate/biomedical-science',
'https://www.anglia.ac.uk/study/undergraduate/civil-engineering',
'https://www.anglia.ac.uk/study/undergraduate/performing-arts-peterborough',
'https://www.anglia.ac.uk/study/undergraduate/psychosocial-studies-peterborough',
'https://www.anglia.ac.uk/study/undergraduate/computer-gaming-technology',
'https://www.anglia.ac.uk/study/undergraduate/nursing-child',
'https://www.anglia.ac.uk/study/undergraduate/business-management-peterborough',
'https://www.anglia.ac.uk/study/undergraduate/electronic-engineering',
'https://www.anglia.ac.uk/study/undergraduate/marketing',
'https://www.anglia.ac.uk/study/undergraduate/psychosocial-studies-west-anglia',
'https://www.anglia.ac.uk/study/undergraduate/medical-science-with-foundation-year',
'https://www.anglia.ac.uk/study/undergraduate/quantity-surveying',]
        url=set(url)
        for u in url:
            yield scrapy.Request(url=u,callback=self.parsesss,meta={'url':u})
    def parsesss(self, response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.meta['url']
        item['university']='Anglia Ruskin University'
        # yield item
        ib = response.xpath('//*[contains(text(),"International Baccalaureate")]/text()').extract()
        ib=response.xpath('//span[contains(text(),"nternational Baccalaureate")]/text()').extract()
        print(ib)
        # item['ib'] = ''.join(ib)
        # alevel = response.xpath(
        #     '//*[contains(text(),"A Level")]/text()|//*[contains(text(),"A-level")]/text()|//*[contains(text(),"A level")]/text()').extract()
        # if alevel == []:
        #     alevel = response.xpath('//span[contains(text(),"A Level")]//text()').extract()
        # if alevel == []:
        #     alevel = response.xpath('//p[contains(text(),"A-Level")]//text()').extract()
        # if alevel == []:
        #     print(response.url)
        # else:
        #     print(alevel)
        # item['alevel'] = ''.join(alevel)
        # yield item
    def parsess(self, response):
        # print(response.url)
        pro_url=response.xpath('//h3[@class="listing--common__title"]/a/@href').extract()
        for i in pro_url:
            URL='https://www.anglia.ac.uk'+i
            yield scrapy.Request(url=URL,callback=self.parses)
        next_page=response.xpath('//a[contains(text(),"Next")]/@href').extract()
        if next_page!=[]:
            full_url='https://www.anglia.ac.uk'+next_page[0]
            yield scrapy.Request(url=full_url,callback=self.parse)
    def parses(self,response):
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'Anglia Ruskin University'
        item['url'] = response.url
        item['degree_type']='1'
        programme = response.xpath('//h1/text()').extract()
        programme = ''.join(programme).split('\r\n')
        if len(programme) == 4:
            prog = programme[1].strip()
            degr = programme[2].strip()
            # print(degr)
            item['degree_name'] =degr
        else:
            prog = ''.join(programme)
        # print(prog)
        item['programme_en'] = prog

        location = response.xpath(
            '//div[@class="course-summary__text"]/p[@class="course-summary__locations"]/a/text()').extract()
        location = set(location)
        # print(location)
        location = ','.join(location)
        item['location'] = location

        start_date = response.xpath(
            '//div[@class="course-summary__text"]/p[@class="course-summary__entry"]/text()').extract()
        start_date = tracslateDate(start_date)
        # print(start_date)
        start_date = ','.join(start_date)
        item['start_date'] = start_date

        duration = response.xpath('//p[@class="course-summary__type"]/text()').extract()
        try:
            duration = clear_duration(duration)
            item['duration'] = duration['duration']
            item['duration_per'] = duration['duration_per']
        except:
            pass

        overview = response.xpath('//div[@id="overview"]').extract()
        overview = remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        career = response.xpath('//div[@id="careers"]').extract()
        career = remove_class(career)
        # print(career)
        item['career_en'] = career

        modules = response.xpath('//div[@id="modulesassessment"]').extract()
        modules = remove_class(modules)
        item['modules_en'] = remove_class(modules)

        rntry = response.xpath('//div[@id="entryrequirements"]').extract()
        rntry = remove_class(rntry)
        item['require_chinese_en'] = rntry
        # print(rntry)

        item['ielts'] = '6.0'
        item['ielts_l'] = '5.5'
        item['ielts_s'] = '5.5'
        item['ielts_r'] = '5.5'
        item['ielts_w'] = '5.5'
        item['ielts_desc'] = 'Our standard entry criteria for postgraduate courses is IELTS 6.0 or equivalent, with nothing lower than 5.5 in any of the four elements (listening, speaking, reading and writing).'
        item['toefl'] = '80'
        item['toefl_l'] = '17'
        item['toefl_s'] = '20'
        item['toefl_r'] = '18'
        item['toefl_w'] = '17'
        item['toefl_desc'] = "TOEFL iBT with 80 overall and a minimum of 17 in Writing and Listening, 18 in Reading and 20 in Speaking"
        fee = response.xpath('//div[@id="feesfunding"]//text()').extract()
        tuition_fee = getTuition_fee(fee)
        # print(tuition_fee)
        if tuition_fee == 2018:
            tuition_fee = 0
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = '£'

        department = response.xpath('//a[contains(text(),"Visit your")]/@href').extract()
        department = ''.join(department).split('/')[-1]
        department = department.title().replace('-', ' ')
        item['department'] = department

        how_to_apply = ["<p>Step 1 - Choose your course</p>",
"<p>Step 2 - Submit your application form</p>",
"<p>Step 3 - Check your email regularly</p>",
"<p>Step 5 - Start your visa application</p>",
"<p>Step 4 - Receive our decision on your application</p>",]
        how_to_apply = '\n'.join(how_to_apply)
        item['apply_proces_en'] = how_to_apply

        apply_d = ["<ul><li>Qualification certificates and transcripts, including certified translations, where applicable</li>",
"<li>A personal statement. You can download and complete our Personal Statement Form.</li>",
"<li>References/recommendation letters</li>",
"<li>Curriculum vitae/resume</li>",
"<li>Passport</li>",
"<li>Current and previous visa(s) (if applicable)</li>",
"<li>Proof of name change (if applicable)</li>",
"<li>Portfolio (if applicable)</li></ul>",]
        apply_d = '\n'.join(apply_d)
        item['apply_documents_en'] = apply_d

        ib=response.xpath('//*[contains(text(),"International Baccalaureate")]/text()').extract()
        item['ib']=''.join(ib)
        alevel=response.xpath('//*[contains(text(),"A Level")]/text()|//*[contains(text(),"A-level")]/text()|//*[contains(text(),"A level")]/text()').extract()
        if alevel==[]:
            alevel=response.xpath('//span[contains(text(),"A Level")]//text()').extract()
        if alevel==[]:
            alevel=response.xpath('//p[contains(text(),"A-Level")]//text()').extract()
        if alevel==[]:
            print(response.url)
        else:
            print('GG')
        item['alevel']=''.join(alevel)
        ucascode = response.xpath('//span[contains(text(),"UCAS")]/following-sibling::span/text()').extract()
        # print(ucascode)
        UCAS=re.findall('[A-Z0-9]+',''.join(ucascode))
        ucascode = ''.join(ucascode).strip()

        assessment=response.xpath('//h4[contains(text(),"Assessment")]/following-sibling::*').extract()
        if assessment==[]:
            assessment=response.xpath('//h4[contains(text(),"Assessment")]/..').extract()
        assessment=remove_class(assessment)
        item['assessment_en']=assessment
        yield item

        if ',' in ucascode:
            ucascode = ucascode.split(',')
            for i in ucascode:
                item['ucascode'] = i.strip()
                yield item
        else:
            item['ucascode'] = ucascode
            yield item


        # courseid = response.xpath('//input[@id="erastracode"]/@value').extract()
        # print(courseid)
        # if courseid == ['']:
        #     rntry = response.xpath('//h4[contains(text(),"ain")]/following-sibling::*').extract()
        #     rntry = remove_class(rntry)
        #     # print(rntry)
        #     item['rntry_requirements'] = rntry
        # else:
        #     cid = re.findall('[A-Z0-9]+', courseid[0])
        #     courseid = '%20'.join(cid)
        #     ucas='%2C+'.join(UCAS)
        #     rntry_url = 'https://www.anglia.ac.uk/api/coursewidget/multipleentryrequirements?academicYears=2017%2C2018&moaCode=FT&astraCode=' + courseid+'&ucasCode='+ucas
        #     print(rntry_url)
        #     try:
        #         rntry_content = json.loads(requests.get(rntry_url).text)[0]['GroupItems'][0]['Text'][0]
        #         rntry_content = '<div>' + rntry_content + '</div>'
        #     except:
        #         rntry_content = ''
        #     item['rntry_requirements'] = rntry_content




