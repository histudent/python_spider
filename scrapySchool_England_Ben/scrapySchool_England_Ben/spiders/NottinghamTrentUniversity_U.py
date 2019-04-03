import scrapy
import re
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.getIELTS import get_ielts
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime

class NottinghamTrentUniversity_USpider(scrapy.Spider):
    name = "NottinghamTrentUniversity_U"
    start_urls = ["https://www.ntu.ac.uk/_resources/funnelback/rests/course-collection-json?level-of-study=Undergraduate&year-of-study=2019&study-option=Full-time&sort=title&start_rank=1"]
    # print(len(start_urls))
    # start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        text_dict = json.loads(response.text)
        # print("text_dict: ", text_dict)
        pagination = text_dict.get("resultsPagination").get("currentStart")
        # print("currentStart: ", pagination)
        # 在第一页的时候将所有的列表链接加到start_urls
        if pagination == "1":
            last_pagination = text_dict.get("pagination").get("hasLast").get("url")
            last_start = int(last_pagination.replace("start_rank=", "").strip())
            # print(last_start)
            for sr in range(1, last_start+10, 10):
                # print("====================", sr)
                url = "https://www.ntu.ac.uk/_resources/funnelback/rests/course-collection-json?level-of-study=Undergraduate&year-of-study=2019&study-option=Full-time&sort=title&start_rank=" + str(sr)
                # print(url)
                # self.start_urls.append(url)
                yield scrapy.Request(url, callback=self.parse_url)
        # print(len(self.start_urls))
        # self.start_urls = list(set(self.start_urls))
        # print(len(self.start_urls))
        # print(self.start_urls)

    def parse_url(self,response):
        # print("======", response.url)
        text_dict = json.loads(response.text)
        # 获得专业链接
        links = text_dict.get("results")
        # print(links)
        for linkdict in links:
            u = linkdict.get("courseURL")
            # print(u)
            yield scrapy.Request(u, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "https://www.ntu.ac.uk/"
        item['university'] = "Nottingham Trent University"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        print("===============================")
        # print(response.url)
        print(item['url'])
        try:
            # 专业、学位类型
            programme = response.xpath("//h1[@class='course-heading page-heading']//text()").extract()
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en'] = ", item['programme_en'])

            degree_type = response.xpath("//h2[@class='js_qualification']/strong//text()").extract()
            item['degree_name'] = ''.join(degree_type)
            print("item['degree_name'] = ", item['degree_name'])


            # //div[@id='tabs-key-info']/div[@class='tab tab-1 active-tab']/p[3]/span
            location = response.xpath(
                "//span[@class='location save']//text()").extract()
            item['location'] = ''.join(location).strip()
            # print("item['location'] = ", item['location'])

            start_date = response.xpath(
                "//strong[contains(text(),'Starting:')]/following-sibling::span//text()").extract()
            # print(start_date)
            item['start_date'] = ''.join(start_date)
            # print("item['start_date'] = ", item['start_date'])
            item['start_date'] = getStartDate(item['start_date'])
            # print("item['start_date']1 = ", item['start_date'])

            # //html//div[@class='content']/div[1]/div  专业描述
            overview = response.xpath(
                "//div[@id='what-you-will-study']/preceding-sibling::*").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en'] = ", item['overview_en'])

            # modules   课程设置
            modules = response.xpath(
                "//div[@id='what-you-will-study']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en'] = ", item['modules_en'])

            # teaching_assessment   评估方式
            teaching_assessment = response.xpath(
                "//div[@id='how-youre-taught']").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(teaching_assessment))
            # print("item['assessment_en'] = ", item['assessment_en'])

            # career   评估方式
            career = response.xpath(
                "//div[@id='careers-and-employability']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en'] = ", item['career_en'])

            # //div[@id='entry-requirements-1']
            entry_requirements = response.xpath(
                "//div[@id='entry-requirements-0']").extract()
            item['apply_desc_en'] = remove_class(clear_lianxu_space(entry_requirements))
            print("item['apply_desc_en'] = ", item['apply_desc_en'])

            # //div[@id='entry-requirements-1']
            how_to_apply = response.xpath(
                "//div[@id='how-to-apply-1']").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(how_to_apply))
            # print("item['apply_proces_en'] = ", item['apply_proces_en'])

            # //div[@id='how-to-apply-1']//h3[contains(text(),'Interview')]/following-sibling::p[position()<3]
            interview_desc_en = response.xpath(
                "//div[@id='how-to-apply-1']//h3[contains(text(),'Interview')]/following-sibling::p[position()<3]").extract()
            item['interview_desc_en'] = remove_class(clear_lianxu_space(interview_desc_en))
            # print("item['interview_desc_en'] = ", item['interview_desc_en'])

            # deadline
            deadline = response.xpath(
                "//div[@id='how-to-apply-1']//p//strong[contains(text(),'Application closing date')]/../following-sibling::p[1]//text()|//div[@id='how-to-apply-1']//h3[contains(text(),'Application deadline')]/following-sibling::p[1]//text()").extract()
            clear_space(deadline)
            # print("deadline: ", deadline)
            deadline_str = ''.join(deadline)
            item['deadline'] = getStartDate(deadline_str)
            # print("item['deadline'] = ", item['deadline'])

            alevel = response.xpath(
                "//div[@id='entry-requirements-0']//li[contains(text(),'A-levels')]//text()").extract()
            clear_space(alevel)
            # print(alevel)
            if len(alevel) > 0:
                item['alevel'] = ''.join(alevel[0]).strip()
            # print("item['alevel'] = ", item['alevel'])

            if len(item['alevel']) > 160:
                item['alevel'] = ''.join(item['alevel'][:161])
            # print("item['alevel']1 = ", item['alevel'])


            # https://www.ntu.ac.uk/international/scholarships-and-fees/tuition-fees
            tuition_fee = response.xpath("//html//div[@id='fees-and-funding-1']//text()").extract()
            clear_space(tuition_fee)
            # print(tuition_fee)
            tuition_fee = getTuition_fee(''.join(tuition_fee))
            item['tuition_fee'] = tuition_fee
            if item['tuition_fee'] == 0:
                item['tuition_fee'] = None
            else:
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee'] = ", item['tuition_fee'])
            # print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])

            departmentDict = {"Economics with Business": "Nottingham Business School","Animal Health and Welfare": "School of Animal, Rural and Environmental Sciences",
"Applied Anthrozoology": "School of Animal, Rural and Environmental Sciences",
"Biodiversity Conservation": "School of Animal, Rural and Environmental Sciences",
"Endangered Species Recovery and Conservation": "School of Animal, Rural and Environmental Sciences",
"Equine Health and Welfare": "School of Animal, Rural and Environmental Sciences",
"Equine Performance": "School of Animal, Rural and Environmental Sciences",
"Equine Performance, Health and Welfare": "School of Animal, Rural and Environmental Sciences",
"Global Food Security and Development": "School of Animal, Rural and Environmental Sciences",
"Architecture": "School of Architecture, Design and the Built Environment",
"Architecture (ARB/RIBA Part 2)rch": "School of Architecture, Design and the Built Environment",
"Building Surveying": "School of Architecture, Design and the Built Environment",
"Civil Engineering": "School of Architecture, Design and the Built Environment",
"Construction Management": "School of Architecture, Design and the Built Environment",
"Construction Project Management (Online)": "School of Architecture, Design and the Built Environment",
"Interior Architecture and Design": "School of Architecture, Design and the Built Environment",
"International Real Estate Investment and Finance": "School of Architecture, Design and the Built Environment",
"Planning and Development": "School of Architecture, Design and the Built Environment",
"Project Management (Construction)": "School of Architecture, Design and the Built Environment",
"Quantity Surveying": "School of Architecture, Design and the Built Environment",
"Real Estate": "School of Architecture, Design and the Built Environment",
"Structural Engineering with Management": "School of Architecture, Design and the Built Environment",
"Structural Engineering with Materials": "School of Architecture, Design and the Built Environment",
"Animation": "School of Art & Design",
"Commercial Photography": "School of Art & Design",
"Culture, Style and Fashion": "School of Art & Design",
"Branding and Identity": "School of Art & Design",
"Fashion Communications": "School of Art & Design",
"Fashion Design": "School of Art & Design",
"Fashion Knitwear Design": "School of Art & Design",
"Fashion Marketing": "School of Art & Design",
"Fine Art": "School of Art & Design",
"Graphic Design": "School of Art & Design",
"Illustration": "School of Art & Design",
"International Fashion Management": "School of Art & Design",
"Luxury Fashion Brand Management": "School of Art & Design",
"Photography": "School of Art & Design",
"Textile Design Innovation": "School of Art & Design",
"Culture, Style and Fashion": "School of Art & Design",
"Fashion Communications": "School of Art & Design",
"Fashion Marketing": "School of Art & Design",
"Fashion and Textile Design": "School of Art & Design",
"Fine Art": "School of Art & Design",
"Graphic Design Theory and Practice": "School of Art & Design",
"International Fashion Management": "School of Art & Design",
"Luxury Fashion Brand Management": "School of Art & Design",
"Photography": "School of Art & Design",
"PG Cert Creative Pattern Cutting (15 weeks)": "School of Art & Design",
"Art and Design Professional Doctorate": "School of Art & Design",
"Art and Design": "School of Art & Design",
"Broadcast Journalism": "School of Arts and Humanities",
"Digital and Newspaper Journalism": "School of Arts and Humanities",
"Magazine Journalism": "School of Arts and Humanities",
"Documentary Journalism": "School of Arts and Humanities",
"Media and Globalisation": "School of Arts and Humanities",
"Creative Writing": "School of Arts and Humanities",
"English Literary Research": "School of Arts and Humanities",
"Linguistics": "School of Arts and Humanities",
"Philosophy": "School of Arts and Humanities",
"History": "School of Arts and Humanities",
"PGCert Museum and Heritage Development": "School of Arts and Humanities",
"Holocaust and Genocide": "School of Arts and Humanities",
"International Development": "School of Arts and Humanities",
"English Language Teaching": "School of Arts and Humanities",
"TESOL (Teaching English to Speakers of Other Languages)": "School of Arts and Humanities",
"Management": "Nottingham Business School",
"Management and Finance": "Nottingham Business School",
"Management and Global Supply Chain Management": "Nottingham Business School",
"Management and Innovation and Enterprise": "Nottingham Business School",
"Management and International Business": "Nottingham Business School",
"Management and Marketing": "Nottingham Business School",
"Marketing": "Nottingham Business School",
"Branding and Advertising": "Nottingham Business School",
"Digital Marketing": "Nottingham Business School",
"Management and Marketing": "Nottingham Business School",
"fees, funding and scholarships": "Nottingham Business School",
"Return to all courses": "Nottingham Business School",
"Human resource Management": "Nottingham Business School",
"Economics": "Nottingham Business School",
"Economics and Investment Banking": "Nottingham Business School",
"International Business": "Nottingham Business School",
"International Business (Dual Award) ": "Nottingham Business School",
"Management and International Business": "Nottingham Business School",
"Management and International Publishing": "Nottingham Business School",
"Management and Global Supply Chain Management": "Nottingham Business School",
"Finance": "Nottingham Business School",
"Finance and Accounting": "Nottingham Business School",
"Finance and Investment Banking": "Nottingham Business School",
"Management and Finance": "Nottingham Business School",
"Economics and Investment Banking": "Nottingham Business School",
"Entrepreneurship": "Nottingham Business School",
"Project Management": "Nottingham Business School",
"Management": "Nottingham Business School",
"Management and International Business": "Nottingham Business School",
"Marketing": "Nottingham Business School",
"Branding and Advertising": "Nottingham Business School",
"Finance": "Nottingham Business School",
"International Business": "Nottingham Business School",
"Assessment Only Route to QTS (Primary) - Non-NTU Award": "Nottingham Institute of Education",
"Assessment Only Route to QTS (Secondary) - Non-NTU Award": "Nottingham Institute of Education",
"Early Years Initial Teacher Training": "Nottingham Institute of Education",
"Early Years Initial Teacher Training (Assessment Only) - Non-NTU Award": "Nottingham Institute of Education",
"Education": "Nottingham Institute of Education",
"English Language Teaching": "Nottingham Institute of Education",
"Post-Compulsory Education and Training": "Nottingham Institute of Education",
"Post-Compulsory Education and Training (with English and Literacy)": "Nottingham Institute of Education",
"Post-Compulsory Education and Training (with Mathematics and Numeracy)": "Nottingham Institute of Education",
"Post-Compulsory Education and Training (with Science, Engineering and Technology)": "Nottingham Institute of Education",
"Post-Compulsory Education and Training (with Special and Inclusive Practice)": "Nottingham Institute of Education",
"Primary Education": "Nottingham Institute of Education",
"Primary: School-Centred Initial Teacher Training (SCITT)": "Nottingham Institute of Education",
"School Direct Training Programme (Primary salaried)": "Nottingham Institute of Education",
"School Direct Training Programme (Primary)": "Nottingham Institute of Education",
"School Direct Training Programme (Secondary salaried)": "Nottingham Institute of Education",
"School Direct Training Programme (Secondary)": "Nottingham Institute of Education",
"Secondary Biology": "Nottingham Institute of Education",
"Secondary Business Education": "Nottingham Institute of Education",
"Secondary Chemistry": "Nottingham Institute of Education",
"Secondary Computer Science with ICT": "Nottingham Institute of Education",
"Secondary Education (Design and Technology)": "Nottingham Institute of Education",
"Secondary Education (Physics)": "Nottingham Institute of Education",
"Secondary English": "Nottingham Institute of Education",
"Secondary Mathematics": "Nottingham Institute of Education",
"Secondary Music": "Nottingham Institute of Education",
"Special Educational Needs Coordination - National Award": "Nottingham Institute of Education",
"Teaching English to Speakers of Other Languages (TESOL)": "Nottingham Institute of Education",
"Corporate and Insolvency Law": "Nottingham Law School",
"Dual LLM in Corporate and Insolvency Law / European and Insolvency Law": "Nottingham Law School",
"General Law": "Nottingham Law School",
"Health Law and Ethics": "Nottingham Law School",
"Human Rights and Justice": "Nottingham Law School",
"Intellectual Property Law": "Nottingham Law School",
"International Financial Law": "Nottingham Law School",
"International Trade and Commercial Law": "Nottingham Law School",
"Oil, Gas and Mining Law": "Nottingham Law School",
"Sports Law": "Nottingham Law School",
"Corporate and Insolvency Law": "Nottingham Law School",
"International Trade and Commercial Law": "Nottingham Law School",
"Legal Practice": "Nottingham Law School",
"Oil, Gas and Mining Law": "Nottingham Law School",
"Biomedical Science": "School of Science and Technology",
"Biomedical Science (Flexible Learning)": "School of Science and Technology",
"Neuropharmacology": "School of Science and Technology",
"Pharmacology": "School of Science and Technology",
"Molecular Microbiology": "School of Science and Technology",
"Biotechnology": "School of Science and Technology",
"Molecular Cell Biology": "School of Science and Technology",
"Environmental Management": "School of Science and Technology",
"Biotechnology": "School of Science and Technology",
"Cancer Biology": "School of Science and Technology",
"Cell Biology": "School of Science and Technology",
"Molecular Biology": "School of Science and Technology",
"Molecular Microbiology": "School of Science and Technology",
"Neuropharmacology": "School of Science and Technology",
"Pharmacology": "School of Science and Technology",
"Environmental Management": "School of Science and Technology",
"Biomedical Science (Flexible Learning)": "School of Science and Technology",
"Environmental Management": "School of Science and Technology",
"Chemistry / Chemistry (Professional Practice)": "School of Science and Technology",
"Pharmaceutical and Medicinal Science": "School of Science and Technology",
"Pharmaceutical Analysis": "School of Science and Technology",
"Analytical Chemistry": "School of Science and Technology",
"Chemistry": "School of Science and Technology",
"Advanced Materials Engineering": "School of Science and Technology",
"Forensic Science": "School of Science and Technology",
"Computer Science": "School of Science and Technology",
"Cloud and Enterprise Computing": "School of Science and Technology",
"IT Security": "School of Science and Technology",
"Engineering (Electronics)": "School of Science and Technology",
"Engineering (Cybernetics and Communications)": "School of Science and Technology",
"Engineering Management": "School of Science and Technology",
"Computing Systems": "School of Science and Technology",
"Data Analytics for Business": "School of Science and Technology",
"Computer Science": "School of Science and Technology",
"Electronic Systems": "School of Science and Technology",
"Online MBA with Data Analytics": "School of Science and Technology",
"Mathematical Sciences": "School of Science and Technology",
"Data Analytics for Business": "School of Science and Technology",
"Online MBA with Data Analytics": "School of Science and Technology",
"Medical and Materials Imaging": "School of Science and Technology",
"Medical Imaging": "School of Science and Technology",
"Physics": "School of Science and Technology",
"Physics": "School of Science and Technology",
"Sport Science": "School of Science and Technology",
"Exercise Physiology": "School of Science and Technology",
"Performance Nutrition": "School of Science and Technology",
"Performance Analysis": "School of Science and Technology",
"Biomechanics": "School of Science and Technology",
"Sport and Exercise Psychology": "School of Science and Technology",
"Psychology": "School of Social Sciences",
"Applied Child Psychology": "School of Social Sciences",
"sychological Research Methods": "School of Social Sciences",
"Forensic Mental Health": "School of Social Sciences",
"Forensic Psychology (BPS accredited)": "School of Social Sciences",
"Cyberpsychology": "School of Social Sciences",
"Psychology in Clinical Practice": "School of Social Sciences",
"Psychological Wellbeing and Mental Health": "School of Social Sciences",
"Criminology": "School of Social Sciences",
"Sociology": "School of Social Sciences",
"Politics": "School of Social Sciences",
"International Relations": "School of Social Sciences",
"Online International Relations (Distance learning)": "School of Social Sciences",
"Public Health": "School of Social Sciences",
"Career Development": "School of Social Sciences",
"Social Work (January 2019 entry)": "School of Social Sciences",}
            item['department'] = departmentDict.get(item['programme_en'])
            if item['department'] == None:
                item['department'] = departmentDict.get(item['programme_en'])
                if item['department'] == None:
                    item['department'] = departmentDict.get(item['programme_en'])
                    if item['department'] == None:
                        item['department'] = departmentDict.get(item['programme_en'].replace(" ", " "))
            print("item['department'] = ", item['department'])

            # School of Animal, Rural and Environmental Sciences
            # School of Architecture, Design and the Built Environment
            # School of Art &amp; Design
            # School of Arts and Humanities
            # Nottingham Business School
            # Nottingham Institute of Education
            # Nottingham Law School
            # School of Science and Technology
            # School of Social Sciences
            if item['department'] is None:
                if "/animal-rural-environmental-sciences" in item['url']:
                    item['department'] = "School of Animal, Rural and Environmental Sciences"
                elif "/architecture-design-built-environment" in item['url']:
                    item['department'] = "School of Architecture, Design and the Built Environment"
                elif "/art-design" in item['url']:
                    item['department'] = "School of Art & Design"
                elif "/arts-humanities" in item['url']:
                    item['department'] = "School of Arts and Humanities"
                elif "/business" in item['url']:
                    item['department'] = "Nottingham Business School"
                elif "/education" in item['url']:
                    item['department'] = "Nottingham Institute of Education"
                elif "/law" in item['url']:
                    item['department'] = "Nottingham Law School"
                elif "/science-technology" in item['url']:
                    item['department'] = "School of Science and Technology"
                elif "/social-sciences" in item['url']:
                    item['department'] = "School of Social Sciences"
            print("item['department']1 = ", item['department'])

            if item['degree_name'] == "BA (Hons)":
                item['ielts'] = 7.0
                item['ielts_l'] = 6.5
                item['ielts_s'] = 6.5
                item['ielts_r'] = 6.5
                item['ielts_w'] = 6.5
            elif item['department'] == "School of Art & Design" or item['department'] == "School of Animal, Rural and Environmental Sciences" or item['department'] == "School of Science and Technology":
                item['ielts'] = 6.0
                item['ielts_l'] = 5.5
                item['ielts_s'] = 5.5
                item['ielts_r'] = 5.5
                item['ielts_w'] = 5.5
            elif item['department'] == "Nottingham Business School":
                item['ielts'] = 6.5
                item['ielts_l'] = 5.5
                item['ielts_s'] = 5.5
                item['ielts_r'] = 5.5
                item['ielts_w'] = 5.5
            elif item['department'] == "School of Architecture, Design and the Built Environment" or item['department'] == "School of Arts and Humanities" or item['department'] == "Nottingham Institute of Education" or item['department'] == "Nottingham Law School" or item['department'] == "School of Social Sciences" or item['department'] == "School of Art & Design":
                item['ielts'] = 6.5
                item['ielts_l'] = 5.5
                item['ielts_s'] = 5.5
                item['ielts_r'] = 5.5
                item['ielts_w'] = 5.5
            # print("item['IELTS'] = %s item['IELTS_L'] = %s item['IELTS_S'] = %s item['IELTS_R'] = %s item['IELTS_W'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            entry_requirements = response.xpath(
                "//div[@id='entry-requirements-1']//text()").extract()
            entry_requirementsStr = ''.join(entry_requirements)
            ielts = re.findall(r"IELTS.{1,200}", entry_requirementsStr)
            item['ielts_desc'] = ''.join(ielts)
            # print("item['ielts_desc']: ", item['ielts_desc'])

            if item['ielts'] == None:
                ieltsDict = get_ielts(''.join(ielts))
                item['ielts'] = ieltsDict.get("IELTS")
                item['ielts_l'] = ieltsDict.get("IELTS_L")
                item['ielts_s'] = ieltsDict.get("IELTS_S")
                item['ielts_r'] = ieltsDict.get("IELTS_R")
                item['ielts_w'] = ieltsDict.get("IELTS_W")
            # print("item['IELTS'] = %sitem['IELTS_L'] = %sitem['IELTS_S'] = %sitem['IELTS_R'] = %sitem['IELTS_W'] = %s==" % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            item["require_chinese_en"] = remove_class(clear_lianxu_space(["""<h2>Entry requirements</h2>
                        <table id="table76765" style="width: 100%;"><thead><tr><th id="table76765r1c1"> Your qualification</th><th id="table76765r1c2"> You could study</th></tr></thead><tbody><tr><td headers="table76765r1c1">         High School Year 2<br />Grades of 70% and above       </td><td headers="table76765r1c2">         Foundation courses at <a href="https://www.kaplanpathways.com/colleges/nottingham-trent-international-college/courses/">Nottingham Trent International College (NTIC) </a></td></tr><tr><td headers="table76765r1c1">         High School Year 3<br />Grades of 80% and above       </td><td headers="table76765r1c2">         International Year One courses at NTIC       </td></tr><tr><td headers="table76765r1c1">         Completion of first year of Chinese university degree       </td><td headers="table76765r1c2">         First year bachelors degrees       </td></tr><tr><td headers="table76765r1c1">         Three year diploma or higher national diploma       </td><td headers="table76765r1c2">         Considered for final year entry to selected bachelors degrees or for Pre-Masters courses at <a href="https://www.kaplanpathways.com/colleges/nottingham-trent-international-college/courses/">Nottingham Trent International College</a></td></tr><tr><td headers="table76765r1c1">         Bachelors degree (four years or six years in medicine / dentistry) from recognised institution in China. <br />Grades of 75% or above<br />Grades of 70% or above from 211 universities       </td><td headers="table76765r1c2">         Postgraduate (Masters) courses       </td></tr><tr><td headers="table76765r1c1">         Masters degree from a recognised institution in China.<br />Grades of 70% or above       </td><td headers="table76765r1c2">         Postgraduate research       </td></tr></tbody></table><p>If you have questions about your qualification and it is not listed here, please <a href="mailto:international@ntu.ac.uk">contact us</a> for advice.</p>
