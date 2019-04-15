import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'University_of_Westminster_U'
    allowed_domains = []
    base_url= 'https://www.westminster.ac.uk%s'
    start_urls = []
    C = ['/accounting-finance-and-economics-courses/2019-20/september/full-time/accounting-bsc-honours',
'/art-and-design-television-film-and-moving-image-courses/2019-20/september/full-time/animation-ba-honours',
'/art-and-design-courses/2019-20/september/full-time/animation-with-foundation-ba-honours',
'/english-languages-courses/2019-20/september/full-time/arabic-and-english-language-ba-honours',
'/english-languages-courses/2019-20/september/full-time/arabic-and-english-literature-ba-honours',
'/languages-politics-and-international-relations-courses/2019-20/september/full-time/arabic-and-international-relations-ba-honours',
'/languages-linguistics-courses/2019-20/september/full-time/arabic-and-linguistics-ba-honours',
'/architecture-and-interiors-property-and-construction-courses/2019-20/september/full-time/architectural-technology-bsc-honours',
'/architecture-and-interiors-courses/2019-20/september/full-time/architecture-and-environmental-design-bsc-honours',
'/architecture-and-interiors-courses/2019-20/september/full-time/architecture-ba-honours',
'/biosciences-courses/2019-20/september/full-time/biochemistry-bsc-honours',
'/biosciences-courses/2019-20/september/full-time/biochemistry-with-foundation-bsc-honours',
'/biosciences-courses/2019-20/september/full-time/biological-sciences-bsc-honours',
'/biosciences-courses/2019-20/september/full-time/biological-sciences-with-foundation-bsc-honours',
'/biomedical-sciences-courses/2019-20/september/full-time/biomedical-sciences-bsc-honours',
'/biomedical-sciences-courses/2019-20/september/full-time/biomedical-sciences-with-foundation-bsc-honours',
'/property-and-construction-courses/2019-20/september/full-time/building-surveying-bsc-honours',
'/accounting-finance-and-economics-courses/2019-20/september/full-time/business-economics-bsc-honours',
'/business-information-systems-courses/2019-20/september/full-time/business-information-systems-bsc-honours',
'/business-information-systems-courses/2019-20/september/full-time/business-information-systems-with-foundation-bsc-honours',
'/accounting-finance-and-economics-business-and-management-courses/2019-20/september/full-time/business-management-accounting-ba-honours',
'/business-and-management-courses/2019-20/september/full-time/business-management-ba-honours',
'/accounting-finance-and-economics-business-and-management-courses/2019-20/september/full-time/business-management-economics-ba-honours',
'/business-and-management-courses/2019-20/september/full-time/business-management-entrepreneurship-ba-honours',
'/accounting-finance-and-economics-business-and-management-courses/2019-20/september/full-time/business-management-finance-ba-honours',
'/business-and-management-human-resource-management-courses/2019-20/september/full-time/business-management-human-resource-management-ba-honours',
'/business-and-management-marketing-courses/2019-20/september/full-time/business-management-marketing-ba-honours',
'/business-and-management-courses/2019-20/september/full-time/business-management-with-foundation-ba-honours',
'/english-languages-courses/2019-20/september/full-time/chinese-and-english-language-ba-honours',
'/english-languages-courses/2019-20/september/full-time/chinese-and-english-literature-ba-honours',
'/languages-politics-and-international-relations-courses/2019-20/september/full-time/chinese-and-international-relations-ba-honours',
'/languages-linguistics-courses/2019-20/september/full-time/chinese-and-linguistics-ba-honours',
'/psychology-courses/2019-20/september/full-time/cognitive-and-clinical-neuroscience-bsc-honours',
'/digital-media-and-games-computing-courses/2019-20/september/full-time/computer-games-development-bsc-honours',
'/digital-media-and-games-computing-courses/2019-20/september/full-time/computer-games-development-with-foundation-bsc-honours',
'/computer-and-network-engineering-courses/2019-20/september/full-time/computer-network-security-bsc-honours',
'/computer-and-network-engineering-courses/2019-20/september/full-time/computer-network-security-with-foundation-bsc-honours',
'/computer-science-and-software-engineering-courses/2019-20/september/full-time/computer-science-bsc-honours',
'/computer-science-and-software-engineering-courses/2019-20/september/full-time/computer-science-with-foundation-bsc-honours',
'/computer-and-network-engineering-courses/2019-20/september/full-time/computer-systems-engineering-bsc-honours',
'/computer-and-network-engineering-courses/2019-20/september/full-time/computer-systems-engineering-with-foundation-bsc-honours',
'/property-and-construction-courses/2019-20/september/full-time/construction-management-bsc-honours',
'/television-film-and-moving-image-photography-courses/2019-20/september/full-time/contemporary-media-practice-ba-honours',
'/television-film-and-moving-image-photography-courses/2019-20/september/full-time/contemporary-media-practice-with-foundation-ba-honours',
'/english-courses/2019-20/september/full-time/creative-writing-and-english-language-ba-honours',
'/english-courses/2019-20/september/full-time/creative-writing-and-english-literature-ba-honours',
'/english-courses/2019-20/september/full-time/creative-writing-and-english-literature-with-foundation-ba-honours',
'/criminology-courses/2019-20/september/full-time/criminology-ba-honours',
'/criminology-courses/2019-20/september/full-time/criminology-with-foundation-ba-honours',
'/architecture-and-interiors-planning-housing-and-urban-design-courses/2019-20/september/full-time/designing-cities-planning-and-architecture-ba-honours',
'/journalism-digital-media-and-pr-courses/2019-20/september/full-time/digital-media-and-communication-ba-honours',
'/business-information-systems-digital-media-and-games-computing-courses/2019-20/september/full-time/digital-media-development-bsc-honours',
'/digital-media-and-games-computing-courses/2019-20/september/full-time/digital-media-development-with-foundation-bsc-honours',
'/english-courses/2019-20/september/full-time/english-language-and-linguistics-with-foundation-ba-honours',
'/english-linguistics-courses/2019-20/september/full-time/english-language-and-linguistics-ba-honours',
'/english-history-courses/2019-20/september/full-time/english-literature-and-history-ba-honours',
'/english-courses/2019-20/september/full-time/english-literature-and-language-with-foundation-ba-honours',
'/english-courses/2019-20/september/full-time/english-literature-and-language-ba-honours',
'/english-courses/2019-20/september/full-time/english-literature-ba-honours',
'/english-courses/2019-20/september/full-time/english-literature-with-foundation-ba-honours',
'/law-courses/2019-20/september/full-time/european-legal-studies-llb-honours',
'/fashion-courses/2019-20/september/full-time/fashion-buying-management-ba-honours',
'/fashion-courses/2019-20/september/full-time/fashion-design-ba-honours',
'/fashion-courses/2019-20/september/full-time/fashion-marketing-and-promotion-ba-honours',
'/fashion-courses/2019-20/september/full-time/fashion-merchandise-management-ba-honours',
'/television-film-and-moving-image-courses/2019-20/september/full-time/film-ba-honours',
'/accounting-finance-and-economics-courses/2019-20/september/full-time/finance-bsc-honours',
'/art-and-design-courses/2019-20/september/full-time/fine-art-mixed-media-ba-honours',
'/art-and-design-courses/2019-20/september/full-time/fine-art-mixed-media-with-foundation-ba-honours',
'/english-languages-courses/2019-20/september/full-time/french-and-english-language-ba-honours',
'/english-languages-courses/2019-20/september/full-time/french-and-english-literature-ba-honours',
'/languages-politics-and-international-relations-courses/2019-20/september/full-time/french-and-international-relations-ba-honours',
'/languages-linguistics-courses/2019-20/september/full-time/french-and-linguistics-ba-honours',
'/languages-courses/2019-20/september/full-time/french-and-spanish-ba-honours',
'/art-and-design-courses/2019-20/september/full-time/graphic-communication-design-ba-honours',
'/art-and-design-courses/2019-20/september/full-time/graphic-communication-design-with-foundation-ba-honours',
'/history-politics-and-international-relations-courses/2019-20/september/full-time/history-and-politics-ba-honours',
'/history-courses/2019-20/september/full-time/history-ba-honours',
'/history-courses/2019-20/september/full-time/history-with-foundation-ba-honours',
'/nutrition-courses/2019-20/september/full-time/human-nutrition-bsc-honours',
'/nutrition-courses/2019-20/september/full-time/human-nutrition-with-foundation-bsc-honours',
'/business-and-management-human-resource-management-courses/2019-20/september/full-time/human-resource-management-ba-honours',
'/art-and-design-courses/2019-20/september/full-time/illustration-and-visual-communication-with-foundation-ba-honours',
'/art-and-design-courses/2019-20/september/full-time/illustration-and-visual-communication-ba-honours',
'/architecture-and-interiors-courses/2019-20/september/full-time/interior-architecture-ba-honours',
'/business-and-management-courses/2019-20/september/full-time/international-business-arabic-ba-honours',
'/business-and-management-courses/2019-20/september/full-time/international-business-ba-honours',
'/business-and-management-courses/2019-20/september/full-time/international-business-chinese-ba-honours',
'/business-and-management-courses/2019-20/september/full-time/international-business-french-ba-honours',
'/business-and-management-courses/2019-20/september/full-time/international-business-spanish-ba-honours',
'/business-and-management-marketing-courses/2019-20/september/full-time/international-marketing-ba-honours',
'/politics-and-international-relations-courses/2019-20/september/full-time/international-relations-and-development-with-foundation-ba-honours',
'/politics-and-international-relations-courses/2019-20/september/full-time/international-relations-and-development-ba-honours',
'/politics-and-international-relations-courses/2019-20/september/full-time/international-relations-ba-honours',
'/politics-and-international-relations-courses/2019-20/september/full-time/international-relations-with-foundation-ba-honours',
'/journalism-digital-media-and-pr-courses/2019-20/september/full-time/journalism-ba-honours',
'/law-courses/2019-20/september/full-time/law-llb-honours',
'/law-courses/2019-20/september/full-time/law-with-foundation-llb-honours',
'/law-courses/2019-20/september/full-time/law-with-french-law-llb-honours',
'/business-and-management-marketing-courses/2019-20/september/full-time/marketing-communications-ba-honours',
'/business-and-management-marketing-courses/2019-20/september/full-time/marketing-management-ba-honours',
'/law-courses/2019-20/september/full-time/m-law-integrated-masters-of-law',
'/languages-courses/2019-20/september/full-time/modern-languages-arabic-and-global-communication-with-foundation-ba-honours',
'/languages-courses/2019-20/september/full-time/modern-languages-arabic-and-global-communication-ba-honours',
'/languages-courses/2019-20/september/full-time/modern-languages-chinese-and-global-communication-with-foundation-ba-honours',
'/languages-courses/2019-20/september/full-time/modern-languages-chinese-and-global-communication-ba-honours',
'/languages-courses/2019-20/september/full-time/modern-languages-french-and-global-communication-with-foundation-ba-honours',
'/languages-courses/2019-20/september/full-time/modern-languages-french-and-global-communication-ba-honours',
'/languages-courses/2019-20/september/full-time/modern-languages-spanish-and-global-communication-with-foundation-ba-honours',
'/languages-courses/2019-20/september/full-time/modern-languages-spanish-and-global-communication-ba-honours',
'/music-courses/2019-20/september/full-time/music-production-performance-and-enterprise-ba-bmus',
'/biosciences-courses/2019-20/september/full-time/pharmacology-physiology-bsc-honours',
'/biosciences-courses/2019-20/september/full-time/pharmacology-and-physiology-with-foundation-bsc-honours',
'/photography-courses/2019-20/september/full-time/photography-ba-honours',
'/photography-courses/2019-20/september/full-time/photography-with-foundation-ba-honours',
'/politics-and-international-relations-courses/2019-20/september/full-time/politics-and-international-relations-with-foundation-ba-honours',
'/politics-and-international-relations-courses/2019-20/september/full-time/politics-and-international-relations-ba-honours',
'/politics-and-international-relations-courses/2019-20/september/full-time/politics-ba-honours',
'/politics-and-international-relations-courses/2019-20/september/full-time/politics-with-foundation-ba-honours',
'/planning-housing-and-urban-design-property-and-construction-courses/2019-20/september/full-time/property-and-planning-bsc-honours',
'/psychology-courses/2019-20/september/full-time/psychology-and-counselling-bsc-honours',
'/psychology-courses/2019-20/september/full-time/psychology-bsc-honours',
'/journalism-digital-media-and-pr-courses/2019-20/september/full-time/public-relations-and-advertising-ba-honours',
'/property-and-construction-courses/2019-20/september/full-time/quantity-surveying-and-commercial-management-bsc-honours',
'/journalism-digital-media-and-pr-courses/2019-20/september/full-time/radio-and-digital-production-ba-honours',
'/property-and-construction-courses/2019-20/september/full-time/real-estate-bsc-honours',
'/criminology-sociology-courses/2019-20/september/full-time/sociology-and-criminology-ba-honours',
'/sociology-courses/2019-20/september/full-time/sociology-ba-honours',
'/sociology-courses/2019-20/september/full-time/sociology-with-foundation-ba-honours',
'/computer-science-and-software-engineering-courses/2019-20/september/full-time/software-engineering-beng-honours',
'/computer-science-and-software-engineering-courses/2019-20/september/full-time/software-engineering-meng',
'/computer-science-and-software-engineering-courses/2019-20/september/full-time/software-engineering-with-foundation-beng-honours',
'/english-languages-courses/2019-20/september/full-time/spanish-and-english-language-ba-honours',
'/english-languages-courses/2019-20/september/full-time/spanish-and-english-literature-ba-honours',
'/languages-politics-and-international-relations-courses/2019-20/september/full-time/spanish-and-international-relations-ba-honours',
'/languages-linguistics-courses/2019-20/september/full-time/spanish-and-linguistics-ba-honours',
'/journalism-digital-media-and-pr-television-film-and-moving-image-courses/2019-20/september/full-time/television-production-ba-honours',
'/english-courses/2019-20/september/full-time/theatre-studies-and-creative-writing-ba-honours',
'/english-courses/2019-20/september/full-time/theatre-studies-and-english-literature-ba-honours',
'/tourism-and-events-courses/2019-20/september/full-time/tourism-and-events-management-ba-honours',
'/tourism-and-events-courses/2019-20/september/full-time/tourism-planning-and-management-ba-honours',
'/tourism-and-events-courses/2019-20/september/full-time/tourism-with-business-ba-honours',
'/languages-courses/2019-20/september/full-time/translation-studies-french-ba-honours',
'/languages-courses/2019-20/september/full-time/translation-studies-french-with-foundation-ba-honours',
'/languages-courses/2019-20/september/full-time/translation-studies-spanish-ba-honours',
'/languages-courses/2019-20/september/full-time/translation-studies-spanish-with-foundation-ba-honours',]

