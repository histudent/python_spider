# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/18 11:52'
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
    name = 'GoldSmithUniversityofLondon_u'
    allowed_domains = ['gold.ac.uk/']
    start_urls = []
    C= [
        'https://www.gold.ac.uk/ug/ba-anthropology/',
        'https://www.gold.ac.uk/ug/ba-anthropology-sociology/',
        'https://www.gold.ac.uk/ug/ba-anthropology-media/',
        'https://www.gold.ac.uk/ug/ba-anthropology-visual-practice/',
        'https://www.gold.ac.uk/ug/ba-arts-management/',
        'https://www.gold.ac.uk/ug/ba-community-youth-work/',
        'https://www.gold.ac.uk/ug/ba-curating/',
        'https://www.gold.ac.uk/ug/ba-criminology/',
        'https://www.gold.ac.uk/ug/ba-design/',
        'https://www.gold.ac.uk/ug/ba-drama-comedy-satire/',
        'https://www.gold.ac.uk/ug/ba-drama-musical-theatre/',
        'https://www.gold.ac.uk/ug/ba-drama-theatre-arts/',
        'https://www.gold.ac.uk/ug/ba-drama-performance-politics-society/',
        'https://www.gold.ac.uk/ug/ba-economics/',
        'https://www.gold.ac.uk/ug/ba-economics-politics-public/',
        'https://www.gold.ac.uk/ug/ba-education-culture-society/',
        'https://www.gold.ac.uk/ug/ba-english/',
        'https://www.gold.ac.uk/ug/ba-fine-art/',
        'https://www.gold.ac.uk/ug/ba-english-history/',
        'https://www.gold.ac.uk/ug/ba-english-american-literature/',
        'https://www.gold.ac.uk/ug/ba-english-comparative-literature/',
        'https://www.gold.ac.uk/ug/ba-english-creative-writing/',
        'https://www.gold.ac.uk/ug/ba-english-drama/',
        'https://www.gold.ac.uk/ug/ba-english-language-literature/',
        'https://www.gold.ac.uk/ug/ba-fine-art-extension/',
        'https://www.gold.ac.uk/ug/ba-history/',
        'https://www.gold.ac.uk/ug/ba-history-anthropology/',
        'https://www.gold.ac.uk/ug/ba-history-of-art/',
        'https://www.gold.ac.uk/ug/ba-fine-art-history-of-art/',
        'https://www.gold.ac.uk/ug/ba-history-journalism/',
        'https://www.gold.ac.uk/ug/ba-history-politics/',
        'https://www.gold.ac.uk/ug/ba-international-relations-chinese/',
        'https://www.gold.ac.uk/ug/ba-journalism/',
        'https://www.gold.ac.uk/ug/ba-international-relations/',
        'https://www.gold.ac.uk/ug/ba-media-sociology/',
        'https://www.gold.ac.uk/ug/ba-politics-international-relations/',
        'https://www.gold.ac.uk/ug/ba-media-communications/',
        'https://www.gold.ac.uk/ug/ba-media-english/',
        'https://www.gold.ac.uk/ug/ba-politics/',
        'https://www.gold.ac.uk/ug/ba-psychosocial-studies/',
        'https://www.gold.ac.uk/ug/ba-religion/',
        'https://www.gold.ac.uk/ug/ba-politics-philosophy-economics/',
        'https://www.gold.ac.uk/ug/ba-sociology-chinese/',
        'https://www.gold.ac.uk/ug/ba-sociology-criminology/',
        'https://www.gold.ac.uk/ug/ba-social-work/',
        'https://www.gold.ac.uk/ug/ba-sociology/',
        'https://www.gold.ac.uk/ug/ba-sociology-politics/',
        'https://www.gold.ac.uk/ug/bmus-music/',
        'https://www.gold.ac.uk/ug/bmus-popular-music/',
        'https://www.gold.ac.uk/ug/bsc-computer-science/',
        'https://www.gold.ac.uk/ug/bsc-business-computing-entrepreneurship/',
        'https://www.gold.ac.uk/ug/bsc-creative-computing/',
        'https://www.gold.ac.uk/ug/bsc-digital-arts-computing/',
        'https://www.gold.ac.uk/ug/bsc-economics-econometrics/',
        'https://www.gold.ac.uk/ug/bsc-management-marketing/',
        'https://www.gold.ac.uk/ug/bsc-management-economics/',
        'https://www.gold.ac.uk/ug/bsc-games-programming/',
        'https://www.gold.ac.uk/ug/bsc-management-with-entrepreneurship/',
        'https://www.gold.ac.uk/ug/bsc-marketing/',
        'https://www.gold.ac.uk/ug/bsc-psychology/',
        'https://www.gold.ac.uk/ug/bsc-clinical-psychology/',
        'https://www.gold.ac.uk/ug/bsc-psychology-forensic-psychology/',
        'https://www.gold.ac.uk/ug/bsc-psychology-cognitive-neuroscience/',
        'https://www.gold.ac.uk/ug/bsc-psychology-management/',
        'https://www.gold.ac.uk/ug/integrated-degree-anthropology/',
        'https://www.gold.ac.uk/ug/integrated-degree-history/',
        'https://www.gold.ac.uk/ug/integrated-degree-english/',
        'https://www.gold.ac.uk/ug/integrated-degree-psychology/',
        'https://www.gold.ac.uk/ug/integrated-degree-media/',
        'https://www.gold.ac.uk/ug/llb-law/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        # 1.university
        university = 'Goldsmiths, University of London'
        # print(university)

        # 2.department
        try:
            department = response.xpath("//*[contains(text(),'Department')]//following-sibling::p").extract()[0]
            department = ''.join(department)
            department = clear_space_str(department)
            department = remove_tags(department)
        except:
            department = 'N/A'
        # print(department)

        # 3.programme_en
        try:
            programme_e = response.xpath('//*[@id="maincontent"]/article//header//h1/span/span').extract()
            programme_e = ''.join(programme_e)
            programme_e = clear_space_str(programme_e)
            programme_e = remove_tags(programme_e)
            programme_e = programme_e.replace('&amp','')
            # print(programme_e)
        except:
            programme_e= 'N/A'
        programme_en = programme_e.split()[2:]
        programme_en = ' '.join(programme_en)
        if 'in' in programme_en:
            programme_en = programme_en.replace('in','').strip()
        else:pass
        # print(programme_en)

        # 4.overview_en
        try:
            overview_en = response.xpath('//*[@id="maincontent"]/article/section[2]/div/div/div').extract()
            overview_en = ''.join(overview_en)
            overview_en = clear_space_str(overview_en)
            overview_en = remove_class(overview_en)
            #
        except:
            overview = 'N/A'
        # print(overview_en)

        # 5.duration
        try:
            duration = response.xpath("//*[contains(text(),'Length')]//following-sibling::p").extract()
            duration = ''.join(duration)
            duration = re.findall('\d',duration)[0]
            duration = remove_tags(duration)
            # print(duration)
        except:
            duration = None
        # print(duration)

        #6.duration_per
        duration_per = 1

        # 7.modules_en

        modules_en  = response.xpath('//h2[contains(text(),"ll study")]/../../../following-sibling::div').extract()
        modules_en  = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # modules_en  = clear_space_str(modules_en)

        # print(modules_en)

        # 8.career_en
        try:
            career_en = response.xpath('//*[@id="maincontent"]/article/section[6]/div/div').extract()
            career_en = ''.join(career_en)
            career_en = remove_class(career_en)
            career_en = clear_space_str(career_en)
            #
        except:
            career_en = 'N/A'
        # print(career_en)

        # 9.other
        other = 'https://www.gold.ac.uk/ug/fees-funding/'

        #10.alevel
        alevel = response.xpath("//*[contains(text(),'A-level:')]//text()[1]").extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel).replace('A-level:','').strip()
        # print(alevel)

        #11.ucascode
        ucascode = response.xpath("//*[contains(text(),'UCAS code')]//following-sibling::*").extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode).strip()
        if 'G401' in ucascode:
            ucascode = 'G401'
        # print(ucascode)

        #12.ib
        ib = response.xpath('//*[@id="maincontent"]/article/section[1]/div/div/div/div[2]/p').extract()
        ib = ''.join(ib)
        ib = remove_tags(ib)
        try:
            ib= re.findall(r'IB:(.*)',ib)[0]
        except:
            ib = 'N/A'
        # print(ib)


        #13.ielts 14151617
        try:
            IELTS_list = response.xpath(
                '//*[@id="maincontent"]/article/section[4]/div/div').extract()
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
            ielts_w = clear_space_str(ielts_r)
            ielts_s = clear_space_str(ielts_r)
            ielts_l = clear_space_str(ielts_r)
            # print(ielts)
            # print(ielts_r,ielts_w,ielts_s,ielts_l)
        except:
            ielts = 6.5
            ielts_w = 6.0
            ielts_r = 6.0
            ielts_s = 6.0
            ielts_l = 6.0


        # 18.url
        url = response.url
        # print(url)

        #19.degree_type
        degree_type = 1

        #20.degree_name
        degree_name = programme_e.split()[0]
        # print(degree_name)


        #21.location
        location = 'London'

        #22.tuition_fee_pre
        tuition_fee_pre = '£'


        #23.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'How you’ll be assessed')]//following-sibling::*[position()<5]").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)


        require_chinese_en = '<p>For direct entry onto our undergraduate programmes you’ll need A-levels, an International Baccalaureate or a recognised Access or Foundation course. Please see individual programme pages for specific entrance requirements.When we consider your application we’ll assess your test scores and academic grades alongside your personal statement, reference letter and extracurricular activities.</p>'

        item['assessment_en'] = assessment_en
        item['require_chinese_en'] = require_chinese_en
        item['university'] = university
        item['department'] = department
        item['programme_en'] = programme_en
        # item['overview_en'] = overview_en
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['other'] = other
        item['alevel'] = alevel
        item['ucascode'] = ucascode
        item['ib'] = ib
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['ielts_w'] = ielts_w
        item['url'] = url
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['location'] = location
        item['tuition_fee_pre'] = tuition_fee_pre
        yield  item