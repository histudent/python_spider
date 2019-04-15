# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/30 16:52'
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
from scrapySchool_England.translate_date import tracslateDate
from scrapySchool_England.getTuition_fee import getT_fee
class UniversityofSouthernQueenslandSpider(scrapy.Spider):
    name = 'UniversityofSouthernQueensland_p'
    allowed_domains = ['usq.edu.au/']
    start_urls = []
    C= [
        'https://www.usq.edu.au/study/degrees/master-of-business-administration/finance',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration/project-management',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration/digital-marketing-analytics',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration/digital-marketing-analytics',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration/business-leadership',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration/business-leadership',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration-international/business-leadership',
        'https://www.usq.edu.au/study/degrees/master-of-arts/creative-arts',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration-international/business-leadership',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration-international/finance',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration-international/finance',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration-international/digital-marketing-analytics',
        'https://www.usq.edu.au/study/degrees/master-of-education-commonwealth-supported/guidance-counselling',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration-international/digital-marketing-analytics',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration/general',
        'https://www.usq.edu.au/study/degrees/master-of-learning-and-teaching/primary',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration/general',
        'https://www.usq.edu.au/study/degrees/master-of-education-commonwealth-supported/early-childhood',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration-international/project-management',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration-international/project-management',
        'https://www.usq.edu.au/study/degrees/master-of-project-management',
        'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/big-data-visualisation',
        'https://www.usq.edu.au/study/degrees/master-of-learning-and-teaching/secondary',
        'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/big-data-visualisation',
        'https://www.usq.edu.au/study/degrees/master-of-engineering-science/civil-engineering',
        'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/enterprise-leadership',
        'https://www.usq.edu.au/study/degrees/master-of-engineering-science/electrical-electronic-engineering',
        'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/enterprise-leadership',
        'https://www.usq.edu.au/study/degrees/master-of-engineering-science/environmental-engineering',
        'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/crisis-management',
        'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/crisis-management',
        'https://www.usq.edu.au/study/degrees/master-of-engineering-science/mechanical-engineering',
        'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/finance',
        'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/finance',
        'https://www.usq.edu.au/study/degrees/master-of-engineering-science/power-engineering',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration-international/strategic-marketing',
        'https://www.usq.edu.au/study/degrees/master-of-spatial-science-technology/geographic-information-systems',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration-international/strategic-marketing',
        'https://www.usq.edu.au/study/degrees/master-of-engineering-science/structural-engineering',
        'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/international-business',
        'https://www.usq.edu.au/study/degrees/master-of-engineering-science/agricultural-engineering',
        'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/international-business',
        'https://www.usq.edu.au/study/degrees/master-of-spatial-science-technology/surveying',
        'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/general',
        'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/general',
        'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/sustainable-business',
        'https://www.usq.edu.au/study/degrees/master-of-arts/corporate-communication',
        'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/sustainable-business',
        'https://www.usq.edu.au/study/degrees/master-of-arts/humanities-communication',
        'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/professional-communication',
        'https://www.usq.edu.au/study/degrees/master-of-computing-technology/networking-system-security',
        'https://www.usq.edu.au/study/degrees/master-of-business-and-innovation/professional-communication',
        'https://www.usq.edu.au/study/degrees/master-of-computing-technology/software-the-web',
        'https://www.usq.edu.au/study/degrees/master-of-professional-accounting',
        'https://www.usq.edu.au/study/degrees/master-of-professional-accounting',
        'https://www.usq.edu.au/study/degrees/master-of-education-commonwealth-supported/teaching-english-to-speakers-of-other-languages',
        'https://www.usq.edu.au/study/degrees/master-of-arts/editing-publishing',
        'https://www.usq.edu.au/study/degrees/master-of-education-commonwealth-supported/teaching-english-to-speakers-of-other-languages',
        'https://www.usq.edu.au/study/degrees/master-of-computing',
        'https://www.usq.edu.au/study/degrees/master-of-science/sport-exercise',
        'https://www.usq.edu.au/study/degrees/master-of-science/sport-exercise',
        'https://www.usq.edu.au/study/degrees/master-of-business-administration/digital-transformation',
        'https://www.usq.edu.au/study/degrees/master-of-science/mathematics-statistics',
        'https://www.usq.edu.au/study/degrees/master-of-science/mathematics-statistics',
        'https://www.usq.edu.au/study/degrees/master-of-science/applied-data-science',
        'https://www.usq.edu.au/study/degrees/master-of-science/applied-data-science',
        'https://www.usq.edu.au/study/degrees/master-of-information-systems',
        'https://www.usq.edu.au/study/degrees/master-of-information-systems'
    ]
    # print(len(C))
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Southern Queensland'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.degree_name
        degree_name = response.xpath('//*[@id="main-wrap"]/section[3]/div/div/div[1]/h1').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name).replace('&amp; ','')
        # print(degree_name)

        #4.degree_type
        degree_type = 2

        #5.degree_overview_en
        degree_overview_en = response.xpath('//*[@id="overview"]/div/div').extract()
        degree_overview_en = ''.join(degree_overview_en)
        degree_overview_en = remove_class(degree_overview_en)
        # print(degree_overview_en)

        #6.career_en
        career_en = response.xpath('//*[@id="careerOutcomesCollapse"]/div').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #7.programme_en
        if ' &amp;' in degree_name:
            degree_name = degree_name.replace(' &amp;','')
        if '('in degree_name:
            programme_en = re.findall(r'\((.*)\)',degree_name)[0]
        else:programme_en = degree_name.replace('Master of ','')
        # print(programme_en)

        #8.start_date
        start_date = response.xpath('//*[@id="summary"]/div[3]/div[4]/ul/li').extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        if 'Semester 1 (February)Semester 2 (July)Semester 3 (November)' in start_date:
            start_date = '2,7,11'
        elif 'Semester 1 (February)Semester 2 (July)' in start_date:
            start_date = '2,7'
        elif 'Semester 2 (July)Semester 1 (February)' in start_date:
            start_date = '2,7'
        elif 'Semester 1 (February)' in start_date:
            start_date = '2'
        # print(start_date)

        #9.duration
        duration = response.xpath('//*[@id="summary"]/div[3]/div[6]/ul/li').extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        if '1.5' in duration:
            duration = 1.5
        else: duration =re.findall('\d',duration)[0]
        # print(duration)

        #10.location
        location = response.xpath('//*[@id="summary"]/div[3]/div[7]/ul/li').extract()
        location = ','.join(location)
        location = remove_tags(location)
        # print(location)

        #11.modules_en
        modules_en_url = response.xpath('//*[@id="program-structure"]//div[@class="icon-message__text"]//a/@href').extract()
        modules_en_url = ''.join(modules_en_url)
        headers = {
            "User-Agent": "Mozilla/5.0. (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

        data = requests.get(modules_en_url,headers=headers)
        response2 = etree.HTML(data.text.replace('<?xml version="1.0" encoding="UTF-8"?>',''))
        modules_en = response2.xpath("//h2[contains(text(),'Program structure')]//following-sibling::*")
        doc = ""
        if len(modules_en) > 0:
            for a in modules_en:
                doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                doc = remove_class(doc)
        modules_en = doc

        # print(modules_en)

        #12.tuition_fee
        tuition_fee = response.xpath('//*[@id="fees"]/div/div').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = getT_fee(tuition_fee)
        # print(tuition_fee)

        #13.tuition_fee_pre
        tuition_fee_pre = 'AUD'

        #14.apply_pre
        apply_pre = 'AUD'

        #15.deadline
        deadline = response.xpath('//*[@id="how-to-apply"]/div/div/ul/li').extract()
        deadline = ''.join(deadline)
        deadline = remove_tags(deadline)
        if 'Semester 3' in deadline:
            deadline ='2018-11-5,2019-2-25,2019-7-15'
        else:deadline = '2019-2-25,2019-7-15'
        # print(deadline)

        #16.rntry_requirements_en
        rntry_requirements_en = response.xpath('//*[@id="entry-requirements"]/div/div').extract()
        rntry_requirements_en = ''.join(rntry_requirements_en)
        rntry_requirements_en = remove_class(rntry_requirements_en)
        # print(rntry_requirements_en)

        #17.work_experience_desc_en
        if 'a minimum of two years’ professional work experience, or equivalent.' in rntry_requirements_en:
            work_experience_desc_en = 'a minimum of two years’ professional work experience, or equivalent.'
        elif 'a minimum of one year professional work experience in business, or equivalent.' in rntry_requirements_en:
            work_experience_desc_en = 'a minimum of one year professional work experience in business, or equivalent.'
        elif 'USQ’s Graduate Certificate of Business provides a pathway into the Master of Business and Innovation for students who meet the work experience requirements but do not hold a Graduate Certificate at AQF level 8 or equivalent.' in rntry_requirements_en:
            work_experience_desc_en = 'USQ’s Graduate Certificate of Business provides a pathway into the Master of Business and Innovation for students who meet the work experience requirements but do not hold a Graduate Certificate at AQF level 8 or equivalent.'
        else:work_experience_desc_en = ''
        work_experience_desc_en = '<p>'+work_experience_desc_en+'</p>'

        #18.average_score
        average_score = '75'

        #19.ielts 20212223 24.toefl 25262728
        ielts = 6.5
        ielts_r = 6
        ielts_w = 6
        ielts_s = 6
        ielts_l = 6
        toefl = 90
        toefl_r = 20
        toefl_w = 20
        toefl_s = 20
        toefl_l = 20

        #29.apply_documents_en
        apply_documents_en = '本科毕业证 本科学位证 本科在读证明 本科成绩单 护照 语言成绩 个人简历（可选）个人陈述（可选）推荐信（可选）'

        #30.apply_desc_en
        apply_desc_en = "<p>How to apply 1. Choose a degree Choose the degree you want to apply for.2. Check you meet the entry requirements Check the degree details to find out the entry requirements.Check the standard undergraduate entry requirements by country.All students must also meet USQ's English Language Requirements. 3. Collect supporting documentationAlong with your application you will need to also submit certified copies of:award certificates academic transcripts formal identity papers, such as your passport, national identity card, and student visa.If your documents are not in English, you will need to supply a certified English translation.If you applying for on-campus study, and are under 18 years of age at time of application, we will require additional information to ensure that the requirements of Standard 5 - Younger Students, of the 2018 Education Services for Overseas Students (ESOS) National Code, and the USQ U18 International Student Care Framework are satisfied. Please complete and attach the U18 Welfare and Accommodation form to your USQ application for admission.4. Submit application There is no application or assessment fee to apply to study with USQ.Before you submit your application, make sure you have attached all certified supporting documentation. This will ensure we are able to provide a faster turnaround time for your application.Studying on-campus USQ is obligated to ensure that all students studying on-campus on a student visa are genuine students, who meet the Genuine Temporary Entrant (GTE) criteria outlined in the Department of Home Affairs Simplified Student Visa Framework (SSVF). Some of the factors that are considered under the existing requirement to be a genuine applicant for entry and study as a student include: English language proficiency; financial capacity; age requirements; and intention to comply with visa conditions. Please visit the Department of Home Affairs for further information. Our admissions team will consider all your application information and make an assessment as to whether the requirements are met in your particular case. Paper application form Our on-line application system has been designed to work on desktop or mobile devices. If you are unable to apply online, you can download our International Student application form and email to the admissions team.  Application form (PDF 321 KB) Professional Development Single Courses Application Form (PDF 71 KB) Credit for previous study If you have studied or worked previously you be eligible for credit. Have a look at our Credit Calculator. You can apply for credit within the online application form. If you’re applying for credit you will need to provide further supporting documentation including: A copy of an approved course synopsis for the year in which the subject was successfully completed If your documents aren't in English, you'll need to supply a certified English translation.   When to apply? USQ accepts applications all year round. USQ receives thousands of applications each year so it is important to apply early, to make sure you secure a place and to allow time for you to make your necessary study arrangements (e.g. visa, organise family and work commitments). Semester start dates are: Semester 1, 2018 - 26 February 2018 Semester 2, 2018 - 16 July 2018 Semester 3, 2018 - 19 November 2018 Semester 1, 2019 - 25 February 2019 Semester 2, 2019 - 15 July 2019How long will it take to have my application processed?Whilst USQ endeavors to process your application to study as soon as possible, the below guide provides examples of the typical application processing times, you can help us by ensuring you have supplied full information at time of applicatoin: Undergraduate applications: allow up to two weeks from the time all supporting certified documentation is submitted. where additional assessment requried for course credits and exemptions, this may take longer. Postgraduate coursework applications: allow two weeks from the time all supporting certified documentation is submitted. where additional assessment requried for course credits andexemptions, this may take longer. Postgraduate research applications: should allow a minimum of 25 working days for assessment, however this can be impacted by the availability of an appropriate supervisor. </p>"

        item['university'] = university
        item['url'] = url
        item['degree_name'] = degree_name
        item['degree_type'] = degree_type
        item['degree_overview_en'] = degree_overview_en
        item['career_en'] = career_en
        item['programme_en'] = programme_en
        item['start_date'] = start_date
        item['duration'] = duration
        item['location'] = location
        item['modules_en'] = modules_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_pre'] = apply_pre
        item['deadline'] = deadline
        item['rntry_requirements_en'] = rntry_requirements_en
        item['work_experience_desc_en'] = work_experience_desc_en
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
        yield  item
