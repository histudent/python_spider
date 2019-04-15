import scrapy
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from scrapySchool_Canada_Ben import getItem
from w3lib.html import remove_tags
import requests
import re
from lxml import etree

class BaiduSpider(scrapy.Spider):
    name = 'Carleton_University_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['https://admissions.carleton.ca/programs/accounting/',
'https://admissions.carleton.ca/programs/actuarial-science/',
'https://admissions.carleton.ca/programs/aerospace-engineering/',
'https://admissions.carleton.ca/programs/africa-globalization/',
'https://admissions.carleton.ca/programs/african-studies/',
'https://admissions.carleton.ca/programs/algorithms/',
'https://admissions.carleton.ca/programs/anthropology/',
'https://admissions.carleton.ca/programs/applied-linguistics-and-discourse-studies/',
'https://admissions.carleton.ca/programs/applied-physics/',
'https://admissions.carleton.ca/programs/architectural-conservation-and-sustainability-engineering/',
'https://admissions.carleton.ca/programs/architectural-studies/',
'https://admissions.carleton.ca/programs/art-history/',
'https://admissions.carleton.ca/programs/arts/',
'https://admissions.carleton.ca/programs/biochemistry/',
'https://admissions.carleton.ca/programs/bioinformatics/',
'https://admissions.carleton.ca/programs/biology-ba/',
'https://admissions.carleton.ca/programs/biology-bsc/',
'https://admissions.carleton.ca/programs/biomedical-and-electrical-engineering/',
'https://admissions.carleton.ca/programs/biomedical-and-mechanical-engineering/',
'https://admissions.carleton.ca/programs/biomedical-sciences/',
'https://admissions.carleton.ca/programs/biotechnology/',
'https://admissions.carleton.ca/programs/canadian-studies/',
'https://admissions.carleton.ca/programs/chemistry/',
'https://admissions.carleton.ca/programs/child-studies/',
'https://admissions.carleton.ca/programs/civil-engineering/',
'https://admissions.carleton.ca/programs/cognitive-science/',
'https://admissions.carleton.ca/programs/commerce/',
'https://admissions.carleton.ca/programs/communication-media-studies/',
'https://admissions.carleton.ca/programs/communications-engineering/',
'https://admissions.carleton.ca/programs/computational-and-applied-mathematics-and-statistics/',
'https://admissions.carleton.ca/programs/computational-biochemistry/',
'https://admissions.carleton.ca/programs/computer-and-internet-security/',
'https://admissions.carleton.ca/programs/computer-game-development/',
'https://admissions.carleton.ca/programs/computer-science/',
'https://admissions.carleton.ca/programs/computer-systems-engineering/',
'https://admissions.carleton.ca/programs/criminology-and-criminal-justice/',
'https://admissions.carleton.ca/programs/disability-chronic-illness/',
'https://admissions.carleton.ca/programs/earth-sciences/',
'https://admissions.carleton.ca/programs/economics/',
'https://admissions.carleton.ca/programs/electrical-engineering/',
'https://admissions.carleton.ca/programs/engineering/',
'https://admissions.carleton.ca/programs/engineering-physics/',
'https://admissions.carleton.ca/programs/english/',
'https://admissions.carleton.ca/programs/entrepreneurship/',
'https://admissions.carleton.ca/programs/environment-health/',
'https://admissions.carleton.ca/programs/environmental-engineering/',
'https://admissions.carleton.ca/programs/environmental-science/',
'https://admissions.carleton.ca/programs/environmental-studies/',
'https://admissions.carleton.ca/programs/europe-russia-world/',
'https://admissions.carleton.ca/programs/european-and-russian-studies/',
'https://admissions.carleton.ca/programs/film-studies/',
'https://admissions.carleton.ca/programs/finance/',
'https://admissions.carleton.ca/programs/food-science-and-nutrition/',
'https://admissions.carleton.ca/programs/french/',
'https://admissions.carleton.ca/programs/french-francophone-studies/',
'https://admissions.carleton.ca/programs/geography-ba/',
'https://admissions.carleton.ca/programs/geomatics/',
'https://admissions.carleton.ca/programs/geomatics-bsc/',
'https://admissions.carleton.ca/programs/global-international-studies/',
'https://admissions.carleton.ca/programs/global-transnational-history/',
'https://admissions.carleton.ca/programs/global-development/',
'https://admissions.carleton.ca/programs/global-financial-management-and-systems/',
'https://admissions.carleton.ca/programs/global-genders-sexualities/',
'https://admissions.carleton.ca/programs/global-health/',
'https://admissions.carleton.ca/programs/global-inequalities-social-change/',
'https://admissions.carleton.ca/programs/global-law-social-justice/',
'https://admissions.carleton.ca/programs/global-literatures/',
'https://admissions.carleton.ca/programs/global-media-and-communication/',
'https://admissions.carleton.ca/programs/global-politics/',
'https://admissions.carleton.ca/programs/global-religions-identity-and-community/',
'https://admissions.carleton.ca/programs/globalization-environment/',
'https://admissions.carleton.ca/programs/globalization-culture-power/',
'https://admissions.carleton.ca/programs/greek-and-roman-studies/',
'https://admissions.carleton.ca/programs/health-sciences/',
'https://admissions.carleton.ca/programs/health-throughout-lifespan/',
'https://admissions.carleton.ca/programs/history/',
'https://admissions.carleton.ca/programs/history-and-theory-of-architecture/',
'https://admissions.carleton.ca/programs/human-rights-ba/',
'https://admissions.carleton.ca/programs/humanities/',
'https://admissions.carleton.ca/programs/indigenous-studies/',
'https://admissions.carleton.ca/programs/industrial-design/',
'https://admissions.carleton.ca/programs/information-resource-management-irm/',
'https://admissions.carleton.ca/programs/information-systems/',
'https://admissions.carleton.ca/programs/information-technology/',
'https://admissions.carleton.ca/programs/interactive-multimedia-and-design-imd/',
'https://admissions.carleton.ca/programs/interdisciplinary-science-and-practice/',
'https://admissions.carleton.ca/programs/international-business-bcomm/',
'https://admissions.carleton.ca/programs/international-business/',
'https://admissions.carleton.ca/programs/international-economic-policy/',
'https://admissions.carleton.ca/programs/international-marketing-and-trade/',
'https://admissions.carleton.ca/programs/international-strategy-and-human-resources-management/',
'https://admissions.carleton.ca/programs/journalism/',
'https://admissions.carleton.ca/programs/journalism-humanities/',
'https://admissions.carleton.ca/programs/latin-american-caribbean-studies/',
'https://admissions.carleton.ca/programs/law-ba/',
'https://admissions.carleton.ca/programs/linguistics/',
'https://admissions.carleton.ca/programs/management/',
'https://admissions.carleton.ca/programs/management-and-business-systems/',
'https://admissions.carleton.ca/programs/marketing/',
'https://admissions.carleton.ca/programs/mathematics-3/',
'https://admissions.carleton.ca/programs/mathematics/',
'https://admissions.carleton.ca/programs/mechanical-engineering/',
'https://admissions.carleton.ca/programs/media-production-design/',
'https://admissions.carleton.ca/programs/migration-diaspora-studies/',
'https://admissions.carleton.ca/programs/mobile-computing/',
'https://admissions.carleton.ca/programs/music-ba/',
'https://admissions.carleton.ca/programs/music-bmus/',
'https://admissions.carleton.ca/programs/nanoscience/',
'https://admissions.carleton.ca/programs/network-computing/',
'https://admissions.carleton.ca/programs/network-technology-net/',
'https://admissions.carleton.ca/programs/neuroscience/',
'https://admissions.carleton.ca/programs/neuroscience-and-mental-health/',
'https://admissions.carleton.ca/programs/philosophy/',
'https://admissions.carleton.ca/programs/photonics-and-laser-technology-plt/',
'https://admissions.carleton.ca/programs/physical-geography/',
'https://admissions.carleton.ca/programs/physics/',
'https://admissions.carleton.ca/programs/political-science/',
'https://admissions.carleton.ca/programs/psychology-ba/',
'https://admissions.carleton.ca/programs/psychology-bsc/',
'https://admissions.carleton.ca/programs/public-affairs-and-policy-management/',
'https://admissions.carleton.ca/programs/religion/',
'https://admissions.carleton.ca/programs/science/',
'https://admissions.carleton.ca/programs/social-work/',
'https://admissions.carleton.ca/programs/sociology/',
'https://admissions.carleton.ca/programs/software-engineering-beng/',
'https://admissions.carleton.ca/programs/software-engineering-computer-science/',
'https://admissions.carleton.ca/programs/statistics/',
'https://admissions.carleton.ca/programs/supply-chain-management/',
'https://admissions.carleton.ca/programs/sustainable-and-renewable-energy-engineering/',
'https://admissions.carleton.ca/programs/teaching-english-global-contexts/',
'https://admissions.carleton.ca/programs/undeclared/',
'https://admissions.carleton.ca/programs/womens-and-gender-studies/',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        item = getItem.get_item(ScrapyschoolCanadaBenItem)



        try:
            major_name_en = response.xpath('//*[@id="framework"]/section[1]/div[1]/h1').extract()[0]
            #major_name_en = ''.join(major_name_en)
            #major_name_en = major_name_en.replace('\r\n','').replace('\n','').replace('           ','').replace('\t','').replace('     ','')
            major_name_en = remove_tags(major_name_en)
          #  print(major_name_en)
        except:
            major_name_en = None
            #print(major_name_en)
