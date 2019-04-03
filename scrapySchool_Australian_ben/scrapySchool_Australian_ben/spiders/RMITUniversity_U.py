# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_Australian_ben.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_ben.getItem import get_item
from scrapySchool_Australian_ben.getTuition_fee import getTuition_fee
from scrapySchool_Australian_ben.items import ScrapyschoolAustralianBenItem
from scrapySchool_Australian_ben.remove_tags import remove_class
from scrapySchool_Australian_ben.getStartDate import getStartDate, getStartDateMonth
from scrapySchool_Australian_ben.getDuration import getIntDuration
from scrapySchool_Australian_ben.getIELTS import get_ielts, get_toefl
import requests
from lxml import etree

# 2019/03/21 星期四 数据更新
class RMITUniversity_USpider(scrapy.Spider):
    name = "RMITUniversity_U"
    # start_urls = ["https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study"]
    start_urls = ["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees",
                  "https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        links = response.xpath("//a[contains(text(),'Bachelor of')]/@href").extract()
        # 组合字典
        programme_dict = {}
        programme_list = response.xpath(
            "//a[contains(text(),'Bachelor of')]//text()").extract()
        clear_space(programme_list)

        for link in range(len(links)):
            url = "https://www.rmit.edu.au" + links[link]
            programme_dict[url] = programme_list[link]

        print(len(links))
        links = list(set(links))
        print(len(links))
        # links = ["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bh072",
        #          "https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bp023",
        #          "https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bp134",
        #          "https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bp148",
        #          "https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bh071", ]

        for link in links:
            url = "https://www.rmit.edu.au" + link
            # url = link
            yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "RMIT University"
        # item['country'] = 'Australia'
        # item['website'] = 'https://www.rmit.edu.au'
        item['url'] = response.url
        item['degree_type'] = 1
        item['major_type1'] = response.meta.get(response.url)
        print("===========================")
        print(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            programme = response.xpath("//h1[@id='course-name']//text()|//h1[@class='highLight program-header']//text()").extract()
            clear_space(programme)
            item['degree_name'] = ''.join(programme).strip()
            if item['degree_name'] == "":
                print("***degree_name为空")
            print("item['degree_name']: ", item['degree_name'])

            pro_re = re.findall(r"Bachelor", item['degree_name'])
            # print("pre_re: ", pro_re)
            if len(pro_re) < 2:
                programme_re = re.findall(r"\(.+\)", item['degree_name'].replace("(Honours)", ""))
                if len(programme_re) > 0:
                    item['programme_en'] = ''.join(programme_re).replace("(", "").replace(")", "").strip()
                else:
                    item['programme_en'] = item['degree_name'].replace("Bachelor of", "").strip()
                print("item['programme_en']: ", item['programme_en'])

                location = response.xpath("//span[@class='icon-location']/..//text()|"
                                          "//h4[@class='description'][contains(text(),'Location')]/following-sibling::*//text()").extract()
                clear_space(location)
                item['location'] = ' '.join(location).strip()
                if item['location'] == "":
                    print("***location为空")
                print("item['location']: ", item['location'])

                duration = response.xpath("//div[@class='b-program-content links b-international']//span[@class='icon-clock']/..//text()|"
                                          "//div[@class='b-program-content links b-international  ']//span[@class='icon-clock']/..//text()|"
                                          "//div[contains(@class,'box b-international not-hide col-xs-12')]//h4[@class='description'][contains(text(),'Duration')]/following-sibling::*//text()").extract()
                clear_space(duration)
                item['duration'] = ''.join(duration).strip()
                # if item['duration'] == "":
                #     print("***duration为空")
                # print("item['duration']: ", item['duration'])

                tuition_fee = response.xpath("//div[contains(@class,'b-program-content links b-international')]//span[@class='icon-fees']/..//text()|"
                                             "//div[contains(@class,'b-program-content links b-international  ')]//span[@class='icon-fees']/..//text()|"
                                             "//div[contains(@class,'box b-international not-hide col-xs-12')]//h4[@class='description'][contains(text(),'Fees')]/following-sibling::*//text()").extract()
                clear_space(tuition_fee)
                tuition_fee = getTuition_fee(''.join(tuition_fee))
                item['tuition_fee'] = tuition_fee
                if item['tuition_fee'] == 0:
                    item['tuition_fee'] = None
                # print("item['tuition_fee']: ", item['tuition_fee'])

                start_date = response.xpath("//div[@class='b-program-content links b-international']//span[@class='icon-intake']/..//text()|"
                                            "//div[@class='b-program-content links b-international  ']//span[@class='icon-intake']/..//text()|"
                                            "//div[contains(@class,'box b-international not-hide col-xs-12')]//h4[@class='description'][contains(text(),'Next intake')]/following-sibling::*//text()|"
                                            "//div[contains(@class,'box b-international not-hide col-xs-12')]//h4[@class='description'][contains(text(),'Next Intake')]/following-sibling::*//text()").extract()
                clear_space(start_date)
                item['start_date'] = getStartDateMonth(' '.join(start_date))
                if item['start_date'] == "":
                    print("***start_date 为空")
                print("item['start_date']: ", item['start_date'])

                overview = response.xpath("//div[@id='overview']/..|//div[@id='overview']/../following-sibling::div[1]|"
                                          "//div[@id='Overview']/..|//div[@id='Overview']/../following-sibling::div[1]").extract()
                item['degree_overview_en'] = remove_class(clear_lianxu_space(overview))

                modules_en_url = response.xpath("//table[@class='table  program-table']//td//a[contains(text(),'View plan')]/@href").extract()
                clear_space(modules_en_url)
                if len(modules_en_url) > 0:
                    url = "https://www.rmit.edu.au"+modules_en_url[0]
                    self.parse_modules1(url, item)
                else:
                    modules_en = response.xpath(
                        "//span[contains(text(),'Electives and program structure')]/../../../..").extract()
                    item['modules_en'] = remove_class(clear_lianxu_space(modules_en))

                if item['degree_overview_en'] == "":
                    overviewModulesUrl = response.url +"/program-details"
                    self.parse_overviewModules1(overviewModulesUrl, item)

                if item['degree_overview_en'] == "":
                    print("***degree_overview_en 为空")
                print("item['degree_overview_en']: ", item['degree_overview_en'])
                if item['modules_en'] == "":
                    print("***modules_en 为空")
                print("item['modules_en']: ", item['modules_en'])

                career = response.xpath(
                    "//div[@id='career']|//div[@id='career']/../following-sibling::div[1]|"
                    "//div[@id=' career']|//div[@id=' career']/../following-sibling::div[1]|"
                    "//div[@id='Career']|//div[@id='Career']/../following-sibling::div[1]|"
                    "//div[@id=' Career']|//div[@id=' Career']/../following-sibling::div[1]").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career))
                if item['career_en'] == "":
                    careerUrl = response.url + "/career"
                    self.parse_career1(careerUrl, item)
                if item['career_en'] == "":
                    print("***career_en 为空")
                print("item['career_en']: ", item['career_en'])

                rntry_requirements_en = response.xpath(
                    "//div[@id='admissions']/..|//div[@id='admissions']/../following-sibling::*[position()<last()-3]|"
                    "//div[@id='Admissions']/..|//div[@id='Admissions']/../following-sibling::*[position()<last()-3]").extract()
                item['rntry_requirements_en'] = remove_class(clear_lianxu_space(rntry_requirements_en))
                if item['rntry_requirements_en'] == "":
                    entryUrl = response.url + "/entry-requirements"
                    self.parse_entryrequirements1(entryUrl, item)
                if item['rntry_requirements_en'] == "":
                    print("***rntry_requirements_en 为空")
                # print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

                ielts_desc = response.xpath(
                    "//li[contains(text(),'IELTS (Academic): ')]//text()").extract()
                item['ielts_desc'] += clear_lianxu_space(ielts_desc)
                # print("item['ielts_desc']: ", item['ielts_desc'])

                ielts_d = get_ielts(item['ielts_desc'])
                item["ielts"] = ielts_d.get('IELTS')
                item["ielts_l"] = ielts_d.get('IELTS_L')
                item["ielts_s"] = ielts_d.get('IELTS_S')
                item["ielts_r"] = ielts_d.get('IELTS_R')
                item["ielts_w"] = ielts_d.get('IELTS_W')
                # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

                toefl_desc = response.xpath(
                    "//*[contains(text(),'TOEFL (Internet Based Test - IBT): ')]//text()").extract()
                item['toefl_desc'] += clear_lianxu_space(toefl_desc)
                # print("item['toefl_desc']: ", item['toefl_desc'])

                ielts_d = get_toefl(item['toefl_desc'])
                item["toefl"] = ielts_d.get('TOEFL')
                item["toefl_l"] = ielts_d.get('TOEFL_L')
                item["toefl_s"] = ielts_d.get('TOEFL_S')
                item["toefl_r"] = ielts_d.get('TOEFL_R')
                item["toefl_w"] = ielts_d.get('TOEFL_W')
                # print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
                #         item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))
            # programme = response.xpath("//div[@class='program-name']/h1/text()").extract()
            # ucascode = response.xpath("//html//div[@class='c-summary c-summary-2-col mb-lg-lg-lg clearfix']/div[1]/span[2]/text()").extract()
            # clear_space(ucascode)
            # # item['ucas_code'] = ''.join(ucascode)
            # # print("item['ucas_code']2: ", item['ucas_code'])
            #
            # duration = response.xpath(
            #     "//div[@data-duration][2]/span[2]/text()").extract()
            # clear_space(duration)
            # item['duration'] = ''.join(duration)
            # print("item['duration']2: ", item['duration'])
            #
            # start_date = response.xpath(
            #     "//div[@data-intake][2]/span[2]/text()").extract()
            # clear_space(start_date)
            # item['start_date'] = ''.join(start_date)
            # print("item['start_date']2: ", item['start_date'])
            #
            # location = response.xpath(
            #     "//div[@class='c-summary-cell not-hide']/span[2]//text()").extract()
            # clear_space(location)
            # item['location'] = ''.join(location)
            # print("item['location']2: ", item['location'])
            #
            # department = response.xpath(
            #     "//html//div[@class='c-summary c-summary-2-col mb-lg-lg-lg clearfix']/div[7]/span[2]/text()").extract()
            # clear_space(department)
            # item['department'] = ''.join(department)
            # print("item['department']2: ", item['department'])
            #
            # overview = response.xpath(
            #     "//html//div[@class='program-summary-section-overview mb-md-md-md']/div[position()<last()-1]").extract()
            # item['degree_overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['degree_overview_en']2: ", item['degree_overview_en'])
            #
            #
            # # //html//div[@class='panel-group accordion']/div/div[4]
            # career = response.xpath(
            #     "//html//div[@class='panel-group accordion']/div/div[@class='panel panel-default Yes'][3]").extract()
            # if "Career outlook" not in career:
            #     career = response.xpath(
            #     "//html//div[@class='panel-group accordion']/div/div[@class='panel panel-default Yes'][4]").extract()
            # item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']2: ", item['career_en'])
            #
            # modulesUrl = response.url + "/program-structure"
            # self.parse_modules2(modulesUrl, item)
            #
            # how_to_applyUrl = response.url + "/how-to-apply"
            # self.parse_how_to_apply2(how_to_applyUrl, item)
            #
            # entryUrl = response.url + "/entry-requirements"
            # self.entryrequirements2(entryUrl, item)
            #
            # feeUrl = response.url + "/fees"
            # self.fees2(feeUrl, item)

                item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<div class="share-heading hide">How to Apply</div>
  </div>
                </div>
			<div class="standard-content-article mb-lg-md-md clearfix">
				<div class="org-area-module-detail-view accordian ">
					<div class="row">
						<div class="col-xs-12 ">
							<div class="clearfix">
  <p class="lead">A step-by-step guide for international students on how to apply to study at RMIT.</p>
  <div class="lower-image-container"></div>
							</div>
							<!-- Parsys -->
							<!-- This Parsys will be used to Put all Main Body Components -->
