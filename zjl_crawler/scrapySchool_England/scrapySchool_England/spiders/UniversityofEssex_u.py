# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/25 13:12'
import scrapy,json
import re
import requests
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from w3lib.html import remove_tags
from scrapySchool_England.clearSpace import  clear_space_str
import urllib.request
from  lxml import etree
class UniversityofEssexSpider(scrapy.Spider):
    name = 'UniversityofEssex_u'
    allowed_domains = ['essex.ac.uk/']
    start_urls = []
    C = [
        'https://www.essex.ac.uk/courses/ug00155/1/ba-european-studies-with-german?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00160/1/ba-european-studies-with-spanish?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00164/1/ba-film-studies?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00203/1/ba-history-with-film-studies?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00021/1/ba-art-history?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00022/1/ba-art-history-and-history?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00248/1/ba-literature-and-art-history?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00023/1/ba-art-history-and-modern-languages?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00025/1/ba-art-history-with-modern-languages?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00165/1/ba-film-studies-and-art-history?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00216/1/bsc-international-business-and-entrepreneurship?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00264/1/bsc-marketing?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00043/1/bba-business-administration?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00012/1/bsc-actuarial-science?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00278/1/bsc-mathematics-and-statistics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00269/1/bsc-mathematics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01289/1/ba-english-language-with-media-communication?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00132/1/ba-english-language-and-literature?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01086/1/ba-english-and-comparative-literature?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00139/1/ba-english-literature?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00098/1/ba-drama-and-literature?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00361/1/ba-psychology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00361/2/bsc-psychology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00092/1/ba-criminology-with-social-psychology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00362/1/bsc-psychology-with-cognitive-neuroscience?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01300/1/bsc-psychology-with-economics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01297/1/ba-business-economics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00252/1/ba-literature-and-sociology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00166/1/ba-film-studies-and-literature?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00126/1/ba-english-and-united-states-literature?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01045/1/ba-curatorial-studies?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00088/1/ba-creative-writing?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00189/1/ba-history?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00151/1/ba-european-studies?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00159/1/ba-european-studies-with-politics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00387/1/ba-sociology-with-human-rights?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00234/1/ba-latin-american-studies-with-human-rights?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01299/1/llb-law-with-criminology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01063/1/llb-law-with-business?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00124/1/llb-english-and-french-law?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00235/1/llb-law?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01021/1/llb-law-senior-status?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00076/1/beng-computer-systems-engineering?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00315/1/bsc-nursing-adult?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00315/2/bsc-nursing-adult?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00154/1/ba-european-studies-with-french?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00152/1/ba-european-studies-and-modern-languages?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00157/1/ba-european-studies-with-italian?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01116/1/bsc-tourism-management?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01275/1/bsc-finance-and-management?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00045/1/bsc-business-management?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00256/1/bsc-management-and-marketing?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00004/1/bsc-accounting-and-management?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00006/1/bsc-accounting-with-economics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01018/1/ba-financial-economics-and-accounting?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00046/1/ba-business-management-and-modern-languages?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00047/1/ba-business-management-with-a-modern-language?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00001/1/bsc-accounting?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00167/1/bsc-finance?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00002/1/bsc-accounting-and-finance?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00030/1/bsc-banking-and-finance?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00231/1/ba-latin-american-studies?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00389/1/ba-social-anthropology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00172/1/ba-financial-economics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00172/3/bsc-financial-economics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00258/3/bsc-management-economics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00258/1/ba-management-economics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00218/1/ba-international-economics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00218/3/bsc-international-economics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01304/2/bsc-economics-with-psychology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00103/1/ba-economics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00103/3/bsc-economics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00111/1/bsc-economics-with-mathematics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00105/1/bsc-economics-and-mathematics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00168/1/bsc-finance-and-mathematics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01112/1/ba-economics-with-a-modern-language?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01304/1/ba-economics-with-psychology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01265/1/bsc-economics-with-computing?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00191/1/ba-history-and-economics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00162/1/ba-film-and-creative-writing?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00221/1/ba-international-relations?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00222/1/ba-international-relations-and-modern-languages?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00375/1/ba-social-work?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00232/1/ba-latin-american-studies-with-business-management?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00321/1/ba-philosophy?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00325/1/ba-philosophy-and-history?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00330/1/ba-philosophy-and-politics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00331/1/ba-philosophy-and-sociology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00334/1/ba-philosophy-politics-and-economics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00322/1/ba-philosophy-and-art-history?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00335/1/ba-philosophy-religion-and-ethics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00332/1/ba-philosophy-with-human-rights?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01124/2/bsc-politics-and-international-relations?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00217/1/ba-international-development?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00343/1/ba-politics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00350/1/ba-politics-with-human-rights?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00293/1/ba-modern-history-and-politics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01124/1/ba-politics-and-international-relations?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00342/1/ba-political-theory-and-public-policy?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00106/1/ba-economics-and-politics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00384/1/ba-sociology-and-politics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01061/1/beng-robotic-engineering?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00282/1/bsc-mathematics-with-computing?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01136/1/ba-social-anthropology-with-human-rights?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00097/1/ba-drama?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01100/1/ba-journalism-and-politics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01090/1/ba-journalism-and-economics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01092/1/ba-journalism-and-sociology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01107/1/ba-journalism-and-philosophy?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01089/1/ba-journalism-and-criminology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01106/1/ba-journalism-and-liberal-arts?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01099/1/ba-journalism-with-human-rights?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01087/1/ba-journalism-and-modern-languages?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01094/1/ba-journalism-and-english-language?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01093/1/ba-journalism-with-business-management?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00230/1/ba-language-studies?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00294/1/ba-modern-languages?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01073/1/mlang-modern-languages-translation?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00176/1/ba-french-studies-and-modern-languages?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00180/1/ba-german-studies-and-modern-languages?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00395/1/ba-spanish-studies-and-modern-languages?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00226/1/ba-italian-studies-and-modern-languages?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00397/1/ba-spanish-portuguese-and-brazilian-studies?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00301/1/ba-modern-languages-with-latin-american-studies?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00326/1/ba-philosophy-and-law?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01049/1/llb-law-with-human-rights?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01298/1/llb-law-with-finance?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01050/1/llb-law-with-philosophy?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01052/1/llb-law-with-politics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01110/1/bsc-speech-and-language-therapy?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00327/1/ba-philosophy-and-literature?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00014/1/ba-american-studies-united-states?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00090/1/ba-criminology-and-american-studies?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00015/1/ba-american-studies-united-states-with-film?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00239/1/ba-liberal-arts?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00194/1/ba-history-and-literature?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00033/1/bsc-biochemistry?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00039/1/bsc-biomedical-science?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00038/1/bsc-biological-sciences?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01028/1/ba-therapeutic-care?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01096/1/ba-journalism-and-literature?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01055/1/ba-literature-and-creative-writing?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00316/1/bsc-nursing-mental-health?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00316/2/bsc-nursing-mental-health?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00341/1/ba-political-economics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01020/1/ba-multimedia-journalism?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00399/1/bsc-sports-and-exercise-science?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01057/1/bsc-sports-performance-and-coaching?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00403/1/bsc-sports-therapy?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01291/1/ba-criminology-with-criminal-law?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01296/1/ba-sociology-with-counselling-skills?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00378/1/ba-sociology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00089/1/ba-criminology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00372/1/ba-sociology-with-social-psychology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00289/1/ba-communications-and-digital-culture?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00388/1/ba-sociology-with-psychosocial-studies?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01132/1/bsc-sociology-with-applied-quantitative-research-methods?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00379/1/ba-sociology-and-criminology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01290/1/ba-criminology-with-counselling-skills?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00178/1/bsc-genetics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00263/1/bsc-marine-biology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01144/1/ba-global-studies-and-modern-languages?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00131/1/ba-english-language-and-linguistics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00296/1/ba-modern-languages-and-linguistics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00246/1/ba-english-language-and-sociology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00297/1/ba-modern-languages-and-teaching-english-as-a-foreign-language?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00295/1/ba-modern-languages-and-english-language?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00129/1/ba-teaching-english-as-a-foreign-language-tefl?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00285/1/bsc-mathematics-with-physics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00069/3/msci-computer-science?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00068/1/beng-computer-networks?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00117/2/meng-electronic-engineering?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00409/1/beng-communications-engineering?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00409/3/meng-communications-engineering?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00117/1/beng-electronic-engineering?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01034/1/bsc-data-science-and-analytics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00080/1/beng-computers-with-electronics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00066/1/bsc-computer-games?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00069/1/bsc-computer-science?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00291/1/ba-modern-history?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00204/1/ba-history-with-human-rights?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01054/1/ba-global-studies?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00292/1/ba-modern-history-and-international-relations?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00190/1/ba-history-and-criminology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00197/1/ba-history-and-sociology?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01121/1/ba-childhood-studies?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug01035/1/ba-psychoanalytic-studies?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00241/1/ba-linguistics?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00404/1/ba-stage-and-production-management',
        'https://www.essex.ac.uk/courses/ug00337/1/ba-physical-theatre?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00008/2/ba-acting',
        'https://www.essex.ac.uk/courses/ug00009/2/ba-acting-and-community-theatre?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00010/1/ba-acting-and-contemporary-theatre',
        'https://www.essex.ac.uk/courses/ug00008/1/ba-acting',
        'https://www.essex.ac.uk/courses/ug01119/1/ba-creative-producing-theatre-and-short-film?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00418/1/ba-world-performance?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00011/1/ba-acting-and-stage-combat?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00138/1/ba-english-language-and-language-development?startdate=19-10',
        'https://www.essex.ac.uk/courses/ug00212/1/bsc-information-and-communication-technology?startdate=19-10'
    ]

    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Essex'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="content"]//h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 1

        #5.degree_name
        degree_name = programme_en.split()[0]
        # print(degree_name)
        programme_en = programme_en.replace(degree_name,'').strip()
        # print(programme_en)

        #6.start_date
        start_date = response.xpath("//*[contains(text(),'Start date')]//following-sibling::select").extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        start_date = clear_space_str(start_date)
        if 'Oct 2018/19' in start_date:
            start_date = '2018-10,2019-10'
        else:
            start_date = '2018-9,2019-9'
        # print(start_date)

        #7.ucascode
        ucascode = response.xpath("//*[contains(text(),'UCAS code:')]//following-sibling::*").extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode)
        # print(ucascode)

        #8.duration #9.duration_per
        duration_list = response.xpath("//*[contains(text(),'Duration')]//following-sibling::*").extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        duration_a = re.findall('\d+',duration_list)[0]
        duration = duration_a
        duration_per = 1
        if int(duration)>5:
            duration_per = 3
        # print(duration,'(((',duration_per)

        #10.location
        location = response.xpath("//*[contains(text(),'Location')]//following-sibling::span").extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #11.department
        department_a =response.xpath("//*[contains(text(),'Based in')]//following-sibling::*").extract()
        department_a =''.join(department_a)
        department_a = remove_tags(department_a)
        if len(department_a)>500:
            department = 'N/A'
        else:
            department = department_a
        # print(department)

        #12.overview_en
        overview_en = response.xpath('//*[@id="overview"]//p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #13.ielts 14151617
        ielts_list = response.xpath('//*[@id="entry-requirements"]//text()').extract()
        ielts_list = ''.join(ielts_list)
        ielts = re.findall(r'[567]\.\d',ielts_list)
        # print(ielts,response.url)
        if len(ielts) == 1:
            a = ielts[0]
            ielts = a
            ielts_s = float(a) - 0.5
            ielts_w = float(a) - 0.5
            ielts_l = float(a) - 0.5
            ielts_r = float(a) - 0.5
        elif len(ielts) ==2:
            a = ielts[0]
            b = ielts[1]
            ielts = a
            ielts_w = b
            ielts_r = b
            ielts_l = b
            ielts_s = b
        else:
            ielts = 6.0
            ielts_w = 5.5
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        # print(ielts,ielts_w,ielts_r,ielts_l,ielts_s)

        #18.modules_en
        modules_en = response.xpath("//div[@class='tabs__panels content-padding']").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        modules_en = clear_space_str(modules_en)
        # print(modules_en)

        #19.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'International fee')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = tuition_fee.replace(',','')
        tuition_fee = tuition_fee.replace('£','')
        if tuition_fee == 'TBC':
            tuition_fee = None
        elif len(tuition_fee) >=200:
            tuition_fee = None
        else:
            pass
        # print(tuition_fee)

        #20.tuition_fee_pre
        tuition_fee_pre = '£'

        #21.apply_proces_en
        apply_proces_en = 'https://www1.essex.ac.uk/pgapply/login.aspx'

        #22.alevel
        alevel_a = response.xpath("//*[contains(text(),'UK entry requirements')]//following-sibling::p[1]").extract()
        alevel_a = ''.join(alevel_a)
        alevel_a = remove_tags(alevel_a)
        # print(alevel_a)
        # alevel = re.findall(r'evels:(\W)',alevel_a)[0]
        try:
            if ','in alevel_a:
                alevel = re.findall(r'levels:(.*),',alevel_a)[0]
            elif 'GCSE' in alevel_a:
                alevel = re.findall(r'levels:(.*)GCSE',alevel_a)[0]
            else:alevel = alevel_a
        except:
            alevel = 'N/A'
        alevel = alevel.replace('A-levels:','').strip()
        # print(alevel)


        #23.require_chinese_en
        # chi_url = re.findall(r'courses/ug(.*)/',url)[0]
        # chi_url1 = re.findall('\d+',chi_url)
        # a = chi_url1[0]
        # b = chi_url1[1]
        # # print(a)
        # # print(b)
        # chi_url2 = 'https://www.essex.ac.uk/api/sitecore/coursePage/EntryRequirementInternational?mastercourseid=UG'+str(a)+'&subgroupcode='+str(b)+'&courseyear=19&countrykey=631'
        # headers = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        # # print(chi_url2)
        # data = requests.get(chi_url2,headers=headers)
        # data_list = etree.HTML(data.text)
        # require_chinese_en = data_list.xpath('/html/body/div/p/text()')
        # require_chinese_en = ''.join(require_chinese_en)
        # require_chinese_en = '<p>'+require_chinese_en+'</p>'
        # print(require_chinese_en)

        #24.apply_documents_en

        apply_documents_en= "<p>Necessary documents When you apply to study with us, you'll need to provide a number of supporting documents - we can't process your application until we have these. Some of these documents you will have to upload with your application, others you may be able to upload at a later date. We may ask to see original documents if you are offered a place. English language If you have received your test results you may include a copy with your application. The main tests we accept are IELTS, TOEFL or Pearson, and the test must be less than two years old at the time of admission. The IELTS requirement for your course is listed on our Postgraduate Research Finder. You can also see more detailed information about English language requirements here (.pdf) Transcripts Official transcript(s), in English or a certified translation of your academic results to date, showing marks or grades, must be provided at the time you make your application. (Transcripts are not required from current or previous University of Essex students, or from students who have previously completed a degree at Colchester Institute awarded by the University of Essex). CV A CV is required for some research degrees at the time of application. Research proposal Requirements vary across departments but two references and a research proposal are required for all research degrees.  A research proposal is required at application stage for most research degrees. Think about your research idea - during your PhD you will conduct and present the results of your original investigations and research. You need to ensure that your research topic will be interesting enough for three or four years. Start to research your topic by reading around your subject area and begin to think what you might like to include in your research proposal. Get in touch with a suitable department by contacting the Graduate Director - you might still be developing your idea at this stage, but it would be great if you could send a short description of your research area and a copy of your CV. This does not need to be longer than one A4 page. You can search for a department or supervisor through our Postgraduate Research Finder. Writing your proposalYour research proposal is an important part of your application for a research degree. Use it to explain your personal and academic goals in undertaking an extended period of research, and reﬂect on the contribution you will make to the development of new knowledge, ideas and solutions. Also comment on how your research interests fit with the academic focus and expertise at Essex  Your research proposal needs to demonstrate that you have, or are able to develop, the competencies and skills needed to complete your project, within the time and resources available. The quality of your writing is important and a good research proposal may be rejected if it is poorly expressed or badly presented. Many of our departments, schools and centres offer more detailed guidance on preparing a research proposal on their web pages. If you are applying for funding, ensure your proposal fulfils the requirements of your preferred funding body. Your research proposal should include: a working title and key words a summary of the aims and objectives of your research an outline of the ways you meet these aims and objectives, referring to research methods and specific resources you use evidence of your awareness of relevant literature and theoretical approaches an overview of the expected outcomes and the original contribution your research will make to existing bodies of knowledge a brief statement on how your research interests tie in with those found in the department, school or centrePersonal statement If you are applying for a taught course and you need a Tier 4 student visa to study in the UK, then a personal statement (no more than 500 words) is required at the time you make your application, and this should refer specifically to your reasons for wishing to study in the UK, and why you have chosen your area of study. Please remember to include details of any relevant work experience, why you think your academic strengths are suited to your area of study, and how this study will assist you to realise your career objectives. References We require two references from you at the application stage.References should be recent and verifiable, on official institution paper, signed and dated by the referee. If a referee wishes to provide an email reference, it must be sent from an official email account (for example, not Yahoo, Gmail or Hotmail).<\p>"
        #25.ib
        ib = response.xpath("//*[contains(text(),'UK entry requirements')]//following-sibling::p[2]").extract()
        ib = ''.join(ib)
        ib =  remove_tags(ib)
        # print(ib)

        #26.career_en
        career_en = response.xpath("//*[contains(text(),'Your future')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)


        item['ucascode'] = ucascode
        item['ib'] = ib
        item['alevel'] = alevel
        item['apply_documents_en'] = apply_documents_en
        # item['require_chinese_en'] = require_chinese_en
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['start_date'] = start_date
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['location'] = location
        item['department'] = department
        item['overview_en'] = overview_en
        item['ielts'] = ielts
        item['ielts_w'] = ielts_w
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['modules_en'] = modules_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_proces_en'] = apply_proces_en
        item['career_en'] = career_en
        # yield item