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


class UniversityOfWestLondon_PSpider(scrapy.Spider):
    name = "UniversityOfWestLondon_P"
    start_urls = ["https://www.uwl.ac.uk/courses/all?field_presentation_refs_field_start_date=2&field_study_level_taxonomy%5B%5D=12&field_c_subject=All&field_presentation_refs_field_healthcare_cpd=332&field_presentation_refs_field_location2=All&field_presentation_refs_field_study_mode=Full+time&keys=&study_mode_3=All&items_per_page=10&items_per_page=500"]

    def parse(self, response):
        links = response.xpath("//div[@class='view-content']/div[@class='item-list'][1]/ul/li/div[@class='views-field views-field-field-location2']/div[@class='field-content']/a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))
        for link in links:
            url = "https://www.uwl.ac.uk" + link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.uwl.ac.uk/"
        item['university'] = "University of West London"
        item['url'] = response.url
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        print("===========================")
        print(response.url)
        try:
            programmeDegreetype = response.xpath(
                "//h1[@id='page-title']//text()").extract()
            # print("programmeDegreetype: ", programmeDegreetype)
            programmeDegreetypeStr = ''.join(programmeDegreetype)

            degree_type = re.findall(r"^(\w+\s?/\s?\w+|\w+)\s", programmeDegreetypeStr)
            # print("degree_type: ", degree_type)
            item['degree_name'] = ''.join(degree_type).strip()
            print("item['degree_name']: ", item['degree_name'])

            if item['degree_name'].lower() == "phd":
                item['teach_type'] = 'phd'
                item['degree_type'] = 3
            print("item['teach_type']: ", item['teach_type'])
            print("item['degree_type']: ", item['degree_type'])

            programme = programmeDegreetypeStr.strip(''.join(degree_type))
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en']: ", item['programme_en'])

            mode = response.xpath("//dt[contains(text(), 'Study mode')]/following-sibling::dd[1]//text()").extract()
            clear_space(mode)
            item['teach_time'] = getTeachTime(''.join(mode))
            # print("item['teach_time']: ", item['teach_time'])

            location = response.xpath("//dt[contains(text(), 'Location')]/following-sibling::dd[1]//text()").extract()
            item['location'] = ''.join(location).replace("See location information", "").strip()
            print("item['location']: ", item['location'])

            start_date = response.xpath("//dt[contains(text(), 'Start date')]/following-sibling::dd[1]//text()").extract()
            clear_space(start_date)
            # print("start_date: ", start_date)
            item['start_date'] = getStartDate(''.join(start_date))
            # print("item['start_date']: ", item['start_date'])

            duration = response.xpath("//dt[contains(text(), 'Duration')]/following-sibling::dd[1]//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            department = response.xpath("//dt[contains(text(), 'Department')]/following-sibling::dd[1]//text()").extract()
            item['department'] = ''.join(department).strip()
            print("item['department']: ", item['department'])

            tuition_fee = response.xpath("//h4[contains(text(),'Overseas students')]/following-sibling::dl[1]//dt[contains(text(), 'Main fee')]/following-sibling::dd[1]//text()").extract()
            # print("tuition_fee: ", tuition_fee)
            if len(tuition_fee) > 0:
                item['tuition_fee'] = getTuition_fee(''.join(tuition_fee))
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee']: ", item['tuition_fee'])
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            # //div[@id='course-detail']
            modules = response.xpath("//div[@id='course-detail']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])

            # //div[@id='course-detail']
            entry_requirements = response.xpath("//div[@id='entry-requirements']//text()").extract()
            item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            ielts_desc = response.xpath("//div[@id='entry-requirements']//*[contains(text(),'IELTS')]/text()").extract()
            clear_space(ielts_desc)
            # print("ielts_desc: ", ielts_desc)
            ielts_desc_re = re.findall(r'.{1,50}IELTS.{1,50}', ''.join(ielts_desc))
            # print("ielts_desc_re: ", ielts_desc_re)
            if len(ielts_desc_re) > 0:
                item['ielts_desc'] = ielts_desc_re[-1]
            # print("item['ielts_desc']: ", item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            how_to_apply = response.xpath("//div[@id='how-to-apply']").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(how_to_apply))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            assessment_en = response.xpath("//h3[contains(text(),'Teaching methods')]/preceding-sibling::*[1]/following-sibling::*[position()<5]|"
                                           "//*[contains(text(),'Assessment')]/preceding-sibling::*[1]/following-sibling::*[position()<5]|"
                                           "//html//div/strong[contains(text(),'How will I be taught?')]/..").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            career_en = response.xpath(
                "//div[@id='career-progression-and-study']|"
                "//div[@id='jobs-and-placements']|"
                "//html//*[contains(text(),'Career and study progression')]/../following-sibling::*[position()<5]").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en)).replace("<div></div>","").strip()
            print("item['career_en']: ", item['career_en'])

            overview_en = response.xpath("//div[@id='course-summary']/*[position()<last()]").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
            print("item['overview_en']: ", item['overview_en'])

            item['require_chinese_en'] = """<h3>Postgraduate entry</h3>
<p>Applicants with the followingqualiﬁcationswill be considered for entry on a postgraduate course:</p>
<p>Bachelor's degree from a national university with a GPA 2.6 / 4.0 or an overall average of 65% or higher</p>
<p>Bachelor's degree from a high-ranking private college with an average of 85% or higher</p>
<p>Honours degree from any university in the UK or Republic of Ireland with a minimum of 2:2 or above</p>
<p>To study a PhD: a proposal is required in addition to a Masters qualification in a related subject area.</p>"""
            yield item
        except Exception as e:
            with open(item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

