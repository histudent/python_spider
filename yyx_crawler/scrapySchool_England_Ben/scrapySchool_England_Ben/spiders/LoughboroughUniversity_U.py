# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
import requests
from lxml import etree
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration


class LoughboroughUniversity_USpider(scrapy.Spider):
    name = "LoughboroughUniversity_U"
    start_urls = ["http://www.lboro.ac.uk/study/undergraduate/courses/a-z/"]
    # start_urls = ["http://search.lboro.ac.uk/s/search.html?query=&f.Level%7Clevel=Undergraduate&collection=loughborough-courses&sort=rel&start_rank=1"]
    # print(len(start_urls))
    # start_urls = list(set(start_urls))
    # print(len(start_urls))

    # rules = (
    #     Rule(LinkExtractor(allow=r'start_rank=\d+'), follow=True, callback="page"),
    #     Rule(LinkExtractor(restrict_xpaths=r"//div[@class='results']/div[@class='result']/h2[@class='result__heading']/a"), follow=True, callback="parse_data"),
    # )
    # def page(self, response):
    #     print(response.url)

    def parse(self, response):
        # //div[@class='programmes']/ul[@class='list list--programmes']/li/h2[@class='list__heading heading']/a[@class='list__link']
        programmeList = response.xpath("//ul[@class='list list--courses']/li/a/h3/span[1]//text()").extract()
        # print("programmeList: ", programmeList)
        # print(len(programmeList))

        departmentList = response.xpath("//ul[@class='list list--courses']/li/a/p//text()").extract()
        clear_space(departmentList)
        # print("departmentList: ", departmentList)
        # print(len(departmentList))

        departmentDict = {}
        for i in range(len(programmeList)):
            departmentDict[programmeList[i]] = departmentList[i]
        # print(departmentDict)
        links = response.xpath("//ul[@class='list list--courses']/li/a/@href").extract()
        for link in links:
            url = "http://www.lboro.ac.uk" + link
            yield scrapy.Request(url, callback=self.parse_data, meta=departmentDict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "Loughborough University"
        # item['country'] = 'England'
        # item['website'] = 'http://www.lboro.ac.uk/'
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        try:
            # 学位名称
            degree_name = response.xpath(
                "//span[@class='course-info__qualification course-info__qualification--default active']//text()").extract()
            # print("degree_name: ", degree_name)
            item['degree_name'] = ''.join(degree_name).replace(', PG certificate', '').strip()
            print("item['degree_name']: ", item['degree_name'])

            # 专业
            programme_en = response.xpath(
                "//h1[@class='course-info__heading']/text()").extract()
            clear_space(programme_en)
            item['programme_en'] = ''.join(programme_en).strip()
            print("item['programme_en']: ", item['programme_en'])

            # 学院
            item['department'] = response.meta.get(item['programme_en'])
            if item['programme_en'] == "Finance and Management":
                item['department'] = "Business and Economics"
            print("item['department']: ", item['department'])

            # 授课类型
            # mode = response.xpath(
            #     "//dt[@class='list__item list__item--term'][contains(text(),'Full-time:')]//text()").extract()
            # clear_space(mode)
            # if len(mode) != 0:
            #     item['teach_time'] = 'fulltime'
            # print("item['teach_time']: ", item['teach_time'])


            start_date = response.xpath(
                "//span[@class='list__text'][contains(text(),'Start date')]/../following-sibling::dd[1]//text()").extract()
            clear_space(start_date)
            # print("start_date: ", start_date)
            if len(start_date) > 0:
                item['start_date'] = getStartDate(''.join(start_date[0]))
            # print("item['start_date']: ", item['start_date'])

            tuition_fee = response.xpath(
                "//span[@class='list__text'][contains(text(),'International fee')]/../following-sibling::dd//text()").extract()
            clear_space(tuition_fee)
            # print('tuition_fee: ', tuition_fee)
            if len(tuition_fee) > 0:
                item['tuition_fee_pre'] = '£'
                item['tuition_fee'] = getTuition_fee(''.join(tuition_fee))
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])
            # print("item['tuition_fee']: ", item['tuition_fee'])

            location = response.xpath(
                "//dt[@class='list__item list__item--term'][contains(text(),'Location:')]/following-sibling::dd//text()").extract()
            clear_space(location)
            item['location'] = ''.join(location).strip()
            # print("item['location']: ", item['location'])

            overview_en = response.xpath("//div[@id='overview']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
            # print("item['overview_en']: ", item['overview_en'])

            # modules
            modules_en = response.xpath("//div[@id='study']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules_en))
            # print("item['modules_en']: ", item['modules_en'])

            # teaching_assessment
            assessment_en = response.xpath("//div[@class='course-section course-section--assessed']").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            alevel = response.xpath(
                "//dt[@class='list__item list__item--term'][contains(text(),'A-Level')]/following-sibling::dd//text()").extract()
            alevel = response.xpath(
                "//span[@class='list__text'][contains(text(),'Typical offer')]/../following-sibling::dd//text()").extract()
            clear_space(alevel)
            if len(alevel) > 0:
                item['alevel'] = ''.join(alevel[0]).strip()
            # print("item['alevel'] = ", item['alevel'])

            ib = response.xpath(
                "//dt[@class='list__item list__item--term'][contains(text(),'IB')]/following-sibling::dd//text()").extract()
            item['ib'] = ''.join(ib).strip()
            # print("item['ib'] = ", item['ib'])

            # //div[@id='china']
            require_chinese_en = response.xpath(
                "//div[@id='china']").extract()
            item['require_chinese_en'] = remove_class(clear_lianxu_space(require_chinese_en))
            # print("item['require_chinese_en'] = ", item['require_chinese_en'])

            item['ielts'] = 6.5
            item['ielts_l'] = 6.0
            item['ielts_s'] = 6.0
            item['ielts_r'] = 6.0
            item['ielts_w'] = 6.0
            if item['programme_en'] == "Communication and Media Studies":
                item['ielts'] = 7.0
                item['ielts_l'] = 6.0
                item['ielts_s'] = 6.0
                item['ielts_r'] = 6.0
                item['ielts_w'] = 6.0
            elif item['programme_en'] == "Information Management and Business" or item[
                'programme_en'] == "Accounting and Financial Management" or item[
                'programme_en'] == "Management Sciences" or item[
                'programme_en'] == "Retailing, Marketing and Management" or item[
                'programme_en'] == "International Business" or item['programme_en'] == "Finance and Management" or item[
                'programme_en'] == "Economics" or item['programme_en'] == "Business Economics and Finance" or item[
                'programme_en'] == "International Economics" or item['programme_en'] == "Economics with Geography" or \
                            item['programme_en'] == "Economics with Politics" or item[
                'programme_en'] == "Economics with Accounting" or item['programme_en'] == "Economics and Management":
                item['ielts'] = 7.0
                item['ielts_l'] = 6.5
                item['ielts_s'] = 6.5
                item['ielts_r'] = 6.5
                item['ielts_w'] = 6.5
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            career = response.xpath("//div[@id='career']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            item['apply_proces_en'] = "http://www.lboro.ac.uk/study/undergraduate/apply/"

            # //option[@value='default']//text()    //span[@class='form__option-value']
            duration = response.xpath("//label[contains(text(),'Study options')]/following-sibling::span//text()").extract()
            clear_space(duration)
            print("duration: ", duration)
            if len(duration) > 0:
                duration_list = getIntDuration(''.join(duration))
                if len(duration_list) == 2:
                    item['duration'] = duration_list[0]
                    item['duration_per'] = duration_list[-1]
                print("item['duration'] = ", item['duration'])
                print("item['duration_per'] = ", item['duration_per'])

                # //span[@class='list__text'][contains(text(),'UCAS code')]/../following-sibling::dd
                ucascode = response.xpath(
                    "//span[@class='list__text'][contains(text(),'UCAS code')]/../following-sibling::dd//text()").extract()
                clear_space(ucascode)
                print("ucascode: ", ucascode)
                if len(ucascode) > 0:
                    item['ucascode'] = ''.join(ucascode[0]).strip()
                print("item['ucascode'] = ", item['ucascode'])
                yield item
            else:
                duration = response.xpath(
                    "//option[@value='default']//text()").extract()
                clear_space(duration)
                print("duration1: ", duration)

                duration_list = getIntDuration(''.join(duration))
                if len(duration_list) == 2:
                    item['duration'] = duration_list[0]
                    item['duration_per'] = duration_list[-1]
                print("item['duration'] = ", item['duration'])
                print("item['duration_per'] = ", item['duration_per'])

                # //span[@class='list__text'][contains(text(),'UCAS code')]/../following-sibling::dd
                ucascode = response.xpath(
                    "//span[@class='list__text'][contains(text(),'UCAS code')]/../following-sibling::dd//text()").extract()
                clear_space(ucascode)
                print("ucascode: ", ucascode)
                if len(ucascode) > 0:
                    item['ucascode'] = ''.join(ucascode[0]).strip()
                print("item['ucascode']1 = ", item['ucascode'])
                yield item

                duration = response.xpath(
                    "//option[@value='variant']//text()").extract()
                clear_space(duration)
                print("duration2: ", duration)

                duration_list = getIntDuration(''.join(duration))
                if len(duration_list) == 2:
                    item['duration'] = duration_list[0]
                    item['duration_per'] = duration_list[-1]
                print("item['duration'] = ", item['duration'])
                print("item['duration_per'] = ", item['duration_per'])

                # //span[@class='list__text'][contains(text(),'UCAS code')]/../following-sibling::dd
                ucascode = response.xpath(
                    "//span[@class='list__text'][contains(text(),'UCAS code')]/../following-sibling::dd//text()").extract()
                clear_space(ucascode)
                print("ucascode: ", ucascode)
                if len(ucascode) > 0:
                    item['ucascode'] = ''.join(ucascode[-1]).strip()
                print("item['ucascode']2 = ", item['ucascode'])
                yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)