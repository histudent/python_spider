import scrapy
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from scrapySchool_Canada_Ben import getItem
from w3lib.html import remove_tags
import re



class BaiduSpider(scrapy.Spider):
    name = 'University_of_Western_Ontario_U'
    start_urls = ['http://welcome.uwo.ca/programs/programs_by_faculty/index.html']
    def parse(self, response):

        urlList=response.xpath('//div[4]/p/a/@href').extract()
        degree = response.xpath('//div[4]/p').extract()
        depart = response.xpath('//div[4]/h2').extract()
        #print(urlList)
        #print(degree)
        for uL,dz,de in zip(urlList,degree,depart):
            uL  = 'http://welcome.uwo.ca/programs/programs_by_faculty/' + uL
            #print(uL)
            yield scrapy.Request(url=uL, callback=self.parses,meta={"degree":dz,"depart":de})
    def parses(self, response):
        item = getItem.get_item(ScrapyschoolCanadaBenItem)

#1.学校名称
        degree = response.meta['degree']
        #degree = remove_tags(degree)
        depart = response.meta["depart"]
        depart = remove_tags(depart)
       # print(depart)
       # print(degree)
        school_name = 'University of Western Ontario'

#2.地点
        try:
            location = 'London,Canada'
            location = re.findall('\((.*)\)',location)[0]
            #print(location)
        except:
            location = None
            #print(location)

#3. 校区
        try:
            campus = 'main campus'
            #campus = remove_tags(campus)
            #campus = campus.replace(', Online','')
            #campus = campus.replace(' ','')
            #campus = campus.split(',')
            #print(campus)
        except:
            campus = None
            #print(campus)

#4. 学院
        try:
            department = depart
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
#         try:
#             degree_name_list = response.xpath('//a[contains(text(),"Degrees")]/../following-sibling::div[1]').extract()
#             degree_name_list = ''.join(degree_name_list)
#             degree_name_list = remove_tags(degree_name_list)
#             degree_name_list = degree_name_list.replace('\xa0','')
#             degree_name_list = degree_name_list.replace('\n\n','')
#             degree_name_list = degree_name_list.split('\n')
#             #degree_name_list = filter(None, degree_name_list)
#             if '' in degree_name_list:
#                 degree_name_list = ['Bachelor of Science in Nursing (BScN)']


            #degree_name = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_name_list)
            #degree_name = degree_name.replace('\t','').replace('\n','').replace('\xa0','').replace(' class="list-inline uofs-cta-list','')
            # degree_name = degree_name.replace('<li>','').replace('</li>','---')
            # degree_name = degree_name.replace('<span>','').replace('</span>','---')
            #degree_name = degree_name.split('</li><li>')
           # print(degree_name_list)
        #    # print(response.url)
        #     #print(response.url)
        # except:
        #
        #     degree_name_list = None
        #    # print(degree_name_list)

#5.学位描述
        try:
            degree_overview_en = degree
            #degree_overview_en = ''.join(degree_overview_en)
            # #degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_overview_en)
            # degree_overview_en = re.sub('<p(https:.*)">?','',degree_overview_en)
            degree_overview_en = degree_overview_en.replace('<br><a><img> Learn more</a></p>','')
            # degree_overview_en = degree_overview_en.replace('https://www.ualberta.ca/campus-saint-jean"','')
            # degree_overview_en = degree_overview_en.replace('https://www.ualberta.ca/en/campus-saint-jean"','')
            # degree_overview_en = degree_overview_en.replace(' xmlns=""','')
            # #degree_overview_en = degree_overview_en.replace('https://www.ualberta.ca/arts"','')
            # #degree_overview_en = degree_overview_en.replace('\r\n','')
            # degree_overview_en = degree_overview_en.replace('\n','')
            # #degree_overview_en = degree_overview_en.replace('\n','')
            # #degree_overview_en = degree_overview_en.replace('  ',' ')
            # degree_overview_en = degree_overview_en.replace('                           ','')
            # degree_overview_en = degree_overview_en.replace('   ','')
            #print(degree_overview_en)
        except:
            degree_overview_en = None
            #print(degree_overview_en)
        #//*[@id="page-content"]/div[3]/div[1]/*

