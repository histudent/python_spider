import scrapy
import re
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space, clear_space_str
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.getIELTS import get_ielts
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime
import requests
from lxml import etree

class UniversityOfSurrey_USpider(scrapy.Spider):
    name = "UniversityOfSurrey_U"
    start_urls = ["https://www.surrey.ac.uk/undergraduate"]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3472.3 Safari/537.36"}

    def parse(self, response):
        links = response.xpath("//div[@class='view-content']/div//a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))
        for link in links:
            url = "https://www.surrey.ac.uk" + link
            # print(url)
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        item['university'] = "University of Surrey"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        item['location'] = '01SE01, Senate House, University of Surrey, Guildford, Surrey GU2 7XH'
        # print("item['location'] = ", item['location'])
        print("===============================")
        print(response.url)
        try:
            overview = response.xpath(
                "//h3[contains(text(),'Course facts')]/../preceding-sibling::*").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en'] = ", item['overview_en'])

            career = response.xpath("//h2[contains(text(),'Careers')]/preceding-sibling::*[1]/following-sibling::*[position()<last()-3]").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # if item['career_en'] == "":
            #     print("***career_en")
            # print("item['career_en'] = ", item['career_en'])

            modules = response.xpath("//div[@class='module-list']/following-sibling::*[1]/preceding-sibling::*").extract()
            # modules1 = response.xpath("//div[@id='modules-ft']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # if item['modules_en'] == "":
            #     print("***modules_en")
            # print("item['modules_en'] = ", item['modules_en'])

            assessment_en = response.xpath(
                "//h2[contains(text(),'Teaching')]/preceding-sibling::*[1]/following-sibling::*[position()<7]|"
                "//h2[contains(text(),'Assessment')]/preceding-sibling::*[1]/following-sibling::*[position()<3]").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # if item['assessment_en'] == "":
            #     print("***assessment_en")
            # print("item['assessment_en'] = ", item['assessment_en'])

            # //a[contains(text(), 'Faculty of')]|//a[contains(text(), 'School of')]
            department = response.xpath(
                "//a[contains(text(), 'Faculty of')]//text()|"
                "//a[contains(text(), 'School of')]//text()").extract()
            item['department'] = remove_class(clear_lianxu_space(department)).replace("academic staff in the", "").strip()
            # if item['department'] == "":
            #     print("***department")
            # print("item['department'] = ", item['department'])

            entry_requirements = response.xpath("//div[@id='entry-collapse']").extract()
            item['apply_desc_en'] = remove_class(clear_lianxu_space(entry_requirements))
            # print("item['apply_desc_en'] = ", item['apply_desc_en'])

            alevel = response.xpath("//h3[contains(text(),'A-level')]/following-sibling::*[1]//text()").extract()
            alevel_str = ''.join(alevel).strip()
            if alevel_str == "Overall:" or alevel_str == "Overall":
                alevel = response.xpath("//h3[contains(text(),'A-level')]/following-sibling::*[position()<4]//text()").extract()
                alevel_str = ''.join(alevel).replace("Overall", "").strip().strip(":").strip()
                # print("***alevel")
            item['alevel'] = clear_space_str(alevel_str)
            # print("item['alevel'] = ", item['alevel'])

            ib = response.xpath("//h3[contains(text(),'International Baccalaureate')]/following-sibling::*[1]//text()").extract()
            ib_str = ''.join(ib).strip()
            if ib_str == "Overall:":
                ib = response.xpath("//h3[contains(text(),'International Baccalaureate')]/following-sibling::*[2]//text()").extract()
                ib_str = ''.join(ib).strip()
                # print("***ib")
            item['ib'] = ib_str
            # print("item['ib'] = ", item['ib'])

            ielts_str = response.xpath("//div[@id='entry-collapse']//h2[contains(text(),'English')]/following-sibling::p[position()<4]//text()").extract()
            ielts_re = re.findall(r"^IELTS.{1,80}", ''.join(ielts_str))
            item['ielts_desc'] = ''.join(ielts_re).strip()
            # print("item['ielts_desc'] = ", item['ielts_desc'])

            ieltsDict = get_ielts(item['ielts_desc'])
            item['ielts'] = ieltsDict.get("IELTS")
            item['ielts_l'] = ieltsDict.get("IELTS_L")
            item['ielts_s'] = ieltsDict.get("IELTS_S")
            item['ielts_r'] = ieltsDict.get("IELTS_R")
            item['ielts_w'] = ieltsDict.get("IELTS_W")
            # print("item['IELTS'] = %sitem['IELTS_L'] = %sitem['IELTS_S'] = %sitem['IELTS_R'] = %sitem['IELTS_W'] = %s==" % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            application_open_date = response.xpath(
                "//div[@class='p-3 p-xl-4 text-center text-light']//text()").extract()
            clear_space(application_open_date)
            # print("application_open_date: ", ''.join(application_open_date))
            item['application_open_date'] = getStartDate(''.join(application_open_date))
            # if item['application_open_date'] == "":
            #     print("***application_open_date")
            # print("item['application_open_date'] = ", item['application_open_date'])

            tuition_fee = response.xpath("//div[@id='fees']//tbody//tr[1]/td[last()-1]//text()").extract()
            # print("tuition_fee: ", tuition_fee)
            if len(tuition_fee) > 0:
                item['tuition_fee'] = getTuition_fee(''.join(tuition_fee))

            if item['tuition_fee'] == 0:
                item['tuition_fee'] = None
            else:
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee'] = ", item['tuition_fee'])
            print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])

            item['apply_proces_en'] = remove_class(clear_lianxu_space([""" <h2>Process</h2>
<ol><li>Choose the programmes you want to study. Still undecided? Search our <a href="/undergraduate">undergraduate degrees</a></li>
<li>Find out <a href="/apply/undergraduate/how-to-apply-through-ucas">how to apply through UCAS</a></li>
<li>Wait for universities to make their decisions, <a href="/apply/undergraduate/after-you-apply">learn what happens after you apply</a></li>
<li>Reply to your <a href="/apply/undergraduate/your-offer">university offers</a></li>
<li><a href="/apply/undergraduate/your-offer">Confirm your university place</a></li>
</ol>"""]))
            # print("item['apply_proces_en'] = ", item['apply_proces_en'])

            # https://www.surrey.ac.uk/china/entry-requirements
            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<h2>Undergraduate</h2>
