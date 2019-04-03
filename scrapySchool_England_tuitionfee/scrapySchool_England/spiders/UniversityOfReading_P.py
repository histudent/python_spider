import scrapy
import re
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space, clear_space_str
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getDuration import getIntDuration, getTeachTime
import requests
from lxml import etree

class UniversityOfReading_PSpider(scrapy.Spider):
    name = "UniversityOfReading_P"
    start_urls = ["https://www.reading.ac.uk/"]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3472.3 Safari/537.36"}

    def parse(self, response):
        links = response.xpath("//article[2]//ul[@class='accordion single-display']/li//ul//a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))

        for link in links:
            url = "http://www.reading.ac.uk" + link
            yield scrapy.Request(url, callback=self.parse_url)

    def parse_url(self, response):
        department = response.xpath("//p[@class='paddingtop22 nopaddingbottom']/strong/a//text()").extract()
        department = ''.join(department).strip()

        links = response.xpath("//section/ul[@class='no-indent']/li/p[@class='pad-none']/a/@href").extract()
        # links = ["http://www.reading.ac.uk/ready-to-study/study/subject-area/animal-sciences-pg.aspxentomology.aspx",
        #          "http://www.icmacentre.ac.uk/programmes/msc-capital-markets-regulation-compliance/",
        #          "http://www.reading.ac.uk/ready-to-study/study/subject-area/politics-and-international-relations-pg/ma-diplomacy.aspx",
        #          "http://www.reading.ac.uk/ready-to-study/study/subject-area/typography-and-graphic-communication-pg/ma-information-design.aspx",
        #          "https://www.icmacentre.ac.uk/programmes/msc-international-securities-investment-banking/",
        #          "http://www.icmacentre.ac.uk/programmes/msc-international-shipping-finance/",
        #          "http://www.reading.ac.uk/ready-to-study/study/subject-area/real-estate-and-planning-ug/bsc-real-estate.aspx",
        #          "http://www.reading.ac.uk/ready-to-study/study/subject-area/real-estate-and-planning-ug/bsc-investment-and-finance-in-property.aspx", ]
        # links = ["http://www.reading.ac.uk/ready-to-study/study/subject-area/finance-pg/mres-economic-history-research.aspx"]
        for link in links:
            url = "http://www.reading.ac.uk" + link
            # url = link
            yield scrapy.Request(url, callback=self.parse_data, meta={"department": department})

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "University of Reading"
        # item['country'] = 'England'
        # item['website'] = 'http://www.reading.ac.uk/'
        item['url'] = response.url
        # 授课方式
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        print("===========================")
        print(response.url)
        try:
            # 专业、学位类型、ucas_code
            programmeDegree_typeUcascode = response.xpath(
                "//span[@class='text-bg-standout text-nice-wrap']/text() | //h1[@id='heading']//text() | //h1[@class='hero-heading']//text() | //h1[@class='block-heading block-heading-l5 block-heading-b5 block-heading-md-l-reset cell-md-t0']//text()").extract()
            clear_space(programmeDegree_typeUcascode)
            programmeDegree_typeUcascode = ''.join(programmeDegree_typeUcascode).strip()
            # print("programmeDegree_typeUcascode: ", programmeDegree_typeUcascode)

            degree_type = re.findall(r"^\w+/\w+", programmeDegree_typeUcascode)
            if len(degree_type) == 0:
                degree_type = re.findall(r"^\w+", programmeDegree_typeUcascode)
            # print("degree_type: ", degree_type)
            item['degree_name'] = ''.join(degree_type)
            print("item['degree_name']: ", item['degree_name'])

            programme = programmeDegree_typeUcascode.replace(item['degree_name'], '').strip()
            item['programme_en'] = programme.title()
            # print("item['programme_en']: ", item['programme_en'])

            # duration
            durationMode = response.xpath(
                "//h2[@class='row-margin-small text-weight-medium text-size-25']/text() | //strong[contains(text(),'Duration')]/../text() | //h3[contains(text(),'Programme length:')]/following-sibling::p[1]//text()").extract()
            clear_space(durationMode)
            # print("durationMode: ", durationMode)
            durationMode = ''.join(durationMode)
            # if ":" in durationMode:
            #     duration = durationMode.split(":")[-1].strip()
            #     mode = durationMode.split(":")[0].strip()
            #     item['duration'] = duration
            duration_list = getIntDuration(''.join(durationMode))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            item['teach_time'] = getTeachTime(''.join(durationMode))
            # print("item['duration']: ", item['duration'])
            # print("item['teach_time']: ", item['teach_time'])
            # print("item['duration_per']: ", item['duration_per'])

            start_date = response.xpath("//p[@class='headline'][contains(text(), 'Start date')]//text()").extract()
            # print(start_date)
            item['start_date'] = getStartDate(''.join(start_date))
            # print("item['start_date']: ", item['start_date'])

            overview2 = response.xpath(
                "//div[@class='m-bg-white m-pad-around m-pull-left-normal m-pull-up']//div[@class='theme-editor'] | //div[@id='top-courseOverview'] | //html//div[@id='top-programmeOverview']/h2[1]/following-sibling::div[1] | //div[@id='tc1']").extract()
            overview = remove_class(clear_lianxu_space(overview2))
            item['overview_en'] = overview
            print("item['overview_en']: ", item['overview_en'])

            # department
            department = response.xpath(
                "//article[@class='pad-around bg-white']//div[@class='theme-editor']//a//text()|//p[@class='paddingtop22 nopaddingbottom']//a//text()|//a[@class='navbar-brand navbar-brand-hbs']//text()").extract()
            clear_space(department)
            if department == "":
                item['department'] = response.meta.get('department')
            else:
                item['department'] = ', '.join(department).strip()
            item['department'] = item['department'].replace("How to apply", "")
            # print("item['department']: ", item['department'])

            item['location'] = "Whiteknights,PO Box 217,Reading, Berkshire,RG6 6AH"
            # //h2[@id='Panel1Trigger']/../..
            entry_requirements = response.xpath(
                "//h2[@id='Panel1Trigger']/../..//text()|//div[@id='bottom-entryRequirements']/..//text()|//div[@id='tc5']//text()").extract()
            if len(entry_requirements) == 0:
                entry_requirements = response.xpath("//h4[contains(text(),'Entry requirements:')]/preceding-sibling::*[1]/following-sibling::*[position()<4]//text()").extract()
            clear_space(entry_requirements)
            entry = ''.join(entry_requirements)
            item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            if item['rntry_requirements'] == "":
                print("rntry_requirements 为空")
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            ielts = re.findall(r"IELT.{1,100}", entry)
            # ielts = response.xpath(
            #     "//strong[contains(text(),'IELTS')]/..//text()").extract()
            # # if item['ielts_desc'] == "":
            clear_space(ielts)
            item['ielts_desc'] = ''.join(ielts).strip()
            # if item['ielts_desc'] == "":
            #     print("ielts_desc 为空")
            # print("item['ielts_desc']1: ", item['ielts_desc'])
            ieltsDict = get_ielts(item['ielts_desc'])
            item['ielts'] = ieltsDict.get("IELTS")
            item['ielts_l'] = ieltsDict.get("IELTS_L")
            item['ielts_s'] = ieltsDict.get("IELTS_S")
            item['ielts_r'] = ieltsDict.get("IELTS_R")
            item['ielts_w'] = ieltsDict.get("IELTS_W")
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            toefl = re.findall(r"TOEFL[\s\(\)\w:\.]{1,300}", entry)
            # print(ielts)
            if item['toefl_desc'] == "":
                item['toefl_desc'] = ''.join(toefl)
            # print("item['toefl_desc']: ", item['toefl_desc'])
            toeflDict = get_toefl(item['toefl_desc'])
            item['toefl'] = toeflDict.get("TOEFL")
            item['toefl_l'] = toeflDict.get("TOEFL_L")
            item['toefl_s'] = toeflDict.get("TOEFL_S")
            item['toefl_r'] = toeflDict.get("TOEFL_R")
            item['toefl_w'] = toeflDict.get("TOEFL_W")
            # print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
            #         item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

            # //h2[@id='Panel1Trigger']/../..
            modules = response.xpath(
                "//h2[@id='Panel2Trigger']/../..|//div[@id='bottom-courseContent']/..|//div[@id='page_content_wrap']/following-sibling::div[position()<3]|//strong[contains(text(),'Programme structure')]/../following-sibling::*").extract()
            if len(modules) == 0:
                modules = response.xpath(
                    "//h4[contains(text(),'Programme structure and content')]/preceding-sibling::*[1]/following-sibling::*[position()<11]").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            print("item['modules_en']: ", item['modules_en'])

            # //h2[@id='Panel1Trigger']/../..
            career = response.xpath(
                "//h2[@id='Panel4Trigger']/../following-sibling::div[1]|//div[@id='bottom-careers']/..|//div[@id='careers']|//h3[contains(text(),'Careers')]/..").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            print("item['career_en']: ", item['career_en'])

            # //h3[@class='row-margin-small text-weight-medium'][contains(text(),'How much will it cost?')]/following-sibling::p[2]
            tuition_fee = response.xpath(
                "//h3[@class='row-margin-small text-weight-medium'][contains(text(),'How much will it cost?')]/following-sibling::p[2]//text()|"
                "//html//div[@id='bottom-feesFunding']//tr[2]/td[3]//text()|"
                "//html//div[@id='bottom-feesFunding']//tr[2]/td[2]//text()|"
                "//html//div[@id='tc2']//h3[1]/following-sibling::p[1]//text()|"
                "//*[contains(text(),'Programme fee')]/following-sibling::*[1]//text()|"
                "//h2[contains(text(),'Fees')]/following-sibling::p[1]//h2[contains(text(),'Fees')]/following-sibling::p[1]|"
                "//h2[contains(text(),'Fees')]/following-sibling::p[position()<3]//text()|"
                "//p[contains(text(),'New international students:')]//text()").extract()
            clear_space(tuition_fee)
            # print(tuition_fee)
            # item['tuition_fee'] = ''.join(tuition_fee).strip()
            tuition_fee_re = re.findall(r"\d+,\d+", ''.join(tuition_fee))
            # print(tuition_fee_re)
            if len(tuition_fee_re) == 1:
                item['tuition_fee'] = int(''.join(tuition_fee_re[0]).replace("£", "").replace(",", "").strip())
                item['tuition_fee_pre'] = "£"
            if len(tuition_fee_re) >= 2:
                item['tuition_fee'] = int(''.join(tuition_fee_re[1]).replace("£", "").replace(",", "").strip())
                item['tuition_fee_pre'] = "£"
            # if item['tuition_fee'] is None:
            #     print("tuition_fee 为空")
            # print("item['tuition_fee']: ", item['tuition_fee'])
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            # //div[@id='top-howWeTeachYou']
            assessment_en = response.xpath(
                "//div[@id='top-howWeTeachYou']").extract()
            item['assessment_en'] =remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            item['apply_proces_en'] = """<div><h1><span>How to apply for postgraduate courses</span></h1></div><div><h4>Postgraduate taught courses</h4><p>The quickest and easiest away to apply for postgraduate study at the University of Reading is through our <a>online application service</a>. The online service allows you to complete your application form and attach electronic copies of your academic transcripts, certificates and other supporting information. It also provides a tool for sending an email request to your referees, enabling them to send your supporting references directly to us.</p><p><span>If you are unable to apply online you can request a paper application form by telephoning </span><a>+44 (0) 118 378 5289</a><span> or writing to:</span></p><p>Admissions Office<br>University of Reading<br>Miller Building<br>Whiteknights<br>Reading, RG6 6AB<br>UK</p><h4>PGCE and School Direct</h4><p>Candidates for the PGCE and School Direct courses should submit an application via <a>UCAS Teacher Training</a>.</p><strong> Postgraduate research </strong><p>For more information on applying for postgraduate research opportunities, please visit our <a>graduate school website</a>.</p></div><div><div><div><h4>Entry requirements</h4><p>Please visit our <a>postgraduate entry requirements</a> page for information on academic qualifications and English language requirements.</p><h4>When to apply</h4><p>There is no specific deadline date for most courses and applications will be considered until the course is full. However, to allow time for us to process your application we recommend that you apply by the following dates for admission in September:</p><div><strong>UK applicants</strong> by 1 August</div><div><strong>International applicants</strong> by 1 June</div><div><br></div><p>Please note that the MSc Speech and Language Therapy has an earlier application deadline of 1 December. Applications for PGCE courses are made through UCAS (see above) and the deadline is 15 September of the year of entry though early applications are recommended.</p><p>Most of our taught courses start at the beginning of the autumn term (in September) but there are a number that also have a start at a different time of the year or have multiple starts throughout the year. Please see the individual subject pages for further details.</p><h4>After you apply</h4><p>As soon as you have submitted your&nbsp;completed application we will send&nbsp;you an email acknowledgement.&nbsp;We will also create an applicant&nbsp;account for you which will allow&nbsp;you to check on the progress of&nbsp;your application online and access&nbsp;other useful information about&nbsp;the University of Reading.</p><p> We aim to reach a decision on&nbsp;your application within 4 weeks.&nbsp;The length of time taken to reach&nbsp;a decision will vary as each&nbsp;application is considered on an individual basis according to your&nbsp;relevant strengths and merits. Once your application has been&nbsp;considered you will receive an&nbsp;email from the Admissions Office&nbsp;informing you of the decision. If&nbsp;your application has been successful,&nbsp;our email will explain the offer and&nbsp;any conditions attached to it and also&nbsp;give further details of the fees and&nbsp;other expenses associated with your&nbsp;course.&nbsp;</p><p>Our team of experienced&nbsp;admissions staff is here to help you&nbsp;throughout the application process&nbsp;so please do not hesitate to get in&nbsp;touch with us if you need any help&nbsp;with completing your application or&nbsp;have a question about the progress&nbsp;of your application. You can contact&nbsp;us at <a>pgadmissions@reading.ac.uk</a>.</p></div></div>"""

            yield item
        except Exception as e:
            with open("scrapySchool_England/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a+',
                      encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

