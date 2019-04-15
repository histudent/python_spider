# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/26 9:11'
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
from scrapySchool_England.TranslateMonth import translate_month
from scrapySchool_England.clearSpace import clear_space
class UniversityofBathSpider(scrapy.Spider):

    name = 'UniversityofBath_u'
    allowed_domains = ['bath.ac.uk/']
    start_urls = []
    C= [
        'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-integrated-design-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-with-astrophysics-including-research-placement/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-sociology-and-social-policy-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-and-politics/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/business-and-management/bsc-business-administration-including-placements/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/modern-languages/ba-modern-languages-and-european-studies-spanish-and-ab-initio-italian-including-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-computer-systems-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/pharmacy/mpharm-pharmacy-including-integrated-pre-registration-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-electronic-engineering-with-space-science-and-technology/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-physics-with-astrophysics-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-social-policy/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/mmath-mathematics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/mchem-chemistry-for-drug-discovery-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-social-sciences/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/bsc-sport-management-and-coaching/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/civil-engineering/meng-civil-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-physics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/modern-languages/ba-modern-languages-and-european-studies-german-and-ab-initio-italian-including-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/msci-mathematics-and-physics-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-criminology-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-computer-systems-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/international-development/bsc-international-development-with-economics/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-social-sciences-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry-with-management-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/accounting-and-finance/bsc-accounting-and-finance/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-and-mathematics-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/mcomp-computer-science-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-electronic-systems-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/politics/ba-italian-ab-initio-and-politics-including-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/bsc-sport-and-exercise-science-including-combined-placement-and-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/business-and-management/bsc-international-management-and-modern-languages-french-including-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/bsc-health-and-exercise-science-including-a-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-mechanical-with-automotive-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/architecture/bsc-architecture-including-placements/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/civil-engineering/beng-civil-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-electronic-systems-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-robotics-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/mchem-chemistry-for-drug-discovery/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-statistics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-criminology/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/education/ba-education-with-psychology-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/integrated-mechanical-and-electrical-engineering/meng-integrated-mechanical-and-electrical-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-computer-systems-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematics/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-electronic-engineering-with-space-science-and-technology-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-mechanical-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/biosciences/bsc-biochemistry/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/natural-sciences/msci-natural-sciences/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-including-placement-year-and-research-placement/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/business-and-management/bsc-management-with-marketing-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-with-astrophysics-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-sociology-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/mchem-chemistry/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-electrical-and-electronic-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/mcomp-computer-science-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/mcomp-computer-science/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-and-politics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-including-combined-placement-and-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-and-mathematics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-electrical-power-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-mechanical-engineering-with-manufacturing-and-management-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-mechanical-with-automotive-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-physics-with-astrophysics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-and-mathematics/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/modern-languages/ba-modern-languages-and-european-studies-french-and-spanish-including-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/pharmacy/mpharm-pharmacy/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/business-and-management/bsc-management/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/civil-engineering/beng-civil-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/politics/ba-spanish-and-politics-including-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/integrated-mechanical-and-electrical-engineering/meng-integrated-mechanical-and-electrical-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/bsc-sport-and-exercise-science/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-integrated-design-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/msci-chemistry-with-management/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-physics/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-mechanical-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/politics/bsc-politics-with-economics/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematical-sciences/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/modern-languages/ba-modern-languages-and-european-studies-french-and-german-including-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry-with-management/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/bsc-computer-science-and-mathematics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-physics-with-astrophysics/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-robotics-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/international-development/bsc-international-development-with-economics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/civil-engineering/meng-civil-and-architectural-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/business-and-management/bsc-management-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-and-politics-including-combined-placement-and-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/bsc-computer-science-and-mathematics/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/politics/bsc-politics-and-international-relations-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-electronic-systems-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/mcomp-computer-science-and-mathematics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/politics/ba-french-and-politics-including-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/psychology/bsc-psychology-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/mmath-mathematics/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/msci-sport-and-exercise-science/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematics-and-statistics-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/mchem-chemistry-for-drug-discovery-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-electronic-engineering-with-space-science-and-technology-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-mathematics-and-physics-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematics-and-statistics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematics-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-sociology/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/modern-languages/ba-modern-languages-and-european-studies-french-and-ab-initio-italian-including-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-electronic-systems-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-statistics/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/mchem-chemistry-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-statistics-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematical-sciences-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/biosciences/bsc-biology/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry-with-management-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/psychology/msci-psychology/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/bsc-computer-science-and-mathematics-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/natural-sciences/bsc-natural-sciences-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/accounting-and-finance/bsc-accounting-and-finance-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-electrical-power-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/bsc-health-and-exercise-science/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-mechanical-engineering-with-manufacturing-and-management/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-with-astrophysics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/education/ba-education-with-psychology/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/bsc-computer-science-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/bsc-sport-management-and-coaching-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-sociology-and-social-policy/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemical-engineering/meng-chemical-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/natural-sciences/msci-natural-sciences-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-mathematics-and-physics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/psychology/msci-psychology-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-electronic-engineering-with-space-science-and-technology/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/natural-sciences/bsc-natural-sciences/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/pharmacology/bsc-pharmacology/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-computer-systems-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-and-politics-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/social-work/bsc-social-work-and-applied-social-studies/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/mcomp-computer-science-and-mathematics-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-including-research-placement/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-aerospace-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-physics-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-and-mathematics-including-combined-placement-and-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/biosciences/bsc-biomedical-sciences/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/msci-mathematics-and-physics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-electrical-power-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/business-and-management/bsc-international-management-and-modern-languages-spanish-including-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/business-and-management/bsc-international-management-including-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/msci-chemistry-with-management-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/biosciences/bsc-biochemistry-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/politics/ba-german-and-politics-including-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-with-astrophysics-including-placement-year-and-research-placement/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemical-engineering/beng-chemical-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/business-and-management/bsc-international-management-and-modern-languages-german-including-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/bsc-computer-science/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/civil-engineering/meng-civil-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematical-sciences-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry-for-drug-discovery-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/pharmacology/mpharmacol-pharmacology-including-integrated-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemical-engineering/meng-chemical-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-aerospace-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemical-engineering/beng-chemical-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-mathematics-and-physics/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/msci-sport-and-exercise-science-including-combined-placement-and-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/msci-sport-and-exercise-science-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/mmath-mathematics-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/bsc-sport-and-exercise-science-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-social-policy-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematics-and-statistics/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-with-astrophysics/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-electrical-and-electronic-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/bsc-sport-and-exercise-science-including-placement/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/biosciences/bsc-biomedical-sciences-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-electrical-and-electronic-engineering/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/bsc-computer-science-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/politics/bsc-politics-and-international-relations/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/mchem-chemistry-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/modern-languages/ba-modern-languages-and-european-studies-german-and-spanish-including-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/politics/bsc-politics-with-economics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/physics/msci-mathematics-and-physics/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-electrical-power-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/natural-sciences/bsc-natural-sciences-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-electrical-and-electronic-engineering-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/msci-sport-and-exercise-science-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-including-placement-year/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/psychology/bsc-psychology/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/natural-sciences/msci-natural-sciences-including-study-year-abroad/',
        'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry-for-drug-discovery/'
    ]
    C = set(C)
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Bath'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.degree_name
        degree_name = response.xpath('/html/body/main/div[2]/div/div/h1/span').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        degree_name = clear_space_str(degree_name)
        # print(degree_name)

        #4.programme_en
        programme_en = response.xpath('/html/body/main/div[2]/div/div/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        programme_en = programme_en.replace(degree_name,'')
        # print(programme_en)
        programme_en = clear_space_str(programme_en)
        programme_en1 = response.xpath('/html/body/main/div[2]/div/div/h2').extract()
        programme_en1 = ''.join(programme_en1)
        programme_en1 = remove_tags(programme_en1)
        programme_en1 = clear_space_str(programme_en1)
        # print(programme_en1)
        if 'Russian' in programme_en1:
            programme_en = programme_en + '-'+ programme_en1
            programme_en = programme_en.replace(', starting in October 2018','').replace(', starting in September 2018','')
        elif 'French' in programme_en1:
            programme_en = programme_en +'-'+ programme_en1
            programme_en = programme_en.replace(', starting in October 2018','').replace(', starting in September 2018','')
        elif 'German' in programme_en1:
            programme_en = programme_en +'-'+ programme_en1
            programme_en = programme_en.replace(', starting in October 2018','').replace(', starting in September 2018','')
        elif 'Spanish' in programme_en1:
            programme_en = programme_en +'-'+ programme_en1
            programme_en = programme_en.replace(', starting in October 2018','').replace(', starting in September 2018','')
        elif 'Italian' in programme_en1:
            programme_en = programme_en +'-'+ programme_en1
            programme_en = programme_en.replace(', starting in October 2018','').replace(', starting in September 2018','')
        else:
            programme_en = programme_en
        # print(programme_en)

        #5.degree_type
        degree_type = 1

        #6.duration
        duration_list = response.xpath('/html/body/main/div[2]/div/div/h2/text()').extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        duration_list = clear_space_str(duration_list)
        # print(duration_list)
        duration = re.findall('\d',duration_list)[0]
        # print(duration)

        #7.start_date
        start_date = translate_month(duration_list)
        # print(start_date)
        start_date = '2019-'+ str(start_date)
        # print(start_date)

        #8.ucascode
        list1=['http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-social-policy-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/international-development/bsc-international-development-with-economics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-and-politics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/pharmacology/mpharmacol-pharmacology-including-integrated-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/social-work/bsc-social-work-and-applied-social-studies/',
'http://www.bath.ac.uk/courses/undergraduate-2019/biosciences/bsc-biology-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/biosciences/bsc-biochemistry-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/civil-engineering/meng-civil-and-architectural-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-criminology/',
'http://www.bath.ac.uk/courses/undergraduate-2019/business-and-management/bsc-management-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-mechanical-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/msci-chemistry-with-management/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-aerospace-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-social-sciences-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/biosciences/bsc-biomedical-sciences/',
'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-and-mathematics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-statistics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/bsc-computer-science-and-mathematics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/politics/bsc-politics-with-economics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/mcomp-computer-science-and-mathematics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/bsc-sport-management-and-coaching-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/integrated-mechanical-and-electrical-engineering/meng-integrated-mechanical-and-electrical-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-mechanical-engineering-with-manufacturing-and-management/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-criminology-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/modern-languages/ba-modern-languages-and-european-studies-german-and-spanish-including-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/modern-languages/ba-modern-languages-and-european-studies-french-and-spanish-including-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/modern-languages/ba-modern-languages-and-european-studies-french-and-german-including-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/business-and-management/bsc-management-with-marketing-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/business-and-management/bsc-international-management-and-modern-languages-spanish-including-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/business-and-management/bsc-international-management-and-modern-languages-german-including-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-physics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/psychology/bsc-psychology/',
'http://www.bath.ac.uk/courses/undergraduate-2019/psychology/msci-psychology/',
'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/pharmacology/bsc-pharmacology/',
'http://www.bath.ac.uk/courses/undergraduate-2019/education/ba-education-with-psychology/',
'http://www.bath.ac.uk/courses/undergraduate-2019/pharmacy/mpharm-pharmacy/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-physics-with-astrophysics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/politics/bsc-politics-and-international-relations/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-computer-systems-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/natural-sciences/msci-natural-sciences/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-electronic-systems-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/international-development/bsc-international-development-with-economics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematical-sciences-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-sociology-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/pharmacy/mpharm-pharmacy-including-integrated-pre-registration-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-electrical-and-electronic-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-electrical-and-electronic-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-mechanical-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-aerospace-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/business-and-management/bsc-international-management-including-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-sociology-and-social-policy-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-electrical-power-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-electrical-power-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/biosciences/bsc-biomedical-sciences-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematics-and-statistics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-integrated-design-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/civil-engineering/meng-civil-and-architectural-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-electronic-engineering-with-space-science-and-technology/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-with-astrophysics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-and-mathematics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-statistics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/mmath-mathematics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/msci-mathematics-and-physics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/mcomp-computer-science/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry-for-drug-discovery/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/mchem-chemistry/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/mchem-chemistry-for-drug-discovery/',
'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/business-and-management/bsc-management/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/bsc-sport-and-exercise-science/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/msci-sport-and-exercise-science/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematical-sciences/',
'http://www.bath.ac.uk/courses/undergraduate-2019/education/ba-education-with-psychology-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemical-engineering/meng-chemical-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/politics/bsc-politics-and-international-relations-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/civil-engineering/meng-civil-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/civil-engineering/beng-civil-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/business-and-management/bsc-international-management-and-modern-languages-french-including-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/accounting-and-finance/bsc-accounting-and-finance-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-mechanical-with-automotive-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-mechanical-engineering-with-manufacturing-and-management-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/bsc-health-and-exercise-science-including-a-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-robotics-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-physics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/politics/bsc-politics-with-economics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/psychology/bsc-psychology-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-sociology/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemical-engineering/beng-chemical-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-physics-with-astrophysics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-mathematics-and-physics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-and-mathematics-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-statistics-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/bsc-sport-and-exercise-science-including-placement/',
'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-and-politics-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/bsc-computer-science-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry-for-drug-discovery-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/bsc-sport-management-and-coaching/',
'http://www.bath.ac.uk/courses/undergraduate-2019/politics/ba-italian-ab-initio-and-politics-including-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemical-engineering/beng-chemical-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematical-sciences-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-mechanical-with-automotive-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/civil-engineering/meng-civil-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry-with-management-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-electrical-power-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/natural-sciences/bsc-natural-sciences-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/modern-languages/ba-modern-languages-and-european-studies-french-and-ab-initio-italian-including-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/modern-languages/ba-modern-languages-and-european-studies-spanish-and-ab-initio-italian-including-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/modern-languages/ba-modern-languages-and-european-studies-german-and-ab-initio-italian-including-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-electronic-engineering-with-space-science-and-technology-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-with-astrophysics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/politics/ba-french-and-politics-including-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/politics/ba-german-and-politics-including-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry-with-management/',
'http://www.bath.ac.uk/courses/undergraduate-2019/politics/ba-spanish-and-politics-including-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/mmath-mathematics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/msci-mathematics-and-physics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mechanical-engineering/meng-integrated-design-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/mcomp-computer-science-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/mchem-chemistry-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/accounting-and-finance/bsc-accounting-and-finance/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/msci-sport-and-exercise-science-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/mchem-chemistry-for-drug-discovery-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/counselling/fdsc-addictions-counselling-franchised/',
'http://www.bath.ac.uk/courses/undergraduate-2019/integrated-mechanical-and-electrical-engineering/meng-integrated-mechanical-and-electrical-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/msci-chemistry-with-management-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-and-politics-including-combined-placement-and-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/mcomp-computer-science-and-mathematics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-computer-systems-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-electronic-systems-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/business-and-management/bsc-business-administration-including-placements/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-electrical-and-electronic-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-with-astrophysics-including-research-placement/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-electrical-power-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/natural-sciences/bsc-natural-sciences/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-sociology-and-social-policy/',
'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-including-combined-placement-and-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-electronic-systems-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-including-research-placement/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemical-engineering/meng-chemical-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/fdsc-sport-sports-performance/',
'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-and-mathematics-including-combined-placement-and-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/civil-engineering/beng-civil-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-robotics-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematics-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-electronic-engineering-with-space-science-and-technology-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/natural-sciences/msci-natural-sciences-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-mathematics-and-physics-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-physics-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-social-policy/',
'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/bsc-computer-science-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/msci-sport-and-exercise-science-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-computer-systems-engineering/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry-for-drug-discovery-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/bsc-health-and-exercise-science/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry-with-management-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-physics-with-astrophysics-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/bsc-computer-science-and-mathematics-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/mmath-mathematics-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/biosciences/bsc-biology/',
'http://www.bath.ac.uk/courses/undergraduate-2019/biosciences/bsc-biochemistry/',
'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/bsc-computer-science/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/msci-mathematics-and-physics-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/bsc-chemistry/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/bsc-sport-and-exercise-science-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/natural-sciences/bsc-natural-sciences-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/mcomp-computer-science-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/mchem-chemistry-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/chemistry/mchem-chemistry-for-drug-discovery-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-with-astrophysics-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/mcomp-computer-science-and-mathematics-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/msci-sport-and-exercise-science-including-combined-placement-and-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematics-and-statistics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/natural-sciences/msci-natural-sciences-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-including-placement-year-and-research-placement/',
'http://www.bath.ac.uk/courses/undergraduate-2019/architecture/bsc-architecture-including-placements/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/mphys-physics-with-astrophysics-including-placement-year-and-research-placement/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sport-exercise-and-health/bsc-sport-and-exercise-science-including-combined-placement-and-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/sociology-social-policy-and-criminology/bsc-social-sciences/',
'http://www.bath.ac.uk/courses/undergraduate-2019/physics/bsc-mathematics-and-physics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/economics/bsc-economics-and-politics/',
'http://www.bath.ac.uk/courses/undergraduate-2019/psychology/msci-psychology-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/computer-science/bsc-computer-science-and-mathematics-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/meng-computer-systems-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-electrical-and-electronic-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-electronic-systems-engineering-including-placement-year/',
'http://www.bath.ac.uk/courses/undergraduate-2019/mathematical-sciences/bsc-mathematics-and-statistics-including-study-year-abroad/',
'http://www.bath.ac.uk/courses/undergraduate-2019/electronic-and-electrical-engineering/beng-electronic-engineering-with-space-science-and-technolog/y']
        list2=['Physics with Astrophysics MPhys (Hons) – 4 years',
'Mathematics BSc (Hons) – 3 years',
'Economics and Mathematics BSc (Hons) – 3 years',
'Statistics BSc (Hons) – 3 years',
'Mathematics MMath (Hons) – 4 years',
'Mathematics and Physics MSci (Hons) – 4 years',
'Computer Science MComp (Hons) – 4 years',
'Chemistry for Drug Discovery BSc (Hons) – 3 years',
'Chemistry MChem (Hons) – 4 years',
'Chemistry for Drug Discovery MChem (Hons) – 4 years',
'Mechanical Engineering MEng (Hons) – 4 years',
'Chemistry with Management MSci (Hons) – 4 years',
'Aerospace Engineering MEng (Hons) – 4 years',
'Social Sciences BSc (Hons) – 4 years including placement year',
'Biomedical Sciences BSc (Hons) – 3 years',
'Economics and Mathematics BSc (Hons) – 4 years including placement year',
'Statistics BSc (Hons) – 4 years including placement year',
'Computer Science and Mathematics BSc (Hons) – 3 years',
'Politics with Economics BSc (Hons) – 4 years including placement year',
'Computer Science and Mathematics MComp (Hons) – 4 years',
'Social Policy BSc (Hons) – 4 years including placement year',
'International Development with Economics BSc (Hons) – 3 years',
'Economics and Politics BSc (Hons) – 4 years including placement year',
'Pharmacology MPharmacol (Hons) – 4 years including integrated placement year',
'Social Work and Applied Social Studies BSc (Hons) – 3 years',
'Biology BSc (Hons) – 4 years including placement year',
'Biochemistry BSc (Hons) – 4 years including placement year',
'Civil and Architectural Engineering MEng (Hons) – 4 years',
'Criminology BSc (Hons) – 3 years',
'Management BSc (Hons) – 4 years including placement year',
'Economics BSc (Hons) – 4 years including placement year',
'Management BSc (Hons) – 3 years',
'Sport and Exercise Science BSc (Hons) – 3 years',
'Sport and Exercise Science MSci (Hons) – 4 years',
'Mathematical Sciences BSc (Hons) – 3 years',
'Education with Psychology BA (Hons) – 4 years including placement year',
'Chemical Engineering MEng (Hons) – 4 years',
'Politics and International Relations BSc (Hons) – 4 years including placement year',
'Civil Engineering MEng (Hons) – 4 years',
'Civil Engineering BEng (Hons) – 3 years',
'Computer Systems Engineering MEng (Hons) – 4 years',
'Natural Sciences MSci (Hons) – 4 years',
'Electronic Systems Engineering MEng (Hons) – 4 years',
'International Development with Economics BSc (Hons) – 4 years including placement year',
'Mathematical Sciences BSc (Hons) – 4 years including placement year',
'Sociology BSc (Hons) – 4 years including placement year',
'Pharmacy MPharm (Hons) – 5 years including integrated pre-registration year',
'Electrical and Electronic Engineering BEng (Hons) – 3 years',
'Electrical and Electronic Engineering MEng (Hons) – 4 years',
'Mechanical Engineering MEng (Hons) – 5 years including placement year',
'Aerospace Engineering MEng (Hons) – 5 years including placement year',
'International Management BSc (Hons) – 4 years including year abroad',
'Sociology and Social Policy BSc (Hons) – 4 years including placement year',
'Electrical Power Engineering BEng (Hons) – 3 years',
'Electrical Power Engineering MEng (Hons) – 4 years',
'Biomedical Sciences BSc (Hons) – 4 years including placement year',
'Mathematics and Statistics BSc (Hons) – 4 years including placement year',
'Integrated Design Engineering MEng (Hons) – 5 years including placement year',
'Civil and Architectural Engineering MEng (Hons) – 5 years including placement year',
'Electronic Engineering with Space Science and Technology MEng (Hons) – 4 years',
'Physics BSc (Hons) – 3 years',
'Physics MPhys (Hons) – 4 years',
'Psychology BSc (Hons) – 3 years',
'Psychology MSci (Hons) – 4 years',
'Economics BSc (Hons) – 3 years',
'Pharmacology BSc (Hons) – 3 years',
'Education with Psychology BA (Hons) – 3 years',
'Pharmacy MPharm (Hons) – 4 years',
'Physics with Astrophysics BSc (Hons) – 3 years',
'Politics and International Relations BSc (Hons) – 3 years',
'Sport Management and Coaching BSc (Hons) – 4 years including placement year',
'Integrated Mechanical and Electrical Engineering MEng (Hons) – 5 years including placement year',
'Mechanical Engineering with Manufacturing and Management MEng (Hons) – 4 years',
'Criminology BSc (Hons) – 4 years including placement year',
'Modern Languages and European Studies(German and Spanish) BA (Hons) – 4 years including year abroad',
'Modern Languages and European Studies (French and Spanish) BA (Hons) – 4 years including year abroad',
'Modern Languages and European Studies (French and German) BA (Hons) – 4 years including year abroad',
'Management with Marketing BSc (Hons) – 4 years including placement year',
'International Management and Modern Languages (Spanish) BSc (Hons) – 4 years including year abroad',
'International Management and Modern Languages (German) BSc (Hons) – 4 years including year abroad',
'International Management and Modern Languages (French) BSc (Hons) – 4 years including year abroad',
'Accounting and Finance BSc (Hons) – 4 years including placement year',
'Mechanical with Automotive Engineering MEng (Hons) – 5 years including placement year',
'Mechanical Engineering with Manufacturing and Management MEng (Hons) – 5 years including placement year',
'Health and Exercise Science BSc (Hons) – 4 years including a placement year',
'Robotics Engineering MEng (Hons) – 5 years including placement year',
'Physics BSc (Hons) – 4 years including placement year',
'Politics with Economics BSc (Hons) – 3 years',
'Psychology BSc (Hons) – 4 years including placement year',
'Economics BSc (Hons) – 4 years including study year abroad',
'Mathematics BSc (Hons) – 4 years including study year abroad',
'Electronic Engineering with Space Science and Technology MEng (Hons) – 5 years including placement year',
'Natural Sciences MSci (Hons) – 5 years including placement year',
'Mathematics and Physics BSc (Hons) – 4 years including study year abroad',
'Physics BSc (Hons) – 4 years including study year abroad',
'Social Policy BSc (Hons) – 3 years',
'Computer Science BSc (Hons) – 4 years including study year abroad',
'Sport and Exercise Science MSci (Hons) – 5 years including study year abroad',
'Chemistry BSc (Hons) – 4 years including study year abroad',
'Computer Systems Engineering BEng (Hons) – 3 years',
'Sociology BSc (Hons) – 3 years',
'Chemical Engineering BEng (Hons) – 3 years',
'Physics with Astrophysics BSc (Hons) – 4 years including placement year',
'Mathematics BSc (Hons) – 4 years including placement year',
'Mathematics and Physics BSc (Hons) – 4 years including placement year',
'Economics and Mathematics BSc (Hons) – 4 years including study year abroad',
'Statistics BSc (Hons) – 4 years including study year abroad',
'Sport and Exercise Science BSc (Hons) – 4 years including placement',
'Economics and Politics BSc (Hons) – 4 years including study year abroad',
'Computer Science BSc (Hons) – 4 years including placement year',
'Natural Sciences BSc (Hons) – 3 years',
'Sociology and Social Policy BSc (Hons) – 3 years',
'Economics BSc (Hons) – 4 years including combined placement and study year abroad',
'Electronic Systems Engineering BEng (Hons) – 3 years',
'Physics MPhys (Hons) – 4 years including research placement',
'Chemical Engineering MEng (Hons) – 5 years including placement year',
'Sport (Sports Performance) FdSc – 2 years',
'Economics and Mathematics BSc (Hons) – 4 years including combined placement and study year abroad',
'Civil Engineering BEng (Hons) – 4 years including placement year',
'Robotics Engineering MEng (Hons) – 4 years',
'Social Sciences BSc (Hons) – 3 years',
'Mathematics and Physics BSc (Hons) – 3 years',
'Economics and Politics BSc (Hons) – 3 years',
'Psychology MSci (Hons) – 5 years including placement year',
'Computer Science and Mathematics BSc (Hons) – 4 years including placement year',
'Computer Systems Engineering MEng (Hons) – 5 years including placement year',
'Electrical and Electronic Engineering BEng (Hons) – 4 years including placement year',
'Electronic Systems Engineering BEng (Hons) – 4 years including placement year',
'Mathematics and Statistics BSc (Hons) – 4 years including study year abroad',
'Electronic Engineering with Space Science and Technology BEng (Hons) – 3 years',
'Integrated Mechanical and Electrical Engineering MEng (Hons) – 4 years',
'Chemistry with Management MSci (Hons) – 5 years including placement year',
'Economics and Politics BSc (Hons) – 4 years including combined placement and study year abroad',
'Computer Science and Mathematics MComp (Hons) – 5 years including placement year',
'Computer Systems Engineering BEng (Hons) – 4 years including placement year',
'Electronic Systems Engineering MEng (Hons) – 5 years including placement year',
'Business Administration BSc (Hons) – 4 years including placements',
'Electrical and Electronic Engineering MEng (Hons) – 5 years including placement year',
'Physics with Astrophysics MPhys (Hons) – 4 years including research placement',
'Electrical Power Engineering MEng (Hons) – 5 years including placement year',
'Electrical Power Engineering BEng (Hons) – 4 years including placement year',
'Natural Sciences BSc (Hons) – 4 years including placement year',
'Modern Languages and European Studies (French and ab initio Italian) BA (Hons) – 4 years including year abroad',
'Modern Languages and European Studies (Spanish and ab initio Italian) BA (Hons) – 4 years including year abroad',
'Modern Languages and European Studies (German and ab initio Italian) BA (Hons) – 4 years including year abroad',
'Electronic Engineering with Space Science and Technology BEng (Hons) – 4 years including placement year',
'Physics with Astrophysics MPhys (Hons) – 5 years including placement year',
'French and Politics BA (Hons) – 4 years including year abroad',
'German and Politics BA (Hons) – 4 years including year abroad',
'Chemistry with Management BSc (Hons) – 3 years',
'Chemistry BSc (Hons) – 4 years including placement year',
'Chemistry for Drug Discovery BSc (Hons) – 4 years including placement year',
'Sport Management and Coaching BSc (Hons) – 3 years',
'Italian ab initio and Politics BA (Hons) – 4 years including year abroad',
'Chemical Engineering BEng (Hons) – 4 years including placement year',
'Mathematical Sciences BSc (Hons) – 4 years including study year abroad',
'Mechanical with Automotive Engineering MEng (Hons) – 4 years',
'Civil Engineering MEng (Hons) – 5 years including placement year',
'Chemistry with Management BSc (Hons) – 4 years including placement year',
'Physics MPhys (Hons) – 5 years including placement year',
'Spanish and Politics BA (Hons) – 4 years including year abroad',
'Mathematics MMath (Hons) – 5 years including placement year',
'Mathematics and Physics MSci (Hons) – 5 years including placement year',
'Integrated Design Engineering MEng (Hons) – 4 years',
'Computer Science MComp (Hons) – 5 years including placement year',
'Chemistry MChem (Hons) – 4 years including placement year',
'Accounting and Finance BSc (Hons) – 3 years',
'Sport and Exercise Science MSci (Hons) – 5 years including placement year',
'Chemistry for Drug Discovery MChem (Hons) – 4 years including placement year ',
'Addictions Counselling FdSc – 2 years franchised',
'Chemistry for Drug Discovery BSc (Hons) – 4 years including study year abroad',
'Health and Exercise Science BSc (Hons) – 3 years',
'Chemistry with Management BSc (Hons) – 4 years including study year abroad',
'Physics with Astrophysics BSc (Hons) – 4 years including study year abroad',
'Computer Science and Mathematics BSc (Hons) – 4 years including study year abroad',
'Mathematics MMath (Hons) – 4 years including study year abroad',
'Physics MPhys (Hons) – 4 years including study year abroad',
'Biology BSc (Hons) – 3 years',
'Biochemistry BSc (Hons) – 3 years',
'Computer Science BSc (Hons) – 3 years',
'Mathematics and Physics MSci (Hons) – 5 years including study year abroad',
'Chemistry BSc (Hons) – 3 years',
'Sport and Exercise Science BSc (Hons) – 4 years including study year abroad',
'Natural Sciences BSc (Hons) – 4 years including study year abroad',
'Computer Science MComp (Hons) – 5 years including study year abroad',
'Chemistry MChem (Hons) – 4 years including study year abroad ',
'Chemistry for Drug Discovery MChem (Hons) – 4 years including study year abroad',
'Physics with Astrophysics MPhys (Hons) – 4 years including study year abroad',
'Computer Science and Mathematics MComp (Hons) – 5 years including study year abroad',
'Sport and Exercise Science MSci (Hons) – 5 years including combined placement and study year abroad',
'Mathematics and Statistics BSc (Hons) – 3 years',
'Natural Sciences MSci (Hons) – 5 years including study year abroad',
'Physics MPhys (Hons) – 5 years including placement year and research placement',
'Architecture BSc (Hons) – 4 years including placements',
'Physics with Astrophysics MPhys (Hons) – 5 years including placement year and research placement',
'Sport and Exercise Science BSc (Hons) – 4 years including combined placement and study year abroad']
        list3=['F300',
'F303',
'C801',
'8C82',
'L100',
'B210',
'LX5H',
'B230',
'F314',
'L291',
'H306',
'F1NF',
'H400',
'L306',
'55TG',
'L103',
'G301',
'G4GD',
'L2LC',
'G4G1',
'H423',
'NN12',
'LL43',
'H630',
'H632',
'1JKI',
'GG31',
'H762',
'H203',
'H6HK',
'F317',
'G100',
'L102',
'G300',
'G103',
'FG3C',
'G403',
'F151',
'F103',
'F154',
'L101',
'N200',
'BC17',
'C605',
'G140',
'LXM3',
'H803',
'L290',
'H200',
'H204',
'L405',
'53H3',
'LLC2',
'B213',
'L501',
'C111',
'C703',
'H202',
'L370',
'N201',
'CX6H',
'HH3Q',
'H716',
'L371',
'RR24',
'RR14',
'RR12',
'NN25',
'NR24',
'NR22',
'HG64',
'GFC0',
'H622',
'L407',
'G141',
'L304',
'B236',
'H603',
'H600',
'H309',
'L300',
'H813',
'F315',
'G101',
'FG31',
'L106',
'G302',
'BCC7',
'LLC3',
'G401',
'NR21',
'NN43',
'H343',
'H713',
'C611',
'H653',
'F301',
'L2L1',
'C800',
'L104',
'F101',
'F152',
'CX63',
'RL23',
'H814',
'G142',
'H330',
'H205',
'F146',
'3SAM',
'L305',
'GF13',
'LL12',
'8C92',
'G4GA',
'HGP4',
'H604',
'H641',
'GG32',
'H6H4',
'RL42',
'3FG4',
'39B2',
'H761',
'G404',
'F104',
'NN34',
'C604',
'F155',
'B940',
'H631',
'FCG0',
'RR1H',
'RR4H',
'RR2H',
'H6H7',
'2RT5',
'RL12',
'RL22',
'F145',
'HHJ6',
'F1NG',
'LLC4',
'GLG1',
'GHK6',
'H623',
'N100',
'H601',
'F318',
'H633',
'CFG0',
'LL34',
'L105',
'H640',
'F313',
'H804',
'C601',
'L107',
'H201',
'H652',
'F153',
'C610',
'F1N2',
'F316',
'I10B',
'G104',
'F312',
'C100',
'C700',
'G400',
'G105',
'H6H5',
'GFCA',
'FG32',
'F307',
'L404',
'I10C',
'C607',
'F107',
'GH46',
'GG13',
'GFCB',
'O2VD',
'K100',
'F320',
'C609',
'385C',
'F100',
'C606',
'GCF0',
'I101',
'F105',
'F156',
'F321',
'G4GC',
'C608']
        dd = {}
        for i in range(len(list1)):
            dd[list1[i]] = list3[i]
        ucascode = dd.get(url)
        # print(ucascode)


        #9.overview_en
        overview_en = response.xpath("//*[contains(text(),'Teaching')]//preceding-sibling::*").extract()
        overview_en = ''.join(overview_en)
        overview_en = clear_space_str(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #10.modules_en
        modules_en = response.xpath('//*[@id="course-structure"]/div/div[2]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #11.assessment_en
        assessment_en = response.xpath('//*[@id="learning-assessment"]//article[2]//li').extract()
        assessment_en = '\n'.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #12.require_chinese_en
        require_chinese_en = ''

        #13.career_en
        career_en =response.xpath("//*[contains(text(),'Careers')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        career_en = clear_space_str(career_en)
        # print(career_en)

        #14.ielts 15161718
        ielts_list = response.xpath('//*[@id="entry-requirements"]/section[6]/div[2]//ul/li[1]').extract()
        ielts_list = ''.join(ielts_list)
        ielts_list = remove_tags(ielts_list)
        # print(ielts_list)
        ielts = re.findall('\d\.\d',ielts_list)
        if len(ielts) ==2:
            a= ielts[0]
            b= ielts[1]
            ielts = a
            ielts_s = b
            ielts_r = b
            ielts_w = b
            ielts_l = b
        else:
            ielts = 6.5
            ielts_s = 6
            ielts_r = 6
            ielts_w = 6
            ielts_l = 6
        # print(ielts,ielts_l,ielts_w,ielts_s,ielts_r)

        #19.alevel
        alevel = response.xpath('//*[@id="entry-requirements"]/section[1]/div[1]//div[1]/header/span').extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel)
        # print(alevel)

        #20.deadline
        deadline_list = response.xpath("//*[contains(text(),'Overseas deadline')]//following-sibling::*").extract()
        deadline_list = ''.join(deadline_list)
        deadline_list =remove_tags(deadline_list)
        if len(deadline_list)!=0:
            deadline_day = re.findall('\d+',deadline_list)[0]
        else:
            deadline_day = 30
        deadline_month = translate_month(deadline_list)
        deadline = '2019-'+str(deadline_month)+'-'+str(deadline_day)
        # print(deadline)

        #21.location
        location = 'Bath'

        #22.department
        department = response.xpath("//*[contains(text(),'Department')]//following-sibling::div/a").extract()
        department = ''.join(department)
        department = remove_tags(department)
        department = department.replace('&amp;','')
        # print(department)

        #23.apply_proces_en
        apply_proces_en = 'https://www.bath.ac.uk/study/ug/applications.pl'

        #24.tuition_fee_pre
        tuition_fee_pre = '£'

        #25.other
        other = 'http://www.bath.ac.uk/corporate-information/faculty-of-humanities-social-sciences-taught-postgraduate-tuition-fees-2018-19/'

        #26.duration_per
        duration_per = 1

        #27.tuition_fee
        if 'Managemen' in programme_en:
            tuition_fee = 17700
        elif 'Science' in programme_en:
            tuition_fee = 19800
        elif 'Engineering' in programme_en:
            tuition_fee = 19800
        elif 'Architecture' in programme_en:
            tuition_fee = 12650
        else:
            tuition_fee = 15900
        #28.apply_documents_en
        apply_documents_en = '<p>Apply for a course To apply for a course, you must use the online application form. You will need to create an account before you can start the application process. On the application form, you will need to give: your personal details the date you plan to start studying your education details proof of your English level if English is not your first language the name and contact details of an academic referee from your current or most recent place of study your personal statement, explaining your reasons for wishing to study the course your supporting information Supporting information So we can assess your application and make our decision, you will need to give us all the necessary supporting information, including: a scan of your undergraduate degree certificate and your postgraduate degree certificate, if you have one a scan of your final degree transcript or your most recent transcript if you are still studying an academic reference from your current or most recent place of study, if you have one an up-to-date CV payment of the application fee, if applicable You can also upload supporting documents through Application Tracker after you have submitted your online application. International applicants If you are an international student, you should also give us: your passport details if you need a Tier 4 visa an authorised translation of your degree certificate and transcript if they are not in English your English language assessment certificate, if available Track your application We will send you login details for Application Tracker when you have submitted your application. We aim to make decisions about applications within six weeks of receiving all your supporting information and will tell you whether or not you have been successful through Application Tracker. You can also check the progress of your application there. We may also contact you for more information or, depending on the course you apply for, to invite you to an interview. Accept your offer If you receive an offer, use Application Tracker to accept or decline as soon as possible. For some courses, you will need to pay a deposit when you accept your offer. Receiving an unconditional offer If you receive an unconditional offer, you have met all the required academic conditions and we are offering you a place. Receiving a conditional offer If you receive a conditional offer, you may not have met all the requirements, but we hope you will be able to do so. These requirements may include English language scores, degree results, satisfactory references or payment of a deposit. You must meet these requirements and submit evidence of them through Application Tracker before you can start your studies. If you need to improve your English language skills before starting your studies, you may be able to take a pre-sessional course to reach the required level. When you meet the conditions of your offer, we will contact you and tell you what to do next.</p>'
        #29.apply_pre
        apply_pre = '£'
        #30.toefl 31323334
        toefl_list = response.xpath('//*[@id="entry-requirements"]/section[1]/div[2]/div/div/div/div[2]/ul/li[5]').extract()
        toefl_list = ''.join(toefl_list)
        # print(toefl_list)
        try:
            toefl = re.findall('\d{2,3}',toefl_list)
        except:
            toefl = ['90','21']
        if len(toefl) ==2:
           a = toefl[0]
           b = toefl[1]
           toefl = a
           toefl_s = b
           toefl_r = b
           toefl_l = b
           toefl_w = b
        else:
            toefl = 90
            toefl = 21
            toefl_s = 21
            toefl_r = 21
            toefl_l = 21
            toefl_w = 21
        # print(toefl,toefl_s,toefl_r,toefl_l,toefl_w)

        #35.ib
        ib = response.xpath('//*[@id="entry-requirements"]/section[1]/div[1]/div/div/div[3]/header/span').extract()
        ib = ''.join(ib)
        ib = remove_tags(ib)
        if len(ib)!=9:
            ib = response.xpath('//*[@id="entry-requirements"]/section[1]/div[1]/div/div/div[4]/header/span').extract()
            ib = ''.join(ib)
            ib = remove_tags(ib)
        # print(ib)

        item['ib'] =  ib
        item['alevel'] = alevel
        item['ucascode'] =  ucascode
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_w'] = toefl_w
        item['toefl_l'] = toefl_l
        item['apply_pre'] = apply_pre
        item['apply_documents_en'] = apply_documents_en
        item['tuition_fee'] = tuition_fee
        item['university'] = university
        item['url'] = url
        item['degree_name'] = degree_name
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['start_date'] = start_date
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['require_chinese_en'] = require_chinese_en
        item['career_en'] = career_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['deadline'] = deadline
        item['location'] = location
        item['department'] = department
        item['apply_proces_en'] = apply_proces_en
        item['tuition_fee_pre'] = tuition_fee_pre
        item['other'] = other
        yield  item