#1.学校名称
        school_name = 'Carleton University'

#2.地点
        try:
            location = 'Ontario'
            #location = remove_tags(location)
            #print(location)
        except:
            location = None
# 3. 校区
        try:
            campus = response.xpath('//h2[contains(text(),"Campus")]/following-sibling::div[1]').extract()[0]
            campus = remove_tags(campus)
            campus = campus.replace(', Online', '')
            campus = campus.replace(' ', '')
            campus = campus.split(',')
            # print(campus_list)
        except:
            campus = None
            # print(campus_list)

                # 4. 学院
        try:
            department = response.xpath('//h2[contains(text(),"Department")]/following-sibling::div[2]').extract()[0]

            department = remove_tags(department)
                # print(department)
        except:
            department = None
            # print(department)

# 4. 学位名称
        try:
            degree_name =  response.xpath('//h2[contains(text(),"Degrees")]/following-sibling::div[1]').extract()[0]
            degree_name = remove_tags(degree_name, keep=('li', 'br', ''))
            degree_name = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]', '', degree_name)
            degree_name = degree_name.replace('<br>', '---')
            degree_name = degree_name.replace('<li>', '').replace('</li>', '---')
            degree_name = degree_name.replace('<span>', '').replace('</span>', '---')
            degree_name = degree_name.split('---')
            # print(degree_name)
        except:
            degree_name = None
            # print(degree_name)

