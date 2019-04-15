import scrapy
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from scrapySchool_Canada_Ben import getItem
from w3lib.html import remove_tags
import re
import urllib.request
import time

class BaiduSpider(scrapy.Spider):
    name = 'university_of_guelph_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
#     C = ['https://admission.uoguelph.ca/basc/adev',
# 'https://admission.uoguelph.ca/bcom/acct',
# 'https://admission.uoguelph.ca/bsc/abio',
# 'https://admission.uoguelph.ca/bscag/ansc',
# 'https://admission.uoguelph.ca/ba/anth',
# 'https://admission.uoguelph.ca/basc/ahn',
# 'https://admission.uoguelph.ca/ba/arth',
# 'https://admission.uoguelph.ca/bsc/bioc',
# 'https://admission.uoguelph.ca/bsc/biod',
# 'https://admission.uoguelph.ca/bsc/biomp',
# 'https://admission.uoguelph.ca/bsc/bpc',
# 'https://admission.uoguelph.ca/beng/bioe',
# 'https://admission.uoguelph.ca/bsc/bios',
# 'https://admission.uoguelph.ca/beng/biomed',
# 'https://admission.uoguelph.ca/bsc/biotox',
# 'https://admission.uoguelph.ca/bsc/biom',
# 'https://admission.uoguelph.ca/bsc/chpy',
# 'https://admission.uoguelph.ca/bsc/chem',
# 'https://admission.uoguelph.ca/basc/cyf',
# 'https://admission.uoguelph.ca/ba/clas',
# 'https://admission.uoguelph.ca/beng/compeng',
# 'https://admission.uoguelph.ca/bcomp/csci',
# 'https://admission.uoguelph.ca/ba/cjpp',
# 'https://admission.uoguelph.ca/bscag/chts',
# 'https://admission.uoguelph.ca/bscenv/ecol',
# 'https://admission.uoguelph.ca/ba/econ',
# 'https://admission.uoguelph.ca/beng/esc',
# 'https://admission.uoguelph.ca/ba/engl',
# 'https://admission.uoguelph.ca/bscenv/erm',
# 'https://admission.uoguelph.ca/bsc/envb',
# 'https://admission.uoguelph.ca/bscenv/eep',
# 'https://admission.uoguelph.ca/beng/enve',
# 'https://admission.uoguelph.ca/bsc/egg',
# 'https://admission.uoguelph.ca/ba/eg',
# 'https://admission.uoguelph.ca/bbrm/em',
# 'https://admission.uoguelph.ca/bscenv/envsci',
# 'https://admission.uoguelph.ca/bbrm/eqm',
# 'https://admission.uoguelph.ca/ba/eurs',
# 'https://admission.uoguelph.ca/ba/fare',
# 'https://admission.uoguelph.ca/bcom/fab',
# 'https://admission.uoguelph.ca/bbrm/fim',
# 'https://admission.uoguelph.ca/bsc/food',
# 'https://admission.uoguelph.ca/ba/fren',
# 'https://admission.uoguelph.ca/bagen',
# 'https://admission.uoguelph.ca/ba/geog',
# 'https://admission.uoguelph.ca/ba/hist',
# 'https://admission.uoguelph.ca/bscag/agrs',
# 'https://admission.uoguelph.ca/bcom/htm',
# 'https://admission.uoguelph.ca/bsc/hk',
# 'https://admission.uoguelph.ca/ba/id',
# 'https://admission.uoguelph.ca/ba/und',
# 'https://admission.uoguelph.ca/bcom/man',
# 'https://admission.uoguelph.ca/bcom/mef',
# 'https://admission.uoguelph.ca/bsc/mfb',
# 'https://admission.uoguelph.ca/bcom/mkmn',
# 'https://admission.uoguelph.ca/ba/maec',
# 'https://admission.uoguelph.ca/ba/msci',
# 'https://admission.uoguelph.ca/beng/me',
# 'https://admission.uoguelph.ca/bsc/micr',
# 'https://admission.uoguelph.ca/bsc/mbg',
# 'https://admission.uoguelph.ca/ba/musc',
# 'https://admission.uoguelph.ca/bsc/nano',
# 'https://admission.uoguelph.ca/bsc/neuro',
# 'https://admission.uoguelph.ca/bsc/nans',
# 'https://admission.uoguelph.ca/ba/phil',
# 'https://admission.uoguelph.ca/bsc/psci',
# 'https://admission.uoguelph.ca/bsc/phys',
# 'https://admission.uoguelph.ca/bsc/plsc',
# 'https://admission.uoguelph.ca/ba/pols',
# 'https://admission.uoguelph.ca/ba/psyc',
# 'https://admission.uoguelph.ca/bcom/pmgt',
# 'https://admission.uoguelph.ca/bcom/reh',
# 'https://admission.uoguelph.ca/ba/shs',
# 'https://admission.uoguelph.ca/ba/soc',
# 'https://admission.uoguelph.ca/bcomp/se',
# 'https://admission.uoguelph.ca/ba/sart',
# 'https://admission.uoguelph.ca/ba/the',
# 'https://admission.uoguelph.ca/bsc/thpy',
# 'https://admission.uoguelph.ca/bcom/und',
# 'https://admission.uoguelph.ca/beng/und',
# 'https://admission.uoguelph.ca/beng/wre',
# 'https://admission.uoguelph.ca/bsc/wlbc',
# 'https://admission.uoguelph.ca/bsc/zoo',]

    C = [
'https://admission.uoguelph.ca/bla',]
    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        item = getItem.get_item(ScrapyschoolCanadaBenItem)



