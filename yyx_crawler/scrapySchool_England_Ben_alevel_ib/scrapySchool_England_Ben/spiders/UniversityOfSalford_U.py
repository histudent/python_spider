import scrapy
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


class UniversityOfSalford_USpider(scrapy.Spider):
    name = "UniversityOfSalford_U"
    start_urls = [
        "https://www.salford.ac.uk/study/a-z-courses?root_node_selection=275503&page_asset_listing_279643_submit_button=Submit&queries_subject_query_posted=1&queries_subject_query=&current_result_page=1&results_per_page=0&submitted_search_category=&mode=&result_279643_result_page=A"]

    def parse(self, response):
        links = ["https://www.salford.ac.uk/ug-courses/music-creative-music-technology",
"https://www.salford.ac.uk/ug-courses/mechanical-engineering",
"https://www.salford.ac.uk/ug-courses/music-popular-music-and-recording",
"https://www.salford.ac.uk/ug-courses/midwifery-156-weeks",
"https://www.salford.ac.uk/ug-courses/interior-architecture",
"https://www.salford.ac.uk/ug-courses/mechanical-engineering2",
"https://www.salford.ac.uk/ug-courses/marine-biology",
"https://www.salford.ac.uk/ug-courses/international-events-management",
"https://www.salford.ac.uk/ug-courses/integrated-practice-in-learning-disabilities-nursing-and-social-work",
"https://www.salford.ac.uk/ug-courses/international-business",
"https://www.salford.ac.uk/ug-courses/international-relations-and-politics",
"https://www.salford.ac.uk/ug-courses/international-politics-and-security",
"https://www.salford.ac.uk/ug-courses/sport-rehabilitation",
"https://www.salford.ac.uk/ug-courses/software-engineering",
"https://www.salford.ac.uk/ug-courses/acoustical-and-audio-engineering",
"https://www.salford.ac.uk/ug-courses/social-work-studies",
"https://www.salford.ac.uk/ug-courses/sound-engineering-and-production",
"https://www.salford.ac.uk/ug-courses/interior-design",
"https://www.salford.ac.uk/ug-courses/law-with-criminology",
"https://www.salford.ac.uk/ug-courses/sociology",
"https://www.salford.ac.uk/ug-courses/law-with-management",
"https://www.salford.ac.uk/ug-courses/sports-science-strength-and-conditioning-or-human-performance-pathways",
"https://www.salford.ac.uk/ug-courses/digital-business",
"https://www.salford.ac.uk/ug-courses/technical-theatre-production-and-design",
"https://www.salford.ac.uk/ug-courses/business-management-with-sport",
"https://www.salford.ac.uk/ug-courses/television-and-radio",
"https://www.salford.ac.uk/ug-courses/building-surveying-msci",
"https://www.salford.ac.uk/ug-courses/theatre-performance-practice",
"https://www.salford.ac.uk/ug-courses/business-information-technology",
"https://www.salford.ac.uk/ug-courses/quantity-surveying",
"https://www.salford.ac.uk/ug-courses/business-management-with-law",
"https://www.salford.ac.uk/ug-courses/occupational-therapy",
"https://www.salford.ac.uk/ug-courses/business-and-management",
"https://www.salford.ac.uk/ug-courses/property-and-real-estate",
"https://www.salford.ac.uk/ug-courses/business-and-economics",
"https://www.salford.ac.uk/ug-courses/podiatry",
"https://www.salford.ac.uk/ug-courses/business-and-financial-management",
"https://www.salford.ac.uk/ug-courses/psychology-first-year-taught-at-salford-city-college",
"https://www.salford.ac.uk/ug-courses/corporate-law",
"https://www.salford.ac.uk/ug-courses/pharmaceutical-science",
"https://www.salford.ac.uk/ug-courses/computer-science-with-data-analytics",
"https://www.salford.ac.uk/ug-courses/physics2",
"https://www.salford.ac.uk/ug-courses/computer-science-with-web-development",
"https://www.salford.ac.uk/ug-courses/psychology-and-criminology",
"https://www.salford.ac.uk/ug-courses/computer-science-with-cyber-security",
"https://www.salford.ac.uk/ug-courses/physics",
"https://www.salford.ac.uk/ug-courses/financial-mathematics",
"https://www.salford.ac.uk/ug-courses/prosthetics-and-orthotics",
"https://www.salford.ac.uk/ug-courses/human-resource-management",
"https://www.salford.ac.uk/ug-courses/psychology-and-criminology-first-year-taught-at-salford-city-college",
"https://www.salford.ac.uk/ug-courses/law",
"https://www.salford.ac.uk/ug-courses/psychology",
"https://www.salford.ac.uk/ug-courses/law-media-and-digital-industries",
"https://www.salford.ac.uk/ug-courses/physics-with-acoustics2",
"https://www.salford.ac.uk/ug-courses/music-musical-arts",
"https://www.salford.ac.uk/ug-courses/pure-and-applied-physics",
"https://www.salford.ac.uk/ug-courses/marketing",
"https://www.salford.ac.uk/ug-courses/psychology-and-counselling",
"https://www.salford.ac.uk/ug-courses/music-production-and-sound-science",
"https://www.salford.ac.uk/ug-courses/physiotherapy",
"https://www.salford.ac.uk/ug-courses/music-creative-music-technology",
"https://www.salford.ac.uk/ug-courses/professional-sound-and-video-technology",
"https://www.salford.ac.uk/ug-courses/music-popular-music-and-recording",
"https://www.salford.ac.uk/ug-courses/physics-with-acoustics",
"https://www.salford.ac.uk/ug-courses/mechanical-engineering2",
"https://www.salford.ac.uk/ug-courses/petroleum-and-mechanical-engineering",
"https://www.salford.ac.uk/ug-courses/international-events-management",
"https://www.salford.ac.uk/ug-courses/photography",
"https://www.salford.ac.uk/ug-courses/international-business",
"https://www.salford.ac.uk/ug-courses/politics",
"https://www.salford.ac.uk/ug-courses/sport-rehabilitation",
"https://www.salford.ac.uk/ug-courses/public-health-and-health-promotion",
"https://www.salford.ac.uk/ug-courses/software-engineering",
"https://www.salford.ac.uk/ug-courses/public-health-and-health-promotion-with-placement",
"https://www.salford.ac.uk/ug-courses/automotive-and-autonomous-vehicle-technology",
"https://www.salford.ac.uk/ug-courses/psychology-of-sport",
"https://www.salford.ac.uk/ug-courses/automotive-and-autonomous-vehicle-technology",
"https://www.salford.ac.uk/ug-courses/wildlife-and-practical-conservation",
"https://www.salford.ac.uk/ug-courses/accounting-and-finance",
"https://www.salford.ac.uk/ug-courses/wildlife-conservation-with-zoo-biology",
"https://www.salford.ac.uk/ug-courses/accounting-and-finance",
"https://www.salford.ac.uk/ug-courses/psychology-with-english-language",
"https://www.salford.ac.uk/ug-courses/zoology-with-marine-biology",
"https://www.salford.ac.uk/ug-courses/zoology",
"https://www.salford.ac.uk/ug-courses/animation",
"https://www.salford.ac.uk/ug-courses/archaeology-and-geography-with-professional-practice",
"https://www.salford.ac.uk/ug-courses/aircraft-engineering-with-pilot-studies",
"https://www.salford.ac.uk/ug-courses/aeronautical-engineering2",
"https://www.salford.ac.uk/ug-courses/architectural-engineering",
"https://www.salford.ac.uk/ug-courses/aircraft-engineering-with-pilot-studies2",
"https://www.salford.ac.uk/ug-courses/automotive-and-autonomous-vehicle-technology",
"https://www.salford.ac.uk/ug-courses/accounting-and-finance",
"https://www.salford.ac.uk/ug-courses/aeronautical-engineering",
"https://www.salford.ac.uk/ug-courses/architectural-design-and-technology",
"https://www.salford.ac.uk/ug-courses/architecture",
"https://www.salford.ac.uk/ug-courses/acoustical-and-audio-engineering",
"https://www.salford.ac.uk/ug-courses/physics-with-studies-in-north-america",
"https://www.salford.ac.uk/ug-courses/sound-engineering-and-production",
"https://www.salford.ac.uk/ug-courses/sports-coaching-analysis",
"https://www.salford.ac.uk/ug-courses/law-with-criminology",
"https://www.salford.ac.uk/ug-courses/social-policy",
"https://www.salford.ac.uk/ug-courses/law-with-management",
"https://www.salford.ac.uk/ug-courses/fine-art",
"https://www.salford.ac.uk/ug-courses/biochemistry",
"https://www.salford.ac.uk/ug-courses/biomedical-science",
"https://www.salford.ac.uk/ug-courses/film-studies",
"https://www.salford.ac.uk/ug-courses/dance",
"https://www.salford.ac.uk/ug-courses/digital-media",
"https://www.salford.ac.uk/ug-courses/diagnostic-radiography",
"https://www.salford.ac.uk/ug-courses/drama-and-creative-writing",
"https://www.salford.ac.uk/ug-courses/english-and-creative-writing",
"https://www.salford.ac.uk/ug-courses/english-language-and-creative-writing",
"https://www.salford.ac.uk/ug-courses/electronic-engineering",
"https://www.salford.ac.uk/ug-courses/english-language",
"https://www.salford.ac.uk/ug-courses/digital-business",
"https://www.salford.ac.uk/ug-courses/english-literature-with-english-language",
"https://www.salford.ac.uk/ug-courses/english-literature",
"https://www.salford.ac.uk/ug-courses/exercise-nutrition-and-health",
"https://www.salford.ac.uk/ug-courses/english-and-film-studies",
"https://www.salford.ac.uk/ug-courses/environmental-management",
"https://www.salford.ac.uk/ug-courses/english-and-drama",
"https://www.salford.ac.uk/ug-courses/building-surveying",
"https://www.salford.ac.uk/ug-courses/business-and-tourism-management",
"https://www.salford.ac.uk/ug-courses/business-management-with-sport",
"https://www.salford.ac.uk/ug-courses/building-surveying-msci",
"https://www.salford.ac.uk/ug-courses/business-information-technology",
"https://www.salford.ac.uk/ug-courses/business-management-with-law",
"https://www.salford.ac.uk/ug-courses/biology-with-studies-in-the-usa",
"https://www.salford.ac.uk/ug-courses/business-and-management",
"https://www.salford.ac.uk/ug-courses/biochemistry-with-studies-in-the-usa",
"https://www.salford.ac.uk/ug-courses/business-and-economics",
"https://www.salford.ac.uk/ug-courses/biology",
"https://www.salford.ac.uk/ug-courses/business-and-financial-management",
"https://www.salford.ac.uk/ug-courses/corporate-law",
"https://www.salford.ac.uk/ug-courses/criminology-and-sociology",
"https://www.salford.ac.uk/ug-courses/contemporary-history-and-politics",
"https://www.salford.ac.uk/ug-courses/civil-engineering3",
"https://www.salford.ac.uk/ug-courses/computer-science",
"https://www.salford.ac.uk/ug-courses/counselling-and-psychotherapy-professional-practice",
"https://www.salford.ac.uk/ug-courses/computer-networks",
"https://www.salford.ac.uk/ug-courses/civil-engineering",
"https://www.salford.ac.uk/ug-courses/contemporary-military-and-international-history",
"https://www.salford.ac.uk/ug-courses/comedy-writing-performance",
"https://www.salford.ac.uk/ug-courses/civil-engineering2",
"https://www.salford.ac.uk/ug-courses/computer-science-with-data-analytics",
"https://www.salford.ac.uk/ug-courses/civil-and-architectural-engineering2",
"https://www.salford.ac.uk/ug-courses/construction-project-management",
"https://www.salford.ac.uk/ug-courses/costume-design",
"https://www.salford.ac.uk/ug-courses/criminology-with-security",
"https://www.salford.ac.uk/ug-courses/criminology",
"https://www.salford.ac.uk/ug-courses/computer-science-with-web-development",
"https://www.salford.ac.uk/ug-courses/civil-and-architectural-engineering",
"https://www.salford.ac.uk/ug-courses/computer-science-with-cyber-security",
"https://www.salford.ac.uk/ug-courses/chemistry",
"https://www.salford.ac.uk/ug-courses/criminology-with-counselling",
"https://www.salford.ac.uk/ug-courses/film-production",
"https://www.salford.ac.uk/ug-courses/fashion-design",
"https://www.salford.ac.uk/ug-courses/financial-mathematics",
"https://www.salford.ac.uk/ug-courses/fashion-image-making-and-styling",
"https://www.salford.ac.uk/ug-courses/graphic-design-first-year-taught-at-carmel-college",
"https://www.salford.ac.uk/ug-courses/film-and-tv-set-design",
"https://www.salford.ac.uk/ug-courses/ba-geography",
"https://www.salford.ac.uk/ug-courses/graphic-design",
"https://www.salford.ac.uk/ug-courses/games-design-production",
"https://www.salford.ac.uk/ug-courses/games-design-production-with-industry-placement",
"https://www.salford.ac.uk/ug-courses/geography",
"https://www.salford.ac.uk/ug-courses/human-resource-management",
"https://www.salford.ac.uk/ug-courses/human-biology-and-infectious-diseases",
"https://www.salford.ac.uk/ug-courses/nursing-rn-mental-health",
"https://www.salford.ac.uk/ug-courses/nursing-rn-children-and-young-peoples",
"https://www.salford.ac.uk/ug-courses/nursing-rn-adult",
"https://www.salford.ac.uk/ug-courses/law",
"https://www.salford.ac.uk/ug-courses/journalism-pr",
"https://www.salford.ac.uk/ug-courses/law-media-and-digital-industries",
"https://www.salford.ac.uk/ug-courses/journalism-multimedia",
"https://www.salford.ac.uk/ug-courses/journalism-broadcast",
"https://www.salford.ac.uk/ug-courses/music-musical-arts",
"https://www.salford.ac.uk/ug-courses/marketing",
"https://www.salford.ac.uk/ug-courses/media-technology",
"https://www.salford.ac.uk/ug-courses/media-performance",
"https://www.salford.ac.uk/ug-courses/music-production-and-sound-science",
"https://www.salford.ac.uk/ug-courses/medicinal-chemistry",
"https://www.salford.ac.uk/ug-courses/mathematics", ]
        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Salford"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:

            alevel = response.xpath("//*[contains(text(),'A level')]/following-sibling::td//text()").extract()
            if len(alevel) == 0:
                alevel = response.xpath("//*[contains(text(),'UCAS tariff points')]/following-sibling::td//text()").extract()
            item['alevel'] = clear_lianxu_space(alevel)
            print("item['alevel']: ", item['alevel'])

            ib = response.xpath("//*[contains(text(),'International Baccalaureate')]/following-sibling::td//text()").extract()
            item['ib'] = clear_lianxu_space(ib)
            print("item['ib']: ", item['ib'])

            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)
