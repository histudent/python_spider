# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.clearSpace import clear_same_s
import re
from scrapySchool_England.middlewares import change_durntion_per,clear_duration,tracslateDate
class BruneluniversitylondonSpider(scrapy.Spider):
    name = 'BrunelUniversityLondon_P'
    allowed_domains = ['brunel.ac.uk']
    start_urls=[]
    for i in range(1, 10):
        fullurl='http://www.brunel.ac.uk/study/Course-listing?courseLevel=0%2f2%2f24%2f28%2f44&studyMode=full-time&page='+str(i)
        start_urls.append(fullurl)
    def parse(self, response):
        # print(response.url)
        url_list=response.xpath('//table[@id="responsive-example-table"]/tbody//a/@href').extract()
        for i in url_list:
            fullurl='http://www.brunel.ac.uk%s' % i
            yield scrapy.Request(fullurl,callback=self.parses)
    def parses(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "Brunel University London"
        item['url'] = response.url
        item['location'] = 'London'
        item['teach_time'] = 'fulltime'
        item['tuition_fee_pre'] = '£'
        item['degree_type'] = '2'
        item['deadline'] = '2018-12-1'
        item['teach_type'] = 'taught'
        programme=response.url.split('/')[-1]
        # print(programme)
        degree_name=programme.split('-')[-1]
        if degree_name[0]!='L':
            programme=programme.replace(degree_name,'')
            programme=programme.replace('-',' ').strip()
        else:
            degree_name=''
            programme=programme.replace('-',' ').strip()
        # print(programme)
        # print(degree_name)
        item['programme_en'] = programme
        item['degree_name'] = degree_name

        overview = response.xpath('//h2[contains(text(),"Overview")]/following-sibling::*').extract()
        overview = remove_class(overview)
        overview = clear_same_s(overview)
        # print(overview)
        item['overview_en'] = overview

        modules=response.xpath('//h2[contains(text(),"Course content")]/following-sibling::*').extract()
        modules = remove_class(modules)
        modules = clear_same_s(modules)
        # print(modules)
        item['modules_en'] = modules

        career=response.xpath('//h2[contains(text(),"Employ")]/following-sibling::*').extract()
        career=remove_class(career)
        career=clear_same_s(career)
        # print(career)
        item['career_en'] = career

        rntry=response.xpath('//h2[contains(text(),"Entry")]/following-sibling::ul').extract()
        rntry=remove_class(rntry)
        rntry=clear_same_s(rntry)
        # print(rntry)
        item['rntry_requirements'] = rntry

        accessment=response.xpath('//h2[contains(text(),"Assessment")]/following-sibling::*').extract()
        accessment=remove_class(accessment)
        accessment=clear_same_s(accessment)
        item['assessment_en'] = accessment

        fees=response.xpath('//*[contains(text(),"£")]//text()').extract()
        tuition_fee=getTuition_fee(fees)
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee

        department=response.xpath('//a[contains(text(),"Subject area")]/text()').extract()
        department=list(set(department))
        department=''.join(department)
        department=department.replace('Subject area:','').strip()
        # print(department)
        item['department'] = department

        item['require_chinese_en']='<p>A minimum score of 70%-80%. Offers within the grade range are determined by the higher education institution attended.</p>'
        # item['start_date'] = '2018-9,2019-1'

        start_date=response.xpath('//h6[contains(text(),"tart date")]/following-sibling::p[1]//text()').extract()
        start_date=set(start_date)
        start_date=tracslateDate(start_date)
        # print(start_date)
        start_date=','.join(start_date)
        item['start_date']=start_date
        ielts=response.xpath('//li[contains(text(),"IELTS")]//text()|//b[contains(text(),"IELTS")]/../text()').extract()
        ielts=get_ielts(ielts)
        # print(ielts)
        if ielts!=[] and ielts!={}:
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            item['ielts'] = ielts['IELTS']

        duration=response.xpath('//*[contains(text(),"Mode of ")]/following-sibling::p[1]/text()').extract()
        # print(duration)
        duration=''.join(duration).replace('-',' ')
        loca=re.findall('delivered[\sA-Za-z,]*',duration)
        if loca!=[]:
            item['location']='Cambridge'
        duration=clear_duration(duration)
        # print(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']

        assessment=response.xpath('//h2[@id="assessment"]/following-sibling::*').extract()
        assessment=remove_class(assessment)
        item['assessment_en']=assessment

        apply_preces_en=["<h2><span>How to apply</span></h2>",
"<p><span>All applications for full-time undergraduate courses must be made through the Universities and Colleges Admissions Service <a>(UCAS).&nbsp;</a></span></p>",
"<p><s><span></span></s>Our institution code is <b>B84 BRUNL</b>.</p>",
"<p>UCAS allows you to apply for up to five courses per year. If you wish to apply for more than one course with us, you&rsquo;ll normally have to make a separate entry for each choice.</p>",
"<p>You&rsquo;ll need to write a personal statement that explains why you want to do the courses you&rsquo;ve applied for. See our <a >top tips for your Personal Statement.&nbsp;</a></p>",
"<p>If you're an international applicant applying through one of our registered agents you may be applying to us directly through our online agent facility. Please note we can only consider direct online applications through agents if you have not applied through UCAS and will not apply through UCAS for this year of&nbsp;entry. To find a Brunel University London registered agent in your country please check our specific <a>country pages</a>.</p>",]
        apply_preces_en=remove_class(apply_preces_en)
        item['apply_proces_en']=apply_preces_en

        # print(programme)
        # yield item
        # print(item)