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

class UniversityofbedfordshirePSpider(scrapy.Spider):
    name = 'UniversityofBedfordshire_P'
    allowed_domains = ['beds.ac.uk']
    start_urls = ['https://www.beds.ac.uk/howtoapply/courses/postgraduate']

    def parse(self, response):
        # print(response.url)
        pro_url=response.xpath('//h2/a/@href').extract()
        # print(len(pro_url))
        for i in pro_url:
            yield scrapy.Request(i,callback=self.parse_main)
    def parse_main(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)

        item['university']='University of Bedfordshire'
        item['url']=response.url

        programme=response.xpath('//div[@id="inner-course-content"]/h1/text()').extract()
        # print(programme)
        programme=''.join(programme)
        # print(programme)
        item['tuition_fee_pre']='£'
        if 'MBA' in programme:
            # print(programme)
            item['tuition_fee']='14000'
        else:
            item['tuition_fee']='12750'

        programme=programme.split('-')
        if len(programme)==2:
            prog=programme[0].strip()
            degr=programme[1].strip()
            # print(prog)
            # print(degr)
            item['degree_name']=degr
            try:
                if degr[0] == 'M':
                    item['degree_type'] = '2'
                elif degr[0] == 'P':
                    item['degree_type'] = '3'
            except:
                pass
        else:
            prog=''.join(programme).strip()
        item['programme_en']=prog
        location=response.xpath('//strong[contains(text(),"Campus Location")]/../text()').extract()
        location=''.join(location).replace('-','').strip()
        # print(location)
        item['location']=location

        duration=response.xpath('//strong[contains(text(),"Duration")]/../text()').extract()
        duration=clear_duration(duration)
        # print(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']

        mode=response.xpath('//strong[contains(text(),"Attendance")]/../text()').extract()
        mode=''.join(mode)
        mode=re.findall('(?i)full',mode)
        if mode!=[]:
            item['teach_time']='1'
        else:
            item['teach_time']='2'

        start_date=response.xpath('//strong[contains(text(),"Start")]/../text()').extract()
        # print(start_date)
        start_date=tracslateDate(start_date)
        # print(start_date)
        start_date=','.join(start_date)
        # print(start_date)
        item['start_date']=start_date

        overview=response.xpath('//div[@id="why_content"]').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en']=overview

        modules=response.xpath('//div[@id="unit_content"]').extract()
        modules=remove_class(modules)
        # print(modules)
        item['modules_en']=modules

        assessment_en=response.xpath('//div[@id="how_content"]').extract()
        assessment_en=remove_class(assessment_en)
        item['assessment_en']=assessment_en

        rntry=response.xpath('//h2[@id="entry"]/following-sibling::div/ul[@class="tab-content"]/div[3]').extract()
        rntry=remove_class(rntry)
        # print(rntry)
        item['rntry_requirements']=rntry

        item['ielts']='6.0'
        item['ielts_l']='5.5'
        item['ielts_s']='5.5'
        item['ielts_r']='5.5'
        item['ielts_w']='5.5'
        # item['toefl']='80'
        item['toefl_l']='17'
        item['toefl_s']='20'
        item['toefl_r']='18'
        item['toefl_w']='17'

        career=response.xpath('//div[@id="career_content"]').extract()
        career=remove_class(career)
        # print(career)
        item['career_en']=career

        apply_d=['<p>There are two ways you can make a direct application to the University of Bedfordshire:</p><ul><li><a href="https://evision.beds.ac.uk/urd/sits.urd/run/siw_ipp_lgn.login?process=siw_ipp_app&amp;code1=OA_FORM&amp;code2=0007">Apply online now for 2017/18</a> Courses starting from 1 August 2017 to 31 July 2018</li><li>Download <span class="include_asset_summary"><a href="https://www.beds.ac.uk/__data/assets/pdf_file/0006/441798/International-Application-web-2018.pdf">an application form - <img src="https://www.beds.ac.uk/__data/asset_types/pdf_file/icon.png" alt="" title="" height="16" width="16"  class="sq-icon" /> PDF  1.0 MB ',
'</a></span> and submit it to our <a href="https://www.beds.ac.uk/international/international-applications/contactus">Admissions Team</a> along with scans of your supporting documents, via email, post or in person at the International Office.</li></ul><p>You can post your completed form to:</p><p>University of Bedfordshire International Admissions/International Office/University Square/Luton/Bedfordshire/LU1 3JU/United Kingdom</p><h4>Please note</h4><ul><li><strong>BSc (Hons) Nursing Studies</strong> Level 3 and <strong>MSc Advanced Nursing Studies</strong> are available to overseas students - please contact <a href="https://www.beds.ac.uk/international/international-applications/contactus">International Admissions</a></li><li><strong>Healthcare, Nursing and Midwifery students</strong> - many of these courses are not available to overseas students due to UK immigration law in regard to bursary funding. Please contact <a href="https://www.beds.ac.uk/international/international-applications/contactus">International Admissions</a> to find out if you are eligible to apply.</li></ul><p>*Please note that international students studying on a Tier 4 Student Visa must choose a full-time Undergraduate or Postgraduate course and are not eligible for part-time study.</p><p>Watch some more tips and advice on making your application to Bedfordshire:</p>',]
        apply_d='\n'.join(apply_d)
        item['apply_documents_en']=apply_d

        # item['application_open_date']='2018-8'
        # item['deadline']='2019-7'

        # print(item)
        yield item