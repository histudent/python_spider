__author__ = 'yangyaxia'
__date__ = '2018/12/18 09:00'
import scrapy
import re
from scrapySchool_Canada_College.getItem import get_item
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from w3lib.html import remove_tags
from lxml import etree
import requests

class SouthernAlbertaInstituteofTechnology_USpider(scrapy.Spider):
    name = "SouthernAlbertaInstituteofTechnology_U"
    start_urls = [
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/administrative-information-management",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/aircraft-maintenance-engineers-technology",
"https://www.sait.ca/programs-and-courses/full-time-studies/certificates/aircraft-structures-technician",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/automotive-service-technology",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/avionics-technology",
"https://www.sait.ca/programs-and-courses/full-time-studies/applied-degrees/business-administration",
"https://www.sait.ca/programs-and-courses/full-time-studies/bachelor-degrees/business-administration",
"https://www.sait.ca/programs-and-courses/full-time-studies/bachelor-degrees/construction-project-management",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/baking-and-pastry-arts",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/broadcast-systems-technology",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/business-administration-automotive-management",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/chemical-engineering-technology",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/chemical-laboratory-technology",
"https://www.sait.ca/programs-and-courses/full-time-studies/post-diploma-certificates/culinary-entrepreneurship",
"https://www.sait.ca/programs-and-courses/full-time-studies/post-diploma-certificates/cyber-security-for-control-systems-full-time",
"https://www.sait.ca/programs-and-courses/full-time-studies/certificates/database-administrator-fast-track",
"https://www.sait.ca/programs-and-courses/full-time-studies/certificates/dental-assisting",
"https://www.sait.ca/programs-and-courses/full-time-studies/certificates/diesel-equipment-technician",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/electronics-engineering-technology",
"https://www.sait.ca/programs-and-courses/full-time-studies/certificates/emergency-medical-technician",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/emergency-medical-technology-paramedic",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/energy-asset-management",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/environmental-technology",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/film-and-video-production",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/geomatics-engineering-technology",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/graphic-communications-and-print-technology",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/health-information-management",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/hospitality-management",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/instrumentation-engineering-technology",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/legal-assistant",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/library-information-technology",
"https://www.sait.ca/programs-and-courses/full-time-studies/certificates/machinist-technician",
"https://www.sait.ca/programs-and-courses/full-time-studies/certificates/medical-device-reprocessing-technician-fast-track",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/medical-laboratory-technology",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/medical-radiologic-technology",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/new-media-production-and-design",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/nuclear-medicine-technology",
"https://www.sait.ca/programs-and-courses/full-time-studies/certificates/nutrition-for-healthy-lifestyles",
"https://www.sait.ca/programs-and-courses/full-time-studies/certificates/object-oriented-software-development-fast-track",
"https://www.sait.ca/programs-and-courses/full-time-studies/certificates/office-professional",
"https://www.sait.ca/programs-and-courses/full-time-studies/certificates/power-and-process-operations",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/power-engineering-technology",
"https://www.sait.ca/programs-and-courses/apprenticeships-and-trades/pre-employment-programs/pre-employment-cabinetmaker",
"https://www.sait.ca/programs-and-courses/apprenticeships-and-trades/pre-employment-programs/pre-employment-carpenter",
"https://www.sait.ca/programs-and-courses/apprenticeships-and-trades/pre-employment-programs/pre-employment-industrial-mechanic-(millwright)",
"https://www.sait.ca/programs-and-courses/apprenticeships-and-trades/pre-employment-programs/pre-employment-plumbing",
"https://www.sait.ca/programs-and-courses/apprenticeships-and-trades/pre-employment-programs/pre-employment-steamfitter-pipefitter",
"https://www.sait.ca/programs-and-courses/apprenticeships-and-trades/pre-employment-programs/pre-employment-welding",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/professional-cooking",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/radio-television-and-broadcast-news",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/rehabilitation-therapy-assistant",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/respiratory-therapy",
"https://www.sait.ca/programs-and-courses/full-time-studies/post-diploma-certificates/technology-infrastructure-analyst-fast-track",
"https://www.sait.ca/programs-and-courses/full-time-studies/diplomas/travel-and-tourism",
"https://www.sait.ca/programs-and-courses/full-time-studies/certificates/web-developer-fast-track",
"https://www.sait.ca/programs-and-courses/full-time-studies/certificates/welding-technician", ]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaCollegeItem)
        item['school_name'] = "Southern Alberta Institute of Technology"
        item['url'] = response.url
        print("===========================")
        print(response.url)

        # item['campus'] = 'Antigonish'
        item['location'] = '1301-16 Avenue NW Calgary AB, T2M 0L4'

        item['other'] = """问题描述： 1.没有校区和专业代码"""

        # https://www.sait.ca/admissions/admission-and-selection/english-proficiency
        item['ielts_desc'] = '6.0 in each skill/category'
        item['ielts'] = '6.0'
        item['ielts_l'] = '6.0'
        item['ielts_s'] = '6.0'
        item['ielts_r'] = '6.0'
        item['ielts_w'] = '6.0'
        item['toefl_desc'] = 'A minimum score of 20 in each category'
        item['toefl'] = None
        item['toefl_l'] = '20'
        item['toefl_s'] = '20'
        item['toefl_r'] = '20'
        item['toefl_w'] = '20'

        # https://www.sait.ca/admissions/admission-and-selection/international-document-assessment
        item['require_chinese_en'] = """<div> <span>China</span> <span></span> 
<div>
<table>
<tbody>
<tr>
<td>
<p>We require precise, word-for-word English translations. Documents can be translated by a Canadian certified translator, Immigrant Services Calgary, your institution, or any other professional translation service in your country.</p>
<p>Documents from China need to be verified by China Higher Education Student Information and Career Center (CHESICC: 学信网) or China Academic Degrees &amp; Graduation Education Information (CDGDC: 学位网). Documents can be translated by one of these verification services.</p>
<p><strong>Original secondary school documents required:</strong></p>
<ul>
<li>Senior High School Graduation Diploma (高中毕业证书)</li>
<li>Senior High School transcript (成绩单)</li>
<li>Verification report ( 认证报告 ) from CHESICC (学信网) or CDGDC (学位网)</li>
</ul>
<p><strong>Original post-secondary documents required:</strong></p>
<ul>
<li>&nbsp;Zhuanke ( 专科 ):
<ul>
<li>Graduation certificate (毕业证书)</li>
<li>Academic transcript (成绩单)</li>
<li>Verification report (认证报告) from CHESICC (学信网) or CDGDC (学位网)</li>
</ul>
</li>
</ul>
<ul>
<li>Benke or higher (本科及以上学历):
<ul>
<li>Graduation certificate (毕业证书)</li>
<li>Degree certificate (学位证书)</li>
<li>Academic transcript (成绩单)</li>
<li>Verification report (认证报告) from CHESICC (学信网) or CDGDC (学位网)</li>
</ul>
</li>
</ul>
</td>
</tr>
</tbody>
</table>
</div>
</div>
"""

        #
        item['deadline'] = '2019-08-01'
        item['apply_pre'] = "CAD$"
        """You will need a Visa or Mastercard to pay the $75 online application fee.
A hard-copy application is available — the application fee is $175.
Application fees are non-refundable."""
        item['apply_fee'] = '75'
        try:
            major_name_en = response.xpath("//div[@class='middle g-text-center']/h1//text()").extract()
            clear_space(major_name_en)
            item['major_name_en'] = ''.join(major_name_en).strip()
            print("item['major_name_en']: ", item['major_name_en'])

            # //span[contains(text(),'Credential:')]/..
            degree_name = response.xpath("//span[contains(text(),'Credential:')]/../text()").extract()
            clear_space(degree_name)
            item['degree_name'] = ''.join(degree_name).strip()
            print("item['degree_name']: ", item['degree_name'])

            if item['degree_name'] == "Diploma":
                item['degree_level'] = 3
            if "Bachelor" in item['degree_name']:
                item['degree_level'] = 1
            if "Post" in item['degree_name']:
                item['degree_level'] = 2
            print("item['degree_level']: ", item['degree_level'])

            if item['degree_level'] is not None:
                duration = response.xpath("//span[contains(text(),'Length:')]/../text()").extract()
                clear_space(duration)
                print("duration: ", duration)
                # 判断课程长度单位
                if "year" in ''.join(duration).lower():
                    item['duration_per'] = 1
                if "month" in ''.join(duration).lower():
                    item['duration_per'] = 3
                if "week" in ''.join(duration).lower():
                    item['duration_per'] = 4

                duration_re = re.findall(r"\d+", ''.join(duration))
                # print("duration_re: ", duration_re)
                item['duration'] = ''.join(duration_re).strip()
                # print("item['duration']: ", item['duration'])
                # print("item['duration_per']: ", item['duration_per'])


                # //div[@class='col-1of2']//table[@class='g-table g-table-striped']//td[2]
                start_date = response.xpath("//div[@class='col-1of2']//table[@class='g-table g-table-striped']//td[2]//text()").extract()
                clear_space(start_date)
                print("start_date: ", start_date)

                monthDict = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06",
                             "july": "07", "august": "08", "september": "09", "october": "10", "november": "11",
                             "december": "12",
                             "jan": "01", "feb": "02", "mar": "03", "apr": "04", "jun": "06",
                             "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12", "sept": "09", }
                start_date_str = ""
                if len(start_date) > 0:
                    for sta in start_date:
                        month_re = re.findall(r"[A-Za-z]+", sta)
                        day_re = re.findall(r"\d+,", sta)
                        year_re = re.findall(r"\d{4}", sta)
                        # print(monthDict.get(''.join(month_re).lower().strip()))
                        if monthDict.get(''.join(month_re).lower().strip()) is not None:
                            start_date_str += ''.join(year_re) + "-" + monthDict.get(''.join(month_re).lower().strip()) + "-0" + ''.join(day_re)
                item['start_date'] = start_date_str.strip().strip(",").strip()
                print("item['start_date']: ", item['start_date'])

                overview = response.xpath(
                    "//h3[contains(text(),'Majors')]/preceding-sibling::*[position()<last()]").extract()
                if len(overview) == 0:
                    overview = response.xpath("//h3[contains(text(),'Your Career')]/preceding-sibling::*[position()<last()]|"
                                          "//h3[contains(text(),'Your career')]/preceding-sibling::*[position()<last()]").extract()
                if len(overview) > 0:
                    item['overview_en'] = remove_class(clear_lianxu_space(overview))
                print("item['overview_en']: ", item['overview_en'])

                career_key1 = r"<h3>Your Career</h3>"
                if career_key1 not in response.text:
                    career_key1 = '<h3 style="text-align: left;">Your Career</h3>'
                    if career_key1 not in response.text:
                        career_key1 = '<h3>Your career</h3>'
                career_key2 = r"<h3>Student Success</h3>"
                if career_key2 not in response.text:
                    career_key2 = '<h3 style="text-align: left;">Student Success</h3>'
                    if career_key2 not in response.text:
                        career_key2 = '<h3><a name="CET-Success"></a>Student Success</h3>'

                if career_key1 in response.text and career_key2 in response.text:
                    item['career_en'] = remove_class(getContentToXpath(response.text, career_key1, career_key2))
                # print("item['career_en']: ", item['career_en'])

                # //div[@id='admission_requirements']//div[@class='g-section g-container-sm']
                entry_requirements_en = response.xpath(
                    "//div[@id='admission_requirements']//div[@class='g-section g-container-sm']").extract()
                if len(entry_requirements_en) > 0:
                    item['entry_requirements_en'] = remove_class(clear_lianxu_space(entry_requirements_en))
                # print("item['entry_requirements_en']: ", item['entry_requirements_en'])

                modules_en = response.xpath(
                    "//div[@id='courses']/div[@class='g-section g-container-sm']").extract()
                if len(modules_en) > 0:
                    item['modules_en'] = remove_class(clear_lianxu_space(modules_en))
                # print("item['modules_en']: ", item['modules_en'])

                tuition_fee = response.xpath("//h3[contains(text(),'International Tuition and Fees*')]/following-sibling::table//tr[1]/td[2]//text()").extract()
                clear_space(tuition_fee)
                item['tuition_fee_pre'] = 'CAD$'
                item['tuition_fee'] = ''.join(tuition_fee).replace("$", "").strip()
                item['tuition_fee_per'] = 1
                # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])
                # print("item['tuition_fee']: ", item['tuition_fee'])

                department = response.xpath("//h2[contains(text(),'Contact Information')]/following-sibling::p/strong//text()").extract()
                item['department'] = ''.join(department).strip()
                # print("item['department']: ", item['department'])

                # 特殊学位分专业
                major_list_table = response.xpath(
                    "//div[@id='program_details']/div[@class='g-section g-container-sm']/table[@class='g-table g-table-striped'][1]/tbody/tr/td[1]/strong//text()").extract()
                if len(major_list_table) > 0:
                    print("major_list_table: ", major_list_table)
                    for major_list in major_list_table:
                        item['major_name_en'] = major_list.strip()
                        # print("major: ", major)
                        yield item
                else:
                    yield item
        except Exception as e:
                with open("scrapySchool_Canada_College/error/" + item['school_name'] + ".txt", 'a', encoding="utf-8") as f:
                    f.write(str(e) + "\n" + response.url + "\n========================\n")
                print("异常：", str(e))
                print("报错url：", response.url)

    def parse_modules(self, major_modules_url):
        from selenium import webdriver
        # import time
        # os.chdir(r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Lib\site-packages\selenium")
        driver = webdriver.Chrome(r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Lib\site-packages\selenium\chromedriver.exe")
        driver.get(major_modules_url)
        # time.sleep(3)
        modules_en = driver.find_element_by_xpath("//table[@cellpadding='3']").get_attribute('outerHTML')
        modules_en = remove_class(clear_lianxu_space([modules_en]))
        driver.quit()
        return modules_en