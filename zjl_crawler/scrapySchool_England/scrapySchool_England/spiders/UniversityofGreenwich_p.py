# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/11 10:17'
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
class UniversityofGreenwichSpider(scrapy.Spider):
    name = 'UniversityofGreenwich_p'
    allowed_domains = ['gre.ac.uk/']
    start_urls = []
    C = [
        'https://www.gre.ac.uk/pg/ach/intmarpol',
        'https://www.gre.ac.uk/pg/ach/mbit',
        'https://www.gre.ac.uk/pg/ach/filmprod',
        'https://www.gre.ac.uk/pg/ach/projman',
        'https://www.gre.ac.uk/pg/ach/coneco',
        'https://www.gre.ac.uk/pg/ach/cgcis',
        'https://www.gre.ac.uk/pg/ach/cgcs',
        'https://www.gre.ac.uk/pg/ach/sbe',
        'https://www.gre.ac.uk/pg/ach/intllaw',
        'https://www.gre.ac.uk/pg/ach/cgbdbi',
        'https://www.gre.ac.uk/pg/ach/csne',
        'https://www.gre.ac.uk/pg/ach/realest',
        'https://www.gre.ac.uk/pg/engsci/engman',
        'https://www.gre.ac.uk/pg/ach/cfsm',
        'https://www.gre.ac.uk/pg/ach/litlon',
        'https://www.gre.ac.uk/pg/ach/arcdip',
        'https://www.gre.ac.uk/pg/eduhea/ed',
        'https://www.gre.ac.uk/pg/ach/lanarc',
        'https://www.gre.ac.uk/pg/engsci/elecpow',
        'https://www.gre.ac.uk/pg/ach/intcrim',
        'https://www.gre.ac.uk/pg/ach/wdcp',
        'https://www.gre.ac.uk/pg/engsci/elelec',
        'https://www.gre.ac.uk/pg/engsci/mechmaneng',
        'https://www.gre.ac.uk/pg/ach/lan-arc-mla',
        'https://www.gre.ac.uk/pg/engsci/glo-shi',
        'https://www.gre.ac.uk/pg/engsci/biotech',
        'https://www.gre.ac.uk/pg/engsci/aps',
        'https://www.gre.ac.uk/pg/ach/crimpsych',
        'https://www.gre.ac.uk/pg/engsci/strengthcond',
        'https://www.gre.ac.uk/pg/ach/socialpolicy',
        'https://www.gre.ac.uk/pg/ach/tesol,-ma',
        'https://www.gre.ac.uk/pg/engsci/oil-mgt',
        'https://www.gre.ac.uk/pg/engsci/glob-envi-change',
        'https://www.gre.ac.uk/pg/ach/spatial-data-science',
        'https://www.gre.ac.uk/pg/engsci/agrsustdev',
        'https://www.gre.ac.uk/pg/ach/advlandurb',
        'https://www.gre.ac.uk/pg/bus/finman',
        'https://www.gre.ac.uk/pg/engsci/fs',
        'https://www.gre.ac.uk/pg/bus/tsm',
        'https://www.gre.ac.uk/pg/ach/ma-digital-arts',
        'https://www.gre.ac.uk/pg/engsci/envcons',
        'https://www.gre.ac.uk/pg/engsci/civeng',
        'https://www.gre.ac.uk/pg/engsci/mac-int',
        'https://www.gre.ac.uk/pg/bus/lscm',
        'https://www.gre.ac.uk/pg/engsci/foodinnov',
        'https://www.gre.ac.uk/pg/ach/applied-linguistics,-ma',
        'https://www.gre.ac.uk/pg/bus/intbus',
        'https://www.gre.ac.uk/pg/eduhea/childadolpsych',
        'https://www.gre.ac.uk/pg/bus/pr',
        'https://www.gre.ac.uk/pg/engsci/mps',
        'https://www.gre.ac.uk/pg/bus/inttour',
        'https://www.gre.ac.uk/pg/bus/accfin',
        'https://www.gre.ac.uk/pg/bus/intmba',
        'https://www.gre.ac.uk/pg/engsci/wat-was-env-eng',
        'https://www.gre.ac.uk/pg/eduhea/nursing-adult-nursing',
        'https://www.gre.ac.uk/pg/engsci/natural-resources,-msc-by-research',
        'https://www.gre.ac.uk/pg/eduhea/hsc',
        'https://www.gre.ac.uk/pg/bus/hrm',
        'https://www.gre.ac.uk/pg/eduhea/nursing-childrens-nursing',
        'https://www.gre.ac.uk/pg/eduhea/psych',
        'https://www.gre.ac.uk/pg/eduhea/sport-and-exercise-psychology',
        'https://www.gre.ac.uk/pg/bus/stratmdual',
        'https://www.gre.ac.uk/pg/bus/econ',
        'https://www.gre.ac.uk/pg/eduhea/nursing-mental-health-nursing,-msc',
        'https://www.gre.ac.uk/pg/engsci/engineering,-msc-by-research',
        'https://www.gre.ac.uk/pg/bus/execmba',
        'https://www.gre.ac.uk/pg/bus/stratmcomms',
        'https://www.gre.ac.uk/pg/bus/eveman',
        'https://www.gre.ac.uk/pg/engsci/pb',
        'https://www.gre.ac.uk/pg/bus/inthrm',
        'https://www.gre.ac.uk/pg/bus/finmaninv',
        'https://www.gre.ac.uk/pg/ach/film-production,-ma',
        'https://www.gre.ac.uk/pg/ach/ma-media-and-creative-cultures',
        'https://www.gre.ac.uk/pg/bus/ibf',
        'https://www.gre.ac.uk/pg/bus/stratm',
        'https://www.gre.ac.uk/pg/ach/operational-cyber-security,-msc'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Greenwich'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="faculty"]/div[1]/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en).replace('Postgraduate prospectus','')
        programme_en = clear_space_str(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        try:
            degree_name =re.findall(r',(.*)',programme_en)[0]
        except:
            degree_name = 'N/A'
        try:
            programme_en = programme_en.replace(degree_name,'').replace(',','').strip()
        except:
            pass
        # print(programme_en)
        # print(degree_name)

        #6.department
        department = response.xpath('//*[@id="faculty"]/div[2]/article/div/div/div[1]/div[2]/div[1]/p/a').extract()
        department = ''.join(department)
        department = remove_tags(department)
        if '&amp;' in department:
            department = department.replace('&amp;','')
        # print(department)

        #7.location
        location = response.xpath('//*[@id="faculty"]/div[2]/article/div/div/div[1]/div[2]/div[2]/p/a').extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #8.teach_time
        teach_time_list = response.xpath('//*[@id="faculty"]/div[2]/article/div/div/div[1]/div[2]/div[3]/p[1]').extract()
        teach_time_list = ''.join(teach_time_list)
        teach_time_list = remove_tags(teach_time_list)
        teach_time = 'Full-Time'

        #9.duration #10.duration_per
        try:
            duration = re.findall('\d+',teach_time_list)[0]
        except:
            duration = 1
        if int(duration)>6:
            duration_per = 4
        else:
            duration_per = 1
        # print(duration,'*********',duration_per)

        #11.overview_en
        overview_en = response.xpath('//*[@id="overview"]/*').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #12.modules_en
        modules_en_url = response.xpath("//meta[@name='prog_no']//@content").extract()
        modules_en_url = ''.join(modules_en_url)
        if len(modules_en_url) != 0:
            modules_en_url = 'https://www.gre.ac.uk/ug/content/ajax/courses-ajax-call?prog=' + str(modules_en_url)
        else:
            modules_en_url = ''
        if len(modules_en_url) != 0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data = requests.get(modules_en_url, headers=headers)
            response1 = etree.HTML(data.text)
            modules_en = response1.xpath("//div[@class='gre-page-copy']")
            doc = ""
            if len(modules_en) > 0:
                for a in modules_en:
                    doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc = remove_class(doc)
                    modules_en = doc
        else:
            modules_en = 'N/A'
            doc = ''
        # print(modules_en)

        #13.rntry_requirements
        rntry_requirements = response.xpath('//*[@id="entry-requirements"]/div').extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements).strip()
        # print(rntry_requirements)

        #14.assessment_en
        try:
            assessment_en = response.xpath("//h4[contains(text(),'Assessment')]//following-sibling::*").extract()[0]
            assessment_en = remove_class(assessment_en)
        except:
            assessment_en = ''
        # print(assessment_en)

        #15.career_en
        career_en = response.xpath("//h3[contains(text(),'Careers')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #16.tuition_fee
        if 'LLB' in programme_en:
            tuition_fee = 13950
        elif 'MArch' in programme_en:
            tuition_fee = 13950
        elif 'Business' in programme_en:
            tuition_fee = 13950
        elif 'Economics' in programme_en:
            tuition_fee = 14250
        elif 'Risk' in programme_en:
            tuition_fee = 14250
        elif 'International Banking and Finance' in programme_en:
            tuition_fee = 14250
        elif 'Advanced Practice' in programme_en:
            tuition_fee = 14500
        elif 'Healthcare Practic' in programme_en:
            tuition_fee = 14500
        elif 'MBA' in programme_en:
            tuition_fee = 15500
        else:
            tuition_fee = 13500

        #17.tuition_fee_pre
        tuition_fee_pre = '£'

        #18.apply_proces_en
        apply_proces_en = 'https://www.gre.ac.uk/study/apply/pg'

        #19.ielts 20212223
        ielts_list = re.findall(r'[567]\.\d',rntry_requirements)
        if len(ielts_list)==2:
            a = ielts_list[0]
            b = ielts_list[1]
            ielts = a
            ielts_r = b
            ielts_w = b
            ielts_l = b
            ielts_s = b
        elif len(ielts_list)==1:
            a = ielts_list[0]
            ielts = a
            ielts_r = None
            ielts_w = None
            ielts_l = None
            ielts_s = None
        elif len(ielts_list)>2:
            a = ielts_list[0]
            b = ielts_list[1]
            ielts = a
            ielts_r = b
            ielts_w = b
            ielts_l = b
            ielts_s = b
        else:
            ielts = None
            ielts_r = None
            ielts_w = None
            ielts_l = None
            ielts_s = None


        #24.apply_pre
        apply_pre = '£'
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['department'] = department
        item['location'] = location
        item['teach_time'] = teach_time
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['rntry_requirements'] = rntry_requirements
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_proces_en'] = apply_proces_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        yield  item


    # def get_modules(self,modules_en_url):
    #     headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    #     data = requests.get(modules_en_url, headers=headers)
    #     response = etree.HTML(data.text)
    #     datadict = {}
    #     modules_en = response.xpath('//*[@id="default"]/div[2]/article/div/div[2]/ul/li/a/text()')
    #     modules_en = '\n'.join(modules_en)
    #     # print(modules_en)
    #     datadict['modules_en'] = modules_en
    #     return datadict