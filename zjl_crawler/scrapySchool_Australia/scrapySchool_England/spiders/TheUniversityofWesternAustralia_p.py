# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/18 16:57'
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
class TheUniversityofWesternAustraliaSpider(scrapy.Spider):
    name = 'TheUniversityofWesternAustralia_p'
    allowed_domains = ['uwa.edu.au/']
    start_urls = []
    C = [
        'https://study.uwa.edu.au/courses/master-of-forensic-science',
        'https://study.uwa.edu.au/courses/master-of-science',
        'https://study.uwa.edu.au/courses/master-of-philosophy',
        'https://study.uwa.edu.au/courses/master-of-education--thesis--coursework',
        'https://study.uwa.edu.au/courses/master-of-educational-leadership--thesis--coursework',
        'https://study.uwa.edu.au/courses/master-of-arts',
        'https://study.uwa.edu.au/courses/master-of-architecture-design',
        'https://study.uwa.edu.au/courses/master-of-clinical-audiology-and-doctor-of-philosophy',
        'https://study.uwa.edu.au/courses/master-of-advanced-social-work',
        'https://study.uwa.edu.au/courses/master-of-curatorial-studies-in-fine-arts',
        'https://study.uwa.edu.au/courses/master-of-health-professions-education---thesis-and-coursework',
        'https://study.uwa.edu.au/courses/master-of-rural-and-remote-medicine',
        'https://study.uwa.edu.au/courses/master-of-clinical-research',
        'https://study.uwa.edu.au/courses/master-of-music',
        'https://study.uwa.edu.au/courses/master-of-research',
        'https://study.uwa.edu.au/courses/master-of-fine-arts',
        'https://study.uwa.edu.au/courses/master-of-exercise-science---thesis-and-coursework',
        'https://study.uwa.edu.au/courses/master-of-infectious-diseases',
        'https://study.uwa.edu.au/courses/master-of-landscape-architecture',
        'https://study.uwa.edu.au/courses/master-of-teaching-secondary',
        'https://study.uwa.edu.au/courses/master-of-marketing',
        'https://study.uwa.edu.au/courses/master-of-pharmacy',
        'https://study.uwa.edu.au/courses/master-of-information-technology',
        'https://study.uwa.edu.au/courses/master-of-dental-public--primary-health',
        'https://study.uwa.edu.au/courses/master-of-clinical-audiology',
        'https://study.uwa.edu.au/courses/master-of-commercial-and-resources-law',
        'https://study.uwa.edu.au/courses/master-of-biological-arts',
        'https://study.uwa.edu.au/courses/master-of-health-professions-education---coursework-and-dissertation',
        'https://study.uwa.edu.au/courses/master-of-asian-studies',
        'https://study.uwa.edu.au/courses/master-of-data-science',
        'https://study.uwa.edu.au/courses/master-of-music-international-pedagogy---coursework-and-dissertation',
        'https://study.uwa.edu.au/courses/master-of-engineering-in-oil-and-gas',
        'https://study.uwa.edu.au/courses/master-of-social-work',
        'https://study.uwa.edu.au/courses/master-of-professional-accounting',
        'https://study.uwa.edu.au/courses/master-of-heritage-studies',
        'https://study.uwa.edu.au/courses/master-of-building-information-modelling',
        'https://study.uwa.edu.au/courses/master-of-geoscience',
        'https://study.uwa.edu.au/courses/master-of-teaching-primary',
        'https://study.uwa.edu.au/courses/master-of-educational-leadership---coursework',
        'https://study.uwa.edu.au/courses/master-of-human-resources-and-employment-relations',
        'https://study.uwa.edu.au/courses/master-of-clinical-exercise-physiology',
        'https://study.uwa.edu.au/courses/master-of-environmental-science',
        'https://study.uwa.edu.au/courses/master-of-agricultural-economics',
        'https://study.uwa.edu.au/courses/master-of-international-law-and-master-of-international-relations',
        'https://study.uwa.edu.au/courses/master-of-professional-engineering-preliminary',
        'https://study.uwa.edu.au/courses/master-of-physics',
        'https://study.uwa.edu.au/courses/master-of-hydrogeology',
        'https://study.uwa.edu.au/courses/master-of-health-science',
        'https://study.uwa.edu.au/courses/master-of-agricultural-science',
        'https://study.uwa.edu.au/courses/master-of-business-administration-and-master-of-laws-mba',
        'https://study.uwa.edu.au/courses/master-of-applied-finance',
        'https://study.uwa.edu.au/courses/master-of-business-administration-flexible-mba',
        'https://study.uwa.edu.au/courses/master-of-industrial-and-organisational-psychology',
        'https://study.uwa.edu.au/courses/master-of-forensic-anthropology',
        'https://study.uwa.edu.au/courses/master-of-geographic-information-science',
        'https://study.uwa.edu.au/courses/master-of-commerce-and-master-of-international-commercial-law',
        'https://study.uwa.edu.au/courses/master-of-public-health',
        'https://study.uwa.edu.au/courses/master-of-studies',
        'https://study.uwa.edu.au/courses/master-of-biomedical-science',
        'https://study.uwa.edu.au/courses/master-of-biotechnology',
        'https://study.uwa.edu.au/courses/master-of-biological-science',
        'https://study.uwa.edu.au/courses/master-of-translation-studies',
        'https://study.uwa.edu.au/courses/master-of-professional-engineering',
        'https://study.uwa.edu.au/courses/master-of-teaching--early-childhood',
        'https://study.uwa.edu.au/courses/master-of-business-administration-full-time-mba',
        'https://study.uwa.edu.au/courses/master-of-international-relations',
        'https://study.uwa.edu.au/courses/master-of-economics',
        'https://study.uwa.edu.au/courses/master-of-social-research-methods',
        'https://study.uwa.edu.au/courses/master-of-urban-and-regional-planning',
        'https://study.uwa.edu.au/courses/master-of-legal-practice',
        'https://study.uwa.edu.au/courses/master-of-taxation-law',
        'https://study.uwa.edu.au/courses/master-of-infectious-diseases-and-doctor-of-philosophy',
        'https://study.uwa.edu.au/courses/master-of-architecture',
        'https://study.uwa.edu.au/courses/master-of-strategic-communication',
        'https://study.uwa.edu.au/courses/master-of-business-information-and-logistics-management',
        'https://study.uwa.edu.au/courses/master-of-international-law',
        'https://study.uwa.edu.au/courses/master-of-mining-and-energy-law',
        'https://study.uwa.edu.au/courses/master-of-science-communication',
        'https://study.uwa.edu.au/courses/master-of-international-commercial-law',
        'https://study.uwa.edu.au/courses/master-of-public-policy',
        'https://study.uwa.edu.au/courses/master-of-public-health-specialisation',
        'https://study.uwa.edu.au/courses/master-of-urban-design',
        'https://study.uwa.edu.au/courses/master-of-education',
        'https://study.uwa.edu.au/courses/master-of-business-administration-and-master-of-international-commercial-law-mba',
        'https://study.uwa.edu.au/courses/master-of-international-development',
        'https://study.uwa.edu.au/courses/master-of-business-psychology',
        'https://study.uwa.edu.au/courses/master-of-petroleum-geoscience',
        'https://study.uwa.edu.au/courses/master-of-exercise-science',
        'https://study.uwa.edu.au/courses/master-of-law-policy-and-government',
        'https://study.uwa.edu.au/courses/master-of-laws',
        'https://study.uwa.edu.au/courses/master-of-commerce',
        'https://study.uwa.edu.au/courses/master-of-ocean-leadership'
    ]
    C = set(C)
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'The University of Western Australia'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="page-content"]/div[1]/div[3]/div/div/div[3]/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        if 'Master of' in programme_en:
            programme_en = programme_en.replace('Master of','').strip()
        # print(programme_en)

        #4.overview_en
        overview_en = response.xpath('//*[@id="course-details"]/div/div/div/section/div[1]/div[1]/div[1]/div/div').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #5.modules_en
        modules_en = response.xpath("//h2[contains(text(),'Course structure details')]//following-sibling::*").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #6.teach_time
        teach_time = 'coursework'

        #7.location
        location = response.xpath("//*[contains(text(),'Locations')]//following-sibling::*").extract()[0]
        # location = ''.join(location)
        location = remove_tags(location).strip()
        location = clear_space_str(location)
        # print(location)

        #8.start_date
        start_date = response.xpath("//*[contains(text(),'Starting dates')]//following-sibling::*").extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date).strip()
        if 'January' in start_date:
            start_date = '2019-1'
        else:
            start_date = 'Semester1,Semester2'
        # print(start_date)

        #9.career_en
        career_en = response.xpath('//*[@id="careers-and-further-study"]/div/div/div/section/div[2]/div/div/div/a').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en).strip()
        # print(career_en)

        #10.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'fee')]//following-sibling::div").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        if tuition_fee ==0:
            tuition_fee = response.xpath("//*[contains(text(),'Fee')]//following-sibling::div").extract()
            tuition_fee = ''.join(tuition_fee)
            tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee,response.url)

        #11.tuition_fee_pre
        tuition_fee_pre = '$'

        #12.rntry_requirements_en
        rntry_requirements_en = response.xpath("//*[contains(text(),'Admission Requirements')]//following-sibling::div").extract()
        rntry_requirements_en = ''.join(rntry_requirements_en)
        rntry_requirements_en = remove_class(rntry_requirements_en)
        # print(rntry_requirements_en)

        #13.ielts 14151617
        if 'MBA' in programme_en:
            ielts = 7.0
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
            ielts_s = 6.5
        elif 'Health' in programme_en:
            ielts = 7.0
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
            ielts_s = 6.5
        elif 'Educational Leadership' in programme_en:
            ielts = 7.0
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
            ielts_s = 6.5
        elif 'Forensic Odontology' in programme_en:
            ielts = 7.0
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
            ielts_s = 6.5
        elif 'Dental Medicine' in programme_en:
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 7.0
            ielts_s = 7.0
        elif 'Clinical Dentistry' in programme_en:
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 7.0
            ielts_s = 7.0
        elif programme_en =='Medicine':
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 7.0
            ielts_s = 7.0
        elif 'Podiatric Medicine' in programme_en:
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 7.0
            ielts_s = 7.0
        elif 'Clinical Neuropsychology' in programme_en:
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 7.0
            ielts_s = 7.0
        elif 'Clinical Psychology' in programme_en:
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 7.0
            ielts_s = 7.0
        elif 'Clinical Audiology' in programme_en:
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 7.0
            ielts_s = 7.0
        elif 'Clinical Audiology' in programme_en:
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 7.0
            ielts_s = 7.0
        elif programme_en =='Industrial and Organisational Psychology':
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 7.0
            ielts_s = 7.0
        elif programme_en =='Pharmacy':
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 7.0
            ielts_s = 7.0
        elif programme_en =='Social Work':
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 7.0
            ielts_s = 7.0
        elif programme_en=='Education':
            ielts = 7.5
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
            ielts_s = 6.5
        elif programme_en =='Teaching':
            ielts = 7.5
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 8.0
            ielts_s = 8.0
        elif 'Law' in programme_en:
            ielts = 7.0
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
            ielts_s = 6.5
        elif 'Juris Doctor'in programme_en:
            ielts = 7.5
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 7.0
            ielts_s = 7.0
        else:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_l = 6.0
            ielts_s = 6.0

        #18.toefl 19202122
        if 'Law' in programme_en:
            toefl = 100
            toefl_s = 28
            toefl_l = 26
            toefl_r = 26
            toefl_w = 26
        elif 'Juris Doctor'in programme_en:
            toefl = 106
            toefl_s = 28
            toefl_l = 26
            toefl_r = 26
            toefl_w = 26
        elif 'MBA'in programme_en:
            toefl = 100
            toefl_s = 20
            toefl_l = 20
            toefl_r = 20
            toefl_w = 20
        elif 'MBA'in programme_en:
            toefl = 100
            toefl_s = 20
            toefl_l = 20
            toefl_r = 20
            toefl_w = 20
        elif 'Clinical Neuropsychology'in programme_en:
            toefl = 94
            toefl_s = 23
            toefl_l = 24
            toefl_r = 24
            toefl_w = 27
        elif 'Clinical Psychology' in programme_en:
            toefl = 94
            toefl_s = 23
            toefl_l = 24
            toefl_r = 24
            toefl_w = 27
        elif 'Clinical Audiology' in programme_en:
            toefl = 94
            toefl_s = 23
            toefl_l = 24
            toefl_r = 24
            toefl_w = 27
        elif 'Industrial and Organisationa' in programme_en:
            toefl = 94
            toefl_s = 23
            toefl_l = 24
            toefl_r = 24
            toefl_w = 27
        else:
            toefl = 82
            toefl_s = 20
            toefl_l = 20
            toefl_r = 18
            toefl_w = 22

        #23.apply_proces_en
        apply_proces_en = 'Check your chosen course is open to applications. Ensure you meet the admission requirements for this course as detailed on the previous tab. Ensure you meet our English language competency requirement and any course/major prerequisites. Apply'

        #24.apply_pre
        apply_pre='$'

        #25.apply_fee
        apply_fee = 100

        #26.degree_name
        degree_name = response.xpath('//*[@id="page-content"]/div[1]/div[3]/div/div/div[3]/h1').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #27.degree_type
        degree_type = 2

        #28.duration
        duration = response.xpath("//*[contains(text(),'duration')]//following-sibling::*[1]//ul//li").extract()
        duration = ''.join(duration)
        if '<li>1.5' in duration:
            duration = 1.5
        elif '<li>1 to 2' in duration:
            duration = '1/2'
        elif '<li>0.5-1.5' in duration:
            duration = '0.5/1.5'
        elif '<li>2-3' in duration:
            duration = '2/3'
        elif '<li>One' in duration:
            duration = 1
        elif '<li>Two' in duration:
            duration = 2
        else:
            duration = re.findall(r'\d+',duration)[0]
        # print(duration,url)
        

        
        
        item['duration'] = duration
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['teach_time'] = teach_time
        item['location'] = location
        item['start_date'] = start_date
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['rntry_requirements_en'] = rntry_requirements_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['toefl_w'] = toefl_w
        item['apply_proces_en'] = apply_proces_en
        item['apply_pre'] = apply_pre
        item['apply_fee'] = apply_fee
        yield item