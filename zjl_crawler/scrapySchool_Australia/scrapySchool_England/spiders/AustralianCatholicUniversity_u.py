# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/31 18:38'
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
from scrapySchool_England.clearSpace import clear_space_str
import requests
from lxml import etree
from scrapySchool_England.translate_date import tracslateDate
from scrapySchool_England.getTuition_fee import getT_fee
class AustralianCatholicUniversitySpider(scrapy.Spider):
    name = 'AustralianCatholicUniversity_u'
    allowed_domains = ['acu.edu.au/']
    start_urls = []
    C= [
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_applied_public_health',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_biomedical_science',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_early_childhood_education_birth_to_five_years',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_accounting_and_finance',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_business_administration',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_arts',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_creative_arts',
        'http://www.acu.edu.au/courses/undergraduate/social_work/human_services/bachelor_of_human_services',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_inclusive_education_and_disability_studies',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_education_primary',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_information_technology',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_exercise_and_sports_science',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_international_development_studies',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_laws',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_nursing',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_education_early_childhood_and_primary',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_occupational_therapy',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_nutrition_science',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_physical_activity_and_health_science',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_media_production',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_nursing_enrolled_nurses',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_laws_graduate_entry',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_speech_pathology',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_sport_and_outdoor_education',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_social_work',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_psychological_science',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_youth_work',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_physiotherapy',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_sport_and_outdoor_education',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_visual_arts_and_design',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_theology',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_commerce',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_commerce',
        'http://www.acu.edu.au/courses/2019/undergraduate/bachelor_of_commerce'
    ]
    # print(len(C))
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Australian Catholic University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.degree_name
        degree_name = response.xpath('//*[@id="main-content"]/section/div/h1').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        degree_name = clear_space_str(degree_name)
        # print(degree_name)

        #4.location
        location = response.xpath('//*[@id="main-content"]/div[2]/div[1]/div[1]/dl/dd[2]/ul/li').extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #5.degree_overview_en
        degree_overview_en = response.xpath('//*[@id="collapseOne"]/div').extract()
        degree_overview_en = ''.join(degree_overview_en)
        degree_overview_en = remove_class(degree_overview_en)
        # print(degree_overview_en)


        #6.duration
        duration = response.xpath('//*[@id="collapseTwo"]/div/p').extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        try:
            duration = re.findall(r'\d',duration)[0]
        except:
            duration = ''
        # print(duration)

        #7.modules_en
        modules_en_url = response.xpath('//*[@id="collapseFive"]/div/a//@href').extract()[-1]
        modules_en_url = ''.join(modules_en_url)
        headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        try:
            data = requests.get(modules_en_url, headers=headers)
            response1 = etree.HTML(data.text)
            modules_en = response1.xpath("//h3[contains(text(),'Curriculum Studies')]//following-sibling::table")
            if len(modules_en) == 0:
                modules_en = response1.xpath("//h3[contains(text(),'Core Units')]//following-sibling::table[1]")
            if len(modules_en) == 0:
                modules_en = response1.xpath("//table")
            doc = ""
            if len(modules_en) > 0:
                for a in modules_en:
                    doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc = remove_class(doc)
        except:
            modules_en = 'N/A'
            doc = None
        # print(modules_en)

        #8.start_date
        start_date = response.xpath('//*[@id="kollapseThree"]/div').extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        start_date = clear_space_str(start_date)
        # print(start_date)

        #9.career_en
        try:
            career_en = response.xpath("//*[contains(text(),'Career paths')]/../../following-sibling::*").extract()[0]
            career_en = ''.join(career_en)
            career_en = remove_class(career_en)
        except:
            career_en = 'N/A'
        # print(career_en)

        #10.programme_en
        # print(degree_name)
        programme_en = degree_name.replace('Bachelor of ','')
        # print(programme_en)

        #11.deadline
        deadline = ''
        # print(deadline)

        #12.apply_pre
        apply_pre = '$'

        #13.apply_fee
        apply_fee = '110'

        #14.tuition_fee
        tuition_fee = response.xpath('//*[@id="kollapseSix"]/div/ul/li[2]').extract()
        tuition_fee = ''.join(tuition_fee)
        # print(tuition_fee)
        tuition_fee = getT_fee(tuition_fee)
        # print(tuition_fee)

        #15.rntry_requirements_en
        rntry_requirements_en = response.xpath("//*[contains(text(),'Essential requirements for admission')]/../../following-sibling::*").extract()
        rntry_requirements_en = ''.join(rntry_requirements_en)
        rntry_requirements_en = remove_class(rntry_requirements_en)
        # print(rntry_requirements_en)

        #16.apply_documents_en
        apply_documents_en = '高中毕业证/在读证明 高中成绩单 语言成绩 护照 高考成绩单'

        #17.apply_desc_en
        apply_desc_en = 'https://www.acu.edu.au/international/how_to_apply'

        #18.average_score
        average_score = '70'

        #19.ielts 20212223 24.toefl 25262728
        ielts_list = response.xpath("//*[contains(text(),'English language requirements')]/../../following-sibling::*").extract()
        ielts_list = ''.join(ielts_list)
        ielts_list = remove_class(ielts_list)
        if len(ielts_list)==0:
            ielts_list = response.xpath("//*[contains(text(),'Essential requirements for admission')]/../../following-sibling::*").extract()
            ielts_list = ''.join(ielts_list)
            ielts_list = remove_tags(ielts_list)
        if '100' in ielts_list:
            toefl = 100
            toefl_r = 25
            toefl_s = 25
            toefl_l = 25
            toefl_w = 25
        else:
            toefl = 79
            toefl_r = 0
            toefl_s = 0
            toefl_l = 0
            toefl_w = 0
        # print(toefl,toefl_r,toefl_s,toefl_l,toefl_w)
        # print(ielts,ielts_r,ielts_l,ielts_w,ielts_s,response.url)
        # print(ielts_list)

        item['university'] = university
        item['url'] = url
        item['degree_name'] = degree_name
        item['location'] = location
        item['degree_overview_en'] = degree_overview_en
        item['duration'] = duration
        item['modules_en'] = doc
        item['start_date'] = start_date
        item['career_en'] = career_en
        item['deadline'] = deadline
        item['apply_pre'] = apply_pre
        item['apply_fee'] = apply_fee
        item['tuition_fee'] = tuition_fee
        item['rntry_requirements_en'] = rntry_requirements_en
        item['apply_documents_en'] = apply_documents_en
        item['apply_desc_en'] = apply_desc_en
        item['average_score'] = average_score
        item['ielts'] = ''
        item['ielts_r'] = ''
        item['ielts_w'] = ''
        item['ielts_l'] = ''
        item['ielts_s'] = ''
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['toefl_w'] = toefl_w
        item['programme_en'] = programme_en
        yield item
        #
        #
        # if url =='http://www.acu.edu.au/courses/2018/postgraduate/master_of_education':
        #     major = response.xpath("//*[contains(text(),'Specialisations')]/../../following-sibling::div//h3//text()").extract()
        #     for i in major:
        #         cour = i
        #         xpaths = "//*[contains(text(),'" +str(cour)+"')]//following-sibling::p[1]"
        #         overview_en_a = response.xpath(xpaths).extract()
        #         overview_en_a = ''.join(overview_en_a)
        #         item['programme_en'] = cour
        #         item['overview_en'] = overview_en_a
        #         yield item
        # else:
        #     item['programme_en'] = programme_en
        #     item['overview_en'] = ''
        #     yield item

