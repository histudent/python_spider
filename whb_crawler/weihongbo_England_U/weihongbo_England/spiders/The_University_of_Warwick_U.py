import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'The_University_of_Warwick_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []


    C= ['https://warwick.ac.uk/study/undergraduate/courses-2019/accountingandfinance',
'https://warwick.ac.uk/study/undergraduate/courses-2019/accountingandfinancefoundation',
'https://warwick.ac.uk/study/undergraduate/courses-2019/ancienthistoryandclassicalarchaeology',
'https://warwick.ac.uk/study/undergraduate/courses-2019/ancienthistoryandclassicalarchaeologysie',
'https://warwick.ac.uk/study/undergraduate/courses-2019/automotiveengineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/automotiveengineeringmeng',
'http://www2.warwick.ac.uk/study/undergraduate/courses-2019/biochemistry',
'http://www2.warwick.ac.uk/study/undergraduate/courses-2019/biochemistrymbio',
'http://www2.warwick.ac.uk/study/undergraduate/courses-2019/biosciences',
'http://www2.warwick.ac.uk/study/undergraduate/courses-2019/biosciencesmbio',
'http://www2.warwick.ac.uk/study/undergraduate/courses-2019/biomedicalscience',
'http://www2.warwick.ac.uk/study/undergraduate/courses-2019/biomedicalsciencembio',
'https://warwick.ac.uk/study/undergraduate/courses-2019/biomedicalsystemsengineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/biomedicalsystemsengineeringmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/management',
'https://warwick.ac.uk/study/undergraduate/courses-2019/managementfoundation',
'https://warwick.ac.uk/study/undergraduate/courses-2019/internationalbusinesswithfrench',
'https://warwick.ac.uk/study/undergraduate/courses-2019/chemistry',
'https://warwick.ac.uk/study/undergraduate/courses-2019/chemistrymchem',
'https://warwick.ac.uk/study/undergraduate/courses-2019/chemindustrialmchem',
'https://warwick.ac.uk/study/undergraduate/courses-2019/cheminternationalmchem',
'https://warwick.ac.uk/study/undergraduate/courses-2019/chemmedicinalchem',
'https://warwick.ac.uk/study/undergraduate/courses-2019/chemmedicinalmchem',
'https://warwick.ac.uk/study/undergraduate/courses-2019/civilengineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/civilengineeringmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/classicalcivilisation',
'https://warwick.ac.uk/study/undergraduate/courses-2019/classicalcivilisationSIE',
'https://warwick.ac.uk/study/undergraduate/courses-2019/classics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/classicsandenglish',
'https://warwick.ac.uk/study/undergraduate/courses-2019/classicsancientgreek',
'https://warwick.ac.uk/study/undergraduate/courses-2019/classicslatin',
'https://warwick.ac.uk/study/undergraduate/courses-2019/computersciencebusiness',
'https://warwick.ac.uk/study/undergraduate/courses-2019/computerscience',
'https://warwick.ac.uk/study/undergraduate/courses-2019/computersciencemeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/compsyseng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/compsysengmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/cybersecurity',
'https://warwick.ac.uk/study/undergraduate/courses-2019/datascience',
'https://warwick.ac.uk/study/undergraduate/courses-2019/discretemaths',
'https://warwick.ac.uk/study/undergraduate/courses-2019/discretemathsmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/economics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/economicsgsd',
'https://warwick.ac.uk/study/undergraduate/courses-2019/economicsindustrialorg',
'https://warwick.ac.uk/study/undergraduate/courses-2019/economicspoliticsinternational',
'https://warwick.ac.uk/study/undergraduate/courses-2019/educationstudies',
'https://warwick.ac.uk/study/undergraduate/courses-2019/electricalandelectronicengineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/electricalandelectronicengineeringmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/electronicengineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/electronicengineeringmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/engineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/engineeringmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/engineeringbusinessmanagement',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishandfrench',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishandgerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishandhispanicstudies',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishhistory',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishanditalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishlanguagelinguistics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishlit',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishlitcreativewriting',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishtheatre',
'https://warwick.ac.uk/study/undergraduate/courses-2019/filmandliterature',
'https://warwick.ac.uk/study/undergraduate/courses-2019/filmstudies',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frencheconomics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchandgerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchandhistory',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchanditalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchandlinguistics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchandtheatre',
'https://warwick.ac.uk/study/undergraduate/courses-2019/french',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwitharabic',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwithchinese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwithfilm',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwithgerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwithitalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwithjapanese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwithportuguese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwithrussian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwithspanish',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanandbusiness',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanandeconomics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanandhistory',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germananditalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanandlinguistics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanandtheatre',
'https://warwick.ac.uk/study/undergraduate/courses-2019/german',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwitharabic',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwithchinese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwithfilm',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwithfrench',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwithitalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwithjapanese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwithPORTUGUESE',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwithrussian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwithspanish',
'https://warwick.ac.uk/study/undergraduate/courses-2019/gsd',
'https://warwick.ac.uk/study/undergraduate/courses-2019/gsdbusiness',
'http://www2.warwick.ac.uk/study/cll/courses/undergraduate/parttime/healthsocialpolicy/',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudiesandeconomics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudiesandfrench',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudiesandgerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudiesandhistory',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudiesanditalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudiesandlinguistics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudiesandtheatre',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswitharabic',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswithchinese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswithfilmstudies',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswithfrench',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswithgerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswithitalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswithjapanese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswithportuguese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswithrussian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/historyba',
'https://warwick.ac.uk/study/undergraduate/courses-2019/historyanditalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/historygsd',
'https://warwick.ac.uk/study/undergraduate/courses-2019/historyandphilosophy',
'https://warwick.ac.uk/study/undergraduate/courses-2019/historyandpoliticsba',
'https://warwick.ac.uk/study/undergraduate/courses-2019/historyandsociology',
'http://www2.warwick.ac.uk/study/undergraduate/courses-2019/historyofart',
'https://warwick.ac.uk/study/undergraduate/courses-2019/historyofartitalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/internationalbusinesswithgerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/internationalbusinesswithitalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/internationalbusinesswithspanish',
'https://warwick.ac.uk/study/undergraduate/courses-2019/internationalmanagement',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianandclassics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianandeconomics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianhistoryofart',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianandlinguistics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italiantheatre',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianstudies',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianarabic',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianchinese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianfilmstudies',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianfrench',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italiangerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianjapanese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianportuguese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianrussian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianspanish',
'https://warwick.ac.uk/study/undergraduate/courses-2019/languageculturecommunication',
'https://warwick.ac.uk/study/undergraduate/courses-2019/law',
'https://warwick.ac.uk/study/undergraduate/courses-2019/law4years',
'https://warwick.ac.uk/study/undergraduate/courses-2019/lawstudyabroadenglish',
'https://warwick.ac.uk/study/undergraduate/courses-2019/lawwithfrenchlaw',
'https://warwick.ac.uk/study/undergraduate/courses-2019/lawwithgermanlaw',
'https://warwick.ac.uk/study/undergraduate/courses-2019/lawbusinessstudies',
'https://warwick.ac.uk/study/undergraduate/courses-2019/lawandsociology',
'https://warwick.ac.uk/study/undergraduate/courses-2019/lawwithhumanities',
'https://warwick.ac.uk/study/undergraduate/courses-2019/lawwithsocialsciences',
'https://warwick.ac.uk/study/undergraduate/courses-2019/liberalarts',
'https://warwick.ac.uk/study/undergraduate/courses-2019/lifesciencesgsd',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswitharabic',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswithchinese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswithfrench',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswithgerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswithitalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswithjapanese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswithportuguese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswithrussian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswithspanish',
'https://warwick.ac.uk/study/undergraduate/courses-2019/manufacturingandmechanicalengineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/manufacturingandmechanicalengineeringmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mathsbsc',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mathematicsmmath',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mathematicsandphilosophy',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mathsphysicsbsc',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mmathsphysics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mathsstatsbsc',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mmathstat',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mechanicalengineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mechanicalengineeringmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/modernlang',
'https://warwick.ac.uk/study/undergraduate/courses-2019/modernlanguagesandeconomics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/modernlanguagesandlinguistics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/modernlanguageswithlinguistics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mmorse',
'https://warwick.ac.uk/study/undergraduate/courses-2019/morse',
'https://warwick.ac.uk/study/undergraduate/courses-2019/philosophy',
'https://warwick.ac.uk/study/undergraduate/courses-2019/philosophygsd',
'https://warwick.ac.uk/study/undergraduate/courses-2019/philosophyliterature',
'https://warwick.ac.uk/study/undergraduate/courses-2019/philosophywithpsychology',
'http://www2.warwick.ac.uk/study/undergraduate/courses-2019/ppe',
'https://warwick.ac.uk/study/undergraduate/courses-2019/physicsbsc',
'https://warwick.ac.uk/study/undergraduate/courses-2019/physicsmphys',
'https://warwick.ac.uk/study/undergraduate/courses-2019/physicsbusiness',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politicsinternational',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politicsinternationalchinese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politicsinternationalfrench',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politicsinternationalgerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/paisgsd',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politicsinternationalhispanic',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politicsinternationalitalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politicsinternationalstudiesquantitative',
'https://warwick.ac.uk/study/undergraduate/courses-2019/ppl',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politicssociology',
'https://warwick.ac.uk/study/undergraduate/courses-2019/psychology',
'https://warwick.ac.uk/study/undergraduate/courses-2019/psychologyeducation',
'https://warwick.ac.uk/study/undergraduate/courses-2019/paisgsd/psychologygsd',
'https://warwick.ac.uk/study/undergraduate/courses-2019/psychologylinguistics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/sociology',
'https://warwick.ac.uk/study/undergraduate/courses-2019/sociologygsd',
'https://warwick.ac.uk/study/undergraduate/courses-2019/sociologyquantitativemethods',
'https://warwick.ac.uk/study/undergraduate/courses-2019/systemsengineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/systemsengineeringmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/theatrestudies',
'https://warwick.ac.uk/study/undergraduate/courses-2019/theatregsd',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'The University of Warwick'
        try:
            location = 'warwick'
            #location = remove_tags(location)
            #print(location)
        except:
            location = 'N/A'
            #print(location)
        try:
            department = response.xpath('').extract()[0]
            department = remove_tags(department)
            department = department.replace('\n\n', '\n')
            department = department.replace('\r\n', '')
            department = department.replace('	', '')
            department = department.replace('  ', '')
            department = department.replace('\n', '')
            department = department.replace('Our Staff', '')
            #print(department)
        except:
            department = ''
            #print(department)


        try:
            degree_name = response.xpath('//*[@id="main"]/div/div/div/div/div[2]/div[1]/section/h3/strong').extract()[0]
            degree_name = remove_tags(degree_name)
            degree_name = re.findall('.* \((.*)\)',degree_name)[0]

            #degree_name = re.findall('(.*)\n.*',degree_name)[0]
            #degree_name = re.findall('(.*)                    .*',degree_name)[0]
            #degree_name = re.findall('\((.*)\)',degree_name)[0]
            #degree_name = degree_name.replace('\n',degree_name)
            degree_name = degree_name.replace(' ','')
            #print(degree_name)
        except:
            degree_name = 'BA'
            #print(degree_name)

        try:
            degree_overview_en = ''
            degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = "<div><p>" + degree_overview_en + "</p></div>"
            #print(degree_overview_en)
        except:
            degree_overview_en = ''

        try:
            programme_en = response.xpath('//*[@id="main"]/div/div/div/div/div[2]/div[1]/section/h3/strong').extract()[0]
            programme_en = remove_tags(programme_en)
            programme_en =programme_en.replace('\r\n','')
            #programme_en = re.findall('',programme_en)[0]
            programme_en = programme_en.replace('  ',' ')
            programme_en = programme_en.replace(degree_name,'')
            programme_en = programme_en.replace('()','')
            #print(programme_en)

        except:
            programme_en = 'N/A'
            #print(programme_en)

        try:
            overview_en = response.xpath('//*[@id="course-tab-1"]/section/p').extract()[0]
            overview_en = remove_tags(overview_en)
            overview_en = overview_en.replace('  ','')
            #overview_en = overview_en.replace('\n\n','\n')
            overview_en = overview_en.replace('\n\n','')
            overview_en = overview_en.replace('\r\n','')
            overview_en = overview_en.replace('\n','')
            overview_en = '<div>' + overview_en + '</div>'
            #overview_en = remove_tags(overview_en)
            #print(overview_en)
        except:
            overview_en = 'N/A'
            #print(overview_en)


        try:
            start_date = response.xpath('//*[@id="course-tab-5"]').extract()[0]
            start_date = remove_tags(start_date)
            start_date = start_date.replace('\r\n','')
            start_date = start_date.replace('  ',' ')
            start_date = start_date.replace('\n','')
            start_date = re.findall('Start Date(.*)',start_date)[0]
            if 'October' in start_date:
                start_date = '2019-10'
            elif '24' in start_date:
                start_date = '2019-9-24'
            else:
                start_date = '2019-9'
            #print(start_date)

        except:
            start_date = 'N/A'
            #print(start_date)



        try:
            modules_en = response.xpath('//*[@id="course-tab-3"]').extract()[0]
            modules_en = remove_tags(modules_en)
            modules_en = modules_en.replace('\n\n','\n')
            modules_en = modules_en.replace('\r\n','')
            modules_en = modules_en.replace('	','')
            modules_en = modules_en.replace('  ','')
            modules_en = modules_en.replace('\n','')
            modules_en = "<div><p>" + modules_en + "</p></div>"
            #print(modules_en)
        except:
            modules_en = 'N/A'
            #print(modules_en)



        try:
            degree_requirements = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[2]/div[2]/div[1]/div[2]').extract()[0]
            degree_requirements = remove_tags(degree_requirements)
            degree_requirements = degree_requirements.replace('  ','')
            #print(degree_requirements)
        except:
            degree_requirements = ''
            #print(degree_requirements)

        try:
            rntry_requirements_en = response.xpath('//*[@id="course-tab-2"]').extract()[0]
            rntry_requirements_en = remove_tags(rntry_requirements_en)
            rntry_requirements_en = "<div>"+rntry_requirements_en+"</div>"
            rntry_requirements_en = rntry_requirements_en.replace('\n\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\r\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('  ','')
            #rntry_requirements_en =rntry_requirements_en.replace('		                        ','')
            #print(rntry_requirements_en)
        except:
            rntry_requirements_en = 'N/A'
            #print(rntry_requirements_en)

        try:
            professional_background = response.xpath('').extract()
            professional_background = remove_tags(professional_background)
        except:
            professional_background = ''

        try:
            require_chinese_en = ''
        except:
            require_chinese_en = ''
        try:
            ielts_desc = 'https://warwick.ac.uk/study/undergraduate/courses-2019/economicspoliticsinternational'
            #print(ielts_desc)

        except:
            ielts_desc = 'N/A'

            #print(ielts_desc)

        try:
            #ielts = '6.5'
            #ielts =remove_tags(ielts)
            #ielts = re.findall('IELTS(.*)',ielts)[0]
            ielts = 0
            #print(ielts)
        except:
            ielts = 0
            #print(ielts)

        try:
            #ielts_l = '5.5'
            ielts_l = 0
            #print(ielts_l)
            #ielts_l = remove_tags(ielts_l)
        except:
            ielts_l = 0

        try:
            ielts_s = ielts_l

        except:
            ielts_s = ielts_l

        try:
            ielts_r = ielts_l
        except:
            ielts_r = ielts_l

        try:
            ielts_w = ielts_l
        except:
            ielts_w = ielts_l

        try:
            toefl_code = response.xpath('').extract()
            toefl_code = remove_tags(toefl_code)
        except:
            toefl_code = 0

        try:
            toefl_desc = response.xpath('').extract()
            toefl_desc = remove_tags(toefl_desc)
        except:
            toefl_desc = 0

        try:
            toefl = response.xpath('').extract()
            toefl = remove_tags(toefl)

        except:
            toefl = 0

        try:
            toefl_l = response.xpath('').extrcat()
            toefl_l = remove_tags(toefl_l)

        except:
            toefl_l = 0

        try:
            toefl_s = response.xpath('').extract()
            toefl_s = remove_tags(toefl_s)

        except:
            toefl_s = 0

        try:
            toefl_r = response.xpath('').extract()
            toefl_r = remove_tags(toefl_r)
        except:
            toefl_r = 0

        try:
            toefl_w = response.xpath('').extract()
            toefl_w = remove_tags(toefl_w)
        except:
            toefl_w = 0

        try:
            interview_desc_en = response.xpath('//*[@id="entry-requirements-accordion-0"]/div[1]').extract()[0]
            interview_desc_en = remove_tags(interview_desc_en)
            interview_desc_en = interview_desc_en.replace('\n\n', '\n')
            interview_desc_en = interview_desc_en.replace('\r\n', '')
            interview_desc_en = interview_desc_en.replace('	', '')
            interview_desc_en = interview_desc_en.replace('  ', '')
            interview_desc_en = interview_desc_en.replace('\n', '')
            interview_desc_en = "<div>" + interview_desc_en + "</div>"
            #print(interview_desc_en)
        except:
            interview_desc_en = 'N/A'
            #print(interview_desc_en)
        try:
            work_experience_desc_en = response.xpath('').extract()
            work_experience_desc_en = remove_tags(work_experience_desc_en)
        except:
            work_experience_desc_en = ''

        try:
            portfolio_desc_en = response.xpath('').extract()
            portfolio_desc_en = remove_tags(portfolio_desc_en)
        except:
            portfolio_desc_en = ''

        try:
            career_en = response.xpath('//*[@id="course-tab-4"]').extract()[0]
            career_en = remove_tags(career_en)
            career_en = career_en.replace('\r\n','')
            career_en = career_en.replace('  ','')
            career_en = career_en.replace('\n','')
            career_en = "<div><span>" + career_en + "</span></div>"
            #print(career_en)
        except:
            career_en = ''
            #print(career_en)
        try:
            apply_desc_en = '<span>Assessing each application fairly and consistently within an extremely competitive field is a difficult task. It is carried out by course selectors (Admissions Tutors) who are academics in departments and by professionals in the Undergraduate Admissions Team to ensure that decisions are made fairly, taking into account as much information about applicants as possible. Applications are assessed on their own merits and in competition with others, as we receive many more applications for most courses than there are places available. Selectors judge the evidence provided on the UCAS application against the criteria set for the chosen course. They take into account existing academic achievements and the context within which they have been achieved (including any exceptional circumstances), predicted grades, the personal statement and the academic reference. Remember that selectors want to hear about you and your interests and potential – there is no one-size-fits-all approach! As a consequence of the high level of competition for our courses, and because we want to consider your full profile and your potential as an individual rather than simply looking at your actual or predicted grades, it may take some time to communicate a decision to you. We will keep you informed of the status of your application during the admissions process. Successful candidates will receive an offer which the selector feels is most appropriate, though typical offer levels are listed for each course. We will provide feedback to candidates to whom we are not able to make an offer when this is requested in writing. You should be aware that decisions are made on a highly competitive basis and therefore we are often unable to make offers to all applicants who meet, or even exceed, the typical entry requirements.</span>'
            #apply_desc_en = remove_tags(apply_desc_en)
            #apply_desc_en = "<div>" + apply_desc_en + "</div>"
            #print(apply_desc_en)
        except:
            apply_desc_en = ''

        try:
            apply_documents_en = ''
            #apply_documents_en = remove_tags(apply_documents_en)
        except:
            apply_documents_en = ''


        apply_fee = 13

        dead_time = '1-15'
        #other = ''
        try:
            apply_proces_en = response.xpath('').extract()
        except:
            apply_proces_en = ''


        try:
            duration = response.xpath('//*[@id="course-tab-5"]').extract()[0]
            #duration = remove_tags(duration)
            duration = remove_tags(duration)
            duration = duration.replace('  ','')
            duration = duration.replace('\r\n','')
            duration = duration.replace('\n','')
            duration = re.findall('Duration(.*)',duration)[0]
            #duration = re.findall('(\d) Years',duration)[0]
            if '4' in duration:
                duration = '4'
            elif '3' in duration:
                duration = '3'
            elif '5' in duration:
                duration = '5'
            elif '2' in duration:
                duration = '2'
            elif '1' in duration:
                duration = '1'
            elif 'two' in duration:
                duration = '2'
            else:
                duration = 'N/A'
            #print(duration)

        except:
            duration = 'N/A'
            #print(duration)



        try:
            other = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/a').extract()[0]
            other = remove_tags(other)
            #print('成功'+ other + response.url)
        except:
            other = ''
           #print('失败' + other)

        try:
            ib = response.xpath('//*[@id="main"]/div/div/div/div/div[2]/div[1]/section/p[1]/strong[2]').extract()[0]
            ib = remove_tags(ib)
            #print(ib)
        except:
            ib = ''
            #print(ib)

        try:
            alevel = response.xpath('//*[@id="main"]/div/div/div/div/div[2]/div[1]/section/p[1]/strong[1]').extract()[0]
            alevel = remove_tags(alevel)
            alevel = re.findall('entry, (.*), IB',alevel)[0]
            #alevel = alevel.replace('*','')
            #alevel = re.findall("(\w\w\w)",alevel)[0]
            #print(alevel)
        except:
            alevel = 'N/A'
            #print(alevel)
        try:
            ucascode = response.xpath('//*[@id="course-tab-5"]').extract()[0]
            ucascode = remove_tags(ucascode)
            ucascode = ucascode.replace('\r\n','')
            ucascode = ucascode.replace('\n','')
            ucascode = ucascode.replace('  ',' ')
            ucascode = re.findall('UCAS Code(.*)Award',ucascode)[0]
            ucascode = ucascode.replace('     ','')
            ucascode = ucascode.replace('   ','')
            #print(ucascode)
        except:
            ucascode = 'N/A'
            #print(ucascode)

        try:
            tuition_fee = response.xpath('/html/body/div[1]/div/div[1]/section[7]/div/div/div[3]/div/div[2]').extract()[0]
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = tuition_fee.replace('£','')
            tuition_fee = tuition_fee.replace(',','')
            tuition_fee = tuition_fee.replace('*','')
            tuition_fee = tuition_fee.replace(' ','')
            tuition_fee = tuition_fee.replace('\r\n','')
            tuition_fee = tuition_fee.replace('\n','')

            tuition_fee = re.findall('(\d\d\d\d\d)',tuition_fee)[0]

            # tuition_fee = tuition_fee.replace('  ','')
            # tuition_fee = tuition_fee.replace('\n','')
            # tuition_fee = re.findall('Full-time international students: £(.*) paStudents',tuition_fee)[0]
            # tuition_fee = int(tuition_fee)
            #print(tuition_fee)
        except:
            tuition_fee = 0
            #print(tuition_fee)

        try:
            assessment_en = response.xpath('//*[@id="assessment-methods"]/div/p').extract()[0]
            assessment_en = remove_tags(assessment_en)
            assessment_en = assessment_en.replace('\r\n', '')
            assessment_en = assessment_en.replace('  ', '')
            assessment_en = assessment_en.replace('\n', '')
            assessment_en = "<div><span>" + assessment_en + "</span></div>"
            #print(assessment_en)
        except:
            assessment_en = ''
            #print(assessment_en)

        application_open_date = '2018-10-6/2018-10-20'
        item["university"] = university
        item["location"] = location
        item["department"] = department
        item["degree_type"] = 1
        item["degree_name"] = degree_name
        #item["degree_overview_en"] = degree_overview_en
        item["programme_en"] = programme_en
        item["overview_en"] = overview_en
        item["teach_time"] = 1
        item["start_date"] = start_date
        item["modules_en"] = modules_en
        item["career_en"] = career_en
        item["application_open_date"] = '9'
        item["deadline"] = ''
        item["apply_pre"] = '£'
        item["apply_fee"] = apply_fee
        #item["rntry_requirements_en"] = rntry_requirements_en
        item["degree_requirements"] = degree_requirements
        item["tuition_fee_pre"] = '£'
        #item["major_requirements"] = rntry_requirements_en
        item["professional_background"] = professional_background
        item["ielts_desc"] = ielts_desc
        item["ielts"] = ielts
        item["ielts_l"] = ielts_l
        item["ielts_s"] = ielts_l
        item["ielts_r"] = ielts_l
        item["ielts_w"] = ielts_l
        item["toefl_code"] = toefl_code
        item["toefl_desc"] = toefl_desc
        item["toefl"] = toefl
        item["toefl_l"] = toefl_l
        item["toefl_s"] = toefl_s
        item["toefl_r"] = toefl_r
        item["toefl_w"] = toefl_w
        item["work_experience_desc_en"] = work_experience_desc_en
        item["interview_desc_en"] = interview_desc_en
        item["portfolio_desc_en"] = portfolio_desc_en
        item["apply_desc_en"] = apply_desc_en
        item["apply_documents_en"] = apply_documents_en
        item["other"] = other
        item["url"] = response.url
        item["gatherer"] = 'weihongbo'
        item["apply_proces_en"] = apply_proces_en
        item["batch_number"] = 2
        item["finishing"] = 0
        stime = time.time()
        create_time = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(float(stime)))
        #print(create_time)
        item["create_time"] = create_time
        item["import_status"] = 0
        item["duration"] = duration
        item["tuition_fee"] = tuition_fee
        item["update_time"] = create_time
        item["alevel"] = alevel
        item["ib"] = ib
        item["ucascode"] = ucascode
        item["rntry_requirements"] = rntry_requirements_en
        item["require_chinese_en"] = require_chinese_en
        item["assessment_en"] =  assessment_en
        item["application_open_date"] = application_open_date
        #item["apply_pre"] = ''
        yield item


