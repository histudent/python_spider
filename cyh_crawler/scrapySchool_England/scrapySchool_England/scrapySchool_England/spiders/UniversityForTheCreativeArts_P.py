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

class UniversityforthecreativeartsPSpider(scrapy.Spider):
    name = 'UniversityForTheCreativeArts_P'
    allowed_domains = ['uca.ac.uk']
    # start_urls = ['https://www.uca.ac.uk/study/courses/?subject=&campus=&studyLevel=postgraduate']
    # def parse(self, response):
    #     pro_url=response.xpath('//span[@class="level f-l1" and contains(text(),"M")]/../../@href').extract()
    #     # print(len(pro_url))
    #     for i in pro_url:
    #         full_url='https://www.uca.ac.uk'+i
    #         yield scrapy.Request(url=full_url,callback=self.parse_main)
    start_urls=['https://www.uca.ac.uk/study/courses/ma-animation/',
'https://www.uca.ac.uk/study/courses/ma-photography/',
'https://www.uca.ac.uk/study/courses/ma-media-communication/',
'https://www.uca.ac.uk/study/courses/ma-luxury-brand-management/',
'https://www.uca.ac.uk/study/courses/ma-urban-design/',
'https://www.uca.ac.uk/study/courses/ma-printed-textiles/',
'https://www.uca.ac.uk/study/courses/ma-product-design/',
'https://www.uca.ac.uk/study/courses/ma-jewellery/',
'https://www.uca.ac.uk/study/courses/msc-international-financial-management/',
'https://www.uca.ac.uk/study/courses/ma-international-jewellery-management/',
'https://www.uca.ac.uk/study/courses/mba-international/',
'https://www.uca.ac.uk/study/courses/ma-interior-design/',
'https://www.uca.ac.uk/study/courses/ma-illustration/',
'https://www.uca.ac.uk/study/courses/ma-graphic-design/',
'https://www.uca.ac.uk/study/courses/ma-global-media-management/',
'https://www.uca.ac.uk/study/courses/ma-glass/',
'https://www.uca.ac.uk/study/courses/ma-games-design/',
'https://www.uca.ac.uk/study/courses/ma-fine-art-farnham/',
'https://www.uca.ac.uk/study/courses/ma-fine-art-canterbury/',
'https://www.uca.ac.uk/study/courses/ma-filmmaking-documentary/',
'https://www.uca.ac.uk/study/courses/mfa-photography/',
'https://www.uca.ac.uk/study/courses/ma-textiles/',
'https://www.uca.ac.uk/study/courses/ma-visual-communication/',
'https://www.uca.ac.uk/study/courses/ma-fashion-business-management/',
'https://www.uca.ac.uk/study/courses/ma-filmmaking/',
'https://www.uca.ac.uk/study/courses/ma-digital-media/',
'https://www.uca.ac.uk/study/courses/ma-fashion-photography/',
'https://www.uca.ac.uk/study/courses/ma-fashion-design/',
'https://www.uca.ac.uk/study/courses/ma-fashion-marketing-communication/',
'https://www.uca.ac.uk/study/courses/ma-design-innovation-brand-management/',
'https://www.uca.ac.uk/study/courses/ma-curatorial-practice/',
'https://www.uca.ac.uk/study/courses/ma-creative-business-management/',
'https://www.uca.ac.uk/study/courses/ma-architecture/',
'https://www.uca.ac.uk/study/courses/master-of-architecture/',
'https://www.uca.ac.uk/study/courses/ma-creative-marketing-advertising/',
'https://www.uca.ac.uk/study/courses/ma-ceramics/',

]
    def parse(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)

        item['university']='University for the Creative Arts'
        item['url']=response.url

        programme=response.xpath('//h1/text()').extract()
        programme=''.join(programme)
        # print(programme)
        item['programme_en']=programme

        degr=response.xpath('//h1/following-sibling::p[1]/text()').extract()
        # print(degr)
        degr=''.join(degr).split('-')
        if len(degr)==3:
            # print(degr)
            degree_name=degr[0]
            location=degr[1]
            item['degree_name']=degree_name
            try:
                if degree_name[0] == 'M':
                    item['degree_type'] = '2'
                elif degree_name[0] == 'P':
                    item['degree_type'] = '3'
            except:
                pass
        elif len(degr)==4:
            # print(degr)
            item['degree_name']='Pre-degree'
            item['degree_type']='2'

        duration=response.xpath('//p[contains(text(),"Length of study")]/following-sibling::p/text()').extract()
        duration=clear_duration(duration)
        # print(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']

        location=response.xpath('//p[contains(text(),"Campus")]/following-sibling::p/text()').extract()
        location=''.join(location)
        item['location']=location

        start_date=response.xpath('//p[contains(text(),"Start month")]/following-sibling::p/text()').extract()
        start_date=tracslateDate(start_date)
        # print(start_date)
        start_date=','.join(start_date)
        item['start_date']=start_date

        overview=response.xpath('//div[@class="cell overview"]').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en']=overview

        modules=response.xpath('//div[@id="syllabus"]/following-sibling::section[@class="article-content-area"][1]').extract()
        modules=remove_class(modules)
        # print(modules)
        item['modules_en']=modules

        career=response.xpath('//div[contains(text(),"Career")]/following-sibling::div').extract()
        career=remove_class(career)
        # print(career)
        item['career_en']=career

        item['ielts'] = '6'
        item['ielts_l'] = '5.5'
        item['ielts_s'] = '5.5'
        item['ielts_r'] = '5.5'
        item['ielts_w'] = '5.5'

        rntry=["We will consider equivalent qualifications from your home country for entry onto our Foundation, Bachelor’s and Master’s courses. Please see below for details of the accepted qualifications (including English language qualifications) for each level of course. Each application we receive is considered individually and therefore these qualifications are provided as a guide.",
"For our International Foundation in Art, Design and Media, we usually require that you have one of the following:",
"Chinese Senior School graduation with 12 years of completed school study, with an average of 65% or above.",
"Pre Foundation course at Guildford College Training School (China).",
"For our Bachelor's courses, we usually require that you have:",
"Chinese Senior School graduation with 12 years of completed school study, plus a recognised Foundation course.",
"A transcript showing successful completion of one year of university study at a recognised Chinese university with average of 70%.",
"For our Master's courses, we usually require that you have:",
"Bachelor's degree with 80% average grade from a recognised Chinese university.",]
        rntry='\n'.join(rntry)
        rntry=response.xpath('//h3[contains(text(),"UK entry requirements")]/following-sibling::*').extract()
        item['rntry_requirements']=remove_class(rntry)
        portfolio=response.xpath('//h3[contains(text(),"Your portfolio")]/following-sibling::*').extract()
        item['portfolio_desc_en']=remove_class(portfolio)

        item['tuition_fee']='13540'
        item['tuition_fee_pre']='£'

        item['deadline']='2019-3'



        # print(item)
        yield item