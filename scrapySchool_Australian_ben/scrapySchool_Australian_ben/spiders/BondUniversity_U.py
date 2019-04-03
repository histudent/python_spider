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

class BondUniversity_USpider(scrapy.Spider):
    name = "BondUniversity_U"
    start_urls = ["https://bond.edu.au/intl/future-students/study-bond/search-program#undergraduate"]


    def parse(self, response):
        links = response.xpath("//div[@id='tab-undergraduate']//ul[@class='links-list']//li/a/@href").extract()
        # print(len(links))
        # links = list(set(links))
        # print(len(links))

        # 组合字典
        programme_dict = {}
        programme_list = response.xpath("//div[@id='tab-undergraduate']//ul[@class='links-list']//li/a//text()").extract()
        clear_space(programme_list)

        for link in range(len(links)):
            url = "https://bond.edu.au" + links[link]
            programme_dict[url] = programme_list[link]

        # # 过滤链接
        # for li1 in range(len(links)):
        #     if "graduate" in links[li1]:
        #         links[li1] = ""
        clear_space(links)
        print(len(links))
        links = list(set(links))
        print(len(links))

        for link1 in links:
            if link1 != "":
                url = "https://bond.edu.au" + link1
                yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "Bond University"
        # item['country'] = 'Australia'
        # item['website'] = 'https://bond.edu.au'
        item['url'] = response.url
        item['degree_type'] = 1
        item['major_type1'] = response.meta.get(response.url)
        print("===========================")
        print(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            degree_type = response.xpath("//h1[@class='page-title']//text()").extract()
            clear_space(degree_type)
            degree_type = ''.join(degree_type)
            item['degree_name'] = degree_type
            print("item['degree_name']: ", item['degree_name'])
            programme = degree_type
            if "(Business)" in degree_type:
                item['programme_en'] = "Business"
            else:
                item['programme_en'] = degree_type.replace("Bachelor of", "").strip()
            print("item['programme_en']: ", item['programme_en'])

            other = response.xpath("//html//article/blockquote[1]//text()").extract()
            item['other'] = clear_lianxu_space(other)
            # print("item['other']: ", item['other'])

            overview = response.xpath("//html//article/section[@class='section'][1]").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # if item['overview_en'] == "":
            #     print("***overview_en为空")
            print("item['overview_en']: ", item['overview_en'])

            degree_description = response.xpath("//div[@id='show-less-0']|//section[@id='accordion-program']/p").extract()
            item['degree_overview_en'] = remove_class(clear_lianxu_space(degree_description))
            # if item['degree_overview_en'] == "":
            #     print("***degree_overview_en为空")
            # print("item['degree_overview_en']: ", item['degree_overview_en'])

            # //html//section[@id='accordion-program']/div[@class='table-responsive']//tr[2]/td[2]
            duration = response.xpath(
                "//strong[contains(text(),'Duration')]/../following-sibling::td[1]//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration = ', '.join(duration)
            duration_re = re.findall(r"\d\ssemesters|\d\ssemester", duration)
            if len(duration_re) > 0:
                for d in duration_re:
                    item['duration'] = duration.replace(d, "").replace("(", "").replace(")", "").strip()
            else:
                item['duration'] = duration.replace("(", "").replace(")", "").strip()
            print("item['duration']: ", item['duration'])

            start_date = response.xpath(
                "//strong[contains(text(),'Starting semesters')]/../following-sibling::td[1]//text()").extract()
            clear_space(start_date)
            # print("start_date: ", start_date)
            monthDict = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06",
                         "july": "07", "august": "08", "september": "09", "october": "10", "november": "11",
                         "december": "12",
                         "jan": "01", "feb": "02", "mar": "03", "apr": "04", "may": "05", "jun": "06",
                         "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12",
                         "sept": "09", }
            std = []
            start_date_re = re.findall(r"january|february|march|april|may|june|july|august|september|october|november|december", ','.join(start_date), re.I)
            # print(start_date_re)
            if len(start_date_re) > 0:
                for s in start_date_re:
                    std_tmp = monthDict.get(s.lower())
                    if std_tmp is not None:
                        std.append(std_tmp)
            std = list(set(std))
            item['start_date'] = ','.join(std).replace("0", "").strip().strip(",").strip()
            print("item['start_date']: ", item['start_date'])

            career = response.xpath(
                "//div[@id='collapse-field_pgm_prof_out']|//a[@class='collapsed'][contains(text(),'Professional outcomes')]/../../..").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # if item['career_en'] == "":
            #     print("***career_en为空")
            print("item['career_en']: ", item['career_en'])

            modules = response.xpath(
                "//div[@id='collapse-field_pgm_str_sub']|//a[@class='collapsed'][contains(text(),'Structure and subjects')]/../../..").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # if item['modules_en'] == "":
            #     print("***modules_en为空")
            # print("item['modules_en']: ", item['modules_en'])

            tuition_fee = response.xpath(
                "//span[contains(@data-prefix,'Program fees 2019:')]//text()|//strong[contains(text(),'Program fees 2019')]/../text()|"
                "//strong[contains(text(),'2019 fees:')]/../text()").extract()  # 2019.03.20 星期三
            clear_space(tuition_fee)
            # print("tuition_fee: ", tuition_fee)
            tuition_fee_re = re.findall(r"\d+,\d+", ''.join(tuition_fee))
            if len(tuition_fee_re) > 0:
                item['tuition_fee'] = tuition_fee_re[0].replace(",", "").strip()
            print("item['tuition_fee']: ", item['tuition_fee'])

            entry_requirements = response.xpath(
                "//div[@id='collapse-field_pgm_ent_req']|//a[@data-toggle='collapse'][contains(text(),'Entry requirements')]/../../..|"
                "//h4[contains(text(),'Academic requirements')]/..").extract()  # 2019.03.20 星期三
            item['rntry_requirements_en'] = remove_class(clear_lianxu_space(entry_requirements))
            if item['rntry_requirements_en'] == "":
                print("***rntry_requirements_en为空")
            # print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

            # "https://bond.edu.au/intl/future-students/bond-international/information-international-students/international-english-language-testing-requirements"
            ielt_desc_dict = {"Bachelor of Business Law": "IELTS score 7.0 No sub score less than 6.5",
"Bachelor of Jurisprudence": "IELTS score 7.0 No sub score less than 6.5",
"Bachelor of Medical Studies (BMedSt) and the Doctor of Medicine (MD)": "IELTS score 7.0 No sub score less than 6.5",
"Bachelor of Laws": "IELTS score 7.0 No sub score less than 6.5",
"Bachelor of Psychological Science": "IELTS score 7.0 No sub score less than 6.5",
"Bachelor of Psychological Science (Honours)": "IELTS score 7.0 No sub score less than 6.5",
"Bachelor of Arts": "IELTS score 6.5 Writing 6.5, Reading 6.0, Listening 6.0, Speaking 6.0",
"Bachelor of Communication": "IELTS score 6.5 Writing 6.5, Reading 6.0, Listening 6.0, Speaking 6.0",
"Bachelor of Communication (Business)": "IELTS score 6.5 Writing 6.5, Reading 6.0, Listening 6.0, Speaking 6.0",
"Bachelor of Film and Television": "IELTS score 6.5 Writing 6.5, Reading 6.0, Listening 6.0, Speaking 6.0",
"Bachelor of Film and Television (3 Year Program)": "IELTS score 6.5 Writing 6.5, Reading 6.0, Listening 6.0, Speaking 6.0",
"Bachelor of Global Studies (Sustainability)": "IELTS score 6.5 Writing 6.5, Reading 6.0, Listening 6.0, Speaking 6.0",
"Bachelor of International Relations": "IELTS score 6.5 Writing 6.5, Reading 6.0, Listening 6.0, Speaking 6.0",
"Bachelor of Interactive Media and Design": "IELTS score 6.5 Writing 6.5, Reading 6.0, Listening 6.0, Speaking 6.0",
"Bachelor of Journalism": "IELTS score 6.5 Writing 6.5, Reading 6.0, Listening 6.0, Speaking 6.0",
"Bachelor of Social Science": "IELTS score 6.5 Writing 6.5, Reading 6.0, Listening 6.0, Speaking 6.0",
"Bachelor of Architectural Studies": "IELTS score 6.5 No sub score less than 6.0",
"Bachelor of Construction Management and Quantity Surveying": "IELTS score 6.5 No sub score less than 6.0",
"Bachelor of Sustainable Environments and Planning": "IELTS score 6.5 No sub score less than 6.0",
"Bachelor of Arts": "IELTS score 6.5 No sub score less than 6.0",
"Bachelor of Communication": "IELTS score 6.5 No sub score less than 6.0",
"Bachelor of Communication (Business)": "IELTS score 6.5 No sub score less than 6.0",
"Bachelor of Film and Television": "IELTS score 6.5 No sub score less than 6.0",
"Bachelor of Film and Television (3 Year Program)": "IELTS score 6.5 No sub score less than 6.0",
"Bachelor of Global Studies (Sustainability)": "IELTS score 6.5 No sub score less than 6.0",
"Bachelor of International Relations": "IELTS score 6.5 No sub score less than 6.0",
"Bachelor of Interactive Media and Design": "IELTS score 6.5 No sub score less than 6.0",
"Bachelor of Journalism": "IELTS score 6.5 No sub score less than 6.0",
"Bachelor of Jurisprudence": "IELTS score 6.5 No sub score less than 6.0",
"Bachelor of Laws": "IELTS score 6.5 No sub score less than 6.0",
"Bachelor of Social Science": "IELTS score 6.5 No sub score less than 6.0",
"Bachelor of Actuarial Science": "IELTS score 6.0 No sub score less than 6.0",}
            item['ielts_desc'] = ielt_desc_dict.get(item['degree_name'])
            print("item['ielts_desc']: ", item['ielts_desc'])

            if item['ielts_desc'] is not None:
                ieltlsrw = re.findall(r"\d[\d\.]{0,2}", item['ielts_desc'])
                if len(ieltlsrw) == 2:
                    item["ielts"] = ieltlsrw[0]
                    item["ielts_l"] = ieltlsrw[1]
                    item["ielts_s"] = ieltlsrw[1]
                    item["ielts_r"] = ieltlsrw[1]
                    item["ielts_w"] = ieltlsrw[1]
                elif len(ieltlsrw) == 1:
                    item["ielts"] = ieltlsrw[0]
                    item["ielts_l"] = ieltlsrw[0]
                    item["ielts_s"] = ieltlsrw[0]
                    item["ielts_r"] = ieltlsrw[0]
                    item["ielts_w"] = ieltlsrw[0]
                elif len(ieltlsrw) == 5:
                    item["ielts"] = ieltlsrw[0]
                    item["ielts_l"] = ieltlsrw[2]
                    item["ielts_s"] = ieltlsrw[2]
                    item["ielts_r"] = ieltlsrw[2]
                    item["ielts_w"] = ieltlsrw[1]
            print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                    item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            item['apply_desc_en'] = remove_class(clear_lianxu_space(["""<section class="section" id="section-8551"> <a id="application" name="application" class="anchor" ></a><h2 class="field field-name-field-title field-type-text field-label-hidden"> Application essentials</h2><div class="panel-group" id="accordion-8552" role="tablist" aria-multiselectable="true"><div class="panel panel-default"><div class="panel-heading"><h4 class="panel-title"> <a class="collapsed" data-toggle="collapse" data-parent="#accordion-8552" href="#collapse-8553"> Application process </a></h4></div><div id="collapse-8553" class="panel-collapse collapse"><div class="panel-body"><h3>Australian students</h3><p>Applications for most Bond programs can be lodged at any time directly to the University. With the exception of the <a href="https://bond.edu.au/intl/future-students/study-bond/search-program/medicine-bond">Medical Program</a>, you do not need to go through QTAC and your Bond application will not affect your QTAC application for other university programs. Apply direct to Bond University via our secure online <a href="https://apply.bond.edu.au/?refURL=/future-students/study-bond/how-apply" target="_blank">Application Form</a>.</p><h3>International students - full degree</h3><p>Apply directly to Bond using our secure online <a href="https://apply.bond.edu.au/?refURL=/future-students/study-bond/how-apply" target="_blank">Application Form</a> or through a representative in your country.</p><h3>English language students</h3><p>Apply to study English at Bond University College, located on the Bond University campus, by selecting your desired program below:</p><ul><li><a href="https://apply.bond.edu.au/">English for Academic Purposes</a></li><li><a href="https://college.bond.edu.au/apply-english">General English</a></li></ul><h3>Diploma, university preparation or foundation program students</h3><p>You can apply for your academic pathway through our secure online <a href="https://apply.bond.edu.au/?refURL=/future-students/study-bond/how-apply" target="_blank">Application Form</a>.</p><h3>Outbound exchange - Bond students</h3><p>Undergraduate Bond students must have completed two semesters prior to application while postgraduate Bondies can apply from their first semesters. Applications received in first and second semesters will be pending GPA requirements of 65% and above. Find out how to <a href="https://bond.edu.au/intl/future-students/bond-international/semester-abroad-exchange/outbound-bond">apply for exchange</a>.</p><h3>Inbound exchange students</h3><p>If your home institution has a formal exchange agreement with Bond, you will need to apply through them via their outbound exchange student application process. Your university may set certain academic performance standards for you to qualify for the program. Providing you meet their criteria, your home institution will contact Bond to nominate you as an exchange student and we will contact you to advise that your nomination has been successful. You will then be able to apply to Bond using our secure online <a href="https://apply.bond.edu.au/?refURL=/future-students/study-bond/how-apply" target="_blank">Application Form</a>, which must be accompanied by the required documentation. Exchange students pay their regular tuition fees to their home institution – not to Bond University.</p><h3>Study abroad students</h3><p>Firstly obtain approval from your home institution, then apply directly to Bond using our secure online <a href="https://apply.bond.edu.au/?refURL=/future-students/study-bond/how-apply" target="_blank">Application Form</a>; through a study abroad representative in your country; or through your home university if applicable.</p><ul></ul></div></div></div><div class="panel panel-default"><div class="panel-heading"><h4 class="panel-title"> <a class="collapsed" data-toggle="collapse" data-parent="#accordion-8552" href="#collapse-8554"> When can you start? </a></h4></div><div id="collapse-8554" class="panel-collapse collapse"><div class="panel-body"><p>Bond University runs three full semesters each year with intakes in January (Semester 1), May (Semester 2) and September (Semester 3). Our semesters are scheduled to coordinate with the Northern Hemisphere school/university timetables. (You’ll find that most other Australian universities offer only two semesters a year, meaning that you may have to wait until February or July before you can start your international studies.)</p></div></div></div><div class="panel panel-default"><div class="panel-heading"><h4 class="panel-title"> <a class="collapsed" data-toggle="collapse" data-parent="#accordion-8552" href="#collapse-8555"> Admissions criteria </a></h4></div><div id="collapse-8555" class="panel-collapse collapse"><div class="panel-body"><p>Bond University is committed to open and transparent admission processes, and to providing detailed information about the options and entry criteria that are relevant for you. </p><p>Learn more about our <a href="https://bond.edu.au/intl/future-students/study-bond/how-apply/undergraduate-admissions-criteria">undergraduate admissions criteria</a>. If you have further questions or wish to speak to one of our advisors, contact the <a href="https://bond.edu.au/intl/contact#ofs">Office of Future Students</a>.</p><p>For postgraduate study, the entry requirements are unique to each individual program. <a href="https://bond.edu.au/intl/future-students/study-bond/search-program#postgraduate">Search for your program</a> of interest to find out the specific entry requirements. </p></div></div></div><div class="panel panel-default"><div class="panel-heading"><h4 class="panel-title"> <a class="collapsed" data-toggle="collapse" data-parent="#accordion-8552" href="#collapse-8567"> Academic and English language entry requirements </a></h4></div><div id="collapse-8567" class="panel-collapse collapse"><div class="panel-body"><p>In addition to any performance standards stipulated by your home institution, you will also need to meet Bond’s academic and <a href="https://bond.edu.au/intl/future-students/bond-international/information-international-students/english-language-requirements">English language</a> requirements for the study program you have chosen.</p><p>If you need extra instruction, Bond offers <a href="https://college.bond.edu.au/english-at-bond">English classes</a> on campus through Bond University College, as well as a <a href="https://bond.edu.au/intl/program/bond-university-college-foundation-program">Foundation Program</a> to prepare you for university studies in Australia.</p></div></div></div></div></section>"""]))
            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<div class="panel-group" id="accordion-8552" role="tablist" aria-multiselectable="true"><div class="panel panel-default"><div class="panel-heading"><h4 class="panel-title"> <a class="collapsed" data-toggle="collapse" data-parent="#accordion-8552" href="#collapse-8553"> Application process </a></h4></div><div id="collapse-8553" class="panel-collapse collapse"><div class="panel-body"><h3>Australian students</h3><p>Applications for most Bond programs can be lodged at any time directly to the University. With the exception of the <a href="https://bond.edu.au/intl/future-students/study-bond/search-program/medicine-bond">Medical Program</a>, you do not need to go through QTAC and your Bond application will not affect your QTAC application for other university programs. Apply direct to Bond University via our secure online <a href="https://apply.bond.edu.au/?refURL=/future-students/study-bond/how-apply" target="_blank">Application Form</a>.</p><h3>International students - full degree</h3><p>Apply directly to Bond using our secure online <a href="https://apply.bond.edu.au/?refURL=/future-students/study-bond/how-apply" target="_blank">Application Form</a> or through a representative in your country.</p><h3>English language students</h3><p>Apply to study English at Bond University College, located on the Bond University campus, by selecting your desired program below:</p><ul><li><a href="https://apply.bond.edu.au/">English for Academic Purposes</a></li><li><a href="https://college.bond.edu.au/apply-english">General English</a></li></ul><h3>Diploma, university preparation or foundation program students</h3><p>You can apply for your academic pathway through our secure online <a href="https://apply.bond.edu.au/?refURL=/future-students/study-bond/how-apply" target="_blank">Application Form</a>.</p><h3>Outbound exchange - Bond students</h3><p>Undergraduate Bond students must have completed two semesters prior to application while postgraduate Bondies can apply from their first semesters. Applications received in first and second semesters will be pending GPA requirements of 65% and above. Find out how to <a href="https://bond.edu.au/intl/future-students/bond-international/semester-abroad-exchange/outbound-bond">apply for exchange</a>.</p><h3>Inbound exchange students</h3><p>If your home institution has a formal exchange agreement with Bond, you will need to apply through them via their outbound exchange student application process. Your university may set certain academic performance standards for you to qualify for the program. Providing you meet their criteria, your home institution will contact Bond to nominate you as an exchange student and we will contact you to advise that your nomination has been successful. You will then be able to apply to Bond using our secure online <a href="https://apply.bond.edu.au/?refURL=/future-students/study-bond/how-apply" target="_blank">Application Form</a>, which must be accompanied by the required documentation. Exchange students pay their regular tuition fees to their home institution – not to Bond University.</p><h3>Study abroad students</h3><p>Firstly obtain approval from your home institution, then apply directly to Bond using our secure online <a href="https://apply.bond.edu.au/?refURL=/future-students/study-bond/how-apply" target="_blank">Application Form</a>; through a study abroad representative in your country; or through your home university if applicable.</p><ul></ul></div></div></div></div>"""]))
            # print(item)
            # print("+++", "Graduate" not in item['degree_name'])
            if "/" not in item['degree_name'] or "/" not in item['degree_name'] and "online" not in item['degree_name'].lower():
                print("++++++++++++")
                major_list = response.xpath("//a[@id='majors']/following-sibling::div//div/div/h4/a//text()").extract()
                clear_space(major_list)
                print("major_list: ", major_list)
                print(len(major_list))

                if len(major_list) == 0:
                    yield item
                else:
                    modules_list = response.xpath("//a[@id='majors']/following-sibling::div//div/div/div").extract()
                    print("===", modules_list)
                    print(len(modules_list))
                    if len(modules_list) == len(major_list):
                        for m in range(len(major_list)):
                            item['programme_en'] = major_list[m]
                            item['modules_en'] = remove_class(clear_lianxu_space([modules_list[m]]))
                            print("item['programme_en']: ", item['programme_en'])
                            yield item

        except Exception as e:
            with open("scrapySchool_Australian_ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

