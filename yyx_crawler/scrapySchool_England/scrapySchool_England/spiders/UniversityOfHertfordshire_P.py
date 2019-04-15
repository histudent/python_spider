# -*- coding: utf-8 -*-
import scrapy, requests
from lxml import etree
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
import json

class UniversityOfHertfordshire_PSpider(scrapy.Spider):
    name = "UniversityOfHertfordshire_P"
    # allowed_domains = ["herts.ac.uk", "funnelback.co.uk"]
    # start_urls = ["https://www.herts.ac.uk/courses/postgraduate?collection=herts-courses&query=!nullsearch&start_rank=1&sort=relevance&f.Course%20Type|T=Postgraduate&f.Method%20of%20Study|S=Full%20Time&f.International%20Course|I=1"]
    start_urls = ["https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=1&query=!nullsearch&f.Course%20Type|T=Postgraduate&f.Method%20of%20Study|S=Full%20Time&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=11&query=!nullsearch&f.Course%20Type|T=Postgraduate&f.Method%20of%20Study|S=Full%20Time&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=21&query=!nullsearch&f.Course%20Type|T=Postgraduate&f.Method%20of%20Study|S=Full%20Time&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=31&query=!nullsearch&f.Course%20Type|T=Postgraduate&f.Method%20of%20Study|S=Full%20Time&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=41&query=!nullsearch&f.Course%20Type|T=Postgraduate&f.Method%20of%20Study|S=Full%20Time&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=51&query=!nullsearch&f.Course%20Type|T=Postgraduate&f.Method%20of%20Study|S=Full%20Time&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=61&query=!nullsearch&f.Course%20Type|T=Postgraduate&f.Method%20of%20Study|S=Full%20Time&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=71&query=!nullsearch&f.Course%20Type|T=Postgraduate&f.Method%20of%20Study|S=Full%20Time&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=81&query=!nullsearch&f.Course%20Type|T=Postgraduate&f.Method%20of%20Study|S=Full%20Time&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=91&query=!nullsearch&f.Course%20Type|T=Postgraduate&f.Method%20of%20Study|S=Full%20Time&f.International%20Course|I=1&sort=relevance", ]
    # rules = (
    #     # Rule(LinkExtractor(restrict_xpaths=r"//a[@class='color-btn next-arr arrow']"), follow=True, callback='page_url'),
    #     Rule(LinkExtractor(restrict_xpaths=r"//p[@class='pagination']/a"), follow=True,
    #          callback='page_url'),
    # )

    def parse(self, response):
        # print("======", response.url)
        # links = response.xpath("//ul[@id='course-listing']/li/div[@class='course-content']/div[@class='headline']/a/@href").extract()
        # print(len(links))
        # links = list(set(links))
        # print(len(links))
        # for url in links:
        #     yield scrapy.Request(url, callback=self.parse_data)
        url_dict = json.loads(response.text)
        links = url_dict.get('response').get('resultPacket').get('results')
        # print(links)
        # print(len(links))
        # links = list(set(links))
        # print(len(links))
        programme_dict = {}
        for link in links:
            programme_dict[link.get('liveUrl')] = link.get('title')

        for link in links:
            url = link.get('liveUrl')
            yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "http://www.herts.ac.uk/"
        item['university'] = "University of Hertfordshire"
        item['url'] = response.url
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        print("===========================")
        print(response.url)
        try:
            # //div[@id='content']/main/div[@class='course-sub-head']/a
            department = response.xpath("//div[@id='content']/main/div[@class='course-sub-head']/a//text()|//div[@class='banner__caption banner__caption--below']//text()").extract()
            department = ''.join(department).replace("in the ", "").strip()
            item['department'] = department
            print("department: ", department)

            # 专业、学位类型 //div[@id='content']/main/h1
            programmeDegreetype = response.xpath("//div[@id='content']/main/h1//text()|//span[@class='color--red']/..//text()").extract()
            # print("programmeDegreetype: ", programmeDegreetype)
            programmeDegreetypeStr = ''.join(programmeDegreetype).strip()
            # print("programmeDegreetypeStr: ", programmeDegreetypeStr)
            degreetype = re.findall(r"^\w+\s", programmeDegreetypeStr)
            # print(degreetype)
            if len(degreetype) != 0:
                degreetype = ''.join(list(degreetype[0])).strip()
                # print(degreetype)
                item['degree_name'] = degreetype
            print("item['degree_name']: ", item['degree_name'])
            programme = programmeDegreetypeStr.replace(''.join(degreetype), '')
            # print(programme)
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en']: ", item['programme_en'])


            duration = response.xpath(
                "//h3[contains(text(),'Key course information')]/following-sibling::ul//*[contains(text(), 'Full')]//text()|"
                "//h4[contains(text(),'Course length')]/following-sibling::div[1]//text()").extract()
            clear_space(duration)
            # print("duration: ", duration)
            duration_str = ''.join(duration)

            item['teach_time'] = getTeachTime(duration_str)
            duration_list = getIntDuration(duration_str)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['teach_time'] = ", item['teach_time'])
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            location = response.xpath(
                "//h3[contains(text(),'Key course information')]/following-sibling::ul//*[contains(text(), 'Locations')]/../../following-sibling::*//text()|"
                "//h4[contains(text(),'Locations')]/following-sibling::div[1]//text()").extract()
            clear_space(location)
            item['location'] = ''.join(location).strip()
            # print("item['location'] = ", item['location'])

            # //div[@id='overview']
            overview = response.xpath("//div[@id='overview']|//section[@data-section='section-overview']").extract()
            overview_en = remove_class(clear_lianxu_space(overview))
            # print("overview_en: ", overview_en)
            # overview_en_re = re.findall(r"<script>.*?</script>", overview_en)
            # print(overview_en_re)
            # if len(overview_en_re) > 0:
            #     for o in overview_en_re:
            #         item['overview_en'] = overview_en.replace(o, "")
            # else:
            item['overview_en'] = overview_en
            # print("item['overview_en']: ", item['overview_en'])

            assessment_en = response.xpath("//h3[contains(text(),'Teaching methods')]/following-sibling::*").extract()
            if len(assessment_en) == 0:
                assessment_en = response.xpath(
                    "//h3[contains(text(),'Teaching methods')]/..").extract()
            if len(assessment_en) > 0:
                item['assessment_en'] = "<h3>Teaching methods</h3>" + remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            career_en = response.xpath("//h3[contains(text(),'Teaching methods')]/preceding-sibling::*").extract()
            if len(career_en) == 0:
                career_en = response.xpath(
                    "//h3[contains(text(),'Careers')]|//h3[contains(text(),'Careers')]/following-sibling::*").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            # print("item['career_en']: ", item['career_en'])

            modules = response.xpath("//div[@id='modules']|//div[@id='module-structure']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])

            # //div[@id='fees']
            feeContent = response.xpath("//h4[contains(text(),'International Students')]/following-sibling::h5[contains(text(), 'Full')]/following-sibling::ul[1]//text()").extract()
            clear_space(feeContent)
            # print("feeContent: ", feeContent)
            feelist = re.findall(r"£[\d,]+", ''.join(feeContent))
            if len(feelist) > 0:
                item['tuition_fee'] = int(feelist[0].replace('£', '').replace(',', '').strip())
                item['tuition_fee_pre'] = '£'
            # print("item['tuition_fee']: ", item['tuition_fee'])
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            # //div[@id='how-to-apply']
            entry_requirements = response.xpath("//h2[contains(text(),'How to apply')]/preceding-sibling::*//text()").extract()
            item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            # print("entry_requirementsStr: ", entry_requirementsStr)
            ielts = re.findall(r"IELT[\sa-zA-Z]*\d\.?\d?[\sa-z\(\)]*\d\.?\d?[\sa-z\(\)]{1,100}", item['rntry_requirements'])
            # print("ielts: ", ielts)
            item['ielts_desc'] = ''.join(ielts).strip()
            # print("item['ielts_desc']: ", item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            start_date = response.xpath(
                "//div[@class='how-to-apply-table']//table//td[contains(text(),'Full')]/preceding-sibling::*[2]//text()").extract()
            clear_space(start_date)
            print("start_date: ", start_date)
            start_date = list(set(start_date))
            item['start_date'] = ','.join(start_date).strip()
            print("item['start_date'] = ", item['start_date'])

            item["require_chinese_en"] = "<p>Chinese 4-year Bachelor degree with 70% or above</p>"
            item["apply_proces_en"] = "https://www.herts.ac.uk/study/how-to-apply"
            yield item
        except Exception as e:
            with open(item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    # def parse_data(self, response):
    #     # item = get_item1(HertsBenSchoolItem)
    #     # item['university'] = "University of Hertfordshire"
    #     # item['url'] = response.url
    #     print("===========================")
    #     print(response.url)
    #     # try:
        #     # 专业、学位类型 //div[@id='content']/main/h1
        #     programmeDegreetype = response.xpath("//div[@id='content']/main/h1//text()").extract()
        #     print("programmeDegreetype: ", programmeDegreetype)
        #
        #     # item['programme'] = ''.join(programme)
        #     # print("item['programme']: ", item['programme'])
        #
        #     yield item
        # except Exception as e:
        #     with open("./error/hertsBenSchoolerror.txt", 'a+', encoding="utf-8") as f:
        #         f.write(str(e) + "\n" + response.url + "\n========================")
        #     print("异常：", str(e))
        #     print("报错url：", response.url)

