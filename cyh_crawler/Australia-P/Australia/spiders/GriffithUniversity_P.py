# -*- coding: utf-8 -*-
import scrapy
from Australia.middlewares import *
from Australia.items import AustraliaItem
import requests
from lxml import etree
class GriffithuniversityUSpider(scrapy.Spider):
    name = 'GriffithUniversity_P'
    start_urls=['https://degrees.griffith.edu.au/Program/5584/Overview/International',
'https://degrees.griffith.edu.au/Program/5627/Overview/International',
'https://degrees.griffith.edu.au/Program/5558/Overview/International',
'https://degrees.griffith.edu.au/Program/5663/Overview/International',
'https://degrees.griffith.edu.au/Program/5647/Overview/International',
'https://degrees.griffith.edu.au/Program/5714/Overview/International',
'https://degrees.griffith.edu.au/Program/5632/Overview/International',
'https://degrees.griffith.edu.au/Program/5158/Overview/International',
'https://degrees.griffith.edu.au/Program/5731/Overview/International',
'https://degrees.griffith.edu.au/Program/5642/Overview/International',
'https://degrees.griffith.edu.au/Program/5692/Overview/International',
'https://degrees.griffith.edu.au/Program/5702/Overview/International',
'https://degrees.griffith.edu.au/Program/5070/Overview/International',
'https://degrees.griffith.edu.au/Program/5726/Overview/International',
'https://degrees.griffith.edu.au/Program/5703/Overview/International',
'https://degrees.griffith.edu.au/Program/5720/Overview/International',
'https://degrees.griffith.edu.au/Program/5601/Overview/International',
'https://degrees.griffith.edu.au/Program/5668/Overview/International',
'https://degrees.griffith.edu.au/Program/5649/Overview/International',
'https://degrees.griffith.edu.au/Program/5645/Overview/International',
'https://degrees.griffith.edu.au/Program/5643/Overview/International',
'https://degrees.griffith.edu.au/Program/5660/Overview/International',
'https://degrees.griffith.edu.au/Program/5693/Overview/International',
'https://degrees.griffith.edu.au/Program/5611/Overview/International',
'https://degrees.griffith.edu.au/Program/5593/Overview/International',
'https://degrees.griffith.edu.au/Program/5648/Overview/International',
'https://degrees.griffith.edu.au/Program/5592/Overview/International',
'https://degrees.griffith.edu.au/Program/5686/Overview/International',
'https://degrees.griffith.edu.au/Program/5665/Overview/International',
'https://degrees.griffith.edu.au/Program/5724/Overview/International',
'https://degrees.griffith.edu.au/Program/5725/Overview/International',
'https://degrees.griffith.edu.au/Program/5586/Overview/International',
'https://degrees.griffith.edu.au/Program/5618/Overview/International',
'https://degrees.griffith.edu.au/Program/5658/Overview/International',
'https://degrees.griffith.edu.au/Program/5613/Overview/International',
'https://degrees.griffith.edu.au/Program/5612/Overview/International',
'https://degrees.griffith.edu.au/Program/5722/Overview/International',
'https://degrees.griffith.edu.au/Program/5653/Overview/International',
'https://degrees.griffith.edu.au/Program/5311/Overview/International',
'https://degrees.griffith.edu.au/Program/5729/Overview/International',
'https://degrees.griffith.edu.au/Program/5738/Overview/International',
'https://degrees.griffith.edu.au/Program/5631/Overview/International',
'https://degrees.griffith.edu.au/Program/5709/Overview/International',
'https://degrees.griffith.edu.au/Program/5629/Overview/International',
'https://degrees.griffith.edu.au/Program/5733/Overview/International',
'https://degrees.griffith.edu.au/Program/5298/Overview/International',
'https://degrees.griffith.edu.au/Program/5280/Overview/International',
'https://degrees.griffith.edu.au/Program/5587/Overview/International',
'https://degrees.griffith.edu.au/Program/5683/Overview/International',
'https://degrees.griffith.edu.au/Program/5728/Overview/International',
'https://degrees.griffith.edu.au/Program/5263/Overview/International',
'https://degrees.griffith.edu.au/Program/5701/Overview/International',
'https://degrees.griffith.edu.au/Program/5572/Overview/International',
'https://degrees.griffith.edu.au/Program/5700/Overview/International',
'https://degrees.griffith.edu.au/Program/5621/Overview/International',
'https://degrees.griffith.edu.au/Program/5567/Overview/International',
'https://degrees.griffith.edu.au/Program/5706/Overview/International',
'https://degrees.griffith.edu.au/Program/5727/Overview/International',
'https://degrees.griffith.edu.au/Program/5576/Overview/International',]
    start_urls=set(start_urls)
    def parse(self, response):
        item=get_item(AustraliaItem)
        item['university']='Griffith University'
        item['url']=response.url
        programme=response.xpath('//div[@class="col-xs-12"]/h1/text()').extract()
        item['programme_en']=''.join(programme).replace('Master of ','').strip()
        item['degree_name']=''.join(programme).strip()
        duration=response.xpath('//h2[contains(text(),"Duration")]/../following-sibling::div/p/text()').extract()
        duration=clear_duration(duration)
        item['duration']=duration['duration']
        item['duration_per']=duration['duration_per']
        location=response.xpath('//div[@class="h-box gry-grad"]/p/text()|//div[@class="h-box gry-grad "]/p/text()').extract()
        location=','.join(location).strip()
        item['location']=location
        fee=response.xpath('//p[contains(text(),"$")]/text()').extract()
        fee=getTuition_fee(fee)
        item['tuition_fee']=fee
        item['tuition_fee_pre']='AUD'
        deg_overview=response.xpath('//h2[contains(text(),"Why choose")]/following-sibling::div[1]').extract()
        deg_overview=remove_class(deg_overview)
        item['degree_overview_en']=deg_overview
        career=response.xpath('//div[@id="opportunities"]').extract()
        career=remove_class(career)
        item['career_en']=career
        gaokao=['<p>Successful completion of the National College Entrance Examination (Gao Kao) with a minimum of 63% of the overall maximum score</p>'+'\n','<p>Grade average of 90 in the final year results OR successful completion of a recognised pre-tertiary or foundation program OR successful completion of one year study at a recognised tertiary or higher education institution is required in addition to the completion of High School studies.</p>']
        gaokao=remove_class(gaokao)
        item['china_score_requirements']=gaokao
        how_to_apply_ulr=response.url.replace('Overview','HowToApply')
        htps=self.how_to_apply(how_to_apply_ulr)
        ielts=get_ielts(htps.xpath('//*[contains(text(),"IELTS")]/../text()'))
        item['ielts_desc']=remove_class(htps.xpath('//*[contains(text(),"IELTS")]/../text()'))
        if ielts!=[]:
            item['ielts']=ielts['IELTS']
            item['ielts_l']=ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
        toefl=re.findall('[1]?[217890]\d',''.join(htps.xpath('//*[contains(text(),"iBT")]//text()')))
        item['toefl_desc']=remove_class(htps.xpath('//*[contains(text(),"iBT")]//text()'))
        if len(toefl)==2:
            toefl=list(map(int,toefl))
            item['toefl']=max(toefl)
            item['toefl_l']=min(toefl)
            item['toefl_s'] = min(toefl)
            item['toefl_r'] = min(toefl)
            item['toefl_w'] = min(toefl)
        modules_url=response.url.replace('Overview','Courses')
        modu=self.how_to_apply(modules_url)
        degree_requ=modu.xpath('//div[@id="degree-requirements"]//text()')
        degree_requ=clear_long_text(degree_requ)
        item['degree_requirements']=degree_requ
        modules=modu.xpath('//div[@id="course-list-content"]//td[@class="name"]/text()')
        modules=clear_long_text(modules)
        item['modules_en']=modules
        major_name = response.xpath('//h4[contains(text(),"MAJORS")]/following-sibling::p/strong/text()|//h2[contains(text(),"Why choose")]/following-sibling::div[1]//*[contains(text(),"ajor")]/following-sibling::ul/li//text()').extract()
        #专业页面上如果匹配到了专业，根据专业名字逐条插入。
        if major_name != []:
            for maj in major_name:
                maj=maj.strip()
                item['programme_en'] = maj
                yield item
        else:
            yield item
    def how_to_apply(self,url):
        try:
            responses=requests.get(url).content
            responses=etree.HTML(responses)
            return responses
        except:
            return ''




