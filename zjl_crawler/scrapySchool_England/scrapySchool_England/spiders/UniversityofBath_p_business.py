# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/25 11:11'
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
from scrapySchool_England.TranslateMonth import translate_month
from lxml import etree
import requests
class UniversityofBathSpider(scrapy.Spider):
    name = 'UniversityofBath_p_business'
    allowed_domains = ['bath.ac.uk/']
    start_urls = []
    C= [
        'http://management-masters.bath.ac.uk/course/management/',
        'http://management-masters.bath.ac.uk/course/accounting-and-finance/',
        'http://management-masters.bath.ac.uk/course/finance/',
        'http://management-masters.bath.ac.uk/course/finance-with-banking/',
        'http://management-masters.bath.ac.uk/course/finance-with-risk-management/',
        'http://management-masters.bath.ac.uk/course/business-analytics/',
        'http://management-masters.bath.ac.uk/course/entrepreneurship-and-management/',
        'http://management-masters.bath.ac.uk/course/human-resource-management-and-consulting/',
        'http://management-masters.bath.ac.uk/course/innovation-and-technology-management/',
        'http://management-masters.bath.ac.uk/course/international-management/',
        'http://management-masters.bath.ac.uk/course/marketing/',
        'http://management-masters.bath.ac.uk/course/operations-logistics-and-supply-chain-management/',
        'http://management-masters.bath.ac.uk/course/sustainability-and-management/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Bath'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.degree_name
        degree_name = response.xpath('//*[@id="content"]/div/div/h1').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        degree_name = degree_name.split()[0]
        # print(degree_name)

        #4.programme_en
        programme_en = response.xpath('//*[@id="content"]/div/div/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        programme_en = programme_en.replace(degree_name,'').replace('in ','').strip()
        # print(programme_en)

        #5.degree_type
        degree_type = 2

        #6.duration
        duration = '1'

        #7.start_date
        start_date = '2018-10-1'

        #8.teach_type
        teach_type ='Taught'

        #9.overview_en
        overview_en = response.xpath('//*[@id="content"]/section[2]/div/div[3]/p').extract()
        overview_en = ''.join(overview_en)
        # overview_en = clear_space_str(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #10.modules_en
        modules_url  = url+'content-and-structure/'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        data = requests.get(modules_url,headers = headers)
        # print(data)
        response1 = etree.HTML(data.text)
        modules_en = response1.xpath('//*[@id="content"]/section[3]/div[2]/div[1]/div[1]/div[2]/div/ul[1]')
        doc = ""
        if len(modules_en) > 0:
            for a in modules_en:
                doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                doc = remove_class(doc)
        # print(doc)

        #11.assessment_en
        assessment_en = 'Units are assessed by a combination of formal examinations and coursework.'
        assessment_en = '<p>' + assessment_en+ '</p>'
        # print(assessment_en)

        #12.require_chinese_en
        require_chinese_en = '<p>A four-year Bachelor’s degree with a final overall score of at least 80% depending on the institution attended.To apply for this course you may have an undergraduate degree in any subject.We may make an offer based on a lower grade if you can provide evidence of your suitability for the degree.</p>'

        #13.career_en
        career_en_url = url+'careers/'
        data2 = requests.get(career_en_url, headers=headers)
        # print(data2)
        response2 = etree.HTML(data2.text)
        career_en = response2.xpath('//*[@id="here"]/div/div[2]/ul/li/text()')
        career_en = ' '.join(career_en)
        career_en = '<p>'+career_en+'</p>'
        # print(career_en)

        #14.ielts 15161718
        ielts_list_url = url+'entry-requirements/'
        data3 = requests.get(ielts_list_url, headers=headers)
        # print(data3)
        response3 = etree.HTML(data3.text)
        ielts_list = response3.xpath('//*[@id="content"]/section[2]/div/div[1]/section[2]/div/div/p//strong/text()')
        ielts_list = ''.join(ielts_list)
        try:
            a = re.findall(r'[567]\.\d',ielts_list)[0]
            b = re.findall(r'[567]\.\d',ielts_list)[1]
        except:
            a = 7
            b = 6.5
        ielts = a
        ielts_r = b
        ielts_w = b
        ielts_l = b
        ielts_s = b

        # print(ielts,ielts_l,ielts_w,ielts_s,ielts_r)

        #19.teach_time
        teach_time = 'Full-Time'

        #20.deadline
        deadline = '2018-6-30'
        # print(deadline)

        #21.location
        location = 'Bath'

        #22.department
        department = 'Management'
        # print(department)

        #23.apply_proces_en
        apply_proces_en = 'https://www.bath.ac.uk/study/pg/applications.pl'

        #24.tuition_fee_pre
        tuition_fee_pre = '£'

        #25.other
        other = 'http://www.bath.ac.uk/corporate-information/faculty-of-humanities-social-sciences-taught-postgraduate-tuition-fees-2018-19/'

        #26.duration_per
        duration_per = 1

        #27.tuition_fee
        if 'Finance with Risk Management' in programme_en:
            tuition_fee = 24500
        elif 'Finance with Banking' in programme_en:
            tuition_fee = 24500
        elif 'Finance' in programme_en:
            tuition_fee = 24500
        else:
            tuition_fee = 19500

        #28.apply_documents_en
        apply_documents_en = '<p>Apply for a course To apply for a course, you must use the online application form. You will need to create an account before you can start the application process. On the application form, you will need to give: your personal details the date you plan to start studying your education details proof of your English level if English is not your first language the name and contact details of an academic referee from your current or most recent place of study your personal statement, explaining your reasons for wishing to study the course your supporting information Supporting information So we can assess your application and make our decision, you will need to give us all the necessary supporting information, including: a scan of your undergraduate degree certificate and your postgraduate degree certificate, if you have one a scan of your final degree transcript or your most recent transcript if you are still studying an academic reference from your current or most recent place of study, if you have one an up-to-date CV payment of the application fee, if applicable You can also upload supporting documents through Application Tracker after you have submitted your online application. International applicants If you are an international student, you should also give us: your passport details if you need a Tier 4 visa an authorised translation of your degree certificate and transcript if they are not in English your English language assessment certificate, if available Track your application We will send you login details for Application Tracker when you have submitted your application. We aim to make decisions about applications within six weeks of receiving all your supporting information and will tell you whether or not you have been successful through Application Tracker. You can also check the progress of your application there. We may also contact you for more information or, depending on the course you apply for, to invite you to an interview. Accept your offer If you receive an offer, use Application Tracker to accept or decline as soon as possible. For some courses, you will need to pay a deposit when you accept your offer. Receiving an unconditional offer If you receive an unconditional offer, you have met all the required academic conditions and we are offering you a place. Receiving a conditional offer If you receive a conditional offer, you may not have met all the requirements, but we hope you will be able to do so. These requirements may include English language scores, degree results, satisfactory references or payment of a deposit. You must meet these requirements and submit evidence of them through Application Tracker before you can start your studies. If you need to improve your English language skills before starting your studies, you may be able to take a pre-sessional course to reach the required level. When you meet the conditions of your offer, we will contact you and tell you what to do next.</p>'
        #29.apply_pre
        apply_pre = '£'

        #35.rntry_requirements
        rntry_requirements = response.xpath('//*[@id="content"]/section[2]/div/div[1]/div/ul/li[4]/p[2]').extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        item['rntry_requirements'] = rntry_requirements
        item['apply_pre'] = apply_pre
        item['apply_documents_en'] = apply_documents_en
        item['tuition_fee'] = tuition_fee
        item['university'] = university
        item['url'] = url
        item['degree_name'] = degree_name
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['start_date'] = start_date
        item['teach_type'] = teach_type
        item['overview_en'] = overview_en
        item['modules_en'] = doc
        item['assessment_en'] = assessment_en
        item['require_chinese_en'] = require_chinese_en
        item['career_en'] = career_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['teach_time'] = teach_time
        item['deadline'] = deadline
        item['location'] = location
        item['department'] = department
        item['apply_proces_en'] = apply_proces_en
        item['tuition_fee_pre'] = tuition_fee_pre
        item['other'] = other
        yield  item