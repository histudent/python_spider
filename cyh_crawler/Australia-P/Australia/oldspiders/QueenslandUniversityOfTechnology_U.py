# -*- coding: utf-8 -*-
import scrapy
from Australia.middlewares import *
from Australia.items import AustraliaItem
from lxml import etree
import requests

class QueenslanduniversityoftechnologyUSpider(scrapy.Spider):
    name = 'QueenslandUniversityOfTechnology_U'
    #爬虫起始页
    start_urls = ['https://www.qut.edu.au/']
    def parse(self, response):
        start_area=response.xpath('//h3[contains(text(),"Browse course")]/following-sibling::ul/li/a/@href').extract()
        for i in start_area:
            # print(i)
            yield scrapy.Request(i,callback=self.parse_list)
    def parse_list(self,response):
        # print(response.url)
        programme=response.xpath('//h2[contains(text(),"Undergraduate courses")]/following-sibling::div/table//td/a/text()').extract()
        pro_list=response.xpath('//h2[contains(text(),"Undergraduate courses")]/following-sibling::div/table//td/a/@href').extract()
        # print(len(pro_list),' ',len(programme))
        deg_xpaths='//a[contains(@href,"%s")]/../following-sibling::td[1]//text()'
        for pro,url in zip(programme,pro_list):
            url=url.replace('/courses/','/international-courses/')
            deg_num=re.findall('bachelor',url)
            if deg_num!=[]:
                yield scrapy.Request(url,callback=self.parses)
    def parses(self,response):
        url_list=response.xpath('//p[contains(text(),"Choose an option to see course information:")]/following-sibling::ul[1]/li/a/@href').extract()
        item=get_item(AustraliaItem)
        if url_list==[]:
            print('这个学位页面没有找到专业',response.url)
            htp = response.xpath('//h3[@id="how-to-apply"]/following-sibling::*').extract()
            htp = remove_class(htp)
            item['apply_proces_en'] = htp
            item['university'] = 'Queensland University of Technology'
            item['url'] = response.url
            programme=response.xpath('//h1/a/text()').extract()
            programme=''.join(programme).strip()
            # print(programme)
            deg=re.findall('\(.*\)',programme.replace('(Honours)',''))
            deg=''.join(deg).strip()
            # print(deg)
            if deg == '':
                item['programme_en'] = programme.replace(deg, '').replace('Bachelor of', '').strip()
                item['degree_name'] = programme
            else:
                item['programme_en'] = deg.replace(')', '').replace('(', '').strip()
                item['degree_name'] = programme.replace(deg, '').strip()
            department=response.xpath('//td[contains(text(),"aculty")]/following-sibling::td/ul/li/text()').extract()
            department='\n'.join(department).strip()
            item['department']=department

            start_date=response.xpath('//td[contains(text(),"tart month")]/following-sibling::td/text()').extract()
            start_date=tracslateDate(start_date)
            start_date=','.join(start_date)
            # print(start_date)
            item['start_date']=start_date

            career=response.xpath('//td[contains(text(),"Careers")]/following-sibling::td').extract()
            career=remove_class(career)
            item['career_en']=career

            overview=response.xpath('//table[@class="overview-table"]/preceding-sibling::ul[1]').extract()
            overview=remove_class(overview)
            item['overview_en']=overview

            modules=response.xpath('//div[@id="units"]').extract()
            modules=remove_class(modules)
            item['modules_en']=modules

            rntry=response.xpath('//div[@class="requirement-tables"]').extract()
            rntry=remove_class(rntry)
            item['rntry_requirements_en']=rntry
            chinese=['<p>GAOKAO 60% in best 4 academic subjects.</p>\n','<p>GAOKAO score converted to percentage using Chinese, English/Foreign Language, Mathematics and one other subject (excluding Technology). Percent is the [sum of scores attained for the four units] / [sum of maximum grades for the four units].</p>']
            china_score_requirements=remove_class(chinese)
            item['china_score_requirements']=china_score_requirements
            degree_overview=response.xpath('//div[@id="details"]').extract()
            degree_overview=remove_class(degree_overview)
            item['degree_overview_en']=degree_overview
            fee=response.xpath('//div[@id="costs"]//*[contains(text(),"$")]//text()').extract()
            fee=getTuition_fee(fee)
            item['tuition_fee']=fee
            # print(fee)
            item['tuition_fee_pre']='AUD'
            item['ielts']=''.join(response.xpath('//td[contains(text(),"IELTS Aca")]/following-sibling::td[@id="elt-overall"]/text()').extract()).strip()
            item['ielts_l']=''.join(response.xpath('//td[contains(text(),"IELTS Aca")]/following-sibling::td[@id="elt-listening"]/text()').extract()).strip()
            item['ielts_s']=''.join(response.xpath('//td[contains(text(),"IELTS Aca")]/following-sibling::td[@id="elt-speaking"]/text()').extract()).strip()
            item['ielts_r']=''.join(response.xpath('//td[contains(text(),"IELTS Aca")]/following-sibling::td[@id="elt-reading"]/text()').extract()).strip()
            item['ielts_w']=''.join(response.xpath('//td[contains(text(),"IELTS Aca")]/following-sibling::td[@id="elt-writing"]/text()').extract()).strip()
            item['toefl'] = ''.join(response.xpath(
                '//td[contains(text(),"TOEFL iBT")]/following-sibling::td[@id="elt-overall"]/text()').extract()).strip()
            item['toefl_l'] = ''.join(response.xpath(
                '//td[contains(text(),"TOEFL iBT")]/following-sibling::td[@id="elt-listening"]/text()').extract()).strip()
            item['toefl_s'] = ''.join(response.xpath(
                '//td[contains(text(),"TOEFL iBT")]/following-sibling::td[@id="elt-speaking"]/text()').extract()).strip()
            item['toefl_r'] = ''.join(response.xpath(
                '//td[contains(text(),"TOEFL iBT")]/following-sibling::td[@id="elt-reading"]/text()').extract()).strip()
            item['toefl_w'] = ''.join(response.xpath(
                '//td[contains(text(),"TOEFL iBT")]/following-sibling::td[@id="elt-writing"]/text()').extract()).strip()
            duration=response.xpath('//td[contains(text(),"ourse duration")]/following-sibling::td/text()').extract()
            duration=''.join(duration).strip()
            # print(duration)
            duration=clear_duration(duration)
            item['duration']=duration['duration']
            item['duration_per']=duration['duration_per']
            print(item)
            # yield item
        else:
            # print('有烦人的专业',response.url)
            for i in url_list:
                i=i.replace('/courses/','/international-courses/')
                yield scrapy.Request(i,callback=self.parse_major)
    def parse_major(self,response):
        print('进入专业页面',response.url)
        item=get_item(AustraliaItem)
        programme = response.xpath('//h1/a/text()').extract()
        programme = ''.join(programme).strip()
        # print(programme)

        htp = response.xpath('//h3[@id="how-to-apply"]/following-sibling::*').extract()
        htp = remove_class(htp)
        item['apply_proces_en'] = htp
        item['university'] = 'Queensland University of Technology'
        item['url'] = response.url

        deg = re.findall('\(.*\)', programme.replace('(Honours)', ''))
        deg = ''.join(deg).strip()
        # print(deg)
        if deg=='':
            item['programme_en']=programme.replace(deg,'').replace('Bachelor of','').strip()
            item['degree_name']=programme
        else:
            item['programme_en']=deg.replace(')','').replace('(','').strip()
            item['degree_name']=programme.replace(deg,'').strip()
        print(item['programme_en'])
        print(item['degree_name'])

        department = response.xpath('//td[contains(text(),"aculty")]/following-sibling::td/ul/li/text()').extract()
        department = '\n'.join(department).strip()
        item['department'] = department

        start_date = response.xpath('//td[contains(text(),"tart month")]/following-sibling::td/text()').extract()
        start_date = tracslateDate(start_date)
        start_date = ','.join(start_date)
        # print(start_date)
        item['start_date'] = start_date

        career = response.xpath('//td[contains(text(),"Careers")]/following-sibling::td').extract()
        career = remove_class(career)
        item['career_en'] = career

        overview = response.xpath('//table[@class="overview-table"]/preceding-sibling::ul[1]').extract()
        overview = remove_class(overview)
        item['overview_en'] = overview

        modules = response.xpath('//div[@id="units"]').extract()
        modules = remove_class(modules)
        item['modules_en'] = modules

        rntry = response.xpath('//div[@class="requirement-tables"]').extract()
        rntry = remove_class(rntry)
        item['rntry_requirements_en'] = rntry

        chinese = ['<p>GAOKAO 60% in best 4 academic subjects.</p>\n',
                   '<p>GAOKAO score converted to percentage using Chinese, English/Foreign Language, Mathematics and one other subject (excluding Technology). Percent is the [sum of scores attained for the four units] / [sum of maximum grades for the four units].</p>']
        china_score_requirements = remove_class(chinese)
        item['china_score_requirements'] = china_score_requirements

        degree_overview = response.xpath('//div[@id="details"]').extract()
        degree_overview = remove_class(degree_overview)
        item['degree_overview_en'] = degree_overview

        fee = response.xpath('//div[@id="costs"]//*[contains(text(),"$")]//text()').extract()
        fee = getTuition_fee(fee)
        item['tuition_fee'] = fee
        # print(fee)
        item['tuition_fee_pre'] = 'AUD'

        item['ielts'] = ''.join(response.xpath(
            '//td[contains(text(),"IELTS Aca")]/following-sibling::td[@id="elt-overall"]/text()').extract()).strip()
        item['ielts_l'] = ''.join(response.xpath(
            '//td[contains(text(),"IELTS Aca")]/following-sibling::td[@id="elt-listening"]/text()').extract()).strip()
        item['ielts_s'] = ''.join(response.xpath(
            '//td[contains(text(),"IELTS Aca")]/following-sibling::td[@id="elt-speaking"]/text()').extract()).strip()
        item['ielts_r'] = ''.join(response.xpath(
            '//td[contains(text(),"IELTS Aca")]/following-sibling::td[@id="elt-reading"]/text()').extract()).strip()
        item['ielts_w'] = ''.join(response.xpath(
            '//td[contains(text(),"IELTS Aca")]/following-sibling::td[@id="elt-writing"]/text()').extract()).strip()

        item['toefl'] = ''.join(response.xpath(
            '//td[contains(text(),"TOEFL iBT")]/following-sibling::td[@id="elt-overall"]/text()').extract()).strip()
        item['toefl_l'] = ''.join(response.xpath(
            '//td[contains(text(),"TOEFL iBT")]/following-sibling::td[@id="elt-listening"]/text()').extract()).strip()
        item['toefl_s'] = ''.join(response.xpath(
            '//td[contains(text(),"TOEFL iBT")]/following-sibling::td[@id="elt-speaking"]/text()').extract()).strip()
        item['toefl_r'] = ''.join(response.xpath(
            '//td[contains(text(),"TOEFL iBT")]/following-sibling::td[@id="elt-reading"]/text()').extract()).strip()
        item['toefl_w'] = ''.join(response.xpath(
            '//td[contains(text(),"TOEFL iBT")]/following-sibling::td[@id="elt-writing"]/text()').extract()).strip()
        duration = response.xpath('//td[contains(text(),"ourse duration")]/following-sibling::td/text()').extract()
        duration = ''.join(duration).strip()
        # print(duration)
        duration = clear_duration(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']

        # print(item)
        # yield item