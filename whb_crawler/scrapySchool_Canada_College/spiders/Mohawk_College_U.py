import scrapy
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from scrapySchool_Canada_College import getItem
from w3lib.html import remove_tags
import requests
import re
import time

class BaiduSpider(scrapy.Spider):
    name = 'Mohawk_College_C'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['https://www.mohawkcollege.ca/programs/graduate-studies/autism-and-behavioural-science-164',
'https://www.mohawkcollege.ca/programs/graduate-studies/brain-disorders-management-470',
'https://www.mohawkcollege.ca/programs/graduate-studies/business-analysis-334',
'https://www.mohawkcollege.ca/programs/graduate-studies/communications-media-practices-266',
'https://www.mohawkcollege.ca/programs/graduate-studies/concurrent-disorders-252',
'https://www.mohawkcollege.ca/programs/communication-arts/creative-arts-business-387',
'https://www.mohawkcollege.ca/programs/community-services/educational-support-intensive-997',
'https://www.mohawkcollege.ca/programs/business/global-business-management-international-only-967',
'https://www.mohawkcollege.ca/programs/business/global-business-management-family-enterprise-international-only-970',
'https://www.mohawkcollege.ca/programs/graduate-studies/human-resources-management-113',
'https://www.mohawkcollege.ca/programs/graduate-studies/international-business-management-116',
'https://www.mohawkcollege.ca/programs/graduate-studies/mental-health-and-disability-management-475',
'https://www.mohawkcollege.ca/programs/graduate-studies/public-relations-166',
'https://www.mohawkcollege.ca/programs/business/supply-chain-management-385',
'https://www.mohawkcollege.ca/programs/business/advertising-and-marketing-communications-management-652',
'https://www.mohawkcollege.ca/programs/communication-arts/animation-3d-373',
'https://www.mohawkcollege.ca/programs/communication-arts/applied-music-bass-986',
'https://www.mohawkcollege.ca/programs/communication-arts/applied-music-classical-piano-981',
'https://www.mohawkcollege.ca/programs/communication-arts/applied-music-classical-strings-guitar-976',
'https://www.mohawkcollege.ca/programs/communication-arts/applied-music-classical-voice-983',
'https://www.mohawkcollege.ca/programs/communication-arts/applied-music-classical-winds-brass-977',
'https://www.mohawkcollege.ca/programs/communication-arts/applied-music-contemporary-brass-winds-979',
'https://www.mohawkcollege.ca/programs/communication-arts/applied-music-contemporary-guitar-980',
'https://www.mohawkcollege.ca/programs/communication-arts/applied-music-contemporary-piano-982',
'https://www.mohawkcollege.ca/programs/communication-arts/applied-music-contemporary-voice-984',
'https://www.mohawkcollege.ca/programs/communication-arts/applied-music-drums-percussion-978',
'https://www.mohawkcollege.ca/programs/communication-arts/applied-music-other-985',
'https://www.mohawkcollege.ca/programs/communication-arts/applied-music-660',
'https://www.mohawkcollege.ca/programs/communication-arts/art-and-design-foundations-270',
'https://www.mohawkcollege.ca/programs/communication-arts/broadcasting-radio-220',
'https://www.mohawkcollege.ca/programs/communication-arts/broadcasting-television-and-communications-media-651',
'https://www.mohawkcollege.ca/programs/graduate-studies/communications-media-practices-266',
'https://www.mohawkcollege.ca/programs/communication-arts/creative-arts-business-387',
'https://www.mohawkcollege.ca/programs/preparatory-studies/general-arts-and-science-college-transfer-230',
'https://www.mohawkcollege.ca/programs/preparatory-studies/general-arts-and-science-university-transfer-208',
'https://www.mohawkcollege.ca/programs/communication-arts/graphic-design-508',
'https://www.mohawkcollege.ca/programs/communication-arts/journalism-297',
'https://www.mohawkcollege.ca/programs/communication-arts/photography-still-and-motion-378',
'https://www.mohawkcollege.ca/programs/graduate-studies/public-relations-166',
'https://www.mohawkcollege.ca/programs/graduate-studies/autism-and-behavioural-science-164',
'https://www.mohawkcollege.ca/programs/graduate-studies/brain-disorders-management-470',
'https://www.mohawkcollege.ca/programs/community-services/child-and-youth-care-612',
'https://www.mohawkcollege.ca/programs/community-services/community-and-justice-services-286-288',
'https://www.mohawkcollege.ca/programs/graduate-studies/concurrent-disorders-252',
'https://www.mohawkcollege.ca/programs/community-services/early-childhood-education-213',
'https://www.mohawkcollege.ca/programs/community-services/educational-support-intensive-997',
'https://www.mohawkcollege.ca/programs/community-services/educational-support-747',
'https://www.mohawkcollege.ca/programs/preparatory-studies/general-arts-and-science-college-transfer-230',
'https://www.mohawkcollege.ca/programs/preparatory-studies/general-arts-and-science-university-transfer-208',
'https://www.mohawkcollege.ca/programs/community-services/health-wellness-and-fitness-268',
'https://www.mohawkcollege.ca/programs/community-services/massage-therapy-469',
'https://www.mohawkcollege.ca/programs/graduate-studies/mental-health-and-disability-management-475',
'https://www.mohawkcollege.ca/programs/business/paralegal-285',
'https://www.mohawkcollege.ca/programs/community-services/protection-security-and-investigation-293-294',
'https://www.mohawkcollege.ca/programs/community-services/social-service-worker-215',
'https://www.mohawkcollege.ca/programs/graduate-studies/autism-and-behavioural-science-164',
'https://www.mohawkcollege.ca/programs/health/canadian-health-care-for-foreign-trained-professionals-international-only-993',
'https://www.mohawkcollege.ca/programs/graduate-studies/concurrent-disorders-252',
'https://www.mohawkcollege.ca/programs/preparatory-studies/general-arts-and-science-college-transfer-230',
'https://www.mohawkcollege.ca/programs/preparatory-studies/general-arts-and-science-university-transfer-208',
'https://www.mohawkcollege.ca/programs/community-services/health-wellness-and-fitness-268',
'https://www.mohawkcollege.ca/programs/community-services/massage-therapy-469',
'https://www.mohawkcollege.ca/programs/health/occupational-therapist-assistant-and-physiotherapist-assistant-746',
'https://www.mohawkcollege.ca/programs/business/office-administration-health-services-335',
'https://www.mohawkcollege.ca/programs/health/personal-support-worker-110',
'https://www.mohawkcollege.ca/programs/health/pharmacy-technician-407',
'https://www.mohawkcollege.ca/programs/health/recreation-therapy-283',
'https://www.mohawkcollege.ca/programs/skilled-trades/electrical-engineering-technician-power-403-433',
'https://www.mohawkcollege.ca/programs/preparatory-studies/general-arts-and-science-college-transfer-230',
'https://www.mohawkcollege.ca/programs/preparatory-studies/general-arts-and-science-university-transfer-208',
'https://www.mohawkcollege.ca/programs/skilled-trades/manufacturing-engineering-technician-automation-industrial-mechanic',
'https://www.mohawkcollege.ca/programs/skilled-trades/motive-power-fundamentals-187',
'https://www.mohawkcollege.ca/programs/skilled-trades/motive-power-technician-446',
'https://www.mohawkcollege.ca/programs/skilled-trades/power-engineering-techniques-482',
'https://www.mohawkcollege.ca/programs/technology/architectural-technician-420',
'https://www.mohawkcollege.ca/programs/technology/architectural-technology-531',
'https://www.mohawkcollege.ca/programs/technology/aviation-technician-aircraft-maintenance-269',
'https://www.mohawkcollege.ca/programs/technology/aviation-technician-aircraft-structures-289',
'https://www.mohawkcollege.ca/programs/technology/biotechnology-health-370-670',
'https://www.mohawkcollege.ca/programs/technology/biotechnology-369-669',
'https://www.mohawkcollege.ca/programs/technology/chemical-engineering-technology-533',
'https://www.mohawkcollege.ca/programs/technology/civil-engineering-technician-421',
'https://www.mohawkcollege.ca/programs/technology/civil-engineering-technology-534',
'https://www.mohawkcollege.ca/programs/technology/civil-engineering-technology-transportation-524',
'https://www.mohawkcollege.ca/programs/technology/computer-engineering-technician-583',
'https://www.mohawkcollege.ca/programs/technology/computer-engineering-technician-mechatronic-systems-563',
'https://www.mohawkcollege.ca/programs/technology/computer-engineering-technology-552-0',
'https://www.mohawkcollege.ca/programs/technology/computer-engineering-technology-–-mechatronic-systems-562',
'https://www.mohawkcollege.ca/programs/technology/computer-systems-technician-network-systems-447-455',
'https://www.mohawkcollege.ca/programs/technology/computer-systems-technician-software-support-548-558',
'https://www.mohawkcollege.ca/programs/technology/computer-systems-technology-network-engineering-and-security-analyst-555',
'https://www.mohawkcollege.ca/programs/technology/computer-systems-technology-software-development-559',
'https://www.mohawkcollege.ca/programs/technology/electrical-engineering-technology-582',
'https://www.mohawkcollege.ca/programs/technology/energy-systems-engineering-technology-360',
'https://www.mohawkcollege.ca/programs/technology/environmental-technician-453-463',
'https://www.mohawkcollege.ca/programs/preparatory-studies/general-arts-and-science-college-transfer-230',
'https://www.mohawkcollege.ca/programs/preparatory-studies/general-arts-and-science-university-transfer-208',
'https://www.mohawkcollege.ca/programs/technology/mechanical-engineering-technology-529',
'https://www.mohawkcollege.ca/programs/technology/pre-technology-168',
'https://www.mohawkcollege.ca/programs/technology/quality-engineering-technician-non-destructive-evaluation-nde-439-436',
'https://www.mohawkcollege.ca/programs/graduate-studies/autism-and-behavioural-science-164',
'https://www.mohawkcollege.ca/programs/graduate-studies/brain-disorders-management-470',
'https://www.mohawkcollege.ca/programs/graduate-studies/business-analysis-334',
'https://www.mohawkcollege.ca/programs/graduate-studies/communications-media-practices-266',
'https://www.mohawkcollege.ca/programs/graduate-studies/concurrent-disorders-252',
'https://www.mohawkcollege.ca/programs/communication-arts/creative-arts-business-387',
'https://www.mohawkcollege.ca/programs/community-services/educational-support-intensive-997',
'https://www.mohawkcollege.ca/programs/business/global-business-management-international-only-967',
'https://www.mohawkcollege.ca/programs/business/global-business-management-family-enterprise-international-only-970',
'https://www.mohawkcollege.ca/programs/graduate-studies/human-resources-management-113',
'https://www.mohawkcollege.ca/programs/graduate-studies/international-business-management-116',
'https://www.mohawkcollege.ca/programs/graduate-studies/mental-health-and-disability-management-475',
'https://www.mohawkcollege.ca/programs/graduate-studies/public-relations-166',
'https://www.mohawkcollege.ca/programs/business/supply-chain-management-385',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        item = getItem.get_item(ScrapyschoolCanadaCollegeItem)
        try:
            major_name_en = response.xpath('//h1').extract()[0]
            major_name_en = remove_tags(major_name_en)
            major_name_en = major_name_en.replace('\n','').replace('          ','').replace('        ','')
            #major_name_en =
            major_name_en = re.findall('(.*) - ',major_name_en)[0]
           # print(major_name_en)
        except:
            major_name_en = None
           # print(major_name_en)
#programme_code
        try:
            programme_code = response.xpath('//h1').extract()[0]
            programme_code = remove_tags(programme_code)
            programme_code = re.findall('\d\d\d', programme_code)[0]
            #print(programme_code)
        except:
            programme_code = None
            #print(programme_code)


        try:
            duration = response.xpath('//*[@id="s_program_length"]').extract()[0]
            duration = remove_tags(duration)
            duration_per = '1'
            if 'One year or less' in duration:
                duration = '1'
            elif 'Two years' in duration:
                duration = '2'
            elif 'Three years' in duration:
                duration = '3'

            #print(duration)
        except:
            duration = None
            duration_per = None
            #print(duration)

#1.学校名称
        school_name = 'Mohawk College'


#2.地点
        try:
            location = 'Hamilton, ON'
           # location = remove_tags(location)
           # print(location)
        except:
            location = None
          #  print(location)

#3. 校区
        try:
            campus = 'Fennell Campus (FF)'
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
            department = None

            #print(len(department))
          #  print(department)
            #print(response.url)
        except:
            department = None
           # print(department)

# 4.
        try:
            degree_name = response.xpath('//*[@id="s_accreditation"]').extract()[0]
            degree_name = remove_tags(degree_name)
            degree_name = degree_name.replace('Ontario College ','')
            if 'Graduate Certificate' in degree_name:
                degree_level = '2'
            elif  'Diploma' in degree_name:
                degree_level = '3'
            elif 'Advanced Diploma' in degree_name:
                degree_level = '4'
            elif 'Certificate' in degree_name:
                degree_level = 'No'
            else:
                degree_level = None
           # print(degree_level)
            #print(degree_name)
        except:

            degree_name = None
            #print(degree_name)
#
#5.学位描述
        try:
            degree_overview_en = response.xpath('//h2[contains(text(),"Overview")]/following-sibling::p|//h3[contains(text(),"Program Highlights")]/following-sibling::div').extract()
            degree_overview_en = ''.join(degree_overview_en)
            #degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_overview_en)
            #degree_overview_en = degree_overview_en.replace('\r\n','')
            #degree_overview_en = degree_overview_en.replace('\n','')
            #degree_overview_en = degree_overview_en.replace('\n','')
            #degree_overview_en = degree_overview_en.replace('  ',' ')
            #degree_overview_en = degree_overview_en.replace('					','')
            #degree_overview_en = degree_overview_en.replace('			  	','')
           # print(degree_overview_en)
        except:
            degree_overview_en = None
          #  print(degree_overview_en)

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
            start_date = response.xpath('//h4[contains(text(),"International Students")]/following-sibling::div//div[@class = "program-session--start-dates"]').extract()
            start_date = ','.join(start_date)
            start_date = remove_tags(start_date)
            # start_date = start_date.replace('Spring','').replace('Winter','').replace('Summer','').replace('Fall','')
            # start_date = start_date.replace('September 2019','2019-09').replace('May 2019','2019-05').replace('July 2019','2019-07').replace('January 2020','2020-01').replace('January 2019','2019-01')
            start_date = start_date.replace('Jan 2019','2019-01,').replace('Sep 2019','2019-09,').replace('Sep 2018','2018-09,').replace('May 2019','2019-05,').replace('Aug 2018','2018-08,')
            start_date = start_date.rstrip(',')
            start_date = start_date.replace(',,',',')
            #print(start_date)
        except:
            start_date = None
            #print(start_date)


#10.课程设置
        try:
          modules_en = response.xpath('//*[@id="edit-group-pos"]/div/div/div/p[2]/iframe/@src').extract()[0]
          #   print(url_list)
          #   headers = {
          #       "Connection":"keep-alive",
          #       "Cookie":"_gcl_au=1.1.304662546.1545356846; _ga=GA1.2.1442532783.1545356846; _gid=GA1.2.675782388.1545356846",
          #       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
          #   }
          #   response1 = requests.get(url_list, headers=headers)
          #   print(response1)
          #   modules_en = response1.text
          #   #print(modules_en)
          #   modules_en = ''.join(modules_en)
          #   modules_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',modules_en)
          #   modules_en = modules_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
          # #  print(modules_en)
           # modules_en = None
        except:
            modules_en = None
           # print(modules_en)

#11.就业方向
        try:
            career_en = response.xpath('//h2[contains(text(),"Opportunities")]/following-sibling::*').extract()
            career_en = ''.join(career_en)
            career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',career_en)
            career_en = career_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
        #    print(career_en)
        except:
            career_en = None
            #print(career_en)

#12.截止日期
        try:
            deadline = start_date.replace('-09','-06-15').replace('-01','-11-15').replace('-05','-03-15')
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
        apply_fee = '100'
        try:
            entry_requirements_en = response.xpath('//div[@class = "field field--name-field-admission-requirements field--type-entity-reference field--label-hidden field__items"]').extract()
            entry_requirements_en = ''.join(entry_requirements_en)
            entry_requirements_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]', '', entry_requirements_en)
            #entry_requirements_en = remove_tags(entry_requirements_en)
            #print(entry_requirements_en)
            #print(abc)
        except:
            entry_requirements_en = None
            #print(entry_requirements_en)
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
            other = '课程字段需要ssl证书'
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
        item['duration_per'] = duration_per
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
        item['degree_level'] = degree_level
        if 'No' not  in degree_level:
            yield item
     #   yield item