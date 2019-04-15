import scrapy
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from scrapySchool_Canada_Ben import getItem
from w3lib.html import remove_tags
import requests
import re
import time

class BaiduSpider(scrapy.Spider):
    name = 'University_of_Northern_British_Columbia_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['https://www.unbc.ca/calendar/undergraduate/anthropology.html',
'https://www.unbc.ca/calendar/undergraduate/ba_general.html',
'https://www.unbc.ca/calendar/undergraduate/biochemistry_molecular_biology.html',
'https://www.unbc.ca/calendar/undergraduate/biology.html',
'https://www.unbc.ca/calendar/undergraduate/bsc_integrated.html',
'https://www.unbc.ca/calendar/undergraduate/chemistry.html',
'https://www.unbc.ca/calendar/undergraduate/commerce.html',
'https://www.unbc.ca/calendar/undergraduate/computer_science.html',
'https://www.unbc.ca/calendar/undergraduate/economics.html',
'https://www.unbc.ca/calendar/undergraduate/education.html',
'https://www.unbc.ca/calendar/undergraduate/english.html',
'https://www.unbc.ca/calendar/undergraduate/environmental_engineering.html',
'https://www.unbc.ca/calendar/undergraduate/environmental_science.html',
'https://www.unbc.ca/calendar/undergraduate/first_nations.html',
'https://www.unbc.ca/calendar/undergraduate/forest-ecology-mangement-bsc-program',
'https://www.unbc.ca/calendar/undergraduate/geography.html',
'https://www.unbc.ca/calendar/undergraduate/global-and-international-studies-ba-program',
'https://www.unbc.ca/calendar/undergraduate/health_sciences.html',
'https://www.unbc.ca/calendar/undergraduate/history.html',
'https://www.unbc.ca/calendar/undergraduate/mathematics_and_statistics.html',
'https://www.unbc.ca/calendar/undergraduate/nature_based_tourism_management.html',
'https://www.unbc.ca/calendar/undergraduate/nmp_admissions.html',
'https://www.unbc.ca/calendar/undergraduate/northern_studies.html',
'https://www.unbc.ca/calendar/undergraduate/nrem.html',
'https://www.unbc.ca/calendar/undergraduate/nursing.html',
'https://www.unbc.ca/calendar/undergraduate/philosophy.html',
'https://www.unbc.ca/calendar/undergraduate/physics.html',
'https://www.unbc.ca/calendar/undergraduate/planning.html',
'https://www.unbc.ca/calendar/undergraduate/political_science.html',
'https://www.unbc.ca/calendar/undergraduate/psychology.html',
'https://www.unbc.ca/calendar/undergraduate/russian-studies',
'https://www.unbc.ca/calendar/undergraduate/social_work.html',
'https://www.unbc.ca/calendar/undergraduate/wildlife-and-fisheries-bsc-program',
'https://www.unbc.ca/calendar/undergraduate/womens_studies.html',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        item = getItem.get_item(ScrapyschoolCanadaBenItem)



#1.学校名称
        school_name = 'University of Northern British Columbia'

#2.地点
        try:
            location = 'Prince George, British Columbia, Prince George, YXS'
            location = remove_tags(location)
            #print(location)
        except:
            location = None
            #print(location)

#3. 校区
        try:
            campus =  response.xpath('').extract()[0]
            campus = remove_tags(campus)
            campus = campus.replace(', Online','')
            campus = campus.replace(' ','')
            campus = campus.split(',')
            #print(campus)
        except:
            campus = None
            #print(campus)

#4. 学院
        try:
            department = None

            #print(len(department))
            #print(department)
            #print(response.url)
        except:
            department = None
           # print(department)

# 4.
        try:
            degree_name = response.xpath('//*[@id="page-title"]').extract()[0]
            degree_name = remove_tags(degree_name)
            degree_name = re.findall('\((.*)\)',degree_name)[0]
            degree_name = degree_name.replace(' Program','')
            #print(degree_name)
        except:

            degree_name = None
            #print(degree_name)

#5.学位描述
        try:
            degree_overview_en = response.xpath('//span[contains(text(),"Major in")]/following-sibling::text()').extract()
            degree_overview_en = ''.join(degree_overview_en)
            #degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_overview_en)
            #degree_overview_en = degree_overview_en.replace('\r\n','')
            #degree_overview_en = degree_overview_en.replace('\n','')
            #degree_overview_en = degree_overview_en.replace('\n','')
            #degree_overview_en = degree_overview_en.replace('  ',' ')
            #degree_overview_en = degree_overview_en.replace('					','')
            #degree_overview_en = degree_overview_en.replace('			  	','')
            print(degree_overview_en)
        except:
            degree_overview_en = None
            print(degree_overview_en)

