import scrapy
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from scrapySchool_Canada_Ben import getItem
from w3lib.html import remove_tags
import requests
import re
import time

class BaiduSpider(scrapy.Spider):
    name = 'Vancouver_Islands_University_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['https://www.viu.ca/programs/art-design-performing-arts/bachelor-design-graphic-design',
'https://www.viu.ca/programs/art-design-performing-arts/bachelor-interior-design',
'https://www.viu.ca/programs/art-design-performing-arts/bachelor-music-jazz-studies',
'https://www.viu.ca/programs/art-design-performing-arts/theatre-0',
'https://www.viu.ca/programs/art-design-performing-arts/visual-art',
'https://www.viu.ca/programs/arts-humanities-social-sciences/anthropology',
'https://www.viu.ca/programs/arts-humanities-social-sciences/biology',
'https://www.viu.ca/programs/arts-humanities-social-sciences/ba-chemistry',
'https://www.viu.ca/programs/arts-humanities-social-sciences/ba-computing-science',
'https://www.viu.ca/programs/arts-humanities-social-sciences/ba-english',
'https://www.viu.ca/programs/arts-humanities-social-sciences/ba-geography',
'https://www.viu.ca/programs/arts-humanities-social-sciences/ba-mathematics',
'https://www.viu.ca/programs/arts-humanities-social-sciences/ba-psychology',
'https://www.viu.ca/programs/arts-humanities-social-sciences/bachelor-arts-honours-majors-and-minors',
'https://www.viu.ca/programs/arts-humanities-social-sciences/business',
'https://www.viu.ca/programs/arts-humanities-social-sciences/creative-writing-and-journalism',
'https://www.viu.ca/programs/arts-humanities-social-sciences/criminology',
'https://www.viu.ca/programs/arts-humanities-social-sciences/digital-media',
'https://www.viu.ca/programs/arts-humanities-social-sciences/digital-media-studies',
'https://www.viu.ca/programs/arts-humanities-social-sciences/earth-science',
'https://www.viu.ca/programs/arts-humanities-social-sciences/economics',
'https://www.viu.ca/programs/arts-humanities-social-sciences/global-studies',
'https://www.viu.ca/programs/arts-humanities-social-sciences/history',
'https://www.viu.ca/programs/arts-humanities-social-sciences/liberal-studies',
'https://www.viu.ca/programs/arts-humanities-social-sciences/media-studies',
'https://www.viu.ca/programs/arts-humanities-social-sciences/philosophy',
'https://www.viu.ca/programs/education/physical-education',
'https://www.viu.ca/programs/arts-humanities-social-sciences/political-studies',
'https://www.viu.ca/programs/arts-humanities-social-sciences/sociology',
'https://www.viu.ca/programs/arts-humanities-social-sciences/studies-women-and-gender',
'https://www.viu.ca/programs/art-design-performing-arts/theatre-0',
'https://www.viu.ca/programs/art-design-performing-arts/visual-art',
'https://www.viu.ca/programs/business-management/bachelor-business-administration',
'https://www.viu.ca/programs/education/bachelor-education',
'https://www.viu.ca/programs/education/physical-education',
'https://www.viu.ca/programs/health/bachelor-science-nursing',
'https://www.viu.ca/programs/human-services/bachelor-arts-child-and-youth-care',
'https://www.viu.ca/programs/human-services/bachelor-social-work',
'https://www.viu.ca/programs/science-and-technology/bachelor-natural-resource-protection',
'https://www.viu.ca/programs/science-and-technology/bachelor-science-majors-minors-and-transfer',
'https://www.viu.ca/programs/science-and-technology/bachelor-science-fisheries-and-aquaculture',
'https://www.viu.ca/programs/science-and-technology/biology',
'https://www.viu.ca/programs/science-and-technology/bsc-chemistry',
'https://www.viu.ca/programs/science-and-technology/bsc-computing-science',
'https://www.viu.ca/programs/science-and-technology/bsc-earth-science',
'https://www.viu.ca/programs/science-and-technology/bsc-psychology',
'https://www.viu.ca/programs/science-and-technology/geography',
'https://www.viu.ca/programs/science-and-technology/geoscience',
'https://www.viu.ca/programs/science-and-technology/mathematics',
'https://www.viu.ca/programs/tourism-recreation-hospitality/bachelor-hospitality-management',
'https://www.viu.ca/programs/tourism-recreation-hospitality/bachelor-tourism-management',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        item = getItem.get_item(ScrapyschoolCanadaBenItem)



