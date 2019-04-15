# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space, clear_space_str
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime
import requests
from lxml import etree
from w3lib.html import remove_tags


class StGeorgesUniversityOfLondon_USpider(scrapy.Spider):
    name = "StGeorgesUniversityOfLondon_U"
    start_urls = ["https://www.sgul.ac.uk/study/undergraduate/undergraduate-courses"]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3472.3 Safari/537.36"}

    def parse(self, response):
        links = ["https://www.sgul.ac.uk/study/undergraduate/undergraduate-courses/biomedical-science-msci",
"https://www.sgul.ac.uk/study/undergraduate/undergraduate-courses/biomedical-science-bsc-hons",
"https://www.sgul.ac.uk/study/undergraduate/undergraduate-courses/clinical-pharmacology-bsc-hons",
"https://www.sgul.ac.uk/study/undergraduate/undergraduate-courses/medicine-mbbs",
"https://www.sgul.ac.uk/study/undergraduate/undergraduate-courses/occupational-therapy-bsc",
"https://www.sgul.ac.uk/study/undergraduate/undergraduate-courses/physiotherapy-bsc-hons",
"https://www.sgul.ac.uk/study/undergraduate/undergraduate-courses/radiography-diagnostic-bsc-hons",
"https://www.sgul.ac.uk/study/undergraduate/undergraduate-courses/radiography-therapeutic-bsc-hons", ]

        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "St George's, University of London"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:
                entry_url = response.xpath("//a[contains(text(),'Entry')]/@href").extract()
                # print("entry_url: ", entry_url)
                if len(entry_url) != 0:
                    parse_entry_url = "https://www.sgul.ac.uk" + entry_url[0]
                    # print("parse_entry_url: ", parse_entry_url)
                    entry_dict = self.parse_rntry_requirements(parse_entry_url)
                    # print(entry_dict)
                    # item['rntry_requirements'] = entry_dict.get('rntry_requirements')

                    item['alevel'] = entry_dict.get('alevel')
                    item['ib'] = entry_dict.get('ib')
                print("item['alevel']: ", item['alevel'])
                print("item['ib']: ", item['ib'])

                yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_rntry_requirements(self, parse_entry_url):
        data = requests.get(parse_entry_url, headers=self.headers)
        response = etree.HTML(data.text)
        entry_dict = {}
        rntry_requirements = response.xpath("//div[@class='col col1 article-content']/div//text()")
        rntry_requirements_str = clear_lianxu_space(rntry_requirements)
        rep = re.findall(r"//<!--.*//-->", rntry_requirements_str)
        # print(rep, "======")
        rntry_requirements_str = rntry_requirements_str.replace(''.join(rep), '')

        ielts_desc = response.xpath("//h2[contains(text(),'IELTS')]/..//text()|//strong[contains(text(),'IELTS')]/../..//text()|"
                                    "//td[contains(text(),'IELTS')]/following-sibling::td[1]//text()")
        # print("ielts_desc: ", ielts_desc)
        # ielts_desc = ' '.join(ielts_desc).replace("\n", "").replace("\r", "").replace('\t', "").replace("  ", "").strip()
        ielts_desc_str = clear_lianxu_space(ielts_desc)

        alevel = response.xpath(
            "//*[contains(text(),'A Level')]/../../following-sibling::*//text()|"
            "//*[contains(text(),'A Level')]/../following-sibling::*//text()")
        alevel_str = ""
        # if len(alevel) > 0:
        alevel_str = clear_lianxu_space(alevel)
        # print("ielts_desc: ", ielts_desc)

        ib = response.xpath(
            "//*[contains(text(),'International Baccalaureate')]/../../following-sibling::*//text()|"
            "//*[contains(text(),'International Baccalaureate')]/../following-sibling::*//text()")
        ib_str = ""
        # print(ib)
        # if len(ib) > 0:
        ib_str = clear_lianxu_space(ib).strip()
        # print("ielts_desc: ", ielts_desc)
        entry_dict['rntry_requirements'] = rntry_requirements_str
        entry_dict['ielts_desc'] = ielts_desc_str
        entry_dict['alevel'] = alevel_str
        entry_dict['ib'] = ib_str
        return entry_dict
