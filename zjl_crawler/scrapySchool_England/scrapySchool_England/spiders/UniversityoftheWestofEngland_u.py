# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/26 20:15'
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
from scrapySchool_England.translate_date import  tracslateDate
from scrapySchool_England.TranslateMonth import translate_month
from scrapySchool_England.getTuition_fee import getT_fee
class UniversityoftheWestofEnglandSpider(scrapy.Spider):
    name = 'UniversityoftheWestofEngland_u'
    allowed_domains = ['uwe.ac.uk/']
    start_urls = []
    C= [
        "https://courses.uwe.ac.uk/3W25/2019/uniformed-and-public-services",
        "https://courses.uwe.ac.uk/I100/2019/applied-computi",
        "https://courses.uwe.ac.uk/HK10/2019/building-services-engineering",
        "https://courses.uwe.ac.uk/HM3L/2019/electronic-and-computer-engineering",
        "https://courses.uwe.ac.uk/II62/2019/games-and-animation-production",
        "https://courses.uwe.ac.uk/Z040/2019/international-business-management",
        "https://courses.uwe.ac.uk/W384/2019/music",
        "https://courses.uwe.ac.uk/W241/2019/product-design",
        "https://courses.uwe.ac.uk/G102/2019/mathematics",
        "https://courses.uwe.ac.uk/B711/2019/midwifery",
        "https://courses.uwe.ac.uk/B702/2019/nursing-children's",
        "https://courses.uwe.ac.uk/B950/2019/paramedic-science",
        "https://courses.uwe.ac.uk/C980/2019/biomedical-science",
        "https://courses.uwe.ac.uk/C98M/2019/biomedical-scien",
        "https://courses.uwe.ac.uk/C990/2019/healthcare-science-life-science",
        "https://courses.uwe.ac.uk/F41M/2019/forensic-science",
        "https://courses.uwe.ac.uk/F410/2019/forensic-science",
        "https://courses.uwe.ac.uk/B160/2019/physiotherapy",
        "https://courses.uwe.ac.uk/H404/2019/aerospace-engineeri",
        "https://courses.uwe.ac.uk/H335/2019/automotive-engineeri",
        "https://courses.uwe.ac.uk/H61C/2019/electronic-engineering",
        "https://courses.uwe.ac.uk/H301/2019/mechanical-engineering",
        "https://courses.uwe.ac.uk/H406/2019/aerospace-engineering-with-pilot-studi",
        "https://courses.uwe.ac.uk/G1X9/2019/mathematics-with-qualified-teacher-status",
        "https://courses.uwe.ac.uk/G300/2019/mathematics-and-statistics",
        "https://courses.uwe.ac.uk/G101/2019/mathematics",
        "https://courses.uwe.ac.uk/B701/2019/nursing-adult-nursing",
        "https://courses.uwe.ac.uk/B703/2019/nursing-learning-disabilities",
        "https://courses.uwe.ac.uk/B704/2019/nursing-mental-health",
        "https://courses.uwe.ac.uk/45MN/2019/wildlife-ecology-and-conservation-science",
        "https://courses.uwe.ac.uk/45MM/2019/wildlife-ecology-and-conservation-science",
        "https://courses.uwe.ac.uk/C11M/2019/biological-scienc",
        "https://courses.uwe.ac.uk/C110/2019/biological-scienc",
        "https://courses.uwe.ac.uk/B919/2019/environmental-health-and-practice",
        "https://courses.uwe.ac.uk/F900/2019/environmental-science",
        "https://courses.uwe.ac.uk/F90M/2019/environmental-science",
        "https://courses.uwe.ac.uk/B821/2019/diagnostic-imaging",
        "https://courses.uwe.ac.uk/B822/2019/radiotherapy-and-oncology",
        "https://courses.uwe.ac.uk/BC96/2019/sport-rehabilitation",
        "https://courses.uwe.ac.uk/G611/2019/games-technology",
        "https://courses.uwe.ac.uk/H405/2019/aerospace-engineering-with-pilot-studi",
        "https://courses.uwe.ac.uk/H671/2019/robotics",
        "https://courses.uwe.ac.uk/H403/2019/aerospace-engineeri",
        "https://courses.uwe.ac.uk/H331/2019/automotive-engineeri",
        "https://courses.uwe.ac.uk/H61D/2019/electronic-engineering",
        "https://courses.uwe.ac.uk/H300/2019/mechanical-engineering",
        "https://courses.uwe.ac.uk/KH12/2019/architecture-and-environmental-engineeri",
        "https://courses.uwe.ac.uk/H290/2019/civil-and-environmental-engineering",
        "https://courses.uwe.ac.uk/L19F/2019/economics-with-foundation-year",
        "https://courses.uwe.ac.uk/L190/2019/economics",
        "https://courses.uwe.ac.uk/J932/2019/audio-and-music-technolo",
        "https://courses.uwe.ac.uk/WJ39/2019/creative-music-technology",
        "https://courses.uwe.ac.uk/H6J9/2019/broadcast-audio-and-music-technology",
        "https://courses.uwe.ac.uk/N51F/2019/marketing-communication-management-with-foundation-year",
        "https://courses.uwe.ac.uk/N591/2019/marketing-communication-management",
        "https://courses.uwe.ac.uk/C800/2019/psychology",
        "https://courses.uwe.ac.uk/C8M9/2019/psychology-with-criminology",
        "https://courses.uwe.ac.uk/C8L3/2019/psychology-with-sociology",
        "https://courses.uwe.ac.uk/L30F/2019/sociology-with-foundation-year",
        "https://courses.uwe.ac.uk/L38F/2019/sociology-with-psychology-with-foundation-year",
        "https://courses.uwe.ac.uk/P50F/2019/broadcast-journalism-with-foundation-year",
        "https://courses.uwe.ac.uk/W81F/2019/creative-and-professional-writing-with-foundation-year",
        "https://courses.uwe.ac.uk/M90F/2019/criminology-with-foundation-year",
        "https://courses.uwe.ac.uk/ML3F/2019/criminology-and-sociology-with-foundation-year",
        "https://courses.uwe.ac.uk/W11F/2019/drawing-and-print-with-foundation-year",
        "https://courses.uwe.ac.uk/X31F/2019/early-childhood-with-foundation-year",
        "https://courses.uwe.ac.uk/QV3F/2019/english-and-history-with-foundation-year",
        "https://courses.uwe.ac.uk/Q30F/2019/english-literature-with-foundation-year",
        "https://courses.uwe.ac.uk/QQ3F/2019/english-language-and-linguistics-with-foundation-year",
        "https://courses.uwe.ac.uk/Q39F/2019/english-language-and-literature-with-foundation-year",
        "https://courses.uwe.ac.uk/Q3WF/2019/english-literature-with-writing-with-foundation-year",
        "https://courses.uwe.ac.uk/W2PF/2019/fashion-communication-with-foundation-year",
        "https://courses.uwe.ac.uk/W23F/2019/fashion-textiles-with-foundation-year",
        "https://courses.uwe.ac.uk/P3AF/2019/film-studies-with-foundation-year",
        "https://courses.uwe.ac.uk/W10F/2019/fine-art-with-foundation-year",
        "https://courses.uwe.ac.uk/W22F/2019/graphic-design-with-foundation-year",
        "https://courses.uwe.ac.uk/W20F/2019/illustration-with-foundation-year",
        "https://courses.uwe.ac.uk/V10F/2019/history-with-foundation-year",
        "https://courses.uwe.ac.uk/2C3F/2019/interior-design-with-foundation-year",
        "https://courses.uwe.ac.uk/PP5F/2019/journalism-and-public-relations-with-foundation-year",
        "https://courses.uwe.ac.uk/PL3F/2019/media-and-cultural-production-with-foundation-year",
        "https://courses.uwe.ac.uk/P31F/2019/media-culture-and-communication-with-foundation-year",
        "https://courses.uwe.ac.uk/P25F/2019/media-and-journalism-with-foundation-year",
        "https://courses.uwe.ac.uk/L29F/2019/politics-and-international-relations-with-foundation-year",
        "https://courses.uwe.ac.uk/L3C8/2019/sociology-with-psychology",
        "https://courses.uwe.ac.uk/L300/2019/sociology",
        "https://courses.uwe.ac.uk/W615/2019/animati",
        "https://courses.uwe.ac.uk/P500/2019/broadcast-journalism",
        "https://courses.uwe.ac.uk/N201/2019/business-management-and-leadership",
        "https://courses.uwe.ac.uk/N1N4/2019/business-management-with-accounting-and-finance",
        "https://courses.uwe.ac.uk/W810/2019/creative-and-professional-writing",
        "https://courses.uwe.ac.uk/M900/2019/criminology",
        "https://courses.uwe.ac.uk/ML93/2019/criminology-and-sociology",
        "https://courses.uwe.ac.uk/W490/2019/drama-and-acting",
        "https://courses.uwe.ac.uk/W400/2019/drama",
        "https://courses.uwe.ac.uk/W110/2019/drawing-and-print",
        "https://courses.uwe.ac.uk/X312/2019/early-childhood",
        "https://courses.uwe.ac.uk/QQ3C/2019/english-language-and-linguistics",
        "https://courses.uwe.ac.uk/QV31/2019/english-and-history",
        "https://courses.uwe.ac.uk/Q300/2019/english-literature",
        "https://courses.uwe.ac.uk/Q390/2019/english-language-and-literature",
        "https://courses.uwe.ac.uk/W2P2/2019/fashion-communication",
        "https://courses.uwe.ac.uk/W23A/2019/fashion-textiles",
        "https://courses.uwe.ac.uk/0PC3/2019/english-literature-with-writing",
        "https://courses.uwe.ac.uk/P30A/2019/film-studies",
        "https://courses.uwe.ac.uk/W101/2019/fine-art",
        "https://courses.uwe.ac.uk/W211/2019/graphic-design",
        "https://courses.uwe.ac.uk/V100/2019/history",
        "https://courses.uwe.ac.uk/W224/2019/illustration",
        "https://courses.uwe.ac.uk/2C3W/2019/interior-design",
        "https://courses.uwe.ac.uk/PP52/2019/journalism-and-public-relations",
        "https://courses.uwe.ac.uk/P251/2019/media-and-journalism",
        "https://courses.uwe.ac.uk/P30C/2019/media-culture-and-communication",
        "https://courses.uwe.ac.uk/PL36/2019/media-and-cultural-production",
        "https://courses.uwe.ac.uk/B920/2019/occupational-therapy",
        "https://courses.uwe.ac.uk/L290/2019/politics-and-international-relations",
        "https://courses.uwe.ac.uk/W640/2019/photography",
        "https://courses.uwe.ac.uk/X123/2019/primary-education-ite",
        "https://courses.uwe.ac.uk/V500/2019/philosophy",
        "https://courses.uwe.ac.uk/H67F/2019/robotics-with-foundation-year",
        "https://courses.uwe.ac.uk/K41F/2019/urban-planning-with-foundation-year",
        "https://courses.uwe.ac.uk/H45F/2019/aerospace-engineering-with-pilot-studies-with-foundation-ye",
        "https://courses.uwe.ac.uk/H43F/2019/aerospace-engineering-with-foundation-ye",
        "https://courses.uwe.ac.uk/KH1F/2019/architecture-and-environmental-engineering-with-foundation-ye",
        "https://courses.uwe.ac.uk/KK1F/2019/architecture-and-planning-with-foundation-ye",
        "https://courses.uwe.ac.uk/H31F/2019/automotive-engineering-with-foundation-ye",
        "https://courses.uwe.ac.uk/N1IF/2019/business-computing-with-foundation-year",
        "https://courses.uwe.ac.uk/M21F/2019/commercial-law-with-foundation-year",
        "https://courses.uwe.ac.uk/L74F/2019/geography-and-planning-with-foundation-year",
        "https://courses.uwe.ac.uk/L70F/2019/geography-with-foundation-year",
        "https://courses.uwe.ac.uk/N89F/2019/geography-and-tourism-with-foundation-year",
        "https://courses.uwe.ac.uk/K12F/2019/interior-architecture-with-foundation-year",
        "https://courses.uwe.ac.uk/M10F/2019/law-with-foundation-year",
        "https://courses.uwe.ac.uk/H3FF/2019/mechanical-engineering-with-foundation-year",
        "https://courses.uwe.ac.uk/W41F/2019/product-design-with-foundation-year",
        "https://courses.uwe.ac.uk/KN21/2019/quantity-surveying-and-commercial-management",
        "https://courses.uwe.ac.uk/K401/2019/urban-planning",
        "https://courses.uwe.ac.uk/K252/2019/construction-project-management",
        "https://courses.uwe.ac.uk/L700/2019/geography",
        "https://courses.uwe.ac.uk/L7K4/2019/geography-and-planning",
        "https://courses.uwe.ac.uk/K120/2019/interior-architecture",
        "https://courses.uwe.ac.uk/H29F/2019/civil-and-environmental-engineering-with-foundation-year",
        "https://courses.uwe.ac.uk/G45F/2019/digital-media-with-foundation-year",
        "https://courses.uwe.ac.uk/H6DF/2019/electronic-engineering-with-foundation-year",
        "https://courses.uwe.ac.uk/FF8F/2019/geography-with-foundation-year",
        "https://courses.uwe.ac.uk/G30F/2019/mathematics-and-statistics-with-foundation-year",
        "https://courses.uwe.ac.uk/G1XF/2019/mathematics-with-qualified-teacher-status-with-foundation-year",
        "https://courses.uwe.ac.uk/G451/2019/digital-media",
        "https://courses.uwe.ac.uk/FF89/2019/geography",
        "https://courses.uwe.ac.uk/GN52/2019/information-technology-management-for-business-itmb",
        "https://courses.uwe.ac.uk/K10F/2019/architecture-with-foundation-ye",
        "https://courses.uwe.ac.uk/K44F/2019/real-estate-with-foundation-year",
        "https://courses.uwe.ac.uk/6F3F/2019/software-engineering-for-business-with-foundation-year",
        "https://courses.uwe.ac.uk/N42F/2019/accounting-and-finance-with-foundation-ye",
        "https://courses.uwe.ac.uk/K26F/2019/architectural-technology-and-design-with-foundation-ye",
        "https://courses.uwe.ac.uk/J93F/2019/audio-and-music-technology-with-foundation-ye",
        "https://courses.uwe.ac.uk/N30F/2019/banking-and-finance-with-foundation-ye",
        "https://courses.uwe.ac.uk/H6JF/2019/broadcast-audio-and-music-technology-with-foundation-year",
        "https://courses.uwe.ac.uk/K230/2019/building-surveying",
        "https://courses.uwe.ac.uk/N19F/2019/business-team-entrepreneurship-with-foundation-year",
        "https://courses.uwe.ac.uk/K23F/2019/building-surveying-with-foundation-year",
        "https://courses.uwe.ac.uk/NN2F/2019/business-and-events-management-with-foundation-year",
        "https://courses.uwe.ac.uk/NNQF/2019/business-and-human-resource-management-with-foundation-year",
        "https://courses.uwe.ac.uk/N10F/2019/business-and-management-with-foundation-year",
        "https://courses.uwe.ac.uk/NL1F/2019/business-management-and-economics-with-foundation-year",
        "https://courses.uwe.ac.uk/N21F/2019/business-management-and-leadership-with-foundation-year",
        "https://courses.uwe.ac.uk/NN4F/2019/business-management-with-accounting-and-finance-with-foundation-year",
        "https://courses.uwe.ac.uk/NMAF/2019/business-management-with-law-with-foundation-year",
        "https://courses.uwe.ac.uk/NN5F/2019/business-management-with-marketing-with-foundation-year",
        "https://courses.uwe.ac.uk/NM1F/2019/business-and-law-with-foundation-year",
        "https://courses.uwe.ac.uk/G40F/2019/computer-science-with-foundation-year",
        "https://courses.uwe.ac.uk/I10F/2019/computing-with-foundation-year",
        "https://courses.uwe.ac.uk/MM9F/2019/criminology-and-law-with-foundation-year",
        "https://courses.uwe.ac.uk/M98F/2019/criminology-with-psychology-with-foundation-year",
        "https://courses.uwe.ac.uk/L10F/2019/economics-with-foundation-year",
        "https://courses.uwe.ac.uk/M12F/2019/european-and-international-law-with-foundation-year",
        "https://courses.uwe.ac.uk/G4HF/2019/forensic-computing-and-security-with-foundation-year",
        "https://courses.uwe.ac.uk/G61F/2019/games-technology-with-foundation-year",
        "https://courses.uwe.ac.uk/N11F/2019/international-business-with-foundation-year",
        "https://courses.uwe.ac.uk/NMBF/2019/law-with-business-with-foundation-year",
        "https://courses.uwe.ac.uk/G10F/2019/mathematics-with-foundation-year",
        "https://courses.uwe.ac.uk/W24F/2019/product-design-technology-with-foundation-year",
        "https://courses.uwe.ac.uk/K43F/2019/property-development-and-planning-with-foundation-year",
        "https://courses.uwe.ac.uk/KN2F/2019/quantity-surveying-and-commercial-management-with-foundation-year",
        "https://courses.uwe.ac.uk/N1N6/2019/business-and-human-resource-management",
        "https://courses.uwe.ac.uk/NM1A/2019/business-management-with-law",
        "https://courses.uwe.ac.uk/MM19/2019/criminology-and-law",
        "https://courses.uwe.ac.uk/W293/2019/filmmaking",
        "https://courses.uwe.ac.uk/K100/2019/architectu",
        "https://courses.uwe.ac.uk/K440/2019/real-estate",
        "https://courses.uwe.ac.uk/6F3B/2019/software-engineering-for-business",
        "https://courses.uwe.ac.uk/N420/2019/accounting-and-finan",
        "https://courses.uwe.ac.uk/K236/2019/architectural-technology-and-desi",
        "https://courses.uwe.ac.uk/KK14/2019/architecture-and-planni",
        "https://courses.uwe.ac.uk/N300/2019/banking-and-finan",
        "https://courses.uwe.ac.uk/N191/2019/business-team-entrepreneurship",
        "https://courses.uwe.ac.uk/NN21/2019/business-and-events-management",
        "https://courses.uwe.ac.uk/NM11/2019/business-and-law",
        "https://courses.uwe.ac.uk/NL14/2019/business-management-and-economics",
        "https://courses.uwe.ac.uk/N100/2019/business-and-management",
        "https://courses.uwe.ac.uk/N1N5/2019/business-management-with-marketing",
        "https://courses.uwe.ac.uk/M221/2019/commercial-law",
        "https://courses.uwe.ac.uk/G400/2019/computer-science",
        "https://courses.uwe.ac.uk/G401/2019/computing",
        "https://courses.uwe.ac.uk/M9C8/2019/criminology-with-psychology",
        "https://courses.uwe.ac.uk/L100/2019/economics",
        "https://courses.uwe.ac.uk/M121/2019/european-and-international-law",
        "https://courses.uwe.ac.uk/G4H4/2019/forensic-computing-and-security",
        "https://courses.uwe.ac.uk/N890/2019/geography-and-tourism",
        "https://courses.uwe.ac.uk/N110/2019/international-business",
        "https://courses.uwe.ac.uk/M100/2019/law",
        "https://courses.uwe.ac.uk/NM1B/2019/law-with-business",
        "https://courses.uwe.ac.uk/K430/2019/property-development-and-planning",
        "https://courses.uwe.ac.uk/N50F/2019/marketing-with-foundation-year",
        "https://courses.uwe.ac.uk/N500/2019/marketing",
        "https://courses.uwe.ac.uk/N1I1/2019/business-computing",
        "https://courses.uwe.ac.uk/W240/2019/product-design-technology",
        "https://courses.uwe.ac.uk/V50F/2019/philosophy-with-foundation-year",
        "https://courses.uwe.ac.uk/C1MF/2019/biological-sciences-with-foundation-ye",
        "https://courses.uwe.ac.uk/45FF/2019/wildlife-ecology-and-conservation-science-with-foundation-year",
        "https://courses.uwe.ac.uk/45MF/2019/wildlife-ecology-and-conservation-science-with-foundation-yea",
        "https://courses.uwe.ac.uk/C11F/2019/biological-sciences-with-foundation-ye",
        "https://courses.uwe.ac.uk/C9MF/2019/biomedical-science-with-foundation-year",
        "https://courses.uwe.ac.uk/C98F/2019/biomedical-science-with-foundation-year",
        "https://courses.uwe.ac.uk/F90F/2019/environmental-science-with-foundation-year",
        "https://courses.uwe.ac.uk/F41F/2019/forensic-science-with-foundation-year",
        "https://courses.uwe.ac.uk/F4MF/2019/forensic-science-with-foundation-year",
        "https://courses.uwe.ac.uk/C91F/2019/healthcare-science-physiological-sciences-with-foundation-year",
        "https://courses.uwe.ac.uk/C90F/2019/healthcare-science-life-science-with-foundation-year",
        "https://courses.uwe.ac.uk/C80F/2019/psychology-with-foundation-year",
        "https://courses.uwe.ac.uk/C8LF/2019/psychology-with-sociology-with-foundation-year",
        "https://courses.uwe.ac.uk/C89F/2019/psychology-with-criminology-with-foundation-year",
        "https://courses.uwe.ac.uk/F9MF/2019/environmental-science-with-foundation-year",
        "https://courses.uwe.ac.uk/L500/2019/social-work",
        "https://courses.uwe.ac.uk/B510/2019/optometry",
        "https://courses.uwe.ac.uk/F600/2019/geology",
        "https://courses.uwe.ac.uk/N1C6/2019/sports-business-and-entrepreneurship"
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of the West of England'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="content"]/div//h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_name
        degree_name = response.xpath("//div[@class='m-course__header__details']//p").extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        if '/' in degree_name:
            degree_name =  degree_name.split('/')[0]
        else:
            pass
        # print(degree_name)

        #5.degree_type
        degree_type = 1

        #6.department
        department = response.xpath("//*[contains(text(),'Department:')]//following-sibling::dd[1]").extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #7.location
        location = response.xpath("//*[contains(text(),'Campus:')]//following-sibling::dd[1]").extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #8.duration #9.duration_per
        duration = response.xpath("//*[contains(text(),'Duration:')]//following-sibling::dd[1]").extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        str = ''
        d_dict = {"One": "1",
                  "Two": "2",
                  "Three": "3",
                  "Four": "4",
                  "Five": "5",
                  "Six": "6",
                  "Seven": "7",
                  "Eight": "8",
                  "Nine": "9",
                  "Ten": "10",
                  "one": "1",
                  "two": "2",
                  "three": "3",
                  "four": "4",
                  "five": "5",
                  "six": "6",
                  "seven": "7",
                  "eight": "8",
                  "nine": "9",
                  "ten": "10",
                  }
        a = duration.split()
        # print(a)
        for i in a:
            str1 = d_dict.get(i)
            if str1 is not None:
                str +=str1+','
        # print(str)
        duration = str
        duration_per =1
        # print(duration,"****",duration_per)

        #10.ucascode
        ucascode = response.xpath("//*[contains(text(),'Course code:')]//following-sibling::dd[1]").extract()
        ucascode = ''.join(ucascode)
        ucascode =remove_tags(ucascode)
        # print(ucascode)

        #11.overview_en
        overview_en = response.xpath("//h2/a[contains(text(),'Introduction')]/../following-sibling::*").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en).strip()
        # print(overview_en)

        #12.modules_en
        modules_en = response.xpath("//*[contains(text(),'Content')]//following-sibling::*").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en).strip()
        end = modules_en.find('<h3>Learning and Teaching</h3>')
        modules_en = modules_en[:end]
        # print(modules_en)

        #13.assessment_en
        assessment_en = response.xpath("//h3[contains(text(),'Assessment')]//following-sibling::*").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #14.career_en
        career_en = response.xpath("//h3[contains(text(),'Careers')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #15.alevel
        try:
            alevel = response.xpath("//*[contains(text(),'A-level subjects:')]//..").extract()[0]
            alevel = remove_tags(alevel).strip()
        except:
            alevel = 'N/A'
        # print(alevel)

        #16.tuition_fee
        tuition_fee= None

        #17.tuition_fee_pre
        tuition_fee_pre = '£'

        #18.ielts 19202122
        try:
            ielts= response.xpath("//*[contains(text(),'English Language Requirement:')]//..").extract()[0]
            ielts = remove_tags(ielts).strip()
            ielts=re.findall(r'[567]\.\d',ielts)
            if len(ielts)==2:
                a = ielts[0]
                b = ielts[1]
                ielts=a
                ielts_r=b
                ielts_s =b
                ielts_w = b
                ielts_l =  b
            elif len(ielts)==1:
                a = ielts[0]
                ielts = a
                ielts_r = a
                ielts_s = a
                ielts_w = a
                ielts_l = a
            else:
                ielts = 6.0
                ielts_r = 5.5
                ielts_s = 5.5
                ielts_w = 5.5
                ielts_l = 5.5
        except:
            ielts = 6.0
            ielts_r = 5.5
            ielts_s = 5.5
            ielts_w = 5.5
            ielts_l = 5.5
        # print(ielts,ielts_r,ielts_w,ielts_l,ielts_s)


        #28.apply_pre
        apply_pre = '£'


        #29.ib
        try:
            ib = response.xpath("//*[contains(text(),'Baccalaureate IB')]//..").extract()[0]
            ib = ''.join(ib)
            ib = remove_tags(ib)
        except:
            ib = ''
        # print(ib)



        item['ib'] = ib
        item['ucascode'] = ucascode
        item['alevel'] = alevel
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_name'] = degree_name
        item['degree_type'] = degree_type
        item['department'] = department
        item['location'] = location
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['ielts'] = ielts
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['ielts_r'] = ielts_r
        yield item