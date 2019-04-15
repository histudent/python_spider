# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/2 14:47'
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
from translate import translate
import requests
from lxml import etree
from bs4 import  BeautifulSoup
class KinstonUniversitySpider(scrapy.Spider):
    name = 'KinstonUniversity_u'
    allowed_domains = ['kingston.ac.uk/']
    start_urls = []
    C = [
        'https://www.kingston.ac.uk/undergraduate-course/pharmaceutical-science-mpharm/',
        'https://www.kingston.ac.uk/undergraduate-course/pharmacy/',
        'https://www.kingston.ac.uk/undergraduate-course/pharmacy/',
        'https://www.kingston.ac.uk/undergraduate-course/aerospace-engineering/',
        'https://www.kingston.ac.uk/undergraduate-course/astronautics-space-technology/',
        'https://www.kingston.ac.uk/undergraduate-course/aerospace-engineering/',
        'https://www.kingston.ac.uk/undergraduate-course/astronautics-space-technology/',
        'https://www.kingston.ac.uk/undergraduate-course/aerospace-engineering/',
        'https://www.kingston.ac.uk/undergraduate-course/astronautics-space-technology/',
        'https://www.kingston.ac.uk/undergraduate-course/aerospace-engineering/',
        'https://www.kingston.ac.uk/undergraduate-course/astronautics-space-technology/',
        'https://www.kingston.ac.uk/undergraduate-course/mechanical-engineering-beng/',
        'https://www.kingston.ac.uk/undergraduate-course/mechanical-engineering-beng/',
        'https://www.kingston.ac.uk/undergraduate-course/mechanical-engineering-beng/',
        'https://www.kingston.ac.uk/undergraduate-course/mechanical-engineering-beng/',
        'https://www.kingston.ac.uk/undergraduate-course/mechanical-engineering-beng/',
        'https://www.kingston.ac.uk/undergraduate-course/mechanical-engineering-beng/',
        'https://www.kingston.ac.uk/undergraduate-course/mechanical-engineering-beng/',
        'https://www.kingston.ac.uk/undergraduate-course/mechanical-engineering-beng/',
        'https://www.kingston.ac.uk/undergraduate-course/mechanical-engineering-beng/',
        'https://www.kingston.ac.uk/undergraduate-course/chemistry-mchem/',
        'https://www.kingston.ac.uk/undergraduate-course/law-llb/',
        'https://www.kingston.ac.uk/undergraduate-course/law-llb/',
        'https://www.kingston.ac.uk/undergraduate-course/international-law/',
        'https://www.kingston.ac.uk/undergraduate-course/international-law/',
        'https://www.kingston.ac.uk/undergraduate-course/adult-nursing/',
        'https://www.kingston.ac.uk/undergraduate-course/accounting-finance/',
        'https://www.kingston.ac.uk/undergraduate-course/accounting-finance/',
        'https://www.kingston.ac.uk/undergraduate-course/aerospace-engineering-bsc/',
        'https://www.kingston.ac.uk/undergraduate-course/aviation-operations-and-technology/',
        'https://www.kingston.ac.uk/undergraduate-course/aerospace-engineering-bsc/',
        'https://www.kingston.ac.uk/undergraduate-course/aviation-operations-and-technology/',
        'https://www.kingston.ac.uk/undergraduate-course/aerospace-engineering-bsc/',
        'https://www.kingston.ac.uk/undergraduate-course/biomedical-science-bsc/',
        'https://www.kingston.ac.uk/undergraduate-course/biomedical-science-bsc/',
        'https://www.kingston.ac.uk/undergraduate-course/biomedical-science-bsc/',
        'https://www.kingston.ac.uk/undergraduate-course/biochemistry-bsc/',
        'https://www.kingston.ac.uk/undergraduate-course/biochemistry-bsc/',
        'https://www.kingston.ac.uk/undergraduate-course/biochemistry-bsc/',
        'https://www.kingston.ac.uk/undergraduate-course/building-surveying/',
        'https://www.kingston.ac.uk/undergraduate-course/building-surveying/',
        'https://www.kingston.ac.uk/undergraduate-course/biological-sciences/',
        'https://www.kingston.ac.uk/undergraduate-course/biological-sciences/',
        'https://www.kingston.ac.uk/undergraduate-course/biological-sciences/',
        'https://www.kingston.ac.uk/undergraduate-course/childrens-nursing/',
        'https://www.kingston.ac.uk/undergraduate-course/construction-management/',
        'https://www.kingston.ac.uk/undergraduate-course/construction-management/',
        'https://www.kingston.ac.uk/undergraduate-course/business-economics/',
        'https://www.kingston.ac.uk/undergraduate-course/business-economics/',
        'https://www.kingston.ac.uk/undergraduate-course/criminology/',
        'https://www.kingston.ac.uk/undergraduate-course/criminology/',
        'https://www.kingston.ac.uk/undergraduate-course/mathematics/',
        'https://www.kingston.ac.uk/undergraduate-course/mathematics/',
        'https://www.kingston.ac.uk/undergraduate-course/mathematics/',
        'https://www.kingston.ac.uk/undergraduate-course/marketing-advertising/',
        'https://www.kingston.ac.uk/undergraduate-course/international-business/',
        'https://www.kingston.ac.uk/undergraduate-course/marketing-advertising/',
        'https://www.kingston.ac.uk/undergraduate-course/international-business/',
        'https://www.kingston.ac.uk/undergraduate-course/learning-disability-nursing/',
        'https://www.kingston.ac.uk/undergraduate-course/mental-health-nursing/',
        'https://www.kingston.ac.uk/undergraduate-course/midwifery/',
        'https://www.kingston.ac.uk/undergraduate-course/midwifery-registered-nurses/',
        'https://www.kingston.ac.uk/undergraduate-course/pharmaceutical-science-bsc/',
        'https://www.kingston.ac.uk/undergraduate-course/pharmaceutical-science-bsc/',
        'https://www.kingston.ac.uk/undergraduate-course/pharmaceutical-science-bsc/',
        'https://www.kingston.ac.uk/undergraduate-course/digital-media-technology/',
        'https://www.kingston.ac.uk/undergraduate-course/digital-media-technology/',
        'https://www.kingston.ac.uk/undergraduate-course/pharmacology/',
        'https://www.kingston.ac.uk/undergraduate-course/digital-media-technology/',
        'https://www.kingston.ac.uk/undergraduate-course/pharmacology/',
        'https://www.kingston.ac.uk/undergraduate-course/pharmacology/',
        'https://www.kingston.ac.uk/undergraduate-course/psychology/',
        'https://www.kingston.ac.uk/undergraduate-course/psychology/',
        'https://www.kingston.ac.uk/undergraduate-course/psychology-with-criminology/',
        'https://www.kingston.ac.uk/undergraduate-course/psychology-with-criminology/',
        'https://www.kingston.ac.uk/undergraduate-course/psychology-with-criminology/',
        'https://www.kingston.ac.uk/undergraduate-course/sociology-and-international-relations/',
        'https://www.kingston.ac.uk/undergraduate-course/sociology-and-international-relations/',
        'https://www.kingston.ac.uk/undergraduate-course/real-estate-management/',
        'https://www.kingston.ac.uk/undergraduate-course/sociology/',
        'https://www.kingston.ac.uk/undergraduate-course/psychology-with-sociology/',
        'https://www.kingston.ac.uk/undergraduate-course/real-estate-management/',
        'https://www.kingston.ac.uk/undergraduate-course/sociology/',
        'https://www.kingston.ac.uk/undergraduate-course/psychology-with-sociology/',
        'https://www.kingston.ac.uk/undergraduate-course/quantity-surveying-consultancy/',
        'https://www.kingston.ac.uk/undergraduate-course/nutrition/',
        'https://www.kingston.ac.uk/undergraduate-course/real-estate-management/',
        'https://www.kingston.ac.uk/undergraduate-course/psychology-with-sociology/',
        'https://www.kingston.ac.uk/undergraduate-course/quantity-surveying-consultancy/',
        'https://www.kingston.ac.uk/undergraduate-course/nutrition/',
        'https://www.kingston.ac.uk/undergraduate-course/nutrition-exercise-health/',
        'https://www.kingston.ac.uk/undergraduate-course/nutrition/',
        'https://www.kingston.ac.uk/undergraduate-course/nutrition-exercise-health/',
        'https://www.kingston.ac.uk/undergraduate-course/nutrition-exercise-health/',
        'https://www.kingston.ac.uk/undergraduate-course/sport-science/',
        'https://www.kingston.ac.uk/undergraduate-course/sport-science-coaching/',
        'https://www.kingston.ac.uk/undergraduate-course/sport-science/',
        'https://www.kingston.ac.uk/undergraduate-course/sport-science-coaching/',
        'https://www.kingston.ac.uk/undergraduate-course/sport-science/',
        'https://www.kingston.ac.uk/undergraduate-course/sport-science-coaching/',
        'https://www.kingston.ac.uk/undergraduate-course/criminology-and-forensic-psychology/',
        'https://www.kingston.ac.uk/undergraduate-course/criminology-and-international-relations/',
        'https://www.kingston.ac.uk/undergraduate-course/criminology-and-forensic-psychology/',
        'https://www.kingston.ac.uk/undergraduate-course/criminology-and-international-relations/',
        'https://www.kingston.ac.uk/undergraduate-course/chemistry-bsc/',
        'https://www.kingston.ac.uk/undergraduate-course/computer-games-programming/',
        'https://www.kingston.ac.uk/undergraduate-course/criminology-and-forensic-psychology/',
        'https://www.kingston.ac.uk/undergraduate-course/criminology-and-international-relations/',
        'https://www.kingston.ac.uk/undergraduate-course/chemistry-bsc/',
        'https://www.kingston.ac.uk/undergraduate-course/computer-games-programming/',
        'https://www.kingston.ac.uk/undergraduate-course/business-management/',
        'https://www.kingston.ac.uk/undergraduate-course/criminology-and-sociology/',
        'https://www.kingston.ac.uk/undergraduate-course/criminology-and-sociology/',
        'https://www.kingston.ac.uk/undergraduate-course/criminology-and-sociology/',
        'https://www.kingston.ac.uk/undergraduate-course/business-management/',
        'https://www.kingston.ac.uk/undergraduate-course/computer-games-programming/',
        'https://www.kingston.ac.uk/undergraduate-course/chemistry-bsc/',
        'https://www.kingston.ac.uk/undergraduate-course/digital-business/',
        'https://www.kingston.ac.uk/undergraduate-course/digital-business/',
        'https://www.kingston.ac.uk/undergraduate-course/computer-science/',
        'https://www.kingston.ac.uk/undergraduate-course/entrepreneurship-and-innovation-management/',
        'https://www.kingston.ac.uk/undergraduate-course/computer-science/',
        'https://www.kingston.ac.uk/undergraduate-course/computer-science/',
        'https://www.kingston.ac.uk/undergraduate-course/geography/',
        'https://www.kingston.ac.uk/undergraduate-course/geography/',
        'https://www.kingston.ac.uk/undergraduate-course/geography/',
        'https://www.kingston.ac.uk/undergraduate-course/financial-economics/',
        'https://www.kingston.ac.uk/undergraduate-course/financial-economics/',
        'https://www.kingston.ac.uk/undergraduate-course/forensic-science/',
        'https://www.kingston.ac.uk/undergraduate-course/forensic-science/',
        'https://www.kingston.ac.uk/undergraduate-course/forensic-psychology/',
        'https://www.kingston.ac.uk/undergraduate-course/forensic-psychology/',
        'https://www.kingston.ac.uk/undergraduate-course/aircraft-engineering/',
        'https://www.kingston.ac.uk/undergraduate-course/civil-and-infrastructure-engineering/',
        'https://www.kingston.ac.uk/undergraduate-course/civil-and-infrastructure-engineering/',
        'https://www.kingston.ac.uk/undergraduate-course/civil-and-infrastructure-engineering/',
        'https://www.kingston.ac.uk/undergraduate-course/business-joint-honours/',
        'https://www.kingston.ac.uk/undergraduate-course/architecture/',
        'https://www.kingston.ac.uk/undergraduate-course/art-design-history-practice/',
        'https://www.kingston.ac.uk/undergraduate-course/creative-and-cultural-industries-art-direction/',
        'https://www.kingston.ac.uk/undergraduate-course/creative-and-cultural-industries-design-marketing/',
        'https://www.kingston.ac.uk/undergraduate-course/creative-and-cultural-industries-curation-exhibition-events/',
        'https://www.kingston.ac.uk/undergraduate-course/english-history/',
        'https://www.kingston.ac.uk/undergraduate-course/english-history/',
        'https://www.kingston.ac.uk/undergraduate-course/film-cultures/',
        'https://www.kingston.ac.uk/undergraduate-course/global-politics-and-international-relations/',
        'https://www.kingston.ac.uk/undergraduate-course/global-politics-and-international-relations/',
        'https://www.kingston.ac.uk/undergraduate-course/global-politics-and-international-relations/',
        'https://www.kingston.ac.uk/undergraduate-course/graphic-design/',
        'https://www.kingston.ac.uk/undergraduate-course/history-and-international-relations/',
        'https://www.kingston.ac.uk/undergraduate-course/history-and-international-relations/',
        'https://www.kingston.ac.uk/undergraduate-course/history/',
        'https://www.kingston.ac.uk/undergraduate-course/human-geography/',
        'https://www.kingston.ac.uk/undergraduate-course/human-geography/',
        'https://www.kingston.ac.uk/undergraduate-course/human-geography/',
        'https://www.kingston.ac.uk/undergraduate-course/human-rights-and-criminology/',
        'https://www.kingston.ac.uk/undergraduate-course/human-rights-and-criminology/',
        'https://www.kingston.ac.uk/undergraduate-course/human-rights-and-criminology/',
        'https://www.kingston.ac.uk/undergraduate-course/human-rights-and-history/',
        'https://www.kingston.ac.uk/undergraduate-course/human-rights-and-history/',
        'https://www.kingston.ac.uk/undergraduate-course/human-rights-and-history/',
        'https://www.kingston.ac.uk/undergraduate-course/human-rights-and-social-justice/',
        'https://www.kingston.ac.uk/undergraduate-course/human-rights-and-social-justice/',
        'https://www.kingston.ac.uk/undergraduate-course/human-rights-and-social-justice/',
        'https://www.kingston.ac.uk/undergraduate-course/drama-creative-writing-ba/',
        'https://www.kingston.ac.uk/undergraduate-course/drama-creative-writing-ba/',
        'https://www.kingston.ac.uk/undergraduate-course/human-rights-and-sociology/',
        'https://www.kingston.ac.uk/undergraduate-course/human-rights-and-sociology/',
        'https://www.kingston.ac.uk/undergraduate-course/human-rights-and-sociology/',
        'https://www.kingston.ac.uk/undergraduate-course/media-and-global-politics/',
        'https://www.kingston.ac.uk/undergraduate-course/media-and-global-politics/',
        'https://www.kingston.ac.uk/undergraduate-course/interior-design/',
        'https://www.kingston.ac.uk/undergraduate-course/illustration-animation/',
        'https://www.kingston.ac.uk/undergraduate-course/journalism/',
        'https://www.kingston.ac.uk/undergraduate-course/journalism-and-media/',
        'https://www.kingston.ac.uk/undergraduate-course/journalism/',
        'https://www.kingston.ac.uk/undergraduate-course/journalism-and-media/',
        'https://www.kingston.ac.uk/undergraduate-course/journalism-and-media/',
        'https://www.kingston.ac.uk/undergraduate-course/media-communication/',
        'https://www.kingston.ac.uk/undergraduate-course/media-communication/',
        'https://www.kingston.ac.uk/undergraduate-course/popular-music/',
        'https://www.kingston.ac.uk/undergraduate-course/popular-music/',
        'https://www.kingston.ac.uk/undergraduate-course/product-furniture-design/',
        'https://www.kingston.ac.uk/undergraduate-course/primary-teaching-qts/',
        'https://www.kingston.ac.uk/undergraduate-course/photography/',
        'https://www.kingston.ac.uk/undergraduate-course/social-work/',
        'https://www.kingston.ac.uk/undergraduate-course/music-technology/',
        'https://www.kingston.ac.uk/undergraduate-course/music-technology/',
        'https://www.kingston.ac.uk/undergraduate-course/working-with-children-young-people/',
        'https://www.kingston.ac.uk/undergraduate-course/dance/',
        'https://www.kingston.ac.uk/undergraduate-course/dance/',
        'https://www.kingston.ac.uk/undergraduate-course/creative-writing-and-film-cultures/',
        'https://www.kingston.ac.uk/undergraduate-course/dance-and-drama/',
        'https://www.kingston.ac.uk/undergraduate-course/education/',
        'https://www.kingston.ac.uk/undergraduate-course/drama-and-film-cultures/',
        'https://www.kingston.ac.uk/undergraduate-course/dance-and-drama/',
        'https://www.kingston.ac.uk/undergraduate-course/drama/',
        'https://www.kingston.ac.uk/undergraduate-course/drama-english/',
        'https://www.kingston.ac.uk/undergraduate-course/drama/',
        'https://www.kingston.ac.uk/undergraduate-course/drama-english/',
        'https://www.kingston.ac.uk/undergraduate-course/english-and-creative-writing/',
        'https://www.kingston.ac.uk/undergraduate-course/english-and-creative-writing/',
        'https://www.kingston.ac.uk/undergraduate-course/filmmaking/',
        'https://www.kingston.ac.uk/undergraduate-course/english-language-linguistics/',
        'https://www.kingston.ac.uk/undergraduate-course/fine-art-history/',
        'https://www.kingston.ac.uk/undergraduate-course/fine-art/',
        'https://www.kingston.ac.uk/undergraduate-course/english-literature/',
        'https://www.kingston.ac.uk/undergraduate-course/english-literature/'
    ]
    for i in C:
        start_urls.append(i)

    start_urls = list(set(start_urls))
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Kingston University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en #4.degree_name
        programme_en = response.xpath('//*[@id="middle-col"]/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        programme_en = programme_en.replace('&amp; ','')
        if '(' in programme_en:
            degree_name_a = re.findall(r'[A-Za-z/]+\(Hons\)',programme_en)[0]
            degree_name = degree_name_a.replace('(Hons)','')
        else:
            degree_name_a = ''
            degree_name = ''
        if len(degree_name_a)!=0:
            programme_en = programme_en.replace(degree_name_a,'')
        programme_en = programme_en.replace('  ',' ')
        # print(programme_en)
        # print(degree_name)

        #5.degree_type
        degree_type = 1


        #6.start_date
        start_date = '2018-9,2019-1,2019-4'

        #7.overview_en
        overview_en = response.xpath("//h2[contains(text(),'What you will study')]/preceding-sibling::*").extract()
        overview_en = ''.join(overview_en)
        overview_en = clear_space_str(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #8.assessment_en
        assessment_url = url +'teaching-learning-assessment.html'
        # print(assessment_url)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        data = requests.get(assessment_url, headers=headers)
        response_assessment_en = etree.HTML(data.text)
        assessment_en = response_assessment_en.xpath('//*[@id="middle-col"]/div[2]/p//text()')
        assessment_en = ''.join(assessment_en)
        # print(assessment_en)

        #9.modules_en
        modules_en =response.xpath('//*[@id="modulelist"]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #10.alevel
        alevel_url = url+'entry-requirements.html'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        data = requests.get(alevel_url, headers=headers)
        response_alevel = etree.HTML(data.text)
        alevel = response_alevel.xpath("//*[contains(text(),'evel')]/.//text()")
        alevel = ''.join(alevel)
        # print(alevel,url)

        #11.ielts 12131415
        if 'Health' in programme_en:
            ielts = 6.5
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        elif 'Social Care' in programme_en:
            ielts = 6.5
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        elif 'Education' in programme_en:
            ielts = 6.5
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        elif 'Journalism' in programme_en:
            ielts = 6.5
            ielts_r = 5.5
            ielts_w = 6.5
            ielts_l = 5.5
            ielts_s = 5.5
        elif 'Nursing' in programme_en:
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_l = 7.0
            ielts_s = 7.0
        elif 'Nutrition' in programme_en:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_l = 6.0
            ielts_s = 6.0
        else:
            ielts = 6.0
            ielts_r = 5.5
            ielts_w = 6.5
            ielts_l = 5.5
            ielts_s = 5.5

        #16.tuition_fee
        tuition_fee_url = url+'fees-and-funding.html'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        data = requests.get(tuition_fee_url, headers=headers)
        response_tuition_fee = etree.HTML(data.text)
        tuition_fee = response_tuition_fee.xpath('//*[@id="middle-col"]/div[2]/table/tbody/tr[3]/td[2]//text()')
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)


        #17.tuition_fee_pre
        tuition_fee_pre = '£'

        #18.apply_proces_en
        apply_proces_en = response.url +'apply-now.html'
        # print(apply_proces_en)

        #19.career_en
        career_en_url =  url+'after-you-graduate.html'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        data = requests.get(career_en_url, headers=headers)
        response_career_en = etree.HTML(data.text)
        career_en = response_career_en.xpath("//h2[contains(text(),'Careers and progression')]/../..")
        doc = ""
        if len(career_en) > 0:
            for a in career_en:
                doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                doc = remove_class(doc)
        career_en = ''.join(doc)
        # print(career_en)

        #20.location
        location = 'London'

        #21.apply_pre
        apply_pre = '£'


        item['alevel'] = alevel
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_name'] = degree_name
        item['degree_type'] = degree_type
        item['start_date'] = start_date
        item['overview_en'] = overview_en
        item['assessment_en'] = assessment_en
        item['modules_en'] = modules_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_proces_en'] = apply_proces_en
        item['career_en'] = career_en
        item['location'] = location

        # 22.ucascode
        ucascode = response.xpath('//*[@id="middle-col"]//table//tr/td').extract()
        ucascode = ''.join(ucascode)
        # ucascode = remove_tags(ucascode)
        # ucascode = re.findall(r'<td>(.*)</td>',ucascode)
        ucas = re.findall('td>([A-Z][A-Z0-9]{3})', ucascode)
        # if len(ucas) == 1:
        #     ucascode = ucas[0]
        # elif len(ucascode)>1:
        #     ucascode = ''.join(ucas)
        # else:ucascode = ''
        print(ucas,'---')
        item['duration'] = None
        item['other'] = ''
        item['ucascode'] = ''
        if len(ucas) > 0:
            response_duration = []
            for i in ucas:
                response_ucascode = i
                xpaths = '//*[contains(text(),' + str(response_ucascode) + ')]//preceding-sibling::td[contains(text(),"full time")]'
                response_duration = response.xpath(xpaths).extract()
            # print(response_duration, '===')

            if len(ucas) == len(response_duration):
                for j in range(len(ucas)):
                    duration_major = response_duration[j].replace('<td>','').replace('</td>','')
                    duration = re.findall('\d', duration_major)[0]
                    item['duration'] = duration
                    item['other'] = duration_major
                    item['ucascode'] = ucas[j]

                    print("==========================", str(j))
                    print(item['duration'] , '---')
                    print(item['other'] , '---')
                    print(item['ucascode'] , '---')

                    yield item
            else:

                yield item
        else:

            yield item
                # if len(ucas) == 1:
        #     xpathss = '//*[contains(text(),'+str(ucascode)+')]//preceding-sibling::td[1]'
        #     duration = response.xpath(xpathss).extract()
        #     duration = ''.join(duration)
        #     try:
        #         duration = re.findall('\d', duration)[0]
        #     except:
        #         duration = ''
        # else:
        #     duration = ''
        #
        # if len(ucas) > 1:
        #     for i in ucas:
        #         response_ucascode = i
        #         xpaths = '//*[contains(text(),'+str(response_ucascode)+')]//preceding-sibling::td[contains(text(),"full time")]'
        #         response_duration = response.xpath(xpaths).extract()
        #         print(response_duration, '===')
        #         response_duration = ''.join(response_duration)
        #         try:
        #             response_duration = re.findall('\d',response_duration)[0]
        #         except:
        #             response_duration = ''
        #         item['ucascode'] = response_ucascode
        #         item['duration'] = response_duration
        #
        #         yield item
        # else:
        #     item['ucascode'] = ucascode
        #     item['duration'] = duration
        #     yield item







