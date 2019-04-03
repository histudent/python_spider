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
from scrapySchool_Australian_ben.getIELTS import get_ielts


# 2019/03/21 星期四 数据更新
class UniversityofTechnologySydney_USpider(scrapy.Spider):
    name = "UniversityofTechnologySydney_U"
    start_urls = ["https://www.uts.edu.au/future-students/find-a-course/search?search=#panel-postgraduate"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        links = response.xpath(
            "//div[@id='panel-undergraduate']//div[1]//tr//td[1]/a/@href|"
            "//div[@id='panel-undergraduate']//div[2]//tr//td[1]/a/@href|"
            "//div[@id='panel-undergraduate']//div[5]//tr//td[1]/a/@href").extract()
        # print(len(links))
        # links = list(set(links))
        # print(len(links))

        # 组合字典
        programme_dict = {}
        programme_list = response.xpath(
            "//div[@id='panel-undergraduate']//div[1]//tr//td[1]/a//text()|"
            "//div[@id='panel-undergraduate']//div[2]//tr//td[1]/a//text()|"
            "//div[@id='panel-undergraduate']//div[5]//tr//td[1]/a//text()").extract()
        clear_space(programme_list)

        for link in range(len(links)):
            url = "https://www.uts.edu.au" + links[link]
            programme_dict[url] = programme_list[link]

        clear_space(links)

#         links = ["https://www.uts.edu.au/future-students/find-a-course/bachelor-laws-honours",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-laws-honours",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-science-information-technology",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-science-information-technology",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-engineering-honours",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-engineering-honours",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-science-information-technology-diploma-information",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-science-information-technology-diploma-information",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-engineering-honours-diploma-professional-engineering",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-engineering-honours-diploma-professional-engineering",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-engineering-science",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-engineering-science",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-science-games-development",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-science-games-development",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-sport-and-exercise-science",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-management",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-computing-science-honours",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-sport-and-exercise-management",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-economics",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-communication-social-and-political-sciences",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-communication-social-and-political-sciences",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-communication-creative-writing",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-communication-creative-writing",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-environmental-biology",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-environmental-biology",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-biomedical-physics",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-biomedical-physics",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-fashion-and-textiles",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-fashion-and-textiles",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-honours-interior-architecture",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-honours-interior-architecture",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-medical-science",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-medical-science",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-global-studies",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-global-studies",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-advanced-science",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-advanced-science",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-honours-photography",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-honours-photography",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-interior-architecture",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-interior-architecture",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-property-economics",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-property-economics",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-biomedical-science",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-biomedical-science",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-marine-biology",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-marine-biology",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-health-science",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-health-science",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-laws",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-laws",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-business",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-business",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-honours-fashion-and-textiles",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-honours-fashion-and-textiles",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-communication-media-arts-and-production",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-communication-media-arts-and-production",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-medicinal-chemistry",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-medicinal-chemistry",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-communication-public-communication",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-communication-public-communication",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-animation",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-animation",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-nursing",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-nursing",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-biotechnology",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-biotechnology",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-construction-project-management",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-construction-project-management",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-visual-communication",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-visual-communication",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-science",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-science",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-music-and-sound-design",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-music-and-sound-design",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-honours-architecture",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-honours-architecture",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-honours-product-design",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-honours-product-design",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-architecture",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-architecture",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-communication-journalism",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-communication-journalism",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-landscape-architecture-honours",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-landscape-architecture-honours",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-health-science-traditional-chinese-medicine",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-health-science-traditional-chinese-medicine",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-product-design",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-product-design",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-communication-digital-and-social-media",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-communication-digital-and-social-media",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-photography",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-photography",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-science-analytics",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-science-analytics",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-forensic-science",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-forensic-science",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-technology-and-innovation",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-technology-and-innovation",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-honours-animation",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-design-honours-animation",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-arts-educational-studies",
# "https://www.uts.edu.au/future-students/find-a-course/bachelor-arts-educational-studies",]
#         print(len(links))
#         links = list(set(links))
#         print(len(links))

        for link1 in links:
            url = "https://www.uts.edu.au" + link1
            # url = link1
            yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "University of Technology Sydney"
        # item['country'] = 'Australia'
        # item['website'] = 'https://www.uts.edu.au'
        item['url'] = response.url
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        item['major_type1'] = response.meta.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            # 2019/03/21 div的class值多了个空格，使用contains
            programme = response.xpath('//div[@class="field-item"]/div[contains(@class,"page-title")]/h1//text()').extract()
            clear_space(programme)
            programme = ''.join(programme).strip()
            item['degree_name'] = programme
            print("item['degree_name']: ", item['degree_name'])

            de_p = re.findall(r"\(.+\)", item['degree_name'])
            if len(de_p) > 0:
                de_s = ''.join(de_p).strip()
                if de_s != "(Honours)":
                    item['programme_en'] = de_s.replace("(", "").replace(")", "").strip()
                else:
                    item['programme_en'] = item['degree_name'].replace("Bachelor of", "").replace("(Honours)", "").strip()
            else:
                item['programme_en'] = item['degree_name'].replace("Bachelor of", "").replace("(Honours)", "").strip()
            pro_re = re.findall(r"in\s.*", item['degree_name'])
            if len(pro_re) > 0:
                de_s = ''.join(pro_re).replace("in", "").strip()
                item['programme_en'] = de_s
            print("item['programme_en']: ", item['programme_en'])

            start_date = response.xpath(
                "//dt[contains(text(),'UAC')]/following-sibling::dd/span//text()").extract()
            clear_space(start_date)
            print(start_date)
            if len(start_date) > 0:
                start_date_re = re.findall(r"\w+\ssession", ' '.join(start_date))
                start_date_re = list(set(start_date_re))
                print("start_date_re: ", start_date_re)
                item['start_date'] = ','.join(start_date_re).replace("(", "").replace(")", "").replace(" session",
                                                                                                       "").strip()
            print("item['start_date']: ", item['start_date'])

            overview = response.xpath('//div[@class="field field-dddd-view-modeluts-course-course__overview field-type-ds field-label-hidden"]').extract()
            item['degree_overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['degree_overview_en']: ", item['degree_overview_en'])

            career = response.xpath('//div[@class="field field-dddd-view-modeluts-course-course__careers field-type-ds field-label-hidden"]').extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            modules = response.xpath("//div[@class='course__structure']").extract()
            if len(modules) == 0:
                print("*********")
                # modules = response.xpath("//div[@class='course__structure']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            print("item['modules_en']: ", item['modules_en'])

            location = response.xpath('//div[@class="field field-dddd-view-modeluts-course-course__location field-type-ds field-label-hidden"]//p//text()').extract()
            clear_space(location)
            location = ''.join(location).strip()
            item['location'] = location
            # print("item['location']: ", item['location'])

            duration = response.xpath('//div[@class="field field-dddd-view-modeluts-course-course__duration field-type-ds field-label-hidden"]//p//text()').extract()
            clear_space(duration)
            # print("duration: ", duration)
            if len(duration) > 0:
                duration = duration[0]
            # print(duration)
            if "or" in duration:
                duration = duration.strip("or").strip()
            mode = re.findall("\w+\stime$", duration)
            # print(mode)
            mode = ''.join(mode)
            # item['mode'] = mode
            # print("item['mode']: ", item['mode'])
            item['duration'] = ''.join(duration.replace(mode, "").strip())
            # print("item['duration']: ", item['duration'])

            # feeDict = {'C04006v6': '15000', 'C04007v7': '15000', 'C04008v6': '15000', 'C04018v6': '19015', 'C04037v6': '17570', 'C04038v8': '18650', 'C04048v7': '18650', 'C04052v4': '19770', 'C04055v4': '15585', 'C04067v7': '18650', 'C04090v5': '17930', 'C04094v5': '17570', 'C04097v2': '17930', 'C04098v3': '17570', 'C04106v5': '16005', 'C04108v3': '14790', 'C04109v7': '14790', 'C04140v11': '16005', 'C04143v8': '20575', 'C04145v4': '20575', 'C04147v5': '22280', 'C04149v4': '21415', 'C04157v8': '19770', 'C04158v4': '19015', 'C04160v7': '20985', 'C04203v4': '14790', 'C04210v1': '16895', 'C04218v5': '19770', 'C04222v1': '19770', 'C04224v4': '20985', 'C04226v4': '17570', 'C04227v3': '17570', 'C04228v2': '16005', 'C04229v3': '17570', 'C04231v2': '15145', 'C04232v3': '15145', 'C04234v1': '19770', 'C04235v2': '17570', 'C04236v3': '22280', 'C04237v3': '18650', 'C04238v3': '18650', 'C04239v2': '14150', 'C04241v2': '18280', 'C04242v1': '20575', 'C04243v3': '17270', 'C04244v1': '13520', 'C04245v1': '14790', 'C04246v2': '16005', 'C04248v1': '16280', 'C04250v2': '22280', 'C04251v1': '20575', 'C04252v2': '19015', 'C04253v2': '19015', 'C04254v1': '14790', 'C04255v1': '12300', 'C04257v1': '11145', 'C04258v3': '18650', 'C04259v2': '18650', 'C04260v2': '18650', 'C04261v2': '18650', 'C04262v1': '14790', 'C04264v1': '22280', 'C04265v2': '18280', 'C04266v1': '17270', 'C04267v1': '18280', 'C04268v1': '13340', 'C04269v2': '13340', 'C04270v1': '17570', 'C04271v2': '17930', 'C04272v2': '17570', 'C04273v2': '17930', 'C04274v1': '17570', 'C04275v1': '17570', 'C04277v2': '17930', 'C04278v2': '17570', 'C04279v2': '16005', 'C04281v2': '18650', 'C04284v2': '14150', 'C04285v1': '15000', 'C04286v1': '18650', 'C04287v1': '18650', 'C04288v1': '15000', 'C04289v1': '18650', 'C04290v1': '15000', 'C04291v1': '14150', 'C04292v1': '16005', 'C04293v2': '17930', 'C04294v1': '15585', 'C04295v2': '19770', 'C04296v2': '19015', 'C04297v2': '19770', 'C04298v1': '14790', 'C04299v1': '18280', 'C04300v1': '18650', 'C04301v1': '15000', 'C04302v1': '16005', 'C04303v1': '16005', 'C04304v3': '19015', 'C04305v1': '14415', 'C04306v1': '25070', 'C04307v1': '14415', 'C04309v2': '17930', 'C04314v1': '18650', 'C04315v1': '15585', 'C04316v2': '15000', 'C04317v1': '15000', 'C04319v1': '15000', 'C04320v1': '22280', 'C04321v1': '16565', 'C04322v1': '16005', 'C04323v1': '15585', 'C04324v2': '18650', 'C04325v2': '18650', 'C04368v1': '16895', 'C04369v1': '16895', 'C04371v1': '16895', 'C04372v1': '17930', 'C04373v1': '18650', 'C06006v5': '15000', 'C06009v8': '19015', 'C06017v7': '15000', 'C06033v4': '11145', 'C06037v4': '16005', 'C06041v6': '14790', 'C06058v7': '19770', 'C06096v3': '14415', 'C06097v1': '16895', 'C06099v1': '20575', 'C06100v2': '19015', 'C06101v1': '14790', 'C06102v1': '14790', 'C06103v1': '14790', 'C06104v1': '16565', 'C06105v1': '14790', 'C06106v1': '14790', 'C06107v1': '13340', 'C06108v1': '17930', 'C06109v1': '17570', 'C06110v1': '17570', 'C06113v1': '19770', 'C06114v2': '17930', 'C06115v2': '15000', 'C06116v1': '14415', 'C06118v2': '25070', 'C06119v1': '15585', 'C06121v1': '15585', 'C06122v1': '19015', 'C06123v1': '19770', 'C06124v1': '17930', 'C07002v7': '15000', 'C07004v4': '15000', 'C07012v7': '18650', 'C07018v5': '18650', 'C07019v6': '15000', 'C07021v8': '18650', 'C07027v8': '14150', 'C07028v9': '14150', 'C07029v7': '15000', 'C07044v4': '16005', 'C07048v7': '16005', 'C07073v5': '22280', 'C07074v5': '22280', 'C07075v4': '18280', 'C07078v3': '19015', 'C07080v7': '20985', 'C07107v3': '13520', 'C07112v4': '18650', 'C07113v3': '18650', 'C07118v1': '14790', 'C07119v1': '17270', 'C07120v2': '16895', 'C07122v1': '22280', 'C07124v1': '16005', 'C07125v1': '14790', 'C07126v1': '16005', 'C07128v1': '18650', 'C07129v1': '18650', 'C07132v1': '18650', 'C11001v5': '15000', 'C11005v5': '15000', 'C11008v7': '19015', 'C11015v8': '18650', 'C11017v5': '17570', 'C11021v5': '18650', 'C11027v5': '18650', 'C11039v4': '18650', 'C11048v3': '17930', 'C11051v3': '17570', 'C11054v2': '17570', 'C11125v4': '20575', 'C11128v3': '16005', 'C11130v4': '20575', 'C11142v7': '19770', 'C11145v7': '20985', 'C11198v3': '18650', 'C11199v4': '18650', 'C11206v3': '18650', 'C11210v2': '17270', 'C11211v2': '22280', 'C11215v4': '11145', 'C11216v1': '18280', 'C11217v1': '20575', 'C11223v1': '14790', 'C11225v1': '17270', 'C11227v1': '16895', 'C11229v1': '20575', 'C11230v2': '19015', 'C11232v1': '18280', 'C11234v1': '17270', 'C11235v1': '13340', 'C11236v1': '17930', 'C11237v1': '17570', 'C11238v1': '17930', 'C11239v1': '17570', 'C11242v1': '16005', 'C11245v1': '15000', 'C11247v1': '19770', 'C11248v1': '17930', 'C11249v2': '15000', 'C11254v1': '14415', 'C11257v1': '15000', 'C11260v2': '25070', 'C11262v1': '16005', 'C11264v1': '22280', 'C11265v1': '20575', 'C11270v1': '15000', 'C11271v1': '15000', 'C11274v1': '17930', 'C01001v2': '12810', 'C01002v2': '12810', 'C01003v2': '12810', 'C01004v2': '12810', 'C01005v2': '12810', 'C02001v2': '13850', 'C02018v5': '17570', 'C02019v3': '12810', 'C02020v2': '12810', 'C02024v4': '16005', 'C02025v5': '13520', 'C02026v4': '13520', 'C02028v6': '15000', 'C02029v4': '16280', 'C02030v3': '18280', 'C02031v3': '18280', 'C02037v4': '12810', 'C02039v3': '13340', 'C02041v4': '12810', 'C02047v1': '16280', 'C02048v4': '16005', 'C02050v1': '12810', 'C02056v1': '15000', 'C02057v1': '16005', 'C02058v2': '16005', 'C02059v1': '15000', 'C02060v1': '15000', 'C02061v1': '16005', 'C02062v1': '16005', 'C02063v1': '15000', 'C03001v4': '13850', 'C03002v5': '13850', 'C03012v4': '13850', 'C03017v5': '17570', 'C03018v3': '12810', 'C03024v7': '15000', 'C03025v4': '16280', 'C03026v6': '18280', 'C03029v4': '18280', 'C03032v4': '12810', 'C03034v3': '13340', 'C03044v2': '12810', 'C03046v3': '16005', 'C03047v2': '12810', 'C03048v3': '16005', 'C03049v3': '16005', 'C03050v3': '16005', 'C03051v1': '16280', 'C03053v1': '15000', 'C03054v1': '15000', 'C03055v1': '16005', 'C03056v1': '15000', 'C03057v1': '15000', 'C03058v1': '16005', 'C03059v1': '15000'}
            feeDict = {}
            cod = ["C09004v6",
"C09018v6",
"C09019v4",
"C09020v7",
"C09022v3",
"C09023v3",
"C09026v3",
"C09029v3",
"C09031v3",
"C09035v4",
"C09046v2",
"C09047v1",
"C09048v2",
"C09049v1",
"C09050v1",
"C09052v2",
"C09055v2",
"C09056v1",
"C09057v2",
"C09059v2",
"C09060v1",
"C09061v1",
"C09063v2",
"C09064v1",
"C09066v2",
"C09067v2",
"C09068v2",
"C09069v2",
"C09070v2",
"C09071v2",
"C09072v2",
"C09073v2",
"C09074v2",
"C09075v2",
"C09076v2",
"C09077v1",
"C09078v1",
"C09079v3",
"C09081v1",
"C09082v1",
"C09083v2",
"C09084v1",
"C09085v2",
"C09086v1",
"C09087v2",
"C09088v1",
"C09089v2",
"C09091v2",
"C09093v2",
"C09094v2",
"C09095v2",
"C09096v2",
"C09097v1",
"C09098v2",
"C09099v1",
"C09101v1",
"C09119v1",
"C09120v1",
"C09121v1",
"C10004v6",
"C10007v8",
"C10011v5",
"C10020v4",
"C10021v4",
"C10026v4",
"C10027v4",
"C10039v10",
"C10040v8",
"C10044v7",
"C10045v9",
"C10054v5",
"C10055v8",
"C10056v5",
"C10059v8",
"C10061v6",
"C10062v5",
"C10063v6",
"C10065v10",
"C10066v7",
"C10067v7",
"C10068v9",
"C10073v7",
"C10074v6",
"C10075v7",
"C10076v7",
"C10078v7",
"C10079v6",
"C10098v2",
"C10115v9",
"C10122v11",
"C10123v7",
"C10124v8",
"C10125v9",
"C10126v8",
"C10129v6",
"C10131v6",
"C10132v4",
"C10136v9",
"C10137v4",
"C10148v4",
"C10152v4",
"C10155v9",
"C10157v6",
"C10158v5",
"C10162v6",
"C10163v4",
"C10164v7",
"C10167v4",
"C10169v5",
"C10172v7",
"C10174v5",
"C10184v6",
"C10186v9",
"C10206v6",
"C10208v5",
"C10209v7",
"C10214v3",
"C10215v3",
"C10219v4",
"C10223v2",
"C10224v3",
"C10226v6",
"C10227v4",
"C10228v5",
"C10229v4",
"C10239v1",
"C10242v2",
"C10243v2",
"C10244v2",
"C10245v3",
"C10246v1",
"C10247v1",
"C10248v1",
"C10250v1",
"C10251v1",
"C10252v2",
"C10253v2",
"C10254v2",
"C10255v1",
"C10256v2",
"C10257v2",
"C10258v3",
"C10259v3",
"C10260v3",
"C10261v3",
"C10262v2",
"C10263v3",
"C10264v2",
"C10265v4",
"C10266v4",
"C10269v2",
"C10270v2",
"C10271v4",
"C10272v3",
"C10273v2",
"C10274v2",
"C10275v1",
"C10276v1",
"C10277v1",
"C10300v2",
"C10301v2",
"C10302v2",
"C10303v2",
"C10304v2",
"C10305v2",
"C10306v1",
"C10307v1",
"C10308v1",
"C10309v1",
"C10310v1",
"C10311v1",
"C10312v1",
"C10313v1",
"C10314v1",
"C10315v1",
"C10316v1",
"C10317v1",
"C10318v1",
"C10319v1",
"C10320v1",
"C10321v2",
"C10322v3",
"C10323v2",
"C10324v2",
"C10325v3",
"C10326v2",
"C10327v2",
"C10328v2",
"C10330v2",
"C10332v1",
"C10333v1",
"C10334v1",
"C10335v1",
"C10336v1",
"C10337v1",
"C10338v2",
"C10339v1",
"C10341v1",
"C10342v2",
"C10343v1",
"C10345v1",
"C10346v1",
"C10347v2",
"C10348v1",
"C10349v3",
"C10350v3",
"C10351v2",
"C10352v3",
"C10353v2",
"C10354v2",
"C10355v3",
"C10356v2",
"C10359v2",
"C10360v1",
"C10361v1",
"C10362v1",
"C10363v1",
"C10364v1",
"C10365v1",
"C10366v1",
"C10367v1",
"C10368v1",
"C10369v1",
"C10370v1",
"C10371v1",
"C10372v1",
"C10373v2",
"C10374v2",
"C10375v2",
"C10376v2",
"C10377v2",
"C10378v1",
"C10379v1",
"C10380v1",
"C10381v1",
"C10382v1",
"C10383v1",
"C10384v1",
"C10385v1",
"C10386v1",
"C10387v1",
"C10388v1",
"C10389v2",
"C10390v1",
"C10391v1",
"C10392v1",
"C20049v1",
"C20056v1",
"C20059v1",
"C20060v1 ", ]
            fee = ["18130",
"18130",
"20340",
"18825",
"18825",
"18825",
"18825",
"18825",
"18825",
"18825",
"18825",
"16800",
"18445",
"15525",
"18825",
"18130",
"18130",
"18130",
"15525",
"18130",
"18130",
"18130",
"15750",
"18130",
"21180",
"21180",
"19960",
"19960",
"19960",
"19960",
"19960",
"19960",
"19960",
"19960",
"19960",
"18825",
"18825",
"18445",
"17390",
"15900",
"21180",
"21180",
"21180",
"21180",
"21180",
"21180",
"21180",
"21180",
"21180",
"21180",
"21180",
"21180",
"21180",
"21180",
"17735",
"18130",
"20340",
"21180",
"21180",
"18445",
"15750",
"15525",
"18130",
"15525",
"18130",
"17390",
"16800",
"16800",
"15525",
"15525",
"17090",
"18130",
"15750",
"18130",
"21180",
"16800",
"16800",
"19960",
"19960",
"21180",
"19960",
"19960",
"16800",
"16800",
"19960",
"16800",
"16800",
"14195",
"18825",
"18130",
"18130",
"21180",
"21180",
"21180",
"21180",
"21180",
"17735",
"21180",
"17735",
"20340",
"20340",
"17735",
"17735",
"17735",
"18825",
"18825",
"17735",
"18825",
"18825",
"18825",
"18825",
"18825",
"17735",
"15900",
"15900",
"15900",
"15750",
"15750",
"20340",
"18825",
"17735",
"18130",
"18825",
"18825",
"20340",
"20340",
"18825",
"18825",
"18825",
"21180",
"17390",
"17390",
"15135",
"15135",
"15135",
"17390",
"17390",
"15135",
"14195",
"15135",
"15135",
"20340",
"20340",
"20340",
"20340",
"17735",
"20340",
"16085",
"18130",
"18130",
"18445",
"18445",
"18130",
"18130",
"18130",
"18130",
"18825",
"19190",
"19190",
"15525",
"15525",
"15525",
"15525",
"18130",
"18130",
"18130",
"18130",
"18130",
"18130",
"15750",
"15135",
"15135",
"20340",
"15135",
"15135",
"20340",
"15135",
"15135",
"20340",
"15750",
"18130",
"18130",
"18130",
"18130",
"18445",
"18130",
"20340",
"15525",
"18825",
"17390",
"17390",
"17390",
"17390",
"17390",
"17390",
"21180",
"16800",
"18445",
"17390",
"17390",
"20340",
"18825",
"19190",
"18130",
"15900",
"15900",
"18130",
"19190",
"18825",
"18825",
"17390",
"18130",
"16800",
"15525",
"19190",
"19190",
"16800",
"16800",
"19190",
"19190",
"16800",
"16800",
"16800",
"16800",
"16800",
"16800",
"19190",
"16800",
"16800",
"19190",
"16800",
"21180",
"21180",
"21180",
"21180",
"21180",
"21180",
"17735",
"17735",
"21180",
"18825",
"18825",
"18825",
"16085",
"21180",
"15900",
"20755",
"20755",
"14855",
"17090", ]
            for i in range(len(cod)):
                feeDict[cod[i]] = fee[i]
            # //div[@class='sidebar__info sidebar--info-codes']//dl/dd[1]
            feeIndex = response.xpath("//div[@class='sidebar__info sidebar--info-codes']//dl/dd[1]//text()").extract()
            clear_space(feeIndex)
            print("---", feeIndex)
            v_re = re.findall(r"version\s\d", ''.join(feeIndex))
            print(v_re, "***")
            if feeIndex:
                feeIndexe = feeIndex[1] + ''.join(v_re).replace("version ", "v").strip()
                print('===', feeIndexe)
                item['tuition_fee'] = feeDict.get(feeIndexe)
            # feeIndex = ''.join(feeIndex)
            # print(feeIndex)
            # item['tuition_fee'] = feeDict.get(feeIndex)
            print("item['tuition_fee']: ", item['tuition_fee'])

            # //h4[@class='collapsible__title'][contains(text(),'Admission requirements')]/following-sibling::div[1]
            entry_requirements = response.xpath("//h4[@class='collapsible__title'][contains(text(),'Admission requirements')]/following-sibling::div[1]").extract()
            entry_requirements_str = ''.join(entry_requirements).strip()
            item['rntry_requirements_en'] = remove_class(clear_lianxu_space(entry_requirements))
            print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

            ieltsRe = re.findall(r"IELTS[0-9a-zA-Z:\.,\s]*;", entry_requirements_str)
            # print("ieltsRe: ", ieltsRe)
            toeflRe = re.findall(r"internet\sbased[0-9a-zA-Z:\.,\s-]*;", entry_requirements_str)
            # print("toeflRe: ", toeflRe)
            item['ielts_desc'] = ''.join(ieltsRe).strip()
            print("item['ielts_desc']: ", item['ielts_desc'])

            item['toefl_desc'] = ''.join(toeflRe).strip()
            print("item['toefl_desc']: ", item['toefl_desc'])

            # ieltsDict = {"Bachelor of Arts ": "7.5 overall,speaking 8.0,listening 8.0,reading 7.0,writing 7.0",
            #              "Bachelor of Education": "7.5 overall,speaking 8.0,listening 8.0,reading 7.0,writing 7.0",
            #              "Bachelor of Arts ": "7.5 overall,speaking 8.0,listening 8.0,reading 7.0,writing 7.0",
            #              "Bachelor of Education (Honours)": "7.5 overall,speaking 8.0,listening 8.0,reading 7.0,writing 7.0",
            #              "Bachelor of Education ": "7.5 overall,speaking 8.0,listening 8.0,reading 7.0,writing 7.0",
            #              "Bachelor of Arts in International Studies": "7.5 overall,speaking 8.0,listening 8.0,reading 7.0,writing 7.0",
            #              "Bachelor of Design (Honours) in Animation": "7.0 overall,writing 7.0",
            #              "Bachelor of Communication (Honours)": "7.0 overall,writing 7.0",
            #              "Bachelor of Education (Honours) in Primary Education": "7.0 overall,writing 7.0",
            #              "Bachelor of Nursing": "6.5 overall, writing 6.0",
            #              "Bachelor of Nursing ": "6.5 overall, writing 6.0",
            #              "Bachelor of Arts in International Studies": "6.5 overall, writing 6.0", }
            # if item['ielts_desc'] == "":
            #     item['ielts_desc'] = ieltsDict.get(item['degree_name'])
            #     if item['ielts_desc'] is None:
            #         item['ielts_desc'] = "6.5 overall, writing 6.0"
            # # print("item['ielts_desc']: ", item['ielts_desc'])
            #
            # toeflDict = {
            #     "Bachelor of Arts ": "102-109 overall, speaking 23-27, listening 23-27, reading 23-27, writing 24",
            #     "Bachelor of Education": "102-109 overall, speaking 23-27, listening 23-27, reading 23-27, writing 24 ",
            #     "Bachelor of Arts ": "102-109 overall, speaking 23-27, listening 23-27, reading 23-27, writing 24 ",
            #     "Bachelor of Education (Honours)": "102-109 overall, speaking 23-27, listening 23-27, reading 23-27, writing 24 ",
            #     "Bachelor of Education ": "102-109 overall, speaking 23-27, listening 23-27, reading 23-27, writing 24 ",
            #     "Bachelor of Arts in International Studies": "102-109 overall, speaking 23-27, listening 23-27, reading 23-27, writing 24 ",
            #     "Bachelor of Design (Honours) in Animation": "94-101 overall, writing 23  ",
            #     "Bachelor of Communication (Honours)": "94-101 overall, writing 23  ",
            #     "Bachelor of Education (Honours) in Primary Education": "94-101 overall, writing 23 ",
            #     "Bachelor of Nursing": "79-93 overall,writing 21 ",
            #     "Bachelor of Nursing ": "79-93 overall,writing 21 ",
            #     "Bachelor of Arts in International Studies": "79-93 overall,writing 21 ", }
            # if item['toefl_desc'] == "":
            #     item['toefl_desc'] = toeflDict.get(item['degree_name'])
            #     if item['toefl_desc'] is None:
            #         item['toefl_desc'] = "79-93 overall, writing 21"
            # # print("item['toefl_desc']: ", item['toefl_desc'])

            ielts_d = get_ielts(item['ielts_desc'])
            item["ielts"] = ielts_d.get('IELTS')
            item["ielts_l"] = ielts_d.get('IELTS_L')
            item["ielts_s"] = ielts_d.get('IELTS_S')
            item["ielts_r"] = ielts_d.get('IELTS_R')
            item["ielts_w"] = ielts_d.get('IELTS_W')
            print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                    item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            department = response.xpath(
                "//div[@class='field field-dddd-view-modeluts-course-course__part-of field-type-ds field-label-hidden']//div[@class='field-item']//p/a/text()").extract()
            clear_space(department)
            department = ''.join(department).replace("UTS:", "").strip()
            item['department'] = department
            print("item['department']: ", item['department'])


            apply_procces = response.xpath("//h4[contains(text(),'International students')]/..").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(apply_procces))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            yield item
        except Exception as e:
            with open("scrapySchool_Australian_yan/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