#6.专业英文
        try:
            major_name_en_list = response.xpath('//div[4]/div/div[1]/ul').extract()
            major_name_en_list = ''.join(major_name_en_list)
            #major_name_en = major_name_en.replace('\r\n','').replace('\n','').replace('           ','').replace('\t','').replace('     ','')
            #major_name_en_list = remove_tags(major_name_en_list)
            major_name_en_list = major_name_en_list.replace('\n','').replace('<ul><li>','').replace('</li></ul>','').replace('<ul class="squarelist"><li>','')
            major_name_en_list = major_name_en_list.split('</li><li>')
            #print(major_name_en_list)
        except:
            major_name_en_list = None
            #print(major_name_en_list)


        try:
            degree_name_li = response.xpath('//div[4]/div/div[2]/ul').extract()
            degree_name_li = ''.join(degree_name_li)
            #major_name_en = major_name_en.replace('\r\n','').replace('\n','').replace('           ','').replace('\t','').replace('     ','')
            #degree_name_li = remove_tags(degree_name_li)
            degree_name_li = degree_name_li.replace('\n','').replace('<ul><li>','').replace('</li></ul>','').replace('<ul class="squarelist"><li>','')
            degree_name_li = degree_name_li.split('</li><li>')
            #print(degree_name_li)
        except:
            degree_name_li = None
            #print(degree_name_li)


#7.专业介绍
        try:
            overview_en = degree_overview_en
            # overview_en = response.xpath('').extract()
            # overview_en = ''.join(overview_en)
            # overview_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',overview_en)

            # print(overview_en)
        except:
            overview_en = degree_overview_en
            # print(overview_en)

#8.入学时间
        try:
            start_date = '2019-09'
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
            if 'medical_sciences.html' in response.url:
                modules_en = '<div><p><strong><a>There are 6 Specialization modules </a></strong>available in the BMSc Program and only students registered in Years 3 and 4 BMSc may register in these modules.</p><p><strong>NOTE:</strong> Very few students pursue the Specialization modules since these modules lead only to non-honors BMSc degrees. Since most students in the BMSc Program meet and/or exceed the marks/averages required to register in Honors degrees, students are strongly encouraged to pursue either Honors Specialization modules or Double Majors.</p><p>Enrollment in the Specialization modules is <strong>not</strong> limited as none of these modules contain a capstone course in Year 4</p><ul><li>the 4000-level capstone courses (<strong><a>Research Projects</a></strong> and <strong><a>Medical Sciences 4900F/G + 4930F/G</a></strong>) <strong>cannot be taken by students in the Specialization modules</strong></li><li>see <strong><a>Admission to Year 3 BMSc</a></strong> and <strong><a>Admission to Year 4 BMSc</a></strong> for information about admission to the Specialization modules in Years 3 and 4</li></ul><p>See the <strong><a>Academic Calendar</a></strong> for the complete listing of modules offered by the basic medical science departments</p></div>'
            else:
                modules_en = None
        except:
            modules_en = None
            #print(modules_en)

#11.就业方向
        try:
            if 'medical_sciences.html' in response.url:
                career_en = '<p>Students with a BMSc degree can contribute to society in a variety career opportunities including professional programs, academic and other research institutions, and industry. A large proportion of the graduates of this program choose a career in Medicine, Dentistry or Graduate Studies. Others enter professional programs such as Pharmacy, Optometry, Law, Education, Physiotherapy, Occupational Therapy and Nursing.</p><p>Each year BMSc graduates are surveyed to determine their career plans for the upcoming September.  The following chart summarizes the responses from 238 of the 344 (70%) BMSc students who graduated in June 2017.</p>'
            else:
                career_en = None
        except:
            career_en = None
            #print(career_en)

#12.截止日期
        try:
            deadline = '2019-02-15'
            #deadline = response.xpath('//h3[contains(text(),"Deadline")]/following-sibling::p[1]').extract()[0]
            #deadline = remove_tags(deadline)
            #deadline = deadline.replace('Documents due: ', '')
            #deadline = remove_tags(deadline)
            #print(deadline)
        except:
            deadline = None
            #print(deadline)
