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
from scrapySchool_Australian_ben.getIELTS import get_ielts
from selenium import webdriver
import json
from lxml import etree


# 2019/03/26 星期二 数据更新
class FederationUniversityAustralia_USpider(scrapy.Spider):
    name = "FederationUniversityAustralia_U"
    # //a[contains(@href,'#/course')]
    start_urls = ["https://study.federation.edu.au/api/programs_plan_code/DHM5/",
"https://study.federation.edu.au/api/programs_plan_code/DHS8.HU/",
"https://study.federation.edu.au/api/programs_plan_code/DHS8.SS/",
"https://study.federation.edu.au/api/programs_plan_code/DHC5/",
"https://study.federation.edu.au/api/programs_plan_code/DHJ5/",
"https://study.federation.edu.au/api/programs_plan_code/DBB5.NSM/",
"https://study.federation.edu.au/api/programs_plan_code/DBB5.ENT/",
"https://study.federation.edu.au/api/programs_plan_code/DBB8/",
"https://study.federation.edu.au/api/programs_plan_code/DBB5.HRM/",
"https://study.federation.edu.au/api/programs_plan_code/DBB5.MHR/",
"https://study.federation.edu.au/api/programs_plan_code/DBB5.MM/",
"https://study.federation.edu.au/api/programs_plan_code/DBB5.MAN/",
"https://study.federation.edu.au/api/programs_plan_code/DBB5.MRM/",
"https://study.federation.edu.au/api/programs_plan_code/DBB5.MIT/",
"https://study.federation.edu.au/api/programs_plan_code/DBB5.MK/",
"https://study.federation.edu.au/api/programs_plan_code/DBB5.PE/",
"https://study.federation.edu.au/api/programs_plan_code/DBC5.NSM/",
"https://study.federation.edu.au/api/programs_plan_code/DBC5.AIT/",
"https://study.federation.edu.au/api/programs_plan_code/DBC5.ACC/",
"https://study.federation.edu.au/api/programs_plan_code/DBC5.ACE/",
"https://study.federation.edu.au/api/programs_plan_code/DBC5.ECO/",
"https://study.federation.edu.au/api/programs_plan_code/DBC8/",
"https://study.federation.edu.au/api/programs_plan_code/DBC5.LM/",
"https://study.federation.edu.au/api/programs_plan_code/DBD5/",
"https://study.federation.edu.au/api/programs_plan_code/DVH5/",
"https://study.federation.edu.au/api/programs_plan_code/DTO5/",
"https://study.federation.edu.au/api/programs_plan_code/DTX5/",
"https://study.federation.edu.au/api/programs_plan_code/DTZ5/",
"https://study.federation.edu.au/api/programs_plan_code/DTC5/",
"https://study.federation.edu.au/api/programs_plan_code/DTL5/",
"https://study.federation.edu.au/api/programs_plan_code/DTA5/",
"https://study.federation.edu.au/api/programs_plan_code/DEG8.CIV/",
"https://study.federation.edu.au/api/programs_plan_code/DEG8.MEC/",
"https://study.federation.edu.au/api/programs_plan_code/DEG8.MIN/",
"https://study.federation.edu.au/api/programs_plan_code/DGM8/",
"https://study.federation.edu.au/api/programs_plan_code/DCT5.NSM/",
"https://study.federation.edu.au/api/programs_plan_code/DCT5.BDA/",
"https://study.federation.edu.au/api/programs_plan_code/DCT5.BIS/",
"https://study.federation.edu.au/api/programs_plan_code/DCT5.CEC/",
"https://study.federation.edu.au/api/programs_plan_code/DCT5.GD/",
"https://study.federation.edu.au/api/programs_plan_code/DCT5.MAD/",
"https://study.federation.edu.au/api/programs_plan_code/DCT5.NS/",
"https://study.federation.edu.au/api/programs_plan_code/DCI5/",
"https://study.federation.edu.au/api/programs_plan_code/DCT5.SD/",
"https://study.federation.edu.au/api/programs_plan_code/DSH5/",
"https://study.federation.edu.au/api/programs_plan_code/DSH5.EHI/",
"https://study.federation.edu.au/api/programs_plan_code/DSH5.LMH/",
"https://study.federation.edu.au/api/programs_plan_code/DHN5/",
"https://study.federation.edu.au/api/programs_plan_code/DAY5/",
"https://study.federation.edu.au/api/programs_plan_code/DHY5/",
"https://study.federation.edu.au/api/programs_plan_code/DSB5/",
"https://study.federation.edu.au/api/programs_plan_code/DST5/",
"https://study.federation.edu.au/api/programs_plan_code/DSE5/",
"https://study.federation.edu.au/api/programs_plan_code/DSN5/",
"https://study.federation.edu.au/api/programs_plan_code/DSG5/",
"https://study.federation.edu.au/api/programs_plan_code/DSY5/",
"https://study.federation.edu.au/api/programs_plan_code/DSC5/",
"https://study.federation.edu.au/api/programs_plan_code/DSZ8/",
"https://study.federation.edu.au/api/programs_plan_code/DSV5/",
"https://study.federation.edu.au/api/programs_plan_code/DPX5/",
"https://study.federation.edu.au/api/programs_plan_code/DPH5/",
"https://study.federation.edu.au/api/programs_plan_code/DOE5/",
"https://study.federation.edu.au/api/programs_plan_code/DPM5/",
"https://study.federation.edu.au/api/programs_plan_code/DPZ5/",
"https://study.federation.edu.au/api/programs_plan_code/DHS8.CA/",
"https://study.federation.edu.au/api/programs_plan_code/DAI5/",
"https://study.federation.edu.au/api/programs_plan_code/DAQ5/",
"https://study.federation.edu.au/api/programs_plan_code/DAA5.FA/",]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "Federation University Australia"
        # item['country'] = 'Australia'
        # item['website'] = 'https://search.federation.edu.au'
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        informationUrl = response.url.replace("https://study.federation.edu.au/api/programs_plan_code", "https://study.federation.edu.au/#/course")
        print("------------", informationUrl)
        item['url'] = informationUrl
        try:
            # jsonData = clear_space_str(response.body).replace('\"', "'").replace(" ", "")
            jsonData = response.body
            informationDict = json.loads(jsonData)
            print(informationDict)

            international_details = informationDict.get("international_details")
            # print("international_details: ", international_details)

            programme = informationDict.get("title")
            item['degree_name'] = programme
            print("item['degree_name']: ", item['degree_name'])

            pro_re = re.findall(r"Bachelor", item['degree_name'])
            # print("pre_re: ", pro_re)
            if len(pro_re) < 2:
                programme_re = re.findall(r"\(.+\)", item['degree_name'])
                if len(programme_re) > 0:
                    if ''.join(programme_re) != "(Honours)":
                        item['programme_en'] = ''.join(programme_re).replace("(", "").replace(")", "").strip()
                    else:
                        item['programme_en'] = item['degree_name'].replace("Bachelor of", "").replace("(Honours)", "").strip()
                else:
                    item['programme_en'] = item['degree_name'].replace("Bachelor of", "").strip()
                print("item['programme_en']: ", item['programme_en'])

                location = international_details.get("teaching_location")
                item['location'] = location
                # print("item['location']: ", item['location'])

                department = informationDict.get("school_dept")
                item['department'] = department
                # print("item['department']: ", item['department'])

                overviewHtml = informationDict.get("outline")
                # print("overviewHtml: ", overviewHtml)
                delFu = re.findall(r"&\w+;", overviewHtml)
                # print(delFu)
                if len(delFu) != 0:
                    for d in delFu:
                        overviewHtml = overviewHtml.replace(d, "")
                # pageHtml = '<!DOCTYPE html><html><body>' + overviewHtml + '</body></html>'
                item['degree_overview_en'] = remove_class(clear_lianxu_space([overviewHtml]))
                # print("item['degree_overview_en']: ", item['degree_overview_en'])

                duration = international_details.get("duration")
                item['duration'] = duration
                # print("item['duration']: ", item['duration'])

                start_date = informationDict.get("commences")
                item['start_date'] = start_date
                # print("item['start_date']: ", item['start_date'])

                career1 = informationDict.get("careers")
                career1Str = ""
                # print(career1)
                if len(career1) != 0:
                    for career1dict in career1:
                        career1Str += "<p>"+career1dict.get("name") + "</p>"
                career2 = informationDict.get("career_opportunities")
                # print(career2)
                if "<p>" in career2:
                    delFu = re.findall(r"&\w+;", career2)
                    if len(delFu) != 0:
                        for d in delFu:
                            career2 = career2.replace(d, " ")
                    career2 = career2.replace("<br>", " ")
                    # pageHtml = '<!DOCTYPE html><html><body>' + career2 + '</body></html>'
                    career2 = remove_class(clear_lianxu_space([career2]))
                career = career1Str + career2
                item['career_en'] = career
                # print("item['career_en']: ", item['career_en'])

                tuition_fee = international_details.get("annual_fee_int")
                item['tuition_fee'] = tuition_fee
                # print("item['tuition_fee']: ", item['tuition_fee'])

                entry_requirements = international_details.get("academic_entry_requirements")
                entry_requirements1 = international_details.get("extra_requirements")
                delFu = re.findall(r"&\w+;", entry_requirements)
                if len(delFu) != 0:
                    for d in delFu:
                        entry_requirements = entry_requirements.replace(d, " ")
                # entry_requirementsHtml = '<!DOCTYPE html><html><body>' + entry_requirements + '</body></html>'
                item['rntry_requirements_en'] = remove_class(clear_lianxu_space([entry_requirements]))+remove_class(clear_lianxu_space([entry_requirements1]))
                # print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

                IELTS = international_details.get("english_language_requirement")
                delFu = re.findall(r"&\w+;", IELTS)
                if len(delFu) != 0:
                    for d in delFu:
                        IELTS = IELTS.replace(d, " ")
                IELTSHtml = '<!DOCTYPE html><html><body>' + IELTS + '</body></html>'
                html = etree.fromstring(IELTSHtml)
                IELTS = html.xpath("//p//text()")
                IELTS = ''.join(IELTS)
                item['ielts_desc'] = IELTS
                # print("item['ielts_desc']: ", item['ielts_desc'])

                ieltlsrw = re.findall(r"\d[\d\.]{0,2}", item['ielts_desc'])
                # print(ieltlsrw)
                if len(ieltlsrw) == 1:
                    item["ielts"] = ieltlsrw[0]
                    item["ielts_l"] = ieltlsrw[0]
                    item["ielts_s"] = ieltlsrw[0]
                    item["ielts_r"] = ieltlsrw[0]
                    item["ielts_w"] = ieltlsrw[0]
                elif len(ieltlsrw) == 2:
                    item["ielts"] = ieltlsrw[0]
                    item["ielts_l"] = ieltlsrw[1]
                    item["ielts_s"] = ieltlsrw[1]
                    item["ielts_r"] = ieltlsrw[1]
                    item["ielts_w"] = ieltlsrw[1]
                elif len(ieltlsrw) == 3:
                    item["ielts"] = ieltlsrw[0]
                    item["ielts_l"] = ieltlsrw[1]
                    item["ielts_s"] = ieltlsrw[1]
                    item["ielts_r"] = ieltlsrw[2]
                    item["ielts_w"] = ieltlsrw[2]
                # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                        # item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

                # print("--ces")
                modules = informationDict.get("domestic_details").get("program_structures").get("majors")
                # print("modules: ", type(modules))
                if len(modules) != 0:
                    modules = modules[0].get("year_levels")
                # print("modules: ", modules)
                # print("modules: ", type(modules))
                modulesStr = ""
                for m in modules:
                    modulesStr += str(m)
                item['modules_en'] = "<div>"+modulesStr.replace("[", "").replace("]", "").replace("{", "").replace("}", "")+"</div>"
                print("item['modules_en']: ", item['modules_en'])

                # item['application_date'] = "Monday 5 March, 2018"
                # item['deadline'] = "TBC"
                # item['application_fee'] = "25"

                how_to_apply = informationDict.get("apply_link")
                item['apply_proces_en'] = how_to_apply
                # print("item['apply_proces_en']: ", item['apply_proces_en'])

                # driver = webdriver.Chrome(r"C:\Users\delsk\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\selenium\chromedriver.exe")
                # driver = webdriver.PhantomJS(r"C:\Users\delsk\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\selenium\phantomjs-2.1.1-windows\bin\phantomjs.exe")
                # driver.get(informationUrl)
                # print(driver.page_source)
                # modules = driver.find_element_by_xpath("//div[@class='no-print panel panel-default']").text
                # print(modules)
                # item['modules_en'] = remove_class(clear_lianxu_space(modules))
                # print("item['modules_en']: ", item['modules_en'])
                yield item
        except Exception as e:
            with open("scrapySchool_Australian_ben/error/" + item['university'] + str(item['degree_type']) + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

