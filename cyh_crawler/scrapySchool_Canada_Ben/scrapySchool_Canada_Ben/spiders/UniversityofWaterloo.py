# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.getItem import *
from scrapySchool_Canada_Ben.items import *
import requests
from lxml import etree

class UniversityofwaterlooSpider(scrapy.Spider):
    name = 'UniversityofWaterloo'
    # allowed_domains = ['a.b']
    # start_urls = ['https://uwaterloo.ca/future-students/programs-faculty']
    #学费 https://uwaterloo.ca/future-students/financing/tuition
    #AP IB Alevel https://uwaterloo.ca/future-students/admissions/admission-requirements
    #雅思托福90 overall 25 writing, 25 speaking  6.5 overall 6.5 writing, 6.5 speaking, 6.0 reading, 6.0 listening
    #高考 Chinese National University Entrance Examination (Gao Kao) results provided by the China Qualifications Verification (CQV). We expect a minimum provincial Tier 1 (or equivalent) university cut-off score.
    #截至日期 https://uwaterloo.ca/future-students/admissions/application-deadlines
    #起始页 https://uwaterloo.ca/future-students/programs/biology
    #入学要求  https://uwaterloo.ca/future-students/admissions/admission-requirements/%s/international-system/chinese-system/
    #AP https://uwaterloo.ca/future-students/admissions/admission-requirements/%s/international-system/american-system/
    start_urls=['https://uwaterloo.ca/future-students/programs/geography-and-environmental-management',
'https://uwaterloo.ca/future-students/programs/geography-and-aviation',
'https://uwaterloo.ca/future-students/programs/planning',
'https://uwaterloo.ca/future-students/programs/geomatics',
'https://uwaterloo.ca/future-students/programs/knowledge-integration',
'https://uwaterloo.ca/future-students/programs/computer-science',
'https://uwaterloo.ca/future-students/programs/international-development',
'https://uwaterloo.ca/future-students/programs/architecture',
'https://uwaterloo.ca/future-students/programs/electrical-engineering',
'https://uwaterloo.ca/future-students/programs/computer-engineering',
'https://uwaterloo.ca/future-students/programs/biomedical-engineering',
'https://uwaterloo.ca/future-students/programs/civil-engineering',
'https://uwaterloo.ca/future-students/programs/environmental-engineering',
'https://uwaterloo.ca/future-students/programs/chemical-engineering',
'https://uwaterloo.ca/future-students/programs/sociology',
'https://uwaterloo.ca/future-students/programs/geological-engineering',
'https://uwaterloo.ca/future-students/programs/architectural-engineering',
'https://uwaterloo.ca/future-students/programs/theatre-performance',
'https://uwaterloo.ca/future-students/programs/spanish',
'https://uwaterloo.ca/future-students/programs/speech-communication',
'https://uwaterloo.ca/future-students/programs/economics',
'https://uwaterloo.ca/future-students/programs/tourism-development',
'https://uwaterloo.ca/future-students/programs/therapeutic-recreation',
'https://uwaterloo.ca/future-students/programs/kinesiology',
'https://uwaterloo.ca/future-students/programs/public-health',
'https://uwaterloo.ca/future-students/programs/accounting-and-financial-management',
'https://uwaterloo.ca/future-students/programs/fine-arts',
'https://uwaterloo.ca/future-students/programs/systems-design-engineering',
'https://uwaterloo.ca/future-students/programs/recreation-and-leisure-studies',
'https://uwaterloo.ca/future-students/programs/recreation-and-sport-business',
'https://uwaterloo.ca/future-students/programs/mechatronics-engineering',
'https://uwaterloo.ca/future-students/programs/mathematics-business-administration',
'https://uwaterloo.ca/future-students/programs/environment-and-business',
'https://uwaterloo.ca/future-students/programs/nanotechnology-engineering',
'https://uwaterloo.ca/future-students/programs/mathematics',
'https://uwaterloo.ca/future-students/programs/environment-resources-and-sustainability',
'https://uwaterloo.ca/future-students/programs/financial-analysis-and-risk-management',
'https://uwaterloo.ca/future-students/programs/software-engineering',
'https://uwaterloo.ca/future-students/programs/management-engineering',
'https://uwaterloo.ca/future-students/programs/life-sciences',
'https://uwaterloo.ca/future-students/programs/biotechnology-economics',
'https://uwaterloo.ca/future-students/programs/biomedical-sciences',
'https://uwaterloo.ca/future-students/programs/global-business-and-digital-arts',
'https://uwaterloo.ca/future-students/programs/arts-and-business',
'https://uwaterloo.ca/future-students/programs/psychology-science',
'https://uwaterloo.ca/future-students/programs/history',
'https://uwaterloo.ca/future-students/programs/gender-and-social-justice',
'https://uwaterloo.ca/future-students/programs/environmental-science',
'https://uwaterloo.ca/future-students/programs/biology',
'https://uwaterloo.ca/future-students/programs/honours-science',
'https://uwaterloo.ca/future-students/programs/mathematics-accounting',
'https://uwaterloo.ca/future-students/programs/anthropology',
'https://uwaterloo.ca/future-students/programs/french',
'https://uwaterloo.ca/future-students/programs/sexuality-marriage-and-family-studies',
'https://uwaterloo.ca/future-students/programs/social-development-studies',
'https://uwaterloo.ca/future-students/programs/computing-and-financial-management',
'https://uwaterloo.ca/future-students/programs/classical-studies',
'https://uwaterloo.ca/future-students/programs/german',
'https://uwaterloo.ca/future-students/programs/honours-arts',
'https://uwaterloo.ca/future-students/programs/applied-mathematics',
'https://uwaterloo.ca/future-students/programs/information-technology-management',
'https://uwaterloo.ca/future-students/programs/biochemistry',
'https://uwaterloo.ca/future-students/programs/actuarial-science',
'https://uwaterloo.ca/future-students/programs/mechanical-engineering',
'https://uwaterloo.ca/future-students/programs/english',
'https://uwaterloo.ca/future-students/programs/data-science',
'https://uwaterloo.ca/future-students/programs/religious-studies',
'https://uwaterloo.ca/future-students/programs/health-studies',
'https://uwaterloo.ca/future-students/programs/legal-studies',
'https://uwaterloo.ca/future-students/programs/music',
'https://uwaterloo.ca/future-students/programs/liberal-studies',
'https://uwaterloo.ca/future-students/programs/political-science',
'https://uwaterloo.ca/future-students/programs/peace-and-conflict-studies',
'https://uwaterloo.ca/future-students/programs/philosophy',
'https://uwaterloo.ca/future-students/programs/medieval-studies',
'https://uwaterloo.ca/future-students/programs/psychology-arts',
'https://uwaterloo.ca/future-students/programs/physics',
'https://uwaterloo.ca/future-students/programs/physics-and-astronomy',
'https://uwaterloo.ca/future-students/programs/materials-and-nanosciences',
'https://uwaterloo.ca/future-students/programs/physical-sciences',
'https://uwaterloo.ca/future-students/programs/chemistry',
'https://uwaterloo.ca/future-students/programs/medicinal-chemistry',
'https://uwaterloo.ca/future-students/programs/earth-sciences',
'https://uwaterloo.ca/future-students/programs/science-and-business',
'https://uwaterloo.ca/future-students/programs/life-physics',
'https://uwaterloo.ca/future-students/programs/science-and-aviation',
'https://uwaterloo.ca/future-students/programs/mathematical-economics',
'https://uwaterloo.ca/future-students/programs/mathematical-optimization',
'https://uwaterloo.ca/future-students/programs/statistics',
'https://uwaterloo.ca/future-students/programs/mathematical-finance',
'https://uwaterloo.ca/future-students/programs/mathematical-physics',
'https://uwaterloo.ca/future-students/programs/pure-mathematics',
'https://uwaterloo.ca/future-students/programs/computational-mathematics',
'https://uwaterloo.ca/future-students/programs/biotechnology-accounting',
'https://uwaterloo.ca/future-students/programs/waterloo-math-teaching',
'https://uwaterloo.ca/future-students/programs/combinatorics-and-optimization',
'https://uwaterloo.ca/future-students/programs/biostatistics',]
    #根据链接补抓某个字段
    def parses(self, response):
        item=get_item(ScrapyschoolCanadaBenItem)
        item['url']=response.url
        print(response.url)
        item['school_name'] = 'University of Waterloo'
        ag=response.xpath('//*[contains(text(),"average")]//text()').extract()
        ags=re.findall('\d{2}s',''.join(ag))
        # print(ags)
        if len(ags)==2:
            item['average_score']=ags[1].replace('s','')
        if len(ags)==1:
            item['average_score']=''.join(ags).replace('s','')
        yield item
    #正式起点

    def parsess(self, response):
        modulesResDicts = {}
        for mo in ['http://ugradcalendar.uwaterloo.ca/courses/AFM/',
        'http://ugradcalendar.uwaterloo.ca/courses/ACTSC/',
        'http://ugradcalendar.uwaterloo.ca/courses/ANTH/',
        'http://ugradcalendar.uwaterloo.ca/courses/AHS/',
        'http://ugradcalendar.uwaterloo.ca/courses/APPLS/',
        'http://ugradcalendar.uwaterloo.ca/courses/AMATH/',
        'http://ugradcalendar.uwaterloo.ca/courses/ARCH/',
        'http://ugradcalendar.uwaterloo.ca/courses/AE/',
        'http://ugradcalendar.uwaterloo.ca/courses/ARTS/',
        'http://ugradcalendar.uwaterloo.ca/courses/ARBUS/',
        'http://ugradcalendar.uwaterloo.ca/courses/AVIA/',
        'http://ugradcalendar.uwaterloo.ca/courses/BIOL/',
        'http://ugradcalendar.uwaterloo.ca/courses/BME/',
        'http://ugradcalendar.uwaterloo.ca/courses/BET/',
        'http://ugradcalendar.uwaterloo.ca/courses/CDNST/',
        'http://ugradcalendar.uwaterloo.ca/courses/CHE/',
        'http://ugradcalendar.uwaterloo.ca/courses/CHEM/',
        'http://ugradcalendar.uwaterloo.ca/courses/CHINA/',
        'http://ugradcalendar.uwaterloo.ca/courses/CMW/',
        'http://ugradcalendar.uwaterloo.ca/courses/CIVE/',
        'http://ugradcalendar.uwaterloo.ca/courses/CLAS/',
        'http://ugradcalendar.uwaterloo.ca/courses/CO/',
        'http://ugradcalendar.uwaterloo.ca/courses/COMM/',
        'http://ugradcalendar.uwaterloo.ca/courses/CS/',
        'http://ugradcalendar.uwaterloo.ca/courses/CROAT/',
        'http://ugradcalendar.uwaterloo.ca/courses/CI/',
        'http://ugradcalendar.uwaterloo.ca/courses/DAC/',
        'http://ugradcalendar.uwaterloo.ca/courses/DRAMA/',
        'http://ugradcalendar.uwaterloo.ca/courses/DUTCH/',
        'http://ugradcalendar.uwaterloo.ca/courses/EARTH/',
        'http://ugradcalendar.uwaterloo.ca/courses/EASIA/',
        'http://ugradcalendar.uwaterloo.ca/courses/ECON/',
        'https://ugradcalendar.uwaterloo.ca/courses/ECE/',
        'https://ugradcalendar.uwaterloo.ca/courses/ENGL/',
        'https://ugradcalendar.uwaterloo.ca/courses/ENBUS/',
        'http://ugradcalendar.uwaterloo.ca/courses/ERS/',
        'https://ugradcalendar.uwaterloo.ca/courses/ENVE/',
        'https://ugradcalendar.uwaterloo.ca/courses/ENVS/',
        'https://ugradcalendar.uwaterloo.ca/courses/FINE/',
        'https://ugradcalendar.uwaterloo.ca/courses/FR/',
        'https://ugradcalendar.uwaterloo.ca/courses/GENE/',
        'http://ugradcalendar.uwaterloo.ca/courses/GEOG/',
        'https://ugradcalendar.uwaterloo.ca/courses/GEOE/',
        'http://ugradcalendar.uwaterloo.ca/courses/GER/',
        'https://ugradcalendar.uwaterloo.ca/courses/GERON/',
        'https://ugradcalendar.uwaterloo.ca/courses/GBDA/',
        'https://ugradcalendar.uwaterloo.ca/courses/GRK/',
        'https://ugradcalendar.uwaterloo.ca/courses/HLTH/',
        'https://ugradcalendar.uwaterloo.ca/courses/HIST/',
        'https://ugradcalendar.uwaterloo.ca/courses/HRM/',
        'https://ugradcalendar.uwaterloo.ca/courses/HUMSC/',
        'http://ugradcalendar.uwaterloo.ca/courses/INDG/',
        'https://ugradcalendar.uwaterloo.ca/courses/INDEV/',
        'https://ugradcalendar.uwaterloo.ca/courses/INTST/',
        'https://ugradcalendar.uwaterloo.ca/courses/ITAL/',
        'https://ugradcalendar.uwaterloo.ca/courses/ITALST/',
        'https://ugradcalendar.uwaterloo.ca/courses/JAPAN/',
        'https://ugradcalendar.uwaterloo.ca/courses/JS/',
        'https://ugradcalendar.uwaterloo.ca/courses/KIN/',
        'https://ugradcalendar.uwaterloo.ca/courses/INTEG/',
        'https://ugradcalendar.uwaterloo.ca/courses/KOREA/',
        'https://ugradcalendar.uwaterloo.ca/courses/LAT/',
        'https://ugradcalendar.uwaterloo.ca/courses/LS/',
        'https://ugradcalendar.uwaterloo.ca/courses/MSCI/',
        'https://ugradcalendar.uwaterloo.ca/courses/MNS/',
        'https://ugradcalendar.uwaterloo.ca/courses/MATH/',
        'https://ugradcalendar.uwaterloo.ca/courses/MTHEL/',
        'https://ugradcalendar.uwaterloo.ca/courses/ME/',
        'https://ugradcalendar.uwaterloo.ca/courses/MTE/',
        'https://ugradcalendar.uwaterloo.ca/courses/MEDVL/',
        'https://ugradcalendar.uwaterloo.ca/courses/MUSIC/',
        'http://ugradcalendar.uwaterloo.ca/courses/NE/',
        'https://ugradcalendar.uwaterloo.ca/courses/PACS/',
        'https://ugradcalendar.uwaterloo.ca/courses/PHIL/',
        'https://ugradcalendar.uwaterloo.ca/courses/PHYS/',
        'https://ugradcalendar.uwaterloo.ca/courses/PLAN/',
        'https://ugradcalendar.uwaterloo.ca/courses/PSCI/',
        'https://ugradcalendar.uwaterloo.ca/courses/PORT/',
        'https://ugradcalendar.uwaterloo.ca/courses/PSYCH/',
        'http://ugradcalendar.uwaterloo.ca/courses/PMATH/',
        'https://ugradcalendar.uwaterloo.ca/courses/REC/',
        'https://ugradcalendar.uwaterloo.ca/courses/RS/',
        'https://ugradcalendar.uwaterloo.ca/courses/RUSS/',
        'https://ugradcalendar.uwaterloo.ca/courses/REES/',
        'https://ugradcalendar.uwaterloo.ca/courses/SCI/',
        'https://ugradcalendar.uwaterloo.ca/courses/SCBUS/',
        'https://ugradcalendar.uwaterloo.ca/courses/SMF/',
        'https://ugradcalendar.uwaterloo.ca/courses/SDS/',
        'https://ugradcalendar.uwaterloo.ca/courses/SOCWK/',
        'https://ugradcalendar.uwaterloo.ca/courses/SWREN/',
        'https://ugradcalendar.uwaterloo.ca/courses/STV/',
        'https://ugradcalendar.uwaterloo.ca/courses/SOC/',
        'https://ugradcalendar.uwaterloo.ca/courses/SE/',
        'https://ugradcalendar.uwaterloo.ca/courses/SPAN/',
        'https://ugradcalendar.uwaterloo.ca/courses/SPCOM/',
        'https://ugradcalendar.uwaterloo.ca/courses/STAT/',
        'https://ugradcalendar.uwaterloo.ca/courses/SI/',
        'https://ugradcalendar.uwaterloo.ca/courses/SYDE/',
        'https://ugradcalendar.uwaterloo.ca/courses/VCULT/',
        'http://ugradcalendar.uwaterloo.ca/courses/WS/',]:
            res=etree.HTML(requests.get(mo).content)
            modulesResDicts[mo]=res
            print('获取所有课程链接返回内容')
        departments=response.xpath('//div[@class="field-item even"]//h2/text()').extract()
        urlsXpath='//h2[contains(text(),"%s")]/following-sibling::div[contains(@class,"col-50")][position()<3]//ul/li/a/@href'
        for dep in departments:
            urlXpath=urlsXpath % dep
            urllist=response.xpath(urlXpath).extract()
            for proUrl in urllist:
                Url='https://uwaterloo.ca'+proUrl
                # print(dep)
                yield scrapy.Request(url=Url,callback=self.parses,meta={'department':dep,'modulesResDicts':modulesResDicts})
            # print('===============================')
    #根据链接补抓数据
    def parses(self,response):
        urlList = ['https://uwaterloo.ca/future-students/programs/german',
                      'https://uwaterloo.ca/future-students/programs/honours-arts',
                      'https://uwaterloo.ca/future-students/programs/english',
                      'https://uwaterloo.ca/future-students/programs/mechanical-engineering',
                      'https://uwaterloo.ca/future-students/programs/applied-mathematics',
                      'https://uwaterloo.ca/future-students/programs/information-technology-management',
                      'https://uwaterloo.ca/future-students/programs/biochemistry',
                      'https://uwaterloo.ca/future-students/programs/data-science',
                      'https://uwaterloo.ca/future-students/programs/actuarial-science', ]
        for uL in urlList:
            depXpath = '//a[@href="%s"]/../../../preceding-sibling::h2[1]/text()' % uL.replace('https://uwaterloo.ca', '')
            department=''.join(response.xpath(depXpath).extract())
            yield scrapy.Request(url=uL,callback=self.parses,meta={'department':department})
    start_urls=['https://uwaterloo.ca/future-students/programs/financial-analysis-and-risk-management']
    def parse(self,response):
        item=get_item(ScrapyschoolCanadaBenItem)
        item['school_name'] = 'University of Waterloo'
        item['url']=response.url
        item['toefl'],item['toefl_w'],item['toefl_s']='90','25','25'
        item['ielts'],item['ielts_w'],item['ielts_s'],item['ielts_r'],item['ielts_l']='6.5','6.5','6.5','6.0','6.0'
        item['gaokao_desc']='<p>Chinese National University Entrance Examination (Gao Kao) results provided by the China Qualifications Verification (CQV). We expect a minimum provincial Tier 1 (or equivalent) university cut-off score.</p>'
        item['deadline'] = '2019-03-29'
        item['apply_fee'] = '200'
        item['apply_pre'] = 'CAD$'
        item['start_date'] = '2019-09'
        item['toefl_code'] = '0996'
        item['sat_code'] = '0996'
        department=response.meta['department']
        # department='Faculty of Mathematics'
        modulesResDicts=response.meta['modulesResDicts']
        if department in ['Faculty of Applied Health Sciences','Faculty of Arts','Faculty of Environment']:
            item['tuition_fee']='30,300 – 31,120'
            item['tuition_fee_pre']='$'
        elif department=='Faculty of Engineering':
            item['tuition_fee'] = '47,970'
            item['tuition_fee_pre'] = '$'
            item['deadline']='2019-02'
        elif department=='Faculty of Mathematics':
            item['tuition_fee'] = '32,820 – 34,900'
            item['tuition_fee_pre'] = '$'
            item['deadline'] = '2019-02'
        elif department=='Faculty of Science':
            item['tuition_fee'] = '31,790 – 32,370'
            item['tuition_fee_pre'] = '$'

        progremme=response.xpath('//h1/text()').extract()
        progremme=''.join(progremme).strip()
        if progremme=='Accounting and Financial Management':
            item['tuition_fee'] = '31,030'
            item['tuition_fee_pre'] = '$'
            item['deadline'] = '2019-02'
        elif progremme=='Architecture':
            item['tuition_fee'] = '45,170'
            item['tuition_fee_pre'] = '$'
            item['deadline'] = '2019-02'
        elif progremme=='Computing and Financial Management':
            item['tuition_fee'] = '33,510'
            item['tuition_fee_pre'] = '$'
        elif progremme=='Global Business and Digital Arts':
            item['tuition_fee'] = '33,400'
            item['tuition_fee_pre'] = '$'
        item['major_name_en']=progremme
        print(response.url)
        # print(progremme)
        # print(department)
        item['department']=department


        allTag=response.xpath('//div[@class="field-item even"]/*').extract()
        oveSplit=response.xpath('//div[@class="field-item even"]/div[@class="col-50 first"][1]').extract()
        if oveSplit!=[]:
            overview=allTag[0:allTag.index(oveSplit[0])]
            overview=remove_class(overview)
            # print(overview)
            item['overview_en']=overview
        degree_name=response.xpath('//img[contains(@alt,"ap")]/../text()').extract()
        # print(degree_name)
        degree_name=' '.join(degree_name).replace('Earn a','').strip()
        degree_name=degree_name.split(' in ')[0].strip()
        # print(degree_name)
        item['degree_name']=degree_name

        rcu=response.url.split('/')[-1]
        require_chinese_url='https://uwaterloo.ca/future-students/admissions/admission-requirements/%s/international-system/chinese-system/' % rcu
        ap_url='https://uwaterloo.ca/future-students/admissions/admission-requirements/%s/international-system/american-system/' % rcu
        ib_url='https://uwaterloo.ca/future-students/admissions/admission-requirements/%s/international-system/ib/' %rcu
        alevel_url='https://uwaterloo.ca/future-students/admissions/admission-requirements/%s/international-system/british-system/' %rcu
        er_url='https://uwaterloo.ca/future-students/admissions/admission-requirements/%s/canada/ontario/' %rcu

        def getAR(url):
            rcuRes = requests.get(url).content
            rcuRes = etree.HTML(rcuRes)
            require_chinese_en = rcuRes.xpath('//div[@id="block-system-main"]')
            require_chinese = []
            for rc in require_chinese_en:
                require_chinese += etree.tostring(rc, method='html', encoding='unicode')
            require_chinese=remove_class(require_chinese)
            return require_chinese
        item['require_chinese_en'] = getAR(require_chinese_url)
        item['ib']=getAR(ib_url)
        item['ap']=getAR(ap_url)
        item['alevel']=getAR(alevel_url)
        # item['average_score']=','.join(re.findall('\d{2}\%',item['require_chinese_en']))
        item['entry_requirements_en']=getAR(er_url)

        # av=response.xpath('//li[contains(text(),"Admission average")]/text()').extract()
        # # print(av)
        # av=''.join(av)
        # if '90' in av:
        #     average_score='90'
        #     item['average_score']=average_score
        # elif '80' in av:
        #     average_score='80'
        #     item['average_score']=average_score

        # modulesUrl = response.xpath('//a[contains(text(),"courses required")]/@href').extract()
        modulesDict={'Architecture': 'http://ugradcalendar.uwaterloo.ca/courses/ARCH/', 'Jewish Studies': 'https://ugradcalendar.uwaterloo.ca/courses/JS/', 'Croatian': 'http://ugradcalendar.uwaterloo.ca/courses/CROAT/', 'Chemistry': 'http://ugradcalendar.uwaterloo.ca/courses/CHEM/', 'General Engineering': 'https://ugradcalendar.uwaterloo.ca/courses/GENE/', 'Arts': 'http://ugradcalendar.uwaterloo.ca/courses/ARTS/', 'Russian': 'https://ugradcalendar.uwaterloo.ca/courses/RUSS/', 'Accounting & Financial Management': 'http://ugradcalendar.uwaterloo.ca/courses/AFM/', 'Italian': 'https://ugradcalendar.uwaterloo.ca/courses/ITAL/', 'Spanish': 'https://ugradcalendar.uwaterloo.ca/courses/SPAN/', 'Peace and Conflict Studies': 'https://ugradcalendar.uwaterloo.ca/courses/PACS/', 'Church Music and Worship': 'http://ugradcalendar.uwaterloo.ca/courses/CMW/', 'Classical Studies': 'http://ugradcalendar.uwaterloo.ca/courses/CLAS/', 'Cultural Identities': 'http://ugradcalendar.uwaterloo.ca/courses/CI/', 'Sociology': 'https://ugradcalendar.uwaterloo.ca/courses/SOC/', 'Geography and Environmental Management': 'http://ugradcalendar.uwaterloo.ca/courses/GEOG/', 'Medieval Studies': 'https://ugradcalendar.uwaterloo.ca/courses/MEDVL/', 'History': 'https://ugradcalendar.uwaterloo.ca/courses/HIST/', 'Systems Design Engineering': 'https://ugradcalendar.uwaterloo.ca/courses/SYDE/', 'Social Work (Social Development Studies)': 'https://ugradcalendar.uwaterloo.ca/courses/SOCWK/', 'Environmental Studies': 'https://ugradcalendar.uwaterloo.ca/courses/ENVS/', 'Knowledge Integration': 'https://ugradcalendar.uwaterloo.ca/courses/INTEG/', 'Legal Studies': 'https://ugradcalendar.uwaterloo.ca/courses/LS/', 'Architectural Engineering': 'http://ugradcalendar.uwaterloo.ca/courses/AE/', 'Environment and Business': 'https://ugradcalendar.uwaterloo.ca/courses/ENBUS/', 'International Studies': 'https://ugradcalendar.uwaterloo.ca/courses/INTST/', 'Arts and Business': 'http://ugradcalendar.uwaterloo.ca/courses/ARBUS/', 'Computer Science': 'http://ugradcalendar.uwaterloo.ca/courses/CS/', 'Japanese': 'https://ugradcalendar.uwaterloo.ca/courses/JAPAN/', 'Software Engineering': 'https://ugradcalendar.uwaterloo.ca/courses/SE/', 'Indigenous Studies': 'http://ugradcalendar.uwaterloo.ca/courses/INDG/', 'Women Studies': 'http://ugradcalendar.uwaterloo.ca/courses/WS/', 'Studies in Islam': 'https://ugradcalendar.uwaterloo.ca/courses/SI/', 'Italian Studies': 'https://ugradcalendar.uwaterloo.ca/courses/ITALST/', 'Commerce\xa0': 'http://ugradcalendar.uwaterloo.ca/courses/COMM/', 'Statistics': 'https://ugradcalendar.uwaterloo.ca/courses/STAT/', 'Mechanical Engineering': 'https://ugradcalendar.uwaterloo.ca/courses/ME/', 'Applied Mathematics': 'http://ugradcalendar.uwaterloo.ca/courses/AMATH/', 'Philosophy': 'https://ugradcalendar.uwaterloo.ca/courses/PHIL/', 'Earth Sciences': 'http://ugradcalendar.uwaterloo.ca/courses/EARTH/', 'Environmental Engineering': 'https://ugradcalendar.uwaterloo.ca/courses/ENVE/', 'Chinese': 'http://ugradcalendar.uwaterloo.ca/courses/CHINA/', 'Digital Arts Communication': 'http://ugradcalendar.uwaterloo.ca/courses/DAC/', 'Mathematics Electives': 'https://ugradcalendar.uwaterloo.ca/courses/MTHEL/', 'Nanotechnology Engineering': 'http://ugradcalendar.uwaterloo.ca/courses/NE/', 'Economics': 'http://ugradcalendar.uwaterloo.ca/courses/ECON/', 'French': 'https://ugradcalendar.uwaterloo.ca/courses/FR/', 'Management Sciences': 'https://ugradcalendar.uwaterloo.ca/courses/MSCI/', 'Human Resources Management': 'https://ugradcalendar.uwaterloo.ca/courses/HRM/', 'Visual Culture': 'https://ugradcalendar.uwaterloo.ca/courses/VCULT/', 'Aviation': 'http://ugradcalendar.uwaterloo.ca/courses/AVIA/', 'Health': 'https://ugradcalendar.uwaterloo.ca/courses/HLTH/', 'Canadian Studies': 'http://ugradcalendar.uwaterloo.ca/courses/CDNST/', 'Business, Entrepreneurship and Technology': 'http://ugradcalendar.uwaterloo.ca/courses/BET/', 'Sexuality, Marriage, and Family Studies': 'https://ugradcalendar.uwaterloo.ca/courses/SMF/', 'Mathematics': 'https://ugradcalendar.uwaterloo.ca/courses/MATH/', 'International Development': 'https://ugradcalendar.uwaterloo.ca/courses/INDEV/', 'Civil Engineering': 'http://ugradcalendar.uwaterloo.ca/courses/CIVE/', 'Science and Business': 'https://ugradcalendar.uwaterloo.ca/courses/SCBUS/', 'Anthropology': 'http://ugradcalendar.uwaterloo.ca/courses/ANTH/', 'Biomedical Engineering': 'http://ugradcalendar.uwaterloo.ca/courses/BME/', 'Mechatronics Engineering': 'https://ugradcalendar.uwaterloo.ca/courses/MTE/', 'English': 'https://ugradcalendar.uwaterloo.ca/courses/ENGL/', 'Social Work (Bachelor of Social Work)': 'https://ugradcalendar.uwaterloo.ca/courses/SWREN/', 'Society, Technology and Values': 'https://ugradcalendar.uwaterloo.ca/courses/STV/', 'Human Sciences': 'https://ugradcalendar.uwaterloo.ca/courses/HUMSC/', 'Applied Language Studies': 'http://ugradcalendar.uwaterloo.ca/courses/APPLS/', 'Materials\xa0and Nano-Sciences': 'https://ugradcalendar.uwaterloo.ca/courses/MNS/', 'Geological Engineering': 'https://ugradcalendar.uwaterloo.ca/courses/GEOE/', 'Fine Arts': 'https://ugradcalendar.uwaterloo.ca/courses/FINE/', 'Russian and East European Studies': 'https://ugradcalendar.uwaterloo.ca/courses/REES/', 'Actuarial Science': 'http://ugradcalendar.uwaterloo.ca/courses/ACTSC/', 'Social Development Studies': 'https://ugradcalendar.uwaterloo.ca/courses/SDS/', 'Pure Mathematics': 'http://ugradcalendar.uwaterloo.ca/courses/PMATH/', 'Music': 'https://ugradcalendar.uwaterloo.ca/courses/MUSIC/', 'Drama': 'http://ugradcalendar.uwaterloo.ca/courses/DRAMA/', 'Global Business and Digital Arts': 'https://ugradcalendar.uwaterloo.ca/courses/GBDA/', 'Kinesiology': 'https://ugradcalendar.uwaterloo.ca/courses/KIN/', 'Gerontology': 'https://ugradcalendar.uwaterloo.ca/courses/GERON/', 'Greek': 'https://ugradcalendar.uwaterloo.ca/courses/GRK/', 'Psychology': 'https://ugradcalendar.uwaterloo.ca/courses/PSYCH/', 'Physics': 'https://ugradcalendar.uwaterloo.ca/courses/PHYS/', 'Applied Health Sciences': 'http://ugradcalendar.uwaterloo.ca/courses/AHS/', 'Speech Communication': 'https://ugradcalendar.uwaterloo.ca/courses/SPCOM/', 'Science': 'https://ugradcalendar.uwaterloo.ca/courses/SCI/', 'Latin': 'https://ugradcalendar.uwaterloo.ca/courses/LAT/', 'Recreation and Leisure Studies': 'https://ugradcalendar.uwaterloo.ca/courses/REC/', 'German': 'http://ugradcalendar.uwaterloo.ca/courses/GER/', 'Portuguese': 'https://ugradcalendar.uwaterloo.ca/courses/PORT/', 'East Asian': 'http://ugradcalendar.uwaterloo.ca/courses/EASIA/', 'Environment, Resources and Sustainability': 'http://ugradcalendar.uwaterloo.ca/courses/ERS/', 'Electrical and Computer Engineering': 'https://ugradcalendar.uwaterloo.ca/courses/ECE/', 'Political Science': 'https://ugradcalendar.uwaterloo.ca/courses/PSCI/', 'Dutch': 'http://ugradcalendar.uwaterloo.ca/courses/DUTCH/', 'Chemical Engineering': 'http://ugradcalendar.uwaterloo.ca/courses/CHE/', 'Korean': 'https://ugradcalendar.uwaterloo.ca/courses/KOREA/', 'Religious Studies': 'https://ugradcalendar.uwaterloo.ca/courses/RS/', 'Biology': 'http://ugradcalendar.uwaterloo.ca/courses/BIOL/', 'Planning': 'https://ugradcalendar.uwaterloo.ca/courses/PLAN/', 'Combinatorics and Optimization': 'http://ugradcalendar.uwaterloo.ca/courses/CO/'}
        prolists=''.join(progremme).split(' ')
        #名字配件//td[@colspan="2"]/b/text()
        #代号配件//td[@align="left"]/b/text()
        #编号配件//td[@align="right"]/text()

        for pl in prolists:
            if pl not in ['','and','Double','Degree'] and pl in modulesDict.keys():
                Res=modulesResDicts[modulesDict[pl]]
                modules_Dh=Res.xpath('//td[@align="left"]/b/text()')
                modules_name = Res.xpath('//td[@colspan="2"]/b/text()')
                modules_Bh=Res.xpath('//td[@align="right"]/text()')
                modules=[]
                for Dh,name,Bh in zip(modules_Dh,modules_name,modules_Bh):
                    modules+='<p>'+Dh+' '+name+' '+Bh+'</p>'
                # print(len(modules_name),len(modules_Dh),len(modules_Bh))
                # print(modules)
                modules=''.join(modules)
            else:
                modules=[]
        if modules==[]:
            modules = response.xpath(
                '//h2[contains(text(),"First-year")]/following-sibling::*[position()<5]').extract()
            modules = remove_class(modules)
        item['modules_en']=remove_class(modules)

        career=response.xpath('//h2[contains(text(),"raduates")]/following-sibling::*[1]|//h2[contains(text(),"areer")]/following-sibling::*[1]').extract()
        # print(career)
        career=remove_class(career)
        item['career_en']=career

        other='根据业务老师要求，将专业名拆开进行匹配获取课程设置内容。若为匹配到，则抓取专业页面第一年的课程。若专业页面没有关于课程的内容，则字段为空。与老师沟通时未在页面上找到的部分字段:campus,start_date,duration'
        item['other']=other

        yield item