#13.学费
        # try:
        #     abaa = 'https://apps.admissions.ualberta.ca/costcalculator/faculties/%s/international/off-campus?pttool=true'
        #     acc = response.xpath('//*[@id="get-program-costs"]/@href').extract()[0]
        #     acc = re.findall('\d',acc)[0]
        #     #print(acc)
        #     url = abaa % acc
        #     #print(url)
        #     headers = {
        #         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        #     response1 = requests.get(url,headers=headers)
        #     #print(response1.text)
        #     tuition_fee = response1.text
        #     tuition_fee = remove_tags(tuition_fee)
        #     tuition_fee = tuition_fee.replace('\n','').replace('\r\n','').replace('                           ','')
        #     tuition_fee = re.findall('\$(\d+\.\d+)',tuition_fee)[0]
        #     #print(tuition_fee)
        # except:
        #     tuition_fee = None
        #     #print(tuition_fee)
#14 申请费:
        apply_fee = '156'

#15 申请要求
        try:

            entry_requirements_en = '<ol><li><p><strong>Academic transcript of Senior Secondary</strong> indicating all subjects taken and grades earned.</p><p>Applicants may be considered for conditional admission on the basis of mid-year/mid-term results.&nbsp; Mid-year results and a secondary school transcript must be submitted directly to Western from the institutions attended.&nbsp; If you are issued a conditional offer of admission, you will be required to have your final official academic transcript, Graduation Examinations, and University Entrance Examinations sent directly from the proper issuing authority along with word-for-word English translations, to World Education Services (WES) Canada for authentication and verification.**</p></li><li><p><strong>Senior Secondary Graduation Diploma</strong></p></li><li><p><strong>General Education Examination results (Graduation Exams/ Hui Kao/Xuéyé Shuiping Cèshi/Academic Proficiency Test).</strong>&nbsp; For provinces that do not administer or are exempt from taking the general education examinations, a letter from your Senior Secondary verifying the schools and/or provinces examination policy is required.</p></li><li><p><strong>Chinese University Entrance Examination (NCEE / Gao Kao)</strong></p></li><li><p><strong>Proof of English language proficiency.</strong> &nbsp;Test results must be issued directly to Western from the Examining Board. &nbsp;Western\'s institution code is 0984. Please review .</p></li><li><p><strong>Refer to the&nbsp;content below for program specific required and recommended courses. &nbsp;Course prerequisites should be presented at the senior level:</strong></p></li></ol>'
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
            require_chinese_en = '<ol><li><p><strong>Academic transcript of Senior Secondary</strong> indicating all subjects taken and grades earned.</p><p>Applicants may be considered for conditional admission on the basis of mid-year/mid-term results.&nbsp; Mid-year results and a secondary school transcript must be submitted directly to Western from the institutions attended.&nbsp; If you are issued a conditional offer of admission, you will be required to have your final official academic transcript, Graduation Examinations, and University Entrance Examinations sent directly from the proper issuing authority along with word-for-word English translations, to World Education Services (WES) Canada for authentication and verification.**</p></li><li><p><strong>Senior Secondary Graduation Diploma</strong></p></li><li><p><strong>General Education Examination results (Graduation Exams/ Hui Kao/Xuéyé Shuiping Cèshi/Academic Proficiency Test).</strong>&nbsp; For provinces that do not administer or are exempt from taking the general education examinations, a letter from your Senior Secondary verifying the schools and/or provinces examination policy is required.</p></li><li><p><strong>Chinese University Entrance Examination (NCEE / Gao Kao)</strong></p></li><li><p><strong>Proof of English language proficiency.</strong> &nbsp;Test results must be issued directly to Western from the Examining Board. &nbsp;Western\'s institution code is 0984. Please review .</p></li><li><p><strong>Refer to the&nbsp;content below for program specific required and recommended courses. &nbsp;Course prerequisites should be presented at the senior level:</strong></p></li></ol>'
            #require_chinese_en = remove_tags(require_chinese_en)
            # print(require_chinese_en)
        except:
            require_chinese_en = None
            # print(require_chinese_en)

#17 特殊专业要求
        # try:
        #     specific_requirement_en = response.xpath('//div[@class = "row-fluid required-courses"]').extract()
        #     specific_requirement_en = ''.join(specific_requirement_en)
        #     specific_requirement_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',specific_requirement_en)
        #     #print(specific_requirement_en)
        # except:
        #     specific_requirement_en = None
        #     #print(specific_requirement_en)

