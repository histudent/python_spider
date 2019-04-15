# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '18-7-17 上午9:57'
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
from scrapySchool_England.getTuition_fee import getT_fee
class UniversityoftheWestofEnglandSpider(scrapy.Spider):
    name = 'UniversityoftheWestofEngland_p'
    allowed_domains = ['uwe.ac.uk/']
    start_urls = []
    C = [
        'https://courses.uwe.ac.uk/H3N21/automation-and-computer-vision',
        'https://courses.uwe.ac.uk/W6201/cinematography',
        'https://courses.uwe.ac.uk/H60C12/embedded-systems-and-wireless-networks',
        'https://courses.uwe.ac.uk/B82A1/radiotherapy-and-oncology',
        'https://courses.uwe.ac.uk/P3101/creative-producing',
        'https://courses.uwe.ac.uk/B9611/physician-associate-studies',
        'https://courses.uwe.ac.uk/K23A12/building-surveying',
        'https://courses.uwe.ac.uk/BL9412/public-health',
        'https://courses.uwe.ac.uk/C9001/biomedical-science',
        'https://courses.uwe.ac.uk/M3AC12/advanced-legal-practice-lpc-llm',
        'https://courses.uwe.ac.uk/N6001/human-resource-management-international',
        'https://courses.uwe.ac.uk/B90032/environmental-health',
        'https://courses.uwe.ac.uk/M99A1/bar-professional-training-studiespgdip-bptc',
        'https://courses.uwe.ac.uk/N12212/master-of-business-administration-mba-full-time',
        'https://courses.uwe.ac.uk/W6411/photography',
        'https://courses.uwe.ac.uk/CB8942/health-psychology',
        'https://courses.uwe.ac.uk/KN231/real-estate-finance-and-investment',
        'https://courses.uwe.ac.uk/KN4112/real-estate-management',
        'https://courses.uwe.ac.uk/C1841/advanced-wildlife-conservation-in-practice',
        'https://courses.uwe.ac.uk/W9911/culture',
        'https://courses.uwe.ac.uk/K9011/architecture-design-and-the-built-environment',
        'https://courses.uwe.ac.uk/G3901/data-science',
        'https://courses.uwe.ac.uk/F8101/geography-and-environmental-management',
        'https://courses.uwe.ac.uk/W21D12/graphic-arts',
        'https://courses.uwe.ac.uk/F8NA1/sustainable-development-in-practice',
        'https://courses.uwe.ac.uk/N630M2/human-resource-management',
        'https://courses.uwe.ac.uk/P39A1/documentary-production',
        'https://courses.uwe.ac.uk/F7901/urban-design',
        'https://courses.uwe.ac.uk/K2101/building-information-modelling-bim-in-design-construction-and-operations',
        'https://courses.uwe.ac.uk/K90012/construction-project-management',
        'https://courses.uwe.ac.uk/L1501/global-political-economy',
        'https://courses.uwe.ac.uk/P50012/journalism',
        'https://courses.uwe.ac.uk/G70012/software-engineering',
        'https://courses.uwe.ac.uk/K4911/urban-planning',
        'https://courses.uwe.ac.uk/D4P31/wildlife-filmmaking',
        'https://courses.uwe.ac.uk/H20H1/civil-engineering',
        'https://courses.uwe.ac.uk/P3121/radio-documentary',
        'https://courses.uwe.ac.uk/N20B12/business-management',
        'https://courses.uwe.ac.uk/H9N21/engineering-business-management',
        'https://courses.uwe.ac.uk/H19012/engineering-management',
        'https://courses.uwe.ac.uk/H30B12/mechanical-engineering',
        'https://courses.uwe.ac.uk/P11012/information-management',
        'https://courses.uwe.ac.uk/W92012/animation',
        'https://courses.uwe.ac.uk/I9001/cyber-security',
        'https://courses.uwe.ac.uk/K90D1/facade-engineering',
        'https://courses.uwe.ac.uk/K4931/planning-major-projects',
        'https://courses.uwe.ac.uk/W3701/music-technology',
        'https://courses.uwe.ac.uk/I7101/virtual-reality',
        'https://courses.uwe.ac.uk/B9191/environmental-health-professional-practice',
        'https://courses.uwe.ac.uk/H67A1/robotics',
        'https://courses.uwe.ac.uk/P30B1/contemporary-film-culture',
        'https://courses.uwe.ac.uk/I9W91/creative-technology',
        'https://courses.uwe.ac.uk/W90L12/curating',
        'https://courses.uwe.ac.uk/WW1212/multi-disciplinary-printmaking',
        'https://courses.uwe.ac.uk/H67B1/robotics',
        'https://courses.uwe.ac.uk/M34C12/international-trade-and-economic-law',
        'https://courses.uwe.ac.uk/G56A12/information-technology',
        'https://courses.uwe.ac.uk/M34A12/commercial-law',
        'https://courses.uwe.ac.uk/M29A1/environmental-law-and-sustainable-development',
        'https://courses.uwe.ac.uk/M29A2/international-banking-and-finance-law',
        'https://courses.uwe.ac.uk/M30G12/international-law',
        'https://courses.uwe.ac.uk/K10B1/architecture',
        'https://courses.uwe.ac.uk/F1N21/environmental-management',
        'https://courses.uwe.ac.uk/B70U1/specialist-practice-district-nursing',
        'https://courses.uwe.ac.uk/F90012/environmental-consultancy',
        'https://courses.uwe.ac.uk/N34012/accounting-and-financial-management',
        'https://courses.uwe.ac.uk/N39012/finance',
        'https://courses.uwe.ac.uk/P90012/science-communication',
        'https://courses.uwe.ac.uk/N9011/innovation-and-applied-entrepreneurship',
        'https://courses.uwe.ac.uk/K46D1/transport-engineering-and-planning',
        'https://courses.uwe.ac.uk/K4N912/transport-planning',
        'https://courses.uwe.ac.uk/N14512/international-management',
        'https://courses.uwe.ac.uk/K24012/quantity-surveying',
        'https://courses.uwe.ac.uk/H1011/engineering',
        'https://courses.uwe.ac.uk/I6001/commercial-games-development',
        'https://courses.uwe.ac.uk/N50212/marketing-communications',
        'https://courses.uwe.ac.uk/N8201/events-management',
        'https://courses.uwe.ac.uk/N50012/marketing',
        'https://courses.uwe.ac.uk/HK111/building-services-engineering',
        'https://courses.uwe.ac.uk/C8BA1/social-sciences',
        'https://courses.uwe.ac.uk/C99K1/applied-sciences',
        'https://courses.uwe.ac.uk/C8901/sport-and-exercise-psychology'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of the West of England'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="content"]/div//h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_name
        degree_name = response.xpath("//div[@class='m-course__header__details']//p").extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        if '/' in degree_name:
            degree_name =  degree_name.split('/')[0]
        else:
            pass
        # print(degree_name)

        #5.degree_type
        degree_type = 2

        #6.department
        department = response.xpath("//*[contains(text(),'Department:')]//following-sibling::dd[1]").extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #7.location
        location = response.xpath("//*[contains(text(),'Campus:')]//following-sibling::dd[1]").extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #8.duration #9.duration_per
        duration_list = response.xpath("//*[contains(text(),'Duration:')]//following-sibling::dd[1]").extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        # print(duration_list)
        if 'One year' in duration_list:
            duration = 1
            duration_per = 1
        elif 'Two years' in duration_list:
            duration = 2
            duration_per = 1
        elif 'Six months' in duration_list:
            duration = 6
            duration_per = 3
        elif 'one year' in duration_list:
            duration = 1
            duration_per = 1
        elif 'Three years' in duration_list:
            duration = 3
            duration_per = 1
        elif 'Nine months' in duration_list:
            duration = 9
            duration_per = 3
        elif 'five years' in duration_list:
            duration = 5
            duration_per = 1
        elif 'four years' in duration_list:
            duration = 4
            duration_per = 1
        elif  len(re.findall('\d+',duration_list))!=0:
            duration = re.findall('\d+',duration_list)[0]
            if int(duration)>5:
                duration_per = 3
            else:duration_per = 1
        else :
            duration = 1
            duration_per = 1
        # print(duration,"****",duration_per)

        #10.teach_time
        teach_time = response.xpath("//*[contains(text(),'Delivery')]//following-sibling::dd[1]").extract()
        teach_time = ''.join(teach_time)
        if 'Full-time' in teach_time:
            teach_time = 'Full-time'
        elif 'full-time' in teach_time:
            teach_time = 'Full-time'
        else:teach_time = 'Part-time'
        # print(teach_time)

        #11.overview_en
        overview_en = response.xpath("//h2/a[contains(text(),'Introduction')]/../following-sibling::*").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en).strip()
        # print(overview_en)

        #12.modules_en
        modules_en = response.xpath("//*[contains(text(),'Content')]//following-sibling::*").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en).strip()
        end = modules_en.find('<h3>Learning and Teaching</h3>')
        modules_en = modules_en[:end]
        # print(modules_en)

        #13.assessment_en
        assessment_en = response.xpath("//h3[contains(text(),'Assessment')]//following-sibling::*").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #14.career_en
        career_en = response.xpath("//h3[contains(text(),'Careers')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #15.rntry_requirements
        rntry_requirements = response.xpath("//h3[contains(text(),'Entry requirements')]//following-sibling::*").extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #16.tuition_fee
        tuition_fee= response.xpath("//*[contains(text(),'International-Full Time-Award Fee')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = getT_fee(tuition_fee)
        # print(tuition_fee)

        #17.tuition_fee_pre
        tuition_fee_pre = '£'

        #18.ielts 19202122
        ielts=6.5
        ielts_r = 5.5
        ielts_s = 5.5
        ielts_l = 5.5
        ielts_w = 5.5
        #23.toefl 24252627
        toefl = 90
        toefl_l =17
        toefl_w =17
        toefl_r =18
        toefl_s =20
        #28.apply_pre
        apply_pre = '£'

        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['toefl_l'] = toefl_l
        item['toefl_s'] = toefl_s
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_name'] = degree_name
        item['degree_type'] = degree_type
        item['department'] = department
        item['location'] = location
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['teach_time'] = teach_time
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['rntry_requirements'] = rntry_requirements
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['ielts'] = ielts
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['ielts_r'] = ielts_r
        yield item