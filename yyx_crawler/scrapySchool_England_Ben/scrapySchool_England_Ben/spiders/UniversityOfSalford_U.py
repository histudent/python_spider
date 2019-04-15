import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime

class UniversityOfSalford_USpider(CrawlSpider):
    name = "UniversityOfSalford_U"
    start_urls = ["https://www.salford.ac.uk/study/a-z-courses?root_node_selection=275503&page_asset_listing_279643_submit_button=Submit&queries_subject_query_posted=1&queries_subject_query=&current_result_page=1&results_per_page=0&submitted_search_category=&mode=&result_279643_result_page=A"]

    rules = (
        Rule(LinkExtractor(allow=r"result_279643_result_page=[A-Z@]"), follow=True, callback='parse_url'),
    )

    def parse_url(self, response):
        # print("===", response.url)
        links = response.xpath("//div[@id='atoz']//div[@class='list-group']/a/@href").extract()

        # 组合字典
        programme_dict = {}
        programme_list = response.xpath("//div[@id='atoz']//div[@class='list-group']/a//text()").extract()
        clear_space(programme_list)

        for link in range(len(links)):
            url = "https://www.salford.ac.uk" + links[link]
            programme_dict[url] = programme_list[link]

        # print(len(links))
        links = list(set(links))
        # print(len(links))
#         links = ["https://www.salford.ac.uk/ug-courses/aeronautical-engineering-with-foundation-year",
# "https://www.salford.ac.uk/ug-courses/civil-engineering-with-foundation-year",
# "https://www.salford.ac.uk/ug-courses/mechanical-engineering-with-foundation-year", ]
        for link in links:
            url = "https://www.salford.ac.uk" + link
            # url = link
            yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "https://www.salford.ac.uk/"
        item['university'] = "University of Salford"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        item['location'] = 'The Crescent, Salford, M5 4WT, UK'
        print("===========================")
        print(response.url)
        item['major_type1'] = response.meta.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            # 专业、学位类型
            programme = response.xpath("//div[@id='content']/div[@class='col-md-12']/div[@class='course-title']/div[@class='row']/div[@class='col-sm-8 col-md-8']/h1//text()").extract()
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en']: ", item['programme_en'])

            if "Foundation" not in item['programme_en'] and item['degree_name'] != "Graduate Certificate":
                degree_type = response.xpath("//div[@id='content']/div[@class='col-md-12']/div[@class='course-title']/div[@class='row']/div[@class='col-sm-8 col-md-8']/h2//text()").extract()
                item['degree_name'] = ''.join(degree_type).replace("(Hons)", "").strip()
                print("item['degree_name']: ", item['degree_name'])

                # //div[@id='content']/div[@class='col-md-12']/div[@class='course-title']/div[@class='row']/div[@class='col-sm-8 col-md-8']/p
                department = response.xpath("//strong[contains(text(), 'School -')]/../text()").extract()
                item['department'] = ''.join(department).strip()
                # print("item['department']: ", item['department'])

                start_date = response.xpath("//strong[contains(text(), 'Start Date(s):')]/../text()").extract()
                clear_space(start_date)
                # print("start_date: ", start_date)
                if ";" in ''.join(start_date):
                    start_date = ''.join(start_date).split(";")
                    for s in start_date:
                        item['start_date'] += getStartDate(s) + ","
                else:
                    item['start_date'] = getStartDate(''.join(start_date))
                item['start_date'] = item['start_date'].strip().strip(",").strip()
                # print("item['start_date']: ", item['start_date'])



                # //strong[contains(text(), 'Fees')]/../following-sibling::p[contains(text(), 'International -')]
                tuition_fee = response.xpath("//strong[contains(text(), 'Fees')]/../following-sibling::p[contains(text(), 'International')]//text()").extract()
                clear_space(tuition_fee)
                # print("tuition_fee: ", tuition_fee)
                tuition_fee_re = re.findall(r"£\d+,\d+", ''.join(tuition_fee))
                # print("tuition_fee_re: ", tuition_fee_re)
                if len(tuition_fee_re) > 0:
                    item['tuition_fee'] = getTuition_fee(''.join(tuition_fee_re))
                # print("item['tuition_fee']: ", item['tuition_fee'])

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
                    if len(modules_en) == 0:
                        modules_en = response.xpath("//h2[contains(text(),'Course Structure')]|//h2[contains(text(),'Course Structure')]/following-sibling::*").extract()
                item['modules_en'] = remove_class(clear_lianxu_space(modules_en)) # .replace("&nbsp;", "")
                item['modules_en'] = item['modules_en'].encode('utf-8').decode("unicode-escape").replace("Â ", "")
                # print("item['modules_en']: ", item['modules_en'])

                alevel = response.xpath("//*[contains(text(),'A level')]/following-sibling::td//text()").extract()
                item['alevel'] = clear_lianxu_space(alevel)
                # print("item['alevel']: ", item['alevel'])

                ib = response.xpath("//*[contains(text(),'International Baccalaureate')]/following-sibling::td//text()").extract()
                item['ib'] = clear_lianxu_space(ib)
                # print("item['ib']: ", item['ib'])

                # //section[@id='requirements']/div
                entry_requirements = response.xpath("//section[@id='requirements']/div//text()").extract()
                # item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
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

                ielts_dict = get_ielts(item['ielts_desc'].replace("level 4, 5, 6 ", "").strip())
                item['ielts'] = ielts_dict.get('IELTS')
                item['ielts_l'] = ielts_dict.get('IELTS_L')
                item['ielts_s'] = ielts_dict.get('IELTS_S')
                item['ielts_r'] = ielts_dict.get('IELTS_R')
                item['ielts_w'] = ielts_dict.get('IELTS_W')
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

                item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<div class="col-xs-12 col-sm-6 col-md-6 col-lg-6"><h1>How to apply?</h1>
