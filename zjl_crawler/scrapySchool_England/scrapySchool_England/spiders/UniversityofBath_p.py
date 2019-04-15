# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/4 13:55'
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
from scrapySchool_England.TranslateMonth import translate_month
class UniversityofBathSpider(scrapy.Spider):
    name = 'UniversityofBath_p'
    allowed_domains = ['bath.ac.uk/']
    start_urls = []
    C= [
        'https://www.bath.ac.uk/courses/postgraduate-2019/taught-postgraduate-courses/msc-molecular-biosciences-medical-biosciences/',
        'https://www.bath.ac.uk/courses/postgraduate-2019/taught-postgraduate-courses/msc-molecular-biosciences-biotechnology/',
        'https://www.bath.ac.uk/courses/postgraduate-2019/taught-postgraduate-courses/msc-molecular-biosciences-microbiology/',
        'https://www.bath.ac.uk/courses/postgraduate-2019/taught-postgraduate-courses/msc-molecular-biosciences-bioinformatics/',
        'https://www.bath.ac.uk/courses/postgraduate-2019/taught-postgraduate-courses/msc-environmental-engineering/'
    ]
    C = set(C)
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Bath'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.degree_name
        degree_name = response.xpath('/html/body/main/div[2]/div/div/h1/span').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        degree_name = clear_space_str(degree_name)
        # print(degree_name)

        #4.programme_en
        programme_en = response.xpath('/html/body/main/div[2]/div/div/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        programme_en = programme_en.replace(degree_name,'')
        programme_en = clear_space_str(programme_en)
        programme_en1 = response.xpath('/html/body/main/div[2]/div/div/h2').extract()
        programme_en1 = ''.join(programme_en1)
        programme_en1 = remove_tags(programme_en1)
        programme_en1 = clear_space_str(programme_en1)
        # print(programme_en1)
        if 'Russian' in programme_en1:
            programme_en = programme_en + '-'+ programme_en1
            programme_en = programme_en.replace(', starting in October 2018','').replace(', starting in September 2018','')
        elif 'French' in programme_en1:
            programme_en = programme_en +'-'+ programme_en1
            programme_en = programme_en.replace(', starting in October 2018','').replace(', starting in September 2018','')
        elif 'German' in programme_en1:
            programme_en = programme_en +'-'+ programme_en1
            programme_en = programme_en.replace(', starting in October 2018','').replace(', starting in September 2018','')
        elif 'Spanish' in programme_en1:
            programme_en = programme_en +'-'+ programme_en1
            programme_en = programme_en.replace(', starting in October 2018','').replace(', starting in September 2018','')
        elif 'Italian' in programme_en1:
            programme_en = programme_en +'-'+ programme_en1
            programme_en = programme_en.replace(', starting in October 2018','').replace(', starting in September 2018','')
        else:
            programme_en = programme_en
        # print(programme_en)

        #5.degree_type
        degree_type = 2

        #6.duration
        duration_list = response.xpath('/html/body/main/div[2]/div/div/h2/text()').extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        duration_list = clear_space_str(duration_list)
        # print(duration_list)
        duration = re.findall('\d',duration_list)[0]
        # print(duration)

        #7.start_date
        start_date = translate_month(duration_list)
        # print(start_date)
        start_date = '2018-'+ str(start_date)
        # print(start_date)

        #8.teach_type
        teach_type ='Taught'

        #9.overview_en
        overview_en = response.xpath('/html/body/main/section[1]//p').extract()
        overview_en = ''.join(overview_en)
        overview_en = clear_space_str(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #10.modules_en
        modules_en = response.xpath('//*[@id="course-structure"]').extract()
        modules_en = ''.join(modules_en)
        # modules_en = clear_space_str(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #11.assessment_en
        assessment_en = response.xpath('//*[@id="learning-assessment"]//article[2]//li').extract()
        assessment_en = '\n'.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #12.require_chinese_en
        require_chinese_en = '<p>A four-year Bachelor’s degree with a final overall score of at least 80% depending on the institution attended.To apply for this course you may have an undergraduate degree in any subject.We may make an offer based on a lower grade if you can provide evidence of your suitability for the degree.</p>'

        #13.career_en
        career_en =response.xpath("//*[contains(text(),'Graduate prospects')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        career_en = clear_space_str(career_en)
        if len(career_en) ==0:
            career_en = response.xpath("//*[contains(text(),'Careers')]//following-sibling::*").extract()
            career_en = ''.join(career_en)
            career_en = remove_class(career_en)
            career_en = clear_space_str(career_en)
        else:
            pass
        # print(career_en)

        #14.ielts 15161718
        ielts_list = response.xpath('//*[@id="entry-requirements"]/section[1]//li[1]').extract()
        ielts_list = ''.join(ielts_list)
        ielts_list = remove_tags(ielts_list)
        # print(ielts_list)
        ielts = re.findall('\d\.\d',ielts_list)
        if len(ielts) ==3:
            a=ielts[0]
            b=ielts[1]
            c=ielts[2]
            ielts = a
            ielts_s = b
            ielts_r = c
            ielts_w = c
            ielts_l = c
        elif len(ielts) ==2:
            a= ielts[0]
            b= ielts[1]
            ielts = a
            ielts_s = b
            ielts_r = b
            ielts_w = b
            ielts_l = b
        else:
            ielts = 6.5
            ielts_s = 6
            ielts_r = 6
            ielts_w = 6
            ielts_l = 6
        # print(ielts,ielts_l,ielts_w,ielts_s,ielts_r)

        #19.teach_time
        teach_time = response.xpath("//*[contains(text(),'Mode of study')]//following-sibling::*").extract()
        teach_time = ''.join(teach_time)
        teach_time = remove_tags(teach_time)
        if len(teach_time) > 20:
            teach_time = 'Part time'
        # print(teach_time)

        #20.deadline
        deadline_list = response.xpath("//*[contains(text(),'Overseas deadline')]//following-sibling::*").extract()
        deadline_list = ''.join(deadline_list)
        deadline_list =remove_tags(deadline_list)
        if len(deadline_list)!=0:
            deadline_day = re.findall('\d+',deadline_list)[0]
        else:
            deadline_day = 30
        deadline_month = translate_month(deadline_list)
        deadline = '2018-'+str(deadline_month)+'-'+str(deadline_day)
        # print(deadline)

        #21.location
        location = 'Bath'

        #22.department
        department = response.xpath("//*[contains(text(),'Department')]//following-sibling::div/a").extract()
        department = ''.join(department)
        department = remove_tags(department)
        department = department.replace('&amp;','')
        # print(department)

        #23.apply_proces_en
        apply_proces_en = 'https://www.bath.ac.uk/study/pg/applications.pl'

        #24.tuition_fee_pre
        tuition_fee_pre = '£'

        #25.other
        other = 'http://www.bath.ac.uk/corporate-information/faculty-of-humanities-social-sciences-taught-postgraduate-tuition-fees-2018-19/'

        #26.duration_per
        duration_per = 1

        #27.tuition_fee
        if 'Economics and Finance' in programme_en:
            tuition_fee = 19000
        elif programme_en =='Economics':
            tuition_fee = 15900
        elif department =='Department of Economics':
            tuition_fee = 17700
        elif programme_en =='Education':
            tuition_fee = 15900
        elif department =='Department of Education':
            tuition_fee = 17700
        elif department =='Department for Health':
            tuition_fee = 15900
        elif 'Translation and Professional Language Skills' in programme_en:
            tuition_fee = 16650
        elif 'Politics and International Studies' in programme_en:
            tuition_fee = 15900
        elif 'Department of Politics' in department:
            tuition_fee = 17700
        elif programme_en  =='Psychology':
            tuition_fee = 15900
        elif 'Sustainable Futures' in programme_en:
            tuition_fee = 15900
        elif department == 'Department of Psychology':
            tuition_fee = 17700
        elif 'International Development' in programme_en:
            tuition_fee = 17700
        elif 'Department of Social' in department:
            tuition_fee = 15900
        else:
            tuition_fee = 17700
        #28.apply_documents_en
        apply_documents_en = '<p>Apply for a course To apply for a course, you must use the online application form. You will need to create an account before you can start the application process. On the application form, you will need to give: your personal details the date you plan to start studying your education details proof of your English level if English is not your first language the name and contact details of an academic referee from your current or most recent place of study your personal statement, explaining your reasons for wishing to study the course your supporting information Supporting information So we can assess your application and make our decision, you will need to give us all the necessary supporting information, including: a scan of your undergraduate degree certificate and your postgraduate degree certificate, if you have one a scan of your final degree transcript or your most recent transcript if you are still studying an academic reference from your current or most recent place of study, if you have one an up-to-date CV payment of the application fee, if applicable You can also upload supporting documents through Application Tracker after you have submitted your online application. International applicants If you are an international student, you should also give us: your passport details if you need a Tier 4 visa an authorised translation of your degree certificate and transcript if they are not in English your English language assessment certificate, if available Track your application We will send you login details for Application Tracker when you have submitted your application. We aim to make decisions about applications within six weeks of receiving all your supporting information and will tell you whether or not you have been successful through Application Tracker. You can also check the progress of your application there. We may also contact you for more information or, depending on the course you apply for, to invite you to an interview. Accept your offer If you receive an offer, use Application Tracker to accept or decline as soon as possible. For some courses, you will need to pay a deposit when you accept your offer. Receiving an unconditional offer If you receive an unconditional offer, you have met all the required academic conditions and we are offering you a place. Receiving a conditional offer If you receive a conditional offer, you may not have met all the requirements, but we hope you will be able to do so. These requirements may include English language scores, degree results, satisfactory references or payment of a deposit. You must meet these requirements and submit evidence of them through Application Tracker before you can start your studies. If you need to improve your English language skills before starting your studies, you may be able to take a pre-sessional course to reach the required level. When you meet the conditions of your offer, we will contact you and tell you what to do next.</p>'
        #29.apply_pre
        apply_pre = '£'
        #30.toefl 31323334
        toefl_list = response.xpath('//*[@id="entry-requirements"]/section[2]/div//ul/li[3]').extract()
        toefl_list = ''.join(toefl_list)
        try:
            toefl = re.findall('\d{2,3}',toefl_list)
        except:
            toefl = ['90','21']
        if len(toefl) ==3:
           a = toefl[0]
           b = toefl[1]
           c = toefl[2]
           toefl = a
           toefl_s = b
           toefl_r = c
           toefl_l = c
           toefl_w = c
        elif len(toefl) ==2:
           a = toefl[0]
           b = toefl[1]
           toefl = a
           toefl_s = b
           toefl_r = b
           toefl_l = b
           toefl_w = b
        else:
            toefl = 90
            toefl = 21
            toefl_s = 21
            toefl_r = 21
            toefl_l = 21
            toefl_w = 21
        # print(toefl,toefl_s,toefl_r,toefl_l,toefl_w)
        #35.rntry_requirements
        rntry_requirements = response.xpath('//*[@id="entry-requirements"]/section[1]/div[1]').extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        item['rntry_requirements'] = rntry_requirements
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_w'] = toefl_w
        item['toefl_l'] = toefl_l
        item['apply_pre'] = apply_pre
        item['apply_documents_en'] = apply_documents_en
        item['tuition_fee'] = tuition_fee
        item['university'] = university
        item['url'] = url
        item['degree_name'] = degree_name
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['start_date'] = start_date
        item['teach_type'] = teach_type
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['require_chinese_en'] = require_chinese_en
        item['career_en'] = career_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['teach_time'] = teach_time
        item['deadline'] = deadline
        item['location'] = location
        item['department'] = department
        item['apply_proces_en'] = apply_proces_en
        item['tuition_fee_pre'] = tuition_fee_pre
        item['other'] = other
        yield  item