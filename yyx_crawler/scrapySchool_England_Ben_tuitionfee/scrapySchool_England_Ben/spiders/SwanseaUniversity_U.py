# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
import requests, json
from lxml import etree
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration

class SwanseaUniversity_USpider(scrapy.Spider):
    name = "SwanseaUniversity_U"

    start_urls = ["https://www.swan.ac.uk/sf-widgets/en/course/a-to-z/undergraduate?callback=jQuery17204488796514986544_1528359708486&_=1528359713212"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # 370
    # print(len(start_urls))

    def parse(self, response):
        # print("html = ", response.text)
        hrefJson = json.loads(response.text.replace(");", "").replace("/**/jQuery17204488796514986544_1528359708486(", ""))
        # print(hrefJson)
        htmlStr= hrefJson.get('html')
        # print(htmlStr)
        # 将字符串格式化为HTML文件，然后使用xpath获取专业链接
        html = etree.fromstring(htmlStr)
        links = html.xpath("//ul/li/ul/li/a/@href")
        # print(links)
        # print(len(links))
        for url in links:
            if url != "":
                yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "http://www.swansea.ac.uk/"
        item['university'] = "Swansea University"
        item['url'] = response.url
        item['degree_type'] = 1
        item['location'] = "Singleton Park, Swansea, SA2 8PP, Wales, UK"
        print("===============================")
        print(response.url)
        try:
            # ucas_code
            ucascode = response.xpath(
                "//div[@class='top-button-ucas-code']/div[@class='top-button-value']//text()").extract()
            clear_space(ucascode)
            item['ucascode'] = ''.join(ucascode).strip()
            print("item['ucascode'] = ", item['ucascode'])

            # 专业、学位类型
            courseDegreeaward = response.xpath("//h1[@class='content-header-heading']//text()").extract()
            courseDegreeawardStr = ''.join(courseDegreeaward).strip()
            print(courseDegreeawardStr)
            if len(courseDegreeawardStr) != 0:
                d = re.findall(r"^(\w+\s/\w+\s/\w+)|^(\w+/\w+/\w+)|(^\w+\s\(\w+\))|^(\w+/\s\w+)|^(\w+)", courseDegreeawardStr)
                if len(d) != 0:
                    degree_type = ''.join(list(d)[0])
                    # print(degree_type)
                    item['degree_name'] = degree_type
                    programme = courseDegreeawardStr.split(degree_type)
                    item['programme_en'] = ''.join(programme).strip()
            item['programme_en'] = item['programme_en'].replace(item['ucascode'], "").strip()
            print("item['degree_name'] = ", item['degree_name'])
            print("item['programme_en'] = ", item['programme_en'])

            # //ul[@style='width: 5000px;']/li[4]
            department = response.xpath(
                "//div[@class='breadCrumb module']//ul/li[4]//text()").extract()
            clear_space(department)
            item['department'] = ''.join(department).strip()
            # print("item['department'] = ", item['department'])

            # 课程长度
            duration = response.xpath(
                "//table[@class='top-button-course-variants-table']//tr/td//text()|//div[@class='top-button-duration']/div[@class='top-button-duration-value']/text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            # mode
            mode = response.xpath(
                "//table[@class='top-button-course-variants-table']//tr/td//text()|//div[@class='top-button-duration']/div[@class='top-button-duration-value']/small/text()").extract()
            clear_space(mode)
            # item['mode'] = ''.join(mode).strip()
            # print("item['mode'] = ", item['mode'])

            # 专业描述
            overview1 = response.xpath(
                "//div[@id='content-items']/div[@class='layout-article-items']/div[@class='title-and-body-text']").extract()
            overview2 = response.xpath("//div[@id='key-features']").extract()
            overview3 = response.xpath("//div[@id='description']").extract()
            # clear_space(overview1)
            # clear_space(overview2)
            # clear_space(overview3)
            overview1 = remove_class(clear_lianxu_space(overview1))
            overview2 = remove_class(clear_lianxu_space(overview2))
            overview3 = remove_class(clear_lianxu_space(overview3))
            # overview = '\n'.join(overview1).strip() + "\n" + '\n'.join(overview2).strip() + "\n" +  '\n'.join(overview3).strip()
            overview = overview1 + "\n" + overview2 + "\n" + overview3
            item['overview_en'] = overview
            # print("item['overview_en'] = ", item['overview_en'])

            # 课程设置
            modules = response.xpath("//div[@id='modules']").extract()
            # //div[@id='course-structure-']
            modules1 = response.xpath("//div[@id='course-structure-']").extract()
            # print(modules1)
            clear_space(modules)
            modulesEnd = re.findall(r"\(function\s\(\)\s{.*", '\n'.join(modules).strip())
            # print(modulesEnd)
            clear_space(modules1)
            modules = remove_class(clear_lianxu_space(modules)).replace(''.join(modulesEnd), '').strip()
            item['modules_en'] = modules + remove_class(clear_lianxu_space(modules1))
            # print("item['modules_en'] = ", item['modules_en'])

            # IELTS
            entryRequirements = response.xpath("//div[@id='entry-requirements']//text()").extract()
            # clear_space(entryRequirements)
            entryRequirements = clear_lianxu_space(entryRequirements)
            # item['entry_requirements'] = entryRequirements.strip()
            # print("item['entry_requirements'] = ", item['entry_requirements'])
            entryRequirementsStr = ''.join(entryRequirements)
            # print("entryRequirementsStr = ", entryRequirementsStr)

            alevel_re = response.xpath("//span[@class='top-button-grades-required-value-postgraduate']//text()").extract()
            clear_space(alevel_re)
            item['alevel'] = ''.join(alevel_re).strip()
            # print("item['alevel'] = ", item['alevel'])

            ib = response.xpath("//div[@id='entry-requirements']//*[contains(text(),'IB')]/text()|"
                                "//div[@id='entry-requirements']//*[contains(text(),'International Baccalaureate')]//text()").extract()
            # print("ib: ", ib)
            if len(ib) > 0:
                item['ib'] = ''.join(ib[0]).strip()
            # print("item['ib']1 = ", item['ib'])

            if item['ib'] == "":
                ibStart1 = entryRequirementsStr.find("International Baccalaureate")
                # if ibStart1 == -1:
                #     ibStart1 = entryRequirementsStr.find("IB")
                ibEnd = entryRequirementsStr.find("BTEC")
                if ibEnd == -1:
                    ibEnd = entryRequirementsStr.find("Welsh")
                ib = entryRequirementsStr[ibStart1:ibEnd - 1]
                item['ib'] = ''.join(ib).strip()
            # print("item['ib'] = ", item['ib'])

            pat = r".{0,50}IELTS.{0,50}"
            re_ielts = re.compile(pat)
            ielts = re_ielts.findall(entryRequirementsStr)
            item['ielts_desc'] = ''.join(ielts)
            # print("item['ielts_desc'] = ", item['ielts_desc'])

            ieltlsrw = re.findall(r"\d\.\d",  item['ielts_desc'])
            if len(ieltlsrw) >= 2:
                item['ielts'] = ieltlsrw[0]
                item['ielts_l'] = ieltlsrw[1]
                item['ielts_s'] = ieltlsrw[1]
                item['ielts_r'] = ieltlsrw[1]
                item['ielts_w'] = ieltlsrw[1]
            elif len(ieltlsrw) == 1:
                item['ielts'] = ieltlsrw[0]
                item['ielts_l'] = ieltlsrw[0]
                item['ielts_s'] = ieltlsrw[0]
                item['ielts_r'] = ieltlsrw[0]
                item['ielts_w'] = ieltlsrw[0]
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            # 学费
            # fee = html.xpath("//div[@id='tuition-fees-contents']/div[@class='table-wrapper']/table[@class='expander-item-fees-table']/tbody/tr[@class='expander-item-fees-table-row odd']/td[@class='expander-item-fees-table-data odd'][2]//text()")
            tuition_fee = response.xpath(
                "//div[@id='tuition-fees-contents']//table[@class='expander-item-fees-table']/tbody/tr[1]/td[4]//text()").extract()
            clear_space(tuition_fee)
            # print("tuition_fee: ", tuition_fee)
            if len(tuition_fee)> 0:
                item['tuition_fee'] = getTuition_fee(''.join(tuition_fee))
                item['tuition_fee_pre'] = "£"
                if item['tuition_fee'] == 0:
                    item['tuition_fee'] = None
            # print("item['tuition_fee'] = ", item['tuition_fee'])
            # print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])

            # //div[@id='how-to-apply']
            how_to_apply = response.xpath(
                "//div[@id='how-to-apply']").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(how_to_apply))
            # print("item['apply_proces_en'] = ", item['apply_proces_en'])

            assessment_en = response.xpath(
                "//a[contains(text(),'assessment')]/../..").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en'] = ", item['assessment_en'])

            career = response.xpath(
                "//div[@id='careers-and-employability']|//div[@id='careers-employability']|//div[@id='employabilitycareers']|"
                "//div[@id='employability-and-careers-']|//div[@id='careers-in-child-nursing-']|//div[@id='careers']"
                "|//div[@id='graduate-employability-and-careers']|//div[@id='careers-in-radiotherapy-physics']|//div[@id='careers-in-midwifery']|"
                "//div[@id='careers-in-neurophysiology-']|//div[@id='careers-in-psychology-']|//div[@id='careers-in-adult-nursing-']|"
                "//a[contains(text(),'Careers')]/../..").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en'] = ", item['career_en'])

            item['deadline'] = "http://www.swansea.ac.uk/undergraduate/apply/application-process/applying-for-2018/"
            # item['interview_desc_en'] = "http://www.swansea.ac.uk/undergraduate/apply/application-process/interviews/"
            item['require_chinese_en'] = """<p><strong>Undergraduate Programmes:&nbsp;<br /></strong>Candidates are expected to have achieved a <span>Senior High School Graduation Diploma plus 1 year in a recognised Higher Education Institution (with 60% pass mark)</span>, including an&nbsp;IELTS 6.0 with 5.5 in each part of the test (or&nbsp;equivalent).</p>"""
            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)
