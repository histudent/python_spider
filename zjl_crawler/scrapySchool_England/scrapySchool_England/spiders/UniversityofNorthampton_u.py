# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/8 17:55'
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
import  requests
from lxml import etree
class UniversityofNorthamptonSpider(scrapy.Spider):
    name = 'UniversityofNorthampton_u'
    allowed_domains = ['northampton.ac.uk/']
    start_urls = []
    C= [
        'https://www.northampton.ac.uk/study/courses/social-care-and-community-practice-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/games-art-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/acting-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/acting-creative-theatre-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/environmental-science-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/engineering-bsc/',
        'https://www.northampton.ac.uk/study/courses/sport-and-exercise-science-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/sport-and-exercise-science-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/biology-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/accounting-and-finance-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/podiatry-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/computing-graphics-and-visualisation-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/computer-networks-engineering-beng-hons-meng/',
        'https://www.northampton.ac.uk/study/courses/computing-computer-networks-engineering-beng-hons/',
        'https://www.northampton.ac.uk/study/courses/computing-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/computing-software-engineering/',
        'https://www.northampton.ac.uk/study/courses/computing-computer-systems-engineering-beng-hons/',
        'https://www.northampton.ac.uk/study/courses/computing-web-technology-and-security/',
        'https://www.northampton.ac.uk/study/courses/product-design-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/fashion-promotion-and-communication/',
        'https://www.northampton.ac.uk/study/courses/footwear-and-accessories-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/graphic-communication-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/criminology-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/economics-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/economics-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/computer-games-development/',
        'https://www.northampton.ac.uk/study/courses/popular-music-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/fashion-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/fashion-textiles-for-fashion-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/leather-for-fashion/',
        'https://www.northampton.ac.uk/study/courses/interior-design-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/childhood-and-youth-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/business-computing-systems-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/mechanical-engineering/',
        'https://www.northampton.ac.uk/study/courses/events-management-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/banking-and-financial-planning-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/marketing-management-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/fashion-marketing-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/business-studies-ba-hons-2/',
        'https://www.northampton.ac.uk/study/courses/business-entrepreneurship-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/international-business-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/management-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/advertising-and-digital-marketing-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/international-tourism-management-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/occupational-therapy-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/paramedic-science-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/geography-human-geography-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/geography-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/geography-physical-geography-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/special-educational-needs-and-inclusion-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/drama-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/human-resource-management-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/psychology-and-counselling-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/fine-art-painting-and-drawing/',
        'https://www.northampton.ac.uk/study/courses/international-relations-and-politics-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/media-production-and-moving-image-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/psychology-developmental-and-educational-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/psychology-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/creative-writing-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/multimedia-sports-journalism/',
        'https://www.northampton.ac.uk/study/courses/criminal-and-corporate-investigation-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/leather-technology-leather-science-marketing-or-business-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/policing-ba/',
        'https://www.northampton.ac.uk/study/courses/multimedia-journalism-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/english-ba/',
        'https://www.northampton.ac.uk/study/courses/mental-health-nursing-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/photography-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/learning-disability-nursing-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/adult-nursing-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/education-studies-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/fine-art/',
        'https://www.northampton.ac.uk/study/courses/social-work-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/sport-development-and-physical-education-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/early-childhood-studies-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/international-development-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/child-nursing-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/history-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/sociology-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/architectural-technology-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/illustration-ba-hons/',
        'https://www.northampton.ac.uk/study/courses/business-computing-web-design-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/law-llb-hons/',
        'https://www.northampton.ac.uk/study/courses/law-twoyear-intensive-llb-hons/',
        'https://www.northampton.ac.uk/study/courses/human-biosciences-bsc-hons/',
        'https://www.northampton.ac.uk/study/courses/mobile-computing-bsc-hons/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Northampton'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="main"]/section/div[1]/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en).strip().replace('BA (Hons)','').replace('BSc (Hons)','').replace('LLB (Hons)','').replace('&amp;','').replace('BEng (Hons) / MEng','').replace('BEng (Hons)','').strip()
        # print(programme_en)

        #4.degree_name
        degree_name = response.xpath('//*[@id="site-content"]/article/header/div[2]/h1/small').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name).replace('(Hons)','').strip()
        # print(degree_name)

        #5.degree_type
        degree_type = 1

        #6.start_date
        start_date= '2018-9'

        #7.duration
        duration = response.xpath("//*[contains(text(),'Length of Study:')]/..").extract()
        duration = ''.join(duration)
        duration =remove_tags(duration)
        # print(duration)

        #8.duration_per
        duration_per = 1

        #9.ucascode
        try:
            list1 = ['https://www.northampton.ac.uk/study/courses/accounting-and-finance-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/acting-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/acting-creative-theatre-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/adult-nursing-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/advertising-and-digital-marketing-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/applied-criminal-justice-studies-topup-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/architectural-technology-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/banking-and-financial-planning-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/biology-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/business-hnd/',
    'https://www.northampton.ac.uk/study/courses/business-and-management-top-up-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/business-computing-systems-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/business-computing-systems-hnd/',
    'https://www.northampton.ac.uk/study/courses/business-computing-web-design-hnd/',
    'https://www.northampton.ac.uk/study/courses/business-computing-web-design-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/business-entrepreneurship-fda/',
    'https://www.northampton.ac.uk/study/courses/business-entrepreneurship-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/business-studies-ba-hons-2/',
    'https://www.northampton.ac.uk/study/courses/child-nursing-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/childhood-and-youth-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/commercial-and-creative-photography-hnd/',
    'https://www.northampton.ac.uk/study/courses/computer-games-development-hnd-hnd/',
    'https://www.northampton.ac.uk/study/courses/computer-games-development/',
    'https://www.northampton.ac.uk/study/courses/computer-networks-engineering-beng-hons-meng/',
    'https://www.northampton.ac.uk/study/courses/computing-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/computing-hnd/',
    'https://www.northampton.ac.uk/study/courses/computing-computer-networks-engineering-beng-hons/',
    'https://www.northampton.ac.uk/study/courses/computing-computer-systems-engineering-beng-hons/',
    'https://www.northampton.ac.uk/study/courses/computing-graphics-and-visualisation-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/mobile-computing-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/computing-software-engineering/',
    'https://www.northampton.ac.uk/study/courses/computing-web-technology-and-security/',
    'https://www.northampton.ac.uk/study/courses/media-production-and-moving-image-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/creative-writing-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/criminal-and-corporate-investigation-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/criminology-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/dental-nursing-fdsc/',
    'https://www.northampton.ac.uk/study/courses/digital-film-production-hnd/',
    'https://www.northampton.ac.uk/study/courses/drama-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/early-childhood-studies-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/early-childhood-studies-topup-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/economics-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/education-studies-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/engineering-hnd/',
    'https://www.northampton.ac.uk/study/courses/engineering-bsc/',
    'https://www.northampton.ac.uk/study/courses/engineering-topup-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/english-ba/',
    'https://www.northampton.ac.uk/study/courses/environmental-science-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/events-management-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/events-management-top-up-ba/',
    'https://www.northampton.ac.uk/study/courses/fashion-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/fashion-textiles-for-fashion-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/fashion-marketing-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/fashion-promotion-and-communication/',
    'https://www.northampton.ac.uk/study/courses/fine-art/',
    'https://www.northampton.ac.uk/study/courses/fine-art-painting-and-drawing/',
    'https://www.northampton.ac.uk/study/courses/footwear-and-accessories-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/games-art-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/geography-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/geography-human-geography-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/geography-physical-geography-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/graphic-communication-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/health-and-social-care-top-up-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/history-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/human-biosciences-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/human-resource-management-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/ba-human-resource-management-top-up/',
    'https://www.northampton.ac.uk/study/courses/illustration-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/interior-design-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/international-accounting-top-up-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/international-business-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/international-business-communications-topup-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/international-development-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/international-hospitality-management-top-up/',
    'https://www.northampton.ac.uk/study/courses/international-logistics-and-trade-finance-topup-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/international-relations-and-politics-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/international-tourism-management-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/international-tourism-management-topup-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/law-llb-hons/',
    'https://www.northampton.ac.uk/study/courses/law-twoyear-intensive-llb-hons/',
    'https://www.northampton.ac.uk/study/courses/learning-and-teaching-topup-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/learning-disability-nursing-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/leather-for-fashion/',
    'https://www.northampton.ac.uk/study/courses/leather-technology-leather-science-marketing-or-business-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/leather-technology-leather-science-marketing-or-business-topup-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/leathersellers-certificate-leather-science-marketing-and-business/',
    'https://www.northampton.ac.uk/study/courses/leathersellers-diploma-leather-science-marketing-or-business/',
    'https://www.northampton.ac.uk/study/courses/management-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/marketing-management-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/marketing-management-topup-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/mechanical-engineering/',
    'https://www.northampton.ac.uk/study/courses/mental-health-nursing-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/multimedia-journalism-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/multimedia-sports-journalism/',
    'https://www.northampton.ac.uk/study/courses/music-production-hnd/',
    'https://www.northampton.ac.uk/study/courses/occupational-therapy-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/paramedic-science-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/photography-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/photography-top-up-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/podiatry-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/policing-ba/',
    'https://www.northampton.ac.uk/study/courses/popular-music-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/pre-sessional-english-programme-pep/',
    'https://www.northampton.ac.uk/study/courses/product-design-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/product-design-hnd/',
    'https://www.northampton.ac.uk/study/courses/psychology-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/psychology-developmental-and-educational-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/psychology-and-counselling-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/social-care-and-community-practice-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/social-work-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/sociology-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/special-educational-needs-and-inclusion-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/sport-and-exercise-science-bsc-hons/',
    'https://www.northampton.ac.uk/study/courses/sport-development-and-physical-education-ba-hons/',
    'https://www.northampton.ac.uk/study/courses/theatre-practice-hnd/',
    'https://www.northampton.ac.uk/study/courses/travel-and-tourism-management-hnd/']
            listvalue = ['N420',
    'W410',
    'W411',
    'B700',
    '3 years BA Advertising & Digital Marketing (UCAS code N564) 4 years (with Foundation Year) BA Advertising & Digital Marketing (UCAS code N561)',
    'M212',
    'K210',
    '3 year BSc Banking and Financial Planning (UCAS code N390) 4 year (with Foundation Year) BSc Banking and Financial Planning (UCAS code N391)',
    'C100',
    '001N',
    'N250',
    'G503',
    '205G',
    '205G',
    'IN21',
    'N000',
    '3 year BA Business Entrepreneurship (UCAS code NN13)  4 year (with Foundation Year) BA Business Entrepreneurship (UCAS code NN14)',
    '3 year BA Business Studies (UCAS code N100)​ 4 year (with Foundation Year) BA Business Studies (UCAS code N101)',
    'B702',
    'L590',
    '056W',
    '016I',
    'II67',
    'G421',
    'G400',
    '204G',
    'I120',
    'I200',
    'G450',
    'G420',
    'G600',
    'G451',
    'P390',
    'W800',
    '3 year BA Professional Investigative Practice (UCAS code L438) 4 year (with Foundation Year) BA Professional Investigative Practice (UCAS code L430)​',
    'M930',
    'B750',
    '216W',
    'W400',
    'X310',
    'None',
    'L101/L102',
    'X301',
    '001H',
    'H100',
    'H10A',
    'Q300',
    'F750',
    '3 year BA Events Management (UCAS code N820) 4 year (with Foundation Year) BA Events Management (UCAS code N822)​',
    'N821',
    'W230',
    'W231',
    '3 year BA Fashion Marketing (UCAS code NWM2) 4 year (with Foundation Year) BA Fashion Marketing (UCAS code NWM3)​',
    'N560',
    'W101',
    'W120',
    'W232',
    'I630',
    'F800',
    'L700',
    'F640',
    'W210',
    'L512',
    'V100',
    '3 year BSc Human Bioscience (UCAS code B190) 4 year (with Foundation Year) BSc Human Bioscience (UCAS code B191)​',
    '3 year BA Human Resource Management (UCAS code N600) 4 year (with Foundation Year) BA Human Resource Management ​(UCAS code N601)​',
    'None',
    'W220',
    'W250',
    'None',
    '3 year BA International Business (UCAS code N121) 4 year (with Foundation Year) BA International Business (UCAS code N122)​',
    'None',
    '3 year BA International Development (UCAS code L901) 4 year (with Foundation Year) BA International Development (UCAS code L902)​',
    'N862',
    'JN93',
    'None',
    '3 year BA International Tourism Management (UCAS code N830) 4 year (with Foundation Year) BA International Tourism Management (UCAS code N831)​',
    'N800',
    '3 year LLB Law (UCAS code M100) 4 year (with Foundation Year) LLB Law (UCAS code M102)',
    'None',
    'None',
    'B703',
    'W220',
    'J430',
    'J43D',
    'None',
    'None',
    'N200',
    '3 year BSc Marketing Management (UCAS code N500) 4 year (with Foundation Year) BSc Marketing Management (UCAS code N502)​',
    'N501',
    'None',
    'B710',
    'P500',
    'P590',
    'O93W',
    'B930',
    'B950',
    'W640',
    'W641',
    'B985',
    'N478',
    'W340',
    'None',
    'W240',
    '042W',
    '3 year BSc Psychology (UCAS code C800) 4 year (with Foundation Year) BSc Psychology (UCAS code C801)​',
    'C891',
    'BC98',
    'L540',
    'L500',
    '3 year BA Sociology (UCAS code L300) 4 year (with Foundation Year) BA Sociology (UCAS code L301)​',
    'X360',
    'C600/C603',
    'year BA Sport Development and Physical Education (UCAS code C602) 4 year (with Foundation Year) BA Sport Development and Physical Education (UCAS code C604)​',
    '044W',
    'None']
            dd = {}
            for i in range(len(list1)):
                dd[list1[i]] = listvalue[i]
                ucascode = dd.get(url)
        except:
            ucascode = ''


        #10.overview_en
        overview_en = response.xpath('//*[@id="overview"]/div[2]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #11.modules_en
        modules_en = response.xpath('//*[@id="main"]/div[1]/section[5]/div/div/div[1]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)

        # print(modules_en)

        #12.career_en
        career_en = response.xpath('//*[@id="careers"]/div[1]/p').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #13.apply_proces_en
        apply_proces_en = 'http://www.northampton.ac.uk/study/how-to-apply/'

        #14.apply_proces_en
        apply_proces_en = response.xpath('//*[@id="entry-requirements"]/div[1]/p').extract()
        apply_proces_en = ''.join(apply_proces_en)
        apply_proces_en = remove_class(apply_proces_en)
        # print(apply_proces_en)

        #15.ielts 16171819
        ielts = 6.0
        ielts_r = 6.0
        ielts_s = 6.0
        ielts_w = 6.0
        ielts_l = 6.0
        # print(ielts,ielts_r,ielts_s,ielts_w,ielts_l)

        #20.tuition_fee
        tuition_fee = response.xpath('//*[@id="fees-and-funding"]').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #21.tuition_fee_pre
        tuition_fee_pre = "£"

        #22.apply_pre
        apply_pre = '£'

        #23.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'Assessments')]//following-sibling::*").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #24.alevel
        alevel = apply_proces_en

        item['alevel'] = alevel
        item['assessment_en'] = assessment_en
        item['ucascode'] = ucascode
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_name'] = degree_name
        item['degree_type'] = degree_type
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['start_date'] = start_date
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['apply_proces_en'] = apply_proces_en
        item['apply_proces_en'] = apply_proces_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['tuition_fee_pre'] = tuition_fee_pre
        item['tuition_fee'] = tuition_fee
        yield  item