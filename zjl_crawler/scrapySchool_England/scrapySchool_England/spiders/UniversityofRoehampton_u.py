# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/6 13:56'
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
from scrapySchool_England.clearSpace import  clear_space_str
from scrapySchool_England.translate_date import  tracslateDate
from scrapySchool_England.translate_date import tracslateDate
class UniversityofRoehamptonSpider(scrapy.Spider):
    name = 'UniversityofRoehampton_u'
    allowed_domains = ['roehampton.ac.uk/']
    start_urls = []
    C = [
        'https://www.roehampton.ac.uk/undergraduate-courses/primary-education-qts/',
        'https://www.roehampton.ac.uk/undergraduate-courses/primary-education-qts/',
        'https://www.roehampton.ac.uk/undergraduate-courses/business-management/',
        'https://www.roehampton.ac.uk/undergraduate-courses/business-management-and-entrepreneurship/',
        'https://www.roehampton.ac.uk/undergraduate-courses/accounting/',
        'https://www.roehampton.ac.uk/undergraduate-courses/diverse-dance-styles/',
        'https://www.roehampton.ac.uk/undergraduate-courses/business-management-and-economics/',
        'https://www.roehampton.ac.uk/undergraduate-courses/international-business/',
        'https://www.roehampton.ac.uk/undergraduate-courses/human-resource-management/',
        'https://www.roehampton.ac.uk/undergraduate-courses/mass-communications/',
        'https://www.roehampton.ac.uk/undergraduate-courses/marketing/',
        'https://www.roehampton.ac.uk/undergraduate-courses/dance/',
        'https://www.roehampton.ac.uk/undergraduate-courses/mass-communications-extended-degree/',
        'https://www.roehampton.ac.uk/undergraduate-courses/marketing-extended-degree/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Roehampton'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="wrapper"]/div/figure/figcaption/div/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en).replace('Undergraduate','').replace('Extended Degree','').strip()
        # print(programme_en)

        #4.degree_type
        degree_type = 1

        #5.degree_name
        # degree_name = response.xpath("//*[contains(text(),'Degree type')]//following-sibling::*").extract()[0]
        # degree_name = ''.join(degree_name)
        # degree_name = remove_tags(degree_name)
        # if '/BSc' in degree_name:
        #     degree_name = 'BSc (single honours)'
        # degree_name = degree_name.strip()
        # degree_name = degree_name.replace('(single honours)','').strip()
        # print(degree_name,url)

        #6.overview_en
        overview_en = response.xpath("//*[contains(text(),'Summary')]//following-sibling::*[position()<6]").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #7.department
        department = response.xpath("//h3[contains(text(),'Department')]//following-sibling::*").extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #8.duration
        duration_list = response.xpath("//h3[contains(text(),'Duration')]//following-sibling::*").extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        duration = duration_list.replace('(full-time)','').strip().replace('(full time)','').strip()
        # print(duration)

        #9.ucascode
        ucascode = response.xpath("//h3[contains(text(),'UCAS Code')]//following-sibling::*").extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode)
        # print(ucascode)


        #11.start_date
        start_date = '2018-9'

        #12.tuition_fee
        tuition_fee = response.xpath("//h3[contains(text(),'Tuition Fees (per year)')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #13.tuition_fee_pre
        tuition_fee_pre = '£'

        #14.apply_desc_en
        apply_desc_en = "<p>The University uses the UCAS Tariff to compare applicants with different qualifications. This also allows us to consider applicants who themselves have taken a range of different qualifications. Many programmes have specific entry requirements, so it is advisable to check on our website before you apply. All offers are subject to the University's general entrance requirements. For undergraduate courses, these are as follows: passes in two distinct subjects at GCE Advanced Level;a pass in one subject at GCE Advanced Level plus (a) passes in two distinct subjects at GCE Advanced Subsidiary Level, or (b) a Vocational A-Level Single Award, or (c) two Vocational A-Level part Awards; a Vocational A-Level Double Award; or a Vocational A-Level Single Award plus (a) two Vocational A-Level part Awards, or (b) passes in two distinct subjects at GCE Advanced Subsidiary Level; or a BTEC National Certificate or Diploma; or a Scottish Certificate of Education with (a) passes in five subjects, including at least three at Higher grade, or (b) passes in four subjects all at Higher grade or New Higher grade; or the full Diploma of the International Baccalaureate; or an Irish Leaving Certificate with passes in four subjects at Grade C at the Higher level. For some courses we require applicants to achieve a GCSE Grade C or above in specific subjects, or an equivalent qualification. The information below lists the equivalent qualifications we can accept.If you require any further advice on our entry requirements, please contact the Enquiries Office at undergraduate@roehampton.ac.uk, or by calling 020 8392 3232.If you are applying from overseas and require specific advice about your qualifications, you can visit the country pages or contact our international team on international@roehampton.ac.uk or by calling 0208 392 3192. Acceptable English Qualifications (UK students) GCSE at Grade C or above Equivalent Access course modules at Level 2 or above Functional Skills Level 2 English with a pass grade (Not acceptable for BA Primary Education) Key Skills Level 2 English with a pass grade (Not acceptable for BA Primary Education) The University of Roehampton also recognises the test offered by the organisation Equivalency Testing, which sets and operates GCSE Equivalency Testing in English, Mathematics and Science. Please contact them on +44 (0)1277 203336 for further information or visit their website, www.equivalencytesting.com Submission of Your Results:You should send a copy of your results to: admissions@roehampton.ac.uk. BA Primary Education and PGCE students must submit their original certificates. If you are applying as an EU or International student you will find a list of acceptable English qualifications on our international webpages. Acceptable Mathematics Qualifications GCSE at Grade C or above Equivalent Access course modules at Level 2 or above Functional Skills Level 2 Maths with a pass grade (Not acceptable for BA Primary Education) Key Skills Level 2 Adult Numeracy or Application of Number (Not acceptable for BA Primary Education) The University of Roehampton also recognises the test offered by the organisation Equivalency Testing, which sets and operates GCSE Equivalency Testing in English, Mathematics and Science. Please contact them on +44 (0)1277 203336 for further information or visit their website, www.equivalencytesting.com.</p>"

        #15.ielts 16171819
        ielts = 6.0
        ielts_l = 5.5
        ielts_w = 5.5
        ielts_r = 5.5
        ielts_s = 5.5

        #20.toefl 21222324
        toefl = 80
        toefl_r = 18
        toefl_w = 17
        toefl_l = 17
        toefl_s = 20

        #25.modules_en
        modules_en = response.xpath('//*[@id="accordion"]/div[3]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #26.career_en
        career_en = response.xpath("//*[contains(text(),'Career options')]/../following-sibling::*").extract()
        if len(career_en)==0:
            career_en = response.xpath("//*[contains(text(),'Career options')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en).strip()

        # print(career_en)

        #27.apply_pre
        apply_pre = '£'

        #28.apply_proces_en
        apply_proces_en ='http://www.roehampton.ac.uk/globalassets/documents/international/country-specific/2018/china-2018.pdf'

        #29.alevel
        alevel = "<p>Undergraduate general entrance requirements UK students The University uses the UCAS Tariff to compare applicants with different qualifications. This also allows us to consider applicants who themselves have taken a range of different qualifications. Many programmes have specific entry requirements, so it is advisable to check on our website before you apply.All offers are subject to the University's general entrance requirements. For undergraduate courses, these are as follows:passes in two distinct subjects at GCE Advanced Level; a pass in one subject at GCE Advanced Level plus (a) passes in two distinct subjects at GCE Advanced Subsidiary Level, or (b) a Vocational A-Level Single Award, or (c) two Vocational A-Level part Awards; a Vocational A-Level Double Award; or a Vocational A-Level Single Award plus (a) two Vocational A-Level part Awards, or (b) passes in two distinct subjects at GCE Advanced Subsidiary Level; or a BTEC National Certificate or Diploma; or a Scottish Certificate of Education with (a) passes in five subjects, including at least three at Higher grade, or (b) passes in four subjects all at Higher grade or New Higher grade; or the full Diploma of the International Baccalaureate; oran Irish Leaving Certificate with passes in four subjects at Grade C at the Higher level.For some courses we require applicants to achieve a GCSE Grade C or above in specific subjects, or an equivalent qualification. The information below lists the equivalent qualifications we can accept.If you require any further advice on our entry requirements, please contact the Enquiries Office at undergraduate@roehampton.ac.uk, or by calling 020 8392 3232.If you are applying from overseas and require specific advice about your qualifications, you can visit the country pages or contact our international team on international@roehampton.ac.uk or by calling 0208 392 3192. Acceptable English Qualifications (UK students) GCSE at Grade C or above Equivalent Access course modules at Level 2 or above Functional Skills Level 2 English with a pass grade (Not acceptable for BA Primary Education)Key Skills Level 2 English with a pass grade (Not acceptable for BA Primary Education)The University of Roehampton also recognises the test offered by the organisation Equivalency Testing, which sets and operates GCSE Equivalency Testing in English, Mathematics and Science. Please contact them on +44 (0)1277 203336 for further information or visit their website, www.equivalencytesting.comSubmission of Your Results:You should send a copy of your results to: admissions@roehampton.ac.uk.BA Primary Education and PGCE students must submit their original certificates. If you are applying as an EU or International student you will find a list of acceptable English qualifications on our international webpages. Acceptable Mathematics Qualifications GCSE at Grade C or above Equivalent Access course modules at Level 2 or above Functional Skills Level 2 Maths with a pass grade (Not acceptable for BA Primary Education) Key Skills Level 2 Adult Numeracy or Application of Number (Not acceptable for BA Primary Education)The University of Roehampton also recognises the test offered by the organisation Equivalency Testing, which sets and operates GCSE Equivalency Testing in English, Mathematics and Science. Please contact them on +44 (0)1277 203336 for further information or visit their website, www.equivalencytesting.com.</p>"

        #30.ib
        ib= response.xpath("//*[contains(text(),'requirements')]/../following-sibling::*").extract()
        ib = ''.join(ib)
        ib = remove_tags(ib)
        # print(ib,url)

        item['ib'] = ib
        item['alevel'] = alevel
        item['ucascode'] = ucascode
        item['apply_desc_en'] = apply_desc_en
        item['apply_pre'] = apply_pre
        item['apply_proces_en'] = apply_proces_en
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        # item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['department'] = department
        item['duration'] = duration
        item['start_date'] = start_date
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['ielts'] = ielts
        item['ielts_l'] = ielts_l
        item['ielts_w'] = ielts_w
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['toefl'] = toefl
        item['toefl_l'] = toefl_l
        item['toefl_s'] = toefl_s
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        yield item