# -*- coding: utf-8 -*-
import scrapy
from Australia.middlewares import *
from Australia.items import AustraliaItem
import requests
from lxml import etree
class MonashuniversityUSpider(scrapy.Spider):
    name = 'MonashUniversity_U'
    start_urls = ['https://www.monash.edu/study/courses/find-a-course?f.Tabs%7CcourseTab=Undergraduate&f.InterestAreas%7CcourseInterestAreas=']
    def parse(self, response):
        pro_url = response.xpath('//h2/a/@title').extract()
        # for i in pro_url:
        #     yield scrapy.Request(i,callback=self.parses)
        programme = response.xpath('//h2/a/text()').extract()
        for url, pro in zip(pro_url, programme):
            pro = pro.strip()
            deg_xpath = '//a[contains(@title,"' + url + '")]/../../following-sibling::span/text()'
            degree_name = response.xpath(deg_xpath).extract()
            degree_name = ''.join(degree_name).strip()
            if  '/' in degree_name or 'Diploma' in degree_name:
                pass
            else:
                # print('下载',response.url)
                yield scrapy.Request(url=url,callback=self.parses)
    def parses(self, response):
        item = get_item(AustraliaItem)
        item['university'] = 'Monash University'
        item['url'] = response.url
        print(response.url)
        programme = response.xpath('//strong[@class="h1"]/text()').extract()
        programme = ''.join(programme).strip()
        item['programme_en'] = programme
        degree_name = response.xpath('//th[contains(text(),"Qualification")]/following-sibling::td/text()').extract()
        degree_name = ''.join(degree_name)
        if degree_name == '':
            degree_name = 'Bachelor of ' +programme
        item['degree_name'] = degree_name
        location = 'Melbourne'
        item['location'] = location
        start_date = response.xpath('//th[contains(text(),"Start date")]/following-sibling::td/text()').extract()
        start_date = tracslateDate(start_date)
        start_date = ','.join(start_date)
        item['start_date'] = start_date
        rntry_requirement = response.xpath('//div[@id="entry-requirements-2"]').extract()
        rntry_requirement = remove_class(rntry_requirement)
        item['rntry_requirements_en'] = rntry_requirement
        modules = response.xpath('//div[@id="course-structure-3"]').extract()
        modules = remove_class(modules)
        item['modules_en'] = modules
        degree_overview = response.xpath('//div[@class="course-page__overview-panel standard-course"]').extract()
        degree_overview = remove_class(degree_overview)
        item['degree_overview_en'] = degree_overview
        item['ielts'] = '6.5'
        item['ielts_l'] = '6.0'
        item['ielts_s'] = '6.0'
        item['ielts_r'] = '6.0'
        item['ielts_w'] = '6.0'
        item['toefl'] = '79'
        item['toefl_l'] = '12'
        item['toefl_s'] = '18'
        item['toefl_r'] = '13'
        item['toefl_w'] = '21'
        fee = response.xpath(
            '//strong[contains(text(),"$")]//text()|//p[contains(text(),"Domestic Annual Fee")]//text()').extract()
        tuition_fee = getTuition_fee(fee)
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = 'AUD'
        major_name = response.xpath('//p[@id="specialisations"]/following-sibling::ul/li/a/text()|//ul[@class="majors"]/li/a/text()').extract()
        major_url = response.xpath('//p[@id="specialisations"]/following-sibling::ul/li/a/@data-href|//ul[@class="majors"]/li/a/@data-href').extract()
        duration=response.xpath('//th[contains(text(),"Duration")]/following-sibling::*//text()').extract()
        duration=''.join(duration).strip()
        mode=re.findall('(?i)full',duration)
        overview = response.xpath('//div[@id="overview-tab-content"]').extract()
        item['overview_en']=remove_class(overview)
        deprtment_url = response.xpath('//p[@id="faculty-link"]/a/@href').extract()
        if deprtment_url != []:
            department = self.getDepartment(deprtment_url[0])
            item['department'] = ''.join(department)
        if mode!=[]:
            dura=re.findall('\d',duration)
            dura=list(map(int,dura))
            item['duration']=min(dura)
            item['duration_per']=1
            if major_url!=[]:
                for j,name in zip(major_url,major_name):
                    majorOverview = self.getMajorOverview(j)
                    majMod=''
                    for mM in majorOverview:
                        majMod+=etree.tostring(mM,method='html',encoding='unicode')
                    majorOverview = remove_class(majMod)
                    item['programme_en'] = name.strip()
                    item['overview_en'] = majorOverview
                    # print('有专业:',j)
                    yield item
            else:
                # print('无专业:',response.url)
                yield item
        else:
            print('课程长度为',duration,'只有兼职，不要')

    def getDepartment(self,url):
        depResponse=requests.get(url).content
        depResponse=etree.HTML(depResponse)
        department=depResponse.xpath('//div[@class="content-wrapper"]/h2/text()')
        return department
    def getMajorOverview(self,url):
        try:
            moResponse = etree.HTML(requests.get(url).content)
            mo = moResponse.xpath('//button[contains(text(),"Choose another")]/following-sibling::*')
            return mo
        except:
            return None

