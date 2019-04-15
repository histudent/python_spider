# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/23 9:17'
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
from lxml import etree
import requests
class RoyalHollowayUniversityofLondonSpider(scrapy.Spider):
    name = 'RoyalHollowayUniversityofLondon_u'
    allowed_domains = ['royalholloway.ac.uk/']
    start_urls = []
    C= [
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-and-philosophy/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/management-with-corporate-responsibility/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/law/law-with-a-year-in-industry/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-with-international-film/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-and-american-literature/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/electronic-engineering/electronic-engineering-with-a-year-in-industry-beng/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/comparative-literature-and-culture-with-philosophy/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/drama-theatre-and-dance/drama-and-theatre-studies/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-and-music/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/psychology/applied-psychology/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-and-econometrics-with-a-year-in-business/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/financial-and-business-economics-with-a-year-in-business/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/comparative-literature-and-culture-and-philosophy/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/physics/physics-with-music/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/business-and-management/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-and-mathematics-with-a-year-in-business/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-with-philosophy/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/law/criminology-and-psychology-with-a-year-in-industry/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-and-english/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/politics-and-international-relations/european-and-international-studies-italian/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/earth-sciences/environmental-geoscience-with-a-year-of-international-study/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/management-with-marketing-with-a-year-in-business/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/physics/physics-with-particle-physics-msci/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-with-german/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-with-translation-studies/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-and-classical-studies/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-with-italian/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/medical-biochemistry/",
        "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/translation-studies-with-history-of-art-and-visual-culture-with-a-language-year-abroad/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/management-with-human-resources/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-software-engineering/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/earth-sciences/environmental-geoscience-with-a-year-in-industry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/drama-theatre-and-dance/drama-and-creative-writing/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/law/law-with-politics-with-a-year-in-industry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/translation-studies-and-comparative-literature-and-culture-with-a-language-year-abroad/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/biology/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-and-comparative-literature-and-culture/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/finance-and-mathematics-with-a-year-in-business/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/law/law-with-sociology-with-a-year-in-industry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-and-history/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/law/criminology-and-sociology/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/psychology/psychology-clinical-and-cognitive-neuroscience/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-and-creative-writing/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-and-translation-studies/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/music/music-with-italian/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/earth-sciences/geoscience-with-a-year-of-international-study/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/drama-theatre-and-dance/drama-and-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/media-arts/digital-media-culture-and-technology-ba/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/media-arts/digital-media-culture-and-technology-bsc/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/psychology/psychology-msci/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/music/music/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/geography/physical-geography/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/politics-and-international-relations/politics-with-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/financial-and-business-economics/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-artificial-intelligence-with-a-year-in-industry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/mathematics/mathematical-studies/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/politics-and-international-relations/politics-and-law/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/physics/theoretical-physics-msci/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/physics/astrophysics-bsc/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-software-engineering-msci/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/history/history-and-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/history/history-and-music/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/translation-studies-and-history-of-art-and-visual-culture/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-artificial-intelligence/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/translation-studies-with-history-of-art-and-visual-culture/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/liberal-arts/liberal-arts/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/comparative-literature-and-culture-and-drama/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-with-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-with-political-studies-with-a-year-in-business/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/translation-studies/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-and-management/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/law/law-with-sociology/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/psychology/psychology/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/drama-theatre-and-dance/drama-with-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/mathematics/mathematics-with-management/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/management-with-international-business/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/finance-and-mathematics/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/history/modern-and-contemporary-history/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-and-film-studies/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/earth-sciences/environmental-geology/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-and-drama/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/comparative-literature-and-culture-with-history-of-art-and-visual-culture/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-software-engineering-with-a-year-in-industry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/earth-sciences/geology/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/electronic-engineering/electronic-engineering-meng/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/classics/ancient-and-medieval-history/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/music/music-with-spanish/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/mathematics/mathematics-with-german/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-and-management/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/law/law-with-criminology/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/electronic-engineering/music-technology/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/philosophy/philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-artificial-intelligence-with-a-year-in-industry-msci/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/mathematics/mathematics-and-music/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/earth-sciences/geoscience-with-a-year-in-industry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/classics/classics-and-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-politics-and-international-relations-with-a-year-in-business/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/ecology-and-conservation/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/mathematics/mathematics-with-spanish/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/media-arts/video-games-art-and-design/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/earth-sciences/environmental-geoscience/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/law/law-with-politics/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/physics/experimental-physics-msci/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/physics/astrophysics-msci/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/classics/classics/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/politics-and-international-relations/politics-and-international-relations-and-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-information-security-with-a-year-in-industry-msci/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/electronic-engineering/computer-systems-engineering-meng/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/electronic-engineering/electronic-engineering-with-a-year-in-industry-meng/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/mathematics/mathematics-and-physics-msci/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/business-and-management-with-a-year-in-business/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/physics/physics-with-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/classics/classical-studies-with-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/classics/classical-archaeology-and-ancient-history/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-politics-and-international-relations/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-and-history-of-art-and-visual-culture/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-information-security-with-a-year-in-industry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/politics-and-international-relations/politics-and-international-relations/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-information-security-msci/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/translation-studies-and-comparative-literature-and-culture/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-and-latin/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/politics-and-international-relations/politics/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-and-management-with-a-year-in-business/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/mathematics/mathematics-with-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/music/music-with-political-studies/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/music/music-with-french/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/politics-and-international-relations/international-relations/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/management-with-corporate-responsibility-with-a-year-in-business/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-with-spanish/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/geography/human-geography/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/mathematics/mathematics-with-italian/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/law/law-with-international-relations-with-a-year-in-industry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-and-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-and-drama/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/electronic-engineering/music-technology-with-a-year-in-industry-meng/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/classics/greek/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/geography/geography-bsc/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/physics/theoretical-physics-bsc/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/physics/experimental-physics-bsc/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/media-arts/film-studies/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/psychology/psychology-clinical-psychology-and-mental-health/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/comparative-literature-and-culture-with-international-film/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/mathematics/mathematics-msci/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/comparative-literature-and-culture-and-english/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/drama-theatre-and-dance/drama-with-film/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-information-security/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/politics-and-international-relations/european-and-international-studies-spanish/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/law/law-with-criminology-with-a-year-in-industry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-and-classical-studies/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-and-econometrics/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/geography/geography-ba/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/electronic-engineering/computer-systems-engineering-with-a-year-in-industry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/physics/physics-with-particle-physics-bsc/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-with-political-studies/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/classics/ancient-history-and-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/politics-philosophy-and-economics/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/classics/classical-studies-and-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/accounting-and-finance-with-a-year-in-business/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-with-a-year-in-business/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/politics-and-international-relations/european-and-international-studies-german/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/management-with-international-business-with-a-year-in-business/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/law/criminology-and-psychology/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/electronic-engineering/computer-systems-engineering-with-a-year-in-industry-meng/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-with-a-year-in-industry-msci/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/law/criminology-and-sociology-with-a-year-in-industry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/classics/classical-studies-and-drama/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/translation-studies-and-history-of-art-and-visual-culture-with-a-language-year-abroad/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/translation-studies-with-international-film/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-with-history-of-art-and-visual-culture/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/earth-sciences/petroleum-geology/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-software-engineering-with-a-year-in-industry-msci/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/classics/ancient-history/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/psychology/psychology-development-and-developmental-disorders/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/classics/latin/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/classics/classics-with-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/earth-sciences/environmental-geology-with-a-year-in-industry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-with-music/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-artificial-intelligence-msci/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/management-with-digital-innovation-with-a-year-in-business/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/translation-studies-with-international-film-with-a-language-year-abroad/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/mathematics/mathematics-with-french/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/media-arts/film-television-and-digital-production/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/electronic-engineering/music-technology-with-a-year-in-industry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/mathematics/mathematics-and-physics/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-and-greek/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/liberal-arts/liberal-arts-with-a-language-year-abroad/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/biomedical-sciences/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/electronic-engineering/music-technology-meng/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/mathematics/mathematics/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-with-mathematics/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/music/music-and-english/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-and-latin/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-msci/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/translation-studies-with-a-language-year-abroad/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/classics/ancient-history-with-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/management-with-marketing/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/english/american-literature-and-creative-writing/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-with-international-relations/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/liberal-arts/liberal-arts-with-an-international-year/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/management-with-accounting/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-and-mathematics/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/media-arts/film-studies-with-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/zoology/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/management-with-human-resources-with-a-year-in-business/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/history/history-politics-and-international-relations/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/music/music-and-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/management-with-accounting-with-a-year-in-business/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/electronic-engineering/electronic-engineering/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/molecular-biology/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/electronic-engineering/computer-systems-engineering/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/management-with-mathematics/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/classics/classical-studies/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/classics/classical-studies-and-comparative-literature-and-culture/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/accounting-and-finance/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/management-with-digital-innovation/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/comparative-literature-and-culture/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/politics-and-international-relations/politics-and-law-with-a-year-in-industry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/law/law/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-with-a-year-in-industry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/management-with-entrepreneurship-with-a-year-in-business/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/earth-sciences/digital-geosciences/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/earth-sciences/geoscience/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/biological-sciences/biochemistry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/history/history/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/mathematics/mathematics-and-management/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/earth-sciences/geology-with-a-year-in-industry/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/physics/physics-bsc/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/mathematics/mathematics-with-statistics/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/drama-theatre-and-dance/drama-and-music/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/economics/economics-with-french/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/modern-languages-literatures-and-cultures/modern-languages-with-music/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/computer-science/computer-science-and-mathematics/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/law/law-with-international-relations/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/english/english-and-history/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/politics-and-international-relations/european-and-international-studies-french/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/music/music-with-german/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/physics/physics-msci/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/drama-theatre-and-dance/drama-and-dance/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/music/music-with-philosophy/",
    "https://www.royalholloway.ac.uk/studying-here/undergraduate/management/management-with-entrepreneurship/"
    ]
    # print(len(C))
    C = set(C)
    # print(len(C))
    for i in C:
        start_urls.append(i)

    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Royal Holloway University of London'
        # print(university)

        #2.department
        try:
            department = response.xpath('//*[@id="main"]/aside/div[2]/a/div[2]/span[2]').extract()
            department = ''.join(department)
            department = remove_tags(department)
            # print(department)
        except:
            department = 'N/A'

        #3.location
        location = 'London'

        #4.degree_type
        degree_type = 1

        #5.degree_name
        try:
            degree_name = response.xpath('/html/body/div[1]/main/div[1]//span').extract()
            degree_name = ''.join(degree_name)
            degree_name = remove_tags(degree_name)
        except:
            degree_name = 'N/A'
        # print(degree_name)
        # if len(degree_name)==0:
        #     print(response.url)

        #6.programme_en
        try:
            programme_en = response.xpath('/html/body/div[1]/main/div[1]//h2').extract()
            programme_en = ''.join(programme_en)
            programme_en = remove_tags(programme_en)
            programme_en = clear_space_str(programme_en)
        except:
            programme_en = ''
        # print(programme_en)

        #7.overview_en
        try:
            overview_en = response.xpath('//*[@id="main"]/article/p').extract()
            overview_en = ''.join(overview_en)
            overview_en = remove_class(overview_en)
            overview_en = clear_space_str(overview_en)

        except:
            overview_en = ''
        # print(overview_en)

        #8.duration
        try:
            duration = response.xpath('/html/body/div[1]/main/div[2]/div/ul/li[2]/span').extract()
            duration = ''.join(duration)
            duration = re.findall('\d',duration)[0]
        except:
            duration = ''
        # print(duration)

        #9.duration_per
        duration_per = 1


        #10.modules_en
        try:
            modules_en = response.xpath("//div[contains(@class,'courseModulesRemoveBullets')]").extract()
            modules_en = ''.join(modules_en).replace('<button','<p').replace('</button>','</p>')
            modules_en = remove_class(modules_en)
        except:
            modules_en = None
        # print(modules_en)
        # if len(modules_en)==0:
        #     print(response.url)

        #11.assessment_en
        try:
            assessment_en = response.xpath('//*[@id="accordionItem2"]/div').extract()
            assessment_en = ''.join(assessment_en)
            assessment_en = remove_class(assessment_en)
            assessment_en = clear_space_str(assessment_en)
        except:
            assessment_en = ''
        # print(assessment_en)

        #12.career_en
        try:
            career_en = response.xpath('//*[@id="accordionItem4"]/div').extract()
            career_en = ''.join(career_en)
            career_en = remove_class(career_en)
            career_en = clear_space_str(career_en)
        except:
            career_en = ''
        # print(career_en)

        #13.tuition_fee
        tuition_fee = response.xpath('//*[@id="accordionItem5"]/div/p[2]').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        try:
            tuition_fee = re.findall('\£(\d+)', tuition_fee)[0]
        except:
            tuition_fee = None
        # print(tuition_fee,response.url)
        if  tuition_fee == None:
            tuition_fee = response.xpath('//*[@id="accordionItem5"]/div/p[3]').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        try:
            tuition_fee = re.findall('\£(\d+)', tuition_fee)[0]
        except:
            tuition_fee = tuition_fee
        # print(tuition_fee,response.url)

        #14.tuition_fee_pre
        tuition_fee_pre = '£'

        #15.ucascode
        ucascode = response.xpath('/html/body/div[1]/main/div[2]/div/ul/li[1]/span').extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode)
        # print(ucascode)

        #16.ielts 17181920
        ielts_list = response.xpath('//*[@id="accordionItem3"]/div/ul/li[1]').extract()
        ielts_list = ''.join(ielts_list)
        ielts = re.findall(r'[567]\.\d',ielts_list)
        if len(ielts)==3:
            a = ielts[0]
            b = ielts[1]
            c = ielts[2]
            ielts = a
            ielts_w = b
            ielts_l = c
            ielts_s = c
            ielts_r = c
        elif len(ielts)==2:
            a = ielts[0]
            b = ielts[1]
            ielts = a
            ielts_w = b
            ielts_l = b
            ielts_s = b
            ielts_r = b
        else:
            ielts = None
            ielts_w = None
            ielts_l =None
            ielts_s = None
            ielts_r = None
        # print(ielts)


        #21.alevel
        alevel = response.xpath('//*[@id="accordionItem3"]/div/h4[1]').extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel)
        # print(alevel)

        #22.url
        url = response.url
        # print(url)

        #23.other
        other = 'https://intranet.royalholloway.ac.uk/international/documents/pdf/internationalstudentsupport/tier-4-checklist-outside-uk.pdf'

        #24.apply_proces_en
        apply_proces_en = 'https://admissions.royalholloway.ac.uk/AP/Login.aspx'

        #25.require_chinese_en
        # level = response.xpath("//*[contains(text(),'International')]//following-sibling::*//@data-grade").extract()
        # level = ''.join(level)
        # level = remove_tags(level)
        # # print(level)
        # chi_url = 'https://www.royalholloway.ac.uk/umbraco/api/course/GetInternationalEntryRequirement?grade='+level+'&country=china'
        # data = requests.get(chi_url)
        # response1 = etree.HTML(data.text)
        # require_chinese_en = response1.xpath('//text()')
        # require_chinese_en = ''.join(require_chinese_en)
        # require_chinese_en = '<p>'+require_chinese_en+'</p>'
        # print(require_chinese_en)

        #26.ib
        ib = response.xpath("//*[contains(text(),'International Baccalaureate')]//@value").extract()
        ib = ''.join(ib)
        ib = remove_tags(ib)
        # print(ib)




        item['ucascode'] = ucascode
        item['alevel'] = alevel
        item['ib'] = ib
        item['other'] = other
        item['apply_proces_en'] =apply_proces_en
        item['university'] = university
        item['department'] = department
        item['location'] = location
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['programme_en'] = programme_en
        item['overview_en'] = overview_en
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['ielts'] = ielts
        item['ielts_w'] = ielts_w
        item['ielts_r'] = ielts_r
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        # item['require_chinese_en'] = require_chinese_en
        item['url'] = url
        yield item