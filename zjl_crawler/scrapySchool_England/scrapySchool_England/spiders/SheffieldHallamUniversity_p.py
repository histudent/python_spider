# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/5 16:51'
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
from scrapySchool_England.TranslateMonth import translate_month
class SheffieldHallamUniversitySpider(scrapy.Spider):
    name = 'SheffieldHallamUniversity_p'
    allowed_domains = ['shu.ac.uk/']
    start_urls = []
    C = [
        'https://www.shu.ac.uk/courses/media-pr-and-journalism/ma-journalism/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/ma-fine-art/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/ma-design-interaction/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/mfa-design-packaging/full-time/2018',
        'https://www.shu.ac.uk/courses/media-pr-and-journalism/ma-international-journalism/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/mfa-design-interaction/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/mfa-design-interior/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/mfa-design-product/full-time/2018',
        'https://www.shu.ac.uk/courses/accounting-banking-and-finance/msc-wealth-management/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/ma-design-fashion/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/mfa-design-jewellery-and-metalwork/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/mfa-design-illustration/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/ma-design-graphics/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/mfa-design-fashion/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/mfa-fine-art/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/mfa-design-graphics/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/ma-design-illustration/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/ma-design-interior/full-time/2018',
        'https://www.shu.ac.uk/courses/architecture/msc-technical-architecture/full-time/2018',
        'https://www.shu.ac.uk/courses/food-and-nutrition/msc-food-consumer-marketing-and-product-development-with-work-experience/full-time/2018',
        'https://www.shu.ac.uk/courses/food-and-nutrition/msc-food-consumer-marketing-and-product-development-with-work-experience/full-time/2018',
        'https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-pharmaceutical-analysis/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/ma-design-product/full-time/2018',
        'https://www.shu.ac.uk/courses/accounting-banking-and-finance/msc-banking-and-finance/full-time/2018',
        'https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-biomedical-sciences/full-time/2018',
        'https://www.shu.ac.uk/courses/accounting-banking-and-finance/msc-finance-and-investment/full-time/2018',
        'https://www.shu.ac.uk/courses/engineering/msc-logistics-and-supply-chain-management/full-time/2018',
        'https://www.shu.ac.uk/courses/food-and-nutrition/msc-food-consumer-marketing-and-product-development/full-time/2018',
        'https://www.shu.ac.uk/courses/engineering/msc-telecommunication-and-electronic-engineering/full-time/2018',
        'https://www.shu.ac.uk/courses/media-pr-and-journalism/ma-sports-journalism/full-time/2018',
        'https://www.shu.ac.uk/courses/engineering/msc-advanced-engineering/full-time/2018',
        'https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-biotechnology/full-time/2018',
        'https://www.shu.ac.uk/courses/history/mhr-history-by-research/full-time/2018',
        'https://www.shu.ac.uk/courses/media-pr-and-journalism/ma-public-relations/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/ma-design-packaging/full-time/2018',
        'https://www.shu.ac.uk/courses/accounting-banking-and-finance/msc-accounting-and-finance/full-time/2018',
        'https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-pharmacology-and-biotechnology/full-time/2018',
        'https://www.shu.ac.uk/courses/engineering/msc-advanced-materials-engineering/full-time/2018',
        'https://www.shu.ac.uk/courses/engineering/msc-food-processing-engineering/full-time/2018',
        'https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-analytical-chemistry/full-time/2018',
        'https://www.shu.ac.uk/courses/engineering/msc-advanced-engineering-and-management/full-time/2018',
        'https://www.shu.ac.uk/courses/engineering/msc-automation-control-and-robotics/full-time/2018',
        'https://www.shu.ac.uk/courses/food-and-nutrition/msc-food-and-nutrition-sciences/full-time/2018',
        'https://www.shu.ac.uk/courses/business-and-management/msc-international-human-resource-management/full-time/2018',
        'https://www.shu.ac.uk/courses/business-and-management/msc-entrepreneurship/full-time/2018',
        'https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-molecular-and-cell-biology/full-time/2018',
        'https://www.shu.ac.uk/courses/radiotherapy-and-oncology/msc-radiotherapy-and-oncology-in-practice/full-time/2018',
        'https://www.shu.ac.uk/courses/tourism-and-hospitality/msc-international-tourism-management/full-time/2018',
        'https://www.shu.ac.uk/courses/business-and-management/mres-business/full-time/2018',
        'https://www.shu.ac.uk/courses/tourism-and-hospitality/msc-international-hospitality-management/full-time/2018',
        'https://www.shu.ac.uk/courses/engineering/msc-mechanical-engineering/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/ma-arts-and-cultural-management/full-time/2018',
        'https://www.shu.ac.uk/courses/construction-real-estate-and-surveying/msc-urban-planning/full-time/2018',
        'https://www.shu.ac.uk/courses/tourism-and-hospitality/msc-international-hospitality-and-tourism-management/full-time/2018',
        'https://www.shu.ac.uk/courses/accounting-banking-and-finance/msc-forensic-accounting/full-time/2018',
        'https://www.shu.ac.uk/courses/occupational-therapy/msc-occupational-therapy-preregistration/full-time/2018',
        'https://www.shu.ac.uk/courses/engineering/msc-advanced-mechanical-engineering/full-time/2018',
        'https://www.shu.ac.uk/courses/psychology/msc-clinical-cognitive-neuroscience/full-time/2018',
        'https://www.shu.ac.uk/courses/construction-real-estate-and-surveying/msc-real-estate/full-time/2018',
        'https://www.shu.ac.uk/courses/digital-media/ma-games-design/full-time/2018',
        'https://www.shu.ac.uk/courses/law/llmr-master-of-laws-by-research/full-time/2018',
        'https://www.shu.ac.uk/courses/geography-and-environment/msc-environmental-management/full-time/2018',
        'https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-biomedical-laboratory-sciences/full-time/2018',
        'https://www.shu.ac.uk/courses/health-and-social-care-management/msc-public-health/full-time/2018',
        'https://www.shu.ac.uk/courses/construction-real-estate-and-surveying/msc-quantity-surveying/full-time/2018',
        'https://www.shu.ac.uk/courses/law/llm-legal-professional-practice/full-time/2018',
        'https://www.shu.ac.uk/courses/geography-and-environment/msc-geographical-information-systems/full-time/2018',
        'https://www.shu.ac.uk/courses/construction-real-estate-and-surveying/msc-building-surveying/full-time/2018',
        'https://www.shu.ac.uk/courses/teaching-and-education/ma-education/full-time/2018',
        'https://www.shu.ac.uk/courses/event-management/msc-international-events-and-conference-management/full-time/2018',
        'https://www.shu.ac.uk/courses/food-and-nutrition/msc-nutrition-with-public-health-management/full-time/2018',
        'https://www.shu.ac.uk/courses/psychology/msc-developmental-psychology/full-time/2018',
        'https://www.shu.ac.uk/courses/computing/msc-information-systems-security/full-time/2018',
        'https://www.shu.ac.uk/courses/mba/mba-master-of-business-administration/full-time/2018',
        'https://www.shu.ac.uk/courses/law/llm-applied-human-rights/full-time/2018',
        'https://www.shu.ac.uk/courses/computing/msc-computing/full-time/2018',
        'https://www.shu.ac.uk/courses/physiotherapy/msc-physiotherapy-preregistration/full-time/2018',
        'https://www.shu.ac.uk/courses/psychology/msc-health-psychology/full-time/2018',
        'https://www.shu.ac.uk/courses/teaching-and-education/ma-teaching-english-to-speakers-of-other-languages-tesol/full-time/2018',
        'https://www.shu.ac.uk/courses/law/ma-applied-human-rights/full-time/2018',
        'https://www.shu.ac.uk/courses/construction-real-estate-and-surveying/msc-construction-project-management/full-time/2018',
        'https://www.shu.ac.uk/courses/business-and-management/msc-international-business-management/full-time/2018',
        'https://www.shu.ac.uk/courses/english/ma-creative-writing/full-time/2018',
        'https://www.shu.ac.uk/courses/psychology/msc-psychology/full-time/2018',
        'https://www.shu.ac.uk/courses/art-and-design/ma-design-jewellery-and-metalwork/full-time/2018',
        'https://www.shu.ac.uk/courses/sociology-and-politics/ma-international-relations-and-global-crises/full-time/2018',
        'https://www.shu.ac.uk/courses/computing/msc-games-software-development/full-time/2018',
        'https://www.shu.ac.uk/courses/digital-media/ma-filmmaking/full-time/2018',
        'https://www.shu.ac.uk/courses/geography-and-environment/msc-urban-planning/full-time/2018',
        'https://www.shu.ac.uk/courses/digital-media/ma-animation-and-digital-effects/full-time/2018',
        'https://www.shu.ac.uk/courses/mba/mba-industrial-management/full-time/2018',
        'https://www.shu.ac.uk/courses/computing/msc-advanced-computer-networks/full-time/2018',
        'https://www.shu.ac.uk/courses/marketing/msc-international-marketing/full-time/2018',
        'https://www.shu.ac.uk/courses/accounting-banking-and-finance/msc-financial-management/full-time/2018',
        'https://www.shu.ac.uk/courses/sport-and-physical-activity/msc-applied-sport-and-exercise-science/full-time/2018',
        'https://www.shu.ac.uk/courses/computing/msc-big-data-analytics/full-time/2018',
        'https://www.shu.ac.uk/courses/english/mer-english-by-research/full-time/2018',
        'https://www.shu.ac.uk/courses/sociology-and-politics/mres-social-science/full-time/2018',
        'https://www.shu.ac.uk/courses/sport-and-physical-activity/msc-sports-engineering/full-time/2018',
        'https://www.shu.ac.uk/courses/computing/msc-information-technology-management/full-time/2018',
        'https://www.shu.ac.uk/courses/digital-media/ma-digital-media-management/full-time/2018',
        'https://www.shu.ac.uk/courses/sport-and-physical-activity/msc-sport-and-exercise-psychology/full-time/2018',
        'https://www.shu.ac.uk/courses/business-and-management/msc-human-resource-management/full-time/2018',
        'https://www.shu.ac.uk/courses/sport-and-physical-activity/msc-sport-business-management/full-time/2018'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Sheffield Hallam University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath("/html/body/section[1]//h1").extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        degree_name = response.xpath('/html/body/section[1]/div/div[2]/span').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #6.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'What is the fee?')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee =getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #7.tuition_fee_pre
        tuition_fee_pre = '£'

        #8.duration
        duration_list = response.xpath("//*[contains(text(),'How long will I study?')]//following-sibling::*").extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        try:
            duration = re.findall('\d+',duration_list)[0]
        except:
            duration = 1
        # print(duration_list)
        if int(duration)>5:
            duration_per = 3
        else:duration_per = 1
        # print(duration,'*********',duration_per)

        #9.location
        location = 'Sheffield'

        #10.teach_time
        teach_time = response.xpath('/html/body/section[1]//span[1]').extract()
        teach_time = ''.join(teach_time)
        teach_time = remove_tags(teach_time)
        if 'Full-time' in teach_time:
            teach_time = 'Full-time'
        else:
            teach_time = 'Part-time'
        # print(teach_time)

        #11.overview_en
        overview_en = response.xpath("//*[contains(text(),'Course summary')]//following-sibling::*").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #12.career_en
        career_en = response.xpath("//*[contains(text(),'Future careers')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        career_en = clear_space_str(career_en)
        # print(career_en)

        #13.rntry_requirements
        rntry_requirements = response.xpath('//*[@id="entry-requirements"]/div').extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #14.modules_en
        modules_en = response.xpath("//*[contains(text(),'Compulsory modules')]/../following-sibling::*").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        modules_en = clear_space_str(modules_en)
        # print(modules_en)

        #15.apply_proces_en
        apply_proces_en = response.xpath('//*[@id="apply-now"]/div[1]//a/@href').extract()
        apply_proces_en = ''.join(apply_proces_en)
        # print(apply_proces_en)

        #16.duration_per
        duration_per = 1

        #17.ielts 18192021
        ielts_list = re.findall(r'[567]\.\d',rntry_requirements)
        # print(ielts_list,response.url)
        if len(ielts_list)!=0:
            a = ielts_list[0]
            b = ielts_list[1]
            ielts = a
            ielts_r = b
            ielts_l = b
            ielts_s = b
            ielts_w = b
        else:
            ielts = 6.5
            ielts_r = 6.0
            ielts_l = 6.0
            ielts_s = 6.0
            ielts_w = 6.0

        #22.require_chinese_en
        require_chinese_en = '<p>The following qualifications from China will be considered for entry on to postgraduate taught programmes, with a usual minimum average of 60 per cent Four year Bachelor Degree from a recognised university Three year university diploma plus relevant work experience Successful completion of a recognised pre-masters course</p>'
        #23.apply_fre
        apply_pre = '£'
        #24.start_date
        start_date = response.xpath("//*[contains(text(),'When do I start?')]//following-sibling::*").extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        start_date = clear_space_str(start_date)
        # print(start_date)
        if'September, January' in start_date:
            start_date = '2018-9,2019-1'
        elif 'January' in start_date:
            start_date = '2019-1'
        else:
            start_date = translate_month(start_date)
            start_date = '2018-'+str(start_date)
        # print(start_date)


        item['start_date'] = start_date
        item['apply_pre'] = apply_pre
        item['require_chinese_en'] = require_chinese_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['duration'] = duration
        item['location'] = location
        item['teach_time'] = teach_time
        item['overview_en'] = overview_en
        item['career_en'] = career_en
        item['rntry_requirements'] = rntry_requirements
        item['modules_en'] = modules_en
        item['apply_proces_en'] = apply_proces_en
        item['duration_per'] = duration_per
        yield  item