# -*- coding: utf-8 -*-
import scrapy
from Australia.middlewares import *
from Australia.items import AustraliaItem
import requests
from lxml import etree
class GriffithuniversityUSpider(scrapy.Spider):
    name = 'GriffithUniversity_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://degrees.griffith.edu.au/Program/1575/Overview/International',
'https://degrees.griffith.edu.au/Program/1179/Overview/International',
'https://degrees.griffith.edu.au/Program/2035/Overview/International',
'https://degrees.griffith.edu.au/Program/1492/Overview/International',
'https://degrees.griffith.edu.au/Program/1016/Overview/International',
'https://degrees.griffith.edu.au/Program/1021/Overview/International',
'https://degrees.griffith.edu.au/Program/2005/Overview/International',
'https://degrees.griffith.edu.au/Program/2007/Overview/International',
'https://degrees.griffith.edu.au/Program/1388/Overview/International',
'https://degrees.griffith.edu.au/Program/1517/Overview/International',
'https://degrees.griffith.edu.au/Program/1367/Overview/International',
'https://degrees.griffith.edu.au/Program/1094/Overview/International',
'https://degrees.griffith.edu.au/Program/1031/Overview/International',
'https://degrees.griffith.edu.au/Program/2100/Overview/International',
'https://degrees.griffith.edu.au/Program/1358/Overview/International',
'https://degrees.griffith.edu.au/Program/2087/Overview/International',
'https://degrees.griffith.edu.au/Program/2108/Overview/International',
'https://degrees.griffith.edu.au/Program/1540/Overview/International',
'https://degrees.griffith.edu.au/Program/1034/Overview/International',
'https://degrees.griffith.edu.au/Program/1347/Overview/International',
'https://degrees.griffith.edu.au/Program/1288/Overview/International',
'https://degrees.griffith.edu.au/Program/2088/Overview/International',
'https://degrees.griffith.edu.au/Program/1095/Overview/International',
'https://degrees.griffith.edu.au/Program/2093/Overview/International',
'https://degrees.griffith.edu.au/Program/1604/Overview/International',
'https://degrees.griffith.edu.au/Program/1286/Overview/International',
'https://degrees.griffith.edu.au/Program/1337/Overview/International',
'https://degrees.griffith.edu.au/Program/1035/Overview/International',
'https://degrees.griffith.edu.au/Program/2089/Overview/International',
'https://degrees.griffith.edu.au/Program/2105/Overview/International',
'https://degrees.griffith.edu.au/Program/1597/Overview/International',
'https://degrees.griffith.edu.au/Program/1534/Overview/International',
'https://degrees.griffith.edu.au/Program/2123/Overview/International',
'https://degrees.griffith.edu.au/Program/1598/Overview/International',
'https://degrees.griffith.edu.au/Program/1548/Overview/International',
'https://degrees.griffith.edu.au/Program/1609/Overview/International',
'https://degrees.griffith.edu.au/Program/1541/Overview/International',
'https://degrees.griffith.edu.au/Program/1385/Overview/International',
'https://degrees.griffith.edu.au/Program/1112/Overview/International',
'https://degrees.griffith.edu.au/Program/2117/Overview/International',
'https://degrees.griffith.edu.au/Program/2022/Overview/International',
'https://degrees.griffith.edu.au/Program/1577/Overview/International',
'https://degrees.griffith.edu.au/Program/1581/Overview/International',
'https://degrees.griffith.edu.au/Program/1574/Overview/International',
'https://degrees.griffith.edu.au/Program/1189/Overview/International',
'https://degrees.griffith.edu.au/Program/2043/Overview/International',
'https://degrees.griffith.edu.au/Program/2081/Overview/International',
'https://degrees.griffith.edu.au/Program/1567/Overview/International',
'https://degrees.griffith.edu.au/Program/1546/Overview/International',
'https://degrees.griffith.edu.au/Program/1542/Overview/International',
'https://degrees.griffith.edu.au/Program/1586/Overview/International',
'https://degrees.griffith.edu.au/Program/1543/Overview/International',
'https://degrees.griffith.edu.au/Program/1547/Overview/International',
'https://degrees.griffith.edu.au/Program/1171/Overview/International',
'https://degrees.griffith.edu.au/Program/2096/Overview/International',
'https://degrees.griffith.edu.au/Program/1284/Overview/International',
'https://degrees.griffith.edu.au/Program/2074/Overview/International',
'https://degrees.griffith.edu.au/Program/1181/Overview/International',
'https://degrees.griffith.edu.au/Program/2037/Overview/International',
'https://degrees.griffith.edu.au/Program/1264/Overview/International',
'https://degrees.griffith.edu.au/Program/2107/Overview/International',
'https://degrees.griffith.edu.au/Program/1338/Overview/International',
'https://degrees.griffith.edu.au/Program/2083/Overview/International',
'https://degrees.griffith.edu.au/Program/1399/Overview/International',
'https://degrees.griffith.edu.au/Program/2090/Overview/International',
'https://degrees.griffith.edu.au/Program/2121/Overview/International',
'https://degrees.griffith.edu.au/Program/1093/Overview/International',
'https://degrees.griffith.edu.au/Program/2101/Overview/International',
'https://degrees.griffith.edu.au/Program/1394/Overview/International',
'https://degrees.griffith.edu.au/Program/1098/Overview/International',
'https://degrees.griffith.edu.au/Program/2092/Overview/International',
'https://degrees.griffith.edu.au/Program/1407/Overview/International',
'https://degrees.griffith.edu.au/Program/1539/Overview/International',
'https://degrees.griffith.edu.au/Program/1538/Overview/International',
'https://degrees.griffith.edu.au/Program/2020/Overview/International',
'https://degrees.griffith.edu.au/Program/2011/Overview/International',
'https://degrees.griffith.edu.au/Program/1596/Overview/International',
'https://degrees.griffith.edu.au/Program/1107/Overview/International',
'https://degrees.griffith.edu.au/Program/1105/Overview/International',
'https://degrees.griffith.edu.au/Program/1408/Overview/International',
'https://degrees.griffith.edu.au/Program/1409/Overview/International',
'https://degrees.griffith.edu.au/Program/2104/Overview/International',
'https://degrees.griffith.edu.au/Program/1398/Overview/International',
'https://degrees.griffith.edu.au/Program/1116/Overview/International',
'https://degrees.griffith.edu.au/Program/2023/Overview/International',
'https://degrees.griffith.edu.au/Program/1484/Overview/International',
'https://degrees.griffith.edu.au/Program/1455/Overview/International',
'https://degrees.griffith.edu.au/Program/1483/Overview/International',
'https://degrees.griffith.edu.au/Program/1454/Overview/International',
'https://degrees.griffith.edu.au/Program/1527/Overview/International',
'https://degrees.griffith.edu.au/Program/1500/Overview/International',
'https://degrees.griffith.edu.au/Program/1526/Overview/International',
'https://degrees.griffith.edu.au/Program/1525/Overview/International',
'https://degrees.griffith.edu.au/Program/1328/Overview/International',
'https://degrees.griffith.edu.au/Program/1370/Overview/International',
'https://degrees.griffith.edu.au/Program/2116/Overview/International',
'https://degrees.griffith.edu.au/Program/1280/Overview/International',
'https://degrees.griffith.edu.au/Program/1306/Overview/International',
'https://degrees.griffith.edu.au/Program/2099/Overview/International',
'https://degrees.griffith.edu.au/Program/2095/Overview/International',
'https://degrees.griffith.edu.au/Program/2021/Overview/International',
'https://degrees.griffith.edu.au/Program/2013/Overview/International',
'https://degrees.griffith.edu.au/Program/1419/Overview/International',
'https://degrees.griffith.edu.au/Program/2051/Overview/International',
'https://degrees.griffith.edu.au/Program/1414/Overview/International',
'https://degrees.griffith.edu.au/Program/1413/Overview/International',
'https://degrees.griffith.edu.au/Program/1404/Overview/International',
'https://degrees.griffith.edu.au/Program/1162/Overview/International',
'https://degrees.griffith.edu.au/Program/1165/Overview/International',
'https://degrees.griffith.edu.au/Program/1161/Overview/International',
'https://degrees.griffith.edu.au/Program/2094/Overview/International',
'https://degrees.griffith.edu.au/Program/1355/Overview/International',
'https://degrees.griffith.edu.au/Program/1436/Overview/International',
'https://degrees.griffith.edu.au/Program/1400/Overview/International',
'https://degrees.griffith.edu.au/Program/1587/Overview/International',
'https://degrees.griffith.edu.au/Program/1405/Overview/International',
'https://degrees.griffith.edu.au/Program/1588/Overview/International',
'https://degrees.griffith.edu.au/Program/2097/Overview/International',
'https://degrees.griffith.edu.au/Program/2098/Overview/International',
'https://degrees.griffith.edu.au/Program/1533/Overview/International',
'https://degrees.griffith.edu.au/Program/2122/Overview/International',
'https://degrees.griffith.edu.au/Program/1528/Overview/International',
'https://degrees.griffith.edu.au/Program/2118/Overview/International',
'https://degrees.griffith.edu.au/Program/1395/Overview/International',
'https://degrees.griffith.edu.au/Program/2119/Overview/International',
'https://degrees.griffith.edu.au/Program/1186/Overview/International',
'https://degrees.griffith.edu.au/Program/2041/Overview/International',
'https://degrees.griffith.edu.au/Program/1589/Overview/International',
'https://degrees.griffith.edu.au/Program/1579/Overview/International',
'https://degrees.griffith.edu.au/Program/1590/Overview/International',
'https://degrees.griffith.edu.au/Program/1578/Overview/International',
'https://degrees.griffith.edu.au/Program/2062/Overview/International',
'https://degrees.griffith.edu.au/Program/1012/Overview/International',
'https://degrees.griffith.edu.au/Program/1312/Overview/International',
'https://degrees.griffith.edu.au/Program/2004/Overview/International',
'https://degrees.griffith.edu.au/Program/2033/Overview/International',
'https://degrees.griffith.edu.au/Program/1014/Overview/International',
'https://degrees.griffith.edu.au/Program/1178/Overview/International',
'https://degrees.griffith.edu.au/Program/1440/Overview/International',
'https://degrees.griffith.edu.au/Program/1018/Overview/International',
'https://degrees.griffith.edu.au/Program/1210/Overview/International',
'https://degrees.griffith.edu.au/Program/2111/Overview/International',
'https://degrees.griffith.edu.au/Program/2112/Overview/International',
'https://degrees.griffith.edu.au/Program/2110/Overview/International',
'https://degrees.griffith.edu.au/Program/1330/Overview/International',
'https://degrees.griffith.edu.au/Program/1576/Overview/International',
'https://degrees.griffith.edu.au/Program/1372/Overview/International',
'https://degrees.griffith.edu.au/Program/1282/Overview/International',
'https://degrees.griffith.edu.au/Program/1416/Overview/International',
'https://degrees.griffith.edu.au/Program/1417/Overview/International',
'https://degrees.griffith.edu.au/Program/1493/Overview/International',
'https://degrees.griffith.edu.au/Program/2120/Overview/International',
'https://degrees.griffith.edu.au/Program/1279/Overview/International',
'https://degrees.griffith.edu.au/Program/1086/Overview/International',
'https://degrees.griffith.edu.au/Program/1432/Overview/International',
'https://degrees.griffith.edu.au/Program/1431/Overview/International',]
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
