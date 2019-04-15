import scrapy
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from scrapySchool_Canada_College import getItem
from w3lib.html import remove_tags
import requests
import re
import time

class BaiduSpider(scrapy.Spider):
    name = 'St_Clair_College_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['http://www.stclaircollege.ca/programs/postsec/architectural/',
'http://www.stclaircollege.ca/programs/postsec/autism/',
'http://www.stclaircollege.ca/programs/postsec/biomedical/',
'http://www.stclaircollege.ca/programs/postsec/borderservices/',
'http://www.stclaircollege.ca/programs/postsec/borderservices_ft/',
'http://www.stclaircollege.ca/programs/postsec/business/',
'http://www.stclaircollege.ca/programs/postsec/business_accounting/',
'http://www.stclaircollege.ca/programs/postsec/business_marketing/',
'http://www.stclaircollege.ca/programs/postsec/busadmin_accounting/',
'http://www.stclaircollege.ca/programs/postsec/busadmin_finance/',
'http://www.stclaircollege.ca/programs/postsec/busadmin_hr/',
'http://www.stclaircollege.ca/programs/postsec/busadmin_marketing/',
'http://www.stclaircollege.ca/programs/postsec/cardiovascular_technology/',
'http://www.stclaircollege.ca/programs/postsec/carpentry/',
'http://www.stclaircollege.ca/programs/postsec/chemlab/',
'http://www.stclaircollege.ca/programs/postsec/child_youth/',
'http://www.stclaircollege.ca/programs/postsec/child_youth_acc/',
'http://www.stclaircollege.ca/programs/postsec/civil/',
'http://www.stclaircollege.ca/programs/postsec/comm_justice/',
'http://www.stclaircollege.ca/programs/postsec/cice/',
'http://www.stclaircollege.ca/programs/postsec/comp_technician/',
'http://www.stclaircollege.ca/programs/postsec/comp_technology/',
'http://www.stclaircollege.ca/programs/postsec/construction/',
'http://www.stclaircollege.ca/programs/postsec/culinary_management/',
'http://www.stclaircollege.ca/programs/postsec/dental_assist/',
'http://www.stclaircollege.ca/programs/postsec/dental_hygiene/',
'http://www.stclaircollege.ca/programs/postsec/dsw_acc/',
'http://www.stclaircollege.ca/programs/postsec/dsw/',
'http://www.stclaircollege.ca/programs/postsec/ece/',
'http://www.stclaircollege.ca/programs/postsec/ece/',
'http://www.stclaircollege.ca/programs/postsec/ece_acc/',
'http://www.stclaircollege.ca/programs/postsec/educational_support/',
'http://www.stclaircollege.ca/programs/postsec/elec_eng_technician/',
'http://www.stclaircollege.ca/programs/postsec/elec_techniques/',
'http://www.stclaircollege.ca/programs/postsec/electromech_technician/',
'http://www.stclaircollege.ca/programs/postsec/elec_automation/',
'http://www.stclaircollege.ca/programs/postsec/eap/',
'http://www.stclaircollege.ca/programs/postsec/esports_admin/',
'http://www.stclaircollege.ca/programs/postsec/esthetician/',
'http://www.stclaircollege.ca/programs/postsec/event_management/',
'http://www.stclaircollege.ca/programs/postsec/programs/postsec/fashion_design/',
'http://www.stclaircollege.ca/programs/postsec/programs/postsec/fitness_health_promotion/',
'http://www.stclaircollege.ca/programs/postsec/generalarts/',
'http://www.stclaircollege.ca/programs/postsec/programs/postsec/graphic/',
'http://www.stclaircollege.ca/programs/postsec/hair/',
'http://www.stclaircollege.ca/programs/postsec/hvac/',
'http://www.stclaircollege.ca/programs/postsec/social_justice/',
'http://www.stclaircollege.ca/programs/postsec/hospitality/',
'http://www.stclaircollege.ca/programs/postsec/hr_management/',
'http://www.stclaircollege.ca/programs/postsec/interior/',
'http://www.stclaircollege.ca/programs/postsec/international_bus_mgmt/',
'http://www.stclaircollege.ca/programs/postsec/journalism/',
'http://www.stclaircollege.ca/programs/postsec/horticulture/',
'http://www.stclaircollege.ca/programs/postsec/liberal_arts/',
'http://www.stclaircollege.ca/programs/postsec/mech_ind/',
'http://www.stclaircollege.ca/programs/postsec/mech_auto/',
'http://www.stclaircollege.ca/programs/postsec/mech_cadcam/',
'http://www.stclaircollege.ca/programs/postsec/precision_metal_cutting/',
'http://www.stclaircollege.ca/programs/postsec/media_convergence/',
'http://www.stclaircollege.ca/programs/postsec/medlab/',
'http://www.stclaircollege.ca/programs/postsec/medlab_tech/',
'http://www.stclaircollege.ca/programs/postsec/mobile_app_dev/',
'http://www.stclaircollege.ca/programs/postsec/motive/',
'http://www.stclaircollege.ca/programs/postsec//programs/postsec/music_theatre/',
'http://www.stclaircollege.ca/programs/postsec/native_ece/',
'http://www.stclaircollege.ca/programs/postsec/nursing/',
'http://www.stclaircollege.ca/programs/postsec/otapa/',
'http://www.stclaircollege.ca/programs/postsec/office_exec/',
'http://www.stclaircollege.ca/programs/postsec/office_exec_ft/',
'http://www.stclaircollege.ca/programs/postsec/office_general/',
'http://www.stclaircollege.ca/programs/postsec/office_health_services/',
'http://www.stclaircollege.ca/programs/postsec/office_health_services_ft/',
'http://www.stclaircollege.ca/programs/postsec/paralegal/',
'http://www.stclaircollege.ca/programs/postsec/paralegal_accelerated/',
'http://www.stclaircollege.ca/programs/postsec/paramedic/',
'http://www.stclaircollege.ca/programs/postsec/personalsupport/',
'http://www.stclaircollege.ca/programs/postsec/pharmacy/',
'http://www.stclaircollege.ca/programs/postsec/plumbing/',
'http://www.stclaircollege.ca/programs/postsec/police/',
'http://www.stclaircollege.ca/programs/postsec/police_ft/',
'http://www.stclaircollege.ca/programs/postsec/power_eng/',
'http://www.stclaircollege.ca/programs/postsec/powerline_technician/',
'http://www.stclaircollege.ca/programs/postsec/pract_nursing/',
'http://www.stclaircollege.ca/programs/postsec/prehealth_sciences_pathway/',
'http://www.stclaircollege.ca/programs/postsec/preservicefirefighter/',
'http://www.stclaircollege.ca/programs/postsec/psi/',
'http://www.stclaircollege.ca/programs/postsec/psi_ft/',
'http://www.stclaircollege.ca/programs/postsec//programs/postsec/public_relations/',
'http://www.stclaircollege.ca/programs/postsec//programs/postsec/respiratory_therapy/',
'http://www.stclaircollege.ca/programs/postsec/ssw_gerontology/',
'http://www.stclaircollege.ca/programs/postsec/sport_management/',
'http://www.stclaircollege.ca/programs/postsec/supply_chain_management/',
'http://www.stclaircollege.ca/programs/postsec/tourism/',
'http://www.stclaircollege.ca/programs/postsec/vet_tech/',
'http://www.stclaircollege.ca/programs/postsec/wia/',
'http://www.stclaircollege.ca/programs/postsec/welding/',
'http://www.stclaircollege.ca/programs/postsec/woodwork/',]
    D = ['http://www.stclaircollege.ca/programs/postsec/dsw_acc/',
'http://www.stclaircollege.ca/programs/postsec/diagnostic_medical_sonography/',
'http://www.stclaircollege.ca/programs/postsec/child_youth_acc/',
'http://www.stclaircollege.ca/programs/postsec/fashion_design/',
'http://www.stclaircollege.ca/programs/postsec/fitness_health_promotion/',
'http://www.stclaircollege.ca/programs/postsec/graphic/',
'http://www.stclaircollege.ca/programs/postsec/music_theatre/',
'http://www.stclaircollege.ca/programs/postsec/native_comm/',
'http://www.stclaircollege.ca/programs/postsec/office_health_services_ft/',
'http://www.stclaircollege.ca/programs/postsec/public_relations/',
'http://www.stclaircollege.ca/programs/postsec/respiratory_therapy/',]

    for i in D:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        item = getItem.get_item(ScrapyschoolCanadaCollegeItem)

        try:
            major_name_en = response.xpath('//*[@id="contentheader_content"]|//*[@id="body"]/div[2]/div[2]/h1').extract()[0]
            major_name_en = remove_tags(major_name_en)
            major_name_en = major_name_en.replace('\r\n','').replace('					','').replace('				','')
            #print(major_name_en)
        except:
            major_name_en = None
            #print(major_name_en)
