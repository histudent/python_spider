# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_Australian_ben.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_ben.getItem import get_item
from scrapySchool_Australian_ben.getTuition_fee import getTuition_fee
from scrapySchool_Australian_ben.items import ScrapyschoolAustralianBenItem
from scrapySchool_Australian_ben.remove_tags import remove_class
from scrapySchool_Australian_ben.getStartDate import getStartDate
from scrapySchool_Australian_ben.getDuration import getIntDuration
from lxml import etree
import requests

class TheUniversityOfMelbourne_USpider(scrapy.Spider):
    name = "TheUniversityOfMelbourne_U"
    start_urls = ["https://coursesearch.unimelb.edu.au/undergrad"]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36"}

    def parse(self, response):
        links = response.xpath("//div[@class='inner-wrapper']//div[5]//div[2]//div/a/@href").extract()
        # print("majors link = ", links)
        print(len(links))
        links = list(set(links))
        print(len(links))

        links = ["https://study.unimelb.edu.au/find/courses/specialisation/management/",
                 "https://study.unimelb.edu.au/find/courses/specialisation/business/",
                 "https://coursesearch.unimelb.edu.au/majors/73-management",
                 "https://study.unimelb.edu.au/find/courses/major/screen-and-cultural-studies/",
                 "https://study.unimelb.edu.au/find/courses/specialisation/accounting/",
                 "https://study.unimelb.edu.au/find/courses/specialisation/actuarial-studies/",
                 "https://study.unimelb.edu.au/find/courses/major/ancient-world-studies",
                 "https://study.unimelb.edu.au/find/courses/major/anthropology",
                 "https://study.unimelb.edu.au/find/courses/major/arabic-studies",
                 "https://study.unimelb.edu.au/find/courses/major/art-history",
                 "https://study.unimelb.edu.au/find/courses/major/asian-studies",
                 "https://study.unimelb.edu.au/find/courses/major/australian-indigenous-studies",
                 "https://study.unimelb.edu.au/find/courses/major/chinese-societies",
                 "https://study.unimelb.edu.au/find/courses/major/chinese-studies",
                 "https://study.unimelb.edu.au/find/courses/major/classics",
                 "https://study.unimelb.edu.au/find/courses/major/creative-writing",
                 "https://study.unimelb.edu.au/find/courses/major/criminology",
                 "https://study.unimelb.edu.au/find/courses/specialisation/economics",
                 "https://study.unimelb.edu.au/find/courses/major/english-and-theatre-studies",
                 "https://study.unimelb.edu.au/find/courses/major/french-studies",
                 "https://study.unimelb.edu.au/find/courses/major/gender-studies",
                 "https://study.unimelb.edu.au/find/courses/major/geography",
                 "https://study.unimelb.edu.au/find/courses/major/german-studies",
                 "https://study.unimelb.edu.au/find/courses/major/hebrew-and-jewish-studies",
                 "https://study.unimelb.edu.au/find/courses/major/history",
                 "https://study.unimelb.edu.au/find/courses/major/indonesian-studies",
                 "https://study.unimelb.edu.au/find/courses/major/islamic-studies",
                 "https://study.unimelb.edu.au/find/courses/major/italian-studies",
                 "https://study.unimelb.edu.au/find/courses/major/japanese-studies",
                 "https://study.unimelb.edu.au/find/courses/major/linguistics-and-applied-linguistics",
                 "https://study.unimelb.edu.au/find/courses/major/media-and-communications",
                 "https://study.unimelb.edu.au/find/courses/major/philosophy",
                 "https://study.unimelb.edu.au/find/courses/major/politics-and-international-studies",
                 "https://study.unimelb.edu.au/find/courses/major/psychology",
                 "https://study.unimelb.edu.au/find/courses/major/russian-studies",
                 "https://study.unimelb.edu.au/find/courses/major/history-and-philosophy-of-science",
                 "https://study.unimelb.edu.au/find/courses/major/screen-and-cultural-studies",
                 "https://study.unimelb.edu.au/find/courses/major/sociology",
                 "https://study.unimelb.edu.au/find/courses/major/spanish-and-latin-american-studies",
                 "https://study.unimelb.edu.au/find/courses/specialisation/finance/",
                 "https://study.unimelb.edu.au/find/courses/major/performance-design/",
                 "https://study.unimelb.edu.au/find/courses/major/creative-writing",
                 "https://study.unimelb.edu.au/find/courses/major/performance-design",
                 "https://study.unimelb.edu.au/find/courses/major/screen-and-cultural-studies",
"https://coursesearch.unimelb.edu.au/majors/51-film-and-television",
"https://coursesearch.unimelb.edu.au/majors/10-cell-and-developmental-biology",
"https://coursesearch.unimelb.edu.au/majors/52-music-theatre",
"https://coursesearch.unimelb.edu.au/majors/100-music-performance",
"https://coursesearch.unimelb.edu.au/majors/28-microbiology-and-immunology",
"https://coursesearch.unimelb.edu.au/majors/93-property",
"https://coursesearch.unimelb.edu.au/majors/70-business",
"https://coursesearch.unimelb.edu.au/majors/55-visual-art",
"https://coursesearch.unimelb.edu.au/majors/159-computing",
"https://coursesearch.unimelb.edu.au/majors/102-musicology-ethnomusicology",
"https://coursesearch.unimelb.edu.au/majors/164-graphic-design",
"https://coursesearch.unimelb.edu.au/majors/68-accounting",
"https://coursesearch.unimelb.edu.au/majors/154-interactive-composition",
"https://coursesearch.unimelb.edu.au/majors/77-construction",
"https://coursesearch.unimelb.edu.au/majors/92-urban-planning",
"https://coursesearch.unimelb.edu.au/majors/148-arts-minors",
"https://coursesearch.unimelb.edu.au/majors/26-mathematics-and-statistics",
"https://coursesearch.unimelb.edu.au/majors/146-screenwriting",
"https://coursesearch.unimelb.edu.au/majors/167-environmental-engineering-systems",
"https://coursesearch.unimelb.edu.au/majors/144-oral-health",
"https://coursesearch.unimelb.edu.au/majors/155-computational-biology",
"https://coursesearch.unimelb.edu.au/majors/169-theatre",
"https://coursesearch.unimelb.edu.au/majors/101-composition",
"https://coursesearch.unimelb.edu.au/majors/165-performance-design",
"https://coursesearch.unimelb.edu.au/majors/152-civil-systems",
"https://coursesearch.unimelb.edu.au/majors/168-acting",
"https://coursesearch.unimelb.edu.au/majors/75-architecture",
"https://coursesearch.unimelb.edu.au/majors/96-landscape-architecture",
"https://coursesearch.unimelb.edu.au/majors/9-biotechnology",
"https://coursesearch.unimelb.edu.au/majors/157-digital-technologies",
"https://coursesearch.unimelb.edu.au/majors/74-marketing",
"https://coursesearch.unimelb.edu.au/majors/153-jazz-and-improvisation",
"https://coursesearch.unimelb.edu.au/majors/166-data-science",
"https://coursesearch.unimelb.edu.au/majors/156-mechatronics-systems",
"https://coursesearch.unimelb.edu.au/majors/53-production",
"https://coursesearch.unimelb.edu.au/majors/69-actuarial-studies",
"https://coursesearch.unimelb.edu.au/majors/72-finance",
"https://coursesearch.unimelb.edu.au/majors/49-dance",
"https://coursesearch.unimelb.edu.au/majors/32-physics",
"https://coursesearch.unimelb.edu.au/majors/12-chemistry", ]
        for link in links:
            # url = "https://coursesearch.unimelb.edu.au" + link
            url = link
            yield scrapy.Request(url, callback=self.parse_programme_message)

    def parse_programme_message(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "The University of Melbourne"
        # item['country'] = 'Australia'
        # item['website'] = 'http://www.unimelb.edu.au/'
        item['url'] = response.url
        item['degree_type'] = 1
        print("=========================")
        print(response.url)
        try:
            programme = response.xpath("//div[@class='headline']/h1/text()|//h1[@id='page-header']//text()").extract()
            clear_space(programme)
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en']: ", item['programme_en'])

            # //div[@class='description']
            overview_en = response.xpath("//h3[contains(text(),'Careers')]/preceding-sibling::*|"
                                         "//section[@id='course-overview']//div[@class='course-section__main course-section__main-with-aside']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
            print("item['overview_en']: ", item['overview_en'])

            career_en = response.xpath("//h3[contains(text(),'Careers')]/preceding-sibling::*[1]/following-sibling::*").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            # print("item['career_en']: ", item['career_en'])

            modules = response.xpath("//div[@class='description']/following-sibling::*").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])
            modulesUrl = response.url+"what-will-i-study/"
            # print(modulesUrl)
            item['modules_en'] = self.parse_modules(modulesUrl)
            print("item['modules_en']: ", item['modules_en'])


            # https://futurestudents.unimelb.edu.au/admissions/entry-requirements/language-requirements/undergraduate-toefl-ielts
            item['ielts_desc'] = "an overall band score of 6.5 or more in the Academic International English Language Testing System (IELTS), with no bands less than 6.0"
            item["ielts"] = '6.5'
            item["ielts_l"] = '6.0'
            item["ielts_s"] = '6.0'
            item["ielts_r"] = '6.0'
            item["ielts_w"] = '6.0'

            item['toefl_code'] = '0974'
            item["toefl"] = '79'
            item["toefl_l"] = '13'
            item["toefl_s"] = '18'
            item["toefl_r"] = '13'
            item["toefl_w"] = '21'

            # https://futurestudents.unimelb.edu.au/admissions/applications/ug-int
            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<div class='main page-body' id='main-content' role='main'>
            <h1>International undergraduate</h1>
