# -*- coding: utf-8 -*-
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import *
from scrapySchool_Canada_Ben.items import *

class UniversityoflethbridgeSpider(scrapy.Spider):
    name = 'UniversityofLethbridge'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.uleth.ca/future-student/university-lethbridge-programs-degrees']
    def parse(self, response):
        urlList=response.xpath('//a[contains(@data-href,"uleth")]/@data-href').extract()
        for uL in urlList:
            yield scrapy.Request(url=uL,callback=self.parses)
    def parses(self,response):
        item=get_item(ScrapyschoolCanadaBenItem)
        item['school_name']='University of Lethbridge'
        item['url']=response.url
        print(response.url)
        #加拿大学生入学要求 https://www.uleth.ca/ross/admissions/undergrad/high-school/canada
        item['entry_requirements_en']='\n'.join(['<p><strong>Minimum Academic Requirements<br></strong>Applicants from other countries must present qualifications comparable to those of Canadian applicants:</p>',
'<ul>',
'<li>Applicants who have completed secondary qualifications in other countries will be considered for admission under the High School Admission Route.</li>',
'<li>Applicants to undergraduate programs who have completed post-secondary study will be considered for admission under the Post-Secondary Admission Route.</li>',
'<li>Applicants to master’s programs should note the admission requirements for the country in which their undergraduate study was completed. &nbsp;</li>',
'</ul>',])
        #中国学生要求 https://www.uleth.ca/ross/admissions/undergrad/international/intreq_table
        item['require_chinese_en']='<p>Senior Secondary School Certificate of Graduation and an average grade of 72% or higher (where 60% is the passing grade)</p>'
        item['average_score']='72'
        item['apply_fee']='140'
        item['apply_pre']='$'
        item['tuition_fee_pre']='$'
        item['tuition_fee']='18,661'
        item['toefl_code']='0855'
        item['deadline']='2018-06-30,2018-11-01'
        item['location']='Alberta'
        item['start_date']='2018-09,2019-01'

        item['sat1_desc'],item['act_desc']='Admission average based on SAT or ACT results','Admission average based on SAT or ACT results'
        #英语语言要求 https://www.uleth.ca/ross/admissions/elp
        item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']='6.0','6.0','6.0','6.0','6.0'
        item['toefl'],item['toefl_l'],item['toefl_s'],item['toefl_r'],item['toefl_w']='80','16','16','16','18'
        #AP IB https://www.uleth.ca/ross/admissions/undergrad/high-school
        item['alevel']='At least five distinct courses with appropriate grade achievement, including at least three courses at the Ordinary level (or equivalent) and at least two courses at the Advanced level (or equivalent). The courses must include English, and a course will not be considered if it duplicates a course subject at the other level. All five courses are used in calculating the admission average. Students who have completed Ordinary level and subsequently completed either an Advanced International Certificate of Education (AICE) Diploma or a year of overseas College Foundation studies (including English) will be considered. Transfer credit will be considered for Advanced level courses in appropriate subjects, completed with grades of ‘C’ or higher. Credit for up to a maximum of ten term courses may be obtained in this manner.'
        item['ib']='If you take Advanced Placement (AP) or International Baccalaureate (IB) classes in high school, we may be able to give you some university-level credit depending on your final grades. This means that the number of courses you need to take at uLethbridge in order to graduate will be reduced and you will already have a head start in your program.'
        item['ap']='If you take Advanced Placement (AP) or International Baccalaureate (IB) classes in high school, we may be able to give you some university-level credit depending on your final grades. This means that the number of courses you need to take at uLethbridge in order to graduate will be reduced and you will already have a head start in your program.'
        #deadline https://www.uleth.ca/future-student/application-dates-and-deadlines
        major_name=response.xpath('//h1/text()').extract()[0]
        item['major_name_en']=major_name

        department=response.xpath('//h1/preceding-sibling::h2/a/text()').extract()
        department=''.join(department).strip()
        # print(department)
        item['department']=department.lower()

        degree_name=response.xpath('//h3[contains(text(),"Degrees Available")]/following-sibling::ul/li/text()').extract()
        # print(degree_name)
        for dn in degree_name:
            if 'Diploma' in dn:
                degree_name.remove(dn)
            # elif '/' in dn:
            #     degree_name=degree_name+list(map(lambda x: x.strip(),dn.split('/')))
            #     degree_name.remove(dn)
            # else:
            #     pass
        try:
            campus=response.xpath('//h3[contains(text(),"Campu")]/../text()').extract()[-2].strip()
            # item['campus']=campus
        except:
            campus=''
        if campus=='Lethbridge & Calgary':
            camp=['Lethbridge','Calgary']
        else :
            camp=['Lethbridge']



        pd=response.xpath('//h3[contains(text(),"Program Description")]/following-sibling::*').extract()
        pd_split=response.xpath('//h3[contains(text(),"Program Description")]/following-sibling::h3[1]').extract()
        if pd_split!=[]:
            overview=pd[0:pd.index(pd_split[0])]
        else:
            overview=pd
        item['overview_en']=remove_class(overview)

        career=response.xpath('//h3[contains(text(),"areer")]/following-sibling::ul[1]').extract()
        item['career_en']=remove_class(career)

        modules=response.xpath('//h3[contains(text(),"lasses")]/following-sibling::div[1]').extract()
        item['modules_en']=remove_class(modules)

        duration=response.xpath('//dt[contains(text(),"egree Length")]/following-sibling::dd[1]//text()').extract()
        # print(duration)
        if '5' in ''.join(duration):
            item['duration']='5'
            item['duration_per']='1'
        elif '4' in ''.join(duration):
            item['duration']='4'
            item['duration_per'] = '1'
        # yield item





        degree_name=list(set(degree_name))
        if degree_name==[]:
            yield item
        else:
            for deg in degree_name:
                item['degree_name']=deg
                for ca in camp:
                    item['campus']=ca
                    yield item