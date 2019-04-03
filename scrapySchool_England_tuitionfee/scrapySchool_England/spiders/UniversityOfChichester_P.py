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
from w3lib.html import remove_tags

class UniversityOfChichester_PSpider(scrapy.Spider):
    name = "UniversityOfChichester_P"
    start_urls = ["https://www.chi.ac.uk/search/course-search-results?f%5B0%5D=field_course_type%253APostgraduate&f%5B1%5D=field_course_type%3APostgraduate&f%5B2%5D=field_year%3A2019"]

    def parse(self, response):
        links = response.xpath("//div[@class='view-content']/div//a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))

#         links = ["https://www.chi.ac.uk/department-childhood-social-work-social-care/our-courses/ma-social-work",
# "https://www.chi.ac.uk/ma-performance-dance-mapdance",
# "https://www.chi.ac.uk/ma-choreography-independent-research",
# "https://www.chi.ac.uk/ma-sport-pedagogy-physical-education",
# "https://www.chi.ac.uk/department-creative-digital-technologies/courses/ma-music-industry-innovation-enterprise-platform-one-isle-wight",
# "https://www.chi.ac.uk/ma-somatic-practices-independent-research", ]
        for link in links:
            url = "https://www.chi.ac.uk" + link
            # print(url)
            # url = link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "University of Chichester"
        item['url'] = response.url
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        item['location'] = 'University of Chichester, College Lane, Chichester, West Sussex, PO19 6PE'
        print("===========================")
        print(response.url)
        try:
            department = response.xpath("//div[@class='breadcrumb']//a[2]//text()").extract()
            item['department'] = ''.join(department).strip()
            print("item['department']: ", item['department'])

            programmeDegreetype = response.xpath(
                "//div[@class='field-items accordion-content']/h2//text()").extract()
            # print("programmeDegreetype: ", programmeDegreetype)
            programmeDegreetypeStr = ''
            if len(programmeDegreetype) > 0:
                programmeDegreetypeStr = programmeDegreetype[0].strip().strip("In").strip()
            # print("programmeDegreetypeStr: ", programmeDegreetypeStr)

            degree_type = re.findall(r"^(Postgraduate\sCertificate|\w+-\w+\sand\s\w+|\w+\s?/\s?\w+|\w+)\s", programmeDegreetypeStr, re.I)
            item['degree_name'] = ''.join(degree_type).strip()
            print("item['degree_name']: ", item['degree_name'])

            programme = programmeDegreetypeStr.replace(''.join(degree_type), '')
            item['programme_en'] = ''.join(programme).title().strip().strip('-').strip()
            print("item['programme_en']: ", item['programme_en'])

            # if item['degree_name'].lower() == "phd":
            #     item['teach_type'] = 'phd'
            #     item['degree_type'] = 3
            # print("item['teach_type']: ", item['teach_type'])
            # print("item['degree_type']: ", item['degree_type'])

            entry_requirements = response.xpath(
                "//section//div[@class='field field-name-field-main-content field-type-text-long field-label-hidden']//div[@class='field-items accordion-content']//h2[contains(text(), 'Entry')]/..//text()|"
                "//section//div[@class='field field-name-field-main-content field-type-text-long field-label-hidden']//div[@class='field-items accordion-content']//h2[contains(text(), 'ENTRY')]/..//text()").extract()
            # print("==", entry_requirements)
            item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            ielts_desc = response.xpath("//*[contains(text(),'IELTS')]/text()").extract()
            clear_space(ielts_desc)
            # print("ielts_desc: ", ielts_desc)
            item['ielts_desc'] = ''.join(ielts_desc)
            # print("item['ielts_desc']: ", item['ielts_desc'])

            # ielts_dict = get_ielts(item['ielts_desc'])
            item['ielts'] = 6.5
            item['ielts_l'] = 6.0
            item['ielts_s'] = 6.0
            item['ielts_r'] = 6.0
            item['ielts_w'] = 6.0
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            tuition_fee = re.findall(r"£\d+,\d+", item['rntry_requirements']) # Full\sFee:\s£\d+,\d+
            # print("tuition_fee: ", tuition_fee)
            if len(tuition_fee) > 0:
                item['tuition_fee'] = getTuition_fee(''.join(tuition_fee))
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee']: ", item['tuition_fee'])
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            overview_en = response.xpath("//span[contains(text(),'Course content')]/../..").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
            # print("item['overview_en']: ", item['overview_en'])

            career_en = response.xpath("//span[contains(text(),'Where this can take you')]/../..").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en)).replace("<div></div>", "").strip()
            # print("item['career_en']: ", item['career_en'])

            modules = response.xpath("//span[contains(text(),'Indicative modules')]/../..").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])

            assessment_en = response.xpath("//span[contains(text(),'Teaching and assessment')]/../..").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<div class="col-2-3">
      
              <h1 class="title" id="page-title">Postgraduate Applications</h1>
      
      
        <div class="region region-content">
    <div id="block-system-main" class="block block-system">

    
  <div class="content">
    <div id="node-2131" class="node node-content-page node-readydeploy clearfix" about="/international/how-apply/postgraduate-applications" typeof="sioc:Item foaf:Document">
  
  <div class="content">
    <div class="field field-name-field-serif-intro field-type-text-long field-label-hidden"><div class="field-items"><div class="field-item even"><p>If you are applying for a postgraduate course you need to apply directly to the university.</p>
