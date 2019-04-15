import scrapy
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from scrapySchool_Canada_Ben import getItem
from w3lib.html import remove_tags
import re
import time

class BaiduSpider(scrapy.Spider):
    name = 'lakehead_university_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['https://www.lakeheadu.ca/academics/other-programs/aboriginal-programs/aboriginal-education/node/3268',
'https://www.lakeheadu.ca/academics/undergraduate-programs/orillia/anthropology/node/14',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/applied-life-sciences/node/18',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/bioinformatics/node/3364',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/biology/node/3362',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/business/node/3456',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/chemistry/node/2709',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/computer-science/node/1110',
'https://www.lakeheadu.ca/academics/undergraduate-programs/orillia/criminology/node/3363',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/economics/node/2957',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/education-concurrent/node/3437',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/education-two-year/node/3438',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/engineering/node/3569',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/engineering/chemical/node/1111',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/engineering/civil/node/3355',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/engineering/electrical/node/3570',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/engineering/mechanical/node/3571',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/engineering/software/node/3575',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/english/node/3354',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/environmental-management/node/3577',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/environmental-studies/node/3578',
'https://www.lakeheadu.ca/academics/undergraduate-programs/orillia/environmental-sustainability/node/3358',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/forestry-hbscf/node/3579',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/general-arts/node/3580',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/general-science/node/3581',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/geoarchaeology/node/3593',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/geography/node/3357',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/geology/node/3601',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/gerontology/node/1114',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/history/node/3600',
'https://www.lakeheadu.ca/academics/other-programs/aboriginal-programs/native-language-instructors-program/node/3271',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/indigenous-learning/node/3787',
'https://www.lakeheadu.ca/academics/other-programs/aboriginal-programs/native-teacher-education/node/3338',
'https://www.lakeheadu.ca/academics/undergraduate-programs/orillia/interdisciplinary-studies/node/3453',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/kinesiology/node/1113',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/lakehead-arts-one/node/28166',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/lakehead-science-one/node/28167',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/languages/node/3353',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/jd-law/node/3598',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/math/node/3597',
'https://www.lakeheadu.ca/academics/undergraduate-programs/orillia/media-studies/node/3454',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/medicine/node/1570',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/music/node/3352',
'https://www.lakeheadu.ca/academics/other-programs/aboriginal-programs/native-access-program/node/3270',
'https://www.lakeheadu.ca/academics/undergraduate-programs/natural-resources-management/node/48836',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/natural-science/node/3596',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/northern-studies/node/3595',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/nursing/node/1571',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/outdoorrec/node/2960',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/philosophy/node/3594',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/physics/node/3361',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/political-science/node/3602',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/psychology/node/3592',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/resource-and-environmental-economics/node/3360',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/social-work/node/1101',
'https://www.lakeheadu.ca/academics/undergraduate-programs/orillia/sociology/node/23871',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/visual-arts/node/2959',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/water-resource-science/node/3359',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/womens-studies/node/2958',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/computer-science/node/1110',
'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/applied-life-sciences/node/18',
         'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/applied-life-sciences/node/18',
         'https://www.lakeheadu.ca/academics/undergraduate-programs/thunder-bay/computer-science/node/1110',
         ]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        item = getItem.get_item(ScrapyschoolCanadaBenItem)



#1.学校名称
        school_name = 'Lakehead University'

#2.地点
        try:
            location = response.xpath('').extract()[0]
            location = remove_tags(location)
            #print(location)
        except:
            location = None
            #print(location)

#3. 校区
        try:
            campus_list = response.xpath('//h2[contains(text(),"Campus")]/following-sibling::div[1]').extract()[0]
            campus_list = remove_tags(campus_list)
            campus_list = campus_list.replace(', Online','')
            campus_list = campus_list.replace(' ','')
            campus_list = campus_list.split(',')
            #print(campus_list)
        except:
            campus_list = None
            #print(campus_list)

#4. 学院
        try:
            department = response.xpath('//h2[contains(text(),"Department")]/following-sibling::div[2]').extract()[0]
            department = remove_tags(department)
            #print(department)
        except:
            department = None
            #print(department)

# 4. 学位名称列表,需要拆分,在下方yield 处写循环.此处是拆分存入列表
    #'https://www.lakeheadu.ca/academics/undergraduate-programs/engineering'特殊情况
        #'https://www.lakeheadu.ca/academics/undergraduate-programs/forestry'
        try:
            degree_name_list = response.xpath('//h2[contains(text(),"Degrees")]/following-sibling::div[1]').extract()[0]
            degree_name_list = remove_tags(degree_name_list,keep=('li','br',''))
            degree_name_list = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_name_list)
            degree_name_list = degree_name_list.replace('<br>','---')
            degree_name_list = degree_name_list.replace('<li>','').replace('</li>','---')
            degree_name_list = degree_name_list.replace('<span>','').replace('</span>','---')
            degree_name_list = degree_name_list.split('---')
           # print(degree_name_list)
        except:

            degree_name_list = None
            #print(degree_name_list)

