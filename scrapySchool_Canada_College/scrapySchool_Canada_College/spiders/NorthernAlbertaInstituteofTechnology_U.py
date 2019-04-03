__author__ = 'yangyaxia'
__date__ = '2018/12/18 13:49'
import scrapy
import re
from scrapySchool_Canada_College.getItem import get_item
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from w3lib.html import remove_tags
from lxml import etree
import requests

class NorthernAlbertaInstituteofTechnology_USpider(scrapy.Spider):
    name = "NorthernAlbertaInstituteofTechnology_U"
    start_urls = ["http://www.nait.ca/programsandcourses.htm?searchType=program&PCDelivery=Day&PCCredential=Diploma",
                  "http://www.nait.ca/programsandcourses.htm?searchType=program&PCDelivery=Day&PCCredential=Degree"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        links = response.xpath('//tbody[@id="results"]/tr/td[@class="prog-name"]/a/@href').extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))

        for url in links:
            yield scrapy.Request(url, self.parse_data)


    def parse_data(self, response):
        item = get_item(ScrapyschoolCanadaCollegeItem)
        item['school_name'] = "Northern Alberta Institute of Technology"
        item['url'] = response.url
        print("===========================")
        print(response.url)

        # item['campus'] = ''
        item['location'] = '11762 - 106 Street Edmonton, Alberta, Canada, T5G 2R1'

        item['other'] = """问题描述： 1.没有专业代码和中国学生要求"""



        # item['require_chinese_en'] = ''

        # http://www.nait.ca/88953.htm
        item['apply_pre'] = "CAD$"
        item['apply_fee'] = '115'
        try:
            major_name_en = response.xpath("//section[@id='content']/h1//text()").extract()
            clear_space(major_name_en)
            item['major_name_en'] = ''.join(major_name_en).strip()
            print("item['major_name_en']: ", item['major_name_en'])

            # //span[@title='Campus']/following-sibling::span
            campus = response.xpath("//span[@title='Campus']/following-sibling::span//text()").extract()
            clear_space(campus)
            item['campus'] = ''.join(campus).strip()
            # print("item['campus']: ", item['campus'])

            degree_name = response.xpath("//span[@title='Credential']/following-sibling::span/text()").extract()
            clear_space(degree_name)
            item['degree_name'] = ''.join(degree_name).strip()
            # print("item['degree_name']: ", item['degree_name'])

            if item['degree_name'] == "Diploma":
                item['degree_level'] = 3
            if "degree" in item['degree_name'].lower():
                item['degree_level'] = 1
                item['degree_name'] = item['major_name_en']
            if "Post" in item['degree_name']:
                item['degree_level'] = 2
            print("item['degree_name']1: ", item['degree_name'])
            # print("item['degree_level']: ", item['degree_level'])

            if item['degree_level'] is not None:
                duration = response.xpath("//span[@title='Program Length']/following-sibling::span//text()").extract()
                clear_space(duration)
                # print("duration: ", duration)
                # 判断课程长度单位
                if "year" in ''.join(duration).lower():
                    item['duration_per'] = 1
                if "month" in ''.join(duration).lower():
                    item['duration_per'] = 3
                if "week" in ''.join(duration).lower():
                    item['duration_per'] = 4

                duration_re = re.findall(r"\d+\syear", ''.join(duration))
                # print("duration_re: ", duration_re)
                if len(duration_re) > 0:
                    item['duration'] = ''.join(duration_re[0]).replace("year", "").strip()
                # print("item['duration']: ", item['duration'])
                # print("item['duration_per']: ", item['duration_per'])


                start_date = response.xpath("//strong[contains(text(),'Start Date')]/../text()").extract()
                clear_space(start_date)
                # print("start_date: ", start_date)

                monthDict = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06",
                             "july": "07", "august": "08", "september": "09", "october": "10", "november": "11",
                             "december": "12",
                             "jan": "01", "feb": "02", "mar": "03", "apr": "04", "jun": "06",
                             "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12", "sept": "09", }
                start_date_str = ""
                deadline_str = ""
                if len(start_date) > 0:
                    # 将每个日期转成需要的日期格式
                    for sta in range(len(start_date)):
                        month_re = re.findall(r"[A-Za-z]+", start_date[sta])
                        day_re = re.findall(r"\d+,", start_date[sta])
                        year_re = re.findall(r"\d{4}", start_date[sta])
                        # print(monthDict.get(''.join(month_re).lower().strip()))
                        if monthDict.get(''.join(month_re).lower().strip()) is not None:
                            start_date[sta] = ''.join(year_re) + "-" + monthDict.get(''.join(month_re).lower().strip()) + "-" + ''.join(day_re)
                    # print("start_date: ", start_date)

                    for s in range(0, len(start_date), 2):
                        # print("s == ", s)
                        start_date_str += start_date[s]
                    item['start_date'] = start_date_str.strip().strip(",").strip()

                    for s in range(1, len(start_date), 2):
                        # print("sd == ", s)
                        deadline_str += start_date[s]
                    item['deadline'] = deadline_str.strip().strip(",").strip()

                # print("item['start_date']: ", item['start_date'])
                # print("item['deadline']: ", item['deadline'])

                overview = response.xpath(
                    "//div[@id='program-quick-facts']/preceding-sibling::*").extract()
                if len(overview) == 0:
                    overview = response.xpath("//div[@id='program-quick-facts']/../text()").extract()
                if len(overview) > 0:
                    item['overview_en'] = remove_class(clear_lianxu_space(overview))
                # print("item['overview_en']: ", item['overview_en'])

                career_en = response.xpath("//h3[@class='prepend-top']/../*[position()<last()]").extract()
                if len(career_en) > 0:
                    item['career_en'] = remove_class(clear_lianxu_space(career_en))
                # print("item['career_en']: ", item['career_en'])


                modules_url = response.xpath("//li/a[@id='sidenav-child'][contains(text(), 'Courses')]/@href").extract()
                # print("modules_url: ", modules_url)
                if len(modules_url) > 0:
                    item['modules_en'] = self.parse_modules(modules_url[0])
                # print("item['modules_en']: ", item['modules_en'])

                major_key = ["Academic Upgrading ",
"Alternative Energy Technology",
"Animal Health Technology",
"Applied Financial Services",
"Architectural Technology",
"Bachelor of Applied Business Administration - Accounting",
"Bachelor of Applied Business Administration - Finance",
"Bachelor of Applied Information Systems Technology",
"Bachelor of Business Administration",
"Bachelor of Technology - Construction Management",
"Bachelor of Technology in Technology Management",
"Baking and Pastry Arts",
"Biological Sciences Technology",
"Biomedical Engineering Technology",
"Biomedical Engineering Technology Co-op",
"Building Environmental Systems Technology",
"Business Administration - Accounting",
"Business Administration - Finance",
"Business Administration - Human Resources Management",
"Business Administration - Management",
"Business Administration - Marketing",
"Business Administration - Year One",
"Captioning and Court Reporting",
"Chemical Engineering Technology",
"Chemical Technology",
"Chemical Technology Co-op",
"Civil Engineering Technology",
"Civil Engineering Technology Co-op",
"CNC Machinist Technician",
"Computer Engineering Technology",
"Computer Engineering Technology Co-op",
"Computer Network Administrator",
"Construction Engineering Technology",
"Culinary Arts",
"Cytotechnology",
"Dental Assisting Technology",
"Dental Technology",
"Denturist Technology",
"Digital Media and IT",
"Digital Media and IT Co-op",
"Electrical Engineering Technology",
"Electronics Engineering Technology",
"Electronics Engineering Technology Co-op",
"Emergency Management",
"Emergency Management Certificate",
"Engineering Design and Drafting Technology",
"Forest Technology",
"Geological Technology",
"Geomatics Engineering Technology",
"Graphic Communications",
"Hospitality Management",
"HVAC-R Technician Certificate",
"Industrial Heavy Equipment Technology",
"Instrumentation Engineering Technology",
"Instrumentation Eng Technology Co-op",
"Interior Design Technology",
"Landscape Architectural Technology",
"Materials Engineering Technology",
"Mechanical Engineering Technology",
"Medical Laboratory Assistant",
"Medical Laboratory Technology",
"Medical Transcription",
"Millwork & Carpentry Certificate",
"Nanotechnology Systems",
"Network Engineering Technology",
"Network Engineering Technology Co-op",
"Occupational Health and Safety",
"Optical Sciences - Contact Lenses",
"Optical Sciences - Eyeglasses",
"Personal Fitness Trainer ",
"Petroleum Engineering Technology",
"Photographic Technology ",
"Power Engineering - Fourth Class",
"Power Engineering Technology ",
"Pre-Employment - Auto Body Repair ",
"Pre-Trades - Automotive Service Technician",
"Radio & Television - Radio",
"Respiratory Therapy",
"Retail Meatcutting Certificate",
"Veterinary Medical Assistant ",
"Water & Wastewater Technician ",
"Wireless Systems Engineering Technology", ]
                tuition_fee_value = ["7,814",
"8,653",
"7,814",
"7,814",
"8,051",
"8.051",
"8,051",
"8,653",
"8,051",
"8,993",
"8,653",
"8,051",
"8,051",
"8,993",
"8,993",
"8,993",
"8,051",
"8,051",
"8,051",
"8,051",
"8,051",
"8,051",
"7,814",
"8,653",
"8,653",
"8,653",
"8,993",
"8,993 ",
"8,653",
"8,051",
"8,051",
"8,051",
"8,993",
"8,051",
"8,993",
"8,653",
"8,051",
"8,653",
"8,051",
"8,051",
"8,993",
"8,051",
"8,051",
"8,993",
"8,993",
"8,653",
"8,051",
"8,051",
"8,993",
"7,814",
"7,814",
"8,653",
"8,653",
"8,993",
"8,993",
"7,814",
"8,051",
"8,653",
"8,653",
"8,051",
"8,653",
"8,653",
"7,814",
"8,653",
"8,653",
"8,653",
"8,653",
"8,051",
"8,051",
"7,814",
"8,993",
"7,814",
"8,993",
"8,993",
"8,051",
"8,653",
"7,814",
"8,993",
"8,051",
"7,814",
"8,993",
"8,653", ]
                tuition_fee_dict = {}
                for t in range(len(tuition_fee_value)):
                    tuition_fee_dict[major_key[t].strip()] = tuition_fee_value[t].strip()
                item['tuition_fee'] = tuition_fee_dict.get(item['major_name_en'])
                item['tuition_fee_per'] = "1"
                item['tuition_fee_pre'] = "CAD$"
                if "Biological Sciences Technology" in item['major_name_en']:
                    item['tuition_fee'] = "8,051"
                if "Radio & Television" in item['major_name_en']:
                    item['tuition_fee'] = "7,814"
                # print("item['tuition_fee']: ", item['tuition_fee'])
                # print("item['tuition_fee_per']: ", item['tuition_fee_per'])
                # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

                # http://www.nait.ca/56525.htm

                if item['major_name_en'] == "Bachelor of Applied Information Systems Technology" or item['major_name_en'] in ["Animal Health Technology", "Laboratory & X-ray Combined", "Dental Assisting Technology", "Dental Technology", "Denturist Technology", "Diagnostic Medical Sonography", "Emergency Medical Technology – Paramedic", "Magnetic Resonance", "Magnetic Resonance Imaging", "Medical Laboratory Assisting", "Medical Laboratory Technology", "Medical Radiologic Technology", "Veterinary Medical Assistant"]:
                    item['ielts_l'] = '6.0'
                    item['ielts_s'] = '6.5'
                    item['ielts_r'] = '6.0'
                    item['ielts_w'] = '6.0'
                    item['toefl_l'] = '20'
                    item['toefl_s'] = '23'
                    item['toefl_r'] = '20'
                    item['toefl_w'] = '20'
                elif "Business Administration" in item['major_name_en']:
                    item['ielts'] = '5.5'
                    item['ielts_l'] = '5.5'
                    item['ielts_s'] = '5.5'
                    item['ielts_r'] = '5.5'
                    item['ielts_w'] = '5.5'
                    item['toefl'] = '74'
                elif item['major_name_en'] == "Respiratory Therapy":
                    item['ielts_l'] = '8.0'
                    item['ielts_s'] = '7.0'
                    item['ielts_r'] = '7.0'
                    item['ielts_w'] = '7.0'
                    item['toefl_l'] = '28'
                    item['toefl_s'] = '23'
                    item['toefl_r'] = '24'
                    item['toefl_w'] = '27'
                else:
                    item['ielts'] = '6.5'
                    item['ielts_l'] = '5.0'
                    item['ielts_s'] = '5.5'
                    item['ielts_r'] = '5.0'
                    item['ielts_w'] = '5.0'
                    item['toefl'] = '80'
                    item['toefl_l'] = '20'
                    item['toefl_s'] = '20'
                    item['toefl_r'] = '20'
                    item['toefl_w'] = '20'

                entry_requirements_en_url = response.xpath("//li/a[@id='sidenav-child'][contains(text(), 'About the Program')]/@href").extract()
                # print("entry_requirements_en_url: ", entry_requirements_en_url)
                major_list = None
                if len(entry_requirements_en_url) > 0:
                    datadict = self.parse_entry_requirements_en(entry_requirements_en_url[0])
                    item['entry_requirements_en'] = datadict.get('entry_requirements_en')
                    major_list = datadict.get('major_list')
                # print("item['entry_requirements_en']: ", item['entry_requirements_en'])

                if major_list is not None:
                    if "Emphasis" in ' '.join(major_list):
                        for major in major_list:
                            item['major_name_en'] = major.replace("Emphasis", "").strip()
                            yield item
                    else:
                        yield item
                else:
                    yield item

                # yield item
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
            "//section[@id='content']")
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
            "//h3[contains(text(),'Entrance Requirements')]/..")
        entry_requirements_en_str = ""
        if len(entry_requirements_en) > 0:
            for m in entry_requirements_en:
                entry_requirements_en_str += etree.tostring(m, encoding='unicode', method='html')
        entry_requirements_en = remove_class(clear_lianxu_space([entry_requirements_en_str]))

        major_list = response.xpath("//li[@class='navigation-active navigation-children']/ul/li//text()")
        print("major_list: ", major_list)

        datadict = {}
        datadict['entry_requirements_en'] = entry_requirements_en
        datadict['major_list'] = major_list
        return datadict