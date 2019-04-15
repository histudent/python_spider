# -*- coding: utf-8 -*-
import scrapy
import re, json, requests
from scrapySchool_England.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from w3lib.html import remove_tags
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts
from lxml import etree
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.getDuration import getIntDuration


class TheUniversityOfSheffield_USpider(scrapy.Spider):
    name = "TheUniversityOfSheffield_P"
    start_urls = ["https://www.sheffield.ac.uk/postgraduate/taught/courses/all"]
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    def parse(self, response):
        links = response.xpath(
            "//div[@class='row']/div[@class='col-md-19 col-lg-22 no-gutter']/main[@class='main content']/p/a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))
        for link in links:
            # print(link, "-----")
            if "http" not in link:
                url = "https://www.sheffield.ac.uk" + link
            else:
                url = link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "The University of Sheffield"
        # item['country'] = 'England'
        # item['website'] = 'https://www.sheffield.ac.uk'
        item['url'] = response.url
        # 授课方式
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        item['location'] = "Western Bank, Sheffield, S10 2TN, UK"
        print("===========================")
        print(response.url)
        try:
            # 专业、学位类型
            programmeDegree_type = response.xpath(
                "//main[@class='main content']/h1//text()").extract()
            if len(programmeDegree_type) == 0:
                programmeDegree_type = response.xpath(
                    "//main[@class='main content']/h2[1]//text()").extract()
            programmeDegree_type = ''.join(programmeDegree_type)
            # print("programmeDegree_type: ", programmeDegree_type)
            degree_typeList = re.findall(r"^[A-Za-z/\(\)]*", programmeDegree_type)
            # print("degree_typeList: ", degree_typeList)
            programme = programmeDegree_type
            if len(degree_typeList) != 0:
                degree_type = ''.join(list(degree_typeList[0]))
                item['degree_name'] = degree_type
                programme = programmeDegree_type.split(item['degree_name'])
            print("item['degree_name']: ", item['degree_name'])
            item['programme_en'] = ''.join(programme).strip().replace("in ", "").strip()
            print("item['programme_en']: ", item['programme_en'])

            # 学院
            department = response.xpath(
                "//html//main[@class='main content']/p[1]//text()").extract()
            department = ''.join(department)
            clear_space_str(department)
            item['department'] = department.strip()
            # print("item['department']: ", item['department'])

            # start_date //a[@href='#tab00']
            start_date = response.xpath(
                "//table[@class='cms-tabs']/tbody/tr[last()]/th[1]//text()").extract()
            clear_space(start_date)
            # print("start_date: ", start_date)
            item['start_date'] = getStartDate(''.join(start_date)).replace("--20", "").strip()
            # print("item['start_date']: ", item['start_date'])

            # 专业描述
            overview = response.xpath("//div[@id='tab00']//div[@class='highlight neutral']|//h2[contains(text(),'Overview')]/..").extract()
            # print("overview: ", overview)
            if len(overview) == 0:
                overview = response.xpath("//div[@class='highlight neutral']").extract()
                # print("overview1: ", overview)
                if len(overview) == 0:
                    overview = response.xpath("//h3[contains(text(),'Core modules')]/preceding-sibling::*").extract()
                    # print("overview2: ", overview)
                    if len(overview) == 0:
                        overview = response.xpath("//h3[contains(text(),'Teaching')]/preceding-sibling::*").extract()
                        # print("overview3: ", overview)
                        if len(overview) == 0:
                            overview = response.xpath(
                                "//h3[contains(text(),'Course duration')]/preceding-sibling::*").extract()
                            # print("overview3: ", overview)
                            if len(overview) == 0:
                                overview = response.xpath(
                                    "//*[contains(text(), 'Course descriptio')]/preceding-sibling::*[1]/following-sibling::*[position()<4]").extract()
                                # print("overview4: ", overview)
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])

            # 课程长度
            durationContent = response.xpath(
                "//h3[contains(text(),'Course duration')]/following-sibling::p[1]//text() | //h3[contains(text(),'Course duration')]/following-sibling::ul/li[1]//text()").extract()
            clear_space(durationContent)
            # print(durationContent)
            if len(durationContent) != 0:
                duration = durationContent[0].strip()
                if "full" in duration:
                    item['teach_time'] = 'fulltime'
                elif "part" in duration or "Part" in duration:
                    item['teach_time'] = 'parttime'
                d_re = re.findall(r'\d+', duration)
                if len(d_re) != 0:
                    item['duration'] = d_re[0]
                if 'year' in duration:
                    item['duration_per'] = 1
                elif 'month' in duration:
                    item['duration_per'] = 3
            duration_list = getIntDuration(''.join(durationContent))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['teach_time']: ", item['teach_time'])
            # print("item['duration']: ", item['duration'])
            # print("item['duration_per']: ", item['duration_per'])

            # //div[@id='tab00']
            # modules   评估方式
            twoContent = response.xpath(
                "//main[@class='main content']//text()").extract()
            clear_space(twoContent)
            # print(twoContent)
            if "Core modules" in twoContent:
                modulesIndex = twoContent.index("Core modules")
                modules = ""
                if "Teaching and assessment" in twoContent:
                    modulesIndexEnd = twoContent.index("Teaching and assessment")
                    modules = twoContent[modulesIndex:modulesIndexEnd]
                elif "Teaching" in twoContent:
                    modulesIndexEnd = twoContent.index("Teaching")
                    modules = twoContent[modulesIndex:modulesIndexEnd]
                elif "Course duration" in twoContent:
                    modulesIndexEnd = twoContent.index("Course duration")
                    modules = twoContent[modulesIndex:modulesIndexEnd]
                item['modules_en'] = clear_lianxu_space(modules)
            if item['modules_en'] != "":
                item['modules_en'] = "<div>" + item['modules_en'] + "</div>"
            # print("item['modules_en']: ", item['modules_en'])

            if item['modules_en'] == "":
                modules_bu = response.xpath("//h2[contains(text(),'Programme structure')]/..|"
                                            "//h3[contains(text(),'odules')]|//h3[contains(text(),'odules')]/following-sibling::*[position()<5]|"
                                            "//h3[contains(text(),'Subjects')]|//h3[contains(text(),'Subjects')]/following-sibling::*[position()<5]|"
                                            "//h3[contains(text(),'odules')]|//h3[contains(text(),'odules')]/following-sibling::*[position()<5]|"
                                            "//h3[contains(text(),'Course content')]|//h3[contains(text(),'Course content')]/following-sibling::*[position()<5]|"
                                            "//h3[contains(text(),'odules')]|//h3[contains(text(),'odules')]/following-sibling::*[position()<5]|"
                                            "//h3[contains(text(),'Subjects')]|//h3[contains(text(),'Subjects')]/following-sibling::*[position()<5]|"
                                            "//h3[contains(text(),'odules')]|//h3[contains(text(),'odules')]/following-sibling::*[position()<5]|"
                                            "//h3[contains(text(),'semester')]|//h3[contains(text(),'semester')]/following-sibling::*[position()<6]|"
                                            "//h3[contains(text(),'Stage')]|//h3[contains(text(),'Stage')]/following-sibling::*[position()<4]|"
                                            "//h3[contains(text(),'Semester')]|//h3[contains(text(),'Semester')]/following-sibling::*[position()<6]").extract()
                item['modules_en'] = remove_class(clear_lianxu_space(modules_bu))
            if item['modules_en'] == "":
                print("***** modules_en")
            print("item['modules_en']: ", item['modules_en'])

            if "Teaching and assessment" in twoContent:
                teachingIndex = twoContent.index("Teaching and assessment")
                if "Course duration" in twoContent:
                    teachingIndexEnd = twoContent.index("Course duration")
                    teaching = twoContent[teachingIndex:teachingIndexEnd]
                    item['assessment_en'] = clear_lianxu_space(teaching)
                elif "Entry requirements" in twoContent:
                    teachingIndexEnd = twoContent.index("Entry requirements")
                    teaching = twoContent[teachingIndex:teachingIndexEnd]
                    item['assessment_en'] = clear_lianxu_space(teaching)
            elif "Teaching" in twoContent:
                teachingIndex = twoContent.index("Teaching")
                if "Course duration" in twoContent:
                    teachingIndexEnd = twoContent.index("Course duration")
                    teaching = twoContent[teachingIndex:teachingIndexEnd]
                    item['assessment_en'] = clear_lianxu_space(teaching)
            elif "Assessment" in twoContent:
                teachingIndex = twoContent.index("Assessment")
                if "Course duration" in twoContent:
                    teachingIndexEnd = twoContent.index("Course duration")
                    teaching = twoContent[teachingIndex:teachingIndexEnd]
                    item['assessment_en'] = clear_lianxu_space(teaching)
            if len(item['assessment_en']) != 0:
                item['assessment_en'] = "<div>" + item['assessment_en'] + "</div>"
            if len(item['assessment_en']) == 0:
                item['assessment_en'] = remove_class(clear_lianxu_space(response.xpath("//h2[contains(text(),'Assessment')]/..|"
                                                                                       "//h3[contains(text(),'How we will teach and assess you')]|//h3[contains(text(),'How we will teach and assess you')]/following-sibling::*[position()<3]|"
                                                                                       "//h3[contains(text(),'teaching and assessment')]|//h3[contains(text(),'teaching and assessment')]/following-sibling::*[position()<5]").extract()))
            print("item['assessment_en']: ", item['assessment_en'])

            entry_requirements = response.xpath(
                "//div[@class='highlight complement']//h4[contains(text(),'English language')]/preceding-sibling::*//text()|"
                "//div[@class='highlight complement']//h4[contains(text(),'English Language')]/preceding-sibling::*//text()").extract()
            if len(entry_requirements) == 0:
                entry_requirements = response.xpath("//h4[contains(text(),'English language')]/preceding-sibling::*[position()<3]//text()").extract()
                if len(entry_requirements) == 0:
                    entry_requirements = response.xpath(
                        "//*[contains(text(),'Entry')]/following-sibling::*[position()<4]//text()").extract()
            item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            ielts_desc = response.xpath(
                "//div[@class='highlight complement']//h4[contains(text(),'English language')]/following-sibling::p[1]//text()|"
                "//div[@class='highlight complement']//h4[contains(text(),'English Language')]/following-sibling::p[1]//text()").extract()
            if len(ielts_desc) == 0:
                ielts_desc = response.xpath("//h4[contains(text(),'English language')]/following-sibling::*[position()<3]//text()").extract()
                if len(ielts_desc) == 0:
                    ielts_desc = response.xpath(
                        "//p[contains(text(),'IELTS')]//text()").extract()
            clear_space(ielts_desc)
            if len(ielts_desc) > 0:
                item['ielts_desc'] = ''.join(ielts_desc[0])
            # print("item['ielts_desc']: ", item['ielts_desc'])

            ieltDict = get_ielts(item['ielts_desc'])
            item['ielts'] = ieltDict.get('IELTS')
            item["ielts_l"] = ieltDict.get('IELTS_L')  # float
            item["ielts_s"] = ieltDict.get('IELTS_S')  # float
            item["ielts_r"] = ieltDict.get('IELTS_R')  # float
            item["ielts_w"] = ieltDict.get('IELTS_W')
            # print("ielts = %s  ielts_l = %s  ielts_s = %s  ielts_r = %s  ielts_w = %s"%(
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            item['apply_proces_en'] = """<h1>Applying</h1>
    <p>You can apply for postgraduate study using our Postgraduate Online Application Form. It is a quick and easy process. Use the following link to enter:</p>
    <p>Postgraduate online application form</p>
    <p>The form has comprehensive instructions about how to complete it and pop-up help is available on each page.</p>
    <table>
    <tbody>
    <tr>
    <td>
    <h4>MArch Applications</h4>
    <p>Direct-entry applicants to Part 2 of the  RIBA-accredited MArch Architecture (undergraduate masters course) should  apply using the form available on the School of Architecture's webpages:</p>
    <p>Applying for MArch courses (RIBA Part 2)</p>
    </td>
    </tr>
    </tbody>
    </table>
    <h3>Completing your application</h3>
    <p>The form is divided into two parts. Part 1 is for personal information, including English language ability, and previous education and employment. You have to complete all of the mandatory fields in this part (marked with a *) before you can go on to Part 2. Part 2 is where you select the course or courses you want to apply for. You can apply for a total of three different postgraduate courses.</p>
    <h3>Supporting Documents</h3>
    <p>You will need to include certain documents to support your application, for example evidence of your previous qualifications and a personal statement. You can supply these simply by uploading them to the relevant sections of your online application.</p>
    <p>You can find more information about the supporting documents you will need, and how to supply them, on our Supporting Documents webpage:</p>
    <p>Supporting documents</p>
    <h3>Submitting your application</h3>
    <p>Your application will only be submitted to us when you click the "Submit Application" button. If you have forgotten to fill in any sections, you will be prompted to go back and complete them at this stage. When you have successfully submitted the completed form we will confirm this on-screen. You will also then be sent an email confirmation.</p>
    <p>If you want to apply for more than one course, you do not need to submit them all at the same time. Each course choice has its own "Submit Application" button.</p>
    <p>If you have any problems completing your online application, please contact us:</p>
    <p>Problems using the Postgraduate Online Application Form</p>
    <h3>After you've applied</h3>
    <p>When we have created your applicant record, we will send you a second email to confirm this. This email will include your applicant and choice numbers, as well as information about what happens next.</p>
    <p>You can find more information about what happens after you submit your application, and about preparing to study at the University of Sheffield, on the After You Apply webpage:</p>
    <p>After you apply</p>
    <p>If you have any questions about the application process or about studying at the University,  please contact us.</p>"""
            item['require_chinese_en'] = """<div>Postgraduate Taught Programmes e.g. MA, MSc
    New! Mandarin web pages for postgraduate applicants
    Find out more about how to apply in Mandarin using our new web pages from Admissions, which give you guidelines about how to apply to our postgraduate taught courses.
    We have over 200 postgraduate taught courses - if you are considering further study, there's a very good chance we'll have the course to meet your needs.
    Search for a postgraduate course
    Chinese University Degree Holders
    Holders of a good bachelor degree from a recognised Chinese university will be considered for direct entry to postgraduate diploma or masters programmes.
    For Entry to MBA
    Holders of a good bachelor degree from a recognised Chinese university and at least 3 years´ post-graduation work experience will be considered for direct entry to the MBA. Applicants must be at least 25 years old by the time the programme starts.
    For further information on the MBA programme
    For Entry to Postgraduate Research Programmes e.g. MPhil, PhD, PhD with Integrated Masters
    With around 2,000 postgraduate research students from over 100 different countries, Sheffield is one of the foremost centres for research training in the UK.
    Search for a research area
    Chinese Masters Degree Holders
    Holders of a good bachelor degree and a good masters degree from a recognised Chinese university will be considered for direct admission to postgraduate research programmes.
    If you are in any doubt about whether you are eligible to study at Sheffield, please contact the China Team.</div>"""

            tuition_fee_str = re.findall(r'course=.+"', response.text)
            tuition_fee_str = ''.join(tuition_fee_str).replace("course=", '').replace('"', '')
            # print("tuition_fee_str: ", tuition_fee_str)
            tuition_fee_url = "https://ssd.dept.shef.ac.uk/fees/pgt/api/lookup.php?year=2018&status=Overseas&course=" + tuition_fee_str
            # print("tuition_fee_url: ", tuition_fee_url)
            r = requests.get(tuition_fee_url, headers=self.headers)
            # print(r.text)
            tuition_fee = re.findall(r"&pound;\d+", r.text)
            # print(tuition_fee, "*******")
            if len(tuition_fee) != 0:
                item['tuition_fee'] = int(''.join(tuition_fee).replace('&pound;', ''))
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee']: ", item['tuition_fee'])

            career = response.xpath("//h3[contains(text(),'Careers')]|//h3[contains(text(),'Careers')]/following-sibling::*[position()<2]").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            print("item['career_en']: ", item['career_en'])
            yield item
        except Exception as e:
            with open("scrapySchool_England/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a',
                      encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

