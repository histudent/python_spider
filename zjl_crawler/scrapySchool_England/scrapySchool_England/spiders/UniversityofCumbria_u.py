# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/9 15:41'
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
class UniversityofCumbriaSpider(scrapy.Spider):
    name = 'UniversityofCumbria_u'
    allowed_domains = ['cumbria.ac.uk/']
    start_urls = []
    C= [
        'https://www.cumbria.ac.uk/study/courses/undergraduate/biomedical-sciences/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/games-design-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/criminology/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/zoology-with-placement/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/zoology-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/nursing-learning-disabilities/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/forest-management/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/wildlife-media-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/business-accounting-and-finance-with-sandwich-placement/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/conservation-biology/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/nursing-childrens/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/business-management-with-marketing/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/business-management-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/photography-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/security-intelligence-and-investigative-practice-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/international-business-management/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/primary-education-inclusion-with-send-with-qts/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/criminology-with-social-sciences/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/law/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/dance/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/project-management-bsc/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/fine-art/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/forest-management-with-placement/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/applied-psychology/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/business-accounting-and-finance-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/teaching-and-learning/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/wildlife-media/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/acting/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/paramedic-science/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/dance-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/english-literature/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/nursing-adult/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/illustration-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/forensic-and-investigative-science/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/animal-conservation-science-with-placement/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/physiotherapy/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/outdoor-adventure-and-environment-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/business-management-with-marketing-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/sport-coaching-and-physical-education/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/working-with-children-and-families-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/outdoor-leadership-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/criminology-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/psychology/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/business-management-with-sandwich-placement/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/performing-arts/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/animation-and-visual-effects/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/criminology-with-law-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/graphic-design-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/illustration/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/working-with-children-and-families/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/fine-art-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/business-management/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/criminology-with-policing-and-investigation-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/nursing-mental-health/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/animal-conservation-science-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/film-and-television-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/primary-education-3-11-with-qts/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/marine-and-freshwater-conservation-with-placement/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/performing-arts-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/woodland-ecology-and-conservation/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/sport-and-exercise-science/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/games-design/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/conservation-biology-with-placement/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/social-work/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/criminology-with-forensic-investigation-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/zoology/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/criminology-with-applied-psychology/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/conservation-biology-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/law-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/sport-coaching-and-physical-education-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/geography/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/creative-writing-ba/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/midwifery/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/criminology-with-forensic-investigation/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/criminology-with-social-sciences-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/criminology-with-law/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/sport-and-exercise-science-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/applied-psychology-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/animal-conservation-science/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/biomedical-sciences-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/international-business-management-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/sport-rehabilitation/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/graphic-design/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/woodland-ecology-and-conservation-with-placement/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/education-studies/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/film-and-television/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/business-management-with-human-resources-management-with-sandwich-placement/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/musical-theatre-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/psychology-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/criminology-with-policing-and-investigation/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/occupational-therapy/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/marine-and-freshwater-conservation-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/biology-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/outdoor-leadership/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/international-business-management-with-sandwich-placement/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/outdoor-adventure-and-environment/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/diagnostic-radiography/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/business-management-with-marketing-with-sandwich-placement/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/security-intelligence-and-investigative-practice/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/professional-policing/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/photography/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/musical-theatre/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/professional-policing-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/sport-rehabilitation-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/business-accounting-and-finance/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/business-management-with-human-resources-management/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/forensic-and-investigative-science-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/youth-work-and-community-development/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/acting-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/business-management-with-human-resources-management-ify/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/healthcare-science/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/geography-with-integrated-foundation-year/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/marine-and-freshwater-conservation/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/biology-with-pathways/',
        'https://www.cumbria.ac.uk/study/courses/undergraduate/criminology-with-applied-psychology-with-integrated-foundation-year/'
    ]
    C = set(C)
    # print(len(C))
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Cumbria'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('/html/body/main/div[1]/header/div/h1/text()').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        programme_en = clear_space_str(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 1

        #5.degree_name
        degree_name = response.xpath('/html/body/main/div[1]/header/div/h1/em').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #6.location
        location = response.xpath("//*[contains(text(),'Location')]//following-sibling::*").extract()
        location = ''.join(location)
        location = remove_tags(location)
        if len(location)>50:
            location = 'N/A'
        # print(location)

        #7.duration #8.duration_per
        duration_list = response.xpath("//*[contains(text(),'Duration')]//following-sibling::*").extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list).strip()
        duration = re.findall('\d',duration_list)[0]
        # print(duration)
        duration_per = 1

        #9.ucascode
        ucascode = response.xpath('//div[@class="ucas-code"]//text()').extract()
        ucascode = ''.join(ucascode).strip()
        ucascode = ucascode.replace('Course code','').strip()
        # print(ucascode)


        #10.start_date
        start_date = response.xpath("//*[contains(text(),'Start date')]//following-sibling::*").extract()[0]
        start_date = remove_tags(start_date)
        # print(start_date)

        #11.modules_en
        modules_en = response.xpath("//h3[contains(text(),'Modules')]//following-sibling::*[1]").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en).strip()
        # print(modules_en)

        #12.apply_desc_en
        apply_desc_en = response.xpath('//*[@id="entry-requirements"]').extract()
        apply_desc_en = ''.join(apply_desc_en)
        apply_desc_en = remove_class(apply_desc_en)
        # print(apply_desc_en)

        #13.tuition_fee_pre
        tuition_fee_pre = '£'

        #14.other
        other = 'https://www.cumbria.ac.uk/media/university-of-cumbria-website/content-assets/public/finance/documents/studentfinance/fees/postgraduate-taught-tuition-fees-2018-19.pdf'

        #15.ielts 16171819
        if 'Nursing' in programme_en:
            ielts = 7.0
            ielts_l = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_s = 7.0
        elif 'Midwifery' in programme_en:
            ielts = 7.0
            ielts_l = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_s = 7.0
        elif 'Occupational Therapy' in programme_en:
            ielts = 7.0
            ielts_l = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_s = 7.0
        elif 'Social Work' in programme_en:
            ielts = 7.0
            ielts_l = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_s = 7.0
        elif 'Physiotherapy' in programme_en:
            ielts = 7.0
            ielts_l = 6.5
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_s = 6.5
        elif 'Diagnostic Radiography' in programme_en:
            ielts = 7.0
            ielts_l = 6.5
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_s = 6.5
        else:
            ielts = 6.0
            ielts_l = 5.5
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_s = 5.5

        #20.require_chinese_en
        require_chinese_en = '<p>High School Diploma / NUEE (Gaokao): High School Diploma and Gaokao are not accepted; applicants must complete an additional qualification, such as our International Foundation programme. English Language: IELTS 6.0 with at least 5.5 in each section (or equivalent).</p>'

        #21.apply_pre
        apply_pre = '£'

        #22.tuition_fee
        if 'Social Work' in programme_en:
            tuition_fee = 15500
        elif 'integrated foundation year' in programme_en:
            tuition_fee = 7500
        else:
            tuition_fee = 10500

        #23.overview_en
        overview_en = response.xpath('/html/body/main/div[3]/article/section[1]').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #24.assessment_en
        alevel = response.xpath('//*[@id="entry-requirements"]').extract()
        alevel = ''.join(alevel)
        alevel = remove_class(alevel)
        # print(alevel)

        item['alevel'] = alevel
        item['overview_en'] = overview_en
        item['tuition_fee'] = tuition_fee
        item['apply_pre'] = apply_pre
        item['require_chinese_en'] = require_chinese_en
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['location'] = location
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['ucascode'] = ucascode
        item['start_date'] = start_date
        item['modules_en'] = modules_en
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_desc_en'] = apply_desc_en
        item['other'] = other
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        yield  item