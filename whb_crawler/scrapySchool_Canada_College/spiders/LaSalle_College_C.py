import scrapy
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from scrapySchool_Canada_College import getItem
from w3lib.html import remove_tags
import requests
import re
import time

class BaiduSpider(scrapy.Spider):
    name = 'LaSalle_College_C'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['http://www.lasallecollege.com/business-and-technologies-school/dec-accounting-courses',
'http://www.lasallecollege.com/business-and-technologies-school/dec-business-management-courses',
'http://www.lasallecollege.com/business-and-technologies-school/dec-computer-science-courses-data-processing',
'http://www.lasallecollege.com/business-and-technologies-school/dec-network-administration-courses',
'http://www.lasallecollege.com/business-and-technologies-school/dec-video-game-programming-courses',
'http://www.lasallecollege.com/fashion-arts-design-school/dec-arts-and-letters-option-culture-and-media-courses',
'http://www.lasallecollege.com/fashion-arts-design-school/dec-arts-and-literature-option-design-courses',
'http://www.lasallecollege.com/fashion-arts-design-school/dec-costume-design-courses',
'http://www.lasallecollege.com/fashion-arts-design-school/dec-fashion-design-courses',
'http://www.lasallecollege.com/fashion-arts-design-school/dec-fashion-marketing-courses',
'http://www.lasallecollege.com/fashion-arts-design-school/dec-men-fashion-design-courses',
'http://www.lasallecollege.com/hospitality-management-school/dec-hotel-management',
'http://www.lasallecollege.com/hospitality-management-school/dec-restaurant-management-courses',
'http://www.lasallecollege.com/hospitality-management-school/dec-travel-and-tourism-products-courses',
'http://www.lasallecollege.com/social-sciences-and-education-school/dec-civilization-studies',
'http://www.lasallecollege.com/social-sciences-and-education-school/dec-early-childhood-education-courses',
'http://www.lasallecollege.com/social-sciences-and-education-school/dec-international-studies',
'http://www.lasallecollege.com/social-sciences-and-education-school/dec-social-science-courses',
'http://www.lasallecollege.com/social-sciences-and-education-school/dec-special-care-counselling-courses',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        item = getItem.get_item(ScrapyschoolCanadaCollegeItem)
        try:
            major_name_en = response.xpath('/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/div[1]').extract()[0]
            major_name_en = remove_tags(major_name_en)
            major_name_en = major_name_en.replace('\r\n','').replace('          ','').replace('        ','').replace('      ','')
            #major_name_en =
           # major_name_en = re.findall('(.*) - ',major_name_en)[0]
         #   print(major_name_en)
        except:
            major_name_en = None
         #   print(major_name_en)
#programme_code
        try:
            programme_code = response.xpath('//div[@class = "ProgramDetails"]').extract()[0]
            #programme_code = remove_tags(programme_code)
            programme_code = re.findall('.*\|(.*)', programme_code)[0]
            programme_code = programme_code.lstrip(' ')
            if 'Online' in programme_code:
               programme_code = 'No'
            #print(programme_code)

        except:
            programme_code = None
            #print(programme_code)


        try:
            duration = None


            #print(duration)
        except:
            duration = None
            duration_per = None
            #print(duration)

#1.学校名称
        school_name = 'LaSalle College'


#2.地点
        try:
            location = 'Montreal'
           # location = remove_tags(location)
           # print(location)
        except:
            location = None
          #  print(location)

#3. 校区
        try:
            campus = 'Montreal'
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
            department = response.url
            department = re.findall('http://www.lasallecollege.com/(.*)/.*',department)[0]
            department = department.replace('-',' ')
            if 'online courses' in department:
                department = 'No'
            else:
                pass
            #print(len(department))
           # print(department)
            #print(response.url)
        except:
            department = None
           # print(department)

# 4.
        try:
            degree_level= None
            degree_name = response.xpath('//div[@class = "ProgramDetails"]').extract()[0]
            degree_name = re.findall('(.*)\|.*', degree_name)[0]
            degree_name = remove_tags(degree_name)
            degree_name = degree_name.replace('Ontario College ','').replace(' ','')
            if 'DEC' in degree_name:
                degree_name = 'A diploma of college studies'
            elif 'AEC' in degree_name:
                degree_name = 'An attestation of college studies'
            elif 'DEP' in degree_name:
                degree_name = 'A diploma of vocational studies'
            else:
                pass

           # print(degree_level)
            #print(degree_name)
        except:
            degree_level = None
            degree_name = None
            #print(degree_name)
#
#5.学位描述
        try:
            degree_overview_en = response.xpath('//div[@class = "programContent"]').extract()
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
           # print(degree_overview_en)

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
            start_date = response.xpath('//span[contains(text(),"Semester")]/following-sibling::span[1]').extract()
            start_date = ''.join(start_date)
            start_date = remove_tags(start_date)
            start_date = start_date.replace('2019','').replace('Spring','2019-01,').replace('Winter','2019-01,').replace('Summer','2019-05,').replace('Fall','2019-09,').replace(' | ','').replace(', ',',').replace(', ',',')
            start_date = start_date.rstrip(',')
            #start_date =
            # start_date = start_date.replace('September 2019','2019-09').replace('May 2019','2019-05').replace('July 2019','2019-07').replace('January 2020','2020-01').replace('January 2019','2019-01')
            #start_date = start_date.replace('Jan 2019','2019-01,').replace('Sep 2019','2019-09,').replace('Sep 2018','2018-09,').replace('May 2019','2019-05,').replace('Aug 2018','2018-08,')
            #start_date = start_date.rstrip(',')
            #start_date = start_date.replace(',,',',')
            #print(start_date)
        except:
            start_date = None
            #print(start_date)


#10.课程设置
        try:
            modules_en = response.xpath('//div[contains(text(),"Concentration Courses")]/following-sibling::div|//div[contains(text(),"Specialized training")]/following-sibling::div').extract()
            modules_en = ''.join(modules_en)
            modules_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',modules_en)
            print(modules_en)
        except:
            modules_en = None
            print(modules_en)

#11.就业方向
        try:
            career_en = response.xpath('//div[contains(text(),"Career Prospects")]/following-sibling::div').extract()
            career_en = ''.join(career_en)
            career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',career_en)
            career_en = career_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
           # print(career_en)
        except:
            career_en = None
           # print(career_en)

#12.截止日期
        try:
            deadline = None
            #print(start_date)
            #print(deadline)
        except:
            deadline = None
            #print(deadline)
#13.学费
        try:
            tuition_fee = response.xpath('//h3[contains(text(),"Tuition and Fees")]/following-sibling::div').extract()
            tuition_fee = ''.join(tuition_fee)
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = re.findall('(\$\d\d,\d\d\d\.\d\d)',tuition_fee)[0]
            tuition_fee = tuition_fee.replace('$','')
            #print(tuition_fee)
           # print(response.url)
        except:
            tuition_fee = None
            #print(tuition_fee)
#14 申请费:
        apply_fee = '101'
        try:
            entry_requirements_en = response.xpath('//div[contains(text(),"Admission Criteria")]/following-sibling::div').extract()
            entry_requirements_en = ''.join(entry_requirements_en)
            entry_requirements_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]', '', entry_requirements_en)
            #entry_requirements_en = remove_tags(entry_requirements_en)
            #print(entry_requirements_en)
            #print(abc)
        except:
            entry_requirements_en = None
           # print(entry_requirements_en)
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
            specific_requirement_en = entry_requirements_en
            specific_requirement_en = specific_requirement_en.replace('\n','')
            specific_requirement_en = re.findall('(.*)Note:',specific_requirement_en)
              # #specific_requirement_en = remove_tags(specific_requirement_en)
            specific_requirement_en = ''.join(specific_requirement_en)
            specific_requirement_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',specific_requirement_en)
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

