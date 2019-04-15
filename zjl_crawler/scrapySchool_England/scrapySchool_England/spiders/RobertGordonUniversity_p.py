# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/9 15:52'
import scrapy,json
import re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from w3lib.html import remove_tags
from scrapySchool_England.clearSpace import  clear_space_str
from scrapySchool_England.translate_date import  tracslateDate
from scrapySchool_England.translate_date import tracslateDate
from lxml import  etree
import  requests
from scrapySchool_England.TranslateMonth import translate_month
class RobertGordonUniversitySpider(scrapy.Spider):
    name = 'RobertGordonUniversity_p'
    allowed_domains = ['rgu.ac.uk/']
    start_urls = []
    C= [
        'https://www.rgu.ac.uk/study/courses/957-pgcert-pgdip-msc-data-science',
'https://www.rgu.ac.uk/study/courses/1050-pgcert-pgdip-msc-digital-marketing',
'https://www.rgu.ac.uk/study/courses/955-pgcert-pgdip-msc-corporate-social-responsibility',
'https://www.rgu.ac.uk/study/courses/469-pgcert-pgdip-msc-cyber-security',
'https://www.rgu.ac.uk/study/courses/1051-pgcert-pgdip-msc-corporate-communications-and-public-affairs',
'https://www.rgu.ac.uk/study/courses/942-pgcert-pgdip-ma-curatorial-studies',
'https://www.rgu.ac.uk/study/courses/951-pgcert-pgdip-msc-construction-project-management',
'https://www.rgu.ac.uk/study/courses/693-msc-analytical-science-environmental-analysis',
'https://www.rgu.ac.uk/study/courses/690-msc-analytical-science-drug-analysis-and-toxicology',
'https://www.rgu.ac.uk/study/courses/964-pgcert-pgdip-msc-advancing-nursing-practice',
'https://www.rgu.ac.uk/study/courses/694-msc-analytical-science-food-analysis-authenticity-and-safety',
'https://www.rgu.ac.uk/study/courses/929-pgcert-pgdip-msc-architectural-design-innovation',
'https://www.rgu.ac.uk/study/courses/936-master-of-architecture-part-2',
'https://www.rgu.ac.uk/study/courses/1150-msc-biomedical-technology',
'https://www.rgu.ac.uk/study/courses/1177-msc-business-analytics',
'https://www.rgu.ac.uk/study/courses/1107-msc-clinical-pharmacy-service-developmenta',
'https://www.rgu.ac.uk/study/courses/941-pgcert-pgdip-ma-communication-design',
'https://www.rgu.ac.uk/study/courses/456-pgcert-pgdip-msc-computer-science',
'https://www.rgu.ac.uk/study/courses/926-msc-petroleum-production-engineering',
'https://www.rgu.ac.uk/study/courses/919-msc-physiotherapy-pre-registration',
'https://www.rgu.ac.uk/study/courses/814-pgcert-pgdip-msc-procurement-and-supply-chain-management',
'https://www.rgu.ac.uk/study/courses/938-pgcert-pgdip-ma-product-design',
'https://www.rgu.ac.uk/study/courses/918-msc-public-health-and-health-promotion',
'https://www.rgu.ac.uk/study/courses/822-pgcert-pgdip-msc-project-management',
'https://www.rgu.ac.uk/study/courses/896-msc-drilling-and-well-engineering',
'https://www.rgu.ac.uk/study/courses/856-pgcert-pgdip-msc-energy-management',
'https://www.rgu.ac.uk/study/courses/935-msc-exercise-health-and-wellness-coaching',
'https://www.rgu.ac.uk/study/courses/940-pgcert-pgdip-ma-fashion-textiles',
'https://www.rgu.ac.uk/study/courses/713-pgcert-pgdip-msc-fashion-management',
'https://www.rgu.ac.uk/study/courses/860-pgcert-pgdip-msc-financial-management',
'https://www.rgu.ac.uk/study/courses/939-pgcert-pgdip-ma-fine-art',
'https://www.rgu.ac.uk/study/courses/689-pgcert-pgdip-msc-management',
'https://www.rgu.ac.uk/study/courses/571-mba-master-of-business-administration',
'https://www.rgu.ac.uk/study/courses/570-mba-master-of-business-administration-oil-and-gas-management',
'https://www.rgu.ac.uk/study/courses/563-msc-offshore-engineering-systems',
'https://www.rgu.ac.uk/study/courses/862-msc-oil-and-gas-accounting-and-finance',
'https://www.rgu.ac.uk/study/courses/928-msc-oil-and-gas-engineering',
'https://www.rgu.ac.uk/study/courses/455-msc-llm-oil-and-gas-law',
'https://www.rgu.ac.uk/study/courses/812-pgcert-pgdip-msc-human-resource-management',
'https://www.rgu.ac.uk/study/courses/931-msc-information-and-library-studies',
'https://www.rgu.ac.uk/study/courses/877-pgcert-pgdip-msc-information-technology',
'https://www.rgu.ac.uk/study/courses/933-pgcert-pgdip-msc-information-technology-with-business-intelligence',
'https://www.rgu.ac.uk/study/courses/932-pgcert-pgdip-msc-information-technology-with-cyber-security',
'https://www.rgu.ac.uk/study/courses/894-pgcert-pgdip-msc-information-technology-with-network-management',
'https://www.rgu.ac.uk/study/courses/688-pgcert-pgdip-msc-international-business',
'https://www.rgu.ac.uk/study/courses/967-pgcert-pgdip-msc-social-work',
'https://www.rgu.ac.uk/study/courses/424-msc-solar-energy-systems',
'https://www.rgu.ac.uk/study/courses/1053-pgcert-pgdip-msc-international-marketing-management',
'https://www.rgu.ac.uk/study/courses/1056-pgcert-pgdip-msc-international-tourism-and-hospitality-management',
'https://www.rgu.ac.uk/study/courses/882-pgcert-pgdip-msc-it-for-the-oil-and-gas-industry',
'https://www.rgu.ac.uk/study/courses/937-pgcert-pgdip-ma-jewellery',
'https://www.rgu.ac.uk/study/courses/716-pgcert-pgdip-msc-journalism',
'https://www.rgu.ac.uk/study/courses/849-llm-law',
'https://www.rgu.ac.uk/study/courses/845-llm-law-and-dispute-resolution',
'https://www.rgu.ac.uk/study/courses/846-llm-law-and-energy-law',
'https://www.rgu.ac.uk/study/courses/847-llm-law-and-international-commercial-law',
'https://www.rgu.ac.uk/study/courses/848-llm-law-and-international-law'
    ]
    # print(len(C))
    # C = set(C)
    # print(len(C))
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Robert Gordon University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="flexicontent"]/article//h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        degree_name = response.xpath('//*[@id="flexicontent"]/article/div[1]//p').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #6.department
        department = response.xpath('//*[@id="flexicontent"]/article/div[2]//h3/a').extract()
        department = ''.join(department)
        department = remove_tags(department).replace('&amp;','')
        # print(department)

        #7.apply_proces_en
        apply_proces_en = response.url + '#apply_container'

        #8.overview_en
        overview_en = response.xpath("//div[@class='study-options-banner-text']/../../../preceding-sibling::*").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #9.teach_time
        teach_time = response.xpath("//*[contains(text(),'Mode of Study')]//following-sibling::*").extract()
        teach_time = ''.join(teach_time)
        teach_time = remove_tags(teach_time)
        if 'Full Time' in teach_time:
            teach_time = 'Full Time'
        else:
            teach_time = 'Part Time'
        # print(teach_time)

        #10.start_date
        start_date = response.xpath('//*[@id="study-options-lists"]/div[2]/div[3]/text()').extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        if 'Block one attendance: 12 - 14 September 2018 Block two attendance: 5 - 7 December 2018'in start_date:
            start_date = '2018-9-12,2018-12-5'
        elif '24 January 2019' in start_date:
            start_date = '2019-1-24'
        elif 'September / January September / January' in start_date:
            start_date = '2018-9,2019-1'
        elif 'September January' in start_date:
            start_date = '2018-9,2019-1'
        elif 'January or September' in start_date:
            start_date = '2018-9,2019-1'
        elif 'January, May or September' in start_date:
            start_date = '2019-1,2019-5,2019-9'
        else:
            start_date = translate_month(start_date)
            if start_date == 1:
                start_date = '2019-1'
            else:
                start_date = '2018-'+ str(start_date)
        # print(start_date)

        #11.duration #12.duration_per
        # duration_a = response.xpath('//*[@id="study-options-lists"]/div[2]/div[4]').extract()
        # duration_a = ''.join(duration_a)
        # duration_a = remove_tags(duration_a)
        # # print(duration)
        # duration=re.findall('\d+',duration_a)[0]
        # if 'year' in duration_a:
        #     duration_per= 1
        # else:
        #     duration_per = 3
        # print(duration,'*******',duration_per)

        #13.modules_en
        try:
            modulesurl = response.xpath('//*[@id="tab-1"]/a/@href').extract()[0]
        except:
            modulesurl = ''
        print(modulesurl)
        if len(modulesurl)!=0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data = requests.get(modulesurl, headers=headers)
            response1 = etree.HTML(data.text)
            modules_en =  response1.xpath('//*[@id="content"]//table')
            doc = ""
            if len(modules_en) > 0:
                for a in modules_en:
                    doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc = remove_class(doc)
                    modules_en = doc


        #14.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'Assessment')]//following-sibling::*").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #15.career_en
        career_en = response.xpath("//*[contains(text(),'Job Prospects')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en= remove_class(career_en)
        # print(career_en)

        #16.rntry_requirements
        rntry_requirements = response.xpath('//*[@id="tab-4"]/div/div[1]/div').extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #17.ielts 18,19,20,21
        ielts_list = response.xpath("//*[contains(text(),'English Language Requirements')]//following-sibling::*").extract()
        ielts_list = ''.join(ielts_list)
        ielts_list = remove_tags(ielts_list)
        try:
            ielts = re.findall('\d\.\d',ielts_list)
        except:
            ielts = ''
        if len(ielts) ==2:
            a=ielts[0]
            b= ielts[1]
            ielts = a
            ielts_r =b
            ielts_w =b
            ielts_s =b
            ielts_l =b
        else:
            ielts = 6.5
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
        # print(ielts,ielts_r,ielts_l,ielts_s,ielts_w)

        #21.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'International Students')]/../following-sibling::*|//*[contains(text(),'International Students')]//following-sibling::*|//*[contains(text(),'Students')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(response.url)
        # print(tuition_fee)

        #22.tuition_fee_pre
        tuition_fee_pre = '£'

        #23.apply_documents_en
        apply_documents_en = '<p>Before you begin, make sure you know the name of the course you are applying for and have copies of all relevant documents to hand. Certificates and/or transcripts for qualifications you have completed Curriculum Vitae (CV)/Resumé Any letter of reference you may have Copy of the details page of your passport (non-EU applicants applying for full time study)</p>'
        #24.apply_pre
        apply_pre = '£'


        item['apply_documents_en'] = apply_documents_en
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['department'] = department
        item['apply_proces_en'] = apply_proces_en
        item['overview_en'] = overview_en
        item['teach_time'] = teach_time
        item['start_date'] = start_date
        # item['duration'] = duration
        # item['duration_per'] = duration_per
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['rntry_requirements'] = rntry_requirements
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        yield  item

    def parse_getmodules(self,modulesurl):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        data = requests.get(headers=headers,url = modulesurl)
        response = etree.HTML(data.text)
        datadict ={}
        modules_en = response.xpath('//*[@id="content"]//a/text()')
        modules_en = '\n'.join(modules_en)
        # print(modules_en)
        datadict['modules_en'] = modules_en
        return datadict