# 5.学位描述
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
            start_date = '2019-09'
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
            modules_en_dict = {"Aerospace Engineering":"AERO/",
    "African Studies":"AFRI/",
    "American Sign Language":"ASLA/",
    "Anthropology":"ANTH/",
    "Applied Linguistics and Discourse Studies":"ALDS/",
    "Arabic":"ARAB/",
    "Theory/History":"ARCH/",
    "Technical":"ARCC/",
    "Urban":"ARCU/",
    "Techniques":"ARCN/",
    "Design Studios/Design Thesis/Research":"ARCS/",
    "Art History":"ARTH/",
    "Biochemistry":"BIOC/",
    "Biology":"BIOL/",
    "Business":"BUSI/",
    "Canadian Studies":"CDNS/",
    "Centre for Initiatives in Education":"CIED/",
    "Chemistry":"CHEM/",
    "Child Studies":"CHST/",
    "Chinese":"CHIN/",
    "Civil Engineering":"CIVE/",
    "Classical Civilization":"CLCV/",
    "Co-operative Education":"COOP/",
    "Cognitive Science":"CGSC/",
    "Communication and Media Studies":"COMS/",
    "Communication Courses for Disciplines and Professions":"CCDP/",
    "Computer Science":"COMP/",
    "Criminology and Criminal Justice":"CRCJ/",
    "Digital Humanities":"DIGH/",
    "Disability Studies":"DBST/",
    "Earth Sciences":"ERTH/",
    "Economics":"ECON/",
    "Electronics":"ELEC/",
    "Engineering Common Core Courses":"ECOR/",
    "English":"ENGL/",
    "English as a Second Language":"ESLA/",
    "Environmental Engineering":"ENVE/",
    "Environmental Science":"ENSC/",
    "Environmental Studies":"ENST/",
    "European, Russian and Eurasian Studies":"EURR/",
    "Film Studies":"FILM/",
    "First-Year Seminars":"FYSM/",
    "Food Science":"FOOD/",
    "French":"FREN/",
    "French Interdisciplinary Studies":"FINS/",
    "Geography":"GEOG/",
    "Geomatics":"GEOM/",
    "German":"GERM/",
    "Global and International Studies":"GINS/",
    "Global Politics":"GPOL/",
    "Greek":"GREK/",
    "Health Sciences":"HLTH/",
    "Hebrew":"HEBR/",
    "History":"HIST/",
    "Human Rights":"HUMR/",
    "Humanities":"HUMS/",
    "Indigenous Studies":"INDG/",
    "Industrial Design":"IDES/",
    "Information Resource Management":"IRM/",
    "Interactive Media and Design":"IMD/",
    "Network Technology":"NET/",
    "Photonics":"PLT",
    "Information Technology":"ITEC/",
    "Integrated Science":"INSC/",
    "Interdisciplinary Public Affair":"IPAF/",
    "Interdisciplinary Science":"ISCI/",
    "Interdisciplinary Studies":"DIST/",
    "International Affairs":"INAF/",
    "Italian":"ITAL/",
    "Japanese":"JAPA/",
    "Journalism and Communication":"JOUR/",
    "Korean":"KORE/",
    "Language Studies":"LANG/",
    "Latin":"LATN/",
    "Latin American and Caribbean Studies":"LACS/",
    "Law":"LAWS/",
    "Linguistics":"LING/",
    "Mathematics":"MATH/",
    "Mechanical Engineering":"MECH/",
    "Mechanical and Aerospace Engineering":"MAAE/",
    "Media Production and Design":"MPAD/",
    "Medieval and Early Modern Studies":"MEMS/",
    "Migration and Diaspora Studies":"MGDS/",
    "Music":"MUSI/",
    "Natural Sciences":"NSCI/",
    "Neuroscience":"NEUR/",
    "Philosophy":"PHIL/",
    "Physics":"PHYS/",
    "Political Managemen":"POLM/",
    "Political Science":"PSCI/",
    "Portuguese":"PORT/",
    "Psychology":"PSYC/",
    "Public Affairs and Policy Management":"PAPM/",
    "Public Policy and Administration":"PADM/",
    "Religion":"RELI/",
    "Russian":"RUSS/",
    "Sexuality Studies":"SXST/",
    "Social Work":"SOWK/",
    "Sociology":"SOCI/",
    "South Asian Studies":"SAST/",
    "Spanish":"SPAN/",
    "Statistics":"STAT/",
    "Sustainable and Renewable Energy Engineering":"SREE/",
    "Systems and Computer Engineering":"SYSC/",
    "Technology, Society, Environment Studies":"TSES/",
    "Women’s and Gender Studies":"WGST/"}
            modules_en_val = re.sub(' \(.*\)','',major_name_en)
           # print(modules_en_val)
            modules_en_val = modules_en_dict[modules_en_val]
           # print(modules_en_val)
            url = 'http://calendar.carleton.ca/undergrad/courses/' + modules_en_val
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
            response2 = etree.HTML(requests.get(url, headers=headers).text)
            response2 = response2.xpath('//div[@class="courses"]')
            modules_en = []
            # print(response2)
            for rea in response2:
                modules_en += etree.tostring(rea, method='html', encoding='unicode')
                modules_en = ''.join(modules_en)
            # print(modules_en,'------------')
            modules_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',modules_en)
            modules_en = modules_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
            print(modules_en)
        except:
            modules_en = None
            #print(modules_en)

