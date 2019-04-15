import scrapy
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from scrapySchool_Canada_College import getItem
from w3lib.html import remove_tags
import requests
import re
from lxml import etree
import time

class BaiduSpider(scrapy.Spider):
    name = 'Camosun_College_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    # C = [
    #     'http://camosun.ca/learn/calendar/current/web/acct.html',
    #     'http://camosun.ca/learn/subjects/anthropology/',
    #     'http://camosun.ca/learn/calendar/current/web/art.html',
    #     'http://camosun.ca/learn/calendar/current/web/arch.html',
    #     'http://camosun.ca/learn/subjects/asia-pacific/',
    #     'http://camosun.ca/learn/subjects/astronomy/',
    #     'http://camosun.ca/learn/subjects/biology/',
    #     'http://camosun.ca/learn/calendar/current/web/bus.html',
    #     'http://camosun.ca/learn/subjects/chemistry/',
    #     'http://camosun.ca/learn/subjects/communications/',
    #     'http://camosun.ca/learn/calendar/current/web/comp.html',
    #     'http://camosun.ca/learn/subjects/creative-writing/',
    #     'http://camosun.ca/learn/calendar/current/web/crim.html',
    #     'http://camosun.ca/learn/calendar/current/web/dime.html',
    #     'http://camosun.ca/learn/calendar/current/web/econ.html',
    #     'http://camosun.ca/learn/subjects/english/',
    #     'http://camosun.ca/learn/calendar/current/web/envr.html',
    #     'http://camosun.ca/learn/calendar/current/web/fin.html',
    #     'http://camosun.ca/learn/subjects/gender-studies/',
    #     'http://camosun.ca/learn/subjects/geography/',
    #     'http://camosun.ca/learn/subjects/geoscience/',
    #     'http://camosun.ca/learn/calendar/current/web/gbst.html',
    #     'http://camosun.ca/learn/subjects/history/',
    #     'http://camosun.ca/learn/calendar/current/web/hlth.html',
    #     'http://camosun.ca/learn/calendar/current/web/ist.html',
    #     'http://camosun.ca/learn/calendar/current/web/ids.html',
    #     'http://camosun.ca/learn/subjects/japanese/',
    #     'http://camosun.ca/learn/subjects/korean/',
    #     'http://camosun.ca/learn/calendar/current/web/mark.html',
    #     'http://camosun.ca/learn/subjects/mathematics/',
    #     'http://camosun.ca/learn/subjects/music/',
    #     'http://camosun.ca/learn/subjects/philosophy/',
    #     'http://camosun.ca/learn/subjects/physics/',
    #     'http://camosun.ca/learn/subjects/political-science/',
    #     'http://camosun.ca/learn/subjects/psychology/',
    #     'http://camosun.ca/learn/subjects/religion/',
    #     'http://camosun.ca/learn/subjects/social-sciences/',
    #     'http://camosun.ca/learn/subjects/social-work/',
    #     'http://camosun.ca/learn/subjects/sociology/',
    #     'http://camosun.ca/learn/subjects/spanish/',
    #     'http://camosun.ca/learn/programs/economics/',
    #     'http://camosun.ca/learn/programs/english/',
    #     'http://camosun.ca/learn/programs/general-arts/',
    #     'http://camosun.ca/learn/programs/pre-social-work/',
    #     'http://camosun.ca/learn/programs/psychology/',
    #     'http://camosun.ca/learn/programs/biology/',
    #     'http://camosun.ca/learn/programs/general-science/',
    #     'http://camosun.ca/learn/programs/psychology/',
    #     'http://camosun.ca/learn/programs/applied-chemistry-biotechnology/',
    #     'http://camosun.ca/learn/programs/arts-science-studies/',
    #     'http://camosun.ca/learn/programs/criminal-justice/',
    #     'http://camosun.ca/learn/programs/environmental-technology/',
    #     'http://camosun.ca/learn/programs/visual-arts/',
    #     'http://camosun.ca/learn/programs/business-administration/degree/accounting/',
    #     'http://camosun.ca/learn/programs/business-administration/degree/human-resource-management-leadership/',
    #     'http://camosun.ca/learn/programs/business-administration/degree/marketing/',
    #     'http://camosun.ca/learn/programs/business-administration/diploma/accounting/index.html',
    #     'http://camosun.ca/learn/programs/business-administration/diploma/finance/index.html',
    #     'http://camosun.ca/learn/programs/business-administration/diploma/general-management/index.html',
    #     'http://camosun.ca/learn/programs/business-administration/diploma/marketing/',
    #     'http://camosun.ca/learn/programs/business-administration/post-degree-diploma/accounting/',
    #     'http://camosun.ca/learn/programs/business-administration/post-degree-diploma/human-resource-management-leadership/',
    #     'http://camosun.ca/learn/programs/business-administration/post-degree-diploma/marketing/',
    #     'http://camosun.ca/learn/programs/electronics-computer-engineering-technology/',
    #     'http://camosun.ca/learn/programs/information-computer-systems/',
    #     'http://camosun.ca/learn/programs/mechanical-engineering-technology/',
    #     'http://camosun.ca/learn/programs/engineering-bridge/',
    #     'http://camosun.ca/learn/programs/engineering-bridge/',
    #     'http://camosun.ca/learn/programs/engineering-bridge/',
    #     'http://camosun.ca/learn/programs/engineering-bridge/',
    #     'http://camosun.ca/learn/programs/community-family-child-studies/',
    #     'http://camosun.ca/learn/programs/dental-hygiene/',
    #     'http://camosun.ca/learn/programs/early-learning-and-care/',
    #     'http://camosun.ca/learn/programs/practical-nursing/',
    #     'http://camosun.ca/learn/programs/athletic-and-exercise-therapy/',
    #     'http://camosun.ca/learn/programs/exercise-and-wellness/',
    #     'http://camosun.ca/learn/programs/sport-management/',
    #     'http://camosun.ca/learn/programs/exercise-and-wellness/',
    #     'http://camosun.ca/learn/programs/massage-therapy/',
    #     'http://camosun.ca/learn/programs/sport-management/',
    # ]
    C = ['http://camosun.ca/learn/subjects/biology/',
'http://camosun.ca/learn/subjects/astronomy/',
'http://camosun.ca/learn/calendar/current/web/acct.html',
'http://camosun.ca/learn/calendar/current/web/bus.html',
'http://camosun.ca/learn/subjects/anthropology/',
'http://camosun.ca/learn/subjects/asia-pacific/',
'http://camosun.ca/learn/subjects/chemistry/',
'http://camosun.ca/learn/subjects/english/',
'http://camosun.ca/learn/calendar/current/web/econ.html',
'http://camosun.ca/learn/subjects/creative-writing/',
'http://camosun.ca/learn/calendar/current/web/dime.html',
'http://camosun.ca/learn/calendar/current/web/art.html',
'http://camosun.ca/learn/calendar/current/web/crim.html',
'http://camosun.ca/learn/subjects/communications/',
'http://camosun.ca/learn/calendar/current/web/comp.html',
'http://camosun.ca/learn/subjects/history/',
'http://camosun.ca/learn/calendar/current/web/ids.html',
'http://camosun.ca/learn/calendar/current/web/fin.html',
'http://camosun.ca/learn/subjects/geography/',
'http://camosun.ca/learn/calendar/current/web/ist.html',
'http://camosun.ca/learn/calendar/current/web/hlth.html',
'http://camosun.ca/learn/subjects/gender-studies/',
'http://camosun.ca/learn/subjects/geoscience/',
'http://camosun.ca/learn/calendar/current/web/gbst.html',
'http://camosun.ca/learn/subjects/japanese/',
'http://camosun.ca/learn/subjects/music/',
'http://camosun.ca/learn/subjects/physics/',
'http://camosun.ca/learn/calendar/current/web/mark.html',
'http://camosun.ca/learn/subjects/mathematics/',
'http://camosun.ca/learn/calendar/current/web/envr.html',
'http://camosun.ca/learn/subjects/korean/',
'http://camosun.ca/learn/subjects/philosophy/',
'http://camosun.ca/learn/subjects/psychology/',
'http://camosun.ca/learn/subjects/social-work/',
'http://camosun.ca/learn/subjects/social-sciences/',
'http://camosun.ca/learn/subjects/religion/',
'http://camosun.ca/learn/subjects/spanish/',
'http://camosun.ca/learn/subjects/sociology/',
'http://camosun.ca/learn/subjects/political-science/',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        item = getItem.get_item(ScrapyschoolCanadaCollegeItem)
        try:
            major_name_en = response.xpath('//h1').extract()[0]
            major_name_en = remove_tags(major_name_en)
            major_name_en = major_name_en.replace(' &amp;','')
            major_name_en = major_name_en.replace('Post-Degree Diploma in    					    Applied Tourism and   					    Hospitality Management','Applied Tourism and ospitality Management')
           # print(major_name_en)
        except:
            major_name_en = None
           # print(major_name_en)
#programme_code
        try:
            programme_code = None
          #  programme_code = remove_tags(programme_code)
            #programme_code = re.findall('\d\d\d', programme_code)[0]
            #print(programme_code)
        except:
            programme_code = None
            #print(programme_code)


        try:
            duration = response.xpath('//dt[contains(text(),"Length")]/following-sibling::dd[1]').extract()[0]
            duration = remove_tags(duration)
            duration_per = '1'
            if  'Two or four years' in duration:
                duration = '2,4'
            elif '2 ½ to 3 years' in duration:
                duration = '2,3'
            elif  'Two Semesters' in duration:
                duration = '2'
                duration_per = '2'
            elif '8 months' in duration:
                duration = '8'
                duration_per = '3'
            elif '10 months' in duration:
                duration = '10'
                duration_per = '3'
            elif 'Two years' in duration and 'Two' in duration:
                duration = '2'
                duration_per = '1'
            elif 'One or two years' in duration:
                duration = '1,2'
            elif '20 consecutive months' in duration:
                duration = '20'
                duration_per = '3'
            elif 'One year' in duration:
                duration = '1'
                duration_per = '1'
            elif '8-12 months' in duration:
                duration_per = '1'
                duration = '1'
            elif 'Varies' in duration:
                duration = 'No'
            elif 'One, Two, or Four years' in duration:
                duration = '1,2,4'
            elif '16 months' in duration:
                duration = '16'
                duration_per = '3'
            elif 'Two  years' in duration:
                duration = '2'
            elif 'Four years' in duration:
                duration = '4'
            elif 'Two academic years' in duration:
                duration = '2'
            elif '3 years' in duration:
                duration = '3'
            elif 'One  year' in duration:
                duration = '1'

           # print(duration)
        except:
            duration = 'No'
            duration_per = None
           # print(duration)

#1.学校名称
        school_name = 'Camosun College'


#2.地点
        try:
            location = response.xpath('//dt[contains(text(),"Campus")]/following-sibling::dd[1]').extract()
            location = ''.join(location)
            location = location.replace('                  ','').replace('  ','')
            location = remove_tags(location)
           # print(location)
        except:
            location = None
           # print(location)

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
            department = response.xpath('//dt[contains(text(),"School")]/following-sibling::dd[1]').extract()
            department = ''.join(department)
            department = remove_tags(department)
            department = department.replace(' &amp;','')
            #print(department)
          #  print(department)
            #print(response.url)
        except:
            department = None
           # print(department)

# 4.
        try:
            degree_name = response.xpath('//*[@id="page-banner"]/div/div/div/h2').extract()[0]
            degree_name = remove_tags(degree_name)
            if 'Associate' in degree_name:
                degree_level = '4'
            elif 'Advanced Diploma' in degree_name:
                degree_level = '4'
            elif 'Bachelor\'s Degree' in degree_name or 'Bachelor of' in degree_name:
                degree_level = '1'
            elif 'Post-Degree Diploma' in degree_name:
                degree_level = '2'
            elif 'Diploma' in degree_name:
                degree_level = '3'
            else:
                degree_level = 'No'

            if 'in' in degree_name:
                degree_name = re.findall('(.*) in',degree_name)[0]
            #print(degree_level)
            #print(degree_name)
        except:
            degree_level = ''
            degree_name = None
            #print(degree_name)
#
#5.学位描述
        try:
            degree_overview_en = response.xpath('//*[@id="page-introduction"]/div/p').extract()
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
            start_date = response.xpath('//dt[contains(text(),"Start")]/following-sibling::dd[1]').extract()
            start_date = ','.join(start_date)
            start_date = remove_tags(start_date)
            if 'September, January or May' in start_date or 'September,                   January, or May' in start_date or 'September, January, May' in start_date or 'January, May or September' in start_date:
                start_date = '2019-01,2019-05,2019-09'
            elif 'Full-time &amp; Part-time: September  								  Part-time:  							    January' in start_date or 'September or January (Part Time)' in start_date:
                start_date = '2019-09'
            elif 'UVic Bridge: January                UBC Bridge: September ' in start_date:
                start_date = '2019-01,2019-09'
            elif 'January 2020 (every other year)' in start_date:
                start_date = '2020-01'
            elif 'Fall, Winter' in start_date:
                start_date = '2019-01,2019-09'
            elif 'September' in start_date or 'Fall' in start_date:
                start_date = '2019-09'


            #print(start_date)
        except:
            start_date = None
            #print(start_date)


#10.课程设置
        try:
            if 'calendar' in response.url:
                url_list = response.url
            else:
                url_list = re.findall('subjects/(.*)/',response.url)[0]
                url_list = re.findall('(\w\w\w\w).*',url_list)[0]
                url_list = 'http://camosun.ca/learn/calendar/current/web/' + url_list + '.html'
            #print(url_list)
          #   print(url_list)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
            }
            response1 = requests.get(url_list, headers=headers)
            response1 = response1.text
            modules_en =response1
            modules_en = ''.join(modules_en)

          #   modules_en = ''.join(modules_en)
            modules_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',modules_en)
            modules_en = ''.join(modules_en)
            modules_en = modules_en.replace('\r\n','').replace('\n','')
            modules_en = re.findall('</h1>(.*)',modules_en)[0]
            modules_en = re.findall('(.*)Contact Us',modules_en)[0]
            print(modules_en)
            #modules_en = modules_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
          #  print(modules_en)

        except:
            modules_en = None
            print(modules_en)

