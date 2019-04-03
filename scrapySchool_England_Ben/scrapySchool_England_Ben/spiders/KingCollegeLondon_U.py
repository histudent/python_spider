import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl

class KingsCollegeLondon_USpider(scrapy.Spider):
    name = "KingsCollegeLondon_U"
    start_urls = ["https://www.kcl.ac.uk/study/subject-areas/index.aspx"]

    def parse(self, response):
        # 获得研究领域链接
        subject_area_links = response.xpath("//html//tr/td/p[1]/a/@href").extract()
        print(len(subject_area_links))
        subject_area_links = list(set(subject_area_links))
        print(len(subject_area_links))
        for sub in subject_area_links:
            url = "https://www.kcl.ac.uk" + sub
            # print(url, "==========================")
            yield scrapy.Request(url, callback=self.parse_url)

    def parse_url(self, response):
        # 筛选研究生的链接
        links = response.xpath("//table/tbody/tr/td//a/@href").extract()
        print(links)

        for link in links:
            if "/study/undergraduate/courses" in link:
                url = "https://www.kcl.ac.uk" + link
                # url = "https://www.kcl.ac.uk/study/undergraduate/courses/physics-with-biophysics-bsc.aspx"
                yield scrapy.Request(url, callback=self.parse_data)
#         links = ["https://www.kcl.ac.uk/study/undergraduate/courses/physics-with-astrophysics-and-cosmology-bsc.aspx",
# "https://www.kcl.ac.uk/study/undergraduate/courses/physics-with-astrophysics-and-cosmology-msci.aspx",
# "https://www.kcl.ac.uk/study/undergraduate/courses/german-and-spanish-with-a-year-abroad--ba.aspx", ]
#         for url in links:
#             yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "https://www.kcl.ac.uk/"
        item['university'] = "King's College London"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        item['location'] = "Strand, London. WC2R 2LS, United Kingdom"
        print("===============================")
        print(response.url)
        try:
            # //div[@id='container']/div[@class='hero clearfix']/div[@class='wrapper']/div[@class='inner']/h1
            # 专业、学位类型
            programmeDegree = response.xpath("//div[@id='container']/div[@class='hero clearfix']/div[@class='wrapper']/div[@class='inner']/h1//text()").extract()
            clear_space(programmeDegree)
            programmeDegreeStr = ''.join(programmeDegree)
            print(programmeDegreeStr)
            degree_type = re.findall(r"(\s\w+)$|(\s\w+\s\(.*\))$|(\s\w+/\w+)$|(\s\w+/\w+/\w+)$", programmeDegreeStr)
            if len(degree_type) > 0:
                degree_type = list(degree_type[0])
            while '' in degree_type:
                degree_type.remove('')
            print("degree_type = ", degree_type)
            item['degree_name'] = ''.join(degree_type).strip()
            programme = programmeDegreeStr.replace(item['degree_name'], '').strip()
            item['programme_en'] = programme
            print("item['degree_name'] = ", item['degree_name'])
            print("item['programme_en'] = ", item['programme_en'])

            ucascode = response.xpath(
                "//strong[contains(text(),'UCAS code')]/following-sibling::*//text()").extract()
            clear_space(ucascode)
            item['ucascode'] = ''.join(ucascode).strip()
            if "," in item['ucascode']:
                item['ucascode'] = item['ucascode'].split(',')[0].strip()
            print("item['ucascode']: ", item['ucascode'])

            # //div[@id='tabs-key-info']/div[@class='tab tab-1 active-tab']/p[2]/span
            duration = response.xpath("//strong[contains(text(),'Duration')]/following-sibling::*//text()").extract()
            durationStr = ''.join(duration)
            print(durationStr)
            # duration_re = re.findall(r"([a-zA-Z0-9]+\s)(year|month|week){1}", durationStr, re.I)
            duration_re = re.findall(r"([a-zA-Z0-9\.]+\s)(year|month|week|yr|yft){1}|([0-9\.]+)(yr|yft|\-month){1}",
                                     durationStr, re.I)
            # print(duration_re)
            d_dict = {"One": "1",
                      "Two": "2",
                      "Three": "3",
                      "Four": "4",
                      "Five": "5",
                      "Six": "6",
                      "Seven": "7",
                      "Eight": "8",
                      "Nine": "9",
                      "Ten": "10",
                      "one": "1",
                      "two": "2",
                      "three": "3",
                      "four": "4",
                      "five": "5",
                      "six": "6",
                      "seven": "7",
                      "eight": "8",
                      "nine": "9",
                      "ten": "10",
                      }
            if len(duration_re) > 0:
                d_int = re.findall(r"\d+", ''.join(duration_re[0]))
                if len(d_int) > 0:
                    item['duration'] = int(''.join(d_int))
                else:
                    d = re.findall(
                        r"(One)|(Two)|(Three)|(Four)|(Five)|(Six)|(Seven)|(Eight)|(Nine)|(Ten)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(ten)",
                        ', '.join(duration_re[0]))
                    # print("d = ", d)
                    if len(d) > 0:
                        item['duration'] = int(d_dict.get(''.join(d[0]).strip()))
                if "y" in ''.join(duration_re[0]) or "Y" in ''.join(duration_re[0]):
                    item['duration_per'] = 1
                elif "m" in ''.join(duration_re[0]) or "M" in ''.join(duration_re[0]):
                    item['duration_per'] = 3
                elif "w" in ''.join(duration_re[0]) or "W" in ''.join(duration_re[0]):
                    item['duration_per'] = 4
            print("item['duration'] = ", item['duration'])
            print("item['duration_per'] = ", item['duration_per'])


            # //div[@id='tabs-key-info']/div[@class='tab tab-2']
            includeDepartment = response.xpath("//div[@class='tab tab-2']//p[contains(text(), 'Faculty')]/span//text()").extract()
            if len(includeDepartment) == 0:
                includeDepartment = response.xpath(
                    "//p[contains(text(), 'Department')]/span//text()").extract()
            clear_space(includeDepartment)
            item['department'] = ''.join(includeDepartment).strip()
            print("item['department'] = ", item['department'])

            # //div[@id='coursepage-overview']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate']
            overview = response.xpath("//div[@id='coursepage-overview']/div[@class='wrapper clearfix']/div[1]").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            print("item['overview_en'] = ", item['overview_en'])

            # //div[@id='coursepage-course-detail']/div[@class='wrapper clearfix']/div
            # modules = response.xpath("//h3[contains(text(),'Course format and assessment')]/preceding-sibling::*").extract()
            modules = response.xpath(
                "//div[@id='coursepage-course-detail']/div[@class='wrapper clearfix']/div[@class='inner right lop-to-measure']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            print("item['modules_en'] = ", item['modules_en'])

            assessment_en = response.xpath(
                "//h3[contains(text(),'Course format and assessment')]/preceding-sibling::*[1]/following-sibling::*|"
                "//h3[contains(text(),'Course Structure & Assessment')]/preceding-sibling::*[1]/following-sibling::*[position()<last()-1]|"
                "//h3[contains(text(),'Teaching style')]/preceding-sibling::*[1]/following-sibling::*[position()<last()-1]|"
                "//*[contains(text(),'Teaching')]/preceding-sibling::*[1]/following-sibling::*[position()<last()-3]|"
                "//*[contains(text(),'TEACHING')]/../preceding-sibling::*[1]/following-sibling::*[position()<last()-3]|"
                "//*[contains(text(),'Teaching')]/../preceding-sibling::*[1]/following-sibling::*[position()<last()-3]|//strong[contains(text(),'Teaching')]/../preceding-sibling::*[1]/following-sibling::*|"
                "//b[contains(text(),'Teaching')]/../preceding-sibling::*[1]/following-sibling::*").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            print("item['assessment_en'] = ", item['assessment_en'])

            alevel = response.xpath(
                "//div[@class='requirements EntryReqs_UKALevel clearfix']//b[contains(text(),'Required grades')]/../following-sibling::p[1]//text()").extract()
            if len(alevel) == 0:
                alevel = response.xpath(
                    "//strong[contains(text(),'A-Level')]/../following-sibling::td[1]//text()").extract()
                if len(alevel) == 0:
                    alevel = response.xpath(
                        "//div[@class='requirements EntryReqs_UKALevel clearfix']//div[@class='required-grades']//text()//text()").extract()
            clear_space(alevel)
            if len(alevel) > 0:
                item['alevel'] = ''.join(alevel).strip()[:160]
            print("item['alevel'] = ", item['alevel'])

            ib = response.xpath(
                # "//div[@class='requirements EntryReqs_UKIB clearfix']//b[contains(text(),'Required grades')]/../following-sibling::p[1]//text()|"
                "//div[@class='requirements EntryReqs_UKIB clearfix']//div[@class='required-grades']//text()").extract()
            if len(ib) == 0:
                ib = response.xpath(
                    "//div[@class='requirements EntryReqs_UKIB clearfix']//b[contains(text(),'Required grades')]/../../text()").extract()
                if len(ib) == 0:
                    ib = response.xpath(
                        "//strong[contains(text(),'International Baccalaureate')]/../following-sibling::td[1]//text()").extract()
            clear_space(ib)
            if len(ib) > 0:
                item['ib'] = ''.join(ib).strip()[:160]
            print("item['ib'] = ", item['ib'])


            # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']
            entry_requirements = response.xpath("//div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[1]//text()").extract()
            # item['rntry_requirements'] =clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements'] = ", item['rntry_requirements'])

            item['require_chinese_en'] = '''<h4><b>Undergraduate entry</b></h4>
<p>The Senior High School Certificate and/or <i>Hui&nbsp;</i><i>Kao</i>&nbsp;are not considered suitable for direct entry to undergraduate study at King's. Applicants may wish to consider taking one of our International Foundation programmes (see below).</p>'''

            # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']
            IELTS = response.xpath("//*[contains(text(),'English')]/../../following-sibling::td[1]//text()|"
                                   "//*[contains(text(),'English')]/../following-sibling::td[1]//text()|"
                                   "//strong[contains(text(),'TOEFL iBT')]/../../following-sibling::td[1]//text()|"
                                   "//*[contains(text(),'English')]//../following-sibling::td[1]//text()").extract()
            clear_space(IELTS)
            # print(IELTS)
            item['ielts_desc'] = ''.join(IELTS).strip()
            item['toefl_desc'] = item['ielts_desc']
            print("item['ielts_desc'] = ", item['ielts_desc'])


            if item['ielts_desc'] == "Band A":
                item["ielts"] = 7.5  # float
                item["ielts_l"] = 7.0  # float
                item["ielts_s"] = 7.0  # float
                item["ielts_r"] = 7.0  # float
                item["ielts_w"] = 7.0
                item["toefl"] = 109  # float
                item["toefl_l"] = 25  # float
                item["toefl_s"] = 25  # float
                item["toefl_r"] = 25  # float
                item["toefl_w"] = 27
            elif item['ielts_desc'] == "Band B" or item['department'] == "The Dickson Poon School of Law" or item['department'] == "Dental Institute" or "Medicine" in item['programme_en']:
                item["ielts"] = 7.0  # float
                item["ielts_l"] = 6.5  # float
                item["ielts_s"] = 6.5  # float
                item["ielts_r"] = 6.5  # float
                item["ielts_w"] = 6.5
                item["toefl"] = 100  # float
                item["toefl_l"] = 23  # float
                item["toefl_s"] = 23  # float
                item["toefl_r"] = 23  # float
                item["toefl_w"] = 25
            elif item['ielts_desc'] == "Band D"  or "Biochemistry" in item['programme_en']:
                item["ielts"] = 6.5  # float
                item["ielts_l"] = 6.0  # float
                item["ielts_s"] = 6.0  # float
                item["ielts_r"] = 6.0  # float
                item["ielts_w"] = 6.0
                item["toefl"] = 92  # float
                item["toefl_l"] = 20  # float
                item["toefl_s"] = 20  # float
                item["toefl_r"] = 20  # float
                item["toefl_w"] = 23
            elif item['ielts_desc'] == "Band E":
                item["ielts"] = 6.0  # float
                item["ielts_l"] = 5.5  # float
                item["ielts_s"] = 5.5  # float
                item["ielts_r"] = 5.5  # float
                item["ielts_w"] = 5.5
                item["toefl"] = 80  # float
                item["toefl_l"] = 20  # float
                item["toefl_s"] = 20  # float
                item["toefl_r"] = 20  # float
                item["toefl_w"] = 20

            if item['ielts_desc'] == "":
                ielts_desc = response.xpath("//strong[contains(text(),'IELTS Academic')]/../../../following-sibling::td[1]//text()").extract()
                item['ielts_desc'] = ''.join(ielts_desc).strip()
            if item['toefl_desc'] == "":
                toefl_desc = response.xpath("//strong[contains(text(),'TOEFL iBT')]/../../following-sibling::td[1]//text()").extract()
                item['toefl_desc'] = ''.join(toefl_desc).strip()

            if item['ielts'] == None:
                ielts_dict = get_ielts(item['ielts_desc'])
                item["ielts"] = ielts_dict.get('IELTS') # float
                item["ielts_l"] = ielts_dict.get('IELTS_L')  # float
                item["ielts_s"] = ielts_dict.get('IELTS_S')   # float
                item["ielts_r"] = ielts_dict.get('IELTS_R')   # float
                item["ielts_w"] = ielts_dict.get('IELTS_W')
            if item['toefl'] == None:
                toefl_dict = get_ielts(item['toefl_desc'])
                item["toefl"] = toefl_dict.get('TOEFL')  # float
                item["toefl_l"] = toefl_dict.get('TOEFL_L')  # float
                item["toefl_s"] = toefl_dict.get('TOEFL_S')  # float
                item["toefl_r"] = toefl_dict.get('TOEFL_R')  # float
                item["toefl_w"] = toefl_dict.get('TOEFL_W')
                    # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']/div[@class='requirements uk clearfix']/div[@class='copy'][2]/p[1]
            application_fee = response.xpath("//h3[contains(text(), 'Application procedure')]/following-sibling::div[1]//text()").extract()
            clear_space(application_fee)
            # print(''.join(application_fee))
            application_fee_re = re.findall(r"application\sfee.*£\d+", ''.join(application_fee))
            print("apply_fee: ", ''.join(application_fee_re))
            af = ''.join(application_fee_re).replace("application fee of", "").replace("£", "").strip()
            if len(af) != 0:
                item['apply_fee'] = int(af)
                item['apply_pre'] = "£"
            print("item['apply_fee'] = ", item['apply_fee'])

            # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']/div[@class='requirements uk clearfix']/div[@class='copy'][2]/p[1]
            application_documents = response.xpath("//h3[contains(text(), 'Personal statement and supporting information')]/following-sibling::div[1]").extract()
            item['apply_documents_en'] = remove_class(clear_lianxu_space(application_documents))
            print("item['apply_documents_en'] = ", item['apply_documents_en'])

            # //div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off expanded']/div[@class='requirements uk clearfix']/div[@class='copy'][2]/p[1]
            deadline = response.xpath("//div[@id='coursepage-entry-requirements']/div[@class='wrapper clearfix']/div[1]/div[@class='requirements uk clearfix']/div[@class='copy'][4]//text()").extract()
            clear_space(deadline)
            print(deadline)
            deadline_str = ''.join(deadline).strip()
            item['deadline'] = getStartDate(deadline_str)
            print("item['deadline'] = ", item['deadline'])

            # //div[@id='coursepage-fees-and-funding']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate lopped-off']/ul[1]/li[2]
            tuition_fee = response.xpath("//p[contains(text(),'The International tuition fee for the 2018-2019 ac')]//text()").extract()
            print("tuition_fee = ", tuition_fee)
            tuition_fee_re = re.findall(r"£\d+,\d+|£\d+|\d+,\d+", ''.join(tuition_fee))
            # print(tuition_fee_re)
            if len(tuition_fee_re) >= 1:
                item['tuition_fee_pre'] = "£"
                item['tuition_fee'] = int(tuition_fee_re[0].replace("£", "").replace(",", "").strip())
            print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])
            print("item['tuition_fee'] = ", item['tuition_fee'])

            # //div[@id='coursepage-career-prospect']/div[@class='wrapper clearfix']/div[@class='inner left lop-to-truncate']
            career = response.xpath("//div[@id='coursepage-career-prospect']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            print("item['career_en'] = ", item['career_en'])

            # //b[contains(text(),'The interview')]/..|//b[contains(text(),'The interview')]/../following-sibling::*[position()<3]
            interview_desc_en = response.xpath("//b[contains(text(),'The interview')]/..|"
                                               "//b[contains(text(),'The interview')]/../following-sibling::*[position()<3]|"
                                               "//b[contains(text(),'Interviewing')]/../following-sibling::*[1]").extract()
            item['interview_desc_en'] = remove_class(clear_lianxu_space(interview_desc_en))
            print("item['interview_desc_en'] = ", item['interview_desc_en'])

            # //b[contains(text(),'Application deadline:')]/..
            deadline = response.xpath("//b[contains(text(),'Application deadline:')]/../text()").extract()
            item['deadline'] = remove_class(clear_lianxu_space(deadline))
            print("item['deadline'] = ", item['deadline'])

            item['apply_proces_en'] = remove_class(clear_lianxu_space([""" <h1>Applying to King&#39;s College London</h1>
<img alt="King's College London lecture at the Strand campus" height="330" width="780" src="/ImportedImages/0Prospectus/undergraduate/apply/generic-page-images/lecturer-2014-strand-6.29.jpg" />
<p><br />We're delighted that you're considering applying to King's. Once you've checked the information and&nbsp;<a class="sys_16" href="https://www.kcl.ac.uk/study/undergraduate/apply/entry-requirements/index.aspx">entry requirements</a>&nbsp;for your chosen course, you will need to follow the correct application procedure, depending on the type of study you're interested in:</p>
<div class="contentpage-accordion clearfix">
<h3 class="accordion-toggle">Undergraduate degree courses (UCAS)</h3>
<div class="accordion-content">
<p class="p1">For all full-time undergraduate higher education courses at universities and colleges in the UK you must make an online application via the Universities and Colleges Admissions Service - more commonly known as&nbsp; <a class="sys_16" href="http://www.ucas.com/">UCAS</a>.<br /><br /></p>
<h4 class="p1"><b>UCAS has three key functions:</b></h4>
<ol>
<li class="p4"><a class="sys_16" href="https://digital.ucas.com/search">Course search</a>:&nbsp;allows you to search for courses throughout the UK. Remember to always check King's&nbsp;online prospectus&nbsp;for the most detailed information on King's courses.</li>
<li class="p4"><a class="sys_16" href="https://www.ucas.com/ucas/undergraduate/register">Apply</a>:&nbsp;the UCAS online application system. You should use this to make your application(s) to King's. 'Apply' will allow you to apply to several different universities and/or courses at once.</li>
<li class="p4"><a class="sys_16" href="https://www.ucas.com/ucas/undergraduate/login">Track</a>:&nbsp;a central tracking system for following the progress of your different applications. King's will also provide you with an account for our own supplementary tracking and messaging system (called King's Apply).</li>
</ol>
<p class="p1">Please read the following guidelines before making your application.</p>
<h4 class="p1"><b><br />Who should use UCAS?</b></h4>
<ul>
<li class="p2">All applicants for full-time undergraduate courses at King's should apply through UCAS (with the exception of applicants from&nbsp; <a class="sys_16" href="http://www.kcl.ac.uk/usa">North America</a>&nbsp;who may use Common App if preferred).</li>
<li class="p2">All applicants for Nursing with registration (graduate entry) PG Dip</li>
<li class="p2">All applicants for Midwifery with registration (graduate entry) PG Dip</li>
</ul>
<p>You can apply through your school or college, or as an individual.</p>
<h4 class="p1"><b><br />When should I apply?</b></h4>
<p class="p2">You can apply to UCAS from 1 September for entry the following autumn, but remember you can start&nbsp; <a title="Undergraduate study" class="sys_0 sys_t0" href="/study/undergraduate/index.aspx">doing your research</a>, attending&nbsp;open days, and preparing your personal statement earlier than this.</p>
<p class="p2">The normal closing date for receipt of applications is&nbsp;15&nbsp;January.&nbsp;However if you are including Oxford or Cambridge, or to Medicine or Dentistry, then the closing date is&nbsp;15 October&nbsp;in the year prior to entry.&nbsp;</p>
<p class="p2">The UCAS website states a more flexible deadline for international students, however, any application received by King's after the above dates is considered late.</p>
<h4 class="p1"><b><br />How do I use UCAS?</b></h4>
<p class="p2">UCAS allows you to apply to a maximum of five courses per year, but only four of those may be Medicine/Dentistry courses.</p>
<p class="p2">You will need to create an account in UCAS 'Apply' and complete an application form. Your application will then be forwarded by UCAS to all of the universities you have applied to for us to consider.</p>
<p class="p2">If you have participated in a King's widening participation scheme such as K+, please ensure you note this in your application as advised by the&nbsp;<a title="Widening Participation" class="sys_0 sys_t0" href="/study/widening-participation/index.aspx">Widening Participation team</a>.</p>
<p class="p2">UCAS has detailed instructions on the&nbsp;<a class="sys_16" href="http://www.ucas.com/how-it-all-works/undergraduate">UCAS website</a>.</p>
<p class="p2">You can also read our&nbsp;<a title="Before you apply" class="sys_0 sys_t7240628" href="/study/undergraduate/apply/faqs/index.aspx">frequently asked questions about applying</a>.<a title="UCAS website" class="sys_16" href="https://www.ucas.com/"><span class="kcl_BigRedButton">Apply now</span></a></p>

</div>



<h3 class="accordion-toggle">Undergraduate degree courses (Common App)</h3>
<div class="accordion-content">

<p>King's College Lon</p>
<h4>UCAS or Common App?</h4>
<p>We will only consider applicants through The Common Application who have not also applied through UCAS.&nbsp;</p>
<h4>Who should use Common App?</h4>
<ul>
<li>Common App is an option to be used by students who will be classified as paying international fees. Therefore Home/EU fee students must use UCAS. Those who are unsure should use UCAS.</li>
</ul>
<ol>
<li>Common App is available for all programmes excluding Physiotherapy, Nursing, Medicine, Dentistry, and Nutrition and Dietetics. Students must use UCAS to apply to these programmes.</li>
<li>Students must apply to no more than a combined total of five courses (UCAS and Common App) within the UK.</li>
</ol>
<p>All Common App applicants will be expected to complete the supplement element of the Common Application. We strongly encourage students to submit their application by January 15, but the College may consider later applications up to May 1. Once a Common Application is submitted to King's, students will be registered on the College's MyApplication system through which they will be able to track the progress of their application.</p>
<h4>King&rsquo;s College London Common Application timeline</h4>
<ol>
<li>Applicant applies to King&rsquo;s using the&nbsp;<a class="sys_16" href="http://www.commonapp.org/">Common Application form</a>.</li>
<li>The application is transferred onto the KCL Admissions Portal by King&rsquo;s admissions staff. This process may take approximately 30 days, depending upon when you submitted your application.</li>
<li>Once the application has been successfully inputted into the system, the applicant receives login details for the &lsquo;<a class="sys_16" href="https://myapplication.kcl.ac.uk/">MyApplication</a>&rsquo; admissions portal. This is used to track the progress of an application and communicate with admissions staff</li>
<li>Applicants will be contacted through&nbsp;<a class="sys_16" href="https://myapplication.kcl.ac.uk/">myApplication</a>&nbsp;in the event that any further supporting documents are required before the application can be fully processed.</li>
<li>Decisions on completed applications submitted by January 15 will be made before March 31st. All notifications of decisions will be sent through&nbsp;<a class="sys_16" href="https://myapplication.kcl.ac.uk/">myApplication</a>.</li>
</ol>
<p>&nbsp;</p>

</div>



<h3 class="accordion-toggle">Post Qualification Nursing BSc Programmes &amp; Free Standing Courses</h3>
<div class="accordion-content">

<p>Applications for our post qualification nursing BSc programmes should be made direct to King&rsquo;s, through the King&rsquo;s Apply portal. <a title="Apply now" class="sys_16" onclick="void(window.open('https://apply.kcl.ac.uk/','','toolbar=yes,menubar=yes,location=yes,scrollbars=yes,status=yes,resizable=yes'));return false;" onkeypress="void(window.open('https://apply.kcl.ac.uk/','','toolbar=yes,menubar=yes,location=yes,scrollbars=yes,status=yes,resizable=yes'));return false;" href="https://apply.kcl.ac.uk/"><span class="kcl_BigRedButton">Apply now</span></a></p>

</div>



<h3 class="accordion-toggle">Intercalated BScs (iBScs)</h3>
<div class="accordion-content">

<p>Intercalated BScs (iBScs) programmes are for medical, dental and veterinary students. If you are from another university and you are interested in studying an iBSc at King&rsquo;s, then please see our detailed information on <a title="Intercalated BScs: How to apply" class="sys_0 sys_t7240628" href="/study/subject-areas/intercalated/how-to-apply.aspx">how to apply</a>. If you are a current King&rsquo;s student, please refer to application information on the <a class="sys_16" href="https://internal.kcl.ac.uk/lsm/students/ug/intercalated-bsc/how-to-apply.aspx">King's internal website</a>.<a title="King&#39;s Apply" class="sys_16" href="https://apply.kcl.ac.uk/"><span class="kcl_BigRedButton">Apply now</span></a></p>

</div>



<h3 class="accordion-toggle">Transfers to undergraduate degree courses</h3>
<div class="accordion-content">

<p>Some of our academic departments may consider transfer applications from suitably qualified students currently attending other universities. Visit the&nbsp;<a class="sys_0 sys_t2452" href="https://www.kcl.ac.uk/study/undergraduate/apply/transferring-to-kings.aspx">transferring to King&rsquo;s web page</a>&nbsp;for more information. Transfer applications must be submitted through UCAS</p>
<p><a title="UCAS" class="sys_16" href="https://www.ucas.com/"><span class="kcl_BigRedButton">Apply now</span></a></p>

</div>



<h3 class="accordion-toggle">King's International Foundation Programme</h3>
<div class="accordion-content">

<p>Applications for our one year full-time International Foundation academic preparation course should be made direct to King's, through the <a class="sys_16" href="https://apply.kcl.ac.uk/">King&rsquo;s Apply portal</a>. We have detailed guidance on the supporting documentation needed for your application on the relevant International Foundation Programme course web page.<a title="King&#39;s Apply" class="sys_16" href="https://apply.kcl.ac.uk/"><span class="kcl_BigRedButton">Apply now</span></a></p>

</div>



<h3 class="accordion-toggle">Study Abroad</h3>
<div class="accordion-content">

<p>King's welcomes students currently enrolled in universities outside the UK to <a title="King&#39;s Apply" class="sys_16" href="https://apply.kcl.ac.uk/">participate</a> on a study abroad programme.&nbsp;</p>
<p>You can study abroad at King's either as an exchange or a study abroad fee-paying student for the full academic year (starting in September) or for one semester only (September-December or January-June).&nbsp;</p>
<p>Visit our&nbsp;<a class="sys_16" title="Study abroad" href="/study/abroad/index.aspx">Study Abroad web pages</a>&nbsp;to find out more.<a title="King&#39;s Apply" class="sys_16" href="https://apply.kcl.ac.uk/"><span class="kcl_BigRedButton">Apply now</span></a></p>

</div>


</div>

<h3><br />After you&rsquo;ve applied</h3>
<p>Your application can be tracked using our&nbsp;<a class="sys_16" title="King&#39;s application portal" onclick="void(window.open('https://myapplication.kcl.ac.uk/',''));return false;" onkeypress="void(window.open('https://myapplication.kcl.ac.uk/',''));return false;" href="https://myapplication.kcl.ac.uk/">online portal, King's Apply</a>, where you can:</p>
<ul>
<li>
<p>see offer details</p>
</li>
<li>
<p>check if you&rsquo;ve been invited to interview</p>
</li>
<li>
<p>apply for accommodation</p>
</li>
<li>
<p>learn more about the &lsquo;points-based&rsquo; visa system</p>
</li>
</ul>
<p>After you have applied to King's, we will send you a username and password so you can access these pages. To contact us about your application during the application year, please use our <a title="King&#39;s application portal" class="sys_16" onclick="void(window.open('https://myapplication.kcl.ac.uk/',''));return false;" onkeypress="void(window.open('https://myapplication.kcl.ac.uk/',''));return false;" href="https://myapplication.kcl.ac.uk/">online portal, King's Apply</a>&nbsp;.</p>
<p><a class="sys_0 sys_t2452" title="Tracking your application" href="https://www.kcl.ac.uk/study/undergraduate/apply/faqs/tracking-your-application.aspx">Read our FAQs on tracking your application</a></p>


<div class="contentpage-accordion clearfix">
<br />


<h3 class="accordion-toggle">Cancellation rights</h3>
<div class="accordion-content">

<p class="MRNoHead2">Please note, these terms and conditions apply to all levels of study.&nbsp; For applications to undergraduate study, we also advise applicants to contact UCAS directly for details of your cancellation rights.</p>
<p class="MRNoHead2">1.1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; You have the right to cancel your acceptance of a place at King&rsquo;s for any reason (including if you change your mind) during a fourteen (14) day cancellation period (the &ldquo;Cancellation Period&rdquo;), which will start on the day you accept an offer from King&rsquo;s.</p>
<p class="MRNoHead2">1.2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; To cancel your acceptance, you must clearly inform us in writing of your decision to cancel before the Cancellation Period has expired. We ask that you do this by sending a message through &ldquo;King&rsquo;s Apply&rdquo;. Alternatively, you may contact the King&rsquo;s Admissions Office by letter or email. You may also use the <a title="Cancellation Form - Kings College London" class="sys_17" href="/study/assets/word/admissions/v.2-cancellation-form.docx">Cancellation Form </a>to notify us of your decision to cancel.</p>
<p class="MRNoHead2">1.3 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; To meet the cancellation deadline, it is sufficient for you to send your communication concerning your exercise of the right to cancel before the Cancellation Period has expired. We do not have to have received it before the expiry of the Cancellation Period.</p>
<p class="MRNoHead2">1.4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; If you cancel your acceptance within the 14 day Cancellation Period, we will reimburse any tuition fee payment including any deposit received from you as soon as we can, and no later than 14 days after the day on which you informed us of your decision to cancel your acceptance.</p>

</div>


</div>

"""]))
            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

