# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration
from lxml import etree
import requests


class UniversityOfChichester_USpider(scrapy.Spider):
    name = "UniversityOfChichester_U"
    start_urls = ["https://www.chi.ac.uk/search/course-search-results?f%5B0%5D=field_course_type%253APostgraduate&f%5B1%5D=field_year%3A2019&f%5B2%5D=field_course_type%3AUndergraduate"]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36"}

    def parse(self, response):
        links = response.xpath("//div[@class='view-content']/div//a/@href").extract()
        # 组合字典
        programme_dict = {}
        programme_list = response.xpath("//div[@class='view-content']/div//a//text()").extract()
        clear_space(programme_list)

        for link in range(len(links)):
            url = "https://www.chi.ac.uk" + links[link]
            programme_dict[url] = programme_list[link]

        # print(programme_dict)
        print(len(links))
        links = list(set(links))
        print(len(links))
        for link in links:
            url = "https://www.chi.ac.uk" + link
            # print(url)
            yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Chichester"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        item['location'] = 'University of Chichester, College Lane, Chichester, West Sussex, PO19 6PE'
        print("===========================")
        print(response.url)
        item['major_type1'] = response.meta.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            department = response.xpath("//div[@class='breadcrumb']//a[2]//text()").extract()
            item['department'] = ''.join(department).strip()
            # print("item['department']: ", item['department'])

            programmeDegreetype = response.xpath(
                "//div[@class='field-items accordion-content']/h2//text()").extract()
            # print("programmeDegreetype: ", programmeDegreetype)
            programmeDegreetypeStr = ''
            if len(programmeDegreetype) > 0:
                programmeDegreetypeStr = programmeDegreetype[0].strip()
            # print("programmeDegreetypeStr: ", programmeDegreetypeStr)

            degree_type = re.findall(r"^\w+/\w+|^\w+.*/\s\w+|^\w+\s\(Hons\)|^\w+/\w+\s\(Hons\)|^\w+", programmeDegreetypeStr, re.I)
            degree_name_str = ''.join(degree_type).strip()
            item['degree_name'] = degree_name_str.replace("(Hons)", "").replace("(HONS)", "").strip()
            print("item['degree_name']: ", item['degree_name'])

            programme = programmeDegreetypeStr.replace(degree_name_str, '')
            item['programme_en'] = ''.join(programme).replace("(Hons)", "").title().strip().strip('-').strip()
            print("item['programme_en']: ", item['programme_en'])

            ucascode = response.xpath(
                "//p[contains(text(),'UCAS ')]//text()").extract()
            clear_space(ucascode)
            # print("ucascode: ", ucascode)
            if len(ucascode) > 0:
                item['ucascode'] = ''.join(ucascode[0]).replace("UCAS", "").strip()
            print("item['ucascode'] = ", item['ucascode'])

            alevel = response.xpath("//*[contains(text(),'A levels')]//text()").extract()
            item['alevel'] = clear_lianxu_space(alevel)
            # print("item['alevel']: ", item['alevel'])

            ib = response.xpath("//*[contains(text(),'International Baccalaureate')]//text()").extract()
            item['ib'] = clear_lianxu_space(ib)
            # print("item['ib']: ", item['ib'])

            entry_requirements = response.xpath(
                "//section//div[@class='field field-name-field-main-content field-type-text-long field-label-hidden']//div[@class='field-items accordion-content']//h2[contains(text(), 'Entry')]/..//text()|"
                "//section//div[@class='field field-name-field-main-content field-type-text-long field-label-hidden']//div[@class='field-items accordion-content']//h2[contains(text(), 'ENTRY')]/..//text()").extract()
            # print("==", entry_requirements)
            rntry_requirements= clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            ielts_desc = response.xpath("//*[contains(text(),'IELTS')]/text()").extract()
            clear_space(ielts_desc)
            # print("ielts_desc: ", ielts_desc)
            item['ielts_desc'] = ''.join(ielts_desc)
            # print("item['ielts_desc']: ", item['ielts_desc'])


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

            # interview_desc_en = response.xpath("//span[contains(text(),'Teaching and assessment')]/../..").extract()
            # item['interview_desc_en'] = remove_class(clear_lianxu_space(interview_desc_en))
            # print("item['interview_desc_en']: ", item['interview_desc_en'])


            duration_url = response.xpath("//iframe[@id='unistats-widget-frame']/@src").extract()
            clear_space(duration_url)
            print("duration_url: ", duration_url)
            if len(duration_url) > 0:
                data = etree.HTML(requests.get(duration_url[0], headers=self.headers).text)
                duration = data.xpath("//p[contains(text(),'Full time')]//text()")
                clear_space(duration)
                print("duration: ", duration)
                duration_list = getIntDuration(''.join(duration))
                if len(duration_list) == 2:
                    item['duration'] = duration_list[0]
                    item['duration_per'] = duration_list[-1]
            print("item['duration'] = ", item['duration'])
            print("item['duration_per'] = ", item['duration_per'])

            item['ielts'] = 6.0
            item['ielts_l'] = 5.5
            item['ielts_s'] = 5.5
            item['ielts_r'] = 5.5
            item['ielts_w'] = 5.5

            # https://www.chi.ac.uk/study-us/fees-finance/tuition-fees
            item['tuition_fee'] = 13000
            item['require_chinese_en'] = """<p>Senior Secondary School Certificate PLUS an International Foundation</p>
<p>Year OR Senior Secondary School Certificate 80% +</p>"""
            # https://www.chi.ac.uk/international/how-apply/undergraduate-applications
            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<div class="col-2-3">
      
              <h1 class="title" id="page-title">Undergraduate Applications</h1>
      
      
        <div class="region region-content">
    <div id="block-system-main" class="block block-system">

    
  <div class="content">
    <div id="node-2130" class="node node-content-page node-readydeploy clearfix" about="/international/how-apply/undergraduate-applications" typeof="sioc:Item foaf:Document">
  
  <div class="content">
    <div class="field field-name-field-serif-intro field-type-text-long field-label-hidden"><div class="field-items"><div class="field-item even"><p>We recommend you apply online through  <a target="_blank" href="http://www.ucas.com/apply">UCAS</a>. International students may also apply directly to the University using the University of Chichester <a target="_blank" href="https://d3mcbia3evjswv.cloudfront.net/files/International%20Application%202017-2018_1_0.doc?dt7VFSaSnVZlYb1a1vvKmEfvuuqVmsqE">International Application Form.</a></p>
