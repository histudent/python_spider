# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
class ManchestermetropolitanuniversityUSpider(scrapy.Spider):
    name = 'ManchesterMetropolitanUniversity_U'

    start_urls = ['https://www2.mmu.ac.uk/study/undergraduate/courses/subject-areas/']
    def parse(self, response):
        urls=['https://www2.mmu.ac.uk/study/undergraduate/course/mbiol-zoology/',
'https://www2.mmu.ac.uk/study/undergraduate/course/bsc-physical-geography-with-option-to-study-overseas/QD',
'https://www2.mmu.ac.uk/study/undergraduate/course/mbiol-biology/',
'https://www2.mmu.ac.uk/study/undergraduate/course/mgeog-geography/',
'https://www2.mmu.ac.uk/study/undergraduate/course/ba-education-studies-early-years-specialism/',
'https://www2.mmu.ac.uk/study/undergraduate/course/ba-bsc-criminology-psychology/',]
        urls=set(urls)
        for u in urls:
            yield scrapy.Request(url=u,callback=self.parses,meta={'url':u})
    def parses(self, response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'Manchester Metropolitan University'
        item['url'] = response.meta['url']
        alevel=response.xpath('//h4[contains(text(),"UCAS tariff")]/following-sibling::p[2]/text()').extract()
        ib=response.xpath('//h4[contains(text(),"International Baccalaureate points")]/following-sibling::text()[1]').extract()
        item['alevel']=remove_class(alevel)
        item['ib']=remove_class(ib)
        yield item

    def parsess(self, response):
        pro_list=response.xpath('//li[@class="listing--results__item"]/a/@href').extract()
        full_url='https://www2.mmu.ac.uk/study/undergraduate/courses/subject-areas/'
        # pro_list=['https://www2.mmu.ac.uk/study/undergraduate/course/ba-three-dimensional-design/', 'https://www2.mmu.ac.uk/study/undergraduate/course/bsc-specialist-community-public-health-nursing-health-visiting-or-school-nursing/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-english-and-multimedia-journalism/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-teaching-english-to-speakers-of-other-languages-tesol-with-a-minor-route-language/', 'https://www2.mmu.ac.uk/study/undergraduate/course/bsc-secondary-mathematics-education-with-qts/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-teaching-english-to-speakers-of-other-languages-tesol-spanish/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-sports-marketing-management/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-philosophy-politics/', 'https://www2.mmu.ac.uk/study/undergraduate/course/llb-hons-part-time/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-teaching-english-to-speakers-of-other-languages-tesol-french/', 'https://www2.mmu.ac.uk/study/undergraduate/course/bsc-speech-and-language-therapy-foundation-year/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-philosophy/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-philosophy-sociology/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-economics-and-finance-joint-honours/', 'https://www2.mmu.ac.uk/study/undergraduate/course/bsc-psychology-with-foundation-year/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-sustainable-performance-management-cima/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-accounting-top-up/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-accounting-and-finance/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-ethics-religion-philosophy/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-history-philosophy/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-history-and-philosophy-degrees-with-a-foundation-year-stream-a/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-international-relations/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-history-international-relations/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-history-politics/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-international-relations-philosophy/', 'https://www2.mmu.ac.uk/study/undergraduate/course/bsc-physiotherapy/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-english-politics/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-criminology-politics/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-english-degrees-with-a-foundation-year-stream-b-combined-honours-politics-or-philosophy/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-spanish-studies/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-spanish-with-a-minor-route-language/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-economics-politics/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-international-relations-with-a-minor-route-language/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-international-relations-spanish/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-english-philosophy/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-international-business-french/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-international-relations-french/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-international-business-spanish/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-multimedia-journalism-with-a-minor-route-language/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-french-with-a-minor-route-language/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-french-and-spanish/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-french-studies/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-english-with-a-minor-route-language/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-languages-degrees-with-a-foundation-year-stream-c-international-relations-with-a-language/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-business-with-a-minor-route-language/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-business-spanish/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-english-french/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-english-spanish/', 'https://www2.mmu.ac.uk/study/undergraduate/course/llb-law-with-a-foundation-year/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-business-french/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-business-management-with-law/', 'https://www2.mmu.ac.uk/study/undergraduate/course/bsc-forensic-psychology/', 'https://www2.mmu.ac.uk/study/undergraduate/course/bsc-speech-and-language-therapy/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-teaching-english-to-speakers-of-other-languages-tesol-and-linguistics/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-international-business-with-a-minor-route-language/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-linguistics-with-a-minor-route-language/', 'https://www2.mmu.ac.uk/study/undergraduate/course/llb-hons/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-languages-degrees-with-a-foundation-year-stream-b-french-spanish-linguistics-tesol-minor-languages/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-languages-degrees-with-a-foundation-year-stream-a-linguistics-and-language-combinations-with-english/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-english-teaching-english-to-speakers-of-other-languages-tesol/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-english-linguistics/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-linguistics/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-linguistics-spanish/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-international-business-marketing/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-business-marketing/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-business-enterprise-marketing/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-advertising-and-brand-management/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-public-relations-and-marketing/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-primary-education-with-mathematics-with-qts/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-linguistics-french/', 'https://www2.mmu.ac.uk/study/undergraduate/course/mmath-mathematics/', 'https://www2.mmu.ac.uk/study/undergraduate/course/marketing-management-foundation-year/', 'https://www2.mmu.ac.uk/study/undergraduate/course/bsc-mathematics/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-marketing-management/', 'https://www2.mmu.ac.uk/study/undergraduate/course/ba-integrated-health-and-social-care-with-foundation-year/']
        for i in pro_list:
            i=full_url+i
            yield scrapy.Request(url=i,callback=self.parse_list)
    def parse_list(self,response):
        # print(response.url)
        pro_url=response.xpath('//li[@class="listing--results__item"]/a/@href').extract()
        # print(pro_url)
        # print(len(pro_url))
        # self.nums=self.nums+int(len(pro_url))
        # print(self.nums)
        for j in pro_url:
            fullurl='https://www2.mmu.ac.uk'+j
            yield scrapy.Request(url=fullurl,callback=self.parses)
    def pars(self,response):
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'Manchester Metropolitan University'
        item['url'] = response.url
        item['location'] = 'Manchester'
        degree_name = response.xpath('//h1/span/text()').extract()
        degree_name = ''.join(degree_name)
        item['degree_name'] = degree_name
        programme = response.xpath('//h1/text()').extract()
        programme = ''.join(programme).strip()
        item['programme_en'] = programme
        # print(degree_name)
        # print(programme)

        overview = response.xpath('//h2[contains(text(),"Overview")]/following-sibling::article').extract()
        overview = remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        career = response.xpath('//h2[contains(text(),"Career")]/following-sibling::p').extract()
        career = remove_class(career)
        item['career_en'] = career

        rntry=['<h4 class="detail__subsubheader">Foundation Year</h4>',
'<p>Senior High School Diploma ("Gao san") or Chinese University Entrance Examination with good grades</p>',
'<h4 class="detail__subsubheader">Undergraduate Courses</h4>',
'<p>Students who have successfully completed the first year at university in China with good grades can be considered for direct entry to undergraduate programmes. Students who hold Diplomas from Specialist Colleges ("Zhongzhan") with good grades may be considered for direct entry to undergraduate programmes. Holders of SQA / BTEC diplomas or Chinese 3 year diplomas ("Dazhuan" or "Zhuanke") may be eligible for second or third year entry to an undergraduate degree.</p>',
]
        rntry=remove_class(rntry)
        item['require_chinese_en']=rntry


        modules = response.xpath('//h2[contains(text(),"Course")]/following-sibling::div').extract()
        modules = remove_class(modules)
        item['modules_en'] = modules
        # print(modules)

        # fee = response.xpath('//*[contains(text(),"£")]//text()').extract()
        # tuition = getTuition_fee(fee)
        # print(tuition)
        item['tuition_fee'] = '15000'
        item['tuition_fee_pre'] = '£'

        texts=response.xpath('//h2[contains(text(),"Entry requirements")]/../text()').extract()
        # print(texts)
        texts=''.join(texts).strip()
        ib=re.findall('\d{2}',texts)
        ielts=re.findall('\d\.\d.*',texts)
        # print(ib)
        # print(ielts)
        item['ielts_desc']=''.join(ielts).strip()
        ielts=get_ielts(ielts)
        try:
            if ielts != [] and ielts != {}:
                item['ielts_l'] = ielts['IELTS_L']
                item['ielts_s'] = ielts['IELTS_S']
                item['ielts_r'] = ielts['IELTS_R']
                item['ielts_w'] = ielts['IELTS_W']
                item['ielts'] = ielts['IELTS']
        except:
            pass
        item['ib']=''.join(ib).strip()

        turation = response.xpath('//li[contains(text(),"Length")]/span//text()').extract()
        duration = clear_duration(turation)

        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']

        start_date = response.xpath('//li[contains(text(),"Start")]/span//text()').extract()
        # print(start_date)
        start_date = tracslateDate(start_date)
        # print(start_date)
        start_date = ','.join(start_date)
        item['start_date'] = start_date
        item['department'] = ''.join(response.xpath('//span[@id="department_name"]/text()').extract()).strip()

        ucascode=response.xpath('//h4[contains(text(),"UCAS code")]/following-sibling::p[2]/text()').extract()
        ucascode=''.join(ucascode).strip()
        item['ucascode']=ucascode[0:5]

        alevel=response.xpath('//h4[contains(text(),"tariff points/grades")]/following-sibling::p[position()<=2]//text()').extract()
        # if alevel==[]:
        #     print(response.url)
        # else:
        #     print(alevel)
        item['alevel']=remove_class(alevel)
        if response.status == 404:
            print("****404****")
            with open("errorurl.txt", 'a+') as f:
                f.write(response.url + "\n")
        else:
            yield item