#1.学校名称
        school_name = 'University of Guelph'

#2.地点
        try:
            location = response.xpath('//*[@id="feature"]/div/p/img/@alt').extract()[0]
            location = remove_tags(location)
            location = location.split(',')
            location = location[-2] + ',' + location[-1]
            location = location.replace(', ',',')
            location = location.lstrip(' ')
            #location = re.findall(',(.*?),.*\.',location)[0]
            #print(location)
        except:
            location = None
            #print(location)

#3. 校区
        try:
            campus = response.xpath('//*[@id="feature"]/div/p/img/@alt').extract()[0]
            campus = remove_tags(campus)
            campus = campus.split(',')
            campus = campus[-2]
            campus = campus.lstrip(' ')
           # print(campus)
        except:
            campus = None
            #print(campus)

#4. 学院
        try:
            department = response.xpath('//*[@id="content"]/ul[2]/li/a').extract()[0]
            department = remove_tags(department)
            department = department.replace(' - Art History','')
            #print(department)
        except:
            department = None
            #print(department)

# 4. 学位名称列表,需要拆分,在下方yield 处写循环.此处是拆分存入列表
    #'https://www.lakeheadu.ca/academics/undergraduate-programs/engineering'特殊情况
        #'https://www.lakeheadu.ca/academics/undergraduate-programs/forestry'
        try:
            degree_name = response.xpath('//*[@id="feature"]/div/p/img/@alt').extract()[0]
            degree_name = remove_tags(degree_name)
            #degree_name = degree_name.replace('<br>','---')
            #degree_name = degree_name.replace('<li>','').replace('</li>','---')
            degree_name = re.findall(',(.*?),.*\.',degree_name)[0]
            degree_name = degree_name.replace(' B','B')
          #  degree_name = degree_name.split('---')
           # print(degree_name)
        except:

            degree_name = None
          #  print(degree_name)

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
            major_name_en = response.xpath('//*[@id="content"]/h1').extract()[0]
            major_name_en = remove_tags(major_name_en)
            major_name_en = major_name_en.replace('amp;','')
            #print(major_name_en)
        except:
            major_name_en = None

           # print(major_name_en)