</div>
<div class="clearfix"></div>
<div id="content_container_1135928">
<p class="lead">We try to make applying to Salford as flexible and straightforward as possible.</p><p>If you have any queries about the application process, please contact the Course Enquiries Team on 0161 295 4545 (choose option 1) or <a href="mailto:enquiries@salford.ac.uk">enquiries@salford.ac.uk</a></p><p>The majority of our undergraduate applications are via UCAS, however there are some exceptions. The normal closing date for UCAS applications for September entry is 15 January (although if you are at school or college, they may ask you to fill it in earlier to give them time to prepare your reference). Applications received after this date may still be considered if the course is not full. If you apply late you are advised to check the UCAS website for course availability first. To find out more about how to apply and the different options available, we have given some guidance below.</p><p><strong>If you're interested in applying through clearing, please see further details below.</strong></p>
</div>
<div class="accordion-inner" id="accordion_1421686" role="tablist" aria-multiselectable="true">
<div class="panel panel-default">
<div class="panel-heading" role="tab" id="1421686_1">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion_1421686" href="#collapse_1421686_1" aria-expanded="false" aria-controls="collapse_sub_1" class="collapsed">
          Applying through Clearing?
        </a>
      </h4>
    </div>
    <div id="collapse_1421686_1" class="panel-collapse collapse" role="tabpanel" aria-labelledby="1421686_1">
      <div class="panel-body">
<div id="content_container_1615870">
<p>Clearing is applicable to those who have not yet submitted an application or those who are not yet holding any offers. During this time, universities can take applications to fill any course vacancies they may have. UCAS will list course availability so you can take a look on <a href="http://www.ucas.com">www.ucas.com</a> for more information. Despite popular belief, clearing opens at 9.00am on 5 July 2018 so potential applicants needn&rsquo;t wait until Results Day. You can find more information about this process <a href="https://www.ucas.com/undergraduate/results-confirmation-and-clearing/what-clearing">here.</a></p><p>If you'd like to apply to Salford through clearing, or have any questions at all about the process, please give our hotline a call on 0300 555 5030 and one of our friendly team can help you. The lines are open 9.00am to 5.00pm Monday to Thursday and 10.00am to 4.00pm on Friday. Please ensure you have an idea of what course or subject area you&rsquo;re interested in and that you have details of all your current qualifications to hand when you call. This means we'll be able to advise you of the best options to match your interests and qualifications.</p><p>If you are successful in gaining a place through clearing, you will need to either attach to the University via UCAS Track or complete a direct application form, depending on your current circumstances. We can help advise you of this when you call.</p>
</div>
      </div>
    </div>