#programme_code
        try:
            campus_list = response.xpath('//li[contains(text(),"Campus:")]/following-sibling::li').extract()
            campus_list = ''.join(campus_list)
            campus_list = remove_tags(campus_list)
            campus_list = campus_list.replace('\r\n','')
            campus_list = campus_list.replace('							','==')
            # if '-' in campus_list:
            #     campus_list = re.sub('(-.*)==',campus_list)
            # else:
            #     pass
            campus_list = campus_list.lstrip('==')
            campus_list = campus_list.split('==')
            #print(campus_list)
            #print(response.url)
        except:
            campus_list = None
            #print(campus_list)
        try:
            duration = response.xpath('//li[contains(text(),"Program Length")]/following-sibling::li').extract()[0]
            duration = remove_tags(duration)
            if 'Four Year' in duration:
                duration = '4'
            elif 'Two Year' in duration:
                duration = '2'
            elif 'One Year' in duration:
                duration = '1'
            elif 'weeks' in duration:
                duration = 'No'
            elif 'Three Year' in duration:
                duration = '3'
            else:
                duration = None
            #print(duration)
        except:
            duration = None
            #print(duration)

#1.学校名称
        school_name = 'St. Clair College'



#4. 学院
        try:
            department = response.xpath('//*[@id="block-nu-breadcrumbs"]/div/nav/ol/li[4]/a').extract()[0]
            department = remove_tags(department,keep=("i"))

            #print(len(department))
           # print(department)
            #print(response.url)
        except:
            department = None
            #print(department)

