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
import json
import requests
from w3lib.html import remove_tags
from lxml import etree

class UniversityOfBradford_USpider(scrapy.Spider):
    name = "UniversityOfBradford_U"
    start_urls = ["https://www.bradford.ac.uk/courses/ug/"]

    def parse(self, response):
        links = response.xpath("//div[@id='results_initial']//div[contains(@class,'result ug')]//a/@href").extract()

        # 组合字典
        programme_dict = {}
        programme_list = response.xpath("//div[@id='results_initial']//div[contains(@class,'result ug')]//a//text()").extract()
        clear_space(programme_list)

        for link in range(len(links)):
            url = "https://www.bradford.ac.uk" + links[link].replace("-3-years", "").replace("-4-years", "").replace("-5-years", "").strip()
            programme_dict[url] = programme_list[link]

        print(len(links))
        links = list(set(links))
        print(len(links))
        # print(programme_dict)
        # links = ["https://www.bradford.ac.uk/courses/ug/computer-science-bsc/",
        #          "https://www.bradford.ac.uk/courses/ug/computer-science-for-games-bsc/",
        #          "https://www.bradford.ac.uk/courses/ug/law-social-justice-llb/",
        #          "https://www.bradford.ac.uk/courses/ug/psychology-bsc/", ]
        for link in links:
            url = "https://www.bradford.ac.uk" + link
            # print(url)
            # url = link
            yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Bradford"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        # if "ug/" in response.url:
        print("===========================")
        print(response.url)
        # 重定向匹配不了
        item['major_type1'] = response.meta.get(response.url)
        # print("item['major_type1']: ", item['major_type1'])
        item['location'] = 'Bradford West Yorkshire BD7 1DP UK'
        # print("item['location']: ", item['location'])
        try:
            key_url = response.url.split("/")[-2].strip()

            programme = response.xpath("//div[@id='course-key-info']//div[@class='col-xs-12']/h1//text()").extract()
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en']: ", item['programme_en'])

            degree_type = response.xpath("//p[@id='cAward']//text()").extract()
            item['degree_name'] = ''.join(degree_type).replace("(Hons)", "").strip()
            print("item['degree_name']: ", item['degree_name'])

            mode = response.xpath("//option[@value='fulltime']//text()|//span[@id='cAttendance']//text()|//span[@id='displayYear']//text()").extract()
            clear_space(mode)
            # item['teach_time'] = getTeachTime(''.join(mode))
            print("mode: ", mode)

            if "full" in ''.join(mode).lower() and "Foundation" not in item['programme_en']:
                overview_en = response.xpath("//div[@id='overviewStripe']").extract()
                item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
                # print("item['overview_en']: ", item['overview_en'])

                modules = response.xpath("//div[@id='course-curriculum']").extract()
                item['modules_en'] = remove_class(clear_lianxu_space(modules))
                # print("item['modules_en']: ", item['modules_en'])

                assessment_en = response.xpath("//div[@class='row stripe background--green']").extract()
                item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
                # print("item['assessment_en']: ", item['assessment_en'])

                career_en = response.xpath("//div[@id='nav-course-career']").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career_en)).replace("<div></div>", "").strip()
                # print("item['career_en']: ", item['career_en'])

                item['apply_proces_en'] = 'https://www.bradford.ac.uk/undergraduate/apply/'
                item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<div class="entryReq __undergraduate"><h3>Undergraduate</h3><table><tbody><tr><th rowspan="2">Qualification</th><th colspan="3">UCAS tariff points</th></tr><tr><th>136+</th><th>120 - 135</th><th>96 - 119</th></tr><tr><td>Senior Secondary School Graduation Certificate / 高中毕业证书</td><td colspan="3">Foundation Programme required</td></tr></tbody></table></div> """]))
                # print("item['require_chinese_en']: ", item['require_chinese_en'])

                department_dict = {"Animation": "Faculty of Engineering and Informatics",
"Biomedical Engineering": "Faculty of Engineering and Informatics",
"Business Computing": "Faculty of Engineering and Informatics",
"Chemical Engineering": "Faculty of Engineering and Informatics",
"Civil and Structural Engineering": "Faculty of Engineering and Informatics",
"Clinical Technology": "Faculty of Engineering and Informatics",
"Computer Science": "Faculty of Engineering and Informatics",
"Computer Science for Cyber Security": "Faculty of Engineering and Informatics",
"Computer Science for Games": "Faculty of Engineering and Informatics",
"Film and Television Production": "Faculty of Engineering and Informatics",
"Film and Visual Effects Technology": "Faculty of Engineering and Informatics",
"Game Design and Development": "Faculty of Engineering and Informatics",
"Graphics for Games": "Faculty of Engineering and Informatics",
"Mechanical Engineering": "Faculty of Engineering and Informatics",
"Software Engineering": "Faculty of Engineering and Informatics",
"Virtual and Augmented Reality": "Faculty of Engineering and Informatics",
"MPhysiotherapy - Sport and Exercise Medicine MPhysio": "Faculty of Health Studies",
"Nursing (Adult)": "Faculty of Health Studies",
"Nursing (Adult) – Harrogate and District NHS Trust": "Faculty of Health Studies",
"Nursing (Mental Health)": "Faculty of Health Studies",
"Occupational Therapy": "Faculty of Health Studies",
"Physiotherapy": "Faculty of Health Studies",
"Public Health and Community Wellbeing": "Faculty of Health Studies",
"Archaeology": "Faculty of Life Sciences",
"Biomedical Science": "Faculty of Life Sciences",
"Certificate of International Foundation Studies": "Faculty of Life Sciences",
"Chemistry": "Faculty of Life Sciences",
"Chemistry - Analytical Chemistry": "Faculty of Life Sciences",
"Chemistry - Industrial Experience": "Faculty of Life Sciences",
"Chemistry - Materials Chemistry": "Faculty of Life Sciences",
"Chemistry - Mathematical and Computational Chemistry": "Faculty of Life Sciences",
"Chemistry - Medicinal Chemistry": "Faculty of Life Sciences",
"Clinical Sciences": "Faculty of Life Sciences",
"Forensic and Medical Sciences": "Faculty of Life Sciences",
"Forensic Archaeology and Anthropology": "Faculty of Life Sciences",
"Forensic Science": "Faculty of Life Sciences",
"Foundation in Clinical Sciences/Medicine": "Faculty of Life Sciences",
"Optometry": "Faculty of Life Sciences",
"Pharmacy": "Faculty of Life Sciences",
"Pharmacy 5 years (including pre-registration training)": "Faculty of Life Sciences",
"Accounting and Finance": "Faculty of Management, Law & Social Sciences",
"Business and Management": "Faculty of Management, Law & Social Sciences",
"Business Studies and Law": "Faculty of Management, Law & Social Sciences",
"Economics": "Faculty of Management, Law & Social Sciences",
"Finance and Economics": "Faculty of Management, Law & Social Sciences",
"Human Resource Management": "Faculty of Management, Law & Social Sciences",
"International Business and Management": "Faculty of Management, Law & Social Sciences",
"Law": "Faculty of Management, Law & Social Sciences",
"Law (Commercial Law)": "Faculty of Management, Law & Social Sciences",
"Law (Criminal Law)": "Faculty of Management, Law & Social Sciences",
"Law (Social Justice)": "Faculty of Management, Law & Social Sciences",
"Law with Business and Management": "Faculty of Management, Law & Social Sciences",
"Marketing": "Faculty of Management, Law & Social Sciences",
"Criminology and Criminal Behaviour": "Faculty of Management, Law & Social Sciences",
"Psychology": "Faculty of Management, Law & Social Sciences",
"Psychology with Counselling": "Faculty of Management, Law & Social Sciences",
"Social Work": "Faculty of Management, Law & Social Sciences",
"Sociology": "Faculty of Management, Law & Social Sciences",
"Working with Children, Young People and Families": "Faculty of Management, Law & Social Sciences", }
                item['department'] = department_dict.get(item['programme_en'].strip())
                print("item['department']: ", item['department'])

                # 将Full-time的情况获取duration、ucascode、alevel、ib、tuition_fee字段
                # # 1.duration
                # # https://www.bradford.ac.uk/courses/ug/api.php?uri=/courses/ug/biomedical-engineering-beng/&duration=duration&level=ug&year=y2019&attendance=fulltime
                # duration_url = "https://www.bradford.ac.uk/courses/ug/api.php?uri=/courses/ug/" + key_url + "/&duration=duration&level=ug&year=y2019&attendance=fulltime"
                # # print("duration_url: ", duration_url)
                # duration = json.loads(requests.get(duration_url).text).get("data")
                # # print("duration: ", duration)
                # if duration != None:
                #     duration_list = getIntDuration(''.join(duration))
                #     if len(duration_list) == 2:
                #         item['duration'] = duration_list[0]
                #         item['duration_per'] = duration_list[-1]
                # # print("item['duration'] = ", item['duration'])
                # # print("item['duration_per'] = ", item['duration_per'])
                #
                # # 2.ucascode
                # # https://www.bradford.ac.uk/courses/ug/api.php?uri=/courses/ug/biomedical-engineering-beng/&ucasCode=ucasCode&level=ug&year=y2019&attendance=fulltime
                # ucascode_url = "https://www.bradford.ac.uk/courses/ug/api.php?uri=/courses/ug/" + key_url + "/&ucasCode=ucasCode&level=ug&year=y2019&attendance=fulltime"
                # # print("ucascode_url: ", ucascode_url)
                # ucascode = json.loads(requests.get(ucascode_url).text).get("data")
                # # print("ucascode: ", ucascode)
                # if ucascode is not None:
                #     item['ucascode'] = ''.join(ucascode).strip()
                # # print("item['ucascode']: ", item['ucascode'])
                #
                #
                # # 3.alevel、ib
                # # https://www.bradford.ac.uk/courses/ug/api.php?uri=/courses/ug/biomedical-engineering-beng/&entry=entry&level=ug&year=y2019&attendance=filltime
                # entry_url = "https://www.bradford.ac.uk/courses/ug/api.php?uri=/courses/ug/" + key_url + "/&entry=entry&level=ug&year=y2019&attendance=fulltime"
                # # print("entry_url: ", entry_url)
                # entry = json.loads(requests.get(entry_url).text).get("data")
                # # print("entry: ", entry)
                # if entry is not None:
                #     entry_response = etree.HTML(entry)
                #     alevel = entry_response.xpath("//strong[contains(text(),'A levels')]/../../following-sibling::div//text()")
                #     # print("alevel: ", alevel)
                #     item['alevel'] = clear_lianxu_space(alevel)
                #
                #     ib = entry_response.xpath(
                #         "//strong[contains(text(),'International Baccalaureate requirements')]/../../following-sibling::div//text()")
                #     # print("ib: ", ib)
                #     item['ib'] = clear_lianxu_space(ib)
                #
                #     ielts_desc = entry_response.xpath(
                #         "//strong[contains(text(),'English language requirements')]/../../following-sibling::div/p[1]//text()")
                #     item['ielts_desc'] = clear_lianxu_space(ielts_desc)
                #     print("item['ielts_desc']: ", item['ielts_desc'])
                #
                #     ielts_dict = get_ielts(item['ielts_desc'])
                #     item['ielts'] = ielts_dict.get('IELTS')
                #     item['ielts_l'] = ielts_dict.get('IELTS_L')
                #     item['ielts_s'] = ielts_dict.get('IELTS_S')
                #     item['ielts_r'] = ielts_dict.get('IELTS_R')
                #     item['ielts_w'] = ielts_dict.get('IELTS_W')
                #     print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))
                #
                # # 4.tuition_fee
                # # https://www.bradford.ac.uk/courses/ug/api.php?uri=/courses/ug/biomedical-engineering-beng/&fees=fees&level=ug&year=y2019&attendance=fulltime
                # tuition_fee_url = "https://www.bradford.ac.uk/courses/ug/api.php?uri=/courses/ug/" + key_url + "/&fees=fees&level=ug&year=y2019&attendance=fulltime"
                # # print("tuition_fee_url: ", tuition_fee_url)
                # tuition_fee = json.loads(requests.get(tuition_fee_url).text).get("data")
                # # print("tuition_fee: ", tuition_fee)
                # if tuition_fee is not None:
                #     tuition_fee_response = etree.HTML(tuition_fee)
                #     tuition_fee_str = tuition_fee_response.xpath("//div[@id='tuitionFees']//p[contains(text(),'International:')]//text()")
                #     # print("tuition_fee_str: ", tuition_fee_str)
                #     tuition_fee_re = re.findall(r"£\d+,\d+", ''.join(tuition_fee_str))
                #
                #     if len(tuition_fee_re) > 0:
                #         item['tuition_fee'] = getTuition_fee(''.join(tuition_fee_re))
                # # print("item['tuition_fee']: ", item['tuition_fee'])


                is_full_sand = response.xpath("//select[@id='variant-attendance-mode']/option//text()").extract()
                clear_space(is_full_sand)
                item['other'] = ','.join(is_full_sand).strip().strip(',').strip()
                print("is_full_sand: ", is_full_sand)

                if len(is_full_sand) > 0:
                    for f in is_full_sand:
                        if f == "Full-time":
                            mode = 'fulltime'
                            detail_dict = self.parse_detail(key_url, mode)
                            item['duration'] = detail_dict.get('duration')
                            item['duration_per'] = detail_dict.get('duration_per')
                            item['ucascode'] = detail_dict.get('ucascode')
                            item['alevel'] = detail_dict.get('alevel')
                            item['ib'] = detail_dict.get('ib')
                            item['ielts_desc'] = detail_dict.get('ielts_desc')
                            item['tuition_fee'] = detail_dict.get('tuition_fee')
                            ielts_dict = get_ielts(item['ielts_desc'])
                            item['ielts'] = ielts_dict.get('IELTS')
                            item['ielts_l'] = ielts_dict.get('IELTS_L')
                            item['ielts_s'] = ielts_dict.get('IELTS_S')
                            item['ielts_r'] = ielts_dict.get('IELTS_R')
                            item['ielts_w'] = ielts_dict.get('IELTS_W')
                            print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                                item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))
                        elif f == "Full-time with Sandwich Year":
                            mode = 'sandwich'
                            detail_dict = self.parse_detail(key_url, mode)
                            item['duration'] = detail_dict.get('duration')
                            item['duration_per'] = detail_dict.get('duration_per')
                            item['ucascode'] = detail_dict.get('ucascode')
                            item['alevel'] = detail_dict.get('alevel')
                            item['ib'] = detail_dict.get('ib')
                            item['ielts_desc'] = detail_dict.get('ielts_desc')
                            item['tuition_fee'] = detail_dict.get('tuition_fee')
                            ielts_dict = get_ielts(item['ielts_desc'])
                            item['ielts'] = ielts_dict.get('IELTS')
                            item['ielts_l'] = ielts_dict.get('IELTS_L')
                            item['ielts_s'] = ielts_dict.get('IELTS_S')
                            item['ielts_r'] = ielts_dict.get('IELTS_R')
                            item['ielts_w'] = ielts_dict.get('IELTS_W')
                            print("===item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                                item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))
                        yield item
                else:
                    yield item

        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_detail(self, key_url, mode):
        detail_dict = {}
        detail_dict['duration'] = None
        detail_dict['duration_per'] = None
        detail_dict['ucascode'] = ""
        detail_dict['alevel'] = ""
        detail_dict['ib'] = ""
        detail_dict['ielts_desc'] = ""
        detail_dict['tuition_fee'] = None
        # 1.duration
        # https://www.bradford.ac.uk/courses/ug/api.php?uri=/courses/ug/biomedical-engineering-beng/&duration=duration&level=ug&year=y2019&attendance=fulltime
        duration_url = "https://www.bradford.ac.uk/courses/ug/api.php?uri=/courses/ug/" + key_url + "/&duration=duration&level=ug&year=y2019&attendance=" + mode
        # print("duration_url: ", duration_url)
        duration = json.loads(requests.get(duration_url).text).get("data")
        # print("duration: ", duration)
        if duration != None:
            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                detail_dict['duration'] = duration_list[0]
                detail_dict['duration_per'] = duration_list[-1]
        # print("item['duration'] = ", item['duration'])
        # print("item['duration_per'] = ", item['duration_per'])

        # 2.ucascode
        # https://www.bradford.ac.uk/courses/ug/api.php?uri=/courses/ug/biomedical-engineering-beng/&ucasCode=ucasCode&level=ug&year=y2019&attendance=fulltime
        ucascode_url = "https://www.bradford.ac.uk/courses/ug/api.php?uri=/courses/ug/" + key_url + "/&ucasCode=ucasCode&level=ug&year=y2019&attendance=" + mode
        # print("ucascode_url: ", ucascode_url)
        ucascode = json.loads(requests.get(ucascode_url).text).get("data")
        # print("ucascode: ", ucascode)
        if ucascode is not None:
            detail_dict['ucascode'] = ''.join(ucascode).strip()
        # print("item['ucascode']: ", item['ucascode'])


        # 3.alevel、ib
        # https://www.bradford.ac.uk/courses/ug/api.php?uri=/courses/ug/biomedical-engineering-beng/&entry=entry&level=ug&year=y2019&attendance=filltime
        entry_url = "https://www.bradford.ac.uk/courses/ug/api.php?uri=/courses/ug/" + key_url + "/&entry=entry&level=ug&year=y2019&attendance=" + mode
        # print("entry_url: ", entry_url)
        entry = json.loads(requests.get(entry_url).text).get("data")
        # print("entry: ", entry)
        if entry is not None:
            entry_response = etree.HTML(entry)
            alevel = entry_response.xpath("//strong[contains(text(),'A levels')]/../../following-sibling::div//text()")
            # print("alevel: ", alevel)
            detail_dict['alevel'] = clear_lianxu_space(alevel)

            ib = entry_response.xpath(
                "//strong[contains(text(),'International Baccalaureate requirements')]/../../following-sibling::div//text()")
            # print("ib: ", ib)
            detail_dict['ib'] = clear_lianxu_space(ib)

            ielts_desc = entry_response.xpath(
                "//strong[contains(text(),'English language requirements')]/../../following-sibling::div/p[1]//text()")
            detail_dict['ielts_desc'] = clear_lianxu_space(ielts_desc)
            # print("item['ielts_desc']: ", item['ielts_desc'])

        # 4.tuition_fee
        # https://www.bradford.ac.uk/courses/ug/api.php?uri=/courses/ug/biomedical-engineering-beng/&fees=fees&level=ug&year=y2019&attendance=fulltime
        tuition_fee_url = "https://www.bradford.ac.uk/courses/ug/api.php?uri=/courses/ug/" + key_url + "/&fees=fees&level=ug&year=y2019&attendance=" + mode
        # print("tuition_fee_url: ", tuition_fee_url)
        tuition_fee = json.loads(requests.get(tuition_fee_url).text).get("data")
        # print("tuition_fee: ", tuition_fee)
        if tuition_fee is not None:
            tuition_fee_response = etree.HTML(tuition_fee)
            tuition_fee_str = tuition_fee_response.xpath(
                "//div[@id='tuitionFees']//p[contains(text(),'International:')]//text()")
            # print("tuition_fee_str: ", tuition_fee_str)
            tuition_fee_re = re.findall(r"£\d+,\d+", ''.join(tuition_fee_str))

            if len(tuition_fee_re) > 0:
                detail_dict['tuition_fee'] = getTuition_fee(''.join(tuition_fee_re))
                # print("item['tuition_fee']: ", item['tuition_fee'])
        return detail_dict