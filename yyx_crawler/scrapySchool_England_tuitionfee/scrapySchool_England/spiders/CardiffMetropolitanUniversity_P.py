# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getDuration import getIntDuration, getTeachTime


class CardiffMetropolitanUniversity_PSpider(scrapy.Spider):
    name = "CardiffMetropolitanUniversity_P"
    start_urls = ["http://www.cardiffmet.ac.uk/study/Pages/Postgraduate-Courses-A-Z.aspx"]

    def parse(self, response):
        alllinks = response.xpath("//ul[@class='dfwp-column dfwp-list']//a/@href").extract()
        # print(len(set(alllinks)))
        alllinks = list(set(alllinks))
        # print(len(set(alllinks)))
        for url in alllinks:
            # print("url = ", url)
            # url = "http://www.cardiffmet.ac.uk/health/courses/Pages/Food-Safety-Management---MSc-PgD-.aspx"
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.cardiffmet.ac.uk/"
        item['university'] = "Cardiff Metropolitan University"
        item['url'] = response.url
        # 授课方式
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        item['location'] = 'Llandaff Campus, Western Avenue, Cardiff, CF5 2YB'
        # print("item['location'] = ", item['location'])
        print("===========================")
        print(response.url)
        try:
            # 专业、学位类型
            programmeDegreetype = response.xpath("//div[@id='ordercontainer']/span[@id='DeltaPlaceHolderMain']/div[@class='coursefullwidth']/div/h1//text()|//div[@class='cstcoursetitle']/h1/text()").extract()
            # print("programmeDegreetype: ", programmeDegreetype)
            clear_space(programmeDegreetype)
            programmeDegreetypeStr = ''.join(programmeDegreetype).replace("–", "-").strip()
            print("programmeDegreetypeStr: ", programmeDegreetypeStr)
            programmeDegreetypesplit = programmeDegreetypeStr.split("-")
            print(programmeDegreetypesplit)
            if len(programmeDegreetypesplit) > 1:
                degreetype = programmeDegreetypesplit[-1]
                # print(degreetype)
                item['degree_name'] = degreetype.strip()
                programme = programmeDegreetypesplit[0].strip()
                # print(programme)
                item['programme_en'] = ''.join(programme)
            else:
                programme = programmeDegreetypesplit[0]
                # print(programme)
                item['programme_en'] = item['degree_name'] = ''.join(programme).strip()

            if item['degree_name'] == "" and "mba" in item['programme_en'].lower():
                item['degree_name'] = "MBA"
            elif item['degree_name'] == "" and "MA " in item['programme_en']:
                item['degree_name'] = "MA"
                item['programme_en'] = item['programme_en'].replace("MA", "").strip()
            print("item['degree_name']: ", item['degree_name'])
            print("item['programme_en']: ", item['programme_en'])

            department = response.xpath(
                "//div[@class='crumbcontainer']/span/span[1]/a[1]//text()").extract()
            clear_space(department)
            item['department'] = ''.join(department)
            print("item['department'] = ", item['department'])

            duration = response.xpath(
                "//strong[contains(text(),'Course Length:')]/..//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            item['teach_time'] = getTeachTime(''.join(duration))
            duration_list = getIntDuration(''.join(duration))
            # print("duration_list: ", duration_list)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['teach_time'] = ", item['teach_time'])
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            # //div[@id='ordercontainer']/span[@id='DeltaPlaceHolderMain']/div[@class='coursefullwidth']/div[@class='rightcontainer']/div[@class='coursefacts']/div/div//p
            overview = response.xpath(
                "//div[@id='ordercontainer']/span[@id='DeltaPlaceHolderMain']/div[@class='coursefullwidth']/div[@class='coursecontentarea']/div[@class='courseoverview']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])

            modules_en = response.xpath(
                "//h3[contains(text(),'Course Content')]/following-sibling::div[1]").extract()
            if len(modules_en) == 0:
                modules_en = response.xpath("//h3[contains(text(),'Course content')]/..").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules_en))
            if item['modules_en'] != "":
                item['modules_en'] = "<h3>Course Content</h3>" + item['modules_en']
            # print("item['modules_en']: ", item['modules_en'])

            assessment_en = response.xpath(
                "//h3[contains(text(),'Learning & Teaching')]/following-sibling::div[1]").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            if item['assessment_en'] != "":
                item['assessment_en'] = "<h3>Learning & Teaching</h3>" + item['assessment_en']

            assessment_en1 = response.xpath("//h3[contains(text(),'Assessment')]/following-sibling::div[1]").extract()
            # print(len(assessment_en1))
            if len(assessment_en1) != 0:
                item['assessment_en'] += "<h3>Assessment</h3>" + remove_class(clear_lianxu_space(assessment_en1))
            # print("item['assessment_en']: ", item['assessment_en'])

            career_en = response.xpath(
                "//h3[contains(text(),'Employability & Careers')]/following-sibling::div[1]").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            if item['career_en'] != "":
                item['career_en'] = "<h3>Employability & Careers</h3>" + item['career_en']
            # print("item['career_en']: ", item['career_en'])

            rntry_requirements = response.xpath(
                "//h3[contains(text(),'Entry Requirements & How to Apply')]/following-sibling::div[1]//strong[contains(text(),'How to Apply:')]/../preceding-sibling::*//text()|//div[@id='ui-accordion-accordion-panel-1']//text()").extract()
            if len(rntry_requirements) == 0:
                rntry_requirements = response.xpath(
                    "//h3[contains(text(),'Entry Requirements​')]/following-sibling::div[1]//text()").extract()
                if len(rntry_requirements) == 0:
                    rntry_requirements = response.xpath(
                        "//h3[contains(text(),'Entry Requirements & How to Apply')]/following-sibling::div[1]//text()").extract()
            item['rntry_requirements'] = clear_lianxu_space(rntry_requirements)
            if item['rntry_requirements'] != "":
                item['rntry_requirements'] = "Entry Requirements " + item['rntry_requirements'].strip()
            # print("item['rntry_requirements']: ", item['rntry_requirements'])


            ielts = re.findall(r"IELTS.{1,80}", item['rntry_requirements'])
            clear_space(ielts)
            # print("ielts: ", ielts)
            if len(ielts) > 0:
                item['ielts_desc'] = ielts[0]
            # print("item['ielts_desc']: ", item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            # if len(ielts_list) == 1:
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            apply_proces_en = ["""<p style="text-align: center;"> 
      <strong><span style="color: #d44831;">Application Stages</span>  </strong></p>
   <p> 
      <strong>1. </strong>Choose<strong> programme of study</strong><strong>.</strong></p>
   <p> 
      <strong>2.</strong>&#160;Check if the programme has a 
      <strong>specific deadline for applications</strong>.</p>
   <p> 
      <strong>3.</strong>&#160;It is <strong>essential</strong> that&#160;you check the 
      <strong>Compulsory Supporting Documents</strong>. Some programmes require specific information e.g. a Personal Statement template and/or additional information.</p>
   <p> 
      <strong>4.</strong> If applying for 
      <strong>RPL</strong> please see information under <em>Make an Online Application</em>.</p>
   <p> 
      <strong>5.</strong> Make 
      online application, ensuring <strong>all </strong><strong>required documents are uploaded</strong>.</p>
   <p> 
      <strong>6.</strong> Applications can take 
      <strong>2-4 weeks </strong>for&#160;consideration.</p> 
   <p> 
      <strong>7. </strong>If required you will be invited for<strong>&#160;interview</strong>.&#160;</p>
   <p> 
      <strong>8.</strong>&#160;If successful, o<span style="font-size: 12.825px; background-color: #f0eded;">fficial 
         <strong>offer letter</strong>&#160;will be&#160;provided by Admissions.</span></p>
   <p><strong>9.</strong>&#160;<strong>Accept&#160;place on programme.</strong>&#160;</p><p><strong>10.</strong>&#160;<span style="font-size: 12.825px; background-color: #f0eded;">Once any conditions have been met (if applicable)&#160;you will be provided&#160;with <strong>joining and&#160;</strong></span><span style="font-size: 12.825px; background-color: #f0eded;"><strong>enrolment&#160;</strong></span><span style="font-size: 12.825px; background-color: #f0eded;"><strong>information </strong>a month prior&#160;to programme&#160;commencement. <strong>It is essential that you accept your place to enable you to receive your joining information (status&#160;Unconditional Firm).</strong></span></p>
"""]
            item['apply_proces_en'] = remove_class(clear_lianxu_space(apply_proces_en)).strip()
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            interview_desc_en = response.xpath(
                "//*[contains(text(),'interview')]").extract()
            item['interview_desc_en'] = remove_class(clear_lianxu_space(interview_desc_en)).strip()
            # print("item['interview_desc_en']: ", item['interview_desc_en'])

            # http://www.cardiffmet.ac.uk/study/finance/Documents/2018-2019-Fee-Tables.pdf
            item['tuition_fee'] = '13000'
            if "mba" in item['programme_en'].lower():
                item['tuition_fee'] = '13500'
            item['tuition_fee_pre'] = "£"

            item['require_chinese_en'] = remove_class(clear_lianxu_space(["<h4>Postgraduate Courses</h4><p>Students with a Bachelor degree from a recognised institution in China or UK. </p><p>OR students with a Masters degree from a recognised institution in China</p>"]))
            yield item
        except Exception as e:
            with open(item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

