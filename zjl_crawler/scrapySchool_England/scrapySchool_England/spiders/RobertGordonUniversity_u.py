# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/7 14:54'
import scrapy,json
import re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from w3lib.html import remove_tags
from scrapySchool_England.clearSpace import  clear_space_str
from scrapySchool_England.translate_date import  tracslateDate
from scrapySchool_England.translate_date import tracslateDate
from lxml import  etree
import  requests
from scrapySchool_England.TranslateMonth import translate_month
class RobertGordonUniversitySpider(scrapy.Spider):
    name = 'RobertGordonUniversity_u'
    allowed_domains = ['rgu.ac.uk/']
    start_urls = []
    C=[
        'https://www.rgu.ac.uk/study/courses/453-ba-hons-communication-design-graphic-design-illustration-photography',
        'https://www.rgu.ac.uk/study/courses/452-ba-hons-contemporary-art-practice-moving-image-photography-printmaking-sculpture',
        'https://www.rgu.ac.uk/study/courses/975-mrad-diagnostic-radiography',
        'https://www.rgu.ac.uk/study/courses/446-bsc-hons-computer-science',
        'https://www.rgu.ac.uk/study/courses/968-bsc-hons-applied-bioscience',
        'https://www.rgu.ac.uk/study/courses/430-bsc-hons-cyber-security',
        'https://www.rgu.ac.uk/study/courses/1091-bsc-hons-construction-management',
        'https://www.rgu.ac.uk/study/courses/873-bsc-hons-applied-biomedical-science',
        'https://www.rgu.ac.uk/study/courses/431-ba-hons-accounting-and-finance',
        'https://www.rgu.ac.uk/study/courses/977-mdiet-dietetics',
        'https://www.rgu.ac.uk/study/courses/920-ba-hons-applied-social-sciences',
        'https://www.rgu.ac.uk/study/courses/974-bsc-hons-applied-sport-and-exercise-science',
        'https://www.rgu.ac.uk/study/courses/921-bsc-hons-architectural-technology',
        'https://www.rgu.ac.uk/study/courses/850-bsc-master-of-architecture',
        'https://www.rgu.ac.uk/study/courses/900-bachelor-of-midwifery',
        'https://www.rgu.ac.uk/study/courses/872-bsc-hons-biomedical-science',
        'https://www.rgu.ac.uk/study/courses/827-ba-hons-international-hospitality-management',
        'https://www.rgu.ac.uk/study/courses/828-ba-hons-international-tourism-management',
        'https://www.rgu.ac.uk/study/courses/710-ba-hons-journalism',
        'https://www.rgu.ac.uk/study/courses/436-llb-hons-law',
        'https://www.rgu.ac.uk/study/courses/437-ba-hons-law-and-management',
        'https://www.rgu.ac.uk/study/courses/661-ba-hons-management',
        'https://www.rgu.ac.uk/study/courses/668-ba-hons-management-with-human-resource-management',
        'https://www.rgu.ac.uk/study/courses/671-ba-hons-management-with-marketing',
        'https://www.rgu.ac.uk/study/courses/868-beng-mechanical-and-electrical-engineering',
        'https://www.rgu.ac.uk/study/courses/864-meng-mechanical-and-electrical-engineering',
        'https://www.rgu.ac.uk/study/courses/866-beng-mechanical-and-offshore-engineering',
        'https://www.rgu.ac.uk/study/courses/863-meng-mechanical-and-offshore-engineering',
        'https://www.rgu.ac.uk/study/courses/861-beng-mechanical-engineering',
        'https://www.rgu.ac.uk/study/courses/859-meng-mechanical-engineering',
        'https://www.rgu.ac.uk/study/courses/696-ba-hons-media',
        'https://www.rgu.ac.uk/study/courses/914-bn-hons-nursing-adult',
        'https://www.rgu.ac.uk/study/courses/908-bn-nursing-adult',
        'https://www.rgu.ac.uk/study/courses/917-ba-hons-social-work',
        'https://www.rgu.ac.uk/study/courses/925-bsc-hons-surveying',
        'https://www.rgu.ac.uk/study/courses/422-ba-hons-three-dimensional-design',
        'https://www.rgu.ac.uk/study/courses/441-bsc-hons-digital-media',
        'https://www.rgu.ac.uk/study/courses/869-beng-electronic-and-electrical-engineering',
        'https://www.rgu.ac.uk/study/courses/865-meng-electronic-and-electrical-engineering',
        'https://www.rgu.ac.uk/study/courses/823-ba-hons-events-management',
        'https://www.rgu.ac.uk/study/courses/438-ba-hons-fashion-and-textile-design',
        'https://www.rgu.ac.uk/study/courses/714-ba-hons-fashion-management',
        'https://www.rgu.ac.uk/study/courses/871-bsc-hons-food-nutrition-and-human-health',
        'https://www.rgu.ac.uk/study/courses/870-bsc-hons-forensic-and-analytical-science',
        'https://www.rgu.ac.uk/study/courses/664-ba-hons-international-business-management',
        'https://www.rgu.ac.uk/study/courses/907-bn-nursing-children-and-young-people',
        'https://www.rgu.ac.uk/study/courses/904-bn-nursing-mental-health',
        'https://www.rgu.ac.uk/study/courses/980-mo-oth-hons-occupational-therapy',
        'https://www.rgu.ac.uk/study/courses/432-ba-hons-painting',
        'https://www.rgu.ac.uk/study/courses/883-mpharm-pharmacy',
        'https://www.rgu.ac.uk/study/courses/1081-mphys-physiotherapy',
        'https://www.rgu.ac.uk/study/courses/697-ba-hons-public-relations'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Robert Gordon University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="flexicontent"]/article//h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 1

        #5.degree_name
        degree_name = response.xpath('//*[@id="flexicontent"]/article/div[1]//p').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        if '(Hons)' in degree_name:
            degree_name = degree_name.replace('(Hons)','').strip()
        # print(degree_name)

        #6.department
        department = response.xpath('//*[@id="flexicontent"]/article/div[2]//h3/a').extract()
        department = ''.join(department)
        department = remove_tags(department).replace('&amp;','')
        # print(department)

        #7.apply_proces_en
        apply_proces_en = 'https://www.rgu.ac.uk/study/apply/undergraduate-applicants'

        #8.overview_en
        overview_en = response.xpath("//div[@class='study-options-banner-text']/../../../preceding-sibling::*").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #9.ucascode
        ucascode = response.xpath('//*[@id="apply_container"]/div/div/p').extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode).replace('UCAS Code: ','').strip()
        # print(ucascode)

        #10.start_date
        start_date = response.xpath('//*[@id="study-options-lists"]/div[2]/div[3]/text()').extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        start_date =translate_month(start_date)
        # print(start_date)

        #11.duration
        # try:
        #     ab = response.xpath("//div[@class='kis-widget']//@data-institution").extract()[0]
        # except:
        #     ab = ''
        # try:
        #     cd = response.xpath("//div[@class='kis-widget']//@data-course").extract()[0]
        # except:
        #     cd = ''
        # if len(ab)!= 0:
        #     duration_url = 'https://widget.unistats.ac.uk/Widget/'+str(ab)+'/'+str(cd)+'/small/en-GB/Full Time'
        # else:duration_url= ''
        # # print(duration_url)
        # if len(duration_url)!=0:
        #     headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        #     data = requests.get(duration_url, headers=headers)
        #     response_duration = etree.HTML(data.text)
        #     duration = response_duration.xpath('//*[@id="kisWidget"]/div[2]/p[1]//text()')
        #     duration = ''.join(duration)
        #     duration =remove_tags(duration)
        #     try:
        #         duration = re.findall(r'\d',duration)[0]
        #     except:
        #         duration = ''
        # else:
        #     duration = ''
        # print(duration)

        #12.ib
        ib = response.xpath("//*[contains(text(),'IB Diploma:')]//..").extract()
        ib = ''.join(ib)
        ib = remove_tags(ib)
        ib = ib.replace('IB Diploma:','').strip()
        # print(ib)

        #25.alevel
        try:
            alevel = response.xpath("//*[contains(text(),'GCE A Level')]//..").extract()[0]
            alevel = ''.join(alevel)
            alevel = remove_tags(alevel)
        except:
            alevel = 'N/A'
        # print(alevel)



        #13.modules_en
        try:
            modulesurl = response.xpath('//*[@id="tab-1"]/a/@href').extract()[0]
        except:
            modulesurl = ''
        if len(modulesurl)!=0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data = requests.get(modulesurl, headers=headers)
            response1 = etree.HTML(data.text)
            modules_en =  response1.xpath('//*[@id="content"]//table')
            doc = ""
            if len(modules_en) > 0:
                for a in modules_en:
                    doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc = remove_class(doc)
                    modules_en = doc

        #14.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'Assessment')]//following-sibling::*").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #15.career_en
        career_en = response.xpath("//*[contains(text(),'Job Prospects')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en= remove_class(career_en)
        # print(career_en)

        #16.apply_desc_en
        apply_desc_en = response.xpath('//*[@id="tab-4"]/div/div[1]/div').extract()
        apply_desc_en = ''.join(apply_desc_en)
        apply_desc_en = remove_class(apply_desc_en)
        # print(apply_desc_en)

        #17.ielts 18,19,20,21
        ielts_list = response.xpath("//*[contains(text(),'English Language Requirements')]//following-sibling::*").extract()
        ielts_list = ''.join(ielts_list)
        ielts_list = remove_tags(ielts_list)
        try:
            ielts = re.findall('\d\.\d',ielts_list)
        except:
            ielts = ''
        if len(ielts) ==2:
            a=ielts[0]
            b= ielts[1]
            ielts = a
            ielts_r =b
            ielts_w =b
            ielts_s =b
            ielts_l =b
        else:
            ielts = 6.5
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
        # print(ielts,ielts_r,ielts_l,ielts_s,ielts_w)

        #21.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'International Students')]/../following-sibling::*|//*[contains(text(),'International Students')]//following-sibling::*|//*[contains(text(),'Students')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(response.url)
        # print(tuition_fee)

        #22.tuition_fee_pre
        tuition_fee_pre = '£'

        #23.apply_documents_en
        apply_documents_en = '<p>Before you begin, make sure you know the name of the course you are applying for and have copies of all relevant documents to hand. Certificates and/or transcripts for qualifications you have completed Curriculum Vitae (CV)/Resumé Any letter of reference you may have Copy of the details page of your passport (non-EU applicants applying for full time study)</p>'
        #24.apply_pre
        apply_pre = '£'


        item['apply_documents_en'] = apply_documents_en
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['department'] = department
        item['apply_proces_en'] = apply_proces_en
        item['overview_en'] = overview_en
        item['ucascode'] = ucascode
        item['start_date'] = start_date
        # item['duration'] = duration
        item['ib'] = ib
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['apply_desc_en'] = apply_desc_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['alevel'] = alevel
        yield  item

    def parse_getmodules(self,modulesurl):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        data = requests.get(headers=headers,url = modulesurl)
        response = etree.HTML(data.text)
        datadict ={}
        modules_en = response.xpath('//*[@id="content"]//a/text()')
        modules_en = '\n'.join(modules_en)
        # print(modules_en)
        datadict['modules_en'] = modules_en
        return datadict