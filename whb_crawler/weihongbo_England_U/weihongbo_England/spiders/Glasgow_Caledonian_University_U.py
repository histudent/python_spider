import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'Glasgow_Caledonian_University_U'
    allowed_domains = []
    base_url= 'https://www.gcu.ac.uk%s'
    start_urls = []
    C = ['/study/courses/details/index.php/P02961/3D_Animation_and_Visualisation?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02708/Accountancy?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02967/Accountancy_Pathway?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00227/Applied_Biomedical_Science_Biomedical_Science?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02651/Applied_Psychology?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02896/Audio_Technology?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02711/Bachelor_of_Laws?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02477/Bachelor_of_Laws_Fast_track?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02749/Bachelor_of_Laws_with_Risk?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02307/Building_Services_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00231/Building_Surveying?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02979/Building_Surveying_Pathway?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02693/Business_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00295/Cell_and_Molecular_Biology?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02969/Cell_and_Molecular_Biology_Pathway?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02850/Computer_Games_Art_and_Animation_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P01628/Computer_Games_Design_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02769/Computer_Games_Indie_Development_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00265/Computer_Games_Software_Development_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03120/Computer_Networking?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02359/Computer_Aided_Mechanical_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02445/Computer_Aided_Mechanical_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03195/Computer_Aided_Mechanical_Engineering_Pathway?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02768/Computing?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00242/Construction_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02977/Construction_Management_Pathway?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02276/Cyber_Security_and_Networks?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02973/Cyber_Security_and_Networks_Pathway?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P01640/Diagnostic_Imaging?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02793/Digital_Design_Graphics_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02274/Digital_Security_and_Forensics?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02447/Electrical_Power_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00109/Electrical_Power_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02975/Electrical_Power_Engineering_Pathway?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02866/Electrical_and_Electronic_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02868/Electrical_and_Electronic_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02976/Electrical_and_Electronic_Engineering_Pathway?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02517/Electrical_Electronic_and_Energy_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02536/Electrical_Electronic_and_Energy_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00237/Environmental_Civil_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02314/Environmental_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02709/Finance_Investment_and_Risk?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/p02709p/Finance_Investment_and_Risk_Pathway?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02924/Fire_Risk_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02899/Fire_Risk_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00262/Food_Bioscience?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02970/Food_Bioscience_Pathway?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00260/Forensic_Investigation?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02800/Health_and_Safety_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02767/Health_Safety_and_Environmental_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00268/Human_Nutrition_and_Dietetics?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00280/IT_Management_for_Business?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02696/International_Business?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02697/International_Business_and_Human_Resource_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02702/International_Business_and_Tourism_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02700/International_Business_with_Languages?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02601/International_Events_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02966/International_Events_Management_Pathway?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02694/International_Fashion_Branding?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02602/International_Fashion_Business?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02611/International_Marketing?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02596/International_Sports_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02600/International_Supply_Chain_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02446/Mechanical_Systems_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02483/Mechanical_Systems_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02448/Mechanical_and_Power_Plant_Systems?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02481/Mechanical_and_Power_Plant_Systems?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02705/Media_and_Communication?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00322/Microbiology?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02971/Microbiology_Pathway?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02706/Multimedia_Journalism?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02272/Networked_Systems_Engineering?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02876/Nursing_Studies_Adult_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02880/Nursing_Studies_Adult_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02877/Nursing_Studies_Child_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02881/Nursing_Studies_Child_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02884/Nursing_Studies_Dual_Registration_Learning_Disability_Child_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02878/Nursing_Studies_Learning_Disability_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02882/Nursing_Studies_Learning_Disability_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02879/Nursing_Studies_Mental_Health_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02883/Nursing_Studies_Mental_Health_?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00307/Occupational_Therapy?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00305/Optometry?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02679/Oral_Health_Science?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02367/Orthoptics?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P03109/Paramedic_Science?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00340/Pharmacology?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02972/Pharmacology_Pathway?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00310/Physiotherapy?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00308/Podiatry?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02627/Professional_Studies_in_Nursing?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02630/Professional_Studies_in_Nursing?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00318/Quantity_Surveying?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02978/Quantity_Surveying_Pathway?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P01641/Radiotherapy_and_Oncology?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02997/Real_Estate?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02710/Risk_Management?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02704/Social_Sciences?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P00088/Social_Work?utm_medium=web&utm_campaign=courselisting',
'/study/courses/details/index.php/P02655/Software_Development_for_Business?utm_medium=web&utm_campaign=courselisting',]

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
            start_date = '9'

            #print(start_date)
        except:
            start_date = ''


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
            duration =  response.xpath('//*[@id="Studyoptions"]').extract()[0]
            duration = remove_tags(duration)
            #duration = remove_tags(duration)
            #duration = re.findall('(\d) Years',duration)[0]


            if '4' in duration:
                duration = '4'
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
            ib = response.xpath('//*[@id="Entryrequirements"]/div/div/div/dl[1]/dd[4]').extract()[0]
            ib = remove_tags(ib)
            #print(ib)
        except:
            ib = ''
            #print(ib)

        try:
            alevel = response.xpath('//*[@id="Entryrequirements"]/div/div/div/dl[1]/dd[2]').extract()[0]
            alevel = remove_tags(alevel)
            #alevel = re.findall("(\w\w\w) at A Level",alevel)[0]
            #print(alevel)
        except:
            alevel = 'N/A'
            #print(alevel)
        try:
            ucascode = response.xpath('//*[@id="Studyoptions"]/div/section[1]/div[2]/div/div/div/section/section/article/div[6]/span').extract()[0]
            ucascode = remove_tags(ucascode)
            ucascode = ucascode.replace(' ','')

            #print(ucascode)
        except:
            ucascode = ''
            #print(ucascode)

        try:
            tuition_fee = response.xpath('//*[@id="Feesandfunding"]/div/div/div').extract()[0]
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
            tuition_fee = 11500
            #print(tuition_fee)

        try:
            assessment_en = response.xpath('//*[@id="Assessmentmethods"]|//*[@id="AssessmentMethods"]/div/div/div').extract()[0]
            assessment_en = remove_tags(assessment_en)
            #assessment_en = assessment_en.replace('\n','')
            assessment_en = assessment_en.replace('\r\n','')
            assessment_en = assessment_en.replace('  ',' ')
            assessment_en = assessment_en.replace('                                      ','')
            assessment_en = assessment_en.replace('                                  ','')
            assessment_en = "<div><span>" + assessment_en + "</span></div>"
            #print(assessment_en)

        except:
            assessment_en = 'N/A'
            #print(assessment_en)
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
        item["assessment_en"] = assessment_en
        #item["apply_pre"] = ''
        yield item


