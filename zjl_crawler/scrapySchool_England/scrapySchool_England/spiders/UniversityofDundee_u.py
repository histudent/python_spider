# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/26 16:44'
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
    name = 'UniversityofDundee_u'
    allowed_domains = ['dundee.ac.uk/']
    start_urls = []
    C= [
        'https://www.dundee.ac.uk/study/ug/law-eng-ni/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/law-eng-ni/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/law-eng-ni-oil-gas-law/',
        'https://www.dundee.ac.uk/study/ug/law-eng-ni/',
        'https://www.dundee.ac.uk/study/ug/law-eng-ni/',
        'https://www.dundee.ac.uk/study/ug/law-scots-eng-dual/',
        'https://www.dundee.ac.uk/study/ug/mathematics-and-astrophysics/',
        'https://www.dundee.ac.uk/study/ug/mathematics/',
        'https://www.dundee.ac.uk/study/ug/physics-with-astrophysics/',
        'https://www.dundee.ac.uk/study/ug/physics/',
        'https://www.dundee.ac.uk/study/ug/physiological-sciences/',
        'https://www.dundee.ac.uk/study/ug/mathematics/',
        'https://www.dundee.ac.uk/study/ug/physics/',
        'https://www.dundee.ac.uk/study/ug/product-design/',
        'https://www.dundee.ac.uk/study/ug/renewables/',
        'https://www.dundee.ac.uk/study/ug/politics-international-relations/',
        'https://www.dundee.ac.uk/study/ug/mathematics/',
        'https://www.dundee.ac.uk/study/ug/oral-health-sciences/',
        'https://www.dundee.ac.uk/study/ug/neuroscience/',
        'https://www.dundee.ac.uk/study/ug/pharmacology/',
        'https://www.dundee.ac.uk/study/ug/philosophy/',
        'https://www.dundee.ac.uk/study/ug/psychology/',
        'https://www.dundee.ac.uk/study/ug/renewables/',
        'https://www.dundee.ac.uk/study/ug/politics-international-relations/',
        'https://www.dundee.ac.uk/study/ug/mathematics/',
        'https://www.dundee.ac.uk/study/ug/philosophy/',
        'https://www.dundee.ac.uk/study/ug/psychology/',
        'https://www.dundee.ac.uk/study/ug/social-work/',
        'https://www.dundee.ac.uk/study/ug/renewables/',
        'https://www.dundee.ac.uk/study/ug/politics-international-relations/',
        'https://www.dundee.ac.uk/study/ug/mathematics/',
        'https://www.dundee.ac.uk/study/ug/textile-design/',
        'https://www.dundee.ac.uk/study/ug/philosophy/',
        'https://www.dundee.ac.uk/study/ug/psychology/',
        'https://www.dundee.ac.uk/study/ug/politics-international-relations/',
        'https://www.dundee.ac.uk/study/ug/mathematics/',
        'https://www.dundee.ac.uk/study/ug/philosophy/',
        'https://www.dundee.ac.uk/study/ug/psychology/',
        'https://www.dundee.ac.uk/study/ug/politics-international-relations/',
        'https://www.dundee.ac.uk/study/ug/mathematics/',
        'https://www.dundee.ac.uk/study/ug/philosophy/',
        'https://www.dundee.ac.uk/study/ug/psychology/',
        'https://www.dundee.ac.uk/study/ug/politics-international-relations/',
        'https://www.dundee.ac.uk/study/ug/philosophy/',
        'https://www.dundee.ac.uk/study/ug/town-regional-planning/',
        'https://www.dundee.ac.uk/study/ug/psychology/',
        'https://www.dundee.ac.uk/study/ug/politics-international-relations/',
        'https://www.dundee.ac.uk/study/ug/philosophy/',
        'https://www.dundee.ac.uk/study/ug/psychology/',
        'https://www.dundee.ac.uk/study/ug/politics-international-relations/',
        'https://www.dundee.ac.uk/study/ug/philosophy/',
        'https://www.dundee.ac.uk/study/ug/psychology/',
        'https://www.dundee.ac.uk/study/ug/politics-international-relations/',
        'https://www.dundee.ac.uk/study/ug/philosophy/',
        'https://www.dundee.ac.uk/study/ug/psychology/',
        'https://www.dundee.ac.uk/study/ug/politics-international-relations/',
        'https://www.dundee.ac.uk/study/ug/philosophy/',
        'https://www.dundee.ac.uk/study/ug/psychology/',
        'https://www.dundee.ac.uk/study/ug/politics-international-relations/',
        'https://www.dundee.ac.uk/study/ug/philosophy/',
        'https://www.dundee.ac.uk/study/ug/psychology/',
        'https://www.dundee.ac.uk/study/ug/philosophy/',
        'https://www.dundee.ac.uk/study/ug/psychology/',
        'https://www.dundee.ac.uk/study/ug/philosophy/',
        'https://www.dundee.ac.uk/study/ug/psychology/',
        'https://www.dundee.ac.uk/study/ug/psychology/',
        'https://www.dundee.ac.uk/study/ug/psychology/',
        'https://www.dundee.ac.uk/study/ug/psychology/',
        'https://www.dundee.ac.uk/study/ug/anatomical-sciences/',
        'https://www.dundee.ac.uk/study/ug/applied-computing/',
        'https://www.dundee.ac.uk/study/ug/applied-computing-human-computer-interaction/',
        'https://www.dundee.ac.uk/study/ug/applied-computing-games-dundee-angus-college/',
        'https://www.dundee.ac.uk/study/ug/biological-biomedical-singapore/',
        'https://www.dundee.ac.uk/study/ug/accountancy/',
        'https://www.dundee.ac.uk/study/ug/animation/',
        'https://www.dundee.ac.uk/study/ug/nursing/',
        'https://www.dundee.ac.uk/study/ug/accountancy/',
        'https://www.dundee.ac.uk/study/ug/nursing/',
        'https://www.dundee.ac.uk/study/ug/biochemistry/',
        'https://www.dundee.ac.uk/study/ug/biological-chemistry-drug-discovery/',
        'https://www.dundee.ac.uk/study/ug/accountancy/',
        'https://www.dundee.ac.uk/study/ug/nursing/',
        'https://www.dundee.ac.uk/study/ug/biochemistry/',
        'https://www.dundee.ac.uk/study/ug/biological-chemistry-drug-discovery/',
        'https://www.dundee.ac.uk/study/ug/accountancy/',
        'https://www.dundee.ac.uk/study/ug/nursing/',
        'https://www.dundee.ac.uk/study/ug/community-learning-development/',
        'https://www.dundee.ac.uk/study/ug/biological-sciences/',
        'https://www.dundee.ac.uk/study/ug/biomedical-engineering/',
        'https://www.dundee.ac.uk/study/ug/business-management/',
        'https://www.dundee.ac.uk/study/ug/business-management-accounting-finance/',
        'https://www.dundee.ac.uk/study/ug/biochemistry/',
        'https://www.dundee.ac.uk/study/ug/accountancy/',
        'https://www.dundee.ac.uk/study/ug/nursing/',
        'https://www.dundee.ac.uk/study/ug/biological-sciences/',
        'https://www.dundee.ac.uk/study/ug/civil-engineering/',
        'https://www.dundee.ac.uk/study/ug/biomedical-sciences/',
        'https://www.dundee.ac.uk/study/ug/accountancy/',
        'https://www.dundee.ac.uk/study/ug/nursing/',
        'https://www.dundee.ac.uk/study/ug/education/',
        'https://www.dundee.ac.uk/study/ug/electronic-engineering/',
        'https://www.dundee.ac.uk/study/ug/civil-engineering/',
        'https://www.dundee.ac.uk/study/ug/biomedical-sciences/',
        'https://www.dundee.ac.uk/study/ug/accountancy/',
        'https://www.dundee.ac.uk/study/ug/electronic-engineering/',
        'https://www.dundee.ac.uk/study/ug/architecture-studies/',
        'https://www.dundee.ac.uk/study/ug/applied-physics/',
        'https://www.dundee.ac.uk/study/ug/art-philosophy/',
        'https://www.dundee.ac.uk/study/ug/english-film-studies/',
        'https://www.dundee.ac.uk/study/ug/computing-science/',
        'https://www.dundee.ac.uk/study/ug/architecture/',
        'https://www.dundee.ac.uk/study/ug/english-film-studies/',
        'https://www.dundee.ac.uk/study/ug/dentistry/',
        'https://www.dundee.ac.uk/study/ug/digital-interaction-design/',
        'https://www.dundee.ac.uk/study/ug/english-film-studies/',
        'https://www.dundee.ac.uk/study/ug/english-film-studies/',
        'https://www.dundee.ac.uk/study/ug/environmental-science/',
        'https://www.dundee.ac.uk/study/ug/environmental-sustainability/',
        'https://www.dundee.ac.uk/study/ug/forensic-anthropology/',
        'https://www.dundee.ac.uk/study/ug/finance/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/english-film-studies/',
        'https://www.dundee.ac.uk/study/ug/environmental-science/',
        'https://www.dundee.ac.uk/study/ug/environmental-science-dundee-angus-college/',
        'https://www.dundee.ac.uk/study/ug/environmental-sustainability/',
        'https://www.dundee.ac.uk/study/ug/fine-art/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/english-film-studies/',
        'https://www.dundee.ac.uk/study/ug/environmental-science/',
        'https://www.dundee.ac.uk/study/ug/environmental-sustainability/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/english-film-studies/',
        'https://www.dundee.ac.uk/study/ug/geography/',
        'https://www.dundee.ac.uk/study/ug/european-studies/',
        'https://www.dundee.ac.uk/study/ug/history/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/english-film-studies/',
        'https://www.dundee.ac.uk/study/ug/geography/',
        'https://www.dundee.ac.uk/study/ug/european-studies/',
        'https://www.dundee.ac.uk/study/ug/history/',
        'https://www.dundee.ac.uk/study/ug/illustration/',
        'https://www.dundee.ac.uk/study/ug/interior-environmental-design/',
        'https://www.dundee.ac.uk/study/ug/graphic-design/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/english-film-studies/',
        'https://www.dundee.ac.uk/study/ug/geography/',
        'https://www.dundee.ac.uk/study/ug/european-studies/',
        'https://www.dundee.ac.uk/study/ug/history/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/english-film-studies/',
        'https://www.dundee.ac.uk/study/ug/geography/',
        'https://www.dundee.ac.uk/study/ug/law-dual-qualifying-oil-gas-law/',
        'https://www.dundee.ac.uk/study/ug/european-studies/',
        'https://www.dundee.ac.uk/study/ug/history/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/english-film-studies/',
        'https://www.dundee.ac.uk/study/ug/geography/',
        'https://www.dundee.ac.uk/study/ug/international-business/',
        'https://www.dundee.ac.uk/study/ug/international-finance/',
        'https://www.dundee.ac.uk/study/ug/law-scots/',
        'https://www.dundee.ac.uk/study/ug/european-studies/',
        'https://www.dundee.ac.uk/study/ug/history/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/english-film-studies/',
        'https://www.dundee.ac.uk/study/ug/geography/',
        'https://www.dundee.ac.uk/study/ug/international-business/',
        'https://www.dundee.ac.uk/study/ug/law-scots/',
        'https://www.dundee.ac.uk/study/ug/european-studies/',
        'https://www.dundee.ac.uk/study/ug/history/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/english-film-studies/',
        'https://www.dundee.ac.uk/study/ug/geography/',
        'https://www.dundee.ac.uk/study/ug/international-business/',
        'https://www.dundee.ac.uk/study/ug/law-scots/',
        'https://www.dundee.ac.uk/study/ug/european-studies/',
        'https://www.dundee.ac.uk/study/ug/history/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/geography/',
        'https://www.dundee.ac.uk/study/ug/international-business/',
        'https://www.dundee.ac.uk/study/ug/law-scots-oil-gas-law/',
        'https://www.dundee.ac.uk/study/ug/liberal-arts/',
        'https://www.dundee.ac.uk/study/ug/law-scots/',
        'https://www.dundee.ac.uk/study/ug/european-studies/',
        'https://www.dundee.ac.uk/study/ug/history/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/geography/',
        'https://www.dundee.ac.uk/study/ug/international-business/',
        'https://www.dundee.ac.uk/study/ug/liberal-arts/',
        'https://www.dundee.ac.uk/study/ug/european-studies/',
        'https://www.dundee.ac.uk/study/ug/history/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/international-business/',
        'https://www.dundee.ac.uk/study/ug/mathematical-biology/',
        'https://www.dundee.ac.uk/study/ug/european-studies/',
        'https://www.dundee.ac.uk/study/ug/history/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/mechanical-engineering/',
        'https://www.dundee.ac.uk/study/ug/international-business/',
        'https://www.dundee.ac.uk/study/ug/mathematical-biology/',
        'https://www.dundee.ac.uk/study/ug/european-studies/',
        'https://www.dundee.ac.uk/study/ug/history/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/international-business/',
        'https://www.dundee.ac.uk/study/ug/medicine/',
        'https://www.dundee.ac.uk/study/ug/history/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/international-business/',
        'https://www.dundee.ac.uk/study/ug/history/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/international-business/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/international-business/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/international-business/',
        'https://www.dundee.ac.uk/study/ug/jewellery-metal-design/',
        'https://www.dundee.ac.uk/study/ug/microbiology/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/',
        'https://www.dundee.ac.uk/study/ug/economic-studies/'
    ]
    C =set(C)
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
        programme_en =response.xpath("//table[@class='table table-striped-no unstackable table-kis']//tbody//tr//td[2]").extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        if '(Hons)' in programme_en:
            programme_en = programme_en.replace('(Hons)','').strip()
            try:
                degree_name = programme_en.split()[-1]
            except:
                degree_name = ''
        else:
            try:
                degree_name = programme_en.split()[-1]
            except:
                degree_name = ''
        programme_en = programme_en.replace(degree_name,'').strip()

        #4.degree_type
        degree_type = 1



        #6.start_date
        start_date = '2019-9'
        # print(start_date)

        #7.duration #8.duration_per
        duration_list = response.xpath('//*[@id="maincontent"]/ul/li[2]/text()').extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        if len(duration_list)==0:
            duration_list = response.xpath('//*[@id="maincontent"]/div/div[1]/div/div/div/div[2]/ul/li[2]').extract()
            duration_list = ''.join(duration_list)
            duration_list = remove_tags(duration_list)
        try:
            duration = re.findall('\d+',duration_list)[0]
        except:
            duration = None
        # print(duration)
        duration_per = 1
        # print(duration,'***************',duration_per)

        #9.alevel
        alevel = response.xpath("//*[contains(text(),'GCE A-Level')]//following-sibling::*[1]").extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel)
        # print(alevel)

        #10.ucascode
        ucascode = response.xpath("//table[@class='table table-striped-no unstackable table-kis']//tbody//tr//td[3]").extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode)
        # print(ucascode)

        #11.overview_en
        overview_en = response.xpath("//*[contains(text(),'Overview')]/../following-sibling::p").extract()
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
        modules_en = response.xpath("//*[contains(text(),'What you will study')]//following-sibling::*").extract()
        modules_en = ''.join(modules_en)
        modules_en =remove_class(modules_en)
        # print(modules_en)

        #14.career_en
        career_en = response.xpath("//h1[contains(text(),'Careers')]/../following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #15.ib
        ib = response.xpath("//*[contains(text(),'International Baccalaureate')]//following-sibling::*[1]").extract()
        ib = ''.join(ib)
        ib = remove_tags(ib)
        # print(ib)

        #16.ielts 17181920
        try:
            ielts = response.xpath("//*[contains(text(),'IELTS Overall')]//following-sibling::*").extract()[0]
            ielts = ''.join(ielts)
            ielts = re.findall('\d\.\d',ielts)[0]
        except:
            ielts = 6.0
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
            ielts_w = 6.0
        # print(ielts,ielts_w,ielts_l,ielts_s,ielts_r)

        #21.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'Overseas students (non-EU)')]/../following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #22.tuition_fee_pre
        tuition_fee_pre = '£'

        #23.apply_proces_en
        apply_proces_en  = 'https://www.dundee.ac.uk/clearing/'
        # print(apply_proces_en)


        #24.apply_pre
        apply_pre = '£'

        #25.major
        major = response.xpath("//table[@class='table table-striped-no unstackable table-kis']//tbody//tr//td[2]").extract()
        response_ucascode = response.xpath("//table[@class='table table-striped-no unstackable table-kis']//tbody//tr//td[3]").extract()

        #26.ucascode

        item['ib'] = ib
        item['alevel'] = alevel
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['start_date'] = start_date
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['overview_en'] = overview_en
        item['assessment_en'] = assessment_en
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_proces_en'] = apply_proces_en
        item['ucascode'] = None
        yield item
        # if len(major)>0:
        #     for i,j in zip(major,response_ucascode):
        #         response_programme_en = i
        #         response_programme_en = remove_tags(response_programme_en)
        #         if '(Hons)' in response_programme_en:
        #             response_programme_en = response_programme_en.replace('(Hons)', '').strip()
        #             try:
        #                 response_degree_name = response_programme_en.split()[-1]
        #             except:
        #                 response_degree_name = ''
        #         else:
        #             try:
        #                 response_degree_name = response_programme_en.split()[-1]
        #             except:
        #                 response_degree_name = ''
        #         response_programme_en = response_programme_en.replace(response_degree_name, '').strip().replace('&amp; ','')
        #         response_ucascode1 = j
        #         response_ucascode1 = remove_tags(response_ucascode1)
        #         item['programme_en'] = response_programme_en
        #         item['ucascode'] = response_ucascode1
        #         item['degree_name'] = response_degree_name
        #         yield item
        # else:
        #     item['programme_en'] = programme_en
        #     item['ucascode'] = ucascode
        #     item['degree_name'] = degree_name
        #     yield item


