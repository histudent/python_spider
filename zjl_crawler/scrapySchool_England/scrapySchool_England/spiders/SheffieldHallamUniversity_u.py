# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/2 9:55'
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
class SheffieldHallamUniversitySpider(scrapy.Spider):
    name = 'SheffieldHallamUniversity_u'
    allowed_domains = ['shu.ac.uk/']
    start_urls = []
    C = [
        'https://www.shu.ac.uk/courses/computing/bsc-honours-information-technology-with-business-studies-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/physics/bsc-honours-physics-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/sociology-and-politics/ba-honours-politics/full-time/2019',
        'https://www.shu.ac.uk/courses/media-pr-and-journalism/ba-honours-photography-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/bsc-honours-business-and-information-and-communications-technology-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/meng-electrical-and-electronic-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/geography-and-environment/bsc-honours-geography/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/beng-honours-software-engineering-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/sport-and-physical-activity/ba-honours-sport-studies/full-time/2018',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-electronic-engineering-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/tourism-and-hospitality/bsc-honours-international-tourism-management/full-time/2019',
        'https://www.shu.ac.uk/courses/media-pr-and-journalism/ba-honours-sports-journalism/full-time/2019',
        'https://www.shu.ac.uk/courses/languages/ba-honours-languages-with-tourism-french/full-time/2019',
        'https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-nursing-mental-health/full-time/2019',
        'https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-nursing-adult/full-time/2019',
        'https://www.shu.ac.uk/courses/marketing/ba-honours-marketing-communications-and-advertising/full-time/2019',
        'https://www.shu.ac.uk/courses/media-pr-and-journalism/ba-honours-journalism/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-electrical-and-electronic-engineering-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/mathematics/bsc-honours-mathematics/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-computer-systems-engineering-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-sport-and-exercise-science/full-time/2019',
        'https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-biology/full-time/2019',
        'https://www.shu.ac.uk/courses/digital-media/ba-honours-film-and-media-production/full-time/2019',
        'https://www.shu.ac.uk/courses/accounting-banking-and-finance/ba-honours-finance-and-investment/full-time/2019',
        'https://www.shu.ac.uk/courses/physiotherapy/bsc-honours-physiotherapy/full-time/2019',
        'https://www.shu.ac.uk/courses/teaching-and-education/ba-honours-education-studies/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/bsc-honours-computing/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/bsc-honours-computer-science-for-games/full-time/2019',
        'https://www.shu.ac.uk/courses/digital-media/ba-honours-digital-media-production/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/mcomp-computer-science-for-games/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-materials-engineering-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/food-and-nutrition/bsc-honours-nutrition-diet-and-lifestyle/full-time/2019',
        'https://www.shu.ac.uk/courses/food-and-nutrition/bsc-honours-food-marketing-management/full-time/2019',
        'https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-biomedical-science/full-time/2019',
        'https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-physical-education-and-school-sport/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-aerospace-engineering-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-product-design-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/teaching-and-education/ba-honours-primary-education-511-with-qualified-teacher-status/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-fashion-management-and-communication/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/meng-materials-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-electronic-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/construction-real-estate-and-surveying/bsc-honours-real-estate/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-aerospace-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/bsc-honours-computer-science/full-time/2019',
        'https://www.shu.ac.uk/courses/teaching-and-education/bsc-honours-science-with-education-and-qualified-teacher-status/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-jewellery-and-metalwork-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-illustration-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-physical-activity-sport-and-health/full-time/2019',
        'https://www.shu.ac.uk/courses/childhood-studies/ba-honours-early-childhood-studies/full-time/2019',
        'https://www.shu.ac.uk/courses/english/ba-honours-creative-writing/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-automotive-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/tourism-and-hospitality/bsc-honours-airline-and-airport-management/full-time/2019',
        'https://www.shu.ac.uk/courses/tourism-and-hospitality/ba-honours-international-tourism-management-with-german/full-time/2019',
        'https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-analytics/full-time/2019',
        'https://www.shu.ac.uk/courses/tourism-and-hospitality/bsc-honours-international-hotel-management/full-time/2019',
        'https://www.shu.ac.uk/courses/business-and-management/ba-honours-international-business-with-spanish/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-product-design/full-time/2019',
        'https://www.shu.ac.uk/courses/architecture/bsc-honours-architectural-technology/full-time/2019',
        'https://www.shu.ac.uk/courses/languages/ba-honours-languages-with-tourism-spanish/full-time/2019',
        'https://www.shu.ac.uk/courses/media-pr-and-journalism/ba-honours-sports-journalism-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/media-pr-and-journalism/ba-honours-public-relations-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-product-design-furniture-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/meng-chemical-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/criminology/ba-honours-criminology-and-sociology/full-time/2019',
        'https://www.shu.ac.uk/courses/media-pr-and-journalism/ba-honours-media-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/media-pr-and-journalism/ba-honours-public-relations-and-media-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/film-and-performance/ba-honours-performance-for-stage-and-screen/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/bsc-honours-computer-science-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-fine-art-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/accounting-banking-and-finance/ba-honours-accounting-and-economics/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/bsc-honours-computer-science-for-games-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-mechanical-engineering-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/meng-automotive-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/bsc-honours-business-and-information-and-communications-technology/full-time/2019',
        'https://www.shu.ac.uk/courses/tourism-and-hospitality/ba-honours-international-tourism-management-with-french/full-time/2019',
        'https://www.shu.ac.uk/courses/english/ba-honours-english-and-history/full-time/2019',
        'https://www.shu.ac.uk/courses/marketing/ba-honours-marketing/full-time/2019',
        'https://www.shu.ac.uk/courses/teaching-and-education/bsc-honours-mathematics-with-education-and-qualified-teacher-status/full-time/2019',
        'https://www.shu.ac.uk/courses/english/ba-honours-english-literature/full-time/2019',
        'https://www.shu.ac.uk/courses/english/ba-honours-english-language/full-time/2019',
        'https://www.shu.ac.uk/courses/geography-and-environment/bsc-honours-environmental-science/full-time/2019',
        'https://www.shu.ac.uk/courses/criminology/ba-honours-criminology/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-interior-architecture-and-design/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/bsc-honours-computer-networks/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-jewellery-and-metalwork/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/bsc-honours-computer-security-with-forensics/full-time/2019',
        'https://www.shu.ac.uk/courses/film-and-performance/ba-honours-film-studies-and-screenwriting/full-time/2019',
        'https://www.shu.ac.uk/courses/media-pr-and-journalism/ba-honours-journalism-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-chemical-engineering-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-automotive-engineering-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/digital-media/ba-honours-digital-media-production-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/digital-media/ba-honours-film-and-media-production-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/digital-media/ba-honours-games-design-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/digital-media/ba-honours-animation-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/bsc-honours-computer-security-with-forensics-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/bsc-honours-cyber-security-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/film-and-performance/ba-honours-film-studies/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/bsc-honours-computing-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-sport-and-exercise-technology/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-product-design-furniture/full-time/2019',
        'https://www.shu.ac.uk/courses/business-and-management/ba-honours-international-business-with-german/full-time/2019',
        'https://www.shu.ac.uk/courses/english/ba-honours-english/full-time/2019',
        'https://www.shu.ac.uk/courses/digital-media/ba-honours-animation/full-time/2019',
        'https://www.shu.ac.uk/courses/tourism-and-hospitality/bsc-honours-international-tourism-and-hospitality-business-management/full-time/2019',
        'https://www.shu.ac.uk/courses/languages/ba-honours-languages-with-international-business-spanish/full-time/2019',
        'https://www.shu.ac.uk/courses/media-pr-and-journalism/ba-honours-media/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-illustration/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-fine-art/full-time/2019',
        'https://www.shu.ac.uk/courses/media-pr-and-journalism/ba-honours-public-relations-and-media/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-electrical-and-electronic-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/childhood-studies/ba-honours-childhood-studies/full-time/2019',
        'https://www.shu.ac.uk/courses/history/ba-honours-history/full-time/2019',
        'https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-studies/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-chemical-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/business-and-management/ba-honours-international-business-with-french/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-railway-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/mcomp-software-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/physics/bsc-honours-physics/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/bsc-honours-information-technology-with-business-studies/full-time/2019',
        'https://www.shu.ac.uk/courses/food-and-nutrition/bsc-honours-nutrition-and-public-health/full-time/2019',
        'https://www.shu.ac.uk/courses/construction-real-estate-and-surveying/bsc-honours-quantity-surveying/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-fashion-management-and-communication-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-mechanical-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/digital-media/ba-honours-photography/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/beng-honours-software-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/sociology-and-politics/ba-honours-applied-social-science/full-time/2019',
        'https://www.shu.ac.uk/courses/criminology/bsc-honours-criminology-and-psychology/full-time/2019',
        'https://www.shu.ac.uk/courses/languages/ba-honours-languages-with-international-business-french/full-time/2019',
        'https://www.shu.ac.uk/courses/tourism-and-hospitality/bsc-honours-international-hospitality-business-management/full-time/2019',
        'https://www.shu.ac.uk/courses/construction-real-estate-and-surveying/bsc-honours-building-surveying/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-computer-systems-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/event-management/bsc-honours-international-events-management/full-time/2019',
        'https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-sport-coaching/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/meng-mechanical-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/construction-real-estate-and-surveying/bsc-honours-construction-project-management/full-time/2019',
        'https://www.shu.ac.uk/courses/business-and-management/ba-honours-international-business/full-time/2019',
        'https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-sport-business-management/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/bsc-honours-cyber-security/full-time/2019',
        'https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-sport-development-with-coaching/full-time/2019',
        'https://www.shu.ac.uk/courses/economics/bsc-honours-economics/full-time/2019',
        'https://www.shu.ac.uk/courses/accounting-banking-and-finance/ba-honours-forensic-accounting/full-time/2019',
        'https://www.shu.ac.uk/courses/law/llb-hons-law/full-time/2019',
        'https://www.shu.ac.uk/courses/languages/ba-honours-languages-with-international-business-german/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/meng-aerospace-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-fashion-design/full-time/2019',
        'https://www.shu.ac.uk/courses/food-and-nutrition/bsc-honours-food-and-nutrition/full-time/2019',
        'https://www.shu.ac.uk/courses/radiotherapy-and-oncology/bsc-honours-radiotherapy-and-oncology/full-time/2019',
        'https://www.shu.ac.uk/courses/sociology-and-politics/ba-honours-sociology/full-time/2019',
        'https://www.shu.ac.uk/courses/occupational-therapy/bsc-honours-occupational-therapy/full-time/2019',
        'https://www.shu.ac.uk/courses/teaching-and-education/ba-honours-early-years-and-primary-education-37-with-qualified-teacher-status/full-time/2019',
        'https://www.shu.ac.uk/courses/diagnostic-radiography/bsc-honours-diagnostic-radiography/full-time/2019',
        'https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-nursing-child/full-time/2019',
        'https://www.shu.ac.uk/courses/tourism-and-hospitality/ba-honours-international-tourism-management-with-spanish/full-time/2019',
        'https://www.shu.ac.uk/courses/geography-and-environment/ba-honours-human-geography/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-graphic-design/full-time/2019',
        'https://www.shu.ac.uk/courses/languages/ba-honours-languages-with-teaching-english-to-speakers-of-other-languages-spanish/full-time/2019',
        'https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-and-marketing/full-time/2019',
        'https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-and-financial-management/full-time/2019',
        'https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-economics/full-time/2019',
        'https://www.shu.ac.uk/courses/languages/ba-honours-languages-with-teaching-english-to-speakers-of-other-languages-french/full-time/2019',
        'https://www.shu.ac.uk/courses/law/llb-hons-law-with-criminology/full-time/2019',
        'https://www.shu.ac.uk/courses/languages/ba-honours-languages-with-teaching-english-to-speakers-of-other-languages-german/full-time/2019',
        'https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-and-enterprise-management/full-time/2019',
        'https://www.shu.ac.uk/courses/accounting-banking-and-finance/ba-honours-finance-and-economics/full-time/2019',
        'https://www.shu.ac.uk/courses/languages/ba-honours-languages-with-tourism-german/full-time/2019',
        'https://www.shu.ac.uk/courses/media-pr-and-journalism/ba-honours-public-relations/full-time/2019',
        'https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-human-biology/full-time/2019',
        'https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-and-human-resource-management/full-time/2019',
        'https://www.shu.ac.uk/courses/teaching-and-education/ba-honours-education-with-psychology-and-counselling/full-time/2019',
        'https://www.shu.ac.uk/courses/psychology/bsc-honours-psychology/full-time/2019',
        'https://www.shu.ac.uk/courses/accounting-banking-and-finance/ba-honours-finance-and-banking/full-time/2019',
        'https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-biochemistry/full-time/2019',
        'https://www.shu.ac.uk/courses/digital-media/ba-honours-games-design/full-time/2019',
        'https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-chemistry/full-time/2019',
        'https://www.shu.ac.uk/courses/accounting-banking-and-finance/ba-honours-accounting-and-finance/full-time/2019',
        'https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-chemistry/full-time/2019',
        'https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-chemistry/full-time/2019',
        'https://www.shu.ac.uk/courses/architecture/bsc-honours-architecture/full-time/2019',
        'https://www.shu.ac.uk/courses/operating-department-practice/bsc-honours-operating-department-practice/full-time/2019',
        'https://www.shu.ac.uk/courses/paramedic-science/bsc-honours-paramedic-science/full-time/2019',
        'https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-nursing-learning-disability-and-social-work/full-time/2019',
        'https://www.shu.ac.uk/courses/social-work/ba-honours-social-work/full-time/2019',
        'https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-midwifery/full-time/2019',
        'https://www.shu.ac.uk/courses/engineering/beng-honours-materials-engineering/full-time/2019',
        'https://www.shu.ac.uk/courses/computing/bsc-honours-computer-networks-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-fashion-design-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/art-and-design/ba-honours-graphic-design-with-foundation-year/full-time/2019',
        'https://www.shu.ac.uk/courses/mathematics/bsc-honours-mathematics-with-foundation-year/full-time/2019'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Sheffield Hallam University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath("/html/body/section[1]//h1").extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en,response.url)

        #4.degree_type
        degree_type = 1

        #5.degree_name
        degree_name = response.xpath('/html/body/section[1]/div/div[2]/span').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #6.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'What is the fee?')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee =getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #7.tuition_fee_pre
        tuition_fee_pre = '£'

        #8.duration
        duration_list = response.xpath("//*[contains(text(),'How long will I study?')]//following-sibling::*").extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list).strip()
        duration =duration_list
        duration_per = 1

        #9.location
        location = 'Sheffield'

        #10.ucascode
        ucascode = response.xpath("//*[contains(text(),'What is the UCAS code?')]//following-sibling::*").extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode)
        ucascode = clear_space_str(ucascode)
        # print(ucascode)

        #11.overview_en
        overview_en = response.xpath("//*[contains(text(),'Course summary')]//following-sibling::*").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #12.career_en
        career_en = response.xpath("//*[contains(text(),'Future careers')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #13.alevel
        alevel = response.xpath('//*[@id="entry-requirements"]/div/div[1]/ul[2]/li[1]').extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel)
        # print(alevel)


        #14.apply_proces_en
        apply_proces_en = response.xpath('//*[@id="apply-now"]/div[1]//a/@href').extract()
        apply_proces_en = ''.join(apply_proces_en)
        # print(apply_proces_en)

        #16.duration_per
        duration_per = 1

        #17.ielts_desc
        ielts_desc = response.xpath('//*[@id="entry-requirements"]/div/div[1]').extract()
        ielts_desc = ''.join(ielts_desc)
        ielts_desc = remove_tags(ielts_desc)
        ielts_list = re.findall(r'[567]\.\d',ielts_desc)
        # print(ielts_list,response.url)
        if len(ielts_list) == 2:
            a = ielts_list[0]
            b = ielts_list[1]
            ielts = a
            ielts_r = b
            ielts_l = b
            ielts_s = b
            ielts_w = b
        else:
            ielts = None
            ielts_r = None
            ielts_l = None
            ielts_s = None
            ielts_w = None

        #18.require_chinese_en
        require_chinese_en = '<p>The following qualifications from China will be considered for entry on to undergraduate programmes, with a minimum average of 60 per cent: Diploma from Specialised College (Zhongzhnan) Diploma from Vocational Secondary School (Zhixiao) Three year middle school diploma plus foundation degree A levels Graduate Diploma from: Radio and TV Universities Spare Time Universities Training Colleges for Administrative cadres Higher Education Self Study Examinations Adult Education/Adult Education in Science and Technology subjects Senior High School Diploma Chinese University Entrance Examination (until 2003) College Graduation Diploma (Dazhuan awarded by university/college on completion of 2-3 years study) Applicants who have completed the first year of an undergraduate degree at a Chinese university may be considered for direct entry to Sheffield Hallam University undergraduate programmes.Sheffield Hallam welcomes applications from international school students taking the International Baccalaureate Diploma and those achieving 28 points or more will usually be successful in obtaining an offer of a place on our undergraduate programmes. For information about IB points equivalences against the UCAS tariff please visit the UCAS website.</p>'
        #19.apply_fre
        apply_pre = '£'
        #20.start_date
        start_date = response.xpath("//*[contains(text(),'When do I start?')]//following-sibling::*").extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        start_date = clear_space_str(start_date)
        # print(start_date)
        if'September, January' in start_date:
            start_date = '2018-9,2019-1'
        elif 'January' in start_date:
            start_date = '2019-1'
        else:
            start_date = translate_month(start_date)
            start_date = '2018-'+str(start_date)
        # print(start_date)

        #21.modules_en
        modules_en = response.xpath('//div[@data-section="split"][6]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        item['modules_en'] = modules_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['start_date'] = start_date
        item['apply_pre'] = apply_pre
        item['require_chinese_en'] = require_chinese_en
        item['ielts_desc'] = ielts_desc
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['duration'] = duration
        item['location'] = location
        item['ucascode'] = ucascode
        item['overview_en'] = overview_en
        item['career_en'] = career_en
        item['alevel'] = alevel
        item['apply_proces_en'] = apply_proces_en
        item['duration_per'] = duration_per
        yield  item