# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/12/20 10:20'
#NiagaraCollege_C.py
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.getItem import get_item
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from lxml import etree
import requests
class NiagaraCollege_CSpider(scrapy.Spider):
    name = 'NiagaraCollege_C'
    allowed_domains = ['niagaracollege.ca/']
    start_urls = []
    C= [
        'https://www.niagaracollege.ca/aft',
        'https://www.niagaracollege.ca/acp',
        'https://www.niagaracollege.ca/advlaw',
        'https://www.niagaracollege.ca/ad/',
        'https://www.niagaracollege.ca/abs',
        'https://www.niagaracollege.ca/bagd',
        'https://www.niagaracollege.ca/bsgp',
        'https://www.niagaracollege.ca/brew',
        'https://www.niagaracollege.ca/fp',
        'https://www.niagaracollege.ca/rtvp',
        'https://www.niagaracollege.ca/tvp',
        'https://www.niagaracollege.ca/bg',
        'https://www.niagaracollege.ca/bib',
        'https://www.niagaracollege.ca/bsm',
        'https://www.niagaracollege.ca/ba',
        'https://www.niagaracollege.ca/baa',
        'https://www.niagaracollege.ca/baac/',
        'https://www.niagaracollege.ca/bahr',
        'https://www.niagaracollege.ca/baib',
        'https://www.niagaracollege.ca/bam',
        'https://www.niagaracollege.ca/bascom',
        'https://www.niagaracollege.ca/crt',
        'https://www.niagaracollege.ca/cyc',
        'https://www.niagaracollege.ca/civil',
        'https://www.niagaracollege.ca/bee',
        'https://www.niagaracollege.ca/ccp',
        'https://www.niagaracollege.ca/cajs',
        'https://www.niagaracollege.ca/communitymentalhealth',
        'https://www.niagaracollege.ca/cet',
        'https://www.niagaracollege.ca/cp',
        'https://www.niagaracollege.ca/cpa',
        'https://www.niagaracollege.ca/cst',
        'https://www.niagaracollege.ca/cetech',
        'https://www.niagaracollege.ca/criticalcarenursing',
        'https://www.niagaracollege.ca/cift',
        'https://www.niagaracollege.ca/cm',
        'https://www.niagaracollege.ca/dh',
        'https://www.niagaracollege.ca/ece',
        'https://www.niagaracollege.ca/ecea',
        'https://www.niagaracollege.ca/eco',
        'https://www.niagaracollege.ca/easns',
        'https://www.niagaracollege.ca/elec',
        'https://www.niagaracollege.ca/elect',
        'https://www.niagaracollege.ca/elnc',
        'https://www.niagaracollege.ca/elnct',
        'https://www.niagaracollege.ca/ema',
        'https://www.niagaracollege.ca/et',
        'https://www.niagaracollege.ca/est',
        'https://www.niagaracollege.ca/em',
        'https://www.niagaracollege.ca/eshp',
        'https://www.niagaracollege.ca/fhp',
        'https://www.niagaracollege.ca/gamedev',
        'https://www.niagaracollege.ca/gas',
        'https://www.niagaracollege.ca/geo',
        'https://www.niagaracollege.ca/gerontology',
        'https://www.niagaracollege.ca/gd',
        'https://www.niagaracollege.ca/gta',
        'https://www.niagaracollege.ca/gtc',
        'https://www.niagaracollege.ca/hair',
        'https://www.niagaracollege.ca/healthcareleadership',
        'https://www.niagaracollege.ca/bbah',
        'https://www.niagaracollege.ca/bbahr',
        'https://www.niagaracollege.ca/bbaic',
        'https://www.niagaracollege.ca/hta',
        'https://www.niagaracollege.ca/htc',
        'https://www.niagaracollege.ca/hm',
        'https://www.niagaracollege.ca/htm',
        'https://www.niagaracollege.ca/hrm',
        'https://www.niagaracollege.ca/ia',
        'https://www.niagaracollege.ca/ibm',
        'https://www.niagaracollege.ca/lta',
        'https://www.niagaracollege.ca/ltc',
        'https://www.niagaracollege.ca/lc',
        'https://www.niagaracollege.ca/met',
        'https://www.niagaracollege.ca/mety',
        'https://www.niagaracollege.ca/mpt',
        'https://www.niagaracollege.ca/nsp',
        'https://www.niagaracollege.ca/otapa',
        'https://www.niagaracollege.ca/oae',
        'https://www.niagaracollege.ca/oam',
        'https://www.niagaracollege.ca/palliativecare',
        'https://www.niagaracollege.ca/paramed',
        'https://www.niagaracollege.ca/pt',
        'https://www.niagaracollege.ca/photography',
        'https://www.niagaracollege.ca/pet',
        'https://www.niagaracollege.ca/pety',
        'https://www.niagaracollege.ca/pf',
        'https://www.niagaracollege.ca/pfa',
        'https://www.niagaracollege.ca/pn',
        'https://www.niagaracollege.ca/pna',
        'https://www.niagaracollege.ca/psicbs',
        'https://www.niagaracollege.ca/psips',
        'https://www.niagaracollege.ca/pr',
        'https://www.niagaracollege.ca/rt',
        'https://www.niagaracollege.ca/rtft',
        'https://www.niagaracollege.ca/ret',
        'https://www.niagaracollege.ca/ssw',
        'https://www.niagaracollege.ca/sa',
        'https://www.niagaracollege.ca/smgt',
        'https://www.niagaracollege.ca/tesl/',
        'https://www.niagaracollege.ca/tmbd',
        'https://www.niagaracollege.ca/welt',
        'https://www.niagaracollege.ca/wbm',
        'https://www.niagaracollege.ca/wvt',
        'https://www.niagaracollege.ca/wvt'
    ]
    C= set(C)
    for i in C:
        start_urls.append(i)

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaCollegeItem)

        #1.school_name
        school_name = 'Niagara College'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.location
        location = 'Ontario, Canada'

        #4.major_name_en
        major_name_en = response.xpath('//*[@id="page-title"]/div[2]/div[2]/h3/span').extract()
        major_name_en = ''.join(major_name_en)
        major_name_en = remove_tags(major_name_en).replace('&amp; ','')
        # print(major_name_en)

        #5.programme_code
        programme_code = response.xpath("//span[contains(text(),'Code:')]//following-sibling::*").extract()
        programme_code = ''.join(programme_code)
        programme_code = remove_tags(programme_code)
        # print(programme_code)

        #6.department
        department = response.xpath('//*[@id="page-title"]/div[2]/div[1]/h2/div/a/span').extract()
        department = ''.join(department)
        department = remove_tags(department)
        if 'School of ' not in department:
            department = department.replace('School of','School of ')
        department  = department.replace('  ',' ')
        # print(department)

        #7.degree_name #8.degree_level
        degree_name = response.xpath("//span[contains(text(),'Credential Awarded:')]//following-sibling::*").extract()
        degree_name  = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        if 'Advanced Diploma' in degree_name:
            degree_name = 'Advanced Diploma'
            degree_level = 3
        elif 'Diploma' in degree_name:
            degree_name = 'Diploma'
            degree_level = 3
        elif 'Graduate Certificate' in degree_name:
            degree_name = 'Graduate Certificate'
            degree_level = 2
        else:
            degree_name = "Bachelor's Degree"
            degree_level = 1
        # print(degree_name)

        #9.duration #10.duration_per
        duration = response.xpath("//span[contains(text(),'Length:')]//following-sibling::*").extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        if 'Year' in duration:
            duration = re.findall('\d',duration)[0]
            duration_per = 1
        elif 'Months' in duration:
            duration = re.findall('\d+',duration)[0]
            duration_per = 3
        else:
            if '3' in duration:
                duration = 3
                duration_per = 2
            elif 'Four' in duration:
                duration = 4
                duration_per = 2
            elif 'Six' in duration:
                duration = 6
                duration_per = 2
            else:
                duration = None
                duration_per = None
        # print(duration,'########',duration_per)

        #11.start_date
        start_date = response.xpath('//*[@id="status-table"]//tr').extract()
        start_date = ''.join(start_date)
        start_date  = remove_tags(start_date)
        start_date = re.findall('([A-Za-z]+\s[0-9]+)Open',start_date)
        start_date = ','.join(start_date).replace('September 2019','2019-09').replace('January 2020','2020-01').replace('May 2020','2020-05').replace('January 2019','2019-01').replace('May 2019','2019-05')
        start_date = start_date.replace('Available','').replace('Closed','')
        # print(start_date)

        #12.campus
        campus = response.xpath("//span[contains(text(),'Campus:')]//following-sibling::*").extract()
        campus = ''.join(campus)
        campus = remove_tags(campus).replace('&amp; ','')
        # print(campus)

        #13.overview_en
        overview_en = response.xpath("//div[@class='program-overview']").extract()
        overview_en= ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #14.career_en
        career_en = response.xpath("//ul[@class='career-opp-list']").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #15.entry_requirements_en #16.specific_requirement_en
        entry_requirements_en_url = url +'admission-requirements/'
        # print(entry_requirements_en)
        if len(entry_requirements_en_url) != 0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data = requests.get(entry_requirements_en_url, headers=headers)
            response1 = etree.HTML(data.text)
            entry_requirements_en = response1.xpath('//*[@id="content"]/div[1]')
            specific_requirement_en = response1.xpath('//*[@id="content"]/div[2]')
            doc = ""
            doc1 = ""
            if len(entry_requirements_en) > 0:
                for a in entry_requirements_en:
                    doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc = remove_class(doc)
                    entry_requirements_en = doc
            else:
                entry_requirements_en = None
            if len(specific_requirement_en) > 0:
                for a in specific_requirement_en:
                    doc1 += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc1 = remove_class(doc1)
                    specific_requirement_en = doc1
            else:
                specific_requirement_en = None
        else:
            entry_requirements_en = None
            specific_requirement_en =None
        # print(entry_requirements_en)
        # print(specific_requirement_en)

        #17.modules_en
        modules_en_url = url + 'courses/'
        # print(modules_en_url)
        if len(modules_en_url) != 0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data2 = requests.get(modules_en_url, headers=headers)
            response2 = etree.HTML(data2.text)
            modules_en = response2.xpath('//table')
            doc2 = ""
            if len(modules_en) > 0:
                for a in modules_en:
                    doc2 += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc2 = remove_class(doc2)
                    modules_en = doc2
            else:
                modules_en = None
        else:
            modules_en = None
        # print(modules_en)

        #18.deadline
        deadline = '2019-02-01,2019-06-07,2019-11-01'

        #19.tuition_fee_pre
        tuition_fee_pre = "$"

        #20.tuition_fee
        if degree_level ==1:
            tuition_fee = '15,150'
        elif degree_level ==2:
            tuition_fee = '13,350'
        else:
            tuition_fee = '14,150'

        #21.apply_pre
        apply_pre = '$'

        #22.ielts 23242526
        if degree_level ==3:
            ielts = 6.0
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
        else:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_s = 6.0
            ielts_l = 6.0

        #23.toefl 2425
        if degree_level ==3:
            toefl = 79
            toefl_w = 20
            toefl_s = 20
        else:
            toefl = 79
            toefl_w = 22
            toefl_s = 22

        other = '1.申请费未找到。2.中国学生要求未找到'
        item['school_name'] = school_name
        item['url'] = url
        item['location'] = location
        item['major_name_en'] = major_name_en
        item['programme_code'] = programme_code
        item['department'] = department
        item['degree_name'] = degree_name
        item['degree_level'] = degree_level
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['start_date'] = start_date
        item['campus'] = campus
        item['overview_en'] = overview_en
        item['career_en'] = career_en
        item['entry_requirements_en'] = entry_requirements_en
        item['specific_requirement_en'] = specific_requirement_en
        item['modules_en'] = modules_en
        item['deadline'] = deadline
        item['tuition_fee_pre'] = tuition_fee_pre
        item['tuition_fee'] = tuition_fee
        item['apply_pre'] = apply_pre
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl'] = toefl
        item['toefl_s'] = toefl_s
        item['toefl_w'] = toefl_w
        item['other'] = other
        yield  item
