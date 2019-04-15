import scrapy
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from scrapySchool_Canada_College import getItem
from w3lib.html import remove_tags
import requests
import re
from lxml import etree

import time
class BaiduSpider(scrapy.Spider):
    name = 'Langara_College_C'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['https://langara.ca/programs-and-courses/programs/access-langara/index.html',
'https://langara.ca/programs-and-courses/programs/arts-general/index.html',
'https://langara.ca/programs-and-courses/programs/art-history/index.html',
'https://langara.ca/programs-and-courses/programs/arts-science-general/index.html',
'https://langara.ca/programs-and-courses/programs/creative-writing/index.html',
'https://langara.ca/programs-and-courses/programs/design-formation/index.html',
'https://langara.ca/programs-and-courses/programs/english/index.html',
'https://langara.ca/programs-and-courses/programs/film-arts/index.html',
'https://langara.ca/programs-and-courses/programs/fine-arts/index.html',
'https://langara.ca/programs-and-courses/programs/general-education/index.html',
'https://langara.ca/programs-and-courses/programs/journalism/index.html',
'https://langara.ca/programs-and-courses/programs/photo-imaging/index.html',
'https://langara.ca/programs-and-courses/programs/publishing/index.html',
'https://langara.ca/programs-and-courses/programs/theatre-arts-studio58/index.html',
'https://langara.ca/programs-and-courses/programs/web-and-mobile-app/index.html',
'https://langara.ca/programs-and-courses/programs/accounting/index.html',
'https://langara.ca/programs-and-courses/programs/accounting-post-degree/index.html',
'https://langara.ca/programs-and-courses/programs/advanced-accounting/index.html',
'https://langara.ca/programs-and-courses/programs/arts-general/index.html',
'https://langara.ca/programs-and-courses/programs/arts-science-general/index.html',
'https://langara.ca/programs-and-courses/programs/business-administration/index.html',
'https://langara.ca/programs-and-courses/programs/business-administration-post-degree/index.html',
'https://langara.ca/programs-and-courses/programs/business-management/index.html',
'https://langara.ca/programs-and-courses/programs/commerce/index.html',
'https://langara.ca/programs-and-courses/programs/commerce-business-studies/index.html',
'https://langara.ca/programs-and-courses/programs/financial-management/index.html',
'https://langara.ca/programs-and-courses/programs/financial-services/index.html',
'https://langara.ca/programs-and-courses/programs/general-education/index.html',
'https://langara.ca/programs-and-courses/programs/international-business/index.html',
'https://langara.ca/programs-and-courses/programs/marketing-management/index.html',
'https://langara.ca/programs-and-courses/programs/marketing-management-post-degree/index.html',
'https://langara.ca/programs-and-courses/programs/nutrition/index.html',
'https://langara.ca/programs-and-courses/programs/applied-science-for-engineering/index.html',
'https://langara.ca/programs-and-courses/programs/arts-science-general/index.html',
'https://langara.ca/programs-and-courses/programs/bioinformatics/index.html',
'https://langara.ca/programs-and-courses/programs/biology/index.html',
'https://langara.ca/programs-and-courses/programs/chemistry/index.html',
'https://langara.ca/programs-and-courses/programs/computer-science/index.html',
'https://langara.ca/programs-and-courses/programs/computer-studies/index.html',
'https://langara.ca/programs-and-courses/programs/data-analytics/index.html',
'https://langara.ca/programs-and-courses/programs/ecology/index.html',
'https://langara.ca/programs-and-courses/programs/engineering/index.html',
'https://langara.ca/programs-and-courses/programs/full-stack-web-development/index.html',
'https://langara.ca/programs-and-courses/programs/general-education/index.html',
'https://langara.ca/programs-and-courses/programs/internet-web-technology/index.html',
'https://langara.ca/programs-and-courses/programs/library-information-technology/index.html',
'https://langara.ca/programs-and-courses/programs/mathematics-statistics/index.html',
'https://langara.ca/programs-and-courses/programs/physics/index.html',
'https://langara.ca/programs-and-courses/programs/science-general/index.html',
'https://langara.ca/programs-and-courses/programs/web-and-mobile-app/index.html',
'https://langara.ca/programs-and-courses/programs/aboriginal-studies/index.html',
'https://langara.ca/programs-and-courses/programs/applied-planning/index.html',
'https://langara.ca/programs-and-courses/programs/applied-social-sciences-and-humanities/index.html',
'https://langara.ca/programs-and-courses/programs/arts-general/index.html',
'https://langara.ca/programs-and-courses/programs/arts-science-general/index.html',
'https://langara.ca/programs-and-courses/programs/asian-studies/index.html',
'https://langara.ca/programs-and-courses/programs/canadian-studies/index.html',
'https://langara.ca/programs-and-courses/programs/classical-studies/index.html',
'https://langara.ca/programs-and-courses/programs/criminal-justice/index.html',
'https://langara.ca/programs-and-courses/programs/early-childhood/index.html',
'https://langara.ca/programs-and-courses/programs/education-assistant/index.html',
'https://langara.ca/programs-and-courses/programs/environmental-studies/index.html',
'https://langara.ca/programs-and-courses/programs/family-studies/index.html',
'https://langara.ca/programs-and-courses/programs/general-education/index.html',
'https://langara.ca/programs-and-courses/programs/geography/index.html',
'https://langara.ca/programs-and-courses/programs/gerontology/index.html',
'https://langara.ca/programs-and-courses/programs/history/index.html',
'https://langara.ca/programs-and-courses/programs/latin-american/index.html',
'https://langara.ca/programs-and-courses/programs/peace-and-conflict-studies/index.html',
'https://langara.ca/programs-and-courses/programs/philosophy/index.html',
'https://langara.ca/programs-and-courses/programs/political-science/index.html',
'https://langara.ca/programs-and-courses/programs/psychology/index.html',
'https://langara.ca/programs-and-courses/programs/social-service/index.html',
'https://langara.ca/programs-and-courses/programs/womens-studies/index.html',
'https://langara.ca/programs-and-courses/programs/advanced-entry-bsn/index.html',
'https://langara.ca/programs-and-courses/programs/arts-general/index.html',
'https://langara.ca/programs-and-courses/programs/arts-science-general/index.html',
'https://langara.ca/programs-and-courses/programs/dietetics/index.html',
'https://langara.ca/programs-and-courses/programs/diversity-and-inclusion/index.html',
'https://langara.ca/programs-and-courses/programs/food-nutrition/index.html',
'https://langara.ca/programs-and-courses/programs/food-nutrition-and-health-transfer/index.html',
'https://langara.ca/programs-and-courses/programs/foundation-health-studies/index.html',
'https://langara.ca/programs-and-courses/programs/general-education/index.html',
'https://langara.ca/programs-and-courses/programs/health-sciences/index.html',
'https://langara.ca/programs-and-courses/programs/kinesiology/index.html',
'https://langara.ca/programs-and-courses/programs/leisure-studies/index.html',
'https://langara.ca/programs-and-courses/programs/nursing/index.html',
'https://langara.ca/programs-and-courses/programs/nursing-leadership-and-management/index.html',
'https://langara.ca/programs-and-courses/programs/nursing-practice-in-canada/index.html',
'https://langara.ca/programs-and-courses/programs/nursing-transition/index.html',
'https://langara.ca/programs-and-courses/programs/recreation-leadership/index.html',
'https://langara.ca/programs-and-courses/programs/recreation-management/index.html',
'https://langara.ca/programs-and-courses/programs/science-general/index.html',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        item = getItem.get_item(ScrapyschoolCanadaCollegeItem)

        try:
            major_name_en = response.xpath('//h1').extract()[0]
            major_name_en = remove_tags(major_name_en)
            #major_name_en = major_name_en.replace('\r\n','').replace('					','').replace('				','')
            if '(' in major_name_en:
                major_name_en = re.findall('(.* )\(.*\)', major_name_en)[0]
            else:
                pass
            #print(major_name_en)
        except:
            major_name_en = None
           # print(major_name_en)
#programme_code
        try:
            programme_code = response.xpath('').extract()[0]
            programme_code = remove_tags(programme_code)
        except:
            programme_code = None

        try:
            duration = response.xpath('').extract()[0]
            duration = remove_tags(duration)
        except:
            duration = None
#1.学校名称
        school_name = 'Langara College'


#2.地点
        try:
            location = 'Vancouver BC'
            location = remove_tags(location)
            #print(location)
        except:
            location = None
            #print(location)

#3. 校区
        try:
            campus = 'main'
            # campus = remove_tags(campus)
            # campus = campus.replace(', Online','')
            # campus = campus.replace(' ','')
            # campus = campus.split(',')
            #print(campus)
        except:
            campus = None
            #print(campus)

#4. 学院
        try:
            department = response.xpath('//div[contains(text(),"Department")]/following-sibling::div/p').extract()[0]
            department = remove_tags(department)

            #print(len(department))
            #print(department)
            #print(response.url)
        except:
            department = None
            #print(department)

# 4.
        try:
            degree_name_list = response.xpath('//div[contains(text(),"Credential")]/following-sibling::div/p').extract()[0]
            #degree_name_list = remove_tags(degree_name_list,keep=('li','ul'))
            #degree_name_list = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_name_list)
            #degree_name_list = degree_name_list.replace('\t','').replace('\n','').replace('\xa0','').replace(' class="list-inline uofs-cta-list','')
            # degree_name_list = degree_name_list.replace('<li>','').replace('</li>','---')
            # degree_name_list = degree_name_list.replace('<span>','').replace('</span>','---')
           # degree_name_list = degree_name_list.split('</li><li>')
            degree_name_list = remove_tags(degree_name_list)
            degree_name_list = degree_name_list.split(',')

            #print(degree_name_list)

            #print(response.url)
        except:
            degree_name_list = ['No']

#
#5.学位描述
        try:
            degree_overview_en = response.xpath('//h2[contains(text(),"Overview")]/following-sibling::div[1]').extract()
            degree_overview_en = ''.join(degree_overview_en)
            degree_overview_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_overview_en)
           # print(degree_overview_en)

        except:
            degree_overview_en = None
          #  print(degree_overview_en)


        # 14 申请费:
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
            start_date = response.xpath('//div[contains(text(),"Start Date")]/following-sibling::div/p').extract()
            start_date = ','.join(start_date)
            start_date = remove_tags(start_date)
            if 'September, January, May' in start_date or 'September, January (Acting); January (Production)' in start_date:
                start_date = '2019-09,2019-01,2019-05'
            elif 'September, January' in start_date:
                start_date = '2019-09,2019-01'
            elif 'January, May' in start_date:
                start_date = '2019-01,2019-05'
            elif 'September and January' in start_date:
                start_date = '2019-09,2019-01'
            elif 'January, September' in start_date:
                start_date = '2019-09,2019-01'
            elif 'May' in start_date:
                start_date = '2019-05'
            elif 'September' in start_date:
                start_date = '2019-09'
            elif 'January' in start_date:
                start_date = '2019-01'
            #elif ''
            # start_date = start_date.replace('Spring','').replace('Winter','').replace('Summer','').replace('Fall','')
            # start_date = start_date.replace('September 2019','2019-09').replace('May 2019','2019-05').replace('July 2019','2019-07').replace('January 2020','2020-01').replace('January 2019','2019-01')
            #print(start_date)
        except:
            start_date = None
            #print(start_date)
