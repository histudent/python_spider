# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/12/18 15:41'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.getItem import get_item
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from lxml import etree
import requests
class HumberCollege_CSpider(scrapy.Spider):
    name = 'HumberCollege_C'
    allowed_domains = ['humber.ca/']
    start_urls = []
    C= [
        'https://business.humber.ca/programs/business-accounting.html',
        'https://business.humber.ca/programs/business-administration-accounting.html',
        'http://creativearts.humber.ca/programs/acting-for-film-and-television',
        'https://mediastudies.humber.ca/programs/advertising-and-graphic-design.html',
        'https://mediastudies.humber.ca/programs/advertising-and-marketing-communications.html',
        'https://mediastudies.humber.ca/programs/animation-3d.html',
        'http://appliedtechnology.humber.ca/programs/architectural-technology.html',
        'http://hrt.humber.ca/programs/baking-pastry-management.html',
        'http://healthsciences.humber.ca/programs/biotechnology.html',
        'https://mediastudies.humber.ca/programs/brtv.html',
        'https://mediastudies.humber.ca/programs/broadcasting-radio.html',
        'https://appliedtechnology.humber.ca/programs/building-construction-technician.html',
        'https://business.humber.ca/programs/business-administration.html',
        'https://business.humber.ca/programs/business-administration-co-op.html',
        'https://business.humber.ca/programs/business-management.html',
        'http://appliedtechnology.humber.ca/programs/carpentry-and-renovation-technician.html',
        'https://communityservices.humber.ca/programs/child-and-youth-care.html',
        'https://communityservices.humber.ca/programs/child-and-youth-care-accelerated.html',
        'http://appliedtechnology.humber.ca/programs/civil-engineering-technology.html',
        'http://creativearts.humber.ca/programs/comedy/comedy-writing-and-performance',
        'https://communityservices.humber.ca/programs/community-and-justice-services.html',
        'https://appliedtechnology.humber.ca/programs/computer-and-network-support-technician.html',
        'http://appliedtechnology.humber.ca/programs/computer-engineering-technology.html',
        'https://appliedtechnology.humber.ca/programs/computer-programmer.html',
        'https://appliedtechnology.humber.ca/programs/construction-engineering-technology.html',
        'https://business.humber.ca/programs/cosmetic-management.html',
        'https://hrt.humber.ca/programs/culinary-management.html',
        'https://communityservices.humber.ca/programs/developmental-services-worker.html',
        'https://communityservices.humber.ca/programs/developmental-services-worker-accelerated.html',
        'http://healthsciences.humber.ca/programs/early-childhood-education.html',
        'http://appliedtechnology.humber.ca/programs/electrical-engineering-technician-control-systems.html',
        'http://appliedtechnology.humber.ca/programs/electrical-engineering-technology-control-systems.html',
        'https://appliedtechnology.humber.ca/programs/electromechanical-engineering-technician-automation-and-robotics-profile.html',
        'https://appliedtechnology.humber.ca/programs/electromechanical-engineering-technology-automation-and-robotics-profile.html',
        'http://appliedtechnology.humber.ca/programs/electronics-engineering-technician.html',
        'http://appliedtechnology.humber.ca/programs/electronics-engineering-technology.html',
        'https://business.humber.ca/programs/esthetician-spa-management.html',
        'https://business.humber.ca/programs/fashion-arts.html',
        'https://mediastudies.humber.ca/programs/fmtv.html',
        'https://business.humber.ca/programs/business-management-financial-services.html',
        'https://communityservices.humber.ca/programs/fire-services.html',
        'http://hrt.humber.ca/programs/fitness-health-promotion.html',
        'http://hrt.humber.ca/programs/food-nutrition-management.html',
        'http://healthsciences.humber.ca/programs/funeral-director-class-1-embalming.html',
        'http://healthsciences.humber.ca/programs/funeral-director-class-2-non-embalming.html',
        'https://mediastudies.humber.ca/programs/game-programming.html',
        'http://liberalarts.humber.ca/programs/general-arts-and-science-university-transfer-diploma.html',
        'https://mediastudies.humber.ca/programs/graphic-design.html',
        'http://appliedtechnology.humber.ca/programs/heating-refrigeration-and-air-conditioning-technician.html',
        'http://appliedtechnology.humber.ca/programs/heating-refrigeration-and-air-conditioning-technology.html',
        'http://hrt.humber.ca/programs/hospitality-event-management.html',
        'http://hrt.humber.ca/programs/hospitality-hotel-and-restaurant-operations-management.html',
        'http://appliedtechnology.humber.ca/programs/industrial-woodworking-technician.html',
        'http://appliedtechnology.humber.ca/programs/interior-decorating.html',
        'https://mediastudies.humber.ca/programs/journalism-diploma.html',
        'http://appliedtechnology.humber.ca/programs/landscape-technician.html',
        'https://business.humber.ca/programs/law-clerk.html',
        'https://business.humber.ca/programs/business-marketing.html',
        'http://hrt.humber.ca/programs/massage-therapy.html',
        'http://appliedtechnology.humber.ca/programs/mechanical-engineering-technician.html',
        'http://appliedtechnology.humber.ca/programs/mechanical-engineering-technology.html',
        'https://mediastudies.humber.ca/programs/media-communications.html',
        'https://mediastudies.humber.ca/programs/multimedia-design-and-development.html',
        'http://hrt.humber.ca/programs/nutrition-and-healthy-lifestyle-promotion.html',
        'http://healthsciences.humber.ca/programs/occupational-therapist-assistant-and-physiotherapist-assistant.html',
        'https://business.humber.ca/programs/paralegal-education.html',
        'http://healthsciences.humber.ca/programs/paramedic.html',
        'http://healthsciences.humber.ca/programs/pharmacy-technician.html',
        'https://mediastudies.humber.ca/programs/photography.html',
        'http://communityservices.humber.ca/programs/police-foundations',
        'http://healthsciences.humber.ca/programs/practical-nursing.html',
        'https://business.humber.ca/programs/business-administration-professional-golf-management.html',
        'http://communityservices.humber.ca/programs/protection-security-and-investigation',
        'http://communityservices.humber.ca/programs/protection-security-and-investigation-crime-scene-investigation',
        'https://mediastudies.humber.ca/programs/public-relations.html',
        'http://hrt.humber.ca/programs/recreation-leisure-services.html',
        'http://communityservices.humber.ca/programs/social-service-worker',
        'http://hrt.humber.ca/programs/sport-management',
        'http://appliedtechnology.humber.ca/programs/sustainable-energy-and-building-technology.html',
        'http://creativearts.humber.ca/programs/theatre-performance',
        'http://creativearts.humber.ca/programs/theatre-production',
        'http://hrt.humber.ca/programs/tourism-travel-services-management.html',
        'http://healthsciences.humber.ca/programs/traditional-chinese-medicine-practitioner.html',
        'https://mediastudies.humber.ca/programs/visual-and-digital-arts.html',
        'https://mediastudies.humber.ca/programs/web-design-interactive-media.html',
        'https://communityservices.humber.ca/programs/addictions-and-mental-health.html',
        'https://hrt.humber.ca/programs/advanced-chocolate-and-confectionery-artistry.html',
        'https://mediastudies.humber.ca/programs/advertising-account-management.html',
        'https://business.humber.ca/programs/advertising-media-management.html',
        'https://mediastudies.humber.ca/programs/advertising-copywriting.html',
        'https://business.humber.ca/programs/alternative-dispute-resolution.html',
        'http://creativearts.humber.ca/programs/arts-administration-and-cultural-management',
        'http://healthsciences.humber.ca/programs/clinical-research-graduate.html',
        'https://mediastudies.humber.ca/programs/content-strategy',
        'http://creativearts.humber.ca/programs/creative-book-publishing',
        'http://creativearts.humber.ca/programs/school-writers/creative-writing-fiction-creative-non-fiction-poetry.html',
        'http://healthsciences.humber.ca/programs/early-childhood-education-special-needs',
        'https://appliedtechnology.humber.ca/programs/enterprise-software-development.html',
        'https://business.humber.ca/programs/entrepreneurial-enterprise.html',
        'https://business.humber.ca/programs/event-management.html',
        'http://hrt.humber.ca/programs/exercise-science-lifestyle-management.html',
        'https://business.humber.ca/programs/fashion-management-and-promotions.html',
        'https://mediastudies.humber.ca/programs/film-and-multiplatform-storytelling.html',
        'https://business.humber.ca/programs/financial-planning.html',
        'https://communityservices.humber.ca/programs/forensic-identification.html',
        'https://business.humber.ca/programs/fundraising-management.html',
        'https://business.humber.ca/programs/global-business-management.html',
        'http://hrt.humber.ca/programs/hospitality-tourism-operations-management.html',
        'https://business.humber.ca/programs/human-resources-management.html',
        'https://appliedtechnology.humber.ca/programs/information-technology-solutions.html',
        'https://business.humber.ca/programs/insurance-management-property-and-casualty.html',
        'https://business.humber.ca/programs/international-development.html',
        'https://mediastudies.humber.ca/programs/journalism.html',
        'https://business.humber.ca/programs/marketing-management.html',
        'http://creativearts.humber.ca/programs/music/music-business.html',
        'http://creativearts.humber.ca/programs/music/music-composition.html',
        'https://business.humber.ca/programs/paralegal.html',
        'https://mediastudies.humber.ca/programs/post-production.html',
        'https://business.humber.ca/programs/professional-accounting-practice.html',
        'http://liberalarts.humber.ca/programs/professional-writing-and-communications.html',
        'http://appliedtechnology.humber.ca/programs/project-management.html',
        'https://business.humber.ca/programs/public-administration.html',
        'https://mediastudies.humber.ca/programs/public-relations-postgraduate.html',
        'https://mediastudies.humber.ca/programs/radio-and-media-production.html',
        'http://healthsciences.humber.ca/programs/regulatory-affairs-graduate.html',
        'http://liberalarts.humber.ca/programs/research-analyst.html',
        'http://hrt.humber.ca/programs/sport-business-management.html',
        'https://appliedtechnology.humber.ca/programs/supply-chain-management.html',
        'https://healthsciences.humber.ca/programs/systems-navigator.html',
        'http://liberalarts.humber.ca/programs/teaching-english-as-a-second-language.html',
        'http://creativearts.humber.ca/programs/television-writing-and-producing',
        'https://mediastudies.humber.ca/programs/ux-design.html',
        'https://mediastudies.humber.ca/programs/web-development.html',
        'http://hrt.humber.ca/programs/wellness-coaching.html',
        'http://appliedtechnology.humber.ca/programs/wireless-telecommunications.html',
        'https://business.humber.ca/programs/accounting-bachelor-of-commerce.html',
        'https://communityservices.humber.ca/programs/behavioural-science-bachelor.html',
        'https://communityservices.humber.ca/programs/child-and-youth-care-bachelor-of-arts.html',
        'https://communityservices.humber.ca/programs/community-development-bachelor-of.html',
        'https://mediastudies.humber.ca/programs/creative-advertising.html',
        'https://communityservices.humber.ca/programs/criminal-justice-bachelor-of-social-science.html',
        'https://mediastudies.humber.ca/programs/design.html',
        'https://business.humber.ca/programs/digital-business-management.html',
        'https://mediastudies.humber.ca/programs/digital-communications.html',
        'https://business.humber.ca/programs/fashion-management.html',
        'https://mediastudies.humber.ca/programs/film-and-media-production.html',
        'https://business.humber.ca/programs/finance.html',
        'https://business.humber.ca/programs/healthcare-management.html',
        'https://business.humber.ca/programs/hospitality-and-tourism-management.html',
        'https://business.humber.ca/programs/bachelor-of-human-resources-management.html',
        'http://appliedtechnology.humber.ca/programs/bachelor-of-industrial-design.html',
        'http://appliedtechnology.humber.ca/programs/bachelor-of-interior-design.html',
        'https://business.humber.ca/programs/international-business.html',
        'https://business.humber.ca/programs/bachelor-of-international-development.html',
        'https://mediastudies.humber.ca/programs/journalism-bachelor.html',
        'https://business.humber.ca/programs/management-studies.html',
        'https://business.humber.ca/programs/marketing.html',
        'http://creativearts.humber.ca/programs/music/music-bachelor-of.html',
        'http://healthsciences.humber.ca/programs/bachelor-of-nursing.html',
        'https://business.humber.ca/programs/bachelor-of-paralegal-studies.html',
        'https://mediastudies.humber.ca/programs/public-relations-bachelor.html',
        'https://business.humber.ca/programs/supply-chain-management.html',
        'http://healthsciences.humber.ca/programs/bachelor-of-health-sciences-workplace-health-and-wellness'
    ]
    for i in C:
        start_urls.append(i)

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaCollegeItem)

        #1.school_name
        school_name = 'Humber College'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.location
        location = 'Ontario, Canada'

        #4.programme_code
        programme_code = response.xpath("//*[contains(text(),'Program Code: ')]").extract()
        programme_code = ''.join(programme_code)
        programme_code = remove_tags(programme_code).replace('Program Code: ','')
        # print(programme_code)

        #5.overview_en
        overview_en = response.xpath("//*[contains(text(),'Courses')]//preceding-sibling::*").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #6.modules_en
        modules_en = response.xpath("//div[contains(@class,'curriculum')]").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #7.career_en
        career_en = response.xpath("//div[contains(@class,'learning-outcomes')]").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #8.start_date
        start_date = response.xpath('//td[@data-label="START DATE"]').extract()
        start_date = ','.join(start_date)
        start_date = remove_tags(start_date).replace('September 2019','2019-09').replace('January 2020','2020-01').replace('January 2019','2019-01').replace('May 2019','2019-05').replace('January 2020','2019-01').replace('May 2020','2020-05')
        # print(start_date)

        #9.department
        department = response.xpath('//*[@id="HumberNav"]/div[2]/h1/a').extract()
        department = ''.join(department)
        department = remove_tags(department).replace('&amp; ','')
        # print(department)

        #10.tuition_fee_pre
        tuition_fee_pre = '$'

        item['school_name'] = school_name
        item['url'] = url
        item['location'] = location
        item['programme_code'] = programme_code
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['start_date'] = start_date
        item['department'] = department
        item['tuition_fee_pre'] = tuition_fee_pre
        yield item