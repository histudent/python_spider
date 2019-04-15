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
from scrapySchool_England_Ben.getDuration import getIntDuration

class TheUniversityofEdinburgh_USpider(scrapy.Spider):
    name = "TheUniversityofEdinburgh_U"
    # 研究领域链接
    start_urls = ["https://www.ed.ac.uk/studying/undergraduate/degrees/index.php?action=degreeList"]
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    def parse(self, response):
        links = response.xpath("//div[@id='proxy_leftContent']/div[@class='panel panel-default']/div[@class='list-group']/a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))
        for link in links:
            url = "https://www.ed.ac.uk"+ link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "The University of Edinburgh"
        # item['country'] = 'England'
        # item['website'] = 'https://www.ed.ac.uk/'
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        try:
            # 专业
            programme = response.xpath(
                "//h1[@itemprop='headline']//text()").extract()
            clear_space(programme)
            programme_en = ''.join(programme).strip()


            degree_name = re.findall(r"^.*?\s", programme_en)
            if len(degree_name) > 0:
                item['degree_name'] = degree_name[0].strip()
            print("item['degree_name']: ", item['degree_name'])

            item['programme_en'] = programme_en.replace(item['degree_name'], '').strip()
            print("item['programme_en']: ", item['programme_en'])

            department = response.xpath(
                "//div[@id='proxy_rightSummary']//p//span[contains(text(),'College:')]/../text()").extract()
            clear_space(department)
            item['department'] = ''.join(department).strip()
            # print("item['department']: ", item['department'])

            ucascode = response.xpath(
                "//span[contains(text(),'UCAS code:')]/../text()").extract()
            clear_space(ucascode)
            item['ucascode'] = ''.join(ucascode).strip()
            # print("item['ucascode']: ", item['ucascode'])

            duration = response.xpath(
                "//span[contains(text(),'Duration:')]/../text()").extract()
            clear_space(duration)
            # print("duration: ", duration)

            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration']: ", item['duration'])
            # print("item['duration_per']: ", item['duration_per'])

            # //div[@class='col-xs-12']//div[@class='row']//div[@class='col-xs-12']//ul[@class='addressList']//li[@class='contactCampus']
            # location = response.xpath(
            #     "//div[@class='col-xs-12']//div[@class='row']//div[@class='col-xs-12']//ul[@class='addressList']//li[@class='contactCampus']/text()").extract()
            # clear_space(location)
            item['location'] = '33 Buccleuch Place, City, Edinburgh, Post Code. EH8 9JS'
            # print("item['location']: ", item['location'])

            # # //option[@value='0010']
            # start_date = response.xpath(
            #     "//select[@name='code2']//option//text()").extract()
            # clear_space(start_date)
            # if len(start_date) > 1:
            #     item['start_date'] = start_date[0].strip()
            # # print("item['start_date']: ", item['start_date'])
            # item['start_date'] = getStartDate(item['start_date'])
            # print("item['start_date'] = ", item['start_date'])

            overview = response.xpath(
                "//div[@id='proxy_introduction']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])


            # //div[@id='proxy_collapseprogramme']
            modules = response.xpath(
                "//div[@id='proxy_collapseWhatStudy']/..").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(list(modules)))
            # print("item['modules_en']: ", item['modules_en'])

            assessment_en = response.xpath(
                "//div[@id='proxy_collapseLearning']/..").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            career = response.xpath(
                "//div[@id='proxy_collapseCareers']/..").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            # //div[@id='proxy_collapseentry_req']
            # entry_requirements = response.xpath(
            #     "//div[@id='proxy_collapseentry_req']/..//text()").extract()
            # item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            alevel = response.xpath(
                "//li[contains(text(),'A Levels:')]//text()|//p[contains(text(),'A levels:')]//text()").extract()
            clear_space(alevel)
            if len(alevel) > 0:
                item['alevel'] = ''.join(alevel[-1]).strip()
            print("item['alevel'] = ", item['alevel'])

            # ib = response.xpath(
            #     "//html//ul[1]/li[3]/abbr[contains(text(),'IB')]/..//text()|//p[contains(text(),'IB:')]//text()").extract()
            ib = response.xpath("//html//ul[3]/li[3]/abbr[contains(text(),'IB')]/..//text()|//p[contains(text(),'IB:')]//text()").extract()
            clear_space(ib)
            if len(ib) > 0:
                item['ib'] = ''.join(ib).strip()
            print("item['ib'] = ", item['ib'])

            IELTS = response.xpath("//abbr[contains(text(),'IELTS')]/..//text()").extract()
            item['ielts_desc'] = ''.join(IELTS)
            # print("item['ielts_desc']: ", item['ielts_desc'])

            ieltsDict = get_ielts(item['ielts_desc'])
            item['ielts'] = ieltsDict.get("IELTS")
            item['ielts_l'] = ieltsDict.get("IELTS_L")
            item['ielts_s'] = ieltsDict.get("IELTS_S")
            item['ielts_r'] = ieltsDict.get("IELTS_R")
            item['ielts_w'] = ieltsDict.get("IELTS_W")
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            TOEFL = response.xpath("//abbr[contains(text(),'TOEFL')]/..//text()").extract()
            if len(TOEFL) == 0:
                TOEFL = response.xpath("//*[contains(text(),'TOEFL')]//text()").extract()
            item['toefl_desc'] = ''.join(TOEFL)
            # print("item['toefl_desc']: ", item['toefl_desc'])

            toeflDict = get_toefl(item['toefl_desc'])
            item['toefl'] = toeflDict.get("TOEFL")
            item['toefl_l'] = toeflDict.get("TOEFL_L")
            item['toefl_s'] = toeflDict.get("TOEFL_S")
            item['toefl_r'] = toeflDict.get("TOEFL_R")
            item['toefl_w'] = toeflDict.get("TOEFL_W")
            # print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
            #         item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

            tuition_feeDict = {}
            tuition_fee_url = response.xpath("//html//div[@id='proxy_collapseFees']//p[1]/a/@href").extract()
            print("tuition_fee_url: ", tuition_fee_url)
            if len(tuition_fee_url) > 0:
                tuition_fee_url_str = tuition_fee_url[0]
                fee = self.parse_tuition_fee(tuition_fee_url_str)
                clear_space(fee)
                fee_re = re.findall(r"£\d+,\d+", ''.join(fee))
                print("fee_re: ", fee_re)
                item['tuition_fee'] = getTuition_fee(''.join(fee_re))
                item['tuition_fee_pre'] = "£"
            if item['tuition_fee'] == 0:
                item['tuition_fee'] = None
                item['tuition_fee_pre'] = ""
            print("item['tuition_fee']: ", item['tuition_fee'])

            # https://www.ed.ac.uk/studying/international/country/asia/east-asia/china
            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<p class="lead">Undergraduate entry requirements for students from China.</p>


  <h2>Senior High School Certificate</h2>

