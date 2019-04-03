__author__ = 'yangyaxia'
__date__ = '2018/12/19 11:39'
import scrapy
import re
from scrapySchool_Canada_College.getItem import get_item
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from w3lib.html import remove_tags
from lxml import etree
import requests

class RedRiverCollege_USpider(scrapy.Spider):
    name = "RedRiverCollege_U"
    # 五个校区的专业列表链接
#     start_urls = ["https://me.rrc.mb.ca/Catalogue/Programs.aspx?RegionCode=GC",
# "https://me.rrc.mb.ca/Catalogue/Programs.aspx?RegionCode=PFR",
# "https://me.rrc.mb.ca/Catalogue/Programs.aspx?RegionCode=PC",
# "https://me.rrc.mb.ca/Catalogue/Programs.aspx?RegionCode=SC",
# "https://me.rrc.mb.ca/Catalogue/Programs.aspx?RegionCode=WC", ]
    start_urls = ["https://me.rrc.mb.ca/Catalogue/Programs.aspx?DeliveryCode=F"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        # 获取每个校区full time的专业
        links = response.xpath("//table//td[@align='left'][1]/a/@href").extract()
        # print("=========", response.url)
        print(len(links))
        links = list(set(links))
        print(len(links))

        # 落抓的专业
#         links = ["https://me.rrc.mb.ca/Catalogue/ProgramInfo.aspx?ProgCode=TECCF-DP&RegionCode=WPG",
# "https://me.rrc.mb.ca/Catalogue/ProgramInfo.aspx?ProgCode=SCILF-DP&RegionCode=WPG",
# "https://me.rrc.mb.ca/Catalogue/ProgramInfo.aspx?ProgCode=ADVCF-DP&RegionCode=WPG",
# "https://me.rrc.mb.ca/Catalogue/ProgramInfo.aspx?ProgCode=MUNEF-DP&RegionCode=WPG",
# "https://me.rrc.mb.ca/Catalogue/ProgramInfo.aspx?ProgCode=INBSF-AD&RegionCode=WPG",
# "https://me.rrc.mb.ca/Catalogue/ProgramInfo.aspx?ProgCode=INSCF-DP&RegionCode=WPG",
# "https://me.rrc.mb.ca/Catalogue/ProgramInfo.aspx?ProgCode=INDEF-DP&RegionCode=WPG",
# "https://me.rrc.mb.ca/Catalogue/ProgramInfo.aspx?ProgCode=INDAF-DP&RegionCode=WPG",
# "https://me.rrc.mb.ca/Catalogue/ProgramInfo.aspx?ProgCode=GEOTF-DP&RegionCode=WPG",
# "https://me.rrc.mb.ca/Catalogue/ProgramInfo.aspx?ProgCode=CONMF-DG&RegionCode=WPG", ]
        links = ["https://me.rrc.mb.ca/Catalogue/ProgramInfo.aspx?ProgCode=INDEF-DP&RegionCode=WPG",
"https://me.rrc.mb.ca/Catalogue/ProgramInfo.aspx?ProgCode=INSCF-DP&RegionCode=WPG",
"https://me.rrc.mb.ca/Catalogue/ProgramInfo.aspx?ProgCode=MUNEF-DP&RegionCode=WPG",
# "https://me.rrc.mb.ca/Catalogue/ProgramInfo.aspx?ProgCode=SCILF-DP&RegionCode=WPG",
"https://me.rrc.mb.ca/Catalogue/ProgramInfo.aspx?ProgCode=TECCF-DP&RegionCode=WPG",
"https://me.rrc.mb.ca/Catalogue/ProgramInfo.aspx?ProgCode=GEOTF-DP&RegionCode=WPG", ]
        for link in links:
            # url = "https://me.rrc.mb.ca/Catalogue/" + link
            url = link
            yield scrapy.Request(url, self.parse_data)


    def parse_data(self, response):
        item = get_item(ScrapyschoolCanadaCollegeItem)
        item['school_name'] = "Red River College"
        item['url'] = response.url
        print("===========================")
        print(response.url)

        # item['campus'] = ''
        # item['location'] = '11762 - 106 Street Edmonton, Alberta, Canada, T5G 2R1'

        item['other'] = """问题描述： 1.就业空的是页面没有的"""



        # item['require_chinese_en'] = ''

        # https://www.rrc.ca/future-students/fees/#application
        item['apply_pre'] = "CAD$"
        item['apply_fee'] = '120'
        try:
            major_name_en = response.xpath("//span[@id='_ctl0_lblProgramName']//text()").extract()
            clear_space(major_name_en)
            item['major_name_en'] = ''.join(major_name_en).strip()
            print("item['major_name_en']: ", item['major_name_en'])

            degree_name = response.xpath("//span[@id='_ctl0_ContentPlaceHolder1_lblDescriptionText']//ul/li[1]//text()").extract()
            clear_space(degree_name)
            print("degree_name: ", degree_name)
            duration_str = ""
            if len(degree_name) > 0:
                if "advanced diploma" in degree_name[0].lower():
                    item['degree_name'] = "advanced diploma"
                    item['degree_level'] = 3
                elif "diploma" in degree_name[0].lower():
                    item['degree_name'] = "diploma"
                    item['degree_level'] = 3
                elif "degree" in degree_name[0].lower():
                    item['degree_name'] = "Bachelor degree"
                    item['degree_level'] = 1
                duration_str = degree_name[0]

                print("item['degree_name']: ", item['degree_name'])
                print("item['degree_level']: ", item['degree_level'])
                if item['degree_level'] is not None:
                    duration_re = re.findall(r"\w+\-year|[\w\W\-]+month", duration_str)
                    print("duration_re: ", duration_re)
                    # 判断课程长度单位
                    if len(duration_re) > 0:
                        if "year" in ''.join(duration_re[0]).lower():
                            item['duration_per'] = 1
                        if "month" in ''.join(duration_re[0]).lower():
                            item['duration_per'] = 3
                        if "week" in ''.join(duration_re[0]).lower():
                            item['duration_per'] = 4

                    d_dict = {"One": "1",
                              "Two": "2",
                              "Three": "3",
                              "Four": "4",
                              "Five": "5",
                              "Six": "6",
                              "Seven": "7",
                              "Eight": "8",
                              "Nine": "9",
                              "Ten": "10",
                              "one": "1",
                              "two": "2",
                              "three": "3",
                              "four": "4",
                              "five": "5",
                              "six": "6",
                              "seven": "7",
                              "eight": "8",
                              "nine": "9",
                              "ten": "10",
                              }
                    if len(duration_re) > 0:
                        item['duration'] = d_dict.get(''.join(duration_re[0]).replace("year", "").replace("-", "").strip())
                        if item['duration'] is None:
                            item['duration'] =duration_re[0].replace("month", "").replace("-", "").strip()
                            if item['duration'] is None:
                                item['duration'] = duration_re[0].strip()
                    print("item['duration']: ", item['duration'])
                    print("item['duration_per']: ", item['duration_per'])

                    overview = response.xpath(
                        "//b[contains(text(),'Description')]/..|//strong[contains(text(),'Description')]/..|"
                        "//strong[contains(text(),'Description')]/../following-sibling::*").extract()
                    if len(overview) == 0:
                        overview = response.xpath("//u[contains(text(),'Description')]/../..|//u[contains(text(),'Description')]/../../following-sibling::*|"
                                                  "//b//span[@lang='EN-US']/../..|//b//span[@lang='EN-US']/../../following-sibling::*|"
                                                  "//span[contains(text(),'Description')]/../..|//span[contains(text(),'Description')]/../../following-sibling::*|"
                                                  "//span[@id='_ctl0_ContentPlaceHolder1_lblDescriptionText']//p//strong//em/../..|//span[@id='_ctl0_ContentPlaceHolder1_lblDescriptionText']//p//strong//em/../../following-sibling::*").extract()
                    if len(overview) > 0:
                        item['overview_en'] = remove_class(clear_lianxu_space(overview))
                    # print("item['overview_en']: ", item['overview_en'])

                    entry_requirements_en_url = response.xpath(
                        "//a[@id='_ctl0_rProgramMenu__ctl1_MenuLink']/@href").extract()
                    # print("entry_requirements_en_url: ", entry_requirements_en_url)
                    if len(entry_requirements_en_url) > 0:
                        item['entry_requirements_en'] = self.parse_entry_requirements_en("https://me.rrc.mb.ca/Catalogue/"+entry_requirements_en_url[0])
                        # if "'" in item['entry_requirements_en']:
                        #     item['entry_requirements_en'] = item['entry_requirements_en'].strip("'")
                        ielts_list = self.parse_ielts("https://me.rrc.mb.ca/Catalogue/"+entry_requirements_en_url[0])
                        if len(ielts_list) > 0:
                            if "," in ielts_list[1]:
                                ielts_split = ielts_list[1].split(',')
                                for ie in ielts_split:
                                    if "Listening" in ie:
                                        item['ielts_l'] = ie.replace("Listening", "").strip()
                                    if "Speaking" in ie:
                                        item['ielts_s'] = ie.replace("Speaking", "").strip()
                                    if "Reading" in ie:
                                        item['ielts_r'] = ie.replace("Reading", "").strip()
                                    if "Writing" in ie:
                                        item['ielts_w'] = ie.replace("Writing", "").strip()
                    print("item['ielts_l']: ", item['ielts_l'])
                    print("item['ielts_s']: ", item['ielts_s'])
                    print("item['ielts_r']: ", item['ielts_r'])
                    print("item['ielts_w']: ", item['ielts_w'])
                    print("item['entry_requirements_en']: ", item['entry_requirements_en'])

                    modules_url = response.xpath(
                        "//a[contains(text(), 'Courses and Descriptions')]/@href").extract()
                    # print("modules_url: ", modules_url)
                    if len(modules_url) > 0:
                        item['modules_en'] = self.parse_modules("https://me.rrc.mb.ca/Catalogue/" + modules_url[0])
                    # print("item['modules_en']: ", item['modules_en'])

                    career_url = response.xpath(
                        "//a[contains(text(), 'Employment Potential')]/@href").extract()
                    # print("career_url: ", career_url)
                    if len(career_url) > 0:
                        item['career_en'] = self.parse_entry_requirements_en("https://me.rrc.mb.ca/Catalogue/" + career_url[0])
                    # print("item['career_en']: ", item['career_en'])

                    location_date_tuition_url = response.xpath(
                        "//a[contains(text(), 'Locations, Dates and Fees')]/@href").extract()
                    print("location_date_tuition_url: ", location_date_tuition_url)


                    item['tuition_fee_per'] = "1"
                    item['tuition_fee_pre'] = "CAD$"
                    if len(location_date_tuition_url) > 0:
                        print("--------0-------")
                        location_date_tuition_dict = self.parse_location_date_tuition("https://me.rrc.mb.ca/Catalogue/" + location_date_tuition_url[0])
                        item['tuition_fee'] = location_date_tuition_dict.get('tuition_fee')
                        campus_list = location_date_tuition_dict.get('campus_list')
                        start_date_list = location_date_tuition_dict.get('start_date_list')
                        monthDict = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06",
                                     "july": "07", "august": "08", "september": "09", "october": "10", "november": "11",
                                     "december": "12",
                                     "jan": "01", "feb": "02", "mar": "03", "apr": "04", "jun": "06",
                                     "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12", "sept": "09", }
                        if len(start_date_list) > 0:
                            # 将每个日期转成需要的日期格式
                            for sta in range(len(start_date_list)):
                                month_re = re.findall(r"[A-Za-z]+", start_date_list[sta])
                                day_re = re.findall(r"\d+,", start_date_list[sta])
                                year_re = re.findall(r"\d{4}", start_date_list[sta])
                                # print(monthDict.get(''.join(month_re).lower().strip()))
                                if monthDict.get(''.join(month_re).lower().strip()) is not None:
                                    start_date_list[sta] = ''.join(year_re) + "-" + monthDict.get(''.join(month_re).lower().strip()) + "-" + ''.join(day_re)
                        print("start_date_list1: ", start_date_list)
                        if len(start_date_list) == len(campus_list):
                            print("--------1-------")
                            if len(campus_list) > 0:
                                for c in range(len(campus_list)):
                                    item['campus'] = campus_list[c]
                                    item['start_date'] = start_date_list[c].strip().strip(',').strip()
                                    yield item
                            else:
                                yield item
                        else:
                            print("--------2-------")
                            item['start_date'] = ''.join(start_date_list).strip().strip(',').strip()
                            yield item
                    else:
                        print("--------3-------")
                        yield item
        except Exception as e:
                with open("scrapySchool_Canada_College/error/" + item['school_name'] + ".txt", 'a', encoding="utf-8") as f:
                    f.write(str(e) + "\n" + response.url + "\n========================\n")
                print("异常：", str(e))
                print("报错url：", response.url)

    def parse_modules(self, modules_url):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(modules_url, headers=headers_base)
        response = etree.HTML(data.text)

        modules_en = response.xpath(
            "//table[@class='itsCourseListTable']")
        modules_en_str = ""
        if len(modules_en) > 0:
            for m in modules_en:
                modules_en_str += etree.tostring(m, encoding='unicode', method='html')
        modules_en = remove_class(clear_lianxu_space([modules_en_str]))

        return modules_en

    def parse_entry_requirements_en(self, entry_requirements_en_url):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(entry_requirements_en_url, headers=headers_base)
        response = etree.HTML(data.text)

        entry_requirements_en = response.xpath(
            "//table[@width='100%']")
        entry_requirements_en_str = ""
        if len(entry_requirements_en) > 0:
            for m in entry_requirements_en:
                entry_requirements_en_str += etree.tostring(m, encoding='unicode', method='html')
        entry_requirements_en = remove_class(clear_lianxu_space([entry_requirements_en_str]))
        # print("entry_requirements_en: ", entry_requirements_en)
        #
        # ielts = response.xpath("//*[contains(text(), 'International English Language Testing System (IELTS - Academic):')]//text()")
        # clear_space(ielts)
        # print("ielts: ", ielts)
        #
        # entry_data_dict = {}
        # entry_data_dict['entry_requirements_en'] = entry_requirements_en
        # entry_data_dict['ielts_list'] = ielts
        return entry_requirements_en

    def parse_ielts(self, entry_requirements_en_url):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(entry_requirements_en_url, headers=headers_base)
        response = etree.HTML(data.text)

        ielts_list = response.xpath("//*[contains(text(), 'International English Language Testing System (IELTS - Academic):')]//text()")
        clear_space(ielts_list)
        print("ielts_list: ", ielts_list)

        return ielts_list

    def parse_location_date_tuition(self, location_date_tuition_url):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(location_date_tuition_url, headers=headers_base)
        response = etree.HTML(data.text)

        tuition_fee = response.xpath("//font[contains(text(),'Program/Student Fees (International)')]/../../following-sibling::tr[1]/td[2]//text()")
        clear_space(tuition_fee)
        print("tuition_fee: ", tuition_fee)

        tuition_fee_str = ""
        if len(tuition_fee) > 0:
            tuition_fee_str = ''.join(tuition_fee[0]).replace("$", "").strip()
        print("tuition_fee_str: ", tuition_fee_str)

        campus_list = response.xpath(
            "//tr[@class='itsProgramDateHeading']/following-sibling::tr/td[1]//text()")
        clear_space(campus_list)
        print("campus_list: ", campus_list)


        start_date_list = response.xpath(
            "//tr[@class='itsProgramDateHeading']/following-sibling::tr/td[2]//text()")
        clear_space(start_date_list)
        print("start_date_list: ", start_date_list)

        data_dict = {}
        data_dict['tuition_fee'] = tuition_fee_str
        data_dict['campus_list'] = campus_list
        data_dict['start_date_list'] = start_date_list
        return data_dict