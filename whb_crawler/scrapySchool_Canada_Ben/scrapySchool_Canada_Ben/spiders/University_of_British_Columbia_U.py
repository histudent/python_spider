import scrapy
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from scrapySchool_Canada_Ben import getItem
from w3lib.html import remove_tags
import requests
import re
import time
from lxml import etree

class BaiduSpider(scrapy.Spider):
    name = 'University_of_British_Columbia_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['https://you.ubc.ca/ubc_programs/archaeology/',
'https://you.ubc.ca/ubc_programs/anthropology-vancouver/',
'https://you.ubc.ca/ubc_programs/applied-animal-biology/',
'https://you.ubc.ca/ubc_programs/anthropology-okanagan/',
'https://you.ubc.ca/ubc_programs/art-history-visual-culture/',
'https://you.ubc.ca/ubc_programs/art-history/',
'https://you.ubc.ca/ubc_programs/asian-area-studies/',
'https://you.ubc.ca/ubc_programs/atmospheric-science/',
'https://you.ubc.ca/ubc_programs/asian-language-culture/',
'https://you.ubc.ca/ubc_programs/astronomy/',
'https://you.ubc.ca/ubc_programs/behavioural-neuroscience/',
'https://you.ubc.ca/ubc_programs/biochemistry/',
'https://you.ubc.ca/ubc_programs/biochemistry-molecular-biology/',
'https://you.ubc.ca/ubc_programs/biology-okanagan/',
'https://you.ubc.ca/ubc_programs/biochemistry-molecular-biology/',
'https://you.ubc.ca/ubc_programs/biophysics/',
'https://you.ubc.ca/ubc_programs/biotechnology/',
'https://you.ubc.ca/ubc_programs/canadian-studies/',
'https://you.ubc.ca/ubc_programs/business-computer-science/',
'https://you.ubc.ca/ubc_programs/cellular-anatomical-physiological-sciences/',
'https://you.ubc.ca/ubc_programs/chemical-engineering/',
'https://you.ubc.ca/ubc_programs/chemistry-okanagan/',
'https://you.ubc.ca/ubc_programs/chemical-biological-engineering/',
'https://you.ubc.ca/ubc_programs/civil-engineering-okanagan/',
'https://you.ubc.ca/ubc_programs/civil-engineering-vancouver/',
'https://you.ubc.ca/ubc_programs/chemistry-vancouver/',
'https://you.ubc.ca/ubc_programs/classical-near-eastern-religious-studies/',
'https://you.ubc.ca/ubc_programs/human-kinetics-clinical-exercise/',
'https://you.ubc.ca/ubc_programs/cognitive-systems-ba/',
'https://you.ubc.ca/ubc_programs/computer-engineering/',
'https://you.ubc.ca/ubc_programs/cognitive-systems-bsc/',
'https://you.ubc.ca/ubc_programs/computer-science-vancouver-ba/',
'https://you.ubc.ca/ubc_programs/computer-science-okanagan-ba/',
'https://you.ubc.ca/ubc_programs/computer-science-okanagan-bsc/',
'https://you.ubc.ca/ubc_programs/creative-writing-okanagan/',
'https://you.ubc.ca/ubc_programs/computer-science-vancouver-bsc/',
'https://you.ubc.ca/ubc_programs/commerce/',
'https://you.ubc.ca/ubc_programs/creative-writing-vancouver/',
'https://you.ubc.ca/ubc_programs/dental-hygiene/',
'https://you.ubc.ca/ubc_programs/cultural-studies/',
'https://you.ubc.ca/ubc_programs/data-science/',
'https://you.ubc.ca/ubc_programs/dietetics/',
'https://you.ubc.ca/ubc_programs/earth-environmental-sciences/',
'https://you.ubc.ca/ubc_programs/earth-ocean-sciences/',
'https://you.ubc.ca/ubc_programs/ecology-evolutionary-biology/',
'https://you.ubc.ca/ubc_programs/economics-vancouver/',
'https://you.ubc.ca/ubc_programs/education-elementary/',
'https://you.ubc.ca/ubc_programs/economics-okanagan-ba/',
'https://you.ubc.ca/ubc_programs/economics-okanagan-bsc/',
'https://you.ubc.ca/ubc_programs/education-nitep/',
'https://you.ubc.ca/ubc_programs/education-ib/',
'https://you.ubc.ca/ubc_programs/middle-years-education/',
'https://you.ubc.ca/ubc_programs/education-secondary/',
'https://you.ubc.ca/ubc_programs/education-wktep/',
'https://you.ubc.ca/ubc_programs/education-teaching-adolescents/',
'https://you.ubc.ca/ubc_programs/education-teaching-children/',
'https://you.ubc.ca/ubc_programs/electrical-engineering-okanagan/',
'https://you.ubc.ca/ubc_programs/electrical-engineering-vancouver/',
'https://you.ubc.ca/ubc_programs/engineering-physics/',
'https://you.ubc.ca/ubc_programs/english-okanagan/',
'https://you.ubc.ca/ubc_programs/english-vancouver/',
'https://you.ubc.ca/ubc_programs/environmental-engineering/',
'https://you.ubc.ca/ubc_programs/environmental-design/',
'https://you.ubc.ca/ubc_programs/environmental-chemistry/',
'https://you.ubc.ca/ubc_programs/environmental-sciences/',
'https://you.ubc.ca/ubc_programs/film-production/',
'https://you.ubc.ca/ubc_programs/first-nations-endangered-languages/',
'https://you.ubc.ca/ubc_programs/film-studies/',
'https://you.ubc.ca/ubc_programs/first-nations-indigenous-studies/',
'https://you.ubc.ca/ubc_programs/food-nutritional-sciences/',
'https://you.ubc.ca/ubc_programs/food-science/',
'https://you.ubc.ca/ubc_programs/food-market-analysis/',
'https://you.ubc.ca/ubc_programs/food-nutrition-health/',
'https://you.ubc.ca/ubc_programs/forest-sciences/',
'https://you.ubc.ca/ubc_programs/french-okanagan/',
'https://you.ubc.ca/ubc_programs/forestry/',
'https://you.ubc.ca/ubc_programs/french-spanish/',
'https://you.ubc.ca/ubc_programs/french-vancouver/',
'https://you.ubc.ca/ubc_programs/gender-race-sexuality-social-justice/',
'https://you.ubc.ca/ubc_programs/freshwater-science/',
'https://you.ubc.ca/ubc_programs/gender-womens-studies/',
'https://you.ubc.ca/ubc_programs/general-science/',
'https://you.ubc.ca/ubc_programs/general-studies/',
'https://you.ubc.ca/ubc_programs/geographical-sciences/',
'https://you.ubc.ca/ubc_programs/geography/',
'https://you.ubc.ca/ubc_programs/geo-environment-sustainability/',
'https://you.ubc.ca/ubc_programs/geology/',
'https://you.ubc.ca/ubc_programs/human-geography/',
'https://you.ubc.ca/ubc_programs/geophysics/',
'https://you.ubc.ca/ubc_programs/geological-engineering/',
'https://you.ubc.ca/ubc_programs/global-resource-systems/',
'https://you.ubc.ca/ubc_programs/german/',
'https://you.ubc.ca/ubc_programs/indigenous-studies/',
'https://you.ubc.ca/ubc_programs/history-vancouver/',
'https://you.ubc.ca/ubc_programs/human-kinetics-health-promotion/',
'https://you.ubc.ca/ubc_programs/integrated-computer-science/',
'https://you.ubc.ca/ubc_programs/history-okanagan/',
'https://you.ubc.ca/ubc_programs/integrated-engineering/',
'https://you.ubc.ca/ubc_programs/integrated-sciences/',
'https://you.ubc.ca/ubc_programs/interdisciplinary-studies/',
'https://you.ubc.ca/ubc_programs/international-relations-okanagan/',
'https://you.ubc.ca/ubc_programs/international-economics/',
'https://you.ubc.ca/ubc_programs/kinesiology-interdisciplinary-studies/',
'https://you.ubc.ca/ubc_programs/international-relations-vancouver/',
'https://you.ubc.ca/ubc_programs/kinesiology-health-science/',
'https://you.ubc.ca/ubc_programs/latin-american-studies-vancouver/',
'https://you.ubc.ca/ubc_programs/kinesiology-leadership-education-physical-activity/',
'https://you.ubc.ca/ubc_programs/linguistics/',
'https://you.ubc.ca/ubc_programs/materials-engineering/',
'https://you.ubc.ca/ubc_programs/mathematical-sciences-okanagan/',
'https://you.ubc.ca/ubc_programs/mathematics-okanagan-ba/',
'https://you.ubc.ca/ubc_programs/management/',
'https://you.ubc.ca/ubc_programs/mathematical-sciences-vancouver/',
'https://you.ubc.ca/ubc_programs/mathematics-vancouver-ba/',
'https://you.ubc.ca/ubc_programs/mathematics-vancouver-bsc/',
'https://you.ubc.ca/ubc_programs/mathematics-economics/',
'https://you.ubc.ca/ubc_programs/mathematics-okanagan-bsc/',
'https://you.ubc.ca/ubc_programs/mechanical-engineering-okanagan/',
'https://you.ubc.ca/ubc_programs/media-studies-okanagan/',
'https://you.ubc.ca/ubc_programs/mechanical-engineering-vancouver/',
'https://you.ubc.ca/ubc_programs/medical-laboratory-science/',
'https://you.ubc.ca/ubc_programs/media-studies/',
'https://you.ubc.ca/ubc_programs/medieval-studies/',
'https://you.ubc.ca/ubc_programs/midwifery/',
'https://you.ubc.ca/ubc_programs/microbiology/',
'https://you.ubc.ca/ubc_programs/microbiology-immunology/',
'https://you.ubc.ca/ubc_programs/modern-european-studies/',
'https://you.ubc.ca/ubc_programs/museum-studies/',
'https://you.ubc.ca/ubc_programs/mining-engineering/',
'https://you.ubc.ca/ubc_programs/music/',
'https://you.ubc.ca/ubc_programs/music-advanced-performance/',
'https://you.ubc.ca/ubc_programs/music-composition/',
'https://you.ubc.ca/ubc_programs/music-general-studies/',
'https://you.ubc.ca/ubc_programs/music-scholarship/',
'https://you.ubc.ca/ubc_programs/nursing-okanagan/',
'https://you.ubc.ca/ubc_programs/nursing-vancouver/',
'https://you.ubc.ca/ubc_programs/natural-resources-conservation/',
'https://you.ubc.ca/ubc_programs/nutritional-sciences/',
'https://you.ubc.ca/ubc_programs/oceanography/',
'https://you.ubc.ca/ubc_programs/pharmacology/',
'https://you.ubc.ca/ubc_programs/philosophy-okanagan/',
'https://you.ubc.ca/ubc_programs/philosophy-vancouver/',
'https://you.ubc.ca/ubc_programs/philosophy-politics-okanagan/',
'https://you.ubc.ca/ubc_programs/physics-okanagan/',
'https://you.ubc.ca/ubc_programs/physics-vancouver/',
'https://you.ubc.ca/ubc_programs/political-science-okanagan/',
'https://you.ubc.ca/ubc_programs/political-science-vancouver/',
'https://you.ubc.ca/ubc_programs/psychology-vancouver-ba/',
'https://you.ubc.ca/ubc_programs/psychology-okanagan-ba/',
'https://you.ubc.ca/ubc_programs/religion-literature-the-arts/',
'https://you.ubc.ca/ubc_programs/psychology-okanagan-bsc/',
'https://you.ubc.ca/ubc_programs/romance-studies/',
'https://you.ubc.ca/ubc_programs/social-work/',
'https://you.ubc.ca/ubc_programs/spanish-hispanic-studies/',
'https://you.ubc.ca/ubc_programs/sociology-okanagan/',
'https://you.ubc.ca/ubc_programs/science-combined-major/',
'https://you.ubc.ca/ubc_programs/sociology-vancouver/',
'https://you.ubc.ca/ubc_programs/statistics-okanagan/',
'https://you.ubc.ca/ubc_programs/speech-sciences/',
'https://you.ubc.ca/ubc_programs/statistics-vancouver/',
'https://you.ubc.ca/ubc_programs/statistics-combined-majors/',
'https://you.ubc.ca/ubc_programs/sustainable-agriculture-environment/',
'https://you.ubc.ca/ubc_programs/theatre/',
'https://you.ubc.ca/ubc_programs/theatre-acting/',
'https://you.ubc.ca/ubc_programs/vantage-one-applied-science/',
'https://you.ubc.ca/ubc_programs/united-states-studies/',
'https://you.ubc.ca/ubc_programs/urban-forestry/',
'https://you.ubc.ca/ubc_programs/theatre-design-production/',
'https://you.ubc.ca/ubc_programs/vantage-one-arts/',
'https://you.ubc.ca/ubc_programs/vantage-one-science/',
'https://you.ubc.ca/ubc_programs/visual-art-ba/',
'https://you.ubc.ca/ubc_programs/visual-art-bfa/',
'https://you.ubc.ca/ubc_programs/visual-arts/',
'https://you.ubc.ca/ubc_programs/wood-products-processing/',
'https://you.ubc.ca/ubc_programs/zoology/',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)


    def parse(self, response):
        item = getItem.get_item(ScrapyschoolCanadaBenItem)



        try:
            major_name_en = response.xpath('//h1').extract()[0]
            #major_name_en = ''.join(major_name_en)
            #major_name_en = major_name_en.replace('\r\n','').replace('\n','').replace('           ','').replace('\t','').replace('     ','')
            major_name_en = remove_tags(major_name_en)
           # print(major_name_en)
        except:
            major_name_en = None
           # print(major_name_en)