#26 ielts
        try:
            ielts_desc = entry_requirements_en
            ielts_desc = re.findall('IELTS(.*)',ielts_desc)[0]
            #ielts = re.findall('\d\.\d',ielts)
            ielts_desc = remove_tags(ielts_desc)
            ielts_desc = 'IELTS ' + ielts_desc
           # print(ielts_desc)
        except:
            ielts_desc = None
            #print(ielts_desc)
        try:
            ielts_l =  re.findall('.*(\d\.\d).*',ielts_desc)[0]
            ielts = float(ielts_l) + 0.5

            #ielts_desc = remove_tags(ielts_desc)
            #print(ielts)
        except:
            ielts_desc = None
            ielts_l = None
           # print(ielts)

#27 ielts_?

        ielts_s = ielts_l
        ielts_r = ielts_l
        ielts_w = ielts_l
        #print(ielts_l)

#28 toefl_code
        try:
            toefl_code = None
            #toefl_code = remove_tags(toefl_code)
            # print(toefl_code)
        except:
            toefl_code = None
            # print(toefl_code)

#29 toefl_desc
        try:
            toefl_desc = None
            #toefl_desc = remove_tags(toefl_desc)
            # print(toefl_desc)
        except:
            toefl_desc = None
            # print(toefl_desc)

