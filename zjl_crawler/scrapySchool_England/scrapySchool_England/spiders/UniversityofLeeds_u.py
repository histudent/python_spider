# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/24 17:50'
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
class UniversityofLeedsSpider(scrapy.Spider):
    name = 'UniversityofLeeds_u'
    allowed_domains = ['leeds.ac.uk/']
    start_urls = []
    C= ['https://courses.leeds.ac.uk/g259/biology-mbiol-bsc',
'https://courses.leeds.ac.uk/f429/medicinal-chemistry-with-a-year-in-industry-mchem-bsc',
'https://courses.leeds.ac.uk/g266/microbiology-mbiol-bsc',
'https://courses.leeds.ac.uk/g266/microbiology-mbiol-bsc',
'https://courses.leeds.ac.uk/g269/neuroscience-mbiol-bsc',
'https://courses.leeds.ac.uk/g269/neuroscience-mbiol-bsc',
'https://courses.leeds.ac.uk/f425/chemistry-with-study-abroad-mchem-bsc',
'https://courses.leeds.ac.uk/f423/chemistry-with-a-year-in-industry-mchem-bsc',
'https://courses.leeds.ac.uk/f416/architectural-engineering-meng-beng',
'https://courses.leeds.ac.uk/f416/architectural-engineering-meng-beng',
'https://courses.leeds.ac.uk/f414/aeronautical-and-aerospace-engineering-meng-beng',
'https://courses.leeds.ac.uk/f414/aeronautical-and-aerospace-engineering-meng-beng',
'https://courses.leeds.ac.uk/g273/zoology-mbiol-bsc',
'https://courses.leeds.ac.uk/g273/zoology-mbiol-bsc',
'https://courses.leeds.ac.uk/f422/chemistry-mchem-bsc',
'https://courses.leeds.ac.uk/i208/medicinal-chemistry-with-study-abroad-mchem-bsc',
'https://courses.leeds.ac.uk/f413/automotive-engineering-meng-beng',
'https://courses.leeds.ac.uk/f413/automotive-engineering-meng-beng',
'https://courses.leeds.ac.uk/g656/product-design-mdes-bsc',
'https://courses.leeds.ac.uk/g656/product-design-mdes-bsc',
'https://courses.leeds.ac.uk/g800/architecture-meng-beng',
'https://courses.leeds.ac.uk/f428/medicinal-chemistry-mchem-bsc',
'https://courses.leeds.ac.uk/f463/chemical-engineering-meng-beng',
'https://courses.leeds.ac.uk/f463/chemical-engineering-meng-beng',
'https://courses.leeds.ac.uk/i445/civil-engineering-meng-beng',
'https://courses.leeds.ac.uk/i445/civil-engineering-meng-beng',
'https://courses.leeds.ac.uk/f234/chemical-and-energy-engineering-meng-beng',
'https://courses.leeds.ac.uk/f234/chemical-and-energy-engineering-meng-beng',
'https://courses.leeds.ac.uk/f237/chemical-and-materials-engineering-meng-beng',
'https://courses.leeds.ac.uk/f237/chemical-and-materials-engineering-meng-beng',
'https://courses.leeds.ac.uk/f456/electronic-and-electrical-engineering-meng-beng',
'https://courses.leeds.ac.uk/f456/electronic-and-electrical-engineering-meng-beng',
'https://courses.leeds.ac.uk/f411/mechanical-engineering-meng-beng',
'https://courses.leeds.ac.uk/f411/mechanical-engineering-meng-beng',
'https://courses.leeds.ac.uk/f457/electronics-and-computer-engineering-meng-beng',
'https://courses.leeds.ac.uk/f457/electronics-and-computer-engineering-meng-beng',
'https://courses.leeds.ac.uk/f455/electronic-and-communications-engineering-meng-beng',
'https://courses.leeds.ac.uk/f455/electronic-and-communications-engineering-meng-beng',
'https://courses.leeds.ac.uk/f543/mechatronics-and-robotics-meng-beng',
'https://courses.leeds.ac.uk/f543/mechatronics-and-robotics-meng-beng',
'https://courses.leeds.ac.uk/f447/medical-engineering-meng-beng',
'https://courses.leeds.ac.uk/f447/medical-engineering-meng-beng',
'https://courses.leeds.ac.uk/g032/petroleum-engineering-meng-beng',
'https://courses.leeds.ac.uk/g032/petroleum-engineering-meng-beng',
'https://courses.leeds.ac.uk/g736/applied-computer-science-meng-bsc',
'https://courses.leeds.ac.uk/g736/applied-computer-science-meng-bsc',
'https://courses.leeds.ac.uk/f443/civil-and-environmental-engineering-meng-beng',
'https://courses.leeds.ac.uk/f443/civil-and-environmental-engineering-meng-beng',
'https://courses.leeds.ac.uk/g734/computer-science-with-artificial-intelligence-meng-bsc',
'https://courses.leeds.ac.uk/g734/computer-science-with-artificial-intelligence-meng-bsc',
'https://courses.leeds.ac.uk/f412/civil-and-structural-engineering-meng-beng',
'https://courses.leeds.ac.uk/f412/civil-and-structural-engineering-meng-beng',
'https://courses.leeds.ac.uk/i069/computer-science-with-high-performance-graphics-and-games-engineering-meng-bsc',
'https://courses.leeds.ac.uk/g904/environment-and-business-international-menv-ba',
'https://courses.leeds.ac.uk/g005/sustainability-and-environmental-management-international-menv-bsc',
'https://courses.leeds.ac.uk/f454/electronic-engineering-meng-beng',
'https://courses.leeds.ac.uk/f454/electronic-engineering-meng-beng',
'https://courses.leeds.ac.uk/f433/geophysical-sciences-international-mgeophys-bsc',
'https://courses.leeds.ac.uk/f667/chemical-and-nuclear-engineering-meng-beng',
'https://courses.leeds.ac.uk/f667/chemical-and-nuclear-engineering-meng-beng',
'https://courses.leeds.ac.uk/f417/mathematics-mmath-bsc',
'https://courses.leeds.ac.uk/g275/electronics-and-renewable-energy-systems-meng-beng',
'https://courses.leeds.ac.uk/g275/electronics-and-renewable-energy-systems-meng-beng',
'https://courses.leeds.ac.uk/f919/computer-science-meng-bsc',
'https://courses.leeds.ac.uk/f919/computer-science-meng-bsc',
'https://courses.leeds.ac.uk/f418/geological-sciences-international-mgeol-bsc',
'https://courses.leeds.ac.uk/g230/mathematics-and-statistics-mmath-bsc',
'https://courses.leeds.ac.uk/f318/environmental-science-international-menv-bsc',
'https://courses.leeds.ac.uk/f874/meteorology-and-climate-science-international-menv-bsc',
'https://courses.leeds.ac.uk/f400/theoretical-physics-mphys-bsc',
'https://courses.leeds.ac.uk/f332/physics-mphys-bsc',
'https://courses.leeds.ac.uk/i259/nutrition-industrial-msci-bsc',
'https://courses.leeds.ac.uk/i257/food-science-and-nutrition-industrial-msci-bsc',
'https://courses.leeds.ac.uk/g883/sport-science-and-physiology-msci-bsc',
'https://courses.leeds.ac.uk/g883/sport-science-and-physiology-msci-bsc',
'https://courses.leeds.ac.uk/f334/physics-with-astrophysics-mphys-bsc',
'https://courses.leeds.ac.uk/i255/food-science-industrial-msci-bsc',
'https://courses.leeds.ac.uk/g882/sport-and-exercise-sciences-msci-bsc',
'https://courses.leeds.ac.uk/g882/sport-and-exercise-sciences-msci-bsc',
'https://courses.leeds.ac.uk/g492/advanced-psychology-mpsyc-bsc',
'https://courses.leeds.ac.uk/i477/business-management-and-the-human-resource-ba',
'https://courses.leeds.ac.uk/i256/food-science-and-nutrition-msci-bsc',
'https://courses.leeds.ac.uk/i475/business-management-ba',
'https://courses.leeds.ac.uk/i254/food-science-msci-bsc',
'https://courses.leeds.ac.uk/g675/ancient-history-and-english-ba',
'https://courses.leeds.ac.uk/4028/biology-and-history-and-philosophy-of-science-bsc',
'https://courses.leeds.ac.uk/f440/natural-sciences-bsc-mnatsc',
'https://courses.leeds.ac.uk/f440/natural-sciences-bsc-mnatsc',
'https://courses.leeds.ac.uk/g676/ancient-history-and-history-ba',
'https://courses.leeds.ac.uk/g678/ancient-history-and-philosophy-ba',
'https://courses.leeds.ac.uk/g521/studies-in-science-with-foundation-year-bsc',
'https://courses.leeds.ac.uk/631/arabic-and-japanese-ba',
'https://courses.leeds.ac.uk/g690/arabic-and-russian-a-ba',
'https://courses.leeds.ac.uk/e706/arabic-and-russian-b-ba',
'https://courses.leeds.ac.uk/710/arabic-and-portuguese-ba',
'https://courses.leeds.ac.uk/i476/business-management-with-marketing-ba',
'https://courses.leeds.ac.uk/i076/computer-science-with-mathematics-msci-bsc',
'https://courses.leeds.ac.uk/i258/nutrition-msci-bsc',
'https://courses.leeds.ac.uk/i076/computer-science-with-mathematics-msci-bsc',
'https://courses.leeds.ac.uk/773/asia-pacific-studies-and-politics-ba',
'https://courses.leeds.ac.uk/a851/arabic-and-middle-eastern-studies-ba',
'https://courses.leeds.ac.uk/e604/chinese-and-russian-a-ba',
'https://courses.leeds.ac.uk/g294/arts-and-humanities-with-foundation-year-ba',
'https://courses.leeds.ac.uk/632/arabic-and-chinese-ba',
'https://courses.leeds.ac.uk/665/arabic-and-islamic-studies-ba',
'https://courses.leeds.ac.uk/e022/asia-pacific-studies-and-international-relations-ba',
'https://courses.leeds.ac.uk/g116/asia-pacific-studies-international-ba',
'https://courses.leeds.ac.uk/g514/classical-civilisation-and-english-ba',
'https://courses.leeds.ac.uk/e880/asia-pacific-studies-ba',
'https://courses.leeds.ac.uk/0080/chinese-and-japanese-ba',
'https://courses.leeds.ac.uk/a467/environment-and-business-ba',
'https://courses.leeds.ac.uk/g308/chinese-and-thai-studies-ba',
'https://courses.leeds.ac.uk/f254/art-and-design-ba',
'https://courses.leeds.ac.uk/g517/classical-civilisation-and-philosophy-ba',
'https://courses.leeds.ac.uk/115/childhood-studies-ba',
'https://courses.leeds.ac.uk/830/chinese-and-portuguese-ba',
'https://courses.leeds.ac.uk/0778/asia-pacific-studies-and-chinese-ba',
'https://courses.leeds.ac.uk/861/classical-literature-and-french-ba',
'https://courses.leeds.ac.uk/0090/classical-civilisation-ba',
'https://courses.leeds.ac.uk/g581/classical-civilisation-and-history-ba',
'https://courses.leeds.ac.uk/f766/asia-pacific-studies-and-japanese-ba',
'https://courses.leeds.ac.uk/873/classical-literature-and-russian-b-ba',
'https://courses.leeds.ac.uk/e315/chinese-modern-ba',
'https://courses.leeds.ac.uk/0808/chinese-and-italian-b-ba',
'https://courses.leeds.ac.uk/g995/chinese-and-east-asian-religions-and-cultures-ba',
'https://courses.leeds.ac.uk/876/classical-literature-and-italian-b-ba',
'https://courses.leeds.ac.uk/g199/communication-and-media-ba',
'https://courses.leeds.ac.uk/a565/classical-literature-and-philosophy-ba',
'https://courses.leeds.ac.uk/e989/criminal-justice-and-criminology-ba',
'https://courses.leeds.ac.uk/950/economics-and-history-ba',
'https://courses.leeds.ac.uk/g856/digital-media-ba',
'https://courses.leeds.ac.uk/g674/english-and-comparative-literature-ba',
'https://courses.leeds.ac.uk/g971/education-ba',
'https://courses.leeds.ac.uk/850/chinese-and-russian-b-ba',
'https://courses.leeds.ac.uk/g996/east-asian-religions-and-cultures-and-japanese-ba',
'https://courses.leeds.ac.uk/g558/english-and-film-studies-ba',
'https://courses.leeds.ac.uk/g641/cultural-and-media-studies-ba',
'https://courses.leeds.ac.uk/990/economics-and-philosophy-ba',
'https://courses.leeds.ac.uk/g892/east-asian-religions-and-cultures-ba',
'https://courses.leeds.ac.uk/856/classical-literature-and-english-ba',
'https://courses.leeds.ac.uk/300/english-literature-and-theatre-studies-ba',
'https://courses.leeds.ac.uk/0930/economics-and-geography-ba',
'https://courses.leeds.ac.uk/290/english-language-and-literature-ba',
'https://courses.leeds.ac.uk/1150/english-and-music-ba',
'https://courses.leeds.ac.uk/g798/fashion-technology-ba',
'https://courses.leeds.ac.uk/1160/english-and-philosophy-ba',
'https://courses.leeds.ac.uk/f253/fashion-design-ba',
'https://courses.leeds.ac.uk/1100/english-and-history-ba',
'https://courses.leeds.ac.uk/g186/fashion-marketing-ba',
'https://courses.leeds.ac.uk/1217/english-and-social-policy-ba',
'https://courses.leeds.ac.uk/i438/english-literature-with-creative-writing-ba',
'https://courses.leeds.ac.uk/1220/english-and-sociology-ba',
'https://courses.leeds.ac.uk/g619/film-photography-and-media-ba',
'https://courses.leeds.ac.uk/g997/east-asian-religions-and-cultures-and-thai-studies-ba',
'https://courses.leeds.ac.uk/e134/fine-art-ba',
'https://courses.leeds.ac.uk/1238/english-and-theology-and-religious-studies-ba',
'https://courses.leeds.ac.uk/0330/geography-ba',
'https://courses.leeds.ac.uk/i301/english-and-environment-ba',
'https://courses.leeds.ac.uk/g153/english-literature-ba',
'https://courses.leeds.ac.uk/1380/geography-and-history-ba',
'https://courses.leeds.ac.uk/315/french-ba',
'https://courses.leeds.ac.uk/1440/geography-and-sociology-ba',
'https://courses.leeds.ac.uk/340/german-ba',
'https://courses.leeds.ac.uk/g864/geography-with-transport-studies-ba',
'https://courses.leeds.ac.uk/370/history-ba',
'https://courses.leeds.ac.uk/1110/english-and-history-of-art-ba',
'https://courses.leeds.ac.uk/f485/international-development-ba',
'https://courses.leeds.ac.uk/1630/history-and-philosophy-ba',
'https://courses.leeds.ac.uk/1581/history-and-history-and-philosophy-of-science-ba',
'https://courses.leeds.ac.uk/g642/fine-art-with-history-of-art-ba',
'https://courses.leeds.ac.uk/e190/graphic-and-communication-design-ba',
'https://courses.leeds.ac.uk/g644/fine-art-with-contemporary-cultural-theory-ba',
'https://courses.leeds.ac.uk/g645/history-of-art-with-cultural-studies-ba',
'https://courses.leeds.ac.uk/1570/history-and-history-of-art-ba',
'https://courses.leeds.ac.uk/380/history-of-art-ba',
'https://courses.leeds.ac.uk/1000/economics-and-politics-ba',
'https://courses.leeds.ac.uk/a850/islamic-studies-ba',
'https://courses.leeds.ac.uk/1685/history-and-social-policy-ba',
'https://courses.leeds.ac.uk/396/human-resource-management-ba',
'https://courses.leeds.ac.uk/1690/history-and-sociology-ba',
'https://courses.leeds.ac.uk/a753/international-relations-ba',
'https://courses.leeds.ac.uk/g326/english-language-and-linguistics-ba',
'https://courses.leeds.ac.uk/460/linguistics-and-phonetics-ba',
'https://courses.leeds.ac.uk/e169/history-and-philosophy-of-science-and-politics-ba',
'https://courses.leeds.ac.uk/429/italian-b-ba',
'https://courses.leeds.ac.uk/2101/history-of-art-and-philosophy-ba',
'https://courses.leeds.ac.uk/417/japanese-ba',
'https://courses.leeds.ac.uk/1620/history-and-music-ba',
'https://courses.leeds.ac.uk/a028/middle-eastern-studies-ba',
'https://courses.leeds.ac.uk/1632/history-and-philosophy-of-science-and-theology-and-religious-studies-ba',
'https://courses.leeds.ac.uk/g549/music-with-enterprise-ba',
'https://courses.leeds.ac.uk/g809/liberal-arts-ba',
'https://courses.leeds.ac.uk/g682/italian-b-and-portuguese-ba',
'https://courses.leeds.ac.uk/a004/music-ba',
'https://courses.leeds.ac.uk/2619/italian-b-and-russian-a-ba',
'https://courses.leeds.ac.uk/510/philosophy-ba',
'https://courses.leeds.ac.uk/1709/history-and-theology-and-religious-studies-ba',
'https://courses.leeds.ac.uk/e119/linguistics-and-philosophy-ba',
'https://courses.leeds.ac.uk/410/international-history-and-politics-ba',
'https://courses.leeds.ac.uk/e346/business-management-and-philosophy-ba',
'https://courses.leeds.ac.uk/g184/philosophy-ethics-and-religion-ba',
'https://courses.leeds.ac.uk/a571/middle-eastern-studies-and-politics-ba',
'https://courses.leeds.ac.uk/f767/russian-a-ba',
'https://courses.leeds.ac.uk/g923/liberal-arts-international-language-ba',
'https://courses.leeds.ac.uk/e596/italian-a-ba',
'https://courses.leeds.ac.uk/e030/italian-b-and-japanese-ba',
'https://courses.leeds.ac.uk/f552/politics-ba',
'https://courses.leeds.ac.uk/2111/philosophy-and-history-and-philosophy-of-science-ba',
'https://courses.leeds.ac.uk/g835/professional-studies-ba',
'https://courses.leeds.ac.uk/2179/philosophy-and-theology-and-religious-studies-ba',
'https://courses.leeds.ac.uk/i074/journalism-ba',
'https://courses.leeds.ac.uk/2170/philosophy-and-sociology-ba',
'https://courses.leeds.ac.uk/f768/russian-b-ba',
'https://courses.leeds.ac.uk/2120/philosophy-and-politics-ba',
'https://courses.leeds.ac.uk/f044/spanish-ba',
'https://courses.leeds.ac.uk/1845/japanese-and-russian-b-ba',
'https://courses.leeds.ac.uk/i158/teaching-english-to-speakers-of-other-languages-tesol-ba',
'https://courses.leeds.ac.uk/2060/music-and-philosophy-ba',
'https://courses.leeds.ac.uk/h971/social-work-ba',
'https://courses.leeds.ac.uk/g460/philosophy-politics-and-economics-ba',
'https://courses.leeds.ac.uk/580/sociology-ba',
'https://courses.leeds.ac.uk/e939/politics-and-sociology-ba',
'https://courses.leeds.ac.uk/f330/social-policy-and-crime-ba',
'https://courses.leeds.ac.uk/e605/japanese-and-russian-a-ba',
'https://courses.leeds.ac.uk/a926/social-science-ba',
'https://courses.leeds.ac.uk/e999/politics-and-social-policy-ba',
'https://courses.leeds.ac.uk/620/theology-and-religious-studies-ba',
'https://courses.leeds.ac.uk/g075/philosophy-psychology-and-scientific-thought-ba',
'https://courses.leeds.ac.uk/f075/social-policy-ba',
'https://courses.leeds.ac.uk/2430/social-policy-and-sociology-ba',
'https://courses.leeds.ac.uk/g727/thai-studies-ba',
'https://courses.leeds.ac.uk/2251/portuguese-and-russian-a-ba',
'https://courses.leeds.ac.uk/3390/geological-sciences-bsc',
'https://courses.leeds.ac.uk/2459/sociology-and-theology-and-religious-studies-ba',
'https://courses.leeds.ac.uk/i264/theatre-and-performance-with-enterprise-ba',
'https://courses.leeds.ac.uk/g560/religion-politics-and-society-ba',
'https://courses.leeds.ac.uk/3400/geophysical-sciences-bsc',
'https://courses.leeds.ac.uk/2261/portuguese-and-russian-b-ba',
'https://courses.leeds.ac.uk/3600/physics-with-astrophysics-bsc',
'https://courses.leeds.ac.uk/g779/social-policy-with-enterprise-ba',
'https://courses.leeds.ac.uk/3314/environmental-science-bsc',
'https://courses.leeds.ac.uk/2165/philosophy-and-social-policy-ba',
'https://courses.leeds.ac.uk/f834/accounting-and-finance-bsc',
'https://courses.leeds.ac.uk/a409/aviation-technology-and-management-bsc',
'https://courses.leeds.ac.uk/f252/textile-design-ba',
'https://courses.leeds.ac.uk/4187/chemistry-and-mathematics-bsc',
'https://courses.leeds.ac.uk/a410/aviation-technology-with-pilot-studies-bsc',
'https://courses.leeds.ac.uk/g986/banking-and-finance-bsc',
'https://courses.leeds.ac.uk/f869/economics-and-management-bsc',
'https://courses.leeds.ac.uk/g632/business-analytics-bsc',
'https://courses.leeds.ac.uk/4393/economics-and-mathematics-bsc',
'https://courses.leeds.ac.uk/f702/actuarial-mathematics-bsc',
'https://courses.leeds.ac.uk/f881/spanish-portuguese-and-latin-american-studies-ba',
'https://courses.leeds.ac.uk/3580/physics-bsc',
'https://courses.leeds.ac.uk/f104/geography-and-geology-bsc',
'https://courses.leeds.ac.uk/g150/business-studies-with-foundation-year-bsc',
'https://courses.leeds.ac.uk/e648/history-and-philosophy-of-science-and-physics-bsc',
'https://courses.leeds.ac.uk/a002/music-performance-bmus',
'https://courses.leeds.ac.uk/ap01/computer-science-digital-technology-solutions-bsc',
'https://courses.leeds.ac.uk/f833/international-business-and-finance-bsc',
'https://courses.leeds.ac.uk/3220/chemistry-bsc',
'https://courses.leeds.ac.uk/g295/international-business-and-marketing-bsc',
'https://courses.leeds.ac.uk/2229/politics-and-theology-and-religious-studies-ba',
'https://courses.leeds.ac.uk/i125/dental-hygiene-and-dental-therapy-bsc',
'https://courses.leeds.ac.uk/4039/biology-and-mathematics-bsc',
'https://courses.leeds.ac.uk/f835/business-economics-bsc',
'https://courses.leeds.ac.uk/4594/mathematics-and-music-bsc',
'https://courses.leeds.ac.uk/f836/economics-bsc',
'https://courses.leeds.ac.uk/g048/economics-and-finance-bsc',
'https://courses.leeds.ac.uk/i102/diagnostic-radiography-bsc',
'https://courses.leeds.ac.uk/4586/mathematics-and-philosophy-bsc',
'https://courses.leeds.ac.uk/g151/earth-and-environmental-sciences-with-foundation-year-bsc',
'https://courses.leeds.ac.uk/g414/food-science-and-nutrition-bsc',
'https://courses.leeds.ac.uk/a617/music-multimedia-and-electronics-bsc',
'https://courses.leeds.ac.uk/i104/healthcare-science-cardiac-physiology-bsc',
'https://courses.leeds.ac.uk/3380/geography-bsc',
'https://courses.leeds.ac.uk/i073/geography-with-environmental-mathematics-bsc',
'https://courses.leeds.ac.uk/f831/international-business-bsc',
'https://courses.leeds.ac.uk/3335/food-science-bsc',
'https://courses.leeds.ac.uk/4627/mathematics-and-statistics-bsc',
'https://courses.leeds.ac.uk/e651/philosophy-and-physics-bsc',
'https://courses.leeds.ac.uk/3440/mathematics-bsc',
'https://courses.leeds.ac.uk/f948/sociology-and-international-relations-ba',
'https://courses.leeds.ac.uk/3430/interdisciplinary-science-with-foundation-year-bsc',
'https://courses.leeds.ac.uk/i040/chemistry-and-mathematics-mchem-bsc',
'https://courses.leeds.ac.uk/f007/theatre-and-performance-ba',
'https://courses.leeds.ac.uk/e386/business-management-and-mathematics-bsc',
'https://courses.leeds.ac.uk/g139/financial-mathematics-bsc',
'https://courses.leeds.ac.uk/f986/civil-engineering-with-project-management-meng-beng',
'https://courses.leeds.ac.uk/3470/medical-microbiology-bsc',
'https://courses.leeds.ac.uk/f986/civil-engineering-with-project-management-meng-beng',
'https://courses.leeds.ac.uk/3497/medicinal-chemistry-bsc',
'https://courses.leeds.ac.uk/g602/law-with-french-law-llb',
'https://courses.leeds.ac.uk/i473/geography-and-business-management-ba',
'https://courses.leeds.ac.uk/h396/nursing-child-bsc',
'https://courses.leeds.ac.uk/i512/languages-cultures-and-history-ba',
'https://courses.leeds.ac.uk/h953/midwifery-bsc',
'https://courses.leeds.ac.uk/i514/languages-cultures-and-international-relations-ba',
'https://courses.leeds.ac.uk/3670/psychology-bsc',
'https://courses.leeds.ac.uk/i502/languages-and-cultures-ba',
'https://courses.leeds.ac.uk/h952/nursing-mental-health-bsc',
'https://courses.leeds.ac.uk/i518/languages-cultures-and-philosophy-ba',
'https://courses.leeds.ac.uk/g004/sustainability-and-environmental-management-bsc',
'https://courses.leeds.ac.uk/i510/languages-cultures-and-film-studies-ba',
'https://courses.leeds.ac.uk/h395/nursing-adult-bsc',
'https://courses.leeds.ac.uk/i506/languages-cultures-and-economics-ba',
'https://courses.leeds.ac.uk/f873/meteorology-and-climate-science-bsc',
'https://courses.leeds.ac.uk/i508/languages-cultures-and-english-ba',
'https://courses.leeds.ac.uk/i103/healthcare-science-audiology-bsc',
'https://courses.leeds.ac.uk/i057/civil-engineering-with-transport-meng-beng',
'https://courses.leeds.ac.uk/i057/civil-engineering-with-transport-meng-beng',
'https://courses.leeds.ac.uk/i504/languages-cultures-and-business-ba',
'https://courses.leeds.ac.uk/i520/languages-cultures-and-politics-ba',
'https://courses.leeds.ac.uk/3020/law-llb',
'https://courses.leeds.ac.uk/i516/languages-cultures-and-linguistics-ba',
'https://courses.leeds.ac.uk/i427/psychology-with-education-bsc',
'https://courses.leeds.ac.uk/g946/law-with-german-law-llb',
'https://courses.leeds.ac.uk/f666/nutrition-bsc',
'https://courses.leeds.ac.uk/i274/law-with-international-legal-studies-llb',
'https://courses.leeds.ac.uk/3010/law-llb',
'https://courses.leeds.ac.uk/5580/medicine-and-surgery-mbchb',
'https://courses.leeds.ac.uk/i273/law-with-european-legal-studies-llb',
'https://courses.leeds.ac.uk/g033/dental-surgery-mchd-bchd-oral-science-bsc-mchd-bchd-bsc',
'https://courses.leeds.ac.uk/g257/biochemistry-mbiol-bsc',
'https://courses.leeds.ac.uk/g257/biochemistry-mbiol-bsc',
'https://courses.leeds.ac.uk/g924/music-and-music-psychology-marts-ba',
'https://courses.leeds.ac.uk/3686/theoretical-physics-bsc',
'https://courses.leeds.ac.uk/i078/ecology-and-conservation-biology-mbiol-bsc',
'https://courses.leeds.ac.uk/i078/ecology-and-conservation-biology-mbiol-bsc',
'https://courses.leeds.ac.uk/g796/biology-with-enterprise-mbiol-bsc',
'https://courses.leeds.ac.uk/g796/biology-with-enterprise-mbiol-bsc',
'https://courses.leeds.ac.uk/g262/human-physiology-mbiol-bsc',
'https://courses.leeds.ac.uk/g262/human-physiology-mbiol-bsc',
'https://courses.leeds.ac.uk/g265/medical-sciences-mbiol-bsc',
'https://courses.leeds.ac.uk/g265/medical-sciences-mbiol-bsc',
'https://courses.leeds.ac.uk/g947/law-with-hispanic-law-llb',
'https://courses.leeds.ac.uk/g378/biological-sciences-biotechnology-with-enterprise-mbiol-bsc',
'https://courses.leeds.ac.uk/g378/biological-sciences-biotechnology-with-enterprise-mbiol-bsc',
'https://courses.leeds.ac.uk/g261/genetics-mbiol-bsc',
'https://courses.leeds.ac.uk/g261/genetics-mbiol-bsc',
'https://courses.leeds.ac.uk/g263/medical-biochemistry-mbiol-bsc',
'https://courses.leeds.ac.uk/g263/medical-biochemistry-mbiol-bsc',
'https://courses.leeds.ac.uk/g258/biological-sciences-mbiol-bsc',
'https://courses.leeds.ac.uk/g258/biological-sciences-mbiol-bsc',
'https://courses.leeds.ac.uk/g270/pharmacology-mbiol-bsc',
'https://courses.leeds.ac.uk/g270/pharmacology-mbiol-bsc',
'https://courses.leeds.ac.uk/g259/biology-mbiol-bsc']
    C = set(C)
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Leeds'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="main"]/div/header/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 1

        #5.degree_name
        degree_name_list = programme_en.split()
        degree_name = degree_name_list[-1]
        programme_en = programme_en.replace(degree_name,'').strip().replace(',','')
        # print(programme_en)
        # print(degree_name)

        #6.overview_en
        overview_en = response.xpath('//*[@id="acc1"]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #7.modules_en
        modules_en = response.xpath("//*[contains(text(),'Modules')]//following-sibling::*[position()<7]").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # end = modules_en.find()
        # modules_en = clear_space_str(modules_en)
        # print(modules_en)


        #8.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'Assessment')]//following-sibling::*").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = clear_space_str(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #9.start_date
        start_date = '2019-9'
        # print(start_date)

        #10.duration  #24.duration_per
        duration_list = response.xpath("//*[contains(text(),'Duration/Mode')]//following-sibling::*").extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        duration_list = clear_space_str(duration_list)
        # print(duration_list)
        try:
            duration = re.findall('\d+',duration_list)[0]
        except:
            duration = 3
        if int(duration)>10:
            duration_per = 3
        else:
            duration_per = 1
        # print(duration,'*******************',duration_per)

        #11.ucascode
        ucascode = response.xpath("//*[contains(text(),'UCAS code:')]//following-sibling::*").extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode)
        ucascode = clear_space_str(ucascode)
        # print(ucascode)

        #12.ielts 13141516
        ielts_list = response.xpath('//*[@id="acc3"]').extract()
        ielts_list = ''.join(ielts_list)
        ielts = re.findall(r'[567]\.\d',ielts_list)
        if len(ielts)>1:
            a = ielts[0]
            b = ielts[1]
            ielts = a
            ielts_r = b
            ielts_l = b
            ielts_w = b
            ielts_s = b
        elif len(ielts)==1:
            a = ielts[0]
            ielts = a
            ielts_r = a
            ielts_l = a
            ielts_w = a
            ielts_s = a
        else:
            ielts = None
            ielts_r = None
            ielts_l = None
            ielts_w = None
            ielts_s = None
        # print(ielts,ielts_w,ielts_s,ielts_r,ielts_l)
        # print(ielts_s+ielts_s)

        #17.department
        department =response.xpath("//*[contains(text(),'This course is taught by')]/../following-sibling::*").extract()
        department = ''.join(department)
        department = remove_tags(department)
        department = clear_space_str(department)
        # print(department)

        #18.alevel
        alevel = response.xpath('//*[@id="acc3"]/p[1]').extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel).replace('A-level:','').strip()
        # print(alevel)


        #19.tuition_fee
        tuition_fee= response.xpath('//*[@id="acc3"]').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = clear_space_str(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #20.tuition_fee_pre
        tuition_fee_pre = '£'

        #21.ib
        ib = response.xpath("//*[contains(text(),'International Baccalaureate')]//following-sibling::*").extract()
        try:
            ib = ib[-1]
            ib = remove_tags(ib)
        except:
            ib = 'N/A'
        # print(ib)

        #22.career_en
        career_en = response.xpath("//h2[contains(text(),'Career opportunities')]/../following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        career_en = clear_space_str(career_en)
        # print(career_en)

        #23.apply_proces_en
        apply_proces_en = 'https://application.leeds.ac.uk/login/?returnurl=%2f'
        #24.toefl 25262728
        toefl = 87
        toefl_l = 20
        toefl_r = 20
        toefl_s = 22
        toefl_w = 21
        #29.apply_pre
        apply_pre  = '£'
        #30.apply_documents_en
        apply_documents_en = '<p>Make sure you have all your supporting documents scanned and ready to upload with your online application. All documents should be in English, or sent with certified translations into English. Without copies of the required documents we will be unable to make you an offer.</p>'

        item['ib'] = ib
        item['alevel'] = alevel
        item['apply_pre'] = apply_pre
        item['apply_documents_en'] = apply_documents_en
        item['toefl'] = toefl
        item['toefl_l'] = toefl_l
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_w'] = toefl_w
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['start_date'] = start_date
        item['duration'] = duration
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['department'] = department
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['career_en'] = career_en
        item['apply_proces_en'] = apply_proces_en
        item['duration_per'] = duration_per

        ucascode_a = response.xpath("//*[contains(text(),'UCAS code:')]//following-sibling::span//text()").extract()
        if len(ucascode_a) >1:
            for i in ucascode_a:
                ucascode_list = i
                ucascode_list = ucascode_list.strip()
                ucascode_a = re.findall(r':(.*)',ucascode_list)[0].strip()
                degree_name_a = re.findall(r'(.*):',ucascode_list)[0].strip()
                item['ucascode'] = ucascode_a
                item['degree_name'] = degree_name_a
                yield  item

        else:
            item['ucascode'] = ucascode
            item['degree_name'] = degree_name
            yield item