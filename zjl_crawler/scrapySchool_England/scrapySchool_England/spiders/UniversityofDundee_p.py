# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/5 15:05'
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
class UniversityofDundeeSpider(scrapy.Spider):
    name = 'UniversityofDundee_p'
    allowed_domains = ['dundee.ac.uk/']
    start_urls = []
    C = [
        'https://www.dundee.ac.uk/study/pg/energy-studies-energy-finance/',
        'https://www.dundee.ac.uk/study/pg/energy-law-and-policy/',
        'https://www.dundee.ac.uk/study/pg/energy-finance-petroleum-beijing/',
        'https://www.dundee.ac.uk/study/pg/endodontics/',
        'https://www.dundee.ac.uk/study/pg/energy-studies-energy-policy/',
        'https://www.dundee.ac.uk/study/pg/energy-studies-energy-environment/',
        'https://www.dundee.ac.uk/study/pg/energy-studies-energy-economics/',
        'https://www.dundee.ac.uk/study/pg/computing/',
        'https://www.dundee.ac.uk/study/pg/writing-practice-study/?c=creative+writing',
        'https://www.dundee.ac.uk/study/pg/energy-studies-oil-and-gas/',
        'https://www.dundee.ac.uk/study/pg/computing-with-international-business/',
        'https://www.dundee.ac.uk/study/pg/computing/?c=computing+with+work+placement',
        'https://www.dundee.ac.uk/study/pg/computing-with-international-business/?c=computing+with+international+business+with+work+placement',
        'https://www.dundee.ac.uk/study/pg/corporate-commercial-law/',
        'https://www.dundee.ac.uk/study/pg/crime-writing-forensic-investigation/',
        'https://www.dundee.ac.uk/study/pg/data-science/?c=data+science',
        'https://www.dundee.ac.uk/study/pg/dental-public-health/',
        'https://www.dundee.ac.uk/study/pg/data-science/?c=data+science+(part+time)',
        'https://www.dundee.ac.uk/study/pg/design-healthcare-assistive-technologies/',
        'https://www.dundee.ac.uk/study/pg/design-business/',
        'https://www.dundee.ac.uk/study/pg/data-engineering/',
        'https://www.dundee.ac.uk/study/pg/data-science/',
        'https://www.dundee.ac.uk/study/pg/data-science/?c=data+science+individual',
        'https://www.dundee.ac.uk/study/pg/international-marketing/?c=digital+and+social+media+marketing',
        'https://www.dundee.ac.uk/study/pg/developmental-psychology/',
        'https://www.dundee.ac.uk/study/pg/geotechnical-engineering/',
        'https://www.dundee.ac.uk/study/pg/forensic-odontology/',
        'https://www.dundee.ac.uk/study/pg/educational-psychology/',
        'https://www.dundee.ac.uk/study/pg/education-leading-learning-teaching/',
        'https://www.dundee.ac.uk/study/pg/historymlitt/',
        'https://www.dundee.ac.uk/study/pg/humanities/',
        'https://www.dundee.ac.uk/study/pg/human-clinical-embryology-assisted-conception/',
        'https://www.dundee.ac.uk/study/pg/human-anatomy/',
        'https://www.dundee.ac.uk/study/pg/historymres/',
        'https://www.dundee.ac.uk/study/pg/art-humanities/',
        'https://www.dundee.ac.uk/study/pg/information-technology-international-business/',
        'https://www.dundee.ac.uk/study/pg/industrial-engineering-management/',
        'https://www.dundee.ac.uk/study/pg/industrial-engineering-international-finance/',
        'https://www.dundee.ac.uk/study/pg/biomedical-engineering/',
        'https://www.dundee.ac.uk/study/pg/art-society-publics/',
        'https://www.dundee.ac.uk/study/pg/augmentative-alternative-communication/',
        'https://www.dundee.ac.uk/study/pg/cancer-biology/',
        'https://www.dundee.ac.uk/study/pg/comics-graphic-novels/?c=comics+&+graphic+novels',
        'https://www.dundee.ac.uk/study/pg/international-accounting/',
        'https://www.dundee.ac.uk/study/pg/comics-graphic-novels/?c=comics+&+graphic+novels',
        'https://www.dundee.ac.uk/study/pg/community-learning-development-full-time/',
        'https://www.dundee.ac.uk/study/pg/international-business/?c=international+business+and+banking',
        'https://www.dundee.ac.uk/study/pg/civil-engineering/',
        'https://www.dundee.ac.uk/study/pg/international-banking/',
        'https://www.dundee.ac.uk/study/pg/international-business/?c=international+business+and+entrepreneurship',
        'https://www.dundee.ac.uk/study/pg/international-business/?c=international+business+and+finance',
        'https://www.dundee.ac.uk/study/pg/comparative-european-private-international-law/',
        'https://www.dundee.ac.uk/study/pg/international-business/?c=international+business+and+investment',
        'https://www.dundee.ac.uk/study/pg/international-business/?c=international+business+and+management',
        'https://www.dundee.ac.uk/study/pg/international-business/?c=international+business+and+marketing',
        'https://www.dundee.ac.uk/study/pg/international-business/?c=international+business+and+human+resource+management',
        'https://www.dundee.ac.uk/study/pg/international-business/',
        'https://www.dundee.ac.uk/study/pg/accountancy/',
        'https://www.dundee.ac.uk/study/pg/accounting-finance-mres/',
        'https://www.dundee.ac.uk/study/pg/accounting-management-strategy/',
        'https://www.dundee.ac.uk/study/pg/accounting-finance-msc/',
        'https://www.dundee.ac.uk/study/pg/animation-vfx/',
        'https://www.dundee.ac.uk/study/pg/anatomy-advanced-forensic-anthropology/',
        'https://www.dundee.ac.uk/study/pg/advanced-social-work-studies/',
        'https://www.dundee.ac.uk/study/pg/english-studies/?c=english+studies+part-time',
        'https://www.dundee.ac.uk/study/pg/applied-computing/?c=applied+computing+with+work+placement',
        'https://www.dundee.ac.uk/study/pg/applied-computing/',
        'https://www.dundee.ac.uk/study/pg/english-studies/',
        'https://www.dundee.ac.uk/study/pg/applied-mathematics/',
        'https://www.dundee.ac.uk/study/pg/finance/',
        'https://www.dundee.ac.uk/study/pg/film-studies/',
        'https://www.dundee.ac.uk/study/pg/environmental-law/',
        'https://www.dundee.ac.uk/study/pg/forensic-anthropology/',
        'https://www.dundee.ac.uk/study/pg/forensic-dentistry/',
        'https://www.dundee.ac.uk/study/pg/forensic-art-facial-identification/',
        'https://www.dundee.ac.uk/study/pg/forensic-archaeology-anthropology/',
        'https://www.dundee.ac.uk/study/pg/international-business/?c=international+business,+accounting+and+finance',
        'https://www.dundee.ac.uk/study/pg/international-business/?c=international+business+and+strategy',
        'https://www.dundee.ac.uk/study/pg/international-business/?c=international+business,+marketing+and+human+resource+management',
        'https://www.dundee.ac.uk/study/pg/international-business/?c=international+business,+banking+and+finance',
        'https://www.dundee.ac.uk/study/pg/international-criminal-justice-human-rights/',
        'https://www.dundee.ac.uk/study/pg/international-finance/',
        'https://www.dundee.ac.uk/study/pg/international-commercial-law-cergypontoise/',
        'https://www.dundee.ac.uk/study/pg/international-commercial-law/',
        'https://www.dundee.ac.uk/study/pg/international-finance/?c=international+finance+and+investment+management+',
        'https://www.dundee.ac.uk/study/pg/international-finance/?c=international+finance,+risk+and+regulation',
        'https://www.dundee.ac.uk/study/pg/international-law-security-msc/',
        'https://www.dundee.ac.uk/study/pg/international-marketing/?c=international+marketing+and+branding',
        'https://www.dundee.ac.uk/study/pg/international-marketing/?c=international+marketing+and+finance+',
        'https://www.dundee.ac.uk/study/pg/international-law-security-llm/',
        'https://www.dundee.ac.uk/study/pg/international-marketing/?c=international+marketing+and+management+',
        'https://www.dundee.ac.uk/study/pg/international-marketing/',
        'https://www.dundee.ac.uk/study/pg/international-mineral-resources-management/',
        'https://www.dundee.ac.uk/study/pg/international-oil-gas-management/',
        'https://www.dundee.ac.uk/study/pg/international-security/?c=international+security:+european+union',
        'https://www.dundee.ac.uk/study/pg/international-security/?c=international+security:+drugs+and+organised+crime',
        'https://www.dundee.ac.uk/study/pg/international-security/?c=international+security:+russia',
        'https://www.dundee.ac.uk/study/pg/international-security/',
        'https://www.dundee.ac.uk/study/pg/international-relations/',
        'https://www.dundee.ac.uk/study/pg/international-security/?c=international+security:+human+rights',
        'https://www.dundee.ac.uk/study/pg/international-security/?c=international+security:+terrorism',
        'https://www.dundee.ac.uk/study/pg/international-security/?c=international+security:+middle+east',
        'https://www.dundee.ac.uk/study/pg/law-general/',
        'https://www.dundee.ac.uk/study/pg/mathematics-financial-sector/',
        'https://www.dundee.ac.uk/study/pg/mathematical-biology/',
        'https://www.dundee.ac.uk/study/pg/management/?c=management+and+strategy',
        'https://www.dundee.ac.uk/study/pg/managing-energy-industries/',
        'https://www.dundee.ac.uk/study/pg/medical-education/',
        'https://www.dundee.ac.uk/study/pg/medical-imaging/',
        'https://www.dundee.ac.uk/study/pg/mineral-law-policy/',
        'https://www.dundee.ac.uk/study/pg/motion-analysis-msc/',
        'https://www.dundee.ac.uk/study/pg/medical-art/',
        'https://www.dundee.ac.uk/study/pg/natural-resources-law-policy/',
        'https://www.dundee.ac.uk/study/pg/nursing-health/',
        'https://www.dundee.ac.uk/study/pg/oil-gas-law-policy/',
        'https://www.dundee.ac.uk/study/pg/oral-biology/',
        'https://www.dundee.ac.uk/study/pg/orthopaedic-science/',
        'https://www.dundee.ac.uk/study/pg/orthopaedic-rehabilitation-technology/',
        'https://www.dundee.ac.uk/study/pg/oral-cancer/',
        'https://www.dundee.ac.uk/study/pg/leadership-and-innovation-full-time/',
        'https://www.dundee.ac.uk/study/pg/law-banking-and-finance/',
        'https://www.dundee.ac.uk/study/pg/management/?c=management+and+finance',
        'https://www.dundee.ac.uk/study/pg/management/?c=management+and+accounting',
        'https://www.dundee.ac.uk/study/pg/management/',
        'https://www.dundee.ac.uk/study/pg/management/?c=management+and+entrepreneurship',
        'https://www.dundee.ac.uk/study/pg/management/?c=management+and+banking',
        'https://www.dundee.ac.uk/study/pg/management/?c=management+and+human+resources',
        'https://www.dundee.ac.uk/study/pg/management/?c=management+and+marketing',
        'https://www.dundee.ac.uk/study/pg/management/?c=management+and+international+business',
        'https://www.dundee.ac.uk/study/pg/public-health/',
        'https://www.dundee.ac.uk/study/pg/renewable-energy-environmental-modelling/',
        'https://www.dundee.ac.uk/study/pg/science-fiction/',
        'https://www.dundee.ac.uk/study/pg/prosthodontics/',
        'https://www.dundee.ac.uk/study/pg/psychological-research-methods/',
        'https://www.dundee.ac.uk/study/pg/palliative-care-research/',
        'https://www.dundee.ac.uk/study/pg/orthopaedic-surgery/',
        'https://www.dundee.ac.uk/study/pg/psychology-of-mental-health/',
        'https://www.dundee.ac.uk/study/pg/psychology-of-language/',
        'https://www.dundee.ac.uk/study/pg/psychological-therapy-primary-care/',
        'https://www.dundee.ac.uk/study/pg/philosophy-literature/',
        'https://www.dundee.ac.uk/study/pg/product-design/',
        'https://www.dundee.ac.uk/study/pg/philosophy/',
        'https://www.dundee.ac.uk/study/pg/petroleum-taxation-finance/',
        'https://www.dundee.ac.uk/study/pg/professional-accountancy/',
        'https://www.dundee.ac.uk/study/pg/writing-practice-study/',
        'https://www.dundee.ac.uk/study/pg/social-research-methods/',
        'https://www.dundee.ac.uk/study/pg/spatial-planning-environmental-assessment/',
        'https://www.dundee.ac.uk/study/pg/theatre-studies/',
        'https://www.dundee.ac.uk/study/pg/sustainability/?c=sustainability:+climate+change+and+low+carbon+futures',
        'https://www.dundee.ac.uk/study/pg/social-work/',
        'https://www.dundee.ac.uk/study/pg/spatial-planning-geographic-information-systems/',
        'https://www.dundee.ac.uk/study/pg/spatial-planning-urban-conservation/',
        'https://www.dundee.ac.uk/study/pg/spatial-planning-marine-spatial-planning/',
        'https://www.dundee.ac.uk/study/pg/sports-biomechanics-rehabilitation/',
        'https://www.dundee.ac.uk/study/pg/spatial-planning-sustainable-urban-design/',
        'https://www.dundee.ac.uk/study/pg/sustainability/?c=sustainability+and+water+security',
        'https://www.dundee.ac.uk/study/pg/sustainability/?c=sustainability+and+the+green+economy',
        'https://www.dundee.ac.uk/study/pg/sustainability/',
        'https://www.dundee.ac.uk/study/pg/structural-engineering-concrete-materials/',
        'https://www.dundee.ac.uk/study/pg/law-banking-and-finance/',
        'https://www.dundee.ac.uk/study/pg/computing-with-international-business/?c=computing+with+international+business+with+work+placement'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Dundee'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="wrapper"]/header/div[2]/div/div[1]/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        degree_name = programme_en.split()[0]
        # print(degree_name)
        programme_en = programme_en.replace(degree_name,'').strip()
        # print(programme_en)

        #6.start_date
        start_date = response.xpath('//*[@id="maincontent"]/ul/li[1]/text()').extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        if 'January | February | March | April | May | June | July | August | September | October | November | December' in start_date:
            start_date = '2018'
        elif 'January | September' in start_date:
            start_date = '2018-9/2019-1'
        elif 'September/January' in start_date:
            start_date = '2018-9/2019-1'
        elif 'September | January' in start_date:
            start_date = '2018-9/2019-1'
        elif 'September | March' in start_date:
            start_date = '2018-9/2019-3'
        elif 'September' in start_date:
            start_date = '2018-9'
        elif 'January' in start_date:
            start_date = '2019-1'
        elif 'April' in start_date:
            start_date = '2018-4'
        elif 'June' in start_date:
            start_date = '2018-6'
        elif 'August' in start_date:
            start_date = '2018-8'
        elif 'December' in start_date:
            start_date = '2018-12'
        else:
            start_date = 'N/A'
        # print(start_date)

        #7.duration #8.duration_per
        duration_list = response.xpath('//*[@id="maincontent"]/ul/li[2]/text()').extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        duration = re.findall('\d+',duration_list)[0]
        if 'months' in duration_list:
            duration_per = 3
        else:
            duration_per = 4
        # print(duration,'***************',duration_per)

        #9.department
        department = response.xpath('//*[@id="maincontent"]/ul/li[3]/text()').extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #10.teach_time
        teach_time = response.xpath('//*[@id="maincontent"]/ul/li[4]/text()').extract()
        teach_time = ''.join(teach_time)
        teach_time = remove_tags(teach_time)
        if 'Part Time' in teach_time:
            teach_time = 'Full/Part time'
        else:
            teach_time = 'Full time'
        # print(teach_time)

        #11.overview_en
        overview_en = response.xpath("//*[contains(text(),'Overview')]/../following-sibling::p").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        if len(overview_en) ==0:
            overview_en = response.xpath('//*[@id="maincontent"]/div/div[1]/p').extract()
            overview_en = ''.join(overview_en)
            overview_en = remove_class(overview_en)
        # print(overview_en)

        #12.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'How you will be assessed')]//following-sibling::*[1]").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        if len(assessment_en)==0:
            assessment_en = '<p>Each course is assessed by a combination of examinations and a research paper.</p>'
        # print(assessment_en)

        #13.modules_en
        modules_en = response.xpath("//h1[contains(text(),'Assessment')]/../following-sibling::*").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        if len(modules_en)>30000:
            modules_en = modules_en[:30000]
        # print(modules_en)

        #14.career_en
        career_en = response.xpath("//h1[contains(text(),'Careers')]/../following-sibling::*[1]").extract()
        if len(career_en)==0:
            career_en = response.xpath('//*[@id="info-employability"]').extract()
        if len(career_en)==0:
            career_en = response.xpath('//*[@id="info-careers"]').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #15.rntry_requirements
        rntry_requirements = response.xpath("//*[contains(text(),'Entry Requirements')]/../following-sibling::*[1]").extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_tags(rntry_requirements)
        # rntry_requirements = rntry_requirements.raplace('Fees & Funding','')
        # print(rntry_requirements)

        #16.ielts 17181920
        try:
            ielts = response.xpath("//*[contains(text(),'IELTS Overall')]//following-sibling::*").extract()[0]
            ielts = ''.join(ielts)
            ielts = re.findall('\d\.\d',ielts)[0]
        except:
            ielts = 6
        try:
            ielts_l = response.xpath("//*[contains(text(),'Listening')]//following-sibling::*").extract()[0]
            ielts_l = ''.join(ielts_l)
            ielts_l = re.findall('\d\.\d', ielts_l)[0]
        except:
            ielts_l = 5.5
        try:
            ielts_r = response.xpath("//*[contains(text(),'Reading')]//following-sibling::*").extract()[0]
            ielts_r = ''.join(ielts_r)
            ielts_r = re.findall('\d\.\d', ielts_r)[0]
        except:
            ielts_r = 5.5
        try:
            ielts_s = response.xpath("//*[contains(text(),'Speaking')]//following-sibling::*").extract()[0]
            ielts_s = ''.join(ielts_s)
            ielts_s = re.findall('\d\.\d', ielts_s)[0]
        except:
            ielts_s = 5.5
        try:
            ielts_w = response.xpath("//*[contains(text(),'Writing')]//following-sibling::*").extract()[0]
            ielts_w = ''.join(ielts_w)
            ielts_w = re.findall('\d\.\d', ielts_w)[0]
        except:
            ielts_w = 5.5
        # print(ielts,ielts_w,ielts_l,ielts_s,ielts_r)

        #21.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'Overseas students (non-EU)')]/../following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #22.tuition_fee_pre
        tuition_fee_pre = '£'

        #23.apply_proces_en
        try:
            apply_proces_en  = response.xpath("//*[contains(text(),'Apply now')]//@href").extract()[0]
        except:
            apply_proces_en = 'N/A'
        # print(apply_proces_en)
        #24.apply_pre
        apply_pre = '£'

        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['start_date'] = start_date
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['department'] = department
        item['teach_time'] = teach_time
        item['overview_en'] = overview_en
        item['assessment_en'] = assessment_en
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['rntry_requirements'] = rntry_requirements
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_proces_en'] = apply_proces_en
        yield item