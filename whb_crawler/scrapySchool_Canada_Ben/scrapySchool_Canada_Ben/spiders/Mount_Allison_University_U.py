import scrapy
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from scrapySchool_Canada_Ben import getItem
from w3lib.html import remove_tags
import requests
import re
import time

class BaiduSpider(scrapy.Spider):
    name = 'Mount_Allison_University_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['https://www.mta.ca/programs/americanstudies/',
'https://www.mta.ca/programs/appliedphysics/',
'https://www.mta.ca/programs/arthistory/',
'https://www.mta.ca/programs/astronomy/',
'https://www.mta.ca/programs/aviation/',
'https://www.mta.ca/programs/biochemistry/',
'https://www.mta.ca/programs/biology/',
'https://www.mta.ca/Prospective/Academics/Programs_of_study/Canadian_Public_Policy/Canadian_public_policy/',
'https://www.mta.ca/programs/canadianstudies/',
'https://www.mta.ca/programs/chemistry/',
'https://www.mta.ca/programs/classics/',
'https://www.mta.ca/programs/cogsci/',
'https://www.mta.ca/programs/commerce/',
'https://www.mta.ca/programs/cs/',
'https://www.mta.ca/programs/drama/',
'https://www.mta.ca/programs/economics/',
'https://www.mta.ca/programs/english/',
'https://www.mta.ca/programs/enviroscience/',
'https://www.mta.ca/programs/envirostudies/',
'https://www.mta.ca/programs/finearts/',
'https://www.mta.ca/programs/french/',
'https://www.mta.ca/programs/gis/',
'https://www.mta.ca/programs/geography/',
'https://www.mta.ca/programs/german/',
'https://www.mta.ca/programs/greek/',
'https://www.mta.ca/programs/hispanicstudies/',
'https://www.mta.ca/programs/history/',
'https://www.mta.ca/programs/ieb/',
'https://www.mta.ca/programs/ir/',
'https://www.mta.ca/programs/japanese/',
'https://www.mta.ca/programs/latin/',
'https://www.mta.ca/programs/math/',
'https://www.mta.ca/programs/mll/',
'https://www.mta.ca/programs/music/',
'https://www.mta.ca/programs/philosophy/',
'https://www.mta.ca/programs/ppe/',
'https://www.mta.ca/programs/physics/',
'https://www.mta.ca/programs/polisci/',
'https://www.mta.ca/programs/psychology/',
'https://www.mta.ca/programs/religiousstudies/',
'https://www.mta.ca/programs/sociology/',
'https://www.mta.ca/programs/wgs/',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        item = getItem.get_item(ScrapyschoolCanadaBenItem)



#1.学校名称
        school_name = 'Mount Allison University'

#2.地点
        try:
            location = response.xpath('//*[@id="page-wrapper"]/footer/div/div[1]/div/address/a').extract()[0]
            location = remove_tags(location)
           # print(location)
        except:
            location = None
           # print(location)

#3. 校区
        try:
            campus = 'main'
            # campus_list = remove_tags(campus)
            # campus_list = campus_list.replace(', Online','')
            # campus_list = campus_list.replace(' ','')
            # campus_list = campus_list.split(',')
            #print(campus_list)
        except:
            campus = None
            #print(campus_list)

        duration = None

#4. 学院
        try:
            department = response.xpath('//*[@id="programs_curriculum_holder"]/p[1]/text()[1]').extract()[0]
            #department = remove_tags(department,keep=("i"))
            department = re.findall('(F.*)',department)[0]
            #department = department.replace(' class="fa fa-graduation-cap"','').replace(' class="fa fa-university"','')
            #department = department.replace(' <i> </i> ','<i></i>').replace('<i> </i> ','')
            #department = department.split('<i></i>')[-1]
            #print(len(department))
            #print(department)
            #print(response.url)
        except:
            department = None
            #print(department)

# 4.
        try:
            degree_name = response.xpath('//*[@id="programs_curriculum_holder"]/p[1]/text()[2]').extract()[0]
            degree_name = degree_name.lstrip(' ')
            degree_name = re.findall('(.*? ).*',degree_name)[0]
            degree_name = degree_name.replace(':','BSc')
            degree_name = degree_name.replace(';','')
            # degree_name = remove_tags(degree_name,keep=('li','ul'))
            # #degree_name_list = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_name_list)
            # degree_name = degree_name.replace('\t','').replace('\n','').replace('\xa0','').replace(' class="list-inline uofs-cta-list','')
            # # degree_name_list = degree_name_list.replace('<li>','').replace('</li>','---')
            # # degree_name_list = degree_name_list.replace('<span>','').replace('</span>','---')
            # degree_name = degree_name.split('</li><li>')
            degree_name = degree_name.replace('BA','Bachelor of Arts')
            #print(degree_name)
            # #print(response.url)
        except:

            degree_name = None
           # print(degree_name)

