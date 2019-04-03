import scrapy
import re
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space, clear_space_str
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.getIELTS import get_ielts
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime
import requests
from lxml import etree

class UniversityOfCambridge_USpider(scrapy.Spider):
    name = "UniversityOfCambridge_U"
    start_urls = ["https://www.undergraduate.study.cam.ac.uk/courses"]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3472.3 Safari/537.36"}

    def parse(self, response):
        links = response.xpath("//div[@class='attachment attachment-after']/div/div[@class='view-content']/div/div/h4/a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))

        for link in links:
            url = "https://www.undergraduate.study.cam.ac.uk" + link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Cambridge"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        item['location'] = 'Fitzwilliam House, 32 Trumpington Street, Cambridge, CB2 1QY'
        print("===============================")
        print(response.url)
        try:
            # 专业、学位类型
            programme = response.xpath("//h1[@class='campl-sub-title']//text()").extract()
            clear_space(programme)
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en'] = ", item['programme_en'])

            ucascode = response.xpath(
                "//div[contains(text(),'UCAS Code')]/following-sibling::div[1]//text()").extract()
            clear_space(ucascode)
            item['ucascode'] = ''.join(ucascode).strip()
            print("item['ucascode']: ", item['ucascode'])

            duration_degree_name = response.xpath("//div[contains(text(),'Course Duration')]/following-sibling::div[1]//text()").extract()
            clear_space(duration_degree_name)
            print("duration_degree_name: ", duration_degree_name)

            if len(duration_degree_name) > 0:
                if "-" in ''.join(duration_degree_name).strip():
                    duration_degree_name_list = ''.join(duration_degree_name).split("-")
                    item['degree_name'] = duration_degree_name_list[-1].strip()
                elif "–" in ''.join(duration_degree_name).strip():
                    duration_degree_name_list = ''.join(duration_degree_name).split("–")
                    item['degree_name'] = duration_degree_name_list[-1].strip()

                duration_list = getIntDuration(''.join(duration_degree_name))
                if len(duration_list) == 2:
                    item['duration'] = duration_list[0]
                    item['duration_per'] = duration_list[-1]
            print("item['degree_name'] = ", item['degree_name'])
            print("item['duration'] = ", item['duration'])
            print("item['duration_per'] = ", item['duration_per'])

            # //div[contains(text(),'Colleges')]/following-sibling::div[1]
            department = response.xpath(
                "//div[contains(@class,'field-items')]/div[1]/div[1]/li[1]/span[1]//a//text()").extract()
            clear_space(department)
            if len(department)>0:
                item['department'] = ''.join(department[0]).strip()
            if item['department'] == "Course website":
                item['department'] == ""
            if "Faculty of Modern and Medieval Languages" in item['department']:
                item['department'] = "Faculty of Modern and Medieval Languages"
            print("item['department'] = ", item['department'])

            # //html//div[@class='content']/div[1]/div  专业描述
            overview = response.xpath("//fieldset[@id='overview']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en'] = ", item['overview_en'])

            modules_en = response.xpath("//fieldset[@id='course-outline']|//table[contains(@class,'campl-table-bordered campl-table campl-vertical-stacking-table')]").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules_en))
            # print("item['modules_en'] = ", item['modules_en'])

            teaching_assessment= response.xpath("//a[@id='assessment']/../preceding-sibling::*[1]/following-sibling::*[position()<5]|"
                                                "//fieldset[@id='entry-requirements']//h2[contains(text(),'assessment')]/preceding-sibling::*[1]/following-sibling::*[position()<8]").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(teaching_assessment))
            # print("item['assessment_en'] = ", item['assessment_en'])

            apply_desc_en = response.xpath("//fieldset[@id='entry-requirements']").extract()
            item['apply_desc_en'] = remove_class(clear_lianxu_space(apply_desc_en))
            # print("item['apply_desc_en'] = ", item['apply_desc_en'])

            entry_requirements = response.xpath("//h2[contains(text(),'Typical offers require')]/following-sibling::*[1]//text()").extract()
            clear_space(entry_requirements)
            # print("entry_requirements: ", entry_requirements)
            if "IB:" in entry_requirements:
                ibIndex = entry_requirements.index("IB:")
                item['alevel'] = ''.join(entry_requirements[:ibIndex]).strip()
                item['ib'] = ''.join(entry_requirements[ibIndex:]).strip()
            # print("item['alevel'] = ", item['alevel'])
            # print("item['ib'] = ", item['ib'])
            if item['alevel'] == "":
                al = response.xpath("//fieldset[@id='entry-requirements']//*[contains(text(),'A Level')]//text()").extract()
                clear_space(al)
                if len(al)>0:
                    item['alevel'] = al[0].strip()
                # print("item['alevel']2 = ", item['alevel'])

            career_en = response.xpath("//div[@class='fieldset-wrapper']//div[@class='field field-name-body field-type-text-with-summary field-label-hidden']//div[@class='field-item even']/h2[last()]//preceding-sibling::*[1]/following-sibling::*").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            print("item['career_en'] = ", item['career_en'])

            # https://www.undergraduate.study.cam.ac.uk/applying
            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<div class="field-item even"><p>If you want to apply to the University, you do so through UCAS. However, at Cambridge the process starts earlier to allow time for all of the application information to be gathered and considered. This section guides you through the process and explains what we’re looking for in prospective students and how we assess applications.</p>