#11.就业方向
        try:
            career_en = response.xpath('//h3[contains(text(),"opportunities")]/following-sibling::*').extract()
            career_en = ''.join(career_en)
            career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',career_en)
           # career_en = career_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
           # print(career_en)
        except:
            career_en = None
            #print(career_en)

#12.截止日期
        try:
            deadline = start_date.replace('-09','-07-10').replace('-01','-11-10').replace('-05','-03-10')
            #print(start_date)
            #print(deadline)
        except:
            deadline = None
            #print(deadline)
#13.学费
        try:
            if 'calendar' in response.url:
                url_list = response.url
            else:
                url_list = re.findall('subjects/(.*)/',response.url)[0]
                url_list = re.findall('(\w\w\w\w).*',url_list)[0]
                url_list = 'http://camosun.ca/learn/calendar/current/web/' + url_list + '.html'
            print(url_list)
            headers = {
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
              }
            response2 = requests.get(url_list, headers=headers)
            response2 = response2.text
            response2 = etree.HTML(response2)
            tuition_fee = response2.xpath('//*[@id="content"]/div/div/div[2]/text()')[0]

            #print(tuition_fee)
           # print(response.url)
        except:
            tuition_fee = None
            #print(tuition_fee)
#14 申请费:
        apply_fee = '100'
        try:
            url_list = response.url
            url_list = url_list + '/admission-requirements/index.html'
            headers = {
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
              }
            response2 = requests.get(url_list, headers=headers)
            response2 = response2.text
            entry_requirements_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]', '', response2)
            entry_requirements_en = entry_requirements_en.replace('\r\n','').replace('\n','')
            entry_requirements_en = re.findall('<h2>Admission Requirements</h2>(.*)',entry_requirements_en)[0]
            print(entry_requirements_en)
            #print(abc)

        except:
            entry_requirements_en = None
            #print(entry_requirements_en)
