# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/9 13:55'
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
class EdgeHillUniversitySpider(scrapy.Spider):
    name = 'EdgeHillUniversity_p'
    allowed_domains = ['edgehill.ac.uk/']
    start_urls = []
    C= [
        'https://www.edgehill.ac.uk/courses/child-and-adolescent-mental-health-and-wellbeing-msc/',
        'https://www.edgehill.ac.uk/courses/education-dyscalculia/',
        'https://www.edgehill.ac.uk/courses/education-inclusion-sen/',
        'https://www.edgehill.ac.uk/courses/educational-enquiry-and-professional-learning/',
        'https://www.edgehill.ac.uk/courses/special-educational-needs-coordination',
        'https://www.edgehill.ac.uk/courses/specialist-primary-mathematics-practice',
        'https://www.edgehill.ac.uk/courses/spld-dyslexia',
        'https://www.edgehill.ac.uk/courses/tesol',
        'https://www.edgehill.ac.uk/courses/advanced-computer-networking/',
        'https://www.edgehill.ac.uk/courses/big-data-analytics',
        'https://www.edgehill.ac.uk/courses/big-data-analytics-pgcert/',
        'https://www.edgehill.ac.uk/courses/computing-msc',
        'https://www.edgehill.ac.uk/courses/cyber-security',
        'https://www.edgehill.ac.uk/courses/games-programming-and-visual-computing/',
        'https://www.edgehill.ac.uk/courses/information-security-and-it-management',
        'https://www.edgehill.ac.uk/study/courses/master-of-business-administration-information-technology',
        'https://www.edgehill.ac.uk/courses/mres/',
        'https://www.edgehill.ac.uk/courses/employment-enterprise-and-entrepreneurship-development/',
        'https://www.edgehill.ac.uk/courses/leadership-and-management-development',
        'https://www.edgehill.ac.uk/courses/master-of-business-administration',
        'https://www.edgehill.ac.uk/courses/master-of-business-administration-finance',
        'https://www.edgehill.ac.uk/courses/master-of-business-administration-hrm',
        'https://www.edgehill.ac.uk/courses/master-of-business-administration-information-technology',
        'https://www.edgehill.ac.uk/courses/master-of-business-administration-marketing',
        'https://www.edgehill.ac.uk/courses/mres/',
        'https://www.edgehill.ac.uk/courses/marketing-communications-and-branding',
        'https://www.edgehill.ac.uk/courses/master-of-business-administration-marketing',
        'https://www.edgehill.ac.uk/courses/mres/',
        'https://www.edgehill.ac.uk/courses/conservation-management',
        'https://www.edgehill.ac.uk/courses/mres/',
        'https://www.edgehill.ac.uk/courses/creative-writing-ma',
        'https://www.edgehill.ac.uk/courses/mres/',
        'https://www.edgehill.ac.uk/courses/english-ma',
        'https://www.edgehill.ac.uk/courses/popular-culture',
        'https://www.edgehill.ac.uk/courses/mres/',
        'https://www.edgehill.ac.uk/courses/child-and-adolescent-mental-health-and-wellbeing-msc/',
        'https://www.edgehill.ac.uk/courses/applied-clinical-nutrition',
        'https://www.edgehill.ac.uk/courses/public-health-nutrition',
        'https://www.edgehill.ac.uk/courses/advanced-critical-care/',
        'https://www.edgehill.ac.uk/courses/advanced-fertility-practice',
        'https://www.edgehill.ac.uk/courses/advanced-practice',
        'https://www.edgehill.ac.uk/courses/clinical-education/',
        'https://www.edgehill.ac.uk/courses/clinical-research/',
        'https://www.edgehill.ac.uk/courses/health-research/',
        'https://www.edgehill.ac.uk/courses/integrated-palliative-and-end-of-life-care/',
        'https://www.edgehill.ac.uk/courses/leadership-development',
        'https://www.edgehill.ac.uk/courses/medical-leadership',
        'https://www.edgehill.ac.uk/courses/master-of-medicine',
        'https://www.edgehill.ac.uk/courses/mental-health-law-and-ethics',
        'https://www.edgehill.ac.uk/courses/professional-clinical-practice',
        'https://www.edgehill.ac.uk/courses/simulation-and-clinical-learning/',
        'https://www.edgehill.ac.uk/courses/master-of-surgery',
        'https://www.edgehill.ac.uk/courses/surgical-care-practice',
        'https://www.edgehill.ac.uk/courses/teaching-and-learning-in-clinical-practice/',
        'https://www.edgehill.ac.uk/courses/workplace-based-postgraduate-medical-education/',
        'https://www.edgehill.ac.uk/courses/critical-screen-practice',
        'https://www.edgehill.ac.uk/courses/film-and-media',
        'https://www.edgehill.ac.uk/courses/popular-culture',
        'https://www.edgehill.ac.uk/courses/mres/',
        'https://www.edgehill.ac.uk/courses/pre-masters-programme/',
        'https://www.edgehill.ac.uk/courses/film-and-media',
        'https://www.edgehill.ac.uk/courses/media-management',
        'https://www.edgehill.ac.uk/courses/mres/',
        'https://www.edgehill.ac.uk/courses/midwifery-msc/',
        'https://www.edgehill.ac.uk/courses/nursing-adult-msc/',
        'https://www.edgehill.ac.uk/courses/nursing-child-msc/',
        'https://www.edgehill.ac.uk/courses/nursing-learning-disabilities-msc/',
        'https://www.edgehill.ac.uk/courses/nursing-mental-health-msc/',
        'https://www.edgehill.ac.uk/courses/applied-clinical-nutrition',
        'https://www.edgehill.ac.uk/courses/public-health-nutrition',
        'https://www.edgehill.ac.uk/courses/history-and-culture',
        'https://www.edgehill.ac.uk/courses/popular-culture',
        'https://www.edgehill.ac.uk/courses/mres/',
        'https://www.edgehill.ac.uk/study/courses/creative-and-cultural-education',
        'https://www.edgehill.ac.uk/study/courses/making-performance',
        'https://www.edgehill.ac.uk/courses/mres/',
        'https://www.edgehill.ac.uk/study/courses/psychology-msc',
        'https://www.edgehill.ac.uk/courses/mres/',
        'https://www.edgehill.ac.uk/courses/mres/',
        'https://www.edgehill.ac.uk/courses/phd/',
        'https://www.edgehill.ac.uk/courses/emergency-services-management',
        'https://www.edgehill.ac.uk/courses/clinical-research/',
        'https://www.edgehill.ac.uk/courses/health-research/',
        'https://www.edgehill.ac.uk/courses/social-work-ma',
        'https://www.edgehill.ac.uk/courses/sport-physical-activity-and-mental-health/',
        'https://www.edgehill.ac.uk/courses/mres/',
        'https://www.edgehill.ac.uk/courses/pgce-early-years',
        'https://www.edgehill.ac.uk/courses/pgce-primary',
        'https://www.edgehill.ac.uk/courses/pgce-primary-mathematics-specialist',
        'https://www.edgehill.ac.uk/courses/pgce-primary-physical-education-specialist',
        'https://www.edgehill.ac.uk/courses/pgce-secondary-computer-science-and-information-technology',
        'https://www.edgehill.ac.uk/courses/pgce-secondary-english',
        'https://www.edgehill.ac.uk/courses/pgce-secondary-geography',
        'https://www.edgehill.ac.uk/courses/pgce-secondary-history',
        'https://www.edgehill.ac.uk/courses/pgce-secondary-mathematics',
        'https://www.edgehill.ac.uk/courses/pgce-secondary-physical-education',
        'https://www.edgehill.ac.uk/courses/pgce-secondary-religious-education',
        'https://www.edgehill.ac.uk/courses/pgce-secondary-science-biology',
        'https://www.edgehill.ac.uk/courses/further-education-and-training-pgce',
        'https://www.edgehill.ac.uk/courses/biology-ske',
        'https://www.edgehill.ac.uk/courses/computer-science',
        'https://www.edgehill.ac.uk/courses/english-ske/',
        'https://www.edgehill.ac.uk/courses/geography-ske',
        'https://www.edgehill.ac.uk/courses/mathematics'
    ]
    C = set(C)
    # print(len(C))
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Edge Hill University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="primary"]/header/h1/a').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        degree_name = programme_en.split()[0]
        programme_en = programme_en.replace(degree_name,'').strip()
        # print(degree_name)
        # print(programme_en)

        #6.teach_time #7.duration #8.duration_per
        teach_time_list = response.xpath("//*[contains(text(),'Length:')]//following-sibling::*").extract()
        teach_time_list= ''.join(teach_time_list)
        teach_time_list = remove_tags(teach_time_list)
        # print(teach_time_list)
        duration = re.findall('\d+',teach_time_list)[0]
        if 'Months' in teach_time_list:
            duration_per = 3
        elif 'Weeks' in teach_time_list:
            duration_per = 4
        else:
            duration_per = 1
        if 'Full-Time' in teach_time_list:
            teach_time = 'Full-Time'
        else:
            teach_time = 'Part-Time'
        # print(duration,'***********',duration_per)
        # print(teach_time)

        #9.start_date
        start_date = response.xpath("//*[contains(text(),'Dates:')]//following-sibling::*").extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        start_date = tracslateDate(start_date)
        start_date = ','.join(start_date)
        # print(start_date)

        #10.department
        department = response.xpath("//*[contains(text(),'Department:')]//following-sibling::*").extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #11.location
        location = response.xpath("//*[contains(text(),'Location:')]//following-sibling::*").extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #12.overview_en
        overview_en = response.xpath('//*[@id="overview"]/div[1]/div/ul/li/text()').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = '<p>' + overview_en +'</p>'
        # print(overview_en)

        #13.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'How will I be assessed?')]//following-sibling::*[1]").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #14.modules_en
        modules_en = response.xpath('//*[@id="modules"]/h4/strong').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #15.rntry_requirements
        rntry_requirements = response.xpath("//*[contains(text(),'Entry Requirements')]//following-sibling::*").extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #16.ielts 17.18.19.20
        ielts_list = response.xpath("//*[contains(text(),'English Language Requirements')]//following-sibling::*[1]").extract()
        ielts_list = ''.join(ielts_list)
        ielts_list = remove_tags(ielts_list)
        # print(ielts_list)
        try:
            ielts = re.findall('\d\.\d',ielts_list)
        except:
            ielts = None
        if len(ielts) ==1:
            a = ielts[0]
            ielts = a
            ielts_r = a
            ielts_w = a
            ielts_s = a
            ielts_l = a
        elif len(ielts) ==2:
            a= ielts[0]
            b= ielts[1]
            ielts = a
            ielts_r = b
            ielts_w = b
            ielts_s = b
            ielts_l = b
        else:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
        # print(ielts,ielts_r,ielts_w,ielts_l,ielts_s)

        #21.career_en
        career_en = response.xpath("//*[contains(text(),'What are my career prospects?')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #22.tuition_fee
        tuition_fee= response.xpath("//*[contains(text(),'Tuition Fees')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #23.tuition_fee_pre
        tuition_fee_pre= '£'

        #24.apply_proces_en
        apply_proces_en = response.xpath("//h4[contains(text(),'How to Apply')]//following-sibling::*").extract()
        apply_proces_en = ''.join(apply_proces_en)
        apply_proces_en = remove_class(apply_proces_en)
        # print(apply_proces_en)

        #25.apply_pre
        apply_pre = '£'

        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['teach_time'] = teach_time
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['start_date'] = start_date
        item['department'] = department
        item['location'] = location
        item['overview_en'] = overview_en
        item['assessment_en'] = assessment_en
        item['modules_en'] = modules_en
        item['rntry_requirements'] = rntry_requirements
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_proces_en'] = apply_proces_en
        yield  item