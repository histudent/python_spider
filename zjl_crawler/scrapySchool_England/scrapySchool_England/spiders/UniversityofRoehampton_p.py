# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/16 10:37'
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
class UniversityofRoehamptonSpider(scrapy.Spider):
    name = 'UniversityofRoehampton_p'
    allowed_domains = ['roehampton.ac.uk/']
    start_urls = []
    C= [
        'http://www.roehampton.ac.uk/postgraduate-courses/cell-biomedicine/',
        'http://www.roehampton.ac.uk/postgraduate-courses/audiovisual-translation/',
        'http://www.roehampton.ac.uk/postgraduate-courses/anthropology-of-health/',
        'http://www.roehampton.ac.uk/postgraduate-courses/biomechanics/',
        'http://www.roehampton.ac.uk/postgraduate-courses/applied-linguistics-and-tesol/',
        'http://www.roehampton.ac.uk/postgraduate-courses/attachment-studies/',
        'http://www.roehampton.ac.uk/postgraduate-courses/choreography/',
        'http://www.roehampton.ac.uk/postgraduate-courses/choreomundus/',
        'http://www.roehampton.ac.uk/postgraduate-courses/childrens-literature/',
        'http://www.roehampton.ac.uk/postgraduate-courses/choreography-and-performance-mres/',
        'http://www.roehampton.ac.uk/postgraduate-courses/art-psychotherapy/',
        'http://www.roehampton.ac.uk/postgraduate-courses/classical-research/',
        'http://www.roehampton.ac.uk/postgraduate-courses/creative-writing-specialist-pathway/',
        'http://www.roehampton.ac.uk/postgraduate-courses/dance-movement-psychotherapy/',
        'http://www.roehampton.ac.uk/postgraduate-courses/creative-writing/',
        'http://www.roehampton.ac.uk/postgraduate-courses/dramatherapy/',
        'http://www.roehampton.ac.uk/postgraduate-courses/dance-philosophy-and-history/',
        'http://www.roehampton.ac.uk/postgraduate-courses/dance-politics-and-sociology/',
        'http://www.roehampton.ac.uk/postgraduate-courses/clinical-neuroscience/',
        'http://www.roehampton.ac.uk/postgraduate-courses/dance-anthropology/',
        'http://www.roehampton.ac.uk/postgraduate-courses/education-policy/',
        'http://www.roehampton.ac.uk/postgraduate-courses/education-leadership-and-management/',
        'http://www.roehampton.ac.uk/postgraduate-courses/erasmus-mundus-human-rights-policy-and-practice/',
        'http://www.roehampton.ac.uk/postgraduate-courses/education-studies/',
        'http://www.roehampton.ac.uk/postgraduate-courses/early-childhood-studies/',
        'http://www.roehampton.ac.uk/postgraduate-courses/forensic-psychology/',
        'http://www.roehampton.ac.uk/postgraduate-courses/global-criminology/',
        'http://www.roehampton.ac.uk/postgraduate-courses/clinical-nutrition/',
        'http://www.roehampton.ac.uk/postgraduate-courses/film-and-screen-cultures/',
        'http://www.roehampton.ac.uk/postgraduate-courses/global-financial-management/',
        'http://www.roehampton.ac.uk/postgraduate-courses/global-business-management/',
        'http://www.roehampton.ac.uk/postgraduate-courses/global-marketing/',
        'http://www.roehampton.ac.uk/postgraduate-courses/health-sciences/',
        'http://www.roehampton.ac.uk/postgraduate-courses/global-human-resources-management/',
        'http://www.roehampton.ac.uk/postgraduate-courses/human-rights-and-international-relations/',
        'http://www.roehampton.ac.uk/postgraduate-courses/human-rights/',
        'http://www.roehampton.ac.uk/postgraduate-courses/history/',
        'http://www.roehampton.ac.uk/postgraduate-courses/llm-human-rights-and-legal-practice/',
        'http://www.roehampton.ac.uk/postgraduate-courses/intercultural-communication-in-the-creative-industries/',
        'http://www.roehampton.ac.uk/postgraduate-courses/history-ma/',
        'http://www.roehampton.ac.uk/postgraduate-courses/journalism/',
        'http://www.roehampton.ac.uk/postgraduate-courses/londons-theatre-and-performance/',
        'http://www.roehampton.ac.uk/postgraduate-courses/master-of-business-administration/',
        'http://www.roehampton.ac.uk/postgraduate-courses/media-communication-and-culture/',
        'http://www.roehampton.ac.uk/postgraduate-courses/nutrition-and-metabolic-disorders/',
        'http://www.roehampton.ac.uk/postgraduate-courses/music-therapy/',
        'http://www.roehampton.ac.uk/postgraduate-courses/primate-biology-behaviour-and-conservation/',
        'http://www.roehampton.ac.uk/postgraduate-courses/psychology-of-sport-and-exercise/',
        'http://www.roehampton.ac.uk/postgraduate-courses/publishing/',
        'http://www.roehampton.ac.uk/postgraduate-courses/play-therapy/',
        'http://www.roehampton.ac.uk/postgraduate-courses/sen-disability-and-inclusive-education/',
        'http://www.roehampton.ac.uk/postgraduate-courses/sport-and-exercise-physiology/',
        'http://www.roehampton.ac.uk/postgraduate-courses/specialised-translation/',
        'http://www.roehampton.ac.uk/postgraduate-courses/sport-and-exercise-science/',
        'http://www.roehampton.ac.uk/postgraduate-courses/stress-and-health/',
        'http://www.roehampton.ac.uk/postgraduate-courses/theology-and-religious-studies/',
        'http://www.roehampton.ac.uk/postgraduate-courses/sport-and-exercise-science-mres/',
        'http://www.roehampton.ac.uk/postgraduate-courses/social-research-methods/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Roehampton'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="wrapper"]/div/figure/figcaption/div/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en).replace('Postgraduate','')
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        degree_name = response.xpath("//*[contains(text(),'Degree type')]//following-sibling::*").extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #6.overview_en
        overview_en = response.xpath("//*[contains(text(),'Summary')]//following-sibling::*[1]").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #7.department
        department = response.xpath("//h3[contains(text(),'Department')]//following-sibling::*").extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #8.duration #9.duration_per #10.teach_time
        duration_list = response.xpath("//h3[contains(text(),'Duration')]//following-sibling::*").extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        # print(duration_list)
        try:
            duration = re.findall('\d+',duration_list)[0]
        except:
            duration = 1
        if int(duration)>10:
            duration_per = 4
        else:
            duration_per = 1
        if 'full-time' in duration_list:
            teach_time = 'full-time'
        else:
            teach_time = 'part-time'
        # print(duration,teach_time,duration_per)

        #11.start_date
        start_date = response.xpath("//h3[contains(text(),'Programme start')]//following-sibling::*").extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        # print(start_date)
        if 'September' in start_date:
            start_date = '2018-9'
        elif 'October' in start_date:
            start_date = '2018-10'
        else:
            start_date = '2018-9'
        # print(start_date)

        #12.tuition_fee
        tuition_fee = response.xpath("//h3[contains(text(),'Tuition Fees (per year)')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #13.tuition_fee_pre
        tuition_fee_pre = '£'

        #14.rntry_requirements
        rntry_requirements = response.xpath('//*[@id="accordion-2"]/div[1]').extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #15.ielts 16171819
        ielts = 6.5
        ielts_l = 5.5
        ielts_w = 5.5
        ielts_r = 5.5
        ielts_s = 5.5

        #20.toefl 21222324
        toefl = 89
        toefl_r = 18
        toefl_w = 17
        toefl_l = 17
        toefl_s = 20

        #25.modules_en
        modules_en = response.xpath('//*[@id="accordion"]/div[2]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #26.career_en
        career_en = response.xpath("//*[contains(text(),'Career options')]/../following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en).strip()
        # print(career_en)

        #27.apply_pre
        apply_pre = '£'

        #28.apply_proces_en
        apply_proces_en ='<p>You can apply to us now for any postgraduate degree starting in 2018.Postgraduate programmes You can apply to us now for any postgraduate degree starting in 2018.All postgraduate taught applications can be made via our online application form. Check our application deadlines View our entry requirements for postgraduate programmes View our general entry criteria If you need any help or advice with your application, or just want to ask us a question before you apply, please do not hesitate to contact us. International studentsPlease note that most international applicants have to pay a deposit before securing their place.</p>'

        item['apply_pre'] = apply_pre
        item['apply_proces_en'] = apply_proces_en
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['department'] = department
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['teach_time'] = teach_time
        item['start_date'] = start_date
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['rntry_requirements'] = rntry_requirements
        item['ielts'] = ielts
        item['ielts_l'] = ielts_l
        item['ielts_w'] = ielts_w
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['toefl'] = toefl
        item['toefl_l'] = toefl_l
        item['toefl_s'] = toefl_s
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        yield item