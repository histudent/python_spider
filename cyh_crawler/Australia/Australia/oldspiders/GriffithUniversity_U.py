# -*- coding: utf-8 -*-
import scrapy
from Australia.middlewares import *
from Australia.items import AustraliaItem
import requests
from lxml import etree
class GriffithuniversityUSpider(scrapy.Spider):
    name = 'GriffithUniversity_U'
    start_urls=['https://degrees.griffith.edu.au/Program/1012/Courses/International',
'https://degrees.griffith.edu.au/Program/1014/Courses/International',
'https://degrees.griffith.edu.au/Program/1016/Courses/International',
'https://degrees.griffith.edu.au/Program/1016/Courses/International',
'https://degrees.griffith.edu.au/Program/1016/Courses/International',
'https://degrees.griffith.edu.au/Program/1016/Courses/International',
'https://degrees.griffith.edu.au/Program/1016/Courses/International',
'https://degrees.griffith.edu.au/Program/1016/Courses/International',
'https://degrees.griffith.edu.au/Program/1016/Courses/International',
'https://degrees.griffith.edu.au/Program/1021/Courses/International',
'https://degrees.griffith.edu.au/Program/1021/Courses/International',
'https://degrees.griffith.edu.au/Program/1021/Courses/International',
'https://degrees.griffith.edu.au/Program/1021/Courses/International',
'https://degrees.griffith.edu.au/Program/1021/Courses/International',
'https://degrees.griffith.edu.au/Program/1021/Courses/International',
'https://degrees.griffith.edu.au/Program/1021/Courses/International',
'https://degrees.griffith.edu.au/Program/1021/Courses/International',
'https://degrees.griffith.edu.au/Program/1021/Courses/International',
'https://degrees.griffith.edu.au/Program/1021/Courses/International',
'https://degrees.griffith.edu.au/Program/1021/Courses/International',
'https://degrees.griffith.edu.au/Program/1021/Courses/International',
'https://degrees.griffith.edu.au/Program/1031/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1034/Courses/International',
'https://degrees.griffith.edu.au/Program/1035/Courses/International',
'https://degrees.griffith.edu.au/Program/1035/Courses/International',
'https://degrees.griffith.edu.au/Program/1035/Courses/International',
'https://degrees.griffith.edu.au/Program/1093/Courses/International',
'https://degrees.griffith.edu.au/Program/1094/Courses/International',
'https://degrees.griffith.edu.au/Program/1095/Courses/International',
'https://degrees.griffith.edu.au/Program/1095/Courses/International',
'https://degrees.griffith.edu.au/Program/1098/Courses/International',
'https://degrees.griffith.edu.au/Program/1105/Courses/International',
'https://degrees.griffith.edu.au/Program/1105/Courses/International',
'https://degrees.griffith.edu.au/Program/1105/Courses/International',
'https://degrees.griffith.edu.au/Program/1105/Courses/International',
'https://degrees.griffith.edu.au/Program/1105/Courses/International',
'https://degrees.griffith.edu.au/Program/1105/Courses/International',
'https://degrees.griffith.edu.au/Program/1105/Courses/International',
'https://degrees.griffith.edu.au/Program/1105/Courses/International',
'https://degrees.griffith.edu.au/Program/1105/Courses/International',
'https://degrees.griffith.edu.au/Program/1105/Courses/International',
'https://degrees.griffith.edu.au/Program/1105/Courses/International',
'https://degrees.griffith.edu.au/Program/1105/Courses/International',
'https://degrees.griffith.edu.au/Program/1105/Courses/International',
'https://degrees.griffith.edu.au/Program/1105/Courses/International',
'https://degrees.griffith.edu.au/Program/1105/Courses/International',
'https://degrees.griffith.edu.au/Program/1105/Courses/International',
'https://degrees.griffith.edu.au/Program/1107/Courses/International',
'https://degrees.griffith.edu.au/Program/1116/Courses/International',
'https://degrees.griffith.edu.au/Program/1116/Courses/International',
'https://degrees.griffith.edu.au/Program/1116/Courses/International',
'https://degrees.griffith.edu.au/Program/1116/Courses/International',
'https://degrees.griffith.edu.au/Program/1116/Courses/International',
'https://degrees.griffith.edu.au/Program/1116/Courses/International',
'https://degrees.griffith.edu.au/Program/1116/Courses/International',
'https://degrees.griffith.edu.au/Program/1116/Courses/International',
'https://degrees.griffith.edu.au/Program/1116/Courses/International',
'https://degrees.griffith.edu.au/Program/1116/Courses/International',
'https://degrees.griffith.edu.au/Program/1161/Courses/International',
'https://degrees.griffith.edu.au/Program/1162/Courses/International',
'https://degrees.griffith.edu.au/Program/1165/Courses/International',
'https://degrees.griffith.edu.au/Program/1171/Courses/International',
'https://degrees.griffith.edu.au/Program/1178/Courses/International',
'https://degrees.griffith.edu.au/Program/1179/Courses/International',
'https://degrees.griffith.edu.au/Program/1181/Courses/International',
'https://degrees.griffith.edu.au/Program/1186/Courses/International',
'https://degrees.griffith.edu.au/Program/1186/Courses/International',
'https://degrees.griffith.edu.au/Program/1186/Courses/International',
'https://degrees.griffith.edu.au/Program/1187/Courses/International',
'https://degrees.griffith.edu.au/Program/1187/Courses/International',
'https://degrees.griffith.edu.au/Program/1187/Courses/International',
'https://degrees.griffith.edu.au/Program/1189/Courses/International',
'https://degrees.griffith.edu.au/Program/1189/Courses/International',
'https://degrees.griffith.edu.au/Program/1189/Courses/International',
'https://degrees.griffith.edu.au/Program/1189/Courses/International',
'https://degrees.griffith.edu.au/Program/1189/Courses/International',
'https://degrees.griffith.edu.au/Program/1189/Courses/International',
'https://degrees.griffith.edu.au/Program/1189/Courses/International',
'https://degrees.griffith.edu.au/Program/1189/Courses/International',
'https://degrees.griffith.edu.au/Program/1210/Courses/International',
'https://degrees.griffith.edu.au/Program/1210/Courses/International',
'https://degrees.griffith.edu.au/Program/1210/Courses/International',
'https://degrees.griffith.edu.au/Program/1210/Courses/International',
'https://degrees.griffith.edu.au/Program/1210/Courses/International',
'https://degrees.griffith.edu.au/Program/1210/Courses/International',
'https://degrees.griffith.edu.au/Program/1210/Courses/International',
'https://degrees.griffith.edu.au/Program/1210/Courses/International',
'https://degrees.griffith.edu.au/Program/1210/Courses/International',
'https://degrees.griffith.edu.au/Program/1264/Courses/International',
'https://degrees.griffith.edu.au/Program/1264/Courses/International',
'https://degrees.griffith.edu.au/Program/1280/Courses/International',
'https://degrees.griffith.edu.au/Program/1282/Courses/International',
'https://degrees.griffith.edu.au/Program/1284/Courses/International',
'https://degrees.griffith.edu.au/Program/1286/Courses/International',
'https://degrees.griffith.edu.au/Program/1286/Courses/International',
'https://degrees.griffith.edu.au/Program/1286/Courses/International',
'https://degrees.griffith.edu.au/Program/1286/Courses/International',
'https://degrees.griffith.edu.au/Program/1286/Courses/International',
'https://degrees.griffith.edu.au/Program/1286/Courses/International',
'https://degrees.griffith.edu.au/Program/1286/Courses/International',
'https://degrees.griffith.edu.au/Program/1286/Courses/International',
'https://degrees.griffith.edu.au/Program/1286/Courses/International',
'https://degrees.griffith.edu.au/Program/1286/Courses/International',
'https://degrees.griffith.edu.au/Program/1286/Courses/International',
'https://degrees.griffith.edu.au/Program/1286/Courses/International',
'https://degrees.griffith.edu.au/Program/1286/Courses/International',
'https://degrees.griffith.edu.au/Program/1286/Courses/International',
'https://degrees.griffith.edu.au/Program/1288/Courses/International',
'https://degrees.griffith.edu.au/Program/1288/Courses/International',
'https://degrees.griffith.edu.au/Program/1288/Courses/International',
'https://degrees.griffith.edu.au/Program/1288/Courses/International',
'https://degrees.griffith.edu.au/Program/1288/Courses/International',
'https://degrees.griffith.edu.au/Program/1288/Courses/International',
'https://degrees.griffith.edu.au/Program/1306/Courses/International',
'https://degrees.griffith.edu.au/Program/1312/Courses/International',
'https://degrees.griffith.edu.au/Program/1328/Courses/International',
'https://degrees.griffith.edu.au/Program/1330/Courses/International',
'https://degrees.griffith.edu.au/Program/1330/Courses/International',
'https://degrees.griffith.edu.au/Program/1337/Courses/International',
'https://degrees.griffith.edu.au/Program/1337/Courses/International',
'https://degrees.griffith.edu.au/Program/1338/Courses/International',
'https://degrees.griffith.edu.au/Program/1354/Courses/International',
'https://degrees.griffith.edu.au/Program/1354/Courses/International',
'https://degrees.griffith.edu.au/Program/1355/Courses/International',
'https://degrees.griffith.edu.au/Program/1358/Courses/International',
'https://degrees.griffith.edu.au/Program/1370/Courses/International',
'https://degrees.griffith.edu.au/Program/1388/Courses/International',
'https://degrees.griffith.edu.au/Program/1388/Courses/International',
'https://degrees.griffith.edu.au/Program/1388/Courses/International',
'https://degrees.griffith.edu.au/Program/1388/Courses/International',
'https://degrees.griffith.edu.au/Program/1388/Courses/International',
'https://degrees.griffith.edu.au/Program/1388/Courses/International',
'https://degrees.griffith.edu.au/Program/1388/Courses/International',
'https://degrees.griffith.edu.au/Program/1388/Courses/International',
'https://degrees.griffith.edu.au/Program/1395/Courses/International',
'https://degrees.griffith.edu.au/Program/1399/Courses/International',
'https://degrees.griffith.edu.au/Program/1399/Courses/International',
'https://degrees.griffith.edu.au/Program/1399/Courses/International',
'https://degrees.griffith.edu.au/Program/1399/Courses/International',
'https://degrees.griffith.edu.au/Program/1400/Courses/International',
'https://degrees.griffith.edu.au/Program/1404/Courses/International',
'https://degrees.griffith.edu.au/Program/1405/Courses/International',
'https://degrees.griffith.edu.au/Program/1407/Courses/International',
'https://degrees.griffith.edu.au/Program/1408/Courses/International',
'https://degrees.griffith.edu.au/Program/1408/Courses/International',
'https://degrees.griffith.edu.au/Program/1409/Courses/International',
'https://degrees.griffith.edu.au/Program/1409/Courses/International',
'https://degrees.griffith.edu.au/Program/1409/Courses/International',
'https://degrees.griffith.edu.au/Program/1409/Courses/International',
'https://degrees.griffith.edu.au/Program/1409/Courses/International',
'https://degrees.griffith.edu.au/Program/1409/Courses/International',
'https://degrees.griffith.edu.au/Program/1410/Courses/International',
'https://degrees.griffith.edu.au/Program/1413/Courses/International',
'https://degrees.griffith.edu.au/Program/1414/Courses/International',
'https://degrees.griffith.edu.au/Program/1417/Courses/International',
'https://degrees.griffith.edu.au/Program/1419/Courses/International',
'https://degrees.griffith.edu.au/Program/1432/Courses/International',
'https://degrees.griffith.edu.au/Program/1436/Courses/International',
'https://degrees.griffith.edu.au/Program/1440/Courses/International',
'https://degrees.griffith.edu.au/Program/1454/Courses/International',
'https://degrees.griffith.edu.au/Program/1455/Courses/International',
'https://degrees.griffith.edu.au/Program/1483/Courses/International',
'https://degrees.griffith.edu.au/Program/1484/Courses/International',
'https://degrees.griffith.edu.au/Program/1492/Courses/International',
'https://degrees.griffith.edu.au/Program/1493/Courses/International',
'https://degrees.griffith.edu.au/Program/1500/Courses/International',
'https://degrees.griffith.edu.au/Program/1517/Courses/International',
'https://degrees.griffith.edu.au/Program/1525/Courses/International',
'https://degrees.griffith.edu.au/Program/1526/Courses/International',
'https://degrees.griffith.edu.au/Program/1527/Courses/International',
'https://degrees.griffith.edu.au/Program/1528/Courses/International',
'https://degrees.griffith.edu.au/Program/1528/Courses/International',
'https://degrees.griffith.edu.au/Program/1533/Courses/International',
'https://degrees.griffith.edu.au/Program/1534/Courses/International',
'https://degrees.griffith.edu.au/Program/1538/Courses/International',
'https://degrees.griffith.edu.au/Program/1539/Courses/International',
'https://degrees.griffith.edu.au/Program/1540/Courses/International',
'https://degrees.griffith.edu.au/Program/1541/Courses/International',
'https://degrees.griffith.edu.au/Program/1541/Courses/International',
'https://degrees.griffith.edu.au/Program/1541/Courses/International',
'https://degrees.griffith.edu.au/Program/1541/Courses/International',
'https://degrees.griffith.edu.au/Program/1541/Courses/International',
'https://degrees.griffith.edu.au/Program/1541/Courses/International',
'https://degrees.griffith.edu.au/Program/1542/Courses/International',
'https://degrees.griffith.edu.au/Program/1542/Courses/International',
'https://degrees.griffith.edu.au/Program/1542/Courses/International',
'https://degrees.griffith.edu.au/Program/1542/Courses/International',
'https://degrees.griffith.edu.au/Program/1542/Courses/International',
'https://degrees.griffith.edu.au/Program/1542/Courses/International',
'https://degrees.griffith.edu.au/Program/1543/Courses/International',
'https://degrees.griffith.edu.au/Program/1546/Courses/International',
'https://degrees.griffith.edu.au/Program/1546/Courses/International',
'https://degrees.griffith.edu.au/Program/1546/Courses/International',
'https://degrees.griffith.edu.au/Program/1546/Courses/International',
'https://degrees.griffith.edu.au/Program/1547/Courses/International',
'https://degrees.griffith.edu.au/Program/1548/Courses/International',
'https://degrees.griffith.edu.au/Program/1548/Courses/International',
'https://degrees.griffith.edu.au/Program/1567/Courses/International',
'https://degrees.griffith.edu.au/Program/1567/Courses/International',
'https://degrees.griffith.edu.au/Program/1567/Courses/International',
'https://degrees.griffith.edu.au/Program/1567/Courses/International',
'https://degrees.griffith.edu.au/Program/1567/Courses/International',
'https://degrees.griffith.edu.au/Program/1567/Courses/International',
'https://degrees.griffith.edu.au/Program/1567/Courses/International',
'https://degrees.griffith.edu.au/Program/1567/Courses/International',
'https://degrees.griffith.edu.au/Program/1567/Courses/International',
'https://degrees.griffith.edu.au/Program/1567/Courses/International',
'https://degrees.griffith.edu.au/Program/1567/Courses/International',
'https://degrees.griffith.edu.au/Program/1567/Courses/International',
'https://degrees.griffith.edu.au/Program/1567/Courses/International',
'https://degrees.griffith.edu.au/Program/1567/Courses/International',
'https://degrees.griffith.edu.au/Program/1567/Courses/International',
'https://degrees.griffith.edu.au/Program/1574/Courses/International',
'https://degrees.griffith.edu.au/Program/1575/Courses/International',
'https://degrees.griffith.edu.au/Program/1576/Courses/International',
'https://degrees.griffith.edu.au/Program/1576/Courses/International',
'https://degrees.griffith.edu.au/Program/1576/Courses/International',
'https://degrees.griffith.edu.au/Program/1576/Courses/International',
'https://degrees.griffith.edu.au/Program/1576/Courses/International',
'https://degrees.griffith.edu.au/Program/1576/Courses/International',
'https://degrees.griffith.edu.au/Program/1576/Courses/International',
'https://degrees.griffith.edu.au/Program/1576/Courses/International',
'https://degrees.griffith.edu.au/Program/1576/Courses/International',
'https://degrees.griffith.edu.au/Program/1576/Courses/International',
'https://degrees.griffith.edu.au/Program/1576/Courses/International',
'https://degrees.griffith.edu.au/Program/1577/Courses/International',
'https://degrees.griffith.edu.au/Program/1578/Courses/International',
'https://degrees.griffith.edu.au/Program/1579/Courses/International',
'https://degrees.griffith.edu.au/Program/1581/Courses/International',
'https://degrees.griffith.edu.au/Program/1586/Courses/International',
'https://degrees.griffith.edu.au/Program/1587/Courses/International',
'https://degrees.griffith.edu.au/Program/1588/Courses/International',
'https://degrees.griffith.edu.au/Program/1589/Courses/International',
'https://degrees.griffith.edu.au/Program/1590/Courses/International',
'https://degrees.griffith.edu.au/Program/1596/Courses/International',
'https://degrees.griffith.edu.au/Program/1596/Courses/International',
'https://degrees.griffith.edu.au/Program/1597/Courses/International',
'https://degrees.griffith.edu.au/Program/1597/Courses/International',
'https://degrees.griffith.edu.au/Program/1598/Courses/International',
'https://degrees.griffith.edu.au/Program/1604/Courses/International',
'https://degrees.griffith.edu.au/Program/1609/Courses/International',
'https://degrees.griffith.edu.au/Program/1609/Courses/International',
'https://degrees.griffith.edu.au/Program/1609/Courses/International',
'https://degrees.griffith.edu.au/Program/1609/Courses/International',]
    start_urls=set(start_urls)
    # def parse(self, response):
    #     item=get_item(AustraliaItem)
    #     item['url']=response.url.replace('Courses','Overview')
    #     item['university'] = 'Griffith University'
    #     modules=response.xpath('//div[@id="course-list-content"]').extract()
    #     # print(modules)
    #     item['modules_en']=remove_class(modules)
    #     yield item
    def parse(self, response):
        item=get_item(AustraliaItem)
        item['university']='Griffith University'
        item['url']=response.url
        programme=response.xpath('//div[@class="col-xs-12"]/h1/text()').extract()
        item['programme_en']=''.join(programme).replace('Bachelor of','').strip()
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
        # how_to_apply_ulr=response.url.replace('Overview','HowToApply')
        # htps=self.how_to_apply(how_to_apply_ulr)
        # htp = htps.xpath('//div[@id="process"]//text()')
        # htp=clear_long_text(htp)
        # item['apply_proces_en']=htp
        # ielts=get_ielts(htps.xpath('//*[contains(text(),"IELTS")]/../text()'))
        # item['ielts_desc']=remove_class(htps.xpath('//*[contains(text(),"IELTS")]/../text()'))
        # if ielts!=[]:
        #     item['ielts']=ielts['IELTS']
        #     item['ielts_l']=ielts['IELTS_L']
        #     item['ielts_s'] = ielts['IELTS_S']
        #     item['ielts_r'] = ielts['IELTS_R']
        #     item['ielts_w'] = ielts['IELTS_W']
        # toefl=re.findall('[1]?[217890]\d',''.join(htps.xpath('//*[contains(text(),"iBT")]//text()')))
        # item['toefl_desc']=remove_class(htps.xpath('//*[contains(text(),"iBT")]//text()'))
        # if len(toefl)==2:
        #     toefl=list(map(int,toefl))
        #     item['toefl']=max(toefl)
        #     item['toefl_l']=min(toefl)
        #     item['toefl_s'] = min(toefl)
        #     item['toefl_r'] = min(toefl)
        #     item['toefl_w'] = min(toefl)
        # modules_url=response.url.replace('Overview','Courses')
        # modu=self.how_to_apply(modules_url)
        # degree_requ=modu.xpath('//div[@id="degree-requirements"]//text()')
        # degree_requ=clear_long_text(degree_requ)
        # item['degree_requirements']=degree_requ
        # modules=modu.xpath('//div[@id="course-list-content"]//td[@class="name"]/text()')
        # modules=clear_long_text(modules)
        # item['modules_en']=modules
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




