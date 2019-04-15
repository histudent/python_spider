# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/5 9:15'
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
from scrapySchool_England.TranslateMonth import translate_month
from translate import translate
import requests
from lxml import etree
from bs4 import  BeautifulSoup
class KinstonUniversitySpider(scrapy.Spider):
    name = 'KinstonUniversity_p'
    allowed_domains = ['kingston.ac.uk/']
    start_urls = []
    C = ['https://www.kingston.ac.uk/postgraduate-course/forensic-psychology-msc/',
'https://www.kingston.ac.uk/postgraduate-course/environmental-management-msc/',
'https://www.kingston.ac.uk/postgraduate-course/sport-and-exercise-science-msc/',
'https://www.kingston.ac.uk/postgraduate-course/landscape-urbanism-ma/',
'https://www.kingston.ac.uk/postgraduate-course/landscape-architecture-mla/',
'https://www.kingston.ac.uk/postgraduate-course/fashion-ma/',
'https://www.kingston.ac.uk/postgraduate-course/communication-design-illustration-ma/',
'https://www.kingston.ac.uk/postgraduate-course/communication-design-graphic-design-ma/',
'https://www.kingston.ac.uk/postgraduate-course/art-market-appraisal-ma/',
'https://www.kingston.ac.uk/postgraduate-course/art-space-ma/',
'https://www.kingston.ac.uk/postgraduate-course/art-design-history-ma/',
'https://www.kingston.ac.uk/postgraduate-course/curating-contemporary-design-ma/',
'https://www.kingston.ac.uk/postgraduate-course/product-furniture-design-ma/',
'https://www.kingston.ac.uk/postgraduate-course/fine-art-mfa/',
'https://www.kingston.ac.uk/postgraduate-course/experimental-film-ma/',
'https://www.kingston.ac.uk/postgraduate-course/political-economy-ma/',
'https://www.kingston.ac.uk/postgraduate-course/international-conflict-msc/',
'https://www.kingston.ac.uk/postgraduate-course/international-relations-msc/',
'https://www.kingston.ac.uk/postgraduate-course/financial-economics-ma/',
'https://www.kingston.ac.uk/postgraduate-course/terrorism-and-political-violence-msc/',
'https://www.kingston.ac.uk/postgraduate-course/human-rights-ma/',
'https://www.kingston.ac.uk/postgraduate-course/literature-and-philosophy-ma/',
'https://www.kingston.ac.uk/postgraduate-course/gender-without-borders-ma/',
'https://www.kingston.ac.uk/postgraduate-course/international-human-resource-management-msc/',
'https://www.kingston.ac.uk/postgraduate-course/business-management-mres/',
'https://www.kingston.ac.uk/postgraduate-course/real-estate-msc/',
'https://www.kingston.ac.uk/postgraduate-course/general-law-llm/',
'https://www.kingston.ac.uk/postgraduate-course/creative-writing-ma/',
'https://www.kingston.ac.uk/postgraduate-course/creative-writing-mfa/',
'https://www.kingston.ac.uk/postgraduate-course/creative-writing-publishing-ma/',
'https://www.kingston.ac.uk/postgraduate-course/media-communication-ma/',
'https://www.kingston.ac.uk/postgraduate-course/journalism-ma/',
'https://www.kingston.ac.uk/postgraduate-course/magazine-journalism-ma/',
'https://www.kingston.ac.uk/postgraduate-course/film-making-ma/',
'https://www.kingston.ac.uk/postgraduate-course/managing-in-the-creative-economy-ma/']
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Kingston University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en #4.degree_name
        programme_en = response.xpath('//*[@id="middle-col"]/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        if 'PgDip/MA' in programme_en:
            degree_name = 'PgDip/MA'
        elif 'MA' in programme_en:
            degree_name = 'MA'
        elif 'MSc' in programme_en:
            degree_name = 'MSc'
        elif 'PgDip' in programme_en:
            degree_name = 'PgDip'
        elif 'MArch' in programme_en:
            degree_name = 'MArch'
        elif 'MRes' in programme_en:
            degree_name = 'MRes'
        elif 'MMus' in programme_en:
            degree_name = 'MMus'
        elif 'PhD' in programme_en:
            degree_name = 'PhD'
        elif 'PGCE' in programme_en:
            degree_name = 'PGCE'
        elif 'MFA' in programme_en:
            degree_name = 'MFA'
        elif 'LLM' in programme_en:
            degree_name = 'LLM'
        elif 'MLA' in programme_en:
            degree_name = 'MLA'
        elif 'PgCert' in programme_en:
            degree_name = 'PgCert'
        elif 'MPhilStud' in programme_en:
            degree_name = 'MPhilStud'
        else:
            degree_name = 'N/A'
        if degree_name !='N/A':
            programme_en = programme_en.replace(degree_name,'').replace('(','').replace(")",'').replace('&amp;','')
        else:
            pass
        # print(degree_name)
        # print(programme_en)

        #5.degree_type
        degree_type = 2


        #6.teach_time
        teach_time = response.xpath('//table[1]//tr[2]/td[1]').extract()
        teach_time = ''.join(teach_time)
        teach_time = remove_tags(teach_time)
        teach_time = clear_space_str(teach_time)
        if 'Part time' in teach_time:
            teach_time = 'Part time'
        else:
            teach_time = 'Full time'
            # print(url)
        # print(teach_time)

        #7.duration  #8.duration_per
        duration_list = response.xpath('//table[1]//tr[2]/td[2]').extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        duration_list = clear_space_str(duration_list)
        try:
            duration = re.findall('\d+',duration_list)[0]
        except:
            duration = 1
        if 'months' in duration_list:
            duration_per = '3'
        else:
            duration_per = '1'
        # print(duration,"*************",duration_per)

        #9.start_date
        start_date = response.xpath('//table[1]//tr[2]/td[4]').extract()
        if len(start_date) ==0:
            start_date = response.xpath('//table[1]//tr[2]/td[3]').extract()
        start_date = ''.join(start_date)
        if 'September 2018' in start_date and 'January 2019' in start_date:
            start_date = '2018-9,2019-1'
        else:
            start_date = remove_tags(start_date)
            start_date = clear_space_str(start_date)
            start_date = translate_month(start_date)
            if start_date == 9:
                start_date = '2018-' + str(start_date)
            elif start_date ==10:
                start_date = '2018-' + str(start_date)
            elif start_date == 1:
                start_date = '2019-' + str(start_date)
            elif start_date == 2:
                start_date = '2019-' + str(start_date)
            else:
                start_date = '2018-9'

        # print(start_date)

        #10.overview_en
        overview_en = response.xpath("//*[contains(text(),'Assessment')]/preceding-sibling::*").extract()
        overview_en = ''.join(overview_en)
        overview_en = clear_space_str(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #11.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'Assessment')]//following-sibling::*").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        assessment_en = clear_space_str(assessment_en)
        # print(assessment_en)

        #12.modules_en

        # modules_en =response.xpath("//*[contains(text(),'Core modules')]//following-sibling::ul[1]/li").extract()
        # modules_en = ''.join(modules_en)
        # # modules_en = remove_tags(modules_en)
        # modules_en = clear_space_str(modules_en)
        # modules_en = remove_class(modules_en)
        # if len(modules_en)==0:
        #     modules_en_url = response.xpath("//*[contains(text(),'Course features')]//@href").extract()[0]
        #     modules_en_url = 'https://www.kingston.ac.uk' + modules_en_url
        # if len(modules_en_url)!=0:
        #     headers = {
        #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        #     data = requests.get(modules_en_url, headers=headers)
        #     response3 = etree.HTML(data.text)
        #     modules_en = response3.xpath("//*[contains(text(),'What this course offers you')]/../following-sibling::*")
        #     doc = ""
        #     if len(modules_en) > 0:
        #         for a in modules_en:
        #             doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
        #             doc = remove_class(doc)

        # print(doc)

        #13.ielts  14.15.16.17
        ielts_url = response.xpath("//*[contains(text(),'Entry requirements')]//@href").extract()[0]
        ielts_url = 'https://www.kingston.ac.uk'+ ielts_url

        if len(ielts_url) != 0:
            datadict = self.parse_ielts(ielts_url)

        ielts = datadict.get('ielts')
        ielts_r = datadict.get('ielts_r')
        ielts_w = datadict.get('ielts_w')
        ielts_s = datadict.get('ielts_s')
        ielts_l = datadict.get('ielts_l')


        #18.rntry_requirements
        rntry_requirements = datadict.get('rntry_requirements')
        rntry_requirements = '<p>'+rntry_requirements+'</p>'

        #19.tuition_fee
        # try:
        #     tuition_fee_url = response.xpath("//*[contains(text(),'Fees and bursaries')]//@href").extract()[0]
        # except:
        #     tuition_fee_url = ''
        # if len(tuition_fee_url)!=0:
        #     tuition_fee_url = 'https://www.kingston.ac.uk'+ tuition_fee_url
        #     tuitionfeedict = self.parse_gettuitionfee(tuition_fee_url)
        # try:
        #     tuition_fee = tuitionfeedict.get("tuition_fee")
        # except:
        #     tuition_fee = 0

        #20.tuition_fee_pre
        tuition_fee_pre = '£'

        #21.apply_proces_en
        apply_proces_en = response.url +'apply-now.html'
        # print(apply_proces_en)

        #22.career_en
        career_en_url = url + 'after-you-graduate.html'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        data = requests.get(career_en_url, headers=headers)
        response_career_en = etree.HTML(data.text)
        career_en = response_career_en.xpath("//h2[contains(text(),'Where this course will take you')]/../..")
        doc = ""
        if len(career_en) > 0:
            for a in career_en:
                doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                doc = remove_class(doc)
        career_en = ''.join(doc)

        #23.location
        location = 'London'
        #24.apply_pre
        apply_pre = '£'
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_name'] = degree_name
        item['degree_type'] = degree_type
        item['teach_time'] = teach_time
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['start_date'] = start_date
        item['overview_en'] = overview_en
        item['assessment_en'] = assessment_en
        # item['modules_en'] = doc
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        # item['tuition_fee'] = tuition_fee
        item['rntry_requirements'] = rntry_requirements
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_proces_en'] = apply_proces_en
        item['career_en'] = career_en
        item['location'] = location
        yield  item

    def parse_ielts(self,ielts_url):
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        data = requests.get(ielts_url,headers=headers)
        response = etree.HTML(data.text)
        # print(data.text)
        datadict = {}
        ielts = response.xpath("//*[contains(text(),'English language requirements')]/../following-sibling::*//text()")
        ielts = ''.join(ielts)
        try:
            ielts = re.findall('\d\.\d',ielts)
        except:
            ielts = None
        if len(ielts) ==3:
            a = ielts[0]
            b = ielts[1]
            c = ielts[2]
            ielts = a
            ielts_w = b
            ielts_r = c
            ielts_l = c
            ielts_s = c
        elif len(ielts) ==2:
            a = ielts[0]
            b = ielts[1]
            ielts = a
            ielts_w = b
            ielts_r = b
            ielts_l = b
            ielts_s = b
        else:
            ielts = 6.5
            ielts_w = 5.5
            ielts_r = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
        # print(ielts,ielts_w,ielts_r,ielts_s,ielts_l)
        datadict['ielts'] = ielts
        datadict['ielts_r'] = ielts_r
        datadict['ielts_w'] = ielts_w
        datadict['ielts_s'] = ielts_s
        datadict['ielts_l'] = ielts_l
        rntry_requirements = response.xpath("//*[contains(text(),'What you need to apply for this course')]/../following-sibling::*//text()")
        rntry_requirements = ''.join(rntry_requirements)
        # print(rntry_requirements,'************************************************************************')
        datadict['rntry_requirements'] = rntry_requirements
        return datadict
    #
    # def parse_gettuitionfee(self,tuitionfee_url):
    #     headers = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    #     data = requests.get(tuitionfee_url,headers=headers)
    #     response = etree.HTML(data.text)
    #     tuitionfeedict ={}
    #     tuition_fee = response.xpath("//*[contains(text(),'Overseas (not EU) 2018/19')]//following-sibling::*//text()")
    #     tuition_fee = ''.join(tuition_fee)
    #     tuition_fee = getTuition_fee(tuition_fee)
    #     tuitionfeedict['tuition_fee'] = tuition_fee
    #     # print(tuition_fee)
    #     return  tuitionfeedict
    #
    # def parse_getcareer(self,career_url):
    #     headers = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    #     data = requests.get(career_url, headers=headers)
    #     response = etree.HTML(data.text)
    #     careerdict = {}
    #     career_en = response.xpath("//*[contains(text(),'career')]//following-sibling::*//text()")
    #     career_en = ''.join(career_en)
    #     # print(career_en)
    #     careerdict["career_en"] = career_en
    #     return  careerdict

