# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem

class CoventryuniversityUSpider(scrapy.Spider):
    name = 'CoventryUniversity_U'
    allowed_domains = ['coventry.ac.uk']
    start_urls=['']

    def parse(self, response):
        urls=['https://www.coventry.ac.uk/london/course-structure/undergraduate-new/2018-19/international-finance-and-accounting-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/london/course-structure/undergraduate-new/2018-19/international-fashion-management-and-marketing-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/international-economics-and-trade-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/interior-architecture-and-design-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/international-disaster-management-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/international-fashion-business-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/information-technology-for-business-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/international-business-management-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/cus/course-structure/hnc-hnd-degree/2018-19/health-social-care/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/history-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/human-biosciences-bsc/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/illustration-and-animation-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/geography-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/graphic-design-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/london/course-structure/undergraduate-new/2018-19/global-business-management-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/geography-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/games-art-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/illustration-and-graphics-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/history-and-politics-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/geography-and-natural-hazards-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/games-technology-bsc/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/food-and-nutrition-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/food-safety-inspection-and-control-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/fine-art-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/financial-economics-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/forensic-investigations-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/fine-art-and-illustration-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/finance-and-investment-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/finance-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/french-and-international-relations-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/cuc/course-structure/hnc-hnd-degree/2018-19/financial-services/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/ethical-hacking-and-cybersecurity-bsc-/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/european-business-management-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/english-and-teaching-english-as-a-foreign-language-tefl-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/english-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/english-and-creative-writing-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/enterprise-and-entrepreneurship-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/english-and-journalism-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/cus/course-structure/hnc-hnd-degree/2018-19/electro-mechanical-engineering/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/electrical-and-electronic-engineering-mengbeng/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/economics-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/cuc/course-structure/hnc-hnd-degree/2018-19/childhood/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/event-management-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/disaster-management-and-emergency-planning-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/digital-media-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/digital-marketing-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/fashion-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/cuc/course-structure/hnc-hnd-degree/2018-19/electro-mechanical-engineering/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/hls-nhs/dietetics-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/cuc/course-structure/hnc-hnd-degree/2018-19/digital-technology/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/electronic-engineering-beng-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/criminology-and-law-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/criminology-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/cuc/course-structure/hnc-hnd-degree/2018-19/counselling/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/computing-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/counselling-coaching-and-mentoring-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/criminal-psychology-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/civil-engineering-mengbeng/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/construction-management-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/computer-science-mscibsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/computer-hardware-and-software-engineering-beng/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/biomedical-scienceapplied-biomedical-science-bsc/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/civil-engineering-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/cus/course-structure/hnc-hnd-degree/2018-19/science/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/criminology-and-psychology-ba/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/building-services-engineering-bsc/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/building-surveying-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/biological-and-forensic-science-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/automotive-engineering-mengbeng-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/aviation-management-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/architecture-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/architectural-technology-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/automotive-and-transport-design-mdesba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/aerospace-technology-beng-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/analytical-chemistry-and-forensic-science-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/aerospace-systems-engineering-beng-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/advertising-and-marketing-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/london/course-structure/undergraduate-new/2019-20/applied-global-marketing-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/cuc/course-structure/hnc-hnd-degree/2018-19/science/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/accountancy-and-finance-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/accountancy-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/civil-and-environmental-engineering-mengbeng/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/civil-and-structural-engineering-mengbeng/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/business-law-llb-hons/?visitor=international',
'https://www.coventry.ac.uk/cus/course-structure/hnc-hnd-degree/2018-19/management/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/business-economics-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/business-and-marketing-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/business-and-hr-management-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/business-and-finance-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/sports-therapy-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/childhood-and-youth-studies-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/theatre-and-professional-practice-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/business-administration-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/sport-management-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/sport-and-exercise-psychology-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/hls-nhs/children-and-young-peoples-nursing-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/sport-marketing-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/hls-nhs/social-work-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/business-management-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/sociology-and-criminology-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/social-sciences-bsc/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/-quantity-surveying-and-commercial-management-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/spanish-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/sport-and-exercise-science-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/psychology-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/cuc/course-structure/hnc-hnd-degree/2018-19/public-health/?visitor=international',
'https://www.coventry.ac.uk/cus/course-structure/hnc-hnd-degree/2018-19/primary-education/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/sociology-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/product-design-ba/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/politics-ba/?visitor=international',
'https://www.coventry.ac.uk/cus/course-structure/hnc-hnd-degree/2018-19/policing/?visitor=international',
'https://www.coventry.ac.uk/cuc/course-structure/hnc-hnd-degree/2018-19/accounting/?visitor=international',
'https://www.coventry.ac.uk/cuc/course-structure/hnc-hnd-degree/2018-19/policing/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/hls-nhs/physiotherapy-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/photography-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/cus/course-structure/hnc-hnd-degree/2018-19/public-health/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/oil-gas-and-energy-management-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/nutrition-and-health-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/hls-nhs/occupational-therapy-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/music-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/music-technology-bsc/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/media-production-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/HLS/medical-and-pharmacological-sciences-bsc/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/motorsport-engineering-mengbeng-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/media-and-communications-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/mechanical-engineering-mengbeng-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/mathematics-and-data-analytics-mscibsc/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/mathematics-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fbl/marketing-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/mathematics-and-statistics-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/cuc/course-structure/hnc-hnd-degree/2018-19/marketing/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/multimedia-computing-bsc/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/manufacturing-engineering-mengbeng-hons/?visitor=international',
'https://www.coventry.ac.uk/cuc/course-structure/hnc-hnd-degree/2018-19/management/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/eec/mathematics-and-physics-bsc-hons/?visitor=international',
'https://www.coventry.ac.uk/cus/course-structure/hnc-hnd-degree/2018-19/marketing/?visitor=international',
'https://www.coventry.ac.uk/cul/course-structure/hnc-hnd-degree/2018-19/law/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/languages-for-international-business-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/journalism-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/fah/international-relations-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/international-law-llb-hons/?visitor=international',
'https://www.coventry.ac.uk/cuc/course-structure/hnc-hnd-degree/2018-19/law-practice/?visitor=international',
'https://www.coventry.ac.uk/london/course-structure/undergraduate-new/2018-19/international-hospitality-and-tourism-management-ba-hons/?visitor=international',
'https://www.coventry.ac.uk/course-structure/UG/2018-19/law-llb-hons/?visitor=international',]
        urls=set(urls)
        for u in urls:
            yield scrapy.Request(url=u,callback=self.parsesss,meta={'url':u})
    def parsesss(self,response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.meta['url']
        item['university']='Coventry University'


    def parses(self, response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = "Coventry University"
        item['url'] = response.url.replace('?visitor=uk','?visitor=international')
        ucascode=response.xpath('//h5[contains(text(),"Course code")]/../following-sibling::div[1]//text()').extract()
        if ucascode==[]:
            print(response.url)
        else:
            print(''.join(ucascode).strip())
        # for i in urllist:
        #     fullurl = 'https://www.coventry.ac.uk' + i + '?visitor=international'
        #     yield scrapy.Request(fullurl, callback=self.parses)
    def parsess(self, response):
        print(response.url)
        item = get_item1(ScrapyschoolEnglandItem)
        item['university'] = "Coventry University"
        item['url'] = response.url
        item['location'] = 'Coventry'
        item['tuition_fee_pre'] = '£'
        progremme = response.xpath('//h2[@class="padded-multiline"]//text()').extract()
        progremme = ''.join(progremme).strip()
        # print(progremme)

        degree_name = re.findall('[A-Z]+[a-z]*\s\(Hons\)', progremme)
        # print(degree_name)
        degree_name = ''.join(degree_name)
        item['degree_name'] = degree_name
        progremme=progremme.replace(degree_name,'').strip()
        item['programme_en'] = progremme
        # print(progremme)
        # print(degree_name)


        duration = response.xpath(
            '//h5[contains(text(),"Study options")]/../following-sibling::div[1]//text()').extract()
        # print(duration)
        # print(clear_duration(duration))
        item['duration'] = clear_duration(duration)['duration']
        item['duration_per'] = clear_duration(duration)['duration_per']

        fee = response.xpath('//h5[contains(text(),"Fee")]/../following-sibling::div[1]//text()').extract()
        tuition_fee = getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee

        start_date = response.xpath('//h5[contains(text(),"Start")]/../following-sibling::div[1]//text()').extract()
        # print(start_date)
        start_date = tracslateDate(start_date)
        # print(start_date)
        start_date = ','.join(start_date)
        item['start_date'] = start_date

        deparment = response.xpath('//h5[contains(text(),"Faculty")]/../following-sibling::div[1]//text()').extract()
        deparment = ' '.join(deparment).strip()
        # print(deparment)
        item['department'] = deparment

        overview = response.xpath('//div[@id="overview-tab-pane"]/div[@class="container"]').extract()
        overview = clear_same_s(overview)
        overview = remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        modules = response.xpath('//h2[contains(text(),"Modules")]/following-sibling::*').extract()
        modules = clear_same_s(modules)
        modules = remove_class(modules)
        # print(modules)
        item['modules_en'] = modules

        career = response.xpath('//div[@id="career-tab-pane"]').extract()
        career = clear_same_s(career)
        career = remove_class(career)
        # print(career)
        item['career_en'] = career

        rntry_requirement = response.xpath('//div[@id="offerInfo-international"]').extract()
        rntry_requirement = clear_same_s(rntry_requirement)
        rntry_requirement = remove_class(rntry_requirement)
        ielts = get_ielts(rntry_requirement)
        # print(ielts)
        ielts_desc=response.xpath('//strong[contains(text(),"English as a Foreign Language")]/../text()').extract()
        item['ielts_desc']=''.join(ielts_desc).strip()
        if ielts != {} and ielts != []:
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            item['ielts'] = ielts['IELTS']
        item['require_chinese_en'] = rntry_requirement