# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem

class UniversitycollegelondonUSpider(scrapy.Spider):
    name = 'UniversityCollegeLondon_U'
    # allowed_domains = ['a.b']
    start_urls = ['http://www.ucl.ac.uk/prospective-students/undergraduate/degrees']

    #更新学费
    def parse(self, response):
        start_urlsss = [
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/economics-geography-bsc-econ/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemistry-european-language-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemistry-management-studies-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemistry-european-language-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/economics-business-east-european-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/economics-bsc-econ/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemical-physics-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemistry-international-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemical-physics-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/cancer-biomedicine-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-east-european-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemistry-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/economics-statistics-bsc-econ/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/economics-business-east-european-studies-year-abroad-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemistry-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bioprocessing-new-medicines-science-engineering-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/biotechnology-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/biological-sciences-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/biochemistry-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/biological-sciences-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bioprocessing-new-medicines-business-management-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/astrophysics-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/biomedical-sciences-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/arts-sciences-study-abroad-basc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/biochemistry-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/archaeology-year-abroad-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/arts-sciences-basc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/law-ucl-hku-llb/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/architectural-interdisciplinary-studies-year-abroad-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/archaeology-placement-year-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/archaeology-anthropology-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/archaeology-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/archaeology-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/architectural-interdisciplinary-studies-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/applied-medical-sciences-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/anthropology-year-abroad-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/anthropology-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/applied-medical-sciences-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/ancient-world-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/ancient-languages-year-abroad-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/ancient-world-year-abroad-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/ancient-history-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/ancient-languages-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/earth-sciences-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-slovak-east-european-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/computer-science-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/computer-science-meng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/classics-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/classical-archaeology-civilisation-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/architecture-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemistry-management-studies-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/urban-planning-design-management-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/astrophysics-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemistry-mathematics-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/viking-old-norse-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/earth-sciences-international-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/urban-studies-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemistry-mathematics-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/statistics-economics-finance-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/theoretical-physics-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/statistics-economics-language-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/ukrainian-east-european-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/earth-sciences-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/theoretical-physics-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/comparative-literature-year-abroad-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/comparative-literature-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/sociology-and-politics-of-science/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/social-sciences-quantitative-methods-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/spanish-latin-american-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/statistics-management-business-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/statistics-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/sport-exercise-medical-sciences-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/statistical-science-international-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/scandinavian-studies-history-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/social-sciences-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/serbian-croatian-east-european-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/slovak-czech-east-european-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/security-crime-science-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/scandinavian-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/russian-east-european-language-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/psychology-education-ba-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/russian-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/russian-history-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/psychology-language-sciences-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/project-management-construction-sandwich-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/psychology-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/psychology-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/project-management-construction-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/population-health-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/psychology-language-sciences-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/politics-international-relations-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/polish-east-european-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/politics-sociology-east-european-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/planning-real-estate-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/physics-medical-physics-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/politics-sociology-east-european-studies-year-abroad-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/physics-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/physics-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/philosophy-history-art-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/philosophy-politics-economics-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/philosophy-greek-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/pharmacy-mpharm/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/philosophy-economics-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/pharmacology-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/philosophy-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/neuroscience-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/nutrition-medical-sciences-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/modern-language-plus-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/modern-languages-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/natural-sciences-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/natural-sciences-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/medicine-mbbs-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/pharmacology-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/medicinal-chemistry-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/medicinal-chemistry-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/medical-sciences-engineering-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/medical-sciences-engineering-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/medical-innovation-enterprise-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-modern-languages-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/medical-physics-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-modern-languages-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-mathematical-physics-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/neuroscience-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-management-studies-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-statistical-science-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-statistical-science-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-economics-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-economics-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/romanian-east-european-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/medical-innovation-enterprise-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-physics-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-physics-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/management-science-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematical-computation-meng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/management-science-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/linguistics-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-mathematical-physics-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/linguistics-international-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-management-studies-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/law-hispanic-llb/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/law-french-llb/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/law-german-llb/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/language-culture-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/latin-greek-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/latin-english-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/international-social-political-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/information-management-business-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/law-llb/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/icelandic-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/human-sciences-evolution-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/latin-greek-study-abroad-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-european-language-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hungarian-east-european-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-studies-ucl-venice-double-degree-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-art-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-politics-americas-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/classics-study-abroad-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/infection-immunity-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-year-abroad-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-central-east-european-jewish-studies-year-abroad-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hebrew-jewish-studies-year-abroad-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/human-sciences-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-philosophy-science-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/greek-latin-study-abroad-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hebrew-jewish-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/greek-latin-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/greek-english-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-studies-history-art-ucl-venice-double-degree-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-politics-economics-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-history-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geophysics-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geology-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geology-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geography-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geography-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geophysics-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geography-international-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-asian-african-language-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/fine-art-bfa/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/fine-art-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-politics-americas-year-abroad-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-east-european-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/european-social-political-studies-dual-degree-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-art-material-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-architectural-design-meng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/environmental-geoscience-msci/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/environmental-geoscience-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/european-social-political-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-mechanical-meng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/english-german-law-dual-degree-llb/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/english-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-mechanical-beng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-mechanical-business-finance-beng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geography-international-bsc/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-electronic-electrical-meng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-chemical-meng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-electronic-electrical-beng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-biomedical-beng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-mechanical-business-finance-meng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-civil-beng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-biochemical-meng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-chemical-beng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-biomedical-meng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/education-studies-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-biochemical-beng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/economics-year-abroad-bsc-econ/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-civil-meng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/economics-placement-year-bsc-econ/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/egyptian-archaeology-ba/2019', ]
        start_urlsss = set(start_urlsss)
        for su in start_urlsss:
            yield scrapy.Request(url=su,meta={'url':su},callback=self.pars)
    def pars(self, response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'University College London'
        item['url'] = response.meta['url']
        tuition=response.xpath('//dt[contains(text(),"Overseas student")]/following-sibling::dd/text()').extract()
        print(tuition)
        tui=re.findall('\d{2}\,\d{3}',''.join(tuition))
        print(tui)
        item['tuition_fee']=''.join(tui).replace(',','').strip()
        if tui!=[]:
            yield item
    def parsess(self, response):
        pro_url=response.xpath('//td[@class="degree-list__item"]/a/@href').extract()
        # print(pro_url)
        for i in pro_url:
            i=i.replace('//','http://')
            yield scrapy.Request(url=i,callback=self.parses)
    #更新modules
    # def parse(self, response):
    #     item=get_item1(ScrapyschoolEnglandItem)
    #     item['university'] = 'University College London'
    #     item['url'] = response.url
    #     module_num = response.xpath('//div[contains(@id,"tab-year-")]').extract()
    #     # print(len(module_num))
    #     # print(module_num)
    #     title=response.xpath('//a[contains(@href,"#tab-year-")]//text()').extract()
    #     modules=[]
    #     # print(len(title))
    #     for tit,mod in zip(title,module_num):
    #         modules+='<h3>'+tit+'</h3>'+remove_class(mod)
    #     # print(''.join(modules))
    #     item['modules_en']=''.join(modules)
    #     print(response.url)
    #     yield item
    def parses(self,response):
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'University College London'
        item['url'] = response.url
        item['tuition_fee_pre'] = '£'
        location = response.xpath('//dt[contains(text(),"Location")]/following-sibling::dd//text()').extract()
        location = ''.join(location).strip()
        item['location'] = location
        programme = response.xpath('//h1//text()').extract()
        programme = ''.join(programme)
        # print(programme)
        degree_name = re.findall('[MB][A-Z][a-z]*', programme)
        # print(degree_name)
        degree_name = ''.join(set(degree_name)).strip()
        programme = programme.replace(degree_name, '')
        item['programme_en'] = programme
        item['degree_name'] = degree_name

        department = response.xpath('//a[@class="clicktracker facultylink"]/text()').extract()
        department = ''.join(department).strip()
        # print(department)
        item['department'] = department

        overview = response.xpath('//div[@id="standfirst"]').extract()
        # if overview==[]:
        #     print(response.url)
        # else:
        #     print('GG')
        overview = remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        application_open_date = response.xpath('//div[contains(text(),"Open")]/text()').extract()
        application_open_date = tracslateDate(application_open_date)
        # print(application_open_date)
        application_open_date = ','.join(set(application_open_date))
        item['application_open_date'] = application_open_date

        deadline = response.xpath('//dt[contains(text(),"deadline")]/following-sibling::dd[1]//text()').extract()
        deadline = tracslateDate(deadline)
        deadline = ','.join(set(deadline))
        item['deadline'] = deadline

        tuition_fee = getTuition_fee(response.xpath('//*[contains(text(),"£")]//text()').extract())
        item['tuition_fee'] = tuition_fee

        duration = response.xpath('//dt[contains(text(),"uration")]/following-sibling::dd/div/text()').extract()
        duration = clear_duration(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']

        ucascode=response.xpath('//dt[contains(text(),"UCAS")]/following-sibling::dd[1]//text()').extract()
        ucascode=''.join(ucascode).strip()
        item['ucascode']=ucascode

        start_date = response.xpath('//h4[contains(text(),"start")]/following-sibling::div/text()').extract()
        # print(start_date)
        start_date = tracslateDate(start_date)
        # print(start_date)
        start_date = ','.join(set(start_date))
        # print(start_date)
        item['start_date'] = start_date

        item['apply_fee'] = '75'
        item['apply_pre'] = '£'

        eng_level = response.xpath('//span[contains(text(),"The English language level for this programme is:")]/following-sibling::strong/text()').extract()
        eng_level = ''.join(eng_level).strip()
        if eng_level == 'Standard':
            ielts = 'Overall grade of 6.5 with a minimum of 6.0 in each of the subtests.'
            toefl = 'Overall score of 92 with 24/30 in reading and writing and 20/30 in speaking and listening.'
        elif eng_level == 'Good':
            ielts = 'Overall grade of 7.0 with a minimum of 6.5 in each of the subtests.'
            toefl = 'Overall score of 100 with 24/30 in reading and writing and 20/30 in speaking and listening.'
        elif eng_level == 'Advanced':
            ielts = 'Overall grade of 7.5 with a minimum of 6.5 in each of the subtests.'
            toefl = 'Overall score of 109 with 24/30 in reading and writing and 20/30 in speaking and listening.'
        else:
            ielts = ''
            toefl = ''

        ieltss = get_ielts(ielts)
        # print(ieltss)
        if ieltss != {} and ieltss != []:
            # ieltss=list(map(float,ieltss))
            item['ielts_l'] = ieltss['IELTS_L']
            item['ielts_s'] = ieltss['IELTS_S']
            item['ielts_r'] = ieltss['IELTS_R']
            item['ielts_w'] = ieltss['IELTS_W']
            item['ielts'] = ieltss['IELTS']
        toefls = re.findall('\d{1,3}', ''.join(toefl))
        # print(toefls)
        if len(toefls) == 5:
            item['toefl'] = toefls[0]
            item['toefl_l'] = toefls[4]
            item['toefl_w'] = toefls[2]
            item['toefl_r'] = toefls[1]
            item['toefl_s'] = toefls[3]
        elif len(toefls) == 2:
            toefls = list(map(int, toefls))
            item['toefl'] = max(toefls)
            item['toefl_l'] = min(toefls)
            item['toefl_w'] = min(toefls)
            item['toefl_r'] = min(toefls)
            item['toefl_s'] = min(toefls)
        item['ielts_desc'] = ielts
        item['toefl_desc'] = toefl
        # print(item)

        rntry_requirements = response.xpath('//h4[contains(text(),"ntry")]/following-sibling::p[1]').extract()
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)
        # item['rntry_requirements'] = rntry_requirements

        chinese_reuqirement = 'Successful completion of two years of the Bachelor Degree at a Chinese university recognised by UCL, with an average of: B+, 85% or a Cumulative GPA of 3.45/4.00%.'
        # chinese_reuqirement = '\n'.join(chinese_reuqirement)
        item['require_chinese_en'] = chinese_reuqirement

        modules = response.xpath('//h3[contains(text(),"Modules")]/following-sibling::div[1]').extract()
        modules = remove_class(modules)
        # print(modules)
        item['modules_en'] = modules

        career = response.xpath('//section[@id="careers"]').extract()
        # if career==[]:
        #     print(response.url)
        # else:
        #     print('GG')
        career = remove_class(career)
        item['career_en'] = career

        alevel=response.xpath('//h3[contains(text(),"A Levels")]/following-sibling::dl[1]//text()').extract()
        alevel=remove_class(alevel)
        # print(alevel)
        item['alevel']=alevel

        ib=response.xpath('//h3[contains(text(),"IB")]/following-sibling::dl[1]//text()').extract()
        ib=remove_class(ib)
        item['ib']=ib

        assessment=response.xpath('//h3[contains(text(),"ssessment")]/following-sibling::p[position()<=4]').extract()
        item['assessment_en']=remove_class(assessment)

        # print(item)
        yield item



