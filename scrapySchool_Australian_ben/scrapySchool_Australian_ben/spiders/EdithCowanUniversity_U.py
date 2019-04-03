# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_Australian_ben.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_ben.getItem import get_item
from scrapySchool_Australian_ben.getTuition_fee import getTuition_fee
from scrapySchool_Australian_ben.items import ScrapyschoolAustralianBenItem
from scrapySchool_Australian_ben.remove_tags import remove_class
from scrapySchool_Australian_ben.getStartDate import getStartDate
from scrapySchool_Australian_ben.getDuration import getIntDuration
from scrapySchool_Australian_ben.getIELTS import get_ielts
from lxml import etree
import requests
from scrapy.http import Request
from urllib import parse


# 2019/03/26 星期二 数据更新
class EdithCowanUniversity_USpider(scrapy.Spider):
    name = "EdithCowanUniversity_U"
    # start_urls = ["https://www.ecu.edu.au/degrees/courses?f.Resident%20Type%7Cr=International&profile=collapsing&f.Degree%20Type%7Ce=Undergraduate&collection=ecu-fs-courses&f.Delivery%20Mode%7CS=On%20Campus&form=courses&f.Study%20Mode%7CT=Full%20Time&f.Course+Type%7Cf=Bachelors+Degrees+%28Undergraduate%29",
    #               "https://www.ecu.edu.au/degrees/courses?f.Resident%20Type%7Cr=International&profile=collapsing&f.Degree%20Type%7Ce=Undergraduate&collection=ecu-fs-courses&f.Delivery%20Mode%7CS=On%20Campus&form=courses&f.Study%20Mode%7CT=Full%20Time&f.Course+Type%7Cf=Honours+%28Undergraduate%29"]
    start_urls = ["https://www.ecu.edu.au/degrees/courses?f.Study%20Mode%7CT=Full%20Time&f.Resident%20Type%7Cr=International&profile=collapsing&f.Degree%20Type%7Ce=Undergraduate&collection=ecu-fs-courses&form=courses"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        links = response.xpath("//a[contains(text(),'Bachelor of')]/@href").extract()
        clear_space(links)
        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield Request(parse.urljoin(response.url, url), callback=self.parse_data)

        next_url = response.xpath("//div[@class='pagination hidden-phone']//a[@title='Next Page']/@href").extract_first("")
        print("next====", next_url)
        if next_url:
            yield Request(parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "Edith Cowan University"
        # item['country'] = 'Australia'
        # item['website'] = 'https://www.uts.edu.au'
        item['url'] = response.url
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        # 组合字典
        links = ["http://www.ecu.edu.au/degrees/courses/bachelor-of-arts",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-south-west",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-psychology-and-addiction-studies",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-psychology-and-counselling",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-psychology",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-psychology-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-psychology-criminology-and-justice",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-bachelor-of-commerce",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-bachelor-of-media-and-communication",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-bachelor-of-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-commerce-bachelor-of-arts-psychology",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-contemporary-arts",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-counselling",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-criminology-and-justice",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-criminology-and-justice-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-design",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-laws-bachelor-of-arts",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-laws-bachelor-of-criminology-and-justice",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-laws-bachelor-of-psychological-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-media-and-communication",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-psychological-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-psychology",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-psychology-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-social-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-social-science-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-social-work",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-social-work-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-youth-work",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-bachelor-of-commerce",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-commerce",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-commerce-professional",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-commerce-bachelor-of-arts-psychology",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-honours-bachelor-of-commerce",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-honours-bachelor-of-laws",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-hospitality-and-tourism-management",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-international-hotel-and-resort-management",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-laws-graduate-entry",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-laws",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-laws-bachelor-of-arts",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-laws-bachelor-of-commerce",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-laws-bachelor-of-criminology-and-justice",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-laws-bachelor-of-psychological-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-marketing-advertising-and-public-relations",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-exercise-and-sports-science-bachelor-of-commerce-sport-business",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-bachelor-of-commerce",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-sport-recreation-and-event-management",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-aviation",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-chemical-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-civil-and-environmental-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-civil-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-computer-systems-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-computer-systems-honours-bachelor-of-computer-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-electrical-and-renewable-energy-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-electrical-power-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-electronics-and-communications-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-instrumentation-control-and-automation-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-marine-and-offshore-engineering-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-mechanical-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-mechatronics-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-mechatronics-honours-bachelor-of-technology-motorsports",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-naval-architecture-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-ocean-engineering-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-petroleum-engineering-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-honours-bachelor-of-commerce",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-honours-bachelor-of-laws",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-honours-bachelor-of-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-bachelor-of-commerce",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-technology-aeronautical",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-technology-electronic-and-computer-systems",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-technology-engineering",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-technology-motorsports",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-health-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-health-science-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-medical-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-biomedical-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-exercise-and-sports-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-exercise-and-sports-science-bachelor-of-commerce-sport-business",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-exercise-science-and-rehabilitation",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-medical-science-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-occupational-therapy",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-occupational-therapy-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-paramedical-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-sports-science-and-football",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-sports-science-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-bachelor-of-commerce",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-speech-pathology",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-speech-pathology-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-nursing-studies",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-nursing",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-nursing-bachelor-of-science-midwifery",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-computer-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-computer-science-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-counter-terrorism-security-and-intelligence",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-computer-systems-honours-bachelor-of-computer-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-engineering-honours-bachelor-of-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-information-technology",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-information-technology-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-biological-sciences",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-conservation-and-wildlife-biology",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-cyber-security",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-environmental-management",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-marine-and-freshwater-biology",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-mathematics-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-physics-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-security",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-security-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-science-bachelor-of-commerce",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-sustainability",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-education-early-childhood-studies",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-education-primary",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-education-secondary",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-acting",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-arts-management",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-arts-management-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-dance",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-dance-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-arts-music-theatre",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-education-secondary",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-music",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-music-honours",
"http://www.ecu.edu.au/degrees/courses/bachelor-of-performing-arts", ]
        programme_dict = {}
        programme_list = ["Bachelor of Arts",
"Bachelor of Arts (South West)",
"Bachelor of Arts (Psychology and Addiction Studies)",
"Bachelor of Arts (Psychology and Counselling)",
"Bachelor of Arts (Psychology)",
"Bachelor of Arts (Psychology) Honours",
"Bachelor of Arts (Psychology, Criminology and Justice)",
"Bachelor of Arts Honours",
"Bachelor of Arts/Bachelor of Commerce",
"Bachelor of Arts/Bachelor of Media and Communication",
"Bachelor of Arts/Bachelor of Science",
"Bachelor of Commerce/Bachelor of Arts (Psychology)",
"Bachelor of Contemporary Arts",
"Bachelor of Counselling",
"Bachelor of Criminology and Justice",
"Bachelor of Criminology and Justice Honours",
"Bachelor of Design",
"Bachelor of Laws/Bachelor of Arts",
"Bachelor of Laws/Bachelor of Criminology and Justice",
"Bachelor of Laws/Bachelor of Psychological Science",
"Bachelor of Media and Communication",
"Bachelor of Psychological Science",
"Bachelor of Science (Psychology)",
"Bachelor of Science (Psychology) Honours",
"Bachelor of Social Science",
"Bachelor of Social Science Honours",
"Bachelor of Social Work",
"Bachelor of Social Work Honours",
"Bachelor of Youth Work",
"Bachelor of Arts/Bachelor of Commerce",
"Bachelor of Commerce",
"Bachelor of Commerce Professional",
"Bachelor of Commerce/Bachelor of Arts (Psychology)",
"Bachelor of Engineering Honours/Bachelor of Commerce",
"Bachelor of Engineering Honours/Bachelor of Laws",
"Bachelor of Hospitality and Tourism Management",
"Bachelor of International Hotel and Resort Management",
"Bachelor of Laws (Graduate Entry)",
"Bachelor of Laws",
"Bachelor of Laws/Bachelor of Arts",
"Bachelor of Laws/Bachelor of Commerce",
"Bachelor of Laws/Bachelor of Criminology and Justice",
"Bachelor of Laws/Bachelor of Psychological Science",
"Bachelor of Marketing, Advertising and Public Relations",
"Bachelor of Science (Exercise and Sports Science)/Bachelor of Commerce (Sport Business)",
"Bachelor of Science/Bachelor of Commerce",
"Bachelor of Sport, Recreation and Event Management",
"Bachelor of Aviation",
"Bachelor of Engineering (Chemical) Honours",
"Bachelor of Engineering (Civil and Environmental) Honours",
"Bachelor of Engineering (Civil) Honours",
"Bachelor of Engineering (Computer Systems) Honours",
"Bachelor of Engineering (Computer Systems) Honours/Bachelor of Computer Science",
"Bachelor of Engineering (Electrical and Renewable Energy) Honours",
"Bachelor of Engineering (Electrical Power) Honours",
"Bachelor of Engineering (Electronics and Communications) Honours",
"Bachelor of Engineering (Instrumentation Control and Automation) Honours",
"Bachelor of Engineering (Marine and Offshore Engineering) Honours",
"Bachelor of Engineering (Mechanical) Honours",
"Bachelor of Engineering (Mechatronics) Honours",
"Bachelor of Engineering (Mechatronics) Honours/Bachelor of Technology (Motorsports)",
"Bachelor of Engineering (Naval Architecture) Honours",
"Bachelor of Engineering (Ocean Engineering) Honours",
"Bachelor of Engineering (Petroleum Engineering) Honours",
"Bachelor of Engineering Honours/Bachelor of Commerce",
"Bachelor of Engineering Honours/Bachelor of Laws",
"Bachelor of Engineering Honours/Bachelor of Science",
"Bachelor of Engineering Science",
"Bachelor of Science/Bachelor of Commerce",
"Bachelor of Technology (Aeronautical)",
"Bachelor of Technology (Electronic and Computer Systems)",
"Bachelor of Technology (Engineering)",
"Bachelor of Technology (Motorsports)",
"Bachelor of Health Science",
"Bachelor of Health Science Honours",
"Bachelor of Medical Science",
"Bachelor of Science (Biomedical Science)",
"Bachelor of Science (Exercise and Sports Science)",
"Bachelor of Science (Exercise and Sports Science)/Bachelor of Commerce (Sport Business)",
"Bachelor of Science (Exercise Science and Rehabilitation)",
"Bachelor of Science (Medical Science) Honours",
"Bachelor of Science (Occupational Therapy)",
"Bachelor of Science (Occupational Therapy) Honours",
"Bachelor of Science (Paramedical Science)",
"Bachelor of Science (Sports Science and Football)",
"Bachelor of Science (Sports Science) Honours",
"Bachelor of Science/Bachelor of Commerce",
"Bachelor of Speech Pathology",
"Bachelor of Speech Pathology Honours",
"Bachelor of Science (Nursing Studies)",
"Bachelor of Science (Nursing)",
"Bachelor of Science (Nursing)/Bachelor of Science (Midwifery)",
"Bachelor of Computer Science",
"Bachelor of Computer Science Honours",
"Bachelor of Counter Terrorism Security and Intelligence",
"Bachelor of Engineering (Computer Systems) Honours/Bachelor of Computer Science",
"Bachelor of Engineering Honours/Bachelor of Science",
"Bachelor of Information Technology",
"Bachelor of Information Technology Honours",
"Bachelor of Science",
"Bachelor of Science (Biological Sciences)",
"Bachelor of Science (Conservation and Wildlife Biology)",
"Bachelor of Science (Cyber Security)",
"Bachelor of Science (Environmental Management)",
"Bachelor of Science (Marine and Freshwater Biology)",
"Bachelor of Science (Mathematics) Honours",
"Bachelor of Science (Physics) Honours",
"Bachelor of Science (Security)",
"Bachelor of Science (Security) Honours",
"Bachelor of Science Honours",
"Bachelor of Science/Bachelor of Commerce",
"Bachelor of Sustainability",
"Bachelor of Education (Early Childhood Studies)",
"Bachelor of Education (Primary)",
"Bachelor of Education (Secondary)",
"Bachelor of Arts (Acting)",
"Bachelor of Arts (Arts Management)",
"Bachelor of Arts (Arts Management) Honours",
"Bachelor of Arts (Dance)",
"Bachelor of Arts (Dance) Honours",
"Bachelor of Arts (Music Theatre)",
"Bachelor of Education (Secondary)",
"Bachelor of Music",
"Bachelor of Music Honours",
"Bachelor of Performing Arts", ]
        for link in range(len(links)):
            url = links[link]
            programme_dict[url] = programme_list[link]
        item['major_type1'] = programme_dict.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            programme = response.xpath("//h2[contains(text(), 'Bachelor of')]//text()").extract()
            clear_space(programme)
            programme = ''.join(programme).strip()
            item['degree_name'] = programme
            print("item['degree_name']: ", item['degree_name'])

            pro_re = re.findall(r"Bachelor", item['degree_name'])
            # print("pre_re: ", pro_re)
            if len(pro_re) == 1:
                programme_re = re.findall(r"\(.+\)", item['degree_name'].replace("Honours", "").replace("(Advanced)", ""))
                if len(programme_re) > 0:
                    item['programme_en'] = ''.join(programme_re).replace("(", "").replace(")", "").strip()
                else:
                    item['programme_en'] = item['degree_name'].replace("Bachelor of", "").strip()
                print("item['programme_en']: ", item['programme_en'])

                overview = response.xpath("//span[@id='overview']/..").extract()
                item['degree_overview_en'] = remove_class(clear_lianxu_space(overview))
                # print("item['degree_overview_en']: ", item['degree_overview_en'])

                entry_requirements = response.xpath("//div[@id='before-you-start']").extract()
                entry_requirements_str = ''.join(entry_requirements).strip()
                item['rntry_requirements_en'] = remove_class(clear_lianxu_space(entry_requirements))
                # print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

                modules = response.xpath(
                    "//h4[contains(text(),'Course structure')]|//div[@class='structure-heading']").extract()
                item['modules_en'] = remove_class(clear_lianxu_space(modules))
                # print("item['modules_en']: ", item['modules_en'])

                career = response.xpath("//h4[contains(text(),'Employment opportunities')]|//h4[contains(text(),'Employment opportunities')]/following-sibling::*[1]|"
                                        "//h4[contains(text(),'Possible future job titles')]|//h4[contains(text(),'Possible future job titles')]/following-sibling::*[1]").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career))
                if item['career_en'] == "":
                    print("***career_en 为空")
                print("item['career_en']: ", item['career_en'])

                location = response.xpath("//div[@class='courseOverview__info courseOverview__info--international courseOverview__info--noOnline']//div[@class='studyCampus__location studyCampus__location--joondalup studyCampus__location--active']/h4//text()|"
                                          "//div[@class='courseOverview__info courseOverview__info--international courseOverview__info--noOnline']//div[@class='studyCampus__location studyCampus__location--mtLawley studyCampus__location--active']/h4//text()|"
                                          "//div[@class='courseOverview__info courseOverview__info--international courseOverview__info--noOnline']//div[@class='studyCampus__location studyCampus__location--bunbury studyCampus__location--active']/h4//text()").extract()
                clear_space(location)
                location = ','.join(location).strip().strip().strip(',').strip()
                item['location'] = location
                location_tmp = item['location']
                print("item['location']: ", item['location'])

                duration = response.xpath(
                    "//div[@class='courseOverview__info courseOverview__info--international courseOverview__info--noOnline']//p[contains(text(),'year')]//text()|"
                    "//div[@class='courseOverview__info courseOverview__info--international']//p[contains(text(),'year')]//text()").extract()
                clear_space(duration)
                print("duration: ", duration)
                duration_re = re.findall(r"Start\sSemester.*", ''.join(duration).strip())
                print(duration_re, "===")
                item['start_date'] = ','.join(duration_re)
                item['duration'] = ''.join(duration).replace(''.join(duration_re), "").strip()
                print("item['duration']: ", item['duration'])

                other = response.xpath("//span[@class='courseOverview__subHeader alert-warning alert']//text()").extract()
                item['other'] = ''.join(other)
                print("item['other']: ",item['other'])

                # https://www.ecu.edu.au/future-students/course-entry/english-competency
                item['ielts_desc'] = "An overall band score of 6.0, with no individual band less than 6.0"
                item['ielts'] = "6.0"
                item['ielts_l'] = "6.0"
                item['ielts_s'] = "6.0"
                item['ielts_r'] = "6.0"
                item['ielts_w'] = "6.0"
                item['toefl_desc'] = "Minimum score of 70, with no individual score less than 17"
                item['toefl'] = "70"
                item['toefl_l'] = "17"
                item['toefl_s'] = "17"
                item['toefl_r'] = "17"
                item['toefl_w'] = "17"

                if "This course is not offered for study on-campus to international students with a student visa" not in item['other']:
                    major_list_url = response.xpath("//div[@class='section']//ul[@class='core-units']//a/@href").extract()
                    clear_space(major_list_url)
                    print("major_list_url: ", major_list_url)
                    print(len(major_list_url))

                    if len(major_list_url) == 0:
                        item['url'] = response.url
                        print("item['url']2: ", item['url'])
                        yield item
                    else:
                        for major_url in major_list_url:
                            headers_base = {
                                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36", }
                            data = requests.get(major_url, headers=headers_base)
                            response_major = etree.HTML(data.text)
                            item['url'] = major_url
                            print("item['url']_major: ", item['url'])

                            programme_major = response_major.xpath("//span[@id='overview']/following-sibling::h2//text()")
                            item['programme_en'] = ''.join(programme_major).strip()
                            print("item['programme_en']_major: ", item['programme_en'])

                            location_major = response_major.xpath(
                                "//div[@class='studyCampus__location studyCampus__location--active']/h4//text()")
                            item['location'] = ','.join(location_major).strip().strip(',').strip()
                            if item['location'] == "":
                                item['location'] = location_tmp
                            print("item['location']_major: ", item['location'])

                            overview_en = response_major.xpath(
                                "//span[@id='overview']/..")
                            overview_en_str = ""
                            if len(overview_en) > 0:
                                for o in overview_en:
                                    overview_en_str += etree.tostring(o, encoding='unicode', method='html')
                            item['overview_en'] = remove_class(clear_lianxu_space([overview_en_str]))
                            print("item['overview_en']_major: ", item['overview_en'])

                            modules_en = response_major.xpath(
                                "//h4[contains(text(),'Structure')]|//h4[contains(text(),'Course structure')]|//div[@class='structure-heading']")
                            modules_en_str = ""
                            if len(modules_en) > 0:
                                for o in modules_en:
                                    modules_en_str += etree.tostring(o, encoding='unicode', method='html')
                            item['modules_en'] = remove_class(clear_lianxu_space([modules_en_str]))
                            print("item['modules_en']_major: ", item['modules_en'])
                            yield item
        except Exception as e:
            with open("scrapySchool_Australian_yan/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