#5.学位描述
        try:
            degree_overview_en = response.xpath('//*[@id="programs_intro_text"]').extract()
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
            major_name_en = response.xpath('//*[@id="page-wrapper"]/div/div[1]/div/div/div/h1').extract()[0]
            major_name_en = major_name_en.replace('\r\n','').replace('\n','').replace('           ','').replace('\t','').replace('     ','')
            major_name_en = remove_tags(major_name_en)
            major_name_en = major_name_en.replace('&amp; ','')
            major_name_en = major_name_en.replace('Ancient Greek','Greek')
           # print(major_name_en)
        except:
            major_name_en = None
           # print(major_name_en)

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
            start_date = '2019-01,2019-09'
            # start_date = ','.join(start_date)
            # start_date = remove_tags(start_date)
            # start_date = start_date.replace('Spring','').replace('Winter','').replace('Summer','').replace('Fall','')
            # start_date = start_date.replace('September 2019','2019-09').replace('May 2019','2019-05').replace('July 2019','2019-07').replace('January 2020','2020-01').replace('January 2019','2019-01')
            # #print(start_date)
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
            modules_en = response.xpath('//*[@id="programs_curriculum_holder"]').extract()[0]
            modules_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',modules_en)

            modules_en = modules_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
            abc = re.findall('<p>.*?</p>',modules_en)[0]
            modules_en = modules_en.replace(abc,'')
            print(modules_en)

        except:
            modules_en = None
            print(modules_en)

#11.就业方向
        try:
            career_en = response.xpath('//*[@id="programs_careers_holder"]').extract()[0]
            career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',career_en)
            career_en = career_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
            #print(career_en)
        except:
            career_en = None
            #print(career_en)

#12.截止日期
        try:
            if 'BMus' in degree_name:
                deadline = '2019-02-10'
            elif 'finearts' in response.url:
                deadline = '2019-02-15'
            else:
                deadline = '2019-03-01'
            #deadline = remove_tags(deadline)
            #print(deadline)
        except:
            deadline = None
            #print(deadline)
#13.学费
        try:
            if 'Aviation' in major_name_en:
                tuition_fee = '32120'
            else:
                tuition_fee = '17,600'

            #print(tuition_fee)
        except:
            tuition_fee = None
            #print(tuition_fee)
#14 申请费:
        apply_fee = '50'

#
        average_score = 'An average of 3.5 / 70%'
#15 申请要求
        try:
            entry_requirements_en = '<div><div><p><span>International admission requirements:</span></p><p>To be considered for admission, a university-preparatory language arts course and generally a minimum of four additional university-preparatory courses are required. A university-preparatory math (pre-calculus) is required for students applying to the Bachelor of Science or Commerce programs.</p><p>As admissions requirements vary by country and each application to Mount Allison is assessed on an individual basis, you are encouraged to contact your admissions counsellor (international@mta.ca) to discuss requirements as they apply to your specific academic background. Be sure to include your country, desired program of study, current grade, and age in your email so we can provide accurate and detailed advice.</p><p><strong>Official transcripts</strong>: To be considered \'official,\' transcripts must be forwarded directly to Mount Allison\'s registrar\'s office by the issuing institution. Please note that notarized English translations of required documents should be included if applicable.</p><p><strong>Regular admission</strong>: To be considered for admission, a minimum final grade of 65% or the equivalent is required in all university-preparatory courses reviewed.</p><p><strong>Early admission</strong>: Applicants may be considered for early admission based on their final grade 11 transcripts. A minimum admissions average of 80% is required for consideration.</p><p><strong>Conditional offers of admission</strong>: If an applicant meets Mount Allison’s academic requirements but has not provided proof of English language proficiency they may be granted a conditional offer of admission. Students must complete a university-preparatory English language program at one of <a>Mount Allison’s partner language training institutes</a><strong> </strong>or provide sufficient <a>proof of English language proficiency</a> before of full offer of admission will be granted.</p> </div><div><p>&nbsp;</p> </div><div></div></div>'

        except:
            entry_requirements_en = None
            #print(entry_requirements_en)
            #print(abc)

