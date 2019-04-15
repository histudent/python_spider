import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.getIELTS import get_ielts
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime

class UniversityOfPlymouth_USpider(CrawlSpider):
    name = "UniversityOfPlymouth_U"
    start_urls = ["https://www.plymouth.ac.uk/courses?course_index=A&course_type=undergraduate"]

    rules = (
        Rule(LinkExtractor(allow=r"\?course_index=[A-Z3]&course_type=undergraduate", allow_domains='www.plymouth.ac.uk'), follow=True, callback="parse_pagelist"),
        # Rule(LinkExtractor(restrict_xpaths=r"//ul[@class='course-list']/li/a"), follow=False, callback="parse_data"),
        Rule(LinkExtractor(restrict_xpaths=r"//ul[@class='course-list']/li/a", deny=r"course_index=[A-Z]&partner=y"), follow=False, callback="parse_data"),
    )

    # def parse_pagelist(self, response):
    #     print(response.url, "**********")

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "https://www.plymouth.ac.uk/"
        item['university'] = "University of Plymouth"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        print("===============================")
        print(response.url)
        try:
            # //span[@class='course-title']
            programme = response.xpath(
                "//span[@class='course-title']//text()").extract()
            clear_space(programme)
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en'] = ", item['programme_en'])

            degree_type = response.xpath(
                "//h1[@class='hero-heading']/text()").extract()
            clear_space(degree_type)
            item['degree_name'] = ''.join(degree_type).strip()
            print("item['degree_name'] = ", item['degree_name'])

            ucascode = response.xpath("//td[contains(text(),'UCAS course code')]/following-sibling::td//text()").extract()
            clear_space(ucascode)
            item['ucascode'] = ''.join(ucascode).strip()
            # print("item['ucascode']: ", item['ucascode'])

            department = response.xpath(
                "//h2[@class='school-title']//text()").extract()
            clear_space(department)
            item['department'] = ''.join(department)
            # print("item['department'] = ", item['department'])

            # 课程长度
            duration = response.xpath("//td[contains(text(),'Duration')]/following-sibling::td//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            # location
            location = response.xpath("//td[contains(text(),'Location')]/following-sibling::td//text()").extract()
            clear_space(location)
            item['location'] = ''.join(location).strip()
            # print("item['location'] = ", item['location'])

            # overview
            overview1 = response.xpath("//div[@class='overview']|//div[@id='key-features-accordion']").extract()
            # overview2 = response.xpath("//div[@id='key-features-accordion']").extract()
            # overview = remove_class(clear_lianxu_space(overview1)) + remove_class(clear_lianxu_space(overview2))
            item['overview_en'] = remove_class(clear_lianxu_space(overview1))
            # if item['overview_en'] == '':
            #     print("***overview")
            # print("item['overview_en'] = ", item['overview_en'])

            # modules
            modules = response.xpath("//div[@id='structure-accordion']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en'] = ", item['modules_en'])

            career_en = response.xpath("//div[contains(@id, 'career')]").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            print("item['career_en'] = ", item['career_en'])

            # entry_requirements
            entry_requirements = response.xpath("//div[@id='entry-requirements-accordion']//text()").extract()
            clear_space(entry_requirements)
            entry_requirements_str = ''.join(entry_requirements)
            # item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements'] = ", item['rntry_requirements'])

            # .{1,150}IELTS.{1,150}
            IELTS = re.findall(r"IELT.{1,80}|ILETS.{1,80}", entry_requirements_str)
            print("IELTS: ", IELTS)
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

            # alevel = response.xpath("//div[@id='entry-requirements-accordion']//*[contains(text(),'A Level')]/..//text()|"
            #                         "//div[@id='entry-requirements-accordion']//*[contains(text(),'A level')]//text()").extract()
            alevel = re.findall(r"A.*Level.{1,100}|A.*level.{1,100}", entry_requirements_str)
            clear_space(alevel)
            item['alevel'] = ''.join(alevel).strip()
            if item['alevel'] == '':
                print("***alevel")
            print("item['alevel'] = ", item['alevel'])
            if len(item['alevel']) > 300:
                item['alevel'] = ''.join(item['alevel'][:301])
            print("item['alevel']1 = ", item['alevel'])


            # ib = response.xpath("//div[@id='entry-requirements-accordion']//b[contains(text(),'International Baccalaureate')]/..//text()|"
            #                     "//div[@id='entry-requirements-accordion']//b[contains(text(),'IB')]/..//text()|"
            #                     "//div[@id='entry-requirements-accordion']//b[contains(text(),'International baccalaureate')]/..//text()").extract()
            # if len(ib) == 0:
            #     ib = response.xpath("//div[@id='entry-requirements-accordion']//b[contains(text(),'IB')]/../following-sibling::*[1]//text()").extract()
            #     if len(ib) == 0:
            ib = re.findall(r"IB.{1,100}|International.*Baccalaureate.{1,100}|International.*baccalaureate.{1,100}", entry_requirements_str)
            clear_space(ib)
            item['ib'] = ''.join(ib).strip()
            if item['ib'] == '':
                print("***ib")
            print("item['ib'] = ", item['ib'])

            # how_to_apply
            how_to_apply = response.xpath("//div[@id='how-to-apply-accordion']").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(how_to_apply))
            # print("item['apply_proces_en'] = ", item['apply_proces_en'])

            # //html//div[@class='course-accordions']//tr[3]/td[3]
            # how_to_apply
            tuition_fee = response.xpath("//strong[contains(text(),'International')]/../following-sibling::*[2]//text()|"
                                         "//div[@id='fees-funding-accordion']//table[1]//td//text()").extract()
            clear_space(tuition_fee)
            print("tuition_fee: ", tuition_fee)
            tuition_fee_str = ''.join(tuition_fee)
            if len(tuition_fee)>0:
                item['tuition_fee'] = getTuition_fee(tuition_fee_str)
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee']1 = ", item['tuition_fee'])
            if item['tuition_fee'] == 0:
                item['tuition_fee'] = None
                item['tuition_fee_pre'] = ""
            print("item['tuition_fee'] = ", item['tuition_fee'])
            print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])

            # https://www.plymouth.ac.uk/international/study/international-students-country-guides/asia/china
            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<p><b>Undergraduate</b></p><p>To apply for our undergraduate courses you'll need good grades in your&nbsp;
