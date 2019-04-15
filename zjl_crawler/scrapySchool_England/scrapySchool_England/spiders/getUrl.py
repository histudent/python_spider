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
from scrapySchool_England.clearSpace import clear_space
class geturlspider(scrapy.Spider):
    name = 'getUrl'
    allowed_domains = []
    start_urls=[]
    for i in range(0,15,1):
        # print(i)
        base_url = 'https://www.uos.ac.uk/course-list?search_api_views_fulltext=&field_study_mode%5B0%5D=41&type%5B0%5D=ucs_ug_courses&field_international_students%5B0%5D=43&page='+str(i)
        start_urls.append(base_url)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)
        url_list = response.xpath("//div[@class='l-teaser--image c-teaser--image']//@href").extract()
        # ucascode = response.xpath('//*[@id="search-results"]/li/ul/li[3]/text()').extract()
        # major_type1 = response.xpath('//*[@id="search-results"]/li/h3/a').extract()
        # clear_space(major_type1)
        for i in url_list:
            print(i)
        # for k in ucascode:
        #     print(k)
        # for j in major_type1:
        #     print(j)
        # print(response.url)