# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import *
from scrapySchool_Canada_Ben.items import *

class MacewanuniversitySpider(scrapy.Spider):
    name = 'MacEwanUniversity'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.macewan.ca/wcm/SchoolsFaculties/ArtsScience/Programs/BachelorofArts/index.htm',
'https://www.macewan.ca/wcm/SchoolsFaculties/Business/Programs/BachelorofCommerce/index.htm',
'https://www.macewan.ca/wcm/SchoolsFaculties/FFAC/Programs/BachelorofCommunicationStudies/index.htm',
'https://www.macewan.ca/wcm/SchoolsFaculties/FFAC/Programs/BachelorofDesign/index.htm',
'https://www.macewan.ca/wcm/SchoolsFaculties/FFAC/Programs/BachelorofMusicinJazzandContemporaryPopularMusic/index.htm',
'https://www.macewan.ca/wcm/SchoolsFaculties/Nursing/BachelorofPsychiatricNursing/index.htm',
'https://www.macewan.ca/wcm/SchoolsFaculties/Nursing/BachelorofScienceinNursing/index.htm',
'https://www.macewan.ca/wcm/SchoolsFaculties/HCS/Programs/BachelorofSocialWork/index.htm',
'https://www.macewan.ca/wcm/SchoolsFaculties/ArtsScience/Programs/BachelorofScience/index.htm']

    def parse(self, response):
        item=get_item(ScrapyschoolCanadaBenItem)
        item['school_name']='MacEwan University'
        item['url']=response.url
        print(response.url)

        #不能明确区分校区
        item['location']='Edmonton'
        item['campus']='Edmonton'
        #$638.00 Cost Per Credit
        item['tuition_fee']='638.00'
        # item['tuition_fee_per']='5'
        item['tuition_fee_pre']='$'
        item['apply_fee']='110'
        item['apply_pre']='$'

        item['ap']='Minimum grade of 4'
        item['ib']='Minimum grade of 5 in English A1 or A2, or minimum grade of 6 in English B.'
        item['alevel']='Minimum grade of B.'

        duration=response.xpath('//div[contains(text(),"Length of Study")]/following-sibling::p/text()').extract()
        # print(duration)
        item['duration_per']='1'
        if '4' in ''.join(duration):
            item['duration']='4'
        elif '1.5' in ''.join(duration):
            item['duration']='1.5'
        else:
            item['duration']='2'

        programme=response.xpath('//h1/text()').extract()
        # print(programme)
        item['degree_name']=''.join(programme).strip()
        print(item['degree_name'])
        item['major_name_en']=''.join(programme).replace('Bachelor of','').strip()

        department=response.xpath('//p[@class="breadcrumbs"]/a/text()').extract()
        # print(department)
        if len(department)>=2:
            item['department']=department[1].strip()
            item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']='6.5','5.5','5.5','5.5','5.5'
            item['toefl'],item['toefl_l'],item['toefl_s'],item['toefl_r'],item['toefl_w']='86','21','21','21','21'
        else:
            item['department']='Faculty of Nursing'
            item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w'] = '6.5', '6.0', '7.0', '5.5', '5.5'
            item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w'] = '86', '23', '26', '21', '21'

        # degree_name=response.xpath('//div[text()="Credential Granted"]/following-sibling::p/text()').extract()
        # # print(degree_name)
        # item['degree_name']=degree_name[0]


        start_date=response.xpath('//div[contains(text(),"Intake")]/following-sibling::p/text()').extract()
        # print(start_date)

        item['entry_requirements_en']='<div><p>&nbsp;</p><h2>Categories of admission</h2><p>Applicants may be admitted to one of the following:</p><div><h3><a>Regular admission </a></h3><div><p>To be evaluated through the Office of the University Registrar</p><p>Applicants must have a minimumoverall average of 65 percent, with no course grade lower than 50 percent, inthe following high school courses:</p><ul><li><p>ELA 30-1 or 75% in ELA 30-2</p></li><li><p>Four subjects from Group A, B, C, or D</p></li></ul><p>Notes:</p><ul><li><p>Applicantsare strongly encouraged to present a broad range of subjects in order tobenefit from the breadth of learning and to increase flexibility of futureprogram and course choices.</p></li><li><p>Amaximum of two Group B subjects may be presented; they must be from differentdisciplines.</p></li><li><p>Amaximum of one Group D subject may be presented.&nbsp; Group D subjects used for admission must be5-credit or any credit combination of at least 5 credits (e.g., two 3-creditsubjects).</p></li></ul><p>Applicants with nine or moreuniversity-level credits must also present a minimum Admission Grade PointAverage (AGPA) of 2.0 on a 4.0 scale. </p><p><a>Learn more about Group A, B, C or D courses</a></p></div><h3><a>Mature admission </a></h3><div><p>To be evaluated through the Office of the University Registrar</p><p>Applicants must be 20 years ofage or older and have been out of full-time high school at least one year bythe beginning of the intake term. Applicants must have the following:</p><ul><li><p>ELA30-1 with a minimum grade of 65 percent (or equivalent) <br><br>OR</p></li><li><p>Six credits ofuniversity-level English with no grade less than C-</p></li></ul><p>Applicants with nine or moreuniversity-level credits must also present a minimum Admission Grade PointAverage (AGPA) of 2.0 on a 4.0 scale.</p></div><h3><a>Previous post-secondary </a></h3><div><p>To be evaluated through the Office of the University Registrar</p> <p>Admission in this categorydoes not imply or guarantee the transfer of any coursework and/or credentialunless a block transfer agreement (internal or external) is in effect andpublished in the calendar by the Office of the University Registrar. Inaddition, transfer of coursework does not imply or guarantee that an applicantwill be admitted.</p> <p>Applicants must havesuccessfully completed one of the following from a recognized institution:</p> <ul><li><p>A diploma in design (orequivalent)<br><br>OR</p></li><li><p>A minimum of 24university-level credits with a minimum Admission Grade Point Average (AGPA) of2.0 on a 4.0 scale and must have completed the required high school courses listedunder the Regular or Mature Admission category.</p></li></ul></div></div><p>&nbsp;</p><h2>Additional admission criteria</h2><p>All applicants must meet the following:</p><div><h3><a>English language proficiency<br> </a></h3><div><p>To be evaluated through the Office of the University Registrar | Applicable to all admission categories</p><p>All applicants must meet an acceptable level of English language proficiency. We will require official documents such as high school or post-secondary transcripts or proof of successful completion of standardized language evaluation. Full details are available in MacEwan University’s academic calendar or online at: MacEwan.ca/ELP.</p><p><a>Learn more about English language proficiency</a></p></div><h3><a>Other admission criteria </a></h3><div><p>To be evaluated through the program | Applicable to all admission categories</p><p>Applicants are required tosubmit a Portfolio and a Statement of Intent to a committee of Design Studiesfaculty. </p><ul><li>Portfolio– the portfolio of design work shall consist of the applicant’s original bodyof work. </li><li>Statementof Intent – applicants must demonstrate the following in their statement:</li><ul><li>theability to express ideas well in writing</li><li>howthe MacEwan University program is aligned with their interests and goals</li><li>aninterest in learning about design theory and practice</li></ul></ul><p><a>Follow the portfolio guidelines</a></p></div></div><div></div><div></div><div></div></div>'
        if 'January' in ''.join(start_date):
            item['start_date']='2019-01,2019-09'
            item['deadline']='2018-09-30,2019-05-01'
        else:
            item['start_date']='2019-09'

        overview=response.xpath('//div[@id="content"]').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en']=overview

        #文科专业
        majors=['Requirements','Accounting','Anthropology','Business Law','Business Studies','Chinese','Classics','Comparative Literature','Creative Writing','Economics','Education','English','Finance','French','Gender Studies','German','History','Human Resources','Humanities','Japanese','Latin','Linguistics','Marketing','Philosophy','Political Science','Psychology','Sociology','Spanish']
        #理科专业
        majors2=['Applied Statistics','Biological Sciences','Chemistry','Computer Science','Earth and Planetary Sciences','Mathematical Sciences','Mathematics','Physical Sciences','Physics','Planetary Physics','Psychology','Statistics',]
        if item['degree_name']=='Bachelor of Arts':
            # print(majors)
            for i in majors:
                item['major_name_en']=i
                yield item
        elif item['degree_name']=='Bachelor of Science':
            # print(majors2)
            for j in majors2:
                item['major_name_en']=j
                yield item
        else:
            yield item