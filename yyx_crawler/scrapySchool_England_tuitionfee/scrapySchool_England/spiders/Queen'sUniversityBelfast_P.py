# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
import requests
from lxml import etree
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getDuration import getIntDuration

class QueensUniversityBelfast_PSpider(scrapy.Spider):
    name = "QueensUniversityBelfast_P"
    # 研究领域链接
    start_urls = ["http://www.qub.ac.uk/courses/postgraduate-taught/?keyword="]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        links = response.xpath("//article[@class='levels']/div[@class='results inner']/table/tbody/tr/th/a/@href").extract()
        for link in links:
            url = "http://www.qub.ac.uk/courses/postgraduate-taught/"+ link
            # url = "http://www.qub.ac.uk/courses/postgraduate-taught/arts-humanities-mres/"
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "Queen's University Belfast"
        # item['country'] = 'England'
        # item['website'] = 'http://www.qub.ac.uk/'
        item['url'] = response.url
        item['teach_type'] = 'taught'
        item['degree_type'] = 2
        print("===========================")
        print(response.url)
        try:
            degree_type = response.xpath(
                "//div[@class='columns aligned']//div[@class='column colspan-8']/p[1]//text()").extract()
            degree_type = ''.join(degree_type).split("|")
            # print("degree_type: ", degree_type)
            if len(degree_type) != 0:
                item['degree_name'] = degree_type[0].strip()
            print("item['degree_name']: ", item['degree_name'])

            # 专业
            programme = response.xpath(
                "//div[@class='columns aligned']//div[@class='column colspan-8']/h1//text()").extract()
            clear_space(programme)
            item['programme_en'] = ''.join(programme).strip(item['degree_name']).strip()
            print("item['programme_en']: ", item['programme_en'])

            # start_date
            start_date = response.xpath(
                "//span[@class='key-entry-year']//text()").extract()
            clear_space(start_date)
            item['start_date'] = ''.join(start_date).strip()
            print("item['start_date']: ", item['start_date'])

            # start_date
            mode = response.xpath(
                "//div[@id='duration-tabs']/ul/li//text()").extract()
            clear_space(mode)
            if "Full" in ''.join(mode) or 'full' in ''.join(mode):
                item['teach_time'] = 'fulltime'
            print("item['teach_time']: ", item['teach_time'])

            # duration
            duration = response.xpath(
                "//div[@id='duration-tabs']/div/p/text()").extract()
            clear_space(duration)
            print(duration)
            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            print("item['duration']-: ", item['duration'])
            print("item['duration_per']-: ", item['duration_per'])

            # duration1 = ""
            # if len(duration) == 2:
            #     duration1 = duration[0].strip()
            # elif len(duration) == 4:
            #     duration1 = duration[0].strip() + "\t" + duration[2]
            # elif len(duration) == 6:
            #     duration1 = duration[0].strip() + "\t" + duration[2] + "\t" + duration[4]
            # # print(duration1)
            #
            # d_re = re.findall(r'\d+', duration1)
            # if len(d_re) != 0:
            #     item['duration'] = int(d_re[0])
            # y_re = re.findall(r'year', duration1)
            # if len(y_re) > 1:
            #     item['duration_per'] = 1
            # print("item['duration']: ", item['duration'])
            # print("item['duration_per']: ", item['duration_per'])

            # //div[@id='overview']
            overview = response.xpath(
                "//div[@id='overview']").extract()
            # clear_space(overview)
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])

            # //div[@id='overview']
            modules = response.xpath(
                "//h3[@class='alt'][contains(text(),'Course Structure')]/following-sibling::table").extract()
            # clear_space(modules)
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])

            career = response.xpath(
                "//h3[@class='alt'][contains(text(),'Career Prospects')]/following-sibling::p[1]").extract()
            # clear_space(career)
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            teaching_assessment = response.xpath(
                "//h3[@class='alt'][contains(text(),'Learning and Teaching')]/following-sibling::*").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(teaching_assessment).replace("\n", ""))
            # print("item['assessment_en']: ", item['assessment_en'])

            entry_requirements = response.xpath(
                "//div[@id='entry']//text()").extract()
            item['rntry_requirements'] = remove_class(clear_lianxu_space(entry_requirements))
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            ielts = re.findall(r"IELTS.{1,150}", item['rntry_requirements'])
            item['ielts_desc'] = ''.join(ielts)
            # print("item['ielts_desc']: ", item['ielts_desc'])
            ieltsDict = get_ielts(''.join(ielts))
            item['ielts'] = ieltsDict.get("IELTS")
            item['ielts_l'] = ieltsDict.get("IELTS_L")
            item['ielts_s'] = ieltsDict.get("IELTS_S")
            item['ielts_r'] = ieltsDict.get("IELTS_R")
            item['ielts_w'] = ieltsDict.get("IELTS_W")
            # print(
            #     "item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            # //html//div[@id='fees']//tr[4]
            tuition_fee = response.xpath(
                "//html//div[@id='fees']//tr[4]//text()").extract()
            clear_space(tuition_fee)
            # print("tuition_fee: ", tuition_fee)
            tuition_fee_str = ''.join(tuition_fee).replace("International", "").strip()
            tuition_fee_re = re.findall(r"\d+,\d+|\d+", tuition_fee_str)
            # print("tuition_fee_re: ", tuition_fee_re)
            if len(tuition_fee_re) > 0:
                item['tuition_fee_pre'] = "£"
                item['tuition_fee'] = int(''.join(tuition_fee_re).replace(',', '').strip())
            # if item['tuition_fee'] is None:
            #     print("tuition_fee 为空")
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])
            # print("item['tuition_fee']: ", item['tuition_fee'])

            # //div[@class='panel bg--primary']//div[@class='inner']//p
            department = response.xpath(
                "//div[@class='panel bg--primary']//div[@class='inner']//p//text()").extract()
            clear_space(department)
            # print(department)
            for d in department:
                if "School" in d:
                    item['department'] = d.strip()
                elif "College" in d:
                    item['department'] = d.strip()
                elif "Campus" in d or d == "Biological Sciences" or d == "Marketing strategy" or d == "Management":
                    item['department'] = d.strip()
                elif len(d) == 4 or len(d) == 5 or d == "Arts, English and Languages" or d == "Global Food Security" or d == "Centre for Economic History":
                    item['department'] = d.strip()
            # print("item['department']: ", item['department'])

            department = response.xpath(
                "//html//div[@class='panel bg--grey-l']/div[@class='inner']//a//text()").extract()
            clear_space(department)
            item['department'] = ''.join(department).strip()
            print("item['department']: ", item['department'])

            # //html//div[@class='panel bg--grey-l']/div[@class='inner']/p[1]
            location = response.xpath(
                "//html//div[@class='panel bg--grey-l']/div[@class='inner']/text()").extract()
            clear_space(location)
            location.remove('')
            print("location: ", location)
            item['location'] = ', '.join(location).strip().strip(",").strip()
            print("item['location']: ", item['location'])

            item['apply_desc_en'] = remove_class(clear_lianxu_space(["""<h2>Postgraduate Taught Courses</h2>
<h3>Master's Degrees&nbsp;</h3>
<p>The normal minimum requirement for admission to a Master's degree is a Second Class Honours degree from a UK or Republic of Ireland (ROI) Higher Education Provider or an equivalent qualification acceptable to the University.<span style="text-decoration: underline; line-height: 1.25;"><br /></span></p>"""]))
            # print("item['apply_desc_en']: ", item['apply_desc_en'])

            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<h1 class="alt"><a name="PG"></a>Postgraduate entry requirements</h1>
