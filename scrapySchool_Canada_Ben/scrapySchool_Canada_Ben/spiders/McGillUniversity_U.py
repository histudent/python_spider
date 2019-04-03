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

class McGillUniversity_USpider(scrapy.Spider):
    name = "McGillUniversity_U"
    start_urls = ["https://mcgill.ca/undergraduate-admissions/programs"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        # 所有的本科课程链接
        all_links = response.xpath("//div[@id='tabs-2']/div[@class='paging-group']/div[@class='alphabetic-group']/ul[@class='programs-group']/li/a/@href").extract()
        # print(len(all_links))
        links = list(set(all_links))
        # 262
        # print(len(all_links))
        for link in all_links:
            url = "https://mcgill.ca" + link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)
        item['school_name'] = "McGill University"
        # item['campus'] = 'Montreal, Quebec, Canada'
        # item['location'] = 'Montreal, Quebec, Canada'
        item['url'] = response.url
        print("===========================")
        print(response.url)

        try:
            major_name_en = response.xpath("//div[@class='details']/h1//text()").extract()
            clear_space(major_name_en)
            item['major_name_en'] = ''.join(major_name_en).strip()
            print("item['major_name_en']: ", item['major_name_en'])

            department = response.xpath("//span[@class='value faculty']//text()").extract()
            item['department'] = department
            # if item['department'] == "":
            #     print("***department 为空")
            print("item['department']: ", item['department'])
            if len(item['department']) > 0:
                for dep in item['department']:
                    if dep in item['major_name_en']:
                        item['major_name_en'] = item['major_name_en'].replace(dep, '').replace('(', '').replace(')', '')
            item['major_name_en'] = item['major_name_en'].strip().strip('-').strip()
            print("item['major_name_en']2== ", item['major_name_en'])

            degree_name = response.xpath("//span[@class='value degree']//text()").extract()
            item['degree_name'] = ', '.join(degree_name).replace("Concurrent", '').strip()
            print("item['degree_name']: ", item['degree_name'])
            if item['degree_name'] == "Bachelor of Science, Bachelor of Science in Agricultural and Environmental Sciences" or item['degree_name'] == "Bachelor of Science in Agricultural and Environmental Sciences":
                item['degree_name'] = 'Bachelor of Science'

            overview = response.xpath("//p[contains(text(),'DETAILED PROGRAM OUTLINE')]/preceding-sibling::p[position()>1]").extract()
            if len(overview) == 0:
                overview = response.xpath(
                    "//div[@class='description']/p[position()<last()-1]").extract()

            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # if item['overview_en'] == "":
            #     print("***overview_en 为空")
            # print("item['overview_en']: ", item['overview_en'])

            # 第一种情况 页面含有major的学位
            # modules_en_major = response.xpath("//a[contains(text(),'Major ')]//text()").extract()
            modules_en_a = response.xpath("//a[contains(text(),'Major ')]/@href").extract()
            # print("***********")
            # print(len(modules_en_major))
            # print(modules_en_major)
            # # 每个专业分为多个专业，专业名不一样，需要匹配
            # if len(modules_en_major) > 0:
            #     for m in range(len(modules_en_major)):
            #         if '- Major ' + item['major_name_en'] + ' - ' not in modules_en_major[m] or '- Major ' + item['major_name_en'] + ': ' not in modules_en_major[m]:
            #             modules_en_major[m] = 'nono'
            # print(modules_en_major)
            # print('modules_en_a==', modules_en_a)
            # if len(modules_en_a) == 1:
            #     modules_en = response.xpath(
            #         "//a[contains(text(),'Major ')]/following-sibling::div//h3[contains(text(),'Program Requirement: ')]/preceding-sibling::*[1]/following-sibling::*[position()<last()]").extract()
            #     item['modules_en'] = remove_class(clear_lianxu_space(modules_en))
            modules_en_list = []
            major_en_list = []
            if len(modules_en_a) > 0:
                for modules_a in modules_en_a:
                    # print("***************", modules_a, "**************")
                    if "https://mcgill.ca/study/2018-2019/courses" not in modules_a:
                        modules_en_major_dict = self.parse_modules(modules_a)
                        modules_en = modules_en_major_dict['modules_en']
                        major_name_del = modules_en_major_dict['major_en_del']
                        modules_en_list.append(modules_en)
                        major_en_list.append(major_name_del)
            else:
                modules_en_a = response.xpath("//a[contains(text(),'Bachelor of')]/@href").extract()
                if len(modules_en_a) > 0:
                    # print(len(modules_en_a))
                    # print('1==', modules_en_a)
                    for i in range(len(modules_en_a)):
                        if "/undergraduate-admissions/" in modules_en_a[i]:
                            modules_en_a[i] = 'yes'
                    total_len = len(modules_en_a)
                    if 'yes' in modules_en_a:
                        modules_en_a.remove('yes')
                    # print(len(modules_en_a))
                    # print('2==', modules_en_a)
                    if len(modules_en_a) > 0:
                        if modules_en_a[0] == "yes":
                            modules_en_major_dict = self.parse_modules(modules_en_a[1])
                            modules_en = modules_en_major_dict['modules_en']
                            major_name_del = modules_en_major_dict['major_en_del']
                        else:
                            # modules_en = self.parse_modules(modules_en_a[0])
                            modules_en_major_dict = self.parse_modules(modules_en_a[0])
                            modules_en = modules_en_major_dict['modules_en']
                            major_name_del = modules_en_major_dict['major_en_del']
                        modules_en_list.append(modules_en)
                        major_en_list.append(major_name_del)
            print('modules_en_list=', len(modules_en_list))
            print('major_en_list=', len(major_en_list))

            # if item['modules_en'] == "":
            #     print("***modules_en 为空")
            # print("item['modules_en']: ", item['modules_en'])

            # https://mcgill.ca/applying/requirements/international/china#Process
            item['start_date'] = '9月'
            item['deadline'] = '2019-01-15'


            # https://mcgill.ca/applying/requirements/international/china#Process
            item['entry_requirements_en'] = """<h2>Admission review process</h2>
<p>Applicants will be considered for admission on their high school transcript (Grades 1, 2 and midyear grade 3) and all available results of the Huikao exams. Note that SAT cannot be used as a substitute for the Huikao/Academic Proficiency Test (APT).</p>
<p>Applicants from Chinese provinces where the Huikao is not offered must present additional external information of their academic credentials, such as SATI and SATII scores. If admitted to McGill, you must arrange for your school to send to McGill University an official final transcript of your complete high school record, the graduation certificate, and all final HUIKAO results.</p>
<p>If you write the GAOKAO, you must make arrangements to forward to us the final official results.</p>
<p>If admitted, you are expected to maintain your level of academic performance through to the completion of your pre-McGill studies.</p>
<h2><span>Minimum grades & prerequisites</span></h2>
<ul><li>The minimum requirements normally are averages of 85% or higher in each year and in all prerequisite courses. Many programs are more competitive and will require higher grades; applicants who present the minimum requirements are not guaranteed admission.</li>
</ul>"""
            item['average_score'] = 85
            # https://mcgill.ca/music/admissions/undergraduate/prepare
            item['require_chinese_en'] = '''
<div><ul><li>You need a high school diploma.</li>
<li>Your high school average must be 75% or higher if you're applying to a performance program, 80% or higher if you're applying to a music research program.</li>
<li>If you receive an offer of admission, it will be conditional upon successful graduation from ​high school and your final grades.</li>
<li>If you are admitted, we will determine whether you are eligible for advanced standing in your program by evaluating your placement exams and, if applicable, your:
	<ul><li>IB Diploma</li>
		<li>A levels</li>
		<li>French Baccaleaurate</li>
	</ul></li>
</ul></div>'''
            # https://mcgill.ca/applying/requirements/international/ib
            item['ib'] = '''Applicants will be considered for admission on their high school transcript and predicted IB results or, if already completed, on the final IB Diploma results. The Diploma with grades of 5 or better on each Higher and Standard Level subject is the minimum expected for most programs. Many programs are more competitive and will require higher grades.
Note: The Math Studies course is not acceptable for programs where math is a required prerequisite.
If admitted, you are expected to maintain your level of academic performance through to the completion of your pre-McGill studies.
A maximum of 30 credits of advanced standing may be granted for the International Baccalaureate Diploma.'''

            # https://www.mcgill.ca/applying/requirements/prep
            item['ielts_desc'] = 'The regular Academic test and the test for UKVI are both accepted. A band score of 6.5 or better; individual component scores of 6.0 or better. '
            item['ielts'] = '6.5'
            item['ielts_l'] = '6.0'
            item['ielts_s'] = '6.0'
            item['ielts_r'] = '6.0'
            item['ielts_w'] = '6.0'

            # https://www.mcgill.ca/applying/requirements/usa#SAT
            # https://mcgill.ca/transfercredit/prospective/ap
            # item['sat1_desc'] = ''
            # item['act_desc'] = ''
            item['toefl_code'] = item['sat_code'] = '0935'
            item['act_code'] = '5231'
            item['ap'] = '0935-00'
            item['other'] = '''问题清单：1.有些专业对应多个学位，意味着对应多个课程设置，三者之间关系的匹配比较复杂
                                    2.学费在单独页面，需要选择各个学位区分出学费，然后再匹配,导致有些学费是空的
                                    3.统一没有找到课程长度
                                    4.有些专业需要分多条，专业名不一样，没法做到每个拆分的专业的名都能准确的采集下来
                                    5.专业描述和课程设置、就业为空的是详情页没有的
                                    '''

            # 一个专业处于几个学院的情况
            if len(department) == 1:
                item['department'] = ''.join(item['department']).replace('(Macdonald Campus)', '').strip()
                if "Faculty of Agricultural & Environmental Sciences" in item['department']:
                    item['campus'] = 'Macdonald Campus'
                    item['location'] = "Ste. Anne de Bellevu"
                elif "Faculty of Science" in item['department'] and item['major_name_en'] == "Human Nutrition":
                    item['campus'] = 'Macdonald Campus'
                    item['location'] = "Ste. Anne de Bellevu"
                else:
                    item['campus'] = 'Downtown Campus'
                    item['location'] = "Montreal"

                if "Bachelor of Education" in item['degree_name'] or item['department'] == "Desautels Faculty of Management":
                    item['toefl'] = "100"
                elif "Bachelor of Music" in item['degree_name']:
                    item['toefl'] = "79-80"
                else:
                    # item['toefl_desc'] = 'minimum component score of 21 in each of reading, writing, listening, and speaking'
                    item['toefl'] = "90"
                    item['toefl_l'] = "21"
                    item['toefl_s'] = "21"
                    item['toefl_r'] = "21"
                    item['toefl_w'] = "21"

                item['apply_pre'] = 'CAD$'
                if item['department'] == "Faculty of Medicine":
                    item['apply_fee'] = '154.56'
                else:
                    item['apply_fee'] = '110.40'

                # https://www.mcgill.ca/undergraduate-admissions/yearly-costs
                item['tuition_fee_pre'] = 'CAD$'
                if "Bachelor of Music" in item['degree_name'] and "Bachelor of Education" in item['degree_name']:
                    item['tuition_fee'] = '17,799.30'
                elif "Bachelor of Science" in item['degree_name'] and "Bachelor of Education" in item['degree_name']:
                    item['tuition_fee'] = '17,799.30'
                elif "Bachelor of Arts and Science" in item['degree_name']:
                    item['tuition_fee'] = '17,799.30'
                elif item['major_name_en'] == "Kinesiology" or item['degree_name']=="Bachelor of Arts" or "Bachelor of Social Work" in item['degree_name'] or "Bachelor of Theology" in item['degree_name']:
                    item['tuition_fee'] = '16,815.6'
                elif "Licentiate in Music" in item['major_name_en'] or "Bachelor of Nursing (Integrated)" in item['degree_name'] or \
                        "(BScN)" in item['degree_name'] or "Occupational Therapy" in item['major_name_en'] or "Physical Therapy" in item['major_name_en'] or\
                        "Bachelor of Science in Agricultural and Environmental Sciences" in item['degree_name'] or "Bachelor of Science in Architecture" in item['degree_name'] or\
                        "Bachelor of Science in Food Science" in item['degree_name'] or "Bachelor of Science in Nutritional Science" in item['degree_name']:
                    item['tuition_fee'] = '18,782.7'

                elif "Bachelor of Engineering" in item['degree_name'] or item['degree_name'] == "Bachelor of Science" or item['degree_name'] == "Concurrent Bachelor of Civil Law (B.C.L) and Bachelor of Laws (LL.B)":
                    item['tuition_fee'] = '39,361.2'
                elif item['degree_name'] == "Bachelor of Commerce":
                    item['tuition_fee'] = '45,262.8'
                if item['tuition_fee'] is None and item['degree_name'] == 'Bachelor of Music':
                    item['tuition_fee'] = "18,782.7"
                if item['tuition_fee'] is None and item['degree_name'] == 'Bachelor of Education':
                    item['tuition_fee'] = "17,799.30"
                print("item['tuition_fee']: ", item['tuition_fee'])

                # 判断不是minor的课程
                is_minor = response.xpath("//span[@class='value option']//text()").extract()

                if "Bachelor of Science in Agricultural and Environmental Sciences" in item['degree_name'] or \
                        "Bachelor of Engineering in Bioresource Engineering" in item['degree_name'] or "Bachelor of Science in Food Science" in item['degree_name']:
                    item['specific_requirement_en'] = '''<ul><li>Subjects must include mathematics and two science courses in biology, chemistry, or physics as well as</li>
<li>Huikao exams in these subjects</li></ul>'''
                elif "Bachelor of Science in Architecture" in item['degree_name']:
                    item['specific_requirement_en'] = '''<ul><li>Subjects must include mathematics, physics and chemistry in the Grade 2 or 3 level</li>
<li>Huikao exams in mathematics and physics or chemistry</li>
<li>Applicants must submit a portfolio which will be taken into account during the admission process.</li></ul>'''
                elif "Bachelor of Arts and Science" in item['degree_name']:
                    item['specific_requirement_en'] = '''<ul><li>Subjects must include mathematics and two science courses in biology, chemistry, or physics in the Grade 2 or 3 level</li>
                    <li>Huikao exams in mathematics and two of biology, chemistry or physics</li></ul>'''
                elif "Secondary - Mathematics" in item['major_name_en']:
                    item['specific_requirement_en'] = '''<ul><li>Mathematics, at Senior Grade 2 or 3.</li></ul>'''
                elif "Secondary - Science and Technology" in item['major_name_en']:
                    item['specific_requirement_en'] = '''<ul><li>Subjects must include mathematics and at least two of biology, chemistry, or physics in the Grade 2 or 3 level; Huikao exams in these subjects. </li></ul>'''
                elif item['major_name_en'] == 'Bioengineering' or item['major_name_en'] == 'Chemical Engineering' or item[
                    'major_name_en'] == 'Civil Engineering' or item['major_name_en'] == 'Software Engineering' or \
                        item['major_name_en'] == 'Computer Engineering' or item['major_name_en'] == 'Electrical Engineering' or 'Mechanical Engineering' in item['major_name_en'] or \
                        'Materials Engineering' in item['major_name_en'] or 'Mining Engineering' in item['major_name_en']:
                    item['specific_requirement_en'] = '''<ul><li>Subjects must include mathematics, physics and chemistry in the Grade 2 or 3 level</li>
<li>Huikao exams in mathematics and physics or chemistry</li>
<li>Biology cannot be used as prerequisite</li></ul>'''
                elif "Human Nutrition" in item['major_name_en']:
                    item['specific_requirement_en'] = '''<ul><li>Subjects must include mathematics and two science courses in biology, chemistry, or physics as well as/li>
                                        <li>Huikao exams in these subjects</li></ul>'''
                elif item['major_name_en'] == 'Kinesiology':
                    item['specific_requirement_en'] = '''<ul><li>Subjects must include mathematics and at least two of biology, chemistry, or physics in the Grade 2 or 3 level/li>
                                        <li>Huikao exams in these subjects</li></ul>'''
                elif "Management" in item['major_name_en']:
                    item['specific_requirement_en'] = '''Subjects must include mathematics at grade 3 level</li>
                                        <li>Huikao exam in mathematics</li></ul>'''
                elif "Nursing" in item['major_name_en']:
                    item['specific_requirement_en'] = '''Subjects must include mathematics and at least two of biology, chemistry, or physics in the Grade 2 or 3 level</li>
                                        <li>Huikao exams in these subjects</li></ul>'''
                elif "Bachelor of Theology" in item['degree_name']:
                    item['specific_requirement_en'] = '''<h2>Admission Requirements</h2>
<p>The B.Th. program has three points of entry:</p>
<ol><li>To enter the 120-credit degree program from outside Quebec, the applicant must hold a high school diploma, with a minimum average of 75%, or the equivalent. A maximum of 60 credits from another institution of higher learning can be considered for transfer into the 120-credit program.</li>
<li>To enter the 90-credit first-degree program, the applicant is expected to have completed the Diploma of Collegial Studies (DCS) of a Quebec CEGEP with a minimum average Cote R of 24, or the equivalent elsewhere. A maximum of 30 credits from another institution of higher learning can be considered for transfer into this program.</li>
<li>To enter the 60-credit program, the applicant must have completed a B.A. or other Bachelor’s degree with a minimum CGPA of 2.7 (B-). No credits can be transferred from another institution of higher learning into the 60-credit program.</li>
</ol><p>Any McGill student in good standing, with a minimum of 30 credits, may apply for transfer from their current degree program into the B.Th. program. B.Th. students entering the 120- or 90-credit programs are free to pursue Minors in other departments, schools, or faculties, in consultation with their B.Th. adviser(s).</p>
<p>The B.Th. program extends over three academic years of full time studies for those admitted with a Diploma of Collegial Studies and over two academic years for those admitted with a Bachelor's degree. For all other students it requires four years. The normal load consists of five 3-credits courses (15 credits) each term.</p>'''
                elif 'Biological, Biomedical & Life Sciences' in ','.join(is_minor) or \
                        'Physical, Earth, Math & Computer Sciences' in ','.join(is_minor) or \
                        'Physical, Earth, Math and Computer Sciences' in ','.join(is_minor) or \
                        'Bio-Physical-Computational Sciences' in ','.join(is_minor):
                    item['specific_requirement_en'] = '''<ul><li>Subjects must include mathematics and at least two of biology, chemistry, or physics in the Grade 2 or 3 level</li>
<li>Huikao exams in these subjects</li></ul>'''

                # print("item['specific_requirement_en']: ", item['specific_requirement_en'])

                # Water Environments and Ecosystems
                if len(modules_en_list) > 0:
                    if len(modules_en_list) == len(major_en_list):
                        for m in range(len(modules_en_list)):
                            item['modules_en'] = modules_en_list[m]
                            item['major_name_en'] = major_en_list[m]
                            print('isminor: ', is_minor)
                            if 'online' not in item['major_name_en'] and 'Diploma' not in item['major_name_en'] and 'Diploma' not in item['degree_name'] and 'Minor' not in item[
                                'major_name_en'] and ''.join(is_minor) != 'Minor Concentration' and ''.join(is_minor) != 'Minor':
                                print('筛选之后的数据')
                                yield item
                            else:
                                if item['major_name_en'] == "Materials Engineering (Co-op & Minor)":
                                    yield item
                    else:
                        for m in modules_en_list:
                            item['modules_en'] = m
                            print('isminor: ', is_minor)
                            if 'online' not in item['major_name_en'] and 'Diploma' not in item['major_name_en'] and 'Diploma' not in item['degree_name'] and 'Minor' not in item[
                                'major_name_en'] and ''.join(is_minor) != 'Minor Concentration' and ''.join(is_minor) != 'Minor':
                                print('筛选之后的数据')
                                yield item
                            else:
                                if item['major_name_en'] == "Materials Engineering (Co-op & Minor)":
                                    yield item
            else:
                for dep in item['department']:
                    item['department'] = dep.replace('(Macdonald Campus)', '').strip()
                    if "Faculty of Agricultural & Environmental Sciences" in item['department']:
                        item['campus'] = 'Macdonald Campus'
                        item['location'] = "Ste. Anne de Bellevu"
                    elif "Faculty of Science" in item['department'] and item['major_name_en'] == "Human Nutrition":
                        item['campus'] = 'Macdonald Campus'
                        item['location'] = "Ste. Anne de Bellevu"
                    else:
                        item['campus'] = 'Downtown Campus'
                        item['location'] = "Montreal"

                    # item['department'] = ''.join(item['department'])
                    if "Bachelor of Education" in item['degree_name'] or item[
                        'department'] == "Desautels Faculty of Management":
                        item['toefl'] = "100"
                    elif "Bachelor of Music" in item['degree_name']:
                        item['toefl'] = "79-80"
                    else:
                        # item['toefl_desc'] = 'minimum component score of 21 in each of reading, writing, listening, and speaking'
                        item['toefl'] = "90"
                        item['toefl_l'] = "21"
                        item['toefl_s'] = "21"
                        item['toefl_r'] = "21"
                        item['toefl_w'] = "21"

                    item['apply_pre'] = 'CAD$'
                    if item['department'] == "Faculty of Medicine":
                        item['apply_fee'] = '154.56'
                    else:
                        item['apply_fee'] = '110.40'

                    # https://www.mcgill.ca/undergraduate-admissions/yearly-costs
                    item['tuition_fee_pre'] = 'CAD$'
                    if "Bachelor of Music" in item['degree_name'] and "Bachelor of Education" in item['degree_name']:
                        item['tuition_fee'] = '17,799.30'
                    elif "Bachelor of Science" in item['degree_name'] and "Bachelor of Education" in item[
                        'degree_name']:
                        item['tuition_fee'] = '17,799.30'
                    elif "Bachelor of Arts and Science" in item['degree_name']:
                        item['tuition_fee'] = '17,799.30'
                    elif item['major_name_en'] == "Kinesiology" or item[
                        'degree_name'] == "Bachelor of Arts" or "Bachelor of Social Work" in item[
                        'degree_name'] or "Bachelor of Theology" in item['degree_name']:
                        item['tuition_fee'] = '16,815.6'
                    elif "Licentiate in Music" in item['major_name_en'] or "Bachelor of Nursing (Integrated)" in item[
                        'degree_name'] or \
                            "(BScN)" in item['degree_name'] or "Occupational Therapy" in item[
                        'major_name_en'] or "Physical Therapy" in item['major_name_en'] or \
                            "Bachelor of Science in Agricultural and Environmental Sciences" in item[
                        'degree_name'] or "Bachelor of Science in Architecture" in item['degree_name'] or \
                            "Bachelor of Science in Food Science" in item[
                        'degree_name'] or "Bachelor of Science in Nutritional Science" in item['degree_name']:
                        item['tuition_fee'] = '18,782.7'

                    elif "Bachelor of Engineering" in item['degree_name'] or item[
                        'degree_name'] == "Bachelor of Science" or item[
                        'degree_name'] == "Concurrent Bachelor of Civil Law (B.C.L) and Bachelor of Laws (LL.B)":
                        item['tuition_fee'] = '39,361.2'
                    elif item['degree_name'] == "Bachelor of Commerce":
                        item['tuition_fee'] = '45,262.8'

                    if item['tuition_fee'] is None and item['degree_name'] == 'Bachelor of Music':
                        item['tuition_fee'] = "18,782.7"
                    if item['tuition_fee'] is None and item['degree_name'] == 'Bachelor of Education':
                        item['tuition_fee'] = "17,799.30"
                    print("item['tuition_fee']: ", item['tuition_fee'])

                    # 判断不是minor的课程
                    is_minor = response.xpath("//span[@class='value option']//text()").extract()

                    if "Bachelor of Science in Agricultural and Environmental Sciences" in item['degree_name'] or \
                            "Bachelor of Engineering in Bioresource Engineering" in item[
                        'degree_name'] or "Bachelor of Science in Food Science" in item['degree_name']:
                        item['specific_requirement_en'] = '''<ul><li>Subjects must include mathematics and two science courses in biology, chemistry, or physics as well as</li>
                    <li>Huikao exams in these subjects</li></ul>'''
                    elif "Bachelor of Science in Architecture" in item['degree_name']:
                        item['specific_requirement_en'] = '''<ul><li>Subjects must include mathematics, physics and chemistry in the Grade 2 or 3 level</li>
                    <li>Huikao exams in mathematics and physics or chemistry</li>
                    <li>Applicants must submit a portfolio which will be taken into account during the admission process.</li></ul>'''
                    elif "Bachelor of Arts and Science" in item['degree_name']:
                        item['specific_requirement_en'] = '''<ul><li>Subjects must include mathematics and two science courses in biology, chemistry, or physics in the Grade 2 or 3 level</li>
                                        <li>Huikao exams in mathematics and two of biology, chemistry or physics</li></ul>'''
                    elif "Secondary - Mathematics" in item['major_name_en']:
                        item['specific_requirement_en'] = '''<ul><li>Mathematics, at Senior Grade 2 or 3.</li></ul>'''
                    elif "Secondary - Science and Technology" in item['major_name_en']:
                        item[
                            'specific_requirement_en'] = '''<ul><li>Subjects must include mathematics and at least two of biology, chemistry, or physics in the Grade 2 or 3 level; Huikao exams in these subjects. </li></ul>'''
                    elif item['major_name_en'] == 'Bioengineering' or item['major_name_en'] == 'Chemical Engineering' or \
                            item[
                                'major_name_en'] == 'Civil Engineering' or item[
                        'major_name_en'] == 'Software Engineering' or \
                            item['major_name_en'] == 'Computer Engineering' or item[
                        'major_name_en'] == 'Electrical Engineering' or 'Mechanical Engineering' in item[
                        'major_name_en'] or \
                            'Materials Engineering' in item['major_name_en'] or 'Mining Engineering' in item[
                        'major_name_en']:
                        item['specific_requirement_en'] = '''<ul><li>Subjects must include mathematics, physics and chemistry in the Grade 2 or 3 level</li>
                    <li>Huikao exams in mathematics and physics or chemistry</li>
                    <li>Biology cannot be used as prerequisite</li></ul>'''
                    elif "Human Nutrition" in item['major_name_en']:
                        item['specific_requirement_en'] = '''<ul><li>Subjects must include mathematics and two science courses in biology, chemistry, or physics as well as/li>
                                                            <li>Huikao exams in these subjects</li></ul>'''
                    elif item['major_name_en'] == 'Kinesiology':
                        item['specific_requirement_en'] = '''<ul><li>Subjects must include mathematics and at least two of biology, chemistry, or physics in the Grade 2 or 3 level/li>
                                                            <li>Huikao exams in these subjects</li></ul>'''
                    elif "Management" in item['major_name_en']:
                        item['specific_requirement_en'] = '''Subjects must include mathematics at grade 3 level</li>
                                                            <li>Huikao exam in mathematics</li></ul>'''
                    elif "Nursing" in item['major_name_en']:
                        item['specific_requirement_en'] = '''Subjects must include mathematics and at least two of biology, chemistry, or physics in the Grade 2 or 3 level</li>
                                                            <li>Huikao exams in these subjects</li></ul>'''
                    elif "Bachelor of Theology" in item['degree_name']:
                        item['specific_requirement_en'] = '''<h2>Admission Requirements</h2>
                    <p>The B.Th. program has three points of entry:</p>
                    <ol><li>To enter the 120-credit degree program from outside Quebec, the applicant must hold a high school diploma, with a minimum average of 75%, or the equivalent. A maximum of 60 credits from another institution of higher learning can be considered for transfer into the 120-credit program.</li>
                    <li>To enter the 90-credit first-degree program, the applicant is expected to have completed the Diploma of Collegial Studies (DCS) of a Quebec CEGEP with a minimum average Cote R of 24, or the equivalent elsewhere. A maximum of 30 credits from another institution of higher learning can be considered for transfer into this program.</li>
                    <li>To enter the 60-credit program, the applicant must have completed a B.A. or other Bachelor’s degree with a minimum CGPA of 2.7 (B-). No credits can be transferred from another institution of higher learning into the 60-credit program.</li>
                    </ol><p>Any McGill student in good standing, with a minimum of 30 credits, may apply for transfer from their current degree program into the B.Th. program. B.Th. students entering the 120- or 90-credit programs are free to pursue Minors in other departments, schools, or faculties, in consultation with their B.Th. adviser(s).</p>
                    <p>The B.Th. program extends over three academic years of full time studies for those admitted with a Diploma of Collegial Studies and over two academic years for those admitted with a Bachelor's degree. For all other students it requires four years. The normal load consists of five 3-credits courses (15 credits) each term.</p>'''
                    elif 'Biological, Biomedical & Life Sciences' in ','.join(is_minor) or \
                            'Physical, Earth, Math & Computer Sciences' in ','.join(is_minor) or \
                            'Physical, Earth, Math and Computer Sciences' in ','.join(is_minor) or \
                            'Bio-Physical-Computational Sciences' in ','.join(is_minor):
                        item['specific_requirement_en'] = '''<ul><li>Subjects must include mathematics and at least two of biology, chemistry, or physics in the Grade 2 or 3 level</li>
                    <li>Huikao exams in these subjects</li></ul>'''

                    # print("item['specific_requirement_en']: ", item['specific_requirement_en'])

                    if len(modules_en_list) > 0:
                        if len(modules_en_list) == len(major_en_list):
                            for m in range(len(modules_en_list)):
                                item['modules_en'] = modules_en_list[m]
                                item['major_name_en'] = major_en_list[m]
                                print('isminor: ', is_minor)
                                if 'online' not in item['major_name_en'] and 'Diploma' not in item[
                                    'major_name_en'] and 'Diploma' not in item['degree_name'] and 'Minor' not in item[
                                    'major_name_en'] and ''.join(is_minor) != 'Minor Concentration' and ''.join(
                                    is_minor) != 'Minor':
                                    print('筛选之后的数据')
                                    yield item
                                else:
                                    if item['major_name_en'] == "Materials Engineering (Co-op & Minor)":
                                        yield item
                        else:
                            for m in modules_en_list:
                                item['modules_en'] = m
                                print('isminor: ', is_minor)
                                if 'online' not in item['major_name_en'] and 'Diploma' not in item[
                                    'major_name_en'] and 'Diploma' not in item['degree_name'] and 'Minor' not in item[
                                    'major_name_en'] and ''.join(is_minor) != 'Minor Concentration' and ''.join(
                                    is_minor) != 'Minor':
                                    print('筛选之后的数据')
                                    yield item
                                else:
                                    if item['major_name_en'] == "Materials Engineering (Co-op & Minor)":
                                        yield item


        except Exception as e:
            with open("scrapySchool_Canada_Ben/error/" + item['school_name'] + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)


    # 匹配多个modules的需要拆分
    def parse_modules(self, modules_a_url):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(modules_a_url, headers=headers_base)
        response = etree.HTML(data.text)

        major_en = response.xpath(
            "//h1[@id='page-title']//text()")
        print("major_en: ", major_en)
        major_en = ''.join(major_en).replace('Major Concentration', '').replace('Major', '').strip()
        del_re = re.findall(r"\(\d+\scredits\)", major_en)
        major_en_del = major_en.replace(''.join(del_re), '').strip()
        # print("major_en_del: ", major_en_del)

        modules_en = response.xpath(
            "//h3[contains(text(),'Program Requirements')]/..")
        modules_en_str = ""
        if len(modules_en) > 0:
            for m in modules_en:
                modules_en_str += etree.tostring(m, encoding='unicode', method='html')
                modules_en = remove_class(clear_lianxu_space([modules_en_str]))
        # print('modules_en: ', modules_en)
        modules_en_major_dict = {}
        modules_en_major_dict['major_en_del'] = major_en_del
        modules_en_major_dict['modules_en'] = modules_en
        return modules_en_major_dict