#1.学校名称
        school_name = 'Vancouver Islands University'

#2.地点
        try:
            location = response.xpath('//*[contains(text(),"Location Offered")]/following-sibling::span').extract()[0]
            location = remove_tags(location)
            #print(location)
        except:
            location = None
            #print(location)

#3. 校区
        try:
            campus = location
            #campus_list = remove_tags(campus_list)
            #campus_list = campus_list.replace(', Online','')
            #campus_list = campus_list.replace(' ','')
            #campus_list = campus_list.split(',')
            #print(campus_list)
        except:
            campus_list = None
            #print(campus_list)

#4. 学院
        try:
            department = response.xpath('//*[@id="tabbed-content"]/div[5]').extract()[0]
            #department = remove_tags(department,keep=("i"))
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
            degree_name1 = response.xpath('//*[@id="page-title"]').extract()[0]
            degree_name2 = response.xpath('//h2[@id][1]').extract()[0]
            degree_name1 = remove_tags(degree_name1)
            degree_name2 = remove_tags(degree_name2)

           # degree_name = remove_tags(degree_name,keep=('li','ul'))
            #degree_name_list = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_name_list)
           # degree_name = degree_name.replace('\t','').replace('\n','').replace('\xa0','').replace(' class="list-inline uofs-cta-list','')
            # degree_name_list = degree_name_list.replace('<li>','').replace('</li>','---')
            # degree_name_list = degree_name_list.replace('<span>','').replace('</span>','---')
            #degree_name_list = degree_name_list.split('</li><li>')
            #print("1:" + degree_name2)
            #print("2:" + degree_name1)
            if 'Bachelor of Education' in degree_name1 or 'Bachelor of Education' in degree_name2:
                degree_name = 'Bachelor of Education'
            elif 'BSc' in degree_name2 or 'BSc' in degree_name1:
                degree_name = 'Bachelor of Science'
            elif 'BA' in degree_name1 or 'BA' in degree_name2:
                degree_name = 'Bachelor of Arts'
            elif 'Bachelor of Hospitality Management' in degree_name1 or 'Bachelor of Hospitality Management' in degree_name2:
                degree_name = 'Bachelor of Hospitality Management'
            elif 'Bachelor of Tourism Management' in degree_name1 or 'Bachelor of Tourism Management' in degree_name2:
                degree_name = 'Bachelor of Tourism Management'
            elif 'Minor' in degree_name1 or 'Minor' in degree_name2:
                degree_name = 'Minor Pass'
            elif 'Bachelor of Science' in degree_name1 or 'Bachelor of Science' in degree_name2:
                degree_name = 'Bachelor of Science'
            elif 'Geoscience' in degree_name1 or 'Geoscience' in degree_name2:
                degree_name = 'Bachelor of Science'
            elif 'Bachelor of Arts' in degree_name1 or 'Bachelor of Arts' in degree_name2:
                degree_name = 'Bachelor of Arts'
            elif 'Bachelor of Natural Resource Protection' in degree_name1 or 'Bachelor of Natural Resource Protection' in degree_name2:
                degree_name = 'Bachelor of Natural Resource Protection'
            elif 'Bachelor of Social Work' in degree_name1 or 'Bachelor of Social Work' in degree_name2:
                degree_name = 'Bachelor of Social Work'
            elif 'Education' in degree_name1 or 'Education' in degree_name2:
                degree_name = 'Bachelor of Education'
            elif 'BBA' in degree_name1 or 'BBA' in degree_name2:
                degree_name = 'Bachelor of Business Administration'
            elif 'Studies in Women and Gender' in degree_name1 or 'Studies in Women and Gender' in degree_name2:
                degree_name = 'Bachelor of Arts'
            elif 'Bachelor of Anthropology' in degree_name1 or 'Bachelor of Anthropology' in degree_name2:
                degree_name = 'Bachelor of Anthropology'
            elif 'Political Studies' in degree_name1 or 'Political Studies' in degree_name2:
                degree_name = 'Bachelor of Arts'
            elif 'Visual Art' in degree_name1 or 'Visual Art' in degree_name2:
                degree_name = 'Bachelor of Art'
            elif 'Philosophy' in degree_name1 or 'Philosophy' in degree_name2:
                degree_name ='Bachelor of Arts'
            elif 'Sociology' in degree_name1 or 'Sociology' in degree_name2:
                degree_name = 'Bachelor of Arts'
            elif 'Liberal' in degree_name1 or 'Liberal' in degree_name2:
                degree_name = 'Bachelor of Arts'
            elif 'Physical' in degree_name1 or 'Physical' in degree_name2:
                degree_name = 'Bachelor of Education'
            elif 'Media Studies' in degree_name1 or 'Media Studies' in degree_name2:
                degree_name = 'Bachelor of Arts'
            elif 'Economics' in degree_name1 or 'Economics' in degree_name2:
                degree_name = 'Bachelor of Arts'
            elif 'Global' in degree_name1 or 'Global' in degree_name2:
                degree_name = 'Bachelor of Arts'
            elif 'History' in degree_name1 or 'History' in degree_name2:
                degree_name = 'Bachelor of Arts'
            elif 'Business' in degree_name1 or 'Business' in degree_name2:
                degree_name = 'Bachelor of Arts'
            elif 'Bachelor of Music' in degree_name1 or 'Bachelor of Music' in degree_name2:
                degree_name ='Bachelor of Music'
            elif 'Earth Science' in degree_name1 or 'Earth Science' in degree_name2:
                degree_name = 'Bachelor of Arts'
            elif 'Digital Media Studies' in degree_name1 or 'Digital Media Studies' in degree_name2:
                degree_name = 'Digital Media Studies'
            elif 'Creative Writing' in degree_name1 or 'Creative Writing' in degree_name2:
                degree_name = 'Bachelor of Arts'
            elif 'Bachelor of Interior Design' in degree_name1 or 'Bachelor of Interior Design' in degree_name2:
                degree_name = 'Bachelor of Interior Design'
            elif 'Bachelor of Design' in degree_name1 or 'Bachelor of Design' in degree_name2:
                degree_name = 'Bachelor of Design'
            elif 'https://www.viu.ca/programs/arts-humanities-social-sciences' in response.url:
                degree_name = 'Bachelor of Arts'
            else:
                degree_name = None
            #print(degree_name)
            #print(response.url)
        except:

            degree_name = None
            #print(degree_name)

        try:
            duration = response.xpath('//*[contains(text(),"Program Length")]/following-sibling::span').extract()[0]
            duration = remove_tags(duration)
            duration = duration.replace(' Years','').replace('\n','')
            #print(duration)
        except:
            duration = None
            #print(duration)
