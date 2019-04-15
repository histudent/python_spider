# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
import requests
from lxml import etree
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration

class QueensUniversityBelfast_USpider(scrapy.Spider):
    name = "QueensUniversityBelfast_U"
    # 研究领域链接
    start_urls = ["http://www.qub.ac.uk/courses/undergraduate/?keyword="]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        links = ["http://www.qub.ac.uk/courses/undergraduate/accounting-bsc-n400/",
"http://www.qub.ac.uk/courses/undergraduate/accounting-french-bsc-n4r1/",
"http://www.qub.ac.uk/courses/undergraduate/accounting-spanish-bsc-n4r4/",
"http://www.qub.ac.uk/courses/undergraduate/actuarial-science-risk-management-bsc-n323/",
"http://www.qub.ac.uk/courses/undergraduate/adult-nursing-bsc-b74a/",
"http://www.qub.ac.uk/courses/undergraduate/adult-nursing-bsc-b740/",
"http://www.qub.ac.uk/courses/undergraduate/aerospace-engineering-beng-h400/",
"http://www.qub.ac.uk/courses/undergraduate/aerospace-engineering-meng-h402/",
"http://www.qub.ac.uk/courses/undergraduate/aerospace-engineering-sandwich-meng-h405/",
"http://www.qub.ac.uk/courses/undergraduate/aerospace-engineering-sandwich-beng-h404/",
"http://www.qub.ac.uk/courses/undergraduate/agricultural-technology-bsc-d473/",
"http://www.qub.ac.uk/courses/undergraduate/agricultural-technology-bsc-d470/",
"http://www.qub.ac.uk/courses/undergraduate/anthropology-ba-l600/",
"http://www.qub.ac.uk/courses/undergraduate/anthropology-english-ba-ql36/",
"http://www.qub.ac.uk/courses/undergraduate/anthropology-french-ba-rl16/",
"http://www.qub.ac.uk/courses/undergraduate/anthropology-history-ba-vl16/",
"http://www.qub.ac.uk/courses/undergraduate/anthropology-irish-ba-ql56/",
"http://www.qub.ac.uk/courses/undergraduate/anthropology-spanish-ba-lr64/",
"http://www.qub.ac.uk/courses/undergraduate/applied-mathematics-physics-bsc-gf13/",
"http://www.qub.ac.uk/courses/undergraduate/applied-mathematics-physics-msci-gfc3/",
"http://www.qub.ac.uk/courses/undergraduate/archaeology-msci-v403/",
"http://www.qub.ac.uk/courses/undergraduate/archaeology-ba-v402/",
"http://www.qub.ac.uk/courses/undergraduate/archaeology-palaeoecology-bsc-v400/",
"http://www.qub.ac.uk/courses/undergraduate/archaeology-history-ba-vv41/",
"http://www.qub.ac.uk/courses/undergraduate/archaeology-irish-ba-vq45/",
"http://www.qub.ac.uk/courses/undergraduate/archaeology-french-ba-v4r1/",
"http://www.qub.ac.uk/courses/undergraduate/archaeology-portuguese-ba-v4r5/",
"http://www.qub.ac.uk/courses/undergraduate/archaeology-spanish-ba-v4r4/",
"http://www.qub.ac.uk/courses/undergraduate/archaeologypalaeoecology-geography-bsc-vf48/",
"http://www.qub.ac.uk/courses/undergraduate/architecture-bsc-k100/",
"http://www.qub.ac.uk/courses/undergraduate/audio-engineering-bsc-j930/",
"http://www.qub.ac.uk/courses/undergraduate/biochemistry-bsc-c704/",
"http://www.qub.ac.uk/courses/undergraduate/biochemistry-bsc-c700/",
"http://www.qub.ac.uk/courses/undergraduate/biochemistry-msci-c702/",
"http://www.qub.ac.uk/courses/undergraduate/biochemistry-msci-c705/",
"http://www.qub.ac.uk/courses/undergraduate/biological-sciences-bsc-c100/",
"http://www.qub.ac.uk/courses/undergraduate/biological-sciences-msci-c102/",
"http://www.qub.ac.uk/courses/undergraduate/biological-sciences-bsc-c104/",
"http://www.qub.ac.uk/courses/undergraduate/biological-sciences-msci-c105/",
"http://www.qub.ac.uk/courses/undergraduate/biomedical-science-bsc-b940/",
"http://www.qub.ac.uk/courses/undergraduate/broadcast-production-ba-p310/",
"http://www.qub.ac.uk/courses/undergraduate/business-economics-bsc-l110/",
"http://www.qub.ac.uk/courses/undergraduate/business-information-technology-bsc-gn51/",
"http://www.qub.ac.uk/courses/undergraduate/business-management-placement-bsc/",
"http://www.qub.ac.uk/courses/undergraduate/chemical-engineering-beng-h800/",
"http://www.qub.ac.uk/courses/undergraduate/chemical-engineering-meng-h802/",
"http://www.qub.ac.uk/courses/undergraduate/chemical-engineering-beng-h804/",
"http://www.qub.ac.uk/courses/undergraduate/chemical-engineering-meng-h805/",
"http://www.qub.ac.uk/courses/undergraduate/chemical-technology-meng-h881/",
"http://www.qub.ac.uk/courses/undergraduate/chemical-technology-msci-hh80/",
"http://www.qub.ac.uk/courses/undergraduate/chemistry-msci-f105/",
"http://www.qub.ac.uk/courses/undergraduate/chemistry-bsc-f100/",
"http://www.qub.ac.uk/courses/undergraduate/chemistry-msci-f107/",
"http://www.qub.ac.uk/courses/undergraduate/chemistry-french-msci-fr11/",
"http://www.qub.ac.uk/courses/undergraduate/chemistry-spanish-msci-f1r4/",
"http://www.qub.ac.uk/courses/undergraduate/chemistry-study-abroad-msci-f106/",
"http://www.qub.ac.uk/courses/undergraduate/childrens-nursing-bsc-b730/",
"http://www.qub.ac.uk/courses/undergraduate/civil-engineering-beng-h204/",
"http://www.qub.ac.uk/courses/undergraduate/civil-engineering-meng-h202/",
"http://www.qub.ac.uk/courses/undergraduate/civil-engineering-meng-h205/",
"http://www.qub.ac.uk/courses/undergraduate/civil-engineering-beng-h200/",
"http://www.qub.ac.uk/courses/undergraduate/common-civil-law-french-llb-m2r1/",
"http://www.qub.ac.uk/courses/undergraduate/common-civil-law-major-hispanic-studies-llb-m2r4/",
"http://www.qub.ac.uk/courses/undergraduate/computer-science-beng-g404/",
"http://www.qub.ac.uk/courses/undergraduate/computer-science-meng-g405/",
"http://www.qub.ac.uk/courses/undergraduate/computer-science-bsc-g400/",
"http://www.qub.ac.uk/courses/undergraduate/computer-science-meng-g402/",
"http://www.qub.ac.uk/courses/undergraduate/computing-information-technology-bsc-gg45/",
"http://www.qub.ac.uk/courses/undergraduate/criminology-ba-m900/",
"http://www.qub.ac.uk/courses/undergraduate/criminology-social-policy-ba-ml94/",
"http://www.qub.ac.uk/courses/undergraduate/criminology-sociology-ba-ml93/",
"http://www.qub.ac.uk/courses/undergraduate/dentistry-bds-a200/",
"http://www.qub.ac.uk/courses/undergraduate/2018/divinity-bd/",
"http://www.qub.ac.uk/courses/undergraduate/drama-ba-w400/",
"http://www.qub.ac.uk/courses/undergraduate/drama-english-ba-wq43/",
"http://www.qub.ac.uk/courses/undergraduate/economics-bsc-l100/",
"http://www.qub.ac.uk/courses/undergraduate/economics-accounting-bsc-ln14/",
"http://www.qub.ac.uk/courses/undergraduate/economics-finance-bsc-l1n3/",
"http://www.qub.ac.uk/courses/undergraduate/economics-french-bsc-l1r1/",
"http://www.qub.ac.uk/courses/undergraduate/economics-spanish-bsc-l1r4/",
"http://www.qub.ac.uk/courses/undergraduate/electrical-electronic-engineering-beng-h600/",
"http://www.qub.ac.uk/courses/undergraduate/electrical-electronic-engineering-beng-h604/",
"http://www.qub.ac.uk/courses/undergraduate/electrical-electronic-engineering-meng-h605/",
"http://www.qub.ac.uk/courses/undergraduate/electrical-electronic-engineering-meng-h602/",
"http://www.qub.ac.uk/courses/undergraduate/english-ba-q300/",
"http://www.qub.ac.uk/courses/undergraduate/english-film-studies-ba-qw36/",
"http://www.qub.ac.uk/courses/undergraduate/english-french-ba-qr31/",
"http://www.qub.ac.uk/courses/undergraduate/english-history-ba-qv31/",
"http://www.qub.ac.uk/courses/undergraduate/english-irish-ba-qq53/",
"http://www.qub.ac.uk/courses/undergraduate/english-linguistics-ba-qq31/",
"http://www.qub.ac.uk/courses/undergraduate/english-philosophy-ba-qv35/",
"http://www.qub.ac.uk/courses/undergraduate/english-politics-ba-ql32/",
"http://www.qub.ac.uk/courses/undergraduate/english-sociology-ba-ql33/",
"http://www.qub.ac.uk/courses/undergraduate/english-spanish-ba-qr34/",
"http://www.qub.ac.uk/courses/undergraduate/english-creative-writing-ba-q3w8/",
"http://www.qub.ac.uk/courses/undergraduate/environmental-civil-engineering-meng-h255/",
"http://www.qub.ac.uk/courses/undergraduate/environmental-civil-engineering-meng-h252/",
"http://www.qub.ac.uk/courses/undergraduate/environmental-management-bsc-f850/",
"http://www.qub.ac.uk/courses/undergraduate/environmental-management-bsc-f854/",
"http://www.qub.ac.uk/courses/undergraduate/european-planning-mplan-k490/",
"http://www.qub.ac.uk/courses/undergraduate/film-theatre-making-ba-ww65/",
"http://www.qub.ac.uk/courses/undergraduate/film-studies-production-ba-w600/",
"http://www.qub.ac.uk/courses/undergraduate/finance-bsc-n300/",
"http://www.qub.ac.uk/courses/undergraduate/food-quality-safety-nutrition-msci-bd46/",
"http://www.qub.ac.uk/courses/undergraduate/food-quality-safety-nutrition-bsc-db6k/",
"http://www.qub.ac.uk/courses/undergraduate/food-quality-safety-nutrition-msci-db64/",
"http://www.qub.ac.uk/courses/undergraduate/food-quality-safety-nutrition-bsc-bdk6/",
"http://www.qub.ac.uk/courses/undergraduate/food-science-food-security-msci-d990/",
"http://www.qub.ac.uk/courses/undergraduate/food-science-food-security-msci-d991/",
"http://www.qub.ac.uk/courses/undergraduate/french-ba-r120/",
"http://www.qub.ac.uk/courses/undergraduate/french-history-ba-rv11/",
"http://www.qub.ac.uk/courses/undergraduate/french-international-studies-ba-rlc2/",
"http://www.qub.ac.uk/courses/undergraduate/french-irish-ba-qr51/",
"http://www.qub.ac.uk/courses/undergraduate/french-politics-ba-rl12/",
"http://www.qub.ac.uk/courses/undergraduate/french-portuguese-ba-rr15/",
"http://www.qub.ac.uk/courses/undergraduate/french-spanish-ba-rr14/",
"http://www.qub.ac.uk/courses/undergraduate/geography-bsc-f800/",
"http://www.qub.ac.uk/courses/undergraduate/geography-a-language-bsc-f8rx/",
"http://www.qub.ac.uk/courses/undergraduate/history-ba-v140/",
"http://www.qub.ac.uk/courses/undergraduate/history-international-studies-ba-lv21/",
"http://www.qub.ac.uk/courses/undergraduate/history-irish-ba-qv51/",
"http://www.qub.ac.uk/courses/undergraduate/history-philosophy-ba-vv1m/",
"http://www.qub.ac.uk/courses/undergraduate/history-politics-ba-vl12/",
"http://www.qub.ac.uk/courses/undergraduate/history-sociology-ba-vl13/",
"http://www.qub.ac.uk/courses/undergraduate/history-spanish-ba-rv41/",
"http://www.qub.ac.uk/courses/undergraduate/human-biology-bsc-b100/",
"http://www.qub.ac.uk/courses/undergraduate/international-business-french-bsc-n1r1/",
"http://www.qub.ac.uk/courses/undergraduate/international-business-german-bsc-n2r2/",
"http://www.qub.ac.uk/courses/undergraduate/international-business-mandarin-bsc-n1r9/",
"http://www.qub.ac.uk/courses/undergraduate/international-business-portuguese-bsc-n2r5/",
"http://www.qub.ac.uk/courses/undergraduate/international-business-spanish-bsc-n1r4/",
"http://www.qub.ac.uk/courses/undergraduate/international-politics-conflict-studies-ba-l253/",
"http://www.qub.ac.uk/courses/undergraduate/international-studies-irish-ba-lqf5/",
"http://www.qub.ac.uk/courses/undergraduate/international-studies-politics-ba-l290/",
"http://www.qub.ac.uk/courses/undergraduate/international-studies-spanish-ba-lrf4/",
"http://www.qub.ac.uk/courses/undergraduate/irish-ba-q504/",
"http://www.qub.ac.uk/courses/undergraduate/irish-politics-ba-ql52/",
"http://www.qub.ac.uk/courses/undergraduate/irish-spanish-ba-qr54/",
"http://www.qub.ac.uk/courses/undergraduate/law-llb-m100/",
"http://www.qub.ac.uk/courses/undergraduate/law-major-politics-llb-m1l2/",
"http://www.qub.ac.uk/courses/undergraduate/actuarial-science-risk-management-bsc-n323/",
"http://www.qub.ac.uk/courses/undergraduate/learning-disability-nursing-bsc-b761/",
"http://www.qub.ac.uk/courses/undergraduate/2018/master-of-liberal-arts-mlibarts-y300/",
"http://www.qub.ac.uk/courses/undergraduate/liberal-arts-mlibarts-y300/",
"http://www.qub.ac.uk/courses/undergraduate/marine-biology-msci-c165/",
"http://www.qub.ac.uk/courses/undergraduate/marine-biology-bsc-c160/",
"http://www.qub.ac.uk/courses/undergraduate/marine-biology-bsc-c164/",
"http://www.qub.ac.uk/courses/undergraduate/marine-biology-msci-c162/",
"http://www.qub.ac.uk/courses/undergraduate/mathematics-msci-g103/",
"http://www.qub.ac.uk/courses/undergraduate/mathematics-bsc-g100/",
"http://www.qub.ac.uk/courses/undergraduate/mathematics-computer-science-msci-ggk1/",
"http://www.qub.ac.uk/courses/undergraduate/mathematics-computer-science-bsc-gg41/",
"http://www.qub.ac.uk/courses/undergraduate/mathematics-statistics-research-msci-ggc3/",
"http://www.qub.ac.uk/courses/undergraduate/mathematics-statistics-research-bsc-gg13/",
"http://www.qub.ac.uk/courses/undergraduate/mathematics-extended-studies-in-europe-bsc-g104/",
"http://www.qub.ac.uk/courses/undergraduate/mathematics-finance-bsc-g1n3/",
"http://www.qub.ac.uk/courses/undergraduate/mechanical-engineering-meng-h303/",
"http://www.qub.ac.uk/courses/undergraduate/mechanical-engineering-beng-h304/",
"http://www.qub.ac.uk/courses/undergraduate/mechanical-engineering-beng-h300/",
"http://www.qub.ac.uk/courses/undergraduate/mechanical-engineering-meng-h305/",
"http://www.qub.ac.uk/courses/undergraduate/medicinal-chemistry-bsc-f150/",
"http://www.qub.ac.uk/courses/undergraduate/medicinal-chemistry-msci-f15a/",
"http://www.qub.ac.uk/courses/undergraduate/medicinal-chemistry-bsc-f154/",
"http://www.qub.ac.uk/courses/undergraduate/medicine-mb-a100/",
"http://www.qub.ac.uk/courses/undergraduate/mental-health-nursing-bsc-b760/",
"http://www.qub.ac.uk/courses/undergraduate/microbiology-bsc-c504/",
"http://www.qub.ac.uk/courses/undergraduate/microbiology-bsc-c500/",
"http://www.qub.ac.uk/courses/undergraduate/microbiology-msci-c502/",
"http://www.qub.ac.uk/courses/undergraduate/microbiology-msci-c505/",
"http://www.qub.ac.uk/courses/undergraduate/midwifery-sciences-bsc-b720/",
"http://www.qub.ac.uk/courses/undergraduate/music-bmus-w302/",
"http://www.qub.ac.uk/courses/undergraduate/music-audio-production-ba-w374/",
"http://www.qub.ac.uk/courses/undergraduate/music-sound-design-ba-w371/",
"http://www.qub.ac.uk/courses/undergraduate/music-performance-ba-w310/",
"http://www.qub.ac.uk/courses/undergraduate/pharmaceutical-biotechnology-bsc-b212/",
"http://www.qub.ac.uk/courses/undergraduate/pharmaceutical-biotechnology-sandwich-bsc-b213/",
"http://www.qub.ac.uk/courses/undergraduate/pharmaceutical-sciences-bsc-b210/",
"http://www.qub.ac.uk/courses/undergraduate/pharmaceutical-sciences-sandwich-bsc-b211/",
"http://www.qub.ac.uk/courses/undergraduate/pharmacy-mpharm-b230/",
"http://www.qub.ac.uk/courses/undergraduate/philosophy-ba-v500/",
"http://www.qub.ac.uk/courses/undergraduate/philosophy-politics-ba-vlm2/",
"http://www.qub.ac.uk/courses/undergraduate/physics-bsc-f300/",
"http://www.qub.ac.uk/courses/undergraduate/physics-msci-f303/",
"http://www.qub.ac.uk/courses/undergraduate/physics-extended-studies-in-europe-msci-f309/",
"http://www.qub.ac.uk/courses/undergraduate/physics-astrophysics-bsc-f3f5/",
"http://www.qub.ac.uk/courses/undergraduate/physics-astrophysics-msci-f3fm/",
"http://www.qub.ac.uk/courses/undergraduate/physics-medical-applications-bsc-f3b9/",
"http://www.qub.ac.uk/courses/undergraduate/physics-medical-applications-msci-f3bx/",
"http://www.qub.ac.uk/courses/undergraduate/physics-wth-extended-studies-in-europe-bsc-f308/",
"http://www.qub.ac.uk/courses/undergraduate/planning-environment-development-bsc-k430/",
"http://www.qub.ac.uk/courses/undergraduate/politics-ba-l200/",
"http://www.qub.ac.uk/courses/undergraduate/politics-spanish-ba-lr24/",
"http://www.qub.ac.uk/courses/undergraduate/politics-philosophy-economics-ba-lv00/",
"http://www.qub.ac.uk/courses/undergraduate/product-design-engineering-beng-h150/",
"http://www.qub.ac.uk/courses/undergraduate/product-design-engineering-beng-h151/",
"http://www.qub.ac.uk/courses/undergraduate/product-design-engineering-meng-h155/",
"http://www.qub.ac.uk/courses/undergraduate/product-design-engineering-meng-h152/",
"http://www.qub.ac.uk/courses/undergraduate/psychology-bsc-c800/",
"http://www.qub.ac.uk/courses/undergraduate/social-policy-sociology-ba-ll43/",
"http://www.qub.ac.uk/courses/undergraduate/social-work-bsw-l500/",
"http://www.qub.ac.uk/courses/undergraduate/social-work-relevant-degree-entry-bsw-l501/",
"http://www.qub.ac.uk/courses/undergraduate/sociology-ba-l300/",
"http://www.qub.ac.uk/courses/undergraduate/software-electronic-systems-engineering-meng-gh6q/",
"http://www.qub.ac.uk/courses/undergraduate/software-electronic-systems-engineering-beng-gh67/",
"http://www.qub.ac.uk/courses/undergraduate/software-electronic-systems-engineering-beng-gh6p/",
"http://www.qub.ac.uk/courses/undergraduate/software-electronic-systems-engineering-meng-gh68/",
"http://www.qub.ac.uk/courses/undergraduate/software-engineering-meng-g605/",
"http://www.qub.ac.uk/courses/undergraduate/software-engineering-beng-g604/",
"http://www.qub.ac.uk/courses/undergraduate/software-engineering-meng-g602/",
"http://www.qub.ac.uk/courses/undergraduate/software-engineering-digital-technology-partnership-beng-g606/",
"http://www.qub.ac.uk/courses/undergraduate/spanish-ba-r410/",
"http://www.qub.ac.uk/courses/undergraduate/spanish-portuguese-studies-ba-rr45/",
"http://www.qub.ac.uk/courses/undergraduate/structural-engineering-architecture-meng-h2kc/",
"http://www.qub.ac.uk/courses/undergraduate/structural-engineering-architecture-meng-h2k1/",
"http://www.qub.ac.uk/courses/undergraduate/theology-bd-v600/",
"http://www.qub.ac.uk/courses/undergraduate/theology-ba-v610/",
"http://www.qub.ac.uk/courses/undergraduate/theoretical-physics-bsc-f340/",
"http://www.qub.ac.uk/courses/undergraduate/theoretical-physics-msci-f344/",
"http://www.qub.ac.uk/courses/undergraduate/zoology-bsc-c300/",
"http://www.qub.ac.uk/courses/undergraduate/zoology-bsc-c301/",
"http://www.qub.ac.uk/courses/undergraduate/zoology-msci-c305/",
"http://www.qub.ac.uk/courses/undergraduate/zoology-msci-c302/", ]
        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "Queen's University Belfast"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:

            alevel = response.xpath(
                "//b[contains(text(),'A level requirements')]/..//text()").extract()
            if len(alevel) > 0:
                item['alevel'] = clear_lianxu_space(alevel)
            print("item['alevel'] = ", item['alevel'])

            ib = response.xpath(
                "//b[contains(text(),'International Baccalaureate Diploma')]/..//text()").extract()
            item['ib'] = clear_lianxu_space(ib)
            print("item['ib'] = ", item['ib'])


            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/"+item['university']+str(item['degree_type'])+".txt", 'w', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)
