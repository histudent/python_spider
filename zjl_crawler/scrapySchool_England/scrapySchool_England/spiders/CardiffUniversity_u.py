# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/26 19:26'
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
class CardiffUniversitySpider(scrapy.Spider):
    name = 'CardiffUniversity_u'
    allowed_domains = ['cardiff.ac.uk/']
    start_urls = []
    C= [
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/banking-and-finance-with-a-european-language-german-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/archaeology-and-history-with-a-year-abroad-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-management-logistics-and-operations-with-a-professional-placement-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/architectural-engineering-with-a-year-in-industry-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-engineering-with-a-year-in-france-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/spanish-and-japanese-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-language-and-french-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/welsh-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-literature-and-philosophy-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/integrated-engineering-with-a-year-in-industry-beng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/music-and-mathematics-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/french-and-spanish-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/french-and-economics-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-engineering-with-a-year-in-germany-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/exploration-and-resource-geology-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/computer-science-with-security-and-forensics-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/translation-ba-4-years',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/music-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/financial-mathematics-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/archaeology-and-medieval-history-with-a-year-abroad-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/environmental-geoscience-mesci',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/electrical-and-electronic-engineering-international-with-a-year-in-industry-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-language-and-german-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/law-and-welsh-llb',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/financial-mathematics-with-a-professional-placement-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/child-nursing-september-intake-bn',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/computer-science-with-visual-computing-with-a-year-of-study-abroad-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/geology-mesci',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/archaeology-and-philosophy-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/integrated-engineering-with-a-year-in-france-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-management-human-resources-management-with-a-professional-placement-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-management-human-resources-management-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/msci-in-computer-science-with-a-year-in-industry',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biochemistry-with-a-preliminary-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/integrated-engineering-with-a-year-in-industry-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/ancient-history-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/integrated-engineering-international-with-a-year-in-industry-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/bsc-in-mathematics-with-a-professional-placement-year',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/physics-with-astronomy-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/architectural-engineering-with-a-year-in-industry-beng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/music-and-history-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/financial-mathematics-with-a-year-abroad-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/marine-geography-international-mesci',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/computer-science-with-visual-computing-with-a-year-in-industry-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/operating-department-practice-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biological-sciences-with-a-preliminary-year-and-professional-training-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/ancient-history-and-french-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mechanical-engineering-international-with-a-year-in-industry-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-language-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/politics-and-welsh-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/dental-surgery-bds',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/optometry-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/welsh-and-religious-studies-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/physics-with-astronomy-with-professional-placement-mphys',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/physics-with-astronomy-with-professional-placement-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-management-international-management-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/archaeology-and-medieval-history-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/engineering-foundation-year-foundation-programme',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/modern-chinese-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/journalism-and-communications-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biochemistry-4-years-mbiochem',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/law-and-criminology-llb',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/banking-and-finance-with-a-european-language-french-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-management-with-a-european-language-german-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-and-environmental-engineering-with-a-year-in-france-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/philosophy-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-literature-and-creative-writing-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/german-and-portuguese-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/psychology-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/religious-studies-and-ancient-history-with-a-year-abroad-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/sociology-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/ancient-history-and-spanish-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/human-and-social-sciences-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mechanical-engineering-with-a-year-in-industry-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/ancient-and-medieval-history-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/ancient-history-with-a-year-abroad-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-and-environmental-engineering-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/history-and-economics-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/computer-science-with-high-performance-computing-with-a-year-of-study-abroad-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biomedical-sciences-with-a-professional-training-year-5-years-mbiomed',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mathematics-operational-research-and-statistics-with-a-year-abroad-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/economics-with-a-professional-placement-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/history-with-welsh-history-with-a-year-abroad-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mathematics-with-a-year-abroad-mmath',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/archaeology-and-history-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/urban-planning-and-development-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/astrophysics-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/italian-and-politics-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mathematics-operational-research-and-statistics-with-a-professional-placement-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/marine-geography-with-professional-placement-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/italian-and-japanese-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biochemistry-with-a-professional-training-year-5-years-mbiochem',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/archaeology-and-italian-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/history-and-religious-studies-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/architectural-engineering-with-a-year-in-spain-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/urban-planning-and-development-with-a-year-in-industry-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/ancient-history-and-archaeology-with-a-year-abroad-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/media-and-communications-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biomedical-sciences-4-years-mbiomed',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/midwifery-bmid',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-economics-with-a-european-language-german-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/philosophy-and-economics-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/medicine-mbbch',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/translation-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/religious-studies-and-german-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/computer-science-with-high-performance-computing-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/master-of-mathematics,-operational-research-and-statistics-with-a-year-of-study-abroad-mmors',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/radiotherapy-and-oncology-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-language-and-linguistics-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mathematics-mmath',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/economics-with-a-european-language-french-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/integrated-engineering-beng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/german-and-history-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/environmental-geography-international-mesci',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/ancient-history-and-german-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/diagnostic-radiography-and-imaging-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/environmental-geography-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biochemistry-with-a-preliminary-year-and-professional-training-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/religious-and-theological-studies-with-a-year-abroad-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/french-and-german-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-management-international-management-with-professional-placement-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-management-marketing-with-a-professional-placement-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biomedical-sciences-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-management-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/physics-with-professional-placement-mphys',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/optometry-with-a-preliminary-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mental-health-nursing-march-intake-bn',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/exploration-and-resource-geology-international-mesci',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/archaeology-and-german-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/conservation-of-objects-in-museums-and-archaeology-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mechanical-engineering-international-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-engineering-international-with-a-year-in-industry-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/social-analytics-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/theoretical-and-computational-physics-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/ancient-history-and-history-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/chemistry-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/german-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/neuroscience-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-management-with-a-european-language-french-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/politics-and-spanish-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/economics-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/medical-pharmacology-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/physics-with-medical-physics-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/electrical-and-electronic-engineering-beng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/music-with-a-year-of-study-abroad-bmus',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/occupational-therapy-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/spanish-and-economics-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/architectural-engineering-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/italian-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/international-relations-bscecon',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/law-and-politics',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/german-and-italian-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/archaeology-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/italian-and-english-literature-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/archaeology-and-french-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/archaeology-and-ancient-history-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-literature-and-history-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/computer-science-with-security-and-forensics-with-a-year-of-study-abroad-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/economics-with-a-european-language-spanish-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-literature-and-welsh-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/conservation-of-objects-in-museum-and-archaeology-with-a-year-abroad-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mechanical-engineering-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/medical-engineering-international-with-a-year-in-industry-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/french-and-japanese-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biomedical-sciences-with-a-preliminary-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-management-with-welsh-with-a-professional-placement-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/applied-software-engineering-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/accounting-with-a-professional-placement-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/law-and-sociology-llb',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-and-environmental-engineering-beng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/philosophy-and-politics-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/ancient-history-and-italian-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/sociology-and-social-policy-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/social-science-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-economics-with-a-professional-placement-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/politics-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/philosophy-and-religious-studies-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/ancient-history-and-philosophy-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/music-bmus',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-engineering-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-engineering-with-a-year-in-spain-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/msci-in-computer-science-with-a-year-of-study-abroad',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/law-llb',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/dental-therapy-and-hygiene-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/religious-studies-and-italian-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/economics-and-finance-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/italian-and-philosophy-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/welsh-and-italian-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/spanish-and-philosophy-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-language-and-italian-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mechanical-engineering-with-a-year-in-spain-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/education-and-welsh-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/religious-studies-and-theology-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/french-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mathematics-and-physics-with-a-year-of-study-abroad-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-language-and-spanish-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/geology-international-mesci',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/italian-and-spanish-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/chemistry-mchem',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/geography-human-and-planning-with-professional-placement-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-management-with-a-professional-placement-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/exploration-and-resource-geology-with-professional-placement-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/environmental-geography-mesci',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/ancient-history-and-history-with-a-year-of-study-abroad',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-management-with-welsh-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/education-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/portuguese-and-italian-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-language-and-welsh-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/french-and-philosophy-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/neuroscience-4-years-mneuro',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/history-and-italian-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/french-and-italian-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/geography-human-and-planning-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/chemistry-with-industrial-experience-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/neuroscience-with-a-professional-training-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/french-and-politics-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/architectural-engineering-with-a-year-in-france-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/french-and-portuguese',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/architectural-engineering-with-a-year-in-germany-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/electrical-and-electronic-engineering-international-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/physics-with-professional-placement-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mental-health-nursing-september-intake-bn',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/chemistry-with-a-year-abroad-mchem',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-engineering-with-a-year-in-industry-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/accounting-and-finance-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/archaeology-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/psychology-with-a-professional-placement-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/economics-with-a-european-language-german-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-language-and-philosophy-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-literature-and-ancient-history-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/politics-and-sociology-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/physics-and-mathematics-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/master-of-mathematics,-operational-research-and-statistics-mmors',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/archaeology-and-religious-studies-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/history-with-a-year-abroad-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/economics-and-management-studies-with-a-professional-placement-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mathematics-operational-research-and-statistics-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/marine-geography-mesci',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/chemistry-with-a-preliminary-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/architectural-engineering-international-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/computer-science-with-high-performance-computing-with-a-year-in-industry-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/criminology-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/neuroscience-with-a-preliminary-year-and-professional-training-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biochemistry-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/dental-surgery-with-a-preliminary-year-bds',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/italian-and-economics-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/journalism-media-and-sociology-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biological-sciences-with-a-professional-training-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/banking-and-finance-with-a-european-language-spanish-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/neuroscience-with-a-preliminary-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/environmental-geoscience-with-professional-placement-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/religious-studies-and-archaeology-with-a-year-abroad-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/journalism-media-and-english-literature-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/adult-nursing-september-intake-bn',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-engineering-with-a-year-in-industry-beng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/architectural-engineering-beng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/music-and-english-literature-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/medical-engineering-with-a-year-in-industry-beng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-economics-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/philosophy-and-welsh-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/welsh-and-spanish-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-management-logistics-and-operations-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biochemistry-with-a-professional-training-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/french-and-history-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mechanical-engineering-with-a-year-in-industry-beng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/sociology-and-education-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/economics-and-finance-with-a-professional-placement-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/german-and-spanish-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-engineering-international-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biological-sciences-4-years-mbiol',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/electrical-and-electronic-engineering-with-a-year-in-industry-beng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/architectural-engineering-international-with-a-year-in-industry-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/media-journalism-and-culture-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/history-and-sociology-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-literature-and-german-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/german-and-economics-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/integrated-engineering-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biological-sciences-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/history-and-welsh-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/exploration-and-resource-geology-mesci',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/journalism-and-welsh-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biological-sciences-with-a-preliminary-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-literature-and-religious-studies-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/international-relations-and-politics-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/journalism-communications-and-politics',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/geology-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/music-and-mathematics-with-a-year-abroad-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/medicine-with-a-preliminary-year-mbbch',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/physics-mphys',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/ancient-and-medieval-history-with-a-year-abroad-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-literature-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/french-and-welsh-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/history-and-spanish-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-and-environmental-engineering-with-a-year-in-germany-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/spanish-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/physics-with-astronomy-mphys',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/religious-studies-and-history-with-a-year-abroad-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mechanical-engineering-with-a-year-in-france-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/neuroscience-with-a-professional-training-year-5-years-mneuro',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/german-and-japanese-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/architecture-bscmarch',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/history-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biological-sciences-with-a-professional-training-year-5-years-mbiol',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/spanish-and-english-literature-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/adult-nursing-march-intake-bn',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/geography-human-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/physics-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-and-environmental-engineering-with-a-year-in-industry-international-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/law-and-french-llb',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-language-and-literature-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/german-and-music-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/politics-and-international-relations-with-a-language-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/integrated-engineering-with-a-year-in-spain-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/politics-and-economics-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/welsh-and-music-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-and-environmental-engineering-international-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/history-with-welsh-history-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/environmental-geoscience-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/religious-studies-and-politics-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/accounting-and-finance-with-a-professional-placement-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mechanical-engineering-with-a-year-in-germany-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-studies-and-japanese-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/marine-geography-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/archaeology-with-a-year-abroad-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/banking-and-finance-with-a-professional-placement-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-and-environmental-engineering-with-a-year-in-spain-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/electrical-and-electronic-engineering-with-a-year-in-industry-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/chemistry-with-a-year-in-industry-mchem',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biomedical-sciences-with-a-preliminary-year-and-professional-training-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/msci-in-computer-science',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/electrical-and-electronic-engineering-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/environmental-geoscience-international-mesci',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/pharmacy-mpharm',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/economics-and-management-studies-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/integrated-engineering-international-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/german-and-politics-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/religious-studies-and-spanish-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mathematics-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/physiotherapy-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/archaeology-with-a-year-abroad-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-and-environmental-engineering-with-a-year-in-industry-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/religious-studies-and-music-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/master-of-mathematics,-operational-research-and-statistics-with-a-professional-placement-year-mmors',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-economics-with-a-european-language-spanish-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/integrated-engineering-with-a-year-in-germany-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/portuguese-and-spanish-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mathematics-with-a-year-abroad-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-and-environmental-engineering-with-a-year-in-industry-beng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/french-and-music-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-economics-with-a-european-language-french-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/history-and-philosophy-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/accounting-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/medical-engineering-beng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/music-and-philosophy-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/english-literature-and-archaeology-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/banking-and-finance-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/computer-science-with-visual-computing-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/criminology-and-social-policy-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/medical-engineering-international-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/ancient-history-and-religious-studies-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-management-marketing-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/biomedical-sciences-with-a-professional-training-year-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/computer-science-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/civil-engineering-beng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/medical-engineering-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/business-management-with-a-european-language-spanish-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/french-and-english-literature-ba',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/criminology-and-sociology-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/modern-history-and-politics-bsc-econ',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/mechanical-engineering-beng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/astrophysics-mphys',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/medical-engineering-with-a-year-in-industry-meng',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/computer-science-with-a-year-in-industry-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/computer-science-with-a-year-of-study-abroad-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/computer-science-with-security-and-forensics-with-a-year-in-industry-bsc',
        'https://www.cardiff.ac.uk/study/undergraduate/courses/2019/italian-and-music-ba'
    ]
    C = set(C)
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Cardiff University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en_a= response.xpath('//*[@id="content"]/div[1]/div/div[1]/h1').extract()
        programme_en_a = ''.join(programme_en_a)
        programme_en_a = remove_tags(programme_en_a)
        if '(' in programme_en_a:
            programme_en = programme_en_a.split()[:-1]
            programme_en = ' '.join(programme_en)
        else:programme_en = programme_en_a
        # print(programme_en)

        #4.overview_en
        overview_en = response.xpath('//*[@id="content"]/div[1]/div/div[1]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #5.start_date
        start_date = '2019-9'

        #6.duration #7.duration_per
        duration_list = response.xpath("//*[contains(text(),'Duration')]//following-sibling::*").extract()
        duration_list  = ''.join(duration_list)
        duration_list  = remove_tags(duration_list)
        try:
            duration_a = re.findall('\d+',duration_list)[0]
        except:
            duration_a = 1
        if 'five years' in duration_list:
            duration = 5
        elif 'seven years' in duration_list:
            duration = 7
        else:
            duration = duration_a
        if 'months' in duration_list:
            duration_per = 3
        else:
            duration_per = 1
        # print(duration,'********',duration_per)

        #8.degree_name
        degree_name = response.xpath('//*[@id="content"]/div[1]/div/div[1]/h1').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        degree_name = degree_name.split()[-1]
        degree_name = degree_name.replace('(','').replace(')','').strip()
        # print(degree_name)


        #9.ucascode
        ucascode = response.xpath('//*[@id="section1"]/table[1]//tr[1]/td').extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode)
        # print(ucascode)

        #10.modules_en
        # modules_en = response.xpath('//*[@id="coreModulesList-1"]/div/table//tr/td/a').extract()
        # modules_en = ''.join(modules_en)
        # modules_en = remove_class(modules_en)
        # modules_en = '<p>'+modules_en+'</p>'
        modules_en = response.xpath('//*[@id="section2"]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)

        # print(modules_en)

        #11.alevel
        alevel = response.xpath("//*[contains(text(),'A level ')]//following-sibling::*").extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel).strip()
        # print(alevel)

        #12.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'How will I be assessed?')]//following-sibling::p").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #13.career_en
        career_en = response.xpath('//*[@id="section5"]/div[1]/div[1]/p').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #14.tuition_fee
        tuition_fee = response.xpath('//*[@id="tuitionfees"]/table/tbody/tr/td[1]').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #15.ib
        ib = response.xpath("//*[contains(text(),'International Baccalaureate')]//following-sibling::*").extract()
        ib =  ''.join(ib)
        ib = remove_tags(ib).strip()
        # print(ib)

        #16.tuition_fee_pre
        tuition_fee_pre = '£'

        #17 18192021
        if 'Dentistry' in programme_en:
            ielts = 7.0
            ielts_s = 6.5
            ielts_r = 6.5
            ielts_l = 6.5
            ielts_w = 6.5
        elif 'Medicine' in programme_en:
            ielts = 7.0
            ielts_s = 6.5
            ielts_r = 6.5
            ielts_l = 6.5
            ielts_w = 6.5
        elif 'Law' in programme_en:
            ielts = 6.5
            ielts_s = 6.5
            ielts_r = 6.0
            ielts_l = 6.0
            ielts_w = 6.0
        elif 'Politics' in programme_en:
            ielts = 6.5
            ielts_s = 6.5
            ielts_r = 6.0
            ielts_l = 6.0
            ielts_w = 6.0
        else:
            ielts = 6.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_w = 5.5
        # print(ielts,ielts_s,ielts_r,ielts_l,ielts_w)

        #22.degree_type
        degree_type = 1

        item['ib'] = ib
        item['alevel'] = alevel
        item['ucascode'] = ucascode
        item['degree_name'] = degree_name
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['overview_en'] = overview_en
        item['start_date'] = start_date
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['degree_type'] = degree_type
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['ielts'] = ielts
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        yield  item