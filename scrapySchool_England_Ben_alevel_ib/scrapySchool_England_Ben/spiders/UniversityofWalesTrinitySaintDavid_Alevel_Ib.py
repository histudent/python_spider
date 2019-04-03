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


class UniversityofWalesTrinitySaintDavid_Alevel_IbSpider(scrapy.Spider):
    name = "UniversityofWalesTrinitySaintDavid_Alevel_Ib"
    start_urls = ["https://www.bolton.ac.uk/subject-areas/all-subjects/"]

    def parse(self, response):
        links = ["https://www.uwtsd.ac.uk/bsc-computing-information-systems-foundation/",
"https://www.uwtsd.ac.uk/bsc-computing/",
"https://www.uwtsd.ac.uk/ba-chinese-studies/",
"https://www.uwtsd.ac.uk/bsc-software-engineering/",
"https://www.uwtsd.ac.uk/bsc-applied-computing-foundation/",
"https://www.uwtsd.ac.uk/bsc-computer-games-development/",
"https://www.uwtsd.ac.uk/bsc-web-development/",
"https://www.uwtsd.ac.uk/bsc-web-development-foundation/",
"https://www.uwtsd.ac.uk/ba-classical-civilisation/",
"https://www.uwtsd.ac.uk/beng-energy-environmental-engineering-4-year/",
"https://www.uwtsd.ac.uk/ba-creative-writing/",
"https://www.uwtsd.ac.uk/ba-english/",
"https://www.uwtsd.ac.uk/beng-extreme-sports-engineering/",
"https://www.uwtsd.ac.uk/bsc-environmental-conservation/",
"https://www.uwtsd.ac.uk/ba-conflict-and-war/",
"https://www.uwtsd.ac.uk/beng-energy-environmental-engineering/",
"https://www.uwtsd.ac.uk/beng-extreme-sports-engineering-4-year/",
"https://www.uwtsd.ac.uk/ba-history/",
"https://www.uwtsd.ac.uk/ba-heritage-studies/",
"https://www.uwtsd.ac.uk/ba-international-development-and-global-politics/",
"https://www.uwtsd.ac.uk/ba-humanities/",
"https://www.uwtsd.ac.uk/mtour-tourism-management/",
"https://www.uwtsd.ac.uk/marts-ancient-civilisations/",
"https://www.uwtsd.ac.uk/bsc-logistics-supply-chain-management/",
"https://www.uwtsd.ac.uk/marts-classical-languages/",
"https://www.uwtsd.ac.uk/marts-3d-computer-animation/",
"https://www.uwtsd.ac.uk/mart-fine-art/",
"https://www.uwtsd.ac.uk/undergraduate/international-development-and-global-politics/marts-international-development-humanitarianism-and-law/",
"https://www.uwtsd.ac.uk/marts-art-gallery-museum-studies/",
"https://www.uwtsd.ac.uk/marts-photography-in-the-arts/",
"https://www.uwtsd.ac.uk/marts-digital-film-television-production/",
"https://www.uwtsd.ac.uk/marts-creative-computer-games-design/",
"https://www.uwtsd.ac.uk/marts-photojournalism/",
"https://www.uwtsd.ac.uk/mdes-advertising-brand-design/",
"https://www.uwtsd.ac.uk/mdes-automotive-design/",
"https://www.uwtsd.ac.uk/mdes-graphic-design/",
"https://www.uwtsd.ac.uk/mdes-illustration/",
"https://www.uwtsd.ac.uk/mdes-surface-pattern-design-fashion-object/",
"https://www.uwtsd.ac.uk/mdes-product-design/",
"https://www.uwtsd.ac.uk/mdes-set-design/",
"https://www.uwtsd.ac.uk/mdes-surface-pattern-design-textile-for-interiors/",
"https://www.uwtsd.ac.uk/mdes-surface-pattern-design-textile-for-fashion/",
"https://www.uwtsd.ac.uk/mdes-surface-pattern-design-maker/",
"https://www.uwtsd.ac.uk/mdes-product-design-technology/",
"https://www.uwtsd.ac.uk/meach-early-childhood/",
"https://www.uwtsd.ac.uk/beng-mechanical-manufacturing-engineering-4-year/",
"https://www.uwtsd.ac.uk/beng-mechanical-engineering/",
"https://www.uwtsd.ac.uk/beng-mechanical-engineering-four-year-including-foundation-entry/",
"https://www.uwtsd.ac.uk/marts-music-technology/",
"https://www.uwtsd.ac.uk/mdes-transport-design/",
"https://www.uwtsd.ac.uk/ba-medieval-studies/",
"https://www.uwtsd.ac.uk/beng-motorcycle-engineering/",
"https://www.uwtsd.ac.uk/ba-modern-historical-studies/",
"https://www.uwtsd.ac.uk/beng-motorcycle-engineering-4yr/",
"https://www.uwtsd.ac.uk/undergraduate/philosophy-politics-and-economics/",
"https://www.uwtsd.ac.uk/beng-motorsport-engineering-4yrs/",
"https://www.uwtsd.ac.uk/beng-motorsport-engineering/",
"https://www.uwtsd.ac.uk/bsc-motorsport-management/",
"https://www.uwtsd.ac.uk/undergraduate/political-ecology/",
"https://www.uwtsd.ac.uk/ba-religious-studies/",
"https://www.uwtsd.ac.uk/ba-philosophy/",
"https://www.uwtsd.ac.uk/ba-ancient-history/",
"https://www.uwtsd.ac.uk/bsc-architecture/",
"https://www.uwtsd.ac.uk/beng-automotive-engineering/",
"https://www.uwtsd.ac.uk/ba-accounting/",
"https://www.uwtsd.ac.uk/ba-applied-drama/",
"https://www.uwtsd.ac.uk/ba-business-and-management/",
"https://www.uwtsd.ac.uk/beng-automotive-engineering-4-yr/",
"https://www.uwtsd.ac.uk/ba-archaeology/",
"https://www.uwtsd.ac.uk/ba-ancient-history-ancient-egyptian-culture/",
"https://www.uwtsd.ac.uk/ba-ancient-civilisations/",
"https://www.uwtsd.ac.uk/ba-cultural-industries-management/",
"https://www.uwtsd.ac.uk/ba-law-and-business/",
"https://www.uwtsd.ac.uk/ba-performing-arts-contemporary-performance/",
"https://www.uwtsd.ac.uk/ba-business-management/",
"https://www.uwtsd.ac.uk/ba-3d-computer-animation/",
"https://www.uwtsd.ac.uk/ba-design-crafts/",
"https://www.uwtsd.ac.uk/ba-architectural-glass-arts/",
"https://www.uwtsd.ac.uk/ba-international-business/",
"https://www.uwtsd.ac.uk/ba-acting/",
"https://www.uwtsd.ac.uk/ba-advocacy/",
"https://www.uwtsd.ac.uk/ba-ancient-history-archaeology/",
"https://www.uwtsd.ac.uk/ba-ancient-history-history/",
"https://www.uwtsd.ac.uk/ba-adventure-filmmaking/",
"https://www.uwtsd.ac.uk/ba-ancient-history-education-studies/",
"https://www.uwtsd.ac.uk/ba-advertising-brand-design/",
"https://www.uwtsd.ac.uk/ba-anthropology/",
"https://www.uwtsd.ac.uk/ba-ancient-history-latin/",
"https://www.uwtsd.ac.uk/ba-archaeology-anthropology/",
"https://www.uwtsd.ac.uk/ba-automotive-design/",
"https://www.uwtsd.ac.uk/ba-business-management-finance/",
"https://www.uwtsd.ac.uk/ba-business-management-human-resource-management/",
"https://www.uwtsd.ac.uk/ba-art-gallery-museum-studies/",
"https://www.uwtsd.ac.uk/ba-business-management-events-festivals/",
"https://www.uwtsd.ac.uk/ba-anthropology-psychology/",
"https://www.uwtsd.ac.uk/ba-business-management-marketing/",
"https://www.uwtsd.ac.uk/ba-chinese-civilisation-and-medieval-studies/",
"https://www.uwtsd.ac.uk/ba-chinese-studies-education-studies/",
"https://www.uwtsd.ac.uk/ba-classical-studies-heritage-studies/",
"https://www.uwtsd.ac.uk/ba-classical-studies-ancient-egyptian-culture/",
"https://www.uwtsd.ac.uk/ba-classical-studies-archaeology/",
"https://www.uwtsd.ac.uk/ba-classical-studies-with-education-studies/",
"https://www.uwtsd.ac.uk/ba-classical-studies-creative-writing/",
"https://www.uwtsd.ac.uk/undergraduate/classics/ba-classical-civilisation-with-greek/",
"https://www.uwtsd.ac.uk/ba-classical-studies-theology/",
"https://www.uwtsd.ac.uk/ba-english-classical-studies/",
"https://www.uwtsd.ac.uk/ba-creative-computer-games-design/",
"https://www.uwtsd.ac.uk/ba-rural-enterprise-management/",
"https://www.uwtsd.ac.uk/ba-dance/",
"https://www.uwtsd.ac.uk/ba-early-years-education-and-care/",
"https://www.uwtsd.ac.uk/ba-classical-studies-religious-studies/",
"https://www.uwtsd.ac.uk/bsc-music-technology/",
"https://www.uwtsd.ac.uk/ba-digital-marketing/",
"https://www.uwtsd.ac.uk/ba-early-years-education-and-care-early-years-practitioner/",
"https://www.uwtsd.ac.uk/ba-classical-studies-heritage-management/",
"https://www.uwtsd.ac.uk/ba-early-years-education-and-care-early-years-practitioner-2-years/",
"https://www.uwtsd.ac.uk/ba-education-studies/",
"https://www.uwtsd.ac.uk/ba-primary-education-studies/",
"https://www.uwtsd.ac.uk/ba-english-education-studies/",
"https://www.uwtsd.ac.uk/ba-english-tefl/",
"https://www.uwtsd.ac.uk/ba-education-studies-contemporary-learners-learning/",
"https://www.uwtsd.ac.uk/ba-education-studies-international-perspectives/",
"https://www.uwtsd.ac.uk/undergraduate/early-years/ba-early-years-education-and-care-early-years-practitioner-status---2-years/",
"https://www.uwtsd.ac.uk/ba-ethical-political-studies/",
"https://www.uwtsd.ac.uk/ba-english-classical-studies/",
"https://www.uwtsd.ac.uk/ba-event-management/",
"https://www.uwtsd.ac.uk/ba-film-tv/",
"https://www.uwtsd.ac.uk/ba-filmmaking/",
"https://www.uwtsd.ac.uk/ba-illustration/",
"https://www.uwtsd.ac.uk/ba-graphic-design/",
"https://www.uwtsd.ac.uk/ba-heritage-studies-digital-humanities/",
"https://www.uwtsd.ac.uk/ba-humanistic-counselling/",
"https://www.uwtsd.ac.uk/ba-international-sports-management/",
"https://www.uwtsd.ac.uk/ba-fine-art-site-context/",
"https://www.uwtsd.ac.uk/ba-international-hotel-management/",
"https://www.uwtsd.ac.uk/ba-history-education-studies/",
"https://www.uwtsd.ac.uk/ba-law-and-public-service/",
"https://www.uwtsd.ac.uk/ba-international-travel-and-tourism-management/",
"https://www.uwtsd.ac.uk/ba-education-studies-additional-learning-needs-inclusion/",
"https://www.uwtsd.ac.uk/ba-law-criminology/",
"https://www.uwtsd.ac.uk/ba-leisure-management/",
"https://www.uwtsd.ac.uk/ba-law-policing/",
"https://www.uwtsd.ac.uk/ba-medieval-studies-modern-historical-studies/",
"https://www.uwtsd.ac.uk/cbc/ba-perfformio/",
"https://www.uwtsd.ac.uk/ba-medieval-studies-latin/",
"https://www.uwtsd.ac.uk/ba-philosophy-classical-studies/",
"https://www.uwtsd.ac.uk/ba-outdoor-education/",
"https://www.uwtsd.ac.uk/ba-medieval-studies-classical-studies/",
"https://www.uwtsd.ac.uk/ba-photography-in-the-arts/",
"https://www.uwtsd.ac.uk/ba-philosophy-education-studies/",
"https://www.uwtsd.ac.uk/ba-photojournalism/",
"https://www.uwtsd.ac.uk/ba-product-design/",
"https://www.uwtsd.ac.uk/ba-philosophy-religion-applied-psychology/",
"https://www.uwtsd.ac.uk/ba-modern-historical-studies-heritage-management/",
"https://www.uwtsd.ac.uk/ba-physical-education/",
"https://www.uwtsd.ac.uk/ba-primary-education-qts/",
"https://www.uwtsd.ac.uk/ba-philosophy-psychology/",
"https://www.uwtsd.ac.uk/ba-public-services/",
"https://www.uwtsd.ac.uk/ba-religion-philosophy-ethics/",
"https://www.uwtsd.ac.uk/ba-religion-theology-ethics/",
"https://www.uwtsd.ac.uk/ba-religious-studies-theology/",
"https://www.uwtsd.ac.uk/ba-religion-ethics-applied-psychology/",
"https://www.uwtsd.ac.uk/ba-religious-studies-islamic-studies/",
"https://www.uwtsd.ac.uk/ba-set-design/",
"https://www.uwtsd.ac.uk/ba-religious-studies-psychology/",
"https://www.uwtsd.ac.uk/ba-religion-theology-philosophy/",
"https://www.uwtsd.ac.uk/ba-sinology/",
"https://www.uwtsd.ac.uk/ba-social-studies-additional-needs/",
"https://www.uwtsd.ac.uk/ba-religious-studies-education-studies/",
"https://www.uwtsd.ac.uk/ba-sport-health/",
"https://www.uwtsd.ac.uk/ba-sports-management/",
"https://www.uwtsd.ac.uk/ba-social-studies-health-social-care/",
"https://www.uwtsd.ac.uk/ba-surface-pattern-design-contemporary-applied-arts-practice/",
"https://www.uwtsd.ac.uk/ba-stadium-sports-facility-management/",
"https://www.uwtsd.ac.uk/ba-surface-pattern-design-textiles-for-interiors/",
"https://www.uwtsd.ac.uk/ba-surface-pattern-design-fashion-object/",
"https://www.uwtsd.ac.uk/ba-theatre-design-production/",
"https://www.uwtsd.ac.uk/ba-theology-education-studies/",
"https://www.uwtsd.ac.uk/ba-social-studies-communities-families-individuals/",
"https://www.uwtsd.ac.uk/ba-transport-design/",
"https://www.uwtsd.ac.uk/ba-watersports-management/",
"https://www.uwtsd.ac.uk/ba-vocal-studies/",
"https://www.uwtsd.ac.uk/ba-tourism-management/",
"https://www.uwtsd.ac.uk/ba-theology/",
"https://www.uwtsd.ac.uk/ba-theology-philosophy-ethics/",
"https://www.uwtsd.ac.uk/ba-surface-pattern-design-textiles-for-fashion/",
"https://www.uwtsd.ac.uk/bsc-psychology/",
"https://www.uwtsd.ac.uk/bsc-counselling-studies-psychology/",
"https://www.uwtsd.ac.uk/beng-electrical-electronic-engineering/",
"https://www.uwtsd.ac.uk/bsc-health-nutrition-lifestyle/",
"https://www.uwtsd.ac.uk/bsc-mental-health/",
"https://www.uwtsd.ac.uk/bsc-police-sciences/",
"https://www.uwtsd.ac.uk/ba-youth-community-work/",
"https://www.uwtsd.ac.uk/bsc-applied-psychology/",
"https://www.uwtsd.ac.uk/bsc-policing-criminology/",
"https://www.uwtsd.ac.uk/bsc-health-care-children-young-people/",
"https://www.uwtsd.ac.uk/bsc-health-social-care/",
"https://www.uwtsd.ac.uk/bsc-product-design-technology/",
"https://www.uwtsd.ac.uk/bsc-public-health/",
"https://www.uwtsd.ac.uk/bsc-health-management/",
"https://www.uwtsd.ac.uk/sport-and-exercise-science/",
"https://www.uwtsd.ac.uk/bsc-outdoor-fitness/",
"https://www.uwtsd.ac.uk/bsc-sports-exercise-science/",
"https://www.uwtsd.ac.uk/bsc-sport-therapy/",
"https://www.uwtsd.ac.uk/bsc-personal-training/",
"https://www.uwtsd.ac.uk/bsc-sports-exercise-science-sports-nutrition/",
"https://www.uwtsd.ac.uk/ba-classics/",
"https://www.uwtsd.ac.uk/ba-chinese-studies-history/",
"https://www.uwtsd.ac.uk/bsc-computer-networks/", ]
        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})


    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Wales Trinity Saint David"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:
            # ucas_point = response.xpath("//li[@class='iconim points']//b[contains(text(),'UCAS points:')]/../span//text()").extract()
            # print("ucas_point: ", ucas_point)

            alevel = response.xpath(
                "//div[@id='collapseEntryCriteria']//*[contains(text(),'UCAS points')]//text()|"
                "//div[@id='collapseEntryCriteria']//*[contains(text(),'A Level')]//text()|"
                "//div[@id='collapseEntryCriteria']//*[contains(text(),'A level')]//text()").extract()
            if len(alevel) == 0:
                alevel = response.xpath(
                    "//*[contains(text(),'UCAS Points')]//text()|"
                    "//*[contains(text(),'UCAS points')]//text()|"
                    "//ul[@type='disc']/preceding-sibling::*[1]//text()|//ul[@type='disc']//text()").extract()
            item['alevel'] = clear_lianxu_space(alevel)
            print("item['alevel']: ", item['alevel'])

            yield item

        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

