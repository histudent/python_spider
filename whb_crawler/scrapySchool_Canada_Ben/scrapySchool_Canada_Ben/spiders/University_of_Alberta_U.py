import scrapy
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from scrapySchool_Canada_Ben import getItem
from w3lib.html import remove_tags
import requests
import re
import time
from lxml import etree


class BaiduSpider(scrapy.Spider):
    name = 'University_of_Alberta_U'
    start_urls = ['https://apps.admissions.ualberta.ca/programs/search?keywords=.&searchType=keywords']
    def parse(self, response):

        urlList=response.xpath('//tr/td[1]/a/@href').extract()
        dizhi = response.xpath('//tr/td[4]/a').extract()
        for uL,dz in zip(urlList,dizhi):
            uL  = 'https://apps.admissions.ualberta.ca' + uL
            yield scrapy.Request(url=uL, callback=self.parses,meta={"didian":dz})
    def parses(self, response):
        item = getItem.get_item(ScrapyschoolCanadaBenItem)
#1.学校名称
        Didian = response.meta['didian']
        Didian = remove_tags(Didian)
        #print(Didian)
        school_name = 'University of Alberta'
#2.地点
        try:
            location = Didian
            location = re.findall('\((.*)\)',location)[0]
            #print(location)
        except:
            location = None
            #print(location)

#3. 校区
        try:
            campus = re.findall('(.*) \(.*\)',Didian)[0]
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
            department = response.xpath('//*[@id="page-content"]/div[1]/div[1]/p[2]').extract()[0]
            department = remove_tags(department)
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
            degree_name = response.xpath('//*[@id="page-content"]/div[1]/div[1]/p[1]').extract()[0]
            degree_name = remove_tags(degree_name)

            #degree_name = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_name_list)
            #degree_name = degree_name.replace('\t','').replace('\n','').replace('\xa0','').replace(' class="list-inline uofs-cta-list','')
            # degree_name = degree_name.replace('<li>','').replace('</li>','---')
            # degree_name = degree_name.replace('<span>','').replace('</span>','---')
            #degree_name = degree_name.split('</li><li>')
            #print(degree_name)
            #print(response.url)
        except:

            degree_name = None
            #print(degree_name)

#5.学位描述
        try:
            degree_overview_en = response.xpath('//*[@id="page-content"]/div[3]/div[1]/h4[1]/following-sibling::p').extract()
            degree_overview_en = ''.join(degree_overview_en)
            #degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_overview_en)
            degree_overview_en = re.sub('<p(https:.*)">?','',degree_overview_en)
            degree_overview_en = degree_overview_en.replace('https://www.ualberta.ca/agriculture-life-environment-sciences/"','')
            degree_overview_en = degree_overview_en.replace('https://www.ualberta.ca/campus-saint-jean"','')
            degree_overview_en = degree_overview_en.replace('https://www.ualberta.ca/en/campus-saint-jean"','')
            degree_overview_en = degree_overview_en.replace(' xmlns=""','')
            #degree_overview_en = degree_overview_en.replace('https://www.ualberta.ca/arts"','')
            #degree_overview_en = degree_overview_en.replace('\r\n','')
            degree_overview_en = degree_overview_en.replace('\n','')
            #degree_overview_en = degree_overview_en.replace('\n','')
            #degree_overview_en = degree_overview_en.replace('  ',' ')
            degree_overview_en = degree_overview_en.replace('                           ','')
            degree_overview_en = degree_overview_en.replace('   ','')
            #print(degree_overview_en)
        except:
            degree_overview_en = None
            #print(degree_overview_en)
        #//*[@id="page-content"]/div[3]/div[1]/*

