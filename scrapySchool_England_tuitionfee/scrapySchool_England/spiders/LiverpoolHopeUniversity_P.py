# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getDuration import getIntDuration, getTeachTime


class LiverpoolHopeUniversity_PSpider(scrapy.Spider):
    name = "LiverpoolHopeUniversity_P"
    start_urls = ['http://www.hope.ac.uk/postgraduate/postgraduatecourses/']

    def parse(self, response):
        links = response.xpath("//div[@class='grid_12']/a/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))
        for link in links:
            url = "http:" + link
            # print("url = ", url)
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.lincoln.ac.uk/"
        item['university'] = "Liverpool Hope University"
        item['url'] = response.url
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        item['location'] = 'Hope Park, Liverpool, L16 9JD'
        print("===========================")
        print(response.url)
        try:
            # 专业
            programmelist = response.xpath("//section[@id='pageContent']/div[@class='course_header']/h1//text()").extract()
            # print(programmelist)
            programmeStr = ''.join(programmelist)
            degree_type = ''.join(re.findall(r"\(.{1,10}\)|\(Postgraduate\sCertificate\)", programmeStr.strip()))
            # print(degree_type)
            programme = programmeStr.replace(degree_type, "")
            item['programme_en'] = programme.title()
            item['degree_name'] = degree_type.replace("(", "").replace(")", "").strip()
            print("item['programme_en']: ", item['programme_en'])
            print("item['degree_name']: ", item['degree_name'])

            duration = response.xpath("//strong[contains(text(),'Duration')]//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration_str = ''.join(duration)

            item['teach_time'] = getTeachTime(duration_str)
            duration_list = getIntDuration(duration_str)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['teach_time'] = ", item['teach_time'])
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            # //strong[contains(text(),'Start month')]
            start_date = response.xpath("//strong[contains(text(),'Start month')]//text()").extract()
            clear_space(start_date)
            print("start_date: ", start_date)
            if '&' in ''.join(start_date):
                start_date_list = ''.join(start_date).split('&')
                print(start_date_list)
                for s in start_date_list:
                    item['start_date'] += getStartDate(s.strip()) + ","
            else:
                item['start_date'] = getStartDate(''.join(start_date))
            item['start_date'] = item['start_date'].strip().strip(",").strip()
            print("item['start_date'] = ", item['start_date'])

            overview = response.xpath("//div[@id='overview']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])

            modules = response.xpath("//div[@id='curriculum']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])

            entry_requirements = response.xpath("//div[@id='entry_reqs']//text()").extract()
            item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            assessment_en = response.xpath("//div[@id='teaching_research']").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            career_en = response.xpath("//div[@id='careers']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            # print("item['career_en']: ", item['career_en'])

            # //h2[contains(text(),'INTERNATIONAL TUITION FEES')]/following-sibling::p[1]
            tuition_fee = response.xpath("//h2[contains(text(),'INTERNATIONAL TUITION FEES')]/following-sibling::p//text()").extract()
            clear_space(tuition_fee)
            # print("tuition_fee: ", tuition_fee)
            tuition_fee_re = re.findall(r"£[\d,]+", ''.join(tuition_fee))
            # print("tuition_fee_re: ", tuition_fee_re)
            if len(tuition_fee_re) > 0:
                item['tuition_fee'] = int(tuition_fee_re[0].replace("£", "").replace(",", "").strip())
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee']: ", item['tuition_fee'])
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            dep_dict = {"liverpool hope business school":"Faculty of Arts and Humanities",
"creative and performing arts":"Faculty of Arts and Humanities",
"english":"Faculty of Arts and Humanities",
"fine and applied art":"Faculty of Arts and Humanities",
"history and politics":"Faculty of Arts and Humanities",
"law":"Faculty of Arts and Humanities",
"media and communication":"Faculty of Arts and Humanities",
"social sciences":"Faculty of Arts and Humanities",
"theology, philosophy and religion":"Faculty of Arts and Humanities",
"disability and education":"Faculty of Education",
"early childhood":"Faculty of Education",
"education studies":"Faculty of Education",
"teacher education":"Faculty of Education",
"geography and environmental science":"Faculty of Science",
"mathematics and computer science":"Faculty of Science",
"psychology":"Faculty of Science",
"health sciences":"Faculty of Science",}
            department = response.xpath("//div[contains(text(),'Department of')]//text()|//div[contains(text(),'School')]//text()").extract()
            clear_space(department)
            # print(department)
            department_key = ''.join(department).replace("Department of", "").replace("School of", "").lower().strip()
            # print("department_key: ", department_key)
            item['department'] = dep_dict.get(department_key)
            # print("item['department']: ", item['department'])

            ielts_desc = re.findall(r".{1,20}IELTS.{1,40}", item['rntry_requirements'])
            # print("ielts_desc: ", ielts_desc)
            item['ielts_desc'] = ''.join(ielts_desc)

            ielts_list = re.findall(r"\d[\d\.]{0,2}", item['ielts_desc'])
            # print(ielts_list)
            if len(ielts_list) == 1:
                item['ielts'] = ielts_list[0]
                item['ielts_l'] = ielts_list[0]
                item['ielts_s'] = ielts_list[0]
                item['ielts_r'] = ielts_list[0]
                item['ielts_w'] = ielts_list[0]
            elif len(ielts_list) == 2:
                item['ielts'] = ielts_list[0]
                item['ielts_l'] = ielts_list[1]
                item['ielts_s'] = ielts_list[1]
                item['ielts_r'] = ielts_list[1]
                item['ielts_w'] = ielts_list[1]
            elif len(ielts_list) == 3:
                item['ielts'] = ielts_list[0]
                item['ielts_l'] = ielts_list[0]
                item['ielts_s'] = ielts_list[0]
                item['ielts_r'] = ielts_list[1]
                item['ielts_w'] = ielts_list[2]
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            toefl_desc = re.findall(r"TOEFL.{1,40}", item['rntry_requirements'])
            # print("toefl_desc: ", toefl_desc)
            item['toefl_desc'] = ''.join(toefl_desc)

            toefl_list = re.findall(r"\d\d+", item['toefl_desc'])
            # print(toefl_list)
            if len(toefl_list) == 1:
                item['toefl'] = toefl_list[0]
            elif len(toefl_list) == 2:
                item['toefl'] = toefl_list[0]
                item['toefl_l'] = toefl_list[1]
                item['toefl_s'] = toefl_list[1]
                item['toefl_r'] = toefl_list[1]
                item['toefl_w'] = toefl_list[1]
            # print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
            #         item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

            item['apply_proces_en'] = "http://www.hope.ac.uk/postgraduate/howtoapply/"
            item['require_chinese_en'] = """<h3>2018 Postgraduate Entry Requirements</h3><ul><li>A degree from a recognised institution equivalent to a UK Honours degree</li></ul>"""
            yield item
        except Exception as e:
            with open(item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

