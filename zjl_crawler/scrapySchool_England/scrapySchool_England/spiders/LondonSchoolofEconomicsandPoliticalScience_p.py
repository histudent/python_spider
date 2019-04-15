# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/2 14:28'
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
    name = 'LondonSchoolofEconomicsandPoliticalScience_p'
    allowed_domains = ['lse.ac.uk/']
    start_urls = []
    C= [
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Accounting-Organisations-and-Institutions?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Accounting-and-Finance?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-African-Development?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Anthropology-and-Development?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Anthropology-and-Development-Management?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Applicable-Mathematics?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Applied-Social-Data-Science?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-China-in-Comparative-Perspective?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-City-Design-and-Social-Science?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Comparative-Politics?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Conflict-Studies?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Criminal-Justice-Policy?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Culture-and-Society?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Data-Science?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Development-Management?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Development-Studies?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Econometrics-and-Mathematical-Economics?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Economic-History?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Economic-History-Research?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Economics?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Economics-two-year-programme?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Economics-and-Management?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Economics-and-Philosophy?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Economy-Risk-and-Society?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Empires-Colonialism-and-Globalisation?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Environment-and-Development?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Environmental-Economics-and-Climate-Change?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Environmental-Policy-and-Regulation?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-EU-Politics?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-European-Studies-Research?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Finance-full-time?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Finance-and-Economics?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Finance-and-Private-Equity?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Financial-Mathematics?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Gender?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Gender-Research?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Gender-Sexuality?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Gender-Development-and-Globalisation?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Gender-Media-and-Culture?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Gender-Policy-and-Inequalities?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Global-Europe-Culture-and-Conflict?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Global-Health?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Global-Politics?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Health-and-International-Development?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-History-of-International-Relations?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Human-Geography-and-Urban-Studies-Research?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Human-Resources-and-Organisations?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Human-Rights?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Inequalities-and-Social-Science?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-International-Development-and-Humanitarian-Emergencies?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-International-Health-Policy?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-International-Health-Policy-Health-Economics?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-International-Migration-and-Public-Policy?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-International-Political-Economy?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-International-Political-Economy-Research?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-International-Relations?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-International-Relations-Research?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-International-Relations-Theory?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-International-Social-and-Public-Policy?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/LLM?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Law-and-Accounting?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Local-Economic-Development?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/Masters-in-Management?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/Global-Masters-Management?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Management-and-Strategy?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Management-Information-Systems-and-Digital-Innovation?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Marketing?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Media-and-Communications?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Media-and-Communications-Data-and-Society?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Media-and-Communications-Media-and-Communication-Governance?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Media-And-Communications-Research?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Media-Communication-and-Development?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Operations-Research-and-Analytics?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Organisational-and-Social-Psychology?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Philosophy-and-Public-Policy?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Philosophy-of-Science?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Philosophy-of-the-Social-Sciences?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Political-Economy-of-Europe?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Political-Economy-of-Late-Development?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Political-Science-and-Political-Economy?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Political-Sociology?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Political-Theory?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Politics-and-Communication?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Psychology-of-Economic-Life?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MA-Global-Studies-A-European-Perspective?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Public-Policy-and-Administration?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/LSE-PKU-Double-MSc-Degree-in-International-Affairs?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Quantitative-Economic-History?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Global-Media-and-Communications-LSE-and-Fudan?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Real-Estate-Economics-and-Finance?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Global-Media-and-Communications-LSE-and-UCT?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Regulation?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Global-Population-Health?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Risk-and-Finance?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Global-Media-and-Communications-LSE-and-USC?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Social-and-Cultural-Psychology?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Health-Policy-Planning-and-Financing?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Social-and-Public-Communication?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Social-Anthropology?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Social-Anthropology-Learning-and-Cognition',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Social-Anthropology-Religion-in-the-Contemporary-World?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Social-Innovation-and-Entrepreneurship?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Social-Policy-Research?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Social-Research-Methods?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Sociology?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Statistics?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Statistics-Research?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Statistics-Financial-Statistics?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Statistics-Financial-Statistics-Research?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Statistics-Social-Statistics?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Statistics-Social-Statistics-Research?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Strategic-Communications?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Theory-and-History-of-International-Relations?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Urbanisation-and-Development?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Women-Peace-and-Security?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/Master-of-Public-Administration?from_serp=1',
        'http://www.lse.ac.uk/study-at-lse/Graduate/Degree-programmes-2018/MSc-Regional-And-Urban-Planning-Studies?from_serp=1'
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

        #3.teach_type
        if '2018/VRS' in url:
            teach_type = 'research'
        elif '2018/MResPhD' in url:
            teach_type = 'research'
        elif '2018/MPhilPhD' in url:
            teach_type = 'research'
        else:
            teach_type = 'taught'
        # print(teach_type)

        #4.programme_en
        programme_en = response.xpath('//*[@id="form1"]/header[2]/div/div[2]/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #5.degree_type
        degree_type = 2

        #6.degree_name
        if 'MSc' in programme_en:
            degree_name = 'MSc'
        elif 'LSE' in programme_en:
            degree_name = 'LSE'
        elif 'MPA' in programme_en:
            degree_name = 'MPA'
        elif 'LLM' in programme_en:
            degree_name = 'LLM'
        elif 'Diploma' in programme_en:
            degree_name = 'Diploma'
        elif 'MA' in programme_en:
            degree_name = 'MA'
        elif 'MPhil/PhD' in programme_en:
            degree_name = 'MPhil/PhD'
        elif 'MRes/PhD' in programme_en:
            degree_name = 'MRes/PhD'
        elif 'Visiting Research' in programme_en:
            degree_name = 'Visiting Research'
        else:
            degree_name = 'N/A'
        # print(degree_name)
        programme_en = programme_en.replace(degree_name,'').strip().replace('-','')
        # print(programme_en)

        #7.department
        department = response.xpath('//*[@id="form1"]/div[4]/div/div[1]/div/ul/li[2]').extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #8.overview_en
        overview_en =response.xpath('//*[@id="form1"]/div[3]/div/div[2]/div/p|//*[@id="form1"]/div[4]/div/div[2]/div/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #9.start_date
        start_date = response.xpath("//*[contains(text(),'Start date')]//following-sibling::*").extract()
        start_date = ''.join(start_date)
        start_date =remove_tags(start_date)
        try:
            start_date = tracslateDate(start_date)[0]
            if 'Introductory' in start_date:
                start_date = '2018-9'
            elif 'Early' in start_date:
                start_date = '2018-9'
            elif 'First' in start_date:
                start_date ='2018-9'
            elif 'Mandatory' in start_date:
                start_date ='2018-9'
            elif 'Suspended' in start_date:
                start_date = '2018-9'
            elif 'Late' in start_date:
                start_date = '2018-9'
            elif 'Intake' in start_date:
                start_date = '2018-9'
            else:start_date = start_date
        except:
            start_date = 'N/A'
        # print(start_date)

        #10.deadline
        deadline = response.xpath("//*[contains(text(),'Application deadline')]//following-sibling::*").extract()
        deadline = ''.join(deadline)
        deadline = remove_tags(deadline)
        deadline = tracslateDate(deadline)
        deadline = ''.join(deadline)
        deadline = deadline.replace('None','').replace('However','').replace('Apply','').replace('Sciences','')
        # print(deadline)

        #11.duration
        duration_list= response.xpath("//*[contains(text(),'Duration')]//following-sibling::*").extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        # print(duration_list)
        if 'Nine months' in duration_list:
            duration = 9
            duration_per = 3
        elif 'Ten months' in duration_list:
            duration = 10
            duration_per = 3
        elif 'months' in duration_list:
            duration = re.findall('\d+',duration_list)[0]
            # print(duration)
            duration_per = 3
        elif 'Three-four years' in duration_list:
            duration = 3
            duration_per = 1
        elif 'Three to four years' in duration_list:
            duration = 3
            duration_per = 1
        elif 'Four to five' in duration_list:
            duration = 4
            duration_per = 1
        elif 'Five years' in duration_list:
            duration = 5
            duration_per = 1
        elif '3 to 4 years' in duration_list:
            duration = 3
            duration_per =1
        elif 'Six years' in duration_list:
            duration = 6
            duration_per = 1
        else:
            duration = 1
            duration_per =1
        # print(duration,'********************',duration_per)

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

        #14.rntry_requirements
        rntry_requirements = response.xpath("//*[contains(text(),'Minimum entry requirement')]//following-sibling::*[1]").extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        rntry_requirements = clear_space_str(rntry_requirements)
        # print(rntry_requirements)

        #15.modules_en
        modules_en = response.xpath("//*[contains(text(),'Programme structure and courses')]/../../following-sibling::*").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        modules_en = clear_space_str(modules_en)
        # print(modules_en)

        #16.assessment_en
        assessment_en = response.xpath("//h3[contains(text(),'ssessment')]//following-sibling::*").extract()
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
        if 'MPhil' in programme_en:
            ielts = 7.0
            ielts_r = 6.5
            ielts_l = 6.5
            ielts_w = 7.0
            ielts_s = 6.5
        elif 'LLM' in programme_en:
            ielts = 7.5
            ielts_r = 6.5
            ielts_l = 7.0
            ielts_w = 7.0
            ielts_s = 6.5
        else:
            ielts = 7.0
            ielts_r = 6.5
            ielts_l = 6.5
            ielts_w = 6.0
            ielts_s = 6.0

        #23.require_chinese_en
        require_chinese_en = "<p>Graduate entry requirements for applicants from China Taught master's programmes (MSc/MA/MPA/LLM)To be considered for admission to a taught master's programme, we would normally require a bachelor's degree with an overall mark of 85 per cent from applicants who have attended a highly regarded institution in China, with all other applicants we would normally require a mark of at least 90 per cent.Research programmes (MPhil/MRes/PhD)To be considered for admission to a research programme, we would normally require a master's degree with an overall mark of 85 per cent/B from applicants who have attended a highly regarded institution, while all other applicants are normally required to obtain a mark of 90 per cent/A.</p>"

        #24.apply_proces_en
        apply_proces_en = 'http://www.lse.ac.uk/study-at-lse/Graduate/Prospective-students/How-to-Apply'

        #25.teach_time
        teach_time = 'Full time'

        #26.tuition_fee_pre
        tuition_fee_pre = '£'
        #27.toefl 28293031
        if 'MPhil' in programme_en:
            toefl = 100
            toefl_r = 23
            toefl_l = 22
            toefl_w = 27
            toefl_s = 22
        elif 'LLM' in programme_en:
            toefl = 109
            toefl_r = 23
            toefl_l = 24
            toefl_w = 27
            toefl_s = 22
        else:
            toefl = 100
            toefl_r = 23
            toefl_l = 22
            toefl_w = 24
            toefl_s = 22
        #32.apply_pre
        apply_pre = '£'
        #33.apply_documents_en
        apply_documents_en = '<p>We welcome applications from all suitably qualified prospective students and want to recruit students with the very best academic merit, potential and motivation, irrespective of their background. We carefully consider each application on an individual basis, taking into account all the information presented on your application form, including your: academic achievement (including predicted and achieved grades) personal statement two references CV</p>'
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['toefl_l'] = toefl_l
        item['toefl_s'] = toefl_s
        item['apply_pre'] = apply_pre
        item['apply_documents_en'] = apply_documents_en
        item['university'] = university
        item['url'] = url
        item['teach_type'] = teach_type
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
        item['rntry_requirements'] = rntry_requirements
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
        item['teach_time'] = teach_time
        item['tuition_fee_pre'] = tuition_fee_pre
        yield item