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
class VictoriaUniversity_USpider(CrawlSpider):
    name = "VictoriaUniversity_U"
    start_urls = ["https://www.vu.edu.au/courses/search?f%5B0%5D=field_unit_lev%3Aundergrad&iam=non-resident&page=0&query="]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    rules = (
        # Rule(page_link, callback='get_programme_link', follow=True),
        Rule(LinkExtractor(allow=r'page=\d+'), follow=True, callback='page'),
        Rule(LinkExtractor(restrict_xpaths="//html//div[@class='view-content']//li//a"), follow=True, callback='parse_data'),
    )
    def page(self, response):
        print(response.url)

    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "Victoria University"
        # item['country'] = 'Australia'
        # item['website'] = 'https://www.vu.edu.au/'
        item['url'] = response.url
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        pro = ["Bachelor of Arts",
"Bachelor of Biomedical and Exercise Science",
"Bachelor of Biomedicine",
"Bachelor of Commerce",
"Bachelor of Community Development",
"Bachelor of Construction Management (Honours)",
"Bachelor of Criminal Justice",
"Bachelor of Criminal Justice and Psychological Studies",
"Bachelor of Early Childhood Education",
"Bachelor of Education Studies",
"Bachelor of Engineering (Honours) (Electrical and Sports Engineering)",
"Bachelor of Human Nutrition",
"Bachelor of Screen Media",
"Bachelor of Social Work (Honours)",
"Bachelor of Sport and Exercise Science (Honours)",
"Bachelor of Sport Science (Human Movement)/Bachelor of Psychological Studies",
"Bachelor of Youth Work",]
        uu = ["https://www.vu.edu.au/courses/international/ABAB",
"https://www.vu.edu.au/courses/international/HBES",
"https://www.vu.edu.au/courses/international/HBBM",
"https://www.vu.edu.au/courses/international/BBCA",
"https://www.vu.edu.au/courses/international/ABCD",
"https://www.vu.edu.au/courses/international/NHCM",
"https://www.vu.edu.au/courses/international/ABCJ",
"https://www.vu.edu.au/courses/international/ABCY",
"https://www.vu.edu.au/courses/international/EBEC",
"https://www.vu.edu.au/courses/international/EBST",
"https://www.vu.edu.au/courses/international/NHES",
"https://www.vu.edu.au/courses/international/HBNT",
"https://www.vu.edu.au/courses/international/ABSN",
"https://www.vu.edu.au/courses/international/ABSX",
"https://www.vu.edu.au/courses/international/SHSP",
"https://www.vu.edu.au/courses/international/SBHP",
"https://www.vu.edu.au/courses/international/ABYW",]
        programme_dict = {}
        for i in range(len(pro)):
            programme_dict[uu[i]] = pro[i]
        item['major_type1'] = programme_dict.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            # //h1[@class='page-header']
            programme = response.xpath("//h1[@class='page-header']//text()").extract()
            clear_space(programme)
            item['degree_name'] = ''.join(programme).strip()
            print("item['degree_name']: ", item['degree_name'])

            pro_re = re.findall(r"Bachelor", item['degree_name'])
            # print("pre_re: ", pro_re)
            if len(pro_re) < 2 and "Graduate" not in item['degree_name']:
                programme_re = re.findall(r"\(.+\)", item['degree_name'])
                if len(programme_re) > 0:
                    if ''.join(programme_re) != "(Honours)":
                        item['programme_en'] = ''.join(programme_re).replace("(", "").replace(")", "").strip()
                    else:
                        item['programme_en'] = item['degree_name'].replace("Bachelor of", "").replace("(Honours)", "").strip()
                else:
                    item['programme_en'] = item['degree_name'].replace("Bachelor of", "").strip()
                print("item['programme_en']: ", item['programme_en'])

                department = response.xpath("//div[@class='field field-name-field-college field-type-link-field field-label-inline clearfix']//div[@class='field-items']//text()").extract()
                clear_space(department)
                item['department'] = ''.join(department).strip()
                print("item['department']: ", item['department'])

                start_date = response.xpath(
                    "//div[@class='field field-essentials-intake']//div[@class='field-item']//text()|"
                    "//strong[contains(text(),'Intakes:')]/../div//text()").extract()
                clear_space(start_date)
                print("start_date: ", start_date)
                monthDict = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06",
                             "july": "07", "august": "08", "september": "09", "october": "10", "november": "11",
                             "december": "12",
                             "jan": "01", "feb": "02", "mar": "03", "apr": "04", "may": "05", "jun": "06",
                             "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12",
                             "sept": "09", }
                start_date_re = re.findall(r"january|february|march|april|may|june|july|febraugustuary|september|october|november|december", ''.join(start_date), re.I)
                start_date_str = ""
                # print(start_date_re)
                if len(start_date_re) > 0:
                    for s in start_date_re:
                        s1 = monthDict.get(s.lower().strip())
                        if s1 is not None:
                            start_date_str += s1 + ","
                start_date_str = start_date_str.replace("0", "").strip().strip(',').strip()
                item['start_date'] = start_date_str
                # print("item['start_date']: ", item['start_date'])

                duration = response.xpath(
                    "//div[@class='field field-essentials-duration']//div[@class='field-item']//text()|"
                    "//strong[contains(text(),'Duration:')]/../div//text()").extract()
                clear_space(duration)
                item['duration'] = ''.join(duration).strip()
                # print("item['duration']: ", item['duration'])

                location = response.xpath(
                    "//div[@class='field field-essentials-locations']//div[@class='field-items']//text()|"
                    "//strong[contains(text(),'Location:')]/../div//text()").extract()
                clear_space(location)
                item['location'] = ','.join(location).strip()
                # print("item['location']: ", item['location'])

                tuition_fee = response.xpath(
                    "//div[@class='field field-essentials-short-fees']//div[@class='field-item']//text()|"
                    "//strong[contains(text(),'Fees:')]/../div//text()").extract()
                clear_space(tuition_fee)
                tuition_fee_str = ''.join(tuition_fee).strip()
                tuition_fee_re = re.findall(r"\d+,\d+", tuition_fee_str)
                item['tuition_fee'] = ''.join(tuition_fee_re).replace(",", "").strip()
                # print("item['tuition_fee']: ", item['tuition_fee'])

                overview = response.xpath(
                    "//div[@id='overview']").extract()
                item['overview_en'] = item['degree_overview_en'] = remove_class(clear_lianxu_space(overview))
                # print("item['degree_overview_en']: ", item['degree_overview_en'])

                career = response.xpath(
                    "//div[@id='careers']").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career))
                # print("item['career_en']: ", item['career_en'])

                modules = response.xpath(
                    "//div[@id='course-structure']").extract()
                item['modules_en'] = remove_class(clear_lianxu_space(modules))
                # print("item['modules_en']: ", item['modules_en'])

                entry_requirements = response.xpath(
                    "//html//article/div[4]").extract()
                item['rntry_requirements_en'] = remove_class(clear_lianxu_space(entry_requirements))
                # print("item['rtry_requirements_en']: ", item['rntry_requirements_en'])

                how_to_apply = response.xpath(
                    "//div[@id='apply-now']").extract()
                item['apply_desc_en'] = remove_class(clear_lianxu_space(how_to_apply))
                # print("item['apply_desc_en']: ", item['apply_desc_en'])

                ielts_desc_re = re.findall(r"IELTS.{1,120}", item['rntry_requirements_en'])
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
                elif  len(ieltlsrw) == 2:
                    item["ielts"] = ieltlsrw[0]
                    item["ielts_l"] = ieltlsrw[1]
                    item["ielts_s"] = ieltlsrw[1]
                    item["ielts_r"] = ieltlsrw[1]
                    item["ielts_w"] = ieltlsrw[1]
                elif  len(ieltlsrw) == 5:
                    item["ielts"] = ieltlsrw[0]
                    item["ielts_l"] = ieltlsrw[1]
                    item["ielts_s"] = ieltlsrw[4]
                    item["ielts_r"] = ieltlsrw[2]
                    item["ielts_w"] = ieltlsrw[3]
                # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))
                # item['ielts_desc'] = "Overall score of 6.5 (no band less than 6.0)"
                item['toefl'] = "67"
                item['toefl_l'] = "12"
                item['toefl_s'] = "18"
                item['toefl_r'] = "15"
                item['toefl_w'] = "21"

                major_list = response.xpath("//div[contains(@class,'field-item even')]//h3[contains(text(),'Majors')]/../../../../../following-sibling::div[contains(@id,'accordion')]//h3/a//text()").extract()
                clear_space(major_list)
                print("major_list: ", major_list)
                print("===", clear_lianxu_space(major_list))
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

