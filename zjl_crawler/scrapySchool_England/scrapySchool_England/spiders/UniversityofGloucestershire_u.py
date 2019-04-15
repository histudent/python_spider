# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/7 15:43'
import scrapy,json
import re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from w3lib.html import remove_tags
from scrapySchool_England.clearSpace import  clear_space_str
from scrapySchool_England.translate_date import  tracslateDate
from scrapySchool_England.TranslateMonth import translate_month
import  urllib.request
from lxml import  etree
import  requests
class UniversityofGloucestershireSpider(scrapy.Spider):
    name = 'UniversityofGloucestershire_u'
    allowed_domains = ['glos.ac.uk/']
    start_urls = []
    C= [
        'http://www.glos.ac.uk/courses/undergraduate/ibn/pages/international-business-studies-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/ecs/pages/early-childhood-studies-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/pas/pages/paramedic-science.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/spt/pages/sports-therapy-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/fpr/pages/film-production-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/tvp/pages/television-production-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/spj/pages/sports-journalism-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/anm/pages/animation-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/anb/pages/animal-biology-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/anb/pages/animal-biology-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/bmm/pages/business-and-marketing-management-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/bmm/pages/business-and-marketing-management-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/bio/pages/biology-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/bio/pages/biology-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/bmn/pages/business-management-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/bmn/pages/business-management-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/bmn/pages/business-management-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/bmn/pages/business-management-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/cri/pages/criminology-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/cps/pages/criminology-and-psychology-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/dan/pages/dance-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/dgm/pages/digital-marketing-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/dgm/pages/digital-marketing-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/ees/pages/ecology-and-environmental-science-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/ees/pages/ecology-and-environmental-science-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/gea/pages/geography-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/gea/pages/geography-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/geo/pages/geography-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/geo/pages/geography-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/ibg/pages/international-business-management-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/ibg/pages/international-business-management-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/jou/pages/journalism-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/law/pages/law-bachelor-of-law.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/law/pages/law-bachelor-of-law.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/law/pages/law-bachelor-of-law.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/mjp/pages/magazine-journalism-and-production-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/mab/pages/marketing-advertising-and-branding-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/mab/pages/marketing-advertising-and-branding-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/mub/pages/music-business-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/mub/pages/music-business-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/mep/pages/media-production-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/pfa/pages/performing-arts-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/edpk1/pages/primary-general-fsks1-ages-3-7-bed-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/edpk2/pages/primary-general-ks1ks2-ages-5-11-bed-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/psy/pages/psychology-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/spx/pages/sport-and-exercise-sciences-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/edpms/pages/primary-general-maths-ks1ks2-ages-5-11-bed-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/num/pages/nursing-mental-health-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/nur/pages/nursing-adult-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/sdc/pages/sports-development-and-coaching-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/spc/pages/sports-coaching-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/adv/pages/advertising-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/abm/pages/accounting-and-business-management-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/abm/pages/accounting-and-business-management-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/afi/pages/accounting-and-finance-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/afi/pages/accounting-and-finance-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/fmn/pages/accounting-and-financial-management-studies-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/buc/pages/business-computing-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/buc/pages/business-computing-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/ccf/pages/computer-and-cyber-forensics-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/ccf/pages/computer-and-cyber-forensics-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/cgp/pages/computer-games-programming-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/cgp/pages/computer-games-programming-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/crt/pages/creative-music-technology-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/cop/pages/computing-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/cop/pages/computing-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/crw/pages/creative-writing-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/cgs/pages/computer-games-design-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/cgs/pages/computer-games-design-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/crs/pages/criminology-and-sociology-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/dpp/pages/drama-and-performance-practice-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/dsc/pages/cyber-and-computer-security-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/dsc/pages/cyber-and-computer-security-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/dmw/pages/digital-media-and-web-technologies-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/dmw/pages/digital-media-and-web-technologies-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/edc/pages/education-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/elc/pages/english-literature-and-creative-writing-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/enl/pages/english-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/evm/pages/events-management-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/evm/pages/events-management-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/fad/pages/fashion-design-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/elw/pages/english-language-and-creative-writing-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/art/pages/fine-art-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/grd/pages/graphic-design-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/his/pages/history-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/hrt/pages/hotel-resort-and-tourism-management-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/ind/pages/interior-design-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/hre/pages/hotel-resort-and-events-management-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/ill/pages/illustration-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/isb/pages/international-sports-business-and-coaching.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/laa/pages/landscape-architecture-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/pvp/pages/photography-editorial-and-advertising-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/pjd/pages/photojournalism-and-documentary-photography-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/ped/pages/physical-education-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/phy/pages/photography-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/pec/pages/physical-education-and-coaching-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/pom/pages/popular-music-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/prd/pages/product-design-ba-bsc.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/prd/pages/product-design-ba-bsc.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/prd/pages/product-design-ba-bsc.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/prd/pages/product-design-ba-bsc.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/rpe/pages/religion-philosophy-and-ethics-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/soc/pages/sociology-ba-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/spr/pages/sports-strength-and-conditioning-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/swu/pages/social-work-bsc-hons.aspx',
        'http://www.glos.ac.uk/courses/undergraduate/pol/pages/policing-bsc-hons.aspx'
    ]
    C = set(C)

    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Gloucestershire'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en #4.degree_name #5.degree_type
        programme_en_a = response.xpath('//*[@id="uog4PageWrapper"]/div[3]/div/div/h1').extract()
        programme_en_a = ''.join(programme_en_a)
        programme_en_a = remove_tags(programme_en_a)
        programme_en_a = clear_space_str(programme_en_a)
        try:
            degree_name = re.findall(r'\([a-zA-Z]+\sHons\)',programme_en_a)[0]
        except:
            degree_name = ''
        programme_en = programme_en_a.replace(degree_name,'').strip()
        degree_name = degree_name.replace('(','').replace(')','').replace('Hons','').strip()
        degree_type = 1
        # print(degree_name)
        # print(programme_en)

        #6.alevel
        alevel = response.xpath("//*[contains(text(),'Typical offers')]//following-sibling::*[1]").extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel)
        # print(alevel)

        #7.apply_desc_en
        apply_desc_en = response.xpath('//*[@id="tab-1"]').extract()
        apply_desc_en = ''.join(apply_desc_en)
        apply_desc_en = remove_class(apply_desc_en)
        # print(apply_desc_en)

        #8.location
        location = response.xpath("//*[contains(text(),'Campus')]//following-sibling::p[1]").extract()
        location = ''.join(location)
        location = remove_tags(location)
        if len(location)>200:
            location = ''
        # print(location)

        #9.overview_en
        overview_en = response.xpath("//div[@class='cep-promo-block']//p/../preceding-sibling::*").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        if len(overview_en)==0:
            overview_en = response.xpath('//*[@id="courseOutline"]/div/p').extract()
            overview_en = ''.join(overview_en)
            overview_en = remove_class(overview_en)
        # print(overview_en)

        #10.tuition_fee_pre
        tuition_fee_pre = '£'

        #11.tuition_fee
        tuition_fee = 13840

        #12.apply_proces_en
        apply_proces_en = 'http://www.glos.ac.uk/study/undergraduate/pages/apply-for-an-undergraduate-degree.aspx'

        #13.ucascode
        try:
            ucascode_a = response.xpath("//*[contains(text(),'UCAS codes available for this subject')]/../following-sibling::*").extract()[0]
            ucascode = remove_tags(ucascode_a)
        except:
            ucascode = 'N/A'
            ucascode_a= ''
        try:
            ucascode = ucascode[-4:]
        except:
            ucascode = ''
        # print(ucascode)

        #14.ielts 15161718
        ielts =6.0
        ielts_r = 5.5
        ielts_w = 5.5
        ielts_l = 5.5
        ielts_s = 5.5


        #19.career_en
        career_en = response.xpath("//*[contains(text(),'Careers')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #20.require_chinese_en
        require_chinese_en = '<p>Foundation Successful completion of Year 2 Senior High with 60% average  OR  Successful completion of Year 3 with a pass  IELTS 4.0 Undergraduate (Bachelors) Successful completion of Senior High School with a pass including a pass in Maths PLUS  Completion of a recognised foundation course OR  Successful completion of 1 year of University with a minimum of 60% IELTS 6.0 overall with no less than 5.5 in any band</p>'

        #21.apply_pre
        apply_pre = '£'

        #22.duration
        try:
            duration = re.findall('\d',ucascode_a)[0]
        except:
            duration = ''
        # print(duration)

        #23.modules_en
        modules_en_url = response.xpath('//div[@id="ctaCourseMap"]//div//h2//a//@href|//*[@id="ctaCourseMap"]/a/@href').extract()
        modules_en_url = ''.join(modules_en_url)
        if len(modules_en_url) != 0:
            modules_en_url = 'http://www.glos.ac.uk' + modules_en_url
            # print(modules_en_url)
        if len(modules_en_url) != 0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data = requests.get(modules_en_url, headers=headers)
            response2 = etree.HTML(data.text)
            judge = response2.xpath('//*[@id="uog4MainContent"]/div/div[2]/div[1]/div/ul/li/a/@href')
            if len(judge) != 0:
                modules_en_url = modules_en_url + '/pages/' + judge[-1]
                # print(modules_en_url)
        if len(modules_en_url) != 0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data = requests.get(modules_en_url, headers=headers)
            response3 = etree.HTML(data.text)
            modules_en = response3.xpath("//*[contains(@id,'Level')]")
            doc = ""
            if len(modules_en) > 0:
                for a in modules_en:
                    doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc = remove_class(doc)
        else:
            doc = ''

        item['modules_en'] =doc
        item['apply_pre'] = apply_pre
        item['require_chinese_en'] = require_chinese_en
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_name'] = degree_name
        item['degree_type'] = degree_type
        item['location'] = location
        item['overview_en'] = overview_en
        item['tuition_fee_pre'] = tuition_fee_pre
        item['tuition_fee'] = tuition_fee
        item['apply_proces_en'] = apply_proces_en
        item['alevel'] = alevel
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['career_en'] = career_en
        item['apply_desc_en'] = apply_desc_en

        ucascodes = response.xpath("//*[contains(text(),'UCAS codes available for this subject')]/../following-sibling::*").extract()
        if len(ucascodes)>1:
            for i in ucascodes:
                response_ucascode = i
                response_ucascode = remove_tags(response_ucascode)
                response_duration = re.findall('\d',response_ucascode)[0]
                response_ucascode = response_ucascode[-4:]
                item['ucascode'] = response_ucascode
                item['duration'] = response_duration
                yield item
        else:
            item['ucascode'] = ucascode
            item['duration'] = duration
            yield item