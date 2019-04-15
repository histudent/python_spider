# -*- coding: utf-8 -*-
import scrapy
import re
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

class UniversityOfPortsmouth_USpider(scrapy.Spider):
    name = "UniversityOfPortsmouth_U"
    # start_urls = ["http://www.port.ac.uk/courses/"]
    start_urls = ["https://www.port.ac.uk/study/courses?level=ug&mode=Full-time&page=1&results=10&sort=AZ"]

    for i in range(20):
        url = "https://www.port.ac.uk/study/courses?level=ug&mode=Full-time&page="+str(i)+"&results=10&sort=AZ"
        start_urls.append(url)
    # rules = (
    #     Rule(LinkExtractor(allow="page=\d+"), follow=True, callback='page_url'),
    # )
    #
    # def page_url(self, response):
    #     print(response.url)

    def parse(self, response):
        links = response.xpath("//div[@class='Content']/div[@class='Panel Panel--imageright']//a[contains(@href, '/study/course')]/@href").extract()

        start_date = response.xpath("//div[@class='Content']/div[@class='Panel Panel--imageright']//strong[contains(text(), 'Start Date')]/../text()").extract()
        clear_space(start_date)
        # 组合字典
        programme_dict = {}
        # programme_list = response.xpath("//div[@class='Content']/div[@class='Panel Panel--imageright']//a[contains(@href, '/study/course')]/text()").extract()
        # clear_space(programme_list)


        for link in range(len(links)):
            url = "https://www.port.ac.uk" + links[link]
            programme_dict[url] = start_date[link]

        # print(len(links))
        links = list(set(links))
        # print(len(links))
        # links = ["https://www.port.ac.uk/study/courses/ba-hons-hospitality-management",
        #          "http://www.port.ac.uk/courses/modern-languages-and-area-studies/ba-hons-applied-languages/",
        #          "http://www.port.ac.uk/courses/modern-languages-and-area-studies/mlang-applied-languages/",
        #          "http://www.port.ac.uk/courses/business-and-management/ba-hons-hospitality-management-with-tourism/",
        #          "http://www.port.ac.uk/courses/modern-languages-and-area-studies/ba-hons-international-development-studies-and-languages/",
        #          "https://www.port.ac.uk/study/courses/ba-hons-international-relations-and-languages",
        #          "https://www.port.ac.uk/study/courses/ba-hons-modern-languages", ]
        links = ["https://www.port.ac.uk/study/courses/ba-hons-animation",
"https://www.port.ac.uk/study/courses/ba-hons-american-studies-with-english",
"https://www.port.ac.uk/study/courses/bsc-hons-business-information-systems", ]
        for link in links:
            # url = "http://www.port.ac.uk" + link
            url = link
            yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "https://www.port.ac.uk/"
        item['university'] = "University of Portsmouth"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        item['location'] = 'University House, Winston Churchill Avenue, Portsmouth PO1 2UP'
        print("===========================")
        print(response.url)
        try:
            # //div[@class='video']/div[@class='video_title']/div/div[@class='course_title']/h1
            programme = response.xpath("//h1[@class='Title']/text()").extract()
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en']: ", item['programme_en'])

            # //div[@class='video']/div[@class='video_title']/div/div[@class='course_title']/h1
            degree_type = response.xpath(
                "//h1[@class='Title']/small//text()").extract()
            item['degree_name'] = ''.join(degree_type).replace("(Hons)", "").strip()
            print("item['degree_name']: ", item['degree_name'])

            ucascode = response.xpath("//nobr[contains(text(),'UCAS Code')]/../following-sibling::*//text()").extract()
            clear_space(ucascode)
            item['ucascode'] = ''.join(ucascode).replace("UCAS Code:", "").strip()
            # print("item['ucascode'] = ", item['ucascode'])

            item['start_date'] = response.meta.get(response.url)
            # print("item['start_date'] = ", item['start_date'])

            # //div[@class='video']/div[@class='video_title']/div/div[@class='course_title']/h1
            # department = response.xpath(
            #     "//dt[contains(text(), 'Department')]/following-sibling::dd[1]//text()").extract()
            # item['department'] = ''.join(department)
            # print("item['department']: ", item['department'])

            # //div[@class='video']/div[@class='video_title']/div/div[@class='course_title']/h1
            duration = response.xpath("//div[contains(text(),'Duration')]/following-sibling::*//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration_str = ''.join(duration)
            item['other'] = duration_str

            duration_list = getIntDuration(duration_str)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            location = response.xpath("//div[contains(text(),'Location')]/following-sibling::*//text()").extract()
            item['location'] = ''.join(location)
            # print("item['location']: ", item['location'])


            # //strong[contains(text(),'International students')]/../following-sibling::p[1]
            tuition_fee = response.xpath(
                "//h3[contains(text(),'Tuition fees')]/..//*[contains(text(),'International students')]//text()").extract()
            clear_space(tuition_fee)
            # print("tuition_fee: ", tuition_fee)
            tuition_fee_re = re.findall(r"£\d+,\d+", ''.join(tuition_fee))
            # print("tuition_fee_re: ", tuition_fee_re)
            if len(tuition_fee_re) > 0:
                item['tuition_fee'] = int(tuition_fee_re[0].replace(",", "").replace("£", "").strip())
            # print("item['tuition_fee']: ", item['tuition_fee'])

            overview = response.xpath("""//h2[@id='overview']/..|//h3[contains(text(),"What you'll experience")]/..|
            //h3[contains(text(),'What you’ll experience')]/..|//*[contains(text(),"What you'll experience")]/../..""").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview)).replace("<h3>What you'll experience</h3>","").strip()
            print("item['overview_en']: ", item['overview_en'])

            career = response.xpath("//h3[contains(text(),'Careers and opportunities')]/..").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            rntry_requirements_content = response.xpath("//div[contains(text(),'Entry Requirements')]/../../..//div[contains(text(),'2019 start')]/../../../..//text()").extract()
            rntry_requirements_str = clear_lianxu_space(rntry_requirements_content)

            ieltsList = response.xpath("//*[contains(text(),'English language proficiency')]/text()|"
                                       "//*[contains(text(),'English Language proficiency')]/text()").extract()
            # print(ieltsList)
            if len(ieltsList) == 0:
                ieltsList = re.findall(r".{1,45}IELTS.{1,85}", rntry_requirements_str)
            clear_space(ieltsList)
            if len(ieltsList) > 0:
                item['ielts_desc'] = ''.join(ieltsList[1:]).strip()
                if item['ielts_desc'] == "":
                    item['ielts_desc'] = ''.join(ieltsList).strip()
            # print("item['ielts_desc']: ", item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            alevel = response.xpath("//*[contains(text(),'A levels')]/text()").extract()
            # print(ieltsList)
            if len(alevel) == 0:
                alevel = re.findall(r".{1,45}A\slevels.{1,85}", rntry_requirements_str)
            clear_space(alevel)
            if len(alevel) > 0:
                item['alevel'] = ''.join(alevel[1:]).strip()
                if item['alevel'] == "":
                    item['alevel'] = ''.join(alevel).strip()
            print("item['alevel']: ", item['alevel'])

            modules = response.xpath("//h2[@id='What youll study']/..|//h2[@id='What youll study']/../following-sibling::div[1]|//div[contains(text(),'Units currently being studied')]/../../..").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])

            teaching_assessment = response.xpath("//h2[@id='Teaching']/..|//h2[@id='Teaching']/../following-sibling::*[1]|//h2[@id='How youre assessed']/..|//h2[@id='How youre assessed']/../following-sibling::*[1]").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(teaching_assessment))
            # print("item['assessment_en']: ", item['assessment_en'])

            apply_proces_en = response.xpath(
                "//h2[@id='Apply']/..|//h2[@id='Apply']/../following-sibling::*").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(apply_proces_en))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            item['apply_documents_en'] = remove_class(clear_lianxu_space(["""<h2 style="color: #384047; margin: 33px 0px 0.7em; padding: 0px;">What you'll need to send us</h2>
<p style="color: #384047; margin: 0px 0px 25px; border: none;">When you apply to join us, we'll need to see the following documents:</p>
<ul style="color: #384047; margin: 0px 0px 25px; padding-left: 35px; border: none; list-style-image: initial;">
    <li style="margin-top: 0px;">A completed application form</li>
    <li>A Personal Statement or Statement of Purpose</li>
    <li>Officially certified and translated copies of your high school or college qualification and grades (for undergraduate courses)</li>
    <li>Officially certified and translated copies of your degree qualification and grades (for Postgraduate courses)</li>
    <li>Proof of your English language level (such as an IELTS Certificate)</li>
    <li style="margin-bottom: 0px;">One academic reference on official headed paper for undergraduate courses or two references for postgraduate courses</li>
</ul>"""]))
            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<h3>Undergraduate courses</h3>
