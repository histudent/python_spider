import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getDuration import getIntDuration, getTeachTime

class UniversityOfSalford_PSpider(CrawlSpider):
    name = "UniversityOfSalford_P"
    start_urls = ["https://www.salford.ac.uk/study/a-z-courses?root_node_selection=275504&page_asset_listing_279643_submit_button=Submit&queries_subject_query_posted=1&queries_subject_query=&current_result_page=1&results_per_page=0&submitted_search_category=&mode=&result_279643_result_page=A"]

    rules = (
        Rule(LinkExtractor(allow=r"result_279643_result_page=[A-Z@]"), follow=True, callback='parse_url'),
    )

    def parse_url(self, response):
        # print("===", response.url)
        links = response.xpath("//div[@id='atoz']//div[@class='list-group']/a/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))
#         links = ["https://www.salford.ac.uk/pgt-courses/social-work",
# "https://www.salford.ac.uk/pgt-courses/nursing-research,-practice,-education",
# "https://www.salford.ac.uk/pgt-courses/literature-culture",
# "https://www.salford.ac.uk/pgt-courses/human-resource-management-and-development",
# "https://www.salford.ac.uk/pgt-courses/health,-safety-and-industrial-law",
# "https://www.salford.ac.uk/pgt-courses/ecologies-of-cities",
# "https://www.salford.ac.uk/pgt-courses/dance-creative-dance-education",
# "https://www.salford.ac.uk/pgt-courses/digital-marketing",
# "https://www.salford.ac.uk/pgt-courses/dance-choreography-and-professional-practices",
# "https://www.salford.ac.uk/pgt-courses/drug-design-and-discovery",
# "https://www.salford.ac.uk/pgt-courses/digital-business",
# "https://www.salford.ac.uk/pgt-courses/msc-data-science",
# "https://www.salford.ac.uk/pgt-courses/advanced-diabetes-care",
# "https://www.salford.ac.uk/pgt-courses/dance-performance-and-professional-practices",
# "https://www.salford.ac.uk/pgt-courses/dementia-care-and-the-enabling-environment",
# "https://www.salford.ac.uk/pgt-courses/design-for-communication-with-industry-experience",
# "https://www.salford.ac.uk/pgt-courses/finance-and-investment-management",
# "https://www.salford.ac.uk/pgt-courses/financial-services-management",
# "https://www.salford.ac.uk/pgt-courses/fraud-and-risk-management-forensic-accounting",
# "https://www.salford.ac.uk/pgt-courses/contemporary-arts-practice-with-industry-experience",
# "https://www.salford.ac.uk/pgt-courses/cyber-security,-threat-intelligence-and-forensics",
# "https://www.salford.ac.uk/pgt-courses/contemporary-performance-practice",
# "https://www.salford.ac.uk/pgt-courses/creative-writing-innovation-and-experiment",
# "https://www.salford.ac.uk/pgt-courses/construction-management",
# "https://www.salford.ac.uk/pgt-courses/building-surveying",
# "https://www.salford.ac.uk/pgt-courses/cognitive-behavioural-psychotherapy",
# "https://www.salford.ac.uk/pgt-courses/biotechnology",
# "https://www.salford.ac.uk/pgt-courses/biomedical-science",
# "https://www.salford.ac.uk/pgt-courses/bim-and-digital-built-environments",
# "https://www.salford.ac.uk/pgt-courses/environmental-acoustics",
# "https://www.salford.ac.uk/pgt-courses/environmental-assessment-and-management",
# "https://www.salford.ac.uk/pgt-courses/gas-engineering-and-management",
# "https://www.salford.ac.uk/pgt-courses/health-and-global-environment",
# "https://www.salford.ac.uk/pgt-courses/nursing-rn-adult-mental-health-children-young-people",
# "https://www.salford.ac.uk/pgt-courses/international-journalism-for-digital-media",
# "https://www.salford.ac.uk/pgt-courses/international-business-with-law",
# "https://www.salford.ac.uk/pgt-courses/international-events-management",
# "https://www.salford.ac.uk/pgt-courses/international-human-resource-management-and-development",
# "https://www.salford.ac.uk/pgt-courses/international-corporate-finance",
# "https://www.salford.ac.uk/pgt-courses/international-business",
# "https://www.salford.ac.uk/pgt-courses/international-commercial-law",
# "https://www.salford.ac.uk/pgt-courses/international-business-law",
# "https://www.salford.ac.uk/pgt-courses/islamic-banking-and-finance",
# "https://www.salford.ac.uk/pgt-courses/intelligence-and-security-studies",
# "https://www.salford.ac.uk/pgt-courses/information-systems-management",
# "https://www.salford.ac.uk/pgt-courses/operations-management",
# "https://www.salford.ac.uk/pgt-courses/international-banking-and-finance",
# "https://www.salford.ac.uk/pgt-courses/leadership-and-management-for-healthcare-practice",
# "https://www.salford.ac.uk/pgt-courses/media-production-tv-documentary-production",
# "https://www.salford.ac.uk/pgt-courses/media-production-childrens-tv-production",
# "https://www.salford.ac.uk/pgt-courses/molecular-parasitology-and-vector-biology",
# "https://www.salford.ac.uk/pgt-courses/managing-innovation-and-information-technology",
# "https://www.salford.ac.uk/pgt-courses/media-production-post-production-for-tv",
# "https://www.salford.ac.uk/pgt-courses/music2",
# "https://www.salford.ac.uk/pgt-courses/midwifery",
# "https://www.salford.ac.uk/pgt-courses/media-psychology",
# "https://www.salford.ac.uk/pgt-courses/media-production-animation",
# "https://www.salford.ac.uk/pgt-courses/media-production-tv-drama-production",
# "https://www.salford.ac.uk/pgt-courses/marketing",
# "https://www.salford.ac.uk/pgt-courses/management",
# "https://www.salford.ac.uk/pgt-courses/journalism-news-broadcast-sport",
# "https://www.salford.ac.uk/pgt-courses/psychology-of-coercive-control",
# "https://www.salford.ac.uk/pgt-courses/petroleum-and-gas-engineering",
# "https://www.salford.ac.uk/pgt-courses/public-health",
# "https://www.salford.ac.uk/pgt-courses/procurement,-logistics-and-supply-chain-management",
# "https://www.salford.ac.uk/pgt-courses/project-management",
# "https://www.salford.ac.uk/pgt-courses/professional-accounting",
# "https://www.salford.ac.uk/pgt-courses/public-relations-and-digital-communications",
# "https://www.salford.ac.uk/pgt-courses/project-management-in-construction",
# "https://www.salford.ac.uk/pgt-courses/safety,-health-and-environment",
# "https://www.salford.ac.uk/pgt-courses/socially-engaged-photography-practice-with-community-experience",
# "https://www.salford.ac.uk/pgt-courses/structural-engineering",
# "https://www.salford.ac.uk/pgt-courses/sustainability",
# "https://www.salford.ac.uk/pgt-courses/quantity-surveying",
# "https://www.salford.ac.uk/pgt-courses/socially-engaged-arts-practice-with-community-experience",
# "https://www.salford.ac.uk/pgt-courses/trauma-and-orthopaedics-lower-limb",
# "https://www.salford.ac.uk/pgt-courses/trauma-and-orthopaedics",
# "https://www.salford.ac.uk/pgt-courses/the-salford-mba",
# "https://www.salford.ac.uk/pgt-courses/terrorism-and-security",
# "https://www.salford.ac.uk/pgt-courses/transport-engineering-and-planning",
# "https://www.salford.ac.uk/pgt-courses/trauma-and-orthopaedics-spinal",
# "https://www.salford.ac.uk/pgt-courses/wildlife-conservation",
# "https://www.salford.ac.uk/pgt-courses/wildlife-documentary-production",
# "https://www.salford.ac.uk/pgt-courses/trauma-and-orthopaedics-upper-limb",
# "https://www.salford.ac.uk/pgt-courses/advancing-physiotherapy2",
# "https://www.salford.ac.uk/pgt-courses/accounting-and-finance",
# "https://www.salford.ac.uk/pgt-courses/advanced-counselling-and-psychotherapy-studies-supervision",
# "https://www.salford.ac.uk/pgt-courses/advanced-counselling-and-psychotherapy-studies",
# "https://www.salford.ac.uk/pgt-courses/digital-media-audio-production",
# "https://www.salford.ac.uk/pgt-courses/aerospace-engineering2",
# "https://www.salford.ac.uk/pgt-courses/advanced-control-systems",
# "https://www.salford.ac.uk/pgt-courses/robotics-and-automation",
# "https://www.salford.ac.uk/pgt-courses/real-estate-and-property-management",
# "https://www.salford.ac.uk/pgt-courses/advanced-automotive-and-autonomous-technology",
# "https://www.salford.ac.uk/pgt-courses/audio-acoustics2",
# "https://www.salford.ac.uk/pgt-courses/risk-and-crisis-management-food-safety-assurance", ]
        for link in links:
            url = "https://www.salford.ac.uk" + link
            # url = link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.salford.ac.uk/"
        item['university'] = "University of Salford"
        item['url'] = response.url
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        item['location'] = 'The Crescent, Salford, M5 4WT, UK'
        print("===========================")
        print(response.url)
        try:
            # 专业、学位类型
            programme = response.xpath("//div[@id='content']/div[@class='col-md-12']/div[@class='course-title']/div[@class='row']/div[@class='col-sm-8 col-md-8']/h1//text()").extract()
            item['programme_en'] = ''.join(programme)
            print("item['programme_en']: ", item['programme_en'])

            degree_type = response.xpath("//div[@id='content']/div[@class='col-md-12']/div[@class='course-title']/div[@class='row']/div[@class='col-sm-8 col-md-8']/h2//text()").extract()
            item['degree_name'] = ''.join(degree_type)
            print("item['degree_name']: ", item['degree_name'])

            # //div[@id='content']/div[@class='col-md-12']/div[@class='course-title']/div[@class='row']/div[@class='col-sm-8 col-md-8']/p
            department = response.xpath("//strong[contains(text(), 'School -')]/../text()|"
                                        "//p[contains(text(),'This course is a collaboration between the followi')]/../following-sibling::*[1]//text()").extract()
            clear_space(department)
            item['department'] = ', '.join(department).replace(', , ', ', ').strip().strip(',').strip()
            if item['department'] == "":
                print("***")
            print("item['department']: ", item['department'])

            start_date = response.xpath("//strong[contains(text(), 'Start Date(s):')]/../text()").extract()
            clear_space(start_date)
            print("start_date: ", start_date)
            start_date = ''.join(start_date)
            if ";" in start_date:
                start_date_list = start_date.split(";")
                print(start_date_list)
                for s in start_date_list:
                    item['start_date'] += getStartDate(s.strip().lower()) + ","
            else:
                item['start_date'] = getStartDate(''.join(start_date).lower())
            item['start_date'] = item['start_date'].strip().strip(",").strip()
            print("item['start_date']: ", item['start_date'])

            duration = response.xpath("//strong[contains(text(), 'Duration')]/../following-sibling::*[position()<3]//text()").extract()
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

            # //strong[contains(text(), 'Fees')]/../following-sibling::p[contains(text(), 'International -')]
            tuition_fee = response.xpath("//strong[contains(text(), 'Fees')]/../following-sibling::p[contains(text(), 'International')]//text()").extract()
            clear_space(tuition_fee)
            print("tuition_fee: ", tuition_fee)
            tuition_fee_re = re.findall(r"£\d+,\d+", ''.join(tuition_fee))
            # print("tuition_fee_re: ", tuition_fee_re)
            if len(tuition_fee_re) > 0:
                item['tuition_fee'] = getTuition_fee(''.join(tuition_fee_re))
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee']: ", item['tuition_fee'])
            print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            # //div[@id='content']/div[@class='col-md-12']/div[@class='row']/div[1]
            overview = response.xpath(
                "//div[@id='content']/div[@class='col-md-12']/div[@class='row']/div[1] | //div[@id='content']/div[@class='row']/div[1]").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])

            # //section[@id='about']/div[@id='content']
            modules_en = response.xpath("//div[@id='courseaccordion']").extract()
            if len(modules_en) == 0:
                # print("********")
                modules_en = response.xpath("//h2[contains(text(),'Course Details')]/following-sibling::*").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules_en)) # .replace("&nbsp;", "")
            item['modules_en'] = item['modules_en'].encode('utf-8').decode("unicode-escape").replace("Â ", "")
            # print("item['modules_en']: ", item['modules_en'])

            # //section[@id='requirements']/div
            entry_requirements = response.xpath("//section[@id='requirements']/div//text()").extract()
            item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            # 申请材料
            apply_documents_en = response.xpath("//h3[contains(text(),'Applicant profile')]/preceding-sibling::*[1]/following-sibling::*").extract()
            item['apply_documents_en'] = remove_class(clear_lianxu_space(apply_documents_en))
            # print("item['apply_documents_en']: ", item['apply_documents_en'])

            # //h3[contains(text(),'English Language Requirements')]/following-sibling::*[1]
            ielts_desc = response.xpath("//h3[contains(text(),'English Language Requirements')]/following-sibling::*[position()<3]//text()").extract()
            clear_space(ielts_desc)
            item['ielts_desc'] = ''.join(ielts_desc).replace("Suitable For", "").strip()
            # print("item['ielts_desc']: ",item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            if item['url'] == "https://www.salford.ac.uk/pgt-courses/journalism-news-broadcast-sport":
                item['ielts_l'] = 6.0
                item['ielts_s'] = 6.0
                item['ielts_r'] = 6.0
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))


            # //section[@id='teaching']/div[@class='container main']/div[@class='col-md-12']/div[@id='teaching_0a19']
            assessment_en = response.xpath("//section[@id='teaching']/div").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            # //section[@id='employability']/div[@class='container main']/div[@class='col-md-12']/div[@id='employ_0a19']
            career = response.xpath("//section[@id='employability']/div").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<div id="content_div_43743">
