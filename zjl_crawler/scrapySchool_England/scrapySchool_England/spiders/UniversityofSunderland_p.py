# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/16 16:38'
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
from scrapySchool_England.TranslateMonth import translate_month
class UniversityofSunderlandSpider(scrapy.Spider):
    name = 'UniversityofSunderland_p'
    allowed_domains = ['sunderland.ac.uk/']
    start_urls = []
    C= [
        'https://www.sunderland.ac.uk/study/performing-arts/advanced-professional-practice-dance/',
        'https://www.sunderland.ac.uk/study/business-and-management/postgraduate-digital-marketing-data-analytics/',
        'https://www.sunderland.ac.uk/study/business-and-management/mba-supply-chain-sc/',
        'https://www.sunderland.ac.uk/study/pharmacy-pharmaceutical-and-cosmetic-sciences/msc-clinical-pharmacy-sc/',
        'https://www.sunderland.ac.uk/study/business-and-management/mba-hospitality-management-sc/',
        'https://www.sunderland.ac.uk/study/engineering/postgraduate-engineering-management-sc-pt/',
        'https://www.sunderland.ac.uk/study/business-and-management/postgraduate-human-resource-management/',
        'https://www.sunderland.ac.uk/study/creative-arts/postgraduate-glass-and-ceramics/',
        'https://www.sunderland.ac.uk/study/pharmacy-pharmaceutical-and-cosmetic-sciences/ospap-overseas-pharmacist/',
        'https://www.sunderland.ac.uk/study/journalism-and-pr/postgraduate-journalism/',
        'https://www.sunderland.ac.uk/study/business-and-management/mba-marketing-sc/',
        'https://www.sunderland.ac.uk/study/engineering/postgraduate-project-management/',
        'https://www.sunderland.ac.uk/study/health-paramedic-clinical-sciences/postgraduate-environment-health-safety/',
        'https://www.sunderland.ac.uk/study/business-and-management/operations-logistics-management/',
        'https://www.sunderland.ac.uk/study/health-paramedic-clinical-sciences/postgraduate-health-safety-wellbeing/',
        'https://www.sunderland.ac.uk/study/business-and-management/mba-hospitality-management/',
        'https://www.sunderland.ac.uk/study/tourism-hospitality-and-events/postgraduate-tourism-hospitality-study-centres/',
        'https://www.sunderland.ac.uk/study/pharmacy-pharmaceutical-and-cosmetic-sciences/msc-drug-discovery-development/',
        'https://www.sunderland.ac.uk/study/business-and-management/postgraduate-global-business-general-mgt-da-sc/',
        'https://www.sunderland.ac.uk/study/pharmacy-pharmaceutical-and-cosmetic-sciences/msc-pharmaceutical-biopharmaceutical-formulations/',
        'https://www.sunderland.ac.uk/study/business-and-management/ma-mbm-msc-extended/',
        'https://www.sunderland.ac.uk/study/business-and-management/postgraduate-mba-sc/',
        'https://www.sunderland.ac.uk/study/business-and-management/postgraduate-marketing/',
        'https://www.sunderland.ac.uk/study/law/postgraduate-legal-practice/',
        'https://www.sunderland.ac.uk/study/education/postgraduate-education/',
        'https://www.sunderland.ac.uk/study/psychology/postgraduate-psychological-research/',
        'https://www.sunderland.ac.uk/study/psychology/postgraduate-psychology/',
        'https://www.sunderland.ac.uk/study/media/postgraduate-radio/',
        'https://www.sunderland.ac.uk/study/business-and-management/mba-marketing/',
        'https://www.sunderland.ac.uk/study/business-and-management/mba-finance/',
        'https://www.sunderland.ac.uk/study/law/postgraduate-criminal-law-procedure/',
        'https://www.sunderland.ac.uk/study/law/postgraduate-law/',
        'https://www.sunderland.ac.uk/study/nursing/postgraduate-nursing/',
        'https://www.sunderland.ac.uk/study/social-sciences/postgraduate-social-work/',
        'https://www.sunderland.ac.uk/study/languages/postgraduate-tesol/',
        'https://www.sunderland.ac.uk/study/media/postgraduate-media-production/',
        'https://www.sunderland.ac.uk/study/computing/postgraduate-computing-sc/',
        'https://www.sunderland.ac.uk/study/law/postgraduate-commercial-law-trade/',
        'https://www.sunderland.ac.uk/study/english/postgraduate-english-studies/',
        'https://www.sunderland.ac.uk/study/business-and-management/postgraduate-finance-management/',
        'https://www.sunderland.ac.uk/study/law/postgraduate-international-law/',
        'https://www.sunderland.ac.uk/study/computing/postgraduate-cybersecurity/',
        'https://www.sunderland.ac.uk/study/creative-arts/postgraduate-fine-art/',
        'https://www.sunderland.ac.uk/study/media/postgraduate-film-cultural-studies/',
        'https://www.sunderland.ac.uk/study/computing/postgraduate-data-science/',
        'https://www.sunderland.ac.uk/study/media/postgraduate-media-cultural-studies/',
        'https://www.sunderland.ac.uk/study/law/postgraduate-international-human-rights/',
        'https://www.sunderland.ac.uk/study/health-paramedic-clinical-sciences/postgraduate-public-health/',
        'https://www.sunderland.ac.uk/study/engineering/postgraduate-manufacturing-engineering/',
        'https://www.sunderland.ac.uk/study/business-and-management/international-business-management/',
        'https://www.sunderland.ac.uk/study/business-and-management/mba-enterprise-innovation/',
        'https://www.sunderland.ac.uk/study/business-and-management/integrated-marketing-communications/',
        'https://www.sunderland.ac.uk/study/social-sciences/postgraduate-practice-development/',
        'https://www.sunderland.ac.uk/study/engineering/postgraduate-maintenance-engineering/',
        'https://www.sunderland.ac.uk/study/business-and-management/mba-hr-management/',
        'https://www.sunderland.ac.uk/study/computing/postgraduate-computing/',
        'https://www.sunderland.ac.uk/study/business-and-management/mba-business-administration/',
        'https://www.sunderland.ac.uk/study/business-and-management/mba-finance-sc/',
        'https://www.sunderland.ac.uk/study/design/postgraduate-design/',
        'https://www.sunderland.ac.uk/study/history/postgraduate-historical-research/',
        'https://www.sunderland.ac.uk/study/computing/business-technology-management/',
        'https://www.sunderland.ac.uk/study/business-and-management/mba-cybersecurity/',
        'https://www.sunderland.ac.uk/study/computing/postgraduate-it-management-sc/',
        'https://www.sunderland.ac.uk/study/journalism-and-pr/postgraduate-magazine-journalism/',
        'https://www.sunderland.ac.uk/study/creative-arts/participatory-arts-media/',
        'https://www.sunderland.ac.uk/study/engineering/postgraduate-project-management-study-centre/',
        'https://www.sunderland.ac.uk/study/business-and-management/mba-hrm-sc/',
        'https://www.sunderland.ac.uk/study/business-and-management/mba-creative-cultural-industries/',
        'https://www.sunderland.ac.uk/study/business-and-management/mba-supply-chain/',
        'https://www.sunderland.ac.uk/study/sport-and-exercise-sciences/postgraduate-sport-exercise-science/',
        'https://www.sunderland.ac.uk/study/creative-arts/postgraduate-photography/',
        'https://www.sunderland.ac.uk/study/tourism-hospitality-and-events/cid916-msc-tourism-and-events/',
        'https://www.sunderland.ac.uk/study/engineering/postgraduate-electronic-engineering/',
        'https://www.sunderland.ac.uk/study/tourism-hospitality-and-events/postgraduate-tourism-hospitality/',
        'https://www.sunderland.ac.uk/study/journalism-and-pr/postgraduate-public-relations/',
        'https://www.sunderland.ac.uk/study/engineering/postgraduate-mechanical-engineering/',
        'https://www.sunderland.ac.uk/study/engineering/postgraduate-engineering-management/',
        'https://www.sunderland.ac.uk/study/journalism-and-pr/postgraduate-sports-journalism/',
        'https://www.sunderland.ac.uk/study/engineering/postgraduate-telecommunications-engineering-sc/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Sunderland'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.degree_type
        degree_type = 2

        #4.degree_name
        degree_name = response.xpath('/html/body/div[2]/header/div/div[1]/h1/span[1]').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #5.programme_en
        programme_en = response.xpath('/html/body/div[2]/header/div/div[1]/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en).replace(degree_name,'')
        programme_en = clear_space_str(programme_en)
        # print(programme_en)

        #6.duration #7.duration_per
        duration_list = response.xpath("//*[contains(text(),'year')]//*|//*[contains(text(),'months')]//*|//*[contains(text(),'weeks')]//*").extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        try:
            duration = re.findall('\d+',duration_list)[0]
        except:
            duration = 1
        if int(duration) ==8:
            duration_per = 4
        elif int(duration) >18:
            duration_per = 4
        elif int(duration)>5:
            duration_per = 3
        else:
            duration_per=1
        # print(duration,'*(*&*(&(*',duration_per)

        # 8.start_date
        start_date_list = response.xpath("//*[contains(text(),'Next start date')]//*").extract()
        start_date_list = ''.join(start_date_list)
        start_date_list = remove_tags(start_date_list)
        # start_date = tracslateDate(start_date)
        try:
            start_date = re.findall('\d+',start_date_list)[0]
        except:
            start_date = ''
        if 'Oct' in start_date_list:
            start_date = '2018-10-'+str(start_date)
        elif 'Aug' in start_date_list:
            start_date = '2018-8-'+str(start_date)
        elif 'Sep' in start_date_list:
            start_date = '2018-9-' + str(start_date)
        elif 'Jan' in start_date_list:
            start_date = '2018-11-'+ str(start_date)
        elif 'Nov' in start_date_list:
            start_date = '2019-1-' + str(start_date)
        else:
            start_date = ''
        # print(start_date_list,start_date)

        #9.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),' International fee')]//*|//*[contains(text(),'Tuition fee')]//*").extract()
        tuition_fee =''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        if ',' in tuition_fee:
            tuition_fee = getTuition_fee(tuition_fee)
        else:
            try:tuition_fee = re.findall('\d+',tuition_fee)[0]
            except:tuition_fee = None
        # print(tuition_fee)

        #10.teach_time
        teach_time = response.xpath("//*[contains(text(),'time')]//*").extract()
        teach_time = ''.join(teach_time)
        teach_time = remove_tags(teach_time)
        if 'Full' in teach_time:
            teach_time = 'Full-Time'
            # print(url)
        else:
            teach_time = 'Part-Time'
        # print(teach_time)

        #11.tuition_fee_pre
        tuition_fee_pre = '£'

        #12.overview_en
        overview_en = response.xpath("//*[contains(text(),'Overview')]//following-sibling::p").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #13.modules_en
        modules_en = response.xpath('//*[@id="course-years"]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #14.rntry_requirements
        rntry_requirements = response.xpath("//*[contains(text(),'Entry requirements')]//following-sibling::*").extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #15.ielts 16171819
        ielts_list = re.findall('\d\.\d',rntry_requirements)
        # print(ielts_list)
        if len(ielts_list) == 5:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_l = 6.0
            ielts_s = 6.0
        elif  len(ielts_list) ==3:
            a = ielts_list[0]
            b = ielts_list[1]
            c = ielts_list[2]
            ielts = a
            ielts_w = b
            ielts_r = c
            ielts_l = c
            ielts_s = c
        elif len(ielts_list) ==2:
            a = ielts_list[0]
            b = ielts_list[1]
            ielts = a
            ielts_w = b
            ielts_r = b
            ielts_l = b
            ielts_s = b
        elif len(ielts_list) ==1:
            a = ielts_list[0]
            ielts = a
            ielts_w = float(a)-0.5
            ielts_r = float(a)-0.5
            ielts_l = float(a)-0.5
            ielts_s = float(a)-0.5
        else:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_l = 6.0
            ielts_s = 6.0
        # print(ielts,ielts_r,ielts_s,ielts_l,ielts_w)

        #20.career_en
        career_en = response.xpath("//*[contains(text(),'Employment')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)
        #21.apply_pre
        apply_pre = '£'
        #22.apply_proces_en
        apply_proces_en = '<p>When you are ready to make your application, there are six ways of applying. Choose the option which is the most convenient for you: Option 1: The Universitys overseas offices If you would like to apply to a course, you can contact one of our overseas offices to start the application process.Our overseas offices are able to answer any questions you may have about studying in the United Kingdom. Contact one of our offices in China, Malaysia, India, Vietnam or Greece to begin your application.Option 2: UCAS – undergraduate onlyInternational and UK students apply for undergraduate courses in the same way – through the Universities and Colleges Admissions Service (UCAS) website.The UCAS institution code for the University is S84.Option 3: Apply online – postgraduate only To study at postgraduate level, you need to apply to the University of Sunderland directly.Find the postgraduate course you’re interested in, and on the course page you will see a link to either apply online or download an application form (.pdf).Option 4: Email your application directly To apply for undergraduate and postgraduate courses at the main University of Sunderland campuses, email your completed application form (.pdf) to Studentadmin@sunderland.ac.uk. To apply for undergraduate and postgraduate courses at the University of Sunderland in London, email your completed application form (.pdf) to admissions-london@sunderland.ac.uk. Option 5: In-country representatives If you live outside the UK, make your application by finding the most convenient contact from our in-country representatives.Once you have completed and submitted your application, you will be given a unique Personal ID number so you can be kept up-to-date with any developments in your application process. Option 6: Apply through a study centre To study with us in your country, through one of the University of Sunderlands study centres, you must apply directly through the relevant study centre. Visit the Other ways to study with us page to discover where you can study.</p>'

        item['apply_proces_en'] = apply_proces_en
        item['university'] = university
        item['url'] = url
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['programme_en'] = programme_en
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['start_date'] = start_date
        item['tuition_fee'] = tuition_fee
        item['teach_time'] = teach_time
        item['tuition_fee_pre'] = tuition_fee_pre
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['rntry_requirements'] = rntry_requirements
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['career_en'] = career_en
        yield item