#1.学校名称
        school_name = 'University of British Columbia'

#2.地点
        try:
            location =response.xpath('//*[@id="program-vitals"]/ul[1]/li[1]/strong').extract()[0]
            location = remove_tags(location)
           # print(location)
        except:
            location = None
            #print(location)

#3. 校区
        try:
            campus = location
            # campus = remove_tags(campus)
            # campus = campus.replace(', Online','')
            # campus = campus.replace(' ','')
            # campus = campus.split(',')
            #print(campus)
        except:
            campus = None
            #print(campus)

#4. 学院
        try:
            department = response.xpath('//*[@id="program-vitals"]/ul[1]/li[2]/strong').extract()[0]
            department = remove_tags(department)
            #print(len(department))
            #print(department)
            #print(response.url)
        except:
            department = None
            #print(department)

# 4.
        try:
            degree_name = response.xpath('//*[@id="program-vitals"]/ul[1]/li[3]/strong').extract()[0]
            degree_name = remove_tags(degree_name)
            #degree_name_list = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_name_list)
            #print(degree_name)
            #print(response.url)
        except:
            degree_name = None
            #print(degree_name)

#5.学位描述
        try:
            degree_overview_en = response.xpath('//*[@id="program-summary"]/div').extract()
            degree_overview_en = ''.join(degree_overview_en)
            #degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',degree_overview_en)
            #degree_overview_en = degree_overview_en.replace('\r\n','')
            #degree_overview_en = degree_overview_en.replace('\n','')
            #degree_overview_en = degree_overview_en.replace('\n','')
            #degree_overview_en = degree_overview_en.replace('  ',' ')
            #degree_overview_en = degree_overview_en.replace('					','')
            #degree_overview_en = degree_overview_en.replace('			  	','')
            #print(degree_overview_en)
        except:
            degree_overview_en = None
            #print(degree_overview_en)

