import scrapy
import re
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.getIELTS import get_ielts
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getDuration import getIntDuration, getTeachTime

class NottinghamTrentUniversity_PSpider(scrapy.Spider):
    name = "NottinghamTrentUniversity_P"
    start_urls = ["https://www.ntu.ac.uk/_resources/funnelback/rests/course-collection-json?level-of-study=Postgraduate%20taught&year-of-study=2019&study-option=Full-time&sort=title&start_rank=1"]
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
                url = "https://www.ntu.ac.uk/_resources/funnelback/rests/course-collection-json?level-of-study=Postgraduate%20taught&year-of-study=2019&study-option=Full-time&sort=title&start_rank=" + str(sr)
                # print(url)
                self.start_urls.append(url)
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
#         l = ["https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/art-design/pg/2018-19/animation",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2019-20/branding-and-advertising",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2019-20/branding-and-advertising",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2019-20/branding-and-advertising",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/art-design/pg/2018-19/branding-and-identity",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/art-design/pg/2018-19/commercial-photography",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/art-design/pg/2018-19/culture-style-and-fashion",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/master-of-business-administration-digital-marketing",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/digital-marketing",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/digital-marketing",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/economics",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/economics",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/economics-and-investment-banking",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/economics-and-investment-banking",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/education/pg/2018-19/education-full-time",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/animal-rural-environmental-sciences/pg/2018-19/equine-performance,-health-and-welfare",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/art-design/pg/2018-19/fashion-communications",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/art-design/pg/2018-19/fashion-design",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/art-design/pg/2018-19/fashion-marketing",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/master-of-business-administration-finance",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-finance",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-finance",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-finance",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/finance-and-accounting",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/finance-and-accounting",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/finance-and-accounting",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-finance-and-investment-banking",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-finance-and-investment-banking",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-finance-and-investment-banking",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/art-design/pg/2018-19/fine-art",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/master-of-business-administration-global-supply-chain-management",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/art-design/pg/2018-19/graphic-design",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-human-resource-management-full-time",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-human-resource-management-full-time",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/art-design/pg/2018-19/illustration",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/art-design/pg/2018-19/international-fashion-management",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/art-design/pg/2018-19/luxury-fashion-brand-management",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-management",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-management",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-management",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-management-and-finance",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-management-and-finance",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-management-and-global-supply-chain-management",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-management-and-global-supply-chain-management",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-management-and-innovation-and-enterprise",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-management-and-innovation-and-enterprise",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-management-and-marketing",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-management-and-marketing",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-marketing",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-marketing",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/msc-marketing",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/business/pg/2018-19/master-of-business-administration",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/art-design/pg/2018-19/photography",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/social-sciences/pg/2018-19/social-work",
# "https://www.ntu.ac.uk/study-and-courses/courses/find-your-course/art-design/pg/2018-19/textile-design-innovation",]
        for linkdict in links:
            u = linkdict.get("courseURL")
            # print(u)
            # for u in l:
            yield scrapy.Request(u, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.ntu.ac.uk/"
        item['university'] = "Nottingham Trent University"
        item['url'] = response.url
        # 授课方式
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        print("===============================")
        print(response.url)
        try:
            # 专业、学位类型
            programme = response.xpath("//h1[@class='course-heading page-heading']//text()").extract()
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en'] = ", item['programme_en'])

            degree_type = response.xpath("//h2[@class='js_qualification']/strong//text()").extract()
            item['degree_name'] = ''.join(degree_type)
            print("item['degree_name'] = ", item['degree_name'])

            #
            mode = response.xpath(
                "//strong[contains(text(),'Study mode(s):')]/following-sibling::span//text()").extract()
            clear_space(mode)
            # print("mode: ", mode)
            item['teach_time'] = getTeachTime(''.join(mode))
            # print("item['teach_time'] = ", item['teach_time'])

            # //div[@id='tabs-key-info']/div[@class='tab tab-1 active-tab']/p[3]/span
            location = response.xpath(
                "//span[@class='location save']//text()").extract()
            item['location'] = ''.join(location)
            # print("item['location'] = ", item['location'])

            start_date = response.xpath(
                "//strong[contains(text(),'Starting:')]/following-sibling::span//text()").extract()
            # print(start_date)
            item['start_date'] = ''.join(start_date)
            # print("item['start_date'] = ", item['start_date'])
            item['start_date'] = getStartDate(item['start_date'])
            # print("item['start_date']1 = ", item['start_date'])

            duration = response.xpath("//strong[contains(text(),'Course duration:')]/following-sibling::span//text()").extract()
            # print("duration: ", duration)
            duration_list = getIntDuration(''.join(duration))
            # print("duration_list: ", duration_list)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

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
                "//div[@id='entry-requirements-0']//text()").extract()
            item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            print("item['rntry_requirements'] = ", item['rntry_requirements'])

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

            # //html//div[@id='fees-and-funding-1']//tr/td[3]
            tuition_fee = response.xpath("//html//div[@id='fees-and-funding-1']//*[contains(text(),'Full')]/..//text()|"
                                         "//html//div[@id='fees-and-funding-1']//*[contains(text(),'full')]/../..//text()").extract()
            if len(tuition_fee) == 0:
                tuition_fee = response.xpath(
                    "//html//div[@id='fees-and-funding-1']//text()").extract()
            clear_space(tuition_fee)
            # print("tuition_fee: ", tuition_fee)
            tuition_fee = ''.join(tuition_fee)
            tuition_fee = getTuition_fee(tuition_fee)
            item['tuition_fee'] = tuition_fee
            if item['tuition_fee'] == 0:
                item['tuition_fee'] = None
            else:
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee'] = ", item['tuition_fee'])
            # print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])

            departmentDict = {"MSc / MRes Animal Health and Welfare": "School of Animal, Rural and Environmental Sciences",
"MRes Applied Anthrozoology": "School of Animal, Rural and Environmental Sciences",
"MSc / MRes Biodiversity Conservation": "School of Animal, Rural and Environmental Sciences",
"MSc / MRes Endangered Species Recovery and Conservation": "School of Animal, Rural and Environmental Sciences",
"MRes Equine Health and Welfare": "School of Animal, Rural and Environmental Sciences",
"MRes Equine Performance": "School of Animal, Rural and Environmental Sciences",
"MSc Equine Performance, Health and Welfare": "School of Animal, Rural and Environmental Sciences",
"MSc / MRes Global Food Security and Development": "School of Animal, Rural and Environmental Sciences",
"Architecture - Professional Certificate in": "School of Architecture, Design and the Built Environment",
"Architecture (ARB/RIBA Part 2) - MArch": "School of Architecture, Design and the Built Environment",
"Building Surveying - MSc": "School of Architecture, Design and the Built Environment",
"Civil Engineering - MSc": "School of Architecture, Design and the Built Environment",
"Construction Management - MSc": "School of Architecture, Design and the Built Environment",
"Construction Project Management (Online) - MSc": "School of Architecture, Design and the Built Environment",
"Interior Architecture and Design - MA": "School of Architecture, Design and the Built Environment",
"International Real Estate Investment and Finance - MSc": "School of Architecture, Design and the Built Environment",
"Planning and Development - MSc": "School of Architecture, Design and the Built Environment",
"Project Management (Construction) - MSc": "School of Architecture, Design and the Built Environment",
"Quantity Surveying - MSc": "School of Architecture, Design and the Built Environment",
"Real Estate - MSc": "School of Architecture, Design and the Built Environment",
"Structural Engineering with Management - MSc": "School of Architecture, Design and the Built Environment",
"Structural Engineering with Materials - MSc": "School of Architecture, Design and the Built Environment",
"MA Animation": "School of Art & Design",
"MA Commercial Photography": "School of Art & Design",
"MA Culture, Style and Fashion": "School of Art & Design",
"MA Branding and Identity": "School of Art & Design",
"MA Fashion Communications": "School of Art & Design",
"MA Fashion Design": "School of Art & Design",
"MA Fashion Knitwear Design": "School of Art & Design",
"MA Fashion Marketing": "School of Art & Design",
"MFA Fine Art": "School of Art & Design",
"MA Graphic Design": "School of Art & Design",
"MA Illustration": "School of Art & Design",
"MA International Fashion Management": "School of Art & Design",
"MA Luxury Fashion Brand Management": "School of Art & Design",
"MA Photography": "School of Art & Design",
"MA Textile Design Innovation": "School of Art & Design",
"MA Culture, Style and Fashion": "School of Art & Design",
"MA Fashion Communications": "School of Art & Design",
"MA Fashion Marketing": "School of Art & Design",
"MA Fashion and Textile Design": "School of Art & Design",
"MFA Fine Art": "School of Art & Design",
"MA Graphic Design Theory and Practice": "School of Art & Design",
"MA International Fashion Management": "School of Art & Design",
"MA Luxury Fashion Brand Management": "School of Art & Design",
"MA Photography": "School of Art & Design",
"PG Cert Creative Pattern Cutting (15 weeks)": "School of Art & Design",
"Art and Design Professional Doctorate": "School of Art & Design",
"Art and Design PhD / MPhil": "School of Art & Design",
"MA / PGDip Broadcast Journalism": "School of Arts and Humanities",
"MA / PGDip Digital and Newspaper Journalism": "School of Arts and Humanities",
"MA / PGDip Magazine Journalism": "School of Arts and Humanities",
"MA / PGDip Documentary Journalism": "School of Arts and Humanities",
"MA Media and Globalisation": "School of Arts and Humanities",
"MA Creative Writing": "School of Arts and Humanities",
"MRes English Literary Research": "School of Arts and Humanities",
"MA Linguistics (by research)": "School of Arts and Humanities",
"MA Philosophy (by research)": "School of Arts and Humanities",
"MA History": "School of Arts and Humanities",
"MA/ PGDip/ PGCert Museum and Heritage Development": "School of Arts and Humanities",
"MA Holocaust and Genocide (by research)": "School of Arts and Humanities",
"MA International Development": "School of Arts and Humanities",
"MA English Language Teaching": "School of Arts and Humanities",
"MA TESOL (Teaching English to Speakers of Other Languages)": "School of Arts and Humanities",
"MSc Management": "Nottingham Business School",
"MSc Management and Finance": "Nottingham Business School",
"MSc Management and Global Supply Chain Management": "Nottingham Business School",
"MSc Management and Innovation and Enterprise": "Nottingham Business School",
"MSc Management and International Business": "Nottingham Business School",
"MSc Management and Marketing": "Nottingham Business School",
"MSc Marketing": "Nottingham Business School",
"MSc Branding and Advertising": "Nottingham Business School",
"MSc Digital Marketing": "Nottingham Business School",
"MSc Management and Marketing": "Nottingham Business School",
"fees, funding and scholarships": "Nottingham Business School",
"Return to all courses": "Nottingham Business School",
"MSc Human resource Management (full-time)": "Nottingham Business School",
"MSc Economics": "Nottingham Business School",
"MSc Economics and Investment Banking": "Nottingham Business School",
"MSc International Business": "Nottingham Business School",
"MSc International Business (Dual Award) ": "Nottingham Business School",
"MSc Management and International Business": "Nottingham Business School",
"MSc Management and International Publishing": "Nottingham Business School",
"MSc Management and Global Supply Chain Management": "Nottingham Business School",
"MSc Finance": "Nottingham Business School",
"MSc Finance and Accounting": "Nottingham Business School",
"MSc Finance and Investment Banking": "Nottingham Business School",
"MSc Management and Finance": "Nottingham Business School",
"MSc Economics and Investment Banking": "Nottingham Business School",
"MSc Entrepreneurship": "Nottingham Business School",
"MSc Project Management": "Nottingham Business School",
"MSc Management": "Nottingham Business School",
"MSc Management and International Business": "Nottingham Business School",
"MSc Marketing": "Nottingham Business School",
"MSc Branding and Advertising": "Nottingham Business School",
"MSc Finance": "Nottingham Business School",
"MSc International Business": "Nottingham Business School",
"Assessment Only Route to QTS (Primary) - Non-NTU Award": "Nottingham Institute of Education",
"Assessment Only Route to QTS (Secondary) - Non-NTU Award": "Nottingham Institute of Education",
"Early Years Initial Teacher Training - PGCE": "Nottingham Institute of Education",
"Early Years Initial Teacher Training (Assessment Only) - Non-NTU Award": "Nottingham Institute of Education",
"Education, full-time - MA / PGCert / PGDip": "Nottingham Institute of Education",
"Education, Part-time - MA / PGCert / PGDip": "Nottingham Institute of Education",
"English Language Teaching - MA": "Nottingham Institute of Education",
"Post-Compulsory Education and Training - Cert Ed / PGCE / ProfGCE in": "Nottingham Institute of Education",
"Post-Compulsory Education and Training (with English and Literacy) - Cert Ed / PGCE / ProfGCE in": "Nottingham Institute of Education",
"Post-Compulsory Education and Training (with Mathematics and Numeracy) - Cert Ed / PGCE / ProfGCE in": "Nottingham Institute of Education",
"Post-Compulsory Education and Training (with Science, Engineering and Technology) - Cert Ed / PGCE / ProfGCE in": "Nottingham Institute of Education",
"Post-Compulsory Education and Training (with Special and Inclusive Practice) - Cert Ed / PGCE / ProfGCE in": "Nottingham Institute of Education",
"Primary Education - PGCE": "Nottingham Institute of Education",
"Primary: School-Centred Initial Teacher Training (SCITT) - PGCE": "Nottingham Institute of Education",
"School Direct Training Programme (Primary salaried) - PGCE": "Nottingham Institute of Education",
"School Direct Training Programme (Primary) - PGCE": "Nottingham Institute of Education",
"School Direct Training Programme (Secondary salaried) - PGCE": "Nottingham Institute of Education",
"School Direct Training Programme (Secondary) - PGCE": "Nottingham Institute of Education",
"Secondary Biology - PGCE": "Nottingham Institute of Education",
"Secondary Business Education - PGCE": "Nottingham Institute of Education",
"Secondary Chemistry - PGCE": "Nottingham Institute of Education",
"Secondary Computer Science with ICT - PGCE": "Nottingham Institute of Education",
"Secondary Education (Design and Technology) - PGCE": "Nottingham Institute of Education",
"Secondary Education (Physics) - PGCE": "Nottingham Institute of Education",
"Secondary English - PGCE": "Nottingham Institute of Education",
"Secondary Mathematics - PGCE": "Nottingham Institute of Education",
"Secondary Music - PGCE": "Nottingham Institute of Education",
"Special Educational Needs Coordination - National Award": "Nottingham Institute of Education",
"Teaching English to Speakers of Other Languages (TESOL) - MA": "Nottingham Institute of Education",
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
"MSc Biomedical Science": "School of Science and Technology",
"MSc Biomedical Science (Flexible Learning)": "School of Science and Technology",
"MSc Neuropharmacology": "School of Science and Technology",
"MSc Pharmacology": "School of Science and Technology",
"MSc Molecular Microbiology": "School of Science and Technology",
"MSc Biotechnology": "School of Science and Technology",
"MSc Molecular Cell Biology": "School of Science and Technology",
"MSc by Research Environmental Management": "School of Science and Technology",
"MRes Biotechnology": "School of Science and Technology",
"MRes Cancer Biology": "School of Science and Technology",
"MRes Cell Biology": "School of Science and Technology",
"MRes Molecular Biology": "School of Science and Technology",
"MRes Molecular Microbiology": "School of Science and Technology",
"MRes Neuropharmacology": "School of Science and Technology",
"MRes Pharmacology": "School of Science and Technology",
"MRes Environmental Management": "School of Science and Technology",
"MSc Biomedical Science (Flexible Learning)": "School of Science and Technology",
"MRes Environmental Management": "School of Science and Technology",
"MSc Chemistry / MSc Chemistry (Professional Practice)": "School of Science and Technology",
"MRes Pharmaceutical and Medicinal Science": "School of Science and Technology",
"MRes Pharmaceutical Analysis": "School of Science and Technology",
"MRes Analytical Chemistry": "School of Science and Technology",
"MRes Chemistry": "School of Science and Technology",
"MRes Advanced Materials Engineering": "School of Science and Technology",
"MSc Forensic Science": "School of Science and Technology",
"MSc Computer Science": "School of Science and Technology",
"MSc Cloud and Enterprise Computing": "School of Science and Technology",
"MSc IT Security": "School of Science and Technology",
"MSc Engineering (Electronics)": "School of Science and Technology",
"MSc Engineering (Cybernetics and Communications)": "School of Science and Technology",
"MSc Engineering Management": "School of Science and Technology",
"MSc Computing Systems": "School of Science and Technology",
"MSc Data Analytics for Business": "School of Science and Technology",
"MRes Computer Science": "School of Science and Technology",
"MRes Electronic Systems": "School of Science and Technology",
"Online MBA with Data Analytics": "School of Science and Technology",
"MRes Mathematical Sciences": "School of Science and Technology",
"MSc Data Analytics for Business": "School of Science and Technology",
"Online MBA with Data Analytics": "School of Science and Technology",
"MRes Medical and Materials Imaging": "School of Science and Technology",
"MRes Medical Imaging": "School of Science and Technology",
"MSc Physics": "School of Science and Technology",
"MRes Physics": "School of Science and Technology",
"MRes Sport Science": "School of Science and Technology",
"MRes Exercise Physiology": "School of Science and Technology",
"MRes Performance Nutrition": "School of Science and Technology",
"MRes Performance Analysis": "School of Science and Technology",
"MRes Biomechanics": "School of Science and Technology",
"MRes Sport and Exercise Psychology": "School of Science and Technology",
"MSc / PGDip Psychology": "School of Social Sciences",
"MSc Applied Child Psychology": "School of Social Sciences",
"MRes / MSc Psychological Research Methods": "School of Social Sciences",
"MSc Forensic Mental Health": "School of Social Sciences",
"MSc Forensic Psychology (BPS accredited)": "School of Social Sciences",
"MSc Cyberpsychology": "School of Social Sciences",
"MSc Psychology in Clinical Practice": "School of Social Sciences",
"MSc Psychological Wellbeing and Mental Health": "School of Social Sciences",
"MA Criminology": "School of Social Sciences",
"MA Sociology": "School of Social Sciences",
"MA Politics": "School of Social Sciences",
"MA International Relations": "School of Social Sciences",
"Online MA International Relations (Distance learning)": "School of Social Sciences",
"MA Public Health": "School of Social Sciences",
"PG Cert / MA Career Development": "School of Social Sciences",
"MA Social Work (January 2019 entry)": "School of Social Sciences", }
            departmentKey = item['degree_name'] + " " + item['programme_en']
            departmentKey1 = item['programme_en'] + " - " + item['degree_name']
            # print("departmentKey = ", departmentKey)
            # print("departmentKey1 = ", departmentKey1)
            item['department'] = departmentDict.get(departmentKey)
            if item['department'] == None:
                item['department'] = departmentDict.get(departmentKey1)
                if item['department'] == None:
                    item['department'] = departmentDict.get(item['programme_en'])
                    if item['department'] == None:
                        item['department'] = departmentDict.get(item['programme_en'].replace(" ", " "))
            # print("item['department'] = ", item['department'])

            if item['department'] == "School of Art & Design" or item['department'] == "School of Animal, Rural and Environmental Sciences" or item['department'] == "School of Science and Technology":
                item['ielts'] = 6.5
                item['ielts_l'] = 5.5
                item['ielts_s'] = 5.5
                item['ielts_r'] = 5.5
                item['ielts_w'] = 5.5
            elif item['department'] == "Nottingham Business School":
                item['ielts_desc'] = """For 1-year Masters you'll need a 6.5 grade overall with minimum of 5.5 in each component.
For 2-year Masters you'll need a 6.5 grade overall with a minimum of 6.0 in speaking and listening, and 5.5 in reading and writing."""
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
            print("item['ielts_desc']: ", item['ielts_desc'])

            if item['ielts'] == None:
                ieltsDict = get_ielts(''.join(ielts))
                item['ielts'] = ieltsDict.get("IELTS")
                item['ielts_l'] = ieltsDict.get("IELTS_L")
                item['ielts_s'] = ieltsDict.get("IELTS_S")
                item['ielts_r'] = ieltsDict.get("IELTS_R")
                item['ielts_w'] = ieltsDict.get("IELTS_W")
            print("item['IELTS'] = %sitem['IELTS_L'] = %sitem['IELTS_S'] = %sitem['IELTS_R'] = %sitem['IELTS_W'] = %s==" % (
                item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            item['require_chinese_en'] = """<div>Bachelors degree (four years or six years in medicine / dentistry) from recognised institution in China. 
Grades of 75% or above
Grades of 70% or above from 211 universities</div>"""
            yield item
        except Exception as e:
            with open("scrapySchool_England/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