</div><div class="panel panel-default">
<div class="panel-heading" role="tab" id="1421686_2">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion_1421686" href="#collapse_1421686_2" aria-expanded="false" aria-controls="collapse_sub_2" class="collapsed">
          Entry requirements
        </a>
      </h4>
    </div>
    <div id="collapse_1421686_2" class="panel-collapse collapse" role="tabpanel" aria-labelledby="1421686_2">
      <div class="panel-body">
<div id="advice_and_guidance">
<p><script>(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){     (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),     m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)     })(window,document,'script','//www.google-analytics.com/analytics.js','ga');     ga('create', 'UA-2643712-2', 'salford.ac.uk');     ga('require', 'displayfeatures');     ga('require', 'linkid', 'linkid.js');     ga('send', 'pageview');</script></p><div id="page"><div><div><div id="content_div_44347"><p>From A level to Access to HE diplomas to International Baccalaureate &ndash; our entry requirements are wide and varied and we recognise a wide range of qualifications from around the world.</p><p>If you are a UK applicant leaving school or college we accept the following qualifications:</p><ul><li>A/AS level</li><li>Scottish Higher/Advanced Higher</li><li>14 to 19 Advanced Diplomas</li><li>the International Baccalaureate</li><li>Welsh Baccalaureate</li><li>BTEC Awards</li><li>AQA Baccalaureate</li><li>Cambridge Pre-U</li><li>Access to Higher Education Diploma</li></ul><p>We&rsquo;re committed to widening access to higher education for all sections of the community and so are as flexible as possible in our admissions policy.</p></div></div></div></div>
</div>
      </div>
    </div>
</div><div class="panel panel-default">
<div class="panel-heading" role="tab" id="1421686_3">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion_1421686" href="#collapse_1421686_3" aria-expanded="false" aria-controls="collapse_sub_3" class="collapsed">
          The UCAS application process
        </a>
      </h4>
    </div>
    <div id="collapse_1421686_3" class="panel-collapse collapse" role="tabpanel" aria-labelledby="1421686_3">
      <div class="panel-body">
<div id="advice_and_guidance">
<div id="page"><div><div><div id="content_div_44326"></div><h4>APPLYING VIA UCAS</h4></div></div></div><p>You can apply online via the&nbsp;<a href="http://www.ucas.com/students/apply" target="_blank"><u>UCAS website</u></a>. Your school or college should help you to access this service, and will give you a buzzword which you will need to register. You can also use the service if you&rsquo;re applying independently in the UK and overseas.</p><p>Take some time to check your online application before you submit it. It&rsquo;s important that you take care when completing the 'choices' section and use the correct institution codes and programme codes.</p><p>You can apply for up to five programmes, so make sure you think through your options carefully before applying. Also check that the 'education' section displays your correct qualification details. You should then forward your application on to your referee, who will check your application, provide the reference and forward the application to UCAS. If you are applying independently, you will be responsible for obtaining and adding the reference yourself.</p><p>It costs £23 to apply for two-five choices. If, however, you wish to only apply to the University of Salford and you are only applying for one programme, you may use a single entry at a fee of £12. You may pay online using a credit or debit card, or alternatively if you are applying from your school or college they may choose to be invoiced.</p><p>You can follow the progress of your application 24 hours a day, seven days a week using UCAS&nbsp;<cite>Track</cite> by logging on to&nbsp;<a href="http://www.ucas.com" target="_blank"><u>www.ucas.com</u></a>.</p><p>If you experience any difficulties with Apply you should contact the UCAS Customer Services team:<br />T +44 (0)871 468 0468</p><p>If you would like further help from the University, please contact:</p><p>Central Admissions<br />T: 0161 295 4545<br /><a href="mailto:enquiries@salford.ac.uk"><u>enquiries@salford.ac.uk</u></a></p><p>All applications should be made via the UCAS website, except for:</p><ul><li>applications for part-time courses and BSc (Hons) Nursing Studies</li><li>applications for the International Foundation Year</li><li>applications for post qualifying Health and Social care courses and single modules</li><li>applications for International and the Graduate Certificate in Management (GCIM)</li></ul><p>If the above applies to you, please see the &lsquo;Alternative application process&rsquo; section on this page for more details of how to apply.</p>
</div>
      </div>
    </div>
