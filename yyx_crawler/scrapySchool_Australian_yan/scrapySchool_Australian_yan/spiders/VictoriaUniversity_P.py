# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_Australian_yan.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_yan.getItem import get_item
from scrapySchool_Australian_yan.getTuition_fee import getTuition_fee
from scrapySchool_Australian_yan.items import ScrapyschoolAustralianYanItem
from scrapySchool_Australian_yan.remove_tags import remove_class
from scrapySchool_Australian_yan.getStartDate import getStartDate
from scrapySchool_Australian_yan.getDuration import getIntDuration
from scrapySchool_Australian_yan.getIELTS import get_ielts


# 2019.03.18 星期一 数据更新
class VictoriaUniversity_PSpider(CrawlSpider):
    name = "VictoriaUniversity_P"
    start_urls = ["https://www.vu.edu.au/courses/search?f%5B0%5D=field_unit_lev%3Apostgrad&iam=non-resident&page=0&query="]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    rules = (
        # Rule(page_link, callback='get_programme_link', follow=True),
        Rule(LinkExtractor(allow=r'page=\d+'), follow=True, callback='page'),
        Rule(LinkExtractor(restrict_xpaths="//html//div[@class='view-content']//li//a"), follow=True, callback='parse_data'),
    )
    # def page(self, response):
    #     print(response.url)
    #     # links = ["https://www.vu.edu.au/courses/international/HRAT",
    #     #          "https://www.vu.edu.au/courses/international/HREH"]
    #     for link in links:
    #         yield scrapy.Request(link, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianYanItem)
        item['university'] = "Victoria University"
        # item['country'] = 'Australia'
        # item['website'] = 'https://www.vu.edu.au/'
        item['url'] = response.url
        item['degree_type'] = 2
        item['teach_time'] = 'coursework'
        print("===========================")
        print(response.url)
        pro = ["Graduate Certificate in Enterprise and Resource Planning Systems",
"Graduate Certificate in International Business",
"Graduate Diploma in Education",
"Graduate Diploma in Project Management",
"Master of Business (Accounting)/Master of Finance",
"Master of Business (Enterprise Resource Planning Systems)/ Master of Supply Chain Management",
"Master of Business (Enterprise Resource Planning Systems)/Master of Business Analytics",
"Master of Business (Finance)",
"Master of Business (International Business)",
"Master of Counselling",
"Master of Engineering (Building Fire Safety and Risk Engineering)",
"Master of Finance",
"Master of Industrial Relations and Human Resource Management",
"Master of International Business",
"Master of Management",
"Master of Marketing",
"Master of Supply Chain Management",
"Master of Teaching (Secondary Education)",
"Master of Tourism and Destination Management", ]
        uu = ["https://www.vu.edu.au/courses/international/BTEN",
"https://www.vu.edu.au/courses/international/BTIB",
"https://www.vu.edu.au/courses/international/EGED",
"https://www.vu.edu.au/courses/international/NGPM",
"https://www.vu.edu.au/courses/international/BMDD",
"https://www.vu.edu.au/courses/international/BMDB",
"https://www.vu.edu.au/courses/international/BMDA",
"https://www.vu.edu.au/courses/international/BMFN",
"https://www.vu.edu.au/courses/international/BMIA",
"https://www.vu.edu.au/courses/international/AMPE",
"https://www.vu.edu.au/courses/international/EMQB",
"https://www.vu.edu.au/courses/international/BMFF",
"https://www.vu.edu.au/courses/international/BMIH",
"https://www.vu.edu.au/courses/international/BMIB",
"https://www.vu.edu.au/courses/international/BMMM",
"https://www.vu.edu.au/courses/international/BMKM",
"https://www.vu.edu.au/courses/international/BMSP",
"https://www.vu.edu.au/courses/international/EMES",
"https://www.vu.edu.au/courses/international/BMTD", ]
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

            pro_re = re.findall(r"Master", item['degree_name'])
            # print("pre_re: ", pro_re)
            if len(pro_re) < 2 and "Graduate" not in item['degree_name']:
                programme_re = re.findall(r"\(.+\)", item['degree_name'])
                if len(programme_re) > 0:
                    item['programme_en'] = ''.join(programme_re).replace("(", "").replace(")", "").strip()
                else:
                    item['programme_en'] = item['degree_name'].replace("Master of", "").strip()
                print("item['programme_en']: ", item['programme_en'])

                department = response.xpath("//div[@class='field field-name-field-college field-type-link-field field-label-inline clearfix']//div[@class='field-items']//text()").extract()
                clear_space(department)
                item['department'] = ''.join(department).strip()
                print("item['department']: ", item['department'])

                start_date = response.xpath(
                    "//div[@class='field field-essentials-intake']//div[@class='field-item']//text()|"
                    "//strong[contains(text(),'Intakes:')]/../div//text()").extract()
                clear_space(start_date)
                # print("start_date: ", start_date)
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
                print("item['start_date']: ", item['start_date'])

                duration = response.xpath(
                    "//div[@class='field field-essentials-duration']//div[@class='field-item']//text()|"
                    "//strong[contains(text(),'Duration:')]/../div//text()").extract()
                clear_space(duration)
                item['duration'] = ''.join(duration).strip()
                print("item['duration']: ", item['duration'])

                location = response.xpath(
                    "//div[@class='field field-essentials-locations']//div[@class='field-items']//text()|"
                    "//strong[contains(text(),'Location:')]/../div//text()").extract()
                clear_space(location)
                item['location'] = ''.join(location).strip()
                print("item['location']: ", item['location'])

                tuition_fee = response.xpath(
                    "//div[@class='field field-essentials-short-fees']//div[@class='field-item']//text()|"
                    # "//strong[contains(text(),'Fees:')]/../div/text()|"
                    "//strong[contains(text(),'Fees:')]/../div//text()").extract()
                print("tuition_fee: ", tuition_fee)
                clear_space(tuition_fee)
                tuition_fee_str = ''.join(tuition_fee).strip()
                tuition_fee_re1 = re.findall(r"2019[\w\W]*?\d+,\d+", tuition_fee_str)
                tuition_fee_re = re.findall(r"\d+,\d+", ''.join(tuition_fee_re1))
                item['tuition_fee'] = ''.join(tuition_fee_re).replace(",", "").strip()
                print("item['tuition_fee']: ", item['tuition_fee'])

                overview = response.xpath(
                    "//div[@id='overview']").extract()
                item['degree_overview_en'] = remove_class(clear_lianxu_space(overview))
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
                # print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

                how_to_apply = response.xpath(
                    "//div[@id='apply-now']").extract()
                item['apply_desc_en'] = remove_class(clear_lianxu_space(how_to_apply))
                # print("item['apply_desc_en']: ", item['apply_desc_en'])

                ielts_desc_re = re.findall(r"IELTS.{1,120}", item['rntry_requirements_en'])
                item['ielts_desc'] = ''.join(ielts_desc_re).strip()
                print("item['ielts_desc']: ", item['ielts_desc'])

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
                print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                        item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))
                # item['ielts_desc'] = "Overall score of 6.5 (no band less than 6.0)"
                item['toefl'] = "79"
                item['toefl_l'] = "19"
                item['toefl_s'] = "19"
                item['toefl_r'] = "18"
                item['toefl_w'] = "22"
                yield item
        except Exception as e:
            with open("scrapySchool_Australian_yan/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

