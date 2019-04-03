import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl

class KingsCollegeLondon_USpider(scrapy.Spider):
    name = "KingsCollegeLondon_U"
    start_urls = ["https://www.kcl.ac.uk/study/subject-areas/index.aspx"]

    def parse(self, response):
        links = ["https://www.kcl.ac.uk/study/undergraduate/courses/anatomy-developmental-and-human-biology-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/ancient-history-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/biochemistry-msci.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/biochemistry-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/biomedical-engineering-meng.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/biomedical-engineering-beng.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/biomedical-science-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/business-management-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/chemistry-msci.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/chemistry-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/chemistry-with-year-in-placement-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/chemistry-with-year-in-placement-msci.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/chemistry-with-biomedicine-msci.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/chemistry-with-biomedicine-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/chemistry-with-biomedicine-with-year-in-placement-msci.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/chemistry-with-biomedicine-with-year-in-placement.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/classical-and-modern-greek-studies-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/classical-archaeology-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/classical-studies-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/classical-studies-and-comparative-literature-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/classical-studies-and-french-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/classical-studies-with-english-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/classics-greek-and-latin-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/comparative-literature-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/comparative-literature-with-film-studies-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/computer-science-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/computer-science-msci.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/computer-science-with-a-year-abroad-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/computer-science-with-a-year-in-industry-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/computer-science-with-intelligent-systems-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/computer-science-with-management-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/computer-science-with-management-and-a-year-abroad-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/computer-science-with-management-and-a-year-in-industry-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/computer-science-with-robotics-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/dentistry-bds.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/digital-culture-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/economics-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/economics-and-management-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/electronic-and-information-engineering-beng.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/electronic-and-information-engineering-meng.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/electronic-engineering-meng.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/electronic-engineering-beng.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/electronic-engineering-with-management-beng.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/electronic-engineering-with-management-meng.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/english-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/english-language-and-linguistics-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/english-law-and-american-law-llb-and-jd.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/english-law-and-french-law-llb.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/english-law-and-german-law-llb.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/english-law-and-hong-kong-law-llb-jd.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/english-law-with-australian-law-llb.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/english-law-hong-kong-law-llb-llm.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/english-with-film-studies-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/enhanced-support-dentistry-programme-bds.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/european-politics-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/european-studies-french-pathway-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/european-studies-german-pathway-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/european-studies-spanish-pathway-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/extended-medical-degree-programme-mbbs.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/film-studies-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/french-and-german-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/french-and-history-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/french-and-management-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/french-and-philosophy-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/french-four-year-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/french-three-year-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/french-and-spanish-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/french-with-english-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/french-with-film-studies-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/geography-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/geography-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/german-and-history-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/german-and-management-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/german-and-music-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/german-and-philosophy-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/german-and-portuguese-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/german-and-spanish-with-a-year-abroad--ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/german-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/german-with-english-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/german-with-film-studies-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/global-health-and-social-medicine-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/global-health-and-social-medicine-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/history-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/history-and-international-relations.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/international-development-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/international-management-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/international-relations-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/law-llb.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/law-with-american-legal-studies-llb.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/law-with-european-legal-studies-llb.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/law-with-transnational-legal-studies-llb.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/liberal-arts-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/mathematics-msci.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/mathematics-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/mathematics-and-philosophy-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/mathematics-with-management-and-finance-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/mathematics-with-statistics.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/medical-physiology-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/medicine-mbbs.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/medicine-maxfax-entry-programme-mbbs.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/midwifery-with-registration-as-a-midwife-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/molecular-genetics-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/molecular-genetics-msci.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/music-bmus.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/neuroscience-msci.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/neuroscience-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/nursing-with-registration-as-a-childrens-nurse-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/nursing-with-registration-as-a-mental-health-nurse-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/nursing-with-registration-as-an-adult-nurse-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/nutrition-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/nutrition-and-dietetics-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/pharmacology-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/pharmacology-and-molecular-genetics-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/pharmacy-mpharm.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/philosophy-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/philosophy-and-spanish-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/philosophy-politics-and-economics-ba-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/physics-msci.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/physics-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/physics-and-philosophy-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/physics-and-philosophy-msci.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/physics-and-philosophy-with-a-year-abroad-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/physics-with-a-year-abroad-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/physics-with-astrophysics-and-cosmology-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/physics-with-astrophysics-and-cosmology-msci.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/physics-with-theoretical-physics-msci.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/physics-with-theoretical-physics-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/physiotherapy-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/political-economy-ba-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/politics-ba-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/politics-philosophy-and-law-llb.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/portuguese-and-french-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/portuguese-and-management-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/psychology-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/religion-philosophy-and-ethics-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/religion-politics-and-society-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/social-sciences-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/spanish-and-latin-american-studies-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/spanish-and-management-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/spanish-and-portuguese-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/spanish-with-english-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/spanish-with-film-studies-with-a-year-abroad-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/sport-and-exercise-medical-sciences-bsc.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/theology-religion-and-culture-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/war-studies-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/war-studies-and-history-ba.aspx",
"https://www.kcl.ac.uk/study/undergraduate/courses/war-studies-and-philosophy-ba.aspx", ]
        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "King's College London"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:

            alevel = response.xpath(
                # "//table//*[contains(text(),'A-level')]/../..//text()|//table//*[contains(text(),'A-Level')]/../..//text()"
                "//div[@class='further-information']//table//tbody/tr[1]//text()").extract()
            # if len(alevel) == 0:
            #     alevel = response.xpath(
            #         "//strong[contains(text(),'A-Level')]/../following-sibling::td[1]//text()").extract()
            #     if len(alevel) == 0:
            #         alevel = response.xpath(
            #             "//div[@class='requirements EntryReqs_UKALevel clearfix']//div[@class='required-grades']//text()//text()").extract()
            # clear_space(alevel)
            if len(alevel) > 0:
                item['alevel'] = clear_lianxu_space(alevel)
                # print("item['alevel']1 = ", item['alevel'])


            print("item['alevel'] = ", item['alevel'])

            ib = response.xpath(
                # "//*[contains(text(),'International Baccalaureate')]/../..//text()"
                "//div[@class='further-information']//table//tbody/tr[8]//text()").extract()
            # if len(ib) == 0:
            #     ib = response.xpath(
            #         "//*[contains(text(),'International Baccalaureate')]/../../..//text()").extract()
            if len(ib) > 0:
                item['ib'] = clear_lianxu_space(ib)
            print("item['ib'] = ", item['ib'])

            if "All candidates" in item['alevel']:
                alevel = response.xpath(
                    "//div[@class='further-information']//table//tbody/tr[2]//text()").extract()
                item['alevel'] = clear_lianxu_space(alevel)

                ib = response.xpath(
                    "//b[contains(text(),'International Baccalaureate')]/../../..//text()").extract()
                item['ib'] = clear_lianxu_space(ib)

            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

