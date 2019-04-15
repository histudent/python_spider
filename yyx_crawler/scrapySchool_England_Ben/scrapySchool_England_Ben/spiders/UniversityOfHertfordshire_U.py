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

class UniversityOfHertfordshire_USpider(scrapy.Spider):
    name = "UniversityOfHertfordshire_U"
    # allowed_domains = ["herts.ac.uk", "funnelback.co.uk"]
    start_urls = ["https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=1&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=11&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=21&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=31&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=41&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=51&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=61&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=71&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=81&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=91&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=101&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=111&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=121&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=131&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=141&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance",
"https://herts.funnelback.co.uk/s/search.json?collection=herts-courses&num_ranks=10&start_rank=151&query=!padrenullquery&f.Course%20Type|T=Undergraduate&f.International%20Course|I=1&sort=relevance", ]

    # rules = (
    #     Rule(LinkExtractor(allow=r"start_rank=\d+"), follow=True, callback='page'),
    #     # Rule(LinkExtractor(restrict_xpaths=r"//p[@class='pagination']/a"), follow=True, callback='page_url'),
    # )
    # def page(self, response):
    #     print(response.url)

    def parse(self, response):
        # print("======", response.url)
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
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "http://www.herts.ac.uk/"
        item['university'] = "University of Hertfordshire"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        item['major_type1'] = response.meta.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            department = response.xpath("//div[@class='banner__caption banner__caption--below']//text()").extract()
            department = ''.join(department).replace("in the ", "").strip()
            item['department'] = department
            # print("item['department']: ", item['department'])

            # 专业、学位类型
            degree_name = response.xpath("//span[@class='color--red']/../text()").extract()
            degree_name_str = ''.join(degree_name).strip()
            item['degree_name'] = degree_name_str.replace("(Hons)", "").strip()
            # print("item['degree_name']: ", item['degree_name'])

            programme_en = response.xpath("//span[@class='color--red']//text()|//nav[@class='breadcrumb']//li[contains(text(),'Physics')]//text()").extract()
            item['programme_en'] = ''.join(programme_en).replace(degree_name_str, "").strip()
            # print("item['programme_en']: ", item['programme_en'])

            if "online" not in item['programme_en'].lower():
                if item['degree_name'] == "":
                    # print("*********")
                    degree_name_re = re.findall(r"^.*\(Hons\)", item['programme_en'])
                    d_re = ''.join(degree_name_re).strip()
                    item['degree_name'] = d_re.replace("(Hons)", "").strip()
                    item['programme_en'] = item['programme_en'].replace(d_re, "").strip()
                print("item['degree_name']1: ", item['degree_name'])
                print("item['programme_en']1: ", item['programme_en'])
                # if item['degree_name'] == "":
                #     print("*****111****")

                duration = response.xpath(
                    "//h4[contains(text(),'Course length')]/following-sibling::div[1]//text()").extract()
                clear_space(duration)
                # print("duration: ", duration)
                item['other'] = ' '.join(duration).strip()
                # print("item['other']: ", item['other'])
                duration_str = ''.join(duration)

                duration_list = getIntDuration(duration_str)
                if len(duration_list) == 2:
                    item['duration'] = duration_list[0]
                    item['duration_per'] = duration_list[-1]
                # print("item['duration'] = ", item['duration'])
                # print("item['duration_per'] = ", item['duration_per'])

                location = response.xpath(
                    "//h4[contains(text(),'Locations')]/following-sibling::div[1]//text()").extract()
                clear_space(location)
                item['location'] = ''.join(location).strip()
                # print("item['location'] = ", item['location'])

                # //div[@id='overview']
                overview = response.xpath("//section[@data-section='section-overview']").extract()
                overview_en = remove_class(clear_lianxu_space(overview))
                item['overview_en'] = overview_en
                # print("item['overview_en']: ", item['overview_en'])
                # if item['overview_en'] == "":
                #     print("*****111****")

                career_en = response.xpath("//h3[contains(text(),'Teaching methods')]/preceding-sibling::*").extract()
                if len(career_en) == 0:
                    career_en = response.xpath(
                        "//h3[contains(text(),'Careers')]|//h3[contains(text(),'Careers')]/following-sibling::*").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career_en)).replace("<h2>Course details</h2>", "").strip()
                # print("item['career_en']: ", item['career_en'])
                # if item['career_en'] == "":
                #     print("*****111****")

                assessment_en = response.xpath("//h3[contains(text(),'Teaching methods')]|//h3[contains(text(),'Teaching methods')]/following-sibling::*").extract()
                item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
                # print("item['assessment_en']: ", item['assessment_en'])
                # if item['assessment_en'] == "":
                #     print("*****111****")

                modules = response.xpath("//div[@id='module-structure']").extract()
                item['modules_en'] = remove_class(clear_lianxu_space(modules))
                # print("item['modules_en']: ", item['modules_en'])

                # //div[@id='fees']
                feeContent = response.xpath("//h4[contains(text(),'International Students')]/following-sibling::h5[contains(text(), 'Full time')]/following-sibling::*[1]//text()").extract()
                if len(feeContent) == 0:
                    feeContent = response.xpath(
                        "//h4[contains(text(),'International Students')]/following-sibling::p//strong[contains(text(),'Full time')]/..//text()").extract()
                clear_space(feeContent)
                # print("feeContent: ", feeContent)
                feelist = re.findall(r"£[\d,]+", ''.join(feeContent))
                if len(feelist) > 0:
                    item['tuition_fee'] = int(feelist[0].replace('£', '').replace(',', '').strip())
                # print("item['tuition_fee']: ", item['tuition_fee'])

                # //div[@id='how-to-apply']
                entry_requirements = response.xpath("//h2[contains(text(),'How to apply')]/preceding-sibling::*//text()").extract()
                rntry_requirements = clear_lianxu_space(entry_requirements)
                # print("item['rntry_requirements']: ", item['rntry_requirements'])

                # print("entry_requirementsStr: ", entry_requirementsStr)
                # ielts = re.findall(r"IELTS[\sa-zA-Z]*\d\.?\d?[\sa-z\(\)]*\d\.?\d?[\sa-z\(\)]{1,100}", rntry_requirements)
                # # print("ielts: ", ielts)
                item['ielts_desc'] = 'https://www.herts.ac.uk/international/new-international-students/applying-to-the-university-of-hertfordshire/international-entry-requirements'
                # print("item['ielts_desc']: ", item['ielts_desc'])

                if "Humanities" in item['programme_en'] or "Nursing" in item['programme_en'] or "Social Work" in item['programme_en'] or\
                        item['degree_name'] == "BSc" and item['programme_en'] == "Nutrition" or \
                                        item['degree_name'] == "BSc" and item['programme_en'] == "Pharmaceutical Science":
                    item['ielts_desc'] = 'IELTS 6.5 (minimum band scores also apply)'
                    item['ielts'] = '6.5'
                    item['ielts_l'] = '6.5'
                    item['ielts_s'] = '6.5'
                    item['ielts_r'] = '6.5'
                    item['ielts_w'] = '6.5'
                elif item['degree_name'] == "BSc" and item['programme_en'] == "Physiotherapy" or item['degree_name'] == "BSc" and item['programme_en'] == "Dietetics":
                    item['ielts_desc'] = 'IELTS 7.0 (minimum band scores also apply)'
                    item['ielts'] = '7.0'
                    item['ielts_l'] = '7.0'
                    item['ielts_s'] = '7.0'
                    item['ielts_r'] = '7.0'
                    item['ielts_w'] = '7.0'
                else:
                    item['ielts_desc'] = 'International English Language Testing System (IELTS) score of 6.0 (with no less than 5.5 in any band) for undergraduate or 6.5 (with no less than 5.5 in any band) for postgraduate.'
                    item['ielts'] = '6.0'
                    item['ielts_l'] = '5.5'
                    item['ielts_s'] = '5.5'
                    item['ielts_r'] = '5.5'
                    item['ielts_w'] = '5.5'
                # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

                # //div[@class='how-to-apply-table']/preceding-sibling::*[position()>1]
                item['alevel'] = None
                alevel = response.xpath("//p[contains(text(),'UCAS points')]//text()").extract()
                if len(alevel) == 0:
                    alevel = response.xpath("//li[contains(text(),'UCAS points')]//text()").extract()
                    if len(alevel) == 0:
                        alevel = response.xpath("//*[contains(text(),'UCAS points')]//text()").extract()
                        if len(alevel) == 0:
                            alevel = response.xpath("//strong[contains(text(),'A-Levels')]/../following-sibling::p[1]//text()|"
                                                    "//strong[contains(text(),'A Levels')]/../following-sibling::*[1]//text()").extract()
                if len(alevel) > 0:
                    item['alevel'] = remove_class(clear_lianxu_space([alevel[0]]))
                    if item['programme_en'] == "Nursing (Mental Health)":
                        item['alevel'] = remove_class(clear_lianxu_space(alevel))
                print("item['alevel']: ", item['alevel'])

                # //p[contains(text(),' IB')]
                item['ib'] = None
                ib = response.xpath("//p[contains(text(),' IB')]//text()|//*[contains(text(),'IB -')]//text()|//*[contains(text(),'IB –')]//text()").extract()
                if len(ib) == 0:
                    ib = response.xpath(
                        "//strong[contains(text(),'International Baccalaureate')]/../following-sibling::p[1]//text()|"
                        "//h3[contains(text(),'International Baccalaureate')]/following-sibling::p[1]//text()").extract()
                if len(ib) > 0:
                    item['ib'] = remove_class(clear_lianxu_space([ib[-1]]))
                print("item['ib']: ", item['ib'])

                item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<tr><th scope="row" id="table76505r3c1"> Undergraduate (year 1)</th><td headers="table76505r1c2 table76505r3c1">
