# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/12/19 16:11'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.getItem import get_item
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from lxml import etree
import requests
class GeorgeBrownCollege_CSpider(scrapy.Spider):
    name = 'GeorgeBrownCollege_C'
    allowed_domains = ['georgebrown.ca/']
    start_urls = []
    C= ['https://www.georgebrown.ca/programs/interaction-design-program-g113/',
'https://www.georgebrown.ca/programs/game-art-program-g119/',
'https://www.georgebrown.ca/programs/honours-bachelor-of-digital-experience-design-g301/',
'https://www.georgebrown.ca/programs/design-management-program-postgraduate-g401/',
'https://www.georgebrown.ca/programs/digital-design-game-design-program-postgraduate-g405/',
'https://www.georgebrown.ca/programs/concept-art-for-entertainment-program-postgraduate-g407/',
'https://www.georgebrown.ca/programs/interactive-media-management-program-postgraduate-g412/',
'https://www.georgebrown.ca/programs/interdisciplinary-design-strategy-postgraduate-at-the-institute-without-boundaries-g414/',
'https://www.georgebrown.ca/programs/fashion-management-program-f102/',
'https://www.georgebrown.ca/programs/jewellery-methods-program-f110/',
'https://www.georgebrown.ca/programs/fashion-business-industry-program-f112/',
'https://www.georgebrown.ca/programs/fashion-techniques-and-design-program-f113/',
'https://www.georgebrown.ca/programs/jewellery-arts-program-f114/',
'https://www.georgebrown.ca/programs/international-fashion-management-postgraduate-certificate-program-f412/',
'https://www.georgebrown.ca/programs/apparel-technical-design-postgraduate-certificate-program-f414/',
'https://www.georgebrown.ca/programs/sustainable-fashion-production-postgraduate-certificate-program-f415/',
'https://www.georgebrown.ca/programs/video-design-and-production-program-g112/',
'https://www.georgebrown.ca/programs/visual-effects-program-postgraduate-g408/',
'https://www.georgebrown.ca/programs/sound-design-and-production-postgraduate-g409/',
'https://www.georgebrown.ca/programs/theatre-arts-performance-program-p104/',
'https://www.georgebrown.ca/programs/dance-performance-program-p105/',
'https://www.georgebrown.ca/programs/acting-for-media-program-p107/',
'https://www.georgebrown.ca/programs/screenwriting-and-narrative-design-p400/',
'https://www.georgebrown.ca/programs/computer-programmer-analyst-program-t127/',
'https://www.georgebrown.ca/programs/computer-systems-technician-program-t141/',
'https://www.georgebrown.ca/programs/computer-systems-technology-program-t147/',
'https://www.georgebrown.ca/programs/game-programming-program-t163/',
'https://www.georgebrown.ca/programs/health-informatics-program-postgraduate-t402/',
'https://www.georgebrown.ca/programs/information-systems-business-analysis-program-with-experiential-learning-capstone-t405/',
'https://www.georgebrown.ca/programs/wireless-networking-program-postgraduate-t411/',
'https://www.georgebrown.ca/programs/network-and-system-security-analysis-program-postgraduate-t413/',
'https://www.georgebrown.ca/programs/business-accounting-program-b103/',
'https://www.georgebrown.ca/programs/business-administration-accounting-program-b107/',
'https://www.georgebrown.ca/programs/business-administration-finance-program-b130/',
'https://www.georgebrown.ca/programs/business-finance-program-b133/',
'https://www.georgebrown.ca/programs/business-administration-finance-program-with-work-experience-b150/',
'https://www.georgebrown.ca/programs/business-administration-accounting-program-with-work-experience-b157/',
'https://www.georgebrown.ca/programs/honours-bachelor-of-commerce-financial-services-b302/',
'https://www.georgebrown.ca/programs/financial-planning-program-postgraduate-b407/',
'https://www.georgebrown.ca/programs/business-human-resources-program-b134/',
'https://www.georgebrown.ca/programs/business-administration-human-resources-program-b144/',
'https://www.georgebrown.ca/programs/business-administration-human-resources-program-with-work-experience-b154/',
'https://www.georgebrown.ca/programs/human-resources-management-program-postgraduate-b408/',
'https://www.georgebrown.ca/programs/business-administration-supply-chain-and-operations-management-program-b122/',
'https://www.georgebrown.ca/programs/business-administration-retail-program-b123/',
'https://www.georgebrown.ca/programs/business-program-b125/',
'https://www.georgebrown.ca/programs/business-administration-project-management-program-b126/',
'https://www.georgebrown.ca/programs/business-administration-international-business-program-b131/',
'https://www.georgebrown.ca/programs/business-administration-program-b145/',
'https://www.georgebrown.ca/programs/business-administration-program-with-work-experience-b155/',
'https://www.georgebrown.ca/programs/business-administration-project-management-program-with-work-experience-b156/',
'https://www.georgebrown.ca/programs/business-administration-international-business-program-with-work-experience-b161/',
'https://www.georgebrown.ca/programs/business-administration-supply-chain-and-operations-management-program-with-work-experience-b162/',
'https://www.georgebrown.ca/programs/business-administration-retail-program-with-work-experience-b163/',
'https://www.georgebrown.ca/programs/international-business-management-program-postgraduate-b411/',
'https://www.georgebrown.ca/programs/analytics-for-business-decision-making-program-postgraduate-b412/',
'https://www.georgebrown.ca/programs/consulting-program-postgraduate-b414/',
'https://www.georgebrown.ca/programs/project-management-program-postgraduate-b415/',
'https://www.georgebrown.ca/programs/entrepreneurship-management-program-postgraduate-b416/',
'https://www.georgebrown.ca/programs/business-administration-marketing-program-b108/',
'https://www.georgebrown.ca/programs/business-marketing-program-b120/',
'https://www.georgebrown.ca/programs/business-administration-marketing-program-with-work-experience-b158/',
'https://www.georgebrown.ca/programs/sport-and-event-marketing-program-postgraduate-b400/',
'https://www.georgebrown.ca/programs/marketing-management-financial-services-program-postgraduate-b406/',
'https://www.georgebrown.ca/programs/strategic-relationship-marketing-program-postgraduate-b409/',
'https://www.georgebrown.ca/programs/digital-media-marketing-program-postgraduate-b413/',
'https://www.georgebrown.ca/programs/intervenor-for-deafblind-persons-program-c108/',
'https://www.georgebrown.ca/programs/honours-bachelor-of-interpretation-program-american-sign-language-english-c302/',
'https://www.georgebrown.ca/programs/early-childhood-education-program-c100/',
'https://www.georgebrown.ca/programs/early-childhood-education-consecutive-diploma-degree-program-c118/',
'https://www.georgebrown.ca/programs/early-childhood-education-program-fast-track-c130/',
'https://www.georgebrown.ca/programs/early-childhood-education-program-accelerated-c160/',
'https://www.georgebrown.ca/programs/honours-bachelor-of-early-childhood-leadership-program-c300/',
'https://www.georgebrown.ca/programs/honours-bachelor-of-early-childhood-leadership-program-fast-track-c301/',
'https://www.georgebrown.ca/programs/community-worker-program-c101/',
'https://www.georgebrown.ca/programs/social-service-worker-program-c119/',
'https://www.georgebrown.ca/programs/community-worker-program-fast-track-c131/',
'https://www.georgebrown.ca/programs/child-and-youth-care-program-c133/',
'https://www.georgebrown.ca/programs/social-service-worker-program-fast-track-c135/',
'https://www.georgebrown.ca/programs/assaulted-womens-and-childrens-counsellor-advocate-program-c137/',
'https://www.georgebrown.ca/programs/child-and-youth-care-program-fast-track-c143/',
'https://www.georgebrown.ca/programs/career-development-practitioner-program-c406/',
'https://www.georgebrown.ca/programs/construction-engineering-technology-program-t105/',
'https://www.georgebrown.ca/programs/construction-engineering-technician-program-t161/',
'https://www.georgebrown.ca/programs/civil-engineering-technology-program-t164/',
'https://www.georgebrown.ca/programs/honours-bachelor-of-technology-construction-management-t312/',
'https://www.georgebrown.ca/programs/construction-management-for-internationally-educated-professionals-program-postgraduate-t403/',
'https://www.georgebrown.ca/programs/residential-construction-management-program-postgraduate-t408/',
'https://www.georgebrown.ca/programs/building-information-modeling-bim-management-program-postgraduate-t412/',
'https://www.georgebrown.ca/programs/building-renovation-technician-program-t110/',
'https://www.georgebrown.ca/programs/building-renovation-technology-program-t148/',
'https://www.georgebrown.ca/programs/heating-refrigeration-and-air-conditioning-technician-program-t160/',
'https://www.georgebrown.ca/programs/heating-refrigeration-and-air-conditioning-technology-program-t162/',
'https://www.georgebrown.ca/programs/architectural-technology-program-t109/',
'https://www.georgebrown.ca/programs/architectural-technician-program-t132/',
'https://www.georgebrown.ca/programs/interior-design-technology-program-t170/',
'https://www.georgebrown.ca/programs/mechanical-engineering-technology-design-program-t121/',
'https://www.georgebrown.ca/programs/electromechanical-engineering-technician-program-t146/',
'https://www.georgebrown.ca/programs/electromechanical-engineering-technology-building-automation-program-t171/',
'https://www.georgebrown.ca/programs/mechanical-technician-cnc-and-precision-machining-t173/',
'https://www.georgebrown.ca/programs/dental-technology-program-s100/',
'https://www.georgebrown.ca/programs/denturism-program-s101/',
'https://www.georgebrown.ca/programs/dental-hygiene-program-s124/',
'https://www.georgebrown.ca/programs/restorative-dental-hygiene-postgraduate-program-s400/',
'https://www.georgebrown.ca/programs/activation-co-ordinator-gerontology-program-c102/',
'https://www.georgebrown.ca/programs/behavioural-science-technician-program-c146/',
'https://www.georgebrown.ca/programs/behavioural-science-technician-program-intensive-c156/',
'https://www.georgebrown.ca/programs/autism-and-behavioural-science-program-postgraduate-c405/',
'https://www.georgebrown.ca/programs/orthotic-prosthetic-technician-program-s102/',
'https://www.georgebrown.ca/programs/hearing-instrument-specialist-program-s117/',
'https://www.georgebrown.ca/programs/fitness-and-health-promotion-program-s125/',
'https://www.georgebrown.ca/programs/honours-bachelor-of-behaviour-analysis-program-s302/',
'https://www.georgebrown.ca/programs/honours-bachelor-of-behaviour-analysis-program-intensive-s303/',
'https://www.georgebrown.ca/programs/clinical-methods-in-orthotics-prosthetics-program-postgraduate-s407/',
'https://www.georgebrown.ca/programs/health-information-management-program-c139/',
'https://www.georgebrown.ca/programs/office-administration-health-services-program-s135/',
'https://www.georgebrown.ca/programs/bachelor-of-science-in-nursing-bscn-s118/',
'https://www.georgebrown.ca/programs/practical-nursing-program-pn-s121/',
'https://www.georgebrown.ca/programs/registered-nurse-critical-care-nursing-program-postgraduate-s402/',
'https://www.georgebrown.ca/programs/registered-nurse-perinatal-intensive-care-nursing-program-postgraduate-s404/',
'https://www.georgebrown.ca/programs/registered-nurse-operating-room-perioperative-nursing-postgraduate-program-s414/',
'https://www.georgebrown.ca/programs/registered-nurse-critical-care-nursing-program-online-postgraduate-s422/',
'https://www.georgebrown.ca/programs/culinary-management-program-h100/',
'https://www.georgebrown.ca/programs/baking-and-pastry-arts-management-program-h113/',
'https://www.georgebrown.ca/programs/culinary-management-integrated-learning-program-h116/',
'https://www.georgebrown.ca/programs/culinary-management-nutrition-program-h119/',
'https://www.georgebrown.ca/programs/honours-bachelor-of-commerce-culinary-management-h315/',
'https://www.georgebrown.ca/programs/honours-bachelor-of-commerce-culinary-management-bridging-h316/',
'https://www.georgebrown.ca/programs/food-and-nutrition-management-program-postgraduate-h402/',
'https://www.georgebrown.ca/programs/culinary-arts-italian-postgraduate-program-h411/',
'https://www.georgebrown.ca/programs/advanced-french-patisserie-postgraduate-program-h413/',
'https://www.georgebrown.ca/programs/tourism-and-hospitality-management-program-h130/',
'https://www.georgebrown.ca/programs/special-event-management-program-h131/',
'https://www.georgebrown.ca/programs/food-and-beverage-management-restaurant-management-program-h132/',
'https://www.georgebrown.ca/programs/hospitality-hotel-operations-management-program-h133/',
'https://www.georgebrown.ca/programs/honours-bachelor-of-business-administration-hospitality-h311/',
'https://www.georgebrown.ca/programs/honours-bachelor-of-business-administration-hospitality-fast-track-h312/',
'https://www.georgebrown.ca/programs/advanced-wine-and-beverage-business-management-postgraduate-program-h414/',
'https://www.georgebrown.ca/programs/college-teachers-training-for-Internationally-educated-professionals-postgraduate-program-r403/',
'https://www.georgebrown.ca/programs/general-arts-and-science-two-year-diploma-program-r101/',
'https://www.georgebrown.ca/programs/graphic-design-program-g102/']
    C = set(C)
    for i in C:
        start_urls.append(i)

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaCollegeItem)

        #1.school_name
        school_name = 'George Brown College'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        # 3.location
        location = 'Ontario, Canada'

        #4.major_name_en
        major_name_en = response.xpath("//div[contains(text(),'Program name')]//following-sibling::*").extract()
        major_name_en = ''.join(major_name_en)
        major_name_en = remove_tags(major_name_en).replace('&amp; ','')
        # print(major_name_en)

        #5.programme_code
        programme_code = response.xpath("//div[contains(text(),'Code')]//following-sibling::*").extract()
        programme_code = ''.join(programme_code)
        programme_code = remove_tags(programme_code)
        # print(programme_code)

        #6.duration #7.duration_per
        duration = response.xpath("//div[contains(text(),'Duration')]//following-sibling::*").extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        duration = re.findall('\d+\s[a-zA-Z]+',duration)[0]
        # print(duration)
        if 'year' in duration:
            duration_per = 1
        elif 'semester' in duration:
            duration_per = 2
        elif 'month' in duration:
            duration_per = 3
        elif 'weeks' in duration:
            duration_per = 4
        else:
            duration_per = None
        duration = re.findall('\d+',duration)[0]
        if duration_per == None:
            if duration ==1:
                duration_per = 2
            else:
                duration_per = 3
        # print(duration,'*************',duration_per)

        #8.department
        department = response.xpath("//div[contains(text(),'School')]//following-sibling::*").extract()
        department = ''.join(department)
        department = remove_tags(department)
        department = clear_space_str(department)
        # print(department)

        #9.degree_name #10.degree_level
        degree_name = response.xpath("//div[contains(text(),'Credential')]//following-sibling::*").extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        degree_name = clear_space_str(degree_name)
        # print(degree_name)
        if 'Advanced Diploma' in degree_name:
            degree_name = 'Advanced Diploma'
            degree_level = 3
        elif 'Diploma' in degree_name:
            degree_name = 'Diploma'
            degree_level = 3
        elif 'Graduate Certificate' in degree_name:
            degree_name = 'Graduate Certificate'
            degree_level =  2
        else:
            degree_level = 1
            degree_name = degree_name
        # print(degree_name,degree_level)

        #11.start_date
        start_date = response.xpath("//div[contains(text(),'Starting month')]//following-sibling::*").extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        if 'September, January, May' in start_date:
            start_date = '2019-01,2019-05,2019-09'
        elif 'September, January' in start_date:
            start_date = '2019-01,2019-09'
        elif 'May' in start_date:
            start_date = '2019-05'
        elif 'September' in start_date:
            start_date = '2019-09'
        elif 'January' in start_date:
            start_date = '2019-01'
        else:
            start_date = None
        # print(start_date)

        #12.campus
        campus = response.xpath("//div[contains(text(),'Location')]//following-sibling::*").extract()
        campus = ''.join(campus)
        campus = remove_tags(campus)
        campus = clear_space_str(campus)
        # print(campus)

        #13.overview_en
        overview_en = response.xpath('//*[@id="overview-intro"]/div[1]/div').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #14.modules_en
        modules_en = response.xpath('//*[@id="coursesContent"]/div[1]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #15.career_en
        career_en = response.xpath('//*[@id="careersContent"]/div[1]').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #16.entry_requirements_en
        entry_requirements_en = response.xpath('//*[@id="admReqsContent"]/div[1]/div[1]').extract()
        entry_requirements_en = ''.join(entry_requirements_en)
        entry_requirements_en = remove_class(entry_requirements_en)
        # print(entry_requirements_en)

        #17.tuition_fee
        if degree_level ==1:
            tuition_fee = '16,500'
        else:
            tuition_fee = '13,520'

        #18.tuition_fee_pre
        tuition_fee_pre = '$'

        #19.apply_fee
        apply_fee = '95'

        #20.apply_pre
        apply_pre = '$'

        #21.ielts_desc 2223242526
        ielts_desc = 'Diploma/Certificate Programs:6.0, minimum 5.5 in each skill band;Postgraduate Programs and Fast-track/ Bridges**:6.5, minimum 6.0 in each skill band;GBC Degree Programs*:6.5, minimum 6.0 in each skill band'
        if degree_level ==1:
            ielts = 6.5
            ielts_r = 6
            ielts_w = 6
            ielts_s = 6
            ielts_l = 6
        else:
            ielts = 6
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_s = 5.5
            ielts_l = 5.5

        #27.deadline
        deadline = '2019-05-31'

        #28.toefl_desc 2930313233
        toefl_desc = 'Diploma/Certificate Programs:80 (online) minimum 20 in each skill band,Postgraduate Programs and Fast-track/ Bridges**:88 (online) minimum 22 in each skill band,GBC Degree Programs*:84 (online) minimum 21 in each skill band'
        if degree_level == 1:
            toefl = 84
            toefl_r = 21
            toefl_w = 21
            toefl_s = 21
            toefl_l = 21
        else:
            toefl = 80
            toefl_r = 20
            toefl_w = 20
            toefl_s = 20
            toefl_l = 20
        item['school_name'] = school_name
        item['url'] = url
        item['location'] = location
        item['major_name_en'] = major_name_en
        item['programme_code'] = programme_code
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['department'] = department
        item['degree_name'] = degree_name
        item['degree_level'] = degree_level
        item['start_date'] = start_date
        item['campus'] = campus
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['entry_requirements_en'] = entry_requirements_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_fee'] = apply_fee
        item['apply_pre'] = apply_pre
        item['ielts_desc'] = ielts_desc
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['deadline'] = deadline
        item['toefl_desc'] = toefl_desc
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_w'] = toefl_w
        item['toefl_l'] = toefl_l
        item['ielts'] = ielts
        item['toefl'] = toefl
        yield item
