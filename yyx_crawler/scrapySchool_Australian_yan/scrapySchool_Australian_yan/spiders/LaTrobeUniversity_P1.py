# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
import requests
# from scrapyNewAustralia.middlewares import *
# from scrapyNewAustralia.items import ScrapynewaustraliaItem
from scrapySchool_Australian_yan.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_yan.getItem import get_item
from scrapySchool_Australian_yan.getTuition_fee import getTuition_fee
from scrapySchool_Australian_yan.items import ScrapyschoolAustralianYanItem
from scrapySchool_Australian_yan.remove_tags import remove_class
from scrapySchool_Australian_yan.getStartDate import getStartDateMonth
from scrapySchool_Australian_yan.getIELTS import get_ielts
import re
from w3lib.html import remove_tags

class Latrobeuniversity_P1Spider(scrapy.Spider):
    name = 'LaTrobeUniversity_P1'

#     start_urls = ["https://www.latrobe.edu.au/courses/master-of-applied-linguistics2",
# "https://www.latrobe.edu.au/courses/master-of-clinical-neuropsychology",
# "https://www.latrobe.edu.au/courses/master-of-clinical-psychology",
# "https://www.latrobe.edu.au/courses/master-of-communication-journalism-innovation",
# "https://www.latrobe.edu.au/courses/master-of-communication-public-relations",
# "https://www.latrobe.edu.au/courses/master-of-community-planning-and-development",
# "https://www.latrobe.edu.au/courses/master-of-international-development",
# "https://www.latrobe.edu.au/courses/master-of-international-relations",
# "https://www.latrobe.edu.au/courses/master-of-professional-archaeology",
# "https://www.latrobe.edu.au/courses/master-of-social-work",
# "https://www.latrobe.edu.au/courses/master-of-business-administration",
# "https://www.latrobe.edu.au/courses/master-of-business-analytics",
# "https://www.latrobe.edu.au/courses/master-of-cybersecurity-business-operations",
# "https://www.latrobe.edu.au/courses/master-of-cybersecurity-computer-science",
# "https://www.latrobe.edu.au/courses/master-of-cybersecurity-law",
# "https://www.latrobe.edu.au/courses/master-of-accounting-and-financial-management",
# "https://www.latrobe.edu.au/courses/master-of-biotechnology-management",
# "https://www.latrobe.edu.au/courses/master-of-business-administration-advanced",
# "https://www.latrobe.edu.au/courses/master-of-business-administration-and-master-of-health-administration",
# "https://www.latrobe.edu.au/courses/master-of-business-information-management-and-systems",
# "https://www.latrobe.edu.au/courses/master-of-engineering-management",
# "https://www.latrobe.edu.au/courses/master-of-financial-analysis",
# "https://www.latrobe.edu.au/courses/master-of-financial-analysis-financial-risk-management",
# "https://www.latrobe.edu.au/courses/master-of-financial-analysis-investment",
# "https://www.latrobe.edu.au/courses/master-of-financial-analysis-master-of-business-administration",
# "https://www.latrobe.edu.au/courses/master-of-financial-analysis-master-of-international-business",
# "https://www.latrobe.edu.au/courses/master-of-financial-analysis-master-of-professional-accounting",
# "https://www.latrobe.edu.au/courses/master-of-international-business",
# "https://www.latrobe.edu.au/courses/master-of-management",
# "https://www.latrobe.edu.au/courses/master-of-management-corporate-governance-and-risk",
# "https://www.latrobe.edu.au/courses/master-of-management-entrepreneurship-and-innovation",
# "https://www.latrobe.edu.au/courses/master-of-management-human-resource-management",
# "https://www.latrobe.edu.au/courses/master-of-management-project-management",
# "https://www.latrobe.edu.au/courses/master-of-management-sport-management",
# "https://www.latrobe.edu.au/courses/master-of-professional-accounting",
# "https://www.latrobe.edu.au/courses/master-of-professional-accounting-business-analytics",
# "https://www.latrobe.edu.au/courses/master-of-professional-accounting-cpa-australia-extension",
# "https://www.latrobe.edu.au/courses/master-of-professional-accounting-information-systems-management",
# "https://www.latrobe.edu.au/courses/master-of-teaching-primary",
# "https://www.latrobe.edu.au/courses/master-of-teaching-secondary",
# "https://www.latrobe.edu.au/courses/master-of-applied-linguistics2",
# "https://www.latrobe.edu.au/courses/master-of-education",
# "https://www.latrobe.edu.au/courses/master-of-educational-leadership-and-management",
# "https://www.latrobe.edu.au/courses/master-of-special-education",
# "https://www.latrobe.edu.au/courses/master-of-teaching-english-to-speakers-of-other-languages-tesol",
# "https://www.latrobe.edu.au/courses/master-of-sports-analytics",
# "https://www.latrobe.edu.au/courses/master-of-art-therapy",
# "https://www.latrobe.edu.au/courses/master-of-business-administration-and-master-of-health-administration",
# "https://www.latrobe.edu.au/courses/master-of-clinical-audiology",
# "https://www.latrobe.edu.au/courses/master-of-clinical-prosthetics-and-orthotics",
# "https://www.latrobe.edu.au/courses/master-of-dietetic-practice",
# "https://www.latrobe.edu.au/courses/master-of-exercise-physiology",
# "https://www.latrobe.edu.au/courses/master-of-health-administration",
# "https://www.latrobe.edu.au/courses/master-of-health-information-management",
# "https://www.latrobe.edu.au/courses/master-of-health-sciences",
# "https://www.latrobe.edu.au/courses/master-of-nursing-science",
# "https://www.latrobe.edu.au/courses/master-of-occupational-therapy-practice",
# "https://www.latrobe.edu.au/courses/master-of-orthoptics",
# "https://www.latrobe.edu.au/courses/master-of-physiotherapy-practice",
# "https://www.latrobe.edu.au/courses/master-of-podiatric-practice",
# "https://www.latrobe.edu.au/courses/master-of-public-health",
# "https://www.latrobe.edu.au/courses/master-of-public-health-and-master-of-health-administration",
# "https://www.latrobe.edu.au/courses/master-of-social-work",
# "https://www.latrobe.edu.au/courses/master-of-speech-pathology",
# "https://www.latrobe.edu.au/courses/master-of-teaching-english-to-speakers-of-other-languages-tesol",
# "https://www.latrobe.edu.au/courses/master-of-business-analytics",
# "https://www.latrobe.edu.au/courses/master-of-cybersecurity-business-operations",
# "https://www.latrobe.edu.au/courses/master-of-cybersecurity-computer-science",
# "https://www.latrobe.edu.au/courses/master-of-cybersecurity-law",
# "https://www.latrobe.edu.au/courses/master-of-data-science",
# "https://www.latrobe.edu.au/courses/master-of-sports-analytics",
# "https://www.latrobe.edu.au/courses/master-of-computer-science",
# "https://www.latrobe.edu.au/courses/master-of-electronic-engineering",
# "https://www.latrobe.edu.au/courses/master-of-engineering-civil",
# "https://www.latrobe.edu.au/courses/master-of-engineering-electronics",
# "https://www.latrobe.edu.au/courses/master-of-engineering-manufacturing",
# "https://www.latrobe.edu.au/courses/master-of-engineering-management",
# "https://www.latrobe.edu.au/courses/master-of-information-and-communication-technology",
# "https://www.latrobe.edu.au/courses/master-of-information-technology",
# "https://www.latrobe.edu.au/courses/master-of-information-technology-computer-networks",
# "https://www.latrobe.edu.au/courses/master-of-professional-accounting-information-systems-management",
# "https://www.latrobe.edu.au/courses/master-of-telecommunication-and-network-engineering",
# "https://www.latrobe.edu.au/courses/master-of-cybersecurity-law",
# "https://www.latrobe.edu.au/courses/master-of-laws",
# "https://www.latrobe.edu.au/courses/master-of-laws-in-global-business-law",
# "https://www.latrobe.edu.au/courses/master-of-data-science",
# "https://www.latrobe.edu.au/courses/master-of-biotechnology-and-bioinformatics",
# "https://www.latrobe.edu.au/courses/master-of-biotechnology-management",
# "https://www.latrobe.edu.au/courses/master-of-chemical-sciences",
# "https://www.latrobe.edu.au/courses/master-of-nanotechnology",
# "https://www.latrobe.edu.au/courses/master-of-science-in-physical-sciences", ]
    start_urls = ["http://www.latrobe.edu.au/courses/master-of-teaching-secondary",
"http://www.latrobe.edu.au/courses/master-of-marketing",
"http://www.latrobe.edu.au/courses/master-of-business-administration-advanced",
"http://www.latrobe.edu.au/courses/master-of-engineering",
"http://www.latrobe.edu.au/courses/bachelor-of-human-services-and-master-of-social-work",
"http://www.latrobe.edu.au/courses/bachelor-of-exercise-science-and-master-of-exercise-physiology",
"http://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-physiotherapy-practice",
"http://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-speech-pathology",
"http://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-podiatric-practice",
"http://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-orthoptics",
"http://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-clinical-audiology",
"http://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-dietetic-practice",
"http://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-occupational-therapy-practice",
"http://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-clinical-prosthetics-and-orthotics",
"http://www.latrobe.edu.au/courses/master-of-agricultural-science",
"http://www.latrobe.edu.au/courses/master-of-psychological-science", ]
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
                    yield scrapy.Request(url=pu, callback=self.parses)
            # print(pro_url)

    def parses(self, response):
        item=get_item(ScrapyschoolAustralianYanItem)
        item['university'] = 'La Trobe University'
        item['url'] = response.url
        # item['location']='Melbourne'
        item['degree_type'] = 2
        item['teach_time'] = 'coursework'
        print("================================================")
        print(response.url)

        try:
            # 学位名称
            degree_name = response.xpath('//h1[contains(text(),"Master of")]/text()').extract()
            clear_space(degree_name)
            item['degree_name'] = ''.join(degree_name).strip()
            print("item['degree_name']: ", item['degree_name'])

            pro_re = re.findall(r"Master", item['degree_name'])
            # print("pre_re: ", pro_re)
            if len(pro_re) < 2:
                programme_re = re.findall(r"\(.+\)", item['degree_name'].replace("(Advanced)", "").strip())
                if len(programme_re) > 0:
                    item['programme_en'] = ''.join(programme_re).replace("(", "").replace(")", "").strip()
                else:
                    item['programme_en'] = item['degree_name'].replace("Master of", "").strip()
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

                work_experience_desc_en = response.xpath("//section[@id='entry-requirements']//p[contains(text(), 'work experience')]").extract()
                item['work_experience_desc_en'] = remove_class(clear_lianxu_space(work_experience_desc_en))
                if item['work_experience_desc_en'] == "":
                    work_experience_desc_en = re.findall(r"<.{1,200}work\sexperience.{1,200}>", response.text)
                    item['work_experience_desc_en'] = "<p>" + remove_tags(clear_lianxu_space(work_experience_desc_en)) + "</p>"
                    item['work_experience_desc_en'] = item['work_experience_desc_en'].replace("<p></p>", "")
                # print("item['work_experience_desc_en']: ", item['work_experience_desc_en'])

                item['apply_proces_en'] = "https://www.latrobe.edu.au/international/how-to-apply/undergraduate-and-postgraduate"

                item['overview_en'] = item['degree_overview_en']
                programme_major = response.xpath('//section[@id="overview"]/div[@class="block"]//ul/li').extract()
                print(len(programme_major))
                if len(programme_major) == 0:
                    yield item
                else:
                    for i in range(len(programme_major)):
                        print("***************************"+str(i+1)+"****************************")
                        programme_major1 = response.xpath('//section[@id="overview"]/div[@class="block"]//ul/li['+str(i+1)+']//text()').extract()
                        item['programme_en'] = ''.join(programme_major1).strip()
                        print("item['programme_en']_major: ", item['programme_en'])
                        yield item
                degree_name_list=response.xpath('//p[contains(text(),"Our Majors are:")]/following-sibling::ul/li//text()|'
                                                '//p[contains(text(),"Choose from five majors")]/following-sibling::ul[1]/li/text()|'
                                                '//h3[contains(text(),"Specialisations, majors and minors")]/following-sibling::table/tbody/tr/td[1]//text()').extract()

        except Exception as e:
            with open("scrapySchool_Australian_yan/error/" + item['university'] + str(item['degree_type']) + ".txt",
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