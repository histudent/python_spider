# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/10/15 13:47'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from lxml import etree
import requests

class UniversityofToronto_USpider(scrapy.Spider):
    name = 'UniversityofToronto_U'
    allowed_domains = ['utoronto.ca/']
    start_urls = []
    C= [
        'http://www.future.utoronto.ca/content/genome-biology',
        'http://www.future.utoronto.ca/content/geographic-information-systems',
        'http://www.future.utoronto.ca/content/geophysics',
        'http://www.future.utoronto.ca/content/geoscience',
        'http://www.future.utoronto.ca/content/hungarian-studies',
        'http://www.future.utoronto.ca/content/immunology',
        'http://www.future.utoronto.ca/content/international-relations',
        'http://www.future.utoronto.ca/content/kinesiology',
        'http://www.future.utoronto.ca/content/materials-engineering',
        'http://www.future.utoronto.ca/content/materials-science',
        'http://www.future.utoronto.ca/content/mechanical-engineering',
        'http://www.future.utoronto.ca/content/mineral-engineering',
        'http://www.future.utoronto.ca/content/music-faculty-music',
        'http://www.future.utoronto.ca/content/nanoscience',
        'http://www.future.utoronto.ca/content/near-and-middle-eastern-civilizations',
        'http://www.future.utoronto.ca/content/neuroscience',
        'http://www.future.utoronto.ca/content/nutritional-sciences',
        'http://www.future.utoronto.ca/content/accounting',
        'http://www.future.utoronto.ca/content/pathobiology',
        'http://www.future.utoronto.ca/content/pharmaceutical-chemistry',
        'http://www.future.utoronto.ca/content/philosophy-and-physics',
        'http://www.future.utoronto.ca/content/physical-and-environmental-geography',
        'http://www.future.utoronto.ca/content/architectural-studies',
        'http://www.future.utoronto.ca/content/planetary-science',
        'http://www.future.utoronto.ca/content/asian-literatures-and-cultures',
        'http://www.future.utoronto.ca/content/polish-language-and-literature',
        'http://www.future.utoronto.ca/content/polish-studies',
        'http://www.future.utoronto.ca/content/public-policy',
        'http://www.future.utoronto.ca/content/biology',
        'http://www.future.utoronto.ca/content/russian-language',
        'http://www.future.utoronto.ca/content/russian-literature-translation',
        'http://www.future.utoronto.ca/content/south-slavic-studies',
        'http://www.future.utoronto.ca/content/chemical-engineering',
        'http://www.future.utoronto.ca/content/chemical-physics',
        'http://www.future.utoronto.ca/content/christianity-and-culture',
        'http://www.future.utoronto.ca/content/christianity-and-education',
        'http://www.future.utoronto.ca/content/ukrainian-language-and-literature',
        'http://www.future.utoronto.ca/content/civil-engineering',
        'http://www.future.utoronto.ca/content/visual-studies',
        'http://www.future.utoronto.ca/content/computer-engineering',
        'http://www.future.utoronto.ca/content/creative-expressions-and-society',
        'http://www.future.utoronto.ca/content/czech-and-slovak-studies',
        'http://www.future.utoronto.ca/content/data-science-0',
        'http://www.future.utoronto.ca/content/diaspora-and-transnational-studies',
        'http://www.future.utoronto.ca/content/earth-and-environmental-systems-0',
        'http://www.future.utoronto.ca/content/earth-sciences',
        'http://www.future.utoronto.ca/content/economics-and-mathematics',
        'http://www.future.utoronto.ca/content/environmental-chemistry',
        'http://www.future.utoronto.ca/content/environmental-geosciences',
        'http://www.future.utoronto.ca/content/financial-economics'
    ]
    C = set(C)
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)

        #1.school_name
        school_name = 'University of Toronto'

        #2.url
        url = response.url
        # print(url)

        #3.location
        location = 'Toronto'

        #7.major_name_en
        major_name_en = response.xpath('//*[@class="node node-program-details clearfix"]/h2/a').extract()
        major_name_en = ''.join(major_name_en)
        major_name_en = remove_tags(major_name_en)
        major_name_en = major_name_en.strip()
        # print(major_name_en)

        #12.require_chinese_en

        #13.1415161718 ielts_desc
        ielts_desc = 'The minimum requirement is an overall band of 6.5, with no band below 6.0.'
        ielts = 6.5
        ielts_l = 6
        ielts_s = 6
        ielts_r = 6
        ielts_w = 6

        #19 20 21
        toefl_desc = 'Minimum Requirement: total score of 100 + 22 on Writing'
        toefl = 100
        toefl_w = 22

        #22.apply_fee 23 24
        apply_fee = 180
        apply_pre = '$'
        tuition_fee_pre = '$'

        #25 26
        toefl_code = '0982'
        sat_code = '0982'

        #27.deadline
        #28.IB
        ib = 'If you are currently  enrolled in or have completed the International Baccalaureate Diploma, here’s what you need to know about our admission requirements and transfer credit you may be eligible for.An International Baccalaureate Diploma, including English HL or SL is required for admission.Prerequisite courses can be presented at either the Standard or Higher Level. For programs with a Math prerequisite, Math SL or HL is required. “Math Studies” is not acceptable. A total score of 27, not including bonus points, is required for admission consideration. More competitive programs require a significantly higher score. If you are currently enrolled in the IB Diploma program, you must submit your predicted IB results (1-7 scale), confirmation that you are completing the full IB Diploma, a current transcript including any mid-term/mid-year results available, and complete the online self-reported grades form. If you are currently enrolled in the IB Certificate/Course program, you must submit your predicted IB results (1-7 scale), confirmation that you are completing the IB Certificate/Course program, a current transcript including any mid-term/mid-year results available; and importantly, the name of the matriculation certificate/diploma to be awarded upon completion of your studies.Final IB results must be sent to the University electronically by the International Baccalaureate Organization (IBO). '


        item['ib'] = ib
        item['toefl_code'] = toefl_code
        item['sat_code'] = sat_code
        item['apply_fee'] = apply_fee
        item['apply_pre'] = apply_pre
        item['tuition_fee_pre'] = tuition_fee_pre
        item["ielts_desc"] = ielts_desc
        item["ielts"]  = ielts
        item["ielts_l"] = ielts_l
        item["ielts_s"] = ielts_s
        item["ielts_r"] = ielts_r
        item["ielts_w"] = ielts_w
        item["toefl_desc"] = toefl_desc
        item["toefl"] = toefl
        item["toefl_w"] = toefl_w
        item['school_name'] = school_name
        item['url'] = url
        item['location'] = location
        item['major_name_en'] = major_name_en

        #5.department 需要循环yield
        #6.degree_name 需要循环yield
        #8.entry_requirements_en 需要循环yield
        #9.overview_en 需要循环yield
        #10.career_en 需要循环yield
        #11.modules_en 需要循环yield
        #4.campus 需要循环yield
        campus = response.xpath("//div/h3[@class='field-item even']").extract()

        degree_name = response.xpath("//h3[contains(text(),'Program')]//preceding-sibling::*[1]").extract()
        if len(degree_name)==0:
            degree_name = response.xpath("//*[contains(text(),'Program')]//preceding-sibling::*[1]").extract()

        entry_requirements_en = response.xpath("//h3[contains(text(),'Admissions Requirements')]//following-sibling::ul//li[1]").extract()
        if len(entry_requirements_en)==0:
            entry_requirements_en = response.xpath("//h3[contains(text(),'Admissions Requirements')]/../following-sibling::*//ul//li//p[1]").extract()
        if len(entry_requirements_en)==0:
            entry_requirements_en = response.xpath("//*[contains(text(),'Admissions Requirements')]//following-sibling::*//li[1]").extract()

        overview_en_url = response.xpath("//div[@class='field-items']//div[@class='field-item even']//*[contains(text(),'Learn more about')]//@href").extract()

        if len(campus) !=0:
            for i,j,k,l in zip(campus,degree_name,entry_requirements_en,overview_en_url):
                response_campus_a = remove_tags(i)

                if ',' in response_campus_a:
                    response_campus = response_campus_a.split(',')[0].strip()
                    if 'John H' in response_campus_a:
                        department = 'John H. Daniels Faculty of Architecture, Landscape and Design'
                    else:
                        department = response_campus_a.split(',')[-1].strip().replace('amp;','')
                    response_degree_name = remove_tags(j).strip()
                    response_entry_requirements_en = remove_class(k).strip()
                else:
                    response_campus = response_campus_a.strip()
                    department = ''
                    response_degree_name = remove_tags(j).strip()
                    response_entry_requirements_en = remove_class(k).strip()
                response_degree_name = response_degree_name.replace('amp;','')
                # print(response_campus,l)

                if 'St. George Campus' in response_campus:
                    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
                    data = requests.get(l, headers=headers)
                    response_s = etree.HTML(data.text)


                    overview_en = response_s.xpath("//*[contains(text(),'Introduction')]//following-sibling::p[position()<3]")
                    if len(overview_en)==0:
                        overview_en = response_s.xpath('//*[@id="block-system-main"]/div/div/div[1]/div/div[2]/div/p')
                    if len(overview_en)==0:
                        overview_en = response_s.xpath("//div[@class='content clearfix']//div[1]/div/p[1]")
                    response_overview = ''
                    if len(overview_en) > 0:
                        for a in overview_en:
                            response_overview += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                            response_overview = remove_class(response_overview)
                    if 'engineering' in url:
                        response_overview = '<p>U of T Engineering is a world-renowned faculty known for leading-edge research and discovery. Regardless of the program you choose, you will have access to U of T’s top-ranked professors and facilities, as well as a curriculum that is constantly evolving. We offer you the most interdisciplinary engineering education in Canada. You can tailor your degree through academic options, minors and certificates, adding breadth and depth to your studies. This academic flexibility starts in first year, with a choice of three different entry points: Core Programs (Core 8) TrackOne, Undeclared Engineering Science</p>'

                    modules_en = response_s.xpath("//div[contains(text(),'Completion')]//following-sibling::*")
                    # modules_en = response_s.xpath("//*[contains(text(),'Search Courses by Keyword')]/../../../../../../..//following-sibling::h3[contains(@class,'views-accordion')]")
                    # if len(modules_en)==0:
                    #     modules_en = response_s.xpath("//*[contains(text(),'First Year Courses')]//following-sibling::*[1]")
                    # if len(modules_en)==0:
                    #     modules_en = response_s.xpath("//div[contains(text(),'Completion')]//following-sibling::*")
                    # if len(modules_en)<20:
                    #     modules_en = response_s.xpath("//*[contains(text(),'First Year Courses')]//following-sibling::*")
                    # print(modules_en,url)
                    response_modules_en =''
                    if len(modules_en) > 0:
                        for a in modules_en:
                            response_modules_en += (
                            etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                            response_modules_en = remove_class(response_modules_en)


                    response_career_en = None

                elif 'Mississauga Campus' in response_campus:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
                    data = requests.get(l, headers=headers)
                    response_m = etree.HTML(data.text)


                    overview_en = response_m.xpath("//h2[contains(text(),'Programs & Requirements*')]//preceding-sibling::*")
                    response_overview = ''
                    if len(overview_en) > 0:
                        for a in overview_en:
                            response_overview += (
                            etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                            response_overview = remove_class(response_overview)



                    career_en = response_m.xpath("//*[contains(text(),'Careers by Major')]//following::*[position()<2]")
                    response_career_en = ''
                    if len(career_en) > 0:
                        for a in career_en:
                            response_career_en += (
                                etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                            response_career_en = remove_class(response_career_en)


                    response_modules_en = ''
                elif 'Scarborough Campus' in response_campus:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
                    data = requests.get(l, headers=headers)
                    response_sc = etree.HTML(data.text)


                    overview_en = response_sc.xpath("//div[@class='program_summary indent']//p")
                    response_overview = ''
                    if len(overview_en) > 0:
                        for a in overview_en:
                            response_overview += (
                                etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                            response_overview = remove_class(response_overview)

                    career_en_url = response_sc.xpath("//*[contains(text(),'Career Options')]//following-sibling::*//@href")
                    data2 = requests.get(career_en_url[0],headers=headers)
                    response_car = etree.HTML(data2.text)
                    career_en = response_car.xpath("//*[contains(text(),'Entry-Level')]//following-sibling::ul[1]")
                    response_career_en = ''
                    if len(career_en) > 0:
                        for a in career_en:
                            response_career_en += (
                                etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                            response_career_en = remove_class(response_career_en)


                    response_modules_en = None
                else:

                    response_career_en = None
                    response_modules_en = None
                    response_overview = None



                item['modules_en'] = response_modules_en
                item['career_en'] = response_career_en
                item['overview_en'] = response_overview
                item['campus'] = response_campus
                item['department'] = department
                item['degree_name'] = response_degree_name
                item['entry_requirements_en'] = response_entry_requirements_en

                if 'Engineering' in department or 'Engineering' in major_name_en:
                    require_chinese_en = 'Candidates studying in the Chinese High School system are required to present: Senior 3 level Math, Chemistry and Physics — if students are permitted to take only one science subject within their Gao Kao, we recommend Physics; Chemistry should be presented in Senior Year 3  Hui Kao: Chinese Upper Middle School Graduation Exam results (if available in your province)  Gao Kao: Chinese National University Entrance Examinations  Proof of English Facility may be required*'
                else:
                    require_chinese_en = 'Senior High School (Upper Middle School) Graduation Diploma and Academic Proficiency Test/Upper Middle School Graduation (Hui Kao) Exam and  Chinese National University Entrance Examinations (Gao Kao)'
                item['require_chinese_en'] = require_chinese_en

                if 'Applied Science and Engineering' in major_name_en:
                    deadline = '2019-01-10'
                elif 'Architecture' in major_name_en:
                    deadline = '2019-01-10'
                elif 'Landscape' in major_name_en:
                    deadline = '2019-01-10'
                elif 'Design' in major_name_en:
                    deadline = '2019-01-10'
                elif 'Bachelor of Information' in degree_name:
                    deadline = '2019-01-15'
                elif 'Medical Radiation Sciences' in major_name_en:
                    deadline = '2019-02-01'
                elif 'Nursing' in major_name_en:
                    deadline = '2019-01-15'
                elif 'Physician Assistant' in major_name_en:
                    deadline = '2019-01-15'
                else:
                    deadline = '2019-01-16'
                item['deadline'] = deadline

                if 'Engineering' in department or 'Engineering' in major_name_en:
                    tuition_fee = '59230'
                else:
                    tuition_fee = '54280'
                item['tuition_fee'] = tuition_fee
                yield item
