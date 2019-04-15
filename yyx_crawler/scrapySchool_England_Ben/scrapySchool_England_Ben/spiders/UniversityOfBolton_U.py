# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime


class UniversityOfBolton_USpider(scrapy.Spider):
    name = "UniversityOfBolton_U"
    start_urls = ["https://www.bolton.ac.uk/subject-areas/all-subjects/"]

    def parse(self, response):
        # 获取研究领域的链接
        links = response.xpath("//div[@class='vc_column-inner']/div[@class='wpb_wrapper']/div[@class='nectar-fancy-box using-img ']/a/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))
        for link in links:
            url = link
            yield scrapy.Request(url, callback=self.parse_url)

    def parse_url(self, response):
        # print("======subject area link======", response.url)
        subjectArea = response.xpath("//li[@class='current']/span//text()").extract()
        # print("subjectArea: ", subjectArea)
        # 获取搜索课程的链接
        links = response.xpath("//span[@class='link_wrap']//a[@class='link_text'][contains(text(), 'all')]/@href|//span[@class='link_wrap']//a[@class='link_text'][contains(text(), 'ALL')]/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))
        # print(links)
        for url in links:
            yield scrapy.Request(url, callback=self.parse_course_url, meta={'subjectArea': ''.join(subjectArea)})

    def parse_course_url(self, response):
        # print("======search course link======", response.url)
        # print("subjectArea: ", response.meta['subjectArea'])
        # 获取搜索课程的链接
        links = response.xpath("//html//article/div[1]/h2[1]/a/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))
        # print(links)
        # links = []
        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta={'subjectArea': response.meta['subjectArea']})

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Bolton"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        print("subjectArea===: ", response.meta['subjectArea'])
        try:
            programmeDegreetype = response.xpath(
                "//div[@class='wpb_text_column wpb_content_element  vc_custom_1506499626241']/div[@class='wpb_wrapper']/h2//text()").extract()
            # print("programmeDegreetype: ", programmeDegreetype)
            programmeDegreetypeStr = ''.join(programmeDegreetype).strip()

            degree_type = response.xpath("//li[@class='iconim award']//b[contains(text(),'Award:')]/..//text()").extract()
            # print("degree_type: ", degree_type)
            item['degree_name'] = ''.join(degree_type).replace("Award:", "").replace("(Hons)", "").strip()
            # if item['degree_name'] == "":
            #     item['degree_name'] = "**"
            print("item['degree_name']: ", item['degree_name'])

            # if item['degree_name'].lower() == "phd":
            #     item['teach_type'] = 'phd'
            #     item['degree_type'] = 3
            # print("item['teach_type']: ", item['teach_type'])
            # print("item['degree_type']: ", item['degree_type'])

            programme = programmeDegreetypeStr.replace(item['degree_name'], '').replace("(Hons)", "").replace("()", "").strip()
            item['programme_en'] = programme
            print("item['programme_en']: ", item['programme_en'])


            start_date = response.xpath(
                "//li[@class='iconim date']//b[contains(text(),'Start date:')]/..//text()").extract()
            clear_space(start_date)
            # print("start_date: ", start_date)
            start_date_str = ''.join(start_date).replace("Start date:", "").strip()
            # print("start_date_str: ", start_date_str)
            start_date_re = re.findall(r"\d+/\d+/\d+", start_date_str)
            # print("start_date_re: ", start_date_re)
            if len(start_date_re) > 0:
                for s in start_date_re:
                    start_date_sp = s.split('/')
                    item['start_date'] += start_date_sp[-1] + "-" + start_date_sp[1] + "-" + start_date_sp[0] + ", "
            if item['start_date'] != None:
                item['start_date'] = item['start_date'].strip().rstrip(',').strip()
            # print("item['start_date']: ", item['start_date'])

            location = response.xpath("//li[@class='iconim location']//b[contains(text(),'Location:')]/..//text()").extract()
            item['location'] = ''.join(location).replace("Location:", "").strip()
            # print("item['location']: ", item['location'])

            duration = response.xpath("//li[@class='iconim duration']//b[contains(text(),'Duration:')]/..//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            overview_en = response.xpath("//div[@id='course-details']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
            # print("item['overview_en']: ", item['overview_en'])

            # //div[@id='course-detail']
            entry_requirements = response.xpath("//div[@id='entry-requirements']//text()").extract()
            # item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            ielts_desc = response.xpath("//div[@id='entry-requirements']//*[contains(text(),'IELTS')]/text()").extract()
            clear_space(ielts_desc)
            # print("ielts_desc: ", ielts_desc)
            # ielts_desc_re = re.findall(r'.{1,50}IELTS.{1,50}', ''.join(ielts_desc))
            # print("ielts_desc_re: ", ielts_desc_re)
            # if len(ielts_desc) > 0:
            item['ielts_desc'] = ''.join(ielts_desc).strip()
            # print("item['ielts_desc']: ", item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            career_en = response.xpath("//div[@id='careers-employment']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en)).replace("<div></div>", "").strip()
            # print("item['career_en']: ", item['career_en'])

            how_to_apply = response.xpath("//div[@id='how-to-apply']").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(how_to_apply))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            modules = response.xpath(
                "//div[@class='tab_content modules_tab_content tab__teaching-assessment__modules']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])

            assessment_en = response.xpath("//div[@class='tab_content modules_tab_content tab__teaching-assessment__teaching-methods']"
                                           "|//div[@class='tab_content modules_tab_content tab__teaching-assessment__assessment-methods']").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            tuition_fee = response.xpath(
                "//h3[@class='table_header'][contains(text(),'International fees')]/following-sibling::div[1]/table//tr/th[contains(text(),'2018/')][1]/following-sibling::td[1]//text()").extract()
            print("tuition_fee: ", tuition_fee)
            if len(tuition_fee) > 0:
                item['tuition_fee'] = getTuition_fee(''.join(tuition_fee))
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee']: ", item['tuition_fee'])
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            department_dict = {"Art & Design and Fine Art": "Bolton School of the Arts",
"Textiles & Fashion": "Bolton School of the Arts",
"Media & Photography": "Bolton School of the Arts",
"Theatre & Performance": "Bolton School of the Arts",
"English & Creative Writing": "Bolton School of the Arts",
"Graphic Design": "Bolton School of the Arts",
"Animation & Illustration": "Bolton School of the Arts",
"Accountancy": "Institute of Management Greater Manchester",
"Business, Retail, Logistics & Supply Chain Management": "Institute of Management Greater Manchester",
"Nursing": "Faculty of Health & Wellbeing",
"Health & Social Care": "Faculty of Health & Wellbeing",
"Dental Sciences": "Faculty of Health & Wellbeing",
"Early Years & Childhood Studies": "Faculty of Health & Wellbeing",
"Community Work & Youth": "Faculty of Health & Wellbeing",
"School of Sport & Biological Sciences": "Faculty of Health & Wellbeing",
"Automotive Design": "National Centre for Motorsport Engineering",
"Chassis Dynamics & Aerodynamics": "National Centre for Motorsport Engineering",
"General Engineering": "National Centre for Motorsport Engineering",
"Motorsport & Trackside Technology": "National Centre for Motorsport Engineering",
"Engines & Performance Modelling": "National Centre for Motorsport Engineering",
"Our Partners": "National Centre for Motorsport Engineering",
"Computing": "School of Creative Technologies",
"Games": "School of Creative Technologies",
"Special & Visual Effects": "School of Creative Technologies",
"Education & Teacher Training": "School of Education & Psychology",
"Psychology": "School of Education & Psychology",
"Access courses": "School of Education & Psychology",
"International Foundation programmes & English Pre-Sessional courses": "School of Education & Psychology",
"Construction": "School of Engineering",
"Civil Engineering": "School of Engineering",
"Mechanical Engineering": "School of Engineering",
"Motorsport & Automotive Performance Engineering": "School of Engineering",
"Biomedical & Medical Engineering": "School of Engineering",
"Electrical & Electronic Engineering": "School of Engineering",
"Mathematics": "School of Engineering",
"Law": "School of Law",
"Centre for Contemporary Coronial Law": "School of Law",
"Medical Biology": "School of Sport & Biological Sciences",
"Sports & Sport Rehabilitation": "School of Sport & Biological Sciences",}
            item['department'] = department_dict.get(response.meta['subjectArea'])
            print("item['department']: ", item['department'])

            alevel = response.xpath(
                "//li[@class='iconim points']//b[contains(text(),'UCAS points:')]/../span//text()").extract()
            item['alevel'] = clear_lianxu_space(alevel)
            print("item['alevel']: ", item['alevel'])

            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<p><strong>Undergraduate entry to year 1 </strong></p>
<p>The above qualifications and completion of a suitable foundation programme.</p>
<p>Alternatively, successful completion of one year at a recognised Chinese university in a relevant subject.</p>
<p><strong>Undergraduate entry to year 2 / 3</strong></p>
<p>2 Year Diploma in a suitable subject area.</p>
<p>University College Graduation Diploma or Graduation Diploma from recognised institutions.</p>
<p>EDEXCEL or SQA HND</p>
<p>Da Zhuan (3 Year Diploma)</p>
<p>(Year 2 &amp; 3 entry is subject to successful programme mapping)</p>"""]))

            ucascode = response.xpath("//li[@class='iconim code']//b[contains(text(),'UCAS code:')]/..//text()").extract()
            clear_space(ucascode)
            print("ucascode: ", ucascode)
            item['ucascode'] = ''.join(ucascode).replace("UCAS code:", "").strip()
            print("item['ucascode'] = ", item['ucascode'])

            mode = response.xpath("//b[contains(text(),'Course type:')]/..//text()").extract()
            clear_space(mode)
            teach_time = ''.join(mode)
            print("teach_time: ", teach_time)

            isup = response.xpath("//a[contains(text(),'Click here for more information on')]//text()").extract()
            # print("isup: ", isup)
            isup_str = ''.join(isup)
            if len(isup) == 0:
                isup = response.xpath("//li[@class='iconim code']//b[contains(text(),'UCAS code:')]/..//text()"
                                      "|//li[@class='iconim points']//b[contains(text(),'UCAS points:')]/..//text()").extract()
            print("isup_str: ", isup_str)
            print("isup: ", isup)
            if "full" in teach_time.lower():
                if "https://courses.bolton.ac.uk/course" in item['url']:
                    if "undergraduate" in isup_str or len(item['ucascode']) != 0:
                        print("******存到数据库*****")
                        yield item

        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