#5.学位描述
        try:
            degree_overview_en = response.xpath('//h2[contains(text(),"Program")]/following-sibling::div/span').extract()
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
           # start_date = response.xpath('//*[@id="Admissionrequirementsanddeadlines-subsection-0"]/table/tbody/tr/td[1]').extract()
            start_date = '2019-09'
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
            modules_en = response.xpath('//*[@id="program-outline"]/div[1]/span').extract()[0]
            modules_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',modules_en)
            modules_en = modules_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
            #print(modules_en)
        except:
            modules_en = None
            #print(modules_en)

#11.就业方向
        try:
            career_en = response.xpath('//a[contains(text(),"Career Opportunities")]/../../following-sibling::div').extract()[0]
            career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',career_en)
            career_en = career_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
            #print(career_en)
        except:
            career_en = None
            #print(career_en)

#12.截止日期
        try:
            deadline = '2019-03-31'
            #deadline = response.xpath('//*[@id="Admissionrequirementsanddeadlines-subsection-0"]/table/tbody/tr/td[3]').extract()
            #deadline = '---'.join(deadline)
            #deadline = remove_tags(deadline)
            #deadline = deadline.replace('Documents due: ', '')
            #deadline =  deadline.replace('Sep 1, 2018Oct 1, 2018','2018-09-01').replace('Feb 1, 2019Mar 1, 2019','2019-02-01').replace('Mar 1, 2019Apr 1, 2019','2019-03-01').replace('May 1, 2019Jun 1, 2019','2019-05-01').replace('Sep 1, 2019Oct 1, 2019','2019-09-01').replace('Feb 15, 2019Mar 1, 2019','2019-02-15').replace('---',',')
            #deadline = remove_tags(deadline)
            #print(deadline)
        except:
            deadline = None
            #print(deadline)
