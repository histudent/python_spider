import scrapy
import re
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space, clear_space_str
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.getIELTS import get_ielts
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getDuration import getIntDuration, getTeachTime
import requests
from lxml import etree

class UniversityOfSurrey_PSpider(scrapy.Spider):
    name = "UniversityOfSurrey_P"
    start_urls = ["https://www.surrey.ac.uk/postgraduate"]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3472.3 Safari/537.36"}

    def parse(self, response):
        links = response.xpath("//div[@class='view-content']/div//a/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))
        links = ["https://www.surrey.ac.uk/postgraduate/acting-mfa-2018",
"https://www.surrey.ac.uk/postgraduate/investment-management-msc-2018",
"https://www.surrey.ac.uk/postgraduate/advanced-geotechnical-engineering-msc-2018",
"https://www.surrey.ac.uk/postgraduate/information-security-msc-2018",
"https://www.surrey.ac.uk/postgraduate/social-research-methods-msc-2018",
"https://www.surrey.ac.uk/postgraduate/public-health-practice-scphn-school-nursing-msc-2018",
"https://www.surrey.ac.uk/postgraduate/air-transport-management-msc-2018",
"https://www.surrey.ac.uk/postgraduate/operations-and-supply-chain-digital-era-msc-2018",
"https://www.surrey.ac.uk/postgraduate/business-administration-mba-2018",
"https://www.surrey.ac.uk/postgraduate/stage-and-production-management-ma-2018",
"https://www.surrey.ac.uk/postgraduate/criminology-and-social-research-corporate-crime-and-corporate-responsibility-msc-2018",
"https://www.surrey.ac.uk/postgraduate/international-hotel-management-msc-2018",
"https://www.surrey.ac.uk/postgraduate/leadership-and-healthcare-msc-2018",
"https://www.surrey.ac.uk/postgraduate/music-performance-mmus-2018",
"https://www.surrey.ac.uk/postgraduate/acting-ma-2018",
"https://www.surrey.ac.uk/postgraduate/human-resources-management-msc-2018",
"https://www.surrey.ac.uk/postgraduate/process-and-environmental-systems-engineering-msc-2018",
"https://www.surrey.ac.uk/postgraduate/communication-and-international-marketing-ma-2018",
"https://www.surrey.ac.uk/postgraduate/primary-and-community-care-district-nursing-msc-2018",
"https://www.surrey.ac.uk/postgraduate/music-composition-mmus-2018",
"https://www.surrey.ac.uk/postgraduate/strategic-hotel-management-msc-2018",
"https://www.surrey.ac.uk/postgraduate/international-economics-finance-and-development-msc-2018",
"https://www.surrey.ac.uk/postgraduate/creative-writing-mfa-2018",
"https://www.surrey.ac.uk/postgraduate/chemistry-mres-2018",
"https://www.surrey.ac.uk/postgraduate/criminology-and-social-research-cybercrime-and-cybersecurity-msc-2018",
"https://www.surrey.ac.uk/postgraduate/economics-ma-2018",
"https://www.surrey.ac.uk/postgraduate/international-financial-management-msc-2018",
"https://www.surrey.ac.uk/postgraduate/water-and-environmental-engineering-msc-2018",
"https://www.surrey.ac.uk/postgraduate/structural-engineering-msc-2018",
"https://www.surrey.ac.uk/postgraduate/mathematics-msc-2018",
"https://www.surrey.ac.uk/postgraduate/entrepreneurship-msc-2018",
"https://www.surrey.ac.uk/postgraduate/environmental-strategy-msc-2018",
"https://www.surrey.ac.uk/postgraduate/infrastructure-engineering-and-management-msc-2018",
"https://www.surrey.ac.uk/postgraduate/public-health-practice-scphn-health-visiting-msc-2018",
"https://www.surrey.ac.uk/postgraduate/criminology-and-social-research-msc-2018",
"https://www.surrey.ac.uk/postgraduate/international-events-management-msc-2018",
"https://www.surrey.ac.uk/postgraduate/corporate-environmental-management-msc-2018",
"https://www.surrey.ac.uk/postgraduate/physics-msc-2018",
"https://www.surrey.ac.uk/postgraduate/music-musicology-mmus-2018",
"https://www.surrey.ac.uk/postgraduate/economics-msc-2018",
"https://www.surrey.ac.uk/postgraduate/musical-theatre-ma-2018",
"https://www.surrey.ac.uk/postgraduate/veterinary-microbiology-msc-2018",
"https://www.surrey.ac.uk/postgraduate/music-creative-practice-mmus-2018",
"https://www.surrey.ac.uk/postgraduate/information-systems-msc-2018",
"https://www.surrey.ac.uk/postgraduate/medical-physics-msc-2018",
"https://www.surrey.ac.uk/postgraduate/civil-engineering-msc-2018",
"https://www.surrey.ac.uk/postgraduate/international-hospitality-management-euromasters-msc-2018",
"https://www.surrey.ac.uk/postgraduate/business-economics-and-finance-msc-2018",
"https://www.surrey.ac.uk/postgraduate/developmental-psychology-research-and-practice-msc-2018",
"https://www.surrey.ac.uk/postgraduate/petroleum-refining-systems-engineering-msc-2018",
"https://www.surrey.ac.uk/postgraduate/economics-and-finance-msc-2018",
"https://www.surrey.ac.uk/postgraduate/bridge-engineering-msc-2018",
"https://www.surrey.ac.uk/postgraduate/nuclear-science-and-applications-msc-2018",
"https://www.surrey.ac.uk/postgraduate/advanced-materials-msc-2018",
"https://www.surrey.ac.uk/postgraduate/teaching-english-speakers-other-languages-tesol-ma-2018",
"https://www.surrey.ac.uk/postgraduate/accounting-and-finance-msc-2018",
"https://www.surrey.ac.uk/postgraduate/international-tourism-management-msc-2018",
"https://www.surrey.ac.uk/postgraduate/musical-theatre-mfa-2018",
"https://www.surrey.ac.uk/postgraduate/international-business-management-msc-2018",
"https://www.surrey.ac.uk/postgraduate/health-psychology-msc-2018",
"https://www.surrey.ac.uk/postgraduate/primary-and-community-care-community-childrens-nursing-msc-2018",
"https://www.surrey.ac.uk/postgraduate/international-commercial-law-llm-2018",
"https://www.surrey.ac.uk/postgraduate/healthcare-practice-msc-2018",
"https://www.surrey.ac.uk/postgraduate/corporate-finance-msc-2018",
"https://www.surrey.ac.uk/postgraduate/social-psychology-msc-2018",
"https://www.surrey.ac.uk/postgraduate/biomedical-engineering-msc-2018",
"https://www.surrey.ac.uk/postgraduate/creative-writing-ma-2018",
"https://www.surrey.ac.uk/postgraduate/psychology-conversion-msc-2018",
"https://www.surrey.ac.uk/postgraduate/english-literature-ma-2018",
"https://www.surrey.ac.uk/postgraduate/primary-and-community-care-general-practice-nursing-msc-2018", ]
        for link in links:
            # url = "https://www.surrey.ac.uk" + link
            # print(url)
            url = link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "University of Surrey"
        item['url'] = response.url
        # 授课方式
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        print("===============================")
        print(response.url)
        try:

            # 专业、学位类型
            programme_en = response.xpath("//h1[@class='text-center my-0']//text()").extract()
            programme_en_list = ''.join(programme_en).split("\n")
            # print(programme_en_list)
            if len(programme_en_list) > 1:
                item['programme_en'] = programme_en_list[0].strip()
                item['degree_name'] = ''.join(programme_en_list[1:]).strip()
            print("item['programme_en'] = ", item['programme_en'])
            print("item['degree_name'] = ", item['degree_name'])

            overview = response.xpath(
                "//h3[@class='px-3 pt-1 text-white'][contains(text(),'Course facts')]/../preceding-sibling::*").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en'] = ", item['overview_en'])

            teach_time = response.xpath("//td[@headers='view-field-study-mode-table-column'][contains(text(),'Full-time')]//text()").extract()
            item['teach_time'] = getTeachTime(''.join(teach_time))
            # print("item['teach_time'] = ", item['teach_time'])

            duration = response.xpath("//td[@headers='view-field-study-mode-table-column'][contains(text(),'Full-time')]/following-sibling::*[1]//text()").extract()
            clear_space(duration)
            # print(duration)
            if len(duration) != 0:
                duration_list = getIntDuration(''.join(duration))
                # print("duration_list: ", duration_list)
                if len(duration_list) == 2:
                    item['duration'] = duration_list[0]
                    item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            start_date = response.xpath(
                "//td[@headers='view-field-study-mode-table-column'][contains(text(),'Full-time')]/following-sibling::*[last()]//text()").extract()
            # print("start_date: ", start_date)
            item['start_date'] = getStartDate(''.join(start_date))
            # print("item['start_date'] = ", item['start_date'])

            item['location'] ='01SE01, Senate House, University of Surrey, Guildford, Surrey GU2 7XH'
            # print("item['location'] = ", item['location'])


            career = response.xpath("//h2[contains(text(),'Professional development')]/preceding-sibling::*[1]/following-sibling::*[position()<last()-1]|"
                                    "//h2[contains(text(),'Professional recognition')]|//h2[contains(text(),'Professional recognition')]/following-sibling::*[position()<3]|"
                                    "//h2[contains(text(),'Careers')]|//h2[contains(text(),'Careers')]/following-sibling::*[position()<3]|"
                                    "//h2[contains(text(),'Industrial placement')]|//h2[contains(text(),'Industrial placement')]/following-sibling::*[position()<4]").extract()
            if len(career) == 0:
                career = response.xpath("//h2[contains(text(),'Career prospects')]/preceding-sibling::*[1]/following-sibling::*[position()<last()-1]").extract()
                if len(career) == 0:
                    career = response.xpath(
                        "//h2[contains(text(),'Graduate prospects')]/preceding-sibling::*[1]/following-sibling::*[position()<last()-1]").extract()
            # print(career)
            item['career_en'] = remove_class(clear_lianxu_space(career))
            print("item['career_en'] = ", item['career_en'])

            modules = response.xpath("//div[@class='module-list']/preceding-sibling::*").extract()
            modules1 = response.xpath("//div[@id='modules-ft']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules)) + remove_class(clear_lianxu_space(modules1))
            if item['modules_en'] == "":
                item['modules_en'] = remove_class(clear_lianxu_space(response.xpath("//h2[contains(text(),'Modules')]/following-sibling::p[position()<3]").extract()))
            # print("item['modules_en'] = ", item['modules_en'])

            entry_requirements = response.xpath("//div[@id='entry-collapse']/*//text()").extract()
            item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements'] = ", item['rntry_requirements'])

            ielts_str = response.xpath("//h2[contains(text(),'English language requirements')]/following-sibling::p[position()<4]//text()").extract()
            ielts_re = re.findall(r"^IELTS.{1,80}", ''.join(ielts_str))
            # print(ielts_re)
            item['ielts_desc'] = ''.join(ielts_re)

            ieltsDict = get_ielts(item['ielts_desc'])
            item['ielts'] = ieltsDict.get("IELTS")
            item['ielts_l'] = ieltsDict.get("IELTS_L")
            item['ielts_s'] = ieltsDict.get("IELTS_S")
            item['ielts_r'] = ieltsDict.get("IELTS_R")
            item['ielts_w'] = ieltsDict.get("IELTS_W")
            # print("item['IELTS'] = %sitem['IELTS_L'] = %sitem['IELTS_S'] = %sitem['IELTS_R'] = %sitem['IELTS_W'] = %s==" % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            tuition_fee = response.xpath("//div[@id='fees-collapse']//td[@headers='view-field-study-mode-table-column--2'][contains(text(),'Full-time')]/following-sibling::*[last()]//text()").extract()
            # print(tuition_fee)
            if len(tuition_fee) > 0 and "£" in "".join(tuition_fee):
                item['tuition_fee'] = int(''.join(tuition_fee[0]).replace("£", "").replace(",", "").strip())
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee'] = ", item['tuition_fee'])
            print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])

            how_to_apply_url = response.xpath(
                "//span[@class='studymode'][contains(text(), 'Full-time')]/following-sibling::span[@class='applink']/a/@href").extract()
            # print(how_to_apply_url)
            if len(how_to_apply_url) > 0:
                how_to_apply_url = ''.join(how_to_apply_url[0])
                # print(how_to_apply_url)
                item['apply_proces_en'] = self.parse_apply_proces_en(how_to_apply_url)
            print("item['apply_proces_en'] = ", item['apply_proces_en'])

            # https://www.surrey.ac.uk/china/entry-requirements
            item['require_chinese_en'] = """<h2>Postgraduate</h2>
<p>To apply for one of our postgraduate courses that require a UK 2:1, you must achieve between 75-85% overall.</p>
<p>For courses that require a UK 2:2, you must achieve between 70-80% overall.</p>
<p>For courses that require a UK first-class degree to be eligible for a scholarship, you must achieve between 80-90% overall.</p>
"""

            department_dict = {}
            department1_list = ["Criminology", "Criminology and Sociology", "Law with Criminology", "Media, Culture and Society", "Media Studies with Film Studies", "Politics and Sociology", "Sociology", "Criminology and Social Research", "Criminology and Social Research (Corporate Crime and Corporate Responsibility)", "Criminology and Social Research (Cybercrime and Cybersecurity)", "Social Research Methods", "Sociology", "Economics", "Business Economics", "Economics and Finance", "Economics and thetics", "Economics", "Business Economics and Finance", "Economics", "Economics and Finance", "International Economics, Finance and Development", "Economics (Four Year)", "Law", "Law with Criminology", "Law with International Relations", "International Commercial Law", "Law", "Accounting and Finance", "Business and Retail nagement", "Business nagement", "Business nagement (Entrepreneurship)", "Business nagement (HRM)", "Business nagement (rketing)", "International Business nagement", "Accounting and Finance", "Business Administration", "Business Analytics", "Corporate Finance", "Entrepreneurship", "Hun Resources nagement", "International Business nagement", "International Financial nagement", "International rketing nagement", "International Retail rketing in the Digital Environment", "Investment nagement", "nagement Education", "rketing nagement", "Occupational and Organizational Psychology", "Operations and Supply Chain in the Digital Era", "nagement and Business", "Creative Music Technology", "Digital Media Arts", "Film and Video Production Technology", "Music", "Music and Sound Recording (Tonmeister)", "Music (Composition)", "Music (Conducting)", "Music (Creative Practice)", "Music (Musicology)", "Music (Perfornce)", "Digital Media Arts", "Music", "Sound Recording", "English Literature with Politics", "International Relations", "Politics", "Politics and Economics", "Politics and Sociology", "Public Affairs", "International Relations", "Public Affairs", "International Event nagement", "International Hospitality and Tourism nagement", "International Hospitality nagement", "International Tourism nagement", "Air Transport nagement", "International Events nagement", "International Events nagement (Eurosters)", "Eurosters", "International Hospitality nagement (Eurosters)", "International Hotel nagement", "International Tourism nagement", "International Tourism nagement (Eurosters)", "Eurosters", "Strategic Hotel nagement", "Strategic Tourism nagement and rketing", "Hospitality and Tourism nagement", "English Literature", "English Literature and French", "English Literature and Gern", "English Literature and Spanish", "English Literature with Creative Writing", "English Literature with Film Studies", "English Literature with Politics", "English Literature with Sociology", "Creative Writing", "Creative Writing", "English Literature", "Creative Writing", "English Literature", "Business nagement and French", "Business nagement and Gern", "Business nagement and Spanish", "English Literature and French", "English Literature and Gern", "English Literature and Spanish", "Modern Languages (French and Gern)", "Modern Languages (French and Spanish)", "Modern Languages (Gern and Spanish)", "Communication and International rketing", "Intercultural Communication with International Business", "Interpreting", "Interpreting (Chinese Pathway)", "Teaching English to Speakers of Other Languages (TESOL)", "Translation", "Translation and Interpreting", "Translation and Interpreting Studies", "Film Studies", "Linguistics", "Literary and Cultural Studies", "Translation and Interpreting", "Acting", "Actor-Musician", "Dance", "Musical Theatre", "Theatre", "Theatre and Perfornce", "Theatre Production", "Acting", "Musical Theatre", "Stage and Production nagement", "Theatre", "Acting", "Musical Theatre", "Dance", "Theatre",]
            department1_list = list(set(department1_list))
            department1_value = "Faculty of Arts and Social Sciences"
            for d in department1_list:
                department_dict[d.lower()] = department1_value

            department2_list = ["Practitioner Doctorate in Sustainability", "Environment and Sustainability", "Corporate Environmental Management", "Environmental Strategy", "Sustainable Development", "Chemistry", "Chemistry", "Chemistry", "Chemistry with Forensic Investigation", "Medicinal Chemistry", "Mathematics", "Mathematics with Statistics", "Mathematics with Music", "Financial Mathematics", "Mathematics and Physics", "Economics and Mathematics", "Mathematics", "Mathematics and Physics", "Physics", "Physics with Astronomy", "Physics with Nuclear Astrophysics", "Physics with Quantum Technologies", "Medical Physics", "Nuclear Science and Applications", "Physics", "Radiation and Environmental Protection", "Physics", "Information Systems", "Information Security", "Advanced Materials", "Biomedical Engineering",]
            department2_list = list(set(department2_list))
            department2_value = "Faculty of Engineering and Physical Sciences"
            for d in department2_list:
                department_dict[d.lower()] = department2_value

            department3_list = ["Nutrition", "Nutrition and Dietetics", "Nutrition and Food Science", "Human Nutrition", "Nutritional Medicine", "International English Language Testing System (IELTS)", "Developmental Psychology in Research and Practice", "Health Psychology", "Psychology (Conversion)", "Primary and Community Care (SPA Community Children's Nursing)", "Primary and Community Care (SPA District Nursing)", "Primary and Community Care (SPA General Practice Nursing)", "Public Health Practice (SCPHN Health Visiting)", "Public Health Practice (SCPHN School Nursing)", "Advanced Clinical Practice", "Advanced Practitioner (Primary and Community Care)", "Advanced Practitioner (Public Health Practice)", "Education for Health Professionals", "Education for Professional Practice", "Healthcare Practice", "Leadership and Healthcare", "Physician Associate", "Primary and Community Care (SPA Community Children's Nursing)", "Primary and Community Care (SPA District Nursing)", "Primary and Community Care (SPA General Practice Nursing)", "Public Health Practice (SCPHN Health Visiting)", "Public Health Practice (SCPHN School Nursing)",]
            department3_list = list(set(department3_list))
            department3_value = "Faculty of Health and Medical Sciences"
            for d in department3_list:
                department_dict[d.lower()] = department3_value

            item['department'] = department_dict.get(item['programme_en'].lower())
            print("item['department: ", item['department'])
            yield item
        except Exception as e:
            with open(item['university'] + str(item['degree_type']) + ".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_apply_proces_en(self, how_to_apply_url):
        data = requests.get(how_to_apply_url, headers=self.headers)
        response = etree.HTML(data.text)
        # print(response)
        apply_proces_en = response.xpath("//div[@class='layout-row intro summary']")
        # 将Element转换成HTML格式
        apply = ""
        if len(apply_proces_en) > 0:
            apply = etree.tostring(apply_proces_en[0], encoding='unicode', pretty_print=False, method='html')
        else:
            apply = how_to_apply_url
        apply = remove_class(clear_space_str(apply))
        return apply

