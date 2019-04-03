# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem

class StaffordshireuniversityUSpider(scrapy.Spider):
    name = 'StaffordshireUniversity_U'
    # allowed_domains = ['a.b']
    start_urls = ['http://search.staffs.ac.uk/s/search.html?collection=courses&meta_V_and=undergraduate&query=&meta_t_and=&f.Mode+of+attendance%7CM=full-time']

    def parse(self, response):
        urls=['http://www.staffs.ac.uk/course/3d-designer-maker-ceramics-ba',
'http://www.staffs.ac.uk/course/3d-designer-maker-craft-ba',
'http://www.staffs.ac.uk/course/3d-designer-maker-jewellery-fashion-ba',
'http://www.staffs.ac.uk/course/accounting-finance-ba',
'http://www.staffs.ac.uk/course/accounting-finance-ba',
'http://www.staffs.ac.uk/course/accounting-finance-ba',
'http://www.staffs.ac.uk/course/acting-screen-performance-ba',
'http://www.staffs.ac.uk/course/acting-theatre-arts-ba',
'http://www.staffs.ac.uk/course/advertising-film-music-video-production-ba',
'http://www.staffs.ac.uk/course/aeronautical-engineering-bsc',
'http://www.staffs.ac.uk/course/aeronautical-engineering-bsc',
'http://www.staffs.ac.uk/course/animation-ba',
'http://www.staffs.ac.uk/course/automotive-engineering-beng-meng',
'http://www.staffs.ac.uk/course/automotive-engineering-beng-meng',
'http://www.staffs.ac.uk/course/automotive-engineering-beng-meng',
'http://www.staffs.ac.uk/course/biological-science-bsc-msci',
'http://www.staffs.ac.uk/course/biological-science-bsc-msci',
'http://www.staffs.ac.uk/course/biological-science-bsc-msci',
'http://www.staffs.ac.uk/course/biological-science-bsc-msci',
'http://www.staffs.ac.uk/course/biomedical-science-bsc-msci',
'http://www.staffs.ac.uk/course/biomedical-science-bsc-msci',
'http://www.staffs.ac.uk/course/biomedical-science-bsc-msci',
'http://www.staffs.ac.uk/course/business-information-technology-bsc',
'http://www.staffs.ac.uk/course/business-information-technology-bsc',
'http://www.staffs.ac.uk/course/business-information-technology-bsc',
'http://www.staffs.ac.uk/course/business-management-ba',
'http://www.staffs.ac.uk/course/business-management-ba',
'http://www.staffs.ac.uk/course/business-management-ba',
'http://www.staffs.ac.uk/course/cartoon-comic-arts-ba',
'http://www.staffs.ac.uk/course/cgi-visual-effects-bsc',
'http://www.staffs.ac.uk/course/chemistry-bsc-mchem',
'http://www.staffs.ac.uk/course/chemistry-bsc-mchem',
'http://www.staffs.ac.uk/course/chemistry-bsc-mchem',
'http://www.staffs.ac.uk/course/chemistry-bsc-mchem',
'http://www.staffs.ac.uk/course/computer-gameplay-design-production-bsc',
'http://www.staffs.ac.uk/course/computer-gameplay-design-production-bsc',
'http://www.staffs.ac.uk/course/computer-gameplay-design-production-bsc',
'http://www.staffs.ac.uk/course/computer-games-animation-ba',
'http://www.staffs.ac.uk/course/computer-games-design-bsc',
'http://www.staffs.ac.uk/course/computer-games-design-bsc',
'http://www.staffs.ac.uk/course/computer-games-design-bsc',
'http://www.staffs.ac.uk/course/computer-games-design-programming-bsc',
'http://www.staffs.ac.uk/course/computer-games-design-programming-bsc',
'http://www.staffs.ac.uk/course/computer-games-development-bsc',
'http://www.staffs.ac.uk/course/computer-games-development-bsc',
'http://www.staffs.ac.uk/course/computer-games-development-bsc',
'http://www.staffs.ac.uk/course/computer-games-programming-bsc',
'http://www.staffs.ac.uk/course/computer-games-programming-bsc',
'http://www.staffs.ac.uk/course/computer-games-programming-virtual-reality-bsc',
'http://www.staffs.ac.uk/course/computer-games-programming-virtual-reality-bsc',
'http://www.staffs.ac.uk/course/computer-games-programming-virtual-reality-bsc',
'http://www.staffs.ac.uk/course/computer-networks-security-bsc-msci',
'http://www.staffs.ac.uk/course/computer-networks-security-bsc-msci',
'http://www.staffs.ac.uk/course/computer-networks-security-bsc-msci',
'http://www.staffs.ac.uk/course/computer-networks-security-bsc-msci',
'http://www.staffs.ac.uk/course/computer-networks-security-bsc-msci',
'http://www.staffs.ac.uk/course/computer-science-bsc-msci',
'http://www.staffs.ac.uk/course/computer-science-bsc-msci',
'http://www.staffs.ac.uk/course/computer-science-bsc-msci',
'http://www.staffs.ac.uk/course/computer-science-bsc-msci',
'http://www.staffs.ac.uk/course/computing-bsc',
'http://www.staffs.ac.uk/course/computing-bsc',
'http://www.staffs.ac.uk/course/computing-bsc',
'http://www.staffs.ac.uk/course/concept-art-games-film-ba',
'http://www.staffs.ac.uk/course/concept-art-games-film-ba',
'http://www.staffs.ac.uk/course/creative-music-technology-ba',
'http://www.staffs.ac.uk/course/criminology-offender-management-ba',
'http://www.staffs.ac.uk/course/cyber-security-bsc',
'http://www.staffs.ac.uk/course/cyber-security-bsc',
'http://www.staffs.ac.uk/course/early-childhood-studies-ba',
'http://www.staffs.ac.uk/course/ecology-conservation-practice-bsc',
'http://www.staffs.ac.uk/course/ecology-conservation-practice-bsc',
'http://www.staffs.ac.uk/course/education-studies-ba',
'http://www.staffs.ac.uk/course/electrical-electronic-engineering-beng-meng',
'http://www.staffs.ac.uk/course/electrical-electronic-engineering-beng-meng',
'http://www.staffs.ac.uk/course/electrical-electronic-engineering-beng-meng',
'http://www.staffs.ac.uk/course/english-ba',
'http://www.staffs.ac.uk/course/english-ba',
'http://www.staffs.ac.uk/course/english-creative-writing-ba',
'http://www.staffs.ac.uk/course/esports-ba',
'http://www.staffs.ac.uk/course/esports-ba',
'http://www.staffs.ac.uk/course/events-management-ba',
'http://www.staffs.ac.uk/course/events-management-ba',
'http://www.staffs.ac.uk/course/experimental-film-production-ba',
'http://www.staffs.ac.uk/course/fashion-ba',
'http://www.staffs.ac.uk/course/fashion-ba',
'http://www.staffs.ac.uk/course/film-production-interactive-technology-bsc',
'http://www.staffs.ac.uk/course/film-production-interactive-technology-bsc',
'http://www.staffs.ac.uk/course/film-television-radio-ba',
'http://www.staffs.ac.uk/course/fine-art-ba',
'http://www.staffs.ac.uk/course/forensic-biology-bsc-msci',
'http://www.staffs.ac.uk/course/forensic-biology-bsc-msci',
'http://www.staffs.ac.uk/course/forensic-biology-bsc-msci',
'http://www.staffs.ac.uk/course/forensic-computing-bsc',
'http://www.staffs.ac.uk/course/forensic-computing-bsc',
'http://www.staffs.ac.uk/course/forensic-computing-bsc',
'http://www.staffs.ac.uk/course/forensic-investigation-bsc-msc',
'http://www.staffs.ac.uk/course/forensic-investigation-bsc-msc',
'http://www.staffs.ac.uk/course/forensic-investigation-bsc-msc',
'http://www.staffs.ac.uk/course/forensic-psychology-bsc',
'http://www.staffs.ac.uk/course/forensic-psychology-bsc',
'http://www.staffs.ac.uk/course/forensic-science-bsc-msc',
'http://www.staffs.ac.uk/course/forensic-science-bsc-msc',
'http://www.staffs.ac.uk/course/forensic-science-bsc-msc',
'http://www.staffs.ac.uk/course/games-art-ba',
'http://www.staffs.ac.uk/course/games-art-ba',
'http://www.staffs.ac.uk/course/games-journalism-pr-ba',
'http://www.staffs.ac.uk/course/games-studies-ba',
'http://www.staffs.ac.uk/course/games-studies-ba',
'http://www.staffs.ac.uk/course/geography-bsc',
'http://www.staffs.ac.uk/course/geography-human-bsc',
'http://www.staffs.ac.uk/course/geography-physical-bsc',
'http://www.staffs.ac.uk/course/geography-with-mountain-leadership-bsc',
'http://www.staffs.ac.uk/course/graphic-design-ba',
'http://www.staffs.ac.uk/course/health-social-care-bsc',
'http://www.staffs.ac.uk/course/history-modern-ba',
'http://www.staffs.ac.uk/course/history-modern-international-ba',
'http://www.staffs.ac.uk/course/human-biology-bsc-msci',
'http://www.staffs.ac.uk/course/human-biology-bsc-msci',
'http://www.staffs.ac.uk/course/human-biology-bsc-msci',
'http://www.staffs.ac.uk/course/illustration-ba',
'http://www.staffs.ac.uk/course/journalism-ba',
'http://www.staffs.ac.uk/course/journalism-ba',
'http://www.staffs.ac.uk/course/journalism-ba',
'http://www.staffs.ac.uk/course/law-llb',
'http://www.staffs.ac.uk/course/law-llb',
'http://www.staffs.ac.uk/course/law-llb',
'http://www.staffs.ac.uk/course/marketing-management-ba',
'http://www.staffs.ac.uk/course/marketing-management-ba',
'http://www.staffs.ac.uk/course/mechanical-engineering-beng-meng',
'http://www.staffs.ac.uk/course/mechanical-engineering-beng-meng',
'http://www.staffs.ac.uk/course/mechanical-engineering-beng-meng',
'http://www.staffs.ac.uk/course/media-film-production-ba',
'http://www.staffs.ac.uk/course/motorsport-engineering-bsc',
'http://www.staffs.ac.uk/course/motorsport-engineering-bsc',
'http://www.staffs.ac.uk/course/motorsport-engineering-bsc',
'http://www.staffs.ac.uk/course/music-business-production-ba',
'http://www.staffs.ac.uk/course/music-production-ba',
'http://www.staffs.ac.uk/course/music-technology-bsc',
'http://www.staffs.ac.uk/course/music-technology-bsc',
'http://www.staffs.ac.uk/course/network-computing-bsc',
'http://www.staffs.ac.uk/course/network-computing-bsc',
'http://www.staffs.ac.uk/course/network-computing-bsc',
'http://www.staffs.ac.uk/course/nursing-practice-adult-bsc',
'http://www.staffs.ac.uk/course/nursing-practice-adult-bsc',
'http://www.staffs.ac.uk/course/nursing-practice-adult-bsc',
'http://www.staffs.ac.uk/course/nursing-practice-adult-bsc',
'http://www.staffs.ac.uk/course/nursing-practice-adult-bsc',
'http://www.staffs.ac.uk/course/nursing-practice-child-bsc',
'http://www.staffs.ac.uk/course/nursing-practice-child-bsc',
'http://www.staffs.ac.uk/course/nursing-practice-mental-health-bsc',
'http://www.staffs.ac.uk/course/nursing-practice-mental-health-bsc',
'http://www.staffs.ac.uk/course/nursing-practice-mental-health-bsc',
'http://www.staffs.ac.uk/course/nursing-practice-mental-health-bsc',
'http://www.staffs.ac.uk/course/operating-department-practice-bsc',
'http://www.staffs.ac.uk/course/paramedic-science-bsc',
'http://www.staffs.ac.uk/course/paramedic-science-bsc',
'http://www.staffs.ac.uk/course/pharmaceutical-science-bsc-msci',
'http://www.staffs.ac.uk/course/pharmaceutical-science-bsc-msci',
'http://www.staffs.ac.uk/course/pharmaceutical-science-bsc-msci',
'http://www.staffs.ac.uk/course/pharmaceutical-science-bsc-msci',
'http://www.staffs.ac.uk/course/photography-ba',
'http://www.staffs.ac.uk/course/physical-education-youth-sport-coaching-bsc',
'http://www.staffs.ac.uk/course/policing-criminal-investigation-bsc-msci',
'http://www.staffs.ac.uk/course/policing-criminal-investigation-bsc-msci',
'http://www.staffs.ac.uk/course/policing-criminal-investigation-bsc-msci',
'http://www.staffs.ac.uk/course/post-production-technology-bsc',
'http://www.staffs.ac.uk/course/post-production-technology-bsc',
'http://www.staffs.ac.uk/course/primary-education-qts-ba',
'http://www.staffs.ac.uk/course/product-design-ba',
'http://www.staffs.ac.uk/course/psychology-bsc',
'http://www.staffs.ac.uk/course/psychology-bsc',
'http://www.staffs.ac.uk/course/psychology-bsc',
'http://www.staffs.ac.uk/course/psychology-child-development-bsc',
'http://www.staffs.ac.uk/course/psychology-child-development-bsc',
'http://www.staffs.ac.uk/course/psychology-counselling-bsc',
'http://www.staffs.ac.uk/course/psychology-counselling-bsc',
'http://www.staffs.ac.uk/course/psychology-criminology-bsc',
'http://www.staffs.ac.uk/course/psychology-criminology-bsc',
'http://www.staffs.ac.uk/course/social-welfare-law-policy-advice-practice-ba',
'http://www.staffs.ac.uk/course/social-work-ba',
'http://www.staffs.ac.uk/course/sociology-ba',
'http://www.staffs.ac.uk/course/sociology-criminology-deviance-ba',
'http://www.staffs.ac.uk/course/software-engineering-bsc-msci',
'http://www.staffs.ac.uk/course/software-engineering-bsc-msci',
'http://www.staffs.ac.uk/course/software-engineering-bsc-msci',
'http://www.staffs.ac.uk/course/software-engineering-bsc-msci',
'http://www.staffs.ac.uk/course/sound-design-bsc',
'http://www.staffs.ac.uk/course/sound-design-bsc',
'http://www.staffs.ac.uk/course/sport-exercise-science-bsc',
'http://www.staffs.ac.uk/course/sports-coaching-ba',
'http://www.staffs.ac.uk/course/sports-coaching-ba',
'http://www.staffs.ac.uk/course/sports-journalism-ba',
'http://www.staffs.ac.uk/course/sports-strength-conditioning-accelerated',
'http://www.staffs.ac.uk/course/sports-therapy-bsc',
'http://www.staffs.ac.uk/course/SSTK-02596.jsp',
'http://www.staffs.ac.uk/course/surface-pattern-design-ba',
'http://www.staffs.ac.uk/course/terrorism-criminology-ba',
'http://www.staffs.ac.uk/course/transport-design-ba',
'http://www.staffs.ac.uk/course/UCYM-11646.jsp',
'http://www.staffs.ac.uk/course/virtual-reality-design-ba',
'http://www.staffs.ac.uk/course/virtual-reality-design-ba',
'http://www.staffs.ac.uk/course/virtual-reality-design-ba',
'http://www.staffs.ac.uk/course/web-design-bsc',
'http://www.staffs.ac.uk/course/web-design-bsc',
'http://www.staffs.ac.uk/course/web-development-bsc-msci',
'http://www.staffs.ac.uk/course/web-development-bsc-msci',
'http://www.staffs.ac.uk/course/web-development-bsc-msci',
'http://www.staffs.ac.uk/course/web-development-bsc-msci',
'http://www.staffs.ac.uk/course/web-development-bsc-msci',
'http://www.staffs.ac.uk/course/web-development-bsc-msci',]
        urls=set(urls)
        for u in urls:
            yield scrapy.Request(url=u,callback=self.parsesss,meta={'url':u})
    def parsesss(self, response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.url
        item['university']='Staffordshire University'
        alevel=response.xpath('//li[contains(text(),"A level")]/text()').extract()
        print(alevel)
        item['alevel']=remove_class(alevel)
        yield item
    def parsess(self, response):
        # print(response.url)
        pro_url=response.xpath('//article/a/@href').extract()
        for i in pro_url:
            full_url='http://search.staffs.ac.uk'+i
            yield scrapy.Request(url=full_url,callback=self.parses)
        next_page=response.xpath('//a[contains(text(),"Next")]/@href').extract()
        if next_page!=[]:
            next_url='http://search.staffs.ac.uk/s/'+next_page[0]
            yield scrapy.Request(url=next_url,callback=self.parse)
    def parses(self,response):
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'Staffordshire University'
        item['url'] = response.url
        item['location'] = 'Staffordshire'
        programme = response.xpath('//h1/text()').extract()
        programme = ''.join(programme).strip()
        item['programme_en'] = programme
        degree_name = response.xpath('//h2[@class="hero_header text-center"]/text()').extract()
        if degree_name == []:
            degree_name = re.findall('[A-Z]{2,}[a-z]*', programme)
            degree_name = ''.join(degree_name).strip()
        #     item['degree_name'] = degree_name
        # else:
        #     item['degree_name'] = ''.join(degree_name).strip()
        start_date = response.xpath('//dt[contains(text(),"Academic year:")]/following-sibling::dd/text()').extract()
        if start_date == []:
            start_date = response.xpath('//th[contains(text(),"Course start")]/following-sibling::td/text()').extract()
        start_date = tracslateDate(start_date)
        item['start_date'] = ','.join(start_date).strip()
        department = response.xpath('//th[contains(text(),"School")]/following-sibling::td/text()').extract()
        department = ''.join(department).strip()
        item['department'] = department
        # print(department)
        fee = response.xpath('//*[contains(text(),"£")]//text()').extract()
        tuition_fee = getTuition_fee(fee)
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = '£'
        overview=response.xpath('//div[@id="key-features"]|//section[@class="course-details_section summary-section"]//div[@class="medium-8 medium-pull-4 large-pull-3 column"]').extract()
        # overview=response.xpath('//div[@data-field="Purpose and key features"]').extract()
        # if overview==[]:
        #     print(response.url)
        overview=remove_class(overview)
        item['overview_en']=overview
        modules = response.xpath(
            '//div[@id="course-content"]|//section[@id="contents"]|//div[@id="course-summary"]').extract()
        modules = remove_class(modules)
        item['modules_en'] = modules
        rntry = response.xpath('//div[@id="course-entry-requirements"]|//section[@id="entry"]').extract()
        rntry = remove_class(rntry)
        item['rntry_requirements'] = rntry
        career = response.xpath('//div[@id="graduate-destinations"]|//section[@id="careers"]').extract()
        career = remove_class(career)
        item['career_en'] = career
        ielts = response.xpath('//*[contains(text(),"IELTS")]//text()').extract()
        ielts = ''.join(ielts).strip()
        item['ielts_desc'] = ielts
        ielts = get_ielts(ielts)
        # duration = clear_duration(duration)
        # item['duration'] = duration['duration']
        # item['duration_per'] = duration['duration_per']
        start_date = response.xpath(
            '//dt[contains(text(),"Academic year:")]/following-sibling::dd[1]//text()').extract()
        # print(start_date)
        if start_date != []:
            start_date = start_date[0]
            start_date = tracslateDate(start_date)
            start_date = ''.join(start_date)
            item['start_date'] = start_date
            # print(start_date)
        else:
            start_date = response.xpath('//th[contains(text(),"Course start")]/following-sibling::td/text()').extract()
            start_date = tracslateDate(start_date)
            start_date = ','.join(start_date)
            item['start_date'] = start_date
            # print(start_date)
        alevel = response.xpath('//li[contains(text(),"A level")]/text()').extract()
        alevel = ''.join(alevel).strip()
        item['alevel'] = alevel
        try:
            if ielts != [] or ielts != {}:
                item['ielts_l'] = ielts['IELTS_L']
                item['ielts_s'] = ielts['IELTS_S']
                item['ielts_r'] = ielts['IELTS_R']
                item['ielts_w'] = ielts['IELTS_W']
                item['ielts'] = ielts['IELTS']
        except:
            pass
        ucascode=response.xpath('//dt[contains(text(),"UCAS")]/following-sibling::dd[1]/text()').extract()
        UCAS=ucascode
        ucascode=','.join(ucascode).strip()
        item['ucascode']=ucascode
        duration = response.xpath(
            '//th[contains(text(),"Duration")]/following-sibling::td/text()|//dt[contains(text(),"Duration")]/following-sibling::dd[1]/text()').extract()
        deg=response.xpath('//select[@id="award-selector"]/option/text()').extract()
        mode=response.xpath('//dt[contains(text(),"Mode of ")]/following-sibling::dd[1]/text()').extract()
        try:
            for i in mode:
                pdtj=re.findall('(?i)full',i)
                if pdtj==[]:
                    del duration[mode.index(i)]
        except:
            pass
        assessment = response.xpath('//section[@id="teaching"]//h3[contains(text(),"ssessment")]/following-sibling::div[position()<=1]').extract()
        if assessment==[]:
            print(response.url)
        else:
            print('GG')
        teaching=response.xpath('//section[@id="teaching"]//h3[contains(text(),"Teaching")]/following-sibling::div[position()<=1]').extract()

        item['assessment_en'] = '<h3>Teaching</h3>'+'\n'+remove_class(teaching)+'\n'+'<h3>Aassessment</h3>'+'\n'+remove_class(assessment)
        item['duration_per']=1
        yield item




