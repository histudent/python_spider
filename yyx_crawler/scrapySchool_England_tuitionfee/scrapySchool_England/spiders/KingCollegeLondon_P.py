import scrapy
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getStartDate import getStartDate


class KingsCollegeLondon_PSpider(scrapy.Spider):
    name = "KingsCollegeLondon_P"
    start_urls = ["https://www.kcl.ac.uk/study/subject-areas/index.aspx"]

    def parse(self, response):
        # 获得研究领域链接
        subject_area_links = response.xpath("//html//tr/td/p[1]/a/@href").extract()
        # print(len(subject_area_links))
        subject_area_links = list(set(subject_area_links))
        # print(len(subject_area_links))
        for sub in subject_area_links:
            url = "https://www.kcl.ac.uk" + sub
            # print(url, "==========================")
            yield scrapy.Request(url, callback=self.parse_url)

    def parse_url(self, response):
        # 筛选研究生的链接
        links = response.xpath("//div[@id='main']/div[@class='contentpage-main-content']/div[@class='wrapper']/table/tbody/tr/td//a/@href").extract()
        # print(links)
        alllinks = []
        for link in links:
            strurl = re.findall(r"/study/postgraduate/taught-courses/.*", link)
            alllinks.append(''.join(strurl))
        # print(response.url)
        while '' in alllinks:
            alllinks.remove('')

