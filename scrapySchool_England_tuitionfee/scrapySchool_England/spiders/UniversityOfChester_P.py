# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getDuration import getIntDuration, getTeachTime
import json
import requests

class UniversityOfChester_PSpider(scrapy.Spider):
    name = "UniversityOfChester_P"
    start_urls = ["https://www1.chester.ac.uk/course_atoz/52"]

    def parse(self, response):
        links = response.xpath("//html//table/tbody/tr/td[3]/ul[1]/li/a[contains(text(), 'Full')]/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))

        # links = ["https://www1.chester.ac.uk/study/postgraduate/master-nursing/201810",
# "https://www1.chester.ac.uk/study/postgraduate/mathematics-enhancement-course/201810", ]
        for link in links:
            url = "https://www1.chester.ac.uk" + link
            # print(url)
            # url = link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "University of Chester"
        item['url'] = response.url
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        print("===========================")
        print(response.url)
        try:
            programme = response.xpath("//h1[@id='main-content']/text()").extract()
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en']: ", item['programme_en'])

            degree_type = response.xpath("//h1[@id='main-content']/div//text()").extract()
            item['degree_name'] = ''.join(degree_type).strip()
            print("item['degree_name']: ", item['degree_name'])

            if "doctor of" in item['programme_en'].lower() or item['degree_name'].lower() == "mres":
                item['teach_type'] = 'phd'
                item['degree_type'] = 3
            print("item['teach_type']: ", item['teach_type'])
            print("item['degree_type']: ", item['degree_type'])

            start_date = response.xpath("//span[@class='m-facts__fact']//text()|"
                                        "//select[@id='edit-date']//option[@selected='selected']//text()").extract()
            clear_space(start_date)
            print("start_date: ", start_date)
            item['start_date'] = getStartDate(''.join(start_date))
            print("item['start_date']: ", item['start_date'])

            mode = response.xpath("//select[@id='edit-mode']//text()").extract()
            clear_space(mode)
            item['teach_time'] = getTeachTime(''.join(mode))
            print("item['teach_time']: ", item['teach_time'])

            location = response.xpath("//label[@for='edit-compulsory']/following-sibling::*//text()").extract()
            item['location'] = ''.join(location).strip()
            print("item['location']: ", item['location'])

            duration = response.xpath("//dt[@class='m-facts__label']//following-sibling::*//text()").extract()
            clear_space(duration)
            print("duration: ", duration)
            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            print("item['duration'] = ", item['duration'])
            print("item['duration_per'] = ", item['duration_per'])

            overview_en = response.xpath(
                "//h3[@class='field-label'][contains(text(),'Course overview')]/../*[position()<last()]|"
                "//div[@class='m-body__margin-bottom t-course__overview']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
            # print("item['overview_en']: ", item['overview_en'])

            entry_requirements = response.xpath("//div[@id='entry-international']//form[@id='courses-international-form']/preceding-sibling::*//text()").extract()
            item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            ielts_desc = response.xpath("//div[@id='entry-international']//li[contains(text(),'Postgraduate:')]//text()").extract()
            clear_space(ielts_desc)
            # print("ielts_desc: ", ielts_desc)
            item['ielts_desc'] = ''.join(ielts_desc)
            # print("item['ielts_desc']: ", item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            assessment_en = response.xpath("//h3[@class='field-label'][contains(text(),'How will I be taught?')]/..|"
                                           "//h3[@class='field-label'][contains(text(),'How will I be assessed?')]/..").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            tuition_fee = response.xpath("//div[@class='field-fees-international']/p//text()").extract()
            print("tuition_fee: ", tuition_fee)
            if len(tuition_fee) > 0:
                item['tuition_fee'] = getTuition_fee(''.join(tuition_fee))
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee']: ", item['tuition_fee'])
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            career_en = response.xpath("//div[@id='careers-job-prospects']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en)).replace("<div></div>", "").strip()
            # print("item['career_en']: ", item['career_en'])

            modules = re.findall(r"function\sinit_drupal_core_settings\(\)\s{jQuery\.extend\(Drupal\.settings,.*}", response.text)
            # print("modules: ", modules)
            modules_str = ''.join(modules).replace("function init_drupal_core_settings() {jQuery.extend(Drupal.settings,", "").strip()
            modules_dict = json.loads(modules_str)
            print("modules_dict: ", modules_dict)
            # groupCode     modulesNid
            print(modules_dict.get("courses"))
            # if modules_dict.get('courses').get('groupCode') is not False:
            if modules_dict.get('courses').get('groupCode') is not None:
                modules_json = "https://www1.chester.ac.uk/courses/modules/ajax/"+modules_dict.get('courses').get('modulesNid')+"/"+modules_dict.get('courses').get('groupCode')+"/389"
                # print("modules_json: ", modules_json)
                mdict = json.loads(requests.get(modules_json).text)
                # print("mdict: ", len(mdict))
                m = mdict[-1].get('data')
                if m != None:
                    item['modules_en'] = remove_class(clear_lianxu_space([m]))
            print("item['modules_en']: ", item['modules_en'])

            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<div class="content">
    
  <h2>Before You Apply</h2>
<p>Please read the relevant course information carefully. If you would like to know more about a programme or research area, we suggest that you contact the programme leader or centre director, in writing, by telephone or by&nbsp;<a href="mailto:postgrad@chester.ac.uk">email</a>&nbsp;via Postgraduate Admissions. They will be able to answer your questions in more detail and send you further information.</p>
<h2>How to Apply</h2>
<p>If you are a Home/EU student applying for a postgraduate taught course, you should apply directly via the online application system (AIMS) via the link below.&nbsp; If you are an International student applying for a postgraduate taught course, you should apply via the <a href="http://www1.chester.ac.uk/study/postgraduate/how-apply/applying-taught-courses-international-applicants">International Centre</a>. If you are applying for a PGCE Primary, Secondary or Early Years programmes, please note there is a separate admissions&nbsp;procedure.&nbsp; Please email <a href="mailto:postgrad@chester.ac.uk">postgrad@chester.ac.uk</a> and we will forward your details on to PGCE Admissions. All&nbsp;<a href="http://www.chester.ac.uk/research/degrees/application">research degree</a>&nbsp;applicants,&nbsp;whether Home, EU or International, should visit the relevant web pages or follow the links on the right hand side of this page.</p>
<p>Paper application forms are no longer issued, except in cases where an online application would impossible for the candidate. Please complete the relevant online application on our website.&nbsp;</p>
<p>&nbsp;Once you have submitted your application, the system will automatically contact your referees on your behalf. Your application may not be considered without two appropriate references and all additional documents required with your application, which include:&nbsp;</p>
<ul>
<li>Copies of certificates/transcripts</li>
<li>Copy of English language proficiency certificate (if required).&nbsp;<strong>Applicants whose first language is not English must provide evidence of proficiency to IELTS 6.5 with no less than 5.5 in each band or equivalent.</strong></li>
<li>Full curriculum vitae (if required)</li>
<li>You may also be asked to complete a fees assessment in order to determine the level of tuition fee payable.</li>
</ul>
<p>Specific programmes require additional documents to be submitted with your application, e.g. Nutrition and Dietetics, Fine Art.</p>
<p>Before doing so, please ensure that you inform your referees. In most cases the references shall come from independent academic referees, i.e. they are not normally provided by the programme leader of the course you are applying for. Once your application is submitted, we will then forward it to the relevant programme leader for consideration. If your application is successful, an offer of a place will be made in writing by Postgraduate Admissions. This will either be unconditional or conditional, depending on the completeness of your application.</p>
<h2>Entry Requirements</h2>
<p>Usually, postgraduate applicants should have an appropriate first degree, with a minimum of second class honours or equivalent. However, if you do not have appropriate academic qualifications, you may be admitted by virtue of prior work experience or by demonstrating relevant knowledge and skills in a specific field. If you are unsure whether your qualifications are acceptable for admission to your chosen programme of study, contact the programme leader or Postgraduate Admissions for further advice.&nbsp;</p>
<p>If your qualifications or experience are not suitable, we will be able to advise you about further options that might bring you up to the required level necessary to enter the course of your choice.</p>
<p>Each course has its own entry requirements, which are shown on each individual course web page under the 'Entry requirements' tab.</p>
<p>For entry requirements relating to our PGCE<a href="/postgraduate/pgce-in-education-primary" title="PG Primary">&nbsp;Primary</a>,&nbsp;<a href="/postgraduate/pgce-secondary-programme" title="PG Secondary">Secondary&nbsp;</a>and&nbsp;<a href="/postgraduate/pgce-early-years" title="PG Early Years">Early Years</a>&nbsp;courses please refer to the relevant pages.</p>
<p>If you have any queries concerning the applications process please contact us at:</p>
<h4>T: 01244 512456/512474<br />
E:&nbsp;<a href="mailto:postgrad@chester.ac.uk" title="Postgraduate Enquiries">postgrad@chester.ac.uk</a></h4>
<p>&nbsp;</p>
<h2>Accreditation of Prior Learning (APL/APEL)</h2>
<p>To be admitted to a postgraduate course, evidence of your prior learning should be equal to higher education Level 3, now referred to as level 6, which is the final year of an undergraduate degree course, or other equivalent, e.g. related professional qualifications. A subject tutor will help you to determine how much of your prior learning can be credited against the course. This may not have been undertaken in an educational environment, but its value may be the same, or more. Information about how this system works and how professional qualification equivalence is available can be obtained from the subject departments.</p>
<p>We may give credit for a course, or part of a course, that would exempt you from having to study that area again. The onus is on you to prove that your learning and experience matches the area for which exemption is claimed.</p>
<p>There may be subject areas for which course attendance is compulsory and credit exemption does not apply, but, equally, there may be areas of study for which credit may be gained purely on the basis of your prior academic achievements or experience.</p>
<p>It is possible to claim credit for up to 66.7% of any award. Please note that this does not apply to MPhil or PhD courses as they have their own process known as 'Advance Standing'. Please contact&nbsp;<a href="mailto:pgradmissions@chester.ac.uk">Postgraduate Research Admissions</a>&nbsp;for further details.</p>
<p>If you have any queries or would like to find out more about CATS or APL/APEL, please contact the APL Officer within the relevant faculty.</p>
<h2>When do the programmes start?</h2>
<p>The majority of postgraduate programmes commence in early October each year, although some allow students to enter in January/February or April/May. For specific start dates for your chosen programme, please consult the relevant section of the website, or contact Postgraduate Admissions, who will be able to help you.</p>
<h2>What is the deadline for applications?</h2>
<p>There are no specific deadlines for most applications made directly to us, although there are some exceptions (check your programme details). The University will accept applications throughout the year, but we would generally advise that you send in your application form by the end of July to ensure that you have time to make any funding and/or accommodation arrangements, and for documents such as transcripts and references to be obtained if not submitted with the application. This will also give you more time to meet any conditions we may potentially attach to an offer.&nbsp; Some courses have earlier application deadlines.&nbsp; Please check the deadline that applies to the programme you are interested in before you apply. There is a strict deadline for applications to Nutrition and Dietetics and Social Work. Please refer to the relevant course web pages.</p>
<p>The deadline for PGCE applications is set by the Graduate Teacher Training Register (GTTR).</p>
<h2>Students with Disabilities</h2>
<p>We are committed to a policy of equal opportunities for applicants with disabilities or specific needs. Although applications from all prospective students are considered according to the same entry criteria, those of you who declare a disability or specific need will also be considered on an individual basis. As some of our buildings are old and not purpose-built, they may not be suitable for those of you with restricted mobility.&nbsp;</p>
<p>However, we are continually working to improve access routes and other facilities on campus to assist physically disabled students during their programmes of study. Wherever possible, we try to make arrangements or adaptations as appropriate, within the existing restrictions placed upon us.</p>
<p><strong>Good luck with your application!</strong></p>
<p><a class="m-link m-link--primary" href="https://flow.chester.ac.uk/tkflow_U/Flow.aspx?f=appform1.kdt&amp;template=template5&amp;course=PGT&amp;theme=redmond">Apply Now</a></p>
<div class="m-callout">
<p>If you're interested in a course at University Centre Shrewsbury, <a href="http://ucshrewsbury.ac.uk/postgraduate/apply">find out more about the application process.</a></p>
</div>
  </div>
"""]))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            item['require_chinese_en'] = remove_class(clear_lianxu_space([""" <div class="field-collection-view clearfix view-mode-full">
  <h3 class="field-course-type">
    Postgraduate Study  </h3>

  <ul><li>Bachelor's degree with 68% or above</li>
<li>East and West International Education (EWIE)/ Wiseway Global International Pre-Masters Programme at 60% or above</li>
<li>Dongfang International Centre for Education Exchange Top University Pre-Masters Programme at 60% or above</li>
<li>Applicants for the MBA should have 2 years work experience, although well qualified and motivated individuals without this will be considered</li>
</ul></div>  <div class="field-collection-view clearfix view-mode-full field-collection-view-final">
  <p><strong>Academic Requirements:</strong></p>
<ul><li>Master's degree with a recognised institution</li>
</ul><p><strong>English Requirements:</strong></p>
<ul><li><strong>IELTS: 6.5 (no less than 5.5 in any band)</strong></li>
</ul></div>"""]))
            # print("item['require_chinese_en']: ", item['require_chinese_en'])

            # department = response.xpath("//dt[contains(text(), 'Department')]/following-sibling::dd[1]//text()").extract()
            # item['department'] = ''.join(department).strip()
            # print("item['department']: ", item['department'])

            yield item
        except Exception as e:
            with open("scrapySchool_England/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

