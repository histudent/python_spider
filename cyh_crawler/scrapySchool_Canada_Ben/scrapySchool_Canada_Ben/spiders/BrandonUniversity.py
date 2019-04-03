# -*- coding: utf-8 -*-
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import *
from scrapySchool_Canada_Ben.items import *

class BrandonuniversitySpider(scrapy.Spider):
    name = 'BrandonUniversity'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.brandonu.ca/future-students/programs/business-admin/',
'https://www.brandonu.ca/future-students/programs/education/',
'https://www.brandonu.ca/future-students/programs/education-5-year/',
'https://www.brandonu.ca/future-students/programs/fine-arts/',
'https://www.brandonu.ca/future-students/programs/music/',
'https://www.brandonu.ca/future-students/programs/nursing/',
'https://www.brandonu.ca/future-students/programs/phys-ed/',
'https://www.brandonu.ca/future-students/programs/psych-nursing/',
'https://www.brandonu.ca/future-students/programs/environmental-science/','https://www.brandonu.ca/future-students/programs/degrees/arts/anthropology/',
'https://www.brandonu.ca/future-students/programs/degrees/science/ades/',
'https://www.brandonu.ca/future-students/programs/degrees/arts/business-administration/',
'https://www.brandonu.ca/future-students/programs/degrees/arts/classical-and-modern-languages/',
'https://www.brandonu.ca/future-students/programs/degrees/arts/drama/',
'https://www.brandonu.ca/future-students/programs/degrees/arts/economics/',
'https://www.brandonu.ca/future-students/programs/degrees/arts/english-creative-writing/',
'https://www.brandonu.ca/future-students/programs/degrees/arts/gender-and-womens-studies/',
'https://www.brandonu.ca/future-students/programs/degrees/arts/history/',
'https://www.brandonu.ca/future-students/programs/degrees/arts/native-studies/',
'https://www.brandonu.ca/future-students/programs/degrees/arts/philosophy/',
'https://www.brandonu.ca/future-students/programs/degrees/arts/political-science/',
'https://www.brandonu.ca/future-students/programs/degrees/arts/religion/',
'https://www.brandonu.ca/future-students/programs/degrees/arts/rural-development/',
'https://www.brandonu.ca/future-students/programs/degrees/arts/sociology/',
'https://www.brandonu.ca/future-students/programs/degrees/arts/visual-and-aboriginal-art/',
'https://www.brandonu.ca/future-students/programs/degrees/science/biology/',
'https://www.brandonu.ca/future-students/programs/degrees/science/chemistry/',
'https://www.brandonu.ca/future-students/programs/degrees/science/math-comp-sci/',
'https://www.brandonu.ca/future-students/programs/degrees/science/geography/',
'https://www.brandonu.ca/future-students/programs/degrees/science/geology/',
'https://www.brandonu.ca/future-students/programs/degrees/science/physics-and-astronomy/',
'https://www.brandonu.ca/future-students/programs/degrees/science/psychology/',]
    start_urls = set(start_urls)
    def parse(self, response):
        item=get_item(ScrapyschoolCanadaBenItem)
        item['url']=response.url
        item['school_name']='Brandon University'
        print(response.url)
        item['ielts_desc']='6.5 overall'
        item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']='6.5','6.5','6.5','6.5','6.5'
        item['toefl_desc']='80 (Internet-based test) with a minimum score of 20 in each testing section.'
        item['toefl'],item['toefl_l'],item['toefl_s'],item['toefl_r'],item['toefl_w']='80','20','20','20','20'
        item['ib']='Students with an International Baccalaureate Diploma with an overall score of 24 points are considered to have the equivalent of Manitoba High School Graduation for purposes of admission to Brandon University. The IB Diploma must contain at least three Higher Level courses, with the remaining courses being either the Higher Level or the Standard Level'
        item['require_chinese_en']='Senior High School Graduation Diploma'
        item['entry_requirements_en']='<ul><li>have a Grade 12 average below 70%; OR</li><li>are missing or have less than 60% in Grade 12 English; OR</li><li>have fewer than 5 approved courses at the S (academic) level (or equivalent based on provincial standards);&nbsp; OR</li><li>graduates with a G.E.D. as recognized in North America</li></ul>'
        item['start_date']='2019-09'
        item['deadline']='2019-04-01'
        item['ap']='Completion of Advanced Placement (AP) English, Literature and Composition or Language and Composition with a score of four or greater.'
        item['alevel']='Must have passes in five different subjects of which at least two must be passed at the Advanced level or passes in four different subjects of which at least three must be passed at the advance level. Or Two Advanced Subsidiary Level courses in lieu of one Advance Level course, or four Advance Subsidiary Level for two Advance Level to meet the minimum admission requirements. Students with one Advance Subsidiary subject will be considered in lieu of an Ordinary level subject.'
        item['tuition_fee_pre']='$'
        major_name=response.xpath('//h1/text()').extract()
        # print(major_name)
        item['major_name_en']=major_name
        if 'arts/' in response.url:
            item['degree_name']='Bachelor of Arts'
            item['department']='Faculty of Arts'
            item['tuition_fee'] = '7,203.00'
        elif 'science/' in response.url:
            item['degree_name']='Bachelor of Science'
            item['department']='Faculty of Science'
            item['tuition_fee']='7,824.00'
        else:
            item['degree_name']=major_name
        if '/music/' in response.url:
            item['department']='Faculty of Music'
            item['tuition_fee']='7,653.00'
        elif '/education' in response.url:
            item['department'] = 'Faculty of Education'
            item['tuition_fee'] = '7,332.00'

        career=response.xpath('//h3[contains(text(),"areer")]/following-sibling::*[1]').extract()
        item['career_en']=remove_class(career)

        yield item