#18 高考(官网要求)
        try:
            gaokao_desc = 'General Education Examination results (Graduation Exams/ Hui Kao/Xuéyé Shuiping Cèshi/Academic Proficiency Test).  For provinces that do not administer or are exempt from taking the general education examinations, a letter from your Senior Secondary verifying the schools and/or provinces examination policy is required.'
            #gaokao_desc = remove_tags(gaokao_desc)
            # print(gaokao_desc)
        except:
            gaokao_desc = None
            # print(gaokao_desc)

#19 高考(展示以及判断字段)
        try:
            gaokao_zs = None
            #gaokao_zs = remove_tags(gaokao_zs)
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
            huikao_desc = 'General Education Examination results (Graduation Exams/Hui Kao/Xuéyé Shuiping Cèshi/Academic Proficiency Test).  For provinces that do not administer or are exempt from taking the general education examinations, a letter from your Senior Secondary verifying the schools and/or provinces examination policy is required.'
            #huikao_desc = remove_tags(huikao_desc)
            # print(huikao_desc)
        except:
            huikao_desc = None
            # print(huikao_desc)

#23 会考描述
        try:
            huikao_zs = 'General Education Examination results (Graduation Exams/ Hui Kao/Xuéyé Shuiping Cèshi/Academic Proficiency Test).  For provinces that do not administer or are exempt from taking the general education examinations, a letter from your Senior Secondary verifying the schools and/or provinces examination policy is required.'
            huikao_zs = remove_tags(huikao_zs)
            # print(huikao_zs)
        except:
            huikao_zs = None
            # print(huikao_zs)

#24 最低语言要求
        try:
            min_language_require = 'IELTS Academic is required with a minimum overall band score of 6.5 with no part less than 6.0.'
            min_language_require = remove_tags(min_language_require)
            # print(min_language_require)
        except:
            min_language_require = None
            # print(min_language_require)

#25 雅思要求
        try:
            ielts_desc = 'At least 6.5 with no band less than 5.5'
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
            toefl_code = '0984'
            #toefl_code = remove_tags(toefl_code)
            # print(toefl_code)
        except:
            toefl_code = None
            # print(toefl_code)

#29 toefl_desc
        try:
            toefl_desc = 'The minimum score required on the TOEFL is 550 on the paperbased with a 5 on the TWE, and 83 on the internet-based tests with no score below 20.'
            #toefl_desc = remove_tags(toefl_desc)
            # print(toefl_desc)
        except:
            toefl_desc = None
            # print(toefl_desc)

#30 toefl
        try:
            toefl = '83'
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
            alevel = ''
            #alevel = remove_tags(alevel)
            # print(alevel)
        except:
            alevel = None
            # print(alevel)

#33 ib
        try:
            ib = 'If you are currently completing the International Baccalaureate program, you must complete the full International Baccalaureate Diploma including each of the following to be considered for admission:<br>Completion of the entire Diploma including the Theory of Knowledge and Extended Essay<br>Passes in a minimum of 6 subjects of which 3 must be at the Higher Level<br>A minimum grade total of 28 including points awarded for the Extended Essay and Theory of Knowledge<br>No mark less than 4 on any individual course<br>Prerequisites for your program as specified by Western <br>Please note the minimum grade total quoted is the minimum required for admission consideration. Competitive admission based on predicted results is usually in the low to mid 30\'s and can vary depending on the program.<br>Applications should be submitted in the Fall prior to the year in which you are seeking admission.'
            #print(ib)
        except:
            ib = None
            #print(ib)

