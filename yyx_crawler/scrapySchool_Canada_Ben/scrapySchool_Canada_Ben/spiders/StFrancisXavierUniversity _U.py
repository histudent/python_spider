__author__ = 'yangyaxia'
__date__ = '2018/10/25 09:00'
import scrapy
import re
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from w3lib.html import remove_tags
from lxml import etree
import requests

class StFrancisXavierUniversit_USpider(scrapy.Spider):
    name = "StFrancisXavierUniversity_U"
    start_urls = ["https://www.stfx.ca/academics"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        # 列表专业名和学院
        major_list = response.xpath("//span[@class='c-program__title']//text()").extract()
        department_list = response.xpath("//span[@class='c-program__faculty'][contains(text(),'Faculty of')]/..")

        # print(major_list)
        # print(department_list)
        # print(len(major_list))
        # print(len(department_list))

        '''匹配学院+专业名'''
        department_dict = {}
        for dep in range(len(department_list)):
            department = department_list[dep].xpath("./span[@class='c-program__faculty'][contains(text(),'Faculty of')]//text()").extract()
            # print('deparmrnt = ', department)
            department_dict[major_list[dep]] = department
        # print(department_dict)

        # 所有的本科课程链接
        all_links = response.xpath("//div[@class='o-container  c-program-search__slider  js-program-search-slider']/a/@href").extract()

        # print(len(all_links))
        links = ["/academics/schwartz-school/programs/accounting",
"/academics/schwartz-school/programs/enterprise-systems",
"/academics/schwartz-school/programs/entrepreneurship",
"/academics/schwartz-school/programs/finance",
"/academics/schwartz-school/programs/international-business",
"/academics/schwartz-school/programs/management-and-leadership",
"/academics/schwartz-school/programs/marketing", ]
        all_links = all_links+links
        # print(len(all_links))

        for link in all_links:
            if "http" not in link:
                url = "https://www.stfx.ca" + link
                # print(url)
                yield scrapy.Request(url, callback=self.parse_data, meta=department_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)
        item['school_name'] = "St. Francis Xavier University"
        item['campus'] = 'Antigonish'
        item['location'] = 'Antigonish'
        item['url'] = response.url
        print("===========================")
        print(response.url)

        try:
            major_name_en = response.xpath("//h1[@class='c-page-title c-page-title--hero']//text()").extract()
            clear_space(major_name_en)
            item['major_name_en'] = ''.join(major_name_en).strip()
            print("item['major_name_en']: ", item['major_name_en'])

            if 'online' not in item['major_name_en'] and 'Diploma' not in item['major_name_en']:

                overview = response.xpath("//html//div[@class='region region-content']/div[1]/div[1]").extract()
                item['overview_en'] = remove_class(clear_lianxu_space(overview))
                # if item['overview_en'] == "":
                #     print("***overview_en 为空")
                # print("item['overview_en']: ", item['overview_en'])

                career = response.xpath("//h3[contains(text(),'Career')]/..|//h3[contains(text(),'career')]/..").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career))
                # if item['career_en'] == "":
                #     print("***career_en 为空")
                # print("item['career_en']: ", item['career_en'])


                # https://www.stfx.ca/admissions/apply
                item['start_date'] = '1月, 9月'
                item['deadline'] = '2018-10-15,2019-05-30'
                if item['major_name_en'] == 'Nursing':
                    item['deadline'] = '2019-03-01'

                # https://www.stfx.ca/admissions/tuition-fees/intl-tuition-and-other-fees
                item['tuition_fee_pre'] = 'CAD$'
                item['tuition_fee'] = '8570'
                item['apply_pre'] = 'CAD$'
                item['apply_fee'] = '25'

                item['average_score'] = '70'

                # https://www.stfx.ca/admissions/requirements
                item['require_chinese_en'] = item['entry_requirements_en'] = '''<h3>GENERAL ADMISSION REQUIREMENTS</h3>
<p>For high school graduates, the minimum requirements include an overall average of 70% in Grade 12, with no marks below 65% in each of the required subjects.  Admissions to limited enrolment programs are competitive, thus, minimum grade requirements are subject to change.</p>'''
                if item['major_name_en'] == 'Nursing':
                    item['require_chinese_en'] = item['specific_requirement_en'] = item['entry_requirements_en'] = '''<div>
<div>
<div>
<p>All applicants interested in the Four-Year Traditional BSc Nursing program, Two-Year Accelerated program or LPN to BScN at StFX are required to complete a CASPer Assessment prior to their respective application deadlines.</p>
<p>This test is an online screening tool designed to evaluate the student’s personal and professional characteristics. The test is mandatory for all students who wish to be considered for Nursing. Knowing that academic knowledge is not always the best indicator of a superior applicant, CASPer allows our admissions team to gain a better understanding of each applicant, beyond cognitive measures. CASPer assesses non-cognitive skills and interpersonal characteristics.</p>
</div>
</div>
<div>
<div>
<h4><strong>Admissions Requirement:</strong></h4>
<ul><li>Applicants are required to complete a 90-minute online assessment (CASPer).</li>
<li>Successful completion of CASPer is mandatory in order to maintain admission eligibility.</li>
<li>CASPer can be attempted once during a StFX admission cycle.</li>
<li>Applicants will require a StFX student number to register for the CASPer test. (Student numbers are assigned at the point of application to StFX)</li>
<li>CASPer tests are also required for current StFX students who are applying to transfer to nursing.  </li>
</ul></div>
</div>
<div>
<div>
<h4><strong>Test Results:</strong></h4>
<ul><li>CASPer scores will be submitted directly to the institutions identified when registering for the test at takeCASPer.com.</li>
<li>Approximately three weeks after the test is complete scores will be received by StFX, and will be used in combination with academic performance to determine admissibility to the program.</li>
<li>CASPer scores are not released to applicants in an effort to protect the integrity of the test.</li>
<li>CASPer test results are valid for one StFX admission cycle.</li>
<li>Test results from previous years will not be considered.</li>
</ul></div>
</div></div>'''

                # https://www.stfx.ca/admissions/become-a-student-at-stfx/admissions-and-language-requirements
                item['ielts_desc'] = 'Students with an IELTS score of 6.5 and no band below 6.0 will be deemed to have satisfied the English language requirements for admissions to undergraduate programs at St. Francis Xavier University.'
                item['ielts'] = '6.5'
                item['ielts_l'] = '6.0'
                item['ielts_s'] = '6.0'
                item['ielts_r'] = '6.0'
                item['ielts_w'] = '6.0'
                item['toefl_desc'] = 'TOEFL (minimum score required is 92)'
                item['toefl'] = '92'


                # https://www.stfx.ca/admissions/requirements/international-baccalaureate
                item['ib'] = '''StFX welcomes and encourages applications from International Baccalaureate students.
Requirements
Students who complete the International Baccalaureate (IB) Diploma with a minimum score of 24 will be considered for admission
Minimum grade requirement for any subject is 3
Students can submit predicted or anticpated results for early fall admission and scholarship purposes
Transfer Credit
Students admitted to StFX with a score of 30 or higher on the IB Diploma, and who have received a score of at least 5 on all higher level and standard level courses, will be granted up to 30 credits.
Students who have any one minimum score falling below 5 will have their courses individually assessed for possible transfer credits.
Students who have completed IB courses but who do not possess the diploma, or who scored less than 30 on the IB Diploma, may receive individual university course credit if they have achieved grades of 5, 6, or 7 in higher level courses.
'''

                item['sat1_desc'] = 'SAT and ACT scores are NOT required for admission into any of these academic programs. An overall B average is required in these courses for admission into each respective program.'
                item['act_desc'] = 'SAT and ACT scores are NOT required for admission into any of these academic programs. An overall B average is required in these courses for admission into each respective program.'
                item['toefl_code'] = item['sat_code'] = item['act_code'] = '0953'

                item['other'] = '''问题清单：1.就业为空的是页面没有的
                2.修改学费、deadline、特殊专业要求(https://www.stfx.ca/admissions/requirements/international-admissions-requirements)
                3.有些课程设置为空是因为采集的课程设置列表没有那些专业http://www2.mystfx.ca/registrars-office/Course-Timetable
                '''
                modules_major = ["Anthropology",
"APEX",
"Aquatic Resources",
"Art",
"Biology",
"Business Administration",
"Catholic Studies",
"Celtic Studies",
"Chemistry",
"Classics",
"Climate and Environment",
"Computer Science",
"Co-operative Education",
"Development Studies",
"Earth Sciences",
"Economics",
"Engineering",
"English",
"French",
"German",
"Health",
"History",
"Human Kinetics",
"Human Nutrition",
"Interdisciplinary Studies",
"Mathematics",
"Mi'kmaq",
"Music",
"Nursing",
"Philosophy",
"Physics",
"Political Science",
"Psychology",
"Public Policy and Governance",
"Religious Studies",
"Sociology",
"Spanish",
"Sport Management",
"Statistics",
"Women's and Gender Studies", ]
                modules_url = ["https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=ANTH&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=APEX&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=AQUA&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=ART&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=BIOL&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=BSAD&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=CATH&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=CELT&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=CHEM&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=CLAS&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=CLEN&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=CSCI&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=COOP&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=DEVS&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=ESCI&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=ECON&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=ENGR&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=ENGL&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=FREN&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=GERM&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=HLTH&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=HIST&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=HKIN&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=HNU&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=IDS&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=MATH&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=MIKM&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=MUSI&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=NURS&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=PHIL&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=PHYS&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=PSCI&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=PSYC&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=PGOV&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=RELS&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=SOCI&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=SPAN&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=SMGT&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=STAT&pterm=201910",
"https://mesamis.stfx.ca/reports/Timetable_List.asp?pdept=WMGS&pterm=201910", ]
                modules_url_dict = {}
                for i in range(len(modules_major)):
                    modules_url_dict[modules_major[i]] = modules_url[i]
                # print('modules_url_dict: ', modules_url_dict)
                # 本专业的课程设置的链接
                major_modules_url = modules_url_dict.get(item['major_name_en'])
                if item['major_name_en'] == "Finance"  or item['major_name_en'] == "Management and Leadership"  or item['major_name_en'] == "Accounting"  or item['major_name_en'] == "International Business"  or item['major_name_en'] == "Enterprise Systems"  or item['major_name_en'] == "Marketing"  or item['major_name_en'] == "Entrepreneurship":
                    major_modules_url = modules_url_dict.get("Business Administration")
                if item['major_name_en'] == "Classical Studies":
                    major_modules_url = modules_url_dict.get("Classicsn")
                print(major_modules_url)
                if major_modules_url is not None:
                    item['modules_en'] = self.parse_modules(major_modules_url)
                print("item['modules_en']: ", item['modules_en'])

                department_list = response.meta.get(item['major_name_en'])
                if department_list is None and 'schwartz-school/' in response.url:
                    department_list = ['Gerald Schwartz School of Business']
                print("department_list: ", department_list)
                if len(department_list) > 0:
                    for dep in department_list:
                        item['department'] = dep.strip()
                        print("item['department']: ", item['department'])

                        item['degree_name'] = 'Bachelor of ' + item['department'] .replace('Faculty of', '').strip()
                        if item['department'] == "Gerald Schwartz School of Business":
                            item['degree_name'] = "Bachelor of Business Administration"
                        print("item['degree_name']: ", item['degree_name'])
                        # 特殊专业要求
                        if item['degree_name'] == "Bachelor of Business Administration":
                            item['specific_requirement_en'] = "<p>English 12, Math 12, and three one other university preparatory courses</p>"
                        elif item['major_name_en'] == "Health":
                            item['specific_requirement_en'] = "<p>English 12, two of (Math 12, Chemistry 12, Biology 12, Physics 12), and two other university preparatory courses</p>"
                        elif item['major_name_en'] == "Climate and Environment":
                            item['specific_requirement_en'] = "<p>English 12, two of (Math 12, Chemistry 12, Biology 12, Physics 12), and two other university preparatory courses</p>"
                        elif item['degree_name'] == "Bachelor of Arts":
                            if item['major_name_en'] == "Human Kinetics":
                                item['specific_requirement_en'] = "<p>English 12, one of (Math 12, Chemistry 12, Biology 12, Physics 12), and three other university preparatory courses</p>"
                            else:
                                item['specific_requirement_en'] = "<p>English 12 and four other university preparatory courses</p>"
                        elif item['degree_name'] == "Bachelor of Science":
                            if item['major_name_en'] == "Human Kinetics":
                                item['specific_requirement_en'] = "<p>English 12, two of (Math 12, Chemistry 12, Biology 12, Physics 12), and two other university preparatory courses</p>"
                            elif item['major_name_en'] == "Nursing":
                                item['specific_requirement_en'] = "<p>English 12, Math 12, Chemistry 12, Biology 12, one other university preparatory course, successful completion of CASPer*</p>"
                            elif item['major_name_en'] == "Human Nutrition":
                                item['specific_requirement_en'] = "<p>English 12, Math, two of (Chemistry 12, Biology 12, Physics 12) and one other university preparatory course</p>"
                            elif item['major_name_en'] == "Engineering":
                                item['specific_requirement_en'] = "<p>English 12, Pre-Calculus 12 or Calculus 12, Chemistry 12, one of Biology 12 or Physics 12 (Physics recommended), and one other university preparatory course</p>"
                            elif item['major_name_en'] == "Aquatic Resources":
                                item['specific_requirement_en'] = "<p>English 12, Pre Calculus 12 or Calculus 12, two of (Biology 12, Chemistry 12, Physics 12) and one other university preparatory course</p>"
                            else:
                                item['specific_requirement_en'] = "<p>English 12, Pre Calculus 12 or Calculus 12, two of (Biology 12, Chemistry 12, Physics 12) and one other university preparatory course</p>"
                        yield item
                else:
                    yield item

        except Exception as e:
            with open("scrapySchool_Canada_Ben/error/" + item['school_name'] + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_modules(self, major_modules_url):
        from selenium import webdriver
        # import time
        # os.chdir(r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Lib\site-packages\selenium")
        driver = webdriver.Chrome(r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Lib\site-packages\selenium\chromedriver.exe")
        driver.get(major_modules_url)
        # time.sleep(3)
        modules_en = driver.find_element_by_xpath("//table[@cellpadding='3']").get_attribute('outerHTML')
        modules_en = remove_class(clear_lianxu_space([modules_en]))
        driver.quit()
        return modules_en