</div><div class="panel panel-default">
<div class="panel-heading" role="tab" id="1421686_4">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion_1421686" href="#collapse_1421686_4" aria-expanded="false" aria-controls="collapse_sub_4" class="collapsed">
          UCAS applications: key information
        </a>
      </h4>
    </div>
    <div id="collapse_1421686_4" class="panel-collapse collapse" role="tabpanel" aria-labelledby="1421686_4">
      <div class="panel-body">
<div id="content_container_1136542">
<p>When applying, make sure you use the correct codes:</p><p>Salford institution code name:&nbsp;<strong>SALF</strong></p><p>Salford institution code:&nbsp;<strong>S03</strong></p><p>Campus code: there are no campus codes at Salford - leave this blank</p><p>We will start receiving applications for entry in autumn 2018 from early September 2017</p><p>The normal closing date for applications is&nbsp;<strong>15 January 2018</strong> (although if you are at school or college, they may ask you to fill it in earlier to give them time to prepare your reference). Applications received after this date may still be considered if the course is not full. If you apply late, please check the UCAS website for course availability first.</p><p><strong>UCAS Extra:</strong> 25 February &ndash; 4 July 2018</p><p><strong>Clearing starts:</strong> 5 July 2018</p><p><strong>A level results:</strong> 16 August 2018</p>
</div>
      </div>
    </div>
</div><div class="panel panel-default">
<div class="panel-heading" role="tab" id="1421686_5">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion_1421686" href="#collapse_1421686_5" aria-expanded="false" aria-controls="collapse_sub_5" class="collapsed">
          Alternative application process
        </a>
      </h4>
    </div>
    <div id="collapse_1421686_5" class="panel-collapse collapse" role="tabpanel" aria-labelledby="1421686_5">
      <div class="panel-body">
<div id="advice_and_guidance">
<h3>INTERNATIONAL FOUNDATION YEAR APPLICATIONS</h3><p>If you would like to apply for our International Foundation Year you will need to download and complete the application form.</p><p>You should then email it to&nbsp;<a href="mailto:international@salford.ac.uk">IFY-Admissions@salford.ac.uk</a> or post the completed form to the address on the front cover of the form.</p><p>NOTE: Together with the form, you will also need to send us a photocopy of the identity page of your passport and proof of your current level of English.</p><ul type="disc"><li><a href="http://www.salford.ac.uk/__data/assets/pdf_file/0005/1190894/0518-International-foundation-year-salford-2017.pdf" target="_blank">International Foundation Year application form</a></li></ul><h3>POST QUALIFYING HEALTH AND SOCIAL CARE COURSES AND SINGLE MODULE APPLICATIONS</h3><p>If your Trust is part of the North West SHA-SLA agreement, contact your&nbsp;<strong>CPD Lead to agree funding</strong>. You must then apply through the NHS CPD Apply system: <a href="http://www.cpd-applynw.nhs.uk"><strong>www.cpd-applynw.nhs.uk</strong></a></p><p><strong> </strong></p><p>If you are self-funding or your workplace is funding your course or single module, please complete the appropriate application form below and send directly to the University. Full details on who to send the form to are included on the form. If workplace funded, you will also need to supply a letter&nbsp;&nbsp;from your Trust stating that they will be funding your study.</p><p><strong> </strong></p><h3>APPLICATION FORMS</h3><p><strong>LEVEL 5 AND LEVEL 6 (UNDERGRADUATE/SINGLE MODULE) APPLICATION FORM</strong></p><p><a href="http://www.salford.ac.uk/__data/assets/pdf_file/0008/974168/RU1095-UGApplicationFormNov2016v3.pdf"><strong>Download Undergraduate Application Form (please note you will need to provide two references)</strong></a></p><p><strong> </strong></p><p><strong>LEVEL 7 (MASTERS/SINGLE MODULE) APPLICATION FORM</strong></p><p><a href="http://www.salford.ac.uk/__data/assets/pdf_file/0007/79522/RU12483-PGApplicationNov2016.pdf"><strong>Download Postgraduate Application Form (please note you will need to provide two references)</strong></a></p><h3>INTERNATIONAL APPLICATIONS</h3><p>We welcome applications from international students. Applicants from outside the United Kingdom must apply through UCAS.</p><p>Students from the following countries should submit their applications to UCAS through the appropriate overseas office in London as listed in the UCAS Handbook: Cyprus, Guyana, India, Luxembourg, Thailand. Applicants from other countries should send their applications direct to UCAS. (Salford participates&nbsp;in the British Council Education Promotion Service and advisers are available in your local British Council Office).</p><p>Applications for the&nbsp;<strong>Graduate Certificate in Management</strong> should be made by completing the&nbsp;<a href="http://www.salford.ac.uk/__data/assets/pdf_file/0008/974168/RU1095-UGApplicationFormNov2016v3.pdf" target="_blank">undergraduate application form and returned to the address on the form</a>. For more information,&nbsp;see our section specifically for&nbsp;<a href="http://www.salford.ac.uk/international/how-to-apply">international students</a>.</p><h3>APPLYING FOR A TOP-UP COURSE</h3><p>If you are currently studying a Foundation Degree at one of our Partner Colleges and wish to top up your award to an Honours Degree, you should apply directly to the University by completing our&nbsp;<a href="http://www.salford.ac.uk/__data/assets/pdf_file/0008/974168/RU1095-UGApplicationFormNov2016v3.pdf">Undergraduate Studies direct application form</a>.</p><p>Information on the courses available to you to apply for are available from staff at your College.</p>
</div>
      </div>
    </div>
