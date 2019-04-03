# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.clearSpace import clear_same_s
import scrapy
import re
class UniversityoftheartslondonSpider(CrawlSpider):
    name = 'UniversityOfTheArtsLondon_P'
    allowed_domains = ['arts.ac.uk']
    # start_urls = ['http://search.arts.ac.uk/s/search.html?collection=courses&query=&profile=_default&f.Course+level%7Cl=Postgraduate&f.Mode%7Cm=Full+time&start_rank=1']
    # rules = (
    #     Rule(LinkExtractor(allow=r'start_rank=[0-9]+'), follow=True),
    #     Rule(LinkExtractor(restrict_xpaths='//div[@class="search-title"]//h2'), follow=False, callback='parses'),
    # )
    start_urls=['http://www.arts.ac.uk/csm/courses/postgraduate/ma-design-ceramics-furniture-or-jewellery/']
    def parse(self, response):
        start_urlss = ['http://www.arts.ac.uk/csm/courses/postgraduate/ma-design-ceramics-furniture-or-jewellery/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-design-ceramics-furniture-or-jewellery/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-film/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-games-design/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-television/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-fashion-cultures/',
                       'http://www.arts.ac.uk/camberwell/courses/postgraduate/ma-book-arts/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/mres-art-moving-image/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-documentary-film/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-visual-effects/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-sound-arts/',
                       'http://www.arts.ac.uk/wimbledon/courses/postgraduate/mfa-fine-art/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-art-and-science/',
                       'http://www.arts.ac.uk/camberwell/courses/postgraduate/ma-printmaking/',
                       'http://www.arts.ac.uk/wimbledon/courses/postgraduate/ma-theatre-design/',
                       'http://www.arts.ac.uk/chelsea/courses/postgraduate/ma-textile-design/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-fashion-media-production/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-culture-criticism-and-curation/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-user-experience-design/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-graphic-communication-design/',
                       'http://www.arts.ac.uk/chelsea/courses/postgraduate/ma-interior-spatial-design/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-fashion-communication/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-fashion-retail-management/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-fashion-futures/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/mres-art-exhibition-studies/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-3d-computer-animation/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-acting-drama-centre-london/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-strategic-fashion-marketing/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-fashion-design-management/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-fashion-photography/',
                       'http://www.arts.ac.uk/chelsea/courses/postgraduate/ma-curating-collections/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-narrative-environments/',
                       'http://www.arts.ac.uk/camberwell/courses/postgraduate/ma-fine-art-digital/',
                       'http://www.arts.ac.uk/camberwell/courses/postgraduate/ma-designer-maker/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-screen-acting-drama-centre-london/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-service-experience-design-innovation/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-fashion-footwear/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/m-arch-architecture/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/msc-applied-psychology-in-fashion/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/mres-art-theory-and-philosophy/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-pattern-and-garment-technology/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-costume-design-for-performance/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-graphic-branding-and-identity/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-architecture-cities-and-innovation/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-illustration-and-visual-media/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-arts-and-lifestyle-journalism/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-design-for-art-direction/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-interaction-design-communication/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-design-management-and-cultures/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-graphic-media-design/',
                       'http://www.arts.ac.uk/chelsea/courses/postgraduate/ma-graphic-design-communication/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-media-communications-and-critical-practice/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-applied-imagination-in-the-creative-industries/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-photojournalism-and-documentary-photography/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-contemporary-photography-practices-philosopies/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-psychology-for-fashion-professionals/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-screen-directing-drama-centre-london/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-design-ceramics-furniture-or-jewellery/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-fashion-design-technology-womenswear/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-fashion-entrepreneurship-and-innovation/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-data-visualisation/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-performance-design-and-practice/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-character-animation/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-fine-art/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-virtual-reality/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-fashion-curation/',
                       'http://www.arts.ac.uk/camberwell/courses/postgraduate/ma-illustration/',
                       'http://www.arts.ac.uk/wimbledon/courses/postgraduate/ma-drawing/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-innovation-management/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-industrial-design/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-dramatic-writing/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-fashion-artefact/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-material-futures/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-fashion-journalism/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-public-relations/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/ma-fashion-design-technology-menswear/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-advertising/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-screenwriting/',
                       'http://www.arts.ac.uk/chelsea/courses/postgraduate/ma-fine-art/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-photography/',
                       'http://www.arts.ac.uk/wimbledon/courses/postgraduate/ma-painting/',
                       'http://www.arts.ac.uk/fashion/courses/postgraduate/lcf-mba/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-publishing/',
                       'http://www.arts.ac.uk/lcc/courses/postgraduate/ma-animation/',
                       'http://www.arts.ac.uk/csm/courses/postgraduate/ma-fashion/', ]
        for i in start_urlss:
            yield scrapy.Request(url=i,meta={'url':i},callback=self.parses)
    def parses(self, response):
        item=get_item1(ScrapyschoolEnglandItem1)
        item['url']=response.meta['url']
        item['university']='University of the Arts London'
        print(response.url)
        modules=response.xpath('//h2[contains(text(),"ourse detail")]/../following-sibling::div|//h2[contains(text(),"ourse unit")]/../following-sibling::*[1]').extract()
        # print(modules)
        item['modules_en']=remove_class(modules)
        yield item
    def parsess(self, response):
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        programme=response.xpath('//div[@class="course-header"]//h1/text()').extract()
        programme=''.join(programme)
        degree_name=re.findall('[A-Z]{2}[a-z]*',programme)
        degree_name=set(degree_name)
        degree_name=''.join(degree_name)
        programme=programme.replace(degree_name,'').strip()
        item['degree_name'] = degree_name
        item['programme_en'] = programme
        item['university'] = 'University of the Arts London'
        item['url'] = response.url
        item['location'] = 'London'
        item['tuition_fee_pre'] = '£'
        # print(programme)

        CourseOverview=response.xpath('//div[@id="tab1-panel"]').extract()
        overview=remove_class(CourseOverview)
        overview=clear_same_s(overview)
        item['overview_en'] = overview

        Modules = response.xpath('//div[@id="tab2-panel"]').extract()
        modules=remove_class(Modules)
        item['modules_en'] = modules

        apply_desc_en=response.xpath('//div[@id="tab3-panel"]').extract()
        apply_desc_en=remove_class(apply_desc_en)
        apply_desc_en=clear_same_s(apply_desc_en)
        item['apply_desc_en'] = apply_desc_en

        entry=response.xpath('//h2[contains(text(),"ntry")]/following-sibling::*|'
                             '//h2[contains(text(),"ntry")]/../following-sibling::*[1]').extract()
        # if entry==[]:
        #     print(response.url)
        # else:
        #     print('入学要求不为空')
        entry=remove_class(entry)
        item['rntry_requirements'] = entry
        # print(item['rntry_requirements'])

        IELTS=response.xpath('//*[contains(text(),"IELTS")]//text()').extract()
        # print(IELTS)
        ielts = get_ielts(IELTS)
        if ielts != {} and ielts != []:
            ielts_l = ielts['IELTS_L']
            ielts_s = ielts['IELTS_S']
            ielts_r = ielts['IELTS_R']
            ielts_w = ielts['IELTS_W']
            ielts = ielts['IELTS']
        else:
            ielts = ''
            ielts_l, ielts_s, ielts_r, ielts_w = '', '', '', ''
        item['ielts'] = ielts
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        # print(item['ielts_l'])

        tuition_fee=getTuition_fee(response.xpath('//h3[contains(text(),"International fee")]/following-sibling::p[1]//text()').extract())
        item['tuition_fee'] = tuition_fee
        # print(tuition_fee)

        Career=response.xpath('//div[@id="tab5-panel"]').extract()
        career=remove_class(Career)
        career=clear_same_s(career)
        item['career_en'] = career
        # print(career)

        department=response.xpath('//h1//text()').extract()[0]
        # print(department)
        # department=''.join(department)
        item['department'] = department
        # print(department)

        item['start_date'] = '2018-9'

        duration=response.xpath('//strong[contains(text(),"Course length")]/../text()').extract()
        duration=''.join(duration)
        # print(duration)
        # print(item)
        durn=re.findall('\d{1,2}\s[a-zA-Z]+',duration)
        # print(durn)
        if len(durn)==1:
            durn=''.join(durn)
            item['duration'] = ''.join(re.findall('\d+',durn))
            item['duration_per'] = self.change_durntion_per(re.findall('[a-zA-Z]+',durn))
            # print(item['duration'])
            # print(item['duration_per'])
        if len(durn)==2:
            # print(durn)
            durn=durn[0]
            item['duration'] = ''.join(re.findall('\d+',durn))
            item['duration_per'] = self.change_durntion_per(re.findall('[a-zA-Z]+',durn))
        if len(durn)==3:
            # print(durn)
            item['duration'] = 15
            item['duration_per'] = 3
        assessment=response.xpath('//h3[contains(text(),"ssessment")]/following-sibling::*[position()<=5]').extract()
        item['assessment_en']=remove_class(assessment)
        # if assessment==[]:
        #     print(response.url)
        # else:
        #     print('不为空')
        yield item
    def change_durntion_per(self,var):
        var=''.join(var)
        if var=='year' or var=='years':
            return 1
        elif var=='month' or var=='months':
            return 3
        elif var=='week' or var=='weeks':
            return 4
        else:
            return None
