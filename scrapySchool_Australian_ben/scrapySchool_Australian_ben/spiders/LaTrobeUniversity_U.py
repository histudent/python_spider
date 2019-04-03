# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
import requests
# from scrapyNewAustralia.middlewares import *
# from scrapyNewAustralia.items import ScrapynewaustraliaItem
from scrapySchool_Australian_ben.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_ben.getItem import get_item
from scrapySchool_Australian_ben.getTuition_fee import getTuition_fee
from scrapySchool_Australian_ben.items import ScrapyschoolAustralianBenItem
from scrapySchool_Australian_ben.remove_tags import remove_class
from scrapySchool_Australian_ben.getStartDate import getStartDateMonth
from scrapySchool_Australian_ben.getIELTS import get_ielts
import re
from w3lib.html import remove_tags

class Latrobeuniversity_USpider(scrapy.Spider):
    name = 'LaTrobeUniversity_U'

    start_urls = ["https://www.latrobe.edu.au/courses/bachelor-of-arts",
"https://www.latrobe.edu.au/courses/bachelor-of-commerce",
"https://www.latrobe.edu.au/courses/bachelor-of-criminology",
"https://www.latrobe.edu.au/courses/bachelor-of-media-and-communication",
"https://www.latrobe.edu.au/courses/bachelor-of-psychological-science",
"https://www.latrobe.edu.au/courses/bachelor-of-science",
"https://www.latrobe.edu.au/courses/bachelor-of-creative-arts",
"https://www.latrobe.edu.au/courses/bachelor-of-international-relations",
"https://www.latrobe.edu.au/courses/bachelor-of-laws",
"https://www.latrobe.edu.au/courses/bachelor-of-politics-philosophy-and-economics",
"https://www.latrobe.edu.au/courses/bachelor-of-urban-rural-and-environmental-planning",
"https://www.latrobe.edu.au/courses/bachelor-of-accounting",
"https://www.latrobe.edu.au/courses/bachelor-of-business",
"https://www.latrobe.edu.au/courses/bachelor-of-business-event-management",
"https://www.latrobe.edu.au/courses/bachelor-of-business-marketing",
"https://www.latrobe.edu.au/courses/bachelor-of-business-sport-management",
"https://www.latrobe.edu.au/courses/bachelor-of-commerce",
"https://www.latrobe.edu.au/courses/bachelor-of-finance",
"https://www.latrobe.edu.au/courses/bachelor-of-business-accounting-and-finance",
"https://www.latrobe.edu.au/courses/bachelor-of-business-accounting",
"https://www.latrobe.edu.au/courses/bachelor-of-business-agribusiness",
"https://www.latrobe.edu.au/courses/bachelor-of-business-event-management-marketing",
"https://www.latrobe.edu.au/courses/bachelor-of-business-human-resource-management",
"https://www.latrobe.edu.au/courses/bachelor-of-business-sport-development-and-management",
"https://www.latrobe.edu.au/courses/bachelor-of-business-tourism-and-hospitality",
"https://www.latrobe.edu.au/courses/bachelor-of-business-information-systems",
"https://www.latrobe.edu.au/courses/bachelor-of-business-information-systems-honours",
"https://www.latrobe.edu.au/courses/bachelor-of-international-business",
"https://www.latrobe.edu.au/courses/bachelor-of-politics-philosophy-and-economics",
"https://www.latrobe.edu.au/courses/bachelor-of-arts",
"https://www.latrobe.edu.au/courses/bachelor-of-early-childhood-and-primary-education",
"https://www.latrobe.edu.au/courses/bachelor-of-education-primary",
"https://www.latrobe.edu.au/courses/bachelor-of-education-secondary",
"https://www.latrobe.edu.au/courses/bachelor-of-educational-studies",
"https://www.latrobe.edu.au/courses/bachelor-of-outdoor-education",
"https://www.latrobe.edu.au/courses/bachelor-of-outdoor-recreation-education",
"https://www.latrobe.edu.au/courses/bachelor-of-physical-health-and-outdoor-education",
"https://www.latrobe.edu.au/courses/bachelor-of-biomedical-science",
"https://www.latrobe.edu.au/courses/bachelor-of-biomedicine",
"https://www.latrobe.edu.au/courses/bachelor-of-health-sciences",
"https://www.latrobe.edu.au/courses/bachelor-of-science",
"https://www.latrobe.edu.au/courses/bachelor-of-exercise-science",
"https://www.latrobe.edu.au/courses/bachelor-of-exercise-science-and-master-of-exercise-physiology",
"https://www.latrobe.edu.au/courses/bachelor-of-human-nutrition",
"https://www.latrobe.edu.au/courses/bachelor-of-nursing-pre-registration",
"https://www.latrobe.edu.au/courses/bachelor-of-oral-health-science",
"https://www.latrobe.edu.au/courses/bachelor-of-paramedic-practice-with-honours",
"https://www.latrobe.edu.au/courses/bachelor-of-pharmacy-honours",
"https://www.latrobe.edu.au/courses/bachelor-of-sports-and-exercise-science",
"https://www.latrobe.edu.au/courses/bachelor-of-cybersecurity",
"https://www.latrobe.edu.au/courses/bachelor-of-engineering-honours-industrial",
"https://www.latrobe.edu.au/courses/bachelor-of-information-technology",
"https://www.latrobe.edu.au/courses/bachelor-of-business-information-systems",
"https://www.latrobe.edu.au/courses/bachelor-of-business-information-systems-honours",
"https://www.latrobe.edu.au/courses/bachelor-of-civil-engineering-honours",
"https://www.latrobe.edu.au/courses/bachelor-of-computer-science",
"https://www.latrobe.edu.au/courses/bachelor-of-information-technology-honours",
"https://www.latrobe.edu.au/courses/bachelor-of-criminology",
"https://www.latrobe.edu.au/courses/bachelor-of-laws",
"https://www.latrobe.edu.au/courses/bachelor-of-laws-graduate-entry",
"https://www.latrobe.edu.au/courses/bachelor-of-biomedical-science",
"https://www.latrobe.edu.au/courses/bachelor-of-science",
"https://www.latrobe.edu.au/courses/bachelor-of-agricultural-sciences",
"https://www.latrobe.edu.au/courses/bachelor-of-animal-and-veterinary-biosciences",
"https://www.latrobe.edu.au/courses/bachelor-of-biological-sciences",
"https://www.latrobe.edu.au/courses/bachelor-of-business-agribusiness",
"https://www.latrobe.edu.au/courses/bachelor-of-politics-philosophy-and-economics",
"https://www.latrobe.edu.au/courses/bachelor-of-science-wildlife-and-conservation-biology",
"https://www.latrobe.edu.au/courses/bachelor-of-veterinary-nursing", ]
    # print(len(start_urls))
    start_urls=list(set(start_urls))
    # print(len(start_urls))
    headers_base = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    def parse(self, response):
        # print("============", response.url)
        is_research = response.xpath("//div[@class='title']/h1//text()").extract()
        # print("is_research: ", is_research)

        if "research" not in ''.join(is_research).lower() and "online" not in ''.join(is_research).lower():
            pro_url=re.findall('https?://www.latrobe.edu.au/courses/data/2019/international/[a-z\-/]+', response.text,re.S)
            # print("pro_url: ", pro_url)
            if pro_url!=[]:
                for pu in pro_url:
                    # print(pu)
                    if "international/bu" in pu:
                        # print("melbur")
                        yield scrapy.Request(url=pu, callback=self.parses)
            # print(pro_url)

    def parses(self, response):
        item=get_item(ScrapyschoolAustralianBenItem)
        item['university'] = 'La Trobe University'
        item['url'] = response.url
        # item['location']='Melbourne'
        item['degree_type'] = 1
        print("================================================")
        print(response.url)
        try:
            # 学位名称
            degree_name = response.xpath('//h1[contains(text(),"Bachelor of")]/text()').extract()
            clear_space(degree_name)
            item['degree_name'] = ''.join(degree_name).strip()
            print("item['degree_name']: ", item['degree_name'])

            pro_re = re.findall(r"Bachelor", item['degree_name'].replace("(Honours)", ""))
            # print("pre_re: ", pro_re)
            if len(pro_re) < 2:
                programme_re = re.findall(r"\(.+\)", item['degree_name'].replace("(Advanced)", "").replace("(Honours)", "").strip())
                if len(programme_re) > 0:
                    item['programme_en'] = ''.join(programme_re).replace("(", "").replace(")", "").strip()
                else:
                    item['programme_en'] = item['degree_name'].replace("Bachelor of", "").replace("(Honours)", "").replace("Master of ", "").strip()
                print("item['programme_en']: ", item['programme_en'])

                start_date = response.xpath('//div[contains(text(),"tart")]/following-sibling::div//text()').extract()
                # print('start_date: ',start_date)
                item['start_date'] = getStartDateMonth(''.join(start_date))
                if item['start_date'] == "":
                    item['start_date'] = ''.join(start_date).strip()
                # print("item['start_date']: ", item['start_date'])

                duration = response.xpath('//div[contains(text(),"uration")]/following-sibling::div//text()').extract()
                # print('duration: ',duration)
                item['duration'] = ''.join(duration).strip()
                # print("item['duration']: ", item['duration'])

                fee = response.xpath('//h3[contains(text(),"tuition fee")]/following-sibling::p[1]/text()').extract()
                # print('fee: ',fee)
                fee = ''.join(fee).strip()
                tuition = fee.replace(' ','')
                item['tuition_fee']=tuition[0:99]
                # print("item['tuition_fee']: ", item['tuition_fee'])

                overview = response.xpath('//section[@id="overview"]/div[@class="block"]').extract()
                item['degree_overview_en'] = remove_class(clear_lianxu_space(overview))
                # print("item['degree_overview_en']: ", item['degree_overview_en'])

                rntry = response.xpath('//section[@id="entry-requirements"]').extract()
                item['rntry_requirements_en'] = remove_class(clear_lianxu_space(rntry))
                # print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

                career = response.xpath('//section[@id="career-outcomes"]').extract()
                item['career_en'] = remove_class(clear_lianxu_space(career))
                # print("item['career_en']: ", item['career_en'])

                htp = response.xpath('//section[@id="how-to-apply"]').extract()
                item['apply_desc_en'] = remove_class(clear_lianxu_space(htp))
                # print("item['apply_desc_en']: ", item['apply_desc_en'])

                # //ul[@class='list-arrows']//li
                location_dict = {'BU': 'Melbourne',
'BE': 'Bendigo',
'CI': 'City',
'MI': 'Mildura',
'OT': 'Other',
'FS': 'Franklin Street',
'SH': 'Shepparton',
'SY': 'Sydney',
'ON': 'Online',
'WO': 'Albury-Wodonga',}
                location = response.xpath("//ul[@class='list-arrows']//li//text()").extract()
                # print("location: ", location)
                item['location'] = ''.join(location).replace("(Bundoora)", "").strip()
                if item['location'] == "":
                    location_key = response.url.replace("https://www.latrobe.edu.au/courses/data/2019/international/", "").strip()
                    # print("location_key1: ", location_key)
                    location_key = location_key.split("/")[0]
                    # print("location_key: ", location_key)
                    item['location'] = location_dict.get(''.join(location_key).upper())
                # print("item['location']: ", item['location'])

                ielts = response.xpath('//p[contains(text(),"IELTS")]/text()').extract()
                item['ielts_desc'] = ''.join(ielts).strip()
                # print("item['ielts_desc']: ", item['ielts_desc'])

                ielts = get_ielts(item['ielts_desc'])
                item['ielts'] = ielts.get('IELTS')
                item['ielts_l'] = ielts.get('IELTS_L')
                item['ielts_s'] = ielts.get('IELTS_S')
                item['ielts_r'] = ielts.get('IELTS_R')
                item['ielts_w'] = ielts.get('IELTS_W')
                # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                #        item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

                modules_url = response.xpath('//ul[@class="list-arrows"]/li[1]/a/@href').extract()
                clear_space(modules_url)
                if modules_url!=[]:
                    try:
                        item['modules_en'] = self.parse_modules(modules_url[0])
                    except:
                        item['modules_en'] = ""
                # print("item['modules_en']: ", item['modules_en'])

                item['apply_proces_en'] = "https://www.latrobe.edu.au/international/how-to-apply/undergraduate-and-postgraduate"

                item['overview_en'] = item['degree_overview_en']
                # programme_major = response.xpath('//section[@id="overview"]/div[@class="block"]//ul/li').extract()
                programme_major = response.xpath(
                    # '//p[contains(text(),"Our Majors are:")]/following-sibling::ul/li|'
                    '//p[contains(text(),"Melbourne majors")]/following-sibling::ul[1]/li|'
                    '//p[contains(text(),"Choose from five majors")]/following-sibling::ul[1]/li|'
                    '//th[contains(text(),"Minors")]/../preceding-sibling::*//td[contains(text(),"Yes")][1]/preceding-sibling::td|'
                    '//p[contains(text(),"disciplines:")]/following-sibling::ul[1]/li|'
                    # '//th[contains(text(),"Minors")]/../preceding-sibling::tr|'
                    '//p[contains(text(),"subjects and electives including")]/following-sibling::ul[1]/li').extract()
                print(len(programme_major))
                if len(programme_major) == 0:
                    yield item
                else:
                    for maj in programme_major:
                        print("***************************"+str(programme_major.index(maj)+1)+"****************************")
                        programme_major1 = response.xpath(
                            # '//p[contains(text(),"Our Majors are:")]/following-sibling::ul/li|'
                            '//p[contains(text(),"Melbourne majors")]/following-sibling::ul[1]/li//a[contains(text(),'+'"'+remove_tags(maj)+'"'+')]/@href|'
                            '//p[contains(text(),"Choose from five majors")]/following-sibling::ul[1]/li//a[contains(text(),'+'"'+remove_tags(maj)+'"'+')]/@href|'
                            '//th[contains(text(),"Minors")]/../preceding-sibling::*//td[contains(text(),"Yes")][1]/preceding-sibling::td//a[contains(text(),'+'"'+remove_tags(maj)+'"'+')]/@href|'
                            '//p[contains(text(),"disciplines:")]/following-sibling::ul[1]/li//a[contains(text(),'+'"'+remove_tags(maj)+'"'+')]/@href|'
                            # '//th[contains(text(),"Minors")]/../preceding-sibling::tr|'
                            '//p[contains(text(),"subjects and electives including")]/following-sibling::ul[1]/li//a[contains(text(),'+'"'+remove_tags(maj)+'"'+')]/@href').extract()
                        # programme_major1 = response.xpath("//a[contains(text(),"+"'"+remove_tags(maj)+"'"+")]/@href").extract()
                        if len(programme_major1) == 0:
                            item['programme_en'] = remove_tags(maj).replace("Yes", "").replace("*", "").strip()
                            print("不用跳转的item['programme_en']_major: ", item['programme_en'])
                            yield item
                        else:
                            programme_dict_list = self.parse_major(programme_major1[0], remove_tags(maj))
                            print("programme_dict_list: ", programme_dict_list)
                            for programme_dict in programme_dict_list:
                                item['programme_en'] = programme_dict.get('programme_en')
                                item['overview_en'] = programme_dict.get('overview_en')

                                # item['programme_en'] = ''.join(programme_major1).strip()
                                print("跳转之后的链接item['programme_en']_major: ", item['programme_en'])
                                print("跳转之后的链接item['overview_en']_major: ", item['overview_en'])
                                yield item
                        # programme_major1 = response.xpath(
                        #                     # '//p[contains(text(),"Our Majors are:")]/following-sibling::ul[1]/li['+str(i+1)+']//a/@href|'
                        #                      '//p[contains(text(),"Melbourne majors")]/following-sibling::ul[1]/li['+str(i+1)+']//a/@href'
                        #                     '//p[contains(text(),"Choose from five majors")]/following-sibling::ul[1]/li['+str(i+1)+']//a/@href|'
                        #                     # '//h3[contains(text(),"Specialisations, majors and minors")]/following-sibling::table/tbody/tr|'
                        #                     '//p[contains(text(),"disciplines:")]/following-sibling::ul/li['+str(i+1)+']//a/@href|'
                        #                     '//th[contains(text(),"Minors")]/../preceding-sibling::tr['+str(i+1)+']//a/@href|'
                        #                     '//p[contains(text(),"subjects and electives including")]/following-sibling::ul[1]/li['+str(i+1)+']//a/@href').extract()
                        # clear_space(programme_major1)
                        # print("programme_major1: ", programme_major1)
                        # if len(programme_major1) > 0:
                        #     major_url = programme_major1[0]
                        #     programme_dict_list = self.parse_major(major_url)
                        #     print("programme_dict_list: ", programme_dict_list)
                        #     for programme_dict in programme_dict_list:
                        #         item['programme_en'] = programme_dict.get('programme_en')
                        #         item['overview_en'] = programme_dict.get('overview_en')
                        #
                        #         # item['programme_en'] = ''.join(programme_major1).strip()
                        #         print("跳转之后的链接item['programme_en']_major: ", item['programme_en'])
                        #         print("跳转之后的链接item['overview_en']_major: ", item['overview_en'])
                        #         yield item
                        # else:
                        #     programme_major1 = response.xpath(
                        #         '//p[contains(text(),"Our Majors are:")]/following-sibling::ul[1]/li['+str(i+1)+']//text()|'
                        #         '//p[contains(text(),"Choose from five majors")]/following-sibling::ul[1]/li['+str(i+1)+']//text()|'
                        #         # '//h3[contains(text(),"Specialisations, majors and minors")]/following-sibling::table/tbody/tr|'
                        #         '//p[contains(text(),"disciplines:")]/following-sibling::ul[1]/li['+ str(i+1)+']//text()|'
                        #         '//th[contains(text(),"Minors")]/../preceding-sibling::tr['+str(i+1)+']//text()|'
                        #         '//p[contains(text(),"subjects and electives including")]/following-sibling::ul[1]/li['+str(i+1)+']//text()').extract()
                        #     item['programme_en'] = ''.join(programme_major1).replace("Yes", "").replace("*", "").strip()
                        #     print("不用跳转的item['programme_en']_major: ", item['programme_en'])
                        #     yield item
        except Exception as e:
            with open("scrapySchool_Australian_ben/error/" + item['university'] + str(item['degree_type']) + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_modules(self, modulesUrl):
        # print("modulesUrl: ", modulesUrl)
        data = requests.get(modulesUrl, headers=self.headers_base)
        response = etree.HTML(data.text)

        modules = response.xpath("//h3[contains(text(),'Course structure')]|//h3[contains(text(),'Course structure')]/following-sibling::*[position()<last()]|"
                                "//h3[contains(text(),'Course Structure')]|//h3[contains(text(),'Course Structure')]/following-sibling::*[position()<last()]")
        modules_str = ""
        if len(modules) > 0:
            for m in modules:
                modules_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
        modules_en = remove_class(clear_lianxu_space([modules_str]))
        return modules_en

    def parse_major(self, majorUrl, maj):
        print("majorUrl: ", majorUrl)
        data = requests.get(majorUrl, headers=self.headers_base)
        response = etree.HTML(data.text)
        programme_dict = {}
        # ul_major = response.xpath("//div[@id='why_study']//ul[@type='disc']/li//a/@href")
        ul_major = response.xpath("//div[@id='why_study']//ul[@type='disc']/li//a[contains(text()," + "'" + remove_tags(maj) + "'" + ")]/@href")
        clear_space(ul_major)
        print("ul_major: ", ul_major)
        programme_dict_list = []
        if len(ul_major) == 0:
            programme = response.xpath("//h1//text()")
            programme_str = ''.join(programme).strip()
            programme_dict['programme_en'] = programme_str

            overview_en = response.xpath("//div[@id='overview']|//div[@id='why_study']")
            overview_en_str = ""
            if len(overview_en) > 0:
                for m in overview_en:
                    overview_en_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
            overview_en = remove_class(clear_lianxu_space([overview_en_str]))
            programme_dict['overview_en'] = overview_en
            print("overview_en: ", overview_en)
            programme_dict_list.append(programme_dict)
            # return programme_dict
        else:
            # for ul in ul_major:
            programme_dict = self.parse_major_major(ul_major[0])
            programme_dict_list.append(programme_dict)
        return programme_dict_list

    def parse_major_major(self, majorUrl):
        print("major_majorUrl: ", majorUrl)
        data = requests.get(majorUrl, headers=self.headers_base)
        response = etree.HTML(data.text)
        programme_dict = {}
        programme = response.xpath("//h1//text()")
        programme_str = ''.join(programme).strip()
        programme_dict['programme_en'] = programme_str

        overview_en = response.xpath("//div[@id='intro_txt']")
        overview_en_str = ""
        if len(overview_en) > 0:
            for m in overview_en:
                overview_en_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
        overview_en = remove_class(clear_lianxu_space([overview_en_str]))
        programme_dict['overview_en'] = overview_en

        career_en = response.xpath("//div[@id='intro_txt_2']")
        career_en_str = ""
        if len(career_en) > 0:
            for m in career_en:
                career_en_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
        career_en = remove_class(clear_lianxu_space([career_en_str]))
        programme_dict['career_en'] = career_en
        return programme_dict