# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/3 9:31'
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
class UniversityofLeedsSpider(scrapy.Spider):
    name = 'UniversityofLeeds_p'
    allowed_domains = ['leeds.ac.uk/']
    start_urls = []
    C= [
        'https://courses.leeds.ac.uk/i628/global-governance-and-diplomacy-ma'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Leeds'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="main"]/div/header/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        degree_name_list = programme_en.split()
        degree_name = degree_name_list[-1]
        programme_en = programme_en.replace(degree_name,'').strip()
        # print(programme_en)
        # print(degree_name)

        #6.overview_en
        overview_en = response.xpath('//*[@id="acc1"]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #7.modules_en
        modules_en = response.xpath("//*[contains(text(),'Modules')]//following-sibling::div").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        modules_en = clear_space_str(modules_en)
        # print(modules_en)

        #8.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'Assessment')]//following-sibling::*").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = clear_space_str(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #9.start_date
        start_date = response.xpath('//*[@id="keyfacts-acc"]/ul/li[1]/span[2]').extract()
        start_date = ''.join(start_date)
        start_date = clear_space_str(start_date)
        start_date = remove_tags(start_date)
        if 'September' in start_date:
            start_date = '2018-9'
        elif 'October' in start_date:
            start_date = '2018-10'
        elif 'January' in start_date:
            start_date = '2019-1'
        elif '6 August 2018' in  start_date:
            start_date = '2018-8-6'
        elif '9 July 2018' in  start_date:
            start_date = '2018-7-9'
        else:
            start_date = '2018-9'
        # print(start_date)

        #10.duration  #24.duration_per
        duration_list = response.xpath("//*[contains(text(),'Duration/Mode')]//following-sibling::*").extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        duration_list = clear_space_str(duration_list)
        # print(duration_list)
        try:
            duration_a = re.findall('\d+',duration_list)[0]
        except:
            duration_a = 'N/A'
        if '6 weeks' in duration_list:
            duration = 6
            duration_per = 4
        elif '10 weeks' in duration_list:
            duration = 10
            duration_per = 4
        elif int(duration_a) > 3:
            duration = duration_a
            duration_per = 3
        else:
            duration = duration_a
            duration_per = 1
        # print(duration,'*******************',duration_per)

        #11.teach_time
        if 'full time' in duration_list:
            teach_time = 'full time'
        else:
            teach_time = 'part time'

        #12.ielts 13141516
        ielts_list = response.xpath("//*[contains(text(),'Language requirements')]//following-sibling::*").extract()
        ielts_list = ''.join(ielts_list)
        ielts = re.findall('\d\.\d',ielts_list)
        # print(ielts)
        if len(ielts) ==2:
            a = ielts[0]
            b = ielts[1]
            ielts = a
            ielts_w = b
            ielts_r = b
            ielts_s = b
            ielts_l = b
        elif len(ielts) ==1:
            a = ielts[0]
            ielts = a
            ielts_w = a
            ielts_r = a
            ielts_s = a
            ielts_l = a
        elif len(ielts) == 3:
            a = ielts[0]
            b = ielts[1]
            c = ielts[2]
            ielts = a
            ielts_w = b
            ielts_r = c
            ielts_s = c
            ielts_l = c
        else:
            ielts = None
            ielts_w = None
            ielts_r = None
            ielts_s = None
            ielts_l = None
        # print(ielts,ielts_w,ielts_s,ielts_r,ielts_l)
        # print(ielts_s+ielts_s)

        #17.department
        department =response.xpath("//*[contains(text(),'This course is taught by')]/../following-sibling::*").extract()
        department = ''.join(department)
        department = remove_tags(department)
        department = clear_space_str(department)
        # print(department)

        #18.rntry_requirements
        rntry_requirements = response.xpath("//*[contains(text(),'Entry requirements:')]//following-sibling::*[1]").extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = clear_space_str(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        if 'Full entry requirements' in  rntry_requirements:
            rntry_requirements = rntry_requirements.replace('Full entry requirements','')
        else:
            pass
        # print(rntry_requirements)

        #19.tuition_fee
        tuition_fee= response.xpath("//*[contains(text(),'International fees')]//following-sibling::*[1]").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = clear_space_str(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        try:
            tuition_fee = re.findall('\d+,\d+',tuition_fee)[0]
            tuition_fee = tuition_fee.replace(',','')
        except:
            tuition_fee = None
        # print(tuition_fee)

        #20.tuition_fee_pre
        tuition_fee_pre = '£'

        #21.deadline
        deadline = response.xpath("//*[contains(text(),'Application deadlines')]//following-sibling::*[1]|//*[contains(text(),'Application deadlines:')]/../following-sibling::*[1]").extract()
        deadline = ''.join(deadline)
        deadline = remove_tags(deadline)
        # print(deadline)
        if 'August' in deadline:
            deadline = '2018-8-31'
        elif 'July' in deadline:
            deadline = '2018-7-31'
        elif 'June'  in deadline:
            deadline = '2018-6-30'
        elif 'April' in deadline:
            deadline = '2018-4-30'
        else:
            deadline = 'N/a'
        # print(deadline)

        #22.career_en
        career_en = response.xpath("//h2[contains(text(),'Career opportunities')]/../following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        career_en = clear_space_str(career_en)
        # print(career_en)

        #23.apply_proces_en
        apply_proces_en = 'https://application.leeds.ac.uk/login/?returnurl=%2f'
        #24.toefl 25262728
        toefl = 92
        toefl_l = 21
        toefl_r = 21
        toefl_s = 23
        toefl_w = 22
        #29.apply_pre
        apply_pre  = '£'
        #30.apply_documents_en
        apply_documents_en = '<p>Make sure you have all your supporting documents scanned and ready to upload with your online application. All documents should be in English, or sent with certified translations into English. Without copies of the required documents we will be unable to make you an offer.</p>'

        item['apply_pre'] = apply_pre
        item['apply_documents_en'] = apply_documents_en
        item['toefl'] = toefl
        item['toefl_l'] = toefl_l
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_w'] = toefl_w
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['start_date'] = start_date
        item['duration'] = duration
        item['teach_time'] = teach_time
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['department'] = department
        item['rntry_requirements'] = rntry_requirements
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['deadline'] = deadline
        item['career_en'] = career_en
        item['apply_proces_en'] = apply_proces_en
        item['duration_per'] = duration_per
        yield  item