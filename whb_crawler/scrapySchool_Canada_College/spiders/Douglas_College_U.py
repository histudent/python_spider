import scrapy
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from scrapySchool_Canada_College import getItem
from w3lib.html import remove_tags
import requests
import re
import time

class BaiduSpider(scrapy.Spider):
    name = 'Douglas_College_C'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['https://www.douglascollege.ca/programs-courses/catalogue/programs/AAANTH',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/ASARTS',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/AACMNS',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/ASARTC',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/AACRIM',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/AAECON',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/AAENGL',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/ASARTE',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/ASARTF',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/AAFPP',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/ASARTW',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/ASGEOG',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/AAHIST',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/ASARTI',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/AAMODL',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/AAMUSC',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/AAPEFA',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/AAPHIL',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/AAPOLI',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/AAPSYC',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/AASOCI',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/AATHEA',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/ASSCIE',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/ASBIOL',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/ASCHEM',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/ASGEOL',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/CTEGFND',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/ASENSC',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/ASMATH',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/PDACCT',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/PDACCS',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/PDFIPL',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/PDFIAN',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/PDFIPL',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/PDGBE',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/PDHOSP',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/PDHOMK',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/PDICT',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/PDIBM',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/PDMARK',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/PDPCOM',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/PDPMGT',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/PDSALE',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/PDSCMGT',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/PBACCT',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/PBACCF',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/PBDCIS',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/PBFINC',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/PDHIM',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/PBHSMT',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/PBDISCM',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/BBAA',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/BBAFA',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/BBAMGMT',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/BAAPSYC',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/BAACRIM',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/BACYCC',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/BPA',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPACCT',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPCOMM',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPCSTI',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPCRIM',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPDOPT',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/DPEGESS',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPFSMT',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPFMTS',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/DPMGTG',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPGENS',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPGEOR',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPHEAR',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPHOSP',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPLEGAL',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPLART',
'https://www.douglascollege.ca/programs-courses/catalogue/programs/DPMGTB',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPMARK',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPMUSC',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPMTCH',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPSCIE',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPSTGE',
'http://www.douglascollege.ca/programs-courses/catalogue/programs/DPTHEA',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        item = getItem.get_item(ScrapyschoolCanadaCollegeItem)

        try:
            major_name_en = response.xpath('//h1').extract()[0]
            major_name_en = remove_tags(major_name_en)
            if '(' in major_name_en:
                major_name_en = re.findall('(.* )\(.*\)',major_name_en)[0]
            else:
                pass
            #major_name_en = major_name_en.replace('\r\n','').replace('					','').replace('				','')
           # print(major_name_en)
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
            duration = response.xpath('//span[contains(text(),"Length")]/following-sibling::span').extract()[0]
            duration = remove_tags(duration)
            duration_per = '2'
            if 'Eight semesters' in duration:
                duration = '8'
            elif 'Four semesters' in duration:
                duration = '4'
            elif 'Three semesters' in duration:
                duration = '3'
            elif 'One year' in duration:
                duration = '1'
                duration_per = '1'
            elif 'Two semesters' in duration:
                duration = '2'
            elif 'Two years' in duration:
                duration = '2'
                duration_per = '1'
            elif 'One semester' in duration:
                duration = '1'
            elif 'Six semesters' in duration:
                duration = '6'
            elif 'Five semesters' in duration:
                duration = '5'
            elif 'Self-paced' in duration:
                duration = 'No'
            else:
                duration_per = '1'

            #print(duration)
        except:
            duration = None
            duration_per = None
            #print(duration)

#1.学校名称
        school_name = 'Douglas College'


#2.地点
        try:
            location = response.xpath('//span[contains(text(),"Campu")]/following-sibling::span').extract()[0]
            location = remove_tags(location)
           # print(location)
        except:
            location = None
          #  print(location)

#3. 校区
        try:
            campus = location
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
            department = response.xpath('//span[contains(text(),"Faculty:")]/following-sibling::span').extract()[0]
            department = remove_tags(department,keep=("i"))
            department = department.replace('&amp;','')
            #print(len(department))
          #  print(department)
            #print(response.url)
        except:
            department = None
           # print(department)

# 4.
        try:
            degree_name = response.xpath('//span[contains(text(),"Credential:")]/following-sibling::span').extract()[0]
            #degree_name_list = remove_tags(degree_name_list,keep=('li','ul'))
            #degree_name_list = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_name_list)
            #degree_name_list = degree_name_list.replace('\t','').replace('\n','').replace('\xa0','').replace(' class="list-inline uofs-cta-list','')
            # degree_name_list = degree_name_list.replace('<li>','').replace('</li>','---')
            # degree_name_list = degree_name_list.replace('<span>','').replace('</span>','---')
           # degree_name_list = degree_name_list.split('</li><li>')
            degree_name = remove_tags(degree_name)
            if 'Bachelor\'s Degree' in degree_name:
                degree_level = '1'
            elif 'Associate Degree' in degree_name:
                degree_level = '4'
            elif 'Advanced Certificate' in degree_name:
                degree_level = '4'
            elif 'Post-Degree Diploma' in degree_name or 'Post-Baccalaureate Diploma' in degree_name or 'Graduate Diploma' in degree_name:
                degree_level = '2'
            elif 'Diploma' in degree_name:
                degree_level = '3'

            else:
                degree_level = None
            #print(degree_name)
            #print(response.url)
        except:

            degree_name = None
           # print(degree_name)
#
#5.学位描述
        try:
            degree_overview_en = response.xpath('//*[@id="overview"]/div').extract()
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
            start_date = response.xpath('//span[contains(text(),"Offered:")]/following-sibling::span').extract()[0]
            #start_date = ','.join(start_date)
            start_date = remove_tags(start_date)
            # start_date = start_date.replace('Spring','').replace('Winter','').replace('Summer','').replace('Fall','')
            # start_date = start_date.replace('September 2019','2019-09').replace('May 2019','2019-05').replace('July 2019','2019-07').replace('January 2020','2020-01').replace('January 2019','2019-01')
            start_date = start_date.replace('Winter','2019-01').replace('Spring','2019-01').replace('Summer','2019-05').replace('Fall','2019-09')
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
            modules_en = response.xpath('//span[contains(text(),"curriculum framework")]/following-sibling::div').extract()
            modules_en = ''.join(modules_en)
            modules_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',modules_en)
            modules_en = modules_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
            #print(modules_en)
        except:
            modules_en = None
            #print(modules_en)

#11.就业方向
        try:
            career_en = response.xpath('//span[contains(text(),"career transfer pathways")]/following-sibling::div').extract()[0]
            career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',career_en)
            career_en = career_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
           # print(career_en)
        except:
            career_en = None
          #  print(career_en)

#12.截止日期
        try:
            if '2019-01' in start_date and '2019-05' in start_date and '2019-09' in start_date:
                deadline = '2019-05-31,2018-09-30,2019-01-30'
            elif '2019-01' in start_date and '2019-05' in start_date:
                deadline = '2018-09-30,2019-01-30'
            elif '2019-05' in start_date and '2019-09' in start_date:
                deadline = '2019-01-30,2019-05-31'
            elif '2019-01' in start_date and '2019-09' in start_date:
                deadline = '2018-09-30,2019-05-31'
            elif '2019-01' in start_date:
                deadline = '2018-09-30'
            elif '2019-05' in start_date:
                deadline = '2019-01-30'
            elif '2019-09' in start_date:
                deadline = '2019-05-31'
            else:
                deadline = None
            #print(deadline)
        except:
            deadline = None
            #print(deadline)
#13.学费
        try:
            tuition_fee = '692.56'
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = tuition_fee.replace('$','')
            #print(tuition_fee)
        except:
            tuition_fee = None
            #print(tuition_fee)
#14 申请费:
        apply_fee = '90'
        try:

            entry_requirements_en = '<ul><li>Undergraduate (diploma and associate degree) programs:<ul><li>High school graduation OR minimum 17 years of age by the end of the first month of studies in the semester of entry to Douglas College; and</li><li>Minimum overall grade average of 60% (or equivalent) in the final year of high school; and</li><li>Minimum final grade of “C” or 60% (or equivalent) in Grade 11 Mathematics or equivalent for most programs</li></ul></li></ul><ul><li>Post-Graduate (Post-Degree and Post-Baccalaureate) programs:<br><ul><li>Graduation from a recognized degree granting post-secondary institution with a minimum 3-year bachelor degree; and</li><li>Minimum cumulative grade point average of 60% (or equivalent) during the bachelor degree program</li></ul></li></ul>'
            #entry_requirements_en = remove_tags(entry_requirements_en)
            #print(entry_requirements_en)
            #print(abc)
        except:
            entry_requirements_en = None

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
        try:
            ielts_desc = 'English Requirements for ELLA placement You must submit proof of ONE of the following: TOEFL - minimum score 45 IBT ((Douglas College only accepts an official TOEFL score. Douglas College\'s institutional code is 9568).  IELTS – minimum score 4.5, no band below 4.5'
            #ielts_desc = remove_tags(ielts_desc)
            # print(ielts_desc)
        except:
            ielts_desc = None
            # print(ielts_desc)

#26 ielts
        try:
            ielts = '4.5'
            #ielts = re.findall('\d\.\d',ielts)
            #ielts = remove_tags(ielts)
            #print(ielts)
        except:
            ielts = None
            #print(ielts)
#27 ielts_?

        ielts_l = 4.5
        ielts_s = 4.5
        ielts_r = 4.5
        ielts_w = 4.5

#28 toefl_code
        try:
            toefl_code = '9568'
            #toefl_code = remove_tags(toefl_code)
            # print(toefl_code)
        except:
            toefl_code = None
            # print(toefl_code)

#29 toefl_desc
        try:
            toefl_desc = 'English Requirements for ELLA placement You must submit proof of ONE of the following: TOEFL - minimum score 45 IBT ((Douglas College only accepts an official TOEFL score. Douglas College\'s institutional code is 9568).  IELTS – minimum score 4.5, no band below 4.5'
            #toefl_desc = remove_tags(toefl_desc)
            # print(toefl_desc)
        except:
            toefl_desc = None
            # print(toefl_desc)

#30 toefl
        try:
            toefl = '45'
            #toefl = re.findall('\d\d',toefl)
            #toefl = remove_tags(toefl)
            #print(toefl)
        except:
            toefl = None
           # print(toefl)

#31 toefl_?
        toefl_l = None
        toefl_s = None
        toefl_r = None
        toefl_w = None




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
            # print(portfolio_desc_en)
        except:
            portfolio_desc_en = None
            # print(portfolio_desc_en)

#37 other
        try:
            other = 'IB:Minimum grade of 3 or C  ap:Minimum grade of 3 or C '
            #other = remove_tags(other)
            # print(other)
        except:
            other = None
            # print(other)

#平均分  average_score
        average_score = '60'

# degree_name_desc
        try:
            degree_name_desc = overview_en
        except:
            degree_name_desc = None


        ap = 'Minimum grade of 3 or C '

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
#
#

        yield item

     #   yield item