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
from w3lib.html import remove_tags


class EdinburghNapierUniversity_Alevel_IbSpider(scrapy.Spider):
    name = "EdinburghNapierUniversity_Alevel_Ib"
    start_urls = ["https://www.bolton.ac.uk/subject-areas/all-subjects/"]

    def parse(self, response):
        links = ["https://www.napier.ac.uk/courses/bsc-hons-physical-activity-and-health-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-sport-and-exercise-science-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bdes-hons-graphic-design-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-photography-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bdes-hons-product-design-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-communication-advertising--public-relations-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-languages-and-intercultural-communication-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-microbiology-and-biotechnology-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-animal-biology-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-acting-and-english-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-international-festival--event-management-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-sports-coaching-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/meng-civil-engineering-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bengbeng-hons-computing-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-creative-computing-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-social-sciences-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/beng-hons-cybersecurity-and-forensics-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bengbeng-hons-civil-engineering-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-international-festival--event-management-with-tourism-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-international-festival--event-management-with-language-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-business-management-with-entrepreneurship-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-marine-and-freshwater-biology-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-animal-and-conservation-biology-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-international-business-management-and-languages-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-international-hospitality-management-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-international-hospitality-management-and-festival--event-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-business-management-with-marketing-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-business-management-with-human-resource-management-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-biological-sciences-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-international-hospitality-management-with-language-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-biomedical-sciences-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-applied-microbiology-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-international-business-management-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-international-hospitality--service-management-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-business-studies-sandwich-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-accounting-with-corporate-finance-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-accounting-with-law-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-accounting-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/meng-civil--transportation-engineering-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-psychology-with-sociology-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-financial-services-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bn-nursing-adult-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bengbeng-hons-engineering-with-management-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons--bsc-hons-psychology-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bengbeng-hons-mechatronics-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bscbsc-hons-construction-and-project-management-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bn-nursing-learning-disabilities-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-international-hospitality-management-city-of-glasgow-college-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-international-tourism-management-with-language-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/llb--llb-hons-law-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-criminology-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-international-tourism-management-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bdes-hons-interior--spatial-design-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-information-technology-management-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/meng-mechanical-engineering-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-policing-and-criminology-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-business-information-technology-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-english-and-film-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-music-popular-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/beng-hons-computer-systems-and-networks-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-english-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bmus-hons-music-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-business-management-west-lothian-college-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bscbsc-hons-computing-science-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bm-midwifery-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/baba-hons-accounting-and-finance-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-television-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-journalism-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bengbeng-hons-software-engineering-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-international-tourism-and-airline-management-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-web-design-and-development-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/meng-software-engineering-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bscbsc-hons-games-development-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bengbeng-hons-electronic--electrical-engineering-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bn-nursing-mental-health-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/meng-electronic--electrical-engineering-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-digital-media-and-interaction-design-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bengbeng-hons-energy-and-environmental-engineering-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-film-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bscbsc-hons-architectural-technology-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bn-nursing-child-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bscbsc-hons-real-estate-surveying-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-sound-design-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-acting-for-stage-and-screen-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-marketing-with-digital-media-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-digital-media-and-interaction-design-global-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/ba-hons-marketing-management-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-hons-veterinary-nursing-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bengbeng-hons-mechanical-engineering-undergraduate-fulltime",
"https://www.napier.ac.uk/courses/bsc-nursing-studies--option-rich-programme-undergraduate-fulltime", ]
        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})


    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "Edinburgh Napier University"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:
            alevel = response.xpath(
                "//div[@id='tab1']//h3[contains(text(),'A Level')]/following-sibling::*").extract()
            print(alevel)
            if len(alevel) > 0:
                for i in range(len(alevel)):
                    if "<h3>" in alevel[i]:
                        item['alevel'] = remove_tags(clear_lianxu_space(alevel[:i]))
                        break
                if item['alevel'] == "":
                    item['alevel'] = remove_tags(clear_lianxu_space(alevel))
            # item['alevel'] = clear_lianxu_space(alevel)
            print("item['alevel']: ", item['alevel'])

            ib = response.xpath(
                "//div[@id='tab1']//h3[contains(text(),'International Baccalaureate')]/following-sibling::*").extract()
            print("ib: ", ib)
            if len(ib) > 0:
                for i in range(len(ib)):
                    if "<h3>" in ib[i]:
                        item['ib'] = remove_tags(clear_lianxu_space(ib[:i]))
                        break
                if item['ib'] == "":
                    item['ib'] = remove_tags(clear_lianxu_space(ib))
            # item['ib'] = clear_lianxu_space(ib)
            print("item['ib']: ", item['ib'])

            yield item

        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

