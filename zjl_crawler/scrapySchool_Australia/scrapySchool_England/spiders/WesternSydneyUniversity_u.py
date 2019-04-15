# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/1 17:30'
import scrapy,json
import re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from w3lib.html import remove_tags
from scrapySchool_England.clearSpace import clear_space_str
import requests
from lxml import etree
from scrapySchool_England.translate_date import tracslateDate
from scrapySchool_England.getTuition_fee import getT_fee
class WesternSydneyUniversitySpider(scrapy.Spider):
    name = 'WesternSydneyUniversity_u'
    allowed_domains = ['westernsydney.edu.au/']
    start_urls = []
    C = [
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-international-studies.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-advanced-honours.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-international-studies.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-advanced-honours.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-social-science-geography-and-urban-studies.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing-graduate-entry.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-social-science-geography-and-urban-studies.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-design-and-technology.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing-graduate-entry.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems-advanced.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing-graduate-entry.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-creative-industries.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing-graduate-entry.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-advanced-honours.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-advanced-honours.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-design-and-technology.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems-advanced.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-humanitarian-and-development-studies.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-advanced-honours.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-advanced-honours.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-industrial-design-honours.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-planning-pathway-to-master-of-urban-management-and-planning.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-criminal-and-community-justice.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-planning-pathway-to-master-of-urban-management-and-planning.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-creative-industries.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-criminal-and-community-justice.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-building-design-management.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-design-and-technology.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-industrial-design-honours.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-building-design-management.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems-advanced.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-with-a-key-program-in-psychology.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-with-a-key-program-in-psychology.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-creative-industries.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-with-a-key-program-in-psychology.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-industrial-design-honours.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems-advanced.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-creative-industries.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-mathematicalscience.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-mathematicalscience.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-creative-industries.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-anthropology.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-anthropology.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-creative-industries.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-environmental-science.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-environmental-science.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science-health-and-physical-education.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-construction-management.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-environmental-science.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-construction-management.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-health-information-management.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-health-information-management.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-environmental-science.html",
        "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-health-information-management.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-natural-science-animal-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-social-work.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-social-work.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-environmental-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-natural-science-animal-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-social-science-criminology-and-criminal-justice.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-social-science-criminology-and-criminal-justice.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-environmental-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-social-science-criminology-and-criminal-justice.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-social-science-criminology-and-criminal-justice.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science-paramedicine.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-ict.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-entrepreneurship-games-design-and-simulation.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-entrepreneurship-games-design-and-simulation.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-humanitarian-and-development-studies.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-humanitarian-and-development-studies.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-and-communications-technology-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science-hpe-pathway-to-teaching-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-laws-graduate-entry.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-laws-graduate-entry.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-entrepreneurship-games-design-and-simulation.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-screen-media-arts-and-production.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-entrepreneurship-games-design-and-simulation.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-psychology-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-interpreting-and-translation.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-psychology-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-psychology-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-socialscience.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-music.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science-sport-and-exercise-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-sustainable-agriculture-and-food-security.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-sustainable-agriculture-and-food-security.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-policing.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-policing.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-sustainable-agriculture-and-food-security.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-zoology.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-biological-sciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-industrial-design.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-computer-science-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-medical-science-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-industrial-design.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-zoology.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-computer-science-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-health-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-zoology.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-industrial-design.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-computer-science-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-zoology.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-traditional-chinese-medicine.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-accounting.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-accounting.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-languages-and-linguistics.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-accounting.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-laws-non-graduate-entry.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-data-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-accounting.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-laws-non-graduate-entry.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-criminology.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-criminology.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-computer-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-natural-science-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-tourism-management.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-advanced-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-accounting.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-accounting.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-accounting.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-accounting.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-zoology.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-accounting.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-computer-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-accounting.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-natural-science-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-accounting.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-tourism-management.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-accounting.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-zoology.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-computer-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-natural-science-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-tourism-management.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-design-visual-communication.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-community-welfare.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-community-welfare.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-occupational-therapy.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-social-science-heritage-and-tourism.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-social-science-heritage-and-tourism.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-nutritionandfoodsciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-nursing.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-natural-science-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-creative-industries.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-social-science-psychology.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-tourism-management.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-social-science-psychology.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-social-science-psychology.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-chemistry.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-social-science-psychology.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-chemistry.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-pathway-to-teaching-primary-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-nutritionandfoodsciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-creative-industries.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-pathway-to-teaching-primary-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-pathway-to-teaching-primary-secondary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-tourism-management.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-chemistry.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-chemistry.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-business.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-creative-industries.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-nutritionandfoodsciences.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-birth-to-5-birth-to-12.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-chemistry.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-creative-industries.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-chemistry.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-tourism-management.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-creative-industries.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science-forensic-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-advanced-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-advanced-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-creative-industries.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts-pathway-to-teaching-primary.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-tourism-management.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-advanced-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-advanced-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-science.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-information-systems-advanced.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-engineering-honours.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-arts.html",
      "https://www.westernsydney.edu.au/future/study/courses/undergraduate/bachelor-of-podiatric-medicine.html"
    ]
    C =set(C)
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Western Sydney University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.degree_name
        degree_name = response.xpath('//*[@id="wrapper"]/div/div[3]/div/div[1]//div/h1').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #4.duration
        duration = response.xpath("//*[contains(text(),'FULL TIME')]//following-sibling::*").extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        if '3' in duration:
            duration = 3
        elif '4' in duration:
            duration = 4
        else:duration = ''
        # print(duration,response.url)

        #5.degree_overview_en
        degree_overview_en = response.xpath('//*[@id="wrapper"]/div/div[3]/div/div[2]//div[1]/div/div[1]/p').extract()
        degree_overview_en = ''.join(degree_overview_en)
        degree_overview_en = remove_class(degree_overview_en)
        # print(degree_overview_en)
        # if len(degree_overview_en)==0:
        #     print(url)

        #6.start_date
        start_date = response.xpath('//*[@id="wrapper"]/div/div[3]/div/div[2]//div[1]/div/div/div[2]/div/div[2]').extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        start_date = clear_space_str(start_date)
        if 'Start timesQ1January(2018)Q2April(2018)Q3June(2018)Q4September(2018)' in start_date:
            start_date = '1,4,6,9'
        elif 'Start timesAutumnMarch(2018)SpringJuly(2018)' in start_date:
            start_date = '3,7'
        elif 'Start timesQ1(2018)Q2(2018)Q3(2018)Q4(2018)' in start_date:
            start_date = ''
        elif 'Start timesAutumnFebruary(2018)SpringJuly(2018)' in start_date:
            start_date = '2,7'
        elif 'Start timesAutumnMarch(2018)' in start_date:
            start_date = '3'
        elif 'Start times1HJanuary(2018)2HJune(2018)' in start_date:
            start_date = '1,6'
        elif 'Start times1HJanuary(2018)SpringJuly(2018)' in start_date:
            start_date = '1,7'
        elif 'Start timesQ3June(2018)Q4September(2018)' in start_date:
            start_date = '6,9'
        elif 'Start timesQ2April(2018)Q3June(2018)Q4September(2018)' in start_date:
            start_date = '4,6,9'
        elif 'Start timesSpringJuly(2018)' in start_date:
            start_date = '7'
        else:start_date = ''
        # print(start_date)

        #7.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'Fee')]//..").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #8.tuition_fee_pre
        tuition_fee_pre = 'AU$'

        #9.apply_pre
        apply_pre = 'AU$'

        #10.location
        location = response.xpath('//div/a/div/div/h3').extract()
        location = ','.join(location)
        location = remove_tags(location)
        location = clear_space_str(location)
        # print(location)

        #11.career_en
        career_en = response.xpath("//*[contains(text(),'Your career')]/../following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #12.degree_type
        degree_type = 1

        #13.modules_en
        modules_en_url = response.xpath("//h3[contains(text(),'Course structure')]/../../following-sibling::*//@href").extract()
        modules_en_url = ''.join(modules_en_url)
        if len(modules_en_url)!=0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            try:
                data = requests.get(modules_en_url, headers=headers)
                response_modules_en = etree.HTML(data.text)
                # print(response_modules_en)
                modules_en = response_modules_en.xpath('//*[@id="hbcontent"]/table//td/span')
                doc = ""
                if len(modules_en) > 0:
                    for a in modules_en:
                        doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                        doc = remove_class(doc)
                        modules_en = doc
                else:
                    modules_en = None
            except:
                modules_en = None
        else:modules_en= None
        # print(modules_en)

        #14.apply_fee
        apply_fee = 68

        #15.programme_en
        programme_en = degree_name.replace('Bachelor of ','')
        if 'Planning (Pathway to Master of Urban Management and Planning)' in programme_en:
            programme_en = programme_en
        elif 'Laws (Non-graduate entry)' in programme_en:
            programme_en = programme_en
        elif '(Advanced)' in programme_en:
            programme_en = programme_en
        elif 'Health Science (HPE) - Pathway to Teaching (Secondary)' in programme_en:
            programme_en = programme_en
        elif '(Honours)' in programme_en:
            programme_en = programme_en
        elif '(Graduate Entry)' in programme_en:
            programme_en = programme_en
        elif 'Arts (with a key program in Psychology)' in programme_en:
            programme_en = programme_en

        elif '(' in programme_en:
            programme_en = re.findall(r'\((.*)\)',programme_en)[0]
        else:programme_en = programme_en
        # print(programme_en)

        #16.ielts 17181920 #21.toefl 22232425
        ielts = 6.5
        ielts_r = 6
        ielts_w = 6
        ielts_s = 6
        ielts_l = 6
        toefl = 82
        toefl_w = 21
        toefl_s = 18
        toefl_r = 13
        toefl_l = 13


        #26.average_score
        average_score = 70

        #27.rntry_requirements_en
        modules_en_url = response.xpath('//*[@id="wrapper"]/div/div[3]/div/div[5]/div/div/div/div/div[2]/div/p/a//@href').extract()
        modules_en_url = ''.join(modules_en_url)
        if len(modules_en_url) != 0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data2 = requests.get(modules_en_url, headers=headers)
            response_rntry_requirements_en = etree.HTML(data2.text)
            # print(response_modules_en)
            rntry_requirements_en = response_rntry_requirements_en.xpath("//span[contains(text(),'Admission')]/../following-sibling::p[position()<5]//text()")
            rntry_requirements_en = ' '.join(rntry_requirements_en)
            rntry_requirements_en = '<p>' + rntry_requirements_en + '</p>'
        else:rntry_requirements_en = 'N/A'
        # print(rntry_requirements_en,modules_en_url)

        #28.apply_documents_en
        apply_documents_en = '高中毕业证/在读证明 高中成绩单 语言成绩 护照 高考成绩单'

        #29.apply_desc_en
        apply_desc_en = '<p>International students can apply direct to Western Sydney University.  Apply early! As a guide you should apply by 15th November for courses commencing in the Autumn Session (February/March) ‘and by 15th May for courses commencing in the Spring Session (July/August). Apply Online For a fast and efficient service apply online  (opens in new window) . Apply via an agent You may submit all completed forms and certified documents through an authorised agent representative of the University.</p>'

        #30.overview_en
        overview_en = '1'
        # print(overview_en)

        item['university'] = university
        item['url'] = url
        item['degree_name'] = degree_name
        item['duration'] = duration
        item['degree_overview_en'] = degree_overview_en
        item['start_date'] = start_date
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_pre'] = apply_pre
        item['location'] = location
        item['career_en'] = career_en
        item['degree_type'] = degree_type
        item['modules_en'] = modules_en
        item['apply_fee'] = apply_fee
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['toefl_l'] = toefl_l
        item['toefl_s'] = toefl_s
        item['average_score'] = average_score
        item['rntry_requirements_en'] = rntry_requirements_en
        item['apply_documents_en'] = apply_documents_en
        item['apply_desc_en'] = apply_desc_en

        major = response.xpath("//*[contains(text(),'Choose from 4 specialisations')]//following-sibling::option").extract()
        if len(major) > 0:
            for m in range(len(major)):
                major_l = response.xpath("//*[contains(text(),'Choose from 4 specialisations')]//following-sibling::option[" + str(m+1) + "]//text()").extract()[0]
                major_l = major_l.title()
                overview_en_l = response.xpath("//*[contains(text(),'Choose from 4 specialisations')]/../../following-sibling::div/div[" + str(m+2) + "]").extract()[0]
                item['programme_en'] = major_l
                item['overview_en'] = overview_en_l
                yield item
        else:
            item['programme_en'] = programme_en
            item['overview_en'] = overview_en
            yield item