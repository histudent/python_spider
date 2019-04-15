# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/6 9:11'
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
class EdgeHillUniversitySpider(scrapy.Spider):
    name = 'EdgeHillUniversity_u'
    allowed_domains = ['edgehill.ac.uk/']
    start_urls = []
    C= [
        'https://www.edgehill.ac.uk/courses/accountancy',
        'https://www.edgehill.ac.uk/courses/business-and-management-with-accounting-and-finance',
        'https://www.edgehill.ac.uk/courses/advertising',
        'https://www.edgehill.ac.uk/courses/business-and-management-with-marketing',
        'https://www.edgehill.ac.uk/courses/marketing',
        'https://www.edgehill.ac.uk/courses/marketing-with-advertising',
        'https://www.edgehill.ac.uk/courses/marketing-with-digital-communications',
        'https://www.edgehill.ac.uk/courses/animation',
        'https://www.edgehill.ac.uk/courses/biology',
        'https://www.edgehill.ac.uk/courses/biotechnology',
        'https://www.edgehill.ac.uk/courses/ecology-and-conservation',
        'https://www.edgehill.ac.uk/courses/food-science/',
        'https://www.edgehill.ac.uk/courses/genetics',
        'https://www.edgehill.ac.uk/courses/human-biology',
        'https://www.edgehill.ac.uk/courses/plant-science/',
        'https://www.edgehill.ac.uk/courses/business-and-economics',
        'https://www.edgehill.ac.uk/courses/business-and-management',
        'https://www.edgehill.ac.uk/courses/business-and-management-with-accounting-and-finance',
        'https://www.edgehill.ac.uk/courses/business-and-management-with-human-resource-management',
        'https://www.edgehill.ac.uk/courses/business-and-management-with-leisure-and-tourism',
        'https://www.edgehill.ac.uk/courses/business-and-management-with-logistics-and-supply-chain-management/',
        'https://www.edgehill.ac.uk/courses/business-and-management-with-marketing',
        'https://www.edgehill.ac.uk/courses/business-innovation-and-enterprise',
        'https://www.edgehill.ac.uk/courses/international-business',
        'https://www.edgehill.ac.uk/courses/child-and-adolescent-mental-health-and-wellbeing/',
        'https://www.edgehill.ac.uk/courses/child-health-and-wellbeing',
        'https://www.edgehill.ac.uk/courses/childhood-and-youth-studies',
        'https://www.edgehill.ac.uk/courses/childhood-youth-studies-and-criminology/',
        'https://www.edgehill.ac.uk/courses/childhood-youth-studies-and-sociology/',
        'https://www.edgehill.ac.uk/courses/early-childhood-studies',
        'https://www.edgehill.ac.uk/courses/early-childhood-studies-and-sociology/',
        'https://www.edgehill.ac.uk/study/courses/children-and-young-people-s-learning-and-development',
        'https://www.edgehill.ac.uk/study/courses/teaching-learning-and-child-development',
        'https://www.edgehill.ac.uk/courses/working-and-teaching-in-the-early-years/',
        'https://www.edgehill.ac.uk/courses/working-with-children-5-11/',
        'https://www.edgehill.ac.uk/courses/business-information-systems',
        'https://www.edgehill.ac.uk/courses/information-technology-management-for-business',
        'https://www.edgehill.ac.uk/courses/computer-science-bsc',
        'https://www.edgehill.ac.uk/courses/computer-science-and-mathematics',
        'https://www.edgehill.ac.uk/courses/data-science/',
        'https://www.edgehill.ac.uk/courses/computer-security-and-networks',
        'https://www.edgehill.ac.uk/courses/computing',
        'https://www.edgehill.ac.uk/courses/computing-mcomp',
        'https://www.edgehill.ac.uk/courses/computing-games-programming',
        'https://www.edgehill.ac.uk/courses/computing-networking-security-and-forensics',
        'https://www.edgehill.ac.uk/courses/robotics-and-artificial-intelligence/',
        'https://www.edgehill.ac.uk/courses/software-application-development',
        'https://www.edgehill.ac.uk/courses/software-engineering/',
        'https://www.edgehill.ac.uk/courses/web-design-and-development',
        'https://www.edgehill.ac.uk/courses/web-design-and-development-mcomp',
        'https://www.edgehill.ac.uk/courses/counselling-and-psychotherapy/',
        'https://www.edgehill.ac.uk/courses/critical-approaches-to-counselling-and-psychotherapy/',
        'https://www.edgehill.ac.uk/courses/creative-writing',
        'https://www.edgehill.ac.uk/courses/creative-writing-and-drama/',
        'https://www.edgehill.ac.uk/courses/creative-writing-and-english-literature/',
        'https://www.edgehill.ac.uk/courses/creative-writing-and-film-studies/',
        'https://www.edgehill.ac.uk/courses/childhood-youth-studies-and-criminology/',
        'https://www.edgehill.ac.uk/courses/criminology-ba',
        'https://www.edgehill.ac.uk/courses/criminology-and-law',
        'https://www.edgehill.ac.uk/courses/criminology-and-psychology',
        'https://www.edgehill.ac.uk/courses/criminology-and-sociology/',
        'https://www.edgehill.ac.uk/courses/politics-and-criminology/',
        'https://www.edgehill.ac.uk/courses/psychology-and-criminology',
        'https://www.edgehill.ac.uk/courses/psychosocial-analysis-of-offending-behaviour',
        'https://www.edgehill.ac.uk/courses/education-ba',
        'https://www.edgehill.ac.uk/courses/education-and-english',
        'https://www.edgehill.ac.uk/courses/education-and-history',
        'https://www.edgehill.ac.uk/courses/education-and-religion',
        'https://www.edgehill.ac.uk/courses/education-and-sociology',
        'https://www.edgehill.ac.uk/courses/children-and-young-people-s-learning-and-development',
        'https://www.edgehill.ac.uk/courses/teaching-learning-and-child-development',
        'https://www.edgehill.ac.uk/courses/working-and-teaching-in-the-early-years/',
        'https://www.edgehill.ac.uk/courses/working-with-children-5-11/',
        'https://www.edgehill.ac.uk/courses/creative-writing-and-english-literature/',
        'https://www.edgehill.ac.uk/courses/drama-and-english-literature/',
        'https://www.edgehill.ac.uk/courses/education-and-english/',
        'https://www.edgehill.ac.uk/courses/english',
        'https://www.edgehill.ac.uk/courses/english-and-film-studies/',
        'https://www.edgehill.ac.uk/courses/english-language',
        'https://www.edgehill.ac.uk/courses/english-language-with-creative-writing/',
        'https://www.edgehill.ac.uk/courses/english-literature',
        'https://www.edgehill.ac.uk/courses/english-literature-and-history/',
        'https://www.edgehill.ac.uk/courses/english-literature-with-creative-writing/',
        'https://www.edgehill.ac.uk/courses/english-with-creative-writing/',
        'https://www.edgehill.ac.uk/courses/film-and-television-production/',
        'https://www.edgehill.ac.uk/courses/media-film-and-television',
        'https://www.edgehill.ac.uk/courses/television-production-management',
        'https://www.edgehill.ac.uk/courses/creative-writing-and-film-studies/',
        'https://www.edgehill.ac.uk/courses/drama-and-film-studies/',
        'https://www.edgehill.ac.uk/courses/english-and-film-studies/',
        'https://www.edgehill.ac.uk/courses/film-studies',
        'https://www.edgehill.ac.uk/courses/film-studies-with-film-production',
        'https://www.edgehill.ac.uk/courses/environmental-science',
        'https://www.edgehill.ac.uk/courses/geoenvironmental-hazards/',
        'https://www.edgehill.ac.uk/courses/geography-bsc',
        'https://www.edgehill.ac.uk/courses/geography-ba',
        'https://www.edgehill.ac.uk/courses/geology-with-physical-geography',
        'https://www.edgehill.ac.uk/courses/human-geography',
        'https://www.edgehill.ac.uk/courses/physical-geography',
        'https://www.edgehill.ac.uk/courses/physical-geography-and-geology',
        'https://www.edgehill.ac.uk/courses/child-and-adolescent-mental-health-and-wellbeing/',
        'https://www.edgehill.ac.uk/courses/child-health-and-wellbeing',
        'https://www.edgehill.ac.uk/courses/counselling-and-psychotherapy',
        'https://www.edgehill.ac.uk/courses/critical-approaches-to-counselling-and-psychotherapy/',
        'https://www.edgehill.ac.uk/courses/global-public-health/',
        'https://www.edgehill.ac.uk/courses/health-and-social-care-leadership-and-management/',
        'https://www.edgehill.ac.uk/courses/health-and-social-wellbeing',
        'https://www.edgehill.ac.uk/courses/nutrition-and-health',
        'https://www.edgehill.ac.uk/courses/nutrition-msci/',
        'https://www.edgehill.ac.uk/courses/psychosocial-analysis-of-offending-behaviour',
        'https://www.edgehill.ac.uk/courses/education-and-history/',
        'https://www.edgehill.ac.uk/courses/english-literature-and-history/',
        'https://www.edgehill.ac.uk/courses/history',
        'https://www.edgehill.ac.uk/courses/history-with-politics/',
        'https://www.edgehill.ac.uk/courses/politics-and-history/',
        'https://www.edgehill.ac.uk/courses/criminology-and-law',
        'https://www.edgehill.ac.uk/courses/law',
        'https://www.edgehill.ac.uk/courses/law-with-criminology',
        'https://www.edgehill.ac.uk/courses/law-with-politics',
        'https://www.edgehill.ac.uk/courses/medicine',
        'https://www.edgehill.ac.uk/courses/mbchb',
        'https://www.edgehill.ac.uk/courses/media-music-and-sound',
        'https://www.edgehill.ac.uk/courses/music',
        'https://www.edgehill.ac.uk/courses/music-production',
        'https://www.edgehill.ac.uk/courses/musical-theatre',
        'https://www.edgehill.ac.uk/courses/midwifery',
        'https://www.edgehill.ac.uk/courses/nursing-adult',
        'https://www.edgehill.ac.uk/courses/nursing-children',
        'https://www.edgehill.ac.uk/courses/nursing-learning-disabilities',
        'https://www.edgehill.ac.uk/courses/nursing-mental-health',
        'https://www.edgehill.ac.uk/courses/adult-nursing-and-social-work/',
        'https://www.edgehill.ac.uk/courses/childrens-nursing-and-social-work/',
        'https://www.edgehill.ac.uk/courses/learning-disabilities-and-nursing-social-work/',
        'https://www.edgehill.ac.uk/courses/mental-health-nursing-and-social-work/',
        'https://www.edgehill.ac.uk/courses/operating-department-practice-bsc/',
        'https://www.edgehill.ac.uk/courses/nutrition-and-health',
        'https://www.edgehill.ac.uk/courses/nutrition-msci/',
        'https://www.edgehill.ac.uk/courses/paramedic-practice-bsc/',
        'https://www.edgehill.ac.uk/courses/creative-performance/',
        'https://www.edgehill.ac.uk/courses/creative-writing-and-drama/',
        'https://www.edgehill.ac.uk/courses/dance/',
        'https://www.edgehill.ac.uk/courses/dance-and-drama/',
        'https://www.edgehill.ac.uk/courses/drama/',
        'https://www.edgehill.ac.uk/courses/drama-and-english-literature/',
        'https://www.edgehill.ac.uk/courses/drama-and-film-studies/',
        'https://www.edgehill.ac.uk/courses/musical-theatre/',
        'https://www.edgehill.ac.uk/courses/policing/',
        'https://www.edgehill.ac.uk/courses/politics-and-criminology/',
        'https://www.edgehill.ac.uk/courses/politics-and-history/',
        'https://www.edgehill.ac.uk/courses/politics-and-media/',
        'https://www.edgehill.ac.uk/courses/politics-and-sociology/',
        'https://www.edgehill.ac.uk/courses/history-with-politics/',
        'https://www.edgehill.ac.uk/courses/law-with-politics/',
        'https://www.edgehill.ac.uk/courses/sociology-with-politics/',
        'https://www.edgehill.ac.uk/courses/fastrack-preparation-for-higher-education',
        'https://www.edgehill.ac.uk/courses/international-foundation-programme/',
        'https://www.edgehill.ac.uk/courses/criminology-and-psychology',
        'https://www.edgehill.ac.uk/courses/educational-psychology',
        'https://www.edgehill.ac.uk/courses/psychology',
        'https://www.edgehill.ac.uk/courses/psychology-and-criminology',
        'https://www.edgehill.ac.uk/courses/psychosocial-analysis-of-offending-behaviour',
        'https://www.edgehill.ac.uk/courses/sport-and-exercise-psychology',
        'https://www.edgehill.ac.uk/courses/social-work',
        'https://www.edgehill.ac.uk/courses/adult-nursing-and-social-work/',
        'https://www.edgehill.ac.uk/courses/childrens-nursing-and-social-work/',
        'https://www.edgehill.ac.uk/courses/learning-disabilities-and-nursing-social-work/',
        'https://www.edgehill.ac.uk/courses/mental-health-nursing-and-social-work/',
        'https://www.edgehill.ac.uk/courses/childhood-youth-studies-and-sociology/',
        'https://www.edgehill.ac.uk/courses/criminology-and-sociology/',
        'https://www.edgehill.ac.uk/courses/early-childhood-studies-and-sociology/',
        'https://www.edgehill.ac.uk/courses/education-and-sociology/',
        'https://www.edgehill.ac.uk/courses/politics-and-sociology/',
        'https://www.edgehill.ac.uk/courses/sociology',
        'https://www.edgehill.ac.uk/courses/sociology-with-politics/',
        'https://www.edgehill.ac.uk/courses/physical-education-and-school-sport',
        'https://www.edgehill.ac.uk/courses/sport-and-exercise-psychology',
        'https://www.edgehill.ac.uk/courses/sport-and-exercise-science',
        'https://www.edgehill.ac.uk/courses/sports-coaching-and-development',
        'https://www.edgehill.ac.uk/courses/sports-development-and-management',
        'https://www.edgehill.ac.uk/courses/sports-management-and-coaching',
        'https://www.edgehill.ac.uk/courses/sports-therapy',
        'https://www.edgehill.ac.uk/courses/?post_type=course&p=96513',
        'https://www.edgehill.ac.uk/courses/sports-coaching-and-development-msci',
        'https://www.edgehill.ac.uk/courses/?post_type=course&p=96515',
        'https://www.edgehill.ac.uk/courses/early-years-education-with-qts',
        'https://www.edgehill.ac.uk/courses/primary-education-with-qts',
        'https://www.edgehill.ac.uk/courses/secondary-english-education-with-qts',
        'https://www.edgehill.ac.uk/courses/secondary-mathematics-education-with-qts',
        'https://www.edgehill.ac.uk/courses/secondary-religious-education-with-qts'
    ]
    C = set(C)
    # print(len(C))
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Edge Hill University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="primary"]/header/h1/a').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        degree_name = programme_en.split()[0]
        programme_en = programme_en.replace(degree_name,'').strip()
        if '(Hons)' in programme_en:
            programme_en = programme_en.replace('(Hons)','').strip()
        # print(degree_name,'***',programme_en)
        # print(programme_en)

        #6.duration
        duration = response.xpath("//*[contains(text(),'Length:')]//following-sibling::*").extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        if ',' in duration:
            duration = re.findall(r'(.*),',duration)[0]
        if 'Full-Time' in duration:
            duration = duration.replace('Full-Time','').strip()
        # print(duration)


        #7.start_date
        start_date = response.xpath("//*[contains(text(),'Dates:')]//following-sibling::*").extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        start_date = tracslateDate(start_date)
        start_date = ','.join(start_date)
        # print(start_date)

        #8.ucascode
        ucascode = response.xpath("//*[contains(text(),'UCAS Code:')]//following-sibling::*").extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode)
        # print(ucascode)

        #9.alevel
        alevel = response.xpath('//*[@id="entry-criteria"]/ul/li[1]').extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel)
        # print(alevel)

        #10.department
        department = response.xpath("//*[contains(text(),'Department:')]//following-sibling::*").extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #11.location
        location = response.xpath("//*[contains(text(),'Location:')]//following-sibling::*").extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #12.overview_en
        overview_en = response.xpath('//*[@id="overview"]/div[1]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #13.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'How will I be assessed?')]//following-sibling::*[1]").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #14.modules_en
        modules_en = response.xpath('//*[@id="modules"]/h4/strong').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #15.apply_desc_en
        apply_desc_en = response.xpath('//*[@id="entry-criteria"]').extract()
        apply_desc_en = ''.join(apply_desc_en)
        apply_desc_en = remove_class(apply_desc_en)
        # print(apply_desc_en)

        #16.ielts 17.18.19.20
        ielts_list = response.xpath("//*[contains(text(),'English Language Requirements')]//following-sibling::*[1]").extract()
        ielts_list = ''.join(ielts_list)
        ielts_list = remove_tags(ielts_list)
        # print(ielts_list)
        try:
            ielts = re.findall('\d\.\d',ielts_list)
        except:
            ielts = None
        if len(ielts) ==1:
            a = ielts[0]
            ielts = a
            ielts_r = a
            ielts_w = a
            ielts_s = a
            ielts_l = a
        elif len(ielts) ==2:
            a= ielts[0]
            b= ielts[1]
            ielts = a
            ielts_r = b
            ielts_w = b
            ielts_s = b
            ielts_l = b
        else:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
        # print(ielts,ielts_r,ielts_w,ielts_l,ielts_s)

        #21.career_en
        career_en = response.xpath("//*[contains(text(),'What are my career prospects?')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #22.tuition_fee
        tuition_fee= response.xpath("//*[contains(text(),'Tuition Fees')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #23.tuition_fee_pre
        tuition_fee_pre= '£'

        #24.apply_proces_en
        apply_proces_en = response.xpath("//h4[contains(text(),'How to Apply')]//following-sibling::*").extract()
        apply_proces_en = ''.join(apply_proces_en)
        apply_proces_en = remove_class(apply_proces_en)
        # print(apply_proces_en)

        #25.apply_pre
        apply_pre = '£'

        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['ucascode'] = ucascode
        item['duration'] = duration
        item['apply_desc_en'] = apply_desc_en
        item['start_date'] = start_date
        item['department'] = department
        item['location'] = location
        item['overview_en'] = overview_en
        item['assessment_en'] = assessment_en
        item['modules_en'] = modules_en
        item['alevel'] = alevel
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_proces_en'] = apply_proces_en
        yield  item