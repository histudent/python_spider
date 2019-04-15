import scrapy
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from scrapySchool_Canada_Ben import getItem
from w3lib.html import remove_tags
import requests
import re
from lxml import etree
import time

class BaiduSpider(scrapy.Spider):
    name = 'Ontario_Institute_of_Technology_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['https://uoit.ca/programs/health-sciences/allied-health-sciences.php',
'https://uoit.ca/programs/science/applied-and-industrial-mathematics-regular-and-co-op.php',
'https://uoit.ca/programs/engineering-and-applied-science/automotive-engineering-automotive-engineering-and-management.php',
'https://uoit.ca/programs/science/biological-science-biological-science-and-management-regular-and-co-op.php',
'https://uoit.ca/programs/science/biological-science-advanced-entry.php',
'https://uoit.ca/programs/science/chemical-biology.php',
'https://uoit.ca/programs/science/chemistry-regular-and-co-op.php',
'https://uoit.ca/programs/business-and-information-technology/commerce.php',
'https://uoit.ca/programs/business-and-information-technology/commerce-pathways-program-advanced-entry.php',
'https://uoit.ca/programs/business-and-information-technology/commerce-pathways-program-bridge.php',
'https://uoit.ca/programs/social-science-and-humanities/communication.php',
'https://uoit.ca/programs/social-science-and-humanities/communication-advanced-entry.php',
'https://uoit.ca/programs/social-science-and-humanities/communication-and-digital-media-studies-gas-transfer.php',
'https://uoit.ca/programs/science/computer-science-regular-and-co-op.php',
'https://uoit.ca/programs/science/computer-science-diploma-to-degree.php',
'https://uoit.ca/programs/education/concurrent-education.php',
'https://uoit.ca/programs/social-science-and-humanities/criminology-and-justice.php',
'https://uoit.ca/programs/social-science-and-humanities/criminology-and-justice-advanced-entry.php',
'https://uoit.ca/programs/social-science-and-humanities/criminology-and-justice-gas-transfer.php',
'https://uoit.ca/programs/science/data-science.php',
'https://uoit.ca/programs/education/designing-adult-learning-for-the-digital-age.php',
'https://uoit.ca/programs/education/educational-studies-and-digital-technology .php',
'https://uoit.ca/programs/engineering-and-applied-science/electrical-engineering-electrical-engineering-and-management.php',
'https://uoit.ca/programs/science/environmental-biology.php',
'https://uoit.ca/programs/social-science-and-humanities/forensic-psychology.php',
'https://uoit.ca/programs/social-science-and-humanities/forensic-psychology-advanced-entry.php',
'https://uoit.ca/programs/social-science-and-humanities/forensic-psychology-gas-transfer.php',
'https://uoit.ca/programs/science/forensic-science.php',
'https://uoit.ca/programs/energy-systems-and-nuclear-science/health-physics-and-radiation-science.php',
'https://uoit.ca/programs/health-sciences/health-science.php',
'https://uoit.ca/programs/business-and-information-technology/information-technology-game-development-and-entrepreneurship-specialization.php',
'https://uoit.ca/programs/business-and-information-technology/information-technology-pathways-program-game-development-and-entrepreneurship-specialization-bridge.php',
'https://uoit.ca/programs/business-and-information-technology/information-technology-networking-and-information-technology-security-specialization.php',
'https://uoit.ca/programs/business-and-information-technology/information-technology-pathways-program-networking-and-information-technology-security-bridge.php',
'https://uoit.ca/programs/health-sciences/kinesiology.php',
'https://uoit.ca/programs/health-sciences/kinesiology-pathways.php',
'https://uoit.ca/programs/health-sciences/kinesiology-advanced-entry-ota-pta.php',
'https://uoit.ca/programs/social-science-and-humanities/legal-studies.php',
'https://uoit.ca/programs/social-science-and-humanities/legal-studies-advanced-entry.php',
'https://uoit.ca/programs/social-science-and-humanities/legal-studies-gas-transfer.php',
'https://uoit.ca/programs/social-science-and-humanities/liberal-studies.php',
'https://uoit.ca/programs/science/life-sciences-regular-and-co-op.php',
'https://uoit.ca/programs/engineering-and-applied-science/manufacturing-engineering-manufacturing-engineering-and-management.php',
'https://uoit.ca/programs/engineering-and-applied-science/mechanical-engineering-mechanical-engineering-and-management.php',
'https://uoit.ca/programs/engineering-and-applied-science/mechatronics-engineering.php',
'https://uoit.ca/programs/health-sciences/medical-laboratory-science.php',
'https://uoit.ca/programs/business-and-information-technology/information-technology-pathways-program-networking-and-information-technology-security-direct-entry.php',
'https://uoit.ca/programs/energy-systems-and-nuclear-science/nuclear-engineering.php',
'https://uoit.ca/programs/health-sciences/nursing-collaborative.php',
'https://uoit.ca/programs/health-sciences/nursing-post-rpn-barrie.php',
'https://uoit.ca/programs/health-sciences/nursing-post-rpn.php',
'https://uoit.ca/programs/science/pharmaceutical-chemistry.php',
'https://uoit.ca/programs/science/physics-regular-and-co-op.php',
'https://uoit.ca/programs/social-science-and-humanities/political-science.php',
'https://uoit.ca/programs/social-science-and-humanities/political-science-advanced-entry.php',
'https://uoit.ca/programs/social-science-and-humanities/political-science-gas-transfer.php',
'https://uoit.ca/programs/science/science-advanced-entry.php',
'https://uoit.ca/programs/engineering-and-applied-science/software-engineering-software-engineering-and-management.php',
'https://uoit.ca/programs/energy-systems-and-nuclear-science/sustainable-energy-systems.php',
'https://uoit.ca/programs/business-and-information-technology/technology-management.php',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        item = getItem.get_item(ScrapyschoolCanadaBenItem)



