# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
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
class SouthernCrossUniversity_USpider(CrawlSpider):
    name = "SouthernCrossUniversity_U"
    # start_urls = ["https://www.scu.edu.au/study-at-scu/course-search/?year=2019&courseType=Undergraduate&page=1",
    #               "https://www.scu.edu.au/study-at-scu/course-search/?year=2019&courseType=Honours&page=1"]
    start_urls = ["https://www.scu.edu.au/study-at-scu/course-search/?keyword=&year=2019&available_to=International+Onshore&courseType=Undergraduate&courseType=Honours&location=China+-+Guangxi+UST&location=China+-+TUST&location=Coffs+Harbour&location=Gold+Coast&location=Lismore&location=Melbourne&location=Melbourne+-+The+Hotel+School&location=National+Marine+Science+Centre+Coffs+Harbour&location=New+Zealand+-+MIT&location=Papua+New+Guinea+-+IBSU+Enga&location=Papua+New+Guinea+-+IBSU+Port+Moresby&location=Perth&location=SCU+Online&location=Singapore+-+MDIS&location=Sydney&location=Sydney+-+The+Hotel+School&location=Tweed+Heads+-+Riverside&location=Uzbekistan+-+MDIS+Tashkent"]
    rules = (
        # Rule(page_link, callback='get_programme_link', follow=True),
        Rule(LinkExtractor(allow=r'page=\d+'), follow=True, callback='page'),
        Rule(LinkExtractor(restrict_xpaths="//table[@class='table']/tbody/tr/td[1]/a"), follow=True, callback='content'),
    )

    # def page(self, response):
    #     print("===============")
    #     print(response.url)

    def content(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "Southern Cross University"
        # item['country'] = 'Australia'
        # item['website'] = 'https://www.scu.edu.au/'
        item['url'] = response.url
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        try:
            programme = response.xpath("//h1[@class='pageTitleFixSource']//text()").extract()
            clear_space(programme)
            item['degree_name'] = ''.join(programme)
            print("item['degree_name']: ", item['degree_name'])

            pro_re = re.findall(r"Bachelor", item['degree_name'])
            # print("pre_re: ", pro_re)
            if len(pro_re) < 2:
                duration = response.xpath(
                    "//div[@id='international']//td[contains(text(),'Duration')]/following-sibling::td//text()").extract()
                clear_space(duration)
                item['duration'] = ''.join(duration).strip()
                print("item['duration']: ", item['duration'])

                if "full" in item['duration'].lower():
                    programme_re = re.findall(r"\(.+\)", item['degree_name'].replace("(Honours)", "").replace("with Honours", ""))
                    if len(programme_re) > 0:
                        if len(programme_re) != "(Honours)":
                            item['programme_en'] = ''.join(programme_re).replace("(", "").replace(")", "").strip()
                        else:
                            item['programme_en'] = item['degree_name'].replace("Bachelor of", "").replace("(Honours)", "").strip()
                    else:
                        in_re = re.findall(r"in\s.*", item['degree_name'].replace("(Honours)", "").replace("with Honours", ""))
                        if len(in_re) > 0:
                            item['programme_en'] = ''.join(in_re).strip().strip("in").strip()
                        else:
                            item['programme_en'] = item['degree_name'].replace("Bachelor of", "").replace("with Honours", "").strip()
                    print("item['programme_en']: ", item['programme_en'])

                    overview = response.xpath("//div[@class='summary']").extract()
                    item['degree_overview_en'] = remove_class(clear_lianxu_space(overview))
                    item['overview_en'] = item['degree_overview_en']
                    # if item['degree_overview_en'] == "":
                    #     print("***degree_overview_en 为空")
                    # print("item['degree_overview_en']: ", item['degree_overview_en'])

                    career = response.xpath(
                        "//h3[contains(text(), 'Career opportunities')]/..").extract()
                    item['career_en'] = remove_class(clear_lianxu_space(career))
                    # if item['career_en'] == "":
                    #     print("***career_en 为空")
                    # print("item['career_en']: ", item['career_en'])

                    start_date = response.xpath("//h3[contains(text(),'International students studying in Australia')]/..//div[@class='accordion course-apply-accordion']//div/h5/span//text()").extract()
                    print("start_date: ", start_date)
                    if start_date:
                        item['start_date'] = ','.join(start_date).strip()
                    print("item['start_date']: ", item['start_date'])

                    tuition_fee = response.xpath(
                        "//div[@id='international']//div[@class='table-grid table-responsive no-overflow']//tbody/tr/td[3]//text()").extract()
                    clear_space(tuition_fee)
                    item['tuition_fee'] = '; '.join(tuition_fee).strip()
                    print("item['tuition_fee']: ", item['tuition_fee'])

                    # //tr[@class='data-label-Overall']/td[2]
                    IELTS = response.xpath(
                        "//tr[@class='data-label-Overall']/td[2]//text()|//tr[@class='data-label-Overall Score']/td[2]//text()|"
                        "//td[contains(text(),'Overall Score')]/following-sibling::td//text()").extract()
                    clear_space(IELTS)
                    item['ielts'] = ','.join(IELTS).strip()
                    print("item['ielts']: ", item['ielts'])

                    IELTS_L = response.xpath(
                        "//tr[@class='data-label-Listening']/td[2]//text()").extract()
                    clear_space(IELTS_L)
                    item['ielts_l'] = ','.join(IELTS_L).strip()
                    # print("item['ielts_l']: ", item['ielts_l'])

                    IELTS_S = response.xpath(
                        "//tr[@class='data-label-Speaking']/td[2]//text()").extract()
                    clear_space(IELTS_S)
                    item['ielts_s'] = ','.join(IELTS_S).strip()
                    # print("item['ielts_s']: ", item['ielts_s'])

                    IELTS_R = response.xpath(
                        "//tr[@class='data-label-Reading']/td[2]//text()").extract()
                    clear_space(IELTS_R)
                    item['ielts_r'] = ','.join(IELTS_R).strip()
                    # print("item['ielts_r']: ", item['ielts_r'])

                    IELTS_W = response.xpath(
                        "//tr[@class='data-label-Writing']/td[2]//text()").extract()
                    clear_space(tuition_fee)
                    item['ielts_w'] = ','.join(IELTS_W).strip()
                    # print("item['ielts_w']: ", item['ielts_w'])

                    average_score = response.xpath(
                        "//tr[@class='data-label-China Senior Middle 3']//text() | //tr[@class='data-label-China Gao Kao']//text()").extract()
                    clear_space(average_score)
                    # item['average_score'] = ','.join(average_score).strip()
                    # print("item['average_score']: ", item['average_score'])

                    modules = response.xpath(
                        "//div[@id='structure']").extract()
                    item['modules_en'] = remove_class(clear_lianxu_space(modules))
                    # print("item['modules_en']: ", item['modules_en'])

                    # //h2[contains(text(),'Admission requirements')]|//h2[contains(text(),'Admission requirements')]/following-sibling::div[1]
                    rntry_requirements_en = response.xpath(
                        "//h2[contains(text(),'Admission requirements')]|//h2[contains(text(),'Admission requirements')]/following-sibling::div[1]").extract()
                    item['rntry_requirements_en'] = remove_class(clear_lianxu_space(rntry_requirements_en))
                    # print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

                    how_to_apply = response.xpath(
                        "//div[@id='apply']").extract()
                    item['apply_desc_en'] =  remove_class(clear_lianxu_space(how_to_apply))
                    # print("item['apply_desc_en']: ", item['apply_desc_en'])

                    other = response.xpath(
                        "//div[@id='international']//text()").extract()
                    clear_space(other)
                    # item['other'] = ''.join(other).strip()
                    # print("item['other']: ", item['other'])

                    location = response.xpath(
                        "//div[@id='international']//td[contains(text(),'Availability details')]/following-sibling::td//tbody/tr[position()<last()]/td[1]//text()").extract()
                    clear_space(location)
                    item['location'] = ', '.join(location).strip()
                    print("item['location']: ", item['location'])

                    if item['location'] != "SCU Online":
                        major_list = response.xpath("//h3[contains(text(),'Specialisations')]/../../following-sibling::tr[@class='header-row text group-hdr']//h4//text()").extract()
                        clear_space(major_list)
                        print("major_list: ", major_list)
                        print(len(major_list))

                        if len(major_list) == 0:
                            yield item
                        else:
                            modules_list = response.xpath(
                                "//h3[contains(text(),'Specialisations')]/../../following-sibling::tr[@class='header-row text group-hdr']//h4/following-sibling::div").extract()
                            print("===", modules_list)
                            print(len(modules_list))
                            if len(modules_list) == len(major_list):
                                for m in range(len(major_list)):
                                    item['programme_en'] = major_list[m]
                                    item['modules_en'] = remove_class(clear_lianxu_space([modules_list[m]]))
                                    print("item['programme_en']: ", item['programme_en'])
                                    yield item
        except Exception as e:
            with open("scrapySchool_Australian_yan/error/" + item['university'] + str(item['degree_type']) + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

