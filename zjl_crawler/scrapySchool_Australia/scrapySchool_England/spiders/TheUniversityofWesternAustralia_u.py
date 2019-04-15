# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/19 13:22'
import scrapy,json
import re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from w3lib.html import remove_tags
from scrapySchool_England.clearSpace import clear_space_str
class TheUniversityofWesternAustraliaSpider(scrapy.Spider):
    name = 'TheUniversityofWesternAustralia_u'
    allowed_domains = ['uwa.edu.au/']
    start_urls = []
    C = [
        'https://study.uwa.edu.au/Courses/Conservation-Biology',
        'https://study.uwa.edu.au/Courses/Conservation-Biology',
        'https://study.uwa.edu.au/Courses/Professional-Economics',
        'https://study.uwa.edu.au/Courses/Professional-Economics',
        'https://study.uwa.edu.au/Courses/Professional-Economics',
        'https://study.uwa.edu.au/Courses/Professional-Economics',
        'https://study.uwa.edu.au/Courses/Pharmacology',
        'https://study.uwa.edu.au/Courses/Pharmacology',
        'https://study.uwa.edu.au/Courses/Pharmacology',
        'https://study.uwa.edu.au/Courses/Pharmacology',
        'https://study.uwa.edu.au/Courses/Marine-Science',
        'https://study.uwa.edu.au/Courses/Marine-Science',
        'https://study.uwa.edu.au/Courses/Marine-Science',
        'https://study.uwa.edu.au/Courses/Marine-Science',
        'https://study.uwa.edu.au/Courses/Environmental-Science',
        'https://study.uwa.edu.au/Courses/Environmental-Science',
        'https://study.uwa.edu.au/Courses/Environmental-Science',
        'https://study.uwa.edu.au/Courses/Environmental-Science',
        'https://study.uwa.edu.au/Courses/Anthropology-and-Sociology',
        'https://study.uwa.edu.au/Courses/Anthropology-and-Sociology',
        'https://study.uwa.edu.au/Courses/Anthropology-and-Sociology',
        'https://study.uwa.edu.au/Courses/Anthropology-and-Sociology',
        'https://study.uwa.edu.au/Courses/Chemistry',
        'https://study.uwa.edu.au/Courses/Chemistry',
        'https://study.uwa.edu.au/Courses/Chemistry',
        'https://study.uwa.edu.au/Courses/Chemistry',
        'https://study.uwa.edu.au/Courses/Genetics',
        'https://study.uwa.edu.au/Courses/Genetics',
        'https://study.uwa.edu.au/Courses/Genetics',
        'https://study.uwa.edu.au/Courses/Genetics',
        'https://study.uwa.edu.au/Courses/Genetics',
        'https://study.uwa.edu.au/Courses/Genetics',
        'https://study.uwa.edu.au/Courses/English-and-Cultural-Studies',
        'https://study.uwa.edu.au/Courses/English-and-Cultural-Studies',
        'https://study.uwa.edu.au/Courses/English-and-Cultural-Studies',
        'https://study.uwa.edu.au/Courses/English-and-Cultural-Studies',
        'https://study.uwa.edu.au/Courses/Marketing',
        'https://study.uwa.edu.au/Courses/Marketing',
        'https://study.uwa.edu.au/Courses/Marketing',
        'https://study.uwa.edu.au/Courses/Marketing',
        'https://study.uwa.edu.au/Courses/Pathology-and-Laboratory-Medicine',
        'https://study.uwa.edu.au/Courses/Pathology-and-Laboratory-Medicine',
        'https://study.uwa.edu.au/Courses/Pathology-and-Laboratory-Medicine',
        'https://study.uwa.edu.au/Courses/Pathology-and-Laboratory-Medicine',
        'https://study.uwa.edu.au/Courses/Psychological-Science',
        'https://study.uwa.edu.au/Courses/Psychological-Science',
        'https://study.uwa.edu.au/Courses/Psychological-Science',
        'https://study.uwa.edu.au/Courses/Psychological-Science',
        'https://study.uwa.edu.au/Courses/Italian-Studies',
        'https://study.uwa.edu.au/Courses/Italian-Studies',
        'https://study.uwa.edu.au/Courses/Italian-Studies',
        'https://study.uwa.edu.au/Courses/Italian-Studies',
        'https://study.uwa.edu.au/Courses/Anatomy-and-Human-Biology',
        'https://study.uwa.edu.au/Courses/Anatomy-and-Human-Biology',
        'https://study.uwa.edu.au/Courses/Anatomy-and-Human-Biology',
        'https://study.uwa.edu.au/Courses/Anatomy-and-Human-Biology',
        'https://study.uwa.edu.au/Courses/Anatomy-and-Human-Biology',
        'https://study.uwa.edu.au/Courses/Anatomy-and-Human-Biology',
        'https://study.uwa.edu.au/Courses/Management',
        'https://study.uwa.edu.au/Courses/Management',
        'https://study.uwa.edu.au/Courses/Management',
        'https://study.uwa.edu.au/Courses/Management',
        'https://study.uwa.edu.au/Courses/Human-Resource-Management',
        'https://study.uwa.edu.au/Courses/Human-Resource-Management',
        'https://study.uwa.edu.au/Courses/Human-Resource-Management',
        'https://study.uwa.edu.au/Courses/Human-Resource-Management',
        'https://study.uwa.edu.au/Courses/Physiology',
        'https://study.uwa.edu.au/Courses/Physiology',
        'https://study.uwa.edu.au/Courses/Physiology',
        'https://study.uwa.edu.au/Courses/Physiology',
        'https://study.uwa.edu.au/Courses/Accounting',
        'https://study.uwa.edu.au/Courses/Accounting',
        'https://study.uwa.edu.au/Courses/Accounting',
        'https://study.uwa.edu.au/Courses/Accounting',
        'https://study.uwa.edu.au/Courses/Microbiology-and-Immunology',
        'https://study.uwa.edu.au/Courses/Microbiology-and-Immunology',
        'https://study.uwa.edu.au/Courses/Microbiology-and-Immunology',
        'https://study.uwa.edu.au/Courses/Microbiology-and-Immunology',
        'https://study.uwa.edu.au/Courses/Psychology-in-Society',
        'https://study.uwa.edu.au/Courses/Psychology-in-Society',
        'https://study.uwa.edu.au/Courses/Psychology-in-Society',
        'https://study.uwa.edu.au/Courses/Psychology-in-Society',
        'https://study.uwa.edu.au/Courses/Architecture',
        'https://study.uwa.edu.au/Courses/History-of-Art',
        'https://study.uwa.edu.au/Courses/History-of-Art',
        'https://study.uwa.edu.au/Courses/Sport-Science',
        'https://study.uwa.edu.au/Courses/Sport-Science',
        'https://study.uwa.edu.au/Courses/Linguistics',
        'https://study.uwa.edu.au/Courses/Linguistics',
        'https://study.uwa.edu.au/Courses/Natural-Resource-Management',
        'https://study.uwa.edu.au/Courses/Natural-Resource-Management',
        'https://study.uwa.edu.au/Courses/Exercise-and-Health',
        'https://study.uwa.edu.au/Courses/Exercise-and-Health',
        'https://study.uwa.edu.au/Courses/Exercise-and-Health',
        'https://study.uwa.edu.au/Courses/Landscape-Architecture',
        'https://study.uwa.edu.au/Courses/Landscape-Architecture',
        'https://study.uwa.edu.au/Courses/Geology',
        'https://study.uwa.edu.au/Courses/Geology',
        'https://study.uwa.edu.au/Courses/Political-Science-and-International-Relations',
        'https://study.uwa.edu.au/Courses/Political-Science-and-International-Relations',
        'https://study.uwa.edu.au/Courses/Music-Studies',
        'https://study.uwa.edu.au/Courses/Music-Studies',
        'https://study.uwa.edu.au/Courses/Archaeology',
        'https://study.uwa.edu.au/Courses/Archaeology',
        'https://study.uwa.edu.au/Courses/Law-and-Society',
        'https://study.uwa.edu.au/Courses/Law-and-Society',
        'https://study.uwa.edu.au/Courses/Philosophy',
        'https://study.uwa.edu.au/Courses/Philosophy',
        'https://study.uwa.edu.au/Courses/Physics',
        'https://study.uwa.edu.au/Courses/Physics',
        'https://study.uwa.edu.au/Courses/Music-General-Studies',
        'https://study.uwa.edu.au/Courses/Music-General-Studies',
        'https://study.uwa.edu.au/Courses/Classics-and-Ancient-History',
        'https://study.uwa.edu.au/Courses/Classics-and-Ancient-History',
        'https://study.uwa.edu.au/Courses/Music-Electronic-Music-and-Sound-Design',
        'https://study.uwa.edu.au/Courses/Music-Electronic-Music-and-Sound-Design',
        'https://study.uwa.edu.au/Courses/Computer-Science',
        'https://study.uwa.edu.au/Courses/Computer-Science',
        'https://study.uwa.edu.au/Courses/Asian-Studies',
        'https://study.uwa.edu.au/Courses/Asian-Studies',
        'https://study.uwa.edu.au/Courses/Work-and-Employment-Relations',
        'https://study.uwa.edu.au/Courses/Work-and-Employment-Relations',
        'https://study.uwa.edu.au/Courses/Indigenous-Knowledge-History-and-Heritage',
        'https://study.uwa.edu.au/Courses/Indigenous-Knowledge-History-and-Heritage',
        'https://study.uwa.edu.au/Courses/Fine-Arts',
        'https://study.uwa.edu.au/Courses/Fine-Arts',
        'https://study.uwa.edu.au/Courses/Music-Specialist-Studies',
        'https://study.uwa.edu.au/Courses/Music-Specialist-Studies',
        'https://study.uwa.edu.au/Courses/Data-Science',
        'https://study.uwa.edu.au/Courses/Data-Science',
        'https://study.uwa.edu.au/Courses/Communication-and-Media-Studies',
        'https://study.uwa.edu.au/Courses/Communication-and-Media-Studies',
        'https://study.uwa.edu.au/Courses/Mathematics-and-Statistics',
        'https://study.uwa.edu.au/Courses/Mathematics-and-Statistics',
        'https://study.uwa.edu.au/Courses/Japanese',
        'https://study.uwa.edu.au/Courses/Japanese',
        'https://study.uwa.edu.au/Courses/Aboriginal-Health-and-Wellbeing',
        'https://study.uwa.edu.au/Courses/Aboriginal-Health-and-Wellbeing',
        'https://study.uwa.edu.au/Courses/Biochemistry-and-Molecular-Biology',
        'https://study.uwa.edu.au/Courses/Engineering-Science',
        'https://study.uwa.edu.au/Courses/Biochemistry-and-Molecular-Biology',
        'https://study.uwa.edu.au/Courses/Engineering-Science',
        'https://study.uwa.edu.au/Courses/Biochemistry-and-Molecular-Biology',
        'https://study.uwa.edu.au/Courses/Human-Geography-and-Planning',
        'https://study.uwa.edu.au/Courses/Biochemistry-and-Molecular-Biology',
        'https://study.uwa.edu.au/Courses/Human-Geography-and-Planning',
        'https://study.uwa.edu.au/Courses/Biochemistry-and-Molecular-Biology',
        'https://study.uwa.edu.au/Courses/Biochemistry-and-Molecular-Biology',
        'https://study.uwa.edu.au/Courses/Korean-Studies',
        'https://study.uwa.edu.au/Courses/Economics',
        'https://study.uwa.edu.au/Courses/Korean-Studies',
        'https://study.uwa.edu.au/Courses/Economics',
        'https://study.uwa.edu.au/Courses/Economics',
        'https://study.uwa.edu.au/Courses/Economics',
        'https://study.uwa.edu.au/Courses/Finance',
        'https://study.uwa.edu.au/Courses/Finance',
        'https://study.uwa.edu.au/Courses/Indonesian',
        'https://study.uwa.edu.au/Courses/Finance',
        'https://study.uwa.edu.au/Courses/Indonesian',
        'https://study.uwa.edu.au/Courses/Finance',
        'https://study.uwa.edu.au/Courses/History',
        'https://study.uwa.edu.au/Courses/History',
        'https://study.uwa.edu.au/Courses/History',
        'https://study.uwa.edu.au/Courses/History',
        'https://study.uwa.edu.au/Courses/Population-Health',
        'https://study.uwa.edu.au/Courses/Population-Health',
        'https://study.uwa.edu.au/Courses/German-Studies',
        'https://study.uwa.edu.au/Courses/Population-Health',
        'https://study.uwa.edu.au/Courses/German-Studies',
        'https://study.uwa.edu.au/Courses/Population-Health',
        'https://study.uwa.edu.au/Courses/Botany',
        'https://study.uwa.edu.au/Courses/Botany',
        'https://study.uwa.edu.au/Courses/Botany',
        'https://study.uwa.edu.au/Courses/Botany',
        'https://study.uwa.edu.au/Courses/Zoology',
        'https://study.uwa.edu.au/Courses/Zoology',
        'https://study.uwa.edu.au/Courses/Zoology',
        'https://study.uwa.edu.au/Courses/Zoology',
        'https://study.uwa.edu.au/Courses/Business-Law',
        'https://study.uwa.edu.au/Courses/Business-Law',
        'https://study.uwa.edu.au/Courses/Business-Law',
        'https://study.uwa.edu.au/Courses/Business-Law',
        'https://study.uwa.edu.au/Courses/Conservation-Biology',
        'https://study.uwa.edu.au/Courses/Conservation-Biology'
    ]
    # print(len(C))
    C = set(C)
    # print(len(C))
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'The University of Western Australia'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="page-content"]/div[1]/div[3]/div/div/div[3]/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.overview_en
        overview_en = response.xpath('//*[@id="course-details"]/div/div/div/section/div[1]/div[1]/div[1]/div/div').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #5.modules_en
        modules_en = response.xpath("//h2[contains(text(),'Course structure details')]//following-sibling::*").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        modules_en = clear_space_str(modules_en)
        # print(modules_en)

        #6.apply_pre
        apply_pre = '$'



        #8.start_date
        start_date = response.xpath("//*[contains(text(),'Starting dates')]//following-sibling::*").extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date).strip()
        if 'January' in start_date:
            start_date = '2019-1'
        else:
            start_date = 'Semester1,Semester2'
        # print(start_date)

        #9.career_en
        career_en = response.xpath('//*[@id="careers-and-further-study"]/div/div/div/section/div[2]/div/div/div/a').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en).strip()
        # print(career_en)

        #10.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'Fee')]//following-sibling::div").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee,response.url)

        #11.tuition_fee_pre
        tuition_fee_pre = '$'

        #12.rntry_requirements_en
        rntry_requirements_en = response.xpath("//h3[contains(text(),'Admission requirements')]//following-sibling::div[1]").extract()
        rntry_requirements_en = ''.join(rntry_requirements_en)
        rntry_requirements_en = remove_class(rntry_requirements_en)
        # print(rntry_requirements_en)

        #13.ielts 14151617
        if 'Law' in programme_en:
            ielts = 7.0
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_l = 6.5
            ielts_s = 6.5
        else:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_l = 6.0
            ielts_s = 6.0

        #18.toefl 19202122
        if 'Law' in programme_en:
            toefl = 100
            toefl_s = 28
            toefl_l = 26
            toefl_r = 26
            toefl_w = 26
        else:
            toefl = 82
            toefl_s = 20
            toefl_l = 20
            toefl_r = 18
            toefl_w = 22

        #23.apply_proces_en
        apply_proces_en = 'Check your chosen course is open to applications. Ensure you meet the admission requirements for this course as detailed on the previous tab. Ensure you meet our English language competency requirement and any course/major prerequisites. Apply'

        #24.apply_fee
        apply_fee= 100

        #25.china_score_requirements
        try:
            china_score_requirements = response.xpath("//*[contains(text(),'Chinese Gao Kao')]//following-sibling::div/ul/li").extract()[0]
            china_score_requirements = remove_tags(china_score_requirements)
        except:
            china_score_requirements = ''
        #26.degree_type
        degree_type = 1



        #28.department
        department = response.xpath("//*[contains(text(),'Faculty')]//following-sibling::div[1]/ul/li[1]").extract()
        department = ''.join(department)
        department = remove_tags(department).replace('&amp;','')
        # print(department)

        #29.duration_per
        duration_per = 1

        #30.duration
        duration_list = response.xpath("//*[contains(text(),'duration')]//following-sibling::div[1]/ul/li[1]").extract()
        duration_list = ''.join(duration_list)
        # print(duration_list)
        try:
            duration = re.findall('\d',duration_list)[0]
        except:
            duration = 3
        # print(duration)

        # 7.location
        location = response.xpath("//*[contains(text(),'Locations')]//following-sibling::*").extract()[0]
        # location = ''.join(location)
        location = remove_tags(location).strip()
        # location = clear_space_str(location)
        if 'Perth' in location and 'Albany' in location:
            location = 'Albany,Perth'
        else:location = location

        item['location'] = location
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['department'] = department
        item['degree_type'] = degree_type
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['start_date'] = start_date
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['rntry_requirements_en'] = rntry_requirements_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['toefl_w'] = toefl_w
        item['apply_proces_en'] = apply_proces_en
        item['apply_pre'] = apply_pre
        item['apply_fee'] = apply_fee
        item['china_score_requirements'] = china_score_requirements


        # 27.degree_name
        degree_name = response.xpath("//*[contains(text(),'Degrees course is available in')]//following-sibling::div[1]//ul//li").extract()
        if len(degree_name)!=0:
            for i in degree_name:
                degree_name = i
                degree_name = degree_name.replace('<li>','').replace('</li>','')
                item['degree_name'] = degree_name
                yield item
        else:
            item['degree_name'] = ''
            yield item

