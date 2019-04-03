# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime


class CardiffMetropolitanUniversity_USpider(scrapy.Spider):
    name = "CardiffMetropolitanUniversity_U"
    start_urls = ["http://www.cardiffmet.ac.uk/study/Pages/Undergraduate-Courses-A-Z.aspx"]

    def parse(self, response):
        links = ["http://www.cardiffmet.ac.uk/education/courses/Pages/BA-Drama-Joint-Honours.aspx",
"http://www.cardiffmet.ac.uk/artanddesign/courses/Pages/babscproductdesign.aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/BA-TESOL-Joint-Honours.aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/BA-Creative-Writing-Joint-Honours.aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/BA-Drama-Joint-Honours.aspx",
"http://www.cardiffmet.ac.uk/technologies/courses/Pages/bsc-data-science.aspx",
"http://www.cardiffmet.ac.uk/health/courses/Pages/Biomedical-Science-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/health/courses/Pages/Psychology-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/management/courses/Pages/International-Business-Management-BA-(Hons).aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/primary-education-studies-and-english-language-teaching.aspx",
"http://www.cardiffmet.ac.uk/management/courses/Pages/Events-Management-BA-(Hons).aspx",
"http://www.cardiffmet.ac.uk/management/courses/Pages/Economics-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/management/courses/Pages/Business-Economics-BA-(Hons).aspx",
"http://www.cardiffmet.ac.uk/technologies/courses/Pages/bsc-computing-with-creative-design.aspx",
"http://www.cardiffmet.ac.uk/technologies/courses/Pages/Software-Engineering-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/BA-(Hons)-Education-Psychology-and-Special-Educational-Needs-.aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/Social-Work-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/health/courses/Pages/Public-Health-Nutrition-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/management/courses/Pages/Accounting-and-Finance-BA-(Hons).aspx",
"http://www.cardiffmet.ac.uk/artanddesign/courses/Pages/ba-photographic-practice-bridgend.aspx",
"http://www.cardiffmet.ac.uk/management/courses/Pages/International-Tourism-Management-BA-(Hons).aspx",
"http://www.cardiffmet.ac.uk/artanddesign/courses/Pages/BAArtistDesignerMaker.aspx",
"http://www.cardiffmet.ac.uk/artanddesign/courses/Pages/ba-interior-design.aspx",
"http://www.cardiffmet.ac.uk/management/courses/Pages/International-Economics-and-Finance-BSc-BScEcon-(Hons).aspx",
"http://www.cardiffmet.ac.uk/health/courses/Pages/Environmental-Health-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/schoolofsport/courses/Pages/Sport-Conditioning,-Rehabilitation-and-Massage-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/schoolofsport/courses/Pages/Sport-and-Physical-Education-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/management/courses/Pages/Digital-Marketing-BA-(Hons)-Degree.aspx",
"http://www.cardiffmet.ac.uk/technologies/courses/Pages/Business-Information-Systems-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/health/courses/Pages/Food-Science-and-Technology-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/health/courses/Pages/public-health-bsc-(hons).aspx",
"http://www.cardiffmet.ac.uk/artanddesign/courses/Pages/babscproductdesign.aspx",
"http://www.cardiffmet.ac.uk/management/courses/Pages/Marketing-Management-BA-(Hons).aspx",
"http://www.cardiffmet.ac.uk/management/courses/Pages/International-Hospitality-Management-BA-(Hons).aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/BA-(Hons)-Primary-Education-Studies.aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/BA-Creative-Writing-Joint-Honours.aspx",
"http://www.cardiffmet.ac.uk/artanddesign/courses/Pages/ba-fashion-design.aspx",
"http://www.cardiffmet.ac.uk/management/courses/Pages/fashion-marketing-management-ba-(hons).aspx",
"http://www.cardiffmet.ac.uk/schoolofsport/courses/Pages/Sport-Coaching-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/BA-Drama-Joint-Honours.aspx",
"http://www.cardiffmet.ac.uk/schoolofsport/courses/Pages/Sport-Development-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/technologies/courses/Pages/bsc-computing-for-interaction-degree.aspx",
"http://www.cardiffmet.ac.uk/technologies/courses/Pages/bsc-computer-security-degree.aspx",
"http://www.cardiffmet.ac.uk/health/courses/Pages/Human-Nutrition-and-Dietetics-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/BA-TESOL-Joint-Honours.aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/BA-English-Joint-Honours.aspx",
"http://www.cardiffmet.ac.uk/schoolofsport/courses/Pages/Sport%20and%20Physical%20Education%20Studies%20(bilingual)%20-%20BSc%20(Hons).aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/BA-Early-Childhood-Studies-(Single-Honours).aspx",
"http://www.cardiffmet.ac.uk/management/courses/Pages/Banking-and-Finance-BSc-(Hons)-Degree.aspx",
"http://www.cardiffmet.ac.uk/technologies/courses/Pages/Computer-Games-Design-and-Development-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/schoolofsport/courses/Pages/Sport-Management-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/management/courses/Pages/Accounting-BA-(Hons).aspx",
"http://www.cardiffmet.ac.uk/artanddesign/courses/Pages/bafineart.aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/Youth-Community-Work-BA-(Hons).aspx",
"http://www.cardiffmet.ac.uk/health/courses/Pages/Healthcare-Science-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/artanddesign/courses/Pages/BA-Animation.aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/Health-and-Social-Care-HND-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/housing-studies-bsc.aspx",
"http://www.cardiffmet.ac.uk/schoolofsport/courses/Pages/Sport-Performance-Analysis-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/health/courses/Pages/Dental-Technology-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/schoolofsport/courses/Pages/dance-and-physical-education.aspx",
"http://www.cardiffmet.ac.uk/health/courses/Pages/Podiatry-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/artanddesign/courses/Pages/hndbscadt.aspx",
"http://www.cardiffmet.ac.uk/schoolofsport/courses/Pages/Sport-and-Exercise-Science-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/artanddesign/courses/Pages/baillustration.aspx",
"http://www.cardiffmet.ac.uk/health/courses/Pages/Biomedical-Sciences-Health-Exercise-Nutrition-BSc-Hons.aspx",
"http://www.cardiffmet.ac.uk/management/courses/Pages/Business-and-Management-Studies-(with-specialist-pathways)-BA-(Hons).aspx",
"http://www.cardiffmet.ac.uk/artanddesign/courses/Pages/baceramics.aspx",
"http://www.cardiffmet.ac.uk/health/courses/Pages/Complementary-Healthcare-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/health/courses/Pages/Speech-and-Language-Therapy-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/artanddesign/courses/Pages/bagraphics.aspx",
"http://www.cardiffmet.ac.uk/schoolofsport/courses/Pages/Sport-Studies-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/BA-Media-Joint-Honours.aspx",
"http://www.cardiffmet.ac.uk/artanddesign/courses/Pages/batextiles.aspx",
"http://www.cardiffmet.ac.uk/technologies/courses/Pages/Computer-Science-BSc-(Hons).aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/BA-TESOL-Joint-Honours.aspx",
"http://www.cardiffmet.ac.uk/education/courses/Pages/BA-Creative-Writing-Joint-Honours.aspx", ]
        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "Cardiff Metropolitan University"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:
            item['alevel'] = None
            # alevel = response.xpath(
            #     "//*[contains(text(),'A levels')]//text()|"
            #     "//*[contains(text(),'A Levels')]//text()").extract()
            alevel = response.xpath(
                "//h3[contains(text(), 'Entry Requirement')]/following-sibling::div[1]//*[contains(text(),'Degree')]/../following-sibling::p[1]//text()|"
                "//h3[contains(text(), 'Entry Requirement')]/following-sibling::div[1]//*[contains(text(),'Degree')]/..//following-sibling::ul[1]/li[1]//text()").extract()
            if len(alevel) == 0:
                alevel = response.xpath(
                    "//h3[contains(text(), 'Entry Requirement')]/following-sibling::div[1]/p[1]//text()|"
                    "//h3[contains(text(), 'Entry Requirement')]/following-sibling::div[1]//ul[1]/li[1]//text()").extract()
            item['alevel'] = clear_lianxu_space(alevel)
            print("item['alevel']: ", item['alevel'])

            # ib = response.xpath(
            #     "//strong[contains(text(),'International Baccalaureate:')]/../text()").extract()
            # item['ib'] = clear_lianxu_space(ib)
            # print("item['ib']: ", item['ib'])


            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

