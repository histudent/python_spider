# -*- coding: utf-8 -*-
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.getItem import *
from scrapySchool_Canada_College.items import *

class StlawencecollegeSpider(scrapy.Spider):
    name = 'StLawenceCollege'
    # allowed_domains = ['a.b']
    start_urls = [
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/advertising-and-marketing-communications/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/advertising-and-marketing-communications-management/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/assistant-cook-apprenticeship/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/autism-and-behavioural-science/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/automotive-service-apprenticeship/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/baa-behavioural-psychology/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/bachelor-of-business-administration/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/bachelor-of-business-administration-parttime/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/bachelor-of-science-in-nursing-bscn/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/bachelor-of-science-in-nursing-bscn/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/bachelor-of-science-in-nursing-bscn/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/behavioural-science-technology/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/behavioural-science-fasttrack/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/biotechnology-advanced/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/brick-and-stone-masonry-apprenticeship/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-accounting/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-accounting/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-human-resources/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-at-alpha-international-academy/alpha-toronto/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-at-canadian-college/vancouver/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-administration/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-administration-accounting/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-administration-accounting/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-administration-human-resources/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-administration-human-resources-fasttrack/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-administration-human-resources-fasttrack/alpha-toronto/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-administration-marketing/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-analytics/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-analytics-int/business-analytics-int/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-fundamentals/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-fundamentals/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-fundamentals/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/business-marketing/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/careercollege-preparatory-program-adult-upgrading/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/careercollege-preparatory-program-adult-upgrading/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/careercollege-preparatory-program-adult-upgrading/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/carpenter-apprenticeship/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/carpenter-apprenticeship/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/carpentry-techniques/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/carpentry-techniques-general-construction/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/child-and-youth-care/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/child-and-youth-care/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/child-and-youth-care-fasttrack/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/civil-engineering-technology/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/communicative-disorders-assistant/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/community-and-justice-services/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/community-integration-through-cooperative-education-cice/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/community-integration-through-cooperative-education-cice/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/community-integration-through-cooperative-education-cice/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/computer-networking-and-technical-support/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/computer-networking-and-technical-support/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/computer-networking-tech-support-at-canadian-college/vancouver/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/computer-networking-and-technical-support-alpha/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/computer-programmer-analyst/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/cook-apprenticeship/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/culinary-management/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/culinary-managementcook-coop-diploma-apprenticeship/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/culinary-skills-chef-training/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/early-childhood-education/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/early-childhood-education/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/electrical-engineering-technician/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/electrician-construction-and-maintenance-apprenticeship/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/energy-systems-engineering-technician/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/energy-systems-engineering-technology/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/english-as-a-second-language-at-alpha-international/alpha-toronto/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/english-as-a-second-language-esl/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/english-for-academic-purposes-general-arts-and-science/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/environmental-technician/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/environmental-technician-fast-track/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/esthetician/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/fine-arts-visual-and-creative-arts/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/fitness-and-health-promotion/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/french-advanced-proficiency-in-conversational-french/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/game-programming/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-arts-and-science-certificate-applied-arts-stream/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-arts-and-science-certificate-behavioural-psychology-stream/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-arts-and-science-certificate-general-studies-stream/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-arts-and-science-certificate-general-studies-stream/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-arts-and-science-certificate-general-studies-stream/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-arts-and-science-certificate-social-sciences-stream/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-arts-and-science-certificate-social-sciences-stream/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-arts-and-science-certificate-technology-stream/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-arts-and-science-certificate-technology-stream/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-arts-and-science-certificate-trades-stream/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-arts-and-science-certificate-trades-stream/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-arts-and-science-diploma/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-arts-and-science-diploma/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-arts-and-science-diploma/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-arts-and-science-canadian-college/vancouver/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-construction-carpentry-techniques/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/general-machinist-apprenticeship/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/graphic-design/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/hairstyling/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/hairstyling/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/hairstylist-apprenticeship/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/health-care-administration/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/health-care-administration-canadian-college/vancouver/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/health-care-administration/kintl/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/health-information-management/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/honours-bachelor-of-behavioural-psychology/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/hospitality/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/industrial-electrician-apprenticeship/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/industrial-mechanic-millwright-apprenticeship/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/instrumentation-and-control-engineering-technician/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/instrumentation-and-control-engineering-technology/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/interactive-marketing-communications/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/international-business-management-canadian-college/vancouver/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/law-clerk/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/mechanical-technician/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/media-arts-fundamentals/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/medical-laboratory-assistanttechnician/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/medical-laboratory-science/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/mental-wellness-and-addictions-worker/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/motive-power-technician/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/motive-power-technician-diploma-automotive-service-technician-coop-apprenticeship/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/music-and-digital-media/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/a_m/music-theatre-performance/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/office-administration-general/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/office-administration-general/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/office-administration-health-services/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/office-administration-health-services/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/office-administration-legal/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/office-administration-legal/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/office-administration-legalhealthservices/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/office-administration-legalhealthservices/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/paramedic/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/personal-support-worker/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/personal-support-worker/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/plumber-apprenticeship/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/police-foundations/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/police-foundations/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/police-foundations/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/police-foundations-fasttrack/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/police-foundations-fasttrack/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/police-foundations-fasttrack/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/police-foundations/police-foundations-part-time-online/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/police-foundations/police-foundations-online/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/practical-nursing/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/practical-nursing/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/practical-nursing/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/prehealth-sciences-pathway/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/prehealth-sciences-pathway/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/prehealth-sciences-pathway/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/prehealth-path-to-cert-and-diploma/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/prehealth-path-to-cert-and-diploma/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/preservice-firefighter-education-and-training/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/project-management-at-alpha-international/alpha-toronto/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/social-service-worker/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/social-service-worker/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/social-service-worker-fasttrack/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/supply-chain-management/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/supply-chain-management-canadian-college/vancouver/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/supply-chain-management-at-alpha-internaitonal/alpha-logistics/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/therapeutic-recreation/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/tourism/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/tourism-alpha/alpha/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/user-experience-design/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/veterinary-assistant/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/veterinary-technology/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/visual-and-creative-arts-fine-arts/brockville/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/welding-and-fabrication-technician/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/welding-and-fabrication-technician-coop-diploma-apprenticeship/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/welding-and-fabrication-techniques/cornwall/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/wind-turbine-technician/kingston/',
'http://www.stlawrencecollege.ca/programs-and-courses/full-time/programs/n_z/wind-turbine-technician-industrial-electrician-coop-diploma-apprenticeship/kingston/',]

    def parse(self, response):
        item=get_item(ScrapyschoolCanadaCollegeItem)
        item['school_name']='St. Lawence College'
        item['url']=response.url
        print(response.url)

        item['other']='1.课程代码一样的专业校区不一样 2.国际生学费在PDF里面'
        item['apply_fee'],item['apply_pre']='100','$'
        item['toefl']='78'
        item['ielts_desc']='A minimum score of 6.0 overall, with a minimum score of 5.5'
        item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']='6.0','5.5','5.5','5.5','5.5'
        item['average_score']='60'
        major_name=response.xpath('//h2/text()').extract()
        major_name=''.join(major_name).strip()
        # print(major_name)
        item['major_name_en']=major_name

        overview=response.xpath('//overview').extract()
        # print(overview)
        item['overview_en']=remove_class(overview)

        modules=response.xpath('//div[@class="programOutline printTwoColumns"]').extract()
        # print(modules)
        item['modules_en']=remove_class(modules)

        career=response.xpath('//h4[text()="Career Opportunities"]/following-sibling::p[1]').extract()
        item['career_en']=remove_class(career)

        texts=response.xpath('//h4[text()="Program Name"]/..//text()').extract()
        print(texts)
        if 'Program Code' in texts:
            code=texts[texts.index('Program Code')+1].strip()
            # print(code)
            item['programme_code']=code
        degree_name=texts[texts.index('Credential')+1].strip()
        # print(degree_name)
        item['degree_name']=degree_name
        if 'Start Dates' in texts:
            start_date=texts[texts.index('Start Dates')+1:texts.index('Program Duration')]
            print(start_date)
            start_date=tracslateDate(start_date)
            print(start_date)
            item['start_date']=','.join(start_date)
        if 'Program Duration' in texts:
            duration=texts[texts.index('Program Duration')+1].strip()
            # print(duration)
            dura=clear_duration(duration)
            # print(dura)
            item['duration'],item['duration_per']=dura['duration'],dura['duration_per']
        if 'Location (Campus)' in texts:
            location=texts[texts.index('Location (Campus)')+1].strip()
            # print(location)
            item['location'],item['campus']=location,location

        entry=response.xpath('//h4[text()="Admission Requirements"]/..').extract()
        item['entry_requirements_en']=remove_class(entry)


        if degree_name!='Ontario College Certificate' and degree_name!='Certificate':
            yield item