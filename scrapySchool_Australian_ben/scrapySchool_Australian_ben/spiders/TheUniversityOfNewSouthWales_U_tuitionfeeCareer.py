# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_Australian_ben.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_ben.getItem import get_item
from scrapySchool_Australian_ben.getTuition_fee import getTuition_fee
from scrapySchool_Australian_ben.items import ScrapyschoolAustralianBenItem
from scrapySchool_Australian_ben.remove_tags import remove_class
from scrapySchool_Australian_ben.getStartDate import getStartDate
from scrapySchool_Australian_ben.getDuration import getIntDuration
from lxml import etree
import requests
from w3lib.html import remove_tags


class TheUniversityOfNewSouthWales_U_TuitionfeeCareerSpider(scrapy.Spider):
    name = "TheUniversityOfNewSouthWales_U_TuitionfeeCareer"
    start_urls = ["http://www.international.unsw.edu.au/faculty/art-design-undergraduate-degree-programs",
"http://www.international.unsw.edu.au/faculty/arts-social-sciences-undergraduate-degree-programs",
"http://www.international.unsw.edu.au/faculty/built-environment-undergraduate-degree-programs",
"http://www.international.unsw.edu.au/faculty/business-school-undergraduate-degree-programs",
"http://www.international.unsw.edu.au/faculty/engineering-undergraduate-degree-programs",
"http://www.international.unsw.edu.au/faculty/law-undergraduate-degree-programs",
"http://www.international.unsw.edu.au/faculty/medicine-undergraduate-degree-programs",
"http://www.international.unsw.edu.au/faculty/science-undergraduate-degree-programs",]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))
    headers_base = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}



    def parse(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "The University of New South Wales"
        # item['country'] = 'Australia'
        # item['website'] = 'http://www.unsw.edu.au/'
        item['url'] = response.url
        item['degree_type'] = 1
        # item['teach_time'] = 'coursework'
        print("===========================")
        print(response.url)
        try:
            department = response.xpath("//div[@class='inlinevideo-inner']//div[@class='contentarea-title']/h3//text()").extract()
            item['department'] = ''.join(department).strip()
            print("item['department']: ", item['department'])

            # 学位类型列表
            degree_type = response.xpath("//section//div[@class='degree js-degree']//h5//text()").extract()
            clear_space(degree_type)
            print(len(degree_type))
            print("degree_type: ", degree_type)

            duration = response.xpath(
                "//section//dt[contains(text(), 'Minimum years')]/following-sibling::dd[1]//text()").extract()
            clear_space(duration)
            print(len(duration))
            print("duration: ", duration)

            start_date = response.xpath(
                "//section//dt[contains(text(), 'Entry')]/following-sibling::dd[1]//text()").extract()
            clear_space(start_date)
            print(len(start_date))
            print("start_date: ", start_date)

            tuition_fee = response.xpath(
                "//section//dt[contains(text(), 'Estimated first year tuition')]/following-sibling::*[1]//text()").extract()
            clear_space(tuition_fee)
            print(len(tuition_fee))
            print("tuition_fee: ", tuition_fee)

            careerEle = response.xpath("//section//dl[last()]")
            print(len(careerEle))
            print("careerEle: ", careerEle)

            for i in range(len(degree_type)):
                print("-------------------"+str(i)+"-----------------")
                item['degree_name'] = degree_type[i]
                print("item['degree_name']: ", item['degree_name'])

                # 课程长度
                item['duration'] = duration[i]
                print("item['duration']: ", item['duration'])

                # 开学时间
                item['start_date'] = start_date[i]
                if "and" in item['start_date']:
                    start_date_sp = item['start_date'].split("and")
                else:
                    start_date_sp = [item['start_date']]
                # print(start_date_sp)
                start_date_str = ""
                for st in start_date_sp:
                    start_date_str += getStartDate(st).replace("0", "") + ","
                item['start_date'] = start_date_str.strip().strip(',').strip()
                print("item['start_date']: ", item['start_date'])

                # 学费
                item['tuition_fee'] = tuition_fee[i].replace("AUD $", "").replace(",", "").strip()
                print("item['tuition_fee']: ", item['tuition_fee'])

                # print(careerEle[i])
                careerRe = careerEle[i].xpath(".//dt[contains(text(), 'Career Opportunities')]|.//dt[contains(text(), 'Career Opportunities')]/following-sibling::dd[1]").extract()
                item['career_en'] = remove_class(clear_lianxu_space(careerRe))
                print("item['career_en']: ", item['career_en'])

                if "Graduate" not in item['degree_name']:
                    yield item

            # programme = response.xpath("//div[@class='internalContentWrapper']/h1[1]//text()").extract()
            # programme = ''.join(programme)
            # programme = programme.split("-")
            # item['programme_en'] = programme[0].strip()
            # print("item['programme_en']: ", item['programme_en'])

            # yield item
        except Exception as e:
            with open(".//scrapySchool_Australian_yan/error/"+item['university']+str(item['degree_type'])+".txt", 'w', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_major_detile(self, major_url, item):
        item['url'] = major_url
        print("item['url']_major: ", item['url'])
        data = requests.get(major_url, headers=self.headers_base)
        response = etree.HTML(data.text.replace('<?xml version="1.0" encoding="utf-8"?>', ""))
        # print("===1=", response)
        programme = response.xpath("//div[@class='internalContentWrapper']/h1[1]//text()")
        print("prog ", programme)
        programme_str = ''.join(programme)
        if "-" in programme_str:
            programme_list = programme_str.split("-")
            item['programme_en'] = ''.join(programme_list[:-1]).strip()
        else:
            item['programme_en'] = programme_str
        print("item['programme_en']_major: ", item['programme_en'])

        overview_en = response.xpath("//h2[contains(text(),'Stream Outline')]/../preceding-sibling::*[1]/following-sibling::*[position()<3]|"
                                     "//td[@class='mainInformation']//div[1]")
        overview_en_str = ""
        if len(overview_en) > 0:
            for m in overview_en:
                # print("===", overview_en_str)
                overview_en_str += etree.tostring(m, encoding='unicode',method='html')
        item['overview_en'] = remove_class(clear_lianxu_space([overview_en_str]))
        print("item['overview_en']_major: ", item['overview_en'])

        modules_en = response.xpath(
            "//a[@name='planstructure']/preceding-sibling::*[1]/following-sibling::*[position()<last()-1]|"
            "//table[@class='tabluatedInfo']")
        modules_en_str = ""
        if len(modules_en) > 0:
            for m in modules_en:
                modules_en_str += etree.tostring(m, encoding='unicode',method='html')
        item['modules_en'] = remove_class(clear_lianxu_space([modules_en_str]))
        print("item['modules_en']_major: ", item['modules_en'])

        new_url_list = response.xpath("//table[@class='tabluatedInfo']//tr/td/a/@href")
        return new_url_list