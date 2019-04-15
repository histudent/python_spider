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


class UniversityofCanberra_PSpider(CrawlSpider):
    name = "UniversityofCanberra_P"
    start_urls = ["https://search.canberra.edu.au/s/search.html?collection=courses&form=course-search&profile=_default&query=!padre&course-search-widget__submit=&meta_C_and=COURSE&sort=metaH&f.Type|B=postgraduate&f.Attendance+Type%7CJ=Full+Time&start_rank=1"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    rules = (
        # Rule(page_link, callback='get_programme_link', follow=True),
        Rule(LinkExtractor(allow=r'start_rank=\d+'), follow=True, callback='page'),
        Rule(LinkExtractor(restrict_xpaths="//table[@class='table course_results']/tbody/tr/td//a[contains(text(), 'Master')]", attrs=r"title"), follow=True, callback='parse_data'),
    )
    # def page(self, response):
    #     links = ["http://www.canberra.edu.au/coursesandunits/course?course_cd=979AA&version_number=2&title=Master-of-Arts-in-TESOL-and-Foreign-Language-Teaching&location=BRUCE&rank=CCC&faculty=Faculty-of-Education&year=2019",
    #              "http://www.canberra.edu.au/coursesandunits/course?course_cd=246JA&version_number=4&title=Master-of-Teaching&location=BRUCE&rank=CCC&faculty=Faculty-of-Education&year=2019"]
    #     for link in links:
    #         yield scrapy.Request(link, callback=self.parse_data)
    #     # print(response.url)

    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianYanItem)
        item['university'] = "University of Canberra"
        # item['country'] = 'Australia'
        # item['website'] = 'https://www.vu.edu.au/'
        item['url'] = response.url
        item['degree_type'] = 2
        item['teach_time'] = 'coursework'
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

            pro_re = re.findall(r"Master", item['degree_name'])
            # print("pre_re: ", pro_re)
            if len(pro_re) < 2 and "online" not in item['degree_name']:
                programme_re = re.findall(r"\(.+\)", item['degree_name'])
                if len(programme_re) > 0:
                    item['programme_en'] = ''.join(programme_re).replace("(", "").replace(")", "").strip()
                else:
                    item['programme_en'] = item['degree_name'].replace("Master of", "").strip()
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

                # duration = response.xpath(
                #     "//div[@class='field field-essentials-duration']//div[@class='field-item']//text()").extract()
                # clear_space(duration)
                # item['duration'] = ''.join(duration).strip()
                # # print("item['duration']: ", item['duration'])

                overview = response.xpath(
                    "//h2[contains(text(),'Career opportunities')]/preceding-sibling::*").extract()
                if len(overview) == 0:
                    overview = response.xpath(
                        "//div[@class='collapsible-section']/preceding-sibling::*").extract()
                item['degree_overview_en'] = remove_class(clear_lianxu_space(overview))
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

                work_experience_desc_en = response.xpath(
                    "//*[contains(text(), 'work experience')]").extract()
                item['work_experience_desc_en'] = remove_class(clear_lianxu_space(work_experience_desc_en))
                print("item['work_experience_desc_en']: ", item['work_experience_desc_en'])

                yield item
        except Exception as e:
            with open("scrapySchool_Australian_yan/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