<div class="floated-image-container pull-right">
<div class="detail-img-list not-hide image-square">
	<figure>
		<div class="c-detail-image c-detail-image-square">
			<img data-ri-xxs="/content/dam/rmit/rmit-images/life-at-rmit/Study-modes_EVE-800x800.jpg.transform/rendition-800x800/image.jpg" data-ri-sm="/content/dam/rmit/rmit-images/life-at-rmit/Study-modes_EVE-800x800.jpg.transform/rendition-640x640/image.jpg" class="c-responsive-image bg-cover offset-content">
		</div>
		<div class="c-detail-image c-detail-image-portrait">
			<img data-ri-xxs="/content/dam/rmit/rmit-images/life-at-rmit/Study-modes_EVE-800x800.jpg.transform/rendition-800x1068/image.jpg" data-ri-sm="/content/dam/rmit/rmit-images/life-at-rmit/Study-modes_EVE-800x800.jpg.transform/rendition-640x854/image.jpg" class="c-responsive-image bg-cover offset-content">
		</div>
	</figure>
</div>
</div>
<div>
    <div class="extended-desc not-hidden">
        <p>If you want to study for only one or two semesters, you can apply for a&nbsp;<a href="/content/rmit-ui/en/study-with-us/international-students/programs-for-international-students/study-abroad-and-exchange/study-abroad.html">study abroad program</a>&nbsp;or&nbsp;<a href="/content/rmit-ui/en/study-with-us/international-students/programs-for-international-students/study-abroad-and-exchange/student-exchange.html">student exchange</a>&nbsp;at RMIT.</p>
