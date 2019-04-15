# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/9 9:00'
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
from scrapySchool_England.TranslateMonth import translate_month
from translate import translate
import requests
from lxml import etree
from bs4 import  BeautifulSoup
class UniversityofGreenwichSpider(scrapy.Spider):
    name = 'UniversityofGreenwich_u'
    allowed_domains = ['gre.ac.uk/']
    start_urls = []
    C= [
        'https://www.gre.ac.uk/ug/ach/g100',
        'https://www.gre.ac.uk/ug/eduhea/l591',
        'https://www.gre.ac.uk/ug/ach/v100',
        'https://www.gre.ac.uk/ug/eduhea/x360',
        'https://www.gre.ac.uk/ug/eduhea/9k65',
        'https://www.gre.ac.uk/ug/ach/soc-cri',
        'https://www.gre.ac.uk/ug/engsci/gg4q',
        'https://www.gre.ac.uk/ug/ach/g600',
        'https://www.gre.ac.uk/ug/engsci/2w00',
        'https://www.gre.ac.uk/ug/engsci/h650',
        'https://www.gre.ac.uk/ug/ach/q3w8',
        'https://www.gre.ac.uk/ug/engsci/f410',
        'https://www.gre.ac.uk/ug/engsci/h200',
        'https://www.gre.ac.uk/ug/engsci/b401',
        'https://www.gre.ac.uk/ug/engsci/cf13',
        'https://www.gre.ac.uk/ug/engsci/g401',
        'https://www.gre.ac.uk/ug/ach/ww37',
        'https://www.gre.ac.uk/ug/ach/mat-mmath',
        'https://www.gre.ac.uk/ug/ach/k242',
        'https://www.gre.ac.uk/ug/ach/w400',
        'https://www.gre.ac.uk/ug/ach/k252',
        'https://www.gre.ac.uk/ug/business-school/n1nn',
        'https://www.gre.ac.uk/ug/eduhea/x320',
        'https://www.gre.ac.uk/ug/ach/mc98',
        'https://www.gre.ac.uk/ug/business-school/n1nj',
        'https://www.gre.ac.uk/ug/business-school/nj19',
        'https://www.gre.ac.uk/ug/ach/gg64',
        'https://www.gre.ac.uk/ug/business-school/nnc2',
        'https://www.gre.ac.uk/ug/business-school/nr11',
        'https://www.gre.ac.uk/ug/eduhea/b781',
        'https://www.gre.ac.uk/ug/engsci/f918',
        'https://www.gre.ac.uk/ug/eduhea/x314',
        'https://www.gre.ac.uk/ug/ach/i10f',
        'https://www.gre.ac.uk/ug/business-school/n300',
        'https://www.gre.ac.uk/ug/ach/p315',
        'https://www.gre.ac.uk/ug/business-school/n15n',
        'https://www.gre.ac.uk/ug/business-school/n1nq',
        'https://www.gre.ac.uk/ug/business-school/n2fy',
        'https://www.gre.ac.uk/ug/eduhea/c800',
        'https://www.gre.ac.uk/ug/business-school/n600',
        'https://www.gre.ac.uk/ug/eduhea/b720',
        'https://www.gre.ac.uk/ug/ach/ww55',
        'https://www.gre.ac.uk/ug/business-school/n196',
        'https://www.gre.ac.uk/ug/pc/bsc-hons-agriculture-hadlow-college',
        'https://www.gre.ac.uk/ug/eduhea/x310',
        'https://www.gre.ac.uk/ug/engsci/h609',
        'https://www.gre.ac.uk/ug/ach/i311',
        'https://www.gre.ac.uk/ug/ach/p317',
        'https://www.gre.ac.uk/ug/business-school/n16n',
        'https://www.gre.ac.uk/ug/business-school/nn43',
        'https://www.gre.ac.uk/ug/ach/p390',
        'https://www.gre.ac.uk/ug/business-school/n920',
        'https://www.gre.ac.uk/ug/pc/bsc-hons-international-agriculture',
        'https://www.gre.ac.uk/ug/ach/n390',
        'https://www.gre.ac.uk/ug/ach/k310',
        'https://www.gre.ac.uk/ug/ach/vq13',
        'https://www.gre.ac.uk/ug/eduhea/c608',
        'https://www.gre.ac.uk/ug/eduhea/b912',
        'https://www.gre.ac.uk/ug/eduhea/c8b9',
        'https://www.gre.ac.uk/ug/ach/vl12',
        'https://www.gre.ac.uk/ug/business-school/n4n3',
        'https://www.gre.ac.uk/ug/eduhea/b761',
        'https://www.gre.ac.uk/ug/business-school/nn21',
        'https://www.gre.ac.uk/ug/eduhea/b902',
        'https://www.gre.ac.uk/ug/business-school/n302',
        'https://www.gre.ac.uk/ug/pc/bsc-hons-horticulture-commercial',
        'https://www.gre.ac.uk/ug/ach/i202',
        'https://www.gre.ac.uk/ug/ach/DMDD',
        'https://www.gre.ac.uk/ug/engsci/pharm-physio',
        'https://www.gre.ac.uk/ug/ach/m2fy',
        'https://www.gre.ac.uk/ug/ach/p316',
        'https://www.gre.ac.uk/ug/engsci/geography-extended,-bsc-hons',
        'https://www.gre.ac.uk/ug/business-school/n13n',
        'https://www.gre.ac.uk/ug/pc/bsc-hons-equine-training-and-management',
        'https://www.gre.ac.uk/ug/business-school/l112',
        'https://www.gre.ac.uk/ug/business-school/l101',
        'https://www.gre.ac.uk/ug/engsci/c100',
        'https://www.gre.ac.uk/ug/engsci/chemical-engineering,-meng',
        'https://www.gre.ac.uk/ug/business-school/n203',
        'https://www.gre.ac.uk/ug/ach/g404',
        'https://www.gre.ac.uk/ug/ach/m211',
        'https://www.gre.ac.uk/ug/ach/computer-science-networking,-bsc-hons',
        'https://www.gre.ac.uk/ug/pc/bsc-hons-animal-management',
        'https://www.gre.ac.uk/ug/eduhea/nursing',
        'https://www.gre.ac.uk/ug/business-school/nn25',
        'https://www.gre.ac.uk/ug/pc/bsc-hons-aquaculture-and-fisheries-management',
        'https://www.gre.ac.uk/ug/eduhea/b760',
        'https://www.gre.ac.uk/ug/pc/bsc-hons-applied-equine-welfare-and-management',
        'https://www.gre.ac.uk/ug/business-school/n501',
        'https://www.gre.ac.uk/ug/ach/m100',
        'https://www.gre.ac.uk/ug/business-school/n201',
        'https://www.gre.ac.uk/ug/engsci/natural-sciences,-bsc-hons',
        'https://www.gre.ac.uk/ug/ach/w210',
        'https://www.gre.ac.uk/ug/business-school/250',
        'https://www.gre.ac.uk/ug/ach/computer-science-games,-bsc-hons',
        'https://www.gre.ac.uk/ug/business-school/n862',
        'https://www.gre.ac.uk/ug/business-school/nmr9',
        'https://www.gre.ac.uk/ug/business-school/n287',
        'https://www.gre.ac.uk/ug/engsci/chemical-engineering,-beng',
        'https://www.gre.ac.uk/ug/business-school/n820',
        'https://www.gre.ac.uk/ug/engsci/pharm-physio-with-fd',
        'https://www.gre.ac.uk/ug/business-school/n602',
        'https://www.gre.ac.uk/ug/ach/computer-science-data-science,-bsc-hons',
        'https://www.gre.ac.uk/ug/business-school/n835',
        'https://www.gre.ac.uk/ug/eduhea/bsc-hons-speech-and-language-therapy',
        'https://www.gre.ac.uk/ug/pc/bsc-hons-animal-conservation-and-biodiversity',
        'https://www.gre.ac.uk/ug/engsci/biology,-bsc-hons',
        'https://www.gre.ac.uk/ug/business-school/n506',
        'https://www.gre.ac.uk/ug/ach/studyabroad',
        'https://www.gre.ac.uk/ug/business-school/nnr0',
        'https://www.gre.ac.uk/ug/pc/bsc-hons-agriculture-hadlow-college',
        'https://www.gre.ac.uk/ug/business-school/p210',
        'https://www.gre.ac.uk/ug/business-school/n823',
        'https://www.gre.ac.uk/ug/engsci/environmental-science-extended,-bsc-hons',
        'https://www.gre.ac.uk/ug/business-school/n125',
        'https://www.gre.ac.uk/ug/business-school/l1nh',
        'https://www.gre.ac.uk/ug/business-school/l100',
        'https://www.gre.ac.uk/ug/business-school/n400',
        'https://www.gre.ac.uk/ug/pc/bsc-hons-equine-sports-therapy-and-rehabilitation',
        'https://www.gre.ac.uk/ug/ach/digital-media-design-development',
        'https://www.gre.ac.uk/ug/ach/computer-science-cyber-security,-bsc-hons',
        'https://www.gre.ac.uk/ug/business-school/n120',
        'https://www.gre.ac.uk/ug/business-school/nrc1',
        'https://www.gre.ac.uk/ug/ach/games-design-and-development-programming,-bsc-hons',
        'https://www.gre.ac.uk/ug/pc/bsc-hons-applied-behavioural-science-and-welfare',
        'https://www.gre.ac.uk/ug/pc/ba-hons-garden-design',
        'https://www.gre.ac.uk/ug/eduhea/b710',
        'https://www.gre.ac.uk/ug/engsci/chemical-engineering-extended,-beng-hons',
        'https://www.gre.ac.uk/ug/ach/mathematics,-bsc-hons-extended',
        'https://www.gre.ac.uk/ug/pc/bsc-hons-landscape-and-countryside-management',
        'https://www.gre.ac.uk/ug/ach/x162',
        'https://www.gre.ac.uk/ug/engsci/h102',
        'https://www.gre.ac.uk/ug/engsci/h104',
        'https://www.gre.ac.uk/ug/engsci/h105',
        'https://www.gre.ac.uk/ug/ach/g311',
        'https://www.gre.ac.uk/ug/engsci/h700',
        'https://www.gre.ac.uk/ug/engsci/c743',
        'https://www.gre.ac.uk/ug/engsci/h6gp',
        'https://www.gre.ac.uk/ug/engsci/f110',
        'https://www.gre.ac.uk/ug/engsci/n1nk',
        'https://www.gre.ac.uk/ug/engsci/b208',
        'https://www.gre.ac.uk/ug/engsci/h308',
        'https://www.gre.ac.uk/ug/engsci/h304',
        'https://www.gre.ac.uk/ug/engsci/f413',
        'https://www.gre.ac.uk/ug/engsci/gn52',
        'https://www.gre.ac.uk/ug/ach/gg41',
        'https://www.gre.ac.uk/ug/engsci/6h50',
        'https://www.gre.ac.uk/ug/ach/k100',
        'https://www.gre.ac.uk/ug/engsci/c6x1',
        'https://www.gre.ac.uk/ug/engsci/f801',
        'https://www.gre.ac.uk/ug/ach/q390',
        'https://www.gre.ac.uk/ug/ach/gf54',
        'https://www.gre.ac.uk/ug/engsci/n106',
        'https://www.gre.ac.uk/ug/ach/q300',
        'https://www.gre.ac.uk/ug/engsci/h600',
        'https://www.gre.ac.uk/ug/ach/lc38',
        'https://www.gre.ac.uk/ug/engsci/f4m9',
        'https://www.gre.ac.uk/ug/ach/l300',
        'https://www.gre.ac.uk/ug/pc/ww54',
        'https://www.gre.ac.uk/ug/ach/g400',
        'https://www.gre.ac.uk/ug/engsci/h603',
        'https://www.gre.ac.uk/ug/engsci/f100',
        'https://www.gre.ac.uk/ug/engsci/h203',
        'https://www.gre.ac.uk/ug/engsci/h103',
        'https://www.gre.ac.uk/ug/ach/vl13',
        'https://www.gre.ac.uk/ug/eduhea/x300',
        'https://www.gre.ac.uk/ug/engsci/b230',
        'https://www.gre.ac.uk/ug/ach/qw43',
        'https://www.gre.ac.uk/ug/engsci/c609',
        'https://www.gre.ac.uk/ug/ach/lt22',
        'https://www.gre.ac.uk/ug/engsci/65h0',
        'https://www.gre.ac.uk/ug/eduhea/l500',
        'https://www.gre.ac.uk/ug/engsci/hnc2',
        'https://www.gre.ac.uk/ug/ach/w801',
        'https://www.gre.ac.uk/ug/ach/gw42',
        'https://www.gre.ac.uk/ug/engsci/c1fy',
        'https://www.gre.ac.uk/ug/ach/i312',
        'https://www.gre.ac.uk/ug/engsci/c690',
        'https://www.gre.ac.uk/ug/engsci/1h50',
        'https://www.gre.ac.uk/ug/engsci/b408',
        'https://www.gre.ac.uk/ug/engsci/c610',
        'https://www.gre.ac.uk/ug/engsci/c600',
        'https://www.gre.ac.uk/ug/ach/i304',
        'https://www.gre.ac.uk/ug/engsci/7h00',
        'https://www.gre.ac.uk/ug/ach/g1l1',
        'https://www.gre.ac.uk/ug/engsci/f105',
        'https://www.gre.ac.uk/ug/engsci/b202',
        'https://www.gre.ac.uk/ug/engsci/b940',
        'https://www.gre.ac.uk/ug/engsci/c611',
        'https://www.gre.ac.uk/ug/ach/lt23',
        'https://www.gre.ac.uk/ug/engsci/n1n5',
        'https://www.gre.ac.uk/ug/engsci/h208',
        'https://www.gre.ac.uk/ug/engsci/f412',
        'https://www.gre.ac.uk/ug/ach/g402',
        'https://www.gre.ac.uk/ug/ach/g1n2',
        'https://www.gre.ac.uk/ug/ach/qw38'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Greenwich'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="default"]/header/div/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        programme_en = clear_space_str(programme_en)
        programme_en = programme_en.split(',')
        programme_en = ''.join(programme_en[:-1])
        # print(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 1

        #5.degree_name
        try:
            degree_name =re.findall(r',(.*)',programme_en)[0].strip()
        except:
            degree_name = 'N/A'
        if ',' in degree_name:
            degree_name = re.findall(r',(.*)',degree_name)[0].strip()
        try:
            programme_en = programme_en.replace(degree_name,'').replace(',','').strip()
        except:
            pass
        # print(programme_en)
        # print(degree_name)

        #6.department
        department = response.xpath('//i[@aria-label="Department"]//following-sibling::*').extract()
        department = ''.join(department)
        department = remove_tags(department)
        if '&amp; ' in department:
            department = department.replace('&amp; ','')
        # print(department)

        #7.location
        location = response.xpath('//i[@aria-label="Location"]//following-sibling::*').extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #8.ucascode
        ucascode = response.xpath('//*[@id="faculty"]/div[2]/article/div/div/div[1]/div[2]/div[2]/div/h3').extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode)
        ucascode = ucascode[:4]
        # print(ucascode)

        #9.duration #10.duration_per
        duration = response.xpath('//*[@aria-label="Duration"]//following-sibling::p[1]').extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        duration = duration.replace('full time','').strip()
        # print(duration)
        duration_per = 1

        #11.overview_en
        overview_en = response.xpath("//div[contains(@class,'overview-text')]").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #12.modules_en
        modules_en_url = response.xpath("//meta[@name='prog_no']//@content").extract()
        modules_en_url = ''.join(modules_en_url)
        if len(modules_en_url)!=0:
            modules_en_url = 'https://www.gre.ac.uk/ug/content/ajax/courses-ajax-call?prog='+str(modules_en_url)
        else:modules_en_url = ''
        if len(modules_en_url)!=0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data = requests.get(modules_en_url, headers=headers)
            response1 = etree.HTML(data.text)
            modules_en =  response1.xpath("//div[@class='gre-page-copy']")
            doc = ""
            if len(modules_en) > 0:
                for a in modules_en:
                    doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc = remove_class(doc)
        else:
            modules_en = 'N/A'
            doc = ''
        print(modules_en)



        #13.apply_desc_en
        apply_desc_en = response.xpath('//*[@id="entry-requirements"]/div').extract()
        apply_desc_en = ''.join(apply_desc_en)
        apply_desc_en = remove_class(apply_desc_en).strip()
        # print(apply_desc_en)

        #14.assessment_en
        try:
            assessment_en = response.xpath("//h3[contains(text(),'Careers')]//preceding-sibling::*").extract()
            assessment_en = ''.join(assessment_en)
            assessment_en = remove_class(assessment_en)
        except:
            assessment_en = ''
        # print(assessment_en)

        #15.career_en
        career_en = response.xpath("//h4[contains(text(),'Do you provide employability services?')]//preceding-sibling::*").extract()
        if len(career_en)==0:
            career_en = response.xpath("//h4[contains(text(),'areers')]/following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #16.tuition_fee
        if 'Adult Nursing' in programme_en:
            tuition_fee = 13950
        elif 'Business Logistics and Transport Management' in programme_en:
            tuition_fee = 13950
        elif 'Business Purchasing and Supply Chain Management' in programme_en:
            tuition_fee = 13950
        elif 'Business Studies' in programme_en:
            tuition_fee = 13950
        elif 'Business with Accounting' in programme_en:
            tuition_fee = 13950
        elif 'Business with Finance' in programme_en:
            tuition_fee = 13950
        elif 'Business with Human Resource Management' in programme_en:
            tuition_fee = 13950
        elif 'Business with Marketing' in programme_en:
            tuition_fee = 13950
        elif "Children's Nursing" in programme_en:
            tuition_fee = 13950
        elif 'Law' in programme_en:
            tuition_fee = 13950
        elif 'Nursing' in programme_en:
            tuition_fee = 13950
        elif 'Mental Health Work' in programme_en:
            tuition_fee = 13950
        elif 'Midwifery' in programme_en:
            tuition_fee = 13950
        elif 'Paramedic Science' in programme_en:
            tuition_fee = 13950
        elif 'Specialist Community Public Health' in programme_en:
            tuition_fee = 13950
        elif 'Study Abroad' in programme_en:
            tuition_fee = 13950
        else:
            tuition_fee = 12100

        #17.tuition_fee_pre
        tuition_fee_pre = '£'

        #18.apply_proces_en
        apply_proces_en = 'https://www.gre.ac.uk/study/apply/ug'

        #19.ielts 20212223
        ielts = 6.5
        ielts_r = 5.5
        ielts_w = 5.5
        ielts_s = 5.5
        ielts_l = 5.5

        #24.apply_pre
        apply_pre = '£'

        #25.alevel
        alevel = response.xpath("//*[contains(text(),'UCAS points')]//following-sibling::*[1]").extract()
        if len(alevel)==0:
            alevel = response.xpath("//*[contains(text(),'points')]//text()").extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel)
        try:
            alevel = re.findall('(\d+)\W\(view',alevel)[0]
        except:
            alevel = ''
        if len(alevel)==0:
            alevel = response.xpath("//*[contains(text(),'points')]//text()").extract()
            alevel = ''.join(alevel)
            try:
                alevel = re.findall('(\d+)\WUCAS',alevel)[0]
            except:
                alevel = None
        alevel = alevel + ' UCAS points'
        # print(alevel)

        item["alevel"] = alevel
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['department'] = department
        item['location'] = location
        item['ucascode'] = ucascode
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['overview_en'] = overview_en
        # item['modules_en'] = doc
        item['apply_desc_en'] = apply_desc_en
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_proces_en'] = apply_proces_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        yield  item