<h1>1. Choose a course</h1>
<p>You’re going to be studying to a very high level for several years so make sure you <a href="https://www.undergraduate.study.cam.ac.uk/courses/">choose a course</a> you’re personally interested in and will really enjoy studying! Check, also, that you meet the <a href="https://www.undergraduate.study.cam.ac.uk/applying/entrance-requirements">entrance requirements</a> of the course you want to study.</p>
<h1>2. Choose a College</h1>
<p>Where would you like to live when you’re here? In your UCAS application, indicate if you have a preference <a href="https://www.undergraduate.study.cam.ac.uk/colleges">College</a> or if you’re <a href="https://www.undergraduate.study.cam.ac.uk/colleges/open-applications">making an open application</a>.</p>
<h1>3. Apply</h1>
<h3>UCAS application</h3>
<p>Submit your <a href="https://www.undergraduate.study.cam.ac.uk/applying/ucas-application">UCAS application</a> by <strong>15 October</strong> – our institution code is CAM C05.</p>
<p>Other application deadlines apply for those wishing to be interviewed in <a href="https://www.undergraduate.study.cam.ac.uk/international-students/overseas-interviews">overseas countries</a>, and for some <a href="https://www.undergraduate.study.cam.ac.uk/applying/mature-students-and-second-undergraduate-degrees/mature-student-applications">mature applicants</a>.</p>
<p>There's an additional application form if you're applying for the <a href="https://www.undergraduate.study.cam.ac.uk/courses/medicine-graduate-course">Graduate Course in Medicine</a>.</p>
<h3>Supplementary Application Questionnaire (SAQ)</h3>
<p>Shortly after submitting the UCAS application, you'll be asked (via email) to complete the <a href="https://www.undergraduate.study.cam.ac.uk/applying/saq">Supplementary Application Questionnaire (SAQ)</a> – a few extra questions requesting information not included in your UCAS application, which we find helpful. To make a valid application to the University of Cambridge, you must submit your SAQ by the deadline set. In the majority of cases this deadline will be 6.00pm (UK time) on 22 October 2018.</p>
<h3>Cambridge Online Preliminary Application (COPA)</h3>
<p>If you're living or attending school/college outside the EU and/or applying for an <a href="https://www.undergraduate.study.cam.ac.uk/finance/music-awards/organ-scholarships">Organ Scholarship</a>, you need to submit the <a href="https://www.undergraduate.study.cam.ac.uk/applying/copa">Cambridge Online Preliminary Application (COPA)</a>, and the deadline for submitting this may be earlier than 15 October (see the relevant page for information).</p>
<h3>Transcripts</h3>
<p>You may be required to submit an <a href="https://www.undergraduate.study.cam.ac.uk/applying/transcripts">academic transcript</a>.</p>
<h1>4. Written assessment</h1>
<p>Most applicants are required to take a <a href="https://www.undergraduate.study.cam.ac.uk/applying/admission-assessments">written admission assessment</a>, either pre-interview or at interview (if interviewed).</p>
<h1>5. Interview</h1>
<p>Everyone with a realistic chance of being offered a place is invited to attend an <a href="https://www.undergraduate.study.cam.ac.uk/applying/interviews">interview</a>. That’s around 75 per cent of applicants each year.</p>
<h1>6. Decision</h1>
<p>We’ll advise you of our <a href="https://www.undergraduate.study.cam.ac.uk/applying/decisions">decision</a> before the end of January.</p>
</div>"""]))
            item['deadline'] = '2018-10-15'
            # item["application_open_date"] = '2018-11-30'

            tuition_fee_dict = {"Anglo-Saxon, Norse, and Celtic": 20157,
"Archaeology": 20157,
"Asian and Middle Eastern Studies": 20157,
"Classics": 20157,
"Economics": 20157,
"Education": 20157,
"English": 20157,
"History": 20157,
"History of Art": 20157,
"History and Modern Languages": 20157,
"History and Politics": 20157,
"Human, Social, and Political Sciences": 20157,
"Land Economy": 20157,
"Law": 20157,
"Linguistics": 20157,
"Modern and Medieval Languages": 20157,
"Philosophy": 20157,
"Theology, Religion, and Philosophy of Religion": 20157,
"Mathematics": 22482,
"Architecture": 26376, "Geography": 26376, "Music": 26376,
"Chemical Engineering": 30678,
"Computer Science": 30678,
"Engineering": 30678,
"Management Studies (Part II course)": 30678,
"Manufacturing Engineering (Part II course)": 30678,
"Natural Sciences": 30678,
"Psychological and Behavioural Sciences": 30678,
"Veterinary Medicine": 52638,
"Medicine (Graduate Course)": 70131, "Medicine": 70131,}
            item['tuition_fee'] = tuition_fee_dict.get(item['programme_en'])
            if item['tuition_fee'] is not None:
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee'] = ", item['tuition_fee'])
            # print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])

            # https://www.undergraduate.study.cam.ac.uk/international-students/english-language-requirements
            item['ielts'] = '7.5'
            item['ielts_l'] = '7.0'
            item['ielts_s'] = '7.0'
            item['ielts_r'] = '7.0'
            item['ielts_w'] = '7.0'
            # print("item['IELTS'] = %sitem['IELTS_L'] = %sitem['IELTS_S'] = %sitem['IELTS_R'] = %sitem['IELTS_W'] = %s==" % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))
            item['toefl'] = '110'
            item['toefl_l'] = '25'
            item['toefl_s'] = '25'
            item['toefl_r'] = '25'
            item['toefl_w'] = '25'
            # print("item['toefl'] = %sitem['toefl_l'] = %sitem['toefl_s'] = %sitem['toefl_r'] = %sitem['toefl_w'] = %s==" % (
            #         item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<h2>Entry requirements</h2>
<p>The Gaokao is regarded as suitable preparation for Cambridge. The Gaokao scores of successful applicants will vary from province to province and year to year. As a guideline, successful applicants will usually have scores in the top 0.1% of those taking the Gaokao in their province. In addition to the total score, Cambridge Colleges will pay close attention to individual subject scores and scores in the Senior High School Examinations (Xueye Shuiping Kaoshi; previously the Huikao). The Xueye Shuiping Kaoshi alone are not regarded as suitable preparation for Cambridge.</p>
<p>Applicants studying for the Gaokao are encouraged to undertake additional study outside of their school qualifications. This might include, for example, relevant science Olympiads or College Board SAT I or II; or Advanced Placement Tests.</p>
<p>Gaokao offers are made on an individual basis, and we recommend that you <a href="https://www.undergraduate.study.cam.ac.uk/colleges/college-contacts">contact the College</a> to which you wish to apply for further advice and guidance.</p>"""]))

            # item['apply_fee'] = apply_fee_re1[0].replace("£", "").strip()
            # item["apply_pre"] = "£"
            # print("item['apply_fee'] = ", item['apply_fee'])
            # print("item['apply_pre'] = ", item['apply_pre'])

            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