<h3>Applying for a research degree?</h3>
<p>If you want to apply for a research program, <a href="/content/rmit-ui/en/research/phds-and-other-research-degrees/how-to-apply.html">follow this process and apply here</a> instead.<br>
</p>
<h2>Step 1: Find a program</h2>
<p>Search for a program in your&nbsp;<a href="/content/rmit-ui/en/study-with-us.html">interest area</a>&nbsp;or browse by&nbsp;<a href="/content/rmit-ui/en/study-with-us/international-students/programs-for-international-students.html">level of study</a>. Some programs are not available in the July intake, in which case, you will need to apply for the next available intake.</p>
<p>You can also use the&nbsp;<a href="https://www.international.rmit.edu.au/info/programfees.asp" title="Programs, intakes and tuition fees database">Programs, intakes and tuition fees database</a>&nbsp;to search for programs.</p>
<h2>Step 2: Check the entry requirements</h2>
<p>Check that you qualify for the program's entry requirements including:</p>
<ul>
<li>English language requirements</li>
<li>academic entry requirement (see equivalent&nbsp;<a href="/content/rmit-ui/en/study-with-us/international-students/apply-to-rmit-international-students/entry-requirements/country-equivalency.html">entry requirements by country</a>)</li>
<li>pre-requisites</li>
<li>selection tasks.</li>
</ul>
<p>If you don’t meet the entry requirements for your preferred program, you can consider a range of programs that may provide&nbsp;<a href="/content/rmit-ui/en/study-with-us/international-students/apply-to-rmit-international-students/pathways-and-credit-transfer.html">pathways</a>&nbsp;to your preferred program.</p>
<p>If you are&nbsp;​currently ​studying ​an​ Australian Year 12 ​(in Australia or overseas) ​​or​ International Baccalaureate ​(​in Australia or New Zealand) and ​applying &nbsp;for a&nbsp;Bachelor, Associate or Honours degree, you will need to apply via VTAC. You should <a href="http://www.rmit.edu.au/study-with-us/international-students/apply-to-rmit-international-students/how-to-apply/international-students-studying-vce-or-ib">check the VTAC entry requirements</a>.<br>
</p>
<h2>Step 3: Collect required documents</h2>
<p>To avoid delays in admission processing, submit&nbsp;a&nbsp;complete set of supporting documents&nbsp;including:</p>
<ul>
<li>passport</li>
<li>certified copies of academic transcripts&nbsp;&nbsp;(not required for current RMIT students applying to another RMIT program)</li>
<li>certified copies of all graduation certificates in both the original&nbsp;language and English&nbsp;&nbsp;(not required for current RMIT students applying to another RMIT program)</li>
<li>evidence of English language proficiency&nbsp;&nbsp;(not required for current RMIT students applying to another RMIT program)</li>
<li>any documentation relating to selection tasks (pre-selection kits,&nbsp;folios etc.)</li>
<li>CV, work reference letter, referee report etc if applicable</li>
</ul>
<p>&nbsp;Please note that documents submitted will not be returned.</p>
<h2>Step 4: Submit your application</h2>
<p>Submit your&nbsp;application online&nbsp;with&nbsp;<a href="/content/rmit-ui/en/study-with-us/international-students/apply-to-rmit-international-students/how-to-apply/documentation-required.html">all the required documents</a>.</p>
<h4>Students completing an Australian Year 12 (in Australia or overseas), or the International Baccalaureate (in Australia or New Zealand)</h4>
<ul>
<li>Apply for <strong>Higher Education</strong> programs (Bachelor, Associate Degree and Honours) through the Victorian Tertiary Admissions Centre (VTAC).<br>
<br>
<a href="http://www.vtac.edu.au/applying.html">Apply now via VTAC</a></li>
<li>Apply for <strong>Vocational Education</strong> programs (Foundation Studies, ELICOS, VCE, Certificate IV, Diploma and Advanced Diplomas) via iApply, the online application system for international students.<br>
<br>
<a href="https://iapply.rmit.edu.au/sitsvision/wrd/SIW_LGN">Apply now via iApply</a></li>
</ul>
<h4>Studying fully online<br>
</h4>
<ul>
<li>If your program is delivered fully online, use the online application system for local students and follow the local student application process. Note: fully online programs do not qualify for an Australian Student Visa.<br>
<br>
<a href="https://rmit.service-now.com/rmit-admissions/">Apply now via Admissions</a></li>
</ul>
<h4>All other international students<br>
</h4>
<ul>
<li>If you are applying for on-campus study in a coursework program use iApply, the online application system for international students.<br>
<br>
<a href="https://iapply.rmit.edu.au/sitsvision/wrd/SIW_LGN">Apply now via iApply</a></li>
</ul>
<h4>Application fee</h4>
<p>You will need to pay an application fee if you are from one of these&nbsp;<a href="/content/rmit-ui/en/study-with-us/international-students/apply-to-rmit-international-students/how-to-apply/application-fee.html">countries classified as high risk</a>.</p>
<h2>Need help?</h2>
<p>If you need assistance,&nbsp;<a href="https://connect.prospectivestudent.info/RMITInt?_ga=1.241036611.1742672422.1416265787">contact us</a>&nbsp;or one of&nbsp;<a href="https://www.international.rmit.edu.au/info/agentlist/">RMIT’s appointed representatives</a>&nbsp;(agents).</p>
<h2>Next steps:</h2>
<p>Your application will be assessed in line with RMIT’s policies and procedures. If you are successful, you will receive an offer letter. You can then&nbsp;<a href="/content/rmit-ui/en/study-with-us/international-students/apply-to-rmit-international-students/accept-your-offer.html">accept your offer</a>&nbsp;by following the instructions in your offer letter.&nbsp;</p>
<p>RMIT will normally advise you on the outcome of your application within 10 business days. If you are applying from Australia you should hear within 24 hours. If you don't hear back within the time frame above please <a href="https://rmit.au1.qualtrics.com/jfe/form/SV_0fbt3k9dEkNATZ3">contact Admissions Helpdesk</a>.</p>
<p>If you are applying via VTAC <a href="http://www.vtac.edu.au/dates.html">check the VTAC website</a> for important dates.</p>
    </div>