#6.专业英文
        try:
            major_name_en = response.xpath('//h1').extract()[1]
            major_name_en = major_name_en.replace('\r\n','').replace('\n','').replace('           ','').replace('\t','').replace('     ','')
            major_name_en = remove_tags(major_name_en)
           # print(major_name_en)
            #print(major_name_en)
        except:
            major_name_en = None
            #print(major_name_en)

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
            modules_en_dict = {"Augustana FacultyAccounting":"AUACC","Augustana FacultyArt":"AUART","Augustana FacultyBiology":"AUBIO","Augustana FacultyChemistry":"AUCHE","Augustana FacultyClassical Studies":"AUCLA","Augustana FacultyCrime and Community":"AUCRI","Augustana FacultyComputing Science":"AUCSC","Augustana FacultyCommunity Service Learning":"AUCSL","Augustana FacultyDrama":"AUDRA","Augustana FacultyEnglish for Academic Purposes":"AUEAP","Augustana FacultyEconomics":"AUECO","Augustana FacultyEducational Computing":"AUEDC","Augustana FacultyEducation Field Experience":"AUEFX","Augustana FacultyEnglish":"AUENG","Augustana FacultyEnvironmental Studies":"AUENV","Augustana FacultyEducational Psychology":"AUEPS","Fine Arts Option":"AUFAR","Augustana FacultyFrench":"AUFRE","Augustana FacultyGlobal and Development Studies":"AUGDS","Augustana FacultyGeography":"AUGEO","Augustana FacultyGerman":"AUGER","Augustana FacultyGreek":"AUGRE","Augustana FacultyHistory":"AUHIS","Augustana FacultyInterdisciplinary Studies":"AUIDS","Augustana FacultyIndigenous Studies":"AUIND","Augustana FacultyLanguage Studies":"AULAN","Augustana FacultyLatin":"AULAT","Augustana FacultyWorld Literatures":"AULIT","Augustana FacultyMathematics":"AUMAT","Augustana FacultyManagement":"AUMGT","Augustana FacultyMusic":"AUMUS","Augustana FacultyPhysical Activity":"AUPAC","Augustana FacultyPhysical Education":"AUPED","Augustana FacultyPhilosophy":"AUPHI","Augustana FacultyPhysics":"AUPHY","Augustana FacultyPolitical Studies":"AUPOL","Augustana FacultyPsychology":"AUPSY","Augustana FacultyReligion":"AUREL","Augustana FacultyScandinavian":"AUSCA","Augustana FacultySociology":"AUSOC","Augustana FacultySpanish":"AUSPA","Augustana FacultyStatistics":"AUSTA","Agriculture, Forestry, and Home Economics":"AFHE","Agricultural, Food and Nutritional Science":"AFNS","Agricultural, Life and Environmental Sciences":"ALES","Animal Science":"AN SC","Agricultural and Resource Economics":"AREC","Environmental and Conservation Sciences":"ENCS","Forest Science":"FOR","Forest Economics":"FOREC","Human Ecology":"HECOL","Nutrition and Food Sciences":"NU FS","Nutrition":"NUTR","Plant Science":"PL SC","Rural Sociology":"R SOC","Renewable Resources":"REN R","University":"UNIV","Astronomy":"ASTRO","Bioinformatics":"BIOIN","Biology":"BIOL","Botany":"BOT","Chemistry":"CHEM","Computing Science":"CMPUT","Earth and Atmospheric Sciences":"EAS","Engineering Physics":"EN PH","Entomology":"ENT","Environmental Physical Sciences":"ENVPS","Genetics":"GENET","Geophysics":"GEOPH","Immunology and Infection":"IMIN","Integrated Petroleum Geosciences":"IPG","Mathematical Physics":"MA PH","Marine Science":"MA SC","Mathematics":"MATH","Microbiology":"MICRB","Master of Internetworking":"MINT","Multimedia":"MM","Paleontology":"PALEO","Physics":"PHYS","Urban and Regional Planning":"PLAN","Psychology":"PSYCO","Science":"SCI","Statistics":"STAT","Work Experience":"WKEXP","Zoology":"ZOOL","Pharmacy":"PHARM","Nursing":"NURS","Sciences infirmières":"SC INF","Native Studies":"NS","Anaesthesia":"ANAES","Anatomy":"ANAT","Biochemistry":"BIOCH","Biomedical Engineering":"BME","Cell Biology":"CELL","Dental Hygiene":"D HYG","Dentistry":"DDS","Dentistry":"DENT","Dentistry/Medicine":"DMED","Electrical and Computer Engineering/Biomedical Eng":"EE BE","Family Medicine":"F MED","Laboratory Medicine and Pathology":"LABMP","Medical Genetics":"MDGEN","Medicine":"MED","Medical Laboratory Science":"MLSCI","Medical Microbiology and Immunology":"MMI","Neuroscience (Centre for)":"NEURO","Obstetrics and Gynaecology":"OB GY","Oral Biology":"OBIOL","Oncology":"ONCOL","Ophthalmology":"OPHTH","Paediatrics":"PAED","Postgraduate Dental Education":"PGDE","Postgraduate Medical Education":"PGME","Physiology":"PHYSL","Pharmacology":"PMCOL","Psychiatry":"PSYCI","Radiology and Diagnostic Imaging":"RADDI","Radiation Therapy":"RADTH","Surgery":"SURG","Law":"LAW","Dance Activity":"DAC","Dance":"DANCE","Health Education":"HE ED","Kinesiology":"KIN","Kinesiology, Recreation, Leisure and Sport":"KRLS","Physical Activity":"PAC","Physical Education and Sport":"PEDS","Physical Education, Recreation and Leisure Studies":"PERLS","Recreation and Leisure Studies":"RLS","Chemical Engineering":"CH E","Civil Engineering":"CIV E","Chemical and Materials Engineering":"CME","Computer Engineering":"CMPE","Electrical Engineering":"E E","Electrical and Computer Engineering":"ECE","Engineering, Computer":"ENCMP","Engineering Management":"ENG M","Engineering, General":"ENGG","Environmental Engineering":"ENV E","Materials Engineering":"MAT E","Mechanical Engineering":"MEC E","Mining Engineering":"MIN E","Petroleum Engineering":"PET E","EducationAdult":"EDAE","EducationBusiness":"EDBU","EducationCareer Technology Studies":"EDCT","EducationElementary":"EDEL","EducationElementary and Secondary":"EDES","EducationField Experience":"EDFX","EducationInstructional Technology":"EDIT","EducationPolicy Studies":"EDPS","EducationPsychology":"EDPY","EducationSecondary":"EDSE","Education":"EDU","Library and Information Studies":"LIS","Accounting":"ACCTG","Business Law":"B LAW","Business Economics":"BUEC","Business":"BUS","Finance":"FIN","Industrial Relations":"IND R","Marketing":"MARK","Management Science":"MGTSC","Management Information Systems":"MIS","Operations Management":"OM","Organizational Analysis":"ORG A","Strategic Management and Organization":"SMO","Anthropology":"ANTHR","Arabic":"ARAB","Art":"ART","Art History":"ART H","American Sign Language":"ASL","Comparative Literature":"C LIT","Chinese":"CHINA","Classics":"CLASS","Community Service-Learning":"CSL","Danish":"DANSK","Design":"DES","Drama":"DRAMA","East Asian Studies":"EASIA","Economics":"ECON","English":"ENGL","French Language and Literature":"FREN","Film Studies":"FS","German":"GERM","Greek":"GREEK","Gender and Social Justice":"GSJ","History of Art, Design, and Visual Culture":"HADVC","Hebrew":"HEBR","Human Geography and Planning":"HGP","Hindi":"HINDI","History":"HIST","Humanities Computing":"HUCO","Hungarian":"HUNG","Interdisciplinary Undergraduate & Graduate Courses":"INT D","Italian":"ITAL","Japanese":"JAPAN","Korean":"KOREA","Latin American Studies":"LA ST","Latin":"LATIN","Linguistics":"LING","Middle Eastern and African Studies":"MEAS","Modern Languages and Cultural Studies":"MLCS","Music":"MUSIC","Norwegian":"NORW","Persian":"PERS","Philosophy":"PHIL","Political Science":"POL S","Polish":"POLSH","Portuguese":"PORT","Punjabi":"PUNJ","Religious Studies":"RELIG","Russian":"RUSS","Scandinavian":"SCAND","Slavic and East European Studies":"SLAV","Sociology":"SOC","Spanish":"SPAN","Science, Technology, and Society":"STS","Swahili":"SWAH","Swedish":"SWED","Theatre Design":"T DES","Ukrainian":"UKR","Women's Studies":"W ST","Women's and Gender Studies":"WGS","Writing (Creative Writing)":"WRITE","Writing Studies":"WRS"}
            if 'Augustana Faculty' in department:
                modules_en_val =  'Augustana Faculty' + major_name_en
                modules_en_val = modules_en_val.replace(' Co-operative','')
                print('第一:'+modules_en_val)
            else:
                modules_en_val = major_name_en
                modules_en_val = modules_en_val.replace(' Co-operative','')
                print("第一:"+modules_en_val)
            modules_en_val = modules_en_dict[modules_en_val]
            url = 'https://catalogue.ualberta.ca/Course/Subject?subjectCode='+ modules_en_val  + '&all=True'
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
            response2 = etree.HTML(requests.get(url, headers=headers).text)
            response2=response2.xpath('//div[@class = "claptrap-course"]')
            modules_en=[]
            for rea in response2:
                modules_en += etree.tostring(rea,method='html',encoding='unicode')
                modules_en=''.join(modules_en)
            modules_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',modules_en)
            modules_en = modules_en.replace('\r\n','').replace('\n','').replace('            ','').replace('        ','').replace('    ','')
            print(modules_en)
        except:
            modules_en = None
            print(modules_en)