#     C = [
#         'https://www.westminster.ac.uk/english-languages-courses/2018-19/september/full-time/arabic-and-english-literature-ba-honours',
#         'https://www.westminster.ac.uk/languages-courses/2019-20/september/full-time/modern-languages-arabic-and-global-communication-ba-honours',
#         ' https://www.westminster.ac.uk/journalism-digital-media-and-pr-television-film-and-moving-image-courses/2018-19/september/full-time/television-production-ba-honours',
#         'https://www.westminster.ac.uk/accounting-finance-and-economics-courses/2019-20/september/full-time/accounting-bsc-honours',
# 'https://www.westminster.ac.uk/english-languages-courses/2019-20/september/full-time/arabic-and-english-literature-ba-honours',
# 'https://www.westminster.ac.uk/biosciences-courses/2019-20/september/full-time/biochemistry-bsc-honours',
# 'https://www.westminster.ac.uk/biosciences-courses/2019-20/september/full-time/biological-sciences-bsc-honours',
# 'https://www.westminster.ac.uk/biomedical-sciences-courses/2019-20/september/sandwich/biomedical-sciences-bsc-honours',
# 'https://www.westminster.ac.uk/accounting-finance-and-economics-business-and-management-courses/2019-20/september/full-time/business-management-finance-ba-honours',
# 'https://www.westminster.ac.uk/television-film-and-moving-image-photography-courses/2019-20/september/full-time/contemporary-media-practice-with-foundation-ba-honours',
# 'https://www.westminster.ac.uk/english-courses/2019-20/september/full-time/creative-writing-and-english-literature-ba-honours',
# 'https://www.westminster.ac.uk/business-information-systems-digital-media-and-games-computing-courses/2019-20/september/full-time/digital-media-development-bsc-honours',
# 'https://www.westminster.ac.uk/english-courses/2019-20/september/full-time/english-literature-ba-honours',
# 'https://www.westminster.ac.uk/english-courses/2019-20/september/full-time/english-literature-with-foundation-ba-honours',
# 'https://www.westminster.ac.uk/fashion-courses/2019-20/september/full-time/fashion-buying-management-ba-honours',
# 'https://www.westminster.ac.uk/fashion-courses/2019-20/september/sandwich/fashion-design-ba-honours',
# 'https://www.westminster.ac.uk/art-and-design-courses/2019-20/september/full-time/graphic-communication-design-with-foundation-ba-honours',
# 'https://www.westminster.ac.uk/history-politics-and-international-relations-courses/2019-20/september/full-time/history-and-politics-ba-honours',
# 'https://www.westminster.ac.uk/nutrition-courses/2019-20/september/full-time/human-nutrition-bsc-honours',
# 'https://www.westminster.ac.uk/business-and-management-courses/2019-20/september/full-time/international-business-ba-honours',
# 'https://www.westminster.ac.uk/business-and-management-courses/2019-20/september/full-time/international-business-chinese-ba-honours',
# 'https://www.westminster.ac.uk/business-and-management-courses/2019-20/september/full-time/international-business-french-ba-honours',
# 'https://www.westminster.ac.uk/politics-and-international-relations-courses/2019-20/september/full-time/politics-and-international-relations-ba-honours',
# 'https://www.westminster.ac.uk/politics-and-international-relations-courses/2019-20/september/full-time/politics-with-foundation-ba-honours',
# 'https://www.westminster.ac.uk/sociology-courses/2019-20/september/full-time/sociology-ba-honours',
# 'https://www.westminster.ac.uk/english-languages-courses/2019-20/september/full-time/spanish-and-english-language-ba-honours',
# 'https://www.westminster.ac.uk/languages-politics-and-international-relations-courses/2019-20/september/full-time/spanish-and-international-relations-ba-honours',
# 'https://www.westminster.ac.uk/journalism-digital-media-and-pr-television-film-and-moving-image-courses/2019-20/september/full-time/television-production-ba-honours',
# 'https://www.westminster.ac.uk/languages-courses/2019-20/september/full-time/translation-studies-spanish-with-foundation-ba-honours',]
    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'University of Westminster'
        try:
            location = response.xpath('//*[@id="location"]/a').extract()[0]
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
            degree_name = response.xpath('/html/body/div[2]/div[2]/div/header/h1/span').extract()[0]
            degree_name = remove_tags(degree_name)
            #degree_name = degree_name.split()[0]

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
            programme_en = response.xpath('/html/body/div[2]/div[2]/div/header/h1/text()').extract()[0]
            #programme_en = remove_tags(programme_en)
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
            overview_en = response.xpath('/html/body/div[4]/div/section/div[2]/div[4]/div[1]').extract()[0]
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
            modules_en = response.xpath('/html/body/div[4]/div/section/div[2]/div[4]/div[2]').extract()[0]
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
            rntry_requirements_en = response.xpath('//div[@class = "layout__1col"]').extract()[0]
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
            require_chinese_en = '<div>Applying for a course If you are interested in studying for a Master\'s degree (eg MA, MSc or LLM) or research programme (eg MPhil or PhD) at the University of Westminster, you will need to check that you meet our entry requirements. We have included typical entry requirements below, but these are simply a guideline. Some courses may also have specific subject or grade requirements, which will be listed on individual course pages. For entry to a Master\'s degree that requires a UK 2:2 degree, you will typically need to have one of the following: Bachelor degree from 211, 985 or top national universities with an overall average grade of 70% Bachelor degree from national universities with an overall average grade of 75% Bachelor degree from high-ranking private universities with an overall average grade of 75% Master degrees with an overall average grade of 60% For entry to a Master\'s degree that requires a UK 2:1 degree, you will typically need to have one of the following: Bachelor degree from 211, 985 or top national universities with an overall average grade of 75% Bachelor degree from national universities with an overall average grade of 80% Bachelor degree from high-ranking private universities with an overall average grade of 80% Master degrees with an overall average grade of 70% For more details on the application process, visit our How to apply page. To search or browse our postgraduate courses, visit our Postgraduate page. If your qualifications are not listed If your qualifications are not listed above, you may still be able to apply for entry to our courses – just get in touch with our overseas representatives or course enquiries team via the contact details on this page. If you find that your qualifications do not meet our entry requirements, you may want to consider applying for one of the University preparation courses offered by our partner college – see below for details. University preparation courses Our partner college, Kaplan International College London, offers a Pre-Master\'s course leading to entry to a number of our Master\'s degrees. To find out more and apply, visit the Kaplan International College London website.</div>'
        except:
            require_chinese_en = ''
        try:
            ielts_desc = ''
            #print(ielts_desc)

        except:
            ielts_desc = 'N/A'

            #print(ielts_desc)

        try:
            ielts = response.xpath('//body').extract()[0]
            ielts = remove_tags(ielts)
            ielts = ielts.replace('\r\n','')
            ielts = ielts.replace('\n','')
            #ielts = re.findall('International Baccalaureate(.*)',ielts)[0]

            ielts = re.findall('IELTS(.*)',ielts)[0]
            ielts = re.findall('(\d\.\d)',ielts)[0]
            #print(ielts)

        except:

            ielts = '0'
            #print(ielts)
        try:
            ielts_l = response.xpath('//body').extract()[0]
            ielts_l = remove_tags(ielts_l)
            ielts_l = re.findall('IELTS(.*)',ielts_l)[0]
            ielts_l = re.findall('(\d\.\d)',ielts_l)[1]
            print(ielts_l)
            #ielts_l = remove_tags(ielts_l)
        except:
            ielts_l = 0

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
            career_en = response.xpath('/html/body/div[4]/div/section/div[2]/div[14]/div').extract()[0]
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
            apply_desc_en = '<p>To apply for a postgraduate course, simply click on the red \'Apply\' button at the top of our course pages. You will be directed to the UCAS Postgraduate website to make your application. When completing the application form on UCAS Postgraduate remember to specify: why you wish to enrol on the course any relevant experience you have why you think you should be given a place</p>'
            #apply_desc_en = remove_tags(apply_desc_en)
            #apply_desc_en = "<div>" + apply_desc_en + "</div>"
            #print(apply_desc_en)
        except:
            apply_desc_en = ''

        try:
            apply_documents_en = '<span>why you wish to enrol on the course any relevant experience you have why you think you should be given a place<\span>'
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
            duration =  response.xpath('/html/body/div[4]/div/section/div[2]/div[2]/div/div[2]/div[2]/div/span[2]').extract()[0]
            duration = remove_tags(duration)
            #duration = remove_tags(duration)
            #duration = re.findall('(\d) Years',duration)[0]
            if '6' in duration:
                duration = '6'
            elif '5' in duration:
                duration = '5'
            elif '4' in duration:
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
            ib = response.xpath('//*[@id]/div/div/div/ul[1]/li[2]').extract()[0]
            ib = remove_tags(ib)
            #print(ib)
        except:
            ib = ''
            #print(ib)

        try:
            alevel = response.xpath('//*[@id]/div/div/div/ul[1]/li[1]').extract()[0]
            alevel = remove_tags(alevel)
            #alevel = re.findall("(\w\w\w) at A Level",alevel)[0]
            #print(alevel)
        except:
            alevel = 'N/A'
            #print(alevel)
        try:
            ucascode = response.xpath('//*[@id="js-anchor-nav"]/div/div/div/div/p/strong[1]').extract()[0]
            ucascode = remove_tags(ucascode)

            #print(ucascode)
        except:
            ucascode = ''
            #print(ucascode)

        try:
            tuition_fee = response.xpath('/html/body/div[4]/div/section/div[2]/div[2]/div/div[2]/div[1]/div[2]/span[2]/a').extract()[0]
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

        assessment_en = ''
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