# 4.
        try:
            degree_name = response.xpath('//li[contains(text(),"Program Length")]/following-sibling::li').extract()[0]
            #degree_name_list = remove_tags(degree_name_list,keep=('li','ul'))
            #degree_name_list = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_name_list)
            #degree_name_list = degree_name_list.replace('\t','').replace('\n','').replace('\xa0','').replace(' class="list-inline uofs-cta-list','')
            # degree_name_list = degree_name_list.replace('<li>','').replace('</li>','---')
            # degree_name_list = degree_name_list.replace('<span>','').replace('</span>','---')
           # degree_name_list = degree_name_list.split('</li><li>')
            degree_name = remove_tags(degree_name)
            D = ['http://www.stclaircollege.ca/programs/postsec/hr_management/',
'http://www.stclaircollege.ca/programs/postsec/international_bus_mgmt/',
'http://www.stclaircollege.ca/programs/postsec/supply_chain_management/',
'http://www.stclaircollege.ca/programs/postsec/autism/',
'http://www.stclaircollege.ca/programs/postsec/autism_alternate',
'http://www.stclaircollege.ca/programs/postsec/child_youth_acc/',
'http://www.stclaircollege.ca/programs/postsec/dsw_acc/',
'http://www.stclaircollege.ca/programs/postsec/ece_acc/',
'http://www.stclaircollege.ca/programs/postsec/event_management/',
'http://www.stclaircollege.ca/programs/postsec/media_convergence/',
'http://www.stclaircollege.ca/programs/postsec/wia/',
'http://www.stclaircollege.ca/programs/postsec/borderservices_ft/',
'http://www.stclaircollege.ca/programs/postsec/paralegal_accelerated/',
'http://www.stclaircollege.ca/programs/postsec/police_ft/',
'http://www.stclaircollege.ca/programs/postsec/psi_ft/',]
            if 'Advanced Diploma' in degree_name:
                degree_name = 'Advanced Diploma'
                degree_level = '4'
            elif response.url in D:
                degree_level = '2'
                if 'Graduate Certificate' in degree_name:
                    degree_name = 'Post_graduate(Certificate)'
                elif 'Diploma' in degree_name:
                    degree_name = 'Post-Diploma'
                else:
                    degree_name = None
                #print(degree_name)
            elif 'Certificate' in degree_name:
                degree_name = 'No'
                degree_level = '0'
            else:
                degree_level = '3'
                degree_name = 'Diploma'
           # print(degree_name)
            #elif  ''
            #print(response.url)
        except:

            degree_name = None
            #print(degree_name)
