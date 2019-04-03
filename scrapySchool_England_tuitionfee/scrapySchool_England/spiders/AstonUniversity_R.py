import scrapy
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.getDuration import getIntDuration, getTeachTime
import json

class AstonUniversity_RSpider(scrapy.Spider):
    name = "AstonUniversity_R"
    start_urls = ['http://w01.aston.ac.uk/data/core/content/courses.j2d?types[]=phd&types[]=mba']

    def parse(self, response):
        data_dict = json.loads(response.text)
        # print(data_dict)
        # print(len(data_dict))
        ll = []
        for d in data_dict:
            mode = d.get("mode")
            # print("mode: ", mode)
            if 'full' in mode.lower():
                url = d.get("_data-href")
                print("mode--: ", mode)
                print("---",url)
                # ll.append(url)
                yield scrapy.Request(url, callback=self.parse_data)
        # print(len(ll))
        # ll = list(set(ll))
        # print(len(ll))
    # def parse_url(self, response):
    #     print("--*-", response.url)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.aston.ac.uk/"
        item['university'] = "Aston University"
        item['url'] = response.url
        # 授课方式
        item['teach_type'] = 'phd'
        # 学位类型
        item['degree_type'] = 3
        item['teach_time'] = 'fulltime'
        item['location'] = "Aston University,Birmingham, B4 7ET"
        print("======================================")
        print(response.url)
        try:
            programmeDegreetype = response.xpath("//h1[@id='skiplinks']//text()").extract()
            programmeDegreetypeStr = ''.join(programmeDegreetype)
            # print(programmeDegreetypeStr)
            degree_type = re.findall(r"^\w+\s", programmeDegreetypeStr)
            # print("degree_type = ", degree_type)
            item['degree_name'] = ''.join(degree_type)
            programme = programmeDegreetypeStr.replace(''.join(degree_type), "").strip()
            item['programme_en'] = ''.join(programme)
            print("item['degree_name']: ", item['degree_name'])
            print("item['programme_en']: ", item['programme_en'])

            overview = response.xpath("//*[contains(text(), 'Course outline')]/../../../../../../div/following-sibling::div[1]|"
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
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            print("item['overview_en'] = ", item['overview_en'])

            modules_en = response.xpath("//*[contains(text(),'modules:')]/../..").extract()
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
                                if len(modules_en) == 0:
                                    modules_en = response.xpath("//*[contains(text(),'Programme Structure')]/../../../../../following-sibling::div[1]").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules_en))
            print("item['modules_en'] = ", item['modules_en'])

            career_en = response.xpath("//*[contains(text(),'Your future career prospects')]/../../../../../following-sibling::*|"
                                       "//*[contains(text(),'Your future career opportunities')]/../../../../../following-sibling::*|"
                                       "//*[contains(text(),'Career opportunities')]/../../../../../following-sibling::*|"
                                       "//*[contains(text(),'Professional development programme')]/../../../../../following-sibling::*|"
                                       "//*[contains(text(),'Career Prospects')]/../../../../../following-sibling::*|"
                                       "//*[contains(text(),'Professional Development Programme')]/../../../../div/following-sibling::*|"
                                       # "//*[contains(text(),'Professional Development Programme')]/../../../../../following-sibling::*|"
                                       "//*[contains(text(),'Career prospects')]/../../../../../following-sibling::*|"
                                       "//*[contains(text(),'Career Opportunities')]/../../../../../following-sibling::*").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            print("item['career_en'] = ", item['career_en'])

            assessment_en = response.xpath(
                "//*[contains(text(),'Learning, teaching & assessment')]/../../../../../following-sibling::*|"
                "//*[contains(text(),'Learning, Teaching & Assessment')]/../../../../../following-sibling::*|"
                "//*[contains(text(),'Learning, Teaching and Assessment')]/../../../../../following-sibling::*|"
                "//*[contains(text(),'Learning, teaching and assessment')]/../../../../../following-sibling::*|"
                "//*[contains(text(),'Learning, teaching and assessments')]/../../../../../following-sibling::*|"
                "//*[contains(text(),'Learning, teaching & assesment')]/../../../../../following-sibling::*").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            print("item['assessment_en'] = ", item['assessment_en'])

            # //*[contains(text(),'How To Apply')]/../../../../../following-sibling::div[1]
            apply_proces_en = response.xpath(
                "//*[contains(text(),'How To Apply')]/../../../../../following-sibling::div[1]").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(apply_proces_en))
            print("item['apply_proces_en'] = ", item['apply_proces_en'])

            tuition_fee = response.xpath(
                "//*[contains(text(),'Fees')]/../../../../../following-sibling::*//text()|"
                "//*[contains(text(),'fees')]/../../../../../following-sibling::*//text()").extract()
            if len(tuition_fee) == 0:
                tuition_fee = response.xpath("//strong[contains(text(),'Fees:')]/../following-sibling::*[1]//text()").extract()
            clear_space(tuition_fee)
            tuition_fee_str = ''.join(tuition_fee)
            # print("tuition_fee_str: ", tuition_fee_str)
            tuition_fee_re = re.findall(r"Overseas\sStudents\sFull-time\sfees\sper\syear:\s£\d+,\d+|International.*?£\d+,\d+|non-EU.*?£\d+,\d+|MSc.*?£\d+,\d+|entry:£\d+,\d+|2018/2019:£\d+,\d+|£\d+,\d+\sfor\sOutside\sEU", tuition_fee_str, re.I)
            # print(tuition_fee_re)
            if len(tuition_fee_re) != 0:
                t = re.findall(r"\d+,\d+",''.join(tuition_fee_re))
                # item['tuition_fee'] = int(''.join(t).replace(",", "").strip())
                # print("item['tuition_fee']1 = ", item['tuition_fee'])
                item['tuition_fee'] = getTuition_fee(''.join(tuition_fee_re))
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee'] = ", item['tuition_fee'])
            print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])

            rntry_requirements = response.xpath(
                "//*[contains(text(),'Entry requirements & fees')]/../../../../../following-sibling::*//text()|"
                "//*[contains(text(),'Entry Requirements & Fees')]/../../../../../following-sibling::*//text()|"
                "//*[contains(text(),'Key information for applicants & entry requirements')]/../../../../../following-sibling::*//text()|"
                "//*[contains(text(),'Entry requirements')]/../../../../../following-sibling::*//text()|"
                "//*[contains(text(),'Entry Requirements')]/../../../../../following-sibling::*//text()").extract()
            start_date = rntry_requirements
            item['rntry_requirements'] = clear_lianxu_space(rntry_requirements)
            # print("item['rntry_requirements'] = ", item['rntry_requirements'])

            duration = response.xpath(
                "//*[contains(text(),'Duration')]/following-sibling::*//text()|"
                "//*[contains(text(),'Duration')]/..//text()").extract()
            if len(duration) == 0:
                duration = response.xpath("//*[contains(text(),'Duration of course')]/../following-sibling::*[1]//text()").extract()
            if len(duration) == 0:
                duration = start_date
            clear_space(duration)

            duration_str = ''.join(duration)
            # print("duration_str: ", duration_str)
            duration_list = getIntDuration(duration_str)

            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            print("item['duration']: ", item['duration'])
            print("item['duration_per']: ", item['duration_per'])

            clear_space(start_date)
            start_date_str = '; '.join(start_date)
            # print("start_date_str: ", start_date_str)
            start_date_re = re.findall(r'Start.{1,25}', start_date_str)
            # print("start_date_re", start_date_re)
            item['start_date'] = getStartDate(''.join(start_date_re))
            print("item['start_date']: ", item['start_date'])

            # ielts_desc = ' '.join(start_date)
            # ielts_desc = re.findall(r'.{1,80}IELTS.{1,80}', ielts_desc)
            # print("ielts_desc: ", ielts_desc)
            allcontent = response.xpath(
                "//div[@class='tabbed-zone-outer oAccordionPanels tabbed-zone-sigma']//text() | //div[@class='tabbed-zone-outer oAccordionPanels tabbed-zone-rho']//text() | //div[@class='tabbed-zone-outer oAccordionPanels tabbed-zone-delta']//text() | //div[@class='tabbed-zone-outer oAccordionPanels tabbed-zone-sigma'][2]//text() | //div[@class='tabbed-zone-outer oAccordionPanels tabbed-zone-upsilon']//text()").extract()
            clear_space(allcontent)
            department_1 = response.xpath("//a[@href='/study/postgraduate/taught-programmes/abs/']//text()|"
                                          "//*[contains(text(),'Life & Health Sciences')]//text()|"
                                          "//*[contains(text(),'Engineering & Applied Science')]//text()|"
                                          "//*[contains(text(),'Languages & Social Sciences')]//text()").extract()
            print(department_1)
            if len(department_1) > 0:
                item['department'] = ''.join(department_1[0]).strip()
            department_re = re.findall(r"Life\s&\sHealth\sSciences\s-\sOSPAP|Aston\sBusiness\sSchool|Engineering\s&\sApplied\sScience|Languages\s&\sSocial\sSciences|Life\s&\sHealth\sSciences", ''.join(allcontent))
            print("department_re: ", department_re)
            if item['department'] == "":
                if len(department_re) > 0:
                    item['department'] = ''.join(department_re[0]).strip()
            print("item['department']: ", item['department'])

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

            if 'business' in item['programme_en'].lower():
                item['department'] = "Aston Business School"
            if 'electrical' in item['programme_en'].lower() or 'engineering' in item['programme_en'].lower():
                item['department'] = "Engineering & Applied Science"
            print("item['department']2: ", item['department'])
            if item['department'] == "Aston Business School" or item['department'] == "Languages & Social Sciences":
                item['ielts'] = 6.5
                item['ielts_l'] = 6
                item['ielts_s'] = 6.5
                item['ielts_r'] = 6
                item['ielts_w'] = 6.5
            elif item['department'] == "Engineering & Applied Science" or item['department'] == "Life & Health Sciences":
                item['ielts'] = 6.5
                item['ielts_l'] = 6
                item['ielts_s'] = 6
                item['ielts_r'] = 6
                item['ielts_w'] = 6
            print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                            item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            if item['department'] == "Aston Business School" or item['department'] == "Languages & Social Sciences":
                item['toefl'] = 93
                item['toefl_l'] = 19
                item['toefl_r'] = 18
                item['toefl_s'] = 22
                item['toefl_w'] = 26
            elif item['department'] == "Engineering & Applied Science" or item['department'] == "Life & Health Sciences":
                item['toefl'] = 93
                item['toefl_l'] = 19
                item['toefl_r'] = 18
                item['toefl_s'] = 19
                item['toefl_w'] = 23
            print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
                                                item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))
            yield item
        except Exception as e:
            with open(item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)
