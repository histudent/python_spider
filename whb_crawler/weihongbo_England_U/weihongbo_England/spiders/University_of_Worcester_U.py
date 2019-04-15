import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'University_of_Worcester_U'
    allowed_domains = []
    base_url= 'https://www.worcester.ac.uk%s'
    #base_url = '%s'
    start_urls = []
    C = [
'/journey/mathematics-physical-education-pe-bsc-hons.html',
'/journey/mathematics-psychology-bsc-hons.html',
'/courses/media-culture-and-sociology-ba-hons.html',
'/courses/physical-education-and-sports-coaching-science-bsc-hons.html',
'/courses/physical-education-and-sports-studies-bsc-hons.html',
'/courses/politics-and-sociology-ba-hons.html',
'/journey/psychology-and-religion-philosophy-and-values-in-education-ba-bsc-hons.html',
'/journey/religion-philosophy-and-values-in-education-and-sociology-ba-hons.html',
'/courses/film-production-and-screenwriting-ba-hons.html',
'/courses/film-studies-and-media-culture-ba-hons.html',
'/courses/film-studies-and-screenwriting-ba-hons.html',
'/courses/fine-art-and-illustration-ba-hons.html',
'/courses/fine-art-and-psychology-ba-bsc-hons.html',
'/courses/geography-and-physical-education-bsc-hons.html',
'/courses/geography-and-sports-studies-bsc-hons.html',
'/journey/geography-mathematics-bsc-hons.html',
'/courses/history-and-journalism-ba-hons.html',
'/courses/history-and-politics-ba-hons.html',
'/courses/history-and-sociology-ba-hons.html',
'/courses/drama-performance-and-psychology-ba-bsc-hons.html',
'/courses/drama-performance-and-screenwriting-ba-hons.html',
'/courses/ecology-and-environmental-science-bsc-hons.html',
'/courses/ecology-and-physical-geography-bsc-hons.html',
'/courses/education-studies-and-english-language-ba-hons.html',
'/courses/education-studies-and-english-literature-ba-hons.html',
'/courses/education-studies-and-physical-education-ba-bsc-hons.html',
'/courses/education-studies-and-psychology-ba-bsc-hons.html',
'/journey/education-studies-and-religion-philosophy-and-values-in-education-ba-hons.html',
'/courses/education-studies-and-sociology-ba-hons.html',
'/journey/education-studies-mathematics-bsc-hons.html',
'/courses/english-language-and-english-literature-ba-hons.html',
'/courses/english-language-and-journalism-ba-hons.html',
'/courses/english-language-and-media-culture-ba-hons.html',
'/journey/english-language-and-religion-philosophy-and-values-in-education-ba-hons.html',
'/courses/english-literature-and-film-studie-ba-hons.html',
'/courses/english-literature-and-history-ba-hons.html',
'/courses/english-literature-and-journalism-ba-hons.html',
'/courses/english-literature-and-media-culture-ba-hons.html',
'/courses/animation-and-graphic-design-ba-hons.html',
'/courses/animation-and-illustration-ba-hons.html',
'/courses/animation-and-screenwriting-ba-hons.html',
'/courses/archaeology-heritage-studies-and-art-design-ba-hons.html',
'/courses/archaeology-heritage-studies-and-geography-ba-bsc-hons.html',
'/courses/archaeology-heritage-studies-and-history-ba-hons.html',
'/courses/art-design-and-drama-performance-ba-hons.html',
'/courses/art-design-and-education-studies-ba-hons.html',
'/courses/art-design-and-english-literature-ba-hons.html',
'/courses/art-design-and-illustration-ba-hons.html',
'/courses/animation-and-screenwriting-ba-hons.html',
'/courses/archaeology-heritage-studies-and-art-design-ba-hons.html',
'/courses/archaeology-heritage-studies-and-geography-ba-bsc-hons.html',
'/courses/archaeology-heritage-studies-and-history-ba-hons.html',
'/courses/art-design-and-drama-performance-ba-hons.html',
'/courses/art-design-and-education-studies-ba-hons.html',
'/courses/art-design-and-english-literature-ba-hons.html',
'/courses/art-design-and-illustration-ba-hons.html',
'/courses/art-design-and-psychology-ba-bsc-hons.html',
'/courses/geography-and-physical-education-bsc-hons.html',
'/courses/geography-and-sports-studies-bsc-hons.html',
'/journey/geography-mathematics-bsc-hons.html',
'/courses/history-and-journalism-ba-hons.html',
'/courses/history-and-politics-ba-hons.html',
'/courses/history-and-sociology-ba-hons.html',
'/courses/human-biology-and-human-nutrition-bsc-hons.html',
'/courses/human-biology-and-psychology-bsc-hons.html',
'/courses/human-nutrition-and-psychology-bsc-hons.html',
'/courses/human-nutrition-and-sports-studies-bsc-hons.html',
'/courses/journalism-and-media-culture-ba-hons.html',
'/courses/drama-performance-and-film-studies-ba-hons.html',
'/courses/drama-performance-and-psychology-ba-bsc-hons.html',
'/courses/drama-performance-and-screenwriting-ba-hons.html',
'/courses/ecology-and-environmental-science-bsc-hons.html',
'/courses/ecology-and-physical-geography-bsc-hons.html',
'/courses/education-studies-and-english-language-ba-hons.html',
'/courses/education-studies-and-english-literature-ba-hons.html',
'/courses/education-studies-and-physical-education-ba-bsc-hons.html',
'/courses/education-studies-and-psychology-ba-bsc-hons.html',
'/journey/education-studies-and-religion-philosophy-and-values-in-education-ba-hons.html',
'/journey/religion-philosophy-and-values-in-education-and-sociology-ba-hons.html',
'/journey/biochemistry-bsc-hons.html',
'/journey/biochemistry-mbiol-integrated-masters.html',
'/journey/biology-bsc-hons.html',
'/journey/biology-mbiol-integrated-masters.html',
'/journey/biomedical-sciences-bsc-hons.html',
'/courses/birth-and-beyond-ba-top-up.html',
'/journey/business-administration-ba-hons.html',
'/journey/business-and-accountancy-ba-hons.html',
'/journey/business-and-digital-communications-ba-hons.html',
'/journey/business-and-enterprise-ba-hons.html',
'/journey/business-and-finance-ba-hons.html',
'/journey/business-and-human-resource-management-ba-hons.html',
'/journey/business-and-marketing-ba-hons.html',
'/journey/business-economics-finance-ba-hons-wbs.html',
'/journey/business-information-technology-bsc-hons.html',
'/journey/business-management-ba-hons-top-up.html',
'/journey/business-management-ba-hons-wbs.html',
'/journey/business-management-hnd.html',
'/courses/business-psychology-bsc-hons.html',
'/journey/business-studies-ba-hons.html',
'/journey/child-adolescent-mental-health-bsc-hons-top-up.html',
'/journey/child-adolescent-mental-health-fdsc.html',
'/courses/clinical-psychology-bsc-hons.html',
'/journey/collaborative-working-with-children-young-people-families-fda.html',
'/journey/computer-games-design-development-bsc-hons.html',
'/journey/computing-bsc-hons.html',
'/journey/computing-hnd.html',
'/courses/counselling-fdsc.html',
'/journey/counselling-psychology-bsc-hons.html',
'/journey/creative-digital-media-ba-hons.html',
'/journey/cricket-coaching-management-bsc-hons.html',
'/journey/criminology-ba-hons.html',
'/journey/criminology-with-policing-ba-hons.html',
'/journey/dance-and-community-practice-ba-hons.html',
'/journey/dance-hnd.html',
'/courses/developmental-psychology-bsc-hons.html',
'/journey/drama-performance-ba-hons.html',
'/journey/early-childhood-professional-practice-ba-hons.html',
'/discover/early-years-foundation-degree-flexible-distributed-learning-pathway.html',
'/journey/early-years-sector-endorsed-fda.html',
'/journey/education-studies-ba-hons.html',
'/journey/english-literature-ba-hons.html',
'/courses/entrepreneurship-ba-hons-wbs.html',
'/journey/environmental-science-bsc-hons.html',
'/journey/film-production-ba-hons.html',
'/journey/film-studies-ba-hons.html',
'/journey/fine-art-practice-ba-hons.html',
'/courses/football-business-management-coaching-fdsc.html',
'/journey/forensic-and-applied-biology-bsc-hons.html',
'/journey/forensic-psychology-bsc-hons.html',
'/journey/accounting-and-finance-ba-hons-wbs.html',
'/journey/animal-biology-bsc-hons.html',
'/journey/animal-biology-mbiol-integrated-masters.html',
'/journey/archaeology-and-heritage-studies-ba-hons.html',
'/journey/game-art-ba-hons.html',
'/journey/geography-bsc-hons.html',
'/journey/graphic-design-ba-hons.html',
'/courses/health-and-social-care-fdsc.html',
'/journey/history-ba-hons.html',
'/journey/human-biology-bsc-hons.html',
'/journey/human-biology-mbiol-integrated-masters.html',
'/journey/human-geography-ba-hons.html',
'/journey/human-nutrition-bsc-hons.html',
'/journey/illustration-ba-hons.html',
'/journey/integrated-working-children-families-ba-hons-top-up-degree.html',
'/courses/integrative-counselling-ba-hons.html',
'/journey/english-literature-ba-hons.html',
'/journey/animal-biology-bsc-hons.html',
'/journey/animal-biology-mbiol-integrated-masters.html',
'/journey/animation-ba-hons.html',
'/courses/applied-health-social-care-ba-top-up.html',
'/journey/archaeology-and-heritage-studies-ba-hons.html',
'/journey/biochemistry-bsc-hons.html',
'/journey/biochemistry-mbiol-integrated-masters.html',
'/journey/biology-bsc-hons.html',
'/journey/biology-mbiol-integrated-masters.html',
'/journey/biomedical-sciences-bsc-hons.html',
'/courses/birth-and-beyond-ba-top-up.html',
'/journey/business-administration-ba-hons.html',
'/journey/business-and-accountancy-ba-hons.html',
'/journey/business-and-digital-communications-ba-hons.html',
'/journey/business-and-enterprise-ba-hons.html',
'/journey/business-and-finance-ba-hons.html',
'/journey/business-and-human-resource-management-ba-hons.html',
'/journey/business-and-marketing-ba-hons.html',
'/journey/business-economics-finance-ba-hons-wbs.html',
'/journey/pharmacology-bsc-hons.html',
'/journey/physical-education-and-dance-ba-hons.html',
'/journey/physical-education-and-outdoor-education-bsc-hons.html',
'/courses/physical-geography-bsc-hons.html',
'/journey/physiotherapy-bsc-hons.html',
'/journey/plant-science-mbiol-integrated-masters .html',
'/journey/politics-ba-hons.html',
'/journey/primary-initial-teacher-education-ba-hons.html',
'/journey/primary-outdoor-education-ba-hons.html',
'/journey/computer-games-design-development-bsc-hons.html',
'/journey/computing-bsc-hons.html',
'/journey/computing-hnd.html',
'/courses/counselling-fdsc.html',
'/journey/counselling-psychology-bsc-hons.html',
'/journey/creative-digital-media-ba-hons.html',
'/journey/cricket-coaching-management-bsc-hons.html',
'/journey/criminology-ba-hons.html',
'/journey/criminology-with-policing-ba-hons.html',
'/journey/dance-and-community-practice-ba-hons.html',
'/courses/sport-exercise-psychology-bsc-hons.html',
'/journey/sport-exercise-science-bsc-hons.html',
'/journey/sports-coaching-science-bsc-hons.html',
'/journey/sports-coaching-science-with-disability-sport-bsc-hons.html',
'/journey/sports-studies-bsc-hons.html',
'/journey/sports-therapy-bsc-hons.html',
'/journey/teaching-and-learning-fda.html',
'/journey/web-development-bsc-hons.html',
'/journey/biology-degrees.html',
'/journey/business-management-degrees.html',
'/your-home/spanish-module.html',
'/journey/sports-coaching-science-degrees.html',
'/journey/sports-studies-degrees.html',
'/journey/university-diploma-in-academic-tutoring.html',
'/journey/university-diploma-in-leadership-and-management.html',
'/journey/mathematics-bsc-hons.html',
'/journey/media-culture-degrees.html',
'/journey/physical-education-degrees.html',
'/journey/pre-hospital-unscheduled-emergency-care-fdsc.html',
'/courses/psychology-and-sociology-ba-bsc-hons.html',
'/journey/film-production-degrees.html',
'/journey/film-studies-degrees.html',
'/journey/fine-art-degrees.html',
'/your-home/french-module.html',
'/journey/animal-biology-degrees.html',
'/journey/animation-degrees.html',
'/your-home/arabic-module.html',
'/journey/archaeology-heritage-studies-degrees.html',
'/journey/geography-degrees.html',
'/your-home/german-module.html',
'/courses/graphic-design-and-illustration-ba-hons.html',
'/journey/graphic-design-multimedia-degrees.html',
'/journey/history-degrees.html',
'/journey/human-biology-degrees.html',
'/journey/human-nutrition-degrees.html',
'/your-home/ihs-health-sciences-bsc-hons.html',
'/journey/illustration-degrees.html',
'/your-home/italian-module.html',
'/your-home/japanese-module.html',
'/journey/english-language-degrees.html',
'/journey/english-literature-degrees.html',
'/journey/animal-biology-degrees.html',
'/journey/animation-degrees.html',
'/your-home/arabic-module.html',
'/journey/archaeology-heritage-studies-degrees.html',
'/journey/biology-degrees.html',
'/journey/business-management-degrees.html',
'/journey/computing-degrees.html',
'/journey/creative-digital-media-degrees.html',
'/journey/creative-professional-writing-degrees.html',
'/journey/diploma-in-teaching-english-literacy-and-esol.html',
'/journey/drama-performance-degrees.html',
'/journey/ecology-degrees.html',
'/journey/education-studies-degrees.html',]
#     C = ['https://www.worcester.ac.uk/courses/media-culture-and-sociology-ba-hons.html',
# 'https://www.worcester.ac.uk/courses/animal-biology-and-ecology-bsc-hons.html',
# 'https://www.worcester.ac.uk/courses/midwifery-bsc-hons.html',
# 'https://www.worcester.ac.uk/journey/journalism-ba-hons.html',
# 'https://www.worcester.ac.uk/courses/sociology-ba-hons.html',
# 'https://www.worcester.ac.uk/journey/international-business-management-ba-hons-wbs.html',
# 'https://www.worcester.ac.uk/journey/marketing-advertising-and-public-relations-ba-hons-wbs.html',
# 'https://www.worcester.ac.uk/courses/english-literature-ba-hons.html',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'University of Worcester'
        try:
            location = 'Worcester'
            location = remove_tags(location)
            #print(location)
        except:
            location = 'N/A'
            #print(location)
        try:
            department = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/p[2]/a[3]/strong').extract()[0]
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
            degree_name = response.xpath('//h1').extract()[0]
            degree_name = remove_tags(degree_name)
            degree_name = degree_name.replace('(Hons)','')
            degree_name = degree_name.split()[-1]


            #degree_name = re.findall('(.*)\n.*',degree_name)[0]
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
            #programme_en = re.findall(' (.*)',programme_en)[0]
            programme_en = programme_en.replace(degree_name,'')
            programme_en = programme_en.replace('  ',' ')

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
            overview_en = response.xpath('//*[@id="section-1"]/div[1]/div[1]/ul').extract()[0]
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
            modules_en = response.xpath('//*[@id="section-3"]').extract()[0]
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
            rntry_requirements_en = response.xpath('//*[@id="section-2"]/div/div[2]').extract()[0]
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
            ielts_desc = 'Postgraduate courses usually require a minimum IELTS of 6.5 (with no less than 5.5 in any component)'
            ielts_desc = remove_tags(ielts_desc)
            #print(ielts_desc)

        except:
            ielts_desc = 'N/A'

            #print(ielts_desc)

        try:
            ielts = '6.5'
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
            career_en = response.xpath('//*[@id="section-5"]').extract()[0]
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
            apply_desc_en = '<div>Undergraduate degrees (BSc, BA, HND and Foundation degrees) If you are applying for a full-time undergraduate course, EU/ Non-EU students are strongly advised to apply online through the Universities & Colleges Admissions Service (UCAS). If you are using The Common Application, you can add the University of Worcester to your list of colleges via this link and complete the application there. You can get in touch with us before you apply to get advice on the offer you are likely to receive. For further details on when to apply, please see the Undergraduate How to apply section. Postgraduate degrees (MA, MSc, MBA) If you are applying for a place on a postgraduate course please apply directly to Worcester using the Overseas Application for Admission Form. For further details on when to apply, please refer to the Taught Postgraduate How to apply section. Applying through University of Worcester Overseas Representatives You also have the option to use the services of our recognised representatives overseas. They can give you advice and guide you through the process of applying. To see who we work with in your country, please visit the Overseas Representatives page. What do you need to include in your application? In order for us to process your application successfully, you will need to provide the following documents: All academic transcripts Copies of degree/diploma certificates Up to two academic references (depending on your course level and subject) An English language test score (IELTS/Cambridge Advanced, Pearson) Your personal statement Copy of your current passport or ID card It is important that you send this information to us - either paper copies by mail or scanned and emailed - as soon as possible. The International Team and Admissions Office will process your application and, if the application is complete, will endeavour to respond with a decision as soon as we can. Receiving an offer All applications to the University of Worcester are carefully considered by an admissions tutor (an academic member of staff from the relevant course area), whose job is to view applications. They will make one of the following offers or responses to you through UCAS: an Unconditional offer, (you have achieved the entry requirements) a Conditional offer (you need to achieve specified entry requirements before you are accepted) regretfully reject your application (this does not prevent you from applying again in a subsequent year) For full details about the different stages of the application process, please refer to the What happens to my application pages. Good luck with your preparation and we hope that you will become part of our International Community at the University of Worcester.</div>'
            #apply_desc_en = remove_tags(apply_desc_en)
            #apply_desc_en = "<div>" + apply_desc_en + "</div>"
            #print(apply_desc_en)
        except:
            apply_desc_en = ''

        try:
            apply_documents_en = '<p>All academic transcripts Copies of degree/diploma certificates Up to two academic references (depending on your course level and subject) An English language test score (IELTS/Cambridge Advanced, Pearson) Your personal statement Copy of your current passport or ID card</p>'
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
            # duration =  response.xpath('/html/body/div/div/div/div[2]/div[1]/div[2]/p[1]/strong').extract()[0]
            # duration = remove_tags(duration)
            duration = 3
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
            alevel = 'N/A'
            #print(alevel)
        try:
            ucascode = response.xpath('//body').extract()[0]
            ucascode = remove_tags(ucascode)
            ucascode = ucascode.replace('\r\n','')
            ucascode = ucascode.replace('\n','')
            ucascode = ucascode.replace('  ',' ')
            if 'Apply through UCAS' in ucascode:
                ucascode = re.findall('Apply through UCAS.*- (\w\w\w\w)',ucascode)[0] or re.findall('\(.*\)(\w\w\w\w)',ucascode)[0] or re.findall('Apply through UCAS.*– (\w\w\w\w)',ucascode)[0]
            elif 'Apply through UCAS' not in ucascode:
                ucascode = response.xpath('//*[@id="section-7"]/div[2]/div[2]/p[1]').extract()[0]
                ucascode = remove_tags(ucascode)
            else:
                ucascode = 'N/A'
            print(ucascode)
        except:

            ucascode = 'N/A'
            print(ucascode)
        try:
            tuition_fee = '12900'
            # tuition_fee = remove_tags(tuition_fee)
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
            #print(tuition_fee)
        except:
            tuition_fee = 0
            #print(tuition_fee)
        try:
            assessment_en = response.xpath('//*[@id="section-4"]/div[2]/div').extract()[0]
            assessment_en = remove_tags(assessment_en)
            assessment_en = assessment_en.replace('\r\n', '')
            assessment_en = assessment_en.replace('  ', '')
            assessment_en = assessment_en.replace('\n', '')
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
        item["batch_number"] = 4
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