#6.专业英文


#7.专业介绍
        try:
            #overview_en = degree_overview_en
            overview_en = degree_overview_en
            # print(overview_en)
        except:
            overview_en = degree_overview_en
            # print(overview_en)

#8.入学时间
        try:
            start_date = response.xpath('').extract()[0]
            start_date = remove_tags(start_date)
            # print(start_date)
        except:
            start_date = None
            # print(start_date)

#9.课程长度
        try:
            duration = response.xpath('//*[@id="program-vitals"]/ul[2]/li[1]/strong').extract()[0]
            if '4.5' in duration:
                duration = '4.5'
                duration_per = '1'
            elif '4' in duration:
                duration = '4'
                duration_per = '1'
            elif '2' in duration:
                duration = '2'
                duration_per = '1'
            elif '5' in duration:
                duration = '5'
                duration_per = '1'
            elif '3' in duration:
                duration = '3'
                duration_per = '1'
            elif '11' in duration:
                duration = '11'
                duration_per = '2'
            elif '16' in duration:
                duration = '16'
                duration_per = '2'
            else:
                duration = None
                duration_per = '1'
            #print(duration)
        except:
            duration = None
            duration_per = 1
           # print(duration)

#10.课程设置
        try:
            modules_en = response.xpath('//h3[contains(text(),"What you will learn")]/following-sibling::div').extract()[0]
            modules_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',modules_en)
            modules_en = modules_en.replace('\r\n','').replace('\n','').replace('\t','').replace('                                                                                                                         ','').replace('                                                                       ','')
            #print(modules_en)
        except:
            modules_en = None
            #print(modules_en)

