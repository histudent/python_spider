# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime


class CanterburyChristChurchUniversity_Alevel_IbSpider(scrapy.Spider):
    name = "CanterburyChristChurchUniversity_Alevel_Ib"
    start_urls = ["https://www.bolton.ac.uk/subject-areas/all-subjects/"]

    def parse(self, response):
        links = ["https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-bsc-hons-at-bromley-college-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-finance-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-finance-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/accelerated-degree-accounting-bsc-hons-at-bromley-college-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-and-management-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/advertising-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/applied-practice-health-and-social-care-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/advertising-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/animal-science-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/american-studies-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/american-studies-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/animal-science-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/applied-criminology-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/archaeology-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/archaeology-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/biomolecular-science-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-accelerated-degree-bsc-hons-at-london-south-east-colleges-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/biomolecular-science-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/biochemistry-and-biological-chemistry-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-information-systems-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-management-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/biochemistry-and-biological-chemistry-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-bsc-hons-at-london-south-east-colleges-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-management-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/biology-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/chemistry-for-drug-discovery-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/biology-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/computer-forensics-and-security-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/computer-forensics-and-security-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/computing-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/computing-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/computing-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/counselling-coaching-and-mentoring-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/computer-forensics-and-security-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/chemistry-for-drug-discovery-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/creative-and-professional-writing-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/dance-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/counselling-coaching-and-mentoring-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/creative-and-professional-writing-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/digital-media-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/digital-marketing-communications-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/digital-media-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/early-childhood-education-and-care-bromley-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/dance-education-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/drama-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/early-childhood-studies-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/ecology-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/ecology-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/education-studies-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/education-studies-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/early-childhood-studies-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/english-literature-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/english-literature-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-studies-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/english-language-and-communication-2018-19.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/environmental-science-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/english-language-and-communication-with-foundation-year-2018-19.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/events-management-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/film-production-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/film-production-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/film-radio-and-television-studies-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/environmental-science-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/finance-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/computer-science-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/forensic-investigation-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/chemical-engineering-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/forensic-investigation-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-studies-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/games-design-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/ba-geography-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/french-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/graphic-design-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/finance-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/film-radio-and-television-studies-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/health-studies-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/health-studies-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/history-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/hospitality-management-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-biology-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-biology-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-development-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/graphic-design-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/geography-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/environmental-science-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-resource-management-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/information-technology-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-resource-management-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/international-relations-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/international-relations-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/multimedia-journalism-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/journalism-multimedia-journalism-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-resource-management-bsc-at-bromley-college-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-development-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/law-llb-with-another-subject-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/games-design-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/management-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/history-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/forensic-investigation-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/marketing-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/logistics-management-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/media-and-communications-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/media-and-communications-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/medieval-and-early-modern-studies-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-production-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/medieval-and-early-modern-studies-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/law-llb-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-production-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-bmus-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-ba-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-commercial-music-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/law-llb-with-business-at-london-south-east-colleges-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-creative-music-technology-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/mathematics-with-secondary-education-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/occupational-therapy-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/marketing-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/management-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/management-sustainable-ethical-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/performing-arts-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/performing-arts-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/operating-department-practice-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-commercial-music-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/physical-education-and-sport-exercise-science-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/physical-education-and-sport-exercise-science-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/policing-criminal-investigation-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/plant-science-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/policing-critical-incidents-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/photography-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/plant-science-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/policing-terrorism-and-political-violence-2018-19.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/policing-youth-justice-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/policing-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/policing-global-perspectives-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/politics-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/policing-criminal-psychology-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/politics-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/psychology-sport-and-exercise-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/psychology-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/psychology-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/primary-education-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/public-relations-media-and-marketing-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/religion-philosophy-and-ethics-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/photography-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/social-work-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/nursing-studies-adult-nursing-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/sociology-and-social-policy-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/sociology-and-social-policy-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/sociology-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/religion-philosophy-and-ethics-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/special-educational-needs-and-inclusion-studies-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-and-exercise-psychology-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/special-educational-needs-and-inclusion-studies-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/sociology-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-and-exercise-psychology-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/policing-cybersecurity-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/politics-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/speech-and-language-therapy-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-creative-music-technology-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-and-exercise-psychology-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-coaching-science-with-foundation-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-and-exercise-science-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/tourism-studies-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/tourism-management-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-and-exercise-science-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/theology-with-foundation-year-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-coaching-science-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/theology-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/web-technology-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-coaching-science-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/tourism-studies-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/tourism-studies-19-20.aspx",
"https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-and-management-with-foundation-year-19-20.aspx", ]
        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})


    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "Canterbury Christ Church University"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:
            # ucas_point = response.xpath("//li[@class='iconim points']//b[contains(text(),'UCAS points:')]/../span//text()").extract()
            # print("ucas_point: ", ucas_point)

            alevel = response.xpath(
                "//h3[contains(text(),'Entry requirements')]/following-sibling::*//*[contains(text(), 'A level')]//text()|"
                "//h3[contains(text(),'Entry requirements')]/following-sibling::*//*[contains(text(), ' UCAS Tariff points')]//text()|"
                "//h3[contains(text(),'Entry requirements')]/following-sibling::*//*[contains(text(), 'UCAS points')]//text()|"
                "//h3[contains(text(),'Entry requirements')]/following-sibling::*//*[contains(text(), 'A typical offer')]//text()").extract()
            # del_re = re.findall(r"More entry requirement details.*", ''.join(alevel))
            # print("del_re: ", del_re)
            item['alevel'] = clear_lianxu_space(alevel).replace("More entry requirement details", "").replace(".", "").strip()
            print("item['alevel']: ", item['alevel'])

            # ib = response.xpath(
            #     "//h5[contains(text(),'EU/International students')]/following-sibling::table//td[contains(text(),'International Baccalaureate')]/following-sibling::td//text()|"
            #     "//p[contains(text(),'International Baccalaureate')]//text()|"
            #     "//strong[contains(text(),'International Baccalaureate:')]/../span//text()").extract()
            # if len(ib) == 0:
            #     ib = response.xpath(
            #         "//td[contains(text(),'International Baccalaureate')]/following-sibling::td//text()").extract()
            # item['ib'] = clear_lianxu_space(ib)
            # print("item['ib']: ", item['ib'])

            yield item

        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

