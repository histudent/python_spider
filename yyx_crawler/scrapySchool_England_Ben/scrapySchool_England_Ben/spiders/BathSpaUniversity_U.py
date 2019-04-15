import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getIELTS import get_ielts
from scrapySchool_England_Ben.getDuration import getIntDuration

class BathSpaUniversity_USpider(scrapy.Spider):
    name = "BathSpaUniversity_U"
    start_urls = ["https://www.bathspa.ac.uk/courses/course-index-a-z/"]


    def parse(self, response):
        links = response.xpath("//h3[@class='title'][contains(text(),'Undergraduate')]/following-sibling::div[1]//a/@href|"
                               "//h2[contains(text(),'Undergraduate course combinations')]/following-sibling::div//a/@href").extract()
        # links1 = response.xpath("//h3[@class='title'][contains(text(),'Undergraduate')]/following-sibling::div[1]//a/@href|"
        #                        "//h2[contains(text(),'Undergraduate course combinations')]/following-sibling::div//a/@href").extract()
        # 组合字典
        programme_dict = {}
        programme_list = response.xpath(
            "//h3[@class='title'][contains(text(),'Undergraduate')]/following-sibling::div[1]//a//text()|"
            "//h2[contains(text(),'Undergraduate course combinations')]/following-sibling::div//a//text()").extract()
        clear_space(programme_list)

        for link in range(len(links)):
            url = "https://www.bathspa.ac.uk" + links[link]
            programme_dict[url] = programme_list[link]

        print(len(links))
        links = list(set(links))
        print(len(links))
#         links = ["https://www.bathspa.ac.uk/courses/ug-3d-design-idea-material-object/",
# "https://www.bathspa.ac.uk/courses/ug-publishing/",
# "https://www.bathspa.ac.uk/courses/ug-youth-and-community-studies/", ]
        for link in links:
            url = "https://www.bathspa.ac.uk" + link
            # url = link
            # url = "https://www.bathspa.ac.uk/courses/ug-furniture-and-product-design/"
            yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "https://www.bathspa.ac.uk/"
        item['university'] = "Bath Spa University"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        item['major_type1'] = response.meta.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            item['location'] = 'Bath'
            # 专业、学位类型//div[@class='masthead-inner']/div/div[@class='masthead-content']/h1
            programme = response.xpath("//div[@class='masthead-inner']/div/div[@class='masthead-content']/h1//text()").extract()
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en']: ", item['programme_en'])

            degree_type = response.xpath("//div[@class='masthead-inner']/div/div[@class='masthead-content']/p[1]//text()").extract()
            item['degree_name'] = ''.join(degree_type).replace("(Hons)", "").strip()
            print("item['degree_name']: ", item['degree_name'])

            # //dt[contains(text(),'School')]/following-sibling::dd[1]
            department = response.xpath("//dt[contains(text(),'School')]/following-sibling::dd[1]//text()").extract()
            item['department'] = ''.join(department).strip()
            # print("item['department']: ", item['department'])

            location = response.xpath(
                "//dt[contains(text(),'Campus or location')]/following-sibling::dd[1]//text()").extract()
            item['location'] = ''.join(location).strip()
            # print("item['location']: ", item['location'])

            modules = response.xpath(
                "//h3[contains(text(),'Course structure')]/..|//h3[contains(text(),'Course modules')]/..|//h2[contains(text(),'Course modules')]/..").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])

            career = response.xpath("//h3[contains(text(),'Career')]/..").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            feeContent = response.xpath(
                "//h3[contains(text(),'International students full time')]/../div/table[1]//td[contains(text(), 'Year')]/following-sibling::td//text()").extract()
            clear_space(feeContent)
            # print(feeContent)
            if len(feeContent) > 0:
                item['tuition_fee'] = int(feeContent[0].replace("£", "").replace(",", "").strip())
            # print("item['tuition_fee']: ", item['tuition_fee'])

            alevel = response.xpath("//span[contains(text(),'A Level')]/..//text()|//li[contains(text(),'A Level')]//text()").extract()
            item['alevel'] = ''.join(alevel).strip()
            # print("item['alevel']: ", item['alevel'])
            # if item['alevel'] == "":
            #     print("****alevel")

            ib = response.xpath("//span[contains(text(),'International Baccalaureate')]/..//text()|"
                "//li[contains(text(),'International Baccalaureate')]//text()").extract()
            item['ib'] = ''.join(ib).strip()
            # print("item['ib']: ", item['ib'])
            # if item['ib'] == "":
            #     print("****ib")

            # //div[@class='content']/div[@class='collapsible-content highlighted']/div[2]/div[2]

            ieltsList = response.xpath("//*[contains(text(),'IELTS')]//text()").extract()
            item['ielts_desc'] = ''.join(ieltsList).strip()
            # print("item['ielts_desc']: ", item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            interview_desc_en = response.xpath("//h3[contains(text(),'Interview and portfolio guidance')]/..|"
                                               "//h3[contains(text(),'Portfolio and interview')]/..").extract()
            item['interview_desc_en'] = remove_class(clear_lianxu_space(interview_desc_en))
            # print("item['interview_desc_en']: ", item['interview_desc_en'])
            # if item['interview_desc_en'] == "":
            #     print("****interview_desc_en")

            portfolio_desc_en = response.xpath("//h3[contains(text(),'Interview and portfolio guidance')]/..|"
                                               "//h3[contains(text(),'Portfolio')]/..").extract()
            item['portfolio_desc_en'] = remove_class(clear_lianxu_space(portfolio_desc_en))
            # print("item['portfolio_desc_en']: ", item['portfolio_desc_en'])
            # if item['portfolio_desc_en'] == "":
            #     print("****portfolio_desc_en")

            # https://www.bathspa.ac.uk/international/country-advice/china/

            item['require_chinese_en'] = "<p><strong>Undergraduate</strong></p><ul><li>Senior Secondary School Graduation Certificate with a grade of 70% and a Foundation Certification from a recognised institution.</li></ul><p><strong>Undergraduate - Year 2 or 3 entry</strong></p><ul><li>Students with a Dazhuan Certificate will be considered for Year 3 entry on an individual basis.&nbsp;</li></ul>"

            # https://www.bathspa.ac.uk/applicants/how-to-apply/postgraduate/
            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<div class="intro-text">
	<p class="intro">We’re delighted you’re applying to study with us. The process is different based on your location and mode of study. Here’s what you need to do.</p>
