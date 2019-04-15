# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/10/29 10:18'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from lxml import etree
import requests

class NewfoundlandMemorialUniversity_U_GrenfellSpider(scrapy.Spider):
    name = 'NewfoundlandMemorialUniversity_U_Grenfell'
    allowed_domains = ['mun.ca/']
    start_urls = []
    C= [
        'http://www.grenfell.mun.ca/business',
        'http://www.grenfell.mun.ca/mathematics',
        'http://www.grenfell.mun.ca/education',
        'http://www.grenfell.mun.ca/english',
        'http://www.grenfell.mun.ca/environmental-science',
        'http://www.grenfell.mun.ca/environmental-studies',
        'http://www.grenfell.mun.ca/science',
        'http://www.grenfell.mun.ca/historical-studies',
        'http://www.grenfell.mun.ca/humanities',
        'http://www.grenfell.mun.ca/physics',
        'http://www.grenfell.mun.ca/psychology',
        'http://www.grenfell.mun.ca/academics-and-research/Pages/Bachelor-of-Science/Psychology.aspx',
        'http://www.grenfell.mun.ca/social-cultural-studies',
        'http://www.grenfell.mun.ca/resource-management',
        'http://www.grenfell.mun.ca/theatre',
        'http://www.grenfell.mun.ca/visual-arts'
    ]
    C = set(C)
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)

        #1.school_name
        school_name = 'Newfoundland Memorial University'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.major_name_en
        major_name_en_a = response.xpath("//div[@id='pageHeading']//h1").extract()
        major_name_en_a = ''.join(major_name_en_a)
        major_name_en_a = remove_tags(major_name_en_a).replace(', BFA','')
        if 'environmental sustainability' in major_name_en_a:
            major_name_en = 'Environmental sustainability'
        elif 'education' in major_name_en_a:
            major_name_en = 'Education'
        else:
            major_name_en = major_name_en_a
        # print(major_name_en,url)

        #4.campus
        campus = 'Grenfell Campus'

        #5.location
        location = 'Grenfell'

        #6.department
        major_list = ['Business administration','Computational mathematics','Education','English','Environmental science','Environmental studies','General science','Historical studies','Humanities','Physics','Psychology','Psychology','Social cultural studies','Environmental sustainability','Theatre','Visual Arts']
        department_list = ['Arts and Social Science','Science and the Environment','Education','Arts and Social Science','Science and the Environment','Science and the Environment','Science and the Environment','Arts and Social Science','Arts and Social Science','Science and the Environment','Arts and Social Science','Science','Arts and Social Science','Science and the Environment','Fine Arts','Fine Arts']
        department = department_list[major_list.index(major_name_en)]
        # print(department)

        #7.degree_name
        degree_name = None

        # 8.duration #34.duration_per
        duration = None
        duration_per = None

        #9.deadline
        if '​Theatre' in major_name_en:
            deadline = '2019-03-31'
        elif 'Visual arts' in major_name_en:
            deadline = '2019-03-01'
        else:
            deadline = '2019-02-01,2019-03-01,2019-10-01'

        #10.overview_en
        if 'Historical studies' in major_name_en or 'Theatre' in major_name_en:
            overview_en = response.xpath("//h2[contains(text(),'Why')]//following::p[1]").extract()
        elif 'sustainability' in major_name_en:
            overview_en = response.xpath("//h2[contains(text(),'Why')]//following::p[position()<4]|//h2[contains(text(),'Why')]//following::ul[1]").extract()
        elif 'Environmental studies' in major_name_en:
            overview_en = response.xpath("//h3[contains(text(),'Why')]//following::p[position()<3]").extract()
        elif 'Education' in major_name_en:
            overview_en = response.xpath('//*[@id="ctl00_PlaceHolderMain_ctl01__ControlWrapper_RichHtmlField"]/h2|//*[@id="ctl00_PlaceHolderMain_ctl01__ControlWrapper_RichHtmlField"]/p').extract()
        else:
            overview_en = response.xpath("//h2[contains(text(),'Why')]//following::p[1]|//h2[contains(text(),'Why')]//following::ul[1]").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #11.modules_en
        modules_en_url = url.replace('.aspx','/Courses.aspx')
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        try:
            response1 = requests.get(modules_en_url,headers=headers)
            data = etree.HTML(response1.text)
            modules_en = data.xpath('//table')
            doc = ""
            if len(modules_en) > 0:
                for a in modules_en:
                    doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc = remove_class(doc)
            modules_en = doc
        except:
            modules_en = None


        #12.career_en
        career_en = response.xpath("//h2[contains(text(),'Career opportunities')]//following-sibling::p[1]|//h2[contains(text(),'Career opportunities')]//following-sibling::ul").extract()
        if len(career_en)==0:
            career_en  = response.xpath("//h3[contains(text(),'Career opportunities')]//following-sibling::p[1]|//h3[contains(text(),'Career opportunities')]//following-sibling::ul[1]").extract()
        if 'Social cultural studies' in major_name_en:
            career_en  = response.xpath("//h2[contains(text(),'Career opportunities')]//following-sibling::p[position()<16]").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        # 13.entry_requirements_en
        entry_requirements_en = '<p>To be eligible for admission as an international high school student, you must have graduated from a recognized university preparatory program with acceptable senior level courses in five subject areas, which normally include: English, mathematics, a laboratory science, a social science and one other subject area. Admission requirements may vary depending on the educational system(s) in place in your country. Visit the Admissions Requirements page to see application and admission requirements, by country, including details about: Credentials, certificates, or transcripts required; Subject areas and minimum grades;  English proficiency; and Document submission requirements</p>'

        # 14.require_chinese_en
        require_chinese_en = '<p>Credential Senior Secondary School Certificate ,Required Subject Areas English Mathematics* Laboratory Science* (Biology, Chemistry, or Physics) Social Studies or Modern/Classical Language Elective</p>'

        # 15.average_score
        average_score = 75

        # 16.ielts_desc 171819
        ielts_desc = 'A minimum overall band score of 6.5, with at least a band 6 in reading and writing.'
        ielts = 6.5
        ielts_r = 6
        ielts_w = 6

        # 20.toefl_desc 2122232425
        toefl_desc = 'A minimum score of 550 on the paper-based test, or 79 on the internet-based TOEFL (iBT) with a minimum score of 20 in reading and writing, and not less than 17 in listening and speaking.'
        toefl = 79
        toefl_r = 20
        toefl_w = 20
        toefl_l = 17
        toefl_s = 17

        # 26.tuition_fee
        tuition_fee = '11,460'

        # 27.tuition_fee_pre
        tuition_fee_pre = '$'

        # 28.apply_pre
        apply_pre = '$'

        # 29.apply_fee
        apply_fee = 120

        # 30.ib
        ib = 'Minimum score of 24 on the IB Diploma with completion of the required subject areas or completion of another recognized High School diploma program. Please see your country’s specific requirements for more information.'

        # 31.alevel
        alevel = 'Completion of the GCE including a minimum grade of C/4 in the required subject areas at the Ordinary (“O” or IGCSE) Level and at least three Advanced Subsidiary (“AS”) Level or two Advanced (“A”) Level subjects with a minimum grade of C. Exceptional candidates may be admitted based upon GCSE/IGCSE examination results.'

        # 32.toefl_code
        toefl_code = '0885'

        # 33.sat_code
        sat_code = '0885'

        item['duration_per'] = duration_per
        item['toefl_code'] = toefl_code
        item['sat_code'] = sat_code
        item['school_name'] = school_name
        item['url'] = url
        item['major_name_en'] = major_name_en
        item['campus'] = campus
        item['location'] = location
        item['department'] = department
        item['degree_name'] = degree_name
        item['duration'] = duration
        item['deadline'] = deadline
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['entry_requirements_en'] = entry_requirements_en
        item['require_chinese_en'] = require_chinese_en
        item['average_score'] = average_score
        item['ielts_desc'] = ielts_desc
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['toefl_desc'] = toefl_desc
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_pre'] = apply_pre
        item['apply_fee'] = apply_fee
        item['ib'] = ib
        item['alevel'] = alevel
        yield item