#
#5.学位描述
        try:
            degree_overview_en = response.xpath('//*[@id="rightcolumn_inner"]').extract()
            degree_overview_en = ''.join(degree_overview_en)
            #degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_overview_en)
            #degree_overview_en = degree_overview_en.replace('\r\n','')
            #degree_overview_en = degree_overview_en.replace('\n','')
            #degree_overview_en = degree_overview_en.replace('\n','')
            #degree_overview_en = degree_overview_en.replace('  ',' ')
            #degree_overview_en = degree_overview_en.replace('					','')
            #degree_overview_en = degree_overview_en.replace('			  	','')
            degree_overview_en = degree_overview_en.replace('\n','')
            degree_overview_en = re.findall('PROGRAM OVERVIEW(.*)PROGRAM HIGHLIGHTS',degree_overview_en)[0]
            degree_overview_en = degree_overview_en.replace('\t','').replace('\r','')
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
            start_date = response.xpath('//li[contains(text(),"Starts")]/following-sibling::li').extract()[0]
            start_date = remove_tags(start_date)
            start_date = start_date.replace('September','2019-09').replace('January','2019-01').replace('May','2019-05').replace('July','2019-07').replace('March','2019-03').replace('October','2019-10').replace(' and ',',').replace(' &amp; ',',').replace(', ',',').replace(' (Semester 3)','').replace(' (Semester 4)','').replace(' (Windsor only)','')

            # start_date = ','.join(start_date)
            # start_date = remove_tags(start_date)
            # start_date = start_date.replace('Spring','').replace('Winter','').replace('Summer','').replace('Fall','')
            # start_date = start_date.replace('September 2019','2019-09').replace('May 2019','2019-05').replace('July 2019','2019-07').replace('January 2020','2020-01').replace('January 2019','2019-01')
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
            modules_en = response.xpath('//h4[contains(text(),"REQUIREMENTS")]/following-sibling::div').extract()
            modules_en = ''.join(modules_en)
            modules_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',modules_en)
            modules_en = modules_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
            #print(modules_en)
        except:
            modules_en = None
            #print(modules_en)

#11.就业方向
        try:
            career_en = response.xpath('//*[@id="rightcolumn_inner"]').extract()[0]
            career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',career_en)
            career_en = career_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
            career_en = re.findall('CAREER OPPORTUNITIES(.*)ADDITIONAL INFORMATION',career_en)[0]
           # print(career_en)
        except:
            career_en = None
          #  print(career_en)

#12.截止日期
        try:
            if '2019-01' in start_date:
                deadline = '2019-04-26'
            else:
                deadline = None
            # deadline = response.xpath('//*[@id="Admissionrequirementsanddeadlines-subsection-0"]/table/tbody/tr/td[3]').extract()
            # deadline = '---'.join(deadline)
            # deadline = remove_tags(deadline)
            # deadline = deadline.replace('Documents due: ', '')
            # deadline =  deadline.replace('Sep 1, 2018Oct 1, 2018','2018-09-01').replace('Feb 1, 2019Mar 1, 2019','2019-02-01').replace('Mar 1, 2019Apr 1, 2019','2019-03-01').replace('May 1, 2019Jun 1, 2019','2019-05-01').replace('Sep 1, 2019Oct 1, 2019','2019-09-01').replace('Feb 15, 2019Mar 1, 2019','2019-02-15').replace('---',',')
            # #deadline = remove_tags(deadline)
            # #print(deadline)
        except:
            deadline = None
            #print(deadline)
#13.学费
        try:
            tuition_fee = 'http://www.stclaircollege.ca/programs/postsec/docs/fees/Tuition-Fee-Sheet-2018-19.pdf'
            #tuition_fee = remove_tags(tuition_fee)
            #tuition_fee = tuition_fee.replace('$','')
            #print(tuition_fee)
        except:
            tuition_fee = None
            #print(tuition_fee)
#14 申请费:
        apply_fee = '125'
        try:

            entry_requirements_en = response.xpath('//*[@id="rightcolumn_inner"]').extract()
            entry_requirements_en = ''.join(entry_requirements_en)
            entry_requirements_en =  re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',entry_requirements_en)
            entry_requirements_en = entry_requirements_en.replace('\r\n','')
            entry_requirements_en = re.findall('ADMISSION REQUIREMENTS(.*)PROGRAM OVERVIEW',entry_requirements_en)[0]
            #print(entry_requirements_en)
            #print(abc)
        except:
            entry_requirements_en = None
            #print(entry_requirements_en)