</div><div class="panel panel-default">
<div class="panel-heading" role="tab" id="1421686_6">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion_1421686" href="#collapse_1421686_6" aria-expanded="false" aria-controls="collapse_sub_6" class="collapsed">
          Writing your personal statement
        </a>
      </h4>
    </div>
    <div id="collapse_1421686_6" class="panel-collapse collapse" role="tabpanel" aria-labelledby="1421686_6">
      <div class="panel-body">
<div id="content_container_1136542">
<p>Writing your personal statement is a key part of the UCAS application process, but we know that it can sometimes feel like a daunting task. <br /><img width="1" height="15" alt="http://www.salford.ac.uk/__data/assets/image/0005/660326/spacer.gif" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAAPCAMAAAASwVXLAAAAAXNSR0ICQMB9xQAAAANQTFRFAAAAp3o92gAAAAF0Uk5TAEDm2GYAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAZdEVYdFNvZnR3YXJlAE1pY3Jvc29mdCBPZmZpY2V/7TVxAAAAC0lEQVQY02NgwAcAAB4AAcmYI4MAAAAASUVORK5CYII=" /><br /> Here are our top five tips for a winning personal statement&hellip;</p><h4>1. PREPARATION, PREPARATION, PREPARATION</h4><p>Start to prepare your personal statement early on. Without thinking about a structure, it will be harder for you to collect and organise your thoughts later on. Begin with a mind map, noting down anything you think might be relevant, such as your skills, qualities, likes, dislikes and experience. Formulate this into a plan, and use your plan to help structure your first draft.</p><h4>2. capture the attention of the reader</h4><p>Capture the attention of the reader with a sharp introduction; use positive language to show them you&rsquo;re enthusiastic about your chosen subject. The main section of your statement should demonstrate what you have learned from the experiences you are writing about, and how this is relevant to the course you want to study. Tell the reader about your skills and qualities, and how these contribute to your understanding of the subject.</p><h4>3. TELL THEM ABOUT YOURSELF</h4><p>Your work experience and interests are also important, as this can highlight why you&rsquo;re the perfect student for the course. Universities want to know that you&rsquo;ll become an active member of the student community, not just succeed academically. Are you part of a club, do you play any sports, or have an unusual hobby?&nbsp;&nbsp;Make sure you mention these here. Remember; entry requirements are transparent, you and your experiences are unique.</p><h4>4. SELL, SELL, SELL</h4><p>Conclude your personal statement by summarising your key strengths, and reiterate that you are ready (both socially and academically) for university life. Be confident, keep it positive, and really sell yourself.</p><h4>5. LOSE THE WAFFLE</h4><p>Remember that you have a limited number of words, so be clear and concise &ndash; don&rsquo;t waffle! Don&rsquo;t expect your first draft to be perfect; ask a teacher or careers advisor to check over it for you so that your spelling and grammar are spot on.<br /><img width="1" height="15" alt="http://www.salford.ac.uk/__data/assets/image/0005/660326/spacer.gif" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAAPCAMAAAASwVXLAAAAAXNSR0ICQMB9xQAAAANQTFRFAAAAp3o92gAAAAF0Uk5TAEDm2GYAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAZdEVYdFNvZnR3YXJlAE1pY3Jvc29mdCBPZmZpY2V/7TVxAAAAC0lEQVQY02NgwAcAAB4AAcmYI4MAAAAASUVORK5CYII=" /></p>
</div>
      </div>
    </div>