#7.专业介绍
        try:
            overview_en = response.xpath('//*[@id="content"]/p').extract()
            overview_en = ''.join(overview_en)
            overview_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',overview_en)
            overview_en = overview_en.replace('<p><strong>Also available in co-op.</strong></p>','')
            overview_en = overview_en.replace('<p>For more information, please visit:</p>','')
            overview_en = overview_en.replace('<strong>Also available in co-op. </strong>','')
            overview_en = overview_en.replace('For more information, please visit:','')
           # print(overview_en)
        except:
            overview_en = degree_overview_en
           # print(overview_en)

# #8.入学时间
        try:
            start_date = '2019-09'
           # start_date = remove_tags(start_date)
            # print(start_date)
        except:
            start_date = None
            # print(start_date)

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
            career_en = response.xpath('//h2[contains(text(),"Sample Careers")]/following-sibling::ul[1]').extract()[0]
            career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',career_en)
            #print(career_en)
        except:
            career_en = None
            #print(career_en)

#12.截止日期
        try:
            deadline = '2019-02-15'
            #deadline = remove_tags(deadline)
            # print(career_en)
        except:
            deadline = None
            # print(deadline)
#13.学费
        try:
            if 'Bachelor of Arts' in degree_name:
                tuition_fee = '11,045.39'
            elif 'Bachelor of Commerce' in degree_name:
                tuition_fee = '12,531.77'
            elif 'Bachelor of Science' in degree_name:
                tuition_fee = '11,045.39'
            elif 'Bachelor of Applied Science' in degree_name:
                tuition_fee = '11,045.39'
            elif 'Bachelor of Engineering' in degree_name:
                tuition_fee = '14,587.57'
            elif 'Bachelor of Computing' in degree_name:
                tuition_fee = '11,691.55'
            else:
                tuition_fee = '11,045.39'
           # print(tuition_fee)
        except:
            tuition_fee = None
          #  print(tuition_fee)
#14 申请费:
        apply_fee = '90'

#15 申请要求

        try:
            entry_requirements_en = '<p>You must have a minimum cumulative grade point average (GPA) of 3.0 from a regionally accredited high school to begin consideration.</p><p>In addition, if your school is inside the US, you must submit an SAT with a minimum of 1100 in each component or a minimum ACT score of 24. GPA, SAT and ACT scores will vary by degree and major. Senior level courses should include specific subjects that are required for admission to your degree program and major of choice. Your school profile with grading scale should be included with documents, and all sent through Parchment/Naviance whenever possible. </p><p>Posessing the minimum requirement does not guarantee admission.<\p>'
            #entry_requirements_en = remove_tags(entry_requirements_en)
            # print(entry_requirements_en)
        except:
            entry_requirements_en = None
            # print(entry_requirements_en)

#16 中国学生申请要求
        try:
            require_chinese_en = '<p>1. I am currently studying in high school in a Chinese curriculum school</p><p>General Academic Requirements – Due March 1, 2019</p><p>Submit high school transcript with grades completed to date from years 10, 11 and first semester grade 12 are submitted by March 1. Final official Upper Middle School Graduation Certificate must be received in the original sealed school envelope or from the CHESICC by August 11, 2019.</p><p>Academic Proficiency Test examination results (Huikao) with a minimum of 80/100 including required subjects.</p><p>Huikao results must be verified by the China Higher Education Student Information & Career Center (CHESICC) using the CHESICC-Parchment Portal Service. </p><p>English Proficiency requirements</p><p>We welcome students to check the status of their documents at any time by checking their WebAdvisor account.<p></p></p><p>If you wish to include a Personal Statement, please use our Student Profile Form.<p></p></p><p>2. I have graduated from a Chinese curriculum high school</p><p>General Academic Requirements – Due March 1, 2019</p><p>Upper Middle School Graduation Certificate.</p><p>Academic Proficiency Test examination results (Huikao) with a minimum of 80/100 including required subjects.</p><p>NCEE (Gaokao) results including required subjects with a minimum of approximately 550 (in the absence of NCEE students may submit SAT and SATII results. See below for information). </p><p>Both Gaokao and Huikao results must be verified by the China Higher Education Student Information & Career Center (CHESICC) using the CHESICC-Parchment Portal Service. Visit the CHESICC website for instructions.</p><p>English Proficiency requirements</p>'
            #require_chinese_en = remove_tags(require_chinese_en)
            # print(require_chinese_en)
        except:
            require_chinese_en = None
            # print(require_chinese_en)

