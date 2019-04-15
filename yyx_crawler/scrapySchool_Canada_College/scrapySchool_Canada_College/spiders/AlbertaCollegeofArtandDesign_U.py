__author__ = 'yangyaxia'
__date__ = '2018/12/19 18:09'
import scrapy
import re
from scrapySchool_Canada_College.getItem import get_item
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from w3lib.html import remove_tags
from lxml import etree
import requests

class AlbertaCollegeofArtandDesign_USpider(scrapy.Spider):
    name = "AlbertaCollegeofArtandDesign_U"
    start_urls = ["https://acad.ca/degrees-programs/bachelors-degrees/bfa/ceramics",
"https://acad.ca/degrees-programs/bachelors-degrees/bfa/critical-creative-studies",
"https://acad.ca/degrees-programs/bachelors-degrees/bfa/drawing",
"https://acad.ca/degrees-programs/bachelors-degrees/bfa/fibre",
"https://acad.ca/degrees-programs/bachelors-degrees/bfa/glass",
"https://acad.ca/degrees-programs/bachelors-degrees/bfa/jewellery-metals",
"https://acad.ca/degrees-programs/bachelors-degrees/bfa/media-arts",
"https://acad.ca/degrees-programs/bachelors-degrees/bfa/painting",
"https://acad.ca/degrees-programs/bachelors-degrees/bfa/print-media",
"https://acad.ca/degrees-programs/bachelors-degrees/bfa/sculpture",
"https://acad.ca/degrees-programs/bachelors-degrees/bdes/visual-communications-design",
"https://acad.ca/degrees-programs/bachelors-degrees/bdes/photography", ]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaCollegeItem)
        item['school_name'] = "Alberta College of Art and Design"
        item['url'] = response.url
        print("===========================")
        print(response.url)

        # item['campus'] = ''
        item['location'] = '1407 - 14 Ave. NW Calgary, Alberta, Canada T2N 4R3'

        item['other'] = """问题描述： 1.没有就业信息和课程长度"""



        # https://www.acad.ca/future-students/how-apply/how-apply-bachelors-degree/how-apply-if-youre-international-student
        item['apply_pre'] = "CAD$"
        item['apply_fee'] = '110'
        item['start_date'] = '2019-09'
        item['deadline'] = "2019-02-01"

        # https://www.acad.ca/future-students/how-apply/how-apply-bachelors-degree/academic-requirements/english-requirements
        item['ielts_desc'] = 'A score of 6.5 or higher on the International English Language Test (IELTS)'
        item['ielts'] = '6.5'
        item['toefl_desc'] = 'A score of 83 or higher on an official Test of English as a Foreign Language (TOEFL) on the Internet-based test (iBT)'
        item['toefl'] = '83'

        item['portfolio_desc_en'] = """ <div>
            <h1>Portfolio requirements and statement of intent</h1>
  <span></span><span></span>
  <p>
    Your portfolio has two major components, a statement of intent and samples of your work. Both are an important part of your application to ACAD, and a key way for the review committee to get to know more about you.  </p>
  <h3>
	1. Statement of intent</h3>
<p>
	This is where you tell us all about you – your background, inspiration, and goals. Your statement of intent should be approximately 500 words in length and explain the following:</p>
<ul>
	<li>
		Why do you want to study at ACAD?</li>
	<li>
		Why do you want to study visual art and design?</li>
	<li>
		What mediums or artists inspire you?</li>
	<li>
		How will you benefit from studies in art and design?</li>
</ul>
<h3>
	2. Samples of your work</h3>
<p>
	Here’s where you get to really show us your stuff! Choose examples that best represent your abilities, your personality, and be sure to follow these guidelines:</p>
<ol>
	<li>
		Select 12 to 15 samples of your artwork.</li>
	<li>
		Include representational drawing examples, including one or two observational drawings of figure, landscape or still life.</li>
	<li>
		Include artwork created in a variety of mediums that explore&nbsp; different tools, techniques, and ideas.</li>
	<li>
		Demonstrate how you express ideas and concepts, preferably in work you’ve done on your own initiative outside of the classroom (for example, how do you respond creatively to current events, issues, or themes of personal interest?).</li>
</ol>
<p>
	Once you’ve written your personal statement and selected the work you want to include in your portfolio, follow our instructions on&nbsp;<a>how to photograph your portfolio</a><strong> </strong>and <a>how to submit your portfolio</a><a>.</a></p>
        </div>          """

        # https://www.acad.ca/current-students/pay-tuition-and-fees/undergraduate-tuition-and-fees
        item['tuition_fee'] = '14,934.9'
        item['tuition_fee_per'] = 1
        item['tuition_fee_pre'] = 'CAD$'

        # https://acad.ca/future-students/how-apply-bachelors-degree/academic-requirements
        item['entry_requirements_en'] = """<p>Applicants must possess a high school diploma, have achieved a grade of at least 60% in four grade 12 subjects, including a grade of 60% or higher your school’s highest-level English class (or equivalent), and meet English language proficiency requirements. There are also specific portfolio requirements for all applicants.</p>"""
        # https://www.acad.ca/future-students/how-apply/how-apply-bachelors-degree/how-apply-if-youre-international-student
        item['require_chinese_en'] = """<p>To attend a Bachelors degree program at ACAD, you must have the equivalent of an Alberta high school diploma, with a minimum average grade of 60% (or equivalent) in your final year of studies.</p>
<p>If you attended high school in a language other than English you’ll also need to meet our English language proficiency requirements for undergraduate students.</p>"""
        try:
            major_name_en = response.xpath("//div[@class='large-8 content-con columns']/h1//text()").extract()
            clear_space(major_name_en)
            item['major_name_en'] = ''.join(major_name_en).strip()
            print("item['major_name_en']: ", item['major_name_en'])


            degree_name = response.xpath("//a[@class='active-trail'][contains(text(),'Bachelors degrees')]/../ul//a[@class='active-trail']//text()").extract()
            clear_space(degree_name)
            print("degree_name: ", degree_name)
            item['degree_name'] = ''.join(degree_name).strip()
            if item['degree_name'] == "BFA":
                item['degree_name'] = "Bachelor of Fine Arts"
            elif item['degree_name'] == "BDes":
                item['degree_name'] = "Bachelor of Design"
            print("item['degree_name']: ", item['degree_name'])

            if item['degree_name'] == "Diploma":
                item['degree_level'] = 3
            if "Bachelor" in item['degree_name']:
                item['degree_level'] = 1
            if "Post" in item['degree_name']:
                item['degree_level'] = 2
            print("item['degree_level']: ", item['degree_level'])

            if item['degree_level'] is not None:
                overview_en = response.xpath("//h2[contains(text(),'Faculty')]/preceding-sibling::*[position()<last()-3]").extract()
                if len(overview_en) > 0:
                    item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
                print("item['overview_en']: ", item['overview_en'])

                # career_en = response.xpath("//h3[@class='prepend-top']/../*[position()<last()]").extract()
                # if len(career_en) > 0:
                #     item['career_en'] = remove_class(clear_lianxu_space(career_en))
                # print("item['career_en']: ", item['career_en'])


                # modules_url = response.xpath("//li/a[@id='sidenav-child'][contains(text(), 'Courses')]/@href").extract()
                # # print("modules_url: ", modules_url)
                # if len(modules_url) > 0:
                #     item['modules_en'] = self.parse_modules(modules_url[0])
                # print("item['modules_en']: ", item['modules_en'])

                yield item
        except Exception as e:
                with open("scrapySchool_Canada_College/error/" + item['school_name'] + ".txt", 'a', encoding="utf-8") as f:
                    f.write(str(e) + "\n" + response.url + "\n========================\n")
                print("异常：", str(e))
                print("报错url：", response.url)

    def parse_modules(self, modules_url):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(modules_url, headers=headers_base)
        response = etree.HTML(data.text)

        modules_en = response.xpath(
            "//section[@id='content']")
        modules_en_str = ""
        if len(modules_en) > 0:
            for m in modules_en:
                modules_en_str += etree.tostring(m, encoding='unicode', method='html')
        modules_en = remove_class(clear_lianxu_space([modules_en_str]))

        return modules_en

    def parse_entry_requirements_en(self, entry_requirements_en_url):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(entry_requirements_en_url, headers=headers_base)
        response = etree.HTML(data.text)

        entry_requirements_en = response.xpath(
            "//h3[contains(text(),'Entrance Requirements')]/..")
        entry_requirements_en_str = ""
        if len(entry_requirements_en) > 0:
            for m in entry_requirements_en:
                entry_requirements_en_str += etree.tostring(m, encoding='unicode', method='html')
        entry_requirements_en = remove_class(clear_lianxu_space([entry_requirements_en_str]))

        major_list = response.xpath("//li[@class='navigation-active navigation-children']/ul/li//text()")
        print("major_list: ", major_list)

        datadict = {}
        datadict['entry_requirements_en'] = entry_requirements_en
        datadict['major_list'] = major_list
        return datadict