<p>We do not accept the Chinese National University Entrance Examination. However, you can apply to study for an <a href="http://isc.surrey.ac.uk/programmes/international-foundation-year?ch=uniweb&amp;cc=uniweb&amp;cid=uniweb&amp;utm_source=signposting&amp;utm_medium=signposting&amp;utm_campaign=uniweb&amp;_ga=2.246594701.825790074.1509959240-87246970.1500115796">International Foundation Year</a> at our <a href="http://isc.surrey.ac.uk/">International Study Centre</a>, which will prepare you for a full undergraduate degree course.</p>"""]))

            # 专业、学位类型
            programme_en = response.xpath("//h1[@class='text-center my-0']//text()").extract()
            programme_en_str = (''.join(programme_en).split("–"))[0].strip()
            print(programme_en_str)

            if "2019" in ''.join(programme_en):
                item['start_date'] = '2019'
            # print("item['start_date'] = ", item['start_date'])

            # 判断可以拆分几条数据，ucascode、duration、degree_name
            is_degree_name = response.xpath("//tbody[@class='w-100']/tr").extract()
            # print("is_degree_name: ", is_degree_name)
            print(len(is_degree_name))
            for i in range(len(is_degree_name)):
                print("****************"+str(i+1)+"***************")
                degree_name_re = re.findall(r"\w+\s\(Hons\).*|\w+$", programme_en_str)
                if len(degree_name_re) > 0:
                    item['degree_name'] = ''.join(degree_name_re).strip()
                    item['programme_en'] = programme_en_str.replace(item['degree_name'], '').strip()
                else:
                    item['programme_en'] = programme_en_str
                print("item['programme_en'] = ", item['programme_en'])

                degree_name_xpath = response.xpath("//tbody[@class='w-100']//tr["+str(i+1)+"]/td[1]//text()").extract()
                clear_space(degree_name_xpath)
                item['degree_name'] = ''.join(degree_name_xpath).strip()
                print("item['degree_name'] = ", item['degree_name'])

                duration = response.xpath("//tbody[@class='w-100']//tr["+str(i+1)+"]/td[2]//text()").extract()
                clear_space(duration)
                # print("duration: ", duration)
                if len(duration) != 0:
                    duration_list = getIntDuration(''.join(duration))
                    # print("duration_list: ", duration_list)
                    if len(duration_list) == 2:
                        item['duration'] = duration_list[0]
                        item['duration_per'] = duration_list[-1]
                print("item['duration'] = ", item['duration'])
                print("item['duration_per'] = ", item['duration_per'])

                ucascode = response.xpath(
                    "//tbody[@class='w-100']//tr["+str(i+1)+"]/td[4]//text()").extract()
                clear_space(ucascode)
                item['ucascode'] = ''.join(ucascode).strip()
                print("item['ucascode']: ", item['ucascode'])

                tick = response.xpath(
                    "//tbody[@class='w-100']//tr[" + str(i + 1) + "]/td[3]//i[@class='icon icon-tick']").extract()
                clear_space(tick)
                print("tick: ", tick)
                print(len(tick))
                if len(tick) == 1:
                    item['other'] = 'Professional Training'
                print("item['other']: ", item['other'])
                yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_apply_proces_en(self, how_to_apply_url):
        data = requests.get(how_to_apply_url, headers=self.headers)
        response = etree.HTML(data.text)
        # print(response)
        apply_proces_en = response.xpath("//div[@class='layout-row intro summary']")
        # 将Element转换成HTML格式
        apply = ""
        if len(apply_proces_en) > 0:
            apply = etree.tostring(apply_proces_en[0], encoding='unicode', pretty_print=False, method='html')
        else:
            apply = how_to_apply_url
        apply = remove_class(clear_space_str(apply))
        return apply