<p>Students who have completed the Chinese Senior High School Certificate are required to undertake further study for entry to most subjects as this qualification does not normally meet our minimum entry requirements.</p>

<p>We accept the following qualifications for direct entry to our undergraduate degree programmes:</p>

<ul>
	<li><a class="uoe-node-link uoe-published" href="/studying/undergraduate/entry-requirements/ruk/a-levels" title="A Levels"><abbr title="General Certificate of Education">GCE</abbr> <abbr title="Advanced Level">A Levels</abbr></a></li>
	<li><a class="uoe-node-link uoe-published" href="/studying/undergraduate/entry-requirements/international/ib" >International Baccalaureate</a></li>
	<li><a class="uoe-node-link uoe-published" href="/studying/undergraduate/entry-requirements/scottish-qualifications/highers" title="SQA Highers and Advanced Highers">Scottish qualifications</a></li>
	<li><a class="uoe-node-link uoe-published" href="/studying/international/country/americas/united-states-of-america" title="United States of America"><abbr title="United States">US</abbr> qualifications</a></li>
</ul>

<p>Applicants with qualifications other than those listed above will usually be required to complete a Foundation Year before entering the University.</p>

<p><a class="uoe-node-link uoe-published" href="/studying/international/applying/foundation" title="International Foundation Programme">Foundation year</a></p>

