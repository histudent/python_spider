import scrapy
from bs4 import BeautifulSoup
from weihongbo_Australia.items import UcasItem
from weihongbo_Australia import items
from w3lib.html import remove_tags
import re
import time


class BaiduSpider(scrapy.Spider):
    name = 'Charles_Darwin_University_P'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['https://www.cdu.edu.au/study/bachelor-laws-blaws-2019',
'https://www.cdu.edu.au/study/bachelor-midwifery-wmidw1-2019',
'https://www.cdu.edu.au/study/bachelor-medical-laboratory-science-bmlsc-2019',
'https://www.cdu.edu.au/study/diploma-network-engineering-dipne-2019',
'https://www.cdu.edu.au/study/diploma-network-engineering-yneng1-2019',
'https://www.cdu.edu.au/study/bachelor-nursing-bnrsg-2019',
'https://www.cdu.edu.au/study/associate-degree-network-engineering-xneng1-2019',
'https://www.cdu.edu.au/study/bachelor-pharmacy-bphar-2019',
'https://www.cdu.edu.au/study/bachelor-psychological-science-wpsys1-2019',
'https://www.cdu.edu.au/study/diploma-psychology-ypsy01-2019',
'https://www.cdu.edu.au/study/bachelor-psychological-science-bpsys-2019',
'https://www.cdu.edu.au/study/bachelor-science-wsci01-2019',
'https://www.cdu.edu.au/study/bachelor-social-work-bsw-2019',
'https://www.cdu.edu.au/study/diploma-science-ysci01-2019',
'https://www.cdu.edu.au/study/bachelor-social-work-wscwk1-2019',
'https://www.cdu.edu.au/study/bachelor-software-engineering-bseng-2019',
'https://www.cdu.edu.au/study/bachelor-software-engineering-honours-bsengh-2019',
'https://www.cdu.edu.au/study/diploma-science-dipsci-2019',
'https://www.cdu.edu.au/study/bachelor-science-honours-bscih-2019',
'https://www.cdu.edu.au/study/bachelor-arts-bart-2019',
'https://www.cdu.edu.au/study/bachelor-accounting-wacc01-2019',
'https://www.cdu.edu.au/study/bachelor-artsbachelor-laws-barbla-2019',
'https://www.cdu.edu.au/study/bachelor-arts-warts1-2019',
'https://www.cdu.edu.au/study/bachelor-arts-barts-2019',
'https://www.cdu.edu.au/study/diploma-alcohol-and-other-drugs-yaod01-2019',
'https://www.cdu.edu.au/study/associate-degree-applied-social-science-xass01-2019',
'https://www.cdu.edu.au/study/bachelor-applied-social-science-wass01-2019',
'https://www.cdu.edu.au/study/diploma-aboriginal-and-torres-strait-islander-knowledges-yatsi1-2019',
'https://www.cdu.edu.au/study/bachelor-arts-honours-bah22-2019',
'https://www.cdu.edu.au/study/bachelor-behavioural-science-bbsc22-2019',
'https://www.cdu.edu.au/study/bachelor-business-wbus01-2019',
'https://www.cdu.edu.au/study/bachelor-creative-arts-and-industries-honours-bcaih-2019',
'https://www.cdu.edu.au/study/bachelor-computer-science-wcoms1-2019',
'https://www.cdu.edu.au/study/bachelor-creative-arts-and-industries-new-media-designbachelor-information-technology-bcnmit',
'https://www.cdu.edu.au/study/bachelor-computer-sciencemaster-information-technology-hcsit1-2019',
'https://www.cdu.edu.au/study/bachelor-creative-arts-wcart1-2019',
'https://www.cdu.edu.au/study/bachelor-engineeringbachelor-commerce-bengbc-2019',
'https://www.cdu.edu.au/study/diploma-counselling-ycoun1-2019',
'https://www.cdu.edu.au/study/bachelor-design-bdes-2019',
'https://www.cdu.edu.au/study/bachelor-educational-studies-wedst1-2019',
'https://www.cdu.edu.au/study/bachelor-engineeringbachelor-information-technology-bengbi-2019',
'https://www.cdu.edu.au/study/bachelor-environmental-science-environmental-management-besem-2019',
'https://www.cdu.edu.au/study/bachelor-environmental-science-wenvs1-2019',
'https://www.cdu.edu.au/study/associate-degree-exercise-and-sport-science-xexss1-2019',
'https://www.cdu.edu.au/study/diploma-exercise-and-sport-science-yexss1-2019',
'https://www.cdu.edu.au/study/diploma-engineering-yeng01-2019',
'https://www.cdu.edu.au/study/bachelor-engineering-sciencemaster-engineering-heng01-2019',
'https://www.cdu.edu.au/study/bachelor-education-secondary-weds01-2019',
'https://www.cdu.edu.au/study/bachelor-engineering-sciencemaster-engineering-bensme-2019',
'https://www.cdu.edu.au/study/associate-degree-engineering-xeng01-2019',
'https://www.cdu.edu.au/study/bachelor-engineering-science-wengs1-2019',
'https://www.cdu.edu.au/study/bachelor-engineering-science-bengs-2019',
'https://www.cdu.edu.au/study/bachelor-engineering-honours-veng01-2019',
'https://www.cdu.edu.au/study/bachelor-exercise-and-sport-science-bess-2019',
'https://www.cdu.edu.au/study/bachelor-education-early-childhood-teaching-bedec-2019',
'https://www.cdu.edu.au/study/bachelor-education-primary-wedp01-2019',
'https://www.cdu.edu.au/study/bachelor-humanitarian-and-community-studies-bhcs-2019',
'https://www.cdu.edu.au/study/bachelor-health-science-whsc01-2019',
'https://www.cdu.edu.au/study/bachelor-information-systems-bis-2019',
'https://www.cdu.edu.au/study/bachelor-information-technology-bit3-2019',
'https://www.cdu.edu.au/study/bachelor-information-technology-wint01-2019',
'https://www.cdu.edu.au/study/bachelor-indigenous-languages-and-linguistics-winll1-2019',
'https://www.cdu.edu.au/study/bachelor-indigenous-knowledges-honours-vinkh1-2019',
'https://www.cdu.edu.au/study/associate-degree-indigenous-languages-and-linguistics-xinll1-2019',
'https://www.cdu.edu.au/study/associate-degree-information-and-communication-technology-xict01-2019',
'https://www.cdu.edu.au/study/bachelor-information-technology-bit-2019',
'https://www.cdu.edu.au/study/bachelor-laws-honours-blawh-2019',
'https://www.cdu.edu.au/study/diploma-laws-ylaw01-2019',
'https://www.cdu.edu.au/study/associate-degree-legal-studies-xlest1-2019',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        item = UcasItem()
#1  university
        university = 'Charles Darwin University'

#2  location
        try:
            #location = ''
            location = response.xpath('//*[@id="panel"]/div[1]/div/div[1]/nav/a').extract()
            location = ','.join(location)
            location = remove_tags(location)
            if ',Online' in location:
                location = location.replace(',Online','')
            else:
                pass
            #print(location)
        except:
            location = 'N/A'
            #print(location)

#3  department
        try:
            #department = ''
            department = response.xpath('').extract()[0]
            department = remove_tags(department)
            #print(department)
        except:
            department = ''
            #print(department)

#4  degree_type
        try:
            degree_type = 2
            degree_type = response.xpath('').extract()[0]
            degree_type = remove_tags(degree_type)
            #print(degree_type)
        except:
            degree_type = 'N/A'
            #print(degree_type)

#5  degree_name_en
        try:
            #degree_name_en = ''
            degree_name_en = response.xpath('//h1').extract()[0]
            degree_name_en = remove_tags(degree_name_en)
            #print(degree_name_en)
        except:
            degree_name_en = 'N/A'
            #print(degree_name_en)

#6  degree_overview_en
        try:
            #degree_overview_en = ''
            degree_overview_en = response.xpath('').extract()[0]
            degree_overview_en = remove_tags(degree_overview_en)
            #print(degree_overview_en)
        except:
            degree_overview_en = 'N/A'
            #print(degree_overview_en)

#7  programme_en
        try:
            #programme_en = ''
            programme_en = degree_name_en.replace('Graduate Certificate in ','').replace('Master of ','').replace('Juris Doctor / Graduate Diploma in ','')
            programme_en = remove_tags(programme_en)
            #print(programme_en)
        except:
            programme_en = 'N/A'
            #print(programme_en)

#8  overview_en
        try:
            #overview_en = ''
            overview_en = response.xpath('//*[@id="uon-body"]/div/div/div[1]/div[1]').extract()
            overview_en = ''.join(overview_en)
            overview_en = remove_tags(overview_en,keep=('div','p','ul','li'))
            duoyu = re.findall('div (.*?)>',overview_en)[0]
            overview_en = overview_en.replace(' '+duoyu,'')
            #print(overview_en + response.url)
        except:
            overview_en = 'N/A'
            #print(overview_en)


#9  start_date
        try:
            #start_date = ''
            start_date = response.xpath('//*[@id="panel"]/div[1]/div/div[2]/div[2]/div[1]/div[2]/ul/li').extract()
            start_date = ','.join(start_date)
            start_date = remove_tags(start_date)
            if ',,' in start_date:
                start_date = start_date.replace(',,',',').replace(',,,,',',').replace(',,',',')

            elif start_date =='':
                start_date = 'N/A'
            else:
                pass
            #print(start_date)
        except:
            start_date = 'N/A'
            #print(start_date)

#10 duration
        try:
            #duration = ''
            duration = response.xpath('//*[@id="panel"]/div[1]/div/div[2]/div[2]/div[2]/div[1]/p').extract()[0]
            duration = remove_tags(duration)
            if '2' in duration:
                duration = '2'
            elif '1.5' in duration:
                duration = '1.5'
            elif '0.5' in duration:
                duration = '0.5'
            elif '1' in duration:
                duration = '1'
            elif '3' in duration:
                duration = '3'
            else:
                pass
            #print(duration)
        except:
            duration = 'N/A'
            #print(duration)

 # 11 modules_en
        try:
            # modules_en = ''
            modules_en = response.xpath('//*[@id="what-you-will-study"]/div/div[1]').extract()[0]
            modules_en = remove_tags(modules_en,keep=('div','p','ul','li'))
            duoyu = re.findall('div( .*?)>',modules_en)[0]
            duoyu2 = re.findall('li( data-id="\d\d\d\d\d\d" data-component="")>',modules_en)
            modules_en = modules_en.replace(duoyu,'')
            modules_en = modules_en.replace(duoyu2,'')
            #modules_en = remove_tags(modules_en)
            #print(modules_en)
        except:
            modules_en = 'N/A'
            #print(modules_en)

#12 career_en
        try:
            # career_en = ''
            career_en = response.xpath('//*[@id="career-opportunities"]').extract()[0]
            career_en = remove_tags(career_en)
            career_en = career_en.replace('\n\n','')
            career_en = career_en.replace('\r\n','')
            career_en = '<div>' + career_en + '</div>'

            #print(career_en)
        except:
            career_en = 'N/A'
            #print(career_en)

#13 application_open_date
        try:
            # application_open_date = ''
            application_open_date = response.xpath('').extract()[0]
            application_open_date = remove_tags(application_open_date)
            # print(application_open_date)
        except:
            application_open_date = 'N/A'
            # print(application_open_date)

# 14 application_open_date
        try:
            # application_open_date = ''
            application_open_date = response.xpath('').extract()[0]
            application_open_date = remove_tags(application_open_date)
            # print(application_open_date)

        except:
            deadline = 'N/A'
            # print(deadline)

#15 deadline
        try:
            # deadline = ''
            deadline = response.xpath('').extract()[0]
            deadline = remove_tags(deadline)
            #print(deadline)

        except:
            deadline = 'N/A'
            #print(deadline)

#16 apply_fee
        try:
            # apply_fee = ''
            apply_fee = response.xpath('').extract()[0]
            apply_fee = remove_tags(apply_fee)
            #print(apply_fee)

        except:
            apply_fee = 'N/A'
            #print(apply_fee)

#17 tuition_fee
        try:
            # tuition_fee = ''
            tuition_fee = response.xpath('').extract()[0]
            tuition_fee = remove_tags(tuition_fee)
            # print(tuition_fee)

        except:
            tuition_fee = 'N/A'
            # print(tuition_fee)

#18 rntry_requirements_en
        try:
            # rntry_requirements_en = ''
            rntry_requirements_en = response.xpath('').extract()[0]
            rntry_requirements_en = remove_tags(rntry_requirements_en)
            # print(rntry_requirements_en)

        except:
            rntry_requirements_en = 'N/A'
            # print(rntry_requirements_en)

#19 degree_requirements
        try:
            # degree_requirements = ''
            degree_requirements = response.xpath('').extract()[0]
            degree_requirements = remove_tags(degree_requirements)
            # print(degree_requirements)
            print(response.url)
        except:
            degree_requirements = 'N/A'
            # print(degree_requirements)

# 19 major_requirements
        try:
            # major_requirements = ''
            major_requirements = response.xpath('').extract()[0]
            major_requirements = remove_tags(major_requirements)
            # print(major_requirements)

        except:
            major_requirements = 'N/A'
            # print(major_requirements)

# 20 professional_background
        try:
            # professional_background = ''
            professional_background = response.xpath('').extract()[0]
            professional_background = remove_tags(professional_background)
            # print(professional_background)

        except:
            professional_background = 'N/A'
            # print(professional_background)

# 21 average_score
        try:
            # average_score = ''
            average_score = response.xpath('').extract()[0]
            average_score = remove_tags(average_score)
            # print(average_score)

        except:
            average_score = 'N/A'
            # print(average_score)

# 21 ielts_desc
        try:
            # ielts_desc = ''
            ielts_desc = response.xpath('').extract()[0]
            ielts_desc = remove_tags(ielts_desc)
            # print(ielts_desc)

        except:
            ielts_desc = 'N/A'
            # print(ielts_desc)

# 22 ielts
        try:
            # ielts = ''
            ielts = response.xpath('').extract()[0]
            ielts = remove_tags(ielts)
            # print(ielts)

        except:
            ielts = 'N/A'
            # print(ielts)

# 23 ielts_l
        try:
            # ielts_l = ''
            ielts_l = response.xpath('').extract()[0]
            ielts_l = remove_tags(ielts_l)
            # print(ielts_l)

        except:
            ielts_l = 'N/A'
            # print(ielts_l)

#24 ielts_s
        try:
            # ielts_s = ''
            ielts_s = response.xpath('').extract()[0]
            ielts_s = remove_tags(ielts_s)
            # print(ielts_s)

        except:
            ielts_s = 'N/A'
            # print(ielts_s)

#25 ielts_r
        try:
            # ielts_r = ''
            ielts_r = response.xpath('').extract()[0]
            ielts_r = remove_tags(ielts_r)
            # print(ielts_r)

        except:
            ielts_r = 'N/A'
            # print(ielts_r)

#26 ielts_w
        try:
            # ielts_w = ''
            ielts_w = response.xpath('').extract()[0]
            ielts_w = remove_tags(ielts_w)
            # print(ielts_w)

        except:
            ielts_w = 'N/A'
            # print(ielts_w)

#27 toefl_code
        try:
            # toefl_code = ''
            toefl_code = response.xpath('').extract()[0]
            toefl_code = remove_tags(toefl_code)
            # print(toefl_code)

        except:
            toefl_code = 'N/A'
            # print(toefl_code)

#28 toefl_desc
        try:
            # toefl_desc = ''
            toefl_desc = response.xpath('').extract()[0]
            toefl_desc = remove_tags(toefl_desc)
            # print(toefl_desc)

        except:
            toefl_desc = 'N/A'
            # print(toefl_desc)

#29 toefl
        try:
            # toefl = ''
            toefl = response.xpath('').extract()[0]
            toefl = remove_tags(toefl)
            # print(toefl)

        except:
            toefl = 'N/A'
            # print(toefl)

#30 toefl_l
        try:
            # toefl_l = ''
            toefl_l = response.xpath('').extract()[0]
            toefl_l = remove_tags(toefl_l)
            # print(toefl_l)

        except:
            toefl_l = 'N/A'
            # print(toefl_l)


#31 toefl_s
        try:
            # toefl_s = ''
            toefl_s = response.xpath('').extract()[0]
            toefl_s = remove_tags(toefl_s)
            # print(toefl_s)

        except:
            toefl_s = 'N/A'
            # print(toefl_s)

#32 toefl_r
        try:
            # toefl_r = ''
            toefl_r = response.xpath('').extract()[0]
            toefl_r = remove_tags(toefl_r)
            # print(toefl_r)

        except:
            toefl_r = 'N/A'
            # print(toefl_r)

#33 toefl_w
        try:
            # toefl_w = ''
            toefl_w = response.xpath('').extract()[0]
            toefl_w = remove_tags(toefl_w)
            # print(toefl_w)

        except:
            toefl_w = 'N/A'
            # print(toefl_w)

#34 interview_desc_en
        try:
            # interview_desc_en = ''
            interview_desc_en = response.xpath('').extract()[0]
            interview_desc_en = remove_tags(interview_desc_en)
            # print(interview_desc_en)

        except:
            interview_desc_en = 'N/A'
            # print(interview_desc_en)

#35 portfolio_desc_en
        try:
            # portfolio_desc_en = ''
            portfolio_desc_en = response.xpath('').extract()[0]
            portfolio_desc_en = remove_tags(portfolio_desc_en)
            # print(portfolio_desc_en)

        except:
            portfolio_desc_en = 'N/A'
            # print(portfolio_desc_en)

#36 apply_desc_en
        try:
            # apply_desc_en = ''
            apply_desc_en = response.xpath('').extract()[0]
            apply_desc_en = remove_tags(apply_desc_en)
            # print(apply_desc_en)

        except:
            apply_desc_en = 'N/A'
            # print(apply_desc_en)

#37 apply_documents_en
        try:
            # apply_documents_en = ''
            apply_documents_en = response.xpath('').extract()[0]
            apply_documents_en = remove_tags(apply_documents_en)
            # print(apply_documents_en)

        except:
            apply_documents_en = 'N/A'
            # print(apply_documents_en)

#38 apply_proces_en
        try:
            # apply_proces_en = ''
            apply_proces_en = response.xpath('').extract()[0]
            apply_proces_en = remove_tags(apply_proces_en)
            # print(apply_proces_en)

        except:
            apply_proces_en = 'N/A'
            # print(apply_proces_en)

#39 is_work_experience
        try:
            # is_work_experience = ''
            is_work_experience = response.xpath('').extract()[0]
            is_work_experience = remove_tags(is_work_experience)
            # print(is_work_experience)

        except:
            is_work_experience = 'N/A'
            # print(is_work_experience)

#40 work_experience_years
        try:
            # work_experience_years = ''
            work_experience_years = response.xpath('').extract()[0]
            work_experience_years = remove_tags(work_experience_years)
            # print(work_experience_years)

        except:
            work_experience_years = 'N/A'
            # print(work_experience_years)

#41 work_experience_desc_en
        try:
            # work_experience_desc_en = ''
            work_experience_desc_en = response.xpath('').extract()[0]
            work_experience_desc_en = remove_tags(work_experience_desc_en)
            # print(work_experience_desc_en)

        except:
            work_experience_desc_en = 'N/A'
            # print(work_experience_desc_en)

#42 china_score_requirements
        try:
            # china_score_requirements = ''
            china_score_requirements = response.xpath('').extract()[0]
            china_score_requirements = remove_tags(china_score_requirements)
            # print(china_score_requirements)
        except:
            china_score_requirements = 'N/A'
            # print(china_score_requirements)
        item["university"] = university
        item["location"] = location
        item["department"] = department
        item["degree_type"] = degree_type
        item["degree_name_en"] = degree_name_en
        item["degree_overview_en"] = degree_overview_en
        item["programme_en"] = programme_en
        item["overview_en"] = overview_en
        item["start_date"] = start_date
        item["duration"] = duration
        item["modules_en"] = modules_en
        item["career_en"] = career_en
        item["application_open_date"] = application_open_date
        item["deadline"] = deadline
        item["apply_fee"] = apply_fee
        item["tuition_fee"] = tuition_fee
        item["rntry_requirements_en"] = rntry_requirements_en
        item["degree_requirements"] = degree_requirements
        item["major_requirements"] = major_requirements
        item["professional_background"] = professional_background
        item["average_score"] = average_score
        item["ielts_desc"] = ielts_desc
        item["ielts"] = ielts
        item["ielts_l"] = ielts_l
        item["ielts_s"] = ielts_s
        item["ielts_r"] = ielts_r
        item["ielts_w"] = ielts_w
        item["toefl_code"] = toefl_code
        item["toefl_desc"] = toefl_desc
        item["toefl"] = toefl
        item["toefl_l"] = toefl_l
        item["toefl_s"] = toefl_s
        item["toefl_r"] = toefl_r
        item["toefl_w"] = toefl_w
        item["interview_desc_en"] = interview_desc_en
        item["portfolio_desc_en"] = portfolio_desc_en
        item["apply_desc_en"] = apply_desc_en
        item["apply_documents_en"] = apply_documents_en
        item["apply_proces_en"] = apply_proces_en


        item["url"] = response.url
        item["teach_time"] = 'coursework'
        item["duration_per"] = '1'
        item["apply_pre"] = 'AUD'
        item["tuition_fee_pre"] = 'AUD'
        item["other"] = ''
        item["batch_number"] = ''


# 研究生
        item["is_work_experience"] = is_work_experience
        item["work_experience_years"] = work_experience_years
        item["work_experience_desc_en"] = work_experience_desc_en
# 本科
        #item["china_score_requirements"] = china_score_requirements
        #yield item