#1.学校名称
        school_name = 'University of Ontario Institute of Technology'

#2.地点
        try:
            location = response.xpath('//th[contains(text(),"Location")]/following-sibling::td').extract()[0]
            location = remove_tags(location)
            location = location.replace('                                                     ','')
            location = location.replace('                                                  ','')
            location = location.replace('UOIT, ','')
            #print(location)
        except:
            location = None
            #print(location)

#3. 校区
        try:
            campus = location

            #print(campus_list)
        except:
            campus_list = None
            #print(campus_list)

#4. 学院
        try:
            department = response.xpath('//th[contains(text(),"Faculty")]/following-sibling::td').extract()[0]
            department = remove_tags(department)
            department = department.replace('                                                     ','')
            department = department.replace('                                                  ','')
            #print(department)
        except:
            department = None
            #print(department)

# 4.
        try:
            degree_name_list = response.xpath('//th[contains(text(),"Degree")]/following-sibling::td').extract()[0]
            degree_name_list = remove_tags(degree_name_list)
            degree_name_list = degree_name_list.replace('                                                     ', '')
            degree_name_list = degree_name_list.replace('                                                   ', '')
            #degree_name_list = degree_name_list.replace('\n','')
            degree_name_list = degree_name_list.replace('                                                 ','')
            degree_name_list = degree_name_list.replace(' \n',':::')
            degree_name_list = degree_name_list.replace('\n','')
            #degree_name_list = degree_name_list.replace('\n','')
            #degree_name_list =
            degree_name_list = degree_name_list.rstrip(':::')
            degree_name_list = degree_name_list.split(':::')
            #print(degree_name_list)
        except:
            degree_name_list = ['None']
           # print(degree_name_list)

#5.学位描述
        try:
            degree_overview_en = response.xpath('//h2[contains(text(),"Additional information")]/preceding-sibling::*').extract()
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
            major_name_en = major_name_en.replace('\r\n','').replace('\n','')

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
            start_date = response.xpath('//th[contains(text(),"Start dates")]/following-sibling::td').extract()
            start_date = ','.join(start_date)
            start_date = remove_tags(start_date)
            if 'May' in start_date:
                start_date = '2019-05'
            elif 'May (part-time); and September (full-time)' in start_date:
                start_date = '2019-05,2019-09'
            elif 'Fall' in start_date:
                start_date = '2019-09'
            elif 'September' in start_date:
                start_date = '2019-09'

            #start_date = start_date.replace('Spring','').replace('Winter','').replace('Summer','').replace('Fall','')
            #start_date = start_date.replace('September 2019','2019-09').replace('May 2019','2019-05').replace('July 2019','2019-07').replace('January 2020','2020-01').replace('January 2019','2019-01')
           # print(start_date)
        except:
            start_date = None
           # print(start_date)

