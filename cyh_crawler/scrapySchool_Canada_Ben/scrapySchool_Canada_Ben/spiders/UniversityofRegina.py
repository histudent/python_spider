# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import *
from scrapySchool_Canada_Ben.items import *

class UniversityofreginaSpider(scrapy.Spider):
    name = 'UniversityofRegina'
    # allowed_domains = ['a.b']
    start_urls = ['https://urconnected.uregina.ca/program.do?programAction=DegreeProgramList']
    def parse(self, response):
        urlList=response.xpath('//a[contains(text(),"Bachelor Degree")]/../../following-sibling::tr[1]/td/div//td/a/@href').extract()
        # print(urlList)
        for uL in urlList:
            urls='https://urconnected.uregina.ca/programs/degree/'+uL[61:]
            yield scrapy.Request(url=urls,callback=self.parses)
    #;jsessionid=4647EC41C7CCD45F6BBAFE157DD8C5F8
    #;jsessionid=248C8491B6CB3BAC6589857760669C11
    def parses(self, response):
        item=get_item(ScrapyschoolCanadaBenItem)
        item['alevel']='<p>Minimum of two Advanced Level (A-level) approved courses</p>'
        item['school_name']='University of Regina'
        item['url']=response.url
        item['sat1_desc']='<p>SAT I  (minimum score of 1100) or ACT (minimum ACT score of 24)</p>'
        #语言要求  https://urconnected.uregina.ca/apply/elp.ezc
        item['toefl'],item['toefl_l'],item['toefl_s'],item['toefl_r'],item['toefl_w']='80','19','18','19','18'
        item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']='6.5','5.5','5.5','5.5','5.5'
        item['ib']='<p>Passes in six subjects with three at the standard level and three at the higher level</p><p>Minimum 24 diploma points required</p><p>Faculty-specific course prerequisite must be presented at either the standard or the higher level</p>'
        item['apply_fee'],item['apply_pre']='100','$'
        item['tuition_fee'],item['tuition_fee_pre']='18,719.90 - 21,784.90','$'
        #申请截止日期 https://urconnected.uregina.ca/apply/fall-deadlines.ezc
        item['deadline']='2019-03-15'
        item['require_chinese_en']=''.join(['<div><h1>China Requirements</h1>  ',
'<h2>China <span>Admission</span> Requirements</h2>',
'<h3>Applying from Secondary School:</h3>',
'<ul>',
'	<li>High School/Senior Middle School Diploma</li>',
'	<li>Final Official High School Score Report - must show Year 1 (grade 10), Year 2 (grade 11) and Year 3 (grade 12)</li>',
'	<li>Unified exams or Joint Academic Upper Middle School Graduation Examination</li>',
'</ul>',
'<h3>Transferring from another Post-Secondary Institution:</h3>',
'<ul>',
'	<li>Original transcripts of grades for all post-secondary institutions attended. Must be sent directly from the institution or in an institution sealed envelope</li>',
'	<li>Diploma (when attained)</li>',
'</ul>',
'<h3>Proof of English Language Proficiency:</h3>',
'<p>All students at the University of Regina must provide Proof of <a>English Language Proficiency</a></p>',
'<h3>&nbsp;</h3>',
'<h3>Faculty specific requirements:</h3>',
'<p><strong>Science:</strong> Mathematics and one of Chemistry, Biology or Physics in Year 3</p>',
'<p><strong>Engineering:</strong> Mathematics, Chemistry and Physics in Year 3</p>',
'<p><strong>Kinesiology and Health Studies:</strong> Mathematics and one of Biology, Chemistry and Physics in Year 3.</p>',
'<p>An English translation of documents is required if they are not in English or French.</p>',
'<p>A school attested copy will be accepted from countries where only one original document is provided.&nbsp; The original will need to be presented to the admissions office upon arrival.</p>',
'</div>',])

        programme=response.xpath('//strong[contains(text(),"Program Name")]/../following-sibling::td/a/text()').extract()[0]
        item['major_name_en']=programme
        department=response.xpath('//strong[contains(text(),"Faculty")]/../following-sibling::td/a/text()').extract()[0]
        item['department']=department

        deg = response.xpath('//strong[contains(text(),"Degree")]/../following-sibling::td/text()').extract()
        deg=''.join(deg).strip()
        # print(deg)
        if '4' in deg:
            item['duration']=4
            item['duration_per']=1
        elif '5' in deg:
            item['duration'] = 5
            item['duration_per'] = 1
        item['degree_name']='Bachelor Degree'

        ove=response.xpath('//strong[contains(text(),"Program Description")]/../following-sibling::td/p').extract()
        ove_split=response.xpath('//strong[contains(text(),"Sample Courses")]/../self::*').extract()
        item['modules_en']=remove_class(ove_split)
        if ove_split!=[]:
            overview=ove[0:ove.index(ove_split[0])]
            item['overview_en']=remove_class(overview)
        career=response.xpath('//strong[contains(text(),"areer")]/../self::*').extract()
        # print(career)
        item['career_en']=remove_class(career)
        campuses=response.xpath('//strong[contains(text(),"Campuses")]/../following-sibling::td/text()').extract()
        # print(campuses)
        campuses=list(map(lambda a:a.strip(),campuses))
        # print(campuses)

        for cp in campuses:
            if cp!='':
                item['campus']=cp
                yield item

