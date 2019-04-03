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
class UniversityofleicesterSpider(scrapy.Spider):
    name = 'UniversityOfLeicester_P'
    # allowed_domains = ['a.b']
    start_urls = ['https://le.ac.uk/courses?Page=1&level=Postgraduate&location=Campus-based&q=&mode=Full-time']
    def parse(self, response):
        # print(response.url)
        # pro_url=response.xpath('//h4/a/@href').extract()
        pro_url=['https://le.ac.uk/courses/bioinformatics-and-molecular-genetics-msc',
'https://le.ac.uk/courses/entrepreneurship-msc',
'https://le.ac.uk/courses/innovation-management-in-organisations-msc',
'https://le.ac.uk/courses/media-gender-and-social-justice-ma',]
        # print(len(pro_url))
        for i in pro_url:
            # i=i+'?option=September%202019'
            yield scrapy.Request(url=i,callback=self.parse_main)
        # next_page=response.xpath('//a[@aria-label="Next"]/@href').extract()
        # if next_page!=[]:
        #     next_url='https://le.ac.uk/courses'+next_page[0]
        #     yield scrapy.Request(url=next_url,callback=self.parse)
    def parse_main(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university']='University of Leicester'
        item['url']=response.url
        item['tuition_fee_pre']='£'

        department=response.xpath('//dt[contains(text(),"Department")]/following-sibling::dd/text()').extract()
        department=''.join(department).strip()
        # print(department)
        item['department']=department

        overview=response.xpath('//h2[contains(text(),"Course description")]/following-sibling::*').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en']=overview

        chinese_require=["<p>",
"If you have completed a four-year Bachelors degree in China, you can be considered for entry to a Masters degree at Leicester. Our requirements depend on the rank of the university from which you graduated and your chosen Masters degree. The following is intended as a guide to our requirements:</p>",
"<p>If you have graduated from a 'top 200' university in China, you may be asked for 70% overall if you are applying for an Engineering or Science degree, or 75% for an Arts, Humanities, Law or Social Science degree. You may need to have scores of at least 80% in modules that are particularly relevant to your chosen Master&rsquo;s degree. The School of Museum Studies requires at least 80% overall.</p>",
"<p>If you graduated from a Chinese university ranked below the top 200 you may require higher scores (80-85%).</p>",
"<p>If you have completed a three-year college diploma from a Chinese university, you will need to take an accepted one-year Pre-Masters course or upgrade your diploma to a Bachelor&rsquo;s degree before applying for a Master&rsquo;s degree.</p>",]
        chinese_require=remove_class(chinese_require)
        item['require_chinese_en']=chinese_require

        rntry=response.xpath('//h2[contains(text(),"Entry requirements")]/following-sibling::*').extract()
        rntry=remove_class(rntry).replace('International Qualifications','').replace('Countries list','').replace('Find your country in this list to check equivalent qualifications, scholarships and additional requirements.','')
        # print(rntry)
        item['rntry_requirements']=rntry

        fee=response.xpath('//h3[contains(text(),"International Students")]/following-sibling::*//text()').extract()
        tuition_fee=getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee']=tuition_fee

        career=response.xpath('//div[@id="careers"]').extract()
        career=remove_class(career)
        # print(career)
        item['career_en']=career

        modules=response.xpath('//div[@id="course-structure"]').extract()
        modules=remove_class(modules)
        item['modules_en']=modules

        assessment=response.xpath('//h2[contains(text(),"Teaching and learning")]/following-sibling::div').extract()
        assessment=remove_class(assessment)
        item['assessment_en']=assessment

        ielts=response.xpath('//*[contains(text(),"IELTS")]//text()').extract()
        ielts=get_ielts(ielts)
        # print(ielts)
        if ielts!=[]:
            item['ielts']=ielts['IELTS']
            item['ielts_l']=ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']

        if item['ielts']==6.0:
            item['toefl']=80
        elif item['ielts']==6.5:
            item['toefl']=90
        elif item['ielts']==7.0:
            item['toefl']=100
        if item['toefl']!=None:
            item['toefl_l']='17'
            item['toefl_s']='20'
            item['toefl_r']='18'
            item['toefl_w']='17'

        programme=response.xpath('//span[contains(text(),"Course")]/following-sibling::span/text()').extract()
        # print(programme)
        degree_name=response.xpath('//span[contains(text(),"Qualification")]/following-sibling::span/text()').extract()
        # print(degree_name)
        duration=response.xpath('//span[contains(text(),"Duration")]/following-sibling::span/text()').extract()
        # print(duration)
        start_date=response.xpath('//span[contains(text(),"Start Dates")]/following-sibling::span/text()').extract()
        # print(start_date)
        if start_date==[]:
            start_date=['','','','']
        for pro,deg,dur,sta in zip(programme,degree_name,duration,start_date):
            item['programme_en']=pro
            item['degree_name']=deg
            dura=clear_duration(dur)
            item['duration']=dura['duration']
            item['duration_per']=dura['duration_per']
            sta=tracslateDate(sta)
            sta=','.join(sta)
            item['start_date']=sta
            mode=re.findall('(?i)full',dur)
            if mode!=[]:
                item['teach_time']='fulltime'
                if deg!='PGDip' and deg!='PGCert' and deg!='PGCE':
                    # print(item)
                    yield item
            else:
                item['teach_time']='parttime'
                if deg!='PGDip' and deg!='PGCert' and deg!='PGCE':
                    # print(item)
                    yield item
