# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime

class UniversityOfPortsmouth_USpider(scrapy.Spider):
    name = "UniversityOfPortsmouth_U"
    # start_urls = ["http://www.port.ac.uk/courses/"]
    start_urls = ["https://www.port.ac.uk/study/courses?level=ug&mode=Full-time&page=1&results=10&sort=AZ"]

    # for i in range(20):
    #     url = "https://www.port.ac.uk/study/courses?level=ug&mode=Full-time&page="+str(i)+"&results=10&sort=AZ"
    #     start_urls.append(url)

    def parse(self, response):
        links = ["https://www.port.ac.uk/study/courses/bsc-hons-environmental-science",
"https://www.port.ac.uk/study/courses/ba-hons-english-language-and-linguistics-with-literature",
"https://www.port.ac.uk/study/courses/ba-hons-american-studies",
"https://www.port.ac.uk/study/courses/bsc-econ-hons-economics-finance-and-banking",
"https://www.port.ac.uk/study/courses/ba-hons-marketing",
"https://www.port.ac.uk/study/courses/ba-hons-history-with-sociology",
"https://www.port.ac.uk/study/courses/ba-hons-media-and-digital-practice",
"https://www.port.ac.uk/study/courses/ba-hons-international-development-studies",
"https://www.port.ac.uk/study/courses/ba-hons-journalism",
"https://www.port.ac.uk/study/courses/ba-hons-childhood-and-youth-studies",
"https://www.port.ac.uk/study/courses/bsc-hons-quantity-surveying",
"https://www.port.ac.uk/study/courses/bsc-hons-geography",
"https://www.port.ac.uk/study/courses/ba-hons-media-studies",
"https://www.port.ac.uk/study/courses/ba-hons-fashion-and-textile-design",
"https://www.port.ac.uk/study/courses/bsc-hons-forensic-psychology",
"https://www.port.ac.uk/study/courses/ba-hons-film-production",
"https://www.port.ac.uk/study/courses/bsc-hons-dental-hygiene-and-dental-therapy",
"https://www.port.ac.uk/study/courses/ba-hons-geography",
"https://www.port.ac.uk/study/courses/bsc-hons-criminology-and-forensic-studies",
"https://www.port.ac.uk/study/courses/bsc-hons-criminology-with-psychology",
"https://www.port.ac.uk/study/courses/ba-hons-business-and-management",
"https://www.port.ac.uk/study/courses/bsc-hons-digital-media",
"https://www.port.ac.uk/study/courses/bsc-hons-data-science-and-analytics",
"https://www.port.ac.uk/study/courses/bsc-hons-dental-hygiene",
"https://www.port.ac.uk/study/courses/bsc-hons-cyber-security-and-forensic-computing",
"https://www.port.ac.uk/study/courses/ba-hons-film-industries",
"https://www.port.ac.uk/study/courses/ba-hons-digital-marketing",
"https://www.port.ac.uk/study/courses/bsc-hons-geology",
"https://www.port.ac.uk/study/courses/ba-hons-financial-management-for-business",
"https://www.port.ac.uk/study/courses/ba-hons-film-industries-and-creative-writing",
"https://www.port.ac.uk/study/courses/ba-hons-international-business",
"https://www.port.ac.uk/study/courses/ba-hons-international-business-communication",
"https://www.port.ac.uk/study/courses/ba-hons-international-relations-with-international-development-studies",
"https://www.port.ac.uk/study/courses/ba-hons-international-relations",
"https://www.port.ac.uk/study/courses/ba-hons-interior-architecture-and-design",
"https://www.port.ac.uk/study/courses/beng-hons-innovation-engineering",
"https://www.port.ac.uk/study/courses/bsc-hons-product-design-and-innovation",
"https://www.port.ac.uk/study/courses/bsc-hons-social-work",
"https://www.port.ac.uk/study/courses/bsc-hons-sociology",
"https://www.port.ac.uk/study/courses/ba-hons-international-relations-and-politics",
"https://www.port.ac.uk/study/courses/ba-hons-international-relations-with-history",
"https://www.port.ac.uk/study/courses/ba-hons-politics",
"https://www.port.ac.uk/study/courses/bsc-hons-psychology",
"https://www.port.ac.uk/study/courses/ba-hons-childhood-and-youth-studies-with-criminology",
"https://www.port.ac.uk/study/courses/bsc-hons-sociology-with-media-studies",
"https://www.port.ac.uk/study/courses/ba-hons-international-trade-and-business-communication",
"https://www.port.ac.uk/study/courses/ba-hons-childhood-and-youth-studies-with-psychology",
"https://www.port.ac.uk/study/courses/bsc-hons-computer-animation-and-visual-effects",
"https://www.port.ac.uk/study/courses/meng-civil-engineering",
"https://www.port.ac.uk/study/courses/bsc-hons-business-and-systems-management",
"https://www.port.ac.uk/study/courses/ba-hons-communication-and-english-studies",
"https://www.port.ac.uk/study/courses/bsc-hons-sociology-and-criminology",
"https://www.port.ac.uk/study/courses/beng-hons-petroleum-engineering",
"https://www.port.ac.uk/study/courses/bsc-hons-physics-astrophysics-and-cosmology",
"https://www.port.ac.uk/study/courses/mphys-hons-physics-astrophysics-and-cosmology",
"https://www.port.ac.uk/study/courses/bsc-hons-computer-games-enterprise",
"https://www.port.ac.uk/study/courses/beng-hons-civil-engineering",
"https://www.port.ac.uk/study/courses/bsc-hons-pharmacology",
"https://www.port.ac.uk/study/courses/ba-hons-photography",
"https://www.port.ac.uk/study/courses/bsc-hons-physics",
"https://www.port.ac.uk/study/courses/meng-petroleum-engineering",
"https://www.port.ac.uk/study/courses/beng-hons-mechanical-and-manufacturing-engineering",
"https://www.port.ac.uk/study/courses/mphys-hons-physics",
"https://www.port.ac.uk/study/courses/mpharm-hons-pharmacy",
"https://www.port.ac.uk/study/courses/bsc-hons-palaeontology",
"https://www.port.ac.uk/study/courses/moptom-optometry",
"https://www.port.ac.uk/study/courses/ba-hons-musical-theatre",
"https://www.port.ac.uk/study/courses/bsc-hons-property-development",
"https://www.port.ac.uk/study/courses/llb-hons-law-with-business",
"https://www.port.ac.uk/study/courses/bsc-hons-music-and-sound-technology",
"https://www.port.ac.uk/study/courses/ba-hons-journalism-with-media-studies",
"https://www.port.ac.uk/study/courses/llb-hons-law-with-criminology",
"https://www.port.ac.uk/study/courses/ba-hons-journalism-with-english-language-and-linguistics",
"https://www.port.ac.uk/study/courses/llb-hons-law",
"https://www.port.ac.uk/study/courses/llb-hons-law-with-international-relations",
"https://www.port.ac.uk/study/courses/bsc-hons-mathematics-with-statistics",
"https://www.port.ac.uk/study/courses/bsc-hons-mathematics-for-finance-and-management",
"https://www.port.ac.uk/study/courses/bsc-hons-mathematics",
"https://www.port.ac.uk/study/courses/beng-hons-electronic-engineering",
"https://www.port.ac.uk/study/courses/mmath-mathematics",
"https://www.port.ac.uk/study/courses/meng-mechanical-engineering",
"https://www.port.ac.uk/study/courses/ba-hons-journalism-with-english-literature",
"https://www.port.ac.uk/study/courses/beng-hons-mechanical-engineering",
"https://www.port.ac.uk/study/courses/ba-hons-early-childhood-studies",
"https://www.port.ac.uk/study/courses/ba-hons-marketing-with-psychology",
"https://www.port.ac.uk/study/courses/ba-hons-drama-and-performance",
"https://www.port.ac.uk/study/courses/bsc-hons-marine-environmental-science",
"https://www.port.ac.uk/study/courses/ba-hons-modern-languages",
"https://www.port.ac.uk/study/courses/ba-hons-early-childhood-studies-with-psychology",
"https://www.port.ac.uk/study/courses/ba-hons-international-relations-and-languages",
"https://www.port.ac.uk/study/courses/bsc-hons-marine-biology",
"https://www.port.ac.uk/study/courses/ba-hons-hospitality-management",
"https://www.port.ac.uk/study/courses/ba-hons-economics-and-management",
"https://www.port.ac.uk/study/courses/ba-hons-international-development-studies-and-languages",
"https://www.port.ac.uk/study/courses/bsc-econ-hons-economics",
"https://www.port.ac.uk/study/courses/ba-hons-hospitality-management-with-tourism",
"https://www.port.ac.uk/study/courses/meng-electronic-engineering",
"https://www.port.ac.uk/study/courses/mlang-applied-languages",
"https://www.port.ac.uk/study/courses/ba-hons-history",
"https://www.port.ac.uk/study/courses/ba-hons-applied-languages",
"https://www.port.ac.uk/study/courses/bsc-hons-industrial-design",
"https://www.port.ac.uk/study/courses/ba-hons-human-resource-management-with-psychology",
"https://www.port.ac.uk/study/courses/ba-hons-history-with-politics",
"https://www.port.ac.uk/study/courses/ba-hons-illustration",
"https://www.port.ac.uk/study/courses/meng-innovation-engineering",
"https://www.port.ac.uk/study/courses/bsc-hons-computer-games-technology",
"https://www.port.ac.uk/study/courses/bsc-hons-criminology-and-criminal-justice",
"https://www.port.ac.uk/study/courses/ba-hons-graphic-design",
"https://www.port.ac.uk/study/courses/bsc-hons-computer-networks",
"https://www.port.ac.uk/study/courses/bsc-hons-creative-media-technologies",
"https://www.port.ac.uk/study/courses/ba-hons-creative-writing",
"https://www.port.ac.uk/study/courses/bsc-hons-computing",
"https://www.port.ac.uk/study/courses/beng-hons-construction-engineering-management",
"https://www.port.ac.uk/study/courses/ba-hons-english-and-creative-writing",
"https://www.port.ac.uk/study/courses/ba-hons-english-literature",
"https://www.port.ac.uk/study/courses/ba-hons-english-literature-with-history",
"https://www.port.ac.uk/study/courses/meng-computer-science",
"https://www.port.ac.uk/study/courses/ba-hons-english-language-and-linguistics",
"https://www.port.ac.uk/study/courses/bsc-hons-computer-science",
"https://www.port.ac.uk/study/courses/beng-hons-engineering-geology-and-geotechnics",
"https://www.port.ac.uk/study/courses/bsc-hons-criminology-and-cybercrime",
"https://www.port.ac.uk/study/courses/bsc-hons-exercise-and-fitness-management",
"https://www.port.ac.uk/study/courses/beng-hons-engineering-and-technology-with-foundation-year",
"https://www.port.ac.uk/study/courses/ba-hons-english-literature-with-media-studies",
"https://www.port.ac.uk/study/courses/ba-hons-american-studies-with-history",
"https://www.port.ac.uk/study/courses/ba-hons-accounting-with-finance",
"https://www.port.ac.uk/study/courses/ba-hons-animation",
"https://www.port.ac.uk/study/courses/ba-hons-architecture",
"https://www.port.ac.uk/study/courses/bsc-hons-biochemistry",
"https://www.port.ac.uk/study/courses/bsc-hons-biology",
"https://www.port.ac.uk/study/courses/ba-hons-business-and-human-resource-management",
"https://www.port.ac.uk/study/courses/ba-hons-business-management-and-entrepreneurship",
"https://www.port.ac.uk/study/courses/ba-hons-american-studies-with-english",
"https://www.port.ac.uk/study/courses/bsc-hons-business-information-systems",
"https://www.port.ac.uk/study/courses/bsc-hons-advanced-dental-nursing",
"https://www.port.ac.uk/study/courses/bsc-hons-biomedical-science",
"https://www.port.ac.uk/study/courses/bsc-hons-building-surveying",
"https://www.port.ac.uk/study/courses/bsc-econ-hons-business-economics",
"https://www.port.ac.uk/study/courses/bsc-hons-sport-and-exercise-science",
"https://www.port.ac.uk/study/courses/bsc-hons-television-and-broadcasting",
"https://www.port.ac.uk/study/courses/bsc-hons-sport-and-exercise-psychology",
"https://www.port.ac.uk/study/courses/bsc-hons-sports-management-and-development",
"https://www.port.ac.uk/study/courses/bsc-hons-software-engineering",
"https://www.port.ac.uk/study/courses/bsc-hons-business-and-supply-chain-management",
"https://www.port.ac.uk/study/courses/bsc-hons-sociology-with-psychology", ]

        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Portsmouth"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:
            rntry_requirements_content = response.xpath(
                "//div[contains(text(),'Entry Requirements')]/../../..//div[contains(text(),'2019 start')]/../../../..//text()").extract()
            rntry_requirements_str = clear_lianxu_space(rntry_requirements_content)

            alevel = response.xpath("//*[contains(text(),'A level')]/text()").extract()
            print("====", alevel)
            if len(alevel) == 0:
                alevel = re.findall(r".{1,45}A\slevels.{1,85}", rntry_requirements_str)
            clear_space(alevel)
            if len(alevel) > 0:
                item['alevel'] = ''.join(alevel[1:]).strip()
                if item['alevel'] == "":
                    item['alevel'] = ''.join(alevel).strip()
            print("item['alevel']: ", item['alevel'])


            # item["ib"] = "Most courses will require between 24 and 31 points in the International Baccalaureate (IB), depending on the degree you apply for."
            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a',
                      encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