#17 特殊专业要求
        try:
            if 'Bachelor of Arts' in degree_name:
                specific_requirement_en = '<p>English</p><p>5 additional courses</p>'
            elif 'Bachelor of Science' in degree_name:
                specific_requirement_en = '<p>Biological Sciences </p><p>English </p><p>Advanced Math </p><p>2 credits from: Biology, Chemistry, Physics </p><p>2 additional courses </p><p>Physical Sciences </p><p>English </p><p>Calculus </p><p>2 credits from: Biology, Chemistry, Physics </p><p>2 additional courses</p>'
            elif 'Bachelor of Applied Science' in degree_name:
                specific_requirement_en = '<td><p><strong>Applied Human Nutrition</strong></p><ul><li>English</li><li>Math</li><li>Biology</li><li>Chemistry</li><li>2 additional courses</li></ul><p><strong>Adult Development &amp; Child, Youth and Family</strong></p><ul><li>English</li><li>Math</li><li>Biology or Chemistry</li><li>3 additional courses</li></ul></td>'
            elif 'Bachelor of Commerce' in degree_name:
                specific_requirement_en = '<td><ul><li>English</li><li>Advanced Math</li><li>4 additional courses</li></ul></td>'
            elif 'Bachelor of Computing' in degree_name:
                specific_requirement_en = '<td><ul><li>English</li><li>Calculus</li><li>4 additional courses</li></ul></td>'
            elif 'Bachelor of Engineering' in degree_name:
                specific_requirement_en = '<td><ul><li>English</li><li>Calculus</li><li>2 credits from: Biology, Chemistry, Physics</li><li>1 additional courses</li></ul></td>'
            elif 'Bachelor ofBio-Resource Management' in degree_name:
                specific_requirement_en = '<td><ul><li>English</li><li>Biology</li><li>4 additional courses</li></ul><p>Food Industry Management also&nbsp;requires:</p><ul style="margin-left:20px"><li>Advanced Math</li><li>Chemistry</li></ul></td>'
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
            min_language_require = 'Minimum overall score of 6.5 with no band less than 6,Internet-based: minimum total score of 89 with no individual scaled score less than 21'
            min_language_require = remove_tags(min_language_require)
            # print(min_language_require)
        except:
            min_language_require = None
            # print(min_language_require)

#25 雅思要求
        try:
            ielts_desc =  'Minimum overall score of 6.5 with no band less than 6'
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
            toefl_code = '0892'
            #toefl_code = remove_tags(toefl_code)
            # print(toefl_code)
        except:
            toefl_code = None
            # print(toefl_code)

#29 toefl_desc
        try:
            toefl_desc = 'minimum total score of 89 with no individual scaled score less than 21'
            #toefl_desc = remove_tags(toefl_desc)
            # print(toefl_desc)
        except:
            toefl_desc = None
            # print(toefl_desc)

#30 toefl
        try:
            toefl = '89'
            #toefl = remove_tags(toefl)
            # print(toefl)
        except:
            toefl = None
            # print(toefl)

