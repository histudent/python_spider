import scrapy
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from scrapySchool_Canada_Ben import getItem
from w3lib.html import remove_tags
import requests
import re
import time

class BaiduSpider(scrapy.Spider):
    name = 'university_of_saskatchewan_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['https://admissions.usask.ca/aboriginal-business-administration.php',
'https://admissions.usask.ca/kanawayihetaytan-askiy.php',
'https://admissions.usask.ca/accounting.php',
'https://admissions.usask.ca/agribusiness.php',
'https://admissions.usask.ca/agricultural-biology.php',
'https://admissions.usask.ca/agricultural-economics.php',
'https://admissions.usask.ca/agronomy.php',
'https://admissions.usask.ca/anatomy-cell-biology.php',
'https://admissions.usask.ca/animal-bioscience.php',
'https://admissions.usask.ca/animal-science.php',
'https://admissions.usask.ca/anthropology.php',
'https://admissions.usask.ca/applied-mathematics.php',
'https://admissions.usask.ca/applied-plant-ecology.php',
'https://admissions.usask.ca/archaeology.php',
'https://admissions.usask.ca/art-history.php',
'https://admissions.usask.ca/biochemistry.php',
'https://admissions.usask.ca/bioinformatics.php',
'https://admissions.usask.ca/biology.php',
'https://admissions.usask.ca/business-administration.php',
'https://admissions.usask.ca/business-economics.php',
'https://admissions.usask.ca/career-and-guidance-studies.php',
'https://admissions.usask.ca/chemical-engineering.php',
'https://admissions.usask.ca/chemistry.php',
'https://admissions.usask.ca/civil-engineering.php',
'https://admissions.usask.ca/classical-medieval-latin.php',
'https://admissions.usask.ca/classical-medieval-renaissance-studies.php',
'https://admissions.usask.ca/computer-engineering.php',
'https://admissions.usask.ca/computer-science.php',
'https://admissions.usask.ca/criminology-addictions.php',
'https://admissions.usask.ca/crop-science.php',
'https://admissions.usask.ca/dental-assisting.php',
'https://admissions.usask.ca/dentistry.php',
'https://admissions.usask.ca/drama.php',
'https://admissions.usask.ca/economics.php',
'https://admissions.usask.ca/education.php',
'https://admissions.usask.ca/education-sequential-music.php',
'https://admissions.usask.ca/electrical-engineering.php',
'https://admissions.usask.ca/engineering-physics.php',
'https://admissions.usask.ca/english.php',
'https://admissions.usask.ca/english-as-an-additional-language.php',
'https://admissions.usask.ca/english-for-academic-purposes.php',
'https://admissions.usask.ca/environment-society.php',
'https://admissions.usask.ca/environmental-biology.php',
'https://admissions.usask.ca/environmental-earth-sciences.php',
'https://admissions.usask.ca/environmental-engineering.php',
'https://admissions.usask.ca/environmental-science.php',
'https://admissions.usask.ca/ethics-justice-law.php',
'https://admissions.usask.ca/exercise-and-sport-studies.php',
'https://admissions.usask.ca/finance.php',
'https://admissions.usask.ca/food-and-bioproduct-sciences.php',
'https://admissions.usask.ca/food-science.php',
'https://admissions.usask.ca/french.php',
'https://admissions.usask.ca/geological-engineering.php',
'https://admissions.usask.ca/geology.php',
'https://admissions.usask.ca/geophysics.php',
'https://admissions.usask.ca/global-studies.php',
'https://admissions.usask.ca/health-studies.php',
'https://admissions.usask.ca/history.php',
'https://admissions.usask.ca/horticulture-science.php',
'https://admissions.usask.ca/human-resources.php',
'https://admissions.usask.ca/itep.php',
'https://admissions.usask.ca/indigenous-governance-politics.php',
'https://admissions.usask.ca/indigenous-languages.php',
'https://admissions.usask.ca/indigenous-studies.php',
'https://admissions.usask.ca/interactive-systems-design.php',
'https://admissions.usask.ca/international-studies.php',
'https://admissions.usask.ca/internationally-educated-teachers.php',
'https://admissions.usask.ca/jazz.php',
'https://admissions.usask.ca/jewish-christian-origins.php',
'https://admissions.usask.ca/kanawayihetaytan-askiy.php',
'https://admissions.usask.ca/kinesiology-education.php',
'https://admissions.usask.ca/law.php',
'https://admissions.usask.ca/leadership-in-post-secondary-education.php',
'https://admissions.usask.ca/linguistics.php',
'https://admissions.usask.ca/management.php',
'https://admissions.usask.ca/marketing.php',
'https://admissions.usask.ca/mathematical-physics.php',
'https://admissions.usask.ca/mathematics.php',
'https://admissions.usask.ca/mechanical-engineering.php',
'https://admissions.usask.ca/medicine.php',
'https://admissions.usask.ca/microbiology-immunology.php',
'https://admissions.usask.ca/modern-languages.php',
'https://admissions.usask.ca/music.php',
'https://admissions.usask.ca/music-education.php',
'https://admissions.usask.ca/nursing.php',
'https://admissions.usask.ca/nutrition.php',
'https://admissions.usask.ca/operations-management.php',
'https://admissions.usask.ca/palaeobiology.php',
'https://admissions.usask.ca/pharmacy.php',
'https://admissions.usask.ca/philosophy.php',
'https://admissions.usask.ca/physics.php',
'https://admissions.usask.ca/physiology-pharmacology.php',
'https://admissions.usask.ca/political-studies.php',
'https://admissions.usask.ca/practical-and-applied-arts.php',
'https://admissions.usask.ca/prairie-horticulture.php',
'https://admissions.usask.ca/professional-communication.php',
'https://admissions.usask.ca/psychology.php',
'https://admissions.usask.ca/regional-urban-planning.php',
'https://admissions.usask.ca/religion-culture.php',
'https://admissions.usask.ca/resource-economics-and-policy.php',
'https://admissions.usask.ca/resource-science.php',
'https://admissions.usask.ca/suntep.php',
'https://admissions.usask.ca/sociology.php',
'https://admissions.usask.ca/soil-science.php',
'https://admissions.usask.ca/special-education.php',
'https://admissions.usask.ca/statistics.php',
'https://admissions.usask.ca/studio-art.php',
'https://admissions.usask.ca/sustainability.php',
'https://admissions.usask.ca/english-as-a-second-language.php',
'https://admissions.usask.ca/technical-vocational-education.php',
'https://admissions.usask.ca/toxicology.php',
'https://admissions.usask.ca/veterinary-medicine.php',
'https://admissions.usask.ca/wicehtowin-theatre.php',
'https://admissions.usask.ca/womens-gender-studies.php',]
    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        item = getItem.get_item(ScrapyschoolCanadaBenItem)



