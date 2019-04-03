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
import json
import requests

class UniversityOfBradford_PSpider(scrapy.Spider):
    name = "UniversityOfBradford_P"
    start_urls = ["https://www.bradford.ac.uk/courses/pg/"]

    def parse(self, response):
        links = response.xpath("//html//div[@id='results_initial']//a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))
        for link in links:
            url = "https://www.bradford.ac.uk" + link
            # print(url)
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "University of Bradford"
        item['url'] = response.url
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        if "pg" in response.url:
            print("===========================")
            print(response.url)
            try:
                key_url = response.url.split("/")[-2].strip()

                programme = response.xpath("//div[@id='course-key-info']//div[@class='col-xs-12']/h1//text()").extract()
                item['programme_en'] = ''.join(programme).strip()
                print("item['programme_en']: ", item['programme_en'])

                degree_type = response.xpath("//p[@id='cAward']//text()").extract()
                item['degree_name'] = ''.join(degree_type).strip()
                print("item['degree_name']: ", item['degree_name'])

                if "phd" in item['programme_en'].lower() or item['degree_name'].lower() == "doctorate":
                    item['teach_type'] = 'phd'
                    item['degree_type'] = 3
                print("item['teach_type']: ", item['teach_type'])
                print("item['degree_type']: ", item['degree_type'])

                mode = response.xpath("//option[@value='fulltime']//text()|//span[@id='cAttendance']//text()").extract()
                clear_space(mode)
                item['teach_time'] = getTeachTime(''.join(mode))
                print("item['teach_time']: ", item['teach_time'])

                start_date_url = "https://www.bradford.ac.uk/courses/pg/pgapi.php?uri=/courses/pg/" + key_url + "/&startMonth=startMonth&level=pg&year=y2018&attendance=fulltime"
                print("start_date_url: ", start_date_url)
                start_date = json.loads(requests.get(start_date_url).text).get("data")
                print("start_date: ", start_date)
                if start_date != None:
                    if "," in start_date:
                        start_date_list = start_date.split(",")
                        for s in start_date_list:
                            item['start_date'] += getStartDate(s.lower()) + ","
                    else:
                        item['start_date'] = getStartDate(''.join(start_date).lower())
                item['start_date'] = item['start_date'].strip().strip(",").strip()
                print("item['start_date']: ", item['start_date'])
                # start_date_year = response.xpath(
                #     "//div[@class='col-xs-5']//span[@id='displayYear']//text()").extract()
                # if len(start_date_year) != 0 and item['start_date'] != "":
                #     item['start_date'] = ''.join(start_date_year).strip() + "-" + item['start_date']
                # else:
                #     item['start_date'] = ''.join(start_date_year).strip()
                # print("item['start_date']: ", item['start_date'])

                item['location'] = 'Bradford West Yorkshire BD7 1DP UK'
                # print("item['location']: ", item['location'])

                duration_url = "https://www.bradford.ac.uk/courses/pg/pgapi.php?uri=/courses/pg/" + key_url + "/&duration=duration&level=pg&year=y2018&attendance=fulltime"
                # print("duration_url: ", duration_url)
                duration = json.loads(requests.get(duration_url).text).get("data")
                # print("duration: ", duration)
                if duration != None:
                    duration_list = getIntDuration(''.join(duration))
                    if len(duration_list) == 2:
                        item['duration'] = duration_list[0]
                        item['duration_per'] = duration_list[-1]
                # print("item['duration'] = ", item['duration'])
                # print("item['duration_per'] = ", item['duration_per'])

                overview_en = response.xpath(
                    "//div[@id='overviewStripe']").extract()
                item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
                # print("item['overview_en']: ", item['overview_en'])

                entry_requirements = response.xpath("//div[@id='course-entry']//text()|//div[@id='nav-course-entry']//text()").extract()
                entry_requirements_str = ''.join(entry_requirements).strip()
                item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
                # print("item['rntry_requirements']: ", item['rntry_requirements'])

                ielts_desc = response.xpath("//div[@id='course-entry']//*[contains(text(),'IELTS')]//text()|"
                                            "//div[@id='nav-course-entry']//*[contains(text(),'IELTS')]//text()").extract()

                # print("ielts_desc: ", ielts_desc)
                item['ielts_desc'] = ''.join(ielts_desc).strip()
                # print("item['ielts_desc']: ", item['ielts_desc'])

                ielts_dict = get_ielts(item['ielts_desc'])
                item['ielts'] = ielts_dict.get('IELTS')
                item['ielts_l'] = ielts_dict.get('IELTS_L')
                item['ielts_s'] = ielts_dict.get('IELTS_S')
                item['ielts_r'] = ielts_dict.get('IELTS_R')
                item['ielts_w'] = ielts_dict.get('IELTS_W')
                # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                    # item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

                if item['ielts'] is None:
                    ielts_desc = re.findall(r"IELTS.{1,100}", entry_requirements_str)
                    clear_space(ielts_desc)
                    item['ielts_desc'] = ''.join(ielts_desc).strip()
                print("item['ielts_desc']: ", item['ielts_desc'])

                ielts_dict = get_ielts(item['ielts_desc'])
                item['ielts'] = ielts_dict.get('IELTS')
                item['ielts_l'] = ielts_dict.get('IELTS_L')
                item['ielts_s'] = ielts_dict.get('IELTS_S')
                item['ielts_r'] = ielts_dict.get('IELTS_R')
                item['ielts_w'] = ielts_dict.get('IELTS_W')
                print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                        item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

                toefl_desc = re.findall(r"TOEFL.{1,250}", entry_requirements_str)
                clear_space(toefl_desc)
                item['toefl_desc'] = ''.join(toefl_desc).strip()
                # print("item['toefl_desc']: ", item['toefl_desc'])

                toefl_list = re.findall(r"\d\d+", item['toefl_desc'])
                # print(toefl_list)
                if len(toefl_list) == 1:
                    item['toefl'] = toefl_list[0]
                    # item['toefl_l'] = toefl_list[0]
                    # item['toefl_s'] = toefl_list[0]
                    # item['toefl_r'] = toefl_list[0]
                    # item['toefl_w'] = toefl_list[0]
                elif len(toefl_list) == 2:
                    item['toefl'] = toefl_list[0]
                    item['toefl_l'] = toefl_list[1]
                    item['toefl_s'] = toefl_list[1]
                    item['toefl_r'] = toefl_list[1]
                    item['toefl_w'] = toefl_list[1]
                elif len(toefl_list) == 5:
                    item['toefl'] = toefl_list[0]
                    item['toefl_l'] = toefl_list[1]
                    item['toefl_s'] = toefl_list[3]
                    item['toefl_r'] = toefl_list[2]
                    item['toefl_w'] = toefl_list[4]
                # print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
                #                             item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

                modules = response.xpath("//div[@id='course-curriculum']").extract()
                item['modules_en'] = remove_class(clear_lianxu_space(modules))
                # print("item['modules_en']: ", item['modules_en'])

                assessment_en = response.xpath("//div[@class='row stripe background--green']").extract()
                item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
                # print("item['assessment_en']: ", item['assessment_en'])

                tuition_fee = response.xpath("//div[@id='tuitionFees']//p[contains(text(),'International:')]//text()").extract()
                if len(tuition_fee) == 0:
                    tuition_fee = response.xpath(
                        "//div[@id='tuitionFees']//text()").extract()
                clear_space(tuition_fee)
                # print("tuition_fee: ", tuition_fee)
                tuition_fee_re = re.findall(r"£\d+,\d+", ''.join(tuition_fee))

                if len(tuition_fee_re) > 0:
                    item['tuition_fee'] = getTuition_fee(''.join(tuition_fee))
                    item['tuition_fee_pre'] = "£"
                else:
                    print("***")
                print("item['tuition_fee']: ", item['tuition_fee'])
                print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

                career_en = response.xpath("//div[@id='nav-course-career']").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career_en)).replace("<div></div>", "").strip()
                # print("item['career_en']: ", item['career_en'])


                # apply_url_key = response.url.split("/")
                # print(apply_url_key)
                apply_url = "https://www.bradford.ac.uk/courses/pg/pgapi.php?uri=/courses/pg/"+key_url+"/&applyCTAModal=applyCTAModal&level=pg&year=y2018&attendance=fulltime"
                # print("apply_url: ", apply_url)
                apply = json.loads(requests.get(apply_url).text).get("data")
                if apply != None:
                    item['apply_proces_en'] = remove_class(clear_lianxu_space([apply]))
                # print("item['apply_proces_en']: ", item['apply_proces_en'])

                item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<div class="entryReq __postgraduate"><h3>Postgraduate</h3><p>The entry requirement for a postgraduate taught course is typically equivalent to a UK Second Class Honours Second Division (2:2). For individual course requirements, please see the course details in the <a href="/courses/pg/">postgraduate course listings</a>.</p>
