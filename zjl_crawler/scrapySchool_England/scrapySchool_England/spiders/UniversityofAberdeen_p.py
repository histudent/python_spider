# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/4 9:44'
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
from scrapySchool_England.TranslateMonth import  translate_month
class UniversityofAberdeenSpider(scrapy.Spider):
    name = 'UniversityofAberdeen_p'
    allowed_domains = ['abdn.ac.uk/']
    start_urls = []
    C = [
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/3/analytical-chemistry/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1120/advanced-chemical-engineering/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1/accounting-and-finance/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/17/archaeology/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1126/advanced-structural-engineering/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/15/applied-marine-and-fisheries-ecology/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1037/advanced-mechanical-engineering/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/22/archaeology-of-the-north/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/921/art-and-business/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1034/artificial-intelligence/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1036/msc-biotechnology-bioinformatics-and-bio-business/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/32/business-research/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/37/clinical-pharmacology/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1156/cardiovascular-science-and-diabetes/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1128/business-law-and-sustainable-development-with-dissertation/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/87/comparative-european-societies/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/43/criminal-justice-and-human-rights/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/924/cultural-and-creative-communication/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1142/divinity/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1015/decommissioning/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/40/criminal-justice/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/54/drug-discovery/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/39/creative-writing/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/55/drug-discovery-and-development/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/925/ecology-and-conservation/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/928/energy-and-environmental-law-with-professional-skills/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/931/energy-law-with-professional-skills/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/926/energy-and-environmental-law-with-dissertation/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/947/environmental-and-forest-management/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1021/environmental-and-ecological-sciences/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1022/environmental-management/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/75/english-literary-studies/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/929/energy-law-with-dissertation/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/72/energy-politics-and-law/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/84/environmental-science/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/332/film-and-visual-culture/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/82/environmental-partnership-management/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/89/finance-and-investment-management-includes-level-1-cfa-examination/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/979/finance-and-real-estate-does-not-include-cfa-examination/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/93/finance-and-real-estate-includes-level-1-cfa-examination/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1023/environmental-pollution-and-remediation/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1099/foundations-of-clinical-psychology/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/86/ethnology-and-folklore/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/98/genetics/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/90/finance-and-investment-management-does-not-include-level-1-cfa-examination/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/99/geographical-information-systems/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/106/global-conflict-and-peace-processes/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/107/global-health-and-management/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/97/general-law/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1070/global-subsea-engineering/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/102/geophysics/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/112/health-psychology/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/118/human-nutrition/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/110/globalization/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/122/human-rights/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/920/financial-mathematics/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/127/immunology/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/918/intellectual-property-law/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/124/human-rights-and-criminal-justice/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1161/industrial-biotechnology/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/133/information-technology/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1044/international-business-and-finance/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/141/international-business-management/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/138/integrated-petroleum-geoscience/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/148/international-commercial-law-with-professional-skills/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1134/intellectual-property-law-with-professional-skills/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1136/msc-international-finance-with-cfa/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/150/international-law/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/156/international-relations-and-international-law/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/155/international-relations/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/153/international-law-and-strategic-studies/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1110/international-trade-law/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/146/international-commercial-law-with-dissertation/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/917/international-political-economy/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/286/rural-surveying-and-rural-property-management/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/152/international-law-and-international-relations/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1131/msc-leadership-corporate-responsibility-and-sustainability/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1024/marine-conservation/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1056/international-trade-law-with-dissertation-in-treaty-negotiation-online-distance-learning/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/173/marketing-management/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1107/international-finance/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/909/master-of-public-health/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1122/law-and-economics-of-oil-and-gas/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/31/mba-aberdeen/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/69/energy-management/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/178/medical-imaging/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/180/medical-physics/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1151/medical-sciences/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1130/mba-finance/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/183/medieval-and-early-modern-studies/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/184/microbiology/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1148/molecular-medicine/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/199/museum-studies/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1143/offshore-engineering/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/200/music/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/212/oil-and-gas-enterprise-management/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/196/modern-history/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/206/oil-and-gas-chemistry/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/218/oil-and-gas-law-with-professional-skills/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/221/people-and-the-environment/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1009/petroleum-data-management/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/222/petroleum-engineering/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/214/oil-and-gas-law-with-dissertation/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/243/political-research/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/244/post-conflict-justice-and-peacebuilding/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/228/petroleum-energy-economics-and-finance/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1118/msc-monitoring-and-evaluation-for-policy-impact/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/249/process-safety/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/242/physician-associate-studies/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/252/professional-communication/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/264/psychology/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/266/public-international-law/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/272/real-estate-international-option/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/247/private-international-law/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1112/osteoarchaeology/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/278/renewable-energy-engineering/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/980/real-estate-commercial-option/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/261/psychological-studies/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/283/reservoir-engineering/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/935/safety-and-reliability-engineering/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/288/safety-and-reliability-engineering-for-oil-and-gas/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/276/religion-and-society/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/290/scandinavian-studies-viking-and-medieval-studies/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/1152/reproductive-and-developmental-biology/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/293/social-anthropology/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/298/social-research/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/300/sociology/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/304/soil-science/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/291/sex-gender-violence/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/292/social-and-educational-research/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/305/sonic-arts/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/309/strategic-studies/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/317/subsea-engineering/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/313/strategic-studies-and-international-law/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/321/tesol/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/314/strategic-studies-and-management/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/329/translation-studies/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/971/stratified-medicine-and-pharmacological-innovation/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/188/transnational-cultures/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/932/strategic-studies-and-energy-security/',
        'https://www.abdn.ac.uk/study/postgraduate-taught/degree-programmes/333/vocal-music/'
    ]
    for i in C:
        start_urls.append(i)

    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Aberdeen'
        # print(university)

        #2.url
        url = response.url

        #3.programme_en
        programme_en = response.xpath('//*[@id="top"]/div[3]/div/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        if ',' in programme_en:
            programme_en = re.findall('(.*?),',programme_en)[0]
        else:
            programme_en = programme_en
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.overview_en
        overview_en = response.xpath('//*[@id="overview"]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #6.degree_name
        degree_name_list = response.xpath('//*[@id="programme_overview"]/div[2]/div[2]/div/dl/dd[2]/abbr').extract()
        degree_name_list= ''.join(degree_name_list)
        degree_name_list = remove_tags(degree_name_list)
        if len(degree_name_list) ==0:
            degree_name = response.xpath('//*[@id="programme_overview"]/div[2]/div[2]/div/dl/dd').extract()
            degree_name = ''.join(degree_name)
            degree_name = remove_tags(degree_name)
            degree_name = clear_space_str(degree_name)
        else:
            degree_name = degree_name_list
        # print(degree_name)

        #7.teach_type
        if len(degree_name_list)==0:
            teach_type = 'Research'
        else:
            teach_type = 'Taught'
        # print(teach_type)

        #8.duration
        duration = response.xpath('//*[@id="programme_overview"]/div[2]/div[2]/div/dl/dd[3]').extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        duration = clear_space_str(duration)
        # print(duration)
        try:
            duration = re.findall('\d+',duration)[0]
        except:
            duration = None
        # print(duration)

        #9.duration_per
        duration_per = 3

        #10.teach_time
        teach_time = response.xpath('//*[@id="programme_overview"]/div[2]/div[2]/div/dl/dd[4]').extract()
        teach_time = ''.join(teach_time)
        teach_time = remove_tags(teach_time)
        teach_time = clear_space_str(teach_time)
        if teach_time == 'Full Time or Part Time':
            teach_time ='Full Time'
        else:
            pass
        # print(teach_time)

        #11.start_date
        start_date = response.xpath('//*[@id="programme_overview"]/div[2]/div[2]/div/dl/dd[5]').extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        start_date = clear_space_str(start_date)
        # print(start_date)
        if start_date =='September or January':
            start_date = '2018-9,2019-1'
        elif start_date =='September, January or June':
            start_date = '2018-9,2019-1,2019-6'
        elif start_date =='July, October, January or March':
            start_date = '2018-7,2018-10,2019-1,2019-3'
        elif start_date =='January':
            start_date = '2019-1'
        else:
            start_date = '2018-9'
        # print(start_date)

        #12.modules_en
        modules_en = response.xpath('//*[@id="what_you_study"]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)

        # print(modules_en)

        #13.assessment_en
        assessment_en =response.xpath("//*[contains(text(),'Assessment Methods')]//following-sibling::*").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        assessment_en = clear_space_str(assessment_en)
        # print(assessment_en)

        #14.rntry_requirements
        rntry_requirements =response.xpath("//*[contains(text(),'Qualifications')]//following-sibling::p").extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        rntry_requirements =clear_space_str(rntry_requirements)
        if len(rntry_requirements) ==0:
            rntry_requirements = response.xpath("//*[contains(text(),'Entry Requirements')]//following-sibling::div").extract()
            rntry_requirements = ''.join(rntry_requirements)
            rntry_requirements = remove_class(rntry_requirements)
            rntry_requirements =clear_space_str(rntry_requirements)
        else:
            pass
        # print(rntry_requirements)

        #15.require_chinese_en
        require_chinese_en = '<p>The entry requirements for postgraduate taught programmes is 75% from any Chinese institution.</p>'

        #16.ielts 17.18.19.20
        ielts = response.xpath("//*[contains(text(),'IELTS Academic:')]/../following-sibling::*[1]").extract()
        ielts = ''.join(ielts)
        ielts = remove_tags(ielts)
        ielts =clear_space_str(ielts)
        if len(ielts) != 0:
            a = re.findall('\d\.\d',ielts)[0]
            b = re.findall('\d\.\d',ielts)[1]
            c = re.findall('\d\.\d', ielts)[2]
            d = re.findall('\d\.\d', ielts)[3]
            e = re.findall('\d\.\d', ielts)[4]
            ielts = a
            ielts_l = b
            ielts_r = c
            ielts_s = d
            ielts_w = e
        else:
            ielts = 6.5
            ielts_w = 6.0
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        # print(ielts,ielts_w,ielts_r,ielts_l,ielts_s)

        #21.toefl 22.23.24.25
        toefl = response.xpath("//*[contains(text(),'TOEFL iBT:')]/../following-sibling::*[1]").extract()
        toefl = ''.join(toefl)
        toefl = remove_tags(toefl)
        toefl = clear_space_str(toefl)
        if len(toefl) !=0:
            a = re.findall('\d+', toefl)[0]
            b = re.findall('\d+', toefl)[1]
            c = re.findall('\d+', toefl)[2]
            d = re.findall('\d+', toefl)[3]
            e = re.findall('\d+', toefl)[4]
            toefl = a
            toefl_l = b
            toefl_r = c
            toefl_s = d
            toefl_w = e
        else:
            toefl = 90
            toefl_l = 17
            toefl_r = 18
            toefl_s = 20
            toefl_w = 21
        # print(toefl,toefl_l,toefl_r,toefl_w,toefl_s)

        #26.career_en
        career_en = response.xpath('//*[@id="careers"]/*').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        career_en = clear_space_str(career_en)
        # print(career_en)

        #27.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'                               International Students                                ')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = clear_space_str(tuition_fee)
        tuition_fee = remove_class(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #28.tuition_fee_pre
        tuition_fee_pre = '£'

        #29.apply_proces_en
        apply_proces_en = 'https://www.abdn.ac.uk/study/enquire.php'

        #30.location
        location = 'Aberdeen'
        #31.apply_pre
        apply_pre = '£'

        #32.apply_documents_en
        apply_documents_en = '<p>In order to submit the completed application, you must upload the following documents: Your final, official academic transcript/s (if you have not completed your studies yet, please upload a copy of your transcript of studies to date) with an official English translation (if the original language is not English).   A personal statement. We suggest that you prepare the personal statement before you start the online application. The personal statement should be between 250 to 500 words in total and should answer the following three questions: Why have you chosen to apply to the University of Aberdeen to study this subject? Which personal qualities do you possess that will help you to successfully complete this programme of study? How will studying this programme help you when you return home and in your future career? Other documents that may be required but which can be uploaded later include: Degree Certificate For international applicants, document/s to demonstrate your proficiency in English - refer to our English Language requirements page for further information Academic References For Research programmes (PhD) two confidential references. You can uploaded these to your applicant portal or, your referee can send them by e-mail to pgadmissions@abdn.ac.uk. Please ask your referee to include your full name, date of birth, and Applicant Personal ID For Taught programmes (MBA, MSc, MLitt, MRes etc), if you have a first degree from an institution outside the UK, a small number of our degrees may require you to provide one reference. Please refer to the individual programme web page for more details. You can search our degrees here  A Research Proposal should usually be uploaded with applications for PhD and Masters by Research programmes. Some programmes or disciplines require an extended Research Profile, and applicants should refer to individual school websites for details before submitting an application</p>'

        # item['apply_documents_en'] =apply_documents_en
        # item['apply_pre'] = apply_pre
        # item['location'] = location
        item['university'] = university
        item['url'] = url
        # item['programme_en'] = programme_en
        # item['degree_type'] = degree_type
        # item['overview_en'] = overview_en
        # item['degree_name'] = degree_name
        # item['teach_type'] = teach_type
        # item['duration'] = duration
        # item['duration_per'] = duration_per
        # item['teach_time'] = teach_time
        # item['start_date'] = start_date
        item['modules_en'] = modules_en
        # item['assessment_en'] = assessment_en
        # item['rntry_requirements'] = rntry_requirements
        # item['require_chinese_en'] = require_chinese_en
        # item['ielts'] = ielts
        # item['ielts_r'] = ielts_r
        # item['ielts_w'] = ielts_w
        # item['ielts_s'] = ielts_s
        # item['ielts_l'] = ielts_l
        # item['toefl'] = toefl
        # item['toefl_r'] = toefl_r
        # item['toefl_w'] = toefl_w
        # item['toefl_s'] = toefl_s
        # item['toefl_l'] = toefl_l
        # item['career_en'] = career_en
        # item['tuition_fee'] = tuition_fee
        # item['tuition_fee_pre'] = tuition_fee_pre
        # item['apply_proces_en'] = apply_proces_en
        yield  item