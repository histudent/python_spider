# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getDuration import getIntDuration, getTeachTime

class UniversityOfPortsmouth_RSpider(scrapy.Spider):
    name = "UniversityOfPortsmouth_R"
    start_urls = ["http://www.port.ac.uk/courses/"]

    def parse(self, response):
        links = response.xpath("//h2[@id='postgraduate-research']/following-sibling::div[@class='group quarter'][1]/div/nav/ul/li/a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))
        # print(links)
        for link in links:
            if "http" not in link:
                url = "http://www.port.ac.uk" + link
            else:
                url = link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.port.ac.uk/"
        item['university'] = "University of Portsmouth"
        item['url'] = response.url
        item['teach_type'] = 'phd'
        # 学位类型
        item['degree_type'] = 3
        item['location'] = 'University House, Winston Churchill Avenue, Portsmouth PO1 2UP'
        print("===========================")
        print(response.url)
        try:
            # //div[@class='video']/div[@class='video_title']/div/div[@class='course_title']/h1
            programme = response.xpath("//div[@class='video']/div[@class='video_title']/div/div[@class='course_title']/h1//text()|"
                                       "//div[@class='onscreen-area']/div/div[@class='section'][1]/div[@class='page-title above-page-nav course-page-title']/div[@class='wrap']/h1//text()").extract()
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en']: ", item['programme_en'])

            # //div[@class='video']/div[@class='video_title']/div/div[@class='course_title']/h1
            degree_type = response.xpath(
                "//div[@class='video']/div[@class='video_title']/div/div[@class='course_title']/span//text()|"
                "//div[@class='onscreen-area']/div/div[@class='section'][1]/div[@class='page-title above-page-nav course-page-title']/div[@class='wrap']/p//text()").extract()
            item['degree_name'] = ''.join(degree_type).strip()
            print("item['degree_name']: ", item['degree_name'])

            # //div[@class='video']/div[@class='video_title']/div/div[@class='course_title']/h1
            department = response.xpath(
                "//dt[contains(text(), 'Department')]/following-sibling::dd[1]//text()|//strong[contains(text(), 'Department')]/following-sibling::a//text()|"
                "//strong[contains(text(), 'Department')]/../following-sibling::p//text()|"
                "//span[contains(text(), 'Department')]/../following-sibling::*[1]//text()").extract()
            clear_space(department)
            # print(department)
            if len(department) > 0:
                item['department'] = department[0].strip()
                if item['department'] == "This course is eligible for the":
                    item['department'] = department[-1].strip()
            # print("item['department']: ", item['department'])

            # //div[@class='video']/div[@class='video_title']/div/div[@class='course_title']/h1
            duration = response.xpath("//dt[contains(text(), 'Duration')]/following-sibling::dd[1]//text()|//dt[contains(text(), 'duration')]/following-sibling::dd[1]//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration_str = ''.join(duration)

            item['teach_time'] = getTeachTime(duration_str)
            duration_list = getIntDuration(duration_str)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['teach_time'] = ", item['teach_time'])
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])


            # //strong[contains(text(),'International students')]/../following-sibling::p[1]
            tuition_fee = response.xpath(
                "//strong[contains(text(),'International students')]/../following-sibling::p//text()|"
                "//strong[contains(text(),'2018/19 entry')]/../following-sibling::p[1]//text()|"
                "//dt[contains(text(),'Fees')]/following-sibling::dd[1]//text()").extract()
            clear_space(tuition_fee)
            # print("tuition_fee: ", tuition_fee)
            tuition_fee_re = re.findall(r"Full\stime:\s£\d+,\d+|Full\stime\s£\d+,\d+|International\sfull-time\sstudents:\s£\d+,\d+", ''.join(tuition_fee))
            # print("tuition_fee_re: ", tuition_fee_re)
            tuition_fee_re1 = re.findall(r"\d+,\d+",''.join(tuition_fee_re))
            if len(tuition_fee_re1) > 0:
                item['tuition_fee'] = int(tuition_fee_re1[0].replace(",", "").replace("£", "").strip())
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee']: ", item['tuition_fee'])
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            rntry_requirements_content = response.xpath("//h3[contains(text(),'Key Facts')]/..//text()").extract()
            clear_space(rntry_requirements_content)
            # print("rntry_requirements_content: ", rntry_requirements_content)
            if "2018 ENTRY REQUIREMENTS" in rntry_requirements_content:
                rntry_requirements_index = rntry_requirements_content.index("2018 ENTRY REQUIREMENTS")
                if "Fees" in rntry_requirements_content:
                    rntry_requirements_indexEnd = rntry_requirements_content.index("Fees")
                    item['rntry_requirements'] = clear_lianxu_space(rntry_requirements_content[rntry_requirements_index:rntry_requirements_indexEnd])
            if "2018 entry requirements" in rntry_requirements_content:
                rntry_requirements_index = rntry_requirements_content.index("2018 entry requirements")
                if "Fees" in rntry_requirements_content:
                    rntry_requirements_indexEnd = rntry_requirements_content.index("Fees")
                    item['rntry_requirements'] = clear_lianxu_space(
                        rntry_requirements_content[rntry_requirements_index:rntry_requirements_indexEnd])
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            if item['rntry_requirements'] == "":
                # //dt[contains(text(),'Entry')]/following-sibling::dd[1]
                rntry_requirements = response.xpath("//dt[contains(text(),'Entry')]/following-sibling::dd[1]//text()").extract()
                item['rntry_requirements'] = clear_lianxu_space(rntry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            ieltsList = re.findall(r".{1,45}IELTS.{1,45}", item['rntry_requirements'])
            item['ielts_desc'] = ''.join(ieltsList).strip()
            # print("item['ielts_desc']: ", item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            overview = response.xpath("//h3[contains(text(),'Why take this course?')]/../*[not(@class='blockquote-img')]|"
                                      "//div[@class='onscreen-area']/div/div[@class='section'][1]/div[@class='wrap']/div[@class='group third']/div[@class='column twothirds']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])

            modules = response.xpath("//h3[@id='structure']/../../following-sibling::div[1]|"
                                     "//div[@class='onscreen-area']/div/div[@class='section slate dark']/div[@class='wrap']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])

            teaching_assessment = response.xpath("//div[@class='pure-g purple content']/div[1]/div[@class='box']").extract()
            if len(teaching_assessment) == 0:
                teaching_assessment = response.xpath(
                    "//h3[contains(text(), 'Teaching')]/preceding-sibling::*[1]/following-sibling::*[position()<3]").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(teaching_assessment))
            # print("item['assessment_en']: ", item['assessment_en'])

            career = response.xpath("//div[@class='box container content pure-g']|//div[@class='onscreen-area']/div/div[@class='section teal dark']/div[@class='wrap']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            print("item['career_en']: ", item['career_en'])

            item['apply_proces_en'] = "http://www.port.ac.uk/application-fees-and-funding/applying-postgraduate/#mastersCourses"
            yield item
        except Exception as e:
            with open(item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

