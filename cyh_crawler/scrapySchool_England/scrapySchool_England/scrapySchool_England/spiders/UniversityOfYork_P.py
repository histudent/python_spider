# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.middlewares import clear_duration,tracslateDate

class TheuniversityofyorkPSpider(scrapy.Spider):
    name = 'UniversityOfYork_P'
    # allowed_domains = ['york.ac.uk']
    # start_urls = ['https://www.york.ac.uk/study/postgraduate/courses/all?mode=taught&q=&level=postgraduate']
    # def parse(self, response):
        # programme=response.xpath('//td[@class="coursetitle"]/a[1]//text()').extract()
        # pro_url=response.xpath('//td[@class="coursetitle"]/a[1]//@href').extract()
        # yaobuyao=response.xpath('//td[contains(@class,"code")]/*/text()').extract()
        # deg_xpaths='//a[contains(@href,"%s")]/../following-sibling::td[@class="detail"]/ul/li/abbr/text()'
        # dur_xpaths='//a[contains(@href,"%s")]/../following-sibling::td[@class="detail"]/ul/li/text()'
        # for pro,url,yao in zip(programme,pro_url,yaobuyao):
        #     pro=pro.strip()
            # deg_xpath=deg_xpaths % url
            # dur_xpath=dur_xpaths % url
            # degree_name=response.xpath(deg_xpath).extract()
            # duration=response.xpath(dur_xpath).extract()
            # mode=re.findall('(?i)full',''.join(duration))
            # if 'P' not in ''.join(degree_name):
            # if mode!=[]:
    #             yield scrapy.Request(url=url,callback=self.translates,meta={'programme': pro, 'duration': ''.join(set(duration)),
    #         #                        'degree': ''.join(degree_name)})
    start_urls=['https://www.york.ac.uk/study/postgraduate-taught/courses/ma-film-television-production-producing/']
    def parse(self,response):
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        university = 'University of York'
        item['university'] = university
        item['url'] = response.url
        item['location'] = 'York'
        item['tuition_fee_pre'] = '£'
        start_date=response.xpath('//h4[contains(text(),"Start date")]/following-sibling::p//text()').extract()
        start_date = tracslateDate(start_date)
        start_date = ','.join(start_date)
        item['start_date'] = start_date
        overview = response.xpath('//div[@class="o-grid__box o-grid__box--half o-grid__box--half@medium"]|'
                                  '//h2[contains(text(),"verview")]/following-sibling::*|'
                                  '//h2[contains(text(),"At a glance")]/following-sibling::*|'
                                  '//h2[contains(text(),"Course summary")]/following-sibling::*|'
                                  '//h2[contains(text(),"At a Glance")]/following-sibling::*|'
                                  '//div[@id="mdcolumn"]/h1/following-sibling::*[position()<5]').extract()
        overview = remove_class(overview)
        item['overview_en'] = overview
        # print(overview)
        modules = response.xpath('//div[@id="content_modules"]|'
                                 '//h2[contains(text(),"Course structure")]/following-sibling::*|'
                                 '//th[contains(text(),"Module")]/../../..|'
                                 '//h2[contains(text(),"ontent")]/following-sibling::*|'
                                 '//h3[contains(text(),"What does the course cover?")]/following-sibling::p[1]|'
                                 '//strong[contains(text(),"Course structure")]/../following-sibling::*[position()<=5]|'
                                 '//h2[contains(text(),"Structure and ethos")]/..|'
                                 '//h2[contains(text(),"Modules")]/following-sibling::*|'
                                 '//h2[contains(text(),"Structure and Ethos")]/following-sibling::*|'
                                 '//h2[contains(text(),"module")]/following-sibling::*').extract()
        modules = remove_class(modules)
        item['modules_en'] = modules
        # print(modules)
        tuition_fee = response.xpath('//div[@id="fees"]/following-sibling::div[1]//*[contains(text(),"£")]//text()').extract()
        tuition_fee = getTuition_fee(tuition_fee)
        item['tuition_fee'] = tuition_fee
        # print(tuition_fee)
        assessment = response.xpath('//h2[contains(text(),"Teaching and assessment")]/../../following-sibling::div[1]'
                                    '|//h2[contains(text(),"ssessment")]/following-sibling::*|'
                                    '//h2[contains(text(),"ssessment")]/following-sibling::*[position()<=5]|'
                                    '//strong[contains(text(),"Specialist training tailored to your interests and aspirations")]/../following-sibling::*|'
                                    '//span[contains(text(),"ssessment")]/../following-sibling::*[position()<=3]|'
                                    '//h3[contains(text(),"ssessment")]/following-sibling::*[position()<=3]|'
                                    '//strong[contains(text(),"SUMMER TERM")]/../following-sibling::*|'
                                    '//strong[contains(text(),"ssessment")]/../following-sibling::*[position()<=3]|'
                                    '//h2[contains(text(),"Teaching")]/following-sibling::*|'
                                    '//blockquote[@class="rightBox"]/following-sibling::*[1]|'
                                    '//h2[contains(text(),"Dissertation")]/following-sibling::p[1]|'
                                    '//p[contains(text(),"This programme aims: ")]/following-sibling::table[1]').extract()
        # if assessment==[]:
        #     print(response.url)
        assessment = remove_class(assessment)
        item['assessment_en'] = assessment
        # print(assessment)

        entry_requirements = response.xpath('//div[@id="entry"]|'
                                            '//h2[contains(text(),"requirement")]/following-sibling::*|'
                                            '//h2[contains(text(),"pplicants")]/following-sibling::*|'
                                            '//h3[contains(text(),"Entry Requirements")]/following-sibling::*|'
                                            '//h2[contains(text(),"Entry")]/following-sibling::*[position()>1]|'
                                            '//h3[contains(text(),"International students")]/following-sibling::*|'
                                            '//h3[contains(text(),"Entry requirements")]/following-sibling::*[position()<4]|'
                                            '//h2[contains(text(),"English Language Requirements")]/following-sibling::*[position()<3]').extract()
        # if entry_requirements==[]:
        #     print(response.url)
        entry_requirements = remove_class(entry_requirements)
        item['rntry_requirements'] = entry_requirements
        # print(entry_requirements)

        ielts=response.xpath('//*[contains(text(),"IELTS")]//text()').extract()
        ielts = get_ielts(ielts)
        if ielts != {} and ielts != []:
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            item['ielts'] = ielts['IELTS']
        toefl=response.xpath('//*[contains(text(),"TOEFL")]//text()').extract()
        toefl=''.join(toefl).strip()
        item['toefl_desc']=toefl
        toefl = re.findall('\d{2,3}', toefl)
        if len(toefl) == 2:
            toefl = list(map(int, toefl))
            item['toefl'] = max(toefl)
            item['toefl_l'] = min(toefl)
            item['toefl_w'] = min(toefl)
            item['toefl_r'] = min(toefl)
            item['toefl_s'] = min(toefl)

        career = response.xpath('//div[@class="o-grid__box o-grid__box--half"]|'
                                '//h2[contains(text(),"areer")]/following-sibling::*|'
                                '//h2[contains(text(),"Employment relevance")]/following-sibling::*|'
                                '//p[contains(text(),"employment,")]/following-sibling::ul[1]|'
                                '//p[contains(text(),"This programme aims: ")]/following-sibling::ul[1]|'
                                '//h3[contains(text(),"areers")]/following-sibling::ul[1]|'
                                '//h2[contains(text(),"Employment outcomes")]/following-sibling::*|'
                                '//h3[contains(text(),"What can it lead to?")]/following-sibling::p[1]').extract()
        # if career==[]:
        #     print(response.url)
        career = remove_class(career)
        # print(career)
        item['career_en'] = career
        departnemt=response.xpath('//h4[contains(text(),"Department")]/following-sibling::p//text()|//div[@id="location"]/h1//text()').extract()
        departnemt=''.join(departnemt)
        item['department']=departnemt
        # pro = response.meta['programme']
        # item['programme_en'] = pro
        # duration = response.meta['duration']
        # print(duration)
        # duration = clear_duration(duration)
        # item['duration'] = duration['duration']
        # item['duration_per'] = duration['duration_per']
        programme=response.xpath('//div[@id="mdcolumn"]/h1/text()|//div[@class="c-figure__content c-figure__content--left c-figure__content--half"]/h1/text()').extract()
        # print(programme)
        clears=re.findall('[A-Za-z]+ in ',''.join(programme))
        programme=''.join(programme).replace(''.join(clears),'').strip()
        item['programme_en']=programme
        duration=response.xpath('//h4[contains(text(),"Length")]/following-sibling::p//text()').extract()
        # print(duration)
        duration = clear_duration(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']

        major_type1 = response.xpath(
            '//div[@class="c-figure__content c-figure__content--left c-figure__content--half"]/h1/text()|//div[@id="content-container"]//h1/text()').extract()
        major_type1 = ''.join(major_type1)
        item['major_type1']=major_type1
        # if 'diploma' not in response.url:
            # print(response.url)
            # print(major_type1)
        degree_name=re.findall('[A-Z]{2}[a-zA-Z]*',major_type1)
        # print(degree_name)
        degree_name='/'.join(degree_name).strip()
        item['degree_name']=degree_name
        # print(item)
        # yield item










