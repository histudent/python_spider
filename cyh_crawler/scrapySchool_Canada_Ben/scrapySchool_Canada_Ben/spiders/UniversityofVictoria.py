# -*- coding: utf-8 -*-
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import *
from scrapySchool_Canada_Ben.items import *

class UniversityofvictoriaSpider(scrapy.Spider):
    name = 'UniversityofVictoria'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.uvic.ca/future-students/undergraduate/programs/index.php']
    #学费 https://www.uvic.ca/future-students/undergraduate/tuition-finance/estimator/index.php?level=UG&residency=D&program=4
    #https://www.uvic.ca/apis/fee/getFees?level=UG&residency=I&programId=4
    #英语语言要求 https://www.uvic.ca/future-students/undergraduate/admissions/language/index.php
    #申请截止日期 https://www.uvic.ca/future-students/undergraduate/deadlines/index.php
    #中国学生要求 https://www.uvic.ca/future-students/undergraduate/admissions/high-school/cn/index.php
    #IB https://www.uvic.ca/future-students/undergraduate/admissions/high-school/ib/index.php
    #alevel https://www.uvic.ca/future-students/undergraduate/admissions/high-school/uk/index.php
    def parse(self, response):
        programme=response.xpath('//span[contains(text(),"Bachelor degree")]/../preceding-sibling::td/a/span/text()').extract()
        urls=response.xpath('//span[contains(text(),"Bachelor degree")]/../preceding-sibling::td/a/@href').extract()
        # print(len(urls))
        for pg,u in zip(programme,urls):
            u='https://www.uvic.ca/future-students/undergraduate/programs/'+u
            yield scrapy.Request(url=u,meta={'programme':pg},callback=self.parses)
    def parses(self,response):
        item=get_item(ScrapyschoolCanadaBenItem)
        item['url']=response.url
        print(response.url)
        item['school_name']='University of Victoria'
        item['ielts_desc']='6.5, with no component less than 6.0'
        item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']='6.5','6.0','6.0','6.0','6.0'
        item['toefl_desc']='90 on the iBT (Internet-based test) with no section less than 20'
        item['toefl'],item['toefl_l'],item['toefl_s'],item['toefl_r'],item['toefl_w']='90','20','20','20','20'
        item['deadline']='2019-02-28'
        item['start_date']='2019-09'
        item['require_chinese_en']='<p>Senior high school graduation showing grade results for Senior Years 1, 2 and 3 with a minimum overall average of 85%, plus the National Chinese Entrance Examinations (Gao Kao) with an acceptable score or SAT/ACT results.</p>'
        item['ib']='<ul><li>Full diploma with at least three HL subjects completed</li><li>English at the HL/SL level</li><li>Math at the HL/SL level (Math Studies is not acceptable)</li></ul>'
        item['alevel']='<p>General Certificate of Secondary Education (GCSE) and Advanced Level Examinations</p><p>At least five Ordinary Level subjects and three Advanced Level subjects with a minimum grade of "C" in each subject</p><ul><li>One of the subjects must be English</li><li>Other subjects are dependent upon the program requested</li></ul>'
        item['sat1_desc']='<p>SAT scores of at least 1,270</p>'
        item['sat_code']='0989'
        item['act_desc']='<p>composite ACT scores of at least 26</p>'
        item['act_code']='5327'
        item['apply_fee'],item['apply_pre']='127.00','$'

        modules=response.xpath('//h3[contains(text(),"Sample course")]/following-sibling::ul[1]').extract()
        item['modules_en']=remove_class(modules)
        # if modules!=[]:
        #     modules=remove_class(modules)
        #     print(modules)
        # else:
        #     print(response.url)

        department=response.xpath('//h3[contains(text(),"Faculties and departments")]/following-sibling::ul[1]/li/a/text()').extract()
        # print(department)
        item['department']=','.join(department)

        degree_name=response.xpath('//dt[text()="Credential(s) granted:"]/following-sibling::dd[contains(text(),"Bachelor")]/text()').extract()

        item['tuition_fee']='10,837'
        item['tuition_fee_pre']='$'

        major_name=response.xpath('//h1/text()').extract()
        # print(major_name)
        item['major_name_en']=''.join(major_name).strip()

        overview=response.xpath('//div[@class="program-content"]/p[1]').extract()
        item['overview_en']=remove_class(overview)

        career=response.xpath('//h3[text()="What can you do with your degree?"]/following-sibling::div/div/ul').extract()
        if career==[]:
            career=response.xpath('//h3[text()="What can you do with your degree?"]/following-sibling::ul[1]').extract()
        item['career_en']=remove_class(career)

        # focus=response.xpath('//h3[text()="Areas of focus"]/following-sibling::ul/li/text()').extract()
        for dn in degree_name:
            item['degree_name']=dn
            yield item
            # if focus!=[]:
            #     for fo in focus:
            #         item['major_name_en']=fo
            #         yield item
            # else:
            #     yield item