</div></div></div><div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even" property="content:encoded"><h3><span class="rangySelectionBoundary" id="selectionBoundary_1424440432166_7907926958422292" style="line-height: 0; display: none;">﻿</span><strong>Applying via UCAS</strong></h3>
<p>You can apply for up to five different degree courses at up to five different institutions through UCAS (the national Universities and Colleges Admissions Service). Your application is sent to all five  universities which you have applied to at the same time.  There is no need to choose a first choice university at this stage.</p>
<p>Each course has a UCAS code that you will find on our <a href="/search/course-search">Course pages </a>or in our prospectus. You will need to know the UCAS code for the course you want to apply for when you make your application.</p>
<p><strong>Deadlines and important dates</strong></p>
<ul><li>1 September UCAS opens for applications for courses starting in September/October the following year.</li>
<li>15 January - Recommended application date for UK and other EU applicants.</li>
<li>30 June - Closing date for international (non-EU) applicants. (We do advise you to apply earlier if possible though.)</li>
<li>July / August - applications can still be submitted via UCAS but you can only apply to one university at a time in July and August (known as "Clearing")</li>
</ul><p>When you are applying to UCAS you will also need the UCAS institution code for the university. The UCAS code for the University of Chichester is <strong>(CHICH) C58</strong>.</p>
<p>Need further information or guidance on applying?</p>
<p>Then please either contact Admissions on +44 (0)1243 816002 or email <a href="mailto:admissions@chi.ac.uk?subject=International%20application">admissions@chi.ac.uk</a></p>
<h4><strong>Accepting an offer of a place</strong></h4>
<p>Your university offer(s) will be notified to you via your UCAS account and you can select a first ("firm") choice and, if you wish, a second ("insurance") choice via UCAS who will then inform the universities of your decision.</p>
<p><strong>Tuition fee deposit</strong></p>
<p>If you wish to accept an offer from the University of Chichester, you will be expected to pay a deposit of £2,000 before a UKVI Certificate of Acceptance for Studies (CAS) will be issued to you.</p>
<p>The deposit will be refunded, in full, if the University withdraws the programme.</p>
<p>Otherwise, the deposit will only be refunded, minus a £250 administration charge, if the applicant provides written evidence of being refused a visa to join the programme, through no fault of his or her own. Where the applicant has not disclosed relevant previous study, or does not have sufficient funds in the bank account for the relevant period, are examples of where it would be deemed the applicant's responsibility for not securing a visa.</p>
</div></div></div></div></div></div></div></div></div>"""]))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            if "/" in item['ucascode']:
                if len(item['ucascode']) > 20:
                    item['ucascode'] = ""
                print("///////////////")
                print("item['ucascode']1: ", item['ucascode'])
                ucascode_0 = item['ucascode'].split("/")
                if "/" in item['degree_name']:
                    degree_name_0 = item['degree_name'].split("/")
                else:
                    degree_name_0 = [item['degree_name'], item['degree_name']]
                for u in range(len(ucascode_0)):
                    item['ucascode'] = ucascode_0[u]
                    item['degree_name'] = degree_name_0[u]
                    yield item
            else:
                yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

