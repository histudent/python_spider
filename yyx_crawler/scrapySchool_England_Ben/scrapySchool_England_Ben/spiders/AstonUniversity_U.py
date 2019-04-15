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
        data_dict = json.loads(response.text)
        # print(data_dict)
        # print(len(data_dict))
        ll = []
        for d in data_dict:
            mode = d.get("mode")
            # print("mode: ", mode)
            m = d.get("type")
            # print("mode: ", m)
            if 'full' in mode.lower() and "Foundation" not in m:
                url = d.get("_data-href")
                # print("mode: ", mode)
                # print("---",url)
                # ll.append(url)
                # yield scrapy.Request(url, callback=self.parse_data)
        links = ["http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-language-and-literature/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/sociology-social-policy/english-language-sociology/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/english-language/englishlanguage/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/english-language/englishlanguage-social-policy/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/meng-electronic-engineering-and-computer-science/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/beng-electronic-engineering-and-computer-science/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/bsc-translation-studies-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/bsc-spanish/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/politics-sociology/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/politics-social-policy/",
"http://www.aston.ac.uk/aston-medical-school/mbchb-medicine/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/sociology-social-policy/bsc-sociology-and-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/bsc-politics-with-international-relations/",
"http://www.aston.ac.uk/study/undergraduate/courses/joint-honours/politics-and-economics/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-mathematics-for-industry/",
"http://www.aston.ac.uk/study/undergraduate/courses/lhs/bsc-optometry/",
"http://www.aston.ac.uk/study/undergraduate/courses/lhs/bsc-optometry/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/politics-english-language/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/sociology-social-policy/sociology-international-relations/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-logistics-with-purchasing-management/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/international-relations-and-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/international-relations-and-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/international-relations-and-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/international-relations-social-policy/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/international-relations-and-politics/international-relations-english-language/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-language-modern-languages/%20",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/german/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-literature-and-politics/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-literature-and-sociology/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/german-spanish/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-literature-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/french/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/frenchandgerman/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/frenchandspanish/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/english-language/bsc-business-management-and-english-language/",
"http://www.aston.ac.uk/study/undergraduate/courses/eas/bsc-cybersecurity/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-literature-and-international-relations/",
"http://www.aston.ac.uk/study/undergraduate/courses/joint-honours/international-relations-business/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/bsc-translation-studies-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/bsc-translation-studies-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/bsc-translation-studies-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/bsc-translation-studies-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/languages-translation/bsc-translation-studies-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/sociology-social-policy/bsc-sociology-and-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-language-modern-languages/%20",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-language-modern-languages/%20",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-literature-modern-languages/",
"http://www.aston.ac.uk/study/undergraduate/courses/languages-social-sciences/bsc-english-literature-modern-languages/", ]


        for url in links:
            yield scrapy.Request(url, callback=self.parse_data)
        # print(len(ll))
        # ll = list(set(ll))
        # print(len(ll))
    # def parse_url(self, response):
    #     print("--*-", response.url)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "https://www.aston.ac.uk/"
        item['university'] = "Aston University"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        item['location'] = "Aston University,Birmingham, B4 7ET"
        print("======================================")
        print(response.url)
        try:
            programmeDegreetype = response.xpath("//h1[@id='skiplinks']//text()").extract()
            programmeDegreetypeStr = ''.join(programmeDegreetype)
            # print(programmeDegreetypeStr)
            degree_type = re.findall(r"^\w+/\w+|^\w+\s/\s\w+|^\w+\s\(Hons\)|^[BML]\w{1,7}\s", programmeDegreetypeStr)
            # print("degree_type = ", degree_type)
            item['degree_name'] = ''.join(degree_type).replace("(Hons)", "").strip()
            if item['degree_name'] == "Business":
                item['degree_name'] = ""
            programme = programmeDegreetypeStr.replace(item['degree_name'], "").strip()
            item['programme_en'] = ''.join(programme).replace("(Hons)", "").strip().strip("in").strip()
            print("item['degree_name']: ", item['degree_name'])
            print("item['programme_en']: ", item['programme_en'])



            alevel = response.xpath(
                "//span[contains(text(),'A Levels')]/../../../../../../following-sibling::*[1]//text()|"
                "//span[contains(text(),'A-Levels')]/../../../../../../following-sibling::*[1]//text()").extract()
            clear_space(alevel)
            # print("alevel: ", alevel)
            item['alevel'] = ''.join(alevel).strip()

            if item['alevel'] == "":
                alevel1 = response.xpath("//strong[contains(text(),'A Levels')]/..//text()").extract()
                if "A Levels" in ''.join(alevel1).strip():
                    alevelindex = ''.join(alevel1).strip().index('A Levels')
                    item['alevel'] = ''.join(''.join(alevel1).strip()[alevelindex:]).strip()
            # print("item['alevel']: ", item['alevel'])
            if len(item['alevel']) > 300:
                item['alevel'] = item['alevel'][:301]

            ib = response.xpath("//span[contains(text(),'IB')]/../../../../../../following-sibling::*[2]//text()|"
                                "//strong[contains(text(),'IB')]/..//text()").extract()
            clear_space(ib)
            item['ib'] = ''.join(ib).strip()
            # print("item['ib']: ", item['ib'])
            if len(item['ib']) > 300:
                item['ib'] = item['ib'][:301]

            overview = response.xpath("//a[contains(text(),'Course overview')]/../../../../../..|"
                                      "//*[contains(text(), 'Course outline')]/../../../../../../div/following-sibling::div[1]|"
                                      "//*[contains(text(), 'Course Outline')]/../../../../../div/../following-sibling::div[1]//*[contains(text(), 'Modules')]/../preceding-sibling::*|"
                                      "//*[contains(text(),'Course Outline')]/../../../../../following-sibling::div[1]//*[contains(text(),'Sample module options')]/../preceding-sibling::*|"
                                      "//*[contains(text(), 'Subject Guide & Modules')]/../../../../../../div/following-sibling::div[1]//*[contains(text(),'Sample module options')]/../preceding-sibling::*|"
                                      "//*[contains(text(), 'Course Outline')]/../../../../../div/../following-sibling::div[1]//*[contains(text(), 'Sample module options')]/../../preceding-sibling::*|"
                                      "//*[contains(text(), 'Subject Guide & Modules')]/../../../../../../div/following-sibling::div[1]//*[contains(text(),'Sample module options')]/..|"
                                      "//*[contains(text(), 'Subject Guide & Modules')]/../../../../../../div/following-sibling::div[1]//*[contains(text(),'Core modules:')]/../preceding-sibling::*|"
                                      "//strong[contains(text(),'Courses')]/../../following-sibling::div[1]|"
                                      "//*[contains(text(), 'Programme outline and modules')]/../../../../../../div/following-sibling::div[1]//*[contains(text(),'Modules')]/..|"
                                      "//*[contains(text(),'Course Outline')]/../../../../../following-sibling::div[1]//*[contains(text(),'Sample Module Options')]/../preceding-sibling::*|"
                                      "//*[contains(text(),'Course Outline & Modules')]/../../../../../following-sibling::div[1]//*[contains(text(),'Modules')]/preceding-sibling::*").extract()
            if len(overview) == 0:
                overview = response.xpath("//a[contains(text(),'Course Outline')]/../../../../../..").extract()
            item['overview_en'] = ''.join(remove_class(clear_lianxu_space(overview)).replace("<br>", "").strip().split("\n")).strip()
            # if item['overview_en'] == "":
            #     print("overview 为空")
            # print("item['overview_en'] = ", item['overview_en'])

            modules_en = response.xpath("//*[contains(text(),'modules:')]/../..|//strong[contains(text(),'Programme content')]/../preceding-sibling::*[1]/following-sibling::*").extract()
            if len(modules_en) == 0:
                modules_en = response.xpath(
                    "//*[contains(text(),'Modules')]/../../..").extract()
                if len(modules_en) == 0:
                    modules_en = response.xpath(
                        "//*[contains(text(),'Modules')]/../..").extract()
                    if len(modules_en) == 0:
                        modules_en = response.xpath(
                            "//*[contains(text(),'Modules')]/..").extract()
                        if len(modules_en) == 0:
                            modules_en = response.xpath(
                                "//*[contains(text(),'What you will study')]/../../../../../following-sibling::*").extract()
                            if len(modules_en) == 0:
                                modules_en = response.xpath("//*[contains(text(), 'Subject guide and modules')]/../../../../../../div/following-sibling::div[1]").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules_en))
            if item['modules_en'] == "":
                item['modules_en'] = None
            print("item['modules_en'] = ", item['modules_en'])

            career_en = response.xpath("//*[contains(text(),'Your future career')]/../../../../../following-sibling::*|"
                                       "//*[contains(text(),'Your future career opportunities')]/../../../../../following-sibling::*|"
                                       "//*[contains(text(),'Career opportunities')]/../../../../../following-sibling::*|"
                                       "//*[contains(text(),'Professional development programme')]/../../../../../following-sibling::*|"
                                       "//*[contains(text(),'Career Prospects')]/../../../../../following-sibling::*|"
                                       "//*[contains(text(),'Professional Development Programme')]/../../../../div/following-sibling::*|"
                                       # "//*[contains(text(),'Professional Development Programme')]/../../../../../following-sibling::*|"
                                       "//*[contains(text(),'Career prospects')]/../../../../../following-sibling::*|"
                                       "//*[contains(text(),'Career Opportunities')]/../../../../../following-sibling::*|"
                                       "//*[contains(text(),'Graduate destinations')]/../../../../../following-sibling::*|"
                                       "//a[contains(text(),'Career')]/../../../../../following-sibling::*|"
                                       "//a[contains(text(),'Personal Development')]/../../../../../following-sibling::*|"
                                       "//*[contains(text(),'Professional accreditation')]/../../../../../following-sibling::*").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            # print("item['career_en'] = ", item['career_en'])
            # if item['career_en'] == "":
            #     print("*** career")

            # following-sibling::*
            assessment_en = response.xpath(
                "//a[@id='learning'][contains(text(),'Learning, teaching & assessment')]/../..|"
                "//a[@class='panel-event'][contains(text(),'Learning, teaching & assessment')]/../../../../../..|"
                "//*[contains(text(),'Learning, Teaching & Assessment')]/../../../../../..|"
                "//*[contains(text(),'Learning, Teaching and Assessment')]/../../../../../..|"
                "//*[contains(text(),'Learning, teaching and assessment')]/../../../../../..|"
                "//*[contains(text(),'Learning, teaching and assessments')]/../../../../../..|"
                "//*[contains(text(),'Learning, teaching & assesment')]/../../../../../..").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en'] = ", item['assessment_en'])


            rntry_requirements = response.xpath(
                "//*[contains(text(),'Entry requirements & fees')]/../../../../../following-sibling::*//text()|"
                "//*[contains(text(),'Entry Requirements & Fees')]/../../../../../following-sibling::*//text()|"
                "//*[contains(text(),'Key information and entry requirements')]/../../../../../..//text()|"
                "//*[contains(text(),'Key information for applicants & entry requirements')]/../../../../../following-sibling::*//text()|"
                "//*[contains(text(),'Entry requirements')]/../../../../../following-sibling::*//text()|"
                "//*[contains(text(),'Entry Requirements')]/../../../../../following-sibling::*//text()").extract()
            start_date = rntry_requirements
            # print("start_date: ", start_date)
            item['apply_desc_en'] = "<div>"+clear_lianxu_space(rntry_requirements)+ "</div>"
            # print("item['apply_desc_en'] = ", item['apply_desc_en'])
            clear_space(start_date)
            duration_str = '; '.join(start_date)

            tuition_fee = response.xpath("//*[contains(text(),'Fees')]/../../../../../following-sibling::*//text()|"
                "//*[contains(text(),'fees')]/../../../../../following-sibling::*//text()|"
                "//strong[contains(text(),'Tuition fees')]/..//text()").extract()
            if len(tuition_fee) == 0:
                tuition_fee = response.xpath(
                    "//strong[contains(text(),'Fees:')]/../following-sibling::*[1]//text()").extract()
            clear_space(tuition_fee)
            tuition_fee_str = ''.join(tuition_fee)
            # print("tuition_fee_str: ", tuition_fee_str)
            tuition_fee_re = re.findall(
                r"International.*?£\d+,\d+|non-EU.*?£\d+,\d+|MSc.*?£\d+,\d+|entry:£\d+,\d+|2018/2019:£\d+,\d+|£\d+,\d+\sfor\sOutside\sEU|£\d+,\d+",
                tuition_fee_str, re.I)
            tuition_fee_re += re.findall(r"£\d+,\d+",duration_str)
            # print("tuition_fee_re: ", tuition_fee_re)
            if len(tuition_fee_re) != 0:
                t = re.findall(r"\d+,\d+", ''.join(tuition_fee_re))
                # item['tuition_fee'] = int(''.join(t).replace(",", "").strip())
                # print("item['tuition_fee']1 = ", item['tuition_fee'])
                item['tuition_fee'] = getTuition_fee(''.join(tuition_fee_re))
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee'] = ", item['tuition_fee'])
            # print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])

            # duration = response.xpath(
            #     "//*[contains(text(),'Duration')]/following-sibling::*//text()|"
            #     "//*[contains(text(),'Duration')]/..//text()").extract()
            # ((One)|(Two)|(Three)|(Four)|(Five)|(Six)|(Seven)|(Eight)|(Nine)|(Ten).{1,8}year)
            duration_re = re.findall(r'Duration.{1,85}|\d.{1,8}year|One.{1,8}year|Two.{1,8}year|Three.{1,8}year|Four.{1,8}year|Five.{1,8}year|Six.{1,8}year|Seven.{1,8}year|Eight.{1,8}year|Nine.{1,8}year|Ten.{1,8}year', duration_str, re.I)
            duration_re += re.findall(r'Duration.{1,80}|\d.{1,8}year|One.{1,8}year|Two.{1,8}year|Three.{1,8}year|Four.{1,8}year|Five.{1,8}year|Six.{1,8}year|Seven.{1,8}year|Eight.{1,8}year|Nine.{1,8}year|Ten.{1,8}year', item['overview_en'], re.I)
            # if len(duration) == 0:
            #     duration = response.xpath("//*[contains(text(),'Duration of course')]/../following-sibling::*[1]//text()").extract()
            clear_space(duration_re)
            duration_str = ' '.join(duration_re)
            # print("duration_str: ", duration_str)
            duration_list = getIntDuration(duration_str)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration']: ", item['duration'])
            # print("item['duration_per']: ", item['duration_per'])

            # https://www2.aston.ac.uk/about/termdates/2019-2020
            start_date_str = '; '.join(start_date)
            # print("start_date_str: ", start_date_str)
            start_date_re = re.findall(r'Start.{1,25}', start_date_str)
            # print("start_date_re", start_date_re)
            item['start_date'] = getStartDate(''.join(start_date_re))
            # print("item['start_date']: ", item['start_date'])

            # ielts_desc = ' '.join(start_date)
            # ielts_desc = re.findall(r'.{1,80}IELTS.{1,80}', ielts_desc)
            # print("ielts_desc: ", ielts_desc)
            allcontent = response.xpath(
                "//div[@class='tabbed-zone-outer oAccordionPanels tabbed-zone-sigma']//text() | //div[@class='tabbed-zone-outer oAccordionPanels tabbed-zone-rho']//text() | //div[@class='tabbed-zone-outer oAccordionPanels tabbed-zone-delta']//text() | //div[@class='tabbed-zone-outer oAccordionPanels tabbed-zone-sigma'][2]//text() | //div[@class='tabbed-zone-outer oAccordionPanels tabbed-zone-upsilon']//text()").extract()
            clear_space(allcontent)
            department_1 = response.xpath("//a[@href='/study/postgraduate/taught-programmes/abs/']//text()").extract()
            # print(department_1)
            if len(department_1) > 0:
                item['department'] = ''.join(department_1[0]).strip()
            department_re = re.findall(r"Life\s&\sHealth\sSciences\s-\sOSPAP|Aston\sBusiness\sSchool|Engineering\s&\sApplied\sScience|Languages\s&\sSocial\sSciences|Life\s&\sHealth\sSciences", ''.join(allcontent))
            # print("department_re: ", department_re)
            if item['department'] == "":
                if len(department_re) > 0:
                    item['department'] = ''.join(department_re[0]).strip()
            # print("item['department']: ", item['department'])

            # Aston Business School
            de_1 = ["full time mba",
"executive mba - part time",
"online mba",
"the executive dba",
"phd programme",
"msc business analytics",
"msc business & management",
"msc business & management (online)",
"msc information systems & business analysis",
"msc supply chain management",
"msc international business",
"msc international accounting & finance",
"msc international accounting & finance (online)",
"msc strategy and international business",
"msc entrepreneurship",
"msc accounting & finance",
"msc business economics & finance",
"msc finance",
"msc international accounting & finance",
"msc international accounting & finance (online)",
"msc investment analysis",
"msc strategic marketing management ",
"msc human resource management & business",
"msc organisational behaviour",
"msc work psychology & business",
"international pre-masters", ]
            #Engineering & Applied Science
            de_2 = ["msc professional engineering",
"msc computer science",
"msc software engineering ",
"msc software project management",
"msc professional engineering",
"msc electrical power engineering and systems ",
"msc telecommunications systems",
"msc wireless communications and networking",
"msc smart telecom and sensing networks (smartnet)",
"msc photonic integrated circuits, sensors and networks (pixnet)",
"msc professional engineering",
"msc engineering management",
"msc supply chain management",
"msc engineering leadership & management",
"msc supply chain leadership and management",
"msc professional engineering",
"msc mechanical engineering ",
"msc product design ",
"msc professional engineering", ]
            #Languages & Social Sciences
            de_3 = ["ma in forensic linguistics",
"ma in the european union & international relations",
"joint ma in multilevel governance & international relations",
"double ma in europe & the world",
"double ma in governance and international politics",
"ma in international relations and global governance",
"ma in sociology and social research",
"ma in policy and social research",
"ma in teaching english to speakers of other languages (tesol)",
"ma in tesol and translation studies",
"ma in tesol and translation studies",
"ma in translation in a european context",]
            # Life & Health Sciences
            de_4 = ["advanced hearing therapy practice - msc",
"clinical science (neurosensory sciences) - msc",
"doctor of hearing therapy - professional doctorate",
"biomedical science - msc",
"biomedical sciences top modules - all standalone modules",
"stem cells and regenerative medicine - msc",
"clinical neurophysiology practice - msc",
"clinical science (neurosensory sciences) - msc",
"neurophysiology - pgcert",
"clinical science (neurosensory sciences) - msc",
"doctor of optometry / doctor of ophthalmic science - professional doctorate",
"graduate diploma in optometry - graduate diploma",
"independent prescribing for optometrists - professional accreditation",
"optometry / ophthalmic science - msc",
"overseas pharmacists course (ospap) - full time pgdip / msc",
"pharmacist independent prescribing - pgcert",
"pharmacy (includes: msc pharmaceutical sciences, msc drug delivery, and msc pharmacokinetics) – msc",
"psychiatric pharmacy by distance learning and practice - pgdip",
"psychiatric pharmacy practice - msc",
"psychiatric therapeutics by distance learning - pgcert",
"cognitive neuroscience - msc",
"health psychology (online) - msc",
"health psychology (on campus) - msc",]
            if item['department'] == "":
                for de1 in de_1:
                    if item['programme_en'] == de1:
                        item['department'] = "Aston Business School"
                        break
            if item['department'] == "":
                for de2 in de_2:
                    if item['programme_en'] == de2:
                        item['department'] = "Engineering & Applied Science"
                        break
            if item['department'] == "":
                for de3 in de_3:
                    if item['programme_en'] == de3:
                        item['department'] = "Languages & Social Sciences"
                        break
            if item['department'] == "":
                for de4 in de_4:
                    if item['programme_en'] == de4:
                        item['department'] = " Life & Health Sciences"
                        break

            if 'business' in item['programme_en'].lower():
                item['department'] = "Aston Business School"
            if 'electrical' in item['programme_en'].lower() or 'engineering' in item['programme_en'].lower():
                item['department'] = "Engineering & Applied Science"
            # print("item['department']1: ", item['department'])

            if item['department'] == "Aston Medical School":
                item['ielts'] = 7.5
                item['ielts_l'] = 7
                item['ielts_s'] = 7
                item['ielts_r'] = 7
                item['ielts_w'] = 7
                item['toefl'] = 109
                item['toefl_l'] = 26
                item['toefl_r'] = 26
                item['toefl_s'] = 23
                item['toefl_w'] = 28
            elif  item['department'] == "Engineering & Applied Science" or  item['department'] == "Languages & Social Sciences":
                item['ielts'] = 6
                item['ielts_l'] = 5.5
                item['ielts_s'] = 5.5
                item['ielts_r'] = 5.5
                item['ielts_w'] = 5.5
                item['toefl'] = 78
                item['toefl_l'] = 11
                item['toefl_r'] = 12
                item['toefl_s'] = 17
                item['toefl_w'] = 20
            else:
                item['ielts'] = 6.5
                item['ielts_l'] = 6
                item['ielts_s'] = 6
                item['ielts_r'] = 6
                item['ielts_w'] = 6
                item['toefl'] = 93
                item['toefl_l'] = 19
                item['toefl_r'] = 18
                item['toefl_s'] = 19
                item['toefl_w'] = 23
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #                 item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))
            # print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
            #        item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<div class="tab-inner">
