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


class UniversityOfBolton_USpider(scrapy.Spider):
    name = "UniversityOfBolton_U"
    start_urls = ["https://www.bolton.ac.uk/subject-areas/all-subjects/"]

    def parse(self, response):
        links = ["https://courses.bolton.ac.uk/course/COM001-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ENG017-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/CRT030-F-BSA-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ENG018-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/CRT029-F-BSA-SX/2018-19/",
"https://courses.bolton.ac.uk/course/PSY003-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/GAM003-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ART006-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/ART007-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/CRT021-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/CRT022-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM007-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/TFS024-F-SOA-SX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM041-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/CRT027-F-BSA-SX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM043-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/TFS024-F-SOA-FX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM045-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM042-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/ESH001-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM044-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/ENG018-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM046-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/GAM005-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/CRT008-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/TFS007-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/CRT002-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/CRT008-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/CRT002-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/HLT037-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/CRT007-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/CRT007-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/TFS007-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/HLT049-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/EDU057-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/CSA011-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/CSA011-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/NRS005-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/CST002-F-UOB-SN/2018-19/",
"https://courses.bolton.ac.uk/course/PSY001-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/NRS006-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/HLT029-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ESH005-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/NRS003-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/AAL011-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/CST002-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/NRS004-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/CST002-F-UOB-FN/2018-19/",
"https://courses.bolton.ac.uk/course/PSY001-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/NRS002-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ESH005-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/AAL011-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/CST002-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/HLT029-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM002-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/PSY013-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/BES005-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/DEN002-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/BES005-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ENG017-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ENG022-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ENG022-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/CIE006-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/CIE006-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/COM009-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/COM006-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/GAM005-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/COM021-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/GAM002-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/COM006-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/COM021-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/COM009-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/COM001-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/GAM002-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ENG023-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/SPT009-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/SRB002-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/SPT003-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ENG023-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/SPT009-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/SRB002-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/SPT003-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/ENG004-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ELR003-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/MAT001-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/MAT004-F-UOB-IX/2018-19/",
"https://courses.bolton.ac.uk/course/MAT003-F-UOB-IX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM005-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/ELR003-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM043-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM045-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/AAL002-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/ART006-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ART002-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ART010-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM042-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/AAL002-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM040-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM040-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM041-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM046-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM044-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM005-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM002-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/CRT024-F-SSR-SX/2018-19/",
"https://courses.bolton.ac.uk/course/BAM007-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/CRE002-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/CRE002-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/TFS004-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ESH001-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ENG004-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/AAL006-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/AAL006-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/ART029-F-UOB-FX/2018-19/",
"https://courses.bolton.ac.uk/course/ART027-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ART005-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ART028-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/ART029-F-UOB-SX/2018-19/",
"https://courses.bolton.ac.uk/course/HLT006-F-UOB-TX/2018-19/", ]
        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})


    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Bolton"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:
            # ucas_point = response.xpath("//li[@class='iconim points']//b[contains(text(),'UCAS points:')]/../span//text()").extract()
            # print("ucas_point: ", ucas_point)

            alevel = response.xpath(
                "//li[@class='iconim points']//b[contains(text(),'UCAS points:')]/../span//text()").extract()
            item['alevel'] = clear_lianxu_space(alevel)
            print("item['alevel']: ", item['alevel'])

            yield item

        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