#5.学位描述
        try:
            degree_overview_en = response.xpath('//div[2]/div[1]/div/div/div/p|//div/div[1]/div/div/div/p').extract()
            degree_overview_en = ''.join(degree_overview_en)
            #degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_overview_en)
            #degree_overview_en = degree_overview_en.replace('\r\n','')
            #degree_overview_en = degree_overview_en.replace('\n','')
            #degree_overview_en = degree_overview_en.replace('\n','')
            #degree_overview_en = degree_overview_en.replace('  ',' ')
            #degree_overview_en = degree_overview_en.replace('					','')
            #degree_overview_en = degree_overview_en.replace('			  	','')
            #print(degree_overview_en)
        except:
            degree_overview_en = None
            #print(degree_overview_en)

#6.专业英文
        try:
            major_name_en = response.xpath('//h1').extract()[0]
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

# #8.入学时间
#         try:
#             start_date = response.xpath('').extract()[0]
#             start_date = remove_tags(start_date)
#             # print(start_date)
#         except:
#             start_date = None
#             # print(start_date)

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
            modules_en = response.xpath('//div[@class = "field field-name-field-first-year field-type-text-long field-label-hidden"]').extract()[0]
            modules_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',modules_en)
            #print(modules_en)
        except:
            modules_en = None
            #print(modules_en)

#11.就业方向
        try:
            career_en = response.xpath('//h2[contains(text(),"Future Careers")]/following-sibling::div[1]').extract()[0]
            career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',career_en)
            #print(career_en)
        except:
            career_en = None
            #print(career_en)

#12.截止日期
        try:
            deadline = '2018-11-02,2019-03-01'
            #deadline = remove_tags(deadline)
            # print(career_en)
        except:
            deadline = None
            # print(deadline)
#13.学费
        try:
            tuition_fee = response.xpath('//tbody/tr[1]/td[2]/div/div').extract()[-1]
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = tuition_fee.replace('$','')
            #print(tuition_fee)
        except:
            tuition_fee = None
            #print(tuition_fee)
#14 申请费:
        apply_fee = '135'

#15 申请要求

        try:
            entry_requirements_en = '<div><h3>General Admission Requirements</h3><p>To be considered for admission as an International Student, you must currently reside outside of Canada and you are not a Canadian citizen.&nbsp;<span class="s1">To meet the General Admission Requirements to Lakehead, you will need the following:</span></p><ul><li>Successful graduation from an academic secondary school program or equivalent (For most countries, the same academic preparation as is required for university entrance in that country is required for consideration. Refer to&nbsp;Admission Requirements by Country.</a>)&nbsp;</li><li>Program-Specific Prerequisite courses completed at the senior level (e.g. Grade 12);</li><li>Equivalent of a minimum 70% overall final average (Canadian)</li></ul><p>Note: Meeting the minimum admission requirements is not a guarantee of admission.</p></div>'
            #entry_requirements_en = remove_tags(entry_requirements_en)
            # print(entry_requirements_en)
        except:
            entry_requirements_en = None
            # print(entry_requirements_en)

#16 中国学生申请要求
        try:
            require_chinese_en = '<p>Senior High School (Upper Middle School) Graduation Diploma</p><div><h3>General Admission Requirements</h3><p>To be considered for admission as an International Student, you must currently reside outside of Canada and you are not a Canadian citizen.&nbsp;<span class="s1">To meet the General Admission Requirements to Lakehead, you will need the following:</span></p><ul><li>Successful graduation from an academic secondary school program or equivalent (For most countries, the same academic preparation as is required for university entrance in that country is required for consideration. Refer to&nbsp;Admission Requirements by Country.</a>)&nbsp;</li><li>Program-Specific Prerequisite courses completed at the senior level (e.g. Grade 12);</li><li>Equivalent of a minimum 70% overall final average (Canadian)</li></ul><p>Note: Meeting the minimum admission requirements is not a guarantee of admission.</p></div>'
            #require_chinese_en = remove_tags(require_chinese_en)
            # print(require_chinese_en)
        except:
            require_chinese_en = None
            # print(require_chinese_en)

