# -*- coding: utf-8 -*-
import scrapy
import re
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

class UniversityOfPortsmouth_PSpider(scrapy.Spider):
    name = "UniversityOfPortsmouth_P"
    # start_urls = ["http://www.port.ac.uk/courses/"]
    start_urls = []
    for i in range(1,10):
        url = "https://www.port.ac.uk/study/courses?level=pg-taught&mode=Full-time&results=10&sort=AZ&page="+str(i)
        start_urls.append(url)
#     start_urls = ["https://www.port.ac.uk/study/courses/msc-human-resource-management-top-up",
# "https://www.port.ac.uk/study/courses/msc-information-systems",
# "https://www.port.ac.uk/study/courses/msc-criminal-psychology",
# "https://www.port.ac.uk/study/courses/msc-security-management",
# "https://www.port.ac.uk/study/courses/msc-cybercrime-campus-learning-only",
# "https://www.port.ac.uk/study/courses/msc-forensic-information-technology",
# "https://www.port.ac.uk/study/courses/msc-logistics-and-supply-chain-management",
# "https://www.port.ac.uk/study/courses/llm-law",
# "https://www.port.ac.uk/study/courses/mba-global",
# "https://www.port.ac.uk/study/courses/msc-crime-science",
# "https://www.port.ac.uk/study/courses/llm-corporate-governance-and-law-grad-icsa",
# "https://www.port.ac.uk/study/courses/msc-real-estate-management",
# "https://www.port.ac.uk/study/courses/msc-quantity-surveying",
# "https://www.port.ac.uk/study/courses/msc-project-management", ]

    def parse(self, response):
        links = response.xpath("//div[@class='Content']/div/div[@class='o-Grid o-Grid--full']/div/div[@class='Panel-body']/h2/a/@href").extract()
        start_date = response.xpath(
            "//div[@class='Content']/div[@class='Panel Panel--imageright']//strong[contains(text(), 'Start Date')]/../text()").extract()
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
        # 专业描述未能完全匹配上
        # print(len(links))
        # links = response.xpath(
        #     "//a[contains(@href, 'http://www2.port.ac.uk')][contains(text(), 'here')]/@href").extract()

