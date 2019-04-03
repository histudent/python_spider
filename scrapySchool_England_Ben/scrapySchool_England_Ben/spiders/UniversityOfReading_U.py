import scrapy
import re
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space, clear_space_str
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime
import requests
from lxml import etree

class UniversityOfReading_USpider(scrapy.Spider):
    name = "UniversityOfReading_U"
    start_urls = ["https://www.reading.ac.uk/"]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3472.3 Safari/537.36"}

    def parse(self, response):
        links = response.xpath("//article[1]//ul[@class='accordion single-display']/li//ul//a/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))
        for link in links:
            url = "https://www.reading.ac.uk" + link
            yield scrapy.Request(url, callback=self.parse_url)

    def parse_url(self, response):
        department = response.xpath("//p[@class='paddingtop22 nopaddingbottom']/strong/a//text()|//h1[contains(text(), 'department')]/following-sibling::*//text()").extract()
        department = ''.join(department).replace("Visit the", "").replace("website", "").strip().strip('.').strip()

        links = response.xpath("//section/ul[@class='no-indent']/li/p[@class='pad-none']/a/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))
        for link in links:
            url = "http://www.reading.ac.uk" + link
            yield scrapy.Request(url, callback=self.parse_data, meta={"department": department})

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Reading"
        # item['country'] = 'England'
        # item['website'] = 'http://www.reading.ac.uk/'
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        item['location'] = "Whiteknights,PO Box 217,Reading, Berkshire,RG6 6AH"
        print("===========================")
        print(response.url)
        try:
            # 专业、学位类型、ucas_code
            programmeDegree_typeUcascode = response.xpath(
                "//span[@class='text-bg-standout text-nice-wrap']/text() | //h1[@id='heading']//text() | //h1[@class='hero-heading']//text() | //h1[@class='block-heading block-heading-l5 block-heading-b5 block-heading-md-l-reset cell-md-t0']//text()").extract()
            clear_space(programmeDegree_typeUcascode)
            programmeDegree_typeUcascode = ''.join(programmeDegree_typeUcascode).strip()
            # print("programmeDegree_typeUcascode: ", programmeDegree_typeUcascode)

            degree_type = re.findall(r"^\w+/\w+", programmeDegree_typeUcascode)
            if len(degree_type) == 0:
                degree_type = re.findall(r"^\w+", programmeDegree_typeUcascode)
            # print("degree_type: ", degree_type)
            item['degree_name'] = ''.join(degree_type)
            print("item['degree_name']: ", item['degree_name'])

            ucascode = re.findall(r"\w{4}$", programmeDegree_typeUcascode)
            item['ucascode'] = ''.join(ucascode).strip()
            # print("item['ucascode']: ", item['ucascode'])

            programme = programmeDegree_typeUcascode.replace(item['degree_name'], '').replace(item['ucascode'], "").strip()
            item['programme_en'] = programme.title()
            print("item['programme_en']: ", item['programme_en'])

            # duration
            durationMode = response.xpath(
                "//h2[@class='row-margin-small text-weight-medium text-size-25']/text() | //strong[contains(text(),'Duration')]/../text() | //h3[contains(text(),'Programme length:')]/following-sibling::p[1]//text()").extract()
            clear_space(durationMode)
            # print("durationMode: ", durationMode)
            durationMode = ''.join(durationMode)
            duration_list = getIntDuration(''.join(durationMode))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration']: ", item['duration'])
            # print("item['duration_per']: ", item['duration_per'])

            # start_date = response.xpath("//p[@class='headline'][contains(text(), 'Start date')]//text()").extract()
            # # print(start_date)
            # item['start_date'] = getStartDate(''.join(start_date))
            # # print("item['start_date']: ", item['start_date'])

            overview2 = response.xpath(
                "//div[@class='m-bg-white m-pad-around m-pull-left-normal m-pull-up']//div[@class='theme-editor'] | //div[@id='top-courseOverview'] | //html//div[@id='top-programmeOverview']/h2[1]/following-sibling::div[1] | //div[@id='tc1']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview2))
            # if item['overview_en'] == "":
            #     print("***overview_en")
            # print("item['overview_en']: ", item['overview_en'])

            # department
            item['department'] = response.meta['department']
            # print("item['department']: ", item['department'])

            if item['department'] == "":
                department = response.xpath("//aside[contains(@class,'pane base4 m-margin-bottom')]//div[contains(@class,'row-small')]//p[contains(text(), 'School')]/following-sibling::*//text()").extract()
                clear_space(department)
                item['department'] = ''.join(department).strip()
                item['department'] = item['department'].replace("How to apply", "").replace("Visit the", "").replace("website", "").strip().strip('.').strip()
                # print("item['department']1: ", item['department'])
            # if item['department'] == "":
            #     print("***department")

            # //h2[@id='Panel1Trigger']/../..
            entry_requirements = response.xpath(
                "//span[contains(text(),'entry requirements')]/../../..").extract()
            entry = ''.join(entry_requirements).strip()
            item['apply_desc_en'] = remove_class(clear_lianxu_space(entry_requirements))
            # if item['apply_desc_en'] == "":
            #     print("apply_desc_en 为空")
            # print("item['apply_desc_en']: ", item['apply_desc_en'])

            alevel = response.xpath(
                "//h4[contains(text(),'Typical')]/following-sibling::*[1]//text()|//h4[contains(text(),'A level')]/following-sibling::*[1]//text()").extract()
            item['alevel'] = ''.join(alevel).strip()
            # if item['alevel'] == "":
            #     print("alevel 为空")
            # print("item['alevel']: ", item['alevel'])

            ib = response.xpath(
                "//h4[contains(text(),'International Baccalaureate')]/following-sibling::*[1]//text()").extract()
            item['ib'] = ''.join(ib).strip()
            # if item['ib'] == "":
            #     print("ib 为空")
            # print("item['ib']: ", item['ib'])

            ielts = re.findall(r"IELT.{1,100}", entry)
            ielts = response.xpath(
                "//*[contains(text(),'IELT')]//text()").extract()
            if ''.join(ielts).strip() == "IELTS":
                ielts = response.xpath(
                    "//*[contains(text(),'IELT')]/following-sibling::*[1]//text()").extract()
            clear_space(ielts)
            item['ielts_desc'] = ''.join(ielts).strip()
            # if item['ielts_desc'] == "":
            #     print("ielts_desc 为空")
            # print("item['ielts_desc']: ", item['ielts_desc'])
            ieltsDict = get_ielts(item['ielts_desc'])
            item['ielts'] = ieltsDict.get("IELTS")
            item['ielts_l'] = ieltsDict.get("IELTS_L")
            item['ielts_s'] = ieltsDict.get("IELTS_S")
            item['ielts_r'] = ieltsDict.get("IELTS_R")
            item['ielts_w'] = ieltsDict.get("IELTS_W")
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            # toefl = re.findall(r"TOEFL[\s\(\)\w:\.]{1,300}", entry)
            # if item['toefl_desc'] == "":
            #     item['toefl_desc'] = ''.join(toefl)
            # print("item['toefl_desc']: ", item['toefl_desc'])
            # toeflDict = get_toefl(item['toefl_desc'])
            # item['toefl'] = toeflDict.get("TOEFL")
            # item['toefl_l'] = toeflDict.get("TOEFL_L")
            # item['toefl_s'] = toeflDict.get("TOEFL_S")
            # item['toefl_r'] = toeflDict.get("TOEFL_R")
            # item['toefl_w'] = toeflDict.get("TOEFL_W")
            # # print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
            #         item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

            modules = response.xpath(
                "//h2[@id='Panel2Trigger']/../..|//div[@id='bottom-courseContent']/..|//div[@id='page_content_wrap']/following-sibling::div[position()<3]|//strong[contains(text(),'Programme structure')]/../following-sibling::*").extract()
            if len(modules) == 0:
                modules = response.xpath(
                    "//h4[contains(text(),'Programme structure and content')]/preceding-sibling::*[1]/following-sibling::*[position()<11]").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])

            # //h2[@id='Panel1Trigger']/../..
            career = response.xpath(
                "//h2[@id='Panel4Trigger']/../following-sibling::div[1]|//div[@id='bottom-careers']/..|//div[@id='careers']|//h3[contains(text(),'Careers')]/..").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            # //h3[@class='row-margin-small text-weight-medium'][contains(text(),'How much will it cost?')]/following-sibling::p[2]
            tuition_fee = response.xpath(
                "//p[contains(text(),'New international students')]//text()").extract()
            clear_space(tuition_fee)
            # print("tuition_fee: ", tuition_fee)
            tuition_fee_re = re.findall(r"£\d+,\d+|£\d+", ''.join(tuition_fee))
            if len(tuition_fee_re) > 0:
                item['tuition_fee'] = int(''.join(tuition_fee_re).replace("£", "").replace(",", "").strip())

            if item['tuition_fee'] == 0:
                item[tuition_fee] = None
            else:
                item['tuition_fee_pre'] = "£"
            # if item['tuition_fee'] is None:
            #     print("tuition_fee 为空")
            # print("item['tuition_fee']: ", item['tuition_fee'])
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            # //div[@id='top-howWeTeachYou']
            assessment_en = response.xpath(
                "//div[@id='top-howWeTeachYou']").extract()
            item['assessment_en'] =remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<div class="row row-margin-small row-margin-title-10">

                        <h1 class="text-transform-uppercase text-size-30 m-text-size-25 text-weight-medium display-inline text-bg-standout text-nice-wrap">
                            <span class="text-bg-standout">How to apply for undergraduate courses</span>
                        </h1>

                    </div>
                                    <div class="theme-editor theme-editor-break-word">
                        You can apply online for all of our courses via the national admissions service, <a href="http://www.ucas.com">UCAS</a>. You can choose to apply for up to five courses in total, including more than one course at the same institution. <br />
<h4>When to apply&nbsp;</h4>
<p>UK or EU students: You should aim to apply via UCAS between 1 September and 15 January for admission in September 2018. If you have missed the 15 January deadline, there is still the opportunity to apply (via UCAS), and we are happy to consider late applications until 30 June 2018 (all applications received after 30 June are entered into Clearing). Please be aware that some of our courses may be full after the UCAS deadline, so we do recommend early applications where possible.</p>
<p>
International students: You should aim to apply via UCAS between 1 September 2017 and 15 January 2018 for admission in September 2018, though applying before 15 January is encouraged in order to ensure you have time to prepare for studying in the UK. However, if you have missed the 15 January deadline, you are still welcome to apply (via UCAS), and we are happy to consider late applications until 30 June 2018 (all applications received after 30 June are entered into Clearing). Please be aware that some of our courses may be full after the UCAS deadline, so we do recommend early applications where possible.</p>
<h4>UCAS code</h4>
<p>Our UCAS code is R12. The University does not have a campus code.&nbsp;</p>
<h4>UCAS costs</h4>
<p>There is a small charge made by UCAS for applying to university. The application fee is &pound;13 if you&rsquo;re applying to just one course, or &pound;24 for multiple courses and for late applications sent after 30 June.</p>
<h4>Entry requirements</h4>
<p>Please read our <a href="/ready-to-study/study/how-to-apply/entry-requirements-ug.aspx">entry requirements page</a> for more information on accepted qualifications.</p>
<h4>English language requirements</h4>
<p>If English is not your first language, you can find out more information on our <a href="/ready-to-study/international-and-eu/english-language-requirements.aspx">English language requirements</a> page.</p>
                    </div>
                                    <div class="row-large paddingtop-small pad-sides border-top-light">
                        <div class="visuallyhidden" id="show-more-094422b2-b9da-4602-9594-80e05dba925c" aria-hidden="true">
                            <div class="theme-editor">
                                <h4>The application process&nbsp;
</h4>
<p>Once UCAS receives your application, it sends it to our Admissions Office, who assess it and decide whether to offer you a place. The way we assess your application will differ from course to course, but we will use the information supplied in your application form including your personal statement, predicted and achieved grades and the reference supplied by your school or college.&nbsp;</p>
<p>We carefully consider every application so please don’t worry if you don’t hear back from us straight away. We aim to make a decision on all applications within four weeks, and you will be able to track the progress of your application on <a href="https://www.ucas.com/ucas/undergraduate/login">UCAS Track</a>.&nbsp;</p>
<p>We will email you with the outcome of your application and confirm this with UCAS so that you can see the decision online using UCAS Track. If we offer you a place, we will explain any conditions attached to that offer (for example, the need to achieve certain grades in your examinations).&nbsp;</p>
<h4>Interviews</h4>
<p> For some courses, we invite prospective students for an interview before making an offer. These are:&nbsp;</p>
<ul><li>Accounting and Business (assessment centre run in conjunction with PwC)&nbsp;</li>
    <li>Archaeology&nbsp;</li>
    <li>Art</li>
    <li>Chemistry&nbsp;</li>
    <li>Film, Theatre &amp; Television&nbsp;</li>
    <li>Food and Nutritional Sciences&nbsp;</li>
    <li>Graphic Communication&nbsp;</li>
    <li>Pharmacy&nbsp;</li>
    <li>Primary Education&nbsp;</li>
    <li>Psychology (MSci courses)&nbsp;</li>
    <li>Meteorology and Climate (MMet course)&nbsp;</li>
    <li>Theatre Arts, Education and Deaf Studies (TAEDS)&nbsp;</li>
</ul>
<h4>Visit Days</h4>
<p> If you are offered a place to study at the University of Reading without an interview, we will invite you to attend a Visit Day in your department of choice. Visit Days take place between November and March and will usually include a tour of our campus and facilities, a visit to a hall of residence, and the chance to meet academic staff and current students.&nbsp;</p>
<h4>Choosing offers&nbsp;</h4>
<p>Once you have heard from all of the universities that you applied to, UCAS will ask you which offer you want to accept. Most people choose two: one as your ‘firm’ or first choice, the other as your ‘insurance’ or second choice. If you meet the conditions of your offer, you will automatically be accepted onto your firm choice course.&nbsp;</p>
<h4>Confirmation of your place&nbsp;</h4>
<p>Most offers are conditional on exam results. If you meet the conditions set out in our offer, your place is assured and you will see this on <a href="https://www.ucas.com/ucas/undergraduate/login">UCAS Track</a> . If you do not meet the conditions set out in your offer, you may still be able to get on the course. We will let you know as soon as possible after we have received your results.&nbsp;</p>
<h4>Gap year/deferred entry&nbsp;</h4>
<p>We welcome deferred entry applications. You need to apply at the same time as if you were planning to go straight to university, but you should state in your UCAS application that you wish to be considered for deferred admission.</p>
                            </div></div></div>"""]))
            print("item['apply_proces_en']: ", item['apply_proces_en'])

            item['interview_desc_en'] = remove_class(clear_lianxu_space(["""<h4>Interviews</h4>
<p> For some courses, we invite prospective students for an interview before making an offer. These are:&nbsp;</p>
<ul><li>Accounting and Business (assessment centre run in conjunction with PwC)&nbsp;</li>
    <li>Archaeology&nbsp;</li>
    <li>Art</li>
    <li>Chemistry&nbsp;</li>
    <li>Film, Theatre &amp; Television&nbsp;</li>
    <li>Food and Nutritional Sciences&nbsp;</li>
    <li>Graphic Communication&nbsp;</li>
    <li>Pharmacy&nbsp;</li>
    <li>Primary Education&nbsp;</li>
    <li>Psychology (MSci courses)&nbsp;</li>
    <li>Meteorology and Climate (MMet course)&nbsp;</li>
    <li>Theatre Arts, Education and Deaf Studies (TAEDS)&nbsp;</li>
</ul>"""]))
            print("item['interview_desc_en']: ", item['interview_desc_en'])

            item["require_chinese_en"] = remove_class(clear_lianxu_space(["""<h2 class="trigger">Entry requirements</h2>
<table summary="A table outlining the basic entry requirements for courses at the University of Reading based on the qualifications offered in your country">
<tbody>
<tr><!-- HEADINGS-->
<td class="top-head"><strong>Your highest qualification</strong></td>
<td class="top-head"><strong>Likely entry level</strong></td></tr>
<tr><!-- FIRST ROW -->
<td>
<p><!-- EG FIRST ROW FIRST COLUMN INFO -->High School year 2 (Year 11) with leaving certificate: GPA 85%<br/>High School year 3 (Year 12) with graduation certificate: GPA 80%</p></td>
<td><a href="http://www.reading.ac.uk/foundation" name="ifp" >International Foundation Programme</a> </td></tr>
<tr class="even"><!-- SECOND ROW -->
<td>Gao Kao (Chinese University Entrance Exam) 80%</td>
<td><a href="http://www.reading.ac.uk/foundation" name="ifp" >International Foundation Programme</a> </td></tr>
<tr><!-- THIRD ROW -->
<td>Gau Cau (Chinese University Entrance Exam) combined with a successfully completed appropriate foundation/bridging programme. (Visit our <a href="http://www.reading.ac.uk/foundation" name="ifp" >International Foundation Programme</a>) </td>
<td>Undergraduate Degree (Bachelors Degree) </td></tr>
<tr class="even"><!-- FOURTH ROW -->
<td>International Baccalaureate (IB) Diploma </td>
<td>Undergraduate Degree (Bachelors Degree) </td></tr>
<tr><!-- FIFTH ROW -->
<td>British/International A Levels </td>
<td>Undergraduate Degree (Bachelors Degree) </td></tr>
<tr class="even"><!-- SIXTH ROW -->
<td>Chinese-medium A Levels in Mathematics and Sciences (Cambridge Examinations Board) </td>
<td>Undergraduate Degree (Bachelors Degree) in a relevant subject </td></tr>
<tr>
<td>Ameson: High school results of 85% if 11 years completed, 80% if 12 years (with similar grades in relevant subjects), AST Maths: 165 and AST English: 150</td>
<td>Undergraduate Degree (Bachelors Degree)</td></tr>
<tr class="even"><!-- EIGHTH ROW -->
<td>Other international qualifications such as Australian HSC, US SAT or AP Certificates</td>
<td>Undergraduate Degree (Bachelors Degree) </td></tr>
<tr><!-- NINTH ROW -->
<td>Successfully completed first year of a Chinese University degree </td>
<td>Undergraduate Degree (Bachelors Degree) </td></tr>
<tr class="even"><!-- TENTH ROW -->
<td>4-year Bachelor degree </td>
<td>Taught Postgraduate (Masters and Doctoral Degree) </td></tr>
<tr>
<td>&nbsp;Masters degree study </td>
<td>&nbsp;Research Postgraduate (Doctoral Degree) </td></tr></tbody></table>"""]))
            print("item['require_chinese_en']: ", item['require_chinese_en'])
            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a+',
                      encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