#11.就业方向
        try:
            #career_en = response.xpath('//h2/span[contains(text(),"Your future")]/..//following-sibling::div').extract()[0]
            url = response.xpath('//*[@id="container"]/div/nav/div/ul/li[5]/a/@href').extract()[0]
            #print(url + "  ++++++")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
            response2 = etree.HTML(requests.get(url, headers=headers).text)
            response2 = response2.xpath('//div[@id="career-options"]')
            #print(response2)
            career_en = []
            # print(response2)
            for rea in response2:
                career_en += etree.tostring(rea, method='html', encoding='unicode')
                career_en = ''.join(career_en)
                print(career_en + "++++++++++++++++++++++++++")
            # print(modules_en,'------------')
            career_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]', '', career_en)
            print(career_en)
        except:
            career_en = None
            print(career_en)

#12.截止日期
        try:
            deadline = '2019-01-15'

        except:
            deadline = None
            #print(deadline)
#13.学费
        try:
            if 'Okanagan' in campus:
                if 'Bachelor of Applied Science' in degree_name:
                    tuition_fee = '48,196.15'
                elif 'Bachelor of Arts' in degree_name:
                    tuition_fee = '39,082.15'
                elif 'Bachelor of Education' in degree_name:
                    tuition_fee = '31,655.15'
                elif 'Bachelor of Fine Arts' in degree_name:
                    tuition_fee = '38,882.15'
                elif 'Bachelor of Human Kinetics' in degree_name:
                    tuition_fee = '40,425.37'
                elif 'Bachelor of Management' in degree_name:
                    tuition_fee = '40,389.99'
                elif 'Bachelor of Media Studies' in degree_name:
                    tuition_fee = '37,982.15'
                elif 'Bachelor of Science' in degree_name:
                    tuition_fee = '40,344.15'
                else:
                    tuition_fee = None
            elif 'Vancouver' in campus:
                if 'Bachelor of Applied Science' in degree_name:
                    tuition_fee = '50,820.79'
                elif 'Bachelor of Arts' in degree_name:
                    tuition_fee = '39,746.83'
                elif 'Bachelor of Education' in degree_name:
                    tuition_fee = '52,777.83'
                elif 'Bachelor of Fine Arts' in degree_name:
                    tuition_fee = '39,226.83'
                elif 'Bachelor of Human Kinetics' in degree_name:
                    tuition_fee = None
                elif 'Bachelor of Management' in degree_name:
                    tuition_fee = '40,150.83'
                elif 'Bachelor of Media Studies' in degree_name:
                    tuition_fee = '39,746.83'
                elif 'Bachelor of Environmental Design' in degree_name:
                    tuition_fee = '49,663.83'
                elif 'Science' in degree_name:
                    tuition_fee = '55,959.22'
                elif 'Bachelor of Midwifery' in degree_name:
                    tuition_fee = '48,836.83'
                elif 'Bachelor of Urban Forestry' in degree_name:
                    tuition_fee = '40,200.83'
                elif 'Bachelor of Social Work' in degree_name:
                    tuition_fee = '38,503.83'
                elif 'Bachelor of International Economics' in degree_name:
                    tuition_fee = '48,878.31'
                elif 'Bachelor of Kinesiology' in degree_name:
                    tuition_fee = '40,930.83'
                elif 'Bachelor of Music' in degree_name:
                    tuition_fee = '37,250.83'
                else:
                    tuition_fee = None
            else:
                tuition_fee = None
        except:
            tuition_fee = None
        #print(tuition_fee)
        tuition_fee_per = '5'
