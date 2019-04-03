# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
import json
from Australia.middlewares import *
from Australia.items import AustraliaItem

class TheuniversityofsydneyUSpider(scrapy.Spider):
    name = 'TheUniversityOfSydney_U'
    start_urlss=['https://sydney.edu.au/courses/subject-areas/major/accounting0.html',
'https://sydney.edu.au/courses/subject-areas/major/accounting0.html',
'https://sydney.edu.au/courses/subject-areas/major/banking0.html',
'https://sydney.edu.au/courses/subject-areas/major/banking0.html',
'https://sydney.edu.au/courses/subject-areas/major/business-analytics0.html',
'https://sydney.edu.au/courses/subject-areas/major/business-analytics0.html',
'https://sydney.edu.au/courses/subject-areas/major/business-information-systems0.html',
'https://sydney.edu.au/courses/subject-areas/major/business-information-systems0.html',
'https://sydney.edu.au/courses/subject-areas/major/business-law.html',
'https://sydney.edu.au/courses/subject-areas/major/business-law.html',
'https://sydney.edu.au/courses/subject-areas/major/finance0.html',
'https://sydney.edu.au/courses/subject-areas/major/finance0.html',
'https://sydney.edu.au/courses/subject-areas/major/industrial-relations-and-human-resource-management0.html',
'https://sydney.edu.au/courses/subject-areas/major/industrial-relations-and-human-resource-management0.html',
'https://sydney.edu.au/courses/subject-areas/major/international-business0.html',
'https://sydney.edu.au/courses/subject-areas/major/international-business0.html',
'https://sydney.edu.au/courses/subject-areas/major/management0.html',
'https://sydney.edu.au/courses/subject-areas/major/management0.html',
'https://sydney.edu.au/courses/subject-areas/major/marketing0.html',
'https://sydney.edu.au/courses/subject-areas/major/marketing0.html',]
    start_urls=set(start_urlss)
    def parse(self, response):
        item=get_item(AustraliaItem)
        item['university'] = 'The University of Sydney'
        item['url'] = response.url
        programme_en = response.xpath('//h2[@class="pageTitle"]/text()').extract()
        item['programme_en'] = ''.join(programme_en).strip()
        overview = response.xpath('//div[contains(@class,"overview")]//div[contains(@class,"full-text")]').extract()
        item['overview_en'] = remove_class(overview)
        modules = response.xpath('//div[@class="subject-area-rte-common course-rte-common parbase"]').extract()
        item['modules_en'] = remove_class(modules)
        career=response.xpath('//h3[contains(text(),"areer")]/following-sibling::*').extract()
        item['career_en']=remove_class(career)
        # print(career)
        item['department']='University of Sydney Business School'
        item['toefl_desc']='A minimum result of 96 overall including a minimum result of 17 in Reading, Listening and Speaking and 19 in Writing'
        item['toefl'],item['toefl_l'],item['toefl_s'],item['toefl_r'],item['toefl_w']='96','17','17','17','19'
        item['ielts_desc']='A minimum result of 7.0 overall and a minimum result of 6.0 in each band'
        item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']='7.0','6.0','6.0','6.0','6.0'
        item['tuition_fee']='40,500'
        item['tuition_fee_pre']='AUD'
        item['apply_pre']='AUD'
        item['apply_fee']='125'
        item['start_date']='2019-02,2019-08'
        item['deadline']='01-31,06-30'
        modules=['<h4>Sample study plan: Bachelor of Commerce, majoring in Finance and Economics</h4>',
'<p><b>Year 1 – Semester 1</b></p>',
'<ul>',
'<li>Degree core: <i>Future of Business</i></li>',
'<li>Degree core + Finance major core: <i>Quantitative Business Analysis</i></li>',
'<li>Finance and Economics major core: <i>Economics for Business Decision Making</i></li>',
'<li>Elective from Table A or Table S</li>',
'</ul>',
'<p><b>Year 1 – Semester 2</b></p>',
'<ul>',
'<li>Degree core: <i>Accounting, Business and Society</i></li>',
'<li>Economics major core: <i>Introductory Macroeconomics</i></li>',
'<li>Elective from Table A or Table S<i></i></li>',
'<li>Elective from Table A or Table S<i></i></li>',
'</ul>',
'<p><b>Year 2 – Semester 1</b></p>',
'<ul>',
'<li>Degree core: <i>Leading and Influencing Business</i></li>',
'<li>Open Learning Environment elective/s (6 credit points in total)</li>',
'<li>Finance major core: <i>Corporate Finance I</i></li>',
'<li>Economics major core: <i>Intermediate Microeconomics</i></li>',
'</ul>',
'<p><b>Year 2 – Semester 2</b></p>',
'<ul>',
'<li>Open Learning Environment elective/s (6 credit points in total)</li>',
'<li>Finance major core: <i>Corporate Finance II</i></li>',
'<li>Economics major core: <i>Intermediate Macroeconomics</i></li>',
'<li>Elective from Table A or Table S</li>',
'</ul>',
'<p><b>Year 3 – Semester 1</b></p>',
'<ul>',
'<li>Finance major core: <i>Investments and Portfolio Management</i></li>',
'<li>Finance major selective (3000-level)</li>',
'<li>Economics major selective (3000-level)</li>',
'<li>Economics major selective (3000-level)</li>',
'</ul>',
'<p><b>Year 3 – Semester 2</b></p>',
'<ul>',
'<li>Finance major core: <i>Finance in Practice</i></li>',
'<li>Finance major elective (3000-level)</li>',
'<li>Economics major selective (3000-level)</li>',
'<li>Economics major selective (3000-level).</li>',
'</ul>',]
        item['modules_en']=remove_class(modules)
        overview=['<div class="b-more-information-content__content-wrapper b-component--tiny">',
'<p>',
'</p><p><b>Your global business journey starts here. Our Bachelor of Commerce offers a wide variety of subject options, interactive learning experiences and a strong commercial grounding in business. Take advantage of our international exchange and industry placement opportunities and tailor your degree to launch your career in virtually any field, anywhere in the world.</b></p>',
'<p>The three-year, full-time (or equivalent part-time) program combines theory and practice to build your understanding of how businesses operate. You’ll gain the analytical, technical and practical skills to apply your knowledge effectively in your career.</p>',
'<p><b>Bachelor of Advanced Studies</b></p>',
'<p>You can also choose to combine your Bachelor of Commerce degree with the <a href="http://sydney.edu.au/courses/bachelor-of-commerce-and-bachelor-of-advanced-studies">Bachelor of Advanced Studies </a>. In the Bachelor of Advanced Studies, you can complete a second major, combine studies from a range of disciplines, undertake advanced coursework, and get involved in cross-disciplinary community, professional, research or entrepreneurial project work.</p>',
'<p>To succeed in business, graduates need to be equipped with a solid grounding in areas such as accounting and business statistics, as well as leadership skills and a global mindset. Our Bachelor of Commerce combines theory and practice to teach you how businesses operate. Alongside technical development, you will gain the critical thinking and problem-solving skills to apply your knowledge effectively in the business world. Our core units, <i>Future of Business </i>and <i>Leading and Influencing in Business </i>, have been specifically designed to prepare you for the contemporary workforce and a global career.</p>',
'<p>Building on this foundation, you can choose up to two majors. At least one major must be chosen from our wide range of business subject areas, including: accounting; banking; business analytics; business information systems; business law; finance; industrial relations and human resource management; international business; management; and marketing.</p>',
'<p><b>Why study here?</b></p>',
'<ul>',
'<li><b>Build your global network </b>as you connect with our Australian and international partners</li>',
'<li>Take advantage of exchange opportunities and <b>work with leading companies in Sydney, Southeast Asia, Europe, the United States and South America </b>through our industry placements</li>',
'</ul>',
'</div>',]
        item['degree_overview_en']=remove_class(overview)
        rntry_requirements=['<p>To qualify for the award of the Bachelor of Commerce, a student must complete units of study totalling 144 credit points, comprising:</p>',
'<ul>',
'<li>24 credit points of degree core units of study;</li>',
'<li>a major (48 credit points) or program;</li>',
'<li>a minor (36 credit points) or a second major (48 credit points);</li>',
'<li>12 credit points of units of study in the Open Learning Environment; and</li>',
'<li>where appropriate, any additional elective units of study required making the total of 144 credit points for the degree.</li>',
'</ul>',]
        item['rntry_requirements_en']=remove_class(rntry_requirements)
        yield item
    def parses(self, response):
        item=get_item(AustraliaItem)
        item['university'] = 'The University of Sydney'
        item['url'] = response.url
        #判断是否存在课程设置页面的链接
        modules_url=response.xpath('//a[contains(text(),"Study plan for this course")]/@href').extract()
        if modules_url!=[]:
            modules=self.modulesGet(modules_url[0])
        #判断是否专业跳学位页面的链接列表
    # def xueweiye(self,response):
    #     item = get_item(AustraliaItem)
    #     item['university'] = 'The University of Sydney'
    #     item['url'] = response.url
    #     modules_url = response.xpath('//a[contains(text(),"Study plan for this course")]/@href').extract()

    def modulesGet(self,url):
        modRes=requests.get(url).content
        modRes=etree.HTML(modRes)
        


    def parsesss(self, response):
        pro_url = response.xpath('//ul/li/a/@href').extract()
        for i in pro_url:
            full_url = 'https://sydney.edu.au' + i
            if 'bachelor' in full_url:
                yield scrapy.Request(url=full_url, callback=self.parse_main)
        next_page = response.xpath('//a[@title="Next page"]/@href').extract()
        next_page = re.findall('\d+', ''.join(next_page))
        if next_page != []:
            next_page_url = 'https://sydney.edu.au/content/courses/search.result-courses.aoi-.course-level-u.page%s.html' % ''.join(
                next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
    def parse_main(self,response):
        item=get_item(AustraliaItem)
        degree_name = response.xpath('//div[@class="titleColumn"]//h2/div/text()').extract()
        degree_name = ''.join(degree_name).strip()
        programme = re.findall('\(.+\)', degree_name)
        if programme == []:
            programme = degree_name.replace('Master of', '').strip()
        else:
            print(response.url)
            item['programme_en'] = ''.join(programme).replace('(', '').replace(')', '').strip()
        item['degree_name'] = degree_name
        item['programme_en'] = programme

        duration = re.findall('Duration.*', response.text)
        # print(duration)
        duration = ''.join(duration).replace('0.5', '1')
        duration = clear_duration(duration)
        # print(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']
        item['university'] = 'The University of Sydney'
        item['url'] = response.url
        item['apply_fee'] = '125'
        item['apply_pre'] = 'AUD'
        item['location'] = 'Sydney'
        item['degree_type']='1'

        start_date = re.findall('Starting date</h3>\s*<div class="b-see-more-content b-js-see-more-content">\s*<div class="b-see-more-content__summary">\s*<p>.*</p>',response.text)
        start_date = ''.join(start_date).strip()
        start_date = re.findall('p>[a-zA-Z\s0-9\)\(\./\*]*</p', start_date)
        start_date = re.findall('\([A-Za-z]+\)', ''.join(start_date))
        start_date = set(start_date)
        start_date = tracslateDate(start_date)
        start_date = ','.join(start_date)
        item['start_date'] = start_date

        application_open_date = re.findall('pplications open[:\s;a-zA-Z0-9\.]+</p', response.text)
        application_open_date = set(application_open_date)
        application_open_date = ''.join(application_open_date).replace('st', '').strip()
        application_open_date = tracslateDate(application_open_date)
        application_open_date = set(application_open_date)
        application_open_date = ','.join(application_open_date)
        item['application_open_date'] = application_open_date

        deadline = re.findall('pplications close[:\s;a-zA-Z0-9\.]+</p', response.text)
        deadline = set(deadline)
        deadline = ''.join(deadline).replace('st', '').strip()
        deadline = tracslateDate(deadline)
        deadline = set(deadline)
        deadline = ','.join(deadline)
        item['deadline'] = deadline

        ielts_url='https://sydney.edu.au/content/courses/courses/uc/'+response.url.split('/')[-1].replace('.html','.entryrequirement.year.country.json')
        ieltsRes = requests.get(ielts_url).text
        text1 = re.findall('"erqText":"[\sa-zA-Z0-9\.]*"', ieltsRes)
        text1 = ' '.join(set(text1))
        ielts_desc = re.findall('A minimum result of\s\d\.\d[\sa-zA-Z0-9\.]*', text1)
        toefl_desc = re.findall('A minimum result of\s\d{2}\s[\sa-zA-Z0-9\.,]*', urls1_content)
        ielts = re.findall('[6-9]\.[05]', text1)
        toefl = re.findall('\s\d{2}\s', ''.join(toefl_desc))
        ielts_desc = ''.join(ielts_desc).strip()
        toefl_desc = ''.join(toefl_desc).strip()
        item['toefl_desc'] = toefl_desc
        item['ielts_desc'] = ielts_desc
        if len(toefl) == 3:
            item['toefl'] = toefl[0]
            item['toefl_l'] = toefl[1]
            item['toefl_s'] = toefl[1]
            item['toefl_r'] = toefl[1]
            item['toefl_w'] = toefl[2]
        ielts = get_ielts(ielts)
        if ielts != {} and ielts != []:
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            item['ielts'] = ielts['IELTS']

        fee_url='https://sydney.edu.au/content/courses/courses/uc/'+response.url.split('/')[-1].replace('.html','.fee.json')
        fee_response = requests.get(fee_url).text
        fee_json=json.loads(fee_response)['courseFee']['2019']
        # print(fee_json)
        for fe in fee_json:
            if fe['type']=='INTFEE':
                tuition_fee=fe['amount']
                # print(tuition_fee)
                item['tuition_fee'] = tuition_fee.replace('$','').replace(',','').strip()
        item['tuition_fee_pre'] = 'AUD'

        depa_url='https://sydney.edu.au/content/courses/courses/uc/'+response.url.split('/')[-1].replace('.html','.details.json')
        depa_response = requests.get(depa_url).text
        try:
            depa_json=json.loads(depa_response)['facultyTitle']
            # print(depa_json)
            item['department'] = depa_json
        except:
            pass

        how_to_apply = ['<p>How you apply depends on your qualifications and the course for which you are applying.</p>',
'<p>Apply through the Universities Admissions Centre (UAC) if you are completing:</p>',
'<ul>',
'<li>a current Australian Year 12 secondary school examination (eg, NSW Higher School Certificate, Victorian Certificate of Education, Queensland Certificate of Education) in or outside Australia, or</li>',
'<li>a current International Baccalaureate (IB) diploma in Australia.</li>',
'</ul>',
'<p>The University generally participates in all the UAC international offer rounds. Refer to the <a href="http://www.uac.edu.au/international/key-dates.shtml">UAC website</a> for key dates.</p>',
'<p>Apply directly to the University if you are:</p>',
'<ul>',
'<li><p>an applicant not covered in the above UAC categories</p>',
'</li>',
'<li><p>applying for a Sciences-Po dual degree (even if you are applying through UAC for other degrees).</p>',
'</li>',
'</ul>',
'<p>To apply directly to the University, visit <a href="http://sydney.edu.au/study/find-a-course.html">Find a Course</a> and search for your course, then click on the &quot;Apply now&quot; button on the course page.</p>',
'<p>You can use one of the application checklists on the right or watch our ‘How to apply’ <a href="https://www.youtube.com/watch?v=C9xqRWa8s2c">video</a> to learn about the documents you need, the application process, and the websites you can visit for further information.  </p>',
'<p>To find out more about qualifications we accept, visit our <a href="https://sydney.edu.au/study/admissions/apply/admission-criteria/international-students.html">international students page</a> in the admission criteria section.</p>',
'<p>We recommend applying well before the closing date for your course, to ensure you have adequate time to arrange your <a href="http://sydney.edu.au/study/admissions/apply/visas.html">student visa</a>, flights and <a href="http://sydney.edu.au/campus-life/accommodation.html">accommodation</a>.</p>',
'<p>A non-refundable application processing fee of A$125 is charged for new prospective students. This fee is waived if you’re a sponsored student, or if you are granted an exemption by a University staff member during an office interview or recruitment event.</p>',
'<p>If you would like to apply through a University approved agent, we have partnered with a range of <a href="http://sydney.edu.au/study/admissions/apply/agents-overseas.html">agents and representatives</a> who can apply to the University and make arrangements on your behalf.</p>',]
        how_to_apply = remove_class(how_to_apply)
        item['apply_documents_en'] = how_to_apply

        entry = response.xpath('//h3[contains(text(),"Admission criteria")]/following-sibling::*').extract()
        entry = remove_class(entry)
        item['rntry_requirements_en'] = entry

        modules = response.xpath('//h4[contains(text(),"What you")]/following-sibling::div').extract()
        modules = remove_class(modules)
        item['modules_en'] = modules

        overview = response.xpath('//h3[contains(text(),"Overview")]/following-sibling::*').extract()
        overview = remove_class(overview)
        item['degree_overview_en'] = overview

        career = response.xpath('//*[contains(text(),"Careers & future study")]/../../following-sibling::div').extract()
        career = remove_class(career)
        item['career_en'] = career
        major_url='https://sydney.edu.au/content/courses/courses/uc/'+response.url.split('/')[-1].replace('.html','.shared-pathways.json')
        try:
            major_content=requests.get(major_url).text
            major_url_json=json.loads(major_content)['2019']
            # print(major_url_json)
            major_link=[]
            for mj in major_url_json:
                major_link.append('https://sydney.edu.au'+mj['href'])
            # print(major_link)
            if major_link!=[]:
                for i in major_link:
                    if '/major/' in i:
                        item['url']=i
                        major_list=self.getMajor(i)
                        if major_list[0]!='':
                            item['programme_en']=major_list[0]
                            item['overview_en']=major_list[1]
                            item['modules_en']=major_list[2]
                        # yield item
        except:
            pass
    def getMajor(self,url):
        maRes=etree.HTML(requests.get(url).content)
        major_name=maRes.xpath('//h2[@class="pageTitle"]/text()')
        major_name=''.join(major_name).strip()
        major_overview=maRes.xpath('//div[@class="b-see-more-content__summary"]')
        major_ov=''
        for mo in major_overview:
            major_ov+=etree.tostring(mo,method='html',encoding='unicode')
        major_modules=maRes.xpath('//h5[contains(text(),"CORE")]/following-sibling::ul/li/a')
        major_mod=''
        for mm in major_modules:
            major_mod+=etree.tostring(mm,method='html',encoding='unicode')
        return major_name,major_ov,major_mod