#9.课程长度
        try:
            duration = response.xpath('//div[contains(text(),"Duration")]/following-sibling::div/p').extract()[0]
            duration = remove_tags(duration)
            duration_per = '1'

            if 'months' in duration:
                duration = 'No'
                duration_per = None
            elif  'year' in duration or 'Year' in duration:
                duration_per = '1'
                if '2-3 ' in duration:
                    duration = '2,3'
                elif '2 years / 4 consecutive semesters' in duration:
                    duration = '2'
                elif '2 years / 6 consecutive semesters' in duration:
                    duration = '2'
                elif '4' in duration:
                    duration = '4'
                elif '3' in duration:
                    duration = '3'
                elif '2' in duration:
                    duration = '2'
                elif '1' in duration:
                    duration = '1'
            elif 'Semesters' in duration or 'Semester' in duration or 'term' in duration:
                duration_per = '5'
                if '4' in duration:
                    duration = '4'
                elif '3' in duration:
                    duration = '3'
                elif '2' in duration:
                    duration = '2'
                elif '1' in duration:
                    duration = '1'
                elif 'One' in duration:
                    duration = '1'
                elif 'Two' in duration:
                    duration = '2'
                elif 'Three' in duration:
                    duration = '3'
            elif '3 full-time semesters (Diploma), 2 semesters (Citation)' in duration:
                duration_per = '5'
                duration = '3'
            elif '69 Credits' in duration:
                    duration = 'Yes'
           # print(duration)

        except:
            duration = None
            #degree_level= None
           # print(duration)

