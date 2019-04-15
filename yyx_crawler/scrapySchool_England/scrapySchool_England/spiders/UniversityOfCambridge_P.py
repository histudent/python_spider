import scrapy
import re
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space, clear_space_str
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.getIELTS import get_ielts
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getDuration import getIntDuration, getTeachTime
import requests
from lxml import etree

class UniversityOfCambridge_PSpider(scrapy.Spider):
    name = "UniversityOfCambridge_P"
    # 包含研究生和博士的
    # start_urls = ["https://2018.gaobase.admin.cam.ac.uk/api/courses.datatable?qualification_type%5B%5D=1&qualification_type%5B%5D=2&study_mode=full_time"]
    # 只有taught的
    start_urls = ["https://2018.gaobase.admin.cam.ac.uk/api/courses.datatable?study_mode=full_time&taught_research=taught&qualification_type%5B%5D=2"]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3472.3 Safari/537.36"}

    def parse(self, response):
        text_dict = json.loads(response.text)
        # print(text_dict)
        print(len(text_dict.get("data")))
        data = text_dict.get("data")

        # 将所有的基本信息存到字典data_dict里面
        for d in data:
            url = d.get("prospectus_url")
            # print(d)
            # print(url)
            yield scrapy.Request(url, callback=self.parse_data, meta={url: d})

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "University of Cambridge"
        item['url'] = response.url
        # 授课方式
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        print("===============================")
        print(response.url)
        try:
            # print(response.meta)
            # print(response.url.replace("https", "http").replace("graduate.study", "2018.graduate.study").strip())
            programme_dict = response.meta.get(response.url.replace("https", "http").replace("graduate.study", "2018.graduate.study").strip())
            # print("programme_dict: ", programme_dict)

            # 专业、学位类型
            item['programme_en'] = programme_dict.get("name")
            # print("item['programme_en'] = ", item['programme_en'])

            item['degree_name'] = programme_dict.get("qualification")
            # print("item['degree_name'] = ", item['degree_name'])

            duration = programme_dict.get("full_time")
            # print(duration)
            if len(duration) != 0:
                item['teach_time'] = 'fulltime'
                duration_list = getIntDuration(duration)
                # print("duration_list: ", duration_list)
                if len(duration_list) == 2:
                    item['duration'] = duration_list[0]
                    item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])
            # print("item['teach_time'] = ", item['teach_time'])

            item['department'] = programme_dict.get("departments")
            if len(item['department']) > 0:
                item['department'] = item['department'][0]
            # print("item['department'] = ", item['department'])

            taught_research_balance = programme_dict.get("taught_research_balance")
            qualification_type = programme_dict.get("qualification_type")
            # print("taught_research_balance = ", taught_research_balance)
            # print("qualification_type = ", qualification_type)

            # if "phd" in item['degree_name'].lower():
            #     item['teach_type'] = 'phd'
            #     item['degree_type'] = 3
            # if taught_research_balance == "Entirely Research" and "phd" not in item['degree_name'].lower() or taught_research_balance == "Predominantly Research" and "phd" not in item['degree_name'].lower():
            #     item['teach_type'] = 'research'
            #     item['degree_type'] = 3
            # print("item['teach_type'] = ", item['teach_type'])
            # print("item['degree_type'] = ", item['degree_type'])


            # //div[@id='tabs-key-info']/div[@class='tab tab-1 active-tab']/p[3]/span
            item['location'] ='The Old Schools, Trinity Ln, Cambridge CB2 1T'
            # print("item['location'] = ", item['location'])


            application_open_date = response.xpath("//h4[@class='panel-title'][contains(text(),'Lent 2019')]/../following-sibling::div//dt[contains(text(),'Applications open')]/following-sibling::*[1]//text()").extract()
            # print("application_open_date: ", application_open_date)
            item['application_open_date'] = getStartDate(''.join(application_open_date))
            if item['application_open_date'] == "":
                application_open_date1 = response.xpath(
                    "//div[@id='presentations']/div[1]//h4[@class='panel-title'][1]/../following-sibling::div//dt[contains(text(),'Applications open')]/following-sibling::*[1]//text()").extract()
                # print("application_open_date1: ", application_open_date1)
                if len(application_open_date1) > 0:
                    application_open_date_sp = getStartDate(''.join(application_open_date1)).split("-")
                    item['application_open_date'] = str(int(application_open_date_sp[0])+1) + "-" + application_open_date_sp[1] + "-" + application_open_date_sp[-1]
            # print("item['application_open_date'] = ", item['application_open_date'])

            deadline = response.xpath(
                "//h4[@class='panel-title'][contains(text(),'Lent 2019')]/../following-sibling::div//dt[contains(text(),'Application deadline')]/following-sibling::*[1]//text()").extract()
            # print("deadline: ", deadline)
            item['deadline'] = getStartDate(''.join(deadline))
            if item['deadline'] == "":
                deadline1 = response.xpath(
                    "//div[@id='presentations']/div[1]//h4[@class='panel-title']/../following-sibling::div//dt[contains(text(),'Application deadline')]/following-sibling::*[1]//text()").extract()
                # print("deadline1: ", deadline1)
                if len(deadline1) > 0:
                    deadline_sp = getStartDate(''.join(deadline1)).split("-")
                    item['deadline'] = str(int(deadline_sp[0])+1) + "-" + deadline_sp[1] + "-" + deadline_sp[-1]
            # print("item['deadline'] = ", item['deadline'])

            start_date = response.xpath(
                "//h4[@class='panel-title'][contains(text(),'Lent 2019')]/../following-sibling::div//dt[contains(text(),'Course Starts')]/following-sibling::*[1]//text()").extract()
            # print("start_date: ", start_date)
            item['start_date'] = getStartDate(''.join(start_date))
            if item['start_date'] == "":
                start_date1 = response.xpath(
                    "//div[@id='presentations']/div[1]//h4[@class='panel-title']/../following-sibling::div//dt[contains(text(),'Course Starts')]/following-sibling::*[1]//text()").extract()
                # print("start_date1: ", start_date1)
                if len(start_date1) > 0:
                    start_date_sp = getStartDate(''.join(start_date1)).split("-")
                    item['start_date'] = str(int(start_date_sp[0])+1) + "-" + start_date_sp[1] + "-" + start_date_sp[-1]
            # print("item['start_date'] = ", item['start_date'])

            # //html//div[@class='content']/div[1]/div  专业描述
            overview = response.xpath(
                "//h2[contains(text(),'Continuing')]/preceding-sibling::*").extract()
            if len(overview) == 0:
                overview = response.xpath(
                    "//div[@class='field field-name-field-gao-course-overview field-type-text-long field-label-hidden']//div[@class='field-items']//div[@class='field-item even']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            print("item['overview_en'] = ", item['overview_en'])

            career_en = response.xpath(
                "//h2[contains(text(),'Continuing')]|//h2[contains(text(),'Continuing')]/following-sibling::*").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            print("item['career_en'] = ", item['career_en'])

            teaching_assessment_url = response.xpath("//h2[contains(text(), 'Primary tabs')]/../ul/li/a[contains(text(), 'Study')]/@href").extract()
            teaching_assessment_url = "https://www.graduate.study.cam.ac.uk" + ''.join(teaching_assessment_url)
            item['assessment_en'] = self.parse_assessment_en(teaching_assessment_url)
            # print("item['assessment_en'] = ", item['assessment_en'])


            entry_requirements_url = response.xpath("//h2[contains(text(), 'Primary tabs')]/../ul/li/a[contains(text(), 'Requirements')]/@href").extract()
            entry_requirements_url = "https://www.graduate.study.cam.ac.uk" + ''.join(entry_requirements_url)
            entry_dict = self.parse_rntry_requirements(entry_requirements_url)
            item['rntry_requirements'] = entry_dict.get('entry')
            # print("item['rntry_requirements'] = ", item['rntry_requirements'])

            fee_url = programme_dict.get("code")
            fee_url = "https://2018.gaobase.admin.cam.ac.uk/api/courses/" + ''.join(fee_url) + "/financial_tracker.html?fee_status=O&children=0"
            # print("fee_url: ", fee_url)
            tuition_fee = self.parse_tuition_fee(fee_url)
            if len(tuition_fee) > 0:
                item['tuition_fee'] = int(''.join(tuition_fee).replace("£", "").replace(",", "").strip())
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee'] = ", item['tuition_fee'])
            print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])

            how_to_apply_url = response.xpath(
                "//h2[contains(text(), 'Primary tabs')]/../ul/li/a[contains(text(), 'How To Apply')]/@href").extract()
            how_to_apply_url = "https://www.graduate.study.cam.ac.uk" + ''.join(how_to_apply_url)
            apply_list= self.parse_apply_proces_en(how_to_apply_url)
            if len(apply_list)==2:
                item['apply_proces_en'] = apply_list[0]
                item["apply_documents_en"] = apply_list[1]
            # print("item['apply_proces_en'] = ", item['apply_proces_en'])
            # print("item['apply_documents_en'] = ", item['apply_documents_en'])

            # print(teaching_assessment_url)
            # print(entry_requirements_url)
            # print(fee_url)
            # print(how_to_apply_url)

            ieltsDict = entry_dict
            item['ielts'] = ieltsDict.get("IELTS")
            item['ielts_l'] = ieltsDict.get("IELTS_L")
            item['ielts_s'] = ieltsDict.get("IELTS_S")
            item['ielts_r'] = ieltsDict.get("IELTS_R")
            item['ielts_w'] = ieltsDict.get("IELTS_W")
            # print("item['IELTS'] = %sitem['IELTS_L'] = %sitem['IELTS_S'] = %sitem['IELTS_R'] = %sitem['IELTS_W'] = %s==" % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            item['toefl'] = ieltsDict.get("TOEFL")
            item['toefl_l'] = ieltsDict.get("TOEFL_L")
            item['toefl_s'] = ieltsDict.get("TOEFL_S")
            item['toefl_r'] = ieltsDict.get("TOEFL_R")
            item['toefl_w'] = ieltsDict.get("TOEFL_W")
            # print("item['toefl'] = %sitem['toefl_l'] = %sitem['toefl_s'] = %sitem['toefl_r'] = %sitem['toefl_w'] = %s==" % (
            #         item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

            apply_fee_re = re.findall(r".{1,50}application\sfee.{1,50}", item['apply_proces_en'])
            # print("apply_fee_re: ", apply_fee_re)
            apply_fee_re1 = re.findall(r"£\d+\s", ''.join(apply_fee_re))
            # print("apply_fee_re1: ", apply_fee_re1)
            if len(apply_fee_re1) > 0:
                item['apply_fee'] = apply_fee_re1[0].replace("£", "").strip()
                item["apply_pre"] = "£"
            # print("item['apply_fee'] = ", item['apply_fee'])
            # print("item['apply_pre'] = ", item['apply_pre'])

            gre_re = re.findall(r"GRE.{1,100}", item['apply_proces_en'])
            # print("gre_re: ", gre_re)
            item['gre'] = ''.join(gre_re).strip()
            del_gre = re.findall(r"<[/a-zA-Z0-9]+>", item['gre'])
            # print("del_gre: ", del_gre)
            if len(del_gre) > 0:
                for d in del_gre:
                    item['gre'] = item['gre'].replace(d, '').strip()
            # print("item['gre'] = ", item['gre'])

            gmat_re = re.findall(r"GMAT.{1,50}", item['apply_proces_en'])
            # print("gmat_re: ", gmat_re)
            item['gmat'] = ''.join(gmat_re).strip()
            del_gmat = re.findall(r"<[/a-zA-Z0-9]+>", item['gmat'])
            # print("del_gmat: ", del_gmat)
            if len(del_gmat) > 0:
                for d in del_gmat:
                    item['gmat'] = item['gmat'].replace(d, '').strip()
            # print("item['gmat'] = ", item['gmat'])

            work_experience_desc_en_re = re.findall(r".{1,80}work\sexperience.{1,80}", item['apply_proces_en'], re.I)
            # print("work_experience_desc_en_re: ", work_experience_desc_en_re)
            item['work_experience_desc_en'] = ''.join(work_experience_desc_en_re).strip()
            # print("item['work_experience_desc_en'] = ", item['work_experience_desc_en'])
            yield item
        except Exception as e:
            with open("scrapySchool_England/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_assessment_en(self, teaching_assessment_url):
        data = requests.get(teaching_assessment_url, headers=self.headers)
        response = etree.HTML(data.text)
        # print(response)
        assessment_en = response.xpath("//div[@class='field field-name-field-gao-course-study field-type-text-long field-label-hidden']")
        ass = etree.tostring(assessment_en[0], encoding='unicode', pretty_print=False, method='html')
        # print("************", assessment_en)
        # print(ass)
        ass = remove_class(clear_space_str(ass))
        # print(ass)
        return ass

    def parse_rntry_requirements(self, entry_requirements_url):
        data = requests.get(entry_requirements_url, headers=self.headers)
        response = etree.HTML(data.text)
        # print(response)
        entry_requirements = response.xpath("//div[@class='field field-name-field-gao-course-requirements field-type-text-long field-label-hidden']")
        entry = etree.tostring(entry_requirements[0], encoding='unicode', pretty_print=False, method='html')
        # print("************", assessment_en)
        # print(ass)
        entry = remove_class(clear_space_str(entry))
        # print(ass)

        english_dict = {}
        # 获取雅思托福分数
        ielts = response.xpath("//div[@class='content campl-content-container']/div[@class='field field-name-field-gao-course-requirements field-type-text-long field-label-hidden']/div[@class='field-items']/div[@class='field-item even']/div[1]/div[1]/table[1]/tbody[1]//th[contains(text(),'Total')]/following-sibling::*[1]//text()")
        ielts_l = response.xpath("//div[@class='content campl-content-container']/div[@class='field field-name-field-gao-course-requirements field-type-text-long field-label-hidden']/div[@class='field-items']/div[@class='field-item even']/div[1]/div[1]/table[1]/tbody[1]//th[contains(text(),'Listening')]/following-sibling::*[1]//text()")
        ielts_s = response.xpath("//div[@class='content campl-content-container']/div[@class='field field-name-field-gao-course-requirements field-type-text-long field-label-hidden']/div[@class='field-items']/div[@class='field-item even']/div[1]/div[1]/table[1]/tbody[1]//th[contains(text(),'Speaking')]/following-sibling::*[1]//text()")
        ielts_r = response.xpath("//div[@class='content campl-content-container']/div[@class='field field-name-field-gao-course-requirements field-type-text-long field-label-hidden']/div[@class='field-items']/div[@class='field-item even']/div[1]/div[1]/table[1]/tbody[1]//th[contains(text(),'Reading')]/following-sibling::*[1]//text()")
        ielts_w = response.xpath("//div[@class='content campl-content-container']/div[@class='field field-name-field-gao-course-requirements field-type-text-long field-label-hidden']/div[@class='field-items']/div[@class='field-item even']/div[1]/div[1]/table[1]/tbody[1]//th[contains(text(),'Writing')]/following-sibling::*[1]//text()")
        english_dict['IELTS'] = ''.join(ielts)
        english_dict['IELTS_L'] = ''.join(ielts_l)
        english_dict['IELTS_S'] = ''.join(ielts_s)
        english_dict['IELTS_R'] = ''.join(ielts_r)
        english_dict['IELTS_W'] = ''.join(ielts_w)

        toefl = response.xpath(
            "//div[@class='content campl-content-container']/div[@class='field field-name-field-gao-course-requirements field-type-text-long field-label-hidden']/div[@class='field-items']/div[@class='field-item even']/div[1]/div[1]/table[1]/tbody[1]//th[contains(text(),'Total')]/following-sibling::*[1]//text()")
        toefl_l = response.xpath(
            "//div[@class='content campl-content-container']/div[@class='field field-name-field-gao-course-requirements field-type-text-long field-label-hidden']/div[@class='field-items']/div[@class='field-item even']/div[1]/div[1]/table[1]/tbody[1]//th[contains(text(),'Listening')]/following-sibling::*[1]//text()")
        toefl_s = response.xpath(
            "//div[@class='content campl-content-container']/div[@class='field field-name-field-gao-course-requirements field-type-text-long field-label-hidden']/div[@class='field-items']/div[@class='field-item even']/div[1]/div[1]/table[1]/tbody[1]//th[contains(text(),'Speaking')]/following-sibling::*[1]//text()")
        toefl_r = response.xpath(
            "//div[@class='content campl-content-container']/div[@class='field field-name-field-gao-course-requirements field-type-text-long field-label-hidden']/div[@class='field-items']/div[@class='field-item even']/div[1]/div[1]/table[1]/tbody[1]//th[contains(text(),'Reading')]/following-sibling::*[1]//text()")
        toefl_w = response.xpath(
            "//div[@class='content campl-content-container']/div[@class='field field-name-field-gao-course-requirements field-type-text-long field-label-hidden']/div[@class='field-items']/div[@class='field-item even']/div[1]/div[1]/table[1]/tbody[1]//th[contains(text(),'Writing')]/following-sibling::*[1]//text()")
        english_dict['TOEFL'] = ''.join(toefl)
        english_dict['TOEFL_L'] = ''.join(toefl_l)
        english_dict['TOEFL_S'] = ''.join(toefl_s)
        english_dict['TOEFL_R'] = ''.join(toefl_r)
        english_dict['TOEFL_W'] = ''.join(toefl_w)
        # print(english_dict)
        english_dict['entry'] = entry
        return english_dict

    def parse_tuition_fee(self, fee_url):
        data = requests.get(fee_url, headers=self.headers)
        response = etree.HTML(data.text)
        # print(response)
        fee = response.xpath("//div[@id='fee_1']//th[contains(text(),'Total Annual Commitment')]/following-sibling::*[1]//text()")
        # print(ass)
        return fee

    def parse_apply_proces_en(self, how_to_apply_url):
        data = requests.get(how_to_apply_url, headers=self.headers)
        response = etree.HTML(data.text)
        # print(response)
        apply_proces_en = response.xpath("//div[@class='field field-name-field-gao-course-apply field-type-text-long field-label-hidden']")
        # 将Element转换成HTML格式
        apply = ""
        if len(apply_proces_en) > 0:
            apply = etree.tostring(apply_proces_en[0], encoding='unicode', pretty_print=False, method='html')
            apply = remove_class(clear_space_str(apply))

        apply_documents_en = response.xpath(
           '//h2[contains(text(),"Things")]/preceding-sibling::*[1]/following-sibling::*')
        # 将Element转换成HTML格式
        apply_documents = ""
        if len(apply_documents_en) > 0:
            for d in apply_documents_en:
                apply_documents += etree.tostring(d, encoding='unicode', pretty_print=False, method='html')
        apply_documents = remove_class(clear_space_str(apply_documents))
        return [apply, apply_documents]
