# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/24 14:54'
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
class LondonSchoolofEconomicsandPoliticalScienceSpider(scrapy.Spider):
    name = 'LondonSchoolofEconomicsandPoliticalScience_u'
    allowed_domains = ['lse.ac.uk/']
    start_urls = []
    C= [
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BA-Anthropology-and-Law/Home.aspx?from_serp=1'
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BA-Geography/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BA-History/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BA-Social-Anthropology/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Accounting-and-Finance/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Actuarial-Science/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Criminology/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Econometrics-and-Mathematical-Economics/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Economic-History/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Economic-History-and-Geography/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Economic-History-with-Economics/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Economics/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Economics-and-Economic-History/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Economics-with-Economic-History/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Environment-and-Development/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Environmental-Policy-with-Economics/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Finance/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Financial-Mathematics-and-Statistics/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Geography-with-Economics/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-International-Relations/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-International-Relations-and-Chinese/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-International-Relations-and-History/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-International-Social-and-Public-Policy/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-International-Social-and-Public-Policy-and-Economics/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-International-Social-and-Public-Policy-with-Politics/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Language-Culture-and-Society/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Management/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Mathematics-and-Economics/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Mathematics-with-Economics/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Mathematics-Statistics-and-Business/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Philosophy-and-Economics/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Philosophy-Logic-and-Scientific-Method/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Philosophy-Politics-and-Economics/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Politics/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Politics-and-Economics/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Politics-and-History/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Politics-and-International-Relations/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Politics-and-Philosophy/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Psychological-and-Behavioural-Science/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Social-Anthropology/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/BSc-Sociology/Home.aspx?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Undergraduate/Degree-programmes-2019/LLB-Bachelor-of-Laws/Home.aspx?from_serp=1'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'London School of Economics and Political Science'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.ucascode
        ucascode = response.xpath("//*[contains(text(),'UCAS code')]/.").extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode).replace('UCAS code ','')
        # print(ucascode)

        #4.programme_en
        programme_en_a = response.xpath('//*[@id="form1"]/header[2]/div/div[2]/h1').extract()
        programme_en_a = ''.join(programme_en_a)
        programme_en_a = remove_tags(programme_en_a)
        # print(programme_en_a)
        programme_en = programme_en_a.split()[1:]
        programme_en = ' '.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #5.degree_type
        degree_type = 1

        #6.degree_name
        degree_name = programme_en_a.split()[0]
        # print(degree_name)

        #7.department
        department = response.xpath('//*[@id="form1"]/div[4]/div/div[1]/div/ul/li[2]').extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #8.overview_en
        overview_en =response.xpath('//*[@id="form1"]/div[3]/div/div[2]/div/p[1]|//*[@id="form1"]/div[4]/div/div[2]/div/p[1]').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)
        # if len(overview_en)==0:
        #     print(response.url)

        #9.start_date
        start_date = '2019-9-30'


        #10.deadline
        deadline = '2019-1-15'

        #11.duration
        duration_list= response.xpath("//*[contains(text(),'Duration')]//following-sibling::*").extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        if 'Three' in duration_list:
            duration = 3
            duration_per = 1
        else :
            duration = 4
            duration_per =1

        #12.tuition_fee
        tuition_fee= response.xpath("//*[contains(text(),'Tuition fee')]//following-sibling::*[1]").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #13.location
        location = response.xpath("//*[contains(text(),'Location')]//following-sibling::*[1]").extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #14.alevel  #34.ib
        alevel_a = response.xpath("//*[contains(text(),'Usual standard offer')]//following-sibling::*[1]").extract()
        alevel_a  = ''.join(alevel_a)
        alevel_a  = remove_tags(alevel_a)
        alevel = re.findall(r'(.*)International',alevel_a)[0]
        ib = re.findall(r'(International.*)',alevel_a)[0]
        # print(alevel)
        # print(ib)

        #15.modules_en
        modules_en = response.xpath("//*[contains(text(),'Programme structure and courses')]/../../following-sibling::*").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        modules_en = clear_space_str(modules_en)
        # print(modules_en)

        #16.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'Assessment')]/../following-sibling::*").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        assessment_en = clear_space_str(assessment_en)
        # print(assessment_en)

        #17.career_en
        career_en = response.xpath("//*[contains(text(),'Support for your career')]//preceding-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = clear_space_str(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #18.ielts,19.20.21.22

        ielts = 7.0
        ielts_r = 7.0
        ielts_l = 7.0
        ielts_w = 7.0
        ielts_s = 7.0


        #23.require_chinese_en
        require_chinese_en = "<p>We welcome applications from all suitably qualified prospective students and want to recruit students with the very best academic merit, potential and motivation, irrespective of their background. We carefully consider each application on an individual basis, taking into account all the information presented on the UCAS application form, including your:academic achievement (including predicted and achieved grades) subject combinations personal statement teacher’s reference educational circumstances In terms of academic achievement, our entry requirements vary by programme, and are listed on the individual undergraduate degree programme webpagesOn these pages and in our printed prospectus, we list our entry requirements and usual standard offers for each programme for those students applying with GCE A levels and the International Baccalaureate Diploma Programme (IB). However we also consider applications from students with a range of other UK qualifications including BTECs, Foundation Courses and Access to HE Diplomas (see further information on these qualifications) as well as a wide range of international qualifications. Below you will find the equivalency of the qualification/s from your country to GCE A levels. If your qualification is not listed, please get in touch with Undergraduate Admissions.For more information on the application process please see How to apply.You may also have to provide evidence of your evidence of your English language proficiency, although you don't need to provide this at the time you submit your application. Competition for places Competition for places at the School is high. This means that even if you are predicted or if you achieve the grades that meet our usual standard offer, this will not guarantee you an offer of admission. Usual standard offers are intended only as a guide, and in some cases applicants will be asked for grades which differ from this.Chinese senior high school diploma The senior high school diploma is not acceptable as an entry qualification to LSE.Please view information on other accepted international qualifications for alternative options. In terms of academic achievement, our entry requirements vary by programme, and are listed on the individual undergraduate degree programme webpages.</p>"

        #24.apply_proces_en
        apply_proces_en = 'http://www.lse.ac.uk/study-at-lse/Undergraduate/Prospective-Students/How-to-Apply'


        #26.tuition_fee_pre
        tuition_fee_pre = '£'
        #27.toefl 28293031
        toefl = 107
        toefl_r = 25
        toefl_l = 25
        toefl_w = 25
        toefl_s = 25
        #32.apply_pre
        apply_pre = '£'
        #33.apply_documents_en
        apply_documents_en = '<p>We welcome applications from all suitably qualified prospective students and want to recruit students with the very best academic merit, potential and motivation, irrespective of their background. We carefully consider each application on an individual basis, taking into account all the information presented on your application form, including your: academic achievement (including predicted and achieved grades) personal statement two references CV</p>'


        item['ib'] = ib
        item['alevel'] = alevel
        item['ucascode'] = ucascode
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['toefl_l'] = toefl_l
        item['toefl_s'] = toefl_s
        item['apply_pre'] = apply_pre
        item['apply_documents_en'] = apply_documents_en
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['department'] = department
        item['overview_en'] = overview_en
        item['start_date'] = start_date
        item['deadline'] = deadline
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['tuition_fee'] = tuition_fee
        item['location'] = location
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['require_chinese_en'] = require_chinese_en
        item['apply_proces_en'] = apply_proces_en
        item['tuition_fee_pre'] = tuition_fee_pre
        yield item