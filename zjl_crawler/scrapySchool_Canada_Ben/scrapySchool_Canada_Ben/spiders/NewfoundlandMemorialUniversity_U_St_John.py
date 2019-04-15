# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/10/29 9:39'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from lxml import etree
import requests

class NewfoundlandMemorialUniversity_U_St_JohnSpider(scrapy.Spider):
    name = 'NewfoundlandMemorialUniversity_U_St_John'
    allowed_domains = ['mun.ca/']
    start_urls = []
    C= [
        'http://www.mun.ca/undergrad/programs/hss/anthropology.php',
        'http://www.mun.ca/undergrad/programs/science/applied-math.php',
        'http://www.mun.ca/undergrad/programs/hss/archaeology.php',
        'http://www.mun.ca/undergrad/programs/science/neuroscience.php',
        'http://www.mun.ca/undergrad/programs/science/biochemistry.php',
        'http://www.mun.ca/undergrad/programs/science/biology.php',
        'http://www.mun.ca/undergrad/programs/business/bba.php',
        'http://www.mun.ca/undergrad/programs/science/chemistry.php',
        'http://www.mun.ca/undergrad/programs/engineering/civil.php',
        'http://www.mun.ca/undergrad/programs/hss/classics.php',
        'http://www.mun.ca/undergrad/programs/business/bcomm.php',
        'http://www.mun.ca/undergrad/programs/hss/communication.php',
        'http://www.mun.ca/undergrad/programs/engineering/computer.php',
        'http://www.mun.ca/undergrad/programs/science/computer-science.php',
        'http://www.mun.ca/undergrad/programs/science/computer-science.php',
        'http://www.mun.ca/undergrad/programs/science/earth-sciences.php',
        'http://www.mun.ca/undergrad/programs/hss/economics.php',
        'http://www.mun.ca/undergrad/programs/hss/economics.php',
        'https://www.mun.ca/undergrad/programs/education/bed-pe.php',
        'https://www.mun.ca/undergrad/programs/education/bsped.php',
        'http://www.mun.ca/undergrad/programs/engineering/electrical.php',
        'http://www.mun.ca/undergrad/programs/hss/english.php',
        'http://www.mun.ca/undergrad/programs/hss/folklore.php',
        'http://www.mun.ca/undergrad/programs/hss/french.php',
        'http://www.mun.ca/undergrad/programs/hss/gender.php',
        'http://www.mun.ca/undergrad/programs/hss/geography.php',
        'http://www.mun.ca/undergrad/programs/hss/geography.php',
        'http://www.mun.ca/undergrad/programs/hss/german.php',
        'http://www.mun.ca/undergrad/programs/hss/history.php',
        'http://www.mun.ca/undergrad/programs/hkr/bhkr.php',
        'http://www.mun.ca/undergrad/programs/business/ibba.php',
        'http://www.mun.ca/undergrad/programs/hkr/bkin.php',
        'http://www.mun.ca/undergrad/programs/hss/law-society.php',
        'http://www.mun.ca/undergrad/programs/hss/linguistics.php',
        'http://www.mun.ca/undergrad/programs/science/marine.php',
        'http://www.mun.ca/undergrad/programs/engineering/mechanical.php',
        'http://www.mun.ca/undergrad/programs/hss/medieval.php',
        'http://www.mun.ca/undergrad/programs/music/',
        'http://www.mun.ca/undergrad/programs/science/nutrition.php',
        'http://www.mun.ca/undergrad/programs/engineering/ocean-naval.php',
        'http://www.mun.ca/undergrad/programs/science/ocean-sciences.php',
        'http://www.mun.ca/undergrad/programs/science/environmental-systems.php',
        'http://www.mun.ca/undergrad/programs/hss/philosophy.php',
        'http://www.mun.ca/undergrad/programs/hkr/bpe.php',
        'http://www.mun.ca/undergrad/programs/science/physics.php',
        'http://www.mun.ca/undergrad/programs/hss/police.php',
        'http://www.mun.ca/undergrad/programs/hss/polisci.php',
        'http://www.mun.ca/undergrad/programs/engineering/process.php',
        'http://www.mun.ca/undergrad/programs/science/psychology.php',
        'http://www.mun.ca/undergrad/programs/science/psychology.php',
        'http://www.mun.ca/undergrad/programs/science/pure-math.php',
        'http://www.mun.ca/undergrad/programs/science/pure-math.php',
        'http://www.mun.ca/undergrad/programs/hkr/brec.php',
        'http://www.mun.ca/undergrad/programs/hss/religious-studies.php',
        'http://www.mun.ca/undergrad/programs/hss/russian.php',
        'http://www.mun.ca/undergrad/programs/socwrk/',
        'http://www.mun.ca/undergrad/programs/hss/sociology.php',
        'http://www.mun.ca/undergrad/programs/hss/spanish.php',
        'http://www.mun.ca/undergrad/programs/science/stats.php',
        'http://www.mun.ca/undergrad/programs/science/stats.php'
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
        major_name_en_a = response.xpath("//h1[@class='page-title']").extract()
        major_name_en_a = ''.join(major_name_en_a)
        major_name_en_a = remove_tags(major_name_en_a).replace('amp;','')
        if 'Bachelor of' in major_name_en_a:
            major_name_en = major_name_en_a.replace('Bachelor of','').strip()
        else:
            major_name_en = major_name_en_a
        # print(major_name_en)

        #4.campus
        campus = "St. John's Campus"

        #5.location
        location = 'St.Johns City,Newfoundland'

        #6.department
        department = response.xpath("//h6[contains(text(),'Faculty/School:')]//following-sibling::p[1]").extract()
        department = ''.join(department)
        department = remove_tags(department).strip()
        # print(department)

        #7.degree_name
        degree_name = response.xpath("//h6[contains(text(),'Degree:')]//following-sibling::p[1]").extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name).strip()
        # print(degree_name)
        if len(degree_name)==0:
            degree_name = major_name_en_a
        # print(degree_name)

        #8.duration #34.duration_per
        duration = response.xpath("//p[contains(text(),'4 years')]").extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        # print(duration)
        try:
            duration = re.findall('\d',duration)[0]
            duration_per = 1
        except:
            if 'Bachelor of Social Work' in degree_name:
                duration = 4
                duration_per = 1
            elif 'Bachelor of Commerce (co-operative)' in degree_name:
                duration = 5
                duration_per = 1
            elif 'Bachelor of Education (Primary/Elementary)' in degree_name:
                duration = 5
                duration_per = 1
            elif 'Bachelor of Special Education' in degree_name:
                duration = 3
                duration_per = 2
            else:
                duration = 4
                duration_per = 1
        # print(duration,'----',duration_per)

        #9.deadline
        deadline = response.xpath("//h6[contains(text(),'Application Deadline')]//following-sibling::*").extract()
        deadline = ''.join(deadline)
        deadline = remove_tags(deadline)
        if 'rolling basis' in deadline:
            deadline = '2019-02-01,2019-03-01,2019-10-01'
        else:
            if 'Behavioural Neuroscience' in major_name_en:
                deadline = '2019-06-01'
            elif 'Bachelor of Special Education' in major_name_en:
                deadline = '2019-01-15'
            elif 'Bachelor of Education (Primary/Elementary)' in major_name_en:
                deadline = '2019-01-15'
            elif 'Bachelor of Music' in major_name_en:
                deadline = '2019-01-15'
            elif 'International Bachelor of Business Administration' in major_name_en:
                deadline =  '2019-02-01,2019-03-01,2019-10-01'
            elif 'Psychology' in major_name_en:
                deadline = '2019-06-01'
            else:
                deadline = '2019-03-01'
        # print(deadline)

        #10.overview_en
        overview_en = response.xpath("//div[@class='col-md-8']//p[1]").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)

        #11.modules_en
        modules_en = response.xpath("//h3[contains(text(),'Sample')]//following-sibling::p[1]|//h3[contains(text(),'Sample')]//following-sibling::ul[1]").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en,url)

        #12.career_en
        career_en = response.xpath("//h3[contains(text(),'Career')]//following-sibling::ul[1]|//h3[contains(text(),'Career')]//following-sibling::p[1]").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        if len(career_en)==0:
            career_en= None
        # print(career_en)

        #13.entry_requirements_en
        entry_requirements_en = '<p>To be eligible for admission as an international high school student, you must have graduated from a recognized university preparatory program with acceptable senior level courses in five subject areas, which normally include: English, mathematics, a laboratory science, a social science and one other subject area. Admission requirements may vary depending on the educational system(s) in place in your country. Visit the Admissions Requirements page to see application and admission requirements, by country, including details about: Credentials, certificates, or transcripts required; Subject areas and minimum grades;  English proficiency; and Document submission requirements</p>'


        #14.require_chinese_en
        require_chinese_en = '<p>Credential Senior Secondary School Certificate ,Required Subject Areas English Mathematics* Laboratory Science* (Biology, Chemistry, or Physics) Social Studies or Modern/Classical Language Elective</p>'

        #15.average_score
        average_score = 75

        #16.ielts_desc 171819
        ielts_desc = 'A minimum overall band score of 6.5, with at least a band 6 in reading and writing.'
        ielts = 6.5
        ielts_r = 6
        ielts_w = 6

        #20.toefl_desc 2122232425
        toefl_desc = 'A minimum score of 550 on the paper-based test, or 79 on the internet-based TOEFL (iBT) with a minimum score of 20 in reading and writing, and not less than 17 in listening and speaking.'
        toefl = 79
        toefl_r = 20
        toefl_w = 20
        toefl_l = 17
        toefl_s = 17

        #26.tuition_fee
        tuition_fee = '11,460'

        #27.tuition_fee_pre
        tuition_fee_pre = '$'

        #28.apply_pre
        apply_pre = '$'

        #29.apply_fee
        apply_fee = 120

        #30.ib
        ib = 'Minimum score of 24 on the IB Diploma with completion of the required subject areas or completion of another recognized High School diploma program. Please see your country’s specific requirements for more information.'

        #31.alevel
        alevel = 'Completion of the GCE including a minimum grade of C/4 in the required subject areas at the Ordinary (“O” or IGCSE) Level and at least three Advanced Subsidiary (“AS”) Level or two Advanced (“A”) Level subjects with a minimum grade of C. Exceptional candidates may be admitted based upon GCSE/IGCSE examination results.'

        #32.toefl_code
        toefl_code ='0885'

        #33.sat_code
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