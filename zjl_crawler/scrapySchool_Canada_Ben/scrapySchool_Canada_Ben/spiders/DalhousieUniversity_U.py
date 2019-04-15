# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/11/5 15:47'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from lxml import etree
import requests

class DalhousieUniversity_USpider(scrapy.Spider):
    name = 'DalhousieUniversity_U'
    allowed_domains = ['dal.ca/']
    start_urls = []
    C= [
        'https://www.dal.ca/academics/programs/undergraduate/pharmacy.html',
        'https://www.dal.ca/academics/programs/undergraduate/hs.html',
        'https://www.dal.ca/academics/programs/undergraduate/german.html',
        'https://www.dal.ca/academics/programs/undergraduate/ids.html',
        'https://www.dal.ca/academics/programs/undergraduate/healthpromotion.html',
        'https://www.dal.ca/academics/programs/undergraduate/bcmb.html',
        'https://www.dal.ca/academics/programs/undergraduate/philosophy.html',
        'https://www.dal.ca/academics/programs/undergraduate/management.html',
        'https://www.dal.ca/academics/programs/undergraduate/recmgmt.html',
        'https://www.dal.ca/academics/programs/undergraduate/plant-science.html',
        'https://www.dal.ca/academics/programs/undergraduate/engineering.html',
        'https://www.dal.ca/academics/programs/undergraduate/nursing.html',
        'https://www.dal.ca/academics/programs/undergraduate/commerce.html',
        'https://www.dal.ca/academics/programs/undergraduate/environmental-landscape-horticulture.html',
        'https://www.dal.ca/academics/programs/undergraduate/arts-social-sciences.html',
        'https://www.dal.ca/academics/programs/undergraduate/earth-sciences.html',
        'https://www.dal.ca/academics/programs/undergraduate/socialwork.html',
        'https://www.dal.ca/academics/programs/undergraduate/pre-veterinary-medicine.html',
        'https://www.dal.ca/academics/programs/undergraduate/mathematics.html',
        'https://www.dal.ca/academics/programs/undergraduate/canadian.html',
        'https://www.dal.ca/academics/programs/undergraduate/russian.html',
        'https://www.dal.ca/academics/programs/undergraduate/small-business-management.html',
        'https://www.dal.ca/academics/programs/undergraduate/european.html',
        'https://www.dal.ca/academics/programs/undergraduate/spanish.html',
        'https://www.dal.ca/academics/programs/undergraduate/disp.html',
        'https://www.dal.ca/academics/programs/undergraduate/architecture.html',
        'https://www.dal.ca/academics/programs/undergraduate/rectherapeutic.html',
        'https://www.dal.ca/academics/programs/undergraduate/compsci.html',
        'https://www.dal.ca/academics/programs/undergraduate/economics.html',
        'https://www.dal.ca/academics/programs/undergraduate/landscape-architecture.html',
        'https://www.dal.ca/academics/programs/undergraduate/sosa.html',
        'https://www.dal.ca/academics/programs/undergraduate/theatre.html',
        'https://www.dal.ca/academics/programs/undergraduate/bioveterinary-science.html',
        'https://www.dal.ca/academics/programs/undergraduate/neuroscience.html',
        'https://www.dal.ca/academics/programs/undergraduate/polisci.html',
        'https://www.dal.ca/academics/programs/undergraduate/cinema-and-media-studies.html',
        'https://www.dal.ca/academics/programs/undergraduate/animal-science.html',
        'https://www.dal.ca/academics/programs/undergraduate/international-food-business.html',
        'https://www.dal.ca/academics/programs/undergraduate/commdesign.html',
        'https://www.dal.ca/academics/programs/undergraduate/pas.html',
        'https://www.dal.ca/academics/programs/undergraduate/agricultural-business.html',
        'https://www.dal.ca/academics/programs/undergraduate/biology.html',
        'https://www.dal.ca/academics/programs/undergraduate/chemistry.html',
        'https://www.dal.ca/academics/programs/undergraduate/kinesiology.html',
        'https://www.dal.ca/academics/programs/undergraduate/religious.html',
        'https://www.dal.ca/academics/programs/undergraduate/marinebio.html',
        'https://www.dal.ca/academics/programs/undergraduate/applied-computer-science.html',
        'https://www.dal.ca/academics/programs/undergraduate/classics.html',
        'https://www.dal.ca/academics/programs/undergraduate/psychology.html',
        'https://www.dal.ca/academics/programs/undergraduate/ljso.html',
        'https://www.dal.ca/academics/programs/undergraduate/creativewriting.html',
        'https://www.dal.ca/academics/programs/undergraduate/english.html',
        'https://www.dal.ca/academics/programs/undergraduate/mbim.html',
        'https://www.dal.ca/academics/programs/undergraduate/history.html',
        'https://www.dal.ca/academics/programs/undergraduate/integrated-environmental-management.html',
        'https://www.dal.ca/academics/programs/undergraduate/environmental-sciences.html',
        'https://www.dal.ca/academics/programs/undergraduate/ocean-sciences.html',
        'https://www.dal.ca/academics/programs/undergraduate/stats.html',
        'https://www.dal.ca/academics/programs/undergraduate/medsci.html',
        'https://www.dal.ca/academics/programs/undergraduate/gws.html',
        'https://www.dal.ca/academics/programs/undergraduate/french.html',
        'https://www.dal.ca/academics/programs/undergraduate/environmental.html',
        'https://www.dal.ca/academics/programs/undergraduate/actuarial-science.html',
        'https://www.dal.ca/academics/programs/undergraduate/music.html',
        'https://www.dal.ca/academics/programs/undergraduate/agricultural-economics.html',
        'https://www.dal.ca/academics/programs/undergraduate/aquaculture.html',
        'https://www.dal.ca/academics/programs/undergraduate/ess.html',
    ]
    for i in C:
        start_urls.append(i)

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)

        #1.school_name
        school_name = 'Dalhousie University'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.major_name_en
        major_name_en = response.xpath('//*[@id="skipContent"]/div/div/div[1]/div[1]/div/h2/a/text()').extract()
        major_name_en = ''.join(major_name_en)
        major_name_en = remove_tags(major_name_en).strip()
        # print(major_name_en)

        #4.degree_name
        degree_name = response.xpath('//*[@id="skipContent"]/div/div/div[1]/div[1]/div/h2/a/span').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name).strip().replace('amp;','')
        # print(degree_name)

        #5.overview_en
        try:
            overview_en_url = response.xpath("//a[contains(text(),'Program overview') or contains(text(),'Program Overview')]//@href").extract()[0]
            headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
            data = requests.get(overview_en_url,headers=headers)
            response1 = etree.HTML(data.text)
            overview_en = response1.xpath("//div[@class='topRichText text parbase']|//div[@class='text parbase section']")
            doc = ""
            if len(overview_en) > 0:
                for a in overview_en:
                    doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc = remove_class(doc)
                    overview_en = doc
        except:
            overview_en = None
        # print(overview_en,url)

        #6.modules_en
        try:
            modules_en_url = response.xpath(
                "//a[contains(text(),'What will I learn?')]//@href").extract()[0]
            # print(modules_en_url)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
            data2 = requests.get(modules_en_url, headers=headers)
            response2 = etree.HTML(data2.text)
            modules_en = response2.xpath("//div[@class='contentPar parsys']")
            doc2 = ""
            if len(modules_en) > 0:
                for a in modules_en:
                    doc2 += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc2 = remove_class(doc2)
                    modules_en = doc2
        except:
            modules_en = None
        # print(modules_en,url)

        #7.career_en
        try:
            career_en_url = response.xpath("//a[contains(text(),'What can I do with this degree?') or contains(text(),'What can I do with Pre-Vet studies?')]//@href").extract()[0]
            # print(career_en_url)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
            data3 = requests.get(career_en_url, headers=headers)
            response3 = etree.HTML(data3.text)
            career_en = response3.xpath("//div[@class='text parbase section']")
            doc3 = ""
            if len(career_en) > 0:
                for a in career_en:
                    doc3 += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc3 = remove_class(doc3)
                    career_en = doc3
        except:
            career_en = None
        # print(career_en)

        #8.entry_requirements_en
        entry_requirements_en = '<p>You can apply to many Dalhousie programs directly from high school. The general admission requirements for degree programs are:Completion of secondary school (i.e. Grade 12) with a minimum overall average of 70% in five academic Grade 12 courses;A final grade of at least 70% in Grade 12 English and any other required subject</p>'

        #9.require_chinese_en
        require_chinese_en = "<p>Senior Middle School Graduation Certificate and Nation Matriculation Examination or Graduation Examination</p>"

        #10.alevel
        alevel = "As a GCE A Level.British System applicant you need a minimum of five subjects, including two A (Advanced) levels or four AS (Advanced Subsidiary) levels with grades of C or better, for admission. Exceptional candidates may be accepted on GCSE or O (Ordinary) levels."

        #11.ib
        ib = 'As an IB student, you must meet our general entrance requirements. If you are completing the IB Diploma you need at least 26 points (including bonus points) for admission.'

        #12.ap
        ap = 'Dalhousie awards university credit for selected AP courses completed with a national exam result of 4 or 5. '

        #13.toefl_desc 1415161718
        toefl_desc = '237 (computer-based) 90(iBT) and no lower than 20 in each band'
        toefl = 90
        toefl_r = 20
        toefl_w = 20
        toefl_s = 20
        toefl_l = 20

        #19.ielts_desc 2021222324
        ielts_desc = '6.5 overall and no lower than 6.0 in each band'
        ielts = 6.5
        ielts_r = 6.0
        ielts_w = 6.0
        ielts_s = 6.0
        ielts_l = 6.0

        #25.toefl_code #26.sat_code
        toefl_code = '0915'
        sat_code = toefl_code

        #27.apply_fee #28.apply_pre
        apply_fee = 70
        apply_pre = '$'

        #29.deadline
        if 'Health Sciences' in degree_name:
            deadline = '2019-02-15'
        elif  'Nursing' in degree_name:
            deadline = '2019-02-28'
        elif 'Music' in degree_name or 'Environmental Design Studie' in degree_name:
            deadline = '2019-03-01'
        elif 'Medical Sciences' in degree_name:
            deadline = '2019-03-15'
        elif 'International Food Business' in degree_name:
            deadline = '2019-07-01'
        else:
            deadline = '2019-04-01'

        #30.tuition_fee_pre
        tuition_fee_pre = '$'

        #31.act_code
        act_code = '5373'

        #32.sat_desc
        sat_desc = '<p>We also require strong academic standing with a final senior year minimum average of ‘B’ for consideration, and a minimum SAT score of 1100 (new SAT; Post March 2016). Applicants who took the SAT before March 2016 are required to have a minimum score of 1650. Dalhousie’s SAT code is 0915. SAT subject tests are not required for admission. You may present an ACT result in lieu of an SAT result. Dalhousie requires a minimum ACT composite score of 23, with no individual score less than 20. Dalhousie’s ACT code is 5373.For both the SAT & ACT, Dalhousie will super score an applicant with multiple test dates, where the highest category score is taken irrespective of test date. Admission to Dalhousie is purely quantitative for most direct-entry programs. As such, essays, references and/or interviews are not required for admission.Applicants applying for early admission between October 15 and January 31 are required to send in official transcripts of all results up until the end of junior year, in lieu of completing the self-reported grades section of the application.</p>'

        #33.act_desc
        act_desc = sat_desc

        #34.tuition_fee
        tuition_fee_dict = {'Agriculture':'16,669.14',
                            'Architecture':'20,036.06',
                            'Arts & Social Science':'19,153.06',
                            'Music':'20,038.66',
                            'Theatre':'19,345.06',
                            'Commerce Co-op':'21,331.06',
                            'Community Design':'19,712.06',
                            'Costume Studies':'19,954.06',
                            'Engineering':'21,206.06',
                            'Health Sciences':'20,414.06',
                            'Kinesiology':'20,410.06',
                            'Nursing':'21,071.06',
                            'Pharmacy':'21,740.06',
                            'Recreation':'20,410.06',
                            'Health':'20,410.06',
                            'Social Work':'19,967.06',
                            }
        tuition_fee = tuition_fee_dict.get(major_name_en)
        if tuition_fee == None:
            if 'Computer Science' in major_name_en:
                tuition_fee = '20,196.06'
            elif 'Management' in major_name_en:
                tuition_fee = '19,585.56'
            elif 'Health' in major_name_en:
                tuition_fee = '20,410.06'
            elif 'Science' in major_name_en:
                tuition_fee = '20,182.06'
            elif 'Sustainability' in major_name_en:
                tuition_fee = '20,363.56'
            else:
                tuition_fee = None
        # print(tuition_fee)

        #35.location
        location = 'Halifax'

        department = response.xpath('//*[@id="skipContent"]/div/div/div[1]/div[1]/div/h2/span/a[1]').extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        item['department'] = department
        item['location'] = location
        item['school_name'] = school_name
        item['url'] = url
        item['major_name_en'] = major_name_en
        item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['entry_requirements_en'] = entry_requirements_en
        item['require_chinese_en'] = require_chinese_en
        item['alevel'] = alevel
        item['ib'] = ib
        item['ap'] = ap
        item['toefl_desc'] = toefl_desc
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['toefl_w'] = toefl_w
        item['ielts_desc'] = ielts_desc
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['toefl_code'] = toefl_code
        item['sat_code'] = sat_code
        item['apply_fee'] = apply_fee
        item['apply_pre'] = apply_pre
        item['deadline'] = deadline
        item['tuition_fee_pre'] = tuition_fee_pre
        item['act_code'] = act_code
        item['sat1_desc'] = sat_desc
        item['act_desc'] = act_desc
        item['tuition_fee'] = tuition_fee
        yield item