<p>If you've completed the Chinese Senior High School Diploma plus one year at a recognised university in China, we'll consider you for admission onto an undergraduate course such as a Bachelor's degree. You must have studied relevant subjects and achieved strong grades.</p>
<p>If you don't have a Chinese Senior High School Diploma, you can apply with:</p>
<h4>A levels</h4>
<ul>
    <li>Most courses will require 120 UCAS points. Your A level grades should equal or exceed the total points required. You can use the&nbsp;<a rel="noopener noreferrer" rel="noopener noreferrer" href="https://www.ucas.com/ucas/tariff-calculator"></a><a rel="noopener noreferrer" href="https://www.ucas.com/ucas/tariff-calculator" target="_blank">UCAS Tariff Calculator</a>&nbsp;to work out your total points. Please check your specific course page to find the exact number of points.</li>
    <li>Some courses will require you to have studied specific subjects at A level. For example, to study a science course you will usually need to have achieved passing grades in scientific subjects at A level.</li>
    <li>A level points: A* = 56 A = 48 B = 40 C = 32 D = 24.</li>
</ul>
<h4>International Baccalaureate</h4>
<ul>
    <li>Most courses will require between 24 and 31 points in the International Baccalaureate (IB), depending on the degree you apply for.</li>
</ul>
<p>You may also be considered for advanced entry onto a relevant undergraduate degree programme if you have a College Graduation Diploma (Dazhuan) from a recognised university or college on completion of two to three years of study, or a BTEC HND or SQA HND Higher National Diploma in a relevant subject.</p>
<p>You may be able to join an undergraduate course with other qualifications. We do consider qualifications from a range of sources. Contact us to find out more.</p>"""]))
            item["ib"] = "Most courses will require between 24 and 31 points in the International Baccalaureate (IB), depending on the degree you apply for."
            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a',
                      encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

