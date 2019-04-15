# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/16 15:32'
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
from scrapySchool_England.clearSpace import  clear_space_str
from scrapySchool_England.translate_date import  tracslateDate
from scrapySchool_England.translate_date import tracslateDate
class UniversityofSuffolkSpider(scrapy.Spider):
    name = 'UniversityofSuffolk_p'
    allowed_domains = ['uos.ac.uk/']
    start_urls = []
    C= [
        'https://www.uos.ac.uk/courses/pg/msc-advanced-healthcare-practice-0',
        'https://www.uos.ac.uk/courses/pg/postgraduate-certificate-pgc-advanced-practice-and-reporting-computed-tomography',
        'https://www.uos.ac.uk/courses/pg/msc-applications-psychology',
        'https://www.uos.ac.uk/courses/pg/msc-business-and-management',
        'https://www.uos.ac.uk/courses/pg/ma-childhood-studies',
        'https://www.uos.ac.uk/courses/pg/msc-crime-and-community-safety-evidence-based-practice',
        'https://www.uos.ac.uk/courses/pg/dementia-care-health-and-social-care-professionals',
        'https://www.uos.ac.uk/courses/pg/mapgdpgc-education-studies',
        'https://www.uos.ac.uk/courses/pg/effective-practitioner',
        'https://www.uos.ac.uk/courses/pg/maastricht-suffolk-executive-mba',
        'https://www.uos.ac.uk/courses/pg/msc-games-development',
        'https://www.uos.ac.uk/courses/pg/globalisation',
        'https://www.uos.ac.uk/courses/pg/ba-hons-health-and-social-care-practice',
        'https://www.uos.ac.uk/courses/pg/ma-health-and-social-care-studies',
        'https://www.uos.ac.uk/courses/pg/mapgdpgc-healthcare-education',
        'https://www.uos.ac.uk/courses/pg/msc-human-resource-management',
        'https://www.uos.ac.uk/courses/pg/postgraduate-diploma-human-resource-management',
        'https://www.uos.ac.uk/courses/pg/mapgdpgc-professional-practice-heritage-management',
        'https://www.uos.ac.uk/courses/pg/managing-suicide-and-self-harm',
        'https://www.uos.ac.uk/courses/pg/master-business-administration-mba',
        'https://www.uos.ac.uk/courses/pg/postgraduate-certificate-national-award-special-educational-needs-coordinator-senco-0-5',
        'https://www.uos.ac.uk/courses/pg/postgraduate-certificate-national-award-senco',
        'https://www.uos.ac.uk/courses/pg/postgraduate-diploma-clinical-primary-care-nursing-district-nursing',
        'https://www.uos.ac.uk/courses/pg/postgraduate-diploma-clinical-practice-home-district-nursing',
        'https://www.uos.ac.uk/courses/pg/msc-public-health-nursing',
        'https://www.uos.ac.uk/msc-regenerative-medicine',
        'https://www.uos.ac.uk/courses/pg/return-practice-nursing',
        'https://www.uos.ac.uk/courses/pg/postgraduate-diploma-specialist-community-public-health-nursing',
        'https://www.uos.ac.uk/courses/pg/certificate-education-professional-graduate-certificate-education-pgce',
        'https://www.uos.ac.uk/courses/pg/professional-graduate-certificate-education-pgce-north-east-essex-secondary-scitt',
        'https://www.uos.ac.uk/courses/pg/professional-graduate-certificate-education-pgce-tendring-hundred-primary-scitt',
        'https://www.uos.ac.uk/courses/pg/postgraduate-certificate-education-pgce-suffolk-and-norfolk-primary-scitt',
        'https://www.uos.ac.uk/courses/pg/postgraduate-certificate-education-pgce-suffolk-and-norfolk-secondary-scitt'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Suffolk'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('/html/body/div/div[2]/div/div[1]/div[1]/div[2]/header/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        degree_name = programme_en.split()[0]
        if 'Maastricht-Suffolk Executive MBA' in programme_en:
            degree_name = 'MBA'
        elif 'PGCE' in programme_en:
            degree_name = 'PGCE'
        else:
            degree_name = degree_name
        try:
            programme_en = programme_en.replace(degree_name,'').strip()
        except:pass
        # print(degree_name)
        # print(programme_en)

        #6.location
        location = response.xpath("//*[contains(text(),'Location:')]//following-sibling::*").extract()
        location = ''.join(location)
        location = remove_tags(location).strip()
        # print(location)

        #7.teach_time #8.duration #9.duration_per
        teach_time_list = response.xpath("//*[contains(text(),'Duration:')]//following-sibling::*").extract()
        teach_time_list  = ''.join(teach_time_list )
        teach_time_list  = remove_tags(teach_time_list )
        teach_time_list  = clear_space_str(teach_time_list )
        if 'Full-time' in teach_time_list :
            teach_time = 'Full-time'
        else:
            teach_time = 'Part-time'
        if 'five years' in teach_time_list:
            duration = 5
            duration_per = 1
        elif 'One year' in teach_time_list:
            duration = 1
            duration_per = 1
        elif '2/3 years' in teach_time_list:
            duration = 0.67
            duration_per = 1
        elif 'Two years' in teach_time_list:
            duration = 2
            duration_per = 1
        elif '24 Months' in teach_time_list:
            duration = 24
            duration_per = 3
        elif '15 Months' in teach_time_list:
            duration = 15
            duration_per = 3
        elif 'Two Semesters' in teach_time_list:
            duration = 2
            duration_per = 2
        elif '15 weeks' in teach_time_list:
            duration = 15
            duration_per =4
        else:
            duration =1
            duration_per = 1
        # print(duration,teach_time,duration_per)

        #10.overview_en
        overview_en = response.xpath('//*[@id="group-description"]/div[1]//p[1]').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #11.modules_en
        modules_en = response.xpath('//*[@id="group-duration-modules"]/*').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # if len(modules_en)==0:
        #     print(response.url)
        # print(modules_en)

        #12.tuition_fee
        tuition_fee = response.xpath('//*[@id="group-fees"]').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee =getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #13.tuition_fee_pre
        tuition_fee_pre = '£'

        #14.rntry_requirements
        rntry_requirements = response.xpath("//*[contains(text(),'Academic Requirements')]/../../following-sibling::*[1]").extract()
        if len(rntry_requirements)==0:
            rntry_requirements = response.xpath('//*[@id="group-entry-requirements"]').extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #15.ielts 16171819
        ielts_list = response.xpath("//*[contains(text(),'International Requirements')]/../../following-sibling::*[1]").extract()
        ielts_list = ''.join(ielts_list)
        ielts_list = remove_tags(ielts_list)
        # print(ielts_list)
        try:
            ielts = re.findall('\d\.\d',ielts_list)[0]
        except:
            ielts = 6.5
        # print(ielts)
        ielts_r = 5.5
        ielts_l = 5.5
        ielts_w = 5.5
        ielts_s = 5.5

        #20.apply_proces_en
        apply_proces_en = 'https://www.uos.ac.uk/content/how-apply-0'
        #21.apply_pre
        apply_pre = '£'

        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['location'] = location
        item['teach_time'] = teach_time
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['rntry_requirements'] = rntry_requirements
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['apply_proces_en'] = apply_proces_en
        yield  item