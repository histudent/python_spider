# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/24 10:57'
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
    name = 'BournemouthUniversity_u'
    allowed_domains = ['bournemouth.ac.uk/']
    start_urls = []
    C= [

        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-politics-economics-1',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-sociology',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-sociology-anthropology',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-sociology-criminology',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-anthropology',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-business-studies-human-resource-management',
        'https://www1.bournemouth.ac.uk/study/courses/llb-hons-entertainment-law',
        'https://www1.bournemouth.ac.uk/study/courses/llb-hons-law-1',
        'https://www1.bournemouth.ac.uk/study/courses/llb-hons-law',
        'https://www1.bournemouth.ac.uk/study/courses/llb-hons-law-politics',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-english',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-film',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-film-production-cinematography',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-marketing-communications',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-marketing-communications-digital-media',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-marketing-communications-public-relations',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-communication-media',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-media-production',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-photography',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-multimedia-journalism',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-scriptwriting-film-television',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-marketing',
        'https://www1.bournemouth.ac.uk/study/courses/mlit-hons-english',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-music-sound-production-technology',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-archaeology',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-anthropology',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-television-production',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-archaeology-anthropology',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-archaeological-forensic-sciences',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-biological-sciences',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-environmental-science',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-forensic-biology',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-archaeology',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-ecology-wildlife-conservation',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-forensic-investigation',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-forensic-science',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-psychology',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-sport-development-coaching-sciences-0',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-geography',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-sports-management',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-sports-psychology-coaching-sciences',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-sports-therapy-2',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-events-management',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-international-tourism-hospitality-management-0',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-international-hospitality-management',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-tourism-management',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-accounting-business',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-accounting-law',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-economics',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-accounting-taxation',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-accounting-finance',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-finance-business',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-finance-economics',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-politics-economics-1',
        'https://www1.bournemouth.ac.uk/study/courses/maccfin-hons-accounting-finance',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-business-studies-enterprise',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-business-studies',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-business-studies-economics',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-business-studies-finance',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-business-studies-human-resource-management',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-business-studies-marketing',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-events-management',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-business-studies-operations-project-management',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-international-business-studies',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-marketing-communications',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-marketing-communications-advertising',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-data-science-analytics',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-marketing-communications-public-relations',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-marketing',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-computer-animation-art-design',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-computer-animation-technical-arts',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-digital-creative-industries',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-visual-effects',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-games-design',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-games-software-engineering',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-business-information-technology',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-computer-networks',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-computing',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-cyber-security-management',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-forensic-computing-security',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-information-technology-management',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-software-engineering',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-industrial-design',
        'https://www1.bournemouth.ac.uk/study/courses/beng-hons-mechanical-engineering-2',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-product-design',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-design-engineering-3',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-product-design',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-adult-nursing',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-social-work',
        'https://www1.bournemouth.ac.uk/study/courses/mdes-hons-product-design',
        'https://www1.bournemouth.ac.uk/study/courses/meng-hons-mechanical-engineering-0',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-mental-health-nursing',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-childrens-young-peoples-nursing',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-midwifery',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-nutrition',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-occupational-therapy',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-paramedic-science',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-physiotherapy',
        'https://www1.bournemouth.ac.uk/study/courses/bsc-hons-sports-therapy-2',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-history',
        'https://www1.bournemouth.ac.uk/study/courses/ba-hons-politics'
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
        programme_en = programme_en.replace('&amp;','').replace('(Hons)','').strip()
        # print('programme_en:',programme_en)
        # print('degree_name:',degree_name)

        #5.degree_type
        degree_type = 1

        #6.ucascode
        ucascode = response.xpath("//*[contains(text(),'UCAS Code:')]//following-sibling::*").extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode)
        # print(ucascode)

        #7.duration #8.duration_per
        duration_a = response.xpath("//*[contains(text(),'Duration:')]//following-sibling::p").extract()
        duration_a = ''.join(duration_a)
        duration_a = remove_tags(duration_a)
        # print(duration)
        if 'Four years' in duration_a:
            duration = 4
            duration_per = 1
        else:
            duration = re.findall('\d',duration_a)[0]
            duration_per = 1
        # print('duration_per:',duration_per)
        # print('duration:',duration)

        #9.overview_en
        overview_en = response.xpath('//*[@id="main-content"]/div/section[3]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #10.alevel
        try:
            alevel_list = response.xpath("//*[contains(text(),'GCSEs')]//preceding-sibling::p").extract()[1]
            alevel = ''.join(alevel_list)
            alevel = remove_tags(alevel)
        except:
            alevel = 'N/A'
        # print(alevel)

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


        #13.ib
        ib = response.xpath("//*[contains(text(),'International Baccalaureate')]/..").extract()
        ib = ''.join(ib)
        ib = remove_tags(ib)
        if len(ib)>500:
            ib = ib[:500]

        # print(ib)

        #14.ielts 15.16.17.18
        rntry_requirements = response.xpath('//*[@id="entry-requirements"]/div').extract()
        rntry_requirements = ''.join(rntry_requirements)
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
        career_en = response.xpath("//*[contains(text(),'Careers')]//following-sibling::*").extract()
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

        #27.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'How you will be assessed')]//following-sibling::p|//*[@id='accordion-1']/div[6]").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en,url)

        item['assessment_en'] = assessment_en
        item['alevel'] = alevel
        item['ib'] = ib
        item['ucascode'] = ucascode
        item['apply_proces_en'] = apply_proces_en
        item['apply_fee'] = apply_fee
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['location'] = location
        item['programme_en'] = programme_en
        item['degree_name'] = degree_name
        item['degree_type'] = degree_type
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['start_date'] = start_date
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