#         alllinks = ["https://www.kcl.ac.uk/study/postgraduate/taught-courses/web-intelligence-msc.aspx",
# "https://www.kcl.ac.uk/study/postgraduate/taught-courses/urban-informatics-msc.aspx",
# "https://www.kcl.ac.uk/study/postgraduate/taught-courses/strategic-entrepreneurship-and-innovation-msc.aspx",
# "https://www.kcl.ac.uk/study/postgraduate/taught-courses/religion-ma.aspx",
# "https://www.kcl.ac.uk/study/postgraduate/taught-courses/digital-marketing-msc.aspx", ]
#         alllinks = ['https://www.kcl.ac.uk/study/postgraduate/taught-courses/global-affairs-msc.aspx']
        for link in alllinks:
            url = "https://www.kcl.ac.uk" + link
            # url = link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.kcl.ac.uk/"
        item['university'] = "King's College London"
        item['url'] = response.url
        # 授课方式
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        item['location'] = "Strand, London. WC2R 2LS, United Kingdom"
        print("===============================")
        print(response.url)
        try:
            # //div[@id='container']/div[@class='hero clearfix']/div[@class='wrapper']/div[@class='inner']/h1
            # 专业、学位类型
            programmeDegree = response.xpath("//div[@id='container']/div[@class='hero clearfix']/div[@class='wrapper']/div[@class='inner']/h1//text()").extract()
            clear_space(programmeDegree)
            programmeDegreeStr = ''.join(programmeDegree).strip()
            print(programmeDegreeStr)
            # degree_type = list(re.findall(r"(\s\w+)$|(\s\w+\s\(.*\))$|(\s\w+/\w+)$|(\s\w+/\w+/\w+)$", programmeDegreeStr)[0])
            degree_type = re.findall(r"(\w+,[\s\w]+,[\s\w]+)$|(\w+/[\w\s]+/[\w\s]+)$|(\s\w+,[\s\w]+)$|(\s\w+/\w+/[\s\w]+)$|(\s\w+/[\w\s]+)$|(PG\sDip)$|(PG\sCert)$|(\s\w+\s\(.*\))$|(\s\w+)$", programmeDegreeStr)
            if len(degree_type) > 0:
                degree_type = list(degree_type[0])
                print("degree_type = ", degree_type)
                item['degree_name'] = ''.join(degree_type).strip()
            # while '' in degree_type:
            #     degree_type.remove('')
            # # print("degree_type = ", degree_type)
            # item['degree_name'] = ''.join(degree_type).strip()
                programme = programmeDegreeStr.replace(item['degree_name'], '').strip()
                item['programme_en'] = programme
            else:
                item['programme_en'] = programmeDegreeStr
            if item['degree_name'] == "":
                print("degree_name 为空")
            print("item['degree_name'] = ", item['degree_name'])
            print("item['programme_en'] = ", item['programme_en'])

            # //div[@id='tabs-key-info']/div[@class='tab tab-1 active-tab']/p[2]/span
            duration = response.xpath("//div[@id='tabs-key-info']/div[@class='tab tab-1']/p[2]/span//text()").extract()
            durationStr = ''.join(duration)
            # print(durationStr)
            # duration_re = re.findall(r"([a-zA-Z0-9]+\s)(year|month|week){1}", durationStr, re.I)
            duration_re = re.findall(r"([a-zA-Z0-9\.]+\s)(year|month|week|yr|yft){1}|([0-9\.]+)(yr|yft|\-month){1}",
                                     durationStr, re.I)
            # print(duration_re)
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
                    # print("d = ", d)
                    item['duration'] = int(d_dict.get(''.join(d[0]).strip()))
                if "y" in ''.join(duration_re[0]) or "Y" in ''.join(duration_re[0]):
                    item['duration_per'] = 1
                elif "m" in ''.join(duration_re[0]) or "M" in ''.join(duration_re[0]):
                    item['duration_per'] = 3
                elif "w" in ''.join(duration_re[0]) or "W" in ''.join(duration_re[0]):
                    item['duration_per'] = 4
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            # //div[@id='tabs-key-info']/div[@class='tab tab-1 active-tab']/p[3]/span
            teach_time = response.xpath("//div[@id='tabs-key-info']/div[@class='tab tab-1']/p[3]/span//text()").extract()
            # print(teach_time)
            if "Full" in ''.join(teach_time):
                item['teach_time'] = 'fulltime'
            # print("item['teach_time'] = ", item['teach_time'])

            # //div[@id='tabs-key-info']/div[@class='tab tab-2']
            includeDepartment = response.xpath("//div[@class='tab tab-2']//p[contains(text(), 'Faculty')]/span//text()").extract()
            if len(includeDepartment) == 0:
                includeDepartment = response.xpath(
                    "//div[@class='tab tab-2']//p[contains(text(), 'Department')]/span//text()").extract()
            clear_space(includeDepartment)
            # department = ""
            # if "Faculty" in includeDepartment:
            #     facultyIndex = includeDepartment.index("Faculty")
            #     department += includeDepartment[facultyIndex+2] + ", "
            # if "Department" in includeDepartment:
            #     departmentIndex = includeDepartment.index("Department")
            #     department += includeDepartment[departmentIndex+1]
            item['department'] = ''.join(includeDepartment).strip()
            # if item['department'] == "":
            #     print("department 为空")
            # else:
            #     print("item['department'] = ", item['department'])

            # //div[@id='coursepage-overview']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate']
            overview = response.xpath("//div[@id='coursepage-overview']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en'] = ", item['overview_en'])

            # //div[@id='coursepage-course-detail']/div[@class='wrapper clearfix']/div
            # modules = response.xpath("//h3[contains(text(),'Course format and assessment')]/preceding-sibling::*").extract()
            modules = response.xpath(
                "//div[@id='coursepage-course-detail']/div[@class='wrapper clearfix']/div[@class='inner right lop-to-measure']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # if item['modules_en'] == "":
            #     print("modules_en 为空")
            # else:
            #     print("item['modules_en'] = ", item['modules_en'])

            assessment_en = response.xpath(
                "//b[contains(text(),'Teaching')]/preceding-sibling::*[1]/following-sibling::*[position()<5]|"
                "//h3[contains(text(),'Teaching')]/preceding-sibling::*[1]/following-sibling::*|"
                "//b[contains(text(),'Teaching')]/../preceding-sibling::*[1]/following-sibling::*[position()<12]|"
                "//h3[contains(text(),'Course format and assessment')]/following-sibling::*").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # if item['assessment_en'] == "":
                # print("assessment为空")
            # else:
                # print("item['assessment_en'] = ", item['assessment_en'])

            # //div[@id='coursepage-fees-and-funding']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off']/ul[1]/li[2]
            tuition_fee = response.xpath("//div[@id='coursepage-fees-and-funding']/div[@class='wrapper clearfix']/div/ul[1]/li[2]//text()").extract()
            # print("tuition_fee = ", ''.join(tuition_fee))
            tuition_fee = response.xpath("//li[contains(text(),'Full time overseas fees:')]//text()").extract()
            tuition_fee_re = re.findall(r"£\d+,\d+|£\d+|\d+,\d+", ''.join(tuition_fee))
            # print(tuition_fee_re)
            if len(tuition_fee_re) >= 1:
                item['tuition_fee_pre'] = "£"
                item['tuition_fee'] = int(tuition_fee_re[0].replace("£", "").replace(",", "").strip())
            # print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])
            # print("item['tuition_fee'] = ", item['tuition_fee'])

            # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']
            entry_requirements = response.xpath("//div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[1]//text()").extract()
            item['rntry_requirements'] =clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements'] = ", item['rntry_requirements'])

            item['require_chinese_en'] = """<p><b>Postgraduate taught courses</b></p>
<p>A four year Bachelor's degree from a recognised university&nbsp;will be considered for&nbsp;programmes requiring a UK Bachelor (Honours) degree at 2:1.&nbsp;</p>
<p>Grade requirements for each course will vary. However, as an approximate guideline our requirements are in the region of:</p>
<table>
<tbody>
<tr><th><b>UK requirement </b></th><th><b>Chinese Universities considered Prestigious (Project 211)</b></th><th><b>Other recognised Chinese universities</b></th></tr>
<tr>
<td>
<p>First Class Bachelor (Honours) degree</p>
</td>
<td>
<p>Average of 88%</p>
</td>
<td>
<p>Average of 90%</p>
</td>
</tr>
<tr>
<td>
<p>High 2:1 Class Bachelor (Honours) degree</p>
</td>
<td>
<p>Average of 85%</p>
</td>
<td>
<p>Average of 88%</p>
</td>
</tr>
<tr>
<td>
<p>&nbsp;2:1 Class Bachelor (Honours) degree</p>
</td>
<td>
<p>Average of 80%</p>
</td>
<td>
<p>Average of 85%</p>
</td>
</tr>
<tr>
<td>
<p>High 2:2 Class Bachelor (Honours) degree</p>
</td>
<td>
<p>Average of 77%&nbsp;</p>
</td>
<td>
<p>Average of 80%</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;If your degree is graded as a Grade Point Average, note that we will normally be looking for a minimum cumulative GPA of 3.3-3.5 on a 4.0 scale.</p>
<p><b>Important note:&nbsp;</b></p>
<ul>
<li>
<p>You will be a stronger candidate for admission if you have high grades and are attending a university considered prestigious (considered to be those considered prestigious by UK NARIC, or within the Project 211 list of institutions).</p>
</li>
<li>
<p>For our most competitive courses at postgraduate level (i.e. those within the King's Business School, the Dickson Poon School of Law, the department of Digital Humanities), please note that offers will usually only be made to applicants from universities considered prestigious.</p>
</li>
<li>
<p>For King's Business School offers will usually be made to applicants from universities considered prestigious and for non-prestigious universities, we generally only consider applicants with 90% or above.&nbsp;&nbsp;</p>
</li>
</ul>"""

            # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']
            IELTS = response.xpath("//th[contains(text(), 'English Language requirements')]/following-sibling::td[1]//text()").extract()
            clear_space(IELTS)
            # print(IELTS)
            item['ielts_desc'] = ''.join(IELTS).strip()
            item['toefl_desc'] = item['ielts_desc']
            # print("item['ielts_desc'] = ", item['ielts_desc'])

            if item['ielts_desc'] == "Band A":
                item["ielts"] = 7.5  # float
                item["ielts_l"] = 7.0  # float
                item["ielts_s"] = 7.0  # float
                item["ielts_r"] = 7.0  # float
                item["ielts_w"] = 7.0
                item["toefl"] = 100  # float
                item["toefl_l"] = 25  # float
                item["toefl_s"] = 25  # float
                item["toefl_r"] = 25  # float
                item["toefl_w"] = 27
            elif item['ielts_desc'] == "Band B":
                item["ielts"] = 7.0  # float
                item["ielts_l"] = 6.5  # float
                item["ielts_s"] = 6.5  # float
                item["ielts_r"] = 6.5  # float
                item["ielts_w"] = 6.5
                item["toefl"] = 100  # float
                item["toefl_l"] = 23  # float
                item["toefl_s"] = 23  # float
                item["toefl_r"] = 23  # float
                item["toefl_w"] = 25
            elif item['ielts_desc'] == "Band C":
                item["ielts"] = 7.0  # float
                item["ielts_l"] = 6.0  # float
                item["ielts_s"] = 6.0  # float
                item["ielts_r"] = 6.5  # float
                item["ielts_w"] = 6.5
                item["toefl"] = 100  # float
                item["toefl_l"] = 20  # float
                item["toefl_s"] = 20  # float
                item["toefl_r"] = 23  # float
                item["toefl_w"] = 25
            elif item['ielts_desc'] == "Band D":
                item["ielts"] = 6.5  # float
                item["ielts_l"] = 6.0  # float
                item["ielts_s"] = 6.0  # float
                item["ielts_r"] = 6.0  # float
                item["ielts_w"] = 6.0
                item["toefl"] = 92  # float
                item["toefl_l"] = 20  # float
                item["toefl_s"] = 20  # float
                item["toefl_r"] = 20  # float
                item["toefl_w"] = 23
            elif item['ielts_desc'] == "Band E":
                item["ielts"] = 6.0  # float
                item["ielts_l"] = 5.5  # float
                item["ielts_s"] = 5.5  # float
                item["ielts_r"] = 5.5  # float
                item["ielts_w"] = 5.5
                item["toefl"] = 80  # float
                item["toefl_l"] = 20  # float
                item["toefl_s"] = 20  # float
                item["toefl_r"] = 20  # float
                item["toefl_w"] = 20

            # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']/div[@class='requirements uk clearfix']/div[@class='copy'][2]/p[1]
            application_fee = response.xpath("//h3[contains(text(), 'Application procedure')]/following-sibling::div[1]//text()").extract()
            clear_space(application_fee)
            # print(''.join(application_fee))
            application_fee_re = re.findall(r"application\sfee.*£\d+", ''.join(application_fee))
            # print("apply_fee: ", ''.join(application_fee_re))
            af = ''.join(application_fee_re).replace("application fee of", "").replace("£", "").strip()
            if len(af) != 0:
                item['apply_fee'] = int(af)
                item['apply_pre'] = "£"
            # print("item['apply_fee'] = ", item['apply_fee'])

            # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']/div[@class='requirements uk clearfix']/div[@class='copy'][2]/p[1]
            application_documents = response.xpath("//h3[contains(text(), 'Personal statement and supporting information')]/following-sibling::div[1]").extract()
            item['apply_documents_en'] = remove_class(clear_lianxu_space(application_documents))
            # print("item['apply_documents_en'] = ", item['apply_documents_en'])

            # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']/div[@class='requirements uk clearfix']/div[@class='copy'][2]/p[1]
            deadline = response.xpath("//div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[1]/div[@class='requirements uk clearfix']/div[@class='copy'][4]//text()").extract()
            clear_space(deadline)
            print(deadline)
            deadline_str = ''.join(deadline).strip()
            item['deadline'] = getStartDate(deadline_str)
            # if "-000000" in item['deadline']:
            item['deadline'].replace("-000000", "").strip()
            print(len(item['deadline']))
            if len(item['deadline']) > 10:
                item['deadline'] = item['deadline'][:7]
            print("item['deadline'] = ", item['deadline'])

            # //div[@id='coursepage-career-prospect']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate']
            career = response.xpath("//div[@id='coursepage-career-prospect']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en'] = ", item['career_en'])

            apply_proces_en = response.xpath(
                "//h3[contains(text(),'Application procedure')]/preceding-sibling::*[1]/following-sibling::*[position()<3]").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(apply_proces_en))
            # print("item['apply_proces_en'] = ", item['apply_proces_en'])
            yield item
        except Exception as e:
            with open("scrapySchool_England/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