#14 申请费:
        apply_fee = '90'

#15 申请要求
        try:
            entry_requirements_en = response.xpath('//*[@id="requirement_countries"]').extract()
            entry_requirements_en = ''.join(entry_requirements_en)
            entry_requirements_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',entry_requirements_en)
            #entry_requirements_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',entry_requirements_en)
            #entry_requirements_en = remove_tags(entry_requirements_en)
            #print(entry_requirements_en)
        except:
            entry_requirements_en = None
            #print(entry_requirements_en)
            #print(abc)

#16 中国学生申请要求
        try:
            require_chinese_en = 'Graduation from a university-preparatory program at a senior secondary school: <br><br>Upper Middle School Report of Grades.<br>Huikao or Academic proficiency test results provided by China Credentials Verification (CHESICC) or China Qualifications Verification (CQV).<br>Gaokao examinations results provided by CHESICC or CQV. UBC expects students to achieve  a minimum provincial Tier 1 university cut-off score.<br>If you are not writing the Gaokao, you must submit three or more Advanced Placement (AP) exam results in three or more distinct subjects. Competitive results must be achieved in these examinations.<br>Admission average calculated on final year academic courses/exams:<br><br>Grades required for admission will vary by program, but based on the China grading scale, the minimum average needed to fall within the competitive range is approximately 84% (where the minimum pass grade is 60%).'
            #require_chinese_en = remove_tags(require_chinese_en)
            # print(require_chinese_en)
        except:
            require_chinese_en = None
            # print(require_chinese_en)

