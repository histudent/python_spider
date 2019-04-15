import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'Heriot-Watt_University_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []


    C= ['https://www.hw.ac.uk/study/uk/undergraduate/actuarial-science-and-diploma-in-industrial-training.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/applied-languages-and-translating-french-german.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/accountancy-and-business-law.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/computer-science-artificial-intelligence.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/actuarial-science.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/computing-and-electronics.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/accountancy-and-finance.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/combined-studies-bsc.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/computing-and-electronics-meng.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/computer-science-data-science-dip-industrial-training.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/computer-systems-dip-industrial-training.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/applied-languages-and-translating-french-spanish.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemical-engineering-with-energy-engineering.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/business-and-finance.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/biological-sciences.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/computer-science-data-science.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/bachelor-of-business-administration.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/architectural-engineering-with-international-studies.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/architectural-engineering-meng.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/architectural-engineering-beng.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/applied-languages-and-translating-german-spanish.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/british-sign-language-interpreting-translating-and-applied-language.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/brewing-and-distilling.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/biological-sciences-cell-and-molecular-biology.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/biological-sciences-human-health.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemistry-with-materials-nanoscience-mchem.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemistry-with-industrial-experience.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/biological-sciences-microbiology.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemistry-with-materials.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemistry-with-computational-chemistry.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemistry-with-computational-chemistry-mchem.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemical-engineering-meng.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemistry-with-biochemistry.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemical-engineering-beng.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemical-engineering-diploma-in-industrial-training-meng.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemistry-mchem.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemical-physics.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemical-physics-mphys.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemical-engineering-and-diploma-in-industrial-training.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemical-engineering-with-oil-and-gas-technology-with-dit.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemical-engineering-with-oil-and-gas-technology.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemistry-bsc.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemistry-with-biochemistry-mchem.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemistry-with-a-year-in-north-america.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemistry-with-a-year-in-europe.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemistry-with-a-year-in-australia-mchem.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemistry-with-a-european-language.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/computer-systems-games-programming.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/computer-systems.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/computer-science-dip-industrial-training.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/civil-engineering.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/civil-engineering-meng.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/professional-education-and-chemistry-bsc.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/civil-engineering-with-international-studies.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemistry-with-pharmaceutical-chemistry-mchem.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/chemistry-with-pharmaceutical-chemistry.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/computer-science-software-engineering.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/computer-science-bsc.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/computer-science-games-programming.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/information-systems-management.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/information-systems-internet-systems.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/information-systems-interaction-design.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/german-and-applied-language-studies.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/information-systems.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/geography-society-and-environment.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/geography-bsc.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/french-and-applied-language-studies.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/financial-mathematics.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/engineering.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/electrical-power-and-energy.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/fashion-marketing-and-retailing.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mathematical-statistical-and-actuarial-sciences.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/electrical-power-and-energy-meng.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mathematical-physics-mphys.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mathematics-with-finance.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mathematical-physics.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/international-business-management-and-languages-german-as-main.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/interior-design.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/international-business-management-and-languages-french-as-main.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/international-business-management-and-languages-chinese-as-main.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/international-business-management.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/business-management-with-marketing.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/languages-interpreting-and-translating-german-british-sign-language.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/languages-interpreting-and-translating-french-spanish.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/languages-interpreting-and-translating-french-british-sign-language.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/languages-interpreting-and-translating-french-german.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/international-business-management-with-operations-management.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/international-business-management-year-abroad.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/marine-biology.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/international-business-management-with-economics.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/business-management-with-business-law.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/business-management-with-human-resource-management.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/business-management-with-enterprise.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/international-business-management-and-languages-spanish-as-main.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/languages-interpreting-and-translating-spanish-british-sign-language.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mathematics-with-computer-science.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/languages-interpreting-and-translating-german-spanish.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mathematics-bsc.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mathematics-and-computer-science.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mathematics-mmath.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mathematical-statistical-and-actuarial-sciences-and-diploma-in.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/electrical-and-electronic-engineering.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/economics-and-marketing.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/electrical-and-electronic-engineering-meng.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/economics-and-finance.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/fashion.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/engineering-physics.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/finance-and-business-law.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/engineering-physics-mphys.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/fashion-technology.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/fashion-communication.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/finance.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/spanish-and-applied-language-studies.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/physics-bsc.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/structural-engineering-meng.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/statistical-data-science.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/quantity-surveying.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/physics-mphys.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/psychology-with-management.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/professional-education-secondary-engineering-technologies.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/professional-education-primary-science-stem.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mechanical-engineering-and-energy-engineering.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mechanical-engineering-and-energy-engineering-meng.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/professional-education-and-physics-bsc.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mechanical-engineering-beng.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mechanical-engineering-meng.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mathematics-with-spanish.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mathematics-with-statistics.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mathematics-with-physics.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mathematics-with-german.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/psychology-bsc.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mathematics-with-finance-and-diploma-in-industrial-training.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/mathematics-with-french.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/robotics-autonomous-and-interactive-systems.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/software-engineering.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/robotics-autonomous-and-interactive-systems-meng.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/urban-planning-and-property-development.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/structural-engineering-with-international-studies.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/structural-engineering.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/structural-engineering-with-architectural-design-meng.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/construction-project-management.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/economics-and-business-law.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/design-for-textiles-fashion-interior-art.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/structural-engineering-with-architectural-design.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/economics-and-business-management.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/economics-and-accountancy.htm',
'https://www.hw.ac.uk/study/uk/undergraduate/economics-ma.htm',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'Heriot-Watt University'
        try:
            location = response.xpath('//*[@id="content-main"]/section[3]/div/div/dl/dd[3]').extract()[0]
            location = remove_tags(location)
            #print(location)
        except:
            location = 'Edinburgh'
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
            degree_name = response.xpath('//*[@id="content-main"]/section[1]/div/div[2]/div[2]/div/h1').extract()[0]
            degree_name = remove_tags(degree_name)
            degree_name = re.findall('.*,(.*)',degree_name)[0]
            #degree_name = re.findall('\r\n',degree_name)
            #degree_name = re.findall('(.*)\n.*',degree_name)[0]
            #degree_name = re.findall('(.*)                    .*',degree_name)[0]
            #degree_name = re.findall('\((.*)\)',degree_name)[0]
            #degree_name = degree_name.replace('\n',degree_name)
            degree_name = degree_name.replace(' ','')
            degree_name = degree_name.replace('\r\n','')
            degree_name = degree_name.replace('\n','')


            #print(degree_name)
        except:
            degree_name = 'N/A'
            #print(degree_name)

        try:
            degree_overview_en = ''
            degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = "<div><p>" + degree_overview_en + "</p></div>"
            #print(degree_overview_en)
        except:
            degree_overview_en = ''

        try:
            programme_en = response.xpath('//*[@id="content-main"]/section[1]/div/div[2]/div[2]/div/h1').extract()[0]
            programme_en = remove_tags(programme_en)
            programme_en =programme_en.replace('\r\n','')
            #programme_en = re.findall('',programme_en)[0]
            programme_en = programme_en.replace('  ',' ')
            #programme_en = programme_en.replace(degree_name,'')
            #programme_en = programme_en.replace('()','')
            #print(programme_en)

        except:
            programme_en = 'N/A'
            #print(programme_en)

        try:
            overview_en = response.xpath('//*[@id="content-main"]/section[6]/div/div').extract()[0]
            overview_en = remove_tags(overview_en)
            overview_en = overview_en.replace('  ',' ')
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
            modules_en = response.xpath('//*[@id="course-content"]').extract()[0]
            modules_en = remove_tags(modules_en)
            modules_en = modules_en.replace('\n\n','\n')
            modules_en = modules_en.replace('\r\n','')
            modules_en = modules_en.replace('	',' ')
            #modules_en = modules_en.replace('  ','')
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
            rntry_requirements_en = response.xpath('//*[@id="entry-requirements"]').extract()[0]
            rntry_requirements_en = remove_tags(rntry_requirements_en)
            rntry_requirements_en = "<div>"+rntry_requirements_en+"</div>"
            rntry_requirements_en = rntry_requirements_en.replace('\n\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\r\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('  ',' ')
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
            ielts_desc = ''
            #print(ielts_desc)

        except:
            ielts_desc = 'N/A'

            #print(ielts_desc)

        try:
            aa = response.xpath('//*[@id="entry-requirements"]').extract()[0]
            aa =remove_tags(aa)
            ielts = re.findall('\d\.\d',aa)[0]
            #ielts = 0
            #print(ielts)
        except:
            ielts = 0
            #print(ielts)

        try:
            #ielts_l = '5.5'
            ielts_l = re.findall('\d\.\d',aa)[1]
            #print(ielts_l)
            #ielts_l = remove_tags(ielts_l)
        except:
            ielts_l = 0
            #print(ielts)
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
            career_en = response.xpath('//*[@id="career"]').extract()[0]
            career_en = remove_tags(career_en)
            career_en = career_en.replace('\r\n','')
            career_en = career_en.replace('  ',' ')
            career_en = career_en.replace('\n','')
            career_en = "<div><span>" + career_en + "</span></div>"
            #print(career_en)
        except:
            career_en = ''
            #print(career_en)
        try:
            apply_desc_en = ''
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


        apply_fee = 0

        dead_time = '1-15'
        #other = ''
        try:
            apply_proces_en = response.xpath('').extract()
        except:
            apply_proces_en = ''


        try:
            duration = response.xpath('//dl/dd[2]').extract()[0]
            #duration = remove_tags(duration)
            duration = remove_tags(duration)
            duration = duration.replace('  ','')
            duration = duration.replace('\r\n','')
            duration = duration.replace('\n','')
            #duration = re.findall('Duration(.*)',duration)[0]
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
            elif '6' in duration:
                duration = '6'
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
            ib = response.xpath('//*[@id="entry-requirements"]/ul[1]').extract()[0]
            ib = remove_tags(ib)
            ib = re.findall('Int. Baccalaureate(.*)',ib)[0]
            #print(ib)
        except:
            ib = ''
            #print(ib)

        try:
            alevel = response.xpath('//*[@id="entry-requirements"]/ul[1]/li[2]').extract()[0]
            alevel = remove_tags(alevel)
            #alevel = re.findall('entry, (.*), IB',alevel)[0]
            #alevel = alevel.replace('*','')
            #alevel = re.findall("(\w\w\w)",alevel)[0]
            #print(alevel)
        except:
            alevel = 'N/A'
            #print(alevel)
        try:
            ucascode = response.xpath('//*[@id="content-main"]/section[3]/div/div/dl/dd[1]').extract()[0]
            ucascode = remove_tags(ucascode)
            ucascode = ucascode.replace('\r\n','')
            ucascode = ucascode.replace('\n','')
            ucascode = ucascode.replace('  ',' ')
            #ucascode = re.findall('UCAS Code(.*)Award',ucascode)[0]
            #ucascode = ucascode.replace('     ','')
            #ucascode = ucascode.replace('   ','')
            #print(ucascode)
        except:
            ucascode = 'N/A'
            #print(ucascode)

        try:
            tuition_fee = response.xpath('//*[@id="fees-and-funding"]/table/tbody/tr/td[3]').extract()[0]
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
        item["batch_number"] = 3
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
        #yield item


