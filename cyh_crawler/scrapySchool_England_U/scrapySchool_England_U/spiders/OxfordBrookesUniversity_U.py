# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem

class OxfordbrookesuniversityUSpider(scrapy.Spider):
    name = 'OxfordBrookesUniversity_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.brookes.ac.uk/templates/pages/coursefinder.aspx?q=&searchtype=undergraduate&requiredfields=contenttype:course&partialfields=&start=0']
    def parse(self, response):
        url=['https://www.brookes.ac.uk/courses/undergraduate/human-biology/',
'https://www.brookes.ac.uk/courses/undergraduate/illustration/',
'https://www.brookes.ac.uk/courses/undergraduate/graphic-design/',
'https://www.brookes.ac.uk/courses/undergraduate/architecture/',
'https://www.brookes.ac.uk/courses/undergraduate/physiotherapy/',
'https://www.brookes.ac.uk/courses/undergraduate/interior-architecture/',
'https://www.brookes.ac.uk/courses/undergraduate/real-estate-management/',
'https://www.brookes.ac.uk/courses/undergraduate/mbiol-biology/',
'https://www.brookes.ac.uk/courses/undergraduate/events-management/',
'https://www.brookes.ac.uk/courses/undergraduate/economics/',
'https://www.brookes.ac.uk/courses/undergraduate/automotive-engineering/',
'https://www.brookes.ac.uk/courses/undergraduate/automotive-engineering/',
'https://www.brookes.ac.uk/courses/undergraduate/motorsport-engineering-beng-or-meng/',
'https://www.brookes.ac.uk/courses/undergraduate/motorsport-engineering-beng-or-meng/',
'https://www.brookes.ac.uk/courses/undergraduate/mechanical-engineering-beng-or-meng/',
'https://www.brookes.ac.uk/courses/undergraduate/mechanical-engineering-beng-or-meng/',
'https://www.brookes.ac.uk/courses/undergraduate/english-literature-with-creative-writing/',
'https://www.brookes.ac.uk/courses/undergraduate/english-literature/',
'https://www.brookes.ac.uk/courses/undergraduate/english-literature/',
'https://www.brookes.ac.uk/courses/undergraduate/english-literature/',
'https://www.brookes.ac.uk/courses/undergraduate/english-literature/',
'https://www.brookes.ac.uk/courses/undergraduate/english-literature/',
'https://www.brookes.ac.uk/courses/undergraduate/english-literature/',
'https://www.brookes.ac.uk/courses/undergraduate/english-literature/',
'https://www.brookes.ac.uk/courses/undergraduate/english-literature/',
'https://www.brookes.ac.uk/courses/undergraduate/english-literature/',
'https://www.brookes.ac.uk/courses/undergraduate/english-literature/',
'https://www.brookes.ac.uk/courses/undergraduate/english-literature/',
'https://www.brookes.ac.uk/courses/undergraduate/publishing-media/',
'https://www.brookes.ac.uk/courses/undergraduate/marketing-management/',
'https://www.brookes.ac.uk/courses/undergraduate/ba-hons-marketing-and-events-management/',
'https://www.brookes.ac.uk/courses/undergraduate/ba-hons-marketing-communications-management/',
'https://www.brookes.ac.uk/courses/undergraduate/business-and-marketing-management/',
'https://www.brookes.ac.uk/courses/undergraduate/psychology/',
'https://www.brookes.ac.uk/courses/undergraduate/japanese-studies/',
'https://www.brookes.ac.uk/courses/undergraduate/japanese-studies/',
'https://www.brookes.ac.uk/courses/undergraduate/japanese-studies/',
'https://www.brookes.ac.uk/courses/undergraduate/japanese-studies/',
'https://www.brookes.ac.uk/courses/undergraduate/japanese-studies/',
'https://www.brookes.ac.uk/courses/undergraduate/japanese-studies/',
'https://www.brookes.ac.uk/courses/undergraduate/childrens-nursing/',
'https://www.brookes.ac.uk/courses/undergraduate/law/',
'https://www.brookes.ac.uk/courses/undergraduate/history/',
'https://www.brookes.ac.uk/courses/undergraduate/history/',
'https://www.brookes.ac.uk/courses/undergraduate/history/',
'https://www.brookes.ac.uk/courses/undergraduate/history/',
'https://www.brookes.ac.uk/courses/undergraduate/history/',
'https://www.brookes.ac.uk/courses/undergraduate/history/',
'https://www.brookes.ac.uk/courses/undergraduate/history/',
'https://www.brookes.ac.uk/courses/undergraduate/history/',
'https://www.brookes.ac.uk/courses/undergraduate/history/',
'https://www.brookes.ac.uk/courses/undergraduate/international-business-management/',
'https://www.brookes.ac.uk/courses/undergraduate/social-anthropology/',
'https://www.brookes.ac.uk/courses/undergraduate/business-enterprise-and-entrepreneurship/',
'https://www.brookes.ac.uk/courses/undergraduate/business-and-management/',
'https://www.brookes.ac.uk/courses/undergraduate/anthropology/',
'https://www.brookes.ac.uk/courses/undergraduate/anthropology/',
'https://www.brookes.ac.uk/courses/undergraduate/anthropology/',
'https://www.brookes.ac.uk/courses/undergraduate/anthropology/',
'https://www.brookes.ac.uk/courses/undergraduate/anthropology/',
'https://www.brookes.ac.uk/courses/undergraduate/anthropology/',
'https://www.brookes.ac.uk/courses/undergraduate/anthropology/',
'https://www.brookes.ac.uk/courses/undergraduate/anthropology/',
'https://www.brookes.ac.uk/courses/undergraduate/anthropology/',
'https://www.brookes.ac.uk/courses/undergraduate/biological-anthropology/',
'https://www.brookes.ac.uk/courses/undergraduate/human-resource-management/',
'https://www.brookes.ac.uk/courses/undergraduate/biological-sciences/',
'https://www.brookes.ac.uk/courses/undergraduate/accounting-and-finance/',
'https://www.brookes.ac.uk/courses/undergraduate/business-management/',
'https://www.brookes.ac.uk/courses/undergraduate/business-management/',
'https://www.brookes.ac.uk/courses/undergraduate/business-management/',
'https://www.brookes.ac.uk/courses/undergraduate/computing-for-robotic-systems/',
'https://www.brookes.ac.uk/courses/undergraduate/accounting-and-economics/',
'https://www.brookes.ac.uk/courses/undergraduate/international-hospitality-management/',
'https://www.brookes.ac.uk/courses/undergraduate/education-studies/',
'https://www.brookes.ac.uk/courses/undergraduate/education-studies/',
'https://www.brookes.ac.uk/courses/undergraduate/education-studies/',
'https://www.brookes.ac.uk/courses/undergraduate/education-studies/',
'https://www.brookes.ac.uk/courses/undergraduate/education-studies/',
'https://www.brookes.ac.uk/courses/undergraduate/urban-design-planning-and-development/',
'https://www.brookes.ac.uk/courses/undergraduate/international-relations-and-politics/',
'https://www.brookes.ac.uk/courses/undergraduate/international-relations/',
'https://www.brookes.ac.uk/courses/undergraduate/international-relations/',
'https://www.brookes.ac.uk/courses/undergraduate/international-relations/',
'https://www.brookes.ac.uk/courses/undergraduate/international-relations/',
'https://www.brookes.ac.uk/courses/undergraduate/international-relations/',
'https://www.brookes.ac.uk/courses/undergraduate/international-relations/',
'https://www.brookes.ac.uk/courses/undergraduate/international-relations/',
'https://www.brookes.ac.uk/courses/undergraduate/international-relations/',
'https://www.brookes.ac.uk/courses/undergraduate/international-relations/',
'https://www.brookes.ac.uk/courses/undergraduate/education-studies-sen-disabilities-and-inclusion/',
'https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture/',
'https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture/',
'https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture/',
'https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture/',
'https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture/',
'https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture/',
'https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture/',
'https://www.brookes.ac.uk/courses/undergraduate/communication-media-and-culture/',
'https://www.brookes.ac.uk/courses/undergraduate/early-childhood-studies/',
'https://www.brookes.ac.uk/courses/undergraduate/primary-teacher-education-campus-based/',
'https://www.brookes.ac.uk/courses/undergraduate/history-of-art/',
'https://www.brookes.ac.uk/courses/undergraduate/history-of-art/',
'https://www.brookes.ac.uk/courses/undergraduate/history-of-art/',
'https://www.brookes.ac.uk/courses/undergraduate/history-of-art/',
'https://www.brookes.ac.uk/courses/undergraduate/history-of-art/',
'https://www.brookes.ac.uk/courses/undergraduate/criminology/',
'https://www.brookes.ac.uk/courses/undergraduate/criminology/',
'https://www.brookes.ac.uk/courses/undergraduate/criminology/',
'https://www.brookes.ac.uk/courses/undergraduate/criminology/',
'https://www.brookes.ac.uk/courses/undergraduate/criminology/',
'https://www.brookes.ac.uk/courses/undergraduate/criminology/',
'https://www.brookes.ac.uk/courses/undergraduate/criminology/',
'https://www.brookes.ac.uk/courses/undergraduate/economics-finance-and-international-business/',
'https://www.brookes.ac.uk/courses/undergraduate/politics/',
'https://www.brookes.ac.uk/courses/undergraduate/politics/',
'https://www.brookes.ac.uk/courses/undergraduate/politics/',
'https://www.brookes.ac.uk/courses/undergraduate/politics/',
'https://www.brookes.ac.uk/courses/undergraduate/politics/',
'https://www.brookes.ac.uk/courses/undergraduate/bsc-hons-business-and-finance/',
'https://www.brookes.ac.uk/courses/undergraduate/philosophy/',
'https://www.brookes.ac.uk/courses/undergraduate/philosophy/',
'https://www.brookes.ac.uk/courses/undergraduate/philosophy/',
'https://www.brookes.ac.uk/courses/undergraduate/philosophy/',
'https://www.brookes.ac.uk/courses/undergraduate/philosophy/',
'https://www.brookes.ac.uk/courses/undergraduate/planning-and-property-development/',
'https://www.brookes.ac.uk/courses/undergraduate/film/',
'https://www.brookes.ac.uk/courses/undergraduate/film/',
'https://www.brookes.ac.uk/courses/undergraduate/film/',
'https://www.brookes.ac.uk/courses/undergraduate/film/',
'https://www.brookes.ac.uk/courses/undergraduate/english-language-and-communication/',
'https://www.brookes.ac.uk/courses/undergraduate/english-language-and-communication/',
'https://www.brookes.ac.uk/courses/undergraduate/english-language-and-communication/',
'https://www.brookes.ac.uk/courses/undergraduate/english-language-and-communication/',
'https://www.brookes.ac.uk/courses/undergraduate/economics-politics-and-international-relations/',
'https://www.brookes.ac.uk/courses/undergraduate/sociology/',
'https://www.brookes.ac.uk/courses/undergraduate/sociology/',
'https://www.brookes.ac.uk/courses/undergraduate/sociology/',
'https://www.brookes.ac.uk/courses/undergraduate/sociology/',
'https://www.brookes.ac.uk/courses/undergraduate/sociology/',
'https://www.brookes.ac.uk/courses/undergraduate/sociology/',
'https://www.brookes.ac.uk/courses/undergraduate/sociology/',
'https://www.brookes.ac.uk/courses/undergraduate/sociology/',
'https://www.brookes.ac.uk/courses/undergraduate/social-work/',
'https://www.brookes.ac.uk/courses/undergraduate/drama/',
'https://www.brookes.ac.uk/courses/undergraduate/drama/',
'https://www.brookes.ac.uk/courses/undergraduate/sport-coaching-and-physical-education/',
'https://www.brookes.ac.uk/courses/undergraduate/occupational-therapy/',
'https://www.brookes.ac.uk/courses/undergraduate/geography/',
'https://www.brookes.ac.uk/courses/undergraduate/geography/',
'https://www.brookes.ac.uk/courses/undergraduate/geography/',
'https://www.brookes.ac.uk/courses/undergraduate/geography/',
'https://www.brookes.ac.uk/courses/undergraduate/mental-health-nursing/',
'https://www.brookes.ac.uk/courses/undergraduate/fine-art/',
'https://www.brookes.ac.uk/courses/undergraduate/computer-science/',
'https://www.brookes.ac.uk/courses/undergraduate/computer-science-for-cyber-security/',
'https://www.brookes.ac.uk/courses/undergraduate/information-technology-management-for-business/',
'https://www.brookes.ac.uk/courses/undergraduate/digital-media-production/',
'https://www.brookes.ac.uk/courses/undergraduate/nutrition/',
'https://www.brookes.ac.uk/courses/undergraduate/sport-and-exercise-science/',
'https://www.brookes.ac.uk/courses/undergraduate/biomedical-science/',
'https://www.brookes.ac.uk/courses/undergraduate/quantity-surveying-and-commercial-management/',
'https://www.brookes.ac.uk/courses/undergraduate/construction-project-management/',
'https://www.brookes.ac.uk/courses/undergraduate/animal-biology-and-conservation/',
'https://www.brookes.ac.uk/courses/undergraduate/motorsport-technology/',
'https://www.brookes.ac.uk/courses/undergraduate/mechanical-engineering-bsc/',
'https://www.brookes.ac.uk/courses/undergraduate/msci-adult-and-mental-health-nursing/',
'https://www.brookes.ac.uk/courses/undergraduate/msci-nursing-mental-health-and-child/',
'https://www.brookes.ac.uk/courses/undergraduate/adult-nursing/',
'https://www.brookes.ac.uk/courses/undergraduate/adult-nursing/',
'https://www.brookes.ac.uk/courses/undergraduate/biology/',
'https://www.brookes.ac.uk/courses/undergraduate/equine-science-and-thoroughbred-management/',
'https://www.brookes.ac.uk/courses/undergraduate/medical-science/',
'https://www.brookes.ac.uk/courses/undergraduate/environmental-sciences/',
'https://www.brookes.ac.uk/courses/undergraduate/equine-science/',
'https://www.brookes.ac.uk/courses/undergraduate/applied-languages/',
'https://www.brookes.ac.uk/courses/undergraduate/creative-music-production/',
'https://www.brookes.ac.uk/courses/undergraduate/music/',]
        url=set(url)
        for u in url:
            yield scrapy.Request(url=u,callback=self.parsesss,meta={'url':u})
    #补抓
    def parsesss(self, response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'Oxford Brookes University'
        item['url'] = response.meta['url']
        alevel1=response.xpath('//strong[contains(text(),"UCAS Tariff points")]/..//text()').extract()
        alevel2=response.xpath('//strong[contains(text(),"A-Level:")]/..//text()').extract()
        item['alevel']=remove_class(''.join(alevel1)+'\n'+''.join(alevel2))

        yield item
    def parsess(self, response):
        proURL = response.xpath('//h2[contains(text(),"earch r")]/following-sibling::ul/h3//a/@href').extract()
        next_page = response.xpath('//a[contains(text(),"Next")]/@href').extract()
        if next_page != []:
            full_url = 'https://www.brookes.ac.uk' + next_page[0]
            yield scrapy.Request(url=full_url, callback=self.parse)
        for i in proURL:
            yield scrapy.Request(url=i, callback=self.parses)
    def parses(self, response):
        # print(response.url)
        item = get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'Oxford Brookes University'
        item['url'] = response.url
        item['location'] = 'London'
        programme = response.xpath('//h1/text()').extract()
        programme = ''.join(programme).strip()
        # print(programme)
        item['programme_en'] = programme
        degree_name = response.xpath('//h1/following-sibling::h2/text()').extract()
        degree_name = ''.join(degree_name).strip()
        # print(degree_name)
        item['degree_name'] = degree_name
        department = response.xpath('//h1/following-sibling::h2/following-sibling::p/a/text()').extract()
        department = ''.join(department).strip()
        # print(department)
        item['department'] = department
        start_date = response.xpath('//h3[contains(text(),"Available")]/following-sibling::p[1]/text()').extract()
        start_date = tracslateDate(start_date)
        start_date = ','.join(start_date)
        # print(start_date)
        item['start_date'] = start_date
        overview = response.xpath('//h1/following-sibling::h2/following-sibling::p/following-sibling::*').extract()
        overview = remove_class(overview)
        item['overview_en'] = overview
        modules = response.xpath('//div[@id="section-two"]').extract()
        modules = remove_class(modules)
        item['modules_en'] = modules
        fee = response.xpath('//p[contains(text(),"£")]/text()').extract()
        tuition_fee = getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = '£'
        rntry = response.xpath('//div[@id="section-four"]').extract()
        rntry = remove_class(rntry)
        item['rntry_requirements'] = rntry
        career = response.xpath('//div[@id="section-five"]').extract()
        career = remove_class(career)
        item['career_en'] = career
        ielts = response.xpath('//p[contains(text(),"IELTS")]/text()').extract()
        ielts = ''.join(ielts)
        item['ielts_desc'] = ielts
        ielts = get_ielts(ielts)
        if ielts != {} and ielts != []:
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            item['ielts'] = ielts['IELTS']

        ielts1='6.5 overall with 6.0 in reading and writing, 5.5 in listening and speaking'
        ielts3='6.0 overall with 6.0 in reading and writing, 5.5 in listening and speaking'
        if item['ielts_desc']=='':
            if 'Law' in programme or 'Psychology' in programme or 'Architecture' in programme or 'Interior' in programme or 'English' in programme or 'Writing' in programme or 'Creative' in programme :
                item['ielts_desc'],item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']=ielts1,'6.5','5.5','5.5','6.0','6.0'
                print('ielts1')
            else:
                print('ielts3')
                item['ielts_desc'], item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w'] = ielts3, '6.5', '5.5', '5.5', '6.0', '6.0'

        ucascode=response.xpath('//div[@id="factspanel"]/text()').extract()
        ucascode=''.join(ucascode).strip()
        # print(ucascode)
        item['ucascode']=ucascode
        alevel=response.xpath('//strong[contains(text(),"A-Level:")]/../text()').extract()
        item['alevel']=remove_class(alevel)
        ib=response.xpath('//strong[contains(text(),"IB")]/../text()').extract()
        item['ib']=remove_class(ib)
        assessment=response.xpath('//h2[contains(text(),"ssessment")]/following-sibling::*').extract()
        if assessment==[]:
            print(response.url)
        else:
            print('Assessment不为空')
        item['assessment_en']=remove_class(assessment)
        duration=response.xpath('//h2[contains(text(),"Course length")]/following-sibling::ul//text()').extract()
        # print(duration)
        for i in duration:
            if 'Part' in i:
                del duration[duration.index(i)]
        dura=clear_duration(duration)
        item['duration_per']=dura['duration_per']
        lengs=re.findall('\d+',''.join(duration))
        # print(lengs)
        lengs=list(set(lengs))
        if len(lengs)>1:
            item['duration']=duration[0].replace('Full time:','').strip()
        else:
            item['duration']=dura['duration']
        # print(item['duration'])
        chi=['<h4>Entry into the first year</h4><ul><li>Applicants with a Senior Secondary High School Graduation Certificate and at least one year at a university in China or elsewhere will be considered</li><li>British A-levels, from BCC</li><li>Oxford Brookes foundation course</li><li>International Baccalaureate, from 29 points</li></ul><h4>Entry into the 2nd or final year</h4><ul><li>SQA HND - You may be able to',
'                <a draggable="false" title="transfer this to one of our undergraduate courses" href="https://www.brookes.ac.uk/international/applying-to-arriving/how-to-apply/credit-transfer/">transfer this to one of our undergraduate courses</a></li></ul></td><td style="cursor: default;"><ul><li>IELTS 6.0-7.0, with 6.0 in reading and writing, and 5.5 in listening and speaking</li><li>Pre-sessional University English</li><li>Some alternative qualifications</li>',]
        item['require_chinese_en']=remove_class(chi)
        comb=response.xpath('//a[contains(text(),"Combining this course with another subject")]/text()').extract()
        if comb!=[]:
            prog=response.xpath('//a[contains(text(),"Combining this course with another subject")]/../../following-sibling::div//p/a/strong/text()').extract()
            ucas=response.xpath('//a[contains(text(),"Combining this course with another subject")]/../../following-sibling::div//p/a[contains(text(),"See the")]/../text()').extract()
            for pro,uca in zip(prog,ucas):
                item['programme_en']=programme+' and '+pro
                item['ucascode']=uca
                yield item
        else:
            yield item