#6.专业英文
        try:
            major_name_en = response.xpath('//*[@id="page-title"]').extract()[0]
            major_name_en = major_name_en.replace('\r\n','').replace('\n','').replace('           ','').replace('\t','').replace('     ','')
            major_name_en = remove_tags(major_name_en)
            #print(major_name_en)
        except:
            major_name_en = None
            #print(major_name_en)

#7.专业介绍
        try:
            #overview_en = degree_overview_en
            overview_en = degree_overview_en
            # print(overview_en)
        except:
            overview_en = degree_overview_en
            # print(overview_en)

#8.入学时间
        try:
            start_date = '2020-01,2019-09'
            #start_date = ','.join(start_date)
            #start_date = remove_tags(start_date)
            #start_date = start_date.replace('Spring','').replace('Winter','').replace('Summer','').replace('Fall','')
            #start_date = start_date.replace('September 2019','2019-09').replace('May 2019','2019-05').replace('July 2019','2019-07').replace('January 2020','2020-01').replace('January 2019','2019-01')
            #print(start_date)
        except:
            start_date = None
            #print(start_date)

#9.课程长度
        # try:
        #     duration = response.xpath('').extract()[0]
        #     duration = remove_tags(duration)
        #     # print(duration)
        # except:
        #     duration = None
        #     # print(duration)

#10.课程设置
        try:
            modules_en = response.xpath('//*[@id="content"]//table/tbody').extract()[0]
            modules_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',modules_en)
            modules_en = modules_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
            #print(modules_en)
        except:
            modules_en = None
            #print(modules_en)

#11.就业方向
        try:
            career_en = '<div><h3>UNBC Alumni Services</h3><p>Through the Student Career Centre,&nbsp;UNBC&nbsp;Alumni can attend career building workshops and view job postings.&nbsp;</p><p>Alumni with jobs to fill can also list postings for their own companies.&nbsp;</p><p>These services are offered in partnership with the&nbsp;UNBC&nbsp;Alumni Association.</p></div>'
           # career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',career_en)
            #career_en = career_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
            #print(career_en)
        except:
            career_en = None
            #print(career_en)

#12.截止日期
        try:
            deadline = '2019-06-01,2019-03-01'

            #print(deadline)
        except:
            deadline = None
            #print(deadline)
#13.学费
        try:
            tuition_fee = '620.39'
            #tuition_fee = remove_tags(tuition_fee)
            #tuition_fee = tuition_fee.replace('$','')
            #print(tuition_fee)
        except:
            tuition_fee = None
            #print(tuition_fee)


        item["tuition_fee_per"] = 5
#14 申请费:
        apply_fee = '125'

#15 申请要求
        try:


            entry_requirements_en = '<p>Graduation Certificate - Academic Senior Middle School,High School Transcript</p>'
            #entry_requirements_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',entry_requirements_en)
            #entry_requirements_en = ''.join(entry_requirements_en)
            #entry_requirements_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',entry_requirements_en)
            #entry_requirements_en = remove_tags(entry_requirements_en)
            #print(entry_requirements_en)
        except:
            entry_requirements_en = None
            #print(entry_requirements_en)
            #print(abc)

#16 中国学生申请要求
        try:
            require_chinese_en = '<p>Graduation Certificate - Academic Senior Middle School,High School Transcript</p>'
            #require_chinese_en = remove_tags(require_chinese_en)
            # print(require_chinese_en)
        except:
            require_chinese_en = None
            # print(require_chinese_en)

#17 特殊专业要求
        try:
            specific_requirement_en = None
#
            #specific_requirement_en = remove_tags(specific_requirement_en)
            #specific_requirement_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',specific_requirement_en)
            #specific_requirement_en = specific_requirement_en.replace('\r\n','')
            #specific_requirement_en = re.findall('Required high school classes(.*)2.',specific_requirement_en)[0]
            #specific_requirement_en = remove_tags(specific_requirement_en,keep=("li","ul"))
            #print(specific_requirement_en)
        except:
            specific_requirement_en = None
            #print(specific_requirement_en)

#18 高考(官网要求)
        try:
            gaokao_desc = response.xpath('').extract()[0]
            gaokao_desc = remove_tags(gaokao_desc)
            # print(gaokao_desc)
        except:
            gaokao_desc = None
            # print(gaokao_desc)

