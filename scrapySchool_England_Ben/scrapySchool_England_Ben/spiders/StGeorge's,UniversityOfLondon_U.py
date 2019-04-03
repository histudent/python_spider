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
        links = response.xpath("//div[@class='content-holder undergraduate-courses']/table/tbody/tr/td[1]//a/@href").extract()

        # 组合字典
        programme_dict = {}
        programme_list = response.xpath("//div[@class='content-holder undergraduate-courses']/table/tbody/tr/td[1]//a//text()").extract()
        clear_space(programme_list)

        for link in range(len(links)):
            url = "https://www.sgul.ac.uk" + links[link]
            programme_dict[url] = programme_list[link]

        print(len(links))
        links = list(set(links))
        print(len(links))
        # print(links)
        for link in links:
            # print(link)
            if "/study/undergraduate/undergraduate-courses/" in link:
                url = "https://www.sgul.ac.uk" + link
                # print(link)
                yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "St George's, University of London"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] =1
        item['location'] = "Cranmer Terrace, London SW17 0RE"
        print("===========================")
        print(response.url)
        item['major_type1'] = response.meta.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            programmeDegree_name = response.xpath("//div[@class='inner']/h1//text()").extract()
            programmeDegree_nameStr = ''.join(programmeDegree_name).strip()
            # print("programmeDegree_nameStr: ", programmeDegree_nameStr)

            if "Foundation" not in programmeDegree_nameStr:
                degree_name = re.findall(r"\(.*\)$|\w+\s\(.*\)$|\w+$", programmeDegree_nameStr)
                degree_name_str = ''.join(degree_name).strip()
                item['degree_name'] = degree_name_str.replace("(", "").replace(")", "").replace("Hons", "").strip()
                print("item['degree_name']: ", item['degree_name'])

                programme = programmeDegree_nameStr.replace(degree_name_str, "").strip()
                item['programme_en'] = programme
                print("item['programme_en']: ", item['programme_en'])

                ucascode = response.xpath(
                    "//*[contains(text(),'UCAS code')]//text()").extract()
                clear_space(ucascode)
                # print("ucascode: ", ucascode)
                if len(ucascode) > 0:
                    ucascode_re = re.findall(r"UCAS\scode\s\w{4}", ''.join(ucascode))
                    # print("ucascode_re: ", ucascode_re)
                    item['ucascode'] = ''.join(ucascode_re).replace("UCAS code", "").strip()
                # print("item['ucascode'] = ", item['ucascode'])

                other = response.xpath("//img[@alt='globe']/../..//text()").extract()
                if len(other) == 0:
                    other = response.xpath("//td[contains(text(),'Open to UK and EU students. Not currently open to ')]//text()").extract()
                item['other'] = clear_lianxu_space(other)
                # print("item['other'] = ", item['other'])

                # start_date = response.xpath("//dt[contains(text(), 'Start date')]/following-sibling::dd[1]//text()").extract()
                # clear_space(start_date)
                # # print("start_date: ", start_date)
                # item['start_date'] = getStartDate(''.join(start_date))
                # # print("item['start_date']: ", item['start_date'])

                duration = response.xpath("//img[@alt='Calendar']/../following-sibling::td//text()").extract()
                if len(duration) == 0:
                    duration = response.xpath("//img[@alt='Calendar']/../../following-sibling::td//text()").extract()
                clear_space(duration)
                # print("duration: ", ''.join(duration))

                duration_list = getIntDuration(''.join(duration))
                if len(duration_list) == 2:
                    item['duration'] = duration_list[0]
                    item['duration_per'] = duration_list[-1]
                # print("item['duration'] = ", item['duration'])
                # print("item['duration_per'] = ", item['duration_per'])

                # //p[contains(text(),'Non-UK/EU (International) application deadline')]
                deadline = response.xpath(
                    "//*[contains(text(),'Application deadline')]//text()|//*[contains(text(),'UCAS deadline')]//text()").extract()
                clear_space(deadline)
                # print("deadline: ", deadline)
                item['deadline'] = getStartDate(''.join(deadline).replace("Application deadline", "").replace("is", "").replace("UCAS deadline", "").replace(":", "").strip())
                if "2018" not in item['deadline'] and item['deadline'] != "" and "2019" not in item['deadline'] :
                    item['deadline'] = ''.join(deadline).replace("Application deadline", "").replace("is", "").replace("UCAS deadline", "").replace(":", "").strip()
                # print("item['deadline']: ", item['deadline'])

                # location = response.xpath("//*[contains(text(),'Study location:')]//text()").extract()
                # item['location'] = ''.join(location).replace("Study location:", "").strip()
                # print("item['location']: ", item['location'])

                tuition_fee = response.xpath("//h3[contains(text(),'International (Non-EU) Student Fees')]/following-sibling::table//td[contains(text(),'2019/20')]/following-sibling::td[1]//text()|"
                                             "//table//p[contains(text(),'2018 entry Non-EU')]//text()|"
                                             "//table[2]/tbody/tr[4]/td/p[contains(text(),'2018 Non-EU')]/following-sibling::*/*[1]//text()|"
                                             "//table//p[contains(text(),'2018 Non-EU')]/following-sibling::*[1]/*[1]//text()").extract()
                clear_space(tuition_fee)
                # print("tuition_fee: ", ''.join(tuition_fee))
                tuition_fee_re = re.findall(r"\d+,\d+", ''.join(tuition_fee))
                if len(tuition_fee_re) > 0:
                    item['tuition_fee'] = getTuition_fee(''.join(tuition_fee_re))
                # print("item['tuition_fee']: ", item['tuition_fee'])

                overview_en = response.xpath("//p[@class='first']|//table[1]/following-sibling::*[position()<last()-1]").extract()
                item['overview_en'] = remove_class(clear_lianxu_space(overview_en)).replace("<p><button>Make an enquiry</button></p>", "").strip()
                # print("item['overview_en']: ", item['overview_en'])

                entry_url = response.xpath("//a[contains(text(),'Entry')]/@href").extract()
                # print("entry_url: ", entry_url)
                if len(entry_url) != 0:
                    parse_entry_url = "https://www.sgul.ac.uk" + entry_url[0]
                    # print("parse_entry_url: ", parse_entry_url)
                    entry_dict = self.parse_rntry_requirements(parse_entry_url)
                    # print(entry_dict)
                    # item['rntry_requirements'] = entry_dict.get('rntry_requirements')

                    item['ielts_desc'] = entry_dict.get('ielts_desc')
                    item['alevel'] = entry_dict.get('alevel')
                    item['ib'] = entry_dict.get('ib')
                # print("item['ielts_desc']: ", item['ielts_desc'])
                # print("item['alevel']: ", item['alevel'])
                # print("item['ib']: ", item['ib'])

                ielts_list = re.findall(r"\d[\d\.]{0,2}", item['ielts_desc'])
                if len(ielts_list) == 1:
                    item['ielts'] = ielts_list[0]
                    item['ielts_l'] = ielts_list[0]
                    item['ielts_s'] = ielts_list[0]
                    item['ielts_r'] = ielts_list[0]
                    item['ielts_w'] = ielts_list[0]
                elif len(ielts_list) == 2:
                    item['ielts'] = ielts_list[0]
                    item['ielts_l'] = ielts_list[1]
                    item['ielts_s'] = ielts_list[1]
                    item['ielts_r'] = ielts_list[1]
                    item['ielts_w'] = ielts_list[1]
                elif len(ielts_list) == 5:
                    item['ielts'] = ielts_list[0]
                    item['ielts_l'] = ielts_list[1]
                    item['ielts_s'] = ielts_list[4]
                    item['ielts_r'] = ielts_list[2]
                    item['ielts_w'] = ielts_list[3]
                # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

                modules_url = response.xpath("//a[contains(text(),'Module')]/@href").extract()
                # print("modules_url: ", modules_url)
                if len(modules_url) != 0:
                    parse_modules_url = "https://www.sgul.ac.uk" + modules_url[0]
                    # print("parse_modules_url: ", parse_modules_url)
                    item['modules_en'] = remove_class(clear_lianxu_space(self.parse_modules(parse_modules_url))).strip()
                # print("item['modules_en']: ", item['modules_en'])

                assessment_en_url = response.xpath("//a[contains(text(),'Studying')]/@href").extract()
                # print("assessment_en_url: ", assessment_en_url)
                if len(assessment_en_url) != 0:
                    parse_assessment_en_url = "https://www.sgul.ac.uk" + assessment_en_url[0]
                    # print("parse_assessment_en_url: ", parse_assessment_en_url)
                    item['assessment_en'] = remove_class(clear_lianxu_space(self.parse_assessment_en(parse_assessment_en_url))).strip()
                # print("item['assessment_en']: ", item['assessment_en'])

                career_en_url = response.xpath("//a[contains(text(),'Career')]/@href").extract()
                # print("career_en_url: ", career_en_url)
                if len(career_en_url) != 0:
                    parse_career_en_url = "https://www.sgul.ac.uk" + career_en_url[0]
                    # print("parse_career_en_url: ", parse_career_en_url)
                    item['career_en'] = remove_class(clear_lianxu_space(self.parse_career_en(parse_career_en_url))).replace("<p><img></p>", "").strip()
                # print("item['career_en']: ", item['career_en'])

                apply_proces_en_url = response.xpath("//a[contains(text(),'Apply')]/@href|//a[contains(text(),'Application and interview')]/@href").extract()
                # print("apply_proces_en_url: ", apply_proces_en_url)
                if len(apply_proces_en_url) != 0:
                    parse_apply_proces_en_url = "https://www.sgul.ac.uk" + apply_proces_en_url[0]
                    # print("parse_apply_proces_en_url: ", parse_apply_proces_en_url)
                    item['apply_proces_en'] = remove_class(clear_lianxu_space(self.parse_apply_proces_en(parse_apply_proces_en_url))).replace("<p><img></p>", "").strip()
                # print("item['apply_proces_en']: ", item['apply_proces_en'])

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
            "//*[contains(text(),'A Level')]/../../following-sibling::*//*[contains(text(), 'Grades')]/following-sibling::td//text()|"
            "//*[contains(text(),'A Level')]/../following-sibling::*//*[contains(text(), 'Grades')]/following-sibling::td//text()")
        alevel_str = ""
        if len(alevel) > 0:
            alevel_str = alevel[-1]
        # print("ielts_desc: ", ielts_desc)

        ib = response.xpath(
            "//*[contains(text(),'International Baccalaureate')]/../../following-sibling::*//*[contains(text(), 'Grades')]/following-sibling::td//text()|"
            "//*[contains(text(),'International Baccalaureate')]/../following-sibling::*//*[contains(text(), 'core')]/following-sibling::td//text()")
        ib_str = ""
        # print(ib)
        # if len(ib) > 0:
        ib_str = ' '.join(ib).strip()
        # print("ielts_desc: ", ielts_desc)
        entry_dict['rntry_requirements'] = rntry_requirements_str
        entry_dict['ielts_desc'] = ielts_desc_str
        entry_dict['alevel'] = alevel_str
        entry_dict['ib'] = ib_str
        return entry_dict

    def parse_modules(self, parse_modules_url):
        data = requests.get(parse_modules_url, headers=self.headers)
        response = etree.HTML(data.text)
        modules = response.xpath("//div[@class='content-holder modules']/*[position()>2]")
        # print("modules: ", modules)
        modules_en = []
        if len(modules) != 0:
            for m in modules:
                modules_en.append(etree.tostring(m, encoding='unicode', method='html'))
        return modules_en

    def parse_assessment_en(self, parse_assessment_en_url):
        data = requests.get(parse_assessment_en_url, headers=self.headers)
        response = etree.HTML(data.text)
        assessment = response.xpath("//div[@class='content-holder studying-master']/*[position()>3]|//div[@class='content-holder studying']/*[position()>3]")
        assessment_en = []
        if len(assessment) != 0:
            for m in assessment:
                assessment_en.append(etree.tostring(m, encoding='unicode', method='html'))
        return assessment_en

    def parse_career_en(self, parse_career_en_url):
        data = requests.get(parse_career_en_url, headers=self.headers)
        response = etree.HTML(data.text)
        career = response.xpath(
            "//div[@class='content-holder careers-master']/*[position()>3]|//div[@class='content-holder careers']/*[position()>3]")
        career_en = []
        if len(career) != 0:
            for m in career:
                career_en.append(etree.tostring(m, encoding='unicode', method='html'))
        return career_en

    def parse_apply_proces_en(self, parse_apply_proces_en_url):
        data = requests.get(parse_apply_proces_en_url, headers=self.headers)
        response = etree.HTML(data.text)
        apply_proces = response.xpath("//div[@class='content-holder apply-master']/*[position()>3]|//div[@class='content-holder application-and-interview']/*[position()>3]")
        apply_proces_en = []
        if len(apply_proces) != 0:
            for m in apply_proces:
                apply_proces_en.append(etree.tostring(m, encoding='unicode', method='html'))
        return apply_proces_en