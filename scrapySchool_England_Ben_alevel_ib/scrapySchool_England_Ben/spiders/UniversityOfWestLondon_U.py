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


class UniversityOfWestLondon_USpider(scrapy.Spider):
    name = "UniversityOfWestLondon_U"
    start_urls = ["https://www.uwl.ac.uk/courses/all?field_presentation_refs_field_start_date=2&field_study_level_taxonomy%5B0%5D=11&field_c_subject=All&field_presentation_refs_field_healthcare_cpd=332&field_presentation_refs_field_location2=All&field_presentation_refs_field_study_mode=Full%20time&keys=&study_mode_3=All&items_per_page=10&items_per_page=500"]

    def parse(self, response):
        links = response.xpath("//div[@class='view-content']/div[@class='item-list'][1]/ul/li/div[@class='views-field views-field-field-location2']/div[@class='field-content']/a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))

#         links = ["https://www.uwl.ac.uk/course/building-surveying-2/34469",
# "https://www.uwl.ac.uk/course/building-surveying-foundation-year-0/34859",
# "https://www.uwl.ac.uk/course/psychology-substance-use-and-misuse-studies-1/35822",
# "https://www.uwl.ac.uk/course/musical-theatre-foundation-year-0/35891",
# "https://www.uwl.ac.uk/course/music-technology-audio-post-production-1/35858",
# "https://www.uwl.ac.uk/course/music-recording-and-production-1/35867",
# "https://www.uwl.ac.uk/course/music-mixing-and-mastering-1/35864",
# "https://www.uwl.ac.uk/course/electronic-music-production-1/35861",
# "https://www.uwl.ac.uk/course/commercial-photography-2/34955",
# "https://www.uwl.ac.uk/course/information-technology-management-business-foundation-year-itmb-0/34400",
# "https://www.uwl.ac.uk/course/information-technology-management-business-itmb-0/34399",
# "https://www.uwl.ac.uk/course/film-composition-1/35837",
# "https://www.uwl.ac.uk/course/nutrition-and-food-management-0/36096",
# "https://www.uwl.ac.uk/course/nutrition-and-food-management-foundation-year/36097",
# "https://www.uwl.ac.uk/course/midwifery-pre-registration-2/33710",
# "https://www.uwl.ac.uk/course/midwifery-pre-registration-3/33711",
# "https://www.uwl.ac.uk/course/midwifery-pre-registration-1/33709",
# "https://www.uwl.ac.uk/course/midwifery-pre-registration-4/33712",
# "https://www.uwl.ac.uk/course/midwifery-shortened-2/33358",
# "https://www.uwl.ac.uk/course/midwifery-shortened-1/33357",
# "https://www.uwl.ac.uk/course/nursing-childrens-nursing-1/33715",
# "https://www.uwl.ac.uk/course/nursing-childrens-nursing-2/33716",
# "https://www.uwl.ac.uk/course/nursing-adult-8/35982",
# "https://www.uwl.ac.uk/course/nursing-adult-4/35686",
# "https://www.uwl.ac.uk/course/nursing-adult-7/35981",
# "https://www.uwl.ac.uk/course/nursing-adult-1/35631",
# "https://www.uwl.ac.uk/course/nursing-mental-health-4/33719",
# "https://www.uwl.ac.uk/course/nursing-mental-health-3/33718",
# "https://www.uwl.ac.uk/course/nursing-learning-disabilities-2/33088",
# "https://www.uwl.ac.uk/course/operating-department-practice-pre-registration-0/33724",
# "https://www.uwl.ac.uk/course/psychology-5/35807",
# "https://www.uwl.ac.uk/course/psychology-foundation-year-0/35829",
# "https://www.uwl.ac.uk/course/psychology-applied-forensic-investigation-1/35811",
# "https://www.uwl.ac.uk/course/psychology-counselling-theory-1/35815",
# "https://www.uwl.ac.uk/course/psychology-criminology-1/35819",
# "https://www.uwl.ac.uk/course/culinary-arts-management-foundation-year-0/35206",
# "https://www.uwl.ac.uk/course/culinary-arts-management-placement-0/34760",
# "https://www.uwl.ac.uk/course/forensic-science-1/35799",
# "https://www.uwl.ac.uk/course/forensic-science-foundation-year-0/35832",
# "https://www.uwl.ac.uk/course/mathematics-and-statistics-foundation-year-0/35548",
# "https://www.uwl.ac.uk/course/computer-science-1/33767",
# "https://www.uwl.ac.uk/course/mathematics-and-statistics-1/35769",
# "https://www.uwl.ac.uk/course/civil-and-environmental-engineering-4/35267",
# "https://www.uwl.ac.uk/course/civil-engineering-6/36034",
# "https://www.uwl.ac.uk/course/aviation-management-commercial-pilot-licence-0/35972",
# "https://www.uwl.ac.uk/course/airline-and-airport-management-foundation-year-0/35738",
# "https://www.uwl.ac.uk/course/electrical-and-electronic-engineering-0/34855",
# "https://www.uwl.ac.uk/course/civil-and-environmental-engineering-foundation-year-0/34854",
# "https://www.uwl.ac.uk/course/applied-sound-engineering-0/34971",
# "https://www.uwl.ac.uk/course/computer-science-foundation-year-0/34384",
# "https://www.uwl.ac.uk/course/creative-computing-foundation-year-0/34398",
# "https://www.uwl.ac.uk/course/creative-computing-0/34397",
# "https://www.uwl.ac.uk/course/cyber-security-4/35705",
# "https://www.uwl.ac.uk/course/cyber-security-foundation-year-0/35285",
# "https://www.uwl.ac.uk/course/information-technology-1/35054",
# "https://www.uwl.ac.uk/course/information-technology-foundation-year-0/35057",
# "https://www.uwl.ac.uk/course/computer-science-industrial-placement-0/35067",
# "https://www.uwl.ac.uk/course/creative-computing-industrial-placement-0/35641",
# "https://www.uwl.ac.uk/course/computer-games-technology-0/35703",
# "https://www.uwl.ac.uk/course/computer-games-technology-foundation-year-0/35704",
# "https://www.uwl.ac.uk/course/games-design-and-animation-0/35614",
# "https://www.uwl.ac.uk/course/games-design-and-animation-foundation-year-0/35616",
# "https://www.uwl.ac.uk/course/visual-effects-2/34958",
# "https://www.uwl.ac.uk/course/applied-sound-engineering-foundation-year-0/34385",
# "https://www.uwl.ac.uk/course/architectural-design-and-technology-2/34387",
# "https://www.uwl.ac.uk/course/construction-project-management-foundation-year-0/34396",
# "https://www.uwl.ac.uk/course/construction-project-management-5/35280",
# "https://www.uwl.ac.uk/course/politics-and-international-relations-foundation-year-0/35828",
# "https://www.uwl.ac.uk/course/criminology-3/35936",
# "https://www.uwl.ac.uk/course/criminology-psychology-foundation-year-0/35836",
# "https://www.uwl.ac.uk/course/criminology-policing-and-forensics-foundation-year-0/35948",
# "https://www.uwl.ac.uk/course/criminology-law-foundation-year-0/35943",
# "https://www.uwl.ac.uk/course/health-promotion-and-public-health-foundation-year-0/35439",
# "https://www.uwl.ac.uk/course/social-work-0/35824",
# "https://www.uwl.ac.uk/course/health-promotion-and-public-health-1/33689",
# "https://www.uwl.ac.uk/course/community-development-0/35979",
# "https://www.uwl.ac.uk/course/criminology-policing-and-forensics-1/35946",
# "https://www.uwl.ac.uk/course/politics-and-international-relations-1/35826",
# "https://www.uwl.ac.uk/course/criminology-foundation-year-0/35940",
# "https://www.uwl.ac.uk/course/business-economics-foundation-year-0/35908",
# "https://www.uwl.ac.uk/course/business-economics-0/35906",
# "https://www.uwl.ac.uk/course/law-foundation-year-0/35950",
# "https://www.uwl.ac.uk/course/law-0/35949",
# "https://www.uwl.ac.uk/course/criminology-psychology-1/35944",
# "https://www.uwl.ac.uk/course/criminology-law-1/35941",
# "https://www.uwl.ac.uk/course/business-studies-0/35909",
# "https://www.uwl.ac.uk/course/business-studies-foundation-year-0/35914",
# "https://www.uwl.ac.uk/course/business-studies-internship-0/35923",
# "https://www.uwl.ac.uk/course/business-studies-entrepreneurship-foundation-year-0/35919",
# "https://www.uwl.ac.uk/course/business-studies-finance-foundation-year-0/35922",
# "https://www.uwl.ac.uk/course/business-studies-entrepreneurship-0/35917",
# "https://www.uwl.ac.uk/course/business-studies-finance-0/35920",
# "https://www.uwl.ac.uk/course/international-business-management-2/35930",
# "https://www.uwl.ac.uk/course/hospitality-management-5/32203",
# "https://www.uwl.ac.uk/course/international-hotel-management-3/32245",
# "https://www.uwl.ac.uk/course/policing-1/36178",
# "https://www.uwl.ac.uk/course/music-management-1/35844",
# "https://www.uwl.ac.uk/course/accounting-and-finance-0/35900",
# "https://www.uwl.ac.uk/course/social-media-marketing-0/35933",
# "https://www.uwl.ac.uk/course/social-media-marketing-foundation-year-0/35935",
# "https://www.uwl.ac.uk/course/human-resource-management-3/35925",
# "https://www.uwl.ac.uk/course/human-resource-management-foundation-year-0/35929",
# "https://www.uwl.ac.uk/course/international-hotel-management-foundation-year-0/35310",
# "https://www.uwl.ac.uk/course/leisure-management-1/35423",
# "https://www.uwl.ac.uk/course/travel-and-tourism-management-3/35741",
# "https://www.uwl.ac.uk/course/leisure-management-placement-1/35419",
# "https://www.uwl.ac.uk/course/strategic-transport-management-1/35431",
# "https://www.uwl.ac.uk/course/strategic-transport-management-placement-1/35427",
# "https://www.uwl.ac.uk/course/leisure-management-foundation-year-0/35572",
# "https://www.uwl.ac.uk/course/travel-and-tourism-management-placement-3/35743",
# "https://www.uwl.ac.uk/course/event-management-3/33873",
# "https://www.uwl.ac.uk/course/event-management-foundation-year-0/35275",
# "https://www.uwl.ac.uk/course/event-management-hospitality-placement-3/35279",
# "https://www.uwl.ac.uk/course/event-management-placement-5/35269",
# "https://www.uwl.ac.uk/course/event-management-tourism-placement-3/35289",
# "https://www.uwl.ac.uk/course/travel-and-tourism-management-foundation-year-0/35745",
# "https://www.uwl.ac.uk/course/strategic-transport-management-foundation-year-0/35626",
# "https://www.uwl.ac.uk/course/airline-and-airport-management-6/35736",
# "https://www.uwl.ac.uk/course/airline-and-airport-management-placement-5/35214",
# "https://www.uwl.ac.uk/course/hospitality-management-and-food-studies-placement-3/35099",
# "https://www.uwl.ac.uk/course/hospitality-management-placement-3/35293",
# "https://www.uwl.ac.uk/course/international-hotel-management-placement-3/35111",
# "https://www.uwl.ac.uk/course/event-management-hospitality-foundation-year-0/35284",
# "https://www.uwl.ac.uk/course/event-management-tourism-foundation-year-0/35292",
# "https://www.uwl.ac.uk/course/event-management-hospitality-4/33879",
# "https://www.uwl.ac.uk/course/event-management-tourism-4/34851",
# "https://www.uwl.ac.uk/course/hospitality-management-foundation-year-0/35294",
# "https://www.uwl.ac.uk/course/hospitality-management-and-food-studies-foundation-year-0/35296",
# "https://www.uwl.ac.uk/course/hospitality-entrepreneurship-0/36102",
# "https://www.uwl.ac.uk/course/international-business-management-foundation-year-0/35932",
# "https://www.uwl.ac.uk/course/hospitality-management-and-food-studies-3/32222",
# "https://www.uwl.ac.uk/course/information-technology-management-business-itmb-industrial-placement-0/34601",
# "https://www.uwl.ac.uk/course/accounting-and-finance-internship-0/35904",
# "https://www.uwl.ac.uk/course/accounting-and-finance-foundation-year-0/35903",
# "https://www.uwl.ac.uk/course/advertising-and-public-relations-foundation-year-0/34984",
# "https://www.uwl.ac.uk/course/advertising-and-public-relations-0/34656",
# "https://www.uwl.ac.uk/course/culinary-arts-management-0/33869",
# "https://www.uwl.ac.uk/course/media-production-foundation-year-0/34992",
# "https://www.uwl.ac.uk/course/media-and-communications-1/35734",
# "https://www.uwl.ac.uk/course/media-production-2/34957",
# "https://www.uwl.ac.uk/course/content-media-and-film-production-foundation-year-0/36094",
# "https://www.uwl.ac.uk/course/content-media-and-film-production-0/35984",
# "https://www.uwl.ac.uk/course/journalism-0/35513",
# "https://www.uwl.ac.uk/course/journalism-foundation-year-0/35517",
# "https://www.uwl.ac.uk/course/english-and-media-and-communications-foundation-year-0/35015",
# "https://www.uwl.ac.uk/course/english-and-media-and-communications-1/35010",
# "https://www.uwl.ac.uk/course/electrical-and-electronic-engineering-foundation-year-0/34856",
# "https://www.uwl.ac.uk/course/interior-design-0/36001",
# "https://www.uwl.ac.uk/course/graphic-design-foundation-year-0/34998",
# "https://www.uwl.ac.uk/course/fashion-promotion-and-imaging-0/35446",
# "https://www.uwl.ac.uk/course/fashion-promotion-and-imaging-foundation-year-0/35645",
# "https://www.uwl.ac.uk/course/fashion-and-textiles-0/32329",
# "https://www.uwl.ac.uk/course/fashion-branding-and-marketing-0/35702",
# "https://www.uwl.ac.uk/course/fashion-buying-and-management-0/34969",
# "https://www.uwl.ac.uk/course/graphic-design-visual-communication-and-illustration-1/33653",
# "https://www.uwl.ac.uk/course/music-performance-and-recording-0/35853",
# "https://www.uwl.ac.uk/course/voice-performance-0/35893",
# "https://www.uwl.ac.uk/course/music-performance-technology-foundation-year-0/35857",
# "https://www.uwl.ac.uk/course/composition-foundation-year-0/35841",
# "https://www.uwl.ac.uk/course/music-technology-specialist-1/35878",
# "https://www.uwl.ac.uk/course/music-technology-audio-post-production-foundation-year-0/35860",
# "https://www.uwl.ac.uk/course/electronic-music-production-foundation-year-0/35863",
# "https://www.uwl.ac.uk/course/live-sound-production-1/35885",
# "https://www.uwl.ac.uk/course/live-sound-production-foundation-year-0/35887",
# "https://www.uwl.ac.uk/course/music-mixing-and-mastering-foundation-year-0/35866",
# "https://www.uwl.ac.uk/course/music-recording-and-production-foundation-year-0/35869",
# "https://www.uwl.ac.uk/course/music-technology-specialist-foundation-year-0/35880",
# "https://www.uwl.ac.uk/course/music-performance-and-recording-foundation-year-0/35854",
# "https://www.uwl.ac.uk/course/composition-1/35839",
# "https://www.uwl.ac.uk/course/music-performance-and-music-management-0/35852",
# "https://www.uwl.ac.uk/course/music-performance-technology-1/35855",
# "https://www.uwl.ac.uk/course/music-technology-performance-1/35881",
# "https://www.uwl.ac.uk/course/acting-0/35888",
# "https://www.uwl.ac.uk/course/acting-foundation-year-0/35889",
# "https://www.uwl.ac.uk/course/text-and-performance-0/35897",
# "https://www.uwl.ac.uk/course/text-and-performance-foundation-year-0/35898",
# "https://www.uwl.ac.uk/course/actor-musicianship-foundation-year-0/35896",
# "https://www.uwl.ac.uk/course/voice-performance-foundation-year-0/35894",
# "https://www.uwl.ac.uk/course/photography-0/34956",
# "https://www.uwl.ac.uk/course/photography-foundation-year-0/34994",
# "https://www.uwl.ac.uk/course/visual-effects-foundation-year-0/34990",
# "https://www.uwl.ac.uk/course/actor-musicianship-0/35895",
# "https://www.uwl.ac.uk/course/interior-design-foundation-year-0/36003",
# "https://www.uwl.ac.uk/course/music-performance-1/35848",
# "https://www.uwl.ac.uk/course/fashion-branding-and-marketing-foundation-year-0/34987",
# "https://www.uwl.ac.uk/course/fashion-buying-and-management-foundation-year-0/35354",
# "https://www.uwl.ac.uk/course/songwriting-and-recording-0/35851",
# "https://www.uwl.ac.uk/course/fashion-and-textiles-foundation-year-0/34793",
# "https://www.uwl.ac.uk/course/musical-theatre-0/35890",
# "https://www.uwl.ac.uk/course/education-studies-1/35797",
# "https://www.uwl.ac.uk/course/early-years-education-1/35793",
# "https://www.uwl.ac.uk/course/early-years-education-foundation-year-0/35830",
# "https://www.uwl.ac.uk/course/education-studies-foundation-year-0/35831", ]
        for link in links:
            url = "https://www.uwl.ac.uk" + link
            # url = link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "https://www.uwl.ac.uk/"
        item['university'] = "University of West London"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        try:
            programmeDegreetype = response.xpath(
                "//h1[@id='page-title']//text()").extract()
            # print("programmeDegreetype: ", programmeDegreetype)
            programmeDegreetypeStr = ''.join(programmeDegreetype)

            degree_type = re.findall(r"^\w+\s\(Hons\)|^\(\w+\)|^\w+", programmeDegreetypeStr)
            # print("degree_type: ", degree_type)
            degree_type_str = ''.join(degree_type).strip()
            item['degree_name'] = ''.join(degree_type).replace("(Hons)", "").strip()
            print("item['degree_name']: ", item['degree_name'])

            item['programme_en'] = programmeDegreetypeStr.replace(degree_type_str, '').strip()
            print("item['programme_en']: ", item['programme_en'])

            mode = response.xpath("//dt[contains(text(), 'Study mode')]/following-sibling::dd[1]//text()").extract()
            clear_space(mode)
            # print("mode: ", mode)

            location = response.xpath("//dt[contains(text(), 'Location')]/following-sibling::dd[1]//text()").extract()
            item['location'] = ''.join(location).replace("See location information", "").strip()
            # print("item['location']: ", item['location'])

            start_date = response.xpath("//dt[contains(text(), 'Start date')]/following-sibling::dd[1]//text()").extract()
            clear_space(start_date)
            # print("start_date: ", start_date)
            item['start_date'] = getStartDate(''.join(start_date))
            # print("item['start_date']: ", item['start_date'])

            duration = response.xpath("//dt[contains(text(), 'Duration')]/following-sibling::dd[1]//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            ucascode = response.xpath(
                "//dt[contains(text(), 'UCAS code')]/following-sibling::dd[1]//text()").extract()
            clear_space(ucascode)
            item['ucascode'] = ''.join(ucascode).strip()
            # print("item['ucascode'] = ", item['ucascode'])

            department = response.xpath("//dt[contains(text(), 'Department')]/following-sibling::dd[1]//text()").extract()
            item['department'] = ''.join(department).strip()
            # print("item['department']: ", item['department'])

            tuition_fee = response.xpath("//h4[contains(text(),'Overseas students')]/following-sibling::dl[1]//dt[contains(text(), 'Main fee')]/following-sibling::dd[1]//text()").extract()
            # print("tuition_fee: ", tuition_fee)
            if len(tuition_fee) > 0:
                item['tuition_fee'] = getTuition_fee(''.join(tuition_fee))
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee']: ", item['tuition_fee'])
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            # //div[@id='course-detail']
            modules = response.xpath("//div[@id='course-detail']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])

            # //div[@id='course-detail']
            entry_requirements = response.xpath("//div[@id='entry-requirements']//text()").extract()
            # item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            alevel = response.xpath("//*[contains(text(),'A Level')]//text()|//*[contains(text(),'A level')]//text()").extract()
            item['alevel'] = clear_lianxu_space(alevel)
            # print("item['alevel']: ", item['alevel'])

            ielts_desc = response.xpath("//div[@id='entry-requirements']//*[contains(text(),'IELTS')]/text()").extract()
            clear_space(ielts_desc)
            # print("ielts_desc: ", ielts_desc)
            ielts_desc_re = re.findall(r'.{1,50}IELTS.{1,50}', ''.join(ielts_desc))
            # print("ielts_desc_re: ", ielts_desc_re)
            if len(ielts_desc_re) > 0:
                item['ielts_desc'] = ielts_desc_re[-1]
            # print("item['ielts_desc']: ", item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            how_to_apply = response.xpath("//div[@id='how-to-apply']").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(how_to_apply))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            assessment_en = response.xpath("//h3[contains(text(),'Teaching methods')]/preceding-sibling::*[1]/following-sibling::*[position()<5]|"
                                           "//*[contains(text(),'Assessment')]/preceding-sibling::*[1]/following-sibling::*[position()<5]|"
                                           "//html//div/strong[contains(text(),'How will I be taught?')]/..|"
                                           "//strong[contains(text(),'course be assessed?')]/..|//strong[contains(text(),'course be assessed?')]/../following-sibling::div").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            print("item['assessment_en']: ", item['assessment_en'])

            career_en = response.xpath(
                "//div[@id='career-progression-and-study']|"
                "//div[@id='jobs-and-placements']|"
                "//html//*[contains(text(),'Career and study progression')]/../following-sibling::*[position()<5]").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en)).replace("<div></div>","").strip()
            print("item['career_en']: ", item['career_en'])

            overview_en = response.xpath("//div[@id='course-summary']/*[position()<last()]").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
            # print("item['overview_en']: ", item['overview_en'])

            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<h3>Undergraduate entry&nbsp;</h3>
