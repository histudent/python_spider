# -*- coding: utf-8 -*-
from scrapySchool_Canada_College.items import *
from scrapySchool_Canada_College.getItem import *
from scrapySchool_Canada_College.middlewares import *

class OkanagancollegeSpider(scrapy.Spider):
    name = 'OkanaganCollege'
    # allowed_domains = ['a.b']
    start_urls = ['https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=BachelorOfBusinessAdministration',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=BachelorOfComputerInformationSystemsDegree',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=BachelorofBusinessAdministrationAccountingSpecialty',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=BachelorofBusinessAdministrationHonoursProgram',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=BachelorofBusinessAdministrationFinancialServicesSpecialty',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=BachelorOfBusinessAdministration',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=BachelorofBusinessAdministrationHumanResourcesManagementSpecialty',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=BachelorofBusinessAdministrationManagementSpecialty',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=BachelorofBusinessAdministrationMarketingSpecialty',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=BachelorofBusinessAdministrationTourismandHospitalityManagementSpecialty',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=BridgingProgramintotheBBATechnologyandCISBridge',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=BridgingProgramintotheBBAAssociateofArtsBridge',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=BachelorOfComputerInformationSystemsDegree',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=BachelorOfComputerInformationSystemsDegree',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=BachelorOfComputerInformationSystemsDegree',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BachelorOfBusinessAdministration',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BachelorofBusinessAdministrationAccountingSpecialty',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BachelorofBusinessAdministrationFinancialServicesSpecialty',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BachelorofBusinessAdministrationTourismandHospitalityManagementSpecialty',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BachelorofBusinessAdministrationHumanResourcesManagementSpecialty',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BachelorofBusinessAdministrationManagementSpecialty',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BachelorofBusinessAdministrationMarketingSpecialty',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BachelorofBusinessAdministrationHonoursProgram',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BachelorofBusinessAdministrationTourismandHospitalityManagementSpecialty2',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BusinessAdministrationDiplomaAccountingOption',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BusinessAdministrationDiplomaFinancialServicesOption',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BusinessAdministrationDiplomaGeneralStudiesOption',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BusinessAdministrationDiplomaHumanResourcesManagementOption',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BusinessAdministrationDiplomaManagementOption',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BusinessAdministrationDiplomaMarketingOption',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BusinessAdministrationDiplomaTourismandHospitality',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/BusinessAdministrationDiplomaTourismandHospitalityManagementOption2',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=ComputerInformationSystemsDiploma',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=CulinaryManagementDiploma',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/HumanServiceWorkDiploma',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/HumanKineticsDiploma',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/TherapistAssistantDiploma',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/EarlyChildhoodEducationDiploma',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/EarlyChildhoodEducationInfantToddlerCertificate',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/MechanicalEngineeringTechnology',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/ElectronicEngineeringTechnology',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/NetworkAndTelecommunicationsEngineeringTechnology',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/calendar.aspx?page=WaterQualityAndEnvironmentalEngineeringTechnology',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=EnvironmentalStudiesDiploma',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/diploma-in-communications-culture-and-journalism-s',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/Calendar.aspx?page=WritingAndPublishingDiploma',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/InternationalDevelopmentDiploma',
'https://webapps-5.okanagan.bc.ca/ok/Calendar/CriminalAndSocialJusticeDiploma',]

    def parse(self, response):
        item=get_item(ScrapyschoolCanadaCollegeItem)
        item['school_name']='Okanagan College'
        item['url']=response.url
        # print(response.url)

        #学费页面
        #https://www.okanagan.bc.ca/Assets/Departments+(Education)/International+Students/Documents/Cost+Date+Schedule+2019.pdf
        #副学位课程 https://webapps-5.okanagan.bc.ca/ok/Calendar/AssociateOfArtsDegree
        #该学院没有deadline、career、平均分
        #副学位课程有4个校区，每条专业根据校区拆分成了4条
        #副学位课程没有专业代码
        #中国学生要求
        item['apply_fee'],item['apply_pre']='100','CAD$'
        item['tuition_fee_pre']='$'
        item['require_chinese_en']='<p>If an applicant is under 19 and has not been out of full time high school study for a minimum of one year they must provide proof of high school graduation or equivalent. All other applicants must provide proof of the subject requirements.</p>'

        item['ielts_desc']='Overall band score of 6.0(with no band less than 6.0)'
        item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']='6.0','6.0','6.0','6.0','6.0'
        item['toefl'],item['toefl_desc']='79','79 (Internet-based)'

        alls=response.xpath('//div[@id="cal-content"]/*').extract()
        # print(alls)
        if '<h2>Program Outline</h2>' not in alls:
            print(response.url)


        #副学位课程
        #item['degree_level']=3
        # item['entry_requirements_en']="<h1>Associate of Arts Degree</h1><a></a><h2>Admission Requirements</h2><p><span>Regular Applicants:</span> A regular applicant will be a secondary graduate or a secondary school student, or its equivalent, who has or who will complete the requirements for senior secondary graduation, or its equivalent, not less than one month prior to commencement of classes for the semester to which admission is sought&nbsp;- either fall or winter. The following minimum entrance requirements will apply to regular applicants: </p><ul><li><p>B.C. secondary graduation, or equivalent. </p></li><li><p>English 12 with minimum 60% or <a>alternatives</a>. </p></li></ul><p>Students with a passing grade of less than 60% in English 12, English 12 First Peoples or TPC 12 will be admissible to the first year of the Associate of Arts Degree, subject to the following conditions: </p><ol><li><p>Registration is restricted to courses for which the student satisfies the prerequisites. Registration in first-year English courses is, therefore, prohibited. </p></li><li><p>Successful completion of the English entrance requirements within the first year of studies. This may be done in one of the following ways: </p><ul><li><p>Successful completion of English 12, English 12 First Peoples or TPC 12 or an equivalent course with a minimum grade of 60%. This may be done concurrently through the College's Adult Basic Education Program or by completing an equivalent course through a distance education program. </p></li><li><p>Writing the LPI and obtaining a score of at least 24/40 (level 4). </p></li></ul></li></ol><p><span>Mature Applicants: </span>A mature applicant will be at least 19 years of age and will not have attended secondary school on a full-time basis for a minimum period of one year. </p><p>Secondary graduation is waived for mature applicants. The English entrance requirements, as stated above, must be satisfied prior to admission. Admission may be granted on the condition that the entrance requirements will be completed prior to the commencement of classes for the semester to which admission is sought&nbsp;- either fall or winter. </p><p><span>Transfer Students:</span> Students who transfer to Okanagan College may be eligible for transfer credits towards an Okanagan College Associate of Arts degree, Associate of Science degree or a General Studies diploma for work successfully completed at another recognized institution. </p>"
        # item['overview_en']='<p>The Associate of Arts Degree is granted upon completion of 60 credits of prescribed study (below). Students with an Associate of Arts Degree if admitted to BC universities are guaranteed full transfer credit (60 credits) for the work done for their Associate Degree.</p><p>In two B.C. universities (SFU and UNBC), students with an Associate of Arts Degree will be offered priority admission to the Faculty of Arts (subject to a minimum GPA determined by the university)</p><p>Courses used to complete the Okanagan College Associate of Arts Degree must also have transfer credit to one other BC university (Simon Fraser University, University of British Columbia, University of Northern British Columbia, University of Victoria).</p><p>No course may be used to meet more than one of the specific requirements.</p><p>The Associate of Arts Degree is granted upon completion of the following course requirements with a minimum grade average of 60% for all courses counting towards the degree.</p>'
        # item['tuition_fee']='27,500'
        # item['department']='University Studies Arts at Okanagan College'
        # item['degree_name']='Associate of Arts Degree'
        # majorname=response.xpath('//h2[contains(text(),"Communications Emphasis")]/preceding-sibling::a[1]/following-sibling::h2/text()').extract()
        # for ma in majorname:
        #     item['major_name_en']=ma
        #     modulesxpath = '//h2[text()="%s"]/following-sibling::div[1]'% ma
        #     item['modules_en']=remove_class(response.xpath(modulesxpath).extract())
        #     for cam,sd in zip(['Vernon','Penticton','Salmon Arm','Kelowna '],['2019-01,2019-09','2019-01,2019-09','2019-01,2019-09','2019-01,2019-05,2019-07,2019-09']):
        #         item['campus']=cam
        #         item['start_date']=sd
        #         yield item