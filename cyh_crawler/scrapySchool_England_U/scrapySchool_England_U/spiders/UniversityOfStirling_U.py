# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
# from selenium import webdriver
class UniversityofstirlingUSpider(scrapy.Spider):
    name = 'UniversityOfStirling_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/']

    def parse(self, response):
        urls=['https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/modern-languages/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/modern-languages/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/modern-languages/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/modern-languages/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/modern-languages/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/modern-languages/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/aquaculture/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-primary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-primary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-primary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-primary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-primary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-primary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-primary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-primary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-primary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-primary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-primary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-primary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-primary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-primary/',
'https://www.stir.ac.uk/courses/ug/stirling-management-school/accountancy/',
'https://www.stir.ac.uk/courses/ug/stirling-management-school/accountancy-finance/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/applied-computing/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/aquaculture/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/applied-biological-sciences/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/applied-mathematics/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/biology/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/business-computing/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/cell-biology/',
'https://www.stir.ac.uk/courses/ug/stirling-management-school/business-studies/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/computing-science/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/animal-biology/',
'https://www.stir.ac.uk/courses/ug/social-sciences/criminology-social-policy/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/conservation-biology-management/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/digital-media/',
'https://www.stir.ac.uk/courses/ug/social-sciences/criminology-sociology/',
'https://www.stir.ac.uk/courses/ug/stirling-management-school/economics/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/ecology/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/environmental-geography-outdoor-education/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/environmental-science-bsc/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/environmental-science-outdoor-education/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/english-studies/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/environmental-science-msci/',
'https://www.stir.ac.uk/courses/ug/stirling-management-school/finance/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/film-media/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/heritage-tourism/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/geography-environmental-geography/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/history/',
'https://www.stir.ac.uk/courses/ug/stirling-management-school/human-resource-management/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/journalism-studies/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/law-ba-programmes/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/law-llb/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/psychology/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/french/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/marine-biology/',
'https://www.stir.ac.uk/courses/ug/stirling-management-school/management/',
'https://www.stir.ac.uk/courses/ug/stirling-management-school/marketing/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/mathematics/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/religion/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/modern-languages/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/religion/',
'https://www.stir.ac.uk/courses/ug/health-sciences/nursing-adult/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/religion/',
'https://www.stir.ac.uk/courses/ug/health-sciences/nursing-mental-health/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/religion/',
'https://www.stir.ac.uk/courses/ug/health-sciences/nursing-mental-health-with-honours/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/religion/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/int-mgt-studies-euro-languages-society/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/religion/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/philosophy/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/religion/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/politics/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/religion/',
'https://www.stir.ac.uk/courses/ug/health-sciences/nursing-adult-with-honours/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/religion/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/politics-international-politics/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/politics-philosophy-and-economics-ppe/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/stirling-management-school/professional-accountancy/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/stirling-management-school/retail-marketing/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/scottish-history/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/psychology/',
'https://www.stir.ac.uk/courses/ug/social-sciences/social-work/',
'https://www.stir.ac.uk/courses/ug/social-sciences/sociology-social-policy/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/religion/',
'https://www.stir.ac.uk/courses/ug/natural-sciences/software-engineering/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/spanish-latin-american-studies/',
'https://www.stir.ac.uk/courses/ug/sport/sport-exercise-science/',
'https://www.stir.ac.uk/courses/ug/stirling-management-school/sport-business-management/',
'https://www.stir.ac.uk/courses/ug/stirling-management-school/sustainable-events-management/',
'https://www.stir.ac.uk/courses/ug/sport/sports-studies/',
'https://www.stir.ac.uk/courses/ug/arts-humanities/law-ba-programmes/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',
'https://www.stir.ac.uk/courses/ug/social-sciences/education-secondary/',]
        urls=set(urls)
        for u in urls:
            yield scrapy.Request(url=u,callback=self.parsesss,meta={'url':u})

    def parsesss(self, response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['university']='University of Stiriling'
        item['url']=response.meta['url']
        print(response.url)
        alevel_1 = response.xpath('//a[contains(text(),"Year 1 entry")]/text()|//a[contains(text(),"Year 1 entry")]/following-sibling::div/p/strong[contains(text(),"GCE")]/..//text()').extract()
        alevel_2 = response.xpath('//a[contains(text(),"Year 2 entry")]/text()|//a[contains(text(),"Year 2 entry")]/following-sibling::div/p/strong[contains(text(),"GCE")]/..//text()').extract()
        alevel = '\n'.join(alevel_1) + '\n' + '\n'.join(alevel_2)
        # print(alevel)
        ib1 = response.xpath('//a[contains(text(),"Year 1 entry")]/text()|//a[contains(text(),"Year 1 entry")]/following-sibling::div/p/strong[contains(text(),"IB Diploma")]/..//text()').extract()
        ib2 = response.xpath('//a[contains(text(),"Year 2 entry")]/text()|//a[contains(text(),"Year 2 entry")]/following-sibling::div/p/strong[contains(text(),"IB Diploma")]/..//text()').extract()
        ib = '\n'.join(ib1) + '\n' + '\n'.join(ib2)
        # print(ib)
        item['alevel']=alevel
        item['ib']=ib

        yield item
    # def parses(self, response):
    #     item=get_item1(ScrapyschoolEnglandItem)
    #     item['url']=response.url
    #     item['university']='University of Stiriling'
    #     print(response.url)
    #     dirver = webdriver.Chrome(r'C:\Users\delsk21099\Desktop\chromedriver.exe')
    #     dirver.get(response.url)
    #     dirver.maximize_window()
    #     js = "var q=document.documentElement.scrollTop=800"
    #     dirver.execute_script(js)
    #     dirver.find_element_by_id('ug-course-tabs__course-details-label').click()
    #     js = "var q=document.documentElement.scrollTop=1300"
    #     dirver.execute_script(js)
    #     dirver.implicitly_wait(100)
    #     dirver.find_element_by_id("course-modules-container__accordion").find_element_by_name("li").find_element_by_name("a").get_attribute("aria-selected")
    #     print("===", dirver)
    #     # js = """var q=document.getElementById(\"course-modules-container__accordion\")[0].children;
    #     # for
    #     # q.aria-selected = \"true\";"""
    #     # 执行js
    #     # dirver.execute_script(js)
    #
    #     # time.sleep(15)
    #     seme=dirver.find_element_by_xpath('//ul[@id="course-modules-container__accordion"]/li/a[contains(@id,"accordion-label")]').get_attribute('text')
    #     print(seme)
    #     modules = dirver.find_element_by_xpath('//ul[@id="course-modules-container__accordion"]').get_attribute('outerHTML')
    #     print(remove_class(modules))
    #     # item['modules_en']=remove_class(modules)
    #     #class="accordion-item c-course-modules__accordion-item"
    #
    #     # time.sleep(3)
    #     dirver.close()
    #
    #     alevel_1 = response.xpath(
    #         '//a[contains(text(),"Year 1 entry")]/text()|//a[contains(text(),"Year 1 entry")]/following-sibling::div/p/strong[contains(text(),"GCE")]/..//text()').extract()
    #     # print(alevel_1)
    #     alevel_2 = response.xpath(
    #         '//a[contains(text(),"Year 2 entry")]/text()|//a[contains(text(),"Year 2 entry")]/following-sibling::div/p/strong[contains(text(),"GCE")]/..//text()').extract()
    #     # print(alevel_2)
    #     alevel = '\n'.join(alevel_1) + '\n' + '\n'.join(alevel_2)
    #     item['alevel'] = alevel
    #
    #     # yield item
    def parsess(self, response):
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        programme = response.xpath('//h1/text()').extract()
        programme = ''.join(programme).strip()
        # print(programme)
        degree_type = response.xpath('//span[contains(text(),"Award")]/../text()').extract()
        degree_name = ''.join(degree_type).strip()
        # print(degree_name)
        item['degree_name'] = degree_name
        programme=programme.replace(degree_name.replace(',','/'),'').strip()
        # print(programme)
        university = 'University of Stirling'
        item['university'] = university
        item['url'] = response.url
        item['location'] = 'Stirling'
        item['programme_en'] = programme
        modules=response.xpath('//div[@id="ug-course-tabs__course-details"]/div[@class="c-wysiwyg-content"]').extract()
        modules=remove_class(modules)
        # print(modules)
        item['modules_en']=modules

        overview = response.xpath('//div[@id="ug-course-tabs__overview"]').extract()
        overview = remove_class(overview)
        # print(overview)
        item['overview_en'] = overview
        entry_requirement = response.xpath('//div[@id="ug-course-tabs__entry-requirements"]').extract()
        entry_requirement = remove_class(entry_requirement)
        # print(entry_requirement)
        item['rntry_requirements'] = entry_requirement
        IELTS = response.xpath('//li[contains(text(),"IELTS")]//text()').extract()
        IELTS = ''.join(IELTS).strip()
        item['ielts_desc'] = IELTS
        TOEFL = response.xpath('//li[contains(text(),"TOEFL")]//text()').extract()
        TOEFL = ''.join(TOEFL).strip()
        item['toefl_desc'] = TOEFL
        IELTSs = re.findall('\d\.\d', IELTS)
        if len(IELTSs) == 2:
            item['ielts'] = max(IELTSs)
            item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w'] = min(IELTSs), min(IELTSs), min(
                IELTSs), min(IELTSs)
        TOEFLs = re.findall('\d{2,3}', TOEFL)
        if len(TOEFLs) == 2:
            item['toefl'] = max(TOEFLs)
            item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w'] = min(TOEFLs), min(TOEFLs), min(
                TOEFLs), min(TOEFLs)
        tuition_fee = response.xpath('//*[contains(text(),"£")]/text()').extract()
        tuition_fee = getTuition_fee(tuition_fee)
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = '£'
        durations = response.xpath('//span[contains(text(),"Duration")]/../text()').extract()
        duration = clear_duration(durations)['duration']
        duration_per = clear_duration(durations)['duration_per']
        item['duration'] = duration
        item['duration_per'] = duration_per
        start_date=response.xpath('//span[contains(text(),"tart date")]/../text()').extract()
        start_date=tracslateDate(start_date)
        start_date=','.join(start_date)
        # print(start_date)
        item['start_date']=start_date
        ucascode=response.xpath('//span[@id="course-ucas-codes"]/text()').extract()
        ucascode=''.join(ucascode).strip()
        item['ucascode']=ucascode
        alevel=response.xpath('//strong[contains(text(),"level")]/../text()').extract()
        alevel=','.join(alevel).strip()
        item['alevel']=alevel
        ib=response.xpath('//strong[contains(text(),"IB")]/../text()').extract()
        ib=''.join(ib).strip()
        item['ib']=ib

        china=['<p>Direct Entry to 1st Year:</p>'
'<p>• Chinese Senior Secondary School Graduation Certificate with 75% overall</p>'
'<p>• Chinese University Entrance Examination (Gaokao) with a score of 500</p>'
'<p>Advanced Entry to 2nd Year:</p>'
'<p>School leavers with a Gaokao/Zhongkao are required to complete a Foundation Year for entry to the University.</p>']
        item['require_chinese_en']=remove_class(china)
        assessment=response.xpath('//a[contains(text(),"Assessment")]/following-sibling::*').extract()
        item['assessment_en']=remove_class(assessment).replace('data-tab-content','')

        career=response.xpath('//div[@id="ug-course-tabs__after-graduate"]').extract()
        # if career==[]:
        #     print(response.url)
        # else:
        #     print('GG')
        item['career_en']=remove_class(career)

        # print(item)
        yield item