#9.课程长度
        try:
            duration = response.xpath('//th[contains(text(),"Length")]/following-sibling::td').extract()[0]
            duration = remove_tags(duration)
            if 'semesters' in duration:
                item["duration_per"] = '2'
            elif 'year' in duration:
                item["duration_per"] = '1'
            elif 'month' in duration:
                item["duration_per"] = '3'
            else:
                item["duration_per"] = '1'

            if 'Four or five' in duration:
                duration = '4,5'
            elif 'Four years/five years' in duration:
                duration = '4,5'
            elif 'two' in duration:
                duration = '2'
            elif 'Five' in duration:
                duration = '5'
            elif 'five' in duration:
                duration = '5'
            elif 'Four' in duration:
                duration = '4'
            elif 'three' in duration:
                duration = '3'
            elif 'Six' in duration:
                duration = '6'
            elif 'Two' in duration:
                duration = '2'

            #print(duration)
        except:
            duration = None
            #print(duration)


#10.课程设置
        Module_D = {"Academic Learning and Success":"826","Automotive Engineering":"827","Biology":"828","Business":"829","Chemistry":"831","Communication":"832","Computer Science":"833","Criminology and Justice":"861","Curriculum Studies":"834","Economics":"835","Education":"836","Educational Studies and Digital Technology":"825","Electrical Engineering":"837","Engineering":"838","Environmental Science":"839","Forensic Science":"840","Health Science":"841","Indigenous":"862","Information Technology":"842","Legal Studies":"843","Manufacturing Engineering":"844","Mathematics":"845","Mechanical Engineering":"846","Mechatronics":"860","Medical Laboratory Science":"847","Nuclear":"848","Nursing":"849","Physics":"850","Political Science":"851","Psychology":"852","Radiation Science":"853","Science":"855","Science Co-op":"854","Social Science":"858","Sociology":"856","Software Engineering":"857","Statistics":"859"}
        try:
                for key in Module_D:
                    #print(key)
                    if major_name_en in key or key in major_name_en:
                        cc = Module_D[key]
                       # print(cc)
                        url = "http://calendar.uoit.ca/content.php?filter%5B27%5D=-1&filter%5B29%5D=&filter%5Bcourse_type%5D="+ cc +"&filter%5Bkeyword%5D=&filter%5B32%5D=1&filter%5Bcpage%5D=1&cur_cat_oid=20&expand=&navoid=824&search_database=Filter&filter%5Bexact_match%5D=1#acalog_template_course_filter"
                        headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
                        response1 = requests.get(url,headers=headers)
                        modules_en = response1.text
                        response1 = etree.HTML(modules_en)
                        modules_en = response1.xpath('//td[@class = "width"]/a/text()')
                        modules_en = '<br>'.join(modules_en)

                        #print(major_name_en)
                       # print(modules_en)

                    else:
                        continue
                    print(modules_en)
        except:
            modules_en =   None

        if len(modules_en) <= 5:
            modules_en = response.xpath('//*[@id="tab_program_curriculum"]/ul/li').extract()
            modules_en = ''.join(modules_en)
            modules_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',modules_en)
        else:
            modules_en = modules_en

#11.就业方向
        try:
            career_en = response.xpath('//h2[contains(text(),"Career opportunities")]/following-sibling::ul').extract()[0]
            career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',career_en)
            #career_en = career_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
            #print(career_en)
        except:
            career_en = None
            #print(career_en)

#12.截止日期
        try:
            deadline = '2019-01-31'
            # deadline = response.xpath('//*[@id="Admissionrequirementsanddeadlines-subsection-0"]/table/tbody/tr/td[3]').extract()
            # deadline = '---'.join(deadline)
            # deadline = remove_tags(deadline)
            # deadline = deadline.replace('Documents due: ', '')
            # deadline =  deadline.replace('Sep 1, 2018Oct 1, 2018','2018-09-01').replace('Feb 1, 2019Mar 1, 2019','2019-02-01').replace('Mar 1, 2019Apr 1, 2019','2019-03-01').replace('May 1, 2019Jun 1, 2019','2019-05-01').replace('Sep 1, 2019Oct 1, 2019','2019-09-01').replace('Feb 15, 2019Mar 1, 2019','2019-02-15').replace('---',',')
            # #deadline = remove_tags(deadline)
            # #print(deadline)
        except:
            deadline = None
            #print(deadline)
#13.学费

#14 申请费:
        apply_fee = '130'

#15 申请要求
        try:
            entry_requirements_en = response.xpath('//h2[contains(text(),"Admission requirements")]/following-sibling::*').extract()
            entry_requirements_en = ''.join(entry_requirements_en)
            entry_requirements_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',entry_requirements_en)
            #print(entry_requirements_en)
        except:
            entry_requirements_en = None
            #print(entry_requirements_en)