#16 中国学生申请要求
        try:
            require_chinese_en = '<div>If you are not a Canadian citizen or landed immigrant, you will need a Canadian Study Permit to study in Canada and a Letter of Acceptance - issued by the College - in order to apply for the permit.<br><br>General diploma programs admission requirement for international students are as follows:<br><br><b>Canada &amp; USA:</b> High school diploma and Grade 12 transcript, or equivalent.<br><br><b>British education system:</b> General Certificate of Education showing passes in six (6) academic subjects (including English) at the Ordinary level.<br><br><b>Caribbean countries (English):</b> High school diploma and transcript, or equivalent.<br><br><b>West Africa (Nigeria, Ghana, etc.):</b> WAEC (or NECO) transcript with online verifying scratch card number and PIN required.<br><br><b>South Asia (Pakistan, Bangladesh, Nepal, Sri Lanka, etc.):</b> High school diploma and Grade 12 transcript. IELTS 5.5 with no band lower than 5.0, or PTE (Pearson Test of English) Level 51, or TOEFL paper-based test (PBT) score of 500, or internet-based test (iBT) score of 61, or computer-based test (CBT) score of 173.<br><br><strong>India:</strong> High school diploma and Grade 12 transcript. IELTS 6.0 with no band lower than 5.5, or PTE (Pearson Test of English) Level 51, proficiency tests must have been taken within the previous two years from the date of submitting application.<br><br>Other regions (English proficiency test required)<ul>    <li>High school diploma/graduation certificate and transcript or equivalent in original language and English translation.</li>    <li>English proficiency requirement: TOEFL iBT 61, IELTS (overall band) 5.5, or PTE (Pearson Test of English) Level 51</li></ul>Note:<ul>    <li>For information about IELTS, see <a href="/programs/coned/ielts.html">International English Language Testing System</a>.</li>    <li>Applicants who do not have the minimum TOEFL or IELTS score will be required to write the English Proficiency Test (CanTEST) after arrival at the College. Students who do not pass the CanTEST will need to register in the St. Clair College English as a Second Language (ESL) program prior to entering post-secondary programs.</li>    <li>Pharmacy Technician  for the Pharmacy Technician Program.</li></ul></div>'
            require_chinese_en = remove_tags(require_chinese_en)
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
            ielts_desc = 'English proficiency requirement: TOEFL iBT 61, IELTS (overall band) 5.5, or PTE (Pearson Test of English) Level 51'
            #ielts_desc = remove_tags(ielts_desc)
            # print(ielts_desc)
        except:
            ielts_desc = None
            # print(ielts_desc)

#26 ielts
        try:
            ielts = '5.5'
            #ielts = re.findall('\d\.\d',ielts)
            #ielts = remove_tags(ielts)
            #print(ielts)
        except:
            ielts = None
            #print(ielts)
#27 ielts_?

        ielts_l = ''
        ielts_s = ''
        ielts_r = ''
        ielts_w = ''

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
            toefl_desc = 'English proficiency requirement: TOEFL iBT 61, IELTS (overall band) 5.5, or PTE (Pearson Test of English) Level 51'
            #toefl_desc = remove_tags(toefl_desc)
            # print(toefl_desc)
        except:
            toefl_desc = None
            # print(toefl_desc)

#30 toefl
        try:
            toefl = '61'
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
            ap = ''
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
            other = '1.http://www.stclaircollege.ca/registrar/    ——》deadline  2.specific_requirement_en(确认没有)  3.http://www.stclaircollege.ca/international/admissionpolicies.html  ——》雅思 托福 确认没有小分（没有托福code）4.average_score:等待老师给经验值4.http://www.stclaircollege.ca/programs/postsec/docs/fees/Tuition-Fee-Sheet-2018-19.pdf 4,学费联系校代'
            #other = remove_tags(other)
            # print(other)
        except:
            other = None
            # print(other)

#平均分  average_score
        average_score = ''

# degree_name_desc
        try:
            degree_name_desc = degree_overview_en
        except:
            degree_name_desc = None

        item['school_name'] = school_name
        #item['location'] = location
       # item['campus'] = campus
        item['department'] = department
        item['degree_name'] = degree_name
        item['degree_name_desc'] = degree_name_desc
        item['major_name_en'] = major_name_en
       # item['programme_code'] = programme_code
        item['overview_en'] = overview_en
        item['start_date'] = start_date
        item['duration'] = duration
        item['duration_per'] = '1'
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
        item['degree_level'] = degree_level


        for cam in  campus_list:
            campus = cam
            campus = re.sub('( -.*)','',campus)
            item["campus"] = campus
            try:
                item["campus"] = re.findall('(.*)\(.*\)',campus)[0]
                item["programme_code"] =  re.findall('\((.*)\)',campus)[0]
                item["location"] = item["campus"]

            except:
                item["campus"] = 'No'
                item["programme_code"] =  'No'
                item["location"] = 'No'

            if 'No' not in item["campus"] and 'No' not in item["programme_code"] and 'No' not in item["location"] and 'No' not in item["degree_name"] and 'No' not in item['duration']:
                yield item
            else:
                pass
            #print(item["programme_code"])
            #print(item["campus"])

            #print(campus)
     #   yield item