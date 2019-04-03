# -*- coding: utf-8 -*-
import scrapy, requests
from lxml import etree
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re, json
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime

class UniversityOfHertfordshire_USpider(scrapy.Spider):
    name = "UniversityOfHertfordshire_U"
    # allowed_domains = ["herts.ac.uk", "funnelback.co.uk"]
#     start_urls = ["https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=1&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
# "https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=11&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
# "https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=21&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
# "https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=31&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
# "https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=41&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
# "https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=51&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
# "https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=61&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
# "https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=71&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
# "https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=81&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
# "https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=91&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
# "https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=101&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
# "https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=111&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
# "https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=121&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
# "https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=131&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
# "https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=141&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
# "https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=151&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance", ]
    start_urls = ["https://www.herts.ac.uk/courses/international-tourism-management"]

    # rules = (
    #     Rule(LinkExtractor(allow=r"start_rank=\d+"), follow=True, callback='page'),
    #     # Rule(LinkExtractor(restrict_xpaths=r"//p[@class='pagination']/a"), follow=True, callback='page_url'),
    # )
    # def page(self, response):
    #     print(response.url)

    def parse(self, response):
        # print("======", response.url)
        links = ["https://www.herts.ac.uk/courses/model-design-character-and-creative-effects",
"https://www.herts.ac.uk/courses/international-tourism-management",
"https://www.herts.ac.uk/courses/ba-honssw-international-management-with-sandwich-placement-study-abroad-multiple-locations",
"https://www.herts.ac.uk/courses/international-business",
"https://www.herts.ac.uk/courses/interior-architecture-and-design",
"https://www.herts.ac.uk/courses/information-technology-management-for-business-itmb",
"https://www.herts.ac.uk/courses/international-tourism-management",
"https://www.herts.ac.uk/courses/international-business",
"https://www.herts.ac.uk/courses/information-technology-management-for-business-itmb",
"https://www.herts.ac.uk/courses/international-tourism-management",
"https://www.herts.ac.uk/courses/international-business",
"https://www.herts.ac.uk/courses/information-technology-management-for-business-itmb",
"https://www.herts.ac.uk/courses/information-technology-online2",
"https://www.herts.ac.uk/courses/illustration3",
"https://www.herts.ac.uk/courses/humanities-open-programme",
"https://www.herts.ac.uk/courses/marketing-with-fashion2",
"https://www.herts.ac.uk/courses/marketing-with-digital-communications",
"https://www.herts.ac.uk/courses/marketing-and-advertising",
"https://www.herts.ac.uk/courses/marketing",
"https://www.herts.ac.uk/courses/marketing",
"https://www.herts.ac.uk/courses/marketing",
"https://www.herts.ac.uk/courses/beng-hons-manufacturing-engineering-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/meng-hons-manufacturing-engineering-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/management2",
"https://www.herts.ac.uk/courses/bsc-hons-live-sound-and-lighting-technology",
"https://www.herts.ac.uk/courses/journalism-and-media",
"https://www.herts.ac.uk/courses/journalism-and-creative-writing",
"https://www.herts.ac.uk/courses/photography",
"https://www.herts.ac.uk/courses/pharmacy",
"https://www.herts.ac.uk/courses/management2",
"https://www.herts.ac.uk/courses/management2",
"https://www.herts.ac.uk/courses/pharmacology",
"https://www.herts.ac.uk/courses/pharmaceutical-science",
"https://www.herts.ac.uk/courses/bsc-hons-paramedic-science",
"https://www.herts.ac.uk/courses/nutrition",
"https://www.herts.ac.uk/courses/bsc-hons-nursing-mental-health",
"https://www.herts.ac.uk/courses/childrens-nursing",
"https://www.herts.ac.uk/courses/learning-disability-nursing",
"https://www.herts.ac.uk/courses/adult-nursing",
"https://www.herts.ac.uk/courses/radiotherapy-and-oncology",
"https://www.herts.ac.uk/courses/psychology",
"https://www.herts.ac.uk/courses/ba-hons-product-and-industrial-design-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/midwifery-with-rm",
"https://www.herts.ac.uk/courses/ba-hons-politics-and-international-relations-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/physiotherapy",
"https://www.herts.ac.uk/courses/physics3",
"https://www.herts.ac.uk/courses/physics",
"https://www.herts.ac.uk/courses/physical-geography",
"https://www.herts.ac.uk/courses/bsc-hons-physical-activity-and-sports-development-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/media-and-publishing",
"https://www.herts.ac.uk/courses/media-and-creative-writing",
"https://www.herts.ac.uk/courses/mechanical-engineering-and-mechatronics2",
"https://www.herts.ac.uk/courses/mechanical-engineering-and-mechatronics",
"https://www.herts.ac.uk/courses/mechanical-engineering3",
"https://www.herts.ac.uk/courses/mechanical-engineering2",
"https://www.herts.ac.uk/courses/mathematics",
"https://www.herts.ac.uk/courses/master-of-regulatory-science-pharmaceutical-and-devices",
"https://www.herts.ac.uk/courses/ba-hons-mass-communications-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/bachelor-of-laws-llb-hons-commercial-law-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/two-year-accelerated-llb-programme",
"https://www.herts.ac.uk/courses/law-degree-llb",
"https://www.herts.ac.uk/courses/automotive-technology-with-management",
"https://www.herts.ac.uk/courses/automotive-engineering-with-motorsport2",
"https://www.herts.ac.uk/courses/automotive-engineering-with-motorsport",
"https://www.herts.ac.uk/courses/automotive-engineering3",
"https://www.herts.ac.uk/courses/automotive-engineering2",
"https://www.herts.ac.uk/courses/education-studies-with-special-educational-needs-and-disability",
"https://www.herts.ac.uk/courses/education-studies-with-learning-and-teaching",
"https://www.herts.ac.uk/courses/education-studies",
"https://www.herts.ac.uk/courses/economics",
"https://www.herts.ac.uk/courses/economics",
"https://www.herts.ac.uk/courses/economics",
"https://www.herts.ac.uk/courses/early-childhood-education",
"https://www.herts.ac.uk/courses/ba-hons-digital-media-design-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/dietetics",
"https://www.herts.ac.uk/courses/bschons-diagnostic-radiography-and-imaging",
"https://www.herts.ac.uk/courses/ba-hons-design-crafts-textiles-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/ba-hons-design-crafts-jewellery-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/ba-hons-design-crafts-ceramics-and-glass-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/ba-hons-criminal-justice-and-criminology-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/computer-and-network-technology",
"https://www.herts.ac.uk/courses/computer-science-software-engineering3",
"https://www.herts.ac.uk/courses/computer-science-networks2",
"https://www.herts.ac.uk/courses/computer-science-artificial-intelligence2",
"https://www.herts.ac.uk/courses/computer-science",
"https://www.herts.ac.uk/courses/computer-science-software-engineering4",
"https://www.herts.ac.uk/courses/beng-hons-civil-engineering-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/meng-hons-civil-engineering-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/businesstourism",
"https://www.herts.ac.uk/courses/businessmarketing",
"https://www.herts.ac.uk/courses/business-studies2",
"https://www.herts.ac.uk/courses/business-economics",
"https://www.herts.ac.uk/courses/business-studies2",
"https://www.herts.ac.uk/courses/businessinformation-systems",
"https://www.herts.ac.uk/courses/businesshuman-resources",
"https://www.herts.ac.uk/courses/ba-hons-fashion-design-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/event-managementtourism2",
"https://www.herts.ac.uk/courses/bsc-hons-environmental-management-and-ecology-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/fashion-and-fashion-business",
"https://www.herts.ac.uk/courses/event-managementtourism",
"https://www.herts.ac.uk/courses/event-managementmarketing",
"https://www.herts.ac.uk/courses/business-studies2",
"https://www.herts.ac.uk/courses/event-managementtourism2",
"https://www.herts.ac.uk/courses/event-managementtourism2",
"https://www.herts.ac.uk/courses/meng-hons-electronic-engineering-and-mechatronics-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/electronic-engineering-and-mechatronics",
"https://www.herts.ac.uk/courses/electrical-and-electronic-engineering",
"https://www.herts.ac.uk/courses/electrical-and-electronic-engineering2",
"https://www.herts.ac.uk/courses/business-with-finance",
"https://www.herts.ac.uk/courses/businesseconomics",
"https://www.herts.ac.uk/courses/businessevent-management",
"https://www.herts.ac.uk/courses/accountingbusiness",
"https://www.herts.ac.uk/courses/business-administration",
"https://www.herts.ac.uk/courses/business-administration",
"https://www.herts.ac.uk/courses/biomedical-science",
"https://www.herts.ac.uk/courses/biological-sciences",
"https://www.herts.ac.uk/courses/biochemistry2",
"https://www.herts.ac.uk/courses/aerospace-systems-engineering-with-pilot-studies",
"https://www.herts.ac.uk/courses/aerospace-systems-engineering-with-pilot-studies3",
"https://www.herts.ac.uk/courses/aerospace-systems-engineering",
"https://www.herts.ac.uk/courses/astrophysics3",
"https://www.herts.ac.uk/courses/architecture",
"https://www.herts.ac.uk/courses/astrophysics",
"https://www.herts.ac.uk/courses/bsc-hons-audio-recording-and-production",
"https://www.herts.ac.uk/courses/aerospace-technology-with-pilot-studies",
"https://www.herts.ac.uk/courses/aerospace-technology-with-management",
"https://www.herts.ac.uk/courses/aerospace-systems-engineering-with-pilot-studies2",
"https://www.herts.ac.uk/courses/human-resource-management2",
"https://www.herts.ac.uk/courses/human-resource-management2",
"https://www.herts.ac.uk/courses/graphic-design",
"https://www.herts.ac.uk/courses/human-geography-and-environmental-studies",
"https://www.herts.ac.uk/courses/fine-art",
"https://www.herts.ac.uk/courses/human-geography",
"https://www.herts.ac.uk/courses/financial-mathematics",
"https://www.herts.ac.uk/courses/geography",
"https://www.herts.ac.uk/courses/human-resource-management2",
"https://www.herts.ac.uk/courses/human-geography-and-environmental-studies",
"https://www.herts.ac.uk/courses/human-geography-and-environmental-studies",
"https://www.herts.ac.uk/courses/aerospace-engineering-with-space-technology2",
"https://www.herts.ac.uk/courses/aerospace-engineering-with-space-technology",
"https://www.herts.ac.uk/courses/aerospace-engineering-with-space-technology4",
"https://www.herts.ac.uk/courses/aerospace-engineering-with-space-technology3",
"https://www.herts.ac.uk/courses/accounting-and-finance",
"https://www.herts.ac.uk/courses/accountingeconomics",
"https://www.herts.ac.uk/courses/ba-hons-accounting-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/ba-hons-accounting-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/ba-hons-accounting-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/3d-games-art-and-design",
"https://www.herts.ac.uk/courses/3d-computer-animation-and-modelling",
"https://www.herts.ac.uk/courses/2d-animation-and-character-for-digital-media",
"https://www.herts.ac.uk/courses/economics-with-finance",
"https://www.herts.ac.uk/courses/bachelor-of-laws-llb-hons-government-and-politics-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/finance",
"https://www.herts.ac.uk/courses/film-and-television-production",
"https://www.herts.ac.uk/courses/bachelors-of-law-llb-hons-criminal-justice-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/finance",
"https://www.herts.ac.uk/courses/finance",
"https://www.herts.ac.uk/courses/bsc-hons-music-production",
"https://www.herts.ac.uk/courses/music-industry-management",
"https://www.herts.ac.uk/courses/music-composition-and-technology-for-film-and-games",
"https://www.herts.ac.uk/courses/bsc-hons-music-and-sound-design-technology",
"https://www.herts.ac.uk/courses/ba-hons-multiplatform-journalism",
"https://www.herts.ac.uk/courses/motorsport-technology",
"https://www.herts.ac.uk/courses/molecular-biology3",
"https://www.herts.ac.uk/courses/model-design-special-effects",
"https://www.herts.ac.uk/courses/visual-effects-for-film-and-television",
"https://www.herts.ac.uk/courses/tourism-management",
"https://www.herts.ac.uk/courses/sports-therapy",
"https://www.herts.ac.uk/courses/bsc-hons-sports-coaching-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/bsc-hons-sport-business-management-with-optional-sandwich-placement-study-abroad",
"https://www.herts.ac.uk/courses/sport-and-exercise-science",
"https://www.herts.ac.uk/courses/songwriting-and-music-production",
"https://www.herts.ac.uk/courses/social-work",
"https://www.herts.ac.uk/courses/tourism-management",
"https://www.herts.ac.uk/courses/tourism-management",
"https://www.herts.ac.uk/courses/model-design-model-effects", ]
        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Hertfordshire"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:

            # //div[@class='how-to-apply-table']/preceding-sibling::*[position()>1]
            item['alevel'] = None
            alevel = response.xpath("//p[contains(text(),'UCAS points')]//text()").extract()
            if len(alevel) == 0:
                alevel = response.xpath("//li[contains(text(),'UCAS points')]//text()").extract()
                if len(alevel) == 0:
                    alevel = response.xpath("//*[contains(text(),'UCAS points')]//text()").extract()
                    if len(alevel) == 0:
                        alevel = response.xpath("//strong[contains(text(),'A-Levels')]/../following-sibling::p[1]//text()|"
                                                "//strong[contains(text(),'A Levels')]/../following-sibling::*[1]//text()").extract()

            if len(alevel) > 0:
                item['alevel'] = remove_class(clear_lianxu_space([alevel[0]]))
                if item['programme_en'] == "Nursing (Mental Health)":
                    item['alevel'] = remove_class(clear_lianxu_space(alevel))

            print("item['alevel']: ", item['alevel'])
            alevel1 = response.xpath("//p[contains(text(),'A level')]//text()").extract()
            print("alevel: ", alevel1)
            if len(alevel1) > 0:
                if alevel1[0] == item['alevel']:
                    item['alevel'] = item['alevel'] + "\n" + clear_lianxu_space(alevel1[1:])
                else:
                    item['alevel'] = item['alevel'] + "\n" + clear_lianxu_space(alevel1)

            print("item['alevel']===: ", item['alevel'])

            # //p[contains(text(),' IB')]
            item['ib'] = None
            ib = response.xpath("//p[contains(text(),' IB')]//text()|//*[contains(text(),'IB -')]//text()|//*[contains(text(),'IB –')]//text()").extract()
            if len(ib) == 0:
                ib = response.xpath(
                    "//strong[contains(text(),'International Baccalaureate')]/../following-sibling::p[1]//text()|"
                    "//h3[contains(text(),'International Baccalaureate')]/following-sibling::p[1]//text()").extract()
            if len(ib) > 0:
                item['ib'] = remove_class(clear_lianxu_space([ib[-1]]))
            print("item['ib']: ", item['ib'])


            yield item

        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)
