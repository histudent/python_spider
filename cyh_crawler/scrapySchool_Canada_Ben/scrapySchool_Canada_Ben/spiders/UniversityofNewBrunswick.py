# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import *
from scrapySchool_Canada_Ben.items import *
import requests
from lxml import etree
from selenium import webdriver


class UniversityofnewbrunswickSpider(scrapy.Spider):
    name = 'UniversityofNewBrunswick'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.unb.ca/academics/programs/']

    #https://www.unb.ca//international/admission/index.html  国际生入学要求
    #中国学生要求 China: Senior Middle Two and Three results as well as a graduation certificate. Students may also be asked to report scores from the National College Entrance Examination grades of 70% or above.
    #https://www.unb.ca/moneymatters/tuition-fees.html 学费  #15,951
    #https://www.unb.ca/admissions/important-dates.html 申请截止日期
    #125 $
    #International students require an IELTS 6.5  英语语言要求

    def parse(self, response):
        urls=response.xpath('//tr[contains(@class,"program")]/td[1]/a/@href').extract()
        for ul in urls:
            ul='https://www.unb.ca/academics/programs/'+ul
            yield scrapy.Request(url=ul,callback=self.parses)
    def parses(self, response):
        item=get_item(ScrapyschoolCanadaBenItem)
        item['url']=response.url
        print(response.url)
        item['school_name']='University of New Brunswick'
        item['apply_fee']='125'
        item['apply_pre']='$'
        item['tuition_fee']='15,951'
        item['tuition_fee_pre']='$'
        item['deadline']='2019-03-31'
        item['ielts_desc']='International students require an IELTS 6.5 '
        item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']='6.5','6.5','6.5','6.5','6.5'
        item['toefl']='85'
        item['require_chinese_en']='<p>China: Senior Middle Two and Three results as well as a graduation certificate. Students may also be asked to report scores from the National College Entrance Examination grades of 70% or above.</p>'
        item['ib']='<p>Students who complete higher level IB courses and achieve a score of 5, 6 or 7 may be eligible for advanced standing and/or transfer credit in the following subject areas (except where otherwise indicated): Biology, Chemistry, Economics, English, French, Geography (Fredericton campus only), German (Fredericton campus only), History, Math and Physics (minimum score of 6 is required in Physics on the Fredericton campus).</p>'
        item['ap']='<p>Students who complete AP courses and achieve a score of 3, 4 or 5 may be eligible for advanced standing and/or transfer credit in the following subject areas (except where otherwise indicated): Art History (Saint John campus only), Biology, Calculus (minimum score of 4 is required in Calculus), Chemistry, Computer Science, Economics, English, French, German (Saint John campus only), History, Human Geography (Fredericton campus only), Physics, Psychology (Fredericton campus only), Spanish and Statistics (Saint John campus only).</p>'

        prog=response.xpath('//h1[contains(@style,"2px")]/text()').extract()
        # print(prog)
        major_name=''.join(prog).strip()
        item['major_name_en']=major_name
        fbc=response.xpath('//strong[contains(text(),"Faculty")]/../text()').extract()
        facu=fbc[0].replace(':','').strip()
        item['department']=facu
        degr=fbc[2].replace(':','').strip()
        item['degree_name']=degr
        camp=fbc[-1].replace(':','').strip()
        item['campus']=camp

        career=response.xpath('//h3[contains(text(),"areer")]/following-sibling::ul').extract()
        item['career_en']=remove_class(career)

        allweb=response.xpath('//strong[contains(text(),"Faculty")]/../following-sibling::*').extract()
        aw_split=response.xpath('//strong[contains(text(),"Faculty")]/../following-sibling::h3[1]/self::*').extract()
        if aw_split!=[]:
            overview=allweb[0:allweb.index(aw_split[0])]
        else:
            overview=allweb
        item['overview_en']=remove_class(overview)

        # yield item
