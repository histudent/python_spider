# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space, clear_space_str
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
import requests
from lxml import etree
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.getDuration import getIntDuration,getTeachTime


class UniversityofBristol_USpider(scrapy.Spider):
    name = "UniversityofBristol_U"
    # allowed_domains = ['baidu.com']
    start_urls = ['https://www.bristol.ac.uk/study/undergraduate/search/']
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    def parse(self, response):
        links = response.xpath("//div[@class='course-az']/div[@class='course-az-listings']/ul[@class='list-no-style list-half-spacing course-results-list']/li/a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))

#         links = ["https://www.bristol.ac.uk/study/undergraduate/2019/philosophy/ba-philosophy-french/",
# "https://www.bristol.ac.uk/study/undergraduate/2019/politics-international-relations/ba-politics-russian/", ]
        for link in links:
            # print(link)
            url = "https://www.bristol.ac.uk"+link
            # url = link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Bristol"
        # items['country'] = "England"
        # items["website"] = "https://www.bristol.ac.uk/"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        try:
            # 专业
            course = response.xpath("//span[@property='programname']//text()").extract()
            # print("course = ", course)
            item['programme_en'] = ''.join(course).replace("\n", " ").replace("\r", " ").strip()
            print("item['programme_en']: ", item['programme_en'])

            # degreeaward
            degreeaward = response.xpath("//span[@property='award']//text()").extract()
            # print("degreeaward = ", degreeaward)
            item['degree_name'] = clear_space_str(''.join(degreeaward))
            print("item['degree_name']: ", item['degree_name'])

            ucascode = response.xpath(
                "//th[contains(text(),'UCAS code')]/../td//text()").extract()
            clear_space(ucascode)
            item['ucascode'] = ''.join(ucascode).strip()
            # print("item['ucascode']: ", item['ucascode'])
            if item['ucascode'] == "":
                ucascode = response.xpath(
                    "//th[contains(text(),'Application method')]/following-sibling::td//text()").extract()
                clear_space(ucascode)
                # print("ucascode1: ", ucascode)
                item['ucascode'] = ''.join(ucascode).replace("Entry by transfer from", "").replace("Entry by transfer after two years from", "").replace("Entry by transfer after year one of", "").replace("at the end of year one", "").strip()
            # print("item['ucascode']1: ", item['ucascode'])

            # duration
            duration = response.xpath("//th[contains(text(),'Course duration')]/../td//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)

            # duration_list = getIntDuration(''.join(duration))
            if len(duration) == 2:
                item['duration'] = int(duration[0])
                if 'y' in ''.join(duration).lower():
                    item['duration_per'] = 1
            # print("item['duration']: ", item['duration'])
            # print("item['duration_per']: ", item['duration_per'])

            # location
            location = response.xpath("//th[contains(text(),'Location of course')]/../td//text()").extract()
            item['location'] = clear_space_str(''.join(location))
            # print("item['location']: ", item['location'])

            # startdate
            startdate = response.xpath("//p[@class='year-of-entry']/text()").extract()
            clear_space(startdate)
            # print("startdate = ", startdate)
            if len(startdate) > 0:
                item['start_date'] = ''.join(startdate).replace("entry", "").strip()
            # print("item['start_date'] = ", item['start_date'])

            tuitionFee = response.xpath("//li[contains(text(),'International students: £')]//text()").extract()
            # print("tuitionFee = ", tuitionFee)
            if len(tuitionFee) > 0:
                item['tuition_fee_pre'] = "£"
                item['tuition_fee'] = getTuition_fee(''.join(tuitionFee))
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])
            # print("item['tuition_fee']: ", item['tuition_fee'])


            # deadline
            # deadline = response.xpath("//div[@id='apply']/div[@class='apply-deadline']/p[1]//text()").extract()
            # # print("deadline = ", deadline)
            # item['deadline'] = getStartDate(''.join(deadline))
            # # print("item['deadline']: ", item['deadline'])

            # department
            department = response.xpath("//div[@id='contact']/p[@class='pg-contact-address']/text()").extract()
            clear_space(department)
            print("department1 = ", department)
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

            overview = response.xpath("//div[@id='course-description']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])

            assessment_en = response.xpath("//div[@id='teaching']|//div[@id='assessment']").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            print("item['assessment_en']: ", item['assessment_en'])

            alevel = response.xpath(
                "//div[@id='typical-offer']//table//tr/th[contains(text(), 'A-level')]/../td//text()").extract()
            clear_space(alevel)
            # print(alevel)
            if len(alevel) > 0:
                item['alevel'] = ''.join(alevel[0]).strip()
            # print("item['alevel'] = ", item['alevel'])

            # print(len("36 points overall with 18 at Higher Level, including 6, 5 at Higher Level in two of the following subjects: Biology, Chemistry, Physics, Mathematics, Psychology"))
            if len(item['alevel']) > 160:
                item['alevel'] = ''.join(item['alevel'][:161])
            # print("item['alevel']1 = ", item['alevel'])

            ib = response.xpath(
                "//div[@id='typical-offer']//table//tr/th[contains(text(), 'International Baccalaureate ')]/../td//text()").extract()
            clear_space(ib)
            if len(ib) > 0:
                item['ib'] = ''.join(ib[0]).strip()

            if len(item['ib']) > 160:
                item['ib'] = ''.join(item['ib'][:161])
            # print("item['ib'] = ", item['ib'])

            # 课程结构
            modulesUrl = response.xpath("//div[@id='course-structure']//div[@class='collapsible']//a/@href").extract()
            # print("modulesUrl: ", modulesUrl)
            modulesUrl = ''.join(modulesUrl).strip()
            if len(modulesUrl) != 0:
                item['modules_en'] = self.parse_modules_en(modulesUrl)[0]
                # print("item['modules_en']: ", item['modules_en'])
                u = self.parse_modules_en(modulesUrl)[1]
                # print(u)
                while len(u)!=0:
                    u1 = "https://www.bris.ac.uk" + ''.join(u)
                    # print("u1=", u1)
                    item['modules_en'] += self.parse_modules_en(u1)[0]
                    u = self.parse_modules_en(u1)[1]
            # print("item['modules_en']1: ", item['modules_en'])

            # 学术要求本科特殊专业要求、IELTS
            entryRequirements = response.xpath("//div[@id='typical-offer']//text()").extract()
            # item['rntry_requirements'] = clear_lianxu_space(entryRequirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            ielts = response.xpath("//*[contains(text(),'Profile A')]//text()|//*[contains(text(),'Profile B')]//text()|"
                                   "//*[contains(text(),'Profile C')]//text()|//*[contains(text(),'Profile D')]//text()|"
                                   "//*[contains(text(),'Profile E')]//text()|//*[contains(text(),'Profile F')]//text()").extract()
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
                item['ielts_w'] = 7.0
                item['toefl'] = 100
                item['toefl_l'] = 24
                item['toefl_r'] = 24
                item['toefl_s'] = 24
                item['toefl_w'] = 27
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
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))
            # print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
            #       item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

            # assessment_en, career_en
            assessCareerUrlSplit = response.url.rsplit('/')
            assessCareerUrl = response.url.replace(assessCareerUrlSplit[-2]+"/", "").strip()
            print(assessCareerUrl)
            assessCareerDict = self.parseAssessCareer(assessCareerUrl)

            item['assessment_en'] = assessCareerDict.get('assessment_en').strip()
            print("item['assessment_en']: ", item['assessment_en'])

            item['career_en'] = assessCareerDict.get('career_en').strip()
            print("item['career_en']: ", item['career_en'])

            # 申请要求
            apply_desc_en = response.xpath("//div[@id='typical-offer']").extract()
            item['apply_desc_en'] = remove_class(clear_lianxu_space(apply_desc_en))
            # print("item['apply_desc_en']: ", item['apply_desc_en'])

            require_chinese_en = """<h2 id="ugentryreqs">Entry requirements for undergraduate courses</h2>
<p>You can apply for undergraduate programmes either through the&nbsp;<a href="http://www.ucas.com/">Universities and Colleges Admissions Service</a>&nbsp;(UCAS) or&nbsp;<a href="http://www.commonapp.org/">The Common Application.</a>&nbsp;Please use only&nbsp;<strong>one</strong>&nbsp;method of applying. If you are using UCAS to apply for other UK universities, please also make your University of Bristol application through UCAS and do not use the Common Application.The UCAS code name and number for this University is BRISL B78.</p>
<p>Individual course entry requirements&nbsp;are listed in our <a href="http://www.bris.ac.uk/study/undergraduate/">Undergraduate Prospectus</a>&nbsp;for each course.</p>
<ul>
<li>Applicants with the Gaozhong Biye Zhengshu (Senior High School Certificate) and Gaokao&nbsp;(Chinese University entrance exam) combined with a successfully completed appropriate <a href="http://www.bris.ac.uk/english-language/study/ifp/" target="_blank">Foundation programme</a> will be considered for admission to our Bachelor's degree courses.</li>
<li>Applicants who have successfully completed the first year of a Chinese University degree at a prestigious university will be considered for admission to the first year of our Bachelor's degree courses.</li>
<li>Applicants will be required to meet the English language requirements for the programme. The profile level requirements can be found on the&nbsp;<a href="http://www.bristol.ac.uk/study/language-requirements/">English language requirements for study</a>&nbsp;page.</li>
</ul>"""
            item["require_chinese_en"] = remove_class(require_chinese_en)
            # print("item['require_chinese_en']: ", item['require_chinese_en'])

            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<h2>How to apply</h2><p>You can apply through Universities and Colleges Admissions Service (UCAS) or the Common Application (Common App). For Engineering Design, Medicine, Dentistry or Veterinary Science courses, you must apply using UCAS.</p> </div> <!-- end: content - how to apply --> <!-- start: drop down - application options --> <div class="main-col-child">  <div class="dropdown"> <h3 class="dropdown-heading">Applying through UCAS</h3> <div class="dropdown-content"> <p>You can apply for a maximum of five courses using the UCAS form. Apply for medicine, dentistry and veterinary courses through UCAS by 15 October. You can only use four of your five UCAS choices to apply to these courses.</p> <p><a class="btn icon-arrow-right" data-tracking-click-url="http://uk.sitestat.com/bristol/bristol-ext/s?study.undergraduate.apply.international.index_html.international-ucas&amp;ns_type=clickout&amp;ns_url=https://www.ucas.com/ucas/undergraduate/getting-started/ucas-undergraduate-international-and-eu-students" href="https://www.ucas.com/ucas/undergraduate/getting-started/ucas-undergraduate-international-and-eu-students">Apply online through UCAS</a><br />Our UCAS institution code is <strong>BRISL B78</strong>.</p> <p>After you have applied, UCAS will give you a ten-digit personal ID number. You will need this if you contact the University about your application.</p> <h4>Entering your qualifications</h4> <p>Before you submit your UCAS application, make sure you have included:</p> <ul> <li><strong>Full details of qualifications you have already taken</strong>: include grades/marks for the academic qualifications you've achieved from age 16 (GCSE or equivalent), and any English language qualifications.</li> <li><strong>Full details of the qualifications you are taking:</strong> include current studies (name and expected date of examination and major subjects), English language qualifications, and any resits of previous qualifications you expect to take.</li> </ul> <p>If your qualification offers different levels of study, state which subjects you are studying at the higher level, and which at the standard level.</p> <p>Watch the <a href="https://www.ucas.com/connect/videos?v=/apply-education-page">UCAS how-to guide on entering qualifications</a>.</p> <h4>When to apply</h4> <p>Find the <a href="https://www.ucas.com/ucas/undergraduate/apply-track/when-apply"><span>application deadlines on the UCAS website</span></a>.</p> </div>   <h3 class="dropdown-heading" >Applying through the Common App</h3> <div class="dropdown-content"> <p>You can use Common App to apply for any full-time undergraduate course at Bristol, except Engineering Design, Medicine, Dentistry or Veterinary Science courses. The deadline for applying through Common App is 30 June 2018.</p> <p><a class="btn icon-arrow-right" data-tracking-click-url="http://uk.sitestat.com/bristol/bristol-ext/s?study.undergraduate.apply.international.index_html.international-common&amp;ns_type=clickout&amp;ns_url=https://www.commonapp.org/" href="https://www.commonapp.org/">Apply online through the Common App</a></p> <p>After you have applied, you will be given an application number. You will need this if you contact the University about your application.</p> </div>   <h3 class="dropdown-heading" >Applying for direct entry courses</h3> <div class="dropdown-content"> <p>These are our direct entry courses. Please apply using these links and not through UCAS:</p> <ul> <li><a href="/dental/courses/dcp/hygiene/apply/">Diploma in Dental Hygiene</a></li> <li><a href="http://www.bristol.ac.uk/english-language/study/ifp/apply/">International Foundation Programme</a></li> <li><a href="/arts/study/foundation/apply/">Foundation in Arts and Humanities</a></li></ul> """]))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])
            yield item
        except Exception as e:
            print("异常：", str(e))
            print("报错链接：", response.url)
            with open("scrapySchool_England_Ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")


    def parse_modules_en(self, modulesUrl):
        data = requests.get(modulesUrl, headers=self.headers)
        response = etree.HTML(data.text)
        modules1 = response.xpath("//a[@class='active']//text()")
        modules2 = response.xpath("//table[@class='table-basic']")
        m2 = ""
        if len(modules2) > 0:
            m2 = "<h2>"+''.join(modules1)+"</h2>"
            m2 += etree.tostring(modules2[0], encoding='unicode', pretty_print=False, method='html')
        m2 = remove_class(clear_space_str(m2))
        y2 = response.xpath("//a[@class='active']/../following-sibling::li[1]/a/@href")
        return [m2, y2]

    def parseAssessCareer(self, assessCareerUrl):
        data = requests.get(assessCareerUrl, headers=self.headers)
        response = etree.HTML(data.text)
        assessCareerDict = {}
        assessment = response.xpath("//h2[contains(text(),'How is this course taught and assessed?')]|//h2[contains(text(),'How is this course taught and assessed?')]/following-sibling::*[position()<6]")
        assessmentStr = ""
        if len(assessment) > 0:
            for ass in assessment:
                assessmentStr += etree.tostring(ass, encoding='unicode', pretty_print=False, method='html')
        assessmentStr = remove_class(clear_space_str(assessmentStr))
        assessCareerDict['assessment_en'] = assessmentStr

        career = response.xpath(
            "//h2[contains(text(),'What are my career prospects?')]|//h2[contains(text(),'What are my career prospects?')]/following-sibling::p")
        careerStr = ""
        if len(career) > 0:
            for ass in career:
                careerStr += etree.tostring(ass, encoding='unicode', pretty_print=False, method='html')
                careerStr = remove_class(clear_space_str(careerStr))
        assessCareerDict['career_en'] = careerStr
        return assessCareerDict


