# -*- coding: utf-8 -*-
from scrapySchool_Canada_College.items import *
from scrapySchool_Canada_College.getItem import *
from scrapySchool_Canada_College.middlewares import *

class BritishcolumbiainstituteoftechnologySpider(scrapy.Spider):
    name = 'BritishColumbiaInstituteofTechnology'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.bcit.ca/study/programs/5063dipma',
'https://www.bcit.ca/study/programs/537adiplt',
'https://www.bcit.ca/study/programs/537bdiplt',
'https://www.bcit.ca/study/programs/9940bsc',
'https://www.bcit.ca/study/programs/8040bsc',
'https://www.bcit.ca/study/programs/8060btech',
'https://www.bcit.ca/study/programs/8500dbtech',
'https://www.bcit.ca/study/programs/7930dipma',
'https://www.bcit.ca/study/programs/500adiplt',
'https://www.bcit.ca/study/programs/8320bsc',
'https://www.bcit.ca/study/programs/7470dipma',
'https://www.bcit.ca/study/programs/9100fadvdip',
'https://www.bcit.ca/study/programs/8640bsc',
'https://www.bcit.ca/study/programs/7530dipma',
'https://www.bcit.ca/study/programs/8910bsc',
'https://www.bcit.ca/study/programs/6640dipma',
'https://www.bcit.ca/study/programs/8610beng',
'https://www.bcit.ca/study/programs/6540dipma',
'https://www.bcit.ca/study/programs/8630bacc',
'https://www.bcit.ca/study/programs/5740diplt',
'https://www.bcit.ca/study/programs/100adipma',
'https://www.bcit.ca/study/programs/100bdipma',
'https://www.bcit.ca/study/programs/1015dipts',
'https://www.bcit.ca/study/programs/9950bba',
'https://www.bcit.ca/study/programs/6135dipma',
'https://www.bcit.ca/study/programs/6235diplt',
'https://www.bcit.ca/study/programs/5312advdip',
'https://www.bcit.ca/study/programs/6245diplt',
'https://www.bcit.ca/study/programs/5210diplt',
'https://www.bcit.ca/study/programs/6910diplt',
'https://www.bcit.ca/study/programs/6405dipma',
'https://www.bcit.ca/study/programs/5730diplt',
'https://www.bcit.ca/study/programs/5720diplt',
'https://www.bcit.ca/study/programs/5880diplt',
'https://www.bcit.ca/study/programs/6180dipma',
'https://www.bcit.ca/study/programs/625adiplt',
'https://www.bcit.ca/study/programs/5950diplt',
'https://www.bcit.ca/study/programs/745adiplt',
'https://www.bcit.ca/study/programs/745bdiplt',
'https://www.bcit.ca/study/programs/630hdiplt',
'https://www.bcit.ca/study/programs/6300dipma',
'https://www.bcit.ca/study/programs/63aadiplt',
'https://www.bcit.ca/study/programs/630vdiplt',
'https://www.bcit.ca/study/programs/63abdipma',
'https://www.bcit.ca/study/programs/6525dipma',
'https://www.bcit.ca/study/programs/6110dipma',
'https://www.bcit.ca/study/programs/6130dipma',
'https://www.bcit.ca/study/programs/6540dipma',
'https://www.bcit.ca/study/programs/6235diplt',
'https://www.bcit.ca/study/programs/1930dipma',
'https://www.bcit.ca/study/programs/5540dipma',
'https://www.bcit.ca/study/programs/862bbtech',
'https://www.bcit.ca/study/programs/862cbtech',
'https://www.bcit.ca/study/programs/5500dipma',
'https://www.bcit.ca/study/programs/6405dipma',
'https://www.bcit.ca/study/programs/534cdipma',
'https://www.bcit.ca/study/programs/6180dipma',
'https://www.bcit.ca/study/programs/6525dipma',
'https://www.bcit.ca/study/programs/1010dipts',
'https://www.bcit.ca/study/programs/8050btech',
'https://www.bcit.ca/study/programs/7140dipma',
'https://www.bcit.ca/study/programs/1130dipma',
'https://www.bcit.ca/study/programs/5063dipma',
'https://www.bcit.ca/study/programs/m200masc',
'https://www.bcit.ca/study/programs/m100meng',
'https://www.bcit.ca/study/programs/537adiplt',
'https://www.bcit.ca/study/programs/537bdiplt',
'https://www.bcit.ca/study/programs/8660beng',
'https://www.bcit.ca/study/programs/5410diplt',
'https://www.bcit.ca/study/programs/8800btech',
'https://www.bcit.ca/study/programs/534adipma',
'https://www.bcit.ca/study/programs/534bdipma',
'https://www.bcit.ca/study/programs/534cdipma',
'https://www.bcit.ca/study/programs/8060btech',
'https://www.bcit.ca/study/programs/9100fadvdip',
'https://www.bcit.ca/study/programs/8640bsc',
'https://www.bcit.ca/study/programs/7530dipma',
'https://www.bcit.ca/study/programs/2945dipma',
'https://www.bcit.ca/study/programs/8830bid',
'https://www.bcit.ca/study/programs/6160fdipma',
'https://www.bcit.ca/study/programs/635ddiplt',
'https://www.bcit.ca/study/programs/635ediplt',
'https://www.bcit.ca/study/programs/635cdiplt',
'https://www.bcit.ca/study/programs/7340diplt',
'https://www.bcit.ca/study/programs/6640dipma',
'https://www.bcit.ca/study/programs/8610beng',
'https://www.bcit.ca/study/programs/278bdipma',
'https://www.bcit.ca/study/programs/278adipma',
'https://www.bcit.ca/study/programs/5063dipma',
'https://www.bcit.ca/study/programs/8500dbtech',
'https://www.bcit.ca/study/programs/500adiplt',
'https://www.bcit.ca/study/programs/8320bsc',
'https://www.bcit.ca/study/programs/8910bsc',
'https://www.bcit.ca/study/programs/6850diplt',
'https://www.bcit.ca/study/programs/1010dipts',
'https://www.bcit.ca/study/programs/100adipma',
'https://www.bcit.ca/study/programs/100bdipma',
'https://www.bcit.ca/study/programs/1015dipts',
'https://www.bcit.ca/study/programs/1430dipma',
'https://www.bcit.ca/study/programs/143bdipma',
'https://www.bcit.ca/study/programs/1130dipma',
'https://www.bcit.ca/study/programs/2945dipma',
'https://www.bcit.ca/study/programs/8830bid',
'https://www.bcit.ca/study/programs/6160fdipma',
'https://www.bcit.ca/study/programs/278bdipma',
'https://www.bcit.ca/study/programs/278adipma',
]

    def parse(self, response):
        item=get_item(ScrapyschoolCanadaCollegeItem)
        item['school_name']='British Columbia Institute of Technology'
        item['url']=response.url
        item['location']='Vancouver'
        item['apply_fee'],item['apply_pre']='154','CAD$'
        item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w'],item['toefl']='6.5','6.0','6.0','6.0','6.0','86'
        print(response.url)
        item['other']='1.学费、课程长度、开课日期页面上不一定有 2.没有找到平均分要求 3.托佛只有一个总分要求'
        programme=response.xpath('//div[@class="program_title banner_title"]/text()').extract()
        item['require_chinese_en']='<p>12 years of education (includes three years of senior secondary)</p><ul><li>Certificate of Graduation from Senior Secondary School</li><li>High School Diploma</li><li>Upper Middle School Graduation Certificate</li></ul>'
        # print(programme)
        item['major_name_en']=programme[0]
        department=response.xpath('//div[@id="schoolname"]/a/text()').extract()
        # print(department)
        item['department']=department[0]

        degree_name=response.xpath('//span[@class="program_credential"]/text()').extract()
        # print(degree_name)
        item['degree_name']=degree_name[0]

        modules=response.xpath('//div[@id="courses"]//table').extract()
        clearm=response.xpath('//div[@id="courses"]//table//td/div').extract()
        for cm in clearm:
            modules=list(map(lambda x:x.replace(cm,'').replace('\n','').replace('\xa0',''),modules))
        # print(modules)
        item['modules_en']=remove_class(modules).replace('<div>course outline  </div>','')
        print(item['modules_en'])

        career=response.xpath('//div[@id="graduating"]//ul').extract()
        item['career_en']=remove_class(career)

        entry_requirement=response.xpath('//div[@id="requirements"]').extract()
        entry_requirement=''.join(entry_requirement)
        item['entry_requirements_en']=remove_class(entry_requirement)

        overview=response.xpath('//div[@id="overview"]').extract()
        item['overview_en']=remove_class(overview)

        tuition=response.xpath('//strong[text()="International Tuition:"]/following-sibling::a[1]/text()').extract()
        item['tuition_fee_pre']='$'
        # print(tuition)
        item['tuition_fee']=''.join(tuition).replace('$','')

        dur=response.xpath('//h3[contains(text(),"Program Overview")]/../text()').extract()
        # print(dur)
        dura=response.xpath('//h2[contains(text(),"Program length")]/following-sibling::p/text()').extract()
        # print(dura)
        durat=clear_duration(dura)
        # print(durat)
        item['duration']=durat['duration']
        item['duration_per']=durat['duration_per']

        start_date=tracslateDate(dur)
        # print(start_date)
        item['start_date']=','.join(start_date)

        campus=response.xpath('//h2[contains(text(),"Program location")]/following-sibling::p/a/text()').extract()
        # print(campus)
        campus=set(campus)
        # if campus!=[]:
        #     for cam in campus:
        #         if 'Campus' in cam:
        #             item['campus']=cam
        #             # print(cam)
        #             yield item
        # else:
        #     yield item
            # print(campus)
        yield item