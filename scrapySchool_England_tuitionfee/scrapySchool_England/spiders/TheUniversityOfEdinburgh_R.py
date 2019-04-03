# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space, clear_space_str
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
import requests
from lxml import etree
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.getDuration import getTeachTime

class TheUniversityofEdinburgh_RSpider(scrapy.Spider):
    name = "TheUniversityofEdinburgh_R"
    # 研究领域链接
    start_urls = ["https://www.ed.ac.uk/studying/postgraduate/degrees/index.php?r=site/research&edition=2018"]
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    def parse(self, response):
        links = response.xpath("//div[@id='proxy_leftContent']/div[@class='panel panel-default']/div[@class='list-group']/a/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))
        for link in links:
            url = "https://www.ed.ac.uk"+ link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "The University of Edinburgh"
        # item['country'] = 'England'
        # item['website'] = 'https://www.ed.ac.uk/'
        item['url'] = response.url
        # 授课方式
        item['teach_type'] = 'phd'
        # 学位类型
        item['degree_type'] = 3
        print("===========================")
        print(response.url)
        try:
            # 专业
            programme = response.xpath(
                "//h1[@itemprop='headline']//text()").extract()
            clear_space(programme)
            item['programme_en'] = ''.join(programme)
            print("item['programme_en']: ", item['programme_en'])

            degree_name = response.xpath(
                "//span[contains(text(),'Awards:')]/../text()").extract()
            if len(degree_name) > 0:
                item['degree_name'] = degree_name[0]
            print("item['degree_name']: ", item['degree_name'])

            teach_time = response.xpath(
                "//span[contains(text(),'Study modes:')]/../text()").extract()
            teach_time = ''.join(teach_time)
            # teach_time_re = re.findall(r"[a-zA-Z]{4}-time", teach_time)
            # print("teach_time_re: ", teach_time_re)
            item['teach_time'] = getTeachTime(teach_time)
            # item['teach_time'] = item['teach_time'].replace("parttime", "").replace(',', '')
            # print("item['teach_time']: ", item['teach_time'])

            department = response.xpath(
                "//div[@class='col-xs-12']//div[@class='row']//div[@class='col-xs 12']//ul//li//span[contains(text(),'College:')]/following-sibling::*//text()").extract()
            if len(department) == 0:
                department = response.xpath(
                    "//div[@class='col-xs-12']//div[@class='row']//div[@class='col-xs 12']//ul//li//span[contains(text(),'School:')]/following-sibling::a[1]/text()").extract()
            clear_space(department)
            item['department'] = ''.join(department).strip()
            # print("item['department']: ", item['department'])

            # //div[@class='col-xs-12']//div[@class='row']//div[@class='col-xs-12']//ul[@class='addressList']//li[@class='contactCampus']
            location = response.xpath(
                "//div[@class='col-xs-12']//div[@class='row']//div[@class='col-xs-12']//ul[@class='addressList']//li[@class='contactCampus']/text()").extract()
            clear_space(location)
            item['location'] = ''.join(location).strip()
            # print("item['location']: ", item['location'])

            # //option[@value='0010']
            start_date = response.xpath(
                "//select[@name='code2']//option//text()").extract()
            clear_space(start_date)
            # print(start_date)
            if len(start_date) > 0:
                start_date = start_date[0].strip()
            # print("item['start_date']: ", item['start_date'])
                item['start_date'] = getStartDate(start_date)
            # print("item['start_date'] = ", item['start_date'])

            overview = response.xpath(
                "//div[@id='proxy_collapseresearch_profile']/..").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])

            duration = response.xpath(
                "//table[@class='table table-striped']//tbody//tr[1]/td[3]//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration = ''.join(duration).strip()
            duration_int = re.findall(r"\d+", duration)
            if len(duration_int) != 0:
                item['duration'] = int(''.join(duration_int))
            # print("item['duration']: ", item['duration'])

            if "year" in duration or "Year" in duration:
                item['duration_per'] = 1
            if "month" in duration or "Month" in duration:
                item['duration_per'] = 3
            # print("item['duration_per']: ", item['duration_per'])


            # //div[@id='proxy_collapseprogramme']
            modules1 = response.xpath(
                "//div[@id='proxy_collapsehow_taught']/div/*[position()<=last()]").extract()
            # clear_space(modules1)
            modules2url = response.xpath(
                "//html//tr[1]/td[5]/a/@href").extract()
            modules2 = ""
            if len(modules2url) != 0:
                modules2url = ''.join(modules2url)
                modules2 = self.get_modules2(modules2url)
            item['modules_en'] = remove_class(clear_lianxu_space(list(modules1)))
            if modules2 != "":
                item['modules_en'] += "\n" + modules2
            # print("item['modules_en']: ", item['modules_en'])

            career = response.xpath(
                "//div[@id='proxy_collapsecareer_opp']/..").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            # //div[@id='proxy_collapseentry_req']
            entry_requirements = response.xpath(
                "//div[@id='proxy_collapseentry_req']/..//text()").extract()
            item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            IELTS = response.xpath("//abbr[contains(text(),'IELTS')]/..//text()").extract()
            item['ielts_desc'] = ''.join(IELTS)
            print("item['ielts_desc']: ", item['ielts_desc'])

            ieltsDict = get_ielts(item['ielts_desc'])
            item['ielts'] = ieltsDict.get("IELTS")
            item['ielts_l'] = ieltsDict.get("IELTS_L")
            item['ielts_s'] = ieltsDict.get("IELTS_S")
            item['ielts_r'] = ieltsDict.get("IELTS_R")
            item['ielts_w'] = ieltsDict.get("IELTS_W")
            print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            TOEFL = response.xpath("//abbr[contains(text(),'TOEFL')]/..//text()").extract()
            item['toefl_desc'] = ''.join(TOEFL)
            print("item['toefl_desc']: ", item['toefl_desc'])

            toeflDict = get_toefl(item['toefl_desc'])
            item['toefl'] = toeflDict.get("TOEFL")
            item['toefl_l'] = toeflDict.get("TOEFL_L")
            item['toefl_s'] = toeflDict.get("TOEFL_S")
            item['toefl_r'] = toeflDict.get("TOEFL_R")
            item['toefl_w'] = toeflDict.get("TOEFL_W")
            print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
                    item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

            tuition_feeDict = {}
            tuition_fee_url = response.xpath("//div[@id='proxy_collapsefees']//ul/li/a[contains(text(),'Full')]/@href").extract()
            # print("tuition_fee_url: ", tuition_fee_url)
            if len(tuition_fee_url) > 0:
                tuition_fee_url_str = tuition_fee_url[0]
                fee = self.parse_tuition_fee(tuition_fee_url_str)
                clear_space(fee)
                fee_re = re.findall(r"£\d+,\d+", ''.join(fee))
                # print("fee_re: ", fee_re)
                item['tuition_fee'] = getTuition_fee(''.join(fee_re))
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee']: ", item['tuition_fee'])

            item['require_chinese_en'] = "https://www.ed.ac.uk/studying/international/postgraduate-entry/asia/china"
            item['apply_proces_en'] = "https://www.ed.ac.uk/studying/postgraduate/applying"
            # apply_proces_en = response.xpath(
            #     "//div[@id='proxy_collapseHowToApply']/..").extract()
            # item['apply_proces_en'] = remove_class(clear_lianxu_space(apply_proces_en))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            yield item
        except Exception as e:
            with open(item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

    def get_modules2(self, modules2url):
        data = requests.get(modules2url, headers=self.headers)
        response = etree.HTML(data.text)
        modules2 = response.xpath("/html/body/div[@class='container']")
        m2 = etree.tostring(modules2[0], encoding='unicode', pretty_print=False, method='html')
        m2 = remove_class(clear_space_str(m2))
        return m2

    def parse_tuition_fee(self, tuition_fee_url):
        data = requests.get(tuition_fee_url, headers=self.headers)
        response = etree.HTML(data.text)
        fee = response.xpath("//html//tr[2]/td//text()")
        return fee