#11.就业方向
        try:
            career_en = response.xpath('//*[@id="main-content"]/div/section/div/div/div[2]/div[3]/div/ul/li/a|//*[@id="main-content"]/div/section/div/div/div[2]/div[3]|//div[@class = "careers"]|//*[@id="future-opportunities"]').extract()
            career_en = ''.join(career_en)
            career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',career_en)
            career_en = career_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
           # print(career_en)
        except:
            career_en = None
         #   print(career_en)

#12.截止日期
        try:
            deadline = '2019-04-01'
            # deadline = response.xpath('//*[@id="Admissionrequirementsanddeadlines-subsection-0"]/table/tbody/tr/td[3]').extract()
            # deadline = '---'.join(deadline)
            # deadline = remove_tags(deadline)
            # deadline = deadline.replace('Documents due: ', '')
            # deadline =  deadline.replace('Sep 1, 2018Oct 1, 2018','2018-09-01').replace('Feb 1, 2019Mar 1, 2019','2019-02-01').replace('Mar 1, 2019Apr 1, 2019','2019-03-01').replace('May 1, 2019Jun 1, 2019','2019-05-01').replace('Sep 1, 2019Oct 1, 2019','2019-09-01').replace('Feb 15, 2019Mar 1, 2019','2019-02-15').replace('---',',')
            # #deadline = remove_tags(deadline)
            #print(deadline)
        except:
            deadline = None
            #print(deadline)
