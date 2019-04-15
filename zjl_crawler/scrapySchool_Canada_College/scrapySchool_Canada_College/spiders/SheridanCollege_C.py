# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/12/20 14:18'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.getItem import get_item
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from lxml import etree
import requests
class SheridanCollege_CSpider(scrapy.Spider):
    name = 'SheridanCollege_C'
    allowed_domains = ['sheridancollege.ca/']
    start_urls = []
    C= [
        'https://academics.sheridancollege.ca/programs/bachelor-of-business-administration-accounting',
        'https://academics.sheridancollege.ca/programs/bachelor-of-animation',
        'https://academics.sheridancollege.ca/programs/bachelor-of-applied-health-sciences-athletic-therapy',
        'https://academics.sheridancollege.ca/programs/bachelor-of-craft-and-design-ceramics',
        'https://academics.sheridancollege.ca/programs/community-safety',
        'https://academics.sheridancollege.ca/programs/creative-writing-and-publishing',
        'https://academics.sheridancollege.ca/programs/bachelor-of-early-childhood-leadership',
        'https://academics.sheridancollege.ca/programs/bachelor-of-film-and-television',
        'https://academics.sheridancollege.ca/programs/bachelor-of-business-administration-finance',
        'https://academics.sheridancollege.ca/programs/bachelor-of-craft-and-design-furniture',
        'https://academics.sheridancollege.ca/programs/bachelor-of-game-design',
        'https://academics.sheridancollege.ca/programs/bachelor-of-craft-and-design-glass',
        'https://academics.sheridancollege.ca/programs/bachelor-of-business-administration-human-resources-management',
        'https://academics.sheridancollege.ca/programs/bachelor-of-illustration',
        'https://academics.sheridancollege.ca/programs/bachelor-of-craft-and-design-industrial-design',
        'https://academics.sheridancollege.ca/programs/bachelor-of-applied-information-sciences-information-systems-security',
        'https://academics.sheridancollege.ca/programs/bachelor-of-interaction-design',
        'https://academics.sheridancollege.ca/programs/bachelor-of-interior-design',
        'https://academics.sheridancollege.ca/programs/bachelor-of-health-sciences-kinesiology-and-health-promotion',
        'https://academics.sheridancollege.ca/programs/bachelor-of-business-administration-marketing-management',
        'https://academics.sheridancollege.ca/programs/bachelor-of-applied-computer-science-mobile-computing',
        'https://academics.sheridancollege.ca/programs/bachelor-of-music-theatre-performance',
        'https://academics.sheridancollege.ca/programs/bachelor-of-photography',
        'https://academics.sheridancollege.ca/programs/bachelor-of-business-administration-supply-chain-management',
        'https://academics.sheridancollege.ca/programs/bachelor-of-craft-and-design-textiles',
        'https://academics.sheridancollege.ca/programs/bachelor-of-design',
        'https://academics.sheridancollege.ca/programs/business-administration-accounting',
        'https://academics.sheridancollege.ca/programs/advertising-and-marketing-communications-management',
        'https://academics.sheridancollege.ca/programs/architectural-technician-technology',
        'https://academics.sheridancollege.ca/programs/business-general',
        'https://academics.sheridancollege.ca/programs/chemical-laboratory-technician',
        'https://academics.sheridancollege.ca/programs/community-and-justice-services',
        'https://academics.sheridancollege.ca/programs/community-worker-outreach-and-development',
        'https://academics.sheridancollege.ca/programs/computer-engineering-technician-technology',
        'https://academics.sheridancollege.ca/programs/computer-programmer',
        'https://academics.sheridancollege.ca/programs/computer-systems-technician-software-engineering',
        'https://academics.sheridancollege.ca/programs/early-childhood-education',
        'https://academics.sheridancollege.ca/programs/early-childhood-education-intensive',
        'https://academics.sheridancollege.ca/programs/educational-support',
        'https://academics.sheridancollege.ca/programs/educational-support-fast-track-intensive',
        'https://academics.sheridancollege.ca/programs/electrical-engineering-technician',
        'https://academics.sheridancollege.ca/programs/electromechanical-engineering-technician-technology',
        'https://academics.sheridancollege.ca/programs/electronics-engineering-technician-technology',
        'https://academics.sheridancollege.ca/programs/environmental-technician',
        'https://academics.sheridancollege.ca/programs/business-administration-finance',
        'https://academics.sheridancollege.ca/programs/general-arts-and-science-university-profile',
        'https://academics.sheridancollege.ca/programs/business-administration-human-resources',
        'https://academics.sheridancollege.ca/programs/information-technologies-support-services',
        'https://academics.sheridancollege.ca/programs/interior-decorating',
        'https://academics.sheridancollege.ca/programs/investigation-public-and-private',
        'https://academics.sheridancollege.ca/programs/journalism',
        'https://academics.sheridancollege.ca/programs/makeup-for-media-and-creative-arts',
        'https://academics.sheridancollege.ca/programs/business-administration-marketing',
        'https://academics.sheridancollege.ca/programs/mechanical-engineering-technician-technology',
        'https://academics.sheridancollege.ca/programs/mechanical-engineering-technician-technology-design-and-drafting',
        'https://academics.sheridancollege.ca/programs/office-administration-executive',
        'https://academics.sheridancollege.ca/programs/office-administration-health-services',
        'https://academics.sheridancollege.ca/programs/office-administration-legal',
        'https://academics.sheridancollege.ca/programs/paralegal',
        'https://academics.sheridancollege.ca/programs/pharmacy-technician',
        'https://academics.sheridancollege.ca/programs/plumbing-technician',
        'https://academics.sheridancollege.ca/programs/police-foundations',
        'https://academics.sheridancollege.ca/programs/practical-nursing',
        'https://academics.sheridancollege.ca/programs/social-service-worker',
        'https://academics.sheridancollege.ca/programs/social-service-worker-gerontology',
        'https://academics.sheridancollege.ca/programs/theatre-and-drama-studies',
        'https://academics.sheridancollege.ca/programs/mechanical-technician-tool-making',
        'https://academics.sheridancollege.ca/programs/veterinary-technician',
        'https://academics.sheridancollege.ca/programs/visual-and-creative-arts',
        'https://academics.sheridancollege.ca/programs/visual-merchandising-arts',
        'https://academics.sheridancollege.ca/programs/welding-techniques',
        'https://academics.sheridancollege.ca/programs/art-and-art-history',
        'https://academics.sheridancollege.ca/programs/bachelor-of-computing-and-network-communications-honours-internet-communications-technology',
        'https://academics.sheridancollege.ca/programs/chemical-engineering-technology',
        'https://academics.sheridancollege.ca/programs/chemical-engineering-technology-environmental',
        'https://academics.sheridancollege.ca/programs/child-and-youth-care',
        'https://academics.sheridancollege.ca/programs/computer-systems-technology-software-development-and-network-engineering',
        'https://academics.sheridancollege.ca/programs/computer-systems-technology-systems-analyst',
        'https://academics.sheridancollege.ca/programs/internet-communications-technology',
        'https://academics.sheridancollege.ca/programs/technical-production-for-theatre-and-live-events',
        'https://academics.sheridancollege.ca/programs/manufacturing-management',
        'https://academics.sheridancollege.ca/programs/advanced-special-effects-makeup-prosthetics-and-props',
        'https://academics.sheridancollege.ca/programs/advanced-television-and-film',
        'https://academics.sheridancollege.ca/programs/advertising-account-management',
        'https://academics.sheridancollege.ca/programs/business-process-management',
        'https://academics.sheridancollege.ca/programs/computer-animation',
        'https://academics.sheridancollege.ca/programs/creative-industries-management',
        'https://academics.sheridancollege.ca/programs/digital-creature-animation-technical-direction',
        'https://academics.sheridancollege.ca/programs/environmental-control',
        'https://academics.sheridancollege.ca/programs/game-development-advanced-programming',
        'https://academics.sheridancollege.ca/programs/game-level-design',
        'https://academics.sheridancollege.ca/programs/human-resources-management',
        'https://academics.sheridancollege.ca/programs/interactive-media-management',
        'https://academics.sheridancollege.ca/programs/international-business-management',
        'https://academics.sheridancollege.ca/programs/journalism-new-media',
        'https://academics.sheridancollege.ca/programs/marketing-management',
        'https://academics.sheridancollege.ca/programs/music-applied-to-stage-screen-and-interactive-visual-environments',
        'https://academics.sheridancollege.ca/programs/professional-accounting',
        'https://academics.sheridancollege.ca/programs/project-management',
        'https://academics.sheridancollege.ca/programs/public-relations-corporate-communications',
        'https://academics.sheridancollege.ca/programs/quality-assurance-manufacturing-and-management',
        'https://academics.sheridancollege.ca/programs/teaching-english-to-speakers-of-other-languages',
        'https://academics.sheridancollege.ca/programs/visual-effects',
        'https://academics.sheridancollege.ca/programs/web-design'
    ]

    for i in C:
        start_urls.append(i)

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaCollegeItem)

        #1.school_name
        school_name = 'Sheridan College'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.location
        location = 'Ontario, Canada'

        #4.major_name_en
        major_name_en = response.xpath('//*[@id="main"]/article/header[1]/div/div/div/div[1]/h1').extract()
        major_name_en = ''.join(major_name_en)
        major_name_en = remove_tags(major_name_en)
        # print(major_name_en)

        #5.programme_code
        try:
            programme_code = response.xpath("//li[contains(text(),'Program code: ')]//b").extract()[0]
            programme_code  = ''.join(programme_code)
            programme_code = remove_tags(programme_code)
        except:
            programme_code = None
        # print(programme_code,url)

        #6.department
        department = response.xpath('//*[@id="main"]/article/header[1]/div/div/div/div[1]/div[2]').extract()
        department = ''.join(department)
        department = remove_tags(department).replace('&amp; ','')
        # print(department)

        #7.degree_name 8.degree_level
        try:
            degree_name = response.xpath("//div[contains(@class,'plan-offering-header')]//h4").extract()[0]
            degree_name = ''.join(degree_name)
            degree_name = remove_tags(degree_name)
        except:
            degree_name = ''
        if 'Advanced Diploma' in degree_name:
            degree_name = 'Advanced Diploma'
            degree_level  = 3
        elif 'Diploma' in degree_name:
            degree_name = 'Diploma'
            degree_level = 3
        elif 'Graduate Certificate' in degree_name:
            degree_name = 'Graduate Certificate'
            degree_level = 2
        elif 'Degree' in degree_name:
            degree_name = degree_name
            degree_level = 1
        else:
            degree_name = None
            degree_level = None
        # print(degree_name,url)

        #9.duration #10.duration_per
        duration = response.xpath("//div[contains(@class,'plan-offering-header')]//ul//li[2]").extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        try:
            duration = re.findall('\d',duration)[0]
        except:
            duration = None
        duration_per = 1
        # print(duration,url)


        #11.tuition_fee
        tuition_fee = '14,832'

        #12.tuition_fee_pre
        tuition_fee_pre = '$'

        #13.start_date
        start_date = response.xpath('//figure/table//tr/td[1]').extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        start_date = re.findall('([a-zA-Z]+\s\d+)',start_date)
        start_date = set(start_date)
        start_date = ','.join(start_date).replace('Jan 2019','2019-01').replace('May 2019','2019-05').replace('Sep 2019','2019-09').replace('Jan 2020','2020-01')
        start_date = start_date.replace('May 2020','2020-05')
        # print(start_date)

        #14.campus
        try:
            campus = response.xpath('//figure/table//tr/td[2]').extract()[0]
            campus = re.findall('<span>(.*?)</span>',campus)
            campus = ','.join(campus)
        except:
            campus = None
        # print(campus)

        #15.overview_en
        overview_en = response.xpath('//*[@id="main"]/article/div[1]/div/div[2]').extract()
        overview_en =''.join(overview_en)
        overview_en = remove_class(overview_en).replace('Program Summary (PDF)','')
        # print(overview_en)

        #16.modules_en
        modules_en_url = url + '/courses/'
        # print(modules_en_url)
        if len(modules_en_url) != 0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data2 = requests.get(modules_en_url, headers=headers)
            response2 = etree.HTML(data2.text)
            modules_en = response2.xpath('//*[@id="main"]/article/div[1]/div/div[2]/div/div')
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

        #17.career_en
        career_en_url = url + '/career-opportunities'
        # print(modules_en_url)
        if len(career_en_url) != 0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data3 = requests.get(career_en_url, headers=headers)
            response3 = etree.HTML(data3.text)
            career_en = response3.xpath('//*[@id="main"]/article/div[1]/div/div[2]/div/div')
            doc3 = ""
            if len(career_en) > 0:
                for a in career_en:
                    doc3 += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc3 = remove_class(doc3)
                    career_en = doc3
            else:
                career_en = None
        else:
            career_en = None
        # print(career_en)

        #18.entry_requirements_en
        entry_requirements_en_url = url + '/admission-requirements'
        # print(entry_requirements_en)
        if len(entry_requirements_en_url) != 0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data = requests.get(entry_requirements_en_url, headers=headers)
            response1 = etree.HTML(data.text)
            entry_requirements_en = response1.xpath('//*[@id="main"]/article/div[1]/div/div[2]/div/div')
            doc = ""
            if len(entry_requirements_en) > 0:
                for a in entry_requirements_en:
                    doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc = remove_class(doc)
                    entry_requirements_en = doc
            else:
                entry_requirements_en = None
        else:
            entry_requirements_en = None
        # print(entry_requirements_en)

        #19.toefl 20212223
        if degree_level ==3:
            toefl = 80
            toefl_r = 20
            toefl_w = 20
            toefl_s = 20
            toefl_l = 20
        else:
            toefl = 88
            toefl_r = 21
            toefl_w = 21
            toefl_s = 21
            toefl_l = 21

        #24.ielts 25262728
        if degree_level ==3:
            ielts = 6
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        else:
            ielts = 6.5
            ielts_r = 6
            ielts_w = 6
            ielts_l = 6
            ielts_s = 6

        #29.other
        other = 'other 1.部分专业没有学位名称2.duration部分官网页面上没有3.deadline未找到 4.申请费未找到'

        item['school_name'] = school_name
        item['url'] = url
        item['location'] = location
        item['major_name_en'] = major_name_en
        item['programme_code'] = programme_code
        item['department'] = department
        item['degree_name'] = degree_name
        item['degree_level'] = degree_level
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['start_date'] = start_date
        item['campus'] = campus
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['entry_requirements_en'] = entry_requirements_en
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['other'] = other
        yield item










