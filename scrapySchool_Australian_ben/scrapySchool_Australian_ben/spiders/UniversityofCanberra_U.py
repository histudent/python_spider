# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_Australian_ben.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_ben.getItem import get_item
from scrapySchool_Australian_ben.getTuition_fee import getTuition_fee
from scrapySchool_Australian_ben.items import ScrapyschoolAustralianBenItem
from scrapySchool_Australian_ben.remove_tags import remove_class
from scrapySchool_Australian_ben.getStartDate import getStartDate
from scrapySchool_Australian_ben.getDuration import getIntDuration
from scrapySchool_Australian_ben.getIELTS import get_ielts

# 2019/03/26 星期二 数据更新
class UniversityofCanberra_USpider(CrawlSpider):
    name = "UniversityofCanberra_U"
    start_urls = ["https://search.canberra.edu.au/s/search.html?collection=courses&form=course-search&profile=_default&query=!padre&course-search-widget__submit=&meta_C_and=COURSE&sort=metaH&f.Attendance+Type%7CJ=Full+Time&f.Type|B=undergraduate&start_rank=1"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    rules = (
        # Rule(page_link, callback='get_programme_link', follow=True),
        Rule(LinkExtractor(allow=r'start_rank=\d+'), follow=True, callback='page'),
        Rule(LinkExtractor(restrict_xpaths="//table[@class='table course_results']/tbody/tr/td//a[contains(text(), 'Bachelor')]", attrs=r"title"), follow=True, callback='parse_data'),
    )

#     def page(self, response):
#         links = ["http://www.canberra.edu.au/coursesandunits/course?course_cd=943AA&version_number=3&title=Bachelor-of-Applied-Economics&location=BRUCE&rank=AAA&faculty=Faculty-of-Business,-Government---Law&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=429AA&version_number=6&title=Bachelor-of-Arts&location=BRUCE&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=912AA&version_number=6&title=Bachelor-of-Arts-in-Architecture&location=BRUCE&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=793AA&version_number=8&title=Bachelor-of-Arts-in-International-Studies&location=BRUCE&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=183JA&version_number=2&title=Bachelor-of-Australian-Politics-and-Public-Policy&location=BRUCE&rank=AAA&faculty=Faculty-of-Business,-Government---Law&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=762AA&version_number=4&title=Bachelor-of-Commerce&location=GBCA-MELB&rank=AAA&faculty=Faculty-of-Business,-Government---Law&year=2019",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=211JA&version_number=1&title=Bachelor-of-Communication-in-Advertising&location=BRUCE&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=213JA&version_number=1&title=Bachelor-of-Communication-in-Media-and-Public-Affairs&location=BRUCE&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=214JA&version_number=1&title=Bachelor-of-Communication-in-Public-Relations&location=BRUCE&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=206JA&version_number=2&title=Bachelor-of-Design&location=TQB-SB&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=344JA&version_number=1&title=Bachelor-of-Engineering-in-Network-and-Software-Engineering-(Honours)&location=BRUCE&rank=AAB&faculty=Faculty-of-Science-and-Technology&year=2019",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=344JA&version_number=1&title=Bachelor-of-Engineering-in-Network-and-Software-Engineering-(Honours)&location=BRUCE&rank=AAB&faculty=Faculty-of-Science-and-Technology&year=2019",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=208JA&version_number=2&title=Bachelor-of-Entrepreneurship-and-Innovation&location=BRUCE&rank=AAA&faculty=Faculty-of-Business,-Government---Law&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=301JA&version_number=1&title=Bachelor-of-Film-Production&location=BRUCE&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=184JA&version_number=2&title=Bachelor-of-Finance&location=BRUCE&rank=AAA&faculty=Faculty-of-Business,-Government---Law&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=164JA&version_number=3&title=Bachelor-of-Graphic-Design&location=BRUCE&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=317JA&version_number=2&title=Bachelor-of-Health-Science&location=BRUCE&rank=AAA&faculty=Faculty-of-Health&year=2019",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=317JA&version_number=2&title=Bachelor-of-Health-Science&location=BRUCE&rank=AAA&faculty=Faculty-of-Health&year=2019",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=316JA&version_number=2&title=Bachelor-of-Health-Studies&location=BRUCE&rank=AAA&faculty=Faculty-of-Health&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=215JA&version_number=2&title=Bachelor-of-Heritage,-Museums-and-Conservation&location=BRUCE&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=185JA&version_number=3&title=Bachelor-of-Human-Resource-Management&location=BRUCE&rank=AAA&faculty=Faculty-of-Business,-Government---Law&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=288JA&version_number=3&title=Bachelor-of-Industrial-Design&location=BRUCE&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=289JA&version_number=2&title=Bachelor-of-Interior-Architecture&location=TQB-SB&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=186JA&version_number=2&title=Bachelor-of-International-Business&location=BRUCE&rank=AAA&faculty=Faculty-of-Business,-Government---Law&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=320JA&version_number=1&title=Bachelor-of-Journalism&location=BRUCE&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=290JA&version_number=2&title=Bachelor-of-Landscape-Design&location=BRUCE&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=394AA&version_number=6&title=Bachelor-of-Management&location=BRUCE&rank=AAA&faculty=Faculty-of-Business,-Government---Law&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=187JA&version_number=2&title=Bachelor-of-Marketing-Management&location=BRUCE&rank=AAA&faculty=Faculty-of-Business,-Government---Law&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=985AA&version_number=1&title=Bachelor-of-Media-Arts-and-Production&location=TQB-SB&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=325JA&version_number=1&title=Bachelor-of-Primary-Education-(Graduate-Entry)&location=BRUCE&rank=AAA&faculty=Faculty-of-Education&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=210JA&version_number=2&title=Bachelor-of-Public-Administration&location=BRUCE&rank=AAA&faculty=Faculty-of-Business,-Government---Law&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=188JA&version_number=2&title=Bachelor-of-Social-Science&location=BRUCE&rank=AAA&faculty=Faculty-of-Business,-Government---Law&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=689AA&version_number=6&title=Bachelor-of-Sports-Media&location=BRUCE&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=267JA&version_number=1&title=Bachelor-of-Web-Design-and-Production&location=TQB-SB&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018",
# "http://www.canberra.edu.au/coursesandunits/course?course_cd=984AA&version_number=2&title=Bachelor-of-Writing&location=BRUCE&rank=AAA&faculty=Faculty-of-Arts-and-Design&year=2018", ]
#         for url in links:
#             yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "University of Canberra"
        # item['country'] = 'Australia'
        # item['website'] = 'https://www.vu.edu.au/'
        item['url'] = response.url
        item['degree_type'] = 1
        print("===========================")
        print(response.url)

        # item['major_type1'] = programme_dict.get(response.url)
        # print("item['major_type1']: ", item['major_type1'])
        try:
            # //h1[@class='page-header']
            programme = response.xpath("//h1[@class='course_title']//text()").extract()
            clear_space(programme)
            degree_name_str = ''.join(programme).strip()
            degree_name_re = re.findall(r"-.*", degree_name_str)
            item['degree_name'] = degree_name_str.replace(''.join(degree_name_re), '').strip()
            print("item['degree_name']: ", item['degree_name'])

            pro_re = re.findall(r"Bachelor", item['degree_name'])
            # print("pre_re: ", pro_re)
            if len(pro_re) < 2 and "online" not in item['degree_name'].lower():
                programme_re = re.findall(r"\(.+\)", item['degree_name'])
                if len(programme_re) > 0:
                    item['programme_en'] = ''.join(programme_re).replace("(", "").replace(")", "").strip()
                else:
                    item['programme_en'] = item['degree_name'].replace("Bachelor of", "").strip()
                print("item['programme_en']: ", item['programme_en'])

                location = response.xpath(
                    "//th[contains(text(),'Location:')]/following-sibling::td//text()").extract()
                clear_space(location)
                item['location'] = ''.join(location).strip()
                # print("item['location']: ", item['location'])

                department = response.xpath("//th[contains(text(),'Faculty:')]/following-sibling::td//text()").extract()
                clear_space(department)
                item['department'] = ''.join(department).strip()
                # print("item['department']: ", item['department'])

                ielts_desc_re = response.xpath(
                    "//th[contains(text(),'English Language Requirements:')]/following-sibling::td//text()").extract()
                item['ielts_desc'] = ''.join(ielts_desc_re).strip()
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
                elif len(ieltlsrw) == 5:
                    item["ielts"] = ieltlsrw[0]
                    item["ielts_l"] = ieltlsrw[1]
                    item["ielts_s"] = ieltlsrw[4]
                    item["ielts_r"] = ieltlsrw[2]
                    item["ielts_w"] = ieltlsrw[3]
                # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

                tuition_fee = response.xpath(
                    "//div[@id='fees']//tr[2]/td[3]//text()").extract()
                clear_space(tuition_fee)
                # print("tuition_fee: ", tuition_fee)
                tuition_fee_str = ''.join(tuition_fee).strip()
                tuition_fee_re = re.findall(r"\d+,\d+", tuition_fee_str)
                item['tuition_fee'] = ''.join(tuition_fee_re).replace(",", "").strip()
                # print("item['tuition_fee']: ", item['tuition_fee'])

                overview = response.xpath(
                    "//h2[contains(text(),'Career opportunities')]/preceding-sibling::*").extract()
                if len(overview) == 0:
                    overview = response.xpath(
                        "//div[@class='collapsible-section']/preceding-sibling::*").extract()
                item['overview_en'] = item['degree_overview_en'] = remove_class(clear_lianxu_space(overview))
                # print("item['degree_overview_en']: ", item['degree_overview_en'])

                career = response.xpath(
                    "//h2[contains(text(),'Career opportunities')]|//h2[contains(text(),'Career opportunities')]/following-sibling::*[1]|"
                    "//strong[contains(text(),'Career opportunities')]/..|//strong[contains(text(),'Career opportunities')]/../following-sibling::*[position()<3]").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career))
                # if item['career_en'] == "":
                #     print("***career_en 为空")
                # print("item['career_en']: ", item['career_en'])

                modules = response.xpath(
                    "//h2[contains(text(),'Course Requirements')]|//div[@id='toggle-view']").extract()
                item['modules_en'] = remove_class(clear_lianxu_space(modules))
                # if item['modules_en'] == "":
                #     print("***modules_en 为空")
                # print("item['modules_en']: ", item['modules_en'])

                entry_requirements = response.xpath(
                    "//div[@id='admission']").extract()
                item['rntry_requirements_en'] = remove_class(clear_lianxu_space(entry_requirements))
                # print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

                # how_to_apply = response.xpath(
                #     "//div[@id='apply-now']").extract()
                # item['apply_desc_en'] = remove_class(clear_lianxu_space(how_to_apply))
                # # print("item['apply_desc_en']: ", item['apply_desc_en'])

                yield item
        except Exception as e:
            with open("scrapySchool_Australian_ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

