# -*- coding: utf-8 -*-
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.getItem import *
from scrapySchool_Canada_College.items import *

class KwantlenpolytechnicuniversitySpider(scrapy.Spider):
    name = 'KwantlenPolytechnicUniversity'
    # allowed_domains = ['a.b']
    start_urlss = ['http://www.kpu.ca/calendar/2018-19/arts/psychology/psychology-applied-deg.html',
'http://www.kpu.ca/calendar/2018-19/arts/geography/geographyapplied-major.html',
'http://www.kpu.ca/calendar/2018-19/arts/generalstudies/generalstudies-ba.html',
'http://www.kpu.ca/calendar/2018-19/arts/anthropology/anthropology-major.html',
'http://www.kpu.ca/calendar/2018-19/arts/asianstudies/asianstudies-major.html',
'http://www.kpu.ca/calendar/2018-19/arts/creativewriting/creativewriting-major.html',
'http://www.kpu.ca/calendar/2018-19/arts/criminology/criminology-major.html',
'http://www.kpu.ca/calendar/2018-19/arts/english/english-major.html',
'http://www.kpu.ca/calendar/2018-19/arts/philosophy/philosophy-major.html',
'http://www.kpu.ca/calendar/2018-19/arts/policystudies/policystudies-major.html',
'http://www.kpu.ca/calendar/2018-19/arts/politicalscience/politicalscience-major.html',
'http://www.kpu.ca/calendar/2018-19/arts/psychology/psychology-major.html',
'http://www.kpu.ca/calendar/2018-19/arts/sociology/sociology-major.html',
'http://www.kpu.ca/calendar/2018-19/business/accounting/accounting-bba.html',
'http://www.kpu.ca/calendar/2018-19/business/entrepreneurialleadership/entrepreneurialleadership-bba.html',
'http://www.kpu.ca/calendar/2018-19/business/humanresourcesmanagement/humanresourcesmanagement-bba.html',
'http://www.kpu.ca/calendar/2018-19/business/marketing/marketingmanagement-bba.html',
'http://www.kpu.ca/calendar/2018-19/design/graphicdesignmarketing/graphicdesignmarketing-deg.html',
'http://www.kpu.ca/calendar/2018-19/design/productdesign/productdesign-deg.html',
'http://www.kpu.ca/calendar/2018-19/arts/finearts/finearts-deg.html',
'http://www.kpu.ca/calendar/2018-19/science-hort/planthealth/planthealth-deg.html',
'http://www.kpu.ca/calendar/2018-19/science-hort/urbanecosystems/urbanecosystems-deg.html',
'http://www.kpu.ca/calendar/2018-19/arts/journalism/journalism-deg.html',
'http://www.kpu.ca/calendar/2018-19/design/interiordesign/interiordesign-deg.html',
'http://www.kpu.ca/calendar/2018-19/arts/music/general-bmma-deg.html',
'http://www.kpu.ca/calendar/2018-19/arts/psychology/psychology-applied-bsc.html',
'http://www.kpu.ca/calendar/2018-19/science-hort/biology/biology-bsc.html',
'http://www.kpu.ca/calendar/2018-19/science-hort/healthscience/healthscience-bsc.html',
'http://www.kpu.ca/calendar/2018-19/science-hort/mathematics/mathematicsapplications-major.html',
'http://www.kpu.ca/calendar/2018-19/science-hort/physics/physicsformoderntechnology-bsc.html',
'http://www.kpu.ca/calendar/2018-19/business/informationtechnology/informationtechnology-deg.html',
'http://www.kpu.ca/calendar/2018-19/science-hort/sustainableagriculture/sustainableagriculture-deg.html',]
    start_urlss=['http://www.kpu.ca/calendar/2018-19/arts/counselling/counselling-minor.html',
'http://www.kpu.ca/calendar/2018-19/design/fashionandtechnology/fashiontechnology-deg.html',
'http://www.kpu.ca/calendar/2018-19/arts/generalarts/arts-dip.html',
'http://www.kpu.ca/calendar/2018-19/arts/generalarts/arts-cert.html',]
    start_urls=set(start_urlss)
    def parse(self, response):
        item=get_item(ScrapyschoolCanadaCollegeItem)
        item['school_name']='Kwantlen Polytechnic University'
        item['url']=response.url
        item['location']='British Columbia'
        item['average_score']='60'
        item['toefl_desc']='iBT 88 or higher, with no sub score less than 20, taken within the last two years from the term of admission'
        item['toefl'],item['toefl_l'],item['toefl_s'],item['toefl_r'],item['toefl_w']='88','20','20','20','20'
        item['ielts_desc'] = 'overall band of 6.5 or higher, with a minimum 6.0 in each band, taken within the last two years from the term of admission'
        item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w'] = '6.5', '6.0', '6.0', '6.0', '6.0'
        item['tuition_fee'],item['tuition_fee_pre'],item['tuition_fee_per']='658.03','$','5'
        item['apply_fee'],item['apply_pre']='120.00','$'
        item['other']='1.没有deadline,中国学生要求 2.duration,career不一定有'
        print(response.url)
        degree_name=response.xpath('//h3[text()="Credential Granted:"]/following-sibling::ul[1]/li/text()').extract()
        item['degree_name']=''.join(degree_name)
        programme=response.xpath('//h1/text()').extract()
        # print(programme)
        item['major_name_en']=''.join(programme)
        department=response.xpath('//h2[text()="At a Glance"]/following-sibling::h3[1]/text()').extract()
        # print(department)
        item['department']=''.join(department)
        start_date=response.xpath('//h3[contains(text(),"Start Date")]/following-sibling::ul[1]/li/text()').extract()
        # print(start_date)
        start_date=tracslateDate(start_date)
        # print(start_date)
        item['start_date']=','.join(start_date).replace('-9','-09').replace('-1','-01').replace('-5','-05')
        campus=response.xpath('//h3[contains(text(),"Offered At:")]/following-sibling::ul[1]/li/text()').extract()
        campus=list(map(lambda x:x.replace('\xa0 \n\t\t\t\t\t\t\t',''),campus))
        # print(campus)
        item['degree_name']=''.join(degree_name).strip()
        degree_name=''.join(degree_name)
        if 'Diploma' in degree_name:
            item['degree_level']='3'
        if 'Associate' in degree_name:
            item['degree_level']='4'
        if 'Bachelor' in degree_name:
            item['degree_level']='1'


        modules=response.xpath('//h2[contains(text(),"Curricular Requirements")]/following-sibling::table').extract()
        item['modules_en']=remove_class(modules)

        duration=response.xpath('//h2[contains(text(),"Curricular Requirements")]/following-sibling::h3[contains(text(),"ear")]/text()').extract()
        # print(duration)
        if duration != []:
            duration=list(map(lambda x:x.replace('Two','2').replace('Second','2'),duration))
            duration=re.findall('\d+',' '.join(duration))
            duration=list(map(int,duration))
            item['duration']=max(duration)
            item['duration_per']='1'

        alls=response.xpath('//div[@class="content"]/*').extract()
        #标题
        des=response.xpath('//h2[contains(text(),"escription")]/self::*').extract()[0]
        # print(des)
        ar=response.xpath('//h2[contains(text(),"Admission Requirements")]/self::*').extract()[0]
        cr=response.xpath('//h2[contains(text(),"Curricular Requirements")]/self::*').extract()[0]
        career = response.xpath('//h2[contains(text(),"areer")]/self::*').extract()
        career_next=response.xpath('//h2[contains(text(),"areer")]/following-sibling::h2[1]/self::*').extract()
        # item['career_en']=remove_class(career)
        if career != []:
            career=alls[alls.index(career[0]):alls.index(career_next[0])]
            item['career_en']=remove_class(career)
        overview=alls[alls.index(des):alls.index(ar)]
        entry_requirements=alls[alls.index(ar):alls.index(cr)]
        item['overview_en']=remove_class(overview)
        item['entry_requirements_en']=remove_class(entry_requirements)
        if campus!=[]:
            for ca in campus:
                item['campus']=ca
                yield item
        else:
            item['campus']=','.join(campus).strip()
            yield item