#         links = ["https://www.port.ac.uk/study/courses/mpa-public-administration",
# "https://www.port.ac.uk/study/courses/msc-civil-engineering-with-environmental-engineering",
# "https://www.port.ac.uk/study/courses/ma-graphic-design",
# "https://www.port.ac.uk/study/courses/ma-illustration",
# "https://www.port.ac.uk/study/courses/msc-educational-leadership-and-management",
# "https://www.port.ac.uk/study/courses/msc-digital-media",
# "https://www.port.ac.uk/study/courses/msc-international-human-resource-management",
# "https://www.port.ac.uk/study/courses/msc-crisis-and-disaster-management", ]

        '''2018.11.19'''
        # links = ["https://www.port.ac.uk/study/courses/msc-forensic-information-technology",
        #               "https://www.port.ac.uk/study/courses/msc-logistics-and-supply-chain-management",
        #               "https://www.port.ac.uk/study/courses/llm-law",
        #               "https://www.port.ac.uk/study/courses/mba-global",
        #               "https://www.port.ac.uk/study/courses/msc-crime-science",
        #               "https://www.port.ac.uk/study/courses/llm-corporate-governance-and-law-grad-icsa",
        #               "https://www.port.ac.uk/study/courses/msc-real-estate-management",
        #               "https://www.port.ac.uk/study/courses/msc-quantity-surveying",
        #               "https://www.port.ac.uk/study/courses/msc-project-management",
        #               "https://www.port.ac.uk/study/courses/msc-information-systems",
        #               "https://www.port.ac.uk/study/courses/msc-criminal-psychology",
        #               "https://www.port.ac.uk/study/courses/msc-security-management",
        #               "https://www.port.ac.uk/study/courses/msc-cybercrime-campus-learning-only", ]
        for link in links:
            url = "http://www.port.ac.uk" + link
            # url = link
            yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.port.ac.uk/"
        item['university'] = "University of Portsmouth"
        item['url'] = response.url
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        item['location'] = 'University House, Winston Churchill Avenue, Portsmouth PO1 2UP'
        print("===========================")
        print(response.url)
        try:
            # //div[@class='video']/div[@class='video_title']/div/div[@class='course_title']/h1
            programme = response.xpath("//div[@class='video']/div[@class='video_title']/div/div[@class='course_title']/h1//text()|"
                                       "//h1[@class='Title']/text()").extract()
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en']: ", item['programme_en'])

            # //div[@class='video']/div[@class='video_title']/div/div[@class='course_title']/h1
            degree_type = response.xpath(
                "//div[@class='course_title']/span//text()|"
                "//h1[@class='Title']/small//text()").extract()
            item['degree_name'] = ''.join(degree_type).strip()
            print("item['degree_name']: ", item['degree_name'])

            # //div[@class='video']/div[@class='video_title']/div/div[@class='course_title']/h1
            department = response.xpath(
                "//div[@class='video']/div[@class='video_title']/div/div[@class='course_title']/h1//text()|"
                "//dt[contains(text(), 'Department')]/following-sibling::dd[1]//text()").extract()
            item['department'] = ''.join(department)
            # print("item['department']: ", item['department'])

            item['start_date'] = response.meta.get(response.url)
            print("item['start_date']1 = ", item['start_date'])
            if item['start_date'] is not None:
                if "," in item['start_date']:
                    start_date_re = item['start_date'].split(',')
                    start_date_str = ""
                    for s in start_date_re:
                        start_date_str += getStartDate(s) + ","
                    item['start_date'] = start_date_str.strip().strip(',').strip()
            print("item['start_date'] = ", item['start_date'])

            # //div[@class='video']/div[@class='video_title']/div/div[@class='course_title']/h1
            duration = response.xpath("//div[contains(text(),'Duration')]/following-sibling::*//text()|"
                                      "//dt[contains(text(), 'Duration')]/following-sibling::dd[1]//text()|"
                                      "//dt[contains(text(), 'duration')]/following-sibling::dd[1]//text()").extract()
            clear_space(duration)
            print("duration: ", duration)
            duration_str = ''.join(duration)
            item['other'] = duration_str
            item['teach_time'] = getTeachTime(duration_str)

            duration_list = getIntDuration(duration_str)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            print("item['teach_time'] = ", item['teach_time'])
            print("item['duration'] = ", item['duration'])
            print("item['duration_per'] = ", item['duration_per'])

            location = response.xpath("//div[contains(text(),'Location')]/following-sibling::*//text()").extract()
            item['location'] = ''.join(location)
            # print("item['location']: ", item['location'])

            # //strong[contains(text(),'International students')]/../following-sibling::p[1]
            tuition_fee = response.xpath(
                " //strong[contains(text(),'International students')]/../following-sibling::p//text()").extract()
            clear_space(tuition_fee)
            # print("tuition_fee: ", tuition_fee)
            tuition_fee_re = re.findall(r"Full\stime:\s£\d+,\d+|Full\stime\s£\d+,\d+", ''.join(tuition_fee))
            # print("tuition_fee_re: ", tuition_fee_re)
            if len(tuition_fee_re) > 0:
                item['tuition_fee'] = int(tuition_fee_re[0].replace("Full time", "").replace(":", "").replace(",", "").replace("£", "").strip())
            # print("item['tuition_fee']: ", item['tuition_fee'])

            if item['tuition_fee'] == None:
                # //strong[contains(text(),'International students')]/../following-sibling::p[1]
                tuition_fee = response.xpath(
                    "//h3[contains(text(),'Tuition fees')]/..//*[contains(text(),'International students')]/following-sibling::*//*[contains(text(),'Full')]//text()|"
                    "//h3[contains(text(),'Tuition fees')]/..//*[contains(text(),'International students')]/../following-sibling::*//*[contains(text(),'Full')]//text()|"
                    "//h3[contains(text(),'Tuition fees')]/..//h4[contains(text(),'Full-time')]/following-sibling::*[position()<3]//*[contains(text(),'International students')]/../text()").extract()
                clear_space(tuition_fee)
                # print("tuition_fee: ", tuition_fee)
                tuition_fee_re = re.findall(r"£\d+,\d+", ''.join(tuition_fee))
                # print("tuition_fee_re: ", tuition_fee_re)
                if len(tuition_fee_re) > 0:
                    item['tuition_fee'] = int(tuition_fee_re[0].replace(",", "").replace("£", "").strip())
                # print("item['tuition_fee']: ", item['tuition_fee'])

            rntry_requirements_content = response.xpath("//h3[contains(text(),'Key Facts')]/..//text()").extract()
            clear_space(rntry_requirements_content)
            # print("rntry_requirements_content: ", rntry_requirements_content)
            if "2018 ENTRY REQUIREMENTS" in rntry_requirements_content:
                rntry_requirements_index = rntry_requirements_content.index("2018 ENTRY REQUIREMENTS")
                if "Fees" in rntry_requirements_content:
                    rntry_requirements_indexEnd = rntry_requirements_content.index("Fees")
                    item['rntry_requirements'] = clear_lianxu_space(rntry_requirements_content[rntry_requirements_index:rntry_requirements_indexEnd])
            if "2018 entry requirements" in rntry_requirements_content:
                rntry_requirements_index = rntry_requirements_content.index("2018 entry requirements")
                if "Fees" in rntry_requirements_content:
                    rntry_requirements_indexEnd = rntry_requirements_content.index("Fees")
                    item['rntry_requirements'] = clear_lianxu_space(
                        rntry_requirements_content[rntry_requirements_index:rntry_requirements_indexEnd])
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            if item['rntry_requirements'] == "":
                rntry_requirements_content = response.xpath(
                    "//div[contains(text(),'Entry Requirements')]/../../..//div[contains(text(),'2018 start')]/../../../..//text()|"
                    "//div[contains(text(),'Entry requirements')]/../../..//div[contains(text(),'2018 start')]/../../../..//text()").extract()
                item['rntry_requirements'] = clear_lianxu_space(rntry_requirements_content)
            print("item['rntry_requirements']: ", item['rntry_requirements'])

            ieltsList = re.findall(r".{1,45}IELTS.{1,45}", item['rntry_requirements'])
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

            overview = response.xpath("""//h2[@id='overview']/..|//h3[contains(text(),'What you’ll experience')]/..|//*[contains(text(),"What you'll experience")]/..|
                                    //h4[contains(text(),"On this course, you'll:")]/../..|//h3[contains(text(),"What you'll experience")]/../preceding-sibling::*[2]|
                                    //h3[contains(text(),'Why take this course?')]/../*[not(@class='blockquote-img')]""").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview)).replace("<div><div>Get a prospectus</div><div>Book an Open Evening</div><div>Apply Now</div></div>", "").strip()
            print("item['overview_en']: ", item['overview_en'])

            modules = response.xpath("//h2[@id='What youll study']/..|//h2[@id='What youll study']/../following-sibling::div[1]|//div[contains(text(),'Units currently being studied')]/../../..|"
                                     "//h3[@id='structure']/../../following-sibling::div[1]").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])

            teaching_assessment = response.xpath("//h2[@id='Teaching']/..|//h2[@id='Teaching']/../following-sibling::*[1]|"
                                                 "//h2[@id='How youre assessed']/..|//h2[@id='How youre assessed']/../following-sibling::*[1]|"
                                                 "//div[@class='pure-g purple content']/div[1]/div[@class='box']").extract()
            if len(teaching_assessment) == 0:
                teaching_assessment = response.xpath(
                    "//h3[contains(text(), 'Teaching')]/preceding-sibling::*[1]/following-sibling::*[position()<3]").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(teaching_assessment))
            # print("item['assessment_en']: ", item['assessment_en'])

            career = response.xpath("//h3[contains(text(),'Careers and opportunities')]/..|"
                                    "//div[@class='box container content pure-g']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<h3>Postgraduate courses</h3>
<p>For entry to our postgraduate Master's programmes, you'll usually need to have one of the following from a recognised Higher Education institution:</p>
<ul>
    <li>a Bachelor's degree (normally from a four year undergraduate programme)</li>
    <li>a Bachelor's degree from Higher Education Self-Study Examinations (full time)</li>
    <li>a top-up degree or university-recognised Pre-Master&rsquo;s Foundation programme</li>
</ul>
<p>Typical minimum Grade Point Average (GPA) requirements:</p>
<ul>
    <li>From 2.8 on a scale of 1-4</li>
    <li>From 7 on a scale of 1-10</li>
</ul>
<p>If you don't meet the postgraduate entry requirements, you can do a pre-Master's programme at<a rel="noopener noreferrer" href="http://www.icp.navitas.com/"></a><a rel="noopener noreferrer" href="https://www.icp.navitas.com/" target="_blank">International College Portsmouth (ICP)</a>&nbsp;for many of our courses.</p>"""]))
            item['apply_proces_en'] = "https://www.port.ac.uk/study/international-students/how-to-apply"
            yield item
        except Exception as e:
            with open("scrapySchool_England/error/" + item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