<p>Please complete the University of Chichester <a target="_blank" href="http://d3mcbia3evjswv.cloudfront.net/files/International%20Application%202017-2018_1.doc?.ct2wv4wqwjzLELhPfQzFuWiUc9_6Zlt">International Application Form.</a></p>
</div></div></div><div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even" property="content:encoded"><h4>What you will need to provide:</h4>
<p>Along with your <a target="_blank" href="http://d3mcbia3evjswv.cloudfront.net/files/International%20Application%202015-2016_1.doc">International Application Form</a> you will need to include the following documents:</p>
<ul><li>Personal Statement – A written piece of about yourself; why you have chosen the course you are applying for, and why you want to come to the University of Chichester.</li>
<li>Copies of Qualifications to date – Translated into English</li>
<li>Proof of English Language Level – If English is not your first language</li>
<li>Two academic references</li>
<li>For a Music course we will need a DVD of a musical performance for 5 minutes long. We also require an academic essay written in English.</li>
<li>For Dance we need a weblink of two performances, one of which should be contemporary and at least three minutes long. We also require an academic essay written in English. </li>
</ul><h4>When you have all of the above documents, please post to:</h4>
<p>International Admissions, University of Chichester, College Lane, Chichester, West Sussex, PO19 6PE, United Kingdom.</p>
<h4>What happens to your application form?</h4>
<p>When your application is received by the Admissions Department, it will be entered onto our student record system and a ‘Student Number’ will be assigned to you. We will then check that you have included all the necessary documents and that you have the required entry qualifications. The Admissions Tutor for your chosen subject will consider your application. </p>
<h4>You will then be sent one of the following letters:</h4>
<ul><li>Conditional Offer</li>
</ul><p>Conditional Offer is when you have been offered a place on a course, subject to certain conditions. The conditions may be academic, for example the successful completion of a current course of study or obtaining a particular IELTS score. If you are paying international fees, you will also be required to pay a deposit of £2,000.</p>
<ul><li>Unconditional Offer</li>
</ul><p>Unconditional offer is when you fulfil all the entry requirements and have been offered a place on the course</p>
<h4>Need further information or guidance on applying?</h4>
<p>Then please either contact Admissions on +44 (0)1243 816002 or email <a href="mailto:admissions@chi.ac.uk.?subject=International%20Application">admissions@chi.ac.uk.</a></p>
</div></div></div>  </div></div>  </div>
</div>
  </div>
    </div>"""]))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            # mode = response.xpath("//dt[contains(text(), 'Study mode')]/following-sibling::dd[1]//text()").extract()
            # clear_space(mode)
            # item['teach_time'] = getTeachTime(''.join(mode))
            # # print("item['teach_time']: ", item['teach_time'])

            start_date = response.xpath("//strong[contains(text(),'tart date')]//text()").extract()
            clear_space(start_date)
            print("start_date: ", start_date)
            if len(start_date) > 0:
                for s in start_date:
                    item['start_date'] += getStartDate(''.join(start_date)) + ","
            item['start_date'] = item['start_date'].strip().strip(",").strip()
            print("item['start_date']: ", item['start_date'])
            # print(re.findall(".{1,10}Start.{1,10}", response.text, re.I))

            # duration = response.xpath("//dt[contains(text(), 'Duration')]/following-sibling::dd[1]//text()").extract()
            duration = re.findall(".{1,10}month.{1,20}|.{1,10}year.{1,20}", remove_tags(item['overview_en']), re.I)
            clear_space(duration)
            print("duration: ", duration)
            patt = response.xpath(
                "//h2[contains(text()," + "'" + item['programme_en'] + "'" + ")]/..//text()").extract()
            print(patt)
            clear_space(patt)
            duration1 = re.findall(".{1,10}month.{1,20}|.{1,10}year.{1,20}", ''.join(patt), re.I)
            clear_space(duration1)
            print("duration1: ", duration1)
            duration = duration1+duration
            print('; '.join(duration))
            item['other'] = '; '.join(duration)
            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            print("item['duration'] = ", item['duration'])
            print("item['duration_per'] = ", item['duration_per'])


            item['require_chinese_en'] = """<div>4 year bachelor degree (Xueshi) Minimum 70% / GPA 2.8 out of 4</div>"""
            yield item
        except Exception as e:
            with open(item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