#13.学费
        try:
            #tuition_fee = response.xpath('//*').extract()[0]
            #tuition_fee = re.findall('\d\d,\d\d\d\.\d\d',tuition_fee)[0]\
            tuition_fee = '15,240.00'
            #tuition_fee = remove_tags(tuition_fee)
            #tuition_fee = tuition_fee.replace('$','')
            #print(tuition_fee)
        except:
            tuition_fee = None
            #print(tuition_fee)
#14 申请费:
        apply_fee = '150'

#15 申请要求
        try:
            entry_requirements_en = response.xpath('//a[contains(text(),"Admission Requirements")]/../../following-sibling::div').extract()[0]
            entry_requirements_en = remove_tags(entry_requirements_en)
          #  print(entry_requirements_en)
        except:
            entry_requirements_en = None
         #   print(entry_requirements_en)
            #print(abc)

#16 中国学生申请要求
        try:
            require_chinese_en = '<div><h2><a></a>Admission</h2><p>Vancouver Island University accepts international students under <em>one</em> of the following conditions:</p><ul><li>direct applications (online or paper applications);</li><li>applications through authorized representatives;</li><li>institution-to-institution exchange programs;</li><li>sponsorship through inter-governmental agreements;</li><li>winner of academic competitions or international scholarships.</li></ul><h2>Admission to English Language Studies in the English Language Centre</h2><p>All students must:</p><ul><li>be an international visitor or hold a&nbsp;<a>study permit</a>;</li><li>complete a <a>Vancouver Island University ESL language assessment test (or equivalent)</a></li></ul><p>Please keep in mind that students applying for conditional admission to an undergraduate (or diploma, certificate or trades) program at VIU, or thinking of applying upon completion of ESL programming, will still be required to provide proof of high school graduation and their secondary school transcripts.</p><h2>The High School</h2><p>All students must:</p><ul><li>have completed Grade 9, or equivalent;</li><li>turn 15 years of age by December 31 following a September enrollment;</li><li>be under 19 years of age.</li></ul><p>Admission is selective and is based on academic and leadership potential. For more info please visit <a>The High School at VIU</a>.</p><h2>Undergraduate Academic and Vocational Programs</h2><ul><li>Graduation from high school or equivalent.</li><li>Proof of English language proficiency is required from applicants for whom English is not their first language or from those whose education was completed in any country where English is not the official language.</li><li>For students who meet the academic requirements but not the English language requirement, conditional acceptance to VIU may be granted. In this case, admission is granted pending completion of <a>VIU’s English Language Centre program</a> (level AP5). Exceptions may apply.</li><li>Up to 30 advanced credits may be granted for <a>Advanced Placement</a> and <a>International Baccalaureate</a> (higher level) courses.</li><li>Academic programs may have additional program admission requirements and course prerequisites. Please check your specific program requirements from&nbsp;<a>VIU programs</a>.</li><li>International students who are BC high school graduates must have a minimum grade of “C” in English 12 for direct entry into an academic program.</li></ul><h2><a></a>English Language Requirements for Academic Programs</h2><p>To meet the English language requirements for academic programs, students must have completed one of the following:</p><table><tbody><tr><td><h4><strong>Test</strong></h4></td><td><h4><strong>Minimum score</strong></h4></td></tr><tr><td><ul><li><h5>TOEFL Paper Based Test</h5></li></ul></td><td><h5><strong>550 </strong>(no section below 56)</h5></td></tr><tr><td><ul><li><h5>TOEFL IBT</h5></li></ul></td><td><h5><strong>88 </strong>(no section below 20)</h5></td></tr><tr><td><ul><li><h5>IELTS (Academic)</h5></li></ul></td><td><h5><strong>6.5 </strong>(no band below 6.0)</h5></td></tr><tr><td><ul><li><h5>CAEL</h5></li></ul></td><td><h5><strong>60</strong></h5></td></tr><tr><td><ul><li><h5>Cambridge Certificate of Proficiency in English (CPE)</h5></li></ul></td><td><h5><strong>176</strong> overall</h5></td></tr><tr><td><ul><li><h5>Cambridge Certificate of Advanced English (CAE)</h5></li></ul></td><td><h5><strong>176</strong> overall</h5></td></tr><tr><td><ul><li><h5>English 12 (BC)</h5></li></ul></td><td><h5>Min. “<strong>C</strong>”</h5></td></tr><tr><td><ul><li><h5>Pearson (PTE)</h5></li></ul></td><td><h5><strong>60 </strong>(no section below 60)</h5></td></tr><tr><td><ul><li><h5>International Baccalaureate English A1/A2</h5></li></ul></td><td><h5>Higher Level (HL)/ Standard Level (SL) grade <strong>3</strong> or higher</h5></td></tr><tr><td><ul><li><h5>VIU English Language Centre</h5></li></ul></td><td><h5>Successful completion of University Preparation <strong>Level 5</strong></h5></td></tr><tr><td><ul><li><h5>Advanced Placement (AP) English Language and Composition or English Literature and Composition</h5></li></ul></td><td><h5>Grade<strong> 2</strong> or higher</h5></td></tr><tr><td><ul><li><h5>Recognized university where English is the language of instruction.</h5></li></ul></td><td><h5>Completion of six credits of post-secondary English composition and literature with a minimum grade of “<strong>C</strong>”</h5></td></tr><tr><td><ul><li><h5>Language Proficiency Index (LPI)</h5></li></ul></td><td><h5>Score<strong> 5</strong> or higher</h5></td></tr><tr><td><ul><li><h5>General Certificate of Secondary Education (GCSE)</h5></li></ul></td><td><h5>English at the O-level with a minimum grade of <strong>C or 4</strong></h5></td></tr></tbody></table><h2>Admission to Post-Degree Diploma in Business Studies</h2><ul><li>Business or non-business Bachelor\'s degree from a recognized institution.</li><li>Meet VIU’s <a>English language requirements for academic programs</a>. Individual course pre-requisites also apply.</li></ul><h2><a></a>Admission to Graduate Programs</h2><ul><li>Minimum “B” average in the final 2 years of a Bachelor’s degree.</li><li>Meet <strong>one</strong> of the following VIU English language requirements:</li></ul><table><tbody><tr><td><h3><strong>Test</strong></h3></td><td><h3><strong>Minimum score</strong></h3></td></tr><tr><td><h5>TOEFL iBT</h5></td><td><h5><strong>93 </strong>(no band below 20)</h5></td></tr><tr><td><h5>IELTS</h5></td><td><h5><strong>7.0 </strong>(no band below 6.5)</h5></td></tr><tr><td><h5><spanHelvetica Neue\', Helvetica, Arial, sans-serif; font-size: 13px;">VIU\'s&nbsp;</span><aHelvetica Neue\', Helvetica, Arial, sans-serif; font-size: 13px;">English Language Centre</a><spanHelvetica Neue\', Helvetica, Arial, sans-serif; font-size: 13px;">&nbsp;</span></h5></td><td><h5>Successful completion of&nbsp;<span>Graduate Preparation Program (Grad Prep)</span></h5></td></tr><tr><td><h5>CAEL</h5></td><td><h5><strong>70 (no band below 60)</strong></h5></td></tr><tr><td><h5>Pearson (PTE)</h5></td><td><h5><strong>65 </strong>(no section below 60)</h5></td></tr><tr><td><h5>Cambridge Certificate of Proficiency in English (CPE)</h5></td><td><h5><strong>185 overall</strong></h5></td></tr><tr><td><h5>Cambridge Certificate of Advanced English (CAE)</h5></td><td><h5><strong>185 overall</strong></h5></td></tr></tbody></table><p>&nbsp;</p><ul><li>No GMAT or GRE scores required</li><li>For other documents and work experience requirements, please see program specific page.</li></ul><h2>Transfer Credit</h2><p>Students enrolled in a University program may receive transfer credit for up to 50 percent of their program. Students seeking credit for courses from other institutions will need to submit detailed course outlines and a credit transfer request form. Please note, it can take 6-8 weeks after admissions received your documents for credit to appear. Students are welcome to find transfer credit resources by looking up <a>individual courses</a> or searching the BC Council on Admission and Transfer (BCCAT).</p><h2><a></a>Deferring Admission</h2><p><strong>For students wanting to change their program to a later start date:</strong></p><p>If for any reason you need to change when you start your program at VIU, or you haven’t been successful in obtaining a visa and wish to cancel your enrollment, please contact us right away at&nbsp;<a>Study@viu.ca</a>&nbsp; or <a>Masters@viu.ca</a> for students entering Masters programs.&nbsp; Click here for more information on <a>VIU International Tuition Fee Deferral and Refund Policy.</a></p></div>'
            #require_chinese_en = remove_tags(require_chinese_en)
            # print(require_chinese_en)
        except:
            require_chinese_en = None
            # print(require_chinese_en)

