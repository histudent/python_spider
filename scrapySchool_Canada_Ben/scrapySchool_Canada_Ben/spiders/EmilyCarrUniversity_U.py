# -*- coding:utf-8 -*-
"""
# @PROJECT: scrapySchool_Canada_Ben
# @Author: admin
# @Date:   2018-12-17 14:54:55
# @Last Modified by:   admin
# @Last Modified time: 2018-12-14 15:24:55
"""

__author__ = 'yangyaxia'
__date__ = '2018/12/17 14:54'
import scrapy
import re
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from w3lib.html import remove_tags
from lxml import etree
import requests

class EmilyCarrUniversity_USpider(scrapy.Spider):
    name = "EmilyCarrUniversity_U"
    start_urls = ["https://www.ecuad.ca/academics/undergraduate-degrees/bachelor-of-design",
"https://www.ecuad.ca/academics/undergraduate-degrees/bachelor-of-fine-arts",
"https://www.ecuad.ca/academics/undergraduate-degrees/bachelor-of-media-arts", ]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        degree_name = response.xpath("//section[@class='main-body-content']/h1//text()").extract()
        clear_space(degree_name)
        print("degree_name: ", degree_name)

        degree_overview_en = response.xpath("//h2[contains(text(),'Degrees')]/preceding-sibling::*[position()<last()]").extract()
        degree_overview_en_str = remove_class(clear_lianxu_space(degree_overview_en))
        print("degree_overview_en_str: ", degree_overview_en_str)

        links = response.xpath("""//h4//a[contains(text(),'Major')]/@href""").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))
        print(links)

        for url in links:
            yield scrapy.Request(url, self.parse_data, meta={"degree_name": degree_name, "degree_overview_en": degree_overview_en_str})

    def parse_data(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)
        item['school_name'] = "Emily Carr University"
        item['url'] = response.url
        print("===========================")
        print(response.url)
        item['other'] = '''问题描述：1.没有课程长度，其他没有问题'''

        '''公共字段'''
        item['location'] = '520 East 1st Ave Vancouver, BC V5T 0H2'

        # item['act_code'] = '0719'

        # https://www.ecuad.ca/admissions/application-info/undergraduate-applications/how-to-apply-application-process
        item['apply_pre'] = 'CAD$'
        item['apply_fee'] = '70'
        item['start_date'] = "2019-01,2019-09"
        item['deadline'] = '2019-01-15,2019-10-01'

        # https://www.ecuad.ca/assets/pdf-attachments/Undergraduate-Expenses-Overview-June-2018.pdf
        item['tuition_fee_pre'] = 'CAD$'
        item['tuition_fee'] = '15,966'

        # https://www.ecuad.ca/admissions/application-info/undergraduate-applications/english-language-proficiency
        item['sat_code'] = item['toefl_code'] = '0032'
        item['ielts_desc'] = 'minimum band 6.5, with no component less than 6.0'
        item['ielts'] = '6.5'
        item['ielts_l'] = '6.0'
        item['ielts_s'] = '6.0'
        item['ielts_r'] = '6.0'
        item['ielts_w'] = '6.0'
        item['toefl_desc'] = 'minimum of 84 out of 120 total points including a minimum score in each of the four skills; Speaking 20/30, Reading 20/30, Writing 18/30, and Listening 20/30.'
        item['toefl'] = '84'
        item['toefl_l'] = '20'
        item['toefl_s'] = '20'
        item['toefl_r'] = '20'
        item['toefl_w'] = '18'