#34 ap
        try:
            specific_requirement_en = ''
            #ap = remove_tags(ap)
            # print(ap)
        except:
            specific_requirement_en = None
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
            other = '1.页面需要从列表页跳转,列表页有专业和学位介绍,2,详情页需要拆开专业和学位3.课程,就业,特殊专业要求字段,学费字段 需要跳转到各自页面根据列表页信息做匹配.4,后期需要手动补充课程确实字段.因其每个专业课程字段所在页面不同'
            #other = remove_tags(other)
            # print(other)
        except:
            other = None
            # print(other)

        # sat act 代码 介绍
        sat_code = '0984'
        sat1_desc = 'SAT Reasoning Test results submitted directly to Western by the College Board.  Western\'s institution number is 0984. A minimum SAT combined Evidence Based Reading and Writing + Math score of 1190 is required for admission consideration.'
        sat2_desc = None
        act_code = '4837'
        act_desc = ' ACT Test results submitted directly to Western by ACT Institutional Services.  Western\'s institution number is 4837. A minimum ACT composite score of 24 is required for admissions consideration'

       # item["ap"] = ap
        item["duration_per"] = 1
        item["school_name"] = school_name
        item["location"] = location
        item["campus"] = campus
        #item["degree_type"] = 1
        item["department"] = department
       #item["degree_name"] = degree_name
        item["degree_overview_en"] = degree_overview_en
        #item["major_name_en"] = major_name_en
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
        #item["tuition_fee"] = tuition_fee
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
        item["gaokao_desc"] = gaokao_desc
        #item["duration"] = '4'

        if '/science.html' in response.url:
            degree_name = 'BA/BSc'
            tuition_fee = '28,743.00'
            ap = '<div><p><strong>Recommended<span>&nbsp;</span>Prerequisites</strong></p><ul><li>Senior Level Calculus</li></ul><p><span>Notes:</span><br><span>▪&nbsp; First year Biology and Chemistry courses require Grade 12 Biology and Chemistry, respectively. First year Biology and Chemistry courses are required for ALL modules offered by the Department of Biology and for some modules offered by the Department of Chemistry and other Science departments.<br></span><span>▪&nbsp; It is strongly recommended that applicants complete a Grade 12 math course.</span><span>&nbsp;</span></p></div>'
        elif 'arts_and_humanities.html' in response.url:
            degree_name = 'BA'
            tuition_fee = '28,743.00'
            ap = 'No course prerequisites'
        elif 'engineering.html' in response.url:
            degree_name = 'BSc'
            tuition_fee = '36,886.00'
            ap = '<div><p><strong>Required Prerequisites</strong></p><ul><li>Senior Level Calculus</li><li>Senior Level Chemistry</li><li>Senior Level Physics</li></ul><p><strong>Secondary School course descriptions/syllabi</strong> may be requested from applicants to certain programs/faculties at Western for assessment of prerequisite course requirements. Applicants will be notified of this requirement at the point of application review and acknowledgement by the Undergraduate Admissions Office.</p></div>'
        elif 'health_studies.html' in response.url:
            degree_name = 'BHSc'
            tuition_fee = '28,743.00'
            ap = '<div><p><strong>Required<span> </span>Prerequisites</strong></p><ul><li>Senior Level Biology</li><li>Senior Level&nbsp;Math (Recommended)</li></ul><p>Note: Students considering the Honors Specialization in Health Sciences with Biology will need Grade 12 Chemistry in order to fulfill the first year Chemistry requirements of the module.</p><p><strong>Secondary School course descriptions/syllabi</strong> may be requested from applicants to certain programs/faculties at Western for assessment of prerequisite course requirements. Applicants will be notified of this requirement at the point of application review and acknowledgement by the Undergraduate Admissions Office.</p></div>'
        elif 'kinesiology.html' in response.url:
            degree_name = 'BA/BSc'
            tuition_fee = '28,743.00'
            ap = '<div><p><strong>Required Prerequisites</strong></p><ul><li>Senior Level&nbsp;Biology</li></ul><p>Notes:<br><span>▪&nbsp;A Grade 12 Math and Grade 11 or 12 Physics are recommended to prepare for senior Kinesiology subjects in biomechanics, research methods, and statistics.<br></span><span>▪&nbsp;</span>It is strongly recommended that students interested in the BSc program take Grade 12 Science courses such as: Chemistry, Calculus, Pre-Calculus Math, or Physics.<br><span>▪&nbsp;</span>Grade 12 Chemistry is a prerequisite for first year Chemistry courses.</p><p><strong>Secondary School course descriptions/syllabi</strong> may be requested from applicants to certain programs/faculties at Western for assessment of prerequisite course requirements. Applicants will be notified of this requirement at the point of application review and acknowledgement by the Undergraduate Admissions Office.</p></div>'
        elif 'nursing.html' in response.url:
            degree_name = 'BSc'
            tuition_fee = '36,886.00'
            ap = '<div><p><strong>Required Prerequisites</strong></p><ul><li>Senior Level&nbsp;Biology</li><li>Senior Level Chemistry</li><li>Senior Level English</li><li>Senior Level Math</li></ul><p><strong>Secondary School course descriptions/syllabi</strong> may be requested from applicants to certain programs/faculties at Western for assessment of prerequisite course requirements. Applicants will be notified of this requirement at the point of application review and acknowledgement by the Undergraduate Admissions Office.</p></div>'
        elif 'information_and_media_studies.html' in response.url:
            degree_name = 'BA'
            tuition_fee = '28,743.00'
            ap = 'No course prerequisites'
        elif 'music.html' in response.url:
            degree_name = 'BA'
            tuition_fee = '28,743.00'
            ap = '<div><ul><li>No course prerequisites</li></ul><p>Faculty recommendation required based on <a>Audition, Interview, Piano Proficiency and Theory Placement</a> results.</p><p>Note:&nbsp; A senior level math course is recommended for applicants to Music Administrative Studies.</p></div>'
        elif 'medical_sciences.html' in response.url:
            degree_name = 'BMSc'
            tuition_fee = '28,743.00'
            ap = '<div><p><strong>Recommended<span>&nbsp;</span>Prerequisites</strong></p><ul><li>Senior Level Biology</li><li>Senior Level Calculus</li><li>Senior Level Chemistry</li></ul><p><span>Notes:</span><br><span>▪ First year Biology and Chemistry courses require Grade 12 Biology and Chemistry, respectively. First year Biology and Chemistry courses are required for ALL modules offered in the Bachelor of Medical Sciences and Neurosciences programs.<br></span><span>▪ Although Western offers first year Physics courses that do not require Grade 12 Physics as a prerequisite, it is strongly recommended that you complete&nbsp;Grade 12 Physics.</span>&nbsp;</p></div>'
        elif 'social_science.html' in response.url:
            degree_name = 'BA/BSc'
            tuition_fee = '28,743.00'
            ap = '<div><ul><li>No course prerequisites</li></ul><p><span>Notes:</span><br><span>▪&nbsp;</span>All Specializations and Majors in Psychology requires a first-year university Math course, therefore any Grade 12 level academic Math is highly recommended for this program.<br><span>▪&nbsp;</span>Math is helpful as preparation for Sociology and Geography programs.<br><span>▪&nbsp;</span>A Grade 12 Pre-Calculus Math and a Grade 12 Calculus (equivalent to Ontario Grade 12 Advanced Functions and Grade 12 Calculus) are required for all Economics modules.<br><span>▪&nbsp;</span>Grade 12 Biology, Chemistry, and Physics are highly recommended for the BSc in Psychology.</p></div>'
        elif 'management_and_organizational_studies.html' in response.url:
            degree_name = 'BMOS'
            tuition_fee = '34,474.00'
            ap = '<div><p><strong>Recommended Prerequisites</strong></p><ul><li>Senior Level&nbsp;Math</li></ul><p>Note: For Management &amp; Organizational Studies&nbsp;a Grade 12 Calculus and/or a university Calculus course is required prior to taking mandatory upper-year Economics courses in Finance, and pursuing a Major or Honors Specialization in Economics.</p></div>'
        else:
            degree_name = None
            tuition_fee = None
            ap = None
            re.findall("/\\d\d\d\d\d")
        #item["degree_name"] = degree_name
        item["tuition_fee"] = tuition_fee
        item["ap"] = ap

        for acd in major_name_en_list:
            major_name_en = acd
            item["major_name_en"] = major_name_en
            #print(major_name_en)
            for bbc in degree_name_li:
                degree_name = bbc
                item["degree_name"] = degree_name
                #print(degree_name)
                if '3' in degree_name and '4' in degree_name:
                    item["duration"] = '3,4'
                elif '4' in degree_name:
                    item["duration"] = '4'
                elif '3' in degree_name:
                    item["duration"] = '3'
                else:
                    item["duration"] = '123'
                #print(item["duration"])
                if '123' not in item["duration"] and 'jointly' not in degree_name and 'Double' not in degree_name and 'Certificate' not in degree_name and 'minor' not in degree_name and 'After degree' not in degree_name:

                    yield item
            #yield item
#