Chinese 3-year Senior High School certificate with 85% or above
</td><td headers="table76505r1c3 table76505r3c1">
IELTS 6.0 with no less than 5.5 in any band
</td></tr><tr><th scope="row" id="table76505r4c1"> Undergraduate (year 2/3)</th><td headers="table76505r1c2 table76505r4c1">
Chinese 3-year College Diploma in related subject area with 70% or above
<br /><br />
SQA HND in related subject area with overall B grade
<br /><br />
BTEC HND in related subject area with overall Merit profile

</td><td headers="table76505r1c3 table76505r4c1">
IELTS 6.0 with no less than 5.5 in any band
</td></tr>"""]))
                item['apply_proces_en'] = "https://www.herts.ac.uk/international/new-international-students/applying-to-the-university-of-hertfordshire"

                start_date = response.xpath(
                    "//div[@class='how-to-apply-table']//table//td[contains(text(),'Full')]/preceding-sibling::*[2]//text()").extract()
                clear_space(start_date)
                # print("start_date: ", start_date)
                start_date = list(set(start_date))
                start_end = []
                for s in start_date:
                    s_p = s.split("/")
                    # print(s_p)
                    start_end.append(s_p[-1]+"-"+s_p[-2]+"-"+s_p[0])
                item['start_date'] = ','.join(start_end).strip()
                # print("item['start_date'] = ", item['start_date'])

                ucascode = response.xpath(
                    "//span[contains(text(),'UCAS code')]/../text()").extract()
                clear_space(ucascode)
                # print("ucascode: ", ucascode)
                if ',' in ''.join(ucascode):
                    print("****")
                    ucascode_sp = ''.join(ucascode).split(',')
                    # print(ucascode_sp)
                    for u in ucascode_sp:
                        if len(u.strip()) == 4:
                            item['ucascode'] = u.strip()
                            print("item['ucascode']1 = ", item['ucascode'])
                            yield item
                else:
                    item['ucascode'] = ''.join(ucascode).strip()
                    # print("item['ucascode'] = ", item['ucascode'])
                    yield item
                # print("len: ", len(ucascode))

        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)