#17 特殊专业要求
        try:
            specific_requirement_en = 'https://www.lakeheadu.ca/studentcentral/applying/general-admission-requirements/international-student'
            specific_requirement_en = remove_tags(specific_requirement_en)
            ## print(specific_requirement_en)
        except:
            specific_requirement_en = None
            # print(specific_requirement_en)

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
            min_language_require = 'Applicants will automatically be considered for admission through Lakehead University\'s Academic English Program if they meet Lakehead University\'s admission requirements but do not meet English language proficiency requirements. Applicants who complete Lakehead University\'s Academic English Program will meet the English language proficiency requirement for programs that require an IELTS score of 6.5 (no minimum score less than 6.0) or a TOEFL score of 80 (no minimum score less than 19). As a result, applicants interested in the: Nursing programs, Juris Doctor program, One-Year Social Work program, or the Two-Year Bachelor of Education program will need to successfully complete one of the recognized tests with the appropriate minimum scores as outlined in Option 1.'
            min_language_require = remove_tags(min_language_require)
            # print(min_language_require)
        except:
            min_language_require = None
            # print(min_language_require)

#25 雅思要求
        try:
            ielts_desc = 'IELTS score of 6.5 (no minimum score less than 6.0) '
            #ielts_desc = remove_tags(ielts_desc)
            # print(ielts_desc)
        except:
            ielts_desc = None
            # print(ielts_desc)

#26 ielts
        try:
            ielts = '6.5'
            #ielts = remove_tags(ielts)
            # print(ielts)
        except:
            ielts = None
            # print(ielts)
#27 ielts_?

        ielts_l = 6.0
        ielts_s = 6.0
        ielts_r = 6.0
        ielts_w = 6.0

#28 toefl_code
        try:
            toefl_code = '0888'
            #toefl_code = remove_tags(toefl_code)
            # print(toefl_code)
        except:
            toefl_code = None
            # print(toefl_code)

#29 toefl_desc
        try:
            toefl_desc = 'Minimum Score: 80 (no component score less than 19)'
            #toefl_desc = remove_tags(toefl_desc)
            # print(toefl_desc)
        except:
            toefl_desc = None
            # print(toefl_desc)

#30 toefl
        try:
            toefl = '80'
            #toefl = remove_tags(toefl)
            # print(toefl)
        except:
            toefl = None
            # print(toefl)

#31 toefl_?
        toefl_l = 19
        toefl_s = 19
        toefl_r = 19
        toefl_w = 19

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
            if 'Biology' in major_name_en:
                ib = 'Biology 1-00 (Unspecified First Year Full Credit), Credit Weight:1.0'
            elif 'Chemistry' in major_name_en:
                ib = 'Chemistry 1110 Chemistry 1130,Credit Weight:0.5,0.5'
            elif 'Computer Science' in major_name_en:
                ib = 'Computer Science 1_10 (if score of 5,Unspecified First Year Half Credit)Credit Weight:0.5;if score of 6 or better,Computer Science 1_00 (Unspecified First Year Full Credit) Credit Weight:1.0'
            elif 'Economics' in major_name_en:
                ib = 'Economics 1100 ,Credit Weight:1.0'
            elif 'English' in major_name_en:
                ib = 'English 1115 Arts 1-10 (Unspecified First Year Half Credit),Credit Weight:0.5,0.5'
            elif 'French' in major_name_en:
                ib = 'French 1200,Credit Weight: 1.0'
            elif 'Geography' in major_name_en:
                ib = 'Geography 1150,Credit Weight:0.5'
            elif 'Global Politics' in major_name_en:
                ib = 'Political Science 2611,Credit Weight:0.5'
            elif 'History' in major_name_en:
                ib = 'History 1100 (Allows you to begin completing Year 2 History course requirements),Credit Weight:1.0'
            elif 'Information Technology in a Global Society' in major_name_en:
                ib = 'Sociology 2_00 (Unspecified Second Year Full Credit),Credit Weight:1.0'
            elif 'Language' in major_name_en:
                ib = 'Each language will be assessed on an individual basis.,Credit Weight: up to 1.0'
            elif 'Mathematics' in major_name_en:
                ib = 'Math 1-00 (Unspecified First Year Full Credit),Credit Weight: 1.0'
            elif 'Music' in major_name_en:
                ib = 'Assessed on an individual basis.,Credit Weight:up to 1.0'
            elif 'Philosophy' in major_name_en:
                ib = 'Philosophy 1-10 (Unspecified First Year Half Credit),Credit Weight:0.5'
            elif 'Social and Cultural Anthropology' in major_name_en:
                ib = 'Anthropology 1034,Credit Weight:0.5'
            elif 'Social and Cultural Anthropology' in major_name_en:
                ib = 'Anthropology 1034,Credit Weight:0.5'
            elif 'Sports' in major_name_en:
                ib = 'Kinesiology 1010,Credit Weight:0.5'
            elif 'Exercise and Health Science' in major_name_en:
                ib = 'Kinesiology 1_10 (Unspecified First Year Half Credit),Credit Weight:0.5'
            elif 'Visual Arts' in major_name_en:
                ib = 'Visual Arts 1-00 (Unspecified First Year Full Credit),Credit Weight:1.0'
            else:
                ib = 'IB Diploma with a total score of 28* in six subjects, three of which must be at the Higher Level (HL) with no score less than 4 in any subjectProgram-Specific Prerequisite courses *Higher scores may be required for admission to programs in which the demand for places by qualified applicants exceeds the supply of available spaces.'

            #print(ib)
        except:
            ib = None
            #print(ib)

