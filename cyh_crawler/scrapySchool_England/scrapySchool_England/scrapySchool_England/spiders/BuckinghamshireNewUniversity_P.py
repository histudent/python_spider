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
class BuckinghamshirenewuniversityPSpider(scrapy.Spider):
    name = 'BuckinghamshireNewUniversity_P'
    # allowed_domains = ['a.b']
    start_urls = ['https://bucks.ac.uk/pgcourses']
    def parse(self, response):
        # print('获取到一个列表页',response.url)
        pro_url=response.xpath('//h4/strong/a/@href').extract()
        for i in pro_url:
            if '-pt' in i:
                print('跳过一个兼职链接',i)
            else:
                print('抓取',i)
                yield scrapy.Request(i,callback=self.parses)
        next_page=response.xpath('//a[contains(text(),"Next")]/@href').extract()
        if next_page!=[]:
            next_url=next_page[0]
            yield scrapy.Request(next_url,callback=self.parse)
    def parses(self,response):
        # print('进入专业链接页面',response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        item['url']=response.url
        item['university']='Buckinghamshire New University'
        location = response.xpath('//ul[@class="course-details"]/li[contains(text(),"Location")]/text()').extract()
        location = ''.join(location).replace('Location:', '').strip()
        # print(location)
        programme = response.xpath('//h1[@class="banner-title"]/text()').extract()
        item['programme_en'] = ''.join(programme).strip()
        degree_name = response.xpath('//p[@class="school-code"]/text()').extract()
        item['degree_name'] = ''.join(degree_name).strip()
        item['location'] = location
        duration=response.xpath('//ul[@class="course-details"]/li[contains(text(),"Duration")]/text()').extract()
        duration=clear_duration(duration)
        # print(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']
        start_date=response.xpath('//ul[@class="course-details"]/li[contains(text(),"Start Date")]/text()').extract()
        start_date=tracslateDate(start_date)
        # print(start_date)
        overview = response.xpath('//h2[contains(text(),"Course Overview")]/..').extract()
        item['overview_en'] = remove_class(overview)
        modules = response.xpath('//h2[contains(text(),"Course Modules")]/..').extract()
        item['modules_en'] = remove_class(modules)
        career = response.xpath('//h2[contains(text(),"Employability")]/..').extract()
        item['career_en'] = remove_class(career)
        entry = response.xpath(
            '//h3[contains(text(),"What are the course entry requirements?")]/following-sibling::p[position()<=3]').extract()
        if entry==[]:
            print(response.url)
        else:
            print(entry)
        item['rntry_requirements']=remove_class(entry)
        item['tuition_fee']='11500'
        # item['apply_desc_en']=remove_class(entry)
        chi=[' <div>  ',
' <p>Academic entry requirements</p ><p>We require successful completion of a 学士学位 (Bachelor degree) or successful completion of a three-year 本科毕业证书 (Benke) with an overall pass from a UK NARIC-recognised or Ministry of Education-listed institution.</p ><p>Mathematics entry requirements</p ><p>Students need the equivalent of GCSE Mathematics grade C/4.</p >  ',
' </div>  ',]
        htp=['<p>There&rsquo;s still time to apply for September 2018. Visit our <a hre>clearing section</a> to find out more.</p><p><strong>Check you meet the entry requirements</strong></p><p>Once you&rsquo;ve had a good look at our course information, and chosen which one feels right for you, before applying it&rsquo;s worth checking that you meet the entry requirements for your country.</p><p>We welcome applications from students with a wide range of qualifications from around the world. You&rsquo;ll find details of the exact academic and English language requirements for your country on our <a hre>country pages</a>.</p><p>Every student studying with us also needs to meet our <a hre>English language requirements</a> and we will ask you to provide evidence to show you have good enough English to study a higher education course in the UK.</p><p><strong>Different ways to apply</strong></p><p>When you are ready to apply for your course, you can do so in one of three ways:</p><ul><li>directly through our <a href="https://www.applycpd.com/bucks?tabid=21">application portal</a></li><li>through <a hre>UCAS</a>, or</li><li>through a recruitment agent in your country (see <a hre>your country page</a> for details of agents we work with who are operating locally to you).</li></ul><p>It doesn&rsquo;t matter which of these routes you use, but we advise you to apply early to give yourself enough time to prepare for moving to the UK and arranging your visa, if you need one.</p><p>If you&rsquo;ve missed out on your first choices, declined any offers made to you, or you&rsquo;re applying to university after&nbsp;30 June, you can also apply to us through <a hre>Clearing</a>.</p>',]
        item['require_chinese_en']=remove_class(chi)
        item['apply_desc_en']=remove_class(htp)
        item['ielts']='6.0'
        item['ielts_l']='5.5'
        item['ielts_s'] = '5.5'
        item['ielts_r'] = '5.5'
        item['ielts_w'] = '5.5'

        yield item