#17 特殊专业要求
        try:
            specific_requirement_en = response.xpath('//*[@id="admission-requirements"]/div[1]/span/span').extract()[0]
            #specific_requirement_en = remove_tags(specific_requirement_en)
            specific_requirement_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',specific_requirement_en)
            #specific_requirement_en = specific_requirement_en.replace('\r\n','')
            #specific_requirement_en = re.findall('Required high school classes(.*)2.',specific_requirement_en)[0]
            #specific_requirement_en = remove_tags(specific_requirement_en,keep=("li","ul"))
           # print(specific_requirement_en)
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
            min_language_require = '6.5 (no band below 6.0)/88 (no section below 20)'
            min_language_require = remove_tags(min_language_require)
            # print(min_language_require)
        except:
            min_language_require = None
            # print(min_language_require)

#25 雅思要求
        try:
            ielts_desc = '6.5 (no band below 6.0)'
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
            toefl_code = '9581'
            #toefl_code = remove_tags(toefl_code)
            # print(toefl_code)
        except:
            toefl_code = None
            # print(toefl_code)

#29 toefl_desc
        try:
            toefl_desc = '88 (no section below 20)'
            #toefl_desc = remove_tags(toefl_desc)
            # print(toefl_desc)
        except:
            toefl_desc = None
            # print(toefl_desc)