#10.课程设置
        try:
            url = response.url
            url = url.replace('index','program-curriculum')
            #print(url)
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
            response1 = requests.get(url,headers=headers)
            modules_en = response1.text
            modules_en = ''.join(modules_en)
            modules_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',modules_en)
            modules_en = modules_en.replace('\n','')
            modules_en = re.findall('.*(<h2>Program Curriculum</h2>.*)<p><strong>Program Notes:</strong>',modules_en)[0]
            #modules_en = ''
           # print(modules_en)
        except:
            modules_en = None
          #  print(modules_en)

#11.就业方向
        try:
            url = response.url
            url = url.replace('index','career-opportunities')
            #print(url)
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
            response2 = requests.get(url,headers=headers)
            career_en = response2.text
            career_en = ''.join(career_en)
            career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',career_en)
            career_en = career_en.replace('\n','')
            career_en = re.findall('.*(<h2>Career Opportunities</h2>.*)',career_en)[0]
          #  career_en = ''
            #print(career_en)
        except:
            career_en = None
           # print(career_en)

#12.截止日期
        try:
            deadline = start_date.replace('2019-09','2019-05-31').replace('2019-05','2019-02-28').replace('2019-01','2019-10-31')
            # deadline = response.xpath('//*[@id="Admissionrequirementsanddeadlines-subsection-0"]/table/tbody/tr/td[3]').extract()
            # deadline = '---'.join(deadline)
            # deadline = remove_tags(deadline)
            # deadline = deadline.replace ('Documents due: ', '')
            # deadline =  deadline.replace('Sep 1, 2018Oct 1, 2018','2018-09-01').replace('Feb 1, 2019Mar 1, 2019','2019-02-01').replace('Mar 1, 2019Apr 1, 2019','2019-03-01').replace('May 1, 2019Jun 1, 2019','2019-05-01').replace('Sep 1, 2019Oct 1, 2019','2019-09-01').replace('Feb 15, 2019Mar 1, 2019','2019-02-15').replace('---',',')
            # #deadline = remove_tags(deadline)
           # print(deadline)
        except:
            deadline = None
            #print(deadline)
