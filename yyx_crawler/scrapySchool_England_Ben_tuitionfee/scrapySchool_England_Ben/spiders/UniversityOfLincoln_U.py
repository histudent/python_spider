# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getIELTS import get_ielts
from scrapySchool_England_Ben.getDuration import getIntDuration
from w3lib.html import remove_tags


class UniversityOfLincoln_USpider(scrapy.Spider):
    name = "UniversityOfLincoln_U"
    start_urls = ['http://www.lincoln.ac.uk/home/studywithus/findacourse/?l=ug']

    def parse(self, response):
        # print(response.url)
        links = response.xpath(
            "//table[@id='keywordSearchtable']/tbody[@id='asp_searchResults']/tr/td[@class='cr']/div[contains(text(),'Undergraduate')]/preceding-sibling::a/@href").extract()

        # 组合字典
        programme_dict = {}
        programme_list = response.xpath("//table[@id='keywordSearchtable']/tbody[@id='asp_searchResults']/tr/td[@class='cr']/div[contains(text(),'Undergraduate')]/preceding-sibling::a//text()").extract()
        clear_space(programme_list)

        for link in range(len(links)):
            url = "http://www.lincoln.ac.uk" + links[link]

            programme_dict[url] = programme_list[link]

        print(len(links))
        links = list(set(links))
        print(len(links))

        '''2018-11-19：更新modules内容，去掉多余的数据'''
        # links = ["http://www.lincoln.ac.uk/home/course/MTHPHYUM/",
        #          "http://www.lincoln.ac.uk/home/course/BUSPSYUB/",
        #          "http://www.lincoln.ac.uk/home/course/CHMDRGUM/",
        #          "http://www.lincoln.ac.uk/home/course/EGRELCUM/",
        #          "http://www.lincoln.ac.uk/home/course/EDUEDUUB/",
        #          "http://www.lincoln.ac.uk/home/course/SOLSOLUB/",
        #          "http://www.lincoln.ac.uk/home/course/PBRPBRUB/",
        #          "http://www.lincoln.ac.uk/home/course/EGRELCUB/",
        #          "http://www.lincoln.ac.uk/home/course/CHMFRSUB/",
        #          "http://www.lincoln.ac.uk/home/course/JOUCRWUB/",
        #          "http://www.lincoln.ac.uk/home/course/ENLJOUUB/",
        #          "http://www.lincoln.ac.uk/home/course/AHSHSTUB/",
        #          "http://www.lincoln.ac.uk/home/course/HEAHEAUB/",
        #          "http://www.lincoln.ac.uk/home/course/CNSMGTUB/",
        #          "http://www.lincoln.ac.uk/home/course/LAWBSSUB/",
        #          "http://www.lincoln.ac.uk/home/course/LAWCRIUB/",
        #          "http://www.lincoln.ac.uk/home/course/CHMEDUUM/",
        #          "http://www.lincoln.ac.uk/home/course/MEDMEDUB/",
        #          "http://www.lincoln.ac.uk/home/course/BANFINUB/",
        #          "http://www.lincoln.ac.uk/home/course/BUSPRPUB/",
        #          "http://www.lincoln.ac.uk/home/course/GRAGRAUB/",
        #          "http://www.lincoln.ac.uk/home/course/SPTJOUUB/",
        #          "http://www.lincoln.ac.uk/home/course/PHRPHRUM/",
        #          "http://www.lincoln.ac.uk/home/course/EGREGRUM/",
        #          "http://www.lincoln.ac.uk/home/course/BUSECOUB/",
        #          "http://www.lincoln.ac.uk/home/course/BIOCHMUM/",
        #          "http://www.lincoln.ac.uk/home/course/CHMMTHUM/",
        #          "http://www.lincoln.ac.uk/home/course/EGRBCNUB/",
        #          "http://www.lincoln.ac.uk/home/course/MEDAUPUB/",
        #          "http://www.lincoln.ac.uk/home/course/ILLILLUB/",
        #          "http://www.lincoln.ac.uk/home/course/MTHPHLUB/",
        #          "http://www.lincoln.ac.uk/home/course/APPSOSUB/",
        #          "http://www.lincoln.ac.uk/home/course/TOUEMNUB/",
        #          "http://www.lincoln.ac.uk/home/course/EDMPSYUB/",
        #          "http://www.lincoln.ac.uk/home/course/CHMMTHUB/",
        #          "http://www.lincoln.ac.uk/home/course/CRISOPUB/",
        #          "http://www.lincoln.ac.uk/home/course/PRDPRDUB/",
        #          "http://www.lincoln.ac.uk/home/course/CHMDRGUB/",
        #          "http://www.lincoln.ac.uk/home/course/EGRCNSUM/",
        #          "http://www.lincoln.ac.uk/home/course/PROJOUUB/",
        #          "http://www.lincoln.ac.uk/home/course/ACCFINUB/",
        #          "http://www.lincoln.ac.uk/home/course/ARTARTUB/",
        #          "http://www.lincoln.ac.uk/home/course/ECLCSVUB/",
        #          "http://www.lincoln.ac.uk/home/course/PSYFSYUB/",
        #          "http://www.lincoln.ac.uk/home/course/ELECNSUB/",
        #          "http://www.lincoln.ac.uk/home/course/ISTSOPUB/",
        #          "http://www.lincoln.ac.uk/home/course/ISTPOLUB/",
        #          "http://www.lincoln.ac.uk/home/course/SESPESUB/",
        #          "http://www.lincoln.ac.uk/home/course/NURNURUB/",
        #          "http://www.lincoln.ac.uk/home/course/BVSBVSUB/",
        #          "http://www.lincoln.ac.uk/home/course/ENLENLUB/",
        #          "http://www.lincoln.ac.uk/home/course/PHYPHYUM/",
        #          "http://www.lincoln.ac.uk/home/course/EQSABWUM/",
        #          "http://www.lincoln.ac.uk/home/course/MKTPRPUB/",
        #          "http://www.lincoln.ac.uk/home/course/CGPCMPUB/",
        #          "http://www.lincoln.ac.uk/home/course/BUSIBMUB/",
        #          "http://www.lincoln.ac.uk/home/course/HSTHSTUB/",
        #          "http://www.lincoln.ac.uk/home/course/MTHPHYUB/",
        #          "http://www.lincoln.ac.uk/home/course/SESSCSUB/",
        #          "http://www.lincoln.ac.uk/home/course/NURPARUB/",
        #          "http://www.lincoln.ac.uk/home/course/ELECNSUM/",
        #          "http://www.lincoln.ac.uk/home/course/ECOFINUB/",
        #          "http://www.lincoln.ac.uk/home/course/BVSBVSUM/",
        #          "http://www.lincoln.ac.uk/home/course/CRICRIUB/",
        #          "http://www.lincoln.ac.uk/home/course/ELEPENUB/",
        #          "http://www.lincoln.ac.uk/home/course/CGPCMPUM/",
        #          "http://www.lincoln.ac.uk/home/course/ISGISGUB/",
        #          "http://www.lincoln.ac.uk/home/course/ARCARCUB/",
        #          "http://www.lincoln.ac.uk/home/course/EGREGRUB/",
        #          "http://www.lincoln.ac.uk/home/course/MTHCMPUB/",
        #          "http://www.lincoln.ac.uk/home/course/SOPSOLUB/",
        #          "http://www.lincoln.ac.uk/home/course/CHMEDUUB/",
        #          "http://www.lincoln.ac.uk/home/course/CHMCHMUM/",
        #          "http://www.lincoln.ac.uk/home/course/DANDANUB/",
        #          "http://www.lincoln.ac.uk/home/course/FRSFRSUB/",
        #          "http://www.lincoln.ac.uk/home/course/MGTPRPUB/",
        #          "http://www.lincoln.ac.uk/home/course/INTTOUUB/",
        #          "http://www.lincoln.ac.uk/home/course/MKTMKTUB/",
        #          "http://www.lincoln.ac.uk/home/course/CRISOLUB/",
        #          "http://www.lincoln.ac.uk/home/course/ENLDRAUB/",
        #          "http://www.lincoln.ac.uk/home/course/NURCLDUB/",
        #          "http://www.lincoln.ac.uk/home/course/LAWLAWUB/",
        #          "http://www.lincoln.ac.uk/home/course/MUSMUSUB/",
        #          "http://www.lincoln.ac.uk/home/course/FTVFTVUB/",
        #          "http://www.lincoln.ac.uk/home/course/MDSMDSUB/",
        #          "http://www.lincoln.ac.uk/home/course/ENLHSTUB/",
        #          "http://www.lincoln.ac.uk/home/course/GEHGEHUB/",
        #          "http://www.lincoln.ac.uk/home/course/PHAPHAUB/",
        #          "http://www.lincoln.ac.uk/home/course/BIOBIOUB/",
        #          "http://www.lincoln.ac.uk/home/course/CHMCHMUB/",
        #          "http://www.lincoln.ac.uk/home/course/CONCONUB/",
        #          "http://www.lincoln.ac.uk/home/course/ZOOZOOUM/",
        #          "http://www.lincoln.ac.uk/home/course/ELEPENUM/",
        #          "http://www.lincoln.ac.uk/home/course/BIOBIOUM/",
        #          "http://www.lincoln.ac.uk/home/course/TECTHEUB/",
        #          "http://www.lincoln.ac.uk/home/course/MTHMTHUM/",
        #          "http://www.lincoln.ac.uk/home/course/SESSESUB/",
        #          "http://www.lincoln.ac.uk/home/course/POLSOLUB/",
        #          "http://www.lincoln.ac.uk/home/course/BANFINUM/",
        #          "http://www.lincoln.ac.uk/home/course/MEDPROUB/",
        #          "http://www.lincoln.ac.uk/home/course/POLPOLUB/",
        #          "http://www.lincoln.ac.uk/home/course/AADAADUB/",
        #          "http://www.lincoln.ac.uk/home/course/PHYPHLUM/",
        #          "http://www.lincoln.ac.uk/home/course/EGRPENUM/",
        #          "http://www.lincoln.ac.uk/home/course/EQSABWUB/",
        #          "http://www.lincoln.ac.uk/home/course/PBRJOUUB/",
        #          "http://www.lincoln.ac.uk/home/course/ANIANIUB/",
        #          "http://www.lincoln.ac.uk/home/course/MDCMDCUB/",
        #          "http://www.lincoln.ac.uk/home/course/CLMCLMUB/",
        #          "http://www.lincoln.ac.uk/home/course/XMDXMDUB/",
        #          "http://www.lincoln.ac.uk/home/course/MTHMTHUB/",
        #          "http://www.lincoln.ac.uk/home/course/BUSDEVUB/",
        #          "http://www.lincoln.ac.uk/home/course/PSYPSYUB/",
        #          "http://www.lincoln.ac.uk/home/course/PHYPHYUB/",
        #          "http://www.lincoln.ac.uk/home/course/JOUINVUB/",
        #          "http://www.lincoln.ac.uk/home/course/NURMNHUB/",
        #          "http://www.lincoln.ac.uk/home/course/POLSOPUB/",
        #          "http://www.lincoln.ac.uk/home/course/ARCMANUB/",
        #          "http://www.lincoln.ac.uk/home/course/ARCBOAUB/",
        #          "http://www.lincoln.ac.uk/home/course/BUSFINUB/",
        #          "http://www.lincoln.ac.uk/home/course/MGZJOUUB/",
        #          "http://www.lincoln.ac.uk/home/course/ENLCRWUB/",
        #          "http://www.lincoln.ac.uk/home/course/BIOCHMUB/",
        #          "http://www.lincoln.ac.uk/home/course/CRWCRWUB/",
        #          "http://www.lincoln.ac.uk/home/course/EGRCNSUB/",
        #          "http://www.lincoln.ac.uk/home/course/ZOOZOOUB/",
        #          "http://www.lincoln.ac.uk/home/course/AMEAMEUB/",
        #          "http://www.lincoln.ac.uk/home/course/BMSBMSUM/",
        #          "http://www.lincoln.ac.uk/home/course/ECOECOUB/",
        #          "http://www.lincoln.ac.uk/home/course/CLSCVLUB/",
        #          "http://www.lincoln.ac.uk/home/course/ECOFINUM/",
        #          "http://www.lincoln.ac.uk/home/course/PSYCPYUB/",
        #          "http://www.lincoln.ac.uk/home/course/CMPCMSUB/",
        #          "http://www.lincoln.ac.uk/home/course/SESPHYUB/",
        #          "http://www.lincoln.ac.uk/home/course/SBMSBMUB/",
        #          "http://www.lincoln.ac.uk/home/course/BMSBMSUB/",
        #          "http://www.lincoln.ac.uk/home/course/CHMFRSUM/",
        #          "http://www.lincoln.ac.uk/home/course/INTINTUB/",
        #          "http://www.lincoln.ac.uk/home/course/CMPCMSUM/",
        #          "http://www.lincoln.ac.uk/home/course/GEPGEPUB/",
        #          "http://www.lincoln.ac.uk/home/course/SDCSDCUB/",
        #          "http://www.lincoln.ac.uk/home/course/EGRPENUB/",
        #          "http://www.lincoln.ac.uk/home/course/PHYPHLUB/",
        #          "http://www.lincoln.ac.uk/home/course/ISTISTUB/",
        #          "http://www.lincoln.ac.uk/home/course/SOPSOPUB/",
        #          "http://www.lincoln.ac.uk/home/course/FASFASUB/",
        #          "http://www.lincoln.ac.uk/home/course/ADVMKTUB/",
        #          "http://www.lincoln.ac.uk/home/course/PHLPHLUB/",
        #          "http://www.lincoln.ac.uk/home/course/DRADRAUB/",
        #          "http://www.lincoln.ac.uk/home/course/JOUJOUUB/", ]
        for link in links:
            url = "http://www.lincoln.ac.uk" + link
            # url = link
            yield scrapy.Request(url, callback=self.parse_data, meta=programme_dict)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "https://www.lincoln.ac.uk/"
        item['university'] = "University of Lincoln"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        item['location'] = 'University of Lincoln, Brayford Pool, Lincoln, LN6 7TS'
        print("===========================")
        print(response.url)
        item['major_type1'] = response.meta.get(response.url)
        print("item['major_type1']: ", item['major_type1'])
        try:
            if "Foundation" not in item['major_type1']:
                # //table[@id='newTitle']/tbody[@id='newTitleBody']/tr/td/h1[1]/a
                programmeDegreetype = response.xpath("//div[@id='CourseTitleApms']/h1//text()").extract()
                clear_space(programmeDegreetype)
                # print("programmeDegreetype: ", programmeDegreetype)
                if len(programmeDegreetype) > 0:
                    programmeDegreetypeStr = programmeDegreetype[0].strip()

                degree_type = re.findall(r"^\w+\s\(Hons\)|^\(\w+\)|^\w+", programmeDegreetypeStr)
                # print("degree_type: ", degree_type)
                degree_type_str = ''.join(degree_type).strip()
                item['degree_name'] = ''.join(degree_type).replace("(Hons)", "").replace("(", "").replace(")", "").strip()
                print("item['degree_name']: ", item['degree_name'])

                item['programme_en'] = programmeDegreetypeStr.replace(degree_type_str, '').strip()
                print("item['programme_en']: ", item['programme_en'])

                ucascode = response.xpath("//div[@class='nd_2019-20']//span[@class='blue'][contains(text(),'UCAS Code:')]/..//text()").extract()
                if len(ucascode) == 0:
                    ucascode = response.xpath("//span[@class='blue'][contains(text(),'UCAS Code:')]/..//text()").extract()
                clear_space(ucascode)
                # print("ucascode: ", ucascode)
                item['ucascode'] = ''.join(ucascode).replace("UCAS Code:", "").strip()
                # print("item['ucascode'] = ", item['ucascode'])

                # //span[@id='durationFT']
                duration = response.xpath("//div[@class='nd_2019-20']//span[contains(text(),'Full-time Duration')]/..//text()").extract()
                if len(duration) == 0:
                    duration = response.xpath("//span[contains(text(),'Full-time Duration')]/..//text()").extract()
                clear_space(duration)
                # print("duration: ", duration)
                duration_str = ''.join(duration)

                duration_list = getIntDuration(duration_str)
                if len(duration_list) == 2:
                    item['duration'] = duration_list[0]
                    item['duration_per'] = duration_list[-1]
                # print("item['duration'] = ", item['duration'])
                # print("item['duration_per'] = ", item['duration_per'])

                department = response.xpath("//span[contains(text(),'School:')]/following-sibling::a//text()").extract()
                clear_space(department)
                if len(department) > 0:
                    item['department'] = department[0]
                # print("item['department']: ", item['department'])

                dep_dict = {"lincoln school of architecture and the built environment": "College of Arts",
    "lincoln school of design": "College of Arts",
    "lincoln school of film and media": "College of Arts",
    "school of english and journalism": "College of Arts",
    "school of fine and performing arts": "College of Arts",
    "school of history and heritage": "College of Arts",
    "school of chemistry": "College of Science",
    "school of computer science": "College of Science",
    "school of engineering": "College of Science",
    "school of geography": "College of Science",
    "school of life sciences": "College of Science",
    "school of mathematics and physics": "College of Science",
    "school of pharmacy": "College of Science",
    "national centre for food manufacturing": "College of Science",
    "lincoln institute for agri-tech": "College of Science",
    "school of education": "College of Social Science",
    "school of health and social care": "College of Social Science",
    "professional development centre": "College of Social Science",
    "lincoln law school": "College of Social Science",
    "school of psychology": "College of Social Science",
    "school of social and political sciences": "College of Social Science",
    "school of sport and exercise science": "College of Social Science",}
                if item['department'] != "Lincoln Business School":
                    item['department'] = dep_dict.get(item['department'].lower())
                # print("item['department']1: ", item['department'])

                if item['department'] == None:
                    item['department'] = ''.join(response.xpath("//div[@class='breadcrumb-list']//span//a[@href='/home/collegeofsocialscience/']//text()").extract()).strip()
                # print("item['department']2: ", item['department'])

                # //div[@id='feesTables']/table
                fee = response.xpath("//div[@class='nd_2019-20']//div[@class='panel-body']//table[2]//td[contains(text(),'Full-time')]/following-sibling::*[last()]//text()").extract()
                if len(fee) == 0:
                    fee = response.xpath(
                        "//div[@class='panel-body']//table[2]//td[contains(text(),'Full-time')]/following-sibling::*[last()]//text()").extract()
                clear_space(fee)
                # print("fee: ", fee)
                feeStr = ''.join(fee)
                tuitionfee = getTuition_fee(feeStr)
                item['tuition_fee'] = tuitionfee
                if item['tuition_fee'] == 0:
                    item['tuition_fee'] = None
                # print("item['tuition_fee']: ", item['tuition_fee'])

                # //h2[contains(text(),'The Course')]/..
                overview = response.xpath("//h2[contains(text(),'The Course')]/..").extract()
                # print("overview: ", overview)
                if len(overview) > 0:
                    item['overview_en'] = remove_class(clear_lianxu_space([overview[-1]]))
                # print("item['overview_en']: ", item['overview_en'])

                modules_en = response.xpath("//a[contains(text(),'Modules')]/../../..").extract()
                modules_en = response.xpath(
                    "//div[@id='collapse62019-20']//div[@class='tab-content clearfix']").extract()

                if len(modules_en) > 0:
                    item['modules_en'] = remove_class(clear_lianxu_space([modules_en[-1]]))
                if item['modules_en'] == "":
                    item['modules_en'] = None
                    print("*** modules_en")
                else:
                    print("===", item['modules_en'])
                    del_cont = re.findall(r"<br>Find out more</p><div><span>.*?</em></span>", item['modules_en'])
                    print("del_cont==", del_cont)
                    if len(del_cont) > 0:
                        for delc in del_cont:
                            item['modules_en'] = item['modules_en'].replace(delc, '<div>').strip()
                print("item['modules_en']: ", item['modules_en'])

                assessment_en = response.xpath(
                    "//a[contains(text(),'How You Are Assessed')]/../../..|//a[contains(text(),'How you are assessed')]/../../..").extract()
                if len(assessment_en) > 0:
                    item['assessment_en'] = remove_class(clear_lianxu_space([assessment_en[-1]]))
                # print("item['assessment_en']: ", item['assessment_en'])

                interview_desc_en = response.xpath(
                    "//a[contains(text(),'Interviews & Applicant Days')]/../../..").extract()
                if len(interview_desc_en) > 0:
                    item['interview_desc_en'] = remove_class(clear_lianxu_space([interview_desc_en[-1]]))
                # print("item['interview_desc_en']: ", item['interview_desc_en'])

                alevel = response.xpath(
                    "//*[contains(text(),'GCE Advanced Levels')]/text()|//*[contains(text(),'A Level')]/text()").extract()
                if len(alevel) > 0:
                    item['alevel'] = clear_lianxu_space([alevel[-1]])
                print("item['alevel']: ", item['alevel'])

                ib = response.xpath(
                    "//p[contains(text(),'International Baccalaureate')]").extract()
                if len(ib) > 0:
                    item['ib'] = remove_tags(clear_lianxu_space([ib[-1]]))
                # print("item['ib']: ", item['ib'])

                rntry_requirements = response.xpath(
                    "//a[contains(text(),'Entry Requirements')]/../../..|//a[contains(text(),'Entry requirements')]/../../..").extract()
                if len(rntry_requirements) > 0:
                    rntry_requirements = remove_tags(clear_lianxu_space([rntry_requirements[-1]]))
                # print("rntry_requirements: ", rntry_requirements)

                ielts = re.findall(r"IELTS.{1,80}", rntry_requirements)
                item['ielts_desc'] = ''.join(ielts).strip()
                # print("item['ielts_desc']: ", item['ielts_desc'])

                ielts_dict = get_ielts(item['ielts_desc'])
                item['ielts'] = ielts_dict.get('IELTS')
                item['ielts_l'] = ielts_dict.get('IELTS_L')
                item['ielts_s'] = ielts_dict.get('IELTS_S')
                item['ielts_r'] = ielts_dict.get('IELTS_R')
                item['ielts_w'] = ielts_dict.get('IELTS_W')
                # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

                career = response.xpath("//div[@id='CourseCareersApms']").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career))
                # print("item['career_en']: ", item['career_en'])

                # if item['ielts_desc'] == "":
                #     item['ielts_desc'] = "Prospective students require IELTS 6.0 (with no less than 5.5 in each band score) or an equivalent qualification. Please note that some courses require a higher score."
                #     item['ielts'] = 6.0
                #     item['ielts_l'] = 5.5
                #     item['ielts_s'] = 5.5
                #     item['ielts_r'] = 5.5
                #     item['ielts_w'] = 5.5
                # print("******item['ielts_desc']: ", item['ielts_desc'])
                # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

                # http://www.lincoln.ac.uk/home/studywithus/internationalstudents/englishlanguagerequirementsandsupport/englishlanguagerequirements/
                if item['ielts'] == "6.5":
                    item['toefl'] = 90
                    item['toefl_l'] = 20
                    item['toefl_s'] = 22
                    item['toefl_r'] = 21
                    item['toefl_w'] = 22
                elif item['ielts'] == "7.0":
                    item['toefl'] = 100
                    item['toefl_l'] = 22
                    item['toefl_s'] = 23
                    item['toefl_r'] = 23
                    item['toefl_w'] = 23
                # print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
                #         item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

                # http://www.lincoln.ac.uk/home/studywithus/internationalstudents/entryrequirementsandyourcountry/china/
                item["require_chinese_en"] = remove_class(clear_lianxu_space(["""<div class="panel">
<div class="panel-heading">
<h4 class="panel-title">
<a data-toggle="collapse" href="#countryUndergraduateTab">
<em class="more-less glyphicon glyphicon-menu-down"></em>Undergraduate Entry
</a>
</h4>
</div>
<div id="countryUndergraduateTab" class="panel-collapse collapse">
<div class="panel-body">
<p>Prospective students require one of the following qualifications for entry into year one of an undergraduate degree:</p>
<ul>
<li>Successful completion of a Foundation programme with a minimum of 50% plus an average of 70% or above in High School. Please note that some programmes may require a higher foundation score e.g. 60%.</li>
<li>Successful completion of the first year of a Chinese degree / Diploma with an average grade of 70% or above.</li>
</ul>
<p><strong>&nbsp;</strong></p>
<p><strong>HND Students (BTEC and SQA)</strong></p>
<p>Students who have successfully completed a HND BTEC or SQA qualification may be accepted directly into year two or three of a University of Lincoln undergraduate course on a case by case basis.</p>
<p><strong>Chinese Degree / Diploma</strong></p>
<p>Students who have successfully completed the second or third year of a Chinese Degree or Diploma may be considered for direct entry into year two or three of a University of Lincoln undergraduate course on a case by case basis. For more information, please contact the International Admissions team:&nbsp;<a href="mailto:intadmissions&#64;lincoln&#46;ac&#46;uk">intadmissions&#64;lincoln&#46;ac&#46;uk</a>.</p>
<p>&nbsp;</p>	
<!-- START ADVANCED ENTRY (UNDERGRADUATE) -->
<p><strong>Advanced Entry (Undergraduate)</strong></p>
<p>Depending on your academic background and intended course of study, it may be possible to apply for advanced entry into year 2 or 3 of a University of Lincoln undergraduate course.</p>

<!-- START COUNTRY SPECIFIC ADVANCED ENTRY (UNDERGRADUATE) -->


<!-- END COUNTRY SPECIFIC ADVANCED ENTRY (UNDERGRADUATE) -->

<p id="advEntryUgEu">For more information, please contact the Student Administration Team: <a href="mailto:admissions@lincoln.ac.uk">admissions@lincoln.ac.uk</a>.</p>
<p id="advEntryUgInternational">For more information, please contact the International Admissions Team: <a href="mailto:intadmissions@lincoln.ac.uk">intadmissions@lincoln.ac.uk</a>.</p>
<!-- END ADVANCED ENTRY (UNDERGRADUATE) -->
</div>
</div>					
</div>
"""]))
                # print("item['require_chinese_en']: ", item['require_chinese_en'])

                item['apply_proces_en'] = "http://www.lincoln.ac.uk/home/studywithus/undergraduatestudy/howtoapply/"
                # print("item['apply_proces_en']: ", item['apply_proces_en'])
                yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

