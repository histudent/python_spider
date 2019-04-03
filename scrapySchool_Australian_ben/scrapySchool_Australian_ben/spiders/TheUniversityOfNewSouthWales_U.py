# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_Australian_ben.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_ben.getItem import get_item
from scrapySchool_Australian_ben.getTuition_fee import getTuition_fee
from scrapySchool_Australian_ben.items import ScrapyschoolAustralianBenItem
from scrapySchool_Australian_ben.remove_tags import remove_class
from scrapySchool_Australian_ben.getStartDate import getStartDate
from scrapySchool_Australian_ben.getDuration import getIntDuration


class TheUniversityOfNewSouthWales_USpider(scrapy.Spider):
    name = "TheUniversityOfNewSouthWales_U"
    start_urls = ["http://www.handbook.unsw.edu.au/vbook2018/brProgramsByAtoZ.jsp?StudyLevel=Undergraduate&descr=All"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        links = response.xpath("//tr/td[1]/a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))
#         links = ["http://www.handbook.unsw.edu.au/undergraduate/programs/2018/3564.html",
# "http://www.handbook.unsw.edu.au/undergraduate/programs/2018/3521.html",
# "http://www.handbook.unsw.edu.au/undergraduate/programs/2018/3978.html",
# "http://www.handbook.unsw.edu.au/undergraduate/programs/2018/3588.html", ]
        for url in links:
            # print("--")
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianBenItem)
        item['university'] = "The University of New South Wales"
        # item['country'] = 'Australia'
        # item['website'] = 'http://www.unsw.edu.au/'
        item['url'] = response.url
        item['degree_type'] = 1
        print("===========================")
        print(response.url)
        try:
            department = response.xpath("//div[@class='summary']/p[1]/a[1]//text()").extract()
            item['department'] = ''.join(department).strip()
            print("item['department']: ", item['department'])

            if item['department'] != "UNSW Canberra at ADFA":
                programme = response.xpath("//div[@class='internalContentWrapper']/h1[1]//text()").extract()
                programme = ''.join(programme)
                programme = programme.rsplit("-")
                item['programme_en'] = programme[0].replace("(Honours)", "").replace("(Major)", "").strip()
                print("item['programme_en']: ", item['programme_en'])

                location = response.xpath("//div[@class='summary']/p[3]/text()").extract()
                item['location'] = ''.join(location).strip()
                # print("item['location']: ", item['location'])

                duration = response.xpath("//div[@class='summary']/p[5]/text()").extract()
                clear_space(duration)
                # print("duration: ", duration)
                item['duration'] = ''.join(duration)
                # duration_list = getIntDuration(''.join(duration))
                # if len(duration_list) == 2:
                #     item['duration'] = duration_list[0]
                #     item['duration_per'] = duration_list[-1]
                # print("item['duration']: ", item['duration'])
                # print("item['duration_per']: ", item['duration_per'])

                degree_type = response.xpath("//strong[contains(text(),'Award(s):')]/../following-sibling::p//text()").extract()
                if "View program information for " in degree_type:
                    degree_type.remove("View program information for ")
                if "previous years" in degree_type:
                    degree_type.remove("previous years")
                # print(degree_type)
                item['degree_name'] = '/'.join(degree_type).strip()
                print("item['degree_name']: ", item['degree_name'])

                if item['degree_name'] == "":
                    item['degree_name'] = "Bachelor of " + item['programme_en'].replace("&", "and").strip()
                print("***item['degree_name']: ", item['degree_name'])

                # pro_re = re.findall(r"Bachelor", item['degree_name'].replace("(Honours)", "").replace("(Major)", ""))
                # # print("pre_re: ", pro_re)
                # if len(pro_re) < 2:
                allcontent = response.xpath("//div[@class='internalContentWrapper']//text()").extract()
                # clear_space(allcontent)
                # print("allcontent: ", allcontent)

                overview = response.xpath(
                    "//a[@name='programobjectives']/preceding-sibling::*[position()<last()-4]").extract()
                if len(overview) == 0:
                    overview = response.xpath(
                        "//a[@name='description']/preceding-sibling::*[1]/following-sibling::*[position()<3]").extract()
                item['degree_overview_en'] = remove_class(clear_lianxu_space(overview))
                if item['degree_overview_en'] == "":
                    # print("***over***")
                    # overview
                    if "Program Description" in allcontent:
                        overviewIndex = allcontent.index("Program Description")
                        if "Program Objectives and Graduate Attributes" in allcontent:
                            overviewIndexEnd = allcontent.index("Program Objectives and Graduate Attributes")
                            overview = allcontent[overviewIndex:overviewIndexEnd]
                            item['degree_overview_en'] = "<div>"+clear_lianxu_space(overview)+"</div>"
                # if item['degree_overview_en'] == "":
                #     print("degree_overview_en 是空的")
                item['degree_overview_en'] = item['degree_overview_en'].replace("<div></div>", "").strip()
                # print("item['degree_overview_en']: ", item['degree_overview_en'])

                # modules -- 有些过多，需要删除
                if "Program Structure" in allcontent:
                    modulesIndex = allcontent.index("Program Structure")
                    if "General Education Requirements" in allcontent:
                        modulesIndexEnd = allcontent.index("General Education Requirements")
                    elif "Academic Rules" in allcontent:
                        modulesIndexEnd = allcontent.index("Academic Rules")
                    else:
                        modulesIndexEnd = -1
                    modules = allcontent[modulesIndex:modulesIndexEnd]
                    item['modules_en'] = "<div>" + clear_lianxu_space(modules) + "</div>"
                if item['modules_en'] == "":
                    print("modules_en 是空的")
                # print("item['modules_en']: ", item['modules_en'])

                # degree_description_dict = {'Bachelor of Exercise Physiology': '', 'Bachelor of Science / Bachelor of Education (Secondary)': '', 'Bachelor of Arts': '', 'Bachelor of Music / Bachelor of Education (Secondary)': '', 'Bachelor of International Studies': '', 'Bachelor of Social Research and Policy': '', 'Bachelor of Arts and Business': '', 'Bachelor of Criminology and Criminal Justice': '', 'Bachelor of Social Work (Honours)': '', None: '<li><h2>Overview</h2><div><div><ul><li><h3>Important Information - MUST READ</h3></li><li><h3>Program Structure</h3><ul><li>About the Medicine Program</li><li>Styles of Learning and Teaching</li></ul></li><li><h3>Clinical Learning</h3><ul><li>Clinical Skills</li></ul></li><li><h3>Graduate Capabilities</h3></li><li><h3>Assessment &amp; Progression</h3><ul><li>Progression</li><li>Award of Pass with Distinction</li></ul></li><li><h3>Enrolment</h3></li><li><h3>Contact Us</h3><ul><li>Enquiry Form</li></ul></li><li><h3>NSW Health Requirements</h3></li></ul><div>Close Menu</div></div></div></li><li><h2>Learning Resources</h2><div><div></div></div></li><li><h2>Phase One</h2><div><div><ul><li><h3>Overview</h3><ul><li>Important Information - MUST READ</li></ul></li><li><h3>Courses</h3><ul><li>General Education &amp; extra-Faculty Electives</li></ul></li><li><h3>Assessment &amp; Progression</h3><ul><li>Assignments and Projects</li><li>Exams</li><li>Peer Feedback</li><li>Portfolio Examination</li><li>Progression</li></ul></li><li><h3>Medicine/Arts Program 3856</h3></li><li><h3>Newsletters</h3></li></ul><div>Close Menu</div></div></div></li><li><h2>Phase Two</h2><div><div><ul><li><h3>Overview</h3><ul><li>Important Information - MUST READ</li></ul></li><li><h3>Courses</h3><ul><li>Enrolment</li></ul></li><li><h3>Assessment &amp; Progression</h3><ul><li>Assignments &amp; Projects</li><li>Exams</li><li>Portfolio Examination</li><li>Progression</li></ul></li><li><h3>ILP</h3><ul><li>Roles and Responsibilities</li><li>Assessment Overview</li></ul></li><li><h3>BSc (Med) Honours Program</h3></li><li><h3>Scholarships</h3></li><li><h3>Newsletters</h3></li></ul><div>Close Menu</div></div></div></li><ul><li>Roles and Responsibilities</li><li>Assessment Overview</li></ul><li>Assessment Overview</li><li><h2>Phase Three</h2><div><div><ul><li><h3>Internship</h3></li><li><h3>Elective Term</h3></li><li><h3>Assessment &amp; Progression</h3><ul><li>Course Assessments</li><li>Phase Assessments</li><li>Exams</li><li>Portfolio Examination</li><li>Progression</li></ul></li><li><h3>Overview</h3><ul><li>Important Information - MUST READ</li></ul></li><li><h3>Courses</h3><ul><li>Clinical Pharmacology and Therapeutics</li><li>Investigative Medicine and Biomedical Sciences</li><li>Enrolment</li></ul></li><li><h3>Newsletters</h3></li><li><h3>Exchange to Oslo in Phase 3</h3></li></ul><div>Close Menu</div></div></div></li><li><h3>Overview</h3><ul><li>Important Information - MUST READ</li></ul></li><li><h3>Courses</h3><ul><li>Clinical Pharmacology and Therapeutics</li><li>Investigative Medicine and Biomedical Sciences</li><li>Enrolment</li></ul></li><li><h3>Newsletters</h3></li><li><h3>Exchange to Oslo in Phase 3</h3></li><li><h3>Overview</h3><ul><li>Interface and Navigation Features</li><li>Map</li><li>Timetable</li><li>My Preferences</li><li>eMed Portfolio</li><li>Results</li><li>Feedback</li></ul></li>', 'Bachelor of Media Arts (Honours) / Bachelor of Education (Secondary)': '', 'Bachelor of Fine Arts / Bachelor of Education (Secondary)': '', 'Bachelor of Economics / Bachelor of Education (Secondary)': '', 'Bachelor of Design (Honours) / Bachelor of Education (Secondary)': '', 'Bachelor of Engineering (Honours)\nin Renewable Energy Engineering': '', 'Bachelor of Music /Bachelor of Engineering (Honours)': '', 'Bachelor of Engineering (Honours)\nin Petroleum Engineering': '', 'Bachelor of Engineering (Honours) in Mechatronic Engineering': '', 'Bachelor of Engineering (Honours) / Bachelor of Science': '', 'Bachelor of Engineering (Honours) in Mechanical Engineering': '', 'Bachelor of Engineering (Honours) / Bachelor of Commerce': '', 'Bachelor of Engineering (Honours) in Mining Engineering': '', 'Bachelor of Advanced Science (Hons) / Bachelor of Science (Computer Science)': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Commerce/Bachelor of Science (Computer Science)': '', 'Bachelor of Advanced Science (Hons) / Bachelor of Engineering (Honours)': '', 'Bachelor of Engineering (Honours) in Aerospace Engineering': '', 'Bachelor of Advanced Mathematics (Hons) / Bachelor of Science (Computer Science)': '', 'Bachelor of Advanced Mathematics (Hons) / Bachelor of Engineering (Honours)': '', 'Bachelor of Science (Computer Science) / Bachelor of Media Arts (Hons) ': '', 'Bachelor of Engineering (Honours)\nin Electrical Engineering': '', 'Bachelor of Science (Computer Science)': '', 'Bachelor of Engineering (Honours)\nin Telecommunications Engineering': '', 'Bachelor of Material Science and Engineering (Honours) / Masters of Biomedical Engineering ': '', 'Bachelor of Engineering (Honours)\nin Software Engineering': '', 'Bachelor of Engineering (Honours)\nin Computer Engineering': '', 'Bachelor of Engineering (Honours)\nin Surveying': '', 'Bachelor of Engineering (Honours) in Bioinformatics Engineering': '', 'Bachelor of Social Work (Hons) / Bachelor of Laws': '', 'Bachelor of Engineering (Honours)\nin Environmental Engineering': '', 'Bachelor of Engineering (Civil Engineering with Architecture)': '', 'Bachelor of Social Research & Policy / Bachelor of Laws': '', 'Bachelor of Engineering (Honours) in Industrial Chemistry (N.B. Will be replaced by Chemical Product Engineering from T1 2019)': '', 'Bachelor of Engineering (Honours) in Chemical Engineering': '', 'Bachelor of Science / Bachelor of Laws': '', 'Bachelor of Engineering (Honours)\nin Civil Engineering': '', 'Bachelor of Science (Advanced Mathematics) / Bachelor of Laws': '', 'Bachelor of Science & Business / Bachelor of Laws': '', 'Bachelor of Science (Computer Science) / Bachelor of Laws': '', 'Bachelor of Medicinal Chemistry (Hons) / Bachelor of Laws': '', 'Bachelor of Music / Bachelor of Laws': '', 'Bachelor of Psychology (Hons) / Bachelor of Laws': '', 'Bachelor of Psychological Science / Bachelor of Laws': '', 'Bachelor of Media (Screen & Sound Production) / Bachelor of Laws': '', 'Bachelor of Media (Communication & Journalism) / Bachelor of Laws': '', 'Bachelor of International Studies / Bachelor of Laws': '', 'Bachelor of Economics / Bachelor of Laws': '', 'Bachelor of Engineering (Hons) / Bachelor of Laws': '', 'Bachelor of Fine Arts / Bachelor of Laws': '', 'Bachelor of Criminology & Criminal Justice / Bachelor of Laws': '', 'Bachelor of Media (Public Relations & Advertising) / Bachelor of Laws': '', 'Bachelor of Commerce / Bachelor of Laws': '', 'Bachelor of City Planning (Hons) / Bachelor of Laws': '', 'Bachelor of Arts & Business / Bachelor of Laws': '', 'Bachelor of Advanced Science (Hons) / Bachelor of Laws': '', 'Bachelor of Actuarial Studies / Bachelor of Laws': '', 'Bachelor of Art Theory / Bachelor of Laws': '', 'Bachelor of Psychological Science (Honours)': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Psychological Science': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Science / Bachelor of Social Research and Policy': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Science and Business': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Psychology (Hons)': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Science (International)': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Science / Bachelor of Fine Arts': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Arts / Bachelor of Laws': '', 'Bachelor of Science / Bachelor of Arts': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Science (Honours)': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Science': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Advanced Science (Hons)/Social Research and Policy': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Advanced Science (Hons) / Bachelor of Arts': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Advanced Science (Hons) / Bachelor of Engineering (Hons)': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Advanced Science (Hons)': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Vision Science / Master of Clinical Optometry': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Advanced Science (Hons) / Bachelor of Fine Arts': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Science (Advanced Mathematics) (Hons) / Bachelor of Arts': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Science (Advanced Mathematics) / Bachelor of Science (Computer Science) (Hons)': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Materials Science and Engineering (Hons) / Engineering Science': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Engineering (Hons) in Materials Science and Engineering / Bachelor of Commerce': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Engineering (Hons) in Materials Science and Engineering': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Science (Advanced Mathematics) (Hons)': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Engineering (Hons) (Materials Science and Engineering) / Master of Biomedical Engineering': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Medicinal Chemistry (Hons)': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Biotechnology (Hons)': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Life Sciences': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Environmental Management / Bachelor of Arts': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Commerce / Bachelor of Education (Secondary)': '', 'Bachelor of Environmental Management': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Aviation (Management)': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Aviation (Flying)': '<ul><li>Overview</li><li>Our Dean</li><li>Our Schools</li></ul>', 'Bachelor of Media (Screen and Sound Production)': '', 'Bachelor of Music': '', 'Bachelor of Media (Communication and Journalism)': '', 'Bachelor of Arts / Bachelor of Education (Secondary)': '', 'Bachelor of Media (Public Relations and Advertising)': ''}
                # # degree_description      可能不准
                # # degree_description = response.xpath("//a[@name='academicrules']/preceding-sibling::div[1]").extract()
                # item['degree_overview_en'] = degree_description_dict.get(item['degree_name'])
                # if item['degree_overview_en'] == None:
                #     item['degree_overview_en'] = ""
                #     print("**********degree_overview_en为空")
                # else:
                #     print("item['degree_overview_en']: ", item['degree_overview_en'])

                # IELTS、TOEFL
                if item['degree_name'] == "Bachelor of Education":
                    item["ielts"] = '7.5'
                    item["ielts_l"] = '7'
                    item["ielts_s"] = '7'
                    item["ielts_r"] = '7'
                    item["ielts_w"] = '7'
                    item["toefl"] = '102'
                    item["toefl_l"] = '24'
                    item["toefl_s"] = '23'
                    item["toefl_r"] = '24'
                    item["toefl_w"] = '27'
                elif item['department'] == "Built Environment" or item['department'] == "Faculty of Medicine" or item['department'] == "Faculty of Law":
                    item["ielts"] = '7'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '6'
                    item["toefl"] = '94'
                    item["toefl_l"] = '23'
                    item["toefl_s"] = '23'
                    item["toefl_r"] = '23'
                    item["toefl_w"] = '25'
                else:
                    item["ielts"] = '6.5'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '6'
                    item["toefl"] = '90'
                    item["toefl_l"] = '22'
                    item["toefl_s"] = '22'
                    item["toefl_r"] = '22'
                    item["toefl_w"] = '23'
                print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                        item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))
                print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
                      item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

                item['apply_proces_en'] = """<h4>1</h4><div>Choose your degree Choose your degree from 'Degree areas' in the horizontal bar above or from our international student guides, noting down the degree code. </div><h4>2</h4><div> Check your entry requirements You need to satisfy your chosen degree's entry requirements and UNSW’s English language requirements. If you need help, head to enquiry.unsw.edu.au for assistance. </div><h4>3</h4><div> Submit your application online Submit your application at UNSW Apply Online. Click 'Register now' and fill out your details. Upload your supporting documents and pay your application fee. </div><h4>4</h4><div> Track your application To track your application or upload any additional documents (after you have submitted your application and received a receipt letter), you will need to log in to the Application Tracking Portal. To log in, you will need your UNSW login ID (i.e. 'z1234567') and UniPass. To get your UniPass, please go to UNSW Identity Manager (IDM) and follow the setup instructions using the information in your receipt letter. If you are a recognised UNSW agent you will need login details and permission from your applicant to access their account. It takes up to three weeks for UNSW to assess your application. </div><h4>5</h4><div> We will send you a letter of offer We will send you a full offer if everything is fine or a conditional offer if more steps are required. We will inform you of these steps. </div><h4>6</h4><div> Accept your offer If you received a full offer, you can accept it at gettingstarted.unsw.edu.au. Pay your deposit and you will receive an electronic confirmation of enrolment (eCoE). </div><h4>7</h4><div> Enrol online You can then enrol in your degree and courses online at myUNSW. </div>"""
                # item['rntry_requirements_en'] = ""
                if "Entry Requirements" in allcontent:
                    entryIndex = allcontent.index("Entry Requirements")
                    if "How to Apply" in allcontent:
                        entryIndexEnd = allcontent.index("How to Apply")
                    else:
                        entryIndexEnd = -1
                    entry_requirements = allcontent[entryIndex:entryIndexEnd]
                    item['rntry_requirements_en'] = item['rntry_requirements_en'] + clear_lianxu_space(entry_requirements)
                if item['rntry_requirements_en'] == "":
                    # print("rntry_requirements_en 是空的")
                    item['rntry_requirements_en'] = """<div>UNDERGRADUATE
    There are several admission pathways to an undergraduate degree at UNSW including high school qualifications, UNSW Foundation Studies, UNSW Diploma, recognised prior study or university transfer. Read the academic entry requirements in our International Student Guide for undergraduates or check the Undergraduate direct entry table.</div>"""
                else:
                    item['rntry_requirements_en'] = "<div>"+item['rntry_requirements_en']+"</div>"
                # print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

                # 中国要求高考分数
                p = ["Aviation (Flying)",
    "Science (Advanced Mathematics) (Honours)",
    "Aviation (Management)",
    "Eng (H) (Mtrls Sc & Eng)/Com",
    "Life Sciences",
    "Vision Science",
    "Environmental Management",
    "Psychology (Honours)",
    "Biotechnology (Honours)",
    "Vision Science/Master of Clinical Optometry",
    "Science",
    "Psychological Science",
    "Science (International)",
    "Medicinal Chemistry (Honours)",
    "Science and Business",
    "Medical Science",
    "Data Science and Decisions",
    "Engineering (H) (Materials Science & Engineering)",
    "Eng (H) (Mtrls Sc)/Eng Sci (Chem Eng)",
    "Eng (H) (Mtrls Sc)/Biomed Eng",
    "Advanced Science (Honours)",
    "Art Theory",
    "Design (Honours)",
    "Fine Arts (Honours)",
    "Media Arts (Honours)",
    "Design (Hons)/Media (PR & Advt)",
    "Exercise Physiology",
    "Med MD",
    "International Public Health",
    "Computational Design",
    "Industrial Design (Honours)",
    "Interior Architecture (Honours)",
    "Landscape Architecture (Honours)",
    "City Planning (Honours)",
    "Construction Management & Property",
    "Architectural Studies",
    "Music",
    "Economics/Education (Secondary)",
    "Design (Honours)/Education (Secondary)",
    "Music/Eng",
    "Fine Arts/Education (Secondary)",
    "Music/Advanced Science",
    "Media Arts (Honours)/Education (Secondary)",
    "Commerce/Education (Secondary)",
    "Social Research & Policy",
    "Music/Commerce",
    "Social Work (Honours)",
    "Arts",
    "Arts/Education (Secondary)",
    "Criminology & Criminal Justice",
    "Social Work (Hons)/Criminology & Criminal Justice",
    "Science/Education (Secondary)",
    "Media 2",
    "Music/Media 2",
    "Music/Science",
    "Arts and Business",
    "International Studies",
    "Information Systems",
    "Economics",
    "Commerce",
    "Commerce (International)",
    "Actuarial Studies",
    "Engineering (Honours)",
    "Engineering (H)/Biomed Engineering",
    "Eng (Honours) (Civil)/Surveying",
    "Science (Food Science & Technology)",
    "Computer Science)",
    "Eng (Honours)/Commerce",
    "Engineering (H) (Elec)/Engineering (Elec)",
    "Engineering (Honours) (Civil with Architecture)", ]
                v = ["80",
    "85",
    "80",
    "88",
    "80",
    "88",
    "80",
    "NA",
    "80",
    "NA",
    "80",
    "80",
    "80",
    "83",
    "83",
    "83",
    "85",
    "85",
    "85",
    "85",
    "85",
    "80",
    "80",
    "80",
    "80",
    "80",
    "83",
    "NA",
    "80",
    "80",
    "80",
    "80",
    "80",
    "80",
    "80",
    "88",
    "80",
    "85",
    "80",
    "85",
    "80",
    "85",
    "80",
    "88",
    "80",
    "88",
    "80",
    "80",
    "80",
    "80",
    "80",
    "80",
    "80",
    "80",
    "80",
    "83",
    "83",
    "83",
    "85",
    "88",
    "88",
    "88",
    "85",
    "85",
    "85",
    "85",
    "85",
    "88",
    "88",
    "88", ]
                avgDict = {}
                for i in range(len(p)):
                    avgDict[p[i]] = v[i]
                item['average_score'] = avgDict.get(item['programme_en'])
                if item['average_score'] == "NA":
                    item['average_score'] = ""
                # print("item['average_score']: ", item['average_score'])

                tuition_feeDict = {'Bachelor of Engineering (Honours) in Materials Science and Engineering/Bachelor of Engineering Science': '$46,680', 'Bachelor of Data Science and Decisions': '$45,990', 'Bachelor of Biotechnology': '$46,680', 'Bachelor of Aviation (Management)': '$46,680', 'Bachelor of Advanced Science (Honours)': '$46,680', 'Bachelor of Vision Science/Master of Clinical Optometry': '$46,680', 'Bachelor of Science (International)': '$46,680', 'Bachelor of Science (Honours)': '$46,680', 'Bachelor of Science / Bachelor of Social Research and Policy': '$41,440', 'Bachelor of Aviation (Flying)': '$46,680', 'Diploma of Professional Practice': '$34,700', 'Bachelor of Science and Business': '$45,990', 'Bachelor of Vision Science': '$46,680', 'Bachelor of Planning': '$41,220', 'Bachelor of Interior Architecture (Honours)': '$40,440', 'Bachelor of Industrial Design (Honours)': '$40,440', 'Bachelor of Construction Management and Property (Honours)': '$40,440', 'Bachelor of Computational Design (Honours)': '$40,440', 'Bachelor of Computational Design': '$41,680', 'Bachelor of City Planning (Honours)': '$40,440', 'Bachelor of Architectural Studies (UNSW-Tongji)': '$41,680', 'Bachelor of Architectural Studies': '$41,680', 'Bachelor of Media Arts (Honours)': '$36,940', 'Bachelor of Fine Arts (Honours)': '$36,940', 'Bachelor of Landscape Architecture (Honours)': '$40,440', 'Bachelor of Design (Honours)/Bachelor of Media (PR & Advertising)': '$36,570', 'Bachelor of Design (Honours)': '$36,940', 'Bachelor of Art Theory (Honours)': '$36,940', 'Bachelor of Social Work (Honours)/Bachelor of Laws': '$39,690', 'Bachelor of Social Research and Policy / Bachelor of Laws': '$38,380', 'Bachelor of Construction Management and Property': '$40,440', 'Bachelor of Science (Computer Science)/Bachelor of Laws': '$46,240', 'Bachelor of Science/Bachelor of Laws': '$46,240', 'Bachelor of Science and Business/Bachelor of Laws': '$45,300', 'Bachelor of Science (Advanced Mathematics)(Honours)/Bachelor of Laws': '$46,240', 'Bachelor of Architectural Studies (Honours)': '$41,680', 'Bachelor of Science (Advanced) (Honours) / Bachelor of Laws': '$46,240', 'Bachelor of Psychology (Honours)/Bachelor of Laws': '$45,800', 'Bachelor of Psychological Science /Bachelor of Laws': '$46,240', 'Bachelor of Music/Bachelor of Laws': '$41,440', 'Bachelor of Medicinal Chemistry (Honours)/Bachelor of Laws': '$46,240', 'Bachelor of Media (Screen and Sound Production)/Bachelor of Laws': '$38,380', 'Bachelor of Fine Arts/Bachelor of Arts': '$36,940', 'Bachelor of Media (PR & Advertising)/Bachelor of Laws': '$38,380', 'Bachelor of Media (Communication and Journalism)/Bachelor of Laws': '$38,380', 'Bachelor of Fine Arts/Bachelor of Laws': '$38,940', 'Bachelor of International Studies/Bachelor of Laws': '$39,470', 'Bachelor of Engineering (Honours)/Bachelor of Laws': '$46,240', 'Bachelor of Economics/Bachelor of Laws': '$44,870', 'Bachelor of Commerce (all Majors)/Bachelor of Laws': '$44,870', 'Bachelor of  Criminology and Criminal Justice/Bachelor of Laws': '$38,380', 'Bachelor of City Planning (Honours)/Bachelor of Laws': '$40,440', 'Bachelor of Art Theory/Bachelor of Laws': '$38,940', 'Bachelor of Arts/Bachelor of Laws': '$38,380', 'Bachelor of Arts and Business/Bachelor of Laws': '$40,060', 'Bachelor of Actuarial Studies/Bachelor of Law': '$44,870', 'Bachelor of Medicine/ Bachelor of Surgery (MBBS)': '$73,630', 'Bachelor of Medicine/ Bachelor of Surgery(MBBS)/ Bachelor of Arts': '$73,630', 'Bachelor of Science (Medicine) Honours': '$47,430', 'Bachelor of Medical Studies, Doctor of Medicine/Bachelor of Arts': '$73,630', 'Bachelor of Medical Studies Doctor of Medicine': '$73,630', 'Bachelor of Exercise Physiology': '$46,960', 'Bachelor of Art Theory': '$36,940', 'Bachelor of Information Systems': '$43,930', 'Bachelor of Economics (Honours)': '$43,930', 'Bachelor of Economics/Bachelor of Science (Advanced Mathematics) (Honours)': '$45,300', 'Bachelor of Economics / Bachelor of Science': '$45,300', 'Bachelor of Economics/ Bachelor of Arts': '$40,440', 'Bachelor of Economics/Bachelor of Advanced Science (Honours)': '$45,300', 'Bachelor of Economics (all majors)': '$43,930', 'Bachelor of Art Theory / Bachelor of Social Research and Policy': '$36,570', 'Bachelor of Commerce (International)': '$43,930', 'Bachelor of Commerce (Hons)': '$43,930', 'Bachelor of Commerce/Bachelor of Science (Computer Science)': '$45,650', 'Bachelor of Commerce/Bachelor of Science (Advanced Mathematics) (Honours)': '$45,300', 'Bachelor of Commerce/ Bachelor of Science': '$45,300', 'Bachelor of Commerce/Bachelor of Media (PR & Advertising)': '$40,060', 'Bachelor of Commerce/Bachelor of Information Systems': '$43,930', 'Bachelor of Commerce/Bachelor of Fine Arts': '$40,440', 'Bachelor of Commerce/ Bachelor of Economics': '$43,930', 'Bachelor of Commerce/Bachelor of Design (Honours)': '$40,440', 'Bachelor of Commerce/Bachelor of Aviation (Management)': '$44,960', 'Bachelor of Commerce/ Bachelor of Arts': '$40,060', 'Bachelor of International Public Health': '$23,960', 'Bachelor of Commerce/Bachelor of Advanced Science (Honours)': '$45,300', 'Bachelor of Commerce (all specialisations)': '$43,930', 'Bachelor of Art Theory/Bachelor of Arts': '$36,940', 'Bachelor of Actuarial Studies/Bachelor of Science (Advanced Mathematics) (Honours)': '$45,300', 'Bachelor of Actuarial Studies/Bachelor of Science': '$45,300', 'Bachelor of Actuarial Studies/Bachelor of Economics': '$44,620', 'Bachelor of Actuarial Studies/Bachelor of Commerce': '$44,620', 'Bachelor of Actuarial Studies': '$43,930', 'Diploma in Language Studies (concurrent degree)': '$36,190', 'Bachelor of Social Work (Honours)/Bachelor of Social Research and Policy': '$37,500', 'Bachelor of Social Work (Honours)/Bachelor of Criminology and Criminal Justice': '$37,500', 'Bachelor of Social Work (Honours)/Bachelor of Arts': '$37,500', 'Bachelor of Social Work (Honours)': '$37,500', 'Bachelor of Social Research and Policy (Honours)': '$36,190', 'Bachelor of Social Research and Policy': '$36,190', 'Bachelor of Science - Food Science (Honours Year)': '$46,680', 'Bachelor of Science (Computer Science)/Bachelor of Science': '$46,680', 'Bachelor of Science (Computer Science)/Bachelor of Arts': '$42,750', 'Bachelor of Science (Computer Science)': '$46,680', 'Bachelor of Media Arts (Honours)/Bachelor of Science (Computer Science)': '$46,680', 'Bachelor of Food Science (Honours)': '$46,680', 'Bachelor of Engineering (Honours)/Master of Engineering (Electrical Engineering)': '$46,680', 'Bachelor of Engineering (Honours)/Master of Biomedical Engineering': '$46,680', 'Bachelor of Engineering (Honours)/Bachelor of Surveying': '$46,680', 'Bachelor of Engineering (Honours)/Bachelor of Science (Computer Science)': '$46,680', 'Bachelor of Engineering (Honours)/Bachelor of Science': '$46,680', 'Bachelor of Engineering (Honours)/Bachelor of Engineering Science': '$46,680', 'Bachelor of Engineering (Honours)/Bachelor of Commerce': '$46,680', 'Bachelor of Engineering (Honours)/ Bachelor of Arts': '$46,680', 'Bachelor of Engineering (Honours)': '$46,680', 'Bachelor of Engineering - Civil Engineering with Architecture (Honours)': '$46,680', 'Bachelor of Computer Science (Honours)': '$46,680', 'Bachelor of Science/ Bachelor of Education (Secondary)': '$44,490', 'Bachelor of Music (Honours)/Bachelor of Advanced Science (Honours)': '$42,310', 'Bachelor of Music (Honours)': '$37,940', 'Bachelor of Music / Bachelor of Science': '$42,310', 'Bachelor of Music/Bachelor of Media (Screen and Sound Production)': '$37,070', 'Bachelor of Music/Bachelor of Media (Public Relations and Advertising)': '$37,070', 'Bachelor of Music/Bachelor of Media (Communication and Journalism)': '$37,070', 'Bachelor of Music/Bachelor of Engineering (Honours)': '$42,310', 'Bachelor of Music/Bachelor of Commerce': '$40,940', 'Bachelor of Music/Bachelor of Education(Secondary)': '$37,940', 'Bachelor of Music/Bachelor of Arts': '$37,500', 'Bachelor of Music/Bachelor of Advanced Science (Honours)': '$42,310', 'Bachelor of Music': '$37,940', 'Bachelor of Media (Screen and Sound Production)': '$36,190', 'Bachelor of Media in Public Relations and Advertising': '$36,190', 'Bachelor of International Studies / Bachelor of Media (Screen & Sound Production)': '$36,630', 'Bachelor of International Studies / Bachelor of Media (PR & Advertising)': '$36,630', 'Bachelor of International Studies / Bachelor of Media (Communication and Journalism)': '$36,630', 'Bachelor of International Studies (all specialisations)': '$37,940', 'Bachelor of Fine Arts/Bachelor of Education (Secondary)': '$37,690', 'Bachelor of Education (Secondary) (Honours)': '$37,940', 'Bachelor of Design (Honours)/Bachelor of Education (Secondary)': '$37,190', 'Bachelor of Criminology and Criminal Justice (Honours)': '$36,190', 'Bachelor of Criminology and Criminal Justice': '$36,190', 'Bachelor of Commerce/Bachelor of Education (Secondary)': '$42,430', 'Bachelor of Arts/ Bachelor of Education (Secondary)': '$37,070', 'Bachelor of Arts and Social Sciences (Honours)': '$36,190', 'Bachelor of Arts and Business': '$40,060', 'Bachelor of Arts': '$36,190', 'Bachelor of Economics/Bachelor of Education (Secondary)': '$42,430', 'Bachelor of Science/Bachelor of Fine Arts': '$41,810', 'Bachelor of Science/ Bachelor of Arts': '$41,440', 'Bachelor of Science (Advanced Science)/Bachelor of Science (Computer Science)': '$46,680', 'Bachelor of Science - Advanced Science/ Bachelor of Arts': '$46,680', 'Bachelor of Science (Advanced Mathematics) (Honours)/Bachelor of Science (Computer Science)': '$46,680', 'Bachelor of Media in Communication and Journalism': '$36,190', 'Bachelor of Media (Honours)': '$36,190', 'Bachelor of Media Arts (Honours)/Bachelor of Education (Secondary)': '$37,190', 'Bachelor of Science (Advanced Mathematics) (Honours)/ Bachelor of Arts': '$46,680', 'Bachelor of Science (Advanced Mathematics)(Honours)': '$46,680', 'Bachelor of Science (Advanced)/Bachelor of Social Research and Policy': '$41,440', 'Bachelor of Science (Advanced)/Bachelor of Engineering (Honours)': '$46,680', 'Bachelor of Science': '$46,680', 'Bachelor of Psychology (Honours)': '$46,680', 'Bachelor of Psychology': '$46,680', 'Bachelor of Psychological Science (Honours)': '$46,680', 'Bachelor of Psychological Science': '$46,680', 'Bachelor of Nanoscience (Honours)': '$46,680', 'Bachelor of Medicinal Chemistry (honours)': '$46,680', 'Bachelor of Medical Science': '$46,770', 'Bachelor of Science (Advanced Mathematics) (Honours)/Bachelor of Engineering (Honours)': '$46,680', 'Bachelor of Life Sciences': '$46,680', 'Bachelor of Environmental Management': '$46,680', 'Bachelor of Environmental Management/Bachelor of Arts': '$43,710', 'Bachelor of Engineering (Honours) (Materials Science and Engineering)/Bachelor of Commerce': '$46,680', 'Bachelor of Science (Advanced)/Bachelor of Fine Arts': '$41,810', 'Bachelor of Engineering (Honours) in Materials Science and Engineering': '$46,680', 'Bachelor of Engineering (Honours) in Materials Science and Engineering/Master of Biomedical Engineering': '$46,680'}
                tuition_fee = tuition_feeDict.get(item['degree_name'])
                if tuition_fee != None:
                    tuition_fee = int(tuition_fee.replace(",", "").replace("$", "").strip())
                    item['tuition_fee_pre'] = "$"
                item['tuition_fee'] = tuition_fee
                # print("item['tuition_fee']: ", item['tuition_fee'])

                careerDict = {'Bachelor of Exercise Physiology': '', 'Bachelor of Science / Bachelor of Education (Secondary)': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li>', 'Bachelor of Arts': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li><li>volunteer and paid roles (find out more on the UNSW Careers and Employment website)</li><li>leadership in student organisations</li>', 'Bachelor of Music / Bachelor of Education (Secondary)': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li>', 'Bachelor of International Studies': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li>', 'Bachelor of Social Research and Policy': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li><li>volunteer and paid roles (visit UNSW Careers and Employment)</li><li>leadership in student organisations</li>', 'Bachelor of Arts and Business': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li>', 'Bachelor of Criminology and Criminal Justice': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li>', 'Bachelor of Social Work (Honours)': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li>', None: '', 'Bachelor of Media Arts (Honours) / Bachelor of Education (Secondary)': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li>', 'Bachelor of Fine Arts / Bachelor of Education (Secondary)': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li>', 'Bachelor of Economics / Bachelor of Education (Secondary)': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li>', 'Bachelor of Design (Honours) / Bachelor of Education (Secondary)': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li>', 'Bachelor of Engineering (Honours)\nin Renewable Energy Engineering': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Music /Bachelor of Engineering (Honours)': '<li>Careers</li><li>General Rules &amp; Student Info</li><li>Faculties &amp; Schools</li><li>Class Timetable</li>', 'Bachelor of Engineering (Honours)\nin Petroleum Engineering': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Engineering (Honours) in Mechatronic Engineering': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Engineering (Honours) / Bachelor of Science': '<li>Careers</li><li>General Rules &amp; Student Info</li><li>Faculties &amp; Schools</li><li>Class Timetable</li>', 'Bachelor of Engineering (Honours) in Mechanical Engineering': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Engineering (Honours) / Bachelor of Commerce': '<li>Careers</li><li>General Rules &amp; Student Info</li><li>Faculties &amp; Schools</li><li>Class Timetable</li>', 'Bachelor of Engineering (Honours) in Mining Engineering': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Advanced Science (Hons) / Bachelor of Science (Computer Science)': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Commerce/Bachelor of Science (Computer Science)': '<li>Careers</li><li>General Rules &amp; Student Info</li><li>Faculties &amp; Schools</li><li>Class Timetable</li>', 'Bachelor of Advanced Science (Hons) / Bachelor of Engineering (Honours)': '<li>Careers</li><li>General Rules &amp; Student Info</li><li>Faculties &amp; Schools</li><li>Class Timetable</li>', 'Bachelor of Engineering (Honours) in Aerospace Engineering': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Advanced Mathematics (Hons) / Bachelor of Science (Computer Science)': '<li>Careers</li><li>General Rules &amp; Student Info</li><li>Faculties &amp; Schools</li><li>Class Timetable</li>', 'Bachelor of Advanced Mathematics (Hons) / Bachelor of Engineering (Honours)': '<li>Careers</li><li>General Rules &amp; Student Info</li><li>Faculties &amp; Schools</li><li>Class Timetable</li>', 'Bachelor of Science (Computer Science) / Bachelor of Media Arts (Hons) ': '<li>Careers</li><li>General Rules &amp; Student Info</li><li>Faculties &amp; Schools</li><li>Class Timetable</li>', 'Bachelor of Engineering (Honours)\nin Electrical Engineering': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Science (Computer Science)': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Engineering (Honours)\nin Telecommunications Engineering': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Material Science and Engineering (Honours) / Masters of Biomedical Engineering ': '<li>Careers</li><li>General Rules &amp; Student Info</li><li>Faculties &amp; Schools</li><li>Class Timetable</li>', 'Bachelor of Engineering (Honours)\nin Software Engineering': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Engineering (Honours)\nin Computer Engineering': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Engineering (Honours)\nin Surveying': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Engineering (Honours) in Bioinformatics Engineering': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Social Work (Hons) / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Engineering (Honours)\nin Environmental Engineering': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Engineering (Civil Engineering with Architecture)': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Social Research & Policy / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Engineering (Honours) in Industrial Chemistry (N.B. Will be replaced by Chemical Product Engineering from T1 2019)': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Engineering (Honours) in Chemical Engineering': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Science / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Engineering (Honours)\nin Civil Engineering': '<li>Careers</li><li>Facilities</li><li>Our history</li><li>Professional Accreditation</li><li>Faculty staff</li>', 'Bachelor of Science (Advanced Mathematics) / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Science & Business / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Science (Computer Science) / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Medicinal Chemistry (Hons) / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Music / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Psychology (Hons) / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Psychological Science / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Media (Screen & Sound Production) / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Media (Communication & Journalism) / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of International Studies / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Economics / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Engineering (Hons) / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Fine Arts / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Criminology & Criminal Justice / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Media (Public Relations & Advertising) / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Commerce / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of City Planning (Hons) / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Arts & Business / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Advanced Science (Hons) / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Actuarial Studies / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Art Theory / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Psychological Science (Honours)': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Psychological Science': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Science / Bachelor of Social Research and Policy': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Science and Business': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Psychology (Hons)': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Science (International)': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Science / Bachelor of Fine Arts': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Arts / Bachelor of Laws': '<li>Careers</li><li>About Us</li><li>Careers</li><li>Calendar of dates</li><li><alast leaf menu-mlid-18936">The new curriculum</li><li>UNSW Careers online</li><li>myUNSW</li><li>Cloud Email</li><li>Staff webmail</li><li>Staff only (LEX)</li>', 'Bachelor of Science / Bachelor of Arts': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Science (Honours)': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Science': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Advanced Science (Hons)/Social Research and Policy': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Advanced Science (Hons) / Bachelor of Arts': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Advanced Science (Hons) / Bachelor of Engineering (Hons)': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Advanced Science (Hons)': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Vision Science / Master of Clinical Optometry': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Advanced Science (Hons) / Bachelor of Fine Arts': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Science (Advanced Mathematics) (Hons) / Bachelor of Arts': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Science (Advanced Mathematics) / Bachelor of Science (Computer Science) (Hons)': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Materials Science and Engineering (Hons) / Engineering Science': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Engineering (Hons) in Materials Science and Engineering / Bachelor of Commerce': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Engineering (Hons) in Materials Science and Engineering': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Science (Advanced Mathematics) (Hons)': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Engineering (Hons) (Materials Science and Engineering) / Master of Biomedical Engineering': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Medicinal Chemistry (Hons)': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Biotechnology (Hons)': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Life Sciences': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Environmental Management / Bachelor of Arts': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Commerce / Bachelor of Education (Secondary)': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li>', 'Bachelor of Environmental Management': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Aviation (Management)': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Aviation (Flying)': '<li>Careers &amp; Employment</li><li>Scholarships</li><li>Student Opinions</li><li>Career Planning</li><li>Peer Mentoring</li><li>Graduation</li><li>Useful Links</li><li>Exam Tips</li><li>For Careers Advisors</li>', 'Bachelor of Media (Screen and Sound Production)': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li>', 'Bachelor of Music': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li>', 'Bachelor of Media (Communication and Journalism)': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li>', 'Bachelor of Arts / Bachelor of Education (Secondary)': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li>', 'Bachelor of Media (Public Relations and Advertising)': '<li>Careers &amp; Employment</li><li>Internships</li><li>Peer Mentoring</li><li>Scholarships, Awards &amp; Prizes</li><li>Career Ready Mentoring Program</li><li>Global Citizenship Program</li><li>Career Ready Mentoring Program</li><li>Further Study</li><li>Update Your Details</li><li>Latest News</li><li>Upcoming Events</li>'}
                career = response.xpath("//p[contains(text(),'Career Opportunities')]/../../preceding-sibling::*[1]/following-sibling::*[position()<4]").extract()
                item['career_en'] = remove_class(clear_lianxu_space(career))
                if item['career_en'] == "":
                    item['career_en'] = careerDict.get(item['degree_name'])
                    # if item['career_en'] == None:
                    #     print("career是空的")
                    # else:
                    #     print("item['career_en']: ", item['career_en'])

                item['apply_pre'] = "$"
                item['apply_fee'] = 100

                if "/" not in item['programme_en']:
                    print("===")
                    yield item
        except Exception as e:
            with open("scrapySchool_Australian_ben/error/"+item['university']+str(item['degree_type'])+".txt", 'w', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

