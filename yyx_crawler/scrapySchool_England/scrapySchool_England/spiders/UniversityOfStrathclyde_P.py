import scrapy
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getDuration import getIntDuration,getTeachTime
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts

class UniversityOfStrathclyde_PSpider(scrapy.Spider):
    name = "UniversityOfStrathclyde_P"
    # allowed_domains = ['baidu.com']
    url_start = "https://www.strath.ac.uk"
    start_urls = ['https://www.strath.ac.uk/courses/?delivery=attendance&attendance=full-time&level_ug=false&level_pgr=false']

    def parse(self, response):
        # 获得链接
        contentText = response.text
        taughtUrl = re.findall(r"/courses/postgraduatetaught/.*/", contentText)
        # print(len(taughtUrl))
        # print(taughtUrl)

        for link in taughtUrl:
            url = "https://www.strath.ac.uk" + link
            # url = "https://www.strath.ac.uk/courses/postgraduatetaught/socialworkresearchmethods/"
            # url = "https://www.strath.ac.uk/courses/postgraduatetaught/artificialintelligenceapplications/"
            yield scrapy.Request(url, callback=self.parse_data)
    # def error_back(self, response):
    #     with open("err.txt", "a+") as f:
    #         f.write(response.url+"\n==============")
    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.strath.ac.uk/"
        item["university"] = "University of Strathclyde"
        item['url'] = response.url
        # 授课方式
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        item['location'] = "16 Richmond Street, Glasgow, G1 1XQ"
        print("===========================")
        print(response.url)
        try:
            # 学位类型
            degree_type = response.xpath("//main[@id='content']/section[@class='PGtPage']/header[@class='page-summary has-img']/div[@class='wrap']/h1/span/text()").extract()
            item['degree_name'] = ''.join(degree_type).strip()
            print("item['degree_name'] = ", item['degree_name'])

            # 专业名
            programme = response.xpath(
                "//main[@id='content']/section[@class='PGtPage']/header[@class='page-summary has-img']/div[@class='wrap']/h1/text()").extract()
            # print("programme = ", programme)
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en'] = ", item['programme_en'])

            if "Engineering" in item['programme_en']:
                item['department'] = "Faculty of Engineering"
            elif "Science" in item['programme_en']:
                item['department'] = "Faculty of Science"
            elif "Business" in item['programme_en'] or "Finance" in item['programme_en'] or "Marketing" in item['programme_en']:
                item['department'] = "Strathclyde Business School"
            print("item['department'] = ", item['department'])

            # 课程长度、开学时间、截止日期
            durationTeachtime = response.xpath("//b[contains(text(),'Study mode and duration')]/../text()").extract()
            clear_space(durationTeachtime)
            # print("durationTeachtime: ", durationTeachtime)
            durationTeachtimeStr = ''.join(durationTeachtime)

            item['teach_time'] = getTeachTime(durationTeachtimeStr)
            duration_list = getIntDuration(durationTeachtimeStr)
            # print(duration_list)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])
            # print("item['teach_time'] = ", item['teach_time'])

            start_date = response.xpath("//b[contains(text(),'Start date')]/../text()").extract()
            start_date_str = ''.join(start_date).replace(":", "")
            print("start_date_str = ", start_date_str)
            item['start_date'] = getStartDate(start_date_str)
            if item['start_date'] != "" and item['start_date'] > "06" and "201" not in item['start_date']:
                item['start_date'] = "2018-" + item['start_date']
            elif item['start_date'] != "" and item['start_date'] <= "06" and "201" not in item['start_date']:
                item['start_date'] = "2019-" + item['start_date']
            print("item['start_date'] = ", item['start_date'])


            # 截止日期
            deadline = response.xpath("//b[contains(text(),'Application deadline')]/../text()").extract()
            # print("deadline1 = ", deadline)
            deadline = ''.join(deadline).replace(":", "").strip()
            print("deadline = ", deadline)
            item['deadline'] = getStartDate(deadline)
            if item['deadline'] == '2':
                item['deadline'] = ""
            print("item['deadline'] = ", item['deadline'])

            # 专业描述
            overview = response.xpath("//article[@id='why-this-course']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en'] = ", item['overview_en'])

            # 课程设置、评估方式
            modules = response.xpath("//h3[contains(text(),'Learning & teaching')]/preceding-sibling::*").extract()
            if len(modules) == 0:
                modules = response.xpath("//article[@id='course-content']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            if item['modules_en'] == "":
                print("modules_en 为空")
            # else:
            #     print("item['modules_en'] = ", item['modules_en'])

            assessment_en = response.xpath("//h3[contains(text(),'Learning & teaching')]/preceding-sibling::*[1]/following-sibling::*").extract()
            item["assessment_en"] = remove_class(clear_lianxu_space(assessment_en))
            if item['assessment_en'] == "":
                print("assessment_en 为空")
            # else:
            #     print("item['assessment_en'] = ", item['assessment_en'])

            # 学术要求、英语要求
            rntry_requirements = response.xpath("//article[@id='entry-requirements']//text()").extract()
            item["rntry_requirements"] = clear_lianxu_space(rntry_requirements)
            # print("item['rntry_requirements'] = ", item['rntry_requirements'])


            # ielts = response.xpath("//h3[contains(text(),'English language requirements')]/following-sibling::*[position()<4]//text()").extract()
            # print("ielts: ", ielts)
            ielts_re = re.findall(r"IELTS.{1,80}", ''.join(rntry_requirements))
            # print("ielts_re = ", ielts_re)
            item["ielts_desc"] = ''.join(ielts_re)
            print("item['ielts_desc'] = ", item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            # print(ieltlsrw)
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            if item['ielts'] != None:
                item['ielts'] = item['ielts'].strip('.').strip()
            if item['ielts_l'] != None:
                item['ielts_l'] = item['ielts_l'] .strip('.').strip()
            if item['ielts_s'] != None:
                item['ielts_s'] = item['ielts_s'].strip('.').strip()
            if item['ielts_r'] != None:
                item['ielts_r'] = item['ielts_r'].strip('.').strip()
            if item['ielts_w'] != None:
                item['ielts_w'] = item['ielts_w'] .strip('.').strip()
            print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s "
                  %(item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            # 学费    //article[@id='fees-and-funding']/ul[3]/li
            tuition_fee = response.xpath("//html//article[@id='fees-and-funding']/*[contains(text(),'International')]/following-sibling::*[1]//text()").extract()
            # print("tuition_fee: ", tuition_fee)
            tuition_fee_re = re.findall(r"£[\d,]+", ''.join(tuition_fee))
            # print(tuition_fee_re)
            if len(tuition_fee_re) > 0:
                item['tuition_fee'] = ''.join(tuition_fee_re[0]).replace("£", "").replace(",", "")
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee'] = ", item['tuition_fee'])

            # 就业    //article[@id='careers']
            career = response.xpath("//article[@id='careers']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en'] = ", item['career_en'])

            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<h3>Postgraduate</h3>
<div>GPA from a four-year undergraduate degree must be:</div>
<div>
<ul>
<li>over an average of 70% for 211/985 universities</li>
<li>over an average of 75% for the rest of Chinese universities</li>
</ul>
</div>
<div>Students interested in PhD must usually have a Masters and must include a proposal in their application.</div>
<div>For further information on entry requirements, you can contact our representative Lexy Docwra (<a href="mailto:lexy.docwra@strath.ac.uk">lexy.docwra@strath.ac.uk</a>).</div>"""]))
            print("item['require_chinese_en'] = ", item['require_chinese_en'])

            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<h2>Postgraduate application process</h2>
	<ul>
<li>choose the course you want to apply for &ndash; <a href="http://www.strath.ac.uk/courses/?level_ug=false&amp;level_pgt=true&amp;level_pgr=false">search our postgraduate taught courses</a></li>
<li>check the entry requirements for the course on the course page or in the prospectus</li>
<li>start your application online by clicking on the Apply button on the course page</li>
<li>submit your application along with all supporting documentation &ndash; see our document checklist below. Your application may be delayed if you fail to provide all the required documents</li>
<li>to help you fill in the application form please read our <a href="/media/ps/registry/Applicant_Guide_to_Postgraduate_Taught_Admissions.pdf.pagespeed.ce.p3pCAoLRJ3.pdf" title="" rel="external">Applicant Guide to Postgraduate Taught Admissions</a></li>
<li>once you&rsquo;ve submitted your personal information, you&rsquo;ll receive an email which contains your username and password. Please keep these in a safe place as you&rsquo;ll need them to progress with your application and view any decisions</li>
<li>your application will be considered by the relevant selection team. If they need any further information you&rsquo;ll be contacted</li>
<li>a decision will be made on your application &ndash; we try to make a decision on your application as quickly as possible. In most cases this will be within a minimum of 10 working days (two weeks)</li>
<li>you&rsquo;ll receive an email telling you that a decision has been made on your application. You&rsquo;ll be asked to log in to our online application system (PEGASUS) to view the outcome of your application</li>
</ul>"""]))
            print("item['apply_proces_en'] = ", item['apply_proces_en'])

            item['apply_documents_en'] = remove_class(clear_lianxu_space(["""<h2>Document checklist</h2>
<p>Your application may be delayed if you fail to provide the following documents (where appropriate):</p>
<ul>
<li>certified copies of qualifications you&rsquo;ve gained, eg degree certificate and transcripts (showing the subjects taken and your grades). If you&rsquo;re still studying, provide a transcript of your results so far</li>
<li>if your qualifications are in a language other than English, please provide official translations in addition to the copies of the original documents</li>
<li>if English is not your first language, please provide a suitable English language test certificate (if appropriate), for example IELTS</li>
<li>a copy of your passport (if you are a non EU overseas applicant). Your passport is required in order to obtain your Certificate of Acceptance for Studies (CAS) statement which allows you to apply for your Tier 4 visa to study</li>
<li>a copy of your sponsor letter/scholarship award (if appropriate/available)&nbsp;</li>
<li>copies of any other documentation to support your application such as a CV, Personal Statement, Portfolio (for certain programmes)</li>
</ul>"""]))
            print("item['apply_documents_en'] = ", item['apply_documents_en'])

            yield item
        except Exception as e:
            with open("scrapySchool_England/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)



