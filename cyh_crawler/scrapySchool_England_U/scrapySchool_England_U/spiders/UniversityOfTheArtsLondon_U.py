# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem

class UniversityoftheartslondonUSpider(scrapy.Spider):
    name = 'UniversityOfTheArtsLondon_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-games-design-lcc']
    def parse(self, response):
        url=['https://www.arts.ac.uk/subjects/fashion-business/undergraduate/ba-hons-fashion-buying-and-merchandising-lcf',
'https://www.arts.ac.uk/subjects/photography/undergraduate/ba-hons-fashion-photography-lcf',
'https://www.arts.ac.uk/subjects/accessories-footwear-and-jewellery/undergraduate/ba-hons-fashion-jewellery-lcf',
'https://www.arts.ac.uk/subjects/fashion-communication/undergraduate/ba-hons-creative-direction-for-fashion-lcf',
'https://www.arts.ac.uk/subjects/business-and-management-and-science/undergraduate/bsc-hons-psychology-of-fashion-lcf',
'https://www.arts.ac.uk/subjects/journalism-pr-media-and-publishing/undergraduate/ba-hons-fashion-journalism-lcf',
'https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/undergraduate/ba-hons-theatre-design-wimbledon',
'https://www.arts.ac.uk/subjects/textiles-and-materials/undergraduate/ba-hons-textile-design-chelsea',
'https://www.arts.ac.uk/subjects/fashion-design/undergraduate/ba-hons-fashion-sportswear-lcf',
'https://www.arts.ac.uk/subjects/fashion-making-and-pattern-cutting/undergraduate/ba-hons-fashion-pattern-cutting-lcf',
'https://www.arts.ac.uk/subjects/fashion-design/undergraduate/ba-hons-fashion-design-and-development-lcf',
'https://www.arts.ac.uk/subjects/fashion-business/postgraduate/msc-strategic-fashion-management-lcf',
'https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/undergraduate/ba-hons-3d-effects-for-performance-and-fashion-lcf',
'https://www.arts.ac.uk/subjects/architecture-spatial-and-interior-design/undergraduate/ba-hons-interior-design-chelsea',
'https://www.arts.ac.uk/subjects/3d-design-and-product-design/undergraduate/ba-hons-3d-design-camberwell',
'https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-production-arts-for-screen-wimbledon',
'https://www.arts.ac.uk/subjects/communication-and-graphic-design/undergraduate/ba-hons-graphic-design-communication-chelsea',
'https://www.arts.ac.uk/subjects/business-and-management-and-science/postgraduate/msc-cosmetic-science-lcf',
'https://www.arts.ac.uk/subjects/communication-and-graphic-design/undergraduate/ba-hons-design-for-art-direction-lcc',
'https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-painting-camberwell',
'https://www.arts.ac.uk/subjects/fashion-business/undergraduate/ba-hons-fashion-marketing-lcf',
'https://www.arts.ac.uk/subjects/fashion-design/undergraduate/ba-hons-fashion-design-technology-menswear-lcf',
'https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/undergraduate/ba-hons-costume-for-performance-lcf',
'https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/undergraduate/ba-hons-costume-for-theatre-and-screen-wimbledon',
'https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-fine-art-print-and-time-based-media-wimbledon',
'https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-sculpture-camberwell',
'https://www.arts.ac.uk/subjects/illustration/undergraduate/ba-hons-fashion-illustration-lcf',
'https://www.arts.ac.uk/subjects/illustration/undergraduate/ba-hons-illustration-camberwell',
'http://www.arts.ac.uk/fashion/courses/undergraduate/ba-fashion-visual-merchandising-and-branding/',
'https://www.arts.ac.uk/subjects/fashion-styling-and-make-up/undergraduate/ba-hons-fashion-styling-and-production-lcf',
'https://www.arts.ac.uk/subjects/fashion-communication/postgraduate/ma-fashion-media-practice-and-criticism-lcf',
'https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-fine-art-painting-wimbledon',
'https://www.arts.ac.uk/subjects/fashion-design/undergraduate/ba-hons-fashion-design-technology-womenswear-lcf',
'https://www.arts.ac.uk/subjects/communication-and-graphic-design/undergraduate/ba-hons-graphic-design-camberwell',
'https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-fine-art-chelsea',
'https://www.arts.ac.uk/subjects/fashion-making-and-pattern-cutting/undergraduate/ba-hons-bespoke-tailoring-lcf',
'https://www.arts.ac.uk/subjects/fashion-business/undergraduate/bsc-hons-fashion-management-lcf',
'https://www.arts.ac.uk/subjects/animation-interactive-film-and-sound/undergraduate/ba-hons-sound-arts-and-design-lcc',
'https://www.arts.ac.uk/subjects/fashion-communication/undergraduate/ba-hons-fashion-public-relations-and-communication-lcf',
'https://www.arts.ac.uk/subjects/accessories-footwear-and-jewellery/undergraduate/ba-hons-cordwainers-fashion-bags-and-accessories-product-design-and-innovation-lcf',
'https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-photography-camberwell',
'https://www.arts.ac.uk/subjects/fashion-making-and-pattern-cutting/undergraduate/ba-hons-fashion-contour-lcf',
'https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-fine-art-sculpture-wimbledon',
'https://www.arts.ac.uk/subjects/architecture-spatial-and-interior-design/undergraduate/ba-hons-interior-and-spatial-design-chelsea',
'http://www.arts.ac.uk/fashion/courses/undergraduate/ba-fashion-textiles-embroidery/',
'https://www.arts.ac.uk/subjects/fine-art/undergraduate/ba-hons-drawing-camberwell',
'https://www.arts.ac.uk/subjects/accessories-footwear-and-jewellery/undergraduate/ba-hons-cordwainers-footwear-product-design-and-innovation-lcf',
'https://www.arts.ac.uk/subjects/performance-and-design-for-theatre-and-screen/undergraduate/ba-hons-hair-make-up-and-prosthetics-for-performance-lcf',
'http://www.arts.ac.uk/fashion/courses/undergraduate/ba-hair-and-make-up-for-fashion/',
'http://www.arts.ac.uk/fashion/courses/undergraduate/ba-fashion-textiles-print/',
'http://www.arts.ac.uk/fashion/courses/undergraduate/ba-fashion-textiles-knit/',]
        url=set(url)
        for u in url:
            yield scrapy.Request(url=u,callback=self.parsesss,meta={'url':u})
    def parsesss(self, response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'University of the Arts London'
        item['url'] = response.meta['url']
        print(response.url)
        alevel=response.xpath('//h4[contains(text(),"The standard minimum entry requirements for this course are:")]/following-sibling::p[1]/text()|//p[contains(text(),"The standard entry requirements for this course are as follows:")]/following-sibling::p[2]/text()').extract()
        alevel=response.xpath('//li[contains(text(),"A Level")]/text()').extract()
        alevel=''.join(alevel).replace('*',' ').strip()
        item['alevel']=alevel
        yield item

        # yield item
    def parsess(self, response):
        # print(response.url)
        pro_url=response.xpath('//div[@class="search-title"]/h2/a/@href').extract()
        programme=response.xpath('//div[@class="search-title"]/h2/a/text()').extract()
        department=response.xpath('//strong[contains(text(),"College")]/../text()').extract()
        # print(department)
        department=''.join(department).strip()
        department=department.split('Undergraduate')
        for i,dep,pro in zip(pro_url,department,programme):
            full_url='http://search.arts.ac.uk'+i
            # print(dep)
            yield scrapy.Request(url=full_url,callback=self.parses,meta={'programme':pro,'department':dep})
        next_page=response.xpath('//a[contains(text(),"Next")]/@href').extract()
        if next_page!=[]:
            next_page_url='http://search.arts.ac.uk/s/'+next_page[0]
            yield scrapy.Request(url=next_page_url,callback=self.parse)
    def parses(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        # department=response.meta['department'].strip()
        # programme=response.meta['programme']
        # print(department)
        # print(programme)
        # item['department']=department
        # item['major_type1']=programme
        department=response.xpath('//div[@class="container cell course-detail-content"]/h1/text()').extract()
        department=''.join(department).strip()
        item['department']=department
        programme=response.xpath('//div[@class="course-title-heading cell"]/h1/text()').extract()
        programme=''.join(programme).strip()
        degree_name=re.findall('[A-Z]{2}[a-z]*\s\(Hons\)',programme)
        degree_name=''.join(degree_name).strip()
        programme=programme.replace(degree_name,'').strip()
        # print(programme)
        degree_name=degree_name.replace('(Hons)','').strip()
        # print(degree_name)
        item['programme_en']=programme
        item['degree_name']=degree_name

        item['university'] = 'University of the Arts London'
        item['url'] = response.url
        item['location'] = 'London'
        item['tuition_fee_pre'] = '£'

        CourseOverview = response.xpath('//h2[contains(text(),"Course summary")]/following-sibling::div').extract()
        overview = remove_class(CourseOverview)
        item['overview_en'] = overview

        Modules = response.xpath('//h2[contains(text(),"Course de")]/../following-sibling::div').extract()
        modules = remove_class(Modules)
        item['modules_en'] = modules

        apply_desc_en = response.xpath('//div[@id="tab3-panel"]').extract()
        apply_desc_en = remove_class(apply_desc_en)
        item['apply_desc_en'] = apply_desc_en

        entry = response.xpath('//h2[contains(text(),"ntry")]/following-sibling::*').extract()
        entry = remove_class(entry)
        item['require_chinese_en'] = entry
        # print(item['rntry_requirements'])

        IELTS = response.xpath('//*[contains(text(),"IELTS")]//text()').extract()
        print(IELTS)
        ielts = get_ielts(IELTS)
        if ielts != {} and ielts != []:
            ielts_l = ielts['IELTS_L']
            ielts_s = ielts['IELTS_S']
            ielts_r = ielts['IELTS_R']
            ielts_w = ielts['IELTS_W']
            ielts = ielts['IELTS']
            # print(ielts)
            item['ielts'] = ielts
            item['ielts_l'] = ielts_l
            item['ielts_s'] = ielts_s
            item['ielts_r'] = ielts_r
            item['ielts_w'] = ielts_w
        # print(item['ielts_l'])

        tuition_fee = getTuition_fee(
            response.xpath('//h3[contains(text(),"International fee")]/following-sibling::p[1]//text()').extract())
        item['tuition_fee'] = tuition_fee
        # print(tuition_fee)

        Career = response.xpath('//h2[contains(text(),"Career")]/../following-sibling::article').extract()
        career = remove_class(Career)
        career = clear_same_s(career)
        item['career_en'] = career
        # print(career)



        duration = response.xpath('//strong[contains(text(),"Course length")]/../text()').extract()
        duration=clear_duration(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']

        start_date=response.xpath('//div[contains(text(),"Start date")]/following-sibling::div//text()').extract()
        start_date=tracslateDate(start_date)
        start_date=','.join(start_date).strip()
        item['start_date']=start_date

        ucascode=response.xpath('//div[contains(text(),"UCAS")]/following-sibling::div//text()').extract()
        ucascode=''.join(ucascode).strip()
        item['ucascode']=ucascode

        assessment=response.xpath('//h3[contains(text(),"Assess")]/following-sibling::*').extract()
        assessment=remove_class(assessment)
        item['assessment_en']=assessment

        portfolio_desc_en=response.xpath('//h3[contains(text(),"Showing your work")]/following-sibling::*').extract()
        portfolio_desc_en="<ul><li>Examples of your research, development of your ideas and finished pieces</li><li>Your most recent work, even if it's not finished</li><li>Your own independent work; for example, work completed at summer school or on a short course, photography and/or your own experimentation</li><li>Your sketchbooks &ndash; they're a really good way to show us your research and development of ideas. They should include primary and secondary research, rough ideas and notes, descriptions and annotations. They should demonstrate a variety of media and experimentation</li><li>Your portfolio could include the following areas of work: <ul><li>3D and product design</li><li>Drawing and painting</li><li>Fashion and textile design</li><li>Film, video and animation</li><li>Graphic design and illustration</li><li>Interior and spatial design</li><li>Printmaking and digital prints</li><li>Performance</li><li>Photography</li><li>Printmaking and digital prints</li><li>Sculpture and installations</li><li>Written work including essays, journals, blogs and magazines.</li></ul>"
        portfolio_desc_en=remove_class(portfolio_desc_en)
        item['portfolio_desc_en']=portfolio_desc_en

        item['deadline']='2019-1-15'

        interview="<h2>Interviews in China</h2><p>If you have applied through one of our official Representatives in China you can have a face-to-face interview in China with one of our academic staff. Students who apply directly to one of our Colleges are interviewed in London or by telephone from London.</p><p>For more information about face-to-face interviews in China, please email your nearest representative (see contact details above).</p><h3>Offers at interviews in China</h3><ul><li>Further education and undergraduate applications:<br />If you are successful in the interview you will receive an offer on the spot. If the interviewer cannot offer you a place on your first choice course, they will advise you on other suitable courses across UAL's six Colleges or recommend ways you can improve your work so that you can reapply at a later date.</li></ul>"
        interview=remove_class(interview)
        item['interview_desc_en']=interview

        apply_desc_en="<h3>International applicants</h3><p>International applicants may apply through 1 of these 3 routes only:</p><ul><li>Through overseas representatives in your country</li><li>Through UCAS</li><li>Through a direct application, via the online application form found on the specific course page</li></ul><p>You can find more advice and guidance for international students in the <a>dedicated application advice for international students</a> section of this website.</p>"
        apply_desc_en=remove_class(apply_desc_en)
        item['apply_desc_en']=apply_desc_en

        ib=response.xpath('//li[contains(text(),"IB")]/text()').extract()
        ib=''.join(ib).strip()
        item['ib']=ib

        alevel=response.xpath('//li[contains(text(),"A Level")]/text()|//p[contains(text(),"A-level")]//text()|//li[contains(text(),"A level")]//text()').extract()
        # if alevel==[]:
        #     print(response.url)
        alevel=''.join(alevel).strip()
        item['alevel']=alevel

        duration=response.xpath('//div[contains(text(),"Course length")]/following-sibling::div//text()').extract()
        # print(duration)
        item['duration_per']=clear_duration(duration)['duration_per']
        item['duration']=clear_duration(duration)['duration']

        ielts=response.xpath('//*[contains(text(),"IELTS")]//text()').extract()
        if ielts==[]:
            ielts=response.xpath('//h3[contains(text(),"English language requirements")]/following-sibling::p[1]//text()').extract()
            # print(ielts)
        item['ielts_desc']='\n'.join(ielts)
        fee=response.xpath('//h3[contains(text(),"International fee")]/following-sibling::p[1]//text()|//h3[contains(text(),"International Fee")]/following-sibling::p[1]//text()').extract()
        # print(fee)
        fee=getTuition_fee(fee)
        # print(fee)
        item['tuition_fee']=fee

        # print(item)
        yield item



