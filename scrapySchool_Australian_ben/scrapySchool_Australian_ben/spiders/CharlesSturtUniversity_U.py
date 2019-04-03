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
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 2019/03/26 星期二 数据更新
class CharlesSturtUniversity_USpider(scrapy.Spider):
    name = "CharlesSturtUniversity_U"
    start_urls = ["http://futurestudents.csu.edu.au/courses/postgraduate"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    # feeDict = {'Bachelor of Accounting0': 'Albury-Wodonga, Bathurst, Port Macquarie, Wagga Wagga: 23600\xa0(64 Pts)', 'Bachelor of Accounting1': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 25200\xa0(64 Pts)', 'Bachelor of Agricultural Business Management2': 'Wagga Wagga: 28800\xa0(64 Pts)', 'Bachelor of Agricultural Science3': 'Wagga Wagga: 28800\xa0(64 Pts)', 'Bachelor of Animal Science4': 'Wagga Wagga: 28800\xa0(64 Pts)', 'Bachelor of Applied Science (Outdoor Recreation and Ecotourism)5': 'Albury-Wodonga, Port Macquarie: 28800\xa0(64 Pts)', 'Bachelor of Applied Science (Parks Recreation and Heritage)6': 'Albury-Wodonga, Port Macquarie: 28800\xa0(64 Pts)', 'Bachelor of Arts7': 'Bathurst, Wagga Wagga: 19200\xa0(64 Pts)', 'Bachelor of Business (Human Resource Management)8': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 25200\xa0(64 Pts)', 'Bachelor of Business (Management)9': 'Albury-Wodonga, Bathurst, Wagga Wagga: 23600\xa0(64 Pts)', 'Bachelor of Business (Management)10': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 25200\xa0(64 Pts)', 'Bachelor of Business (Marketing)11': 'Albury-Wodonga, Bathurst: 23600\xa0(64 Pts)', 'Bachelor of Business (Marketing)12': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 25200\xa0(64 Pts)', 'Bachelor of Business Studies13': 'Albury-Wodonga, Bathurst, Port Macquarie, Wagga Wagga: 23600\xa0(64 Pts)', 'Bachelor of Business Studies14': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 25200\xa0(64 Pts)', 'Bachelor of Clinical Science15': 'Orange: 28800\xa0(64 Pts)', 'Bachelor of Communication (Advertising)16': 'Bathurst, Port Macquarie: 23200\xa0(64 Pts)', 'Bachelor of Communication (Journalism)17': 'Bathurst: 23200\xa0(64 Pts)', 'Bachelor of Communication (Public Relations)18': 'Bathurst, Port Macquarie: 21600\xa0(64 Pts)', 'Bachelor of Communication (Theatre Media)19': 'Bathurst: 23200\xa0(64 Pts)', 'Bachelor of Computer Science (with specialisation)20': 'Bathurst: 23600\xa0(64 Pts)', 'Bachelor of Computing (Honours)21': 'Albury-Wodonga, Bathurst, Wagga Wagga: 23600\xa0(64 Pts)', 'Bachelor of Creative Arts and Design (Animation and Visual Effects)22': 'Wagga Wagga: 22400\xa0(64 Pts)', 'Bachelor of Creative Arts and Design (Graphic Design / Photography)23': 'Wagga Wagga: 22400\xa0(64 Pts)', 'Bachelor of Creative Arts and Design (Graphic Design)24': 'Port Macquarie: 22400\xa0(64 Pts)', 'Bachelor of Creative Arts and Design (Photography)25': 'Wagga Wagga: 22400\xa0(64 Pts)', 'Bachelor of Criminal Justice26': 'Bathurst, Port Macquarie: 21600\xa0(64 Pts)', 'Bachelor of Criminal Justice (Honours)27': 'Bathurst: 21600\xa0(64 Pts)', 'Bachelor of Dental Science28': 'Orange: 54400\xa0(64 Pts)', 'Bachelor of Education (Early Childhood and Primary)29': 'Albury-Wodonga, Bathurst, Wagga Wagga: 22080\xa0(64 Pts)', 'Bachelor of Education (Health and Physical Education)30': 'Bathurst: 22080\xa0(64 Pts)', 'Bachelor of Education (K - 12)31': 'Albury-Wodonga, Bathurst, Wagga Wagga: 22080\xa0(64 Pts)', 'Bachelor of Education (Technology and Applied Studies)32': 'Wagga Wagga: 22080\xa0(64 Pts)', 'Bachelor of Environmental Science and Management33': 'Albury-Wodonga, Port Macquarie: 28800\xa0(64 Pts)', 'Bachelor of Equine Science (with specialisation)34': 'Wagga Wagga: 28800\xa0(64 Pts)', 'Bachelor of Exercise and Sport Science35': 'Bathurst, Port Macquarie: 28800\xa0(64 Pts)', 'Bachelor of Exercise Science (Honours)36': 'Bathurst: 28800\xa0(64 Pts)', 'Bachelor of Health and Rehabilitation Science37': 'Albury-Wodonga: 28800\xa0(64 Pts)', 'Bachelor of Information Technology (with specialisations)38': 'Albury-Wodonga, Wagga Wagga: 23600\xa0(64 Pts)', 'Bachelor of Information Technology (with specialisations)39': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 26560\xa0(64 Pts)', 'Bachelor of Medical Radiation Science40': 'Port Macquarie, Wagga Wagga: 29600\xa0(64 Pts)', 'Bachelor of Medical Science41': 'Wagga Wagga: 28800\xa0(64 Pts)', 'Bachelor of Nursing42': 'Albury-Wodonga, Bathurst, Wagga Wagga: 27200\xa0(64 Pts)', 'Bachelor of Occupational Therapy43': 'Albury-Wodonga, Port Macquarie: 28800\xa0(64 Pts)', 'Bachelor of Oral Health (Therapy - Hygiene)44': 'Wagga Wagga: 34400\xa0(64 Pts)', 'Bachelor of Paramedicine45': 'Bathurst, Port Macquarie: 28800\xa0(64 Pts)', 'Bachelor of Pharmacy46': 'Orange: 28800\xa0(64 Pts)', 'Bachelor of Physiotherapy47': 'Albury-Wodonga, Orange: 31200\xa0(64 Pts)', 'Bachelor of Podiatric Medicine48': 'Albury-Wodonga: 28800\xa0(64 Pts)', 'Bachelor of Psychology49': 'Bathurst, Port Macquarie: 24000\xa0(64 Pts)', 'Bachelor of Science50': 'Wagga Wagga: 28800\xa0(64 Pts)', 'Bachelor of Science (Honours)51': 'Albury-Wodonga, Orange, Wagga Wagga: 28800\xa0(64 Pts)', 'Bachelor of Social Science (Psychology)52': 'Port Macquarie, Wagga Wagga: 24000\xa0(64 Pts)', 'Bachelor of Social Science (Psychology) / Bachelor of Business (Management)53': 'Bathurst: 24000\xa0(64 Pts)', 'Bachelor of Social Science (Psychology) / Bachelor of Business (Marketing)54': 'Bathurst: 24000\xa0(64 Pts)', 'Bachelor of Social Work55': 'Port Macquarie, Wagga Wagga: 24160\xa0(64 Pts)', 'Bachelor of Speech and Language Pathology56': 'Albury-Wodonga: 28800\xa0(64 Pts)', 'Bachelor of Stage and Screen (Television)57': 'Wagga Wagga: 22400\xa0(64 Pts)', 'Bachelor of Theology58': 'Canberra, United Theological College: 18400\xa0(64 Pts)', 'Bachelor of Theology (Honours)59': 'Canberra, United Theological College: 18400\xa0(64 Pts)', 'Bachelor of Veterinary Biology / Bachelor of Veterinary Science60': 'Wagga Wagga: 54400\xa0(64 Pts)', 'Diploma in Business61': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 25200\xa0(64 Pts)', 'Diploma in Information Studies62': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 26560\xa0(64 Pts)', 'Doctor of Health Science63': 'Uni Wide: 29600\xa0(64 Pts)', 'Doctor of Law Enforcement and Security64': 'Manly: 24000\xa0(64 Pts)', 'Doctor of Ministry65': 'Uni Wide: 22400\xa0(64 Pts)', 'Doctor of Ministry (Extended)66': 'Uni Wide: 22400\xa0(64 Pts)', 'Doctor of Philosophy (Art - By Publication)67': 'Uni Wide: 25600\xa0(64 Pts)', 'Doctor of Philosophy (Art - Extended)68': 'Uni Wide: 25600\xa0(64 Pts)', 'Doctor of Philosophy (Art)69': 'Uni Wide: 25600\xa0(64 Pts)', 'Doctor of Philosophy (Arts - By Publication)70': 'Uni Wide: 24800\xa0(64 Pts)', 'Doctor of Philosophy (Arts - Extended)71': 'Uni Wide: 24800\xa0(64 Pts)', 'Doctor of Philosophy (Arts)72': 'Uni Wide: 25600\xa0(64 Pts)', 'Doctor of Philosophy (Business - By Publication)73': 'Uni Wide: 29600\xa0(64 Pts)', 'Doctor of Philosophy (Business - Extended)74': 'Uni Wide: 29600\xa0(64 Pts)', 'Doctor of Philosophy (Business)75': 'Uni Wide: 29600\xa0(64 Pts)', 'Doctor of Philosophy (Education - By Publication)76': 'Uni Wide: 24800\xa0(64 Pts)', 'Doctor of Philosophy (Education - Extended)77': 'Uni Wide: 24800\xa0(64 Pts)', 'Doctor of Philosophy (Education)78': 'Uni Wide: 24800\xa0(64 Pts)', 'Doctor of Philosophy (Psychology)79': 'Uni Wide: 26400\xa0(64 Pts)', 'Doctor of Philosophy (Science - By Publication)80': 'Uni Wide: 29600\xa0(64 Pts)', 'Doctor of Philosophy (Science - Lab Based Extended)81': 'Uni Wide: 32000\xa0(64 Pts)', 'Doctor of Philosophy (Science - Lab Based)82': 'Uni Wide: 32000\xa0(64 Pts)', 'Doctor of Philosophy (Science - Non Lab Based Extended)83': 'Uni Wide: 29600\xa0(64 Pts)', 'Doctor of Philosophy (Science - Non Lab Based)84': 'Uni Wide: 29600\xa0(64 Pts)', 'Doctor of Sustainable Agriculture85': 'Uni Wide: 29600\xa0(64 Pts)', 'Graduate Certificate in Customs Administration86': 'Port Macquarie: 9600\xa0(32 Pts)', 'Graduate Certificate in Sustainable Agriculture87': 'Orange: 14400\xa0(32 Pts)', 'Graduate Diploma of Accounting88': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 28560\xa0(64 Pts)', 'Graduate Diploma of Commerce89': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 28560\xa0(64 Pts)', 'Graduate Diploma of Customs Administration90': 'Port Macquarie: 19200\xa0(64 Pts)', 'Graduate Diploma of Information Technology91': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 29680\xa0(64 Pts)', 'Graduate Diploma of Sustainable Agriculture92': 'Orange: 28800\xa0(64 Pts)', 'Graduate Diploma of Theology93': 'Canberra, United Theological College: 18400\xa0(64 Pts)', 'Master of Animal Science94': 'Wagga Wagga: 28800\xa0(64 Pts)', 'Master of Business Administration (with specialisations)95': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 28560\xa0(64 Pts)', 'Master of Commerce (with specialisations)96': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 28560\xa0(64 Pts)', 'Master of Customs Administration97': 'Port Macquarie: 19200\xa0(64 Pts)', 'Master of Information Technology (with specialisations)98': 'Port Macquarie: 20100\xa0(48 Pts)', 'Master of Information Technology (with specialisations)99': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 29680\xa0(64 Pts)', 'Master of Medical Radiation Science100': 'Wagga Waggaf: 28800\xa0(64 Pts)', 'Master of Ministry101': 'Canberra, United Theological College: 18400\xa0(64 Pts)', 'Master of Philosophy (Lab Based)102': 'Uni Wide: 32000\xa0(64 Pts)', 'Master of Philosophy (Non Lab Based)103': 'Uni Wide: 29600\xa0(64 Pts)', 'Master of Professional Accounting104': ': 20100\xa0(48 Pts)', 'Master of Professional Accounting105': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 28560\xa0(64 Pts)', 'Master of Sustainable Agriculture106': 'Orange: 28800\xa0(64 Pts)', 'Master of Terrorism and Security Studies107': 'Canberra: 19200\xa0(64 Pts)', 'Master of Theology108': 'Canberra, United Theological College: 18400\xa0(64 Pts)', 'Master of Theology (Research)109': 'Uni Wide: 19200\xa0(64 Pts)'}


    def parse(self, response):
        # links = response.xpath(
        #     "//div[@id='all-courses-list']/ul/li[@data-level='all undergraduate'][@data-mode='all dom-on_campus dom-online int-on_campus dom-online']/a[contains(text(), 'Bachelor of')]/@href|"
        #     "//div[@id='all-courses-list']/ul/li[@data-level='all undergraduate'][@data-mode='all dom-on_campus int-on_campus']/a[contains(text(), 'Bachelor of')]/@href|"
        #     "//div[@id='all-courses-list']/ul/li[@data-level='all undergraduate'][@data-mode='all dom-online int-on_campus dom-online']/a[contains(text(), 'Bachelor of')]/@href|"
        #     "//div[@id='all-courses-list']/ul/li[@data-level='all undergraduate'][@data-mode='all dom-on_campus dom-online int-on_campus']/a[contains(text(), 'Bachelor of')]/@href").extract()
        links = response.xpath("//a[contains(text(), 'Bachelor of')]/@href").extract()
        # 组合字典
        programme_dict = {}
        # programme_list = response.xpath(
        #     "//div[@id='all-courses-list']/ul/li[@data-level='all undergraduate'][@data-mode='all dom-on_campus dom-online int-on_campus dom-online']/a[contains(text(), 'Bachelor of')]//text()|"
        #     "//div[@id='all-courses-list']/ul/li[@data-level='all undergraduate'][@data-mode='all dom-on_campus int-on_campus']/a[contains(text(), 'Bachelor of')]//text()|"
        #     "//div[@id='all-courses-list']/ul/li[@data-level='all undergraduate'][@data-mode='all dom-online int-on_campus dom-online']/a[contains(text(), 'Bachelor of')]//text()|"
        #     "//div[@id='all-courses-list']/ul/li[@data-level='all undergraduate'][@data-mode='all dom-on_campus dom-online int-on_campus']/a[contains(text(), 'Bachelor of')]//text()").extract()
        programme_list = response.xpath("//a[contains(text(), 'Bachelor of')]//text()").extract()

        for link in range(len(links)):
            url = links[link]
            programme_dict[url] = programme_list[link]

        # # 过滤链接
        # for li1 in range(len(links)):
        #     if "graduate" in links[li1]:
        #         links[li1] = ""
        # print(programme_dict)
        links = ["https://futurestudents.csu.edu.au/courses/business/agribusiness",
"https://futurestudents.csu.edu.au/courses/agricultural-wine-sciences/bachelor-agricultural-science",
"https://futurestudents.csu.edu.au/courses/agricultural-wine-sciences/bachelor-agriculture",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science-general-studies",
"https://futurestudents.csu.edu.au/courses/agricultural-wine-sciences/bachelor-horticulture",
"https://futurestudents.csu.edu.au/courses/agricultural-wine-sciences/bachelor-viticulture",
"https://futurestudents.csu.edu.au/courses/agricultural-wine-sciences/bachelor-wine-business",
"https://futurestudents.csu.edu.au/courses/agricultural-wine-sciences/bachelor-wine-science",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science-honours",
"https://futurestudents.csu.edu.au/courses/medical-science/bachelor-clinical-science",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science-general-studies",
"https://futurestudents.csu.edu.au/courses/allied-health-pharmacy/bachelor-health-rehabilitation-science",
"https://futurestudents.csu.edu.au/courses/allied-health-pharmacy/bachelor-health-science-food-nutrition",
"https://futurestudents.csu.edu.au/courses/allied-health-pharmacy/bachelor-health-science-mental-health",
"https://futurestudents.csu.edu.au/courses/medical-science/bachelor-medical-radiation-science",
"https://futurestudents.csu.edu.au/courses/medical-science/bachelor-medical-science",
"https://futurestudents.csu.edu.au/courses/allied-health-pharmacy/bachelor-nursing-graduate-diploma-clinical-practice-paramedic",
"https://futurestudents.csu.edu.au/courses/allied-health-pharmacy/bachelor-occupational-therapy",
"https://futurestudents.csu.edu.au/courses/allied-health-pharmacy/bachelor-paramedicine",
"https://futurestudents.csu.edu.au/courses/allied-health-pharmacy/bachelor-pharmacy",
"https://futurestudents.csu.edu.au/courses/allied-health-pharmacy/bachelor-physiotherapy",
"https://futurestudents.csu.edu.au/courses/allied-health-pharmacy/bachelor-podiatric-medicine",
"https://futurestudents.csu.edu.au/courses/allied-health-pharmacy/bachelor-speech-language-pathology",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science-honours",
"https://futurestudents.csu.edu.au/courses/animal-vet-sciences/bachelor-animal-science",
"https://futurestudents.csu.edu.au/courses/animal-vet-sciences/bachelor-equine-science",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science-general-studies",
"https://futurestudents.csu.edu.au/courses/animal-vet-sciences/bachelor-veterinary-biology-bachelor-veterinary-science",
"https://futurestudents.csu.edu.au/courses/animal-vet-sciences/bachelor-veterinary-technology",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science-honours",
"https://futurestudents.csu.edu.au/courses/business/bachelor-accounting",
"https://futurestudents.csu.edu.au/courses/business/agribusiness",
"https://futurestudents.csu.edu.au/courses/business/bachelor-business-finance",
"https://futurestudents.csu.edu.au/courses/business/bachelor-business-human-resource-management",
"https://futurestudents.csu.edu.au/courses/business/bachelor-business-insurance",
"https://futurestudents.csu.edu.au/courses/business/bachelor-business-management",
"https://futurestudents.csu.edu.au/courses/business/bachelor-business-marketing",
"https://futurestudents.csu.edu.au/courses/business/bachelor-business-studies",
"https://futurestudents.csu.edu.au/courses/business/bachelor-communication-advertising-bachelor-business-marketing",
"https://futurestudents.csu.edu.au/courses/business/bachelor-communication-public-relations-bachelor-business-studies",
"https://futurestudents.csu.edu.au/courses/business/bachelor-business-honours",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-communication",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-communication-advertising-public-relations",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-communication-advertising",
"https://futurestudents.csu.edu.au/courses/business/bachelor-communication-advertising-bachelor-business-marketing",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-communication-digital-media-production",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-communication-journalism-international-studies",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-communication-journalism",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-communication-public-relations",
"https://futurestudents.csu.edu.au/courses/business/bachelor-communication-public-relations-bachelor-business-studies",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-communication-radio",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-creative-industries-acting-performance-interdisciplinary-innovation",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-creative-industries-acting-performance",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-creative-industries-design-visual-arts-interdisciplinary-innovation",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-creative-industries-design-visual-arts",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-creative-industries-interdisciplinary-innovation",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-creative-industries-screen-media-interdisciplinary-innovation",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-creative-industries-screen-media",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-creative-industries-visualisation-interactivity-interdisciplinary-innovation",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-creative-industries-visualisation-interactivity",
"https://futurestudents.csu.edu.au/courses/exercise-sport-science/bachelor-sports-media",
"https://futurestudents.csu.edu.au/courses/communication-creative/bachelor-theatre-media",
"https://futurestudents.csu.edu.au/courses/engineering/bachelor-technology-master-engineering-civil-systems",
"https://futurestudents.csu.edu.au/courses/environmental-outdoor/bachelor-applied-science-outdoor-recreation-ecotourism",
"https://futurestudents.csu.edu.au/courses/environmental-outdoor/bachelor-applied-science-parks-recreation-heritage",
"https://futurestudents.csu.edu.au/courses/environmental-outdoor/bachelor-environmental-science",
"https://futurestudents.csu.edu.au/courses/environmental-outdoor/bachelor-environmental-science-management",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science-general-studies",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science-honours",
"https://futurestudents.csu.edu.au/courses/teaching-education/bachelor-education-health-pe",
"https://futurestudents.csu.edu.au/courses/exercise-sport-science/bachelor-exercise-sport-science",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science-general-studies",
"https://futurestudents.csu.edu.au/courses/exercise-sport-science/bachelor-sports-media",
"https://futurestudents.csu.edu.au/courses/exercise-sport-science/bachelor-exercise-science-honours",
"https://futurestudents.csu.edu.au/courses/humanities-social-sciences/bachelor-arts",
"https://futurestudents.csu.edu.au/courses/humanities-social-sciences/bachelor-human-services",
"https://futurestudents.csu.edu.au/courses/humanities-social-sciences/bachelor-liberal-studies-arts",
"https://futurestudents.csu.edu.au/courses/humanities-social-sciences/bachelor-social-work",
"https://futurestudents.csu.edu.au/courses/police-security-emergency/bachelor-criminal-justice-honours",
"https://futurestudents.csu.edu.au/courses/technology-computing-maths/bachelor-computer-science",
"https://futurestudents.csu.edu.au/courses/teaching-education/bachelor-education-k12",
"https://futurestudents.csu.edu.au/courses/teaching-education/bachelor-educational-studies",
"https://futurestudents.csu.edu.au/courses/technology-computing-maths/bachelor-information-technology",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science",
"https://futurestudents.csu.edu.au/courses/technology-computing-maths/bachelor-computing-honours",
"https://futurestudents.csu.edu.au/courses/library-information-studies/bachelor-information-studies",
"https://futurestudents.csu.edu.au/courses/medical-science/bachelor-clinical-science",
"https://futurestudents.csu.edu.au/courses/medical-science/bachelor-dental-science",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science-general-studies",
"https://futurestudents.csu.edu.au/courses/medical-science/bachelor-medical-radiation-science",
"https://futurestudents.csu.edu.au/courses/medical-science/bachelor-medical-science",
"https://futurestudents.csu.edu.au/courses/medical-science/bachelor-oral-health-therapy-hygiene",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science-honours",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science-general-studies",
"https://futurestudents.csu.edu.au/courses/allied-health-pharmacy/bachelor-health-science-mental-health",
"https://futurestudents.csu.edu.au/courses/nursing-midwifery-indigenous/bachelor-nursing",
"https://futurestudents.csu.edu.au/courses/allied-health-pharmacy/bachelor-nursing-graduate-diploma-clinical-practice-paramedic",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science-honours",
"https://futurestudents.csu.edu.au/courses/police-security-emergency/bachelor-border-management",
"https://futurestudents.csu.edu.au/courses/police-security-emergency/bachelor-criminal-justice",
"https://futurestudents.csu.edu.au/courses/police-security-emergency/bachelor-emergency-management",
"https://futurestudents.csu.edu.au/courses/police-security-emergency/bachelor-laws",
"https://futurestudents.csu.edu.au/courses/police-security-emergency/bachelor-laws-bachelor-criminal-justice",
"https://futurestudents.csu.edu.au/courses/police-security-emergency/bachelor-policing",
"https://futurestudents.csu.edu.au/courses/police-security-emergency/bachelor-policing-investigations",
"https://futurestudents.csu.edu.au/courses/police-security-emergency/bachelor-public-safety-security",
"https://futurestudents.csu.edu.au/courses/police-security-emergency/bachelor-criminal-justice-honours",
"https://futurestudents.csu.edu.au/courses/psychology/bachelor-psychology",
"https://futurestudents.csu.edu.au/courses/psychology/bachelor-social-science-psychology",
"https://futurestudents.csu.edu.au/courses/psychology/bachelor-social-science-psychology-honours",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science-general-studies",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science",
"https://futurestudents.csu.edu.au/courses/science/bachelor-science-honours",
"https://futurestudents.csu.edu.au/courses/teaching-education/bachelor-adult-vocational-education",
"https://futurestudents.csu.edu.au/courses/teaching-education/bachelor-education-birth-to-five-years",
"https://futurestudents.csu.edu.au/courses/teaching-education/bachelor-early-childhood-primary",
"https://futurestudents.csu.edu.au/courses/teaching-education/bachelor-education-health-pe",
"https://futurestudents.csu.edu.au/courses/teaching-education/bachelor-education-k12",
"https://futurestudents.csu.edu.au/courses/teaching-education/bachelor-education-secondary-industry-entry",
"https://futurestudents.csu.edu.au/courses/teaching-education/bachelor-education-technology-applied-studies",
"https://futurestudents.csu.edu.au/courses/teaching-education/bachelor-educational-studies",
"https://futurestudents.csu.edu.au/courses/teaching-education/bachelor-outdoor-education",
"https://futurestudents.csu.edu.au/courses/teaching-education/bachelor-teaching-primary",
"https://futurestudents.csu.edu.au/courses/teaching-education/bachelor-teaching-secondary",
"https://futurestudents.csu.edu.au/courses/theology-religious-studies/bachelor-islamic-studies",
"https://futurestudents.csu.edu.au/courses/theology-religious-studies/bachelor-theology",
"https://futurestudents.csu.edu.au/courses/theology-religious-studies/bachelor-islamic-studies-honours",
"https://futurestudents.csu.edu.au/courses/theology-religious-studies/bachelor-theology-honours", ]
#         links = ["http://futurestudents.csu.edu.au/courses/communication-creative/bachelor-communication-theatre-media",
# "http://futurestudents.csu.edu.au/courses/communication-creative/bachelor-communication-media-practice",]
        clear_space(links)
        print(len(links))
        links = list(set(links))
        print(len(links))

        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "Charles Sturt University"
        # item['country'] = 'Australia'
        # item['website'] = 'http://futurestudents.csu.edu.au'
        item['url'] = response.url
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        item['major_type1'] = response.meta.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        driver = webdriver.Chrome(r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Lib\site-packages\selenium\chromedriver (2).exe")
        driver.implicitly_wait(30)  # 隐式等待
        driver.get(response.url)
        import time
        # time.sleep(30)

        try:
            locator = (By.ID, 'cYear-campus')
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
            location = driver.find_element_by_xpath(r"//div[@id='cYear-campus']").text
            print("location: ", location)
            # location = response.xpath(
            #     "//div[@id='locations1']//div[@class='section no-padding-top']//div[@class='card card-content z-depth-0']//div[@class='is-domestic']//text()|"
            #     "//div[@id='fYear-campus']//text()").extract()
            # clear_space(location)
            item['location'] = location
            print("item['location']: ", item['location'])

            programme = response.xpath(
                "//h1[@class='logo-font csu-slogan course course-name']//text()").extract()
            clear_space(programme)
            programme = ''.join(programme).replace("(with specialisations)", "").replace("  ", "").strip()
            item['degree_name'] = programme
            key_fee = item['degree_name']
            print("item['degree_name']: ", item['degree_name'])

            programme_re = re.findall(r"\(.+\)", item['degree_name'].replace("(Honours)", ""))
            if len(programme_re) > 0:
                item['programme_en'] = ''.join(programme_re).replace("(", "").replace(")", "").strip()
                item['degree_name'] = item['degree_name'].replace(''.join(programme_re), "").strip()
            else:
                item['programme_en'] = programme.replace("Bachelor of", "").strip()
            print("item['programme_en']: ", item['programme_en'])
            print("***item['degree_name']: ", item['degree_name'])

            count_un = re.findall(r"Bachelor", item['degree_name'])
            print("count_un: ", count_un)
            if len(count_un) < 2:
                degree_overview_en = response.xpath(
                    "//div[@id='course-full']/preceding-sibling::p").extract()
                item['overview_en'] = item['degree_overview_en'] = remove_class(clear_lianxu_space(degree_overview_en))
                print("item['degree_overview_en']: ", item['degree_overview_en'])

                locator = (By.CLASS_NAME, 'sectionHead')
                WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
                duration = driver.find_element_by_xpath(r"//div[@id='cYear-duration']").text
                # duration = response.xpath(
                #     "//div[@id='ocbDuration']//text()").extract()
                # clear_space(duration)
                # item['duration'] = ','.join(duration).replace(",,", ",").replace(":,", ":").replace(",:", ":").strip().strip(",").strip()
                item['duration'] = duration
                print("item['duration']: ", item['duration'])


                start_date = driver.find_element_by_xpath(r"//div[@id='cYear-sessions']").text
                # start_date = response.xpath(
                #     "//div[@id='sessDatesKI']/span/text() | //div[@id='sessDateDom']/span/text()").extract()
                # clear_space(start_date)
                # print("start_date: ", start_date)
                # if len(start_date) > 0:
                #     start_date_str = start_date[0].strip()
                #     if ";" in start_date_str:
                #         start_date_list = start_date_str.split(";")
                #         st_l = []
                #         for s in start_date_list:
                #             s1 = s.replace("2018", "").replace("2019", "").replace("0", "").strip()
                #             st_l.append(s1)
                #         st_l = list(set(st_l))
                #         item['start_date'] = ','.join(st_l).strip().strip(",").strip()
                #     else:
                #         item['start_date'] = start_date_str.replace("2018", "").replace("2019", "").replace("0", "").strip()
                item['start_date'] = start_date
                print("item['start_date']: ", item['start_date'])

                career = response.xpath(
                    "//div[@class='hasCareerOpps']|//div[@class='section isPostGrad isHDR']").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career))
                print("item['career_en']: ", item['career_en'])

                # 显示等待，出现id为subject-div的元素结束等待
                locator = (By.ID, 'subject-div')
                WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located(locator))
                # //div[@id='testimonial-area']/following-sibling::div[1]
                modules = driver.find_element_by_xpath(r"//div[@id='subject-div']").get_attribute('innerHTML')
                # modules = response.xpath(
                #     "//div[@id='subject-intro']").extract()
                item['modules_en'] = remove_class(modules)
                # print("item['modules_en']: ", item['modules_en'])

                rntry_requirements_en = driver.find_element_by_xpath(r"//div[@id='detailCardTeam1']").get_attribute('innerHTML')
                # rntry_requirements_en = response.xpath(
                #     "//h3[contains(text(),'Entry requirements')]/..").extract()
                item['rntry_requirements_en'] = remove_class(rntry_requirements_en)
                # print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

                ielts_desc_dict = {"Associate Degree in Policing Practice": "A minimum overall Academic IELTS score of 7.0 with no score below a 7.0 in each of the individual skill areas or a qualification deemed equivalent.",
    "Bachelor of Medical Radiation Science": "A minimum overall Academic IELTS score of 6.5 with no score below a 6.0 in each of the individual skill areas or a qualification deemed equivalent.",
    "Bachelor of Theology": "A minimum overall Academic IELTS score of 6.5 with no score below a 6.0 in each of the individual skill areas or a qualification deemed equivalent.",
    "Bachelor of Health and Rehabilitation Science": "A minimum overall Academic IELTS score IELTS of 6.5 with no score below a 6.5 in each of the individual skill areas or a qualification deemed equivalent.",
    "Bachelor of Occupational Therapy": "A minimum overall Academic IELTS score IELTS of 6.5 with no score below a 6.5 in each of the individual skill areas or a qualification deemed equivalent.",
    "Bachelor of Physiotherapy": "A minimum overall Academic IELTS score IELTS of 6.5 with no score below a 6.5 in each of the individual skill areas or a qualification deemed equivalent.",
    "Bachelor of Podiatric Medicine": "A minimum overall Academic IELTS score IELTS of 6.5 with no score below a 6.5 in each of the individual skill areas or a qualification deemed equivalent.",
    "Bachelor of Clinical Practice (Paramedic)": "A minimum overall Academic IELTS score of 7.0 with no score below a 6.5 in each of the individual skill areas or a qualification deemed equivalent.",
    "Bachelor of Dental Science": "A minimum overall Academic IELTS score of 7.0 with no score below a 6.5 in each of the individual skill areas or a qualification deemed equivalent.",
    "Bachelor of Pharmacy": "A minimum overall Academic IELTS score of 7.0 with no score below a 6.5 in each of the individual skill areas or a qualification deemed equivalent.",
    "Bachelor of Oral Health (Therapy / Hygiene)": "A minimum overall Academic IELTS score of 7.0 with no score below a 6.5 in each of the individual skill areas or a qualification deemed equivalent.",
    "Bachelor of Speech and Language Pathology": "A minimum overall Academic IELTS score of 7.0 with no score below a 6.5 in each of the individual skill areas or a qualification deemed equivalent.",
    "Bachelor of Education (Birth to Five)": "A minimum overall Academic IELTS score of 7.5 (with no score below 7 in reading and writing, and a score of no less than 8 in speaking and listening) or a qualification deemed equivalent. Testing results must be obtained within two years from the date of your application for admission.",
    "Bachelor of Education (Early Childhood and Primary)": "A minimum overall Academic IELTS score of 7.5 (with no score below 7 in reading and writing, and a score of no less than 8 in speaking and listening) or a qualification deemed equivalent. Testing results must be obtained within two years from the date of your application for admission.",
    "Bachelor of Education (Health and Physical Education)": "A minimum overall Academic IELTS score of 7.5 (with no score below 7 in reading and writing, and a score of no less than 8 in speaking and listening) or a qualification deemed equivalent. Testing results must be obtained within two years from the date of your application for admission.",
    "Bachelor of Education (K-12)": "A minimum overall Academic IELTS score of 7.5 (with no score below 7 in reading and writing, and a score of no less than 8 in speaking and listening) or a qualification deemed equivalent. Testing results must be obtained within two years from the date of your application for admission.",
    "Bachelor of Education (Secondary) - Industry entry": "A minimum overall Academic IELTS score of 7.5 (with no score below 7 in reading and writing, and a score of no less than 8 in speaking and listening) or a qualification deemed equivalent. Testing results must be obtained within two years from the date of your application for admission.",
    "Bachelor of Education (Technology and Applied Studies)": "A minimum overall Academic IELTS score of 7.5 (with no score below 7 in reading and writing, and a score of no less than 8 in speaking and listening) or a qualification deemed equivalent. Testing results must be obtained within two years from the date of your application for admission.",
    "Bachelor of Teaching (Primary)": "A minimum overall Academic IELTS score of 7.5 (with no score below 7 in reading and writing, and a score of no less than 8 in speaking and listening) or a qualification deemed equivalent. Testing results must be obtained within two years from the date of your application for admission.",
    "Bachelor of Teaching (Secondary)": "A minimum overall Academic IELTS score of 7.5 (with no score below 7 in reading and writing, and a score of no less than 8 in speaking and listening) or a qualification deemed equivalent. Testing results must be obtained within two years from the date of your application for admission.",
    "Bachelor of Nursing":"An Academic IELTS with a minimum overall score of 7 and with no score below 7 in each of the individual skill areas or a qualification deemed equivalent.",
    "Bachelor of Nursing - Graduate Diploma of Clinical Practice (Paramedic)":"An Academic IELTS with a minimum overall score of 7 and with no score below 7 in each of the individual skill areas or a qualification deemed equivalent.",}
                item['ielts_desc'] = ielts_desc_dict.get(key_fee)
                print("item['ielts_desc']: ", item['ielts_desc'])

                driver.quit()
                if item['ielts_desc'] is not None:
                    ielts_d = get_ielts(item['ielts_desc'])
                    item["ielts"] = ielts_d.get('IELTS')
                    item["ielts_l"] = ielts_d.get('IELTS_L')
                    item["ielts_s"] = ielts_d.get('IELTS_S')
                    item["ielts_r"] = ielts_d.get('IELTS_R')
                    item["ielts_w"] = ielts_d.get('IELTS_W')
                # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

                department = response.xpath(
                    "//html//nav[@class='breadcrumb-wrapper']//a[3]//text()").extract()
                clear_space(department)
                item['department'] = ' '.join(department).strip()
                print("item['department']: ", item['department'])

                apply_desc_en = response.xpath(
                    "//div[@id='international-app']").extract()
                item['apply_desc_en'] = remove_class(clear_lianxu_space(apply_desc_en))
                print("item['apply_desc_en']: ", item['apply_desc_en'])

                deadline = response.xpath(
                    "//div[@class='card']//div[@class='card very-small-international-lower']//text()").extract()
                clear_space(deadline)
                print("deadline: ", deadline)
                deadline_str = ""
                if "Important dates" in deadline:
                    d = deadline.index("Important dates")
                    deadline_str += ''.join(deadline[d+1:d+2]) + " "
                item['deadline'] = getStartDate(deadline_str.strip())
                print("item['deadline']: ", item['deadline'])

                feeDict = {}
                zhuanye = ["Bachelor of Accounting",
"Bachelor of Accounting",
"Bachelor of Agricultural Business Management",
"Bachelor of Agricultural Science",
"Bachelor of Animal Science",
"Bachelor of Applied Science (Outdoor Recreation and Ecotourism)",
"Bachelor of Applied Science (Parks Recreation and Heritage)",
"Bachelor of Arts",
"Bachelor of Business (Human Resource Management)",
"Bachelor of Business (Management)",
"Bachelor of Business (Management)",
"Bachelor of Business (Marketing)",
"Bachelor of Business (Marketing)",
"Bachelor of Business Studies",
"Bachelor of Business Studies",
"Bachelor of Clinical Science",
"Bachelor of Communication (Advertising)",
"Bachelor of Communication (Journalism)",
"Bachelor of Communication (Public Relations)",
"Bachelor of Communication (Theatre Media)",
"Bachelor of Computer Science (with specialisation)",
"Bachelor of Computing (Honours)",
"Bachelor of Creative Arts and Design (Animation and Visual Effects)",
"Bachelor of Creative Arts and Design (Graphic Design / Photography)",
"Bachelor of Creative Arts and Design (Graphic Design)",
"Bachelor of Creative Arts and Design (Photography)",
"Bachelor of Criminal Justice",
"Bachelor of Criminal Justice (Honours)",
"Bachelor of Dental Science",
"Bachelor of Education (Early Childhood and Primary)",
"Bachelor of Education (Health and Physical Education)",
"Bachelor of Education (K - 12)",
"Bachelor of Education (Technology and Applied Studies)",
"Bachelor of Environmental Science and Management",
"Bachelor of Equine Science (with specialisation)",
"Bachelor of Exercise and Sport Science",
"Bachelor of Exercise Science (Honours)",
"Bachelor of Health and Rehabilitation Science",
"Bachelor of Information Technology (with specialisations)",
"Bachelor of Information Technology (with specialisations)",
"Bachelor of Medical Radiation Science",
"Bachelor of Medical Science",
"Bachelor of Nursing",
"Bachelor of Occupational Therapy",
"Bachelor of Oral Health (Therapy - Hygiene)",
"Bachelor of Paramedicine",
"Bachelor of Pharmacy",
"Bachelor of Physiotherapy",
"Bachelor of Podiatric Medicine",
"Bachelor of Psychology",
"Bachelor of Science",
"Bachelor of Science (Honours)",
"Bachelor of Social Science (Psychology)",
"Bachelor of Social Science (Psychology) / Bachelor of Business (Management)",
"Bachelor of Social Science (Psychology) / Bachelor of Business (Marketing)",
"Bachelor of Social Work",
"Bachelor of Speech and Language Pathology",
"Bachelor of Stage and Screen (Television)",
"Bachelor of Theology",
"Bachelor of Theology (Honours)",
"Bachelor of Veterinary Biology / Bachelor of Veterinary Science", ]
                loco = ["Albury-Wodonga, Bathurst, Port Macquarie, Wagga Wagga",
"CSU Study Centre Melbourne, CSU Study Centre Sydney",
"Wagga Wagga",
"Wagga Wagga",
"Wagga Wagga",
"Albury-Wodonga, Port Macquarie",
"Albury-Wodonga, Port Macquarie",
"Bathurst, Wagga Wagga",
"CSU Study Centre Melbourne, CSU Study Centre Sydney",
"Albury-Wodonga, Bathurst, Wagga Wagga",
"CSU Study Centre Melbourne, CSU Study Centre Sydney",
"Albury-Wodonga, Bathurst",
"CSU Study Centre Melbourne, CSU Study Centre Sydney",
"Albury-Wodonga, Bathurst, Port Macquarie, Wagga Wagga",
"CSU Study Centre Melbourne, CSU Study Centre Sydney",
"Orange",
"Bathurst, Port Macquarie",
"Bathurst",
"Bathurst, Port Macquarie",
"Bathurst",
"Bathurst",
"Albury-Wodonga, Bathurst, Wagga Wagga",
"Wagga Wagga",
"Wagga Wagga",
"Port Macquarie",
"Wagga Wagga",
"Bathurst, Port Macquarie",
"Bathurst",
"Orange",
"Albury-Wodonga, Bathurst, Wagga Wagga",
"Bathurst",
"Albury-Wodonga, Bathurst, Wagga Wagga",
"Wagga Wagga",
"Albury-Wodonga, Port Macquarie",
"Wagga Wagga",
"Bathurst, Port Macquarie",
"Bathurst",
"Albury-Wodonga",
"Albury-Wodonga, Wagga Wagga",
"CSU Study Centre Melbourne, CSU Study Centre Sydney",
"Port Macquarie, Wagga Wagga",
"Wagga Wagga",
"Albury-Wodonga, Bathurst, Wagga Wagga",
"Albury-Wodonga, Port Macquarie",
"Wagga Wagga",
"Bathurst, Port Macquarie",
"Orange",
"Albury-Wodonga, Orange",
"Albury-Wodonga",
"Bathurst, Port Macquarie",
"Wagga Wagga",
"Albury-Wodonga, Orange, Wagga Wagga",
"Port Macquarie, Wagga Wagga",
"Bathurst",
"Bathurst",
"Port Macquarie, Wagga Wagga",
"Albury-Wodonga",
"Wagga Wagga",
"Canberra, United Theological College",
"Canberra, United Theological College",
"Wagga Wagga",]
                fee = ["23600",
"25200",
"28800",
"28800",
"28800",
"28800",
"28800",
"19200",
"25200",
"23600",
"25200",
"23600",
"25200",
"23600",
"25200",
"28800",
"23200",
"23200",
"21600",
"23200",
"23600",
"23600",
"22400",
"22400",
"22400",
"22400",
"21600",
"21600",
"54400",
"22080",
"22080",
"22080",
"22080",
"28800",
"28800",
"28800",
"28800",
"28800",
"23600",
"26560",
"29600",
"28800",
"27200",
"28800",
"34400",
"28800",
"28800",
"31200",
"28800",
"24000",
"28800",
"28800",
"24000",
"24000",
"24000",
"24160",
"28800",
"22400",
"18400",
"18400",
"54400", ]
                for i in range(len(zhuanye)):
                    feeDict[zhuanye[i]] = loco[i] + ":" + fee[i]
                item['tuition_fee'] = feeDict.get(key_fee.replace("(12 subjects)", "").replace("(16 subjects)", "").strip())
                print("item['tuition_fee']: ", item['tuition_fee'])

                online = response.xpath("//h2[contains(text(),'Study mode')]/following-sibling::*//text()").extract()
                clear_space(online)
                print("online: ", online)
                if ''.join(online).strip() != "Online":
                    major_list = response.xpath(
                        "//div[@id='fYear-specialisation']/ul[1]/li//text()|"
                        "//div[@id='fYear-specialisation']/h3//text()|"
                        "//div[@id='fYear-specialisation']/h6//text()").extract()
                    clear_space(major_list)
                    print("major_list: ", major_list)
                    print(len(major_list))

                    if len(major_list) == 0:
                        yield item
                    else:
                        for m in range(len(major_list)):
                            item['programme_en'] = major_list[m]
                            # item['modules_en'] = remove_class(clear_lianxu_space([modules_list[m]]))
                            print("item['programme_en']: ", item['programme_en'])
                            yield item
        except Exception as e:
            with open("scrapySchool_Australian_ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

