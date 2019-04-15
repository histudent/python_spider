# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/4 13:56'
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
from scrapySchool_England.TranslateMonth import  translate_month
class geturlspider(scrapy.Spider):
    name = 'getUrl'
    allowed_domains = []
    start_urls=[]
    for i in range(1,170,10):
        base_url = 'https://search.qmul.ac.uk/s/search.html?collection=queenmary-coursefinder-undergraduate-meta&query=&sort=title&start_rank='+str(i)
        start_urls.append(base_url)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)
        url = response.xpath('//li/@data-fb-result').extract()
        for i in url:
            print(i)
        # print(response.url)