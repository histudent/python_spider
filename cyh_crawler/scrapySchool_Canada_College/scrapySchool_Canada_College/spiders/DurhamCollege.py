# -*- coding: utf-8 -*-
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.getItem import *
from scrapySchool_Canada_College.items import *


class DurhamcollegeSpider(scrapy.Spider):
    name = 'DurhamCollege'
    # allowed_domains = ['a.b']
    start_urls = ['https://durhamcollege.ca/programs/health-care-technology-management-honours-bachelor',
'https://durhamcollege.ca/programs/addictions-and-mental-health',
'https://durhamcollege.ca/programs/advanced-filmmaking',
'https://durhamcollege.ca/programs/advanced-law-enforcement-and-investigations',
'https://durhamcollege.ca/programs/advertising-digital-media-management',
'https://durhamcollege.ca/programs/artificial-intelligence-analysis-design-and-implementation-graduate-certificate',
'https://durhamcollege.ca/programs/communicative-disorders-assistant-graduate-certificate',
'https://durhamcollege.ca/programs/registered-nurse-critical-care-nursing-e-learning',
'https://durhamcollege.ca/programs/data-analytics-for-business-decision-making-graduate-certificate',
'https://durhamcollege.ca/programs/gerontology-activation-co-ordination-graduate-certificate',
'https://durhamcollege.ca/programs/human-resources-management-graduate-certificate',
'https://durhamcollege.ca/programs/information-systems-security-computers-and-networking',
'https://durhamcollege.ca/programs/international-business-management-graduate-certificate',
'https://durhamcollege.ca/programs/mediation-alternative-dispute-resolution',
'https://durhamcollege.ca/programs/paralegal-graduate-certificate',
'https://durhamcollege.ca/programs/paramedic-advanced-care-hybrid-delivery-graduate-certificate',
'https://durhamcollege.ca/programs/project-management',
'https://durhamcollege.ca/programs/sport-business-management-graduate-certificate',
'https://durhamcollege.ca/programs/vfx-digital-cinema-graduate-certificate',
'https://durhamcollege.ca/programs/victimology-graduate-certificate',
'https://durhamcollege.ca/programs/youth-justice-and-interventions-graduate-certificate',
'https://durhamcollege.ca/programs/business-administration-accounting',
'https://durhamcollege.ca/programs/animation-digital',
'https://durhamcollege.ca/programs/architectural-technology',
'https://durhamcollege.ca/programs/biomedical-engineering-technology',
'https://durhamcollege.ca/programs/biomedical-engineering-technology-compressed-fast-track',
'https://durhamcollege.ca/programs/biotechnology-advanced-compressed-fast-track',
'https://durhamcollege.ca/programs/biotechnology-advanced',
'https://durhamcollege.ca/programs/chemical-engineering-technology',
'https://durhamcollege.ca/programs/chemical-engineering-technology-compressed-fast-track',
'https://durhamcollege.ca/programs/child-and-youth-care-brock-university-articulation',
'https://durhamcollege.ca/programs/child-and-youth-care',
'https://durhamcollege.ca/programs/civil-engineering-technology',
'https://durhamcollege.ca/programs/computer-programmer-analyst-three-year',
'https://durhamcollege.ca/programs/computer-systems-technology-three-year',
'https://durhamcollege.ca/programs/dental-hygiene',
'https://durhamcollege.ca/programs/electro-mechanical-engineering-technology',
'https://durhamcollege.ca/programs/electronics-engineering-technology-three-year',
'https://durhamcollege.ca/programs/environmental-technology',
'https://durhamcollege.ca/programs/environmental-technology-compressed-fast-track',
'https://durhamcollege.ca/programs/finance-business-administration',
'https://durhamcollege.ca/programs/fine-arts-advanced',
'https://durhamcollege.ca/programs/game-art',
'https://durhamcollege.ca/programs/graphic-design',
'https://durhamcollege.ca/programs/business-administration-human-resources',
'https://durhamcollege.ca/programs/journalism-mass-media',
'https://durhamcollege.ca/programs/law-clerk-advanced',
'https://durhamcollege.ca/programs/law-clerk-advanced-fast-track',
'https://durhamcollege.ca/programs/business-administration-marketing',
'https://durhamcollege.ca/programs/massage-therapy',
'https://durhamcollege.ca/programs/mechanical-engineering-technology',
'https://durhamcollege.ca/programs/music-business-administration-music-business-management',
'https://durhamcollege.ca/programs/chemical-laboratory-technology-pharmaceutical-and-food-science',
'https://durhamcollege.ca/programs/chemical-laboratory-technology-pharmaceutical-and-food-science-fast-track',
'https://durhamcollege.ca/programs/public-relations',
'https://durhamcollege.ca/programs/sport-administration-sport-management',
'https://durhamcollege.ca/programs/supply-chain-and-operations-management-business-administration',
'https://durhamcollege.ca/programs/business-accounting',
'https://durhamcollege.ca/programs/business-two-year-accounting-transfer-program-to-university-of-ontario-institute-of-technology-uoit-bachelor-of-commerce-hons',
'https://durhamcollege.ca/programs/business-administration-accounting',
'https://durhamcollege.ca/programs/advertising-and-marketing-communications',
'https://durhamcollege.ca/programs/animation-digital',
'https://durhamcollege.ca/programs/architectural-technology',
'https://durhamcollege.ca/programs/automotive-technician-service-and-management-motive-power-technician',
'https://durhamcollege.ca/programs/biomedical-engineering-technology',
'https://durhamcollege.ca/programs/biomedical-engineering-technology-compressed-fast-track',
'https://durhamcollege.ca/programs/biotechnology-advanced-compressed-fast-track',
'https://durhamcollege.ca/programs/biotechnology-advanced',
'https://durhamcollege.ca/programs/broadcasting-radio-and-contemporary-media',
'https://durhamcollege.ca/programs/building-construction-technician',
'https://durhamcollege.ca/programs/chemical-engineering-technology',
'https://durhamcollege.ca/programs/chemical-engineering-technology-compressed-fast-track',
'https://durhamcollege.ca/programs/chemical-laboratory-technician',
'https://durhamcollege.ca/programs/child-and-youth-care-brock-university-articulation',
'https://durhamcollege.ca/programs/child-and-youth-care',
'https://durhamcollege.ca/programs/civil-engineering-technician',
'https://durhamcollege.ca/programs/civil-engineering-technology',
'https://durhamcollege.ca/programs/computer-programmer-two-year',
'https://durhamcollege.ca/programs/computer-programmer-analyst-three-year',
'https://durhamcollege.ca/programs/computer-systems-technician-two-year',
'https://durhamcollege.ca/programs/computer-systems-technician-transfer-to-uoit-bachelor-of-information-technology-hons',
'https://durhamcollege.ca/programs/computer-systems-technology-three-year',
'https://durhamcollege.ca/programs/contemporary-web-design-2',
'https://durhamcollege.ca/programs/cosmetic-techniques-and-management',
'https://durhamcollege.ca/programs/culinary-management',
'https://durhamcollege.ca/programs/dental-hygiene',
'https://durhamcollege.ca/programs/developmental-services-worker',
'https://durhamcollege.ca/programs/early-childhood-education-ece',
'https://durhamcollege.ca/programs/electrical-engineering-technician',
'https://durhamcollege.ca/programs/electro-mechanical-engineering-technology',
'https://durhamcollege.ca/programs/electronics-engineering-technician-two-year',
'https://durhamcollege.ca/programs/electronics-engineering-technology-three-year',
'https://durhamcollege.ca/programs/entrepreneurship-and-small-business-business-transfer-to-uoit-bachelor-of-commerce-hons',
'https://durhamcollege.ca/programs/business-entrepreneurship-and-small-business',
'https://durhamcollege.ca/programs/environmental-technology',
'https://durhamcollege.ca/programs/environmental-technology-compressed-fast-track',
'https://durhamcollege.ca/programs/esthetician-spa-management',
'https://durhamcollege.ca/programs/finance-business',
'https://durhamcollege.ca/programs/finance-business-administration',
'https://durhamcollege.ca/programs/fine-arts-advanced',
'https://durhamcollege.ca/programs/fire-and-life-safety-systems-technician',
'https://durhamcollege.ca/programs/fitness-and-health-promotion',
'https://durhamcollege.ca/programs/game-art',
'https://durhamcollege.ca/programs/graphic-design',
'https://durhamcollege.ca/programs/food-and-farming',
'https://durhamcollege.ca/programs/horticulture-technician',
'https://durhamcollege.ca/programs/hospitality-hotel-and-restaurant-operations-management',
'https://durhamcollege.ca/programs/human-resources-business-transfer-uoit-bachelor-commerce-hons',
'https://durhamcollege.ca/programs/business-human-resources',
'https://durhamcollege.ca/programs/business-administration-human-resources',
'https://durhamcollege.ca/programs/interactive-media-design',
'https://durhamcollege.ca/programs/journalism-mass-media',
'https://durhamcollege.ca/programs/law-clerk-advanced',
'https://durhamcollege.ca/programs/law-clerk-advanced-fast-track',
'https://durhamcollege.ca/programs/library-and-information-technician',
'https://durhamcollege.ca/programs/marketing-business-transfer-to-uoit-bachelor-of-commerce-hons',
'https://durhamcollege.ca/programs/business-marketing',
'https://durhamcollege.ca/programs/business-administration-marketing',
'https://durhamcollege.ca/programs/massage-therapy',
'https://durhamcollege.ca/programs/mechanical-engineering-technician',
'https://durhamcollege.ca/programs/mechanical-engineering-technician-non-destructive-evaluation',
'https://durhamcollege.ca/programs/mechanical-engineering-technician-non-destructive-evaluation-compressed-fast-track',
'https://durhamcollege.ca/programs/mechanical-engineering-technology',
'https://durhamcollege.ca/programs/mechanical-technician-elevating-devices',
'https://durhamcollege.ca/programs/mechanical-technician-millwright',
'https://durhamcollege.ca/programs/music-business-administration-music-business-management',
'https://durhamcollege.ca/programs/occupational-therapist-assistantphysiotherapist-assistant',
'https://durhamcollege.ca/programs/office-administration-executive',
'https://durhamcollege.ca/programs/office-administration-health-services',
'https://durhamcollege.ca/programs/office-administration-health-services-fast-track',
'https://durhamcollege.ca/programs/office-administration-legal',
'https://durhamcollege.ca/programs/office-administration-real-estate',
'https://durhamcollege.ca/programs/paralegal',
'https://durhamcollege.ca/programs/paramedic',
'https://durhamcollege.ca/programs/chemical-laboratory-technology-pharmaceutical-and-food-science',
'https://durhamcollege.ca/programs/chemical-laboratory-technology-pharmaceutical-and-food-science-fast-track',
'https://durhamcollege.ca/programs/photography',
'https://durhamcollege.ca/programs/police-foundations',
'https://durhamcollege.ca/programs/police-foundations-fast-track',
'https://durhamcollege.ca/programs/practical-nursing',
'https://durhamcollege.ca/programs/practical-nursing-flex-program',
'https://durhamcollege.ca/programs/practical-nursing-for-internationally-educated-nurses',
'https://durhamcollege.ca/programs/protection-security-and-investigation',
'https://durhamcollege.ca/programs/protection-security-and-investigation-fast-track',
'https://durhamcollege.ca/programs/public-relations',
'https://durhamcollege.ca/programs/recreation-and-leisure-services',
'https://durhamcollege.ca/programs/social-services-worker',
'https://durhamcollege.ca/programs/special-events-management',
'https://durhamcollege.ca/programs/sport-administration-sport-management',
'https://durhamcollege.ca/programs/supply-chain-and-operations-business',
'https://durhamcollege.ca/programs/supply-chain-and-operations-business-transfer-to-uoit-bachelor-of-commerce-hons',
'https://durhamcollege.ca/programs/supply-chain-and-operations-management-business-administration',
'https://durhamcollege.ca/programs/video-production',
'https://durhamcollege.ca/programs/water-quality-technician',
'https://durhamcollege.ca/programs/welding-engineering-technician',]
    def parse(self, response):
        item=get_item(ScrapyschoolCanadaCollegeItem)
        item['url']=response.url
        item['school_name']='Durham College'
        item['apply_fee'],item['apply_pre']='95','$'
        print(response.url)
        major_name=response.xpath('//h1/text()').extract()
        # print(major_name)
        item['major_name_en']=major_name[0].strip()

        degree_name=response.xpath('//dt[text()="Credential"]/following-sibling::dd[1]/text()').extract()
        # print(degree_name)
        item['degree_name']=degree_name[0].strip()
        degree_name=''.join(degree_name).strip()
        item['toefl_code']='8428'
        if 'Diploma' in degree_name:
            item['degree_level']='3'
            item['ielts_desc']='6.0, no band score less than 5.5'
            item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']='6.0','5.5','5.5','5.5','5.5'
            item['toefl_desc']='80, with minimum section scores of 20'
            item['toefl'],item['toefl_l'],item['toefl_s'],item['toefl_r'],item['toefl_w']='80','20','20','20','20'
            item['require_chinese_en']='<td>Scanned original copy along with notarized English-translated copies of one of the following:<p></p><ul><li>National Senior High School Examination with a minimum grade of 65 per cent or C in relevant subjects (School Leaving<br>Certificate).</li><li>Graduation Certificate awarded by senior (upper) middle school; may be academic or vocationally oriented with a minimum<br>of C or 65 per cent in relevant subjects.</li><li>High school transcripts, which must show all courses completed and grades achieved for all three years of study.</li></ul></td>'
        if 'Graduate' in degree_name:
            item['degree_level']='2'
            item['ielts_desc'] = '6.5, no band score less than 6.0'
            item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w'] = '6.5', '6.0', '6.0', '6.0', '6.0'
            item['toefl_desc'] = '88, with minimum section scores of 22'
            item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w'] = '88', '22', '22', '22', '22'
            item['require_chinese_en']='<td>Scanned original copy along with notarized English-translated copies of university degree and transcripts.</td>'


        location=response.xpath('//dt[text()="Location"]/following-sibling::dd[1]/text()').extract()
        # print(location)
        item['location'],item['campus']=location[0].strip(),location[0].strip()

        department=response.xpath('//dt[text()="School"]/following-sibling::dd[1]/a/text()').extract()
        item['department']=''.join(department).strip()

        duration=response.xpath('//dt[text()="Length"]/following-sibling::dd[1]/text()').extract()
        # print(duration)
        duration=clear_duration(duration)
        # print(duration)
        item['duration_per']='2'
        item['duration']=duration['duration']

        code=response.xpath('//dt[text()="OCAS Code"]/following-sibling::dd[1]/text()').extract()
        # print(code)
        item['programme_code']=''.join(code).strip()

        start_date=response.xpath('//th[text()="Date"]/../../following-sibling::tbody/tr/td[contains(text(),"2019")]/text()').extract()
        # print(start_date)
        start_date=tracslateDate(start_date)
        start_date=','.join(start_date).replace('-9','-09').replace('-1','-01').replace('-5','-05')
        # print(start_date)
        item['start_date']=start_date

        overview=response.xpath('//h2[text()="Program Overview"]/following-sibling::p[1]').extract()
        item['overview_en']=remove_class(overview)

        entry=response.xpath('//h2[text()="Admission Requirements"]/following-sibling::*').extract()
        item['entry_requirements_en']=remove_class(entry)

        modules=response.xpath('//h2[text()="Courses"]/following-sibling::*').extract()
        item['modules_en']=remove_class(modules)

        tuition=response.xpath('//td[text()="Tuition"]/following-sibling::td[2]/text()').extract()
        # print(tuition)
        item['tuition_fee']=''.join(tuition).replace('$','')
        item['tuition_fee_pre']='$'

        career=response.xpath('//h2[contains(text(),"areer")]/following-sibling::*').extract()
        item['career_en']=remove_class(career)

        yield item