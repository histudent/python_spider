# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/30 9:24'
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
import requests
from lxml import etree
import urllib.request
class MurdochUniversitySpider(scrapy.Spider):
    name = 'MurdochUniversity_u'
    allowed_domains = ['murdoch.edu.au/']
    start_urls = []
    C= [
        'https://www.murdoch.edu.au/study/courses/course-details/international-business-(bbus)',
        'https://www.murdoch.edu.au/study/courses/course-details/marine-biology-(bsc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Physics-and-Nanotechnology-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Internetworking-and-Network-Security-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Animal-Health-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Environmental-Management-and-Sustainability-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Animal-Science-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Marketing-(BBus)',
        'https://www.murdoch.edu.au/study/courses/course-details/Games-Technology-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Cyber-Security-and-Forensics-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Marine-Science-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Environmental-Science-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/History-(BA)',
        'https://www.murdoch.edu.au/study/courses/course-details/Strategic-Communication-(BCommun)',
        'https://www.murdoch.edu.au/study/courses/course-details/Genetics-and-Molecular-Biology-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Banking-(BBus)',
        'https://www.murdoch.edu.au/study/courses/course-details/Laboratory-Medicine-(BScBLabMed)',
        'https://www.murdoch.edu.au/study/courses/course-details/Global-Media-and-Communication-(BCommun)',
        'https://www.murdoch.edu.au/study/courses/course-details/Clinical-Laboratory-Science-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/English-and-Creative-Writing-(BA)',
        'https://www.murdoch.edu.au/study/courses/course-details/law-(llb-llb(hons))',
        'https://www.murdoch.edu.au/study/courses/course-details/Instrumentation-and-Control-Engineering-Honours-(BE(Hons))',
        'https://www.murdoch.edu.au/study/courses/course-details/Crime-Science-(BCrim)',
        'https://www.murdoch.edu.au/study/courses/course-details/Legal-Studies-(BCrim)',
        'https://www.murdoch.edu.au/study/courses/course-details/Sociology-(BA)',
        'https://www.murdoch.edu.au/study/courses/course-details/Community-Development-(BA)',
        'https://www.murdoch.edu.au/study/courses/course-details/Japanese-(BA)',
        'https://www.murdoch.edu.au/study/courses/course-details/Crop-and-Pasture-Science-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Industrial-Computer-Systems-Engineering-Honours-(BE(Hons))',
        'https://www.murdoch.edu.au/study/courses/course-details/Tourism-and-Events-(BA)',
        'https://www.murdoch.edu.au/study/courses/course-details/Finance-(BBus)',
        'https://www.murdoch.edu.au/study/courses/course-details/Indonesian-(BA)',
        'https://www.murdoch.edu.au/study/courses/course-details/Screen-Production-(BCrMedia)',
        'https://www.murdoch.edu.au/study/courses/course-details/Global-Politics-and-Policy-(BA)',
        'https://www.murdoch.edu.au/study/courses/course-details/Biomedical-Science-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Computer-Science-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Primary-1-10-Health-and-Physical-Education-(BEd)',
        'https://www.murdoch.edu.au/study/courses/course-details/Mathematics-and-Statistics-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Nursing-(BNurs)',
        'https://www.murdoch.edu.au/study/courses/course-details/law-psychology-combined-(llb-bsc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Journalism-(BCommun)',
        'https://www.murdoch.edu.au/study/courses/course-details/Criminal-Behaviour-(BCrim)',
        'https://www.murdoch.edu.au/study/courses/course-details/Accounting-(BBus)',
        'https://www.murdoch.edu.au/study/courses/course-details/Business-Law-(BBus)',
        'https://www.murdoch.edu.au/study/courses/course-details/Psychology-(BA)',
        'https://www.murdoch.edu.au/study/courses/course-details/Chemical-and-Metallurgical-Engineering-Honours-(BE(Hons))',
        'https://www.murdoch.edu.au/study/courses/course-details/Mineral-Science-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/International-Aid-and-Development-(BA)',
        'https://www.murdoch.edu.au/study/courses/course-details/Electrical-Power-Engineering-Honours-(BE(Hons))',
        'https://www.murdoch.edu.au/study/courses/course-details/Law--Arts-(Combined)-(LLB)(BA)',
        'https://www.murdoch.edu.au/study/courses/course-details/Human-Resources-Management-(BBus)',
        'https://www.murdoch.edu.au/study/courses/course-details/sport-and-health-science-(bsc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Law--Science-(Combined)-(LLB)(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Conservation-and-Wildlife-Biology-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Games-Art-and-Design-(BCrMedia)',
        'https://www.murdoch.edu.au/study/courses/course-details/Biological-Sciences-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Sport-and-Exercise-Science-(BSportExSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Chemistry-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/terrorism-and-counterterrorism-studies-(bgs)',
        'https://www.murdoch.edu.au/study/courses/course-details/Sustainable-Development-(BA)',
        'https://www.murdoch.edu.au/study/courses/course-details/Photography-(BCrMedia)',
        'https://www.murdoch.edu.au/study/courses/course-details/Sound-(BCrMedia)',
        'https://www.murdoch.edu.au/study/courses/course-details/Veterinary-Science-(BSc)(DVM)',
        'https://www.murdoch.edu.au/study/courses/course-details/Theatre-and-Drama-(BA)',
        'https://www.murdoch.edu.au/study/courses/course-details/Management-(BBus)',
        'https://www.murdoch.edu.au/study/courses/course-details/Mobile-and-Web-Application-Development-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Primary-Teaching-(BEd)',
        'https://www.murdoch.edu.au/study/courses/course-details/Engineering-Technology-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Graphic-Design-(BCrMedia)',
        'https://www.murdoch.edu.au/study/courses/course-details/Early-Childhood-and-Primary-Teaching-(BEd)',
        'https://www.murdoch.edu.au/study/courses/course-details/law-psychology-combined-(llb-ba)',
        'https://www.murdoch.edu.au/study/courses/course-details/Environmental-Engineering-Honours-(BE(Hons))',
        'https://www.murdoch.edu.au/study/courses/course-details/Renewable-Energy-Engineering-Honours-(BE(Hons))',
        'https://www.murdoch.edu.au/study/courses/course-details/Psychology-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Forensic-Biology-and-Toxicology-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Business-Information-Systems-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Games-Software-Design-and-Production-(BSc)',
        'https://www.murdoch.edu.au/study/courses/course-details/Hospitality-and-Tourism-Management-(BBus)',
        'https://www.murdoch.edu.au/study/courses/course-details/Philosophy-(BA)'
    ]
    # print(len(C))
    C= set(C)
    # print(len(C))
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Murdoch University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.degree_name
        degree_name =response.xpath('//*[@id="course-overview"]/div/div/div/div/h3').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name).strip()
        if 'Bachelor of Laws Honours' in degree_name:
            degree_name = 'Bachelor of Laws Honours'
        elif 'Bachelor of Science' in degree_name:
            degree_name = 'Bachelor of Science'
        elif 'Bachelor of Education' in degree_name:
            degree_name = 'Bachelor of Education'
        elif 'Bachelor of Business' in degree_name:
            degree_name = 'Bachelor of Business'
        elif 'Bachelor of Arts' in degree_name:
            degree_name = 'Bachelor of Arts'
        elif 'Bachelor of Engineering' in degree_name:
            degree_name = 'Bachelor of Engineering'
        elif 'Bachelor of Creative Media' in degree_name:
            degree_name = 'Bachelor of Creative Media'
        elif 'Bachelor of Sport and Exercise Science' in degree_name:
            degree_name = 'Bachelor of Sport and Exercise Science'
        elif 'Bachelor of Nursing' in degree_name:
            degree_name = 'Bachelor of Nursing'
        elif 'Bachelor of Criminology' in degree_name:
            degree_name = 'Bachelor of Criminology'
        elif 'Bachelor of Communication' in degree_name:
            degree_name = 'Bachelor of Communication'
        elif 'Bachelor of Global Security' in degree_name:
            degree_name = 'Bachelor of Global Security'
        else:degree_name = degree_name
        # print(degree_name)

        #4.programme_en
        programme_en = response.xpath('//*[@id="course-overview"]/div/div/div/div/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en).strip()
        # print(programme_en)

        #5.degree_overview_en
        degree_overview_en = response.xpath('//*[@id="course-description-and-structure"]/div/div/div/div/p').extract()
        degree_overview_en = ''.join(degree_overview_en)
        degree_overview_en = remove_class(degree_overview_en)
        # print(degree_overview_en)

        #6.location
        location = response.xpath('//*[@id="course-description-and-structure"]/div/div/div/div/ul/li[1]/ul/li/strong').extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #7.duration
        duration = response.xpath("//*[contains(text(),'Course Duration')]//following-sibling::*").extract()[0]
        duration = ''.join(duration)
        duration = remove_tags(duration).strip()
        try:
            duration = re.findall(r'\d',duration)[0]
        except:
            duration = ''
        # print(duration)

        #8.department
        department = response.xpath("//*[contains(text(),'School')]//following-sibling::*//strong").extract()
        department = ''.join(department)
        department = remove_tags(department).strip()
        if 'School of LawBusiness' in department:
            department = 'School of LawBusiness'
        elif 'School of Veterinary and Life Sciences' in department:
            department = 'School of Veterinary and Life Sciences'
        # print(department)

        #9.degree_type
        degree_type = 1

        #10.start_date
        start_date = '2,7'

        #11.modules_en
        cour = response.xpath("//input[@name='course']//@value").extract()
        cour = ''.join(cour)
        cour = remove_tags(cour)
        # print(cour)
        modules_en_url ='https://handbook.murdoch.edu.au/courses/details/?us='+str(cour)+'&year=2019&structure=true'
        # print(modules_en_url)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        data = requests.get(modules_en_url, headers=headers)
        response_modules_en = etree.HTML(data.text)
        # print(modules_en_url)
        modules_en = response_modules_en.xpath('/html/body/div')
        # modules_en = ''.join(modules_en)
        doc = ""
        if len(modules_en) > 0:
            for a in modules_en:
                doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                doc = remove_class(doc)
                modules_en = doc
        # print(modules_en)

        #12.rntry_requirements_en
        # rntry_url = 'https://webapps2.murdoch.edu.au/entry-requirements/?study_level=undergrad&course='+str(cour)+'&htmlOnly=1&student_origin=international&country=China'
        # data = requests.get(rntry_url, headers=headers)
        # response_rntry = etree.HTML(data.text)
        # # print(rntry_url)
        # response_rntry = response_rntry.xpath('/html/body/div//text()')
        # response_rntry = ''.join(response_rntry)
        # response_rntry = '<p>'+response_rntry+'</p>'
        # # print(response_rntry)
        # rntry_requirements_en = response_rntry

        #13.tuition_fee
        tuition_fee = '1190/学分'

        #14.apply_pre
        apply_pre = '$'

        #15.tuition_fee_pre
        tuition_fee_pre = '$'

        #16.ielts 17181920 #21.toefl 22232425
        if 'Bachelor of Law' in degree_name:
            ielts = 6.5
            ielts_r =  6.5
            ielts_w =  6.5
            ielts_s =  6.5
            ielts_l =  6.5
            toefl =79
            toefl_r = 21
            toefl_w = 21
            toefl_s = 21
            toefl_l = 21
        elif 'Bachelor of Nursing' in degree_name:
            ielts =6.5
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_s = 6.5
            ielts_l = 6.5
            toefl = 79
            toefl_r = 21
            toefl_w = 21
            toefl_s = 21
            toefl_l = 21
        elif 'Bachelor of Veterinary Science' in degree_name:
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_s = 7.0
            ielts_l = 7.0
            toefl = 94
            toefl_r =27
            toefl_w = 27
            toefl_s = 27
            toefl_l = 27
        elif 'Bachelor of Education' in degree_name:
            ielts = 7.0
            ielts_r = 7.0
            ielts_w = 7.0
            ielts_s = 7.0
            ielts_l = 7.0
            toefl = 94
            toefl_r = 27
            toefl_w = 27
            toefl_s = 27
            toefl_l = 27
        else:
            ielts = 6.0
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
            toefl = 73
            toefl_r = 18
            toefl_w = 18
            toefl_s = 18
            toefl_l = 18

        #26.apply_documents_en
        apply_documents_en = '<p>Ready to apply? Before you start, make sure you have all of the following documentation ready for a quick application.Completed official Academic Transcripts and Certificates of Completion – both original and English translated versions A certified copy of your veterinary degree A certified copy of current registration with your local Veterinary Surgeon?s Board A recent Curriculum Vitae Two referee reports – one academic and one personal A typed, signed 500-word personal statement outlining how your veterinary work experience relates to this course English Language Proficiency Document (if available)</p>'

        #27.apply_desc_en
        apply_desc_en = "<p>Your Application Checklist Check the course details Check the entry requirements for the course to clarify your eligibility Check your eligibility for a scholarship Prepare your documentation (see the checklist below) Ask us any questions you might have (we're here to help!) Now you're ready to apply!</p>"

        item['university'] = university
        item['url'] = url
        item['degree_name'] = degree_name
        item['programme_en'] = programme_en
        item['degree_overview_en'] = degree_overview_en
        item['location'] = location
        item['duration'] = duration
        # item['department'] = department
        item['degree_type'] = degree_type
        item['start_date'] = start_date
        item['modules_en'] = modules_en
        # item['rntry_requirements_en'] = rntry_requirements_en
        item['tuition_fee'] = tuition_fee
        item['apply_pre'] = apply_pre
        item['tuition_fee_pre'] = tuition_fee_pre
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['apply_documents_en'] = apply_documents_en
        item['apply_desc_en'] = apply_desc_en
        yield item