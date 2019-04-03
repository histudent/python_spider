# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_Australian_yan.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_yan.getItem import get_item
from scrapySchool_Australian_yan.getTuition_fee import getTuition_fee
from scrapySchool_Australian_yan.items import ScrapyschoolAustralianYanItem
from scrapySchool_Australian_yan.remove_tags import remove_class
from scrapySchool_Australian_yan.getStartDate import getStartDate
from scrapySchool_Australian_yan.getDuration import getIntDuration
from scrapySchool_Australian_yan.getIELTS import get_ielts


class UniversityofTechnologySydney_PSpider(scrapy.Spider):
    name = "UniversityofTechnologySydney_P"
    start_urls = ["https://www.uts.edu.au/future-students/find-a-course/search?search=#panel-postgraduate"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        links = response.xpath(
            '//div[@id="panel-postgraduate"]//th[@id="view-name-ft-table-column--7"][contains(text(), "Master")]/../../following-sibling::*//tr//td[1]/a/@href').extract()
        # print(len(links))
        # links = list(set(links))
        # print(len(links))

        # 组合字典
        programme_dict = {}
        programme_list = response.xpath(
            '//div[@id="panel-postgraduate"]//th[@id="view-name-ft-table-column--7"][contains(text(), "Master")]/../../following-sibling::*//tr//td[1]/a//text()').extract()
        clear_space(programme_list)

        for link in range(len(links)):
            url = "https://www.uts.edu.au" + links[link]
            programme_dict[url] = programme_list[link]

        clear_space(links)
        print(len(links))
        links = list(set(links))
        print(len(links))


        for link1 in links:
            url = "https://www.uts.edu.au" + link1
            yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianYanItem)
        item['university'] = "University of Technology Sydney"
        # item['country'] = 'Australia'
        # item['website'] = 'https://www.uts.edu.au'
        item['url'] = response.url
        item['degree_type'] = 2
        item['teach_time'] = 'coursework'
        print("===========================")
        print(response.url)
        item['major_type1'] = response.meta.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            programme = response.xpath('//div[@class="field-item"]/div[contains(@class,"page-title")]/h1//text()').extract()
            clear_space(programme)
            programme = ''.join(programme).strip()
            item['degree_name'] = programme
            print("item['degree_name']: ", item['degree_name'])

            de_p = re.findall(r"\(.+\)", item['degree_name'])
            de_p = ''.join(de_p).strip()
            item['programme_en'] = item['degree_name'].replace(de_p, "").replace("Master of", "").strip()
            print("item['programme_en']: ", item['programme_en'])

            start_date = response.xpath(
                "//dt[contains(text(),'UAC')]/following-sibling::dd/span//text()").extract()
            clear_space(start_date)
            print(start_date)
            if len(start_date) > 0:
                start_date_re = re.findall(r"\w+\ssession", ' '.join(start_date))
                start_date_re = list(set(start_date_re))
                print("start_date_re: ", start_date_re)

                item['start_date'] = ','.join(start_date_re).replace("(", "").replace(")", "").replace(" session", "").strip()
            print("item['start_date']: ", item['start_date'])

            overview = response.xpath('//div[@class="field field-dddd-view-modeluts-course-course__overview field-type-ds field-label-hidden"]').extract()
            item['degree_overview_en'] = remove_class(clear_lianxu_space(overview))
            item['overview_en'] = item['degree_overview_en']
            print("item['degree_overview_en']: ", item['degree_overview_en'])

            career = response.xpath('//div[@class="field field-dddd-view-modeluts-course-course__careers field-type-ds field-label-hidden"]').extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            print("item['career_en']: ", item['career_en'])

            modules = response.xpath("//div[@class='course__structure']").extract()
            if len(modules) == 0:
                print(" 8888")
            #     modules = response.xpath("//div[@class='course__structure']").extract()
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

            # http://cis.uts.edu.au/fees/course-fees.cfm
            # feeDict = {'C04006v6': '15000', 'C04007v7': '15000', 'C04008v6': '15000', 'C04018v6': '19015', 'C04037v6': '17570', 'C04038v8': '18650', 'C04048v7': '18650', 'C04052v4': '19770', 'C04055v4': '15585', 'C04067v7': '18650', 'C04090v5': '17930', 'C04094v5': '17570', 'C04097v2': '17930', 'C04098v3': '17570', 'C04106v5': '16005', 'C04108v3': '14790', 'C04109v7': '14790', 'C04140v11': '16005', 'C04143v8': '20575', 'C04145v4': '20575', 'C04147v5': '22280', 'C04149v4': '21415', 'C04157v8': '19770', 'C04158v4': '19015', 'C04160v7': '20985', 'C04203v4': '14790', 'C04210v1': '16895', 'C04218v5': '19770', 'C04222v1': '19770', 'C04224v4': '20985', 'C04226v4': '17570', 'C04227v3': '17570', 'C04228v2': '16005', 'C04229v3': '17570', 'C04231v2': '15145', 'C04232v3': '15145', 'C04234v1': '19770', 'C04235v2': '17570', 'C04236v3': '22280', 'C04237v3': '18650', 'C04238v3': '18650', 'C04239v2': '14150', 'C04241v2': '18280', 'C04242v1': '20575', 'C04243v3': '17270', 'C04244v1': '13520', 'C04245v1': '14790', 'C04246v2': '16005', 'C04248v1': '16280', 'C04250v2': '22280', 'C04251v1': '20575', 'C04252v2': '19015', 'C04253v2': '19015', 'C04254v1': '14790', 'C04255v1': '12300', 'C04257v1': '11145', 'C04258v3': '18650', 'C04259v2': '18650', 'C04260v2': '18650', 'C04261v2': '18650', 'C04262v1': '14790', 'C04264v1': '22280', 'C04265v2': '18280', 'C04266v1': '17270', 'C04267v1': '18280', 'C04268v1': '13340', 'C04269v2': '13340', 'C04270v1': '17570', 'C04271v2': '17930', 'C04272v2': '17570', 'C04273v2': '17930', 'C04274v1': '17570', 'C04275v1': '17570', 'C04277v2': '17930', 'C04278v2': '17570', 'C04279v2': '16005', 'C04281v2': '18650', 'C04284v2': '14150', 'C04285v1': '15000', 'C04286v1': '18650', 'C04287v1': '18650', 'C04288v1': '15000', 'C04289v1': '18650', 'C04290v1': '15000', 'C04291v1': '14150', 'C04292v1': '16005', 'C04293v2': '17930', 'C04294v1': '15585', 'C04295v2': '19770', 'C04296v2': '19015', 'C04297v2': '19770', 'C04298v1': '14790', 'C04299v1': '18280', 'C04300v1': '18650', 'C04301v1': '15000', 'C04302v1': '16005', 'C04303v1': '16005', 'C04304v3': '19015', 'C04305v1': '14415', 'C04306v1': '25070', 'C04307v1': '14415', 'C04309v2': '17930', 'C04314v1': '18650', 'C04315v1': '15585', 'C04316v2': '15000', 'C04317v1': '15000', 'C04319v1': '15000', 'C04320v1': '22280', 'C04321v1': '16565', 'C04322v1': '16005', 'C04323v1': '15585', 'C04324v2': '18650', 'C04325v2': '18650', 'C04368v1': '16895', 'C04369v1': '16895', 'C04371v1': '16895', 'C04372v1': '17930', 'C04373v1': '18650', 'C06006v5': '15000', 'C06009v8': '19015', 'C06017v7': '15000', 'C06033v4': '11145', 'C06037v4': '16005', 'C06041v6': '14790', 'C06058v7': '19770', 'C06096v3': '14415', 'C06097v1': '16895', 'C06099v1': '20575', 'C06100v2': '19015', 'C06101v1': '14790', 'C06102v1': '14790', 'C06103v1': '14790', 'C06104v1': '16565', 'C06105v1': '14790', 'C06106v1': '14790', 'C06107v1': '13340', 'C06108v1': '17930', 'C06109v1': '17570', 'C06110v1': '17570', 'C06113v1': '19770', 'C06114v2': '17930', 'C06115v2': '15000', 'C06116v1': '14415', 'C06118v2': '25070', 'C06119v1': '15585', 'C06121v1': '15585', 'C06122v1': '19015', 'C06123v1': '19770', 'C06124v1': '17930', 'C07002v7': '15000', 'C07004v4': '15000', 'C07012v7': '18650', 'C07018v5': '18650', 'C07019v6': '15000', 'C07021v8': '18650', 'C07027v8': '14150', 'C07028v9': '14150', 'C07029v7': '15000', 'C07044v4': '16005', 'C07048v7': '16005', 'C07073v5': '22280', 'C07074v5': '22280', 'C07075v4': '18280', 'C07078v3': '19015', 'C07080v7': '20985', 'C07107v3': '13520', 'C07112v4': '18650', 'C07113v3': '18650', 'C07118v1': '14790', 'C07119v1': '17270', 'C07120v2': '16895', 'C07122v1': '22280', 'C07124v1': '16005', 'C07125v1': '14790', 'C07126v1': '16005', 'C07128v1': '18650', 'C07129v1': '18650', 'C07132v1': '18650', 'C11001v5': '15000', 'C11005v5': '15000', 'C11008v7': '19015', 'C11015v8': '18650', 'C11017v5': '17570', 'C11021v5': '18650', 'C11027v5': '18650', 'C11039v4': '18650', 'C11048v3': '17930', 'C11051v3': '17570', 'C11054v2': '17570', 'C11125v4': '20575', 'C11128v3': '16005', 'C11130v4': '20575', 'C11142v7': '19770', 'C11145v7': '20985', 'C11198v3': '18650', 'C11199v4': '18650', 'C11206v3': '18650', 'C11210v2': '17270', 'C11211v2': '22280', 'C11215v4': '11145', 'C11216v1': '18280', 'C11217v1': '20575', 'C11223v1': '14790', 'C11225v1': '17270', 'C11227v1': '16895', 'C11229v1': '20575', 'C11230v2': '19015', 'C11232v1': '18280', 'C11234v1': '17270', 'C11235v1': '13340', 'C11236v1': '17930', 'C11237v1': '17570', 'C11238v1': '17930', 'C11239v1': '17570', 'C11242v1': '16005', 'C11245v1': '15000', 'C11247v1': '19770', 'C11248v1': '17930', 'C11249v2': '15000', 'C11254v1': '14415', 'C11257v1': '15000', 'C11260v2': '25070', 'C11262v1': '16005', 'C11264v1': '22280', 'C11265v1': '20575', 'C11270v1': '15000', 'C11271v1': '15000', 'C11274v1': '17930', 'C01001v2': '12810', 'C01002v2': '12810', 'C01003v2': '12810', 'C01004v2': '12810', 'C01005v2': '12810', 'C02001v2': '13850', 'C02018v5': '17570', 'C02019v3': '12810', 'C02020v2': '12810', 'C02024v4': '16005', 'C02025v5': '13520', 'C02026v4': '13520', 'C02028v6': '15000', 'C02029v4': '16280', 'C02030v3': '18280', 'C02031v3': '18280', 'C02037v4': '12810', 'C02039v3': '13340', 'C02041v4': '12810', 'C02047v1': '16280', 'C02048v4': '16005', 'C02050v1': '12810', 'C02056v1': '15000', 'C02057v1': '16005', 'C02058v2': '16005', 'C02059v1': '15000', 'C02060v1': '15000', 'C02061v1': '16005', 'C02062v1': '16005', 'C02063v1': '15000', 'C03001v4': '13850', 'C03002v5': '13850', 'C03012v4': '13850', 'C03017v5': '17570', 'C03018v3': '12810', 'C03024v7': '15000', 'C03025v4': '16280', 'C03026v6': '18280', 'C03029v4': '18280', 'C03032v4': '12810', 'C03034v3': '13340', 'C03044v2': '12810', 'C03046v3': '16005', 'C03047v2': '12810', 'C03048v3': '16005', 'C03049v3': '16005', 'C03050v3': '16005', 'C03051v1': '16280', 'C03053v1': '15000', 'C03054v1': '15000', 'C03055v1': '16005', 'C03056v1': '15000', 'C03057v1': '15000', 'C03058v1': '16005', 'C03059v1': '15000'}
            feeDict = {}
            cod = ["C04006v7",
"C04007v7",
"C04008v6",
"C04018v6",
"C04037v6",
"C04038v8",
"C04048v7",
"C04052v4",
"C04055v4",
"C04067v7",
"C04090v5",
"C04094v5",
"C04097v2",
"C04106v5",
"C04109v7",
"C04140v11",
"C04143v8",
"C04145v4",
"C04147v5",
"C04157v8",
"C04158v4",
"C04160v7",
"C04203v4",
"C04210v1",
"C04218v5",
"C04222v1",
"C04224v4",
"C04226v4",
"C04227v3",
"C04228v2",
"C04229v3",
"C04231v2",
"C04232v3",
"C04234v1",
"C04235v2",
"C04236v3",
"C04237v3",
"C04238v3",
"C04239v2",
"C04241v2",
"C04242v1",
"C04243v3",
"C04244v1",
"C04245v1",
"C04246v2",
"C04248v1",
"C04250v2",
"C04251v1",
"C04252v2 A ",
"C04253v2 B ",
"C04254v1",
"C04255v2",
"C04257v1",
"C04258v3",
"C04259v2",
"C04260v2",
"C04261v2",
"C04262v1",
"C04264v1",
"C04265v2",
"C04266v1",
"C04267v1",
"C04268v2",
"C04269v3",
"C04270v1",
"C04271v3",
"C04272v2",
"C04273v3",
"C04274v1",
"C04275v1",
"C04277v3",
"C04278v3",
"C04279v2",
"C04281v2",
"C04284v2",
"C04285v1",
"C04286v1",
"C04287v1",
"C04288v1",
"C04289v1",
"C04290v1",
"C04291v1",
"C04292v1",
"C04293v2",
"C04294v1",
"C04295v2",
"C04296v2",
"C04297v2",
"C04298v1",
"C04299v1",
"C04300v1",
"C04301v1",
"C04302v1",
"C04303v1",
"C04304v4",
"C04305v1",
"C04306v1",
"C04307v1",
"C04309v3",
"C04314v1",
"C04315v1",
"C04316v2",
"C04317v1",
"C04319v1",
"C04320v1",
"C04321v1",
"C04322v1",
"C04323v1",
"C04324v2",
"C04325v2",
"C04367v1",
"C04368v1",
"C04369v1",
"C04371v1",
"C04372v1",
"C04373v1",
"C04374v1",
"C04382v1",
"C04383v1",
"C04384v1",
"C04385v1",
"C04386v1",
"C04388v1",
"C04389v1",
"C04390v1",
"C04391v1",
"C04392v1",
"C04393v1",
"C04394v1",
"C04395v1",
"C04396v1",
"C04397v1",
"C06006v5",
"C06009v8",
"C06017v7",
"C06033v4",
"C06037v4",
"C06041v6",
"C06096v3",
"C06097v1",
"C06099v1",
"C06100v2",
"C06101v1",
"C06102v1",
"C06103v1",
"C06104v1",
"C06105v1",
"C06106v1",
"C06107v1",
"C06108v1",
"C06109v1",
"C06110v1",
"C06113v1",
"C06114v2",
"C06115v2",
"C06116v1",
"C06118v2",
"C06119v2",
"C06121v1",
"C06122v1",
"C06123v1",
"C06124v1",
"C06125v1",
"C06126v1",
"C06127v1",
"C06129v1",
"C06130v1",
"C07002v7",
"C07004v5",
"C07012v7",
"C07018v5",
"C07019v6",
"C07021v8",
"C07028v9",
"C07029v7",
"C07044v4",
"C07048v7",
"C07073v5",
"C07074v5",
"C07078v3",
"C07080v7",
"C07107v3",
"C07112v4",
"C07113v3",
"C07118v1",
"C07119v1",
"C07120v2",
"C07122v1",
"C07124v1",
"C07125v1",
"C07126v1",
"C07128v1",
"C07129v1",
"C07132v1",
"C07135v1",
"C07136v1",
"C07137v1",
"C07140v1",
"C07141v1",
"C11001v5",
"C11005v6",
"C11008v7",
"C11015v8",
"C11017v5",
"C11021v5",
"C11027v5",
"C11039v4",
"C11048v3",
"C11125v4",
"C11128v3",
"C11130v4",
"C11142v7",
"C11145v7",
"C11198v3",
"C11199v4",
"C11206v3",
"C11210v2",
"C11211v2",
"C11215v4",
"C11216v1",
"C11217v1",
"C11223v1",
"C11225v1",
"C11227v1",
"C11229v1",
"C11230v2",
"C11232v1 C ",
"C11234v1",
"C11235v1",
"C11236v1",
"C11237v1",
"C11238v1",
"C11239v1",
"C11242v1",
"C11245v1",
"C11247v1",
"C11249v3",
"C11254v1",
"C11257v1",
"C11260v2",
"C11262v1",
"C11264v1",
"C11265v1",
"C11269v1",
"C11270v1",
"C11271v1",
"C11274v1",
"C11275v1",
"C11276v1",
"C11277v1",
"C11282v1",
"C11283v1",
"C11285v1",
"C11287v1",
"C11289v1",
"C11292v1 ", ]
            fee = ["15750",
"15750",
"15750",
"19960",
"18445",
"19580",
"19580",
"20755",
"16360",
"19580",
"18825",
"18445",
"18825",
"16800",
"15525",
"16800",
"21600",
"21600",
"23390",
"20755",
"19960",
"22030",
"15525",
"17735",
"20755",
"20755",
"22030",
"18445",
"18445",
"16800",
"18445",
"15900",
"15900",
"20755",
"18445",
"23390",
"19580",
"19580",
"14855",
"19190",
"21600",
"18130",
"14195",
"15525",
"16800",
"17090",
"23390",
"21600",
"19960",
"19960",
"15525",
"12915",
"11700",
"19580",
"19580",
"19580",
"19580",
"15525",
"23390",
"19190",
"18130",
"19190",
"14005",
"14005",
"18445",
"18825",
"18445",
"18825",
"18445",
"18445",
"18825",
"18445",
"16800",
"19580",
"14855",
"15750",
"19580",
"19580",
"15750",
"19580",
"15750",
"14855",
"16800",
"18825",
"16360",
"20755",
"19960",
"20755",
"15525",
"19190",
"19580",
"15750",
"16800",
"16800",
"19960",
"15135",
"26320",
"15135",
"18825",
"19580",
"16360",
"15750",
"15750",
"15750",
"23390",
"16800",
"16800",
"16360",
"19580",
"19580",
"19960",
"15750",
"15750",
"15750",
"18825",
"19580",
"23850",
"19580",
"19580",
"15525",
"15525",
"25300",
"19190",
"19190",
"19190",
"19190",
"19190",
"19190",
"17735",
"19960",
"16800",
"16800",
"15750",
"19960",
"15750",
"11700",
"16800",
"15525",
"15135",
"17735",
"21600",
"19960",
"15525",
"15525",
"15525",
"16800",
"15525",
"15525",
"14005",
"18825",
"18445",
"18445",
"20755",
"18825",
"15750",
"15135",
"26320",
"15900",
"16360",
"19960",
"20755",
"18825",
"18445",
"15750",
"23850",
"15525",
"25300",
"15750",
"15750",
"19580",
"19580",
"15750",
"19580",
"14855",
"15750",
"16800",
"16800",
"23390",
"23390",
"19960",
"22030",
"14195",
"19580",
"19580",
"15525",
"18130",
"17735",
"23390",
"16800",
"15525",
"16800",
"19580",
"19580",
"19580",
"19580",
"19190",
"19190",
"17735",
"19190",
"15750",
"15750",
"19960",
"19580",
"18445",
"19580",
"19580",
"19580",
"18825",
"21600",
"16800",
"21600",
"20755",
"22030",
"19580",
"19580",
"19580",
"18130",
"23390",
"11700",
"19190",
"21600",
"15525",
"18130",
"17735",
"21600",
"19960",
"19190",
"18130",
"14005",
"18825",
"18445",
"18825",
"18445",
"16800",
"15750",
"20755",
"15750",
"15135",
"15750",
"26320",
"16800",
"23390",
"21600",
"19960",
"15750",
"15750",
"18825",
"18445",
"15750",
"23850",
"19580",
"25300",
"19190",
"19190",
"17735",
"19190", ]
            for i in range(len(cod)):
                feeDict[cod[i]] = fee[i]
            # //div[@class='sidebar__info sidebar--info-codes']//dl/dd[1]
            feeIndex = response.xpath("//div[@class='sidebar__info sidebar--info-codes']//dl/dd[1]//text()").extract()
            clear_space(feeIndex)
            print("---",feeIndex)
            v_re = re.findall(r"version\s\d", ''.join(feeIndex))
            print(v_re, "***")
            if feeIndex:
                feeIndexe = feeIndex[1]+''.join(v_re).replace("version ", "v").strip()
                print('===', feeIndexe)
                item['tuition_fee'] = feeDict.get(feeIndexe)
            print("item['tuition_fee']: ", item['tuition_fee'])

            # //h4[@class='collapsible__title'][contains(text(),'Admission requirements')]/following-sibling::div[1]
            entry_requirements = response.xpath("//h4[@class='collapsible__title'][contains(text(),'Admission requirements')]/following-sibling::div[1]").extract()
            entry_requirements_str = ''.join(entry_requirements).strip()
            item['rntry_requirements_en'] = remove_class(clear_lianxu_space(entry_requirements))
            # print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

            ieltsRe = re.findall(r"IELTS[0-9a-zA-Z:\.,\s]*;", entry_requirements_str)
            # print("ieltsRe: ", ieltsRe)
            toeflRe = re.findall(r"internet\sbased[0-9a-zA-Z:\.,\s-]*;", entry_requirements_str)
            # print("toeflRe: ", toeflRe)
            item['ielts_desc'] = ''.join(ieltsRe).strip()
            # print("item['ielts_desc']: ", item['ielts_desc'])

            item['toefl_desc'] = ''.join(toeflRe).strip()
            # print("item['toefl_desc']: ", item['toefl_desc'])

            ieltsDict = {
                "Master of Teaching in Secondary Education": "7.5 overall,speaking 8.0,listening 8.0,reading 7.0,writing 7.0",
                "Master of Advanced Journalism": "7.0 overall,with a writing score of 6.5",
                "Master of Pharmacy": "7.0 overall,7.0 in each subtest",
                "Master of Pharmacy (International)": "7.0 overall,7.0 in each subtest",
                "Master of Clinical Psychology": "7.0 overall,writing 7.0",
                "Master of Physiotherapy": "7.0 overall,writing 7.0", }
            if item['ielts_desc'] == "":
                item['ielts_desc'] = ieltsDict.get(item['degree_name'])
                if item['ielts_desc'] is None:
                    item['ielts_desc'] = "6.5 overall, writing 6.0"
            # print("item['ielts_desc']: ", item['ielts_desc'])



            toeflDict = {"Master of Teaching in Secondary Education": "102-109 overall,speaking 23-27,listening 23-27,reading 23-27,writing 24",
"Master of Advanced Journalism": "94-101 overall,with a writing score of 24 ",
"Master of Pharmacy": "94 overall,reading 24,listening 24,speaking 23,writing 27 ",
"Master of Pharmacy (International)": "94 overall,reading 24,listening 24,speaking 23,writing 27  ",
"Master of Clinical Psychology": "94-101 overall,writing 23 ",
"Master of Physiotherapy": "94-101 overall,writing 23 ",}
            if item['toefl_desc'] == "":
                item['toefl_desc'] = ieltsDict.get(item['degree_name'])
                if item['toefl_desc'] is None:
                    item['toefl_desc'] = "79-93 overall, writing 21"
            # print("item['toefl_desc']: ", item['toefl_desc'])

            ielts_d = get_ielts(item['ielts_desc'])
            item["ielts"] = ielts_d.get('IELTS')
            item["ielts_l"] = ielts_d.get('IELTS_L')
            item["ielts_s"] = ielts_d.get('IELTS_S')
            item["ielts_r"] = ielts_d.get('IELTS_R')
            item["ielts_w"] = ielts_d.get('IELTS_W')
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            department = response.xpath(
                "//div[@class='field field-dddd-view-modeluts-course-course__part-of field-type-ds field-label-hidden']//div[@class='field-item']//p/a/text()").extract()
            clear_space(department)
            department = ''.join(department).replace("UTS:", "").strip()
            item['department'] = department
            # print("item['department']: ", item['department'])


            apply_procces = response.xpath("//h4[contains(text(),'International students')]/..").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(apply_procces))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            yield item
        except Exception as e:
            with open("scrapySchool_Australian_yan/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

