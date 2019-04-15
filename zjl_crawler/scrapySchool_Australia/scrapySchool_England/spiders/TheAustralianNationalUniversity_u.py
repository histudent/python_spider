# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/19 11:42'
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
from scrapySchool_England.clearSpace import clear_space_str
import requests
from lxml import etree
class TheAustralianNationalUniversitySpider(scrapy.Spider):
    name = 'TheAustralianNationalUniversity_u'
    allowed_domains = ['anu.edu.au/']
    start_urls = []
    C= [
        'https://programsandcourses.anu.edu.au/2019/major/NAST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/NAST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/NAST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/NAST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SEAS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SEAS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SEAS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SEAS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MECA-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MECA-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MECA-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MECA-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MECA-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CHST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BAPAF',
        'https://programsandcourses.anu.edu.au/2019/major/APIR-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/APIR-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SECU-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SECU-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SECU-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ASPP-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ASPP-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ASPP-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ACMG-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ACMG-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/AHIST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/AHIST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/AHIST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/AHIST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ASIA-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ASIA-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ASIA-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ACMK-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HMRT-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HMRT-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HMRT-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ANTH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ANTH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ANTH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ANTH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ANTH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ANTH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HBIO-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HBIO-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HUEB-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HUEB-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HUEB-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HUEB-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CORP-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BACCT',
        'https://programsandcourses.anu.edu.au/2019/major/ACCT-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/COMP-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/INFS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BHLTH',
        'https://programsandcourses.anu.edu.au/2019/major/PHOT-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PHOT-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GSEC-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BPPOL',
        'https://programsandcourses.anu.edu.au/2019/major/ANVI-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CHEM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CHEM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BMEDS',
        'https://programsandcourses.anu.edu.au/2019/major/PMDR-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HIND-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HIND-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HIND-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HIND-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HIND-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HIND-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/INST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/INST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/INST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/INST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/INDN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/INDN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/INDN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/INDN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/INDN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/INDN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/INDS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/INDS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HIST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HIST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HIST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HIST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HIST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/HIST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/DEST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BDEVS',
        'https://programsandcourses.anu.edu.au/2019/major/DEST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/DEST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ANCH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ANCH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ANCH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ANCH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ANCH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/AGRK-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/AGRK-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/AGRK-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/AGRK-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/AGRK-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/RENE-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/RENE-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SUSY-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SUSY-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SUST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SUST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SUST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SUST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PECO-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PECO-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PECO-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PHIL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PHIL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PHIL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PHIL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/APNSN',
        'https://programsandcourses.anu.edu.au/2019/major/BUSN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ICOM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ICOM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ICOM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ICOM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ICOM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/IREL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/IREL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BIR',
        'https://programsandcourses.anu.edu.au/2019/major/IREL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/IREL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/IREL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BINBS',
        'https://programsandcourses.anu.edu.au/2019/major/INTB-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BINSS',
        'https://programsandcourses.anu.edu.au/2019/major/EART-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/EART-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/EART-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/EART-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GEOG-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GEOG-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GEOG-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GEOG-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GEOG-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GEOG-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GEOG-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PAST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PAST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PAST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PAST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PAST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/QFIN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/FURN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BBUSA',
        'https://programsandcourses.anu.edu.au/2019/major/MARK-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BADAN',
        'https://programsandcourses.anu.edu.au/2019/major/APST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/EURO-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/EURO-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/EURO-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/EURO-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PHOM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GERM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GERM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GERM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GERM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GERM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PSYC-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PSYC-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PSYC-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/APSYC',
        'https://programsandcourses.anu.edu.au/2019/major/GEND-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GEND-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GEND-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GEND-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ITAL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ITAL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ITAL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ITAL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/WARS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/WARS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/WARS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/WARS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/LATN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/LAMS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/LAMS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/LAMS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/LATN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/LATN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/LATN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/LATN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BPPE',
        'https://programsandcourses.anu.edu.au/2019/major/POLS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/POLS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/POLS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/POLS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BPLSC',
        'https://programsandcourses.anu.edu.au/2019/major/DIHU-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/DIHU-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/DIHU-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MATH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MATH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MATH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MATH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MMOD-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MMOD-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MMOD-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BMASC',
        'https://programsandcourses.anu.edu.au/2019/major/MFIN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MFIN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/DTSC-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MECO-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MECO-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/JPST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/JPST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/JPST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/JPST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/JPLN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/JPLN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/JPLN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/JPLN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/JPNS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/JPNS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/JPNS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/JPNS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/JPNS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MMSY-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MMSY-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MTSY-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MTSY-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SANS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SANS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SANS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SANS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SANS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PSTO-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/WASC-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/WASC-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CHIN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CHIN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CHIN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CHIN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CHIN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CHIN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CHST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CHST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CHST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/ALLB',
        'https://programsandcourses.anu.edu.au/2019/major/FREN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/FREN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/FREN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/FREN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/FREN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/FREN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/FREN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/FREN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PERS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PERS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PERS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PERS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/THAI-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/THAI-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/THAI-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/THAI-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/THAI-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MARS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MARS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MARS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MARS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/AUIS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/AUIS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PHYS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PHYS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BCRIM',
        'https://programsandcourses.anu.edu.au/2019/major/CRIM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CRIM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ENST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ENST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ENST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ENST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ENVS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ENVS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ENVS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ENVS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/GLAS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/THST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/BIAN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/BIAN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/BIAN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/BIAN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/BCHM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/BCHM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/BMSY-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/BMSY-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BBIOT',
        'https://programsandcourses.anu.edu.au/2019/major/ELCO-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ELCO-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CFVG-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BSTUD',
        'https://programsandcourses.anu.edu.au/2019/major/SOCY-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SOCY-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SOCY-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/ASSAE',
        'https://programsandcourses.anu.edu.au/2019/program/BSPSY',
        'https://programsandcourses.anu.edu.au/2019/major/SCOM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SCOM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/APHSC',
        'https://programsandcourses.anu.edu.au/2019/major/MGMT-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BACTS',
        'https://programsandcourses.anu.edu.au/2019/major/TEXT-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CMBI-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CMBI-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BECON',
        'https://programsandcourses.anu.edu.au/2019/major/ECST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ECST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ECST-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PAIN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/STAT-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/STDA-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/STAT-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CSEC-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CSEC-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CSEC-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ARCH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ARCH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ARCH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ARCH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ARCH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ARCH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BAPRC',
        'https://programsandcourses.anu.edu.au/2019/major/AHIT-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/AHIT-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/AHIT-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ENGL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ENGL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ENGL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ENGL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ENGL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/PERF-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SPAH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SPAH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SPAH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SPAH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SPAH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SPAH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SPAH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SPAH-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CSCI-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CSCI-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CSCI-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/QBIO-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/QBIO-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BDESN',
        'https://programsandcourses.anu.edu.au/2019/major/LING-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/LING-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/LING-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/LING-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/LING-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CPMK-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/REEN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/REEN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/REEN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/REEN-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/VIET-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/VIET-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/VIET-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/VIET-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/VIET-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SOFT-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/EEOB-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/EEOB-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/EEOB-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/EEOB-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/BGENE',
        'https://programsandcourses.anu.edu.au/2019/major/FINM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/program/AFEST',
        'https://programsandcourses.anu.edu.au/2019/major/ARAB-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ARAB-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ARAB-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ARAB-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ARAB-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ARAB-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/ARAB-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/CERM-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/SCUL-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/KORS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/KORS-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/KORE-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/KORE-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/KORE-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/KORE-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/KORE-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MUSC-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MUSY-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MUSC-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MUSC-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MTEC-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MTEC-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MTEC-MAJ',
        'https://programsandcourses.anu.edu.au/2019/major/MTEC-MAJ'
    ]
    C = set(C)
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'The Australian National University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en_a = response.xpath('//*[@id="top"]/div[5]/div[1]/div[1]/h1/span').extract()
        programme_en_a = ''.join(programme_en_a)
        programme_en_a = remove_tags(programme_en_a)
        programme_en = programme_en_a.replace('Bachelor of ','')
        # print(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 1

        #5.apply_pre #6.duration #7.duration_per
        teach_time_a = response.xpath("//span[@class='tooltip-area']").extract()
        teach_time_a = ''.join(teach_time_a)
        teach_time_a = remove_tags(teach_time_a)
        # print(teach_time_a)
        apply_pre = '$'
        if '1.5' in teach_time_a:
            duration = 1.5
        elif '2.5' in teach_time_a:
            duration = 2.5
        elif len(teach_time_a)!=0:
            duration = re.findall('\d+',teach_time_a)[0]
        else:
            duration = None
        duration_per = 1
        # print(duration,response.url)

        #8.apply_proces_en
        apply_proces_en = response.xpath('//*[@id="top"]/div[5]/div[1]/div[2]/div[1]/a[1]/@href').extract()
        apply_proces_en = ''.join(apply_proces_en)
        apply_proces_en = remove_tags(apply_proces_en)
        if len(apply_proces_en)< 15:
            apply_proces_en = 'https://programsandcourses.anu.edu.au/2019/program/'+apply_proces_en
        # print(apply_proces_en)

        #9.degree_name
        degree_name = programme_en_a
        # print(degree_name)


        #10.department
        department = response.xpath('//*[@id="top"]/div[5]/div[1]/div[1]/div/p/span').extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #11.overview_en
        overview_en = response.xpath('//*[@id="introduction"]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #12.rntry_requirements_en
        rntry_requirements_en = response.xpath('//*[@id="admission-and-fees"]/div').extract()
        rntry_requirements_en = ''.join(rntry_requirements_en)
        rntry_requirements_en = remove_class(rntry_requirements_en)
        # print(rntry_requirements_en)

        #13.tuition_fee
        tuition_fee = response.xpath('//*[@id="indicative-fees__international"]/dl/dd').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #14.tuition_fee_pre
        tuition_fee_pre = '$'

        #15.modules_en
        modules_en = response.xpath('//*[@id="study"]//div').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #16.ielts 18192021 #22.toefl 23242526
        if 'Ju' in programme_en:
            ielts = 7.0
            ielts_w = 6.0
            ielts_l = 6.0
            ielts_s = 6.0
            ielts_r = 6.0
            toefl = 100
            toefl_w = 22
            toefl_r = 22
            toefl_s = 22
            toefl_l = 22
        elif 'law' in programme_en:
            ielts = 7.0
            ielts_w = 6.0
            ielts_l = 6.0
            ielts_s = 6.0
            ielts_r = 6.0
            toefl = 100
            toefl_w = 22
            toefl_r = 22
            toefl_s = 22
            toefl_l = 22
        else:
            ielts = 6.5
            ielts_w = 6.0
            ielts_l = 6.0
            ielts_s = 6.0
            ielts_r = 6.0
            toefl = 80
            toefl_w = 20
            toefl_r = 20
            toefl_s = 18
            toefl_l = 18

        #27.major
        major = response.xpath("//*[contains(text(),'Major')]//following-sibling::div[1]//ul//li//@href").extract()
        # print(major)

        #28.career_en
        career_en = response.xpath("//*[contains(text(),'Career Option')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        item['career_en'] = career_en
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['apply_proces_en'] = apply_proces_en
        item['degree_name'] = degree_name
        item['department'] = department
        item['overview_en'] = overview_en
        item['rntry_requirements_en'] = rntry_requirements_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['modules_en'] = modules_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['toefl'] = toefl
        item['toefl_w'] = toefl_w
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['toefl_r'] = toefl_r
        item['apply_pre'] = apply_pre

        if len(major)!=0:
            for i in major:
                url_major = 'https://programsandcourses.anu.edu.au'+str(i)
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
                data = requests.get(url_major, headers=headers)
                response_major = etree.HTML(data.text)
                response_overview = response_major.xpath('//*[@id="introduction"]')
                response_overview = ''.join(response_overview).strip()
                response_modules = response_major.xpath('//*[@id="study"]/div')
                doc = ""
                if len(response_modules) > 0:
                    for a in response_modules:
                        doc += (etree.tostring(a, encoding='utf-8', pretty_print=False, method='html'))
                        doc = remove_class(doc)
                response_programme = response_major.xpath('//*[@id="skip-to"]/div[1]/div[1]/h1//text()')
                response_programme = ''.join(response_programme).strip()
                item['overview_en'] = response_overview
                item['modules_en'] = doc
                item['url'] = url_major
                item['programme_en'] = response_programme
                yield item
        else:
            item['overview_en'] = overview_en
            item['modules_en'] = modules_en
            item['url'] = url
            item['programme_en'] = programme_en
            yield item