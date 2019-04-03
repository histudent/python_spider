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


class LiverpoolHopeUniversity_USpider(scrapy.Spider):
    name = "LiverpoolHopeUniversity_U"
    start_urls = ['http://www.hope.ac.uk/undergraduate/undergraduatecourses/']

    def parse(self, response):
        links = response.xpath("//div[@class='grid_12']/ul//a/@href").extract()

        # 组合字典
        programme_dict = {}
        programme_list = response.xpath(
            "//div[@class='grid_12']/ul//a//text()").extract()
        clear_space(programme_list)

        for link in range(len(links)):
            url = "http:" + links[link]
            programme_dict[url] = programme_list[link]

        # print(programme_dict)
        clear_space(links)
        print(len(links))
        links = list(set(links))
        print(len(links))
        for link in links:
            url = "http:" + link
            # print("url = ", url)
            yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "https://www.lincoln.ac.uk/"
        item['university'] = "Liverpool Hope University"
        item['url'] = response.url
        # item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 1
        item['location'] = 'Hope Park, Liverpool, L16 9JD'
        print("===========================")
        print(response.url)
        item['major_type1'] = response.meta.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            # 专业
            programmelist = response.xpath("//section[@id='pageContent']/div[@class='course_header']/h1//text()").extract()
            # print(programmelist)
            programmeStr = ''.join(programmelist).replace("(HONS)", "").strip()
            # print("programmeStr: ", programmeStr)
            degree_type = ''.join(re.findall(r"\w+$", programmeStr))
            # print(degree_type)
            programme = programmeStr.replace(degree_type, "")
            item['programme_en'] = programme.title()
            item['degree_name'] = degree_type.replace("(", "").replace(")", "").strip()
            if item['programme_en'] == "":
                item['programme_en'] = item['degree_name'].title()
            print("item['programme_en']: ", item['programme_en'])
            print("item['degree_name']: ", item['degree_name'])

            ucascode = response.xpath("//strong[contains(text(),'UCAS Code:')]//text()").extract()
            clear_space(ucascode)
            # print("ucascode: ", ucascode)
            item['ucascode'] = ''.join(ucascode).replace("UCAS Code:", "").strip()
            print("item['ucascode'] = ", item['ucascode'])

            duration = response.xpath("//strong[contains(text(),'Duration')]//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration_str = ''.join(duration)

            duration_list = getIntDuration(duration_str)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            # //strong[contains(text(),'Start month')]
            start_date = response.xpath("//strong[contains(text(),'Start month')]//text()").extract()
            clear_space(start_date)
            # print("start_date: ", start_date)
            # item['start_date'] = getStartDate(''.join(start_date))
            # print("item['start_date'] = ", item['start_date'])

            overview = response.xpath("//div[@id='overview']").extract()
            if len(overview) == 0:
                overview = response.xpath("//div[@class='grid_9']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])

            modules = response.xpath("//div[@id='curriculum']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])

            assessment_en = response.xpath("//h2[contains(text(),'ASSESSMENT AND FEEDBACK')]|//h2[contains(text(),'ASSESSMENT AND FEEDBACK')]/following-sibling::*[position()<last()]").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            career_en = response.xpath("//div[@id='careers']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            # print("item['career_en']: ", item['career_en'])

            # //h2[contains(text(),'INTERNATIONAL TUITION FEES')]/following-sibling::p[1]
            # tuition_fee = response.xpath("//div[@id='finance']//text()").extract()
            # clear_space(tuition_fee)
            # # print("tuition_fee: ", tuition_fee)
            # tuition_fee_re = re.findall(r"£[\d,]+", ''.join(tuition_fee))
            # # print("tuition_fee_re: ", tuition_fee_re)
            # if len(tuition_fee_re) > 0:
            # item['tuition_fee'] =getTuition_fee(''.join(tuition_fee))
            # if item['tuition_fee'] == 0:
            #     item['tuition_fee'] = None
            item['tuition_fee'] = 11400
            # print("item['tuition_fee']: ", item['tuition_fee'])

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
            department = response.xpath("//*[contains(text(),'Department of')]//text()|//*[contains(text(),'School of')]//text()").extract()
            clear_space(department)
            # print(department)
            department_list = []
            if len(department) > 0:
                for dep in department:
                    department_key = ''.join(dep).replace("Department of", "").replace("School of", "").lower().strip()
                    # print("department_key: ", department_key)
                    if dep_dict.get(department_key) is not None:
                        department_list.append(dep_dict.get(department_key))
            department_list = list(set(department_list))
            item['department'] = ','.join(department_list).strip().strip(",").strip()
            # print("item['department']: ", item['department'])

            entry_requirements = response.xpath("//div[@id='entry_reqs']//text()").extract()
            entry_requirements = clear_lianxu_space(entry_requirements)
            # item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            alevel = response.xpath("//th[contains(text(),'A-Levels')]/following-sibling::td//text()").extract()
            item['alevel'] = clear_lianxu_space(alevel)
            # print("item['alevel'] = ", item['alevel'])

            ib = response.xpath("//th[contains(text(),'IB')]/following-sibling::td//text()").extract()
            item['ib'] = clear_lianxu_space(ib)
            # print("item['ib'] = ", item['ib'])

            ielts_desc = response.xpath("//th[contains(text(),'IELTS')]/following-sibling::td//text()").extract()
            if len(ielts_desc) == 0:
                ielts_desc = re.findall(r".{1,20}IELTS.{1,40}", entry_requirements)
            item['ielts_desc'] = ''.join(ielts_desc)
            print("item['ielts_desc'] = ", item['ielts_desc'])

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
                item['ielts_l'] = ielts_list[2]
                item['ielts_s'] = ielts_list[2]
                item['ielts_r'] = ielts_list[1]
                item['ielts_w'] = ielts_list[1]
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            toefl_desc = re.findall(r"TOEFL.{1,40}", entry_requirements)
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

            item['apply_proces_en'] = "http://www.hope.ac.uk/undergraduate/howtoapply/"
            item['require_chinese_en'] = """<tr><th>Undergraduate (Bachelors, BA, BSc)</th><td><ul>
<li>Senior School Certificate, plus successful completion of a recognised foundation year</li>
<li>Senior School Certificate, plus successful completion of a first year of a recognised university degree</li>
<li>Chinese University / College Entrance Examination (Gaokao)</li>
<li>Graduation Certificate from a Specialised College (Zhongzhuan) or a Vocational Secondary School (Zhongzhi / Zhigao)</li>
</ul></td></tr>"""
            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a',
                      encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

