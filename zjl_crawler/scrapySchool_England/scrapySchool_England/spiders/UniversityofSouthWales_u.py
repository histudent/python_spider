# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/9 14:25'
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
from scrapySchool_England.getTuition_fee import getT_fee
class UniversityofSouthWalesSpider(scrapy.Spider):
    name = 'UniversityofSouthWales_u'
    allowed_domains = ['southwales.ac.uk/']
    start_urls = []
    C= [
        'https://www.southwales.ac.uk/courses/-ba-hons-early-years-education-and-practice-with-early-years-practitioner-status',
        'https://www.southwales.ac.uk/courses/ba-anrh-astudiaethau-cynradd-gyda-sac',
        'https://www.southwales.ac.uk/courses/ba-anrh-theatr-a-drama',
        'https://www.southwales.ac.uk/courses/ba-hons-accounting-and-finance',
        'https://www.southwales.ac.uk/courses/ba-hons-advertising-design',
        'https://www.southwales.ac.uk/courses/ba-hons-animation-d-and-stop-motion',
        'https://www.southwales.ac.uk/courses/ba-hons-business',
        'https://www.southwales.ac.uk/courses/ba-hons-business-management',
        'https://www.southwales.ac.uk/courses/ba-hons-business-studies-top-up',
        'https://www.southwales.ac.uk/courses/ba-hons-business-and-accounting-top-up',
        'https://www.southwales.ac.uk/courses/ba-hons-business-and-finance-top-up',
        'https://www.southwales.ac.uk/courses/ba-hons-business-and-human-resource-management-top-up',
        'https://www.southwales.ac.uk/courses/ba-hons-business-and-marketing-top-up',
        'https://www.southwales.ac.uk/courses/ba-hons-business-and-supply-chain-management-top-up',
        'https://www.southwales.ac.uk/courses/ba-hons-cinema',
        'https://www.southwales.ac.uk/courses/ba-hons-computer-animation',
        'https://www.southwales.ac.uk/courses/ba-hons-computer-games-design',
        'https://www.southwales.ac.uk/courses/ba-hons-counselling-and-therapeutic-practice',
        'https://www.southwales.ac.uk/courses/ba-hons-creative-industries-photography-top-up',
        'https://www.southwales.ac.uk/courses/ba-hons-creative-and-therapeutic-arts',
        'https://www.southwales.ac.uk/courses/ba-hons-dance',
        'https://www.southwales.ac.uk/courses/ba-hons-documentary-photography',
        'https://www.southwales.ac.uk/courses/ba-hons-english',
        'https://www.southwales.ac.uk/courses/ba-hons-english-and-creative-writing',
        'https://www.southwales.ac.uk/courses/ba-hons-event-management',
        'https://www.southwales.ac.uk/courses/ba-hons-fashion-design',
        'https://www.southwales.ac.uk/courses/ba-hons-fashion-marketing-and-retail-design',
        'https://www.southwales.ac.uk/courses/ba-hons-fashion-promotion',
        'https://www.southwales.ac.uk/courses/ba-hons-film',
        'https://www.southwales.ac.uk/courses/ba-hons-film-studies',
        'https://www.southwales.ac.uk/courses/ba-hons-forensic-accounting',
        'https://www.southwales.ac.uk/courses/ba-hons-game-art',
        'https://www.southwales.ac.uk/courses/ba-hons-graphic-communication',
        'https://www.southwales.ac.uk/courses/ba-hons-history',
        'https://www.southwales.ac.uk/courses/ba-hons-hotel-and-hospitality-management',
        'https://www.southwales.ac.uk/courses/ba-hons-human-resource-management',
        'https://www.southwales.ac.uk/courses/ba-hons-illustration',
        'https://www.southwales.ac.uk/courses/ba-hons-interior-design',
        'https://www.southwales.ac.uk/courses/ba-hons-international-business-top-up',
        'https://www.southwales.ac.uk/courses/ba-hons-journalism',
        'https://www.southwales.ac.uk/courses/ba-hons-logistics-and-supply-chain-management',
        'https://www.southwales.ac.uk/courses/ba-hons-marketing',
        'https://www.southwales.ac.uk/courses/ba-hons-media-production',
        'https://www.southwales.ac.uk/courses/ba-hons-media-culture-and-journalism',
        'https://www.southwales.ac.uk/courses/ba-hons-music-business',
        'https://www.southwales.ac.uk/courses/ba-hons-performance-and-media',
        'https://www.southwales.ac.uk/courses/ba-hons-performing-arts',
        'https://www.southwales.ac.uk/courses/ba-hons-photography',
        'https://www.southwales.ac.uk/courses/ba-hons-photojournalism',
        'https://www.southwales.ac.uk/courses/ba-hons-popular-and-commercial-music-',
        'https://www.southwales.ac.uk/courses/ba-hons-primary-studies-with-qts',
        'https://www.southwales.ac.uk/courses/ba-hons-public-services',
        'https://www.southwales.ac.uk/courses/ba-hons-sports-journalism',
        'https://www.southwales.ac.uk/courses/ba-hons-strategic-customer-management',
        'https://www.southwales.ac.uk/courses/ba-hons-tv-and-film-set-design',
        'https://www.southwales.ac.uk/courses/ba-hons-theatre-and-drama',
        'https://www.southwales.ac.uk/courses/ba-hons-visual-effects-and-motion-graphics',
        'https://www.southwales.ac.uk/courses/ba-hons-working-with-children-and-families',
        'https://www.southwales.ac.uk/courses/ba-hons-youth-and-community-work',
        'https://www.southwales.ac.uk/courses/ba-hons-youth-and-community-work-youth-justice',
        'https://www.southwales.ac.uk/courses/beng-hons-aeronautical-engineering',
        'https://www.southwales.ac.uk/courses/beng-hons-aeronautical-engineering-including-foundation-year',
        'https://www.southwales.ac.uk/courses/beng-hons-civil-engineering',
        'https://www.southwales.ac.uk/courses/beng-hons-electrical-and-electronic-engineering',
        'https://www.southwales.ac.uk/courses/beng-hons-electrical-and-electronic-engineering-including-foundation-year',
        'https://www.southwales.ac.uk/courses/beng-hons-mechanical-engineering',
        'https://www.southwales.ac.uk/courses/beng-hons-mechanical-engineering-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bmus-hons-contemporary-music-performance',
        'https://www.southwales.ac.uk/courses/bsc-hons-acute-and-critical-care',
        'https://www.southwales.ac.uk/courses/bsc-hons-aircraft-maintenance-engineering',
        'https://www.southwales.ac.uk/courses/bsc-hons-aircraft-maintenance-engineering-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-aircraft-maintenance-engineering-topup',
        'https://www.southwales.ac.uk/courses/bsc-hons-analytical-and-forensic-science-top-up',
        'https://www.southwales.ac.uk/courses/bsc-hons-applied-cyber-security',
        'https://www.southwales.ac.uk/courses/bsc-hons-banking-finance-and-investment-top-up',
        'https://www.southwales.ac.uk/courses/bsc-hons-biology',
        'https://www.southwales.ac.uk/courses/bsc-hons-biology-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-chemistry',
        'https://www.southwales.ac.uk/courses/bsc-hons-chemistry-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-childhood-development',
        'https://www.southwales.ac.uk/courses/bsc-hons-childhood-studies-top-up',
        'https://www.southwales.ac.uk/courses/bsc-hons-civil-engineering',
        'https://www.southwales.ac.uk/courses/bsc-hons-civil-engineering-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-civil-engineering-post-diploma',
        'https://www.southwales.ac.uk/courses/bsc-hons-community-health-wellbeing-topup',
        'https://www.southwales.ac.uk/courses/bsc-hons-community-health-studies-specialist-practitioner-community-childrens-nursing',
        'https://www.southwales.ac.uk/courses/bsc-hons-community-health-studies-specialist-practitioner-district-nursing-with-integrated-v',
        'https://www.southwales.ac.uk/courses/bsc-hons-community-health-studies-specialist-practitioner-general-practice-nursing',
        'https://www.southwales.ac.uk/courses/bsc-hons-computer-applications-development-',
        'https://www.southwales.ac.uk/courses/bsc-hons-computer-applications-development-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-computer-forensics',
        'https://www.southwales.ac.uk/courses/bsc-hons-computer-forensics-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-computer-games-development',
        'https://www.southwales.ac.uk/courses/bsc-hons-computer-games-development-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-computer-science',
        'https://www.southwales.ac.uk/courses/bsc-hons-computer-science-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-computer-security',
        'https://www.southwales.ac.uk/courses/bsc-hons-computer-security-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-construction-project-management',
        'https://www.southwales.ac.uk/courses/bsc-hons-construction-project-management-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-creative-industries-popular-music-technology-topup',
        'https://www.southwales.ac.uk/courses/bsc-hons-criminology-criminal-justice-and-youth-justice',
        'https://www.southwales.ac.uk/courses/bsc-hons-criminology-and-criminal-justice',
        'https://www.southwales.ac.uk/courses/bsc-hons-criminology-and-criminal-justice-and-sociology',
        'https://www.southwales.ac.uk/courses/bsc-hons-criminology-and-criminal-justice-with-psychology',
        'https://www.southwales.ac.uk/courses/bsc-hons-electrical-and-electronic-engineering-top-up',
        'https://www.southwales.ac.uk/courses/bsc-hons-football-coaching-and-performance',
        'https://www.southwales.ac.uk/courses/bsc-hons-football-coaching-development-and-administration',
        'https://www.southwales.ac.uk/courses/bsc-hons-football-coaching-development-and-administration-top-up',
        'https://www.southwales.ac.uk/courses/bsc-hons-forensic-biology',
        'https://www.southwales.ac.uk/courses/bsc-hons-forensic-investigation',
        'https://www.southwales.ac.uk/courses/bsc-hons-forensic-science',
        'https://www.southwales.ac.uk/courses/bsc-hons-forensic-science-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-forensic-science-with-criminology',
        'https://www.southwales.ac.uk/courses/bsc-hons-forensic-science-with-criminology-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-geography',
        'https://www.southwales.ac.uk/courses/bsc-hons-geography-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-geology',
        'https://www.southwales.ac.uk/courses/bsc-hons-geology-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-geology-and-physical-geography',
        'https://www.southwales.ac.uk/courses/bsc-hons-health-and-social-care-management',
        'https://www.southwales.ac.uk/courses/bsc-hons-human-biology',
        'https://www.southwales.ac.uk/courses/bsc-hons-human-biology-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-information-communication-technology',
        'https://www.southwales.ac.uk/courses/bsc-hons-information-communication-technology-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-international-wildlife-biology',
        'https://www.southwales.ac.uk/courses/bsc-hons-lighting-design-and-technology',
        'https://www.southwales.ac.uk/courses/bsc-hons-lighting-design-and-technology-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-mathematics',
        'https://www.southwales.ac.uk/courses/bsc-hons-mathematics-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-mechanical-engineering',
        'https://www.southwales.ac.uk/courses/bsc-hons-medical-sciences',
        'https://www.southwales.ac.uk/courses/bsc-hons-medicinal-and-biological-chemistry',
        'https://www.southwales.ac.uk/courses/bsc-hons-medicinal-and-biological-chemistry-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-natural-history',
        'https://www.southwales.ac.uk/courses/bsc-hons-natural-history-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-pharmaceutical-science',
        'https://www.southwales.ac.uk/courses/bsc-hons-pharmaceutical-science-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-police-sciences',
        'https://www.southwales.ac.uk/courses/bsc-hons-police-sciences-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-professional-practice-health-care-studies',
        'https://www.southwales.ac.uk/courses/bsc-hons-professional-practice-violence-reduction',
        'https://www.southwales.ac.uk/courses/bsc-hons-psychology',
        'https://www.southwales.ac.uk/courses/bsc-hons-psychology-with-behaviour-analysis',
        'https://www.southwales.ac.uk/courses/bsc-hons-psychology-with-counselling',
        'https://www.southwales.ac.uk/courses/bsc-hons-psychology-with-criminology-criminal-justice',
        'https://www.southwales.ac.uk/courses/bsc-hons-psychology-with-developmental-disorders',
        'https://www.southwales.ac.uk/courses/bsc-hons-public-health',
        'https://www.southwales.ac.uk/courses/bsc-hons-quantity-surveying-and-commercial-management',
        'https://www.southwales.ac.uk/courses/bsc-hons-quantity-surveying-and-commercial-management-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-rugby-coaching-and-performance',
        'https://www.southwales.ac.uk/courses/bsc-hons-secondary-design-and-technology-with-qts',
        'https://www.southwales.ac.uk/courses/bsc-hons-secondary-mathematics-with-ict-with-qts',
        'https://www.southwales.ac.uk/courses/bsc-hons-secondary-mathematics-with-science-with-qts',
        'https://www.southwales.ac.uk/courses/bsc-hons-secondary-science-with-ict-with-qts',
        'https://www.southwales.ac.uk/courses/bsc-hons-secondary-science-with-mathematics-with-qts',
        'https://www.southwales.ac.uk/courses/bsc-hons-social-work',
        'https://www.southwales.ac.uk/courses/bsc-hons-sociology',
        'https://www.southwales.ac.uk/courses/bsc-hons-sound-and-live-event-production',
        'https://www.southwales.ac.uk/courses/bsc-hons-sound-and-live-event-production-including-foundation-year',
        'https://www.southwales.ac.uk/courses/bsc-hons-specialist-community-public-health-nursing-health-visiting',
        'https://www.southwales.ac.uk/courses/bsc-hons-specialist-community-public-health-nursing-school-nursing',
        'https://www.southwales.ac.uk/courses/bsc-hons-sport-psychology',
        'https://www.southwales.ac.uk/courses/bsc-hons-sport-and-exercise-science',
        'https://www.southwales.ac.uk/courses/bsc-hons-sports-coaching-and-development',
        'https://www.southwales.ac.uk/courses/bsc-hons-sports-coaching-and-performance-topup',
        'https://www.southwales.ac.uk/courses/bsc-hons-strength-and-conditioning',
        'https://www.southwales.ac.uk/courses/bsc-hons-systemic-counselling',
        'https://www.southwales.ac.uk/courses/bachelor-of-midwifery-hons-registered-midwife',
        'https://www.southwales.ac.uk/courses/bachelor-of-nursing-honsadult-flexible-learning',
        'https://www.southwales.ac.uk/courses/bachelor-of-nursing-honsadult',
        'https://www.southwales.ac.uk/courses/bachelor-of-nursing-honschild-health',
        'https://www.southwales.ac.uk/courses/bachelor-of-nursing-honslearning-disabilities',
        'https://www.southwales.ac.uk/courses/bachelor-of-nursing-honsmental-health',
        'https://www.southwales.ac.uk/courses/certhe-in-health-care-nursing-support-worker-education',
        'https://www.southwales.ac.uk/courses/certificate-of-higher-education-introduction-to-secondary-teaching',
        'https://www.southwales.ac.uk/courses/chartered-institute-of-procurement-and-supply-cips-diploma-in-procurement-and-supply',
        'https://www.southwales.ac.uk/courses/chartered-institute-of-procurement-and-supply-cips-professional-diploma-in-procurement-and-supply',
        'https://www.southwales.ac.uk/courses/chiropractic-foundation-year',
        'https://www.southwales.ac.uk/courses/foundation-degree-business-studies',
        'https://www.southwales.ac.uk/courses/foundation-degree-community-football-coaching-and-development',
        'https://www.southwales.ac.uk/courses/foundation-degree-community-health-and-wellbeing',
        'https://www.southwales.ac.uk/courses/foundation-degree-sports-coaching-and-development',
        'https://www.southwales.ac.uk/courses/foundation-degree-in-rugby-coaching-and-development-welsh-rugby-union',
        'https://www.southwales.ac.uk/courses/foundation-year-humanities',
        'https://www.southwales.ac.uk/courses/foundation-year-social-sciences',
        'https://www.southwales.ac.uk/courses/further-professional-development-for-returning-and-supply-teachers',
        'https://www.southwales.ac.uk/courses/hnc-civil-engineering',
        'https://www.southwales.ac.uk/courses/hnc-electrical-and-electronic-engineering',
        'https://www.southwales.ac.uk/courses/hnc-mechanical-engineering',
        'https://www.southwales.ac.uk/courses/hnc-surveying',
        'https://www.southwales.ac.uk/courses/hnd-business-studies',
        'https://www.southwales.ac.uk/courses/hnd-electrical-and-electronic-engineering',
        'https://www.southwales.ac.uk/courses/hnd-mechanical-engineering',
        'https://www.southwales.ac.uk/courses/hnd-public-and-emergency-services',
        'https://www.southwales.ac.uk/courses/institute-of-chartered-accountants-in-england-and-wales-icaew',
        'https://www.southwales.ac.uk/courses/international-foundation-programme-intensive-english',
        'https://www.southwales.ac.uk/courses/llb-hons-law',
        'https://www.southwales.ac.uk/courses/llb-hons-law-accelerated-route',
        'https://www.southwales.ac.uk/courses/llb-hons-law-with-criminology-and-criminal-justice',
        'https://www.southwales.ac.uk/courses/llb-hons-legal-practice-exempting',
        'https://www.southwales.ac.uk/courses/mcomp-computer-applications-development',
        'https://www.southwales.ac.uk/courses/mcomp-computer-forensics',
        'https://www.southwales.ac.uk/courses/mcomp-computer-games-development',
        'https://www.southwales.ac.uk/courses/mcomp-computer-science',
        'https://www.southwales.ac.uk/courses/mcomp-computer-security',
        'https://www.southwales.ac.uk/courses/mcomp-information-communication-technology',
        'https://www.southwales.ac.uk/courses/meng-aeronautical-engineering',
        'https://www.southwales.ac.uk/courses/meng-civil-engineering',
        'https://www.southwales.ac.uk/courses/meng-electrical-and-electronic-engineering',
        'https://www.southwales.ac.uk/courses/meng-mechanical-engineering',
        'https://www.southwales.ac.uk/courses/mgeog-geography',
        'https://www.southwales.ac.uk/courses/mmath-mathematics',
        'https://www.southwales.ac.uk/courses/msci-chemistry',
        'https://www.southwales.ac.uk/courses/msci-forensic-biology',
        'https://www.southwales.ac.uk/courses/msci-forensic-investigation',
        'https://www.southwales.ac.uk/courses/msci-forensic-science',
        'https://www.southwales.ac.uk/courses/msci-forensic-science-with-criminology',
        'https://www.southwales.ac.uk/courses/msci-pharmaceutical-science',
        'https://www.southwales.ac.uk/courses/master-of-chiropractic',
        'https://www.southwales.ac.uk/courses/master-of-chiropractic-including-foundation-year',
        'https://www.southwales.ac.uk/courses/professional-graduate-certificate-in-education-pgce-in-post-compulsory-education-and-training-pcet'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of South Wales'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="uni"]/section[1]/div//h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en).strip()
        # print(programme_en)


        #4.degree_type
        degree_type = 1

        #5.degree_name
        if 'BA (Anrh)' in programme_en:
            degree_name = 'BA (Anrh)'
        elif 'BA (Hons)' in programme_en:
            degree_name = 'BA (Hons)'
        elif 'BEng (Hons)' in programme_en:
            degree_name = 'BEng (Hons)'
        elif 'BMus (Hons)' in programme_en:
            degree_name = 'BMus (Hons)'
        elif 'BSc (Hons)' in programme_en:
            degree_name = 'BSc (Hons)'
        elif 'Bachelor of Nursing (Hons)' in programme_en:
            degree_name = 'Bachelor of Nursing (Hons)'
        elif 'Bachelor of Midwifery (Hons)' in programme_en:
            degree_name = 'Bachelor of Midwifery (Hons)'
        elif 'Foundation Degree' in programme_en:
            degree_name = 'Foundation Degree'
        elif 'Foundation Year' in programme_en:
            degree_name = 'Foundation Year'
        elif 'HNC' in programme_en:
            degree_name = 'HNC'
        elif 'HND' in programme_en:
            degree_name = 'HND'
        elif 'LLB (Hons)' in programme_en:
            degree_name = 'LLB (Hons)'
        elif 'MComp' in programme_en:
            degree_name = 'MComp'
        elif 'MEng' in programme_en:
            degree_name = 'MEng'
        elif 'MGeog' in programme_en:
            degree_name = 'MGeog'
        elif 'MMath' in programme_en:
            degree_name = 'MMath'
        elif 'MSci' in programme_en:
            degree_name = 'MSci'
        else:
            degree_name= ''
        programme_en = programme_en.replace(degree_name,'').strip()
        # print(degree_name)
        # print(programme_en)

        #6.overview_en
        overview_en = response.xpath('//*[@id="uni"]/section[1]/div[2]//p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #7.duration #8.duration_per
        duration = response.xpath('//*[@id="2019"]/div/table/tbody/tr/td[3]').extract()
        if len(duration)==0:
            duration = response.xpath('//*[@id="2018"]/div/table/tbody/tr/td[3]').extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        try:
            duration = re.findall(r'\d+',duration)[0]
        except:
            duration = 0
        if int(duration)>6:
            duration_per = 3
        else:
            duration_per = 1
        # print(duration,'**',duration_per)

        #9.ucascode
        ucascode = response.xpath('//*[@id="2019"]/div/table/tbody/tr/td[1]').extract()
        if len(ucascode)==0:
            ucascode = response.xpath('//*[@id="2018"]/div/table/tbody/tr/td[1]').extract()
        ucascode = '*'.join(ucascode)
        ucascode = remove_tags(ucascode)
        # print(ucascode,response.url)

        #10.start_date
        start_date = response.xpath('//*[@id="2018"]/div/table/tbody/tr[1]/td[4]').extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date).strip()
        # print(start_date)

        #11.modules_en
        modules_en = response.xpath('//*[@id="eleven"]/div').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)


        #12.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'Assessment')]//following-sibling::div[1]").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #13.apply_desc_en
        apply_desc_en = response.xpath('//*[@id="odin"]/div').extract()
        apply_desc_en = ''.join(apply_desc_en)
        apply_desc_en = remove_class(apply_desc_en)
        # print(apply_desc_en)

        #14.career_en
        career_en = response.xpath('//*[@id="careers_panel"]/div').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #15.tuition_fee #16.tuition_fee_pre
        tuition_fee = response.xpath("//*[contains(text(),'Full-time International')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getT_fee(tuition_fee)
        # print(tuition_fee,response.url)
        tuition_fee_pre = '£'

        #17.ielts 18192021
        ielts = 6.0
        ielts_l = 5.5
        ielts_w = 5.5
        ielts_s = 5.5
        ielts_r = 5.5
        #22.apply_pre
        apply_pre = '£'

        #23.alevel
        alevel = response.xpath("//*[contains(text(),'Typical A-Level Offer')]//following-sibling::*").extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel)
        # print(alevel)

        #24.ib
        ib = response.xpath("//*[contains(text(),'Typical IB Offer')]//following-sibling::*").extract()
        ib = ''.join(ib)
        ib = remove_tags(ib)
        # print(ib)

        #25.location
        location = response.xpath('//*[@id="2018"]/div/table/tbody/tr/td[5]/a').extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        item['alevel'] = alevel
        item['ib'] = ib
        item['apply_pre'] =  apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['duration_per'] = duration_per
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['apply_desc_en'] = apply_desc_en
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['ielts_w'] = ielts_w

        ucascode_a = response.xpath('//*[@id="2019"]/div/table/tbody/tr/td[1]').extract()
        if len(ucascode_a)==0:
            ucascode_a = response.xpath('//*[@id="2018"]/div/table/tbody/tr/td[1]').extract()
        duration_a = response.xpath('//*[@id="2019"]/div/table/tbody/tr/td[3]').extract()
        if len(duration_a)==0:
            duration_a = response.xpath('//*[@id="2018"]/div/table/tbody/tr/td[3]').extract()
        start_date_a = response.xpath('//*[@id="2019"]/div/table/tbody/tr/td[4]').extract()
        if len(start_date_a)==0:
            start_date_a = response.xpath('//*[@id="2018"]/div/table/tbody/tr/td[4]').extract()
        location_a = response.xpath('//*[@id="2019"]/div/table/tbody/tr/td[5]').extract()
        if len(location_a)==0:
            location_a = response.xpath('//*[@id="2018"]/div/table/tbody/tr/td[5]').extract()
        if len(ucascode_a)>1:
            for i,j,k,l in zip(ucascode_a,duration_a,start_date_a,location_a):
                response_ucascode = i
                response_ucascode = remove_tags(response_ucascode)
                response_duration = j
                try:
                    response_duration = re.findall('\d+',response_duration)[0]
                except:
                    response_duration = ''
                response_start_date = k
                response_start_date = remove_tags(response_start_date).strip()
                response_location = l
                response_location = remove_tags(response_location)
                item['ucascode'] = response_ucascode
                item['duration'] = response_duration
                item['start_date'] = response_start_date
                item['location'] = response_location
                yield item
        else:
            item['ucascode'] = ucascode
            item['duration'] = duration
            item['start_date'] = start_date
            item['location'] = location
            yield item