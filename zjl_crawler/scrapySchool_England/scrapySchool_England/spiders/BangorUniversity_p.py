# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/2 16:45'
import scrapy,json
import re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from w3lib.html import remove_tags
from scrapySchool_England.clearSpace import  clear_space_str
class BangorUniversitySpider(scrapy.Spider):
    name = 'BangorUniversity_p'
    allowed_domains = ['bangor.ac.uk/']
    start_urls = []
#     C= [
# 'https://www.bangor.ac.uk/international/courses/postgraduate/acca-qualification',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/accounting-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/accounting-and-banking-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/accounting-and-finance-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/accounting-banking-economics-finance-management-studies-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/banking-and-finance-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/banking-and-finance-mba',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/banking-and-finance-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/banking-and-finance-chartered-banker-bangor--msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/banking-and-finance-chartered-banker-bangor--ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/banking-and-law-mba',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/banking-and-law-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/chartered-banker-mba',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/finance-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/finance-mba',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/investment-management-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/islamic-banking-and-finance-mba',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/islamic-banking-and-finance-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/law-and-banking-llm',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/management-and-finance-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/management-and-finance-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/research-methodolgy-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/biological-sciences-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/biological-sciences-msc-by-research',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/molecular-biology-with-biotechnology-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/business-and-marketing-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/business-with-consumer-psychology-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/business-with-consumer-psychology-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/consumer-psychology-with-business-msc-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/consumer-psychology-with-business-ma-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/international-business-mba',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/international-commercial-and-business-law-llm-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/international-marketing-mba',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/analytical-chemistry-msc-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/chemistry-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/chemistry-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/chemistry-phd',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/advanced-visualization-virtual-environments-and-computer-animation-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/artificial-intelligence-and-intelligent-agents-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/communication-networks-and-protocols-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/computer-science-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/computer-science-with-visualisation-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/image-processing-for-mobile-devices-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/medical-visualization-and-simulation-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/pattern-recognition-classifiers-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/advanced-visualization-virtual-environments-and-computer-animation-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/artificial-intelligence-and-intelligent-agents-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/communication-networks-and-protocols-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/computer-science-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/computer-science-with-visualisation-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/image-processing-for-mobile-devices-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/medical-visualization-and-simulation-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/pattern-recognition-classifiers-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/agricultural-systems-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/agriculture-and-environment-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/agroforestry-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/agroforestry-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/biodiversity-conservation-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/conservation-and-land-management-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/doctor-of-agriculture-and-environment-dagenv-dagenv',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/environmental-and-business-management-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/environmental-forestry-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/environmental-management-mba',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/environmental-sciences-msc-by-research',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/food-security-in-the-changing-environment-msc-distance-learning',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/forest-ecology-and-management-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/forestry-msc-by-distance-learning',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/forestry-and-environmental-management-transfor-m-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/renewable-materials-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/environmental-and-soil-science-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/sustainable-forest-and-nature-management-sufonama-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/sustainable-tropical-forestry-sutrofor-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/tropical-forestry-msc-by-distance-learning',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/tropical-forestry-msc-international-commonwealth-scholarship-distance-learning',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/comparative-criminology-and-criminal-justice-ma-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/criminology-and-criminal-justice-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/criminology-and-law-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/criminology-and-sociology-ma-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/criminology-criminal-justice-social-policy-sociology-mares',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/childhood-and-youth-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/education-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/education-doctorate-programme-edd',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/education-studies-full-time-ma-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/education-studies-part-time-ma-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/primary-education-pgce',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/secondary-education-pgce',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/broadband-and-optical-communications-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electrical-materials-science-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-bio-electronics-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-micromachining-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-microwave-devices-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-nanotechnology-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-optical-communications-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-optoelectronics-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-organic-electronics-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-polymer-electronics-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-vlsi-design-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/laser-micromachining-and-laboratory-on-a-chip-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/nanotechnology-and-microfabrication-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/optical-communications-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/optoelectronics-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/organic-electronics-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/relational-design-masters-by-research',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/broadband-and-optical-communications-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electrical-materials-science-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-bio-electronics-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-micromachining-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-microwave-devices-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-nanotechnology-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-optical-communications-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-optoelectronics-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-organic-electronics-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-polymer-electronics-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-vlsi-design-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/laser-micromachining-and-laboratory-on-a-chip-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/nanotechnology-and-microfabrication-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/optical-communications-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/optoelectronics-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/organic-electronics-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/relational-design-masters-by-research',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/applied-linguistics-for-tefl-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/bilingualism-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/bilingualism-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/language-acquisition-and-development-msc-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/linguistics-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/linguistics-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-phd-mphil-by-practice',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/creative-and-critical-writing-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/creative-writing-ma-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/english-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/english-literature-ma-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/literatures-of-wales-ma-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/medieval-studies-ma-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/film-studies-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/filmmaking-concept-to-screen-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/creative-studies-phd-mphil-practice-led-research',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/creative-studies-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/agroforestry-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/agroforestry-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/environmental-forestry-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/forest-ecology-and-management-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/forestry-msc-by-distance-learning',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/forestry-and-environmental-management-transfor-m-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/sustainable-forest-and-nature-management-sufonama-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/sustainable-tropical-forestry-sutrofor-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/tropical-forestry-msc-by-distance-learning',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/tropical-forestry-msc-international-commonwealth-scholarship-distance-learning',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/european-languages-and-cultures-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/german-studies-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-phd-mphil-by-practice',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/acute-medical-care-pg-cert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/acute-surgical-care-pg-cert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/adult-nursing-pg-dip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/advanced-clinical-practice-msc-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/advanced-clinical-practice-ahp-msc-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/advanced-healthcare-practice-msc-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/advanced-hems-practice-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/ageing-and-dementia-studies-msc-by-research',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/ageing-and-dementia-studies-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/applied-health-research-msc-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/chronic-disease-gradcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/contraception-associated-health-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/intensive-care-nursing-pg-cert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/dementia-studies-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/diabetes-care-and-management-pg-cert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/emergency-practitioner-gradcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/general-practice-nursing-gradcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/health-economics-msc-by-research',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/health-economics-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/health-studies-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/health-services-research-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/leading-quality-improvement-msc-certhe-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/legal-and-ethical-concepts-in-healthcare-pg-cert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/mental-health-pg-cert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/midwifery-studies-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/non-surgical-aesthetic-medicine-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/optimising-breastfeeding-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/optimising-childbirth-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/palliative-care-practice-pg-dip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/professional-doctorate-in-healthcare-doctor-in-healthcare-dhealthcare-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/prudent-healthcare-pg-cert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/public-health-and-health-promotion-msc-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/archaeology-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/celtic-archaeology-ma-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/heritage-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/history-ma-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/history-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/medieval-studies-ma-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/the-celts-ma-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/welsh-history-ma-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/welsh-history-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/y-celtiaid-ma-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/european-languages-and-cultures-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/italian-studies-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-phd-mphil-by-practice',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/european-languages-and-cultures-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/italian-studies-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-phd-mphil-by-practice',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/banking-and-law-mba',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/banking-and-law-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/criminology-and-law-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/international-commercial-and-business-law-llm-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/international-law-international-criminal-law-and-international-human-rights-law-llm',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/international-intellectual-property-law-llm',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/international-law-llm',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/law-llm-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/law-llm-res',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/law-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/law-and-banking-llm',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/law-and-criminology-llm',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/law-and-management-mba',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/law-of-the-sea-llm',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/law-2-year-graduate-conversion-degree-llb',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/maritime-law-llm',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/procurement-law-strategy-and-practice-by-distance-learning-llm',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/public-procurement-law-and-strategy-llm',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/marine-biology-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/international-media-management-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/media-and-practice-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/creative-studies-phd-mphil-practice-led-research',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/creative-studies-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/clinical-sciences-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/genomics--msc-pg-dip-pg-cert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/medical-education-practice-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/medical-molecular-biology-with-genetics-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/medical-sciences-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/molecular-medicine-mres',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/physician-associate-studies-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/20th-and-21st-century-music-ma-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/composition-electroacoustic-composition-sonic-art-mmus-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/music--ma-by-research',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/music-phd-mphil-ma-by-research-mmus-by-research',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/music-ma-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/music-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/music-mmus-by-research',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/music-with-education-',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/performance-mmus-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/applied-marine-geoscience-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/marine-biology-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/marine-environmental-protection-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/marine-renewable-energy-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/ocean-sciences-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/ocean-sciences-msc-by-research',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/physical-oceanography-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/studies-in-philosophy-and-religion-mres-distance-learning',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/philosophy-and-religion-mares-distance-learning',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/philosophy-and-religion-phd-mphil-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/ageing-and-cognitive-health-phd',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/applied-behaviour-analysis-msc-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/business-with-consumer-psychology-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/business-with-consumer-psychology-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/clinical-and-health-psychology-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/clinical-psychology-dclinpsy',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/consumer-psychology-with-business-ma-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/consumer-psychology-with-business-msc-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/counselling-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/mindfulness-based-approaches-3-years--ma-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/mindfulness-based-approaches--ma-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/mindfulness-based-approaches-5-years--msc-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/mindfulness-based-approaches-ma-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/mindfulness-based-approaches-train-to-be-a-mindfulness-teacher-and-get-a-masters-degree--msc-pgdip-pgcert'
# 'https://www.bangor.ac.uk/international/courses/postgraduate/neuroimaging-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/positive-behavioural-support--msc-pgdip-pgcert-',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/principles-of-clinical-neuropsychology-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/psychological-research-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/psychology-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/psychology-phd',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/psychology-mres-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/psychology-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/sport-and-exercise-psychology-mres-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/sport-and-exercise-psychology-bps-accredited-msc',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/teaching-mindfulness-based-courses-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/criminology-and-sociology-ma-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/criminology-criminal-justice-social-policy-sociology-mares',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/gwaith-cymdeithasol-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/polisi-a-chynllunio-ieithyddol--ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/social-research-and-social-policy-ma-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/social-policy-sociology-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/social-work-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/sociology-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/criminology-and-sociology-ma-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/criminology-criminal-justice-social-policy-sociology-mares',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/gwaith-cymdeithasol-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/polisi-a-chynllunio-ieithyddol--ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/social-research-and-social-policy-ma-pgdip-pgcert',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/social-policy-sociology-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/social-work-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/sociology-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/european-languages-and-cultures-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/hispanic-studies-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-phd-mphil-by-practice',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-phd-mphil/international/courses/postgraduate/astudiaethau-celtaidd-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/celtic-studies-astudiaethau-celtaidd-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/cymraeg-ma-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/llenyddiaeth-gymraeg-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/llenyddiaethau-cymru-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/the-celts-ma-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-ma',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-phd-mphil-by-practice',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/welsh-cymraeg-ma-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/welsh-literature-llenyddiaeth-gymraeg-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/y-celtiaid-ma-pgdip',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/ysgrifennu-creadigol-phd-mphil',
# 'https://www.bangor.ac.uk/international/courses/postgraduate/ysgrifennu-creadigol-ma-pgdip']
    # print(len(C))
    C=[
        'https://www.bangor.ac.uk/international/courses/postgraduate/biological-sciences-msc-by-research',
        'https://www.bangor.ac.uk/international/courses/postgraduate/relational-design-masters-by-research',
        'https://www.bangor.ac.uk/international/courses/postgraduate/management-and-finance-ma',
        'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-organic-electronics-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/business-with-consumer-psychology-ma',
        'https://www.bangor.ac.uk/international/courses/postgraduate/environmental-forestry-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/business-and-marketing-ma',
        'https://www.bangor.ac.uk/international/courses/postgraduate/psychological-research-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/law-and-criminology-llm',
        'https://www.bangor.ac.uk/international/courses/postgraduate/public-health-and-health-promotion-msc-pgdip-pgcert',
        'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/public-procurement-law-and-strategy-llm',
        'https://www.bangor.ac.uk/international/courses/postgraduate/maritime-law-llm',
        'https://www.bangor.ac.uk/international/courses/postgraduate/ageing-and-dementia-studies-msc-by-research',
        'https://www.bangor.ac.uk/international/courses/postgraduate/international-business-mba',
        'https://www.bangor.ac.uk/international/courses/postgraduate/law-llm-res',
        'https://www.bangor.ac.uk/international/courses/postgraduate/sociology-ma',
        'https://www.bangor.ac.uk/international/courses/postgraduate/comparative-criminology-and-criminal-justice-ma-pgdip-pgcert',
        'https://www.bangor.ac.uk/international/courses/postgraduate/dementia-studies-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/20th-and-21st-century-music-ma-pgdip-pgcert',
        'https://www.bangor.ac.uk/international/courses/postgraduate/banking-and-finance-chartered-banker-bangor--msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/chemistry-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/islamic-banking-and-finance-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/sustainable-forest-and-nature-management-sufonama-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/language-acquisition-and-development-msc-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/advanced-hems-practice-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-bio-electronics-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/music--ma-by-research',
        'https://www.bangor.ac.uk/international/courses/postgraduate/marine-renewable-energy-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/leading-quality-improvement-msc-certhe-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/management-and-finance-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/agriculture-and-environment-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/european-languages-and-cultures-ma',
        'https://www.bangor.ac.uk/international/courses/postgraduate/banking-and-law-mba',
        'https://www.bangor.ac.uk/international/courses/postgraduate/accounting-and-banking-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/clinical-sciences-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/sport-and-exercise-psychology-bps-accredited-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/international-intellectual-property-law-llm',
        'https://www.bangor.ac.uk/international/courses/postgraduate/molecular-biology-with-biotechnology-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/law-and-management-mba',
        'https://www.bangor.ac.uk/international/courses/postgraduate/forestry-and-environmental-management-transfor-m-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/psychology-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/applied-health-research-msc-pgdip-pgcert',
        'https://www.bangor.ac.uk/international/courses/postgraduate/music-with-education-',
        'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-optoelectronics-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/banking-and-finance-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-nanotechnology-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/bilingualism-ma',
        'https://www.bangor.ac.uk/international/courses/postgraduate/creative-writing-ma-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/sustainable-tropical-forestry-sutrofor-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/translation-studies-ma',
        'https://www.bangor.ac.uk/international/courses/postgraduate/accounting-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/applied-marine-geoscience-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/environmental-management-mba',
        'https://www.bangor.ac.uk/international/courses/postgraduate/positive-behavioural-support--msc-pgdip-pgcert-',
        'https://www.bangor.ac.uk/international/courses/postgraduate/islamic-banking-and-finance-mba',
        'https://www.bangor.ac.uk/international/courses/postgraduate/music-mmus-by-research',
        'https://www.bangor.ac.uk/international/courses/postgraduate/counselling-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/broadband-and-optical-communications-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/media-and-practice-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/genomics--msc-pg-dip-pg-cert',
        'https://www.bangor.ac.uk/international/courses/postgraduate/finance-mba',
        'https://www.bangor.ac.uk/international/courses/postgraduate/applied-behaviour-analysis-msc-pgdip-pgcert',
        'https://www.bangor.ac.uk/international/courses/postgraduate/research-methodolgy-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/music-ma-pgdip-pgcert',
        'https://www.bangor.ac.uk/international/courses/postgraduate/the-celts-ma-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/international-law-llm',
        'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-vlsi-design-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/welsh-history-ma-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/sport-and-exercise-psychology-mres-pgcert',
        'https://www.bangor.ac.uk/international/courses/postgraduate/social-research-and-social-policy-ma-pgdip-pgcert',
        'https://www.bangor.ac.uk/international/courses/postgraduate/medieval-studies-ma-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/psychology-ma',
        'https://www.bangor.ac.uk/international/courses/postgraduate/conservation-and-land-management-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/social-work-ma',
        'https://www.bangor.ac.uk/international/courses/postgraduate/analytical-chemistry-msc-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/composition-electroacoustic-composition-sonic-art-mmus-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/molecular-medicine-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/consumer-psychology-with-business-msc-pgdip-pgcert',
        'https://www.bangor.ac.uk/international/courses/postgraduate/english-literature-ma-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/finance-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/international-marketing-mba',
        'https://www.bangor.ac.uk/international/courses/postgraduate/applied-linguistics-for-tefl-ma',
        'https://www.bangor.ac.uk/international/courses/postgraduate/medical-molecular-biology-with-genetics-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/celtic-archaeology-ma-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/law-2-year-graduate-conversion-degree-llb',
        'https://www.bangor.ac.uk/international/courses/postgraduate/environmental-and-business-management-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/psychology-mres-pgcert',
        'https://www.bangor.ac.uk/international/courses/postgraduate/non-surgical-aesthetic-medicine-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/investment-management-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/international-law-international-criminal-law-and-international-human-rights-law-llm',
        'https://www.bangor.ac.uk/international/courses/postgraduate/banking-and-finance-ma',
        'https://www.bangor.ac.uk/international/courses/postgraduate/childhood-and-youth-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/computer-science-with-visualisation-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/ocean-sciences-msc-by-research',
        'https://www.bangor.ac.uk/international/courses/postgraduate/linguistics-ma',
        'https://www.bangor.ac.uk/international/courses/postgraduate/education-studies-full-time-ma-pgdip-pgcert',
        'https://www.bangor.ac.uk/international/courses/postgraduate/advanced-clinical-practice-msc-pgdip-pgcert',
        'https://www.bangor.ac.uk/international/courses/postgraduate/international-commercial-and-business-law-llm-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/banking-and-law-ma',
        'https://www.bangor.ac.uk/international/courses/postgraduate/advanced-healthcare-practice-msc-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/advanced-clinical-practice-ahp-msc-pgdip-pgcert',
        'https://www.bangor.ac.uk/international/courses/postgraduate/computer-science-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-polymer-electronics-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/agroforestry-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/advanced-visualization-virtual-environments-and-computer-animation-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/marine-biology-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/criminology-and-law-ma',
        'https://www.bangor.ac.uk/international/courses/postgraduate/law-and-banking-llm',
        'https://www.bangor.ac.uk/international/courses/postgraduate/environmental-sciences-msc-by-research',
        'https://www.bangor.ac.uk/international/courses/postgraduate/banking-and-finance-chartered-banker-bangor--ma',
        'https://www.bangor.ac.uk/international/courses/postgraduate/film-studies-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/filmmaking-concept-to-screen-ma',
        'https://www.bangor.ac.uk/international/courses/postgraduate/performance-mmus-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/mindfulness-based-approaches-ma-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/exercise-rehabilitation-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/nanotechnology-and-microfabrication-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/arthurian-literature-ma-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/criminology-and-sociology-ma-pgdip-pgcert',
        'https://www.bangor.ac.uk/international/courses/postgraduate/applied-sport-and-exercise-physiology-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/applied-sport-science-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/literatures-of-wales-ma-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/information-management-mba',
        'https://www.bangor.ac.uk/international/courses/postgraduate/business-with-consumer-psychology-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/neuroimaging-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-optical-communications-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/principles-of-clinical-neuropsychology-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/clinical-and-health-psychology-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-micromachining-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/accounting-and-finance-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/criminology-criminal-justice-social-policy-sociology-mares',
        'https://www.bangor.ac.uk/international/courses/postgraduate/banking-and-finance-mba',
        'https://www.bangor.ac.uk/international/courses/postgraduate/welsh-cymraeg-ma-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/international-media-management-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/health-economics-msc-by-research',
        'https://www.bangor.ac.uk/international/courses/postgraduate/chartered-banker-mba',
        'https://www.bangor.ac.uk/international/courses/postgraduate/consumer-psychology-with-business-ma-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/electronic-engineering-microwave-devices-mres',
        'https://www.bangor.ac.uk/international/courses/postgraduate/marine-environmental-protection-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/physical-oceanography-msc',
        'https://www.bangor.ac.uk/international/courses/postgraduate/law-llm-pgdip',
        'https://www.bangor.ac.uk/international/courses/postgraduate/law-of-the-sea-llm',
        'https://www.bangor.ac.uk/international/courses/postgraduate/history-ma-pgdip'
    ]
    C=set(C)
    # print(len(C))
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'Bangor University'
        # print(university)

        #2.url
        url = response.url

        #3.overview_en
        overview_en = response.xpath('//*[@id="overview"]').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #4.programme_en
        programme_en = response.xpath('//*[@id="contents"]/h1/text()').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #5.degree_type
        degree_type = 2

        #6.degree_name
        degree_name = response.xpath('//*[@id="contents"]/h1/span').extract()
        degree_name =''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #7.duration
        duration_list =response.xpath('//*[@id="sidepanel"]/ul/li[3]').extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        duration_list = duration_list.replace('One','1')
        try:
            duration_int = re.findall('\d+',duration_list)[0]
        except:
            duration_int = None
        try:
            if int(duration_int) > 5:
                duration_per = 3
            else :
                duration_per = 1
        except:
            duration_per = None
        duration = duration_int
        # print(duration,'*********',duration_per)

        #8.modules_en
        modules_en = response.xpath('//*[@id="content"]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        modules_en = clear_space_str(modules_en)
        # print(modules_en)

        #9.rntry_requirements
        rntry_requirements = response.xpath('//*[@id="requirements"]').extract()
        rntry_requirements = ''.join(rntry_requirements)
        rntry_requirements = clear_space_str(rntry_requirements)
        rntry_requirements = remove_class(rntry_requirements)
        # print(rntry_requirements)

        #10.ielts,11,12,13,14
        ielts_list = re.findall('[5-7]\.\d',rntry_requirements)
        # print(ielts_list)
        if len(ielts_list) == 3:
            ielts = ielts_list[0]
            ielts_w = ielts_list[1]
            ielts_r = ielts_list[2]
            ielts_s = ielts_list[2]
            ielts_l = ielts_list[2]
        elif len(ielts_list) == 2:
            ielts = ielts_list[0]
            ielts_w = ielts_list[1]
            ielts_r = ielts_list[1]
            ielts_s = ielts_list[1]
            ielts_l = ielts_list[1]
        elif len(ielts_list) == 5:
            ielts = 7.0
            ielts_w = 6.5
            ielts_r = 6.5
            ielts_s = 6.5
            ielts_l = 6.5
        elif len(ielts_list) == 1:
            ielts = ielts_list[0]
            ielts_w = ielts_list[0]
            ielts_r = ielts_list[0]
            ielts_s = ielts_list[0]
            ielts_l = ielts_list[0]
        else:
            ielts = 6.5
            ielts_w = 6.0
            ielts_r = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
        # print(ielts,ielts_l,ielts_s,ielts_w,ielts_r)

        #15.require_chinese_en
        require_chinese_en = "Minimum of 65% in undergraduate programme from a recognised university in China (211 university) OR Minimum of 70% in undergraduate programme from a recognised university in China (non 211 university)"
        require_chinese_en +='Mature students will be considered on a case by case basis.'
        require_chinese_en +='If you do not meet the requirements for entry onto a Masters Degree in Bangor Business School then we can consider you for entry onto *International Incorporated Masters '
        require_chinese_en = clear_space_str(require_chinese_en)

        #16.career_en
        career_en = response.xpath('//*[@id="employability"]').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        career_en =clear_space_str(career_en)
        # print(career_en)

        #17.teach_time
        teach_time = 'Full time'

        #18.teach_type
        if 'MPhil' in degree_name:
            teach_type = 'Research'
        elif 'Phd' in degree_name:
            teach_type = 'Research'
        else:
            teach_type = 'Taught'

        #19.tuition_fee_pre
        tuition_fee_pre = '£'

        #20.apply_proces_en
        apply_proces_en = 'https://www.bangor.ac.uk/international/applying/'

        #21.deadline
        deadline = '2018-6-30,2018-10-30'

        #22.location
        location = 'Wales'

        #23.other
        other = 'https://www.bangor.ac.uk/international/future/Finance_and_scholarship.php'
        #24.apply_pre
        apply_pre = '£'


        item['other'] = other
        item['university'] = university
        item['url'] = url
        item['overview_en'] = overview_en
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['modules_en'] = modules_en
        item['rntry_requirements'] = rntry_requirements
        item['ielts'] = ielts
        item['ielts_w'] = ielts_w
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['require_chinese_en'] = require_chinese_en
        item['career_en'] = career_en
        item['teach_time'] = teach_time
        item['teach_type'] = teach_type
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_proces_en'] = apply_proces_en
        item['deadline'] = deadline
        item['location'] = location
        yield item