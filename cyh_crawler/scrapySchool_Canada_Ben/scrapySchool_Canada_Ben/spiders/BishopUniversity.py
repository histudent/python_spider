# -*- coding: utf-8 -*-
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import *
from scrapySchool_Canada_Ben.items import *

class BishopuniversitySpider(scrapy.Spider):
    name = 'BishopUniversity'
    # allowed_domains = ['a.b']
    start_urls = ['http://www.ubishops.ca/academic-programs/z-listing-academic-programs/']

    def parse(self, response):
        urls=response.xpath('//div[@class="su-table"]/table/tbody/tr/td[contains(text(),"Bachelor")]/preceding-sibling::td/a/@href'
                            '|//div[@class="su-table"]/table/tbody/tr/td[contains(text(),"Honours")]/preceding-sibling::td/a/@href'
                            '|//div[@class="su-table"]/table/tbody/tr/td[contains(text(),"Major")]/preceding-sibling::td/a/@href').extract()
        programme=response.xpath('//div[@class="su-table"]/table/tbody/tr/td[contains(text(),"Bachelor")]/preceding-sibling::td/a/text()'
                                 '|//div[@class="su-table"]/table/tbody/tr/td[contains(text(),"Honours")]/preceding-sibling::td/a/text()'
                                 '|//div[@class="su-table"]/table/tbody/tr/td[contains(text(),"Major")]/preceding-sibling::td/a/text()').extract()
        for u,pro in zip(urls,programme):
            # print(u)
            # print(pro)
            yield scrapy.Request(url=u,callback=self.parses,meta={'programme':pro},dont_filter = True)
        # print(len(urls))
    def parses(self,response):
        item=get_item(ScrapyschoolCanadaBenItem)
        item['url']=response.url
        item['school_name']="Bishop's University"
        item['deadline']='2019-05-15'
        item['start_date']='2019-09'
        item['ielts_desc']='IELTS minimun overall score of 6.5'
        item['toefl_desc']='TOEFL minimun overall score of 90(Internet-based)'
        item['ielts']='6.5'
        item['toefl']='90'
        item['apply_fee']='65.00'
        item['apply_pre']='$'
        item['tuition_fee']='20,000'
        item['tuition_fee_pre']='$'

        print(response.url)
        programme=response.meta['programme']
        # print(programme)
        item['major_name_en']=''.join(programme)
        department=response.xpath('//ul[@id="breadcrumbs"]/li[5]/a/text()').extract()
        # print(department)
        item['department']=''.join(department)
        if department=='Faculty of Arts and Science':
            item['ap']='<p>Completed high school diploma</p><p>Academically strong and well-rounded</p><ul><li>Biology, Biochemistry, Neuroscience: 3.60 GPA</li><li>All others: 3.50 GPA</li><li>Required grade 12 course(s): English, Pre-Calculus or Calculus, 2 of Biology, Chemistry, or Physics</li></ul>'
            item['ib'] = '<p>Completed IB Diploma,Minimum predicted IB Diploma score of 30, not including EE/TOK bonus points.</p>'
            item['alevel']='<p>We are looking for academically strong and well-rounded students with academic requirements as follows:</p><ul><li>Five GCSE results with no mark below a “C” plus three A-Level results with a minimum B/B/C</li></ul><p>We require all British Curriculum students to present English Language or Literature at either the GSCE or A level and recommend Further Math for business, sciences, mathematics, psychology and economics programs.</p><p>Students who complete three A-Level exams with no grade lower than C are eligible to receive 30 advanced standing credits, equivalent to one year of full-time study.</p><ul><li>Course Requirements: A-Level or AS-Level Mathematics, One&nbsp;A-Level or AS-Level Science, and One additional Science subject (A, AS, or GSCE-Level)</li></ul>'
            item['entry_requirements_en']='<ul><li>Completed secondary school credential that would permit you access to university in that country.&nbsp;If you are studying at&nbsp;or have graduated&nbsp;from secondary school in&nbsp;a&nbsp;country&nbsp;where secondary school finishes after only&nbsp;11 years of formal schooling, you may not&nbsp;apply directly to Bishop’s University. &nbsp;You will need to complete at least one year of study at a college or university before applying to transfer to Bishop’s.</li><li>Minimum average required varies depending upon curriculum followed; transcripts are reviewed on an individual basis.</li></ul><ul><li>Course Requirements: University-entrance Mathematics, two university-entrance Sciences (usually Biology, Chemistry, or Physics)</li></ul>'
        elif department=='Williams School of Business':
            item['alevel']='<p>We are looking for academically strong and well-rounded students with academic requirements as follows:</p><ul><li>Five GCSE results with no mark below a “C” plus three A-Level results with a minimum B/B/C</li></ul><p>We require all British Curriculum students to present English Language or Literature at either the GSCE or A level and recommend Further Math for business, sciences, mathematics, psychology and economics programs.</p><p>Students who complete three A-Level exams with no grade lower than C are eligible to receive 30 advanced standing credits, equivalent to one year of full-time study.</p><ul><li>Course Requirements: A-Level or AS-Level Mathematics</li><li>Three A-Level results with a minimum B/B/B</li></ul>'
            item['ib']='<p>Completed IB Diploma,Minimum predicted IB Diploma score of 30, not including EE/TOK bonus points.</p><ul><li>Required IB courses: 1 of Mathematics HL or SL or Further Mathematics HL or SL</li></ul>'
            item['ap']='<p>Completed high school diploma</p><p>Academically strong and well-rounded</p><ul><li>3.80 GPA</li><li>Required grade 12 course(s): English, Mathematics (Pre-Calculus or Calculus recommended)</li></ul>'
            item['entry_requirements_en']='<ul><li>Completed secondary school credential that would permit you access to university in that country.&nbsp;If you are studying at&nbsp;or have graduated&nbsp;from secondary school in&nbsp;a&nbsp;country&nbsp;where secondary school finishes after only&nbsp;11 years of formal schooling, you may not&nbsp;apply directly to Bishop’s University. &nbsp;You will need to complete at least one year of study at a college or university before applying to transfer to Bishop’s.</li><li>Minimum average required varies depending upon curriculum followed; transcripts are reviewed on an individual basis.</li></ul><ul><li>Course Requirements: University-entrance&nbsp;Mathematics</li></ul>'
        else:
            item['alevel']='<p>We are looking for academically strong and well-rounded students with academic requirements as follows:</p><ul><li>Five GCSE results with no mark below a “C” plus three A-Level results with a minimum B/B/C</li></ul><p>We require all British Curriculum students to present English Language or Literature at either the GSCE or A level and recommend Further Math for business, sciences, mathematics, psychology and economics programs.</p><p>Students who complete three A-Level exams with no grade lower than C are eligible to receive 30 advanced standing credits, equivalent to one year of full-time study.</p>'
            item['ap']='<p>Completed high school diploma</p><p>Academically strong and well-rounded</p>'
            item['ib'] = '<p>Completed IB Diploma,Minimum predicted IB Diploma score of 30, not including EE/TOK bonus points.</p>'
            item['entry_requirements_en'] = '<ul><li>Completed secondary school credential that would permit you access to university in that country.&nbsp;If you are studying at&nbsp;or have graduated&nbsp;from secondary school in&nbsp;a&nbsp;country&nbsp;where secondary school finishes after only&nbsp;11 years of formal schooling, you may not&nbsp;apply directly to Bishop’s University. &nbsp;You will need to complete at least one year of study at a college or university before applying to transfer to Bishop’s.</li><li>Minimum average required varies depending upon curriculum followed; transcripts are reviewed on an individual basis.</li></ul>'

        # if 'courses-programs'in response.url:
        #     print(response.url)

        overveiw=response.xpath('//h2[contains(text(),"Structure")]/following-sibling::*|//div[@class="bu-col bu-col-3-4 intro-container"]').extract()
        item['overview_en']=remove_class(overveiw)

        modules=response.xpath('//h2[contains(text(),"Core")]/following-sibling::*|//h1[contains(text(),"Courses & Program")]/following-sibling::div/div/div[@class="su-column su-column-size-3-4"]').extract()
        item['modules_en']=remove_class(modules)

        yield item
