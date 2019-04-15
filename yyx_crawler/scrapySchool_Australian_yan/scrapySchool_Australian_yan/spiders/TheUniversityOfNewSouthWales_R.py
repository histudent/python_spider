# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_Australian_yan.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_yan.getItem import get_item
from scrapySchool_Australian_yan.getTuition_fee import getTuition_fee
from scrapySchool_Australian_yan.items import ScrapyschoolAustralianYanItem
from scrapySchool_Australian_yan.remove_tags import remove_class
from scrapySchool_Australian_yan.getStartDate import getStartDate
from scrapySchool_Australian_yan.getDuration import getIntDuration

class TheUniversityOfNewSouthWales_RSpider(scrapy.Spider):
    name = "TheUniversityOfNewSouthWales_R"
    start_urls = ["http://www.handbook.unsw.edu.au/vbook2018/brProgramsByAtoZ.jsp?StudyLevel=Research&descr=All"]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        links = response.xpath("//html//tr/td[1]/a/@href").extract()
        print(len(links))
        start_urls = list(set(links))
        print(len(links))
        for url in links:
            # print("--")
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianYanItem)
        item['university'] = "The University of New South Wales"
        # item['country'] = 'Australia'
        # item['website'] = 'http://www.unsw.edu.au/'
        item['url'] = response.url
        item['degree_type'] = 3
        item['teach_time'] = 'research'
        print("===========================")
        print(response.url)
        try:
            programme = response.xpath("//div[@class='internalContentWrapper']/h1[1]//text()").extract()
            programme = ''.join(programme)
            programme = programme.split("-")
            item['programme_en'] = programme[0].strip()
            print("item['programme_en']: ", item['programme_en'])

            department = response.xpath("//div[@class='summary']/p[1]/a[1]//text()").extract()
            item['department'] = ''.join(department).strip()
            print("item['department']: ", item['department'])

            location = response.xpath("//div[@class='summary']/p[3]/text()").extract()
            item['location'] = ''.join(location).strip()
            # print("item['location']: ", item['location'])

            duration = response.xpath("//div[@class='summary']/p[5]/text()").extract()
            clear_space(duration)
            print("duration: ", duration)
            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            print("item['duration']: ", item['duration'])
            print("item['duration_per']: ", item['duration_per'])

            degree_type = response.xpath(
                "//strong[contains(text(),'Award(s):')]/../following-sibling::p//text()").extract()
            if "View program information for " in degree_type:
                degree_type.remove("View program information for ")
            if "previous years" in degree_type:
                degree_type.remove("previous years")
            # print(degree_type)
            item['degree_name'] = '/'.join(degree_type).strip()
            print("item['degree_name']: ", item['degree_name'])

            allcontent = response.xpath("//div[@class='internalContentWrapper']//text()").extract()
            # clear_space(allcontent)
            # print("allcontent: ", allcontent)

            overview = response.xpath(
                "//a[@name='programobjectives']/preceding-sibling::*[position()<last()-4]").extract()
            if len(overview) == 0:
                overview = response.xpath(
                    "//a[@name='description']/preceding-sibling::*[1]/following-sibling::*[position()<3]").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            if item['overview_en'] == "":
                print("***over***")
                # overview
                if "Program Description" in allcontent:
                    overviewIndex = allcontent.index("Program Description")
                    if "Program Objectives and Graduate Attributes" in allcontent:
                        overviewIndexEnd = allcontent.index("Program Objectives and Graduate Attributes")
                        overview = allcontent[overviewIndex:overviewIndexEnd]
                        item['overview_en'] = "<div>" + clear_lianxu_space(overview) + "</div>"
            # print("item['overview_en']: ", item['overview_en'])

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
            # print("item['modules_en']: ", item['modules_en'])

            # degree_description      可能不准
            degree_description = response.xpath("//a[@name='academicrules']/preceding-sibling::div[1]").extract()
            item['degree_overview_en'] = remove_class(clear_lianxu_space(degree_description))
            print("item['degree_overview_en']: ", item['degree_overview_en'])

            # IELTS、TOEFL
            if item['department'] == "Faculty of Law":
                item["ielts"] = "7"
                item["ielts_l"] = "6.5"
                item["ielts_s"] = "6.5"
                item["ielts_r"] = "6.5"
                item["ielts_w"] = "7"
                item["toefl"] = "96"
                item["toefl_l"] = "23"
                item["toefl_s"] = "23"
                item["toefl_r"] = "23"
                item["toefl_w"] = "27"
            elif item['department'] == "UNSW Business School":
                item["ielts"] = "7"
                item["ielts_l"] = "6.5"
                item["ielts_s"] = "6.5"
                item["ielts_r"] = "6.5"
                item["ielts_w"] = "7"
                item["toefl"] = "96"
                item["toefl_l"] = "23"
                item["toefl_s"] = "23"
                item["toefl_r"] = "23"
                item["toefl_w"] = "27"
            elif "Master of Teaching" in item['degree_name']:
                item["ielts"] = "7.5"
                item["ielts_l"] = "8"
                item["ielts_s"] = "8"
                item["ielts_r"] = "7"
                item["ielts_w"] = "7"
                item["toefl"] = "102"
                item["toefl_l"] = "28"
                item["toefl_s"] = "26"
                item["toefl_r"] = "24"
                item["toefl_w"] = "27"
            elif "Master of Psychology" in item['degree_name']:
                item["ielts"] = "7"
                item["ielts_l"] = "7"
                item["ielts_s"] = "7"
                item["ielts_r"] = "7"
                item["ielts_w"] = "7"
                item["toefl"] = "94"
                item["toefl_l"] = "24"
                item["toefl_s"] = "23"
                item["toefl_r"] = "24"
                item["toefl_w"] = "27"
            else:
                item["ielts"] = "6.5"
                item["ielts_l"] = "6"
                item["ielts_s"] = "6"
                item["ielts_r"] = "6"
                item["ielts_w"] = "6"
                item["toefl"] = "90"
                item["toefl_l"] = "22"
                item["toefl_s"] = "22"
                item["toefl_r"] = "22"
                item["toefl_w"] = "23"

            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))
            # print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
            #       item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))
            # item['application_open_date'] = "30 November 2017    31 May 2018"
            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<div class="checklistitem-inner"> <div class="checklistitem-content"> <div class="checklistitem-content-copy rte"> <h5>Find a research area</h5> <p>You need to satisfy minimum eligibility requirements for your proposed postgraduate research program. You also need to match your area of interest to one of our faculties. Visit the <a href="https://research.unsw.edu.au/">Graduate Research School website</a> for more.</p> </div> </div> </div> </div> <div class="checklistitem "> <div class="checklistitem-number "> <div class="checklistitem-number-inner" data-list-item-number="554">2</div> </div> <div class="checklistitem-inner"> <div class="checklistitem-content"> <div class="checklistitem-content-copy rte"> <h5>Find a supervisor and develop a research description</h5> <p>Most faculties require researchers to secure an agreement for supervision prior to the submission of a formal application. Descriptions of your research interest should be around one page in length.</p> </div> </div> </div> </div> <div class="checklistitem "> <div class="checklistitem-number "> <div class="checklistitem-number-inner" data-list-item-number="555">3</div> </div> <div class="checklistitem-inner"> <div class="checklistitem-content"> <div class="checklistitem-content-copy rte"> <h5>Prepare your documentation</h5> <p>All documents must be in English or include a certified English translation. Scanned copies are sufficient.</p> </div> </div> </div> </div> <div class="checklistitem "> <div class="checklistitem-number "> <div class="checklistitem-number-inner" data-list-item-number="556">4</div> </div> <div class="checklistitem-inner"> <div class="checklistitem-content"> <div class="checklistitem-content-copy rte"> <h5>Submit your application</h5> <p>Submit your application at <a href="https://apply.unsw.edu.au/">UNSW Apply Online</a>. Click 'Register now' and fill out your details. You will receive an ID and password to log in. After logging in, go to 'My Applications' and follow the directions. Please submit only one application. You can apply for scholarships within your application.</p> </div> </div> </div> </div> <div class="checklistitem "> <div class="checklistitem-number "> <div class="checklistitem-number-inner" data-list-item-number="557">5</div> </div> <div class="checklistitem-inner"> <div class="checklistitem-content"> <div class="checklistitem-content-copy rte"> <h5>Track your application</h5> <p>After submitting your application, you will be emailed a confirmation receipt with your UNSW Student ID and a list of any outstanding documentation. You can track the progress of your application through <a href="https://my.unsw.edu.au/" target="_blank">myUNSW</a>. Applications take around 6-8 weeks to process. </p> </div> </div> </div> </div> <div class="checklistitem "> <div class="checklistitem-number "> <div class="checklistitem-number-inner" data-list-item-number="558">6</div> </div> <div class="checklistitem-inner"> <div class="checklistitem-content"> <div class="checklistitem-content-copy rte"> <h5>We will send you an offer</h5> <p>We will send you a full offer if everything is fine or a conditional offer if more steps are required.</p> </div> </div> </div> </div> <div class="checklistitem "> <div class="checklistitem-number "> <div class="checklistitem-number-inner" data-list-item-number="559">7</div> </div> <div class="checklistitem-inner"> <div class="checklistitem-content"> <div class="checklistitem-content-copy rte"> <h5>Accept your offer and enrol online</h5> <p>If you receive a full offer, accept it through <a href="https://my.unsw.edu.au/">myUNSW</a>. You then need to enrol for the start of the semester. Please note, you are not able to do this online. You will be emailed information about the enrolment procedure.</p> </div> </div> </div> """]))
            item['rntry_requirements_en'] = "For postgraduate study, you are generally required to have completed undergraduate studies at a university-type institution. You can find out the exact academic entry requirements for your program in the ‘Coursework program’ section of the international student guide for postgraduates."
            if "Entry Requirements" in allcontent:
                entryIndex = allcontent.index("Entry Requirements")
                if "How to Apply" in allcontent:
                    entryIndexEnd = allcontent.index("How to Apply")
                else:
                    entryIndexEnd = -1
                entry_requirements = allcontent[entryIndex:entryIndexEnd]
                item['rntry_requirements_en'] = item['rntry_requirements_en'] + clear_lianxu_space(entry_requirements)


            # 中国要求高考分数
            avgDict = {'Art Theory': '80', 'Design (Honours)': '80', 'Fine Arts (Honours)': '80',
                       'Media Arts (Honours)': '80', 'Arts': '80', 'Arts and Business': '83',
                       'Arts / Education (Secondary)': '80', 'Commerce / Education (Secondary)': '88',
                       'Design (Honours) / Education (Secondary)': '80', 'Economics / Education (Secondary)': '85',
                       'Fine Arts / Education (Secondary)': '80', 'Media Arts (Honours) / Education (Secondary)': '80',
                       'Science / Education (Secondary)': '80', 'Criminology & Criminal Justice': '80',
                       'International Studies': '83', 'Media (Communication & Journalism)': '80',
                       'Media (Public Relations & Advertising)': '80', 'Media (Screen & Sound Production)': '80',
                       'Music': '80', 'Music / Education (Secondary)': '80', 'Social Research & Policy': '80',
                       'Social Work (Honours)': '80', 'Architectural Studies': '85', 'City Planning (Honours)': '80',
                       'Computational Design': '80', 'Construction Management & Property': '80',
                       'Industrial Design (Honours)': '80', 'Interior Architecture (Honours)': '80',
                       'Landscape Architecture (Honours)': '80', 'Actuarial Studies': '88', 'Commerce': '88',
                       'Commerce (International)': '88', 'Economics': '85', 'Information Systems': '83',
                       'Engineering (Honours)': '85', 'Engineering (H) / M Biomed Engineering': '85',
                       'Engineering (H) (Elec) / M Engineering (Elec)': '88',
                       'Engineering (Honours) (Civil with Architecture)': '85',
                       'Engineering (H) / Engineering Science': '85', 'Science (Food Science & Technology)': '85',
                       'Science (Comp Science)': '85', 'Laws (Dual Degree)': 'NA', 'Med MD': 'NA',
                       'Exercise Physiology': '83', 'Aviation (Flying)': '80', 'Aviation (Management)': '80',
                       'Engineering (Materials Science & Engineering)': '80', 'Environmental Management': '80',
                       'Life Sciences': '80', 'Medical Science': '85', 'Medicinal Chemistry (Honours)': '83',
                       'Nanoscience (Honours)': '80', 'Optometry / Science': 'NA', 'Psychological Science': '80',
                       'Psychology': '88', 'Science': '80', 'Advanced Science (Honours)': '85',
                       'Science and Business': '83', 'Science (Advanced Mathematics) (Honours)': '85',
                       'Biotechnology (Honours)': '80', 'Science (International)': '80'}
            item['average_score'] = avgDict.get(item['programme_en'])
            print("item['average_score']: ", item['average_score'])

            tuition_feeDict = {'Master of Business': '30,720', 'Master of Logistics Management': '30,720',
                               'Doctor of Philosophy (Anatomy)': '43,440', 'Master of Sustainment Management': '30,720',
                               'Doctor of Philosophy (Kirby Institute)': '43,440',
                               'Master of Curating and Cultural Leadership': '32,400',
                               'Master of Laws - Corporate & Commercial Law': '41,520',
                               'Doctor of Philosophy (Creative Practice)': '30,000',
                               'Doctor of Philosophy (Accounting)': '33,120',
                               'Doctor of Philosophy (Aviation)': '40,080',
                               'Graduate Diploma in Biomedical Engineering': '41,280',
                               'Master of Capability Management': '30,720',
                               'Doctor of Philosophy (Medical Education)': '41,280',
                               'Doctor of Philosophy (Art, Design and Media)': '31,680',
                               'Master of Criminal Justice & Criminology': '39,000',
                               'Doctor of Philosophy (Humanities)': '30,000',
                               'Master of Accounting and Business Information Technology': '42,480',
                               'Graduate Diploma of Aviation Management': '29,340',
                               'Master of Biomedical Engineering': '41,280', 'Master of Cyber Security': '30,720',
                               'Doctor of Philosophy (Pathology)': '43,440', 'Master of Design': '32,400',
                               'Master of Laws - Criminal Justice & Criminology': '41,520',
                               'Master of Arts (Research)': '30,000', 'Master of Commerce': '42,480',
                               'Master of Aviation Management': '39,120',
                               'Master of Engineering Science (Biomedical Engineering) ': '41,280',
                               'Master of Cyber Security Operations': '30,720',
                               'Doctor of Philosophy (Physiology and Pharmacology)': '43,440',
                               'Master of Art': '32,400', 'Master of Dispute Resolution': '41,520',
                               'Master of Arts and Social Sciences (Combined)': '31,440',
                               'Master of Commerce (Extension)': '42,480',
                               'Master of Science (Aviation) (Research)': '40,080',
                               'Graduate Diploma in Engineering Science (Chemical Process Engineering) ': '41,280',
                               'Master of Cyber Security, Strategy and Diplomacy': '30,720',
                               'Graduate Certificate in Pharmaceutical Medicine': '20,760',
                               'Master of Fine Arts (Research)': '31,680',
                               'Master of Laws - Dispute Resolution': '41,520',
                               'Master of Journalism and Communication': '31,440',
                               'Master of Financial Analysis': '42,480',
                               'Doctor of Philosophy (Biochemistry & Molecular Genetics)': '40,080',
                               'Graduate Diploma in Engineering Science (Food Process Engineering) ': '41,280',
                               'Master of Information Technology (Specialisation)': '30,720',
                               'Master of Pharmaceutical Medicine': '20,760',
                               'Master of Environmental Law & Policy': '39,240', 'Master of Music (Research)': '30,000',
                               'Master of Philosophy (Commerce and Economics)': '33,120',
                               'Doctor of Philosophy (Microbiology and Immunology)': '40,080',
                               'Graduate Diploma in Food Science': '41,280', 'Master of Project Management': '30,720',
                               'Master of Science (Anatomy) (Research) ': '43,440',
                               'Master of Laws - Environmental Law': '41,520',
                               'Master of Music Education (Research)': '30,000',
                               'Master of Professional Accounting': '42,480',
                               'Master of Science (Biochemistry & Molecular Genetics) (Research)': '40,080',
                               'Master of Engineering Science (Chemical Process Engineering) ': '41,280',
                               'Master of Strategic People Management': '30,720',
                               'Master of Science (Pathology) (Research)': '43,440',
                               'Master of Human Rights Law & Policy': '41,520',
                               'Master of Public Relations and Advertising': '31,440',
                               'Master of Professional Accounting (Extension)': '42,480',
                               'Master of Science (Microbiology and Immunology) (Research)': '40,080',
                               'Master of Engineering Science (Food Process Engineering)': '41,280',
                               'Master of Science (Physiology and Pharmacology) (Research)': '43,440',
                               'Master of Laws - Human Rights & Social Justice': '41,520',
                               'Doctor of Philosophy (Education)': '30,000',
                               'Doctor of Philosophy (Actuarial Studies)': '33,120',
                               'Doctor of Philosophy (Applied Geology)': '40,080', 'Master of Food Science': '41,280',
                               'Doctor of Philosophy in Medicine (Prince of Wales Clinical School)': '43,440',
                               'Master of Laws - Innovation Law': '41,520', 'Master of Actuarial Studies': '42,480',
                               'Doctor of Philosophy (Biological Science)': '40,080',
                               'Graduate Certificate in Engineering Science (Civil Engineering or Geospatial Engineering)': '20,640',
                               'Doctor of Philosophy in Medicine (South Western Sydney Clinical School)': '43,440',
                               'Master of Laws - International Business & Economic Law': '41,520',
                               'Master of Actuarial Studies (Extension)': '42,480',
                               'Doctor of Philosophy (Climate Science)': '40,080',
                               'Master of Engineering (Civil Engineering) ': '41,280',
                               'Doctor of Philosophy in Medicine (St George and Sutherland Clinical School)': '43,440',
                               'Master of International Law & International Relations': '36,480',
                               'Master of Education (Assessment and Evaluation)': '31,440',
                               'Doctor of Philosophy (Environmental Management)': '40,080',
                               'Master of Engineering (Environmental Engineering) ': '41,280',
                               'Doctor of Philosophy in Medicine (St Vincents Clinical School)': '43,440',
                               'Master of Laws - International Law': '41,520',
                               'Master of Education (Educational Psychology)': '31,440',
                               'Doctor of Philosophy (Taxation and Business Law)': '33,120',
                               'Doctor of Philosophy (Geography)': '40,080',
                               'Master of Engineering Science (Civil Engineering)': '41,280',
                               'Master of Medicine (Research)': '43,440',
                               'Doctor of Juridical Science (Research)': '38,400',
                               'Master of Education (Educational Studies)': '31,440',
                               'Master of Business Law': '42,000',
                               'Graduate Certificate in Environmental Management': '18,480',
                               'Master of Engineering Science (Environmental Engineering)': '41,280',
                               'Master of Science in Medicine (Kirby Institute) (Research)': '41,280',
                               'Doctor of Philosophy (Research)': '38,400',
                               'Master of Education (Gifted Education)': '31,440',
                               'Graduate Diploma in Environmental Management': '36,960',
                               'Master of Engineering Science (Geospatial Engineering)': '41,280',
                               'Master of Science in Medicine (Prince of Wales Clinical School) (Research)': '43,440',
                               'JD (Juris Doctor)': '43,680', 'Master of Education (Higher Education)': '31,440',
                               'AGSM MBA': '40,800', 'Master of Marine Science and Management': '39,120',
                               'Master of Engineering Science (Geotechnical Engineering and Engineering Geology)': '41,280',
                               'Master of Science in Medicine (South Western Sydney School) (Research)': '43,440',
                               'Master of Laws': '41,520', 'Master of Education (Research)': '30,000',
                               'Master of Science (Applied Geology) (Research)': '40,080',
                               'Master of Engineering Science (Project Management)': '41,280',
                               'Master of Science in Medicine (St George and Sutherland Clinical School) (Research)': '43,440',
                               'Master of Laws (Research)': '38,400',
                               'Master of Education (Special Education)': '31,440',
                               'Master of Science (Biological Science) (Research)': '40,080',
                               'Master of Engineering Science (Structural Engineering)': '41,280',
                               'Master of Science in Medicine (St Vincents Clinical School)': '43,440',
                               'Master of Law, Media & Journalism': '36,480',
                               'Master of Education (Teacher Professional Learning)': '31,440',
                               'Master of Science (Climate Sciences) (Research)': '40,080',
                               'Master of Engineering Science (Sustainable Systems)': '41,280',
                               'Doctor of Philosophy (Psychiatry)': '43,440',
                               'Master of Laws - Media & Technology Law': '41,520',
                               'Master of Education (TESOL)': '31,440', 'Doctor of Philosophy (Economics)': '33,120',
                               'Master of Science (Geography) (Research)': '40,080',
                               'Master of Engineering Science (Transportation Engineering)': '41,280',
                               'Graduate Certificate in Forensic Mental Health': '20,760',
                               'Master of Education (Visual Arts Education)': '31,440',
                               'Doctor of Philosophy (Biotechnology)': '40,080',
                               'Master of Engineering Science (Water Engineering: Catchments to Coasts)': '41,280',
                               'Graduate Diploma in Forensic Mental Health': '31,140',
                               'Master of Educational Leadership': '31,440', 'Graduate Diploma (Research)': '39,120',
                               'Master of Engineering Science (Water, Wastewater and Waste Engineering )': '41,280',
                               'Master of Forensic Mental Health': '41,520',
                               'Master of Educational Leadership (Research)': '30,000', 'Master of Economics': '42,480',
                               'Master of Science (Biotechnology) (Research)': '40,080',
                               'Graduate Certificate in Computing': '20,640',
                               'Master of Philosophy in Forensic Mental Health': '43,440',
                               'Master of Teaching (Secondary)': '47,160', 'Doctor of Philosophy (Chemistry)': '40,080',
                               'Graduate Diploma in Information Technology': '41,280',
                               'Master of Science (Psychiatry) (Research)': '43,440',
                               'Doctor of Philosophy (Banking and Finance)': '33,120',
                               'Master of Science (Chemistry) (Research)': '40,080',
                               'Master of Information Technology': '41,280', 'Master of Applied Linguistics': '31,440',
                               'Doctor of Philosophy (Materials Science and Engineering)': '40,080',
                               'Graduate Diploma in Engineering Science (Energy Systems) ': '41,280',
                               'Doctor of Philosophy (Public Health & Community Medicine)': '43,440',
                               'Master of Engineering (Materials Science and Engineering) (Research)': '40,080',
                               'Graduate Diploma in Engineering Science (Electrical Engineering) ': '41,280',
                               'Doctor of Public Health (Public Health & Community Medicine)': '41,280',
                               'Master of Finance': '42,480', 'Master of Materials Technology': '39,120',
                               'Graduate Diploma of Engineering Science (Telecommunications) ': '41,280',
                               'Graduate Certificate in Health Management': '20,760',
                               'Master of Interpreting': '31,440',
                               'Master of Science (Materials Science and Engineering) (Research)': '40,080',
                               'Master of Engineering (Telecommunications) ': '41,280',
                               'Graduate Certificate in Infectious Diseases Intelligence': '20,760',
                               'Master of Translation': '31,440', 'Master of Financial Planning': '42,480',
                               'Doctor of Philosophy (Mathematics)': '40,080',
                               'Master of Engineering (Electrical Engineering)': '41,280',
                               'Graduate Certificate in International Public Health': '20,760',
                               'Master of Translation and Interpreting': '31,440',
                               'Graduate Certificate in Mathematics and Statistics': '19,560',
                               'Master of Engineering Science (Electrical Engineering)  ': '41,280',
                               'Graduate Certificate in Public Health': '20,760',
                               'Doctor of Philosophy (Social Sciences)': '30,000',
                               'Doctor of Philosophy (Organisation and Management)': '33,120',
                               'Graduate Diploma in Mathematics and Statistics': '39,120',
                               'Master of Engineering Science (Energy Systems) ': '41,280',
                               'Graduate Diploma in Health Management': '31,140',
                               'Doctor of Public Policy and Governance (Research)': '30,000',
                               'Master of Financial Mathematics': '39,120',
                               'Master of Engineering Science (Nuclear Engineering) ': '41,280',
                               'Graduate Diploma in Infectious Diseases Intelligence': '31,140',
                               'Doctor of Social Work (Research)': '30,000', 'Master of Mathematics': '39,120',
                               'Master of Engineering Science (Systems and Control) ': '41,280',
                               'Graduate Diploma in International Public Health': '31,140',
                               'Master of Science (Mathematics)(Research)': '40,080',
                               'Master of Engineering Science (Telecommunications) ': '41,280',
                               'Graduate Diploma in Public Health': '31,140',
                               'Doctor of Philosophy (Information Systems and Technology Management)': '33,120',
                               'Master of Statistics': '39,120',
                               'Master of Engineering Science (Satellite Systems Engineering)': '41,280',
                               'Master of Health Administration (Research)': '34,320',
                               'Master of Development Studies': '31,440', 'Doctor of Philosophy (Optometry)': '40,080',
                               'Master of Engineering Science': '30,720', 'Master of Health Management': '41,520',
                               'Master of International Relations': '31,440',
                               'Doctor of Philosophy (Vision Science)': '40,080',
                               'Master of Space Engineering': '30,720',
                               'Master of Health Management (Extension)': '41,520',
                               'Master of Public Policy and Governance': '31,440',
                               'Master of Optometry and Vision Science': '39,120',
                               'Master of Space Operations': '30,720',
                               'Master of Health Management (Extension)/International Public Health ': '41,520',
                               'Master of Social Sciences (Research)': '30,000',
                               'Master of Information Systems Management': '42,480',
                               'Master of Science (Optometry)(Research)': '40,080',
                               'Master of Systems Engineering': '30,720',
                               'Master of Health Professions Education (Research)': '34,320',
                               'Master of Social Work (Research)': '30,000',
                               'Master of Science (Vision Science) (Research)': '40,080',
                               'Graduate Diploma in Engineering Science (Manufacturing Engineering & Management)': '41,280',
                               'Master of Infectious Diseases Intelligence': '41,520',
                               'Doctor of Philosophy (Organisation and Management) ': '33,120',
                               'Doctor of Philosophy (Physics)': '40,080',
                               'Graduate Diploma in Engineering Science (Mechanical Engineering)': '41,280',
                               'Master of International Public Health': '41,520',
                               'Master of Engineering (Mechanical Engineering) ': '41,280',
                               'Master of International Public Health (Extension) ': '41,520',
                               'Master of Science (Physics) (Research)': '40,080',
                               'Master of Engineering Science (Manufacturing Engineering & Management)': '41,280',
                               'Master of International Public Health (Extension)': '41,520',
                               'Master of International Business': '42,480',
                               'Doctor of Philosophy (Psychology)': '40,080',
                               'Master of Engineering Science (Mechanical Engineering)': '41,280',
                               'Master of International Public Health (Extension) / Health Management': '41,520',
                               'Doctor of Philosophy/Master of Psychology (Clinical)': '40,080',
                               'Graduate Diploma in Mining Engineering': '41,280',
                               'Master of International Public Health / Health Management': '41,520',
                               'Doctor of Philosophy/Master of Psychology (Forensic)': '40,080',
                               'Master of Mining Engineering': '41,280',
                               'Master of International Public Health / Public Health': '41,520',
                               'Dual PhD / Master of Psychology (Clinical)': '40,080',
                               'Graduate Certificate in Petroleum Engineering': '30,960',
                               'Master of Philosophy in Public Health': '34,320',
                               'Dual PhD / Master of Psychology (Forensic)': '40,080',
                               'Graduate Diploma in Engineering Science (Petroleum Engineering)  ': '41,280',
                               'Master of Public Health': '41,520', 'Doctor of Philosophy (Marketing)': '33,120',
                               'Master of Psychology (Clinical)': '39,120',
                               'Master of Engineering Science (Petroleum Engineering)  ': '41,280',
                               'Master of Public Health (Extension)': '41,520',
                               'Master of Psychology (Forensic)': '38,100',
                               'Graduate Diploma of Engineering Science (Photovoltaics and Solar Energy)': '41,280',
                               'Master of Public Health (Extension) / Health Management ': '41,520',
                               'Master of Science (Psychology) (Research)': '40,080',
                               'Graduate Diploma of Engineering Science (Renewable Energy Engineering)': '41,280',
                               'Master of Public Health (Research)': '34,320', 'Master of Marketing': '42,480',
                               'Master of Engineering Science (Photovoltaics and Solar Energy)  ': '41,280',
                               'Master of Public Health / Health Management': '41,520',
                               'Master of Engineering Science (Renewable Energy Engineering)  ': '41,280',
                               'Master of Public Health /Master of Health Management (Extension) ': '41,520',
                               'Master of Public Health/International Public Health (Extension)': '41,520',
                               'Master of Science (Community Medicine) (Research) ': '34,320',
                               'Doctor of Philosophy (Rural Health)': '43,440',
                               'Master of Laws - Corporate, Commercial Law & Taxation': '41,520',
                               'Master of Science (Rural Health) (Research)': '43,440',
                               'Master of Laws - Taxation': '41,520',
                               'Doctor of Philosophy in Surgery (Prince of Wales Clinical School)': '43,440',
                               'Doctor of Philosophy in Surgery (South Western Sydney Clinical School)': '43,440',
                               'Master of Taxation': '42,480',
                               'Doctor of Philosophy in Surgery (St George and Sutherland Clinical School': '43,440',
                               'Doctor of Philosophy in Surgery (St Vincents Clinical School)': '43,440',
                               'Master of Surgery (Research) (Prince of Wales Clinical School)': '43,440',
                               'Master of Surgery (Research) (South Western Sydney Clinical School)': '43,440',
                               'Master of Surgery (Research) (St George and Sutherland Clinical School) ': '43,440',
                               'Master of Surgery (Research) (St Vincents Clinical School)': '43,440',
                               'Doctor of Philosophy (Childhood Cancer)': '41,280',
                               'Doctor of Philosophy (Obstetrics and Gynaecology)': '43,440',
                               'Doctor of Philosophy (Paediatrics)': '43,440',
                               'Graduate Certificate in Reproductive Medicine': '20,760',
                               "Graduate Certificate in Women's Health Medicine": '20,760',
                               'Graduate Diploma in Reproductive Medicine': '31,140',
                               'Master of Reproductive Medicine': '41,520',
                               'Master of Science (Obstetrics and Gynaecology) (Research)': '43,440',
                               'Master of Science (Paediatrics) (Research)': '43,440',
                               "Master of Women's Health Medicine": '41,520'}
            tuition_fee = tuition_feeDict.get(item['degree_name'])
            if tuition_fee != None:
                tuition_fee = tuition_fee.replace(",", "")
                item['tuition_fee_pre'] = "$"
            item['tuition_fee'] = tuition_fee
            print("item['tuition_fee']: ", item['tuition_fee'])

            # careerDict = {}
            career = response.xpath(
                "//p[contains(text(),'Career Opportunities')]/../../preceding-sibling::*[1]/following-sibling::*[position()<4]").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            print("item['career_en']: ", item['career_en'])

            item['apply_pre'] = "$"
            item['apply_fee'] = 100
            yield item
        except Exception as e:
            with open("scrapySchool_Australian_yan/error/" + item['university'] + str(item['degree_type']) + ".txt",
                      'w', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

