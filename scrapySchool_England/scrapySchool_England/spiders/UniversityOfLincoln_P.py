# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts
from scrapySchool_England.getDuration import getIntDuration, getTeachTime


class UniversityOfLincoln_PSpider(scrapy.Spider):
    name = "UniversityOfLincoln_P"
    start_urls = ['http://www.lincoln.ac.uk/home/studywithus/findacourse/?l=pg']

    def parse(self, response):
        # print(response.url)
        links = response.xpath(
            "//table[@id='keywordSearchtable']/tbody[@id='asp_searchResults']/tr/td[@class='cr']/div[contains(text(),'Postgraduate')]/preceding-sibling::a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))
        for link in links:
            url = "http://www.lincoln.ac.uk" + link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.lincoln.ac.uk/"
        item['university'] = "University of Lincoln"
        item['url'] = response.url
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        item['location'] = 'University of Lincoln, Brayford Pool, Lincoln, LN6 7TS'
        print("===========================")
        print(response.url)
        try:
            # //table[@id='newTitle']/tbody[@id='newTitleBody']/tr/td/h1[1]/a
            programmeDegreetype = response.xpath("//div[@id='CourseTitleApms']//h1[@class='nd_2019-20']//text()").extract()
            clear_space(programmeDegreetype)
            # print("programmeDegreetype: ", programmeDegreetype)
            programmeDegreetypeStr = ''.join(programmeDegreetype)

            degree_type = re.findall(r"^(M\w+\sby\sResearch\s/[/\w]+\s|M\w+\sby\sResearch|PG\s\w+|\w+/\w+|\w+)", programmeDegreetypeStr)
            # print("degree_type: ", degree_type)
            item['degree_name'] = ''.join(degree_type)
            print("item['degree_name']: ", item['degree_name'])

            if "phd" in item['degree_name'].lower():
                item['teach_type'] = 'phd'
                item['degree_type'] = 3
            if "by research" in item['degree_name'].lower() or item['degree_name'] == "MRes":
                item['teach_type'] = 'research'
                item['degree_type'] = 3
            print("item['teach_type']: ", item['teach_type'])
            # print("item['degree_type']: ", item['degree_type'])

            programme = programmeDegreetypeStr.replace(''.join(degree_type), '')
            # if len(programme) > 0:
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en']: ", item['programme_en'])

            # //span[@id='durationFT']
            duration = response.xpath("//span[contains(text(),'Full-time Duration')]/..//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration_str = ''.join(duration)

            item['teach_time'] = getTeachTime(duration_str)
            duration_list = getIntDuration(duration_str)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['teach_time'] = ", item['teach_time'])
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            department = response.xpath("//span[contains(text(),'School:')]/following-sibling::a//text()").extract()
            clear_space(department)
            if len(department) > 0:
                item['department'] = department[0]
            print("item['department']: ", item['department'])

            dep_dict = {"lincoln school of architecture and the built environment": "College of Arts",
"lincoln school of design": "College of Arts",
"lincoln school of film and media": "College of Arts",
"school of english and journalism": "College of Arts",
"school of fine and performing arts": "College of Arts",
"school of history and heritage": "College of Arts",
"school of chemistry": "College of Science",
"school of computer science": "College of Science",
"school of engineering": "College of Science",
"school of geography": "College of Science",
"school of life sciences": "College of Science",
"school of mathematics and physics": "College of Science",
"school of pharmacy": "College of Science",
"national centre for food manufacturing": "College of Science",
"lincoln institute for agri-tech": "College of Science",
"school of education": "College of Social Science",
"school of health and social care": "College of Social Science",
"professional development centre": "College of Social Science",
"lincoln law school": "College of Social Science",
"school of psychology": "College of Social Science",
"school of social and political sciences": "College of Social Science",
"school of sport and exercise science": "College of Social Science",}
            if item['department'] != "Lincoln Business School":
                item['department'] = dep_dict.get(item['department'].lower())
            print("item['department']1: ", item['department'])

            if item['department'] == None:
                item['department'] = ''.join(response.xpath("//div[@class='breadcrumb-list']//span//a[@href='/home/collegeofsocialscience/']//text()").extract()).strip()
                print("item['department']2: ", item['department'])

            # //div[@id='feesTables']/table
            fee = response.xpath("//td[contains(text(),'International')]/following-sibling::td//text()").extract()
            clear_space(fee)
            # print("fee: ", fee)
            feeStr = ''.join(fee)
            tuitionfee = getTuition_fee(feeStr)
            item['tuition_fee'] = tuitionfee
            if item['tuition_fee'] == 0:
                item['tuition_fee'] = None
            else:
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee']: ", item['tuition_fee'])
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            # //h2[contains(text(),'The Course')]/..
            overview = response.xpath("//h2[contains(text(),'The Course')]/..").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])

            modules_en = response.xpath("""//body/section[@class='container basic-accordion']/div[@class='row']/div[@class='col-md-9 no-gutters']/div[@id='accordion']/div[@class="nd_2019-20"]//a[contains(text(),'How you study')]/../../..|
                                        //body/section[@class='container basic-accordion']/div[@class='row']/div[@class='col-md-9 no-gutters']/div[@id='accordion']/div[@class="nd_2019-20"]//a[contains(text(),'How You Study')]/../../..|
                                        //body/section[@class='container basic-accordion']/div[@class='row']/div[@class='col-md-9 no-gutters']/div[@id='accordion']/div[@class="nd_2019-20"]//a[contains(text(),'Modules')]/../../..|
                                        //body/section[@class='container basic-accordion']/div[@class='row']/div[@class='col-md-9 no-gutters']/div[@id='accordion']/div[@class="nd_2019-20"]//a[contains(text(),'Research Areas, Projects & Topics')]/../../..""").extract()
            if len(modules_en) == 0:
                modules_en = response.xpath("""//a[contains(text(),'How you study')]/../../..|
                                        //a[contains(text(),'How You Study')]/../../..|
                                        //a[contains(text(),'Modules')]/../../..|
                                        //a[contains(text(),'Research Areas, Projects & Topics')]/../../..""").extract()
            # 需要去除的多余的内容
            del_modules_en = response.xpath("//div[@id='collapse62019-20']//div[@id='modulePanelPrint']").extract()
            del_modules_en_str = remove_class(clear_lianxu_space(del_modules_en))
            print(modules_en)
            item['modules_en'] = remove_class(clear_lianxu_space(modules_en)).replace(del_modules_en_str, '').strip()
            if item['modules_en'] == "":
                item['modules_en'] = None
                # print("*** modules_en")
            else:
                print("===", item['modules_en'])
                del_cont = re.findall(r"<br>Find out more</p><div><span>.*?</em></span>", item['modules_en'])
                print("del_cont==", del_cont)
                if len(del_cont) > 0:
                    for delc in del_cont:
                        item['modules_en'] = item['modules_en'].replace(delc, '<div>').strip()
            print("item['modules_en']: ", item['modules_en'])

            assessment_en = response.xpath(
                "//a[contains(text(),'How You Are Assessed')]/../../..|//a[contains(text(),'How you are assessed')]/../../..").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            interview_desc_en = response.xpath(
                "//a[contains(text(),'Interviews & Applicant Days')]/../../..").extract()
            item['interview_desc_en'] = remove_class(clear_lianxu_space(interview_desc_en))
            # print("item['interview_desc_en']: ", item['interview_desc_en'])

            rntry_requirements = response.xpath(
                "//a[contains(text(),'Entry Requirements')]/../../..//text()|//a[contains(text(),'Entry requirements')]/../../..//text()").extract()
            item['rntry_requirements'] =clear_lianxu_space(rntry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            ielts = re.findall(r"IELTS.{1,80}",
                               item['rntry_requirements'])
            item['ielts_desc'] = ''.join(ielts).strip()
            # print("item['ielts_desc']: ", item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            career = response.xpath("//div[@id='CourseCareersApms']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            # http://www.lincoln.ac.uk/home/studywithus/internationalstudents/entryrequirementsandyourcountry/china/
            item["require_chinese_en"] = remove_class(clear_lianxu_space(["""<p><strong>Master's</strong></p>
<p>Prospective students require one of the following qualifications:</p>
<ul>
<li>A Chinese degree from a recognised institution with a minimum average grade of 70% (GPA 2.5), some programmes may require 80% or a GPA 3.0</li>
<li>Successful completion of a UK Bachelor degree with a minimum grade of 2:2</li>
<li>Students with a three year Chinese Diploma who have gained at least 3 years full-time relevant work experience may be considered for our MBA programme on a case by case basis</li>
</ul>"""]))
            if item['teach_type'] == "phd":
                item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<p><strong>PhD</strong></p>
<p><span>Successful completion of a Master's Degree from a recognised institution.</span></p>
"""]))
            # print("item['require_chinese_en']: ", item['require_chinese_en'])

            if item['ielts_desc'] == "":
                item['ielts_desc'] = "Prospective students require IELTS 6.0 (with no less than 5.5 in each band score) or an equivalent qualification. Please note that some courses require a higher score."
                item['ielts'] = 6.0
                item['ielts_l'] = 5.5
                item['ielts_s'] = 5.5
                item['ielts_r'] = 5.5
                item['ielts_w'] = 5.5
            # print("******item['ielts_desc']: ", item['ielts_desc'])
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            # http://www.lincoln.ac.uk/home/studywithus/internationalstudents/englishlanguagerequirementsandsupport/englishlanguagerequirements/
            if item['ielts'] == "6.5":
                item['toefl'] = 90
                item['toefl_l'] = 20
                item['toefl_s'] = 22
                item['toefl_r'] = 21
                item['toefl_w'] = 22
            elif item['ielts'] == "7.0":
                item['toefl'] = 100
                item['toefl_l'] = 22
                item['toefl_s'] = 23
                item['toefl_r'] = 23
                item['toefl_w'] = 23
            # print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
            #         item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<h4 class="h2">Follow these five simple steps to apply for a postgraduate course at Lincoln:</h4>
<p class="h2">1. Find your course</p>
<p>On this website you will find an overview of the <a href="/home/studywithus/postgraduatestudy/">postgraduate courses</a> available at the University of Lincoln.</p>
<p>Choose the course you wish to study, making sure you check the entry requirements.</p>
<p>We strongly recommend you attend a <a href="/home/studywithus/opendaysandvisits/postgraduatetasterdays/">Postgraduate Taster Day</a> to find out more.</p>
<p class="h2">2. Check for a closing date</p>
<p>Most of our postgraduate courses have no official closing date for applications. The majority of our taught courses start in September, although some courses have intakes in January or February. Please allow enough time for your application to be considered prior to the start date. If you are an international student you may need to factor in time for your visa application. We would advise you to apply as soon as possible.</p>
<p class="h2">3. Are you eligible for a postgraduate loan or scholarship?</p>
<p>The government has announced a new system of Postgraduate Loans where eligible full-time and part-time students could borrow up to &pound;10,609 towards the cost of a taught postgraduate Master&rsquo;s qualification. <a href="/home/studywithus/postgraduatestudy/feesandfunding/">Visit our Postgraduate Fees and Funding page</a> to find out more. The University of Lincoln also offers a range of postgraduate <a href="/home/studywithus/scholarshipsandbursaries/">scholarships</a>.</p>
<p class="h2">4. Research candidates only - compose your research proposal</p>
<p>If you are applying for a research programme, you will need to draft your research proposal. In your application you will be asked to give a description of the topic or theme you intend to research.</p>
<p class="h2">5. Apply online</p>
<p>When you have found the course you are interested in, go to the course page and click <a href="https://my.lincoln.ac.uk/welcome/pages/login.aspx" target="_blank">&lsquo;Apply Online&rsquo;</a>.</p>
<p>You will need to register with us first to proceed.</p>"""]))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])
            yield item
        except Exception as e:
            with open(item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

