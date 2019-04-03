# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import *
from scrapySchool_Canada_Ben.items import *
import requests
from lxml import etree
class UniversityofwindsorSpider(scrapy.Spider):
    name = 'UniversityofWindsor'
    # allowed_domains = ['a.b']

    #学费  http://web2.uwindsor.ca/finance/fee-estimator/
    #//b[contains(text(),"Total")]/../following-sibling::td/text()
    # 1   http://www.uwindsor.ca/studentrecruitment/sites/uwindsor.ca.studentrecruitment/files/8721_programflyer_hk_lq.pdf
    #192个专业 180 178  166
    # def parses(self, response):
        #初始版本获取连接
        # urllist=response.xpath('//h2[contains(text(),"Program Listing")]/following-sibling::ul/li/a/@href').extract()
        # for ur in urllist:
        #     yield scrapy.Request(callback=self.parses,url='http://www.uwindsor.ca'+ur)
        #第二次补链接
        # majorUrlList = response.xpath('//h1/following-sibling::div[1]//p/a/@href').extract()
        # divT=response.xpath('//div[text()="DEGREE RELATED LINKS"]/text()').extract()
        # if divT==[]:
        #     for majorUrl in majorUrlList:
        #         print(majorUrl)
        # else:
        #     print(response.url)
    start_urls = [
        'http://www.uwindsor.ca/studentrecruitment/330/biology',
        'http://www.uwindsor.ca/studentrecruitment/331/biology-and-biochemistry-health-and-biomedical-sciences-stream',
        'http://www.uwindsor.ca/studentrecruitment/328/behaviour-cognition-and-neuroscience',
        'http://www.uwindsor.ca/studentrecruitment/396/molecular-biology-and-biotechnology',
        'http://www.uwindsor.ca/studentrecruitment/322/business-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/333/business-administration-honours-and-computer-science-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/335/business-administration-honours-and-economics',
        'http://www.uwindsor.ca/studentrecruitment/329/biochemistry',
        'http://www.uwindsor.ca/studentrecruitment/336/chemistry',
        'http://www.uwindsor.ca/studentrecruitment/337/chemistry-and-physics',
        'http://www.uwindsor.ca/studentrecruitment/340/communication-media-and-film',
        'http://www.uwindsor.ca/studentrecruitment/515/communication-media-film-and-education-5-year-concurrent-general-bachelor-arts-communication',
        'http://www.uwindsor.ca/studentrecruitment/563/communication-media-and-filmphilosophy',
        'http://www.uwindsor.ca/studentrecruitment/564/communication-media-and-filmpolitical-science',
        'http://www.uwindsor.ca/studentrecruitment/565/communication-media-and-filmpsychology',
        'http://www.uwindsor.ca/studentrecruitment/566/communication-media-and-filmcreative-writing',
        'http://www.uwindsor.ca/studentrecruitment/567/communication-media-and-filmenglish',
        'http://www.uwindsor.ca/studentrecruitment/351/drama-and-communication-media-and-film',
        'http://www.uwindsor.ca/studentrecruitment/412/visual-arts-and-communication-media-and-film',
        'http://www.uwindsor.ca/studentrecruitment/343/computer-science-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/341/computer-information-systems-honours-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/342/computer-science-honours-applied-computing-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/344/computer-science-software-engineering-specialization-honours-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/345/criminology-honours',
        'http://www.uwindsor.ca/studentrecruitment/568/criminologyfamily-and-social-relations',
        'http://www.uwindsor.ca/studentrecruitment/569/criminologypolitical-science',
        'http://www.uwindsor.ca/studentrecruitment/570/criminologywomen%E2%80%99s-studies',
        'http://www.uwindsor.ca/studentrecruitment/349/disability-studies',
        'http://www.uwindsor.ca/studentrecruitment/350/disability-studies-and-psychology',
        'http://www.uwindsor.ca/studentrecruitment/354/dramatic-art',
        'http://www.uwindsor.ca/studentrecruitment/575/drama-english-literature-and-creative-writing',
        'http://www.uwindsor.ca/studentrecruitment/576/drama-french',
        'http://www.uwindsor.ca/studentrecruitment/351/drama-and-communication-media-and-film',
        'http://www.uwindsor.ca/studentrecruitment/577/drama-education-and-community-ba-honours',
        'http://www.uwindsor.ca/studentrecruitment/356/education-consecutive-program-candidates-existing-degree',
        'http://www.uwindsor.ca/studentrecruitment/524/concurrent-programs',
        'http://www.uwindsor.ca/studentrecruitment/362/english-literature-and-creative-writing',
        'http://www.uwindsor.ca/studentrecruitment/579/english-drama',
        'http://www.uwindsor.ca/studentrecruitment/580/english-french',
        'http://www.uwindsor.ca/studentrecruitment/581/english-philosophy',
        'http://www.uwindsor.ca/studentrecruitment/582/english-political-science',
        'http://www.uwindsor.ca/studentrecruitment/583/english-psychology',
        'http://www.uwindsor.ca/studentrecruitment/360/english-and-education-5-year-concurrent-general-bachelor-arts-english-language-and-literature',
        'http://www.uwindsor.ca/studentrecruitment/339/civil-engineering-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/357/electrical-engineering-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/358/engineering-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/363/environmental-engineering-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/359/engineering-technology',
        'http://www.uwindsor.ca/studentrecruitment/376/industrial-engineering-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/377/industrial-engineering-minor-business-administration-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/391/mechanical-engineering-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/325/mechanical-engineering-aerospace-option-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/327/mechanical-engineering-automotive-engineering-option-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/393/mechanical-engineering-environmental-engineering-option-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/392/mechanical-engineering-materials-option-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/364/environmental-science',
        'http://www.uwindsor.ca/studentrecruitment/365/environmental-studies',
        'http://www.uwindsor.ca/studentrecruitment/367/forensic-science',
        'http://www.uwindsor.ca/studentrecruitment/368/forensics-combined-degree-arts-humanities-and-social-sciences',
        'http://www.uwindsor.ca/studentrecruitment/369/french-studies',
        'http://www.uwindsor.ca/studentrecruitment/584/french-history',
        'http://www.uwindsor.ca/studentrecruitment/585/french-modern-languages-italian',
        'http://www.uwindsor.ca/studentrecruitment/586/french-modern-languages-spanish',
        'http://www.uwindsor.ca/studentrecruitment/403/political-science-bilingual-specialization',
        'http://www.uwindsor.ca/studentrecruitment/370/french-studies-and-education-5-year-concurrent-general-bachelor-arts-french-and-bachelor',
        'http://www.uwindsor.ca/studentrecruitment/374/history',
        'http://www.uwindsor.ca/studentrecruitment/588/history-creative-writing',
        'http://www.uwindsor.ca/studentrecruitment/589/history-english',
        'http://www.uwindsor.ca/studentrecruitment/590/history-greek-and-roman-studies',
        'http://www.uwindsor.ca/studentrecruitment/591/history-political-science',
        'http://www.uwindsor.ca/studentrecruitment/592/historycriminology',
        'http://www.uwindsor.ca/studentrecruitment/593/historymusic',
        'http://www.uwindsor.ca/studentrecruitment/375/history-and-education-5-year-concurrent-general-bachelor-arts-historybachelor-education',
        'http://www.uwindsor.ca/studentrecruitment/381/law-canadian-american-dual-jd-program',
        'http://www.uwindsor.ca/studentrecruitment/382/law-integrated-mbajd-program',
        'http://www.uwindsor.ca/studentrecruitment/383/law-juris-doctor-jd',
        'http://www.uwindsor.ca/studentrecruitment/384/law-mswjd-joint-degree-program',
        'http://www.uwindsor.ca/studentrecruitment/385/liberal-arts-and-professional-studies',
        'http://www.uwindsor.ca/studentrecruitment/470/aeronautics',
        'http://www.uwindsor.ca/studentrecruitment/386/mathematics-general-and-honours',
        'http://www.uwindsor.ca/studentrecruitment/594/mathematics-and-computer-science-bmath-honours',
        'http://www.uwindsor.ca/studentrecruitment/388/mathematics-and-education-5-year-concurrent-general-bachelor-mathematics-and-bachelor-education',
        'http://www.uwindsor.ca/studentrecruitment/680/concurrent-honours-modern-languages-second-language-education-intercultural-streambachelor',
        'http://www.uwindsor.ca/studentrecruitment/476/german-language-and-culture',
        'http://www.uwindsor.ca/studentrecruitment/478/italian-language-and-culture',
        'http://www.uwindsor.ca/studentrecruitment/463/modern-languages-optional-year-abroad',
        'http://www.uwindsor.ca/studentrecruitment/480/spanish-language-and-culture',
        'http://www.uwindsor.ca/studentrecruitment/397/music-honours-bachelor-arts',
        'http://www.uwindsor.ca/studentrecruitment/398/music-honours-bachelor-music',
        'http://www.uwindsor.ca/studentrecruitment/595/musiccommunications-media-film',
        'http://www.uwindsor.ca/studentrecruitment/596/musiccreative-writing',
        'http://www.uwindsor.ca/studentrecruitment/597/musicenglish',
        'http://www.uwindsor.ca/studentrecruitment/598/musicfrench',
        'http://www.uwindsor.ca/studentrecruitment/599/musicpsychology',
        'http://www.uwindsor.ca/studentrecruitment/429/music-and-education-5-year-concurrent-honours-bachelor-music-music-education-and-bachelor',
        'http://www.uwindsor.ca/studentrecruitment/400/philosophy',
        'http://www.uwindsor.ca/studentrecruitment/600/philosophycriminology',
        'http://www.uwindsor.ca/studentrecruitment/485/medical-physics-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/483/physics-honours',
        'http://www.uwindsor.ca/studentrecruitment/484/physics-and-high-technology-honours-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/402/political-science',
        'http://www.uwindsor.ca/studentrecruitment/403/political-science-bilingual-specialization',
        'http://www.uwindsor.ca/studentrecruitment/404/political-science-law-and-politics-specialization',
        'http://www.uwindsor.ca/studentrecruitment/338/child-psychology',
        'http://www.uwindsor.ca/studentrecruitment/346/developmental-psychology-honours',
        'http://www.uwindsor.ca/studentrecruitment/572/developmental-psychologysociology',
        'http://www.uwindsor.ca/studentrecruitment/573/developmental-psychologycriminology',
        'http://www.uwindsor.ca/studentrecruitment/574/developmental-psychologyfamily-social-relations',
        'http://www.uwindsor.ca/studentrecruitment/350/disability-studies-and-psychology',
        'http://www.uwindsor.ca/studentrecruitment/405/psychology',
        'http://www.uwindsor.ca/studentrecruitment/602/psychologycriminology',
        'http://www.uwindsor.ca/studentrecruitment/603/psychology-creative-writing',
        'http://www.uwindsor.ca/studentrecruitment/604/psychologysociology',
        'http://www.uwindsor.ca/studentrecruitment/605/psychologyvisual-arts',
        'http://www.uwindsor.ca/studentrecruitment/606/psychologywomen%E2%80%99s-and-gender-studies',
        'http://www.uwindsor.ca/studentrecruitment/406/psychology-education-and-early-childhood-education-5-year-concurrent-general-bachelor-arts',
        'http://www.uwindsor.ca/studentrecruitment/371/general-science',
        'http://www.uwindsor.ca/studentrecruitment/418/general-science-and-education-5-year-concurrent-general-bachelor-science-general-science-and',
        'http://www.uwindsor.ca/studentrecruitment/407/social-work',
        'http://www.uwindsor.ca/studentrecruitment/408/social-work-and-disability-studies',
        'http://www.uwindsor.ca/studentrecruitment/409/social-work-and-womens-studies',
        'http://www.uwindsor.ca/studentrecruitment/410/sociology',
        'http://www.uwindsor.ca/studentrecruitment/607/sociologycommunication-media-film',
        'http://www.uwindsor.ca/studentrecruitment/608/sociologywomen%E2%80%99s-and-gender-studies',
        'http://www.uwindsor.ca/studentrecruitment/394/media-art-histories-and-visual-culture',
        'http://www.uwindsor.ca/studentrecruitment/326/visual-arts',
        'http://www.uwindsor.ca/studentrecruitment/332/visual-arts-and-built-environment',
        'http://www.uwindsor.ca/studentrecruitment/412/visual-arts-and-communication-media-and-film',
        'http://www.uwindsor.ca/studentrecruitment/610/visual-artsmusic',
        'http://www.uwindsor.ca/studentrecruitment/413/visual-arts-and-education-5-year-concurrent-general-bachelor-arts-visual-arts-and-bachelor',
        'http://www.uwindsor.ca/studentrecruitment/409/social-work-and-womens-studies',
        'http://www.uwindsor.ca/studentrecruitment/414/womens-and-gender-studies',
        'http://www.uwindsor.ca/studentrecruitment/323/acting',
        'http://www.uwindsor.ca/studentrecruitment/470/aeronautics',
        'http://www.uwindsor.ca/studentrecruitment/378/interdisciplinary-arts-and-science',
        'http://www.uwindsor.ca/studentrecruitment/328/behaviour-cognition-and-neuroscience',
        'http://www.uwindsor.ca/studentrecruitment/621/business-administration-honours-and-mathematics-optional-thesis',
        'http://www.uwindsor.ca/studentrecruitment/622/business-administration-honours-and-psychology-optional-thesis',
        'https://www.uwindsor.ca/studentrecruitment/627/sociology-and-criminology',
        'https://www.uwindsor.ca/studentrecruitment/408/social-work-and-disability-studies',
        'https://www.uwindsor.ca/studentrecruitment/352/drama-and-education-5-year-concurrent-general-bachelor-arts-drama-and-bachelor-education',
        'http://www.uwindsor.ca/studentrecruitment/355/economics',
        'https://www.uwindsor.ca/studentrecruitment/361/english-language-and-literature',
        'http://www.uwindsor.ca/studentrecruitment/366/family-and-social-relations',
        'http://www.uwindsor.ca/studentrecruitment/373/greek-and-roman-studies',
        'http://www.uwindsor.ca/studentrecruitment/379/international-relations-and-development-studies',
        'http://www.uwindsor.ca/studentrecruitment/380/kinesiology-optional-co-op',
        'http://www.uwindsor.ca/studentrecruitment/623/mathematics-and-statistics',
        'http://www.uwindsor.ca/studentrecruitment/621/business-administration-honours-and-mathematics-optional-thesis',
        'http://www.uwindsor.ca/studentrecruitment/624/combined-honours-mathematics',
        'http://www.uwindsor.ca/studentrecruitment/625/mathematics-finance-concentration',
        'http://www.uwindsor.ca/studentrecruitment/399/nursing',
        'http://www.uwindsor.ca/studentrecruitment/622/business-administration-honours-and-psychology-optional-thesis',
        'https://www.uwindsor.ca/studentrecruitment/627/sociology-and-criminology',
        'http://www.uwindsor.ca/studentrecruitment/411/undeclared-first-year',
        'http://www.uwindsor.ca/studentrecruitment/332/visual-arts-and-built-environment', ]
    def parse(self, response):
        item=get_item(ScrapyschoolCanadaBenItem)
        item['school_name']='University of Windsor'
        item['url']=response.url
        item['start_date']='2019-1,2019-9'
        item['deadline']='一月开学:上年九月,九月开学:本年三月'
        #中国学生要求
        item['require_chinese_en']='<p>Senior High School Graduation Diploma and Chinese University Entrance Examination (NCEE / Gao Kao) if available</p>'
        item['ielts']='6.5'
        item['toefl']='83'
        item['toefl_l'],item['toefl_s'],item['toefl_r'],item['toefl_w']='20','20','20','20'
        item['toefl_code']='0904'
        item['sat_code']='0904'
        # item['sat1_code']='<p>In addition, applicants are encouraged to submit SAT or ACT scores to supplement their application for admission.Where class rankings are reported on the transcript, a ranking in the top third is preferred. The University of Windsor has an official code to use when you submit your SAT scores (0904) and your ACT scores (7053).</p>'
        item['act_code']='7053'
        item['ib']='Applicants who have completed the International Baccalaureate Diploma with a minimum overall score of 24, and passes in a minimum of 6 subjects including at least three courses at the Higher Level will be considered for admission to the University of Windsor. Applicants who are also completing a provincial or national high school program have the option of being considered for admission on the basis of the high school program. Applicants whose native language is not English will be required to demonstrate proficiency in English subject to University of Windsor policy. '
        item['alevel']='Five Passes on the General Certificate of Education including two at the Advanced or, four passes on the General Certificate of Education, including three at the Advanced Level. Two Advanced Supplementary (AS) Level courses may be substituted for an Advanced Level Course. Applicants who receive a “C” grade in final GCE Advanced level examinations will be considered for transfer credit for those courses that have been assessed as equivalent to specified or unspecified University of Windsor courses and are relevant to the student’s academic program. No transfer credit will be granted for Advanced Subsidiary level examinations. (Maximum credit 6 semester courses) Science must include Advanced Level Mathematics, Physics and Chemistry. Engineering must include Advanced Level Mathematics, Physics and Chemistry. Nursing must include Advanced Level English, Biology and Chemistry. Commerce must include Advanced Level Mathematics.'
        modulesUrl=response.xpath('//strong[contains(text(),"Course Descriptions")]/../@href').extract()
        print('课程链接',modulesUrl,response.url)
        if modulesUrl!=[]:
            modRes=requests.get(modulesUrl[0]).content
            modRes=etree.HTML(modRes)
            modules=modRes.xpath('//b/font[@size="2"]')
            mod=[]
            for mods in modules:
                mod+=etree.tostring(mods,method='html',encoding='unicode')
            item['modules_en']=remove_class(mod).replace('<font>','<p>').replace('</font>','</p>')
        major_name=response.xpath('//h1/text()').extract()
        item['major_name_en']=remove_class(major_name)
        # print(major_name)
        degree_name=response.xpath('//div[@class="headcontentHolder"][1]//text()').extract()
        if degree_name!=[]:
            degree_name=degree_name[0].split(' in ')[0]
            item['degree_name']=degree_name
        department=response.xpath('//strong[contains(text(),"Faculty")]/../text()').extract()
        item['department']=remove_class(department)
        overview=response.xpath('//div[contains(text(),"ADMISSION")]/../preceding-sibling::div[@class="progInfo"]').extract()
        if overview==[]:
            overview=response.xpath('//div[@class="headcontentHolder"]/following-sibling::ul[1]').extract()
        overview=remove_class(overview)
        item['degree_overview_en']=overview
        enrty_requirement_en=response.xpath('//div[contains(text(),"ADMISSION")]/following-sibling::*').extract()
        enrty_requirement_en=remove_class(enrty_requirement_en)
        career=response.xpath('//div[contains(text(),"CAREER TRACKS")]/following-sibling::*').extract()
        career=remove_class(career)
        item['career_en']=career
        # print(enrty_requirement_en)
        item['entry_requirements_en']=enrty_requirement_en
        average_score=re.findall('\d+\%',enrty_requirement_en)
        # print(average_score)
        # item['average_score']=','.join(average_score)
        if average_score!=[]:
            item['average_score']=average_score[0]
        yield item


        # elif len(majorUrlList)>1:
        #     for url in majorUrlList:
        #         if url[0] != 'h':
        #             url='http://www.uwindsor.ca'+url
        #         else:
        #             url=url
                # print('通过自身访问专业链接')
                # yield scrapy.Request(callback=self.parses,url=url)
