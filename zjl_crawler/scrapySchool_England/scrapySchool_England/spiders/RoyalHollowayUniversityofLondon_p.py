# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/6/29 13:51'
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
class RoyalHollowayUniversityofLondonSpider(scrapy.Spider):
    name = 'RoyalHollowayUniversityofLondon_p'
    allowed_domains = ['royalholloway.ac.uk/']
    start_urls = []
    C= [
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/psychology/applied-social-psychology',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/classics/classical-art-and-archaeology',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/music/advanced-musical-studies',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/management/accounting-and-financial-management',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/classics/classics',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/classics/ancient-history',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/modern-languages-literatures-and-cultures/comparative-literature-and-culture',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/psychology/clinical-psychology',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/biological-sciences/biological-sciences',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/classics/classical-reception',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/management/consumption-culture-and-marketing-part-time',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/management/consumption-culture-and-marketing',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/computational-finance-with-a-year-in-industry',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/computational-finance',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/management/business-information-systems',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/drama-theatre-and-dance/contemporary-performance-practices',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/history/crusader-studies',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/english/creative-writing',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/data-science-and-analytics-with-a-year-in-industry',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/distributed-and-networked-systems',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/management/digital-innovation-and-analytics',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/media-arts/documentary-by-practice',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/economics/economics-2-year-course',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/politics-and-international-relations/elections-campaigns-and-democracy',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/distributed-and-networked-systems-with-a-year-in-industry',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/electronic-engineering/electronic-engineering',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/data-science-and-analytics',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/professional-studies/engineering-management',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/english/english-literature',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/management/entrepreneurship-and-innovation-with-a-year-in-business',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/earth-sciences/environmental-diagnosis-and-management',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/economics/finance',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/economics/finance-2-year-course',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/media-arts/film-television-and-digital-production',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/philosophy/european-philosophy',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/modern-languages-literatures-and-cultures/french-studies',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/history/hellenic-studies',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/modern-languages-literatures-and-cultures/german-studies',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/geography/geopolitics-and-security',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/modern-languages-literatures-and-cultures/hispanic-studies',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/management/entrepreneurship-and-innovation',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/history/holocaust-studies',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/history/history',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/economics/economics',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/management/international-management',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/information-security/information-security',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/management/international-management-mba',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/management/international-management-marketing',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/politics-and-international-relations/international-security',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/information-security/information-security-with-a-year-in-industry',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/management/human-resource-management',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/politics-and-international-relations/international-public-policy',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/politics-and-international-relations/islamic-and-west-asian-studies',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/media-arts/international-television-industries',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/politics-and-international-relations/international-relations',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/history/late-antique-and-byzantine-studies',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/modern-languages-literatures-and-cultures/italian-studies',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/machine-learning',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/mathematics/mathematics-for-applications',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/management/international-supply-chain-management/',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/machine-learning-with-a-year-in-industry',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/media-arts/media-management',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/management/marketing',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/english/medieval-studies',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/philosophy/modern-philosophy',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/earth-sciences/petroleum-geoscience',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/music/music-performance',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/mathematics/mathematics-of-cryptography-and-communications',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/earth-sciences/petroleum-geoscience-by-distance-learning',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/politics-and-international-relations/media-power-and-public-affairs',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/drama-theatre-and-dance/playwriting',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/physics/physics-euromasters-2-year-course',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/politics-and-international-relations/politics-of-development',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/history/public-history',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/media-arts/producing-film-and-television',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/geography/quaternary-science',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/english/shakespeare',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/media-arts/screenwriting-for-television-and-film-in-retreat',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/professional-studies/project-management',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/geography/sustainability-and-management',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/english/victorian-literature-art-and-culture',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/the-internet-of-things-with-a-year-in-industry',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/computer-science/the-internet-of-things',
        # 'https://www.royalholloway.ac.uk/studying-here/postgraduate/drama-theatre-and-dance/theatre-directing'
        'https://www.royalholloway.ac.uk/studying-here/postgraduate/geography/cultural-geography/',
        'https://www.royalholloway.ac.uk/studying-here/postgraduate/law/forensic-psychology/',
        'https://www.royalholloway.ac.uk/studying-here/postgraduate/management/international-management-mba-with-a-year-in-business/',
        'https://www.royalholloway.ac.uk/studying-here/postgraduate/media-arts/producing-film-and-television/',
        'https://www.royalholloway.ac.uk/studying-here/postgraduate/law/social-work/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Royal Holloway University of London'
        # print(university)

        #2.department
        try:
            department = response.xpath('//*[@id="main"]/aside/div[2]/a/div[2]/span[2]').extract()
            department = ''.join(department)
            department = remove_tags(department)
            # print(department)
        except:
            department = 'N/A'

        #3.location
        location = 'London'

        #4.degree_type
        degree_type = 2

        #5.degree_name
        try:
            degree_name = response.xpath('/html/body/div[1]/main/div[1]/div/div/div/span').extract()
            degree_name = ''.join(degree_name)
            degree_name = remove_tags(degree_name)
        except:
            degree_name = 'N/A'
        # print(degree_name)

        #6.programme_en
        try:
            programme_en = response.xpath('/html/body/div[1]/main/div[1]/div/div/div/h2').extract()
            programme_en = ''.join(programme_en)
            programme_en = remove_tags(programme_en)
            programme_en = clear_space_str(programme_en)
        except:
            programme_en = ''
        # print(programme_en)

        #7.overview_en
        try:
            overview_en = response.xpath('//*[@id="main"]/article/p[1]').extract()
            overview_en = ''.join(overview_en)
            # overview_en = remove_tags(overview_en)
            overview_en = clear_space_str(overview_en)
            # print(overview_en)
        except:
            overview_en = ''

        #8.duration
        try:
            duration = response.xpath('/html/body/div[1]/main/div[2]/div/ul/li[1]/span').extract()
            duration = ''.join(duration)
            duration = re.findall('\d',duration)[0]
        except:
            duration = ''
        # print(duration)

        #9.duration_per
        duration_per = 1


        #10.modules_en
        try:
            modules_en = response.xpath('//*[@id="accordionItem1"]/div').extract()
            modules_en = ''.join(modules_en)
            modules_en = remove_class(modules_en)
            modules_en = clear_space_str(modules_en)
        except:
            modules_en = ''
        # print(modules_en)

        #11.assessment_en
        try:
            assessment_en = response.xpath('//*[@id="accordionItem2"]/div').extract()
            assessment_en = ''.join(assessment_en)
            assessment_en = remove_class(assessment_en)
            assessment_en = clear_space_str(assessment_en)
        except:
            assessment_en = ''
        # print(assessment_en)

        #12.career_en
        try:
            career_en = response.xpath('//*[@id="accordionItem4"]/div').extract()
            career_en = ''.join(career_en)
            career_en = remove_class(career_en)
            career_en = clear_space_str(career_en)
        except:
            career_en = ''
        # print(career_en)

        #13.tuition_fee
        try:
            tuition_fee = response.xpath('//*[@id="accordionItem5"]/div/p[2]').extract()
            tuition_fee = ''.join(tuition_fee)
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = re.findall('\£(\d+)', tuition_fee)[0]
        except:
            tuition_fee = 'N/A'
        # print(tuition_fee)

        #14.tuition_fee_pre
        tuition_fee_pre = '£'

        #15.rntry_requirements
        rntry_requirements = response.xpath('//*[@id="accordionItem3"]/div').extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_tags(rntry_requirements)
        rntry_requirements = clear_space_str(rntry_requirements)
        # print(rntry_requirements)

        #16.ielts
        if 'Classics' in programme_en:
            ielts = 6.5
            ielts_w = 7
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        elif 'theatre' in programme_en:
            ielts = 6.5
            ielts_w = 7
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        elif 'English' in programme_en:
            ielts = 7
            ielts_w = 7
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        elif 'European Studies' in programme_en:
            ielts = 6.5
            ielts_w = 6.5
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        elif 'History' in programme_en:
            ielts = 6.5
            ielts_w = 7
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        elif 'Media Arts' in programme_en:
            ielts = 6.5
            ielts_w = 6.5
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        elif 'Music' in programme_en:
            ielts = 6.5
            ielts_w = 7
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        elif 'Economics' in programme_en:
            ielts = 6.5
            ielts_w = 6
            ielts_r = 6
            ielts_l = 6
            ielts_s = 6
        elif 'MBA' in programme_en:
            ielts = 7
            ielts_w = 6
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        elif 'Management' in programme_en:
            ielts = 6.5
            ielts_w = 6
            ielts_r = 6
            ielts_l = 6
            ielts_s = 6
        elif 'Biological Sciences' in programme_en:
            ielts = 6.5
            ielts_w = 7
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        elif 'Electronic Engineering' in programme_en:
            ielts = 6.5
            ielts_w = 5.5
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        elif 'Physics' in programme_en:
            ielts = 6.5
            ielts_w = 5.5
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        elif 'Psychology' in programme_en:
            ielts = 6.5
            ielts_w = 5.5
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        else:
            ielts = 6.5
            ielts_w = 5.5
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5


        #21.require_chinese_en
        require_chinese_en =''

        #22.url
        url = response.url

        #23.other
        other = 'https://intranet.royalholloway.ac.uk/international/documents/pdf/internationalstudentsupport/tier-4-checklist-outside-uk.pdf'

        #24.apply_proces_en
        apply_proces_en = 'https://admissions.royalholloway.ac.uk/AP/Login.aspx'
        #25.teach_time
        teach_time = 'Full-time'


        item['teach_time'] = teach_time
        item['other'] = other
        item['apply_proces_en'] =apply_proces_en
        item['university'] = university
        item['department'] = department
        item['location'] = location
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['programme_en'] = programme_en
        item['overview_en'] = overview_en
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['rntry_requirements'] = rntry_requirements
        item['ielts'] = ielts
        item['ielts_w'] = ielts_w
        item['ielts_r'] = ielts_r
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['require_chinese_en'] = require_chinese_en
        item['url'] = url
        yield item