#16 中国学生申请要求
        try:
            require_chinese_en = '<div>  								<h2>Step 1 - Find a program</h2>  								<p>From academic upgrading to business administration degrees and health care technical training, Camosun offers something for everyone. <a>Browse our program list</a>.</p>                  				<h3>English proficiency levels</h3>                  <p>Admission to most academic programs is based on meeting <strong>one of the following</strong> English proficiency levels:</p>  								<ul>  									<li>Completion of BC English 12 with a <strong>C+</strong> or better</li>  									<li>Academic IELTS</li>  									<li>TOEFL iBT</li>  									<li><a>Camosun English assessment</a></li>  								</ul>  								<p>You can also apply for <a>English upgrading</a> in order to meet your English proficiency for program admission.</p>                  <p><strong>Note: </strong>Academic IELTS and TOEFL iBT scores must be from  within the past two years. For TOEFL we require an original document from <a>ETS</a> to  Camosun College: Destination (DI) Code: 7527</p>                  <p>IELTS or TOEFL requirements for <strong>undergraduate</strong> programs:</p>                  <ul>                    <li><strong>Academic IELTS score of 6.0</strong> with no individual band less than 5.5</li>                    <li><strong>TOEFL iBT score of 83</strong> with no score less than 20 on each level </li>                  </ul>                  <p>IELTS or TOEFL requirements for <strong>post-graduate</strong> programs:</p>                  <ul>                    <li><strong>Academic IELTS score of 6.5</strong> with no individual band less than 6.0</li>                    <li><strong>TOEFL iBT score of 88</strong> with no score less than 20 on each level</li>                  </ul>  								<p><span>Note</span> Applicants from countries where <strong>Study Direct Stream (SDS)</strong> or <strong>Canada Express Study (CES)</strong> are available must meet corresponding SDS/CES criteria in addition to Camosun admission requirements.</p>                  <p>Please see our <a>important dates calendar</a> for start dates and tuition deadlines.</p>  								<div>  									<h3>Consider Camosun Homestay</h3>  									<p>Experience Victoria with a Camosun  Homestay family. You must apply at least six weeks before the start of your program. <a>Learn more</a> about the Camosun Homestay program.</p>  								</div>  							</div>'
            #require_chinese_en = remove_tags(require_chinese_en)
            # print(require_chinese_en)
        except:
            require_chinese_en = None
            # print(require_chinese_en)