#1.学校名称
        school_name = 'University of Saskatchewan'
#2.地点
        try:
            location = 'Saskatoon, Saskatchewan'
            location = remove_tags(location)
            #print(location)
        except:
            location = None
            #print(location)

#3. 校区
        try:
            campus_list = response.xpath('').extract()[0]
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
            department = response.xpath('//h4').extract()[0]
            department = remove_tags(department,keep=("i"))
            department = department.replace(' class="fa fa-graduation-cap"','').replace(' class="fa fa-university"','')
            department = department.replace(' <i> </i> ','<i></i>').replace('<i> </i> ','')
            department = department.split('<i></i>')[-1]
            #print(len(department))
            #print(department)
            #print(response.url)
        except:
            department = None
            #print(department)

# 4.
        try:
            degree_name_list = response.xpath('//h1[contains(text(),"Program options")]/following-sibling::div[1]/ul').extract()[0]
            degree_name_list = remove_tags(degree_name_list,keep=('li','ul'))
            #degree_name_list = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_name_list)
            degree_name_list = degree_name_list.replace('\t','').replace('\n','').replace('\xa0','').replace(' class="list-inline uofs-cta-list','')
            # degree_name_list = degree_name_list.replace('<li>','').replace('</li>','---')
            # degree_name_list = degree_name_list.replace('<span>','').replace('</span>','---')
            degree_name_list = degree_name_list.split('</li><li>')
            #print(degree_name_list)
            #print(response.url)
        except:

            degree_name_list = None
            #print(degree_name_list)

