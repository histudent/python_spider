import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'Lancaster_University_P'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/accounting-and-financial-management-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/advanced-financial-analysis-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/advanced-marketing-management-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/applied-linguistics-and-tesol-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/arts-management-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/biomedicine-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/business-administration-mba/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/business-analytics-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/clinical-research-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/computer-science-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/conflict-resolution-and-peace-studies-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/conflict-development-and-security-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/conservation-and-biodiversity-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/creative-writing-modular-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/creative-writing-by-independent-project-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/creative-writing-with-english-literary-studies-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/criminal-justice-and-social-research-methods-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/criminology-and-criminal-justice-llm/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/criminology-and-criminal-justice-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/criminology-and-social-research-methods-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/cyber-security-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/data-science-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/design-management-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/developmental-disorders-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/developmental-psychology-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/diplomacy-and-foreign-policy-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/diplomacy-and-international-law-llmma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/diplomacy-and-religion-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/discourse-studies-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/ebusiness-and-innovation-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/economics-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/education-and-social-justice-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/electronic-engineering-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/engineering-project-management-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/english-language-and-literary-studies-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/english-literary-research-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/english-literary-studies-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/english-literary-studies-with-creative-writing-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/entrepreneurship-innovation-and-practice-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/environment-and-development-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/environment-and-development-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/environment-and-law-llm/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/environment-culture-and-society-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/environmental-management-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/finance-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/gender-and-womens-studies-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/gender-and-womens-studies-and-english-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/gender-and-womens-studies-and-sociology-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/history-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/human-resource-management-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/human-resources-and-consulting-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/human-rights-and-the-environment-llmma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/information-technology-management-and-organisational-change-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/international-business-and-corporate-law-llm/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/international-business-and-strategy-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/international-human-rights-law-llm/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/international-human-rights-and-terrorism-law-llm/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/international-law-llm/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/international-law-and-international-relations-llm/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/international-law-and-international-relations-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/international-relations-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/language-and-linguistics-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/languages-and-cultures-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/law-llm/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/logistics-and-supply-chain-management-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/management-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/management-2-year-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/marketing-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/marketing-analytics-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/mechanical-engineering-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/mechanical-engineering-with-project-management-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/media-and-cultural-studies-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/money-banking-and-finance-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/philosophy-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/philosophy-and-religion-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/politics-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/politics-and-philosophy-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/politics-philosophy-and-management-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/politics-philosophy-and-religion-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/project-management-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/psychological-research-methods-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/psychology-of-advertising-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/quantitative-finance-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/religion-and-conflict-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/religious-studies-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/social-research-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/social-work-ma-l508/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/sociology-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/statistics-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/sustainable-water-management-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/translation-ma/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/volcanology-and-geological-hazards-msc/',
'http://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/wireless-communication-systems-msc/',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'Lancaster University'
        try:
            location = 'Lancaster'
            #location = remove_tags(location)
            #print(location)
        except:
            location = 'N/A'
            #print(location)
        try:
            department = response.xpath('//*[@id="main"]/div[3]/section[1]/div[2]/div/div/div/div[2]/aside/div[2]/div/div/ul/li[1]/a/strong').extract()[0]
            department = remove_tags(department)
            department = department.replace('\n\n', '\n')
            department = department.replace('\r\n', '')
            department = department.replace('	', '')
            #department = department.replace('  ', '')
            department = department.replace('\n', '')
            #department = department.replace('Our Staff', '')
            #print(department)
        except:
            department = ''
            #print(department)


        try:
            degree_name = response.xpath('//*[@id="main"]/div[1]/section[1]/div/div[2]/div/div/h1/span').extract()[0]
            degree_name = remove_tags(degree_name)
            #degree_name =re.findall('.*- (.*)',degree_name)[0]

            #degree_name = re.findall('\((.*)\).*',degree_name)[0]
            #degree_name = re.findall('(.*)                    .*',degree_name)[0]
            #degree_name = re.findall('\((.*)\)',degree_name)[0]
            #degree_name = degree_name.replace('\n',degree_name)
            #degree_name = degree_name.replace(' ','')
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
            programme_en = response.xpath('//h1').extract()[0]
            programme_en = remove_tags(programme_en)
            programme_en = programme_en.replace(degree_name,'')
            programme_en = re.findall('(.*)-.*',programme_en)[0]
            #programme_en = programme_en.replace(' - University of Winchester ','')
            #programme_en = programme_en.split()[1]
            #programme_en = re.findall(' (.*)',programme_en)[0]
            #programme_en = programme_en.replace(degree_name,'')
            #programme_en = programme_en.replace('  ','')
            #programme_en = programme_en.replace('\n', '')
            #programme_en = re.findall(('                    '),'')[0]
            #programme_en = re.findall("\(.*\)(.*)",programme_en)[0]
            #programme_en = programme_en.replace('\n','')
            #programme_en = programme_en.replace('				','')
            #programme_en = programme_en.replace(' -','')
            #print(programme_en)
        except:
            programme_en = 'N/A'
            #print(programme_en)

        try:
            overview_en = response.xpath('//*[@id="overview"]').extract()[0]
            overview_en = remove_tags(overview_en)
            #overview_en = re.findall('COURSE OVERVIEW(.*)',overview_en)[0]
            overview_en = overview_en.replace('  ','')
            overview_en = overview_en.replace('\n\n','\n')
            overview_en = overview_en.replace('\n\n','')
            overview_en = overview_en.replace('\r\n','')
            overview_en = overview_en.replace('\n','')
            #overview_en = re.findall('COURSE OVERVIEW(.*)Careers',overview_en)[0]
            overview_en = '<div>' + overview_en + '</div>'

            #overview_en = remove_tags(overview_en)
            #print(overview_en)
        except:
            overview_en = 'N/A'
            #print(overview_en)


        try:
            start_date = response.xpath('//*[@id="main_content"]/div[2]/div[2]/div[3]/ul/li[2]/ul/li').extract()[0]
            start_date = remove_tags(start_date)

            if 'September or January' in start_date:
                start_date = '1,9'
            elif 'September' in start_date:
                start_date = '9'
            elif 'January' in start_date:
                start_date = '9'
            else:
                start_date = '10'
            #print(start_date)
        except:
            start_date = '10'
            #print(start_date)


        try:
            #modules_en = response.xpath('//div[4]/div/div/div[1]/div[5]/div/div[2]/p').extract()[0]
            modules_en = response.xpath('//*[@id="structure"]/div/div').extract()[0]
            modules_en = remove_tags(modules_en)
            # overview_en = re.findall('COURSE OVERVIEW(.*)',overview_en)[0]
            modules_en = modules_en.replace('  ', ' ')
            modules_en = modules_en.replace('\n\n', '\n')
            modules_en = modules_en.replace('\n\n', '')
            modules_en = modules_en.replace('\r\n', '')
            modules_en = modules_en.replace('\n', '')
            #modules_en = re.findall('Year 1(.*)in Year 1', modules_en)[0]
            modules_en = '<div>' + modules_en + '</div>'
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
            rntry_requirements_en = response.xpath('//*[@id="course-key-information"]').extract()[0]
            rntry_requirements_en = remove_tags(rntry_requirements_en)
            rntry_requirements_en = rntry_requirements_en.replace('\n\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\r\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('  ',' ')
            #rntry_requirements_en = re.findall('ENTRY REQUIREMENTS(.*)Visit us',rntry_requirements_en)[0]
            #rntry_requirements_en = "<div>"+rntry_requirements_en+"</div>"

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
            ielts_desc = remove_tags(ielts_desc)
            #print(ielts_desc)

        except:
            ielts_desc = 'N/A'

            #print(ielts_desc)

        try:
            ielts = rntry_requirements_en
            ielts = re.findall('(\d\.\d)', ielts)[0]
            #ielts =remove_tags(ielts)
            #ielts = re.findall('IELTS(.*)',ielts)[0]
            #ielts = re.findall('(\d\.\d)',ielts)[0]
            #print(ielts)
        except:
            ielts = 0
            #print(ielts)

        try:
            ielts_l = '5.5'
            ielts = re.findall('(\d\.\d)', ielts)[1]
            #print(ielts_l)
            #ielts_l = remove_tags(ielts_l)
        except:
            ielts_l = 0
           #print(ielts_l)

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
            career_en = response.xpath('//*[@id="careers"]').extract()[0]
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
            apply_desc_en = '<div>You can apply directly to the University for admission to postgraduate taught courses using My Applications website. If your native language is not English you will be asked for a recognised English language qualification. Most postgraduate taught courses start in October.</div>'
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


        #other = ''
        try:
            apply_proces_en = response.xpath('').extract()
        except:
            apply_proces_en = ''


        try:
            duration = response.xpath('//*[@id="main_content"]/div[2]/div[2]/div[3]/ul/li[3]/ul/li').extract()[0]
            duration = remove_tags(duration)
            #duration = remove_tags(duration)
            #duration = re.findall('(\d) Years',duration)[0]
            if 'One' in duration:
                duration = '1'
            elif '1' in duration:
                duration = '1'
            elif '12' in duration:
                duration = '1'
            elif 'Two' in duration:
                duration = '2'
            elif '2' in duration:
                duration = '2'
            elif '1' in duration:
                duration = '1'
            elif 'two' in duration:
                duration = '2'

            else:
                duration = '1'
            #print(duration)
        except:
            duration = 1
            #print(duration)



        try:
            other = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/a').extract()[0]
            other = remove_tags(other)
            #print('成功'+ other + response.url)
        except:
            other = ''
           #print('失败' + other)

        try:
            ib = response.xpath('//*[@id="tab-Entry_Requirements"]/div/div[1]/div[1]/table[1]/tbody/tr[11]/td[2]').extract()[0]
            ib = remove_tags(ib)
            #print(ib)
        except:
            ib = ''
            #print(ib)

        try:
            alevel = response.xpath('//*[@id="tab-Entry_Requirements"]/div/div[1]/div/table[1]').extract()[0]
            alevel = remove_tags(alevel)
            alevel = re.findall("(\w\w\w) at A Level",alevel)[0]
            #print(alevel)
        except:
            alevel = 'CC'
            #print(alevel)
        try:
            ucascode = response.xpath('/html/body/div[3]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[2]').extract()[0]
            ucascode = remove_tags(ucascode)

            #print(ucascode)
        except:
            ucascode = ''
            #print(ucascode)

        try:
            tuition_fee = response.xpath('//*[@id="fees"]/div/div/table/tbody/tr[3]/td[1]').extract()[0]
            # tuition_fee = remove_tags(tuition_fee)
            # tuition_fee = tuition_fee.replace('£','')
            tuition_fee = tuition_fee.replace(',','')
            # tuition_fee = tuition_fee.replace('*','')
            # tuition_fee = tuition_fee.replace(' ','')
            # tuition_fee = tuition_fee.replace('\r\n','')
            # tuition_fee = tuition_fee.replace('\n','')
            # #
            tuition_fee = re.findall('(\d\d\d\d\d)',tuition_fee)[0]

            # tuition_fee = tuition_fee.replace('  ','')
            # tuition_fee = tuition_fee.replace('\n','')
            # tuition_fee = re.findall('Full-time international students: £(.*) paStudents',tuition_fee)[0]
            # tuition_fee = int(tuition_fee)
            print(tuition_fee)
        except:
            tuition_fee = 0
            print(tuition_fee)

        try:
            assessment_en = response.xpath('//*[@id="structure"]/section[2]/section[1]').extract()[0]
            assessment_en = remove_tags(assessment_en)
            assessment_en = assessment_en.replace('\r\n', '')
            assessment_en = assessment_en.replace('  ', '')
            assessment_en = assessment_en.replace('\n', '')
            assessment_en = assessment_en.replace('			','')
            assessment_en = assessment_en.replace('		','')
            assessment_en = "<div>"+assessment_en+'</div>'
            #print(assessment_en)
        except:
            assessment_en = 'N/A'
            #print(assessment_en)
        try:
            teach_time = response.xpath('//*[@id="tab-overview1"]/section/div[2]/div').extract()[0]
            teach_time = remove_tags(teach_time)
            if 'full' in teach_time:
                teach_time = 'fulltime'
            elif 'Full' in teach_time:
                teach_time = 'fulltime'
            else:
                teach_time = 'parttime'
            #print(teach_time)
        except:
            teach_time = 'N/A'
            #print(teach_time)

        teach_type = 'taught'

        item["university"] = university
        item["location"] = location
        item["department"] = department
        item["degree_type"] = 2
        item["degree_name"] = degree_name
        #item["degree_overview_en"] = degree_overview_en
        item["programme_en"] = programme_en
        item["overview_en"] = overview_en
        item["teach_time"] = 1
        item["start_date"] = start_date
        item["modules_en"] = modules_en
        item["career_en"] = career_en
        item["application_open_date"] = '9'
        item["deadline"] = '7-31'
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
        item["ielts_s"] = ielts_s
        item["ielts_r"] = ielts_r
        item["ielts_w"] = ielts_w
        item["toefl_code"] = ''
        item["toefl_desc"] = toefl_desc
        item["toefl_l"] = toefl_l
        item["toefl"] = toefl
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
        #item["alevel"] = alevel
        #item["ib"] = ib
        #item["ucascode"] = ucascode
        item["rntry_requirements"] = rntry_requirements_en
        item["require_chinese_en"] = '<p>For entry to a Kent postgraduate degree programme (Master’s), Chinese students typically need to have completed a Bachelor Degree (Xueshi) at a recognised institution. Exact requirements will depend on the postgraduate degree you are applying for and the undergraduate degree you have studied.  For programmes that require a 2:1 we usually ask for a Bachelor degree (Xueshi) from a 211 university with a final grade of 70%. For Bachelor degrees from other recognised institutions you will need to achieve a final grade of 75%  For programmes that require a 2:2 we usually ask for a Bachelor degree (Xueshi) from a 211 university with a final grade of 65%. For Bachelor degrees from other recognised institutions you will need to achieve a final grade of 70%  Applicants with relevant work experience may be considered with lower grades.  Some, but not all, postgraduate programmes require your undergraduate degree to have a related major. Some postgraduate programmes may require work experience in a relevant field or at a certain level.</p>'
        item["assessment_en"] = assessment_en
        item["teach_time"] = teach_time
        item["teach_type"] = teach_type
        #item["apply_pre"] = ''
        #yield item


