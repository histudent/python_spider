import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_Australian_ben.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_ben.getItem import get_item
from scrapySchool_Australian_ben.getTuition_fee import getTuition_fee
from scrapySchool_Australian_ben.items import ScrapyschoolAustralianBenItem
from scrapySchool_Australian_ben.remove_tags import remove_class
from scrapySchool_Australian_ben.getStartDate import getStartDate, getStartDateMonth
from scrapySchool_Australian_ben.getDuration import getIntDuration
from scrapySchool_Australian_ben.getIELTS import get_ielts

# 2019/03/21 星期四 数据更新
class UniversityofSouthAustralia_USpider(scrapy.Spider):
    name = "UniversityofSouthAustralia_U"
    start_urls = ["http://study.unisa.edu.au/"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        links = response.xpath("//div[@id='undergraduate']//div[@class='online-degree-panel medium-up-2 large-up-4']/a/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))

        for link in links:
            url = "http://study.unisa.edu.au" + link
            yield scrapy.Request(url, callback=self.parse_url)

    def parse_url(self, response):
        # print("================", response.url)
        # 判断是否是详情页链接
        span_is = response.xpath("//span[contains(text(),'Degree Level')]//text()").extract()
        # print("****", response.url)
        # print("span_is: ", span_is)
        links = []
        if len(span_is) > 0 and "graduate" not in response.url:
            print("***详情页链接")
            links.append(response.url)
            # yield scrapy.Request(response.url, callback=self.parse_data)
        else:
            print("***不是详情页链接")
            links = response.xpath("//tr//td[contains(text(), 'On-campus')]/preceding-sibling::td/a[contains(text(), 'Bachelor of')]/@href|"
                                   "//h2[contains(text(),'Bachelor of')]/following-sibling::*//a/@href").extract()
            if len(links) == 0:
                links = response.xpath(
                    "//a[contains(text(), 'Bachelor of')]/@href").extract()

        # # print(len(links))
        # links = list(set(links))
        # # print(len(links))
        # print("links: ", links)
        # links = ["http://study.unisa.edu.au/degrees/bachelor-of-health-science/int"]
        if len(links) > 0:
            for link in links:
                if "http" in link:
                    url = link
                else:
                    url = "http://study.unisa.edu.au" + link
                # print("url = ", url)
                yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        # 判断是否学位下面还有专业
        specialisations = response.xpath("//h2[contains(text(),'Specialisations')]/following-sibling::*//a/@href").extract()
        # print("specialisations: ", specialisations, response.url)
        if len(specialisations) > 0:
            for link in specialisations:
                if "http" in link:
                    url = link
                else:
                    url = "http://study.unisa.edu.au" + link
                yield scrapy.Request(url, callback=self.parse_data)
        else:
            item = get_item(ScrapyschoolAustralianBenItem)
            item['university'] = "University of South Australia"
            # item['country'] = 'Australia'
            # item['website'] = 'http://www.unisa.edu.au/'
            item['url'] = response.url
            print("===========================")
            print(response.url)
            item['degree_type'] = 1
            try:
                programme = response.xpath(
                    "//div[@class='title-row']/h1/text()").extract()
                clear_space(programme)
                item['degree_name'] = ''.join(programme).replace("(International)", "").strip()
                print("item['degree_name']: ", item['degree_name'])

                pro_re = re.findall(r"Bachelor", item['degree_name'])
                print("pre_re: ", pro_re)
                if len(pro_re) < 2:
                    programme_re = re.findall(r"\(.+\)", item['degree_name'])
                    print("programme_re: ", programme_re)
                    if len(programme_re) > 0:
                        if ''.join(programme_re).strip() != "(Honours)":
                            item['programme_en'] = ''.join(programme_re).replace("(", "").replace(")", "").strip()
                        else:
                            item['programme_en'] = item['degree_name'].replace("Bachelor of", "").replace("(Honours)", "").strip().strip(
                                "in").strip()
                    else:
                        item['programme_en'] = item['degree_name'].replace("Bachelor of", "").strip().strip("in").strip()
                    print("item['programme_en']: ", item['programme_en'])

                    start_date = response.xpath(
                        "//span[contains(text(), 'Start')]/../text()").extract()
                    clear_space(start_date)
                    # print("start_date: ", start_date)
                    item['start_date'] = getStartDateMonth(', '.join(start_date))
                    print("item['start_date']: ", item['start_date'])

                    # //span[contains(text(),'Campus')]/../a
                    location = response.xpath(
                        "//span[contains(text(),'Campus')]/../a//text()").extract()
                    clear_space(location)
                    item['location'] = ''.join(location).strip()
                    print("item['location']: ", item['location'])

                    duration = response.xpath(
                        "//span[contains(text(),'Duration')]/../text()").extract()
                    clear_space(duration)
                    item['duration'] = ''.join(duration).strip()
                    print("item['duration']: ", item['duration'])

                    tuition_fee = response.xpath("//span[contains(text(),'2019: AUD$')]//text()|"
                                                 "//span[contains(text(),'Fees')]/../text()").extract()
                    print("tuition_fee: ", tuition_fee)
                    clear_space(tuition_fee)
                    tuition_fee = getTuition_fee(''.join(tuition_fee))
                    item['tuition_fee'] = str(tuition_fee)
                    if item['tuition_fee'] == '0':
                        item['tuition_fee'] = None
                    print("item['tuition_fee']: ", item['tuition_fee'])

                    # //span[contains(text(),'English Language Requirements')]/..
                    ielts = response.xpath("//span[contains(text(),'English Language Requirements')]/../ul//text()").extract()
                    clear_space(ielts)
                    item['ielts_desc'] = ' '.join(ielts).strip()
                    print("item['ielts_desc']: ", item['ielts_desc'])

                    ieltlsrw = re.findall(r"\d[\d\.]{0,2}", item['ielts_desc'])
                    if len(ieltlsrw) > 0:
                        item["ielts"] = ieltlsrw[0]

                    ielts_l_re = re.findall(r"listening\s\[.*?\]", item['ielts_desc'])
                    item["ielts_l"] = ''.join(ielts_l_re).replace("listening", "").replace("[", "").replace("]", "").strip()

                    ielts_s_re = re.findall(r"speaking\s\[.*?\]", item['ielts_desc'])
                    item["ielts_s"] = ''.join(ielts_s_re).replace("speaking", "").replace("[", "").replace("]", "").strip()

                    ielts_r_re = re.findall(r"reading\s\[.*?\]", item['ielts_desc'])
                    item["ielts_r"] = ''.join(ielts_r_re).replace("reading", "").replace("[", "").replace("]", "").strip()

                    ielts_w_re = re.findall(r"writing\s\[.*?\]", item['ielts_desc'])
                    item["ielts_w"] = ''.join(ielts_w_re).replace("writing", "").replace("[", "").replace("]", "").strip()
                    print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                            item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

                    # //div[@class='page-info-block-inner']//ul[@id='entry-requirements']
                    entry_requirements = response.xpath(
                        "//div[@class='page-info-block-inner']//ul[@id='entry-requirements']").extract()
                    item['rntry_requirements_en'] = remove_class(clear_lianxu_space(entry_requirements))
                    print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

                    degree_overview_en = response.xpath(
                        "//h2[contains(text(),'Degree overview')]/../../..").extract()
                    item['degree_overview_en'] = remove_class(clear_lianxu_space(degree_overview_en))
                    print("item['degree_overview_en']: ", item['degree_overview_en'])

                    overview_en = response.xpath(
                        "//h2[contains(text(),'Snapshot')]/..|"
                        "//h3[contains(text(),'Snapshot')]/..").extract()
                    item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
                    print("item['overview_en']: ", item['overview_en'])

                    modules_en = response.xpath(
                        "//h2[@class='theme-white'][contains(text(), 'Degree structure')]/../..|"
                        "//h3[contains(text(),'Degree structure')]/../..").extract()
                    item['modules_en'] = remove_class(clear_lianxu_space(modules_en))
                    print("item['modules_en']: ", item['modules_en'])

                    career_en = response.xpath(
                        "//h2[contains(text(),'Your career')]/../../..|"
                        "//h3[contains(text(),'Your career')]/..").extract()
                    item['career_en'] = remove_class(clear_lianxu_space(career_en))
                    print("item['career_en']: ", item['career_en'])

                    apply_desc_en = response.xpath(
                        "//h2[contains(text(),'How to apply')]/../../..").extract()
                    item['apply_desc_en'] = remove_class(clear_lianxu_space(apply_desc_en))
                    print("item['apply_desc_en']: ", item['apply_desc_en'])

                    if "research" not in item['degree_name']:
                        yield item
            except Exception as e:
                with open("scrapySchool_Australian_ben/error/" + item['university'] + str(item['degree_type']) + ".txt",
                          'a', encoding="utf-8") as f:
                    f.write(str(e) + "\n" + response.url + "\n========================\n")
                print("异常：", str(e))
                print("报错url：", response.url)

