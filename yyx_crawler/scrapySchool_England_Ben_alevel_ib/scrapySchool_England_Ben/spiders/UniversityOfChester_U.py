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
import json
import requests

class UniversityOfChester_USpider(scrapy.Spider):
    name = "UniversityOfChester_U"
    start_urls = ["https://www1.chester.ac.uk/course_atoz/51"]

    def parse(self, response):
        links = response.xpath("//html//table/tbody/tr/td[3]/ul[1]/li/a[contains(text(), 'Full')]/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))
        for link in links:
            url = "https://www1.chester.ac.uk" + link
            # print(url)
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Chester"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        try:
            programme = response.xpath("//h1[@id='main-content']/text()").extract()
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en']: ", item['programme_en'])

            degree_type = response.xpath("//h1[@id='main-content']/div//text()").extract()
            item['degree_name'] = ''.join(degree_type).replace("(Hons)", "").strip()
            print("item['degree_name']: ", item['degree_name'])

            start_date = response.xpath("//select[@id='edit-date']/option//text()|//label[@for='edit-date']/following-sibling::span//text()").extract()
            clear_space(start_date)
            # print("start_date: ", start_date)
            start_date_str = ""
            if len(start_date) > 0:
                for s in start_date:
                    # start_date_str = getStartDate(s)
                    if getStartDate(s) != None:
                        start_date_str += getStartDate(s) + ", "
            item['start_date'] = start_date_str.strip().strip(',').strip()
            # print("item['start_date']: ", item['start_date'])

            mode = response.xpath("//select[@id='edit-mode']//text()").extract()
            clear_space(mode)
            # item['teach_time'] = getTeachTime(''.join(mode))
            # print("mode: ", mode)

            location = response.xpath("//label[@for='edit-compulsory']/following-sibling::*//text()").extract()
            item['location'] = ''.join(location).strip()
            # print("item['location']: ", item['location'])

            ucascode = response.xpath(
                "//dt[contains(text(),'UCAS Code')]/following-sibling::*//text()").extract()
            clear_space(ucascode)
            item['ucascode'] = ''.join(ucascode).strip()
            print("item['ucascode'] = ", item['ucascode'])

            duration = response.xpath("//dt[contains(text(),'Duration')]/following-sibling::*//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            overview_en = response.xpath(
                "//h3[contains(text(),'Course overview')]/../*[position()<last()]|"
                "//div[@class='m-body__margin-bottom t-course__overview']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
            # print("item['overview_en']: ", item['overview_en'])

            entry_requirements = response.xpath("//div[@id='entry-international']//form[@id='courses-international-form']/preceding-sibling::*//text()").extract()
            # item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            alevel = response.xpath(
                "//td[contains(text(),'GCE A Level')]/following-sibling::*//text()").extract()
            item['alevel'] = clear_lianxu_space(alevel)
            # print("item['alevel']: ", item['alevel'])

            ib = response.xpath(
                "//td[contains(text(),'International Baccalaureate')]/following-sibling::*//text()").extract()
            item['ib'] = clear_lianxu_space(ib)
            # print("item['ib']: ", item['ib'])

            ielts_desc = response.xpath("//div[@id='entry-international']//li[contains(text(),'Undergraduate:')]//text()").extract()
            clear_space(ielts_desc)
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

            assessment_en = response.xpath("//h3[@class='field-label'][contains(text(),'How will I be taught?')]/..|"
                                           "//h3[@class='field-label'][contains(text(),'How will I be assessed?')]/..").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            tuition_fee = response.xpath("//div[@class='field-fees-international']/p//text()|"
                                         "//p[contains(text(),'The tuition fees for international students studyi')]//text()").extract()
            print("tuition_fee: ", tuition_fee)
            if len(tuition_fee) > 0:
                item['tuition_fee'] = getTuition_fee(''.join(tuition_fee))
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee']: ", item['tuition_fee'])
            print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            career_en = response.xpath("//div[@id='careers-career-services']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en)).replace("<div></div>", "").strip()
            print("item['career_en']: ", item['career_en'])

            modules = re.findall(r"function\sinit_drupal_core_settings\(\)\s{jQuery\.extend\(Drupal\.settings,.*}", response.text)
            # print("modules: ", modules)
            modules_str = ''.join(modules).replace("function init_drupal_core_settings() {jQuery.extend(Drupal.settings,", "").strip()
            modules_dict = json.loads(modules_str)
            # print("modules_dict: ", modules_dict)
            # groupCode     modulesNid
            # print(modules_dict.get("courses"))
            if modules_dict.get('courses').get('groupCode') is not False:
                modules_json = "https://www1.chester.ac.uk/courses/modules/ajax/"+modules_dict.get('courses').get('modulesNid')+"/"+modules_dict.get('courses').get('groupCode')+"/389"
                # print("modules_json: ", modules_json)
                mdict = json.loads(requests.get(modules_json).text)
                # print("mdict: ", len(mdict))
                m = mdict[-1].get('data')
                if m != None:
                    item['modules_en'] = remove_class(clear_lianxu_space([m]))
            # print("item['modules_en']: ", item['modules_en'])

            item['apply_proces_en'] = "https://www1.chester.ac.uk/undergraduate/how-apply/applying-full-time-courses"
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<div class="field-collection-view clearfix view-mode-full">
  <h3 class="field-course-type">
    Undergraduate Study  </h3>

  <ul><li>UK foundation/pathway course with a pass mark of 50% and above.  Engineering courses require an additional mark of at least 55% in a Maths module. </li>
<li>China 3 year National Senior High School Certificate with 80% or above</li>
<li>Gaokao (College Entry Exam) with good grades </li>
<li>Dazhuan considered for entry to 3rd year UG</li>
<li>BFSU Foundation Year at 60% or above</li>
<li>Dongfang International Centre for Education Exchange Top University Foundation Course 60% or above</li>
<li>East and West International Education (EWIE)/ Wiseway Global International Foundation Certificate at 60% or above</li>
<li>Graduation Certificate from a specialised College/School (Zhongzuhan) with 80% or above</li>
</ul></div>"""]))
            # print("item['require_chinese_en']: ", item['require_chinese_en'])

            # department = response.xpath("//dt[contains(text(), 'Department')]/following-sibling::dd[1]//text()").extract()
            # item['department'] = ''.join(department).strip()
            # print("item['department']: ", item['department'])

            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a',
                      encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