#34 ap
        try:
            ap = response.xpath('').extract()[0]
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
            other = '(1).专业特殊要求字段中,匹配不了专业+学位名(因专业详情页中的学位名与专业特殊要求页面中的学位名不相同,)故无法匹配.网站:https://www.lakeheadu.ca/studentcentral/applying/general-admission-requirements/international-student,duration,(2).地点 location,gaokao_desc，huikao_desc，duration， ,sat2_desc,interview_desc,protfolio_desc字段已经与老师核对确认为空,(3).toefl_code 和 sat_code,act_code,每所学校都相同,其他公共字段相同也同老师核对完毕(4)课程字段每个专业进去的页面并不相同,抓取很有难度.故跟老师反映后并获得同意后,只抓能抓到的第一年的课程'
            #other = remove_tags(other)
            # print(other
        except:
            other = None
            # print(other)

        # sat act 代码 介绍
        sat_code = '0888'
        sat1_desc = 'The SAT with the following scores: Reading* = five hundred and fifty (550) Math = five hundred and fifty (550) Total score = one thousand and one hundred (1100)'
        sat2_desc = None
        act_code = '5190*'
        act_desc = 'The Enhanced Composite ACT with a Total Score of twenty-four (24)'

        item["ap"] = ap
        item["duration_per"] = 1
        #item["duration"] = duration
        item["school_name"] = school_name
        item["location"] = location
        #item["campus"] = campus
        #item["degree_type"] = 1
        item["department"] = department
        #item["degree_name"] = degree_name
        item["degree_overview_en"] = degree_overview_en
        item["major_name_en"] = major_name_en
        item["overview_en"] = overview_en
        #item["teach_time"] = 1
        #item["start_date"] = start_date
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

        for i in campus_list:
            item["campus"] = i
            if 'ThunderBay' in i:
                item["start_date"] = '2019-01,2019-09'
            if 'Orillia' in i:
                item["start_date"] = '2019-01,2019-09'

            for b in degree_name_list:
                #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if ' in ' in b:
                    item["major_name_en"] = re.findall('in (.*)',b)[0]
                    if  ')' in item["major_name_en"]:
                       # print(item["major_name_en"] + "---" + response.url)
                        item["major_name_en"] = re.findall('\((.*)\)',b)[0]
                #print(item["major_name_en"])
                    else:
                        pass
                elif '(' in b:
                    item["major_name_en"] = re.findall('\((.*)\)',b)[0]
                   # print(item["major_name_en"])
                    if 'Co-op program available' in item["major_name_en"]:
                        item["major_name_en"] = major_name_en + "(Co-op program available)"
                    elif 'Co-op option available' in item["major_name_en"]:
                        item["major_name_en"] = major_name_en + "(Co-op option available)"
                    elif 'year' in item["major_name_en"]:
                        item["major_name_en"] = major_name_en
                item["major_name_en"] = item["major_name_en"].replace(' Major','')
               #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                if '(' in b:
                    item["degree_name"] =re.sub('\(.*\)', '', b)
                    if ' in ' in item["degree_name"]:
                        item["degree_name"] = re.sub(' in .*', '', b)
                elif ' in ' in b:
                    item["degree_name"] =re.sub(' in .*', '', b)
                else:
                    item["degree_name"] = b
                print(item["degree_name"])

                #print(item["major_name_en"])
                if '1' in b:
                    duration = '1'
                    item["duration"] = duration
                elif '2' in b:
                    duration = '2'
                    item["duration"] = duration
                elif '3' in b:
                    duration = '3'
                    item["duration"] = duration
                elif '4' in b:
                    duration = '4'
                    item["duration"] = duration
                elif '5' in b or 'five' in b or 'Five' in b:
                    duration = '5'
                    item["duration"] = duration
                else:
                    item["duration"] = None
                #print(b)
                if 'Minor' not in major_name_en :
                    yield item
                   # pass


