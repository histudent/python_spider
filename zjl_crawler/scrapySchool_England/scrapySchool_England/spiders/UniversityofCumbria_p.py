# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '18-7-17 上午11:01'
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
from scrapySchool_England.TranslateMonth import translate_month
class UniversityofCumbriaSpider(scrapy.Spider):
    name = 'UniversityofCumbria_p'
    allowed_domains = ['cumbria.ac.uk/']
    start_urls = []
    C= [
        'https://www.cumbria.ac.uk/study/courses/postgraduate/legal-and-criminological-psychology/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/management-and-leadership-in-health-and-social-care-msc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/management-and-leadership-in-health-and-social-care-pgc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/management-and-leadership-in-health-and-social-care-pgd/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/master-of-business-administration-robert-kennedy-college/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/mba-full-time/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/mba-part-time/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/media-leadership-robert-kennedy-college/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/medical-imaging-msc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/medical-imaging-pgc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/medical-imaging-pgd/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/medical-imaging-ultrasound-pgc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/advanced-clinical-practice/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/advanced-practice-of-cognitive-behavioural-therapy-high-intensity-iapt/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/applied-forensic-psychology/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/applied-social-science/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/business-administration/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/business-administration-part-time/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/coaching-and-mentoring-msc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/coaching-and-mentoring-pgc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/coaching-and-mentoring-pgd/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/coaching-and-mentoring-ilm-level-5/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/community-specialist-practice-district-nursing-graddip/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/community-specialist-practice-district-nursing-pgd/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/finance-and-accounting/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/finance-and-sustainability-robert-kennedy-college/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/healthcare-science/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/non-medical-prescribing-for-pharmacists-level-7/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/independent-supplementary-prescribing-v300---level-7/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/international-business-robert-kennedy-college/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/international-business-law-robert-kennedy-college/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/law-international-commercial-law-with-dispute-resolution/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/international-healthcare-management-robert-kennedy-college/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/international-management/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/leadership-and-sustainability-robert-kennedy-college/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/learning-and-teaching-for-higher-education/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/public-health-management-robert-kennedy-college/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/risk-management-robert-kennedy-college/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/social-work/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/strategic-policing/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/sustainable-leadership/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/sustainable-leadership-development/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/tourism-robert-kennedy-college/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/working-with-children-adolescents-and-families-ma/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/working-with-children-adolescents-and-families-pgc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/working-with-children-adolescents-and-families-pgd/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/working-with-individuals-on-the-autism-spectrum-msc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/working-with-individuals-on-the-autism-spectrum-pgc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/outdoor-and-experiential-learning-ma/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/photography/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/physiotherapy/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/practice-development-msc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/practice-development-pgc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/practice-development-pgd/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/practice-development-acute-and-critical-care/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/practice-development-emergency-care/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/practice-development-enhancing-paramedic-practice/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/practice-development-long-term-conditions/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/practice-development-respiratory-care/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/psychological-research-methods/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/medical-imaging-ultrasound-full-time-msc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/medical-imaging-ultrasound-msc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/medical-imaging-magnetic-resonance-imaging-msc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/medical-imaging-magnetic-resonance-imaging-pgc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/medical-imaging-magnetic-resonance-imaging-pgd/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/medical-imaging-ultrasound-pgd/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/national-award-for-sen-coordination/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/non-medical-prescribing-for-allied-health-professionals---independent-prescribing-for-physiotherapists-and-podiatrists-level-7/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/non-medical-prescribing-for-allied-health-professionals---supplementary-prescribing-for-radiographers-level-7/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/nursing-international/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/occupational-therapy/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/outdoor-and-experiential-learning/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/youth-work-and-community-development-ma/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/youth-work-and-community-development-pgd/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/youth-work-and-community-studies-pgc/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/community-specialist-practice-general-practice-nursing-graddip/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/community-specialist-practice-general-practice-nursing-pgd/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/contemporary-fine-art/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/counselling-and-psychotherapy-ma/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/counselling-and-psychotherapy-pgd/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/creative-practice/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/digital-health/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/ecosystem-services-evaluation/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/education-professional-practice-with-pathways/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/educational-leadership-robert-kennedy-college/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/energy-and-sustainability-robert-kennedy-college/',
        'https://www.cumbria.ac.uk/study/courses/postgraduate/executive-coaching-and-mentoring-ilm-level-7/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        #1.university
        university = 'University of Cumbria'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('/html/body/main/div[1]/header/div/h1/text()').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        programme_en = clear_space_str(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        degree_name = response.xpath('/html/body/main/div[1]/header/div/h1/em').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #6.location
        location = response.xpath("//*[contains(text(),'Location')]//following-sibling::*").extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #7.duration #8.duration_per #9.teach_time
        duration_list = response.xpath("//*[contains(text(),'Duration')]//following-sibling::*").extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        try:
            duration = re.findall('\d+',duration_list)[0]
        except:
            duration = 1
        if int(duration)>5:
            duration_per = 3
        else:
            duration_per = 1
        if 'Full' in duration_list:
            teach_time = 'Full-time'
        else:
            teach_time = 'Part-time'
        # print(duration,teach_time,duration_per)

        #10.start_date
        start_date = response.xpath("//*[contains(text(),'Start date')]//following-sibling::*").extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        if 'Various' in start_date:
            start_date = '2018-*'
        elif 'September, November 2018' in start_date:
            start_date = '2018-9,2018-11'
        elif 'September 2018, March 2019' in start_date:
            start_date = '2018-9,2019-3'
        elif 'September 2018; January 2018' in start_date:
            start_date = '2018-9,2019-1'
        elif 'April, September 2018' in start_date:
            start_date = '2018-9,2019-4'
        elif 'January, May, October 2018' in start_date:
            start_date = '2018-10,2019-1,2019-5'
        elif 'January, April, July, October 2018' in start_date:
            start_date = '2018-7,2019-1,2019-4,2019-7'
        elif 'September 2018; March 2018' in start_date:
            start_date = '2018-9,2019-3'
        elif 'June, September 2018' in start_date:
            start_date = '2018-6,2018-9'
        elif 'January, April or September 2018' in start_date:
            start_date = '2018-9,2019-1,2019-4'
        elif 'January, April, September 2018' in start_date:
            start_date = '2018-9,2019-1,2019-4'
        elif 'January 2018; September 2018' in start_date:
            start_date = '2018-9'
        elif 'October 2018; May, January 2018' in start_date:
            start_date = '2018-10,2019-1,2019-5'
        elif 'September 2018; January 2018 ' in start_date:
            start_date = '2018-9,2019-1'
        elif 'January, May, September 2018, 2019'in start_date:
            start_date = '2018-9,2019-1,2019-5'
        else:
            start_date = translate_month(start_date)
            start_date = '2018-'+str(start_date)
        # print(start_date)

        #11.modules_en
        modules_en = response.xpath("//h3[contains(text(),'Modules')]//following-sibling::*[1]").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en).strip()
        # print(modules_en)

        #12.rntry_requirements
        rntry_requirements = response.xpath("//h3[contains(text(),'Selection criteria')]//following-sibling::*").extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #13.tuition_fee_pre
        tuition_fee_pre = '£'

        #14.other
        other = 'https://www.cumbria.ac.uk/media/university-of-cumbria-website/content-assets/public/finance/documents/studentfinance/fees/postgraduate-taught-tuition-fees-2018-19.pdf'

        #15.ielts 16171819
        if 'Occupational Therapy' in programme_en:
            ielts = 7.0
            ielts_r = 6.5
            ielts_s = 6.5
            ielts_l = 6.5
            ielts_w = 6.5
        elif 'Physiotherapy' in programme_en:
            ielts = 7.0
            ielts_r = 6.5
            ielts_s = 6.5
            ielts_l = 6.5
            ielts_w = 6.5
        elif 'Social Work' in programme_en:
            ielts = 7.0
            ielts_r = 6.5
            ielts_s = 6.5
            ielts_l = 6.5
            ielts_w = 6.5
        else :
            ielts = 6.5
            ielts_r = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
            ielts_w = 5.5
        #20.require_chinese_en
        require_chinese_en = '<p>Bachelor’s degree or equivalent.English Language: IELTS 6.5 with at least 6.0 in each section (or equivalent).</p>'
        #21.apply_pre
        apply_pre = '£'

        item['apply_pre'] = apply_pre
        item['require_chinese_en'] = require_chinese_en
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['location'] = location
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['teach_time'] = teach_time
        item['start_date'] = start_date
        item['modules_en'] = modules_en
        item['tuition_fee_pre'] = tuition_fee_pre
        item['rntry_requirements'] = rntry_requirements
        item['other'] = other
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        yield  item