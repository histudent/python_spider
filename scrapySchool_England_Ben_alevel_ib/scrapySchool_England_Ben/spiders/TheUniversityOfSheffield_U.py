# -*- coding: utf-8 -*-
import scrapy
import re, json, requests
from scrapySchool_England_Ben.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from w3lib.html import remove_tags
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getIELTS import get_ielts
from lxml import etree
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration

class TheUniversityOfSheffield_USpider(scrapy.Spider):
    name = "TheUniversityOfSheffield_U"
    start_urls = ["https://www.sheffield.ac.uk/prospectus/courses-az.do?prospectusYear=2019"]

    def parse(self, response):
        links = response.xpath("//table[@class='listTable']//tr/td[1]/a/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))
        for link in links:
            # print(link, "-----")
            if "http" not in link:
                url = "https://www.sheffield.ac.uk/prospectus/" + link
            else:
                url = link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "The University of Sheffield"
        # item['country'] = 'England'
        # item['website'] = 'https://www.sheffield.ac.uk'
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        item['location'] = "Western Bank, Sheffield, S10 2TN, UK"
        print("===========================")
        print(response.url)
        try:
            # 专业、学位类型
            programmeDegree_type = response.xpath(
                "//div[@class='titles']/h2//text()").extract()
            if len(programmeDegree_type) == 0:
                programmeDegree_type = response.xpath(
                    "//main[@class='main content']/h2[1]//text()").extract()
            programmeDegree_type = ''.join(programmeDegree_type).strip()
            print("programmeDegree_type: ", programmeDegree_type)
            degree_typeList = re.findall(r"[A-Za-z/\(\)]*$", programmeDegree_type)
            # print("degree_typeList: ", degree_typeList)
            programme = programmeDegree_type
            if len(degree_typeList) != 0:
                degree_type = ''.join(list(degree_typeList[0]))
                item['degree_name'] = degree_type
                programme = programmeDegree_type.replace(item['degree_name'], '')
            print("item['degree_name']: ", item['degree_name'])
            item['programme_en'] = ''.join(programme)
            print("item['programme_en']: ", item['programme_en'])

            # 学院
            department = response.xpath(
                "//div[@class='titles']//h3//text()").extract()
            clear_space(department)
            item['department'] = ''.join(department).strip()
            print("item['department']: ", item['department'])

            ucascode = response.xpath(
                "//span[@id='adCode']//text()").extract()
            clear_space(ucascode)
            if len(ucascode) > 0:
                item['ucascode'] = ''.join(ucascode[0]).strip()
            print("item['ucascode'] = ", item['ucascode'])

            # 课程长度
            durationContent = response.xpath(
                "//h3[contains(text(),'Course details')]/following-sibling::text()").extract()
            clear_space(durationContent)
            # print(durationContent)

            duration_list = getIntDuration(''.join(durationContent))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            # 专业描述
            overview = response.xpath("//div[@class='descHold']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])

            alevel = response.xpath(
                "//html//div[@id='courseSummary']//tr/td[contains(text(), 'A Levels')]/following-sibling::td//text()").extract()
            clear_space(alevel)
            if len(alevel) > 0:
                item['alevel'] = ''.join(alevel[0]).strip()
            # print("item['alevel'] = ", item['alevel'])

            ib = response.xpath(
                "//html//div[@id='courseSummary']//tr/td[contains(text(), 'International Baccalaureate')]/following-sibling::td//text()").extract()
            item['ib'] = ''.join(ib).strip()
            # print("item['ib'] = ", item['ib'])

            ielts_desc = response.xpath(
                "//*[contains(text(),'IELTS')]//text()").extract()
            clear_space(ielts_desc)
            item['ielts_desc'] = ''.join(ielts_desc)
            # print("item['ielts_desc']: ", item['ielts_desc'])

            ieltDict = get_ielts(item['ielts_desc'])
            item['ielts'] = ieltDict.get('IELTS')
            item["ielts_l"] = ieltDict.get('IELTS_L')  # float
            item["ielts_s"] = ieltDict.get('IELTS_S')  # float
            item["ielts_r"] = ieltDict.get('IELTS_R')  # float
            item["ielts_w"] = ieltDict.get('IELTS_W')
            # print("ielts = %s  ielts_l = %s  ielts_s = %s  ielts_r = %s  ielts_w = %s"%(
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            modules_en = response.xpath(
                "//div[@id='modules']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules_en))
            # print("item['modules_en']: ", item['modules_en'])

            assessment_en = response.xpath(
                "//div[@id='ltam']").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            career_en = response.xpath(
                "//div[@id='graduates']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            # print("item['career_en']: ", item['career_en'])

            # https://www.sheffield.ac.uk/prospectus/courseDetails.do?id=N1202019
            # # start_date //a[@href='#tab00']
            # start_date = response.xpath(
            #     "//table[@class='cms-tabs']/tbody/tr[last()]/th[1]//text()").extract()
            # clear_space(start_date)
            # start_date_str = ''.join(start_date).replace('start', '').replace('entry', '').strip()
            # # print(start_date_str)
            # start_date_1 = getStartDate(start_date_str)
            # print(start_date_1)
            # item['start_date'] = start_date_1
            # print("item['start_date']: ", item['start_date'])

            # //div[@id='tab00']
            # modules   评估方式


            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<h1>How to apply: applying essentials</h1>
    <p><img class="imgRight" alt="Undergraduates in a tutorial"   src="/polopoly_fs/1.550384!/image/undergraduates320.jpg" />This page provides key information about applying to study on an undergraduate course at Sheffield, and contains links to all of our procedures and Admissions policies. Please take the time to read this information before completing your application.</p>
    <h3>Before you apply</h3>
    <p>We normally expect applicants to offer three full A Levels or an accepted equivalent qualification. You can check the University's general entry requirements, including which UK and International qualifications we accept and our English language and mathematics requirements, on our Admissions requirements webpage:</p>
    <p><a  href="/undergraduate/apply/requirements">Admissions requirements</a></p>
    <p>You can find details of the entry requirements for particular courses in our online prospectus. Please note that these represent our typical offer conditions only – we may make different offers in some cases.</p>
    <p><a href="http://www.sheffield.ac.uk/prospectus">Online prospectus</a></p>
    <p>A full list of our formal policies relating to Admissions is available on our Policies webpages. This includes our Student Admissions Policy as well as policies on A Level subject combinations, resits, and qualifications taken early.</p>
    <p><a  href="/undergraduate/policies">Our policies</a></p>
    <h3>Applying</h3>
    <p>You can apply for an undergraduate course at Sheffield via UCAS (the Universities and Colleges Admissions Service):</p>
    <p><a href="http://www.ucas.com/apply">UCAS website – Apply</a></p>
    <p>Applications for places on courses starting the following September (except Medicine and Dentistry) should be submitted to UCAS between:</p>
    <ul>
        <li>1 September and 15 January to be guaranteed equal consideration with other applicants</li>
        <li>16 January and 30 June for further consideration, although we may not be able to consider your application if all the places on the course you have applied for have been filled</li>
    </ul>
    <p>Applications for places on Medicine and Dentistry courses must be submitted between 1 September and 15 October.</p>
    <p>You can find more information about how and when to apply on our Applying webpage. This also contains information about deferred entry, direct entry to year/level 2 and our foundation year courses.</p>
    <p><a  href="/undergraduate/apply/applying">Applying</a></p>
    <p>Our Education For All webpage provides information on the support we provide for Care Leavers, estranged students, carers, mature students and students with a disability or learning difficulty. You can also find information about our outreach activities, our use of contextual data and our Disrupted Studies scheme.</p>
    <p><a  href="/undergraduate/apply/wp">Education for all: Widening Participation and Disrupted Studies</a></p>
    <h3>After you apply</h3>
    <p>You can find out what happens after you have submitted your application on our <a  href="/undergraduate/apply/after">After You Apply</a> webpages. If we make you a Conditional offer and you accept us as either your Firm or Insurance choice, we will also send you an email containing information about what happens when you get your exam results.</p>
    <p><a  href="/undergraduate/apply/after">After you apply</a></p>
    <p>If at any time you find that your studies are&#160;affected by personal, social or domestic issues, please let us know by using our Disrupted Studies form:</p>
    <p><a  href="/undergraduate/apply/applying/disrupted">Disrupted Studies</a></p>
    <h3>Further information</h3>
    <p>If you have any further questions about the University and applying to study with us, please <a href="http://ask.sheffield.ac.uk">Ask Sheffield</a>.</p>
    <p>If you still need help, our Applicant Information Desk (AiD) provides a first point of contact for people who have applied to the University. AiD can help with any questions you have about the process of applying to us and the current status of your application.</p>
    <p><a  href="/aid">Applicant Information Desk</a></p>
    <p>We wish you the best of luck with your application.</p>"""]))
            item['require_chinese_en'] = ''

            tuition_feeDict = {"C180": "21450",
                               "C200": "21450",
                               "C300": "21450",
                               "C100": "21450",
                               "C109": "21450",
                               "C189": "21450",
                               "C209": "21450",
                               "C309": "21450",
                               "C1C9": "21450",
                               "C1CX": "21450",
                               "C1R9": "21450",
                               "C101": "21450",
                               "F400": "18900",
                               "FV41": "18900",
                               "VV46": "18900",
                               "VR47": "18900",
                               "VR41": "18900",
                               "VR42": "18900",
                               "F410": "18900",
                               "VR44": "18900",
                               "QV84": "18900",
                               "F401": "18900",
                               "KK13": "21450",
                               "K100": "21450",
                               "ARCU123": "21450",
                               "ARCU124": "21450",
                               "ARCU13": "21450",
                               "ARCU129": "21450",
                               "Y001": "16800",
                               "H130": "21450",
                               "G500": "21450",
                               "H690": "21450",
                               "H660": "21450",
                               "H310": "21450",
                               "H360": "21450",
                               "H361": "21450",
                               "H1NF": "21450",
                               "H1NF": "21450",
                               "HN62": "21450",
                               "OG31": "21450",
                               "8L16": "21450",
                               "57": "21450",
                               "2G36": "21450",
                               "8M74": "21450",
                               "2A47": "21450",
                               "H653": "21450",
                               "H659": "21450",
                               "B900": "21450",
                               "B909": "21450",
                               "H810": "21450",
                               "H800": "21450",
                               "H840": "21450",
                               "H8T9": "21450",
                               "H8F1": "21450",
                               "H8J7": "21450",
                               "H801": "21450",
                               "F100": "21450",
                               "F105": "21450",
                               "F107": "21450",
                               "F106": "21450",
                               "F335": "21450",
                               "F109": "21450",
                               "F108": "21450",
                               "C720": "21450",
                               "H210": "21450",
                               "HK21": "21450",
                               "H2T9": "21450",
                               "H200": "21450",
                               "H202": "21450",
                               "HK2D": "21450",
                               "H2N2": "21450",
                               "2H26": "21450",
                               "8T63": "21450",
                               "8L55": "21450",
                               "2G91": "21450",
                               "H201": "21450",
                               "A200": "21450",
                               "G600": "21450",
                               "G650": "21450",
                               "G402": "21450",
                               "G400": "21450",
                               "GG41": "21450",
                               "GG74": "21450",
                               "G4G1": "21450",
                               "G700": "21450",
                               "G490": "21450",
                               "G495": "21450",
                               "G401": "21450",
                               "G651": "21450",
                               "GN52": "21450",
                               "GN53": "21450",
                               "X301": "16800",
                               "F401": "18900",
                               "Q305": "16800",
                               "Q310": "16800",
                               "F901": "18900",
                               "L701": "18900",
                               "V101": "16800",
                               "Q307": "16800",
                               "V501": "16800",
                               "L301": "16800",
                               "L401": "16800",
                               "K401": "16800",
                               "K441": "16800",
                               "L790": "16800",
                               "QC19": "21450",
                               "B990": "21450",
                               "C801": "21450",
                               "V642": "16800",
                               "L432": "16800",
                               "T210": "16800",
                               "T300": "18900",
                               "TN42": "18900",
                               "T110": "16800",
                               "T415": "16800",
                               "TN12": "18900",
                               "T1T2": "16800",
                               "T4T2": "16800",
                               "T1R2": "16800",
                               "T2R2": "16800",
                               "T1R4": "16800",
                               "T2R4": "16800",
                               "T1R7": "16800",
                               "T2R7": "16800",
                               "T1R1": "16800",
                               "TV11": "16800",
                               "TV21": "16800",
                               "L100": "16800",
                               "LV15": "16800",
                               "LL12": "16800",
                               "L101": "16800",
                               "LG11": "16800",
                               "L1N3": "16800",
                               "LIN3": "16800",
                               "X300": "16800",
                               "X301": "16800",
                               "H620": "21450",
                               "H621": "21450",
                               "H610": "21450",
                               "H613": "21450",
                               "H614": "21450",
                               "H651": "21450",
                               "H647": "21450",
                               "H645": "21450",
                               "H6T9": "21450",
                               "H623": "21450",
                               "H615": "21450",
                               "H616": "21450",
                               "H652": "21450",
                               "H649": "21450",
                               "H622": "21450",
                               "H611": "21450",
                               "H648": "21450",
                               "H629": "21450",
                               "H628": "21450",
                               "H602": "21450",
                               "H603": "21450",
                               "H100": "21450",
                               "H104": "21450",
                               "H675": "21450",
                               "H673": "21450",
                               "H67I": "21450",
                               "H67H": "21450",
                               "Q3Q1": "16800",
                               "QL33": "16800",
                               "QR14": "16800",
                               "QR17": "16800",
                               "QR32": "16800",
                               "QR37": "16800",
                               "QV15": "16800",
                               "QT12": "16800",
                               "Q304": "16800",
                               "Q310": "16800",
                               "Q305": "16800",
                               "Q306": "16800",
                               "QR31": "16800",
                               "QV31": "16800",
                               "QW33": "16800",
                               "QV35": "16800",
                               "QR34": "16800",
                               "QW34": "16800",
                               "Q307": "16800",
                               "F309": "21450",
                               "G109": "21450",
                               "QR11": "16800",
                               "R120": "16800",
                               "RL11": "16800",
                               "RL12": "16800",
                               "RN12": "16800",
                               "RR12": "16800",
                               "RR14": "16800",
                               "RR17": "16800",
                               "RV11": "16800",
                               "RV15": "16800",
                               "RW13": "16800",
                               "R1R9": "16800",
                               "R1T2": "16800",
                               "R1R7": "16800",
                               "R1RR": "16800",
                               "R1RO": "16800",
                               "L700": "18900",
                               "F800": "18900",
                               "F902": "18900",
                               "F900": "18900",
                               "F901": "18900",
                               "QR12": "16800",
                               "R220": "16800",
                               "RL21": "16800",
                               "RL22": "16800",
                               "RN22": "16800",
                               "RR24": "16800",
                               "RR27": "16800",
                               "RV21": "16800",
                               "RV25": "16800",
                               "RW23": "18900",
                               "R2R9": "16800",
                               "R2T2": "16800",
                               "R2R7": "16800",
                               "R2RR": "16800",
                               "R2R3": "16800",
                               "R410": "16800",
                               "RL42": "16800",
                               "RN42": "16800",
                               "RL41": "16800",
                               "R4T2": "16800",
                               "R4R7": "16800",
                               "R4RR": "16800",
                               "V100": "16800",
                               "RV71": "16800",
                               "RV41": "16800",
                               "VV15": "16800",
                               "VL12": "16800",
                               "VL13": "16800",
                               "V1R9": "16800",
                               "V101": "16800",
                               "B620": "21450",
                               "QC18": "21450",
                               "QC19": "21450",
                               "P110": "18900",
                               "P500": "18900",
                               "K3K4": "18900",
                               "KC39": "18900",
                               "M100": "16800",
                               "ML94": "16800",
                               "M1R4": "16800",
                               "M1R2": "16800",
                               "M1R1": "16800",
                               "M930": "16800",
                               "M120": "16800",
                               "N200": "16800",
                               "N420": "16800",
                               "NG21": "16800",
                               "NG41": "16800",
                               "NL21": "16800",
                               "NL41": "16800",
                               "NP21": "16800",
                               "NP41": "16800",
                               "NT22": "16800",
                               "N120": "16800",
                               "JH51": "21450",
                               "J500": "21450",
                               "J5R9": "21450",
                               "FH21": "21450",
                               "J200": "21450",
                               "FHF1": "21450",
                               "H403": "21450",
                               "H401": "21450",
                               "JH5P": "21450",
                               "JH56": "21450",
                               "J501": "21450",
                               "G100": "18900",
                               "G103": "18900",
                               "GN13": "18900",
                               "G102": "18900",
                               "G1R4": "18900",
                               "G1R1": "18900",
                               "G1R2": "18900",
                               "G106": "18900",
                               "VG51": "18900",
                               "A100": "21450",
                               "T900": "16800",
                               "C400": "21450",
                               "C500": "21450",
                               "C440": "21450",
                               "C700": "21450",
                               "C741": "21450",
                               "CC45": "21450",
                               "CC74": "21450",
                               "CC75": "21450",
                               "C709": "21450",
                               "CC7C": "21450",
                               "CC79": "21450",
                               "C409": "21450",
                               "CC4C": "21450",
                               "C749": "21450",
                               "C509": "21450",
                               "C449": "21450",
                               "C790": "21450",
                               "C791": "21450",
                               "CC47": "21450",
                               "CC4R": "21450",
                               "C431": "21450",
                               "C433": "21450",
                               "C521": "21450",
                               "C523": "21450",
                               "W302": "18900",
                               "RW43": "18900",
                               "VW53": "18900",
                               "WT34": "18900",
                               "WT31": "18900",
                               "WTH4": "18900",
                               "B991": "21450",
                               "B740": "21450",
                               "B990": "21450",
                               "B520": "21450",
                               "QV36": "16800",
                               "RV26": "16800",
                               "QV16": "16800",
                               "VW63": "16800",
                               "VV56": "16800",
                               "VR61": "16800",
                               "BIBU08": "16800",
                               "V641": "16800",
                               "V500": "16800",
                               "RV45": "16800",
                               "V501": "16800",
                               "F300": "21450",
                               "F301": "21450",
                               "F344": "21450",
                               "F350": "21450",
                               "FF35": "21450",
                               "F371": "21450",
                               "F3F5": "21450",
                               "FV35": "21450",
                               "F321": "21450",
                               "F3G4": "21450",
                               "F3GK": "21450",
                               "F305": "21450",
                               "F304": "21450",
                               "F3F5": "21450",
                               "L210": "16800",
                               "LL23": "16800",
                               "LV25": "16800",
                               "L201": "16800",
                               "LL24": "16800",
                               "C800": "21450",
                               "C802": "21450",
                               "C801": "21450",
                               "R710": "16800",
                               "RL71": "16800",
                               "RL72": "16800",
                               "RN72": "16800",
                               "RR47": "16800",
                               "R7R7": "16800",
                               "R7RR": "16800",
                               "RV75": "16800",
                               "RW73": "18900",
                               "R7T2": "16800",
                               "L300": "16800",
                               "LL43": "16800",
                               "NL2K": "16800",
                               "NL24": "16800",
                               "L391": "16800",
                               "L301": "16800",
                               "L401": "16800",
                               "L722": "16800",
                               "TRPU105": "16800",
                               "LK74": "18900",
                               "K401": "16800",
                               "K441": "16800",
                               "L790": "16800", }
            tuition_fee = tuition_feeDict.get(item['ucascode'])
            print("tuition_fee: ", tuition_fee)
            if tuition_fee != None:
                item['tuition_fee'] = int(''.join(tuition_fee))
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee']: ", item['tuition_fee'])
            print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])
            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a',
                      encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

