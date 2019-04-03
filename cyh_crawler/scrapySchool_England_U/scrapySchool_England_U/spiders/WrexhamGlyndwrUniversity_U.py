# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
class WrexhamglyndwruniversityUSpider(scrapy.Spider):
    name = 'WrexhamGlyndwrUniversity_U'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.glyndwr.ac.uk/en/A-Z/UndergraduateA-Z/']
    def parse(self, response):
        url=['https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/Animationfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/AeronauticalandMechanicalEngineeringfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/Acupuncturefoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/AccountingandFinancefoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Chemistry/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/Chemistrywithfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/Computingfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/ConstructionManagementwithFoundationYear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/ComputerSciencefoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/ComputerNetworksandsecurityfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/ComputerNetworkandSecurity/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/ComputerGameDevelopmentfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/YouthandCommunityWorkfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/TelevisionProductionandTechnologyfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/SportsCoachingforParticipationandPerformanceDevelopment/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/SportsCoachingforParticipationandPerformanceDevelopmentfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/SportandExerciseSciencefoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/SoundTechnologyfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/RenewableEnergyandSustainableEngineeringfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/RadioProduction/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/RadioProductionfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/HealthandWellbeingfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/HealthandWellbeing/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/Psychologyfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/ProfessionalSoundandVideo/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/ProfessionalSoundandVideofoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Policing/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/PhotographyandFilmfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/Musictechnologyfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/MentalHealthandWellbeing/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/MentalHealthandWellbeingfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/DesignIllustrationGraphicNovelsandChildrensPublishing/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/IllustrationGraphicNovelsandChildrensPublishingfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/Marketingfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/GraphicDesignfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/FootballCoachingandthePerformanceSpecialist/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/FootballCoachingandthePerformanceSpecialistfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/FineArt/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/FineArtfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/HospitalityTourismandEventManagementfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/GameArtfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/FamiliesandChildhoodStudiesfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/EquineScienceandWelfareManagement/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/FineArtMFA/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/EnglishandCreativeWriting/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/ElectricalandElectronicEngineeringfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/EducationandChildhoodStudiesfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/EquineScienceandWelfareManagementfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/EducationALNSEN/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/CyberSecurityfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/ComputerGameDesignandEnterpriseFoundationYear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/BusinessFoundationYear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/ComplementaryTherapiesforHealthcarefoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/EducationALNSENfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/ForensicSciencefoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/BroadcastingandJournalismfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/AppliedArts/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/AutomotiveEngineeringfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/BroadcastingandJournalism/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/AppliedArtsfoundationyear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/ArchitecturalDesignTechnologyFoundationYear/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/AppliedArtsMDes/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/AnimalScience/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/IllustrationGraphicNovelsandChildrensPublishingMDes/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/FilmandPhotographyMDes/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/GraphicDesignandMultimediaMDes/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/History/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/DesignGraphicDesignandMultimedia/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Psychology/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/ComputerGameDevelopment/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/ArtificialIntelligence/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/ComputerScience/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/ForensicScience/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/AeronauticalandMechanicalEngineering/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/ElectricalandElectronicEngineering/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/AutomotiveEngineering/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/HistoryandCreativeWriting/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/EnglishHistory/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Business/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/SportsandExerciseSciences/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/DesignFilmandPhotography/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Nursing/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/English/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Animation/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/AccountingandFinance/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/FinancialTechnologyManagement/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/GameArt/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/RenewableEnergyandSustainableEngineering/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/ArchitecturalDesignTechnology/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Television/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/RehabilitationandInjuryManagement/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/OccupationalTherapy/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/MusicTechnology/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/FamiliesandChildhoodStudies/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/EducationandChildhoodStudies/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/CriminologyandCriminalJustice/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/AutomationEngineering/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/ComputerGameDesignandEnterprise/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/ConstructionManagement/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/YouthandCommunityWork/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/HospitalityTourismandEventManagement/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/SoundTechnology/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/SocialWork/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Marketing/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Computing/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/CyberSecurity/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/ComputerGameDevelopmentMComp/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/AnimationMDes/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/GameArtMDes/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Journalism/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Acupuncture/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/ComplementaryTherapiesforHealthcare/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/TheatreTelevisionandPerformance/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/HumanResourceManagement/',
'https://www.glyndwr.ac.uk/en/Undergraduatecourses/Foundationyear/HumanResourceManagementfoundationyear/',]
        url=set(url)
        for u in url:
            yield scrapy.Request(url=u,callback=self.parsesss,meta={'url':u})
    def parsesss(self,response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['university']='Wrexham Glyndwr University'
        item['url']=response.meta['url']
        print(response.url)
        item['ib']='For those studying the International Baccalaureate, we require a minimum of 112 UCAS tariff points in total from the certificates you have taken as part of this qualification, with any required subjects studied at Higher Level for undergraduate study.'
        alevel=response.xpath('//p[contains(text(),"tariff")]/text()').extract()
        print(alevel)
        item['alevel']=remove_class(alevel)
        yield item


    def parsess(self, response):
        pro_url=response.xpath('//ul[@id="undergraduatecourses"]/li/a[@class="list-link"]/@href').extract()
        pro_name=response.xpath('//ul[@id="undergraduatecourses"]/li/a[@class="list-link"]//p[@class="course-name"]/text()').extract()
        for url,name in zip(pro_url,pro_name):
            url='https://www.glyndwr.ac.uk'+url
            yield scrapy.Request(url,meta={'programme':name},callback=self.parses)
    def parses(self,response):
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        # print(response.meta['programme'])
        item['url']=response.url
        item['university']='Wrexham Glyndwr University'
        # item['major_type1']=response.meta['programme']
        #第一种在详情页获取专业名的方式
        prog=response.xpath('//div[@class="breadcrumb-links"]/a/text()').extract()
        # print(prog[-1])
        #第二种获取专业名的方式
        pro=response.xpath('//h1/span[@class="course-name"]/text()').extract()
        programme=' '.join(pro).strip()
        # print(programme)
        item['programme_en']=programme
        degree=response.xpath('//h1/span[@class="header-bg-color"]/text()').extract()
        degree=''.join(degree)
        # print(degree)
        item['degree_name']=degree
        ucascode=response.xpath('//div[contains(text(),"UCAS code")]/following-sibling::div/text()').extract()
        # print(ucascode)
        ucascode=''.join(ucascode).strip()
        # print(ucascode)
        item['ucascode']=ucascode
        duration=response.xpath('//div[contains(text(),"Duration")]/following-sibling::div/text()').extract()
        duration=''.join(duration)
        mode=re.findall('(?i)ft',duration)
        # if mode==[]:
        #     print(duration)
        # if mode!=[]:
        #     print(duration)
        dura=re.findall('\d',duration)
        try:
            dura=list(map(int,dura))
            item['duration']=min(dura)
            item['duration_per']='1'
        except:
            pass
        location=response.xpath('//div[contains(text(),"Location")]/following-sibling::div/text()').extract()
        location=''.join(location).strip()
        item['location']=location
        item['tuition_fee']='11750'
        htp=['<h2>Applying through<span>&nbsp;UCAS<br /></span></h2>',
"<p>For the majority of undergraduate courses, you'll need to apply through UCAS.&nbsp; If you are interested in studying a part-time or postgraduate course at Wrexham Glyndwr, then please see our&nbsp;<a>alternative application routes.</a></p>",
'<p>Once you&rsquo;ve decided on which courses you wish to apply for then you&rsquo;ll need to register at&nbsp;<a>.</span></p>',
'<p>If you are currently at school or college, you may be given a &lsquo;buzzword&rsquo; to use when you register &ndash; this will help distinguish where you are applying from. Those who wish to apply independently will not need a buzzword, but will still use the UCAS system to apply.</p>',
'</section><section>',
'<h2><strong><span>Completing</span> your application</strong></h2>',
'<p>The online application system &nbsp;opens in September for entry to the University in the following year.&nbsp; You do not have to complete your application all in one go &ndash; the system will allow you to complete it in stages.</p>',
'<p>Your application will need to include the following information:</p>',
'<p><strong>Your personal details</strong> &ndash; remember your name needs to be stated as shown on your official documents, such as your birth certificate or passport.</p>',
'<p><strong>Your qualifications</strong> &ndash; be sure to enter all of your qualifications and any pending qualifications that you are awaiting results for. If you encounter any problems, get in touch with UCAS or our admissions team.</p>',
'<p><strong>A personal statement</strong> &ndash; this is one of the most important parts of your application as a well-written and thoughtful personal statement can really make you stand out from the crowd. A poor one could undermine an otherwise good application.</p>',
'<p>There is no definitive way of writing a personal statement which will guarantee acceptance onto your chosen course, however there are guidelines that will help you to focus on what you should and shouldn&rsquo;t include. <a>Why not read our Top 10 Tips on Writing your Personal Statement before you get started?</a></p>',
'<p><strong>A reference</strong> &ndash; ideally this should be from a teacher or a professional who knows you well and can verify your suitability for higher education.</p>',
'<p><strong>You will be required to disclose if you have a &lsquo;relevant&rsquo; criminal conviction</strong> &ndash; some specific courses may require you to undergo a DBS check &ndash; where this is the case you must select &ldquo;Yes&rdquo; if you have ever had a conviction, even if this is spent.</p>',
'<p><a>Find out more about obtaining a DBS check for study.</a></p>',
'<h2>Clearing</h2>',
'<p>If you apply through UCAS after 30th June 2018, your application will not be sent to us. Instead you will receive details about Clearing.</p>',
'<p>Clearing is a process that is available between July and September for those who are applying late, have already applied and haven&rsquo;t received a place, or have declined all of their offers.</p>',
'<p>If you wish to secure a place at Wrexham Glyndŵr University, then we strongly advise that from the beginning of July to mid-September you call our dedicated Clearing Hotline on 01978 293439 &ndash; our friendly team will be able to help you with course vacancies and put you in touch with the relevant admissions staff.</p>',
'</section></div>',
]
        item['apply_proces_en']=remove_class(htp)
        overview=response.xpath('//div[@id="introduction-text"]').extract()
        item['overview_en']=remove_class(overview)
        modules=response.xpath('//a[contains(text(),"YOU STUDY")]/../following-sibling::dd[1]').extract()
        # print(modules)
        item['modules_en']=remove_class(modules)
        item['deadline']='2019-6-30'
        item['ielts_desc']='Undergraduate study 6.0 (no band lower than 5.5)'
        item['ielts']='6.0'
        item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']='5.5','5.5','5.5','5.5'
        chi=["<p><strong>本科学习（学士）</strong></p>",
"<p>▪ 高中毕业证书及成绩单，完成英国本科预科 (Foundation Year)<br />▪ 职高毕业证书及成绩单<br />▪ 大专毕业证书及成绩单<br />▪ 大二及以上本科生转学，需持有成绩单</p>",]
        item['require_chinese_en']=remove_class(chi)
        career=response.xpath('//a[contains(text(),"CAREER")]/../following-sibling::dd[1]').extract()
        item['career_en']=remove_class(career)
        assessment=response.xpath('//a[contains(text(),"ASS")]/../following-sibling::dd[1]').extract()
        item['assessment_en']=remove_class(assessment)
        alevel=response.xpath('//p[contains(text(),"A-level")]//text()|//p[contains(text(),"A-Level")]//text()').extract()
        if alevel==[]:
            alevel=response.xpath('//div[contains(text(),"UCAS Tariff")]/following-sibling::div//text()').extract()
        else:
            print('GG')
        # print(alevel)
        item['alevel']=''.join(alevel)
        item['ib']='For those studying the International Baccalaureate, we require a minimum of 28 points overall,'
        yield item
        # else:
        #     print('兼职专业，跳过')
        # yield item