#13.学费
        try:
            tuition_fee = '17,700'
            #tuition_fee = remove_tags(tuition_fee)
            #tuition_fee = tuition_fee.replace('$','')
            #print(tuition_fee)
        except:
            tuition_fee = None
            #print(tuition_fee)
#14 申请费:
        apply_fee = '155'
        try:

            url = response.url
            url = url.replace('index','admission-requirements')
            #print(url)
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
            response3 = requests.get(url,headers=headers)
            entry_requirements_en = response3.text
            entry_requirements_en = ''.join(entry_requirements_en)
            entry_requirements_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',entry_requirements_en)
            entry_requirements_en = entry_requirements_en.replace('\n','')
            entry_requirements_en = re.findall('.*(<h2>Admission Requirements</h2>.*)Contact Us',entry_requirements_en)[0]
           # print(entry_requirements_en)
           # entry_requirements_en = ''
        except:
            entry_requirements_en = None
            #print(entry_requirements_en)
#16 中国学生申请要求
        try:
            require_chinese_en = '<p>Senior High School or Senior Middle School Diploma and transcript for Seniors Years 1-3</p>'
           # require_chinese_en = remove_tags(require_chinese_en)
            # print(require_chinese_en)
        except:
            require_chinese_en = None
            # print(require_chinese_en)

