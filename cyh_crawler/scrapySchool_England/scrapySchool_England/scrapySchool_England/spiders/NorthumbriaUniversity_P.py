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

class NorthumbriauniversityPSpider(scrapy.Spider):
    name = 'NorthumbriaUniversity_P'
    # allowed_domains = ['northumbria.ac.uk']
    start_urls=['https://www.northumbria.ac.uk/study-at-northumbria/courses/architecture-march-ft-dufaht1/',
'http://london.northumbria.ac.uk/course/msc-computing-and-information-technology/',
'http://london.northumbria.ac.uk/course/msc-computing-and-information-technology-with-advanced-practice/',
'https://www.northumbria.ac.uk/study-at-northumbria/courses/master-of-clinical-practice-advanced-critical-care-practice-ft-dtpacl6/',]
    def parse(self, response):
        item=get_item1(ScrapyschoolEnglandItem1)
        print(response.url)
        item['location'] = 'Newcastle'
        item['university'] = 'Northumbria University'
        item['url'] = response.url

        programme=response.xpath('//div[@class="col-sm-6"]/h1/text()|//div[@class="hero-content"]/h1/text()|//header[@class="course-heading"]/h1/text()').extract()
        programme=''.join(programme).strip()
        degree_name=re.findall('[A-Z]{2,}.*',programme)
        degree_name=''.join(degree_name)
        if degree_name!=programme:
            programme=programme.replace(degree_name,'')
        item['programme_en'] = programme
        item['degree_name'] = degree_name
        try:
            if degree_name[0] == 'M':
                item['degree_type'] = '2'
            elif degree_name[0] == 'P':
                item['degree_type'] = '3'
        except:
            pass


        dur=response.xpath('//strong[contains(text(),"Mode")]/../text()|//span[contains(text(),"uration")]/../text()').extract()
        # print(dur)
        duration=clear_duration(dur)
        # print(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']
        item['teach_time'] = '1'

        start_date=response.xpath('//strong[contains(text(),"Start")]/../text()|//span[contains(text(),"Start")]/../text()').extract()
        start_date=list(set(start_date))
        # print(start_date)
        start_date=tracslateDate(start_date)
        # print(start_date)
        start_date=','.join(start_date)
        item['start_date'] = start_date

        deadline=response.xpath('//span[contains(text(),"deadline")]/../text()').extract()
        deadline=list(set(deadline))
        # print(deadline)
        deadline=tracslateDate(deadline)
        # print(deadline)
        deadline=''.join(deadline)
        item['deadline']=deadline

        ielts=response.xpath('//*[contains(text(),"IELTS")]/text()').extract()
        item['ielts_desc']=''.join(ielts).strip()
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
        if ielts==[]:
            ielts=response.xpath('//*[contains(text(),"English Language requirements")]/../text()').extract()
            ielts=get_ielts(ielts)
            try:
                if ielts != [] or ielts != {}:
                    item['ielts_l'] = ielts['IELTS_L']
                    item['ielts_s'] = ielts['IELTS_S']
                    item['ielts_r'] = ielts['IELTS_R']
                    item['ielts_w'] = ielts['IELTS_W']
                    item['ielts'] = ielts['IELTS']
            except:
                pass
            # print(ielts)

        overview=response.xpath('//div[@id="tab-0"]//div[@class="rich-text"]|//h3[contains(text(),"Overview")]/following-sibling::p').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        modules=response.xpath('//div[@id="tab-1"]//div[@class="rich-text"]|//div[@id="modules"]').extract()
        modules=remove_class(modules)
        # print(modules)
        item['modules_en'] = modules

        rntry=response.xpath('//*[contains(text(),"English Language requirements")]/..').extract()
        rntry=remove_class(rntry)
        # print(rntry)
        item['rntry_requirements'] = rntry

        howtoapply=response.xpath('//div[@id="how-to-apply"]').extract()
        howtoapply=remove_class(howtoapply)
        item['apply_proces_en'] = howtoapply

        department=response.xpath('//strong[contains(text(),"Department")]/../text()').extract()
        department=''.join(department).strip()
        item['department'] = department

        fee=response.xpath('//*[contains(text(),"£")]//text()').extract()
        # print(fee)
        tuition_fee=getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = '£'

        career = response.xpath(
            '//h1[contains(text(),"career")]/../following-sibling::div|//div[@id="tab-5"]').extract()
        career = remove_class(career)
        # print(career)
        item['career_en'] = career

        # yield item
        # print(item)