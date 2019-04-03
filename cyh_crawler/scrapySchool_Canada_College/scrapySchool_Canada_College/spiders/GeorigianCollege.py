# -*- coding: utf-8 -*-
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.getItem import *
from scrapySchool_Canada_College.items import *



class GeorigiancollegeSpider(scrapy.Spider):
    name = 'GeorigianCollege'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.georgiancollege.ca/academics/full-time-programs/architectural-technology-co-op-arte/',
'https://www.georgiancollege.ca/academics/full-time-programs/advanced-care-paramedic-parm/',
'https://www.georgiancollege.ca/academics/full-time-programs/addictions-treatment-and-prevention-adtp/',
'https://www.georgiancollege.ca/academics/full-time-programs/acupuncture-acpt/',
'https://www.georgiancollege.ca/academics/full-time-programs/art-and-design-fundamentals-aadf/',
'https://www.georgiancollege.ca/academics/full-time-programs/advertising-and-marketing-communications-admc/',
'https://www.georgiancollege.ca/academics/full-time-programs/architectural-technician-co-op-artc/',
'https://www.georgiancollege.ca/academics/full-time-programs/acute-complex-care-for-internationally-educated-nurses-acca/',
'https://www.georgiancollege.ca/academics/full-time-programs/bachelor-of-science-in-nursing-bscn-collaborative-program-bscn/',
'https://www.georgiancollege.ca/academics/full-time-programs/baking-and-pastry-arts-bake/',
'https://www.georgiancollege.ca/academics/full-time-programs/anishnaabemowin-and-program-development-anpd/',
'https://www.georgiancollege.ca/academics/full-time-programs/automotive-business-co-op-aubu/',
'https://www.georgiancollege.ca/academics/full-time-programs/bookkeeping-bokp/',
'https://www.georgiancollege.ca/academics/full-time-programs/aviation-management-co-op-avia/',
'https://www.georgiancollege.ca/academics/full-time-programs/big-data-analytics-bdat/',
'https://www.georgiancollege.ca/academics/full-time-programs/business-busn/',
'https://www.georgiancollege.ca/academics/full-time-programs/business-co-op-busg/',
'https://www.georgiancollege.ca/academics/full-time-programs/business-entrepreneurship-entb/',
'https://www.georgiancollege.ca/academics/full-time-programs/business-accounting-bacn/',
'https://www.georgiancollege.ca/academics/full-time-programs/business-marketing-bmkn/',
'https://www.georgiancollege.ca/academics/full-time-programs/biotechnology-health-biot/',
'https://www.georgiancollege.ca/academics/full-time-programs/business-entrepreneurship-co-op-entc/',
'https://www.georgiancollege.ca/academics/full-time-programs/business-administration-co-op-badm/',
'https://www.georgiancollege.ca/academics/full-time-programs/cabinetmaking-techniques-cabt/',
'https://www.georgiancollege.ca/academics/full-time-programs/business-administration-accounting-co-op-baac/',
'https://www.georgiancollege.ca/academics/full-time-programs/business-administration-human-resources-co-op-bahr/',
'https://www.georgiancollege.ca/academics/full-time-programs/business-fundamentals-bsfn/',
'https://www.georgiancollege.ca/academics/full-time-programs/carpentry-and-renovation-techniques-crnt/',
'https://www.georgiancollege.ca/academics/full-time-programs/child-and-youth-care-cyca/',
'https://www.georgiancollege.ca/academics/full-time-programs/communications-and-professional-writing-prow/',
'https://www.georgiancollege.ca/academics/full-time-programs/communicative-disorders-assistant-coda/',
'https://www.georgiancollege.ca/academics/full-time-programs/civil-engineering-technician-co-op-cvet/',
'https://www.georgiancollege.ca/academics/full-time-programs/civil-engineering-technology-co-op-cvty/',
'https://www.georgiancollege.ca/academics/full-time-programs/community-and-justice-services-cjsr/',
'https://www.georgiancollege.ca/academics/full-time-programs/community-integration-through-co-operative-education-cice/',
'https://www.georgiancollege.ca/academics/full-time-programs/business-marketing-co-op-bmkt/',
'https://www.georgiancollege.ca/academics/full-time-programs/computer-programmer-co-op-copr/',
'https://www.georgiancollege.ca/academics/full-time-programs/computer-programmer-analyst-co-op-copa/',
'https://www.georgiancollege.ca/academics/full-time-programs/culinary-skills-culi/',
'https://www.georgiancollege.ca/academics/full-time-programs/computer-systems-technician-networking-co-op-cstn/',
'https://www.georgiancollege.ca/academics/full-time-programs/dental-assisting-levels-i-and-ii-dnas/',
'https://www.georgiancollege.ca/academics/full-time-programs/denturism-dntm/',
'https://www.georgiancollege.ca/academics/full-time-programs/development-services-worker-dswr/',
'https://www.georgiancollege.ca/academics/full-time-programs/early-childhood-education-eced/',
'https://www.georgiancollege.ca/academics/full-time-programs/electrical-techniques-eltq/',
'https://www.georgiancollege.ca/academics/full-time-programs/electrical-engineering-technician-co-op-eetn/',
'https://www.georgiancollege.ca/academics/full-time-programs/electrical-engineering-technology-co-op-eety/',
'https://www.georgiancollege.ca/academics/full-time-programs/environmental-technician-co-op-entn/',
'https://www.georgiancollege.ca/academics/full-time-programs/culinary-management-co-op-culn/',
'https://www.georgiancollege.ca/academics/full-time-programs/esthetician-esth/',
'https://www.georgiancollege.ca/academics/full-time-programs/environmental-technology-co-op-envr/',
'https://www.georgiancollege.ca/academics/full-time-programs/dental-hygiene-dnth/',
'https://www.georgiancollege.ca/academics/full-time-programs/event-management-evnt/',
'https://www.georgiancollege.ca/academics/full-time-programs/fine-arts-fiar/',
'https://www.georgiancollege.ca/academics/full-time-programs/fine-arts-advanced-fiaa/',
'https://www.georgiancollege.ca/academics/full-time-programs/food-and-nutrition-management-fdnm/',
'https://www.georgiancollege.ca/academics/full-time-programs/flight-services-flie/',
'https://www.georgiancollege.ca/academics/full-time-programs/fitness-and-health-promotion-fhpr/',
'https://www.georgiancollege.ca/academics/full-time-programs/general-arts-and-science-english-for-academic-purposes-eapc/',
'https://www.georgiancollege.ca/academics/full-time-programs/general-arts-and-science-gaas/',
'https://www.georgiancollege.ca/academics/full-time-programs/gas-technician-gast/',
'https://www.georgiancollege.ca/academics/full-time-programs/general-arts-and-science-one-year-gasc/',
'https://www.georgiancollege.ca/academics/full-time-programs/general-arts-and-science-shki-miikan-new-road-gask/',
'https://www.georgiancollege.ca/academics/full-time-programs/general-english-as-a-second-language-esl-eslg/',
'https://www.georgiancollege.ca/academics/full-time-programs/goldsmithing-and-silversmithing-glds/',
'https://www.georgiancollege.ca/academics/full-time-programs/hairstyling-hair/',
'https://www.georgiancollege.ca/academics/full-time-programs/graphic-design-production-grdp/',
'https://www.georgiancollege.ca/academics/full-time-programs/global-business-management-gbmt/',
'https://www.georgiancollege.ca/academics/full-time-programs/graphic-design-grde/',
'https://www.georgiancollege.ca/academics/full-time-programs/business-accounting-co-op-bact/',
'https://www.georgiancollege.ca/academics/full-time-programs/golf-facilities-operation-management-co-op-glfo/',
'https://www.georgiancollege.ca/academics/full-time-programs/plumbing-techniques-pltq/',
'https://www.georgiancollege.ca/academics/full-time-programs/photography-phot/',
'https://www.georgiancollege.ca/academics/full-time-programs/power-engineering-technology-co-op-pety/',
'https://www.georgiancollege.ca/academics/full-time-programs/police-foundations-pfpr/',
'https://www.georgiancollege.ca/academics/full-time-programs/pre-health-sciences-pathway-to-advanced-diplomas-and-degrees-phpa/',
'https://www.georgiancollege.ca/academics/full-time-programs/office-administration-executive-ofae/',
'https://www.georgiancollege.ca/academics/full-time-programs/pre-service-firefighter-education-and-training-fire/',
'https://www.georgiancollege.ca/academics/full-time-programs/office-administration-general-ofag/',
'https://www.georgiancollege.ca/academics/full-time-programs/practical-nursing-pnrs/',
'https://www.georgiancollege.ca/academics/full-time-programs/office-administration-executive-co-op-ofec/',
'https://www.georgiancollege.ca/academics/full-time-programs/opticianry-co-op-opti/',
'https://www.georgiancollege.ca/academics/full-time-programs/office-administration-health-services-ofah/',
'https://www.georgiancollege.ca/academics/full-time-programs/paralegal-parl/',
'https://www.georgiancollege.ca/academics/full-time-programs/protection-security-and-investigation-psin/',
'https://www.georgiancollege.ca/academics/full-time-programs/public-relations-corporate-communications-prcc/',
'https://www.georgiancollege.ca/academics/full-time-programs/project-management-prjm/',
'https://www.georgiancollege.ca/academics/full-time-programs/research-analyst-co-op-rapp/',
'https://www.georgiancollege.ca/academics/full-time-programs/social-service-worker-sswk/',
'https://www.georgiancollege.ca/academics/full-time-programs/sport-administration-sprt/',
'https://www.georgiancollege.ca/academics/full-time-programs/snow-resort-operations-co-op-srop/',
'https://www.georgiancollege.ca/academics/full-time-programs/therapeutic-recreation-trec/',
'https://www.georgiancollege.ca/academics/full-time-programs/traditional-chinese-medicine-tcmp/',
'https://www.georgiancollege.ca/academics/full-time-programs/veterinary-assistant-veta/',
'https://www.georgiancollege.ca/academics/full-time-programs/veterinary-technician-vetn/',
'https://www.georgiancollege.ca/academics/full-time-programs/tourism-marketing-and-product-development-co-op-tmpd/',
'https://www.georgiancollege.ca/academics/full-time-programs/welding-techniques-wetc/',
'https://www.georgiancollege.ca/academics/full-time-programs/paramedic-para/',
'https://www.georgiancollege.ca/academics/full-time-programs/personal-support-worker-pswr/',
'https://www.georgiancollege.ca/academics/full-time-programs/pharmacy-technician-phrm/',
'https://www.georgiancollege.ca/academics/full-time-programs/recreation-and-leisure-services-co-op-rels/','https://www.georgiancollege.ca/academics/full-time-programs/heating-refrigeration-and-air-conditioning-technician-co-op-hrac/',
'https://www.georgiancollege.ca/academics/full-time-programs/honours-bachelor-of-business-administration-automotive-management-co-op-bbaa/',
'https://www.georgiancollege.ca/academics/full-time-programs/honours-bachelor-of-business-administration-golf-management-co-op-bagm/',
'https://www.georgiancollege.ca/academics/full-time-programs/honours-bachelor-of-police-studies-co-op-baps/',
'https://www.georgiancollege.ca/academics/full-time-programs/hospitality-administration-hotel-and-resort-co-op-hadm/',
'https://www.georgiancollege.ca/academics/full-time-programs/honours-bachelor-of-business-administration-management-and-leadership-co-op-bbml/',
'https://www.georgiancollege.ca/academics/full-time-programs/human-resources-management-co-op-hrmn/',
'https://www.georgiancollege.ca/academics/full-time-programs/honours-bachelor-of-interior-design-co-op-baid/',
'https://www.georgiancollege.ca/academics/full-time-programs/indigenous-community-and-social-development-co-op-icsd/',
'https://www.georgiancollege.ca/academics/full-time-programs/information-systems-security-co-op-inss/',
'https://www.georgiancollege.ca/academics/full-time-programs/interactive-media-design-web-co-op-imdw/',
'https://www.georgiancollege.ca/academics/full-time-programs/interior-decorating-indc/',
'https://www.georgiancollege.ca/academics/full-time-programs/jewellery-and-metals-jmet/',
'https://www.georgiancollege.ca/academics/full-time-programs/kitchen-and-bath-design-kbde/',
'https://www.georgiancollege.ca/academics/full-time-programs/marine-engineering-management-memg/',
'https://www.georgiancollege.ca/academics/full-time-programs/hospitality-hotel-and-resort-operations-management-co-op-hhro/',
'https://www.georgiancollege.ca/academics/full-time-programs/marine-engineering-technology-co-op-mtcy/',
'https://www.georgiancollege.ca/academics/full-time-programs/marine-technology-navigation-co-op-mnav/',
'https://www.georgiancollege.ca/academics/full-time-programs/massage-therapy-masg/',
'https://www.georgiancollege.ca/academics/full-time-programs/mechanical-engineering-technology-co-op-mety/',
'https://www.georgiancollege.ca/academics/full-time-programs/mechanical-techniques-marine-engine-mechanic-mtme/',
'https://www.georgiancollege.ca/academics/full-time-programs/mechanical-technician-precision-skills-co-op-mtps/',
'https://www.georgiancollege.ca/academics/full-time-programs/medical-skin-care-therapies-msct/',
'https://www.georgiancollege.ca/academics/full-time-programs/law-clerk-lclr/',
'https://www.georgiancollege.ca/academics/full-time-programs/mechanical-techniques-small-engine-mechanic-mtse/',
'https://www.georgiancollege.ca/academics/full-time-programs/museum-and-gallery-studies-musm/',
'https://www.georgiancollege.ca/academics/full-time-programs/mechanical-techniques-industrial-maintenance-mtin/',
'https://www.georgiancollege.ca/academics/full-time-programs/mobile-application-development-mdev/',
'https://www.georgiancollege.ca/academics/full-time-programs/occupational-therapist-assistant-and-physiotherapist-assistant-opta/',]

    def parse(self, response):
        item=get_item(ScrapyschoolCanadaCollegeItem)
        item['school_name']='Georgian College'
        item['url']=response.url
        print(response.url)

        #Diploma: approximately $13,500 to $14,500 Degree: approximately $16,500 to $18,500 Graduate certificate: approximately $16,500 to $20,000
        item['apply_fee'],item['apply_pre']='100','$'
        item['location']='Ontario'

        majorname=response.xpath('//header/h1/text()').extract()
        # print(majorname)
        item['major_name_en']=majorname[0].strip()

        degree_name=response.xpath('//strong[contains(text(),"Credential")]/../following-sibling::div/text()').extract()
        # print(degree_name)
        item['degree_name']=degree_name[0]
        degree_name=''.join(degree_name)
        item['tuition_fee_pre'], item['tuition_fee_per'] = '$', '1'
        if 'iploma' in degree_name:
            item['tuition_fee']='13,500'
            item['degree_level']='3'
            item['toefl']='79'
            item['ielts']='6.0'
        if 'egree' in degree_name:
            item['tuition_fee'] = '16,500-18,500'
            item['degree_level']='1'
            item['toefl']='89'
            item['ielts']='6.5'
        if 'raduate Certificate' in degree_name:
            item['tuition_fee']= '16,500-20,000'
            item['degree_level']='2'
            item['toefl']='89'
            item['ielts']='6.5'

        requirement_chinese_en='<ul><li>Senior middle school diploma and Senior middle school transcript</li> <li>Transcripts for all years of study in Senior middle school</li>         <li>Equal to a high school diploma, we accept graduates from secondary vocational training schools</li></ul>'

        overview=response.xpath('//h2[contains(text(),"Program description")]/../following-sibling::*').extract()
        item['overview_en']=remove_class(overview)

        career=response.xpath('//h2[contains(text(),"Career opportunitie")]/../following-sibling::*').extract()
        item['career_en']=remove_class(career)

        entry_requirement=response.xpath('//h2[contains(text(),"Admission information")]/../following-sibling::*').extract()
        item['entry_requirements_en']=remove_class(entry_requirement)

        modules=response.xpath('//h2[contains(text(),"Course")]/../following-sibling::*').extract()
        item['modules_en']=remove_class(modules)

        duration=response.xpath('//strong[text()="Duration"]/../following-sibling::div/text()').extract()
        # print(duration)
        dura=clear_duration(duration)
        # print(dura)
        item['duration']=dura['duration']
        item['duration_per']=dura['duration_per']

        code=response.xpath('//strong[text()="Program code"]/../following-sibling::div/text()').extract()
        item['programme_code']=''.join(code).strip()

        campus=response.xpath('//strong[text()="Campuses"]/../following-sibling::div/a/text()').extract()
        # print(campus)
        item['campus']=','.join(campus)
        start_date=response.xpath('//td[contains(text(),"2019")]/text()').extract()
        # print(start_date)
        start_date=','.join(start_date)
        item['start_date']=start_date.replace('Fall 2019','2019-09').replace('Summer 2019','2019-05').replace('Winter 2019','2019-01')
        yield item
        # for sd in start_date:
        #     # print(sd)
        #     item['start_date']=sd.replace('Fall 2019','2019-09').replace('Summer 2019','2019-05').replace('Winter 2019','2019-01')
        #     campus=response.xpath('//td[text()="%s"]/following-sibling::td/text()'%sd).extract()
        #     # print(campus)
        #     item['campus']=''.join(campus).strip()
        #     yield item