<p>Applicants with the following&nbsp;qualiﬁcations&nbsp;will be considered for entry on an undergraduate degree:</p>
<p>&bull;&nbsp;&nbsp; &nbsp; Chinese university / college entrance examination (Gaokao) with an overall average 65% or higher</p>
<p>&bull;&nbsp;&nbsp; &nbsp; Diploma from specialised college (zhongzhuan) with an overall average of 65% or higher</p>
<p>&bull;&nbsp;&nbsp; &nbsp; Graduation Certificate awarded at &lsquo;Zhuanke&rdquo; / &lsquo;Dazhuan&rsquo; level from universities / colleges with an overall 65% or higher</p>
<p>&bull;&nbsp;&nbsp; &nbsp; Graduation Certificate - Sub degree (Gaozhi) with an overall 65% or above</p>
<p>&bull;&nbsp;&nbsp;&nbsp;&nbsp; British/International A Levels (from a minimum 112&nbsp;UCAS&nbsp;tariff points depending on course)</p>
<p>&bull; &nbsp; &nbsp;&nbsp;IB&nbsp;Diploma (from a minimum 25 points depending on course)</p>
<p>&bull;&nbsp;&nbsp; &nbsp; Second and final year entry on a bachelor&#39;s degree may be available for those with a Higher National Diploma (HND) from the UK with a merit profile</p>
<p>&bull;&nbsp;&nbsp;&nbsp;&nbsp; A recognised foundation course</p>"""]))
            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