<p>The table below shows how the University equates qualifications from your country to UK degree classifications:</p>
<table>
<tbody>
<tr><th>Qualification&nbsp;</th><th>UK 1st Class&nbsp;</th><th>UK 2:1&nbsp;</th><th>UK 2:2&nbsp;</th></tr>
<tr>
<td>Bachelor Degree 学士学位</td>
<td>85%</td>
<td>80%</td>
<td>70%</td>
</tr>
</tbody>
</table></div>
"""]))
                # print("item['require_chinese_en']: ", item['require_chinese_en'])

                department_dict = {"Advanced Biomedical Engineering":"Engineering & Informatics",
"Advanced Chemical and Petroleum Engineering":"Engineering & Informatics",
"Advanced Civil and Structural Engineering":"Engineering & Informatics",
"Advanced Mechanical Engineering":"Engineering & Informatics",
"Big Data Science and Technology":"Engineering & Informatics",
"Cyber Security":"Engineering & Informatics",
"Filmmaking":"Engineering & Informatics",
"Internet of Things (IoT)":"Engineering & Informatics",
"Nursing Studies (International)":"Health Studies",
"PhD (Faculty of Health Studies)":"Health Studies",
"Public Health":"Health Studies",
"Analytical Sciences":"Life Sciences",
"Analytical Sciences":"Life Sciences",
"Archaeological Sciences":"Life Sciences",
"Archaeological Sciences":"Life Sciences",
"Bioinformatics and Computational Biosciences":"Life Sciences",
"Cancer Drug Discovery":"Life Sciences",
"Cancer Pharmacology":"Life Sciences",
"Doctorate in Medicine":"Life Sciences",
"Drug Toxicology and Safety Pharmacology":"Life Sciences",
"Forensic Archaeology and Crime Scene Investigation":"Life Sciences",
"Forensic Archaeology and Crime Scene Investigation":"Life Sciences",
"Human Osteology and Palaeopathology":"Life Sciences",
"Human Osteology and Palaeopathology":"Life Sciences",
"Materials Chemistry":"Life Sciences",
"Medical Bioscience":"Life Sciences",
"Optometry Progression to Pre-registration Period":"Life Sciences",
"Pharmaceutical Technology and Medicines Control":"Life Sciences",
"PhD (School of Pharmacy and Medical Sciences)":"Life Sciences",
"Skin Sciences and Regenerative Medicine":"Life Sciences",
"Applied Management and Entrepreneurship":"Management & Law",
"European and International Business Management":"Management & Law",
"Finance and Investment":"Management & Law",
"Finance, Accounting and Management":"Management & Law",
"Financial Management":"Management & Law",
"MSc Human Resource Management (CIPD Accreditation)":"Management & Law",
"International Business and Management":"Management & Law",
"International Commercial Law":"Management & Law",
"International Human Rights and Development":"Management & Law",
"International Legal Studies":"Management & Law",
"International Strategic Marketing":"Management & Law",
"Logistics, Data Analytics and Supply Chain Management":"Management & Law",
"Management":"Management & Law",
"Marketing and Management":"Management & Law",
"Natural Resources and Environmental Law and Policy":"Management & Law",
"PhD (School of Law)":"Management & Law",
"PhD (School of Management)":"Management & Law",
"Advanced Practice in Peacebuilding and Conflict Resolution":"Social Sciences",
"Economics and Finance for Development":"Social Sciences",
"International Development Management":"Social Sciences",
"International Relations and Security Studies":"Social Sciences",
"Peace, Conflict and Development":"Social Sciences",
"Peace, Resilience and Social Justice":"Social Sciences",
"PhD (Faculty of Social Sciences)":"Social Sciences",
"Project Planning and Management":"Social Sciences",
"Psychology":"Social Sciences",
"Psychology of Health and Wellbeing":"Social Sciences",
"Social Work":"Social Sciences",
"Sociology, Social Policy and Crime":"Social Sciences",
"Sustainable Development":"Social Sciences",
}
                item['department'] =department_dict.get(item['programme_en'].strip())
                # print("item['department']: ", item['department'])
                if item['teach_time'] == "fulltime":
                    yield item
            except Exception as e:
                with open(item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                    f.write(str(e) + "\n" + response.url + "\n========================\n")
                print("异常：", str(e))
                print("报错url：", response.url)

