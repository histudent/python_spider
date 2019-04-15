import scrapy
import re, json
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getDuration import getTeachTime

from lxml import etree

class SwanseaUniversity_RSpider(scrapy.Spider):
    name = "SwanseaUniversity_R"
    # start_urls = ["https://www.swan.ac.uk/postgraduate/taught/"]
    # 接口
    start_urls = ["https://www.swan.ac.uk/sf-widgets/en/course/a-to-z/postgraduate/research"]

    def parse(self, response):
        # hrefJson = json.loads(
        #     response.text.replace(");", "").replace("/**/jQuery172001851942159089104_1529979609089(", ""))
        # # print(hrefJson)
        # htmlStr = hrefJson.get('html')
        # # print(htmlStr)
        # # 将字符串格式化为HTML文件，然后使用xpath获取专业链接
        # html = etree.fromstring(htmlStr)
        links = response.xpath("//ul/li/ul/li/a/@href").extract()
        # print(links)
        print(len(links))
        links = list(set(links))
        print(len(links))
        for url in links:
            if url != "":
                yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "http://www.swansea.ac.uk/"
        item['university'] = "Swansea University"
        item['url'] = response.url
        item['teach_type'] = 'phd'
        item['degree_type'] = 3
        item['location'] = "Singleton Park, Swansea, SA2 8PP, Wales, UK"
        print("===============================")
        print(response.url)
        try:
            # 专业、学位类型
            courseDegreeaward = response.xpath("//h1[@class='content-header-heading']//text()").extract()
            courseDegreeawardStr = ''.join(courseDegreeaward)
            if len(courseDegreeawardStr) != 0:
                d = re.findall(r"^(\w+\s/\w+\s/\w+)|^(\w+/\w+/\w+)|^(\w+/\s\w+)|^(\w+)", courseDegreeawardStr)
                if len(d) != 0:
                    degree_type = ''.join(list(d)[0])
                    # print(degree_type)
                    item['degree_name'] = degree_type
                    programme = courseDegreeawardStr.split(degree_type)
                    item['programme_en'] = ''.join(programme).strip()
            print("item['degree_name'] = ", item['degree_name'])
            print("item['programme_en'] = ", item['programme_en'])

            # print("courseDegreeawardStr = ", courseDegreeawardStr)
            departmentDict = {"Ancient Egyptian Culture": "College of Arts and Humanities",
"Ancient History and Classical Culture": "College of Arts and Humanities",
"Ancient Narrative Literature": "College of Arts and Humanities",
"Classics": "College of Arts and Humanities",
"Chinese-English Translation & Language Teaching": "College of Arts and Humanities",
"Teaching English to Speakers of Other Languages  (TESOL)": "College of Arts and Humanities",
"Creative Writing": "College of Arts and Humanities",
"English Literature": "College of Arts and Humanities",
"Gender and Culture": "College of Arts and Humanities",
"Welsh Writing in English": "College of Arts and Humanities",
"Early Modern History": "College of Arts and Humanities",
"History": "College of Arts and Humanities",
"Medieval Studies": "College of Arts and Humanities",
"Modern History": "College of Arts and Humanities",
"Public History and Heritage": "College of Arts and Humanities",
"Public History and Heritage (extended)": "College of Arts and Humanities",
"Professional Translation": "College of Arts and Humanities",
"Professional Translation (Extended)": "College of Arts and Humanities",
"Translation and Interpreting": "College of Arts and Humanities",
"Translation and Interpreting (Extended)": "College of Arts and Humanities",
"Postgraduate Certificate in Translation Technology": "College of Arts and Humanities",
"Communication, Media Practice and PR": "College of Arts and Humanities",
"International Journalism": "College of Arts and Humanities",
"Digital Media": "College of Arts and Humanities",
"Erasmus Mundus Journalism, Media and Globalisation": "College of Arts and Humanities",
"Development and Human Rights": "College of Arts and Humanities",
"Gender and Culture": "College of Arts and Humanities",
"International Relations": "College of Arts and Humanities",
"International Security & Development": "College of Arts and Humanities",
"Politics": "College of Arts and Humanities",
"Public Policy": "College of Arts and Humanities",
"War and Society": "College of Arts and Humanities",
"BEng Aerospace Engineering": "College of Engineering",
"MEng Aerospace Engineering": "College of Engineering",
"BEng Aerospace Engineering (with a Year in Industry)": "College of Engineering",
"MEng Aerospace Engineering (with a Year in Industry)": "College of Engineering",
"BEng Aerospace Engineering (with a Year Abroad)": "College of Engineering",
"MEng Aerospace Engineering (with a Year Abroad)": "College of Engineering",
"Aerospace Engineering Foundation Year": "College of Engineering",
"MSc Aerospace Engineering": "College of Engineering",
"MSc by Research in Aerospace Engineering": "College of Engineering",
"MSc Engineering Leadership & Management": "College of Engineering",
"Engineering Doctorate (EngD)": "College of Engineering",
"PhD or MPhil Aerospace Engineering": "College of Engineering",
"BEng Chemical Engineering": "College of Engineering",
"MEng Chemical Engineering": "College of Engineering",
"BEng Chemical Engineering (with a Year in Industry)": "College of Engineering",
"MEng Chemical Engineering (with a Year in Industry)": "College of Engineering",
"BEng Chemical Engineering (with a Year Abroad)": "College of Engineering",
"MEng Chemical Engineering (with a Year Abroad)": "College of Engineering",
"Chemical Engineering Foundation Year": "College of Engineering",
"MSc Chemical Engineering": "College of Engineering",
"MSc Engineering Leadership & Management": "College of Engineering",
"MSc by Research in Chemical Engineering": "College of Engineering",
"MSc by Research in Bio-process Engineering": "College of Engineering",
"MSc by Research in Desalination and Water Re-use": "College of Engineering",
"MSc by Research in Fuel Technology": "College of Engineering",
"MSc by Research in Membrane Technology": "College of Engineering",
"PhD or MPhil Chemical Engineering": "College of Engineering",
"Engineering Doctorate (EngD)": "College of Engineering",
"BEng Civil Engineering": "College of Engineering",
"MEng Civil Engineering": "College of Engineering",
"BEng Civil Engineering (with a Year in Industry)": "College of Engineering",
"MEng Civil Engineering (with a Year in Industry)": "College of Engineering",
"BEng Civil Engineering (with a Year Abroad)": "College of Engineering",
"MEng Civil Engineering (with a Year Abroad)": "College of Engineering",
"MSc Civil Engineering": "College of Engineering",
"Erasmus Mundus MSc in Computational Mechanics": "College of Engineering",
"MSc Computer Modelling and Finite Elements in Engineering Mechanics": "College of Engineering",
"MSc Engineering Leadership & Management": "College of Engineering",
"MRes Computer Modelling in Engineering": "College of Engineering",
"MSc by Research in Civil Engineering": "College of Engineering",
"PhD Computational Mechanics": "College of Engineering",
"PhD or MPhil Civil Engineering": "College of Engineering",
"Engineering Doctorate (EngD)": "College of Engineering",
"BEng Electronic and Electrical Engineering": "College of Engineering",
"MEng Electronic and Electrical Engineering": "College of Engineering",
"BEng Electronic and Electrical Engineering (with a year in Europe, N. America, Australia or industry)": "College of Engineering",
"MEng Electronic and Electrical Engineering (with a year in Europe, N. America, Australia or industry)": "College of Engineering",
"Electronic and Electrical Engineering Foundation Year": "College of Engineering",
"MSc Communications Engineering": "College of Engineering",
"MSc Electronic and Electrical Engineering": "College of Engineering",
"MSc Power Engineering and Sustainable Energy": "College of Engineering",
"MSc Nanoscience to Nanotechnology": "College of Engineering",
"MSc by Research in Electronic and Electrical Engineering": "College of Engineering",
"MSc Engineering Leadership & Management": "College of Engineering",
"PhD or MPhil Electronic and Electrical Engineering": "College of Engineering",
"Erasmus Mundus MSc in Computational Mechanics": "College of Engineering",
"MSc Computer Modelling and Finite Elements in Engineering Mechanics": "College of Engineering",
"MSc Engineering Leadership & Management": "College of Engineering",
"MRes Computer Modelling in Engineering": "College of Engineering",
"PhD Computational Mechanics": "College of Engineering",
"PhD or MPhil Civil Engineering": "College of Engineering",
"Engineering Doctorate (EngD)": "College of Engineering",
"BEng Materials Science and Engineering": "College of Engineering",
"MEng Materials Science and Engineering": "College of Engineering",
"BEng Materials Science and Engineering (with a Year in Industry)": "College of Engineering",
"MEng Materials Science and Engineering (with a Year in Industry)": "College of Engineering",
"BEng Materials Science and Engineering (with a Year Abroad)": "College of Engineering",
"MEng Materials Science and Engineering (with a Year Abroad)": "College of Engineering",
"Materials Science and Engineering Foundation Year": "College of Engineering",
"MSc Materials Engineering": "College of Engineering",
"MSc Engineering Leadership & Management": "College of Engineering",
"MSc by Research in Materials Engineering": "College of Engineering",
"Engineering Doctorate (EngD)": "College of Engineering",
"PhD or MPhil Materials Engineering": "College of Engineering",
"BEng Mechanical Engineering": "College of Engineering",
"MEng Mechanical Engineering": "College of Engineering",
"BEng Mechanical Engineering (with a Year in Industry)": "College of Engineering",
"MEng Mechanical Engineering (with a Year in Industry)": "College of Engineering",
"BEng Mechanical Engineering (with a Year Abroad)": "College of Engineering",
"MEng Mechanical Engineering (with a Year Abroad)": "College of Engineering",
"Mechanical Engineering Foundation Year": "College of Engineering",
"MSc Mechanical Engineering": "College of Engineering",
"MSc Engineering Leadership & Management": "College of Engineering",
"MSc by Research in Mechanical Engineering": "College of Engineering",
"PhD or MPhil Mechanical Engineering": "College of Engineering",
"Engineering Doctorate (EngD)": "College of Engineering",
"MSc Nanoscience to Nanotechnology": "College of Engineering",
"MSc Engineering Leadership & Management": "College of Engineering",
"MSc by Research Nanotechnology": "College of Engineering",
"PhD or MPhil Nanotechnology": "College of Engineering",
"Engineering Doctorate (EngD)": "College of Engineering",
"Zienkiewicz Centre for Computational Engineering (ZCCE)": "College of Engineering",
"Materials Research Centre (MRC)": "College of Engineering",
"Systems and Process Engineering Centre (SPEC)": "College of Engineering",
"Applied Sports, Technology, Exercise and Medicine (A-STEM)": "College of Engineering",
"MSc/PGCert/PGDip Gerontology and Ageing Studies": "College of Human and Health Sciences",
"MSc International Gerontology and Ageing Studies": "College of Human and Health Sciences",
"MA/PGDip/PGCert Childhood Studies": "College of Human and Health Sciences",
"MA/PGDip/PGCert Developmental and Therapeutic Play": "College of Human and Health Sciences",
"PGCert Enhanced Neonatal Care": "College of Human and Health Sciences",
"MSc/PGDip/PGCert Child Public Health": "College of Human and Health Sciences",
"MA/PGDip/PGCert Education for Health Professions": "College of Human and Health Sciences",
"MSc/PGDip Advanced Critical Care Practice": "College of Human and Health Sciences",
"MSc/PGDip Advanced Practice in Health Care": "College of Human and Health Sciences",
"MSc/PGDip/PGCert Advanced Specialist Blood Transfusion Practice": "College of Human and Health Sciences",
"PGCert Approved Mental Health Professional": "College of Human and Health Sciences",
"PGCert Blood Component Transfusion": "College of Human and Health Sciences",
"MSc/PgD/PgC Community and Primary Health Care Practice": "College of Human and Health Sciences",
"MSc/PGDip/PGCert Enhanced Professional Practice": "College of Human and Health Sciences",
"MSc/PGDip Enhanced Professional Midwifery Practice": "College of Human and Health Sciences",
"MSc Long Term and Chronic Conditions Management": "College of Human and Health Sciences",
"MA Medical Law and Ethics": "College of Human and Health Sciences",
"PGCert Non-Medical Prescribing for Nurses and Midwives": "College of Human and Health Sciences",
"PGCert Non-Medical Prescribing for Allied Health Professionals": "College of Human and Health Sciences",
"PGCert Non-Medical Prescribing for Pharmacists": "College of Human and Health Sciences",
"MSc Nursing Pre-Registration (Adult)": "College of Human and Health Sciences",
"MSc Nursing Pre-Registration (Child)": "College of Human and Health Sciences",
"MSc Nursing Pre-Registration (Mental Health)": "College of Human and Health Sciences",
"MSc/PgD Public Health & Health Promotion": "College of Human and Health Sciences",
"MSc Social Work": "College of Human and Health Sciences",
"MSc Health Care Management": "College of Human and Health Sciences",
"MSc Leadership, Management and Innovation in Health Care": "College of Human and Health Sciences",
"MSc Abnormal and Clinical Psychology": "College of Human and Health Sciences",
"MSc Cognitive Neuroscience": "College of Human and Health Sciences",
"LLM in LegalTech": "Hillary Rodham Clinton School of Law",
"LLM in Human Rights": "Hillary Rodham Clinton School of Law",
"LLM Intellectual Property & Commercial Practice": "Hillary Rodham Clinton School of Law",
"LLM in International Commercial Law": "Hillary Rodham Clinton School of Law",
"LLM in International Commercial and Maritime Law": "Hillary Rodham Clinton School of Law",
"LLM in International Maritime Law": "Hillary Rodham Clinton School of Law",
"LLM in International Trade Law": "Hillary Rodham Clinton School of Law",
"LLM in Legal Practice and Advanced Drafting": "Hillary Rodham Clinton School of Law",
"LLM in Oil, Gas and Renewable Energy Law": "Hillary Rodham Clinton School of Law",
"Law PhD/MPhil": "Hillary Rodham Clinton School of Law",
"Graduate Diploma in Law": "Hillary Rodham Clinton School of Law",
"Legal Practice Course": "Hillary Rodham Clinton School of Law",
"LLM in Legal Practice and Advanced Drafting": "Hillary Rodham Clinton School of Law",
"MSc Environmental Dynamics and Climate Change": "College of Science",
"MSc Geographic Information and Climate Change": "College of Science",
"MSc High Performance and Scientific Computing": "College of Science",
"MSc by Research in Earth Observation": "College of Science",
"MSc by Research in Environmental Dynamics": "College of Science",
"MSc by Research in Glaciology": "College of Science",
"MSc by Research in Global Environmental Modelling": "College of Science",
"MSc by Research in Global Migration": "College of Science",
"MSc by Research in Media Geographies": "College of Science",
"MSc by Research in Social Theory and Space": "College of Science",
"MSc by Research in Urban Studies": "College of Science",
"PhD/MPhil Human Geography": "College of Science",
"PhD/MPhil Physical Geography": "College of Science",
"MSc Maths & Computing for Finance": "College of Science",
"MSc Mathematics": "College of Science",
"MRes Stochastic Processes: Theory and Application": "College of Science",
"MSc by Research in Mathematics": "College of Science",
"PhD/MPhil Mathematics": "College of Science",
"MSc High Performance and Scientific Computing": "College of Science",
"Antimatter Physics": "College of Science",
"Cold Atoms and Quantum Optics": "College of Science",
"Laser Physics": "College of Science",
"Lattice Gauge Theory": "College of Science",
"Nanotechnology": "College of Science",
"Quantum Fields & Strings": "College of Science",
"Theoretical Particle Physics": "College of Science",
"PhD/MPhil Physics": "College of Science",
"PhD / MSc by Research Chemistry": "College of Science",
"MSc Computer Science": "College of Science",
"MSc Advanced Computer Science": "College of Science",
"MSc Advanced Software Technology": "College of Science",
"MSc High Performance and Scientific Computing": "College of Science",
"MSc Data Science": "College of Science",
"MSc Computer Science: Informatique (Swansea route)": "College of Science",
"MSc Computer Science: Informatique (Grenoble route)": "College of Science",
"MSc by Research in Human Computer Interaction": "College of Science",
"MSc by Research in Theoretical Computer Science": "College of Science",
"MSc by Research in Visual and Interactive Computing": "College of Science",
"MRes Computing and Future Interaction Technologies": "College of Science",
"MRes Visual Computing": "College of Science",
"MRes Logic and Computation": "College of Science",
"PhD/MPhil/MSc by Research in Computer Science": "College of Science",
"MSc Environmental Biology: Conservation and Resource Management": "College of Science",
"MSc High Performance and Scientific Computing": "College of Science",
"MRes Biosciences": "College of Science",
"PhD/MPhil Biological Sciences": "College of Science",
"MSc Accounting & Finance": "School of Management",
"MSc Financial Management": "School of Management",
"MSc Finance and Business Analytics": "School of Management",
"MSc Finance": "School of Management",
"MSc International Banking & Finance": "School of Management",
"MSc Investment Management": "School of Management",
"MSc Strategic Accounting": "School of Management",
"Generalist MSc Management": "School of Management",
"Marketing": "School of Management",
"Finance ": "School of Management",
"Human Resource Management": "School of Management",
"Entrepreneurship ": "School of Management",
"Operations & Supply Management": "School of Management",
"International Management": "School of Management",
"International Standards": "School of Management",
"Business Analytics": "School of Management",
"E-Business": "School of Management",
"Tourism ": "School of Management",
"MSc Economics": "School of Management",
"MSc Economics & Finance": "School of Management",
"Strategic Marketing": "School of Management",
"MSc Management (Marketing)": "School of Management",
"MSc Clinical Medicine": "Swansea University Medical School",
"MSc Clinical Science (Medical Physics)": "Swansea University Medical School",
"MSc Diabetes Practice (Distance Learning)": "Swansea University Medical School",
"MSc Genomic Medicine": "Swansea University Medical School",
"MSc Medical Radiation Physics": "Swansea University Medical School",
"MSc Nanomedicine": "Swansea University Medical School",
"PG Dip Physician Associate Studies": "Swansea University Medical School",
"MSc Applied Analytical Science (LCMS)": "Swansea University Medical School",
"MSc Autism and Related Conditions": "Swansea University Medical School",
"MSc Health Data Science": "Swansea University Medical School",
"MSc Health Informatics": "Swansea University Medical School",
"MSc Leadership for the Health Professions (Distance Learning)": "Swansea University Medical School",
"MRes Applied Analytical Science (LCMS)": "Swansea University Medical School",
"MRes Health Informatics": "Swansea University Medical School",
"MRes Research in Health Professions Education": "Swansea University Medical School",
"MSc Research Methods in Psychology": "College of Human and Health Sciences",
"MSc Social Research Methods": "College of Human and Health Sciences", }
            item['department'] = departmentDict.get(courseDegreeawardStr)
            if item['department'] == None:
                item['department'] = departmentDict.get(courseDegreeawardStr.replace(" ", ""))
                if item['department'] == None:
                    item['department'] = departmentDict.get(item['programme_en'])
            print("item['department'] = ", item['department'])

            # //ul[@style='width: 5000px;']/li[4]
            department = response.xpath(
                "//div[@class='breadCrumb module']//ul/li[4]//text()").extract()
            clear_space(department)
            item['department'] = ''.join(department).strip()
            print("item['department'] = ", item['department'])

            # 课程长度
            duration = response.xpath("//table[@class='top-button-course-variants-table']//tr[1]/td[2]//text()|//div[@class='top-button-duration']/div[@class='top-button-duration-value']/text()").extract()
            clear_space(duration)
            duration = ''.join(duration).strip()
            item['teach_time'] = getTeachTime(duration)

            p_l = ['Yr', 'yrs', 'yr', 'YR']
            for p in p_l:
                if p in duration:
                    item['duration'] = int(duration.replace(p, ""))
                    item['duration_per'] = 1
                    break

            print("item['duration'] = ", item['duration'])
            print("item['duration_per'] = ", item['duration_per'])

            # 专业描述
            overview1 = response.xpath(
                "//div[@id='content-items']/div[@class='layout-article-items']/div[@class='title-and-body-text']").extract()
            # print(overview1)
            overview2 = response.xpath("//div[@id='key-features']").extract()
            overview3 = response.xpath("//div[@id='description']").extract()
            clear_lianxu_space(overview1)
            clear_lianxu_space(overview2)
            clear_lianxu_space(overview3)
            overview = '\n'.join(overview1).strip() + '\n'.join(overview2).strip() + '\n'.join(overview3).strip()
            item['overview_en'] = remove_class(overview)
            print("item['overview_en'] = ", item['overview_en'])

            # 课程设置
            modules_1 = response.xpath("//div[@class='ppsm-ms']//div[@class='variant']")
            # print("modules_1: ", modules_1)
            modules = []
            for m in modules_1:
                modules_year = m.xpath("./h3").extract()
                # print("modules_year: ", modules_year)
                modules.append(''.join(modules_year))
                modules_term = m.xpath("./h4").extract()
                # print("modules_term: ", modules_term)
                if len(modules_term) > 0:
                    for t in range(1, len(modules_term)+1):
                        # print("modules_term: ", modules_term[t-1])
                        modules.append(modules_term[t-1])
                        modules_name = m.xpath("./h4["+str(t)+"]/following-sibling::div[1]//table//tr/td[4]").extract()
                        # print("modules_name: ", modules_name)
                        modules.append(''.join(modules_name))
            # print(modules)
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            print("item['modules_en'] = ", item['modules_en'])

            # IELTS
            entryRequirements = response.xpath("//div[@id='entry-requirements']//text()").extract()
            # clear_space(entryRequirements)
            item['rntry_requirements'] = clear_lianxu_space(entryRequirements)
            # print("item['rntry_requirements'] = ", item['rntry_requirements'])
            entryRequirementsStr = ''.join(entryRequirements)
            # .{0,100}(IELTS).{0,100}
            # ielts = re.findall(r"\.[a-zA-Z0-9\s.]{0,80}(IELTS)[a-zA-Z0-9\s.\(\))]{0,80}", entryRequirementsStr)
            pat = r"\..{0,100}IELTS.{0,100}"
            re_ielts = re.compile(pat)
            ielts = re_ielts.findall(entryRequirementsStr)
            item['ielts_desc'] = ''.join(ielts).lstrip('.').strip()
            print("item['ielts_desc'] = ", item['ielts_desc'])
            ielts = item['ielts_desc']
            ieltlsrw = re.findall(r"\d\.\d", ielts)
            # print(ieltlsrw)
            if len(ieltlsrw) >= 2:
                item['ielts'] = ieltlsrw[0]
                item['ielts_l'] = ieltlsrw[1]
                item['ielts_s'] = ieltlsrw[1]
                item['ielts_r'] = ieltlsrw[1]
                item['ielts_w'] = ieltlsrw[1]
            elif len(ieltlsrw) == 1:
                item['ielts'] = ieltlsrw[0]
                item['ielts_l'] = ieltlsrw[0]
                item['ielts_s'] = ieltlsrw[0]
                item['ielts_r'] = ieltlsrw[0]
                item['ielts_w'] = ieltlsrw[0]
            else:
                item["ielts"] = None  # float
                item["ielts_l"] = None  # float
                item["ielts_s"] = None  # float
                item["ielts_r"] = None  # float
                item["ielts_w"] = None
            print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s "
              %(item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            # 学费
            # fee = html.xpath("//div[@id='tuition-fees-contents']/div[@class='table-wrapper']/table[@class='expander-item-fees-table']/tbody/tr[@class='expander-item-fees-table-row odd']/td[@class='expander-item-fees-table-data odd'][2]//text()")
            tuition_fee = response.xpath(
                "//div[@id='tuition-fees-contents']//table[@class='expander-item-fees-table']/tbody/tr[1]/td[4]//text()").extract()
            clear_space(tuition_fee)
            tuition_fee = ''.join(tuition_fee)
            # print(tuition_fee)
            if "£" in tuition_fee:
                item['tuition_fee'] = int(tuition_fee.replace('£', '').replace(',', ''))
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])
            print("item['tuition_fee'] = ", item['tuition_fee'])

            # //div[@id='how-to-apply']
            how_to_apply = response.xpath(
                "//div[@id='how-to-apply']").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(how_to_apply))
            print("item['apply_proces_en'] = ", item['apply_proces_en'])

            assessment_en = response.xpath(
                "//div[@id='assessment']").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            print("item['assessment_en'] = ", item['assessment_en'])

            career = response.xpath(
                "//div[@id='careers-and-employability']|//div[@id='careers-employability']|//div[@id='employabilitycareers']|//div[@id='employability-and-careers-']|//div[@id='careers-in-child-nursing-']|//div[@id='careers']|//div[@id='graduate-employability-and-careers']|//div[@id='careers-in-radiotherapy-physics']|//div[@id='careers-in-midwifery']|//div[@id='careers-in-neurophysiology-']|//div[@id='careers-in-psychology-']|//div[@id='careers-in-adult-nursing-']|//div[@id='careers-in-nursing']|//div[@id='career-prospects-']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            print("item['career_en'] = ", item['career_en'])


            yield item
        except Exception as e:
            with open(item['university'] + str(item['degree_type']) + ".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

