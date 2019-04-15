# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.getItem import get_item
from scrapySchool_England.getTuition_fee import getTuition_fee
import requests, json
from lxml import etree
from scrapySchool_England.getIELTS import get_ielts, get_toefl

class SwanseaUniversityPrifysgolAbertawe_USpider(scrapy.Spider):
    name = "SwanseaUniversityPrifysgolAbertawe_U"

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
        item = get_item(ScrapyschoolEnglandItem)
        item['country'] = "England"
        item["website"] = "http://www.swansea.ac.uk/"
        item['university'] = "Swansea University Prifysgol Abertawe"
        # item['create_person'] = 'yangyaxia'
        item['url'] = response.url
        print("===============================")
        print(response.url)
        try:
            # 专业、学位类型
            courseDegreeaward = response.xpath("//h1[@class='content-header-heading']//text()").extract()
            courseDegreeawardStr = ''.join(courseDegreeaward)
            if len(courseDegreeawardStr) != 0:
                d = re.findall(r"^(\w+\s/\w+\s/\w+)|^(\w+/\w+/\w+)|(^\w+\s\(\w+\))|^(\w+/\s\w+)|^(\w+)", courseDegreeawardStr)
                if len(d) != 0:
                    degree_type = ''.join(list(d)[0])
                    # print(degree_type)
                    item['degree_type'] = degree_type
                    programme = courseDegreeawardStr.split(degree_type)
                    item['programme'] = ''.join(programme).strip()
            # print("item['degree_type'] = ", item['degree_type'])
            # print("item['programme'] = ", item['programme'])

            # //ul[@style='width: 5000px;']/li[4]
            department = response.xpath(
                "//div[@class='breadCrumb module']//ul/li[4]//text()").extract()
            clear_space(department)
            item['department'] = ''.join(department).strip()
            # print("item['department'] = ", item['department'])

            # ucas_code
            ucas_code = response.xpath(
                "//div[@class='top-button-ucas-code']/div[@class='top-button-value']//text()").extract()
            clear_space(ucas_code)
            item['ucas_code'] = ''.join(ucas_code).strip()
            print("item['ucas_code'] = ", item['ucas_code'])

            # 课程长度
            duration = response.xpath(
                "//table[@class='top-button-course-variants-table']//tr/td//text()|//div[@class='top-button-duration']/div[@class='top-button-duration-value']/text()").extract()
            clear_space(duration)
            item['duration'] = ''.join(duration).strip()
            # print("item['duration'] = ", item['duration'])

            # mode
            mode = response.xpath(
                "//table[@class='top-button-course-variants-table']//tr/td//text()|//div[@class='top-button-duration']/div[@class='top-button-duration-value']/small/text()").extract()
            clear_space(mode)
            # item['mode'] = ''.join(mode).strip()
            # print("item['mode'] = ", item['mode'])

            # 专业描述
            overview1 = response.xpath(
                "//div[@id='content-items']/div[@class='layout-article-items']/div[@class='title-and-body-text']//text()").extract()
            overview2 = response.xpath("//div[@id='key-features']//text()").extract()
            overview3 = response.xpath("//div[@id='description']//text()").extract()
            # clear_space(overview1)
            # clear_space(overview2)
            # clear_space(overview3)
            overview1 = clear_lianxu_space(overview1)
            overview2 = clear_lianxu_space(overview2)
            overview3 = clear_lianxu_space(overview3)
            # overview = '\n'.join(overview1).strip() + "\n" + '\n'.join(overview2).strip() + "\n" +  '\n'.join(overview3).strip()
            overview = overview1 + "\n" + overview2 + "\n" + overview3
            item['overview'] = overview.strip()
            # print("item['overview'] = ", item['overview'])

            # 课程设置
            modules = response.xpath("//div[@id='modules']//text()").extract()
            # //div[@id='course-structure-']
            modules1 = response.xpath("//div[@id='course-structure-']//text()").extract()
            # print(modules1)
            clear_space(modules)
            modulesEnd = re.findall(r"\(function\s\(\)\s{.*", '\n'.join(modules).strip())
            # print(modulesEnd)
            clear_space(modules1)
            modules = '\n'.join(modules).strip().strip(''.join(modulesEnd)).strip()
            item['modules'] = modules + '\n'.join(modules1).strip()
            # print("item['modules'] = ", item['modules'])

            # IELTS
            entryRequirements = response.xpath("//div[@id='entry-requirements']//text()").extract()
            # clear_space(entryRequirements)
            entryRequirements = clear_lianxu_space(entryRequirements)
            item['entry_requirements'] = entryRequirements.strip()
            # print("item['entry_requirements'] = ", item['entry_requirements'])
            entryRequirementsStr = ''.join(entryRequirements)

            if "Entry Requirements" in entryRequirementsStr:
                alevelStart = entryRequirementsStr.find("Entry Requirements")
                ibStart = entryRequirementsStr.find("International Baccalaureate")
                alevel = entryRequirementsStr[alevelStart:ibStart]
                item['Alevel'] = alevel
            else:
                item['Alevel'] = ""
            ibStart1 = entryRequirementsStr.find("International Baccalaureate")
            if ibStart1 == -1:
                ibStart1 = entryRequirementsStr.find("IB")
            ibEnd = entryRequirementsStr.find("BTEC (18-unit)")
            if ibEnd == -1:
                ibEnd = entryRequirementsStr.find("Welsh")
            ib = entryRequirementsStr[ibStart1:ibEnd - 1]
            item['IB'] = ib
            # print("item['Alevel'] = ", item['Alevel'])
            # print("item['IB'] = ", item['IB'])

            # .{0,100}(IELTS).{0,100}
            # ielts = re.findall(r"\.[a-zA-Z0-9\s.]{0,80}(IELTS)[a-zA-Z0-9\s.\(\))]{0,80}", entryRequirementsStr)
            pat = r".{0,50}IELTS.{0,50}"
            re_ielts = re.compile(pat)
            ielts = re_ielts.findall(entryRequirementsStr)
            item['IELTS'] = ''.join(ielts)
            # print("item['IELTS'] = ", item['IELTS'])
            ielts = item['IELTS']
            ieltlsrw = re.findall(r"\d\.\d", ielts)
            # ieltlsrw = re.findall(r"[\d\.]{1,4}", ielts)
            # ieltlsrw = get_ielts(ielts)
            # print(ieltlsrw)
            if len(ieltlsrw) >= 2:
                item['IELTS'] = ieltlsrw[0]
                item['IELTS_L'] = ieltlsrw[1]
                item['IELTS_S'] = ieltlsrw[1]
                item['IELTS_R'] = ieltlsrw[1]
                item['IELTS_W'] = ieltlsrw[1]
            elif len(ieltlsrw) == 1:
                item['IELTS'] = ieltlsrw[0]
                item['IELTS_L'] = ieltlsrw[0]
                item['IELTS_S'] = ieltlsrw[0]
                item['IELTS_R'] = ieltlsrw[0]
                item['IELTS_W'] = ieltlsrw[0]
            # print(
            #     "item['IELTS'] = %s item['IELTS_L'] = %s item['IELTS_S'] = %s item['IELTS_R'] = %s item['IELTS_W'] = %s " % (
            #     item['IELTS'], item['IELTS_L'], item['IELTS_S'], item['IELTS_R'], item['IELTS_W']))

            # 学费
            # fee = html.xpath("//div[@id='tuition-fees-contents']/div[@class='table-wrapper']/table[@class='expander-item-fees-table']/tbody/tr[@class='expander-item-fees-table-row odd']/td[@class='expander-item-fees-table-data odd'][2]//text()")
            tuition_fee = response.xpath(
                "//div[@id='tuition-fees-contents']//table[@class='expander-item-fees-table']/tbody/tr[1]/td[4]//text()").extract()
            clear_space(tuition_fee)
            item['tuition_fee'] = ''.join(tuition_fee)
            # print("item['tuition_fee'] = ", item['tuition_fee'])

            # //div[@id='how-to-apply']
            how_to_apply = response.xpath(
                "//div[@id='how-to-apply']//text()").extract()
            clear_space(how_to_apply)
            item['how_to_apply'] = '\n'.join(how_to_apply).strip()
            # print("item['how_to_apply'] = ", item['how_to_apply'])

            career = response.xpath(
                "//div[@id='careers-and-employability']//text()|//div[@id='careers-employability']//text()|//div[@id='employabilitycareers']//text()|//div[@id='employability-and-careers-']//text()|//div[@id='careers-in-child-nursing-']//text()|//div[@id='careers']//text()|//div[@id='graduate-employability-and-careers']//text()|//div[@id='careers-in-radiotherapy-physics']//text()|//div[@id='careers-in-midwifery']//text()|//div[@id='careers-in-neurophysiology-']//text()|//div[@id='careers-in-psychology-']//text()|//div[@id='careers-in-adult-nursing-']//text()").extract()
            clear_space(career)
            item['career'] = '\n'.join(career).strip()
            # print("item['career'] = ", item['career'])

            item['deadline'] = "http://www.swansea.ac.uk/undergraduate/apply/application-process/applying-for-2018/"
            item['interview'] = "http://www.swansea.ac.uk/undergraduate/apply/application-process/interviews/"
            item['chinese_requirements'] = """"""
            yield item
        except Exception as e:
            with open("./error/"+item['university']+str(item['degree_level'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================"+str(item['create_time'])+"\n")
            print("异常：", str(e))
            print("报错url：", response.url)
