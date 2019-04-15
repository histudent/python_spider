# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/10/31 10:37'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from lxml import etree
import requests

class SimonFraserUniversity_USpider(scrapy.Spider):
    name = 'SimonFraserUniversity_U'
    allowed_domains = ['sfu.ca/']
    start_urls = []
    C= [
        'http://www.sfu.ca/students/admission/programs/a-z/l/labour-studies.html'
    ]
    C =set(C)
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)

        #1.school_name
        school_name = 'Simon Fraser University'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.major_name_en
        major_name_en = response.xpath("//div[@class='greyBanner']//h1").extract()
        major_name_en = ''.join(major_name_en)
        major_name_en = remove_tags(major_name_en)
        # print(major_name_en,url)

        #4.overview_en
        overview_en = response.xpath("//div[contains(@class,'cq-dd-paragraph intro')]//div/div|//div[contains(@class,'cq-colctrl-lt5-c0')]/div/div/p").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #5.degree_name
        degree_name = response.xpath("//h4[contains(text(),'VERVIEW') or contains(text(),'verview')]//following-sibling::p[last()]").extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        degree_name = clear_space_str(degree_name).replace('Degree: ','')
        if 'Bachelor of Arts' in degree_name and 'Bachelor of Business Administration' in degree_name:
            degree_name = 'Bachelor of Arts or Bachelor of Business Administration'
        elif 'Bachelor of Science degree' in degree_name and 'Bachelor of Business Administration' in degree_name:
            degree_name = 'Bachelor of Science degree or Bachelor of Business Administration'
        elif 'bachelor of environment' in degree_name and 'bachelor of business administration' in degree_name:
            degree_name = 'Bachelor of environment or Bachelor of business administration'
        elif 'Resource and Environmental Management' in major_name_en:
            degree_name = 'Bachelor of Environment'
        # print(degree_name)

        #6.career_en
        career_en = response.xpath("//h3[contains(text(),'Career possibilities')]/../../../..//following-sibling::*").extract()
        if len(career_en)==0:
            career_en = response.xpath("//h3[contains(text(),'Are you curious?')]/../../../..//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en).replace('<h3>Career possibilities</h3><p>The world is changing rapidly and you have no way of knowing the full range of career opportunities available to you in the future. Graduates of this program may end up in a range of occupations, including these:<br>','').replace('Not sure where to start? Career Services can help you explore your options and create possibilities.<br>','')
        career_en = clear_space_str(career_en)
        # print(career_en)

        #7.deadline
        deadline = '2019-01-31'

        #8.apply_fee
        apply_fee = '79.5'

        #9.apply_pre
        apply_pre = '$'

        #10.location
        location = 'Vancouver, British Columbia'

        #11.entry_requirements_en
        entry_requirements_en = '<p>Graduation from a university-preparatory program at a senior high school Submit a transcript which includes grades for all courses completed and final grades for the first semester of Senior Year. (An admission average is calculated on final year results.</p>'

        #12.require_chinese_en
        require_chinese_en = "<p>Senior Middle School Graduation Diploma Submit transcript which includes grades for all courses completed and final grades for the first semester of Senior Year 3. Admission is calculated on Senior Year 3 academic subjects. GaoKao Exam Offers of admission are conditional upon receipt of the GaoKao results in July. The required results will depend on the program. In lieu of the GaoKao, you may submit SAT (score of 1130 out of 1600) or ACT (Composite Score of 22) results. If you are following an IB curriculum, or completing GCE A-Levels, you do not need to submit GaoKao results. All applicants must meet the university's Quantitative and Analytical Skills requirements. You need a minimum of 70% in Senior Year 2 or Senior Year 3 Mathematics for admission (based on a 60% pass scale).</p>"

        #13.modules_en
        modules_en_url = response.xpath("//a[contains(text(),'program description') or contains(text(),'Program description') or contains(text(),'PROGRAM DESCRIPTION ')]/@href").extract()[0]
        # print(modules_en_url)
        if 'http://www.sfu.ca'in modules_en_url or 'https://www.sfu.ca'in modules_en_url:
            modules_en_url = modules_en_url.replace('http://www.sfu.ca','').replace('https://www.sfu.ca','')
        modules_en_url = 'http://www.sfu.ca' + modules_en_url
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        data = requests.get(modules_en_url, headers=headers)
        response1 = etree.HTML(data.text)
        modules_en = response1.xpath("//h2[contains(text(),'Program Requirements')]//following-sibling::div[position()<last()-2]")
        doc = ""
        if len(modules_en) > 0:
            for a in modules_en:
                doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                doc = clear_space_str(remove_class(doc))
                modules_en = doc
        else:
            modules_en = None
        # print(modules_en)
        #


        #判断是否拆分
        # modules_en_url = response.xpath(
        #     "//a[contains(text(),'program description') or contains(text(),'Program description') or contains(text(),'PROGRAM DESCRIPTION ')]/@href").extract()[
        #     0]
        # # print(modules_en_url)
        # if 'http://www.sfu.ca' in modules_en_url or 'https://www.sfu.ca' in modules_en_url:
        #     modules_en_url = modules_en_url.replace('http://www.sfu.ca', '').replace('https://www.sfu.ca', '')
        # modules_en_url = 'http://www.sfu.ca' + modules_en_url
        # headers = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        # data = requests.get(modules_en_url, headers=headers)
        # response1 = etree.HTML(data.text)
        # judge = response1.xpath('//*[@id="page-content"]/section/div[4]/div[1]/ul[1]//li')
        # doc1 = ""
        # if len(judge) > 0:
        #     for a in judge:
        #         doc1 += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
        #
        #         doc1 = clear_space_str(remove_class(doc1))
        #         # doc1 = re.findall('<li>.*?</li>',doc1)
        # else:
        #     doc1 =''
        # print(doc1,url)

        #judge2
        # judge2 = response.xpath('//*[@id="page-content"]/section/div[2]/div[2]/div[1]/div[2]/div/h4').extract()
        # print(judge2,url)

        #14.ap
        ap = 'Transfer credit and/or advanced standing are granted to students who complete AP examinations in certain transferable subjects and achieve a score of 4 or 5. Course challenge (credit by examination) is also available in some disciplines. '

        #15.ib
        ib = "Completion of IB Diploma Program including English A1 or A2 or English Literature and Performance (HL or SL) with a minimum grade of 3"

        #16.ielts_desc 1718192021
        ielts_desc = 'International English Language Testing System (IELTS - Academic) with a minimum overall band score of 6.5 with no part less than 6.0.'
        ielts = 6.5
        ielts_r = 6
        ielts_w = 6
        ielts_s = 6
        ielts_l = 6

        #22.toefl_desc 2324252627
        toefl_desc = 'TOEFL iBT (Test of English as a Foreign Language internet based test) with an overall score of 88 or better with a minimum score of 20 in each of the four components (listening, speaking, writing, reading)'
        toefl = 88
        toefl_l = 20
        toefl_w = 20
        toefl_s = 20
        toefl_r = 20

        #28.tuition_fee_pre
        tuition_fee_pre = '$'

        #29.tuition_fee
        if major_name_en =='Business':
            tuition_fee = '891.42/per unit'
        elif 'Engineering' in major_name_en:
            tuition_fee = '833.19/per unit'
        elif 'Computing' in major_name_en:
            tuition_fee  ='820.69/per unit'
        else:
            tuition_fee = '808.34/per unit'

        #30.toefl_code
        toefl_code = '0999'

        #31.sat_code
        sat_code = '0999'
        #32.campus
        campus = response.xpath("//h4[contains(text(),'Overview')]//following-sibling::*").extract()
        campus = ''.join(campus)
        # if 'either the Burnaby or Surrey campus' in campus:
        #     # print(major_name_en,'---','either the Burnaby or Surrey campus')
        # elif 'Surrey campus' in campus:
        #     # print(major_name_en,'---','Surrey campus')
        # elif 'Vancouver campus' in campus:
        #     # print(major_name_en,'---','Vancouver campus')
        # else:
        #     pass

        item['school_name'] = school_name
        item['url'] = url
        item['major_name_en'] = major_name_en
        item['overview_en'] = overview_en
        item['degree_name'] = degree_name
        item['career_en'] = career_en
        item['deadline'] = deadline
        item['apply_fee'] = apply_fee
        item['apply_pre'] = apply_pre
        item['location'] = location
        item['entry_requirements_en'] = entry_requirements_en
        item['require_chinese_en'] = require_chinese_en
        item['modules_en'] = modules_en
        item['ap'] = ap
        item['ib'] = ib
        item['ielts_desc'] = ielts_desc
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl_desc'] = toefl_desc
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['tuition_fee_pre'] = tuition_fee_pre
        item['tuition_fee'] = tuition_fee
        item['toefl_code'] = toefl_code
        item['sat_code'] = sat_code
        yield item