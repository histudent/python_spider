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
from lxml import etree
import requests


class EdithCowanUniversity_PSpider(scrapy.Spider):
    name = "EdithCowanUniversity_P"
#     start_urls = ["http://www.ecu.edu.au/degrees/courses/master-of-business-administration",
# "http://www.ecu.edu.au/degrees/courses/master-of-business-administration-international",
# "http://www.ecu.edu.au/degrees/courses/master-of-clinical-nursing",
# "http://www.ecu.edu.au/degrees/courses/master-of-communication",
# "http://www.ecu.edu.au/degrees/courses/master-of-computer-science",
# "http://www.ecu.edu.au/degrees/courses/master-of-counselling-and-psychotherapy",
# "http://www.ecu.edu.au/degrees/courses/master-of-critical-care-paramedicine",
# "http://www.ecu.edu.au/degrees/courses/master-of-cyber-security",
# "http://www.ecu.edu.au/degrees/courses/master-of-design",
# "http://www.ecu.edu.au/degrees/courses/master-of-disaster-and-emergency-response",
# "http://www.ecu.edu.au/degrees/courses/master-of-education",
# "http://www.ecu.edu.au/degrees/courses/master-of-education-advanced",
# "http://www.ecu.edu.au/degrees/courses/master-of-engineering",
# "http://www.ecu.edu.au/degrees/courses/master-of-environmental-management",
# "http://www.ecu.edu.au/degrees/courses/master-of-environmental-science",
# "http://www.ecu.edu.au/degrees/courses/master-of-exercise-science-strength-and-conditioning",
# "http://www.ecu.edu.au/degrees/courses/master-of-finance-and-banking",
# "http://www.ecu.edu.au/degrees/courses/master-of-human-resource-management",
# "http://www.ecu.edu.au/degrees/courses/master-of-international-hospitality-management",
# "http://www.ecu.edu.au/degrees/courses/master-of-management-information-systems",
# "http://www.ecu.edu.au/degrees/courses/master-of-marketing-and-innovation-management",
# "http://www.ecu.edu.au/degrees/courses/master-of-midwifery-practice",
# "http://www.ecu.edu.au/degrees/courses/master-of-neurological-rehabilitation",
# "http://www.ecu.edu.au/degrees/courses/master-of-nurse-education",
# "http://www.ecu.edu.au/degrees/courses/master-of-nursing",
# "http://www.ecu.edu.au/degrees/courses/master-of-nursing-graduate-entry",
# "http://www.ecu.edu.au/degrees/courses/master-of-nursing-nurse-practitioner",
# "http://www.ecu.edu.au/degrees/courses/master-of-nutrition-and-dietetics",
# "http://www.ecu.edu.au/degrees/courses/master-of-occupational-health-and-safety",
# "http://www.ecu.edu.au/degrees/courses/master-of-occupational-hygiene-and-toxicology",
# "http://www.ecu.edu.au/degrees/courses/master-of-paramedic-practitioner",
# "http://www.ecu.edu.au/degrees/courses/master-of-professional-accounting",
# "http://www.ecu.edu.au/degrees/courses/master-of-professional-communication",
# "http://www.ecu.edu.au/degrees/courses/master-of-professional-design",
# "http://www.ecu.edu.au/degrees/courses/master-of-project-management",
# "http://www.ecu.edu.au/degrees/courses/master-of-psychology",
# "http://www.ecu.edu.au/degrees/courses/master-of-public-health",
# "http://www.ecu.edu.au/degrees/courses/master-of-science-assisted-reproductive-technology",
# "http://www.ecu.edu.au/degrees/courses/master-of-screen-studies",
# "http://www.ecu.edu.au/degrees/courses/master-of-teaching-early-childhood",
# "http://www.ecu.edu.au/degrees/courses/master-of-teaching-primary",
# "http://www.ecu.edu.au/degrees/courses/master-of-teaching-secondary",
# "http://www.ecu.edu.au/degrees/courses/master-of-technology-petroleum-engineering", ]
#     start_urls = ["http://www.ecu.edu.au/degrees/courses/master-of-science-biological-sciences",
# "http://www.ecu.edu.au/degrees/courses/master-of-science-chemistry",
# "http://www.ecu.edu.au/degrees/courses/master-of-science-computer-science",
# "http://www.ecu.edu.au/degrees/courses/master-of-engineering-science",
# "http://www.ecu.edu.au/degrees/courses/master-of-science-environmental-management",
# "http://www.ecu.edu.au/degrees/courses/master-of-science-mathematics-and-planning",
# "http://www.ecu.edu.au/degrees/courses/master-of-arts-performing-arts",
# "http://www.ecu.edu.au/degrees/courses/master-of-science-assisted-reproductive-technology",
# "http://www.ecu.edu.au/degrees/courses/master-of-science-interdisciplinary-studies",
# "http://www.ecu.edu.au/degrees/courses/master-of-social-science",]
    #  2019.03.18 星期一 数据更新
    start_urls = ["https://www.ecu.edu.au/degrees/courses/master-of-environmental-science",
"https://www.ecu.edu.au/degrees/courses/master-of-paramedic-practitioner",
"https://www.ecu.edu.au/degrees/courses/master-of-professional-communication",
"https://www.ecu.edu.au/degrees/courses/master-of-critical-care-paramedicine",
"https://www.ecu.edu.au/degrees/courses/master-of-human-resource-management",
"https://www.ecu.edu.au/degrees/courses/master-of-computer-science",
"https://www.ecu.edu.au/degrees/courses/master-of-nursing",
"https://www.ecu.edu.au/degrees/courses/master-of-communication",
"https://www.ecu.edu.au/degrees/courses/master-of-business-administration-international",
"https://www.ecu.edu.au/degrees/courses/master-of-education",
"https://www.ecu.edu.au/degrees/courses/master-of-public-health",
"https://www.ecu.edu.au/degrees/courses/master-of-science-assisted-reproductive-technology",
"https://www.ecu.edu.au/degrees/courses/master-of-technology-petroleum-engineering",
"https://www.ecu.edu.au/degrees/courses/master-of-engineering",
"https://www.ecu.edu.au/degrees/courses/master-of-project-management",
"https://www.ecu.edu.au/degrees/courses/master-of-professional-design",
"https://www.ecu.edu.au/degrees/courses/master-of-psychology",
"https://www.ecu.edu.au/degrees/courses/master-of-cyber-security",
"https://www.ecu.edu.au/degrees/courses/master-of-finance-and-banking",
"https://www.ecu.edu.au/degrees/courses/master-of-management-information-systems",
"https://www.ecu.edu.au/degrees/courses/master-of-international-hospitality-management",
"https://www.ecu.edu.au/degrees/courses/master-of-marketing-and-innovation-management",
"https://www.ecu.edu.au/degrees/courses/master-of-professional-accounting",
"https://www.ecu.edu.au/degrees/courses/master-of-business-administration",
"https://www.ecu.edu.au/degrees/courses/master-of-counselling-and-psychotherapy",
"https://www.ecu.edu.au/degrees/courses/master-of-design",
"https://www.ecu.edu.au/degrees/courses/master-of-nursing-graduate-entry",
"https://www.ecu.edu.au/degrees/courses/master-of-teaching-secondary",
"https://www.ecu.edu.au/degrees/courses/master-of-education-advanced",
"https://www.ecu.edu.au/degrees/courses/master-of-teaching-primary",
"https://www.ecu.edu.au/degrees/courses/master-of-screen-studies",
"https://www.ecu.edu.au/degrees/courses/master-of-nutrition-and-dietetics",
"https://www.ecu.edu.au/degrees/courses/master-of-teaching-early-childhood", ]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        item = get_item(ScrapyschoolAustralianYanItem)
        item['university'] = "Edith Cowan University"
        # item['country'] = 'Australia'
        # item['website'] = 'https://www.uts.edu.au'
        item['url'] = response.url
        item['degree_type'] = 2
        item['teach_time'] = 'coursework'
        print("===========================")
        print(response.url)
        # 组合字典
        links = ["http://www.ecu.edu.au/degrees/courses/master-of-business-administration",
                 "http://www.ecu.edu.au/degrees/courses/master-of-business-administration-international",
                 "http://www.ecu.edu.au/degrees/courses/master-of-clinical-nursing",
                 "http://www.ecu.edu.au/degrees/courses/master-of-communication",
                 "http://www.ecu.edu.au/degrees/courses/master-of-computer-science",
                 "http://www.ecu.edu.au/degrees/courses/master-of-counselling-and-psychotherapy",
                 "http://www.ecu.edu.au/degrees/courses/master-of-critical-care-paramedicine",
                 "http://www.ecu.edu.au/degrees/courses/master-of-cyber-security",
                 "http://www.ecu.edu.au/degrees/courses/master-of-design",
                 "http://www.ecu.edu.au/degrees/courses/master-of-disaster-and-emergency-response",
                 "http://www.ecu.edu.au/degrees/courses/master-of-education",
                 "http://www.ecu.edu.au/degrees/courses/master-of-education-advanced",
                 "http://www.ecu.edu.au/degrees/courses/master-of-engineering",
                 "http://www.ecu.edu.au/degrees/courses/master-of-environmental-management",
                 "http://www.ecu.edu.au/degrees/courses/master-of-environmental-science",
                 "http://www.ecu.edu.au/degrees/courses/master-of-exercise-science-strength-and-conditioning",
                 "http://www.ecu.edu.au/degrees/courses/master-of-finance-and-banking",
                 "http://www.ecu.edu.au/degrees/courses/master-of-human-resource-management",
                 "http://www.ecu.edu.au/degrees/courses/master-of-international-hospitality-management",
                 "http://www.ecu.edu.au/degrees/courses/master-of-management-information-systems",
                 "http://www.ecu.edu.au/degrees/courses/master-of-marketing-and-innovation-management",
                 "http://www.ecu.edu.au/degrees/courses/master-of-midwifery-practice",
                 "http://www.ecu.edu.au/degrees/courses/master-of-neurological-rehabilitation",
                 "http://www.ecu.edu.au/degrees/courses/master-of-nurse-education",
                 "http://www.ecu.edu.au/degrees/courses/master-of-nursing",
                 "http://www.ecu.edu.au/degrees/courses/master-of-nursing-graduate-entry",
                 "http://www.ecu.edu.au/degrees/courses/master-of-nursing-nurse-practitioner",
                 "http://www.ecu.edu.au/degrees/courses/master-of-nutrition-and-dietetics",
                 "http://www.ecu.edu.au/degrees/courses/master-of-occupational-health-and-safety",
                 "http://www.ecu.edu.au/degrees/courses/master-of-occupational-hygiene-and-toxicology",
                 "http://www.ecu.edu.au/degrees/courses/master-of-paramedic-practitioner",
                 "http://www.ecu.edu.au/degrees/courses/master-of-professional-accounting",
                 "http://www.ecu.edu.au/degrees/courses/master-of-professional-communication",
                 "http://www.ecu.edu.au/degrees/courses/master-of-professional-design",
                 "http://www.ecu.edu.au/degrees/courses/master-of-project-management",
                 "http://www.ecu.edu.au/degrees/courses/master-of-psychology",
                 "http://www.ecu.edu.au/degrees/courses/master-of-public-health",
                 "http://www.ecu.edu.au/degrees/courses/master-of-science-assisted-reproductive-technology",
                 "http://www.ecu.edu.au/degrees/courses/master-of-screen-studies",
                 "http://www.ecu.edu.au/degrees/courses/master-of-teaching-early-childhood",
                 "http://www.ecu.edu.au/degrees/courses/master-of-teaching-primary",
                 "http://www.ecu.edu.au/degrees/courses/master-of-teaching-secondary",
                 "http://www.ecu.edu.au/degrees/courses/master-of-technology-petroleum-engineering", ]
        programme_dict = {}
        programme_list = ["Master of Business Administration",
                          "Master of Business Administration International",
                          "Master of Clinical Nursing",
                          "Master of Communication",
                          "Master of Computer Science",
                          "Master of Counselling and Psychotherapy",
                          "Master of Critical Care Paramedicine",
                          "Master of Cyber Security",
                          "Master of Design",
                          "Master of Disaster and Emergency Response",
                          "Master of Education",
                          "Master of Education (Advanced)",
                          "Master of Engineering",
                          "Master of Environmental Management",
                          "Master of Environmental Science",
                          "Master of Exercise Science (Strength and Conditioning)",
                          "Master of Finance and Banking",
                          "Master of Human Resource Management",
                          "Master of International Hospitality Management",
                          "Master of Management Information Systems",
                          "Master of Marketing and Innovation Management",
                          "Master of Midwifery Practice",
                          "Master of Neurological Rehabilitation",
                          "Master of Nurse Education",
                          "Master of Nursing",
                          "Master of Nursing (Graduate Entry)",
                          "Master of Nursing (Nurse Practitioner)",
                          "Master of Nutrition and Dietetics",
                          "Master of Occupational Health and Safety",
                          "Master of Occupational Hygiene and Toxicology",
                          "Master of Paramedic Practitioner",
                          "Master of Professional Accounting",
                          "Master of Professional Communication",
                          "Master of Professional Design",
                          "Master of Project Management",
                          "Master of Psychology",
                          "Master of Public Health",
                          "Master of Science (Assisted Reproductive Technology)",
                          "Master of Screen Studies",
                          "Master of Teaching (Early Childhood)",
                          "Master of Teaching (Primary)",
                          "Master of Teaching (Secondary)",
                          "Master of Technology (Petroleum Engineering)", ]
        for link in range(len(links)):
            url = links[link]
            programme_dict[url] = programme_list[link]
        item['major_type1'] = programme_dict.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            programme = response.xpath("//h2[contains(text(), 'Master of')]//text()").extract()
            clear_space(programme)
            programme = ''.join(programme).strip()
            item['degree_name'] = programme
            print("item['degree_name']: ", item['degree_name'])

            pro_re = re.findall(r"Master", item['degree_name'])
            # print("pre_re: ", pro_re)
            if len(pro_re) < 2:
                programme_re = re.findall(r"\(.+\)", item['degree_name'].replace("(Graduate Entry)", "").replace("(Advanced)", ""))
                if len(programme_re) > 0:
                    item['programme_en'] = ''.join(programme_re).replace("(", "").replace(")", "").strip()
                else:
                    item['programme_en'] = item['degree_name'].replace("Master of", "").strip()
                print("item['programme_en']: ", item['programme_en'])

                overview = response.xpath("//span[@id='overview']/..").extract()
                item['degree_overview_en'] = remove_class(clear_lianxu_space(overview))
                # print("item['degree_overview_en']: ", item['degree_overview_en'])

                entry_requirements = response.xpath("//div[@id='before-you-start']").extract()
                entry_requirements_str = ''.join(entry_requirements).strip()
                item['rntry_requirements_en'] = remove_class(clear_lianxu_space(entry_requirements))
                # print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

                modules = response.xpath(
                    "//h4[contains(text(),'Course structure')]|//div[@class='structure-heading']").extract()
                item['modules_en'] = remove_class(clear_lianxu_space(modules))
                # print("item['modules_en']: ", item['modules_en'])

                career = response.xpath("//h4[contains(text(),'Employment opportunities')]|//h4[contains(text(),'Employment opportunities')]/following-sibling::*[1]|"
                                        "//h4[contains(text(),'Possible future job titles')]|//h4[contains(text(),'Possible future job titles')]/following-sibling::*[1]").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career))
                if item['career_en'] == "":
                    print("***career_en 为空")
                print("item['career_en']: ", item['career_en'])

                location = response.xpath("//div[@class='courseOverview__info courseOverview__info--international courseOverview__info--noOnline']//div[@class='studyCampus__location studyCampus__location--joondalup studyCampus__location--active']/h4//text()|"
                                          "//div[@class='courseOverview__info courseOverview__info--international courseOverview__info--noOnline']//div[@class='studyCampus__location studyCampus__location--mtLawley studyCampus__location--active']/h4//text()|"
                                          "//div[@class='courseOverview__info courseOverview__info--international courseOverview__info--noOnline']//div[@class='studyCampus__location studyCampus__location--bunbury studyCampus__location--active']/h4//text()|"
                                          "//div[@class='courseOverview__info courseOverview__info--international']//div[@class='studyCampus__location studyCampus__location--joondalup studyCampus__location--active']/h4//text()|"
                                          "//div[@class='courseOverview__info courseOverview__info--international']//div[@class='studyCampus__location studyCampus__location--mtLawley studyCampus__location--active']/h4//text()|"
                                          "//div[@class='courseOverview__info courseOverview__info--international']//div[@class='studyCampus__location studyCampus__location--bunbury studyCampus__location--active']/h4//text()").extract()
                clear_space(location)
                location = ', '.join(location).strip().strip(',').strip()
                item['location'] = location
                location_tmp = item['location']
                print("item['location']: ", item['location'])

                duration = response.xpath("//div[@class='courseOverview__info courseOverview__info--international courseOverview__info--noOnline']//p[contains(text(),'year')]//text()|"
                                          "//div[@class='courseOverview__info courseOverview__info--international']//p[contains(text(),'year')]//text()").extract()
                clear_space(duration)
                print("duration: ", duration)
                duration_re = re.findall(r"Start\sSemester.*", ''.join(duration).strip())
                print(duration_re, "===")
                item['start_date'] = ','.join(duration_re)
                item['duration'] = ''.join(duration).replace(''.join(duration_re), "").strip()
                print("item['duration']: ", item['duration'])

                other = response.xpath("//span[@class='courseOverview__subHeader alert-warning alert']//text()").extract()
                item['other'] = ''.join(other)
                print("item['other']: ",item['other'])

                # 英语要求
                # https://www.ecu.edu.au/future-students/course-entry/english-competency#toggle-2
                # ieltsRe = re.findall(r"IELTS[0-9a-zA-Z:\.,\s]*;", entry_requirements_str)
                # # print("ieltsRe: ", ieltsRe)
                # toeflRe = re.findall(r"internet\sbased[0-9a-zA-Z:\.,\s-]*;", entry_requirements_str)
                # # print("toeflRe: ", toeflRe)
                # item['ielts_desc'] = ''.join(ieltsRe).strip()
                # # print("item['ielts_desc']: ", item['ielts_desc'])
                #
                # item['toefl_desc'] = ''.join(toeflRe).strip()
                # # print("item['toefl_desc']: ", item['toefl_desc'])
                #
                # print("item['ielts_desc']: ", item['ielts_desc'])
                #
                #
                #
                #
                # ielts_d = get_ielts(item['ielts_desc'])
                # item["ielts"] = ielts_d.get('IELTS')
                # item["ielts_l"] = ielts_d.get('IELTS_L')
                # item["ielts_s"] = ielts_d.get('IELTS_S')
                # item["ielts_r"] = ielts_d.get('IELTS_R')
                # item["ielts_w"] = ielts_d.get('IELTS_W')
                # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))
                #
                # department = response.xpath(
                #     "//div[@class='field field-dddd-view-modeluts-course-course__part-of field-type-ds field-label-hidden']//div[@class='field-item']//p/a/text()").extract()
                # clear_space(department)
                # department = ''.join(department).replace("UTS:", "").strip()
                # item['department'] = department
                # print("item['department']: ", item['department'])

                if item['location'].lower() != "online":
                    if "This course is not offered for study on-campus to international students with a student visa" not in item['other']:
                        major_list_url = response.xpath("//div[@class='section']//ul[@class='core-units']//a/@href").extract()
                        clear_space(major_list_url)
                        print("major_list_url: ", major_list_url)
                        print(len(major_list_url))

                        if len(major_list_url) == 0:
                            item['url'] = response.url
                            print("item['url']2: ", item['url'])
                            yield item
                        else:
                            for major_url in major_list_url:
                                headers_base = {
                                    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36", }
                                data = requests.get(major_url, headers=headers_base)
                                response_major = etree.HTML(data.text)
                                item['url'] = major_url
                                print("item['url']_major: ", item['url'])

                                programme_major = response_major.xpath("//span[@id='overview']/following-sibling::h2//text()")
                                item['programme_en'] = ''.join(programme_major).strip()
                                print("item['programme_en']_major: ", item['programme_en'])

                                location_major = response_major.xpath(
                                    "//div[@class='studyCampus__location studyCampus__location--active']/h4//text()")
                                item['location'] = ','.join(location_major).strip().strip(',').strip()
                                if item['location'] == "":
                                    item['location'] = location_tmp
                                print("item['location']_major: ", item['location'])

                                overview_en = response_major.xpath(
                                    "//span[@id='overview']/..")
                                overview_en_str = ""
                                if len(overview_en) > 0:
                                    for o in overview_en:
                                        overview_en_str += etree.tostring(o, encoding='unicode', method='html')
                                item['overview_en'] = remove_class(clear_lianxu_space([overview_en_str]))
                                print("item['overview_en']_major: ", item['overview_en'])

                                modules_en = response_major.xpath(
                                    "//h4[contains(text(),'Structure')]|//h4[contains(text(),'Course structure')]|//div[@class='structure-heading']")
                                modules_en_str = ""
                                if len(modules_en) > 0:
                                    for o in modules_en:
                                        modules_en_str += etree.tostring(o, encoding='unicode', method='html')
                                item['modules_en'] = remove_class(clear_lianxu_space([modules_en_str]))
                                print("item['modules_en']_major: ", item['modules_en'])
                                yield item
        except Exception as e:
            with open("scrapySchool_Australian_yan/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