#5.学位描述
        try:
            degree_overview_en = response.xpath('//h1[contains(text(),"About")]/following-sibling::div//p').extract()
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
            major_name_en = response.xpath('//div/h1').extract()[0]
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
            start_date = response.xpath('//*[@id="Admissionrequirementsanddeadlines-subsection-0"]/table/tbody/tr/td[1]').extract()
            start_date = ','.join(start_date)
            start_date = remove_tags(start_date)
            start_date = start_date.replace('Spring','').replace('Winter','').replace('Summer','').replace('Fall','')
            start_date = start_date.replace('September 2019','2019-09').replace('May 2019','2019-05').replace('July 2019','2019-07').replace('January 2020','2020-01').replace('January 2019','2019-01')
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
            modules_en = response.xpath('//*[@id="accordion-3"]').extract()[0]
            modules_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',modules_en)
            modules_en = modules_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
            #print(modules_en)
        except:
            modules_en = None
            #print(modules_en)

#11.就业方向
        try:
            career_en = response.xpath('//*[@id="Careers-subsection-0"]').extract()[0]
            career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',career_en)
            career_en = career_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
            #print(career_en)
        except:
            career_en = None
            #print(career_en)

#12.截止日期
        try:
            #deadline = '2019-03-01'
            deadline = response.xpath('//*[@id="Admissionrequirementsanddeadlines-subsection-0"]').extract()
            deadline = ''.join(deadline)
            deadline = remove_tags(deadline)
            if 'May 1, 2019' in deadline:
                dead1 = '2019-05-01,'
            else:
                dead1 = ''
            if 'April 1, 2019' in deadline:
                dead2 = '2019-04-01,'
            else:
                dead2 = ''
            if 'July 1, 2019' in deadline:
                dead3 = '2019-07-01,'
            else:
                dead3 = ''
            if 'December 1, 2019' in deadline:
                dead4 = '2019-12-01,'
            else:
                dead4 = ''
            if 'Sep 1, 2018' in deadline:
                dead5 = '2018-09-01,'
            else:
                dead5 = ''
            if 'Feb 1, 2019' in deadline:
                dead6 = '2019-02-01,'
            else:
                dead6 = ''
            if 'Mar 1, 2019' in deadline:
                dead7 = '2019-03-01,'
            else:
                dead7 = ''
            if 'Feb 15, 2019' in deadline:
                dead8 = '2019-02-15'
            else:
                dead8 = ''
            if 'Oct 1, 2018' in deadline:
                dead9 = '2018-10-01'
            else:
                dead9 = ''
            if 'Sep 1, 2019' in deadline:
                dead10 = '2019-09-01'
            else:
                dead10 = ''
            deadline = dead1 + dead2 + dead3 + dead4 +dead5 + dead6 + dead7 + dead8 + dead9 + dead10
            #deadline = remove_tags(deadline)
            #print(deadline)
        except:
            deadline = None
            #print(deadline)
#13.学费
        try:
            tuition_fee = response.xpath('//*[@id="Tuitionestimates-subsection-0"]/table/tbody/tr[2]/td[3]').extract()[0]
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = tuition_fee.replace('$','')
            #print(tuition_fee)
        except:
            tuition_fee = None
            #print(tuition_fee)
#14 申请费:
        apply_fee = '90'

#15 申请要求
        try:
            url = 'https://admissions.usask.ca/documents/admissions/results.php'
            body = {"studenttype":"HS", "institution":"INT-CN", "program":"en"}
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
            abc = response.xpath('//script').extract()
            abc = ''.join(abc)
            abc = abc.replace('\r\n','')
            abc = re.findall('var program = "(.*?)"',abc)[0]
            body["program"] = abc
            entry_requirements_en = response.xpath('//*[@id="adm_form"]').extract()
            response1 = requests.post(url, data=body, headers=headers)
            #print(response.text)

            entry_requirements_en = response1.text
            entry_requirements_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',entry_requirements_en)
            #entry_requirements_en = ''.join(entry_requirements_en)
            #entry_requirements_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',entry_requirements_en)
            #entry_requirements_en = remove_tags(entry_requirements_en)
            print(entry_requirements_en)
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
            specific_requirement_en = response1.text
            #specific_requirement_en = remove_tags(specific_requirement_en)
            specific_requirement_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',specific_requirement_en)
            specific_requirement_en = specific_requirement_en.replace('\r\n','')
            specific_requirement_en = re.findall('Required high school classes(.*)2.',specific_requirement_en)[0]
            specific_requirement_en = remove_tags(specific_requirement_en,keep=("li","ul"))
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
            min_language_require = 'Overall Band Score: 6.5 With minimum individual scores of Reading: 6﻿﻿ Listening: 6 ﻿Speaking: 6 ﻿Writing: 6 or Minimum Score: 86 (no component score less than 19)'
            min_language_require = remove_tags(min_language_require)
            # print(min_language_require)
        except:
            min_language_require = None
            # print(min_language_require)

