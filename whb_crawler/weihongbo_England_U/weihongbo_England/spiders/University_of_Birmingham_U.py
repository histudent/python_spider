import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'University_of_Birmingham_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []


    C= ['https://www.birmingham.ac.uk/undergraduate/courses/metallurgy-materials/aerospace-engineering-beng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/dasa/african-development.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/history/history-ancient-medieval.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/caha/ancient-history.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/dasa/african.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/business/accounting-finance.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/acs/american-canadian-abroad.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/anthropology-and-history.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/sportex/app-golf-mgt-studies.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/physics/theoretical-physics-applied-maths.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/physics/theoretical-physics-applied-maths-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/anthropology-and-african-studies.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/caha/arch-ancient-hist.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/caha/arch-anthropology.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/archaeology-and-ancient-history-and-history.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/computer-science/artificial-intelligence-computer-science-industry.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/computer-science/artificial-intelligence-computer-science.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/anthropology-and-classical-literature-and-civilisation.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/anthropology-and-political-science.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/human-biology-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/human-biology-placement.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/med/biomedical-science.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/med/biomedical-materials-sci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/chemistry/chemistry-business-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/chemistry/chemistry-business-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/maths/mathematics-business-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/maths/mathematics-business.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/edu/ba-education.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/social-policy/policy-politics-economics.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/political-science-social-policy.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/biochemistry.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/biochemistry-genetics.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/biochemistry-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/biochemistry-europe.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/medical-biochemistry.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/biological-sciences-zoology.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/biochemistry-international-year.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/biochemistry-placement.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/biological-sciences-genetics.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/biological-sciences.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/biological-sciences-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/human-biology-international-year.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/human-biology.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/biological-sciences-international-year.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/biological-sciences-placement.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/civil-engineering/civil-engineering-railway-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/biosciences/biological-sciences-europe.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/civil-engineering/civil-engineering-beng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/civil-engineering/civil-engineering-industry.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/civil-engineering/civil-engineering-international-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/caha/classical-lit-civ.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/caha/classical-lit-civ.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/caha/classics.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/civil-engineering/civil-engineering-international-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/civil-engineering/civil-engineering-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/computer-science/computer-science.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/computer-science/computer-science-industry.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/computer-science/computer-science-pwc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/computer-science/computer-science-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/computer-science/computer-science-industry-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/chemical-engineering/chemical-engineering-industry-beng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/chemical-engineering/chemical-engineering-industry-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/chemical-engineering/chemical-engineering-industrial-international-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/chemistry/chemistry-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/chemical-engineering/chemical-engineering-beng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/classical-literature-and-civilisation-and-philosophy.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/chemical-engineering/chemical-engineering-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/chemistry/chemistry-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/chemistry/chemistry-language-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/chemistry/chemistry-language-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/chemistry/chemistry-industrial.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/chemistry/chemistry-study-abroad-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/civil-engineering/civil-engineering-railway-beng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/computer-science/computer-science-international-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/computer-science/artificial-intelligence-computer-science.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/computer-science/artificial-intelligence-computer-science-industry.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/computer-science/computer-science-software-engineering.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/computer-science/computer-science-software-engineering-industry.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/computer-science/computer-science-international-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/english/english-creative.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/drama/drama-theatre.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/environmental-science-abroad.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/drama-and-english.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/environmental-science-placement.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/metallurgy-materials/materials-science-engineering.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/metallurgy-materials/mechanical-materials-engineering-beng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/metallurgy-materials/nuclear-engineering-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/metallurgy-materials/materials-engineering-industrial-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/english-and-classical-literature-and-civilisation.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/english/english-film.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/english-and-history.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/english-and-history-of-art.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/english/english-language-and-linguistics.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/english-and-philosophy.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/english/english.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/english/english-language-and-literature.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/english/english-lang.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/environmental-science.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/environmental-science-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/econ/economics-and-political-science-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/international-relations-economics-year-abroad.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/eese/electrical-railway-engineering-beng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/eese/electrical-railway-engineering-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/eese/electronic-electrical-engineering.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/eese/electronic-electrical-engineering-industry-beng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/eese/electronic-electrical-engineering-industry-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/engineering/engineering-beng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/eese/electronic-electrical-engineering-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/engineering/engineering-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/french-studies-and-geography.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/french-studies-and-history.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/french-studies-and-mathematics.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/international-relations-french.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/geography-and-german-studies.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/geography-and-history.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/geography-planning.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/geography-ba.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/geography-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/geography-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/geography-msci-international.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/geography-bsc-abroad.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/geography-ba-abroad.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/geology-geography.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/geology-physical-geography-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/geology-international.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/geology-physical-geography-msci-international.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/geology.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/geology-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/german-studies-and-history.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/history-and-russian-studies.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/hispanic-studies-and-history.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/history-and-history-of-art.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/history-and-philosophy.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/history-and-political-science.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/history/history.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/histart/history-art.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/history-and-theology.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/psychology/human-neuroscience-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/international-relations.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/law/international-law-globalisation.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/international-relations-german.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/international-relations-economics.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/international-relations-spanish.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/international-relations-year-abroad.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/law/law-llb.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/law/law-business.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/law/law-criminology.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/law/law-french.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/law/law-german.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/liberal-arts/liberal-arts-and-sciences.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/mechanical-engineering/mechanical-engineering-automotive-beng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/mechanical-engineering/mechanical-engineering-automotive-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/mechanical-engineering/mechanical-engineering-beng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/mechanical-engineering/mechanical-engineering-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/mechanical-engineering/mechanical-engineering-industrial-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/eese/mechatronic-robotic-engineering-beng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/eese/mechatronic-robotic-engineering-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/lang/modern-languages-ou-pathway.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/metallurgy-materials/metallurgy-beng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/metallurgy-materials/materials-science-engineering-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/maths/maths-computer-science-industrial-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/maths/maths-computer-science-industrial.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/metallurgy-materials/nuclear-science-materials-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/mathematics-and-music.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/maths/maths-computer-science-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/maths/maths-computer-science.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/mathematics-and-philosophy.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/maths/mathematics.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/maths/mathematics-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/maths/mathematics-industry.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/maths/mathematics-international.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/maths/mathematics-europe.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/metallurgy-materials/mechanical-materials-engineering-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/modern-languages-and-english.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/modern-languages-and-history-of-art.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/modern-languages-and-music.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/lang/modern-languages.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/lang/mod-lang-business.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/music/music.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/liberal-arts/nat-sci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/psychology/psychology-practice.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/psychology/psychology-research.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/psychology/psychology.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/med/public-health.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/physics/physics-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/physics/physics-particle-cosmology-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/physics/physics-particle-cosmology-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/sportex/physiotherapy.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/social-policy/policy-politics-economics-year-abroad.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/political-economy.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/political-economy-year-abroad.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/political-science.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/political-science-international-relations.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/political-science-international-relations-year-abroad.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/political-science-philosophy.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/political-science-philosophy-year-abroad.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/political-science-sociology.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/political-science-sociology-year-abroad.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/political-science-year-abroad.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/thr/politics-religion-philosophy.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/palaeobiology-palaeoenvironments-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/palaeobiology-palaeoenvironments-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/gees/palaeobiology-palaeoenvironments-msci-international.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/chemistry/chemistry-pharmacology-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/chemistry/chemistry-pharmacology-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/med/pharmacy-5-year.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/med/pharmacy-4-year.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/philosophy-and-sociology.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/phil/philosophy.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/thr/philosophy-religion-ethics.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/sportex/sport-pe-coaching.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/physics/physics-international-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/physics/physics-international-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/physics/physics-astrophysics-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/physics/physics-astrophysics-international-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/physics/physics-astrophysics-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/physics/physics-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/jointhonours/russian-studies-and-international-relations.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/social-policy/social-policy-and-criminology.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/social-policy/social-policy-sociology.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/social-policy/social-policy-ba.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/social-policy/social-policy-year-abroad-ba.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/govsoc/political-science-social-policy-year-abroad.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/social-policy/social-work.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/social-policy/sociology-and-criminology.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/edu/education-sociology.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/social-policy/sociology.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/sportex/sport-exercise-sciences.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/physics/theoretical-physics-msci.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/thr/theology.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/econ/economics-german.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/econ/maths-econ-stats-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/business/international-business-comms.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/business/international-business-lang.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/econ/economics-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/social-policy/criminology-year-abroad.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/business/business-management.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/med/dental-hygiene-therapy.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/business/business-mgmt-comms-yini.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/chemical-engineering/chemical-engineering-international-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/social-policy/criminology.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/metallurgy-materials/aerospace-engineering-meng.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/business/business-mgmt-marketing-yini.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/business/business-management-with-marketing.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/business/bus-mgnt-year-in-industry.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/fd/chemical-engineering-foundation.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/med/medicine.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/econ/money-banking-finance-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/med/dental-surgery.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/med/nursing-mnurs.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/acs/american-canadian-studies.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/thr/philosophy-religion-ethics.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/business/business-mgmt-comms.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/physics/theoretical-physics-bsc.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/econ/economics-spanish.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/business/international-business.aspx',
'https://www.birmingham.ac.uk/undergraduate/courses/med/nursing.aspx',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'University of Birmingham'
        try:
            location = 'warwick'
            #location = remove_tags(location)
            #print(location)
        except:
            location = 'N/A'
            #print(location)
        try:
            department = response.xpath('').extract()[0]
            department = remove_tags(department)
            department = department.replace('\n\n', '\n')
            department = department.replace('\r\n', '')
            department = department.replace('	', '')
            department = department.replace('  ', '')
            department = department.replace('\n', '')
            department = department.replace('Our Staff', '')
            #print(department)
        except:
            department = ''
            #print(department)


        try:
            degree_name = response.xpath('//*[@id="main"]/div/div/div/div/div[2]/div[1]/section/h3/strong').extract()[0]
            degree_name = remove_tags(degree_name)
            degree_name = re.findall('.* \((.*)\)',degree_name)[0]

            #degree_name = re.findall('(.*)\n.*',degree_name)[0]
            #degree_name = re.findall('(.*)                    .*',degree_name)[0]
            #degree_name = re.findall('\((.*)\)',degree_name)[0]
            #degree_name = degree_name.replace('\n',degree_name)
            degree_name = degree_name.replace(' ','')
            #print(degree_name)
        except:
            degree_name = 'BA'
            #print(degree_name)

        try:
            degree_overview_en = ''
            degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = "<div><p>" + degree_overview_en + "</p></div>"
            #print(degree_overview_en)
        except:
            degree_overview_en = ''

        try:
            programme_en = response.xpath('//*[@id="main"]/div/div/div/div/div[2]/div[1]/section/h3/strong').extract()[0]
            programme_en = remove_tags(programme_en)
            programme_en =programme_en.replace('\r\n','')
            #programme_en = re.findall('',programme_en)[0]
            programme_en = programme_en.replace('  ',' ')
            programme_en = programme_en.replace(degree_name,'')
            programme_en = programme_en.replace('()','')
            #print(programme_en)

        except:
            programme_en = 'N/A'
            #print(programme_en)

        try:
            overview_en = response.xpath('//*[@id="course-tab-1"]/section/p').extract()[0]
            overview_en = remove_tags(overview_en)
            overview_en = overview_en.replace('  ','')
            #overview_en = overview_en.replace('\n\n','\n')
            overview_en = overview_en.replace('\n\n','')
            overview_en = overview_en.replace('\r\n','')
            overview_en = overview_en.replace('\n','')
            overview_en = '<div>' + overview_en + '</div>'
            #overview_en = remove_tags(overview_en)
            #print(overview_en)
        except:
            overview_en = 'N/A'
            #print(overview_en)


        try:
            start_date = response.xpath('//*[@id="course-tab-5"]').extract()[0]
            start_date = remove_tags(start_date)
            start_date = start_date.replace('\r\n','')
            start_date = start_date.replace('  ',' ')
            start_date = start_date.replace('\n','')
            start_date = re.findall('Start Date(.*)',start_date)[0]
            if 'October' in start_date:
                start_date = '2019-10'
            elif '24' in start_date:
                start_date = '2019-9-24'
            else:
                start_date = '2019-9'
            #print(start_date)

        except:
            start_date = 'N/A'
            #print(start_date)



        try:
            modules_en = response.xpath('//*[@id="course-tab-3"]').extract()[0]
            modules_en = remove_tags(modules_en)
            modules_en = modules_en.replace('\n\n','\n')
            modules_en = modules_en.replace('\r\n','')
            modules_en = modules_en.replace('	','')
            modules_en = modules_en.replace('  ','')
            modules_en = modules_en.replace('\n','')
            modules_en = "<div><p>" + modules_en + "</p></div>"
            #print(modules_en)
        except:
            modules_en = 'N/A'
            #print(modules_en)



        try:
            degree_requirements = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[2]/div[2]/div[1]/div[2]').extract()[0]
            degree_requirements = remove_tags(degree_requirements)
            degree_requirements = degree_requirements.replace('  ','')
            #print(degree_requirements)
        except:
            degree_requirements = ''
            #print(degree_requirements)

        try:
            rntry_requirements_en = response.xpath('//*[@id="course-tab-2"]').extract()[0]
            rntry_requirements_en = remove_tags(rntry_requirements_en)
            rntry_requirements_en = "<div>"+rntry_requirements_en+"</div>"
            rntry_requirements_en = rntry_requirements_en.replace('\n\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\r\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('  ','')
            #rntry_requirements_en =rntry_requirements_en.replace('		                        ','')
            #print(rntry_requirements_en)
        except:
            rntry_requirements_en = 'N/A'
            #print(rntry_requirements_en)

        try:
            professional_background = response.xpath('').extract()
            professional_background = remove_tags(professional_background)
        except:
            professional_background = ''

        try:
            require_chinese_en = ''
        except:
            require_chinese_en = ''
        try:
            ielts_desc = 'https://warwick.ac.uk/study/undergraduate/courses-2019/economicspoliticsinternational'
            #print(ielts_desc)

        except:
            ielts_desc = 'N/A'

            #print(ielts_desc)

        try:
            #ielts = '6.5'
            #ielts =remove_tags(ielts)
            #ielts = re.findall('IELTS(.*)',ielts)[0]
            ielts = 0
            #print(ielts)
        except:
            ielts = 0
            #print(ielts)

        try:
            #ielts_l = '5.5'
            ielts_l = 0
            #print(ielts_l)
            #ielts_l = remove_tags(ielts_l)
        except:
            ielts_l = 0

        try:
            ielts_s = ielts_l

        except:
            ielts_s = ielts_l

        try:
            ielts_r = ielts_l
        except:
            ielts_r = ielts_l

        try:
            ielts_w = ielts_l
        except:
            ielts_w = ielts_l

        try:
            toefl_code = response.xpath('').extract()
            toefl_code = remove_tags(toefl_code)
        except:
            toefl_code = 0

        try:
            toefl_desc = response.xpath('').extract()
            toefl_desc = remove_tags(toefl_desc)
        except:
            toefl_desc = 0

        try:
            toefl = response.xpath('').extract()
            toefl = remove_tags(toefl)

        except:
            toefl = 0

        try:
            toefl_l = response.xpath('').extrcat()
            toefl_l = remove_tags(toefl_l)

        except:
            toefl_l = 0

        try:
            toefl_s = response.xpath('').extract()
            toefl_s = remove_tags(toefl_s)

        except:
            toefl_s = 0

        try:
            toefl_r = response.xpath('').extract()
            toefl_r = remove_tags(toefl_r)
        except:
            toefl_r = 0

        try:
            toefl_w = response.xpath('').extract()
            toefl_w = remove_tags(toefl_w)
        except:
            toefl_w = 0

        try:
            interview_desc_en = response.xpath('//*[@id="entry-requirements-accordion-0"]/div[1]').extract()[0]
            interview_desc_en = remove_tags(interview_desc_en)
            interview_desc_en = interview_desc_en.replace('\n\n', '\n')
            interview_desc_en = interview_desc_en.replace('\r\n', '')
            interview_desc_en = interview_desc_en.replace('	', '')
            interview_desc_en = interview_desc_en.replace('  ', '')
            interview_desc_en = interview_desc_en.replace('\n', '')
            interview_desc_en = "<div>" + interview_desc_en + "</div>"
            #print(interview_desc_en)
        except:
            interview_desc_en = 'N/A'
            #print(interview_desc_en)
        try:
            work_experience_desc_en = response.xpath('').extract()
            work_experience_desc_en = remove_tags(work_experience_desc_en)
        except:
            work_experience_desc_en = ''

        try:
            portfolio_desc_en = response.xpath('').extract()
            portfolio_desc_en = remove_tags(portfolio_desc_en)
        except:
            portfolio_desc_en = ''

        try:
            career_en = response.xpath('//*[@id="EmployabilityTab"]').extract()[0]
            career_en = remove_tags(career_en)
            career_en = career_en.replace('\r\n','')
            career_en = career_en.replace('  ',' ')
            career_en = career_en.replace('\n','')
            career_en = "<div><span>" + career_en + "</span></div>"
            print(career_en)
        except:
            career_en = ''
            print(career_en)
        try:
            apply_desc_en = '<span>Assessing each application fairly and consistently within an extremely competitive field is a difficult task. It is carried out by course selectors (Admissions Tutors) who are academics in departments and by professionals in the Undergraduate Admissions Team to ensure that decisions are made fairly, taking into account as much information about applicants as possible. Applications are assessed on their own merits and in competition with others, as we receive many more applications for most courses than there are places available. Selectors judge the evidence provided on the UCAS application against the criteria set for the chosen course. They take into account existing academic achievements and the context within which they have been achieved (including any exceptional circumstances), predicted grades, the personal statement and the academic reference. Remember that selectors want to hear about you and your interests and potential – there is no one-size-fits-all approach! As a consequence of the high level of competition for our courses, and because we want to consider your full profile and your potential as an individual rather than simply looking at your actual or predicted grades, it may take some time to communicate a decision to you. We will keep you informed of the status of your application during the admissions process. Successful candidates will receive an offer which the selector feels is most appropriate, though typical offer levels are listed for each course. We will provide feedback to candidates to whom we are not able to make an offer when this is requested in writing. You should be aware that decisions are made on a highly competitive basis and therefore we are often unable to make offers to all applicants who meet, or even exceed, the typical entry requirements.</span>'
            #apply_desc_en = remove_tags(apply_desc_en)
            #apply_desc_en = "<div>" + apply_desc_en + "</div>"
            #print(apply_desc_en)
        except:
            apply_desc_en = ''

        try:
            apply_documents_en = ''
            #apply_documents_en = remove_tags(apply_documents_en)
        except:
            apply_documents_en = ''


        apply_fee = 13

        dead_time = '1-15'
        #other = ''
        try:
            apply_proces_en = response.xpath('').extract()
        except:
            apply_proces_en = ''


        try:
            duration = response.xpath('//*[@id="course-tab-5"]').extract()[0]
            #duration = remove_tags(duration)
            duration = remove_tags(duration)
            duration = duration.replace('  ','')
            duration = duration.replace('\r\n','')
            duration = duration.replace('\n','')
            duration = re.findall('Duration(.*)',duration)[0]
            #duration = re.findall('(\d) Years',duration)[0]
            if '4' in duration:
                duration = '4'
            elif '3' in duration:
                duration = '3'
            elif '5' in duration:
                duration = '5'
            elif '2' in duration:
                duration = '2'
            elif '1' in duration:
                duration = '1'
            elif 'two' in duration:
                duration = '2'
            else:
                duration = 'N/A'
            #print(duration)

        except:
            duration = 'N/A'
            #print(duration)



        try:
            other = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/a').extract()[0]
            other = remove_tags(other)
            #print('成功'+ other + response.url)
        except:
            other = ''
           #print('失败' + other)

        try:
            ib = response.xpath('//*[@id="main"]/div/div/div/div/div[2]/div[1]/section/p[1]/strong[2]').extract()[0]
            ib = remove_tags(ib)
            #print(ib)
        except:
            ib = ''
            #print(ib)

        try:
            alevel = response.xpath('//*[@id="main"]/div/div/div/div/div[2]/div[1]/section/p[1]/strong[1]').extract()[0]
            alevel = remove_tags(alevel)
            alevel = re.findall('entry, (.*), IB',alevel)[0]
            #alevel = alevel.replace('*','')
            #alevel = re.findall("(\w\w\w)",alevel)[0]
            #print(alevel)
        except:
            alevel = 'N/A'
            #print(alevel)
        try:
            ucascode = response.xpath('//*[@id="course-tab-5"]').extract()[0]
            ucascode = remove_tags(ucascode)
            ucascode = ucascode.replace('\r\n','')
            ucascode = ucascode.replace('\n','')
            ucascode = ucascode.replace('  ',' ')
            ucascode = re.findall('UCAS Code(.*)Award',ucascode)[0]
            ucascode = ucascode.replace('     ','')
            ucascode = ucascode.replace('   ','')
            #print(ucascode)
        except:
            ucascode = 'N/A'
            #print(ucascode)

        try:
            tuition_fee = response.xpath('/html/body/div[1]/div/div[1]/section[7]/div/div/div[3]/div/div[2]').extract()[0]
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = tuition_fee.replace('£','')
            tuition_fee = tuition_fee.replace(',','')
            tuition_fee = tuition_fee.replace('*','')
            tuition_fee = tuition_fee.replace(' ','')
            tuition_fee = tuition_fee.replace('\r\n','')
            tuition_fee = tuition_fee.replace('\n','')

            tuition_fee = re.findall('(\d\d\d\d\d)',tuition_fee)[0]

            # tuition_fee = tuition_fee.replace('  ','')
            # tuition_fee = tuition_fee.replace('\n','')
            # tuition_fee = re.findall('Full-time international students: £(.*) paStudents',tuition_fee)[0]
            # tuition_fee = int(tuition_fee)
            #print(tuition_fee)
        except:
            tuition_fee = 0
            #print(tuition_fee)

        try:
            assessment_en = response.xpath('//*[@id="assessment-methods"]/div/p').extract()[0]
            assessment_en = remove_tags(assessment_en)
            assessment_en = assessment_en.replace('\r\n', '')
            assessment_en = assessment_en.replace('  ', '')
            assessment_en = assessment_en.replace('\n', '')
            assessment_en = "<div><span>" + assessment_en + "</span></div>"
            #print(assessment_en)
        except:
            assessment_en = ''
            #print(assessment_en)

        application_open_date = '2018-10-6/2018-10-20'
        item["university"] = university
        item["location"] = location
        item["department"] = department
        item["degree_type"] = 1
        item["degree_name"] = degree_name
        #item["degree_overview_en"] = degree_overview_en
        item["programme_en"] = programme_en
        item["overview_en"] = overview_en
        item["teach_time"] = 1
        item["start_date"] = start_date
        item["modules_en"] = modules_en
        item["career_en"] = career_en
        item["application_open_date"] = '9'
        item["deadline"] = ''
        item["apply_pre"] = '£'
        item["apply_fee"] = apply_fee
        #item["rntry_requirements_en"] = rntry_requirements_en
        item["degree_requirements"] = degree_requirements
        item["tuition_fee_pre"] = '£'
        #item["major_requirements"] = rntry_requirements_en
        item["professional_background"] = professional_background
        item["ielts_desc"] = ielts_desc
        item["ielts"] = ielts
        item["ielts_l"] = ielts_l
        item["ielts_s"] = ielts_l
        item["ielts_r"] = ielts_l
        item["ielts_w"] = ielts_l
        item["toefl_code"] = toefl_code
        item["toefl_desc"] = toefl_desc
        item["toefl"] = toefl
        item["toefl_l"] = toefl_l
        item["toefl_s"] = toefl_s
        item["toefl_r"] = toefl_r
        item["toefl_w"] = toefl_w
        item["work_experience_desc_en"] = work_experience_desc_en
        item["interview_desc_en"] = interview_desc_en
        item["portfolio_desc_en"] = portfolio_desc_en
        item["apply_desc_en"] = apply_desc_en
        item["apply_documents_en"] = apply_documents_en
        item["other"] = other
        item["url"] = response.url
        item["gatherer"] = 'weihongbo'
        item["apply_proces_en"] = apply_proces_en
        item["batch_number"] = 4
        item["finishing"] = 0
        stime = time.time()
        create_time = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(float(stime)))
        #print(create_time)
        item["create_time"] = create_time
        item["import_status"] = 0
        item["duration"] = duration
        item["tuition_fee"] = tuition_fee
        item["update_time"] = create_time
        item["alevel"] = alevel
        item["ib"] = ib
        item["ucascode"] = ucascode
        item["rntry_requirements"] = rntry_requirements_en
        item["require_chinese_en"] = require_chinese_en
        item["assessment_en"] =  assessment_en
        item["application_open_date"] = application_open_date
        #item["apply_pre"] = ''
        yield item