#30 toefl
        try:
            if '6.0' in ielts_l:
                toefl = '83'
            elif '5.5' in ielts_l:
                toefl = '80'
            else:
                toefl = None
            #toefl = re.findall('\d\d',toefl)
            #toefl = remove_tags(toefl)
           # print(toefl)
        except:
            toefl = None
           # print(toefl)

#31 toefl_?
        toefl_l = None
        toefl_s = None
        toefl_r = None
        toefl_w = None






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
            other = '时长在pdf中,deadline,学位类型待确认，fee没有, 学位类型对应网站：http://www.lasallecollege.com/futur-students/study-in-canada 没找到语言要求'
            #other = remove_tags(other)
            # print(other)
        except:
            other = None
            # print(other)

#平均分  average_score
        average_score = None

# degree_name_desc
        try:
            degree_name_desc = overview_en
        except:
            degree_name_desc = None


       # ap = 'Minimum grade of 3 or C '

        item['school_name'] = school_name
        item['location'] = location
        item['campus'] = campus
        item['department'] = department
        item['degree_name'] = degree_name
        item['degree_name_desc'] = degree_name_desc
        item['major_name_en'] = major_name_en
        item['programme_code'] = programme_code
        item['overview_en'] = overview_en
        item['start_date'] = start_date
        item['duration'] = duration
        item['duration_per'] = None
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['deadline'] = deadline
        item['apply_pre'] = 'CAD$'
        item['apply_fee'] = apply_fee
        item['tuition_fee_pre'] = 'CAD$'
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_per'] = '5'
        item['entry_requirements_en'] = entry_requirements_en
        item['require_chinese_en'] = require_chinese_en
        item['specific_requirement_en'] = specific_requirement_en
        item['average_score'] = average_score
        item['gaokao_desc'] = gaokao_desc
        item['gaokao_zs'] = gaokao_zs
        item['huikao_desc'] = huikao_desc
        item['huikao_zs'] = huikao_zs
        item['ielts_desc'] = ''
        item['ielts'] = ''
        item['ielts_l'] = ''
        item['ielts_s'] = ''
        item['ielts_r'] = ''
        item['ielts_w'] = ''
        item['toefl_code'] = toefl_code
        item['toefl_desc'] = toefl_desc
        item['toefl'] = ''
        item['toefl_l'] = ''
        item['toefl_s'] = ''
        item['toefl_r'] = ''
        item['toefl_w'] = ''
        item['interview_desc_en'] = interview_desc_en
        item['portfolio_desc_en'] = portfolio_desc_en
        item['other'] = other
        item['url'] = response.url
        item['degree_level'] = degree_level

        yield item

     #   yield item