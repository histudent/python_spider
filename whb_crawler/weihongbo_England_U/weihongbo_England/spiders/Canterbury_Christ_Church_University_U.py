import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'Canterbury_Christ_Church_University_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
#     C = ['https://www.canterbury.ac.uk/study-here/courses/undergraduate/accelerated-degree-accounting-bsc-hons-at-bromley-college-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-bsc-hons-at-bromley-college-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-finance-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-finance-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-and-management-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-and-management-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/advertising-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/advertising-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/american-studies-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/american-studies-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/animal-science-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/animal-science-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/applied-criminology-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/applied-criminology-19-20.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/applied-practice-health-and-social-care-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/archaeology-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/archaeology-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/biochemistry-and-biological-chemistry-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/biochemistry-and-biological-chemistry-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/biology-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/biology-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/biomolecular-science-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/biomolecular-science-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-accelerated-degree-bsc-hons-at-london-south-east-colleges-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/businessmanagement-fd-at-london-south-east-colleges-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-information-systems-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-management-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-management-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-bsc-hons-at-london-south-east-colleges-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-studies-bromley-college-top-up-day-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-studies-bromley-college-top-up-eve-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-studies-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-studies-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/chemical-engineering-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/chemistry-for-drug-discovery-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/chemistry-for-drug-discovery-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/childhood-studies-ba-hons-bromley-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/childhood-studies-foundation-degree-with-sen-at-bromley-college-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/childhood-studies-ba-hons-bexley-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/childhood-studies-foundation-degree-at-bexley-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/childhood-studies-foundation-degree-with-sen-at-west-kent-college-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/childhood-studies-ba-hons-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/childhood-studies-fd-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/computer-forensics-and-security-with-foundation-year-19-20.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/computer-forensics-and-security-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/computer-forensics-and-security-19-20.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/computer-science-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/computing-with-foundation-year-19-20.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/computing-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/computing-19-20.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/counselling-coaching-and-mentoring-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/counselling-coaching-and-mentoring-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/creative-and-professional-writing-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/creative-and-professional-writing-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/dance-education-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/dance-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/digital-marketing-communications-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/digital-media-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/digital-media-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/drama-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/early-childhood-education-and-care-bromley-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/early-childhood-education-and-care-ba-hons-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/early-childhood-education-and-care-foundation-degree-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/early-childhood-studies-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/early-childhood-studies-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/ecology-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/ecology-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/education-studies-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/education-studies-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/english-language-and-communication-with-foundation-year-2018-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/english-language-and-communication-2018-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/english-literature-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/english-literature-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/environmental-science-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/environmental-science-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/environmental-science-19-20.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/events-venues-management-fd-at-london-south-east-colleges-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/events-management-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/film-production-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/film-production-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/film-radio-and-television-studies-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/film-radio-and-television-studies-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/finance-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/finance-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/forensic-investigation-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/forensic-investigation-with-foundation-year-19-20.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/forensic-investigation-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/french-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/games-design-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/games-design-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/ba-geography-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/geography-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/graphic-design-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/graphic-design-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/health-and-care-nursing-associate-foundation-degree-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/health-and-care-foundation-degree-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/health-and-social-care-studies-cert-he-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/health-studies-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/health-studies-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/history-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/history-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/hospitality-management-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-biology-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-biology-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-development-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-development-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-resource-management-bsc-at-bromley-college-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-resource-management-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-resource-management-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/information-technology-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/international-relations-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/international-relations-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/multimedia-journalism-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/journalism-multimedia-journalism-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/law-llb-with-another-subject-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/law-llb-with-business-at-london-south-east-colleges-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/law-llb-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/logistics-management-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/management-sustainable-ethical-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/management-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/management-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/marketing-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/marketing-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/mathematics-with-secondary-education-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/media-and-communications-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/media-and-communications-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/medieval-and-early-modern-studies-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/medieval-and-early-modern-studies-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-production-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-production-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-ba-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-bmus-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-commercial-music-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-commercial-music-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-creative-music-technology-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/music-creative-music-technology-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/nursing-studies-adult-nursing-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/occupational-therapy-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/operating-department-practice-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/ophthalmic-dispensing-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/ophthalmic-dispensing-17-18.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/performing-arts-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/performing-arts-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/photography-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/photography-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/physical-education-and-physical-activity-fd-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/physical-education-and-sport-exercise-science-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/physical-education-and-sport-exercise-science-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/plant-science-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/plant-science-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/policing-criminal-investigation-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/policing-criminal-psychology-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/policing-critical-incidents-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/policing-cybersecurity-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/policing-global-perspectives-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/policing-terrorism-and-political-violence-2018-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/policing-youth-justice-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/policing-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/politics-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/politics-with-foundation-year-19-20.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/politics-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/primary-education-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/psychology-sport-and-exercise-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/psychology-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/psychology-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/public-relations-media-and-marketing-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/religion-philosophy-and-ethics-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/religion-philosophy-and-ethics-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/social-care-studies-fd-west-kent-college.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/social-work-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/sociology-and-social-policy-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/sociology-and-social-policy-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/sociology-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/sociology-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/special-educational-needs-and-inclusion-studies-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/special-educational-needs-and-inclusion-studies-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/speech-and-language-therapy-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-and-exercise-psychology-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-and-exercise-psychology-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-and-exercise-psychology-19-20.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-and-exercise-science-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-and-exercise-science-with-foundation-year-19-20.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-and-exercise-science-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-and-exercise-science-19-20.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-coaching-science-with-foundation-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-coaching-science-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/sport-coaching-science-19-20.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/theology-with-foundation-year-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/theology-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/tourism-management-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/tourism-studies-18-19.aspx',
# 'https://www.canterbury.ac.uk/study-here/courses/undergraduate/web-technology-18-19.aspx',]
    C = ['https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-bsc-hons-at-bromley-college-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-development-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/education-studies-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/physical-education-and-sport-exercise-science-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/advertising-with-foundation-year-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/management-with-foundation-year-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/marketing-with-foundation-year-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-finance-with-foundation-year-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-with-foundation-year-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-management-with-foundation-year-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/finance-with-foundation-year-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/business-studies-with-foundation-year-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-resource-management-with-foundation-year-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/accounting-and-management-with-foundation-year-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/sociology-and-social-policy-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/special-educational-needs-and-inclusion-studies-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/ecology-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/education-studies-with-foundation-year-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/human-development-with-foundation-year-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/physical-education-and-sport-exercise-science-with-foundation-year-18-19.aspx',
'https://www.canterbury.ac.uk/study-here/courses/undergraduate/special-educational-needs-and-inclusion-studies-with-foundation-year-18-19.aspx',]
    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'Canterbury Christ Church University'
        try:
            location = 'Canterbury'
            location = remove_tags(location)
            #print(location)
        except:
            location = 'N/A'
            #print(location)
        try:
            department = response.xpath('//ul[@class="course-department"]').extract()[0]
            department = remove_tags(department)
            department = department.replace('\n\n', '\n')
            department = department.replace('\r\n', '')
            department = department.replace('	', '')
            department = department.replace('  ', '')
            department = department.replace('\n', '')
            department = department.replace('Our Staff', '')
            #print(department)
        except:
            department = 'N/A'
            #print(department)


        try:
            degree_name = response.xpath('//*[@id="form1"]/div[3]/div/div/div[1]/div[1]/h1/span[1]').extract()[0]
            degree_name = remove_tags(degree_name)
            #degree_name = degree_name.split()[0]

            #degree_name = re.findall('(.*)\n.*',degree_name)[0]
            #degree_name = re.findall('(.*)                    .*',degree_name)[0]
            #degree_name = re.findall('\((.*)\)',degree_name)[0]
            #degree_name = degree_name.replace('\n',degree_name)
            degree_name = degree_name.replace(' ','')
            #print(degree_name)
        except:
            degree_name = 'N/A'
            #print(degree_name)

        try:
            degree_overview_en = ''
            degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = "<div><p>" + degree_overview_en + "</p></div>"
            #print(degree_overview_en)
        except:
            degree_overview_en = ''

        try:
            programme_en = response.xpath('///*[@id="form1"]/div[3]/div/div/div[1]/div[1]/h1/span[2]').extract()[0]
            programme_en = remove_tags(programme_en)
            programme_en = re.findall(' (.*)',programme_en)[0]
            #programme_en = programme_en.replace(degree_name,'')
            #programme_en = programme_en.replace('  ','')
            #programme_en = programme_en.replace('\n', '')
            #programme_en = re.findall(('                    '),'')[0]
            #programme_en = re.findall("(.*)\(.*\)",programme_en)[0]
            #programme_en = programme_en.replace('\n','')
            #programme_en = programme_en.replace('  ','')
            #print(programme_en)
        except:
            programme_en = ''
            #print(programme_en)

        try:
            overview_en = response.xpath('//*[@id="collapseOne"]/div').extract()[0]
            overview_en = remove_tags(overview_en)
            overview_en = overview_en.replace('  ','')
            #overview_en = overview_en.replace('\n\n','\n')
            overview_en = overview_en.replace('\n\n','')
            overview_en = overview_en.replace('\r\n','')
            overview_en = overview_en.replace('\n','')
            overview_en = '<div>' + overview_en + '</div>'
            #overview_en = remove_tags(overview_en)
            #print(overview_en)
        except:
            overview_en = 'N/A'
            #print(overview_en)


        try:
            start_date = '9'

            #print(start_date)
        except:
            start_date = ''


        try:
            modules_en = response.xpath('//*[@id="collapseThree"]/div').extract()[0]
            modules_en = remove_tags(modules_en)
            modules_en = modules_en.replace('\n\n','\n')
            modules_en = modules_en.replace('\r\n','')
            modules_en = modules_en.replace('	','')
            modules_en = modules_en.replace('  ','')
            modules_en = modules_en.replace('\n','')
            modules_en = "<div><p>" + modules_en + "</p></div>"
            #print(modules_en)
        except:
            modules_en = 'N/A'
            #print(modules_en)



        try:
            degree_requirements = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[2]/div[2]/div[1]/div[2]').extract()[0]
            degree_requirements = remove_tags(degree_requirements)
            degree_requirements = degree_requirements.replace('  ','')
            #print(degree_requirements)
        except:
            degree_requirements = ''
            #print(degree_requirements)

        try:
            rntry_requirements_en = response.xpath('//*[@id="form1"]/div[3]/div/div/div[2]/div/ul[3]').extract()[0]
            rntry_requirements_en = remove_tags(rntry_requirements_en)
            rntry_requirements_en = "<div>"+rntry_requirements_en+"</div>"
            rntry_requirements_en = rntry_requirements_en.replace('\n\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\r\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('  ','')
            #rntry_requirements_en =rntry_requirements_en.replace('		                        ','')
            #print(rntry_requirements_en)
        except:
            rntry_requirements_en = 'N/A'
            #print(rntry_requirements_en)

        try:
            professional_background = response.xpath('').extract()
            professional_background = remove_tags(professional_background)
        except:
            professional_background = ''

        try:
            require_chinese_en = ' <p>Bachelor degree (Xueshi)  For programmes requiring a 2:1 :  - A minimum final grade of 75% or equivalent  - A minimum final grade of 70% or equivalent from one of the 211 universities  For programmes requiring a 2:2:  - A minimum final grade of 70% or equivalent  - A minimum final grade of 65% or equivalent from one of the 211 universities Read more at https://www.canterbury.ac.uk//study-here/international/your-country/china.aspx#6IcURYBGrdAXt2Fs.99H</p>'
        except:
            require_chinese_en = ' <p>Bachelor degree (Xueshi)  For programmes requiring a 2:1 :  - A minimum final grade of 75% or equivalent  - A minimum final grade of 70% or equivalent from one of the 211 universities  For programmes requiring a 2:2:  - A minimum final grade of 70% or equivalent  - A minimum final grade of 65% or equivalent from one of the 211 universities Read more at https://www.canterbury.ac.uk//study-here/international/your-country/china.aspx#6IcURYBGrdAXt2Fs.99H</p>'
        try:
            ielts_desc = '<p>.For postgraduate entry, you will need a minimum of IELTS 6.5 or equivalent, with no less than 6.0 in Writing and no less than 5.5 in Reading, Speaking and Listening. We are able to accept other English qualifications, including Bachelor\'s and Master\'s degrees depending upon the country of issue.</p>'
            #print(ielts_desc)

        except:
            ielts_desc = 'N/A'

            #print(ielts_desc)

        try:
            ielts = 6.5
            #print(ielts)

        except:

            ielts = 6.5
            #print(ielts)
        try:
            ielts_l = 5.5
            #print(ielts_l)
            #ielts_l = remove_tags(ielts_l)
        except:
            ielts_l = 5.5

        try:
            ielts_s = ielts_l

        except:
            ielts_s = 0

        try:
            ielts_r = ielts_l
        except:
            ielts_r = 0

        try:
            ielts_w = 6.0
        except:
            ielts_w = 0

        try:
            toefl_code = response.xpath('').extract()
            toefl_code = remove_tags(toefl_code)
        except:
            toefl_code = 0

        try:
            toefl_desc = response.xpath('').extract()
            toefl_desc = remove_tags(toefl_desc)
        except:
            toefl_desc = 0

        try:
            toefl = response.xpath('').extract()
            toefl = remove_tags(toefl)

        except:
            toefl = 0

        try:
            toefl_l = response.xpath('').extrcat()
            toefl_l = remove_tags(toefl_l)

        except:
            toefl_l = 0

        try:
            toefl_s = response.xpath('').extract()
            toefl_s = remove_tags(toefl_s)

        except:
            toefl_s = 0

        try:
            toefl_r = response.xpath('').extract()
            toefl_r = remove_tags(toefl_r)
        except:
            toefl_r = 0

        try:
            toefl_w = response.xpath('').extract()
            toefl_w = remove_tags(toefl_w)
        except:
            toefl_w = 0

        try:
            interview_desc_en = response.xpath('//*[@id="entry-requirements-accordion-0"]/div[1]').extract()[0]
            interview_desc_en = remove_tags(interview_desc_en)
            interview_desc_en = interview_desc_en.replace('\n\n', '\n')
            interview_desc_en = interview_desc_en.replace('\r\n', '')
            interview_desc_en = interview_desc_en.replace('	', '')
            interview_desc_en = interview_desc_en.replace('  ', '')
            interview_desc_en = interview_desc_en.replace('\n', '')
            interview_desc_en = "<div>" + interview_desc_en + "</div>"
            #print(interview_desc_en)
        except:
            interview_desc_en = 'N/A'
            #print(interview_desc_en)
        try:
            work_experience_desc_en = response.xpath('').extract()
            work_experience_desc_en = remove_tags(work_experience_desc_en)
        except:
            work_experience_desc_en = ''

        try:
            portfolio_desc_en = response.xpath('').extract()
            portfolio_desc_en = remove_tags(portfolio_desc_en)
        except:
            portfolio_desc_en = ''

        try:
            career_en = response.xpath('//*[@id="your-future-career-5"]/div[1]/div').extract()[0]
            career_en = remove_tags(career_en)
            career_en = career_en.replace('\r\n','')
            career_en = career_en.replace('  ','')
            career_en = career_en.replace('\n','')
            career_en = "<div><span>" + career_en + "</span></div>"
            #print(career_en)
        except:
            career_en = ''
            #print(career_en)
        try:
            apply_desc_en = '<p>Choose your subject area* Download and complete application form Submit your application form with evidence of your qualifications Receive conditional offer letter Meet any offer conditions Apply for accommodation Receive final confirmation of offer Accept confirmation Arrive with original documents confirming your qualifications Register on course Begin course</p>'
            #apply_desc_en = remove_tags(apply_desc_en)
            #apply_desc_en = "<div>" + apply_desc_en + "</div>"
            #print(apply_desc_en)
        except:
            apply_desc_en = ''

        try:
            apply_documents_en = '<div>Make sure you send a copy of your first degree (or equivalent) certificate and transcript. Don\'t forget you will need evidence of your level of English language (IELTS, TOEFL, etc). You will also need to send at least one academic reference. Some degree programmes have additional requirements - check the relevant academic department web pages for details. Never send original documents - send copies only. There are special arrangements for international students applying for courses which require an interview or audition. These will be detailed in your conditional offer letter.</div>'
            #apply_documents_en = remove_tags(apply_documents_en)
        except:
            apply_documents_en = ''


        apply_fee = 0


        #other = ''
        try:
            apply_proces_en = response.xpath('').extract()
        except:
            apply_proces_en = ''


        try:
            duration = response.xpath('//*[@id="form1"]/div[3]/div/div/div[2]/div/ul[3]/li').extract()[0]
            duration = remove_tags(duration)
            duration = re.findall('(\d) years',duration)[0]
            #print(duration)
        except:
            duration = ''
            #print(duration)



        try:
            other = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/a').extract()[0]
            other = remove_tags(other)
            #print('成功'+ other + response.url)
        except:
            other = ''
           #print('失败' + other)

        try:
            ib = response.xpath('//*[@id="tab-Entry_Requirements"]/div/div[1]/div[1]/table[1]/tbody/tr[11]/td[2]').extract()[0]
            ib = remove_tags(ib)
            #print(ib)
        except:
            ib = ''
            #print(ib)

        try:
            alevel = response.xpath('//*[@id="form1"]/div[3]/div/div/div[2]/div[1]/ul[5]/li').extract()[0]
            alevel = remove_tags(alevel)
            #alevel = re.findall("(\w\w\w) at A Level",alevel)[0]
            #print(alevel)
        except:
            alevel = 'N/A'
            #print(alevel)
        try:
            ucascode = response.xpath('//*[@id="form1"]/div[3]/div/div/div[2]/div/ul[1]/li[1]/span|//*[@id="form1"]/div[3]/div/div/div[2]/div/ul[1]/li[2]/span').extract()[0]
            ucascode = remove_tags(ucascode)

            #print(ucascode)
        except:
            ucascode = 'N/A'
            #print(ucascode)

        try:
            tuition_fee = response.xpath('//tbody/tr[2]/td[2]').extract()[0]
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = tuition_fee.replace('£','')
            tuition_fee = tuition_fee.replace(',','')
            tuition_fee = tuition_fee.replace('*','')
            tuition_fee = tuition_fee.replace(' ','')
            tuition_fee = tuition_fee.replace('\r\n','')
            tuition_fee = tuition_fee.replace('\n','')

            tuition_fee = re.findall('(\d\d\d\d\d)',tuition_fee)[0]

            # tuition_fee = tuition_fee.replace('  ','')
            # tuition_fee = tuition_fee.replace('\n','')
            # tuition_fee = re.findall('Full-time international students: £(.*) paStudents',tuition_fee)[0]
            # tuition_fee = int(tuition_fee)
            #print(tuition_fee)
        except:
            tuition_fee = 0
            #print(tuition_fee)

        try:
            assessment_en = response.xpath('//*[@id="collapseEight"]/div/p|//*[@id="collapseSeven"]/div').extract()[0]
            assessment_en = remove_tags(assessment_en)
            assessment_en = assessment_en.replace('\n','')
            assessment_en = "<div>" + assessment_en + "</div>"
            #print(assessment_en)
        except:
            assessment_en = 'N/A'
            #print(assessment_en)
        item["university"] = university
        item["location"] = location
        item["department"] = department
        item["degree_type"] = 2
        item["degree_name"] = degree_name
        #item["degree_overview_en"] = degree_overview_en
        item["programme_en"] = programme_en
        item["overview_en"] = overview_en
        item["teach_time"] = 1
        item["start_date"] = start_date
        item["modules_en"] = modules_en
        item["career_en"] = career_en
        item["application_open_date"] = '9'
        item["deadline"] = ''
        item["apply_pre"] = '£'
        item["apply_fee"] = apply_fee
        #item["rntry_requirements_en"] = rntry_requirements_en
        item["degree_requirements"] = degree_requirements
        item["tuition_fee_pre"] = '£'
        #item["major_requirements"] = rntry_requirements_en
        item["professional_background"] = professional_background
        item["ielts_desc"] = ielts_desc
        item["ielts"] = ielts
        item["ielts_l"] = ielts_l
        item["ielts_s"] = ielts_l
        item["ielts_r"] = ielts_l
        item["ielts_w"] = ielts_l
        item["toefl_code"] = toefl_code
        item["toefl_desc"] = toefl_desc
        item["toefl"] = toefl
        item["toefl_l"] = toefl_l
        item["toefl_s"] = toefl_s
        item["toefl_r"] = toefl_r
        item["toefl_w"] = toefl_w
        item["work_experience_desc_en"] = work_experience_desc_en
        item["interview_desc_en"] = interview_desc_en
        item["portfolio_desc_en"] = portfolio_desc_en
        item["apply_desc_en"] = apply_desc_en
        item["apply_documents_en"] = apply_documents_en
        item["other"] = other
        item["url"] = response.url
        item["gatherer"] = 'weihongbo'
        item["apply_proces_en"] = apply_proces_en
        item["batch_number"] = 4
        item["finishing"] = 0
        stime = time.time()
        create_time = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(float(stime)))
        #print(create_time)
        item["create_time"] = create_time
        item["import_status"] = 0
        item["duration"] = duration
        item["tuition_fee"] = tuition_fee
        item["update_time"] = create_time
        item["alevel"] = alevel
        item["ib"] = ib
        item["ucascode"] = ucascode
        item["rntry_requirements"] = rntry_requirements_en
        item["require_chinese_en"] = require_chinese_en
        item["assessment_en"] = assessment_en
        #item["apply_pre"] = ''
        yield item


