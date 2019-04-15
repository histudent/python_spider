from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
import re
from scrapySchool_Australian_yan.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_yan.getItem import get_item
from scrapySchool_Australian_yan.getTuition_fee import getTuition_fee
from scrapySchool_Australian_yan.items import ScrapyschoolAustralianYanItem
from scrapySchool_Australian_yan.remove_tags import remove_class
from scrapySchool_Australian_yan.getStartDate import getStartDateMonth
from scrapySchool_Australian_yan.getDuration import getIntDuration
from scrapySchool_Australian_yan.getIELTS import get_ielts
from w3lib.html import remove_tags
from lxml import etree
import requests

class DeakinUniversity_PSpider(scrapy.Spider):
    name = "DeakinUniversity_P"
    # start_urls = ["http://www.deakin.edu.au/courses/find-a-course"]
#     start_urls = ["http://www.deakin.edu.au/course/master-accounting-and-international-finance-international",
# "http://www.deakin.edu.au/course/master-accounting-and-law-international",
# "http://www.deakin.edu.au/course/master-architecture-international",
# "http://www.deakin.edu.au/course/master-architecture-design-management-international",
# "http://www.deakin.edu.au/course/master-arts-international-relations-international",
# "http://www.deakin.edu.au/course/master-arts-writing-and-literature-international",
# "http://www.deakin.edu.au/course/master-biotechnology-bioinformatics-international",
# "http://www.deakin.edu.au/course/master-business-sport-management-international",
# "http://www.deakin.edu.au/course/master-business-administration-international",
# "http://www.deakin.edu.au/course/master-business-administration-healthcare-management-international",
# "http://www.deakin.edu.au/course/international-master-business-administration-international",
# "http://www.deakin.edu.au/course/master-business-analytics-international",
# "http://www.deakin.edu.au/course/master-clinical-exercise-physiology-international",
# "http://www.deakin.edu.au/course/master-commerce-international",
# "http://www.deakin.edu.au/course/master-communication-international",
# "http://www.deakin.edu.au/course/master-construction-management-international",
# "http://www.deakin.edu.au/course/master-construction-management-professional-international",
# "http://www.deakin.edu.au/course/master-creative-arts-international",
# "http://www.deakin.edu.au/course/master-cultural-heritage-international",
# "http://www.deakin.edu.au/course/master-data-analytics-international",
# "http://www.deakin.edu.au/course/master-dietetics-international",
# "http://www.deakin.edu.au/course/master-education-international",
# "http://www.deakin.edu.au/course/master-financial-planning-international",
# "http://www.deakin.edu.au/course/master-health-economics-international",
# "http://www.deakin.edu.au/course/master-health-promotion-international",
# "http://www.deakin.edu.au/course/master-health-and-human-services-management-international",
# "http://www.deakin.edu.au/course/master-humanitarian-assistance-international",
# "http://www.deakin.edu.au/course/master-information-systems-international",
# "http://www.deakin.edu.au/course/master-information-technology-international",
# "http://www.deakin.edu.au/course/master-information-technology-professional-international",
# "http://www.deakin.edu.au/course/master-international-accounting-international",
# "http://www.deakin.edu.au/course/master-international-finance-international",
# "http://www.deakin.edu.au/course/master-landscape-architecture-international",
# "http://www.deakin.edu.au/course/master-laws-international",
# "http://www.deakin.edu.au/course/master-marketing-international",
# "http://www.deakin.edu.au/course/master-nutrition-and-population-health-international",
# "http://www.deakin.edu.au/course/master-professional-accounting-international",
# "http://www.deakin.edu.au/course/master-professional-accounting-and-finance-international",
# "http://www.deakin.edu.au/course/master-psychology-clinical-international",
# "http://www.deakin.edu.au/course/master-psychology-organisational-international",
# "http://www.deakin.edu.au/course/master-public-health-international",
# "http://www.deakin.edu.au/course/master-science-research-international",
# "http://www.deakin.edu.au/course/master-sustainability-international",
# "http://www.deakin.edu.au/course/master-teaching-early-childhood-international",
# "http://www.deakin.edu.au/course/master-teaching-primary-and-early-childhood-international",
# "http://www.deakin.edu.au/course/master-teaching-primary-and-secondary-international",
# "http://www.deakin.edu.au/course/master-teaching-primary-international",
# "http://www.deakin.edu.au/course/master-teaching-secondary-international",
# "http://www.deakin.edu.au/course/master-teaching-english-to-speakers-other-languages-international", ]
#     start_urls = ["https://www.deakin.edu.au/course/master-dietetics-international"]
#     start_urls = ["http://www.deakin.edu.au/course/master-cyber-security-international?u"]
    # 2019.03.18星期一 数据更新
    start_urls = ["https://www.deakin.edu.au/course/master-architecture-international",
"https://www.deakin.edu.au/course/master-architecture-design-management-international",
"https://www.deakin.edu.au/course/master-arts-international-relations-international",
"https://www.deakin.edu.au/course/master-arts-writing-and-literature-international",
"https://www.deakin.edu.au/course/master-biotechnology-bioinformatics-international",
"https://www.deakin.edu.au/course/master-business-sport-management-international",
"https://www.deakin.edu.au/course/master-business-administration-international",
"https://www.deakin.edu.au/course/master-business-administration-healthcare-management-international",
"https://www.deakin.edu.au/course/international-master-business-administration-international",
"https://www.deakin.edu.au/course/master-business-analytics-international",
"https://www.deakin.edu.au/course/master-clinical-exercise-physiology-international",
"https://www.deakin.edu.au/course/master-commerce-international",
"https://www.deakin.edu.au/course/master-communication-international",
"https://www.deakin.edu.au/course/master-construction-management-international",
"https://www.deakin.edu.au/course/master-construction-management-professional-international",
"https://www.deakin.edu.au/course/master-creative-arts-international",
"https://www.deakin.edu.au/course/master-cultural-heritage-international",
"https://www.deakin.edu.au/course/master-cyber-security-international",
"https://www.deakin.edu.au/course/master-cyber-security-professional-international",
"https://www.deakin.edu.au/course/master-data-science-international",
"https://www.deakin.edu.au/course/master-dietetics-international",
"https://www.deakin.edu.au/course/master-education-international",
"https://www.deakin.edu.au/course/master-financial-planning-international",
"https://www.deakin.edu.au/course/master-health-economics-international",
"https://www.deakin.edu.au/course/master-health-promotion-international",
"https://www.deakin.edu.au/course/master-health-and-human-services-management-international",
"https://www.deakin.edu.au/course/master-humanitarian-assistance-international",
"https://www.deakin.edu.au/course/master-humanitarian-assistance2018-international",
"https://www.deakin.edu.au/course/master-information-systems-international",
"https://www.deakin.edu.au/course/master-information-technology-international",
"https://www.deakin.edu.au/course/master-information-technology-professional-international",
"https://www.deakin.edu.au/course/master-international-accounting-international",
"https://www.deakin.edu.au/course/master-international-finance-international",
"https://www.deakin.edu.au/course/master-international-and-community-development-international",
"https://www.deakin.edu.au/course/master-landscape-architecture-international",
"https://www.deakin.edu.au/course/master-laws-international",
"https://www.deakin.edu.au/course/master-marketing-international",
"https://www.deakin.edu.au/course/master-nutrition-and-population-health-international",
"https://www.deakin.edu.au/course/master-professional-accounting-international",
"https://www.deakin.edu.au/course/master-professional-accounting-and-finance-international",
"https://www.deakin.edu.au/course/master-professional-accounting-and-law-international",
"https://www.deakin.edu.au/course/master-psychology-clinical-international",
"https://www.deakin.edu.au/course/master-psychology-organisational-international",
"https://www.deakin.edu.au/course/master-public-health-international",
"https://www.deakin.edu.au/course/master-sustainability-international",
"https://www.deakin.edu.au/course/master-teaching-early-childhood-international",
"https://www.deakin.edu.au/course/master-teaching-primary-and-early-childhood-international",
"https://www.deakin.edu.au/course/master-teaching-primary-and-secondary-international",
"https://www.deakin.edu.au/course/master-teaching-primary-international",
"https://www.deakin.edu.au/course/master-teaching-secondary-international",
"https://www.deakin.edu.au/course/master-teaching-english-to-speakers-other-languages-international", ]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        item = get_item(ScrapyschoolAustralianYanItem)
        item['university'] = "Deakin University"
        # item['country'] = 'Australia'
        # item['website'] = 'http://www.deakin.edu.au'
        item['degree_type'] = 2
        item['teach_time'] = 'coursework'
        print("===========================")
        print(response.url)
        # 组合字典
        links = ["http://www.deakin.edu.au/course/master-accounting-and-international-finance-international",
                 "http://www.deakin.edu.au/course/master-accounting-and-law-international",
                 "http://www.deakin.edu.au/course/master-architecture-international",
                 "http://www.deakin.edu.au/course/master-architecture-design-management-international",
                 "http://www.deakin.edu.au/course/master-arts-international-relations-international",
                 "http://www.deakin.edu.au/course/master-arts-writing-and-literature-international",
                 "http://www.deakin.edu.au/course/master-biotechnology-bioinformatics-international",
                 "http://www.deakin.edu.au/course/master-business-sport-management-international",
                 "http://www.deakin.edu.au/course/master-business-administration-international",
                 "http://www.deakin.edu.au/course/master-business-administration-healthcare-management-international",
                 "http://www.deakin.edu.au/course/international-master-business-administration-international",
                 "http://www.deakin.edu.au/course/master-business-analytics-international",
                 "http://www.deakin.edu.au/course/master-clinical-exercise-physiology-international",
                 "http://www.deakin.edu.au/course/master-commerce-international",
                 "http://www.deakin.edu.au/course/master-communication-international",
                 "http://www.deakin.edu.au/course/master-construction-management-international",
                 "http://www.deakin.edu.au/course/master-construction-management-professional-international",
                 "http://www.deakin.edu.au/course/master-creative-arts-international",
                 "http://www.deakin.edu.au/course/master-cultural-heritage-international",
                 "http://www.deakin.edu.au/course/master-data-analytics-international",
                 "http://www.deakin.edu.au/course/master-dietetics-international",
                 "http://www.deakin.edu.au/course/master-education-international",
                 "http://www.deakin.edu.au/course/master-financial-planning-international",
                 "http://www.deakin.edu.au/course/master-health-economics-international",
                 "http://www.deakin.edu.au/course/master-health-promotion-international",
                 "http://www.deakin.edu.au/course/master-health-and-human-services-management-international",
                 "http://www.deakin.edu.au/course/master-humanitarian-assistance-international",
                 "http://www.deakin.edu.au/course/master-information-systems-international",
                 "http://www.deakin.edu.au/course/master-information-technology-international",
                 "http://www.deakin.edu.au/course/master-information-technology-professional-international",
                 "http://www.deakin.edu.au/course/master-international-accounting-international",
                 "http://www.deakin.edu.au/course/master-international-finance-international",
                 "http://www.deakin.edu.au/course/master-landscape-architecture-international",
                 "http://www.deakin.edu.au/course/master-laws-international",
                 "http://www.deakin.edu.au/course/master-marketing-international",
                 "http://www.deakin.edu.au/course/master-nutrition-and-population-health-international",
                 "http://www.deakin.edu.au/course/master-professional-accounting-international",
                 "http://www.deakin.edu.au/course/master-professional-accounting-and-finance-international",
                 "http://www.deakin.edu.au/course/master-psychology-clinical-international",
                 "http://www.deakin.edu.au/course/master-psychology-organisational-international",
                 "http://www.deakin.edu.au/course/master-public-health-international",
                 "http://www.deakin.edu.au/course/master-science-research-international",
                 "http://www.deakin.edu.au/course/master-sustainability-international",
                 "http://www.deakin.edu.au/course/master-teaching-early-childhood-international",
                 "http://www.deakin.edu.au/course/master-teaching-primary-and-early-childhood-international",
                 "http://www.deakin.edu.au/course/master-teaching-primary-and-secondary-international",
                 "http://www.deakin.edu.au/course/master-teaching-primary-international",
                 "http://www.deakin.edu.au/course/master-teaching-secondary-international",
                 "http://www.deakin.edu.au/course/master-teaching-english-to-speakers-other-languages-international", ]
        programme_dict = {}
        programme_list = ["Master of Accounting and International Finance",
                          "Master of Accounting and Law",
                          "Master of Architecture",
                          "Master of Architecture (Design Management)",
                          "Master of Arts (International Relations)",
                          "Master of Arts (Writing and Literature)",
                          "Master of Biotechnology and Bioinformatics",
                          "Master of Business (Sport Management)",
                          "Master of Business Administration",
                          "Master of Business Administration (Healthcare Management)",
                          "Master of Business Administration (International)",
                          "Master of Business Analytics",
                          "Master of Clinical Exercise Physiology",
                          "Master of Commerce",
                          "Master of Communication",
                          "Master of Construction Management",
                          "Master of Construction Management (Professional)",
                          "Master of Creative Arts",
                          "Master of Cultural Heritage",
                          "Master of Data Analytics",
                          "Master of Dietetics",
                          "Master of Education",
                          "Master of Financial Planning",
                          "Master of Health Economics",
                          "Master of Health Promotion",
                          "Master of Health and Human Services Management",
                          "Master of Humanitarian Assistance",
                          "Master of Information Systems",
                          "Master of Information Technology",
                          "Master of Information Technology (Professional)",
                          "Master of International Accounting",
                          "Master of International Finance",
                          "Master of Landscape Architecture",
                          "Master of Laws",
                          "Master of Marketing",
                          "Master of Nutrition and Population Health",
                          "Master of Professional Accounting",
                          "Master of Professional Accounting and Finance",
                          "Master of Psychology (Clinical)",
                          "Master of Psychology (Organisational)",
                          "Master of Public Health",
                          "Master of Science (Research)",
                          "Master of Sustainability",
                          "Master of Teaching (Early Childhood)",
                          "Master of Teaching (Primary and Early Childhood)",
                          "Master of Teaching (Primary and Secondary)",
                          "Master of Teaching (Primary)",
                          "Master of Teaching (Secondary)",
                          "Master of Teaching English to Speakers of Other Languages", ]
        for link in range(len(links)):
            url = links[link]
            programme_dict[url] = programme_list[link]
        item['major_type1'] =programme_dict.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            programme = response.xpath("//div[@class='module__banner-title']/h1//text()").extract()
            clear_space(programme)
            item['degree_name'] = ''.join(programme).strip()
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

                # //div[@class='module__summary--items']/div[1]/div[2]
                ielts = response.xpath("//h3[contains(text(),'English language requirements')]/../following-sibling::*[1]//text()").extract()
                clear_space(ielts)
                item['ielts_desc'] = ''.join(ielts).strip()
                # print("item['ielts_desc']: ", item['ielts_desc'])

                ielts_d = get_ielts(item['ielts_desc'])
                item["ielts"] = ielts_d.get('IELTS')
                item["ielts_l"] = ielts_d.get('IELTS_L')
                item["ielts_s"] = ielts_d.get('IELTS_S')
                item["ielts_r"] = ielts_d.get('IELTS_R')
                item["ielts_w"] = ielts_d.get('IELTS_W')
                # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

                duration = response.xpath("//h3[contains(text(),'Duration')]/../following-sibling::div//text()").extract()
                clear_space(duration)
                # print("duration: ", duration)
                duration_re = re.findall(r".*full[\s\-]time", ''.join(duration).strip())
                item['duration'] = ''.join(duration_re).strip()
                # if item['duration'] == "":
                #     print("***duration 为空")
                # print("item['duration']: ", item['duration'])

                location = response.xpath("//div[@class='module__summary--icon-wrapper']//h3[@class='course__subheading'][contains(text(),'Campuses')]/../following-sibling::div//text()").extract()
                clear_space(location)
                item['location'] = ' '.join(location).strip()
                location_tmp = item['location']
                # print("item['location']: ", item['location'])

                # //div[@id='navigation__course']/following-sibling::div
                overview = response.xpath("//h2[contains(text(),'Course information')]/../..").extract()
                item['degree_overview_en'] = remove_class(clear_lianxu_space(overview))
                # if item['degree_overview_en'] == "":
                #     print("***degree_overview_en 为空")
                # print("item['degree_overview_en']: ", item['degree_overview_en'])

                modules = response.xpath("//div[@id='module__course-structure']").extract()
                item['modules_en'] = remove_class(clear_lianxu_space(modules))
                # if item['modules_en'] == "":
                #     print("***modules_en 为空")
                # print("item['modules_en']: ", item['modules_en'])

                start_date = response.xpath(
                    "//li[contains(text(),'Start date:')]//text()").extract()
                clear_space(start_date)
                # print("start_date: ", start_date)
                item['start_date'] = getStartDateMonth(' '.join(start_date).strip())
                # print("item['start_date']: ", item['start_date'])

                entry_requirements = response.xpath("//div[@data-section='entry requirements']").extract()
                item['rntry_requirements_en'] = remove_class(clear_lianxu_space(entry_requirements))
                # if item['rntry_requirements_en'] == "":
                #     print("***rntry_requirements_en 为空")
                # print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

                # //div[@data-section='fees and scholarships']
                tuition_fee = response.xpath("//div[@class='module__content-panel']//div[@class='module__key-information--item-content']/text()").extract()
                clear_space(tuition_fee)
                # print("tuition_fee: ", tuition_fee)
                tuition_fee = getTuition_fee(''.join(tuition_fee))
                item['tuition_fee'] = tuition_fee
                if item['tuition_fee'] == 0:
                    item['tuition_fee'] = None
                # print("item['tuition_fee']: ", item['tuition_fee'])

                career = response.xpath("//div[@data-section='graduate outcomes']|//div[@data-section='graduate outcomes']/following-sibling::div[1]|"
                                        "//h3[contains(text(),'Career outcomes')]/..|//h3[contains(text(),'Career outcomes')]/../following-sibling::div[1]").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career))
                # if item['career_en'] == "":
                #     print("***career_en 为空")
                # print("item['career_en']: ", item['career_en'])

                # //div[@data-section='application information']/following-sibling::div[2]
                how_to_apply = response.xpath(
                    "//h3[contains(text(),'How to apply')]/../..").extract()
                item['apply_desc_en'] = remove_class(clear_lianxu_space(how_to_apply))
                # if item['apply_desc_en'] == "":
                #     print("***apply_desc_en 为空")
                # print("item['apply_desc_en']: ", item['apply_desc_en'])

                work_experience_desc_en = re.findall(r"<.{1,100}work\sexperience.{1,100}>", response.text)
                item['work_experience_desc_en'] = "<p>"+remove_tags(remove_class(clear_lianxu_space(work_experience_desc_en)))+"</p>"
                item['work_experience_desc_en'] = item['work_experience_desc_en'].replace("<p></p>", "").strip()
                if item['work_experience_desc_en'] != "":
                    print("item['work_experience_desc_en']: ", item['work_experience_desc_en'])
                # print(item)


                major_list_url = response.xpath("//h3[contains(text(), 'Specialisations')]/..//a/@href").extract()
                clear_space(major_list_url)
                print("major_list_url: ", major_list_url)
                print(len(major_list_url))

                major_url_l = []
                for major_url in major_list_url:
                    if "specialisation" in major_url:
                        major_url_l.append(major_url)
                print("major_url_l: ", major_url_l)
                print(len(major_url_l))
                if len(major_url_l) == 0:
                    item['url'] = response.url
                    print("item['url']2: ", item['url'])
                    yield item
                else:
                    for major_url in major_url_l:
                        headers_base = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",}
                        data = requests.get(major_url, headers=headers_base)
                        response_major = etree.HTML(data.text)
                        item['url'] = major_url
                        print("item['url']_major: ", item['url'])

                        programme_major = response_major.xpath("//div[@class='module__banner-title']/h1//text()")
                        item['programme_en'] = ''.join(programme_major).strip()
                        print("item['programme_en']_major: ", item['programme_en'])

                        location_major = response_major.xpath("//*[contains(text(),'Campuses')]/../following-sibling::div[1]//text()")
                        item['location'] = ''.join(location_major).strip()
                        if item['location'] == "":
                            item['location'] = location_tmp
                        # print("item['location']_major: ", item['location'])

                        overview_en = response_major.xpath(
                            "//h2[contains(text(),'Overview')]/../..")
                        overview_en_str = ""
                        if len(overview_en) > 0:
                            for o in overview_en:
                                overview_en_str += etree.tostring(o, encoding='unicode', method='html')
                        item['overview_en'] = remove_class(clear_lianxu_space([overview_en_str]))
                        # print("item['overview_en']_major: ", item['overview_en'])

                        modules_en = response_major.xpath(
                            "//h2[contains(text(),'Explore units')]/../..")
                        modules_en_str = ""
                        if len(modules_en) > 0:
                            for o in modules_en:
                                modules_en_str += etree.tostring(o, encoding='unicode', method='html')
                        item['modules_en'] = remove_class(clear_lianxu_space([modules_en_str]))
                        # print("item['modules_en']_major: ", item['modules_en'])
                        yield item
                        # else:
                        #     item['url'] = response.url
                        #     print("item['url']1: ", item['url'])
                        #     yield item
        except Exception as e:
            with open("scrapySchool_Australian_yan/error/" + item['university'] + str(item['degree_type']) + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