#17 特殊专业要求
        try:
            specific_requirement_en = response.xpath('').extract()[0]
            # #specific_requirement_en = remove_tags(specific_requirement_en)
            # specific_requirement_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',specific_requirement_en)
            # specific_requirement_en = specific_requirement_en.replace('\r\n','')
            # specific_requirement_en = re.findall('Required high school classes(.*)2.',specific_requirement_en)[0]
            # specific_requirement_en = remove_tags(specific_requirement_en,keep=("li","ul"))
            # #print(specific_requirement_en)
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
            toefl_code = '0335'
            #toefl_code = remove_tags(toefl_code)
            # print(toefl_code)
        except:
            toefl_code = None
            # print(toefl_code)

#29 toefl_desc
        try:
            toefl_desc = 'TOEFL (Internet-based) with a total score of 80 or higher and a minimum of 18 in Listening, 20 in Reading, 18 in Speaking, and 20 in Writing'
            #toefl_desc = remove_tags(toefl_desc)
            # print(toefl_desc)
        except:
            toefl_desc = None
            # print(toefl_desc)

#30 toefl
        try:
            toefl = '80'
            #toefl = re.findall('\d\d',toefl)
            #toefl = remove_tags(toefl)
            #print(toefl)
        except:
            toefl = None
           # print(toefl)

#31 toefl_?
        toefl_l = 18
        toefl_s = 20
        toefl_r = 18
        toefl_w = 20




#34 ap
        try:
            ap = None
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
            other = '1.课程设置,就业,入学要求 需要跳转3个链接抓取,缺少数据是因为不同界面拥有的字段不一样,'
            #other = remove_tags(other)
            # print(other)
        except:
            other = None
            # print(other)

#平均分  average_score
        average_score = '60'

# degree_name_desc
        try:
            degree_name_desc = degree_overview_en
        except:
            degree_name_desc = None


        item['school_name'] = school_name
        item['location'] = location
        item['campus'] = campus
        item['department'] = department
        #item['degree_name'] = degree_name
        item['degree_name_desc'] = degree_name_desc
        item['major_name_en'] = major_name_en
        item['programme_code'] = programme_code
        item['overview_en'] = overview_en
        item['start_date'] = start_date
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['deadline'] = deadline
        item['apply_pre'] = 'CAD$'
        item['apply_fee'] = apply_fee
        item['tuition_fee_pre'] = 'CAD$'
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_per'] = '1'
        item['entry_requirements_en'] = entry_requirements_en
        item['require_chinese_en'] = require_chinese_en
        item['specific_requirement_en'] = specific_requirement_en
        item['average_score'] = average_score
        item['gaokao_desc'] = gaokao_desc
        item['gaokao_zs'] = gaokao_zs
        item['huikao_desc'] = huikao_desc
        item['huikao_zs'] = huikao_zs
        item['ielts_desc'] = ielts_desc
        item['ielts'] = ielts
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['toefl_code'] = toefl_code
        item['toefl_desc'] = toefl_desc
        item['toefl'] = toefl
        item['toefl_l'] = toefl_l
        item['toefl_s'] = toefl_s
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['interview_desc_en'] = interview_desc_en
        item['portfolio_desc_en'] = portfolio_desc_en
        item['other'] = other
        item['url'] = response.url
        for degree_names in degree_name_list:
            degree_name = degree_names
            degree_name = degree_name.replace(' Baccalaureate Degree','Baccalaureate Degree')
            if 'Post-Degree Diploma' in degree_name:
                degree_level  = '2'
            elif 'Baccalaureate Degree' in degree_name:
                degree_level = '1'
            elif 'Associate of Arts Degree' in degree_name:
                degree_level = '4'
            elif 'Diploma' in degree_name:
                degree_level = '3'
            else:
                degree_level = 'No'

            item['degree_name'] = degree_name
            item['degree_level'] = degree_level
            yield item
            # print(degree_name)
            # print(degree_level)

            # if 'No' not in duration and 'Yes' not in duration and 'No' not in degree_level:
            #     yield
            #     #pass
            # elif 'Yes' in duration and 'No' not in degree_level:
            #     item["duration"] = None
            #     yield item