#16 中国学生申请要求
        try:
            require_chinese_en = '<p>Minimum entry requirements:<br>Senior Middle School Graduation Certificate<br>High school studies should be university preparatory <br>An average of 3.5 / 70%<br><a>An accepted proof of English proficiency</a><br><br>Students studying at vocational/technical high schools may be considered if they have strong grades and their educational background is relevant to their intended field of study.</p>'
            #require_chinese_en = remove_tags(require_chinese_en)
            # print(require_chinese_en)
        except:
            require_chinese_en = None
            # print(require_chinese_en)

#17 特殊专业要求
        try:
            #
            specific_requirement_en = None
            # #specific_requirement_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',specific_requirement_en)
            # specific_requirement_en = specific_requirement_en.replace('\r\n','')
            # specific_requirement_en = re.findall('Required high school classes(.*)2.',specific_requirement_en)[0]
            # specific_requirement_en = remove_tags(specific_requirement_en,keep=("li","ul"))
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
            min_language_require = 'International English Language Testing System – Academic (IELTS) score of 6.5 with no band score lower than 6*'
            min_language_require = remove_tags(min_language_require)
            # print(min_language_require)
        except:
            min_language_require = None
            # print(min_language_require)


#25 雅思要求
        try:
            ielts_desc = 'International English Language Testing System – Academic (IELTS) score of 6.5 with no band score lower than 6*'
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
            toefl_code = '0939'
            #toefl_code = remove_tags(toefl_code)
            # print(toefl_code)
        except:
            toefl_code = None
            # print(toefl_code)

#29 toefl_desc
        try:
            toefl_desc = 'TOEFL score of 90 (internet test), 580 (paper test), 213 (computer test) (DI Code 0939) with no band score lower than 20'
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
            #print(toefl)
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
            alevel = 'Students who have completed their ‘A’ Level exams with a minimum grade of D may qualify for up to 30 transfer credits.'
            #alevel = remove_tags(alevel)
            # print(alevel)
        except:
            alevel = None
            # print(alevel)

