# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_Australian_ben.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_ben.getItem import get_item
from scrapySchool_Australian_ben.getTuition_fee import getTuition_fee
from scrapySchool_Australian_ben.items import ScrapyschoolAustralianBenItem
import json
from lxml import etree
import requests
from scrapySchool_Australian_ben.remove_tags import remove_class

class UNSWBen_degree_nameSchoolSpider(scrapy.Spider):
    name = "UNSWBen_degree_name"
    start_urls = ["http://www.international.unsw.edu.au/undergraduate-study"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    resultDict = {}
    degree_overview_resultDict1 = {}
    career_resultDict1 = {}
    def parse(self, response):
        links = response.xpath("//ul[@class='programareas-list']//li/a/@href").extract()
        print("subject link = ", links)
        for link in links:
            url = "http://www.international.unsw.edu.au" + link
            yield scrapy.Request(url, callback=self.parse_programmeUrl)
        # print("resultDict: ", self.resultDict)

    def parse_programmeUrl(self, response):
        links = response.xpath("//a[contains(text(), 'Visit Art and Design')]/@href|//a[contains(text(), 'Visit Engineering')]/@href|//a[contains(text(), 'Visit Arts and Social Sciences')]/@href|//a[contains(text(), 'Visit Science')]/@href|//a[contains(text(), 'Visit Business School')]/@href|//a[contains(text(), 'Visit Medicine')]/@href|//a[contains(text(), 'Visit Built Environment')]/@href|//a[contains(text(), 'Visit Law')]/@href").extract()

        degree_name = response.xpath("//h5[contains(text(), 'Bachelor of')]//text()").extract()
        print("degree_name: ", degree_name)
        # degree_name_str = ''.join(degree_name).strip()
        print("degree name link = ", links)
        # print("degree_name_str = ", degree_name_str)
        for i in range(len(links)):
            self.resultDict[links[i]] = degree_name[i]
            yield scrapy.Request(links[i], callback=self.parse_feedata)

    def parse_feedata(self, response):
        print("==============================")
        print(response.url)
        degree_name = self.resultDict.get(response.url)
        print("degree_name==: ", degree_name)

        degree_overview = response.xpath("//*/a[contains(text(), 'Overview')]/../../following-sibling::*[position()<6]|"
                                         "//*/a[contains(text(), 'Overview')]/../following-sibling::*[position()<6]").extract()
        degree_overview = response.xpath(
            "//div[@class='field field-type-text-long']").extract()
        clear_space(degree_overview)
        degree_overview = remove_class(''.join(degree_overview).strip())
        print("degree_overview: ", degree_overview)

        career_en = response.xpath(
            "//*/a[contains(text(), 'Career')]/../preceding-sibling::*[1]/following-sibling::*[position()<6]").extract()
        clear_space(career_en)
        career_en = remove_class(''.join(career_en).strip())
        print("career_en: ", career_en)

        self.degree_overview_resultDict1[degree_name] = degree_overview
        self.career_resultDict1[degree_name] = career_en
        print("**degree_overview_resultDict1: ", self.degree_overview_resultDict1)
        print("*****career_resultDict1: ", self.career_resultDict1)

