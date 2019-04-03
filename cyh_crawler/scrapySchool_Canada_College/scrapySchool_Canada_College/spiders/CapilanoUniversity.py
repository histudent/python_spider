# -*- coding: utf-8 -*-
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.getItem import *
from scrapySchool_Canada_College.items import *

class CapilanouniversitySpider(scrapy.Spider):
    name = 'CapilanoUniversity'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.capilanou.ca/programs--courses/program-profiles/2d-animation--visual-development-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/3d-animation-for-film-and-games-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/academic-studies-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/accounting-assistant-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/acting-for-stage-and-screen-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/applied-behaviour-analysis-autism-post-baccalaureate-certificate/',
'https://www.capilanou.ca/programs--courses/program-profiles/bachelor-of-arts-degree---applied-behaviour-analysis-autism/',
'https://www.capilanou.ca/programs--courses/program-profiles/associate-of-arts-degree---creative-writing/',
'https://www.capilanou.ca/programs--courses/program-profiles/associate-of-arts-degree---english/',
'https://www.capilanou.ca/programs--courses/program-profiles/associate-of-arts-degree---global-stewardship/',
'https://www.capilanou.ca/programs--courses/program-profiles/associate-of-arts-degree---psychology/',
'https://www.capilanou.ca/programs--courses/program-profiles/arts-and-entertainment-management-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/bachelor-of-arts-with-a-major-in-liberal-studies/',
'https://www.capilanou.ca/programs--courses/program-profiles/bachelor-of-business-administration-degree/',
'https://www.capilanou.ca/programs--courses/program-profiles/business-administration-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/bachelor-of-communication-studies-degree/',
'https://www.capilanou.ca/programs--courses/program-profiles/communication-studies-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/community-leadership-and-social-change-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/costuming-for-stage-and-screen-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/bachelor-of-design-in-visual-communication/',
'https://www.capilanou.ca/programs--courses/program-profiles/digital-visual-effects-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/bachelor-of-early-childhood-care-and-education-degree/',
'https://www.capilanou.ca/programs--courses/program-profiles/early-childhood-care-and-education-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/engineering-transition-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/human-kinetics-diploma---exercise-science/',
'https://www.capilanou.ca/programs--courses/program-profiles/human-kinetics-diploma---physical-education/',
'https://www.capilanou.ca/programs--courses/program-profiles/indigenous-independent-digital-filmmaking-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/international-management-graduate-certificate/',
'https://www.capilanou.ca/programs--courses/program-profiles/international-management-graduate-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/jazz-studies-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/bachelor-of-music-in-jazz-studies---education/',
'https://www.capilanou.ca/programs--courses/program-profiles/bachelor-of-music-in-jazz-studies---performancecomposition/',
'https://www.capilanou.ca/programs--courses/program-profiles/bachelor-of-legal-studies-paralegal-degree/',
'https://www.capilanou.ca/programs--courses/program-profiles/local-government-administration-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/bachelor-of-motion-picture-arts-degree/',
'https://www.capilanou.ca/programs--courses/program-profiles/motion-picture-arts-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/music-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/music-diploma---music-therapy-course-stream/',
'https://www.capilanou.ca/programs--courses/program-profiles/bachelor-of-music-therapy-degree/',
'https://www.capilanou.ca/programs--courses/program-profiles/musical-theatre-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/north-american-and-international-management-graduate-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/outdoor-recreation-management-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/paralegal-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/bachelor-of-performing-arts-degree/',
'https://www.capilanou.ca/programs--courses/program-profiles/rehabilitation-assistant-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/associate-of-science-degree---biology/',
'https://www.capilanou.ca/programs--courses/program-profiles/technical-theatre-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/bachelor-of-tourism-management-degree/',
'https://www.capilanou.ca/programs--courses/program-profiles/tourism-management-co-operative-education-diploma/',
'https://www.capilanou.ca/programs--courses/program-profiles/tourism-management-for-international-students-diploma/',]

    def parse(self, response):
        item=get_item(ScrapyschoolCanadaCollegeItem)
        item['school_name']='Capilano University'
        item['url']=response.url
        print(response.url)

        #1.学费空的就是官网上没有 2.就业方向采集的是官网的学习成果
        item['other']='1.空缺的就业方向、课程设置、专业描述的就是官网上没有 2.就业方向采集的是官网的学习成果'
        programme=response.xpath('//h1[@id="page-title"]/text()').extract()
        # print(programme)
        degree_name=response.xpath('//p[contains(text(),"Credential")]/span/text()').extract()
        programme=''.join(programme)
        degree_name=''.join(degree_name)
        if ' - ' in programme:
            item['degree_name']=programme.split(' - ')[0]
            item['major_name_en']=programme.split(' - ')[1]
        elif ' - ' not in programme and 'Diploma' in programme:
            item['degree_name']=programme
            item['major_name_en']=programme.replace('Diploma','').strip()
        else:
            item['degree_name']=degree_name
            item['major_name_en']=programme

        department=response.xpath('//span[contains(text(),"Faculty of ")]/text()').extract()
        # print(department)
        item['department']=department[0]

        start=response.xpath('//th[contains(text(),"Campus")]/../../../tbody/tr/td[2]/text()').extract()
        # print(start)
        item['campus']='North Shore Campus'
        item['location']='North Vancouver'
        item['apply_fee'],item['apply_pre']='135','$'
        item['average_score']='60'
        item['require_chinese_en']='<p>Senior (Upper) Middle School Graduation Certificate</p>'
        item['start_date']=','.join(start).replace('Fall','2019-09').replace('Summer','2019-05').replace('Spring','2019-01')

        duration=response.xpath('//td[contains(text(),"Year ")]/text()').extract()
        duration=re.findall('\d',''.join(duration))
        print(duration)
        if duration!=[]:
            item['duration_per']='1'
            item['duration']=max(list(map(int,duration)))

        tuition=response.xpath('//td[text()="Year 1"]/../td[4]/text()').extract()
        # print(tuition)
        if tuition!=[]:
            item['tuition_fee']=tuition[1].replace('$','').strip()
            item['tuition_fee_pre']='$'

        deadline=response.xpath('//h3[contains(text(),"Application Dates")]/following-sibling::p[1]/text()').extract()
        # print(deadline)
        deadline=list(map(lambda x:x.split('\xa0-\xa0')[1],deadline))
        # print(deadline)
        item['deadline']=''.join(deadline)

        modules=response.xpath('//div[@id="tab-course-outline"]').extract()
        item['modules_en']=remove_class(modules)

        overview=response.xpath('//h2[text()="Program Highlights"]/following-sibling::p').extract()
        item['overview_en']=remove_class(overview)

        career=response.xpath('//h3[text()="Learning Outcomes"]/../../following-sibling::div').extract()
        item['career_en']=remove_class(career)

        entry_requirement=response.xpath('//h2[contains(text(),"dmission Requirement")]/following-sibling::p').extract()
        item['entry_requirements_en']=remove_class(entry_requirement)

        toefl=re.findall('internet=\d+',''.join(entry_requirement))
        # print(toefl)
        item['toefl']=''.join(toefl).replace('internet=','').strip()

        ielts=re.findall('[567]\.[05]',''.join(entry_requirement))
        # print(ielts)
        if len(ielts)==1:
            item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']=ielts[0],ielts[0],ielts[0],ielts[0],ielts[0]
        elif len(ielts)==2:
            item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w'] =ielts[0],ielts[1],ielts[1],ielts[1],ielts[1]
        elif len(ielts)==3:
            item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w'] = ielts[0], ielts[1],ielts[1], ielts[1], ielts[2]

        yield item