高中毕业证书
 Senior High School Graduation Examination and the&nbsp;
高考
 Chinese University Entrance Examination (Gaokao) for admission to year 1.&nbsp;</p><p>
Applicants who have completed the 专科毕业证书 &nbsp;Graduation Certificate - Specialist / Sub-degree (Zuanke) level (also known as the &nbsp;大专 Dazhuan) will be considered for final year (top-up) entry. We generally require an overall 70 per cent grade or above but this will vary depending on the institution.&nbsp;Contact us for more information: <a href="mailto:international-admissions@plymouth.ac.uk">international-admissions@plymouth.ac.uk</a>
</p><p>If you're a high school leaver, our partner college on campus, <a href="http://www.plymouth.ac.uk/international/plymouth-university-international-college">Plymouth University International College (PUIC)</a>, offers a wide variety of foundation courses. &nbsp;
</p><p><div class="table-responsive">
  <table class="table align-left">
      <tr>
            <td><b>A level</b> </td>
            <td> <b>UCAS tariff</b> </td>
            <td><b>Gaokao - percentage</b>&nbsp;</td>
            <td><b>Gaokao - overall grade</b>&nbsp;</td>
            <td><b>Gaokao - GPA</b>&nbsp;</td>
            <td> </td>
      </tr>
      <tr>
            <td> AAA </td>
            <td> 144 </td>
            <td> 90 – 100 </td>
            <td> A </td>
            <td> 4.0 </td>
            <td> </td>
      </tr>
      <tr>
            <td> BBB </td>
            <td> 120 </td>
            <td> 78 – 81 </td>
            <td> B </td>
            <td> 3.0 </td>
            <td> </td>
      </tr>
      <tr>
            <td> CCC </td>
            <td> 96 </td>
            <td> 70 – 71 </td>
            <td> C </td>
            <td> 2.0 </td>
            <td> </td>
      </tr>
</table>"""]))
            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/"+item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

