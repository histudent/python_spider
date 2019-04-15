# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/6/29 10:50'
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
from scrapySchool_England.clearSpace import clear_space_str
class GoldSmithUniversityofLondonSpider(scrapy.Spider):
    name = 'GoldSmithUniversityofLondon_p'
    allowed_domains = ['gold.ac.uk/']
    start_urls = []
    C= [
        'https://www.gold.ac.uk/pg/ma-education-culture-language-identity/',
        'https://www.gold.ac.uk/pg/ma-dramaturgy-writing-performance/',
        'https://www.gold.ac.uk/pg/ma-filmmaking-editing/',
        'https://www.gold.ac.uk/pg/ma-film-screen-studies/',
        'https://www.gold.ac.uk/pg/ma-filmmaking-cinematography/',
        'https://www.gold.ac.uk/pg/ma-filmmaking-directing-fiction/',
        'https://www.gold.ac.uk/pg/ma-filmmaking-producing/',
        'https://www.gold.ac.uk/pg/ma-filmmaking-screen-documentary/',
        'https://www.gold.ac.uk/pg/ma-filmmaking/',
        'https://www.gold.ac.uk/pg/ma-events-experience-management/',
        'https://www.gold.ac.uk/pg/ma-anthropology-cultural-politics/',
        'https://www.gold.ac.uk/pg/ma-applied-anthropology-community-arts/',
        'https://www.gold.ac.uk/pg/ma-anthropology-museum-practice/',
        'https://www.gold.ac.uk/pg/ma-applied-anthropology-community-youth-work/',
        'https://www.gold.ac.uk/pg/ma-filmmaking-sound-recording-design/',
        'https://www.gold.ac.uk/pg/ma-applied-anthropology-community-development/',
        'https://www.gold.ac.uk/pg/ma-art-politics/',
        'https://www.gold.ac.uk/pg/ma-applied-theatre/',
        'https://www.gold.ac.uk/pg/ma-music-musicology/',
        'https://www.gold.ac.uk/pg/ma-art-psychotherapy/',
        'https://www.gold.ac.uk/pg/ma-music-general/',
        'https://www.gold.ac.uk/pg/ma-music-ethnomusicology/',
        'https://www.gold.ac.uk/pg/ma-music-popular-music-research/',
        'https://www.gold.ac.uk/pg/ma-performance-culture/',
        'https://www.gold.ac.uk/pg/ma-performance-making/',
        'https://www.gold.ac.uk/pg/ma-musical-theatre/',
        'https://www.gold.ac.uk/pg/ma-photography-urban-cultures/',
        'https://www.gold.ac.uk/pg/ma-photography-electronic-arts/',
        'https://www.gold.ac.uk/pg/ma-gender-media-culture/',
        'https://www.gold.ac.uk/pg/ma-global-media-transnational-communications/',
        'https://www.gold.ac.uk/pg/ma-history/',
        'https://www.gold.ac.uk/pg/ma-human-rights/',
        'https://www.gold.ac.uk/pg/ma-independent-games-design/',
        'https://www.gold.ac.uk/pg/ma-international-relations/',
        'https://www.gold.ac.uk/pg/ma-journalism/',
        'https://www.gold.ac.uk/pg/ma-literary-studies/',
        'https://www.gold.ac.uk/pg/ma-literary-studies/american-literature-and-culture/',
        'https://www.gold.ac.uk/pg/ma-literary-studies/comparative-literature-and-criticism/',
        'https://www.gold.ac.uk/pg/ma-literary-studies/critical-theory/',
        'https://www.gold.ac.uk/pg/ma-literary-studies/literature-of-the-caribbean-and-its-diasporas/',
        'https://www.gold.ac.uk/pg/ma-literary-studies/modern-literature/',
        'https://www.gold.ac.uk/pg/ma-literary-studies/romantic-and-victorian-literature-and-culture/',
        'https://www.gold.ac.uk/pg/ma-literary-studies/shakespeare-early-modern/',
        'https://www.gold.ac.uk/pg/ma-luxury-brand-management/',
        'https://www.gold.ac.uk/pg/ma-media-communications/',
        'https://www.gold.ac.uk/pg/ma-migration-mobility/',
        'https://www.gold.ac.uk/pg/ma-multilingualism-linguistics-education/',
        'https://www.gold.ac.uk/pg/ma-music-contemporary-music-studies/',
        'https://www.gold.ac.uk/pg/ma-artists-film-moving-image/',
        'https://www.gold.ac.uk/pg/ma-arts-admin-cultural-policy/',
        'https://www.gold.ac.uk/pg/ma-arts-admin-cultural-policy-music-pathway/',
        'https://www.gold.ac.uk/pg/ma-arts-learning/',
        'https://www.gold.ac.uk/pg/ma-black-british-writing/',
        'https://www.gold.ac.uk/pg/ma-brands-communication-culture/',
        'https://www.gold.ac.uk/pg/ma-childrens-literature/',
        'https://www.gold.ac.uk/pg/ma-childrens-literature-illustration/',
        'https://www.gold.ac.uk/pg/ma-cities-society/',
        'https://www.gold.ac.uk/pg/ma-computational-arts/',
        'https://www.gold.ac.uk/pg/ma-creative-cultural-entrepreneurship-theatre/',
        'https://www.gold.ac.uk/pg/ma-creative-life-writing/',
        'https://www.gold.ac.uk/pg/ma-creative-writing-education/',
        'https://www.gold.ac.uk/pg/ma-critical-creative-analysis/',
        'https://www.gold.ac.uk/pg/ma-cultural-policy-relations/',
        'https://www.gold.ac.uk/pg/ma-cultural-studies/',
        'https://www.gold.ac.uk/pg/ma-culture-industry/',
        'https://www.gold.ac.uk/pg/ma-dance-movement-psychotherapy/',
        'https://www.gold.ac.uk/pg/ma-design-expanded-practice/',
        'https://www.gold.ac.uk/pg/ma-digital-media-technology-cultural-form/',
        'https://www.gold.ac.uk/pg/ma-social-anthropology/',
        'https://www.gold.ac.uk/pg/ma-social-entrepreneurship/',
        'https://www.gold.ac.uk/pg/ma-social-work/',
        'https://www.gold.ac.uk/pg/ma-sociocultural-linguistics/',
        'https://www.gold.ac.uk/pg/ma-tv-journalism/',
        'https://www.gold.ac.uk/pg/ma-tourism-cultural-policy/',
        'https://www.gold.ac.uk/pg/ma-translation/',
        'https://www.gold.ac.uk/pg/ma-understanding-domestic-violence-and-sexual-abuse/',
        'https://www.gold.ac.uk/pg/mmus-performance/',
        'https://www.gold.ac.uk/pg/mmus-popular-music/',
        'https://www.gold.ac.uk/pg/mmus-sonic-arts/',
        'https://www.gold.ac.uk/pg/ma-political-communications/',
        'https://www.gold.ac.uk/pg/ma-politics-development-global-south/',
        'https://www.gold.ac.uk/pg/ma-postcolonial-culture-global-policy/',
        'https://www.gold.ac.uk/pg/ma-promotional-media/',
        'https://www.gold.ac.uk/pg/ma-queer-history/',
        'https://www.gold.ac.uk/pg/ma-race-media-social-justice/',
        'https://www.gold.ac.uk/pg/ma-radio/',
        'https://www.gold.ac.uk/pg/ma-research-architecture/',
        'https://www.gold.ac.uk/pg/ma-script-writing/',
        'https://www.gold.ac.uk/pg/ma-creative-cultural-entrepreneurship-comp/',
        'https://www.gold.ac.uk/pg/ma-computer-games-art-design/',
        'https://www.gold.ac.uk/pg/ma-contemporary-art-theory/',
        'https://www.gold.ac.uk/pg/ma-counselling/',
        'https://www.gold.ac.uk/pg/ma-creative-cultural-entrepreneurship/',
        'https://www.gold.ac.uk/pg/ma-creative-cultural-entrepreneurship-fashion/',
        'https://www.gold.ac.uk/pg/ma-creative-cultural-entrepreneurship-media/',
        'https://www.gold.ac.uk/pg/ma-creative-cultural-entrepreneurship-leadership/',
        'https://www.gold.ac.uk/pg/ma-creative-cultural-entrepreneurship-music/',
        'https://www.gold.ac.uk/pg/ma-visual-anthropology/',
        'https://www.gold.ac.uk/pg/ma-visual-sociology/',
        'https://www.gold.ac.uk/pg/ma-world-theatres/',
        'https://www.gold.ac.uk/pg/ma-creative-cultural-entrepreneurship-design/',
        'https://www.gold.ac.uk/pg/ma-digital-journalism/',
        'https://www.gold.ac.uk/pg/mfa-computational-arts/',
        'https://www.gold.ac.uk/pg/mfa-curating/',
        'https://www.gold.ac.uk/pg/mfa-fine-art/',
        'https://www.gold.ac.uk/pg/mmus-composition/',
        'https://www.gold.ac.uk/pg/mmus-creative-practice/',
        'https://www.gold.ac.uk/pg/msc-cognitive-clinical-neuroscience/',
        'https://www.gold.ac.uk/pg/msc-computational-cognitive-neuroscience/',
        'https://www.gold.ac.uk/pg/msc-consumer-behaviour/',
        'https://www.gold.ac.uk/pg/msc-occupational-psychology/',
        'https://www.gold.ac.uk/pg/msc-psychology-arts-neuroaesthetics-creativity/',
        'https://www.gold.ac.uk/pg/msc-data-science/',
        'https://www.gold.ac.uk/pg/msc-forensic-psychology/',
        'https://www.gold.ac.uk/pg/msc-clinical-psychology-health-services/',
        'https://www.gold.ac.uk/pg/msc-management-innovation/',
        'https://www.gold.ac.uk/pg/msc-marketing-technology/',
        'https://www.gold.ac.uk/pg/msc-music-mind-brain/',
        'https://www.gold.ac.uk/pg/msc-cognitive-behavioural-therapy/',
        'https://www.gold.ac.uk/pg/msc-social-research/',
        'https://www.gold.ac.uk/pg/msc-psychology-social-relations/'
    ]
    for i in C:
        start_urls.append(i)
    # for i in range(1,172,10):
    #     base_url = 'https://www.gold.ac.uk/course-finder/results/?collection=goldsmiths-courses&sort=Title&f.Level|level=Postgraduate&start_rank='+ str(i)
    #     start_urls.append(base_url)
    # def parse(self, response):
    #     pass
    #     item = get_item1(ScrapyschoolEnglandItem1)
    #     url = response.xpath('//*[@id="maincontent"]/section[2]/div[1]/section/div/div/article/div/h3/a/@title').extract()    #     print(url)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        # 1.university
        university = 'Goldsmiths, University of London'
        # print(university)

        # 2.department
        try:
            department = response.xpath('//*[@id="maincontent"]/article/section[1]/div/div/div/div[1]/p/a').extract()
            department = ''.join(department)
            department = clear_space_str(department)
            department = remove_tags(department)
            # print(department)
        except:
            department = 'N/A'

        # 3.programme_en
        try:
            programme_en_a = response.xpath('//*[@id="maincontent"]/article/header/div/div/div/div[1]/div[1]/div/h1/span').extract()
            programme_en_a = ''.join(programme_en_a)
            # programme_en_a = clear_space_str(programme_en_a)
            programme_en_a = remove_tags(programme_en_a)
            # programme_en_a = programme_en_a.replace('&amp','')
            # print(programme_en)
        except:
            programme_en = 'N/A'
        programme_en = programme_en_a.split()[2:]
        programme_en = ' '.join(programme_en)
        if ';'in programme_en:
            programme_en = programme_en.replace(';',' ')
        if 'in ' in programme_en:
            programme_en = programme_en.replace('in ','')
        programme_en = programme_en.strip()
        # print(programme_en,response.url)


        # 4.overview_en
        try:
            overview_en = response.xpath('//*[@id="maincontent"]/article/section[2]/div/div/div').extract()
            overview_en = ''.join(overview_en)
            overview_en = clear_space_str(overview_en)
            overview_en = remove_class(overview_en)
            # print(overview_en)
        except:
            overview = 'N/A'

        # 5.duration
        try:
            duration = response.xpath('//*[@id="maincontent"]/article/section[1]/div/div/div/div[2]/p').extract()
            duration = ''.join(duration)
            duration = re.findall('\d',duration)[0]
            duration = remove_tags(duration)
            # print(duration)
        except:
            duration = None

        #6.duration_per
        duration_per = 1

        # 7.modules_en
        try:
            modules_en  = response.xpath('//*[@id="maincontent"]/article/section[3]/div/div').extract()
            modules_en  = ''.join(modules_en)
            modules_en = remove_class(modules_en)
            modules_en  = clear_space_str(modules_en)
        except:
            modules_en= 'N/A'

        # 8.career_en
        try:
            career_en = response.xpath('//*[@id="maincontent"]/article/section[7]/div/div').extract()
            career_en = ''.join(career_en)
            career_en = remove_class(career_en)
            career_en = clear_space_str(career_en)
            # print(career_en)
        except:
            career_en = 'N/A'

        # 9.other
        other = 'https://www.gold.ac.uk/media/study-section/fees/PG-Fees-1819.pdf'

        #10.apply_proces_en
        apply_proces_en = response.xpath('//*[@id="maincontent"]/article/section[6]/div/div').extract()
        apply_proces_en = ''.join(apply_proces_en)
        apply_proces_en = clear_space_str(apply_proces_en)
        apply_proces_en = remove_class(apply_proces_en)
        # print(apply_proces_en)

        # 11.-15.雅思(听说读写)
        try:
            IELTS_list = response.xpath(
                '//h3[contains(text(),"International qualifications")]/following-sibling::p').extract()
            IELTS_list = ''.join(IELTS_list)
            IELTS_list = remove_tags(IELTS_list)
            pat = re.findall('\d\.\d', IELTS_list)

            if len(pat) == 3:
                ielts = pat[0]
                ielts_w = pat[1]
                ielts_r = pat[2]
                ielts_s = pat[2]
                ielts_l= pat[2]
            elif len(pat) == 2:
                ielts = pat[0]
                ielts_w = pat[1]
                ielts_r = None
                ielts_s = None
                ielts_l = None
            else:
                ielts = 6.5
                ielts_w = 6.0
                ielts_r = 6.0
                ielts_s = 6.0
                ielts_l = 6.0
            ielts = clear_space_str(ielts)
            ielts_r = clear_space_str(ielts_r)
            ielts_w = clear_space_str(ielts_w)
            ielts_s = clear_space_str(ielts_s)
            ielts_l = clear_space_str(ielts_l)
            # print(ielts)
            # print(ielts_r,ielts_w,ielts_s,ielts_l)
        except:
            ielts = 6.5
            ielts_w = 6.0
            ielts_r = 6.0
            ielts_s = 6.0
            ielts_l = 6.0

        # 14.rntry_requirements
        rntry_requirements =response.xpath('//*[@id="maincontent"]/article/section[4]/div/div').extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        # 15.apply_documents_en
        try:
            apply_documents_en = response.xpath(
                '//h3[contains(text(),"When to apply")]/preceding-sibling::ul').extract()
            apply_documents_en = ''.join(apply_documents_en)
            apply_documents_en = clear_space_str(apply_documents_en)
            apply_documents_en = remove_class(apply_documents_en)
            # print(apply_documents_en)
        except:
            apply_documents_en = 'N/A'


        # 16.url
        url = response.url
        # print(url)

        #17.degree_type
        degree_type = 2

        #18.degree_name
        if 'MA' in programme_en_a:
            degree_name = 'MA'
        elif 'MSc' in programme_en_a:
            degree_name = 'MSc'
        elif 'PGCert' in programme_en_a:
            degree_name = 'PGCert'
        elif 'MMus' in programme_en_a:
            degree_name = 'MMus'
        elif 'MRes' in programme_en_a:
            degree_name = 'MRes'
        elif 'MPhil' in programme_en_a:
            degree_name = 'MPhil'
        elif 'MFA' in programme_en_a:
            degree_name = 'MFA'
        elif 'MMus' in programme_en_a:
            degree_name = 'MMus'
        elif 'PhD' in programme_en_a:
            degree_name = 'PhD'
        else:
            degree_name = 'Graduate'
        # print(degree_name)

        #19.location
        location = 'London'

        #20.apply_pre
        apply_pre  = '£'


        #21.require_chinese_en
        require_chinese_en = '<p>Postgraduate taught For entry to postgraduate programmes you will normally need a Bachelors degree in relevant subject. Refer to individual course pages to see whether there are any additional application requirements.Research degrees You will normally need to have completed a Masters degree in a subject relevant to your proposed postgraduate study. There may also be other specific entrance requirements. You can refer to individual course pages to find out what these are.</p>"'

        #22.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'Assessment')]//following-sibling::*").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en,url)

        item['assessment_en'] = assessment_en
        item['require_chinese_en'] = require_chinese_en
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['department'] = department
        item['programme_en'] = programme_en
        item['overview_en'] = overview_en
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['other'] = other
        item['apply_proces_en'] = apply_proces_en
        item['ielts'] = ielts
        item['ielts_w'] = ielts_w
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['rntry_requirements'] = rntry_requirements
        item['apply_documents_en'] = apply_documents_en
        item['url'] = url
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['location'] = location
        yield  item