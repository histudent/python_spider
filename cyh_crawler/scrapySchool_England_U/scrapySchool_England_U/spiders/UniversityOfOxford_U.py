# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
from scrapySchool_England_U.middlewares import *

class UniversityofoxfordUSpider(scrapy.Spider):
    name = 'UniversityOfOxford_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing?wssl=1']


    # 补抓
    # def parse(self, response):
    #     item=get_item1(ScrapyschoolEnglandItem)
    #     item['university'] = "University of Oxford"
    #     item['url'] = response.url
    #     overview=response.xpath('//div[@id="content-tab"]/child::*').extract()
    #     overview_split=response.xpath('//h2[contains(text(),"areer")]/self::*').extract()
    #     over_pre=response.xpath('//div[@class="field field-name-field-intro field-type-text-long field-label-hidden"]//text()').extract()
    #     over_pre='<p>'+''.join(over_pre).strip()+'</p>'
    #     if overview_split!=[]:
    #         overview=overview[0:overview.index(overview_split[0])]
    #         over=remove_class(overview)
    #         over=re.sub('<iframe.*</iframe>','',over)
    #         item['overview_en']=over_pre+over
    #         # yield item
    #     career_split=response.xpath('//h2[contains(text(),"aree")]/following-sibling::h2[1]/self::*').extract()
    #     career=response.xpath('//h2[contains(text(),"aree")]/self::*|//h2[contains(text(),"aree")]/following-sibling::*').extract()
    #     career=career[0:career.index(career_split[0])]
    #     item['career_en']=remove_class(career)
    #     assessment=response.xpath('//h2[contains(text(),"A typical week")]|//h2[contains(text(),"A typical week")]/following-sibling::*').extract()
    #     item['assessment_en']=remove_class(assessment)
    #     yield item
    def parse(self, response):
        urls=['https://www.ox.ac.uk/admissions/undergraduate/courses-listing/archaeology-and-anthropology?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/biochemistry-molecular-and-cellular?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/biology?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/biomedical-sciences?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/chemistry?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/classical-archaeology-and-ancient-history?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/classics-and-english?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/classics-and-modern-languages?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/classics-and-oriental-studies?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/classics?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/computer-science-and-philosophy?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/computer-science?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/earth-sciences-geology?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/economics-and-management?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/engineering-science?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/english-and-modern-languages?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/english-language-and-literature?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/fine-art?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/geography?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/history-ancient-and-modern?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/history-and-economics?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/history-and-english?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/history-and-modern-languages?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/history-and-politics?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/history-art?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/history?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/human-sciences?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/law-jurisprudence?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/materials-science?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/mathematics-and-computer-science?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/mathematics-and-philosophy?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/mathematics-and-statistics?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/mathematics?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/medicine?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/modern-languages-and-linguistics?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/modern-languages?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/music?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/oriental-studies?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/philosophy-and-modern-languages?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/philosophy-and-theology?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/philosophy-politics-and-economics?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/physics-and-philosophy?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/physics?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/psychology-experimental?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/psychology-philosophy-and-linguistics?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/religion-and-oriental-studies?wssl=1',
'https://www.ox.ac.uk/admissions/undergraduate/courses-listing/theology-and-religion?wssl=1',]
        for u in urls:
            yield scrapy.Request(url=u,callback=self.pars,meta={'url':u})
    def pars(self,response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.meta['url']
        item['university']="University of Oxford"
        tuition=response.xpath('//td[contains(text(),"versea")]/following-sibling::td[contains(text(),"£")]/text()').extract()
        print(tuition)
        tui=re.findall('\d{2}\,\d{3}',''.join(tuition))
        item['tuition_fee']=''.join(tui).replace(',','').strip()
        yield item

    def parsess(self, response):
        pro_url=response.xpath('//table[@class="table-reduced"]//a/@href').extract()
        programme=response.xpath('//table[@class="table-reduced"]//a/text()').extract()
        for i,pro in zip(pro_url,programme):
            i=i.replace('//','https://')
            yield scrapy.Request(url=i,callback=self.parses,meta={"programme":pro})
    def parses(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        # major_type1=response.meta['programme']
        # item['major_type1']=major_type1
        item['university'] = "University of Oxford"
        item['url'] = response.url
        item['location'] = 'Oxford'
        item['application_open_date']='2018-9-14'
        overview=response.xpath('//div[@id="content-tab"]').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en']=overview
        modules=response.xpath('//div[@id="content-tab"]//h2[contains(text(),"A typical weekly timetable")]/following-sibling::*').extract()
        modules=remove_class(modules)
        # print(modules)
        if modules=='':
            # print(response.url)
            modules=response.xpath('//div[@id="content-tab"]//h2[contains(text(),"Related courses")]/following-sibling::*').extract()
            modules=remove_class(modules)
            # print(modules)
        item['modules_en']=modules
        item['toefl_l'] = '22'
        item['toefl_s'] = '25'
        item['toefl_r'] = '24'
        item['toefl_w'] = '24'

        # if 'Math' in major_type1 or 'Computer' in major_type1:
        #     item['ielts']='7.0'
        #     item['ielts_l']='6.5'
        #     item['ielts_s'] = '6.5'
        #     item['ielts_r'] = '6.5'
        #     item['ielts_w'] = '6.5'
        #     item['toefl']='100'
        # else:
        #     item['ielts'] = '7.5'
        #     item['ielts_l'] = '7.0'
        #     item['ielts_s'] = '7.0'
        #     item['ielts_r'] = '7.0'
        #     item['ielts_w'] = '7.0'
        #     item['toefl'] = '110'

        require_chinese_en=["<p>Senior High School Diploma, Chinese University Entrance Examination or 'GaoKao' would not be sufficient for candidates to make a competitive application</p>",
"<p>You could take British A-levels (the British Council may know where you can take A-levels in your country), the International Baccalaureate (IB), or any other qualifications listed as acceptable on this page. The first year of a bachelor's degree from another university could also be an acceptable alternative.</p>"]
        require_chinese_en=remove_class(require_chinese_en)
        item['require_chinese_en']=require_chinese_en

        ib=response.xpath('//strong[contains(text(),"IB")]/../text()').extract()
        ib=''.join(ib).strip()
        item['ib']=ib

        alevel=response.xpath('//strong[contains(text(),"A-level")]/../text()').extract()
        alevel=''.join(alevel).strip()
        item['alevel']=alevel

        assessment = response.xpath('//strong[contains(text(),"ssessment")]/../..').extract()
        if assessment==[]:
            print(response.url)
        item['assessment_en']=remove_class(assessment)

        applyproces_en=response.xpath('//div[@id="content-tab--4"]').extract()
        applyproces_en=remove_class(applyproces_en)
        item['apply_proces_en']=applyproces_en

        programme=response.xpath('//header[@id="main-title"]/h1/text()').extract()
        programme=''.join(programme).strip()
        item['programme_en']=programme
        #ret_list = list((set(a_list).union(set(b_list)))^(set(a_list)^set(b_list)))
        career_a=response.xpath('//h2[contains(text(),"areer")]/following-sibling::*').extract()
        career_b=response.xpath('//h2[contains(text(),"areer")]/following-sibling::h2[1]/preceding-sibling::p').extract()
        career=list((set(career_a).union(set(career_b)))^(set(career_a)^set(career_b)))
        career=remove_class(career)
        # print(career)
        item['career_en']=career

        fee=response.xpath('//td[contains(text(),"Overseas")]/following-sibling::td/text()').extract()
        tuition=getTuition_fee(fee)
        item['tuition_fee']=tuition
        # print(tuition)

        duration = response.xpath('//h2[contains(text()," in ")]//text()').extract()
        # print(duration)
        durations = clear_duration(duration)
        # print(duration)
        item['duration'] = durations['duration']
        item['duration_per'] = durations['duration_per']
        if duration != []:
            deg = duration[0]
            # print(deg)
            us = re.findall('UCAS.*', deg)
            # print(us)
            deg = deg.replace(''.join(us), '').strip()
            # print(deg)
            degree_name = re.findall('[BM][A-Z][a-zA-Z]*', deg)
            # print(degree_name)
            degree_name = ' '.join(degree_name)
            if degree_name == '':
                # print(response.url)
                degree_name = 'BA MBiol'
        else:
            degree_name = ''
        degree_name = degree_name.split(' ')
        div = response.xpath(
            '//div[@class="field field-name-field-related-content-top field-type-text-long field-label-hidden field-group-field-odd"]//text()').extract()
        # print(div)
        UCAS = re.findall('\s?[A-Z][A-Z0-9]{3}\s?',','.join(div))
        print(UCAS)
        ucas=[]
        yield item
        # for i in UCAS:
        #     if 'UCAS' not in i:
        #         ucas.append(i.strip())
        # #//strong[contains(text(),"Oriental Studies")]/../../following-sibling::tr/td/text()
        # # print(ucas)
        # for deg in degree_name:
        #     item['degree_name']=deg
        #     if ucas!=[]:
        #         for u in ucas:
        #             item['ucascode']=u.strip()
        #             yield item
        #     else:
        #         item['ucascode']=''
        #         yield item



