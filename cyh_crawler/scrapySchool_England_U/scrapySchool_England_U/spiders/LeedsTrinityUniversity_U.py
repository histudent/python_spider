# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem

class LeedstrinityuniversityUSpider(scrapy.Spider):
    name = 'LeedsTrinityUniversity_U'
    # allowed_domains = ['a.b']
    start_urls = ['http://www.leedstrinity.ac.uk/']
    def parse(self, response):
        pro_url=response.xpath('//div[@class="coursesmenu"]//ul/li/a/@href').extract()
        # print(pro_url)
        for i in pro_url:
            full_url='http://www.leedstrinity.ac.uk'+i
            yield scrapy.Request(url=full_url,callback=self.parses)
    def parses(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['location'] = 'Leeds'
        item['university'] = 'Leeds Trinity University'
        item['url'] = response.url
        progremme=response.xpath('//div[@class="course-title"]//h1/text()').extract()
        progremme=''.join(progremme).strip()
        # print(progremme)
        item['programme_en']=progremme
        degree_name=response.xpath('//div[@class="course-title"]//h2/text()').extract()
        degree_name=''.join(degree_name).strip()
        # print(degree_name)
        item['degree_name']=degree_name

        # start_date=response.xpath('//span[contains(text(),"Year of entry")]/span/text()').extract()
        # print(start_date)
        start_date='2019-9'
        item['start_date']=start_date

        open_day=response.xpath('//h4[contains(text(),"Open Days")]/span/text()').extract()
        # print(open_day)
        open_day=tracslateDate(open_day)
        # print(open_day)
        item['application_open_date']=open_day

        duration=response.xpath('//li[contains(text(),"Course Type")]//text()').extract()
        duration=clear_duration(duration)
        # print(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']

        tuition_fee='11250'
        item['tuition_fee']=tuition_fee
        item['tuition_fee_pre']='£'

        item['ielts']='6.0'
        item['ielts_l']='5.5'
        item['ielts_s'] = '5.5'
        item['ielts_r'] = '5.5'
        item['ielts_w'] = '5.5'
        item['ielts_desc']='(IELTS) 6.0 overall with a minimum of 5.5 in each component.'

        item['apply_fee']='150'
        item['apply_pre']='£'

        apply_prose=["<div><h3>Application Stage</h3>",
"<p>1. Complete your application form accurately and in full providing relevant information about your",
"educational history and demonstrating logical progression from your previous academic studies.",
"Your personal statement needs to outline why you are applying for your chosen programme, what",
"you hope to achieve through your studies at Leeds Trinity University, how the programme is",
"relevant to your future goals and how you feel your past/current studies and experience support",
"your application.</p>",
"<p>2. Provide copies of relevant qualification documents with official translations if applicable.</p>",
"<p>3. Meet the University’s academic requirements, including English Language requirements.</p>",
"<p>4. Provide detailed information and related documentation about your immigration and study history",
"if you have lived and/or studied in the UK at any time. You should:",
"i. Provide a consistent and logical study history in the UK which leads to the course you are",
"applying for at Leeds Trinity University.",
"ii. Show satisfactory academic progression in your previous studies.",
"iii. Be applying for a course at a higher level than your previous studies. Exceptionally, and at the",
"University’s discretion, it may be possible to study at the same level where the course is in a",
"related subject area and of a deeper specialisation, in line with Tier 4 academic progression",
"requirements.",
"iv. Meet the UKVI time limit for studying in the UK under Tier 4.</p>",
"<p>5. If your application meets our entry criteria, you will be required to complete a telephone/skype",
"interview with an international admissions tutor.",
"Decision Stage</p>",
"<p>6. If you are eligible to be made an offer, you will receive an offer letter and acceptance form.</p>",
"<p>7. Submit your completed and signed acceptance form.</p>",
"<p>8. Once any academic conditions are met, pay a 50% tuition fee deposit. No refund will be allowed",
"for any reason other than your being refused a visa to study in the UK. Upon receiving visa refusal",
"documents, we will refund you, minus a £150 administration fee.</p>",
"<p>9. Submit the CAS Request Form. You can only request a CAS once your offer is unconditional and you",
"have paid your deposit.</p>",
"<p>10. Once the above have been completed successfully we will send you your CAS by email and you can",
"then apply for your visa. Please keep us informed if there are any delays or problems with your visa",
"application or you will be arriving late to start your course for any reason.</p>",
"<p>11. Complete online registration via e:Vision before the start of the course (your username and",
"password will be emailed to you).</p>",
"<p>12. Bring your passport, visa vignette, BRP, original academic and English language qualifications to",
"Student Administration during Intro week and pay the remaining balance of your tuition fees in",
"order to obtain full registration with the University.</p></div>",]
        apply_prose=''.join(apply_prose)
        item['apply_proces_en']=apply_prose

        overview=response.xpath('//div[@id="info"]').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en']=overview

        modules=response.xpath('//div[@class="sub-tab-content modules-overview"]').extract()
        modules=response.xpath('//h6[@class="sub-sub-tab"]/a/text()').extract()
        # modules=remove_class(modules)
        # print(modules)
        modules='</h3><h3>'.join(modules)
        # print(modules)
        modules='<h3>'+modules+'</h3>'
        # print(modules)
        item['modules_en']=modules

        # rntry=response.xpath('//div[@id="entry"]').extract()
        # rntry=remove_class(rntry)
        # print(rntry)
        rntry='<p>Successful completion of an IFY or year one of university degree with 60%​</p>'
        item['require_chinese_en']=rntry

        assessment=response.xpath('//div[@id="learning"]').extract()
        assessment=remove_class(assessment)
        # print(assessment)
        item['assessment_en']=assessment

        career=response.xpath('//div[@id="placement-information"]//div[@class="container"]').extract()
        career=remove_class(career)
        # print(career)
        item['career_en']=career


        apply_d=["<ul><li>your transcripts</li>",
"<li>English language qualification</li>",
"<li>references (in English)</li>",
"<li>copy of your passport if available</li></ul>",
]
        apply_d='\n'.join(apply_d)
        item['apply_documents_en']=apply_d

        yield item