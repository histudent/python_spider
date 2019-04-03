# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
import requests
from lxml import etree
class UniversityofliverpoolUSpider(scrapy.Spider):
    name = 'UniversityOfLiverpool_U'
    start_url=[]
    # feeRes =etree.HTML(requests.get('https://www.liverpool.ac.uk/study/international/tuition-fees-and-scholarships/undergraduate-fees/').content)
    start_urls=['https://www.liverpool.ac.uk/study/undergraduate/courses/diagnostic-radiography-bsc-hons/entry-requirements/']
    def parse(self, response):
        urls=['https://www.liverpool.ac.uk/study/undergraduate/courses/diagnostic-radiography-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/earth-sciences-entry-route-leading-to-bsc-hons-4-year-route-including-a-foundation-year-at-carmel-college/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/economics-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/economics-year-in-industry-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/egyptology-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/electrical-engineering-and-electronics-beng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/electrical-engineering-and-electronics-meng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/electrical-engineering-and-electronics-with-a-year-in-industry-beng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/electrical-engineering-and-electronics-with-a-year-in-industry-meng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/engineering-beng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/engineering-foundation-beng-hons-4-year-route-including-a-foundation-year-at-carmel-college/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/engineering-meng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/english-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/english-language-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/english-literature-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/environment-and-planning-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/environmental-sciences-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/evolutionary-anthropology-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/film-studies-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/finance-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/finance-year-in-industry-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/e-finance-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/financial-computing-with-a-year-in-industry-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/french-and-mathematics-ba-joint-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/french-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/genetics-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/oceans-climate-and-physical-geography-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/geography-and-planning-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/geography-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/geography-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/geography-bsc-hons-4-year-route-including-a-foundation-year-at-carmel-college/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/geology-north-america-mesci-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/geology-and-geophysics-mesci-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/geology-and-physical-geography-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/geology-and-physical-geography-mesci-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/geology-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/geology-mesci-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/geophysics-geology-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/geophysics-north-america-mesci-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/geophysics-physics-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/german-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/iberian-and-latin-american-studies-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/history-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/physiology-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/industrial-design-engineering-beng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/industrial-design-engineering-meng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/international-business-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/international-business-year-in-industry-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/international-politics-and-policy-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/irish-studies-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/italian-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/law-llb-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/law-with-a-year-abroad-llb-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/law-with-accounting-and-finance-llb-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/marine-biology-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/marine-biology-mmarbiol/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/marine-biology-with-oceanography-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/marketing-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/marketing-year-in-industry-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mathematical-physics-mmath/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mathematical-sciences-entry-route-leading-to-bsc-hons-4-year-route-including-a-foundation-year-at-carmel-college/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mathematics-and-business-studies-bsc-joint-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mathematics-and-computer-science-bsc-joint-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mathematics-and-computer-science-with-a-year-in-industry-bsc-joint-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mathematics-and-economics-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mathematics-and-music-technology-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mathematics-and-philosophy-ba-joint-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mathematics-and-statistics-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mathematics-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mathematics-mmath/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mathematics-with-finance-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mathematical-sciences-with-a-european-language-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mathematics-with-ocean-and-climate-sciences-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mechanical-engineering-meng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mechanical-engineering-beng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mechatronics-and-robotic-systems-beng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mechatronics-and-robotic-systems-meng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mechatronics-and-robotic-systems-with-year-in-industry-beng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/mechatronics-and-robotic-systems-with-year-in-industry-meng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/medicinal-chemistry-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/medicinal-chemistry-with-pharmacology-mchem/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/medicine-and-surgery-mbchb/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/microbiology-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/modern-language-studies-ba-joint-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/modern-languages-triple-subject-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/music-popular-music-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/music-and-technology-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/music-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/occupational-therapy-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/ocean-sciences-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/ocean-sciences-mosci-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/orthoptics-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/pharmacology-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/philosophy-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/philosophy-politics-economics-ba/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/physical-sciences-entry-route-leading-to-bsc-hons-4-year-route-including-a-foundation-year-at-carmel-college/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/physics-and-mathematics-bsc-joint-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/physics-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/physics-mphys/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/physics-with-astronomy-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/physics-with-medical-applications-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/physics-with-nuclear-science-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/physiotherapy-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/politics-and-international-business-ba-joint-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/politics-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/popular-music-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/psychology-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/psychology-bsc-hons-with-foundation-element/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/psychology-mpsycholsci-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/radiotherapy-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/sociology-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/theoretical-physics-mphys/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/town-and-regional-planning-mplan/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/tropical-disease-biology-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/urban-regeneration-and-planning-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/veterinary-science-bvsc/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/zoology-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/accounting-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/anatomy-and-human-biology-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/aerospace-engineering-with-pilot-studies-beng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/accounting-and-finance-year-in-industry-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/aerospace-engineering-with-pilot-studies-meng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/actuarial-mathematics-bsc/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/aerospace-engineering-beng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/biological-sciences-mbiolsci-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/aerospace-engineering-meng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/ancient-history-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/archaeology-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/archaeology-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/architectural-engineering-beng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/archaeology-of-ancient-civilisations-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/architectural-engineering-meng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/architecture-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/astrophysics-mphys/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/avionic-systems-beng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/avionic-systems-meng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/avionic-systems-with-year-in-industry-beng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/biochemistry-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/biological-and-medical-sciences-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/biological-sciences-with-a-foundation-year-leading-to-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/biological-sciences-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/bioveterinary-science-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/business-economics-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/business-economics-year-in-industry-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/business-management-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/business-studies-with-a-year-industry-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/chemical-sciences-bsc-hons-4-year-route-including-a-foundation-year-at-carmel-college/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/chemistry-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/chemistry-sustainable-energy-mchem/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/chemistry-mchem/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/chemistry-with-a-year-in-industry-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/chemistry-with-research-in-industry-mchem/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/civil-and-structural-engineering-meng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/civil-engineering-beng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/civil-engineering-meng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/classical-studies-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/classics-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/communication-and-media/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/communication-and-media-with-a-year-in-industry/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/computer-science-and-electronic-engineering-beng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/computer-science-and-electronic-engineering-meng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/computer-science-and-electronic-engineering-with-year-in-industry-beng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/computer-science-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/computer-science-bsc-hons-foundation-4-year-route-with-carmel-college/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/computer-science-meng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/computer-science-with-a-year-in-industry-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/computer-science-with-a-year-in-industry-meng-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/software-development-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/software-development-with-a-year-in-industry-bsc-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/criminology-ba-hons/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/dental-hygiene-and-dental-therapy-bsc/overview/',
'https://www.liverpool.ac.uk/study/undergraduate/courses/dental-surgery-bds/overview/',]
        urls=set(urls)
        for u in urls:
            u=u.replace('/overview/','/entry-requirements/')
            yield scrapy.Request(url=u,callback=self.parses,meta={'url':u})
    def parses(self, response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['location']='Liverpool'
        item['university'] = 'University of Liverpool'
        item['url']=response.url
        # programme=response.xpath('//h1/span/text()').extract()
        # deg=re.findall('[A-Za-z]+\s?\(Hons\)',''.join(programme))
        # deg=''.join(deg).strip()
        # programme=''.join(programme).replace(deg,'').strip()
        # item['programme_en']=programme
        # item['degree_name']=deg
        modules_url = response.url.replace('overview', 'module-details')
        career_url=response.url.replace('fees-finance','career-prospects')
        career=self.getTag(self.getRes(career_url).xpath('//div[@class="course-detail"]'))
        item['career_en']=career
        modules=self.getTag(self.getRes(modules_url).xpath('//div[@class="course-detail"]'))
        item['modules_en']=modules
        item['tuition_fee_pre']='£'
        # ucascode = response.xpath('//li[contains(text(),"UCAS")]/span/text()').extract()
        # ucascode = set(ucascode)
        # ucascode = ''.join(ucascode).strip()
        # item['ucascode'] = ucascode
        # duration = response.xpath('//li[contains(text(),"Course length")]/span/text()').extract()
        # duration = set(duration)
        # duration = clear_duration(duration)
        # item['duration'] = duration['duration']
        # item['duration_per'] = duration['duration_per']
        # require_chinese_en = ['<h3>Undergraduate</h3>',
        #                       '<p>Students who have completed 12 years of education (Gao Zhong) in China must complete a Foundation Programme or GCE A Level (or equivalent) and demonstrate proficiency in English language in order to progress on to an undergraduate degree programme. Please note that students who have taken the Chinese University Entrance Exam (Gao Kao) in China are also required to complete a Foundation Programme.</p>', ]
        # require_chinese_en = remove_class(require_chinese_en)
        # item['require_chinese_en'] = require_chinese_en
        # aib = response.xpath('//li[contains(text(),"Typical")]//text()').extract()
        # aib = ''.join(aib)
        # alevel = re.findall('A-level :\s*[A-Z]*', aib)
        # alevel = set(alevel)
        # alevel = ''.join(alevel).replace('A-level :', '').strip()
        # item['alevel'] = alevel
        # ib = re.findall('IB :\s*\d+', aib)
        # ib = ''.join(ib).replace('IB :', '').strip()
        # item['ib'] = ib
        # department=response.xpath('//a[contains(text(),"Visit the")]/../preceding-sibling::h3/text()').extract()
        # item['department']=''.join(department).strip()
        overview=response.xpath('//h3[contains(text(),"Why this")]|//h3[contains(text(),"Why this")]/following-sibling::*').extract()
        overview=remove_class(overview)
        item['overview_en']=overview

        # department=''.join(department)
        # if department=='Dentistry' or department=='Medicine' or department=='Veterinary Science':
        #     item['ielts_desc'] = '7.0 with minimum 7.0 in each component'
        #     item['ielts_l'] = '7.0'
        #     item['ielts_s'] = '7.0'
        #     item['ielts_r'] = '7.0'
        #     item['ielts_w'] = '7.0'
        #     item['ielts'] = '7.0'
        # elif department in ['Chemistry','Engineering','Electrical Engineering and Electronics','Computer Science','Earth Sciences','Ecology and Marine Biology','Mathematical Sciences','Physics','Ocean Sciences']:
        #     item['ielts_desc'] = '6.0 with minimum 5.5 in each component'
        #     item['ielts_l'] = '5.5'
        #     item['ielts_s'] = '5.5'
        #     item['ielts_r'] = '5.5'
        #     item['ielts_w'] = '5.5'
        #     item['ielts'] = '6.0'
        # else:
        #     item['ielts_desc'] = '6.5 with minimum 5.5 in each component'
        #     item['ielts_l'] = '5.5'
        #     item['ielts_s'] = '5.5'
        #     item['ielts_r'] = '5.5'
        #     item['ielts_w'] = '5.5'
        #     item['ielts'] = '6.5'

        # assessment_en=response.xpath('//h4[contains(text(),"Teaching and Learning")]/following-sibling::*').extract()
        # item['assessment_en']=remove_class(assessment_en)

        # print(item['ielts'])
        # if department!='':
        #     feexpath='//td/p[contains(text(),"'+str(department)+'")]/../following-sibling::td//text()|//td[contains(text(),"'+str(department)+'")]/following-sibling::td//text()'
        #     fee=self.feeRes.xpath(feexpath)
        #     item['tuition_fee']=getTuition_fee(fee)
        # yield item
        # print(item)
    def getRes(self,urls):
        return etree.HTML(requests.get(urls).content)
    def getTag(self,text):
        var=''
        for i in text:
            var+=etree.tostring(i,method='html',encoding='unicode')
        var=remove_class(var)
        return var