# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/26 14:25'
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
from scrapySchool_England.clearSpace import  clear_space_str
from scrapySchool_England.translate_date import  tracslateDate
from scrapySchool_England.translate_date import tracslateDate
from lxml import etree
import  requests
class UniversityofEastAngliaSpider(scrapy.Spider):
    name = 'UniversityofEastAnglia_u'
    allowed_domains = ['uea.ac.uk/']
    start_urls = []
    C = [
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-sports-development-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-translation-media-and-modern-language-double-honours',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-in-geography-and-international-development-with-overseas-placement',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-translation-and-interpreting-with-modern-languages-double-honours',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-translation-media-and-modern-language-french-or-spanish-3-years',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-translation-media-and-modern-language',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-actuarial-sciences',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-accounting-and-management',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-accounting-and-finance',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-actuarial-sciences-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-accounting-and-management-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-adult-nursing',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-accounting-and-finance-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-american-history',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-american-studies',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-american-studies-3-years',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-american-literature-with-creative-writing',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-archaeology-anthropology-and-art-history',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-archaeology-anthropology-and-art-history-year-in-australasia-or-north-america',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-american-studies-with-a-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-biochemistry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-american-and-english-literature',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-biochemistry-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mcsi-biochemistry-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mcsi-biochemistry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-biological-sciences-with-education',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/msci-biological-sciences',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-biological-sciences',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-biological-sciences-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-biological-sciences-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-biomedicine',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/biological-sciences-with-a-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-business-economics-with-a-placement-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-business-finance-and-economics-with-a-placement-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-business-economics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-business-finance-and-economics-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-business-economics-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-business-finance-and-economics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-business-finance-and-management',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-business-finance-and-management-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-business-information-systems',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-business-information-systems-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-business-management-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-chemical-physics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mchem-chemical-physics-with-a-year-in-north-america',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mchem-chemical-physics-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-business-management',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-chemistry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mchem-chemistry-with-a-year-in-north-america',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-children-s-nursing',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-climate-change',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/chemistry-with-a-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mchem-chemistry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mchem-chemistry-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-chemistry-with-education',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-computer-graphics-imaging-and-multimedia',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-climate-change-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-computing-science-with-imaging-and-multimedia-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-cognitive-psychology',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-cognitive-psychology-with-placement-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-cognitive-psychology-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/msci-climate-change',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/beng-computer-systems-engineering-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-computing-science-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-computing-science',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mcomp-computing-science',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-computing-sciences-with-education',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/beng-computer-systems-engineering',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-applied-computing-science-with-a-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mcomp-computing-science-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-developmental-psychology',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-developmental-psychology-with-placement-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-developmental-psychology-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-ecology',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-ecology-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-ecology-and-conservation',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-culture-literature-and-politics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-drama',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-ecology-and-conservation-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-economics-and-finance',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/msci-economics-and-finance',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-economics-and-finance-with-a-placement-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-economics-with-accountancy',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-economics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-economics-with-accountancy-with-a-placement-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-economics-with-accountancy-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-economics-with-a-placement-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-economics-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-education',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-education-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/energy-engineering-beng',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/beng-energy-engineering-with-environmental-management',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/energy-engineering-meng',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/engineering-meng',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/engineering-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/engineering-beng',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-english-literature-and-drama',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-english-literature-and-philosophy',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-english-literature',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-english-literature-with-a-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-environmental-sciences',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/msci-environmental-sciences',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-english-literature-with-creative-writing',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-english-and-american-literature',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/msci-environmental-sciences-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-environmental-sciences-with-education',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/environmental-sciences-with-a-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-environmental-sciences-and-international-development',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-geography-with-education',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-film-and-television-studies',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-film-and-television-studies-with-a-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-environmental-sciences-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-film-and-english-studies',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-geography',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-geography',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-geography-and-international-development',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-geography-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-geography-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-geology-with-geography',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/msci-geology-with-geography',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-geography-and-international-development-with-overseas-experience-unu1ll7v303',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-geography-and-international-development-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/msci-geology-with-geography-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-geology-with-geography-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-geophysics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/msci-geophysics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/msci-geophysics-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-geophysics-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-film-and-history',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-history',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-history-with-a-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-history-and-history-of-art',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-history-of-art',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-history-of-art-witha-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-history-of-art-and-literature',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-history-of-art-with-gallery-and-museum-studies',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-history-of-art-with-a-year-in-australasia-or-north-america',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-intercultural-communication-with-business-management',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-history-and-politics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-in-international-development-and-the-environment-with-overseas-experience',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development-and-the-environment-with-overseas-placement',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-international-development-and-the-environment-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development-with-anthropology',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-intercultural-communication-with-business-management-with-a-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development-with-anthropology-with-overseas-experience',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-international-development-with-environment',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development-with-economics-with-overseas-placement',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development-with-anthropology-with-overseas-placement',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development-with-anthropology-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development-with-economics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development-with-economics-with-overseas-experience',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development-with-economics-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development-with-overseas-experience',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development-with-overseas-placement',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development-with-politics-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development-with-politics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development-with-politics-with-overseas-experience',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-development-with-politics-with-overseas-placement',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-relations',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-relations-and-modern-languages',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-relations-and-modern-history',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-international-relations-and-politics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-learning-disabilities-nursing',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/llb-law',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/llb-law-with-american-law',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/llb-law-with-european-legal-systems',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-mathematics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-mathematics-with-education',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-marketing-and-management-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-marketing-and-management',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mmath-master-of-mathematics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mmath-master-of-mathematics-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-literature-and-history',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-mathematics-with-business',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-mathematics-with-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-mathematics-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-media-studies',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-media-and-international-development',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/media-and-international-development-with-overseas-experience',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-media-and-international-development-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mbbs-medicine',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-media-and-international-development-with-overseas-placement',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mbbs-medicine-with-a-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-meteorology-and-oceanography-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-mental-health-nursing',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-meteorology-and-oceanography',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/msci-meteorology-and-oceanography',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/msci-meteorology-and-oceanography-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-midwifery',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-modern-history',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-molecular-biology-and-genetics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-modern-languages-double-honours',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-modern-languages-with-management-studies-double-honours-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-modern-language-french-or-spanish-3-years',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-modern-language',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-modern-language-with-management-studies',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-natural-sciences',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-occupational-therapy',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-paramedic-science',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-pharmacology-and-drug-discovery',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-natural-sciences-with-a-year-in-industry',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-natural-sciences-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mnatsci-natural-sciences',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/msci-pharmacology-and-drug-discovery',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mpharm-pharmacy',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/pharmacy-with-a-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mpharm-pharmacy-with-a-placement-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-philosophy-and-politics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-pharmacology-and-drug-discovery-with-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-philosophy-and-history',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-philosophy',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-philosophy-with-a-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-philosophy-politics-and-economics-with-a-placement-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/philosophy-politics-and-economics-with-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-physical-education',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-physical-activity-and-health',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-physical-education-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-physical-activity-and-health-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-physical-education',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-philosophy-politics-and-economics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-physiotherapy',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-physical-education-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-physical-education-sport-and-health',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-physical-education-sport-and-health-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-physics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/mphy',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-physics-with-education',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-physics-with-a-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-politics-and-economics-with-a-placement-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-psychology',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-psychology-with-placement-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-politics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-politics-and-economics',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-politics-and-economics-with-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-politics-and-media-studies',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-politics-with-a-foundation-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-psychology-with-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-social-psychology',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-social-psychology-with-placement-year',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-social-psychology-with-a-year-abroad',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-social-work',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-society-culture-and-media',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/ba-scriptwriting-and-performance',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-speech-and-language-therapy',
        'https://www2.uea.ac.uk/study/undergraduate/degree/detail/bsc-sport-development'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of East Anglia'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en_a = response.xpath('//*[@id="course-title"]/div/div/div/h1').extract()
        programme_en_a = ''.join(programme_en_a)
        programme_en_a = remove_tags(programme_en_a)
        # print(programme_en)
        programme_en = programme_en_a.split()[1:]
        programme_en = ' '.join(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type=1

        #5.degree_name
        # degree_name = programme_en_a.split()[0]
        # programme_en = programme_en.replace(degree_name,'').strip()
        # print(degree_name)

        #6.ucascode
        ucascode = response.xpath('//*[@id="course-spec-right"]/dd[1]').extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode)
        # print(ucascode)

        #7.department
        department = response.xpath('//*[@id="faculty-and-school"]/li[1]/a').extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #8.overview_en
        overview_en = response.xpath('//*[@id="course-about"]/div/div[2]').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #9.modules_en
        try:
            modules_en1 = response.xpath("//*[contains(@id,'module_y_1')]/div/table").extract()
            modules_en1 =''.join(modules_en1)
            modules_en1 = remove_class(modules_en1)
        except:
            modules_en1 = 'N/A'
        modules_en1 = '<h3>year1</h3>' + modules_en1
        try:
            modules_en2 = response.xpath("//*[contains(@id,'module_y_2')]/div/table").extract()
            modules_en2 = ''.join(modules_en2)
            modules_en2 = remove_class(modules_en2)
        except:
            modules_en2 = 'N/A'
        modules_en2 = '<h3>year2</h3>' + modules_en2
        try:
            modules_en3 = response.xpath("//*[contains(@id,'module_y_3')]/div/table").extract()
            modules_en3 = ''.join(modules_en3)
            modules_en3 = remove_class(modules_en3)
        except:
            modules_en3 = 'N/A'
        modules_en3 = '<h3>year3</h3>' + modules_en3
        try:
            modules_en4 = response.xpath("//*[contains(@id,'module_y_4')]/div/table").extract()
            modules_en4 = ''.join(modules_en4)
            modules_en4 = remove_class(modules_en4)
        except:
            modules_en4 = 'N/A'
        modules_en4 = '<h3>year4</h3>' + modules_en4
        modules_en = modules_en1+modules_en2+modules_en3+modules_en4

        # print(modules_en)

        #10.alevel
        alevel = response.xpath('//*[@id="course-spec-right"]/dd[2]/text()').extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel).strip()
        # print(alevel)

        #11.ielts 12131415
        ielts = response.xpath('//*[@id="course-entry-requirements"]').extract()
        ielts = ''.join(ielts)
        ielts = remove_tags(ielts)
        # print(ielts)
        try:
            ielts = re.findall('[567]\.\d',ielts)
        except:
            ielts = None
        # print(ielts)
        if len(ielts)>1:
            a=ielts[0]
            b=ielts[1]
            ielts = a
            ielts_w = b
            ielts_r = b
            ielts_s = b
            ielts_l = b
        else:
            ielts = 6.5
            ielts_w = 6.0
            ielts_r = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
        # print(ielts,ielts_r,ielts_w,ielts_s,ielts_l)

        #16.ib
        try:
            ib= response.xpath("//*[contains(text(),'International Baccalaureate')]//following-sibling::span").extract()[-1]
            ib = remove_tags(ib)
        except:
            ib = ''
        # print(ib)



        #18.tuition_fee_pre
        tuition_fee_pre = '£'

        #19.apply_proces_en
        apply_proces_en = 'http://www.uea.ac.uk/study/postgraduate/apply'

        #20.location
        location = 'Norwich'

        #21.apply_pre
        apply_pre = '£'

        #22.other
        other = 'https://portal.uea.ac.uk/documents/6207125/7154540/Fees+Table+2018-19+-+Overseas+v6-1.pdf/869dace0-fc79-bcce-0aea-5cc0ceb2bc78'

        #23.duration
        # try:
        #     ab = response.xpath("//div[@class='kis-widget']//@data-institution").extract()[0]
        # except:
        #     ab = ''
        # try:
        #     cd = response.xpath("//div[@class='kis-widget']//@data-course").extract()[0]
        # except:
        #     cd = ''
        # if len(ab)!= 0:
        #     duration_url = 'https://widget.unistats.ac.uk/Widget/'+str(ab)+'/'+str(cd)+'/small/en-GB/Full Time'
        # else:duration_url= ''
        # # print(duration_url)
        # if len(duration_url)!=0:
        #     headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        #     data = requests.get(duration_url, headers=headers)
        #     response_duration = etree.HTML(data.text)
        #     duration = response_duration.xpath('//*[@id="kisWidget"]/div[2]/p[1]//text()')
        #     duration = ''.join(duration)
        #     duration =remove_tags(duration)
        #     try:
        #         duration = re.findall(r'\d',duration)[0]
        #     except:
        #         duration = ''
        # else:
        #     duration = ''
        # print(duration)

        #24.tuition_fee
        if 'N323' in ucascode:
            tuition_fee =  15300
        elif 'N324' in ucascode:
            tuition_fee = 15300
        elif 'G390' in ucascode:
            tuition_fee = 15300
        elif 'GN54' in ucascode:
            tuition_fee = 15300
        else:
            depart = response.xpath('//*[@id="faculty-and-school"]/li[2]/a').extract()
            depart = ''.join(depart)
            depart = remove_tags(depart)
            list1 = ['Art, Media and American Studies',
    'Biological Sciences',
    'Chemistry',
    'Computing Sciences',
    'International Development',
    'Economics',
    'Education and Lifelong Learning',
    'Engineering',
    'Environmental Sciences',
    'History',
    'Health Sciences',
    'Law',
    'School Literature, Drama and Creative Writing',
    'Norwich Medical School',
    'Mathematics',
    'Natural Sciences',
    'Norwich Business School',
    'Pharmacy',
    'Politics, Philosophy, Language and Communication Studies Overseas',
    'Psychology']
            listvalue = ['15300',
    '19400',
    '19400',
    '19400',
    '15300',
    '15300',
    '15300',
    '19400',
    '19400',
    '15300',
    '15300',
    '15300',
    '15300',
    '30000',
    '15300',
    '19400',
    '15300',
    '19400',
    '15300',
    '15300']
            dd = {}
            for i in range(len(list1)):
                dd[list1[i]] = listvalue[i]
                # print(dd)
                tuition_fee = dd.get(depart)
        # print(tuition_fee)

        #25.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'Assessment')]//following-sibling::div[1]").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #26.career_en
        # career_en = response.xpath("//*[contains(text(),'Career destinations')]//following-sibling::div[1]").extract()
        # career_en = ''.join(career_en)
        # career_en = remove_class(career_en)
        career_en = response.xpath("//*[contains(text(),'After the course')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)


        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        # item['duration'] = duration
        item['ucascode'] = ucascode
        item['ib'] = ib
        item['alevel'] = alevel
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        # item['degree_name'] = degree_name
        item['department'] = department
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_proces_en'] = apply_proces_en
        item['location'] = location
        item['other'] = other
        yield item