# -*- coding: utf-8 -*-
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import *
from scrapySchool_Canada_Ben.items import *
import requests
from lxml import etree
class TrentuniversitySpider(scrapy.Spider):
    name = 'TrentUniversity'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.trentu.ca/futurestudents/undergraduate/programs']

    def parse(self, response):
        urls=response.xpath('//div[text()="specialization"]/../@href').extract()
        # programme=response.xpath('//div[text()="degree"]/following-sibling::h3/text()').extract()
        # print(len(urls))
        for u in urls:
            yield scrapy.Request(url=u,callback=self.parses)
    def parses(self,response):
        item=get_item(ScrapyschoolCanadaBenItem)
        item['url']=response.url
        item['school_name']='Trent University'
        item['tuition_fee']='20366.55'
        item['tuition_fee_pre']='$'
        item['apply_fee'],item['apply_pre']='90','$'
        item['start_date'],item['deadline']='2019-09','2019-06-01'
        item['ielts_desc']='6.5, with no band below 6.0'
        item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']='6.5','6.0','6.0','6.0','6.0'
        item['toefl_desc']='86 IBT with a minimum writing score of 20 '
        item['toefl'],item['toefl_w']='86','20'
        item['toefl_code']='0896'
        item['require_chinese_en']='<p>Transcript of marks for grades 10, 11 and 12 (senior upper middle school) with minimum 75%. Senior School Leaving Certificate and Huikao (Senior School Graduation Exam) results. Gaokao (National College Entrance Examination, NCEE) results, if written.</p>'
        item['alevel']='Minimum ‘C’ grade in five O-level subjects, including English or English Literature and two A-level subjects. Minimum grade of "C" in each subject. Two AS-level subjects may be substituted for one A-level subject.'
        item['ib']='Minimum overall score of 26 (including bonus points) in IB diploma, including three courses at the Higher Level.'
        item['average_score']='75'
        item['ap']='<tbody><tr><td><p><em><strong>AP Course</strong> </em></p></td><td><p><strong>Trent Equivalent</strong></p></td><td><p><strong>Credit value</strong></p></td></tr><tr><td><p>ART HISTORY</p></td><td><p>ARTS-YR1</p></td><td><p>1</p></td></tr><tr><td><p>ART STUDIO (DRAWING)</p></td><td><p>ARTS-YR1</p></td><td><p>1</p></td></tr><tr><td><p>ART STUDIES (GENERAL)</p></td><td><p>ARTS-YR1</p></td><td><p>1</p></td></tr><tr><td><p>BIOLOGY</p></td><td><p>BIOL-1020H</p></td><td><p>0.5</p></td></tr><tr><td><p>&nbsp;</p></td><td><p>BIOL-1030H</p></td><td><p>0.5</p></td></tr><tr><td><p>CALCULUS AB</p></td><td><p>SCIE-YR1</p></td><td><p>1</p></td></tr><tr><td><p>CALCULUS BC</p></td><td><p>MATH-1100Y</p></td><td><p>1</p></td></tr><tr><td><p>CHEMISTRY</p></td><td><p>CHEM-1000H</p></td><td><p>0.5</p></td></tr><tr><td><p>&nbsp;</p></td><td><p>CHEM-1010H</p></td><td><p>0.5</p></td></tr><tr><td><p>COMP. GOV. &amp; POLITICS</p></td><td><p>POST-YR1</p></td><td><p>0.5</p></td></tr><tr><td><p>COMPUTER SCIENCE A</p></td><td><p>COIS-1010H</p></td><td><p>0.5</p></td></tr><tr><td><p>COMPUTER SCIENCE AB</p></td><td><p>COIS-1010H</p></td><td><p>0.5</p></td></tr><tr><td><p>&nbsp;</p></td><td><p>COIS-YR1</p></td><td><p>0.5</p></td></tr><tr><td><p>ENGLISH LANGUAGE AND COMPOSITION</p></td><td><p>ARTS-YR1</p></td><td><p>0.5</p></td></tr><tr><td><p>ENGLISH LITERATURE</p></td><td><p>ARTS-YR1</p></td><td><p>1</p></td></tr><tr><td><p>ENVIRONMENTAL SCIENCE</p></td><td><p>ERSC-YR1</p></td><td><p>1</p></td></tr><tr><td><p>FRENCH LANGUAGE</p></td><td><p>ARTS-YR1</p></td><td><p>1</p></td></tr><tr><td><p>FRENCH LITERATURE</p></td><td><p>ARTS-YR1</p></td><td><p>1</p></td></tr><tr><td><p>GERMAN</p></td><td><p>GRMN-1000Y</p></td><td><p>1</p></td></tr><tr><td><p>HISTORY – AMERICAN</p></td><td><p>HIST-YR1</p></td><td><p>1</p></td></tr><tr><td><p>HISTORY – EUROPE</p></td><td><p>HIST-1200Y</p></td><td><p>1</p></td></tr><tr><td><p>LATIN</p></td><td><p>LATN-1000H</p></td><td><p>0.5</p></td></tr><tr><td><p>&nbsp;</p></td><td><p>LATN-1001H</p></td><td><p>0.5</p></td></tr><tr><td><p>MACROECONOMICS</p></td><td><p>ECON-1020H</p></td><td><p>0.5</p></td></tr><tr><td><p>MICROECONOMICS</p></td><td><p>ECON-1010H</p></td><td><p>0.5</p></td></tr><tr><td><p>MUSIC LITERATURE</p></td><td><p>ARTS-YR1</p></td><td><p>1</p></td></tr><tr><td><p>MUSIC THEORY</p></td><td><p>ARTS-YR1</p></td><td><p>1</p></td></tr><tr><td><p>PHYSICS B</p></td><td><p>SCIE-YR1</p></td><td><p>1</p></td></tr><tr><td><p>PHYSICS C – ELECTRICITY</p></td><td><p>SCIE-YR1</p></td><td><p>0.5</p></td></tr><tr><td><p>PHYSICS C – MECHANICS</p></td><td><p>SCIE-YR1</p></td><td><p>0.5</p></td></tr><tr><td><p>PSYCHOLOGY</p></td><td><p>PSYC-1020H</p></td><td><p>0.5</p></td></tr><tr><td><p>&nbsp;</p></td><td><p>PSYC-1030H</p></td><td><p>0.5</p></td></tr><tr><td><p>SPANISH LANGUAGE</p></td><td><p>ARTS-YR1</p></td><td><p>1</p></td></tr><tr><td><p>SPANISH LITERATURE</p></td><td><p>ARTS-YR1</p></td><td><p>1</p></td></tr><tr><td><p>US. GOVERNMENT</p></td><td><p>POST-YR1</p></td><td><p>0.5</p></td></tr></tbody>'
        print(response.url)
        programme=response.xpath('//h1[@id="page-title"]/text()').extract()
        programme=''.join(programme).strip()
        # print(programme)
        item['major_name_en']=programme

        department=response.xpath('//a[@class="btn-bordered"]/text()').extract()
        department=''.join(department).replace('Program Website','').replace('Math Website','').replace('Physics Website','').replace('Computing Systems Website','').strip()
        # print(department)
        item['department']=department

        overview=response.xpath('//h2[text()="Degrees Offered:"]/../../preceding-sibling::div').extract()
        # print(overview)
        item['overview_en']=remove_class(overview)

        location=response.xpath('//h2[text()="Locations:"]/following-sibling::ul/li/text()').extract()
        # print(location)
        location=list(map(lambda x:x.strip(),location))
        # print(location)
        location=','.join(location)
        item['location']=location

        career=response.xpath('//h2[contains(text(),"areer")]/../following-sibling::div').extract()
        item['career_en']=remove_class(career)

        modurls = response.xpath('//a[contains(text(),"View All Course")]/@href').extract()
        # print(modurls)
        if len(modurls) == 1:
            modRes = etree.HTML(requests.get(modurls[0]).content)
            moduleName = modRes.xpath('//tbody/tr/th/text()')
            # print(moduleName)
            modules = []
            for mN in moduleName:
                # print(mN)
                courseName = modRes.xpath('//th[text()="%s"]/following-sibling::td[1]//strong/text()' % mN)
                # print(courseName)
                modules += '<p>' + mN + '  ' + ''.join(courseName).strip() + '</p>'
                # print(modules)
            item['modules_en'] = remove_class(modules)
        else:
            item['modules_en']=[]
        if item['modules_en']==[]:
            modules1=response.xpath('//h2[contains(text(),"Popular Course")]/following-sibling::ul[1]').extract()
            item['modules_en']=remove_class(modules1)


        entry_requirements_en=response.xpath('//h2[text()="Admission Requirements"]/following-sibling::ul').extract()
        # print(entry_requirements_en)
        item['entry_requirements_en']=remove_class(entry_requirements_en)

        degree_name = response.xpath('//h2[text()="Degrees Offered:"]/following-sibling::ul/li/text()').extract()
        # print(degree_name)
        for dn in degree_name:
            dn=dn.replace('B.E.S.S.','').replace('B.Ed.','Bachelor of Education').replace('B.Bachelor of Art','Bachelor of Art (Honours)').replace('B.A.','Bachelor of Art').replace('B.A. (Honours)','Bachelor of Art (Honours)').replace('B.Sc.','Bachelor of Science').replace('B.Sc. (Honours)','Bachelor of Science (Honours)')
            item['degree_name']=dn
            yield item

