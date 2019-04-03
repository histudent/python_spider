# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_Australian_ben.clearSpace import clear_space, clear_space_str
from scrapySchool_Australian_ben.getItem import get_item
from scrapySchool_Australian_ben.getTuition_fee import getTuition_fee
from scrapySchool_Australian_ben.items import ScrapyschoolAustralianBenItem

class TheUniversityOfMelbourne_U1Spider(scrapy.Spider):
    name = "TheUniversityOfMelbourne_U1"
    start_urls = ["https://coursesearch.unimelb.edu.au/",
]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        links = response.xpath("//div[@class='undergraduate-intro']//ul[@class='course-list']/li/a[contains(text(), 'Bachelor of')]/@href").extract()
        print("subject link = ", links)
        for link in links:
            url = "https://coursesearch.unimelb.edu.au" + link
            yield scrapy.Request(url, callback=self.parse_programmeUrl)

    def parse_programmeUrl(self, response):
        degree_type = response.xpath("//div[@class='headline']/h1/text()").extract()
        clear_space(degree_type)
        degree_type = ''.join(degree_type)
        # print("degree_type: ", degree_type)
        department = ''
        if "Bachelor of " in degree_type:
            department = degree_type.split("Bachelor of ")
            department = ''.join(department)
        # print("department: ", department)

        durationMode = response.xpath("//div[@class='course-length icn icn-duration']/text()").extract()
        clear_space(durationMode)
        durationMode = ''.join(durationMode)
        # print("durationMode: ", durationMode)
        duration = list(re.findall("(3\syears)|(1\syear)|(4\syears)|(4\syear)", durationMode)[0])
        # print("duration: ", duration)
        duration = ''.join(duration)
        mode = ''.join(durationMode.split(duration))
        # print("mode: ", mode)

        location = response.xpath("//div[@class='course-location icn icn-location']//text()").extract()
        clear_space(location)
        location = ''.join(location)
        # print("location: ", location)

        degree_description = response.xpath("//div[@class='primary']//div[@class='description']//text()").extract()
        clear_space(degree_description)
        degree_description = ''.join(degree_description)
        # print("degree_description: ", degree_description)

        # //html//div[@class='secondary']//p[2]/strong[1]
        feedict = {"Bachelor of Agriculture": "40976",
"Bachelor of Arts": "31096–35012",
"Bachelor of Biomedicine": "38208–40648",
"Bachelor of Commerce": "38648–41144",
"Bachelor of Design": "28664–41272",
"Bachelor of Fine Arts": "27808–44208",
"Bachelor of Music": "28664–31184",
"Bachelor of Oral Health": "58120",
"Bachelor of Science": "37468–41232",}
        tuition_fee = feedict.get(degree_type)
        # print("tuition_fee: ", tuition_fee)


        links = response.xpath("//div[@class='wrapper']/div[@class='primary']/div/ul/li/a/@href").extract()
        if len(links) != 0:
            for link in links:
                url = "https://coursesearch.unimelb.edu.au" + link
                yield scrapy.Request(url, callback=self.parse_data,
                                     meta={"degree_type": degree_type,"duration": duration, "mode": mode, "location": location,
                                           "degree_description": degree_description, "tuition_fee": tuition_fee, "department":department})

    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "The University of Melbourne"
        # item['country'] = 'Australia'
        # item['website'] = 'http://www.unimelb.edu.au/'
        item['url'] = response.url
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        degree_type = response.meta['degree_type']
        item['degree_name'] = degree_type
        print("item['degree_name']: ", item['degree_name'])

        department = response.meta['department']
        item['department'] = department
        print("item['department']: ", item['department'])

        duration = response.meta['duration']
        item['duration'] = duration
        print("item['duration']: ", item['duration'])

        # mode = response.meta['mode']
        # item['mode'] = mode
        # print("item['mode']: ", item['mode'])

        location = response.meta['location']
        item['location'] = location
        print("item['location']: ", item['location'])

        degree_description = response.meta['degree_description']
        item['degree_overview_en'] = degree_description
        print("item['degree_overview_en']: ", item['degree_overview_en'])

        tuition_fee = response.meta['tuition_fee']
        item['tuition_fee'] = tuition_fee
        print("item['tuition_fee']: ", item['tuition_fee'])
        try:
            programme = response.xpath("//div[@class='headline']/h1/text()").extract()
            clear_space(programme)
            programme = ''.join(programme)
            item['programme_en'] = programme
            print("item['programme_en']: ", item['programme_en'])

            # //div[@class='description']
            overviewCareer = response.xpath("//div[@class='description']//text()").extract()
            clear_space(overviewCareer)
            # print("overviewCareer: ", overviewCareer)
            careerIndex = -1
            if "Careers" in overviewCareer:
                careerIndex = overviewCareer.index("Careers")
            overview = overviewCareer[:careerIndex]
            item['overview_en'] = ''.join(overview)
            # print("item['overview_en']: ", item['overview_en'])

            career = overviewCareer[careerIndex:]
            item['career_en'] = ''.join(career)
            # print("item['career_en']: ", item['career_en'])

            modules = response.xpath("//html//li/div[1]/a/text()").extract()
            modules = ''.join(modules)
            item['modules_en'] = "Subjects you could take in this major: " + modules
            # print("item['modules_en']: ", item['modules_en'])

#             item['entry_requirements'] = """To be eligible for entry to an undergraduate degree you must fulfill all of the following requirements:Complete the Victorian Certificate of Education (VCE) or an equivalent Australian or overseas qualification (see qualifications below)Complete and achieve the required grades in each of the prerequisite subjects for the course and any prerequisite tests, interviews or auditions (see Course Search for details about prerequisite subjects and scores)Meet the English language requirements"""
#             item['average_score'] = '''Agriculture: 75; Arts: 80; Biomedicine: 91; Commerce: 86; Design: 80; Fine Arts: NA^; Music: 67^; Oral Health: 80#; Science: 80; '''
#             item['IELTS'] = 'an overall band score of 6.5 or more in the Academic International English Language Testing System (IELTS), with no bands less than 6.0.'
#             item['TOEFL'] = '''Paper based test - a score of 577 or more including a score of 4.5 in the Test of Written English.
# Internet based test - a score of 79 and scores of:'''
#             item['TOEFL_L'] = '13'
#             item['TOEFL_S'] = '18'
#             item['TOEFL_R'] = '13'
#             item['TOEFL_W'] = '21'
#             item['how_to_apply'] = "https://futurestudents.unimelb.edu.au/admissions/applications/ug-int"

            yield item
        except Exception as e:
            with open("scrapySchool_Australian_ben/error/"+item['university']+str(item['degree_type'])+".txt", 'w', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

