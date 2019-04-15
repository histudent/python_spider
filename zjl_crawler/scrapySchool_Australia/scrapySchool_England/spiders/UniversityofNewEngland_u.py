# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/31 14:47'
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
from scrapySchool_England.clearSpace import clear_space_str
import requests
from lxml import etree
from scrapySchool_England.translate_date import tracslateDate
from scrapySchool_England.getTuition_fee import getT_fee
class UniversityofNewEnglandSpider(scrapy.Spider):
    name = 'UniversityofNewEngland_u'
    allowed_domains = ['une.edu.au/']
    start_urls = []
    C= [
        'https://my.une.edu.au/courses/2019/courses/BACC',
        'https://my.une.edu.au/courses/2019/courses/BBUS',
        'https://my.une.edu.au/courses/2019/courses/BEDECP',
        'https://my.une.edu.au/courses/2019/courses/BEDSMT',
        'https://my.une.edu.au/courses/2019/courses/BURP',
        'https://my.une.edu.au/courses/2019/courses/HBPH1',
        'https://my.une.edu.au/courses/2019/courses/BSUS',
        'https://my.une.edu.au/courses/2019/courses/BSOCWK',
        'https://my.une.edu.au/courses/2019/courses/BBIOSC',
        'https://my.une.edu.au/courses/2019/courses/BA',
        'https://my.une.edu.au/courses/2019/courses/BEDEC1',
        'https://my.une.edu.au/courses/2019/courses/HBPSYC',
        'https://my.une.edu.au/courses/2019/courses/BZOOL',
        'https://my.une.edu.au/courses/2019/courses/BSC',
        'https://my.une.edu.au/courses/2019/courses/BEDSMU',
        'https://my.une.edu.au/courses/2019/courses/BEDK6',
        'https://my.une.edu.au/courses/2019/courses/BGEOSC',
        'https://my.une.edu.au/courses/2019/courses/BEC',
        'https://my.une.edu.au/courses/2019/courses/BMUS',
        'https://my.une.edu.au/courses/2019/courses/BEDK12',
        'https://my.une.edu.au/courses/2019/courses/BENSC',
        'https://my.une.edu.au/courses/2019/courses/BAGPM',
        'https://my.une.edu.au/courses/2019/courses/BRURSC',
        'https://my.une.edu.au/courses/2019/courses/BMC',
        'https://my.une.edu.au/courses/2019/courses/BAUD',
        'https://my.une.edu.au/courses/2019/courses/BAGB',
        'https://my.une.edu.au/courses/2019/courses/BSOCSC',
        'https://my.une.edu.au/courses/2019/courses/BNURS',
        'https://my.une.edu.au/courses/2019/courses/BEDISC',
        'https://my.une.edu.au/courses/2019/courses/BLANG',
        'https://my.une.edu.au/courses/2019/courses/BLAW01',
        'https://my.une.edu.au/courses/2019/courses/BHIP',
        'https://my.une.edu.au/courses/2019/courses/BSCST',
        'https://my.une.edu.au/courses/2019/courses/BCRIM',
        'https://my.une.edu.au/courses/2019/courses/BEDSSC',
        'https://my.une.edu.au/courses/2019/courses/BLIB',
        'https://my.une.edu.au/courses/2019/courses/BEDPF',
        'https://my.une.edu.au/courses/2019/courses/BLS',
        'https://my.une.edu.au/courses/2019/courses/BIS',
        'https://my.une.edu.au/courses/2019/courses/BEDSA',
        'https://my.une.edu.au/courses/2019/courses/BAGR',
        'https://my.une.edu.au/courses/2019/courses/BILS',
        'https://my.une.edu.au/courses/2019/courses/BEDS',
        'https://my.une.edu.au/courses/2019/courses/BLAWS',
        'https://my.une.edu.au/courses/2019/courses/BCOMP',
        'https://my.une.edu.au/courses/2019/courses/BCEP',
        'https://my.une.edu.au/courses/2019/courses/BAGREC',
        'https://my.une.edu.au/courses/2019/courses/BPSYSC',
        'https://my.une.edu.au/courses/2019/courses/BEXSS'
    ]
    # print(len(C))
    C =set(C)
    # print(len(C))
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of New England'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.degree_name
        degree_name = response.xpath('//*[@id="main-content"]/div/h2').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        degree_name = clear_space_str(degree_name)
        # print(degree_name)

        #4.degree_overview_en
        degree_overview_en = response.xpath("//h4[contains(text(),'Career Opportunities')]//preceding-sibling::p").extract()
        degree_overview_en = ''.join(degree_overview_en)
        degree_overview_en = remove_class(degree_overview_en)
        # print(degree_overview_en)

        #5.programme_en
        programme_en = degree_name.replace('Bachelor of ','')
        # if '/' in programme_en:
            # print(url)
        # print(programme_en,response.url)

        #6.career_en
        career_en = response.xpath("//h4[contains(text(),'Career Opportunities')]//following-sibling::p").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #7.duration
        duration = response.xpath('//*[@id="overviewTab-snapshotDiv"]/p[1]').extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        duration = clear_space_str(duration)
        if '4 Years Full-time' in duration:
            duration = 4
        elif '3 Years Full-time' in duration:
            duration = 3
        elif '5 Years Full-time' in duration:
            duration = 5
        elif '1 Year Full-time' in duration:
            duration = 1
        elif '2.5 or 3 Years Full-time' in duration:
            duration = 2.5,3
        elif '2.5 Years Full-time' in duration:
            duration = 2.5
        elif '2 Years Full-time' in duration:
            duration = 2
        elif '1.5 or 3 Years Full-time' in duration:
            duration = 1.5,3
        elif '4 or 3.5 or 2.5 Years Full-time' in duration:
            duration = 4,3.5,2.5
        else:duration = duration
        # print(duration)

        #8.degree_type
        degree_type = 1

        #9.rntry_requirements_en
        rntry_requirements_en = response.xpath("//*[contains(text(),'Entry Requirements')]//following-sibling::*").extract()
        rntry_requirements_en = ''.join(rntry_requirements_en)
        rntry_requirements_en = remove_class(rntry_requirements_en)
        # print(rntry_requirements_en)

        #10.modules_en
        try:
            modules_en_url = response.xpath("//*[contains(text(),'Program of Study')]//following-sibling::p//@href").extract()[0]
        except:
            modules_en_url = []
        if len(modules_en_url)>0:
            modules_en_url = 'https://my.une.edu.au/courses/2019/courses/'+modules_en_url
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        try:
            data = requests.get(modules_en_url, headers=headers)
            response1 = etree.HTML(data.text)
            modules_en = response1.xpath('//*[@id="main-content"]//table[1]')
            doc = ""
            if len(modules_en) > 0:
                for a in modules_en:
                    doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc = remove_class(doc)
                    modules_en = doc
        except:
            modules_en = None
        # print(modules_en)

        #11.location
        location = response.xpath("//*[contains(text(),'Mode of Study')]/../following-sibling::tr[1]//td[1]").extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #12.deadline
        deadline = ''

        #13.tuition_fee_pre
        tuition_fee_pre = '$'

        #14.apply_pre
        apply_pre = '$'

        #15.ielts 16171819  20.toefl 21222324
        ielts = 6.0
        ielts_r = 5.5
        ielts_w = 5.5
        ielts_s = 5.5
        ielts_l = 5.5
        toefl = 79
        toefl_r = 22
        toefl_w = 22
        toefl_s = 22
        toefl_l = 22

        #25.tuition_fee
        list1 = ['Advanced Diploma in Arts',
'Advanced Diploma in Local, Family and Applied History',
'Associate Degree in Teaching (Pacific Focus)',
'Bachelor of Accounting',
'Bachelor of Agribusiness',
'Bachelor of Agribusiness with Honours',
'Bachelor of Agricultural and Resource Economics',
'Bachelor of Agriculture',
'Bachelor of Agriculture/Bachelor of Business',
'Bachelor of Agriculture/Bachelor of Laws',
'Bachelor of Agricultural Production and Management',
'Bachelor of Animal Science',
'Bachelor of Arts',
'Bachelor of Arts with Honours',
'Bachelor of Arts/Bachelor of Business',
'Bachelor of Arts/Bachelor of Laws',
'Bachelor of Arts/Bachelor of Science',
'Bachelor of Audiometry',
'Bachelor of Biomedical Science',
'Bachelor of Business',
'Bachelor of Business/Bachelor of Economics',
'Bachelor of Business/Bachelor of Laws',
'Bachelor of Clinical Exercise Physiology',
'Bachelor of Computer Science',
'Bachelor of Computer Science with Honours',
'Bachelor of Computer Science/Bachelor of Laws',
'Bachelor of Criminology',
'Bachelor of Criminology with Honours',
'Bachelor of Criminology/Bachelor of Laws',
'Bachelor of Economics',
'Bachelor of Economics with Honours',
'Bachelor of Economics/Bachelor of Laws',
'Bachelor of Education (Early Childhood Teaching)',
'Bachelor of Education (Pacific Focus)',
'Bachelor of Education (Secondary Arts)',
'Bachelor of Education (Secondary Mathematics)',
'Bachelor of Education (Secondary Science)',
'Bachelor of Educational Studies',
'Bachelor of Environmental Science',
'Bachelor of Environmental Science/Bachelor of Laws',
'Bachelor of Exercise & Sport Science',
'Bachelor of GeoScience',
'Bachelor of Historical Inquiry and Practice',
'Bachelor of International Studies',
'Bachelor of International Studies with Honours',
'Bachelor of Languages',
'Bachelor of Languages and International Business',
'Bachelor of Laws (3 Years)',
'Bachelor of Laws (4 Years)',
'Bachelor of Media and Communications',
'Bachelor of Media and Communications with Honours',
'Bachelor of Music',
'Bachelor of Music with Honours',
'Bachelor of Nursing',
'Bachelor of Nursing',
'Bachelor of Nursing with Honours',
'Bachelor of Organisational Leadership',
'Bachelor of Pharmacy with Honours',
'Bachelor of Psychological Science',
'Bachelor of Psychology with Honours',
'Bachelor of Rural Science',
'Bachelor of Science',
'Bachelor of Science with Honours',
'Bachelor of Science/Bachelor of Laws',
'Bachelor of Scientific Studies',
'Bachelor of Social Science',
'Bachelor of Social Science with Honours',
'Bachelor of Social Work',
'Bachelor of Sustainability',
'Bachelor of Training and Development',
'Bachelor of Urban and Regional Planning',
'Bachelor of Zoology']
        list2 = ['24,990',
'24,990',
'24,990',
'26,250',
'26,250',
'26,250',
'26,250',
'29,400',
'29,400',
'29,400',
'29,400',
'29,400',
'24,990',
'24,990',
'26,250',
'26,250',
'29,400',
'26,250',
'29,400',
'26,250',
'26,250',
'26,250',
'29,400',
'29,400',
'29,400',
'29,400',
'26,250',
'26,250',
'26,250',
'26,250',
'26,250',
'26,250',
'24,990',
'24,990',
'24,990',
'24,990',
'27,300',
'24,990',
'29,400',
'29,400',
'29,400',
'29,400',
'24,990',
'24,990',
'24,990',
'24,990',
'24,990',
'26,250',
'26,250',
'24,990',
'24,990',
'24,990',
'24,990',
'28,000',
'28,000',
'28,000',
'26,250',
'29,400',
'28,000',
'28,000',
'29,400',
'29,400',
'29,400',
'29,400',
'29,400',
'24,990',
'26,250',
'26,250',
'26,250',
'26,250',
'26,250',
'29,400']
        dict = {}
        for i in range(len(list1)):
            dict[list1[i]] = list2[i]
        tuition_fee = dict.get(degree_name)
        # print(tuition_fee)
        try:
            if ',' in tuition_fee:
                tuition_fee = tuition_fee.replace(',','')
        except:
            tuition_fee = tuition_fee
        # print(tuition_fee)

        #26.average_score
        average_score = 75

        #27.apply_documents_en
        apply_documents_en = '高中毕业证/在读证明 高中成绩单 语言成绩 护照 高考成绩单'

        #28.apply_desc_en
        apply_desc_en = '<p>Application Steps Complete the online applicationUNE will assess your completed application. If you meet academic requirements, a conditional or unconditional Offer Letter will be issued together with an International Offer Guide which contains essential information you need to know about studying at UNE, including how to accept your offer.If your admission application is not successful, UNE will advise you in writing.You may be required to undergo additional Genuine Temporary Entrant (GTE) assessment under the Streamlined Student Visa Framework (SSVF). Your Offer Letter will tell you if you are required to do this and once you have completed this additional assessment, UNE will advise you whether or not you can proceed with your admission. You must not pay any tuition fees prior to UNE advising of the outcome of your GTE assessment.When you are ready to accept your offer (you must have met all conditions in your offer letter first), you need to complete and sign the Offer Acceptance/COE Request Form and organize payment of fees as outlined in the International Offer Guide.UNE will process your acceptance and if you are coming to study on-campus, you will be issued with a Confirmation of Enrolment (CoE) for your visa application. If you are an online student, you will be sent online enrolment information.If you are coming to study on campus, you should arrange your travel and accommodation as soon as you have your Student Visa granted. You should let UNE International know of your arrival date so that we can arrange to pick you up from the airport or train station and take you to your accommodation. You should plan to arrive in enough time to attend the compulsory International Student Orientation and Enrolment prior to commencing your studies.</p>'

        item['university'] = university
        item['url'] = url
        item['degree_name'] = degree_name
        item['degree_overview_en'] = degree_overview_en
        item['programme_en'] = programme_en
        item['career_en'] = career_en
        item['duration'] = duration
        item['degree_type'] = degree_type
        item['rntry_requirements_en'] = rntry_requirements_en
        item['modules_en'] = modules_en
        item['location'] = location
        item['deadline'] = deadline
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_pre'] = apply_pre
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['tuition_fee'] = tuition_fee
        item['average_score'] = average_score
        item['apply_documents_en'] = apply_documents_en
        item['apply_desc_en'] = apply_desc_en
        yield  item