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

class UniversityOfCentralLancashire_USpider(scrapy.Spider):
    name = "UniversityOfCentralLancashire_U"
    start_urls = ["https://www.uclan.ac.uk/courses/index.php?q=undergraduate"]


    def parse(self, response):
        links = response.xpath("//h4[contains(text(),'Undergraduate')]/following-sibling::ul[1]/li/a/@href").extract()
        # 组合字典
        programme_dict = {}
        programme_list = response.xpath("//h4[contains(text(),'Undergraduate')]/following-sibling::ul[1]/li/a//h5//text()").extract()
        clear_space(programme_list)

        for link in range(len(links)):
            url = links[link]
            programme_dict[url] = programme_list[link]

        print(len(links))
        links = list(set(links))
        print(len(links))
        # print(programme_dict)
        for url in links:
            yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "https://www.uclan.ac.uk/"
        item['university'] = "University of Central Lancashire"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        # item['location'] = 'Hope Park, Liverpool, L16 9JD'
        print("===========================")
        print(response.url)
        item['major_type1'] = response.meta.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            # 专业、学位类型
            programme = response.xpath(
                "//div[@id='TopGraphic']/div[@class='twelvecol last']/h2/text()").extract()
            if len(programme) == 0:
                programme = response.xpath(
                    "//div[@class='marketing-version']/div[@class='course-title']/h1/text()").extract()
            clear_space(programme)
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en']: ", item['programme_en'])

            degree_type = response.xpath(
                "//div[@id='TopGraphic']/div[@class='twelvecol last']/h2/span/text()").extract()
            if len(degree_type) == 0:
                degree_type = response.xpath(
                    "//div[@class='marketing-version']/div[@class='course-title']/h1/span/text()").extract()
            clear_space(degree_type)
            item['degree_name'] = ''.join(degree_type).replace("(Hons)", "").strip()
            print("item['degree_name']: ", item['degree_name'])

            if "Foundation" not in item['programme_en']:
                department = response.xpath(
                    "//h4[contains(text(),'Contact Us')]/following-sibling::*[1]//text()").extract()
                clear_space(department)
                # print("department: ", department)
                if len(department) > 0:
                    for d in department:
                        if "This course is based in the" in d:
                            item['department'] = d.replace("This course is based in the", "").strip()
                            break
                # item['department'] = ''.join(department)
                # print("item['department']: ", item['department'])

                duration = response.xpath(
                    "//h4[contains(text(), 'Duration:')]/..//text()").extract()
                clear_space(duration)
                # print("duration: ", duration)
                duration_str = ''.join(duration).strip()
                item['other'] = duration_str

                duration_list = getIntDuration(duration_str)
                if len(duration_list) == 2:
                    item['duration'] = duration_list[0]
                    item['duration_per'] = duration_list[-1]
                # print("item['duration'] = ", item['duration'])
                # print("item['duration_per'] = ", item['duration_per'])

                location = response.xpath("//h4[contains(text(), 'Campus')]/following-sibling::p[1]//text()").extract()
                item['location'] = ''.join(location)
                # print("item['location']", item['location'])

                start_date = response.xpath("//h4[contains(text(), 'Start Date:')]/following-sibling::p[1]//text()").extract()
                # print(start_date)
                item['start_date'] = getStartDate(''.join(start_date))
                # print("item['start_date']", item['start_date'])

                overview = response.xpath(
                    "//div[@class='overview']|//div[@id='outline']/div[position()<3]").extract()
                item['overview_en'] = remove_class(clear_lianxu_space(overview))
                # print("item['overview_en']", item['overview_en'])
                # if item['overview_en'] == "":
                #     print("*******111")

                entry_requirements = response.xpath(
                    "//div[@class='sevencol']//div[contains(@class,'entry-requirements')]//text()").extract()
                clear_space(entry_requirements)
                print(entry_requirements)
                rntry_requirements = ''.join(entry_requirements).strip()

                item['alevel'] = None
                if "BTEC Extended Diploma:" in entry_requirements:
                    alevel = entry_requirements[:entry_requirements.index("BTEC Extended Diploma:")]
                    item['alevel'] = clear_lianxu_space(alevel)
                elif "BTEC Extended Diploma:\xa0" in entry_requirements:
                    alevel = entry_requirements[:entry_requirements.index("BTEC Extended Diploma:\xa0")]
                    item['alevel'] = clear_lianxu_space(alevel)
                elif "BTEC Extended Diploma" in entry_requirements:
                    alevel = entry_requirements[:entry_requirements.index("BTEC Extended Diploma")]
                    item['alevel'] = clear_lianxu_space(alevel)
                elif "QCFBED:" in entry_requirements:
                    alevel = entry_requirements[:entry_requirements.index("QCFBED:")]
                    item['alevel'] = clear_lianxu_space(alevel)
                elif "A Levels" in entry_requirements:
                    alevel = entry_requirements[entry_requirements.index("A Levels")+1]
                    item['alevel'] = clear_lianxu_space([alevel])
                if item['alevel'] is not None:
                    item['alevel'] = item['alevel'].strip().strip(":").strip()
                print("item['alevel']: ", item['alevel'])

                item['ib'] = None
                if "International Baccalaureate:" in entry_requirements:
                    ib = entry_requirements[entry_requirements.index("International Baccalaureate:")+1]
                    item['ib'] = clear_lianxu_space([ib])
                elif "International Baccalaureate Diploma:\xa0" in entry_requirements:
                    ib = entry_requirements[entry_requirements.index("International Baccalaureate Diploma:\xa0")+1]
                    item['ib'] = clear_lianxu_space([ib])
                elif "International Baccalaureate :" in entry_requirements:
                    ib = entry_requirements[entry_requirements.index("International Baccalaureate :")+1]
                    item['ib'] = clear_lianxu_space([ib])
                elif "International Baccalaureate:\xa0" in entry_requirements:
                    ib = entry_requirements[entry_requirements.index("International Baccalaureate:\xa0")+1]
                    item['ib'] = clear_lianxu_space([ib])
                elif "International Baccalaureate" in entry_requirements:
                    ib = entry_requirements[entry_requirements.index("International Baccalaureate")+1]
                    item['ib'] = clear_lianxu_space([ib])
                elif "International Baccalaureate Diploma:" in entry_requirements:
                    ib = entry_requirements[entry_requirements.index("International Baccalaureate Diploma:")+1]
                    item['ib'] = clear_lianxu_space([ib])
                if item['ib'] is not None:
                    item['ib'] = item['ib'].strip().strip(":").strip()
                print("item['ib']: ", item['ib'])
                # if item['ib'] == "":
                #     print("*******111")

                if "IELTS:" in entry_requirements:
                    ieltsList = entry_requirements[entry_requirements.index("IELTS:"):entry_requirements.index("IELTS:")+2]
                else:
                    ieltsList = re.findall(r'.{1,50}IELTS.{1,80}', rntry_requirements)
                item['ielts_desc'] = ''.join(ieltsList).strip()
                # print("item['ielts_desc']: ", item['ielts_desc'])

                ielts_list = re.findall(r"[5-9]\.\d\s|[5-9]\.\d,|[5-9]\.\d\.|[5-9]\.\d$|[5-9]\s|[5-9]\.", item['ielts_desc'])
                # print(ielts_list)
                if len(ielts_list) == 1:
                    item['ielts'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                    item['ielts_l'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                    item['ielts_s'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                    item['ielts_r'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                    item['ielts_w'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                elif len(ielts_list) == 2:
                    item['ielts'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                    item['ielts_l'] = ielts_list[1].strip().strip('.').replace(',', '').strip()
                    item['ielts_s'] = ielts_list[1].strip().strip('.').replace(',', '').strip()
                    item['ielts_r'] = ielts_list[1].strip().strip('.').replace(',', '').strip()
                    item['ielts_w'] = ielts_list[1].strip().strip('.').replace(',', '').strip()
                elif len(ielts_list) == 3:
                    item['ielts'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                    item['ielts_l'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                    item['ielts_s'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                    item['ielts_r'] = ielts_list[1].strip().strip('.').replace(',', '').strip()
                    item['ielts_w'] = ielts_list[2].strip().strip('.').replace(',', '').strip()
                # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))


                modules = response.xpath("//div[@id='caag']").extract()
                item['modules_en'] = remove_class(clear_lianxu_space(modules))
                # print("item['modules_en']", item['modules_en'])
                # if item['modules_en'] == "":
                #     print("*******111")

                # //h3[contains(text(),'Learning Environment and Assessment')]/..
                # assessment_en = response.xpath("//*[contains(text(),'Learning Environment and Assessment')]/..").extract()
                assessment_en = response.xpath(
                    "//*[contains(text(),'Learning Environment and Assessment')]|//*[contains(text(),'Learning Environment and Assessment')]/following-sibling::p").extract()
                item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
                # print("item['assessment_en']", item['assessment_en'])
                # if item['assessment_en'] == "":
                #     print("*******111")

                # //h4[contains(text(),'Industry Links')]|//h4[contains(text(),'Industry Links')]/following-sibling::*[1]
                career_en = response.xpath(
                    "//h4[contains(text(),'Industry Links')]/..|//h4[contains(text(),'Opportunities')]/..|"
                    "//strong[contains(text(),'Careers')]/../..").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career_en))
                # print("item['career_en']", item['career_en'])
                # if item['career_en'] == "":
                #     print("*******career")


                # https://www.uclan.ac.uk/study_here/fees_and_finance/international_tuition_fees.php#international
                item['tuition_fee'] = '12450'
                if item['department'] == "School of Forensic and Applied Sciences" or item['department'] == "School of Physical Sciences and Computing" \
                        or item['department'] == "School of Pharmacy and Biomedical Sciences" or item['department'] == "School of Engineering":
                    item['tuition_fee'] = '13450'
                item['tuition_fee_pre'] = "£"

                item['require_chinese_en'] = "<h2>Undergraduate – Year 0 entry 200 tariff points/80 tariff points</h2><p>Senior Secondary School Graduation Certificate 60% average</p><p>Completion of second year Senior Secondary School 70% average</p><h2>Undergraduate - Year 1 entry 280 tariff points/112 tariff points</h2><p>3 Year leaving certificate from SeniorHigh School with 75%</p><p>Chinese National University GaoKao University Entrance Test with 450+ (maximum is 750, 150 for each of five subjects)</p><p>Successful completion of one year Higher Education is acceptable in lieu of Grade 3 High School at 85%</p><p>Completion of Shenzhen University International Foundation Programme with 60% - Group B</p>"
                item['apply_proces_en'] = 'https://www.uclan.ac.uk/study_here/how_to_apply/international.php'

                ucascode = response.xpath("//h4[contains(text(),'UCAS Code:')]/following-sibling::*//text()").extract()
                clear_space(ucascode)
                # print("ucascode: ", ucascode)
                item['ucascode'] = ''.join(ucascode).strip()
                # print("len: ", len(ucascode))
                # print("item['ucascode'] = ", item['ucascode'])

                if item['programme_en'] != "":
                    yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