#17 特殊专业要求
        try:
            specific_requirement_en = response.xpath('//h4[contains(text(),"Degree-specific")]/following-sibling::*').extract()[0]

            specific_requirement_en = re.sub(' [a-zA-Z\-]*=[\'\"].+?[\'\"]','',specific_requirement_en)
            # specific_requirement_en = specific_requirement_en.replace('\r\n','')
            # specific_requirement_en = remove_tags(specific_requirement_en,keep=("li","ul"))
           # print(specific_requirement_en)
        except:
            specific_requirement_en = None
           # print(specific_requirement_en)

#18 高考(官网要求)
        try:
            gaokao_desc =  'Gaokao examinations results provided by CHESICC or CQV. UBC expects students to achieve  a minimum provincial Tier 1 university cut-off score.'
            gaokao_desc = remove_tags(gaokao_desc)
            # print(gaokao_desc)
        except:
            gaokao_desc = None
            # print(gaokao_desc)

#19 高考(展示以及判断字段)
        try:
            gaokao_zs = response.xpath('').extract()[0]
            gaokao_zs = remove_tags(gaokao_zs)
            # print(gaokao_zs)
        except:
            gaokao_zs = None
            # print(gaokao_zs)

#20 高考分数(文科)
        try:
            gaokao_score_wk = response.xpath('').extract()[0]
            gaokao_score_wk = remove_tags(gaokao_score_wk)
            # print(gaokao_score_wk)
        except:
            gaokao_score_wk = None
            # print(gaokao_score_wk)

