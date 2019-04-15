 # _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/10 10:42'
import scrapy,json
import re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from w3lib.html import remove_tags
from scrapySchool_England.clearSpace import  clear_space_str
from scrapySchool_England.translate_date import  tracslateDate
from scrapySchool_England.translate_date import tracslateDate
class TeessideUniversitySpider(scrapy.Spider):
    name = 'TeessideUniversity_p'
    allowed_domains = ['tees.ac.uk/']
    start_urls = []
    C= [
        'http://www.tees.ac.uk/postgraduate_courses/Computer_Games/MA_3D_Games_Art.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Business_Accounting_Marketing_&_Enterprise/MSc_Accounting_and_Finance.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MSc_Advanced_Clinical_Practice.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Advanced_Home_Construction_&_Futures/MSc_Advanced_Home_Futures.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MSc_Advanced_Practitioner.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgCert_Advancing_Human_Factors_in_Health_and_Social_Care.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgCert_Advancing_Quality_Improvement_in_Health_and_Social_Care.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MA_Advancing_Quality_Safety_and_Governance_in_Health_and_Social_Care.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Computer_Animation_&_Visual_Effects/MA_Animation.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Education_Early_Childhood_&_Youth/PgCert_Applied_Education_Leadership.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgDip_MSc_Autism_Practice.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Business_Accounting_Marketing_&_Enterprise/Doctorate_Business_Administration_(DBA).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Law_Policing_&_Investigation/Graduate_Fast-track_Diploma_CILEx_.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Engineering/PgDip_MSc_Civil_and_Structural_Engineering.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Engineering/MSc_Civil_and_Structural_Engineering_(with_Advanced_Practice).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/Doctorate_Clinical_Psychology_(DClinPsy).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MRes_Clinical_Research.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgCert_Clinical_Research_and_Evidence-based_Medicine.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MSc_Cognitive_Behavioural_Therapy.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgDip_Cognitive_Behavioural_Therapy_(IAPT).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/The_Arts/MA_Comics_and_Graphic_Novels.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Computing_&_Web/MRes_Computer_Science.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Computing_&_Web/MSc_Computer_Science.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Computing_&_Web/MSc_Computing.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Computer_Games/MA_Concept_Art.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Psychology/Doctorate_Counselling_Psychology.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/English/MA_Creative_Writing.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/English/MA_Creative_Writing_(Distance_Learning).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Crime_Forensic_&_Investigative_Sciences/PgDip_MSc_Crime_Intelligence_and_Data_Analytics.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Crime_Forensic_&_Investigative_Sciences/MSc_Crime_Intelligence_and_Data_Analytics_(with_Advanced_Practice).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Law_Policing_&_Investigation/MSc_Criminal_Investigation.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Criminology_&_Sociology/MSc_Criminology.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Computing_&_Web/MSc_Cybersecurity.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Computing_&_Web/MSc_Data_Science.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgCert_PgDip_MSc_Diagnostic_Imaging_Reporting.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgDip_MSc_Diagnostic_Radiography_(Pre-registration).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MSc_Dietetics_(Pre-Registration).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Design_Fashion_&_Textiles/MA_Digital_Arts_and_Design.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Design_Fashion_&_Textiles/MA_Digital_Arts_and_Design_with_Advanced_Practice.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Media_&_Communications/MA_Digital_Media_and_Communications_.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Education_Early_Childhood_&_Youth/Doctorate_Education.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Education_Early_Childhood_&_Youth/MA_Education.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Education_Early_Childhood_&_Youth/MA_Education_(Early_Childhood_Studies)_.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Education_Early_Childhood_&_Youth/MA_Education_(Educational_Leadership).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Education_Early_Childhood_&_Youth/Professional_Graduate_Certificate_in_Education_Education_and_Training.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Engineering/PgDip_MSc_Electrical_Power_and_Energy_Systems.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Engineering/MSc_Electrical_Power_and_Energy_Systems_(with_Advanced_Practice).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Life_&_Physical_Sciences/PgDip_MSc_Energy_and_Environmental_Management.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Life_&_Physical_Sciences/MSc_Energy_and_Environmental_Management_(with_Advanced_Practice).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/English/MA_English.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgDip_MSc_Evidence-based_Medicine.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MSc_Evidence-based_Practice.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/The_Arts/MA_Fine_Art.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Engineering/PgDip_MSc_Food_Processing_Engineering.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Engineering/MSc_Food_Processing_Engineering_(with_Advanced_Practice).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Life_&_Physical_Sciences/PgDip_MSc_Food_Science_and_Biotechnology.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Life_&_Physical_Sciences/MSc_Food_Science_and_Biotechnology_(with_Advanced_Practice).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Psychology/MSc_Forensic_Psychology.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgCert_MSc_Forensic_Radiography.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Crime_Forensic_&_Investigative_Sciences/PgDip_MSc_Forensic_Science.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Crime_Forensic_&_Investigative_Sciences/PgDip_MSc_Forensic_Science_with_Advanced_Practice.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Design_Fashion_&_Textiles/MA_Future_Design.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Design_Fashion_&_Textiles/MA_Future_Design_(with_Advanced_Practice).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Computer_Games/MA_Games_Design.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MCh_General_and_Oncoplastic_Breast_Surgery.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MSc_Health_and_Social_Care_Sciences_(Generic_pathway).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Psychology/MSc_Health_Psychology_and_Clinical_Skills.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/History/MA_History.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MSc_Human_Factors_and_Patient_Safety.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Business_Accounting_Marketing_&_Enterprise/MA_Human_Resource_Management.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Business_Accounting_Marketing_&_Enterprise/MA_Human_Resource_Management_(Applied).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/The_Arts/MA_Illustration.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Media_&_Communications/MA_Immersive_Events.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Engineering/PgDip_MSc_Instrumentation_and_Control_Engineering.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Engineering/MSc_Instrumentation_and_Control_Engineering_(with_Advanced_Practice).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Business_Accounting_Marketing_&_Enterprise/MSc_International_Management.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Business_Accounting_Marketing_&_Enterprise/PgDip_International_Management.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Business_Accounting_Marketing_&_Enterprise/MSc_International_Management_(Accountancy).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Business_Accounting_Marketing_&_Enterprise/MSc_International_Management_(Applied).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Business_Accounting_Marketing_&_Enterprise/MSc_International_Management_(Digital_Business).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Business_Accounting_Marketing_&_Enterprise/MSc_International_Management_(Human_Resource_Management).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Business_Accounting_Marketing_&_Enterprise/MSc_International_Management_(Marketing_Management).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Business_Accounting_Marketing_&_Enterprise/MSc_International_Management_(Operations).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Computing_&_Web/MSc_IT_Project_Management.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Law_Policing_&_Investigation/Master_of_Laws_LLM.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Law_Policing_&_Investigation/Master_of_Laws_LLM_(Applied).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgCert_Low_Intensity_Assessment_and_Intervention_Skills_for_Psychological_Wellbeing_Practice.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Business_Accounting_Marketing_&_Enterprise/MBA_Master_of_Business_Administration.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Business_Accounting_Marketing_&_Enterprise/MBA_Master_of_Business_Administration_(Applied).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Business_Accounting_Marketing_&_Enterprise/MBA_Master_of_Business_Administration_Degree_Apprenticeship.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MPH_Master_of_Public_Health_.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Engineering/PgDip_MSc_Mechanical_Engineering.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Engineering/MSc_Mechanical_Engineering_(with_Advanced_Practice).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MSc_Medical_Ultrasound.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgCert_Medical_Ultrasound.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgDip_Medical_Ultrasound.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MSc_Midwifery_Studies_(Pre-registration).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Media_&_Communications/MA_Multimedia_Public_Relations.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgDip_MSc_Occupational_Therapy_(Pre-registration).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Engineering/PgDip_MSc_Oil_and_Gas_Management.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Engineering/MSc_Oil_and_Gas_Management_(with_Advanced_Practice).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MCh_Orthopaedics.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Engineering/PgDip_MSc_Petroleum_Engineering.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Engineering/MSc_Petroleum_Engineering_(with_Advanced_Practice).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/The_Arts/MA_Photography.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MSc_Physiotherapy_(Pre-registration).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Media_&_Communications/MA_Producing_for_Film_and_Television.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Engineering/PgDip_MSc_Project_Management.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Engineering/MSc_Project_Management_(with_Advanced_Practice).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Psychology/MSc_Psychology.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Psychology/Diploma_in_Psychology_(Graduate_Conversion).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Psychology/Doctorate_Psychology_(Top-up).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/Doctor_of_Public_Health_(DrPH).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Criminology_&_Sociology/MSc_Social_Research_Methods_(Criminology).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Criminology_&_Sociology/MSc_Social_Research_Methods_(Social_Policy).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MA_Social_Work.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MSc_Specialist_Community_Public_Health_Nursing_(Health_Visiting).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgDip_Specialist_Community_Public_Health_Nursing_(Health_Visiting).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgDip_Specialist_Community_Public_Health_Nursing_(Occupational_Health_Nursing).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MSc_Specialist_Community_Public_Health_Nursing_(School_Nursing).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgDip_Specialist_Community_Public_Health_Nursing_(School_Nursing).cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/PgDip_MSc_Specialist_Practice_in_District_Nursing.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/Professional_Graduate_Certificate_Specialist_Practice_in_District_Nursing.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Sport_&_Exercise/MSc_Sport_and_Exercise.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Sport_&_Exercise/MSc_Sports_Rehabilitation.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MCh_Surgical_Gastroenterology_and_Minimally_Invasive_Surgery.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Computer_Animation_&_Visual_Effects/MSc_Technical_Direction_for_Visual_Effects.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MSc_Transformational_Leadership_in_Health_and_Social_Care.cfm',
        'http://www.tees.ac.uk/postgraduate_courses/Health_&_Social_Care/MCh_Vascular_and_Endovascular_Surgery.cfm'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Teesside University'
        # print(university)

        #2.url
        url = response.url

        #3.programme_en
        programme_en = response.xpath('//*[@id="top"]/section[2]/div/div[1]/div[1]/div[2]/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        degree_name = programme_en.split()[0]
        programme_en = programme_en.replace(degree_name,'').strip()
        # print(degree_name)

        #6.overview_en
        overview_en = response.xpath('//*[@id="top"]/section[2]/div/div[1]/div[1]/div[2]/p[1]').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #7.modules_en
        modules_en = response.xpath('//*[@id="tab2"]/div/p').extract()
        modules_en ='\n'.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #8.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'How you are assessed')]//following-sibling::*").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #9.career_en
        career_en = response.xpath("//*[contains(text(),'Career opportunities')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #10.rntry_requirements
        rntry_requirements = response.xpath("//h2[contains(text(),'Entry requirements')]//following-sibling::*").extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #11.teach_time
        teach_time_list = response.xpath("//*[contains(text(),'Course information')]//following-sibling::*[1]").extract()
        teach_time_list =''.join(teach_time_list)
        teach_time_list = remove_tags(teach_time_list)
        teach_time_list = clear_space_str(teach_time_list)
        # print(teach_time_list)
        if 'Full-time' in teach_time_list:
            teach_time='Full-time'
        else:teach_time= 'Part-time'

        #12.duration #13.duration_per
        try:
            duration = re.findall('\d+',teach_time_list)[0]
        except:
            duration = None
        if int(duration) ==2018:
            duration = 1
            duration_per = 1
        elif int(duration)>4:
            duration_per = 3
        elif 'year' in teach_time_list:
            duration_per = 1
        elif 'years' in teach_time_list:
            duration_per = 1
        else:
            duration_per = 3
        # print(duration,"*****************",duration_per)

        #14.teach_type
        teach_type = 'taught'

        #15.start_date
        start_date = '2018-9,2019-1'

        #16.tuition_fee_pre
        tuition_fee_pre = '£'

        #17.other
        other='https://www.tees.ac.uk/sections/international/fees.cfm'

        #18.require_chinese_en
        require_chinese_en = '<p>(4 year) Bachelor degrees with a GPA 2.7/4.0 or 70% from a National University; or from a Project 211 University with a GPA 2.6/4.0 or 65%; or from a Private University with GPA 2.75/4.0 or 75%.</p>'


        #19.ielts,20212223
        if 'Arts and Design' in programme_en:
            ielts = 6.0
        elif 'Business' in programme_en:
            ielts = 6.0
        elif 'Computing' in programme_en:
            ielts = 6.0
        elif 'Computing' in programme_en:
            ielts = 6.0
        elif 'Sport' in programme_en:
            ielts = 6.0
        elif 'Engineering' in programme_en:
            ielts = 6.0
        elif 'Science' in programme_en:
            ielts = 6.0
        elif 'Multimedia' in programme_en:
            ielts = 6.0
        elif 'Communications' in programme_en:
            ielts = 6.0
        elif 'MBA' in programme_en:
            ielts = 6.5
        elif 'Education' in programme_en:
            ielts = 6.5
        elif 'English' in programme_en:
            ielts = 6.5
        elif 'Law' in programme_en:
            ielts = 6.5
        elif 'History' in programme_en:
            ielts = 6.5
        elif 'Psychology' in programme_en:
            ielts = 6.5
        elif 'Criminology' in programme_en:
            ielts = 6.5
        elif 'Criminal' in programme_en:
            ielts = 6.5
        elif 'Investigation' in programme_en:
            ielts = 6.5
        elif 'Human Resource' in programme_en:
            ielts = 6.5
        elif 'Psychology' in programme_en:
            ielts = 6.5
        elif 'Management' in programme_en:
            ielts = 6.5
        elif 'DBA' in programme_en:
            ielts = 7.0
        elif 'Health' in programme_en:
            ielts = 7.0
        else: ielts=6.0
        if 'PgDip/MSc Diagnostic Radiography' in programme_en:
            ielts_r = 6.5
            ielts_s = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
        elif 'PgDip/MSc Occupational Therapy' in programme_en:
            ielts_r = 6.5
            ielts_s = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
        elif 'MSc Physiotherapy' in programme_en:
            ielts_r = 6.5
            ielts_s = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
        else:
            ielts_r = 5.5
            ielts_s = 5.5
            ielts_w = 5.5
            ielts_l = 5.5
        # print(ielts,ielts_l,ielts_w,ielts_s,ielts_r)
        #24.apply_pre
        apply_pre = '£'
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['rntry_requirements'] = rntry_requirements
        item['teach_time'] = teach_time
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['teach_type'] = teach_type
        item['start_date'] = start_date
        item['tuition_fee_pre'] = tuition_fee_pre
        item['other'] = other
        item['require_chinese_en'] = require_chinese_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        yield  item