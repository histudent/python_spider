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
from w3lib.html import remove_tags


class UniversityofPlymouth_USpider(scrapy.Spider):
    name = "UniversityOfPlymouth_U"
    start_urls = ["https://www.bolton.ac.uk/subject-areas/all-subjects/"]

    def parse(self, response):
        links = ["https://www.plymouth.ac.uk/courses/undergraduate/ba-3d-design",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-theatre-and-performance",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-biological-sciences",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-tourism-and-hospitality-management",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-tourism-management",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-robotics",
"https://www.plymouth.ac.uk/courses/undergraduate/beng-robotics",
"https://www.plymouth.ac.uk/courses/undergraduate/meng-robotics",
"https://www.plymouth.ac.uk/courses/undergraduate/beng-robotic-engineering-with-foundation-year",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-publishing",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-psychology-with-sociology",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-psychology-with-human-biology",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-psychology-with-criminology-and-criminal-justice-studies",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-psychology",
"https://www.plymouth.ac.uk/courses/undergraduate/bed-primary-music",
"https://www.plymouth.ac.uk/courses/undergraduate/bed-primary-humanities",
"https://www.plymouth.ac.uk/courses/undergraduate/bed-primary-physical-education",
"https://www.plymouth.ac.uk/courses/undergraduate/bed-primary-special-educational-needs",
"https://www.plymouth.ac.uk/courses/undergraduate/bed-primary-science",
"https://www.plymouth.ac.uk/courses/undergraduate/bed-primary-mathematics",
"https://www.plymouth.ac.uk/courses/undergraduate/bed-primary-english",
"https://www.plymouth.ac.uk/courses/undergraduate/bed-primary-earlychildhood-studies",
"https://www.plymouth.ac.uk/courses/undergraduate/bed-primary-artand-design",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-pre-registration-midwifery",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-pre-registration-midwifery-old",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-police-and-criminal-justice-studies",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-politics-with-law",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-politics-with-international-relations",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-podiatry",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-physiotherapy",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-quantity-surveying",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-paramedic-practitioner",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-physical-geography-and-geology",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-sociology",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-photography",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-social-work",
"https://www.plymouth.ac.uk/courses/undergraduate/bmbs-bachelor-of-medicine-bachelor-of-surgery",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-anthropology",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-architecture",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-architectural-engineering",
"https://www.plymouth.ac.uk/courses/undergraduate/march-architecture",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-applied-geology",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-animal-behaviour-and-welfare",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-oceanography-and-coastal-processes",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-ocean-exploration-and-surveying",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-optometry",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-ocean-science-and-marine-conservation",
"https://www.plymouth.ac.uk/courses/undergraduate/msci-ocean-science",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-occupational-therapy",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-fine-art-and-art-history",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-fine-art",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-film-and-television-production",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-financial-economics",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-illustration",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-healthcare-science-life-sciences",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-music",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-medical-physiology",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-media-arts",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-cruise-management",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-criminology-and-criminal-justice-studies-with-sociology",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-criminology-and-criminal-justice-studies-with-psychology",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-criminology-and-criminal-justice-studies-with-international-relations",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-criminology-and-criminal-justice-studies",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-conservation-biology",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-construction-management-and-the-environment",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-criminology-and-criminal-justice-studies-with-law",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-computing-with-foundation-year",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-computing-games-development",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-computing",
"https://www.plymouth.ac.uk/courses/undergraduate/msci-computer-science",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-computer-science",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-computer-and-information-security",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-computer-systems-and-networks",
"https://www.plymouth.ac.uk/courses/undergraduate/beng-civil-engineering-with-foundation-year",
"https://www.plymouth.ac.uk/courses/undergraduate/meng-civil-engineering",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-chemistry-with-foundation-year",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-documentary-photography",
"https://www.plymouth.ac.uk/courses/undergraduate/beng-civil-and-coastal-engineering",
"https://www.plymouth.ac.uk/courses/undergraduate/beng-civil-engineering",
"https://www.plymouth.ac.uk/courses/undergraduate/meng-civil-and-coastal-engineering",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-chemistry",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-digital-media-design",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-dietetics",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-dental-therapy-hygiene",
"https://www.plymouth.ac.uk/courses/undergraduate/bds-dental-surgery",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-data-modelling-and-analytics",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-dance",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-digital-media-design",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-events-management",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-environmental-sciences-with-foundation-year",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-environmental-management-and-sustainability",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-english-with-spanish",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-environmental-science",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-english-with-publishing",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-english-with-french",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-english-with-foundation",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-english-with-history",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-english",
"https://www.plymouth.ac.uk/courses/undergraduate/beng-electronic-and-electrical-engineering-with-foundation-year",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-electrical-and-electronic-engineering",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-english-and-creative-writing",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-english-and-creative-writing-with-foundation",
"https://www.plymouth.ac.uk/courses/undergraduate/beng-electrical-and-electronic-engineering",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-education-studies",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-economics-with-politics",
"https://www.plymouth.ac.uk/courses/undergraduate/meng-electrical-and-electronic-engineering",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-economics",
"https://www.plymouth.ac.uk/courses/undergraduate/beng-mechanical-engineering-with-foundation-year",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-economics-with-international-relations",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-economics-with-law",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-earth-sciences-with-foundation-year",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-early-childhood-studies",
"https://www.plymouth.ac.uk/courses/undergraduate/meng-mechanical-engineering-with-composites",
"https://www.plymouth.ac.uk/courses/undergraduate/meng-mechanical-engineering",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-mathematics-with-high-performance-computing",
"https://www.plymouth.ac.uk/courses/undergraduate/beng-mechanical-engineering-with-composites",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-mathematics-with-foundation-year",
"https://www.plymouth.ac.uk/courses/undergraduate/beng-mechanical-engineering",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-mathematics-with-finance",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-mathematics-with-theoretical-physics",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-mathematics-with-education",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-marketing",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-maritime-business-and-maritime-law",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-mathematics",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-mathematics-and-statistics",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-maritime-business-and-logistics",
"https://www.plymouth.ac.uk/courses/undergraduate/meng-marine-technology",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-marine-sciences-with-foundation-year",
"https://www.plymouth.ac.uk/courses/undergraduate/beng-marine-technology",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-marine-biology-with-foundation-year",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-marine-biology-and-oceanography",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-marine-biology-and-coastal-ecology",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-marine-biology",
"https://www.plymouth.ac.uk/courses/undergraduate/foundation-year-management-government-and-law-foundation-year",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-nutrition-exercise-and-health",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-nursing-mental-health",
"https://www.plymouth.ac.uk/courses/undergraduate/llb-law-with-business",
"https://www.plymouth.ac.uk/courses/undergraduate/llb-law-with-criminology-and-criminal-justice-studies",
"https://www.plymouth.ac.uk/courses/undergraduate/llb-law",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-geology-with-ocean-science",
"https://www.plymouth.ac.uk/courses/undergraduate/mgeol-geology",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-geography-with-ocean-science",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-hospitality-management",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-human-biosciences",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-geology",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-history-with-politics",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-graphic-communication-with-typography",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-human-biology-with-foundation-year",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-history-with-foundation",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-history-with-english",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-history-with-international-relations",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-history",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-healthcare-science-physiological-sciences",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-nursing-child-health",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-navigation-and-maritime-science",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-geography-with-international-relations",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-nursing-adult",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-geography",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-internet-design",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-internet-design",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-geography",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-game-arts-and-design",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-international-tourism-management",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-international-relations-with-politics",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-international-relations",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-international-relations-with-law",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-international-hospitality-management",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-international-business-with-spanish",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-international-business-with-french",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-international-business-economics",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-international-business",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-acting",
"https://www.plymouth.ac.uk/courses/undergraduate/mchem-analytical-chemistry",
"https://www.plymouth.ac.uk/courses/undergraduate/mpsych-advanced-psychology",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-accounting-and-finance",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-art-history",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-business-management-2",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-business-management",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-business-economics",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-building-surveying-and-the-environment",
"https://www.plymouth.ac.uk/courses/undergraduate/ba-business",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-biomedical-science",
"https://www.plymouth.ac.uk/courses/undergraduate/bsc-biology-with-foundation-year", ]
        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})


    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Plymouth"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:
            entry = response.xpath("//div[@id='entry-requirements-accordion']//text()").extract()
            clear_space(entry)
            print("entry: ", entry)

            if "A level" in entry:
                alevel_index = entry.index("A level")
                item['alevel'] = entry[alevel_index+1]
            elif "A level/AS level" in entry:
                alevel_index = entry.index("A level/AS level")
                item['alevel'] = entry[alevel_index + 1]
            elif "A levels" in entry:
                alevel_index = entry.index("A levels")
                item['alevel'] = entry[alevel_index + 1]
            elif "A levels:" in entry:
                alevel_index = entry.index("A levels:")
                item['alevel'] = entry[alevel_index + 1].strip()
            elif "A Level:" in entry:
                alevel_index = entry.index("A Level:")
                item['alevel'] = entry[alevel_index + 1]
            elif "A level:" in entry:
                alevel_index = entry.index("A level:")
                item['alevel'] = entry[alevel_index + 1]
            else:
                item['alevel'] = None
                alevel_index = 0
            if item['alevel'] == ":" or item['alevel'] == '':
                item['alevel'] = entry[alevel_index + 2]



            if "International Baccalaureate" in entry:
                ib_index = entry.index("International Baccalaureate")
                item['ib'] = entry[ib_index + 1]
            elif "International baccalaureate" in entry:
                ib_index = entry.index("International baccalaureate")
                item['ib'] = entry[ib_index + 1]
            elif "International baccalaureates" in entry:
                ib_index = entry.index("International baccalaureates")
                item['ib'] = entry[ib_index + 1]
            elif "International baccalaureates:" in entry:
                ib_index = entry.index("International baccalaureates:")
                item['ib'] = entry[ib_index + 1]
            elif "International baccalaureate:" in entry:
                ib_index = entry.index("International baccalaureate:")
                item['ib'] = entry[ib_index + 1]
            elif "International Baccalaureate:" in entry:
                ib_index = entry.index("International Baccalaureate:")
                item['ib'] = entry[ib_index + 1]
            elif "IB" in entry:
                ib_index = entry.index("IB")
                item['ib'] = entry[ib_index + 1]
            elif "IB:" in entry:
                ib_index = entry.index("IB:")
                item['ib'] = entry[ib_index + 1]
            else:
                item['ib'] = None
                ib_index = 0
            if item['ib'] == ":" or item['ib'] == '':
                item['ib'] = entry[ib_index + 2]

            # alevel = response.xpath(
            #     "//b[contains(text(),'A Level:')]/..//text()|//b[contains(text(),'A level:')]/..//text()").extract()
            # item['alevel'] = clear_lianxu_space(alevel)
            print("item['alevel']: ", item['alevel'])

            # ib = response.xpath(
            #     "//b[contains(text(),'Baccalaureate:')]/..//text()").extract()
            # if len(ib) == 0:
            #     ib = response.xpath(
            #         "//b[contains(text(),'International Baccalaureate')]/..//text()").extract()
            # item['ib'] = clear_lianxu_space(ib)
            print("item['ib']: ", item['ib'])

            yield item

        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