#11.就业方向
        try:
            career_en = response.xpath('//*[@id="page-content"]/div[3]/div[1]/h4/following-sibling::ul').extract()[0]
            career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',career_en)
            career_en = career_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
            career_en = career_en.replace('                              ','')
            #print(career_en)
        except:
            career_en = None
            #print(career_en)

#12.截止日期
        try:
            deadline = '2019-03-01'
            #deadline = response.xpath('//h3[contains(text(),"Deadline")]/following-sibling::p[1]').extract()[0]
            #deadline = remove_tags(deadline)
            #deadline = deadline.replace('Documents due: ', '')
            #deadline = remove_tags(deadline)
            #print(deadline)
        except:
            deadline = None
            #print(deadline)
#13.学费
        try:
            abaa = 'https://apps.admissions.ualberta.ca/costcalculator/faculties/%s/international/off-campus?pttool=true'
            acc = response.xpath('//*[@id="get-program-costs"]/@href').extract()[0]
            acc = re.findall('\d',acc)[0]
            #print(acc)
            url = abaa % acc
            #print(url)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
            response1 = requests.get(url,headers=headers)
            #print(response1.text)
            tuition_fee = response1.text
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = tuition_fee.replace('\n','').replace('\r\n','').replace('                           ','')
            tuition_fee = re.findall('\$(\d+\.\d+)',tuition_fee)[0]
            #print(tuition_fee)
        except:
            tuition_fee = None
            #print(tuition_fee)
