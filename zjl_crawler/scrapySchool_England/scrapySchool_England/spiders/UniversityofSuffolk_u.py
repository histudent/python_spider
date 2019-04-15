# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/9 16:22'
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
class UniversityofSuffolkSpider(scrapy.Spider):
    name = 'UniversityofSuffolk_u'
    allowed_domains = ['uos.ac.uk/']
    start_urls = []
    C = [
        'https://www.uos.ac.uk/courses/ug/ba-hons-applied-psychology-and-sociology',
        'https://www.uos.ac.uk/courses/ug/ba-hons-fine-art',
        'https://www.uos.ac.uk/courses/ug/ba-hons-interior-architecture-and-design',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-nutrition-and-human-health-foundation-year',
        'https://www.uos.ac.uk/courses/ug/ba-hons-social-science',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-bioscience-foundation-year',
        'https://www.uos.ac.uk/courses/ug/ba-hons-early-childhood-studies-0',
        'https://www.uos.ac.uk/courses/ug/bsc-operating-department-practice',
        'https://www.uos.ac.uk/courses/ug/ba-hons-computer-games-design',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-radiotherapy-and-oncology',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-mental-health-nursing',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-computer-games-programming',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-computer-games-technology',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-applied-psychology',
        'https://www.uos.ac.uk/courses/ug/ba-hons-sociology-and-law',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-software-development',
        'https://www.uos.ac.uk/courses/ug/ba-hons-early-and-primary-education-studies',
        'https://www.uos.ac.uk/courses/ug/ba-hons-social-work',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-public-health',
        'https://www.uos.ac.uk/courses/ug/ba-hons-english-and-applied-psychology',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-psychology',
        'https://www.uos.ac.uk/courses/ug/ba-hons-graphic-and-communication-design',
        'https://www.uos.ac.uk/courses/ug/ba-hons-history-and-applied-sociology',
        'https://www.uos.ac.uk/courses/ug/ba-hons-integrative-counselling',
        'https://www.uos.ac.uk/courses/ug/ba-hons-business-and-management',
        'https://www.uos.ac.uk/courses/ug/ba-hons-business-and-management-events',
        'https://www.uos.ac.uk/courses/ug/ba-hons-business-and-management-law',
        'https://www.uos.ac.uk/courses/ug/ba-hons-business-and-management-marketing',
        'https://www.uos.ac.uk/courses/ug/ba-hons-art-practice',
        'https://www.uos.ac.uk/courses/ug/ba-hons-creative-and-commercial-music-production',
        'https://www.uos.ac.uk/courses/ug/ba-hons-economics',
        'https://www.uos.ac.uk/courses/ug/ba-hons-economics-banking-and-finance',
        'https://www.uos.ac.uk/courses/ug/ba-hons-family-studies',
        'https://www.uos.ac.uk/courses/ug/ba-hons-film-studies',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-cyber-security',
        'https://www.uos.ac.uk/courses/ug/ba-hons-architecture',
        'https://www.uos.ac.uk/courses/ug/ba-hons-marketing',
        'https://www.uos.ac.uk/courses/ug/ba-hons-marketing-and-public-relations',
        'https://www.uos.ac.uk/courses/ug/ba-project-management-professional-placement-and-study-abroad',
        'https://www.uos.ac.uk/courses/ug/ba-project-management-study-abroad',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-psychology-business-management',
        'https://www.uos.ac.uk/courses/ug/ba-hons-politics',
        'https://www.uos.ac.uk/courses/ug/ba-hons-politics-and-economics',
        'https://www.uos.ac.uk/courses/ug/ba-hons-politics-and-history',
        'https://www.uos.ac.uk/courses/ug/ba-hons-politics-and-sociology',
        'https://www.uos.ac.uk/courses/ug/ba-hons-project-management',
        'https://www.uos.ac.uk/courses/ug/ba-project-management-professional-placement',
        'https://www.uos.ac.uk/courses/ug/ba-hons-childhood-studies',
        'https://www.uos.ac.uk/courses/ug/ba-hons-childhood-and-family-studies',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-wildlife-ecology-and-conservation-science',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-software-engineering',
        'https://www.uos.ac.uk/courses/ug/llb-law',
        'https://www.uos.ac.uk/courses/ug/llb-law-business-management',
        'https://www.uos.ac.uk/courses/ug/llb-hons-law-professional-placement',
        'https://www.uos.ac.uk/courses/ug/ba-hons-human-geography-and-sociology',
        'https://www.uos.ac.uk/courses/ug/llb-law-politics',
        'https://www.uos.ac.uk/courses/ug/llb-hons-law-business-management-professional-placement',
        'https://www.uos.ac.uk/courses/ug/llb-hons-law-politics-professional-placement',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-network-engineering',
        'https://www.uos.ac.uk/courses/ug/ba-hons-human-geography',
        'https://www.uos.ac.uk/courses/ug/ba-hons-english',
        'https://www.uos.ac.uk/courses/ug/ba-hons-english-literature-creative-writing-0',
        'https://www.uos.ac.uk/courses/ug/ba-hons-english-literature-language',
        'https://www.uos.ac.uk/courses/ug/ba-hons-event-and-tourism-management',
        'https://www.uos.ac.uk/courses/ug/ba-hons-photography',
        'https://www.uos.ac.uk/courses/ug/ba-hons-digital-film-production',
        'https://www.uos.ac.uk/courses/ug/ba-hons-person-centred-counselling',
        'https://www.uos.ac.uk/courses/ug/ba-hons-screenwriting',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-diagnostic-radiography',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-mobile-and-web-engineering',
        'https://www.uos.ac.uk/courses/ug/ba-hons-graphic-design',
        'https://www.uos.ac.uk/courses/ug/ba-hons-graphic-design-graphic-illustration',
        'https://www.uos.ac.uk/courses/ug/ba-hons-history',
        'https://www.uos.ac.uk/courses/ug/ba-hons-business-management',
        'https://www.uos.ac.uk/courses/ug/ba-hons-design',
        'https://www.uos.ac.uk/courses/ug/ba-hons-applied-care-practice-early-years-progression-route',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-midwifery',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-bioscience',
        'https://www.uos.ac.uk/courses/ug/ba-hons-event-management',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-sport-and-exercise-science',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-information-technology-service-management',
        'https://www.uos.ac.uk/courses/ug/ba-hons-tourism-management',
        'https://www.uos.ac.uk/courses/ug/ba-hons-applied-interior-design',
        'https://www.uos.ac.uk/courses/ug/ba-hons-accounting-and-financial-management',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-adult-nursing-0',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-nutrition-and-human-health',
        'https://www.uos.ac.uk/courses/ug/ba-hons-early-childhood-studies',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-child-development-and-developmental-therapies',
        'https://www.uos.ac.uk/courses/ug/ba-hons-counselling',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-business-management-and-information-technology',
        'https://www.uos.ac.uk/courses/ug/ba-hons-english-and-history',
        'https://www.uos.ac.uk/courses/ug/ba-hons-dance',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-criminology-and-law',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-criminology-and-sociology',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-criminology',
        'https://www.uos.ac.uk/courses/ug/llb-hons-law-criminology',
        'https://www.uos.ac.uk/courses/ug/llb-hons-law-sociology',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-psychology-and-criminology',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-psychology-and-early-childhood-studies',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-psychology-and-sociology',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-sociology',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-paramedic-science',
        'https://www.uos.ac.uk/courses/ug/ba-hons-special-educational-needs-and-disability-studies',
        'https://www.uos.ac.uk/courses/ug/ba-hons-business-management-0',
        'https://www.uos.ac.uk/courses/ug/msci-sports-psychology-football',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-child-health-nursing',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-sport-psychology',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-strength-and-conditioning',
        'https://www.uos.ac.uk/courses/ug/bsc-hons-sport-performance-analysis'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Suffolk'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('/html/body/div/div[2]/div/div[1]/div[1]/div[2]/header/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 1

        #5.degree_name
        if 'BSc (Hons)' in programme_en:
            degree_name = 'BSc (Hons)'
        elif 'MSci' in programme_en:
            degree_name = 'MSci'
        elif 'BA (Hons)' in programme_en:
            degree_name = 'BA (Hons)'
        elif 'FdSc' in programme_en:
            degree_name = 'FdSc'
        elif 'BA' in programme_en:
            degree_name = 'BA'
        elif 'FdA' in programme_en:
            degree_name = 'FdA'
        elif 'Dip/HE' in programme_en:
            degree_name = 'Dip/HE'
        elif 'LLB (Hons)' in programme_en:
            degree_name = 'LLB (Hons)'
        elif 'HNC' in programme_en:
            degree_name = 'HNC'
        elif 'HND' in programme_en:
            degree_name = 'HND'
        elif 'BEng (Hons)' in programme_en:
            degree_name = 'BEng (Hons)'
        else:
            degree_name = ''
        programme_en = programme_en.replace(degree_name,'').strip()
        # print(degree_name)
        # print(programme_en)

        #6.location
        location = response.xpath("//*[contains(text(),'Location:')]//following-sibling::*").extract()
        location = ','.join(location)
        location = remove_tags(location).strip()
        # print(location)

        #7.duration
        duration = response.xpath("//*[contains(text(),'Duration:')]//following-sibling::*//p[1]").extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        if 'Also available as online' in duration:
            duration = 1
        try:
            duration = re.findall(r'(.*)full-time',duration)[0].strip()
        except:
            duration = 1
        duration = 3
        # print(duration)
        #
        #8.duration_per
        duration_per =1

        #9.ucascode
        ucascode = response.xpath("//*[contains(text(),'UCAS code:')]//following-sibling::*").extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode).strip()
        ucascode = ucascode[:4]
        # print(ucascode)

        #10.overview_en
        overview_en = response.xpath('//*[@id="group-description"]/div[1]//p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #11.modules_en
        modules_en = response.xpath('//*[@id="group-duration-modules"]/*').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # if len(modules_en)==0:
        #     print(response.url)
        # print(modules_en)

        #12.tuition_fee
        tuition_fee = response.xpath('//*[@id="group-fees"]').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee =getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #13.tuition_fee_pre
        tuition_fee_pre = '£'

        #14.apply_desc_en
        apply_desc_en = response.xpath("//*[contains(text(),'Academic Requirements')]/../../following-sibling::*[1]").extract()
        if len(apply_desc_en)==0:
            apply_desc_en = response.xpath('//*[@id="group-entry-requirements"]').extract()
        apply_desc_en = ''.join(apply_desc_en)
        apply_desc_en = remove_class(apply_desc_en)
        # print(apply_desc_en)

        #15.ielts 16171819
        ielts_list = response.xpath("//*[contains(text(),'International Requirements')]/../../following-sibling::*[1]").extract()
        ielts_list = ''.join(ielts_list)
        ielts_list = remove_tags(ielts_list)
        # print(ielts_list)
        try:
            ielts = re.findall('\d\.\d',ielts_list)[0]
        except:
            ielts = 6.5
        # print(ielts,url)
        ielts_r = 5.5
        ielts_l = 5.5
        ielts_w = 5.5
        ielts_s = 5.5

        #20.apply_proces_en
        apply_proces_en = 'https://www.uos.ac.uk/content/how-apply-0'

        #21.apply_pre
        apply_pre = '£'

        #22.alevel
        try:
            alevel = response.xpath("//*[contains(text(),'A-Level')]/.").extract()[-1]
            alevel = remove_tags(alevel).strip()
        except:
            alevel = 'N/A'
        # print(alevel)

        #23.career_en
        career_en = response.xpath('//*[@id="group-career"]').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        item['career_en'] = career_en
        item['alevel'] = alevel
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['location'] = location
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_desc_en'] = apply_desc_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['apply_proces_en'] = apply_proces_en
        item['ucascode'] = ucascode
        yield  item