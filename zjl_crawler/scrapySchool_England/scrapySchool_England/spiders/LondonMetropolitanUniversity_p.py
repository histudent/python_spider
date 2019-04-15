# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/4 16:55'
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

class LondonMetropolitanUniversitySpider(scrapy.Spider):
    name = 'LondonMetropolitanUniversity_p'
    allowed_domains = ['londonmet.ac.uk/']
    start_urls = []
    C = [
        'https://www.londonmet.ac.uk/courses/postgraduate/marketing---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/criminology---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/food-science---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/psychology---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/public-health---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/architecture---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/interpreting---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/education---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/criminology---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/marketing---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/interpreting---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/education---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/psychology---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/architecture---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/product-design---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/textile-design---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/product-design---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/cancer-pharmacology---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/public-health---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/food-science---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/conference-interpreting---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/biomedical-science---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/textile-design---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/cancer-immunotherapy---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/ma-by-project---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/architecture-and-urbanism---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/llm-legal-practice---llm/',
        'https://www.londonmet.ac.uk/courses/postgraduate/dietetics-and-nutrition---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/international-relations---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/woman-and-child-abuse---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/teaching-languages-english---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/teaching-languages-arabic---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/early-childhood-studies---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/master-of-fine-arts---mfa/',
        'https://www.londonmet.ac.uk/courses/postgraduate/media-and-entertainment-law---llm/',
        'https://www.londonmet.ac.uk/courses/postgraduate/psychology-of-mental-health---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/digital-media---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/design-for-cultural-commons---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/data-analytics---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/medical-genomics---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/human-resource-management---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/social-work---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/crime-violence-and-prevention---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/master-of-business-administration---mba/',
        'https://www.londonmet.ac.uk/courses/postgraduate/psychology---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/translation---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/sports-therapy---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/international-trade-and-finance---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/internet-of-things-and-digital-enterprise---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/architecture-and-urbanism---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/organised-crime-and-global-security---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/computer-networking-and-cyber-security---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/human-rights-and-international-conflict---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/human-nutrition-public-health--sports---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/creative-digital-and-professional-writing---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/master-of-public-administration-mpa---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/international-oil-gas-and-energy-law---llm/',
        'https://www.londonmet.ac.uk/courses/postgraduate/master-of-philosophy---mphil/',
        'https://www.londonmet.ac.uk/courses/postgraduate/doctor-of-philosophy---mphil--phd/',
        'https://www.londonmet.ac.uk/courses/postgraduate/aviation-management-for-the-21st-century---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/learning-and-teaching-in-higher-education---ma/',
        'https://www.londonmet.ac.uk/courses/postgraduate/master-of-business-administration-islamic-finance---mba/',
        'https://www.londonmet.ac.uk/courses/postgraduate/internet-of-things-and-digital-enterprise---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/master-of-business-administration-cyber-security---mba/',
        'https://www.londonmet.ac.uk/courses/postgraduate/corporate-social-responsibility-and-sustainability---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/master-of-business-administration-data-analytics---mba/',
        'https://www.londonmet.ac.uk/courses/postgraduate/health-and-social-care-management-and-policy---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/pharmaceutical-science-and-drug-delivery-systems---msc/',
        'https://www.londonmet.ac.uk/courses/postgraduate/master-of-business-administration-life-sciences---mba/',
        'https://www.londonmet.ac.uk/courses/postgraduate/financial-services-law-regulation-and-compliance---llm/',
        'https://www.londonmet.ac.uk/courses/postgraduate/computer-networking-and-cyber-security-with-work-experience---msc/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'London Metropolitan University'
        # print(university)

        # 2.url
        url = response.url

        #3.programme_en
        programme_en = response.xpath('/html/body/div[1]/div/h1/span').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en).strip()
        # print(programme_en,url)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        try:
            degree_name =re.findall(r'-\s[A-Za-z\s/]+$',programme_en)[0]
        except:
            degree_name = ''
        programme_en = programme_en.replace(degree_name,'').strip()
        degree_name = degree_name.replace('-','').strip()
        # print(degree_name)

        #6.overview_en
        overview_en = response.xpath('//*[@id="why-study-this-course"]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #7.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'Assessment')]//following-sibling::*").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = clear_space_str(assessment_en)
        # print(assessment_en)

        #8.modules_en
        modules_en = response.xpath('//*[@id="modular-structure"]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en).replace('▼','')
        # print(modules_en)

        #9.career_en
        career_en = response.xpath('//*[@id="after-the-course"]').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #10.ielts 11121314
        if 'Education' in programme_en:
            ielts = 6.5
            ielts_w = 6.0
            ielts_r = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
        elif 'Creative, Digital and Professional Writing' in programme_en:
            ielts = 6.5
            ielts_w = 6.0
            ielts_r = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
        elif 'Interpreting' in programme_en:
            ielts = 6.5
            ielts_w = 6.0
            ielts_r = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
        elif 'LLM' in programme_en:
            ielts = 6.5
            ielts_w = 6.0
            ielts_r = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
        elif 'Psychology' in programme_en:
            ielts = 6.5
            ielts_w = 6.0
            ielts_r = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
        elif 'Teaching Languages (English) - MA' in programme_en:
            ielts = 6.5
            ielts_w = 6.0
            ielts_r = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
        elif 'Biomedical Science - MSc' in programme_en:
            ielts = 7.0
            ielts_w = 6.5
            ielts_r = 6.5
            ielts_s = 6.5
            ielts_l = 6.5
        elif 'Blood Science (Distance Learning) - MSc' in programme_en:
            ielts = 7.0
            ielts_w = 6.5
            ielts_r = 6.5
            ielts_s = 6.5
            ielts_l = 6.5
        elif 'Common Professional Exam' in programme_en:
            ielts = 7.0
            ielts_w = 6.5
            ielts_r = 6.5
            ielts_s = 6.5
            ielts_l = 6.5
        elif 'Legal Practice Course' in programme_en:
            ielts = 7.0
            ielts_w = 6.5
            ielts_r = 6.5
            ielts_s = 6.5
            ielts_l = 6.5
        else:
            ielts = 6.0
            ielts_w = 5.5
            ielts_r = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
        # print(ielts,ielts_l,ielts_r,ielts_s,ielts_w)

        #15.tuition_fee
        tuition_fee = response.xpath("//optgroup[@label='International']/option[1]/@data-cost").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #16.duration 17.duration_per
        duration_list = response.xpath("//optgroup[@label='International']/option[1]/@data-duration").extract()
        duration_list = ''.join(duration_list)
        if len(duration_list) !=0:
            duration = re.findall('\d+',duration_list)[0]
            if 'months' in duration_list:
                duration_per = 3
            elif 'year' in duration_list:
                duration_per = 1
            elif 'weeks' in duration_list:
                duration_per = 4
            else:
                duration_per = None
        else:
            duration = None
            duration_per = None
        # print(duration,"*************",duration_per)

        #18.tuition_fee_pre
        tuition_fee_pre = '£'

        #19.teach_time
        teach_time = 'Full time'

        #20.location
        location = 'London'
        #21.apply_pre
        apply_pre = '£'
        #22.rntry_requirements
        rntry_requirements = response.xpath('//*[@id="entry-requirements"]').extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #23.require_chinese_en
        require_chinese_en = "<p>A completed bachelor's degree from a high ranking Chinese institution Grade: 70% or above</p>"

        item['require_chinese_en'] = require_chinese_en
        item['rntry_requirements'] = rntry_requirements
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['assessment_en'] = assessment_en
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['teach_time'] = teach_time
        item['location'] = location
        yield  item