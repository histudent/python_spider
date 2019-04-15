# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/8 13:45'
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
    name = 'UniversityofSunderland_u'
    allowed_domains = ['sunderland.ac.uk/']
    start_urls = []
    C= [
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-business-marketing-management/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-business-financial-management/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/integrated-events-management/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-tourism-management/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-tourism-hospitality-management/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-sport-ex-sciences/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-criminology/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-childhood-studies/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-health-social-care/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-sociology/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-community-youth-work/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-computing/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-computer-science/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-games-software-development/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-network-computing/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-cybersecurity-computer-forensics/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-information-communication-technology/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-journalism/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-sports-journalism/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-media-culture-comms/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-film-media/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-fashion-journalism/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-law/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-digital-film-production/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-media-production/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-english/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-history/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/integrated-performing-arts/',
        'https://www.sunderland.ac.uk/study/creative-arts/undergraduate-photography-video-digital-imaging/',
        'https://www.sunderland.ac.uk/study/creative-arts/undergraduate-glass-ceramics/',
        'https://www.sunderland.ac.uk/study/creative-arts/undergraduate-fine-art/',
        'https://www.sunderland.ac.uk/study/creative-arts/undergraduate-art-design-extended/',
        'https://www.sunderland.ac.uk/study/business-and-management/undergraduate-international-business/',
        'https://www.sunderland.ac.uk/study/business-and-management/undergraduate-business-management/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-business-financial-management/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-business-management/',
        'https://www.sunderland.ac.uk/study/business-and-management/undergraduate-business-marketing-management/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-business-marketing-management/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-business-hr-management/',
        'https://www.sunderland.ac.uk/study/business-and-management/undergraduate-hr-management/',
        'https://www.sunderland.ac.uk/study/business-and-management/undergraduate-business-economics/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/business-economics/',
        'https://www.sunderland.ac.uk/study/business-and-management/undergraduate-business-financial-management/',
        'https://www.sunderland.ac.uk/study/business-and-management/undergraduate-business-hr-management-sc/',
        'https://www.sunderland.ac.uk/study/business-and-management/undergraduate-business-management-sc/',
        'https://www.sunderland.ac.uk/study/business-and-management/undergraduate-business-marketing-management-sc/',
        'https://www.sunderland.ac.uk/study/business-and-management/undergraduate-business-management-extended-sc/',
        'https://www.sunderland.ac.uk/study/business-and-management/undergraduate-hospitality-management-sc/',
        'https://www.sunderland.ac.uk/study/computing/undergraduate-computing/',
        'https://www.sunderland.ac.uk/study/computing/undergraduate-computer-forensics/',
        'https://www.sunderland.ac.uk/study/computing/undergraduate-computer-science/',
        'https://www.sunderland.ac.uk/study/computing/undergraduate-information-communication-technology/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-computing/',
        'https://www.sunderland.ac.uk/study/computing/undergraduate-network-computing/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-computer-science/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-network-computing/',
        'https://www.sunderland.ac.uk/study/computing/undergraduate-games-software-development/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-games-software-development/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-information-communication-technology/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-cybersecurity-computer-forensics/',
        'https://www.sunderland.ac.uk/study/design/undergraduate-graphic-design/',
        'https://www.sunderland.ac.uk/study/design/undergraduate-animation-games-art/',
        'https://www.sunderland.ac.uk/study/design/undergraduate-illustration-design/',
        'https://www.sunderland.ac.uk/study/design/undergraduate-fashion-design-promotion/',
        'https://www.sunderland.ac.uk/study/design/undergraduate-advertising-design-sc/',
        'https://www.sunderland.ac.uk/study/education/undergraduate-education-studies/',
        'https://www.sunderland.ac.uk/study/education/undergraduate-primary-education-qts/',
        'https://www.sunderland.ac.uk/study/education/undergraduate-physics-mathematics-qts/',
        'https://www.sunderland.ac.uk/study/english/tesol-english-language/',
        'https://www.sunderland.ac.uk/study/education/undergraduate-mathematics-education-qts/',
        'https://www.sunderland.ac.uk/study/social-sciences/undergraduate-childhood-studies/',
        'https://www.sunderland.ac.uk/study/education/modern-foreign-languages-education-qts/',
        'https://www.sunderland.ac.uk/study/engineering/undergraduate-mechanical-engineering/',
        'https://www.sunderland.ac.uk/study/engineering/undergraduate-automotive-engineering/',
        'https://www.sunderland.ac.uk/study/engineering/meng-mechanical-engineering/',
        'https://www.sunderland.ac.uk/study/engineering/undergraduate-electronic-electrical-engineering/',
        'https://www.sunderland.ac.uk/study/engineering/undergraduate-manufacturing-engineering/',
        'https://www.sunderland.ac.uk/study/engineering/meng-manufacturing-engineering/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-mechanical-engineering/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-automotive-engineering/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-electronic-electrical-engineering/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-manufacturing-engineering/',
        'https://www.sunderland.ac.uk/study/engineering/undergraduate-electronic-electrical-sc-dual-award/',
        'https://www.sunderland.ac.uk/study/engineering/undergraduate-mechanical-engineering-sc-dual-award/',
        'https://www.sunderland.ac.uk/study/engineering/undergraduate-mechanical-engineering-sc/',
        'https://www.sunderland.ac.uk/study/engineering/undergraduate-automotive-engineering-sc/',
        'https://www.sunderland.ac.uk/study/engineering/meng-electronic-electrical-engineering/',
        'https://www.sunderland.ac.uk/study/engineering/undergraduate-electronic-electrical-engineering-sc/',
        'https://www.sunderland.ac.uk/study/english/undergraduate-english/',
        'https://www.sunderland.ac.uk/study/english/tesol-english-language/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-english/',
        'https://www.sunderland.ac.uk/study/health-paramedic-clinical-sciences/undergraduate-paramedic-science/',
        'https://www.sunderland.ac.uk/study/health-paramedic-clinical-sciences/undergraduate-healthcare-physiological-life/',
        'https://www.sunderland.ac.uk/study/health-paramedic-clinical-sciences/undergraduate-public-health/',
        'https://www.sunderland.ac.uk/study/health-paramedic-clinical-sciences/undergraduate-biomedical-science/',
        'https://www.sunderland.ac.uk/study/health-paramedic-clinical-sciences/undergraduate-physiological-sciences/',
        'https://www.sunderland.ac.uk/study/health-paramedic-clinical-sciences/undergraduate-extended-biomedical-sciences/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-public-health/',
        'https://www.sunderland.ac.uk/study/health-paramedic-clinical-sciences/undergraduate-practice-development-sc/',
        'https://www.sunderland.ac.uk/study/history/undergraduate-history/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-history/',
        'https://www.sunderland.ac.uk/study/history/politics-history/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/politics-history/',
        'https://www.sunderland.ac.uk/study/journalism-and-pr/undergraduate-social-media-management/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/social-media-management/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-fashion-journalism/',
        'https://www.sunderland.ac.uk/study/journalism-and-pr/undergraduate-fashion-journalism/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-sports-journalism/',
        'https://www.sunderland.ac.uk/study/journalism-and-pr/undergraduate-sports-journalism/',
        'https://www.sunderland.ac.uk/study/journalism-and-pr/undergraduate-journalism/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-journalism/',
        'https://www.sunderland.ac.uk/study/languages/french-spanish/',
        'https://www.sunderland.ac.uk/study/english/tesol-english-language/',
        'https://www.sunderland.ac.uk/study/law/undergraduate-law/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-law/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-media-production/',
        'https://www.sunderland.ac.uk/study/media/undergraduate-media-production/',
        'https://www.sunderland.ac.uk/study/media/undergraduate-digital-film-production/',
        'https://www.sunderland.ac.uk/study/media/undergraduate-film-media/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-digital-film-production/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-film-media/',
        'https://www.sunderland.ac.uk/study/media/undergraduate-media-culture-comms/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-media-culture-comms/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/social-media-management/',
        'https://www.sunderland.ac.uk/study/media/undergraduate-media-culture-comms-sc/',
        'https://www.sunderland.ac.uk/study/media/undergraduate-screen-performance/',
        'https://www.sunderland.ac.uk/study/medicine/mbchb-medicine/',
        'https://www.sunderland.ac.uk/study/nursing/undergraduate-adult-nursing-practice/',
        'https://www.sunderland.ac.uk/study/nursing/learning-disability-nursing/',
        'https://www.sunderland.ac.uk/study/nursing/mental-health-nursing/',
        'https://www.sunderland.ac.uk/study/performing-arts/undergraduate-performing-arts/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/integrated-performing-arts/',
        'https://www.sunderland.ac.uk/study/performing-arts/professional-dance/',
        'https://www.sunderland.ac.uk/study/media/undergraduate-screen-performance/',
        'https://www.sunderland.ac.uk/study/performing-arts/undergraduate-jazz-commercial-popular-music/',
        'https://www.sunderland.ac.uk/study/pharmacy-pharmaceutical-and-cosmetic-sciences/undergraduate-pharmacy/',
        'https://www.sunderland.ac.uk/study/pharmacy-pharmaceutical-and-cosmetic-sciences/undergraduate-biochemistry/',
        'https://www.sunderland.ac.uk/study/pharmacy-pharmaceutical-and-cosmetic-sciences/undergraduate-cosmetic-science/',
        'https://www.sunderland.ac.uk/study/pharmacy-pharmaceutical-and-cosmetic-sciences/medicinal-chemistry/',
        'https://www.sunderland.ac.uk/study/pharmacy-pharmaceutical-and-cosmetic-sciences/undergraduate-biopharmaceutical-science/',
        'https://www.sunderland.ac.uk/study/pharmacy-pharmaceutical-and-cosmetic-sciences/undergraduate-extended-biopharmaceutical-science/',
        'https://www.sunderland.ac.uk/study/psychology/forensic-psychology/',
        'https://www.sunderland.ac.uk/study/psychology/psychology-health-wellbeing/',
        'https://www.sunderland.ac.uk/study/psychology/psychology-clinical-skills/',
        'https://www.sunderland.ac.uk/study/psychology/undergraduate-psychology/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-psychology/',
        'https://www.sunderland.ac.uk/study/psychology/undergraduate-psychology-counselling/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-psychology-counselling/',
        'https://www.sunderland.ac.uk/study/social-sciences/undergraduate-sociology/',
        'https://www.sunderland.ac.uk/study/social-sciences/undergraduate-social-work/',
        'https://www.sunderland.ac.uk/study/social-sciences/undergraduate-health-social-care/',
        'https://www.sunderland.ac.uk/study/social-sciences/undergraduate-community-youth-work/',
        'https://www.sunderland.ac.uk/study/social-sciences/undergraduate-criminology/',
        'https://www.sunderland.ac.uk/study/social-sciences/undergraduate-childhood-studies/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-sociology/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-health-social-care/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-criminology/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-childhood-studies/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-community-youth-work/',
        'https://www.sunderland.ac.uk/study/social-sciences/undergraduate-social-work-pt/',
        'https://www.sunderland.ac.uk/study/social-sciences/undergraduate-health-social-care-pt/',
        'https://www.sunderland.ac.uk/study/social-sciences/health-social-care-sc/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-sociology/',
        'https://www.sunderland.ac.uk/study/sport-and-exercise-sciences/undergraduate-exercise-health-fitness/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-physical-ed-sports-coaching/',
        'https://www.sunderland.ac.uk/study/sport-and-exercise-sciences/undergraduate-sport-exercise-sciences/',
        'https://www.sunderland.ac.uk/study/sport-and-exercise-sciences/undergraduate-sports-coaching/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-ex-health-fitness/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-sports-coaching/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-sport-ex-sciences/',
        'https://www.sunderland.ac.uk/study/sport-and-exercise-sciences/undergraduate-physical-education-sports-coaching/',
        'https://www.sunderland.ac.uk/study/tourism-hospitality-and-events/undergraduate-tourism-aviation-management/',
        'https://www.sunderland.ac.uk/study/tourism-hospitality-and-events/undergraduate-tourism-management/',
        'https://www.sunderland.ac.uk/study/tourism-hospitality-and-events/n820-ba-hons-events-management/',
        'https://www.sunderland.ac.uk/study/tourism-hospitality-and-events/undergraduate-tourism-hospitality-management/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/integrated-events-management/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-tourism-hospitality-management/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-tourism-management/',
        'https://www.sunderland.ac.uk/study/tourism-hospitality-and-events/undergraduate-international-tourism-hospitality-sc/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-psychology/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-psychology-counselling/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-physical-ed-sports-coaching/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-public-health/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/screen-performance/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/business-economics/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/social-media-management/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/politics-history/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-ex-health-fitness/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-sports-coaching/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-automotive-engineering/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-electronic-electrical-engineering/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-mechanical-engineering/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-business-management/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-manufacturing-engineering/',
        'https://www.sunderland.ac.uk/study/integrated-foundation-year/ug-integrated-business-hr-management/'
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
        degree_type = 1

        #4.degree_name
        degree_name = response.xpath('/html/body/div[2]/header/div/div[1]/h1/span[1]').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        if '(Hons)' in degree_name:
            degree_name = degree_name.replace('(Hons)','').strip()
        # print(degree_name,response.url)

        #5.programme_en
        programme_en = response.xpath('/html/body/div[2]/header/div/div[1]/h1/text()').extract()
        programme_en = ''.join(programme_en)
        programme_en = clear_space_str(programme_en).strip()
        # print(programme_en)

        #6.duration
        duration = response.xpath('/html/body/div[2]/header/aside/div/ul/li[1]/span').extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        if 'Full/Part' in duration:
            duration = ''
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

        #10.ucascode
        ucascode = response.xpath("//*[contains(text(),'UCAS code')]/..").extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode).replace('UCAS code','').strip()
        if len(ucascode)>50:
            ucascode = ucascode[:50]
        # print(ucascode)

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

        #14.apply_desc_en
        apply_desc_en = response.xpath("//*[contains(text(),'Entry requirements')]//following-sibling::*").extract()
        apply_desc_en = ''.join(apply_desc_en)
        apply_desc_en = remove_class(apply_desc_en)
        # print(apply_desc_en)

        #15.ielts 16171819
        ielts = 6.0
        ielts_r = 5.5
        ielts_w = 5.5
        ielts_s = 5.5
        ielts_l = 5.5
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

        #23.alevel
        alevel = response.xpath('//*[@id="fees-and-reqs"]/div[1]/p[3]').extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel)
        # print(alevel)

        item['alevel'] = alevel
        item['apply_proces_en'] = apply_proces_en
        item['university'] = university
        item['url'] = url
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['programme_en'] = programme_en
        item['duration'] = duration
        item['start_date'] = start_date
        item['tuition_fee'] = tuition_fee
        item['ucascode'] = ucascode
        item['tuition_fee_pre'] = tuition_fee_pre
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['apply_desc_en'] = apply_desc_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['career_en'] = career_en
        yield item