</div><div class="rich-text" >
  <div data-hash-anchor='<a id="d.en.1281"></a>'></div>
    <div>
        <h2>UCAS applicants</h2>
<p>If you fit the following criteria, you’ll need to apply through the Universities and Colleges Admissions Service (UCAS):</p>
<ul>
<li>You’re applying directly out of sixth form or college;</li>
<li>You want to study full-time;</li>
<li>You don’t already hold an undergraduate qualification and are from the UK, EU or Channel Islands.</li>
</ul>
<p><strong>The official UCAS deadline for 2018/19 applications to any course: 15 January 2018.</strong></p>
<p>You’ll need some information from your course's webpage, including Bath Spa University’s institution code: BASPA B20.</p>
<p>Read more about <a href="/applicants/how-to-apply/undergraduate-and-foundation/how-to-apply-through-ucas/">how to </a><a href="/applicants/how-to-apply/undergraduate-and-foundation/how-to-apply-through-ucas/">apply through UCAS</a> or just get started. You’ll need to register or login to the UCAS site. &nbsp;</p>
<p><a href="https://www.ucas.com/ucas/undergraduate/ucas-undergraduate-apply-and-track">Apply via UCAS</a></p>
<h2>International applicants</h2>
<p>You can apply for one of our undergraduate courses online from the course’s webpage.&nbsp;You’ll be asked to create an online account.</p>
<p>Don’t have time to complete your whole application? Don’t worry, you can save your application and come back to it at anytime.</p>
<p>Alternatively, you can also <a href="https://www.ucas.com/ucas/undergraduate/ucas-undergraduate-apply-and-track">apply via UCAS</a>.</p>
<p>Entry requirements are listed on the course pages. As part of the process you will be required to provide evidence to support your application.&nbsp;Please see our <a href="/international/">international</a> webpages for more information for international students, including entry requirements and visa advice specific to your country.</p>
<p><a href="/courses/">Search for your course</a></p>
<h2>Applying for part-time study</h2>
<p>If you’d like to study part-time, you’ll need to apply online directly with us, rather than through UCAS. &nbsp;</p>
<p><strong>Click the 'apply now' button on the webpage for the course you’d like to study.</strong></p>
<h2>Already hold an undergraduate degree?</h2>
<p>If you already have a degree or higher qualification than that for which you are applying, your fee requirements may be different, due to the way government University funding is distributed. Please check the Equivalent or Lower Qualification (ELQ) policy&nbsp;for more details.<br><br>This also applies to students who progress to the third year of study, following completion of a Foundation Degree. Please note that Foundation Degrees are currently exempt from higher fees.</p>
    </div>
