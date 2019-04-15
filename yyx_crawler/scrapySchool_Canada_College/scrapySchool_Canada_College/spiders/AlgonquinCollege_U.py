__author__ = 'yangyaxia'
__date__ = '2018/12/20 11:14'
import scrapy
import re
from scrapySchool_Canada_College.getItem import get_item
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from w3lib.html import remove_tags
from lxml import etree
import requests

class AlgonquinCollege_USpider(scrapy.Spider):
    name = "AlgonquinCollege_U"
    # 五个校区的专业列表链接
    # start_urls = ["https://www.algonquincollege.com/future-students/programs/credential/"]
    start_urls = ["http://www.algonquincollege.com/mediaanddesign/program/advertising/",
"http://www.algonquincollege.com/mediaanddesign/program/animation/",
"http://www.algonquincollege.com/healthandcommunity/program/applied-museum-studies/",
"http://www.algonquincollege.com/acce/program/architectural-technology/",
"http://www.algonquincollege.com/sat/program/biotechnology-advanced/",
"http://www.algonquincollege.com/business/program/business-administration/",
"http://www.algonquincollege.com/healthandcommunity/program/child-and-youth-care/",
"http://www.algonquincollege.com/acce/program/civil-engineering-technology/",
"http://www.algonquincollege.com/sat/program/computer-engineering-technology-computing-science/",
"http://www.algonquincollege.com/sat/program/computer-systems-technology-security/",
"http://www.algonquincollege.com/healthandcommunity/program/dental-hygiene-3-years/",
"http://www.algonquincollege.com/acce/program/electrical-engineering-technology/",
"http://www.algonquincollege.com/mediaanddesign/program/game-development/",
"http://www.algonquincollege.com/mediaanddesign/program/graphic-design/",
"http://www.algonquincollege.com/healthandcommunity/program/massage-therapy/",
"http://www.algonquincollege.com/healthandcommunity/program/massage-therapy-intensive/",
"http://www.algonquincollege.com/sat/program/mechanical-engineering-technology/",
"http://www.algonquincollege.com/healthandcommunity/program/medical-radiation-technology/",
"http://www.algonquincollege.com/healthandcommunity/program/respiratory-therapy/",
"http://www.algonquincollege.com/sat/program/bachelor-of-automation-and-robotics/",
"http://www.algonquincollege.com/acce/program/bachelor-of-building-science-2-year-bridging-program-co-op/",
"http://www.algonquincollege.com/acce/program/bachelor-of-building-science-3-year-bridging-program-co-op/",
"http://www.algonquincollege.com/acce/program/bachelor-of-building-science/",
"http://www.algonquincollege.com/business/program/bachelor-of-commerce-e-supply-chain-management/",
"http://www.algonquincollege.com/healthandcommunity/program/bachelor-of-early-learning-and-community-development/",
"http://www.algonquincollege.com/hospitalityandtourism/program/bachelor-of-hospitality-and-tourism-management-5-term-bridging-program-co-op/",
"http://www.algonquincollege.com/hospitalityandtourism/program/bachelor-of-hospitality-and-tourism-management/",
"http://www.algonquincollege.com/healthandcommunity/program/bit-information-resource-management/",
"http://www.algonquincollege.com/mediaanddesign/program/bit-interactive-multimedia-and-design/",
"http://www.algonquincollege.com/sat/program/bit-photonics-and-laser-technology/",
"http://www.algonquincollege.com/sat/program/bit-network-technology/",
"http://www.algonquincollege.com/mediaanddesign/program/bachelor-of-interior-design/bridging-program/",
"http://www.algonquincollege.com/mediaanddesign/program/bachelor-of-interior-design/",
"http://www.algonquincollege.com/ppsi/program/bachelor-public-safety-honours/",
"http://www.algonquincollege.com/healthandcommunity/program/bachelor-of-science-in-nursing/",
"http://www.algonquincollege.com/pembroke/program/bachelor-of-science-in-nursing/",
"http://www.algonquincollege.com/sat/program/aircraft-maintenance-technician/",
"http://www.algonquincollege.com/pembroke/program/applied-nuclear-science-radiation-safety/",
"http://www.algonquincollege.com/acce/program/architectural-technician/",
"http://www.algonquincollege.com/acce/program/architectural-technician-weekend/",
"http://www.algonquincollege.com/sat/program/aviation-management-general-arts-and-science/",
"http://www.algonquincollege.com/hospitalityandtourism/program/baking-and-pastry-arts-management/",
"http://www.algonquincollege.com/mediaanddesign/program/broadcasting-radio/",
"http://www.algonquincollege.com/mediaanddesign/program/broadcasting-television/",
"http://www.algonquincollege.com/acce/program/building-construction-technician/",
"http://www.algonquincollege.com/pembroke/program/business/",
"http://www.algonquincollege.com/business/program/business-accounting/",
"http://www.algonquincollege.com/perth/program/business-agriculture/",
"http://www.algonquincollege.com/business/program/management-and-entrepreneurship/",
"http://www.algonquincollege.com/business/program/business-marketing/",
"http://www.algonquincollege.com/acce/program/cabinetmaking-and-furniture-technician/",
"http://www.algonquincollege.com/healthandcommunity/program/cardiovascular-technology/",
"http://www.algonquincollege.com/perth/program/carpentry-and-joinery-heritage/#admission",
"http://www.algonquincollege.com/ppsi/program/community-and-justice-services/",
"https://www.algonquincollege.com/perth/program/computer-programmer/",
"http://www.algonquincollege.com/sat/program/computer-programmer/",
"http://www.algonquincollege.com/pembroke/program/computer-systems-technician/",
"http://www.algonquincollege.com/sat/program/computer-systems-technician/",
"http://www.algonquincollege.com/acce/program/construction-engineering-technician/",
"http://www.algonquincollege.com/acce/program/construction-engineering-technician-weekend/",
"http://www.algonquincollege.com/hospitalityandtourism/program/culinary-management/",
"http://www.algonquincollege.com/healthandcommunity/program/developmental-services-worker/",
"http://www.algonquincollege.com/healthandcommunity/program/early-childhood-education/",
"http://www.algonquincollege.com/pembroke/program/early-childhood-education/",
"http://www.algonquincollege.com/perth/program/early-childhood-education/",
"http://www.algonquincollege.com/healthandcommunity/program/early-childhood-education-intensive/",
"http://www.algonquincollege.com/acce/program/electrical-engineering-technician/",
"http://www.algonquincollege.com/sat/program/electro-mechanical-engineering-technician-robotics/",
"http://www.algonquincollege.com/pembroke/program/environmental-technician/",
"http://www.algonquincollege.com/hospitalityandtourism/program/esthetician/",
"http://www.algonquincollege.com/healthandcommunity/program/fitness-and-health-promotion/",
"http://www.algonquincollege.com/pembroke/program/forestry-technician/",
"http://www.algonquincollege.com/generalarts/program/general-arts-and-science-january-start/",
"http://www.algonquincollege.com/generalarts/program/general-arts-and-science-year-ii/",
"http://www.algonquincollege.com/hospitalityandtourism/program/hairstyling/",
"http://www.algonquincollege.com/acce/program/heating-refrigeration-and-air-conditioning-technician/",
"http://www.algonquincollege.com/mediaanddesign/program/horticultural-industries/",
"http://www.algonquincollege.com/hospitalityandtourism/program/hospitality-hotel-restaurant-operations-management/",
"http://www.algonquincollege.com/mediaanddesign/program/illustration-and-concept-art/",
"http://www.algonquincollege.com/mediaanddesign/program/interactive-media-design/",
"http://www.algonquincollege.com/mediaanddesign/program/interior-decorating/",
"http://www.algonquincollege.com/sat/program/internet-applications-web-development/",
"http://www.algonquincollege.com/mediaanddesign/program/journalism/",
"http://www.algonquincollege.com/business/program/law-clerk/",
"http://www.algonquincollege.com/business/program/law-clerk-intensive/",
"http://www.algonquincollege.com/healthandcommunity/program/library-and-information-technician/",
"http://www.algonquincollege.com/sat/program/manufacturing-engineering-technician/",
"http://www.algonquincollege.com/mediaanddesign/program/mobile-application-design-and-development/",
"http://www.algonquincollege.com/sat/program/motive-power-technician/",
"http://www.algonquincollege.com/sat/program/motive-power-technician-diesel-equipment-truck/",
"http://www.algonquincollege.com/mediaanddesign/program/music-industry-arts/",
"http://www.algonquincollege.com/healthandcommunity/program/occupational-therapist-assistant-physiotherapist-assistant/",
"http://www.algonquincollege.com/business/program/office-administration-executive/",
"http://www.algonquincollege.com/pembroke/program/office-administration-executive/",
"http://www.algonquincollege.com/business/program/office-administration-medical/",
"http://www.algonquincollege.com/business/program/office-administration-legal/",
"http://www.algonquincollege.com/pembroke/program/outdoor-adventure/",
"http://www.algonquincollege.com/pembroke/program/outdoor-adventure-naturalist/",
"http://www.algonquincollege.com/ppsi/program/paramedic/",
"http://www.algonquincollege.com/mediaanddesign/program/photography/",
"http://www.algonquincollege.com/pembroke/program/police-foundations/",
"http://www.algonquincollege.com/perth/program/police-foundations/",
"http://www.algonquincollege.com/ppsi/program/police-foundations/",
"http://www.algonquincollege.com/acce/program/powerline-technician/",
"http://www.algonquincollege.com/healthandcommunity/program/practical-nursing/",
"http://www.algonquincollege.com/pembroke/program/practical-nursing/",
"http://www.algonquincollege.com/healthandcommunity/program/practical-nursing-ftn-foreign-trained-nurse/",
"http://www.algonquincollege.com/mediaanddesign/program/professional-writing/",
"http://www.algonquincollege.com/mediaanddesign/program/public-relations/",
"http://www.algonquincollege.com/healthandcommunity/program/recreation-and-leisure-services/",
"http://www.algonquincollege.com/healthandcommunity/program/social-service-worker/",
"http://www.algonquincollege.com/pembroke/program/social-service-worker/",
"http://www.algonquincollege.com/healthandcommunity/program/social-service-worker-intensive/",
"http://www.algonquincollege.com/hospitalityandtourism/program/tourism-and-travel/",
"http://www.algonquincollege.com/healthandcommunity/program/veterinary-technician/",
"http://www.algonquincollege.com/sat/program/water-and-waste-water-technician/",
"http://www.algonquincollege.com/business/program/accounting-and-financial-practice/",
"http://www.algonquincollege.com/ppsi/program/advanced-care-paramedic/",
"http://www.algonquincollege.com/mediaanddesign/program/brand-management/",
"http://www.algonquincollege.com/acce/program/building-automation-system-operations/",
"http://www.algonquincollege.com/acce/program/building-information-modeling-lifecycle-management/",
"http://www.algonquincollege.com/sat/program/business-intelligence-system-infrastructure/",
"http://www.algonquincollege.com/healthandcommunity/program/clinically-intensive-orientation-to-nursing-in-ontario/",
"http://www.algonquincollege.com/healthandcommunity/program/diagnostic-cardiac-sonography/",
"http://www.algonquincollege.com/healthandcommunity/program/diagnostic-medical-sonography/",
"http://www.algonquincollege.com/healthandcommunity/program/digital-health/",
"http://www.algonquincollege.com/sat/program/energy-management/",
"http://www.algonquincollege.com/sat/program/environmental-management-and-assessment/",
"http://www.algonquincollege.com/hospitalityandtourism/program/event-management/",
"http://www.algonquincollege.com/business/program/financial-services/",
"http://www.algonquincollege.com/hospitalityandtourism/program/food-and-nutrition-management/",
"http://www.algonquincollege.com/sat/program/geographic-information-systems/",
"http://www.algonquincollege.com/acce/program/green-architecture/",
"http://www.algonquincollege.com/business/program/human-resources-management/",
"http://www.algonquincollege.com/mediaanddesign/program/imm/",
"http://www.algonquincollege.com/mediaanddesign/program/interdisciplinary-studies-in-human-centered-design/",
"http://www.algonquincollege.com/business/program/international-business-management/",
"http://www.algonquincollege.com/business/program/marketing-management/",
"http://www.algonquincollege.com/business/program/marketing-research-and-business-intelligence/",
"http://www.algonquincollege.com/healthandcommunity/program/orientation-to-nursing-in-ontario-for-nurses/",
"http://www.algonquincollege.com/business/program/paralegal-graduate-certificate/",
"http://www.algonquincollege.com/business/program/project-management/",
"http://www.algonquincollege.com/sat/program/regulatory-affairs-sciences/",
"http://www.algonquincollege.com/hospitalityandtourism/program/retirement-communities-management/",
"http://www.algonquincollege.com/mediaanddesign/program/scriptwriting/",
"http://www.algonquincollege.com/hospitalityandtourism/program/spa-management/",
"http://www.algonquincollege.com/business/program/sport-business-management/",
"https://www.algonquincollege.com/languages/program/teachers-of-english-as-a-foreign-language-international/",
"https://www.algonquincollege.com/languages/program/teachers-of-english-as-a-second-foreign-language/",
"http://www.algonquincollege.com/sat/program/technical-writer/",
"http://www.algonquincollege.com/healthandcommunity/program/therapeutic-recreation/",
"http://www.algonquincollege.com/ppsi/program/victimology/", ]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaCollegeItem)
        item['school_name'] = "Algonquin College"
        item['url'] = response.url
        # print(response.status)
        print("===========================")
        print(response.url)

        # item['campus'] = ''
        # item['location'] = '11762 - 106 Street Edmonton, Alberta, Canada, T5G 2R1'

        item['other'] = """问题描述： 1.overview、modules、career空缺的是页面上没有"""



        # item['require_chinese_en'] = ''
        item['start_date'] = "2019-01,2019-05,2019-09"
        item['deadline'] = ""
        # https://www.algonquincollege.com/international/future-students-2018/admissions-apply/
        item['apply_pre'] = "CAD$"
        item['apply_fee'] = '95'
        try:
            major_name_en = response.xpath("//div[@class='program_title']/h1//text()|"
                                           "//span[@id='programNamePlain']//text()").extract()
            clear_space(major_name_en)
            if len(major_name_en) > 0:
                item['major_name_en'] = ''.join(major_name_en).strip()
            print("item['major_name_en']: ", item['major_name_en'])

            department = response.xpath("//div[@y='col-md-10 breadcrumb']//span[2]//text()|"
                                        "//div[@class='col-md-10 breadcrumb']//span[2]//text()").extract()
            clear_space(department)
            if len(department) > 0:
                item['department'] = ''.join(department).strip()
            # print("item['department']: ", item['department'])

            campus = response.xpath("//strong[contains(text(),'Campus:')]/following-sibling::*//text()").extract()
            clear_space(campus)
            if len(campus) > 0:
                item['campus'] = ''.join(campus).strip()
            # print("item['campus']: ", item['campus'])

            if item['campus'] == "Pembroke":
                item['location'] = "1 College Way Pembroke, Ontario K8A 0C8"
            elif item['campus'] == "Perth":
                item['location'] = "7 Craig Street Perth, Ontario K7H 1X7"
            elif item['campus'] == "Ottawa":
                item['location'] = "1385 Woodroffe Avenue Ottawa, Ontario K2G 1V8"

            programme_code = response.xpath("//strong[contains(text(),'Program Code:')]/following-sibling::*//text()").extract()
            clear_space(programme_code)
            if len(programme_code) > 0:
                item['programme_code'] = ''.join(programme_code).strip()
            # print("item['programme_code']: ", item['programme_code'])

            degree_name = response.xpath("//strong[contains(text(),'Credential:')]/following-sibling::*//text()").extract()
            clear_space(degree_name)
            # print("degree_name: ", degree_name)
            if len(degree_name) > 0:
                item['degree_name'] = ''.join(degree_name).replace("Ontario College", "").strip()
            # print("item['degree_name']: ", item['degree_name'])

            if item['degree_name'] is not None:
                if "diploma" in item['degree_name'].lower():
                    item['degree_level'] = 3
                elif "Graduate" in item['degree_name']:
                    item['degree_level'] = 2
                elif "Degree" in item['degree_name']:
                    if "Honours" in item['degree_name'] and "Honours" not in item['major_name_en']:
                        item['degree_name'] = "Honours " + item['major_name_en']
                    else:
                        item['degree_name'] = item['major_name_en']
                    item['degree_level'] = 1
            if "Bachelor of" in item['major_name_en'] and item['degree_name'] is None:
                item['degree_name'] = item['major_name_en']
                item['degree_level'] = 1
            print("item['degree_name']1: ", item['degree_name'])
            # print("item['degree_level']: ", item['degree_level'])

            # duration
            duration = response.xpath("//strong[contains(text(),'Duration:')]/following-sibling::*//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration_str = ''.join(duration).strip()

            duration_re = re.findall(r"[\d]+", duration_str)
            # print("duration_re: ", duration_re)
            item['duration'] = ''.join(duration_re)

            # 判断课程长度单位
            if "year" in ''.join(duration).lower():
                item['duration_per'] = 1
            if "month" in ''.join(duration).lower():
                item['duration_per'] = 3
            if "week" in ''.join(duration).lower():
                item['duration_per'] = 4
            # print("item['duration']: ", item['duration'])
            # print("item['duration_per']: ", item['duration_per'])


            overview = response.xpath(
                "//strong[contains(text(),'Bring Your Own Device (BYOD)')]/../preceding-sibling::*").extract()
            if len(overview) == 0:
                overview = response.xpath("//h3[contains(text(),'SUCCESS FACTORS')]/preceding-sibling::*|"
                                          "//h2[contains(text(),'Program Eligibility')]/preceding-sibling::*[position()<last()-1]|"
                                          "//strong[contains(text(),'Program Eligibility')]/../preceding-sibling::*[position()<last()-1]").extract()
            if len(overview) > 0:
                item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])

            modules = response.xpath(
                "//div[@id='courses']//*[@class='level-container']").extract()
            # print("modules_en: ", modules)
            if len(modules) > 0:
                item['modules_en'] = remove_class(clear_lianxu_space(modules)).replace("<div>Hours</div>", "").strip()
                print("item['modules_en']: ", item['modules_en'])

                del_key1 = re.findall(r"<p><span>.*?Read More</p>", item['modules_en'])
                print("del_key1: ", del_key1)
                del_key2 = re.findall(r"<p>[\d\.]+?</p>", item['modules_en'])
                print("del_key2: ", del_key2)

                if len(del_key1) > 0:
                    for d_k1 in del_key1:
                        item['modules_en'] = item['modules_en'].replace(d_k1, '').strip()
                if len(del_key2) > 0:
                    for d_k2 in del_key2:
                        item['modules_en'] = item['modules_en'].replace(d_k2, '').strip()
            print("item['modules_en']=== ", item['modules_en'])

            # print("item['modules_en']: ", item['modules_en'])

            career = response.xpath(
                "//h3[contains(text(),'Learning Outcomes')]/preceding-sibling::*").extract()
            if len(career) > 0:
                item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])


            entry_requirements_en = response.xpath(
                "//div[@id='application_admission']//div[@class='col-sm-8']").extract()
            if len(entry_requirements_en) > 0:
                item['entry_requirements_en'] = remove_class(clear_lianxu_space(entry_requirements_en))
            # print("item['entry_requirements_en']: ", item['entry_requirements_en'])

            # ielts = response.xpath("//p[contains(text(), 'IELT')]//text()").extract()
            # print("ielts: ", ielts)
            if item['entry_requirements_en'] is not None:
                ielts_list = re.findall(r"IELTS\-[\w\W]{1,120}", item['entry_requirements_en'])
                # print("ielts_list: ", ielts_list)
                if len(ielts_list) > 0:
                    item['ielts_desc'] = ielts_list[0]
                    ielts_dict = get_ielts(ielts_list[0])
                    item['ielts'] = ielts_dict.get("IELTS")
                    item['ielts_l'] = ielts_dict.get("IELTS_L")
                    item['ielts_s'] = ielts_dict.get("IELTS_S")
                    item['ielts_r'] = ielts_dict.get("IELTS_R")
                    item['ielts_w'] = ielts_dict.get("IELTS_W")

                toefl_list = re.findall(r"TOEFL\-Internet\-based[\w\W]{1,120}", item['entry_requirements_en'])
                # print("toefl_list: ", toefl_list)
                if len(toefl_list) > 0:
                    item['toefl_desc'] = toefl_list[0]

                if item['toefl_desc'] is not None:
                    toefl = re.findall(r"overall\s\d+", item['toefl_desc'], re.I)
                    # print("toefl: ", toefl)
                    toefl_ench = re.findall(r"\d+\sin each component", item['toefl_desc'], re.I)
                    # print("toefl_each: ", toefl_ench)

                    item['toefl'] = ''.join(toefl).lower().replace("overall", "").strip()
                    item['toefl_l'] = ''.join(toefl_ench).lower().replace("in each component", "").strip()
                    item['toefl_s'] = item['toefl_l']
                    item['toefl_r'] = item['toefl_l']
                    item['toefl_w'] = item['toefl_l']
            # print("item['ielts_desc']: ", item['ielts_desc'])
            # print("item['ielts']: ", item['ielts'])
            # print("item['ielts_l']: ", item['ielts_l'])
            # print("item['ielts_s']: ", item['ielts_s'])
            # print("item['ielts_r']: ", item['ielts_r'])
            # print("item['ielts_w']: ", item['ielts_w'])

            # print("item['toefl_desc']: ", item['toefl_desc'])
            # print("item['toefl']: ", item['toefl'])
            # print("item['toefl_l']: ", item['toefl_l'])
            # print("item['toefl_s']: ", item['toefl_s'])
            # print("item['toefl_r']: ", item['toefl_r'])
            # print("item['toefl_w']: ", item['toefl_w'])

            item['tuition_fee_per'] = "1"
            item['tuition_fee_pre'] = "CAD$"

            if item['degree_level'] == 3:
                item['require_chinese_en'] = """<p>Admission To Postsecondary Certificate or Diploma Program (1/2/3 years)</p>
<p>• One of the following:</p>
<p>    1. The National Senior High School Examination with a minimum grade of 65% or C in relevant subjects (School Leaving Certificate).</p>
<p>    2. Graduation Certificate awarded by senior (upper) middle school; may be academic or vocationally oriented with a minimum of C or 65% in relevant subjects.</p>
<p>    3. Matriculation Examination with a minimum mark of 490. </p>
<p>• English Proficiency requirements are as follows for consideration:</p>
<p>    1. A minimum TOEFL score of 80 (internet based with no single test score below 20) </p>
<p>    2. Or IELTS with an overall minimum score of 6.0 (with no single test score below 5.5) </p>
<p>    3. Or CAEL (Canadian Academic English Language Assessment) with an overall band score of 60</p>"""
            elif item['degree_level'] == 2:
                item['require_chinese_en'] = """<p>Admission To A Post Graduate Certificate Program (1 year)</p>
<p>• Bachelor’s degree and University transcripts</p>
<p>• English Proficiency requirements are as follows for consideration:</p>
<p>    1. A minimum TOEFL score of 88 (internet based with no single test score below 21) </p>
<p>    2. Or an IELTS with an overall minimum score of 6.5 (with no single test score below 6.0) </p>
<p>    3. Or CAEL with an overall band score of 70</p>"""
            elif item['degree_level'] == 1:
                item['require_chinese_en'] = """<p>Admission To Postsecondary Bachelor’s Degree Program (4 years)</p>
<p>• One of the following:</p>
<p>    1. The National Senior High School Examination with a minimum grade of 70% or B in relevant subjects (School Leaving Certificate).</p>
<p>    2. Graduation Certificate awarded by senior (upper) middle school; may be academic or vocationally oriented with a minimum of B or 70% in relevant subjects.</p>
<p>    3. Matriculation Examination with a minimum mark of 525. Include transcripts for any postsecondary courses or programs completed</p>
<p>• Include transcripts for any post-secondary courses or programs completed</p>
<p>• English Proficiency requirements are as follows for consideration:</p>
<p>    1. A minimum TOEFL score of 88 (internet based with no single test score below 21) </p>
<p>    2. Or an IELTS with an overall minimum score of 6.5 (with no single test score below 6.0) </p>
<p>    3. Or CAEL with an overall band score of 70</p>"""

            if item['degree_level'] == 3 and item['ielts'] is None:
                item['ielts'] = '6.0'
                item['ielts_l'] = '5.5'
                item['ielts_s'] = '5.5'
                item['ielts_r'] = '5.5'
                item['ielts_w'] = '5.5'
            elif item['degree_level'] == 2 and item['ielts'] is None or item['degree_level'] == 1 and item['ielts'] is None:
                item['ielts'] = '6.5'
                item['ielts_l'] = '6.0'
                item['ielts_s'] = '6.0'
                item['ielts_r'] = '6.0'
                item['ielts_w'] = '6.0'

            if item['degree_level'] == 3 and item['toefl'] is None:
                item['toefl'] = '80'
                item['toefl_l'] = '20'
                item['toefl_s'] = '20'
                item['toefl_r'] = '20'
                item['toefl_w'] = '20'
            elif item['degree_level'] == 2 and item['toefl'] is None or item['degree_level'] == 1 and item['toefl'] is None:
                item['toefl'] = '88'
                item['toefl_l'] = '21'
                item['toefl_s'] = '21'
                item['toefl_r'] = '21'
                item['toefl_w'] = '21'

            fee_url = response.xpath("//a[contains(text(),'Tuition and Fee Estimator')]/@href").extract()
            # print("fee_url: ", fee_url)
            if len(fee_url) > 0:
                fee_url_tmp = 'https://www.algonquincollege.com' + ''.join(fee_url[0])
                fee_url_tmp = fee_url_tmp.replace("residency=canadian&", "residency=international&").strip()
                # print("fee_url_tmp: ", fee_url_tmp)
                # //ul[@id='ui-id-2']//span[@class='feeTitle'][contains(text(),'International Student Premium (PRG)')]/following-sibling::span[@class='feeValue']
                item['tuition_fee'] = self.parse_tuition_fee(fee_url_tmp)
            # print("item['tuition_fee']: ", item['tuition_fee'])


            yield item
        except Exception as e:
                with open("scrapySchool_Canada_College/error/" + item['school_name'] + ".txt", 'a', encoding="utf-8") as f:
                    f.write(str(e) + "\n" + response.url + "\n========================\n")
                print("异常：", str(e))
                print("报错url：", response.url)

    def parse_tuition_fee(self, fee_url_tmp):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(fee_url_tmp, headers=headers_base)
        response = etree.HTML(data.text)

        fee = response.xpath(
            "//ul[@class='feeSemester']//span[@class='feeTitle'][contains(text(),'International Student Premium (PRG)')]/following-sibling::span[@class='feeValue']//text()")
        clear_space(fee)
        # print("fee: ", fee)
        fee_str = None
        if len(fee) > 0:
            fee_str = ''.join(fee[0]).replace("$", "").strip()
        return fee_str

