# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
from scrapySchool_England_U.middlewares import *

class MiddlesexuniversityUSpider(scrapy.Spider):
    name = 'MiddlesexUniversity_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.mdx.ac.uk/_resources/funnelback/outputs/london-course-finder?collection=mdx-courses&f.Course_level%7CI=Undergraduate&start_rank=1']
    start_rank=1
    def parse(self, response):
        url=['https://www.mdx.ac.uk/courses/undergraduate/business-management-project-management',
'https://www.mdx.ac.uk/courses/undergraduate/graphic-design',
'https://www.mdx.ac.uk/courses/undergraduate/criminology-policing',
'https://www.mdx.ac.uk/courses/undergraduate/business-accounting',
'https://www.mdx.ac.uk/courses/undergraduate/dance-performance',
'https://www.mdx.ac.uk/courses/undergraduate/international-tourism-management-mandarin',
'https://www.mdx.ac.uk/courses/undergraduate/banking-and-finance',
'https://www.mdx.ac.uk/courses/undergraduate/medical-biochemistry',
'https://www.mdx.ac.uk/courses/undergraduate/international-business',
'https://www.mdx.ac.uk/courses/undergraduate/biomedical-engineering',
'https://www.mdx.ac.uk/courses/undergraduate/international-tourism-management-and-spanish',
'https://www.mdx.ac.uk/courses/undergraduate/international-politics-economics-and-law',
'https://www.mdx.ac.uk/courses/undergraduate/nursing-degree-child-field',
'https://www.mdx.ac.uk/courses/undergraduate/business-management-finance',
'https://www.mdx.ac.uk/courses/undergraduate/environmental-health-degree',
'https://www.mdx.ac.uk/courses/undergraduate/human-resource-management',
'https://www.mdx.ac.uk/courses/undergraduate/design-engineering-robotics',
'https://www.mdx.ac.uk/courses/undergraduate/advertising-public-relations-and-branding',
'https://www.mdx.ac.uk/courses/undergraduate/sport-and-exercise-science-strength-and-conditioning-degree',
'https://www.mdx.ac.uk/courses/undergraduate/sport-and-exercise-rehabilitation-degree',
'https://www.mdx.ac.uk/courses/undergraduate/llb-law-with-human-rights',
'https://www.mdx.ac.uk/courses/undergraduate/international-tourism-management',
'https://www.mdx.ac.uk/courses/undergraduate/business-management-marketing',
'https://www.mdx.ac.uk/courses/undergraduate/journalism-and-communication',
'https://www.mdx.ac.uk/courses/undergraduate/professional-aviation-tayside',
'https://www.mdx.ac.uk/courses/undergraduate/criminology-with-psychology-degree',
'https://www.mdx.ac.uk/courses/undergraduate/business-management-innovation',
'https://www.mdx.ac.uk/courses/undergraduate/architectural-technology',
'https://www.mdx.ac.uk/courses/undergraduate/accounting-and-finance',
'https://www.mdx.ac.uk/courses/undergraduate/veterinary-nursing-degree',
'https://www.mdx.ac.uk/courses/undergraduate/veterinary-nursing-degree',
'https://www.mdx.ac.uk/courses/undergraduate/veterinary-nursing-degree',
'https://www.mdx.ac.uk/courses/undergraduate/biomedical-engineering',
'https://www.mdx.ac.uk/courses/undergraduate/law-degree',
'https://www.mdx.ac.uk/courses/undergraduate/neuroscience',
'https://www.mdx.ac.uk/courses/undergraduate/biochemistry',
'https://www.mdx.ac.uk/courses/undergraduate/english',
'https://www.mdx.ac.uk/courses/undergraduate/marketing',
'https://www.mdx.ac.uk/courses/undergraduate/mathematics',
'https://www.mdx.ac.uk/courses/undergraduate/music',
'https://www.mdx.ac.uk/courses/undergraduate/sport-and-exercise-science-degree',
'https://www.mdx.ac.uk/courses/undergraduate/business-management-supply-chain',
'https://www.mdx.ac.uk/courses/undergraduate/nursing-degree-mental-health-field',
'https://www.mdx.ac.uk/courses/undergraduate/llb-law-with-international-relations',
'https://www.mdx.ac.uk/courses/undergraduate/computer-forensics',
'https://www.mdx.ac.uk/courses/undergraduate/sport-and-exercise-science-physical-education-coaching',
'https://www.mdx.ac.uk/courses/undergraduate/public-health-bsc',
'https://www.mdx.ac.uk/courses/undergraduate/professional-aviation-pilot-practice-programme-helicopter',
'https://www.mdx.ac.uk/courses/undergraduate/design-engineering',
'https://www.mdx.ac.uk/courses/undergraduate/illustration-degree',
'https://www.mdx.ac.uk/courses/undergraduate/criminology',
'https://www.mdx.ac.uk/courses/undergraduate/fashion-textiles',
'https://www.mdx.ac.uk/courses/undergraduate/games-design',
'https://www.mdx.ac.uk/courses/undergraduate/computer-networks',
'https://www.mdx.ac.uk/courses/undergraduate/computer-communication-and-networks',
'https://www.mdx.ac.uk/courses/undergraduate/interior-design',
'https://www.mdx.ac.uk/courses/undergraduate/computer-systems-engineering',
'https://www.mdx.ac.uk/courses/undergraduate/psychology-degree',
'https://www.mdx.ac.uk/courses/undergraduate/design-engineering',
'https://www.mdx.ac.uk/courses/undergraduate/visual-effects',
'https://www.mdx.ac.uk/courses/undergraduate/product-design-engineering',
'https://www.mdx.ac.uk/courses/undergraduate/midwifery-degree',
'https://www.mdx.ac.uk/courses/undergraduate/design-engineering-electronic-engineering',
'https://www.mdx.ac.uk/courses/undergraduate/theatre-arts',
'https://www.mdx.ac.uk/courses/undergraduate/mathematics-with-computing-bscmsci',
'https://www.mdx.ac.uk/courses/undergraduate/social-work',
'https://www.mdx.ac.uk/courses/undergraduate/design-engineering-mechatronics',
'https://www.mdx.ac.uk/courses/undergraduate/popular-music',
'https://www.mdx.ac.uk/courses/undergraduate/medical-biochemistry',
'https://www.mdx.ac.uk/courses/undergraduate/economics-bsc',
'https://www.mdx.ac.uk/courses/undergraduate/pharmaceutical-chemistry',
'https://www.mdx.ac.uk/courses/undergraduate/digital-media',
'https://www.mdx.ac.uk/courses/undergraduate/design-engineering-robotics',
'https://www.mdx.ac.uk/courses/undergraduate/dance-studies',
'https://www.mdx.ac.uk/courses/undergraduate/ba-economics',
'https://www.mdx.ac.uk/courses/undergraduate/fine-art',
'https://www.mdx.ac.uk/courses/undergraduate/llb-with-commercial-law',
'https://www.mdx.ac.uk/courses/undergraduate/pharmaceutical-chemistry',
'https://www.mdx.ac.uk/courses/undergraduate/sociology-psychology',
'https://www.mdx.ac.uk/courses/undergraduate/international-politics',
'https://www.mdx.ac.uk/courses/undergraduate/information-technology',
'https://www.mdx.ac.uk/courses/undergraduate/biology-biotechnology',
'https://www.mdx.ac.uk/courses/undergraduate/television-production',
'https://www.mdx.ac.uk/courses/undergraduate/interior-architecture',
'https://www.mdx.ac.uk/courses/undergraduate/business-management',
'https://www.mdx.ac.uk/courses/undergraduate/llb',
'https://www.mdx.ac.uk/courses/undergraduate/business-management-spanish',
'https://www.mdx.ac.uk/courses/undergraduate/nursing-degree-adult-field',
'https://www.mdx.ac.uk/courses/undergraduate/product-design-engineering',
'https://www.mdx.ac.uk/courses/undergraduate/design-engineering-mechatronics',
'https://www.mdx.ac.uk/courses/undergraduate/biology-molecular-biology',
'https://www.mdx.ac.uk/courses/undergraduate/criminology-youth-justice',
'https://www.mdx.ac.uk/courses/undergraduate/llb-law-with-criminology',
'https://www.mdx.ac.uk/courses/undergraduate/education-studies-degree',
'https://www.mdx.ac.uk/courses/undergraduate/jazz',
'https://www.mdx.ac.uk/courses/undergraduate/biology-environmental-biology',
'https://www.mdx.ac.uk/courses/undergraduate/sociology-criminology-degree',
'https://www.mdx.ac.uk/courses/undergraduate/business-information-systems',
'https://www.mdx.ac.uk/courses/undergraduate/business-management-mandarin',
'https://www.mdx.ac.uk/courses/undergraduate/computer-systems-engineering',
'https://www.mdx.ac.uk/courses/undergraduate/criminology-criminal-justice',
'https://www.mdx.ac.uk/courses/undergraduate/3d-animation-and-games',
'https://www.mdx.ac.uk/courses/undergraduate/animation',
'https://www.mdx.ac.uk/courses/undergraduate/psychology-with-neuroscience',
'https://www.mdx.ac.uk/courses/undergraduate/psychology-with-education-degree',
'https://www.mdx.ac.uk/courses/undergraduate/medical-physiology-neuroscience',
'https://www.mdx.ac.uk/courses/undergraduate/european-nursing-degree-adult',
'https://www.mdx.ac.uk/courses/undergraduate/nutrition',
'https://www.mdx.ac.uk/courses/undergraduate/early-childhood-studies-degree',
'https://www.mdx.ac.uk/courses/undergraduate/media-and-cultural-studies',
'https://www.mdx.ac.uk/courses/undergraduate/photography',
'https://www.mdx.ac.uk/courses/undergraduate/creative-writing-and-journalism',
'https://www.mdx.ac.uk/courses/undergraduate/publishing-and-digital-culture',
'https://www.mdx.ac.uk/courses/undergraduate/mathematics-with-computing-bscmsci',
'https://www.mdx.ac.uk/courses/undergraduate/psychology-with-criminology-degree',
'https://www.mdx.ac.uk/courses/undergraduate/international-politics-and-law',
'https://www.mdx.ac.uk/courses/undergraduate/business-management-fast-track',
'https://www.mdx.ac.uk/courses/undergraduate/sociology',
'https://www.mdx.ac.uk/courses/undergraduate/biology',
'https://www.mdx.ac.uk/courses/undergraduate/film',
'https://www.mdx.ac.uk/courses/undergraduate/medical-physiology-cardiovascular-science',
'https://www.mdx.ac.uk/courses/undergraduate/fashion-communication-and-styling',
'https://www.mdx.ac.uk/courses/undergraduate/llb-with-european-law-and-politics',
'https://www.mdx.ac.uk/courses/undergraduate/design-engineering-electronic-engineering',
'https://www.mdx.ac.uk/courses/undergraduate/computer-communication-and-networks',
'https://www.mdx.ac.uk/courses/undergraduate/ba-hons-sociology-and-social-policy',
'https://www.mdx.ac.uk/courses/undergraduate/professional-aviation-pilot-practice-programme',
'https://www.mdx.ac.uk/courses/undergraduate/primary-education-with-qts-degree',
'https://www.mdx.ac.uk/courses/undergraduate/psychology-with-counselling-skills',
'https://www.mdx.ac.uk/courses/undergraduate/computer-science',
'https://www.mdx.ac.uk/courses/undergraduate/fashion-design',
'https://www.mdx.ac.uk/courses/undergraduate/product-design',
'https://www.mdx.ac.uk/courses/undergraduate/music-business-and-arts-management',
'https://www.mdx.ac.uk/courses/undergraduate/business-management-human-resources',
'https://www.mdx.ac.uk/courses/undergraduate/biomedical-science',]
        url=set(url)
        for u in url:
            yield scrapy.Request(url=u,callback=self.parsesss,meta={'url':u})
    def parsesss(self,response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.meta['url']
        item['university']='Middlesex University'
        print(response.url)
        alevel=response.xpath('//strong[contains(text(),"UCAS points")]/text()').extract()
        print(alevel)
        if len(alevel)>1:
            item['alevel']=alevel[0]
        yield item

    def parsess(self, response):
        # print(response.url)
        pro_url = response.xpath('//ul[@class="search-results"]/li/h3/a/@href').extract()
        last_page = response.xpath('//a[contains(text(),"Last")]/@href').extract()
        # print(pro_url)
        for i in pro_url:
            yield scrapy.Request(url=i, callback=self.parse_main)
        # print(last_page)
        num_rank = re.findall('start_rank=\d+', ''.join(last_page))
        num_rank = ''.join(num_rank).replace('start_rank=', '')
        try:
            num_rank = int(num_rank)
        except:
            num_rank = self.start_rank
        # print(num_rank)
        while self.start_rank < num_rank:
            self.start_rank = self.start_rank + 10
            next_page = 'https://www.mdx.ac.uk/_resources/funnelback/outputs/london-course-finder?collection=mdx-courses&f.Course_level%7CI=Undergraduate&start_rank=' + str(
                self.start_rank)
            yield scrapy.Request(next_page, callback=self.parses)
    def parses(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'Middlesex University'
        item['url'] = response.url
        item['location'] = 'London'
        programme = response.xpath('//div[@class="course-page-banner__texts"]/h1/text()').extract()
        # print(programme)
        programme = ''.join(programme)
        degree_name = re.findall('[A-Z]{2,}.*', programme)
        # print(degree_name)
        degree_name = ''.join(degree_name)
        if degree_name != programme:
            programme = programme.replace(degree_name, '')
        # print(programme)
        # print(degree_name)
        item['programme_en'] = programme
        item['degree_name'] = degree_name

        start_date = response.xpath('//span[contains(text(),"Start")]/../following-sibling::div//text()').extract()
        # print(start_date)
        start_date = tracslateDate(start_date)
        # print(start_date)
        start_date = ','.join(start_date)
        item['start_date'] = start_date

        ucascode=response.xpath('//span[contains(text(),"Code")]/../following-sibling::div//text()').extract()
        ucascode=','.join(ucascode)
        # print(ucascode)
        item['ucascode']=ucascode

        duration = response.xpath('//span[contains(text(),"Duration")]/../following-sibling::div//text()').extract()
        # mode = re.findall('(?i)full', ''.join(duration))
        duration = clear_duration(duration)
        # print(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']
        # if mode != []:
        #     item['teach_time'] = '1'
        # else:
        #     item['teach_time'] = '2'

        fee = response.xpath('//span[contains(text(),"Fees")]/../following-sibling::div//text()').extract()
        tuition_fee = getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = '£'

        overview = response.xpath('//h2[contains(text(),"Overview")]/following-sibling::*').extract()
        overview = remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        modules = response.xpath('//h2[contains(text(),"Course content")]/following-sibling::*').extract()
        modules = remove_class(modules)
        # print(modules)
        item['modules_en'] = modules

        # rntry = response.xpath('//h2[contains(text(),"Entry requirements")]/following-sibling::*').extract()
        # rntry = remove_class(rntry)
        # print(rntry)
        rntry='<p>For entry to most of our undergraduate courses, we require successful completion of College Entrance Examination with 60% or China High School Graduation Certificate with a minimum average of 75.</p>'
        item['require_chinese_en'] = rntry

        ielts = response.xpath('//p[contains(text(),"IELTS")]//text()').extract()
        ielts = ''.join(ielts)
        item['ielts_desc'] = ielts
        ielts = get_ielts(ielts)
        # print(ielts)
        try:
            if ielts != [] or ielts != {}:
                item['ielts_l'] = ielts['IELTS_L']
                item['ielts_s'] = ielts['IELTS_S']
                item['ielts_r'] = ielts['IELTS_R']
                item['ielts_w'] = ielts['IELTS_W']
                item['ielts'] = ielts['IELTS']
        except:
            pass

        career = response.xpath('//h2[contains(text(),"Careers")]/following-sibling::*').extract()
        career = remove_class(career)
        # print(career)
        item['career_en'] = career

        alevel=response.xpath('//h2[contains(text(),"Entry requirements")]/following-sibling::div[1]/ul/li[1]/div[1]').extract()
        # print(assessment)
        item['alevel']=remove_class(alevel)
        assessment=response.xpath('//h2[contains(text(),"Teaching ")]/following-sibling::div[1]/ul/li[1]/div[1]').extract()
        item['assessment_en']=remove_class(assessment)
        # print(assessment)
        yield item
        # print(item)