#19 高考(展示以及判断字段)
        try:
            gaokao_zs = response.xpath('').extract()[0]
            gaokao_zs = remove_tags(gaokao_zs)
            # print(gaokao_zs)
        except:
            gaokao_zs = None
            # print(gaokao_zs)

#20 高考分数(文科)
        try:
            gaokao_score_wk = response.xpath('').extract()[0]
            gaokao_score_wk = remove_tags(gaokao_score_wk)
            # print(gaokao_score_wk)
        except:
            gaokao_score_wk = None
            # print(gaokao_score_wk)

#21 高考分数(理科)
        try:
            gaokao_score_lk = response.xpath('').extract()[0]
            gaokao_score_lk = remove_tags(gaokao_score_lk)
            # print(gaokao_score_lk)
        except:
            gaokao_score_lk = None
            # print(gaokao_score_lk)

#22 会考描述
        try:
            huikao_desc = response.xpath('').extract()[0]
            huikao_desc = remove_tags(huikao_desc)
            # print(huikao_desc)
        except:
            huikao_desc = None
            # print(huikao_desc)

#23 会考描述
        try:
            huikao_zs = response.xpath('').extract()[0]
            huikao_zs = remove_tags(huikao_zs)
            # print(huikao_zs)
        except:
            huikao_zs = None
            # print(huikao_zs)

#24 最低语言要求
        try:
            min_language_require = 'IELTS (International English Language Testing System) Academic score of at least 6.5 overall, with not less than 6.0 in any of the four modules.'
            min_language_require = remove_tags(min_language_require)
            # print(min_language_require)
        except:
            min_language_require = None
            # print(min_language_require)

#25 雅思要求
        try:
            ielts_desc = 'IELTS (International English Language Testing System) Academic score of at least 6.5 overall, with not less than 6.0 in any of the four modules.'
            #ielts_desc = remove_tags(ielts_desc)
            # print(ielts_desc)
        except:
            ielts_desc = None
            # print(ielts_desc)

#26 ielts
        try:
            ielts = '6.5'
            #ielts = re.findall('\d\.\d',ielts)
            #ielts = remove_tags(ielts)
            #print(ielts)
        except:
            ielts = None
            #print(ielts)
#27 ielts_?

        ielts_l = 6.0
        ielts_s = 6.0
        ielts_r = 6.0
        ielts_w = 6.0

#28 toefl_code
        try:
            toefl_code = '0320'
            #toefl_code = remove_tags(toefl_code)
            # print(toefl_code)
        except:
            toefl_code = None
            # print(toefl_code)

#29 toefl_desc
        try:
            toefl_desc = 'TOEFL (Test of English as a Foreign Language) score of 90 or higher in the internet-based test, with not less than 20 in each of the Reading, Listening, Writing or Speaking components; Score of at least 230 in the computer based or at least 570 in the paper based test. UNBC’s institutional TOEFL code is 0320.'
            #toefl_desc = remove_tags(toefl_desc)
            # print(toefl_desc)
        except:
            toefl_desc = None
            # print(toefl_desc)

#30 toefl
        try:
            toefl = '90'
            #toefl = re.findall('\d\d',toefl)
            #toefl = remove_tags(toefl)
           # print(toefl)
        except:
            toefl = None
            #print(toefl)

#31 toefl_?
        toefl_l = 20
        toefl_s = 20
        toefl_r = 20
        toefl_w = 20

# 32 alevel
        try:
            alevel = 'Possess the (International) General Certificate of Secondary Education with: Passes in at least five subjects: Two of which must be at the Advanced Level (G.C.E.) Two subjects at the Advanced Supplementary (A.S.) Level may be substituted for one subject at the Advanced Level.  For example, 4 Advanced Supplementary (A.S.) Level courses equal two A Level Courses.  The remaining three passes may be at the Ordinary Level (G.C.S.E.) Acceptable standing must be achieved in all subjects Applicants may apply for admission in the year they will be sitting for their final A-Level examinations provided they can present excellent grades in their O-Level examinations and strong predicted A-Level results. With the exception of the Faculty of Engineering, for all other programs that require "Mathematics" as a prerequisite, AS-Level Mathematics is required. Applicants presenting A-Level examinations with a minimum grade of "C" may be considered for advanced standing. In addition to the above, applicants interested in the four year Bachelor of Engineering degree program must complete the following prerequisite courses: A-Level Mathematics A-Level Physics  A-Level Chemistry is preferred; however, AS-level Chemistry will be accepted  O-Level English '
            #alevel = remove_tags(alevel)
            # print(alevel)
        except:
            alevel = None
            # print(alevel)

