# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.clearSpace import clear_same_s
from scrapySchool_England.middlewares import clear_duration
import requests
from lxml import etree
class UniversityofoxfordSpider(scrapy.Spider):
    name = 'UniversityOfOxford_P'
    allowed_domains = ['ox.ac.uk']
    start_urls = ['https://www.ox.ac.uk/admissions/graduate/courses/courses-a-z-listing?wssl=1']
    start_urlss = ['https://www.ox.ac.uk/admissions/graduate/courses/mphil-international-relations?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-international-health-and-tropical-medicine?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-history-science-medicine-and-technology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-history-science-medicine-and-technology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-greek-andor-roman-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-greek-andor-roman-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-history-art-and-visual-culture?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-greek-andor-latin-languages-and-literature?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-global-health-science-and-epidemiology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-global-and-imperial-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-integrated-immunology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-general-linguistics-and-comparative-philology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-global-governance-and-diplomacy?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-general-linguistics-and-comparative-philology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-greek-andor-latin-languages-and-literature?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mfa-fine-art?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-financial-economics?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-film-aesthetics?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-evidence-based-social-intervention-and-policy-evaluation?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-evidence-based-social-intervention-and-policy-evaluation?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-environmental-change-and-management?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-economic-and-social-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-diplomatic-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-eastern-christian-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-cuneiform-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-development-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-criminology-and-criminal-justice?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-economic-and-social-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-comparative-social-policy?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-computer-science?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-contemporary-chinese-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-comparative-social-policy?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-cognitive-and-evolutionary-anthropology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-classical-armenian-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-classical-archaeology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-clinical-embryology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-buddhist-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-biodiversity-conservation-and-management?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-classical-indian-religion?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-archaeology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-biodiversity-conservation-and-management?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-classical-archaeology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-classical-hebrew-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-archaeological-science?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mth-applied-theology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-bible-interpretation?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-archaeological-science?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-archaeology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-ancient-philosophy?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/bachelor-civil-law?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-applied-linguistics-and-second-language-acquisition?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-african-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-egyptology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-english-1550-1700?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-english-1700-1830?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-english-1900-present?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-english-650-1550?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-english-1830-1914?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-education-comparative-and-international-education?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-economics?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-environmental-change-and-management?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-education-child-development-and-education?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-education-research-design-and-methodology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-english-studies-medieval-period?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-education-higher-education?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-english-and-american-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-economics-development?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-world-literatures-english?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-womens-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-water-science-policy-and-management?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-yiddish-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-water-science-policy-and-management?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-visual-material-and-museum-anthropology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-tibetan-and-himalayan-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-traditional-east-asia?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-theology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-traditional-china?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-theology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-visual-material-and-museum-anthropology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-syriac-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-study-religion?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-theoretical-and-computational-chemistry-stand-alone?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-sociology-demography?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-social-science-internet?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-sociology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-statistical-science?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-slavonic-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-russian-and-east-european-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-social-anthropology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-social-anthropology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-slavonic-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-social-data-science?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-russian-and-east-european-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/master-public-policy?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-radiation-biology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-psychological-research?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-politics-comparative-government?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-politics-european-politics-and-society?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-refugee-and-forced-migration-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-philosophical-theology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-politics-political-theory?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-philosophical-theology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/bphil-philosophy?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-pharmacology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-political-theory-research?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-neuroscience?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-nature-society-and-environmental-governance?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-politics-research?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-nature-society-and-environmental-governance?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-music-performance?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-music-performance?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-music-musicology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-oriental-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-philosophy-physics?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-music-musicology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-modern-south-asian-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-modern-south-asian-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-modern-middle-eastern-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-modern-languages?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-modern-middle-eastern-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-music-composition?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-music-composition?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-modern-languages?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-migration-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-modern-chinese-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-medical-anthropology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-mathematical-and-theoretical-physics?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-mathematical-modelling-and-scientific-computing?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-mathematical-and-computational-finance?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-medical-anthropology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-medieval-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-mathematics-and-foundations-computer-science?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/magister-juris?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mba?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-law-and-finance?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-latin-american-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-late-antique-and-byzantine-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-mathematical-sciences?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-late-antique-and-byzantine-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/oxford-1plus1-mba?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-korean-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-judaism-and-christianity-graeco-roman-world?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-jewish-studies-graeco-roman-period?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-jewish-studies-graeco-roman-period?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-latin-american-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-jewish-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-japanese-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-japanese-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-islamic-studies-and-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-islamic-studies-and-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-islamic-art-and-archaeology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-islamic-art-and-archaeology?wssl=1',]
    start_urlss = set(start_urlss)

    def parse(self, response):
        urls=['https://www.ox.ac.uk/admissions/graduate/courses/bachelor-civil-law?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/bphil-philosophy?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/magister-juris?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/master-public-policy?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mba?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mfa-fine-art?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-archaeology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-biodiversity-conservation-and-management?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-buddhist-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-classical-archaeology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-classical-indian-religion?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-comparative-social-policy?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-cuneiform-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-development-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-eastern-christian-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-economic-and-social-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-economics?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-egyptology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-english-studies-medieval-period?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-environmental-change-and-management?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-evidence-based-social-intervention-and-policy-evaluation?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-general-linguistics-and-comparative-philology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-greek-andor-latin-languages-and-literature?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-greek-andor-roman-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-history-science-medicine-and-technology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-international-relations?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-islamic-art-and-archaeology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-islamic-studies-and-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-japanese-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-jewish-studies-graeco-roman-period?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-judaism-and-christianity-graeco-roman-world?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-late-antique-and-byzantine-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-latin-american-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-medical-anthropology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-modern-chinese-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-modern-languages?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-modern-middle-eastern-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-modern-south-asian-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-music-composition?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-music-musicology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-music-performance?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-nature-society-and-environmental-governance?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-philosophical-theology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-politics-comparative-government?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-politics-european-politics-and-society?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-politics-political-theory?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-russian-and-east-european-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-slavonic-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-social-anthropology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-sociology-demography?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-theology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-tibetan-and-himalayan-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-traditional-east-asia?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-visual-material-and-museum-anthropology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mphil-water-science-policy-and-management?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-african-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-applied-linguistics-and-second-language-acquisition?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-archaeological-science?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-biodiversity-conservation-and-management?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-clinical-embryology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-cognitive-and-evolutionary-anthropology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-comparative-social-policy?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-computer-science?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-contemporary-chinese-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-criminology-and-criminal-justice?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-economic-and-social-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-economics-development?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-education-child-development-and-education?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-education-comparative-and-international-education?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-education-higher-education?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-education-research-design-and-methodology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-environmental-change-and-management?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-evidence-based-social-intervention-and-policy-evaluation?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-financial-economics?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-global-governance-and-diplomacy?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-global-health-science-and-epidemiology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-history-science-medicine-and-technology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-integrated-immunology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-international-health-and-tropical-medicine?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-japanese-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-latin-american-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-law-and-finance?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-mathematical-and-computational-finance?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-mathematical-and-theoretical-physics?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-mathematical-modelling-and-scientific-computing?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-mathematical-sciences?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-mathematics-and-foundations-computer-science?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-medical-anthropology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-migration-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-modern-middle-eastern-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-modern-south-asian-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-nature-society-and-environmental-governance?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-neuroscience?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-pharmacology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-political-theory-research?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-politics-research?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-psychological-research?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-radiation-biology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-refugee-and-forced-migration-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-russian-and-east-european-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-social-anthropology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-social-data-science?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-social-science-internet?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-sociology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-statistical-science?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-theoretical-and-computational-chemistry-stand-alone?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-visual-material-and-museum-anthropology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/msc-water-science-policy-and-management?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-ancient-philosophy?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-archaeological-science?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-archaeology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-bible-interpretation?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-classical-archaeology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-classical-armenian-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-classical-hebrew-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-diplomatic-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-english-1550-1700?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-english-1700-1830?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-english-1830-1914?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-english-1900-present?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-english-650-1550?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-english-and-american-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-film-aesthetics?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-general-linguistics-and-comparative-philology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-global-and-imperial-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-greek-andor-latin-languages-and-literature?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-greek-andor-roman-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-history-art-and-visual-culture?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-islamic-art-and-archaeology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-islamic-studies-and-history?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-jewish-studies-graeco-roman-period?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-jewish-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-korean-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-late-antique-and-byzantine-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-medieval-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-modern-languages?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-music-composition?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-music-musicology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-music-performance?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-oriental-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-philosophical-theology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-philosophy-physics?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-slavonic-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-study-religion?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-syriac-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-theology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-traditional-china?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-womens-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-world-literatures-english?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mst-yiddish-studies?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/mth-applied-theology?wssl=1',
'https://www.ox.ac.uk/admissions/graduate/courses/oxford-1plus1-mba?wssl=1',]
        for u in urls:
            yield scrapy.Request(url=u,callback=self.pars,meta={'url':u})
    def pars(self,response):
        item=get_item1(ScrapyschoolEnglandItem1)
        item['url']=response.meta['url']
        item['university']="University of Oxford"
        print(response.url)
        tuition=response.xpath('//td[contains(text(),"versea")]/following-sibling::td[contains(text(),"£")]/text()').extract()
        print(tuition)
        if tuition!=[]:
            tuition=tuition[0]
            tui=re.findall('\d{2}\,\d{3}',tuition)
            item['tuition_fee']=''.join(tui).replace(',','').strip()
            print(item['tuition_fee'])
            yield item
    def parsesss(self, response):
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "University of Oxford"
        item['url'] = response.url
        coursePageUrl=response.xpath('//a[contains(text(),"Course webpage")]/@href').extract()
        # print(coursePageUrl,response.url)
        #//dd[@id="panel-structure"]/div
        if coursePageUrl!=[]:
            mod=[]
            modRes=etree.HTML(requests.get(coursePageUrl[0]).content)
            modules=modRes.xpath('//dd[@id="panel-structure"]/div|//h2/strong[contains(text()," in ")]/../following-sibling::p')
            for mo in modules:
                mod+=etree.tostring(mo,method='html',encoding='unicode')
            item['modules_en']=remove_class(mod)
            yield item
    def parsess(self, response):
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "University of Oxford"
        item['url'] = response.url
        overview_pre=response.xpath('//div[@class="field field-name-field-intro field-type-text-long field-label-hidden"]//text()').extract()
        overview=response.xpath('//div[@id="content-tab"]/child::*').extract()
        overview_spilt=response.xpath('//div[@id="content-tab"]/child::h2[1]').extract()
        overview=overview[0:overview.index(overview_spilt[0])]
        item['overview_en']='<p>'+''.join(overview_pre).strip()+'</p>'+remove_class(overview)
        career=response.xpath('//h2[contains(text(),"Graduate destinations")]/self::*|//h2[contains(text(),"Graduate destinations")]/following-sibling::*').extract()
        career_spilt=response.xpath('//h2[contains(text(),"Graduate destinations")]/following-sibling::h2[1]').extract()
        if career_spilt!=[]:
            career=career[0:career.index(career_spilt[0])]
        item['career_en']=remove_class(career)
        yield item
    def parses(self,response):
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "University of Oxford"
        item['url'] = response.url
        item["degree_type"] = 2
        item['location'] = 'Oxford'
        # item['teach_time'] = response.meta['mode']

        # durations=response.meta['duration']
        # duration_pre=re.findall('[a-zA-Z]*',durations)
        # duration_pre=''.join(duration_pre)
        # duration=re.findall('\d*-?\d*',durations)
        # duration=''.join(duration)
        # if '-' in duration:
        #     duration=duration.split('-')[0]
        #
        # if duration_pre=='months':
        #     duration_pre=3
        # elif duration_pre=='year':
        #     duration_pre=1
        # else:
        #     duration_pre=1
        # duration=clear_duration(durations)
        # item['programme_en'] = response.meta['programme'].strip()
        # item['degree_type'] = 2
        # item['degree_name'] = response.meta['degree_type'].strip()
        # item['duration'] = duration['duration']
        # item['duration_per'] = duration['duration_per']
        # item['department'] = response.meta['department'].strip()

        overview=response.xpath('//div[@id="content-tab"]').extract()
        overview=remove_class(overview)
        overview=clear_same_s(overview)
        item['overview_en'] = overview
        # print(overview)

        entry=response.xpath('//div[@id="content-tab--2"]').extract()
        entry=remove_class(entry)
        entry=clear_same_s(entry)
        item['rntry_requirements'] = entry

        modules=response.xpath('//div[@id="content-tab--3"]').extract()
        modules=remove_class(modules)
        modules=clear_same_s(modules)
        item['modules_en'] = modules

        fee = response.xpath('//*[contains(text(),"£")]//text()').extract()
        tuition_fee = getTuition_fee(fee)
        item['tuition_fee'] = tuition_fee

        applys=response.xpath('//div[@id="content-tab--6"]').extract()
        apply_documents_en = remove_class(applys)
        apply_documents_en = clear_same_s(apply_documents_en)
        item['apply_documents_en'] = apply_documents_en

        level=response.xpath('//h2[contains(text(),"English language requirement")]/following-sibling::p/a/text()').extract()
        level=''.join(level)
        if level=='Higher level':
            item['ielts'] = '7.5'
            item['ielts_l'] = '7.0'
            item['ielts_s'] = '7.0'
            item['ielts_r'] = '7.0'
            item['ielts_w'] = '7.0'
            item['toefl_r'] = '24'
            item['toefl_l'] = '22'
            item['toefl_s'] = '25'
            item['toefl_w'] = '24'
            item['toefl'] = '110'
        else:
            item['ielts'] = '7.0'
            item['ielts_l'] = '6.5'
            item['ielts_s'] = '6.5'
            item['ielts_r'] = '6.5'
            item['ielts_w'] = '6.5'
            item['toefl_r'] = '24'
            item['toefl_l'] = '22'
            item['toefl_s'] = '25'
            item['toefl_w'] = '24'
            item['toefl'] = '100'

        career=response.xpath('//h2[contains(text(),"Graduate destinations")]/following-sibling::p[position()<=3]').extract()
        if career==[]:
            print(response.url)
        item['career_en']=remove_class(career)

        # item['deadline'] = '2019-3'
        # item['application_open_date'] = '2018-9'
        # print(item)
        yield item
