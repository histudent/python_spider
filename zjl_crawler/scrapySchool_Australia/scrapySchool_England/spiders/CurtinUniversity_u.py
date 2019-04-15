# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/28 16:15'
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
class CurtinUniversitySpider(scrapy.Spider):
    name = 'CurtinUniversity_u'
    allowed_domains = ['anu.edu.au/']
    start_urls = []
    C= ['https://study.curtin.edu.au/offering/course-ug-bachelor-of-science-health-sciences--b-hlthscv1/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-applied-science-construction-management--b-conmv1/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-science-oral-health-therapy--b-oralhtv2/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-science-health-promotion--b-hlpromv1/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-science-medical-radiation-science--b-scimrsv1/?int',
'https://study.curtin.edu.au/offering/course-ug-accounting-major-bcom--mjru-acctgv1/',
'https://study.curtin.edu.au/offering/course-ug-accounting-technologies-major-bcom--mjru-actecv1/',
'https://study.curtin.edu.au/offering/course-ug-advertising-major-bcom--mjru-advrtv1/',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-science-speech-pathology--b-speechv1/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-science-laboratory-medicine--b-labmedv1/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-science-human-biology-preclinical--b-humbpcv3/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-laws--b-lawsv1/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-pharmacy-honours--bh-pharmv1/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-science-health-safety-and-environment--b-hlsfenvv1/?int',
'https://study.curtin.edu.au/offering/course-ug-agricultural-science-major-badvsci-honours--mjrh-adagsv1/',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-psychology--b-psychv1/?int',
'https://study.curtin.edu.au/offering/course-ug-banking-major-bcom--mjru-bankgv1/',
'https://study.curtin.edu.au/offering/course-ug-chemistry-major-badvsci-honours--mjrh-adchev1/',
'https://study.curtin.edu.au/offering/course-ug-business-information-systems-professional-major-bcom--mjru-buispv1/',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-technology-computer-systems-and-networking--b-csysntv2/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-applied-science-architectural-science--b-archv2/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-science-applied-geology--b-geolv1/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-surveying--b-survv1/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-business-administration--b-busadmv1/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-education-primary-education--b-edprv1/?int',
'https://study.curtin.edu.au/offering/course-ug-business-information-technology-professional-major-bcom--mjru-buitpv1/',
'https://study.curtin.edu.au/offering/course-ug-civil-and-construction-engineering-major-beng-hons--mjrh-ccoenv1/',
'https://study.curtin.edu.au/offering/course-ug-computing-major-badvsci-honours--mjrh-adcmpv1/',
'https://study.curtin.edu.au/offering/course-ug-business-law-major-bcom--mjru-bslawv1/',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-arts-urban-and-regional-planning--b-urplanv1/?int',
'https://study.curtin.edu.au/offering/course-ug-electrical-and-electronic-engineering-major-beng-hons--mjrh-elelev1/',
'https://study.curtin.edu.au/offering/course-ug-data-science-major-badvsci-honours--mjrh-addscv1/',
'https://study.curtin.edu.au/offering/course-ug-economics-major-bcom--mjru-econsv1/',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-agribusiness--b-agribv1/?int',
'https://study.curtin.edu.au/offering/course-ug-entrepreneurship-major-bcom--mjru-entrpv1/',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-applied-science-interior-architecture--b-intarchv3/?int',
'https://study.curtin.edu.au/offering/course-ug-financial-mathematics-major-badvsci-honours--mjrh-adfmav1/',
'https://study.curtin.edu.au/offering/course-ug-event-management-major-bcom--mjru-evntmv1/',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-science-physiotherapy--b-phythv1/?int',
'https://study.curtin.edu.au/offering/course-ug-geographic-information-science-major-badvsci-honours--mjrh-adgisv1/',
'https://study.curtin.edu.au/offering/course-ug-finance-major-bcom--mjru-fincev1/',
'https://study.curtin.edu.au/offering/course-ug-industrial-and-applied-mathematics-major-badvsci-honours--mjrh-adiamv1/',
'https://study.curtin.edu.au/offering/course-ug-human-resource-management-major-bcom--mjru-hrmgmv1/',
'https://study.curtin.edu.au/offering/course-ug-molecular-genetics-major-badvscihonours--mjrh-adgenv1/',
'https://study.curtin.edu.au/offering/course-ug-industrial-relations-major-bcom--mjru-indrev1/',
'https://study.curtin.edu.au/offering/course-ug-physics-major-badvsci-honours--mjrh-adphyv1/',
'https://study.curtin.edu.au/offering/course-ug-international-business-major-bcom--mjru-intbuv1/',
'https://study.curtin.edu.au/offering/course-ug-logistics-and-supply-chain-management-major-bcom--mjru-lgscmv1/',
'https://study.curtin.edu.au/offering/course-ug-management-major-bcom--mjru-mngmtv1/',
'https://study.curtin.edu.au/offering/course-ug-marketing-major-bcom--mjru-mrktgv1/',
'https://study.curtin.edu.au/offering/course-ug-property-development-and-valuation-major-bcom--mjru-propvv1/',
'https://study.curtin.edu.au/offering/course-ug-public-relations-major-bcom--mjru-pubrlv1/',
'https://study.curtin.edu.au/offering/course-ug-tourism-and-hospitality-major-bcom--mjru-trhosv1/',
'https://study.curtin.edu.au/offering/course-ug-animation-and-game-design-major--mjru-anigdv2/',
'https://study.curtin.edu.au/offering/course-ug-anthropology-and-sociology-major-ba--mjru-antsov2/',
'https://study.curtin.edu.au/offering/course-ug-chinese-major-ba--mjru-chnsev1/',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-science-nutrition-and-food-science--b-nutrv2/?int',
'https://study.curtin.edu.au/offering/course-ug-creative-advertising-and-graphic-design-major-ba--mjru-cragdv1/',
'https://study.curtin.edu.au/offering/course-ug-creative-writing-major-ba--mjru-crwriv1/',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-science-molecular-genetics-and-biotechnology--b-molgenv1/?int',
'https://study.curtin.edu.au/offering/course-ug-digital-design-major-ba--mjru-digdev2/',
'https://study.curtin.edu.au/offering/course-ug-fashion-major-ba--mjru-fashnv1/',
'https://study.curtin.edu.au/offering/course-ug-fine-art-major-ba--mjru-fnartv1/',
'https://study.curtin.edu.au/offering/course-ug-geography-major-ba--mjru-geogrv1/',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-science-occupational-therapy-honours--bh-occtv1/?int',
'https://study.curtin.edu.au/offering/course-ug-international-relations-major-ba--mjru-intrlv1/',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-science-exercise-sports-and-rehabilitation-science--b-exsprhbv2/?int',
'https://study.curtin.edu.au/offering/course-ug-internet-communications-major-ba--mjru-netcmv1/',
'https://study.curtin.edu.au/offering/course-ug-japanese-major-ba--mjru-japanv1/',
'https://study.curtin.edu.au/offering/course-ug-journalism-major-ba--mjru-journv2/',
'https://study.curtin.edu.au/offering/course-ug-librarianship-major-ba--mjru-libshv1/',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-arts-mass-communication--b-mascomsv1/?int',
'https://study.curtin.edu.au/offering/course-ug-literary-and-cultural-studies-major-ba--mjru-litcuv2/',
'https://study.curtin.edu.au/offering/course-ug-english-education-major-bed-secondary-education--mjru-engltv1/',
'https://study.curtin.edu.au/offering/course-ug-photography-and-illustration-design-major-ba--mjru-phillv1/',
'https://study.curtin.edu.au/offering/course-ug-professional-writing-and-publishing-major-ba--mjru-prwrpv1/',
'https://study.curtin.edu.au/offering/course-ug-mathematics-education-major-bed-secondary-education--mjru-mathtv1/',
'https://study.curtin.edu.au/offering/course-ug-screen-arts-major-ba--mjru-scartv1/',
'https://study.curtin.edu.au/offering/course-ug-science-education-major-bed-secondary-education--mjru-scietv1/',
'https://study.curtin.edu.au/offering/course-ug-theatre-arts-major-ba--mjru-perfsv2/',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-educational-studies--b-educv1/?int',
'https://study.curtin.edu.au/offering/course-ug-the-arts-education-major-bed-secondary-education--mjru-artstv1/',
'https://study.curtin.edu.au/offering/course-ug-visualisation-and-interactive-media-major-ba--mjru-vistcv2/',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-science-psychology-and-human-resource-management--b-psychrmv1/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-science-nursing--b-nursv2/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-social-work--b-scwkv1/?int',
'https://study.curtin.edu.au/offering/course-ug-bachelor-of-education-early-childhood-education--b-edecv1/?int']

    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Curtin University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.location
        location = 'Perth'

        #4.department
        department = response.xpath('//*[@id="page-content"]/div/section[1]/div/div/p[3]').extract()
        department = ''.join(department)
        department = remove_tags(department)
        department = clear_space_str(department).replace('TAUGHT BY: ','').strip()
        # print(department)

        #5.degree_name
        degree_name = response.xpath('//*[@id="page-content"]/div/section[1]/div/div/h1').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name).strip()
        # print(degree_name)



        #7.degree_overview_en
        degree_overview_en = response.xpath("//*[contains(text(),'About offering')]//following-sibling::div[1]").extract()
        degree_overview_en = ''.join(degree_overview_en)
        degree_overview_en = remove_class(degree_overview_en)
        # print(degree_overview_en)

        #9.degree_type
        degree_type = 1

        #10.duration
        duration = response.xpath('//*[@id="page-content"]/div/section[1]/div/div[3]/div[1]/p').extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        # print(duration)

        #11.ielts_w
        ielts_w = response.xpath("//*[contains(text(),'Writing')]//following-sibling::td").extract()
        ielts_w = ''.join(ielts_w)
        ielts_w = remove_tags(ielts_w)
        # print(ielts_w)

        #12.ielts_s
        ielts_s = response.xpath("//*[contains(text(),'Speaking')]//following-sibling::td").extract()
        ielts_s = ''.join(ielts_s)
        ielts_s = remove_tags(ielts_s)
        # print(ielts_s)

        #13.ielts_l
        ielts_l = response.xpath("//*[contains(text(),'Listening')]//following-sibling::td").extract()
        ielts_l = ''.join(ielts_l)
        ielts_l = remove_tags(ielts_l)
        # print(ielts_l)

        #14.ielts_r
        ielts_r = response.xpath("//*[contains(text(),'Reading')]//following-sibling::td").extract()
        ielts_r = ''.join(ielts_r)
        ielts_r = remove_tags(ielts_r)
        # print(ielts_r)

        #15.ielts
        ielts = response.xpath("//*[contains(text(),'Overall')]//following-sibling::td").extract()
        ielts = ''.join(ielts)
        ielts = remove_tags(ielts)
        # print(ielts)

        #16.rntry_requirements_en
        rntry_requirements_en =response.xpath("//*[contains(text(),'Admission criteria')]//following-sibling::*").extract()
        rntry_requirements_en = ''.join(rntry_requirements_en)
        rntry_requirements_en =remove_class(rntry_requirements_en)
        # print(rntry_requirements_en)

        #17.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'International student indicative fees for 2018')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #18.tuition_fee_pre
        tuition_fee_pre = '$'

        #19.apply_proces_en
        apply_proces_en = response.xpath('//*[@id="page-content"]/div/section[1]/div/div[2]/p[2]').extract()
        apply_proces_en = ''.join(apply_proces_en)
        apply_proces_en = remove_tags(apply_proces_en)
        apply_proces_en = 'https://apply.curtin.edu.au/before-you-start?spkCode='+str(apply_proces_en)
        # print(apply_proces_en)

        #20.modules_en
        try:
            modules_en_url = response.xpath("//a[@data-sticky-function='handbook']/@href").extract()[0]
        except:
            modules_en_url = ''
        if len(modules_en_url) != 0:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

            data = requests.get(modules_en_url, headers=headers)
            response_modules_en = etree.HTML(data.text)
            # print(response_modules_en)
            modules_en = response_modules_en.xpath('//table')[-1]
            doc = ""
            if len(modules_en) > 0:
                for a in modules_en:
                    doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                    doc = remove_class(doc)
                    modules_en = doc
        else:
            modules_en = None
        # print(modules_en)

        #21.career_en
        career_en = response.xpath("//*[contains(text(),'Career information')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #22.apply_desc_en
        apply_desc_en = "<p>Before you start The Curtin online application form is designed to be used by students and Curtin Registered Education agents alike. Applicants are encouraged to apply to Curtin directly using the online application form. However, applicants from Nigeria, Pakistan and India's Haryana and Punjab regions MUST apply through a Curtin Registered Education Agent.The online application form may only be used for Undergraduate and Postgraduate by Coursework study. You may apply here for Higher Degree by Research study.To apply for our Undergraduate or Postgraduate (by coursework) courses, you must provide a variety of relevant information including:Certified copies of academic transcripts for previously attained qualifications that are relevant to the Curtin course for which you are applying.English test results.Supporting information for your application, including supplementary forms for certain courses. Please note that if the required 'supplementary forms' are not completed and attached to this application, we will not proceed with the assessment of your applications.As part of the Simplified Streamlined Visa Framework (SSVF), you may be required to provide additional information in order for us to perform Genuine Temporary Entrant (GTE) assessments as part of your application.To find out more information about SSVF, GTE or student visas, please refer to the following links: https://www.border.gov.au/Busi/Educ/simplified-student-visa https://www.border.gov.au/Trav/Visa-1/500-https://www.border.gov.au/Trav/Stud/More/Genuine-Temporary-EntrantIt may take you some time to collate this material. By creating an online application account you can come back at any time to update, change, view and then submit your application. Your application will remain active for 45 days.You will be logged out of the application if you are inactive for more than 30 minutes, so please ensure you save your application regularly.Not ready to apply? Submit an enquiry here Can't apply online? Download an application form here, or click here to contact us for further assistance Browser requirements: Internet Explorer v7, Firefox v3.6.15, Safari v5.0.4, Chrome 10.0.648.151 or above<p>"

        #23.apply_pre
        apply_pre = '$'

        # 6.programme_en #8.overview_en
        major = response.xpath('//*[contains(text(),"major")]//following-sibling::ul//li//a/@href').extract()
        programme_en = degree_name.replace('Bachelor of ','')
        if ' (Honours)' in programme_en:
            programme_en = programme_en.replace(' (Honours)','')
        if '(' in programme_en:
            programme_en = re.findall('\((.*)\)',programme_en)[0]
        else:programme_en = programme_en
        # print(programme_en)
        # print(major)

        item['university'] = university
        # item['location'] = location
        # item['department'] = department
        # item['degree_name'] = degree_name
        # item['degree_overview_en'] = degree_overview_en
        # item['degree_type'] = degree_type
        # item['duration'] = duration
        # item['ielts_w'] = ielts_w
        # item['ielts_s'] = ielts_s
        # item['ielts_l'] = ielts_l
        # item['ielts_r'] = ielts_r
        # item['ielts'] = ielts
        # item['rntry_requirements_en'] = rntry_requirements_en
        # item['tuition_fee'] = tuition_fee
        # item['tuition_fee_pre'] = tuition_fee_pre
        # item['apply_proces_en'] = apply_proces_en
        item['modules_en'] = modules_en
        # item['career_en'] = career_en
        # item['apply_desc_en'] = apply_desc_en
        # item['apply_pre'] = apply_pre
        #
        if len(major)!=0:
            for i in major:
                url_major = i
                if 'https://study.curtin.edu.au' in i:
                    url_major = i.replace('https://study.curtin.edu.au','')
                else:pass
                url_major = 'https://study.curtin.edu.au'+str(url_major)
                # print(url_major)
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
                data = requests.get(url_major, headers=headers)
                response_major = etree.HTML(data.text)
                response_overview = response_major.xpath("//*[contains(text(),'About offering')]//following-sibling::div[1]//p//text()")
                response_overview = ''.join(response_overview)
                response_overview = '<p>'+response_overview+'</p>'
                response_programme_en = response_major.xpath('//*[@id="page-content"]/div/section[1]/div/div/h1//text()')
                response_programme_en = ''.join(response_programme_en)
                response_programme_en = remove_class(response_programme_en)
                # print(response_programme_en)
                if ' (Honours)' in response_programme_en:
                    response_programme_en = response_programme_en.replace(' (Honours)','')
                if '(Professional)' in response_programme_en:
                    response_programme_en = response_programme_en.replace(' Major (BCom)','')
                elif '(' in response_programme_en:
                    a = re.findall('\(.*\)',response_programme_en)[0]
                    response_programme_en = response_programme_en.replace(a,'').strip()
                item['overview_en'] = response_overview
                item['url'] = url_major
                item['programme_en'] = response_programme_en
                yield item
        else:
            item['overview_en'] = 'N/A'
            item['url'] = url
            item['programme_en'] = programme_en
            yield item