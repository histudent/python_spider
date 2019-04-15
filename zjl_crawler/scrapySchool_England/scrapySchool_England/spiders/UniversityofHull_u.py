# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/6 15:19'
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
import  requests
from lxml import  etree
class UniversityofHullSpider(scrapy.Spider):
    name = 'UniversityofHull_u'
    allowed_domains = ['hull.ac.uk/']
    start_urls = []
    C = [
        'https://www.hull.ac.uk/study/ug/2018/biology-teacher-training.aspx',
        'https://www.hull.ac.uk/study/ug/2018/accounting-financial-mgmt.aspx',
        'https://www.hull.ac.uk/study/ug/2018/accounting.aspx',
        'https://www.hull.ac.uk/study/ug/2018/american-studies.aspx',
        'https://www.hull.ac.uk/study/ug/2019/american-studies-language.aspx',
        'https://www.hull.ac.uk/study/ug/2018/biochemistry.aspx',
        'https://www.hull.ac.uk/study/ug/2019/drama-modern-language.aspx',
        'https://www.hull.ac.uk/study/ug/2018/biomedical-engineering.aspx',
        'https://www.hull.ac.uk/study/ug/2019/geography-teacher-training-ba.aspx',
        'https://www.hull.ac.uk/study/ug/2018/biology.aspx',
        'https://www.hull.ac.uk/study/ug/2019/creative-writing-english.aspx',
        'https://www.hull.ac.uk/study/ug/2018/biomedical-science.aspx',
        'https://www.hull.ac.uk/study/ug/2019/english-music.aspx',
        'https://www.hull.ac.uk/study/ug/2018/british-politics-legislative.aspx',
        'https://www.hull.ac.uk/study/ug/2019/english-modern-language.aspx',
        'https://www.hull.ac.uk/study/ug/2018/business-economics.aspx',
        'https://www.hull.ac.uk/study/ug/2019/game-ent-design-mod-lang.aspx',
        'https://www.hull.ac.uk/study/ug/2018/business-mgmt-accounting.aspx',
        'https://www.hull.ac.uk/study/ug/2019/history-american-studies.aspx',
        'https://www.hull.ac.uk/study/ug/2018/business-mgmt-hrm.aspx',
        'https://www.hull.ac.uk/study/ug/2019/modern-languages-film.aspx',
        'https://www.hull.ac.uk/study/ug/2018/business-mgmt-economics.aspx',
        'https://www.hull.ac.uk/study/ug/2019/history-modern-language.aspx',
        'https://www.hull.ac.uk/study/ug/2018/business-management.aspx',
        'https://www.hull.ac.uk/study/ug/2019/modern-languages-history.aspx',
        'https://www.hull.ac.uk/study/ug/2018/business-mgmt-ict.aspx',
        'https://www.hull.ac.uk/study/ug/2019/modern-languages-english.aspx',
        'https://www.hull.ac.uk/study/ug/2018/business-mgmt-entrepreneurship.aspx',
        'https://www.hull.ac.uk/study/ug/2019/modern-languages-music.aspx',
        'https://www.hull.ac.uk/study/ug/2018/business-mgmt-financial-mgmt.aspx',
        'https://www.hull.ac.uk/study/ug/2019/music-popular.aspx',
        'https://www.hull.ac.uk/study/ug/2018/business-mgmt-marketing.aspx',
        'https://www.hull.ac.uk/study/ug/2019/music-film-studies.aspx',
        'https://www.hull.ac.uk/study/ug/2018/business-mgmt-supply-chain.aspx',
        'https://www.hull.ac.uk/study/ug/2019/music.aspx',
        'https://www.hull.ac.uk/study/ug/2018/chemical-energy-meng.aspx',
        'https://www.hull.ac.uk/study/ug/2019/philosophy-religion.aspx',
        'https://www.hull.ac.uk/study/ug/2018/business-mgmt-sustainability.aspx',
        'https://www.hull.ac.uk/study/ug/2019/music-modern-language.aspx',
        'https://www.hull.ac.uk/study/ug/2018/chemical-engineering.aspx',
        'https://www.hull.ac.uk/study/ug/2019/philosophy-politics-economics.aspx',
        'https://www.hull.ac.uk/study/ug/2018/chemistry.aspx',
        'https://www.hull.ac.uk/study/ug/2019/digital-design-language.aspx',
        'https://www.hull.ac.uk/study/ug/2018/chemistry-forensic.aspx',
        'https://www.hull.ac.uk/study/ug/2019/politics.aspx',
        'https://www.hull.ac.uk/study/ug/2018/chinese-french.aspx',
        'https://www.hull.ac.uk/study/ug/2019/social-enterprise-creative-care.aspx',
        'https://www.hull.ac.uk/study/ug/2018/chinese-german.aspx',
        'https://www.hull.ac.uk/study/ug/2019/working-with-children.aspx',
        'https://www.hull.ac.uk/study/ug/2018/chinese-italian.aspx',
        'https://www.hull.ac.uk/study/ug/2019/mech-med-engineering.aspx',
        'https://www.hull.ac.uk/study/ug/2018/chinese-spanish.aspx',
        'https://www.hull.ac.uk/study/ug/2019/geography-teacher-training-bsc.aspx',
        'https://www.hull.ac.uk/study/ug/2018/chinese-studies.aspx',
        'https://www.hull.ac.uk/study/ug/2019/logistics-supply-chain.aspx',
        'https://www.hull.ac.uk/study/ug/2018/combined-languages.aspx',
        'https://www.hull.ac.uk/study/ug/2019/nursing-child.aspx',
        'https://www.hull.ac.uk/study/ug/2018/computer-science.aspx',
        'https://www.hull.ac.uk/study/ug/2019/physics-astrophysics.aspx',
        'https://www.hull.ac.uk/study/ug/2018/computer-science-games-dev.aspx',
        'https://www.hull.ac.uk/study/ug/2019/physics.aspx',
        'https://www.hull.ac.uk/study/ug/2018/computer-science-software-eng.aspx',
        'https://www.hull.ac.uk/study/ug/2019/zoology.aspx',
        'https://www.hull.ac.uk/study/ug/2018/computer-science-teacher-training.aspx',
        'https://www.hull.ac.uk/study/ug/2019/international-law.aspx',
        'https://www.hull.ac.uk/study/ug/2018/computing.aspx',
        'https://www.hull.ac.uk/study/ug/2019/law-modern-language.aspx',
        'https://www.hull.ac.uk/study/ug/2018/creative-music-tech.aspx',
        'https://www.hull.ac.uk/study/ug/2018/creative-writing-film-studies.aspx',
        'https://www.hull.ac.uk/study/ug/2018/criminology.aspx',
        'https://www.hull.ac.uk/study/ug/2018/criminology-forensic-science.aspx',
        'https://www.hull.ac.uk/study/ug/2018/criminology-law.aspx',
        'https://www.hull.ac.uk/study/ug/2018/criminology-psychology.aspx',
        'https://www.hull.ac.uk/study/ug/2018/criminology-sociology.aspx',
        'https://www.hull.ac.uk/study/ug/2018/digital-design.aspx',
        'https://www.hull.ac.uk/study/ug/2018/drama.aspx',
        'https://www.hull.ac.uk/study/ug/2018/drama-english.aspx',
        'https://www.hull.ac.uk/study/ug/2018/drama-film-studies.aspx',
        'https://www.hull.ac.uk/study/ug/2018/early-childhood-studies.aspx',
        'https://www.hull.ac.uk/study/ug/2018/economics.aspx',
        'https://www.hull.ac.uk/study/ug/2018/education.aspx',
        'https://www.hull.ac.uk/study/ug/2018/education-special-needs.aspx',
        'https://www.hull.ac.uk/study/ug/2018/education-studies-tesol.aspx',
        'https://www.hull.ac.uk/study/ug/2018/electrical-electronic.aspx',
        'https://www.hull.ac.uk/study/ug/2018/electrical-energy-meng.aspx',
        'https://www.hull.ac.uk/study/ug/2018/electronic-engineering.aspx',
        'https://www.hull.ac.uk/study/ug/2018/engineering-manufacturing.aspx',
        'https://www.hull.ac.uk/study/ug/2018/english.aspx',
        'https://www.hull.ac.uk/study/ug/2018/english-american-lit-culture.aspx',
        'https://www.hull.ac.uk/study/ug/2018/english-film-studies.aspx',
        'https://www.hull.ac.uk/study/ug/2018/english-philosophy.aspx',
        'https://www.hull.ac.uk/study/ug/2018/environmental-science.aspx',
        'https://www.hull.ac.uk/study/ug/2018/film-studies.aspx',
        'https://www.hull.ac.uk/study/ug/2018/financial-mgmt.aspx',
        'https://www.hull.ac.uk/study/ug/2018/forensic-science.aspx',
        'https://www.hull.ac.uk/study/ug/2018/french.aspx',
        'https://www.hull.ac.uk/study/ug/2018/french-german.aspx',
        'https://www.hull.ac.uk/study/ug/2018/french-italian.aspx',
        'https://www.hull.ac.uk/study/ug/2018/french-spanish.aspx',
        'https://www.hull.ac.uk/study/ug/2018/game-entertainment-design.aspx',
        'https://www.hull.ac.uk/study/ug/2018/geography.aspx',
        'https://www.hull.ac.uk/study/ug/2018/geography-bsc.aspx',
        'https://www.hull.ac.uk/study/ug/2018/geology.aspx',
        'https://www.hull.ac.uk/study/ug/2018/geology-physical-geography.aspx',
        'https://www.hull.ac.uk/study/ug/2018/german.aspx',
        'https://www.hull.ac.uk/study/ug/2018/german-italian.aspx',
        'https://www.hull.ac.uk/study/ug/2018/german-spanish.aspx',
        'https://www.hull.ac.uk/study/ug/2018/history.aspx',
        'https://www.hull.ac.uk/study/ug/2018/history-politics.aspx',
        'https://www.hull.ac.uk/study/ug/2018/human-biology.aspx',
        'https://www.hull.ac.uk/study/ug/2018/human-geography.aspx',
        'https://www.hull.ac.uk/study/ug/2018/international-business.aspx',
        'https://www.hull.ac.uk/study/ug/2018/international-relations.aspx',
        'https://www.hull.ac.uk/study/ug/2018/history-archaeology.aspx',
        'https://www.hull.ac.uk/study/ug/2018/italian-spanish.aspx',
        'https://www.hull.ac.uk/study/ug/2018/italian-studies.aspx',
        'https://www.hull.ac.uk/study/ug/2018/language-linguistics-cultures.aspx',
        'https://www.hull.ac.uk/study/ug/2018/law-business-mgmt.aspx',
        'https://www.hull.ac.uk/study/ug/2018/law-criminology.aspx',
        'https://www.hull.ac.uk/study/ug/2018/law-legislative.aspx',
        'https://www.hull.ac.uk/study/ug/2018/law-llb.aspx',
        'https://www.hull.ac.uk/study/ug/2018/law-politics.aspx',
        'https://www.hull.ac.uk/study/ug/2018/marine-biology.aspx',
        'https://www.hull.ac.uk/study/ug/2018/marketing.aspx',
        'https://www.hull.ac.uk/study/ug/2018/marketing-management.aspx',
        'https://www.hull.ac.uk/study/ug/2018/mathematics.aspx',
        'https://www.hull.ac.uk/study/ug/2018/mechanical-energy-meng.aspx',
        'https://www.hull.ac.uk/study/ug/2018/mechanical-engineering.aspx',
        'https://www.hull.ac.uk/study/ug/2018/mechatronics-robotics.aspx',
        'https://www.hull.ac.uk/study/ug/2018/media-studies.aspx',
        'https://www.hull.ac.uk/study/ug/2018/midwifery-bsc.aspx',
        'https://www.hull.ac.uk/study/ug/2018/modern-languages-bus-mgmt.aspx',
        'https://www.hull.ac.uk/study/ug/2018/modern-languages-drama.aspx',
        'https://www.hull.ac.uk/study/ug/2018/modern-languages-marketing.aspx',
        'https://www.hull.ac.uk/study/ug/2018/modern-languages-translation-one.aspx',
        'https://www.hull.ac.uk/study/ug/2018/modern-languages-translation-two.aspx',
        'https://www.hull.ac.uk/study/ug/2018/music-bmus.aspx',
        'https://www.hull.ac.uk/study/ug/2018/music-theatre.aspx',
        'https://www.hull.ac.uk/study/ug/2018/nursing-adult.aspx',
        'https://www.hull.ac.uk/study/ug/2018/nursing-learning.aspx',
        'https://www.hull.ac.uk/study/ug/2018/nursing-mental-health.aspx',
        'https://www.hull.ac.uk/study/ug/2018/nursing-studies.aspx',
        'https://www.hull.ac.uk/study/ug/2018/operating-dept-practice.aspx',
        'https://www.hull.ac.uk/study/ug/2018/paramedic-science.aspx',
        'https://www.hull.ac.uk/study/ug/2018/philosophy.aspx',
        'https://www.hull.ac.uk/study/ug/2018/philosophy-politics.aspx',
        'https://www.hull.ac.uk/study/ug/2018/physical-geography.aspx',
        'https://www.hull.ac.uk/study/ug/2018/physics-qts.aspx',
        'https://www.hull.ac.uk/study/ug/2018/primary-teaching.aspx',
        'https://www.hull.ac.uk/study/ug/2018/psychology.aspx',
        'https://www.hull.ac.uk/study/ug/2018/psychology-criminology.aspx',
        'https://www.hull.ac.uk/study/ug/2018/social-work.aspx',
        'https://www.hull.ac.uk/study/ug/2018/sociology.aspx',
        'https://www.hull.ac.uk/study/ug/2018/spanish-studies.aspx',
        'https://www.hull.ac.uk/study/ug/2018/sport-exercise-nutrition.aspx',
        'https://www.hull.ac.uk/study/ug/2018/sport-exercise-science.aspx',
        'https://www.hull.ac.uk/study/ug/2018/sport-rehabilitation.aspx',
        'https://www.hull.ac.uk/study/ug/2018/sports-coaching-performance.aspx',
        'https://www.hull.ac.uk/study/ug/2018/theoretical-physics.aspx',
        'https://www.hull.ac.uk/study/ug/2018/war-security-studies.aspx',
        'https://www.hull.ac.uk/study/ug/2018/youth-work-community-dev.aspx'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Hull'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="main-content"]/header/div[2]/div[1]/h1|//*[@id="main-content"]/section[1]/div[2]/div/div/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en,url)

        #4.degree_type
        degree_type = 1

        #5.degree_name
        degree_name = response.xpath('//*[@id="main-content"]/header/div[2]/div[1]/p[2]/span[2]').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name,url)

        #6.start_date
        start_date = '2019-9'

        #7.ucascode
        ucascode = response.xpath('//*[@id="main-content"]/header/div[2]/div[2]/div/div[3]/span').extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode).strip()
        ucascode = clear_space_str(ucascode)
        # print(ucascode,url)

        #8.apply_desc_en
        apply_desc_en = response.xpath('//*[@id="entry"]/div/div[1]').extract()
        apply_desc_en = ''.join(apply_desc_en)
        apply_desc_en = remove_class(apply_desc_en)
        # print(apply_desc_en)


        #9.overview_en
        overview_en = response.xpath('//*[@id="about"]/div/div[1]/p').extract()
        overview_en =''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #10.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'Fees and funding')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee =getTuition_fee(tuition_fee)
        # print(tuition_fee)
        #
        #11.tuition_fee_pre
        tuition_fee_pre = '£'

        #12.modules_en
        # modules_en = response.xpath("//*[contains(text(),'odules')]/../following-sibling::*//li//p").extract()
        # if len(modules_en)==0:
        #     modules_en = response.xpath('//*[@id="study"]//p/strong').extract()
        # modules_en = ''.join(modules_en)
        # modules_en = remove_class(modules_en)
        modules_en = response.xpath('//*[@id="study"]/div/div[1]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)

        # print(modules_en)

        #13.ib
        ib = response.xpath("//*[contains(text(),'Alternative qualifications')]/../following-sibling::*//li[1]").extract()
        ib = ''.join(ib)
        ib = remove_tags(ib)
        # print(ib)



        #14.career_en
        career_en = response.xpath("//*[contains(text(),'Future prospects')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #15.require_chinese_en
        require_chinese_en = 'https://www.hull.ac.uk/choose-hull/study-at-hull/international/country/china.aspx'

        #16.ielts 17181920
        ielts_list = response.xpath("//*[contains(text(),'International students')]//following-sibling::*").extract()
        ielts_list = ''.join(ielts_list)
        try:
            ielts= re.findall('\d\.\d',ielts_list)
        except:
            ielts = None
        if len(ielts) ==2:
            a = ielts[0]
            b = ielts[1]
            ielts = a
            ielts_l = b
            ielts_r = b
            ielts_s = b
            ielts_w = b
        else:
            ielts = 6.0
            ielts_l = 5.5
            ielts_r = 5.5
            ielts_s = 5.5
            ielts_w = 5.5
        # print(ielts,ielts_l,ielts_r,ielts_w,ielts_s)

        #21.duration
        # try:
        #     ab = response.xpath("//div[@class='kis-widget']//@data-institution").extract()[0]
        # except:
        #     ab = ''
        # try:
        #     cd = response.xpath("//div[@class='kis-widget']//@data-course").extract()[0]
        # except:
        #     cd = ''
        # if len(ab)!= 0:
        #     duration_url = 'https://widget.unistats.ac.uk/Widget/'+str(ab)+'/'+str(cd)+'/small/en-GB/Full Time'
        # else:duration_url= ''
        # # print(duration_url)
        # if len(duration_url)!=0:
        #     headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        #     data = requests.get(duration_url, headers=headers)
        #     response_duration = etree.HTML(data.text)
        #     duration = response_duration.xpath('//*[@id="kisWidget"]/div[2]/p[1]//text()')
        #     duration = ''.join(duration)
        #     duration =remove_tags(duration)
        #     try:
        #         duration = re.findall(r'\d',duration)[0]
        #     except:
        #         duration = ''
        # else:
        #     duration = ''
        # print(duration)

        #23.apply_pre
        apply_pre = '£'

        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['start_date'] = start_date
        item['overview_en'] = overview_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['modules_en'] = modules_en
        item['ib'] = ib
        item['career_en'] = career_en
        item['require_chinese_en'] = require_chinese_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        # item['duration'] = duration
        item['apply_desc_en'] = apply_desc_en
        item['ucascode'] = ucascode
        yield  item