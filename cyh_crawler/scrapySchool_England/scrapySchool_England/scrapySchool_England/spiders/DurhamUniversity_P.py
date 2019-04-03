# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.middlewares import clear_duration,tracslateDate
from scrapySchool_England.clearSpace import clear_same_s
from urllib.request import urlopen

class DurhamuniversityPSpider(scrapy.Spider):
    name = 'DurhamUniversity_P'
    allowed_domains = ['dur.ac.uk']
    start_urls = ['https://www.dur.ac.uk/courses/all/']
    def parse(self, response):
        programme_url=response.xpath('//tr[contains(@class,"PostgraduateTaught")]/td/a/@href').extract()
        for i in programme_url:
            fullurl='https://www.dur.ac.uk'+i
            yield scrapy.Request(fullurl,callback=self.parses)
    def parses(self, response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university'] = 'Durham University'
        item['url'] = response.url
        item['location'] ='Durham'
        item['tuition_fee_pre'] = '£'
        programme = response.xpath(
            '//div[@id="course"]/div[@class="row-fluid titlebar"]/h1/span[@class="span7 title"]/text()').extract()
        programme = ''.join(programme).strip()
        # print(programme)
        item['programme_en'] = programme
        degree_type = response.xpath(
            '//div[@id="course"]/div[@class="row-fluid titlebar"]/h1//span[@class="type"]/text()').extract()
        degree_type = ''.join(degree_type).strip()
        # print(degree_type)
        item['degree_name'] =degree_type

        duration=response.xpath('//th[contains(text(),"Duration")]/following-sibling::td//text()').extract()
        duration=clear_duration(duration)
        item['duration'] = duration['duration']
        item['duration_per']=duration['duration_per']
        # print(duration)

        mode=response.xpath('//th[contains(text(),"Mode")]/following-sibling::td//text()').extract()
        if mode!=[]:
            item['teach_time']=1
        else:
            item['teach_time']=2

        tuition=response.xpath('//th[contains(text(),"nternational")]/following-sibling::td/text()').extract()
        tuition_fee=getTuition_fee(tuition)
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee

        department=response.xpath('//div[@id="department"]/h3[1]/text()').extract()
        department=' '.join(department)
        # print(department)
        item['department'] = department

        coursecontent=response.xpath('//div[@id="coursecontent"]//*').extract()
        overviewSplit=response.xpath('//div[@id="coursecontent"]/h2[contains(text(),"Structure")]/self::*').extract()
        if overviewSplit!=[]:
            overview=coursecontent[0:coursecontent.index(overviewSplit[0])]
        else:
            overview=coursecontent
        # print(overview)
        item['overview_en']=remove_class(overview)
        modules=response.xpath('//div[@id="coursecontent"]/h2[contains(text(),"Structure")]/following-sibling::*').extract()
        # print(modules)
        item['modules_en']=remove_class(modules)
        # overview=response.xpath('//div[@id="department"]/h5[contains(text(),"verview")]/following-sibling::p').extract()
        # item['overview_en']=remove_class(overview)

        item['ielts'] = '6.5'
        item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']='6.0','6.0','6.0','6.0'
        item['toefl'] ='92'
        item['toefl_l'],item['toefl_l'],item['toefl_l'],item['toefl_l']='23','23','23','23'
        item['ielts_desc'] ='6.5 (no component under 6.0)'
        item['toefl_desc'] ='TOEFL iBT (internet based test): 92 (no component under 23)'

        assessment=response.xpath('//div[@id="learning"]').extract()
        assessment=remove_class(assessment)
        item['assessment_en'] = assessment

        rntry=response.xpath('//div[@id="admissions"]').extract()
        rntry=remove_class(rntry)
        item['rntry_requirements'] = rntry

        # item['apply_pre'] = '£'
        # item['apply_fee'] = '60'
        # item['application_open_date'] = '2018-10-1'
        # item['start_date'] = '2018-9,2019-1,2019-4'
        start_date=response.xpath('//th[contains(text(),"tart Date")]/following-sibling::td/text()').extract()
        start_date=''.join(start_date)
        # print(start_date)
        if start_date!='':
            start_date='2019-10'
            item['start_date']=start_date


        apply_proces=["<p>Apply Online",
"Stage One: Check entry requirements",
"Stage Two: Complete the application form",
"Stage Three: We process your application",
"Stage Four: We communicate a decision",
"Stage Five: Next steps</p>",]
        apply_proces='</p><p>'.join(apply_proces)
        item['apply_proces_en'] = apply_proces

        apply_documents_en=["<p>Personal details",
"Your education and qualifications already achieved and details of any qualifications that you are currently studying for, if applicable",
"The names and addresses of two academic referees",
"A Personal Statement",
"Supporting documents (for example, degree certificates / transcripts, English Language evidence if you are not a native English speaker, CV, samples of academic work).</p>",]
        apply_documents_en='</p><p>'.join(apply_documents_en)
        item['apply_documents_en'] = apply_documents_en

        apply_desc=["<p>The standard minimum entry requirement to study a postgraduate programme at Durham University is normally achievement of an upper second class UK honours degree (2:1) or equivalent qualification and two satisfactory academic references. Full details of qualification equivalencies by country can be found here. For applicants who are not Native English speakers, English language evidence may also be required."
"However, some Academic Departments and programmes have different or additional entry requirements. Therefore, before you apply, it is important to check the appropriate course listing in the courses database or departmental web page to ensure that you meet or are able to meet before the programme commencement date:"
"• The Academic Department and specific programme’s entry requirements and, if applicable, any English language requirements"
"• The financial requirements of the programme you are interested in (including deposit payment, tuition fees and any other associated costs).</p>"]
        apply_desc='</p><p>'.join(apply_desc)
        item['apply_desc_en'] = apply_desc

        career=response.xpath('//div[@id="opportunities"]').extract()
        career=remove_class(career)
        item['career_en'] = career

        # if degree_type not in ['BA', 'BEng', 'BSc', 'PCert', 'PGCE', 'GDip', 'LLB']:
        #     print(item)
        # yield item

        # print(item)
        yield item













