# -*- coding: utf-8 -*-
import scrapy
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


class SouthamptonSolentUniversity_PSpider(CrawlSpider):
    name = "SouthamptonSolentUniversity_P"
    start_urls = ["https://www.solent.ac.uk/courses?course-level=Postgraduate&p=0&viewType=grid"]

    rules = (
        # Rule(LinkExtractor(restrict_xpaths=r"//a[@class='button button--ghost button--center button--btm view-more-courses']"), follow=True, callback='parse_url1'),
        Rule(LinkExtractor(allow=r"p=\d+"), follow=True, callback='parse_url'),
    )
    def parse_url1(self, response):
        print("====", response.url)

    def parse_url(self, response):
        # print(response.url)
        links = response.xpath("//div[@class='row results']/div[@class='large-4 medium-6 column end']/article[@class='subject subject--grid']/div[@class='subject--grid__info']/h2[@class='subject__title']/a/@href|"
                               "//div[@class='column']/article[@class='subject subject--list']/div[@class='subject--list__info']/div[@class='subject--list__detail']/h2[@class='subject__title subject__title--list']/a[2]/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))
        for link in links:
            url = "https://www.solent.ac.uk" + link
            url = url.replace("year=2018", "year=2019").strip()
            # url = "https://www.solent.ac.uk/courses/postgraduate/athletic-development-and-peak-performance-msc?year=2019"
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "Southampton Solent University"
        item['url'] = response.url
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        print("===========================")
        print(response.url)
        try:
            degree_name = response.xpath("//div[@class='row column']/h1/abbr/text()").extract()
            item['degree_name'] = ''.join(degree_name).strip()
            print("item['degree_name']: ", item['degree_name'])

            programme = response.xpath("//div[@class='row column']/h1/text()").extract()
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en']: ", item['programme_en'])


            # start_date = response.xpath("//dt[contains(text(), 'Start date')]/following-sibling::dd[1]//text()").extract()
            # clear_space(start_date)
            # # print("start_date: ", start_date)
            # item['start_date'] = getStartDate(''.join(start_date))
            # # print("item['start_date']: ", item['start_date'])

            duration = response.xpath("//div[@class='banner__stats']//text()").extract()
            clear_space(duration)
            # print("duration: ", ' '.join(duration))
            duration_list = getIntDuration(' '.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            overview_en = response.xpath("//section[@class='intro intro--courses section']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview_en)).replace("Book an open day", "")
            # print("item['overview_en']: ", item['overview_en'])

            tuition_fee = response.xpath(
                "//html//div[@class='facts-figures__panel panel']/p[contains(text(),'The tuition fees for the 2018/19 academic year are:')]//text()|"
                "//html//div[@class='facts-figures__panel panel']/p[contains(text(),'The tuition fees for the 2018/19 academic year are:')]/following-sibling::p[1]//text()").extract()
            # if len(tuition_fee) == 0:
            #     tuition_fee = response.xpath(
            #         "//html//div[@class='facts-figures__panel panel']/p[contains(text(),'The tuition fees for the 2018/19 academic year are:')]/following-sibling::p[1]//text()").extract()
            clear_space(tuition_fee)
            # print("tuition_fee: ", ''.join(tuition_fee))
            tuition_fee_re = re.findall(r"International\sfull-time\sfees:£\d+,\d+|Internationalfull-timefees:£\d+,\d+|Internationaltotal\scoursefees:£\d+,\d+", ''.join(tuition_fee))
            # print("tuition_fee_re: ", tuition_fee_re)
            item['teach_time'] = getTeachTime(''.join(tuition_fee_re))
            # print("item['teach_time']: ", item['teach_time'])

            tuition_fee_re1 = re.findall(r"\d+,\d+", ''.join(tuition_fee_re))
            if len(tuition_fee_re1) > 0:
                item['tuition_fee'] = getTuition_fee(''.join(tuition_fee_re1))
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee']: ", item['tuition_fee'])
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            entry_requirements = response.xpath("//h3[@class='facts-figures__header'][contains(text(),'Key entry requirements')]/../..//text()").extract()
            item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            ielts_desc = response.xpath("//h3[contains(text(),'English language requirements')]/..//*[contains(text(), 'IELTS')]//text()").extract()
            clear_space(ielts_desc)
            # print("ielts_desc: ", ielts_desc)
            item['ielts_desc'] =''.join(ielts_desc)
            # print("item['ielts_desc']: ", item['ielts_desc'])

            ielts_list = re.findall(r"\d[\d\.]{0,2}", item['ielts_desc'])
            if len(ielts_list) == 1:
                item['ielts'] = ielts_list[0]
                item['ielts_l'] = ielts_list[0]
                item['ielts_s'] = ielts_list[0]
                item['ielts_r'] = ielts_list[0]
                item['ielts_w'] = ielts_list[0]
            elif len(ielts_list) == 2:
                item['ielts'] = ielts_list[0]
                item['ielts_l'] = ielts_list[1]
                item['ielts_s'] = ielts_list[1]
                item['ielts_r'] = ielts_list[1]
                item['ielts_w'] = ielts_list[1]
            elif len(ielts_list) == 3:
                item['ielts'] = ielts_list[0]
                item['ielts_l'] = ielts_list[2]
                item['ielts_s'] = ielts_list[2]
                item['ielts_r'] = ielts_list[2]
                item['ielts_w'] = ielts_list[1]
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            toefl_desc = response.xpath(
                "//h3[contains(text(),'English language requirements')]/..//*[contains(text(), 'TOEFL')]//text()").extract()
            clear_space(toefl_desc)
            # print("ielts_desc: ", ielts_desc)
            item['toefl_desc'] = ''.join(toefl_desc)
            # print("item['toefl_desc']: ", item['toefl_desc'])

            toefl_list = re.findall(r"\d\d+", item['toefl_desc'])
            if len(toefl_list) == 1:
                item['toefl'] = toefl_list[0]
                item['toefl_l'] = toefl_list[0]
                item['toefl_r'] = toefl_list[0]
                item['toefl_s'] = toefl_list[0]
                item['toefl_w'] = toefl_list[0]
            elif len(toefl_list) == 2:
                item['toefl'] = toefl_list[0]
                item['toefl_l'] = toefl_list[1]
                item['toefl_r'] = toefl_list[1]
                item['toefl_s'] = toefl_list[1]
                item['toefl_w'] = toefl_list[1]
            elif len(toefl_list) == 3:
                item['toefl'] = toefl_list[0]
                item['toefl_l'] = toefl_list[2]
                item['toefl_r'] = toefl_list[2]
                item['toefl_s'] = toefl_list[2]
                item['toefl_w'] = toefl_list[1]
            elif len(toefl_list) == 5:
                item['toefl'] = toefl_list[0]
                item['toefl_l'] = toefl_list[1]
                item['toefl_r'] = toefl_list[2]
                item['toefl_s'] = toefl_list[3]
                item['toefl_w'] = toefl_list[4]
            # print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
            #        item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

            assessment_en = response.xpath("//*[contains(text(),'Teaching')]/..|//*[contains(text(),'Assessment')]/..").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            if item['assessment_en'] == "":
                print("***")
            print("item['assessment_en']: ", item['assessment_en'])

            work_experience_desc_en = response.xpath("//*[contains(text(),'Work experience')]/..").extract()
            item['work_experience_desc_en'] = remove_class(clear_lianxu_space(work_experience_desc_en))
            # print("item['work_experience_desc_en']: ", item['work_experience_desc_en'])

            how_to_apply = response.xpath("//h3[@class='subheader']/..").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(how_to_apply))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            location = response.xpath("//h4[contains(text(),'Study location')]/following-sibling::*[1]//text()").extract()
            item['location'] = ''.join(location).strip()
            # print("item['location']: ", item['location'])

            modules = response.xpath("//a[contains(text(),'Programme specification document')]/../../preceding-sibling::*").extract()
            if len(modules) == 0:
                # //h2[contains(text(),'Support')]/../../preceding-sibling::*
                modules = response.xpath(
                    "//h2[contains(text(),'Support')]/../../preceding-sibling::*").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # if item['modules_en'] == "":
            #     print("***")
            # print("item['modules_en']: ", item['modules_en'])

            career_en = response.xpath("//h2[@class='header'][contains(text(),'Industry links')]/..").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            # print("item['career_en']: ", item['career_en'])

            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<h2>Entry requirements</h2>
<p>As a general guide, we look for qualifications that are equivalent to the British high school A-levels. A portfolio is also required for most of our art and design courses.</p>
<p>Students with a good Senior High School Diploma and an IELTS of minimum 5.5 may be eligible for a foundation year (level 0 of a bachelor's degree) or an HND programme.</p>
<p>For postgraduate courses, we look for qualifications that are equivalent to the British&nbsp;bachelor's degree.</p>
"""]))
            # print("item['require_chinese_en']: ", item['require_chinese_en'])

            # department = response.xpath("//dt[contains(text(), 'Department')]/following-sibling::dd[1]//text()").extract()
            # item['department'] = ''.join(department).strip()
            # print("item['department']: ", item['department'])


            yield item
        except Exception as e:
            with open(item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