#         item['act_desc'] = item['sat1_desc'] = "SAT or ACT scores will also be considered"

        # https://www.ecuad.ca/admissions/application-info/undergraduate-applications/first-year-academic-requirements
        item['require_chinese_en'] = '''<p>Completion of the highest level of secondary education available in your home country, in a program leading directly to university entrance. You require at least a C+ (67) average in the five courses that most closely match the British Columbia requirements.</p>
<p>Applicants from China (excluding Hong Kong) must verify their educational documents through China Credentials Verification (CHESICC).Send your documents to this Chinese agency for verification in English. Ask the agency to send your official academic transcript and English verification report directly to:</p>
<blockquote> Emily Carr University of Art + Design<br>520 East 1st Ave,<br>Vancouver, BC,V5T 0H2<br>Canada</blockquote>'''
        item['ap'] = """AP Applicants​
Emily Carr University recognizes the value of AP courses. First year university transfer credit will be awarded to students who achieve a grade of 4 or higher in courses that are approved as equivalent to Emily Carr University required courses.
        When ordering transcripts from the College Board website, the four digit code is 4148."""
        item['alevel'] = """Emily Carr welcomes applications from students who have completed their GCSEs (O Levels) and GCEs (A Levels), either in Great Britain or at one of many British Pattern schools around the world.
Minimum requirements:
Graduation from a university-preparatory program at a senior secondary school with standing in at least five subject areas, including English plus two more academic subjects, with at least three approved academic GCE (A Level) subjects; or with standing in at least six subjects at the Advanced Subsidiary Level.  A subject may not be counted at both the GCE (A Level) and the GCSE (O Level) levels.
Your admission average is calculated on your final year academic courses/exams and must include at least two GCSEs (O Levels) and three GCEs (A Levels), or must include at least six Advanced Subsidiary Levels."""
        item['ib'] = """International Baccalaureate (IB)
3 Higher Level and 3 Standard Level subjects. A minimum requirement of 24 points is recommended to be considered for admission.
First year university transfer credit will be awarded to students who achieve a grade of at least 5 or higher in Higher Level courses in courses that are approved as equivalent to Emily Carr University required courses."""
        item['entry_requirements_en'] = """<h1>First Year Academic Requirements</h1>
          <h2>​To be successful with your application, meet our academic requirements.</h2>
          <p><strong>Here is what you need to know to ensure that you satisfy our academic requirements.</strong></p>
<p>The minimum academic requirement for admission to Emily Carr University undergraduate programs is graduation from grade 12 secondary school, with five grade 12 subjects, including English 12 with a minimum grade of 'C', two other grade 12 academic courses and two grade 12 elective courses. The minimum overall grade point average required for admission is 2.5 or C+ or 67%.  All elective courses must be grade 12 and can be Ministry Approved, Board Approved or Locally Developed.</p>
"""

        # https://www.ecuad.ca/admissions/application-info/undergraduate-applications/portfolio-requirements
        item['portfolio_desc_en'] = """<div>
                    <a>
                        <span>First Year Foundation Applicant Portfolios</span>
                        <i></i>
                    </a>
                    <div>
                        <h3><strong></strong><strong>Foundation Portfolio Requirements</strong>
  </h3>
<p>Your portfolio is a collection of work and ideas that demonstrate the state of your creative development. We want to see what you create to imagine how you might succeed at Emily Carr University of Art + Design. A strong portfolio includes a diverse array of artwork, experimental processes, material techniques, observation skills, and creative thinking. There is no rigid or fail-safe formula for a good portfolio: we are looking for that unique combination of creativity, engagement, and inspiration that makes art, design, and media education suitable for you. 
  </p>
<h2>Part 1: Examples of your Creative Practice</h2>
<p>We are interested in seeing a wide range of examples of your creative practice. We encourage you to submit not only visual arts projects, but also sound, time-based, craft-based, design, 3D, illustration, and animation work. All media, mixed or otherwise - from a video or a song, to a comic strip or a zine - are welcome. Please submit only your best work in its final state from the last two years. 
  </p>
<p><strong>We will only evaluate 10 samples maximum</strong>. We are asking that you be critical in your selection. 
  </p>
<h2>Part 2: Process Projects </h2>
<p>We want to know how you create, how you problem-solve, how you ask questions, and where your process takes you. Please respond to all the prompts provided below by submitting <strong>1 sample of your original work&nbsp;<b>per prompt&nbsp;</b>(or one 20-second video)</strong>. Be sure to label your slide with the relevant prompt and feel free to add a title should you feel so inspired.
  &nbsp;
  </p>
<ol><li>What keeps you up at      night?
</li><li>Describe where you live      without showing any images of your home.
</li><li>You have been asked to      design a town square; what would you put in the centre of it?
</li></ol>
<p>After responding to the three prompts artistically, please tell us how you feel about that entire creative process by writing <strong>no more than 50 words</strong>.
  </p>
<h2>Part 3: Written Responses</h2>
<p>Respond to the following three questions. We want to hear your voice and learn about you through your writing. This is not a formal essay, but an opportunity for personal reflection and intellectual honesty. Please keep your answers to <strong>75 - 100 words each</strong>.&nbsp;
  </p>
<ol><li>What makes a problem      interesting to you?
</li><li>Make a list of all the      things you’d like to learn at Emily Carr.</li><li>If you could change one thing in the world, what would it be? 
</li> <span></span></ol>
                    </div>
                </div>"""

        try:
            item['degree_name'] = response.meta.get("degree_name")
            print("item['degree_name']: ", item['degree_name'])

            item['degree_overview_en'] = response.meta.get("degree_overview_en")
            # print("item['degree_overview_en']: ", item['degree_overview_en'])

            major_name_en = response.xpath("//section[@class='main-body-content']/h1//text()").extract()
            clear_space(major_name_en)
            item['major_name_en'] = ''.join(major_name_en).strip()
            if "Major" in item['major_name_en']:
                item['major_name_en'] = item['major_name_en'].replace("Major", "").strip().strip(",").strip()
            print("item['major_name_en']: ", item['major_name_en'])


            overview = response.xpath("//a[@class='tab-link is-active']/../div/*[position()<last()]").extract()
            if len(overview) > 0:
                item['overview_en'] = remove_class(clear_lianxu_space(overview)).replace("<p></p>", "").strip()
            # if item['overview_en'] is None:
            #     print("***overview_en 为空")
            # print("item['overview_en']: ", item['overview_en'])

            career_en = response.xpath("//a[contains(text(),'Pathways')]/../div").extract()
            if len(career_en) > 0:
                item['career_en'] = remove_class(clear_lianxu_space(overview)).replace("<p></p>", "").strip()
            # if item['career_en'] is None:
            #     print("***career_en 为空")
            # print("item['career_en']: ", item['career_en'])




            # if len(modules_url) == 0:
            modules_url = response.xpath(
                "//div[contains(@class,'small-12 medium-4 columns sidbar-container')]//ul[@class='side-nav']//a[contains(@href,'courses/')]/@href").extract()
            # print(modules_url)

            item['modules_en'] = None
            # print("***modules_en 为空")
            # print("item['modules_en']: ", item['modules_en'])

            yield item

        except Exception as e:
            with open("scrapySchool_Canada_Ben/error/" + item['school_name'] + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    # 学术要求
    def parse_requirement(self, requirement_url):
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        data = requests.get(requirement_url, headers=headers_base)
        response = etree.HTML(data.text)

        degree_data = {}
        entry_requirements_en_key1 = r"<h4>Admission Requirements</h4>"
        entry_requirements_en_key2 = r"<h4>Next Steps</h4>"

        entry_requirements_en = remove_class(getContentToXpath(data.text, entry_requirements_en_key1, entry_requirements_en_key2))
        degree_data["entry_requirements_en"] = entry_requirements_en

        degree_overview_en = response.xpath("//h6[contains(text(),'Majors:')]/preceding-sibling::*")
        if len(degree_overview_en) == 0:
            degree_overview_en = response.xpath("//h4[contains(text(),'Careers')]/preceding-sibling::*")
        degree_overview_en_str = ""
        if len(degree_overview_en) > 0:
            for m in degree_overview_en:
                degree_overview_en_str += etree.tostring(m, encoding='unicode', method='html')
        degree_overview_en = remove_class(degree_overview_en_str)
        degree_data['degree_overview_en'] = degree_overview_en
        return degree_data
