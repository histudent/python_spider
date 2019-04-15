import scrapy
import re
from w3lib.html import remove_tags
from weihongbo_England.items import UcasItem

class UcasSpider(scrapy.Spider):
    name = 'Sunshine_coast'
    allowed_domains = ['https://www.usc.edu.au']
    base_url= 'https://coursefinder.uow.edu.au/postgraduate/%s'
    start_urls = []
    C = []
    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        # print(response.url)
        item = UcasItem()