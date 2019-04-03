# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_Australian_ben.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_ben.getItem import get_item
from scrapySchool_Australian_ben.getTuition_fee import getTuition_fee
from scrapySchool_Australian_ben.items import ScrapyschoolAustralianBenItem
from scrapySchool_Australian_ben.remove_tags import remove_class
from scrapySchool_Australian_ben.getStartDate import getStartDate, getStartDateMonth
from scrapySchool_Australian_ben.getDuration import getIntDuration
from lxml import etree
import requests
from urllib import parse
from selenium import webdriver


class TheUniversityOfMelbourne_U_update201903Spider(scrapy.Spider):
    name = "TheUniversityOfMelbourne_U_update201903"

    start_urls = ["https://study.unimelb.edu.au/find/interests/architecture-building-planning-and-design",
"https://study.unimelb.edu.au/find/interests/arts-humanities-and-social-sciences",
"https://study.unimelb.edu.au/find/interests/business-and-economics",
"https://study.unimelb.edu.au/find/interests/education",
"https://study.unimelb.edu.au/find/interests/engineering",
"https://study.unimelb.edu.au/find/interests/environment",
"https://study.unimelb.edu.au/find/interests/health",
"https://study.unimelb.edu.au/find/interests/information-technology-and-computer-science",
"https://study.unimelb.edu.au/find/interests/law",
"https://study.unimelb.edu.au/find/interests/music-and-visual-and-performing-arts",
"https://study.unimelb.edu.au/find/interests/science",
"https://study.unimelb.edu.au/find/interests/veterinary-agricultural-and-food-sciences", ]
    allow_domains = ["https://study.unimelb.edu.au"]
    # print(len(start_urls))
    headers_base = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    def parse(self, response):
        links = response.xpath("//span[contains(text(),'Bachelor')]/../@href").extract()
        # print("links: ", links)
        department_dict = {"https://study.unimelb.edu.au/find/interests/architecture-building-planning-and-design/": "Architecture, Building and Planning",
"https://study.unimelb.edu.au/find/interests/arts-humanities-and-social-sciences/": "Arts, humanities and social sciences",
"https://study.unimelb.edu.au/find/interests/business-and-economics/": "Business and Economics",
"https://study.unimelb.edu.au/find/interests/education/": "Education",
"https://study.unimelb.edu.au/find/interests/engineering/": "Engineering",
"https://study.unimelb.edu.au/find/interests/environment/": "Environment",
"https://study.unimelb.edu.au/find/interests/health/": "Health",
"https://study.unimelb.edu.au/find/interests/information-technology-and-computer-science/": "Information Technology and Computer Science",
"https://study.unimelb.edu.au/find/interests/law/": "Law",
"https://study.unimelb.edu.au/find/interests/music-and-visual-and-performing-arts/": "Music and Visual and Performing arts",
"https://study.unimelb.edu.au/find/interests/science/": "Science",
"https://study.unimelb.edu.au/find/interests/veterinary-agricultural-and-food-sciences/": "Veterinary and Agricultural Sciences",}
        department = department_dict.get(response.url)
        # print(response.url)
        # print("dep: ", department)
        # links = ["https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-fine-arts-music-theatre/"]
        if links:
            for url in links:
                # url = "" + link
                # 使用urllib里面的parse拼接链接
                yield scrapy.Request(parse.urljoin(response.url, url), callback=self.parse_data, meta={"department": department})


    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "The University of Melbourne"
        print("================================================")
        print(response.url)
        item['url'] = response.url
        item['degree_type'] = 1
        item['department'] = response.meta.get('department')
        print("item['department']: ", item['department'])
        try:
            degree_name = response.xpath("//div[@class='headline']/h1/text()|//h1[@id='page-header']//text()").extract()
            item['degree_name'] = ''.join(degree_name).strip()
            print("item['degree_name']: ", item['degree_name'])

            programme = re.findall(r"\(.*\)|\-.*", item['degree_name'])
            print(programme)
            if len(programme) > 0:
                item['degree_name'] = item['degree_name'].replace(''.join(programme), '').strip()
                item['programme_en'] = ''.join(programme).replace("(", "").replace(")", "").replace("-", "").strip()
            else:
                item['programme_en'] = item['degree_name'].replace("Master of", "").strip()
            print("item['degree_name']=: ", item['degree_name'])
            print("item['programme_en']: ", item['programme_en'])

            duration = response.xpath(
                "//div[@class='course-length icn icn-duration']/text()|//li[contains(text(),'full time')]//text()").extract()
            clear_space(duration)
            # print("duration:", duration)
            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration']: ", item['duration'])
            # print("item['duration_per']: ", item['duration_per'])

            location = response.xpath(
                "//li[@id='course-overview-campus']//text()|//li[contains(text(),'Campus')]//text()").extract()
            # print(location, '==')
            item['location'] = ''.join(location).replace("On Campus", "").replace("(", "").replace(")", "").strip()
            print("item['location']: ", item['location'])

            if item['location'].lower() != "online":

                start_date = response.xpath(
                    "//li[@id='course-overview-entryPeriods']//text()").extract()
                # print(start_date, '==')
                start_date_str = getStartDateMonth(''.join(start_date))
                item['start_date'] = start_date_str
                # print("item['start_date']: ", item['start_date'])

                overview_en = response.xpath("//div[@class='course-content']").extract()
                item['degree_overview_en'] = remove_class(clear_lianxu_space(overview_en))
                # print("item['overview_en']: ", item['overview_en'])


                career_url = response.xpath("//a[contains(text(),'Where will this take me?')]/@href").extract_first()
                if career_url:
                    item['career_en'] = self.parse_career(parse.urljoin(response.url, career_url))
                # print("item['career_en']: ", item['career_en'])

                entry_url = response.xpath("//a[contains(text(),'Entry requirements')]/@href").extract_first()
                if entry_url:
                    item['rntry_requirements_en'] = self.parse_entry(parse.urljoin(response.url, entry_url))
                print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

                fee_url = response.xpath("//a[contains(text(),'Fees & scholarships')]/@href").extract_first()
                if fee_url:
                    item['tuition_fee'] = self.parse_fee(parse.urljoin(response.url, fee_url))
                print("item['tuition_fee']: ", item['tuition_fee'])

                # https://study.unimelb.edu.au/how-to-apply/english-language-requirements/undergraduate-english-language-requirements
                item['ielts_desc'] = " you need a score of 6.5 or more in the Academic International English Language Testing System (IELTS), with no bands less than 6.0."
                item["ielts"] = '6.5'
                item["ielts_l"] = '6.0'
                item["ielts_s"] = '6.0'
                item["ielts_r"] = '6.0'
                item["ielts_w"] = '6.0'
                item['toefl_desc'] = "a score of 79 and scores of 21 for writing, 18 for speaking, 13 for reading, 13 for listening for an internet-based test. To submit your scores when you apply, use our TOEFL Institution Code: 0974."
                item["toefl"] = '79'
                item["toefl_l"] = '13'
                item["toefl_s"] = '18'
                item["toefl_r"] = '13'
                item["toefl_w"] = '21'

                print("ielts: ", item['ielts'], ' - ', item['ielts_l'], ' - ', item['ielts_s'], ' - ', item['ielts_r'], ' - ', item['ielts_w'],)
                print("toefl: ", item['toefl'], ' - ', item['toefl_l'], ' - ', item['toefl_s'], ' - ', item['toefl_r'], ' - ', item['toefl_w'], )

                # 匹配跳转之后获取modules
                modules_url = response.xpath("//a[contains(text(),'What will I study?')]/@href").extract_first()
                major_list = []
                major_overview_list = []
                if modules_url:
                    modules = self.parse_modules(parse.urljoin(response.url, modules_url))
                    print("modules: ", modules)
                    item['modules_en'] = modules[0]
                    major_list = modules[1]
                    major_overview_list = modules[2]
                    print(len(major_list), "=====", len(major_overview_list))
                    print(major_list)
                print("item['modules_en']: ", item['modules_en'])

                # 有多个专业和一个专业的区分插入
                if len(major_list) > 0:
                    if len(major_list) == len(major_overview_list):
                        for i in range(len(major_list)):
                            item['programme_en'] = major_list[i]
                            major_overview_str = ""
                            for m in major_overview_list[i]:
                                major_overview_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
                            item['overview_en'] = remove_class(major_overview_str)
                            print("item['overview']==: ", item['overview_en'])
                            yield item
                else:
                    yield item

        except Exception as e:
            with open("scrapySchool_Australian_ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)


    def parse_career(self, career_url):
        print("career_url: ", career_url)
        data = requests.get(career_url, headers=self.headers_base)
        response = etree.HTML(data.text)
        career = response.xpath("//div[@class='with-jumpnav']//div[@class='course-content']")
        # clear_space(modules)
        career_str = ""
        if len(career) > 0:
            for m in career:
                career_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
        career_en = remove_class(clear_lianxu_space([career_str]))
        return career_en

    def parse_modules(self, modulesUrl):
        print("modulesUrl: ", modulesUrl)
        data = requests.get(modulesUrl, headers=self.headers_base)
        response = etree.HTML(data.text)
        # print("response.url: ", data.url)
        # modules = response.xpath("//div[@id='degree-structure']")
        modules = response.xpath("///section[@id='overview']//div[@class='course-section__main']")
        # clear_space(modules)
        modules_str = ""
        if len(modules) > 0:
            for m in modules:
                modules_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
        # modulesRe = re.findall(r"Next.*<", modules_str)
        # print("===", modulesRe)
        modules_en = remove_class(clear_lianxu_space([modules_str]))

        major_list = response.xpath("//span[contains(text(),'Majors')]/../../following-sibling::ul/li[1]/div/span[1]//text()")
        major_overview_list = response.xpath("//span[contains(text(),'Majors')]/../../following-sibling::ul/li[2]")
        # major_overview_list_tmp = []
        # for m in major_overview_list:
        #     tmp = m.xpath
        return modules_en,major_list,major_overview_list

    def parse_entry(self, entryUrl):
        print("entryUrl: ", entryUrl)
        data = requests.get(entryUrl, headers=self.headers_base)
        response = etree.HTML(data.text)
        driver = webdriver.Chrome(r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Lib\site-packages\selenium\chromedriver (2).exe")
        cookiedict = {"_ga": "GA1.1.1809461699.1534918500",
"uom": "00000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
"studentone_faculty": "",
"studentone_ccode": "",
"_gid": "GA1.1.634631721.1552461942",
"_fbp": "fb.2.1552461964657.625675355",
"SQ_SYSTEM_SESSION": "6o6qop02nor8m8n20jecnvdvbntg5aavi8rpqfmrlgqrbbn10vn07cp5iisjhn72p43rt5824rova88hcgvftvear6s8v864ombvhk0",
"fac": "{%22profile%22:{%22open%22:false%2C%22loggedin%22:false%2C%22qualification%22:%22postgrad%22%2C%22entry%22:%2275%22%2C%22residency%22:%22international%22%2C%22persona%22:%22secondary%22}%2C%22favourites%22:[]}",
"liveagent_oref": "",
"liveagent_ptid": "a7725fa7-d619-41cd-8a3a-5d076f70e38b",
"internal_source":"https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-secondary-internship/what-will-i-study/:",
"CONSENTMGR": "ts:1552628190791%7Cconsent:true",
"traffic_source": "(none)",
"liveagent_sid": "9a79ac41-a5c2-4d14-a927-a192e8e9573c",
"liveagent_vc": "4",
"utag_main": "v_id:0165604592d9000346cead476abf0306d005706500978$_sn:11$_ss:0$_st:1552636279696$_pn:10%3Bexp-session$ses_id:1552632639470%3Bexp-session",}
        driver.implicitly_wait(30)
        driver.get(entryUrl)
        import time
        # time.sleep(10)
        # driver.tim
        # driver.add_cookie(cookie_dict=cookiedict)
        handle = driver.current_window_handle
        entry_requirements = driver.find_element_by_xpath("//div[@class='course-content']").get_attribute('innerHTML')
        # entry_requirements = response.xpath("//div[@class='course-content']").innerhtml()

        # print("===",entry_requirements)
        # entry_requirements_str = ""
        # if len(entry_requirements) > 0:
        #     for m in [entry_requirements]:
        #         entry_requirements_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
        # entry_requirementsRe = re.findall(r"Next.*", entry_requirements_str)
        # print("entry_requirementsRe===", entry_requirementsRe)
        entry_requirements_en = remove_class(entry_requirements)
        # if len(entry_requirementsRe) > 0:
        #     entry_requirements_en = entry_requirements_en.replace(''.join(entry_requirementsRe), '<').strip()
        # driver.close()
        driver.quit()
        return entry_requirements_en

    def parse_fee(self, feeUrl):
        print("feeUrl: ", feeUrl)
        data = requests.get(feeUrl, headers=self.headers_base)
        # response = etree.HTML(data.text)
        # print("response.url: ", data.url)
        # tuition_fee = response.xpath("//span[contains(text(),'Typical annual course fee')]/following-sibling::span[1]//text()")
        tuition_fee0 = re.findall(r"""\"international\"\:\{\"ff\-indicative\":\"\$[\d,]*?\",\"ff\-year\"\:\"\$[\d,]*""", data.text)
        tuition_fee1 = re.findall(r"\"ff\-year\"\:\"\$[\d,]*", ''.join(tuition_fee0))
        print("tuition_feetmp: ", tuition_fee1)
        clear_space(tuition_fee1)
        tuition_fee = getTuition_fee(''.join(tuition_fee1).replace("$", "").replace("AUD", ""))
        # if tuition_fee == 0:
        #     item['tuition_fee'] = None
        # else:
        #     item['tuition_fee_pre'] = "AUD$"
        return tuition_fee

    def parse_apply(self, applyUrl, item):
        print("applyUrl: ", applyUrl)
        data = requests.get(applyUrl, headers=self.headers_base)
        response = etree.HTML(data.text)
        # print("response.url: ", data.url)
        how_to_apply = response.xpath("//div[@id='apply-now']|//div[@id='how-to-apply']")
        # clear_space(how_to_apply)
        how_to_apply_str = ""
        if len(how_to_apply) > 0:
            for m in how_to_apply:
                how_to_apply_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
        item['apply_desc_en'] = remove_class(clear_lianxu_space([how_to_apply_str]))
        print("跳转获得：item['apply_desc_en']: ", item['apply_desc_en'])

        deadline = response.xpath(
            "//*[contains(text(),'Application closing dates')]/../following-sibling::*[1]//text()|"
            "//strong[contains(text(),'Application Deadlines')]/../following-sibling::*[position()<3]//text()")
        item['deadline'] =clear_lianxu_space(deadline)
        print("跳转获得：item['deadline']: ", item['deadline'])

        apply_documents_en = response.xpath(
            "//h2[contains(text(),'Application Checklist')]/..")
        doc = ""
        if len(apply_documents_en) > 0:
            for a in apply_documents_en:
                doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
        item['apply_documents_en'] = remove_class(clear_lianxu_space([doc]))
        print("跳转获得：item['apply_documents_en']: ", item['apply_documents_en'])

