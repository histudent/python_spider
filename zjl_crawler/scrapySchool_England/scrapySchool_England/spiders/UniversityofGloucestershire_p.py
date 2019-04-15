# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '18-7-17 下午1:28'
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
from scrapySchool_England.TranslateMonth import translate_month
import  urllib.request
from lxml import  etree
import  requests
class UniversityofGloucestershireSpider(scrapy.Spider):
    name = 'UniversityofGloucestershire_p'
    allowed_domains = ['glos.ac.uk/']
    start_urls = []
    C= [
        'http://www.glos.ac.uk/courses/postgraduate/aec/pages/applied-ecology-postgraduate-certificate-postgraduate-diploma-msc.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/ccw/pages/creative-and-critical-writing-postgraduate-certificate-postgraduate-diploma-ma.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/aftm/pages/accounting-and-finance-masters-stage-msc.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/comtop/pages/computing-masters-stage-msc-masters-stage.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/aft/pages/accounting-and-finance-msc.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/cyb/pages/cyber-security-msc.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/crp/pages/criminology-postgraduate-certificate-postgraduate-diploma-msc.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/iln/pages/illustration-ma.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/edn/pages/education-ma.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/eie/pages/inclusive-education-postgraduate-certificate-postgraduate-diploma-ma-med.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/eel/pages/educational-leadership-postgraduate-certificate-postgraduate-diploma-ma-med.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/fpy/pages/forensic-psychology-postgraduate-certificate-postgraduate-diploma-msc.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/ft/pages/fine-art-postgraduate-certificate-postgraduate-diploma-ma.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/ibu/pages/international-business-msc.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/lc/pages/landscape-architecture-postgraduate-diploma-ma.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/lv/pages/landscape-architecture-with-conversion-year-postgraduate-diploma-ma.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/cmu/pages/ma-creative-music-practice.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/cpm/pages/ma-communications-public-relations-and-media.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/fim/pages/ma-film-making.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/mba/pages/mba-business-administration-postgraduate-certificate-postgraduate-diploma-mba.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/mkt/pages/marketing-postgraduate-certificate-postgraduate-diploma-msc.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/mbatop/pages/mba-business-administration-masters-stage-mba.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/gde/pages/mdes-graphic-design-master-of-design.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/fie/pages/msc-finance-postgraduate-certificate-postgraduate-diploma-msc.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/hrn/pages/msc-human-resource-management-postgraduate-diploma-msc.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/hrntop/pages/msc-human-resource-management-masters-stage-msc.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/pho/pages/photography-postgraduate-certificate-postgraduate-diploma-ma.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/prf/pages/professional-practice-in-physical-education-and-school-sport-postgraduate-certificate-postgraduate-diploma-ma.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/pps/pages/professional-practice-in-sports-coaching-postgraduate-certificate-postgraduate-diploma-msc.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/psg/pages/psychology-postgraduate-certificate-postgraduate-diploma-msc.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/sow/pages/social-work-postgraduate-certificate-postgraduate-diploma-ma.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/sth/pages/sports-therapy-msc.aspx',
        'http://www.glos.ac.uk/courses/postgraduate/ssc/pages/sports-strength-and-conditioning-postgraduate-certificate-postgraduate-diploma-msc.aspx',
        'http://www.glos.ac.uk/courses/research/rspbs/pages/phd-or-msc-by-research-psychology-and-behavioural-sciences.aspx'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Gloucestershire'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en #4.degree_name #5.degree_type
        programme_en_a = response.xpath('//*[@id="uog4PageWrapper"]/div[3]/div/div/h1').extract()
        programme_en_a = ''.join(programme_en_a)
        programme_en_a = remove_tags(programme_en_a)
        programme_en_a = clear_space_str(programme_en_a)
        if '(' in programme_en_a:
            degree_name = re.findall(r'\((.*)\)',programme_en_a)[0]
        else:
            degree_name = 'N/A'
        if 'Social Work' in degree_name:
            degree_name = 'Social Work'
        elif 'MSc' in degree_name:
            degree_name = 'MSc'
        elif 'MA' in degree_name:
            degree_name = 'MA'
        elif 'MBA' in degree_name:
            degree_name = 'MBA'
        elif 'Master of Design' in degree_name:
            degree_name = 'Master of Design'
        elif 'DBA' in degree_name:
            degree_name = 'DBA'
        elif 'PGCE' in degree_name:
            degree_name = 'PGCE'
        elif 'Postgraduate' in degree_name:
            degree_name = 'Postgraduate'
        else:
            degree_name = 'N/A'
        # print(degree_name)
        if '(' in programme_en_a:
            programme_en = re.findall(r'(.*)\(',programme_en_a)[0]
        else:
            programme_en = programme_en_a
        # print(programme_en_a,programme_en)
        degree_type = 2
        # print(programme_en)

        #6.teach_time
        teach_time = response.xpath("//*[contains(text(),'Study mode')]//following-sibling::p[1]").extract()
        teach_time = ''.join(teach_time)
        teach_time = remove_tags(teach_time)
        if 'Full' in teach_time:
            teach_time = 'Full-Time'
        else:
            teach_time = 'Part-Time'
        # print(teach_time)

        #7.teach_type
        if 'research' in url:
            teach_type = 'research'
        else:
            teach_type = 'taught'
        # print(teach_type)

        #8.location
        location = response.xpath("//*[contains(text(),'Campus')]//following-sibling::p[1]").extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #9.overview_en
        overview_en = response.xpath("//strong[contains(text(),'Modules')]/../preceding-sibling::*").extract()
        if len(overview_en)==0:
            overview_en = response.xpath("//h2[contains(text(),'Study style')]//preceding-sibling::*").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #10.tuition_fee_pre
        tuition_fee_pre = '£'

        #11.other
        other = 'http://www.glos.ac.uk/docs/download/Finance/2018-19-International-Tuition-fee-list.pdf'

        #12.apply_proces_en
        apply_proces_en = 'https://www.gov.uk/masters-loan/apply'

        #13.rntry_requirements
        rntry_requirements = response.xpath("//*[contains(text(),'Entry requirements')]//following-sibling::ul[1]").extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #14.ielts 15161718
        ielts_list = re.findall('[567]\.\d',rntry_requirements)
        # print(ielts_list)

        if len(ielts_list)==3:
            a = ielts_list[0]
            b = ielts_list[1]
            c = ielts_list[2]
            ielts = a
            ielts_w = b
            ielts_l = c
            ielts_s = c
            ielts_r = c
        elif len(ielts_list) ==2:
            a = ielts_list[0]
            b = ielts_list[1]
            ielts = a
            ielts_w = b
            ielts_l = b
            ielts_s = b
            ielts_r = b
        elif len(ielts_list) ==1:
            a = ielts_list[0]
            ielts = a
            ielts_w = float(a)-0.5
            ielts_l = float(a)-0.5
            ielts_s = float(a)-0.5
            ielts_r = float(a)-0.5
        else:
            ielts = 6.0
            ielts_w = 5.5
            ielts_r = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
        # print(ielts,ielts_w,ielts_l,ielts_s,ielts_r)

        #19.career_en
        career_en = response.xpath("//*[contains(text(),'Careers')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #20.require_chinese_en
        require_chinese_en = '<p> Successful completion of a Bachelor’s degree with a minimum of 60%</p>'

        #21.apply_pre
        apply_pre = '£'

        #22.tuition_fee
        if 'Accounting and Finance' in programme_en:
            tuition_fee = 13840
        elif 'Business Administration' in programme_en:
            tuition_fee = 14350
        elif 'Finance' in programme_en:
            tuition_fee = 14350
        elif 'Forensic Psychology' in programme_en:
            tuition_fee  =13840
        elif 'Human Resource Management' in programme_en:
            tuition_fee = 13840
        elif 'International Business' in programme_en:
            tuition_fee = 13840
        elif 'Marketing' in programme_en:
            tuition_fee = 13840
        elif 'Psychology' in programme_en:
            tuition_fee  = 14350
        else:
            tuition_fee = 13840

        #23.modules_en
        modules_en_url = response.xpath('//div[@id="ctaCourseMap"]//div//h2//a//@href').extract()
        modules_en_url = ''.join(modules_en_url)
        if len(modules_en_url)!=0:
            modules_en_url = 'http://www.glos.ac.uk' + modules_en_url
            # print(modules_en_url)
        if len(modules_en_url)!=0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data = requests.get(modules_en_url, headers=headers)
            response2 = etree.HTML(data.text)
            judge = response2.xpath('//*[@id="uog4MainContent"]/div/div[2]/div[1]/div/ul/li/a/@href')
            if len(judge)!= 0 :
                modules_en_url = modules_en_url+'/pages/'+judge[-1]
            # print(modules_en_url)
        if len(modules_en_url)!= 0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data = requests.get(modules_en_url, headers=headers)
            response3 = etree.HTML(data.text)
            modules_en = response3.xpath('//*[@id="Level7"]')
            doc = ""
            if len(modules_en) > 0:
                for a in modules_en:
                    doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc = remove_class(doc)
        else:
            doc =''
        # print(doc)
            # print(modules_en)



        item['modules_en'] = doc
        item['tuition_fee'] = tuition_fee
        item['apply_pre'] = apply_pre
        item['require_chinese_en'] = require_chinese_en
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_name'] = degree_name
        item['degree_type'] = degree_type
        item['teach_time'] = teach_time
        item['teach_type'] = teach_type
        item['location'] = location
        item['overview_en'] = overview_en
        item['tuition_fee_pre'] = tuition_fee_pre
        item['other'] = other
        item['apply_proces_en'] = apply_proces_en
        item['rntry_requirements'] = rntry_requirements
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['career_en'] = career_en
        yield item
