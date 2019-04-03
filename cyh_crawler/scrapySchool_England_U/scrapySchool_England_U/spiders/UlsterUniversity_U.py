# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem

class UlsteruniversityUSpider(scrapy.Spider):
    name = 'UlsterUniversity_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.ulster.ac.uk/courses?query=&f.Level|Y=Undergraduate&f.Attendance|modeft=Full-time&f.Entry_year|entryyear=201920&start_rank=1']
    def parse(self, response):
        # print(response.url)
        pro_url=response.xpath('//div[@id="course_list"]/section/a/@href').extract()
        # print(pro_url)
        for i in pro_url:
            yield scrapy.Request(url=i,callback=self.parse_main)
        next_url=response.xpath('//a[@rel="next"]/@href').extract()
        # print(next_url)
        if next_url!=[]:
            next_urls='https://www.ulster.ac.uk/'+''.join(next_url)
            yield scrapy.Request(url=next_urls,callback=self.parse)
    def parse_main(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'Ulster University'
        item['url'] = response.url
        item['location'] = 'Belfast'

        programme = response.xpath('//h1//text()').extract()
        programme = ''.join(programme).strip()
        # print(programme)
        degr = re.findall('-.+', programme)
        degr = ''.join(degr)
        # print(degr)
        programme = programme.replace(degr, '').replace('*', '').strip()
        degr = degr.replace('-', '').strip()
        # print(degr)
        # print(programme)
        item['programme_en'] = programme
        item['degree_name'] = degr


        overview = response.xpath('//h2[contains(text(),"Overview")]/following-sibling::*').extract()
        overview = remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        modules = response.xpath('//div[@id="modules"]').extract()
        modules = remove_class(modules)
        # print(modules)
        item['modules_en'] = modules

        rntry = response.xpath('//div[@id="entryconditions"]').extract()
        rntry = remove_class(rntry)
        # item['rntry_requirements'] = rntry

        career = response.xpath('//div[@id="opportunities"]').extract()
        career = remove_class(career)
        item['career_en'] = career

        start_date = response.xpath('//h3[contains(text(),"Start dates")]/following-sibling::*//text()').extract()
        start_date = tracslateDate(start_date)
        start_date = set(start_date)
        # print(start_date)
        start_date = '.'.join(start_date).strip()
        item['start_date'] = start_date

        # item['deadline'] = '2019-6'

        ielts = response.xpath('//*[contains(text(),"IELTS")]//text()').extract()
        ielts = get_ielts(ielts)
        # print(ielts)
        try:
            if ielts != [] or ielts != {}:
                item['ielts_l'] = ielts['IELTS_L']
                item['ielts_s'] = ielts['IELTS_S']
                item['ielts_r'] = ielts['IELTS_R']
                item['ielts_w'] = ielts['IELTS_W']
                item['ielts'] = ielts['IELTS']
        except:
            pass

        fee = response.xpath('//dt[contains(text(),"International:")]/following-sibling::dd/text()').extract()
        tuition_fee = getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = '£'

        ucascode=response.xpath('//dd[contains(text(),"UCAS code")]/text()').extract()
        ucascode=''.join(ucascode).strip()
        ucascode=ucascode.replace('UCAS code:','').strip()
        # print(ucascode)
        item['ucascode']=ucascode

        department=response.xpath('//h3[contains(text(),"For more information visit")]/following-sibling::p/a/text()').extract()
        department=';'.join(department).strip()
        # print(department)
        item['department']=department

        item['require_chinese_en']='<p>Each programme will have slightly different requirements, both in terms of overall points and certain subjects, so please check the relevant subject in the undergraduate on-line prospectus.</p><p>Normally Ulster University welcomes applications from students with:</p><h4>Bachelors Degree - Completion of Year One</h4><p>Candidates who have completed the first year of a Bachelors Degree at a Chinese university may be considered for progression onto our undergraduate programmes.</p><h4>Higher National Diploma</h4><p>Candidates who have undertaken a Higher National Diploma may be considered for entrance to our undergraduate programmes.</p><h4>Zhuanke/Dazhuan</h4><p>Candidates who have undertaken the Zhuanke or Dazhuan will be considered for entrance to our undergraduate programmes. Candidates who have undertaken two years or more may be considered for Year two entry, if comparable modules to the Year one syllabus at Ulster University have been studied.</p>',

        alevel=response.xpath('//p[contains(text(),"A Level")]/text()').extract()
        alevel='\n'.join(alevel).strip()
        # print(alevel)
        item['alevel']=alevel

        ib=response.xpath('//h3[contains(text(),"International Baccalaureate")]/following-sibling::p[1]/text()').extract()
        ib=''.join(ib).strip()
        # print(ib)
        item['ib']=ib

        # print(item)
        yield item