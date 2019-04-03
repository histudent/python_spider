# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.middlewares import clear_duration,tracslateDate
from scrapySchool_England.clearSpace import clear_lianxu_space,clear_same_s

class QueenmargaretuniversityPSpider(scrapy.Spider):
    name = 'QueenMargaretUniversity_P'
    allowed_domains = ['qmu.ac.uk']
    start_urls = []
    pro_url=["/study-here/postgraduate-study/2018-postgraduate-courses/msc-advancing-physiotherapy-practice-programme/",
"/study-here/postgraduate-study/2018-postgraduate-courses/pgcert-applied-social-development/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-art-psychotherapy-international/",
"/study-here/postgraduate-study/2018-postgraduate-courses/pgcert-arts-management/",
"/study-here/postgraduate-study/2018-postgraduate-courses/ma-arts-festival-and-cultural-management/",
"/study-here/postgraduate-study/2018-postgraduate-courses/pgdip-msc-audiology-pre-registration/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-pgdip-bsl-english-interpreting-post-registration/",
"/study-here/postgraduate-study/2018-postgraduate-courses/chartered-institute-of-public-relations-professional-public-relations-diploma/",
"/study-here/postgraduate-study/2018-postgraduate-courses/chartered-institute-of-public-relations-specialist-diploma-internal-communication/",
"/study-here/postgraduate-study/2018-postgraduate-courses/chartered-institute-of-public-relations-specialist-diploma-public-affairs/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-cognitive-behavioural-therapy/",
"/study-here/postgraduate-study/2018-postgraduate-courses/pgcert-collaborative-working-education-and-therapy/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-diabetes/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-diagnostic-radiography-pre-registration/",
"/study-here/postgraduate-study/2018-postgraduate-courses/pgdip-msc-dietetics/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-digital-campaigning-and-content-creationstar/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-pgdip-pgcert-dispute-resolution/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-gastronomy/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-global-health/",
"/study-here/postgraduate-study/2018-postgraduate-courses/pgcert-health-in-fragile-and-conflict-affected-states/",
"/study-here/postgraduate-study/2018-postgraduate-courses/home-economics-professional-graduate-diploma-in-secondary-education/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-international-health-trop-ed/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-international-management-and-leadership/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-international-management-and-leadership-with-events/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-international-management-and-leadership-with-family-and-smaller-enterprises/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-international-management-and-leadership-with-hospitality/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-international-management-and-leadership-with-tourism/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-mammography/",
"/study-here/postgraduate-research-study/2018-postgraduate-research-courses/master-of-clinical-research/",
"/study-here/postgraduate-research-study/2018-postgraduate-research-courses/master-of-research/",
"/study-here/postgraduate-study/2018-postgraduate-courses/mba-in-business-management-and-enterprise/",
"/study-here/postgraduate-study/2018-postgraduate-courses/mba-family-and-smaller-enterprises/",
"/study-here/postgraduate-study/2018-postgraduate-courses/mba-hospitality/",
"/study-here/postgraduate-study/2018-postgraduate-courses/mba-tourism/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-media-management/",
"/study-here/postgraduate-study/2018-postgraduate-courses/medical-imaging/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-musculoskeletal-medicine/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-music-therapy/",
"/study-here/postgraduate-study/2018-postgraduate-courses/pgdip-msc-occupational-therapy-post-registration/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-occupational-therapy-pre-registration/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-pgdip-pgcert-person-centred-practice/",
"/study-here/postgraduate-study/2018-postgraduate-courses/pgdip-person-centred-practice-district-nursing/",
"/study-here/postgraduate-study/2018-postgraduate-courses/pgdip-person-centred-practice-health-visiting/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-pgdip-pgcert-person-centred-practice-mental-health-and-wellbeing/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-pgdip-person-centred-practice-palliative-care/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-pgdip-person-centred-practice-public-health-and-wellbeing/",
"/study-here/postgraduate-study/2018-postgraduate-courses/pgdip-person-centred-practice-school-nursing/",
"/study-here/postgraduate-research-study/2018-postgraduate-research-courses/doctor-of-philosophy-phd/",
"/study-here/postgraduate-study/2018-postgraduate-courses/pgdipmsc-physiotherapy-pre-registration/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-play-therapy/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-podiatrymsc-podiatry-by-distance-e-learning/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-pgdip-e-pgcert-professional-and-higher-education/",
"/study-here/postgraduate-research-study/2018-postgraduate-research-courses/professional-doctorate/",
"/study-here/postgraduate-study/2018-postgraduate-courses/master-of-public-administration-mpa/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-public-health-nutrition/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-public-sociology/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-radiotherapy-post-registration/",
"/study-here/postgraduate-study/2018-postgraduate-courses/pgdipmsc-radiotherapy-and-oncology-pre-registration/",
"/study-here/postgraduate-study/2018-postgraduate-courses/pgdipmsc-rehabilitative-audiology-post-registration/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-sexual-and-reproductive-health/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-social-development-and-health/",
"/study-here/postgraduate-study/2018-postgraduate-courses/pgdip-msc-speech-and-language-therapy-pre-registration/",
"/study-here/postgraduate-study/2018-postgraduate-courses/ma-stage-management/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-strategic-communication-and-public-relations/",
"/study-here/postgraduate-study/2018-postgraduate-courses/msc-theory-of-podiatric-surgery/",]
    for i in pro_url:
        full_url='https://www.qmu.ac.uk'+i
        start_urls.append(full_url)
    def parse(self, response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university'] = 'Queen Margaret University'
        item['url']=response.url
        item['location']='Musselburgh'
        programme=response.xpath('//h1/text()').extract()
        programme=''.join(programme)
        degree_name=re.findall('[A-Z]{2,}[a-z]*',programme)
        degree_name=set(degree_name)
        degree_name='/'.join(degree_name)
        # print(programme)
        # print(degree_name)
        item['programme_en'] = programme
        item['degree_name']=degree_name
        try:
            if degree_name[0] == 'M':
                item['degree_type'] = '2'
            elif degree_name[0] == 'P':
                item['degree_type'] = '3'
        except:
            pass

        item['tuition_fee']='11500'
        item['tuition_fee_pre']='£'

        duration=response.xpath('//div[contains(text(),"Dura")]/following-sibling::div/text()').extract()
        mode=re.findall('(?i)full',''.join(duration))
        if mode!=[]:
            item['teach_time']='1'
        else:
            item['teach_time']='2'
        duration=clear_duration(duration)
        # print(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']

        start_date=response.xpath('//div[contains(text(),"Start")]/following-sibling::div/text()').extract()
        start_date=tracslateDate(start_date)
        start_date=','.join(start_date)
        # print(start_date)
        item['start_date']=start_date

        department=response.xpath('//div[contains(text(),"School")]/following-sibling::div/text()').extract()
        department=''.join(department).strip()
        # print(department)
        item['department']=department

        overview=response.xpath('//div[@class="accordion-item"]/h3[contains(text(),"Course Overview")]/following-sibling::div').extract()
        overview=remove_class(overview)
        item['overview_en']=overview
        # print(overview)

        modules=response.xpath('//h3[contains(text(),"Modules")]/following-sibling::div').extract()
        modules=remove_class(modules)
        # print(modules)
        item['modules_en']=modules

        career=response.xpath('//h3[contains(text(),"Career")]/following-sibling::div').extract()
        career=remove_class(career)
        item['career_en']=career

        rntry=response.xpath('//h3[contains(text(),"ntry")]/following-sibling::div').extract()
        rntry=remove_class(rntry)
        item['rntry_requirements']=rntry

        ielts=response.xpath('//*[contains(text(),"IELTS")]/text()').extract()
        # print(ielts)
        item['ielts_desc']=''.join(ielts)
        ielts=get_ielts(ielts)
        try:
            if ielts!=[] or ielts!={}:
                item['ielts_l']=ielts['IELTS_L']
                item['ielts_s'] = ielts['IELTS_S']
                item['ielts_r'] = ielts['IELTS_R']
                item['ielts_w'] = ielts['IELTS_W']
                item['ielts'] = ielts['IELTS']
        except:
            pass

        deadline=response.xpath('//h3[contains(text(),"Application Deadline")]/following-sibling::div//text()').extract()
        deadline=tracslateDate(deadline)
        deadline=','.join(deadline)
        item['deadline']=deadline

        apply_documents_en=["·A copy of your degree certificate",
"·A copy of your academic transcripts",
"·Two letters of reference (one of which must be academic) and both signed, dated and written on letter headed paper or sent directly from a professional email account.",
"If your documents are in any language other than English then they will need to be accompanied by a formal certified translation into English, by either the awarding institution or a sworn translator.",]
        apply_documents_en='\n'.join(apply_documents_en)
        item['apply_documents_en']=apply_documents_en

        apply_proces_en=["Applying online",
"You will find all our degree programmes listed on our course information pages. To apply for your chosen programme, click on the “Apply for this Course” button which appears top right on each course page.",
"Each programme will list the entry requirements, available awards, study modes and available start dates.",
"Select your programme and preferred start date and begin your application.",
"Application form",
"On our application form please input your basic details. Be careful spelling your email address as this is how we will contact you about your application in future.",
"As part of your application on the form, you will need to write a personal statement specific to the course that you are applying. This is your chance to sell yourself through highlighting your experience, suitability and motivators for wanting to join this course at QMU.",
"You will have the chance to upload supporting documents as part of your application. This is an important part of the admissions process and without seeing supporting documents, tutors will not have enough information to make a decision on your application.",
"The form allows you to save your application should you wish to complete it later.",
"Once complete you can submit your application to us and you will receive an automatic acknowledgement email confirming receipt of your application. You will also receive a QMU applicant ID number which you should keep a note of and quote in any correspondence to QMU.",]
        apply_proces_en='\n'.join(apply_proces_en)
        item['apply_proces_en']=apply_proces_en

        yield item
