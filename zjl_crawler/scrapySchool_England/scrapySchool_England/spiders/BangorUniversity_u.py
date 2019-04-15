# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/24 16:02'
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
class BangorUniversitySpider(scrapy.Spider):
    name = 'BangorUniversity_u'
    allowed_domains = ['bangor.ac.uk/']
    start_urls = []
    C = ['https://www.bangor.ac.uk/international/courses/undergraduate/MR94-Criminology-and-Criminal-Justice-and-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/3L3Q-Sociology-and-English-Literature',
'https://www.bangor.ac.uk/international/courses/undergraduate/LV31-Sociology-and-History',
'https://www.bangor.ac.uk/international/courses/undergraduate/LQ31-Sociology-and-Linguistics',
'https://www.bangor.ac.uk/international/courses/undergraduate/LM39-Sociology-and-Criminology-and-Criminal-Justice',
'https://www.bangor.ac.uk/international/courses/undergraduate/R1C6-French-and-Sport-Science',
'https://www.bangor.ac.uk/international/courses/undergraduate/NR32-German-and-Banking',
'https://www.bangor.ac.uk/international/courses/undergraduate/NR31-French-and-Banking',
'https://www.bangor.ac.uk/international/courses/undergraduate/NR42-German-and-Accounting',
'https://www.bangor.ac.uk/international/courses/undergraduate/WR92-German-and-Creative-Studies',
'https://www.bangor.ac.uk/international/courses/undergraduate/WR91-French-and-Creative-Studies',
'https://www.bangor.ac.uk/international/courses/undergraduate/06CD-French-and-English-Literature',
'https://www.bangor.ac.uk/international/courses/undergraduate/MT10-Law-with-Contemporary-Chinese-Studies',
'https://www.bangor.ac.uk/international/courses/undergraduate/NR54-Marketing-and-Spanish-4-year',
'https://www.bangor.ac.uk/international/courses/undergraduate/NR1F-Business-Studies-and-German',
'https://www.bangor.ac.uk/international/courses/undergraduate/NR34-Banking-and-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/PR32-Film-Studies-and-German',
'https://www.bangor.ac.uk/international/courses/undergraduate/P3W8-Film-Studies-and-Creative-Writing',
'https://www.bangor.ac.uk/international/courses/undergraduate/PR34-Film-Studies-and-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/LP33-Media-Studies-and-Sociology',
'https://www.bangor.ac.uk/international/courses/undergraduate/P0R3-Film-Studies-and-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/W900-Creative-Practice',
'https://www.bangor.ac.uk/international/courses/undergraduate/W891-Professional-Writing',
'https://www.bangor.ac.uk/international/courses/undergraduate/P308-Media-Studies',
'https://www.bangor.ac.uk/international/courses/undergraduate/WW93-Creative-Studies-and-Music',
'https://www.bangor.ac.uk/international/courses/undergraduate/PW33-Media-Studies-and-Music',
'https://www.bangor.ac.uk/international/courses/undergraduate/PQ3J-Film-Studies-and-English-Language',
'https://www.bangor.ac.uk/international/courses/undergraduate/PR31-Film-Studies-and-French',
'https://www.bangor.ac.uk/international/courses/undergraduate/P3V1-Film-Studies-and-History',
'https://www.bangor.ac.uk/international/courses/undergraduate/3P3Q-English-Literature-and-Film-Studies',
'https://www.bangor.ac.uk/international/courses/undergraduate/32N6-English-Literature-and-Music',
'https://www.bangor.ac.uk/international/courses/undergraduate/3YT5-English-Literature-and-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/1Q3Q-English-Literature-and-Linguistics',
'https://www.bangor.ac.uk/international/courses/undergraduate/M3Q9-English-Literature-and-Criminology-and-Criminal-Justice',
'https://www.bangor.ac.uk/international/courses/undergraduate/NR51-Marketing-and-French-4-year',
'https://www.bangor.ac.uk/international/courses/undergraduate/NR1C-Business-Studies-and-French',
'https://www.bangor.ac.uk/international/courses/undergraduate/R2C6-German-and-Sport-Science',
'https://www.bangor.ac.uk/international/courses/undergraduate/MR91-French-and-Criminology-and-Criminal-Justice',
'https://www.bangor.ac.uk/international/courses/undergraduate/WR94-Spanish-and-Creative-Studies',
'https://www.bangor.ac.uk/international/courses/undergraduate/NR41-French-and-Accounting',
'https://www.bangor.ac.uk/international/courses/undergraduate/3N7S-German-and-English-Literature',
'https://www.bangor.ac.uk/international/courses/undergraduate/CR6K-Spanish-and-Sport-Science',
'https://www.bangor.ac.uk/international/courses/undergraduate/NR52-Marketing-and-German-4-year',
'https://www.bangor.ac.uk/international/courses/undergraduate/NR1K-Business-Studies-and-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/NR44-Accounting-and-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/V104-Welsh-History-and-Archaeology',
'https://www.bangor.ac.uk/international/courses/undergraduate/VP23-Welsh-History-and-Film-Studies',
'https://www.bangor.ac.uk/international/courses/undergraduate/MVX1-History-and-Criminology-and-Criminal-Justice',
'https://www.bangor.ac.uk/international/courses/undergraduate/VW2H-Welsh-History-and-Music',
'https://www.bangor.ac.uk/international/courses/undergraduate/LVH2-Welsh-History-and-Sociology',
'https://www.bangor.ac.uk/international/courses/undergraduate/VW23-Welsh-History-and-Music',
'https://www.bangor.ac.uk/international/courses/undergraduate/VW13-History-and-Music',
'https://www.bangor.ac.uk/international/courses/undergraduate/RV41-History-and-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/RV11-History-and-French',
'https://www.bangor.ac.uk/international/courses/undergraduate/3QV1-History-and-English-Literature',
'https://www.bangor.ac.uk/international/courses/undergraduate/RV21-History-and-German',
'https://www.bangor.ac.uk/international/courses/undergraduate/V2P3-Welsh-History-with-Film-Studies',
'https://www.bangor.ac.uk/international/courses/undergraduate/WR34-Music-and-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/WV32-Music-and-History-and-Welsh-History',
'https://www.bangor.ac.uk/international/courses/undergraduate/WR32-Music-and-German',
'https://www.bangor.ac.uk/international/courses/undergraduate/RW13-Music-and-French',
'https://www.bangor.ac.uk/international/courses/undergraduate/X321-Childhood-and-Youth-Studies-and-Welsh',
'https://www.bangor.ac.uk/international/courses/undergraduate/X319-Childhood-and-Youth-Studies-and-Psychology',
'https://www.bangor.ac.uk/international/courses/undergraduate/X315-Childhood-and-Youth-Studies-and-Sociology',
'https://www.bangor.ac.uk/international/courses/undergraduate/MC98-Criminology-and-Criminal-Justice-and-Psychology',
'https://www.bangor.ac.uk/international/courses/undergraduate/QR3C-English-Language-and-French',
'https://www.bangor.ac.uk/international/courses/undergraduate/QR3F-English-Language-and-German',
'https://www.bangor.ac.uk/international/courses/undergraduate/LQ3J-English-Language-and-Sociology',
'https://www.bangor.ac.uk/international/courses/undergraduate/QR3K-English-Language-and-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/LM52-Health-and-Social-Care-and-Criminology-and-Criminal-Justice',
'https://www.bangor.ac.uk/international/courses/undergraduate/LL53-Health-and-Social-Care-and-Sociology',
'https://www.bangor.ac.uk/international/courses/undergraduate/QR11-Linguistics-and-French',
'https://www.bangor.ac.uk/international/courses/undergraduate/QR12-Linguistics-and-German',
'https://www.bangor.ac.uk/international/courses/undergraduate/QR14-Linguistics-and-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/QQ3M-English-Language-and-Cymraeg',
'https://www.bangor.ac.uk/international/courses/undergraduate/CL83-Sociology-and-Psychology',
'https://www.bangor.ac.uk/international/courses/undergraduate/Q102-Bilingualism',
'https://www.bangor.ac.uk/international/courses/undergraduate/Q101-Linguistics',
'https://www.bangor.ac.uk/international/courses/undergraduate/B720-Midwifery',
'https://www.bangor.ac.uk/international/courses/undergraduate/VVV2-Philosophy-Religion-and-Welsh-History',
'https://www.bangor.ac.uk/international/courses/undergraduate/VVR4-Philosophy-Religion-and-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/VVW3-Philosophy-Religion-and-Music',
'https://www.bangor.ac.uk/international/courses/undergraduate/VVV1-Philosophy-Religion-and-History',
'https://www.bangor.ac.uk/international/courses/undergraduate/VVQ5-Philosophy-Religion-and-Welsh',
'https://www.bangor.ac.uk/international/courses/undergraduate/VVR3-Philosophy-Religion-and-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/VVR1-Philosophy-Religion-and-French',
'https://www.bangor.ac.uk/international/courses/undergraduate/D501-Forestry-with-placement-year',
'https://www.bangor.ac.uk/international/courses/undergraduate/RR14-French-and-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/RR24-German-and-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/RR13-French-and-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/RR23-German-and-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/RR12-French-and-German',
'https://www.bangor.ac.uk/international/courses/undergraduate/RR43-Italian-and-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/R2C8-German-with-Psychology',
'https://www.bangor.ac.uk/international/courses/undergraduate/RV31-History-and-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/R1P3-French-with-Media-Studies',
'https://www.bangor.ac.uk/international/courses/undergraduate/R4R3-Spanish-with-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/CR6H-Italian-and-Sport-Science',
'https://www.bangor.ac.uk/international/courses/undergraduate/R400-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/R1N1-French-with-Marketing',
'https://www.bangor.ac.uk/international/courses/undergraduate/WR33-Music-and-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/R4N5-Spanish-with-Marketing',
'https://www.bangor.ac.uk/international/courses/undergraduate/R4N1-Spanish-with-Business-Studies',
'https://www.bangor.ac.uk/international/courses/undergraduate/NR53-Marketing-and-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/R1R3-French-with-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/R1R2-French-with-German',
'https://www.bangor.ac.uk/international/courses/undergraduate/QR13-Italian-and-Linguistics',
'https://www.bangor.ac.uk/international/courses/undergraduate/R1NC-French-with-Business-Studies',
'https://www.bangor.ac.uk/international/courses/undergraduate/R200-German',
'https://www.bangor.ac.uk/international/courses/undergraduate/R2NC-German-with-Business-Studies',
'https://www.bangor.ac.uk/international/courses/undergraduate/R4W8-Spanish-with-Creative-Writing',
'https://www.bangor.ac.uk/international/courses/undergraduate/R2P4-German-with-Media-Studies',
'https://www.bangor.ac.uk/international/courses/undergraduate/R4P3-Spanish-with-Media-Studies',
'https://www.bangor.ac.uk/international/courses/undergraduate/NR1H-Business-Studies-and-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/NR33-Banking-and-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/R1R4-French-with-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/R2W8-German-with-Creative-Writing',
'https://www.bangor.ac.uk/international/courses/undergraduate/R101-French',
'https://www.bangor.ac.uk/international/courses/undergraduate/R1P5-French-with-Journalism',
'https://www.bangor.ac.uk/international/courses/undergraduate/09V3-English-Literature-and-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/R2N1-German-with-Marketing',
'https://www.bangor.ac.uk/international/courses/undergraduate/R4R2-Spanish-with-German',
'https://www.bangor.ac.uk/international/courses/undergraduate/R2P5-German-with-Journalism',
'https://www.bangor.ac.uk/international/courses/undergraduate/QR3H-English-Language-and-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/R1W8-French-with-Creative-Writing',
'https://www.bangor.ac.uk/international/courses/undergraduate/R2R1-German-with-French',
'https://www.bangor.ac.uk/international/courses/undergraduate/R2R4-German-with-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/R2R3-German-with-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/NR43-Accounting-and-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/R1C8-French-with-Psychology',
'https://www.bangor.ac.uk/international/courses/undergraduate/R4R1-Spanish-with-French',
'https://www.bangor.ac.uk/international/courses/undergraduate/R4P5-Spanish-with-Journalism',
'https://www.bangor.ac.uk/international/courses/undergraduate/QR53-Italian-and-Cymraeg',
'https://www.bangor.ac.uk/international/courses/undergraduate/B741-Adult-Nursing',
'https://www.bangor.ac.uk/international/courses/undergraduate/B732-Childrens-Nursing',
'https://www.bangor.ac.uk/international/courses/undergraduate/B762-Mental-Health-Nursing',
'https://www.bangor.ac.uk/international/courses/undergraduate/B763-Learning-Disability-Nursing',
'https://www.bangor.ac.uk/international/courses/undergraduate/C880-Psychology-with-Clinical-and-Health-Psychology',
'https://www.bangor.ac.uk/international/courses/undergraduate/C807-Psychology',
'https://www.bangor.ac.uk/international/courses/undergraduate/C801-Psychology-with-Neuropsychology',
'https://www.bangor.ac.uk/international/courses/undergraduate/X1WF-Design-and-Technology-Secondary-Education',
'https://www.bangor.ac.uk/international/courses/undergraduate/N5R4-Marketing-with-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/N5R3-Marketing-with-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/N5R1-Marketing-with-French',
'https://www.bangor.ac.uk/international/courses/undergraduate/N5R2-Marketing-with-German',
'https://www.bangor.ac.uk/international/courses/undergraduate/LL13-Sociology-and-Economics',
'https://www.bangor.ac.uk/international/courses/undergraduate/LV11-History-and-Economics',
'https://www.bangor.ac.uk/international/courses/undergraduate/C808-Psychology-with-Clinical-and-Health-Psychology',
'https://www.bangor.ac.uk/international/courses/undergraduate/MR92-German-and-Criminology-and-Criminal-Justice',
'https://www.bangor.ac.uk/international/courses/undergraduate/QQC3-English-Language-and-English-Literature',
'https://www.bangor.ac.uk/international/courses/undergraduate/CB69-Sport-Health-and-Exercise-Science',
'https://www.bangor.ac.uk/international/courses/undergraduate/C600-Sport-Science',
'https://www.bangor.ac.uk/international/courses/undergraduate/C608-Sport-Health-and-Exercise-Science',
'https://www.bangor.ac.uk/international/courses/undergraduate/C609-Sport-Science-Outdoor-Activities',
'https://www.bangor.ac.uk/international/courses/undergraduate/C651-Sport-Health-and-Physical-Education',
'https://www.bangor.ac.uk/international/courses/undergraduate/C602-Sport-Science-Outdoor-Activities',
'https://www.bangor.ac.uk/international/courses/undergraduate/C680-Sport-and-Exercise-Psychology',
'https://www.bangor.ac.uk/international/courses/undergraduate/C607-Sport-Science',
'https://www.bangor.ac.uk/international/courses/undergraduate/VVR2-Philosophy-Religion-and-German',
'https://www.bangor.ac.uk/international/courses/undergraduate/3VQV-Philosophy-Religion-and-English-Literature',
'https://www.bangor.ac.uk/international/courses/undergraduate/D500-Forestry',
'https://www.bangor.ac.uk/international/courses/undergraduate/Q563-Professional-Welsh',
'https://www.bangor.ac.uk/international/courses/undergraduate/MR95-Criminology-Criminal-Justice-and-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/WR93-Creative-Studies-and-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/V101-History',
'https://www.bangor.ac.uk/international/courses/undergraduate/T124-English-Literature-and-Chinese',
'https://www.bangor.ac.uk/international/courses/undergraduate/T125-Film-Studies-and-Chinese',
'https://www.bangor.ac.uk/international/courses/undergraduate/C800-Psychology',
'https://www.bangor.ac.uk/international/courses/undergraduate/2R87-Psychology-with-Business',
'https://www.bangor.ac.uk/international/courses/undergraduate/N1R3-Business-Studies-with-Italian',
'https://www.bangor.ac.uk/international/courses/undergraduate/N1R1-Business-Studies-with-French',
'https://www.bangor.ac.uk/international/courses/undergraduate/N1R4-Business-Studies-with-Spanish',
'https://www.bangor.ac.uk/international/courses/undergraduate/N1R2-Business-Studies-with-German']
    # print(len(C))

    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Bangor University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.overview_en
        overview_en = response.xpath("//h3[contains(text(),'Key Facts from UniStats')]//preceding-sibling::*").extract()
        if len(overview_en)==0:
            overview_en = response.xpath('//*[@id="overview"]').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #4.programme_en
        programme_en = response.xpath('//*[@id="contents"]/h1/text()').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)
        # if len(programme_en)==0:
        #     print(response.url)

        #5.degree_type
        degree_type = 1

        #6.degree_name
        degree_name = response.xpath('//*[@id="contents"]/h1/span').extract()
        degree_name =''.join(degree_name)
        degree_name = remove_tags(degree_name).replace('(Hons)','')
        # print(degree_name)

        #7.duration
        duration_list =response.xpath('//*[@id="coursefacts"]/div[3]/span[2]').extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        try:
            duration = re.findall('\d+',duration_list)[0]
        except:
            duration = None
            # print(response.url)
        duration_per = 1
        # print(duration,'*********',duration_per)


        #8.modules_en
        # modules_en = response.xpath('//*[@id="content"]').extract()
        # modules_en = ''.join(modules_en)
        # modules_en = remove_class(modules_en)
        # modules_en = clear_space_str(modules_en)
        # # print(modules_en)
        try:
            modules_en_url  = response.xpath('//*[@id="content"]//@href').extract()[-1]
            modules_en_url = ''.join(modules_en_url)
        except:
            modules_en_url = ''
        if len(modules_en_url) != 0:
            modules_en_url = 'https://www.bangor.ac.uk' + modules_en_url
        if len(modules_en_url) != 0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            data = requests.get(modules_en_url, headers=headers)
            response3 = etree.HTML(data.text)
            modules_en = response3.xpath('//*[@id="contents"]')
            doc = ""
            if len(modules_en) > 0:
                for a in modules_en:
                    doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc = remove_class(doc)
                    modules_en = doc
            else:
                modules_en = None
        else:
            modules_en = None
        #9.ucascode
        ucascode = response.xpath('//*[@id="coursefacts"]/div[1]/span[2]').extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode)
        # print(ucascode)

        #10.ielts,11,12,13,14
        if 'Creative Studies' in programme_en:
            ielts =6.0
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
        elif 'Media' in programme_en:
            ielts = 6.0
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
        elif 'English Literature' in programme_en:
            ielts = 6.5
            ielts_r = 6
            ielts_w = 6
            ielts_s = 6
            ielts_l = 6
        elif 'English Language' in programme_en:
            ielts = 6.5
            ielts_r = 6
            ielts_w = 6
            ielts_s = 6
            ielts_l = 6
        elif 'Linguistics' in programme_en:
            ielts = 6.5
            ielts_r = 6
            ielts_w = 6
            ielts_s = 6
            ielts_l = 6
        elif 'Law' in programme_en:
            ielts = 6.5
            ielts_r = 6
            ielts_w = 6
            ielts_s = 6
            ielts_l = 6
        else:
            ielts = 6
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
        # print(ielts,ielts_l,ielts_s,ielts_w,ielts_r)

        #15.require_chinese_en
        require_chinese_en ='<p>Students must satisfy one of the following criteria: Good grade in the Secondary School Senior plus a 1 year Foundation Programme is required.OR College Graduation Diploma (Dazhuan awarded by university / colleges on completion of 2-3 years of study) OR Graduation Diploma from selected partner institution.A Levels or International Baccalaureate - see course pages for specific entry requirements. Mature students will be considered on a case by case basis.Entry into Year 2 will be considered for students with a HND or at least one year of study at a University overseas or in the UK.</p>'

        #16.career_en
        career_en = response.xpath('//*[@id="employability"]').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        career_en =clear_space_str(career_en)
        # print(career_en)

        #17.tuition_fee_pre
        tuition_fee_pre = '£'

        #18.apply_proces_en
        apply_proces_en = 'https://www.bangor.ac.uk/international/applying/'

        #19.deadline
        deadline = '2018-6-30,2018-10-30'

        #20.location
        location = 'Wales'

        #21.other
        other = 'https://www.bangor.ac.uk/international/future/Finance_and_scholarship.php'
        #22.apply_pre
        apply_pre = '£'

        #23.alevel
        alevel = response.xpath("//*[contains(text(),'2019')]/../following-sibling::ul[1]").extract()
        alevel = ''.join(alevel)
        alevel = remove_class(alevel)
        # print(alevel)

        item['alevel'] = alevel
        item['apply_pre'] = apply_pre
        item['ucascode'] = ucascode
        item['other'] = other
        item['university'] = university
        item['url'] = url
        item['overview_en'] = overview_en
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['modules_en'] = modules_en
        item['ielts'] = ielts
        item['ielts_w'] = ielts_w
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['require_chinese_en'] = require_chinese_en
        item['career_en'] = career_en
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_proces_en'] = apply_proces_en
        item['deadline'] = deadline
        item['location'] = location
        yield item