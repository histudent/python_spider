# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.middlewares import clear_duration,tracslateDate
class UniversitycollegelondonPSpider(scrapy.Spider):
    # name = 'UniversityCollegeLondon_P'
    allowed_domains = ['ucl.ac.uk']
    start_urls = ['https://search2.ucl.ac.uk/s/search.html?query=&collection=website-meta&profile=_degrees&tab=degrees&f.Level%7CL=Graduate+Taught&f.Mode%7Cm=Full-Time+%28FT%29&start_rank=1']
    # count=1
    def parse(self, response):
        # print(response.url)
        programme=response.xpath('//h3[@class="result__title"]/following-sibling::a/@href').extract()
        # print(programme)
        pro_name=response.xpath('//h3/text()').extract()
        for i,n in zip(programme,pro_name):
            department_xpath = '//a[@href="' + i + '"]/following-sibling::table/tbody/tr/td[4]/text()'
            full_url='https://search2.ucl.ac.uk'+i
            print(full_url)
            print(n)
            # self.count += 1
            # print('传递了')
            department=response.xpath(department_xpath).extract()
            yield scrapy.Request(full_url,callback=self.parses,meta={'department':department})
        next_page=response.xpath('//a[contains(text(),"Next")]/@href').extract()
        if next_page!=[]:
            next_page_url='https://search2.ucl.ac.uk/s/'+''.join(next_page)
            yield scrapy.Request(next_page_url,callback=self.parse)
    def parses(self,response):
        print(response.url)
        # print('收到了')
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university'] = 'University College London'
        item['url'] = response.url
        item['tuition_fee_pre'] = '£'
        location=response.xpath('//div/strong[contains(text(),"Location")]/../text()').extract()
        location=''.join(location).strip()
        item['location'] = location
        programme=response.xpath('//h1[@class="heading"]//text()').extract()
        programme=''.join(programme)
        # print(programme)
        degree_name=re.findall('[MB][A-Z]{1,2}[a-z]*',programme)
        # print(degree_name)
        degree_name=''.join(set(degree_name)).strip()
        programme=programme.replace(degree_name,'')
        item['programme_en'] = programme
        item['degree_name']=degree_name
        item['degree_type']='2'
        # print(programme)
        mode=response.xpath('//*[contains(text(),"FT")]//text()').extract()
        if mode!=[]:
            item['teach_time'] = 1
        else:
            item['teach_time'] = 2
        # department=response.meta['department']
        # department=''.join(department).strip()
        # # print(department)
        # item['department'] = department
        department = response.xpath(
            '//h5[contains(text(),"Department website")]/following-sibling::p/a/text()').extract()
        department = ''.join(department).strip()
        # # print(department)
        item['department'] = department

        overview=response.xpath('//article[@class="article"]/h1/following-sibling::article/p[1]').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        application_open_date=response.xpath('//div[contains(text(),"Open")]/text()').extract()
        application_open_date=tracslateDate(application_open_date)
        # print(application_open_date)
        application_open_date=','.join(set(application_open_date))
        item['application_open_date'] = application_open_date

        deadline=response.xpath('//div[contains(text(),"Close")]/text()').extract()
        deadline=tracslateDate(deadline)
        deadline=','.join(set(deadline))
        item['deadline'] = deadline

        tuition_fee=getTuition_fee(response.xpath('//*[contains(text(),"£")]//text()').extract())
        item['tuition_fee'] = tuition_fee

        duration=response.xpath('//h4[contains(text(),"uration")]/following-sibling::div/text()').extract()
        duration=clear_duration(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']

        start_date=response.xpath('//h4[contains(text(),"tarts")]/following-sibling::p//text()').extract()
        # print(start_date)
        start_date=tracslateDate(start_date)
        # print(start_date)
        start_date=','.join(set(start_date))
        # print(start_date)
        item['start_date'] = start_date

        item['apply_fee'] ='75'
        item['apply_pre'] ='£'

        eng_level=response.xpath('//p[contains(text(),"English language")]/strong/text()').extract()
        eng_level=''.join(eng_level).strip()
        if eng_level=='Standard':
            ielts='Overall grade of 6.5 with a minimum of 6.0 in each of the subtests.'
            toefl='Overall score of 92 with 24/30 in reading and writing and 20/30 in speaking and listening.'
        elif eng_level=='Good':
            ielts='Overall grade of 7.0 with a minimum of 6.5 in each of the subtests.'
            toefl='Overall score of 100 with 24/30 in reading and writing and 20/30 in speaking and listening.'
        elif eng_level=='Advanced':
            ielts='Overall grade of 7.5 with a minimum of 6.5 in each of the subtests.'
            toefl='Overall score of 109 with 24/30 in reading and writing and 20/30 in speaking and listening.'
        else:
            ielts=''
            toefl=''
        ieltss=get_ielts(ielts)
        # print(ieltss)
        if ieltss != {} and ieltss != []:
            # ieltss=list(map(float,ieltss))
            item['ielts_l'] = ieltss['IELTS_L']
            item['ielts_s'] = ieltss['IELTS_S']
            item['ielts_r'] = ieltss['IELTS_R']
            item['ielts_w'] = ieltss['IELTS_W']
            item['ielts'] = ieltss['IELTS']
        toefls=re.findall('\d{1,3}',''.join(toefl))
        # print(toefls)
        if len(toefls)==5:
            item['toefl'] = toefls[0]
            item['toefl_l']=toefls[4]
            item['toefl_w'] = toefls[2]
            item['toefl_r'] = toefls[1]
            item['toefl_s'] = toefls[3]
        elif len(toefls)==2:
            toefls=list(map(int,toefls))
            item['toefl'] = max(toefls)
            item['toefl_l'] = min(toefls)
            item['toefl_w'] = min(toefls)
            item['toefl_r'] = min(toefls)
            item['toefl_s'] = min(toefls)
        item['ielts_desc'] = ielts
        item['toefl_desc'] = toefl
        # print(item)

        rntry_requirements=response.xpath('//h4[contains(text(),"ntry")]/following-sibling::p[1]').extract()
        rntry_requirements=remove_class(rntry_requirements)
        # print(rntry_requirements)
        item['rntry_requirements'] = rntry_requirements

        chinese_reuqirement=["<div>Equivalent qualifications for China",
"Bachelor's degree with a minimum overall average mark of 80%. Please note that a number of programmes / departments will require higher marks.",
"ALTERNATIVE QUALIFICATIONS",
"Medical/ Dental/ Master's degree; Doctorate.</div>",]
        chinese_reuqirement='\n'.join(chinese_reuqirement)
        item['require_chinese_en'] = chinese_reuqirement

        modules=response.xpath('//h2[contains(text(),"About this")]/following-sibling::div').extract()
        modules=remove_class(modules)
        # print(modules)
        item['modules_en'] = modules

        career=response.xpath('//h2[contains(text(),"Career")]/following-sibling::div').extract()
        career=remove_class(career)
        item['career_en'] = career

        yield item
        # print(item)


