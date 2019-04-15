# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/12/18 10:30'
from w3lib.html import remove_tags
import scrapy,json
import re
from scrapySchool_Canada_College.middlewares import *
from scrapySchool_Canada_College.getItem import get_item
from scrapySchool_Canada_College.items import ScrapyschoolCanadaCollegeItem
from lxml import etree
import requests
class FanshaweCollege_CSpider(scrapy.Spider):
    name = 'FanshaweCollege_C'
    allowed_domains = ['fanshawec.ca/']
    start_urls = []
    C= [
        'https://www.fanshawec.ca/programs/anc1-3d-animation-and-character-design',
        'https://www.fanshawec.ca/programs/abk1-advanced-baker-patissier',
        'https://www.fanshawec.ca/programs/adp2-advanced-care-paramedic',
        'https://www.fanshawec.ca/programs/adc1-advanced-communication-professionals',
        'https://www.fanshawec.ca/programs/ade1-advanced-ergonomic-studies',
        'https://www.fanshawec.ca/programs/afm2-advanced-filmmaking',
        'https://www.fanshawec.ca/programs/ale1-advanced-law-enforcement-investigations-security',
        'https://www.fanshawec.ca/programs/aps2-advanced-police-studies',
        'https://www.fanshawec.ca/programs/ael1j-adventure-expeditions-and-interpretive-leadership',
        'https://www.fanshawec.ca/programs/agm2-agri-business-management',
        'https://www.fanshawec.ca/programs/agm1j-agri-business-management',
        'https://www.fanshawec.ca/programs/jda2-agricultural-equipment-technician-john-deere-tech-apprenticeship',
        'https://www.fanshawec.ca/programs/fet2-agricultural-equipment-technician-block-release-apprenticeship',
        'https://www.fanshawec.ca/programs/4067-aircraft-structural-repair-technician',
        'https://www.fanshawec.ca/programs/ana2-anesthesia-assistant',
        'https://www.fanshawec.ca/programs/amf1-applied-aerospace-manufacturing',
        'https://www.fanshawec.ca/programs/amf2-applied-aerospace-manufacturing',
        'https://www.fanshawec.ca/programs/amd2-applied-mechanical-design',
        'https://www.fanshawec.ca/programs/aty1-architectural-technology',
        'https://www.fanshawec.ca/programs/ata2-artisanal-culinary-arts',
        'https://www.fanshawec.ca/programs/apr1-audio-post-production',
        'https://www.fanshawec.ca/programs/aut1-autism-and-behavioural-science',
        'https://www.fanshawec.ca/programs/aut3-autism-and-behavioural-science-weekend',
        'https://www.fanshawec.ca/programs/abc5-auto-body-and-collision-damage-repairer-branch-i-block-release-apprenticeship',
        'https://www.fanshawec.ca/programs/abt1-auto-body-repair-techniques',
        'https://www.fanshawec.ca/programs/abr3-auto-body-repairer-apprentice-branch-ii-block-release-apprenticeship',
        'https://www.fanshawec.ca/programs/ast4-automotive-service-technician-day-release-apprenticeship',
        'https://www.fanshawec.ca/programs/mma3-automotive-service-technician-gm-asep-apprenticeship',
        'https://www.fanshawec.ca/programs/ast5-automotive-service-technician-apprenticeship',
        'https://www.fanshawec.ca/programs/aam3-aviation-technician-aircraft-maintenance',
        'https://www.fanshawec.ca/programs/aam4-aviation-technician-aircraft-maintenance-co-op',
        'https://www.fanshawec.ca/programs/avm3-aviation-technician-avionics-maintenance',
        'https://www.fanshawec.ca/programs/avm4-aviation-technician-avionics-maintenance-co-op',
        'https://www.fanshawec.ca/programs/avi1-aviation-technology-aircraft-maintenance-and-avionics',
        'https://www.fanshawec.ca/programs/avi2-aviation-technology-aircraft-maintenance-and-avionics-co-op',
        'https://www.fanshawec.ca/programs/bpm2-baking-and-pastry-arts-management',
        'https://www.fanshawec.ca/programs/bim2-bim-and-integrated-practice',
        'https://www.fanshawec.ca/programs/bma1-brick-and-stone-mason-block-release-apprenticeship',
        'https://www.fanshawec.ca/programs/tvn1-broadcast-journalism-television-news',
        'https://www.fanshawec.ca/programs/brr2-broadcasting-radio',
        'https://www.fanshawec.ca/programs/brt3-broadcasting-television-and-film-production',
        'https://www.fanshawec.ca/programs/bry1-building-renovation-technology',
        'https://www.fanshawec.ca/programs/bus1-business',
        'https://www.fanshawec.ca/programs/bus2-business-co-op',
        'https://www.fanshawec.ca/programs/bac2-business-accounting',
        'https://www.fanshawec.ca/programs/bac4-business-accounting-co-op',
        'https://www.fanshawec.ca/programs/bem2w-business-entrepreneurship-and-management',
        'https://www.fanshawec.ca/programs/bem3c-business-entrepreneurship-and-management-accelerated',
        'https://www.fanshawec.ca/programs/bfn4-business-finance',
        'https://www.fanshawec.ca/programs/bfn5-business-finance-co-op',
        'https://www.fanshawec.ca/programs/bhr1-business-human-resources',
        'https://www.fanshawec.ca/programs/bin3-business-insurance',
        'https://www.fanshawec.ca/programs/bin5-business-insurance-co-op',
        'https://www.fanshawec.ca/programs/bls1-business-logistics-and-supply-chain-management',
        'https://www.fanshawec.ca/programs/bls2-business-logistics-and-supply-chain-management-co-op',
        'https://www.fanshawec.ca/programs/bmk1-business-marketing',
        'https://www.fanshawec.ca/programs/bmk2-business-marketing-co-op',
        'https://www.fanshawec.ca/programs/bpb1-business-payroll-and-bookkeeping',
        'https://www.fanshawec.ca/programs/bpb2-business-payroll-and-bookkeeping-co-op',
        'https://www.fanshawec.ca/programs/baa2-business-administration-accounting',
        'https://www.fanshawec.ca/programs/bah1-business-administration-human-resources',
        'https://www.fanshawec.ca/programs/bal1-business-administration-leadership-and-management',
        'https://www.fanshawec.ca/programs/bam2-business-administration-marketing',
        'https://www.fanshawec.ca/programs/ban1-business-analysis',
        'https://www.fanshawec.ca/programs/bfs2-business-fundamentals',
        'https://www.fanshawec.ca/programs/enp2-business-fundamentals-entrepreneurship',
        'https://www.fanshawec.ca/programs/crt1-carpentry-and-renovation-technician',
        'https://www.fanshawec.ca/programs/crq1-carpentry-and-renovation-techniques',
        'https://www.fanshawec.ca/programs/clt1-chemical-laboratory-technology-science-laboratory',
        'https://www.fanshawec.ca/programs/cyw4-child-and-youth-care',
        'https://www.fanshawec.ca/programs/cyw5-child-and-youth-care-fast-track',
        'https://www.fanshawec.ca/programs/cdp1-child-development-practitioner-apprenticeship',
        'https://www.fanshawec.ca/programs/cey2-civil-engineering-technology',
        'https://www.fanshawec.ca/programs/nsg3-collaborative-nursing',
        'https://www.fanshawec.ca/programs/cit2-community-integration-through-co-operative-education',
        'https://www.fanshawec.ca/programs/rpa1-community-pharmacy-assistant',
        'https://www.fanshawec.ca/programs/cpa2-computer-programmer-analyst',
        'https://www.fanshawec.ca/programs/ctn2-computer-systems-technician',
        'https://www.fanshawec.ca/programs/cty1-computer-systems-technology',
        'https://www.fanshawec.ca/programs/cty2-computer-systems-technology',
        'https://www.fanshawec.ca/programs/ccq3-construction-carpentry-techniques',
        'https://www.fanshawec.ca/programs/cmy2-construction-engineering-technology',
        'https://www.fanshawec.ca/programs/cpj2-construction-project-management',
        'https://www.fanshawec.ca/programs/cmt-contemporary-media-theory-and-production',
        'https://www.fanshawec.ca/programs/coa2-cook-ii-apprenticeship',
        'https://www.fanshawec.ca/programs/tcs2-costume-production',
        'https://www.fanshawec.ca/programs/clm4-culinary-management',
        'https://www.fanshawec.ca/programs/clm5-culinary-management-apprentice',
        'https://www.fanshawec.ca/programs/chf2-culinary-skills',
        'https://www.fanshawec.ca/programs/csi1-customer-service-fundamentals-insurance',
        'https://www.fanshawec.ca/programs/cyb1-cyber-security',
        'https://www.fanshawec.ca/programs/das3-dental-assisting-levels-i-and-ii',
        'https://www.fanshawec.ca/programs/dhy3-dental-hygiene',
        'https://www.fanshawec.ca/programs/dfn1-design-foundations',
        'https://www.fanshawec.ca/programs/dsw1-developmental-services-worker',
        'https://www.fanshawec.ca/programs/dsw5j-developmental-services-worker-accelerated',
        'https://www.fanshawec.ca/programs/dsw4-developmental-services-worker-fast-track',
        'https://www.fanshawec.ca/programs/dsa1-developmental-services-worker-apprentice-apprenticeship',
        'https://www.fanshawec.ca/programs/dla1-doula-studies',
        'https://www.fanshawec.ca/programs/ece1-early-childhood-education',
        'https://www.fanshawec.ca/programs/ece5j-early-childhood-education-accelerated',
        'https://www.fanshawec.ca/programs/ece6-early-childhood-education-fast-track',
        'https://www.fanshawec.ca/programs/ece7-early-childhood-education-fast-track-weekend',
        'https://www.fanshawec.ca/programs/eln2-electrical-engineering-technician',
        'https://www.fanshawec.ca/programs/ely7-electrical-engineering-technology',
        'https://www.fanshawec.ca/programs/ely6-electrical-engineering-technology-co-op',
        'https://www.fanshawec.ca/programs/elt1-electrical-techniques',
        'https://www.fanshawec.ca/programs/ela5-electrician-construction-and-maintenance-block-release-apprenticeship',
        'https://www.fanshawec.ca/programs/emn3-electromechanical-engineering-technician',
        'https://www.fanshawec.ca/programs/emn2-electromechanical-engineering-technician-coop',
        'https://www.fanshawec.ca/programs/esd2-electronics-and-embedded-systems-development',
        'https://www.fanshawec.ca/programs/eic3s-electronics-engineering-technician-industrial-controls',
        'https://www.fanshawec.ca/programs/emg2-emergency-management',
        'https://www.fanshawec.ca/programs/emt1-emergency-telecommunications',
        'https://www.fanshawec.ca/programs/ent1-environmental-technology',
        'https://www.fanshawec.ca/programs/dfs4-fashion-design',
        'https://www.fanshawec.ca/programs/fmc3-fashion-marketing-and-management',
        'https://www.fanshawec.ca/programs/fwm-finance-and-wealth-management',
        'https://www.fanshawec.ca/programs/fas1-fine-art',
        'https://www.fanshawec.ca/programs/faf1-fine-art-foundation',
        'https://www.fanshawec.ca/programs/fse1-fire-inspection-and-fire-safety-education',
        'https://www.fanshawec.ca/programs/fss1-fire-safety-systems',
        'https://www.fanshawec.ca/programs/fhp1-fitness-and-health-promotion',
        'https://www.fanshawec.ca/programs/fbm7-food-and-beverage-management',
        'https://www.fanshawec.ca/programs/fbm8-food-and-beverage-management-co-op',
        'https://www.fanshawec.ca/programs/vgd2-game-design',
        'https://www.fanshawec.ca/programs/gdp1-game-development-advanced-programming',
        'https://www.fanshawec.ca/programs/gap5-general-arts-and-science-1-year-english-language-studies',
        'https://www.fanshawec.ca/programs/gap6-general-arts-and-science-one-year-co-op',
        'https://www.fanshawec.ca/programs/gap1-general-arts-and-science-one-year',
        'https://www.fanshawec.ca/programs/cga2-general-carpenter-block-release-apprenticeship',
        'https://www.fanshawec.ca/programs/gmc2s-general-machinist-block-and-day-release-apprenticeship',
        'https://www.fanshawec.ca/programs-and-courses/program/pmc21-general-machinist-apprenticeship',
        'https://www.fanshawec.ca/programs/gis1-geographic-information-systems-gis',
        'https://www.fanshawec.ca/programs/gip2-gerontology-interprofessional-practice',
        'https://www.fanshawec.ca/programs/urp2-gis-and-urban-planning',
        'https://www.fanshawec.ca/programs/grm3-golf-and-club-management',
        'https://www.fanshawec.ca/programs/grm2-golf-and-club-management-co-op',
        'https://www.fanshawec.ca/programs/grd1-graphic-design',
        'https://www.fanshawec.ca/programs/cgs2-guest-relations-management-concierge-specialist',
        'https://www.fanshawec.ca/programs/has1w-hair-stylist',
        'https://www.fanshawec.ca/programs/hsa1w-hairstylist-apprentice-apprenticeship',
        'https://www.fanshawec.ca/programs/hsy2-health-systems-management',
        'https://www.fanshawec.ca/programs/mht2w-heating-refrigeration-and-air-conditioning-technician',
        'https://www.fanshawec.ca/programs/het2-heavy-duty-equipment-technician-apprenticeship',
        'https://www.fanshawec.ca/programs/bio2-honours-bachelor-applied-technology-biotechnology',
        'https://www.fanshawec.ca/programs/bca1-honours-bachelor-commerce-accounting',
        'https://www.fanshawec.ca/programs/bdm1-honours-bachelor-commerce-digital-marketing',
        'https://www.fanshawec.ca/programs/bhm1-honours-bachelor-commerce-human-resources-management',
        'https://www.fanshawec.ca/programs/bcm1-honours-bachelor-commerce-management',
        'https://www.fanshawec.ca/programs/ecl1-honours-bachelor-early-childhood-leadership',
        'https://www.fanshawec.ca/programs/bed1-honours-bachelor-environmental-design-and-planning',
        'https://www.fanshawec.ca/programs/bid1-honours-bachelor-interior-design',
        'https://www.fanshawec.ca/programs/hta2-horticultural-technician-apprentice-block-release-apprenticeship',
        'https://www.fanshawec.ca/programs/htn1-horticulture-technician',
        'https://www.fanshawec.ca/programs/hmt7-hospitality-hotel-and-resort-services-management',
        'https://www.fanshawec.ca/programs/hmt8-hospitality-hotel-and-resort-services-management-co-op',
        'https://www.fanshawec.ca/programs/thm2-hospitality-and-tourism-management',
        'https://www.fanshawec.ca/programs/thm1-hospitality-and-tourism-operations-management',
        'https://www.fanshawec.ca/programs/hmg1-human-resources-management',
        'https://www.fanshawec.ca/programs/hsf1-human-services-foundation',
        'https://www.fanshawec.ca/programs/iea1-industrial-electrician-apprentice-block-release-apprenticeship',
        'https://www.fanshawec.ca/programs/ima3s-industrial-mechanic-millwright-block-day-release-apprenticeship',
        'https://www.fanshawec.ca/programs/ism1-information-security-management',
        'https://www.fanshawec.ca/programs/ico1-institutional-cook-apprenticeship',
        'https://www.fanshawec.ca/programs/irm1-insurance-and-risk-management',
        'https://www.fanshawec.ca/programs/idp3-interactive-media-design',
        'https://www.fanshawec.ca/programs/vis1-interactive-media-development-3d-visualization',
        'https://www.fanshawec.ca/programs/ims1-interactive-media-specialist',
        'https://www.fanshawec.ca/programs/itd1-interior-decorating',
        'https://www.fanshawec.ca/programs/itb1-international-business-management',
        'https://www.fanshawec.ca/programs/iwd1-internet-applications-and-web-development',
        'https://www.fanshawec.ca/programs/brj1-journalism-broadcast',
        'https://www.fanshawec.ca/programs/dls4-landscape-design',
        'https://www.fanshawec.ca/programs/lck1-law-clerk',
        'https://www.fanshawec.ca/programs/lck2-law-clerk-co-op',
        'https://www.fanshawec.ca/programs/scm1-logistics-and-supply-chain-management',
        'https://www.fanshawec.ca/programs/mri1-magnetic-resonance-imaging',
        'https://www.fanshawec.ca/programs/men4-manufacturing-engineering-technician',
        'https://www.fanshawec.ca/programs/men1-manufacturing-engineering-technician-co-op',
        'https://www.fanshawec.ca/programs/mey4-manufacturing-engineering-technology',
        'https://www.fanshawec.ca/programs/mey1-manufacturing-engineering-technology-co-op',
        'https://www.fanshawec.ca/programs/mkm1-marketing-management',
        'https://www.fanshawec.ca/programs/msg2-massage-therapy-accelerated',
        'https://www.fanshawec.ca/programs/mim2s-mechanical-engineering-technician-industrial-maintenance',
        'https://www.fanshawec.ca/programs/mnc1s-mechanical-technician-cnccam',
        'https://www.fanshawec.ca/programs/tdi1s-mechanical-technician-tool-and-die',
        'https://www.fanshawec.ca/programs/mqc1s-mechanical-techniques-cnc',
        'https://www.fanshawec.ca/programs/mrt1-medical-radiation-technology',
        'https://www.fanshawec.ca/programs/mta7-motive-power-technician-automotive',
        'https://www.fanshawec.ca/programs/mta8-motive-power-technician-automotive-apprentice',
        'https://www.fanshawec.ca/programs/mtd7-motive-power-technician-diesel',
        'https://www.fanshawec.ca/programs/mtd8-motive-power-technician-diesel-apprentice',
        'https://www.fanshawec.ca/programs/mia2-music-industry-arts',
        'https://www.fanshawec.ca/programs/mra-music-recording-arts',
        'https://www.fanshawec.ca/programs/nsa1-network-and-security-architecture',
        'https://www.fanshawec.ca/programs/fnm2-nutrition-and-food-service-management',
        'https://www.fanshawec.ca/programs/opa1-occupational-therapist-assistant-and-physiotherapist-assistant',
        'https://www.fanshawec.ca/programs/oae3-office-administration-executive',
        'https://www.fanshawec.ca/programs/oag1-office-administration-general',
        'https://www.fanshawec.ca/programs/oam4-office-administration-health-services',
        'https://www.fanshawec.ca/programs/opm2-operations-management',
        'https://www.fanshawec.ca/programs/plg1-paralegal',
        'https://www.fanshawec.ca/programs/par2-paramedic',
        'https://www.fanshawec.ca/programs/ptp1-parts-technician-pre-apprentice',
        'https://www.fanshawec.ca/programs/psw6-personal-support-worker',
        'https://www.fanshawec.ca/programs/psw9-personal-support-worker-weekend',
        'https://www.fanshawec.ca/programs/ptn1-pharmacy-technician',
        'https://www.fanshawec.ca/programs/pht1-photography',
        'https://www.fanshawec.ca/programs/pha3-photography-advanced',
        'https://www.fanshawec.ca/programs/pla2-plumbing-apprentice-block-release-apprenticeship',
        'https://www.fanshawec.ca/programs/plq1-plumbing-techniques',
        'https://www.fanshawec.ca/programs/pft1-police-foundations',
        'https://www.fanshawec.ca/programs/pft2w-police-foundations-accelerated',
        'https://www.fanshawec.ca/programs/peq1s-power-engineering-techniques-4th-class',
        'https://www.fanshawec.ca/programs/pem1-practical-elements-mechanical-engineering',
        'https://www.fanshawec.ca/programs/png5-practical-nursing',
        'https://www.fanshawec.ca/programs/phs2-pre-health-sciences-pathway-advanced-diplomas-and-degrees',
        'https://www.fanshawec.ca/programs/pmd1-pre-media',
        'https://www.fanshawec.ca/programs/prt1-pre-technology',
        'https://www.fanshawec.ca/programs/pac1-professional-accounting',
        'https://www.fanshawec.ca/programs/fsp1-professional-financial-services',
        'https://www.fanshawec.ca/programs/prj1-project-management',
        'https://www.fanshawec.ca/programs/psi1-protection-security-and-investigation',
        'https://www.fanshawec.ca/programs/cor3-public-relations-corporate-communications',
        'https://www.fanshawec.ca/programs/psf1-public-safety-fundamentals',
        'https://www.fanshawec.ca/programs/psl1-public-safety-leadership',
        'https://www.fanshawec.ca/programs/rld2-recreation-and-leisure-services',
        'https://www.fanshawec.ca/programs/rps1-remotely-piloted-aerial-systems-commercial-operations',
        'https://www.fanshawec.ca/programs/ret2s-renewable-energies-technician',
        'https://www.fanshawec.ca/programs/ret3s-renewable-energies-technician-co-op',
        'https://www.fanshawec.ca/programs/res1-research-and-evaluation',
        'https://www.fanshawec.ca/programs/res2-research-and-evaluation-co-op',
        'https://www.fanshawec.ca/programs/ras2w-residential-air-conditioning-systems-mechanic-apprentice-block-release-apprenticeship',
        'https://www.fanshawec.ca/programs/rst4-respiratory-therapy',
        'https://www.fanshawec.ca/programs/rmp1-retail-meat-cutter-pre-apprentice',
        'https://www.fanshawec.ca/programs/rrm1-retirement-residence-management',
        'https://www.fanshawec.ca/programs/sma2-sheet-metal-apprentice-block-release-apprenticeship',
        'https://www.fanshawec.ca/programs/ssw1-social-service-worker',
        'https://www.fanshawec.ca/programs/ssw2-social-service-worker-fast-track',
        'https://www.fanshawec.ca/programs/sst3-software-and-information-systems-testing-co-op',
        'https://www.fanshawec.ca/programs/sep1-special-events-planning',
        'https://www.fanshawec.ca/programs/thp2-theatre-arts-performance',
        'https://www.fanshawec.ca/programs/thr1-theatre-arts-technical-production',
        'https://www.fanshawec.ca/programs/tdm2s-tool-and-die-maker-block-and-day-release-apprenticeship',
        'https://www.fanshawec.ca/programs/ttc6-tourism-travel',
        'https://www.fanshawec.ca/programs/tts1-tourism-travel-studies',
        'https://www.fanshawec.ca/programs/tct4-truck-and-coach-technician-block-release-apprenticeship',
        'https://www.fanshawec.ca/programs/tct3-truck-and-coach-technician-day-release-apprenticeship',
        'https://www.fanshawec.ca/programs/vee1-visual-effects-and-editing-contemporary-media',
        'https://www.fanshawec.ca/programs/wtq1j-welding-techniques'
    ]
    for i in C:
        start_urls.append(i)

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaCollegeItem)

        #1.school_name
        school_name = 'Fanshawe College'
        # print(school_name)

        #2.url
        url = response.url
        # print(url)

        #3.location
        location = 'Ontario, Canada'

        #4.major_name_en
        major_name_en = response.xpath('//*[@id="page-title"]').extract()
        major_name_en = ''.join(major_name_en)
        major_name_en = remove_tags(major_name_en)
        # print(major_name_en)

        #5.overview_en
        overview_en = response.xpath('//*[@id="group_overview"]/div/div/div/div/p').extract()[:-1]
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #6.campus
        campus = response.xpath('//*[@id="group_more_info"]/div/div[1]/div/div/div[3]/em').extract()
        campus = ''.join(campus)
        campus = remove_tags(campus)
        campus =  re.findall('Campus Code:(.*?)September',campus)
        campus = clear_space_list(campus)
        campus = ','.join(campus).replace('\xa0','')
        # print(campus)

        #7.start_date
        start_date = response.xpath('//*[@id="block-views-program-displays-pr-overview-bl"]/div/div/div[2]').extract()
        start_date = ''.join(start_date)
        start_date = remove_tags(start_date)
        start_date = re.findall('(2.*)',start_date)
        start_date = clear_space_list(start_date)
        start_date = set(start_date)
        start_date = ','.join(start_date).replace(' January','-01').replace(' February','-02').replace(' March','-03').replace(' April','-04').replace(' May','-05').replace(' June','-06').replace(' July','-07').replace(' August','-08').replace(' September','-09').replace(' October','-10').replace(' November','-11')
        # print(start_date,url)

        #8.degree_name 待修改
        degree_name = response.xpath("//strong[contains(text(),'Credential')]//following-sibling::*").extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name,url)

        #9.programme_code
        programme_code = response.xpath("//strong[contains(text(),'Program Code')]//following-sibling::*").extract()
        programme_code = ''.join(programme_code)
        programme_code = remove_tags(programme_code)
        # print(programme_code)

        #10.department
        department = response.xpath("//strong[contains(text(),'Academic School')]//following-sibling::*").extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #11.duration
        duration = response.xpath("//strong[contains(text(),'Duration Next')]//following-sibling::*").extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        try:
            duration = re.findall('\d+',duration)[0]
        except:
            duration  = None
        # print(duration,url)

        #12.duration_per
        duration_per = 4

        #13.modules_en
        modules_en = response.xpath('//*[@id="group_courses"]/div').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #14.career_en
        career_en = response.xpath('//*[@id="group_careers"]/div').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #15.entry_requirements_en
        entry_requirements_en = response.xpath('//*[@id="group_admission"]/div').extract()
        entry_requirements_en = ''.join(entry_requirements_en)
        entry_requirements_en = remove_class(entry_requirements_en)
        # print(entry_requirements_en)

        #16.apply_fee
        apply_fee = 100

        #17.apply_pre
        apply_pre = 'CAD$'

        #18.ielts_desc 1920212223
        ielts_desc = 'Overall score of 6.0 with no score less than 5.5 in any of the four bands'
        ielts = 6.0
        ielts_r = 5.5
        ielts_w = 5.5
        ielts_l = 5.5
        ielts_s = 5.5

        #24.toefl_desc 25
        toefl_desc = '550 paper-based test, 79 internet-based test'
        toefl = 79

        #26.tuition_fee_pre
        tuition_fee_pre = 'CAD$'

        #27.other
        other = 'deadline,中国学生要求，degree_name需要拆分，学费需要pdf匹配'

        item['school_name'] = school_name
        item['url'] = url
        item['location'] = location
        item['major_name_en'] = major_name_en
        item['overview_en'] = overview_en
        item['campus'] = campus
        item['start_date'] = start_date
        item['degree_name'] = degree_name
        item['programme_code'] = programme_code
        item['department'] = department
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['entry_requirements_en'] = entry_requirements_en
        item['apply_fee'] = apply_fee
        item['apply_pre'] = apply_pre
        item['ielts_desc'] = ielts_desc
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['ielts_w'] = ielts_w
        item['toefl_desc'] = toefl_desc
        item['toefl'] = toefl
        item['tuition_fee_pre'] = tuition_fee_pre
        item['other'] = other
        yield item