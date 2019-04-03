# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
import requests
from lxml import etree
class UniversityofyorkUSpider(scrapy.Spider):
    name = 'UniversityOfYork_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.york.ac.uk/study/undergraduate/courses/all?mode=&q=&level=undergraduate']

    def parse(self, response):
        urls=['https://www.york.ac.uk/study/undergraduate/courses/ba-archaeology-heritage/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-bioarchaeology/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-archaeology/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-actuarial-science-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-biotechnology-and-microbiology/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-archaeology/',
'https://www.york.ac.uk/study/undergraduate/courses/meng-computer-science-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-actuarial-science/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-accounting-business-finance-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-applied-social-science/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-accounting-business-finance-management-abfm/',
'https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-green-principles-york/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-chemistry-atmosphere-environment/',
'https://www.york.ac.uk/study/undergraduate/courses/meng-computer-science/',
'https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-atmosphere-environment-year-abroad/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-chemistry-green-principles/',
'https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-green-principles-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-green-principles-year-abroad/',
'https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-biological-medicinal-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-biological-medicinal-york/',
'https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-atmosphere-environment-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-atmosphere-environment-york/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-theoretical-physics-year-abroad/',
'https://www.york.ac.uk/study/undergraduate/courses/mphys-theoretical-physics-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/mphys-theoretical-physics/',
'https://www.york.ac.uk/study/undergraduate/courses/mphys-theoretical-physics-year-abroad/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-theoretical-physics/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-theoretical-physics-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-sociology-education/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-sociology-social-psychology/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-social-political-sciences-philosophy/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-social-political-sciences/',
'https://www.york.ac.uk/study/undergraduate/courses/msocw-social-work/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-sociology/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-social-policy-crime-criminal-justice/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-psychology-education/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-theatre-writing-directing-performance/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-social-policy-children/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-social-policy/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-politics-international-relations-placement/',
'https://www.york.ac.uk/language/undergraduate/courses/ba-spanish-linguistics-4year/',
'https://www.york.ac.uk/study/undergraduate/courses/mphys-physics-astrophysics-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-physics-philosophy/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-politics-placement/',
'https://www.york.ac.uk/psychology/prospective/undergraduate/mpsych/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-physics-philosophy-year-abroad/',
'https://www.york.ac.uk/study/undergraduate/courses/mphys-physics-philosophy/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-physics-astrophysics-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/mphys-physics-astrophysics-year-abroad/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-physics-astrophysics-year-abroad/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-physics-astrophysics/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-psychology/',
'https://www.york.ac.uk/study/undergraduate/courses/mphys-physics-astrophysics/',
'https://www.york.ac.uk/study/undergraduate/courses/mphys-physics-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-physics-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/mphys-physics-year-abroad/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-physics-year-abroad/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-physics-foundation-year/',
'https://www.york.ac.uk/study/undergraduate/courses/mphys-physics/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-physics/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-philosophy-politics/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-philosophy-linguistics/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-philosophy-politics-economics-ppe/',
'https://www.york.ac.uk/study/undergraduate/courses/mnurs-nursing-mental-health/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-nursing-mental-health/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-nursing-adult-harrogate-route/',
'https://www.york.ac.uk/study/undergraduate/courses/mnurs-nursing-adult/',
'https://www.york.ac.uk/electronic-engineering/undergraduate/courses/mtsfy/mtsfy_h662/',
'https://www.york.ac.uk/electronic-engineering/undergraduate/courses/eemts/eemts_h663/',
'https://www.york.ac.uk/electronic-engineering/undergraduate/courses/eemts/eemts_h664/',
'https://www.york.ac.uk/electronic-engineering/undergraduate/courses/eemts/eemts_h665/',
'https://www.york.ac.uk/electronic-engineering/undergraduate/courses/eemts/eemts_h666/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-nursing-child/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-molecular-cell-biology/',
'https://www.york.ac.uk/study/undergraduate/courses/mbiol-molecular-cell-biology/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-mathematics-physics-year-abroad/',
'https://www.york.ac.uk/study/undergraduate/courses/mmath-mphys-mathematics-physics/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-mathematics-physics/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-mathematics-europe/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-mathematics/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-marketing-industry/',
'https://www.cs.york.ac.uk/undergraduate/ug-courses/mmath-cs-industry/',
'https://www.cs.york.ac.uk/undergraduate/ug-courses/mmath-cs/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-marketing/',
'https://www.york.ac.uk/study/undergraduate/courses/llb-law/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-international-relations-placement/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-international-relations/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-interactive-media/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-human-geography-environment-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-human-geography-environment/',
'https://www.york.ac.uk/language/undergraduate/courses/ba-linguistics-french-3year/',
'https://www.york.ac.uk/language/undergraduate/courses/ba-linguistics-german-3year/',
'https://www.york.ac.uk/language/undergraduate/courses/ba-linguistics-italian-3year/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-linguistics/',
'https://www.york.ac.uk/language/undergraduate/courses/ba-linguistics-spanish-3year/',
'https://www.york.ac.uk/study/undergraduate/courses/menv-human-geography-environment/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-history-economics/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-history-of-art-abroad/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-history-of-art/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-history-french/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-italian-spanish-year-abroad/',
'https://www.york.ac.uk/language/undergraduate/courses/ba-italian-linguistics-4year/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-history-politics/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-historical-archaeology/',
'https://www.york.ac.uk/study/undergraduate/courses/mbiol-genetics/',
'https://www.york.ac.uk/language/undergraduate/courses/ba-german-linguistics-4year/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-history-philosophy/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-history-art-history/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-genetics/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-french-spanish-year-abroad/',
'https://www.york.ac.uk/language/undergraduate/courses/ba-french-linguistics-4year/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-french-german-year-abroad/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-french-italian-year-abroad/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-german-italian-year-abroad/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-german-spanish-year-abroad/',
'https://www.york.ac.uk/language/undergraduate/courses/ba-german-philosophy-4year/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-film-television-production/',
'https://www.york.ac.uk/study/undergraduate/courses/menv-environmental-science-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-environmental-science-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-environmental-science/',
'https://www.york.ac.uk/language/undergraduate/courses/ba-french-philosophy-4year/',
'https://www.york.ac.uk/study/undergraduate/courses/menv-environmental-geography-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-environmental-geography-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/menv-environmental-geography/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-environmental-geography/',
'https://www.york.ac.uk/study/undergraduate/courses/menv-environment-economics-ecology-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/menv-environment-economics-ecology/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-environment-economics-ecology-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-environment-economics-ecology/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-english-politics/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-english-linguistics/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-english-education/',
'https://www.york.ac.uk/study/undergraduate/courses/beng-electronic-computer-engineering-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/meng-electronic-computer-engineering-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/meng-electronic-computer-engineering/',
'https://www.york.ac.uk/study/undergraduate/courses/meng-electronic-communication-engineering-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/beng-electronic-communication-engineering-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/beng-electronic-communication-engineering/',
'https://www.york.ac.uk/electronic-engineering/undergraduate/courses/eemts/eemts_h661/',
'https://www.york.ac.uk/electronic-engineering/undergraduate/courses/eemts/eemts_h668/',
'https://www.york.ac.uk/study/undergraduate/courses/beng-electronic-engineering-nanotechnology/',
'https://www.york.ac.uk/language/undergraduate/courses/ba-english-language-linguistics/',
'https://www.york.ac.uk/study/undergraduate/courses/meng-electronic-communication-engineering/',
'https://www.york.ac.uk/study/undergraduate/courses/beng-electronic-engineering-nanotech-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/meng-electronic-engineering-nanotech-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/meng-ee-business-management-industry/',
'https://www.york.ac.uk/electronic-engineering/undergraduate/courses/eemts/eemts_h667/',
'https://www.york.ac.uk/study/undergraduate/courses/meng-electronic-engineering-nanotechnology/',
'https://www.york.ac.uk/electronic-engineering/undergraduate/courses/eemts/eemts_h669/',
'https://www.york.ac.uk/study/undergraduate/courses/beng-ee-business-management-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/meng-electronic-engineering-business-management/',
'https://www.york.ac.uk/study/undergraduate/courses/beng-electronic-engineering-business-management/',
'https://www.york.ac.uk/study/undergraduate/courses/beng-electronic-engineering-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/meng-electronic-engineering-industry/',
'https://www.york.ac.uk/electronic-engineering/undergraduate/courses/foundation_year/elec_eng_h604/',
'https://www.york.ac.uk/study/undergraduate/courses/meng-electronic-engineering/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-economics-politics/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-bsc-economics-econometrics/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-education/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-economics-philosophy/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-economics-mathematics/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-ecology/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-criminology/',
'https://www.york.ac.uk/study/undergraduate/courses/mbiol-ecology/',
'https://www.york.ac.uk/study/undergraduate/courses/meng-computer-science-with-cyber-security-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-curating-art-history/',
'https://www.york.ac.uk/study/undergraduate/courses/meng-computer-science-with-cyber-security/',
'https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-york/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-business-management-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-beng-computer-science/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-business-management-industry/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-business-management/',
'https://www.york.ac.uk/study/undergraduate/courses/ba-business-management/',
'https://www.york.ac.uk/study/undergraduate/courses/mbiol-biotechnology-and-microbiology/',
'https://www.york.ac.uk/study/undergraduate/courses/mbiomedsci-biomedical-sciences/',
'https://www.york.ac.uk/study/undergraduate/courses/mbiol-biology/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-biomedical-sciences/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-biology/',
'https://www.york.ac.uk/study/undergraduate/courses/mbiochem-biochemistry/',
'https://www.york.ac.uk/study/undergraduate/courses/bsc-biochemistry/',]
        urls=set(urls)
        for u in urls:
            yield scrapy.Request(url=u,callback=self.parsess,meta={'url':u})
    def parsess(self,response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['university']='University of York'
        print(response.url)
        # item['url']=response.meta['url']
        # alevel=response.xpath('//th[contains(text(),"A levels")]/following-sibling::td//text()').extract()
        # # print(alevel)
        # ib=response.xpath('//th[contains(text(),"International Baccalaureate")]/following-sibling::td//text()').extract()
        # # print(ib)
        # item['alevel']=remove_class(alevel)
        # item['ib']=remove_class(ib)
        tuition=response.xpath('//h4[contains(text(),"nternational fee")]/following-sibling::p/text()').extract()
        print(tuition)
        tui=re.findall('\d{2}\,\d{3}',''.join(tuition))
        item['tuition_fee']=''.join(tui).replace(',','').strip()
        if tui!=[]:
            yield item

        # yield item
    def parses(self, response):
        # print(response.url)
        pro_url=response.xpath('//td[@class="coursetitle"]/a/@href').extract()
        degree_name=response.xpath('//td[@class="detail"]/ul/li/abbr//text()').extract()
        programme=response.xpath('//td[@class="coursetitle"]/a//text()').extract()
        ucascode=response.xpath('//td[@class="code"]/text()').extract()
        for i,deg,pro,ucas in zip(pro_url,degree_name,programme,ucascode):
            yield scrapy.Request(url=i,callback=self.parse_main,meta={"degree_name":deg,"programme":pro,"ucascode":ucas})
    def parse_main(self,response):
        # print(response.url)
        # print(response.meta["degree_name"])
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'University of York'
        item['url'] = response.url
        item['location'] = 'York'

        ucascode=response.meta['ucascode'].strip()
        # print(ucascode)
        item['ucascode']=ucascode

        degree_name=response.meta['degree_name'].strip()
        item['degree_name']=degree_name

        programme=response.xpath('//div[@class="c-figure__content c-figure__content--left c-figure__content--half"]//h1/text()').extract()
        programme=''.join(programme).strip()
        # print(programme)
        if programme=='':
            # print(response.url)
            programme=response.xpath('//h1[@id="course-title"]/text()').extract()
            programme=''.join(programme).strip()

        programme=programme.replace(degree_name,'').strip()
        item['programme_en']=programme

        item['major_type1']=response.meta['programme']

        duration=response.xpath('//h4[contains(text(),"Length")]/following-sibling::p/text()|//table[@id="course-summary-table"]//tr/td//text()').extract()
        duration=clear_duration(duration)
        # print(duration)


        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']

        department=response.xpath('//h4[contains(text(),"Department")]/following-sibling::p/a/text()|//span[@class="org"]/span[1]/text()').extract()
        # print(department)
        department=''.join(department).strip()
        item['department']=department

        start_date=response.xpath('//h4[contains(text(),"Start date")]/following-sibling::p/text()').extract()
        start_date=tracslateDate(start_date)
        start_date=','.join(start_date)
        # print(start_date)
        item['start_date']=start_date

        alevel=response.xpath('//h4[contains(text(),"Typical offer")]/following-sibling::p/text()|//span[@id="course-entry"]/../text()').extract()
        alevel=''.join(alevel).replace('(','').replace(')','').strip()
        # print(alevel)
        item['alevel']=alevel

        tuition_fee=response.xpath('//h4[contains(text(),"International fees")]/following-sibling::p/text()').extract()
        # print(tuition_fee)
        tuition_fee=getTuition_fee(tuition_fee)
        # print(tuition_fee)
        if tuition_fee==0:
            # print(response.url)
            tuition_fee=self.get_tuitionfee(programme)
            # print(tuition_fee)
        item['tuition_fee']=tuition_fee
        item['tuition_fee_pre']='£'

        overview=response.xpath('//div[@class="o-grid__box o-grid__box--half o-grid__box--half@medium"]|//div[@id="course-overview-content"]').extract()
        overview=remove_class(overview)
        item['overview_en']=overview
        # print(overview)

        modules=response.xpath('//div[@class="o-grid__box o-grid__box--twothirds o-grid__box--full@medium"]|//div[@id="course-content-content"]').extract()
        modules=remove_class(modules)
        item['modules_en']=modules
        # print(modules)

        assessment=response.xpath('//div[@class="o-grid__box o-grid__box--half o-grid__box--half@medium o-grid__box--full@small"]|//div[@id="course-assessment-content"]').extract()
        assessment=remove_class(assessment)
        item['assessment_en']=assessment
        # print(assessment)

        career=response.xpath('//h3[contains(text(),"Career opp")]/following-sibling::*|//div[@id="careers"]|//div[@id="course-careers-content"]').extract()
        career=remove_class(career)
        item['career_en']=career
        # if career=='':
        #     print(response.url)

        ib=response.xpath('//th[contains(text(),"International Bacca")]/following-sibling::td//text()|'
                          '//a[contains(text(),"International Bacc")]/../following-sibling::div//text()|'
                          '//h3[contains(text(),"International Bac")]/following-sibling::div//text()').extract()
        ib=''.join(ib).strip()
        item['ib']=ib
        # if ib=='':
        #     print(response.url)

        ielts=response.xpath('//strong[contains(text(),"IELTS")]/../text()|//li[contains(text(),"IELTS")]//text()|//div[@id="entry"]').extract()
        ielts = get_ielts(ielts)
        if ielts != {} and ielts != []:
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            item['ielts'] = ielts['IELTS']

        EntryRequirement = response.xpath('//div[@id="entry"]').extract()
        TOEFL = re.findall('TOEFL[\s:.]*\d+,[a-zA-Z0-9, ]*', ''.join(EntryRequirement))
        TOEFL = ''.join(TOEFL)
        toefl = re.findall('\d{2,3}', TOEFL)
        # print(toefl)
        if len(toefl) == 2:
            toefl = list(map(int, toefl))
            item['toefl'] = max(toefl)
            item['toefl_l'] = min(toefl)
            item['toefl_w'] = min(toefl)
            item['toefl_r'] = min(toefl)
            item['toefl_s'] = min(toefl)
        elif len(toefl) == 4:
            item['toefl'] = toefl[0]
            item['toefl_l'] = toefl[2]
            item['toefl_w'] = toefl[1]
            item['toefl_r'] = toefl[3]
            item['toefl_s'] = toefl[1]
        elif len(toefl) == 5:
            item['toefl'] = toefl[0]
            item['toefl_l'] = toefl[2]
            item['toefl_w'] = toefl[1]
            item['toefl_r'] = toefl[3]
            item['toefl_s'] = toefl[4]

        require_chinese_en='<p>If you are leaving Senior Secondary School in China with a Senior Secondary School Graduation Certificate or Chinese University Entrance Examination (Gaokao) you will need to take an additional course before being able to apply for an undergraduate course at York. This could be A levels, the International Baccalaureate or a recognised <a href="/study/international/applying/foundation-pathways/">foundation course</a>.</p>'
        require_chinese_en=remove_class(require_chinese_en)
        item['require_chinese_en']=require_chinese_en

        apply_prece_en=['<h2><a href="/study/undergraduate/courses/">1. Choose a course</a></h2>',
"<p>Thorough research will help you find a course that is most suited to your needs and ambitions. Explore what's on offer at York.</p>",
'<h2><a href="/study/undergraduate/applying/entry/">2. Check the entry requirements</a></h2>',
'<p>Before you apply you should check that you meet the entry requirements for your chosen course.</p>',
"<p>If you're a non-native English speaking applicant you must provide evidence of your English language ability. Check our&nbsp;<a>English language requirements</a>.</p>",
'<h2><a href="/study/undergraduate/visits/open-days/">3. Meet us at an Open Day</a></h2>',
'<p>Coming to an Open Day is a great way to find out what studying and living in York is really like.</p>',
'<h2><a href="/study/undergraduate/applying/how-to-apply/">4. Apply via UCAS</a></h2>',
"<p>All applications must be made through UCAS (the Universities and Colleges Admissions Service). We'll explain how the application process works.</p>",
'<p>Some of our courses are also available through <a>UCAS Extra</a>&nbsp;(ucas.com).</p>',
'<h2><a href="/study/undergraduate/applying/after/">5. After you apply</a></h2>',
"<p>We'll guide you through what happens next, including how to track your application and how and when to apply for accommodation.</p>",
'<h2>Admissions policy</h2>',
'<p>We consider all&nbsp;applications&nbsp;in a fair, transparent and consistent way.&nbsp;</p>',]
        apply_prece_en=remove_class(apply_prece_en)
        item['apply_proces_en']=apply_prece_en


        # print(item)
        # yield item
    def get_tuitionfee(self,programme):
        # print(response.url)
        responses=requests.get('https://www.york.ac.uk/study/undergraduate/fees-funding/international/').content
        responses=etree.HTML(responses)
        fee_xpath='//strong[contains(text(),"%s")]/../text()' % programme
        fee=responses.xpath(fee_xpath)
        tuition_fee=getTuition_fee(fee)
        return tuition_fee
