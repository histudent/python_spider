import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime
import json
from w3lib.html import remove_tags

class AstonUniversity_USpider(scrapy.Spider):
    name = "AstonUniversity_U"
    start_urls = ['http://w01.aston.ac.uk/data/core/content/courses.j2d?types[]=fdy&types[]=fnd&types[]=ug']

    def parse(self, response):
        links = ["http://www.aston.ac.uk/study/undergraduate/courses/lhs/bsc-optometry/",
"http://www.aston.ac.uk/study/undergraduate/courses/lhs/bsc-optometry/",
"http://www.aston.ac.uk/study/undergraduate/courses/lhs/pharmacy/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/meng-chemical-engineering/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/politics-sociology/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/politics-social-policy/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/bsc-politics-with-international-relations/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/sociology-social-policy/sociology-international-relations/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/international-relations-social-policy/",
"http://www.aston.ac.uk/study/undergraduate/courses/joint-honours/politics-business/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/history-combinations/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/history-combinations/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/history-combinations/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/history-combinations/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/history-combinations/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/history-combinations/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/history-combinations/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/international-business-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/international-business-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/international-business-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/international-business-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/international-business-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/international-business-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/international-business-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/lhs/biomedical-sciences/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/english-language/englishlanguage/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-language-and-literature/",
"http://www.aston.ac.uk/study/undergraduate/courses/joint-honours/politics-and-economics/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-literature-and-politics/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-literature-and-sociology/",
"http://www.aston.ac.uk/study/undergraduate/courses/joint-honours/sociology-business/",
"http://www.aston.ac.uk/study/undergraduate/courses/joint-honours/public-policy-business/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-literature-and-international-relations/",
"http://www.aston.ac.uk/study/undergraduate/courses/joint-honours/international-relations-business/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/english-language/englishlanguage-social-policy/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/politics-english-language/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/international-relations-english-language/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/sociology-social-policy/english-language-sociology/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/english-language/bsc-business-management-and-english-language/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/frenchandgerman/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-literature-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-literature-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-literature-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-language-modern-languages/%20",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-language-modern-languages/%20",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-language-modern-languages/%20",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/german-spanish/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/frenchandspanish/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/french/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/bsc-spanish/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/german/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/international-relations-and-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/international-relations-and-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/international-relations-and-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/lhs/bsc-biochemistry/",
"http://www.aston.ac.uk/study/undergraduate/courses/lhs/human-biology/",
"http://www.aston.ac.uk/study/undergraduate/courses/lhs/biology/",
"http://www.aston.ac.uk/study/undergraduate/courses/lhs/mbiol/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/beng-chemical-engineering/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-applied-chemistry/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/beng-electrical-power-engineering/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/meng-electronic-engineering-and-computer-science/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/meng-electrical-and-electronic-engineering/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/mathematics-economics/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/business-mathematics/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-computer-science-and-mathematics/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/meng-mechanical-engineering/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-mathematics/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-mathematics-for-industry/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-computer-science/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-cybersecurity/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-computer-science-with-business/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-computer-science-with-multimedia/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-mathematics-with-computing/",
"http://www.aston.ac.uk/study/undergraduate/courses/lhs/bsc-neuroscience/",
"http://www.aston.ac.uk/study/undergraduate/courses/lhs/psychology/",
"http://www.aston.ac.uk/study/undergraduate/courses/lhs/psychology/",
"http://www.aston.ac.uk/study/undergraduate/courses/joint-honours/business-psychology/",
"http://www.aston.ac.uk/study/undergraduate/courses/joint-honours/psychology-marketing/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/sociology-social-policy/sociology/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/sociology-social-policy/sociology-and-social-policy/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-construction-project-management/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-business-supply-chain-management/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-product-design-management/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-industrial-product-design/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-chemistry-with-biotechnology/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-chemistry/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/beng-electronic-engineering-and-computer-science/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/beng-electrical-and-electronic-engineering/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/beng-communications-engineering/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-applied-physics/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/mphys-applied-physics/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/beng-mechanical-engineering/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/beng-design-engineering/",
"http://www.aston.ac.uk/study/undergraduate/courses/lhs/biomedical-engineering/",
"http://www.aston.ac.uk/study/undergraduate/courses/lhs/biomedical-engineering/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-logistics-with-supply-chain-management/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-logistics-with-purchasing-management/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-logistics-with-transport-management/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/beng-electromechanical-engineering/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-transport-product-design/",
"http://www.aston.ac.uk/study/undergraduate/courses/joint-honours/psychology-sociology/",
"http://www.aston.ac.uk/study/undergraduate/courses/lhs/bsc-healthcare-science-audiology/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/economics-management/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/marketing/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/llb-law/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/llb-law-with-management/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/international-business-management/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/international-business-economics/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/human-resource-management/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/business-computing-it/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/business-management/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/finance/",
"http://www.aston.ac.uk/study/undergraduate/courses/abs/aston-business-school/accounting-for-management/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/sociology-social-policy/bsc-sociology-and-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/sociology-social-policy/bsc-sociology-and-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/bsc-translation-studies-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/bsc-translation-studies-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/bsc-translation-studies-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/bsc-translation-studies-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/bsc-translation-studies-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/bsc-translation-studies-modern-languages/",
"http://www.aston.ac.uk/aston-medical-school/mbchb-medicine/", ]
        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "Aston University"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:


            alevel = response.xpath(
                "//div[contains(text(),'A level')]/..//text()|//div[contains(text(),'B – B')]/..//text()|"
                "//div[@class='course-details__dt'][contains(text(),'A Level')]/..//text()|"
                "//div[contains(text(),'A-levels')]/..//text()").extract()
            item['alevel'] = clear_lianxu_space(alevel)
            print("item['alevel']: ", item['alevel'])

            ib = response.xpath("//div[contains(text(),'International baacalaureate diploma')]/..//text()|"
                                "//div[contains(text(),'International Baccalaureate')]/..//text()|"
                                "//div[contains(text(),'International baccalaureate')]/..//text()").extract()
            if len(ib) == 0:
                ib = response.xpath("//strong[contains(text(),'International Baccalaureate')]/../following-sibling::*[1]//text()").extract()
            item['ib'] = clear_lianxu_space(ib)
            print("item['ib']: ", item['ib'])

            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)
