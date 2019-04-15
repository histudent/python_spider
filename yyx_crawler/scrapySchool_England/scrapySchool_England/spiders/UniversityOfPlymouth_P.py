import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.getIELTS import get_ielts
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getDuration import getIntDuration, getTeachTime

class UniversityOfPlymouth_PSpider(CrawlSpider):
    name = "UniversityOfPlymouth_P"
    start_urls = ["https://www.plymouth.ac.uk/courses?course_index=A&course_type=postgraduate"]

    rules = (
        Rule(LinkExtractor(allow=r"\?course_index=[A-Z]&course_type=postgraduate", allow_domains='www.plymouth.ac.uk'), follow=True, callback="parse_pagelist"),
        # Rule(LinkExtractor(restrict_xpaths=r"//ul[@class='course-list']/li/a"), follow=False, callback="parse_data"),
        Rule(LinkExtractor(restrict_xpaths=r"//ul[@class='course-list']/li/a", deny=r"course_index=[A-Z]&partner=y"), follow=False, callback="parse_data"),
    )

    # def parse_pagelist(self, response):
    #     print(response.url, "**********")

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.plymouth.ac.uk/"
        item['university'] = "University of Plymouth"
        item['url'] = response.url
        # 授课方式
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        print("===============================")
        print(response.url)
        try:
            # //span[@class='course-title']
            programme = response.xpath(
                "//span[@class='course-title']//text()").extract()
            clear_space(programme)
            item['programme_en'] = ''.join(programme).strip()
            # print("item['programme_en'] = ", item['programme_en'])

            degree_type = response.xpath(
                "//h1[@class='hero-heading']/text()").extract()
            clear_space(degree_type)
            item['degree_name'] = ''.join(degree_type).strip()
            # print("item['degree_name'] = ", item['degree_name'])

            degree_name_lower = item['degree_name'].lower()
            # print("degree_name_lower: ", degree_name_lower)
            if "phd" in degree_name_lower:
                item['teach_type'] = 'phd'
                item['degree_type'] = 3
            elif "res" in degree_name_lower:
                item['teach_type'] = 'research'
                item['degree_type'] = 3
            # print("item['teach_type'] = ", item['teach_type'])
            # print("item['degree_type'] = ", item['degree_type'])

            department = response.xpath(
                "//h2[@class='school-title']//text()").extract()
            clear_space(department)
            item['department'] = ''.join(department)
            # print("item['department'] = ", item['department'])

            # 课程长度
            duration = response.xpath("//td[contains(text(),'Duration')]/following-sibling::td//text()").extract()
            clear_space(duration)
            # print(duration)
            duration_list = getIntDuration(''.join(duration))
            # print("duration_list: ", duration_list)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            # mode
            mode = response.xpath("//td[contains(text(),'Course type')]/following-sibling::td//text()").extract()
            clear_space(mode)
            # print("mode: ", mode)
            item['teach_time'] = getTeachTime(''.join(mode))
            # print("item['teach_time'] = ", item['teach_time'])

            # location
            location = response.xpath("//td[contains(text(),'Location')]/following-sibling::td//text()").extract()
            clear_space(location)
            item['location'] = ''.join(location).strip()
            # print("item['location'] = ", item['location'])

            # overview
            overview1 = response.xpath("//div[@class='overview']").extract()
            overview2 = response.xpath("//div[@id='key-features-accordion']").extract()
            overview = remove_class(clear_lianxu_space(overview1)) + remove_class(clear_lianxu_space(overview2))
            item['overview_en'] = overview
            # print("item['overview_en'] = ", item['overview_en'])

            # modules
            modules = response.xpath("//div[@id='structure-accordion']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en'] = ", item['modules_en'])

            # entry_requirements
            entry_requirements = response.xpath("//div[@id='entry-requirements-accordion']//text()").extract()
            item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements'] = ", item['rntry_requirements'])

            # .{1,150}IELTS.{1,150}
            IELTS = re.findall(r"(.{1,80}IELTS.{1,80})|(.{1,80}ILETS.{1,80})|(.{1,80}IELTs.{1,80})", item['rntry_requirements'])
            # print(IELTS)
            if len(IELTS) != 0:
                ielts = ''.join(list(IELTS[0])).strip()
                item['ielts_desc'] = ielts
            print("item['ielts_desc'] = ", item['ielts_desc'])

            ieltsDict = get_ielts(item['ielts_desc'])
            item['ielts'] = ieltsDict.get("IELTS")
            item['ielts_l'] = ieltsDict.get("IELTS_L")
            item['ielts_s'] = ieltsDict.get("IELTS_S")
            item['ielts_r'] = ieltsDict.get("IELTS_R")
            item['ielts_w'] = ieltsDict.get("IELTS_W")
            if item['ielts'] != None:
                item['ielts'] = item['ielts'].strip(".").strip()
            if item['ielts_l'] != None:
                item['ielts_l'] = item['ielts_l'].strip(".").strip()
            if item['ielts_s'] != None:
                item['ielts_s'] = item['ielts_s'].strip(".").strip()
            if item['ielts_r'] != None:
                item['ielts_r'] = item['ielts_r'].strip(".").strip()
            if item['ielts_w'] != None:
                item['ielts_w'] = item['ielts_w'].strip(".").strip()
            print("item['IELTS'] = %sitem['IELTS_L'] = %sitem['IELTS_S'] = %sitem['IELTS_R'] = %sitem['IELTS_W'] = %s==" % (
                    item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            # how_to_apply
            how_to_apply = response.xpath("//div[@id='how-to-apply-accordion']").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(how_to_apply))
            # print("item['apply_proces_en'] = ", item['apply_proces_en'])

            # //html//div[@class='course-accordions']//tr[3]/td[3]
            # how_to_apply
            tuition_fee = response.xpath("//strong[contains(text(),'International')]/../following-sibling::*[2]//text()").extract()
            clear_space(tuition_fee)
            # print(tuition_fee)
            tuition_fee_str = ''.join(tuition_fee)
            if tuition_fee_str == "To be confirmed" or tuition_fee_str == "":
                item['tuition_fee'] = None
            else:
                item['tuition_fee'] = int(tuition_fee_str.replace("£", "").replace(",", "").strip())
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee'] = ", item['tuition_fee'])
            # print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])

            # https://www.plymouth.ac.uk/international/study/international-students-country-guides/asia/china
            item['require_chinese_en'] = """<p><b>Postgraduate</b></p><p>For postgraduate programmes, you'll need either a bachelor's degree (with high grades), a masters degree from a ranked Chinese university or a good honours degree from a British university.&nbsp;</p><p><div class="table-responsive">
<table>
<tr>
<td><b>Chinese degree classification - prestigious i</b><b>nstitution</b></td>
<td><b>Chinese degree classification - non-prestigious institution</b></td>
<td><b>Chinese degree classification - college institution</b></td>
<td><b>UK degree equivalent</b></td>
<td></td>
</tr>
<tr>
<td>80%</td>
<td>85%</td>
<td>90%</td>
<td>1st</td>
<td></td>
</tr>
<tr>
<td>75%</td>
<td>80%</td>
<td>85%</td>
<td>2:1</td>
<td></td>
</tr>
<tr>
<td>70%</td>
<td>75%</td>
<td>80%</td>
<td>2:2</td>
<td></td>
</tr>
</table></div>"""
            yield item
        except Exception as e:
            with open(item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