</div><div class="panel panel-default">
<div class="panel-heading" role="tab" id="1421686_7">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion_1421686" href="#collapse_1421686_7" aria-expanded="false" aria-controls="collapse_sub_7" class="collapsed">
          Salford Alternative Entry Scheme
        </a>
      </h4>
    </div>
    <div id="collapse_1421686_7" class="panel-collapse collapse" role="tabpanel" aria-labelledby="1421686_7">
      <div class="panel-body">
<div id="content_container_1136542">
<p>At the University of Salford we believe that everyone should be able to achieve their full potential.</p><p>If you&rsquo;ve been out of education for a while, want to further your career or simply want to study in a field that you&rsquo;re passionate about, the Salford Alternative Entry Scheme (SAES) could be for you.</p><p><strong>How can I apply?</strong></p><ul><li>Submit your course application as you would normally through UCAS.</li><li>We will then recommend you to SAES if you&rsquo;re eligible (you&rsquo;ll be notified of this recommendation via UCAS or by our admissions team getting in touch with you).&nbsp;&nbsp;</li></ul><p>Successful applicants will be contacted through SAES about an assessment.&nbsp;</p><p>There are two different entry routes depending on your course. If the course you&rsquo;re studying is related to Business and Law, Health Sciences, Environment &amp; Life Sciences or Arts &amp; Media, you will be assessed through Accreditation for Prior Learning.&nbsp;If the course you&rsquo;re studying is related to Nursing, Midwifery, Social Work &amp; Social Sciences, Computing, Science &amp; Engineering or the Built Environment, you will be assessed through a MSAP-UK test.</p><p>For further information about the Salford Alternative Entry Scheme, please see our dedicated <a href="http://www.salford.ac.uk/study/undergraduate/salford-alternative-entry-scheme/entry-routes" target="_blank">SAES webpage</a>.</p>
</div>
      </div>
    </div>
</div><div class="panel panel-default">
<div class="panel-heading" role="tab" id="1421686_8">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion_1421686" href="#collapse_1421686_8" aria-expanded="false" aria-controls="collapse_sub_8" class="collapsed">
          Part-time and accelerated degree courses
        </a>
      </h4>
    </div>
    <div id="collapse_1421686_8" class="panel-collapse collapse" role="tabpanel" aria-labelledby="1421686_8">
      <div class="panel-body">
<div id="content_container_1136542">
<p>Part-time applications are made directly to the University. If you want to apply to study a part-time undergraduate qualification please contact our&nbsp;<strong>Course Enquiries Service</strong> on&nbsp;<strong>0161 295 4545</strong> for more information.</p><p>You&rsquo;ll need to complete an <a href="http://www.salford.ac.uk/__data/assets/pdf_file/0008/974168/RU1095-UGApplicationFormNov2016v3.pdf" target="_blank"><u>Undergraduate Studies direct application form</u></a>.</p><p>Please note you will need to provide two references.</p><p>If you&rsquo;re applying for one of our accelerated courses in the School of the Built Environment, these applications are made through<a href="http://www.salford.ac.uk/study/undergraduate/how-to-apply/#section1"> UCAS</a>. This applies to both the full-time and the day-release versions of the course, with durations of two or three years respectively. Only the standard part-time courses of five years&rsquo; duration require direct applications.</p>
</div>
      </div>
    </div>