"""]))

            ucascode = response.xpath(
                "//strong[contains(text(),'UCAS code(s):')]/following-sibling::*//text()").extract()
            clear_space(ucascode)
            if len(ucascode) > 0:
                item['ucascode'] = ''.join(ucascode[0]).replace(" / ", "/").strip()
            print("item['ucascode']: ", item['ucascode'])

            duration = response.xpath(
                "//strong[contains(text(),'Course duration:')]/following-sibling::span//text()").extract()
            print("duration: ", duration)
            duration_str = ''.join(duration).replace("/ sandwich", "").strip()
            duration_list = getIntDuration(''.join(duration))
            # print("duration_list: ", duration_list)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            duration_per = item['duration_per']
            print("item['duration'] = ", item['duration'])
            print("item['duration_per'] = ", item['duration_per'])

            if "/" in item['ucascode']:
                ucascode_sp = item['ucascode'].split("/")
                if "/" in duration_str:
                    duration_sp = duration_str.split("/")
                elif " or" in duration_str:
                    duration_sp = duration_str.split(" or")
                elif "," in duration_str:
                    duration_sp = duration_str.split(" or")
                else:
                    duration_sp = [duration_str, duration_str]
                print("ucascode_sp: ", ucascode_sp)
                print("duration_sp: ", duration_sp)
                if len(ucascode_sp) == 2:
                    item['ucascode'] = ucascode_sp[0]
                    duration_list = getIntDuration(duration_sp[0])
                    if len(duration_list) == 2:
                        item['duration'] = duration_list[0]
                        item['duration_per'] = duration_list[-1]
                    if item['duration'] == None:
                        item['duration'] = int(duration_sp[0].strip())
                        item['duration_per'] = duration_per
                    print("item['ucascode']1: ", item['ucascode'])
                    print("item['duration']1 = ", item['duration'])
                    print("item['duration_per']1 = ", item['duration_per'])
                    yield item

                    item['ucascode'] = ucascode_sp[-1]
                    duration_list = getIntDuration(duration_sp[-1].strip())
                    if len(duration_list) == 2:
                        item['duration'] = duration_list[0]
                        item['duration_per'] = duration_list[-1]
                    if item['duration'] == None:
                        item['duration'] = int(duration_sp[-1].replace("year", "").replace("(s)", "").strip())
                        item['duration_per'] = 1
                    print("item['ucascode']2: ", item['ucascode'])
                    print("item['duration']2 = ", item['duration'])
                    print("item['duration_per']2 = ", item['duration_per'])
                    yield item
            else:
                yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

