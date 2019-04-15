# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/18 10:01'
import scrapy,json
import re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.clearSpace import clear_space_str
from w3lib.html import remove_tags
class QueenMaryUniversityofLondonSpider(scrapy.Spider):
    name = 'QueenMaryUniversityofLondon_U'
    allowed_domains = ['qmul.ac.uk/']
    start_urls = []
    C= [
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-finance-and-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-with-finance-and-accounting/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-finance-and-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-with-finance-and-accounting/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-finance-and-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-with-finance-and-accounting/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-finance/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/materials-science-and-engineering-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-finance/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/materials-science-and-engineering-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/materials-science-and-engineering-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-finance/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-finance/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/materials-science-and-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-finance/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/materials-science-and-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/materials-science-and-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-finance/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/materials-science-and-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/materials-science-and-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-finance/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/materials-science-and-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-finance/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-finance/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-politics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-politics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-international-finance/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/electrical-and-electronic-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mechanical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-politics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mechanical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-international-finance/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mechanical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/electrical-and-electronic-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mechanical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-politics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mechanical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-international-finance/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mechanical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/electrical-and-electronic-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-with-actuarial-science/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-politics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-with-actuarial-science/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-international-finance/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-with-actuarial-science/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/electrical-and-electronic-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-with-statistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-politics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-with-statistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-international-finance/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/international-relations/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-and-international-finance/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/international-relations/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/electronic-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/law/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/electronic-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/law-and-politics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/electronic-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-statistics-and-financial-economics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-statistics-and-mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-statistics-and-financial-economics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-statistics-and-mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-statistics-and-financial-economics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-statistics-and-mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-statistics-and-mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/law-with-history/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-statistics-and-mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/law-with-business/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-statistics-and-mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/linguistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/linguistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/materials-and-design/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/german-and-politics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/materials-and-design/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/german-with-business-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/marketing-and-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/electronic-engineering-and-telecommunications/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/materials-and-design/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/electronic-engineering-and-telecommunications/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/marketing-and-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/electronic-engineering-and-telecommunications/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/materials-and-design/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/electronic-engineering-and-telecommunications/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/materials-and-design/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/electronic-engineering-and-telecommunications/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/materials-and-design/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/global-law/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/global-health/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/global-health/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/hispanic-studies-and-comparative-literature/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/hispanic-studies-and-politics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/business-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/international-politics-with-french-paris/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/business-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/international-politics-with-french-paris/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/business-with-law/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/science-and-engineering-foundation-programme-materials-science/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/comparative-literature/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/science-and-engineering-foundation-programme-materials-science/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/comparative-literature/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/hispanic-studies-and-linguistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/science-and-engineering-foundation-programme-mathematical-sciences/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/hispanic-studies-with-business-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/theoretical-physics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/chemical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/theoretical-physics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/chemical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/sustainable-energy-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/chemical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/sustainable-energy-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/chemical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/zoology/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/chemical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/sustainable-energy-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/chemical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/zoology/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/comparative-literature-and-linguistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/sustainable-energy-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/comparative-literature-and-linguistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/sustainable-energy-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/comparative-literature-and-film-studies/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/sustainable-energy-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/comparative-literature-and-film-studies/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/computer-science/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/computer-science/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/international-politics-paris/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/computer-science/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/international-politics-paris/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/computer-science/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/science-and-engineering-foundation-programme-physics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/computer-science/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/science-and-engineering-foundation-programme-physics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/computer-science-with-management-itmb/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mechanical-engineering-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/computer-science-with-management-itmb/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mechanical-engineering-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/chemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mechanical-engineering-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/computer-science-with-management-itmb/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/chemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/medicine-malta-5-year-programme/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/chemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/software-engineering-for-business/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/chemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/software-engineering-for-business/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/chemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/software-engineering-for-business/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/computer-science-and-mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/world-history/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/computer-science-and-mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/world-history/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/computer-science-and-mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/modern-languages/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/computer-systems-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/neuroscience/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/computer-systems-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/neuroscience/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/computer-systems-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/medieval-history/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/creative-computing/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/medicine-5-year-programme/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/creative-computing/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/medical-genetics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/creative-computing/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/medical-genetics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/dentistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/pharmaceutical-chemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/cultural-history/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/pharmaceutical-chemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/cultural-history/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/pharmaceutical-chemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/digital-and-technology-solutions-business-analyst/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/pharmaceutical-chemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/dental-materials/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/pharmaceutical-chemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/dental-materials/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/modern-and-contemporary-history/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/dental-materials/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/dental-materials/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/dental-materials/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/dental-materials/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/design-innovation-and-creative-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/design-innovation-and-creative-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/design-innovation-and-creative-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/design-innovation-and-creative-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/digital-and-technology-solutions-data-analyst/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/digital-and-technology-solutions-it-consultant/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biochemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biochemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biochemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biochemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biochemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/digital-and-technology-solutions-software-engineer/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/astrophysics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/astrophysics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/accounting-and-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/accounting-and-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/aerospace-engineering-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/aerospace-engineering-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/aerospace-engineering-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/aerospace-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/aerospace-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/aerospace-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/aerospace-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/aerospace-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/aerospace-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomaterials-for-biomedical-sciences/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomaterials-for-biomedical-sciences/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomaterials-for-biomedical-sciences/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomaterials-for-biomedical-sciences/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomaterials-for-biomedical-sciences/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomaterials-for-biomedical-sciences/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biology/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biology/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomedical-engineering-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomedical-engineering-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomedical-engineering-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomedical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomedical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomedical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomedical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomedical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomedical-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomedical-sciences/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/biomedical-sciences/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/french-and-history/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/french-and-linguistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/french-with-business-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/french-and-politics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/german-and-linguistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/genetics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/genetics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english-and-drama/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english-and-drama/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/geography-bsc/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/geography-bsc/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/geography-ba/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/geography-ba/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/german-and-comparative-literature/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/geography-with-business-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/geography-with-business-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english-and-european-law/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english-and-french-law/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english-and-film-studies/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english-and-film-studies/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english-and-history/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english-and-history/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english-language/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english-language/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english-with-creative-writing/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english-with-creative-writing/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english-language-and-linguistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english-language-and-linguistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/environmental-science/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/environmental-science/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/environmental-science-with-business-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/environmental-science-with-business-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/film-studies/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/film-studies/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english-literature-and-linguistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/english-literature-and-linguistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/film-studies-and-drama/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/film-studies-and-drama/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/film-studies-and-french/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/film-studies-and-german/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/film-studies-and-hispanic-studies/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/film-studies-and-russian/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/french-and-comparative-literature/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/financial-mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/financial-mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/financial-mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/history/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/history-and-comparative-literature/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/history-and-comparative-literature/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/history-and-german/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/history-and-film-studies/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/history-and-film-studies/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/history-and-politics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/intellectual-history/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/intellectual-history/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/human-geography/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/human-geography/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/pharmacology-and-innovative-therapeutics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/pharmacology-and-innovative-therapeutics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/physics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/physics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/physics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/physics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/physics-with-astrophysics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/physics-with-astrophysics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/physics-with-particle-physics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/physics-with-particle-physics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/politics-with-business-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/physics-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/physics-with-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/politics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/politics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/politics-and-international-relations/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/politics-and-international-relations/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/russian-and-comparative-literature/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/pure-mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/pure-mathematics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/psychology/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/psychology/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/robotics-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/robotics-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/robotics-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/robotics-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/robotics-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/robotics-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/russian-and-politics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/russian-with-business-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/russian-and-linguistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/science-and-engineering-foundation-programme-chemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/science-and-engineering-foundation-programme-chemistry/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/science-and-engineering-foundation-programme-computer-science/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/science-and-engineering-foundation-programme-electronic-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/science-and-engineering-foundation-programme-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/science-and-engineering-foundation-programme-engineering/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/drama/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-and-statistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/drama/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-and-statistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-finance-and-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/mathematics-and-statistics/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-finance-and-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/science-and-engineering-foundation-programme-biological-sciences/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/economics-finance-and-management/',
        'https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2019/science-and-engineering-foundation-programme-biological-sciences/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)
        #1.university
        university = 'Queen Mary University of London'


        #2.location
        location = 'London'


        #3.department
        department = response.xpath('//*[@id="about"]/div/div/div[2]/p[1]/a').extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #4.programme_en
        programme_en = response.xpath('/html/body/section[2]/div/div/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_class(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #5.degree_type
        degree_type = 1

        #6.degree_name
        try:
            degree_name = response.xpath("//*[contains(text(),'Degree')]//following-sibling::dd[1]").extract()[0]
            degree_name = remove_tags(degree_name)
            if '(' in degree_name:
                degree_name = re.findall(r'(.*)\(',degree_name)
                degree_name = ''.join(degree_name)
                if '(' in degree_name:
                    degree_name = re.findall(r'(.*)\(', degree_name)
                    degree_name = ''.join(degree_name)
                else:pass
            else:pass
            # print(degree_name)
        except:
            degree_name = 'N/A'

        #7.duration
        duration = response.xpath("//*[contains(text(),'Duration')]//following-sibling::dd[1]").extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        duration = re.findall('\d+',duration)[0]
        # print(duration)

        #8.duration_per
        duration_per = 1

        #9.overview_en
        overview_en = response.xpath('//*[@id="overview"]/div/div/div[1]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #10.ucascode
        try:
            ucascode = response.xpath("//*[contains(text(),'UCAS code')]//following-sibling::dd[1]").extract()[0]
            ucascode = ''.join(ucascode)
            ucascode = remove_tags(ucascode)
        except:
            ucascode = 'N/A'
        # print(ucascode)

        #11.modules_en
        try:
            modules_en = response.xpath('//*[@id="structure"]/div/div[2]').extract()
            modules_en = ''.join(modules_en)
            modules_en = remove_class(modules_en)
        except:
            modules_en = 'N/A'
        # print(modules_en)

        #12.assessment_en
        try:
            assessment_en = response.xpath("//*[contains(text(),'Assessment')]//following-sibling::*").extract()
            assessment_en = ''.join(assessment_en)
            assessment_en = remove_class(assessment_en)
            assessment_en = clear_space_str(assessment_en)
        except:
            assessment_en = 'N/A'
        # print(assessment_en)

        #13.alevel
        try:
            alevel = response.xpath("//*[contains(text(),'A-Level')]//following-sibling::td").extract()[0]
            alevel = ''.join(alevel)
            alevel = remove_tags(alevel)
        except:
            alevel  = 'N/A'
        # print(alevel)

        #14.ib
        try:
            ib =  response.xpath("//*[contains(text(),'IB')]//following-sibling::td").extract()[0]
            ib = ''.join(ib)
            ib = remove_tags(ib)
        except:
            ib = 'N/A'
        # print(ib)

        #15.career_en
        try:
            career_en = response.xpath("//*[contains(text(),'Career support')]//following-sibling::*").extract()
            career_en = ''.join(career_en)
            career_en = remove_class(career_en)
            career_en = clear_space_str(career_en)
        except:
            career_en = 'N/A'
        # print(career_en)

        #16.tuition_fee
        try:
            tuition_fee1 = response.xpath("//*[contains(text(),'International fees')]//following-sibling::*").extract()
            tuition_fee1 = ''.join(tuition_fee1)
            tuition_fee1 = remove_tags(tuition_fee1)
            tuition_fee = getTuition_fee(tuition_fee1)

        except:
            tuition_fee = 0
        # print(tuition_fee)

        #17.tuition_fee_pre
        tuition_fee_pre = '£'

        #18.start_date
        start_date = '2019-9'

        #19.ielts 20212223
        if department == 'School of Biological and Chemical Sciences':
            ielts=6.5
            ielts_l=5.5
            ielts_s=5.5
            ielts_r=5.5
            ielts_w=6.0
            toefl=92
            toefl_l=17
            toefl_s=20
            toefl_r=18
            toefl_w=21
        elif department =='School of Business and Management':
            ielts = 7.0
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 5.5
            toefl = 100
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 17
        elif department =='School of Economics and Finance':
            ielts = 6.5
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 6.0
            toefl = 92
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 21
        elif department=='School of Electronic Engineering and Computer Science':
            ielts = 6.0
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 6.5
            toefl = 79
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 17
        elif department =='School of English and Drama':
            ielts = 7.0
            ielts_l = 7.0
            ielts_s = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            toefl = 100
            toefl_l = 22
            toefl_s = 25
            toefl_r = 24
            toefl_w = 27
        elif department=='School of Geography':
            ielts = 7.0
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 6.5
            toefl = 92
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 24
        elif department =='School of History':
            ielts = 7.0
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 6.5
            toefl = 100
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 24
        elif department == 'School of Languages, Linguistics and Film':
            ielts = 7.0
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 7.0
            toefl = 100
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 27
        elif department == 'School of Law':
            ielts = 7.0
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 6.5
            toefl = 100
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 24
        elif department == 'School of Mathematical Sciences':
            ielts = 6.0
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 5.5
            toefl = 79
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 17
        elif department == 'School of Medicine and Dentistry':
            ielts = 7.0
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 6.5
            toefl = 100
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 24
        elif department == 'School of Physics and Astronomy':
            ielts = 6.0
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 6.5
            toefl = 79
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 17
        elif department == 'School of Politics and International Relations':
            ielts = 7.0
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 6.5
            toefl = 100
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 24
        else:
            ielts = 6.5
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 6.0
            toefl = 92
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 21
        # print(ielts,ielts_l,ielts_r,ielts_s,ielts_w)

        url = response.url
        # print(url)

        require_chinese_en = '<p>Students who have successfully completed Senior High School education in China with 80% or above will be required to attend the foundation programme first, after finish the foundation programme successfully will be considered for entry onto our undergraduate programmes. All students need to apply to Queen Mary directly. For more information on our undergraduate programmes, please refer to our undergraduate study section of this website.High School Diploma (Gaozhong Biye Zhengshu) with average 80%+ 590+ in College Entrance Exam (Gao Kao) We also accept students from China with:Three A-levels International Baccalaureate (IB) Students whose grades do not meet our minimum requirements may, in some cases, be considered for entry onto our foundation programmes.For more detailed information on Medicine and Dentistry requirements and how to apply please refer to the School of Medicine and Dentistry section of our website.</p>'

        item['university'] = university
        item['location'] = location
        item['department'] = department
        item['degree_type'] = degree_type
        item['duration_per'] = duration_per
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['alevel'] = alevel
        item['ib'] = ib
        item['career_en'] = career_en
        # item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['start_date'] = start_date
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['ielts_w'] = ielts_w
        item['url'] = url
        item['require_chinese_en'] = require_chinese_en
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_w'] = toefl_w
        item['toefl_l'] = toefl_l

        programme_en_a = response.xpath('//section[starts-with(@id, "ucas-")]/h3').extract()
        degree_name_a = response.xpath('//div/dl/dd[1]').extract()
        duration_a = response.xpath('//div/dl/dd[2]').extract()
        ucascode_a = response.xpath('//div/dl/dd[4]').extract()
        if len(ucascode_a)>1:
            for i,j,k,l in zip(ucascode_a,degree_name_a,duration_a,programme_en_a):
                response_programme_en = l
                response_programme_en = remove_tags(response_programme_en)
                response_degree_name = j
                response_degree_name = remove_tags(response_degree_name)
                response_duration = k
                response_duration = remove_tags(response_duration)
                response_ucascode = i
                response_ucascode = remove_tags(response_ucascode)
                response_programme_en = response_programme_en.replace(response_degree_name,'').strip()
                if '(Hons)' in response_degree_name:
                    response_degree_name = response_degree_name.replace('(Hons)','').strip()
                item['programme_en'] = response_programme_en
                item['duration'] = response_duration
                item['degree_name'] = response_degree_name
                item['ucascode'] = response_ucascode
                yield item
        else:
            item['programme_en'] =programme_en
            item['duration'] = duration
            item['degree_name'] = degree_name
            item['ucascode'] = ucascode
            yield item