</div>
						</div>
					</div>"""]))
                item['apply_documents_en'] = remove_class(clear_lianxu_space(["""<p>To avoid delays in admission processing, submit&nbsp;a&nbsp;complete set of supporting documents&nbsp;including:</p>
<ul>
<li>passport</li>
<li>certified copies of academic transcripts&nbsp;&nbsp;(not required for current RMIT students applying to another RMIT program)</li>
<li>certified copies of all graduation certificates in both the original&nbsp;language and English&nbsp;&nbsp;(not required for current RMIT students applying to another RMIT program)</li>
<li>evidence of English language proficiency&nbsp;&nbsp;(not required for current RMIT students applying to another RMIT program)</li>
<li>any documentation relating to selection tasks (pre-selection kits,&nbsp;folios etc.)</li>
<li>CV, work reference letter, referee report etc if applicable</li>
</ul>
<p>&nbsp;Please note that documents submitted will not be returned.</p>"""]))
                yield item
        except Exception as e:
            with open("scrapySchool_Australian_ben/error/" + item['university'] + str(item['degree_type']) + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_overviewModules1(self, url, item):
        headers_base = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        }
        data = requests.get(url, headers=headers_base)
        response = etree.HTML(data.text)
        # ucascode = response.xpath("//div[@class='c-summary-cell']//div[@class='inside']/span[2]//text()")
        # item['ucas_code'] = ''.join(ucascode)
        # print("item['ucas_code']: ", item['ucas_code'])

        # //html//div[@class='module']//div[8]/div[1]/span[2]
        department = response.xpath("//span[contains(text(),'School:')]/following-sibling::*//text()")
        clear_space(department)
        item['department'] = ''.join(department).strip()
        print("item['department']: ", item['department'])

        # ielts = response.xpath("//div[@class='c-summary-cell hidden-cell b-international'][last()]//text()")
        # clear_space(ielts)
        # item['IELTS'] = ''.join(ielts)
        # print("item['IELTS']: ", item['IELTS'])

        overview = response.xpath("//div[@class='c-summary c-summary-3-col clearfix']/following-sibling::div[1]")
        overview_str = ""
        if len(overview) > 0:
            for o in overview:
                overview_str += etree.tostring(o, encoding='unicode', method='html')
        item['degree_overview_en'] = remove_class(clear_lianxu_space([overview_str]))
        # print("item['degree_overview_en']: ", item['degree_overview_en'])

        modules = response.xpath("//h3[contains(text(),'Program Structure')]|//h3[contains(text(),'Program Structure')]/following-sibling::*|"
                                 "//*[contains(text(),'Program structure')]|//*[contains(text(),'Program structure')]/following-sibling::*|"
                                 "//h2[contains(text(),'Structure')]/..|//h2[contains(text(),'Stucture')]/..|"
                                 "//h2[contains(text(),'Specialisations and electives')]/..")
        modules_str = ""
        if len(modules) > 0:
            for o in modules:
                modules_str += etree.tostring(o, encoding='unicode', method='html')
        item['modules_en'] = remove_class(clear_lianxu_space([modules_str]))
        # print("item['modules_en']: ", item['modules_en'])

    def parse_modules1(self, url, item):
        headers_base = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        }
        data = requests.get(url, headers=headers_base)
        response = etree.HTML(data.text)

        modules = response.xpath("//h3[contains(text(),'Program Structure')]|//h3[contains(text(),'Program Structure')]/following-sibling::*|"
                                 "//h2[contains(text(),'Structure')]/..|"
                                 "//h2[contains(text(),'Specialisations and electives')]/..")
        modules_str = ""
        if len(modules) > 0:
            for o in modules:
                modules_str += etree.tostring(o, encoding='unicode', method='html')
        item['modules_en'] += remove_class(clear_lianxu_space([modules_str]))
        # print("item['modules_en']: ", item['modules_en'])

    def parse_career1(self, url, item):
        headers_base = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        }
        data = requests.get(url, headers=headers_base)
        response = etree.HTML(data.text)
        career = response.xpath("//h2[contains(text(),'Career outlook')]/..")
        career_str = ""
        if len(career) > 0:
            for c in career:
                career_str += etree.tostring(c, encoding='unicode', method='html')
        item['career_en'] += remove_class(clear_lianxu_space([career_str]))

        if item['career_en'] == "":
            career = response.xpath("//div[@class='m-super-detail-page']")
            career_str = ""
            if len(career) > 0:
                for c in career:
                    career_str += etree.tostring(c, encoding='unicode', method='html')
            item['career_en'] += remove_class(clear_lianxu_space([career_str]))
        # print("item['career']: ", item['career'])

    def parse_entryrequirements1(self, url, item):
        headers_base = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        }
        data = requests.get(url, headers=headers_base)
        response = etree.HTML(data.text)
        entry_requirements = response.xpath("//div[@data-page-id='overview']/div[position()>=3]")
        entry_requirements_str = ""
        if len(entry_requirements) > 0:
            for c in entry_requirements:
                entry_requirements_str += etree.tostring(c, encoding='unicode', method='html')
        item['rntry_requirements_en'] += remove_class(clear_lianxu_space([entry_requirements_str]))
        # print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

        # ielts_desc
        ielts_desc = response.xpath("//*[contains(text(),'IELTS (Academic): ')]//text()")
        item['ielts_desc'] = ''.join(ielts_desc).strip()

        # toefl_desc
        toefl_desc = response.xpath("//*[contains(text(),'TOEFL (Internet Based Test - IBT): ')]//text()")
        item['toefl_desc'] = ''.join(toefl_desc).strip()

    def parse_modules2(self, url, item):
        headers_base = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        }
        data = requests.get(url, headers=headers_base)
        response = etree.HTML(data.text)
        modules = response.xpath("//div[@class='standard-content-article mb-lg-md-md clearfix']/div/div[position()>2]//text()")
        clear_space(modules)
        item['modules'] = ''.join(modules).strip()
        print("item['modules']: ", item['modules'])

    def parse_how_to_apply2(self, url, item):
        headers_base = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        }
        data = requests.get(url, headers=headers_base)
        response = etree.HTML(data.text)
        how_to_apply = response.xpath("//div[@class='standard-content-article mb-lg-md-md clearfix']/div/div[position()>2]//text()")
        clear_space(how_to_apply)
        item['how_to_apply'] = ''.join(how_to_apply).strip()
        print("item['how_to_apply']: ", item['how_to_apply'])

    def entryrequirements2(self, url, item):
        headers_base = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        }
        data = requests.get(url, headers=headers_base)
        response = etree.HTML(data.text)
        entry_requirements = response.xpath("//div[@class='standard-content-article mb-lg-md-md clearfix']/div/div[position()>2]//text()")
        clear_space(entry_requirements)
        item['entry_requirements'] = ''.join(entry_requirements).strip()
        print("item['entry_requirements']: ", item['entry_requirements'])

        ielts = response.xpath("//div[@class='standard-content-article mb-lg-md-md clearfix']/div/div[position()>2]//ul[last()]/li[position()<4]//text()")
        clear_space(ielts)
        item['IELTS'] = ''.join(ielts)
        print("item['IELTS']: ", item['IELTS'])

    def fees2(self, url, item):
        headers_base = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        }
        data = requests.get(url, headers=headers_base)
        response = etree.HTML(data.text)
        tuition_fee = response.xpath("//div[@class='standard-content-article mb-lg-md-md clearfix']/div/div[position()>2]/div[2]//text()")
        clear_space(tuition_fee)
        # print(tuition_fee)
        # tuition_fee = getTuition_fee(''.join(tuition_fee))
        item['tuition_fee'] = ''.join(tuition_fee)
        print("item['tuition_fee']: ", item['tuition_fee'])
