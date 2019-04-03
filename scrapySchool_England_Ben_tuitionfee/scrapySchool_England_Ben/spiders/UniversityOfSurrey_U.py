import scrapy
import re
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space, clear_space_str
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.getIELTS import get_ielts
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime
import requests
from lxml import etree

class UniversityOfSurrey_USpider(scrapy.Spider):
    name = "UniversityOfSurrey_U"
    start_urls = ["https://www.surrey.ac.uk/undergraduate"]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3472.3 Safari/537.36"}

    def parse(self, response):
        links = ["https://www.surrey.ac.uk/undergraduate/accounting-and-finance",
"https://www.surrey.ac.uk/undergraduate/accounting-and-finance",
"https://www.surrey.ac.uk/undergraduate/acting",
"https://www.surrey.ac.uk/undergraduate/actor-musician",
"https://www.surrey.ac.uk/undergraduate/aerospace-engineering",
"https://www.surrey.ac.uk/undergraduate/aerospace-engineering",
"https://www.surrey.ac.uk/undergraduate/aerospace-engineering",
"https://www.surrey.ac.uk/undergraduate/aerospace-engineering",
"https://www.surrey.ac.uk/undergraduate/automotive-engineering",
"https://www.surrey.ac.uk/undergraduate/automotive-engineering",
"https://www.surrey.ac.uk/undergraduate/automotive-engineering",
"https://www.surrey.ac.uk/undergraduate/automotive-engineering",
"https://www.surrey.ac.uk/undergraduate/biochemistry",
"https://www.surrey.ac.uk/undergraduate/biochemistry",
"https://www.surrey.ac.uk/undergraduate/biological-sciences",
"https://www.surrey.ac.uk/undergraduate/biological-sciences",
"https://www.surrey.ac.uk/undergraduate/biomedical-engineering",
"https://www.surrey.ac.uk/undergraduate/biomedical-engineering",
"https://www.surrey.ac.uk/undergraduate/biomedical-engineering",
"https://www.surrey.ac.uk/undergraduate/biomedical-engineering",
"https://www.surrey.ac.uk/undergraduate/biomedical-science",
"https://www.surrey.ac.uk/undergraduate/biomedical-science",
"https://www.surrey.ac.uk/undergraduate/business-and-retail-management",
"https://www.surrey.ac.uk/undergraduate/business-and-retail-management",
"https://www.surrey.ac.uk/undergraduate/business-economics",
"https://www.surrey.ac.uk/undergraduate/business-economics",
"https://www.surrey.ac.uk/undergraduate/business-management",
"https://www.surrey.ac.uk/undergraduate/business-management",
"https://www.surrey.ac.uk/undergraduate/business-management-entrepreneurship",
"https://www.surrey.ac.uk/undergraduate/business-management-entrepreneurship",
"https://www.surrey.ac.uk/undergraduate/business-management-hrm",
"https://www.surrey.ac.uk/undergraduate/business-management-hrm",
"https://www.surrey.ac.uk/undergraduate/business-management-marketing",
"https://www.surrey.ac.uk/undergraduate/business-management-marketing",
"https://www.surrey.ac.uk/undergraduate/business-management-and-french",
"https://www.surrey.ac.uk/undergraduate/business-management-and-german",
"https://www.surrey.ac.uk/undergraduate/business-management-and-spanish",
"https://www.surrey.ac.uk/undergraduate/chemical-and-petroleum-engineering",
"https://www.surrey.ac.uk/undergraduate/chemical-and-petroleum-engineering",
"https://www.surrey.ac.uk/undergraduate/chemical-and-petroleum-engineering",
"https://www.surrey.ac.uk/undergraduate/chemical-and-petroleum-engineering",
"https://www.surrey.ac.uk/undergraduate/chemical-engineering",
"https://www.surrey.ac.uk/undergraduate/chemical-engineering",
"https://www.surrey.ac.uk/undergraduate/chemical-engineering",
"https://www.surrey.ac.uk/undergraduate/chemical-engineering",
"https://www.surrey.ac.uk/undergraduate/chemistry",
"https://www.surrey.ac.uk/undergraduate/chemistry",
"https://www.surrey.ac.uk/undergraduate/chemistry",
"https://www.surrey.ac.uk/undergraduate/chemistry-forensic-investigation",
"https://www.surrey.ac.uk/undergraduate/chemistry-forensic-investigation",
"https://www.surrey.ac.uk/undergraduate/chemistry-forensic-investigation",
"https://www.surrey.ac.uk/undergraduate/civil-engineering",
"https://www.surrey.ac.uk/undergraduate/civil-engineering",
"https://www.surrey.ac.uk/undergraduate/civil-engineering",
"https://www.surrey.ac.uk/undergraduate/civil-engineering",
"https://www.surrey.ac.uk/undergraduate/computer-and-internet-engineering",
"https://www.surrey.ac.uk/undergraduate/computer-and-internet-engineering",
"https://www.surrey.ac.uk/undergraduate/computer-and-internet-engineering",
"https://www.surrey.ac.uk/undergraduate/computer-and-internet-engineering",
"https://www.surrey.ac.uk/undergraduate/computer-science",
"https://www.surrey.ac.uk/undergraduate/computer-science",
"https://www.surrey.ac.uk/undergraduate/computing-and-information-technology",
"https://www.surrey.ac.uk/undergraduate/computing-and-information-technology",
"https://www.surrey.ac.uk/undergraduate/creative-music-technology",
"https://www.surrey.ac.uk/undergraduate/criminology",
"https://www.surrey.ac.uk/undergraduate/criminology",
"https://www.surrey.ac.uk/undergraduate/criminology-and-sociology",
"https://www.surrey.ac.uk/undergraduate/criminology-and-sociology",
"https://www.surrey.ac.uk/undergraduate/dance",
"https://www.surrey.ac.uk/undergraduate/dance",
"https://www.surrey.ac.uk/undergraduate/digital-media-arts",
"https://www.surrey.ac.uk/undergraduate/digital-media-arts",
"https://www.surrey.ac.uk/undergraduate/economics",
"https://www.surrey.ac.uk/undergraduate/economics",
"https://www.surrey.ac.uk/undergraduate/economics-and-finance",
"https://www.surrey.ac.uk/undergraduate/economics-and-finance",
"https://www.surrey.ac.uk/undergraduate/economics-and-mathematics",
"https://www.surrey.ac.uk/undergraduate/economics-and-mathematics",
"https://www.surrey.ac.uk/undergraduate/electrical-and-electronic-engineering",
"https://www.surrey.ac.uk/undergraduate/electrical-and-electronic-engineering",
"https://www.surrey.ac.uk/undergraduate/electrical-and-electronic-engineering",
"https://www.surrey.ac.uk/undergraduate/electrical-and-electronic-engineering",
"https://www.surrey.ac.uk/undergraduate/electronic-engineering",
"https://www.surrey.ac.uk/undergraduate/electronic-engineering",
"https://www.surrey.ac.uk/undergraduate/electronic-engineering",
"https://www.surrey.ac.uk/undergraduate/electronic-engineering",
"https://www.surrey.ac.uk/undergraduate/electronic-engineering-computer-systems",
"https://www.surrey.ac.uk/undergraduate/electronic-engineering-computer-systems",
"https://www.surrey.ac.uk/undergraduate/electronic-engineering-computer-systems",
"https://www.surrey.ac.uk/undergraduate/electronic-engineering-computer-systems",
"https://www.surrey.ac.uk/undergraduate/electronic-engineering-nanotechnology",
"https://www.surrey.ac.uk/undergraduate/electronic-engineering-nanotechnology",
"https://www.surrey.ac.uk/undergraduate/electronic-engineering-nanotechnology",
"https://www.surrey.ac.uk/undergraduate/electronic-engineering-nanotechnology",
"https://www.surrey.ac.uk/undergraduate/electronic-engineering-space-systems",
"https://www.surrey.ac.uk/undergraduate/electronic-engineering-space-systems",
"https://www.surrey.ac.uk/undergraduate/electronic-engineering-space-systems",
"https://www.surrey.ac.uk/undergraduate/electronic-engineering-space-systems",
"https://www.surrey.ac.uk/undergraduate/english-literature",
"https://www.surrey.ac.uk/undergraduate/english-literature",
"https://www.surrey.ac.uk/undergraduate/english-literature-and-french",
"https://www.surrey.ac.uk/undergraduate/english-literature-and-french",
"https://www.surrey.ac.uk/undergraduate/english-literature-and-german",
"https://www.surrey.ac.uk/undergraduate/english-literature-and-german",
"https://www.surrey.ac.uk/undergraduate/english-literature-and-spanish",
"https://www.surrey.ac.uk/undergraduate/english-literature-and-spanish",
"https://www.surrey.ac.uk/undergraduate/english-literature-creative-writing",
"https://www.surrey.ac.uk/undergraduate/english-literature-creative-writing",
"https://www.surrey.ac.uk/undergraduate/english-literature-film-studies",
"https://www.surrey.ac.uk/undergraduate/english-literature-film-studies",
"https://www.surrey.ac.uk/undergraduate/english-literature-politics",
"https://www.surrey.ac.uk/undergraduate/english-literature-politics",
"https://www.surrey.ac.uk/undergraduate/english-literature-sociology",
"https://www.surrey.ac.uk/undergraduate/english-literature-sociology",
"https://www.surrey.ac.uk/undergraduate/film-and-video-production-technology",
"https://www.surrey.ac.uk/undergraduate/film-and-video-production-technology",
"https://www.surrey.ac.uk/undergraduate/financial-mathematics",
"https://www.surrey.ac.uk/undergraduate/financial-mathematics",
"https://www.surrey.ac.uk/undergraduate/international-business-management",
"https://www.surrey.ac.uk/undergraduate/international-business-management",
"https://www.surrey.ac.uk/undergraduate/international-event-management",
"https://www.surrey.ac.uk/undergraduate/international-event-management",
"https://www.surrey.ac.uk/undergraduate/international-hospitality-and-tourism-management",
"https://www.surrey.ac.uk/undergraduate/international-hospitality-and-tourism-management",
"https://www.surrey.ac.uk/undergraduate/international-hospitality-management",
"https://www.surrey.ac.uk/undergraduate/international-hospitality-management",
"https://www.surrey.ac.uk/undergraduate/international-relations",
"https://www.surrey.ac.uk/undergraduate/international-relations",
"https://www.surrey.ac.uk/undergraduate/international-tourism-management",
"https://www.surrey.ac.uk/undergraduate/international-tourism-management",
"https://www.surrey.ac.uk/undergraduate/law",
"https://www.surrey.ac.uk/undergraduate/law",
"https://www.surrey.ac.uk/undergraduate/law-criminology",
"https://www.surrey.ac.uk/undergraduate/law-criminology",
"https://www.surrey.ac.uk/undergraduate/law-international-relations",
"https://www.surrey.ac.uk/undergraduate/law-international-relations",
"https://www.surrey.ac.uk/undergraduate/mathematics",
"https://www.surrey.ac.uk/undergraduate/mathematics",
"https://www.surrey.ac.uk/undergraduate/mathematics",
"https://www.surrey.ac.uk/undergraduate/mathematics",
"https://www.surrey.ac.uk/undergraduate/mathematics-and-physics",
"https://www.surrey.ac.uk/undergraduate/mathematics-and-physics",
"https://www.surrey.ac.uk/undergraduate/mathematics-and-physics",
"https://www.surrey.ac.uk/undergraduate/mathematics-and-physics",
"https://www.surrey.ac.uk/undergraduate/mathematics-and-physics",
"https://www.surrey.ac.uk/undergraduate/mathematics-and-physics",
"https://www.surrey.ac.uk/undergraduate/mathematics-music",
"https://www.surrey.ac.uk/undergraduate/mathematics-music",
"https://www.surrey.ac.uk/undergraduate/mathematics-statistics",
"https://www.surrey.ac.uk/undergraduate/mathematics-statistics",
"https://www.surrey.ac.uk/undergraduate/mechanical-engineering",
"https://www.surrey.ac.uk/undergraduate/mechanical-engineering",
"https://www.surrey.ac.uk/undergraduate/mechanical-engineering",
"https://www.surrey.ac.uk/undergraduate/mechanical-engineering",
"https://www.surrey.ac.uk/undergraduate/media-and-communication",
"https://www.surrey.ac.uk/undergraduate/media-and-communication",
"https://www.surrey.ac.uk/undergraduate/media-studies-film-studies",
"https://www.surrey.ac.uk/undergraduate/media-studies-film-studies",
"https://www.surrey.ac.uk/undergraduate/medicinal-chemistry",
"https://www.surrey.ac.uk/undergraduate/medicinal-chemistry",
"https://www.surrey.ac.uk/undergraduate/medicinal-chemistry",
"https://www.surrey.ac.uk/undergraduate/microbiology",
"https://www.surrey.ac.uk/undergraduate/microbiology",
"https://www.surrey.ac.uk/undergraduate/midwifery-registered-midwife",
"https://www.surrey.ac.uk/undergraduate/modern-languages-french-and-german",
"https://www.surrey.ac.uk/undergraduate/modern-languages-french-and-spanish",
"https://www.surrey.ac.uk/undergraduate/modern-languages-german-and-spanish",
"https://www.surrey.ac.uk/undergraduate/music",
"https://www.surrey.ac.uk/undergraduate/music",
"https://www.surrey.ac.uk/undergraduate/music-and-sound-recording-tonmeister",
"https://www.surrey.ac.uk/undergraduate/music-and-sound-recording-tonmeister",
"https://www.surrey.ac.uk/undergraduate/musical-theatre",
"https://www.surrey.ac.uk/undergraduate/nursing-studies-registered-nurse-adult-nursing",
"https://www.surrey.ac.uk/undergraduate/nursing-studies-registered-nurse-childrens-nursing",
"https://www.surrey.ac.uk/undergraduate/nursing-studies-registered-nurse-mental-health-nursing",
"https://www.surrey.ac.uk/undergraduate/nutrition",
"https://www.surrey.ac.uk/undergraduate/nutrition",
"https://www.surrey.ac.uk/undergraduate/nutrition-and-dietetics",
"https://www.surrey.ac.uk/undergraduate/nutrition-and-food-science",
"https://www.surrey.ac.uk/undergraduate/nutrition-and-food-science",
"https://www.surrey.ac.uk/undergraduate/paramedic-science",
"https://www.surrey.ac.uk/undergraduate/physics",
"https://www.surrey.ac.uk/undergraduate/physics",
"https://www.surrey.ac.uk/undergraduate/physics",
"https://www.surrey.ac.uk/undergraduate/physics-astronomy",
"https://www.surrey.ac.uk/undergraduate/physics-astronomy",
"https://www.surrey.ac.uk/undergraduate/physics-astronomy",
"https://www.surrey.ac.uk/undergraduate/physics-nuclear-astrophysics",
"https://www.surrey.ac.uk/undergraduate/physics-nuclear-astrophysics",
"https://www.surrey.ac.uk/undergraduate/physics-nuclear-astrophysics",
"https://www.surrey.ac.uk/undergraduate/physics-quantum-technologies",
"https://www.surrey.ac.uk/undergraduate/physics-quantum-technologies",
"https://www.surrey.ac.uk/undergraduate/physics-quantum-technologies",
"https://www.surrey.ac.uk/undergraduate/politics",
"https://www.surrey.ac.uk/undergraduate/politics",
"https://www.surrey.ac.uk/undergraduate/politics-and-economics",
"https://www.surrey.ac.uk/undergraduate/politics-and-economics",
"https://www.surrey.ac.uk/undergraduate/politics-and-sociology",
"https://www.surrey.ac.uk/undergraduate/politics-and-sociology",
"https://www.surrey.ac.uk/undergraduate/psychology",
"https://www.surrey.ac.uk/undergraduate/psychology",
"https://www.surrey.ac.uk/undergraduate/public-affairs",
"https://www.surrey.ac.uk/undergraduate/public-affairs",
"https://www.surrey.ac.uk/undergraduate/sociology",
"https://www.surrey.ac.uk/undergraduate/sociology",
"https://www.surrey.ac.uk/undergraduate/sport-and-exercise-science",
"https://www.surrey.ac.uk/undergraduate/sport-and-exercise-science",
"https://www.surrey.ac.uk/undergraduate/theatre-and-performance",
"https://www.surrey.ac.uk/undergraduate/theatre-and-performance",
"https://www.surrey.ac.uk/undergraduate/theatre-production",
"https://www.surrey.ac.uk/undergraduate/veterinary-biosciences",
"https://www.surrey.ac.uk/undergraduate/veterinary-biosciences",
"https://www.surrey.ac.uk/undergraduate/veterinary-medicine-and-science", ]
        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Surrey"
        item['url'] = response.meta['url']
        print("===============================")
        print(response.url)
        print(response.meta['url'])

        try:
            tuition_fee = response.xpath("//div[@id='fees']//tbody//tr[1]/td[last()-1]//text()").extract()
            # print("tuition_fee: ", tuition_fee)
            if len(tuition_fee) > 0:
                item['tuition_fee'] = getTuition_fee(''.join(tuition_fee))

            if item['tuition_fee'] == 0:
                item['tuition_fee'] = None
            else:
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee'] = ", item['tuition_fee'])
            print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])

            alevel = response.xpath("//h3[contains(text(),'A-level')]/..//text()").extract()
            # alevel_str = ''.join(alevel).strip()
            # if alevel_str == "Overall:" or alevel_str == "Overall":
            #     alevel = response.xpath("//h3[contains(text(),'A-level')]/following-sibling::*[position()<4]//text()").extract()
            #     alevel_str = ''.join(alevel).replace("Overall", "").strip().strip(":").strip()
                # print("***alevel")
            item['alevel'] = clear_lianxu_space(alevel)
            # print("item['alevel'] = ", item['alevel'])

            ib = response.xpath("//h3[contains(text(),'International Baccalaureate')]/..//text()").extract()
            # ib_str = ''.join(ib).strip()
            # if ib_str == "Overall:":
            #     ib = response.xpath("//h3[contains(text(),'International Baccalaureate')]/following-sibling::*[2]//text()").extract()
            #     ib_str = ''.join(ib).strip()
            #     # print("***ib")
            item['ib'] = clear_lianxu_space(ib)
            # print("item['ib'] = ", item['ib'])


            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)
