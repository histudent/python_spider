# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space, clear_space_str
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
import requests
from lxml import etree
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.getDuration import getIntDuration,getTeachTime


class UniversityofBristol_PSpider(scrapy.Spider):
    name = "UniversityofBristol_P"
    # allowed_domains = ['baidu.com']
    start_urls = ['https://www.bristol.ac.uk/study/postgraduate/search/']

    def parse(self, response):
        links = response.xpath("//body[@id='bristol-ac-uk']/div[@class='wrapper']/main[@class='content']/div[@class='prog-az-listings full-width']/ul[@class='list-no-style list-half-spacing prog-results-list']/li/a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))
#         links = ["https://www.bristol.ac.uk/study/postgraduate/2018/sci/phd-chemistry/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/health-sciences/phd-oral-dental-sciences/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/sci/phd-geographical-sciences/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/sci/phd-biological-sciences/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/health-sciences/phd-comparative-clinical-anatomy/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/health-sciences/phd-population-health-sciences/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/biomedical-sciences/phd-cellular-molecular-medicine/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/eng/phd-elec-electronic-eng/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/eng/phd-aero-eng/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/sci/phd-experimental-psychology/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/biomedical-sciences/phd-physiology-pharmacology/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/arts/phd-music/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/health-sciences/phd-translational-health-sciences/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/sci/phd-mathematics/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/sci/phd-earth-sciences/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/biomedical-sciences/phd-biochemistry/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/eng/phd-mech-eng/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/sci/phd-physics/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/eng/phd-civil-eng/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/health-sciences/phd-veterinary-sciences/",
# "https://www.bristol.ac.uk/study/postgraduate/2018/eng/phd-computer-science/",]
#         links = ["http://www.bristol.ac.uk/study/postgraduate/2019/ssl/msc-global-operations-and-supply-chain-management/"]
        for link in links:
            # print(link)
            url = "https://www.bristol.ac.uk"+link
            # url = link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "University of Bristol"
        # items['country'] = "England"
        # items["website"] = "https://www.bristol.ac.uk/"
        item['url'] = response.url
        # 授课方式
        # item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        print("===========================")
        print(response.url)
        try:
            # 专业
            course = response.xpath("//h1[@id='pagetitle']/span//text()").extract()
            # print("course = ", course)
            item['programme_en'] = ''.join(course).replace("\n", " ").replace("\r", " ").strip()
            print("item['programme_en']: ", item['programme_en'])

            # degreeaward
            degreeaward = response.xpath("//th[contains(text(),'Awards available')]/following-sibling::td[1]//text()").extract()
            # print("degreeaward = ", degreeaward)
            item['degree_name'] = clear_space_str(''.join(degreeaward))
            print("item['degree_name']: ", item['degree_name'])

            if "phd" in item['degree_name'].lower() or "md" in item['degree_name'].lower():
                item['teach_type'] = "phd"
                if "research" in item['degree_name'].lower():
                    item['teach_type'] += " " + "research"
                item['degree_type'] = 3
            elif "research" in item['degree_name'].lower():
                item['teach_type'] = "research"
                item['degree_type'] = 3
            else:
                item['teach_type'] = "taught"
                item['degree_type'] = 2
            # print("item['degree_type']: ", item['degree_type'])
            # print("item['teach_type']: ", item['teach_type'])

            # duration
            duration = response.xpath("//th[@scope='row'][contains(text(),'Programme length')]/following-sibling::td[1]//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            item['teach_time'] = getTeachTime(''.join(duration))
            # print("item['teach_time']: ", item['teach_time'])

            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[1]
            # print("item['duration']: ", item['duration'])
            # print("item['duration_per']: ", item['duration_per'])

            # location
            location = response.xpath("//th[@scope='row'][contains(text(),'Location of programme')]/following-sibling::td[1]//text()").extract()
            # print("location = ", location)
            item['location'] = clear_space_str(''.join(location))
            # print("item['location']: ", item['location'])

            # startdate
            startdate = response.xpath("//th[@scope='row'][contains(text(),'Start date')]/following-sibling::td[1]//text()").extract()
            clear_space(startdate)
            print("startdate = ", startdate)
            if len(startdate) > 0:
                # item['start_date'] = startdate[-1].strip()
                # print("item['start_date']: ", item['start_date'])
                item['start_date'] = getStartDate(''.join(startdate[-1]))
            print("item['start_date'] = ", item['start_date'])

            # deadline
            deadline = response.xpath("//div[@id='apply']/div[@class='apply-deadline']/p[1]//text()").extract()
            # print("deadline = ", deadline)
            item['deadline'] = getStartDate(''.join(deadline))
            # print("item['deadline']: ", item['deadline'])

            # department
            department = response.xpath("//div[@id='contact']/p[@class='pg-contact-address']/text()").extract()
            clear_space(department)
            # print("department1 = ", department)
            for d in department:
                if "School" in d or "Faculty" in d:
                    item['department'] = d
            # print("item['department']: ", item['department'])
            if item['department'] == "":
                allcontent = response.xpath("//main[@class='content']//text()").extract()
                clear_space(allcontent)
                department_re = re.findall(r"School\sof.{1,30}", ''.join(allcontent), re.I)
                # print("department_re: ", department_re)
                if len(department_re) > 0:
                    item['department'] = department_re[0].strip()
            # print("item['department']1: ", item['department'])

            # overview  //div[@id='programme-overview']//text()
            overview = response.xpath("//div[@id='programme-overview']|//div[@id='pgr-overview']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])

            # tuitionFee   //div[@id='fees']
            tuitionFee = response.xpath("//dt[contains(text(),'Overseas: full-time')]/following-sibling::dd[1]//text()").extract()
            clear_space(tuitionFee)
            print("tuitionFee = ", tuitionFee)
            if len(tuitionFee) > 0:
                item['tuition_fee_pre'] = "£"
                item['tuition_fee'] = int(''.join(tuitionFee[0]).replace("£", "").replace(",", "").strip())

            if item['tuition_fee'] is None:
                tuitionFee1 = response.xpath(
                    "//dl//dt[contains(text(),'Overseas:')]/following-sibling::dd[1]//text()").extract()
                clear_space(tuitionFee1)
                print("tuitionFee1 = ", tuitionFee1)
                if len(tuitionFee1) > 0:
                    item['tuition_fee_pre'] = "£"
                    item['tuition_fee'] = getTuition_fee(''.join(tuitionFee1))
                if item['tuition_fee'] == 0:
                    item['tuition_fee_pre'] = ""
                    item['tuition_fee'] = None
            if item['tuition_fee'] is None:
                print("tuition_fee 为空")
            print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])
            print("item['tuition_fee']: ", item['tuition_fee'])

            # modules   //div[@id='programme-structure']
            modules = response.xpath("//div[@id='programme-structure']|//div[@id='pgr-research-groups']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            print("item['modules_en']: ", item['modules_en'])

            # 学术要求本科特殊专业要求、IELTS
            entryRequirements = response.xpath("//div[@id='entry-requirements']//text()").extract()
            item['rntry_requirements'] = clear_lianxu_space(entryRequirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            ielts = response.xpath("//*[contains(text(),'Profile')]//text()|//div[contains(text(),'IELTS')]//text()").extract()
            item['ielts_desc'] = clear_lianxu_space(ielts)
            # print("item['ielts_desc']: ", item['ielts_desc'])

            if item['ielts_desc'] == "Profile A":
                item['ielts'] = 7.5
                item['ielts_l'] = 7.0
                item['ielts_s'] = 7.0
                item['ielts_r'] = 7.0
                item['ielts_w'] = 7.0
                item['toefl'] = 109
                item['toefl_l'] = 25
                item['toefl_r'] = 25
                item['toefl_s'] = 25
                item['toefl_w'] = 29
            elif item['ielts_desc'] == "Profile B":
                item['ielts'] = 7.0
                item['ielts_l'] = 6.5
                item['ielts_s'] = 6.5
                item['ielts_r'] = 6.5
                item['ielts_w'] = 6.5
                item['toefl'] = 100
                item['toefl_l'] = 24
                item['toefl_r'] = 24
                item['toefl_s'] = 24
                item['toefl_w'] = 24
            elif item['ielts_desc'] == "Profile C":
                item['ielts'] = 6.5
                item['ielts_l'] = 6.5
                item['ielts_s'] = 6.5
                item['ielts_r'] = 6.5
                item['ielts_w'] = 6.5
                item['toefl'] = 92
                item['toefl_l'] = 23
                item['toefl_r'] = 23
                item['toefl_s'] = 23
                item['toefl_w'] = 24
            elif item['ielts_desc'] == "Profile D":
                item['ielts'] = 6.5
                item['ielts_l'] = 6.0
                item['ielts_s'] = 6.0
                item['ielts_r'] = 7.0
                item['ielts_w'] = 7.0
                item['toefl'] = 92
                item['toefl_l'] = 21
                item['toefl_r'] = 21
                item['toefl_s'] = 21
                item['toefl_w'] = 27
            elif item['ielts_desc'] == "Profile E":
                item['ielts'] = 6.5
                item['ielts_l'] = 6.0
                item['ielts_s'] = 6.0
                item['ielts_r'] = 6.0
                item['ielts_w'] = 6.0
                item['toefl'] = 90
                item['toefl_l'] = 20
                item['toefl_r'] = 20
                item['toefl_s'] = 20
                item['toefl_w'] = 20
            elif item['ielts_desc'] == "Profile F":
                item['ielts'] = 6.0
                item['ielts_l'] = 6.5
                item['ielts_s'] = 6.5
                item['ielts_r'] = 6.0
                item['ielts_w'] = 6.0
                item['toefl'] = 86
                item['toefl_l'] = 20
                item['toefl_r'] = 20
                item['toefl_s'] = 20
                item['toefl_w'] = 23
            elif "Profile" not in item['ielts_desc']:
                ieltsDict = get_ielts(item['ielts_desc'])
                item['ielts'] = ieltsDict.get("IELTS")
                item['ielts_l'] = ieltsDict.get("IELTS_L")
                item['ielts_s'] = ieltsDict.get("IELTS_S")
                item['ielts_r'] = ieltsDict.get("IELTS_R")
                item['ielts_w'] = ieltsDict.get("IELTS_W")
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))
            # print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
            #       item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

            # 就业    //div[@id='careers']
            career = response.xpath("//div[@id='careers']").extract()
            # print("department = ", department)
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            require_chinese_en = """<h2 id="pgentryreqs">Entry requirements for postgraduate programmes</h2>
<p>You should&nbsp;<a href="/pg-howtoapply/">apply online</a>&nbsp;for all our postgraduate programmes.</p>
<p>To be considered for admission to postgraduate study at the University of Bristol, the minimum requirement for entry is an undergraduate (Bachelor&rsquo;s) degree that is equivalent to a UK Upper Second Class degree (also known as a 2:1). Please refer to the <a href="http://www.bristol.ac.uk/study/postgraduate/admissions-statements/%20%20%20" target="_blank">Postgraduate Admissions Statements</a> for each programme for individual entry requirements.</p>
<ul>
<li>Applicants who hold a 4-year Bachelor's (Honours) degree from a prestigious university with a minimum of 80% will be considered for admission to a Master's degree.</li>
<li>Applicants who hold a good Master's degree from a prestigious university will be considered for admission to PhD study.</li>
<li>Applicants will be required to meet the English language requirements for the programme. The profile level requirements can be found on the&nbsp;<a href="http://www.bristol.ac.uk/study/language-requirements/" target="_blank">English language requirements for study</a>&nbsp;page.</li>
</ul>"""
            item["require_chinese_en"] = remove_class(require_chinese_en)
            # print("item['require_chinese_en']: ", item['require_chinese_en'])

            # http://www.bristol.ac.uk/study/postgraduate/apply/
            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<p>We offer an online application system for all of our programmes, except the Postgraduate Certificate in Education for which you should <a href="https://www.ucas.com/ucas/teacher-training/ucas-teacher-training-apply-and-track">apply through UCAS</a>.</p>
<p>You can use our online admissions system to:</p>
<ul>
<li>submit all your application details securely online and view your completed application form;</li>
<li>upload supporting documents;</li>
<li>request references electronically;</li>
<li>track the progress of your application;</li>
<li>receive a decision on your application online;</li>
<li>update your contact details (it is important you tell us if you change your home address or email);</li>
<li>receive useful information about the University and your application.</li>
</ul>
<p>If you are unable to make an online application, please contact the Enquiries team on <a href="mailto:choosebristol-pg@bristol.ac.uk">choosebristol-pg@bristol.ac.uk</a>.</p>"""]))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            apply_documents_en = response.xpath("//h3[contains(text(),'English language requirements')]/preceding-sibling::*[position()<last()]").extract()
            item["apply_documents_en"] = remove_class(clear_lianxu_space(apply_documents_en))
            print("item['apply_documents_en']: ", item['apply_documents_en'])
            yield item
        except Exception as e:
            print("异常：", str(e))
            print("报错链接：", response.url)
            with open("scrapySchool_England/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")







