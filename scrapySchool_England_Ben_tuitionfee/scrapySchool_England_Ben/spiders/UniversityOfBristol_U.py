# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space, clear_space_str
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
import requests
from lxml import etree
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.getDuration import getIntDuration,getTeachTime


class UniversityofBristol_USpider(scrapy.Spider):
    name = "UniversityofBristol_U"
    # allowed_domains = ['baidu.com']
    start_urls = ['https://www.bristol.ac.uk/study/undergraduate/search/']
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    def parse(self, response):
        links = ["https://www.bristol.ac.uk/study/undergraduate/2019/religion-theology/ba-theology-sociology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/politics-international-relations/ba-politics-spanish/",
"https://www.bristol.ac.uk/study/undergraduate/2019/mechanical-engineering/meng-mech-eng-europe/",
"https://www.bristol.ac.uk/study/undergraduate/2019/law/llb-law-and-spanish/",
"https://www.bristol.ac.uk/study/undergraduate/2019/quantitative-research-methods/msci-childhood-quantitative-research/",
"https://www.bristol.ac.uk/study/undergraduate/2019/theatre/ba-theatre-english/",
"https://www.bristol.ac.uk/study/undergraduate/2019/french/ba-french-spanish/",
"https://www.bristol.ac.uk/study/undergraduate/2019/dentistry/bds-gateway-to-dentistry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/quantitative-research-methods/bsc-sociology-quantitative-research/",
"https://www.bristol.ac.uk/study/undergraduate/2019/physics/bsc-physics-preliminary-study/",
"https://www.bristol.ac.uk/study/undergraduate/2019/german/ba-german-spanish/",
"https://www.bristol.ac.uk/study/undergraduate/2019/innovation/msci-psychology-with-innovation/",
"https://www.bristol.ac.uk/study/undergraduate/2019/music/ba-music/",
"https://www.bristol.ac.uk/study/undergraduate/2019/chemical-physics/msci-chemical-physics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/management/bsc-econ-management/",
"https://www.bristol.ac.uk/study/undergraduate/2019/aerospace/meng-aerospace-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/maths/msci-maths-philosophy/",
"https://www.bristol.ac.uk/study/undergraduate/2019/italian/ba-italian-spanish/",
"https://www.bristol.ac.uk/study/undergraduate/2019/innovation/marts-history-with-innovation/",
"https://www.bristol.ac.uk/study/undergraduate/2019/cellular-molecular/bsc-cancer-biology-immunology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/philosophy/ba-philosophy-russian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/geophysics/msci-geophysics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/geoscience/msci-environmental-geoscience-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/biochemistry/bsc-biochem/",
"https://www.bristol.ac.uk/study/undergraduate/2019/italian/ba-italian-portuguese/",
"https://www.bristol.ac.uk/study/undergraduate/2019/politics-international-relations/bsc-politics-and-international-relations-with-stu/",
"https://www.bristol.ac.uk/study/undergraduate/2019/geoscience/bsc-environmental-geoscience/",
"https://www.bristol.ac.uk/study/undergraduate/2019/engineering-maths/meng-maths-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/quantitative-research-methods/msci-geography-quantitative-research/",
"https://www.bristol.ac.uk/study/undergraduate/2019/quantitative-research-methods/bsc-sociology-with-quantitative-research-methods-/",
"https://www.bristol.ac.uk/study/undergraduate/2019/mechanical-engineering/meng-mech-eng-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/biological-sciences/bsc-biology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/modern-languages/ba-modern-languages/",
"https://www.bristol.ac.uk/study/undergraduate/2019/innovation/marts-theatre-with-innovation/",
"https://www.bristol.ac.uk/study/undergraduate/2019/maths/msci-maths-physics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/physics/msci-physics-philosophy/",
"https://www.bristol.ac.uk/study/undergraduate/2019/italian/ba-italian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/economics/bsc-economics-and-politics-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/theatre/ba-theatre-italian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/accounting-finance/bsc-accounting-and-finance-with-professional-plac/",
"https://www.bristol.ac.uk/study/undergraduate/2019/geophysics/msci-geophysics-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/palaeontology-evolution/bsc-palaeontology-and-evolution/",
"https://www.bristol.ac.uk/study/undergraduate/2019/chemistry/msci-chemistry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/management/bsc-accounting-management/",
"https://www.bristol.ac.uk/study/undergraduate/2019/film-television/ba-film-television/",
"https://www.bristol.ac.uk/study/undergraduate/2019/spanish/ba-hispanic-studies/",
"https://www.bristol.ac.uk/study/undergraduate/2019/sociology/bsc-sociology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/liberal-arts/mlibarts-liberal-arts-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/social-policy/bsc-social-policy/",
"https://www.bristol.ac.uk/study/undergraduate/2019/physics/bsc-physics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/film-television/ba-film-italian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/computer-science/meng-comp-sci-europe/",
"https://www.bristol.ac.uk/study/undergraduate/2019/civil-engineering/meng-civil-eng/",
"https://www.bristol.ac.uk/study/undergraduate/2019/engineering-maths/meng-engineering-mathematics-with-a-year-in-indus/",
"https://www.bristol.ac.uk/study/undergraduate/2019/cellular-molecular/bsc-cellular-and-molecular-medicine-with-study-in/",
"https://www.bristol.ac.uk/study/undergraduate/2019/geology/msci-geology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/management/bsc-international-business-management/",
"https://www.bristol.ac.uk/study/undergraduate/2019/vet-nursing-biovet-science/bsc-veterinary-nursing-and-companion-animal-behav/",
"https://www.bristol.ac.uk/study/undergraduate/2019/maths/msci-mathematics-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/electrical-electronic-eng/beng-computer-science-and-electronics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/economics/bsc-economics-and-econometrics-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/social-policy/bsc-social-policy-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/quantitative-research-methods/bsc-geography-quantitative-research/",
"https://www.bristol.ac.uk/study/undergraduate/2019/theatre/ba-theatre-spanish/",
"https://www.bristol.ac.uk/study/undergraduate/2019/biochemistry/bsc-biochem-molecular-biology-biotech/",
"https://www.bristol.ac.uk/study/undergraduate/2019/german/ba-german/",
"https://www.bristol.ac.uk/study/undergraduate/2019/pharmacology/msci-pharmacology-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/liberal-arts/ba-liberal-arts/",
"https://www.bristol.ac.uk/study/undergraduate/2019/psychology/bsc-psychology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/physics/bsc-physics-astrophysics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/innovation/msci-physics-with-innovation/",
"https://www.bristol.ac.uk/study/undergraduate/2019/german/ba-german-italian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/quantitative-research-methods/msci-social-policy-quantitative-research/",
"https://www.bristol.ac.uk/study/undergraduate/2019/chemistry/bsc-chemistry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/czech/ba-czech-russian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/innovation/msci-management-with-innovation/",
"https://www.bristol.ac.uk/study/undergraduate/2019/geography/bsc-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/biochemistry/bsc-biochem-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/civil-engineering/meng-civil-engineering-with-a-year-in-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/aerospace/meng-aerospace-engineering-with-a-year-in-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/biochemistry/bsc-biochem-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/classical-studies/ba-classical-studies/",
"https://www.bristol.ac.uk/study/undergraduate/2019/aerospace/meng-aerospace-engineering-with-a-year-in-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/anthropology/ba-arch-anth/",
"https://www.bristol.ac.uk/study/undergraduate/2019/chemistry/msci-chemistry-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/neuroscience/msci-neuroscience-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/engineering-design/meng-eng-design-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/education/bsc-education-studies/",
"https://www.bristol.ac.uk/study/undergraduate/2019/history-art/ba-history-art/",
"https://www.bristol.ac.uk/study/undergraduate/2019/computer-science/bsc-maths-comp-sci/",
"https://www.bristol.ac.uk/study/undergraduate/2019/dentistry/bds-dentistry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/maths/bsc-maths-philosophy/",
"https://www.bristol.ac.uk/study/undergraduate/2019/russian/ba-russian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/electrical-electronic-eng/meng-mechanical-and-electrical-engineering-with-a/",
"https://www.bristol.ac.uk/study/undergraduate/2019/computer-science/bsc-comp-sci/",
"https://www.bristol.ac.uk/study/undergraduate/2019/german/ba-german-portuguese/",
"https://www.bristol.ac.uk/study/undergraduate/2019/biological-sciences/msci-zoology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/history-art/ba-history-art-italian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/medicine/mb-medicine/",
"https://www.bristol.ac.uk/study/undergraduate/2019/chemical-physics/msci-chemical-physics-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/physiology/bsc-physiology-science/",
"https://www.bristol.ac.uk/study/undergraduate/2019/chemistry/bsc-chemistry-preliminary-study/",
"https://www.bristol.ac.uk/study/undergraduate/2019/mechanical-engineering/meng-mechanical-engineering-with-a-year-in-indust/",
"https://www.bristol.ac.uk/study/undergraduate/2019/politics-international-relations/ba-politics-portuguese/",
"https://www.bristol.ac.uk/study/undergraduate/2019/geophysics/bsc-geophysics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/mechanical-engineering/meng-mechanical-engineering-with-a-year-in-indust/",
"https://www.bristol.ac.uk/study/undergraduate/2019/politics-international-relations/ba-politics-italian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/czech/ba-czech-german/",
"https://www.bristol.ac.uk/study/undergraduate/2019/quantitative-research-methods/bsc-social-policy-quantitative-research/",
"https://www.bristol.ac.uk/study/undergraduate/2019/maths/bsc-maths/",
"https://www.bristol.ac.uk/study/undergraduate/2019/religion-theology/ba-religion-theology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/quantitative-research-methods/bsc-childhood-quantitative-research/",
"https://www.bristol.ac.uk/study/undergraduate/2019/electrical-electronic-eng/meng-elec-electronic-europe/",
"https://www.bristol.ac.uk/study/undergraduate/2019/management/bsc-accounting-and-management-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/law/llb-law/",
"https://www.bristol.ac.uk/study/undergraduate/2019/computer-science/meng-comp-sci-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/maths/bsc-maths-statistics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/biochemistry/msci-biochemistry-with-molecular-biology-and-biot/",
"https://www.bristol.ac.uk/study/undergraduate/2019/economics/bsc-econ-finance/",
"https://www.bristol.ac.uk/study/undergraduate/2019/economics/bsc-economics-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/film-television/ba-film-german/",
"https://www.bristol.ac.uk/study/undergraduate/2019/electrical-electronic-eng/meng-elec-electronic-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/economics/bsc-economics-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/biological-sciences/bsc-zoology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/music/ba-music-german/",
"https://www.bristol.ac.uk/study/undergraduate/2019/economics/bsc-econ-econometrics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/civil-engineering/meng-civil-eng-europe/",
"https://www.bristol.ac.uk/study/undergraduate/2019/czech/ba-czech-italian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/russian/ba-russian-portuguese/",
"https://www.bristol.ac.uk/study/undergraduate/2019/social-policy/bsc-social-policy-politics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/law/llb-law-french/",
"https://www.bristol.ac.uk/study/undergraduate/2019/economics/bsc-econ-maths/",
"https://www.bristol.ac.uk/study/undergraduate/2019/electrical-electronic-eng/meng-comp-sci-electronics-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/social-policy/bsc-social-policy-sociology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/french/ba-french-italian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/innovation/marts-anthropology-with-innovation/",
"https://www.bristol.ac.uk/study/undergraduate/2019/french/ba-french-russian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/history-art/ba-history-art-spanish/",
"https://www.bristol.ac.uk/study/undergraduate/2019/accounting-finance/bsc-accounting-finance-europe/",
"https://www.bristol.ac.uk/study/undergraduate/2019/religion-theology/marts-religion-and-theology-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/maths/bsc-mathematics-with-statistics-for-finance/",
"https://www.bristol.ac.uk/study/undergraduate/2019/french/ba-french-portuguese/",
"https://www.bristol.ac.uk/study/undergraduate/2019/philosophy/bsc-philosophy-and-economics-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/vet-science/bvsc-gateway-to-veterinary-science/",
"https://www.bristol.ac.uk/study/undergraduate/2019/electrical-electronic-eng/meng-mechanical-and-electrical-engineering/",
"https://www.bristol.ac.uk/study/undergraduate/2019/cellular-molecular/bsc-virology-and-immunology-with-study-in-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/accounting-finance/bsc-accounting-finance/",
"https://www.bristol.ac.uk/study/undergraduate/2019/philosophy/ba-philosophy-italian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/mechanical-engineering/meng-mechanical-engineering-with-a-year-in-indust/",
"https://www.bristol.ac.uk/study/undergraduate/2019/quantitative-research-methods/bsc-politics-with-quantitative-research-methods-w/",
"https://www.bristol.ac.uk/study/undergraduate/2019/physics/msci-physics-europe/",
"https://www.bristol.ac.uk/study/undergraduate/2019/maths/bsc-maths-physics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/social-policy/bsc-social-policy-with-criminology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/physics/msci-physics-with-international-experience/",
"https://www.bristol.ac.uk/study/undergraduate/2019/biological-sciences/msci-biology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/electrical-electronic-eng/meng-electrical-and-electronic-engineering-with-a/",
"https://www.bristol.ac.uk/study/undergraduate/2019/philosophy/ba-philosophy-german/",
"https://www.bristol.ac.uk/study/undergraduate/2019/geography/bsc-geography-study-europe/",
"https://www.bristol.ac.uk/study/undergraduate/2019/history-art/ba-history-art-portuguese/",
"https://www.bristol.ac.uk/study/undergraduate/2019/vet-nursing-biovet-science/bsc-vet-nursing/",
"https://www.bristol.ac.uk/study/undergraduate/2019/music/ba-music-italian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/english/ba-english-classical-studies/",
"https://www.bristol.ac.uk/study/undergraduate/2019/geology/bsc-geology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/law/llb-law-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/philosophy/ba-philosophy-portuguese/",
"https://www.bristol.ac.uk/study/undergraduate/2019/physics/msci-theoretical-physics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/criminology/bsc-criminology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/spanish/ba-spanish/",
"https://www.bristol.ac.uk/study/undergraduate/2019/engineering-maths/beng-eng-maths/",
"https://www.bristol.ac.uk/study/undergraduate/2019/electrical-electronic-eng/meng-elec-electronic/",
"https://www.bristol.ac.uk/study/undergraduate/2019/childhood-studies/bsc-childhood-studies-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/english/ba-english/",
"https://www.bristol.ac.uk/study/undergraduate/2019/sociology/bsc-sociology-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/economics/bsc-econ-europe/",
"https://www.bristol.ac.uk/study/undergraduate/2019/cellular-molecular/bsc-cancer-biology-and-immunology-with-study-in-i/",
"https://www.bristol.ac.uk/study/undergraduate/2019/anatomy/bsc-applied-anatomy/",
"https://www.bristol.ac.uk/study/undergraduate/2019/engineering-maths/meng-eng-maths/",
"https://www.bristol.ac.uk/study/undergraduate/2019/management/bsc-economics-and-management-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/accounting-finance/bsc-accounting-and-finance-with-professional-plac/",
"https://www.bristol.ac.uk/study/undergraduate/2019/electrical-electronic-eng/beng-elec-electronic/",
"https://www.bristol.ac.uk/study/undergraduate/2019/accounting-finance/bsc-accounting-and-finance-with-professional-plac/",
"https://www.bristol.ac.uk/study/undergraduate/2019/psychology/msci-psychology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/accounting-finance/bsc-accounting-and-finance-with-professional-plac/",
"https://www.bristol.ac.uk/study/undergraduate/2019/civil-engineering/beng-civil-eng/",
"https://www.bristol.ac.uk/study/undergraduate/2019/film-television/ba-film-spanish/",
"https://www.bristol.ac.uk/study/undergraduate/2019/maths/msci-maths/",
"https://www.bristol.ac.uk/study/undergraduate/2019/philosophy/bsc-philosophy-econ/",
"https://www.bristol.ac.uk/study/undergraduate/2019/film-television/ba-film-portuguese/",
"https://www.bristol.ac.uk/study/undergraduate/2019/childhood-studies/bsc-childhood/",
"https://www.bristol.ac.uk/study/undergraduate/2019/economics/bsc-econ/",
"https://www.bristol.ac.uk/study/undergraduate/2019/aerospace/meng-aerospace/",
"https://www.bristol.ac.uk/study/undergraduate/2019/computer-science/meng-maths-comp-sci/",
"https://www.bristol.ac.uk/study/undergraduate/2019/chemical-physics/bsc-chemical-physics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/theatre/ba-theatre-performance/",
"https://www.bristol.ac.uk/study/undergraduate/2019/chemistry/msci-chemistry-europe/",
"https://www.bristol.ac.uk/study/undergraduate/2019/maths/msci-maths-statistics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/accounting-finance/bsc-accounting-and-finance-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/cellular-molecular/bsc-cellular-molecular/",
"https://www.bristol.ac.uk/study/undergraduate/2019/history-art/ba-history-art-french/",
"https://www.bristol.ac.uk/study/undergraduate/2019/history/ba-history/",
"https://www.bristol.ac.uk/study/undergraduate/2019/quantitative-research-methods/msci-sociology-quantitative-research/",
"https://www.bristol.ac.uk/study/undergraduate/2019/theatre/ba-theatre-film/",
"https://www.bristol.ac.uk/study/undergraduate/2019/anthropology/ba-anthropology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/italian/ba-italian-russian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/physics/msci-physics-astrophysics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/accounting-finance/bsc-economics-and-accounting-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/physics/bsc-physics-philosophy/",
"https://www.bristol.ac.uk/study/undergraduate/2019/computer-science/meng-comp-sci/",
"https://www.bristol.ac.uk/study/undergraduate/2019/theatre/ba-theatre-french/",
"https://www.bristol.ac.uk/study/undergraduate/2019/economics/bsc-econ-politics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/physics/msci-physics-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/management/bsc-management-europe/",
"https://www.bristol.ac.uk/study/undergraduate/2019/spanish/ba-spanish-portuguese/",
"https://www.bristol.ac.uk/study/undergraduate/2019/aerospace/meng-aerospace-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/theatre/ba-theatre-portuguese/",
"https://www.bristol.ac.uk/study/undergraduate/2019/physiology/msci-physiological-science-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/electrical-electronic-eng/beng-mechanical-and-electrical-engineering/",
"https://www.bristol.ac.uk/study/undergraduate/2019/criminology/bsc-criminology-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/mechanical-engineering/meng-mech-eng/",
"https://www.bristol.ac.uk/study/undergraduate/2019/czech/ba-czech-spanish/",
"https://www.bristol.ac.uk/study/undergraduate/2019/innovation/marts-film-and-television-with-innovation/",
"https://www.bristol.ac.uk/study/undergraduate/2019/politics-international-relations/ba-politics-french/",
"https://www.bristol.ac.uk/study/undergraduate/2019/history-art/ba-history-art-german/",
"https://www.bristol.ac.uk/study/undergraduate/2019/management/bsc-management/",
"https://www.bristol.ac.uk/study/undergraduate/2019/aerospace/beng-aerospace-engineering/",
"https://www.bristol.ac.uk/study/undergraduate/2019/law/llb-law-europe/",
"https://www.bristol.ac.uk/study/undergraduate/2019/quantitative-research-methods/msci-politics-quantitative-research/",
"https://www.bristol.ac.uk/study/undergraduate/2019/sociology/bsc-sociology-philosophy/",
"https://www.bristol.ac.uk/study/undergraduate/2019/history-art/ba-history-art-russian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/philosophy/ba-philosophy-french/",
"https://www.bristol.ac.uk/study/undergraduate/2019/maths/msci-maths-europe/",
"https://www.bristol.ac.uk/study/undergraduate/2019/biochemistry/msci-biochemistry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/geoscience/msci-environmental-geoscience/",
"https://www.bristol.ac.uk/study/undergraduate/2019/innovation/meng-electrical-and-electronic-engineering-with-i/",
"https://www.bristol.ac.uk/study/undergraduate/2019/geography/bsc-geography/",
"https://www.bristol.ac.uk/study/undergraduate/2019/aerospace/meng-aerospace-engineering-with-a-year-in-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/classics/ba-classics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/electrical-electronic-eng/meng-mechanical-and-electrical-engineering-with-a/",
"https://www.bristol.ac.uk/study/undergraduate/2019/chemistry/msci-chemistry-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/politics-international-relations/bsc-politics-sociology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/innovation/msci-geography-with-innovation/",
"https://www.bristol.ac.uk/study/undergraduate/2019/french/ba-french-german/",
"https://www.bristol.ac.uk/study/undergraduate/2019/aerospace/meng-aerospace-europe/",
"https://www.bristol.ac.uk/study/undergraduate/2019/english/ba-english-philosophy/",
"https://www.bristol.ac.uk/study/undergraduate/2019/management/bsc-management-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/vet-science/bvsc-veterinary-science/",
"https://www.bristol.ac.uk/study/undergraduate/2019/music/ba-music-french/",
"https://www.bristol.ac.uk/study/undergraduate/2019/neuroscience/bsc-neuroscience/",
"https://www.bristol.ac.uk/study/undergraduate/2019/spanish/ba-spanish-russian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/film-television/ba-film-english/",
"https://www.bristol.ac.uk/study/undergraduate/2019/civil-engineering/meng-civil-eng-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/cellular-molecular/bsc-virology-immunology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/mechanical-engineering/beng-mech-eng/",
"https://www.bristol.ac.uk/study/undergraduate/2019/politics-international-relations/ba-politics-german/",
"https://www.bristol.ac.uk/study/undergraduate/2019/computer-science/meng-comp-sci-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/biomedical-sciences/bsc-biomedical-sciences/",
"https://www.bristol.ac.uk/study/undergraduate/2019/medicine/mb-chb-gateway-to-medicine/",
"https://www.bristol.ac.uk/study/undergraduate/2019/ancient-history/ba-ancient-history/",
"https://www.bristol.ac.uk/study/undergraduate/2019/czech/ba-czech-portuguese/",
"https://www.bristol.ac.uk/study/undergraduate/2019/german/ba-german-russian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/cellular-molecular/bsc-medical-microbiology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/social-policy/bsc-social-policy-management/",
"https://www.bristol.ac.uk/study/undergraduate/2019/philosophy/ba-philosophy/",
"https://www.bristol.ac.uk/study/undergraduate/2019/pharmacology/bsc-pharmacology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/law/llb-law-german/",
"https://www.bristol.ac.uk/study/undergraduate/2019/management/bsc-marketing/",
"https://www.bristol.ac.uk/study/undergraduate/2019/management/bsc-international-business-management-with-study-/",
"https://www.bristol.ac.uk/study/undergraduate/2019/economics/bsc-economics-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/biochemistry/bsc-biochem-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/accounting-finance/bsc-accounting-and-finance-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/biochemistry/bsc-biochem-medical-biochem/",
"https://www.bristol.ac.uk/study/undergraduate/2019/civil-engineering/meng-civil-engineering-with-a-year-in-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/accounting-finance/bsc-accounting-and-finance-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/accounting-finance/bsc-econ-accounting/",
"https://www.bristol.ac.uk/study/undergraduate/2019/civil-engineering/meng-civil-engineering-with-a-year-in-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/education/bsc-psychology-in-education/",
"https://www.bristol.ac.uk/study/undergraduate/2019/cellular-molecular/bsc-medical-microbiology-with-study-in-industry/",
"https://www.bristol.ac.uk/study/undergraduate/2019/palaeontology-evolution/msci-palaeontology-and-evolution/",
"https://www.bristol.ac.uk/study/undergraduate/2019/french/ba-french/",
"https://www.bristol.ac.uk/study/undergraduate/2019/politics-international-relations/bsc-politics-international-relations/",
"https://www.bristol.ac.uk/study/undergraduate/2019/politics-international-relations/bsc-philosophy-politics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/economics/bsc-economics-and-finance-with-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/civil-engineering/meng-civil-eng-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/mechanical-engineering/meng-mech-eng-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/childhood-studies/bsc-childhood-management/",
"https://www.bristol.ac.uk/study/undergraduate/2019/mechanical-engineering/meng-mech-eng-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/philosophy/ba-philosophy-spanish/",
"https://www.bristol.ac.uk/study/undergraduate/2019/czech/ba-czech-french/",
"https://www.bristol.ac.uk/study/undergraduate/2019/innovation/meng-computer-science-with-innovation/",
"https://www.bristol.ac.uk/study/undergraduate/2019/electrical-electronic-eng/meng-comp-sci-electronics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/politics-international-relations/ba-politics-russian/",
"https://www.bristol.ac.uk/study/undergraduate/2019/physics/msci-physics/",
"https://www.bristol.ac.uk/study/undergraduate/2019/maths/bsc-maths-europe/",
"https://www.bristol.ac.uk/study/undergraduate/2019/theatre/ba-theatre-german/",
"https://www.bristol.ac.uk/study/undergraduate/2019/geology/msci-geology-study-abroad/",
"https://www.bristol.ac.uk/study/undergraduate/2019/quantitative-research-methods/bsc-politics-quantitative-research/",
"https://www.bristol.ac.uk/study/undergraduate/2019/philosophy/ba-philosophy-theology/",
"https://www.bristol.ac.uk/study/undergraduate/2019/film-television/ba-film-french/",
"https://www.bristol.ac.uk/study/undergraduate/2019/innovation/marts-music-with-innovation/", ]
        print(len(links))
        links = list(set(links))
        print(len(links))

        for link in links:
            # url = "https://www.bristol.ac.uk"+link
            url = link
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Bristol"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:
            # 专业
            course = response.xpath("//span[@property='programname']//text()").extract()
            # print("course = ", course)
            item['programme_en'] = ''.join(course).replace("\n", " ").replace("\r", " ").strip()
            print("item['programme_en']: ", item['programme_en'])

            tuitionFee = response.xpath("//li[contains(text(),'International students: £')]//text()").extract()
            # print("tuitionFee = ", tuitionFee)
            if len(tuitionFee) > 0:
                item['tuition_fee_pre'] = "£"
                item['tuition_fee'] = getTuition_fee(''.join(tuitionFee))
            print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])
            print("item['tuition_fee']: ", item['tuition_fee'])


            alevel = response.xpath(
                "//div[@id='typical-offer']//table//tr/th[contains(text(), 'A-level')]/../td//text()").extract()
            clear_space(alevel)
            # print(alevel)
            if len(alevel) > 0:
                item['alevel'] = ''.join(alevel[0]).strip()
            # print("item['alevel'] = ", item['alevel'])

            # print(len("36 points overall with 18 at Higher Level, including 6, 5 at Higher Level in two of the following subjects: Biology, Chemistry, Physics, Mathematics, Psychology"))
            if len(item['alevel']) > 160:
                item['alevel'] = ''.join(item['alevel'][:161])
            # print("item['alevel']1 = ", item['alevel'])

            ib = response.xpath(
                "//div[@id='typical-offer']//table//tr/th[contains(text(), 'International Baccalaureate ')]/../td//text()").extract()
            clear_space(ib)
            if len(ib) > 0:
                item['ib'] = ''.join(ib[0]).strip()

            if len(item['ib']) > 160:
                item['ib'] = ''.join(item['ib'][:161])
            # print("item['ib'] = ", item['ib'])

            yield item
        except Exception as e:
            print("异常：", str(e))
            print("报错链接：", response.url)
            with open("scrapySchool_England_Ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")


    def parse_modules_en(self, modulesUrl):
        data = requests.get(modulesUrl, headers=self.headers)
        response = etree.HTML(data.text)
        modules1 = response.xpath("//a[@class='active']//text()")
        modules2 = response.xpath("//table[@class='table-basic']")
        m2 = ""
        if len(modules2) > 0:
            m2 = "<h2>"+''.join(modules1)+"</h2>"
            m2 += etree.tostring(modules2[0], encoding='unicode', pretty_print=False, method='html')
        m2 = remove_class(clear_space_str(m2))
        y2 = response.xpath("//a[@class='active']/../following-sibling::li[1]/a/@href")
        return [m2, y2]

    def parseAssessCareer(self, assessCareerUrl):
        data = requests.get(assessCareerUrl, headers=self.headers)
        response = etree.HTML(data.text)
        assessCareerDict = {}
        assessment = response.xpath("//h2[contains(text(),'How is this course taught and assessed?')]|//h2[contains(text(),'How is this course taught and assessed?')]/following-sibling::*[position()<6]")
        assessmentStr = ""
        if len(assessment) > 0:
            for ass in assessment:
                assessmentStr += etree.tostring(ass, encoding='unicode', pretty_print=False, method='html')
        assessmentStr = remove_class(clear_space_str(assessmentStr))
        assessCareerDict['assessment_en'] = assessmentStr

        career = response.xpath(
            "//h2[contains(text(),'What are my career prospects?')]|//h2[contains(text(),'What are my career prospects?')]/following-sibling::p")
        careerStr = ""
        if len(career) > 0:
            for ass in career:
                careerStr += etree.tostring(ass, encoding='unicode', pretty_print=False, method='html')
                careerStr = remove_class(clear_space_str(careerStr))
        assessCareerDict['career_en'] = careerStr
        return assessCareerDict


