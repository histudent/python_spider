# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/3 16:22'
import scrapy,json
import re
import  requests
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from w3lib.html import remove_tags
from scrapySchool_England.clearSpace import  clear_space_str
import urllib.request
from  lxml import etree
class UniversityofEssexSpider(scrapy.Spider):
    name = 'UniversityofEssex_p'
    allowed_domains = ['essex.ac.uk/']
    start_urls = []
    C = [
        'https://www.essex.ac.uk/courses/pg00679/1/msc-marketing-and-brand-management',
        'https://www.essex.ac.uk/courses/pg00627/1/msc-intelligent-systems-and-robotics',
        'https://www.essex.ac.uk/courses/pg00720/1/msc-physiotherapy-pre-registration',
        'https://www.essex.ac.uk/courses/pg01302/1/ma-international-development?startdate=2019/20',
        'https://www.essex.ac.uk/courses/pg00555/1/ma-english-language-and-linguistics',
        'https://www.essex.ac.uk/courses/pg00428/1/msc-accounting-and-financial-management',
        'https://www.essex.ac.uk/courses/pg00637/1/llm-international-human-rights-law',
        'https://www.essex.ac.uk/courses/pg00633/3/llm-international-commercial-and-business-law',
        'https://www.essex.ac.uk/courses/pg01071/1/ma-translation-and-professional-practice',
        'https://www.essex.ac.uk/courses/pg00761/1/ma-public-opinion-and-political-behaviour',
        'https://www.essex.ac.uk/courses/pg00594/1/ma-global-and-comparative-politics',
        'https://www.essex.ac.uk/courses/pg00463/1/msc-big-data-and-text-analytics',
        'https://www.essex.ac.uk/courses/pg00697/1/msc-occupational-therapy-pre-registration',
        'https://www.essex.ac.uk/courses/pg00702/1/msc-organised-crime-terrorism-and-security',
        'https://www.essex.ac.uk/courses/pg01105/1/llm-international-trade-and-maritime-law',
        'https://www.essex.ac.uk/courses/pg00639/1/msc-international-marketing-and-entrepreneurship',
        'https://www.essex.ac.uk/courses/pg00671/1/ma-management-and-organisational-dynamics',
        'https://www.essex.ac.uk/courses/pg00541/1/llm-economic-social-and-cultural-rights',
        'https://www.essex.ac.uk/courses/pg01067/1/msc-international-accounting-and-banking',
        'https://www.essex.ac.uk/courses/pg00631/1/msc-international-business-and-entrepreneurship',
        'https://www.essex.ac.uk/courses/pg00833/1/ma-theory-and-practice-of-human-rights',
        'https://www.essex.ac.uk/courses/pg01072/1/ma-business-translation-and-interpreting-chinese-english',
        'https://www.essex.ac.uk/courses/pg00495/1/msc-computational-economics-financial-markets-and-policy',
        'https://www.essex.ac.uk/courses/pg01105/2/llm-international-trade-and-maritime-law',
        'https://www.essex.ac.uk/courses/pg00803/1/msc-speech-and-language-therapy-pre-registration',
        'https://www.essex.ac.uk/courses/pg01288/1/ma-chinese-english-translation-and-professional-practice',
        'https://www.essex.ac.uk/courses/pg00472/1/master-of-business-administration,-c-,-the-essex-mba',
        'https://www.essex.ac.uk/courses/pg01102/1/msc-international-logistics-and-supply-chain-management',
        'https://www.essex.ac.uk/courses/pg01134/1/ma-conference-interpreting-and-translation-chinese-english',
        'https://www.essex.ac.uk/courses/pg00845/1/ma-wild-writing-literature-landscape-and-the-environment',
        'https://www.essex.ac.uk/courses/pg00647/1/ma-jungian-and-post-jungian-studies',
        'https://www.essex.ac.uk/courses/pg00599/1/ma-health-and-organisational-research',
        'https://www.essex.ac.uk/courses/pg00695/1/msc-nursing-pre-registration',
        'https://www.essex.ac.uk/courses/pg00619/1/ma-human-rights-and-cultural-diversity',
        'https://www.essex.ac.uk/courses/pg00815/1/ma-teaching-english-to-speakers-of-other-languages-tesol',
        'https://www.essex.ac.uk/courses/pg00727/1/ma-politics',
        'https://www.essex.ac.uk/courses/pg00542/7/ma-economics',
        'https://www.essex.ac.uk/courses/pg00542/2/mres-economics',
        'https://www.essex.ac.uk/courses/pg00609/1/ma-history',
        'https://www.essex.ac.uk/courses/pg00521/1/ma-criminology',
        'https://www.essex.ac.uk/courses/pg00368/2/msc-mathematics',
        'https://www.essex.ac.uk/courses/pg00783/1/ma-sociology',
        'https://www.essex.ac.uk/courses/pg00542/1/msc-economics',
        'https://www.essex.ac.uk/courses/pg00670/1/msc-management',
        'https://www.essex.ac.uk/courses/pg00542/8/msc-economics',
        'https://www.essex.ac.uk/courses/pg00662/2/mres-linguistics',
        'https://www.essex.ac.uk/courses/pg00579/1/msc-finance',
        'https://www.essex.ac.uk/courses/pg00586/1/msc-financial-economics',
        'https://www.essex.ac.uk/courses/pg00724/3/mres-political-economy',
        'https://www.essex.ac.uk/courses/pg00431/1/ma-acting',
        'https://www.essex.ac.uk/courses/pg00662/1/ma-linguistics',
        'https://www.essex.ac.uk/courses/pg00673/1/msc-management-economics',
        'https://www.essex.ac.uk/courses/pg00425/1/msc-accounting',
        'https://www.essex.ac.uk/courses/pg00755/1/msc-psychology',
        'https://www.essex.ac.uk/courses/pg00147/2/mfa-acting-international',
        'https://www.essex.ac.uk/courses/pg01022/1/msc-statistics',
        'https://www.essex.ac.uk/courses/pg00591/1/ma-curating',
        'https://www.essex.ac.uk/courses/pg00742/1/msc-data-science',
        'https://www.essex.ac.uk/courses/pg00742/2/msc-data-science',
        'https://www.essex.ac.uk/courses/pg00462/1/msc-behavioural-economics',
        'https://www.essex.ac.uk/courses/pg00665/1/ma-literature',
        'https://www.essex.ac.uk/courses/pg01042/1/msc-marketing-management',
        'https://www.essex.ac.uk/courses/pg00706/1/ma-philosophy',
        'https://www.essex.ac.uk/courses/pg00641/1/ma-international-relations',
        'https://www.essex.ac.uk/courses/pg00634/1/msc-international-economics',
        'https://www.essex.ac.uk/courses/pg00830/1/ma-theatre-directing',
        'https://www.essex.ac.uk/courses/pg00638/1/msc-international-management',
        'https://www.essex.ac.uk/courses/pg00688/1/msc-money-and-banking',
        'https://www.essex.ac.uk/courses/pg00722/1/ma-playwriting',
        'https://www.essex.ac.uk/courses/pg00747/1/ma-psychoanalytic-studies',
        'https://www.essex.ac.uk/courses/pg00591/3/ma-curating',
        'https://www.essex.ac.uk/courses/pg00641/2/msc-international-relations',
        'https://www.essex.ac.uk/courses/pg00575/1/mres-experimental-linguistics',
        'https://www.essex.ac.uk/courses/pg00763/1/ma-refugee-care',
        'https://www.essex.ac.uk/courses/pg01111/1/ma-avant-gardes',
        'https://www.essex.ac.uk/courses/pg00661/1/ma-linguistic-studies',
        'https://www.essex.ac.uk/courses/pg00519/1/ma-creative-writing',
        'https://www.essex.ac.uk/courses/pg00779/1/ma-language-in-society',
        'https://www.essex.ac.uk/courses/pg00448/1/ma-applied-linguistics',
        'https://www.essex.ac.uk/courses/pg00830/2/mfa-theatre-directing',
        'https://www.essex.ac.uk/courses/pg00366/1/msc-health-research',
        'https://www.essex.ac.uk/courses/pg00786/1/ma-sociology-and-management',
        'https://www.essex.ac.uk/courses/pg01139/1/ma-united-states-politics',
        'https://www.essex.ac.uk/courses/pg00635/1/msc-international-finance',
        'https://www.essex.ac.uk/courses/pg00445/1/mres-analysing-language-use',
        'https://www.essex.ac.uk/courses/pg00577/1/ma-film-studies',
        'https://www.essex.ac.uk/courses/pg00543/1/msc-economics-and-econometrics',
        'https://www.essex.ac.uk/courses/pg00686/1/msc-molecular-medicine',
        'https://www.essex.ac.uk/courses/pg00724/2/msc-political-economy',
        'https://www.essex.ac.uk/courses/pg01023/1/msc-business-analytics',
        'https://www.essex.ac.uk/courses/pg01053/1/mres-political-science-mres',
        'https://www.essex.ac.uk/courses/pg00725/2/msc-political-science',
        'https://www.essex.ac.uk/courses/pg01140/2/msc-migration-studies',
        'https://www.essex.ac.uk/courses/pg00508/1/ma-conflict-resolution',
        'https://www.essex.ac.uk/courses/pg00469/1/msc-biotechnology',
        'https://www.essex.ac.uk/courses/pg00751/1/ma-psycholinguistics',
        'https://www.essex.ac.uk/courses/pg00508/2/msc-conflict-resolution',
        'https://www.essex.ac.uk/courses/pg00425/4/mres-accounting',
        'https://www.essex.ac.uk/courses/pg01081/1/msc-actuarial-science',
        'https://www.essex.ac.uk/courses/pg00585/1/msc-financial-econometrics',
        'https://www.essex.ac.uk/courses/pg00641/3/mres-international-relations',
        'https://www.essex.ac.uk/courses/pg00726/1/ma-political-theory',
        'https://www.essex.ac.uk/courses/pg00724/1/ma-political-economy',
        'https://www.essex.ac.uk/courses/pg00725/1/ma-political-science',
        'https://www.essex.ac.uk/courses/pg00147/1/ma-acting-international',
        'https://www.essex.ac.uk/courses/pg00426/1/msc-accounting-and-finance',
        'https://www.essex.ac.uk/courses/pg00736/2/ma-professional-practice',
        'https://www.essex.ac.uk/courses/pg01140/1/ma-migration-studies',
        'https://www.essex.ac.uk/courses/pg00610/1/msc-mathematics-and-finance',
        'https://www.essex.ac.uk/courses/pg01044/1/ma-american-literatures',
        'https://www.essex.ac.uk/courses/pg00837/1/msc-tropical-marine-biology',
        'https://www.essex.ac.uk/courses/pg01033/1/msc-computer-games',
        'https://www.essex.ac.uk/courses/pg01301/1/ma-theatre-practice',
        'https://www.essex.ac.uk/courses/pg01032/1/msc-finance-and-global-trading',
        'https://www.essex.ac.uk/courses/pg00764/1/msc-research-methods-in-psychology',
        'https://www.essex.ac.uk/courses/pg00582/1/msc-financial-and-business-economics',
        'https://www.essex.ac.uk/courses/pg00461/1/msc-banking-and-finance',
        'https://www.essex.ac.uk/courses/pg00644/1/llm-international-trade-law',
        'https://www.essex.ac.uk/courses/pg00558/1/msc-entrepreneurship-and-innovation',
        'https://www.essex.ac.uk/courses/pg00500/1/msc-computer-engineering',
        'https://www.essex.ac.uk/courses/pg01145/1/msc-cognitive-neuroscience-and-neuropsychology',
        'https://www.essex.ac.uk/courses/pg00457/1/msc-artificial-intelligence',
        'https://www.essex.ac.uk/courses/pg01303/1/msc-quantitative-international-development',
        'https://www.essex.ac.uk/courses/pg00548/1/msc-internet-of-things',
        'https://www.essex.ac.uk/courses/pg01036/1/msc-human-resource-management',
        'https://www.essex.ac.uk/courses/pg00581/1/msc-finance-and-management',
        'https://www.essex.ac.uk/courses/pg00782/1/ma-sociological-research-methods',
        'https://www.essex.ac.uk/courses/pg00576/1/ma-film-and-literature',
        'https://www.essex.ac.uk/courses/pg00621/1/ma-ideology-and-discourse-analysis',
        'https://www.essex.ac.uk/courses/pg00430/1/mres-management-and-organisations',
        'https://www.essex.ac.uk/courses/pg00808/1/msc-statistics-and-operational-research',
        'https://www.essex.ac.uk/courses/pg00594/2/msc-global-and-comparative-politics',
        'https://www.essex.ac.uk/courses/pg00587/1/msc-financial-economics-and-econometrics',
        'https://www.essex.ac.uk/courses/pg01014/1/msc-finance-and-data-analytics',
        'https://www.essex.ac.uk/courses/pg01137/1/llm-international-humanitarian-law',
        'https://www.essex.ac.uk/courses/pg00605/1/msc-algorithmic-trading',
        'https://www.essex.ac.uk/courses/pg00546/1/msc-electronic-engineering',
        'https://www.essex.ac.uk/courses/pg00595/1/msc-global-project-management',
        'https://www.essex.ac.uk/courses/pg00496/1/msc-computational-finance',
        'https://www.essex.ac.uk/courses/pg00835/1/ma-translation-and-literature',
        'https://www.essex.ac.uk/courses/pg00427/1/msc-financial-economics-and-accounting',
        'https://www.essex.ac.uk/courses/pg01101/2/master-of-business-management-mbm',
        'https://www.essex.ac.uk/courses/pg00435/1/msc-advanced-computer-science',
        'https://www.essex.ac.uk/courses/pg00580/1/msc-finance-and-investment',
        'https://www.essex.ac.uk/courses/pg00456/1/ma-art-history-and-theory',
        'https://www.essex.ac.uk/courses/pg00447/1/msc-applied-economics-and-data-analysis',
        'https://www.essex.ac.uk/courses/pg00441/1/ma-advertising-marketing-and-the-media',
        'https://www.essex.ac.uk/courses/pg00522/1/msc-criminology-and-socio-legal-research',
        'https://www.essex.ac.uk/courses/pg00836/1/ma-translation-interpreting-and-subtitling',
        'https://www.essex.ac.uk/courses/pg00695/2/msc-nursing-pre-registration',
        'https://www.essex.ac.uk/courses/pg01071/2/ma-translation-and-professional-practice',
        'https://www.essex.ac.uk/courses/pg01067/2/msc-international-accounting-and-banking',
        'https://www.essex.ac.uk/courses/pg01146/1/msc-sport-and-exercise-psychology',
        'https://www.essex.ac.uk/courses/pg00761/2/msc-public-opinion-and-political-behaviour',
        'https://www.essex.ac.uk/courses/pg01127/1/msc-sport-and-exercise-science',
        'https://www.essex.ac.uk/courses/pg00813/1/msc-survey-methods-for-social-research',
        'https://www.essex.ac.uk/courses/pg00588/1/msc-financial-engineering-and-risk-management',
        'https://www.essex.ac.uk/courses/pg00633/1/llm-international-commercial-and-business-law',
        'https://www.essex.ac.uk/courses/pg00819/1/msc-advanced-communication-systems',
        'https://www.essex.ac.uk/courses/pg00502/1/msc-computer-networks-and-security'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Essex'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="content"]//h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        degree_name = programme_en.split()[0]
        # print(degree_name)
        programme_en = programme_en.replace(degree_name,'').strip()
        # print(programme_en)
        #6.start_date
        start_date = response.xpath("//*[contains(text(),'Start date')]//following-sibling::select").extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        start_date = clear_space_str(start_date)
        if 'Oct 2018/19' in start_date:
            start_date = '2018-10,2019-10'
        else:
            start_date = '2018-9,2019-9'
        # print(start_date)

        #7.teach_time
        teach_time = response.xpath("//*[contains(text(),'Study mode')]//following-sibling::select").extract()
        teach_time = ''.join(teach_time)
        teach_time = remove_tags(teach_time)
        if 'Full Time' in teach_time:
            teach_time = 'Full Time'
        else:
            teach_time = 'Part Time'
        # print(teach_time)

        #8.duration #9.duration_per
        duration_list = response.xpath("//*[contains(text(),'Duration')]//following-sibling::*").extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        duration_a = re.findall('\d',duration_list)[0]
        if duration_list == '1 years 8 months':
            duration = '20'
            duration_per = 3
        elif int(duration_a)<5:
            duration = duration_a
            duration_per = 1
        else:
            duration = duration_a
            duration_per = 3
        # print(duration,'(((',duration_per)

        #10.location
        location = response.xpath("//*[contains(text(),'Location')]//following-sibling::span").extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #11.department
        department_a =response.xpath("//*[contains(text(),'Based in')]//following-sibling::*").extract()
        department_a =''.join(department_a)
        department_a = remove_tags(department_a)
        if len(department_a)>500:
            department = 'N/A'
        else:
            department = department_a
        # print(department)

        #12.overview_en
        overview_en = response.xpath('//*[@id="overview"]//p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #13.ielts 14151617
        ielts_list = response.xpath('//*[@id="entry-requirements"]//text()').extract()
        ielts_list = ''.join(ielts_list)
        ielts = re.findall('\d\.\d',ielts_list)
        # print(ielts)
        if '2.2'  in ielts:
            ielts.remove('2.2')
            if '2.1' in ielts:
                ielts.remove('2.1')
            else:
                pass
        elif '2.1' in ielts:
            ielts.remove('2.1')
        else:
            pass
        # print(ielts)

        if len(ielts) == 2:
            a = ielts[0]
            b = ielts[1]
            ielts = a
            ielts_s = b
            ielts_w = b
            ielts_l = b
            ielts_r = b
        elif len(ielts) ==3:
            a = ielts[0]
            b = ielts[1]
            c = ielts[2]
            ielts = a
            ielts_w = b
            ielts_r = c
            ielts_l = c
            ielts_s = c
        elif len(ielts) ==4:
            a = ielts[0]
            b = ielts[1]
            ielts = a
            ielts_s = b
            ielts_w = b
            ielts_l = b
            ielts_r = b
        else:
            ielts = 6.0
            ielts_w = 5.5
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        # print(ielts,ielts_w,ielts_r,ielts_l,ielts_s)

        #18.modules_en
        modules_en = response.xpath("//div[@class='tabs__panels content-padding']").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        modules_en = clear_space_str(modules_en)
        # print(modules_en)

        #19.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'International fee')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = tuition_fee.replace(',','')
        tuition_fee = tuition_fee.replace('£','')
        if tuition_fee == 'TBC':
            tuition_fee = None
        elif len(tuition_fee) >=200:
            tuition_fee = None
        else:
            pass
        # print(tuition_fee)

        #20.tuition_fee_pre
        tuition_fee_pre = '£'

        #21.apply_proces_en
        apply_proces_en = 'https://www1.essex.ac.uk/pgapply/login.aspx'

        #22.rntry_requirements
        rntry_requirements = response.xpath('//*[@id="entry-requirements"]/div//p[1]').extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #23.require_chinese_en
        chi_url = re.findall(r'courses/pg(.*)/',url)[0]
        chi_url1 = re.findall('\d+',chi_url)
        a = chi_url1[0]
        b = chi_url1[1]
        chi_url2 = 'https://www.essex.ac.uk/api/sitecore/coursePage/EntryRequirementInternational?mastercourseid=PG'+str(a)+'&subgroupcode='+str(b)+'&courseyear=18&countrykey=631'
        data = requests.get(chi_url2)
        data_list = etree.HTML(data.text)
        require_chinese_en = data_list.xpath('/html/body/div/p/text()')
        require_chinese_en = ''.join(require_chinese_en)
        require_chinese_en = '<p>'+require_chinese_en+'</p>'
        # print(require_chinese_en)

        #24.apply_documents_en

        apply_documents_en= "<p>Necessary documents When you apply to study with us, you'll need to provide a number of supporting documents - we can't process your application until we have these. Some of these documents you will have to upload with your application, others you may be able to upload at a later date. We may ask to see original documents if you are offered a place. English language If you have received your test results you may include a copy with your application. The main tests we accept are IELTS, TOEFL or Pearson, and the test must be less than two years old at the time of admission. The IELTS requirement for your course is listed on our Postgraduate Research Finder. You can also see more detailed information about English language requirements here (.pdf) Transcripts Official transcript(s), in English or a certified translation of your academic results to date, showing marks or grades, must be provided at the time you make your application. (Transcripts are not required from current or previous University of Essex students, or from students who have previously completed a degree at Colchester Institute awarded by the University of Essex). CV A CV is required for some research degrees at the time of application. Research proposal Requirements vary across departments but two references and a research proposal are required for all research degrees.  A research proposal is required at application stage for most research degrees. Think about your research idea - during your PhD you will conduct and present the results of your original investigations and research. You need to ensure that your research topic will be interesting enough for three or four years. Start to research your topic by reading around your subject area and begin to think what you might like to include in your research proposal. Get in touch with a suitable department by contacting the Graduate Director - you might still be developing your idea at this stage, but it would be great if you could send a short description of your research area and a copy of your CV. This does not need to be longer than one A4 page. You can search for a department or supervisor through our Postgraduate Research Finder. Writing your proposalYour research proposal is an important part of your application for a research degree. Use it to explain your personal and academic goals in undertaking an extended period of research, and reﬂect on the contribution you will make to the development of new knowledge, ideas and solutions. Also comment on how your research interests fit with the academic focus and expertise at Essex  Your research proposal needs to demonstrate that you have, or are able to develop, the competencies and skills needed to complete your project, within the time and resources available. The quality of your writing is important and a good research proposal may be rejected if it is poorly expressed or badly presented. Many of our departments, schools and centres offer more detailed guidance on preparing a research proposal on their web pages. If you are applying for funding, ensure your proposal fulfils the requirements of your preferred funding body. Your research proposal should include: a working title and key words a summary of the aims and objectives of your research an outline of the ways you meet these aims and objectives, referring to research methods and specific resources you use evidence of your awareness of relevant literature and theoretical approaches an overview of the expected outcomes and the original contribution your research will make to existing bodies of knowledge a brief statement on how your research interests tie in with those found in the department, school or centrePersonal statement If you are applying for a taught course and you need a Tier 4 student visa to study in the UK, then a personal statement (no more than 500 words) is required at the time you make your application, and this should refer specifically to your reasons for wishing to study in the UK, and why you have chosen your area of study. Please remember to include details of any relevant work experience, why you think your academic strengths are suited to your area of study, and how this study will assist you to realise your career objectives. References We require two references from you at the application stage.References should be recent and verifiable, on official institution paper, signed and dated by the referee. If a referee wishes to provide an email reference, it must be sent from an official email account (for example, not Yahoo, Gmail or Hotmail).<\p>"

        #25.career_en
        career_en = response.xpath("//*[contains(text(),'Your future')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #26.assessment_en
        assessment_en_1= response.xpath("//*[contains(text(),'Teaching')]//following-sibling::*").extract()
        assessment_en_1 = ''.join(assessment_en_1)
        assessment_en_1 = remove_class(assessment_en_1)
        assessment_en_2 = response.xpath("//*[contains(text(),'Assessment')]//following-sibling::*").extract()
        assessment_en_2 = ''.join(assessment_en_2)
        assessment_en_2 = remove_class(assessment_en_2)
        assessment_en_3 = response.xpath("//*[contains(text(),'Dissertation')]//following-sibling::*").extract()
        assessment_en_3 = ''.join(assessment_en_3)
        assessment_en_3 = remove_class(assessment_en_3)
        assessment_en = assessment_en_1 + assessment_en_2 +assessment_en_3
        if len(assessment_en)>30000:
            assessment_en = assessment_en[:30000]
        # print(assessment_en)

        item['apply_documents_en'] = apply_documents_en
        item['require_chinese_en'] = require_chinese_en
        item['rntry_requirements'] = rntry_requirements
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['start_date'] = start_date
        item['teach_time'] = teach_time
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['location'] = location
        item['department'] = department
        item['overview_en'] = overview_en
        item['ielts'] = ielts
        item['ielts_w'] = ielts_w
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['modules_en'] = modules_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_proces_en'] = apply_proces_en
        item['career_en'] = career_en
        item['assessment_en'] = assessment_en
        yield item