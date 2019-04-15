# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/9 13:28'
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
class UniversityofBrightonSpider(scrapy.Spider):
    name = 'UniversityofBrighton_u'
    allowed_domains = ['brighton.ac.uk/']
    start_urls = []
    C = [
        'https://www.brighton.ac.uk/courses/study/music-business-media-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/philosophy-politics-and-ethics-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/history-literature-and-culture-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/globalisation-history-politics-culture-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/critical-history-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/humanities-war-conflict-and-modernity-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/architectural-technology-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/building-surveying-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/pharmaceutical-and-chemical-sciences-bsc-hons-with-integrated-foundation-year.aspx',
        'https://www.brighton.ac.uk/courses/study/quantity-surveying-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/pharmaceutical-and-chemical-sciences-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/physical-education-ba-hons-with-qts.aspx',
        'https://www.brighton.ac.uk/courses/study/sport-studies-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/history-of-art-and-design-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/visual-culture-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/philosophy-politics-art-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/marketing-management-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/marketing-management-with-placement-year-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/business-management-with-marketing-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/business-management-with-human-resource-management-and-placement-year-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/business-management-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/business-management-with-economics-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/business-management-with-finance-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/business-management-with-human-resources-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/business-management-with-finance-and-placement-year-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/business-management-with-economics-and-placement-year-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/business-management-with-marketing-and-placement-year-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/international-business-management-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/business-management-with-placement-year-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/media-industry-and-innovation-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/international-hospitality-management-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/podiatry-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/medicine-bm-bs.aspx',
        'https://www.brighton.ac.uk/courses/study/computing-for-web-and-mobile-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/computer-science-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/business-computing-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/business-computing-with-cyber-security-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/software-engineering-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/construction-management-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/civil-engineering-with-construction-management-meng.aspx',
        'https://www.brighton.ac.uk/courses/study/civil-engineering-meng-with-integrated-foundation-year.aspx',
        'https://www.brighton.ac.uk/courses/study/aeronautical-engineering-beng-hons-with-integrated-foundation-year.aspx',
        'https://www.brighton.ac.uk/courses/study/mechanical-engineering-beng-hons-with-integrated-foundation-year.aspx',
        'https://www.brighton.ac.uk/courses/study/automotive-engineering-beng-hons-with-integrated-foundation-year.aspx',
        'https://www.brighton.ac.uk/courses/study/electronic-and-computer-engineering-beng-hons-with-integrated-foundation-year.aspx',
        'https://www.brighton.ac.uk/courses/study/electrical-and-electronic-engineering-beng-hons-with-integrated-foundation-year.aspx',
        'https://www.brighton.ac.uk/courses/study/media-studies-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/3d-design-and-craft-mdes.aspx',
        'https://www.brighton.ac.uk/courses/study/3d-design-and-craft-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/interior-architecture-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/design-for-digital-media-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/mechanical-engineering-meng.aspx',
        'https://www.brighton.ac.uk/courses/study/aeronautical-engineering-meng.aspx',
        'https://www.brighton.ac.uk/courses/study/automotive-engineering-beng-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/aeronautical-engineering-beng-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/automotive-engineering-meng.aspx',
        'https://www.brighton.ac.uk/courses/study/media-and-english-literature-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/mathematics-with-finance-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/mathematics-with-business-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/mathematics-for-data-science-mmath.aspx',
        'https://www.brighton.ac.uk/courses/study/mathematics-mmath.aspx',
        'https://www.brighton.ac.uk/courses/study/media-and-environmental-communication-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/geography-with-geoinformatics-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/english-literature-and-linguistics-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/geology-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/mechanical-engineering-beng-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/ecology-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/ecology-bsc-hons-with-integrated-foundation-year.aspx',
        'https://www.brighton.ac.uk/courses/study/ecology-msci.aspx',
        'https://www.brighton.ac.uk/courses/study/primary-mathematics-education-ba-hons-with-qts.aspx',
        'https://www.brighton.ac.uk/courses/study/primary-education-3-7-years-ba-hons-with-qts.aspx',
        'https://www.brighton.ac.uk/courses/study/primary-education-5-11-years-ba-hons-with-qts.aspx',
        'https://www.brighton.ac.uk/courses/study/primary-english-education-ba-hons-with-qts.aspx',
        'https://www.brighton.ac.uk/courses/study/electrical-and-electronic-engineering-meng.aspx',
        'https://www.brighton.ac.uk/courses/study/electronic-and-computer-engineering-beng-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/electronic-and-computer-engineering-meng.aspx',
        'https://www.brighton.ac.uk/courses/study/electrical-and-electronic-engineering-beng-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/environmental-sciences-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/biomedical-science-msci.aspx',
        'https://www.brighton.ac.uk/courses/study/biomedical-science-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/architecture-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/accounting-and-finance-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/physical-education-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/biomedical-science-bsc-hons-with-integrated-foundation-year.aspx',
        'https://www.brighton.ac.uk/courses/study/pharmacy-mpharm-with-integrated-foundation-year.aspx',
        'https://www.brighton.ac.uk/courses/study/sport-coaching-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/computer-science-with-artificial-intelligence-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/geology-mgeol.aspx',
        'https://www.brighton.ac.uk/courses/study/geography-with-archaeology-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/geography-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/geography-mgeog.aspx',
        'https://www.brighton.ac.uk/courses/study/linguistics-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/international-tourism-management-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/geography-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/civil-engineering-meng.aspx',
        'https://www.brighton.ac.uk/courses/study/civil-engineering-with-construction-management-beng-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/civil-with-environmental-engineering-beng-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/civil-engineering-beng-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/graphic-design-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/pharmacy-mpharm.aspx',
        'https://www.brighton.ac.uk/courses/study/mathematics-bsc-hons-with-integrated-foundation-year.aspx',
        'https://www.brighton.ac.uk/courses/study/applied-psychology-and-sociology-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/applied-psychology-and-criminology-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/economics-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/journalism-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/public-health-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/computer-science-for-games-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/digital-games-development-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/social-policy-and-practice-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/criminology-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/criminology-and-sociology-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/social-work-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/illustration-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/chemistry-mchem.aspx',
        'https://www.brighton.ac.uk/courses/study/chemistry-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/chemistry-bsc-hons-with-integrated-foundation-year.aspx',
        'https://www.brighton.ac.uk/courses/study/finance-and-investment-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/law-llb-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/early-childhood-education-and-care-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/fashion-with-business-studies-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/textiles-with-business-studies-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/textiles-with-business-studies-mdes.aspx',
        'https://www.brighton.ac.uk/courses/study/mathematics-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/mathematics-with-economics-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/secondary-mathematics-education-11-18-years-bsc-with-qts.aspx',
        'https://www.brighton.ac.uk/courses/study/secondary-mathematics-education-ba-hons-with-qts.aspx',
        'https://www.brighton.ac.uk/courses/study/media-production-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/fashion-and-dress-history-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/sport-journalism-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/earth-and-ocean-science-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/sport-business-management-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/humanities-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/moving-image-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/photography-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/digital-music-and-sound-arts-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/creative-writing-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/english-literature-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/english-literature-and-creative-writing-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/english-language-and-creative-writing-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/product-design-with-professional-experience-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/product-design-technology-with-professional-experience-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/project-management-for-construction-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/applied-psychology-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/law-with-criminology-llb-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/law-with-business-llb-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/biological-sciences-bsc-hons-with-integrated-foundation-year.aspx',
        'https://www.brighton.ac.uk/courses/study/biological-sciences-msci.aspx',
        'https://www.brighton.ac.uk/courses/study/biological-sciences-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/film-and-screen-studies-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/social-science-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/politics-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/sociology-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/sport-and-exercise-science-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/civil-with-environmental-engineering-meng.aspx',
        'https://www.brighton.ac.uk/courses/study/english-language-and-media-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/fine-art-painting-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/fine-art-printmaking-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/fine-art-sculpture-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/fashion-communication-with-business-studies-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/physical-geography-and-geology-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/fine-art-critical-practice-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/physiotherapy-bsc-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/english-language-and-linguistics-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/english-language-and-english-literature-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/english-language-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/international-event-management-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/education-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/multimedia-broadcast-journalism-ba-hons.aspx',
        'https://www.brighton.ac.uk/courses/study/digital-film-ba-hons.aspx'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Brighton'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="page-heading"]/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 1

        #5.degree_name
        if ' BEng(Hons)' in programme_en:
            degree_name = ' BEng(Hons)'
        elif ' MEng' in programme_en:
            degree_name = ' MEng'
        elif ' MDes' in programme_en:
            degree_name = ' MDes'
        elif ' BA(Hons)' in programme_en:
            degree_name = ' BA(Hons)'
        elif ' BSc(Hons)' in programme_en:
            degree_name = ' BSc(Hons)'
        elif ' MSci' in programme_en:
            degree_name = ' MSci'
        elif ' MChem' in programme_en:
            degree_name = ' MChem'
        elif ' MGeog' in programme_en:
            degree_name = ' MGeog'
        elif ' MGeol' in programme_en:
            degree_name = ' MGeol'
        elif ' LLB(Hons)' in programme_en:
            degree_name = ' LLB(Hons)'
        elif ' MMath' in programme_en:
            degree_name = ' MMath'
        elif ' MPharm' in programme_en:
            degree_name = ' MPharm'
        else:
            degree_name = ''
        programme_en = programme_en.replace(degree_name,'').strip()
        degree_name = degree_name.strip()
        # print(programme_en)
        # print(degree_name)

        #6.ucascode
        ucascode = response.xpath("//*[contains(text(),'UCAS code')]/..").extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode)
        ucascode = ucascode.replace('UCAS code','').strip()
        if len(ucascode)>299:
            ucascode = ''
        # print(ucascode)

        #7.overview_en
        overview_en = response.xpath('//*[@id="summary"]/div/div/div[2]').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #8.location
        location = response.xpath("//*[contains(text(),'Key facts')]//following-sibling::p[1]/text()").extract()
        location = ''.join(location)
        location =remove_tags(location).strip()
        # print(location)

        #9.duration  #10.duration_per
        duration = response.xpath('//*[@id="summary"]/div/div/div[3]/div[1]/p[3]/text()[1]').extract()
        duration = ''.join(duration)
        duration = remove_tags(duration).strip()
        duration_per = 1
        # print(duration,duration_per)

        #11.apply_desc_en
        apply_desc_en = response.xpath("//section[@id='entry']").extract()
        apply_desc_en = ''.join(apply_desc_en)
        apply_desc_en = remove_class(apply_desc_en)
        # print(apply_desc_en)

        #12.ielts 13141516
        ielts_list = response.xpath("//section[@id='entry']").extract()
        ielts_list = ''.join(ielts_list)
        ielts_list = remove_tags(ielts_list)
        # print(ielts_list)
        try:
            ielts = re.findall(r'[567]\.\d',ielts_list)
        except:
            ielts = None
        # print(ielts,response.url)
        try:
            if len(ielts) ==3:
                a = ielts[0]
                b = ielts[1]
                c = ielts[2]
                ielts = a
                ielts_w = b
                ielts_r = c
                ielts_l = c
                ielts_s = c
            elif len(ielts) ==2:
                a = ielts[0]
                b = ielts[1]
                ielts = a
                ielts_w = b
                ielts_r = b
                ielts_l = b
                ielts_s = b
            elif len(ielts) ==1:
                a= ielts[0]
                ielts = a
                ielts_w = int(a)- 0.5
                ielts_r = int(a)- 0.5
                ielts_l = int(a)- 0.5
                ielts_s = int(a)- 0.5
            else:
                ielts = 6.5
                ielts_w = 6.0
                ielts_r = 6.0
                ielts_l = 6.0
                ielts_s = 6.0
        except:
            ielts = 6.5
            ielts_w = 6.0
            ielts_r = 6.0
            ielts_l = 6.0
            ielts_s = 6.0
        # print(ielts,ielts_l,ielts_r,ielts_w,ielts_s)

        #17.modules_en
        modules_en = response.xpath("//h2[contains(text(),'Course in detail')]//following-sibling::*").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)


        #18.career_en
        career_en = response.xpath("//*[contains(text(),'Careers and employability')]/../following-sibling::*").extract()
        career_en =''.join(career_en)
        career_en = remove_class(career_en).strip()
        career_en = clear_space_str(career_en)
        # print(career_en)

        #19.tuition_fee
        tuition_fee= response.xpath("//*[contains(text(),'International')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_class(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # if tuition_fee ==0:
        #     print(response.url)
        # print(tuition_fee)

        #20.tuition_fee_pre
        tuition_fee_pre= '£'

        #21.alevel
        alevel = response.xpath("//*[contains(text(),'A-level')]//text()").extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel).strip()
        if len(alevel)>500:
            alevel = alevel[:500]
        # print(alevel)

        #22.apply_pre
        apply_pre = '£'

        #23.ib
        ib = response.xpath("//*[contains(text(),'International Baccalaureate')]/../text()").extract()
        ib = ''.join(ib)
        ib = remove_tags(ib).strip()
        # print(ib)

        item['ucascode'] = ucascode
        item['ib'] = ib
        item['alevel'] = alevel
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['location'] = location
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['apply_desc_en'] = apply_desc_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        yield item