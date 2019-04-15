# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '18-7-17 下午2:41'
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
class UniversityofHullSpider(scrapy.Spider):
    name = 'UniversityofHull_p'
    allowed_domains = ['hull.ac.uk/']
    start_urls = []
    C = [
        'https://www.hull.ac.uk/study/pgt/advanced-practice-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/biomedical-science-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/accounting-finance-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/chemical-engineering-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/clinicial-app-psychology.aspx',
        'https://www.hull.ac.uk/study/pgt/cancer-rehabilitation.aspx',
        'https://www.hull.ac.uk/study/pgt/digital-media-ma.aspx',
        'https://www.hull.ac.uk/study/pgt/cardiovascular-rehab-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/economics-business-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/cancer-imaging-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/clinical-exercise-physiology.aspx',
        'https://www.hull.ac.uk/study/pgt/education-digital-tech-ma.aspx',
        'https://www.hull.ac.uk/study/pgt/education-inclusion-ma.aspx',
        'https://www.hull.ac.uk/study/pgt/education-ma.aspx',
        'https://www.hull.ac.uk/study/pgt/electrical-electronic-eng-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/education-leadership-ma.aspx',
        'https://www.hull.ac.uk/study/pgt/edu-earlychildhood-ma.aspx',
        'https://www.hull.ac.uk/study/pgt/criminal-justice-crime-control.aspx',
        'https://www.hull.ac.uk/study/pgt/comp-sci-software-eng-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/engineering-management.aspx',
        'https://www.hull.ac.uk/study/pgt/bus-management-intern-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/comp-sci-games-dev-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/energy-engineering-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/financial-management-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/enviro-change-mgmt-monitor-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/finance-investment-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/gastroenterology-care-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/comp-sci-security-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/healthcare-improvement-leadership.aspx',
        'https://www.hull.ac.uk/study/pgt/colonoscopy-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/hull-emba.aspx',
        'https://www.hull.ac.uk/study/pgt/history-ma.aspx',
        'https://www.hull.ac.uk/study/pgt/international-law-global-economy-asia-europe-trade-investment-llm.aspx',
        'https://www.hull.ac.uk/study/pgt/international-politics-ma.aspx',
        'https://www.hull.ac.uk/study/pgt/marine-enviro-mgmt-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/international-business-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/health-studies-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/leadership-health-social-care-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/marketing-management-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/mechanical-engineering-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/mmus-music.aspx',
        'https://www.hull.ac.uk/study/pgt/logistics-supply-chain-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/occ-health-safety-mgmt.aspx',
        'https://www.hull.ac.uk/study/pgt/occ-health-safety-enviro-mgmt.aspx',
        'https://www.hull.ac.uk/study/pgt/professional-accounting.aspx',
        'https://www.hull.ac.uk/study/pgt/renewable-energy-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/social-work-ma.aspx',
        'https://www.hull.ac.uk/study/pgt/pedagogy-practice.aspx',
        'https://www.hull.ac.uk/study/pgt/strategy-international-security.aspx',
        'https://www.hull.ac.uk/study/pgt/human-resource-management-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/international-law-conflict-security-human-rights-llm.aspx',
        'https://www.hull.ac.uk/study/pgt/social-research-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/tesol-ma.aspx',
        'https://www.hull.ac.uk/study/pgt/theatre-making-ma.aspx',
        'https://www.hull.ac.uk/study/pgt/translational-oncology.aspx',
        'https://www.hull.ac.uk/study/pgt/translation-studies-ma.aspx',
        'https://www.hull.ac.uk/study/pgt/public-engagement-sci-comm.aspx',
        'https://www.hull.ac.uk/study/pgt/tesol-translation-studies.aspx',
        'https://www.hull.ac.uk/study/pgt/translation-studies-tesol.aspx',
        'https://www.hull.ac.uk/study/pgt/english-ma.aspx',
        'https://www.hyms.ac.uk/postgraduate-taught-degrees/msc-in-health-professions-education',
        'https://www.hyms.ac.uk/postgraduate-taught-degrees/msc-in-clinical-anatomy-and-education',
        'https://www.hyms.ac.uk/postgraduate-taught-degrees/msc-in-clinical-anatomy',
        'https://www.hyms.ac.uk/postgraduate-taught-degrees/msc-in-human-anatomy-and-evolution',
        'https://www.hyms.ac.uk/postgraduate-taught-degrees/msc-in-physician-associate-studies',
        'https://www.hull.ac.uk/study/pgt/advanced-comp-sci-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/biomedical-engineering-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/analytical-forensic-chemistry.aspx',
        'https://www.hull.ac.uk/study/pgt/business-management-msc.aspx',
        'https://www.hull.ac.uk/study/pgt/advertising-marketing-msc.aspx'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'd'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="main-content"]/header/div[2]/div[1]/h1|//*[@id="main-content"]/section[1]/div[2]/div/div/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        degree_name = response.xpath('//*[@id="main-content"]/header/div[2]/div[1]/p[2]/span[2]').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)

        # print(programme_en,'###',degree_name,response.url)
        # print(programme_en)

        #6.start_date
        start_date = '2018-9'

        #7.teach_type
        if 'pgt' in url:
            teach_type = 'taught'
        else:
            teach_type = 'research'
        # print(teach_type)

        #8.teach_time
        teach_time_a = response.xpath('//*[@id="main-content"]/header/div[2]/div[2]').extract()
        teach_time_a = ''.join(teach_time_a)
        teach_time_a = remove_tags(teach_time_a)
        teach_time_a = clear_space_str(teach_time_a)
        # print(teach_time_a)
        if 'Full' in teach_time_a:
            teach_time = 'Full-time'
        elif teach_type == 'research':
            teach_time = 'Full-time'
        else:
            teach_time = ''
        # print(teach_time)

        #9.overview_en
        overview_en = response.xpath("//*[contains(text(),'About')]//following-sibling::p").extract()
        overview_en =''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #10.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'Fees and funding')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee =getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #11.tuition_fee_pre
        tuition_fee_pre = '£'

        #12.modules_en
        modules_en = response.xpath('//h2[contains(text(),"What you")]//following-sibling::*').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #13.rntry_requirements
        rntry_requirements = response.xpath("//*[contains(text(),'Entry requirements')]//following-sibling::*").extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #14.career_en
        career_en = response.xpath("//*[contains(text(),'Future prospects')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #15.require_chinese_en
        require_chinese_en = '<p>Lower second-class (2.2) equivalent Overall grade of 70% We may be able to accept a minimum grade of 65% if you have studied at a prestigious University as defined by the Ministry of Education.Upper second-class (2.1) equivalent Overall grade of 75 % We may be able to accept a minimum grade of 70% if you have studied at a prestigious University as defined by the Ministry of Education.</p>'

        #16.ielts 17181920
        ielts_list = response.xpath("//*[contains(text(),'International students')]//following-sibling::*").extract()
        ielts_list = ''.join(ielts_list)
        try:
            ielts= re.findall('\d\.\d',ielts_list)
        except:
            ielts = None
        if len(ielts) ==2:
            a = ielts[0]
            b = ielts[1]
            ielts = a
            ielts_l = b
            ielts_r = b
            ielts_s = b
            ielts_w = b
        else:
            ielts = 6.0
            ielts_l = 5.5
            ielts_r = 5.5
            ielts_s = 5.5
            ielts_w = 5.5

        #21.duration #22.duration_per
        if '3 years' in teach_time_a:
            duration = 3
            duration_per = 1
        elif '2 calendar years' in teach_time_a:
            duration = 2
            duration_per = 1
        elif '2 years' in teach_time_a:
            duration = 2
            duration_per = 1
        elif '16 months' in teach_time_a:
            duration = 16
            duration_per = 3
        elif '18 months' in teach_time_a:
            duration = 18
            duration_per = 3
        elif '5 years' in teach_time_a:
            duration = 5
            duration_per = 1
        else:
            duration = 1
            duration_per = 1

        #23.apply_pre
        apply_pre = '£'


        # print(duration,'#########',duration_per)

        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['start_date'] = start_date
        item['teach_type'] = teach_type
        item['teach_time'] = teach_time
        item['overview_en'] = overview_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['modules_en'] = modules_en
        item['rntry_requirements'] = rntry_requirements
        item['career_en'] = career_en
        item['require_chinese_en'] = require_chinese_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['duration'] = duration
        item['duration_per'] = duration_per
        yield  item