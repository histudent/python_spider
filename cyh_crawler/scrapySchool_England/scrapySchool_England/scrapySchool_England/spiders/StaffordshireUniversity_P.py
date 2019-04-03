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


class StaffordshireuniversityPSpider(scrapy.Spider):
    name = 'StaffordshireUniversity_P'
    allowed_domains = ['staffs.ac.uk']
    start_urls = ['http://search.staffs.ac.uk/s/search.html?collection=courses&meta_V_and=postgraduate&query=&meta_t_and=&f.Mode+of+attendance%7CM=full-time&start_rank=1']
    def parse(self, response):
        # print(response.url)
        pro_url=response.xpath('//article/a/@href').extract()
        for i in pro_url:
            full_url='http://search.staffs.ac.uk'+i
            yield scrapy.Request(url=full_url,callback=self.parses)
        next_page=response.xpath('//a[contains(text(),"Next")]/@href').extract()
        if next_page!=[]:
            next_url='http://search.staffs.ac.uk/s/'+next_page[0]
            yield scrapy.Request(url=next_url,callback=self.parse)
    def parses(self,response):
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university']='Staffordshire University'
        item['url']=response.url
        item['location']='Staffordshire'
        programme=response.xpath('//h1/text()').extract()
        programme=''.join(programme).strip()
        degree_name=response.xpath('//h2[@class="hero_header text-center"]/text()').extract()
        if degree_name==[]:
            degree_name=re.findall('[A-Z]{2,}[a-z]*',programme)
            degree_name=''.join(degree_name).strip()
            item['degree_name']=degree_name
        else:
            item['degree_name']=''.join(degree_name).strip()
        item['programme_en']=programme
        programme=response.xpath('//div[@class="col-sm-9"]/h1/text()|//div[@id="main"]//h1/text()').extract()
        programme=''.join(programme).strip()
        degree=re.findall('[A-Z]{2}[/a-zA-Z\s]*',programme)
        programme=programme.replace(''.join(degree),'').strip()
        if degree==[]:
            degree=response.xpath('//h2[@class="hero_header text-center"]/text()').extract()
        elif degree!=[]:
            degree=''.join(degree)
        else:
            degree=''
        item['degree_name']=''.join(degree).strip()
        item['programme_en']=programme
        duration=response.xpath('//th[contains(text(),"Duration")]/following-sibling::td/text()|//dt[contains(text(),"Duration")]/following-sibling::dd[1]/text()').extract()
        duration=clear_duration(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']
        start_date=response.xpath('//dt[contains(text(),"Academic year:")]/following-sibling::dd/text()').extract()
        if start_date==[]:
            start_date=response.xpath('//th[contains(text(),"Course start")]/following-sibling::td/text()').extract()
        start_date=tracslateDate(start_date)
        item['start_date']=','.join(start_date).strip()
        department=response.xpath('//th[contains(text(),"School")]/following-sibling::td/text()').extract()
        department=''.join(department).strip()
        item['department']=department
        fee=response.xpath('//*[contains(text(),"£")]//text()').extract()
        tuition_fee=getTuition_fee(fee)
        item['tuition_fee']=tuition_fee
        item['tuition_fee_pre']='£'
        overview=response.xpath('//div[@id="key-features"]|'
                                '//section[@class="course-details_section summary-section"]//div[@class="medium-8 medium-pull-4 large-pull-3 column"]').extract()

        overview=remove_class(overview)
        item['overview_en']=overview
        modules=response.xpath('//div[@id="course-content"]|//section[@id="contents"]|//div[@id="course-summary"]').extract()
        modules=remove_class(modules)
        item['modules_en']=modules
        rntry=response.xpath('//div[@id="course-entry-requirements"]|//section[@id="entry"]').extract()
        rntry=remove_class(rntry)
        item['rntry_requirements']=rntry
        career=response.xpath('//div[@id="graduate-destinations"]|//section[@id="careers"]').extract()
        career=remove_class(career)
        item['career_en']=career
        ielts=response.xpath('//*[contains(text(),"IELTS")]//text()').extract()
        ielts=''.join(ielts).strip()
        item['ielts_desc']=ielts
        ielts=get_ielts(ielts)
        try:
            if ielts!=[] or ielts!={}:
                item['ielts_l']=ielts['IELTS_L']
                item['ielts_s'] = ielts['IELTS_S']
                item['ielts_r'] = ielts['IELTS_R']
                item['ielts_w'] = ielts['IELTS_W']
                item['ielts'] = ielts['IELTS']
        except:
            pass
        assessment=response.xpath('//a[contains(text(),"ssessment")]/../following-sibling::div[1]').extract()
        item['assessment_en']=remove_class(assessment)

        yield item
        # print(item)