#13.学费
        try:
            tuition_fee = '34,221'
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = tuition_fee.replace('$','')
            #print(tuition_fee)
        except:
            tuition_fee = None
            #print(tuition_fee)
#14 申请费:
        apply_fee = '166'

#15 申请要求
        try:
            entry_requirements_en = 'General Requirements:<br>Senior High School (3 years of study) <br>Final Chinese Upper Middle School transcript and graduation diploma for verification by China Academic Degrees and Graduate Education Development Centre (CDGDC) or China Credentials Verification (CHESICC-Parchment Portal Service).'
        except:
            entry_requirements_en = None
            #print(entry_requirements_en)
            #print(abc)

#16 中国学生申请要求
        try:
            require_chinese_en = entry_requirements_en
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
            min_language_require = '6.5 IELTS (min 6.0 each band)'
            min_language_require = remove_tags(min_language_require)
            # print(min_language_require)
        except:
            min_language_require = None
            # print(min_language_require)

#25 雅思要求
        try:
            ielts_desc = '6.5 IELTS (min 6.0 each band)'
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
            toefl_code = '0854'
            #toefl_code = remove_tags(toefl_code)
            # print(toefl_code)
        except:
            toefl_code = None
            # print(toefl_code)

#29 toefl_desc
        try:
            toefl_desc = '86 (22 in writing and speaking, 20 reading and listening)'
            #toefl_desc = remove_tags(toefl_desc)
            # print(toefl_desc)
        except:
            toefl_desc = None
            # print(toefl_desc)

#30 toefl
        try:
            toefl = '86'
            #toefl = re.findall('\d\d',toefl)
            #toefl = remove_tags(toefl)
            #print(toefl)
        except:
            toefl = None
            #print(toefl)

#31 toefl_?
        toefl_l = 20
        toefl_s = 22
        toefl_r = 20
        toefl_w = 22

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
            ib = 'You will need the full IB diploma (three subsidiary [SL] and three higher level [HL] subjects), with a minimum of 28 points (please note that some programs are more competitive, so will require higher scores). You may have one subject with a grade of 3, provided it is offset by a grade of 5 or better. Prerequisite subjects must have a grade of 4 or better. Early/conditional offers may be available with predicted results. IB students may be awarded advanced standing (transfer) credit for HL subjects with a grade of 5 or better subject to the discretion of the appropriate faculty, to a maximum of 3.0 credits. Prerequisite Equivalencies  Math: SL or HL Math Chemistry: SL or HL Chemistry Physics: SL or HL Physics English: SL or HL English '
            #print(ib)
        except:
            ib = None
            #print(ib)

#34 ap
        try:
            ap = 'Advanced standing (transfer) credit may be awarded for Advanced Placement “AP” exams with a minimum grade of 4, subject to the discretion of the appropriate faculty, to a maximum of 3.0 credits.'
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

#38 average_score
        try:
            average_score = response.xpath('//span[@class = "listing-text-icon"]/text()').extract()[0]
            average_score = remove_tags(average_score)
            average_score = average_score.replace(' ','')
         #   print(average_score)
        except:
            average_score = None
          #  print(average_score)

        # sat act 代码 介绍
        sat_code = '0854'
        sat1_desc = 'The Grade 12 program must include at least four academic units and a minimum of 16 academic units completed in Grades 9 to 12. A minimum average in your final years of B- or better is required for admission. For Honours or some limited enrolment programs, a higher average may be required. You are encouraged to submit SAT or ACT scores, school grading information including pass marks, and rank in class to support your application.'
        sat2_desc = None
        act_code = '5376'
        act_desc = 'The Grade 12 program must include at least four academic units and a minimum of 16 academic units completed in Grades 9 to 12. A minimum average in your final years of B- or better is required for admission. For Honours or some limited enrolment programs, a higher average may be required. You are encouraged to submit SAT or ACT scores, school grading information including pass marks, and rank in class to support your application.'

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
        item["average_score"] = average_score
        #yield item