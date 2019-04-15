# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/10/23 17:57'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from lxml import etree
import requests

class RyersonUniversity_USpider(scrapy.Spider):
    name = 'RyersonUniversity_U'
    allowed_domains = ['ryerson.ca/']
    start_urls = []
    C= [
        'https://www.ryerson.ca/programs/undergraduate/nursing-collaborative/',
        'https://www.ryerson.ca/programs/undergraduate/chemical-engineering-co-op/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)

        #1.school_name
        school_name = 'Ryerson University'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.major_name_en
        major_name_en_a = response.xpath("//div[contains(@class,'resPageHeadin')]//h1").extract()
        major_name_en_a = ''.join(major_name_en_a)
        major_name_en_a = remove_tags(major_name_en_a).strip()
        if '(' in major_name_en_a:
            major_name_en = re.findall('(.*?)\(',major_name_en_a)[0].strip().replace('amp;','')
        else:
            major_name_en = None
        # print(major_name_en)

        #4.degree_name
        degree_name = response.xpath("//strong[contains(text(),'Degree Earned')]//following-sibling::text()").extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name).strip()
        # print(degree_name,'----------')

        #5.overview_en
        overview_en = response.xpath("//h2[contains(text(),'Is It for You?')]//following-sibling::*").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #6.department
        department = response.xpath("//strong[contains(text(),'Faculty')]//following-sibling::*").extract()
        department = ''.join(department)
        department = remove_class(department).strip().replace('<br>','').replace('amp;','')
        # print(department)

        #7.duration #8.duration_per
        duration = 4
        duration_per = 1



        #10.tuition_fee
        tuition_fee = response.xpath("//div[contains(@class,'stackparsys')]//div[contains(@class,'parbase')]//div[contains(@class,'richtextContent')]").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = re.findall('\$(\d{2},\d{3})',tuition_fee)
        if len(tuition_fee)==1:
            tuition_fee =  tuition_fee[0]
        else:
            tuition_fee = str(tuition_fee[-2]) + '-' + str(tuition_fee[-1])
        # print(tuition_fee)

        #11.tuition_fee_pre
        tuition_fee_pre = '$'

        #12.entry_requirements_en
        entry_requirements_en = response.xpath("//a[contains(text(),'Requirements')]/../../following-sibling::*").extract()[0]
        entry_requirements_en = remove_class(entry_requirements_en).strip()
        entry_requirements_en = clear_space_str(entry_requirements_en)
        # print(entry_requirements_en)

        #13.modules_en
        modules_en_url = response.xpath("//span[contains(text(),'Program Courses')]//..//..//preceding-sibling::*//@href").extract()
        modules_en_url = ''.join(modules_en_url)
        modules_en_url = 'https://www.ryerson.ca' + modules_en_url
        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        data = requests.get(modules_en_url,headers=headers)
        response1 = etree.HTML(data.text)
        modules_en = response1.xpath("//a[@class='defaultSubTitle' and contains(text(),'Semester')]/../following-sibling::*//tbody")
        doc = ""
        if len(modules_en) > 0:
            for a in modules_en:
                doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
        modules_en = doc
        modules_en = clear_space_str(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        # 9.career_en
        career_en = response.xpath("//h2[contains(text(),'After Graduation')]//following-sibling::p").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en,'--------------')

        #14.ielts 15161718
        ielts = 6.5
        ielts_r = 6
        ielts_w = 6
        ielts_s = 6
        ielts_l = 6

        #19.toefl
        if 'Engineering' in department:
            toefl = '83-87'
        elif 'Faculty of Science' in department:
            toefl = '83-87'
        else:
            toefl = '92-93'

        #20.toefl_code,sat_coade
        toefl_code = '0886'
        sat_code = '0886'

        #22.require_chinese_en
        require_chinese_en = '<p>Senior High School (Upper Middle School) Graduation Diploma, Academic Proficiency Test/Upper Middle School Graduation (Hui Kao) Exam, and Chinese National University Entrance Examinations (Gao Kao). Applicants who have not written, or do not intend on writing the Gao Kao examination must submit a signed and dated letter providing the reason(s). Additional requirements include a notarized copy of Hui Kao (or equivalent test) results and results from any other standardized academic tests (e.g. SAT, ACT or AP tests). Copies of awards received for academic achievement as well as reference letters from school officials highlighting academic accomplishments are encouraged. Document Requirements:Interim Secondary A current transcript including any mid-term/mid-year results available, the grading scale, and the name of the diploma to be awarded upon completion of your studies. A school profile should accompany your transcript. Please also provide a letter indicating the date you will write the Gao Kao and proof of registration (if available).  If you have not written, or do not intend on writing the Gao Kao examination, you must submit a signed and dated letter providing the reason(s). Additional requirements include a notarized copy of your Hui Kao (or equivalent test) results and results from any other standardized academic tests (e.g. SAT, ACT or AP tests). Copies of awards received for academic achievement as well as reference letters from school officials highlighting academic accomplishments are encouraged.</p>'

        #23.ap
        ap = 'Graduation from Grade 12 of an academic program at an accredited secondary school with high academic standing including minimum B grades in the program-specific subject prerequisites and a minimum B overall average. Subject to competition, applicants may be required to present averages/grades above the minimum. In most cases, subject prerequisites should be completed at the AP level and/or Grade 12 senior academic level (some exceptions apply). The high school profile (including accreditation, grading scheme, etc.) must accompany the academic record. While we do not have minimum SAT or ACT score requirements, strong performance on a standardized test can strengthen an application. If SAT or ACT examinations have been written, the results should be submitted. Advanced Placement (AP) examination results will also be considered. AP courses with examination scores of 4 or higher will be considered for transfer credit on an individual basis. Engineering students are not eligible for transfer credits for core and professional engineering courses using AP examinations.'

        #24.alevel
        alevel = 'Ryerson University will accept GCE A/AS Levels and GCSE O Levels, as well as the Cambridge Pre-University Certificates or Diploma. BTEC qualifications [BTEC Higher Nationals Level 3, BTEC Higher National Certificate (HNC) Level 4, BTEC Higher National Diploma (HND) Level 5] will be considered for admission on an individual basis provided program specific subject requirements have been completed/are being completed at an appropriate level and the qualifications include sufficient academic content.GCE A Levels with grades of C or better or Pre-U Certificate (Principal Subjects) with grades of M3 or higher, may be considered for transfer credit on an individual basis. No transfer credit is given for AS Levels. Engineering students are not eligible for transfer credits for core and professional engineering courses using GCE A Levels or Pre-U Certificate (Principal Subjects).'

        #25.deadline
        deadline = '2019-02-01'

        #26.location
        location = 'Toronto'

        #27.average_score
        average_score = response.xpath("//div[@class='res-text richtextContent background-opaque']/p[contains(text(),'%')]").extract()
        average_score = ''.join(average_score)
        average_score = remove_tags(average_score)
        try:
            average_score = re.findall('(\d+.*)',average_score)[0]
        except:
            average_score = None

        #28.gaokao_desc 29.huikao_desc
        gaokao_desc = 'Senior High School (Upper Middle School) Graduation Diploma, Academic Proficiency Test/Upper Middle School Graduation (Hui Kao) Exam, and Chinese National University Entrance Examinations (Gao Kao). Applicants who have not written, or do not intend on writing the Gao Kao examination must submit a signed and dated letter providing the reason(s). Additional requirements include a notarized copy of Hui Kao (or equivalent test) results and results from any other standardized academic tests (e.g. SAT, ACT or AP tests). Copies of awards received for academic achievement as well as reference letters from school officials highlighting academic accomplishments are encouraged.A notarized copy of your final Chinese Upper Middle School transcript and graduation diploma are required along with a notarized copy of your Hui Kao (or equivalent test) results and your Gao Kao results verified by China Academic Degrees and Graduate Education Development Centre (CDGDC), external link or China Credentials Verification (CHESICC-Parchment Portal Service), external link. Results from any other standardized academic tests written (e.g. SAT, ACT or AP tests) must also be submitted. If you have not, and will not be sitting for the Gao Kao exam, you must submit a signed and dated letter providing the reason(s).'
        huikao_desc = gaokao_desc




        item['average_score'] = average_score
        item['gaokao_desc'] = gaokao_desc
        item['huikao_desc'] = huikao_desc
        item['location'] = location
        item['school_name'] = school_name
        item['url'] = url
        item['major_name_en'] = major_name_en
        item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['department'] = department
        item['duration_per'] = duration_per
        item['duration'] = duration
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['entry_requirements_en'] = entry_requirements_en
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl'] = toefl
        item['toefl_code'] = toefl_code
        item['sat_code'] = sat_code
        item['require_chinese_en'] = require_chinese_en
        item['ap'] = ap
        item['alevel'] = alevel
        item['deadline'] = deadline
        yield item