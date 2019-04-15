# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/7 11:55'
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
from scrapySchool_England.translate_date import  tracslateDate
from scrapySchool_England.translate_date import tracslateDate
class UniversityofDerbySpider(scrapy.Spider):
    name = 'UniversityofDerby_u'
    allowed_domains = ['derby.ac.uk/']
    start_urls = []
    C = [
        'https://www.derby.ac.uk/undergraduate/access-courses/foundation-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/accounting-courses/accounting-and-finance-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/accounting-courses/accounting-and-finance-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/accounting-courses/accounting-and-finance-integrated-masters-maccfin/',
        'https://www.derby.ac.uk/undergraduate/accounting-courses/accounting-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/accounting-courses/business-accounting-and-finance-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/accounting-courses/business-accounting-and-finance-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/architecture-architectural-technology-courses/architectural-design-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/architecture-architectural-technology-courses/architectural-technology-and-practice-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/architecture-architectural-technology-courses/architectural-technology-and-practice-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/architecture-architectural-technology-courses/interior-architecture-and-venue-design-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/architecture-architectural-technology-courses/interior-architecture-venue-design-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/architecture-architectural-technology-courses/interior-design-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/art-design-courses/animation-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/art-design-courses/animation-mdes/',
        'https://www.derby.ac.uk/undergraduate/art-design-courses/fine-art-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/art-design-courses/graphic-design-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/art-design-courses/graphic-design-mdes/',
        'https://www.derby.ac.uk/undergraduate/art-design-courses/illustration-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/art-design-courses/illustration-mdes/',
        'https://www.derby.ac.uk/undergraduate/biology-zoology-courses/biology-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/biology-zoology-courses/biology-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/biology-zoology-courses/biology-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/biology-zoology-courses/zoology-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/biology-zoology-courses/zoology-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/biology-zoology-courses/zoology-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/biomedical-health-human-biology-courses/biomedical-health-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/biomedical-health-human-biology-courses/biomedical-health-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/biomedical-health-human-biology-courses/biomedical-health-msci/',
        'https://www.derby.ac.uk/undergraduate/biomedical-health-human-biology-courses/human-biology-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/biomedical-health-human-biology-courses/human-biology-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/business-courses/business-enterprise-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/business-courses/business-management-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/business-courses/business-management-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/business-courses/business-management-enterprise-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/business-courses/business-management-finance-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/business-courses/business-management-hrm-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/business-courses/business-management-international-business-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/business-courses/business-management-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/business-courses/business-management-marketing-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/business-courses/business-studies-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/business-courses/business-studies-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/business-courses/it-management-for-business-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/civil-and-infrastructure-engineering-beng-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/civil-and-infrastructure-engineering-beng-hons/',
        'https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/civil-and-infrastructure-engineering-beng-hons/',
        'https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/civil-engineering-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/civil-engineering-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/civil-engineering-meng/',
        'https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/construction-management-and-property-development-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/construction-management-property-dev-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/property-development-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/quantity-surveying-and-commercial-management-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/quantity-surveying-commercial-mgmt-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/analytics-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-forensic-investigation-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-forensics-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-forensics-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-games-modelling-and-animation-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-games-modelling-and-animation-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-games-programming-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-games-programming-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-games-programming-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-network-engineering-beng-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-network-engineering-beng-hons/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-network-engineering-beng-hons/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-networks-and-security-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-networks-security-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-networks-security-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-science-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-science-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/computer-science-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/cyber-security-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/cyber-security-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/cyber-security-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/information-technology-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/information-technology-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/computing-courses/information-technology-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/criminology-policing-courses/criminal-psychology-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/criminology-policing-courses/criminal-psychology-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/criminology-policing-courses/criminology-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/criminology-policing-courses/criminology-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/criminology-policing-courses/criminology-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/criminology-policing-courses/policing-and-investigations-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/criminology-policing-courses/policing-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/economics-finance-courses/economics-and-finance-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/economics-finance-courses/economics-and-finance-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/economics-finance-courses/economics-for-business-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/economics-finance-courses/economics-for-business-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/economics-finance-courses/economics-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/economics-finance-courses/finance-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/economics-finance-courses/finance-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/economics-finance-courses/international-business-and-finance-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/economics-finance-courses/international-business-and-finance-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/economics-finance-courses/international-business-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/economics-finance-courses/international-business-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/education-studies-send-courses/education-studies-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/education-studies-send-courses/education-studies-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/education-studies-send-courses/education-studies-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/education-studies-send-courses/special-educational-needs-disability-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/education-studies-send-courses/special-educational-needs-disability-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/electrical-electronic-engineering-courses/electrical-and-electronic-engineering-beng-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/electrical-electronic-engineering-courses/electrical-and-electronic-engineering-beng-hons/',
        'https://www.derby.ac.uk/undergraduate/electrical-electronic-engineering-courses/electrical-and-electronic-engineering-beng-hons/',
        'https://www.derby.ac.uk/undergraduate/electrical-electronic-engineering-courses/electrical-and-electronic-engineering-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/electrical-electronic-engineering-courses/electrical-and-electronic-engineering-bsc-with-foundation-year/',
        'https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/creative-writing-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/creative-writing-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/creative-writing-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/english-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/english-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/english-integrated-masters-mlit/',
        'https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/english-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/english-language-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/english-literature-and-language-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/english-literature-and-language-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/publishing-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/writing-and-publishing-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/writing-and-publishing-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/entertainment-engineering-courses/broadcast-engineering-and-live-event-technology-foundation/',
        'https://www.derby.ac.uk/undergraduate/entertainment-engineering-courses/broadcast-engineering-live-event-tech-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/entertainment-engineering-courses/sound-light-and-live-event-technology-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/entertainment-engineering-courses/sound-light-and-live-event-technology-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/entertainment-engineering-courses/sound-light-and-live-event-technology-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/events-management-courses/events-management-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/events-management-courses/events-management-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/fashion-textiles-courses/fashion-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/fashion-textiles-courses/fashion-fashion-marketing-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/fashion-textiles-courses/textile-design-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/film-media-production-courses/film-production-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/film-media-production-courses/media-production-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/film-media-production-courses/television-production-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/film-media-production-courses/visual-effects-and-post-production-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/forensic-science-courses/forensic-science-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/forensic-science-courses/forensic-science-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/forensic-science-courses/forensic-science-with-criminology-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/forensic-science-courses/forensic-science-with-criminology-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/forensic-science-courses/forensic-science-with-psychology-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/forensic-science-courses/forensic-science-with-psychology-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/geography-courses/geography-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/geography-courses/geography-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/geography-courses/geography-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/geography-courses/global-development-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/geology-courses/environmental-hazards-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/geology-courses/geology-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/geology-courses/geology-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/geology-courses/geology-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/health-social-community-work-courses/applied-social-work-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/health-social-community-work-courses/child-family-health-wellbeing-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/health-social-community-work-courses/child-family-health-wellbeing-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/health-social-community-work-courses/child-family-health-wellbeing-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/health-social-community-work-courses/health-and-social-care-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/health-social-community-work-courses/health-and-social-care-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/health-social-community-work-courses/youth-work-and-community-development-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/health-social-community-work-courses/youth-work-and-community-development-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/history-courses/history-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/history-courses/history-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/history-courses/history-integrated-masters/',
        'https://www.derby.ac.uk/undergraduate/history-courses/history-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/hospitality-culinary-management-courses/international-hospitality-management-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/hospitality-culinary-management-courses/international-hospitality-management-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/hospitality-culinary-management-courses/professional-culinary-management-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/hospitality-culinary-management-courses/professional-culinary-management-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/human-resource-management-courses/human-resource-management-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/journalism-courses/football-journalism-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/journalism-courses/football-journalism-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/journalism-courses/journalism-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/journalism-courses/journalism-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/journalism-courses/journalism-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/journalism-courses/magazine-journalism-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/journalism-courses/magazine-journalism-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/journalism-courses/specialist-sports-journalism-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/journalism-courses/specialist-sports-journalism-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/law-courses/law-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/law-courses/law-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/law-courses/llb-criminology/',
        'https://www.derby.ac.uk/undergraduate/law-courses/llb/',
        'https://www.derby.ac.uk/undergraduate/logistics-supply-chain-management-courses/logistics-and-supply-chain-management-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/logistics-supply-chain-management-courses/logistics-and-supply-chain-management-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-consumer-psychology-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-consumer-psychology-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-digital-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-digital-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-pr-and-advertising-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-pr-and-advertising-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/mathematics-courses/mathematics-and-computer-science-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/mathematics-courses/mathematics-and-computer-science-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/mathematics-courses/mathematics-and-computer-science-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/mathematics-courses/mathematics-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/mathematics-courses/mathematics-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/mathematics-courses/mathematics-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/mathematics-courses/mathematics-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/mathematics-courses/mathematics-with-education-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/mechanical-manufacturing-engineering-courses/manufacturing-and-production-engineering-beng-hons/',
        'https://www.derby.ac.uk/undergraduate/mechanical-manufacturing-engineering-courses/manufacturing-and-production-engineering-beng-hons/',
        'https://www.derby.ac.uk/undergraduate/mechanical-manufacturing-engineering-courses/mechanical-engineering-beng-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/mechanical-manufacturing-engineering-courses/mechanical-engineering-beng-hons/',
        'https://www.derby.ac.uk/undergraduate/mechanical-manufacturing-engineering-courses/mechanical-engineering-beng-hons/',
        'https://www.derby.ac.uk/undergraduate/mechanical-manufacturing-engineering-courses/mechanical-engineering-meng/',
        'https://www.derby.ac.uk/undergraduate/mechanical-manufacturing-engineering-courses/mechanical-manufacturing-engineering-beng-hons/',
        'https://www.derby.ac.uk/undergraduate/media-cultural-studies-courses/american-studies-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/media-cultural-studies-courses/film-and-television-studies-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/media-cultural-studies-courses/media-and-communication-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/media-cultural-studies-courses/media-and-communication-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/media-cultural-studies-courses/media-studies-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/media-cultural-studies-courses/popular-music-in-society-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/motorsport-engineering-courses/motorsport-engineering-beng-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/motorsport-engineering-courses/motorsport-engineering-beng-hons/',
        'https://www.derby.ac.uk/undergraduate/motorsport-engineering-courses/motorsport-engineering-meng/',
        'https://www.derby.ac.uk/undergraduate/music-music-production-courses/music-technology-production-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/music-music-production-courses/popular-music-production-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/music-music-production-courses/popular-music-with-music-technology-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/nursing-courses/community-specialist-practice-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-adult-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-mental-health-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-mental-health-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/nursing-courses/specialist-community-public-health-nursing-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/occupational-therapy-courses/occupational-therapy-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/occupational-therapy-courses/occupational-therapy-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/outdoor-adventure-sport-courses/adventure-sport-coaching-science-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/outdoor-adventure-sport-courses/adventure-sport-coaching-science-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/outdoor-adventure-sport-courses/outdoor-leadership-and-management-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/performing-arts-theatre-courses/contemporary-theatre-performance-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/performing-arts-theatre-courses/costume-set-design-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/performing-arts-theatre-courses/dance-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/performing-arts-theatre-courses/technical-theatre-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/performing-arts-theatre-courses/theatre-studies-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/photography-courses/commercial-photography-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/photography-courses/photography-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/photography-courses/photography-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/political-sciences-courses/international-relations-and-diplomacy-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/political-sciences-courses/international-relations-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/political-sciences-courses/politics-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/product-design-courses/product-design-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/product-design-courses/product-design-engineering-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/product-design-courses/product-design-engineering-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/psychology-counselling-courses/counselling-psychotherapy-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/psychology-counselling-courses/counselling-psychotherapy-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/psychology-counselling-courses/psychology-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/psychology-counselling-courses/psychology-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/psychology-counselling-courses/psychology-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/radiography-courses/diagnostic-radiography-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/social-sciences-courses/sociology-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/social-sciences-courses/sociology-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/spa-wellness-management-courses/international-spa-management-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/performance-analysis-coaching-science-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/performance-analysis-coaching-science-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/physical-activity-nutrition-health-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/physical-activity-nutrition-health-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-and-education-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-and-education-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-and-exercise-science-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-and-exercise-science-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-and-exercise-studies-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-coaching-and-development-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-management-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-management-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-therapy-and-rehabilitation-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-therapy-and-rehabilitation-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/strength-conditioning-and-rehabilitation-bsc-hons/',
        'https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/strength-conditioning-rehabilitation-bsc-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/teacher-training-courses/education-integrated-masters/',
        'https://www.derby.ac.uk/undergraduate/teacher-training-courses/primary-education-qts-bed-hons/',
        'https://www.derby.ac.uk/undergraduate/therapeutic-practice-courses/creative-expressive-therapies-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/therapeutic-practice-courses/creative-expressive-therapies-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/therapeutic-practice-courses/creative-expressive-therapies-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/therapeutic-practice-courses/creative-expressive-therapies-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/therapeutic-practice-courses/creative-expressive-therapies-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/therapeutic-practice-courses/creative-expressive-therapies-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/therapeutic-practice-courses/creative-expressive-therapies-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/therapeutic-practice-courses/creative-expressive-therapies-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/therapeutic-practice-courses/dance-movement-studies-joint-honours/',
        'https://www.derby.ac.uk/undergraduate/tourism-management-courses/tourism-management-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/tourism-management-courses/tourism-management-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/working-with-children-young-people-courses/child-and-youth-studies-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/working-with-children-young-people-courses/child-and-youth-studies-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/working-with-children-young-people-courses/early-childhood-studies-ba-hons-foundation/',
        'https://www.derby.ac.uk/undergraduate/working-with-children-young-people-courses/early-childhood-studies-ba-hons/',
        'https://www.derby.ac.uk/undergraduate/working-with-children-young-people-courses/early-childhood-studies-joint-honours/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Derby'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//h1/strong').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        programme_en = programme_en.replace('&amp; ','').strip()
        # print(programme_en)

        #4.degree_type
        degree_type = 1

        #5.degree_name
        degree_name = response.xpath('//h1/text()').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        degree_name = degree_name.replace('(Hons)','').strip()
        # print(degree_name)

        #6.overview_en
        overview_en = response.xpath("//*[contains(text(),'Course description')]/../following-sibling::section[1]").extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #7.career_en
        career_en = response.xpath("//*[contains(text(),'Careers')]/../following-sibling::*[1]").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #8.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'assessed')]//following-sibling::*[1]").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        if len(assessment_en)==0:
            assessment_en = response.xpath("//*[contains(text(),'How you will learn')]/../following-sibling::*[1]").extract()
            assessment_en = ''.join(assessment_en)
            assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #9.ucascode
        ucascode = response.xpath("//*[contains(text(),'UCAS code')]//following-sibling::*").extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode).strip()
        if 'Full-time: N200' in ucascode:
            ucascode = 'N200'
        # print(ucascode,url)


        #10.duration
        duration = response.xpath("//*[contains(text(),'Study options')]//following-sibling::*").extract()
        duration = ''.join(duration)
        duration =remove_tags(duration).strip()
        if ',' in duration:
            duration = re.findall(r'(.*),',duration)[0]
        duration = duration.replace('Full-time: ','').strip().replace('†','').strip()
        # print(duration)

        #11.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'International fee')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        if tuition_fee ==0:
            tuition_fee = 12500
        # print(tuition_fee)

        #12.tuition_fee_pre
        tuition_fee_pre = '£'

        #13.location
        location = response.xpath("//*[contains(text(),'Location')]//following-sibling::*").extract()
        location = ''.join(location)
        location = remove_tags(location)
        # print(location)

        #14.start_date
        start_date = response.xpath("//*[contains(text(),'Start date')]//following-sibling::*").extract()
        start_date = ''.join(start_date)
        start_date = remove_class(start_date)
        if 'January, September' in start_date:
            start_date = '2019-9,2020-1'
        else:
            start_date = '2019-9'
        # print(start_date)

        #15.apply_proces_en
        apply_proces_en = 'https://www.derby.ac.uk/services/admissions/apply-online/'

        #16.modules_en
        num = response.xpath('//body//@id').extract()[0]
        num = re.findall('\d+',num)[0]
        xpaths = '//*[@id="section-id-'+str(num)+'"]/main/div[2]/section'
        modules_en = response.xpath(xpaths).extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #17.alevel
        try:
            alevel1 = response.xpath("//*[contains(text(),'Specific requirements at A-level')]/../following-sibling::*").extract()[-1]
            alevel1 = ''.join(alevel1)
            alevel1 = remove_tags(alevel1)
        except:
            alevel1 = 'N/A'
        try:
            alevel2 = response.xpath("//*[contains(text(),'Specific requirements at A-level')]/../../preceding-sibling::*").extract()[-1]
            alevel2 = ''.join(alevel2)
            alevel2 = remove_tags(alevel2)
        except:
            alevel2 = 'N/A'
        alevel = alevel2 + alevel1
        # print(alevel)

        # print(alevel)

        #18.ielts 19202122
        ielts = 6.0
        ielts_w = 5.5
        ielts_r = 5.5
        ielts_s = 5.5
        ielts_l = 5.5

        #23.require_chinese_en
        require_chinese_en = "'<p>You will usually need one of these qualifications Two or three year Diploma from a specialised college  Two year Diploma from a Chinese university First year of an undergraduate degree at a Chinese university</p>'"

        #24.apply_pre
        apply_pre = '£'

        #25.apply_desc_en
        apply_desc_en = response.xpath("//*[contains(text(),'Alternative entry qualifications:')]//following-sibling::*").extract()
        apply_desc_en = ''.join(apply_desc_en)
        apply_desc_en = remove_class(apply_desc_en)
        # print(apply_desc_en)


        item['apply_desc_en'] = apply_desc_en
        item['require_chinese_en'] = require_chinese_en
        item['apply_pre'] = apply_pre
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['overview_en'] = overview_en
        item['career_en'] = career_en
        item['assessment_en'] = assessment_en
        item['ucascode'] = ucascode
        item['alevel'] = alevel2
        item['duration'] = duration
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['location'] = location
        item['start_date'] = start_date
        item['apply_proces_en'] = apply_proces_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['modules_en'] = modules_en
        yield  item