</div><div class="panel panel-default">
<div class="panel-heading" role="tab" id="1421686_9">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion_1421686" href="#collapse_1421686_9" aria-expanded="false" aria-controls="collapse_sub_9" class="collapsed">
          Applying for 2019 Entry?
        </a>
      </h4>
    </div>
    <div id="collapse_1421686_9" class="panel-collapse collapse" role="tabpanel" aria-labelledby="1421686_9">
      <div class="panel-body">
<div id="content_container_1572153">
<p>If you&rsquo;re looking to apply for a course starting in 2019, you can start working on your application through UCAS from 22 May, for submission from 5 September onwards.</p><p>In the meantime, there are plenty of ways to get to know us better:</p><p>Visit us on our next Open Day on 23 June &ndash; book your place <a href="http://www.salford.ac.uk/study/visit/undergraduate-open-days" target="_blank">here</a></p><p>Follow us on social media for live updates:</p><p>Twitter.com/@SalfordUni</p><p>Snapchat: Salforduni</p><p>Instagram:@SalfordUni</p>
</div>
      </div>
    </div>
</div><div class="panel panel-default">
<div class="panel-heading" role="tab" id="1421686_10">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion_1421686" href="#collapse_1421686_10" aria-expanded="false" aria-controls="collapse_sub_10" class="collapsed">
          Higher and Degree Apprenticeship Programmes
        </a>
      </h4>
    </div>
    <div id="collapse_1421686_10" class="panel-collapse collapse" role="tabpanel" aria-labelledby="1421686_10">
      <div class="panel-body">
<div id="content_container_1572153">
<p>If you're looking to apply for a Higher or Degree Apprenticeship programme offered by the University of Salford then you will need to visit our apprenticeship webpage below and contact us via the online form. Applications for apprenticeship programmes do not go through the traditional UCAS system - you will apply directly to the University via a separate application form.&nbsp;</p><p><a href="https://www.salford.ac.uk/higher-and-degree-apprenticeships">www.salford.ac.uk/degree-apprenticeships</a></p><p>In order to apply for a Higher or Degree Apprenticeship you must be employed full-time in a relevant role and your employer must be willing to support you through the programme.</p><p>All apprenticeship roles are listed on the GOV.UK site below:&nbsp;</p><p><a href="https://www.gov.uk/apply-apprenticeship" target="_blank">www.gov.uk/apply-apprenticeship</a></p>
</div>
      </div>
    </div>
</div>
</div>"""]))
                # print("item['apply_proces_en']: ", item['apply_proces_en'])

                item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<h2>Undergraduate</h2><p>Students who have completed a recognised foundation year or the first year of a relevant degree programme at a Chinese university may be considered</p>"""]))
                # print("item['require_chinese_en']: ", item['require_chinese_en'])

                duration = response.xpath(
                    "//strong[contains(text(), 'Duration')]/../following-sibling::*[position()<3]//text()").extract()
                clear_space(duration)
                print("duration: ", duration)
                # duration_str = ''.join(duration)

                if len(duration) == 1:
                    duration_list = getIntDuration(duration[0])
                    if len(duration_list) == 2:
                        item['duration'] = duration_list[0]
                        item['duration_per'] = duration_list[-1]
                else:
                    item['duration'] = ', '.join(duration).replace("Fees:", "").strip().strip(',').strip()
                print("item['duration'] = ", item['duration'])
                print("item['duration_per'] = ", item['duration_per'])

                ucascode = response.xpath(
                    "//strong[contains(text(),'UCAS Code:')]/..//text()").extract()
                clear_space(ucascode)
                print("ucascode: ", ucascode)
                if len(ucascode) > 0:
                    # if len(ucascode[-1]) == 4:
                    #     item['ucascode'] = ucascode[-1]
                    # else:
                    item['ucascode'] = ucascode[-1]
                print("item['ucascode'] = ", item['ucascode'])
                yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)