#17 特殊专业要求
        try:
            specific_requirement_en = entry_requirements_en
           # specific_requirement_en = specific_requirement_en.replace('\n','')
           # specific_requirement_en = re.findall('(.*)Note:',specific_requirement_en)
              # #specific_requirement_en = remove_tags(specific_requirement_en)
            #specific_requirement_en = ''.join(specific_requirement_en)
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
        ielts_desc = 'Academic IELTS score of 6.0 with no individual band less than 5.5/Academic IELTS score of 6.5 with no individual band less than 6.0'
#26 ielts
        try:
            if degree_level == 2:
                ielts = '6.5'
                ielts_l = '6.0'
                toefl = '88'
            else:
                ielts_l = '5.5'
                ielts = '6.0'
                toefl = '83'
        except:
            ielts_l = None
            ielts = None
            toefl = None

#27 ielts_?

        ielts_s = ielts_l
        ielts_r = ielts_l
        ielts_w = ielts_l
        toefl_l = '20'
        toefl_s = '20'
        toefl_w = '20'
        toefl_r = '20'

        #print(ielts_l)

#28 toefl_code
        try:
            toefl_code = '7527'
            #toefl_code = remove_tags(toefl_code)
            # print(toefl_code)
        except:
            toefl_code = None
            # print(toefl_code)

#29 toefl_desc
        try:
            toefl_desc = 'TOEFL iBT score of 83 with no score less than 20 on each level/TOEFL iBT score of 88 with no score less than 20 on each level'
            #toefl_desc = remove_tags(toefl_desc)
            # print(toefl_desc)
        except:
            toefl_desc = None
            # print(toefl_desc)








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
            other = '没有课程代码,跳转3次页面跑的特别慢'
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

        #yield item
           # pass
        #yield item