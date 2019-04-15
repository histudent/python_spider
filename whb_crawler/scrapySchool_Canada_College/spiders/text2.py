import scrapy
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from scrapySchool_Canada_College import getItem
from w3lib.html import remove_tags
import requests
import re
import time

class BaiduSpider(scrapy.Spider):
    name = 'text2'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    D = ['http://detail.zol.com.cn/cell_phone_index/subcate57_1795_list_1.html',]


    for i in D:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        item = getItem.get_item(ScrapyschoolCanadaCollegeItem)

        abc = response.xpath("//li/h3/a/@href").extract()
        print(abc)
        item['school_name'] = None
        #item['location'] = location
       # item['campus'] = campus
        item['department'] = None
        item['degree_name'] = None
        item['degree_name_desc'] = None
        item['major_name_en'] = None
       # item['programme_code'] = programme_code
        item['overview_en'] = None
        item['start_date'] = None
        item['duration'] = None
        item['duration_per'] = '1'
        item['modules_en'] = None
        item['career_en'] = None
        item['deadline'] = None
        item['apply_pre'] = 'CAD$'
        item['apply_fee'] = None
        item['tuition_fee_pre'] = 'CAD$'
        item['tuition_fee'] = None
        item['tuition_fee_per'] = '1'
        item['entry_requirements_en'] = None
        item['require_chinese_en'] = None
        item['specific_requirement_en'] = None
        item['average_score'] = None
        item['gaokao_desc'] = None
        item['gaokao_zs'] = None
        item['huikao_desc'] = None
        item['huikao_zs'] = None
        item['ielts_desc'] = None
        item['ielts'] = None
        item['ielts_l'] = None
        item['ielts_s'] = None
        item['ielts_r'] = None
        item['ielts_w'] = None
        item['toefl_code'] = None
        item['toefl_desc'] = None
        item['toefl'] = None
        item['toefl_l'] = None
        item['toefl_s'] = None
        item['toefl_r'] = None
        item['toefl_w'] = None
        item['interview_desc_en'] = None
        item['portfolio_desc_en'] = None
        item['other'] = None
        item['url'] = response.url
        item['degree_level'] = None


        #yield item