#16 中国学生申请要求
        try:
            require_chinese_en = '<p>Senior Secondary School Graduation Certificate and Huikao, or similar provincial examination results. Applicants are required to submit both their academic transcript indicating all subjects taken and grades achieved and a copy of their graduation certificate and results. If your documents are issued in a language other than English, you must also provide notarized literal English translations.</p>'
            #require_chinese_en = remove_tags(require_chinese_en)
            # print(require_chinese_en)
        except:
            require_chinese_en = None
            # print(require_chinese_en)

#17 特殊专业要求
        try:
            specific_requirement_en = None
            # #specific_requirement_en = remove_tags(specific_requirement_en)
            # specific_requirement_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',specific_requirement_en)
            # specific_requirement_en = specific_requirement_en.replace('\r\n','')
            # specific_requirement_en = re.findall('Required high school classes(.*)2.',specific_requirement_en)[0]
            # specific_requirement_en = remove_tags(specific_requirement_en,keep=("li","ul"))
            #print(specific_requirement_en)
        except:
            specific_requirement_en = None
            #print(specific_requirement_en)

#18 高考(官网要求)
        try:
            gaokao_desc = None
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
            min_language_require = 'Overall score of 6.5 with no sub-score less than 6.0 (Education and Nursing programs require an overall score of 7.0).'
            min_language_require = remove_tags(min_language_require)
            # print(min_language_require)
        except:
            min_language_require = None
            # print(min_language_require)

#25 雅思要求
        try:
            ielts_desc = 'Overall score of 6.5 with no sub-score less than 6.0 (Education and Nursing programs require an overall score of 7.0).'
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
            toefl_code = '7178'
            #toefl_code = remove_tags(toefl_code)
            # print(toefl_code)
        except:
            toefl_code = None
            # print(toefl_code)

#29 toefl_desc
        try:
            toefl_desc = ' Internet-based test (iBT) with a total score of 83 (Education and Nursing programs require a total score of 87), and minimum scaled scores of Listening: 20; Reading: 20; Speaking: 19; and Writing: 20. The university\'s TOEFL code is 7178. Paper-delivered test results will be reviewed on an individual basis. '
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
        toefl_s = 19
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
            ib = 'Completion of the International Baccalaureate Diploma including English SL or HL. Prerequisite courses can be presented at the Standard or Higher Level with no score lower than 4.A minimum overall score of 24 is require for admission consideration; actual admitting scores vary from program to program.For Engineering and Science degrees, applicants must present Math SL or HL and/or Further Math HL (HL is recommended).Final IB results must be sent to the university electronically by the International Baccalaureate office.If you are not completing the full IB Diploma, individual IB courses may be considered for admission. Official transcripts and proof of high school graduation must be submitted directly from your institution.'
            #print(ib)
        except:
            ib = None
            #print(ib)

#34 ap
        try:
            ap = 'Prerequisite courses, including English, should be presented at Grade 12/Senior Year/College Prep/Honors level, SAT Subject Tests or Advanced Placement (APl) exam results.'
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
        sat_code = '4192 '
        sat1_desc = 'SAT or ACT scores should also be submitted if written. The university\'s SAT code is 4192 and the ACT code is 5265.'
        sat2_desc = None
        act_code = '5265'
        act_desc = 'SAT or ACT scores should also be submitted if written. The university\'s SAT code is 4192 and the ACT code is 5265.'

        item["ap"] = ap
        #item["duration_per"] = duration_per
        item["duration"] = duration
        item["school_name"] = school_name
        item["location"] = location
        item["campus"] = campus
        #item["degree_type"] = 1
        item["department"] = department
        #item["degree_name"] = degree_name
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

        for i in degree_name_list:
            degree_name = i
            item["degree_name"] = degree_name
            if 'Bachelor of Engineering' in degree_name:
                item["tuition_fee"] = '26,007.42'
            elif 'Information Technology' in degree_name:
                item["tuition_fee"] = '23,091.20'
            elif 'Bachelor of Commerce' in degree_name:
                item["tuition_fee"] = '22,118.62'
            elif 'Nursing' in degree_name:
                item["tuition_fee"] = '20,333.88'
            elif 'Computer Science' in degree_name:
                item["tuition_fee"] = '21,131.22'
            else:
                item["tuition_fee"] = '19,940.96'
            #print(item["tuition_fee"])
            yield item
#

