# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
import requests
from lxml import etree
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.getDuration import getIntDuration
from scrapySchool_England.remove_tags import remove_class

class LoughboroughUniversity_USpider(scrapy.Spider):
    name = "LoughboroughUniversity_P"
    # 研究领域链接
    start_urls = ["http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))

    # print(len(start_urls))

    def parse(self, response):
        #
        # programmeList = response.xpath(
        #     "//div[@class='programmes']/ul[@class='list list--programmes']/li/h2[@class='list__heading heading']/a[@class='list__link']//text()").extract()
        programmeList = response.xpath(
            "//div[@id='content']//ul[@class='list list--degrees']/li//a/h3/span[@class='list__heading-title']//text()").extract()
        # print("programmeList: ", programmeList)
        # print(len(programmeList))

        # departmentList = response.xpath(
        #     "//div[@class='programmes']/ul[@class='list list--programmes']/li/h3[@class='list__subheading subheading']/a[1]//text()").extract()
        #
        departmentList = response.xpath(
            "//div[@id='content']//ul[@class='list list--degrees']/li//a/p[@class='list__content list__content--department']//span[@class='list__text']//text()").extract()
        clear_space(departmentList)
        # print("departmentList: ", departmentList)
        # print(len(departmentList))

        departmentDict = {}
        for i in range(len(programmeList)):
            departmentDict[programmeList[i]] = departmentList[i]
        # print(departmentDict)
        links = response.xpath(
            "//div[@class='programmes']/ul[@class='list list--programmes']/li/h2[@class='list__heading heading']/a/@href|"
            "//div[@id='content']//ul[@class='list list--degrees']/li//a/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))

#         links = ["http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/mechanical-engineering/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/sport-exercise-nutrition/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/international-water-sanitation-engineering/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/sport-biomechanics/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/managing-innovation-creative-organisations/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/security-peace-building-diplomacy/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/media-cultural-analysis/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/internet-technologies-business-management/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/marketing/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/management/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/media-creative-industries/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/sport-exercise-psychology/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/international-water-sanitation-management/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/media-creative-industries-mres/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/mobile-communications/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/sport-business/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/materials-science-technology/",
# "http://www.lboro.ac.uk/study/postgraduate/masters-degrees/a-z/low-energy-building-services-engineering/", ]
        for link in links:
            url = "http://www.lboro.ac.uk" + link
            # url = link
            yield scrapy.Request(url, callback=self.parse_data, meta=departmentDict)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "Loughborough University"
        # item['country'] = 'England'
        # item['website'] = 'http://www.lboro.ac.uk/'
        item['url'] = response.url
        # 授课方式
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        print("===========================")
        print(response.url)
        try:
            # 学位名称
            degree_name = response.xpath(
                "//span[@class='emphasised']//text()|"
                "//h1[@class='degree-info__heading']/text()").extract()
            # print("degree_name: ", degree_name)
            item['degree_name'] = ''.join(degree_name).replace(', PG certificate', '').strip()
            print("item['degree_name']: ", item['degree_name'])

            # 专业
            programme_en = response.xpath(
                "//h1[@id='top']/text()|"
                "//h1[@class='degree-info__heading']/span//text()").extract()
            clear_space(programme_en)
            item['programme_en'] = ''.join(programme_en).strip()
            print("item['programme_en']: ", item['programme_en'])

            # 学院
            item['department'] = response.meta.get(item['programme_en'])
            print("item['department']: ", item['department'])

            # 授课类型
            mode = response.xpath(
                "//dt[@class='list__item list__item--term'][contains(text(),'Full-time:')]//text()").extract()
            clear_space(mode)
            if len(mode) != 0:
                item['teach_time'] = 'fulltime'
            # print("item['teach_time']: ", item['teach_time'])

            duration = response.xpath(
                "//dt[@class='list__item list__item--term'][contains(text(),'Full-time:')]/following-sibling::dd//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            # if 'year' in ''.join(duration):
            #     item['duration'] = int(''.join(duration).replace('year', '').strip())
            #     item['duration_per'] = 1
            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration']: ", item['duration'])
            # print("item['duration_per']: ", item['duration_per'])

            start_date = response.xpath(
                "//dt[@class='list__item list__item--term'][contains(text(),'Start date:')]/following-sibling::dd//text()").extract()
            clear_space(start_date)
            # print(start_date)
            item['start_date'] = ''.join(start_date).replace('(module restrictions apply)', '').strip()
            # print("item['start_date']: ", item['start_date'])

            # tuition_fee = response.xpath(
            #     "//dt[@class='list__item list__item--term'][contains(text(),'International fees:')]/following-sibling::dd//text()").extract()
            tuition_fee = response.xpath(
                "//span[contains(text(),'International fee')]/../following-sibling::dd//text()").extract()
            clear_space(tuition_fee)
            if "£" in ''.join(tuition_fee):
                item['tuition_fee_pre'] = '£'
                item['tuition_fee'] = ''.join(tuition_fee).replace('£', '').replace(',', '').strip()
            print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])
            print("item['tuition_fee']: ", item['tuition_fee'])

            location = response.xpath(
                "//dt[@class='list__item list__item--term'][contains(text(),'Location:')]/following-sibling::dd//text()").extract()
            clear_space(location)
            item['location'] = ''.join(location).strip()
            # print("item['location']: ", item['location'])

            allcontent = response.xpath("//nav[@class='programme-nav nav']/following-sibling::*//text()").extract()
            clear_space(allcontent)
            # print("allcontent: ", allcontent)

            # 专业描述
            if "Overview" in allcontent:
                overviewIndex = allcontent.index("Overview")
                if "Entry requirements" in allcontent:
                    overviewIndexEnd = allcontent.index("Entry requirements")
                    overview = allcontent[overviewIndex + 1:overviewIndexEnd]
                    # clear_space(overview)
                    item['overview_en'] = clear_lianxu_space(overview).strip("Entry requirements").strip()
            if item['overview_en'] != "":
                item['overview_en'] = "<h2>Overview</h2><div>" + item['overview_en'] + "</div>"
            else:
                overview = response.xpath("//span[contains(text(),'Entry')]/../../../../preceding-sibling::div").extract()
                overview_en = remove_class(clear_lianxu_space(overview))
                item['overview_en'] = overview_en
            print("item['overview_en']: ", item['overview_en'])

            entry = response.xpath("//h2[contains(text(),'Entry requirements')]/..//text()|"
                                   "//h2[contains(text(),'Entry Requirements')]/..//text()").extract()
            item['rntry_requirements'] = clear_lianxu_space(entry)
            # if item['rntry_requirements'] == "":
            #     print("entry_requ 为空")
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            # 学术要求
            # if "Entry requirements" in allcontent:
            #     entry_requirementsIndex = allcontent.index("Entry requirements")
            #     if "English Language requirements" in allcontent:
            #         entry_requirementsIndexEnd = allcontent.index("English Language requirements")
            #         entry_requirements = allcontent[entry_requirementsIndex:entry_requirementsIndexEnd]
            #         # clear_space(entry_requirements)
            #         item['rntry_requirements'] = clear_lianxu_space(entry_requirements).replace(
            #             "English Language requirements", "").strip()
            #     elif "English language requirements" in allcontent:
            #         entry_requirementsIndexEnd = allcontent.index("English language requirements")
            #         entry_requirements = allcontent[entry_requirementsIndex:entry_requirementsIndexEnd]
            #         # clear_space(entry_requirements)
            #         item['rntry_requirements'] = clear_lianxu_space(entry_requirements).strip().replace(
            #             "English language requirements", '').strip()
            #     elif "English Language Requirements" in allcontent:
            #         entry_requirementsIndexEnd = allcontent.index("English Language Requirements")
            #         entry_requirements = allcontent[entry_requirementsIndex:entry_requirementsIndexEnd]
            #         # clear_space(entry_requirements)
            #         item['rntry_requirements'] = clear_lianxu_space(entry_requirements).replace(
            #             "English Language Requirements", '').strip()
            # item['rntry_requirements'] = "Entry requirements " + item['rntry_requirements'].replace(
            #     "Entry requirements", "").strip()
            # print("item['rntry_requirements']: ", item['rntry_requirements'])



            # IELTS
            ielts_toefl = response.xpath("//h2[contains(text(),'English')]/..//text()").extract()
            clear_space(ielts_toefl)
            if len(ielts_toefl) == 0:
                print("ielts_toefl 为空")
            ielts = "".join(ielts_toefl)
            # if "English Language requirements" in allcontent:
            #     ieltsIndex = allcontent.index("English Language requirements")
            #     if "What you'll study" in allcontent:
            #         ieltsIndexIndexEnd = allcontent.index("What you'll study")
            #         ielts = allcontent[ieltsIndex:ieltsIndexIndexEnd]
            #         clear_space(ielts)
            #         ielts = ''.join(ielts).strip()
            # elif "English language requirements" in allcontent:
            #     ieltsIndex = allcontent.index("English language requirements")
            #     if "What you'll study" in allcontent:
            #         ieltsIndexIndexEnd = allcontent.index("What you'll study")
            #         ielts = allcontent[ieltsIndex:ieltsIndexIndexEnd]
            #         clear_space(ielts)
            #         ielts = ''.join(ielts).strip()
            # elif "English Language Requirements" in allcontent:
            #     ieltsIndex = allcontent.index("English Language Requirements")
            #     if "What you'll study" in allcontent:
            #         ieltsIndexIndexEnd = allcontent.index("What you'll study")
            #         ielts = allcontent[ieltsIndex:ieltsIndexIndexEnd]
            #         clear_space(ielts)
            #         ielts = ''.join(ielts).strip()
            # elif "English Language Entry Requirements" in allcontent:
            #     ieltsIndex = allcontent.index("English Language Entry Requirements")
            #     if "What you'll study" in allcontent:
            #         ieltsIndexIndexEnd = allcontent.index("What you'll study")
            #         ielts = allcontent[ieltsIndex:ieltsIndexIndexEnd]
            #         clear_space(ielts)
            #         ielts = ''.join(ielts).strip()
            ielts_re = re.findall(r"IELTS.{1,80}", ielts)
            # print("ielts_re = ", ielts_re)
            toefl_re = re.findall(r"TOEFL.{1,80}", ielts)
            # print("toefl_re = ", toefl_re)

            item['ielts_desc'] = ''.join(ielts_re)
            print("item['ielts_desc']: ", item['ielts_desc'])
            item['toefl_desc'] = ''.join(toefl_re)
            print("item['toefl_desc']: ", item['toefl_desc'])

            ieltsDict = get_ielts(item['ielts_desc'])
            item['ielts'] = ieltsDict.get("IELTS")
            item['ielts_l'] = ieltsDict.get("IELTS_L")
            item['ielts_s'] = ieltsDict.get("IELTS_S")
            item['ielts_r'] = ieltsDict.get("IELTS_R")
            item['ielts_w'] = ieltsDict.get("IELTS_W")
            print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            toeflDict = get_toefl(item['toefl_desc'])
            item["toefl"] = toeflDict.get("TOEFL")  # float
            item["toefl_l"] = toeflDict.get("TOEFL_L")  # float
            item["toefl_s"] = toeflDict.get("TOEFL_S")  # float
            item["toefl_r"] = toeflDict.get("TOEFL_R")  # float
            item["toefl_w"] = toeflDict.get("TOEFL_W")
            # print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
            #         item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

            # modules
            if "What you'll study" in allcontent:
                modulesIndex = allcontent.index("What you'll study")
                if "How you'll be assessed" in allcontent:
                    modulesIndexEnd = allcontent.index("How you'll be assessed")
                    modules = allcontent[modulesIndex:modulesIndexEnd]
                    # clear_space(modules)
                    item['modules_en'] = clear_lianxu_space(modules)
                elif "How you'll study" in allcontent:
                    modulesIndexEnd = allcontent.index("How you'll study")
                    modules = allcontent[modulesIndex:modulesIndexEnd]
                    # clear_space(modules)
                    item['modules_en'] = clear_lianxu_space(modules)
            item['modules_en'] = "<div>" + item['modules_en'] + "</div>"
            # module = response.xpath(r"//h3[@class='subheading'][contains(text(),'Modules')]/../../preceding-sibling::div[1]/following-sibling::div[@class='content-type content-type--toggle']").extract()
            # print("module: ", module)
            # print(len(module))
            # print("item['modules_en']: ", item['modules_en'])

            # teaching_assessment
            if "How you'll be assessed" in allcontent:
                teaching_assessmentIndex = allcontent.index("How you'll be assessed")
                if "Your personal and professional development" in allcontent:
                    teaching_assessmentIndexEnd = allcontent.index("Your personal and professional development")
                    teaching_assessment = allcontent[teaching_assessmentIndex + 1:teaching_assessmentIndexEnd]
                    item['assessment_en'] = "<h2>How you'll be assessed</h2><div>" + clear_lianxu_space(
                        teaching_assessment) + "</div>"
            elif "How you'll study" in allcontent:
                teaching_assessmentIndex = allcontent.index("How you'll study")
                if "Your personal and professional development" in allcontent:
                    teaching_assessmentIndexEnd = allcontent.index("Your personal and professional development")
                    teaching_assessment = allcontent[teaching_assessmentIndex + 1:teaching_assessmentIndexEnd]
                    item['assessment_en'] = "<h2>How you'll study</h2><div>" + clear_lianxu_space(
                        teaching_assessment) + "</div>"
            # print("item['assessment_en']: ", item['assessment_en'])

            # career
            if "Your personal and professional development" in allcontent:
                careerIndex = allcontent.index("Your personal and professional development")
                if "Fees and funding" in allcontent:
                    careerIndexEnd = allcontent.index("Fees and funding")
                    career = allcontent[careerIndex + 1:careerIndexEnd]
                    item['career_en'] = clear_lianxu_space(career)
            item['career_en'] = "<h2>Your personal and professional development</h2><div>" + item[
                'career_en'] + "</div>"
            # print("item['career_en']: ", item['career_en'])

            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<div id="content-wrapper-wide" class="standard ">
<div class="content-wrapper">
<a name="d.en.1074686"></a>
<h3>Postgraduate</h3>
<p>Students are required to have a bachelor degree (4 years) for entry to a postgraduate programme. The University uses the <a href="http://rank2013.netbig.com/">Netbig 2013</a> university ranking to identify the required final mark, as outlined on the table below:&nbsp;</p>
<table border="1" cellpadding="0" cellspacing="0" style="width: 650px;">
<tbody>
<tr>
<td valign="top" width="121">
<p><strong>NETBIG rank 2013 </strong></p>
</td>
<td valign="top" width="130">
<p align="center"><strong>First</strong></p>
</td>
<td valign="top" width="130">
<p align="center"><strong>High 2:1 <br /> (65%)</strong></p>
</td>
<td valign="top" width="134">
<p align="center"><strong>2:1</strong></p>
</td>
<td valign="top" width="132">
<p align="center"><strong>High 2:2 <br /> (55-57%)</strong></p>
</td>
<td valign="top" width="132">
<p align="center"><strong>2:2</strong></p>
</td>
</tr>
<tr>
<td valign="top" width="121">
<p><strong>Top 150</strong></p>
</td>
<td valign="top" width="130">
<p align="center">84</p>
</td>
<td valign="top" width="130">
<p align="center">81</p>
</td>
<td valign="top" width="134">
<p align="center">80</p>
</td>
<td valign="top" width="132">
<p align="center">78</p>
</td>
<td valign="top" width="132">
<p align="center">77</p>
</td>
</tr>
<tr>
<td valign="top" width="121">
<p><strong>151-250</strong></p>
</td>
<td valign="top" width="130">
<p align="center">87</p>
</td>
<td valign="top" width="130">
<p align="center">83</p>
</td>
<td valign="top" width="134">
<p align="center">82</p>
</td>
<td valign="top" width="132">
<p align="center">80</p>
</td>
<td valign="top" width="132">
<p align="center">79</p>
</td>
</tr>
<tr>
<td valign="top" width="121">
<p><strong>251-500</strong></p>
</td>
<td valign="top" width="130">
<p align="center">89</p>
</td>
<td valign="top" width="130">
<p align="center">85</p>
</td>
<td valign="top" width="134">
<p align="center">84</p>
</td>
<td valign="top" width="132">
<p align="center">82</p>
</td>
<td valign="top" width="132">
<p align="center">80</p>
</td>
</tr>
<tr>
<td valign="top" width="121">
<p><strong>501+</strong></p>
</td>
<td valign="top" width="130">
<p align="center">92</p>
<p align="center"><span>(SBE: No Offer)</span></p>
</td>
<td valign="top" width="130">
<p align="center">87</p>
<p align="center">(SBE: No Offer)</p>
</td>
<td valign="top" width="134">
<p align="center">86</p>
<p align="center"><span>(SBE: No Offer)</span></p>
</td>
<td valign="top" width="132">
<p align="center">85</p>
<p align="center"><span>(SBE: No Offer)</span></p>
</td>
<td valign="top" width="132">
<p align="center">82</p>
<p align="center"><span>(SBE: No Offer)</span></p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<div class="clear"></div>
</div><!-- #content-wrapper -->
</div><!-- #content-wrapper-wide -->
<div class="clear"></div>    <!-- ACCORDION - STANDARD - SINGLE -->
<div class="content-wrapper">
<h3 class="trigger fcbg1"><a href="#">Affiliated Colleges</a></h3>
<div class="toggle_container">
<p>The University will consider students from Colleges affiliated to 211 and 985 universities and universities in the top 150 Netbig 2013 rankings. &nbsp;Applicants from these Colleges will be considered as follows:</p>
<ul>
<li>School of Business and Economics with 82% &ndash; 85%</li>
<li>All other programmes with 79% &ndash; 83%.&nbsp;</li>
</ul>
<p>Students from Colleges affiliated to universities with a Netbig 2013 rank of 151 &ndash; 250 will be considered as follows:</p>
<ul>
<li>School of Business and Economics with 85% &ndash; 86%</li>
<li>All other programmes with 80% &ndash; 85%.</li>
</ul>
<p>Students from Colleges affiliated to universities with a Netbig 2013 rank of 251 &ndash; 500 will be considered as follows:</p>
<ul>
<li>School of Business and Economics: not considered</li>
<li>All other programmes with 82% &ndash; 86%.</li>
</ul>
</div>
</div><!-- #content-wrapper -->    <!-- ACCORDION - STANDARD - SINGLE -->
<div class="content-wrapper">
<h3 class="trigger fcbg1"><a href="#">Business and Economics</a></h3>
<div class="toggle_container">
<p>The School of Business and Economics will give special consideration to students who have studied at a university which specialises in business or has expertise in another area.&nbsp; A list of these universities and the grades required can be found here:&nbsp;<a href="/terminalfour/SiteManager?ctfn=download&amp;fnno=60&amp;ceid=273195225">SBE Chinese Universities</a>&zwnj;.&nbsp; Applicants from these universities will be considered with 77% - 84% (depending on programme applied to).</p>
<p>Students who do not meet the above requirements may be considered if they have a relevant degree, can show good grades in relevant subjects, and/or have substantial relevant work experience.</p>
</div>
</div>"""]))
            print("item['require_chinese_en']: ", item['require_chinese_en'])

            item['apply_proces_en'] = "http://www.lboro.ac.uk/study/postgraduate/apply/taught-applications/"
            print("item['apply_proces_en']: ", item['apply_proces_en'])
            yield item

        except Exception as e:
            with open("scrapySchool_England/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)