<p>Entry to graduate diploma or taught masters programmes usually requires either a UK upper second-class (2:1) or a lower second-class (2:2) undergraduate degree. For most courses, your major subject or content of your Bachelor degree may also be considered. Please check our Course Finder for specific entry requirements.</p>
<p>Applicants from China should hold a good four-year bachelor degree from a recognised, well ranked university with an average grade of at least 70-85%.</p>
<table border="1" cellpadding="0" cellspacing="0">
<thead>
<tr><th>
<p><strong>Type of Institution</strong></p>
</th><th>
<p><strong>United Kingdom </strong></p>
<p><strong>2.1 Honours standard</strong></p>
</th><th>
<p><strong>United Kingdom </strong></p>
<p><strong>2.2 Honours standard</strong></p>
</th></tr>
</thead>
<tbody>
<tr>
<td>
<p><strong>Tier 1<br />Prestigious Universities (Top 100 Academic Ranking of World Universities (ARWU), Project 211, Project 985):</strong></p>
</td>
<td>
<p>Final average 75%</p>
</td>
<td>
<p>Final average 70%</p>
</td>
</tr>
<tr>
<td>
<p><strong>Tier 2<br />Other Recognised Universities and Independent Colleges affiliated to a Tier 1 Institution (as defined by Queen's):</strong></p>
</td>
<td>
<p>Final average 80%</p>
</td>
<td>
<p>Final average 75%</p>
</td>
</tr>
<tr>
<td>
<p><strong>Tier 3<br />Other Independent Colleges recognised by Ministry of Education and Self-Study Degrees<br /></strong></p>
</td>
<td>
<p>Final average 85%</p>
</td>
<td>
<p>Final average 80%</p>
</td>
</tr>
</tbody>
</table>"""]))
            # print("item['require_chinese_en']: ", item['require_chinese_en'])

            item['apply_documents_en'] = remove_class(clear_lianxu_space(["""<h2><span style="line-height: 1.25;">International Applicants</span><span style="font-size: 16px; line-height: 1.25;">&nbsp;</span></h2>
<p>To make sure your application is processed in the fastest possible time, you must scan and upload the following supporting documents along with your application. We may not be able to make a decision on your application until we have received all your relevant documents.</p>
<p>Please upload good quality scanned copies of the following:<span style="line-height: 1.25;">&nbsp;</span></p>
<ul>
<li>Degree transcripts for all completed periods of study (undergraduate level and above).<span style="line-height: 1.25;">&nbsp;</span></li>
</ul>
<ul>
<li>If your degree is still in progress, you must provide a transcript of results achieved to date. This can be requested from your University.&nbsp;<span style="line-height: 1.25;">&nbsp;</span></li>
</ul>
<ul>
<li>Copies of your official Degree/Diploma Certificates, for the qualification(s) you have already completed. These are the documents that confirm the level and title of your qualification(s), for example, Bachelor of Science in Mathematics.&nbsp;</li>
<li><span style="line-height: 1.25;">For each qualification, the degree transcript and degree award certificate should be combined in one document for uploading.&nbsp; You may upload a combined document in respect of one undergraduate course, and additional combined documents for up to three postgraduate courses.</span></li>
</ul>
<ul>
<li>Research proposal (for MPhil/PhD/MD applicants only).<span style="line-height: 1.25;">&nbsp;</span></li>
</ul>
<ul>
<li>Certified translations, if your original documents are not in English. If you do not have translations at the time of application, please forward by email to <a href="mailto:intl.student@qub.ac.uk">intl.student@qub.ac.uk</a> when available.<span style="line-height: 1.25;">&nbsp;</span></li>
</ul>
<ul>
<li>English language requirements: applicants whose first language is not English will need to show evidence of an acceptable level of competency in the English language.<span style="line-height: 1.25;">&nbsp;</span></li>
</ul>
<p>Please note that there is no need to mail original documents to us at this stage. However, you will need to produce the original documents when applying for your student visa and to complete registration and enrolment at the University at the start of the programme.</p>"""]))
            # print("item['apply_documents_en']: ", item['apply_documents_en'])

            item['apply_proces_en'] = "http://www.qub.ac.uk/Study/PostgraduateStudy/How-to-apply/"
            yield item
        except Exception as e:
            with open("scrapySchool_England/error/" + item['university']+str(item['degree_type'])+".txt", 'w', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)
