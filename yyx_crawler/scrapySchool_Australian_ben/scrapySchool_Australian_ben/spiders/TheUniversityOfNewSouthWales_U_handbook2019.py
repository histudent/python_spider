# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_Australian_ben.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_ben.getItem import get_item
from scrapySchool_Australian_ben.getTuition_fee import getTuition_fee
from scrapySchool_Australian_ben.items import ScrapyschoolAustralianBenItem
from scrapySchool_Australian_ben.remove_tags import remove_class
from scrapySchool_Australian_ben.getStartDate import getStartDate
from scrapySchool_Australian_ben.getDuration import getIntDuration
from lxml import etree
import requests
from w3lib.html import remove_tags


class TheUniversityOfNewSouthWales_U_handbook2019Spider(scrapy.Spider):
    name = "TheUniversityOfNewSouthWales_U_handbook2019"
    # 2019/03/21 星期四
    start_urls = ["https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4803?browseByFaculty=FacultyOfArtDesign&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4516?browseByFaculty=FacultyOfArtDesign&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4822?browseByFaculty=FacultyOfArtDesign&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4527?browseByFaculty=FacultyOfArtDesign&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4821?browseByFaculty=FacultyOfArtDesign&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4526?browseByFaculty=FacultyOfArtDesign&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4813?browseByFaculty=FacultyOfArtDesign&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4528?browseByFaculty=FacultyOfArtDesign&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3409?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4504?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3444?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3422?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4505?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4056?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4509?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3447?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3417?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3429?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3454?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/4510?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3434?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3453?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3438?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3436?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/4508?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3440?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3478?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/4507?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3420?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/4033?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3261?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4521?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3264?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3362?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3268?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4523?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3332?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4522?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3387?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/4525?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3256?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3381?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3736?browseByFaculty=FacultyOfEngineering&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3778?browseByFaculty=FacultyOfEngineering&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4515?browseByFaculty=FacultyOfEngineering&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3635?browseByFaculty=FacultyOfEngineering&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3707?browseByFaculty=FacultyOfEngineering&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3768?browseByFaculty=FacultyOfEngineering&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3706?browseByFaculty=FacultyOfEngineering&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3061?browseByFaculty=FacultyOfEngineering&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3775?browseByFaculty=FacultyOfEngineering&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4701?browseByFaculty=FacultyOfLaw&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4702?browseByFaculty=FacultyOfLaw&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3871?browseByFaculty=FacultyOfMedicine&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3880?browseByFaculty=FacultyOfMedicine&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3805?browseByFaculty=FacultyOfMedicine&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3831?browseByFaculty=FacultyOfMedicine&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3956?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3962?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3980?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3981?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3053?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3959?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3965?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3966?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3131?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3133?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3991?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3999?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3435?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/4518?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3632?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3970?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/4500?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3987?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3925?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3181?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3182?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3586?browseByFaculty=UnswBusinessSchool&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3587?browseByFaculty=UnswBusinessSchool&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4520?browseByFaculty=UnswBusinessSchool&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3502?browseByFaculty=UnswBusinessSchool&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3554?browseByFaculty=UnswBusinessSchool&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3565?browseByFaculty=UnswBusinessSchool&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/4501?browseByFaculty=UnswBusinessSchool&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3558?browseByFaculty=UnswBusinessSchool&",
"https://www.handbook.unsw.edu.au/undergraduate/programs/2019/3543?browseByFaculty=UnswBusinessSchool&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/4502?browseByFaculty=UnswBusinessSchool&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3979?browseByFaculty=UnswBusinessSchool&",
"https://www.handbook.unsw.edu.au/Undergraduate/programs/2019/3964?browseByFaculty=UnswBusinessSchool&", ]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))
    headers_base = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}


    def parse(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "The University of New South Wales"
        item['url'] = response.url
        item['degree_type'] = 1
        # item['teach_time'] = 'coursework'
        print("===========================")
        print(response.url)
        try:
            department = response.xpath("//li[3]//a//text()").extract()
            item['department'] = ''.join(department).strip()
            print("item['department']: ", item['department'])

            location = response.xpath("//div[@role='complementary']//strong[@tabindex='0'][contains(text(),'Campus')]/../p//text()").extract()
            item['location'] = ''.join(location).strip()
            print("item['location']: ", item['location'])

            duration = response.xpath(
                "//div[contains(@role,'complementary')]//strong[contains(@tabindex,'0')][contains(text(),'Typical duration')]/../p//text()").extract()
            clear_space(duration)
            print("duration: ", duration)
            if "Years" in ''.join(duration):
                item['duration'] = ''.join(duration).replace("Years", "").strip()
                item['duration_per'] = 1
            print("item['duration']: ", item['duration'])

            # //div[@id='readMoreToggle1']
            overview_en = response.xpath("//div[@id='readMoreToggle1']/div[1]").extract()
            item['degree_overview_en'] = item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
            print("item['overview_en']: ", item['overview_en'])

            item["rntry_requirements_en"] = None
            rntry_requirements_en = response.xpath("//div[@class='m-accordion-group m-accordion-with-header']//div[@class='m-accordion-body']|"
                                                   "//strong[@aria-label='Progression Requirements']/../../following-sibling::div").extract()
            if rntry_requirements_en:
                item['rntry_requirements_en'] = remove_class(clear_lianxu_space(rntry_requirements_en))
            print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

            modules_en = response.xpath("//div[@id='structure']/div[position()<last()]").extract()
            if modules_en:
                item['modules_en'] = remove_class(clear_lianxu_space(modules_en))
            print("item['modules_en']: ", item['modules_en'])

            career_en = response.xpath("//strong[@aria-label='Career Opportunities']/../../following-sibling::div").extract()
            if career_en:
                item['career_en'] = remove_class(clear_lianxu_space(career_en))
            print("item['career_en']: ", item['career_en'])


            # start_date = response.xpath(
            #     "//section//dt[contains(text(), 'Entry')]/following-sibling::dd[1]//text()").extract()
            # clear_space(start_date)
            # print(len(start_date))
            # print("start_date: ", start_date)
            #
            # tuition_fee = response.xpath(
            #     "//section//dt[contains(text(), 'Estimated first year tuition')]/following-sibling::*[1]//text()").extract()
            # clear_space(tuition_fee)
            # print(len(tuition_fee))
            # print("tuition_fee: ", tuition_fee)


            # 学位类型列表
            degree_name = response.xpath("//div[@role='complementary']//p[contains(text(),'Bachelor of')]/text()|"
                                         "//div[@role='complementary']//p[contains(text(),'Juris Doctor')]/text()").extract()
            clear_space(degree_name)
            if len(degree_name) > 0:
                item['degree_name'] = ', '.join(degree_name).replace("-", "").strip()
            else:
                item['degree_name'] = None
            print("item['degree_name']: ", item['degree_name'])

            programme_list = response.xpath('//div[@data-hbui-filter-item="specialisation"]/a/div/p//text()|'
                                            '//h4[contains(text(),"Home Majors and Minors")]/../../following-sibling::div//div[@data-hbui-filter-item="major"]/a[contains(@href, "/undergraduate/specialisations/2019/")]/div[last()]/p//text()|'
                                            '//h4[contains(text(),"Business Majors")]/../../following-sibling::div//div[@data-hbui-filter-item="major"]/a[contains(@href, "/undergraduate/specialisations/2019/")]/div[last()]/p//text()|'
                                            '//h4[contains(text(),"Optional Minor or Second Major (International)")]/../../following-sibling::div//div[@data-hbui-filter-item="major"]/a[contains(@href, "/undergraduate/specialisations/2019/")]/div[last()]/p//text()|'
                                            '//h4[contains(text(),"Economics Majors")]/../../following-sibling::div//div[@data-hbui-filter-item="major"]/a[contains(@href, "/undergraduate/specialisations/2019/")]/div[last()]/p//text()|'
                                            '//h4[contains(text(),"Specialisation")]/../../following-sibling::div//div[@data-hbui-filter-item="major"]/a[contains(@href, "/undergraduate/specialisations/2019/")]/div[last()]/p//text()|'
                                            '//h4[contains(text(),"Specialisation")]/../../following-sibling::div//div[@data-hbui-filter-item="honours"]/a[contains(@href, "/undergraduate/specialisations/2019/")]/div[last()]/p//text()|'
                                            '//h4[contains(text(),"Major")]/../../following-sibling::div//div[@data-hbui-filter-item="major"]/a[contains(@href, "/undergraduate/specialisations/2019/")]/div[last()]/p//text()|'
                                            '//h4[contains(text(),"Major")]/../../following-sibling::div//div[@data-hbui-filter-item="honours"]/a[contains(@href, "/undergraduate/specialisations/2019/")]/div[last()]/p//text()|'
                                            '//h4[contains(text(),"major")]/../../following-sibling::div//div[@data-hbui-filter-item="major"]/a[contains(@href, "/undergraduate/specialisations/2019/")]/div[last()]/p//text()').extract()
            if len(programme_list) == 0:
                programme_list = response.xpath('//h4[contains(text(),"Major")]/../../following-sibling::div//div[@data-hbui-filter-item="honours"]/a[contains(@href, "/undergraduate/specialisations/2019/")]/div[last()]/p//text()').extract()
            print("programme_list: ", programme_list)

            programme_list = list(set(programme_list))
            if item['degree_name'] is None:
                pass
            else:
                if len(programme_list) == 0:
                    programme_en = response.xpath("//span[@data-hbui='module-title']//text()").extract_first(None)
                    print("programmen: ", programme_en)
                    item['programme_en'] = programme_en
                    yield item
                else:
                    for prog in programme_list:
                        item['programme_en'] = prog
                        yield item
        except Exception as e:
            with open(".//scrapySchool_Australian_yan/error/"+item['university']+str(item['degree_type'])+".txt", 'w', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_major_detile(self, major_url, item):
        item['url'] = major_url
        print("item['url']_major: ", item['url'])
        data = requests.get(major_url, headers=self.headers_base)
        response = etree.HTML(data.text.replace('<?xml version="1.0" encoding="utf-8"?>', ""))
        # print("===1=", response)
        programme = response.xpath("//div[@class='internalContentWrapper']/h1[1]//text()")
        print("prog ", programme)
        programme_str = ''.join(programme)
        if "-" in programme_str:
            programme_list = programme_str.split("-")
            item['programme_en'] = ''.join(programme_list[:-1]).strip()
        else:
            item['programme_en'] = programme_str
        print("item['programme_en']_major: ", item['programme_en'])

        overview_en = response.xpath("//h2[contains(text(),'Stream Outline')]/../preceding-sibling::*[1]/following-sibling::*[position()<3]|"
                                     "//td[@class='mainInformation']//div[1]")
        overview_en_str = ""
        if len(overview_en) > 0:
            for m in overview_en:
                # print("===", overview_en_str)
                overview_en_str += etree.tostring(m, encoding='unicode',method='html')
        item['overview_en'] = remove_class(clear_lianxu_space([overview_en_str]))
        print("item['overview_en']_major: ", item['overview_en'])

        modules_en = response.xpath(
            "//a[@name='planstructure']/preceding-sibling::*[1]/following-sibling::*[position()<last()-1]|"
            "//table[@class='tabluatedInfo']")
        modules_en_str = ""
        if len(modules_en) > 0:
            for m in modules_en:
                modules_en_str += etree.tostring(m, encoding='unicode',method='html')
        item['modules_en'] = remove_class(clear_lianxu_space([modules_en_str]))
        print("item['modules_en']_major: ", item['modules_en'])

        new_url_list = response.xpath("//table[@class='tabluatedInfo']//tr/td/a/@href")
        return new_url_list