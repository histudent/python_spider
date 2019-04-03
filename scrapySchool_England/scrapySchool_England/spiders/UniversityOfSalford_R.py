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

class UniversityOfSalford_RSpider(CrawlSpider):
    name = "UniversityOfSalford_R"
    start_urls = ["https://www.salford.ac.uk/study/a-z-courses?root_node_selection=275505&page_asset_listing_279643_submit_button=Submit&queries_subject_query_posted=1&queries_subject_query=&current_result_page=1&results_per_page=0&submitted_search_category=&mode=&result_279643_result_page=A"]

    rules = (
        Rule(LinkExtractor(allow=r"result_279643_result_page=[A-Z@]"), follow=True, callback='parse_url'),
    )

    def parse_url(self, response):
        # print("===", response.url)
        links = response.xpath("//div[@id='atoz']//div[@class='list-group']/a/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))
        for link in links:
            url = "https://www.salford.ac.uk" + link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.salford.ac.uk/"
        item['university'] = "University of Salford"
        item['url'] = response.url
        item['teach_type'] = 'phd'
        # 学位类型
        item['degree_type'] = 3
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
            department = response.xpath("//strong[contains(text(), 'School -')]/../text()").extract()
            item['department'] = ''.join(department).strip()
            print("item['department']: ", item['department'])

            start_date = response.xpath("//strong[contains(text(), 'Start Date(s):')]/../text()").extract()
            clear_space(start_date)
            # print("start_date: ", start_date)
            item['start_date'] = getStartDate(''.join(start_date))
            # print("item['start_date']: ", item['start_date'])

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

            if item['department'] == "School of Environment & Life Sciences" or item['department'] == "School of Computing, Science & Engineering" or item['department'] == "School of the Built Environment" or item['department'] == "School of Health Sciences":
                item['tuition_fee'] = 13680
                item['tuition_fee_pre'] = "£"
            elif item['department'] == "School of Arts & Media":
                item['tuition_fee'] = 12490
                item['tuition_fee_pre'] = "£"
            elif item['department'] == "Salford Business School":
                item['tuition_fee'] = 12990
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee']: ", item['tuition_fee'])
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            # //div[@id='content']/div[@class='col-md-12']/div[@class='row']/div[1]
            overview = response.xpath(
                "//div[@id='content']/div[@class='col-md-12']/div[@class='row']/div[1] | //div[@id='content']/div[@class='row']/div[1]").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])

            # //section[@id='about']/div[@id='content']
            # modules_en = response.xpath("//div[@id='courseaccordion']").extract()
            # if len(modules_en) == 0:
            #     # print("********")
            #     modules_en = response.xpath("//h2[contains(text(),'Course Details')]/following-sibling::*").extract()
            # item['modules_en'] = remove_class(clear_lianxu_space(modules_en)) # .replace("&nbsp;", "")
            # item['modules_en'] = item['modules_en'].encode('utf-8').decode("unicode-escape").replace("Â ", "")
            # print("item['modules_en']: ", item['modules_en'])

            # //section[@id='requirements']/div
            entry_requirements = response.xpath("//section[@id='requirements']/div//text()").extract()
            item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            # 申请材料
            apply_documents_en = response.xpath("//h3[contains(text(),'Applicant Profile')]/preceding-sibling::*[1]/following-sibling::*[position()<5]").extract()
            item['apply_documents_en'] = remove_class(clear_lianxu_space(apply_documents_en)).replace("<h3>International Students - Academic Technology Approval Scheme (ATAS)</h3>", "").strip()
            # print("item['apply_documents_en']: ", item['apply_documents_en'])

            # //h3[contains(text(),'English Language Requirements')]/following-sibling::*[1]
            ielts_desc = response.xpath("//*[contains(text(),'IELTS')]//text()").extract()
            clear_space(ielts_desc)
            item['ielts_desc'] = ''.join(ielts_desc).replace("Suitable For", "").strip()
            # print("item['ielts_desc']: ",item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))


            # //section[@id='teaching']/div[@class='container main']/div[@class='col-md-12']/div[@id='teaching_0a19']
            assessment_en = response.xpath("//h3[contains(text(),'Assessment Links')]/preceding-sibling::*[1]/following-sibling::*").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            # //section[@id='employability']/div[@class='container main']/div[@class='col-md-12']/div[@id='employ_0a19']
            career = response.xpath("//section[@id='employability']/div").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<div id="content_div_43747">
