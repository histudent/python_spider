# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
from scrapySchool_England_U.middlewares import *

class UniversityofglasgowUSpider(scrapy.Spider):
    name = 'UniversityOfGlasgow_U'
    # allowed_domains = ['a.b']
    base_url='https://www.gla.ac.uk/undergraduate/degrees/?filter=%s'

    start_urls=['https://www.gla.ac.uk/']
    def parse(self, response):
        urls=['https://www.gla.ac.uk/undergraduate/degrees/accountancy/',
'https://www.gla.ac.uk/undergraduate/degrees/accountingmathematics/',
'https://www.gla.ac.uk/undergraduate/degrees/accountingstatistics/',
'https://www.gla.ac.uk/undergraduate/degrees/aeronauticalengineering/',
'https://www.gla.ac.uk/undergraduate/degrees/aerospacesystems/',
'https://www.gla.ac.uk/undergraduate/degrees/anatomy/',
'https://www.gla.ac.uk/undergraduate/degrees/ancienthistory/',
'https://www.gla.ac.uk/undergraduate/degrees/archaeology/',
'https://www.gla.ac.uk/undergraduate/degrees/astronomy/',
'https://www.gla.ac.uk/undergraduate/degrees/biochemistry/',
'https://www.gla.ac.uk/undergraduate/degrees/biomedicalengineering/',
'https://www.gla.ac.uk/undergraduate/degrees/biotechnology/',
'https://www.gla.ac.uk/undergraduate/degrees/businesseconomics/',
'https://www.gla.ac.uk/undergraduate/degrees/businessmanagement/',
'https://www.gla.ac.uk/undergraduate/degrees/celticcivilisation/',
'https://www.gla.ac.uk/undergraduate/degrees/celticstudies/',
'https://www.gla.ac.uk/undergraduate/degrees/centraleasteuropeanstudies/',
'https://www.gla.ac.uk/undergraduate/degrees/chemicalphysics/',
'https://www.gla.ac.uk/undergraduate/degrees/chemistry/',
'https://www.gla.ac.uk/undergraduate/degrees/chemistrymedicinal/',
'https://www.gla.ac.uk/undergraduate/degrees/civilengineering/',
'https://www.gla.ac.uk/undergraduate/degrees/civilengineeringwitharchitecture/',
'https://www.gla.ac.uk/undergraduate/degrees/classics/',
'https://www.gla.ac.uk/undergraduate/degrees/commonlaw/',
'https://www.gla.ac.uk/undergraduate/degrees/communitydevelopment/',
'https://www.gla.ac.uk/undergraduate/degrees/comparativeliterature/',
'https://www.gla.ac.uk/undergraduate/degrees/computingscience/',
'https://www.gla.ac.uk/undergraduate/degrees/dentistry/',
'https://www.gla.ac.uk/undergraduate/degrees/digitalmedia/',
'https://www.gla.ac.uk/undergraduate/degrees/earthscience2018/',
'https://www.gla.ac.uk/undergraduate/degrees/economics/',
'https://www.gla.ac.uk/undergraduate/degrees/economicsocialhistory/',
'https://www.gla.ac.uk/undergraduate/degrees/education/',
'https://www.gla.ac.uk/undergraduate/degrees/electronics/',
'https://www.gla.ac.uk/undergraduate/degrees/electronicsoftwareengineering/',
'https://www.gla.ac.uk/undergraduate/degrees/electronicswithmusic/',
'https://www.gla.ac.uk/undergraduate/degrees/englishlanguage/',
'https://www.gla.ac.uk/undergraduate/degrees/englishliterature/',
'https://www.gla.ac.uk/undergraduate/degrees/environmentalsciencesustainability/',
'https://www.gla.ac.uk/undergraduate/degrees/filmtelevisionstudies/',
'https://www.gla.ac.uk/undergraduate/degrees/financemathematics/',
'https://www.gla.ac.uk/undergraduate/degrees/financestatistics/',
'https://www.gla.ac.uk/undergraduate/degrees/french/',
'https://www.gla.ac.uk/undergraduate/degrees/gaelic/',
'https://www.gla.ac.uk/undergraduate/degrees/genetics/',
'https://www.gla.ac.uk/undergraduate/degrees/geography/',
'https://www.gla.ac.uk/undergraduate/degrees/geology/',
'https://www.gla.ac.uk/undergraduate/degrees/german/',
'https://www.gla.ac.uk/undergraduate/degrees/greek/',
'https://www.gla.ac.uk/undergraduate/degrees/healthsocialpolicy/',
'https://www.gla.ac.uk/undergraduate/degrees/history/',
'https://www.gla.ac.uk/undergraduate/degrees/historyofart/',
'https://www.gla.ac.uk/undergraduate/degrees/humanbiology/',
'https://www.gla.ac.uk/undergraduate/degrees/humanbiologynutrition/',
'https://www.gla.ac.uk/undergraduate/degrees/immunology/',
'https://www.gla.ac.uk/undergraduate/degrees/internationalrelations/',
'https://www.gla.ac.uk/undergraduate/degrees/italian/',
'https://www.gla.ac.uk/undergraduate/degrees/latin/',
'https://www.gla.ac.uk/undergraduate/degrees/marinefreshwaterbiology/',
'https://www.gla.ac.uk/undergraduate/degrees/mathematics/',
'https://www.gla.ac.uk/undergraduate/degrees/mechanicaldesignengineering/',
'https://www.gla.ac.uk/undergraduate/degrees/mechanicalengineering/',
'https://www.gla.ac.uk/undergraduate/degrees/mechanicalengineeringwithaeronautics/',
'https://www.gla.ac.uk/undergraduate/degrees/mechatronics/',
'https://www.gla.ac.uk/undergraduate/degrees/medicine/',
'https://www.gla.ac.uk/undergraduate/degrees/microbiology/',
'https://www.gla.ac.uk/undergraduate/degrees/molecularcellularbiology/',
'https://www.gla.ac.uk/undergraduate/degrees/musicbmus/',
'https://www.gla.ac.uk/undergraduate/degrees/musicma/',
'https://www.gla.ac.uk/undergraduate/degrees/neuroscience/',
'https://www.gla.ac.uk/undergraduate/degrees/nursing/',
'https://www.gla.ac.uk/undergraduate/degrees/pharmacology/',
'https://www.gla.ac.uk/undergraduate/degrees/philosophy/',
'https://www.gla.ac.uk/undergraduate/degrees/physics/',
'https://www.gla.ac.uk/undergraduate/degrees/physicswithastrophysics/',
'https://www.gla.ac.uk/undergraduate/degrees/physiology/',
'https://www.gla.ac.uk/undergraduate/degrees/physiologysportsscience/',
'https://www.gla.ac.uk/undergraduate/degrees/physiologysportssciencenutrition/',
'https://www.gla.ac.uk/undergraduate/degrees/plantscience/',
'https://www.gla.ac.uk/undergraduate/degrees/politics/',
'https://www.gla.ac.uk/undergraduate/degrees/portuguese/',
'https://www.gla.ac.uk/undergraduate/degrees/primaryeducationtq/',
'https://www.gla.ac.uk/undergraduate/degrees/productdesignengineering/',
'https://www.gla.ac.uk/undergraduate/degrees/psychology/',
'https://www.gla.ac.uk/undergraduate/degrees/publicpolicy/',
'https://www.gla.ac.uk/undergraduate/degrees/quantitativemethods/',
'https://www.gla.ac.uk/undergraduate/degrees/religiousphilosophicaleducation/',
'https://www.gla.ac.uk/undergraduate/degrees/russian/',
'https://www.gla.ac.uk/undergraduate/degrees/scotslaw/',
'https://www.gla.ac.uk/undergraduate/degrees/scottishhistory/',
'https://www.gla.ac.uk/undergraduate/degrees/scottishliterature/',
'https://www.gla.ac.uk/undergraduate/degrees/sociology/',
'https://www.gla.ac.uk/undergraduate/degrees/softwareengineering/',
'https://www.gla.ac.uk/undergraduate/degrees/spanish/',
'https://www.gla.ac.uk/undergraduate/degrees/statistics/',
'https://www.gla.ac.uk/undergraduate/degrees/technologicaleducation/',
'https://www.gla.ac.uk/undergraduate/degrees/theatrestudies/',
'https://www.gla.ac.uk/undergraduate/degrees/theologyreligiousstudies/',
'https://www.gla.ac.uk/undergraduate/degrees/veterinarybiosciences/',
'https://www.gla.ac.uk/undergraduate/degrees/veterinarymedicine/',
'https://www.gla.ac.uk/undergraduate/degrees/zoology/',]
        for u in urls:
            yield scrapy.Request(url=u,callback=self.tuition,meta={'url':u})
    def tuition(self,response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.meta['url']
        item['university']='University of Glasgow'
        print(response.url)
        programme = response.xpath('//div[@id="prog-title"]/h1/text()').extract()
        print(programme)
        item['programme_en'] = ''.join(programme).strip()
        yield item
    start_urlss = []
    subject=['Accounting and Finance',
'Archaeology',
'Biodiversity, Animal Health and Comparative Medicine',
'Business',
'Cardiovascular and Medical Sciences',
'Celtic and Gaelic',
'Central and East European Studies',
'Chemistry',
'Classics',
'Comparative Literature',
'Computing Science',
'Dentistry',
'Economic and Social History',
'Economics',
'Education',
'Engineering',
'English Language and Linguistics',
'English Literature',
'Environment',
'Film and Television Studies',
'Geographical and Earth Sciences',
'Health and Wellbeing',
'History',
'History of Art',
'Infection, Immunity and Inflammation',
'Information Studies',
'Law',
'Life Sciences',
'Management',
'Mathematics',
'Medicine',
'Modern Languages and Cultures',
'Music',
'Neuroscience and Psychology',
'Nursing and Health Care',
'Philosophy',
'Physics and Astronomy',
'Politics',
'Psychology',
'Scottish Literature',
'Sociology',
'Statistics',
'Teaching',
'Theatre Studies',
'Theology and Religious Studies',
'Urban Studies',
'Veterinary Medicine',]
    values=["accountingfinance",
"archaeology",
"bahcm",
"business",
"cms",
"celticgaelic",
"cees",
"chemistry",
"classics",
"comparativeliterature",
"computing",
"dentistry",
"economicsocialhistory",
"economics",
"education",
"engineering",
"englishlanguage",
"englishliterature",
"environment",
"filmtelevision",
"ges",
"healthwellbeing",
"history",
"historyofart",
"iii",
"informationstudies",
"law",
"lifesciences",
"management",
"mathematics",
"medicine",
"modernlanguagescultures",
"music",
"neurosciencepsychology",
"nursing",
"philosophy",
"physics",
"politics",
"psychology",
"scottishliterature",
"sociology",
"statistics",
"teaching",
"theatre",
"theology",
"urbanstudies",
"veterinary",]
    for i in values:
        full_url=base_url % i
        start_urlss.append(full_url)
    def parses(self, response):
        # print(response.url)
        subjects={'veterinary': 'Veterinary Medicine', 'comparativeliterature': 'Comparative Literature', 'healthwellbeing': 'Health and Wellbeing', 'music': 'Music', 'lifesciences': 'Life Sciences', 'medicine': 'Medicine', 'business': 'Business', 'education': 'Education', 'scottishliterature': 'Scottish Literature', 'philosophy': 'Philosophy', 'historyofart': 'History of Art', 'archaeology': 'Archaeology', 'psychology': 'Psychology', 'ges': 'Geographical and Earth Sciences', 'politics': 'Politics', 'history': 'History', 'classics': 'Classics', 'cees': 'Central and East European Studies', 'dentistry': 'Dentistry', 'physics': 'Physics and Astronomy', 'environment': 'Environment', 'teaching': 'Teaching', 'computing': 'Computing Science', 'modernlanguagescultures': 'Modern Languages and Cultures', 'nursing': 'Nursing and Health Care', 'mathematics': 'Mathematics', 'bahcm': 'Biodiversity, Animal Health and Comparative Medicine', 'economicsocialhistory': 'Economic and Social History', 'statistics': 'Statistics', 'englishlanguage': 'English Language and Linguistics', 'filmtelevision': 'Film and Television Studies', 'sociology': 'Sociology', 'management': 'Management', 'engineering': 'Engineering', 'neurosciencepsychology': 'Neuroscience and Psychology', 'englishliterature': 'English Literature', 'accountingfinance': 'Accounting and Finance', 'law': 'Law', 'chemistry': 'Chemistry', 'theatre': 'Theatre Studies', 'cms': 'Cardiovascular and Medical Sciences', 'iii': 'Infection, Immunity and Inflammation', 'informationstudies': 'Information Studies', 'celticgaelic': 'Celtic and Gaelic', 'economics': 'Economics', 'theology': 'Theology and Religious Studies', 'urbanstudies': 'Urban Studies'}
        pro_lis=response.xpath('//ul[@id="jquerylist"]/li/a/@href').extract()
        programme=response.xpath('//ul[@id="jquerylist"]/li/a/text()').extract()
        # print(programme)
        programme='-'.join(programme).strip()
        prog=re.findall('[A-Z/&a-z\s\(\),]{2,}',programme)
        values=re.findall('filter=.+',response.url)
        # print(values)
        values=''.join(values).replace('filter=','')
        subject=subjects[values]
        # print(subject)
        for url,pro in zip(pro_lis,prog):
            pro_url='https://www.gla.ac.uk'+url
            deg_xpath='//a[contains(@href,"%s")]/span/text()' % url
            deg=response.xpath(deg_xpath).extract()
            deg=set(deg)
            # print(deg)
            yield scrapy.Request(url=pro_url,callback=self.parse_main,meta={"programme":pro,"degree_name":deg,"department":subject})
    def parse_main(self, response):
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)

        department=response.meta['department']
        item['department']=department

        programme=response.meta['programme']
        degreee_name=response.meta['degree_name']
        item['major_type1']=programme
        # print(degreee_name)
        # print(programme)
        degreee_name = ','.join(degreee_name).replace(']', '').replace('[', '').strip()
        # item['degree_name']=degreee_name

        degreee_name=response.xpath('//div[@id="ucascodes_db"]/h3/text()').extract()

        item['teach_time'] = 'fulltime'
        item['university'] = 'University of Glasgow'
        item['url'] = response.url
        item['location'] = 'Glasgow'
        # item['start_date'] = '2018-9'
        item['deadline'] = '2018-6-30'
        item["tuition_fee_pre"] = "£"

        duration=response.xpath('//h3[contains(text(),"ear")]//text()').extract()
        # print(duration)
        duration=''.join(duration)
        duration=re.findall('\d+',duration)
        try:
            duration=list(map(int,duration))
            duration=max(duration)
            # print(duration)
            item['duration']=duration
            item['duration_per'] = 1
        except:
            item['duration']=None
            item['duration_per']=None

        overview = response.xpath('//div[@class="whyglasgow"]').extract()
        overview = remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        modules = response.xpath('//h2[contains(text(),"Programme str")]/following-sibling::*').extract()
        modules = remove_class(modules)
        item['modules_en'] = modules
        # print(modules)

        career = response.xpath('//h2[contains(text(),"Career")]/following-sibling::*').extract()
        career = remove_class(career)
        item['career_en'] = career

        item['tuition_fee'] = '15500'

        IELTS = response.xpath('//*[contains(text(),"IELTS")]/../following-sibling::ul[1]//text()').extract()
        # print(IELTS)
        ielts = get_ielts(IELTS)
        if ielts != {} and ielts != []:
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            item['ielts'] = ielts['IELTS']
        TOEFL = response.xpath('//*[contains(text(),"TOEFL")]/..//text()').extract()
        # print(TOEFL)
        toefl = get_toefl(TOEFL)
        # print(toefl)
        if toefl != []:
            try:
                item['toefl_r'] = toefl[1]
                item['toefl_l'] = toefl[2]
                item['toefl_s'] = toefl[3]
                item['toefl_w'] = toefl[4]
                item['toefl'] = toefl[0]
            except:
                pass

        entry = response.xpath('//h2[contains(text(),"Entry requirements")]/following-sibling::*').extract()
        entry = clear_same_s(entry)
        entry = remove_class(entry)
        entry='<p>‌The University will consider students who have gained high scores in their Senior High School exams for direct entry into first year. Students who have taken a recognised foundation or access programme or equivalent will also be considered, as well as those students who have studied GCE A Levels.</p>'
        item['require_chinese_en'] = entry

        apply_d = response.xpath('//h2[contains(text(),"How to apply")]/following-sibling::*').extract()
        apply_d = remove_class(apply_d)
        item['apply_proces_en'] = apply_d

        alevel = response.xpath('//h3[contains(text(),"A-level")]/following-sibling::ul[1]//text()').extract()
        alevel = remove_class(alevel)
        # print(alevel)
        item['alevel']=alevel
        # if alevel == '':
        #     print(response.url)

        ib = response.xpath(
            '//h3[contains(text(),"International Baccalaureate")]/following-sibling::ul[1]//text()').extract()
        ib = remove_class(ib)
        item['ib']=ib
        # print(ib)
        # if ib=='':
        #     print(response.url)

        for i in degreee_name:
            item['degree_name']=i
            pro_xpath='//h3[contains(text(),"%s")]/following-sibling::ul[1]/li/span[contains(@style,"width:90")]/text()' % i
            programme=response.xpath(pro_xpath).extract()
            # print(programme)
            programme=''.join(programme).split(':')[0:-1]
            # print(programme)
            ucas_xpath='//h3[contains(text(),"%s")]/following-sibling::ul[1]//span/strong/text()' % i
            ucas_list=response.xpath(ucas_xpath).extract()
            if len(programme)==len(ucas_list):
                for m,n in zip(programme,ucas_list):
                    item['ucascode']=n
                    item['programme_en']=m
                    yield item
            else:
                item['programme_en']=':'.join(programme)
                item['ucascode']=''.join(ucas_list)
                yield item