#30 toefl
        try:
            toefl = '88'
            #toefl = re.findall('\d\d',toefl)
            #toefl = remove_tags(toefl)
            #print(toefl)
        except:
            toefl = None
            #print(toefl)

#31 toefl_?
        toefl_l = 20
        toefl_s = 20
        toefl_r = 20
        toefl_w = 20

# 32 alevel
        try:
            alevel = None
            #alevel = remove_tags(alevel)
            # print(alevel)
        except:
            alevel = None
            # print(alevel)

#33 ib
        try:
            ib = 'VIU recognizes the International Baccalaureate program. Courses at the Subsidiary Level are roughly equivalent to enriched versions of B.C. Grade 11 courses in academic disciplines. Courses at the Higher Levelare roughly equivalent to enriched B.C. Grade 12.'
            #print(ib)
        except:
            ib = None
            #print(ib)

#34 ap
        try:
            ap = 'A grade of 4 or higher on the exam is required for credit consideration. Courses with exam grades of 3 or less will not be eligible for credit or advance standing.'
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
            # print(other)
        except:
            other = None
            # print(other)

        # sat act 代码 介绍
        sat_code = '9581'
        sat1_desc = None
        sat2_desc = None
        act_code = None
        act_desc = None

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
        #item["major_name_en"] = major_name_en
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
        item["toefl_code"] = '9581'
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
        try:
            major_name_en_list = response.xpath('//*[@id]/div/div[6]/span/span/ul/li/a').extract()
            if len(major_name_en_list) == 0:
                item["major_name_en"] = response.xpath('//h1').extract()[0]
                item["major_name_en"] = remove_tags(item["major_name_en"])

               # yield item
            else:
                for i in major_name_en_list:
                    item["major_name_en"] = i
                    item["major_name_en"] = remove_tags(item["major_name_en"])
                    #yield  item
            #major_name_en = major_name_en.replace('\r\n','').replace('\n','').replace('           ','').replace('\t','').replace('     ','')
            #major_name_en = remove_tags(major_name_en)

        except:
            item["major_name_en"] = None
        #print(item["major_name_en"])
            #yield item


