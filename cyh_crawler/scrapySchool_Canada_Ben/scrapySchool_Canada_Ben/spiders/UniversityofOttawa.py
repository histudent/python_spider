# -*- coding: utf-8 -*-
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import *
from scrapySchool_Canada_Ben.items import *

class UniversityofottawaSpider(scrapy.Spider):
    name = 'UniversityofOttawa'
    # allowed_domains = ['a.b']
    start_urls = ['https://catalogue.uottawa.ca/en/programs/#filter=.filter_19&.filter_21']

    def parse(self, response):
        course_class=response.xpath('//li[contains(@class,"filter_19") and contains(@class,"filter_21")]/@class').extract()
        urls=response.xpath('//li[contains(@class,"filter_19") and contains(@class,"filter_21")]/a/@href').extract()
        course_name=response.xpath('//li[contains(@class,"filter_19") and contains(@class,"filter_21")]/a/span/text()').extract()
        #filter_27 Art  29 Health Sciences 36 Medicine  35 Education  32 Law   28 Science  30 Engineering 34 Management (Telfer)  31 Social Sciences
        for cc,ur,cn in zip(course_class,urls,course_name):
            ur='https://catalogue.uottawa.ca'+ur
            if 'Joint' not in cn and 'Doctor' not in cn and 'é' not in cn and 'Combined' not in cn and 'à' not in cn:
                if 'filter_27' in cc:
                    dep='Faculty of Arts'
                elif 'filter_29' in cc:
                    dep='Faculty of Health Sciences'
                elif 'filter_36' in cc:
                    dep='Faculty of Medicine'
                elif 'filter_35' in cc:
                    dep='Faculty of Education'
                elif 'filter_32' in cc:
                    dep='Faculty of Law'
                elif 'filter_28' in cc:
                    dep='Faculty of Science'
                elif 'filter_30' in cc:
                    dep='Faculty of Engineering'
                elif 'filter_34' in cc:
                    dep='Telfer School of Management'
                elif 'filter_31' in cc:
                    dep='Faculty of Social Sciences'
                else:
                    dep=''
                yield scrapy.Request(url=ur,callback=self.parses,meta={'department':dep})
    def parses(self, response):
        item=get_item(ScrapyschoolCanadaBenItem)
        item['school_name']='University of Ottawa'
        item['url']=response.url
        item['toefl_code']='0993'
        item['apply_fee']='156'
        item['apply_pre']='$'
        department=response.meta['department']
        print(response.url)
        programme=response.xpath('//div[@id="page-title-area"]/h1/text()').extract()[0]
        print(programme)
        item['department']=department
        item['sat1_desc']='<p>achieving a minimum score of 550 (old SAT) or 31 (new SAT) on the SAT writing section</p>'
        item['alevel']='passing an A or AS Level English (non-ESL) course with a minimum grade of B'
        item['ib']='passing the International Baccalaureate English A course with a minimum grade of 4'


        if 'Bachelor of' in programme:
            item['major_name_en']=programme.split('Bachelor of ')[-1]
            item['degree_name']='Bachelor Degree'
        elif 'BASc in' in programme:
            item['major_name_en'] = programme.split('BASc in ')[-1]
            item['degree_name'] = 'BASc'
        elif 'Honours BA in' in programme:
            item['major_name_en'] = programme.split('Honours BA in ')[-1]
            item['degree_name'] = 'Honours BA'
        elif 'Honours BSc in' in programme:
            item['major_name_en'] = programme.split('Honours BSc in ')[-1]
            item['degree_name'] = 'Honours BSc'
        elif 'Honours BSocSc in' in programme:
            item['major_name_en'] = programme.split('Honours BSocSc in ')[-1]
            item['degree_name'] = 'Honours BSocSc'
        elif 'Major in' in programme:
            item['major_name_en'] = programme.split('Major in ')[-1]
            item['degree_name'] = 'Bachelor Degree'
        elif 'Honours BASc in' in programme:
            item['major_name_en'] = programme.split('Honours BASc in ')[-1]
            item['degree_name'] = 'Honours BASc'
        else:
            item['major_name_en']=programme
        if department=='Faculty of Arts':
            item['deadline']='2019-04-01'
            feeList=['15,722.08','14,423.30','14,423.30','14,423.30','13,898.82','13,898.82']
        elif department=='Faculty of Law':
            item['deadline'] = '2019-04-01'
            feeList=['27,973.86','25,662.97','25,662.97','25,662.97','25,423.13','25,423.13']
        elif department=='Faculty of Education':
            item['deadline']='2019-12-01'
            feeList=['15,428.21','14,153.70','14,153.70','14,153.70','13,639.02','13,639.02']
        elif department=='Faculty of Engineering':
            item['deadline']='2019-04-01'
            if 'Computer Science' in programme or 'Computer Science and Mathematics' in programme:
                feeList=['18,121.52','16,624.52','16,624.52','16,624.52','16,469.15','16,020.00']
            else:
                feeList=['22,916.17','21,023.10','19,560.62','18,199.88','17,538.07','17,059.76']
        elif department=='Faculty of Health Sciences':
            item['deadline'] = '2019-04-01'
            if 'Nursing' in programme:
                feeList=['18,670.12','17,127.80','15,936.30','14,827.69','14,288.50','13,898.82']
            else:
                feeList=['15,722.08','14,423.30','14,423.30','14,423.30','13,898.82','13,898.82']
        elif department=='Faculty of Medicine':
            feeList=['15,722.08','14,423.30','14,423.30','14,423.30','14,423.30','14,423.30']
        elif department=='Faculty of Science':
            item['deadline'] = '2019-04-01'
            if 'Biotechnology' in programme or 'Physics / Electrical Engineering' in programme:
                feeList=['20,202.02	','18,533.16','18,533.16','17,444.57','16,810.22','16,810.22']
            else:
                feeList=['15,722.08','14,423.30','14,423.30','14,423.30','13,898.82','13,898.82']
        elif department=='Faculty of Social Sciences':
            item['deadline'] = '2019-04-01'
            feeList=['15,722.08','14,423.30','14,423.30','14,423.30','13,898.82','13,898.82']
        elif department=='Telfer School of Management':
            item['deadline'] = '2019-04-01'
            feeList=['19,295.43','17,701.46','16,470.05','15,324.31','14,767.06','14,364.33']
        else:
            feeList=['0','0','0','0','0','0']
        units=response.xpath('//div[@id="progunits"]/text()').extract()
        # print(feeList)
        if units!=[]:
            # print(units)
            nums=int(units[0].split(' ')[0])
            if nums<=33:
                item['tuition_fee']=feeList[0]
            elif 33<nums<=66:
                item['tuition_fee']=feeList[1]
            elif 66<nums<=99:
                item['tuition_fee']=feeList[2]
            elif 99<nums<=132:
                item['tuition_fee']=feeList[3]
            elif 132<nums<=165:
                item['tuition_fee']=feeList[4]
            elif 165<nums:
                item['tuition_fee']=feeList[5]
            # print(item['tuition_fee'])
        item['tuition_fee_pre']='$'

        item['ielts'],item['ielts_w']='6.5','6.5'
        item['toefl'],item['toefl_w']='86','22'

        item['require_chinese_en']='<p>Upper Middle School Graduation Certificate or The Senior High School Graduation Diploma</p>'
        item['entry_requirements_en']='<p>Upper Middle School Graduation Certificate or The Senior High School Graduation Diploma</p>'

        overview=response.xpath('//div[@id="textcontainer"]').extract()
        item['overview_en']=remove_class(overview).replace('\n\n\n','')

        modules=response.xpath('//div[@id="programrequirementstextcontainer"]//table[1]').extract()
        item['modules_en']=remove_class(modules)

        # yield item
