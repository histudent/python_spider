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

class UniversityOfCambridge_USpider(scrapy.Spider):
    name = "UniversityOfCambridge_U"
    start_urls = ["https://www.undergraduate.study.cam.ac.uk/courses"]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3472.3 Safari/537.36"}

    def parse(self, response):
        links = ["https://www.undergraduate.study.cam.ac.uk/courses/chemical-engineering",
"https://www.undergraduate.study.cam.ac.uk/courses/classics",
"https://www.undergraduate.study.cam.ac.uk/courses/computer-science",
"https://www.undergraduate.study.cam.ac.uk/courses/architecture",
"https://www.undergraduate.study.cam.ac.uk/courses/human-social-and-political-sciences",
"https://www.undergraduate.study.cam.ac.uk/courses/history-and-politics",
"https://www.undergraduate.study.cam.ac.uk/courses/natural-sciences",
"https://www.undergraduate.study.cam.ac.uk/courses/law",
"https://www.undergraduate.study.cam.ac.uk/courses/archaeology",
"https://www.undergraduate.study.cam.ac.uk/courses/economics",
"https://www.undergraduate.study.cam.ac.uk/courses/asian-and-middle-eastern-studies",
"https://www.undergraduate.study.cam.ac.uk/courses/linguistics",
"https://www.undergraduate.study.cam.ac.uk/courses/history-of-art",
"https://www.undergraduate.study.cam.ac.uk/courses/education",
"https://www.undergraduate.study.cam.ac.uk/courses/history",
"https://www.undergraduate.study.cam.ac.uk/courses/land-economy",
"https://www.undergraduate.study.cam.ac.uk/courses/medicine",
"https://www.undergraduate.study.cam.ac.uk/courses/anglo-saxon-norse-and-celtic",
"https://www.undergraduate.study.cam.ac.uk/courses/theology",
"https://www.undergraduate.study.cam.ac.uk/courses/veterinary-medicine",
"https://www.undergraduate.study.cam.ac.uk/courses/chemical-engineering",
"https://www.undergraduate.study.cam.ac.uk/courses/english",
"https://www.undergraduate.study.cam.ac.uk/courses/mathematics",
"https://www.undergraduate.study.cam.ac.uk/courses/music",
"https://www.undergraduate.study.cam.ac.uk/courses/philosophy",
"https://www.undergraduate.study.cam.ac.uk/courses/classics",
"https://www.undergraduate.study.cam.ac.uk/courses/history-and-modern-languages",
"https://www.undergraduate.study.cam.ac.uk/courses/geography",
"https://www.undergraduate.study.cam.ac.uk/courses/engineering",
"https://www.undergraduate.study.cam.ac.uk/courses/psychological-and-behavioural-sciences",
"https://www.undergraduate.study.cam.ac.uk/courses/modern-and-medieval-languages", ]
        print(len(links))
        links = list(set(links))
        print(len(links))

        for link in links:
            url = link
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Cambridge"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:
            programme = response.xpath("//h1[@class='campl-sub-title']//text()").extract()
            clear_space(programme)
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en'] = ", item['programme_en'])

            tuition_fee_dict_old = {"Anglo-Saxon, Norse, and Celtic": 20157,
"Archaeology": 20157,
"Asian and Middle Eastern Studies": 20157,
"Classics": 20157,
"Economics": 20157,
"Education": 20157,
"English": 20157,
"History": 20157,
"History of Art": 20157,
"History and Modern Languages": 20157,
"History and Politics": 20157,
"Human, Social, and Political Sciences": 20157,
"Land Economy": 20157,
"Law": 20157,
"Linguistics": 20157,
"Modern and Medieval Languages": 20157,
"Philosophy": 20157,
"Theology, Religion, and Philosophy of Religion": 20157,
"Mathematics": 22482,
"Architecture": 26376, "Geography": 26376, "Music": 26376,
"Chemical Engineering": 30678,
"Computer Science": 30678,
"Engineering": 30678,
"Management Studies (Part II course)": 30678,
"Manufacturing Engineering (Part II course)": 30678,
"Natural Sciences": 30678,
"Psychological and Behavioural Sciences": 30678,
"Veterinary Medicine": 52638,
"Medicine (Graduate Course)": 70131, "Medicine": 70131,}
            tuition_fee_dict = {"Anglo-Saxon, Norse, and Celtic": 19197,
"Archaeology": 19197,
"Asian and Middle Eastern Studies": 19197,
"Classics": 19197,
"Economics": 19197,
"Education": 19197,
"English": 19197,
"History": 19197,
"History of Art": 19197,
"History and Modern Languages": 19197,
"History and Politics": 19197,
"Human, Social, and Political Sciences": 19197,
"Land Economy": 19197,
"Law": 19197,
"Linguistics": 19197,
"Modern and Medieval Languages": 19197,
"Philosophy": 19197,
"Theology, Religion, and Philosophy of Religion": 19197,
"Mathematics": 20157,
"Architecture": 22482,
"Geography": 26376,
"Music": 26376,
"Chemical Engineering": 30678,
"Computer Science": 30678,
"Engineering": 30678,
"Management Studies (Part II course)": 30678,
"Manufacturing Engineering (Part II course)": 30678,
"Natural Sciences": 30678,
"Psychological and Behavioural Sciences": 30678,
"Veterinary Medicine": 52638,
"Medicine (Graduate Course)": 70131,
"Medicine": 52638,}
            item['tuition_fee'] = tuition_fee_dict.get(item['programme_en'])
            if item['tuition_fee'] is not None:
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee'] = ", item['tuition_fee'])
            print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])

            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

