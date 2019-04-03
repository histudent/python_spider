# -*- coding: utf-8 -*-
import scrapy, requests
from lxml import etree
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re, json
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getDuration import getIntDuration, getTeachTime

class HeriotWattUniversity_USpider(CrawlSpider):
    name = "HeriotWattUniversity_U"
    # allowed_domains = ["herts.ac.uk", "funnelback.co.uk"]
    start_urls = ["https://search.hw.ac.uk/s/search.html?collection=courses&f.Locations|location=United%20Kingdom&f.Study%20level|level=Undergraduate&f.Delivery%7Cdelivery=Full-time&start_rank=1"]

    rules = (
        Rule(LinkExtractor(allow=r"start_rank=\d+"), follow=True, callback='page'),
        Rule(LinkExtractor(restrict_xpaths=r"//div[@id='search-results']/div/a"), follow=True, callback='parse_data'),
    )
    # def page(self, response):
    #     print(response.url)

    # def page_url(self, response):
    #     # print("======", response.url)
    #     url_dict = json.loads(response.text)
    #     links = url_dict.get('response').get('resultPacket').get('results')
    #     # print(links)
    #     # print(len(links))
    #     # links = list(set(links))
    #     # print(len(links))
    #     programme_dict = {}
    #     for link in links:
    #         programme_dict[link.get('liveUrl')] = link.get('title')
    #
    #     for link in links:
    #         url = link.get('liveUrl')
    #         yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "http://www.herts.ac.uk/"
        item['university'] = "Heriot-Watt University"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        # item['major_type1'] = response.meta.get(response.url)
        # print("item['major_type1']: ", item['major_type1'])
        try:
            department = response.xpath("//div[@class='banner__caption banner__caption--below']//text()").extract()
            department = ''.join(department).replace("in the ", "").strip()
            item['department'] = department
            # print("item['department']: ", item['department'])

            # 专业、学位类型
            programmedegreenamestr = response.xpath("//div[@class='col-md-12']/h1//text()").extract()
            programmedegreenamestr = clear_lianxu_space(programmedegreenamestr)
            print("programmedegreenamestr: ", programmedegreenamestr)

            if "," in programmedegreenamestr:
                degree_name_programme = programmedegreenamestr.split(",")
                item['degree_name'] = degree_name_programme[-1].replace("(Hons)", "").strip()
                item['programme_en'] = degree_name_programme[0].strip()
            print("item['degree_name']: ", item['degree_name'])
            print("item['programme_en']: ", item['programme_en'])

            # if item['degree_name'] == "":
            #     print("*****111****")

            location = response.xpath(
                "//dt[contains(text(),'Location')]/following-sibling::dd[1]//text()").extract()
            clear_space(location)
            item['location'] = ''.join(location).strip()
            # print("item['location'] = ", item['location'])

            duration = response.xpath(
                "//dt[contains(text(),'Duration')]/following-sibling::dd[1]//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            item['other'] = '; '.join(duration).replace(",;", ":").replace("; ; ;", ";").strip()
            # print("item['other']: ", item['other'])
            duration_str = ''.join(duration)

            duration_list = getIntDuration(duration_str)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            # //div[@id='overview']
            overview = response.xpath("//h3[contains(text(),'Accreditation')]/preceding-sibling::*").extract()
            if len(overview) == 0:
                overview = response.xpath("//h2[contains(text(),'Overview')]/..").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])
            # if item['overview_en'] == "":
            #     print("*****111****")

            modules = response.xpath("//section[@id='course-content']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])

            career_en = response.xpath("//section[@id='career']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            # print("item['career_en']: ", item['career_en'])

            # //div[@id='fees']
            feeContent = response.xpath("//th[contains(text(),'Fee')]/following-sibling::*[last()]//text()").extract()
            clear_space(feeContent)
            # print("feeContent: ", feeContent)
            feelist = re.findall(r"£[\d,]+", ''.join(feeContent))
            if len(feelist) > 0:
                item['tuition_fee'] = int(feelist[0].replace('£', '').replace(',', '').strip())
            # print("item['tuition_fee']: ", item['tuition_fee'])

            alevel = response.xpath("//section[@id='entry-requirements']//ul[1]//strong[contains(text(), 'A-Levels')]/../text()").extract()
            item['alevel'] = clear_lianxu_space(alevel)
            # print("item['alevel']: ", item['alevel'])

            ib = response.xpath("//section[@id='entry-requirements']//ul[1]//strong[contains(text(), 'Int. Baccalaureate')]/../text()").extract()
            item['ib'] = clear_lianxu_space(ib)
            # print("item['ib']: ", item['ib'])

            # //div[@id='how-to-apply']
            entry_requirements = response.xpath("//strong[contains(text(),'English language requirements')]/..//text()").extract()
            rntry_requirements = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            # print("entry_requirementsStr: ", entry_requirementsStr)
            ielts = response.xpath("//strong[contains(text(),'English language requirements')]/..//text()").extract()
            if len(ielts) == 0:
                ielts = response.xpath("//li[contains(text(),'IELTS')]//text()").extract()
            item['ielts_desc'] = ''.join(ielts).strip()
            print("item['ielts_desc']: ", item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                    item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            if item['ielts'] is None:
                if "Interpreting and Translating" in item['programme_en']:
                    item['ielts'] = 7.5
                    item['ielts_l'] = 7.5
                    item['ielts_s'] = 7.5
                    item['ielts_r'] = 7.5
                    item['ielts_w'] = 7.5
                else:
                    item['ielts'] = 6
                    item['ielts_l'] = 6
                    item['ielts_s'] = 6
                    item['ielts_r'] = 6
                    item['ielts_w'] = 6

            ucascode = response.xpath("//h2[contains(text(),'The course')]/following-sibling::*//dt[contains(text(),'UCAS code')]/following-sibling::dd[1]//text()").extract()
            clear_space(ucascode)
            print("ucascode: ", ucascode)
            item['ucascode'] = ''.join(ucascode).strip()
            print("item['ucascode'] = ", item['ucascode'])

            item['apply_proces_en'] = "https://www.hw.ac.uk/study/apply/uk/undergraduate.htm"
            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

