# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.middlewares import clear_duration,tracslateDate
class BirkbeckuniversityoflondonPSpider(scrapy.Spider):
    name = 'BirkbeckUniversityOfLondon_P'
    # allowed_domains = ['a.b']
    start_urls = ['http://www.bbk.ac.uk/study/2019/postgraduate/']
    def parse(self, response):
        pro_list = response.xpath('//h2[contains(text(),"ubject")]/following-sibling::ol/li/ol/li/a/@href').extract()
        pro_list = list(set(pro_list))
        for i in pro_list:
            yield scrapy.Request(i, callback=self.pro_area)
    def pro_area(self, response):
        pro_url = response.xpath('//h1/following-sibling::ol[1]/li/a/@href').extract()
        for j in pro_url:
            yield scrapy.Request(j, callback=self.programme)
    def programme(self, response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        programme = response.xpath('//h1/text()').extract()
        # print(programme)
        deg = re.findall('\(.*\)', ''.join(programme))
        clears = re.findall(':.*', ''.join(programme))
        # print(deg)
        deg = ''.join(deg)
        programme = ''.join(programme).replace(''.join(clears), '').replace(deg, '').strip()
        # print(programme)
        item['programme_en'] = programme
        item['degree_name'] = deg.replace('(', '').replace(')', '').strip()
        item['url'] = response.url
        start_date = response.xpath('//dt[contains(text(),"tart date")]/following-sibling::dd[1]//text()').extract()
        start_date = tracslateDate(start_date)
        item['start_date'] = ','.join(start_date)
        item['university'] = 'Birkbeck, University of London'
        # item['tuition_fee_pre']='£'
        item['location'] = ''.join(
            response.xpath('//dt[contains(text(),"ocation")]/following-sibling::dd[1]//text()').extract())
        duration = response.xpath('//dt[contains(text(),"uration")]/following-sibling::dd[1]//text()').extract()
        # print(duration)
        mode = re.findall('(?i)full', ''.join(duration))
        # if mode!=[]:
        #     print('这个专业要')
        # else:
        #     print('这个专业只有兼职，不要！！！')
        dura = re.findall('[a-zA-Z0-9\s]+full', ''.join(duration))
        dura = clear_duration(dura)
        # print(dura)
        item['duration'] = dura['duration']
        item['duration_per'] = dura['duration_per']
        overview = response.xpath('//h2[contains(text(),"Highlights")]/preceding-sibling::div[1]').extract()
        overview = remove_class(overview)
        item['overview_en'] = overview
        # print(overview)
        modules = response.xpath('//h2[contains(text(),"Course structure")]/following-sibling::section').extract()
        modules = remove_class(modules)
        item['modules_en'] = modules
        # print(modules)
        # if modules=='':
        #     print(response.url)
        entry = response.xpath('//h2[contains(text(),"ntry requirements")]/following-sibling::*').extract()
        entry = remove_class(entry)
        # print(entry)
        item['rntry_requirements']=entry
        chinese = ['<h3 class="content-show">Postgraduate entry requirements</h3>',
"<ul><li>Please <a>check your postgraduate course online</a> to see if your programme of study has an entry requirement of a UK undergraduate degree with a 2:1 or a 2:2 classification. </li><li>To study a Master's degree that requires a UK undergraduate degree with a <strong>2:2 classification</strong>, you will typically need to have one of the following:</li><ul><li>a Bachelor's degree (<i>Xueshi</i><span>) from a 211, 985 or top national university with an overall average grade of 70% </span></li><li>a Bachelor's degree from a national university with an overall average grade of 75% </li><li>a Bachelor's degree from a high-ranking private university with an overall average grade of 75% </li><li>a Master's degree with an overall average grade of 60%. </li></ul><li>To study a Master's degree that requires a UK undergraduate degree with a <strong>2:1 classification</strong>, you will typically need to have one of the following: </li><ul><li>a Bachelor's degree (<i>Xueshi</i><span>) from a 211, 985 or top national university with an overall average grade of 75% </span></li><li>a Bachelor's degree from a national university with an overall average grade of 80% </li><li>a Bachelor's degree from a high-ranking private university with an overall average grade of 80% </li><li>a Master's degree with an overall average grade of 70%. </li></ul><li>If you do not meet these criteria, you can apply for Birkbeck’s <a>International Foundation Programme</a><span>, which acts as a bridge between undergraduate and postgraduate study, preparing students to study a Master’s degree in the UK. There are progression pathways onto various courses at Birkbeck.</span></li><li>Another option is the <a>Master's Foundation programme</a>, at our partner provider OnCampus London, which is available for two- or three-term progression onto a wide range of Master’s Degrees at Birkbeck.</li><li>If your transcript is provided in GPA format and not a percentage value, <a>please contact our International Office</a> to check your equivalency. For most institutions: </li><ul><li>80% is equivalent to 4/5 or 3.3/4 </li><li>75% is equivalent to 3.5/5 or 2.7/4. </li></ul>"]
        item['require_chinese_en'] = remove_class(chinese)
        item['toefl_desc'] = 'overall score of 92, with 22 in Reading, 21 in Listening, 23 in Speaking, 24 in Writing.'
        item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w'] = '22', '23', '22', '24'
        ielts = 'overall score of 6.5, with 6.0 in each subtest'
        ielts = response.xpath('//*[contains(text(),"IELTS")]//text()').extract()
        # print(ielts)
        ies = re.findall('\d\.?\d?', ''.join(ielts))
        # print(ies)
        if len(ies) == 2:
            ies = list(map(float, ies))
            item['ielts'] = max(ies)
            item['ielts_l'] = min(ies)
            item['ielts_s'] = min(ies)
            item['ielts_r'] = min(ies)
            item['ielts_w'] = min(ies)
        item['ielts_desc'] = '\n'.join(ielts).strip()
        fee = response.xpath('//h2[contains(text(),"Fees")]/following-sibling::p/text()').extract()
        # print(fee)
        assessment = response.xpath('//h2[contains(text(),"Assessment")]/following-sibling::*').extract()
        assessment = remove_class(assessment)
        item['assessment_en'] = assessment
        department = response.xpath('//a[contains(text(),"isit the")]/text()').extract()
        # print(department)
        department = ''.join(department).replace('Visit the', '').strip()
        # print(department)
        item['department'] = department
        howtoapply = response.xpath('//h2[contains(text(),"How to apply")]/following-sibling::*').extract()
        howtoapply = remove_class(howtoapply)
        # print(howtoapply)
        item['apply_proces_en'] = howtoapply
        # print(item)
        if mode!=[]:
            print('这个专业要')
            yield item
        else:
            print('这个专业只有兼职，不要！！！')