</div>"""]))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            ucascode = response.xpath("//dd[contains(text(),'Course Code:')]//text()").extract()
            clear_space(ucascode)
            print("ucascode: ", ucascode)
            item['ucascode'] = ''.join(ucascode).replace("Course Code:", "").strip()
            print("len: ", len(ucascode))
            print("item['ucascode'] = ", item['ucascode'])

            # duration
            durationMode = response.xpath(
                "//dt[contains(text(),'Course length')]/following-sibling::dd[1]//text()").extract()
            clear_space(durationMode)
            print("durationMode: ", durationMode)
            durationMode = ''.join(durationMode)
            duration_list = getIntDuration(durationMode.strip())
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            print("item['duration']: ", item['duration'])
            print("item['duration_per']: ", item['duration_per'])
            item['other'] = durationMode
            print("item['other']: ", item['other'])

            if "or" in item['ucascode']:
                ucascode_list1 = item['ucascode'].split("or")
                print("ucascode_list1", ucascode_list1)

                # 拆分duration
                if ", or" in item['other']:
                    duration_list1 = item['other'].split(", or")
                else:
                    duration_list1 = [item['other'], item['other']]
                print("duration_list1: ", duration_list1)
                for u in range(len(ucascode_list1)):
                    item['ucascode'] = ucascode_list1[u].strip()
                    duration_list = getIntDuration(duration_list1[u].strip())
                    if len(duration_list) == 2:
                        item['duration'] = duration_list[0]
                        item['duration_per'] = duration_list[-1]
                    print("item['duration']: ", item['duration'])
                    print("item['duration_per']: ", item['duration_per'])
                    # 分为两种情况，第一种正常采集，第二种为带实习的专业
                    if u == 0:
                        overview = response.xpath("""//h2[contains(text(),"What you'll learn")]/following-sibling::div//h3[contains(text(),'Overview')]/..""").extract()
                        if len(overview) == 0:
                            overview = response.xpath("""//h2[contains(text(),"What you'll learn")]/following-sibling::div//h3[contains(text(),'overview')]/..""").extract()
                        item['overview_en'] = remove_class(clear_lianxu_space(overview))
                        # print("item['overview_en']1: ", item['overview_en'])

                        assessment_en = response.xpath(
                            """//h2[contains(text(),"What you'll learn")]/following-sibling::div//h3[contains(text(),'How will I be assessed?')]/..|
                            //h2[contains(text(),"What you'll learn")]/following-sibling::div//h3[contains(text(),'How will I be taught?')]/..|
                            //h2[contains(text(),"What you'll learn")]/following-sibling::div//h3[contains(text(),'Assessment')]/..""").extract()
                        item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
                        # print("item['assessment_en']1: ", item['assessment_en'])
                    elif u ==1:
                        overview = response.xpath(
                            """//h2[contains(text(),"Professional placement year")]/following-sibling::div//h3[contains(text(),'Overview')]/..""").extract()
                        if len(overview) == 0:
                            overview = response.xpath(
                                """//h2[contains(text(),"Professional placement year")]/following-sibling::div//h3[contains(text(),'overview')]/..""").extract()
                            if len(overview) == 0:
                                overview = response.xpath(
                                    """//h3[contains(text(),'Overview')]/..|//h3[contains(text(),'overview')]/..""").extract()
                        item['overview_en'] = remove_class(clear_lianxu_space(overview))
                        # print("item['overview_en']2: ", item['overview_en'])

                        assessment_en = response.xpath(
                            "//h2[contains(text(),'Professional placement year')]/following-sibling::div//h3[contains(text(),'How will I be assessed?')]/..|"
                            "//h2[contains(text(),'Professional placement year')]/following-sibling::div//h3[contains(text(),'How will I be taught?')]/..|"
                            "//h2[contains(text(),'Professional placement year')]/following-sibling::div//h3[contains(text(),'Assessment')]/..").extract()
                        if len(assessment_en) == 0:
                            assessment_en = response.xpath(
                                "//h3[contains(text(),'How will I be assessed?')]/..|"
                                "//h3[contains(text(),'How will I be taught?')]/..|"
                                "//h3[contains(text(),'Assessment')]/..").extract()
                        item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
                        # print("item['assessment_en']2: ", item['assessment_en'])
                    yield item
            else:
                overview = response.xpath(
                    """//h2[contains(text(),"What you'll learn")]/following-sibling::div//h3[contains(text(),'Overview')]/..""").extract()
                if len(overview) == 0:
                    overview = response.xpath(
                        """//h2[contains(text(),"What you'll learn")]/following-sibling::div//h3[contains(text(),'overview')]/..""").extract()
                item['overview_en'] = remove_class(clear_lianxu_space(overview))
                # print("item['overview_en']1: ", item['overview_en'])

                assessment_en = response.xpath(
                    """//h2[contains(text(),"What you'll learn")]/following-sibling::div//h3[contains(text(),'How will I be assessed?')]/..|
                    //h2[contains(text(),"What you'll learn")]/following-sibling::div//h3[contains(text(),'How will I be taught?')]/..|
                    //h2[contains(text(),"What you'll learn")]/following-sibling::div//h3[contains(text(),'Assessment')]/..""").extract()
                item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
                # print("item['assessment_en']1: ", item['assessment_en'])
                yield item

        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)


