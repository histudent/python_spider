# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/28 13:13'
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
    name = 'CurtinUniversity_p'
    allowed_domains = ['anu.edu.au/']
    start_urls = []
    C = [
        'https://study.curtin.edu.au/offering/course-pg-master-of-business-administration--mc-busadmv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-creative-practice-major-marts--mjrp-creatv2/',
        'https://study.curtin.edu.au/offering/course-pg-professional-writing-and-publishing-major-marts--mjrp-prowrv2/',
        'https://study.curtin.edu.au/offering/course-pg-media-practice-major-marts--mjrp-meprav2/',
        'https://study.curtin.edu.au/offering/course-pg-social-and-cultural-inquiry-major-marts--mjrp-soculv3/',
        'https://study.curtin.edu.au/offering/course-pg-visualisation-and-interactive-media-major-marts--mjrp-vistev3/',
        'https://study.curtin.edu.au/offering/course-pg-master-of-business-administration--mc-busadmv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-business-administration--mc-busadmv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-science-global-subsea-engineering--mc-gssengv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-international-business--mc-intbusv2/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-science-actuarial-and-financial-science--mc-actfnsv1/',
        'https://study.curtin.edu.au/offering/course-pg-computer-science-major-msc-science--mjrp-cmscmv1/',
        'https://study.curtin.edu.au/offering/course-pg-dryland-agricultural-systems-major-msc-science--mjrp-dragmv1/',
        'https://study.curtin.edu.au/offering/course-pg-master-of-clinical-physiotherapy--mc-phythv2/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-urban-and-regional-planning--mc-urplanv2/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-marketing--mc-mktgv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-business-administration-global--mc-mbaglov2/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-engineering-science-petroleum-engineering--mc-engpetv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-science-food-science-and-technology--mc-foodstv2/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-subsea-engineering--mc-sbsengv3/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-science-geospatial-science--mc-geospav1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-science-geology--mc-glgyv1/',
        'https://study.curtin.edu.au/offering/course-pg-geophysics-major-msc-science--mjrp-geopmv1/',
        'https://study.curtin.edu.au/offering/course-pg-master-of-applied-design-and-art--mc-desartv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-science-geology--mc-glgyv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-public-health--mc-pubhlv2/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-taxation--mc-taxatnv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-science-project-management--mc-projmv3/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-science-geospatial-science--mc-geospav1/',
        'https://study.curtin.edu.au/offering/course-pg-master-of-sustainability-and-climate-policy--mc-sustanv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-petroleum-engineering--mc-petengv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-industrial-engineering-major-msc-science--mjrp-iengmv1/',
        'https://study.curtin.edu.au/offering/course-pg-master-of-pharmacy--mg-pharmv2/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-finance--mc-fincev2/?int',
        'https://study.curtin.edu.au/offering/course-pg-mathematical-sciences-major-msc-science--mjrp-mathmv1/',
        'https://study.curtin.edu.au/offering/course-pg-master-of-arts-tesol--mc-aplingv5/?int',
        'https://study.curtin.edu.au/offering/course-pg-sustainability-management-major-msc-science--mjrp-sstmgv1/',
        'https://study.curtin.edu.au/offering/course-pg-master-of-business-administration-advanced--mc-mbaadvv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-sustainable-aquaculture-major-msc-science--mjrp-suagmv2/',
        'https://study.curtin.edu.au/offering/course-pg-master-of-biomedical-science--mc-biomedv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-water-quality-and-supply-systems-major-msc-science--mjrp-wqualv1/',
        'https://study.curtin.edu.au/offering/course-pg-master-of-sustainability-and-the-built-environment--mc-sustbev1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-engineering-science-mining--mc-miningv3/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-dietetics--mg-dietsv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-professional-engineering--mx-proengv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-sexology--mc-sxlgyv2/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-information-systems-and-technology--mc-isysv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-occupational-therapy--mg-occtv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-physiotherapy--mg-phythv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-science-actuarial-and-financial-science--mc-actfnsv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-science-health-practice--mc-hthprcv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-arts--mc-medcomv2/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-international-relations-and-national-security--mc-intrnsv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-human-resources--mc-humresv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-education--mc-educv2/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-business-administration--mc-busadmv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-molecular-medicine--mc-molmedv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-engineering-science-metallurgy--mc-metalgv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-predictive-analytics--mc-predanv2/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-accounting-cpa-australia-extension-studies--mc-advaccv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-supply-chain-management--mc-scmgmtv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-science-mineral-and-energy-economics--mc-mergecv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-internet-communications--mc-netscmv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-international-business-and-entrepreneurship--mc-mibev2/?int',
        'https://study.curtin.edu.au/offering/course-pg-professional-accounting-major-mcom--mjrp-prfacv1/',
        'https://study.curtin.edu.au/offering/course-pg-advanced-accounting-cpa-australia-extension-major-mcom--mjxp-aacpav1/',
        'https://study.curtin.edu.au/offering/course-pg-applied-finance-major-mcom--mjrp-apfncv1/',
        'https://study.curtin.edu.au/offering/course-pg-master-of-architecture--mc-archv2/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-engineering-science-electrical-engineering--mc-eleengv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-health-administration--mc-hladmnv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-nursing-practice--mg-nursprv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-human-rights--mc-hrightv1/?int',
        'https://study.curtin.edu.au/offering/course-pg-master-of-science-advanced-nursing-practice--mc-scclinv2/?int',
        'https://study.curtin.edu.au/offering/course-pg-marketing-major-mcom--mjrp-mrktgv1/',
        'https://study.curtin.edu.au/offering/course-pg-information-systems-and-technology-major-mcom--mjrp-isystv1/',
        'https://study.curtin.edu.au/offering/course-pg-supply-chain-management-major-mcom--mjrp-sucmmv1/'

    ]
    # C= set(C)
    # print(len(C))
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
        # major = response.xpath("//*[contains(text(),'Major areas of study:')]/../following-sibling::ul//li//a/@href").extract()
        major2 = response.xpath("//*[contains(text(),'Major areas of study:')]//following-sibling::ul//li//a/@href").extract()
        programme_en = degree_name.replace('Master of ','').strip()
        if ' Major (MSc Science)'in programme_en :
            programme_en = programme_en.replace(' Major (MSc Science)','')
        elif ' (MCom)'  in programme_en:
            programme_en = programme_en.replace(' (MCom)','')
        elif ' (Professional)'in programme_en:
            programme_en = programme_en.replace(' (Professional)','')
        elif ' (Global)'in programme_en:
            programme_en = programme_en
        else:
            if '(' in programme_en:
                programme_en = re.findall(r'\((.*)\)',programme_en)[0]
            else:pass

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

        if len(major2)!=0:
            for i in major2:
                url_major = 'https://study.curtin.edu.au'+str(i)
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
                if ' Major (MSc Science)' in response_programme_en:
                    response_programme_en = response_programme_en.replace(' Major (MSc Science)', '')
                elif ' (MCom)' in response_programme_en:
                    response_programme_en = response_programme_en.replace(' (MCom)', '')
                elif ' (Professional)' in programme_en:
                    response_programme_en = response_programme_en.replace(' (Professional)', '')
                elif ' (Global)' in programme_en:
                    response_programme_en = response_programme_en
                else:
                    if '(' in response_programme_en:
                        response_programme_en = re.findall(r'\((.*)\)', response_programme_en)[0]
                    else:
                        pass
                item['programme_en'] = response_programme_en
                item['overview_en'] = response_overview
                item['url'] = url_major
                yield item
        else:
            item['overview_en'] = ''
            item['url'] = url
            item['programme_en'] = programme_en
            yield item