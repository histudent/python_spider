# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.clearSpace import clear_same_s
from scrapySchool_England.middlewares import clear_duration
class DemontfortuniversityPSpider(CrawlSpider):
    name = 'DeMontfortUniversity_P'
    allowed_domains = ['dmu.ac.uk']
    start_urls = ['https://www.dmu.ac.uk/study/courses/postgraduate-courses/postgraduate-courses.aspx']
    rules = (
        Rule(LinkExtractor(allow=r'https://www.dmu.ac.uk/study/courses/postgraduate-courses/postgraduate-courses.aspx\?courselisting1_List_GoToPage=\d+'), follow=True),
        Rule(LinkExtractor(restrict_xpaths='//tbody/tr/td/a'),follow=False,callback='parse'),
    )
    def parse(self,response):
        item=get_item1(ScrapyschoolEnglandItem1)
        print(response.url)
        Internationnal = response.xpath('//div[@data-kftab="2"]//text()').extract()
        # print(response.url)
        Course = response.xpath(
            '//div[@class="block__details block__details--overlay block__details--courseOverlay"]//h1[@class="block__details__title"]//text()').extract()[
            0]
        Course = Course.strip()
        Master = re.findall('[A-Z]{1}[A-Za-z]{1,3}\s?\([a-zA-Z]*\)', Course)
        Master = ''.join(Master)
        programme = Course.replace(Master, '')
        if Master == '':
            Master = re.findall('MA|MSc', Course)
            Master = ''.join(Master)
            # print(Master, Course, response.url)
        else:
            Master = ''
        # 专业描述
        CourseOverview = response.xpath('//div[@class="block large-8 columns course-col2"]').extract()
        overview = remove_class(CourseOverview)
        overview = clear_same_s(overview)
        # 学费
        tuition_fee=response.xpath('//*[contains(text(),"£")]//text()').extract()
        tuition_fee=getTuition_fee(tuition_fee)
        # print(tuition_fee)

        # 课程长度
        duration=response.xpath('//*[contains(text(),"uration")]/..//text()').extract()
        mode=re.findall('(?i)full',''.join(duration))
        if mode!=[]:
            mode='1'
        else:
            mode='2'
        try:
            duration=clear_duration(duration)
        except:
            duration={'duration_per': None, 'duration': None}
        print(duration)

        # 申请要求
        standard = response.xpath(
            '//div[@class="row row--block course-section course-section--criteria"]').extract()
        standard = remove_class(standard)
        standard = clear_same_s(standard)

        # 课程及评估
        Evaluation_method = response.xpath('//div[@id="cycle-slideshow_course"]').extract()
        Evaluation_method = remove_class(Evaluation_method)
        Evaluation_method = clear_same_s(Evaluation_method)
        teaching_assessment = Evaluation_method.strip()

        # 就业
        Career = response.xpath('//div[@class="row row--block course-section course-section--opps"]').extract()
        career = remove_class(Career)
        career = clear_same_s(career)
        # print(Career)
        IELTS=response.xpath('//*[contains(text(),"IELTS")]//text()').extract()
        # print(IELTS)
        ielts=get_ielts(IELTS)
        # print(IELTS)
        if ielts!={} and ielts!=[]:
            item['ielts_l']= ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            item['ielts'] = ielts['IELTS']
        else:
            item['ielts'] = ''
            item['ielts_l'] = ''
            item['ielts_s'] = ''
            item['ielts_r'] = ''
            item['ielts_w'] = ''
        # print(tuition_fee)
        university = 'De Montfort University'
        programme=programme.replace(Master,'').strip()

        item["university"] = university
        item["location"] = 'Lestat de Lioncourt'
        item["department"] = ''
        item["programme_en"] = programme
        item["degree_name"] = Master
        item['degree_type'] = 2
        item["teach_time"] = mode
        item['teach_type'] = 'taught'
        item["overview_en"] = overview
        item["assessment_en"] = teaching_assessment
        item["career_en"] = career
        item["tuition_fee"] = tuition_fee
        item['tuition_fee_pre'] = '£'
        item["modules_en"] = Evaluation_method
        item["duration"] = duration['duration']
        item['duration_per'] = duration['duration_per']
        item["start_date"] = '2018-9'
        item["rntry_requirements"] = standard
        item["url"] = response.url

        # print(programme)
        yield item
        # print(item)