import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'Glasgow_Caledonian_University_P'
    allowed_domains = []
    base_url= 'https://www.gcu.ac.uk%s'
    start_urls = []
    C = ['/study/courses/details/index.php/P03031/3D_Design_for_Virtual_Environments?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03185/Accounting_Finance_and_Regulation?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02765/Advanced_Internetwork_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03194/Advanced_Practice?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02839/Advanced_Practice_in_District_Nursing_with_Specialist_Practitioner_Qualification?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00927/Applied_Instrumentation_and_Control?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02860/Big_Data_Technologies?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00934/Biomolecular_and_Biomedical_Sciences?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00931/Building_Services_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02846/Climate_Justice?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02247/Clinical_Microbiology?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00682/Counselling_Psychology?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02638/Diabetes_Care_and_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02406/Diagnostic_Imaging?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03131/Doctor_of_Physiotherapy_Pre_registration_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02841/Education_in_Academic_and_Practice_Settings?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03118/Electrical_Power_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02519/Electrical_and_Electronic_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03013/Environmental_Management_Waste_Energy_Water_Oil_and_Gas_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02906/Fashion_Business_Creation?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03204/Fashion_and_Lifestyle_Marketing?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00968/Food_Bioscience?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00974/Forensic_Psychology?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02904/Global_Marketing?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03129/Health_Psychology?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00422/Human_Resource_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/NYC3/Impact_Focused_Business_and_Investing?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02585/International_Banking_Finance_and_Risk_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03184/International_Banking_Finance_and_Risk_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03178/International_Business_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02563/International_Fashion_Marketing?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/NYC1/International_Fashion_Marketing?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03181/International_Fashion_Marketing?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02901/International_Management_and_Business_Development?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03182/International_Operations_and_Supply_Chain_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02101/International_Project_Management_Construction_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00992/International_Project_Management_Energy_Construction_Management_Oil_and_Gas_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03179/International_Tourism_and_Events_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03112/Investigative_Ophthalmology_and_Vision_Research?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02900/Luxury_Brand_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02902/Luxury_Brand_Marketing?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03180/Marketing?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03209/Master_of_Public_Health?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03212/Master_of_Public_Health?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/MBA/Masters_of_Business_Administration?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03042/Masters_of_Research?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P01005/Mechanical_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00720/Multimedia_Journalism?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02885/Nursing_Studies_Adult_Pre_registration_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02886/Nursing_Advancing_Professional_Practice?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P01027/Occupational_Therapy_pre_reg_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P01033/Pharmacology?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02388/Physiotherapy?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P01658/Physiotherapy_Pre_registration_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P01630/Psychology_Conversion_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02100/Quantity_Surveying?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02993/Quantity_Surveying?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02574/Risk_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03187/Risk_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/NYC2/Risk_Resilience_and_Integrity_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03183/Social_Business_and_Microfinance?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P01056/Social_Work?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P01233/Specialist_Community_Public_Health_Nursing?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03130/Sports_and_Exercise_Psychology?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P01634/Television_Fiction_Writing?utm_medium=web&utm_campaign=courselisting',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'Glasgow Caledonian University'
        try:
            location = response.xpath('//*[@id="Studyoptions"]/div/section/div[2]/div/div/div/section/section/article/div[5]/span').extract()[0]
            location = remove_tags(location)
            #print(location)
        except:
            location = 'N/A'
            #print(location)
        try:
            department = response.xpath('//ul[@class="course-department"]').extract()[0]
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
            degree_name = response.xpath('//*[@id="MainMiddleWrap"]/article/section/header/h2/div/span[2]').extract()[0]
            degree_name = remove_tags(degree_name)
            degree_name = degree_name.split()[0]

            #degree_name = re.findall('(.*)\n.*',degree_name)[0]
            #degree_name = re.findall('(.*)                    .*',degree_name)[0]
            #degree_name = re.findall('\((.*)\)',degree_name)[0]
            #degree_name = degree_name.replace('\n',degree_name)
            degree_name = degree_name.replace(' ','')
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
            programme_en = response.xpath('//*[@id="MainMiddleWrap"]/article/section/header/h2/div/span[2]').extract()[0]
            programme_en = remove_tags(programme_en)
            #programme_en = re.findall(' (.*)',programme_en)[0]
            programme_en = programme_en.replace(degree_name,'')
            programme_en = programme_en.replace('  ','')
            #programme_en = programme_en.replace('\n', '')
            #programme_en = re.findall(('                    '),'')[0]
            #programme_en = re.findall("(.*)\(.*\)",programme_en)[0]
            #programme_en = programme_en.replace('\n','')
            #programme_en = programme_en.replace('  ','')
            #print(programme_en)
        except:
            programme_en = 'N/A'
            #print(programme_en)

        try:
            overview_en = response.xpath('//*[@id="MainMiddleWrap"]/article/section/section/section[1]/div/div/div').extract()[0]
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
            start_date = response.xpath('//*[@id="Studyoptions"]/div/section/div[2]/div/div/div/section/section/article/div[4]').extract()[0]
            start_date = remove_tags(start_date)
            if 'Jan' in start_date:
                start_date = '1'
            elif 'Sep' in start_date:
                start_date = '9'

            elif 'Oct' in start_date:
                start_date = '10'
            else:
                start_date = '9'
            #print(start_date)
        except:
            start_date = 'N/A'
            #print(start_date)


        try:
            modules_en = response.xpath('//*[@id="Whatyouwillstudy"]/div/div/div').extract()[0]
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
            rntry_requirements_en = response.xpath('//*[@id="Entryrequirements"]/div/div/div').extract()[0]
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
            require_chinese_en = '<p>4-year Bachelor\'s Degree (minimum 70%; for MSc Management 60% can be considered) 3-year Junior College plus 2-year undergraduate degree can be considered</p>'
        except:
            require_chinese_en = ''
        try:
            ielts_desc = ''
            #print(ielts_desc)

        except:
            ielts_desc = 'N/A'

            #print(ielts_desc)

        try:
            ielts_b = response.xpath('//*[@id="Entryrequirements"]/div/div/div').extract()[0]
            ielts =remove_tags(ielts_b)
            ielts = re.findall('IELTS(.*)',ielts_b)[0]
            ielts = re.findall('(\d\.\d)',ielts)[0]
            print(ielts + "1")

        except:

            ielts = 'N/A'
            #print(ielts)
        try:
            ielts_l = re.findall('(\d\.\d)', ielts_b)[1]
            print(ielts_l + "2")
            #ielts_l = remove_tags(ielts_l)
        except:
            ielts_l = 'N/A'

        try:
            ielts_s = ielts_l

        except:
            ielts_s = 0

        try:
            ielts_r = ielts_l
        except:
            ielts_r = 0

        try:
            ielts_w = ielts_l
        except:
            ielts_w = 0

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
            career_en = response.xpath('//*[@id="your-future-career-5"]/div[1]/div').extract()[0]
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
            apply_desc_en = 'Apply Online'
            #apply_desc_en = remove_tags(apply_desc_en)
            #apply_desc_en = "<div>" + apply_desc_en + "</div>"
            #print(apply_desc_en)
        except:
            apply_desc_en = ''

        try:
            apply_documents_en = '<div>Statement of Purpose Your personal statement is an extremely important aspect of the application. It gives you with the opportunity to share with the university your motivations, background and reasons for applying for this particular course. What we look for in a personal statement Letters of Reference Letters of reference provide the university with additional evidence of your ability to successfully complete your programme of study. Upload or attach your letters of reference to your application, or ask your referees to submit this information directly at applications@gcu.ac.uk. What we look for in letters of reference Academic and Professional Certificates Certificates show us what you have already achieved in your previous academic study as well as any CPD during your employment. What we look for in certificates Academic Transcripts Academic transcripts provide the university with full details of the modules you studied at undergraduate level. What we look for in academic transcripts Passport (International Applicants Only) Please provide a photocopy of your passport identification pages.</div>'
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
            duration =  response.xpath('//*[@id="Studyoptions"]/div/section/div[2]/div/div/div/section/section/article/div[3]/span').extract()[0]
            duration = remove_tags(duration)
            #duration = remove_tags(duration)
            #duration = re.findall('(\d) Years',duration)[0]
            if '36' in duration:
                duration = '3'
            elif '16' in duration:
                duration = '1'
            elif '12' in duration:
                duration = '1'
            elif '3' in duration:
                duration = '3'
            elif '2' in duration:
                duration = '2'
            elif '1' in duration:
                duration = '1'
            #print(duration)
        except:
            duration = '0'
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
            tuition_fee = response.xpath('//*[@id="Feesandfunding"]/div/div/div/p[3]').extract()[0]
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
            assessment_en = response.xpath('//*[@id="Assessmentmethods"]/div/div/div').extract()[0]
            assessment_en = remove_tags(assessment_en)
            #assessment_en = assessment_en.replace('\n','')
            assessment_en = assessment_en.replace('\r\n','')
            assessment_en = assessment_en.replace('  ','')
            assessment_en = "<div><span>" + assessment_en + "</span></div>"
            #print(assessment_en)

        except:
            assessment_en = 'N/A'
            #print(assessment_en)

        try:
            teach_time = response.xpath('//*[@id="Studyoptions"]/div/section/div[2]/div/div/div/section/section/article/div[2]').extract()[0]
            teach_time = remove_tags(teach_time)
            if 'full' in teach_time:
                teach_time = 'fulltime'
            elif 'Full' in teach_time:
                teach_time = 'fulltime'
            else:
                teach_time = 'parttime'
            print(teach_time)
        except:
            teach_time = 'N/A'
            print(teach_time)

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
        #item["alevel"] = alevel
        #item["ib"] = ib
        #item["ucascode"] = ucascode
        item["rntry_requirements"] = rntry_requirements_en
        item["require_chinese_en"] = require_chinese_en
        item["assessment_en"] = assessment_en
        item["teach_time"] = teach_time
        item["teach_type"] = teach_type
        #item["apply_pre"] = ''
        yield item


