# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/30 9:18'
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
import urllib.request
class MurdochUniversitySpider(scrapy.Spider):
    name = 'MurdochUniversity_p'
    allowed_domains = ['murdoch.edu.au/']
    start_urls = []
    C = [
        'http://www.murdoch.edu.au/study/courses/course-details/Master-of-Wildlife-Health-and-Conservation-(MWildlifeHth)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Counselling-(MCounsel)',
        'https://www.murdoch.edu.au/study/courses/course-details/master-of-engineering-(instrumentation-control-and-industrial-computer-systems-engineering)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-International-Affairs-and-Security-(MIAS)',
        'https://www.murdoch.edu.au/study/courses/course-details/master-of-engineering-(water-treatment-and-desalination)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Sustainable-Development-(MSustDev)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Education-(Coursework)-(MEd)',
        'https://www.murdoch.edu.au/study/courses/course-details/master-of-engineering-(electrical-power-and-industrial-computer-systems-engineering)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Health-Administration-Policy-and-Leadership-(MHAPL)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Chaplaincy-(MChap)',
        'https://www.murdoch.edu.au/study/courses/course-details/master-of-exercise-science-(research)-(mexsc(res))',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Veterinary-Studies-(Conservation-Medicine)-(MVS)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Environmental-Science-(MEnvSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Business-Administration-(MBA)',
        'https://www.murdoch.edu.au/study/courses/course-details/master-of-business-administration-(global)-(mba(global))',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Divinity-(MDiv)',
        'https://www.murdoch.edu.au/study/courses/course-details/master-of-communication-(mcommun)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Renewable-and-Sustainable-Energy-(MRenSusEn)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Teaching-(Primary)-(MTeachPrim)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Food-Security-(MFoodSec)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Professional-Accounting-(Advanced)-(MPA(Adv))',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Development-Studies-(MDS)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Human-Resources-Management-(MHRM)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Professional-Accounting-(MPA)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Biosecurity-(MBiosec)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Forensic-Science-(Professional-Practice)-(MForSc(ProfessionalPractice))',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Public-Policy-and-Management-(MPPM)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Veterinary-Studies-(Veterinary-Surveillance)-(MVS)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Information-Technology-(MIT)',
        'https://www.murdoch.edu.au/study/courses/course-details/Master-of-Community-Development-(MCommDev)'
    ]

    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Murdoch University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.degree_name
        degree_name =response.xpath('//*[@id="course-overview"]/div/div/div/div/h3').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name).strip()
        # print(degree_name)

        #4.programme_en
        programme_en = response.xpath('//*[@id="course-overview"]/div/div/div/div/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en).strip()
        # print(programme_en)

        #5.degree_overview_en
        degree_overview_en = response.xpath('//*[@id="course-description-and-structure"]/div/div/div/div/p').extract()
        degree_overview_en = ''.join(degree_overview_en)
        degree_overview_en = remove_class(degree_overview_en)
        # print(degree_overview_en)

        #6.location
        location = response.xpath('//*[@id="course-description-and-structure"]/div/div/div/div/ul/li[1]/ul/li/strong').extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #7.duration
        duration = response.xpath("//*[contains(text(),'Course Duration')]//following-sibling::*").extract()[0]
        duration = ''.join(duration)
        duration = remove_tags(duration).strip()
        if '1.5' in duration:
            duration = 1.5
        else:duration = re.findall(r'\d',duration)[0]
        # print(duration)

        #8.department
        department = response.xpath("//*[contains(text(),'School')]//following-sibling::*//strong").extract()
        department = ''.join(department)
        department = remove_tags(department).strip()
        if 'School of Business and GovernanceSocial' in department:
            department = 'School of Business and GovernanceSocial'
        # print(department)

        #9.degree_type
        degree_type = 2

        #10.start_date
        start_date = '2,7'

        #11.modules_en
        cour = response.xpath("//input[@name='course']//@value").extract()
        cour = ''.join(cour)
        cour = remove_tags(cour)
        # print(cour)
        modules_en_url ='https://handbook.murdoch.edu.au/courses/details/?us='+str(cour)+'&year=2019&structure=true'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        data = requests.get(modules_en_url, headers=headers)
        response_modules_en = etree.HTML(data.text)
        # print(modules_en_url)
        modules_en = response_modules_en.xpath('/html/body/div')
        # modules_en = ''.join(modules_en)
        doc = ""
        if len(modules_en) > 0:
            for a in modules_en:
                doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                doc = remove_class(doc)
                modules_en = doc
        # print(modules_en)

        #12.rntry_requirements_en
        # rntry_url = 'https://webapps2.murdoch.edu.au/entry-requirements/?study_level=Postgrad&course='+str(cour)+'&htmlOnly=1&student_origin=international&country=China'
        # data = requests.get(rntry_url, headers=headers)
        # response_rntry = etree.HTML(data.text)
        # # print(rntry_url)
        # response_rntry = response_rntry.xpath('/html/body/div//text()')[0]
        # response_rntry = '<p>'+response_rntry+'</P>'
        # # print(response_rntry)
        # rntry_requirements_en = response_rntry

        #13.tuition_fee
        tuition_fee = '1390/学分'

        #14.apply_pre
        apply_pre = '$'

        #15.tuition_fee_pre
        tuition_fee_pre = '$'

        #16.ielts 17181920 #21.toefl 22232425
        if 'Master of Teaching (Primary)' in degree_name:
            ielts = 7.5
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_s = 8.0
            ielts_l = 8.0
            toefl =102
            toefl_r = 24
            toefl_w = 24
            toefl_s = 29
            toefl_l = 29
        elif 'Master of Veterinary' in degree_name:
            ielts =7.0
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_s = 6.5
            ielts_l = 6.5
            toefl = 92
            toefl_r = 20
            toefl_w = 20
            toefl_s = 20
            toefl_l = 20
        elif 'Master of Food Security' in degree_name:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
            toefl = 79
            toefl_r = 18
            toefl_w = 18
            toefl_s = 18
            toefl_l = 18
        elif 'Master of Education' in degree_name:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
            toefl = 90
            toefl_r = 20
            toefl_w = 20
            toefl_s = 20
            toefl_l = 20
        else:
            ielts = 6.0
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
            toefl = 73
            toefl_r = 18
            toefl_w = 18
            toefl_s = 18
            toefl_l = 18

        #26.apply_documents_en
        apply_documents_en = '<p>Ready to apply? Before you start, make sure you have all of the following documentation ready for a quick application.Completed official Academic Transcripts and Certificates of Completion – both original and English translated versions A certified copy of your veterinary degree A certified copy of current registration with your local Veterinary Surgeon?s Board A recent Curriculum Vitae Two referee reports – one academic and one personal A typed, signed 500-word personal statement outlining how your veterinary work experience relates to this course English Language Proficiency Document (if available)</p>'

        #27.apply_desc_en
        apply_desc_en = "<p>Your Application Checklist Check the course details Check the entry requirements for the course to clarify your eligibility Check your eligibility for a scholarship Prepare your documentation (see the checklist below) Ask us any questions you might have (we're here to help!) Now you're ready to apply!</p>"

        item['university'] = university
        item['url'] = url
        item['degree_name'] = degree_name
        item['programme_en'] = programme_en
        item['degree_overview_en'] = degree_overview_en
        item['location'] = location
        item['duration'] = duration
        item['department'] = department
        item['degree_type'] = degree_type
        item['start_date'] = start_date
        item['modules_en'] = modules_en
        # item['rntry_requirements_en'] = rntry_requirements_en
        item['tuition_fee'] = tuition_fee
        item['apply_pre'] = apply_pre
        item['tuition_fee_pre'] = tuition_fee_pre
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
        item['apply_documents_en'] = apply_documents_en
        item['apply_desc_en'] = apply_desc_en
        yield item