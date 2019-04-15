# -*- coding: utf-8 -*-
import scrapy, requests
from lxml import etree
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re, json
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime

class AberystwythUniversity_USpider(scrapy.Spider):
    name = "AberystwythUniversity_U"
    # allowed_domains = ["herts.ac.uk", "funnelback.co.uk"]
    start_urls = ["https://courses.aber.ac.uk/atoz/"]

    def parse(self, response):
        links = response.xpath("//div[@class='full-width-accordion']/div/div[@class='categories-container']/div[@class='list-listing course-search-listing']/div/ul/li/a[@class='course'][contains(@href, '//courses.aber.ac.uk/undergraduate')]/@href").extract()

        # 组合字典
        programme_dict = {}
        programme_list = response.xpath("//div[@class='full-width-accordion']/div/div[@class='categories-container']/div[@class='list-listing course-search-listing']/div/ul/li/a[@class='course'][contains(@href, '//courses.aber.ac.uk/undergraduate')]//text()").extract()
        clear_space(programme_list)

        for link in range(len(links)):
            url = "https:" + links[link]
            programme_dict[url] = programme_list[link]

        print(len(links))
        links = list(set(links))
        print(len(links))
        for link in links:
            url = "https:" + link
            yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "http://www.herts.ac.uk/"
        item['university'] = "Aberystwyth University"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        item['location'] = "Aberystwyth University, Reception, Penglais, Aberystwyth, Ceredigion, SY23 3FL"
        print("===========================")
        print(response.url)
        item['major_type1'] = response.meta.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            department = response.xpath("//div[@class='banner__caption banner__caption--below']//text()").extract()
            department = ''.join(department).replace("in the ", "").strip()
            item['department'] = department
            # print("item['department']: ", item['department'])

            # 专业、学位类型
            degree_name = response.xpath("//div[@class='hero-header']//header/span//text()").extract()
            item['degree_name'] = ''.join(degree_name).strip()
            print("item['degree_name']: ", item['degree_name'])

            programme_en = response.xpath("//div[@class='hero-header']//header/h1//text()").extract()
            item['programme_en'] = ''.join(programme_en).strip()
            print("item['programme_en']: ", item['programme_en'])

            # if item['degree_name'] == "":
            #     print("*****111****")

            duration = response.xpath(
                "//h3[contains(text(),'Course Length')]/following-sibling::p//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration_str = ''.join(duration)

            duration_list = getIntDuration(duration_str)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            # //div[@id='overview']
            overview = response.xpath("//div[@class='key-facts']/following-sibling::p|"
                                      "//h3[@id='course-overview']|//h3[@id='course-overview']/following-sibling::div[1]|"
                                      "//h3[@id='coursedetails']|//h3[@id='coursedetails']/following-sibling::div[1]").extract()
            if len(overview) == 0:
                overview = response.xpath("//h2[contains(text(),'Overview')]/..").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])
            # if item['overview_en'] == "":
            #     print("*****111****")

            modules = response.xpath("//h3[@id='coursecontent']|//h3[@id='coursecontent']/following-sibling::div[1]").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])
            # if item['modules_en'] == "":
            #     print("*****111****")

            career_en = response.xpath("//h3[@id='employability']|//h3[@id='employability']/following-sibling::div[1]").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            # print("item['career_en']: ", item['career_en'])
            # if item['career_en'] == "":
                # print("*****111****")

            assessment_en = response.xpath(
                "//h3[contains(text(),'Teaching & Learning')]|//h3[contains(text(),'Teaching & Learning')]/following-sibling::div[1]").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])
            # if item['assessment_en'] == "":
            #     print("*****111****")

            alevel = response.xpath(
                "//h3[contains(text(),'Typical A-level offer')]/following-sibling::p//text()").extract()
            item['alevel'] = clear_lianxu_space(alevel)
            # print("item['alevel']: ", item['alevel'])

            ib = response.xpath(
                "//strong[contains(text(),'International Baccalaureate:')]/../text()").extract()
            item['ib'] = clear_lianxu_space(ib)
            # print("item['ib']: ", item['ib'])


            #     item['tuition_fee'] = int(feelist[0].replace('£', '').replace(',', '').strip())
            # print("item['tuition_fee']: ", item['tuition_fee'])

            # print("entry_requirementsStr: ", entry_requirementsStr)
            ielts = response.xpath("//strong[contains(text(),'English language requirements')]/..//text()").extract()
            item['ielts_desc'] = ''.join(ielts).strip()
            # print("item['ielts_desc']: ", item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            ucascode = response.xpath("//span[contains(@title,'UCAS Code')]/em//text()").extract()
            clear_space(ucascode)
            print("ucascode: ", ucascode)
            item['ucascode'] = ''.join(ucascode).strip()
            print("len: ", len(ucascode))
            print("item['ucascode'] = ", item['ucascode'])

            # 学费链接
            item['other'] = "https://www.aber.ac.uk/en/international/fees-scholarships/fees-money/int-under/"
            item['apply_proces_en'] = "https://www.aber.ac.uk/en/undergrad/apply/?course=W402"
            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

