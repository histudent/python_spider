import scrapy
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl

class TheUniversityofManchester_RSpider(scrapy.Spider):
    name = "TheUniversityofManchester_R"
    start_urls = ["http://www.manchester.ac.uk/study/postgraduate-research/programmes/list/xml/"]

    def parse(self, response):
        links = response.xpath("//ul/li//a/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))
        for link in links:
            url = "http://www.manchester.ac.uk/study/postgraduate-research/programmes/list/" + link + "all-content/"
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.manchester.ac.uk/"
        item['university'] = "The University of Manchester"
        item['url'] = response.url
        # 授课方式
        item['teach_type'] = 'research'
        # 学位类型
        item['degree_type'] = 3
        item['location'] = "Oxford Rd, Manchester, M13 9PL, UK"
        print("===============================")
        print(response.url)
        try:
            # print(response.url)
            # 专业、学位类型
            programmeDegree = response.xpath("//div[@id='course-profile']/div[@class='heading']/h1//text()").extract()
            clear_space(programmeDegree)
            programmeDegreeStr = ''.join(programmeDegree)
            # print(programmeDegreeStr)
            degree_type = list(re.findall(r"^(\w{0,6})|(\w{0,6}/\w{0,6})\s", programmeDegreeStr)[0])
            # print("degree_type = ", degree_type)
            item['degree_name'] = ''.join(degree_type)
            programme = programmeDegreeStr.split(''.join(degree_type))
            item['programme_en'] = programme[-1].strip()
            # print("item['degree_name'] = ", item['degree_name'])
            # print("item['programme_en'] = ", item['programme_en'])

            if item['degree_name'] == "PhD":
                item['teach_type'] = 'phd'

            start_date = response.xpath("//*[contains(text(), 'Year of entry:')]//text()").extract()
            item['start_date'] = ''.join(start_date).replace("Year of entry:", "").strip()
            # print("item['start_date'] = ", item['start_date'])

            duration = response.xpath("//div[@id='course-profile']/div[@class='course-profile-content full-page']/div[@class='fact-file']/dl/dd[2]//text()").extract()
            durationStr = ''.join(duration)
            # print("durationStr = ", durationStr)
            if "full" in durationStr or "Full" in durationStr or "FT" in durationStr or "ft" in durationStr:
                item['teach_time'] = "fulltime"
            duration_re = re.findall(r"([a-zA-Z0-9\.]+\s)(year|month|week|yr|yft){1}|([0-9\.]+)(yr|yft|\-month){1}", durationStr, re.I)
            # print("duration_re = ", duration_re)
            d_dict = {"One": "1",
                      "Two": "2",
                      "Three": "3",
                      "Four": "4",
                      "Five": "5",
                      "Six": "6",
                      "Seven": "7",
                      "Eight": "8",
                      "Nine": "9",
                      "Ten": "10",
                      "one": "1",
                      "two": "2",
                      "three": "3",
                      "four": "4",
                      "five": "5",
                      "six": "6",
                      "seven": "7",
                      "eight": "8",
                      "nine": "9",
                      "ten": "10",
                      }
            if len(duration_re) > 0:
                d_int = re.findall(r"\d+", ''.join(duration_re[0]))
                if len(d_int) > 0:
                    item['duration'] = int(''.join(d_int))
                else:
                    d = re.findall(
                        r"(One)|(Two)|(Three)|(Four)|(Five)|(Six)|(Seven)|(Eight)|(Nine)|(Ten)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(ten)",
                        ', '.join(duration_re[0]))
                    print("d = ", d)
                    item['duration'] = int(d_dict.get(''.join(d[0]).strip()))
                if "y" in ''.join(duration_re[0]) or "Y" in ''.join(duration_re[0]):
                    item['duration_per'] = 1
                elif "m" in ''.join(duration_re[0]) or "M" in ''.join(duration_re[0]):
                    item['duration_per'] = 3
                elif "w" in ''.join(duration_re[0]) or "W" in ''.join(duration_re[0]):
                    item['duration_per'] = 4
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            department = response.xpath(
                "//*[contains(text(), 'Academic department')]/following-sibling::*[1]//text()").extract()
            clear_space(department)
            # print(department)
            if len(department) > 0:
                item['department'] = department[0]
            # print("item['department'] = ", item['department'])

            # 专业描述，雅思托福，就业方向, 学术要求，How To Apply
            overview = response.xpath('//h3[@id="programme-description"]/following-sibling::div[1]|//h3[@id="course-description"]/following-sibling::div[1]').extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en'] = ", item['overview_en'])

            # Entry requirements
            rntry_requirements = response.xpath(
                '//h2[@id="entry-requirements"]/following-sibling::*[position()<9]//text()').extract()
            item['rntry_requirements'] = clear_lianxu_space(rntry_requirements)
            # print("item['rntry_requirements'] = ", item['rntry_requirements'])

            # english = clear_lianxu_space(response.xpath("//h3[contains(text(), 'English language')]/following-sibling::div[1]//text()").extract())
            # print(english)
            # ielts_desc = re.findall(r".{1,100}IELTS.{1,100}", english.replace("IELTS", " IELTS").replace("TOEFL", " TOEFL"))
            # toefl_desc = re.findall(r".{1,100}TOEFL.{1,100}", english.replace("IELTS", " IELTS").replace("TOEFL", " TOEFL"))
            # item['ielts_desc'] = ''.join(ielts_desc).strip()
            # item['toefl_desc'] = ''.join(toefl_desc).strip()
            # print("ielts_Desc: ", ielts_desc)
            # print("toefl_desc: ", toefl_desc)

            ielts_desc = response.xpath(
                "//h3[contains(text(), 'English language')]/following-sibling::div[1]//*[contains(text(), 'IELTS')]//text()").extract()
            clear_space(ielts_desc)
            if ''.join(ielts_desc).strip() == "IELTS":
                ielts_desc = response.xpath(
                    "//h3[contains(text(), 'English language')]/following-sibling::div[1]//*[contains(text(), 'IELTS')]/..//text()").extract()
            toefl_desc = response.xpath(
                "//h3[contains(text(), 'English language')]/following-sibling::div[1]//*[contains(text(), 'TOEFL')]//text()").extract()
            clear_space(toefl_desc)
            if ''.join(toefl_desc).strip() == "IBT TOEFL:":
                toefl_desc = response.xpath(
                    "//h3[contains(text(), 'English language')]/following-sibling::div[1]//*[contains(text(), 'TOEFL')]/..//text()").extract()
            item['ielts_desc'] = clear_lianxu_space(ielts_desc)
            item['toefl_desc'] = clear_lianxu_space(toefl_desc)
            print("item['ielts_desc']: ", item['ielts_desc'])
            print("item['toefl_desc']: ", item['toefl_desc'])

            ielts_list = re.findall(r"\d[\d\.]{0,2}", item['ielts_desc'])
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
                item['ielts_r'] = ielts_list[2]
                item['ielts_w'] = ielts_list[1]
            print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                    item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            toefl_list = re.findall(r"1[0-1]\d|[12789]\d", item['toefl_desc'])
            print(toefl_list)
            if len(toefl_list) == 1:
                item['toefl'] = toefl_list[0]
                # item['toefl_l'] = toefl_list[0]
                # item['toefl_r'] = toefl_list[0]
                # item['toefl_s'] = toefl_list[0]
                # item['toefl_w'] = toefl_list[0]
            elif len(toefl_list) == 2:
                item['toefl'] = toefl_list[0]
                item['toefl_l'] = toefl_list[1]
                item['toefl_r'] = toefl_list[1]
                item['toefl_s'] = toefl_list[1]
                item['toefl_w'] = toefl_list[1]
            elif len(toefl_list) == 3:
                item['toefl'] = toefl_list[0]
                item['toefl_l'] = toefl_list[2]
                item['toefl_r'] = toefl_list[2]
                item['toefl_s'] = toefl_list[2]
                item['toefl_w'] = toefl_list[1]
            elif len(toefl_list) == 4:
                item['toefl'] = toefl_list[0]
                item['toefl_l'] = toefl_list[3]
                item['toefl_r'] = toefl_list[1]
                item['toefl_s'] = toefl_list[2]
                item['toefl_w'] = toefl_list[1]
            elif len(toefl_list) == 5:
                item['toefl'] = toefl_list[0]
                item['toefl_l'] = toefl_list[1]
                item['toefl_r'] = toefl_list[3]
                item['toefl_s'] = toefl_list[4]
                item['toefl_w'] = toefl_list[2]
            print(
                "item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
                    item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

            apply_proces_en = response.xpath(
                '//h2[@id="application-and-selection"]/following-sibling::*[position()<15]').extract()
            apply_proces_en_str = remove_class(clear_lianxu_space(apply_proces_en))
            # print(apply_proces_en_str.index("<h2>Course details</h2>"))
            if apply_proces_en_str.find("<h2>Course details</h2>") == -1:
                apply_proces_en_s1 = apply_proces_en_str[0:len(apply_proces_en_str)]
            else:
                apply_proces_en_s1 = apply_proces_en_str[:apply_proces_en_str.find("<h2>Course details</h2>")-1]
            item['apply_proces_en'] = apply_proces_en_s1
            # print("item['apply_proces_en'] = ", item['apply_proces_en'])

            interview_desc_en = response.xpath(
                '//h3[contains(text(), "Interview requirements")]/following-sibling::div[1]').extract()
            item['interview_desc_en'] = remove_class(clear_lianxu_space(interview_desc_en))
            # print("item['interview_desc_en'] = ", item['interview_desc_en'])

            modules_en = response.xpath(
                "//h3[@id='programme-content-year-1']/following-sibling::div[1]").extract()
            if len(modules_en) == 0:
                modules_en = response.xpath(
                    "//*[contains(text(), 'Course unit list')]/following-sibling::*[position()<3]").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules_en))
            # print("item['modules_en'] = ", item['modules_en'])

            assessment_en = response.xpath(
                '//*[@id="teaching-and-learning"]/following-sibling::*[position()<4]').extract()
            if len(assessment_en) == 0:
                assessment_en = response.xpath(
                    '//*[@id="coursework-and-assessment"]/following-sibling::*[position()<4]').extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en'] = ", item['assessment_en'])

            career_en = response.xpath(
                '//*[@id="careers"]/following-sibling::*').extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            # print("item['career_en'] = ", item['career_en'])


            fee1 = response.xpath("//div[@id='course-profile']/div[@class='course-profile-content full-page']/ul[1]/li[1]//text()").extract()
            # print(fee1)
            fee = clear_lianxu_space(fee1)
            fee_re = re.findall(r"International\sstudents\s\(per\sannum\):[\sa-zA-Z\-]+£[\d,]+", fee)
            fee_re1 = re.findall(r"£[\d,]+", ''.join(fee_re))
            # print("fee_re1: ", fee_re1)
            f = ''.join(fee_re1).replace("£", "").replace(",", "").strip()
            if len(f) != 0:
                item['tuition_fee'] = int(f)
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee'] = ", item['tuition_fee'])

            item['require_chinese_en'] = """<h2>Postgraduate research entry requirements</h2>
<p>For entry onto our postgraduate research degrees we require an overall mark of 85% or higher in Bachelor's and Master's of Law or related degree from a well-ranked institution with a strong Very Good mark in Master's dissertation.</p>
<p>For PhD study a degree in Law or a relevant discipline will be considered.</p>"""
            yield item
        except Exception as e:
            with open(item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)
