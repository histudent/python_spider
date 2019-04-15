# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/10 9:16'
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
class RoyalAgriculturalUniversitySpider(scrapy.Spider):
    name = 'RoyalAgriculturalUniversity_p'
    allowed_domains = ['rau.ac.uk/']
    start_urls = []
    C= [
        'https://www.rau.ac.uk/study/postgraduate/courses/graduate-certificate-agriculture',
        'https://www.rau.ac.uk/study/postgraduate/courses/graduate-diploma-agriculture',
        'https://www.rau.ac.uk/study/postgraduate/courses/mba-advanced-farm-management',
        'https://www.rau.ac.uk/study/postgraduate/courses/mba-international-food-and-agribusiness',
        'https://www.rau.ac.uk/study/postgraduate/courses/msc-agricultural-technology-and-innovation',
        'https://www.rau.ac.uk/study/postgraduate/courses/msc-business-management',
        'https://www.rau.ac.uk/study/postgraduate/courses/msc-research-programme',
        'https://www.rau.ac.uk/study/postgraduate/courses/msc-food-safety-and-quality-management',
        'https://www.rau.ac.uk/study/postgraduate/courses/msc-real-estate',
        'https://www.rau.ac.uk/study/postgraduate/courses/msc-rural-estate-management',
        'https://www.rau.ac.uk/study/postgraduate/courses/msc-sustainable-agriculture-and-food-security',
        'https://www.rau.ac.uk/study/postgraduate/courses/phd-programme'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Royal Agricultural University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="site"]//div[1]/div//h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        degree_name = programme_en.split()[0]
        programme_en = programme_en.replace(degree_name,'').strip()
        # print(degree_name)

        #6.overview_en
        overview_en = response.xpath('//*[@id="course-overview"]/div[1]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #7.teach_time
        teach_time = response.xpath("//*[contains(text(),'Mode of study')]//following-sibling::*").extract()
        teach_time = ''.join(teach_time)
        teach_time = remove_tags(teach_time)
        if 'Full time' in teach_time:
            teach_time = 'Full time'
        else:
            teach_time = 'Part time'
        # print(teach_time)

        #8.modules_en
        modules_en = response.xpath("//*[contains(text(),'Modules')]//following-sibling::ul/li").extract()
        modules_en = '\n'.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #9.rntry_requirements
        rntry_requirements = response.xpath("//*[contains(text(),'Entry requirements')]//following-sibling::*").extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #10.tuition_fee
        tuition_fee = response.xpath('//*[@id="course-fees"]/div[1]/table[1]/tbody/tr[1]/td[3]').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        if tuition_fee==0:
            tuition_fee = 5250
        else:pass
        # print(tuition_fee)

        #11.tuition_fee_pre
        tuition_fee_pre = '£'

        #12.career_en
        career_en = response.xpath("//*[contains(text(),'Prospects')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en).strip()
        # print(career_en)

        #13.apply_proces_en
        apply_proces_en = response.xpath("//*[contains(text(),'Apply now')]//following-sibling::div[1]").extract()
        apply_proces_en = ''.join(apply_proces_en)
        apply_proces_en = remove_class(apply_proces_en).strip()
        # print(apply_proces_en)

        #14.start_date
        start_date = '2018-9-1'

        #15.assessment_en
        assessment_en = '<p>During your undergraduate degree, you probably became familiar with many of the methods of delivery and study that we expect you to continue with during your postgraduate course. It is expected that you come already equipped with the basics in academic study, such as the ability to find, evaluate, manage, present and critique research or industry relevant output. There is a greater emphasis on independence and individual contribution towards the topics covered, and so the expectation is that students will actively participate in class-based activities from the outset. Giving presentations, critiquing case studies, using peer-to-peer feedback, working in groups on topical problems and justifying opinions based on the evidence is the norm for postgraduate study. It is not uncommon for students to arrive at a particular postgraduate qualification with very diverse backgrounds, qualifications and experience and we welcome these different perspectives in the classroom to bring a debate alive, however, it does require the student to take responsibility for their own subject knowledge gaps and motivate themselves to fill them. Of course, there will be support and guidance provided for good sources of information, however, it is not expected that these gaps will be specifically addressed within the taught sessions.For most postgraduate programmes group sizes are in the range of between 20 – 100 depending on the course and electives chosen (if relevant). However, alongside the lectures are small group seminars and tutorials where you will have the opportunity to explore key concepts in more detail, discuss topical issues relating to the key themes and undertake practical activities that help set the theories in context. To compliment the lectures and seminars, there may also be practical sessions, laboratory classes, off-site visits, case studies, guest speakers and field trips that are included in your timetabled activities depending on the modules you are studying.</p>'

        #16.deadline
        deadline = '2018-11,2019-5'

        #17.require_chinese_en
        require_chinese_en = '<p>Successful completion of a bachelor degree with a minimum of 60%.</p>'

        #18.ielts 19202122
        ielts = 6.5
        ielts_s=5.5
        ielts_w=5.5
        ielts_l=5.5
        ielts_r=5.5

        #19.apply_pre
        apply_pre = '£'

        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['teach_time'] = teach_time
        item['modules_en'] = modules_en
        item['rntry_requirements'] = rntry_requirements
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['career_en'] = career_en
        item['apply_proces_en'] = apply_proces_en
        item['start_date'] = start_date
        item['assessment_en'] = assessment_en
        item['deadline'] = deadline
        item['require_chinese_en'] = require_chinese_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        yield item
