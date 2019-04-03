# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime


class CardiffMetropolitanUniversity_USpider(scrapy.Spider):
    name = "CardiffMetropolitanUniversity_U"
    start_urls = ["http://www.cardiffmet.ac.uk/study/Pages/Undergraduate-Courses-A-Z.aspx"]

    def parse(self, response):
        links = response.xpath("//ul[@class='dfwp-column dfwp-list']//a/@href").extract()
        # 组合字典
        programme_dict = {}
        programme_list = response.xpath("//ul[@class='dfwp-column dfwp-list']//a//text()").extract()
        clear_space(programme_list)

        for link in range(len(links)):
            url = links[link]
            programme_dict[url] = programme_list[link]

        print(len(links))
        links = list(set(links))
        print(len(links))
        for url in links:
            # print("url = ", url)
            if "//www.cardiffmet.ac.uk" in url:
                yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "https://www.cardiffmet.ac.uk/"
        item['university'] = "Cardiff Metropolitan University"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        item['location'] = 'Llandaff Campus, Western Avenue, Cardiff, CF5 2YB'
        # print("item['location'] = ", item['location'])
        print("===========================")
        print(response.url)
        item['major_type1'] = response.meta.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            # 专业、学位类型
            programmeDegreetype = response.xpath("//div[@id='ordercontainer']/span[@id='DeltaPlaceHolderMain']/div[@class='coursefullwidth']/div/h1//text()").extract()
            # print("programmeDegreetype: ", programmeDegreetype)
            if len(programmeDegreetype) == 0:
                programmeDegreetype = response.xpath(
                    "//div[@class='cstcoursetitle']/h1//text()").extract()

            clear_space(programmeDegreetype)
            programmeDegreetypeStr = ''.join(programmeDegreetype).strip()
            if programmeDegreetypeStr == "":
                programmeDegreetypeStr = item['major_type1']
            # print("programmeDegreetypeStr: ", programmeDegreetypeStr)
            programmeDegreetypesplit = programmeDegreetypeStr.split("-")
            # print(programmeDegreetypesplit)
            if len(programmeDegreetypesplit) > 1:
                degreetype = programmeDegreetypesplit[-1]
                # print(degreetype)
                item['degree_name'] = degreetype
                programme = programmeDegreetypesplit[0]
                # print(programme)
                item['programme_en'] = ''.join(programme)
            else:
                programme = programmeDegreetypesplit[0]
                # print(programme)
                item['programme_en'] = ''.join(programme)
            item['degree_name'] = item['degree_name'].replace("(Hons)", "").replace("Degree", "").replace(" s", "").replace("(Joint Honours)", "").replace("(Franchised)", "").strip()
            print("item['degree_name']: ", item['degree_name'])
            if "(Top-Up)" in item['major_type1']:
                item['programme_en'] = item['programme_en'] + "-Up)"
            print("item['programme_en']: ", item['programme_en'])

            if "Foundation" not in item['major_type1']:
                department = response.xpath("//div[@class='crumbcontainer']/span/span[1]/a[1]//text()").extract()
                clear_space(department)
                item['department'] = ''.join(department)
                # print("item['department'] = ", item['department'])

                duration = response.xpath(
                    "//strong[contains(text(),'Course Length:')]/..//text()").extract()
                clear_space(duration)
                # print("duration: ", duration)
                duration_list = getIntDuration(''.join(duration).replace("Course Length:", "").strip())
                if len(duration_list) == 2:
                    item['duration'] = duration_list[0]
                    item['duration_per'] = duration_list[-1]
                # print("item['duration'] = ", item['duration'])
                # print("item['duration_per'] = ", item['duration_per'])

                # //div[@id='ordercontainer']/span[@id='DeltaPlaceHolderMain']/div[@class='coursefullwidth']/div[@class='rightcontainer']/div[@class='coursefacts']/div/div//p
                overview = response.xpath(
                    "//div[@id='ordercontainer']/span[@id='DeltaPlaceHolderMain']/div[@class='coursefullwidth']/div[@class='coursecontentarea']/div[@class='courseoverview']").extract()
                item['overview_en'] = remove_class(clear_lianxu_space(overview))
                # print("item['overview_en']: ", item['overview_en'])
                # if item['overview_en'] == "":
                #     print("****111****")

                modules_en = response.xpath(
                    "//h3[contains(text(),'Course Content')]|//h3[contains(text(),'Course Content')]/following-sibling::div[1]").extract()
                if len(modules_en) == 0:
                    modules_en = response.xpath("//h3[contains(text(),'Course content')]/..").extract()
                item['modules_en'] = remove_class(clear_lianxu_space(modules_en))
                # print("item['modules_en']: ", item['modules_en'])
                # if item['modules_en'] == "":
                #     print("****111****")

                assessment_en = response.xpath(
                    "//h3[contains(text(),'Learning & Teaching')]|//h3[contains(text(),'Learning & Teaching')]/following-sibling::div[1]|"
                    "//h3[contains(text(),'Assessment')]|//h3[contains(text(),'Assessment')]/following-sibling::div[1]").extract()
                item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
                # print("item['assessment_en']: ", item['assessment_en'])
                # if item['assessment_en'] == "":
                #     print("****111****")

                career_en = response.xpath(
                    "//h3[contains(text(),'Employability & Careers')]|//h3[contains(text(),'Employability & Careers')]/following-sibling::div[1]").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career_en))
                # print("item['career_en']: ", item['career_en'])
                # if item['career_en'] == "":
                #     print("****111****")

                alevel = response.xpath(
                    "//*[contains(text(),'A levels')]//text()|"
                    "//*[contains(text(),'A Levels')]//text()").extract()
                item['alevel'] = clear_lianxu_space(alevel)
                # print("item['alevel']: ", item['alevel'])

                ib = response.xpath(
                    "//strong[contains(text(),'International Baccalaureate:')]/../text()").extract()
                item['ib'] = clear_lianxu_space(ib)
                # print("item['ib']: ", item['ib'])

                rntry_requirements = response.xpath(
                    "//h3[contains(text(),'Entry Requirements')]/following-sibling::div[1]//text()").extract()
                if len(rntry_requirements) == 0:
                    rntry_requirements = response.xpath(
                        "//h3[contains(text(),'Entry Requirements​')]/following-sibling::div[1]//text()").extract()
                    if len(rntry_requirements) == 0:
                        rntry_requirements = response.xpath(
                            "//h3[contains(text(),'Entry Requirements & How to Apply')]/following-sibling::div[1]//text()").extract()
                rntry_requirements = clear_lianxu_space(rntry_requirements)
                # print("item['rntry_requirements']: ", item['rntry_requirements'])

                ielts = re.findall(r"IELTS.{1,80}", rntry_requirements)
                clear_space(ielts)
                # print("ielts: ", ielts)
                if len(ielts) > 0:
                    item['ielts_desc'] = ielts[0]
                # print("item['ielts_desc']: ", item['ielts_desc'])

                ielts_dict = get_ielts(item['ielts_desc'])
                # if len(ielts_list) == 1:
                item['ielts'] = ielts_dict.get('IELTS')
                item['ielts_l'] = ielts_dict.get('IELTS_L')
                item['ielts_s'] = ielts_dict.get('IELTS_S')
                item['ielts_r'] = ielts_dict.get('IELTS_R')
                item['ielts_w'] = ielts_dict.get('IELTS_W')
                # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))


                interview_desc_en = response.xpath("//*[contains(text(),'interview')]").extract()
                if len(interview_desc_en) == 0:
                    interview_desc_en = re.findall(r".{1,100}interview.{1,100}", rntry_requirements)
                item['interview_desc_en'] = remove_class(clear_lianxu_space(interview_desc_en)).strip()
                # print("item['interview_desc_en']: ", item['interview_desc_en'])

                # http://www.cardiffmet.ac.uk/international/study/applying/Pages/Fees-and-Money-Matters.aspx
                item['tuition_fee'] = '12000'
                item['apply_proces_en'] = 'http://www.cardiffmet.ac.uk/study/adviceforapplicants/undergraduate/Pages/default.aspx'
                # print("item['apply_proces_en']: ", item['apply_proces_en'])

                ucascode = response.xpath("//strong[contains(text(),'UCAS Code')]/following-sibling::*[1]//strong//text()|"
                                          "//strong[contains(text(),'UCAS Code')]/..//text()|"
                                          "//strong[contains(text(),'​UCAS Code')]/../following-sibling::p//text()|"
                                          "//strong[contains(text(),'​UCAS Code')]/../following-sibling::p//text()").extract()

                clear_space(ucascode)
                print("ucascode: ", ucascode)
                item['other'] = ' '.join(ucascode).strip()
                print("item['other'] = ", item['other'])

                ucascode_re = re.findall(r"UCAS\sCode:\w{4}|UCAS\sCodes:\w{4}|UCAS\sCodes:\s\w{4}", ''.join(ucascode).strip())
                print("ucascode_re: ", ucascode_re)
                if len(ucascode_re) > 0:
                    item['ucascode'] = ''.join(ucascode_re).replace("UCAS Code:", "").replace("UCAS Codes:", "").strip()
                print("item['ucascode'] = ", item['ucascode'])

                yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

