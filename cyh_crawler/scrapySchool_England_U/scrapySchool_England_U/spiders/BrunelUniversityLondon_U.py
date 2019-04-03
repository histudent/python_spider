# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem

class BruneluniversitylondonUSpider(scrapy.Spider):
    name = 'BrunelUniversityLondon_U'
    # allowed_domains = ['brunel.ac.uk']
    start_urls=['http://www.brunel.ac.uk/study/Course-listing?courseLevel=0/2/24/28/43']

    def parse(self, response):
        urls=['http://www.brunel.ac.uk/study/undergraduate/Accountancy-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Accountancy-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Aerospace-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Aerospace-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Aerospace-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Aerospace-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Anthropology-and-Sociology-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Anthropology-and-Sociology-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Anthropology-and-Sociology-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Anthropology-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Anthropology-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Anthropology-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Automotive-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Automotive-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Automotive-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Automotive-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Aviation-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Aviation-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Aviation-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Aviation-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Aviation-Engineering-with-Pilot-Studies-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Aviation-Engineering-with-Pilot-Studies-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Aviation-Engineering-with-Pilot-Studies-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Aviation-Engineering-with-Pilot-Studies-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Banking-and-Finance-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Banking-and-Finance-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Biomedical-Sciences-Biochemistry-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Biomedical-Sciences-Biochemistry-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Biomedical-Sciences-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Biomedical-Sciences-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Biomedical-Sciences-Genetics-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Biomedical-Sciences-Genetics-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Biomedical-Sciences-Human-Health-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Biomedical-Sciences-Human-Health-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Biomedical-Sciences-Immunology-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Biomedical-Sciences-Immunology-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Business-and-Management-Accounting-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Business-and-Management-Accounting-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Business-and-Management-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Business-and-Management-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Business-and-Management-Marketing-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Business-and-Management-Marketing-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Business-Computing-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Business-Computing-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Business-Computing-eBusiness-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Business-Computing-eBusiness-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Business-Computing-Human-Computer-Interaction-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Business-Computing-Human-Computer-Interaction-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Business-Computing-Social-Media-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Business-Computing-Social-Media-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Civil-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Civil-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Civil-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Civil-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Civil-Engineering-with-Sustainability-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Civil-Engineering-with-Sustainability-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Civil-Engineering-with-Sustainability-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Civil-Engineering-with-Sustainability-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Communication-and-Media-Studies-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Communication-and-Media-Studies-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Computer-Science-Artificial-Intelligence-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Computer-Science-Artificial-Intelligence-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Computer-Science-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Computer-Science-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Computer-Science-Digital-Media-and-Games-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Computer-Science-Digital-Media-and-Games-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Computer-Science-Network-Computing-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Computer-Science-Network-Computing-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Computer-Science-Software-Engineering-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Computer-Science-Software-Engineering-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Computer-Systems-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Computer-Systems-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Computer-Systems-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Computer-Systems-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Creative-Writing-BA',
'http://www.brunel.ac.uk/study/undergraduate/Creative-Writing-BA',
'http://www.brunel.ac.uk/study/undergraduate/Digital-Design-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Digital-Design-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Economics-and-Accounting-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Economics-and-Accounting-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Economics-and-Business-Finance-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Economics-and-Business-Finance-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Economics-and-Management-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Economics-and-Management-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Economics-and-Mathematics-with-an-Integrated-Foundation-Year',
'http://www.brunel.ac.uk/study/undergraduate/Economics-and-Mathematics-with-an-Integrated-Foundation-Year',
'http://www.brunel.ac.uk/study/undergraduate/Economics-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Economics-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Education-BA',
'http://www.brunel.ac.uk/study/undergraduate/Education-BA',
'http://www.brunel.ac.uk/study/undergraduate/Electrical-Engineering-with-Renewable-Energy-Systems-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Electrical-Engineering-with-Renewable-Energy-Systems-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Electronic-and-Communications-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Electronic-and-Communications-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Electronic-and-Communications-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Electronic-and-Communications-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Electronic-and-Computer-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Electronic-and-Computer-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Electronic-and-Computer-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Electronic-and-Computer-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Electronic-and-Electrical-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Electronic-and-Electrical-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Electronic-and-Electrical-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Electronic-and-Electrical-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/English-BA',
'http://www.brunel.ac.uk/study/undergraduate/English-BA',
'http://www.brunel.ac.uk/study/undergraduate/English-with-Creative-Writing-BA',
'http://www.brunel.ac.uk/study/undergraduate/English-with-Creative-Writing-BA',
'http://www.brunel.ac.uk/study/undergraduate/Environmental-Sciences-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Environmental-Sciences-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Environmental-Sciences-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Film-and-Television-Studies-and-English',
'http://www.brunel.ac.uk/study/undergraduate/Film-and-Television-Studies-BA',
'http://www.brunel.ac.uk/study/undergraduate/Finance-and-Accounting-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Finance-and-Accounting-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Financial-Mathematics-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Financial-Mathematics-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Financial-Mathematics-MMath',
'http://www.brunel.ac.uk/study/undergraduate/Financial-Mathematics-MMath',
'http://www.brunel.ac.uk/study/undergraduate/Games-Design-and-Creative-Writing-BA',
'http://www.brunel.ac.uk/study/undergraduate/Games-Design-BA',
'http://www.brunel.ac.uk/study/undergraduate/History-BA',
'http://www.brunel.ac.uk/study/undergraduate/History-BA',
'http://www.brunel.ac.uk/study/undergraduate/Industrial-Design-and-Technology-BA',
'http://www.brunel.ac.uk/study/undergraduate/Industrial-Design-and-Technology-BA',
'http://www.brunel.ac.uk/study/undergraduate/International-Business-BSc',
'http://www.brunel.ac.uk/study/undergraduate/International-Business-BSc',
'http://www.brunel.ac.uk/study/undergraduate/International-Politics-BSc',
'http://www.brunel.ac.uk/study/undergraduate/International-Politics-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Journalism-and-Culture-BA',
'http://www.brunel.ac.uk/study/undergraduate/Law-LLB',
'http://www.brunel.ac.uk/study/undergraduate/Law-LLB',
'http://www.brunel.ac.uk/study/undergraduate/Law-with-Criminal-Justice-LLB',
'http://www.brunel.ac.uk/study/undergraduate/Law-with-Criminal-Justice-LLB',
'http://www.brunel.ac.uk/study/undergraduate/Law-with-International-Arbitration-and-Commercial-Law-LLB',
'http://www.brunel.ac.uk/study/undergraduate/Law-with-International-Arbitration-and-Commercial-Law-LLB',
'http://www.brunel.ac.uk/study/undergraduate/Life-Sciences-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Life-Sciences-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Mathematics-and-Statistics-with-Management-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Mathematics-and-Statistics-with-Management-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Mathematics-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Mathematics-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Mathematics-MMath',
'http://www.brunel.ac.uk/study/undergraduate/Mathematics-MMath',
'http://www.brunel.ac.uk/study/undergraduate/Mathematics-with-Computer-Science-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Mathematics-with-Computer-Science-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Mechanical-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Mechanical-Engineering-BEng',
'http://www.brunel.ac.uk/study/undergraduate/Mechanical-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Mechanical-Engineering-MEng',
'http://www.brunel.ac.uk/study/undergraduate/Military-and-International-History-BA',
'http://www.brunel.ac.uk/study/undergraduate/Military-and-International-History-BA',
'http://www.brunel.ac.uk/study/undergraduate/Music-BA',
'http://www.brunel.ac.uk/study/undergraduate/Music-BA',
'http://www.brunel.ac.uk/study/undergraduate/Occupational-Therapy-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Physical-Education-and-Youth-Sport-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Physical-Education-and-Youth-Sport-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Physiotherapy-BSc-full-time-programme',
'http://www.brunel.ac.uk/study/undergraduate/Politics-and-History-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Politics-and-History-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Politics-and-Sociology-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Politics-and-Sociology-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Politics-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Politics-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Product-Design-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Product-Design-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Product-Design-Engineering-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Product-Design-Engineering-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Psychology-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Psychology-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Psychology-Sport-Health-and-Exercise-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Psychology-Sport-Health-and-Exercise-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Sociology-and-Media-Studies-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Sociology-and-Media-Studies-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Sociology-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Sociology-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Sport-Health-and-Exercise-Sciences-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Sport-Health-and-Exercise-Sciences-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Sport-Health-and-Exercise-Sciences-Coaching-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Sport-Health-and-Exercise-Sciences-Coaching-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Sport-Health-and-Exercise-Sciences-Human-Performance-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Sport-Health-and-Exercise-Sciences-Human-Performance-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Sport-Health-and-Exercise-Sciences-Sport-Development-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Sport-Health-and-Exercise-Sciences-Sport-Development-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Sport-Health-and-Exercise-Sciences-with-Business-Studies-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Sport-Health-and-Exercise-Sciences-with-Business-Studies-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Theatre-and-Creative-Writing-BA',
'http://www.brunel.ac.uk/study/undergraduate/Theatre-and-Creative-Writing-BA',
'http://www.brunel.ac.uk/study/undergraduate/Theatre-and-English-BA',
'http://www.brunel.ac.uk/study/undergraduate/Theatre-and-English-BA',
'http://www.brunel.ac.uk/study/undergraduate/Theatre-BA',
'http://www.brunel.ac.uk/study/undergraduate/Theatre-BA',
'http://www.brunel.ac.uk/study/undergraduate/Visual-Effects-and-Motion-Graphics-BSc',
'http://www.brunel.ac.uk/study/undergraduate/Visual-Effects-and-Motion-Graphics-BSc',]
        urls=set(urls)
        for u in urls:
            yield scrapy.Request(url=u,callback=self.parsesss,meta={'url':u})
    def parsesss(self,response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.meta['url']
        item['university']='Brunel University London'
        print(response.url)
        alevel=response.xpath('//b[contains(text(),"GCE A-level")]/../text()|//strong[contains(text(),"GCE A-level")]/../text()').extract()
        if alevel==[]:
            alevel=response.xpath('//p[contains(text(),"GCE A-level")]/text()').extract()
        if alevel==[]:
            alevel=response.xpath('//*[contains(text(),"GCE A")]/../text()').extract()
        # print(alevel)
        item['alevel']=remove_class(alevel)
        ib = response.xpath(
            '//b[contains(text(),"International Baccalaureate")]/../text()|//strong[contains(text(),"International Baccalaureate")]/../text()').extract()
        if ib == []:
            ib = response.xpath('//p[contains(text(),"International Baccalaureate")]/text()').extract()
        print(ib)
        item['ib']=remove_class(ib)
        yield item


    def parsess(self, response):
        print(response.url)
        next_page=response.xpath('//li/a[contains(text(),"❯")]/@href').extract()
        url_list = response.xpath('//table[@id="responsive-example-table"]/tbody//a/@href').extract()
        for i in url_list:
            fullurl = 'http://www.brunel.ac.uk%s' % i
            yield scrapy.Request(fullurl, callback=self.parses)
        if next_page!=[]:
            next_url='http://www.brunel.ac.uk'+next_page[0]
            yield scrapy.Request(next_url,callback=self.parse)
    def parses(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = "Brunel University London"
        item['url'] = response.url
        item['location'] = 'London'
        item['tuition_fee_pre'] = '£'
        item['degree_type'] = 1
        item['deadline'] = '2019-7'
        programme = response.url.split('/')[-1]
        # print(programme)
        degree_name = programme.split('-')[-1]
        if degree_name[0] != 'L':
            programme = programme.replace(degree_name, '')
            programme = programme.replace('-', ' ').strip()
        else:
            degree_name = ''
            programme = programme.replace('-', ' ').strip()
        # print(programme)
        # print(degree_name)
        item['programme_en'] = programme
        item['degree_name'] = degree_name

        overview = response.xpath('//h2[contains(text(),"Overview")]/following-sibling::*').extract()
        overview = remove_class(overview)
        overview = clear_same_s(overview)
        # print(overview)
        item['overview_en'] = overview

        modules = response.xpath('//h2[contains(text(),"Course content")]/following-sibling::*').extract()
        modules = remove_class(modules)
        modules = clear_same_s(modules)
        # print(modules)
        item['modules_en'] = modules

        career = response.xpath('//h2[contains(text(),"Employ")]/following-sibling::*').extract()
        career = remove_class(career)
        career = clear_same_s(career)
        # print(career)
        item['career_en'] = career

        rntry = response.xpath('//h2[contains(text(),"Entry")]/following-sibling::*').extract()
        rntry = remove_class(rntry)
        rntry = clear_same_s(rntry)
        # print(rntry)
        item['require_chinese_en'] = rntry

        accessment = response.xpath('//h2[contains(text(),"Assessment")]/following-sibling::*').extract()
        accessment = remove_class(accessment)
        accessment = clear_same_s(accessment)
        item['assessment_en'] = accessment

        fees = response.xpath('//span[contains(text(),"nternational")]/following-sibling::*[1]//text()').extract()
        tuition_fee = getTuition_fee(fees)
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee

        department = response.xpath('//a[contains(text(),"Subject area")]/text()').extract()
        department = ''.join(department)
        department = department.replace('Subject area:', '').strip()
        # print(department)
        item['department'] = department

        # item['start_date'] = '2018-9,2019-1'
        start_date=response.xpath('//h6[contains(text(),"Start date")]/following-sibling::p[1]/text()').extract()
        start_date=set(start_date)
        start_date=tracslateDate(start_date)
        # print(start_date)
        start_date=''.join(start_date).strip()
        item['start_date']=start_date

        ielts=response.xpath('//li[contains(text(),"IELTS")]/text()').extract()
        item['ielts_desc']=''.join(ielts).strip()
        ielts=re.findall('\d\.?\d?',''.join(ielts))
        # print(ielts)
        ielts=list(map(float,ielts))
        if ielts!=[]:
            item['ielts_l'] = min(ielts)
            item['ielts_s'] = min(ielts)
            item['ielts_r'] = min(ielts)
            item['ielts_w'] = min(ielts)
            item['ielts'] = max(ielts)

        duration = response.xpath('//*[contains(text(),"Mode of ")]/following-sibling::p[1]/text()').extract()
        # print(duration)
        duration = ''.join(duration)
        dura = re.findall('[a-z\-0-9\s]+full-time', duration)
        dura = set(dura)
        dura = ''.join(dura).replace('full-time', '').strip()
        dura_per = re.findall('[a-zA-Z]+', dura)
        duration_per = change_durntion_per(dura_per)
        duration = re.findall('\d+', dura)
        duration = list(map(float,duration))
        duration = min(duration)
        if duration_per == None:
            duration = 1
            duration_per = 1
        item['duration'] = duration
        item['duration_per'] = duration_per
        # print(item['duration_per'])
        # print(item['duration'])

        howtoapply = ['<div>Transcript',
                      'An academic transcript for each previous degree you have completed',
                      'We can accept a scanned copy of your transcript if applying online, however you must bring the original with you when you register. If your transcript is not in English you will also need to provide a verified English translation.',
                      'Reference 1'
                      'An academic reference from the academic institution you most recently attended',
                      'It is the applicant’s responsibility to ensure that references are supplied. These should normally be on headed paper and signed by the referee.',
                      'Reference 2',
                      'A second academic reference or a reference from your current or most recent employer',
                      'If required, see above.',
                      'Sponsorship details',
                      'A copy of paperwork confirming the award of sponsorship',
                      'Only applies to those in receipt of sponsorship or other grant. Examples might include a letter from a Government agency or an employer.',
                      'English language qualification',
                      'Any relevant certificates for language qualifications (e.g. IELTS, GCSE)',
                      'You can find the English requirement for your course on the "Entry Criteria" tab of the course pages. Read which English language qualifications Brunel accepts.',
                      'Passport ',
                      'A copy of your passport ',
                      'Only applies to applicants from outside the EU. We need a copy of the details page of your passport, (including personal information, date and place of issue)',
                      'Personal statement',
                      'A brief personal statement in support of your application',
                      'Typically this will be a brief explanation of why you want to pursue a degree at Brunel University London. It can be uploaded as an attachment if you already have an electronic copy or it can be typed directly into the online form later in your application.',
                      'Certificates',
                      'Any relevant certificates',
                      'This includes any certificates you consider relevant to your application (not already submitted under transcripts or language qualifications).',
                      'Other documents',
                      'Any other relevant documentation',
                      'This includes any additional information which you consider relevant to your application, for example a Curriculum Vitae if required for your course.</div>', ]
        howtoapply = '\n'.join(howtoapply)
        item['apply_documents_en'] = howtoapply

        ucas_code = response.xpath('//h6[contains(text(),"UCAS code")]/following-sibling::p[1]//text()').extract()
        ucas_code = set(ucas_code)
        # print(ucas_code)
        ucas_code = ''.join(ucas_code).replace(',', ' ').strip()
        # print(ucas_code)
        ucas = re.findall('[A-Z0-9]{4}', ucas_code)
        if ucas!=[]:
            for u in ucas:
                item['ucascode']=u
                # print(u)
                yield item
        else:
            item['ucascode']=ucas_code
            yield item