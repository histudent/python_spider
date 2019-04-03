# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem

class UniversityofbedfordshireUSpider(scrapy.Spider):
    name = 'UniversityofBedfordshire_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.beds.ac.uk/howtoapply/courses/undergraduate']
    def parse(self, response):
        url=['https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/policing-and-criminal-investigation2?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/physiotherapy?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/physical-education-secondary-with-qts?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/photography-and-video-art?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/photographic-practices?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/pharmacology-and-health-science?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/pharmaceutical-and-chemical-sciences?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/performing-arts?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/paramedic-science?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/operating-department-practice2?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/occupational-therapy?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/nursing-with-registered-nurse-mental-health?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/nursing-with-registered-nurse-adult?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/child-nursing-pre-reg-practice?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/music-technology?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/midwifery-registered-midwife?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/midwifery-registered-midwife-2nd-registration2?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/media,-marketing-and-public-relations?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/media-production-radio?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/media-production?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/media-performance-for-film,-tv-and-theatre?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/media-communication?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/mechanical-engineering-with-foundation-year?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/mechanical-engineering?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/marketing-with-tourism-management?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/marketing-with-aviation-and-airport-management?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/marketing-with-events-management?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/marketing0?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/marketing?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/law-with-psychology?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/law-with-criminology?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/law?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/law2?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/journalism,-marketing-and-public-relations?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/journalism-and-public-relations?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/journalism-with-placement?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/journalism?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/sport-and-physical-education?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/international-tourism-with-hospitality-management?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/international-tourism-with-events-management?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/international-tourism-management?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/international-finance-and-banking?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/international-business-with-marketing?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/international-business?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/interior-design-and-retail-branding?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/interior-architecture?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/interactive-digital-technologies?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/information-technology?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/information-and-data-systems?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/illustration?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/human-resources-management-with-law?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/human-resource-management-placement?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/human-resource-management?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/human-resource-management2?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/human-bioscience-and-enterprise?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/healthcare-science?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/health,-nutrition-and-exercise?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/health-psychology?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/health-and-social-care?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/health-and-exercise-science?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/graphic-design?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/forensic-science-and-criminology?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/sport-and-physical-education-sandwich3?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/forensicscience?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/football-studies?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/football-science?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/football-development?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/football-coaching?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/food-science,-technology-and-management?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/food-and-nutrition-science?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/film-production?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/film-and-television-production?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/fashion-design2?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/environmental-health-science?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/english-literature-and-tefl?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/english-literature?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/fine-art?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/teaching-english-as-a-foreign-language-tefl?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/english-language-and-literature?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/english-language-and-linguistics?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/english-and-theatre-studies?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/electronic-engineering?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/education-with-psychology?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/education-studies-and-english?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/education-studies?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/education-and-tefl?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/economics-and-finance?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/early-childhood-education?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/dance-and-professional-practice?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/cybersecurity?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/criminology-and-sociology?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/criminology?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/creative-writing-and-journalism?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/creative-writing?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/contemporary-arts-practice-with-professional-practice-year?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/contemporary-arts-practice?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/computing-and-mathematics?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/computing-and-data-science?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/computer-systems-engineering2?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/computer-security-and-forensics?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/computer-science-and-software-engineering?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/computer-science-and-robotics?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/computer-science?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/computer-networking?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/computer-games-development?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/computer-animation-and-visual-effects?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/communication-and-reputation-management?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/child-and-adolescent-studies?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/business-studies-with-marketing?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/business-studies-with-finance?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/business-studies-marketing2?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/business-studies-general-route?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/business-management-with-law?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/aviation-and-airport-management?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/automotive-engineering?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/artificial-intelligence-and-robotics?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/art-and-design?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/applied-psychology?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/applied-education-studies?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/applied-education-studies5?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/applied-education-studies3?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/applied-education-studies2?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/animation?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/advertising-and-marketing-communications?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/advertising-and-branding-design?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/acting?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/accounting-and-finance?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/event-management2?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/human-resource-management2?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/human-resource-management?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/accounting4?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/broadcast-television-and-radio?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/business-information-systems?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/business-economics2?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/business-management?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/biomedical-science?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/biochemistry?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/behavioural-science-and-health?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/biological-science?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/youth-and-community-work?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/broadcast-journalism?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/business-studies-general-route?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/travel,-aviation-and-tourism-management?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/theatre-and-professional-practice?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/television-production?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/telecommunications-and-network-engineering?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/sports-studies?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/strength-and-conditioning?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/sports-therapy?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/sport-science-and-coaching?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/sports-development-and-management?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/sport-and-physical-education-sandwich3?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/sport-and-physical-education?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/sport-science-and-personal-training?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/sports-journalism?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/special-needs-and-inclusive-education?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/sport-and-exercise-science?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/software-engineering?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/social-work?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/applied-social-studies?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/public-relations?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/radio-and-audio?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/psychology,-counselling-and-therapies?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/psychology-and-criminal-behaviour?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/psychology-and-criminology?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/product-design?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/psychology?=coursesearch-ug',
'https://www.beds.ac.uk/howtoapply/courses/undergraduate/next-year/primary-education-with-qts?=coursesearch-ug',]
        url=set(url)
        for u in url:
            yield scrapy.Request(url=u,callback=self.parsesss,meta={'url':u})
    def parsesss(self,response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.meta['url']
        item['university']='University of Bedfordshire'
        print(response.url)
        alevel=response.xpath('//li[contains(text(),"A level")]/text()').extract()
        print(alevel)
        item['alevel']=remove_class(alevel)
        yield item
    def parses(self, response):
        pro_url=response.xpath('//ul[@id="news-listing-one-column"]//h2/a/@href').extract()
        # print(len(pro_url))
        programme=response.xpath('//ul[@id="news-listing-one-column"]//h2/a/text()').extract()
        for i,pro in zip(pro_url,programme):
            yield scrapy.Request(url=i,callback=self.parses)
    def parsess(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'University of Bedfordshire'
        item['url'] = response.url
        programme = response.xpath('//div[@id="inner-course-content"]/h1/text()').extract()
        # print(programme)
        programme = ''.join(programme)
        # print(programme)
        degree_name=re.findall('[A-Z]{1,2}[a-z]*\s*\(Hons\)',programme)
        # print(degree_name)
        degree_name=''.join(degree_name)
        programme=programme.replace(degree_name,'').strip()
        item['programme_en']=programme
        item['degree_name']=degree_name
        # print(programme)


        item['tuition_fee_pre'] = '£'
        if 'MBA' in programme:
            # print(programme)
            item['tuition_fee'] = '12500'
        else:
            item['tuition_fee'] = '11500'

        location = response.xpath('//strong[contains(text(),"Campus Location")]/../text()').extract()
        location = ''.join(location).replace('-', '').strip()
        # print(location)
        item['location'] = location

        duration = response.xpath('//strong[contains(text(),"Duration")]/../text()').extract()
        duration = clear_duration(duration)
        # print(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']

        start_date = response.xpath('//strong[contains(text(),"Start")]/../text()').extract()
        # print(start_date)
        start_date = tracslateDate(start_date)
        # print(start_date)
        start_date = ','.join(start_date)
        # print(start_date)
        item['start_date'] = start_date

        overview = response.xpath('//div[@id="why_content"]').extract()
        overview = remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        modules = response.xpath('//div[@id="unit_content"]').extract()
        modules = remove_class(modules)
        # print(modules)
        item['modules_en'] = modules

        assessment_en = response.xpath('//div[@id="how_content"]').extract()
        assessment_en = remove_class(assessment_en)
        item['assessment_en'] = assessment_en

        rntry = response.xpath('//h2[@id="entry"]/following-sibling::div/ul[@class="tab-content"]/div[3]').extract()
        rntry = remove_class(rntry)
        # print(rntry)
        item['rntry_requirements'] = rntry

        item['ielts'] = '6.0'
        item['ielts_l'] = '5.5'
        item['ielts_s'] = '5.5'
        item['ielts_r'] = '5.5'
        item['ielts_w'] = '5.5'
        item['toefl'] = '80'
        item['toefl_l'] = '17'
        item['toefl_s'] = '20'
        item['toefl_r'] = '18'
        item['toefl_w'] = '17'

        career = response.xpath('//div[@id="career_content"]').extract()
        career = remove_class(career)
        # print(career)
        item['career_en'] = career

        apply_d = '<ul><li>A completed application form signed by you (an electronic signature is fine)</li><li>Copies of your official academic qualifications and certificates, including proof of your level of English Language (where relevant)</li><li>A one page personal statement. This should tell us why you want to study your chosen course.</li><li>A copy of your current valid passport details</li><li>Please submit copies of any UK Visa that you have held</li></ul>'
        apply_d = remove_class(apply_d)
        item['apply_documents_en'] = apply_d

        ucascode=response.xpath('//strong[contains(text(),"UCAS Code")]/../text()').extract()
        ucascode=''.join(ucascode).replace('-','').strip()
        item['ucascode']=ucascode

        require_chinese_en='<ul><li>Senior Middle School Certificate with transcripts of three years with an average of 60%</li><li>First year of university degree with complete transcripts with overall average marks of 60% or above</li><li>Additional Course requirements if any (see Faculty Course Requirements)</li></ul>'
        require_chinese_en=remove_class(require_chinese_en)
        item['require_chinese_en']=require_chinese_en

        apply_proces_en=['<p>There are two ways you can make a direct application to the University of Bedfordshire:</p><ul><li><a href="https://evision.beds.ac.uk/urd/sits.urd/run/siw_ipp_lgn.login?process=siw_ipp_app&amp;code1=OA_FORM&amp;code2=0007">Apply online now for 2017/18</a> Courses starting from 1 August 2017 to 31 July 2018</li><li>Download <span class="include_asset_summary"><a href="https://www.beds.ac.uk/__data/assets/pdf_file/0006/441798/International-Application-web-2018.pdf">an application form - <img src="https://www.beds.ac.uk/__data/asset_types/pdf_file/icon.png" alt="" title="" height="16" width="16"  class="sq-icon" /> PDF  1.0 MB ',
'</a></span> and submit it to our <a href="https://www.beds.ac.uk/international/international-applications/contactus">Admissions Team</a> along with scans of your supporting documents, via email, post or in person at the International Office.</li></ul><p>You can post your completed form to:</p><p>University of Bedfordshire International Admissions/International Office/University Square/Luton/Bedfordshire/LU1 3JU/United Kingdom</p><h4>Please note</h4><ul><li><strong>BSc (Hons) Nursing Studies</strong> Level 3 and <strong>MSc Advanced Nursing Studies</strong> are available to overseas students - please contact <a href="https://www.beds.ac.uk/international/international-applications/contactus">International Admissions</a></li><li><strong>Healthcare, Nursing and Midwifery students</strong> - many of these courses are not available to overseas students due to UK immigration law in regard to bursary funding. Please contact <a href="https://www.beds.ac.uk/international/international-applications/contactus">International Admissions</a> to find out if you are eligible to apply.</li></ul><p>*Please note that international students studying on a Tier 4 Student Visa must choose a full-time Undergraduate or Postgraduate course and are not eligible for part-time study.</p><p>Watch some more tips and advice on making your application to Bedfordshire:</p>',]
        apply_proces_en=remove_class(apply_proces_en)
        item['apply_documents_en']=apply_proces_en

        # print(item)

        yield item