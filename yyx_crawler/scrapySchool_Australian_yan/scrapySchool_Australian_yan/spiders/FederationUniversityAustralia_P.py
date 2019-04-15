# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_Australian_yan.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_yan.getItem import get_item
from scrapySchool_Australian_yan.getTuition_fee import getTuition_fee
from scrapySchool_Australian_yan.items import ScrapyschoolAustralianYanItem
from scrapySchool_Australian_yan.remove_tags import remove_class
from scrapySchool_Australian_yan.getStartDate import getStartDate
from scrapySchool_Australian_yan.getDuration import getIntDuration
from scrapySchool_Australian_yan.getIELTS import get_ielts
import json
from lxml import etree

# https://study.federation.edu.au/#/results
class FederationUniversityAustralia_PSpider(scrapy.Spider):
    name = "FederationUniversityAustralia_P"

#     start_urls = ["https://study.federation.edu.au/api/programs_plan_code/DHW9/",
# "https://study.federation.edu.au/api/programs_plan_code/DMU9/",
# "https://study.federation.edu.au/api/programs_plan_code/DMM9/",
# "https://study.federation.edu.au/api/programs_plan_code/DBX9/",
# "https://study.federation.edu.au/api/programs_plan_code/DTM9/",
# "https://study.federation.edu.au/api/programs_plan_code/DTY9/",
# "https://study.federation.edu.au/api/programs_plan_code/DTZ9/",
# "https://study.federation.edu.au/api/programs_plan_code/DEI9/",
# "https://study.federation.edu.au/api/programs_plan_code/DEY9.CIV/",
# "https://study.federation.edu.au/api/programs_plan_code/DEY9.MEC/",
# "https://study.federation.edu.au/api/programs_plan_code/DEY9.MIN/",
# "https://study.federation.edu.au/api/programs_plan_code/DEM9/",
# "https://study.federation.edu.au/api/programs_plan_code/DCV9/",
# "https://study.federation.edu.au/api/programs_plan_code/DCG9.EB/",
# "https://study.federation.edu.au/api/programs_plan_code/DCG9.RS/",
# "https://study.federation.edu.au/api/programs_plan_code/DCG9.SE/",
# "https://study.federation.edu.au/api/programs_plan_code/DNN9/",
# "https://study.federation.edu.au/api/programs_plan_code/DHN9.HL/",
# "https://study.federation.edu.au/api/programs_plan_code/DHN9.RP/",
# "https://study.federation.edu.au/api/programs_plan_code/DEJ9/",
# "https://study.federation.edu.au/api/programs_plan_code/DYS9/",
# "https://study.federation.edu.au/api/programs_plan_code/DYL9/",
# "https://study.federation.edu.au/api/programs_plan_code/DSA9/",
# "https://study.federation.edu.au/api/programs_plan_code/DCM9/",
# "https://study.federation.edu.au/api/programs_plan_code/DMM9.HSM/",
# "https://study.federation.edu.au/api/programs_plan_code/DPL9/",
# "https://study.federation.edu.au/api/programs_plan_code/DPN9/",
# "https://study.federation.edu.au/api/programs_plan_code/DPM9/",
# "https://study.federation.edu.au/api/programs_plan_code/DPO9/",
# "https://study.federation.edu.au/api/programs_plan_code/DPJ9/",
# "https://study.federation.edu.au/api/programs_plan_code/DPW9/",
# "https://study.federation.edu.au/api/programs_plan_code/DAU9/", ]
#     start_urls = ["https://study.federation.edu.au/api/programs_plan_code/GVA9/", ]
    # 2019.03.18 星期一 数据更新
    start_urls = ["https://study.federation.edu.au/api/programs_plan_code/DHB9/",
"https://study.federation.edu.au/api/programs_plan_code/DHW9/",
"https://study.federation.edu.au/api/programs_plan_code/DMU9/",
"https://study.federation.edu.au/api/programs_plan_code/DMM9/",
"https://study.federation.edu.au/api/programs_plan_code/DMM9.HSM/",
"https://study.federation.edu.au/api/programs_plan_code/DBX9/",
"https://study.federation.edu.au/api/programs_plan_code/DTY9/",
"https://study.federation.edu.au/api/programs_plan_code/DTZ9/",
"https://study.federation.edu.au/api/programs_plan_code/DEI9/",
"https://study.federation.edu.au/api/programs_plan_code/DEY9.CIV/",
"https://study.federation.edu.au/api/programs_plan_code/DEY9.MEC/",
"https://study.federation.edu.au/api/programs_plan_code/DEY9.MIN/",
"https://study.federation.edu.au/api/programs_plan_code/DCV9/",
"https://study.federation.edu.au/api/programs_plan_code/DCG9.EB/",
"https://study.federation.edu.au/api/programs_plan_code/DCG9.RS/",
"https://study.federation.edu.au/api/programs_plan_code/DCG9.SE/",
"https://study.federation.edu.au/api/programs_plan_code/DNN9/",
"https://study.federation.edu.au/api/programs_plan_code/DHN9.HL/",
"https://study.federation.edu.au/api/programs_plan_code/DHN9.RP/",
"https://study.federation.edu.au/api/programs_plan_code/DEJ9/",
"https://study.federation.edu.au/api/programs_plan_code/DSA9/",
"https://study.federation.edu.au/api/programs_plan_code/DCM9/",
"https://study.federation.edu.au/api/programs_plan_code/DPL9/",
"https://study.federation.edu.au/api/programs_plan_code/DPN9/",
"https://study.federation.edu.au/api/programs_plan_code/DPM9/",
"https://study.federation.edu.au/api/programs_plan_code/DPO9/",
"https://study.federation.edu.au/api/programs_plan_code/DPJ9/",
"https://study.federation.edu.au/api/programs_plan_code/DPW9/",
"https://study.federation.edu.au/api/programs_plan_code/DAU9/", ]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        item = get_item(ScrapyschoolAustralianYanItem)
        item['university'] = "Federation University Australia"
        # item['country'] = 'Australia'
        # item['website'] = 'https://search.federation.edu.au'
        item['degree_type'] = 2
        item['teach_time'] = 'coursework'
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

            type_desc = informationDict.get("type_desc")
            print("type_desc: ", type_desc)
            if "research" not in type_desc.lower():
                programme = informationDict.get("title")
                item['degree_name'] = programme
                print("item['degree_name']: ", item['degree_name'])

                pro_re = re.findall(r"Master", item['degree_name'])
                # print("pre_re: ", pro_re)
                if len(pro_re) < 2:
                    programme_re = re.findall(r"\(.+\)", item['degree_name'])
                    if len(programme_re) > 0:
                        item['programme_en'] = ''.join(programme_re).replace("(", "").replace(")", "").strip()
                    else:
                        item['programme_en'] = item['degree_name'].replace("Master of", "").strip()
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
                            overviewHtml = overviewHtml.replace(d, " ")
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

                    ielts_dict = get_ielts(item['ielts_desc'])
                    item["ielts"] = ielts_dict.get('IELTS')
                    item["ielts_l"] = ielts_dict.get('IELTS_L')
                    item["ielts_s"] = ielts_dict.get('IELTS_S')
                    item["ielts_r"] = ielts_dict.get('IELTS_R')
                    item["ielts_w"] = ielts_dict.get('IELTS_W')
                    # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                    #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

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
                    # print("item['modules_en']: ", item['modules_en'])

                    # item['application_date'] = "Monday 5 March, 2018"
                    # item['deadline'] = "TBC"
                    # item['application_fee'] = "25"

                    how_to_apply = informationDict.get("apply_link")
                    item['apply_proces_en'] = how_to_apply
                    # print("item['apply_proces_en']: ", item['apply_proces_en'])

                    # location = informationDict.get("campuses")
                    # print("location: ", location)
                    # locationStr = ""
                    # if len(location) != 0:
                    #     for locationdict in location:
                    #         locationStr += locationdict.get("name") + " "


                    yield item
        except Exception as e:
            with open("scrapySchool_Australian_yan/error/" + item['university'] + str(item['degree_type']) + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

