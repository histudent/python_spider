# -*- coding: utf-8 -*-
import scrapy
from Australia.middlewares import *
from Australia.items import AustraliaItem
import requests,json
from lxml import etree
class TheuniversityofsydneyUSpider(scrapy.Spider):
    name = 'TheUniversityOfSydney_P'
    # allowed_domains = ['a.b']

    start_urls = []
    for ng in [1,2, 3, 4, 5,6,7,8,9,10,11,12,13]:
        full_page = 'https://sydney.edu.au/content/courses/search.result-courses.aoi-.course-level-pc.page' + str(
            ng) + '.html'
        start_urls.append(full_page)
    def parse(self, response):
        urls=response.xpath('//ul/li/a/@href').extract()
        for u in urls:
            if 'master' in u:
                full_url='https://sydney.edu.au'+u
                # print(full_url)
                yield scrapy.Request(url=full_url,callback=self.parse_main)
    def parse_main(self,response):
        item=get_item(AustraliaItem)
        item['url']=response.url
        print(response.url)
        item['university'] = 'The University of Sydney'
        degree_name=response.xpath('//h2[@class="pageTitle pageTitle__course"]/div/text()').extract()
        item['degree_name']=''.join(degree_name)
        item['degree_type']='2'
        dep_url=response.url.replace('.html','.details.json')
        department=json.loads(requests.get(dep_url).content)['facultyTitle']
        item['department']=department
        feeurl=response.url.replace('.html','.fee.json')
        fee=json.loads(requests.get(feeurl).content)
        TUI=fee['courseFee']['2019']
        # print(TUI)
        for t in TUI:
            if t['type']=='INTFEE':
                try:
                    item['tuition_fee']=t['amount'].replace('$','').replace(',','').strip()
                except:
                    pass
                # print(item['tuition_fee'])
        item['tuition_fee_pre']='AUD$'

        entUrl=response.url.replace('.html','.entryrequirement.json')
        entry=json.loads(requests.get(entUrl).content)
        try:
            IELTSTOEFL=entry['courseEntryRequirements']['2019']['GenericENG']
            TOEFL=IELTSTOEFL[0]['erqText']
            IELTS=IELTSTOEFL[1]['erqText']
            toefl=re.findall('\d{2,}',TOEFL)
            ielts=re.findall('\d\.\d',IELTS)
            item['ielts_desc']=IELTS
            item['toefl_desc']=TOEFL
            # print(ielts)
            if len(toefl[0])==3:
                item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']=ielts[0],ielts[2],ielts[2],ielts[1],ielts[1]
                item['toefl'],item['toefl_l'],item['toefl_s'],item['toefl_r'],item['toefl_w']=toefl[0],toefl[2],toefl[2],toefl[1],toefl[1]
            else:
                item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w'] = ielts[0], ielts[1],  ielts[1], ielts[1], ielts[1]
                item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w'] = toefl[0], toefl[1],toefl[1], toefl[1], toefl[2]
        except:
            pass
        # print(item['ielts_l'],item['ielts_w'],item['toefl_l'],item['toefl_w'])
        rntry_requirements=response.xpath('//h3[contains(text(),"requirement")]/following-sibling::p|//h3[contains(text(),"Admission criteria")]/following-sibling::*').extract()
        item['rntry_requirements_en']=remove_class(rntry_requirements)
        career=response.xpath('//div[@class="course-rte-common parbase"]').extract()
        item['career_en']=remove_class(career)
        module_en=response.xpath('//h4[contains(text(),"ll study")]/following-sibling::div[@class="b-see-more-content b-js-see-more-content b-text--size-base"]').extract()
        item['module_en']=remove_class(module_en)
        degree_overview=response.xpath('//h3[contains(text(),"verview")]/following-sibling::div').extract()
        item['degree_overview_en']=remove_class(degree_overview)
        duration=re.findall('Duration full time:[ \.0-9a-zA-Z]+',response.text)
        dura=re.findall('\d\.?5?',''.join(duration))
        if dura!=[]:
            item['duration']=''.join(set(dura)).strip()
            item['duration_per']=1
        location=re.findall('Location:[ a-zA-Z/]+',response.text)
        item['location']=''.join(location).replace('Location:','').strip()
        start_date=re.findall('<p>Semester[0-9a-zA-Z\(\)\s]+',response.text)
        start_date=set(tracslateDate(start_date))
        item['start_date']=','.join(start_date)
        majorUrl = response.url.replace('.html', '.pathways.json')
        majorlist = json.loads(requests.get(majorUrl).content)
        if majorlist != {}:
            majorurl = majorlist['2020'] + majorlist['2019']
            mus = []
            for mu in majorurl:
                if 'minor' not in mu['href']:
                    mus.append('https://sydney.edu.au' + mu['href'])
            for murl in set(mus):
                mresponse = etree.HTML(requests.get(murl).content)
                programme = mresponse.xpath('//h2[@class="pageTitle"]/text()')
                item['programme_en'] = ''.join(programme).strip()
                career=mresponse.xpath('//h3[contains(text(),"opportunities")]/following-sibling::div//div[contains(@class,"hidden")]|//h3[contains(text(),"areer Pathways")]/following-sibling::div//div[contains(@class,"hidden")]')
                ca=[]
                for c in career:
                    ca+=etree.tostring(c,method='html',encoding='unicode')
                item['career_en']=remove_class(ca)
                overview = mresponse.xpath('//div[contains(@class,"ubject-area-overview")]//div[contains(@class,"hidden")]')
                ov = []
                for o in overview:
                    ov+=etree.tostring(o,method='html',encoding='unicode')
                item['overview_en']=remove_class(ov)
                yield item
        else:
            prog=''.join(degree_name).replace('(Honours)','')
            # if '(' in prog:
            #     programme=re.findall('\(.+\)',prog)
            #     item['programme_en']=''.join(programme).replace('(','').replace(')','').strip()
            # elif ' in ' in prog:
            #     programme=re.findall(' in .+',prog)
            #     item['programme_en']=''.join(programme).replace(' in ','').strip()
            # else:
            item['programme_en']=prog.replace('Master of ','').strip()
            yield item
