# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/30 16:31'
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
from scrapySchool_England.clearSpace import clear_space_str
import requests
from lxml import etree
class UniversityofDivinitySpider(scrapy.Spider):
    name = 'UniversityofDivinity_u'
    allowed_domains = ['divinity.edu.au/']
    start_urls = []
    C= [
        'https://www.divinity.edu.au/study/our-courses/bachelor-of-ministry/',
        'https://www.divinity.edu.au/study/our-courses/bachelor-of-theology/'
    ]
    # print(len(C))
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Divinity'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.degree_name
        degree_name = response.xpath('//*[@id="content"]/p[1]').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #4.programme_en
        programme_en = degree_name.replace('Bachelor of ','')
        # print(programme_en)

        #5.location
        location = 'Melbourne, Victoria'

        #6.department
        department = response.xpath('//*[@id="content"]/ul[1]/li').extract()
        department = ','.join(department)
        department = remove_tags(department)
        # print(department)

        #7.duration
        duration = 3

        #8.degree_overview_en
        degree_overview_en = response.xpath("//*[contains(text(),'What this course is about')]//following-sibling::*[1]").extract()
        degree_overview_en = ''.join(degree_overview_en)
        degree_overview_en = remove_class(degree_overview_en)
        # print(degree_overview_en)

        #9.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'Cost of study')]//following-sibling::*[1]").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #10.tuition_fee_pre
        tuition_fee_pre = '$'

        #11.apply_pre
        apply_pre = '$'

        #12.start_date
        start_date = '2,7'

        #13.modules_en
        modules_en = response.xpath("//h2[contains(text(),'Course structure')]//following-sibling::p").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #14.career_en
        career_en= response.xpath('//*[@id="content"]/ol/li').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #15.deadline
        deadline = '2月入学:11月15日;7月入学：4月15日'

        #16.apply_fee
        apply_fee = 300

        #17.rntry_requirements_en
        rntry_requirements_en = response.xpath("//*[contains(text(),'Admission criteria')]//following-sibling::*[1]").extract()
        rntry_requirements_en = ''.join(rntry_requirements_en)
        rntry_requirements_en = remove_class(rntry_requirements_en)
        # print(rntry_requirements_en)

        #18.average_score
        average_score = 75

        #19.ielts 20212223
        ielts = 6.5
        ielts_l = 6
        ielts_s = 6
        ielts_w = 6
        ielts_r = 6

        #24.toefl 252622728
        toefl = 79
        toefl_l= 12
        toefl_s= 18
        toefl_r = 13
        toefl_w = 21

        #29.apply_documents_en
        apply_documents_en = '<p>copies of official academic transcripts of all relevant tertiary courses, copies of your birth certificate, current passport or other official documents verifying your citizenship status in your current name, copies of English language qualification, complete research training experience, publications and scholarship details, provide a research proposal, Arrange for a Confidential Academic Referee Report from your two listed referees to be sent to the Research Office separately, Enclose CVs of proposed supervisors, Doctoral research scholarship applicants should also send complete research scholarship applicantion form</p>'

        #30.apply_desc_en
        apply_desc_en = '<p>Step 1: Select a course The University offers a wide variety of awards, from diplomas to doctorates. Finding the right course of study will depend partly on your prior academic qualifications and partly on your objectives. Step 2: Select a College We are a collegiate University. This means each student studies at the University through one of its Colleges. The College is your primary learning community and will provide you with course advice and support services throughout your studies. Our Colleges cover a wide range of Christian traditions and places. The choice of a College might depend on your own faith tradition, where you live, or which course you want to study; each College offers a different selection of the University’s courses. Step 3: Attend an interview It is a requirement that all students attend an admissions interview with an academic advisor at a College. This will be a Coursework Coordinator in the case of coursework applicants, and a Research Coordinator in the case of higher degree by research applicants. The interview may be conducted by telephone or email or similar means.  The purpose of the interview is to help you choose the right course, to ensure you meet the admission requirements, and to plan a program of study appropriate to your course and your needs. Step 4: Complete a form Download the Application for Admission if you are new to the University or are enrolling in a new course. If you are a re-enrolling student, download the Re-enrolment form. Complete the form,following the instructions carefully. You will need to submit the completed form, together with supporting documentation (either originals or certified copies) to your College. Step 5: Pay tuition fees Domestic students: Payment of tuition fees must be provided with the application form. Australian citizens can pay in three ways:FEE-HELP: This is a student loan scheme in which the Commonwealth Government pays the student’s tuition fees. Students pay back the fees through taxation if and when the student’s incomerises above a minimum repayment threshold.    Upfront: Students may pay by BPAY, credit card or cheque (payable to University of Divinity)    Sponsorship: Students whose fees are being met by a third party must provide a letter from the sponsor on letterhead accepting responsibility for the fees.</p>'

        item['university'] = university
        item['url'] = url
        item['degree_name'] = degree_name
        item['programme_en'] = programme_en
        item['location'] = location
        item['department'] = department
        item['duration'] = duration
        item['degree_overview_en'] = degree_overview_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_pre'] = apply_pre
        item['start_date'] = start_date
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['deadline'] = deadline
        item['apply_fee'] = apply_fee
        item['rntry_requirements_en'] = rntry_requirements_en
        item['average_score'] = average_score
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['apply_documents_en'] = apply_documents_en
        item['apply_desc_en'] = apply_desc_en
        yield item