#14 申请费:
        apply_fee = '100'

#15 申请要求
        try:

            entry_requirements_en = '<div><div><div><h3><em> <strong></strong></em>Competitive<em><strong> </strong></em>Admission</h3><p><em><strong>We encourage you to apply early, as admission is competitive, and space in each program is limited.</strong></em>&nbsp;</p><p>The University of Alberta provides a wide range of programs, from highly accessible to highly competitive.<br><br>In order to be considered for admission, you need to present a competitive average for your faculty/program of choice, based on the required courses for that program. <br><br>The competitive average for each faculty/program may change throughout the year, based on the competitiveness of the applicant pool.<br><br>In addition to presenting a competitive average when you apply, you must also meet the university’s minimum admission requirements after receiving an admission offer in order to remain eligible.</p></div></div><div><div><h3>Minimum Requirements</h3><p>Admission is competitive; meeting the minimum requirements does not guarantee admission. </p><p>You must meet the minimum requirements in all subjects, even after receiving an admission offer, in order to remain admissible. (See your admission offer letter for more details.)</p><p>&nbsp;</p><table><tbody><tr><td><strong>Minimum requirements</strong><br></td><td><strong>&nbsp;Grade 11 final marks</strong></td><td><strong>&nbsp;Grade 12 first semester / interim marks</strong></td><td><strong>&nbsp;Grade 12 final marks</strong><br></td></tr><tr><td>Minimum grade for each of the five required courses<br></td><td>&nbsp;60%+</td><td>&nbsp;50%+<br></td><td>&nbsp;50%+</td></tr><tr><td>Minimum overall average across all five required courses<br></td><td>&nbsp;70%+</td><td>&nbsp;70%+&nbsp;</td><td>&nbsp;70%+</td></tr></tbody></table></div></div></div>'
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
            require_chinese_en = '<p>A combination of A’s and B’s on the Joint Graduation Exam (Hui Kao) or a competitive score on the University Entrance Exam (Gao Kao) that would normally be required for admission to a key university in China. Results must be issued by the governing authority, not by the school.</p>'
            #require_chinese_en = remove_tags(require_chinese_en)
            # print(require_chinese_en)
        except:
            require_chinese_en = None
            # print(require_chinese_en)

#17 特殊专业要求
        try:
            specific_requirement_en = response.xpath('//div[@class = "row-fluid required-courses"]').extract()
            specific_requirement_en = ''.join(specific_requirement_en)
            specific_requirement_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',specific_requirement_en)
            #print(specific_requirement_en)
        except:
            specific_requirement_en = None
            #print(specific_requirement_en)

#18 高考(官网要求)
        try:
            gaokao_desc = 'A combination of A’s and B’s on the Joint Graduation Exam (Hui Kao) or a competitive score on the University Entrance Exam (Gao Kao) that would normally be required for admission to a key university in China. Results must be issued by the governing authority, not by the school.'
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
            huikao_desc = 'A combination of A’s and B’s on the Joint Graduation Exam (Hui Kao) or a competitive score on the University Entrance Exam (Gao Kao) that would normally be required for admission to a key university in China. Results must be issued by the governing authority, not by the school.'
            #huikao_desc = remove_tags(huikao_desc)
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
            min_language_require = 'At least 6.5 with no band less than 5.5'
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

        ielts_l = 5.5
        ielts_s = 5.5
        ielts_r = 5.5
        ielts_w = 5.5

