# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration
import requests
from w3lib.html import remove_tags
import json

class NewcastleUniversity_USpider(scrapy.Spider):
    name = "NewcastleUniversity_U"
    start_urls = ["https://www.ncl.ac.uk/undergraduate/degrees/#a-z"]


    def parse(self, response):
        links = response.xpath("//ol//li/a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))
        for link in links:
            url = "https://www.ncl.ac.uk" + link
            # url = "https://www.ncl.ac.uk/postgraduate/courses/degrees/business-humanities-presessional-grad-dip-ipc/"
            yield scrapy.Request(url, callback=self.parse_data)


    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "Newcastle University"
        # item['country'] = 'England'
        # item['website'] = 'http://www.ncl.ac.uk/'
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        item['location'] = "Newcastle University, NE1 7RU, United Kingdom"
        print("===========================")
        print(response.url)
        try:
            # 专业
            programmeDegree_type = response.xpath(
                "//header[@class='pageTitle']/h1//text()").extract()
            clear_space(programmeDegree_type)
            programmeDegree_type = ''.join(programmeDegree_type).strip()
            print("programmeDegree_type: ", programmeDegree_type)

            # degree_typeList = re.findall(r"\w+\sHonours$|\w+\sHonours.*", programmeDegree_type)
            degree_name = response.xpath("//strong[contains(text(),'Degree Awarded')]/../text()").extract()
            item['degree_name'] = ''.join(degree_name).strip()
            print("item['degree_name']: ", item['degree_name'])

            item['programme_en'] = programmeDegree_type.replace(item['degree_name'], "").strip()
            print("item['programme_en']: ", item['programme_en'])

            ucascode = response.xpath("//strong[contains(text(),'UCAS Code')]/../text()").extract()
            item['ucascode'] = ''.join(ucascode).strip()
            # print("item['ucascode']: ", item['ucascode'])

            durationMode = response.xpath(
                "//strong[contains(text(),'Course Duration')]/../text()").extract()
            if len(durationMode) == 0:
                durationMode = response.xpath(
                    "//p[@class='duration summary']/text()").extract()
            clear_space(durationMode)
            # print("durationMode: ", durationMode)
            duration_list = getIntDuration(''.join(durationMode))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration']: ", item['duration'])
            # print("item['duration_per']: ", item['duration_per'])

            alevel_ib = response.xpath(
                "//strong[contains(text(),'Entry Requirements')]/../text()").extract()
            clear_space(alevel_ib)
            # print("alevel_ib: ", alevel_ib)
            if len(alevel_ib)==2:
                item['alevel'] = alevel_ib[0]
                item['ib'] = alevel_ib[-1]
            # if item['alevel'] == "":
            #     print("alevel 为空")
            # print("item['alevel']: ", item['alevel'])
            # if item['ib'] == "":
            #     print("ib 为空")
            # print("item['ib']: ", item['ib'])

            # //html//div[@class='contentSeparator textEditorArea expandable']//p[1]/a
            department = response.xpath(
                "//html//div[@class='contentSeparator textEditorArea expandable']//p[1]/a//text()").extract()
            if len(department) == 0:
                department = response.xpath("//*[contains(text(), 'School of')]/text()|//*[contains(text(), 'Faculty of')]/text()").extract()
            # print(department)
            department_str = ';'.join(department).strip()
            # print(department_str)
            dep = re.findall(r"School\sof[a-zA-Z\s,]+|Faculty\sof[a-zA-Z\s,]+", department_str)
            # print("dep: ", dep)
            if len(dep) > 0:
                for d in dep:
                    if "Faculty" in d:
                        item['department'] = d.replace("Graduate School", "").strip()
                        # print("长度1： ", len(item['department']))
                        if len(item['department']) > 55:
                            continue
                        else:
                            break
                    else:
                        item['department'] = dep[0]
                        # print("长度： ", len(item['department']))
                        if len(item['department']) > 55:
                            item['department'] = dep[-1]
            # print("item['department']: ", item['department'])


            # 页面全部内容
            allcontent = response.xpath(
                "//main[@id='content']//article//text()").extract()
            # clear_space(allcontent)
            # print("allcontent：", allcontent)

            department = re.findall(r"Newcastle\sUniversity\sBusiness\sSchool", ''.join(allcontent))
            # print("department: ", department)
            if len(department) > 0 and item['department'] == "":
                item['department'] = department[0]
            # print("==item['department']: ", item['department'])


            # //h3[contains(text(),'Highlights of this degree')]/../preceding-sibling::*[1]
            overview_en = response.xpath("//h3[contains(text(),'Highlights of this degree')]/../preceding-sibling::*[@class='contentSeparator containAsides textEditorArea'][1]|"
                                         "//h3[contains(text(),'Highlights of this degree')]/../following-sibling::*[@class='contentSeparator containAsides textEditorArea'][1]").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
            # if item['overview_en'] == "":
            #     print("overview_en 为空")
            # print("item['overview_en']: ", item['overview_en'])

            # //h3[contains(text(),'Teaching and assessment')]/../../preceding-sibling::*
            modules_en = response.xpath("//h3[contains(text(),'Teaching and assessment')]/../../preceding-sibling::*[position()<10]").extract()
            if len(modules_en) == 0:
                modules_en = response.xpath(
                    "//h2[contains(text(),'Course Details')]/../preceding-sibling::*[1]/following-sibling::*[position()<10]").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules_en))
            rem_modules = re.findall(r"<div><h3>Related Degrees.*|<div>Next step:.*|<div><h3>Compare this course.*|<figure><iframe allowfullscreen></iframe></figure>", item['modules_en'])
            if len(rem_modules) > 0:
                for m in rem_modules:
                    item['modules_en'] = item['modules_en'].replace(m, '').strip()
            item['modules_en'] = item['modules_en'].replace("<div></div>", "").strip()
            item['modules_en'] = ''.join(item['modules_en'].split('\n')).strip()
            # if item['modules_en'] == "":
            #     print("modules_en 为空")
            # print("item['modules_en']: ", item['modules_en'])

            assessment_en = response.xpath(
                "//h3[contains(text(),'Teaching and assessment')]/../..").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # if item['assessment_en'] == "":
                # print("assessment_en 为空")
            # print("item['assessment_en']: ", item['assessment_en'])

            apply_desc_en = response.xpath(
                "//h2[contains(text(),'Entry Requirements')]/../preceding-sibling::*[1]/following-sibling::*[position()<20]").extract()
            item['apply_desc_en'] = ''.join(remove_class(clear_lianxu_space(apply_desc_en)).split('\n')).strip()
            # if item['apply_desc_en'] == "":
            #     print("apply_desc_en 为空")
            # print("item['apply_desc_en']: ", item['apply_desc_en'])

            portfolio_desc_en = response.xpath(
                "//h3[contains(text(),'Portfolio requirements')]/../..").extract()
            item['portfolio_desc_en'] = remove_class(clear_lianxu_space(portfolio_desc_en))
            # if item['portfolio_desc_en'] == "":
            #     print("portfolio_desc_en 为空")
            # print("item['portfolio_desc_en']: ", item['portfolio_desc_en'])


            # //h3[contains(text(),'English')]/../..//*[contains(text(),'IELT')]
            ielts_desc = response.xpath("//h3[contains(text(),'English')]/../..//*[contains(text(),'IELT')]/text()").extract()
            clear_space(ielts_desc)
            if len(ielts_desc) > 0:
                item['ielts_desc'] = ielts_desc[0].strip()
            # print("item['ielts_desc']: ", item['ielts_desc'])

            ielts_list = re.findall(r"\d[\d\.]{0,2}", item['ielts_desc'])
            # print(ielts_list)
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
            elif len(ielts_list) > 3:
                item['ielts'] = ielts_list[0]
                item['ielts_l'] = ielts_list[1]
                item['ielts_s'] = ielts_list[1]
                item['ielts_r'] = ielts_list[1]
                item['ielts_w'] = ielts_list[1]
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))


            career_en = response.xpath("//h2[contains(text(),'Careers')]/..").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            if item['career_en'] == "<div><h2>Careers</h2><div></div></div>":
                item['career_en'] = remove_class(clear_lianxu_space(response.xpath("//h2[contains(text(),'Careers')]/../preceding-sibling::*[1]/following-sibling::*[position()<4]").extract()))
            # if item['career_en'] == "":
            #     print("career_en 为空")
            # print("item['career_en']: ", item['career_en'])


            tuition_fee = response.xpath("//h3[contains(text(),'Tuition Fees (International students)')]/../..//text()").extract()
            if len(tuition_fee) == 0:
                tuition_fee = response.xpath(
                    "//p[contains(text(),'September 2018 start (4 terms) ')]//text()").extract()
            clear_space(tuition_fee)
            # print("tuition_fee: ", tuition_fee)
            item['tuition_fee'] = getTuition_fee(''.join(tuition_fee))
            if item['tuition_fee'] == 0:
                item['tuition_fee'] = None
            else:
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee']: ", item['tuition_fee'])
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            # //h2[contains(text(),'Apply')]/../following-sibling::*
            apply_proces_en = response.xpath(
                "//h2[contains(text(),'Apply')]/../preceding-sibling::*[1]/following-sibling::*").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(apply_proces_en))
            if item['apply_proces_en'] == "":
                print("apply_proces_en 为空")
            print("item['apply_proces_en']: ", item['apply_proces_en'])


            # chinese_requirements
            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<div class="contentSeparator textEditorArea expandable collapsed"><a href="javascript:void(0)" class="toggle-wrapper" name="d.en.666526" data-widget-type="expandable"><h4 class="expandable-is-set">Undergraduate entry requirements</h4><span href="javascript:void(0)" class="toggle expandable-is-set">Undergraduate entry requirements</span></a>
  <div class="answer">
  
  <figure class="widget-aux right"></figure>
    
  <p>Typically we recognise a <strong>70% - 75% average</strong> in <strong>one year of Bachelor degree</strong> study at <strong>Project 211</strong> and <strong>Netbig Top 150</strong><a href="http://rank2011.netbig.com/en/%20"> </a><strong>institutions</strong>&nbsp;and a <strong>75% - 80% average</strong> at <strong>other institutions</strong>&nbsp;as comparable to ABB at A level.</p>
<p>You may be considered for first year entry with a&nbsp;<strong>pass</strong> from a <strong>university foundation programme in China </strong>at a <strong>recognised institution with</strong><em>&nbsp;</em>at least an<strong> 80% average and 80% in relevant subjects</strong>.</p>
<p>We know that different institutions use different grading scales. These may vary from our stated entry requirements. Please <strong>include the institution&rsquo;s marking scale</strong> if it is not stated on your transcript.</p>
<p>Please check course specific&nbsp;<strong>entry requirements</strong>&nbsp;for&nbsp;<a href="/undergraduate/degrees/">undergraduate degrees</a>&nbsp;as they do&nbsp;<strong>vary across courses</strong>, with ABB typically the minimum required.</p>
<p>On our course pages, you can also find out <a href="/undergraduate/apply/">how to apply</a>.</p>
  
  </div>
</div>"""]))
            # print("item['require_chinese_en']: ", item['require_chinese_en'])


            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)
