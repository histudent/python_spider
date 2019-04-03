# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.middlewares import clear_duration,tracslateDate
from scrapySchool_England.clearSpace import clear_lianxu_space,clear_same_s
class LeedsbeckettuniversityPSpider(scrapy.Spider):
    name = 'LeedsBeckettUniversity_P'
    allowed_domains = ['leedsbeckett.ac.uk']
    start_urls = ['https://courses.leedsbeckett.ac.uk/search/courseresults/?q=&year=&level=1&startdates=&attendances=Full-time&semester=&ukeuinternationalreq=&page=']
    def parse(self, response):
        pro_url=response.xpath('//h3/a/@href').extract()
        for i in pro_url:
            URL='https://courses.leedsbeckett.ac.uk'+i
            yield scrapy.Request(url=URL,callback=self.parse_main)
    def parse_main(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university']='Leeds Beckett University'
        item['url']=response.url
        location=response.xpath('//div[contains(text(),"Location")]/following-sibling::span/text()').extract()
        location=set(location)
        location=''.join(location).strip()
        # print(location)
        item['location']='Leeds'

        degree_name=response.xpath('//div[@class="course-hero__label"]/text()').extract()
        degree_name=''.join(degree_name).strip()
        item['degree_name']=degree_name
        programme=response.xpath('//h1[@class="course-hero__title"]/text()').extract()
        programme=''.join(programme).strip()
        # print(programme)
        # print(degree_name)
        item['programme_en']=programme

        department=response.xpath('//div[@class="course-hero__labels"]/a/text()').extract()
        department=''.join(department)
        # print(department)
        item['department']=department

        mode=response.xpath('//div[contains(text(),"Attendance")]/following-sibling::div//text()').extract()
        mode=''.join(mode)
        mode=re.findall('(?i)full',mode)
        if mode!=[]:
            item['teach_time']='1'
        else:
            item['teach_time']='2'

        start_date=response.xpath('//div[contains(text(),"Start Date")]/following-sibling::div//text()').extract()
        start_date=tracslateDate(start_date)
        start_date=set(start_date)
        # print(start_date)
        start_date=','.join(start_date)
        item['start_date']=start_date

        duration=response.xpath('//div[contains(text(),"Duration")]/following-sibling::span//text()').extract()
        duration=clear_duration(duration)
        # print(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']

        overview=response.xpath('//h2[contains(text(),"Overview")]/../following-sibling::div').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en']=overview

        rntry=response.xpath('//h2[contains(text(),"Entry Requirements")]/../following-sibling::div').extract()
        rntry=remove_class(rntry)
        item['rntry_requirements']=rntry

        IELTS=response.xpath('//div[@class="entry-ielts"]/text()').extract()
        ielts=get_ielts(IELTS)
        # print(ielts)
        try:
            if ielts!=[] or ielts!={}:
                item['ielts_l']=ielts['IELTS_L']
                item['ielts_s'] = ielts['IELTS_S']
                item['ielts_r'] = ielts['IELTS_R']
                item['ielts_w'] = ielts['IELTS_W']
                item['ielts'] = ielts['IELTS']
        except:
            pass

        career=response.xpath('//h3[contains(text(),"Careers")]/following-sibling::div').extract()
        career=remove_class(career)
        item['career_en']=career

        modules=response.xpath('//div[@class="course-modules__table-modules"]//div[@class="course-modules__dropdowns"]').extract()
        modules=remove_class(modules)
        # print(modules)
        item['modules_en']=modules

        fee=response.xpath('//div[contains(text(),"£")]/text()').extract()
        fee=''.join(fee).strip()
        fee=re.findall('£\d{3,}',fee)
        fee = '-'.join(fee).replace(',', '').replace('£', '')
        fee = fee.split('-')
        try:
            fee = list(map(int, fee))
            fee = max(fee)
            item['tuition_fee']=fee
        except:
            pass
        item['tuition_fee_pre']='£'

        apply_d=["Academic Certificates.",
"Evidence of your English language ability (see below).",
"A photocopy of your passport.",
"A reference to support your application – either academic or professional.",
"A completed Agent Consent Form (required if you are applying via or with the help of an agent).",]
        apply_d='\n'.join(apply_d)
        item['apply_documents_en']=apply_d

        apply_p=["Applying for a postgraduate course",
"Once you have found the course you want to study in our online prospectus you will then click on the ‘Apply Now’ button located at the top of the online course page. ",
"You will be asked to create an account on our application portal and complete your application via your Leeds Beckett account. Once you have submitted your application you should receive a decision within six weeks of applying. The exception to this is if the course you have applied for has a closing date specified. In this case, we will wait until the closing date has passed before we contact you",]
        apply_p='\n'.join(apply_p)
        item['apply_proces_en']=apply_p

        # print(item)
        yield item