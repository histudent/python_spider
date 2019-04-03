from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
import re
from scrapySchool_Australian_ben.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_ben.getItem import get_item
from scrapySchool_Australian_ben.getTuition_fee import getTuition_fee
from scrapySchool_Australian_ben.items import ScrapyschoolAustralianBenItem
from scrapySchool_Australian_ben.remove_tags import remove_class
from scrapySchool_Australian_ben.getStartDate import getStartDateMonth
from scrapySchool_Australian_ben.getDuration import getIntDuration
from scrapySchool_Australian_ben.getIELTS import get_ielts
from w3lib.html import remove_tags
from lxml import etree
import requests

# 2019/03/21 星期四 数据更新
class DeakinUniversity_USpider(scrapy.Spider):
    name = "DeakinUniversity_U"
    # start_urls = ["http://www.deakin.edu.au/courses/find-a-course"]
#     start_urls = ["http://www.deakin.edu.au/course/bachelor-arts-international",
# "http://www.deakin.edu.au/course/bachelor-arts-honours-international",
# "http://www.deakin.edu.au/course/bachelor-arts-psychology-international",
# "http://www.deakin.edu.au/course/bachelor-arts-psychology-honours-international",
# "http://www.deakin.edu.au/course/bachelor-arts-advanced-honours-international",
# "http://www.deakin.edu.au/course/bachelor-arts-chinese-bachelor-commerce-international",
# "http://www.deakin.edu.au/course/bachelor-arts-master-teaching-secondary-international",
# "http://www.deakin.edu.au/course/bachelor-arts-bachelor-commerce-international",
# "http://www.deakin.edu.au/course/bachelor-arts-bachelor-laws-international",
# "http://www.deakin.edu.au/course/bachelor-arts-bachelor-science-international",
# "http://www.deakin.edu.au/course/bachelor-arts-master-arts-international-relations-international",
# "http://www.deakin.edu.au/course/bachelor-biomedical-science-international",
# "http://www.deakin.edu.au/course/bachelor-business-international",
# "http://www.deakin.edu.au/course/bachelor-business-sport-management-international",
# "http://www.deakin.edu.au/course/bachelor-commerce-international",
# "http://www.deakin.edu.au/course/bachelor-commerce-bachelor-information-systems-international",
# "http://www.deakin.edu.au/course/bachelor-commerce-bachelor-laws-international",
# "http://www.deakin.edu.au/course/bachelor-commerce-bachelor-science-international",
# "http://www.deakin.edu.au/course/bachelor-communication-advertising-international",
# "http://www.deakin.edu.au/course/bachelor-communication-digital-media-international",
# "http://www.deakin.edu.au/course/bachelor-communication-honours-international",
# "http://www.deakin.edu.au/course/bachelor-communication-journalism-international",
# "http://www.deakin.edu.au/course/bachelor-communication-public-relations-international",
# "http://www.deakin.edu.au/course/bachelor-computer-science-international",
# "http://www.deakin.edu.au/course/bachelor-construction-management-honours-international",
# "http://www.deakin.edu.au/course/bachelor-creative-arts-drama-international",
# "http://www.deakin.edu.au/course/bachelor-creative-arts-honours-international",
# "http://www.deakin.edu.au/course/bachelor-creative-arts-photography-international",
# "http://www.deakin.edu.au/course/bachelor-creative-arts-visual-arts-international",
# "http://www.deakin.edu.au/course/bachelor-creative-writing-international",
# "http://www.deakin.edu.au/course/bachelor-criminology-international",
# "http://www.deakin.edu.au/course/bachelor-criminology-bachelor-cyber-security-international",
# "http://www.deakin.edu.au/course/bachelor-criminology-bachelor-laws-international",
# "http://www.deakin.edu.au/course/bachelor-criminology-bachelor-psychological-science-international",
# "http://www.deakin.edu.au/course/bachelor-cyber-security-international",
# "http://www.deakin.edu.au/course/bachelor-design-3d-animation-international",
# "http://www.deakin.edu.au/course/bachelor-design-architecture-international",
# "http://www.deakin.edu.au/course/bachelor-design-architecture-bachelor-construction-management-honours-international",
# "http://www.deakin.edu.au/course/bachelor-design-digital-technologies-international",
# "http://www.deakin.edu.au/course/bachelor-design-visual-communication-international",
# "http://www.deakin.edu.au/course/bachelor-education-early-years-international",
# "http://www.deakin.edu.au/course/bachelor-education-primary-international",
# "http://www.deakin.edu.au/course/bachelor-environmental-engineering-honours-international",
# "http://www.deakin.edu.au/course/bachelor-environmental-science-environmental-management-and-sustainability-international",
# "http://www.deakin.edu.au/course/bachelor-environmental-science-honours-international",
# "http://www.deakin.edu.au/course/bachelor-environmental-science-marine-biology-international",
# "http://www.deakin.edu.au/course/bachelor-environmental-science-wildlife-and-conservation-biology-international",
# "http://www.deakin.edu.au/course/bachelor-exercise-and-sport-science-international",
# "http://www.deakin.edu.au/course/bachelor-exercise-and-sport-science-honours-international",
# "http://www.deakin.edu.au/course/bachelor-exercise-and-sport-science-bachelor-business-sport-management-international",
# "http://www.deakin.edu.au/course/bachelor-film-television-and-animation-international",
# "http://www.deakin.edu.au/course/bachelor-food-and-nutrition-sciences-honours-international",
# "http://www.deakin.edu.au/course/bachelor-forensic-science-international",
# "http://www.deakin.edu.au/course/bachelor-forensic-science-honours-international",
# "http://www.deakin.edu.au/course/bachelor-forensic-science-bachelor-criminology-international",
# "http://www.deakin.edu.au/course/bachelor-health-sciences-international",
# "http://www.deakin.edu.au/course/bachelor-health-sciences-honours-international",
# "http://www.deakin.edu.au/course/bachelor-health-sciences-bachelor-arts-international",
# "http://www.deakin.edu.au/course/bachelor-health-and-medical-science-honours-international",
# "http://www.deakin.edu.au/course/bachelor-health-and-physical-education-international",
# "http://www.deakin.edu.au/course/bachelor-information-systems-international",
# "http://www.deakin.edu.au/course/bachelor-information-systems-bachelor-information-technology-international",
# "http://www.deakin.edu.au/course/bachelor-information-technology-international",
# "http://www.deakin.edu.au/course/bachelor-information-technology-honours-international",
# "http://www.deakin.edu.au/course/bachelor-international-studies-international",
# "http://www.deakin.edu.au/course/bachelor-international-studies-global-scholar-international",
# "http://www.deakin.edu.au/course/bachelor-international-studies-bachelor-commerce-international",
# "http://www.deakin.edu.au/course/bachelor-laws-international",
# "http://www.deakin.edu.au/course/bachelor-laws-bachelor-international-studies-international",
# "http://www.deakin.edu.au/course/bachelor-nursing-international",
# "http://www.deakin.edu.au/course/bachelor-nursing-honours-international",
# "http://www.deakin.edu.au/course/bachelor-nursing-bachelor-midwifery-international",
# "http://www.deakin.edu.au/course/bachelor-nursing-bachelor-psychological-science-international",
# "http://www.deakin.edu.au/course/bachelor-nursing-bachelor-public-health-and-health-promotion-international",
# "http://www.deakin.edu.au/course/bachelor-nutrition-science-international",
# "http://www.deakin.edu.au/course/bachelor-nutrition-science-bachelor-commerce-international",
# "http://www.deakin.edu.au/course/bachelor-occupational-therapy-international",
# "http://www.deakin.edu.au/course/bachelor-property-and-real-estate-international",
# "http://www.deakin.edu.au/course/bachelor-property-and-real-estate-bachelor-commerce-international",
# "http://www.deakin.edu.au/course/bachelor-property-and-real-estate-bachelor-laws-international",
# "http://www.deakin.edu.au/course/bachelor-psychological-science-international",
# "http://www.deakin.edu.au/course/bachelor-psychological-science-honours-international",
# "http://www.deakin.edu.au/course/bachelor-public-health-and-health-promotion-international",
# "http://www.deakin.edu.au/course/bachelor-public-health-and-health-promotion-honours-international",
# "http://www.deakin.edu.au/course/bachelor-public-health-and-health-promotion-bachelor-commerce-international",
# "http://www.deakin.edu.au/course/bachelor-science-international",
# "http://www.deakin.edu.au/course/bachelor-science-honours-international",
# "http://www.deakin.edu.au/course/bachelor-science-master-teaching-secondary-international",
# "http://www.deakin.edu.au/course/bachelor-science-bachelor-laws-international",
# "http://www.deakin.edu.au/course/bachelor-social-work-international",
# "http://www.deakin.edu.au/course/bachelor-software-engineering-honours-international",
# "http://www.deakin.edu.au/course/bachelor-sport-development-international",
# "http://www.deakin.edu.au/course/bachelor-vision-science-master-optometry-international",
# "http://www.deakin.edu.au/course/bachelor-zoology-and-animal-science-international",
# "http://www.deakin.edu.au/course/bachelor-zoology-and-animal-science-honours-international", ]
    # 2019/03/21 星期四 数据更新
    start_urls = ["http://www.deakin.edu.au/course/bachelor-arts-international",
"http://www.deakin.edu.au/course/bachelor-arts-honours-international",
"http://www.deakin.edu.au/course/bachelor-arts-psychology-international",
"http://www.deakin.edu.au/course/bachelor-arts-psychology-honours-international",
"http://www.deakin.edu.au/course/bachelor-arts-advanced-honours-international",
"http://www.deakin.edu.au/course/bachelor-arts-master-teaching-secondary-international",
"http://www.deakin.edu.au/course/bachelor-arts-bachelor-commerce-international",
"http://www.deakin.edu.au/course/bachelor-arts-bachelor-laws-international",
"http://www.deakin.edu.au/course/bachelor-arts-bachelor-science-international",
"http://www.deakin.edu.au/course/bachelor-arts-master-arts-international-relations-international",
"http://www.deakin.edu.au/course/bachelor-biomedical-science-international",
"http://www.deakin.edu.au/course/bachelor-business-international",
"http://www.deakin.edu.au/course/bachelor-business-sport-management-international",
"http://www.deakin.edu.au/course/bachelor-business-analytics-international",
"http://www.deakin.edu.au/course/bachelor-commerce-international",
"http://www.deakin.edu.au/course/bachelor-commerce-bachelor-business-analytics-international",
"http://www.deakin.edu.au/course/bachelor-commerce-bachelor-laws-international",
"http://www.deakin.edu.au/course/bachelor-commerce-bachelor-science-international",
"http://www.deakin.edu.au/course/bachelor-communication-advertising-international",
"http://www.deakin.edu.au/course/bachelor-communication-digital-media-international",
"http://www.deakin.edu.au/course/bachelor-communication-honours-international",
"http://www.deakin.edu.au/course/bachelor-communication-journalism-international",
"http://www.deakin.edu.au/course/bachelor-communication-public-relations-international",
"http://www.deakin.edu.au/course/bachelor-computer-science-international",
"http://www.deakin.edu.au/course/bachelor-creative-arts-drama-international",
"http://www.deakin.edu.au/course/bachelor-creative-arts-honours-international",
"http://www.deakin.edu.au/course/bachelor-creative-arts-photography-international",
"http://www.deakin.edu.au/course/bachelor-creative-arts-visual-arts-international",
"http://www.deakin.edu.au/course/bachelor-creative-writing-international",
"http://www.deakin.edu.au/course/bachelor-criminology-international",
"http://www.deakin.edu.au/course/bachelor-criminology-bachelor-cyber-security-international",
"http://www.deakin.edu.au/course/bachelor-criminology-bachelor-laws-international",
"http://www.deakin.edu.au/course/bachelor-criminology-bachelor-psychological-science-international",
"http://www.deakin.edu.au/course/bachelor-cyber-security-international",
"http://www.deakin.edu.au/course/bachelor-design-3d-animation-international",
"http://www.deakin.edu.au/course/bachelor-design-digital-technologies-international",
"http://www.deakin.edu.au/course/bachelor-design-visual-communication-international",
"http://www.deakin.edu.au/course/bachelor-education-early-years-international",
"http://www.deakin.edu.au/course/bachelor-education-primary-international",
"http://www.deakin.edu.au/course/bachelor-environmental-engineering-honours-international",
"http://www.deakin.edu.au/course/bachelor-environmental-science-environmental-management-and-sustainability-international",
"http://www.deakin.edu.au/course/bachelor-environmental-science-honours-international",
"http://www.deakin.edu.au/course/bachelor-environmental-science-marine-biology-international",
"http://www.deakin.edu.au/course/bachelor-environmental-science-wildlife-and-conservation-biology-international",
"http://www.deakin.edu.au/course/bachelor-exercise-and-sport-science-international",
"http://www.deakin.edu.au/course/bachelor-exercise-and-sport-science-honours-international",
"http://www.deakin.edu.au/course/bachelor-exercise-and-sport-science-bachelor-business-sport-management-international",
"http://www.deakin.edu.au/course/bachelor-exercise-and-sport-science-bachelor-nutrition-science-international",
"http://www.deakin.edu.au/course/bachelor-film-television-and-animation-international",
"http://www.deakin.edu.au/course/bachelor-food-and-nutrition-sciences-honours-international",
"http://www.deakin.edu.au/course/bachelor-forensic-science-international",
"http://www.deakin.edu.au/course/bachelor-forensic-science-honours-international",
"http://www.deakin.edu.au/course/bachelor-forensic-science-bachelor-criminology-international",
"http://www.deakin.edu.au/course/bachelor-health-sciences-international",
"http://www.deakin.edu.au/course/bachelor-health-sciences-honours-international",
"http://www.deakin.edu.au/course/bachelor-health-sciences-bachelor-arts-international",
"http://www.deakin.edu.au/course/bachelor-health-and-medical-science-honours-international",
"http://www.deakin.edu.au/course/bachelor-health-and-physical-education-international",
"http://www.deakin.edu.au/course/bachelor-information-technology-international",
"http://www.deakin.edu.au/course/bachelor-information-technology-honours-international",
"http://www.deakin.edu.au/course/bachelor-international-studies-international",
"http://www.deakin.edu.au/course/bachelor-international-studies-global-scholar-international",
"http://www.deakin.edu.au/course/bachelor-international-studies-bachelor-commerce-international",
"http://www.deakin.edu.au/course/bachelor-laws-international",
"http://www.deakin.edu.au/course/bachelor-laws-honours-international",
"http://www.deakin.edu.au/course/bachelor-laws-bachelor-international-studies-international",
"http://www.deakin.edu.au/course/bachelor-nursing-international",
"http://www.deakin.edu.au/course/bachelor-nursing-honours-international",
"http://www.deakin.edu.au/course/bachelor-nursing-bachelor-midwifery-international",
"http://www.deakin.edu.au/course/bachelor-nursing-bachelor-psychological-science-international",
"http://www.deakin.edu.au/course/bachelor-nursing-bachelor-public-health-and-health-promotion-international",
"http://www.deakin.edu.au/course/bachelor-nutrition-science-international",
"http://www.deakin.edu.au/course/bachelor-nutrition-science-bachelor-commerce-international",
"http://www.deakin.edu.au/course/bachelor-occupational-therapy-international",
"http://www.deakin.edu.au/course/bachelor-property-and-real-estate-international",
"http://www.deakin.edu.au/course/bachelor-property-and-real-estate-bachelor-commerce-international",
"http://www.deakin.edu.au/course/bachelor-property-and-real-estate-bachelor-laws-international",
"http://www.deakin.edu.au/course/bachelor-psychological-science-international",
"http://www.deakin.edu.au/course/bachelor-psychological-science-honours-international",
"http://www.deakin.edu.au/course/bachelor-public-health-and-health-promotion-international",
"http://www.deakin.edu.au/course/bachelor-public-health-and-health-promotion-honours-international",
"http://www.deakin.edu.au/course/bachelor-public-health-and-health-promotion-bachelor-commerce-international",
"http://www.deakin.edu.au/course/bachelor-science-international",
"http://www.deakin.edu.au/course/bachelor-science-honours-international",
"http://www.deakin.edu.au/course/bachelor-science-master-teaching-secondary-international",
"http://www.deakin.edu.au/course/bachelor-science-bachelor-laws-international",
"http://www.deakin.edu.au/course/bachelor-social-work-international",
"http://www.deakin.edu.au/course/bachelor-software-engineering-honours-international",
"http://www.deakin.edu.au/course/bachelor-sport-development-international",
"http://www.deakin.edu.au/course/bachelor-vision-science-master-optometry-international",
"http://www.deakin.edu.au/course/bachelor-zoology-and-animal-science-international",]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "Deakin University"
        # item['country'] = 'Australia'
        # item['website'] = 'http://www.deakin.edu.au'
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        # 组合字典
        links = ["http://www.deakin.edu.au/course/bachelor-arts-international",
"http://www.deakin.edu.au/course/bachelor-arts-honours-international",
"http://www.deakin.edu.au/course/bachelor-arts-psychology-international",
"http://www.deakin.edu.au/course/bachelor-arts-psychology-honours-international",
"http://www.deakin.edu.au/course/bachelor-arts-advanced-honours-international",
"http://www.deakin.edu.au/course/bachelor-arts-chinese-bachelor-commerce-international",
"http://www.deakin.edu.au/course/bachelor-arts-master-teaching-secondary-international",
"http://www.deakin.edu.au/course/bachelor-arts-bachelor-commerce-international",
"http://www.deakin.edu.au/course/bachelor-arts-bachelor-laws-international",
"http://www.deakin.edu.au/course/bachelor-arts-bachelor-science-international",
"http://www.deakin.edu.au/course/bachelor-arts-master-arts-international-relations-international",
"http://www.deakin.edu.au/course/bachelor-biomedical-science-international",
"http://www.deakin.edu.au/course/bachelor-business-international",
"http://www.deakin.edu.au/course/bachelor-business-sport-management-international",
"http://www.deakin.edu.au/course/bachelor-commerce-international",
"http://www.deakin.edu.au/course/bachelor-commerce-bachelor-information-systems-international",
"http://www.deakin.edu.au/course/bachelor-commerce-bachelor-laws-international",
"http://www.deakin.edu.au/course/bachelor-commerce-bachelor-science-international",
"http://www.deakin.edu.au/course/bachelor-communication-advertising-international",
"http://www.deakin.edu.au/course/bachelor-communication-digital-media-international",
"http://www.deakin.edu.au/course/bachelor-communication-honours-international",
"http://www.deakin.edu.au/course/bachelor-communication-journalism-international",
"http://www.deakin.edu.au/course/bachelor-communication-public-relations-international",
"http://www.deakin.edu.au/course/bachelor-computer-science-international",
"http://www.deakin.edu.au/course/bachelor-construction-management-honours-international",
"http://www.deakin.edu.au/course/bachelor-creative-arts-drama-international",
"http://www.deakin.edu.au/course/bachelor-creative-arts-honours-international",
"http://www.deakin.edu.au/course/bachelor-creative-arts-photography-international",
"http://www.deakin.edu.au/course/bachelor-creative-arts-visual-arts-international",
"http://www.deakin.edu.au/course/bachelor-creative-writing-international",
"http://www.deakin.edu.au/course/bachelor-criminology-international",
"http://www.deakin.edu.au/course/bachelor-criminology-bachelor-cyber-security-international",
"http://www.deakin.edu.au/course/bachelor-criminology-bachelor-laws-international",
"http://www.deakin.edu.au/course/bachelor-criminology-bachelor-psychological-science-international",
"http://www.deakin.edu.au/course/bachelor-cyber-security-international",
"http://www.deakin.edu.au/course/bachelor-design-3d-animation-international",
"http://www.deakin.edu.au/course/bachelor-design-architecture-international",
"http://www.deakin.edu.au/course/bachelor-design-architecture-bachelor-construction-management-honours-international",
"http://www.deakin.edu.au/course/bachelor-design-digital-technologies-international",
"http://www.deakin.edu.au/course/bachelor-design-visual-communication-international",
"http://www.deakin.edu.au/course/bachelor-education-early-years-international",
"http://www.deakin.edu.au/course/bachelor-education-primary-international",
"http://www.deakin.edu.au/course/bachelor-environmental-engineering-honours-international",
"http://www.deakin.edu.au/course/bachelor-environmental-science-environmental-management-and-sustainability-international",
"http://www.deakin.edu.au/course/bachelor-environmental-science-honours-international",
"http://www.deakin.edu.au/course/bachelor-environmental-science-marine-biology-international",
"http://www.deakin.edu.au/course/bachelor-environmental-science-wildlife-and-conservation-biology-international",
"http://www.deakin.edu.au/course/bachelor-exercise-and-sport-science-international",
"http://www.deakin.edu.au/course/bachelor-exercise-and-sport-science-honours-international",
"http://www.deakin.edu.au/course/bachelor-exercise-and-sport-science-bachelor-business-sport-management-international",
"http://www.deakin.edu.au/course/bachelor-film-television-and-animation-international",
"http://www.deakin.edu.au/course/bachelor-food-and-nutrition-sciences-honours-international",
"http://www.deakin.edu.au/course/bachelor-forensic-science-international",
"http://www.deakin.edu.au/course/bachelor-forensic-science-honours-international",
"http://www.deakin.edu.au/course/bachelor-forensic-science-bachelor-criminology-international",
"http://www.deakin.edu.au/course/bachelor-health-sciences-international",
"http://www.deakin.edu.au/course/bachelor-health-sciences-honours-international",
"http://www.deakin.edu.au/course/bachelor-health-sciences-bachelor-arts-international",
"http://www.deakin.edu.au/course/bachelor-health-and-medical-science-honours-international",
"http://www.deakin.edu.au/course/bachelor-health-and-physical-education-international",
"http://www.deakin.edu.au/course/bachelor-information-systems-international",
"http://www.deakin.edu.au/course/bachelor-information-systems-bachelor-information-technology-international",
"http://www.deakin.edu.au/course/bachelor-information-technology-international",
"http://www.deakin.edu.au/course/bachelor-information-technology-honours-international",
"http://www.deakin.edu.au/course/bachelor-international-studies-international",
"http://www.deakin.edu.au/course/bachelor-international-studies-global-scholar-international",
"http://www.deakin.edu.au/course/bachelor-international-studies-bachelor-commerce-international",
"http://www.deakin.edu.au/course/bachelor-laws-international",
"http://www.deakin.edu.au/course/bachelor-laws-bachelor-international-studies-international",
"http://www.deakin.edu.au/course/bachelor-nursing-international",
"http://www.deakin.edu.au/course/bachelor-nursing-honours-international",
"http://www.deakin.edu.au/course/bachelor-nursing-bachelor-midwifery-international",
"http://www.deakin.edu.au/course/bachelor-nursing-bachelor-psychological-science-international",
"http://www.deakin.edu.au/course/bachelor-nursing-bachelor-public-health-and-health-promotion-international",
"http://www.deakin.edu.au/course/bachelor-nutrition-science-international",
"http://www.deakin.edu.au/course/bachelor-nutrition-science-bachelor-commerce-international",
"http://www.deakin.edu.au/course/bachelor-occupational-therapy-international",
"http://www.deakin.edu.au/course/bachelor-property-and-real-estate-international",
"http://www.deakin.edu.au/course/bachelor-property-and-real-estate-bachelor-commerce-international",
"http://www.deakin.edu.au/course/bachelor-property-and-real-estate-bachelor-laws-international",
"http://www.deakin.edu.au/course/bachelor-psychological-science-international",
"http://www.deakin.edu.au/course/bachelor-psychological-science-honours-international",
"http://www.deakin.edu.au/course/bachelor-public-health-and-health-promotion-international",
"http://www.deakin.edu.au/course/bachelor-public-health-and-health-promotion-honours-international",
"http://www.deakin.edu.au/course/bachelor-public-health-and-health-promotion-bachelor-commerce-international",
"http://www.deakin.edu.au/course/bachelor-science-international",
"http://www.deakin.edu.au/course/bachelor-science-honours-international",
"http://www.deakin.edu.au/course/bachelor-science-master-teaching-secondary-international",
"http://www.deakin.edu.au/course/bachelor-science-bachelor-laws-international",
"http://www.deakin.edu.au/course/bachelor-social-work-international",
"http://www.deakin.edu.au/course/bachelor-software-engineering-honours-international",
"http://www.deakin.edu.au/course/bachelor-sport-development-international",
"http://www.deakin.edu.au/course/bachelor-vision-science-master-optometry-international",
"http://www.deakin.edu.au/course/bachelor-zoology-and-animal-science-international",
"http://www.deakin.edu.au/course/bachelor-zoology-and-animal-science-honours-international", ]
        programme_dict = {}
        programme_list = ["Bachelor of Arts",
"Bachelor of Arts (Honours)",
"Bachelor of Arts (Psychology)",
"Bachelor of Arts (Psychology) (Honours)",
"Bachelor of Arts - Advanced (Honours)",
"Bachelor of Arts - Chinese/Bachelor of Commerce",
"Bachelor of Arts / Master of Teaching (Secondary)",
"Bachelor of Arts/Bachelor of Commerce",
"Bachelor of Arts/Bachelor of Laws",
"Bachelor of Arts/Bachelor of Science",
"Bachelor of Arts/Master of Arts (International Relations)",
"Bachelor of Biomedical Science",
"Bachelor of Business",
"Bachelor of Business (Sport Management)",
"Bachelor of Commerce",
"Bachelor of Commerce/Bachelor of Information Systems",
"Bachelor of Commerce/Bachelor of Laws",
"Bachelor of Commerce/Bachelor of Science",
"Bachelor of Communication (Advertising)",
"Bachelor of Communication (Digital Media)",
"Bachelor of Communication (Honours)",
"Bachelor of Communication (Journalism)",
"Bachelor of Communication (Public Relations)",
"Bachelor of Computer Science",
"Bachelor of Construction Management (Honours)",
"Bachelor of Creative Arts (Drama)",
"Bachelor of Creative Arts (Honours)",
"Bachelor of Creative Arts (Photography)",
"Bachelor of Creative Arts (Visual Arts)",
"Bachelor of Creative Writing",
"Bachelor of Criminology",
"Bachelor of Criminology/Bachelor of Cyber Security",
"Bachelor of Criminology/Bachelor of Laws",
"Bachelor of Criminology/Bachelor of Psychological Science",
"Bachelor of Cyber Security",
"Bachelor of Design (3D Animation)",
"Bachelor of Design (Architecture)",
"Bachelor of Design (Architecture)/Bachelor of Construction Management (Honours)",
"Bachelor of Design (Digital Technologies)",
"Bachelor of Design (Visual Communication)",
"Bachelor of Education (Early Years)",
"Bachelor of Education (Primary)",
"Bachelor of Environmental Engineering (Honours)",
"Bachelor of Environmental Science (Environmental Management and Sustainability)",
"Bachelor of Environmental Science (Honours)",
"Bachelor of Environmental Science (Marine Biology)",
"Bachelor of Environmental Science (Wildlife and Conservation Biology)",
"Bachelor of Exercise and Sport Science",
"Bachelor of Exercise and Sport Science (Honours)",
"Bachelor of Exercise and Sport Science/Bachelor of Business (Sport Management)",
"Bachelor of Film, Television and Animation",
"Bachelor of Food and Nutrition Sciences (Honours)",
"Bachelor of Forensic Science",
"Bachelor of Forensic Science (Honours)",
"Bachelor of Forensic Science/Bachelor of Criminology",
"Bachelor of Health Sciences",
"Bachelor of Health Sciences (Honours)",
"Bachelor of Health Sciences/Bachelor of Arts",
"Bachelor of Health and Medical Science (Honours)",
"Bachelor of Health and Physical Education",
"Bachelor of Information Systems",
"Bachelor of Information Systems/Bachelor of Information Technology",
"Bachelor of Information Technology",
"Bachelor of Information Technology (Honours)",
"Bachelor of International Studies",
"Bachelor of International Studies (Global Scholar)",
"Bachelor of International Studies/Bachelor of Commerce",
"Bachelor of Laws",
"Bachelor of Laws/Bachelor of International Studies",
"Bachelor of Nursing",
"Bachelor of Nursing (Honours)",
"Bachelor of Nursing/Bachelor of Midwifery",
"Bachelor of Nursing/Bachelor of Psychological Science",
"Bachelor of Nursing/Bachelor of Public Health and Health Promotion",
"Bachelor of Nutrition Science",
"Bachelor of Nutrition Science/Bachelor of Commerce",
"Bachelor of Occupational Therapy",
"Bachelor of Property and Real Estate",
"Bachelor of Property and Real Estate/Bachelor of Commerce",
"Bachelor of Property and Real Estate/Bachelor of Laws",
"Bachelor of Psychological Science",
"Bachelor of Psychological Science (Honours)",
"Bachelor of Public Health and Health Promotion",
"Bachelor of Public Health and Health Promotion (Honours)",
"Bachelor of Public Health and Health Promotion/Bachelor of Commerce",
"Bachelor of Science",
"Bachelor of Science (Honours)",
"Bachelor of Science / Master of Teaching (Secondary)",
"Bachelor of Science/Bachelor of Laws",
"Bachelor of Social Work",
"Bachelor of Software Engineering (Honours)",
"Bachelor of Sport Development",
"Bachelor of Vision Science/Master of Optometry",
"Bachelor of Zoology and Animal Science",
"Bachelor of Zoology and Animal Science (Honours)", ]
        for link in range(len(links)):
            url = links[link]
            programme_dict[url] = programme_list[link]
        item['major_type1'] =programme_dict.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            programme = response.xpath("//div[@class='module__banner-title']/h1//text()").extract()
            clear_space(programme)
            item['degree_name'] = ''.join(programme).strip()
            print("item['degree_name']: ", item['degree_name'])

            pro_re = re.findall(r"Bachelor", item['degree_name'])
            # print("pre_re: ", pro_re)
            if len(pro_re) < 2:
                programme_re = re.findall(r"\(.+\)", item['degree_name'].replace("(Honours)", ""))
                if len(programme_re) > 0:
                    item['programme_en'] = ''.join(programme_re).replace("(", "").replace(")", "").strip()
                else:
                    item['programme_en'] = item['degree_name'].replace("(Honours)", "").replace("Master of ", "").replace("Bachelor of", "").strip()
                item['programme_en'] = item['programme_en'].replace("  ", " ").strip()
                print("item['programme_en']: ", item['programme_en'])

                # //div[@class='module__summary--items']/div[1]/div[2]
                ielts = response.xpath("//h3[contains(text(),'English language requirements')]/../following-sibling::*[1]//text()").extract()
                clear_space(ielts)
                item['ielts_desc'] = ''.join(ielts).strip()
                print("item['ielts_desc']: ", item['ielts_desc'])

                ielts_d = get_ielts(item['ielts_desc'])
                item["ielts"] = ielts_d.get('IELTS')
                item["ielts_l"] = ielts_d.get('IELTS_L')
                item["ielts_s"] = ielts_d.get('IELTS_S')
                item["ielts_r"] = ielts_d.get('IELTS_R')
                item["ielts_w"] = ielts_d.get('IELTS_W')
                # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

                duration = response.xpath("//h3[contains(text(),'Duration')]/../following-sibling::div//text()").extract()
                clear_space(duration)
                # print("duration: ", duration)
                duration_re = re.findall(r".*full[\s\-]time", ''.join(duration).strip())
                item['duration'] = ''.join(duration_re).strip()
                # if item['duration'] == "":
                #     print("***duration 为空")
                # print("item['duration']: ", item['duration'])

                location = response.xpath("//div[@class='module__summary--icon-wrapper']//h3[@class='course__subheading'][contains(text(),'Campuses')]/../following-sibling::div//text()").extract()
                clear_space(location)
                item['location'] = ' '.join(location).strip()
                location_tmp = item['location']
                # print("item['location']: ", item['location'])

                # //div[@id='navigation__course']/following-sibling::div
                overview = response.xpath("//h2[contains(text(),'Course information')]/../..").extract()
                item['degree_overview_en'] = remove_class(clear_lianxu_space(overview))
                # if item['degree_overview_en'] == "":
                #     print("***degree_overview_en 为空")
                # print("item['degree_overview_en']: ", item['degree_overview_en'])

                modules = response.xpath("//div[@id='module__course-structure']").extract()
                item['modules_en'] = remove_class(clear_lianxu_space(modules))
                # if item['modules_en'] == "":
                #     print("***modules_en 为空")
                # print("item['modules_en']: ", item['modules_en'])

                start_date = response.xpath(
                    "//li[contains(text(),'Start date:')]//text()").extract()
                clear_space(start_date)
                # print("start_date: ", start_date)
                item['start_date'] = getStartDateMonth(' '.join(start_date).strip())
                # print("item['start_date']: ", item['start_date'])

                entry_requirements = response.xpath("//div[@data-section='entry requirements']").extract()
                item['rntry_requirements_en'] = remove_class(clear_lianxu_space(entry_requirements))
                # if item['rntry_requirements_en'] == "":
                #     print("***rntry_requirements_en 为空")
                # print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

                # //div[@data-section='fees and scholarships']
                tuition_fee = response.xpath("//div[@class='module__content-panel']//div[@class='module__key-information--item-content']/text()").extract()
                clear_space(tuition_fee)
                # print("tuition_fee: ", tuition_fee)
                tuition_fee = getTuition_fee(''.join(tuition_fee))
                item['tuition_fee'] = tuition_fee
                if item['tuition_fee'] == 0:
                    item['tuition_fee'] = None
                # print("item['tuition_fee']: ", item['tuition_fee'])

                career = response.xpath("//div[@data-section='graduate outcomes']|//div[@data-section='graduate outcomes']/following-sibling::div[1]|"
                                        "//h3[contains(text(),'Career outcomes')]/../..").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career))
                # if item['career_en'] == "":
                #     print("***career_en 为空")
                # print("item['career_en']: ", item['career_en'])

                # //div[@data-section='application information']/following-sibling::div[2]
                how_to_apply = response.xpath(
                    "//h3[contains(text(),'How to apply')]/../..").extract()
                item['apply_desc_en'] = remove_class(clear_lianxu_space(how_to_apply))
                # if item['apply_desc_en'] == "":
                #     print("***apply_desc_en 为空")
                # print("item['apply_desc_en']: ", item['apply_desc_en'])

                major_list_url = response.xpath("//h3[contains(text(), 'Major Sequences')]/..//a/@href|"
                                                "//h3[contains(text(), 'Major sequences')]/..//a/@href|"
                                                "//h3[contains(text(), 'Major sequences')]/following-sibling::ul[1]//a/@href|"
                                                "//td[contains(text(),'Major')]/preceding-sibling::td//a/@href").extract()
                clear_space(major_list_url)
                print("major_list_url: ", major_list_url)
                print(len(major_list_url))

                major_url_l = []
                for major_url in major_list_url:
                    if "major" in major_url:
                        major_url_l.append(major_url)
                print("major_url_l: ", major_url_l)
                print(len(major_url_l))
                if len(major_url_l) == 0:
                    item['url'] = response.url
                    print("item['url']2: ", item['url'])
                    yield item
                else:
                    for major_url in major_url_l:
                        headers_base = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",}
                        data = requests.get(major_url, headers=headers_base)
                        response_major = etree.HTML(data.text)
                        item['url'] = major_url
                        print("item['url']_major: ", item['url'])

                        programme_major = response_major.xpath("//div[@class='module__banner-title']/h1//text()")
                        item['programme_en'] = ''.join(programme_major).strip()
                        print("item['programme_en']_major: ", item['programme_en'])

                        location_major = response_major.xpath("//*[contains(text(),'Campuses')]/../following-sibling::div[1]//text()")
                        item['location'] = ''.join(location_major).strip()
                        if item['location'] == "":
                            item['location'] = location_tmp
                        # print("item['location']_major: ", item['location'])

                        overview_en = response_major.xpath(
                            "//h2[contains(text(),'Overview')]/../..")
                        overview_en_str = ""
                        if len(overview_en) > 0:
                            for o in overview_en:
                                overview_en_str += etree.tostring(o, encoding='unicode', method='html')
                        item['overview_en'] = remove_class(clear_lianxu_space([overview_en_str]))
                        # print("item['overview_en']_major: ", item['overview_en'])

                        modules_en = response_major.xpath(
                            "//h2[contains(text(),'Explore units')]/../..")
                        modules_en_str = ""
                        if len(modules_en) > 0:
                            for o in modules_en:
                                modules_en_str += etree.tostring(o, encoding='unicode', method='html')
                        item['modules_en'] = remove_class(clear_lianxu_space([modules_en_str]))
                        # print("item['modules_en']_major: ", item['modules_en'])
                        yield item
                        # else:
                        #     item['url'] = response.url
                        #     print("item['url']1: ", item['url'])
                        #     yield item
        except Exception as e:
            with open("scrapySchool_Australian_ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