<h1>How to apply for a postgraduate taught degree</h1><p>You should complete your application online. Click the button below to get started. There is plenty of helpful information throughout the application process.</p><p>If you have all your supporting documents ready, it will only take about 20 minutes to complete the process. However, you can save your application at any stage and come back to it as many times as you like.</p>
</div>

<div id="new_content_container_1410668">
<div class="moneybox" id="new_div_48503">
<p><a href="http://webapps.ascentone.com/login.aspx?key=5D4B012A-BB6C-495B-B2E4-B5A56B3CCF00" class="btn btn-primary btn-large">Apply online here</a></p>
</div>
</div>

<div id="new_content_container_1410670">

</div>

<div id="new_div_48505">
<h2>What documents will I need?</h2><p>To complete the application process, you will need to upload scanned copies of your supporting documents. These documents vary from course to course, but usually include:</p><ul><li>One reference&nbsp;</li> <li>Transcripts or certificates demonstrating that you meet, or are likely to meet, the entry requirements for your course&nbsp;&nbsp;</li> <li>Evidence, <a href="http://www.salford.ac.uk/__data/assets/pdf_file/0018/104841/18-02-23-Vouch-List-Equivalent-qualifications-to-English-GCSE-Grade-C.pdf">if English is not your first language, that your command of English meets the standards required for postgraduate study</a> (an IELTS score of 6.5, or the equivalent, is the norm)&nbsp;&nbsp;</li> <li>A copy of your passport, if you are coming to us from outside the EU and will <a href="http://www.advice.salford.ac.uk/page/visa">require a student visa</a>.&nbsp;&nbsp;</li> <li>If you are applying for Applied Social Work Practice (MSc, PgDip or PgCert)&nbsp;you will also need to complete the <a href="http://www.salford.ac.uk/__data/assets/word_doc/0010/448768/Agency-Agreement.docx">Agency Sponsorship Form</a> and send it to <a href="mailto:P.A.Killeen@salford.ac.uk">P.A.Killeen@salford.ac.uk</a></li> <li>For the MA courses in Media Production you will be required to submit a project proposal related to your chosen specialist field, to support your application.&nbsp;&nbsp;A brief written synopsis (max. 500 words) of your ideas would also be required.&nbsp;&nbsp;Please note that this would be for discussion&nbsp;&nbsp;&nbsp;&nbsp;purposes at the interview only.&nbsp;&nbsp;</li></ul><p>You must ensure that you upload all the documents that are needed to support your application.&nbsp;&nbsp;If you do not provide us with the information we require to make a complete assessment your application this will delay our response to you.</p><h2>What if my documents aren't ready?</h2><p>If you have not yet finished a course, if you are currently studying towards a qualification and receive a conditional offer from us, once you have taken your exams, please ensure that you send copies of your transcripts and certificates to us as soon as possible to allow us to update your admission&nbsp;&nbsp;record.</p><p>Once you have completed your application form and submitted it, you will receive an email from us acknowledging receipt of your application. We aim to consider your application as soon as we can but this can vary depending on whether you are required to attend an interview.</p><h2>Deadlines</h2><p>Postgraduate courses may start at varying times throughout the year. You should&nbsp;&nbsp;submit your application at least one month prior to your chosen course starting date.</p><h2>Course application exceptions</h2><div><p>Applications that are&nbsp;<strong>an exception</strong> to our online application process are:&nbsp;&nbsp;</p> <ul><li><a href="http://www.ucas.com"><strong>MA Social Work full-time study via UCAS</strong></a></li> <li><strong><a href="http://www.salford.ac.uk/study/postgraduate/applying/applying-for-taught-courses/post-qualifying-applications-pg">Post qualifying Health and Social Care single modules</a></strong></li> <li><a href="http://www.unigis.org/uk-courses-introduction/uk-courses-how-apply"><strong>Geographical Information Systems are via our partners for this course Manchester Metropolitan University</strong></a></li> </ul></div><div><h2>Policy statement on equality and diversity&nbsp;&nbsp;</h2></div><p><a href="http://www.salford.ac.uk/study/postgraduate/applying/policy-statement-on-equality-and-diversity">Read our policy statement on equality and diversity</a></p>
</div>"""]))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<p><strong>Postgraduate</strong></p><p>(4 year) Bachelor degrees with a GPA 2.7/4.0 or 70% from a National University; or from a Project 211 University with a GPA 2.6/4.0 or 65%; or from a Private University with GPA 2.75/4.0 or 75%.</p>"""]))
            # print("item['require_chinese_en']: ", item['require_chinese_en'])
            yield item
        except Exception as e:
            with open(item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)
