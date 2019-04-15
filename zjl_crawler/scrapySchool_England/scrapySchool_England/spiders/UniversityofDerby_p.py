# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/10 16:23'
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
class UniversityofDerbySpider(scrapy.Spider):
    name = 'UniversityofDerby_p'
    allowed_domains = ['derby.ac.uk/']
    start_urls = []
    C = [
        'https://www.derby.ac.uk/postgraduate/accounting-courses/accounting-finance-msc/',
        'https://www.derby.ac.uk/postgraduate/computing-courses/cyber-security-msc/',
        'https://www.derby.ac.uk/postgraduate/education-courses/childhood-ma/',
        'https://www.derby.ac.uk/postgraduate/art-design-courses/fine-art-ma/',
        'https://www.derby.ac.uk/postgraduate/business-courses/mba/',
        'https://www.derby.ac.uk/postgraduate/hospitality-culinary-management-courses/international-hospitality-management-msc/',
        'https://www.derby.ac.uk/postgraduate/criminology-policing-courses/financial-investigation-digital-intelligence-msc/',
        'https://www.derby.ac.uk/postgraduate/criminology-policing-courses/intelligence-security-and-disaster-management-msc/',
        'https://www.derby.ac.uk/postgraduate/mechanical-manufacturing-engineering-courses/strategic-engineering-management-msc/',
        'https://www.derby.ac.uk/postgraduate/mechanical-manufacturing-engineering-courses/mechanical-manufacturing-engineering-msc/',
        'https://www.derby.ac.uk/postgraduate/art-design-courses/visual-communication-ma/',
        'https://www.derby.ac.uk/postgraduate/computing-courses/big-data-analytics-msc/',
        'https://www.derby.ac.uk/postgraduate/computing-courses/information-technology-msc/',
        'https://www.derby.ac.uk/postgraduate/health-social-community-work-courses/social-work-ma/',
        'https://www.derby.ac.uk/postgraduate/education-courses/education-early-years-ma/',
        'https://www.derby.ac.uk/postgraduate/photography-courses/film-and-photography-ma/',
        'https://www.derby.ac.uk/postgraduate/nursing-health-care-practice-courses/nursing-adult-msc/',
        'https://www.derby.ac.uk/postgraduate/therapeutic-practice-courses/dance-movement-psychotherapy-ma/',
        'https://www.derby.ac.uk/postgraduate/forensic-science-courses/forensic-science-mres/',
        'https://www.derby.ac.uk/postgraduate/mathematics-courses/computational-mathematics-msc/',
        'https://www.derby.ac.uk/postgraduate/computing-courses/mobile-app-development-msc/',
        'https://www.derby.ac.uk/postgraduate/education-courses/careers-education-coaching-ma/',
        'https://www.derby.ac.uk/postgraduate/business-courses/international-business-hrm-msc/',
        'https://www.derby.ac.uk/postgraduate/biology-zoology-courses/conservation-biology-msc/',
        'https://www.derby.ac.uk/postgraduate/architecture-architectural-technology-courses/sustainable-architecture-healthy-buildings-msc/',
        'https://www.derby.ac.uk/postgraduate/architecture-architectural-technology-courses/building-info-modelling-project-collab-msc/',
        'https://www.derby.ac.uk/postgraduate/education-courses/education-lifelong-learning-ma/',
        'https://www.derby.ac.uk/postgraduate/computing-courses/advanced-computer-networks-msc/',
        'https://www.derby.ac.uk/postgraduate/biomedical-health-courses/biomedical-health-msc/',
        'https://www.derby.ac.uk/postgraduate/education-courses/education-tesol-ma/',
        'https://www.derby.ac.uk/postgraduate/education-courses/educational-leadership-ma/',
        'https://www.derby.ac.uk/postgraduate/fashion-textiles-courses/fashion-textiles-ma/',
        'https://www.derby.ac.uk/postgraduate/education-courses/inclusion-and-send-ma/',
        'https://www.derby.ac.uk/postgraduate/mechanical-manufacturing-engineering-courses/advanced-materials-and-additive-manufacturing-msc/',
        'https://www.derby.ac.uk/postgraduate/nursing-health-care-practice-courses/nursing-mental-health-msc/',
        'https://www.derby.ac.uk/postgraduate/events-management-courses/events-management-msc/',
        'https://www.derby.ac.uk/postgraduate/education-courses/education-send-ma/',
        'https://www.derby.ac.uk/postgraduate/biomedical-health-courses/biological-sciences-mres/',
        'https://www.derby.ac.uk/postgraduate/therapeutic-practice-courses/music-therapy-ma/',
        'https://www.derby.ac.uk/postgraduate/education-courses/education-coaching-mentoring-ma/',
        'https://www.derby.ac.uk/postgraduate/education-courses/education-primary-mathematics-ma/',
        'https://www.derby.ac.uk/postgraduate/music-music-production-courses/music-production-ma/',
        'https://www.derby.ac.uk/postgraduate/education-courses/education-leadership-management-ma/',
        'https://www.derby.ac.uk/postgraduate/entertainment-engineering-courses/audio-engineering-msc/',
        'https://www.derby.ac.uk/postgraduate/electrical-electronic-engineering-courses/control-instrumentation-msc/',
        'https://www.derby.ac.uk/postgraduate/education-courses/education-ma-full-time/',
        'https://www.derby.ac.uk/postgraduate/therapeutic-practice-courses/cognitive-behavioural-psychotherapy-msc/',
        'https://www.derby.ac.uk/postgraduate/criminology-policing-courses/criminal-justice-and-criminology-msc/',
        'https://www.derby.ac.uk/postgraduate/civil-engineering-construction-courses/civil-engineering-msc/',
        'https://www.derby.ac.uk/postgraduate/sport-exercise-courses/applied-sport-exercise-science-msc/',
        'https://www.derby.ac.uk/postgraduate/social-political-sciences-courses/social-and-political-studies-ma/',
        'https://www.derby.ac.uk/postgraduate/radiography-courses/diagnostic-radiography-msc/',
        'https://www.derby.ac.uk/postgraduate/english-creative-writing-publishing-courses/creative-writing-ma/',
        'https://www.derby.ac.uk/postgraduate/criminology-policing-courses/criminal-investigation-msc/',
        'https://www.derby.ac.uk/postgraduate/english-creative-writing-publishing-courses/publishing-ma/',
        'https://www.derby.ac.uk/postgraduate/computing-courses/digital-forensics-computer-security-msc/',
        'https://www.derby.ac.uk/postgraduate/motorsport-engineering-courses/motorsport-engineering-msc/',
        'https://www.derby.ac.uk/postgraduate/business-courses/international-business-marketing-msc/',
        'https://www.derby.ac.uk/postgraduate/spa-wellness-management-courses/international-spa-management-msc/',
        'https://www.derby.ac.uk/postgraduate/therapeutic-practice-courses/dramatherapy-ma/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Derby'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//h1/strong').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        degree_name = response.xpath('//h1/text()').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #6.overview_en
        overview_en = response.xpath("//*[contains(text(),'Course description')]/../following-sibling::section[1]").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #7.career_en
        career_en = response.xpath("//*[contains(text(),'Careers')]/../following-sibling::*[1]").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #8.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'Assessment')]/../following-sibling::p").extract()
        if len(assessment_en)==0:
            assessment_en = response.xpath('//h3[contains(text(),"ssessed")]//following-sibling::*').extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #9.teach_time
        teach_time_list = response.xpath("//*[contains(text(),'Study options')]//following-sibling::*").extract()
        teach_time_list = ''.join(teach_time_list)
        teach_time_list = remove_tags(teach_time_list)
        # print(teach_time_list)
        if 'Full-time' in teach_time_list:
            teach_time = 'Full-time'
        else: teach_time = 'Part-time'
        # print(teach_time)

        #10.duration#11.duration_per
        try:
            duration = re.findall('\d+',teach_time_list)[0]
        except:
            duration = 1
        if int(duration)>4:
            duration_per = 3
        else:
            duration_per = 1
        # print(duration,duration_per)

        #12.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'International fee')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        if tuition_fee ==0:
            tuition_fee = 13500
        # print(tuition_fee)

        #13.tuition_fee_pre
        tuition_fee_pre = '£'

        #14.location
        location = response.xpath("//*[contains(text(),'Location')]//following-sibling::*").extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #15.start_date
        start_date = response.xpath("//*[contains(text(),'Start dates')]//following-sibling::*").extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        if len(start_date)==0:
            start_date = 9
        else:
            start_date = '9,1'
        # print(start_date,url)

        #16.apply_proces_en
        apply_proces_en = 'https://www.derby.ac.uk/services/admissions/apply-online/?section_id=2560'

        #17.rntry_requirements
        rntry_requirements = response.xpath("//h2[contains(text(),'Entry requirements')]/../following-sibling::*[1]").extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #18.ielts 19202122
        try:
            ielts = re.findall('\d\.\d',rntry_requirements)
            if '2.1' in ielts:
                ielts.remove('2.1')
                if '2.1' in ielts:
                    ielts.remove('2.1')
                    if '2.2' in ielts:
                        ielts.remove('2.2')
            elif '2.2' in ielts:
                ielts.remove('2.2')
        except:
            ielts = None
        if len(ielts) ==1:
            a = ielts[0]
            ielts = a
            ielts_r = float(a)- 0.5
            ielts_w = float(a)- 0.5
            ielts_s = float(a)- 0.5
            ielts_l = float(a)- 0.5
        elif len(ielts) ==2:
            a = ielts[0]
            b = ielts[1]
            ielts = a
            ielts_r = b
            ielts_w = b
            ielts_s = b
            ielts_l = b
        else:
            ielts = 6.0
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
        # print(ielts,ielts_r,ielts_w,ielts_s,ielts_l)

        #23.require_chinese_en
        require_chinese_en = '<p>You will usually need a four year undergraduate degree from a recognised institution</p>'

        #24.apply_pre
        apply_pre = '£'

        #25.modules_en
        num = response.xpath('//body//@id').extract()[0]
        num = re.findall('\d+', num)[0]
        xpaths = '//*[@id="section-id-' + str(num) + '"]/main/div[1]/section'
        modules_en = response.xpath(xpaths).extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        item['modules_en'] = modules_en
        item['require_chinese_en'] = require_chinese_en
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['career_en'] = career_en
        item['assessment_en'] = assessment_en
        item['teach_time'] = teach_time
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['location'] = location
        item['start_date'] = start_date
        item['apply_proces_en'] = apply_proces_en
        item['rntry_requirements'] = rntry_requirements
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        yield  item
