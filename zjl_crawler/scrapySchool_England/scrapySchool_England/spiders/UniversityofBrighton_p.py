# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/10 14:21'
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
class UniversityofBrightonSpider(scrapy.Spider):
    name = 'UniversityofBrighton_p'
    allowed_domains = ['brighton.ac.uk/']
    start_urls = []
    C= ['https://www.brighton.ac.uk/courses/study/finance-and-banking-msc.aspx',
'https://www.brighton.ac.uk/courses/study/finance-and-risk-management-msc.aspx',
'https://www.brighton.ac.uk/courses/study/history-of-design-and-material-culture-ma.aspx',
'https://www.brighton.ac.uk/courses/study/human-resource-management-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/health-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/health-promotion-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/health-and-management-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/finance-and-accounting-msc.aspx',
'https://www.brighton.ac.uk/courses/study/international-hospitality-management-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/international-management-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/law-conversion-llm.aspx',
'https://www.brighton.ac.uk/courses/study/logistics-and-supply-chain-management-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/linguistics-ma-mres.aspx',
'https://www.brighton.ac.uk/courses/study/international-event-management-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/international-tourism-management-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/the-brighton-mba-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/management-entrepreneurship-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/management-human-resources-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/management-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/marketing-branding-and-communications-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/marketing-international-marketing-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/marketing-digital-marketing-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/marketing-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/marketing-social-marketing-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/musculoskeletal-physiotherapy-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/occupational-therapy-pre-reg-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/management-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/photography-ma.aspx',
'https://www.brighton.ac.uk/courses/study/physiotherapy-and-education-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/physiotherapy-and-management-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/physiotherapy-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/podiatry-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/podiatry-pre-reg-msc.aspx',
'https://www.brighton.ac.uk/courses/study/podiatry-with-diabetes-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/project-management-for-construction-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/management-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/specialist-community-public-health-nursing-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/sequential-design-illustration-ma.aspx',
'https://www.brighton.ac.uk/courses/study/sport-business-management-msc.aspx',
'https://www.brighton.ac.uk/courses/study/strength-and-conditioning-msc.aspx',
'https://www.brighton.ac.uk/courses/study/sustainable-design-ma.aspx',
'https://www.brighton.ac.uk/courses/study/tesol-ma.aspx',
'https://www.brighton.ac.uk/courses/study/sport-and-international-development-ma.aspx',
'https://www.brighton.ac.uk/courses/study/tesol-with-ict-ma.aspx',
'https://www.brighton.ac.uk/courses/study/marketing-social-marketing-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/the-brighton-mba-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/tourism-and-international-development-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/user-experience-design-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/town-planning-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/accounting-acca-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/applied-exercise-physiology-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/applied-sport-physiology-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/architecture-riba-part-2-march.aspx',
'https://www.brighton.ac.uk/courses/study/bioscience-mres.aspx',
'https://www.brighton.ac.uk/courses/study/arts-and-design-by-independent-project-ma.aspx',
'https://www.brighton.ac.uk/courses/study/clinical-pharmacy-msc.aspx',
'https://www.brighton.ac.uk/courses/study/civil-engineering-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/community-psychology-ma.aspx',
'https://www.brighton.ac.uk/courses/study/computer-science-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/computing-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/construction-management-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/curating-collections-and-heritage-ma.aspx',
'https://www.brighton.ac.uk/courses/study/data-analytics-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/digital-media-arts-ma.aspx',
'https://www.brighton.ac.uk/courses/study/digital-media-culture-and-society-ma.aspx',
'https://www.brighton.ac.uk/courses/study/digital-music-and-sound-arts-ma.aspx',
'https://www.brighton.ac.uk/courses/study/earthquake-and-structural-engineering-msc.aspx',
'https://www.brighton.ac.uk/courses/study/education-ma.aspx',
'https://www.brighton.ac.uk/courses/study/environmental-assessment-and-management-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/finance-and-investment-msc-pgcert-pgdip.aspx',
'https://www.brighton.ac.uk/courses/study/english-language-ma.aspx',
'https://www.brighton.ac.uk/courses/study/fine-art-ma.aspx']
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Brighton'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="page-heading"]/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        if  'MBA' in programme_en:
            degree_name = 'MBA'
        elif 'MSc' in programme_en:
            degree_name = 'MSc'
        elif 'GradCert' in programme_en:
            degree_name = 'GradCert'
        elif 'Pre-Diploma' in programme_en:
            degree_name = 'Pre-Diploma'
        elif 'PGDip' in programme_en:
            degree_name = 'PGDip'
        elif 'MA' in programme_en:
            degree_name = 'MA'
        elif 'MRes' in programme_en:
            degree_name = 'MRes'
        elif 'MArch' in programme_en:
            degree_name = 'MArch'
        elif 'ACCA' in programme_en:
            degree_name = 'ACCA'
        elif 'PGCert' in programme_en:
            degree_name = 'PGCert'
        elif 'PGCE' in programme_en:
            degree_name = 'PGCE'
        elif 'PGCert' in programme_en:
            degree_name = 'PGCert'
        elif 'PGCert' in programme_en:
            degree_name = 'PGCert'
        elif 'LLM' in programme_en:
            degree_name = 'LLM'
        else:
            degree_name = 'N/A'
        programme_en = programme_en.replace(degree_name,'').strip()
        # print(degree_name)

        #6.teach_time
        teach_time = response.xpath('//*[@id="summary"]/div/div/div[3]/div/p/strong').extract()
        teach_time = ''.join(teach_time)
        teach_time = remove_tags(teach_time)
        if 'Full-time' in teach_time:
            teach_time = 'Full-time'
        else:
            teach_time = 'Part-time'
        # print(teach_time)

        #7.overview_en
        overview_en = response.xpath('//*[@id="summary"]/div/div/div[2]').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #8.location
        location = response.xpath("//*[contains(text(),'Key facts')]//following-sibling::p[1]/text()").extract()
        location = ''.join(location)
        location =remove_tags(location).strip()
        if '1 year2–6 years' in location:
            location = 'N/A'
        elif len(location)==0:
            location = 'N/A'
        else:
            location = location
        # print(location)

        #9.duration  #10.duration_per
        duration_list = response.xpath("//*[contains(text(),'Key facts')]//following-sibling::p/text()").extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        # print(duration_list)
        try:
            duration = re.findall('\d+',duration_list)[0]
        except:
            duration = 1
        if 'six months' in duration_list:
            duration = 6
        elif 'X110' in duration_list:
            duration = 1
        elif 'X100' in duration_list:
            duration = 1
        elif 'F8X1' in duration_list:
            duration = 1
        elif 'Q3X1' in duration_list:
            duration = 1
        elif 'W5X1' in duration_list:
            duration = 1
        elif 'C6XC' in duration_list:
            duration = 1
        elif 'F3X1' in duration_list:
            duration = 1
        elif 'R9X11' in duration_list:
            duration = 1
        elif 'V6X11' in duration_list:
            duration = 1
        elif 'L508' in duration_list:
            duration = 2
        else:
            duration = duration
        if 'weeks' in duration_list:
            duration_per = 4
        elif int(duration)>4:
            duration_per = 3
        else:
            duration_per = 1
        # print(duration,duration_per)

        #11.rntry_requirements
        rntry_requirements = response.xpath("//*[contains(text(),'Entry requirements')]//following-sibling::*").extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #12.ielts 13141516
        ielts_list = response.xpath('//*[@id="entry"]/div/div/div/div').extract()
        ielts_list = ''.join(ielts_list)
        ielts_list = remove_tags(ielts_list)
        try:
            ielts = re.findall('\d\.\d',ielts_list)
            if '2.1' in ielts:
                ielts = ielts.remove('2.1')
            elif '2.2' in ielts:
                ielts = ielts.remove('2.2')
        except:
            ielts = None
        try:
            if len(ielts) ==3:
                a = ielts[0]
                b = ielts[1]
                c = ielts[2]
                ielts = a
                ielts_w = b
                ielts_r = c
                ielts_l = c
                ielts_s = c
            elif len(ielts) ==2:
                a = ielts[0]
                b = ielts[1]
                ielts = a
                ielts_w = b
                ielts_r = b
                ielts_l = b
                ielts_s = b
            elif len(ielts) ==1:
                a= ielts[0]
                ielts = a
                ielts_w = int(a)- 0.5
                ielts_r = int(a)- 0.5
                ielts_l = int(a)- 0.5
                ielts_s = int(a)- 0.5
            else:
                ielts = 6.5
                ielts_w = 6.0
                ielts_r = 6.0
                ielts_l = 6.0
                ielts_s = 6.0
        except:
            ielts = 6.5
            ielts_w = 6.0
            ielts_r = 6.0
            ielts_l = 6.0
            ielts_s = 6.0
        # print(ielts,ielts_l,ielts_r,ielts_w,ielts_s)

        #17.modules_en
        modules_en = response.xpath("//h2[contains(text(),'Course in detail')]//following-sibling::*").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #18.career_en
        career_en = response.xpath("//*[contains(text(),'Careers and employability')]/../following-sibling::*").extract()
        career_en =''.join(career_en)
        career_en = remove_class(career_en).strip()
        career_en = clear_space_str(career_en)
        # print(career_en)

        #19.tuition_fee
        tuition_fee= response.xpath("//*[contains(text(),'International')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_class(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # if tuition_fee ==0:
        #     print(response.url)
        # print(tuition_fee)

        #20.tuition_fee_pre
        tuition_fee_pre= '£'

        #21.teach_type
        teach_type = 'taught'
        #22.apply_pre
        apply_pre = '£'
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['teach_time'] = teach_time
        item['overview_en'] = overview_en
        item['location'] = location
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['rntry_requirements'] = rntry_requirements
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['teach_type'] = teach_type
        yield item