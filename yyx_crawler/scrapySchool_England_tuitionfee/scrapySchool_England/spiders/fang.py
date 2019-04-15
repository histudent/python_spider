from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import csv
import requests
from lxml import etree
from scrapySchool_England.getIELTS import get_ielts, get_toefl

class FangSpider(CrawlSpider):
    name = "fang"
    start_urls = ["https://cn.student.com/uk/sheffield?page_number=1",
"https://cn.student.com/uk/london?page_number=1",
"https://cn.student.com/uk/manchester?page_number=1",
"https://cn.student.com/uk/nottingham?page_number=1",
"https://cn.student.com/uk/newcastle?page_number=1",
"https://cn.student.com/uk/leeds?page_number=1",
"https://cn.student.com/uk/glasgow?page_number=1",
"https://cn.student.com/uk/coventry?page_number=1",
"https://cn.student.com/uk/birmingham?page_number=1",
"https://cn.student.com/uk/leicester?page_number=1",]
    rules = (
        Rule(LinkExtractor(allow=r'page_number=\d+'), follow=True, callback='parse_data'),
    )

    def parse_data(self, response):
        print("============================")
        print(response.url)

        city = response.xpath("//div[@class='breadcrumb__container']/span//text()").extract()
        print("city: ", ''.join(city))

        fangming = response.xpath("//div[@class='property-list']/div[@class='property-card']/div[@class='property-card__body']/div[@class='property-card__info']/a/h2[@class='property-card__name']//text()").extract()
        print("fangming: ", fangming)
        print(len(fangming))

        with open('fang.txt', 'a') as f:
            for fang in fangming:
                f.write(''.join(city) + "======" + fang + "\n")














