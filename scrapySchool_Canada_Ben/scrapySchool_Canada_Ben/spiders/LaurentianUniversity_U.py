__author__ = 'yangyaxia'
__date__ = '2018/10/23 14:54'
import scrapy
import re
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from lxml import etree
import requests

class LaurentianUniversity_USpider(scrapy.Spider):
    name = "LaurentianUniversity_U"
    start_urls = ["https://laurentian.ca/undergraduate-programs"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        # 所有的本科课程链接
        all_links = response.xpath("//h1[contains(text(),'Faculty')]/../div//a/@href").extract()
        # 不需要的法语课程链接
        french_links = response.xpath("//h1[contains(text(),'Faculty')]/../div/div[contains(@class, 'isalt fr')]//a/@href|"
                                      "//h1[contains(text(),'Faculty')]/../div/div[contains(@class, 'isalt en fr')]//a/@href").extract()

        # print(all_links)
        # print(french_links)
        # print(len(all_links))
        # print(len(french_links))

        '''筛选掉不需要的课程链接'''
        all_links_tmp = all_links
        for all in all_links_tmp:
            for french in french_links:
                if all == french:
                    all_links[all_links.index(all)] = ''
        # print(all_links)
        # print(len(all_links))
        all_links = list(set(all_links))
        # print(len(all_links))

        '''获取专业名匹配的学院'''
        department = response.xpath("//h1[contains(text(),'Faculty')]//text()").extract()
        # print(department)

        # 定义一个字典
        department_dict = {}
        # 获取每一个学院下面的专业名
        for dep in department:
            # 专业匹配学院
            major_list = response.xpath("//h1[contains(text(),'"+dep+"')]/../div//a//text()").extract()
            for major in major_list:
                department_dict[major.strip()] = dep
        # print(department_dict)

        for url in all_links:
            if len(url) > 0:
                yield scrapy.Request(url, callback=self.parse_data, meta=department_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)
        item['school_name'] = "Laurentian University"
        item['campus'] = 'Sudbury campus'
        item['url'] = response.url
        print("===========================")
        print(response.url)

        try:
            major_name_en = response.xpath("//div[@class='header-image-text']/h1//text()").extract()
            clear_space(major_name_en)
            item['major_name_en'] = ''.join(major_name_en).strip()
            print("item['major_name_en']: ", item['major_name_en'])

            if 'online' not in item['major_name_en']:
                item['department'] = response.meta.get(item['major_name_en'])
                # print("item['department']: ", item['department'])

                overview = response.xpath("//section[@id='prog_overview']").extract()
                item['overview_en'] = remove_class(clear_lianxu_space(overview))
                # if item['overview_en'] == "":
                #     print("***overview_en 为空")
                # print("item['overview_en']: ", item['overview_en'])

                career = response.xpath("//h1[contains(text(),'Career Opportunities')]/following-sibling::*").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career))
                # if item['career_en'] == "":
                #     print("***career_en 为空")
                # print("item['career_en']: ", item['career_en'])


                # https://laurentian.ca/international/undergraduate-admissions
                item['deadline'] = '2019-02-01'

                # https://laurentian.ca/fees-financing/undergraduate-tuition
                item['tuition_fee_pre'] = '$'
                if 'engineer' in item['major_name_en'].lower():
                    item['tuition_fee'] = 30627
                elif 'architectur' in item['major_name_en'].lower():
                    item['tuition_fee'] = 31027
                else:
                    item['tuition_fee'] = 24104
                # print("item['tuition_fee']: ", item['tuition_fee'])

                # https://laurentian.ca/international/undergraduate-admissions
                item['require_chinese_en'] = '<p>Senior School Leaving Certificate;  Senior Upper Middle School.  Huikao (Senior School Graduation Exam) is not required.</p>'

                if item['department'] == "Faculty of Arts":
                    item['specific_requirement_en'] = 'Senior level English'
                elif item['department'] == "Faculty of Science, Engineering and Architecture":
                    if 'architectur' in item['major_name_en'].lower():
                        item['specific_requirement_en'] = 'Senior level English and two senior level math'
                    elif 'Computer Science' in item['major_name_en']:
                        item['specific_requirement_en'] = 'Senior level English and two math'
                    elif 'engineering' in item['major_name_en'].lower():
                        item['specific_requirement_en'] = 'Senior level English, math, physics and chemistry'
                    elif 'Forensic Science' in item['major_name_en']:
                        item['specific_requirement_en'] = 'Senior level English, math, biology and chemistry'
                    elif 'Radiation Therapy' in item['major_name_en']:
                        item['specific_requirement_en'] = '''<ul><li>Senior level English, math, physics, chemistry and biology</li><li>Select group of candidates will be invited to interview</li></ul>'''
                    elif 'Sciences' in item['major_name_en']:
                        item['specific_requirement_en'] = '<ul><li>Senior level English</li><li>one senior level math & two senior level sciences OR two senior level math & on senior level science</li></ul>'
                elif item['department'] == "Faculty of Management":
                    if 'Business Administration' in item['major_name_en']:
                        item['specific_requirement_en'] = 'Senior level English and one senior level math'
                    elif 'Sports Administration' in item['major_name_en']:
                        item['specific_requirement_en'] = 'Senior level English and two senior level math'
                elif item['department'] == "Faculty of Health":
                    if 'Nursing' in item['major_name_en']:
                        item['specific_requirement_en'] = 'Senior level English, math, chemistry and biology'
                    elif 'Midwifery' in item['major_name_en']:
                        item['specific_requirement_en'] = 'Senior level English, Biology OR Chemistry and one social science'
                    elif 'Gerontology' in item['major_name_en']:
                        item['specific_requirement_en'] = 'Senior level English'
                    elif 'Social Work' in item['major_name_en'] or 'Indigenous Social Work' in item['major_name_en']:
                        item['specific_requirement_en'] = 'Senior level English'
                    elif 'Sport and Physical Education' in item['major_name_en']:
                        item['specific_requirement_en'] = 'Senior level English and biology'
                    elif 'Kinesiology' in item['major_name_en']:
                        item['specific_requirement_en'] = 'Senior level English, math and chemistry'
                    elif 'Outdoor Adventure Leadership' in item['major_name_en']:
                        item['specific_requirement_en'] = 'Senior level English and biology'
                    elif 'Health Promotion' in item['major_name_en']:
                        item['specific_requirement_en'] = 'Senior level English, chemistry and biology'
                    elif 'Sport Psychology' in item['major_name_en']:
                        item['specific_requirement_en'] = 'Senior level English'

                item['ielts_desc'] = 'International English Language Testing System (IELTS - Academic)(6.5 minimum overall for direct academic entry with no band score lower than 6)'
                item['ielts'] = '6.5'
                item['ielts_l'] = '6.0'
                item['ielts_s'] = '6.0'
                item['ielts_r'] = '6.0'
                item['ielts_w'] = '6.0'
                item['toefl_desc'] = 'Test of English as a Foreign Language (TOEFL) (minimum score: 230 computer-based, 88 Internet-based)'
                item['toefl'] = '88'

                item['start_date'] = '9月'
                item['alevel'] = '5 GCE/GCSE/IGCSE subjects with at least 2 at A-Level.  4 AS-Level subjects with 1 GCSE/IGCSE/O-Level subject will be considered provided the AS-levels do not duplicate subject matter at the GCSE/IGCSE or O Level. (Minimum grade of C or better required)'
                item['sat1_desc'] = '1650'
                item['act_desc'] = '24'
                item['toefl_code'] = item['sat_code'] = item['act_code'] = None
                item['apply_pre'] = 'CAD$'
                item['apply_fee'] = '150'
                # //a[@class='btn btn-default full'][contains(text(),'Program Details')]/@href

                item['other'] = '''问题清单：1.duration页面展示不一致，有些出现在一段话中导致抓取缺少,需要详细核对
                2.学位名称下面有些存在划分的专业，需要找出特殊的那几条然后拆分，不一定全部能拆完全以及准确
                3.因为正则匹配问题，学位名可能不全或者不准确
                4.专业描述和课程设置、就业为空的是详情页没有的
                '''
                detail_url = response.xpath("//a[@class='btn btn-default full'][contains(text(),'Program Details')]/@href").extract()
                if len(detail_url) > 0:
                    print(''.join(detail_url))
                    detail_dict = self.parse_detail_ziduan(''.join(detail_url), item['major_name_en'])
                    item['entry_requirements_en'] = detail_dict['entrey_requirements_en']
                    item['ap'] = detail_dict['ap']
                    item['ib'] = detail_dict['ib']
                    item['modules_en'] = detail_dict['modules_en']

                    degree_name_list = detail_dict['degree_name_list']
                    major_name_en_list = detail_dict['major_name_en_list']
                    duration_text = detail_dict['duration_text']
                    item['other'] = item['other'] + '\n'.join(major_name_en_list)
                    print("degree_name_list: ", degree_name_list)
                    print("major_name_en_list: ", major_name_en_list)
                    print("duration_text: ", duration_text)
                    if len(degree_name_list) == 0:
                        yield item
                    else:
                        # enducation 专业特殊需要处理
                        if item['major_name_en'] == 'Education':
                            degree_name_list = ''.join(degree_name_list).split(';')
                        # print("degree_name_list: ", degree_name_list)
                        # if len(major_name_en_list) > 1:
                        #     if "<h4>Fourth year</h4>" in item['modules_en']:
                        #         item['duration'] = '4'
                        #         item['duration_per'] = 1
                        #     if item['duration'] is None and "<h4>Third year</h4>" in item['modules_en']:
                        #         item['duration'] = '3'
                        #         item['duration_per'] = 1
                        #     if item['duration'] is None and "<h4>Second year</h4>" in item['modules_en']:
                        #         item['duration'] = '2'
                        #         item['duration_per'] = 1
                        #     if item['duration'] is None and "<h4>First year</h4>" in item['modules_en']:
                        #         item['duration'] = '1'
                        #         item['duration_per'] = 1
                        #     item['degree_name'] = degree_name_list[-1].replace('(4 Year)', '').replace('in ' + ''.join(item['major_name_en']), '').strip()
                        #     degree_name_list = degree_name_list[:-1]
                        #     for major_name in major_name_en_list:
                        #         item['major_name_en'] = major_name.replace('Specialization in', '').replace('Option in', '').replace('(27 credits)', '').replace('(24 credits)', '').strip()
                        #         print("item['major_name_en']==:", item['major_name_en'])
                        #         yield item
                        # print("degree_name_list2==: ", degree_name_list)
                        # if len(degree_name_list) > 0:
                        for degree_name in degree_name_list:
                            print("**************", item['major_name_en'])
                            # print(degree_name)
                            duration_re = re.findall(r"\(\d\syear.*?\)|\(\d-year.*?\)", degree_name, re.I)
                            print('duration_re: ', duration_re)
                            if len(duration_re) > 0:
                                duration_re1 = re.findall(r"\d", ''.join(duration_re))
                                item['duration'] = ''.join(duration_re1[0]).strip()
                                item['duration_per'] = 1
                            if item['duration'] is None and "<h4>Fourth year</h4>" in item['modules_en']:
                                item['duration'] = '4'
                                item['duration_per'] = 1
                            if item['duration'] is None and "<h4>Third year</h4>" in item['modules_en']:
                                item['duration'] = '3'
                                item['duration_per'] = 1
                            if item['duration'] is None and "<h4>Second year</h4>" in item['modules_en']:
                                item['duration'] = '2'
                                item['duration_per'] = 1
                            if item['duration'] is None and "<h4>First year</h4>" in item['modules_en']:
                                item['duration'] = '1'
                                item['duration_per'] = 1
                            print("item['duration']: ", item['duration'])
                            print("item['duration_per']: ", item['duration_per'])

                            # 匹配无用的括号里面的东西
                            unuse_re = re.findall(r"\([^B][\w\W]*\)", degree_name)
                            item['degree_name'] = degree_name.replace('  ', ' ').replace(''.join(duration_re), '').replace('Concentration -', '').replace('- 120 credits', '').replace(''.join(unuse_re), '').replace(' in ' + item['major_name_en'], '').replace('in Women’s and Gender Studies','').strip()
                            # 学位缩写
                            if item['major_name_en'] == 'Forensic Science':
                                item['degree_name'] = 'Bachelor of Forensic Science'
                            elif '(B' in degree_name:
                                degree_name_re = re.findall(r"\(B[\w\W]*?\)", degree_name)
                                if 'Honours' in degree_name:
                                    item['degree_name'] = 'Honours' + ''.join(degree_name_re).replace('(', '').replace(')', '').strip()
                                else:
                                    item['degree_name'] = ''.join(degree_name_re).replace('(', '').replace(')', '').strip()
                                item['major_name_en'] = degree_name.replace('Honours', '').replace(
                                        ''.join(degree_name_re), '').replace('Specialization in', '').replace(''.join(unuse_re), '').strip()
                            # BBA 的特殊情况
                            if 'BBA IN' in item['degree_name']:
                                item['major_name_en'] = item['degree_name'].replace('BBA IN', '').strip().title()
                                item['degree_name'] = "BACHELOR OF BUSINESS ADMINISTRATION".title()
                            # print("item['degree_name']: ", item['degree_name'])
                            item['degree_name'] = item['degree_name'].replace(',', ' or ')
                            item['degree_name'] = item['degree_name'].replace('  ', ' ').replace(''.join(duration_re), '').replace('Concentration -', '').replace(
                                '- 120 credits', '').replace(''.join(unuse_re), '').replace(' in ' + item['major_name_en'], '').replace('in Women’s and Gender Studies', '').replace(
                                'Major -', '').replace('Specialization  -', '').strip()
                            print("item['degree_name']: ", item['degree_name'])
                            # 如果含有分专业

                            # 含有 or的学位需要拆分成两条
                            if ' or ' in item['degree_name']:
                                degree_name_list_again = item['degree_name'].split(' or ')
                                print('degree_name_list_again：', degree_name_list_again)
                                for deg in degree_name_list_again:
                                    if deg == 'Science':
                                        item['degree_name'] = 'Bachelor of ' + deg.strip().strip('or').strip()
                                    else:
                                        item['degree_name'] = deg.strip().strip('or').strip()
                                    if len(major_name_en_list) > 1 and '(B' not in ''.join(major_name_en_list) and item['duration'] == '4':
                                        # item['degree_name'] = degree_name_list[-1]
                                        # degree_name_list = degree_name_list[:-1]
                                        for major_name in major_name_en_list:
                                            item['major_name_en'] = major_name.replace('Specialization in', '').replace(
                                                'Option in', '').replace('(27 credits)', '').replace('(24 credits)', '').strip()
                                            print("item['major_name_en']==:", item['major_name_en'])
                                            yield item
                                    else:
                                        yield item
                            elif 'B.Eng.' in item['degree_name']:
                                item['degree_name'] = 'B.Eng.'
                                yield item
                            else:
                                if len(major_name_en_list) > 1 and '(B' not in ''.join(major_name_en_list) and item['duration'] == '4':
                                    # item['degree_name'] = degree_name_list[-1]
                                    # degree_name_list = degree_name_list[:-1]
                                    for major_name in major_name_en_list:
                                        item['major_name_en'] = major_name.replace('Specialization in', '').replace(
                                            'Option in', '').replace('(27 credits)', '').replace('(24 credits)', '').strip()
                                        print("item['major_name_en']==:", item['major_name_en'])
                                        yield item
                                else:
                                    yield item
                else:
                    yield item

        except Exception as e:
            with open("scrapySchool_Canada_Ben/error/" + item['school_name'] + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    # degree_name, modules_en,duration,major_name_en, entry_requirements
    def parse_detail_ziduan(self, detail_url, major_name):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(detail_url, headers=headers_base)
        response = etree.HTML(data.text)
        entrey_requirements_en = response.xpath("//strong[contains(text(),'Applicants from outside an Ontario High School')]/../preceding-sibling::*")
        if len(entrey_requirements_en) == 0:
            entrey_requirements_en = response.xpath(
                "//div[@id='admission']//div[@class='panel-body']")
        entrey_requirements_en_str = ""
        if len(entrey_requirements_en) > 0:
            for m in entrey_requirements_en:
                entrey_requirements_en_str += etree.tostring(m, encoding='unicode', method='html')
        entrey_requirements_en = remove_class(clear_lianxu_space([entrey_requirements_en_str]))
        # print(entrey_requirements_en)

        ap = response.xpath("//strong[contains(text(),'Advanced Placement')]/../following-sibling::p[1]//text()")
        ap_str = ''.join(ap).strip()
        # print('ap_str=', ap_str)

        ib = response.xpath("//strong[contains(text(),'International Baccalaureate')]/../following-sibling::p[1]//text()")
        ib_str = ''.join(ib).strip()
        # print('ib_str=', ib_str)



        '''First year   //span[contains(@data-year,'1')]
        Second Year //span[contains(@data-year,'2')]
        Third Year  //span[contains(@data-year,'3')]
        Fourth Year //span[contains(@data-year,'4')]
        '''

        first_year = response.xpath("//span[contains(@data-year,'1')]")
        first_year_str = ""
        if len(first_year) > 0:
            for m in first_year:
                first_year_str += etree.tostring(m, encoding='unicode', method='html')
            first_year_str = '<h4>First year</h4>' + first_year_str
        first_year_en = remove_class(clear_lianxu_space([first_year_str]))

        second_year = response.xpath("//span[contains(@data-year,'2')]")
        second_year_str = ""
        if len(second_year) > 0:
            for m in second_year:
                second_year_str += etree.tostring(m, encoding='unicode', method='html')
            second_year_str = '<h4>Second year</h4>' + second_year_str
        second_year_en = remove_class(clear_lianxu_space([second_year_str]))

        third_year = response.xpath("//span[contains(@data-year,'3')]")
        third_year_str = ""
        if len(third_year) > 0:
            for m in third_year:
                third_year_str += etree.tostring(m, encoding='unicode', method='html')
            third_year_str = '<h4>Third year</h4>' + third_year_str
        third_year_en = remove_class(clear_lianxu_space([third_year_str]))

        fourth_year = response.xpath("//span[contains(@data-year,'4')]")
        fourth_year_str = ""
        if len(fourth_year) > 0:
            for m in fourth_year:
                fourth_year_str += etree.tostring(m, encoding='unicode', method='html')
            fourth_year_str = '<h4>Fourth year</h4>' + fourth_year_str
        fourth_year_en = remove_class(clear_lianxu_space([fourth_year_str]))
        modules_en = first_year_en + '\n' + second_year_en + '\n' + third_year_en + '\n' + fourth_year_en
        modules_en = modules_en.strip()
        # print(modules_en)


        # 特殊专业
        # https://laurentian.ca/program/biology/details
        # https://laurentian.ca/program/engineering/details
        # https://laurentian.ca/program/education/details
        # https://laurentian.ca/program/native-human-services/details
        # https://laurentian.ca/program/computer-science/details
        degree_name = response.xpath("//div[@id='options']//strong[contains(text(),'BACHELOR OF')]//text()|"
                                     "//div[@id='options']//strong[contains(text(),'Bachelor of')]//text()|"
                                     "//div[@id='options']//strong[contains(text(),'(B')]//text()|"
                                     "//div[@id='options']//strong[contains(text(),'B.Eng.')]//text()|"
                                     "//div[@id='options']//strong[contains(text(),'B.Ed.')]//text()")
        major_name_len = major_name.split(' ')
        count = len(major_name_len)
        # print('===', count)
        if len(degree_name) == 0:
            s = ""
            if count == 1:
                s = '[a-zA-Z]+'
            elif count == 2:
                s = '[a-zA-Z]+\s[a-zA-Z]+'
            elif count == 3:
                s = '[a-zA-Z]+\s[a-zA-Z]+\s[a-zA-Z]+'
            degree_name = re.findall(r"Honours\sBachelor\sof\s"+s, data.text)
            if len(degree_name) == 0:
                degree_name = re.findall(r"Bachelor\sof\s"+s, data.text)
        # print("degree_name: ",degree_name)
        # https://laurentian.ca/program/physics/details Bachelor of Science (4-Year) in Physics
        # Bachelor of Arts (3 Year) in Women’s and Gender Studies


        major_name_en_list = response.xpath("//strong[contains(text(),'Option in')]//text()|"
                                     "//strong[contains(text(),'Bachelor of')]/../following-sibling::*//strong[contains(text(),'Specialization in')]//text()")
        # print(major_name_en_list)

        duration_text = re.findall(r"\w+-year[\w\W]*?Bachelor\sof", data.text)

        detail_dict = {}
        detail_dict['entrey_requirements_en'] = entrey_requirements_en
        detail_dict['ap'] = ap_str
        detail_dict['ib'] = ib_str
        detail_dict['modules_en'] = modules_en
        detail_dict['degree_name_list'] = list(set(degree_name))
        detail_dict['major_name_en_list'] = list(set(major_name_en_list))
        detail_dict['duration_text'] = duration_text
        return detail_dict