<div id="panelGroupHeader_73655987" class="tab-header-outer">
<div class="tab-header-inner">
<ul>
<li class="header"><h2><a href="#" class="panel-event">Undergraduate</a></h2></li>
<li class="expander"><a href="/international-students/your-country/east-asia/china/#" class="panel-event">Expand / Collapse</a>
</li>
</ul>
</div>
</div>
<div id="panelGroupBody_73655987" class="tab-body-outer">
<div class="tab-body-inner"><div class="ContentEditor"><p> <span style="line-height: 1.4em">Students who have achieved an average of 80% in the academic subjects in their Senior High School Leaving Certificate after 3 years of study may be considered for a Foundation programme.  </span><span style="line-height: 1.4em"> </span></p> <p>Students with 2 or 3 year University or College Diploma can be considered for undergraduate study - Year 1 entry. Applicants should be scoring a min of 80% average in relevant  academic subjects. <br /> <br />University students who have studied 1-2 years (full-time) at a recognised university may be eligible for first year entry, dependent on subjects, institution and grades. <span style="line-height: 1.4em"> </span></p> </div>
</div>
</div>
</div>
"""]))
            ucascode = response.xpath("//strong[contains(text(),'UCAS Code')]/following-sibling::*[1]//text()|"
                                      "//strong[contains(text(),'UCAS Code')]/../text()|"
                                      "//div[@class='ContentEditor']//strong[3]/../text()|"
                                      "//strong[contains(text(),'UCAS code')]/..//text()").extract()
            clear_space(ucascode)
            print("ucascode: ", ucascode)
            if len(ucascode) > 0:
                for u in ucascode:
                    if len(u.replace(":", "").replace(".", "").strip()) == 4:
                        item['ucascode'] = u.replace(":", "").replace(".", "").strip()
                        break
            print("item['ucascode']: ", item['ucascode'])

            # print(ucascode[:7])
            # if len(item['ucascode']) != 4 and len(ucascode) > 0:
            #     for u in ucascode[:6]:
            #         ucascode_uu_re = re.findall(r"[A-Z]\w{3}", u)
            #         print("ucascode_uu_re: ", ucascode_uu_re)

            if item['ucascode'] == "":
                ucascode_re = re.findall(r"UCAS\sCode.{1,8}", duration_str, re.I)
                if len(ucascode_re) == 0:
                    ucascode_re = re.findall(r"UCAS\sCode.{1,8}", remove_tags(clear_lianxu_space([response.text])), re.I)
                print("ucascode_re: ", ucascode_re)
                item['ucascode'] = ''.join(ucascode_re).replace("UCAS Code", "").replace("UCAS code", "").replace(".", "").replace("(", "").replace(";", "").replace(":", "").strip()
            print("item['ucascode']1: ", item['ucascode'])
            if item['ucascode'] == "":
                print("**** ucascode")

            # if "/" in item['degree_name']:
            #     print("//////////")
            if item['programme_en'] == "Optometry":
                item['degree_name'] = "Bsc"
                item['ucascode'] = 'B510'
                yield item
                item['degree_name'] = "MOptom"
                item['ucascode'] = 'B512'
                yield item
            elif item['programme_en'] == "Biomedical Engineering":
                item['degree_name'] = "BEng"
                item['ucascode'] = 'H542'
                yield item
                item['degree_name'] = "MEng"
                item['ucascode'] = 'H541'
                yield item
            elif item['programme_en'] == "Psychology":
                item['duration'] = 3
                item['ucascode'] = 'C800'
                yield item
                item['duration'] = 4
                item['ucascode'] = 'C801'
                yield item
            elif item['programme_en'] == "International Relations and Modern Languages (French/German/Spanish)":
                item['ucascode'] = 'LR2C'
                yield item
                item['ucascode'] = 'LR2G'
                yield item
                item['ucascode'] = 'LR2K'
                yield item
            elif item['programme_en'] == "International Business and Modern Languages":
                item['ucascode'] = 'NR11'
                yield item
                item['ucascode'] = 'NR12'
                yield item
                item['ucascode'] = 'NR14'
                yield item
                item['ucascode'] = 'NR24'
                yield item
                item['ucascode'] = 'NR33'
                yield item
                item['ucascode'] = 'NR44'
                yield item
                item['ucascode'] = 'NR15'
                yield item
            else:
                yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)
