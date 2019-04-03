# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem

class UniversityofstandrewsUSpider(scrapy.Spider):
    name = 'UniversityOfStAndrews_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.st-andrews.ac.uk/subjects/']
    def parse(self, response):
        urls=['https://www.st-andrews.ac.uk/subjects/biology/biology-mbiol/',
'https://www.st-andrews.ac.uk/subjects/biology/biology-bsc/',
'https://www.st-andrews.ac.uk/subjects/archaeology/archaeology-ma/',
'https://www.st-andrews.ac.uk/subjects/ancient-history/ancient-history-ma/',
'https://www.st-andrews.ac.uk/subjects/physics/astrophysics-mphys/',
'https://www.st-andrews.ac.uk/subjects/physics/astrophysics-bsc/',
'https://www.st-andrews.ac.uk/subjects/physics/physics-mphys/',
'https://www.st-andrews.ac.uk/subjects/physics/theoretical-physics-mphys/',
'https://www.st-andrews.ac.uk/subjects/italian/italian-ma/',
'https://www.st-andrews.ac.uk/subjects/international-relations/international-relations-ba/',
'https://www.st-andrews.ac.uk/subjects/medicine/medicine-bsc-a100/',
'https://www.st-andrews.ac.uk/subjects/medicine/medicine-bsc-a990/',
'https://www.st-andrews.ac.uk/subjects/physics/physics-bsc/',
'https://www.st-andrews.ac.uk/subjects/german/german-ma/',
'https://www.st-andrews.ac.uk/subjects/geography/geography-ma/',
'https://www.st-andrews.ac.uk/subjects/film-studies/film-studies-ba/',
'https://www.st-andrews.ac.uk/subjects/chemistry/chemistry-mchem/',
'https://www.st-andrews.ac.uk/subjects/geography/geography-bsc/',
'https://www.st-andrews.ac.uk/subjects/international-relations/international-relations-ma/',
'https://www.st-andrews.ac.uk/subjects/film-studies/film-studies-ma/',
'https://www.st-andrews.ac.uk/subjects/management/management-ma/',
'https://www.st-andrews.ac.uk/subjects/management/management-science-bsc/',
'https://www.st-andrews.ac.uk/subjects/management/management-bsc/',
'https://www.st-andrews.ac.uk/subjects/french/french-ma/',
'https://www.st-andrews.ac.uk/subjects/history/scottish-history-ma/',
'https://www.st-andrews.ac.uk/subjects/history/modern-history-ma/',
'https://www.st-andrews.ac.uk/subjects/chemistry/materials-chemistry-mchem/',
'https://www.st-andrews.ac.uk/subjects/history/mediaeval-history-ma/',
'https://www.st-andrews.ac.uk/subjects/history/history-ba/',
'https://www.st-andrews.ac.uk/subjects/history/history-ma/',
'https://www.st-andrews.ac.uk/subjects/psychology/psychology-ma/',
'https://www.st-andrews.ac.uk/subjects/middle-east-studies/middle-east-studies-ma/',
'https://www.st-andrews.ac.uk/subjects/philosophy/philosophy-ma/',
'https://www.st-andrews.ac.uk/subjects/economics/financial-economics-ma/',
'https://www.st-andrews.ac.uk/subjects/economics/financial-economics-bsc/',
'https://www.st-andrews.ac.uk/subjects/economics/economics-bsc/',
'https://www.st-andrews.ac.uk/subjects/economics/economics-ba/',
'https://www.st-andrews.ac.uk/subjects/economics/economics-ma/',
'https://www.st-andrews.ac.uk/subjects/psychology/psychology-bsc/',
'https://www.st-andrews.ac.uk/subjects/chemistry/chemistry-with-medicinal-chemistry-mchem/',
'https://www.st-andrews.ac.uk/subjects/sustainable-development/sustainable-development-bsc/',
'https://www.st-andrews.ac.uk/subjects/sustainable-development/sustainable-development-ma/',
'https://www.st-andrews.ac.uk/subjects/classics/classical-studies-ba/',
'https://www.st-andrews.ac.uk/subjects/neuroscience/neuroscience-bsc/',
'https://www.st-andrews.ac.uk/subjects/biology/zoology-bsc/',
'https://www.st-andrews.ac.uk/subjects/biology/molecular-biology-bsc/',
'https://www.st-andrews.ac.uk/subjects/marine-biology/marine-biology-mmarbiol/',
'https://www.st-andrews.ac.uk/subjects/latin/latin-ma/',
'https://www.st-andrews.ac.uk/subjects/classics/classics-ma/',
'https://www.st-andrews.ac.uk/subjects/greek/greek-ma/',
'https://www.st-andrews.ac.uk/subjects/classics/classical-studies-ma/',
'https://www.st-andrews.ac.uk/subjects/computer-science/computer-science-msci/',
'https://www.st-andrews.ac.uk/subjects/earth-environmental-sciences/geology-bsc/',
'https://www.st-andrews.ac.uk/subjects/computer-science/computer-science-bsc/',
'https://www.st-andrews.ac.uk/subjects/earth-environmental-sciences/environmental-earth-sciences-bsc/',
'https://www.st-andrews.ac.uk/subjects/spanish/spanish-ma/',
'https://www.st-andrews.ac.uk/subjects/mathematics/pure-mathematics-mmath/',
'https://www.st-andrews.ac.uk/subjects/social-anthropology/social-anthropology-ma/',
'https://www.st-andrews.ac.uk/subjects/chemistry/materials-chemistry-mchem/',
'https://www.st-andrews.ac.uk/subjects/mathematics/applied-mathematics-mmath/',
'https://www.st-andrews.ac.uk/subjects/mathematics/mathematics-mmath/',
'https://www.st-andrews.ac.uk/subjects/mathematics/mathematics-ma/',
'https://www.st-andrews.ac.uk/subjects/chemistry/chemistry-with-medicinal-chemistry-mchem/',
'https://www.st-andrews.ac.uk/subjects/mathematics/mathematics-bsc/',
'https://www.st-andrews.ac.uk/subjects/chemistry/chemistry-with-medicinal-chemistry-bsc/',
'https://www.st-andrews.ac.uk/subjects/russian/russian-ma/',
'https://www.st-andrews.ac.uk/subjects/statistics/statistics-bsc/',
'https://www.st-andrews.ac.uk/subjects/chemistry/chemical-sciences-bsc/',
'https://www.st-andrews.ac.uk/subjects/statistics/statistics-ma/',
'https://www.st-andrews.ac.uk/subjects/chemistry/chemistry-mchem/',
'https://www.st-andrews.ac.uk/subjects/statistics/statistics-mmath/',
'https://www.st-andrews.ac.uk/subjects/chemistry/materials-chemistry-bsc/',
'https://www.st-andrews.ac.uk/subjects/chemistry/chemistry-bsc/',
'https://www.st-andrews.ac.uk/subjects/earth-environmental-sciences/earth-sciences-mgeol/',
'https://www.st-andrews.ac.uk/subjects/divinity/new-testament-ma/',
'https://www.st-andrews.ac.uk/subjects/divinity/hebrew-ma/',
'https://www.st-andrews.ac.uk/subjects/divinity/theological-studies-ma/',
'https://www.st-andrews.ac.uk/subjects/divinity/theology-mtheol/',
'https://www.st-andrews.ac.uk/subjects/divinity/divinity-bd/',
'https://www.st-andrews.ac.uk/subjects/divinity/biblical-studies-ma/',
'https://www.st-andrews.ac.uk/subjects/english/english-ba/',
'https://www.st-andrews.ac.uk/subjects/english/english-ma/',
'https://www.st-andrews.ac.uk/subjects/art-history/art-history-ma/',
'https://www.st-andrews.ac.uk/subjects/marine-biology/marine-biology-bsc/',
'https://www.st-andrews.ac.uk/subjects/biology/evolutionary-biology-bsc/',
'https://www.st-andrews.ac.uk/subjects/biology/ecology-conservation-bsc/',
'https://www.st-andrews.ac.uk/subjects/biology/cell-biology-bsc/',
'https://www.st-andrews.ac.uk/subjects/chemistry/biomolecular-science-bsc/',
'https://www.st-andrews.ac.uk/subjects/biology/biochemistry-mbiochem/',
'https://www.st-andrews.ac.uk/subjects/biology/biochemistry-bsc/',
'https://www.st-andrews.ac.uk/subjects/biology/behavioural-biology-bsc/',]
        for u in urls:
            yield scrapy.Request(url=u,callback=self.pars,meta={'url':u})
    def pars(self,response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.meta['url']
        item['university']="University of St Andrews"
        print(response.url)
        tuition=response.xpath('//th[contains(text(),"versea")]/following-sibling::td/text()').extract()
        print(tuition)
        tui=re.findall('\d{2}\,\d{3}',''.join(tuition))
        item['tuition_fee']=''.join(tui).replace(',','').strip()
        #21290变成了22350
        yield item

    #补采
    # def parse(self, response):
    #     item=get_item1(ScrapyschoolEnglandItem)
    #     item['university'] = "University of St Andrews"
    #     item['url'] = response.url
    #     item['location'] = 'St Andrews'
    #     fee=response.xpath('//th[contains(text(),"Overseas")]/following-sibling::td//text()').extract()
    #     if fee==[]:
    #         # print(response.url)
    #         fee=response.xpath('//*[contains(text(),"£")]//text()').extract()
    #     tuition=getTuition_fee(fee)
    #     item['tuition_fee']=tuition
    #     yield item
    def parsew(self, response):
        url_list=response.xpath('//div[@class="col-sm-3"]/h4/a/@href').extract()
        for i in url_list:
            full_url='https://www.st-andrews.ac.uk'+i
            yield scrapy.Request(full_url,callback=self.parse_list)
    def parse_list(self,response):
        # print(response.url)
        pro_list=response.xpath('//h2[contains(text(),"Undergraduate")]/following-sibling::table/tbody/tr/td//a/@href').extract()
        programme=response.xpath('//h2[contains(text(),"Undergraduate")]/following-sibling::table/tbody/tr/td//a/text()').extract()
        degree_name=response.xpath('//h2[contains(text(),"Undergraduate")]/following-sibling::table/tbody/tr/td[2]//text()').extract()
        # print(len(pro_list),len(programme),len(degree_name))
        # print(pro_list)
        for url,pro,deg in zip(pro_list,programme,degree_name):
            yield scrapy.Request(url=url,callback=self.parses,meta={'programme':pro,'degree_name':deg})
    def parses(self,response):
        # print(response.url)
        if 'subjects' not in response.url:
            return None
        item=get_item1(ScrapyschoolEnglandItem)

        # programme=response.meta['programme']

        # print(programme)
        # print(degree_name)

        # item['major_type1']=programme

        item['university'] = "University of St Andrews"
        item['url'] = response.url
        item['location'] = 'St Andrews'
        item["tuition_fee_pre"] = "£"

        programme = response.xpath('//section/h2/text()').extract()
        programme = ''.join(programme).strip()
        # print(programme)
        deg=re.findall(' [A-Z]{2}.*',programme)
        # print(deg)
        programme=programme.replace(''.join(deg),'').strip()
        # print(programme)
        # degree_name = response.meta['degree_name']
        # programme = programme.replace(degree_name, '').strip()
        # degree_name = degree_name.replace('(', '').replace(')', '').strip()
        # print(programme)
        # item['degree_name'] = degree_name
        item['programme_en'] = programme
        overview = response.xpath('//section/h2/following-sibling::p').extract()
        overview = remove_class(overview)
        overview = clear_same_s(overview)
        # print(overview)
        item['overview_en'] = overview
        start_date = response.xpath('//*[contains(text(),"tart date")]//text()').extract()
        start_date=tracslateDate(start_date)
        # print(start_date)
        item['start_date']=','.join(start_date)

        deadline = response.xpath('//h3[contains(text(),"Application deadline")]/following-sibling::*[1]/text()').extract()
        deadline=tracslateDate(deadline)
        # print(deadline)
        item['deadline']=''.join(deadline)

        duration = response.xpath('//*[contains(text(),"ull time")]//text()').extract()
        # print(duration)
        duration=clear_duration(duration)
        # print(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']

        entry_requirements = response.xpath(
            '//h3[contains(text(),"Entry requirements")]/following-sibling::*').extract()
        entry_requirements = remove_class(entry_requirements)
        entry_requirements='<p>High school qualifications from this country do not usually satisfy our entrance requirements. If you have not completed the International Baccalaureate, A-levels, or the American High School Diploma, you will be required to complete a Foundation Year Programme. Further details of this can be found from our Centre for Interational Foundation Programmes.</p>'
        item['rntry_requirements'] = entry_requirements
        # print(item)
        tuition_fee = response.xpath('//*[contains(text(),"Tuition fees")]/following-sibling::p//text()').extract()
        tuition_fee = getTuition_fee(tuition_fee)
        item['tuition_fee'] = tuition_fee
        # print(tuition_fee)
        application_requirements = response.xpath(
            '//h3[contains(text(),"Application requirement")]/following-sibling::*').extract()
        application_requirements = remove_class(application_requirements)
        application_requirements = clear_same_s(application_requirements)
        # print(application_requirements)
        item['apply_desc_en'] = application_requirements
        modules = response.xpath('//div[@id="year-tabs-container"]/..').extract()
        modules = remove_class(modules)
        item['modules_en'] = modules
        # print(modules)

        career = response.xpath('//h3[contains(text(),"areers")]/following-sibling::*|'
                                '//h2[contains(text(),"Your future")]/../../following-sibling::*|'
                                '//h2[contains(text(),"Careers")]/../../following-sibling::*').extract()
        if career==[]:
            print(response.url)
        else:
            print('呦呦呦')
        career = remove_class(career)
        # print(career)
        item['career_en'] = career

        department = response.xpath(
            '//h3/*[contains(text(),"Contact info")]/../following-sibling::p[1]/strong[1]//text()').extract()
        department = ''.join(department)
        item['department'] = department
        # print(department)

        ielts=response.xpath('//p[contains(text(),"IELTS")]//text()').extract()
        ielts=get_ielts(ielts)
        # print(ielts)
        if ielts!=[]:
            item['ielts'] = ielts['IELTS']
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            # ielts=response.xpath('//*[contains(text(),"IELTS")]/text()').extract()
            # if ielts==[]:
            #     print(response.url)
            # else:
            #     print(ielts)
            # iel=re.findall('\d\.?\d?',''.join(ielts))
            # if len(iel)==2:
            #     iel=list(map(float,iel))
            #     item['ielts_desc'], item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']=''.join(ielts),max(iel),min(iel),min(iel),min(iel),min(iel)

        ucascode=response.xpath('//h3[contains(text(),"UCAS code")]/following-sibling::*[1]//text()').extract()
        ucascode=''.join(ucascode)
        # print(ucascode)
        item['ucascode']=ucascode[0:39]

        alevel=response.xpath('//th[contains(text(),"evels")]/following-sibling::td//text()').extract()
        alevel=' '.join(alevel).strip()
        # print(alevel)
        item['alevel']=alevel

        ib=response.xpath('//th[contains(text(),"IB")]/following-sibling::td//text()').extract()
        ib=' '.join(ib).strip()
        item['ib']=ib

        assessment=response.xpath('//h3[contains(text(),"Assessment")]/following-sibling::*').extract()
        assessment=remove_class(assessment)
        item['assessment_en']=assessment

        china=['<p>High school qualifications from this country do not usually satisfy our entrance requirements. If you have not completed the International Baccalaureate, A-levels, or the American High School Diploma, you will be required to complete a Foundation Year Programme.</p>']
        item['require_chinese_en']=china
        apply_proces_en=['<ol>',
'<li>Take a look at the courses available at the University of St Andrews. All courses can be found online in the <a href="/subjects/">course search</a> section or the <a href="/study/prospectus/ug-prospectus/">Undergraduate Prospectus</a>.</li>',
'<li>Check the minimum grades and any subject specific prerequisites for the course that you are interested in. For UK qualifications, these can be found on all online course pages and at the back of the <a href="/study/prospectus/ug-prospectus/">Undergraduate Prospectus</a>. All other students can find the international entry requirements on the <a href="/subjects/entry/">entry requirements</a> page.</li>',
'<li>You should also check the <a href="https://www.st-andrews.ac.uk/subjects/study-options/faculties/">Faculty entry requirements</a> for the course you are interested in.</li>',
'<li>If there is a choice of course between the Faculties of Arts (MA) and Science (BSc), you must decide which Faculty is for you. If you are applying for a course in one Faculty which is also offered in another Faculty, great care should be taken to cite the UCAS code numbers correctly; for example the course code for the Psychology (MA) degree differs from the Psychology (BSc) degree.</li>',
'<li>Once you have decided which course and faculty is the most appropriate, note the UCAS course code of your chosen course. This is the four digit code which can be found under the key information for your course.</li>',
'<li>Draft your UCAS personal statement carefully so that it reflects your choice of course. You can find more information about what we look for in an application on the <a href="/study/apply/ug/">how to apply page</a>.</li>',
'<li>Submit your UCAS application using the correct UCAS course code by the appropriate deadline. The current UCAS deadlines can be found below.</li>',
'</ol>',
]
        apply_proces_en=remove_class(apply_proces_en)
        item['apply_proces_en']=apply_proces_en

        # print(item)
        yield item

