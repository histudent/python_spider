# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re
from scrapySchool_Australian_ben.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_ben.getItem import get_item
from scrapySchool_Australian_ben.getTuition_fee import getTuition_fee
from scrapySchool_Australian_ben.items import ScrapyschoolAustralianBenItem
from scrapySchool_Australian_ben.remove_tags import remove_class
from scrapySchool_Australian_ben.getStartDate import getStartDate
from scrapySchool_Australian_ben.getDuration import getIntDuration
from scrapySchool_Australian_ben.getIELTS import get_ielts,get_toefl
from lxml import etree
import requests
from urllib import parse

# 2019/03/26 星期二 数据更新
class CentralQueenslandUniversity_USpider(scrapy.Spider):
    name = "CentralQueenslandUniversity_U"
    # start_urls = ["https://www.cqu.edu.au/courses/search-course-or-program?queries_all_query=&queries_campus_query=&queries_mode_query=On-campus&queries_level_query=Undergraduate&search_page_108095_submit_button=Search"]
    start_urls = ["https://www.cqu.edu.au/courses/find-a-course?collection=2019-cqu-courses&fmo=true&query=&meta_studyModes_or=%22On-campus%22&meta_studyLevel_or=%22Level%207%3A%20Bachelor%20Degree%22,%22Level%208%3A%20Bachelor%20Honours%20Degree%22"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        links = response.xpath("//tr//td[1]//span//a/@href|"
                               "//a[contains(text(),'Bachelor of')]/@href").extract()

        # 组合字典
        programme_dict = {}
        programme_list = response.xpath(
            "//a[contains(text(),'Bachelor of')]//text()").extract()
        # clear_space(programme_list)
        # print(len(links))

        for link in range(len(links)):
            url = links[link] + "?international"
            programme_dict[url] = programme_list[link]

        clear_space(links)
        # print(len(links))
        links = list(set(links))
        # print(len(links))

        links = ["https://www.cqu.edu.au/courses/bachelor-of-agriculture?international",
"https://www.cqu.edu.au/courses/bachelor-of-aviation-commercial-pilot?international",
"https://www.cqu.edu.au/courses/bachelor-of-education-early-childhood?international",
"https://www.cqu.edu.au/courses/bachelor-of-environmental-science?international",
"https://www.cqu.edu.au/courses/bachelor-of-hospitality-management?international",
"https://www.cqu.edu.au/courses/bachelor-of-occupational-health-and-safety?international",
"https://www.cqu.edu.au/courses/bachelor-of-occupational-therapy-honours?international",
"https://www.cqu.edu.au/courses/bachelor-of-oral-health?international",
"https://www.cqu.edu.au/courses/bachelor-of-paramedic-science?international",
"https://www.cqu.edu.au/courses/bachelor-of-physiotherapy-honours?international",
"https://www.cqu.edu.au/courses/bachelor-of-podiatry-honours?international",
"https://www.cqu.edu.au/courses/bachelor-of-speech-pathology-honours?international", ]
        for url in links:
            yield Request(url+"?international", callback=self.parse_data, meta=programme_dict)

        next_url = response.xpath("//li[@class='pagination-list__item active']/following-sibling::li/a/@href").extract()
        print("next_url: ", next_url)
        if next_url:
            for next in next_url:
                yield Request(parse.urljoin(response.url, next), callback=self.parse)


    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "Central Queensland University"
        # item['country'] = 'Australia'
        # item['website'] = 'https://www.cqu.edu.au'
        item['url'] = response.url
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        item['major_type1'] = response.meta.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            programme = response.xpath("//h1[@class='program-title']/text()|"
                                       "//h1[@itemprop='name']//text()").extract()
            clear_space(programme)
            programme = ''.join(programme).split("-")
            # print("programme: ", programme)
            programme_en = response.xpath("//th[contains(text(),'Majors')]/following-sibling::td//text()").extract()
            clear_space(programme_en)
            print("programme_en: ", programme_en)
            if len(programme_en) == 0:
                item['programme_en'] = ''.join(programme[:-1]).replace("Bachelor of", "").strip()
            else:
                item['programme_en'] = ''.join(programme_en).strip()
            print("item['programme_en']: ", item['programme_en'])
            item['degree_name'] = ''.join(programme[:-1])
            print("item['degree_name']: ", item['degree_name'])

            department = response.xpath(
                "//ol[@id='breadcrumbs']/li[4]/a//text()").extract()
            clear_space(department)
            if department:
                item['department'] = ''.join(department)
            print("item['department']: ", item['department'])

            duration = response.xpath(
                "//th[contains(text(),'Duration')]/following-sibling::td[1]//text()|"
                "//span[contains(text(),'DURATION')]/following-sibling::*[1]//text()").extract()
            clear_space(duration)
            item['duration'] = ''.join(duration).strip()
            print("item['duration']: ", item['duration'])

            start_date = response.xpath("//th[contains(text(),'Intake dates')]/following-sibling::td[1]//text()|"
                                        "//strong[contains(text(),'Term dates for 2019')]/..//text()").extract()
            clear_space(start_date)
            if "," in ''.join(start_date):
                start_date = ''.join(start_date).split(",")
            print("start_date: ", start_date)
            if start_date:
                item['start_date'] = ''.join(start_date).strip()

            monthDict = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06",
                         "july": "07", "august": "08", "september": "09", "october": "10", "november": "11",
                         "december": "12",
                         "jan": "01", "feb": "02", "mar": "03", "apr": "04", "may": "05", "jun": "06",
                         "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12",
                         "sept": "09", }
            std = []
            if len(start_date) > 0:
                for s in start_date:
                    std_tmp = monthDict.get(s.lower().strip())
                    if std_tmp is not None:
                        std.append(std_tmp)
            # if std:
            # item['start_date'] = ','.join(std).replace("0", "").strip().strip(",").strip()
            print("item['start_date']: ", item['start_date'])

            # //div[@class='careers']
            career = response.xpath(
                "//div[@class='careers']|"
                "//span[@class='ct-accordion__title'][contains(text(),'Career Opportunities and Outcomes')]/../..").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            # //p[@itemprop='description']/following-sibling::p
            degree_overview_en = response.xpath(
                "//p[@itemprop='description']|//p[@itemprop='description']/following-sibling::p").extract()
            item['degree_overview_en'] = remove_class(clear_lianxu_space(degree_overview_en))
            # print("item['degree_overview_en']: ", item['degree_overview_en'])

            overview1 = response.xpath(
                "//div[@class='tab-content active']/p|//div[@class='tab details-tab']|//span[@class='ct-accordion__title'][contains(text(),'Course Details')]/../..").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview1))
            # print("item['overview_en']: ", item['overview_en'])

            modules_url = response.xpath("//div[@class='tab structure-tab']//a[contains(text(),'click here')]/@href|"
                                         "//a[contains(text(),'Handbook')]/@href").extract()
            print(len(modules_url))
            if len(modules_url) > 0:
                item['modules_en'] = self.parse_modules(modules_url[0])
            print("item['modules_en']: ", item['modules_en'])

            entry_requirements = response.xpath(
                "//div[@class='tab entry-reqs-tab']|"
                "//div[@class='tab entry-reqs-tab']|//span[@class='ct-accordion__title'][contains(text(),'Entry Requirements')]/../..").extract()
            item['rntry_requirements_en'] = remove_class(clear_lianxu_space(entry_requirements))
            print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

            # //html//div[@class='tab entry-reqs-tab']//tr[1]
            IELTS = response.xpath(
                "//td[contains(text(),'IELTS Academic')]/following-sibling::td[1]//text()|"
                "//div[@class='tab entry-reqs-tab']|//span[@class='ct-accordion__title'][contains(text(),'Entry Requirements')]/../..//text()").extract()
            clear_space(IELTS)
            ielts_re = re.findall(r"International\sEnglish\sLanguage\sTesting\sSystem\s\(IELTS\sAcademic\).*?\sor", ''.join(IELTS))
            # print("ielts:re: ", ielts_re)
            if ielts_re:
                item['ielts_desc'] = ''.join(ielts_re)
                ieltsDict = get_ielts(item['ielts_desc'])
                item['ielts'] = ieltsDict.get("IELTS")
                item['ielts_l'] = ieltsDict.get("IELTS_L")
                item['ielts_s'] = ieltsDict.get("IELTS_S")
                item['ielts_r'] = ieltsDict.get("IELTS_R")
                item['ielts_w'] = ieltsDict.get("IELTS_W")
            print("item['ielts_desc']: ", item['ielts_desc'])

            TOEFL = response.xpath(
                "//td[contains(text(),'TOEFL Internet-based')]/following-sibling::td[1]//text()").extract()
            clear_space(TOEFL)

            TOEFL_re = re.findall(r"TOEFL\siBT.*?\sor|.{0,51}Internet\sBased\sTest.*?\sor", ''.join(IELTS))
            if TOEFL_re:
                item['toefl_desc'] = ''.join(TOEFL_re)
                toeflDict = get_toefl(item['toefl_desc'])
                item['toefl'] = toeflDict.get("TOEFL")
                item['toefl_l'] = toeflDict.get("TOEFL_L")
                item['toefl_s'] = toeflDict.get("TOEFL_S")
                item['toefl_r'] = toeflDict.get("TOEFL_R")
                item['toefl_w'] = toeflDict.get("TOEFL_W")
            print("item['toefl_desc']: ", item['toefl_desc'])


            print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))
            print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
                    item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

            # //div[@class='tab fees-tab']//div[@class='tab-content']//h4
            tuition_fee = response.xpath(
                "//div[@class='tab fees-tab']//div[@class='tab-content']//h4//text()").extract()
            clear_space(tuition_fee)
            # print("tuition_fee: ", tuition_fee)
            tuition_fee_re = re.findall(r"Estimated\sfirst\syear\sfee.*", ','.join(tuition_fee))
            tuition_fee_re1 = re.findall(r"[\d\s]+", ' '.join(tuition_fee_re))
            item['tuition_fee'] = ''.join(tuition_fee_re1).replace(" ", "").strip()
            # print("item['tuition_fee']: ", item['tuition_fee'])

            # //div[@class='tab apply-tab']
            apply_desc_en = response.xpath(
                "//div[@class='tab apply-tab']|"
                "//span[@class='ct-accordion__title'][contains(text(),'How to Apply')]/../..").extract()
            item['apply_desc_en'] = remove_class(clear_lianxu_space(apply_desc_en))
            # print("item['apply_desc_en']: ", item['apply_desc_en'])

            apply_documents_en = response.xpath(
                "//div[contains(text(),'What type of supporting documents do I have to pro')]/..").extract()
            item['apply_documents_en'] = remove_class(clear_lianxu_space(apply_documents_en))
            # print("item['apply_documents_en']: ", item['apply_documents_en'])


            if "/" not in item['degree_name']:
                if "Diploma" not in item['degree_name']:
                    # 判断是否支持国际招生
                    international = response.xpath("//a[@class='tabs-button active']/following-sibling::a[contains(text(), 'INTERNATIONAL')]//text()").extract()
                    print("internation == ", international)
                    # if international:
                    location = response.xpath(
                        "//span[contains(text(),'AVAILABILITY')]/following-sibling::p[1]//text()").extract()
                    clear_space(location)
                    print("location: ", location)
                    if location:
                        item['location'] = ''.join(location).strip().strip(",").strip()
                    print("item['location']: ", item['location'])

                    # 筛选含有多个专业的学位
                    major_list = response.xpath("//th[contains(text(),'Majors')]/../following-sibling::tr/td[1]//text()").extract()
                    print("major_list: ", major_list)
                    if major_list:
                        for major in major_list:
                            item['programme_en'] = major.strip()
                            yield item
                    else:
                        yield item

        except Exception as e:
            with open("scrapySchool_Australian_ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_modules(self, modules_a_url):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(modules_a_url, headers=headers_base)
        response = etree.HTML(data.text)

        modules_en = response.xpath(
            "//div[@id='structure_CoreCore']/div[last()]")
        modules_en_str = ""
        if len(modules_en) > 0:
            for m in modules_en:
                modules_en_str += etree.tostring(m, encoding='unicode', method='html')
                modules_en = remove_class(clear_lianxu_space([modules_en_str]))
        # print('modules_en: ', modules_en)
        return modules_en