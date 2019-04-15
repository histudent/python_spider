# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/12/21 9:40'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.getItem import get_item
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from lxml import etree
import requests
class FlemingCollege_CSpider(scrapy.Spider):
    name = 'FlemingCollege_C'
    allowed_domains = ['flemingcollege.ca/']
    start_urls = []
    C= ['https://flemingcollege.ca/programs/accounting',
'https://flemingcollege.ca/programs/advanced-water-systems-operations-and-management-co-op',
'https://flemingcollege.ca/programs/applied-planning-environmental',
'https://flemingcollege.ca/programs/aquaculture',
'https://flemingcollege.ca/programs/biotechnology-advanced',
'https://flemingcollege.ca/programs/business',
'https://flemingcollege.ca/programs/business-human-resources',
'https://flemingcollege.ca/programs/business-administration',
'https://flemingcollege.ca/programs/business-administration-accounting',
'https://flemingcollege.ca/programs/business-administration-human-resources-management',
'https://flemingcollege.ca/programs/business-administration-marketing',
'https://flemingcollege.ca/programs/carpentry-and-renovation-technician',
'https://flemingcollege.ca/programs/carpentry-and-renovation-techniques',
'https://flemingcollege.ca/programs/child-and-youth-care',
'https://flemingcollege.ca/programs/community-and-justice-services',
'https://flemingcollege.ca/programs/computer-engineering-technician',
'https://flemingcollege.ca/programs/computer-engineering-technology',
'https://flemingcollege.ca/programs/computer-security-and-investigations',
'https://flemingcollege.ca/programs/conservation-and-environmental-law-enforcement',
'https://flemingcollege.ca/programs/construction-engineering-technician',
'https://flemingcollege.ca/programs/culinary-management',
'https://flemingcollege.ca/programs/cultural-heritage-conservation-and-management',
'https://flemingcollege.ca/programs/customs-border-services',
'https://flemingcollege.ca/programs/developmental-services-worker',
'https://flemingcollege.ca/programs/early-childhood-education',
'https://flemingcollege.ca/programs/earth-resources-technician-co-op',
'https://flemingcollege.ca/programs/ecological-restoration',
'https://flemingcollege.ca/programs/ecosystem-management-technician',
'https://flemingcollege.ca/programs/ecosystem-management-technology',
'https://flemingcollege.ca/programs/ecosystem-management-technology-advanced-standing',
'https://flemingcollege.ca/programs/educational-support',
'https://flemingcollege.ca/programs/educational-support-advanced-standing',
'https://flemingcollege.ca/programs/electrical-engineering-technician',
'https://flemingcollege.ca/programs/electrical-power-generation-technician',
'https://flemingcollege.ca/programs/environmental-technician',
'https://flemingcollege.ca/programs/environmental-technician-advanced-standing',
'https://flemingcollege.ca/programs/environmental-technology',
'https://flemingcollege.ca/programs/environmental-visual-communication',
'https://flemingcollege.ca/programs/esthetician',
'https://flemingcollege.ca/programs/expressive-arts',
'https://flemingcollege.ca/programs/fibre-arts',
'https://flemingcollege.ca/programs/fish-and-wildlife-technician',
'https://flemingcollege.ca/programs/fish-and-wildlife-technology',
'https://flemingcollege.ca/programs/fitness-and-health-promotion',
'https://flemingcollege.ca/programs/food-and-nutrition-management',
'https://flemingcollege.ca/programs/forestry-technician',
'https://flemingcollege.ca/programs/general-arts-and-science-university-transfer',
'https://flemingcollege.ca/programs/geographic-information-systems-applications-specialist',
'https://flemingcollege.ca/programs/geographic-information-systems-applications-specialist-online',
'https://flemingcollege.ca/programs/geographic-information-systems-cartographic-specialist',
'https://flemingcollege.ca/programs/global-business-management',
'https://flemingcollege.ca/programs/graphic-design-visual-communication',
'https://flemingcollege.ca/programs/health-information-management',
'https://flemingcollege.ca/programs/health-safety-and-environmental-compliance',
'https://flemingcollege.ca/programs/heating-refrigeration-and-air-conditioning',
'https://flemingcollege.ca/programs/hospitality-hotel-and-restaurant-operations    ',
'https://flemingcollege.ca/programs/independent-studio-practice',
'https://flemingcollege.ca/programs/instrumentation-and-control-engineering-technician',
'https://flemingcollege.ca/programs/integrated-design',
'https://flemingcollege.ca/programs/international-business-management',
'https://flemingcollege.ca/programs/law-clerk',
'https://flemingcollege.ca/programs/massage-therapy',
'https://flemingcollege.ca/programs/mental-health-and-addiction-worker',
'https://flemingcollege.ca/programs/museum-management-and-curatorship',
'https://flemingcollege.ca/programs/occupational-therapist-assistant-and-physiotherapist-assistant',
'https://flemingcollege.ca/programs/office-administration-executive',
'https://flemingcollege.ca/programs/outdoor-and-adventure-education',
'https://flemingcollege.ca/programs/paralegal',
'https://flemingcollege.ca/programs/paramedic',
'https://flemingcollege.ca/programs/pharmacy-technician',
'https://flemingcollege.ca/programs/police-foundations',
'https://flemingcollege.ca/programs/police-foundations-advanced-standing',
'https://flemingcollege.ca/programs/practical-nursing',
'https://flemingcollege.ca/programs/project-management',
'https://flemingcollege.ca/programs/protection-security-and-investigation',
'https://flemingcollege.ca/programs/recreation-and-leisure-services',
'https://flemingcollege.ca/programs/recreation-and-leisure-services-advanced-standing',
'https://flemingcollege.ca/programs/resources-drilling-technician',
'https://flemingcollege.ca/programs/social-service-worker',
'https://flemingcollege.ca/programs/sporting-goods-business',
'https://flemingcollege.ca/programs/sustainable-agriculture-co-op',
'https://flemingcollege.ca/programs/sustainable-waste-management',
'https://flemingcollege.ca/programs/therapeutic-recreation',
'https://flemingcollege.ca/programs/tourism-global-travel',
'https://flemingcollege.ca/programs/tourism-global-travel-advanced-standing',
'https://flemingcollege.ca/programs/urban-forestry-technician-co-op',
'https://flemingcollege.ca/programs/visual-and-creative-arts-diploma',
'https://flemingcollege.ca/programs/welding-and-fabrication-technician',
'https://flemingcollege.ca/programs/wireless-information-networking']
    C= set(C)
    for i in C:
        start_urls.append(i)

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaCollegeItem)

        #1.school_name
        school_name = 'Fleming College'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.location
        location = 'Ontario, Canada'

        #4.major_name_en
        major_name_en = response.xpath('//*[@id="page-title"]/div/div/h2/text()').extract()[0]
        # print(major_name_en)

        #5.programme_code
        try:
            programme_code = response.xpath("//div[contains(text(),'Program code')]//following-sibling::*").extract()[0]
            programme_code = remove_tags(programme_code)
            programme_code = clear_space_str(programme_code)
        except:
            programme_code = None
        # print(programme_code)

        #6.degree_name #7.degree_level
        try:
            degree_name = response.xpath("//span[contains(text(),'Credential: ')]//following-sibling::strong").extract()[0]
            degree_name = remove_tags(degree_name)
        except:
            degree_name = ''
        if 'Graduate Certificate' in degree_name:
            degree_name = 'Graduate Certificate'
            degree_level = 2
        elif 'Advanced Diploma' in degree_name:
            degree_name = 'Advanced Diploma'
            degree_level = 3
        elif 'Diploma' in degree_name:
            degree_name = 'Diploma'
            degree_level = 3
        else:
            degree_name = None
            degree_level = None
        # print(degree_name)

        #8.duration #9.duration_per
        duration = response.xpath("//span[@class='program-credential-length']").extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        duration = re.findall('\d',duration)[0]
        duration_per = 2
        # print(duration)

        #10.start_date
        start_date = response.xpath('//*[@id="program-tabs"]/li/a').extract()
        start_date = ''.join(start_date)
        start_date = re.findall('>([a-zA-Z0-9\s]+)<',start_date)
        start_date =','.join(start_date).replace('September 2019','2019-09').replace('May 2019','2019-05').replace('January 2019','2019-01')
        # print(start_date)

        #11.campus
        try:
            campus = response.xpath("//div[contains(text(),'Offered at:')]//following-sibling::div/a").extract()[0]
            campus = ''.join(campus)
            campus = remove_tags(campus)
        except:
            campus = None
        # print(campus)

        #12.overview_en
        overview_en = response.xpath("//h3[contains(text(),'Program Highlights')]//following-sibling::*").extract()
        overview_en = ''.join(overview_en)
        end = overview_en.find('<h3')
        overview_en = overview_en[:end]
        overview_en = remove_class(overview_en)
        # print(overview_en)
        # print(url)

        #13.career_en
        career_en = response.xpath("//h3[contains(text(),'Career Opportunities')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        end = career_en.find('<h3')
        career_en = career_en[:end]
        career_en = remove_class(career_en)
        # print(career_en)
        # print(url)

        #14.entry_requirements_en
        entry_requirements_en = response.xpath("//h3[contains(text(),'Minimum Admission Requirements')]//following-sibling::*").extract()
        entry_requirements_en = ''.join(entry_requirements_en)
        end = entry_requirements_en.find('<div')
        entry_requirements_en = entry_requirements_en[:end]
        entry_requirements_en = remove_class(entry_requirements_en)
        # print(entry_requirements_en)
        # print(url)

        #15.modules_en
        modules_en_url = response.xpath("//a[@class='icon icon-list']//@href").extract()[0]
        modules_en_url = 'https://flemingcollege.ca' + modules_en_url
        # print(modules_en_url)
        if len(modules_en_url) != 0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data2 = requests.get(modules_en_url, headers=headers)
            response2 = etree.HTML(data2.text)
            modules_en = response2.xpath('//*[@id="content"]/div[2]')
            doc2 = ""
            if len(modules_en) > 0:
                for a in modules_en:
                    doc2 += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc2 = remove_class(doc2)
                    modules_en = doc2
            else:
                modules_en = None
        else:
            modules_en = None
            # print(modules_en)
        # print(modules_en)

        #16.other
        other = '1.缺少deadline，2.页面详情页没有学院,3.部分专业没有学费，4.'

        #17.tuition_fee
        tuition_fee = response.xpath("//span[contains(text(),'International:')]/../following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        try:
            tuition_fee = re.findall('\$([0-9,\.]+)',tuition_fee)[0]
        except:
            tuition_fee = None
        # print(tuition_fee,url)

        #18.tuition_fee_pre
        tuition_fee_pre = '$'

        #19.apply_pre
        apply_pre = '$'

        #20.apply_fee
        apply_fee = '95'

        #21.ielts 22232425
        ielts = 6.0
        ielts_r = 5.5
        ielts_w = 5.5
        ielts_s = 5.5
        ielts_l = 5.5

        #26.toefl
        toefl = 65

        item['school_name'] = school_name
        item['url'] = url
        item['location'] = location
        item['major_name_en'] = major_name_en
        item['programme_code'] = programme_code
        item['degree_name'] = degree_name
        item['degree_level'] = degree_level
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['start_date'] = start_date
        item['campus'] = campus
        item['overview_en'] = overview_en
        item['career_en'] = career_en
        item['entry_requirements_en'] = entry_requirements_en
        item['modules_en'] = modules_en
        item['other'] = other
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_pre'] = apply_pre
        item['apply_fee'] = apply_fee
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl'] = toefl
        # yield  item