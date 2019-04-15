# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/8 15:47'
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
from scrapySchool_England.TranslateMonth import translate_month
class UniversityofKentSpider(scrapy.Spider):
    name = 'UniversityofKent_u'
    allowed_domains = ['kent.ac.uk/']
    start_urls = []
    C= [
        'https://www.kent.ac.uk/courses/undergraduate/7/actuarial-science',
        'https://www.kent.ac.uk/courses/undergraduate/237/accounting-and-finance-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/1896/actuarial-science-with-a-foundation-year',
        'https://www.kent.ac.uk/courses/undergraduate/235/accounting-and-finance',
        'https://www.kent.ac.uk/courses/undergraduate/6/actuarial-science-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/1/accounting-and-finance-and-economics',
        'https://www.kent.ac.uk/courses/undergraduate/11/american-studies',
        'https://www.kent.ac.uk/courses/undergraduate/8/american-studies-history',
        'https://www.kent.ac.uk/courses/undergraduate/10/american-studies-literature',
        'https://www.kent.ac.uk/courses/undergraduate/82/ancient-history',
        'https://www.kent.ac.uk/courses/undergraduate/9/american-studies-latin-america',
        'https://www.kent.ac.uk/courses/undergraduate/36/anthropology',
        'https://www.kent.ac.uk/courses/undergraduate/2507/anthropology-year-professional-practice',
        'https://www.kent.ac.uk/courses/undergraduate/4/architecture',
        'https://www.kent.ac.uk/courses/undergraduate/95/art-history',
        'https://www.kent.ac.uk/courses/undergraduate/889/architecture',
        'https://www.kent.ac.uk/courses/undergraduate/894/ancient-medieval-and-modern-history',
        'https://www.kent.ac.uk/courses/undergraduate/2493/anthropology-with-a-year-abroad',
        'https://www.kent.ac.uk/courses/undergraduate/831/art-history-and-english-and-american-literature',
        'https://www.kent.ac.uk/courses/undergraduate/404/asian-studies-and-comparative-literature',
        'https://www.kent.ac.uk/courses/undergraduate/832/art-history-and-film',
        'https://www.kent.ac.uk/courses/undergraduate/830/art-history-and-classical-and-archaeological-studies',
        'https://www.kent.ac.uk/courses/undergraduate/833/art-history-and-french',
        'https://www.kent.ac.uk/courses/undergraduate/835/art-history-and-hispanic-studies',
        'https://www.kent.ac.uk/courses/undergraduate/403/asian-studies-and-classical-and-archaeological-studies',
        'https://www.kent.ac.uk/courses/undergraduate/1953/asian-studies-and-english-and-american-literature',
        'https://www.kent.ac.uk/courses/undergraduate/398/asian-studies-and-english-language-and-linguistics',
        'https://www.kent.ac.uk/courses/undergraduate/399/asian-studies-and-french',
        'https://www.kent.ac.uk/courses/undergraduate/400/asian-studies-and-german',
        'https://www.kent.ac.uk/courses/undergraduate/397/asian-studies-and-philosophy',
        'https://www.kent.ac.uk/courses/undergraduate/396/asian-studies-and-religious-studies',
        'https://www.kent.ac.uk/courses/undergraduate/836/art-history-and-history',
        'https://www.kent.ac.uk/courses/undergraduate/68/astronomy-space-science-and-astrophysics-mphys',
        'https://www.kent.ac.uk/courses/undergraduate/67/astronomy-space-science-and-astrophysics-bsc',
        'https://www.kent.ac.uk/courses/undergraduate/69/astronomy-space-science-and-astrophysics-with-a-year-abroad-mphys',
        'https://www.kent.ac.uk/courses/undergraduate/2527/astronomy-space-science-astrophysics-year-industry',
        'https://www.kent.ac.uk/courses/undergraduate/142/autism-studies',
        'https://www.kent.ac.uk/courses/undergraduate/96/biochemistry',
        'https://www.kent.ac.uk/courses/undergraduate/75/biological-anthropology',
        'https://www.kent.ac.uk/courses/undergraduate/2492/biological-anthropology-with-a-year-abroad',
        'https://www.kent.ac.uk/courses/undergraduate/255/biology',
        'https://www.kent.ac.uk/courses/undergraduate/258/biology-with-a-year-abroad',
        'https://www.kent.ac.uk/courses/undergraduate/100/biochemistry-with-a-sandwich-year',
        'https://www.kent.ac.uk/courses/undergraduate/1366/biological-anthropology-with-a-year-in-professional-practice',
        'https://www.kent.ac.uk/courses/undergraduate/257/biology-with-a-sandwich-year',
        'https://www.kent.ac.uk/courses/undergraduate/264/biochemistry-with-a-year-abroad',
        'https://www.kent.ac.uk/courses/undergraduate/2497/biomedical-engineering',
        'https://www.kent.ac.uk/courses/undergraduate/2498/biomedical-engineering-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/260/biomedical-science-with-a-year-abroad',
        'https://www.kent.ac.uk/courses/undergraduate/238/business-and-management-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/263/biomedical-science',
        'https://www.kent.ac.uk/courses/undergraduate/137/business-information-technology',
        'https://www.kent.ac.uk/courses/undergraduate/262/biomedical-science-with-a-sandwich-year',
        'https://www.kent.ac.uk/courses/undergraduate/141/business-information-technology-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/12/business-top-up',
        'https://www.kent.ac.uk/courses/undergraduate/388/chemistry-with-a-foundation-year',
        'https://www.kent.ac.uk/courses/undergraduate/15/chemistry-mchem',
        'https://www.kent.ac.uk/courses/undergraduate/78/chemistry',
        'https://www.kent.ac.uk/courses/undergraduate/83/chemistry-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/276/classical-and-archaeological-studies-and-italian',
        'https://www.kent.ac.uk/courses/undergraduate/3/comparative-literature',
        'https://www.kent.ac.uk/courses/undergraduate/896/classical-studies',
        'https://www.kent.ac.uk/courses/undergraduate/265/comparative-literature-and-drama',
        'https://www.kent.ac.uk/courses/undergraduate/155/classical-and-archaeological-studies-and-film',
        'https://www.kent.ac.uk/courses/undergraduate/277/classical-and-archaeological-studies-and-philosophy',
        'https://www.kent.ac.uk/courses/undergraduate/84/classical-and-archaeological-studies',
        'https://www.kent.ac.uk/courses/undergraduate/272/classical-and-archaeological-studies-and-comparative-literature',
        'https://www.kent.ac.uk/courses/undergraduate/268/comparative-literature-and-film',
        'https://www.kent.ac.uk/courses/undergraduate/345/german-and-comparative-literature',
        'https://www.kent.ac.uk/courses/undergraduate/266/comparative-literature-and-english-and-american-literature',
        'https://www.kent.ac.uk/courses/undergraduate/382/comparative-literature-and-english-language-and-linguistics',
        'https://www.kent.ac.uk/courses/undergraduate/384/comparative-literature-and-hispanic-studies',
        'https://www.kent.ac.uk/courses/undergraduate/269/comparative-literature-and-french',
        'https://www.kent.ac.uk/courses/undergraduate/223/comparative-literature-and-italian',
        'https://www.kent.ac.uk/courses/undergraduate/87/comparative-literature-with-a-year-abroad',
        'https://www.kent.ac.uk/courses/undergraduate/124/computer-science',
        'https://www.kent.ac.uk/courses/undergraduate/168/computer-science-networks',
        'https://www.kent.ac.uk/courses/undergraduate/129/computer-science-artificial-intelligence',
        'https://www.kent.ac.uk/courses/undergraduate/131/computer-science-artificial-intelligence-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/158/computer-science-consultancy',
        'https://www.kent.ac.uk/courses/undergraduate/162/computer-science-consultancy-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/2496/computer-science-for-health',
        'https://www.kent.ac.uk/courses/undergraduate/2508/computer-science-for-health-year-industry',
        'https://www.kent.ac.uk/courses/undergraduate/167/computer-science-networks-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/34/computer-systems-engineering-beng',
        'https://www.kent.ac.uk/courses/undergraduate/32/computer-systems-engineering-meng',
        'https://www.kent.ac.uk/courses/undergraduate/208/computer-systems-engineering-including-a-foundation-year',
        'https://www.kent.ac.uk/courses/undergraduate/204/computer-systems-engineering-with-a-year-in-industry-meng',
        'https://www.kent.ac.uk/courses/undergraduate/128/computer-science-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/181/computing',
        'https://www.kent.ac.uk/courses/undergraduate/210/computer-systems-engineering-with-a-year-in-industry-beng',
        'https://www.kent.ac.uk/courses/undergraduate/185/computing-consultancy',
        'https://www.kent.ac.uk/courses/undergraduate/871/contemporary-literature',
        'https://www.kent.ac.uk/courses/undergraduate/187/computing-consultancy-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/183/computing-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/360/criminology-and-sociology',
        'https://www.kent.ac.uk/courses/undergraduate/234/criminology',
        'https://www.kent.ac.uk/courses/undergraduate/1374/criminology-with-quantitative-research',
        'https://www.kent.ac.uk/courses/undergraduate/202/criminology-and-social-policy',
        'https://www.kent.ac.uk/courses/undergraduate/203/criminology-and-cultural-studies',
        'https://www.kent.ac.uk/courses/undergraduate/365/criminal-justice-and-criminology',
        'https://www.kent.ac.uk/courses/undergraduate/198/cultural-studies-and-comparative-literature',
        'https://www.kent.ac.uk/courses/undergraduate/154/cultural-studies-and-film',
        'https://www.kent.ac.uk/courses/undergraduate/878/digital-arts-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/115/digital-arts-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/1908/cultural-studies-and-media-with-journalism',
        'https://www.kent.ac.uk/courses/undergraduate/110/digital-arts',
        'https://www.kent.ac.uk/courses/undergraduate/876/digital-arts',
        'https://www.kent.ac.uk/courses/undergraduate/1382/cultural-studies-and-media',
        'https://www.kent.ac.uk/courses/undergraduate/156/cultural-studies-and-social-anthropology',
        'https://www.kent.ac.uk/courses/undergraduate/1907/cultural-studies-media-and-journalism',
        'https://www.kent.ac.uk/courses/undergraduate/163/drama-and-english-and-american-literature',
        'https://www.kent.ac.uk/courses/undergraduate/1917/history-and-philosophy-of-art-and-drama',
        'https://www.kent.ac.uk/courses/undergraduate/109/economics',
        'https://www.kent.ac.uk/courses/undergraduate/292/drama-and-english-language-and-linguistics',
        'https://www.kent.ac.uk/courses/undergraduate/114/drama-and-theatre',
        'https://www.kent.ac.uk/courses/undergraduate/1941/economics-and-management',
        'https://www.kent.ac.uk/courses/undergraduate/113/economics-with-econometrics',
        'https://www.kent.ac.uk/courses/undergraduate/218/electronic-and-communications-engineering-meng',
        'https://www.kent.ac.uk/courses/undergraduate/180/economics-and-politics',
        'https://www.kent.ac.uk/courses/undergraduate/212/electronic-and-communications-engineering-beng',
        'https://www.kent.ac.uk/courses/undergraduate/224/electronic-and-communications-engineering-with-a-year-in-industry-meng',
        'https://www.kent.ac.uk/courses/undergraduate/112/economics-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/217/electronic-and-communications-engineering-with-a-foundation-year-beng',
        'https://www.kent.ac.uk/courses/undergraduate/215/electronic-and-communications-engineering-with-a-year-in-industry-beng',
        'https://www.kent.ac.uk/courses/undergraduate/225/electronic-and-computer-systems',
        'https://www.kent.ac.uk/courses/undergraduate/318/english-american-and-postcolonial-literature-and-film',
        'https://www.kent.ac.uk/courses/undergraduate/140/english-american-and-postcolonial-literatures',
        'https://www.kent.ac.uk/courses/undergraduate/139/english-american-and-postcolonial-literatures-with-an-approved-year-abroad',
        'https://www.kent.ac.uk/courses/undergraduate/117/english-and-american-literature',
        'https://www.kent.ac.uk/courses/undergraduate/132/english-and-american-literature-and-creative-writing',
        'https://www.kent.ac.uk/courses/undergraduate/136/english-and-american-literature-and-creative-writing-with-an-approved-year-abroad',
        'https://www.kent.ac.uk/courses/undergraduate/138/english-and-american-literature-with-an-approved-year-abroad',
        'https://www.kent.ac.uk/courses/undergraduate/898/english-and-american-literature-and-journalism',
        'https://www.kent.ac.uk/courses/undergraduate/311/hispanic-studies-and-english-and-american-literature',
        'https://www.kent.ac.uk/courses/undergraduate/213/english-and-french-law',
        'https://www.kent.ac.uk/courses/undergraduate/366/english-and-american-literature-and-film',
        'https://www.kent.ac.uk/courses/undergraduate/251/english-and-american-literature-and-sociology',
        'https://www.kent.ac.uk/courses/undergraduate/1914/management-english-language-and-linguistics',
        'https://www.kent.ac.uk/courses/undergraduate/63/environmental-social-science',
        'https://www.kent.ac.uk/courses/undergraduate/88/english-language-and-linguistics',
        'https://www.kent.ac.uk/courses/undergraduate/305/english-language-and-linguistics-and-english-and-american-literature',
        'https://www.kent.ac.uk/courses/undergraduate/211/european-legal-studies',
        'https://www.kent.ac.uk/courses/undergraduate/391/environmental-social-science-with-a-year-in-professional-practice',
        'https://www.kent.ac.uk/courses/undergraduate/99/film',
        'https://www.kent.ac.uk/courses/undergraduate/125/european-studies-humanities-combined-languages',
        'https://www.kent.ac.uk/courses/undergraduate/122/european-studies-humanities-french',
        'https://www.kent.ac.uk/courses/undergraduate/1388/european-studies-humanities-spanish-or-italian',
        'https://www.kent.ac.uk/courses/undergraduate/1387/european-studies-humanities-spanish-or-italian',
        'https://www.kent.ac.uk/courses/undergraduate/133/european-studies-humanities-german',
        'https://www.kent.ac.uk/courses/undergraduate/165/film-and-drama',
        'https://www.kent.ac.uk/courses/undergraduate/863/financial-mathematics-with-year-industry',
        'https://www.kent.ac.uk/courses/undergraduate/102/film-with-a-placement-year',
        'https://www.kent.ac.uk/courses/undergraduate/101/film-with-a-year-abroad',
        'https://www.kent.ac.uk/courses/undergraduate/2495/finance-and-investment-with-year-industry',
        'https://www.kent.ac.uk/courses/undergraduate/126/financial-economics',
        'https://www.kent.ac.uk/courses/undergraduate/127/financial-economics-with-econometrics',
        'https://www.kent.ac.uk/courses/undergraduate/153/financial-mathematics',
        'https://www.kent.ac.uk/courses/undergraduate/74/forensic-science-msci',
        'https://www.kent.ac.uk/courses/undergraduate/73/forensic-science-bsc',
        'https://www.kent.ac.uk/courses/undergraduate/76/forensic-science-with-a-foundation-year',
        'https://www.kent.ac.uk/courses/undergraduate/77/forensic-science-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/98/french',
        'https://www.kent.ac.uk/courses/undergraduate/312/french-and-english-language-and-linguistics',
        'https://www.kent.ac.uk/courses/undergraduate/338/french-and-hispanic-studies',
        'https://www.kent.ac.uk/courses/undergraduate/336/french-and-philosophy',
        'https://www.kent.ac.uk/courses/undergraduate/306/french-and-english-and-american-literature',
        'https://www.kent.ac.uk/courses/undergraduate/371/german',
        'https://www.kent.ac.uk/courses/undergraduate/328/german-and-french',
        'https://www.kent.ac.uk/courses/undergraduate/329/french-and-history',
        'https://www.kent.ac.uk/courses/undergraduate/1909/french-and-management',
        'https://www.kent.ac.uk/courses/undergraduate/341/german-and-history',
        'https://www.kent.ac.uk/courses/undergraduate/319/german-and-english-language-and-linguistics',
        'https://www.kent.ac.uk/courses/undergraduate/107/hispanic-studies',
        'https://www.kent.ac.uk/courses/undergraduate/241/health-and-social-care',
        'https://www.kent.ac.uk/courses/undergraduate/1910/german-and-management',
        'https://www.kent.ac.uk/courses/undergraduate/356/hispanic-studies-and-italian',
        'https://www.kent.ac.uk/courses/undergraduate/219/hispanic-studies-and-english-language-and-linguistics',
        'https://www.kent.ac.uk/courses/undergraduate/3111/global-philosophies',
        'https://www.kent.ac.uk/courses/undergraduate/374/german-and-philosophy',
        'https://www.kent.ac.uk/courses/undergraduate/207/hispanic-studies-and-german',
        'https://www.kent.ac.uk/courses/undergraduate/1913/hispanic-studies-and-management',
        'https://www.kent.ac.uk/courses/undergraduate/361/hispanic-studies-and-history',
        'https://www.kent.ac.uk/courses/undergraduate/288/history-and-film',
        'https://www.kent.ac.uk/courses/undergraduate/304/history-and-drama',
        'https://www.kent.ac.uk/courses/undergraduate/85/history',
        'https://www.kent.ac.uk/courses/undergraduate/316/history-and-english-american-and-postcolonial-literatures',
        'https://www.kent.ac.uk/courses/undergraduate/363/history-and-english-language-and-linguistics',
        'https://www.kent.ac.uk/courses/undergraduate/296/history-and-philosophy',
        'https://www.kent.ac.uk/courses/undergraduate/287/history-and-english-and-american-literature',
        'https://www.kent.ac.uk/courses/undergraduate/301/history-and-social-anthropology',
        'https://www.kent.ac.uk/courses/undergraduate/2532/human-geography',
        'https://www.kent.ac.uk/courses/undergraduate/3105/human-geography-professional-practice',
        'https://www.kent.ac.uk/courses/undergraduate/299/history-and-religious-studies',
        'https://www.kent.ac.uk/courses/undergraduate/866/international-business-with-a-year-abroad-bsc',
        'https://www.kent.ac.uk/courses/undergraduate/867/international-business-with-a-year-in-industry-bsc',
        'https://www.kent.ac.uk/courses/undergraduate/880/international-foundation-programme-biosciences',
        'https://www.kent.ac.uk/courses/undergraduate/865/international-business-bsc',
        'https://www.kent.ac.uk/courses/undergraduate/297/history-and-politics',
        'https://www.kent.ac.uk/courses/undergraduate/883/international-foundation-programme-humanities',
        'https://www.kent.ac.uk/courses/undergraduate/881/international-foundation-programme-computer-science',
        'https://www.kent.ac.uk/courses/undergraduate/886/international-foundation-programme-social-sciences-sept',
        'https://www.kent.ac.uk/courses/undergraduate/885/international-foundation-programme-social-sciences-jan',
        'https://www.kent.ac.uk/courses/undergraduate/855/international-legal-studies-with-year-abroad',
        'https://www.kent.ac.uk/courses/undergraduate/108/italian',
        'https://www.kent.ac.uk/courses/undergraduate/220/italian-and-english-language-and-linguistics',
        'https://www.kent.ac.uk/courses/undergraduate/367/italian-and-french',
        'https://www.kent.ac.uk/courses/undergraduate/342/italian-and-german',
        'https://www.kent.ac.uk/courses/undergraduate/1911/italian-and-management',
        'https://www.kent.ac.uk/courses/undergraduate/105/journalism',
        'https://www.kent.ac.uk/courses/undergraduate/322/law-and-accounting-and-finance',
        'https://www.kent.ac.uk/courses/undergraduate/362/italian-and-history',
        'https://www.kent.ac.uk/courses/undergraduate/326/law-and-criminology',
        'https://www.kent.ac.uk/courses/undergraduate/327/law-and-economics',
        'https://www.kent.ac.uk/courses/undergraduate/1921/law-and-management',
        'https://www.kent.ac.uk/courses/undergraduate/177/law',
        'https://www.kent.ac.uk/courses/undergraduate/332/law-and-history',
        'https://www.kent.ac.uk/courses/undergraduate/192/law-with-a-language-french',
        'https://www.kent.ac.uk/courses/undergraduate/333/law-and-philosophy',
        'https://www.kent.ac.uk/courses/undergraduate/1386/law-senior-status',
        'https://www.kent.ac.uk/courses/undergraduate/330/law-and-english-literature',
        'https://www.kent.ac.uk/courses/undergraduate/334/law-and-social-anthropology',
        'https://www.kent.ac.uk/courses/undergraduate/335/law-and-sociology',
        'https://www.kent.ac.uk/courses/undergraduate/1892/law-with-quantitative-research',
        'https://www.kent.ac.uk/courses/undergraduate/193/law-with-a-language-german',
        'https://www.kent.ac.uk/courses/undergraduate/261/liberal-arts',
        'https://www.kent.ac.uk/courses/undergraduate/869/marketing-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/1399/management',
        'https://www.kent.ac.uk/courses/undergraduate/868/marketing-bsc',
        'https://www.kent.ac.uk/courses/undergraduate/1398/management-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/199/law-with-a-language-spanish',
        'https://www.kent.ac.uk/courses/undergraduate/161/mathematics',
        'https://www.kent.ac.uk/courses/undergraduate/205/mathematics-and-accounting-and-finance',
        'https://www.kent.ac.uk/courses/undergraduate/164/mathematics-and-statistics',
        'https://www.kent.ac.uk/courses/undergraduate/891/mathematics-and-statistics-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/166/mathematics-including-a-foundation-year',
        'https://www.kent.ac.uk/courses/undergraduate/890/mathematics-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/270/mathematics-and-secondary-educations-qts-joint-programme-with-canterbury-christ-church-university',
        'https://www.kent.ac.uk/courses/undergraduate/385/mathematics',
        'https://www.kent.ac.uk/courses/undergraduate/2504/music-performance-production',
        'https://www.kent.ac.uk/courses/undergraduate/227/multimedia-technology-and-design-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/1901/media-studies',
        'https://www.kent.ac.uk/courses/undergraduate/1906/media-studies-with-an-approved-year-abroad',
        'https://www.kent.ac.uk/courses/undergraduate/226/multimedia-technology-and-design',
        'https://www.kent.ac.uk/courses/undergraduate/90/military-history',
        'https://www.kent.ac.uk/courses/undergraduate/2505/music-business-production',
        'https://www.kent.ac.uk/courses/undergraduate/18/pharmacy',
        'https://www.kent.ac.uk/courses/undergraduate/2503/music-technology-audio-production',
        'https://www.kent.ac.uk/courses/undergraduate/1397/pharmacology-and-physiology-with-integrated-foundation-year',
        'https://www.kent.ac.uk/courses/undergraduate/386/pharmacology-and-physiology',
        'https://www.kent.ac.uk/courses/undergraduate/20/philosophy',
        'https://www.kent.ac.uk/courses/undergraduate/353/philosophy-and-english-language-and-linguistics',
        'https://www.kent.ac.uk/courses/undergraduate/323/philosophy-and-film',
        'https://www.kent.ac.uk/courses/undergraduate/21/philosophy-with-an-approved-year-abroad',
        'https://www.kent.ac.uk/courses/undergraduate/1916/philosophy-and-art-history',
        'https://www.kent.ac.uk/courses/undergraduate/309/philosophy-and-english-and-american-literature',
        'https://www.kent.ac.uk/courses/undergraduate/1912/philosophy-and-management',
        'https://www.kent.ac.uk/courses/undergraduate/22/physics-bsc',
        'https://www.kent.ac.uk/courses/undergraduate/23/physics-mphys',
        'https://www.kent.ac.uk/courses/undergraduate/27/physics-with-astrophysics-mphys',
        'https://www.kent.ac.uk/courses/undergraduate/24/physics-with-a-foundation-year',
        'https://www.kent.ac.uk/courses/undergraduate/25/physics-with-a-year-abroad-mphys',
        'https://www.kent.ac.uk/courses/undergraduate/893/physics-with-a-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/352/philosophy-and-politics',
        'https://www.kent.ac.uk/courses/undergraduate/349/philosophy-and-sociology',
        'https://www.kent.ac.uk/courses/undergraduate/26/physics-with-astrophysics-bsc',
        'https://www.kent.ac.uk/courses/undergraduate/28/physics-with-astrophysics-with-a-year-in-the-usa-mphys',
        'https://www.kent.ac.uk/courses/undergraduate/2526/physics-astrophysics-year-industry',
        'https://www.kent.ac.uk/courses/undergraduate/29/politics',
        'https://www.kent.ac.uk/courses/undergraduate/31/politics-and-international-relations',
        'https://www.kent.ac.uk/courses/undergraduate/33/politics-and-international-relations-bidiplome',
        'https://www.kent.ac.uk/courses/undergraduate/390/',
        'https://www.kent.ac.uk/courses/undergraduate/40/politics-and-international-relations-with-a-year-in-continental-europe',
        'https://www.kent.ac.uk/courses/undergraduate/393/politics-and-international-relations-with-a-year-in-north-america',
        'https://www.kent.ac.uk/courses/undergraduate/2494/politics-and-international-relations-with-a-year-in-asia-pacific',
        'https://www.kent.ac.uk/courses/undergraduate/1390/politics-and-international-relations-with-quantitative-research',
        'https://www.kent.ac.uk/courses/undergraduate/194/politics-and-law',
        'https://www.kent.ac.uk/courses/undergraduate/842/positive-behaviour-support',
        'https://www.kent.ac.uk/courses/undergraduate/2530/positive-behaviour-support',
        'https://www.kent.ac.uk/courses/undergraduate/49/psychology',
        'https://www.kent.ac.uk/courses/undergraduate/2528/psychology-placement-year',
        'https://www.kent.ac.uk/courses/undergraduate/50/psychology-with-clinical-psychology',
        'https://www.kent.ac.uk/courses/undergraduate/2529/psychology-clinical-psychology-placement-year',
        'https://www.kent.ac.uk/courses/undergraduate/1389/psychology-with-forensic-psychology',
        'https://www.kent.ac.uk/courses/undergraduate/52/psychology-with-studies-in-europe',
        'https://www.kent.ac.uk/courses/undergraduate/54/religious-studies',
        'https://www.kent.ac.uk/courses/undergraduate/351/religious-studies-and-philosophy',
        'https://www.kent.ac.uk/courses/undergraduate/55/social-anthropology',
        'https://www.kent.ac.uk/courses/undergraduate/152/social-anthropology-and-social-policy',
        'https://www.kent.ac.uk/courses/undergraduate/2490/social-anthropology-with-a-year-abroad',
        'https://www.kent.ac.uk/courses/undergraduate/1954/social-anthropology-year-in-professional-practice',
        'https://www.kent.ac.uk/courses/undergraduate/57/social-anthropology-with-french',
        'https://www.kent.ac.uk/courses/undergraduate/310/religious-studies-and-english-and-american-literature',
        'https://www.kent.ac.uk/courses/undergraduate/151/social-anthropology-and-politics',
        'https://www.kent.ac.uk/courses/undergraduate/60/social-anthropology-with-german',
        'https://www.kent.ac.uk/courses/undergraduate/61/social-anthropology-with-italian',
        'https://www.kent.ac.uk/courses/undergraduate/62/social-anthropology-with-spanish',
        'https://www.kent.ac.uk/courses/undergraduate/65/social-policy',
        'https://www.kent.ac.uk/courses/undergraduate/1375/social-policy-with-quantitative-research',
        'https://www.kent.ac.uk/courses/undergraduate/51/social-psychology',
        'https://www.kent.ac.uk/courses/undergraduate/149/social-policy-and-politics',
        'https://www.kent.ac.uk/courses/undergraduate/359/sociology-and-social-policy',
        'https://www.kent.ac.uk/courses/undergraduate/66/social-sciences',
        'https://www.kent.ac.uk/courses/undergraduate/250/social-work',
        'https://www.kent.ac.uk/courses/undergraduate/3120/sport-and-exercise-for-health-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/146/sociology-and-social-anthropology',
        'https://www.kent.ac.uk/courses/undergraduate/245/sociology',
        'https://www.kent.ac.uk/courses/undergraduate/343/sociology-and-economics',
        'https://www.kent.ac.uk/courses/undergraduate/1373/sociology-with-quantitative-research',
        'https://www.kent.ac.uk/courses/undergraduate/188/sport-and-exercise-for-health',
        'https://www.kent.ac.uk/courses/undergraduate/171/sport-and-exercise-science',
        'https://www.kent.ac.uk/courses/undergraduate/1385/sport-management',
        'https://www.kent.ac.uk/courses/undergraduate/3121/sport-management-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/344/sociology-and-politics',
        'https://www.kent.ac.uk/courses/undergraduate/3122/sport-and-exercise-science-year-in-industry',
        'https://www.kent.ac.uk/courses/undergraduate/392/wildlife-conservation-with-a-year-in-professional-practice',
        'https://www.kent.ac.uk/courses/undergraduate/394/world-literature',
        'https://www.kent.ac.uk/courses/undergraduate/2512/sports-therapy-rehabilitation',
        'https://www.kent.ac.uk/courses/undergraduate/30/wildlife-conservation',
        'https://www.kent.ac.uk/courses/undergraduate/14/war-and-conflict'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Kent'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.degree_type
        degree_type = 1

        #4.programme_en
        programme_en = response.xpath('//*[@id="main_content"]/div[1]/div/div[2]/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        programme_en = programme_en.strip().replace('&amp; ','')
        # print(programme_en)


        #5.degree_name
        degree_name_a = re.findall('-[\s()A-Za-z]+',programme_en)
        if len(degree_name_a)==1:
            degree_name = degree_name_a[0]
            degree_name = degree_name.replace('-','').replace('(Hons)','').strip()
        elif len(degree_name_a)==2:
            degree_name = ''.join(degree_name_a)
            if 'BA' in degree_name:
                degree_name = 'BA'
            elif 'MArch' in degree_name:
                degree_name = 'MArch'
            elif 'BEng' in degree_name:
                degree_name = 'BEng'
            else:
                degree_name = 'Credit'
        else:degree_name = degree_name_a
        # print(degree_name)
        programme_en = re.findall(r'^[A-Za-z\s(),]+-', programme_en)[0]
        programme_en = programme_en.replace('-','').strip()
        # print(programme_en)

        #6.location
        location = response.xpath('//*[@id="main_content"]/div[2]/div[1]/div/div[2]/div[1]/span/a').extract()
        location = ','.join(location)
        location = remove_tags(location).strip()
        # print(location)

        #7.overview_en
        overview_en = response.xpath('//*[@id="overview"]/*[position()<4]').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #8.duration
        duration = response.xpath("//*[contains(text(),'Duration')]//following-sibling::ul//li").extract()
        duration = ','.join(duration)
        duration = remove_tags(duration)
        if ',' in duration:
            duration = re.findall(r'(.*),',duration)[0]
        # print(duration)

        #9.ucascode
        ucascode = response.xpath('//*[@id="main_content"]/div[1]/div/div[2]/p').extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode).replace('UCAS code','').strip()
        # print(ucascode)

        #10.department
        department = response.xpath("//*[contains(text(),'Subject website')]//following-sibling::ul//li").extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #11.modules_en
        modules_en = response.xpath('//*[@id="structure"]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #12.assessment_en
        assessment_en = response.xpath('//*[@id="teaching"]').extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #13.career_en
        career_en = response.xpath('//*[@id="careers"]').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #14.alevel
        alevel = response.xpath("//*[contains(text(),'A level')]//following-sibling::td").extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel).strip()
        # print(alevel)

        #15.ib
        ib = response.xpath("//*[contains(text(),'International Baccalaureate')]//following-sibling::td").extract()
        ib = ''.join(ib)
        ib = remove_tags(ib).strip()
        # print(ib)

        #16.ielts 17181920  21.toefl 22232425
        if 'L508' in ucascode:
            ielts = 7.0
            ielts_r = 6.5
            ielts_s = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
            toefl = 95
            toefl_r = 25
            toefl_l = 22
            toefl_s = 24
            toefl_w = 24
        elif 'G108' in ucascode:
            ielts = 5.5
            ielts_r = 5.5
            ielts_s = 5.5
            ielts_w = 5.5
            ielts_l = 5.5
            toefl = 72
            toefl_r = 18
            toefl_l = 17
            toefl_s = 20
            toefl_w = 17
        elif 'F412' in ucascode:
            ielts = 5.5
            ielts_r = 5.5
            ielts_s = 5.5
            ielts_w = 5.5
            ielts_l = 5.5
            toefl = 72
            toefl_r = 18
            toefl_l = 17
            toefl_s = 20
            toefl_w = 17
        elif 'F105' in ucascode:
            ielts = 5.5
            ielts_r = 5.5
            ielts_s = 5.5
            ielts_w = 5.5
            ielts_l = 5.5
            toefl = 72
            toefl_r = 18
            toefl_l = 17
            toefl_s = 20
            toefl_w = 17
        elif 'F305' in ucascode:
            ielts = 5.5
            ielts_r = 5.5
            ielts_s = 5.5
            ielts_w = 5.5
            ielts_l = 5.5
            toefl = 72
            toefl_r = 18
            toefl_l = 17
            toefl_s = 20
            toefl_w = 17
        elif 'H614' in ucascode:
            ielts = 5.5
            ielts_r = 5.5
            ielts_s = 5.5
            ielts_w = 5.5
            ielts_l = 5.5
            toefl = 72
            toefl_r = 18
            toefl_l = 17
            toefl_s = 20
            toefl_w = 17
        elif 'H605' in ucascode:
            ielts = 5.5
            ielts_r = 5.5
            ielts_s = 5.5
            ielts_w = 5.5
            ielts_l = 5.5
            toefl = 72
            toefl_r = 18
            toefl_l = 17
            toefl_s = 20
            toefl_w = 17
        elif 'L593' in ucascode:
            ielts = 5.0
            ielts_r = 5.0
            ielts_s = 5.0
            ielts_w = 5.0
            ielts_l = 5.0
            toefl = None
            toefl_r = None
            toefl_l = None
            toefl_s = None
            toefl_w = None
        elif 'L592' in ucascode:
            ielts = 5.0
            ielts_r = 5.0
            ielts_s = 5.0
            ielts_w = 5.0
            ielts_l = 5.0
            toefl = None
            toefl_r = None
            toefl_l = None
            toefl_s = None
            toefl_w = None
        elif 'Q308' in ucascode:
            ielts = 5.0
            ielts_r = 5.0
            ielts_s = 5.0
            ielts_w = 5.0
            ielts_l = 5.0
            toefl = None
            toefl_r = None
            toefl_l = None
            toefl_s = None
            toefl_w = None
        elif 'KW11' in ucascode:
            ielts = 5.0
            ielts_r = 5.0
            ielts_s = 5.0
            ielts_w = 5.0
            ielts_l = 5.0
            toefl = None
            toefl_r = None
            toefl_l = None
            toefl_s = None
            toefl_w = None
        elif '45NC' in ucascode:
            ielts = 5.0
            ielts_r = 5.0
            ielts_s = 5.0
            ielts_w = 5.0
            ielts_l = 5.0
            toefl = None
            toefl_r = None
            toefl_l = None
            toefl_s = None
            toefl_w = None
        elif 'C107' in ucascode:
            ielts = 5.0
            ielts_r = 5.0
            ielts_s = 5.0
            ielts_w = 5.0
            ielts_l = 5.0
            toefl = None
            toefl_r = None
            toefl_l = None
            toefl_s = None
            toefl_w = None
        elif 'G408' in ucascode:
            ielts = 5.0
            ielts_r = 5.0
            ielts_s = 5.0
            ielts_w = 5.0
            ielts_l = 5.0
            toefl = None
            toefl_r = None
            toefl_l = None
            toefl_s = None
            toefl_w = None
        else:
            ielts = 6.5
            ielts_r = 6.0
            ielts_s = 5.5
            ielts_w = 6.0
            ielts_l = 5.5
            toefl = 90
            toefl_r = 22
            toefl_l = 17
            toefl_s = 20
            toefl_w = 21

        #26.tuition_fee
        tuition_fee = response.xpath('//*[@id="funding"]/table/tbody/tr/td[3]').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        try:
            tuition_fee = re.findall(r'\d{5}',tuition_fee)[0]
        except:
            tuition_fee = None
        # print(tuition_fee)


        #27.apply_proces_en
        apply_proces_en = 'https://www.ucas.com/students'
        #28.start_date
        start_date = response.xpath("//*[contains(text(),'Start date')]").extract()
        start_date = ''.join(start_date)
        start_date = clear_space_str(start_date)
        print(start_date)
        item['university'] = university
        item['url'] = url
        item['degree_type'] = degree_type
        item['programme_en'] = programme_en
        item['degree_name'] = degree_name
        item['location'] = location
        item['overview_en'] = overview_en
        item['duration'] = duration
        item['ucascode'] = ucascode
        item['department'] = department
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['alevel'] = alevel
        item['ib'] = ib
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['toefl'] = toefl
        item['toefl_w'] = toefl_w
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['tuition_fee'] = tuition_fee
        item['apply_proces_en'] = apply_proces_en
        # yield item