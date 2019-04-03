# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
from scrapySchool_England_U.middlewares import *

class QueenmargaretuniversityUSpider(scrapy.Spider):
    name = 'QueenMargaretUniversity_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.qmu.ac.uk/study-here/course-a-z/?tab=undergraduate']
    def parse(self, response):
        url=['https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/bsc-hons-physiotherapy/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/bsc-hons-speech-and-language-therapy/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/bsc-hons-dietetics/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/bscbsc-hons-human-biology/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/bscbsc-hons-nutrition/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/bscbsc-hons-nutrition-and-food-science/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/bscbsc-hons-physical-activity-health-and-wellbeing/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/bscbsc-hons-applied-pharmacology/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/baba-hons-drama/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/baba-hons-theatre-and-film/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/baba-hons-drama/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/ba-hons-education-studies-primary/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/bscbsc-hons-psychology/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/baba-hons-public-relations-and-media-to-be-renamed-ba-ba-hons-media-and-communications/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/baba-hons-events-management/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/ba-ba-hons-media-and-communications/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/baba-hons-film-and-media/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/bsc-hons-nursing/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/bsc-hons-occupational-therapy/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/baba-hons-international-hospitality-and-tourism-management/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/baba-hons-public-relations-marketing-and-events-to-be-renamed-ba-ba-hons-public-relations-and-marketing-communications/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/baba-hons-business-management/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/baba-hons-business-management-with-enterprise/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/baba-hons-business-management-with-finance/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/baba-hons-business-management-with-marketing/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/bsc-hons-podiatry/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/bsc-hons-diagnostic-radiography/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/bsc-hons-therapeutic-radiography/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/ba-hons-education-studies/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/bscbsc-hons-psychology-and-sociology/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/bscbsc-hons-public-sociology/',
'https://www.qmu.ac.uk/study-here/undergraduate-study/2019-undergraduate-courses-folder/baba-hons-costume-design-and-construction/',]
        url=set(url)
        for u in url:
            yield scrapy.Request(url=u,callback=self.parsesss,meta={'url':u})
    #补抓
    def parsesss(self, response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'Queen Margaret University'
        item['url'] = response.meta['url']
        alevel1=response.xpath('//strong[contains(text(),"A Level")]/..//text()|//strong[contains(text(),"A level")]/..//text()').extract()
        alevel2=response.xpath('//strong[contains(text(),"Required subjects")]/..//text()').extract()
        alevel=''.join(alevel1)+'\n'+''.join(alevel2)
        item['alevel']=remove_class(alevel).strip()
        ib=response.xpath('//strong[contains(text(),"International Baccalaureate")]/../text()').extract()
        item['ib']=remove_class(ib)
        yield item

    def parsess(self, response):
        print(response.url)
        pro_url=response.xpath('//div[@id="Tab1"]//div[@data-id="letter-all"]//a/@href').extract()
        for i in pro_url:
            yield scrapy.Request('https://www.qmu.ac.uk'+i,callback=self.parses)
    def parses(self, response):
        # pro_url=response.xpath('//div[@id="Tab1"]//a/@href').extract()
        print(response.url)
        item = get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'Queen Margaret University'
        item['url'] = response.url
        item['location'] = 'Musselburgh'
        programme = response.xpath('//h1/text()').extract()
        programme = ''.join(programme)
        degree_name = re.findall('[A-Z]{2,}[a-z]*', programme)
        degree_name = re.findall('.+\(Hons\)', programme)
        degree_name = set(degree_name)
        degree_name = '/'.join(degree_name)
        # print(programme)
        # print(degree_name)
        programme = programme.replace(degree_name, '').strip()
        # print(programme)
        # if degree_name=='':
        #     print(programme)
        item['programme_en'] = programme
        item['degree_name'] = degree_name

        item['tuition_fee'] = '11500'
        item['tuition_fee_pre'] = '£'

        duration = response.xpath('//div[contains(text(),"Dura")]/following-sibling::div/text()').extract()
        duration = clear_duration(duration)
        # print(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']

        start_date = response.xpath('//div[contains(text(),"Start")]/following-sibling::div/text()').extract()
        start_date = tracslateDate(start_date)
        start_date = ','.join(start_date)
        # print(start_date)
        item['start_date'] = start_date

        department = response.xpath('//div[contains(text(),"School")]/following-sibling::div/text()').extract()
        department = ''.join(department).strip()
        # print(department)
        item['department'] = department

        overview = response.xpath(
            '//div[@class="accordion-item"]/h3[contains(text(),"Course Overview")]/following-sibling::div').extract()
        overview = remove_class(overview)
        item['overview_en'] = overview
        # print(overview)

        modules = response.xpath('//h3[contains(text(),"Modules")]/following-sibling::div').extract()
        modules = remove_class(modules)
        # print(modules)
        item['modules_en'] = modules

        career = response.xpath('//h3[contains(text(),"Career")]/following-sibling::div').extract()
        career = remove_class(career)
        item['career_en'] = career

        rntry = response.xpath('//h3[contains(text(),"ntry")]/following-sibling::div').extract()
        rntry = remove_class(rntry)
        item['require_chinese_en'] = rntry

        ielts = response.xpath('//*[contains(text(),"IELTS")]/text()').extract()
        # print(ielts)
        item['ielts_desc'] = ''.join(ielts)
        ielts = get_ielts(ielts)
        try:
            if ielts != [] or ielts != {}:
                item['ielts_l'] = ielts['IELTS_L']
                item['ielts_s'] = ielts['IELTS_S']
                item['ielts_r'] = ielts['IELTS_R']
                item['ielts_w'] = ielts['IELTS_W']
                item['ielts'] = ielts['IELTS']
        except:
            pass

        deadline = response.xpath(
            '//h3[contains(text(),"Application Deadline")]/following-sibling::div//text()').extract()
        deadline = tracslateDate(deadline)
        deadline = ','.join(deadline)
        item['deadline'] = deadline

        apply_documents_en = ["·A copy of your degree certificate",
                              "·A copy of your academic transcripts",
                              "·Two letters of reference (one of which must be academic) and both signed, dated and written on letter headed paper or sent directly from a professional email account.",
                              "If your documents are in any language other than English then they will need to be accompanied by a formal certified translation into English, by either the awarding institution or a sworn translator.", ]
        apply_documents_en = '\n'.join(apply_documents_en)
        # item['apply_documents_en'] = apply_documents_en

        apply_proces_en = ["Applying online",
                           "You will find all our degree programmes listed on our course information pages. To apply for your chosen programme, click on the “Apply for this Course” button which appears top right on each course page.",
                           "Each programme will list the entry requirements, available awards, study modes and available start dates.",
                           "Select your programme and preferred start date and begin your application.",
                           "Application form",
                           "On our application form please input your basic details. Be careful spelling your email address as this is how we will contact you about your application in future.",
                           "As part of your application on the form, you will need to write a personal statement specific to the course that you are applying. This is your chance to sell yourself through highlighting your experience, suitability and motivators for wanting to join this course at QMU.",
                           "You will have the chance to upload supporting documents as part of your application. This is an important part of the admissions process and without seeing supporting documents, tutors will not have enough information to make a decision on your application.",
                           "The form allows you to save your application should you wish to complete it later.",
                           "Once complete you can submit your application to us and you will receive an automatic acknowledgement email confirming receipt of your application. You will also receive a QMU applicant ID number which you should keep a note of and quote in any correspondence to QMU.", ]
        apply_proces_en = '\n'.join(apply_proces_en)
        # item['apply_proces_en'] = apply_proces_en

        ucascode = response.xpath('//div[contains(text(),"UCAS")]/following-sibling::div/text()').extract()
        ucascode = ''.join(ucascode).strip()
        item['ucascode'] = ucascode

        alevel = response.xpath('//strong[contains(text(),"A Level")]/../text()').extract()
        alevel = ''.join(alevel).strip()
        # print(alevel)
        item['alevel'] = alevel

        ib=response.xpath('//strong[contains(text(),"International B")]/../text()').extract()
        ib=''.join(ib).strip()
        item['ib']=ib

        # print(item)
        yield item