<h1>Applying for a research degree</h1><p>To apply for your postgraduate research place, you will need to complete our online application form. You will need to have at hand your supporting documents ready to upload when you start the online application. We have four entry points: October, January, April and July. From September 2018, this will change to three entry points, in January, May and September.&nbsp;For the Salford DBA, there are two entry points: April and September.</p><p>Please submit your application with a minimum of six weeks before the date you are aiming to register.</p><ul><li>Degree certificates</li><li>Transcripts</li><li><a href="http://www.salford.ac.uk/__data/assets/pdf_file/0018/104841/18-02-23-Vouch-List-Equivalent-qualifications-to-English-GCSE-Grade-C.pdf">English language qualifications</a></li><li><a href="http://www.advice.salford.ac.uk/page/visa">Passport details (required for International applicants)</a></li><li><a href="http://www.salford.ac.uk/__data/assets/pdf_file/0003/631686/Writing-a-Research-Proposal-Guidance.pdf" title="How to write a research proposal" target="_blank">Research proposal</a></li></ul><p>If you are applying for a PhD by published works, please go <a href="https://shop.salford.ac.uk/product-catalogue/university-goods-and-services/phd-by-published-works/phd-by-published-works-application-fee">to the online shop to make your payment</a> before completing your application.</p><p>For help preparing a research proposal for the PhD in Business, Management and Law, download our <a href="http://www.salford.ac.uk/__data/assets/pdf_file/0009/1572147/HowtoWriteaResearchProposal2018.pdf" title="PhD Research proposal guidance" target="_blank">Research Proposal Guidance</a>. For the Salford DBA, download our <a href="http://www.salford.ac.uk/__data/assets/pdf_file/0008/1559996/Guidance-on-Writing-a-DBA-Research-Proposal-PDF.pdf" title="Guidance on Writing a DBA Research Proposal" target="_blank">Guidance on Writing a DBA Research Proposal</a>.</p><h2>English Language Requirements</h2><p>If you have not yet taken an English Language test please note that availability of these and the time taken to receive certificates of results can vary depending on the time of year. For further information and to check timescales and availability please visit:</p><p><strong>IELTS</strong> - <a href="http://www.ielts.org/">http://www.ielts.org/</a><br /><strong>Pearson Test of English Academic</strong> - <a href="http://www.pearsonpte.com/testme">www.pearsonpte.com/testme</a></p><p>For details of other English Language tests accepted for the UKVI, please visit:<br /><a href="http://www.ukba.homeoffice.gov.uk/sitecontent/applicationforms/new-approved-english-tests.pdf">http://www.ukba.homeoffice.gov.uk/sitecontent/applicationforms/new-approved-english-tests.pdf</a></p><h2>Guide to submitting your application</h2><ol><li>When you first enter the online application you will be asked to create an account</li><li>You will then receive an email with your login PIN and password</li><li>You can re-enter and complete your application at times convenient to you</li><li>Fill in application details &ndash; using the guidance within the form</li><li>Upload your supporting documents</li><li>Once you have submitted your application you can print a copy of your application. However you cannot re-enter and make any changes at this stage</li></ol><h3>What happens next?</h3><ul><li>When you submit your online application you will receive and acknowledgement by email</li><li>You&rsquo;ll be notified of the outcome of your application in writing.</li><li>If you have any questions about the progress of your application please <a href="mailto:pg-admissions@salford.ac.uk">email admissions</a></li></ul><h3>Relevant work experience</h3><p><strong>We try to make applying to Salford as flexible and straightforward as possible.</strong></p><p>We&rsquo;re not just interested in exams you&rsquo;ve passed and certificates you&rsquo;ve collected. If you&rsquo;ve gained enough relevant work experience &ndash; paid or voluntary &ndash; we&rsquo;ll take that into account through our Accreditation of Prior Learning (APL) and Accreditation of PriorExperiential Learning (APEL) schemes.</p><h2>How to prepare a research proposal</h2><p>The research proposal is a crucial part of your application.</p><p>You should discuss your proposal with the <strong>Postgraduate Research Admissions Contact</strong> of the School to which you are applying, to make sure you understand what is expected in your subject area.</p><p>For help preparing a research proposal for the PhD in Business, Management and Law, download our <a href="http://www.salford.ac.uk/__data/assets/pdf_file/0009/1572147/HowtoWriteaResearchProposal2018.pdf" title="PhD Research proposal guidance" target="_blank">Research Proposal Guidance</a>. For the Salford DBA, download our <a href="http://www.salford.ac.uk/__data/assets/pdf_file/0008/1559996/Guidance-on-Writing-a-DBA-Research-Proposal-PDF.pdf" title="Guidance on Writing a DBA Research Proposal" target="_blank">Guidance on Writing a DBA Research Proposal</a>.&nbsp;</p><p>When submitting an application, make sure that the specialist area you wish to study is covered by a member of staff at the University:</p><ul><li>Check individual staff entries on the <a href="http://www.salford.ac.uk/research/research-centres">Research Centre sites</a> that relate to your area</li><li>Explore <a href="http://www.seek.salford.ac.uk/">staff profiles</a> and check current research interests</li><li>Take note of the relevant Research Administrator listed below you will need it when completing your online application</li></ul>
</div>
"""]))
            print("item['apply_proces_en']: ", item['apply_proces_en'])

            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<p><strong>Postgraduate</strong></p><p>(4 year) Bachelor degrees with a GPA 2.7/4.0 or 70% from a National University; or from a Project 211 University with a GPA 2.6/4.0 or 65%; or from a Private University with GPA 2.75/4.0 or 75%.</p>"""]))
            print("item['require_chinese_en']: ", item['require_chinese_en'])
            yield item
        except Exception as e:
            with open(item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)