<div id="content_div_597198">
<p>Starting at university can be daunting, but applying for a place shouldn't be. Here's a guide to help you through the application process at Melbourne.</p><div class="col-1 first step-arrow"><h3>Step 1</h3></div><div class="col-5"><h2>Before you apply</h2><p>The first step is to figure out which course you want to study, and if you meet all of that course's entry requirements. At this stage, you should:</p><ul><li>Find <a href="http://coursesearch.unimelb.edu.au" target="_blank">the right course</a> for you, and make sure you meet the <a href="https://futurestudents.unimelb.edu.au/admissions/entry-requirements/undergraduate-international">entry requirements</a></li><li>If you're unsure, you may need to <a href="https://futurestudents.unimelb.edu.au/start-here">check if you're an international student</a></li><li>Check that you meet the <a href="https://futurestudents.unimelb.edu.au/admissions/entry-requirements/language-requirements">English language requirements</a></li><li>Make sure you're eligible for the appropriate <a href="http://www.services.unimelb.edu.au/international/visas/" target="_blank">visa to study in Australia</a></li><li>Find out what the <a href="https://futurestudents.unimelb.edu.au/admissions/fees/ug-intl">fees</a> for your course are and what <a href="https://scholarships.unimelb.edu.au">scholarships</a> are available to help you</li><li>Check to see if you're eligible for any of our <a href="https://futurestudents.unimelb.edu.au/admissions/high_achievers_programs">High Achievers' programs</a></li><li>Review our <a href="https://futurestudents.unimelb.edu.au/admissions/admission_with_credit">Admission with credit pages</a> if you are currently studying at another university or have completed post-secondary studies.</li><li>Look at the <a href="http://services.unimelb.edu.au/finaid/planning/cost_of_living" target="_blank">cost of living in Melbourne</a>, and what <a href="http://services.unimelb.edu.au/finaid" target="_blank">financial assistance</a> is available to you while you study.</li></ul><p>If you'd prefer to speak to someone in person about your application, contact a <a href="https://futurestudents.unimelb.edu.au/info/overseas-representatives">University of Melbourne representative</a> in your country.</p></div><hr /><div class="col-1 first step-arrow"><h3>Step 2</h3></div><div class="col-5"><h2>How to apply</h2><h3>Studying an Australian or NZ Year 12</h3><p>If you are studying any Australian or NZ year 12 program (including WACE/AUSMAT, SACE/SAM or NCEA) whether in Australia or an another country you should apply through the Victorian Tertiary Admissions Centre (VTAC). Full details about the VTAC application process can be found on the <a href="http://www.vtac.edu.au" target="_blank">VTAC website</a>. Through VTAC, you can list up to 8 course preferences. You should list courses in your order of preference with the course of greatest interest listed first. Be sure that your application is finalised by the <a href="http://www.vtac.edu.au/dates.html" target="_blank">VTAC due dates</a>.</p><p>If you have previously applied to the University of Melbourne via VTAC but were not offered a place or were offered but never enrolled, you should apply as a new student.</p><h3>Current University of Melbourne international students</h3><p>If you're an international student currently studying at the University of Melbourne and you wish to transfer to another University of Melbourne course, you must submit your transfer application via the <a href="http://www.vtac.edu.au/" target="_blank">Victorian Tertiary Admissions Centre (VTAC)</a>. Be sure that your application is finalised by the <a href="http://www.vtac.edu.au/dates.html" target="_blank">VTAC due dates</a>.</p><h3>All other international students</h3><p>You can <a href="https://futurestudents.unimelb.edu.au/admissions/applications/online-application-info">apply online</a> using our e-application.</p><p>Please ensure your application is received by us before the <a href="https://futurestudents.unimelb.edu.au/admissions/dates">relevant deadline</a>. An application fee of AUD$100 applies. This fee is non-refundable.</p><p>Alternatively, if you would prefer to apply in person in your own country, we have a number of overseas representatives in a variety of countries. Search our list of <a href="https://futurestudents.unimelb.edu.au/info/overseas-representatives">overseas representatives</a> to find one near you.</p><p>If you have accepted an offer from another institution in Australia, been granted a Confirmation of Enrolment (COE) and want to transfer to the University of Melbourne within the first six months of study you will need a letter of release from that institution. Please see our <a href="https://futurestudents.unimelb.edu.au/admissions/applications/other-applications/transferring-course/international_student_transfer_policy">International Student Transfer Policy for more details</a>.</p><p><strong>International Baccalaureate and US Advanced Placement students</strong></p><p>You can choose to have your IB or AP results sent directly to the University as soon as they are released. Please make sure you advise us in your application if you have authorised the release of your results.</p><p>University of Melbourne AP institution code: 9015<br /> University of Melbourne IB institution code: 002406</p><h3>Study abroad or exchange</h3><p>If you're interested in studying at Melbourne for a shorter period - one or two semesters - please refer to the <a href="http://www.mobility.unimelb.edu.au/inbound/index.html">Melbourne Global Mobility</a> site.</p></div><hr /><div class="col-1 first step-arrow"><h3><a name="accept" id="accept"></a>Step 3</h3></div><div class="col-5"><h2><a name="accept" id="accept"></a>After you apply - accepting your offer</h2><h3>Acknowledgement</h3><p>When you submit your e-application you will be automatically sent an acknowledgement email.&nbsp;&nbsp;The acknowledgement letter will include your unique student ID and application reference number. Please quote these numbers in all correspondence with the University.</p><p>We will begin by checking that your application contains everything we need to begin assessment.&nbsp;&nbsp;If anything is missing we will email you.</p><p>If your application is complete and we do not require any further information then your application will be assessed. This takes approximately two to four weeks for undergraduate courses.</p><h3>Offer process</h3><p>If your application is successful, your offer letter will be emailed directly to you (and copied to your nominated authorised representative, unless you have applied through VTAC). If the offer is conditional, then you need to meet the conditions of your offer before accepting the offer. If you have been sent an unconditional offer, you can choose to accept it immediately.</p><p>To accept your offer follow the instructions in your offer letter.</p><p>If you choose not to accept the offer right away, you can also:</p><ul><li>Consider <a href="http://students.unimelb.edu.au/get-started">deferring your offer</a></li><li>Ask to be considered for a different course than the one you originally applied for: <ul><li><strong>If you applied through VTAC,</strong> you may be able to <a href="http://www.cop.unimelb.edu.au">change your preferences</a>.</li><li>If you applied directly using our e-application, you can login to your user account and change your preference order and/or submit a new application.</li><li><strong>If you applied directly not using our e-application,</strong> you will need to submit your change of preference via email to International Admissions.</li></ul></li><li><a href="https://futurestudents.unimelb.edu.au/admissions/applications/non-acceptance" target="_blank">Decline your offer</a></li></ul><p>Unsuccessful applicants will receive a letter by mail (or fax to your nominated authorised representative) explaining why the application has been unsuccessful.</p><h3>Are you under 18?</h3><p>If you are an international student who will be under 18 years of age when entering Australia, you will need to confirm you have appropriate accommodation, support and general welfare arrangements in place before you can accept your offer. You will need to meet one of the three requirements below:</p><ul><li>Living with a parent</li><li>Living with a relative</li><li>Other approved care arrangement.</li></ul><p>You can also enrol in the <a href="http://services.unimelb.edu.au/international/under18/supervision-program" target="_blank">University of Melbourne Under 18 Supervision Program</a>. Find out more about <a href="http://services.unimelb.edu.au/international/under18" target="_blank">students under 18</a>.</p></div><hr /><div class="col-1 first step-arrow"><h3>Step 4</h3></div><div class="col-5"><h2><a name="prepare" id="prepare"></a>Preparing for study</h2><div class="col-2" style="float:right; margin-top:10px;"><a href="https://my.unimelb.edu.au" target="_blank"><img src="https://futurestudents.unimelb.edu.au/__data/assets/image/0004/1094539/Student-contact-details-notice.jpg" /></a></div><p>Once you've received and accepted your offer, it's time to get ready to move to Melbourne! You'll need to find a place to live, decide whether you need to work while you study and learn about life in your new city. Below are some helpful resources, including enrolment information, to make the transition easier for you.</p><h3>Visas</h3><p>If you haven't already got your visa to study in Australia, now is the time to do that. All citizens of countries other than New Zealand or Australia need a visa to study here. You should have received information about applying for a student visa with your offer of a place from the University.</p><ul><li><a href="http://services.unimelb.edu.au/international/visas/apply" target="_blank">Applying for a student visa</a></li><li><a href="//services.unimelb.edu.au/international/visas/conditions-and-validity" target="_blank">Student visa conditions</a></li><li><a href="http://services.unimelb.edu.au/international/visas/oshc" target="_blank">Overseas Student Health Cover (OSHC)</a></li></ul><h3>Organising your arrival</h3> Each semester, International Student Services organises pre-departure briefings in a number of countries. All commencing international students and their families are invited to attend the briefings prior to your arrival in Melbourne. This will help you understand more about what life in Melbourne will be like. <ul><li><a href="http://services.unimelb.edu.au/international/planning" target="_blank">Pre-departure briefings</a></li></ul><p>If you can't make it to a pre-departure briefing or there isn't one near you, don't worry. There is a lot of information <a href="http://services.unimelb.edu.au/international/planning" target="_blank">right here</a> that can help you find your way.</p><h3>Accommodation</h3><p>Finding a place to live can be complicated from a distance. Melbourne offers plenty of housing options. Some students choose to live in campus residences, some choose to stay with an Australian family, while most Australian students choose 'share housing', where a number of students live together close to the University.</p><ul><li>Find out more about <a href="https://futurestudents.unimelb.edu.au/explore/accommodation">Accommodation in Melbourne</a></li></ul><p>Need somewhere to stay until longer term housing is available? You can request <a href="https://services.unimelb.edu.au/housing/moving-to-melbourne/temporary-accommodation">temporary accommodation</a> before you arrive in Melbourne. There's also <a href="https://services.unimelb.edu.au/housing">longer term housing</a> available for all students including Study Abroad and Exchange students.</p><ul><li>Read more about <a href="https://services.unimelb.edu.au/housing/moving-to-melbourne">moving to Melbourne</a></li></ul><h3>Enrolment and orientation</h3><p>The first step in your new academic life is enrolling and attending orientation, designed to help ease your entry into campus life. To assist you with your move to Australian tertiary study the <a href="http://studentconnect.unimelb.edu.au" target="_blank">Student Connect website</a> has advice and information to help you understand all aspects of university life, including what happens at <a href="//orientation.unimelb.edu.au" target="_blank">enrolment and orientation</a>.</p><ul><li><a href="http://services.unimelb.edu.au/international/life-and-study" target="_blank">Getting used to a new country</a></li></ul><h3>Work while you study</h3><p>Some students choose to work while they&rsquo;re studying. Student visas allow you to work, however you must comply with the conditions on your visa. For more information, see <a href="http://services.unimelb.edu.au/international/visas/working-while-studying" target="_blank">Work while studying</a></p><h3>Fun while you study</h3> Being at university isn't all hard work. Life on campus can be great fun too! For more information on activities and events outside of classes, take a look at the following: <ul><li><a href="https://futurestudents.unimelb.edu.au/explore/student-experience">Life at Melbourne</a></li><li><a href="http://www.sport.unimelb.edu.au/Clubs" target="_blank">Sports clubs</a></li><li><a href="http://union.unimelb.edu.au/clubs" target="_blank">Clubs and societies</a></li></ul><h3>Leadership and Volunteering</h3><p>Challenge yourself, develop confidence, or enhance your leadership/team and interpersonal skills. Would you like to get involved in the community, connect with others at university and make new friends? How about gaining work experience, going on an adventure or just having fun? If your answer is yes, come and visit&nbsp;<a href="http://equity.unimelb.edu.au/initiatives">Equity and student engagement initiatives</a>.</p><h3>More services</h3><p>Check out all of our fantastic support services to help you out while you study. Our services include: Careers and Employment, Child Care Services, Counselling Service and many more. See <a href="http://services.unimelb.edu.au/" target="_blank">Services for Students</a> for more information.</p></div>
</div>
    </div>"""]))

            degree_name_urls = response.xpath("//span[@class='category']/a/@href|"
                                              "//div[@class='parent-courses']/a/@href").extract()
            print("degree_name_urls: ", degree_name_urls)
            # if len(degree_name_urls) > 0:
            for link in degree_name_urls:
                # degree_url = "https://coursesearch.unimelb.edu.au" + link
                degree_url =  "https://study.unimelb.edu.au" + link
                # print("===", degree_url)
                self.parse_data(degree_url, item)
                yield item
                # print("***")
                # yield scrapy.Request(url, callback=self.parse_data, meta={"programme_en": programme, "overview_en": overview_en, "career_en": career_en, "modules_en": modules})
        except Exception as e:
            with open("scrapySchool_Australian_ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_data(self, degree_url, item):
        print("学位类型链接============"+degree_url+"===============")
        data = requests.get(degree_url, headers=self.headers)
        response = etree.HTML(data.text)
        # try:
        degree_name = response.xpath("//div[@class='headline']/h1/text()|//h1[@id='page-header']//text()")
        item['degree_name'] = ''.join(degree_name).strip()
        print("item['degree_name']: ", item['degree_name'])

        department = ''
        if "Bachelor of " in item['degree_name']:
            department = item['degree_name'].replace("Bachelor of", "")
            department = ''.join(department).strip()
        item['department'] = department
        print("item['department']: ", item['department'])

        duration = response.xpath("//div[@class='course-length icn icn-duration']/text()|//li[contains(text(),'full time')]//text()")
        clear_space(duration)
        print("duration:", duration)
        duration_list = getIntDuration(''.join(duration))
        if len(duration_list) == 2:
            item['duration'] = duration_list[0]
            item['duration_per'] = duration_list[-1]
        print("item['duration']: ", item['duration'])
        print("item['duration_per']: ", item['duration_per'])

        location = response.xpath("//div[@class='course-location icn icn-location']//text()|//li[contains(text(),'campus')]//text()")
        item['location'] = ''.join(location).strip()
        print("item['location']: ", item['location'])

        degree_description = response.xpath("//div[@class='primary']//div[@class='description']|"
                                            "//section[@id='course-overview']//div[@class='course-section__main course-section__main-with-aside']")
        degree_description_str = ""
        if len(degree_description) > 0:
            for deg_desc in degree_description:
                degree_description_str += etree.tostring(deg_desc, encoding='unicode', method='html')
        item['degree_overview_en'] = remove_class(clear_lianxu_space([degree_description_str]))
        print("item['degree_overview_en']: ", item['degree_overview_en'])

        rntry_tuition_fee_url = data.url + ".inline?profile_citizenship=international&profile_qualification=76&profile_year=2019"
        # print("rntry_tuition_fee_url: ", rntry_tuition_fee_url)
        rntry_tuition_fee_list = self.parse_rntry_tuition_fee(rntry_tuition_fee_url)
        item['rntry_requirements_en'] = rntry_tuition_fee_list[0]
        print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

        item['tuition_fee'] = getTuition_fee(rntry_tuition_fee_list[1])
        if item['tuition_fee'] == 0:
            item['tuition_fee'] = None
        else:
            item['tuition_fee_pre'] = "AUD$"
        print("item['tuition_fee']: ", item['tuition_fee'])


    def parse_rntry_tuition_fee(self, rntry_tuition_fee_url):
        data = requests.get(rntry_tuition_fee_url, headers=self.headers)
        response = etree.HTML(data.text)
        rntry_requirements_en_str = ""

        rntry_requirements_en = response.xpath("//div[@class='entry-requirements']|//div[@class='prerequisites']")
        if len(rntry_requirements_en) > 0:
            for deg_desc in rntry_requirements_en:
                rntry_requirements_en_str += remove_class(clear_lianxu_space([etree.tostring(deg_desc, encoding='unicode', method='html')]))

        tuition_fee = response.xpath("//*[contains(text(),'Typical course fee for 2019:')]//text()")
        clear_space(tuition_fee)
        tuition_fee_str = ''.join(tuition_fee).strip()
        return [rntry_requirements_en_str, tuition_fee_str]


    def parse_modules(self, modulesUrl):
        print("课程结构链接============"+modulesUrl+"===============")
        data = requests.get(modulesUrl, headers=self.headers)
        response = etree.HTML(data.text)

        modules_en = response.xpath("//div[@class='with-jumpnav']/*")
        modules_en_str = ""
        if len(modules_en) > 0:
            for deg_desc in modules_en:
                modules_en_str += etree.tostring(deg_desc, encoding='unicode', method='html')
        modules_en1 = remove_class(clear_lianxu_space([modules_en_str]))
        return modules_en1