<h2>Science and Engineering</h2>

<p>For degree programmes in Science and Engineering, applicants who have completed a year of study at a leading Chinese University may be eligible to apply.</p>

<p>The College of Science &amp; Engineering will also give consideration to applicants who have achieved excellent results in the Chinese National University Entrance Examination (Gaokao) on an individual basis.</p>

<h2>Further guidance on academic entry requirements</h2>

<p>Each course may have further specific entry requirements. All applicants must meet these requirements. Staff in the Admissions Offices will be able to provide further guidance.</p>

<p><a class="uoe-node-link uoe-published" href="/studying/undergraduate/contacts" title="Contact us with an enquiry about undergraduate study">Undergraduate admissions contacts</a></p>

<h2>English Language requirements</h2>

<p>If your first language is not English, you will also have to meet English Language requirements to apply. These requirements are listed by programme.</p>

<p><a class="uoe-node-link uoe-published" href="/studying/international/english" title="English language requirements">English Language advice</a></p>

<p><a class="uoe-node-link uoe-published" href="/studying/undergraduate/degrees" title="Degree finder">Specific English language requirement by programme</a></p>

<h2>Contact us</h2>

<p>Edinburgh Global's representative for China is Esther Sum.</p>

<p>Esther will help you with admissions advice and support.</p>

<p><a href="mailto:China.Enquiries@ed.ac.uk">Contact us by email - China.Enquiries@ed.ac.uk</a></p>

<h2>Support in your country</h2>

<p><a class="uoe-node-link uoe-published" href="/studying/international/application/our-visits-overseas" title="Our visits overseas">View a list of our overseas visits</a></p>

<p><a class="uoe-node-link uoe-published" href="/studying/international/agents/list/china" title="China">Our agents in your country</a></p>

<h2>Chat to us</h2>

<p>Talk to a member of staff online and view a presentation about study in Edinburgh.</p>

<p><a class="uoe-node-link uoe-published" href="/studying/international/application/chat-to-us-online" title="Online information sessions">Chat to us</a></p>

<h2>Join our mailing list</h2>

<p>We will send you further useful information about the University, admissions and entry.</p>

<p><a href="http://r1.dotmailer-surveys.com/0127judf-2e1gig1f">Join our mailing list </a></p>

<h2>About Edinburgh</h2>

<p><a class="uoe-node-link uoe-published" href="/about" title="About">More information about Edinburgh</a></p>

<p><a class="uoe-node-link uoe-published" href="/global/immigration/applying-for-visa/visa-requirements" >Do I need a visa?</a></p>

<h2>Student numbers</h2>

<p>There are almost 3,000 students students from China currently studying at the University of Edinburgh.</p>
"""]))
            # print("item['require_chinese_en']: ", item['require_chinese_en'])

            item['apply_proces_en'] = "https://www.ed.ac.uk/studying/undergraduate/applying"

            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

    def get_modules2(self, modules2url):
        data = requests.get(modules2url, headers=self.headers)
        response = etree.HTML(data.text)
        modules2 = response.xpath("/html/body/div[@class='container']")
        m2 = etree.tostring(modules2[0], encoding='unicode', pretty_print=False, method='html')
        m2 = remove_class(clear_space_str(m2))
        return m2

    def parse_tuition_fee(self, tuition_fee_url):
        data = requests.get(tuition_fee_url, headers=self.headers)
        response = etree.HTML(data.text)
        fee = response.xpath("//html//table[1]//tr[2]/td//text()")
        return fee