#21 高考分数(理科)
        try:
            gaokao_score_lk = response.xpath('').extract()[0]
            gaokao_score_lk = remove_tags(gaokao_score_lk)
            # print(gaokao_score_lk)
        except:
            gaokao_score_lk = None
            # print(gaokao_score_lk)

#22 会考描述
        try:
            huikao_desc = 'Huikao or Academic proficiency test results provided by China Credentials Verification (CHESICC) or China Qualifications Verification (CQV)'
            huikao_desc = remove_tags(huikao_desc)
            # print(huikao_desc)
        except:
            huikao_desc = None
            # print(huikao_desc)

#23 会考描述
        try:
            huikao_zs = response.xpath('').extract()[0]
            huikao_zs = remove_tags(huikao_zs)
            # print(huikao_zs)
        except:
            huikao_zs = None
            # print(huikao_zs)

#24 最低语言要求
        try:
            min_language_require = '6.5, with no part less than 6.0'
            min_language_require = remove_tags(min_language_require)
            # print(min_language_require)
        except:
            min_language_require = None
            # print(min_language_require)

#25 雅思要求
        try:
            ielts_desc = '6.5, with no part less than 6.0'
            #ielts_desc = remove_tags(ielts_desc)
            # print(ielts_desc)
        except:
            ielts_desc = None
            # print(ielts_desc)

#26 ielts
        try:
            ielts = '6.5'
            #ielts = re.findall('\d\.\d',ielts)
            #ielts = remove_tags(ielts)
            #print(ielts)
        except:
            ielts = None
            #print(ielts)
#27 ielts_?

        ielts_l = 6.0
        ielts_s = 6.0
        ielts_r = 6.0
        ielts_w = 6.0

#28 toefl_code
        try:
            toefl_code = '0965'
            #toefl_code = remove_tags(toefl_code)
            # print(toefl_code)
        except:
            toefl_code = None
            # print(toefl_code)

#29 toefl_desc
        try:
            toefl_desc = 'Overall: 90,Reading: 22,Listening: 22,Writing: 21,Speaking: 21'
            #toefl_desc = remove_tags(toefl_desc)
            # print(toefl_desc)
        except:
            toefl_desc = None
            # print(toefl_desc)

#30 toefl
        try:
            toefl = '90'
            #toefl = re.findall('\d\d',toefl)
            #toefl = remove_tags(toefl)
           # print(toefl)
        except:
            toefl = None
           # print(toefl)

#31 toefl_?
        toefl_l = 22
        toefl_s = 21
        toefl_r = 22
        toefl_w = 21

# 32 alevel
        try:
            alevel  = None
            #alevel = remove_tags(alevel)
            # print(alevel)
        except:
            alevel = None
            # print(alevel)

#33 ib
        try:
           ib = 'English-language requirements,English is the language of instruction at UBC. All prospective students must demonstrate English-language competency prior to admission. There are numerous ways to meet the English Language Admission Standard.,General admission requirements,Completion of the IB Diploma with a minimum score of 24 points, including at least three Higher Level courses and additional points for Extended Essay and Theory of Knowledge.,Completion of Standard Level or Higher Level English A at a minimum score of 3, where English is the primary language of instruction.,Degree-specific requirements: Arts,No specific courses required beyond those needed for general admission'
            #print(ib)
        except:
            ib = None
            #print(ib)

