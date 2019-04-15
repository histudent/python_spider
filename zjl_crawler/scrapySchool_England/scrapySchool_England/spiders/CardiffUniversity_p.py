# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/9 10:54'
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
class CardiffUniversitySpider(scrapy.Spider):
    name = 'CardiffUniversity_p'
    allowed_domains = ['cardiff.ac.uk/']
    start_urls = []
    C= [
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/social-science-research-methods-politics-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/applied-environmental-geology',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/msc-building-and-infrastructure-information-modelling-bim-for-smart-engineering',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/care-of-collections-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/theology-mth',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/city-futures-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/social-science-research-methods-psychology-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/international-commercial-law-llm',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/sustainable-energy-and-environment-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/history-and-archaeology-of-the-greek-And-roman-world-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/business-administration-mba',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/advanced-practice-msc-community-health',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/welsh-government-and-politics-msc-econ',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/computing-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/public-health-mph',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/medieval-british-studies-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/physiotherapy-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/social-science-research-methods-social-work-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/data-science-and-analytics-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/advanced-chemistry-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/urban-and-regional-development-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/social-science-research-methods-criminology-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/financial-economics-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/english-literature-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/islam-in-contemporary-britain-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/intellectual-property-law-llm',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/journalism,-media-and-communications-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/social-care-law-llm',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/tissue-engineering-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/data-intensive-astrophysics-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/spatial-planning-and-development-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/late-antique-and-byzantine-studies-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/archaeology-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/urban-design-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/civil-engineering-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/managing-care-in-perioperative-and-anaesthesia-practice-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/clinical-dermatology-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/astrophysics-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/social-work-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/international-relations-msc-econ',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/oral-biology-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/clinical-optometry-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/environmental-design-of-buildings-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/civil-and-geoenvironmental-engineering-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/information-security-and-privacy-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/crime,-safety-and-justice-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/structural-engineering-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/conservation-practice-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/social-science-research-methods-international-relations-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/computational-and-data-journalism-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/science-communication-msc-full-time',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/international-planning-and-urban-design-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/msc-compound-semiconductor-physics',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/advanced-practice-education-for-health-professionals-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/childrens-psychological-disorders-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/communication-technology-and-entrepreneurship-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/strategic-marketing-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/computing-and-it-management-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/ancient-history-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/finance-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/accounting-and-finance-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/ageing-health-and-disease-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/physics-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/environment-and-development-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/international-human-resource-management-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/forensic-linguistics-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/magazine-journalism-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/bioinformatics-and-genetic-epidemiology-msc-full-time',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/political-communication-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/religious-studies-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/digital-media-and-society-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/international-economics,-banking-and-finance-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/maritime-policy-and-shipping-management-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/advanced-practice-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/wireless-and-microwave-communication-engineering-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/sport-and-exercise-physiotherapy-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/social-science-research-methods-business-and-management-studies-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/politics-and-public-policy-msc-econ',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/building-diagnostics-for-energy-and-environmental-performance-msc-full-time',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/sustainable-building-conservation-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/cancer-biology-and-therapeutics-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/cultural-and-creative-industries-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/sustainable-supply-chain-management-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/transport-and-planning-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/international-public-relations-and-global-communications-management-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/social-science-research-methods-social-policy-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/broadcast-journalism-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/early-celtic-studies-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/ancient-and-medieval-warfare-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/international-planning-and-development-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/language-and-communication-research-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/music-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/welsh-history-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/neuroimaging-methods-And-applications-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/law-llm',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/legal-and-political-aspects-of-international-affairs-llm',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/manufacturing-engineering,-innovation-and-management-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/occupational-therapy-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/social-science-research-methods-environmental-planning-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/software-engineering',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/welsh-and-celtic-studiesastudiaethau-cymreig-a-cheltaidd-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/applied-linguistics-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/childhood-and-youth-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/radiography-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/social-science-research-methods-science-and-technology-studies-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/sustainability,-planning-and-environmental-policy-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/media-management-mba',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/news-journalism-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/international-management-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/social-science-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/human-rights-law-llm',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/shipping-law-llm',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/master-of-clinical-dentistry-endodontology',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/translation-studies-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/professional-conservation-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/eco-cities-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/operational-research-and-applied-statistics-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/bioinformatics-msc-full-time',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/msc-compound-semiconductor-electronics',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/social-and-public-policy-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/archaeological-science-msc-full-time',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/international-journalism-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/mathematics-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/operational-research,-applied-statistics-and-financial-risk-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/advanced-mechanical-engineering-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/civil-and-water-engineering-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/human-resource-management-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/sustainable-mega-buildings-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/logistics-and-operations-management-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/history-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/medical-education-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/creative-writing-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/medicinal-chemistry-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/catalysis-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/architectural-design-ma',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/advanced-computer-science-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/electrical-energy-systems-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/education,-policy-and-society-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/master-of-design-administration',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/orthodontics-mscd',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/data-intensive-physics-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/bar-professional-training-course-llm',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/global-culture-and-creativity',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/governance-and-devolution-llm',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/biological-chemistry-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/business-strategy-And-entrepreneurship-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/social-science-research-methods-education-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/social-science-research-methods-sociology-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/social-science-research-methods-socio-legal-studies-msc',
        'https://www.cardiff.ac.uk/study/postgraduate/taught/courses/course/european-legal-studies-llm'
    ]

    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Cardiff University'
        # print(university)

        #2.url
        url = response.url

        #3.programme_en
        programme_en = response.xpath('//*[@id="content"]/div[1]/div/div[1]/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        if '(' in programme_en:
            programme_en = programme_en.split()[:-1]
            programme_en = ' '.join(programme_en)
        # print(programme_en)

        #4.overview_en
        overview_en = response.xpath('//*[@id="content"]/div[1]/div/div[1]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #5.start_date
        start_date = '2018-9'

        #6.duration #7.duration_per
        duration_list = response.xpath("//*[contains(text(),'Duration')]//following-sibling::*").extract()
        duration_list  = ''.join(duration_list)
        duration_list  = remove_tags(duration_list)
        try:
            duration_a = re.findall('\d+',duration_list)[0]
        except:
            duration_a = 1
        if 'five years' in duration_list:
            duration = 5
        elif 'seven years' in duration_list:
            duration = 7
        else:
            duration = duration_a
        if 'months' in duration_list:
            duration_per = 3
        else:
            duration_per = 1
        # print(duration,'********',duration_per)

        #8.degree_name
        degree_name = response.xpath("//*[contains(text(),'Qualification')]//following-sibling::*[1]").extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        if len(degree_name)> 30:
            degree_name = 'N/A'

        # print(degree_name)

        #9.teach_time
        teach_time = response.xpath("//*[contains(text(),'Mode')]//following-sibling::*").extract()
        teach_time = ''.join(teach_time)
        teach_time = remove_tags(teach_time)
        if 'Full-time' in teach_time:
            teach_time = 'Full-time'
        elif len(teach_time) ==0:
            teach_time = 'Full-time'
        else:
            teach_time = 'Part-time'
        # print(teach_time)

        #10.modules_en
        modules_en = response.xpath('//*[@id="section2"]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #11.teach_type
        if 'taught' in response.url:
            teach_type = 'taught'
        else:
            teach_type = 'research'
        # print(teach_type)

        #12.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'How will I be assessed?')]//following-sibling::p[position()<3]").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #13.career_en
        career_en = response.xpath('//*[@id="section5"]/div[1]/div[1]/p').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #14.tuition_fee
        tuition_fee = response.xpath('//*[@id="tuitionfees"]/table/tbody/tr/td[1]').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #15.rntry_requirements
        rntry_requirements = response.xpath("//*[contains(text(),'Admissions criteria')]//following-sibling::*").extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_tags(rntry_requirements)
        # print(rntry_requirements)

        #16.tuition_fee_pre
        tuition_fee_pre = '£'

        #17 18192021
        ielts = 6.5
        ielts_s = 5.5
        ielts_l = 5.5
        ielts_w = 5.5
        ielts_r = 5.5

        #22.degree_type
        degree_type = 2

        item['degree_name'] = degree_name
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['overview_en'] = overview_en
        item['start_date'] = start_date
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['degree_type'] = degree_type
        item['teach_time'] = teach_time
        item['modules_en'] = modules_en
        item['teach_type'] = teach_type
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['rntry_requirements'] = rntry_requirements
        item['tuition_fee_pre'] = tuition_fee_pre
        item['ielts'] = ielts
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        yield  item