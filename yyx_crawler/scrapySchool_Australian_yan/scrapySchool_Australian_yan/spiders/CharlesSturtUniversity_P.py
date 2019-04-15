# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_Australian_yan.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_yan.getItem import get_item
from scrapySchool_Australian_yan.getTuition_fee import getTuition_fee
from scrapySchool_Australian_yan.items import ScrapyschoolAustralianYanItem
from scrapySchool_Australian_yan.remove_tags import remove_class
from scrapySchool_Australian_yan.getStartDate import getStartDate
from scrapySchool_Australian_yan.getDuration import getIntDuration
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CharlesSturtUniversity_PSpider(scrapy.Spider):
    name = "CharlesSturtUniversity_P"
    # start_urls = ["http://futurestudents.csu.edu.au/courses/postgraduate"]
    # 2019.03.18 星期一
    start_urls = ["https://futurestudents.csu.edu.au/courses/all?level=postgraduate&mode=int-on_campus"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    # feeDict = {'Bachelor of Accounting0': 'Albury-Wodonga, Bathurst, Port Macquarie, Wagga Wagga: 23600\xa0(64 Pts)', 'Bachelor of Accounting1': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 25200\xa0(64 Pts)', 'Bachelor of Agricultural Business Management2': 'Wagga Wagga: 28800\xa0(64 Pts)', 'Bachelor of Agricultural Science3': 'Wagga Wagga: 28800\xa0(64 Pts)', 'Bachelor of Animal Science4': 'Wagga Wagga: 28800\xa0(64 Pts)', 'Bachelor of Applied Science (Outdoor Recreation and Ecotourism)5': 'Albury-Wodonga, Port Macquarie: 28800\xa0(64 Pts)', 'Bachelor of Applied Science (Parks Recreation and Heritage)6': 'Albury-Wodonga, Port Macquarie: 28800\xa0(64 Pts)', 'Bachelor of Arts7': 'Bathurst, Wagga Wagga: 19200\xa0(64 Pts)', 'Bachelor of Business (Human Resource Management)8': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 25200\xa0(64 Pts)', 'Bachelor of Business (Management)9': 'Albury-Wodonga, Bathurst, Wagga Wagga: 23600\xa0(64 Pts)', 'Bachelor of Business (Management)10': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 25200\xa0(64 Pts)', 'Bachelor of Business (Marketing)11': 'Albury-Wodonga, Bathurst: 23600\xa0(64 Pts)', 'Bachelor of Business (Marketing)12': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 25200\xa0(64 Pts)', 'Bachelor of Business Studies13': 'Albury-Wodonga, Bathurst, Port Macquarie, Wagga Wagga: 23600\xa0(64 Pts)', 'Bachelor of Business Studies14': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 25200\xa0(64 Pts)', 'Bachelor of Clinical Science15': 'Orange: 28800\xa0(64 Pts)', 'Bachelor of Communication (Advertising)16': 'Bathurst, Port Macquarie: 23200\xa0(64 Pts)', 'Bachelor of Communication (Journalism)17': 'Bathurst: 23200\xa0(64 Pts)', 'Bachelor of Communication (Public Relations)18': 'Bathurst, Port Macquarie: 21600\xa0(64 Pts)', 'Bachelor of Communication (Theatre Media)19': 'Bathurst: 23200\xa0(64 Pts)', 'Bachelor of Computer Science (with specialisation)20': 'Bathurst: 23600\xa0(64 Pts)', 'Bachelor of Computing (Honours)21': 'Albury-Wodonga, Bathurst, Wagga Wagga: 23600\xa0(64 Pts)', 'Bachelor of Creative Arts and Design (Animation and Visual Effects)22': 'Wagga Wagga: 22400\xa0(64 Pts)', 'Bachelor of Creative Arts and Design (Graphic Design / Photography)23': 'Wagga Wagga: 22400\xa0(64 Pts)', 'Bachelor of Creative Arts and Design (Graphic Design)24': 'Port Macquarie: 22400\xa0(64 Pts)', 'Bachelor of Creative Arts and Design (Photography)25': 'Wagga Wagga: 22400\xa0(64 Pts)', 'Bachelor of Criminal Justice26': 'Bathurst, Port Macquarie: 21600\xa0(64 Pts)', 'Bachelor of Criminal Justice (Honours)27': 'Bathurst: 21600\xa0(64 Pts)', 'Bachelor of Dental Science28': 'Orange: 54400\xa0(64 Pts)', 'Bachelor of Education (Early Childhood and Primary)29': 'Albury-Wodonga, Bathurst, Wagga Wagga: 22080\xa0(64 Pts)', 'Bachelor of Education (Health and Physical Education)30': 'Bathurst: 22080\xa0(64 Pts)', 'Bachelor of Education (K - 12)31': 'Albury-Wodonga, Bathurst, Wagga Wagga: 22080\xa0(64 Pts)', 'Bachelor of Education (Technology and Applied Studies)32': 'Wagga Wagga: 22080\xa0(64 Pts)', 'Bachelor of Environmental Science and Management33': 'Albury-Wodonga, Port Macquarie: 28800\xa0(64 Pts)', 'Bachelor of Equine Science (with specialisation)34': 'Wagga Wagga: 28800\xa0(64 Pts)', 'Bachelor of Exercise and Sport Science35': 'Bathurst, Port Macquarie: 28800\xa0(64 Pts)', 'Bachelor of Exercise Science (Honours)36': 'Bathurst: 28800\xa0(64 Pts)', 'Bachelor of Health and Rehabilitation Science37': 'Albury-Wodonga: 28800\xa0(64 Pts)', 'Bachelor of Information Technology (with specialisations)38': 'Albury-Wodonga, Wagga Wagga: 23600\xa0(64 Pts)', 'Bachelor of Information Technology (with specialisations)39': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 26560\xa0(64 Pts)', 'Bachelor of Medical Radiation Science40': 'Port Macquarie, Wagga Wagga: 29600\xa0(64 Pts)', 'Bachelor of Medical Science41': 'Wagga Wagga: 28800\xa0(64 Pts)', 'Bachelor of Nursing42': 'Albury-Wodonga, Bathurst, Wagga Wagga: 27200\xa0(64 Pts)', 'Bachelor of Occupational Therapy43': 'Albury-Wodonga, Port Macquarie: 28800\xa0(64 Pts)', 'Bachelor of Oral Health (Therapy - Hygiene)44': 'Wagga Wagga: 34400\xa0(64 Pts)', 'Bachelor of Paramedicine45': 'Bathurst, Port Macquarie: 28800\xa0(64 Pts)', 'Bachelor of Pharmacy46': 'Orange: 28800\xa0(64 Pts)', 'Bachelor of Physiotherapy47': 'Albury-Wodonga, Orange: 31200\xa0(64 Pts)', 'Bachelor of Podiatric Medicine48': 'Albury-Wodonga: 28800\xa0(64 Pts)', 'Bachelor of Psychology49': 'Bathurst, Port Macquarie: 24000\xa0(64 Pts)', 'Bachelor of Science50': 'Wagga Wagga: 28800\xa0(64 Pts)', 'Bachelor of Science (Honours)51': 'Albury-Wodonga, Orange, Wagga Wagga: 28800\xa0(64 Pts)', 'Bachelor of Social Science (Psychology)52': 'Port Macquarie, Wagga Wagga: 24000\xa0(64 Pts)', 'Bachelor of Social Science (Psychology) / Bachelor of Business (Management)53': 'Bathurst: 24000\xa0(64 Pts)', 'Bachelor of Social Science (Psychology) / Bachelor of Business (Marketing)54': 'Bathurst: 24000\xa0(64 Pts)', 'Bachelor of Social Work55': 'Port Macquarie, Wagga Wagga: 24160\xa0(64 Pts)', 'Bachelor of Speech and Language Pathology56': 'Albury-Wodonga: 28800\xa0(64 Pts)', 'Bachelor of Stage and Screen (Television)57': 'Wagga Wagga: 22400\xa0(64 Pts)', 'Bachelor of Theology58': 'Canberra, United Theological College: 18400\xa0(64 Pts)', 'Bachelor of Theology (Honours)59': 'Canberra, United Theological College: 18400\xa0(64 Pts)', 'Bachelor of Veterinary Biology / Bachelor of Veterinary Science60': 'Wagga Wagga: 54400\xa0(64 Pts)', 'Diploma in Business61': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 25200\xa0(64 Pts)', 'Diploma in Information Studies62': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 26560\xa0(64 Pts)', 'Doctor of Health Science63': 'Uni Wide: 29600\xa0(64 Pts)', 'Doctor of Law Enforcement and Security64': 'Manly: 24000\xa0(64 Pts)', 'Doctor of Ministry65': 'Uni Wide: 22400\xa0(64 Pts)', 'Doctor of Ministry (Extended)66': 'Uni Wide: 22400\xa0(64 Pts)', 'Doctor of Philosophy (Art - By Publication)67': 'Uni Wide: 25600\xa0(64 Pts)', 'Doctor of Philosophy (Art - Extended)68': 'Uni Wide: 25600\xa0(64 Pts)', 'Doctor of Philosophy (Art)69': 'Uni Wide: 25600\xa0(64 Pts)', 'Doctor of Philosophy (Arts - By Publication)70': 'Uni Wide: 24800\xa0(64 Pts)', 'Doctor of Philosophy (Arts - Extended)71': 'Uni Wide: 24800\xa0(64 Pts)', 'Doctor of Philosophy (Arts)72': 'Uni Wide: 25600\xa0(64 Pts)', 'Doctor of Philosophy (Business - By Publication)73': 'Uni Wide: 29600\xa0(64 Pts)', 'Doctor of Philosophy (Business - Extended)74': 'Uni Wide: 29600\xa0(64 Pts)', 'Doctor of Philosophy (Business)75': 'Uni Wide: 29600\xa0(64 Pts)', 'Doctor of Philosophy (Education - By Publication)76': 'Uni Wide: 24800\xa0(64 Pts)', 'Doctor of Philosophy (Education - Extended)77': 'Uni Wide: 24800\xa0(64 Pts)', 'Doctor of Philosophy (Education)78': 'Uni Wide: 24800\xa0(64 Pts)', 'Doctor of Philosophy (Psychology)79': 'Uni Wide: 26400\xa0(64 Pts)', 'Doctor of Philosophy (Science - By Publication)80': 'Uni Wide: 29600\xa0(64 Pts)', 'Doctor of Philosophy (Science - Lab Based Extended)81': 'Uni Wide: 32000\xa0(64 Pts)', 'Doctor of Philosophy (Science - Lab Based)82': 'Uni Wide: 32000\xa0(64 Pts)', 'Doctor of Philosophy (Science - Non Lab Based Extended)83': 'Uni Wide: 29600\xa0(64 Pts)', 'Doctor of Philosophy (Science - Non Lab Based)84': 'Uni Wide: 29600\xa0(64 Pts)', 'Doctor of Sustainable Agriculture85': 'Uni Wide: 29600\xa0(64 Pts)', 'Graduate Certificate in Customs Administration86': 'Port Macquarie: 9600\xa0(32 Pts)', 'Graduate Certificate in Sustainable Agriculture87': 'Orange: 14400\xa0(32 Pts)', 'Graduate Diploma of Accounting88': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 28560\xa0(64 Pts)', 'Graduate Diploma of Commerce89': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 28560\xa0(64 Pts)', 'Graduate Diploma of Customs Administration90': 'Port Macquarie: 19200\xa0(64 Pts)', 'Graduate Diploma of Information Technology91': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 29680\xa0(64 Pts)', 'Graduate Diploma of Sustainable Agriculture92': 'Orange: 28800\xa0(64 Pts)', 'Graduate Diploma of Theology93': 'Canberra, United Theological College: 18400\xa0(64 Pts)', 'Master of Animal Science94': 'Wagga Wagga: 28800\xa0(64 Pts)', 'Master of Business Administration (with specialisations)95': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 28560\xa0(64 Pts)', 'Master of Commerce (with specialisations)96': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 28560\xa0(64 Pts)', 'Master of Customs Administration97': 'Port Macquarie: 19200\xa0(64 Pts)', 'Master of Information Technology (with specialisations)98': 'Port Macquarie: 20100\xa0(48 Pts)', 'Master of Information Technology (with specialisations)99': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 29680\xa0(64 Pts)', 'Master of Medical Radiation Science100': 'Wagga Waggaf: 28800\xa0(64 Pts)', 'Master of Ministry101': 'Canberra, United Theological College: 18400\xa0(64 Pts)', 'Master of Philosophy (Lab Based)102': 'Uni Wide: 32000\xa0(64 Pts)', 'Master of Philosophy (Non Lab Based)103': 'Uni Wide: 29600\xa0(64 Pts)', 'Master of Professional Accounting104': ': 20100\xa0(48 Pts)', 'Master of Professional Accounting105': 'CSU Study Centre Melbourne, CSU Study Centre Sydney: 28560\xa0(64 Pts)', 'Master of Sustainable Agriculture106': 'Orange: 28800\xa0(64 Pts)', 'Master of Terrorism and Security Studies107': 'Canberra: 19200\xa0(64 Pts)', 'Master of Theology108': 'Canberra, United Theological College: 18400\xa0(64 Pts)', 'Master of Theology (Research)109': 'Uni Wide: 19200\xa0(64 Pts)'}


    def parse(self, response):
        # links = response.xpath(
        #     "//div[@id='all-courses-list']/ul/li[@data-level='all postgraduate'][@data-mode='all dom-on_campus dom-online int-on_campus dom-online']/a[contains(text(), 'Master of')]/@href|"
        #     "//div[@id='all-courses-list']/ul/li[@data-level='all postgraduate'][@data-mode='all dom-on_campus int-on_campus']/a[contains(text(), 'Master of')]/@href|"
        #     "//div[@id='all-courses-list']/ul/li[@data-level='all postgraduate'][@data-mode='all dom-online int-on_campus dom-online']/a[contains(text(), 'Master of')]/@href").extract()
        links = response.xpath("//a[contains(text(), 'Master of')]/@href").extract()

        # 组合字典
        programme_dict = {}
        # programme_list = response.xpath(
        #     "//div[@id='all-courses-list']/ul/li[@data-level='all postgraduate'][@data-mode='all dom-on_campus dom-online int-on_campus dom-online']/a[contains(text(), 'Master of')]//text()|"
        #     "//div[@id='all-courses-list']/ul/li[@data-level='all postgraduate'][@data-mode='all dom-on_campus int-on_campus']/a[contains(text(), 'Master of')]//text()|"
        #     "//div[@id='all-courses-list']/ul/li[@data-level='all postgraduate'][@data-mode='all dom-online int-on_campus dom-online']/a[contains(text(), 'Master of')]//text()").extract()
        programme_list = response.xpath("//a[contains(text(), 'Master of')]//text()").extract()

        for link in range(len(links)):
            url = links[link]
            programme_dict[url] = programme_list[link]

        # # 过滤链接
        # for li1 in range(len(links)):
        #     if "graduate" in links[li1]:
        #         links[li1] = ""
        # print(programme_dict)
        clear_space(links)
        # print(len(links))
        links = list(set(links))
        # print(len(links))

        links = ["https://futurestudents.csu.edu.au/courses/agricultural-wine-sciences/master-sustainable-agriculture",
"https://futurestudents.csu.edu.au/courses/animal-vet-sciences/master-animal-science",
"https://futurestudents.csu.edu.au/courses/business/master-business-administration-12",
"https://futurestudents.csu.edu.au/courses/business/master-business-administration-16",
"https://futurestudents.csu.edu.au/courses/business/master-commerce-12",
"https://futurestudents.csu.edu.au/courses/business/master-commerce-16",
"https://futurestudents.csu.edu.au/courses/business/master-professional-accounting-12",
"https://futurestudents.csu.edu.au/courses/business/master-professional-accounting-16",
"https://futurestudents.csu.edu.au/courses/technology-computing-maths/master-information-technology-12",
"https://futurestudents.csu.edu.au/courses/technology-computing-maths/master-information-technology-16",
"https://futurestudents.csu.edu.au/courses/library-information-studies/master-information-studies",
"https://futurestudents.csu.edu.au/courses/police-security-emergency/master-customs-administration",
"https://futurestudents.csu.edu.au/courses/police-security-emergency/master-terrorism-security-studies",
"https://futurestudents.csu.edu.au/courses/theology-religious-studies/master-ministry",
"https://futurestudents.csu.edu.au/courses/theology-religious-studies/master-theology", ]
        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianYanItem)
        item['university'] = "Charles Sturt University"
        # item['country'] = 'Australia'
        # item['website'] = 'http://futurestudents.csu.edu.au'
        item['url'] = response.url
        item['degree_type'] = 2
        item['teach_time'] = 'coursework'
        print("===========================")
        print(response.url)
        item['major_type1'] = response.meta.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        driver = webdriver.Chrome(r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Lib\site-packages\selenium\chromedriver.exe")
        driver.implicitly_wait(30)  # 隐式等待
        driver.get(response.url)
        import time
        # time.sleep(2)

        try:
            location = driver.find_element_by_xpath(r"//div[@id='fYear-campus']").text
            print("location: ", location)
            # location = response.xpath(
            #     "//div[@id='locations1']//div[@class='section no-padding-top']//div[@class='card card-content z-depth-0']//div[@class='is-domestic']//text()|"
            #     "//div[@id='fYear-campus']//text()").extract()
            # clear_space(location)
            # item['location'] = ','.join(location).strip()
            item['location'] = location
            print("item['location']: ", item['location'])

            programme = response.xpath(
                "//h1[@class='logo-font csu-slogan course course-name']//text()").extract()
            clear_space(programme)
            programme = ''.join(programme).replace("(with specialisations)", "").replace("  ", "").strip()
            item['degree_name'] = programme
            print("item['degree_name']: ", item['degree_name'])

            item['programme_en'] = programme.replace("Master of", "").strip()
            print("item['programme_en']: ", item['programme_en'])


            degree_overview_en = response.xpath(
                "//div[@class='col s12 m12 push-l1 l9 overview-text']").extract()
            item['degree_overview_en'] = remove_class(clear_lianxu_space(degree_overview_en))
            # print("item['degree_overview_en']: ", item['degree_overview_en'])

            duration = driver.find_element_by_xpath(r"//div[@id='fYear-duration']").text
            # print("duration: ", duration)
            # duration = response.xpath(
            #     "//div[@id='ocbDuration']//text()|"
            #     "//div[@id='fYear-duration']//text()").extract()
            # clear_space(duration)
            # item['duration'] = ','.join(duration).replace(",,", ",").replace(":,", ":").replace(",:", ":").strip().strip(",").strip()
            item['duration'] = duration
            print("item['duration']: ", item['duration'])

            start_date = driver.find_element_by_xpath(r"//div[@id='fYear-sessions']").text
            # print("start_date: ", start_date)
            # start_date = response.xpath(
            #     "//div[@id='sessDatesKI']/span/text() | //div[@id='sessDateDom']/span/text()| "
            #     "//div[@id='fYear-sessions']//text()").extract()
            # clear_space(start_date)
            # print("start_date: ", start_date)
            # start_date_str = ""
            # if len(start_date) > 0:
            #     start_date_str = start_date[0].strip()
            # if ";" in start_date_str:
            #     start_date_list = start_date_str.split(";")
            #     st_l = []
            #     for s in start_date_list:
            #         s1 = s.replace("2018", "").replace("2019", "").replace("0", "").strip()
            #         st_l.append(s1)
            #     st_l = list(set(st_l))
            #     item['start_date'] = ','.join(st_l).strip().strip(",").strip()
            item['start_date'] = start_date
            print("item['start_date']: ", item['start_date'])

            career = response.xpath(
                "//div[@class='hasCareerOpps']|//div[@class='section isPostGrad isHDR']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            # 显示等待，出现id为subject-div的元素结束等待
            locator = (By.ID, 'subject-div')
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
            # //div[@id='testimonial-area']/following-sibling::div[1]
            modules = driver.find_element_by_xpath(r"//div[@id='subject-div']").get_attribute('innerHTML')
            # print("modules: ", modules)
            # modules = response.xpath(
            #     "//div[@id='subject-intro']|//div[@id='subject-div']").extract()
            item['modules_en'] = remove_class(modules)
            print("item['modules_en']: ", item['modules_en'])

            rntry_requirements_en = driver.find_element_by_xpath(r"//div[@id='detailCardTeam1']").get_attribute('innerHTML')
            # print("rntry_requirements_en: ", rntry_requirements_en)
            # rntry_requirements_en = response.xpath(
            #     # "//h3[contains(text(),'Entry requirements')]/..|"
            #     "//div[@id='detailCardTeam1']").extract()
            item['rntry_requirements_en'] = remove_class(clear_lianxu_space([rntry_requirements_en]))
            print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

            item["ielts"] = '6.5'
            item["ielts_l"] = '6.0'
            item["ielts_s"] = '6.0'
            item["ielts_r"] = '6.0'
            item["ielts_w"] = '6.0'

            department = response.xpath(
                "//html//nav[@class='breadcrumb-wrapper']//a[3]//text()").extract()
            clear_space(department)
            item['department'] = ' '.join(department).strip()
            # print("item['department']: ", item['department'])

            apply_desc_en = response.xpath(
                "//div[@id='international-app']").extract()
            item['apply_desc_en'] = remove_class(clear_lianxu_space(apply_desc_en))
            # print("item['apply_desc_en']: ", item['apply_desc_en'])

            deadline = response.xpath(
                "//div[@class='card']//div[@class='card very-small-international-lower']//text()").extract()
            clear_space(deadline)
            # print("deadline: ", deadline)
            deadline_str = ""
            if "Important dates" in deadline:
                d = deadline.index("Important dates")
                deadline_str += deadline[d+1] + " "
            item['deadline'] = getStartDate(deadline_str.strip())
            # print("item['deadline']: ", item['deadline'])

            feeDict = {"Master of Animal Science": "28800",
"Master of Business Administration": "28560",
"Master of Commerce": "28560",
"Master of Customs Administration": "19200",
"Master of Information Technology": "Port Macquarie:20100,CSU Study Centre Melbourne, CSU Study Centre Sydney:29680",
"Master of Medical Radiation Science": "28800",
"Master of Ministry":"18400",
"Master of Philosophy (Lab Based)": "32000",
"Master of Philosophy (Non Lab Based)":"29600",
"Master of Professional Accounting": "CSU Study Centre Melbourne, CSU Study Centre Sydney28560",
"Master of Sustainable Agriculture":"28800",
"Master of Terrorism and Security Studies":"19200",
"Master of Theology": "18400", }
            item['tuition_fee'] = feeDict.get(item['degree_name'].replace("(12 subjects)", "").replace("(16 subjects)", "").strip())

            fd = {"Master of Business Administration(12 subjects)":"29,712",
"Master of Business Administration(16 subjects)":"29,712",
"Master of Commerce(12 subjects)":"22,284",
"Master of Commerce(16 subjects)":"29,712",
"Master of Information Technology(12 subjects)":"23,160",
"Master of Information Technology(16 subjects)":"30,880",
"Master of Professional Accounting(12 subjects)":"22,284",
"Master of Professional Accounting(16 subjects)":"29,712",}
            if item['tuition_fee'] is None:
                item['tuition_fee'] = fd.get(item['degree_name'])

            print("item['tuition_fee']: ", item['tuition_fee'])

            online = response.xpath("//h2[contains(text(),'Study mode')]/following-sibling::*//text()").extract()
            clear_space(online)
            print("online: ", online)
            if ''.join(online).strip() != "Online":
                major_list = response.xpath(
                    # "//div[@id='subject-div']//div[@class='section']//h2//text()|"    # 2019.03.18 星期一之前的xpath
                    # "//div[@id='subject-div']//div[@class='section']//h3//text()|"
                    "//div[@id='fYear-specialisation']/ul[1]/li//text()|"
                    "//div[@id='fYear-specialisation']/h3//text()|"
                    "//div[@id='fYear-specialisation']/h6//text()").extract()
                clear_space(major_list)
                print("major_list: ", major_list)
                print(len(major_list))

                driver.quit()
                if len(major_list) == 0:
                    yield item
                else:
                    for m in range(len(major_list)):
                        item['programme_en'] = major_list[m]
                        # item['modules_en'] = remove_class(clear_lianxu_space([modules_list[m]]))
                        # print("item['programme_en']: ", item['programme_en'])
                        yield item
        except Exception as e:
            with open("scrapySchool_Australian_yan/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

