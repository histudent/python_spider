# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
import requests
from lxml import etree
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration

class QueensUniversityBelfast_USpider(scrapy.Spider):
    name = "QueensUniversityBelfast_U"
    # 研究领域链接
    start_urls = ["http://www.qub.ac.uk/courses/undergraduate/?keyword="]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        links = response.xpath("//article[@class='levels']/div[@class='results inner']/table/tbody/tr/th/a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))

#         links = ["http://www.qub.ac.uk/courses/undergraduate/2018/master-of-liberal-arts-mlibarts-y300/",
# "http://www.qub.ac.uk/courses/undergraduate/2018/divinity-bd/",]
        for link in links:
            url = "http://www.qub.ac.uk/courses/undergraduate/"+ link
            # url = link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "Queen's University Belfast"
        # item['country'] = 'England'
        # item['website'] = 'http://www.qub.ac.uk/'
        item['url'] = response.url
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        try:
            degree_type = response.xpath(
                "//div[@class='columns aligned']//div[@class='column colspan-8']/h2//text()").extract()
            degree_type = ''.join(degree_type).split("|")
            print("degree_type: ", degree_type)
            if len(degree_type) != 0:
                item['degree_name'] = degree_type[0].strip()
            print("item['degree_name']: ", item['degree_name'])

            # 专业
            programme = response.xpath(
                "//div[@class='columns aligned']//div[@class='column colspan-8']/h1//text()").extract()
            clear_space(programme)
            item['programme_en'] = ''.join(programme).replace(item['degree_name'],'').strip()
            print("item['programme_en']: ", item['programme_en'])

            # start_date
            start_date = response.xpath(
                "//span[@class='cf-key-details key-entry-year']//text()").extract()
            clear_space(start_date)
            item['start_date'] = ''.join(start_date).strip()
            print("item['start_date']: ", item['start_date'])

            # duration
            duration = response.xpath(
                "//p[@class='cf-key-details-duration']//span[@class='cf-key-details']//text()").extract()
            clear_space(duration)
            print("duration: ", duration)
            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            print("item['duration']-: ", item['duration'])
            print("item['duration_per']-: ", item['duration_per'])

            ucascode = response.xpath("//span[@class='cf-key-details key-ucas-code']//text()").extract()
            clear_space(ucascode)
            if len(ucascode) > 0:
                item['ucascode'] = ''.join(ucascode[0]).strip()
            print("item['ucascode'] = ", item['ucascode'])

            # //div[@id='overview']
            overview = response.xpath(
                "//div[@id='overview']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])

            # //div[@id='overview']
            modules = response.xpath(
                "//h3[@class='alt'][contains(text(),'Course Structure')]/following-sibling::table").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])

            career = response.xpath(
                "//h3[@class='alt'][contains(text(),'Career Prospects')]/following-sibling::p[1]").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            # //a[@id='teaching']/following-sibling::*[position()<6]
            teaching_assessment = response.xpath(
                "//a[@id='teaching']/following-sibling::*[position()<6]").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(teaching_assessment).replace("\n", ""))
            # print("item['assessment_en']: ", item['assessment_en'])

            entry_requirements = response.xpath(
                "//div[@id='entry']//text()").extract()
            rntry_requirements = remove_class(clear_lianxu_space(entry_requirements))
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            ielts = re.findall(r"IELTS.{1,150}", rntry_requirements)
            item['ielts_desc'] = ''.join(ielts)
            print("item['ielts_desc']: ", item['ielts_desc'])
            ieltsDict = get_ielts(''.join(ielts))
            item['ielts'] = ieltsDict.get("IELTS")
            item['ielts_l'] = ieltsDict.get("IELTS_L")
            item['ielts_s'] = ieltsDict.get("IELTS_S")
            item['ielts_r'] = ieltsDict.get("IELTS_R")
            item['ielts_w'] = ieltsDict.get("IELTS_W")
            print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            alevel = response.xpath(
                "//b[contains(text(),'Entry requirements:')]/following-sibling::span//text()").extract()
            clear_space(alevel)
            if len(alevel) > 0:
                item['alevel'] = ''.join(alevel[0]).strip()
            print("item['alevel'] = ", item['alevel'])

            # ib = response.xpath(
            #     "//html//div[@id='courseSummary']//tr/td[contains(text(), 'International Baccalaureate')]/following-sibling::td//text()").extract()
            # item['ib'] = ''.join(ib).strip()
            # print("item['ib'] = ", item['ib'])

            # //html//div[@id='fees']//tr[4]
            tuition_fee = response.xpath(
                "//html//div[@id='fees']//tr[4]//text()").extract()
            clear_space(tuition_fee)
            print("tuition_fee: ", tuition_fee)
            tuition_fee_str = ''.join(tuition_fee).strip().strip("International")
            if "£" in tuition_fee_str:
                item['tuition_fee_pre'] = "£"
                item['tuition_fee'] = int(tuition_fee_str.replace('£', '').replace(',', '').strip())
            print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])
            print("item['tuition_fee']: ", item['tuition_fee'])

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
            item['location'] = '\t'.join(location).strip()
            print("item['location']: ", item['location'])

            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<h1 class="alt"><a name="UG"></a>Undergraduate entry requirements</h1>
<p>The following qualifications will be considered for direct entry to undergraduate programmes:</p>
<ul>
<li>Students who have completed 12 years of education in China and attained the Secondary School Leaving Certificate with good grades must complete an approved Foundation programme or GCE A Levels for progression to undergraduate degree programmes.</li>
<li>The 'Gaokao' Chinese University Entrance Examination will be considered, along with performance in the Senior High School examination for entry to Stage 1 of our undergraduate programmes.</li>
<li>Progression to Stage 1 of an undergraduate degree programme at Queen's&nbsp;(with the exception of Agricultural Technology, Medicine, Dentistry and Social Work) is guaranteed for students who successfully complete the <a title="University%20Preparation%20Courses" href="/home/International/International-students/Applying/University-Preparation-Courses/">INTO Queen's International Foundation Programme</a> at the required standard.</li>
<li>Students who have completed one or two years of university study in China may be eligible for admission to Bachelor degree programmes, if relevant subjects have been studied and strong grades have been achieved.</li>
<li>Applicants who have already completed A-Levels/a recognised Foundation programme or the first year of a relevant degree programme in China, but who do not meet the academic or English language requirements for entry, may wish to consider <a title="University%20Preparation%20Courses" href="/home/International/International-students/Applying/University-Preparation-Courses/">INTO Queen's International Year One</a>. Successful completion at the required standard offers direct entry to the second year of selected undergraduate degree programmes in Management, Economics, Finance and Engineering.</li>
<li>Between 30 and 36 points in the International Baccalaureate Diploma (IB). <a href="/home/International/International-students/Your-Country/InternationalBaccalaureateIBDiplomaEntryRequirements/">Information on required grades</a>.</li>
</ul>
<p><strong>Please note: </strong>Grades required vary depending on the programme of study. Further guidance on the entry requirements for each degree programme can be found in the Undergraduate Coursefinder.</p>"""]))

            apply_proces_en = response.xpath(
                "//div[@id='apply']").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(apply_proces_en))
            print("item['apply_proces_en']: ", item['apply_proces_en'])
            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/"+item['university']+str(item['degree_type'])+".txt", 'w', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)
