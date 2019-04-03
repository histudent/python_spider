# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.clearSpace import clear_same_s
import requests, json
from lxml import etree

class UniversityofstandrewsPSpider(scrapy.Spider):
    name = 'UniversityOfStAndrews_P'
    allowed_domains = ['www.st-andrews.ac.uk']
    start_urls = ['https://www.st-andrews.ac.uk/subjects/']

    def parse(self, response):
        urls=['https://www.st-andrews.ac.uk/subjects/archive/2018-2019/pg/central-eastern-european-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/art-history/art-history-mlitt/',
'https://www.st-andrews.ac.uk/subjects/art-history/history-photography-mlitt/',
'https://www.st-andrews.ac.uk/subjects/art-history/museum-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/chemistry/catalysis-msc/',
'https://www.st-andrews.ac.uk/subjects/chemistry/chemical-science-msc/',
'https://www.st-andrews.ac.uk/subjects/classics/classics-mlitt/',
'https://www.st-andrews.ac.uk/subjects/comparative-literature/comparative-literature-mlitt/',
'https://www.st-andrews.ac.uk/subjects/comparative-literature/crossways-cultural-narratives-mlitt/',
'https://www.st-andrews.ac.uk/subjects/computer-science/advanced-computer-science-msc/',
'https://www.st-andrews.ac.uk/subjects/computer-science/advanced-systems-dependability-msc/',
'https://www.st-andrews.ac.uk/subjects/computer-science/artificial-intelligence-msc/',
'https://www.st-andrews.ac.uk/subjects/computer-science/computer-communication-systems-msc/',
'https://www.st-andrews.ac.uk/subjects/computer-science/computing-information-technology-msc/',
'https://www.st-andrews.ac.uk/subjects/computer-science/human-computer-interaction-msc/',
'https://www.st-andrews.ac.uk/subjects/computer-science/information-technology-msc/',
'https://www.st-andrews.ac.uk/subjects/computer-science/management-information-technology-msc/',
'https://www.st-andrews.ac.uk/subjects/computer-science/software-engineering-msc/',
'https://www.st-andrews.ac.uk/subjects/divinity/analytic-exegetical-theology-mlitt/',
'https://www.st-andrews.ac.uk/subjects/divinity/bible-contemporary-world-mlitt/',
'https://www.st-andrews.ac.uk/subjects/divinity/biblical-languages-literature-mlitt/',
'https://www.st-andrews.ac.uk/subjects/divinity/systematic-historical-theology-mlitt/',
'https://www.st-andrews.ac.uk/subjects/divinity/theology-arts-mlitt/',
'https://www.st-andrews.ac.uk/subjects/earth-environmental-sciences/geochemistry-msc/',
'https://www.st-andrews.ac.uk/subjects/earth-environmental-sciences/mineral-resources-msc/',
'https://www.st-andrews.ac.uk/subjects/economics/economics-msc/',
'https://www.st-andrews.ac.uk/subjects/economics/finance-economics-msc/',
'https://www.st-andrews.ac.uk/subjects/economics/finance-msc/',
'https://www.st-andrews.ac.uk/subjects/economics/money-banking-finance-msc/',
'https://www.st-andrews.ac.uk/subjects/english/creative-writing-mlitt/',
'https://www.st-andrews.ac.uk/subjects/english/medieval-english-mlitt/',
'https://www.st-andrews.ac.uk/subjects/english/modern-literature-mlitt/',
'https://www.st-andrews.ac.uk/subjects/english/playwriting-screenwriting-mlitt/',
'https://www.st-andrews.ac.uk/subjects/english/postcolonial-world-literatures-mlitt/',
'https://www.st-andrews.ac.uk/subjects/english/romantic-victorian-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/english/shakespeare-renaissance-literature-mlitt/',
'https://www.st-andrews.ac.uk/subjects/english/women-writing-gender-mlitt/',
'https://www.st-andrews.ac.uk/subjects/film-studies/film-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/french/cultural-identity-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/french/french-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/german/german-comparative-literature-mlitt/',
'https://www.st-andrews.ac.uk/subjects/german/german-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/history/book-history-mlitt/',
'https://www.st-andrews.ac.uk/subjects/history/early-modern-history-mlitt/',
'https://www.st-andrews.ac.uk/subjects/history/economic-social-history-msc/',
'https://www.st-andrews.ac.uk/subjects/history/environmental-history-mlitt/',
'https://www.st-andrews.ac.uk/subjects/history/intellectual-history-mlitt/',
'https://www.st-andrews.ac.uk/subjects/history/legal-constitutional-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/history/mediaeval-history-mlitt/',
'https://www.st-andrews.ac.uk/subjects/history/mediaeval-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/history/middle-eastern-history-mlitt/',
'https://www.st-andrews.ac.uk/subjects/history/modern-history-mlitt/',
'https://www.st-andrews.ac.uk/subjects/history/reformation-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/history/scottish-historical-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/history/transnational-history-mlitt/',
'https://www.st-andrews.ac.uk/subjects/interdisciplinary/conservation-studies-msc/',
'https://www.st-andrews.ac.uk/subjects/interdisciplinary/contemporary-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/interdisciplinary/international-development-msc/',
'https://www.st-andrews.ac.uk/subjects/international-relations/international-political-theory-mlitt/',
'https://www.st-andrews.ac.uk/subjects/international-relations/international-security-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/international-relations/meccass-mlitt/',
'https://www.st-andrews.ac.uk/subjects/international-relations/peace-conflict-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/international-relations/strategic-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/international-relations/terrorism-mlitt/',
'https://www.st-andrews.ac.uk/subjects/italian/italian-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/management/banking-finance-msc/',
'https://www.st-andrews.ac.uk/subjects/management/finance-management-msc/',
'https://www.st-andrews.ac.uk/subjects/management/human-resource-management-mlitt/',
'https://www.st-andrews.ac.uk/subjects/management/international-business-mlitt/',
'https://www.st-andrews.ac.uk/subjects/management/management-mlitt/',
'https://www.st-andrews.ac.uk/subjects/management/marketing-mlitt/',
'https://www.st-andrews.ac.uk/subjects/marine-biology/marine-ecosystem-management-msc/',
'https://www.st-andrews.ac.uk/subjects/marine-biology/marine-mammal-science-msc/',
'https://www.st-andrews.ac.uk/subjects/mathematics/mathematics-msc/',
'https://www.st-andrews.ac.uk/subjects/medicine/health-psychology-msc/',
'https://www.st-andrews.ac.uk/subjects/middle-east-studies/iranian-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/middle-east-studies/middle-eastern-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/neuroscience/neuroscience-mres/',
'https://www.st-andrews.ac.uk/subjects/philosophy/epistemology-mind-language-mlitt/',
'https://www.st-andrews.ac.uk/subjects/philosophy/history-philosophy-mlitt/',
'https://www.st-andrews.ac.uk/subjects/philosophy/logic-metaphysics-mlitt/',
'https://www.st-andrews.ac.uk/subjects/philosophy/moral-political-legal-philosophy-mlitt/',
'https://www.st-andrews.ac.uk/subjects/philosophy/philosophy-mlitt/',
'https://www.st-andrews.ac.uk/subjects/physics/astrophysics-msc/',
'https://www.st-andrews.ac.uk/subjects/physics/photonics-msc/',
'https://www.st-andrews.ac.uk/subjects/psychology/evolutionary-psychology-msc/',
'https://www.st-andrews.ac.uk/subjects/psychology/psychology-conversion-msc/',
'https://www.st-andrews.ac.uk/subjects/psychology/research-psychology-msc/',
'https://www.st-andrews.ac.uk/subjects/russian/russian-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/social-anthropology/anthropology-art-perception-mres/',
'https://www.st-andrews.ac.uk/subjects/social-anthropology/pacific-anthropology-mres/',
'https://www.st-andrews.ac.uk/subjects/social-anthropology/social-anthropology-mres/',
'https://www.st-andrews.ac.uk/subjects/spanish/spanish-studies-mlitt/',
'https://www.st-andrews.ac.uk/subjects/statistics/applied-statistics-datamining-msc/',
'https://www.st-andrews.ac.uk/subjects/statistics/data-intensive-analysis-msc/',
'https://www.st-andrews.ac.uk/subjects/statistics/statistics-msc/',
'https://www.st-andrews.ac.uk/subjects/sustainable-development/sdee-msc/',
'https://www.st-andrews.ac.uk/subjects/sustainable-development/sustainable-development-energy-msc/',
'https://www.st-andrews.ac.uk/subjects/sustainable-development/sustainable-development-mres/',
'https://www.st-andrews.ac.uk/subjects/sustainable-development/sustainable-development-msc/',]
        for u in urls:
            yield scrapy.Request(url=u,callback=self.parsea,meta={'url':u})
    def parsea(self,response):
        item=get_item1(ScrapyschoolEnglandItem1)
        item['url']=response.meta['url']
        item['university']="University of St Andrews"
        print(response.url)
        tuition=response.xpath('//strong[contains(text(),"versea")]/following-sibling::text()[1]').extract()
        print(tuition)
        tui=re.findall('\d{2}\,\d{3}',''.join(tuition))
        print(tui)
        item['tuition_fee']=''.join(tui).replace(',','').strip()
        if tui!=[]:
            yield item
    def parses(self, response):
        urllist=response.xpath('//h2[contains(text(),"Subjects")]/following-sibling::div//a/@href').extract()
        for i in urllist:
            fullurl='https://www.st-andrews.ac.uk%s' % i
            yield scrapy.Request(fullurl,callback=self.parse_list)
    def parse_list(self,response):
        urllist=response.xpath('//h2[contains(text(),"Postgraduate")]/following-sibling::table//a/@href').extract()
        for i in urllist:
            yield scrapy.Request(i,callback=self.parses)

    def parsess(self,response):
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "University of St Andrews"
        item['url'] = response.url
        item['location'] = 'St Andrews'
        item["tuition_fee_pre"] = "£"

        item['degree_type'] = 2
        item['teach_time'] = 'fulltime'
        programme=response.xpath('//section/h2/text()').extract()
        programme=''.join(programme).strip()
        # print(programme)
        degree_type=re.findall('\(.*\)',programme)
        degree_type=''.join(degree_type)
        programme=programme.replace(degree_type,'').strip()
        degree_type=degree_type.replace('(','').replace(')','').strip()
        # print(degree_type)
        # print(programme)
        item['degree_name'] = degree_type
        item['programme_en'] = programme
        overview=response.xpath('//section/h2/following-sibling::p').extract()
        overview=remove_class(overview)
        overview=clear_same_s(overview)
        # print(overview)
        item['overview_en'] = overview
        start_date=response.xpath('//*[contains(text(),"Start date")]//text()').extract()
        start_date=''.join(start_date)
        start_date=start_date.replace('Start date:','').strip()
        item['start_date'] = '2018-9-10'
        # print(start_date)
        deadline=response.xpath('//*[contains(text(),"End date")]//text()').extract()
        deadline=''.join(deadline)
        deadline=deadline.replace('End date:','').strip()
        item['deadline'] = '2019-1'
        # print(deadline)
        duration=response.xpath('//*[contains(text(),"Course duration")]/following-sibling::p[1]//text()').extract()
        # print(duration)
        duration=''.join(duration)
        duration=re.findall('[a-zA-Z\s]*years?\s.*full',duration)
        # print(duration)
        duration=''.join(duration)
        if duration=='One year full':
            duration='1'
        elif duration=='Two years full':
            duration='2'
        else:
            duration='1'
        item['duration'] = duration
        item['duration_per'] = 1
        entry_requirements=response.xpath('//h3[contains(text(),"Entry requirements")]/following-sibling::*').extract()
        entry_requirements=remove_class(entry_requirements)
        entry_requirements=clear_same_s(entry_requirements)
        item['rntry_requirements'] = entry_requirements
        # print(item)
        tuition_fee=response.xpath('//*[contains(text(),"Tuition fees")]/following-sibling::p//text()').extract()
        tuition_fee=getTuition_fee(tuition_fee)
        item['tuition_fee'] = tuition_fee
        # print(tuition_fee)
        application_requirements=response.xpath('//h3[contains(text(),"Application requirement")]/following-sibling::*').extract()
        application_requirements=remove_class(application_requirements)
        application_requirements=clear_same_s(application_requirements)
        # print(application_requirements)
        item['apply_desc_en']=application_requirements
        modules=response.xpath('//div[@id="year-tabs-container"]/..').extract()
        modules=remove_class(modules)
        modules=clear_same_s(modules)
        item['modules_en'] = modules
        # print(modules)

        career=response.xpath('//h3[contains(text(),"Career")]/following-sibling::*|'
                              '//h2[contains(text(),"areer")]/../../following-sibling::div').extract()
        if career==[]:
            print(response.url)
        else:
            print('呦呦呦')
            # print(career)
        career=remove_class(career)
        # print(career)
        item['career_en'] = career
        chi="<p>Postgraduate candidates will be expected to hold a Bachelor's degree from a prestigious university with an overall mark of 85% or above.</p>"
        item['require_chinese_en']=remove_class(chi)

        department=response.xpath('//h3/*[contains(text(),"Contact info")]/../following-sibling::p[1]/strong[1]//text()').extract()
        department=''.join(department)
        item['department'] = department
        # print(department)
        item['ielts'] = '7.0'
        item['ielts_l'] = '6.5'
        item['ielts_s'] = '6.5'
        item['ielts_r'] = '6.5'
        item['ielts_w'] = '6.5'
        # print(item)
        yield item
