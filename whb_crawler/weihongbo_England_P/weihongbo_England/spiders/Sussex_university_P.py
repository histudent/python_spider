import scrapy
#from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'sussex_university_P'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['https://www.sussex.ac.uk/study/masters/courses/business-management-and-economics/accounting-and-finance-msc',
'https://www.sussex.ac.uk/study/masters/courses/english/contemporary-performance-ma',
'https://www.sussex.ac.uk/study/masters/courses/law-politics-and-sociology/criminal-law-and-criminal-justice-llm',
'https://www.sussex.ac.uk/study/masters/courses/business-management-and-economics/fintech-risk-and-investment-analysis-msc',
'https://www.sussex.ac.uk/study/masters/courses/law-politics-and-sociology/international-commercial-law-llm',
'https://www.sussex.ac.uk/study/masters/courses/law-politics-and-sociology/international-trade-law-llm',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'Sussex University'
        try:
            location = 'Brighton'
            #location = remove_tags(location)
            #print(location)
        except:
            location = None
            #print(location)
        try:
            department = response.xpath('').extract()[0]
            department = remove_tags(department)
            department = department.replace('\n\n', '\n')
            department = department.replace('\r\n', '')
            department = department.replace('   ', '')
            department = department.replace('  ', '')
            department = department.replace('\n', '')
            #department = department.replace('Our Staff', '')
            #print(department)
        except:
            department = None
            #print(department)


        try:
            degree_name = response.xpath('//*[@id="main"]/div[2]/h1').extract()[0]
            degree_name = remove_tags(degree_name)
            #degree_name = degree_name.split()[0]

            #degree_name = re.findall('\((.*)\).*',degree_name)[0]
            #degree_name = re.findall('(.*)                    .*',degree_name)[0]
            #degree_name = re.findall('\((.*)\)',degree_name)[0]
            #degree_name = degree_name.replace('\n',degree_name)
            #degree_name = degree_name.replace(' ','')
            degree_name = re.findall('.*([A-Z][A-Z][A-Z].*)',degree_name)[0]
        #    print(degree_name)
        except:
            degree_name = re.findall('.*([A-Z][A-Z].*)',degree_name)[0]
       #     print(degree_name)

        try:
            degree_overview_en = response.xpath('//h2[contains(text(),"Key information")]/following-sibling::p').extract()
            degree_overview_en  = ''.join(degree_overview_en)
            degree_overview_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_overview_en)
            #print(degree_overview_en)
        except:
            degree_overview_en = None
            #print(degree_overview_en)

        try:
            programme_en = response.xpath('//*[@id="main"]/div[2]/h1').extract()[0]
            programme_en = remove_tags(programme_en)
            programme_en = programme_en.replace(degree_name,'')
            programme_en = programme_en.rstrip(' ')
            #programme_en = programme_en.split()[1]
            #programme_en = re.findall(' (.*)',programme_en)[0]
            #programme_en = programme_en.replace(degree_name,'')
            #programme_en = programme_en.replace('  ','')
            #programme_en = programme_en.replace('\n', '')
            #programme_en = re.findall(('                    '),'')[0]
            #programme_en = re.findall("\(.*\)(.*)",programme_en)[0]
            #programme_en = programme_en.replace('\n','')
            #programme_en = programme_en.replace('  ','')
           # print(programme_en)
        except:
            programme_en = None
           # print(programme_en)

        try:
            overview_en = degree_overview_en
           # overview_en = remove_tags(overview_en)
            #overview_en = re.findall('COURSE OVERVIEW(.*)',overview_en)[0]
           # overview_en = overview_en.replace('  ','')
           # overview_en = overview_en.replace('\n\n','\n')
           # overview_en = overview_en.replace('\n\n','')
           # overview_en = overview_en.replace('\r\n','')
           # overview_en = overview_en.replace('\n','')
           # overview_en = re.findall('COURSE OVERVIEW(.*)Careers',overview_en)[0]
            #overview_en = '<div>' + overview_en + '</div>'

            #overview_en = remove_tags(overview_en)
            #print(overview_en)
        except:
            overview_en = None
            #print(overview_en)


        try:
            start_date = response.xpath('//dt[contains(text(),"Start date:")]/following-sibling::dd[1]').extract()[0]
            start_date = remove_tags(start_date)
            if 'September 2019' in start_date:
                start_date = '2019-09'
            else:
                start_date = None
         #   print(start_date)
        except:
            start_date = None
         #   print(start_date)


        try:
            #modules_en = response.xpath('//div[4]/div/div/div[1]/div[5]/div/div[2]/p').extract()[0]
            modules_en = response.xpath('//h4[contains(text(),"Core modules")]/following-sibling::*').extract()
            modules_en = ''.join(modules_en)
            modules_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',modules_en)

            # overview_en = re.findall('COURSE OVERVIEW(.*)',overview_en)[0]
           # modules_en = modules_en.replace('  ', '')
           # modules_en = modules_en.replace('\n\n', '\n')
           #modules_en = modules_en.replace('\n\n', '')
           # modules_en = modules_en.replace('\r\n', '')
           # modules_en = modules_en.replace('\n', '')
           # modules_en = re.findall('Year 1(.*)in Year 1', modules_en)[0]
           # modules_en = '<div>' + modules_en + '</div>'
         #   print(modules_en)
        except:
            modules_en = None
         #   print(modules_en)



     #   try:
            #degree_requirements = require_chinese_en
          #  degree_requirements = remove_tags(degree_requirements)
            #degree_requirements = degree_requirements.replace('  ','')
            #print(degree_requirements)
      #  except:
         #   d#egree_requirements = ''
            #print(degree_requirements)

        try:
            rntry_requirements_en = response.xpath('//*[@id="tab-content-uk"]').extract()
            rntry_requirements_en = ''.join(rntry_requirements_en)
            rntry_requirements_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',rntry_requirements_en)
           # rntry_requirements_en = remove_tags(rntry_requirements_en)
           # rntry_requirements_en = rntry_requirements_en.replace('\n\n', '')
           # rntry_requirements_en = rntry_requirements_en.replace('\r\n', '')
            #rntry_requirements_en = rntry_requirements_en.replace('\n', '')
           # rntry_requirements_en = rntry_requirements_en.replace('  ','')
           # rntry_requirements_en = re.findall('ENTRY REQUIREMENTS(.*)Visit us',rntry_requirements_en)[0]
            #rntry_requirements_en = "<div>"+rntry_requirements_en+"</div>"

            #rntry_requirements_en =rntry_requirements_en.replace('                                   ','')
         #   print(rntry_requirements_en)
        except:
            rntry_requirements_en = None
          #  print(rntry_requirements_en)

        try:
            professional_background = response.xpath('').extract()
            professional_background = remove_tags(professional_background)
        except:
            professional_background = ''

        try:
            require_chinese_en = response.xpath('//h4[contains(text(),"China")]/following-sibling::table').extract()
            require_chinese_en = ''.join(require_chinese_en)
            require_chinese_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',require_chinese_en)
           # print(require_chinese_en)
        except:
            require_chinese_en = None
            #print(require_chinese_en)

        try:
            ielts_desc = response.xpath('//h4[contains(text(),"IELTS")]/following-sibling::p[1]').extract()[0]
            ielts_desc = remove_tags(ielts_desc)
           # print(ielts_desc)

        except:
            ielts_desc = None
            #print(ielts_desc)
            #print(ielts_desc)

        try:
            #ielts = '6.5'
            #ielts =remove_tags(ielts)
            ielts = re.findall('(\d\.\d)',ielts_desc)[0]
            #ielts =
          #  print(ielts)
        except:
            ielts = None
            #print(ielts)

        try:
          #  ielts_l = '5.5'
            ielts_l = re.findall('(\d\.\d)',ielts_desc)[1]
            #ielts =
         #   print(ielts_l)
            #ielts_l = remove_tags(ielts_l)
        except:
            ielts_l = None
           # print(ielts_l)
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
            toefl_code = '9166'
            #toefl_code = remove_tags(toefl_code)
        except:
            toefl_code = None

        try:
            toefl_desc = response.xpath('//h5[contains(text(),"TOEFL")]/following-sibling::p[1]').extract()
            toefl_desc = ''.join(toefl_desc)
            toefl_desc = remove_tags(toefl_desc)
         #   print(toefl_desc)
        except:
            toefl_desc = None
          #  print(toefl_desc)


        try:
            toefl = re.findall('\d\d',toefl_desc)[0]
           # toefl = remove_tags(toefl)
            #print(toefl)
        except:
            toefl = None
        #    print(toefl)

        try:
            toefl_l = re.findall('\d\d',toefl_desc)[1]
            toefl_l = remove_tags(toefl_l)

        except:
            toefl_l = None

        try:
            toefl_s = re.findall('\d\d',toefl_desc)[3]
           # toefl_s = remove_tags(toefl_s)

        except:
            toefl_s = None

        try:
            toefl_r = re.findall('\d\d',toefl_desc)[2]
           # toefl_r = remove_tags(toefl_r)
        except:
            toefl_r = None

        try:
            toefl_w = re.findall('\d\d',toefl_desc)[4]
           # toefl_w = remove_tags(toefl_w)
         #   print(toefl_w)
        except:
            toefl_w = None
          #  print(toefl_w)

        try:
            interview_desc_en = response.xpath('//*[@id="entry-requirements-accordion-0"]/div[1]').extract()[0]
            interview_desc_en = remove_tags(interview_desc_en)
            interview_desc_en = interview_desc_en.replace('\n\n', '\n')
            interview_desc_en = interview_desc_en.replace('\r\n', '')
            interview_desc_en = interview_desc_en.replace(' ', '')
            interview_desc_en = interview_desc_en.replace('  ', '')
            interview_desc_en = interview_desc_en.replace('\n', '')
            interview_desc_en = "<div>" + interview_desc_en + "</div>"
            #print(interview_desc_en)
        except:
            interview_desc_en = None
            #print(interview_desc_en)
        try:
            work_experience_desc_en = response.xpath('').extract()
            work_experience_desc_en = remove_tags(work_experience_desc_en)
        except:
            work_experience_desc_en = None

        try:
            portfolio_desc_en = response.xpath('').extract()
            portfolio_desc_en = remove_tags(portfolio_desc_en)
        except:
            portfolio_desc_en = None

        try:
            career_en = response.xpath('//h2[contains(text(),"Careers")]/following-sibling::*').extract()
            career_en = ''.join(career_en)
            career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',career_en)
         #   career_en = career_en.replace('  ','')
           # career_en = career_en.replace('\n','')
          #  career_en = "<div><span>" + career_en + "</span></div>"
         #   print(career_en)
        except:
            career_en = None
        #    print(career_en)
        try:
            apply_desc_en = '<div>Most applications for Masters courses are made directly to Sussex through the postgraduate application system.https://www.sussex.ac.uk/study/masters/apply/log-into-account</div>'
            #apply_desc_en = remove_tags(apply_desc_en)
            #apply_desc_en = "<div>" + apply_desc_en + "</div>"
            #print(apply_desc_en)
        except:
            apply_desc_en = None

        try:
            apply_documents_en = None
            #apply_documents_en = remove_tags(apply_documents_en)
        except:
                apply_documents_en = None


        apply_fee = 0


        #other = ''
        try:
            apply_proces_en = response.xpath('').extract()
        except:
            apply_proces_en = ''


        try:
            duration = 1
            #duration = remove_tags(duration)
            #duration = remove_tags(duration)
            #duration = re.findall('(\d) Years',duration)[0]
            # if '36' in duration:
            #     duration = '3'
            # elif '16' in duration:
            #     duration = '1'
            # elif '12' in duration:
            #     duration = '1'
            # elif '3' in duration:
            #     duration = '3'
            # elif '2' in duration:
            #     duration = '2'
            # elif '1' in duration:
            #     duration = '1'
            # elif 'two' in duration:
            #     duration = '2'
            # else:
            #     duration = '1'
            # #print(duration)
        except:
            duration = 0
            #print(duration)



        try:
            other = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/a').extract()[0]
            other = remove_tags(other)
            #print('成功'+ other + response.url)
        except:
            other = ''
           #print('失败' + other)




        try:
            tuition_fee = response.xpath('//dt[contains(text(),"International students")]/following-sibling::dd').extract()[0]
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = tuition_fee.replace(',','').replace(' per year','').replace('£','')
            # tuition_fee = tuition_fee.replace('£','')
            # tuition_fee = tuition_fee.replace(',','')
            # tuition_fee = tuition_fee.replace('*','')
            # tuition_fee = tuition_fee.replace(' ','')
            # tuition_fee = tuition_fee.replace('\r\n','')
            # tuition_fee = tuition_fee.replace('\n','')
            #
            # tuition_fee = re.findall('(\d\d\d\d\d)',tuition_fee)[0]

            # tuition_fee = tuition_fee.replace('  ','')
            # tuition_fee = tuition_fee.replace('\n','')
            # tuition_fee = re.findall('Full-time international students: £(.*) paStudents',tuition_fee)[0]
            # tuition_fee = int(tuition_fee)
            print(tuition_fee)
        except:
            tuition_fee = None
            print(tuition_fee)
        item["assessment_en"] = None
        item["university"] = university
        item["location"] = location
        item["department"] = department
        item["degree_type"] = 2
        item["degree_name"] = degree_name
#        item["degree_overview_en"] = degree_overview_en
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
        item["degree_requirements"] = require_chinese_en
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
        item["batch_number"] = 22
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
        item["require_chinese_en"] = require_chinese_en
        #item["apply_pre"] = ''
        yield item


