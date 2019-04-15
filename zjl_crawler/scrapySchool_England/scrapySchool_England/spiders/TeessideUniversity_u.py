# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/8 9:05'
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
class TeessideUniversitySpider(scrapy.Spider):
    name = 'TeessideUniversity_u'
    allowed_domains = ['tees.ac.uk/']
    start_urls = []
    C= [
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/534/A201/dentistry/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1183/C605/applied-sports-science/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1115/F610/geoscience/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1165/MT10/law-with-options-in-mandarin-llb/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1146/M1G1/bachelor-of-laws-with-computing-science/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1170/NR20/international-business-with-german/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1168/NR10/international-business-with-french/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1171/NT12/international-business-with-mandarin/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1172/NR14/international-business-with-spanish/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1169/NQ15/international-business-with-gaelic/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1138/N300/finance/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1177/N1R4/mbus-international-business-with-spanish-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1174/N1Q5/mbus-international-business-with-gaelic-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1145/N125/international-business-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1176/NT25/mbus-international-business-with-mandarin-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1173/N1R1/mbus-international-business-with-french-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/796/A100/medicine-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1175/N1R2/mbus-international-business-with-german-5-years/'
    ]
    C= set(C)
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Teesside University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="coursepage"]/section[1]/div[1]/div/div[1]/h1/text()').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en).strip()
        # print(programme_en)

        #4.degree_type
        degree_type = 1

        #5.degree_name
        degree_name = response.xpath('//*[@id="coursepage"]/section[1]/div[1]/div/div[1]/h1/span').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name).strip()
        if '(Hons)' in degree_name:
            degree_name = degree_name.replace('(Hons)','').strip()
        # print(degree_name)

        #6.overview_en
        overview_en = response.xpath('//*[@id="tab1"]/div/div[1]/div').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #7.modules_en
        modules_en = response.xpath('//*[@id="tab2"]/div[1]/div/div[1]/div[1]').extract()
        modules_en =''.join(modules_en)
        modules_en = remove_class(modules_en)
        print(modules_en)

        #8.assessment_en
        assessment_en = response.xpath('//*[@id="tab2"]/div[1]/div/div[1]/div[3]/p').extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #9.career_en
        career_en = response.xpath("//*[contains(text(),'Career opportunities')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #10.ucascode
        ucascode = response.xpath('//*[@id="coursepage"]/section[1]/div[1]/div/div[2]/div/div[2]/p/text()').extract()
        ucascode = ''.join(ucascode)
        ucascode = clear_space_str(ucascode)
        try:
            ucascode = ucascode[:4]
        except:
            ucascode = 'N/A'
        # print(ucascode)

        #11.department
        department = response.xpath('//*[@id="coursepage"]/section[1]/div[1]/div/div[2]/div/div[3]/a/p').extract()
        department = ''.join(department)
        department = remove_tags(department)
        department = department.replace('&amp; ','')
        # print(department)

        #12.duration
        duration = response.xpath('//*[@id="courseinfopdf"]/div[1]/ul/li[1]').extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        # print(duration)

        #13.tuition_fee
        tuition_fee = 11825

        #14.apply_desc_en
        apply_desc_en = response.xpath('//*[@id="tab3"]/div/div[1]/div').extract()
        apply_desc_en = ''.join(apply_desc_en)
        apply_desc_en = remove_class(apply_desc_en)
        # print(apply_desc_en)

        #15.start_date
        start_date = '2018-10-13'

        #16.tuition_fee_pre
        tuition_fee_pre = '£'

        #17.other
        other='https://www.tees.ac.uk/sections/international/fees.cfm'


        #18.require_chinese_en
        require_chinese_en = '<p>For entry onto a Foundation or Extended programme, applicants require:  Huikao (Chinese senior secondary school graduation certificate) Successful completion of the first two years of Senior Secondary School with a minimum average of 70% or successful completion of Senior Secondary School with a minimum average of 60% For entry onto an Undergraduate programme, applicants require:  For entry onto Year 1:Huikao (Chinese senior secondary school graduation certificate) Successful completion of Senior Secondary School with a minimum average of 80% Or Gaokao (Chinese university or college entrance exam) with a minimum score of 500 For entry onto Higher National Diploma: Gaokao with a minimum score of 450 For entry onto Integrated Master of Engineering – MEng (Hons): Gaokao with a minimum score of 550 For entry onto Undergraduate top-up programmes (third-year entry) Dazhuan (three-year college graduation diploma) with a minimum of 70% average or, SQA Higher National Diploma with BBC as minimum or, Edexcel Higher National Diploma – standard UK entry requirements or, UK accredited foundation degree</p>'


        #19.ielts,20212223
        if 'Dental Hygiene and Dental Therapy' in degree_name:
            ielts = 7.0
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
            ielts_s = 6.5
        elif 'Diagnostic Radiography' in degree_name:
            ielts = 7.0
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
            ielts_s = 6.5
        elif 'Midwifery' in degree_name:
            ielts = 7.0
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
            ielts_s = 6.5
        elif 'Physiotherapy' in degree_name:
            ielts = 7.0
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
            ielts_s = 6.5
        elif 'Occupational Therapy' in degree_name:
            ielts = 7.0
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
            ielts_s = 6.5
        elif 'Nursing Studies' in degree_name:
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 7.0
            ielts_s = 7.0
        else:
            ielts = 6
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        if 'Fine Art' in programme_en:
            ielts = 5.5
        elif 'Design' in programme_en:
            ielts = 5.5
        elif 'Media Production' in programme_en:
            ielts = 5.5
        elif 'Engineering' in programme_en:
            ielts = 5.5
        elif 'Science' in programme_en:
            ielts = 5.5
        elif 'Computing' in programme_en:
            ielts = 5.5
        elif 'Media Studies' in programme_en:
            ielts = 5.5
        elif 'Journalism' in programme_en:
            ielts = 5.5
        elif 'Business' in programme_en:
            ielts = 6.0
        elif 'English' in programme_en:
            ielts = 6.0
        elif 'Sport' in programme_en:
            ielts = 6.0
        elif 'History' in programme_en:
            ielts = 6.0
        elif 'Psychology' in programme_en:
            ielts = 6.0
        elif ' Criminology' in programme_en:
            ielts = 6.0
        elif 'Sociology' in programme_en:
            ielts = 6.0
        elif 'Youth Studies' in programme_en:
            ielts = 6.0
        elif 'Education' in programme_en:
            ielts = 6.0
        elif 'Law' in programme_en:
            ielts = 6.0
        elif 'Crime' in programme_en:
            ielts = 6.0
        elif 'Investigation' in programme_en:
            ielts = 6.0
        elif 'Health' in programme_en:
            ielts = 7.0
        else:ielts = 6.0
        # print(ielts,ielts_w,ielts_l,ielts_r,ielts_s)
        #24.apply_pre
        apply_pre = '£'

        #25.alevel
        # alevel = response.xpath('')
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['ucascode'] = ucascode
        item['department'] = department
        item['duration'] = duration
        item['tuition_fee'] = tuition_fee
        item['apply_desc_en'] = apply_desc_en
        item['start_date'] = start_date
        item['other'] = other
        item['tuition_fee_pre'] = tuition_fee_pre
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['require_chinese_en'] = require_chinese_en
        item['apply_pre'] = apply_pre
        # yield item