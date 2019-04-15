# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/10/22 10:20'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from lxml import etree
import requests

class WilfridLaurierUniversity_USpider(scrapy.Spider):
    name = 'WilfridLaurierUniversity_U'
    allowed_domains = ['wlu.ca/']
    start_urls = []
    C= [
        'https://www.wlu.ca/programs/arts/undergraduate/ancient-studies-ba/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/applied-water-science-bsc/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/languages-ba/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/archaeology-and-heritage-studies-ba/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/biochemistry-biotechnology-bsc/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/biology-bsc/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/biology-ba/index.html',
        'https://www.wlu.ca/programs/business-and-economics/undergraduate/business-administration-bba/index.html',
        'https://www.wlu.ca/programs/business-and-economics/undergraduate/business-technology-management-bbtm/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/chemistry-bsc/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/chemistry-and-physics-bsc/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/communication-studies-ba/index.html',
        'https://www.wlu.ca/programs/human-and-social-sciences/undergraduate/community-health-ba/index.html',
        'https://www.wlu.ca/programs/music/undergraduate/community-music-bmus/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/computer-science-bsc-milton/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/computer-science-bsc/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/computer-science-and-physics-bsc/index.html',
        'https://www.wlu.ca/programs/human-and-social-sciences/undergraduate/criminology-ba/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/data-science-bsc-milton/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/data-science-bsc/index.html',
        'https://www.wlu.ca/programs/liberal-arts/undergraduate/digital-media-and-journalism-ba/index.html',
        'https://www.wlu.ca/programs/business-and-economics/undergraduate/economics-ba/index.html',
        'https://www.wlu.ca/programs/business-and-economics/undergraduate/economics-and-accounting-ba/index.html',
        'https://www.wlu.ca/programs/business-and-economics/undergraduate/economics-and-financial-management-ba/index.html',
        'https://www.wlu.ca/programs/liberal-arts/undergraduate/english-ba/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/english-ba/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/environmental-science-bsc/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/environmental-studies-ba/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/film-studies-ba/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/financial-mathematics-ba/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/financial-mathematics-bsc/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/french-ba/index.html',
        'https://www.wlu.ca/programs/human-and-social-sciences/undergraduate/game-design-and-development-bfaa/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/geography-ba/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/geography-bsc/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/languages-ba/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/global-studies-ba/index.html',
        'https://www.wlu.ca/programs/human-and-social-sciences/undergraduate/health-administration-ba/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/health-sciences-bsc/index.html',
        'https://www.wlu.ca/programs/liberal-arts/undergraduate/history-ba/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/history-ba/index.html',
        'https://www.wlu.ca/programs/liberal-arts/undergraduate/human-rights-and-human-diversity-ba/index.html',
        'https://www.wlu.ca/programs/liberal-arts/undergraduate/humanities-with-leadership-foundations-ba/index.html',
        'https://www.wlu.ca/programs/education/undergraduate/international-education-studies-ba/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/languages-ba/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/kinesiology-bkin/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/languages-ba/index.html',
        'https://www.wlu.ca/programs/liberal-arts/undergraduate/law-and-society-ba/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/mathematics-ba/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/mathematics-bsc/index.html',
        'https://www.wlu.ca/programs/music/undergraduate/music-bmus/index.html',
        'https://www.wlu.ca/programs/music/undergraduate/music-bmt/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/philosophy-ba/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/physics-bsc/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/political-science-ba/index.html',
        'https://www.wlu.ca/programs/human-and-social-sciences/undergraduate/psychology-ba/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/psychology-ba/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/psychology-bsc/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/psychology-and-neuroscience-bsc/index.html',
        'https://www.wlu.ca/programs/human-and-social-sciences/undergraduate/public-health-basc/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/religion-and-culture-ba/index.html',
        'https://www.wlu.ca/programs/science/undergraduate/science-bsc-waterloo/index.html',
        'https://www.wlu.ca/programs/liberal-arts/undergraduate/social-and-environmental-justice-ba/index.html',
        'https://www.wlu.ca/programs/social-work/undergraduate/social-work-bsw/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/sociology-ba/index.html',
        'https://www.wlu.ca/programs/arts/undergraduate/spanish-ba/index.html',
        'https://www.wlu.ca/programs/liberal-arts/undergraduate/user-experience-design-bdes/index.html',
        'https://www.wlu.ca/programs/liberal-arts/undergraduate/youth-and-childrens-studies-ba/index.html'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)

        #1.school_name
        school_name = 'Wilfrid Laurier University'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.major_name_en
        major_name_en_a = response.xpath("//div[@class='page-title']//h1").extract()[0]
        major_name_en_a = remove_tags(major_name_en_a)
        # print(major_name_en_a)
        if '(' in major_name_en_a:
            major_name_en = re.findall('(.*?)\(',major_name_en_a)[0]
            # print(major_name_en)
        elif "BA + Master's in English, History or Political Science" in major_name_en_a:
            major_name_en = "English, History or Political Science"
        else:
            major_name_en = None
        major_name_en = major_name_en.strip()
        # print(major_name_en)

        #4.degree_name
        if '(' in major_name_en_a:
            degree_name = re.findall('\((.*?)\)',major_name_en_a)[0]
            degree_name = degree_name.strip()
        elif "BA + Master's in English, History or Political Science" in major_name_en_a:
            degree_name = 'BA + Master'
        else:
            degree_name = None
        # print(degree_name)

        #5.location
        location = response.xpath("//span[@class='program-location']//text()").extract()
        location = ''.join(location).strip()
        location = remove_tags(location)
        if 'online' in location:
            location = 'waterloo'
        # print(location,url)

        #6.campus
        campus = location

        #7.department
        department = response.xpath("//*[@class='faculty-links']//text()").extract()
        department = ''.join(department)
        department = remove_tags(department).strip()
        if 'International Education Studies' in major_name_en:
            department = 'Faculty of Education|Faculty of Arts'
        # print(department,url)

        #8.overview_en
        overview_en_url = url.replace('index.html', 'program-details.html')
        # print(career_en_url)
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data = requests.get(overview_en_url, headers=headers)
            response1 = etree.HTML(data.text)
            overview_en = response1.xpath("//div[contains(@class,'contentColumn')]")
            if len(overview_en)==0:
                overview_en_url = url.replace('index.html', 'program-details/index.html')
                data3 = requests.get(overview_en_url, headers=headers)
                response3 = etree.HTML(data3.text)
                overview_en = response3.xpath("//div[contains(@class,'contentColumn')]")
            doc1 = ""
            if len(overview_en) > 0:
                for a in overview_en:
                    doc1 += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc1 = remove_class(doc1)
        except:
            doc1 = None

        #9.modules_en
        modules_en = response.xpath("//*[contains(text(),'Sample Courses')]/following-sibling::*").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en).strip()
        # print(modules_en)

        #10.entry_requirements_en
        entry_requirements_en = response.xpath("//*[contains(text(),'Requirements')]/following-sibling::ul[1]").extract()
        entry_requirements_en = ''.join(entry_requirements_en)
        entry_requirements_en = remove_class(entry_requirements_en).strip()
        # print(entry_requirements_en,'------------------------------')

        #11.career_en/doc
        career_en_url = url.replace('index.html','careers.html')
        # print(career_en_url)
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data = requests.get(career_en_url,headers= headers)
            response1 = etree.HTML(data.text)
            career_en = response1.xpath("//h2[contains(text(),'Sample Career Options')]//following-sibling::*")
            if len(career_en)==0:
                career_en = response1.xpath("//h2[contains(text(),'SAMPLE CAREER OPTIONS')]//following-sibling::*")
            if len(career_en)==0:
                career_en = response1.xpath("//div[@class='page-title']/../following-sibling::*")
            if len(career_en)==0:
                career_en_url = url.replace('index.html','careers/index.html')
                data2 = requests.get(career_en_url,headers= headers)
                response2 = etree.HTML(data2.text)
                career_en = response2.xpath("//h2[contains(text(),'Career Examples')]//following-sibling::*")
                if len(career_en) == 0:
                    career_en = response2.xpath("//div[contains(@class,'contentColum')]")
            doc = ""
            if len(career_en) > 0:
                for a in career_en:
                    doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc = remove_class(doc)
            if len(doc)==0:
                career_en = response.xpath("//h3[contains(text(),'Career')]//following-sibling::*").extract()
                career_en = ''.join(career_en)
                career_en = remove_class(career_en)
                doc = career_en
        except:
            doc = None

        #12.ib
        ib = response.xpath("//*[contains(text(),'Baccalaureate Requirements')]//following-sibling::ul").extract()
        ib = ''.join(ib)
        ib = remove_tags(ib)
        # print(ib,url,'----')

        #13.14.tuition_fee_pre,tuition_fee
        tuition_fee_pre = '$'
        tuition_fee = '24,104-29,637'

        #15.ielts_desc,1617181920
        ielts_desc = 'An academic score of 6.5 or higher with a minimum of 6.0 in each band.'
        ielts = 6.5
        ielts_r = 6.0
        ielts_s = 6.0
        ielts_l = 6.0
        ielts_w = 6.0

        #21.toefl_desc,2223242526
        toefl_desc = 'an overall score of 83 or higher with a minimum score of 20 in each component.'
        toefl = 83
        toefl_r = 20
        toefl_s = 20
        toefl_l = 20
        toefl_w = 20

        #27.28toefl_code,sat_code
        toefl_code = '0893'
        sat_code = '0893'

        #29.30apply_pre,apply_fee
        apply_pre = '$'
        apply_fee = 100

        #31.ap
        ap ='All prerequisites need to be at either the honours, Advanced Placement (AP) or senior level. '

        #32.act_code
        act_code = '5375'

        #33.act_desc
        act_desc = 'ACT and SAT scores are not required. Applicants can choose to submit their test score for admission consideration. In acknowledgement of the various grading scales used throughout the American Curriculum, the grading scale on the applicant’s transcript will be used, then grades will be converted to reflect a 50% pass rate. School profiles may be requested to verify course offerings and grading scale.'

        #34.require_chinese_en
        require_chinese_en = '<p>In acknowledgement of the various grading scales used throughout China, the grading scale on the transcript will be used:Grades are converted to 50% pass grade.</p>'

        #35.deadline
        deadline = '2019-04-01,2019-10,2019-03-18'

        item['school_name'] = school_name
        item['url'] = url
        item['major_name_en'] = major_name_en
        item['degree_name'] = degree_name
        item['location'] = location
        item['campus'] = campus
        item['department'] = department
        item['overview_en'] = doc1
        item['modules_en'] = modules_en
        item['entry_requirements_en'] = entry_requirements_en
        item['career_en'] = doc
        item['ib'] = ib
        item['tuition_fee_pre'] = tuition_fee_pre
        item['tuition_fee'] = tuition_fee
        item['ielts_desc'] = ielts_desc
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['ielts_w'] = ielts_w
        item['toefl_desc'] = toefl_desc
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['toefl_l'] = toefl_l
        item['toefl_s'] = toefl_s
        item['toefl_code'] = toefl_code
        item['sat_code'] = sat_code
        item['apply_pre'] = apply_pre
        item['apply_fee'] = apply_fee
        item['act_code'] = act_code
        item['ap'] = ap
        item['act_desc'] = act_desc
        item['deadline'] = deadline
        item['require_chinese_en'] = require_chinese_en
        yield item

