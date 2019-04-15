# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/10/25 16:10'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from lxml import etree
import requests

class TrinityWesternUniversity_USpider(scrapy.Spider):
    name = 'TrinityWesternUniversity_U'
    allowed_domains = ['twu.ca/']
    start_urls = []
    C= [
        'https://www.twu.ca/academics/school-business/business-bba-ba',
        'https://www.twu.ca/academics/school-education/education-bed',
        'https://www.twu.ca/academics/school-arts-media-culture/acting',
        'https://www.twu.ca/academics/faculty-natural-applied-sciences/biotechnology',
        'https://www.twu.ca/academics/faculty-natural-applied-sciences/chemistry',
        'https://www.twu.ca/academics/faculty-natural-applied-sciences/biology',
        'https://www.twu.ca/academics/faculty-natural-applied-sciences/biotechnology',
        'https://www.twu.ca/academics/faculty-natural-applied-sciences/chemistry',
        'https://www.twu.ca/academics/faculty-natural-applied-sciences/computing-science',
        'https://www.twu.ca/academics/faculty-natural-applied-sciences/environmental-studies',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/general-studies',
        'https://www.twu.ca/academics/faculty-natural-applied-sciences/mathematics',
        'https://www.twu.ca/academics/faculty-natural-applied-sciences/mathematics-computing-science',
        'https://www.twu.ca/academics/school-human-kinetics/elementary-school-physical-education',
        'https://www.twu.ca/school-human-kinetics/human-kinetics',
        'https://www.twu.ca/academics/school-human-kinetics/kinesiology',
        'https://www.twu.ca/academics/school-human-kinetics/sport-leisure-management',
        'https://www.twu.ca/academics/school-nursing/nursing',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/philosophy',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/political-studies',
        'https://www.twu.ca/academics/academic-transition-first-year-at1',
        'https://www.twu.ca/academics/school-arts-media-culture/art-design',
        'https://www.twu.ca/academics/school-arts-media-culture/arts-media-culture',
        'https://www.twu.ca/adult-degrees-and-flexible-programs/adult-degree-completion/ba-leadership',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/biblical-studies',
        'https://www.twu.ca/academics/school-business/business-bba-ba',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/christianity-culture',
        'https://www.twu.ca/academics/school-arts-media-culture/corporate-communication',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/english-and-creative-writing',
        'https://www.twu.ca/academics/faculty-natural-applied-sciences/environmental-studies',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/european-studies',
        'https://www.twu.ca/adult-degrees-flexible-programs/degree-completion/customized-finishing-my-tw-degree',
        'https://www.twu.ca/academics/freshman-academy',
        'https://www.twu.ca/academics/school-arts-media-culture/game-development',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/general-studies',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/geography',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/history',
        'https://www.twu.ca/school-human-kinetics/human-kinetics',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/humanities',
        'https://www.twu.ca/academics/adult-degrees-and-flexible-programs/independent-studies',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/inter-cultural-studies',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/international-studies',
        'https://www.twu.ca/academics/laurentian-leadership-centre',
        'https://www.twu.ca/academics/twu-extension/leadership-ba-international',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/linguistics',
        'https://www.twu.ca/academics/school-arts-media-culture/media-communication',
        'https://www.twu.ca/academics/school-arts-media-culture/music',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/philosophy',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/political-studies',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/psychology',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/religious-studies',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/sociology',
        'https://www.twu.ca/academics/school-human-kinetics/sport-leisure-management',
        'https://www.twu.ca/academics/school-arts-media-culture/theatre',
        'https://www.twu.ca/academics/twu-extension/university-transition-first-year-ut1',
        'https://www.twu.ca/academics/faculty-humanities-social-sciences/world-languages-cultures'
    ]
    C = set(C)
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)

        #1.school_name
        school_name = 'Trinity Western University'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.major_name_en
        major_name_en = response.xpath('//*[@id="title-wrapper"]/div/h1').extract()
        major_name_en = ''.join(major_name_en)
        major_name_en = remove_tags(major_name_en).replace('amp;','')
        # print(major_name_en)

        #4.career_en
        career_en = response.xpath("//div[@class='field field-name-field-careers-title field-type-text field-label-hidden']/../../following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        career_en = clear_space_str(career_en)
        # print(career_en)


        #6.overview_en
        overview_en = response.xpath("//div[@class='field field-name-body field-type-text-with-summary field-label-hidden']").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #7.location
        location = 'Vancouver, Columbia'

        #8.modules_en
        modules_en = response.xpath("//a[contains(@href,'sites/default/files/2017-2018academic')]//@href").extract()
        if len(modules_en)>0:
            modules_en = modules_en[0]
        else:
            modules_en = None
        # print(modules_en)

        #9.deadline
        deadline = '2019-01-15'

        #10.ielts_desc 1112131415
        ielts_desc = 'Overall score: 6.5 with 6.0 on Writing Band'
        ielts = 6.5
        ielts_r = 6
        ielts_l = 6
        ielts_w = 6
        ielts_s = 6

        #16.toefl_desc 1718192021
        toefl_desc = 'Overall Score: 88 with a minimum score of 21 in each of the four areas and a TWE of at least 5.'
        toefl = 88
        toefl_r = 21
        toefl_w = 21
        toefl_s = 21
        toefl_l = 21

        #22.toefl_code sat_code
        toefl_code = '0876'
        sat_code =toefl_code

        #24.ib
        ib = ' Achieve a final grade of 3 or better on the IB English 12 A1 or A2 (HL) or a final grade of 4 or better on the IB English 12 A1 or A2 (SL) or IB English 12 B with a grade of 4 or better.'

        #25.ap
        ap = 'Achieve a final grade of 4 or better on the AP (Advanced Placement English Language and Composition or AP Literature & Composition.'

        #26.start_date
        start_date = '2019-09'

        #27.tuition_fee
        tuition_fee = '22,260'

        #28.tuition_fee_pre
        tuition_fee_pre = '$'

        #29.require_chinese_en
        require_chinese_en = '<p>Students must have standing in five subjects of which at least two must be taken at the Advanced level.Students may be eligible for three semester hours of credit for each Advanced level course completed to a maximum of 12 semester hours provided that a minimum grade of C is achieved in that course. Departments will determine if credit awarded is general or course specific. The following equivalents will be considered: School Certificate: same as GCE with at least two passes at the principal level of the Higher School Certificate. Certificate of matriculation from recognized universities. International Baccalaureate with at least two subjects at the higher level. Other countries: write or email the Admissions Office for information.</p>'

        #30.entry_requirements_en
        entry_requirements_en = '<p>Students are required to graduate from high school or equivalent with a university preparatory program. This must include English 12 plus three additional Grade 12 academic subjects at a minimum overall average of 70%. A minimum grade of 60% or better is expected on the provincial examination portion of English 12. </p>'

        #31.apply_pre
        apply_pre = '$'

        #32.apply_fee
        apply_fee = '150'

        item['school_name'] = school_name
        item['url'] = url
        item['major_name_en'] = major_name_en
        item['career_en'] = career_en
        item['overview_en'] = overview_en
        item['location'] = location
        item['modules_en'] = modules_en
        item['deadline'] = deadline
        item['ielts_desc'] = ielts_desc
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl_desc'] = toefl_desc
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['toefl_code'] = toefl_code
        item['sat_code'] = sat_code
        item['ib'] = ib
        item['ap'] = ap
        item['start_date'] = start_date
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['require_chinese_en'] = require_chinese_en
        item['entry_requirements_en'] = entry_requirements_en
        item['apply_pre'] = apply_pre
        item['apply_fee'] = apply_fee

        #5.degree_name
        degree_name = response.xpath("//h2[contains(text(),'Degrees')]//following-sibling::*").extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_class(degree_name)
        degree_name = clear_space_str(degree_name)
        degree_name = re.findall('<div>(.*?)</div>',degree_name)
        if 'Minor' in degree_name:
            degree_name.remove('Minor')
        if 'Concentration' in degree_name:
            degree_name.remove('Concentration')
        for i in degree_name:
            degree_name = i
            degree_name = degree_name.replace('<div>','').strip()
            item['degree_name'] = degree_name
            yield item
        # print(degree_name)
