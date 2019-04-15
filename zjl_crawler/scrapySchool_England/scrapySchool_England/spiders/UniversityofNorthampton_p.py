# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/11 14:15'
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
class UniversityofNorthamptonSpider(scrapy.Spider):
    name = 'UniversityofNorthampton_p'
    allowed_domains = ['northampton.ac.uk/']
    start_urls = []
    C= [
        'https://www.northampton.ac.uk/study/courses/accounting-and-finance-msc/',
        'https://www.northampton.ac.uk/study/courses/accounting-and-finance-top-up-msc/',
        'https://www.northampton.ac.uk/study/courses/advanced-occupational-therapy-postgraduate-certificate/',
        'https://www.northampton.ac.uk/study/courses/advanced-professional-practice-occupational-therapy/',
        'https://www.northampton.ac.uk/study/courses/animal-welfare-msc/',
        'https://www.northampton.ac.uk/study/courses/business-analytics-msc/',
        'https://www.northampton.ac.uk/study/courses/child-and-adolescent-mental-health-msc/',
        'https://www.northampton.ac.uk/study/courses/computing-msc/',
        'https://www.northampton.ac.uk/study/courses/computing-computer-networks-engineering-msc/',
        'https://www.northampton.ac.uk/study/courses/computing-internet-technology-and-security-msc/',
        'https://www.northampton.ac.uk/study/courses/computing-serious-games-msc/',
        'https://www.northampton.ac.uk/study/courses/computing-software-engineering-msc/',
        'https://www.northampton.ac.uk/study/courses/corporate-governance-and-leadership-msc/',
        'https://www.northampton.ac.uk/study/courses/corporate-governance-and-leadership-topup-msc/',
        'https://www.northampton.ac.uk/study/courses/counselling/',
        'https://www.northampton.ac.uk/study/courses/counselling-children-and-young-people-msc/',
        'https://www.northampton.ac.uk/study/courses/dba/',
        'https://www.northampton.ac.uk/study/courses/doctorate-of-professional-practice/',
        'https://www.northampton.ac.uk/study/courses/early-years-teacher-status-0-5/',
        'https://www.northampton.ac.uk/study/courses/economics-msc/',
        'https://www.northampton.ac.uk/study/courses/education-ma/',
        'https://www.northampton.ac.uk/study/courses/education-early-years-pathway-ma/',
        'https://www.northampton.ac.uk/study/courses/ma-education-english-language-teaching/',
        'https://www.northampton.ac.uk/study/courses/education-mathematics-pathway-ma/',
        'https://www.northampton.ac.uk/study/courses/education-management-and-leadership-ma/',
        'https://www.northampton.ac.uk/study/courses/msc-engineering/',
        'https://www.northampton.ac.uk/study/courses/english-contemporary-literature-ma/',
        'https://www.northampton.ac.uk/study/courses/equine-behaviour-and-welfare-msc/',
        'https://www.northampton.ac.uk/study/courses/fine-art-ma/',
        'https://www.northampton.ac.uk/study/courses/history-ma/',
        'https://www.northampton.ac.uk/study/courses/human-resource-management-ma/',
        'https://www.northampton.ac.uk/study/courses/human-resource-management-pgdip/',
        'https://www.northampton.ac.uk/study/courses/human-resource-management-topup-ma/',
        'https://www.northampton.ac.uk/study/courses/international-banking-and-finance-msc/',
        'https://www.northampton.ac.uk/study/courses/international-commercial-law-llm/',
        'https://www.northampton.ac.uk/study/courses/international-commercial-law-distance-learning-llm/',
        'https://www.northampton.ac.uk/study/courses/international-criminal-law-and-security-llm/',
        'https://www.northampton.ac.uk/study/courses/international-hotel-management/',
        'https://www.northampton.ac.uk/study/courses/international-logistics-msc/',
        'https://www.northampton.ac.uk/study/courses/international-marketing-strategy-msc/',
        'https://www.northampton.ac.uk/study/courses/international-relations-ma/',
        'https://www.northampton.ac.uk/study/courses/international-special-events-management/',
        'https://www.northampton.ac.uk/study/courses/international-tourism-development-ma/',
        'https://www.northampton.ac.uk/study/courses/leadership-for-health-social-care/',
        'https://www.northampton.ac.uk/study/courses/leather-technology-phd/',
        'https://www.northampton.ac.uk/study/courses/leather-technology-professional/',
        'https://www.northampton.ac.uk/study/courses/llm-in-legal-practice/',
        'https://www.northampton.ac.uk/study/courses/lift-engineering-msc/',
        'https://www.northampton.ac.uk/study/courses/management-msc/',
        'https://www.northampton.ac.uk/study/courses/msc-managing-waste-and-environmental-resources/',
        'https://www.northampton.ac.uk/study/courses/mba-full-time-and-distance-learning/',
        'https://www.northampton.ac.uk/study/courses/master-of-business-administration-distance-learning/',
        'https://www.northampton.ac.uk/study/courses/master-of-business-administration-top-up-mba-2/',
        'https://www.northampton.ac.uk/study/courses/master-of-business-administration-executive-distance-learning/',
        'https://www.northampton.ac.uk/study/courses/master-of-business-administration-top-up-distance-learning/',
        'https://www.northampton.ac.uk/study/courses/nonmedical-prescribing-programmes/',
        'https://www.northampton.ac.uk/study/courses/pgce-qts-primary-secondary-school-direct-route/',
        'https://www.northampton.ac.uk/study/courses/pgce-topup/',
        'https://www.northampton.ac.uk/study/courses/postgraduate-certificate-practice-education/',
        'https://www.northampton.ac.uk/study/courses/postgraduate-certificate-in-primary-english-pgce/',
        'https://www.northampton.ac.uk/study/courses/postgraduate-certificate-primary-computing-pgce/',
        'https://www.northampton.ac.uk/study/courses/postgraduate-certificate-primary-maths-pgce/',
        'https://www.northampton.ac.uk/study/courses/postgraduate-certificate-primary-education-3-7/',
        'https://www.northampton.ac.uk/study/courses/postgraduate-certificate-primary-education-5-11/',
        'https://www.northampton.ac.uk/study/courses/project-management/',
        'https://www.northampton.ac.uk/study/courses/public-health-msc/',
        'https://www.northampton.ac.uk/study/courses/social-innovation-ma/',
        'https://www.northampton.ac.uk/study/courses/social-work-ma/',
        'https://www.northampton.ac.uk/study/courses/special-educational-needs-inclusion-ma/',
        'https://www.northampton.ac.uk/study/courses/special-educational-needs-and-inclusion-autism-pathway/',
        'https://www.northampton.ac.uk/study/courses/specialist-community-public-health-nursing-pgdip/',
        'https://www.northampton.ac.uk/study/courses/strategic-technology-management-msc/',
        'https://www.northampton.ac.uk/study/courses/msc-strength-and-conditioning/',
        'https://www.northampton.ac.uk/study/courses/the-national-award-for-sen-co-ordination/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Northampton'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="site-content"]/article/header/div[2]/h1/text()').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_name
        degree_name = response.xpath('//*[@id="site-content"]/article/header/div[2]/h1/small').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #5.degree_type
        degree_type = 2

        #6.duration #7.duration_per #8.teach_time #9.start_date
        duration_list = response.xpath('//*[@id="overview"]/div[1]/p/span[2]').extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        if len(duration_list) ==0:
            teach_time = 'Full-time'
        elif 'Full Time' in duration_list:
            teach_time = 'Full-time'
        else:
            teach_time = 'Part-time'
        try:
            duration = re.findall('\d+',duration_list)[0]
        except:
            duration = 1
        if int(duration)>5:
            duration_per = 3
        else:
            duration_per = 1
        if 'February and September' in duration_list:
            start_date = '2018-9,2019-2'
        elif 'January and September' in duration_list:
            start_date = '2018-9,2019-1'
        elif 'January, April and September'in duration_list:
            start_date = '2018-9,2019-1,2019-4'
        elif 'February, May and September'in duration_list:
            start_date = '2018-9,2019-2,2019-5'
        elif 'January, May and September' in duration_list:
            start_date = '2018-9,2019-1,2019-5'
        elif 'May and September' in duration_list:
            start_date = '2018-9,2019-5'
        elif 'January'  in duration_list:
            start_date = '2019-1'
        elif 'November' in duration_list:
            start_date = '2018-11'
        else:
            start_date = '2018-9'
        # print(duration,duration_per,start_date,teach_time)

        #10.overview_en
        overview_en = response.xpath('//*[@id="overview"]/div[2]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #11.modules_en
        modules_en = response.xpath('//*[@id="course-content"]/div[2]/div/ul/li/h4').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        modules_en = modules_en.replace('credits)','credits)\n')
        # print(modules_en)

        #12.career_en
        career_en = response.xpath('//*[@id="careers"]/div[1]/p').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #13.apply_proces_en
        apply_proces_en = 'http://www.northampton.ac.uk/study/how-to-apply/'

        #14.rntry_requirements
        rntry_requirements = response.xpath('//*[@id="entry-requirements"]/div[1]/p').extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #15.ielts 16171819
        ielts = re.findall('\d\.\d',rntry_requirements)
        ielts = ''.join(ielts)
        if '7.0' in ielts:
            ielts = 7.0
            ielts_r = 6.5
            ielts_s = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
        else :
            ielts = 6.5
            ielts_r = 6.0
            ielts_s = 6.0
            ielts_w = 6.0
            ielts_l = 6.0
        # print(ielts,ielts_r,ielts_s,ielts_w,ielts_l)

        #20.tuition_fee
        tuition_fee = response.xpath('//*[@id="fees-and-funding"]').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #21.tuition_fee_pre
        tuition_fee_pre = "£"

        #22.apply_pre
        apply_pre = '£'

        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_name'] = degree_name
        item['degree_type'] = degree_type
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['teach_time'] = teach_time
        item['start_date'] = start_date
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['apply_proces_en'] = apply_proces_en
        item['rntry_requirements'] = rntry_requirements
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['tuition_fee_pre'] = tuition_fee_pre
        item['tuition_fee'] = tuition_fee
        yield  item