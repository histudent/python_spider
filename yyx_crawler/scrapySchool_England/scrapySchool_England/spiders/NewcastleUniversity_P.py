
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
import requests
from w3lib.html import remove_tags
import json

class NewcastleUniversity_PSpider(scrapy.Spider):
    name = "NewcastleUniversity_P"
    start_urls = ["https://www.ncl.ac.uk/postgraduate/courses/#a-z"]


    def parse(self, response):
        links = response.xpath("//ol[@id='azlink']/li/a/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))
        links = ["https://www.ncl.ac.uk/postgraduate/courses/degrees/medical-education-mmeded-pgdip-pgcert/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/applied-linguistics-research-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/technology-in-the-marine-environment-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/banking-finance-london-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/reflex-msc-pgdip-pgcert/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/global-wildlife-science-policy-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/ccc-applied-linguistics-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/regional-development-spatial-planning-ma-pgdip/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/marine-engineering-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/biomedical-engineering-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/cross-cultural-communication-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/offshore-engineering-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/latin-american-studies-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/geotechnical-engineering-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/archaeology-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/power-distribution-engineering-msc-pgdip-pgcert/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/spanish-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/architecture-master-of-march/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/applied-linguistics-tesol-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/archaeology-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/wildlife-management-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/materials-design-engineering-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/immunobiology-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/chemistry-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/cross-cultural-communication-education-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/translating-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/english-language-linguistics-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/applied-process-control-msc-pgdip/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/international-marketing-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/electrical-power-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/marine-ecosystems-governance-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/cross-cultural-communication-media-studies-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/sustainable-agriculture-food-security-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/planning-environment-research-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/restorative-dentistry-mclindent/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/european-union-studies-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/musculoskeletal-ageing-cima-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/british-history-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/advanced-electrical-power-engineering-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/urban-design-ma-pgdip/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/international-multimedia-journalism-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/landscape-architecture-studies-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/ccc-int-marketing-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/molecular-microbiology-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/agricultural-environmental-science-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/biofabrication-bioprinting-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/ccc-international-management-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/media-journalism-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/hydrology-water-management-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/design-manufacturing-engineering-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/cardiovascular-science-in-health-disease-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/food-rural-development-research-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/sustainable-agriculture-food-security-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/global-human-resource-management-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/international-political-economy-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/reem-msc-pgdip-pgcert/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/philosophy-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/ecology-wildlife-conservation-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/mechanical-engineering-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/international-financial-analysis-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/neuromuscular-diseases-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/medical-genetics-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/heritage-studies-ma-pgdip/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/media-society-research-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/advanced-computer-science-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/sociology-social-research-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/clinical-research-leader-mclinres-pgdip-pgcert/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/heritage-practice-mprac/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/operations-logistics-supply-chain-management-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/politics-research-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/operations-management-dual-award-msc-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/cell-signalling-health-disease-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/cloud-computing-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/banking-finance-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/clinical-linguistics-evi-based-prac-research-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/sociolinguistics-research-ma-pgdip/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/animal-behaviour-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/edu-int-perspectives-leadership-management-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/mitochondrial-biology-medicine-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/microelectronics-systems-devices-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/automation-control-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/quantitative-finance-risk-management-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/history-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/fine-art-mfa/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/digital-civics-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/ageing-health-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/japanese-studies-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/language-pathology-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/local-regional-development-research-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/urban-planning-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/e-business-information-systems-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/accounting-finance-strategic-investment-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/biodiversity-conservation-ecosystem-management-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/management-business-studies-research-ma-pgdip/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/international-development-education-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/transport-planning-engineering-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/advanced-int-bus-mgt-marketing-msc-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/physician-associate-studies-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/media-public-relations-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/data-science-msc-pgdip-pgcert/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/translation-studies-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/history-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/museum-studies-ma-pgdip/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/innovation-creativity-entrepreneurship-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/human-geography-research-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/cancer-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/master-of-business-administration-mba/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/computer-security-resilience-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/naval-architecture-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/hydrogeology-water-management-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/heritage-museums-galleries-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/museum-practice-mprac/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/synthetic-biology-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/interpreting-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/e-business-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/structural-engineering-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/environmental-consultancy-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/international-business-law-llm/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/chemical-engineering-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/environmental-engineering-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/world-politics-popular-culture-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/e-business-e-marketing-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/int-marketing-london-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/international-relations-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/computer-science-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/foundations-in-clinical-psychology-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/global-public-health-msc-pgdip/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/embedded-systems-internet-of-things-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/transport-planning-business-management-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/german-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/art-museum-gallery-studies-ma-pgdip/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/advanced-architectural-design-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/bioinformatics-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/history-of-medicine-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/health-services-research-msc-pgdip/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/arts-business-creativity-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/international-politics-critical-geopolitics-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/creative-arts-practice-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/professional-translation-for-european-languages-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/forensic-psychology-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/sociology-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/industrial-commercial-biotechnology-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/translation-studies-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/medical-sciences-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/transplantation-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/film-studies-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/law-llm/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/mechatronics-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/music-mmus-pgdip/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/marine-transport-management-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/subsea-engineering-management-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/communications-signal-processing-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/english-literature-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/computational-neuroscience-neuroinformatics-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/advanced-international-business-management-msc-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/cloud-computing-for-big-data-mres-pgdip/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/public-health-mph-pgdip/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/engineering-geology-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/european-history-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/medical-molecular-biosciences-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/pipeline-engineering-msc-pgdip-pgcert/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/biotechnology-business-enterprise-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/sustainable-transport-engineering-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/computer-game-engineering-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/international-law-llm/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/international-business-management-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/creative-writing-ma-pgcert/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/translational-medicine-therapeutics-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/music-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/diabetes-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/finance-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/portuguese-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/french-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/urban-energy-technology-policy-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/translating-interpreting-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/sustainable-chemical-engineering-msc-pgdip/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/international-business-management-london-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/stem-cells-regenerative-medicine-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/social-science-health-research-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/english-literature-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/edu-int-perspectives-technology-education-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/chinese-studies-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/art-museum-gallery-practice-mprac/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/classics-mlitt/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/public-health-hsresearch-msc-pgdip-pgcert/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/drug-chemistry-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/physics-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/international-economics-finance-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/toxicology-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/neuroscience-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/clean-technology-msc-pgdip/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/classics-ancient-history-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/computational-ecology-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/ccc-int-relations-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/linguistics-englishlang-langacq-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/int-politics-globalisation-poverty-development-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/epidemiology-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/international-politics-global-justice-ethics-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/law-society-legal-research-llm/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/evolution-human-behaviour-mres/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/edu-int-perspectives-teaching-learning-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/finance-economics-research-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/int-dev-edu-cross-cultural-comms-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/hydroinformatics-water-management-euro-aquae-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/ecological-consultancy-msc/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/education-research-ma/",
"https://www.ncl.ac.uk/postgraduate/courses/degrees/film-theory-practice-ma/", ]
        for link in links:
            # url = "https://www.ncl.ac.uk" + link
            # url = "https://www.ncl.ac.uk/postgraduate/courses/degrees/business-humanities-presessional-grad-dip-ipc/"
            url = link
            yield scrapy.Request(url, callback=self.parse_data)


    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "Newcastle University"
        # item['country'] = 'England'
        # item['website'] = 'http://www.ncl.ac.uk/'
        item['url'] = response.url
        # 授课方式
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        print("===========================")
        print(response.url)
        try:
            # 专业
            programmeDegree_type = response.xpath(
                "//div[@class='introTextArea']/h1//text()").extract()
            programmeDegree_type = ''.join(programmeDegree_type)
            print("programmeDegree_type: ", programmeDegree_type)
            # degree_typeList = re.findall(r"(\w+,\s\w+,\s\w+$)|(\w+,\s\w+$)|(\w+$)", programmeDegree_type)
            degree_typeList = re.findall(r"(Doctor\sof\s\([\w\s]+\)$)|(Master\sof\s\([\w\s]+\)$)|(Graduate\sDiploma)|(\(PGCE\))|(\w+,\s\w+,\s\w+$)|(\w+,\s\w+$)|(\w+$)", programmeDegree_type)
            # print("degree_typeList: ", degree_typeList)
            programme = programmeDegree_type
            if len(degree_typeList) != 0:
                degree_type = ''.join(list(degree_typeList[0]))
                item['degree_name'] = degree_type.replace("(", "").replace(")", "").strip()
                programme = programmeDegree_type.replace(item['degree_name'], "")
            print("item['degree_name']: ", item['degree_name'])
            item['programme_en'] = ''.join(programme).strip().strip(",").strip()
            print("item['programme_en']: ", item['programme_en'])



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

            # overview
            if "Profile" in allcontent:
                overviewIndex = allcontent.index("Profile")
                if "Delivery" in allcontent:
                    overviewIndexEnd = allcontent.index("Delivery")
                    overview = allcontent[overviewIndex+1:overviewIndexEnd]
                    clear_space(overview)
                    item['overview_en'] = clear_lianxu_space(overview)
                elif "Facilities" in allcontent:
                    overviewIndexEnd = allcontent.index("Facilities")
                    overview = allcontent[overviewIndex+1:overviewIndexEnd]
                    clear_space(overview)
                    item['overview_en'] = clear_lianxu_space(overview)
                elif "Pathway" in allcontent:
                    overviewIndexEnd = allcontent.index("Pathway")
                    overview = allcontent[overviewIndex+1:overviewIndexEnd]
                    clear_space(overview)
                    item['overview_en'] = clear_lianxu_space(overview)
            if len(item['overview_en']) != 0:
                item['overview_en'] = "<div>"+item['overview_en']+"</div>"
            if item['overview_en'] == "":
                overview_r = response.xpath("//h2[contains(text(),'Profile')]|"
                                            "//h2[contains(text(),'Profile')]/following-sibling::*[position()<20]|"
                                            "//h2[contains(text(),'Profile')]/..|"
                                            "//h2[contains(text(),'Profile')]/../following-sibling::*[position()<20]|"
                                            "//p[@class='intro']").extract()
                item['career_en'] = remove_class(clear_lianxu_space(overview_r))
            if item['overview_en'] == "":
                print("overview_en 为空")
            # print("item['overview_en']: ", item['overview_en'])

            # modules
            if "Modules" in allcontent:
                modulesIndex = allcontent.index("Modules")
                if "Explore Careers" in allcontent:
                    modulesIndexEnd = allcontent.index("Explore Careers")
                    modules = allcontent[modulesIndex+1:modulesIndexEnd]
                    clear_space(modules)
                    item['modules_en'] = clear_lianxu_space(modules)
                elif "Fees & Funding" in allcontent:
                    modulesIndexEnd = allcontent.index("Fees & Funding")
                    modules = allcontent[modulesIndex+1:modulesIndexEnd]
                    clear_space(modules)
                    item['modules_en'] = clear_lianxu_space(modules)
            if len(item['modules_en']) != 0:
                # print(item['modules_en'])
                # print("===", item['modules_en'].split('\n'))
                modules_tmp = ""
                for m in item['modules_en'].split('\n'):
                    modules_tmp += "<p>" + m + "</p>"
                item['modules_en'] = "<div>" + modules_tmp + "</div>"

            if item['modules_en'] == "":
                item['modules_en'] = None
                print("modules_en 为空")
            print("item['modules_en']: ", item['modules_en'])


            # career
            if "Careers" in allcontent:
                careerIndex = allcontent.index("Careers")
                if "Explore Fees & Funding" in allcontent:
                    careerIndexEnd = allcontent.index("Explore Fees & Funding")
                    career = allcontent[careerIndex + 2:careerIndexEnd]
                    clear_space(career)
                    item['career_en'] = clear_lianxu_space(career)
            elif "Training & Skills" in allcontent:
                careerIndex = allcontent.index("Training & Skills")
                if "Fees & Funding" in allcontent:
                    careerIndexEnd = allcontent.index("Fees & Funding")
                    career = allcontent[careerIndex + 2:careerIndexEnd]
                    clear_space(career)
                    item['career_en'] = clear_lianxu_space(career)
            if len(item['career_en']) != 0:
                item['career_en'] = "<div>" + item['career_en'] + "</div>"
            if item['career_en'] == "":
                career_r = response.xpath("//h2[contains(text(),'Careers')]/../preceding-sibling::*[1]/following-sibling::*[position()<9]|"
                                          "//h3[contains(text(),'Careers')]|//h3[contains(text(),'Careers')]/following-sibling::*[position()<5]|"
                                          "//h3[contains(text(),'Accreditation')]|//h3[contains(text(),'Accreditation')]/following-sibling::*[position()<5]|"
                                          "//h3[contains(text(),'Your development')]/../..|"
                                          "//span[contains(text(),'Your development')]/..|//span[contains(text(),'Your development')]/../following-sibling::*[position()<10]").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career_r))
            if item['career_en'] == "":
                print("******career")
            # print("item['career_en']: ", item['career_en'])

            work_experience_desc_en = response.xpath(
                "//h3[contains(text(),'Work experience')]/preceding-sibling::*[1]/following-sibling::*[position()<5]").extract()
            item['work_experience_desc_en'] = remove_class(clear_lianxu_space(work_experience_desc_en))
            # print("item['work_experience_desc_en']: ", item['work_experience_desc_en'])

            # tuition_fee
            if "Fees & Funding" in allcontent:
                tuition_feeIndex = allcontent.index("Fees & Funding")
                if "Entry Requirements" in allcontent:
                    tuition_feeIndexEnd = allcontent.index("Entry Requirements")
                    tuition_fee = allcontent[tuition_feeIndex + 2:tuition_feeIndexEnd]
                    clear_space(tuition_fee)
                    maxfee = getTuition_fee(''.join(tuition_fee))
                    # print("maxfee: ========", maxfee)
                    item['tuition_fee'] = maxfee
                    item['tuition_fee_pre'] = "£"
            if item['tuition_fee'] == 0:
                item['tuition_fee'] = None
            # print("item['tuition_fee']: ", item['tuition_fee'])


            # 学术要求
            if "Entry Requirements" in allcontent:
                entry_requirementsIndex = allcontent.index("Entry Requirements")
                if "How to Apply" in allcontent:
                    entry_requirementsIndexEnd = allcontent.index("How to Apply")
                    entry_requirements = allcontent[entry_requirementsIndex+1:entry_requirementsIndexEnd]
                    clear_space(entry_requirements)
                    item['rntry_requirements'] = clear_lianxu_space(entry_requirements).replace("Find out How to Apply", "").strip()
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            # how_to_apply
            if "How to Apply" in allcontent:
                how_to_applyIndex = allcontent.index("How to Apply")
                how_to_apply = allcontent[how_to_applyIndex + 1:]
                clear_space(how_to_apply)
                item['apply_proces_en'] = clear_lianxu_space(how_to_apply)
            if item['apply_proces_en'] != "":
                item['apply_proces_en'] = "<div>" + item['apply_proces_en'] + "</div>"
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

            # if "Application fee" in allcontent:
            #     application_feeIndex = allcontent.index("Application fee")
            #     application_fee = allcontent[application_feeIndex:]
            #     clear_space(application_fee)
            #     item['apply_fee'] = clear_lianxu_space(application_fee)

            apply_fee_re = re.findall(r"application\sfee\sof\s£\d+", item['apply_proces_en'])
            # print(apply_fee_re)
            if len(apply_fee_re) > 0:
                item['apply_fee'] = int(''.join(apply_fee_re).replace("application fee of", "").replace("£", "").strip())
                item['apply_pre'] = "£"
            # print("item['apply_fee']: ", item['apply_fee'])
            # print("item['apply_pre']: ", item['apply_pre'])

            # # School\sof[\w\s]*             Newcastle\sUniversity\sBusiness\sSchool
            # department = re.findall(r"(School\sof[\w\s]{1,20})|(Newcastle\sUniversity\sBusiness\sSchool)", ''.join(allcontent))
            department = re.findall(r"Newcastle\sUniversity\sBusiness\sSchool", ''.join(allcontent))
            # print("department: ", department)
            if len(department) > 0 and item['department'] == "":
                item['department'] = department[0]
            # print("item['department']: ", item['department'])

            # IELTS
            # print("programmeDegree_type: ", programmeDegree_type)
            prt = programmeDegree_type.replace(" ", "%20")
            # print("prt: ", prt)
            ieltsToeflUrl = "http://includes.ncl.ac.uk/cmswebservices/pg/languageRequirements/ws.php?title="+prt
            # print("ieltsToeflUrl: ", ieltsToeflUrl)
            # 获得item['ielts_desc']和item['toefl_desc']
            self.parse_ieltsToefl(ieltsToeflUrl, item)

            if item['ielts_desc'] == "":
                ielt_dd = response.xpath("//*[contains(text(),'IELTS')]/..//text()").extract()
                clear_space(ielt_dd)
                # print(ielt_dd)
                # if len(ielt_dd) > 0:
                item['ielts_desc'] = ''.join(ielt_dd).replace("65", "").strip()
                # print("*item['ielts_desc']*=: ", item['ielts_desc'])
                if item['ielts_desc'] != "":
                    item['ielts_desc'] = ''.join(re.findall(r".{1,90}IELTS.{1,90}", item['ielts_desc'])).strip()
            # print("*item['ielts_desc']: ", item['ielts_desc'])
            # print("*item['toefl_desc']: ", item['toefl_desc'])

            if item['ielts_desc'] != "":
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

            if item['toefl_desc'] != "":
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
                elif len(toefl_list) == 4:
                    item['toefl'] = toefl_list[0]
                    item['toefl_l'] = toefl_list[3]
                    item['toefl_r'] = toefl_list[1]
                    item['toefl_s'] = toefl_list[2]
                    item['toefl_w'] = toefl_list[1]
                elif len(toefl_list) == 5:
                    item['toefl'] = toefl_list[0]
                    item['toefl_l'] = toefl_list[1]
                    item['toefl_r'] = toefl_list[2]
                    item['toefl_s'] = toefl_list[3]
                    item['toefl_w'] = toefl_list[4]
            # print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
            #                             item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))
            if item['toefl_w'] == item['toefl_r'] and item['toefl_w']!= item['toefl_l'] and item['toefl_w']!= item['toefl_s']:
                item['ielts_r'] = item['ielts_w']
            # print("====","item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))


            # chinese_requirements
            item['require_chinese_en'] = """<h3>Postgraduate entry requirements (excluding Newcastle University Business School)</h3><p>Typically we recognise:</p><ul><li>75% in a four Year Bachelor degree from a Tier 1 University or 80% from a Tier 2 University as comparable to a <em>2.1</em> and 70% from a Tier 1 University or 75% from a Tier 2 University as comparable to a <em>2.2</em></li><li>80% in an Adult degree or E-learning as comparable to a<em> 2.1</em> and 75% as equivalent to <em>2.2</em></li></ul><p>You may be considered for <em>entry to masters study with a three year university diploma</em> and more than <em>five years of relevant work experience</em>.</p>"""
            if item['department'] == "Newcastle University Business School":
                item['require_chinese_en'] = """<h3>Newcastle University Business School postgraduate entry requirements</h3><p>Typically we recognise 75% in a four year bachelor degree from a Tier 1 university or 82% from a Tier 2 university as comparable to a<em> 2.1</em> in the following courses:</p><ul><li>Banking and Finance MSc</li><li>Finance MSc</li><li>International Economics and Finance MSc</li><li>Quantitative Finance and Risk Management MSc</li></ul><p>For all other Newcastle University Business School postgraduate courses typically we recognise:</p><ul><li>80% in a four year Bachelor degree from a Tier 1 University as comparable to a <em>2.1</em></li><li>or 85% from a Tier 2 University as comparable to a<em> 2.1</em></li></ul><p>If you <em>do not meet these requirements</em> you may be eligible to apply for entry to a <em>course at INTO Newcastle University</em>. These courses are based on our campus and help you to prepare for study with us.</p>"""
            # print("item['require_chinese_en']: ", item['require_chinese_en'])

            item['location'] = "Newcastle University, NE1 7RU, United Kingdom"

            # duration
            duration = response.xpath(
                "//div[@class='introTextArea']/p/text()").extract()
            duration_str = '\n'.join(duration).strip()
            # print("duration_str: ", duration_str)
            item['teach_time'] = getTeachTime(duration_str)
            duration_list = getIntDuration(duration_str)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration']: ", item['duration'])
            # print("item['duration_per']: ", item['duration_per'])
            # print("item['teach_time']: ", item['teach_time'])
            # 以phd类型存入数据库
            if item['degree_name'].lower() == "phd":
                item['degree_type'] = 3
                item['teach_type'] = 'phd'
                yield item
                # 既有phd类型，又有硕士taught类型，要存两条
            elif "phd" in item['degree_name'].lower() and item['degree_name'].lower() != "phd":
                yield item
                duration_phd_re = re.findall(r"PhD.*", duration_str, re.I)
                # print("duration_phd_re: ", duration_phd_re, "---", item['degree_name'], "---", item['programme_en'])
                duration_phd_list = getIntDuration(''.join(duration_phd_re))
                if len(duration_phd_list) == 2:
                    item['duration'] = duration_phd_list[0]
                    item['duration_per'] = duration_phd_list[-1]
                # print("phd item['duration']: ", item['duration'])
                # print("phd item['duration_per']: ", item['duration_per'])
                # print("phd item['teach_time']: ", item['teach_time'])
                item['degree_type'] = 3
                item['teach_type'] = 'phd'
                yield item
            else:
                item['degree_type'] = 2
                item['teach_type'] = 'taught'
                yield item
            # elif "m" in item['degree_name'].lower():
            #     item['degree_type'] = 2
            #     item['teach_type'] = 'taught'
            # print("item['degree_type']: ", item['degree_type'])
            # print("item['teach_type']: ", item['teach_type'])

            # yield item
        except Exception as e:
            with open("scrapySchool_England/error/" + item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_ieltsToefl(self, ieltsToeflUrl, item):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        data = requests.get(ieltsToeflUrl, headers=headers)
        response = data.text
        # print(data.text, "----")
        response = json.loads(response)
        # print(type(response))
        # print(response)
        d = {}
        if type(response) == type(d):
            item['ielts_desc'] = remove_tags(response.get("ielts"))
            # print("item['ielts_desc']: ", item['ielts_desc'])
            item['toefl_desc'] = remove_tags(response.get("toefl"))
            # print("item['toefl_desc']: ", item['toefl_desc'])