#28 toefl_code
        try:
            toefl_code = '0963'
            #toefl_code = remove_tags(toefl_code)
            # print(toefl_code)
        except:
            toefl_code = None
            # print(toefl_code)

#29 toefl_desc
        try:
            toefl_desc = 'iBT: At least 90 with a minimum score of 21 points in each section Note: the PBT is no longer accepted'
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
            ib = 'Approximately 30–35 IB predicted points on the full diploma, including bonus points.Full IB Diploma students may be eligible to receive admission based on predicted scores. Competitive predicted IB scores for admission vary by Faculty. Final IB grades in the range of 4 to 7 are considered competitive. IB Grade:7(Percent Equivalent:98%),6(Percent Equivalent:90%),5(Percent Equivalent:82%),4(Percent Equivalent:73%),3(Percent Equivalent:55%),2(Percent Equivalent:not accepted),1(Percent Equivalent:not accepted)'
            #print(ib)
        except:
            ib = None
            #print(ib)

#34 ap
        try:
            ap = 'A combination of grades of 4 and 5.AP Result:5(Percent Equivalent:96%),4(Percent Equivalent:86%),3(Percent Equivalent:76%),2(Percent Equivalent:65%)'
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
            other = '1.列表页有校区信息,从列表页进入详情页.2.学位是js加载需要get获取.3.课程界面需要匹配详情页内的学院+专业名称跳转三次获取课程信息4.部分课程数据需要根据业务老师提供链接手动抓取'
            #other = remove_tags(other)
            # print(other)
        except:
            other = None
            # print(other)

        # sat act 代码 介绍
        sat_code = '0963'
        sat1_desc = 'SAT Score of 1200 with a minimum 600 in each section. See International Course Equivalencies for more details.'
        sat2_desc = None
        act_code = ''
        act_desc = ''
        if 'Faculty of Agricultural' in department:
            average_score = 'At least 80% of students admitted into the Faculty of ALES for Fall 2018 had admission averages in the mid-70s or higher.'
        elif 'Arts' in department:
            average_score = 'At least 75% of students admitted into the Faculty of Arts for Fall 2018 had admission averages in the 80s or higher.'
        elif 'Augustana' in department:
            average_score = 'At least 60% of students admitted into the Augustana Faculty for Fall 2018 had admission averages in the 80s or higher.'
        elif 'Engineering' in department:
            average_score = 'At least 70% of students admitted into the Faculty of Engineering for Fall 2018 had admission averages in the mid-80s or higher.'
        elif 'Education' in department:
            average_score = 'At least 77% of students admitted into the Faculty of Education for Fall 2018 had admission averages in the 80s or higher.'
        elif 'Native Studies' in department:
            average_score = 'At least 70% of students admitted into the Faculty of Native Studies for Fall 2018 had admission averages in the mid-70s or higher.'
        elif 'Faculty of Science' in department:
            average_score = 'At least 70% of students admitted into the Faculty of Science for Fall 2018 had admission averages in the mid-80s or higher.'
        elif 'Faculty of Nursing' in  department:
            average_score = 'At least 73% of students admitted into the Faculty of Nursing for Fall 2018 had admission averages in the 90s.'
        elif 'Kinesiology' in department:
            average_score = 'At least 79% of students admitted into the Faculty of Kinesiology, Sport, and Recreation for Fall 2018 had admission averages in the mid-80s or higher.'
        elif 'Faculty of Business' in department:
            average_score = '75'
        else:
            average_score = None
        item["ap"] = ap
        item["duration_per"] = 1
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
        item["sat_code"] = sat1_desc
        item["sat_code"] = sat2_desc
        item["sat_code"] = act_code
        item["sat_code"] = act_desc
        item["gaokao_desc"] = gaokao_desc
        item["average_score"] = average_score
        aaa = response.xpath('//body').extract()
        #print(aaa)
        if 'Minor' not in degree_name and 'After Degree' not  in degree_name and 'This program does not allow admission directly from high school. See requirements below for more details.' not  in aaa and 'Faculté Saint-Jean' not in department:
                yield item

                #pass
            #print(degree_name)
        else:
            pass