# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/10/29 10:16'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from lxml import etree
import requests

class NewfoundlandMemorialUniversity_U_MarineInstituteSpider(scrapy.Spider):
    name = 'NewfoundlandMemorialUniversity_U_MarineInstitute'
    allowed_domains = ['mun.ca/']
    start_urls = []
    C= [
        'https://www.mi.mun.ca/programsandcourses/programs/maritimestudies/',
        'https://www.mi.mun.ca/programsandcourses/programs/oceanmapping/',
        'https://www.mi.mun.ca/programsandcourses/programs/technology/',
        'https://www.mi.mun.ca/programsandcourses/programs/underwatervehicles/'
    ]
    C = set(C)
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)

        #1.school_name
        school_name = 'Newfoundland Memorial University'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)