#33 ib
        try:
            ib = 'Students who successfully complete the IB diploma may receive up to 30 transfer credits comprised of higher level (HL) or standard level (SL) courses with a score of five (5) or higher, and theory of knowledge with a grade of C or higher.   IB certificate students who complete higher level (HL) courses with a score of five (5) or higher will be assessed for transfer credit for those HL courses to a maximum of 18 credits. Standard level (SL) courses completed as an IB certificate are not eligible for transfer credits.   Below is a list of IB courses that have transferred to Mount Allison in the past to give you an idea of the credits you may receive for successfully completed IB courses. An official transfer credit assessment will be completed for each individual upon the submission and receipt of the official International Baccalaureate Organization (IBO) transcript in early summer.   It is the student\'s responsibility to arrange for an official transcript to be sent directly from the IBO to Mount Allison University. The listing of credit transfers noted below does not guarantee the granting of credit in a specific situation as additional factors may apply. While every effort is made to ensure the currency and accuracy of the data found within the list below, errors may occur. It is the responsibility of the applicant to verify this information with the admitting institution. Not every IB course has been evaluated for credit transfer. Therefore if your courses do not appear in the list below, it may still be possible to receive credit for them. Please contact your admissions team for more information.    Mount Allison equivalencies of select IB courses        Arabic A Lang & Lit HL — 6 non-designated Arabic Language credits at the 1000 level (3 credits count as distribution under Arts) Biology HL — BIOL 1001 & BIOL 1501 (BIOL 1001 counts as distribution under Natural Science) Biology SL — 3 non-designated Biology credits at the 1000 level (counts as distribution under Natural Science) Business Management HL — COMM 1011 & 3 non-designated Commerce credits at the 2000 level Business Management SL — COMM 1011 Economics HL — ECON 1001 & ECON 1011 (3 credits from ECON 1001 or 1011 counts as distribution under Social World) Economics SL — 3 non-designated Economics credits at the 1000 level (counts as distribution under Social World) English A  Literature HL — ENGL 1201 & 3 non-designated English credits at the 1000 level (ENGL 1201 counts as distribution under Arts) English A Literature SL — 3 non-designated English credits at the 1000 level (counts as distribution under Arts) English A Language & Literature HL — ENGL 1201 & 3 non-designated English credits at the 1000 level (ENGL 1201 counts as distribution under Arts) English A Language & Literature SL — 3 non-designated English credits at the 1000 level (counts as distribution under Arts) Environment & Society SL — GENS 1401 (counts as distribution under Natural Science) French A Literature HL — 6 non-designated French Language credits at the 1000 level (3 credits count as distribution under Arts) French A Literature SL — 3 non-designated French Language credits at the 1000 level (counts as distribution under Arts) French A Language & Literature HL — 6 non-designated French Language credits at the 1000 level (3 credits count as distribution under Arts) French A Language & Literature SL — 3 non-designated French Language credits at the 1000 level (counts as distribution under Arts) French AB SL — 3 non-designated French Language credits at the 1000 level (counts as distribution under Arts) French B HL — 6 non-designated French Language credits at the 1000 level (3 credits count as distribution under Arts) French B SL — 3 non-designated French Language credits at the 1000 level (3 credits count as distribution under Arts) Geography HL — GENV 1201 & GENS 1401 (GENV 1201 counts as distribution under Social World; GENS 1401 counts as Natural Science) Geography SL — GENS 1401 (counts as distribution under Natural Science) Hindi B HL — 6 non-designated Hindi Language credits at the 1000 level (3 credits count as distribution under Arts) History of Africa & the Middle East HL — 6 non-designated History credits at the 1600 level (3 credits count as distribution under Humanities) History of the Americas HL — 6 non-designated History credits at the 1600 level (3 credits count as distribution under Humanities) History of Asia & Oceania HL — 6 non-designated History credits at the 1600 level (3 credits count as distribution under Humanities) History of Europe HL — 6 non-designated History credits at the 1600 level (3 credits count as distribution under Humanities) History SL — 3 non-designated History credits at the 1600 level (counts as distribution under Humanities) Italian B SL — 3 non-designated Italian Language credits at the 1000 level (counts as distribution under Arts) Mathematics HL — MATH 1111 & 3 non-designated Math credits at the 1000 level (MATH 1111 counts as distribution under Natural Science) Mathematics SL — MATH 1111 (counts as distribution under Natural Science) Norwegian B HL — 6 non-designated Norwegian Language credits at the 1000 level (counts as distribution under Arts) Philosophy HL — 6 non-designated Philosophy credits at the 1000 level Philosophy SL — 3 non-designated Philosophy credits at the 1000 level Physics HL — PHYS 1051 & PHYS 1551 (PHYS 1051 counts as distribution under Natural Science) Physics SL — 3 non-designated Physics credits at the 1000 level (counts as distribution under Natural Science) Psychology HL — PSYC 1011 & 3 non-designated Psychology credits at the 1000 level Psychology SL — 3 non-designated Psychology credits at the 1000 level Swahili B SL — 3 non-designated Swahili Language credits at the 1000 level (counts as distribution under Arts) Theory of Knowledge — 3 non-designated Elective credits at the 1000 level'
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
            if 'BMus' in degree_name:
                interview_desc_en = 'Students applying to the Bachelor of Music or Bachelor of Arts with honours/major in Music programs must submit an application for admission to the University as well as a Music Application Form to the Music Department. Bachelor of Music applicants are required to complete an audition. Applicants to the Bachelor of Music or Bachelor of Arts with honours/major in Music programs are required to complete a personal interview with the department. All applicants to the Music program (including Bachelor of Arts with minor in Music) must complete an entrance assessment. Music Application Forms are due February 10. For more information, visit the Music admissions pages.'
            #interview_desc_en = remove_tags(interview_desc_en)
            else:
                interview_desc_en = None
            # print(interview_desc_en
        except:
            interview_desc_en = None
            # print(interview_desc_en)

#36 作品集描述
        try:
            if 'BFA' in degree_name:
                portfolio_desc_en = 'Students applying to the Bachelor of Fine Arts or Bachelor of Arts with a major/minor in Fine Arts programs must submit an application for admission to the University as well as an Art Information Sheet, brief written statement, digital portfolio, and list of works to the Fine Arts Department. Fine Arts application packages are due February 15. For more information, visit the Fine Arts admission pages. '
            else:
                portfolio_desc_en =  None
            #portfolio_desc_en = remove_tags(portfolio_desc_en)
            # print(portfolio_desc_en
        except:
            portfolio_desc_en = None
            # print(portfolio_desc_en)

#37 other
        try:
            other = '没有课程时长字段'
            #other = remove_tags(other)
            # print(other)
        except:
            other = None
            # print(other)

        # sat act 代码 介绍
        sat_code = '0939'
        sat1_desc = 'Required: Senior-level English and a minimum of four additional university-preparatory courses. Pre-calculus is required for students applying to the Bachelor of Science or Commerce programs. SAT/ACT scores are not required for admissions purposes but students are encouraged to submit their results if available. '
        sat2_desc = None
        act_code = None
        act_desc = None

        item["ap"] = ap
        item["duration_per"] = 1
        item["duration"] = duration
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
        item["average_score"] = average_score

        #yield item


