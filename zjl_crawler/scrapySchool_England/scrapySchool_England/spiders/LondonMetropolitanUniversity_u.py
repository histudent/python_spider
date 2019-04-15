# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/2 11:47'
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
class LondonMetropolitanUniversitySpider(scrapy.Spider):
    name = 'LondonMetropolitanUniversity_u'
    allowed_domains = ['lse.ac.uk/']
    start_urls = []
    C = [
        'https://www.londonmet.ac.uk/courses/undergraduate/airline-airport-and-aviation-management---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/architecture-and-interior-design-extended-degree-with-foundation-year---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/accounting-and-finance---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/advertising-marketing-communications-and-public-relations---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/architecture---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/art-and-design-extended-degree-with-foundation-year---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/accounting-and-finance-extended-degree---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/banking-and-finance-with-integrated-professional-training---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/biochemistry-extended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/banking-and-finance---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/biology-of-infectious-disease-extended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/biological-sciences-extended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/biochemistry---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/beauty-marketing-and-journalism---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/biological-science---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/biology-of-infectious-disease---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/biomedical-scienceextended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/biomedical-science---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/business-economics---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/business-management-extended-degree---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/business-law---llb-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/business-information-technology---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/business-management-and-marketing---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/chemistry---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/business-management---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/business-studies---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/chemistry-extended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/community-development-and-leadership---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/computer-games-programming---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/computer-networking-and-cyber-security---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/computer-networking---beng-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/community-development-and-youth-extended-degree-including-foundation-year---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/computing-technology-and-mathematics-extended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/computing-extended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/computing---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/computer-systems-engineering---beng-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/computer-science---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/computer-network-engineering-extended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/creative-writing-and-english-literature---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/creative-writing-and-english-literature-extended-degree-including-foundation-year---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/criminology-and-youth-studies---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/criminology-and-international-security---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/criminology-and-psychology---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/criminology-policing-and-law-extended-degree-including-foundation-year---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/criminology---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/cyber-security-extended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/criminology-and-sociology---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/criminology-and-policing---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/digital-forensics-and-cyber-security---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/design-for-publishing---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/design-studio-practice---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/dietetics-and-nutrition---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/dietetics---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/early-childhood-studies-extended-degree-including-foundation-year---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/diplomacy-and-law---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/diplomacy-and-international-relations---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/early-years-education-two-year-accelerated-degree---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/digital-media---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/economics---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/early-childhood-studies---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/education-and-social-policy---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/criminology-and-law---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/education-studies-and-english-literature---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/economics-and-finance---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/education-studies-extended-degree-including-foundation-year---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/electronic-and-communications-engineering---beng-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/education-studies---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/fashion-marketing-and-journalism---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/fashion-and-textiles-extended-degree-with-foundation-year---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/fashion-marketing-and-business-management---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/fashion-photography---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/english-literature---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/events-management---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/fashion-accessories-and-jewellery---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/film-photography-and-media-extended-degree-with-foundation-year---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/film-and-television-production---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/film-and-television-studies---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/financial-mathematics---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/film-and-broadcast-production---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/fine-art---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/furniture-and-product-design---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/forensic-science---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/games-animation-modelling-and-effects---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/fashion---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/games-modelling-animation-and-effects---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/forensic-science-extended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/games-programming---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/health-and-social-care-extended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/health-and-social-care---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/health-and-social-policy---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/human-nutrition---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/human-nutritionextended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/graphic-design---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/illustration-and-animation---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/interior-design-and-decoration---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/international-business-management---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/interior-design---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/interior-architecture-and-design---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/international-relations-and-politics-extended-degree-including-foundation-year---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/international-relations-and-law---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/international-relations-and-politics---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/international-relations-with-french---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/international-relations-with-spanish---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/international-relations-with-arabic---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/journalism-film-and-television-studies---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/journalism---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/international-relations-peace-and-conflict-studies---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/international-relations-with-languages---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/mathematical-sciences---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/law-with-international-relations---llb-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/international-relations---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/law---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/llb-law---hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/material-and-visual-culture---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/mathematics-extended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/media-and-communications-extended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/mathematics---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/media-and-marketing---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/mathematics-and-computer-science---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/media-with-spanish---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/media-and-communications---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/media-and-public-relations---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/media-with-french---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/media-with-arabic---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/media-communications-and-journalism---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/medical-sciences-two-year-accelerated-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/llb-criminal-law---hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/media-with-languages---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/medical-bioscience---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/multimedia-journalism---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/pharmaceutical-science-extended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/pharmaceutical-science---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/pharmacology---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/music-business-and-live-entertainment---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/pharmacologyextended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/painting---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/photojournalism---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/photography---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/police-studies-procedure-and-investigation---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/psychology-and-sociology---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/medical-bioscience-extended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/psychology-extended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/primary-education-two-year-accelerated-degree---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/sciences-extended-degree---biology-chemistry-health-psychology---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/psychology---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/social-sciences-and-humanities-extended-degree---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/social-work-extended-degree-including-foundation-year---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/social-work---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/society-politics-and-policy---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/sociology---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/politics---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/sport-psychology-coaching-and-physical-education---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/music-technology-and-production---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/sociology-and-social-policy---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/sports-scienceextended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/sport-and-exercise-science---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/sports-therapy-extended-degree---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/sports-and-dance-therapy---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/textile-design---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/theatre-and-film-production-design---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/sports-therapy---bsc-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/theatre-and-film---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/translation---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/theatre-and-performance-practice---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/tourism-and-travel-management---ba-hons/',
        'https://www.londonmet.ac.uk/courses/undergraduate/youth-studies---bsc-hons/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'London Metropolitan University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.ucascode
        ucascode = response.xpath("//*[contains(text(),'UCAS code:')]//following-sibling::*").extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode)
        ucascode = clear_space_str(ucascode)
        # print(ucascode)

        #4.programme_en
        programme_en = response.xpath('//*[@id="MainContent"]/div[1]/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #5.degree_type
        degree_type = 1

        #6.degree_name
        # degree_name = re.findall(r'-\s(.*)',programme_en)[0]
        # programme_en = programme_en.replace(degree_name,'').replace('-','').strip()
        # print(degree_name)
        # print(programme_en)

        #7.alevel
        alevel = response.xpath('//*[@id="entry-requirements"]/div/ul/li[1]').extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel)
        alevel = clear_space_str(alevel)
        # print(alevel)

        #8.overview_en
        overview_en =response.xpath('//*[@id="LeftColumn"]/section/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #9.start_date
        start_date = '2018-8-18'

        #10.apply_pre
        apply_pre = '£'

        #11.duration
        try:
            duration = response.xpath("//*[contains(text(),'September 2019 - Full-time')]//@data-duration").extract()[0]
            duration = ''.join(duration)
            if len(duration)==0:
                duration = response.xpath("//*[contains(text(),'September 2018 - Full-time')]//@data-duration")[0]
                duration = ''.join(duration)
        except:duration = ''
        # print(duration,response.url)


        #12.tuition_fee
        tuition_fee= response.xpath("//*[contains(text(),'September 2019 - Full-time')]//@data-cost").extract()
        tuition_fee = ''.join(tuition_fee)
        if len(tuition_fee)==0:
            tuition_fee = response.xpath("//*[contains(text(),'September 2018 - Full-time')]//@data-cost").extract()
            tuition_fee = ''.join(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #13.location
        # location = response.xpath("//*[contains(text(),'Location')]//following-sibling::*[1]").extract()[0]
        # location = ''.join(location)
        # location = remove_tags(location).replace('Location:','').strip()
        # print(location)

        #14.apply_documents_en
        apply_documents_en = '<p>We welcome applications from all suitably qualified prospective students and want to recruit students with the very best academic merit, potential and motivation, irrespective of their background. We carefully consider each application on an individual basis, taking into account all the information presented on your application form, including your: academic achievement (including predicted and achieved grades) personal statement two references CV</p>'

        #15.modules_en
        modules_en = response.xpath('//*[@id="modular-structure"]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en).replace('▼','')
        # modules_en = clear_space_str(modules_en)
        # print(modules_en,url)

        #16.assessment_en
        assessment_en = response.xpath("//h3[contains(text(),'Assessment')]//following-sibling::p[1]").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # assessment_en = clear_space_str(assessment_en)
        # print(assessment_en)

        #17.career_en
        career_en = response.xpath('//*[@id="career-opportunities"]/div').extract()
        career_en = ''.join(career_en)
        # career_en = clear_space_str(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #18.ielts,19.20.21.22
        # if 'LLB' in degree_name:
        #     ielts = 6.5
        #     ielts_r = 6.0
        #     ielts_l = 6.0
        #     ielts_w = 6.0
        #     ielts_s = 6.0
        # elif 'BA Translation Year 2 entry' in degree_name:
        #     ielts = 6.5
        #     ielts_r = 6.0
        #     ielts_l = 6.0
        #     ielts_w = 6.0
        #     ielts_s = 6.0
        # elif 'BA Translation Year 3 entry' in degree_name:
        #     ielts = 7
        #     ielts_r = 6.5
        #     ielts_l = 6.5
        #     ielts_w = 6.5
        #     ielts_s = 6.5
        # elif 'BSc Biomedical Science (Leading to MD)' in degree_name:
        #     ielts = 7
        #     ielts_r = 6.5
        #     ielts_l = 6.5
        #     ielts_w = 6.5
        #     ielts_s = 6.5
        # else:
        #     ielts = 6
        #     ielts_r = 5.5
        #     ielts_l = 5.5
        #     ielts_w = 5.5
        #     ielts_s = 5.5

        #23.require_chinese_en
        require_chinese_en = "https://www.londonmet.ac.uk/international/international-admissions/application-guidance-and-entry-criteria/academic-entry-requirements-by-country/non-eueea-countries/china/"

        #24.apply_proces_en
        apply_proces_en = '<p>Stage 1: choosing your course The first step for you as a new applicant is to choose the course you wish to undertake. If you have any questions at this stage you can contact our international recruitment team who will be happy to assist you and provide information about our courses. You can begin a conversation about a course you are interested in by emailing our recruitment team at: international@londonmet.ac.uk. We often have representatives of London Metropolitan University visiting countries all around the world. You can find out the latest planned trips to see if we will be visiting near you, here: Meet us overseas  Stage 2: applying for your course Once you have decided on your course you need to submit an application as soon as possible making sure you observe the international application deadlines. The method of application depends on the type of course you are applying for. The application methods available for each course are listed on the course page. You should check these details carefully to avoid any delay in your application reaching us.You should observe our international application guidance before submitting an application. Please see here: International application advice Stage 3: awaiting and responding to your offer Once the University receives your application you will receive a communication from us acknowledging this. You will also obtain your London Metropolitan University application ID and details about using, the applicant portal (Evision). At this point your application will enter the pending decision/consideration stage, and we will communicate with you again, either to request more information (such as a qualification transcript, portfolio, or piece of written work) for assessment, or to advise you of our decision.If you are successful in receiving an offer from us you will receive a communication detailing a conditional or unconditional offer, and this will contain further information and instruction. If your application is unsuccessful we will also contact you advising you of this, and our reasons for the decision. You can find out more about offers here: Information and advice for offer holders.Stage 4: Immigration and enrolment After obtaining an unconditional offer you will need to focus on making preparations to join the university and your arrangements to come to the UK (if you are not already here). You will receive further information about when and where to arrive, and how to attend your course enrolment closer to the enrolment period of your course.You should be considering your accommodation and finances as soon as possible before the start of term, and you should also be aware of, and be prepared to meet, any immigration requirements such as obtaining a student visa at the earliest opportunity. You can find a variety of information about moving to London here: Immigration and Arrival Advice: New Students.</p>'


        #26.tuition_fee_pre
        tuition_fee_pre = '£'

        item['apply_pre'] = apply_pre
        item['apply_documents_en'] = apply_documents_en
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        # item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['start_date'] = start_date
        item['duration'] = duration
        item['tuition_fee'] = tuition_fee
        # item['location'] = location
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        # item['ielts'] = ielts
        # item['ielts_r'] = ielts_r
        # item['ielts_w'] = ielts_w
        # item['ielts_s'] = ielts_s
        # item['ielts_l'] = ielts_l
        item['require_chinese_en'] = require_chinese_en
        item['apply_proces_en'] = apply_proces_en
        item['tuition_fee_pre'] = tuition_fee_pre
        item['alevel'] = alevel
        item['ucascode'] = ucascode
        yield item