#25 雅思要求
        try:
            ielts_desc = 'Overall Band Score: 6.5 With minimum individual scores of Reading: 6﻿﻿ Listening: 6 ﻿Speaking: 6 ﻿Writing: 6'
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
            toefl_code = '0980'
            #toefl_code = remove_tags(toefl_code)
            # print(toefl_code)
        except:
            toefl_code = None
            # print(toefl_code)

#29 toefl_desc
        try:
            toefl_desc = 'Internet Based: 86,With minimum individual scores of,Reading: 19,Listening: 19,Speaking: 19﻿,Writing: 19﻿'
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
            ib = 'International Baccalaureate (IB) students,After applying for admission, upload a statement of your anticipated/predicted IB scores. Upon completion of your IB examinations, arrange for your official IB transcript of grades to be sent directly to the University of Saskatchewan by the IB organization. '
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
            other = ''
            #other = remove_tags(other)
            # print(other)
        except:
            other = None
            # print(other)

        # sat act 代码 介绍
        sat_code = '0980'
        sat1_desc = None
        sat2_desc = None
        act_code = None
        act_desc = None
        if '70%' in entry_requirements_en:
            average_score = '70%'
        elif '71%' in entry_requirements_en:
            average_score = '70%'
        elif '72%' in entry_requirements_en:
            average_score = '72%'
        elif '73%' in entry_requirements_en:
            average_score = '73%'
        elif '74%' in entry_requirements_en:
            average_score = '74%'
        elif '75%' in entry_requirements_en:
            average_score = '75%'
        else:
            average_score = None
        item["average_score"] = average_score
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
        item["average_score"] = '75'
        bbcccc  =  response.xpath('//body')
        try:
            if len(degree_name_list) == 1 or len(degree_name_list) == None:
                degree_name_list = response.xpath('//h4').extract()[0]
                degree_name_list = remove_tags(degree_name_list,keep=("i"))
                degree_name_list = degree_name_list.replace(' class="fa fa-graduation-cap"','').replace(' class="fa fa-university"','')
                degree_name_list = degree_name_list.replace(' <i> </i> ','<i></i>').replace('<i> </i> ','')
                degree_name_list = degree_name_list.split('<i></i>')[0]
                degree_name_list = degree_name_list.replace('Certificate in Secondary Technical Vocational Education (C.S.T.V.E.)','')

                item["degree_name"] = degree_name_list
                #degree_name_list = degree_name_list.split('')
                item["duration"] = None
                #print(degree_name_list)
                if 'Certificate' not in item["degree_name"] and 'Diploma' not in item[
                    "degree_name"] and 'Diploma' not in item["degree_name"] and 'Dip' not in item[
                    "degree_name"] and 'Double Honours' not in item["degree_name"] and 'This program is under review' not in bbcccc:
                    yield item
                    #pass


            else:
                for i in degree_name_list:
                    i = i.replace('</li></ul>','').replace('<ul><li>','')
                    if 'Honours' in i:
                        item["duration"] = 4
                    elif 'Three-year' in i:
                        item["duration"] = 3
                    elif 'Four-year' in i:
                        item["duration"] = 4
                    else:
                        item["duration"] = None
                    i = i.replace('Three-year','').replace('Four-year','')
                    item["degree_name"] = i
                    #print(["duration"])
                    #print(item["degree_name"])
                    if 'Certificate' not in item["degree_name"] and 'Diploma' not in item["degree_name"] and 'Diploma' not in item["degree_name"] and 'Dip' not in item["degree_name"] and 'Double Honours' not in item["degree_name"] and 'This program is under review' not in bbcccc:

                       yield item
                        #pass

        except:
            item["duration"] = None
            item["degree_name"] = None
                    #print(response.url)


            yield item



