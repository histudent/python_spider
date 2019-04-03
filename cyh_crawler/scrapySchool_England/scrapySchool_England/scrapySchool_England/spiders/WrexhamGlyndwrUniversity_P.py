# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.middlewares import clear_duration,tracslateDate
from scrapySchool_England.clearSpace import clear_lianxu_space,clear_same_s
class WrexhamglyndwruniversityPSpider(scrapy.Spider):
    name = 'WrexhamGlyndwrUniversity_P'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.glyndwr.ac.uk/en/A-Z/PostgraduateA-Z/']
    def parse(self, response):
        pro_url = response.xpath('//ul[@id="undergraduatecourses"]/li/a[@class="list-link"]/@href').extract()
        pro_name = response.xpath(
            '//ul[@id="undergraduatecourses"]/li/a[@class="list-link"]//p[@class="course-name"]/text()').extract()
        for url, name in zip(pro_url, pro_name):
            url = 'https://www.glyndwr.ac.uk' + url
            yield scrapy.Request(url, meta={'programme': name}, callback=self.parses)
    def parses(self,response):
        item=get_item1(ScrapyschoolEnglandItem1)
        item['url'] = response.url
        item['university'] = 'Wrexham Glyndwr University'
        item['major_type1'] = response.meta['programme']
        item['teach_time']='fulltime'
        item['teach_type']='taught'
        # 第一种在详情页获取专业名的方式
        prog = response.xpath('//div[@class="breadcrumb-links"]/a/text()').extract()
        # print(prog[-1])
        # 第二种获取专业名的方式
        pro = response.xpath('//h1/span[@class="course-name"]/text()').extract()
        programme = ' '.join(pro).strip()
        # print(programme)
        item['programme_en'] = programme
        degree = response.xpath('//h1/span[@class="header-bg-color"]/text()').extract()
        degree = ''.join(degree)
        # print(degree)
        item['degree_name'] = degree
        duration = response.xpath('//div[contains(text(),"DURATION")]/following-sibling::div/text()').extract()
        duration = ''.join(duration)
        mode = re.findall('(?i)ft', duration)
        # if mode==[]:
        #     print(duration)
        if mode != []:
            print(duration)
        dura = re.findall('\d', duration)
        try:
            dura = list(map(int, dura))
            item['duration'] = min(dura)
            item['duration_per'] = '1'
        except:
            pass
        location = response.xpath('//div[contains(text(),"LOCATION")]/following-sibling::div/text()').extract()
        location = ''.join(location).strip()
        item['location'] = location
        item['tuition_fee'] = '12500'
        htp = ['<h2>Applying through<span>&nbsp;UCAS<br /></span></h2>',
               "<p>For the majority of undergraduate courses, you'll need to apply through UCAS.&nbsp; If you are interested in studying a part-time or postgraduate course at Wrexham Glyndwr, then please see our&nbsp;<a>alternative application routes.</a></p>",
               '<p>Once you&rsquo;ve decided on which courses you wish to apply for then you&rsquo;ll need to register at&nbsp;<a>.</span></p>',
               '<p>If you are currently at school or college, you may be given a &lsquo;buzzword&rsquo; to use when you register &ndash; this will help distinguish where you are applying from. Those who wish to apply independently will not need a buzzword, but will still use the UCAS system to apply.</p>',
               '</section><section>',
               '<h2><strong><span>Completing</span> your application</strong></h2>',
               '<p>The online application system &nbsp;opens in September for entry to the University in the following year.&nbsp; You do not have to complete your application all in one go &ndash; the system will allow you to complete it in stages.</p>',
               '<p>Your application will need to include the following information:</p>',
               '<p><strong>Your personal details</strong> &ndash; remember your name needs to be stated as shown on your official documents, such as your birth certificate or passport.</p>',
               '<p><strong>Your qualifications</strong> &ndash; be sure to enter all of your qualifications and any pending qualifications that you are awaiting results for. If you encounter any problems, get in touch with UCAS or our admissions team.</p>',
               '<p><strong>A personal statement</strong> &ndash; this is one of the most important parts of your application as a well-written and thoughtful personal statement can really make you stand out from the crowd. A poor one could undermine an otherwise good application.</p>',
               '<p>There is no definitive way of writing a personal statement which will guarantee acceptance onto your chosen course, however there are guidelines that will help you to focus on what you should and shouldn&rsquo;t include. <a>Why not read our Top 10 Tips on Writing your Personal Statement before you get started?</a></p>',
               '<p><strong>A reference</strong> &ndash; ideally this should be from a teacher or a professional who knows you well and can verify your suitability for higher education.</p>',
               '<p><strong>You will be required to disclose if you have a &lsquo;relevant&rsquo; criminal conviction</strong> &ndash; some specific courses may require you to undergo a DBS check &ndash; where this is the case you must select &ldquo;Yes&rdquo; if you have ever had a conviction, even if this is spent.</p>',
               '<p><a>Find out more about obtaining a DBS check for study.</a></p>',
               '<h2>Clearing</h2>',
               '<p>If you apply through UCAS after 30th June 2018, your application will not be sent to us. Instead you will receive details about Clearing.</p>',
               '<p>Clearing is a process that is available between July and September for those who are applying late, have already applied and haven&rsquo;t received a place, or have declined all of their offers.</p>',
               '<p>If you wish to secure a place at Wrexham Glyndŵr University, then we strongly advise that from the beginning of July to mid-September you call our dedicated Clearing Hotline on 01978 293439 &ndash; our friendly team will be able to help you with course vacancies and put you in touch with the relevant admissions staff.</p>',
               '</section></div>',
               ]
        item['apply_proces_en'] = remove_class(htp)
        overview = response.xpath('//div[@id="introduction-text"]').extract()
        item['overview_en'] = remove_class(overview)
        modules = response.xpath('//a[contains(text(),"YOU STUDY")]/../following-sibling::dd[1]').extract()
        # print(modules)
        item['modules_en'] = remove_class(modules)
        item['ielts_desc'] = 'Postgraduate study 6.5 (no band lower than 6.0)'
        item['ielts'] = '6.5'
        item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w'] = '6.0', '6.0', '6.0', '6.0'
        chi = ['<p><strong>硕士学习（授课型）</strong></p>',
'<p>▪ 学士学位证书&nbsp;</p>',
'<p>对于有相关工作经验的大专毕业生，也可以直接攻读研究生。</p>',]
        item['require_chinese_en'] = remove_class(chi)
        career = response.xpath('//a[contains(text(),"CAREER")]/../following-sibling::dd[1]').extract()
        item['career_en'] = remove_class(career)
        assessment = response.xpath('//a[contains(text(),"ASS")]/../following-sibling::dd[1]').extract()
        item['assessment_en'] = remove_class(assessment)
        rntry_requirements=response.xpath('//a[contains(text(),"ENTRY")]/../following-sibling::dd[1]').extract()
        item['rntry_requirements']=rntry_requirements
        if mode != []:
            yield item
            # print(item)
            # print(duration)
        else:
            print('兼职专业，跳过')
