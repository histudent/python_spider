# -*- coding:utf-8 -*-
"""
# @PROJECT: scrapySchool_Canada_Ben
# @Author: admin
# @Date:   2018-11-07 17:33:15
# @Last Modified by:   admin
# @Last Modified time: 2018-11-07 17:33:15
"""
import scrapy
import re
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from w3lib.html import remove_tags
from lxml import etree
import requests

class YorkUniversity_USpider(scrapy.Spider):
    name = "YorkUniversity_U"
    start_urls = ["http://futurestudents.yorku.ca/program-search"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        links = response.xpath("//div[@id='main']//div[contains(@class, 'fs-program undergrad')]/div[2]/a/@href").extract()
        print(len(links))
        links = list(set(links))
        # 76
        print(len(links))
        for link in links:
            url = "http://futurestudents.yorku.ca" + link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)
        item['school_name'] = "York University"
        item['url'] = response.url
        print("===========================")
        print(response.url)

        item['other'] = '''问题描述：1.专业描述和课程设置、就业为空的是详情页没有的
        2.entry_requirements没有找到
        3.雅思托福是根据专业名、学院或者学位判断的，存在个别的为空
        4.没有找到课程长度'''

        '''公共字段'''
        # item['campus'] = 'Toronto'
        item['location'] = 'Toronto'

        # http://futurestudents.yorku.ca/requirements/usa
        item['sat_code'] = item['toefl_code'] = '0894'
        item['act_code'] = '5250'
        item['sat1_desc'] = '1170'
        item['act_desc'] = '24'
        item['ap'] = "Transfer credit granted for final scores of 4 or 5 on the Advanced Placement (AP) exams, depending on the program (maximum 30 credits)."

        # http://futurestudents.yorku.ca/requirements/apply
        item['apply_pre'] = 'CAD$'
        item['apply_fee'] = '120'


        # item['entry_requirements_en'] = """<strong>IF YOU ARE A HIGH SCHOOL STUDENT</strong>
        # <p>If you’re coming to university directly from high school or have completed less than one year of university studies, you’ll take the direct entry route into a faculty or program: this means beginning in University 1 (U1), or applying to a program that offers a direct entry option. U1 is a unique approach to your first year at the U of M, giving you the opportunity to design an individualized schedule that meets the admission and/or first year requirements for one or more target degree programs. U1 will not add any time or cost to your degree; it serves as year 1 of any 3 or 4 year degree program</p>"""

        # item['alevel'] = 'General Certificate of Education (GCE) – 2 A Level Courses (or equivalent)'

        # http://futurestudents.yorku.ca/requirements
        item['average_score'] = '75'
        try:
            major_name_en = response.xpath("//h1[@id='page-title']//text()").extract()
            if "/" in ''.join(major_name_en).strip():
                m = ''.join(major_name_en).strip().split("/")
                item['major_name_en'] = ''.join(m[:-1]).strip()
            else:
                item['major_name_en'] = ''.join(major_name_en).strip()
            print("item['major_name_en']: ", item['major_name_en'])

            department = response.xpath("//div[@class='fs-ug-program-details']//label[contains(text(),'Offered by')]/../div//text()").extract()
            item['department'] = ', '.join(department).strip()
            print("item['department']: ", item['department'])

            degree_name = response.xpath("//div[@class='fs-ug-program-details']//label[contains(text(),'Degrees Offered')]/../div//text()").extract()
            item['degree_name'] = ''.join(degree_name).strip()
            print("item['degree_name']: ", item['degree_name'])

            # is_campus = "Biology, Business Economics, Canadian Studies, Communications, Drama Studies, Economics, Education, English, French Studies , Gender & Women’s Studies, History, International Studies, International Studies & Business Administration dual degree, emlyon Business School, Linguistics & Language Studies, Mathematics, Philosophy, Political Science, Psychology, Sexuality Studies , Sociology, Spanish (Hispanic Studies), Translation, Undecided Major"
            if "Glendon" in item['department']:
                item['campus'] = "Glendon"
            else:
                if item['degree_name'] == 'BEd':
                    item['campus'] = "Glendon"
                else:
                    item['campus'] = "Keele"

            if "Certificate" not in item['degree_name'] and "JD" not in item['degree_name']:
                # http://futurestudents.yorku.ca/requirements/deadlines
                start_date = response.xpath("//div[@class='fs-ug-program-details']//label[contains(text(),'Offered in')]/../div//text()").extract()
                start_date_tmp = ''.join(start_date).strip()
                print("start_date_tmp: ", start_date_tmp)
                start_date_list = []
                if "Fall" in start_date_tmp:
                    start_date_list.append("9月")
                if "Winter" in start_date_tmp:
                    start_date_list.append("1月")
                if "Summer" in start_date_tmp:
                    start_date_list.append("5月")
                item['start_date'] = ','.join(start_date_list).strip()
                print("item['start_date']: ", item['start_date'])

                # deadline  三种情况
                deadline_list = []
                if "9月" in item['start_date']:
                    if item['major_name_en'] == "Business Administration":
                        deadline_list.append('2019-01-30')
                    elif item['major_name_en'] == "Cinema & Media Studies" or item['major_name_en'] == "Dance" or item['major_name_en'] == "Design" or \
                            item['major_name_en'] == "Digital Media" or item['major_name_en'] == "Music" or item['major_name_en'] == "Theatre" or item['major_name_en'] == "Visual Arts":
                        deadline_list.append('2019-01-16')
                    elif item['major_name_en'] == "Social Work":
                        deadline_list.append('2019-02-06')
                    else:
                        deadline_list.append('2019-03-06')
                if "1月" in item['start_date']:
                    if item['major_name_en'] == "Media Arts" or item['major_name_en'] == "Dance" or item['major_name_en'] == "Music" \
                            or item['major_name_en'] == "Intermedia" or item['major_name_en'] == "Visual Arts":
                        deadline_list.append('2018-10-31')
                    else:
                        deadline_list.append('2019-11-15')
                if "5月" in item['start_date']:
                    if item['major_name_en'] == "Media Arts" or item['major_name_en'] == "Film Production" or item['major_name_en'] == "Dance" or item['major_name_en'] == "Music" \
                            or item['major_name_en'] == "Theatre" or item['major_name_en'] == "Intermedia" or item['major_name_en'] == "Visual Arts":
                        deadline_list.append('2019-01-16')
                    else:
                        deadline_list.append('2019-04-01')
                # print(deadline_list)
                item['deadline'] = ','.join(deadline_list).strip()
                # print("item['deadline']: ", item['deadline'])

                overview = response.xpath("//div[@class='field-item even']").extract()
                if len(overview) > 0:
                    item['overview_en'] = remove_class(clear_lianxu_space(overview)).replace("<p></p>", "").strip()
                # print("item['overview_en']: ", item['overview_en'])

                modules = response.xpath("""//h3[contains(text(),'Sample First-year Schedule')]/..|
                //strong[contains(text(),"Courses You'll Take")]/../following-sibling::ul[1]|
                //strong[contains(text(),'Some Courses You’ll Take')]/../following-sibling::ul[1]|
                //h3[contains(text(),'Some Courses You’ll Take')]/following-sibling::ul[1]""").extract()
                if len(modules) == 0 or ''.join(modules) == "<ul></ul>":
                    modules = response.xpath("//h3[contains(text(),'Some Courses You’ll Take')]/following-sibling::p[1]").extract()
                if len(modules) > 0:
                    item['modules_en'] = remove_class(clear_lianxu_space(modules)).replace("<p></p>", "").strip()
                if item['modules_en'] is None:
                    modules_url = response.xpath("//label[contains(text(),'For more information')]/following-sibling::div//a/@href").extract()
                    if len(modules_url) > 0:
                        modules_en_duration_dict = self.parse_modules(modules_url[0])
                        item['modules_en'] = modules_en_duration_dict.get('modules_en')
                        item['duration'] = modules_en_duration_dict.get('duration')
                        item['duration_per'] = modules_en_duration_dict.get('duration_per')
                print("item['modules_en']: ", item['modules_en'])
                print("item['duration']: ", item['duration'])
                print("item['duration_per']: ", item['duration_per'])

                career = response.xpath("//h3[contains(text(),'Possible Career Paths')]/..").extract()
                if len(career) > 0:
                    item['career_en'] = remove_class(clear_lianxu_space(career)).replace("<p></p>", "").strip()
                # print("item['career_en']: ", item['career_en'])

                # //a[contains(text(),'portfolio')]/..
                portfolio_desc_en = response.xpath("//a[contains(text(),'portfolio')]/..//text()").extract()
                if len(portfolio_desc_en) > 0:
                    item['portfolio_desc_en'] = clear_lianxu_space(portfolio_desc_en)
                print("item['portfolio_desc_en']: ", item['portfolio_desc_en'])

                interview_desc_en = response.xpath("//*[contains(text(),'interview')]//text()").extract()
                if len(interview_desc_en) > 0:
                    item['interview_desc_en'] = clear_lianxu_space(interview_desc_en)
                print("item['interview_desc_en']: ", item['interview_desc_en'])

                # 有多个学位的需要拆分成多条
                if "," in item['degree_name'].replace("(Bilingual, Trilingual)", "").strip():
                    degree_name_list = item['degree_name'].replace("(Bilingual, Trilingual)", "").strip().split(',')
                    for d in range(len(degree_name_list)):
                        item['degree_name'] = degree_name_list[d].strip()

                        # http://futurestudents.yorku.ca/requirements/language-tests
                        if item['department'] == "School of the Arts, Media, Performance & Design" or item['department'] == "Faculty of Environmental Studies" \
                                or item['department'] == "Liberal Arts & Professional Studies" or item['department'] == "Faculty of Science" or item['department'] == "Glendon":
                            item['ielts'] = '6.5'
                            item['toefl'] = '83'
                        elif item['department'] == "Faculty of Health":
                            if "Nursing" not in item['major_name_en']:
                                item['ielts'] = '6.5'
                                item['toefl'] = '83'
                            else:
                                item['ielts'] = '7'
                                item['toefl'] = '89'
                        elif item['department'] == "Lassonde School of Engineering":
                            if "BEng" not in item['degree_name']:
                                item['ielts'] = '6.5'
                                item['toefl'] = '83'
                            else:
                                item['ielts'] = '7.5'
                                item['toefl'] = '96-99'
                        elif item['department'] == "Schulich School of Business":
                            item['ielts'] = '7.5'
                            item['toefl'] = '100'
                        elif item['degree_name'] == "BEd":
                            item['ielts_desc'] = 'An overall score of at least 7 on the IELTS (academic test only), with scores of at least 6.5 in reading and listening and scores of at least 7 in writing and speaking.'
                            item['ielts'] = '7.0'
                            item['ielts_l'] = '6.5'
                            item['ielts_s'] = '7.0'
                            item['ielts_r'] = '6.5'
                            item['ielts_w'] = '7.0'
                            item['toefl_desc'] = 'A minimum overall score of 103, with scores of at least 23 in Listening, 24 in Reading, 28 in Writing and 28 in Speaking. '
                            item['toefl'] = '103'
                            item['toefl_l'] = '23'
                            item['toefl_s'] = '28'
                            item['toefl_r'] = '24'
                            item['toefl_w'] = '28'


                        # http://futurestudents.yorku.ca/tuition
                        item['tuition_fee_pre'] = 'CAD$'
                        if item['department'] == "Lassonde School of Engineering":
                            if item['major_name_en'] == "Computer Security" or item['major_name_en'] == "Digital Media" or item['major_name_en'] == "Earth & Atmospheric Science":
                                item['tuition_fee'] = '26,975.40'
                            elif item['major_name_en'] == "Computer Science":
                                item['tuition_fee'] = '27,206.40'
                            elif item['degree_name'] == "BEng":
                                item['tuition_fee'] = '33,880.32'
                        elif item['department'] == "Lassonde School of Engineering":
                            item['tuition_fee'] = '29,469.60'
                        elif item['major_name_en'] == "Design":
                            item['tuition_fee'] = '25,198.81'
                        else:
                            item['tuition_fee'] = "26,975"


                        # http://futurestudents.yorku.ca/requirements
                        chinese_requirement_pre = """<h4>MINIMUM REQUIREMENTS</h4>
        <ul><li>Senior Secondary School Graduation Certificate</li>
        <li>Successful completion of the final year of Senior 3/Grade 12 level of study with a minimum overall average of 75% on all academic courses.</li>
        <li>Some programs require a higher GPA. Please review the requirements for your program below.</li></ul>"""
                        # item['require_chinese_en'] = '<p></p>'
                        uuid = response.xpath("//div[@id='fs-admit-req-wrapper']/script//text()").extract()
                        clear_space(uuid)
                        uuid = ''.join(uuid).strip()
                        print("uuid2: ", uuid)
                        if "=" in uuid:
                            uuid = uuid.split("=")[-1].strip().strip("[").strip("]").strip()
                            # print("uuid1: ", uuid)
                            uuidUpdate = ""
                            ibUrl = ""
                            chineseHighSchoolUrl = ""
                            if "," in uuid:
                                uuidUpdate = uuid.split(",")
                                for i in range(len(uuidUpdate)):
                                    uuidUpdate[i] = uuidUpdate[i].strip().strip("'")
                                ibUrlTmp = ""
                                for uuidstr in uuidUpdate:
                                    ibUrlTmp += "&uuid%5B%5D=" + uuidstr
                                ibUrl = "http://futurestudents.yorku.ca/ajax/admit-req?applicant-type=highschool&cohort=ibcc" + ibUrlTmp
                                chineseHighSchoolUrl = "http://futurestudents.yorku.ca/ajax/admit-req?applicant-type=highschool&cohort=chs" + ibUrlTmp
                                alevelUrl = "http://futurestudents.yorku.ca/ajax/admit-req?applicant-type=highschool&cohort=gce" + ibUrlTmp
                            else:
                                uuidUpdate = uuid.strip().strip("'").strip()
                                ibUrl = "http://futurestudents.yorku.ca/ajax/admit-req?applicant-type=highschool&cohort=ibcc&uuid%5B%5D=" + uuidUpdate
                                chineseHighSchoolUrl = "http://futurestudents.yorku.ca/ajax/admit-req?applicant-type=highschool&cohort=chs&uuid%5B%5D=" + uuidUpdate
                                alevelUrl = "http://futurestudents.yorku.ca/ajax/admit-req?applicant-type=highschool&cohort=gce&uuid%5B%5D=" + uuidUpdate
                            # print("ibUrl: ", ibUrl)
                            # print("uuidUpdate: ", uuidUpdate)
                            # print("chineseHighSchoolUrl: ", chineseHighSchoolUrl)
                            '''ib'''
                            ib_html = etree.HTML(self.parse_IB(ibUrl).replace("\/", "/").strip())
                            # //div[@class='fs-admit-req-general-req']/following-sibling::div
                            # //div//h3[contains(text(), '"+item['degree_name']+"')]/../div
                            ib = ib_html.xpath("//div[@class='fs-admit-req-general-req']/following-sibling::div")
                            if len(ib) == 1:
                                item['ib'] = remove_tags(etree.tostring(ib[0], encoding='unicode')).replace("&#13;", "").replace("Requirements for admission", "\nRequirements for admission").replace("Transfer credit", "\nTransfer credit").strip()
                            else:
                                item['ib'] = remove_tags(etree.tostring(ib[d], encoding='unicode')).replace("&#13;", "").replace("Requirements for admission", "\nRequirements for admission").replace("Transfer credit", "\nTransfer credit").strip()

                            '''中国学生要求'''
                            # 从接口获取了require_chinese_en中国学生要求数据，需要二次解析
                            require_chinese_link = self.parse_IB(chineseHighSchoolUrl)
                            require_chinese_html = etree.HTML(require_chinese_link.replace("\/", "/").strip())
                            # //div[@class='fs-admit-req-general-req']/following-sibling::div
                            # //div//h3[contains(text(), '"+item['degree_name']+"')]/../div
                            require_chinese = require_chinese_html.xpath("//div[@class='fs-admit-req-general-req']/following-sibling::div")
                            if len(require_chinese) == 1:
                                item['require_chinese_en'] = etree.tostring(require_chinese[0], encoding='unicode')
                            else:
                                item['require_chinese_en'] = etree.tostring(require_chinese[d], encoding='unicode')

                            '''alevel'''
                            alevel_html = etree.HTML(self.parse_IB(alevelUrl).replace("\/", "/").strip())
                            alevel = alevel_html.xpath("//div[@class='fs-admit-req-general-req']/following-sibling::div")
                            if len(alevel) == 1:
                                item['alevel'] = remove_tags(etree.tostring(alevel[0], encoding='unicode'))
                            else:
                                item['alevel'] = remove_tags(etree.tostring(alevel[d], encoding='unicode'))

                        if item['require_chinese_en'] is None:
                            item['require_chinese_en'] = ""
                        item['require_chinese_en'] = chinese_requirement_pre +'\n'+ remove_class(clear_lianxu_space([item['require_chinese_en']]))
                        # print("item['require_chinese_en']: ", str(d), item['require_chinese_en'], "===\n===", item['major_name_en'])
                        # print("item['ib']2: ", str(d), item['ib'])
                        print("item['alevel']2: ", str(d), item['alevel'])

                        yield item
                else:
                    # http://futurestudents.yorku.ca/requirements/language-tests
                    if item['department'] == "School of the Arts, Media, Performance & Design" or item['department'] == "Faculty of Environmental Studies" \
                            or item['department'] == "Liberal Arts & Professional Studies" or item[
                        'department'] == "Faculty of Science" or item['department'] == "Glendon":
                        item['ielts'] = '6.5'
                        item['toefl'] = '83'
                    elif item['department'] == "Faculty of Health":
                        if "Nursing" not in item['major_name_en']:
                            item['ielts'] = '6.5'
                            item['toefl'] = '83'
                        else:
                            item['ielts'] = '7'
                            item['toefl'] = '89'
                    elif item['department'] == "Lassonde School of Engineering":
                        if "BEng" not in item['degree_name']:
                            item['ielts'] = '6.5'
                            item['toefl'] = '83'
                        else:
                            item['ielts'] = '7.5'
                            item['toefl'] = '96-99'
                    elif item['department'] == "Schulich School of Business":
                        item['ielts'] = '7.5'
                        item['toefl'] = '100'
                    elif item['degree_name'] == "BEd":
                        item[
                            'ielts_desc'] = 'An overall score of at least 7 on the IELTS (academic test only), with scores of at least 6.5 in reading and listening and scores of at least 7 in writing and speaking.'
                        item['ielts'] = '7.0'
                        item['ielts_l'] = '6.5'
                        item['ielts_s'] = '7.0'
                        item['ielts_r'] = '6.5'
                        item['ielts_w'] = '7.0'
                        item[
                            'toefl_desc'] = 'A minimum overall score of 103, with scores of at least 23 in Listening, 24 in Reading, 28 in Writing and 28 in Speaking. '
                        item['toefl'] = '103'
                        item['toefl_l'] = '23'
                        item['toefl_s'] = '28'
                        item['toefl_r'] = '24'
                        item['toefl_w'] = '28'

                    # http://futurestudents.yorku.ca/tuition
                    item['tuition_fee_pre'] = 'CAD$'
                    if item['department'] == "Lassonde School of Engineering":
                        if item['major_name_en'] == "Computer Security" or item['major_name_en'] == "Digital Media" or \
                                item['major_name_en'] == "Earth & Atmospheric Science":
                            item['tuition_fee'] = '26,975.40'
                        elif item['major_name_en'] == "Computer Science":
                            item['tuition_fee'] = '27,206.40'
                        elif item['degree_name'] == "BEng":
                            item['tuition_fee'] = '33,880.32'
                    elif item['department'] == "Lassonde School of Engineering":
                        item['tuition_fee'] = '29,469.60'
                    elif item['major_name_en'] == "Design":
                        item['tuition_fee'] = '25,198.81'
                    else:
                        item['tuition_fee'] = "26,975"

                    # http://futurestudents.yorku.ca/requirements
                    chinese_requirement_pre = """<h4>MINIMUM REQUIREMENTS</h4>
                            <ul><li>Senior Secondary School Graduation Certificate</li>
                            <li>Successful completion of the final year of Senior 3/Grade 12 level of study with a minimum overall average of 75% on all academic courses.</li>
                            <li>Some programs require a higher GPA. Please review the requirements for your program below.</li></ul>"""
                    # item['require_chinese_en'] = '<p></p>'
                    uuid = response.xpath("//div[@id='fs-admit-req-wrapper']/script//text()").extract()
                    clear_space(uuid)
                    uuid = ''.join(uuid).strip()
                    print("uuid1: ", uuid)
                    if "=" in uuid:
                        uuid = uuid.split("=")[-1].strip().strip("[").strip("]").strip()
                        # print("uuid1: ", uuid)
                        uuidUpdate = ""
                        ibUrl = ""
                        chineseHighSchoolUrl = ""
                        if "," in uuid:
                            uuidUpdate = uuid.split(",")
                            for i in range(len(uuidUpdate)):
                                uuidUpdate[i] = uuidUpdate[i].strip().strip("'")
                            ibUrlTmp = ""
                            for uuidstr in uuidUpdate:
                                ibUrlTmp += "&uuid%5B%5D=" + uuidstr
                            ibUrl = "http://futurestudents.yorku.ca/ajax/admit-req?applicant-type=highschool&cohort=ibcc" + ibUrlTmp
                            chineseHighSchoolUrl = "http://futurestudents.yorku.ca/ajax/admit-req?applicant-type=highschool&cohort=chs" + ibUrlTmp
                            alevelUrl = "http://futurestudents.yorku.ca/ajax/admit-req?applicant-type=highschool&cohort=gce" + ibUrlTmp
                        else:
                            uuidUpdate = uuid.strip().strip("'")
                            ibUrl = "http://futurestudents.yorku.ca/ajax/admit-req?applicant-type=highschool&cohort=ibcc&uuid%5B%5D=" + uuidUpdate
                            chineseHighSchoolUrl = "http://futurestudents.yorku.ca/ajax/admit-req?applicant-type=highschool&cohort=chs&uuid%5B%5D=" + uuidUpdate
                            alevelUrl = "http://futurestudents.yorku.ca/ajax/admit-req?applicant-type=highschool&cohort=gce&uuid%5B%5D=" + uuidUpdate
                        # print("ibUrl: ", ibUrl)
                        # print("uuidUpdate: ", uuidUpdate)
                        # print("chineseHighSchoolUrl: ", chineseHighSchoolUrl)
                        print("alevelUrl: ", alevelUrl)
                        '''ib'''
                        # print(self.parse_IB(ibUrl))
                        ib_html = etree.HTML(self.parse_IB(ibUrl).replace("\/", "/").strip())
                        ib = ib_html.xpath("//div[@class='fs-admit-req-general-req']/following-sibling::div")
                        if len(ib) == 1:
                            item['ib'] = clear_lianxu_space(ib[0].xpath("//text()")[ib[0].xpath("//text()").index("Requirements for admission:"):])

                        '''中国学生要求'''
                        # 从接口获取了require_chinese_en中国学生要求数据，需要二次解析
                        require_chinese_link = self.parse_IB(chineseHighSchoolUrl)
                        # print(require_chinese_link.replace("\/", "/").strip())
                        require_chinese_html = etree.HTML(require_chinese_link.replace("\/", "/").strip())
                        # //div[@class='fs-admit-req-general-req']/following-sibling::div
                        # //div//h3[contains(text(), '"+item['degree_name']+"')]/../div
                        require_chinese = require_chinese_html.xpath(
                            "//div[@class='fs-admit-req-general-req']/following-sibling::div")
                        if len(require_chinese) == 1:
                            item['require_chinese_en'] = etree.tostring(require_chinese[0], encoding='unicode')

                        '''alevel'''
                        # print(self.parse_IB(alevelUrl))
                        alevel_html = etree.HTML(self.parse_IB(alevelUrl).replace("\/", "/").strip())
                        alevel = alevel_html.xpath("//div[@class='fs-admit-req-general-req']/following-sibling::div")
                        if len(alevel) == 1:
                            item['alevel'] = remove_tags(etree.tostring(alevel[0], encoding='unicode'))

                    if item['require_chinese_en'] is None:
                        item['require_chinese_en'] = ""
                    item['require_chinese_en'] = chinese_requirement_pre + '\n' + remove_class(clear_lianxu_space([item['require_chinese_en']]))
                    # print("item['require_chinese_en']1: ", item['require_chinese_en'], "===\n===",item['major_name_en'])
                    # print("item['ib']1: ", item['ib'])
                    print("item['alevel']1: ", item['alevel'])
                    yield item
        except Exception as e:
            with open("scrapySchool_Canada_Ben/error/" + item['school_name'] + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_IB(self, ibUrl):
        headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        data = requests.get(ibUrl, headers=headers)
        resposne = etree.HTML(data.text)
        ib = resposne.xpath("/html//body//text()")
        ib = '\n'.join(ib).strip().strip('"')
        ib = ib.encode('utf-8').decode('unicode-escape')
        # print(ib.encode('utf-8').decode('unicode-escape'))
        # ib = remove_tags(ib)
        # print("ib1 = ", ib)
        return ib

    def parse_modules(self, modules_a_url):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(modules_a_url, headers=headers_base)
        response = etree.HTML(data.text)

        duration = response.xpath(
            "//strong[contains(text(),'Duration')]/following-sibling::*[1]//text()")
        if "yr" in ''.join(duration):
            duration_per = 1
        print("duration: ", duration)
        duration = ''.join(duration).replace('yrs', '').strip()
        duration_per = None

        # print("duration: ", duration)

        modules_en = response.xpath(
            "//div[@id='menu3']")
        modules_en_str = ""
        if len(modules_en) > 0:
            for m in modules_en:
                modules_en_str += etree.tostring(m, encoding='unicode', method='html')
        modules_en = remove_class(clear_lianxu_space([modules_en_str]))
        # print('modules_en: ', modules_en)
        modules_en_duration_dict = {}
        modules_en_duration_dict['duration'] = duration
        modules_en_duration_dict['duration_per'] = duration_per
        modules_en_duration_dict['modules_en'] = modules_en
        return modules_en_duration_dict