#            department_dict = {"arts management":"Bath Business School","accounting and finance":"Bath Business School",
# "business and management":"Bath Business School",
# "business and management (accounting)":"Bath Business School",
# "business and management (entrepreneurship)":"Bath Business School",
# "business and management (international business)":"Bath Business School",
# "business and management (marketing)":"Bath Business School",
# "curatorial practice":"Bath School of Art and Design",
# "design (ceramics)":"Bath School of Art and Design",
# "design (fashion and textiles)":"Bath School of Art and Design",
# "fine art":"Bath School of Art and Design",
# "visual communication":"Bath School of Art and Design",
# "children's publishing":"College of Liberal Arts",
# "classical acting":"College of Liberal Arts",
# "composition":"College of Liberal Arts",
# "creative producing":"College of Liberal Arts",
# "creative writing":"College of Liberal Arts",
# "creative writing phd":"College of Liberal Arts",
# "crime and gothic fictions":"College of Liberal Arts",
# "dance":"College of Liberal Arts",
# "directing":"College of Liberal Arts",
# "directing circus":"College of Liberal Arts",
# "environmental humanities":"College of Liberal Arts",
# "environmental management":"College of Liberal Arts",
# "feature filmmaking":"College of Liberal Arts",
# "heritage management":"College of Liberal Arts",
# "intercultural musicology":"College of Liberal Arts",
# "liberal arts":"College of Liberal Arts",
# "literature, landscape and environment":"College of Liberal Arts",
# "music performance":"College of Liberal Arts",
# "performing shakespeare":"College of Liberal Arts",
# "principles of applied neuropsychology":"College of Liberal Arts",
# "scriptwriting":"College of Liberal Arts",
# "songwriting (campus based)":"College of Liberal Arts",
# "songwriting (distance learning)":"College of Liberal Arts",
# "sound (arts)":"College of Liberal Arts",
# "sound (design)":"College of Liberal Arts",
# "sound (production)":"College of Liberal Arts",
# "theatre for young audiences":"College of Liberal Arts",
# "transnational writing":"College of Liberal Arts",
# "travel and nature writing":"College of Liberal Arts",
# "writing for young people":"College of Liberal Arts",
# "counselling and psychotherapy practice":"Institute for Education",
# "education (education studies)":"Institute for Education",
# "education (early childhood studies)":"Institute for Education",
# "education (international education)":"Institute for Education",
# "education (leadership and management)":"Institute for Education",
# "inclusive education":"Institute for Education",
# "professional practice":"Institute for Education",
# "professional practice in higher education":"Institute for Education",
# "teaching english to speakers of other languages":"Institute for Education",
# "specific learning difficulties / dyslexia":"Institute for Education",
# "national award for special educational needs coordination":"Institute for Education",
# "professional doctorate in education":"Institute for Education",
# }