#34 ap
        try:
            ap = 'AP courses completed as part of the high school curriculum may be used to meet admission requirements'
            ap = remove_tags(ap)
            # print(ap)
        except:
            ap = None
            # print(ap)

#35 面试描述
        try:
            interview_desc_en = response.xpath('').extract()[0]
            interview_desc_en = remove_tags(interview_desc_en)
            # print(interview_desc_en
        except:
            interview_desc_en = None
            # print(interview_desc_en)

#36 作品集描述
        try:
            portfolio_desc_en = response.xpath('').extract()[0]
            portfolio_desc_en = remove_tags(portfolio_desc_en)
            # print(portfolio_desc_en
        except:
            portfolio_desc_en = None
            # print(portfolio_desc_en)

#37 other
        try:
            other = ''
            #other = remove_tags(other)
            # print(other)
        except:
            other = None
            # print(other)

        # sat act 代码 介绍
        sat_code = '0965'
        sat1_desc = 'SAT 1 or ACT + Writing. In countries where the SAT and ACT are unavailable, exemptions may be granted. UBC’s SAT institution code is 0965 and its ACT institution code is 5259. The optional SAT essay section is recommended, but not required.'
        sat2_desc = None
        act_code = '5259'
        act_desc = 'SAT 1 or ACT + Writing. In countries where the SAT and ACT are unavailable, exemptions may be granted. UBC’s SAT institution code is 0965 and its ACT institution code is 5259. The optional SAT essay section is recommended, but not required.'

        item["ap"] = ap
        item["duration_per"] = duration_per
        item["duration"] = duration
        item["school_name"] = school_name
        item["location"] = location
        item["campus"] = campus
        #item["degree_type"] = 1
        item["department"] = department
        item["degree_name"] = degree_name
        item["degree_overview_en"] = degree_overview_en
        item["major_name_en"] = major_name_en
        item["overview_en"] = overview_en
        #item["teach_time"] = 1
        item["start_date"] = start_date
        item["modules_en"] = modules_en
        item["career_en"] = career_en
        item["deadline"] = deadline
        item["apply_pre"] = 'CAD$'
        item["apply_fee"] = apply_fee
        item["entry_requirements_en"] = entry_requirements_en
        item["tuition_fee_pre"] = 'CAD$'
        item["require_chinese_en"] = require_chinese_en
        item["ielts_desc"] = ielts_desc
        item["ielts"] = ielts
        item["ielts_l"] = ielts_l
        item["ielts_s"] = ielts_s
        item["ielts_r"] = ielts_r
        item["ielts_w"] = ielts_w
        item["toefl_code"] = toefl_code
        item["toefl_desc"] = toefl_desc
        item["toefl_l"] = toefl_l
        item["toefl"] = toefl
        item["toefl_s"] = toefl_s
        item["toefl_r"] = toefl_r
        item["toefl_w"] = toefl_w
        item["interview_desc_en"] = interview_desc_en
        item["portfolio_desc_en"] = portfolio_desc_en
        item["other"] = other
        item["url"] = response.url
        item["gatherer"] = 'weihongbo'
        item["finishing"] = 0
        item["import_status"] = 0
        #item["duration"] = duration
        item["tuition_fee"] = tuition_fee
        item["alevel"] = alevel
        item["ib"] = ib
        item["gaokao_zs"] = gaokao_zs
        item["gaokao_score_wk"] = gaokao_score_wk
        item["gaokao_score_lk"] = gaokao_score_lk
        item["specific_requirement_en"] = specific_requirement_en
        item["huikao_desc"] = huikao_desc
        item["huikao_zs"] = huikao_zs
        item["min_language_require"] = min_language_require
        item["sat_code"] = sat_code
        item["sat1_desc"] = sat1_desc
        item["sat2_desc"] = sat2_desc
        item["act_code"] = act_code
        item["act_desc"] = act_desc
        item["tuition_fee_per"] = tuition_fee_per
        #yield item