#33 ib
        try:
            ib = 'Students who are awarded an International Baccalaureate Diploma may be awarded up to 29 credit hours of transfer credit upon receipt of the official transcript from the International Baccalaureate headquarters. Students who are awarded the diploma must have an overall standing of four, with no course below a three. Diploma students are required to present three Higher level subjects and three Subsidiary level subjects in order to be eligible for transfer credits.'
            #print(ib)
        except:
            ib = None
            #print(ib)

#34 ap
        try:
            ap = 'Students who take the College Board Advanced Placement courses in high school may be awarded transfer credit upon receipt of the official exam results from the College Board. Courses completed with a grade of four or above will be awarded transfer credit. Students who have completed AP courses with a grade of three may be considered for Advanced Standing. Advanced Standing allows a student to register in a higher level course without the required prerequisite. However, as credit is not awarded advanced standing will not reduce the number of credits that a student must accumulate to obtain a UNBC degree. As a result a student must make up this credit by completing another course to be used towards their degree requirements. A listing of acceptable AP courses for transfer credit is available on the BC Transfer Guide\'s website at  www.bctransferguide.ca/guides/ap).'
            ap = remove_tags(ap)
            # print(ap)
        except:
            ap = None
            # print(ap)

#35 面试描述
        try:
            interview_desc_en = response.xpath('').extract()[0]
            interview_desc_en = remove_tags(interview_desc_en)
            # print(interview_desc_en
        except:
            interview_desc_en = None
            # print(interview_desc_en)

#36 作品集描述
        try:
            portfolio_desc_en = response.xpath('').extract()[0]
            portfolio_desc_en = remove_tags(portfolio_desc_en)
            # print(portfolio_desc_en
        except:
            portfolio_desc_en = None
            # print(portfolio_desc_en)

#37 other
        try:
            other = ''
            #other = remove_tags(other)
            # print(other)
        except:
            other = None
            # print(other)

        # sat act 代码 介绍
        sat_code = '0320'
        sat1_desc = ''
        sat2_desc = None
        act_code = ''
        act_desc = 'The Enhanced Composite ACT with a Total Score of twenty-four (24)'

        item["ap"] = ap
        item["duration_per"] = 1
        #item["duration"] = duration
        item["school_name"] = school_name
        item["location"] = location
        item["campus"] = campus
        #item["degree_type"] = 1
        item["department"] = department
        item["degree_name"] = degree_name
        item["degree_overview_en"] = degree_overview_en
        item["major_name_en"] = major_name_en
        item["overview_en"] = overview_en
        #item["teach_time"] = 1
        item["start_date"] = start_date
        item["modules_en"] = modules_en
        item["career_en"] = career_en
        item["deadline"] = deadline
        item["apply_pre"] = 'CAD$'
        item["apply_fee"] = apply_fee
        item["entry_requirements_en"] = entry_requirements_en
        item["tuition_fee_pre"] = 'CAD$'
        item["require_chinese_en"] = require_chinese_en
        item["ielts_desc"] = ielts_desc
        item["ielts"] = ielts
        item["ielts_l"] = ielts_l
        item["ielts_s"] = ielts_s
        item["ielts_r"] = ielts_r
        item["ielts_w"] = ielts_w
        item["toefl_code"] = toefl_code
        item["toefl_desc"] = toefl_desc
        item["toefl_l"] = toefl_l
        item["toefl"] = toefl
        item["toefl_s"] = toefl_s
        item["toefl_r"] = toefl_r
        item["toefl_w"] = toefl_w
        item["interview_desc_en"] = interview_desc_en
        item["portfolio_desc_en"] = portfolio_desc_en
        item["other"] = other
        item["url"] = response.url
        item["gatherer"] = 'weihongbo'
        item["finishing"] = 0
        item["import_status"] = 0
        #item["duration"] = duration
        item["tuition_fee"] = tuition_fee
        item["alevel"] = alevel
        item["ib"] = ib
        item["gaokao_zs"] = gaokao_zs
        item["gaokao_score_wk"] = gaokao_score_wk
        item["gaokao_score_lk"] = gaokao_score_lk
        item["specific_requirement_en"] = specific_requirement_en
        item["huikao_desc"] = huikao_desc
        item["huikao_zs"] = huikao_zs
        item["min_language_require"] = min_language_require
        item["sat_code"] = sat_code
        item["sat1_desc"] = sat1_desc
        item["sat2_desc"] = sat2_desc
        item["act_code"] = act_code
        item["act_desc"] = act_desc
        item["average_score"] = '70'
            #print(degree_name_list)


        yield item


