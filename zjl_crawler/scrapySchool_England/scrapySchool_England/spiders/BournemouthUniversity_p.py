# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/2 9:46'
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
class BournemouthUniversitySpider(scrapy.Spider):
    name = 'BournemouthUniversity_p'
    allowed_domains = ['bournemouth.ac.uk/']
    start_urls = []
    C= [
        'https://www1.bournemouth.ac.uk/study/courses/msc-clinical-developmental-neuropsychology',
        'https://www1.bournemouth.ac.uk/study/courses/ma-creative-media-arts-data-innovation',
        'https://www1.bournemouth.ac.uk/study/courses/msc-forensic-neuropsychological-perspectives-face-processing',
        'https://www1.bournemouth.ac.uk/study/courses/ma-multimedia-journalism',
        'https://www1.bournemouth.ac.uk/study/courses/mres-sociology',
        'https://www1.bournemouth.ac.uk/study/courses/ma-media-communication',
        'https://www1.bournemouth.ac.uk/study/courses/msc-finance',
        'https://www1.bournemouth.ac.uk/study/courses/mres-computing-creative-technology-design-engineering',
        'https://www1.bournemouth.ac.uk/study/courses/mres-department-archaeology-anthropology-forensic-sciences-life-environmental-sciences',
        'https://www1.bournemouth.ac.uk/study/courses/msc-tourism-marketing-management',
        'https://www1.bournemouth.ac.uk/study/courses/ma-social-work',
        'https://www1.bournemouth.ac.uk/study/courses/msc-internet-things',
        'https://www1.bournemouth.ac.uk/study/courses/ma-political-psychology',
        'https://www1.bournemouth.ac.uk/study/courses/msc-internet-things-data-analytics',
        'https://www1.bournemouth.ac.uk/study/courses/msc-international-risk-management-finance-1',
        'https://www1.bournemouth.ac.uk/study/courses/msc-international-accounting-finance',
        'https://www1.bournemouth.ac.uk/study/courses/msc-public-health',
        'https://www1.bournemouth.ac.uk/study/courses/msc-events-marketing',
        'https://www1.bournemouth.ac.uk/study/courses/msc-international-hospitality-tourism-management',
        'https://www1.bournemouth.ac.uk/study/courses/msc-hotel-food-services-management',
        'https://www1.bournemouth.ac.uk/study/courses/msc-events-management',
        'https://www1.bournemouth.ac.uk/study/courses/msc-retail-management-marketing',
        'https://www1.bournemouth.ac.uk/study/courses/msc-product-design',
        'https://www1.bournemouth.ac.uk/study/courses/msc-mechanical-engineering-design',
        'https://www1.bournemouth.ac.uk/study/courses/msc-engineering-project-management',
        'https://www1.bournemouth.ac.uk/study/courses/ma-industrial-design',
        'https://www1.bournemouth.ac.uk/study/courses/msc-disaster-management-1',
        'https://www1.bournemouth.ac.uk/study/courses/msc-biological-anthropology',
        'https://www1.bournemouth.ac.uk/study/courses/msc-forensic-anthropology',
        'https://www1.bournemouth.ac.uk/study/courses/ma-sound-design-film-television',
        'https://www1.bournemouth.ac.uk/study/courses/ma-post-production-editing',
        'https://www1.bournemouth.ac.uk/study/courses/ma-social-care',
        'https://www1.bournemouth.ac.uk/study/courses/mres-psychology',
        'https://www1.bournemouth.ac.uk/study/courses/msc-sport-management',
        'https://www1.bournemouth.ac.uk/study/courses/llm-international-commercial-law',
        'https://www1.bournemouth.ac.uk/study/courses/llm-intellectual-property',
        'https://www1.bournemouth.ac.uk/study/courses/llm-legal-practice',
        'https://www1.bournemouth.ac.uk/study/courses/msc-hypnosis-research-medicine-clinical-practice',
        'https://www1.bournemouth.ac.uk/study/courses/llm-public-international-law',
        'https://www1.bournemouth.ac.uk/study/courses/llm-international-tax-law',
        'https://www1.bournemouth.ac.uk/study/courses/msc-applied-data-analytics',
        'https://www1.bournemouth.ac.uk/study/courses/ma-creative-writing-publishing',
        'https://www1.bournemouth.ac.uk/study/courses/msc-tourism-management',
        'https://www1.bournemouth.ac.uk/study/courses/msc-internet-things-cyber-security',
        'https://www1.bournemouth.ac.uk/study/courses/msc-cyber-security-human-factors',
        'https://www1.bournemouth.ac.uk/study/courses/msc-management-human-resources',
        'https://www1.bournemouth.ac.uk/study/courses/msc-international-investment-finance',
        'https://www1.bournemouth.ac.uk/study/courses/msc-international-economics-finance-1',
        'https://www1.bournemouth.ac.uk/study/courses/master-business-administration',
        'https://www1.bournemouth.ac.uk/study/courses/legal-practice-course-0',
        'https://www1.bournemouth.ac.uk/study/courses/msc-international-taxation-finance',
        'https://www1.bournemouth.ac.uk/study/courses/msc-innovation-management-entrepreneurship-0',
        'https://www1.bournemouth.ac.uk/study/courses/msc-international-management',
        'https://www1.bournemouth.ac.uk/study/courses/msc-management-project-management',
        'https://www1.bournemouth.ac.uk/study/courses/msc-international-finance',
        'https://www1.bournemouth.ac.uk/study/courses/msc-marketing-management',
        'https://www1.bournemouth.ac.uk/study/courses/ma-literary-media',
        'https://www1.bournemouth.ac.uk/study/courses/msc-nutrition-behaviour',
        'https://www1.bournemouth.ac.uk/study/courses/ma-digital-effects',
        'https://www1.bournemouth.ac.uk/study/courses/ma-radio-production',
        'https://www1.bournemouth.ac.uk/study/courses/msc-computer-animation-visual-effects',
        'https://www1.bournemouth.ac.uk/study/courses/ma-international-political-communication',
        'https://www1.bournemouth.ac.uk/study/courses/ma-3d-computer-animation',
        'https://www1.bournemouth.ac.uk/study/courses/msc-information-technology',
        'https://www1.bournemouth.ac.uk/study/courses/ma-corporate-communication',
        'https://www1.bournemouth.ac.uk/study/courses/msc-investigative-forensic-psychology',
        'https://www1.bournemouth.ac.uk/study/courses/msc-forensic-archaeology',
        'https://www1.bournemouth.ac.uk/study/courses/ma-directing-film-television',
        'https://www1.bournemouth.ac.uk/study/courses/ma-scriptwriting',
        'https://www1.bournemouth.ac.uk/study/courses/ma-advertising',
        'https://www1.bournemouth.ac.uk/study/courses/ma-cinematography-film-television',
        'https://www1.bournemouth.ac.uk/study/courses/ma-producing-film-television',
        'https://www1.bournemouth.ac.uk/study/courses/msc-biodiversity-conservation',
        'https://www1.bournemouth.ac.uk/study/courses/msc-foundations-clinical-psychology',
        'https://www1.bournemouth.ac.uk/study/courses/msc-clinical-research'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)
        #1.university
        university = 'Bournemouth University'
        # print(university)

        #2.location
        location = response.xpath("//*[contains(text(),'Location:')]//following-sibling::p").extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #3.programme_en 4.degree_name
        programme_en = response.xpath('/html/body/div/section//h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        try:
            degree_name = programme_en.split()[0]
        except:
            degree_name = ''
        if '-' in programme_en :
            programme_en = programme_en.replace('-','')
        programme_en =programme_en.replace(degree_name,'')
        programme_en = clear_space_str(programme_en)
        if '–' in programme_en:
            programme_en = programme_en.replace('–', '').strip()
        programme_en = programme_en.replace('&amp;','')
        # print('programme_en:',programme_en)
        # print('degree_name:',degree_name)

        # 5.degree_type
        degree_type = 2

        #6.teach_time
        teach_time = response.xpath("//*[contains(text(),'Delivery:')]//following-sibling::*").extract()
        teach_time = ''.join(teach_time)
        teach_time = remove_tags(teach_time)
        if 'Full time' in teach_time:
            teach_time = 'Full time'
        else:
            teach_time = 'Part time'
        # print(teach_time)

        #7.duration #8.duration_per
        duration = response.xpath("//*[contains(text(),'Duration:')]//following-sibling::p").extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        # print(duration)
        if '1 year' in duration:
            duration = 1
            duration_per = 1
        elif '12-18 months' in duration:
            duration = 12
            duration_per = 3
        elif '36 months' in duration:
            duration = 36
            duration_per = 3
        elif '1 to 2 years' in duration:
            duration = 1
            duration_per = 1
        elif '2 years' in duration:
            duration = 2
            duration_per = 1
        elif '3-5 years' in duration:
            duration = 3
            duration_per = 1
        elif '48 months' in duration:
            duration = 48
            duration_per = 3
        elif '18-36 months' in duration:
            duration = 18
            duration_per = 3
        elif '12 months' in duration:
            duration = 12
            duration_per = 3
        elif '5 years' in duration:
            duration = 5
            duration_per = 1
        elif '3 years' in duration:
            duration = 3
            duration_per = 1
        elif '14 months' in duration:
            duration = 14
            duration_per = 3
        elif '15 months' in duration:
            duration = 15
            duration_per = 3
        elif '18-24 months' in duration:
            duration = 18
            duration_per = 3
        elif '27 months' in duration:
            duration = 27
            duration_per = 3
        elif '8 months' in duration:
            duration = 8
            duration_per = 3
        elif 'Nine months' in duration:
            duration = 9
            duration_per = 3
        else:
            duration_per = 1
            duration = 1
        # print('duration_per:',duration_per)
        # print('duration:',duration)

        #9.overview_en
        overview_en = response.xpath('//*[@id="main-content"]/div/section[2]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #10.teach_time
        teach_time = 'full time'

        #11.modules_en
        modules_en = response.xpath("//section[@id='course-details']//div[@id='accordion-1']").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        modules_en =clear_space_str(modules_en)
        # print(modules_en)

        #12.start_date
        start_date= response.xpath("//*[contains(text(),'Next start date:')]//following-sibling::p").extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        start_date = clear_space_str(start_date)
        start_date = tracslateDate(start_date)
        start_date = ','.join(start_date)
        # print(start_date)


        #13.rntry_requirements
        rntry_requirements = response.xpath("//*[contains(text(),'Entry requirements')]/../following-sibling::div[1]").extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements =remove_class(rntry_requirements)
        rntry_requirements = clear_space_str(rntry_requirements)
        # print(rntry_requirements,'******************************************************************************')

        #14.ielts 15.16.17.18
        ielts_list = re.findall('\d\.\d',rntry_requirements)
        # print(ielts_list)
        if len(ielts_list) ==4:
            ielts=ielts_list[2]
            ielts_l = ielts_list[3]
            ielts_s = ielts_list[3]
            ielts_r = ielts_list[3]
            ielts_w = ielts_list[3]
        elif len(ielts_list) ==3:
            ielts = ielts_list[1]
            ielts_l = ielts_list[2]
            ielts_s = ielts_list[2]
            ielts_r = ielts_list[2]
            ielts_w = ielts_list[2]
        elif len(ielts_list) ==2:
            ielts = ielts_list[0]
            ielts_l = ielts_list[1]
            ielts_s = ielts_list[1]
            ielts_r = ielts_list[1]
            ielts_w = ielts_list[1]
        elif len(ielts_list) ==1:
            ielts = ielts_list[0]
            ielts_l = ielts_list[0]
            ielts_s = ielts_list[0]
            ielts_r = ielts_list[0]
            ielts_w = ielts_list[0]
        else :
            ielts = None
            ielts_l = None
            ielts_s = None
            ielts_r = None
            ielts_w = None
        # print(ielts,ielts_l,ielts_r,ielts_w,ielts_s)

        #19.career_en
        career_en = response.xpath("//*[contains(text(),'Careers')]/../following-sibling::*|//*[contains(text(),'Careers')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        career_en =clear_space_str(career_en)
        # print(career_en)

        #20.tuition_fee,#21.tuition_fee_pre
        tuition_fee_list = response.xpath('//*[@id="fees-box"]/div/div/span|//*[@id="fees-box"]/div[2]/div[2]/p[2]|//*[@id="fees-box"]/div/div[2]/ul/li[1]').extract()
        tuition_fee_list = ''.join(tuition_fee_list)
        #
        # if len(tuition_fee) == 0:
        #     tuition_fee = response.xpath('//*[@id="fees-box"]/div/div[1]/span[1]').extract()
        # tuition_fee = ''.join(tuition_fee)
        # tuition_fee = remove_tags(tuition_fee)
        # tuition_fee = tuition_fee.replace(',','')
        # tuition_fee = tuition_fee.replace('£','')
        # print(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee_list)
        # print(tuition_fee)
        tuition_fee_pre = '£'

        #22.url
        url = response.url
        # print(url)

        #23.application_open_date
        application_open_date = '2018-7-18'
        #24.apply_pre
        apply_pre = '£'

        #25.apply_fee
        apply_fee = 0
        #26.apply_proces_en
        apply_proces_en = '<p>Step 1: Application Complete all sections of your country’s application form. Step 2: Terms and conditions You must read, understand and agree to be bound by the terms and conditions before moving on to the next step. Step 3: Confirmation Sign the application form to confirm you have provided correct details and you agree to the terms and conditions. Step 4: Other documents Scan, attach and send in your additional documents to the email address on the application form: Academic transcripts and exam results English test score if required If you do not have academic transcripts or English test results, you can still apply and we can make you a conditional offer, the conditions of which you will need to satisfy before we confirm your place. Step 5: Assessment We’ll contact you to arrange one or more of the following if required: English language test Mathematics test Interview This will allow us to further assess your suitability for the program. Step 6: Admission decision Receive an admission decision and, if your application is successful, accompanying offer letter. Step 7: Deposit Accept your offer by paying the deposit. Step 8: Pre-arrival Receive confirmation of program acceptance, pre-arrival information, plus guidance on finding local accommodation if you are coming from outside the USPP host city to study. For conditional offers, these items are issued once we receive proof that the conditions of the offer have been met. Step 9: Travel Arrange travel to USPP location if applicable.Arrive at your USPP center for orientation before classes begin. Step 10: Begin your USPP program USPP teaching begins. View the program timeline for next steps.</p>'
        #27.require_chinese_en

        require_chinese_en = "<p>This is a guide to the normal entry requirements, assuming you’ve followed the Chinese education system. An admissions tutor will study your application, so make sure you include your academic background and personal information when you apply.Entry requirements vary depending on what sort of course you’re coming to BU to study. BU International College Foundation Certificates You can undertake a Foundation Certificate before going on to an undergraduate course if you’ve completed 11 years of schooling or Senior High School Year 2 in China and have a minimum of IELTS (Academic) 5.0. Undergraduate courses You can apply to study a Bachelor's degree from year one if you hold a Chinese Senior High School Diploma plus successful completion of a relevant first-year undergraduate programme in a recognised Chinese university, or a Diploma from Specialized College (zhongzhuan). Chinese Senior High School certificate of graduation with overall HuiKao result grade B average,  transcripts of 3 years with 85% average (85% also eligible for AES). Top-up courses You need to hold a College Graduation Diploma (Dazhuan awarded by a university/college on completion of two to three years of study), or a BTEC Higher National Diploma or Foundation degree in a relevant subject.Postgraduate courses ​You need to have a Bachelor's (Honours) degree from a recognised Chinese university, normally from a four-year undergraduate programme, or a Bachelors degree from Higher Education Self-Study Examinations, or a Top-up degree or university-recognised Pre-Master’s Foundation programme. Grade requirements from Chinese Bachelor's degree holders are as below: Applicants from 985 or 211 universities Media studies and other subjects equivalent to UK 2:1 degree	65% +	GPA 2.25 + Business and subjects equivalent to UK 2:2 degree	60% +	GPA 2.0 + Academic Excellence Scholarship (automatic award of £3500)	75% +	GPA 2.75 + Applicants from other universities Media studies and other subjects equivalent to UK 2:1 degree	70% +	GPA 2.5 + Business and subjects equivalent to UK 2:2 degree	65% +	GPA 2.25 + Academic Excellence Scholarship (automatic award of £3500)	80% +	GPA 3.0 + Research programmes You need a good postgraduate degree to be considered for a BU research programme. Please see more detail on the postgraduate research page.You can find more information about English language requirements for entry to BU on our English language requirements page. Full information about preparatory courses is available on the Bournemouth University International College website.If you need help with your visa or want more information about the immigration process, you can find it on our immigration information page.</p>"

        item['require_chinese_en'] = require_chinese_en
        item['apply_proces_en'] = apply_proces_en
        item['apply_fee'] = apply_fee
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['location'] = location
        item['programme_en'] = programme_en
        item['degree_name'] = degree_name
        item['degree_type'] = degree_type
        item['teach_time'] = teach_time
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['overview_en'] = overview_en
        item['teach_time'] = teach_time
        item['modules_en'] = modules_en
        item['start_date'] = start_date
        item['rntry_requirements'] = rntry_requirements
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['url'] = url
        item['application_open_date'] = application_open_date
        yield  item

