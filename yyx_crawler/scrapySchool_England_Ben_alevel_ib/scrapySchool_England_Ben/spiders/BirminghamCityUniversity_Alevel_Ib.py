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


class BirminghamCityUniversity_Alevel_IbSpider(scrapy.Spider):
    name = "BirminghamCityUniversity_Alevel_Ib"
    start_urls = ["https://www.bolton.ac.uk/subject-areas/all-subjects/"]

    def parse(self, response):
        links = ["http://www.bcu.ac.uk/courses/product-and-furniture-design-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/psychology-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/psychology-with-criminology-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/psychology-with-business-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/psychology-with-sociology-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/quantity-surveying-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/psychology-with-marketing-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/public-relations-and-media-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/human-resource-management-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/computing-information-technology-bsc-hons-msci-hons-2019-20",
"http://www.bcu.ac.uk/courses/accountancy-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/accounting-and-finance-macc-2019-20",
"http://www.bcu.ac.uk/courses/accounting-and-finance-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/architectural-technology-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/acting-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/architecture-riba-part-i-exemption-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/applied-theatre-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/automotive-engineering-beng-meng-2019-20",
"http://www.bcu.ac.uk/courses/biomedical-engineering-beng-meng-2019-20",
"http://www.bcu.ac.uk/courses/art-and-design-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/mechanical-engineering-beng-meng-2019-20",
"http://www.bcu.ac.uk/courses/biomedical-sciences-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/black-studies-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/building-surveying-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/business-studies-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/business-marketing-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/business-professional-practice-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/business-accounting-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/business-finance-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/business-economics-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/business-finance-mfin-2019-20",
"http://www.bcu.ac.uk/courses/business-management-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/business-management-consultancy-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/business-information-technology-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/business-management-enterprise-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/business-management-supply-chain-management-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/business-management-professional-practice-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/civil-engineering-beng-meng-2019-20",
"http://www.bcu.ac.uk/courses/computer-and-data-science-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/computer-networks-and-security-bsc-hons-msci-2019-20",
"http://www.bcu.ac.uk/courses/computer-games-technology-bsc-hons-msci-2019-20",
"http://www.bcu.ac.uk/courses/construction-management-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/computing-information-technology-bsc-hons-msci-hons-2019-20",
"http://www.bcu.ac.uk/courses/criminology-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/costume-design-and-practice-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/design-for-performance-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/criminology-policing-and-investigation-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/digital-marketing-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/digital-media-computing-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/economics-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/education-studies-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/early-childhood-studies-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/criminology-and-security-studies-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/english-and-creative-writing-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/english-and-drama-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/english-and-journalism-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/english-language-and-literature-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/english-literature-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/event-venue-and-experience-management-ba-2019-20",
"http://www.bcu.ac.uk/courses/electronic-engineering-beng-meng-2019-20",
"http://www.bcu.ac.uk/courses/fashion-branding-and-communication-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/fashion-and-beauty-journalism-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/fashion-design-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/fashion-business-promotion-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/film-business-and-promotion-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/film-production-technology-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/film-studies-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/film-and-screenwriting-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/filmmaking-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/finance-and-investment-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/finance-and-investment-mfin-2019-20",
"http://www.bcu.ac.uk/courses/english-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/financial-economics-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/garment-technology-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/fine-art-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/gemmology-and-jewellery-studies-2019-20",
"http://www.bcu.ac.uk/courses/health-studies-public-health-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/horology-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/computer-forensics-bsc-hons-msci-2019-20",
"http://www.bcu.ac.uk/courses/computer-science-bsc-hons-msci-2019-20",
"http://www.bcu.ac.uk/courses/graphic-communication-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/global-sport-management-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/computer-networks-bsc-hons-msci-2019-20",
"http://www.bcu.ac.uk/courses/conductive-education-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/film-technology-and-visual-effects-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/international-business-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/illustration-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/bmus-honours-jazz-2019-20",
"http://www.bcu.ac.uk/courses/jewellery-and-objects-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/international-jewellery-business-ba-honours-2019-20",
"http://www.bcu.ac.uk/courses/journalism-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/landscape-architecture-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/landscape-architecture-ba-hons-china-delivery-2019-20",
"http://www.bcu.ac.uk/courses/law-llb-2019-20",
"http://www.bcu.ac.uk/courses/biomedical-engineering-beng-meng-2019-20",
"http://www.bcu.ac.uk/courses/law-with-american-legal-studies-llb-2019-20",
"http://www.bcu.ac.uk/courses/law-with-business-llb-2019-20",
"http://www.bcu.ac.uk/courses/law-with-criminology-llb-2019-20",
"http://www.bcu.ac.uk/courses/marketing-consumer-psychology-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/marketing-advertising-and-public-relations-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/marketing-digital-media-and-technologies-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/mechanical-engineering-beng-meng-2019-20",
"http://www.bcu.ac.uk/courses/marketing-professional-practice-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/civil-engineering-beng-meng-2019-20",
"http://www.bcu.ac.uk/courses/media-production-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/marketing-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/sociology-and-criminology-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/music-bmus-honours-2019-20",
"http://www.bcu.ac.uk/courses/stage-management-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/media-and-communication-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/sociology-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/music-industries-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/sport-and-exercise-science-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/food-and-nutrition-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/sports-journalism-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/sound-engineering-and-production-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/sport-and-exercise-nutrition-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/video-game-design-and-production-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/textile-design-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/working-with-children-young-people-families-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/video-game-digital-art-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/video-game-development-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/automotive-engineering-beng-meng-2019-20",
"http://www.bcu.ac.uk/courses/interior-architecture-design-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/music-technology-bsc-honours-2019-20",
"http://www.bcu.ac.uk/courses/physical-education-and-school-sport-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/photography-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/product-and-furniture-design-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/property-development-and-planning-bsc-hons-mplan-2019-20",
"http://www.bcu.ac.uk/courses/psychology-with-business-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/psychology-with-criminology-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/psychology-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/psychology-with-marketing-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/quantity-surveying-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/electronic-engineering-beng-meng-2019-20",
"http://www.bcu.ac.uk/courses/marketing-retailing-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/policing-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/primary-education-with-qts-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/photography-ba-hons-2019-20",
"http://www.bcu.ac.uk/courses/physical-education-and-school-sport-bsc-hons-2019-20",
"http://www.bcu.ac.uk/courses/property-development-and-planning-bsc-hons-mplan-2019-20",
"http://www.bcu.ac.uk/courses/music-journalism-ba-hons-2019-20", ]
        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})


    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "Birmingham City University"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:
            # ucas_point = response.xpath("//li[@class='iconim points']//b[contains(text(),'UCAS points:')]/../span//text()").extract()
            # print("ucas_point: ", ucas_point)

            alevel = response.xpath(
                "//td[contains(text(),'A Level')]/following-sibling::td//text()|"
                "//strong[contains(text(),'A Level:')]/..//text()").extract()
            item['alevel'] = clear_lianxu_space(alevel)
            print("item['alevel']: ", item['alevel'])

            ib = response.xpath(
                "//h5[contains(text(),'EU/International students')]/following-sibling::table//td[contains(text(),'International Baccalaureate')]/following-sibling::td//text()|"
                "//p[contains(text(),'International Baccalaureate')]//text()|"
                "//strong[contains(text(),'International Baccalaureate:')]/../span//text()").extract()
            if len(ib) == 0:
                ib = response.xpath(
                    "//td[contains(text(),'International Baccalaureate')]/following-sibling::td//text()").extract()
            item['ib'] = clear_lianxu_space(ib)
            print("item['ib']: ", item['ib'])

            yield item

        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