#31 toefl_?
        toefl_l = 21
        toefl_s = 21
        toefl_r = 21
        toefl_w = 21

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
            ib = '<div><div><div><div></div></div><h1>International Baccalaureate (IB)</h1><p>If you are applying with an IB Diploma from outside Canada, you should present a minimum score of 28. Many programs will require a higher score for admission consideration. Reported bonus points will be taken into consideration.</p><p>Having the minimum score does not guarantee admission.</p><p>You should complete the Diploma with six subjects: <strong>3 Higher Level and 3&nbsp;Standard Level.</strong> You should also include specific subject requirements for the program you are applying to among your Standard and Higher Level courses. If you are currently completing the IB Diploma, you will be considered for admission consideration based upon predicted IB scores. You should ensure that your anticipated&nbsp;scores are submitted using the 7 point scale.</p><p>Upon receipt of official final results from IB, we will assign specific transfer credits, where applicable, to a maximum of 2.0 credits for grades of 5 or better on Higher Level courses where you have been awarded the IB Diploma or DP Course. You may request a change to unspecified credit on an individual basis within the first 30 days of your first semester.</p>'
            #print(ib)
        except:
            ib = None
            #print(ib)

#34 ap
        try:
            ap = '<p>If you have completed Advanced Placement Final Examinations with a minimum grade of 4, you will be eligible to receive university specific transfer credits, where applicable, to a maximum of 2.00 credits. You may request a change to unspecified credit on an individual basis within the first 30 days of your first semester.</p><p>Please arrange for an official score report to be sent directly to Admission Services. Transfer credit will be assigned once this has been received in Admission Services.</p>'
            #ap = remove_tags(ap)
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
            # print(other
        except:
            other = None
            # print(other)

        # sat act 代码 介绍
        sat_code = '0892'
        sat1_desc = 'For students who graduated in previous years without an NCEE you may substitute this by using a combination of SAT and SATII Subject Test, SAT Critical Reading and Math with a combined minimum of 1100 and SAT II Subject tests with an approximate minimum of 550 per subject. The specific SAT II Subject Tests required depend upon the intended field of study: <br>Biological Sciences: Math (level 2), Biology (either E or M) and Chemistry <br>Physical Sciences: Math (level 2), Physics and Chemistry <br>Arts/Humanities/Social Sciences: Literature, and two additional humanities or social science type courses (e.g. World History, French, etc.) <br>Commerce: Math (level 2) plus two additional SAT'
        sat2_desc = 'For students who graduated in previous years without an NCEE you may substitute this by using a combination of SAT and SATII Subject Test, SAT Critical Reading and Math with a combined minimum of 1100 and SAT II Subject tests with an approximate minimum of 550 per subject. The specific SAT II Subject Tests required depend upon the intended field of study: <br>Biological Sciences: Math (level 2), Biology (either E or M) and Chemistry <br>Physical Sciences: Math (level 2), Physics and Chemistry <br>Arts/Humanities/Social Sciences: Literature, and two additional humanities or social science type courses (e.g. World History, French, etc.) <br>Commerce: Math (level 2) plus two additional SAT'
        act_code = None
        act_desc = None

        duration = None

        try:
            if 'basc' in response.url:
                if 'Nutrition' in major_name_en:
                    average_score = '81-85%'
                else:
                    average_score = '77-81%'

            elif 'bcom' in response.url:
                average_score = '78-82%'

            elif 'bsc' in response.url:

                if 'Bio-Medical Science' in major_name_en:
                    average_score = '84-89%'
                elif 'Human Kinetics' in major_name_en:
                    average_score = '79-84%'
                else:
                    average_score = '78-83% '

            elif 'ba' in response.url:
                if 'Criminal Justice' in major_name_en or 'Public Policy' in major_name_en:
                    average_score = '79-83%'
                elif 'Psychology' in major_name_en:
                    average_score = '84-89%'
                else:
                    average_score = '76-80%'

            elif 'beng' in response.url:
                average_score = '84-89%'

            elif 'bbrm' in response.url:
                if 'Food Industry Management' in major_name_en:
                    average_score = '76-80%'
                else:
                    average_score = '75-78%'
            else:
                average_score = None

        except:
            average_score = None
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


        yield item


