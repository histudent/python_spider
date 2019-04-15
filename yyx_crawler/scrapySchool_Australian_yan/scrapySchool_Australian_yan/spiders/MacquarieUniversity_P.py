# -*- coding: utf-8 -*-
import scrapy
import json
from scrapySchool_Australian_yan.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_yan.getItem import get_item
from scrapySchool_Australian_yan.getTuition_fee import getTuition_fee
from scrapySchool_Australian_yan.items import ScrapyschoolAustralianYanItem
from scrapySchool_Australian_yan.remove_tags import remove_class
from scrapySchool_Australian_yan.getStartDate import getStartDateMonth
from scrapySchool_Australian_yan.getDuration import getIntDuration
from scrapySchool_Australian_yan.getIELTS import get_ielts
from lxml import etree
import requests
import re

#
class MacquarieUniversity_PSpider(scrapy.Spider):
    name = "MacquarieUniversity_P"
#     start_urls = ["https://api.coursefinder.mq.edu.au/api/2018/international/research/bachelor-of-philosophymaster-of-research-science-and-engineering?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-advanced-surgery?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-environment?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-politics-and-public-policy?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-social-entrepreneurship?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-international-communication?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/doctor-of-medicine?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-radiopharmaceutical-science?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-applied-finance?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-data-science?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-international-business?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-medicine?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-economics?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-applied-linguistics-and-tesol?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-security-and-strategic-studies?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-conference-interpreting?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-laboratory-quality-analysis-and-management?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-public-health?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-management?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-advanced-professional-accounting?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-surgery?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-clinical-psychology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-engineering?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-professional-psychology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-creative-writing?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-educational-leadership?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-banking-and-finance?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-planning?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/research/master-of-research-science-and-engineering?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-advanced-medicine?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-criminology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-teaching-birth-to-five-years?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-intelligence?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-policy-and-applied-social-research?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/doctor-of-physiotherapy?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-accounting-advanced?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-information-technology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-advanced-translation-and-interpreting-studies?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-actuarial-practice?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-international-public-diplomacy?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-cyber-security?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-early-childhood?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-laws?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-applied-finance-advanced?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-international-trade-and-commerce-law?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-creative-industries?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-biotechnology-and-business?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-international-relations?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/research/bachelor-of-philosophymaster-of-research-human-sciences?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/research/master-of-research-business-and-economics?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/juris-doctor?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-science?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-business-administration?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-marine-science-and-management?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-clinical-neuropsychology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-biotechnology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-conservation-biology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-accounting?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-applied-statistics?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/research/bachelor-of-philosophymaster-of-research-medicine-and-health-sciences?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-chiropractic?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-media?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-international-law-governance-and-public-policy?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-clinical-audiology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-speech-and-language-pathology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-applied-linguistics?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-ancient-history?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-translation-and-interpreting-studies?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-counter-terrorism?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-commerce?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-organisational-psychology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-sustainable-development?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/research/master-of-research-arts?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-accessible-communication?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2018/international/postgraduate/master-of-development-studies?studentType=international", ]
#     start_urls = ["https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-accessible-communication?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-accounting?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-accounting-advanced?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-actuarial-practice?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-advanced-medicine?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-advanced-professional-accounting?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-advanced-surgery?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-advanced-translation-and-interpreting-studies?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-ancient-history?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-applied-finance?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-applied-finance-advanced?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-applied-linguistics?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-applied-linguistics-and-tesol?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-applied-statistics?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-banking-and-finance?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-biotechnology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-biotechnology-and-business?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-business-administration?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-chiropractic?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-clinical-audiology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-clinical-neuropsychology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-clinical-psychology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-commerce?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-conference-interpreting?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-conservation-biology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-counter-terrorism?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-creative-industries?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-creative-industries-with-the-degree-of-master-of-media?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-creative-writing?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-criminology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-cyber-security?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-data-science?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-development-studies?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-early-childhood?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-engineering?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-environment?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-information-technology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-intelligence?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-international-business?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-international-business-with-the-degree-of-master-of-international-communication?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-international-business-with-the-degree-of-master-of-international-relations?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-international-communication?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-international-communication-with-the-degree-of-master-of-international-relations?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-international-law-governance-and-public-policy?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-international-public-diplomacy?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-international-relations?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-international-trade-and-commerce-law?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-laboratory-quality-analysis-and-management?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-laws?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-management?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-marine-science-and-management?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-media?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-organisational-psychology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-planning?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-policy-and-applied-social-research?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-policy-and-applied-social-research-with-the-degree-of-master-of-development-studies?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-politics-and-public-policy?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-politics-and-public-policy-with-the-degree-of-master-of-development-studies?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-politics-and-public-policy-with-the-degree-of-master-of-international-relations?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-politics-and-public-policy-with-the-degree-of-master-of-policy-and-applied-social-research?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-public-health?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-radiopharmaceutical-science?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-security-and-strategic-studies?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-social-entrepreneurship?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-speech-and-language-pathology?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-surgery?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-sustainable-development?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-teaching-birth-to-five-years?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-translation-and-interpreting-studies?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-translation-and-interpreting-studies-with-the-degree-of-master-of-applied-linguistics-and-tesol?studentType=international",
# "https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-translation-and-interpreting-studies-with-the-degree-of-master-of-international-relations?studentType=international", ]
    # 2019.03.18 星期一 数据更新
    start_urls = ["https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/doctor-of-medicine?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/doctor-of-physiotherapy?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/juris-doctor?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-accounting?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-accounting-advanced?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-actuarial-practice?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-advanced-professional-accounting?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-advanced-translation-and-interpreting-studies?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-applied-economics?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-applied-finance?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-applied-finance-advanced?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-applied-linguistics?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-applied-linguistics-and-tesol?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-applied-statistics?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-banking-and-finance?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-biotechnology?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-biotechnology-and-business?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-business-administration?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-chiropractic?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-clinical-audiology?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-clinical-neuropsychology?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-clinical-psychology?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-commerce?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-conference-interpreting?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-conservation-biology?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-counter-terrorism?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-counter-terrorism-with-the-degree-of-master-of-criminology?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-creative-industries?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-creative-industries-with-the-degree-of-master-of-media?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-creative-writing?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-criminology?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-cyber-security?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-cyber-security-with-the-degree-of-master-of-counter-terrorism?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-cyber-security-with-the-degree-of-master-of-criminology?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-data-science?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-early-childhood?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-engineering?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-environment?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-information-technology?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-information-technology-cyber-security?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-intelligence?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-intelligence-with-the-degree-of-master-of-counter-terrorism?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-intelligence-with-the-degree-of-master-of-criminology?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-intelligence-with-the-degree-of-master-of-cyber-security?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-international-business?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-international-business-with-the-degree-of-master-of-international-relations?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-international-relations?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-international-trade-and-commerce-law?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-laboratory-quality-analysis-and-management?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-laws?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-management?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-marine-science-and-management?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-marketing?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-media?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-organisational-psychology?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-planning?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-public-health?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-radiopharmaceutical-science?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-science-innovation?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-security-and-strategic-studies?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-security-and-strategic-studies-with-the-degree-of-master-of-counter-terrorism?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-security-and-strategic-studies-with-the-degree-of-master-of-criminology?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-security-and-strategic-studies-with-the-degree-of-master-of-cyber-security?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-security-and-strategic-studies-with-the-degree-of-master-of-intelligence?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-speech-and-language-pathology?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-sustainable-development?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-teaching-birth-to-five-years?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-translation-and-interpreting-studies?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-translation-and-interpreting-studies-with-the-degree-of-master-of-applied-linguistics-and-tesol?studentType=international",
"https://api.coursefinder.mq.edu.au/api/2019/international/postgraduate/master-of-translation-and-interpreting-studies-with-the-degree-of-master-of-international-relations?studentType=international",]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))
    headers_base = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    degreetypeDict = {}
    def parse(self, response):
        item = get_item(ScrapyschoolAustralianYanItem)
        item['university'] = "Macquarie University"
        # item['country'] = 'Australia'
        # item['website'] = 'https://www.mq.edu.au'
        item['degree_type'] = 2
        item['teach_time'] = 'coursework'
        print("===========================")
        print(response.url)
        informationUrl = response.url.replace("https://api.coursefinder.mq.edu.au/api",
                                              "http://courses.mq.edu.au").replace('?studentType=international",', '",')
        print("------------", informationUrl)
        item['url'] = informationUrl
        try:
            jsonData = response.body
            informationDict = json.loads(jsonData)
            # print(informationDict)

            # programme_dict_all = {"degree_name": degree_name, "programme_en": programme_en, "department": department,
            #                       "duration": duration, "location": location, "start_date": start_date,
            #                       "tuition_fee": tuition_fee, "overview_en": overview_en, "career_en": career_en,
            #                       "modules_en": modules_en, "rntry_requirements_en": rntry_requirements_en,
            #                       "ielts_desc": ielts_desc, "apply_desc_en": apply_desc_en}
            programme_dict_all = self.parse_data(informationDict, item)
            item['degree_name'] = programme_dict_all.get('degree_name')
            item['programme_en'] = programme_dict_all.get('programme_en')
            item['department'] = programme_dict_all.get('department')
            item['duration'] = programme_dict_all.get('duration')
            item["location"] = programme_dict_all.get("location")
            item['start_date'] = programme_dict_all.get('start_date')
            item["tuition_fee"] = programme_dict_all.get("tuition_fee")
            item["degree_overview_en"] = programme_dict_all.get("overview_en")

            item['career_en'] = programme_dict_all.get('career_en')
            item["modules_en"] = programme_dict_all.get("modules_en")
            item["rntry_requirements_en"] = programme_dict_all.get("rntry_requirements_en")

            item["ielts_desc"] = programme_dict_all.get("ielts_desc")
            item["apply_desc_en"] = programme_dict_all.get("apply_desc_en")
            item["apply_documents_en"] = item['apply_desc_en']

            ieltsDict = get_ielts(item['ielts_desc'])
            item['ielts'] = ieltsDict.get("IELTS")
            item['ielts_l'] = ieltsDict.get("IELTS_L")
            item['ielts_s'] = ieltsDict.get("IELTS_S")
            item['ielts_r'] = ieltsDict.get("IELTS_R")
            item['ielts_w'] = ieltsDict.get("IELTS_W")
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            # 为了拼接专业链接，取出链接前缀
            urlPre = re.findall(r"https://api.coursefinder.mq.edu.au/api/2019/international/[a-z]+/", response.url)
            urlPre = ''.join(urlPre)
            print("api接口前缀： ", urlPre)

            # 学位类型
            degreetype = informationDict.get("name")
            if degreetype is None:
                degreetype = ""
            relateMajor = informationDict.get("handbook_detail_data").get("Specialisations")
            print("relateMajor: ", relateMajor)
            if len(relateMajor) == 0:
                # self.parse_data(informationDict, item)
                yield item
            else:
                print("dididididi-----didididiiddididi")
                # self.start_urls.remove(response.url)
                major_list = relateMajor.get(item['degree_name'])
                print("major_list:=== ", major_list)
                # self.degreetypeDict[programme] = degreetype
                # slug = majordict.get("slug")
                if len(major_list) is not None:
                    # 拼接专业链接，加入start_urls
                    for major in major_list:
                        slug = major.get("Name")
                        if slug is not None:
                            slug_s = slug.lower().split(" ")
                            # print("slug_s: ", slug_s)
                            slug_str = '-'.join(slug_s).strip()
                            majorApiUrl = response.url.replace("?studentType=international", "")+ "-" + slug_str + "?studentType=international"
                            print("***专业api链接", majorApiUrl)
                            informationUrl = majorApiUrl.replace("https://api.coursefinder.mq.edu.au/api",
                                                                  "http://courses.mq.edu.au").replace(
                                '?studentType=international",', '",')
                            print("------专业链接------", informationUrl)
                            item['url'] = informationUrl

                            data = requests.get(majorApiUrl, headers=self.headers_base)
                            informationDict = json.loads(data.text)
                            # print(informationDict)
                            major_dict_all = self.parse_data(informationDict, item)
                            programme_en = major_dict_all.get('degree_name')
                            # print("item['programme_en']_major1: ", item['programme_en'])
                            programme_major_re = re.findall(r"in\s.*", programme_en)
                            if len(programme_major_re) > 0:
                                item['programme_en'] = ''.join(programme_major_re).strip().strip("in").strip()
                            else:
                                item['programme_en'] = programme_en.replace("Master of", "").strip()
                            print("item['programme_en']_major: ", item['programme_en'])

                            item['overview_en'] = major_dict_all.get("overview_en")
                            yield item
                # self.start_urls.append(majorApiUrl)
            # self.parse_data(informationDict, item)
            # yield item
        except Exception as e:
            with open("scrapySchool_Australian_yan/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    # 解析页面的json文件
    def parse_data(self, informationDict, item):
        print("********执行了********")
        programme = informationDict.get("name")
        if programme is None:
            programme = ""
        degree_name = programme.strip()
        print("degree_name: ", degree_name)

        pro_re = re.findall(r"Master", degree_name)
        # print("pre_re: ", pro_re)
        if len(pro_re) == 1:
            degree_name_re_str = degree_name.replace("(Advanced)", "").replace("(Birth to Five Years)", "")
            programme_re = re.findall(r"\(.+\)", degree_name_re_str)
            if len(programme_re) > 0:
                programme_en = ''.join(programme_re).replace("(", "").replace(")", "").strip()
            else:
                programme_en = degree_name_re_str.replace("Master of", "").strip()
            print("programme_en: ", programme_en)

            department = informationDict.get("faculty")
            if department is None:
                department = ""
            department = department
            # print("department: ", department)

            duration = informationDict.get("handbook_detail_data").get("Program")[0].get("CandidatureLength")
            # print("duration: ", duration)
            duration = duration.replace("depending on RPL granted", "").strip()
            # print("duration: ", duration)

            start_dateList = informationDict.get("handbook_detail_data").get("Program")[0].get("LocationCommencements")
            # print("start_dateList: ", start_dateList)
            start_date = ""
            location_list = []
            if start_date is not None:
                for st in start_dateList:
                    scope = st.get("Scope")
                    if scope is not None:
                        if 'International' in scope:
                            location = st.get("Location")
                            commencing = st.get("Commencing")
                            if location is None:
                                location = ""
                            if commencing is None:
                                commencing = ""
                            start_date += location + ": " + commencing + ",  "
                            location_list.append(location)
            location_list = list(set(location_list))
            location = ', '.join(location_list).strip().strip(",").strip()
            # print("location: ", location)

            start_date = start_date.strip().strip(',').strip()
            # print("start_date: ", start_date)


            tuition_fee = informationDict.get("handbook_detail_data").get("Program")[0].get("InternationalFees")
            # print("tuition_fee: ", tuition_fee)
            if tuition_fee is None:
                tuition_fee = ""
            else:
                tuition_fee = tuition_fee[0].get("Estimated annual fee")
            tuition_fee = tuition_fee.replace("AUD $", "").replace(",", "")
            # print("item['tuition_fee']: ", item['tuition_fee'])


            # 专业描述
            overview1 = informationDict.get("course_finder_data").get("course_description").get("content").get("override")
            # print("overview1: ", overview1)
            if overview1 is not None:
                if "<p" in overview1:
                    delFu = re.findall(r"&\w+;", overview1)
                    # print(delFu)
                    if len(delFu) != 0:
                        for d in delFu:
                            overview1 = overview1.replace(d, " ")
                    # pageHtml = '<!DOCTYPE html><html><body>' + overview1 + '</body></html>'
                    # html = etree.fromstring(pageHtml)
                    # overview1 = html.xpath("//p//text()")
            elif overview1 is None:
                overview1 = ""
            # print("===overview1: ", overview1)
            overview2 = informationDict.get("course_finder_data").get("key_features").get("content").get("override")
            # print("overview2: ", overview2)
            if overview2 is not None:
                delFu = re.findall(r"&\w+;", overview2)
                # print(delFu)
                if len(delFu) != 0:
                    for d in delFu:
                        overview2 = overview2.replace(d, " ")
                # pageHtml = '<!DOCTYPE html><html><body>' + overview2 + '</body></html>'
                # html = etree.fromstring(pageHtml)
                # overview2 = html.xpath("//li//text()")
                overview2 = "<h2>KEY FEATURES</h2>" + ''.join(overview2)
            elif overview2 is None:
                overview2 = ""
            # print("===overview2: ", overview2)
            overview3 = informationDict.get("course_finder_data").get("accreditation_intro").get("content").get("override")
            if overview3 is not None:
                if "<p" in overview3:
                    delFu = re.findall(r"&\w+;", overview3)
                    # print(delFu)
                    if len(delFu) != 0:
                        for d in delFu:
                            overview3 = overview3.replace(d, " ")
                    # pageHtml = '<!DOCTYPE html><html><body>' + overview3 + '</body></html>'
                    # html = etree.fromstring(pageHtml)
                    # overview3 = html.xpath("//p//text()")
                    overview3 = "<h2>ACCREDITATION</h2>" + ''.join(overview3)
            elif overview3 is None:
                overview3 = ""
            # print("===overview3: ", overview3)
            overview4 = informationDict.get("course_finder_data").get("suitable_for").get("content").get("override")
            if overview4 is not None:
                if "<p" in overview4:
                    delFu = re.findall(r"&\w+;", overview4)
                    # print(delFu)
                    if len(delFu) != 0:
                        for d in delFu:
                            overview4 = overview4.replace(d, " ")
                    # pageHtml = '<!DOCTYPE html><html><body>' + overview4 + '</body></html>'
                    # html = etree.fromstring(pageHtml)
                    # overview4 = html.xpath("//p//text()")
                    overview4 = "<h2>SUITABLE FOR</h2><div>" + ''.join(overview4) + "</div>"
            elif overview4 is None:
                overview4 = ""

            # print("===overview4: ", overview4)
            overview_en = "<h2>Overview</h2>\n" + remove_class(clear_lianxu_space([overview1])) + remove_class(clear_lianxu_space([overview2])) \
                                  + remove_class(clear_lianxu_space([overview3])) + remove_class(clear_lianxu_space([overview4]))
            # print("item['overview_en']: ", item['overview_en'])


            # 就业方向
            career1 = informationDict.get("course_finder_data").get("career_opportunities").get("content").get("default")
            # print("career1: ", career1)
            if career1 is None:
                career1 = ""
            # print("===career1: ", career1)
            career2 = informationDict.get("course_finder_data").get("careers").get("content").get("override")
            # print("career2: ", career2)
            if career2 is not None:
                delFu = re.findall(r"&\w+;", career2)
                # print(delFu)
                if len(delFu) != 0:
                    for d in delFu:
                        career2 = career2.replace(d, " ")
                career2 = career2.replace("&", " ")
                # pageHtml = '<!DOCTYPE html><html><body>' + career2 + '</body></html>'
                # html = etree.fromstring(pageHtml)
                # c2 = html.xpath("//p//text()")
                # career2 = html.xpath("//li//text()")
                career2 = "<h2>PROFESSIONS</h2>" + career2
            elif career2 is None:
                career2 = ""
            # print("===career2: ", career2)
            career3 = informationDict.get("course_finder_data").get("employer_types").get("content").get("override")
            if career3 is not None:
                delFu = re.findall(r"&\w+;", career3)
                # print(delFu)
                if len(delFu) != 0:
                    for d in delFu:
                        career3 = career3.replace(d, " ")
                career3 = career3.replace("&", " ")
                # pageHtml = '<!DOCTYPE html><html><body>' + career3 + '</body></html>'
                # html = etree.fromstring(pageHtml)
                # c3 = html.xpath("//p//text()")
                # career3 = html.xpath("//li//text()")
                career3 = "<h2>EMPLOYERS</h2>" + career3
            elif career3 is None:
                career3 = ""
            # print("===career3: ", career3)
            career_en = remove_class(clear_lianxu_space([career1]))+ remove_class(clear_lianxu_space([career2])) + remove_class(clear_lianxu_space([career3]))
            # print("item['career_en']: ", item['career_en'])


            modules1 = informationDict.get("course_finder_data").get("course_structure_intro").get("content").get("default")
            if modules1 is not None:
                modules1 = "<h2>What You'll Study</h2>" + modules1
            else:
                modules1 = ""
            # print("===modules1: ", modules1)
            modules2 = informationDict.get("course_finder_data").get("units_intro").get("content").get("default")
            if modules2 is not None:
                modules2 = "<h2>Units</h2>" + modules2
            else:
                modules2 = ""

            # print("===modules2: ", modules2)
            modules3 = informationDict.get("course_finder_data").get("general_requirements").get("content").get("default")
            if modules3 is not None:
                modules3 = "<h2>GENERAL REQUIREMENTS</h2>"+modules3
            else:
                modules3 = ""

            # print("===modules3: ", modules3)
            modu4 = informationDict.get("handbook_detail_data").get("GenReqs")
            modules4 = ""
            if modu4 is not None:
                for m4 in modu4:
                    DegreeReq = m4.get("DegreeReq")
                    DegreeReqCP = m4.get("DegreeReqCP")
                    if DegreeReq is None:
                        DegreeReq = ""
                    if DegreeReqCP is None:
                        DegreeReqCP = ""
                    modules4 += "<li>"+DegreeReq + " - " + DegreeReqCP + "</li>\n"
                modules4 = "<ul>" + modules4 + "</ul>"

            # print("===modules4: ", modules4)
            modu5 = informationDict.get("course_finder_data").get("units").get("content").get("override")
            modules5 = ""
            if len(modu5) != 0:
                level1 = modu5.get("level100")
                m5_1 = ""
                if level1 is not None:
                    for l1 in level1:
                        u1 = l1.get("units")
                        for u in u1:
                            name = u.get("name")
                            cp = u.get("cp")
                            if name is None:
                                name = u.get('code')
                                if name is None:
                                    name = ""
                            if cp is None:
                                cp = ""
                            m5_1 += "<li>"+name + " - " + cp + "</li>\n"
                level2 = modu5.get("level200")
                m5_2 = ""
                if level2 is not None:
                    for l1 in level2:
                        u1 = l1.get("units")
                        for u in u1:
                            name = u.get("name")
                            cp = u.get("cp")
                            if name is None:
                                name = u.get('code')
                                if name is None:
                                    name = ""
                            if cp is None:
                                cp = ""
                            m5_2 += "<li>" + name + " - " + cp + "</li>\n"
                level3 = modu5.get("level300")
                m5_3 = ""
                if level3 is not None:
                    for l1 in level3:
                        u1 = l1.get("units")
                        for u in u1:
                            name = u.get("name")
                            cp = u.get("cp")
                            if name is None:
                                name = u.get('code')
                                if name is None:
                                    name = ""
                            if cp is None:
                                cp = ""
                            m5_3 += "<li>" + name + " - " + cp + "</li>\n"
                level4 = modu5.get("800 level")
                m5_4 = ""
                if level4 is not None:
                    for l1 in level4:
                        u1 = l1.get("units")
                        for u in u1:
                            name = u.get("name")
                            cp = u.get("cp")
                            if name is None:
                                name = u.get('code')
                                if name is None:
                                    name = ""
                            if cp is None:
                                cp = ""
                            m5_4 += "<li>" + name + " - " + cp + "</li>\n"
                level5 = modu5.get("600 level")
                m5_5 = ""
                if level5 is not None:
                    for l1 in level5:
                        u1 = l1.get("units")
                        for u in u1:
                            name = u.get("name")
                            cp = u.get("cp")
                            if name is None:
                                name = u.get('code')
                                if name is None:
                                    name = ""
                            if cp is None:
                                cp = ""
                            m5_5 += "<li>" + name + " - " + cp + "</li>\n"
                level6 = modu5.get("level700")
                m5_6 = ""
                if level6 is not None:
                    for l1 in level6:
                        u1 = l1.get("units")
                        for u in u1:
                            name = u.get("name")
                            cp = u.get("cp")
                            if name is None:
                                name = u.get('code')
                                if name is None:
                                    name = ""
                            if cp is None:
                                cp = ""
                            m5_6 += "<li>" + name + " - " + cp + "</li>\n"
                modules5 = "<h2>SPECIFIC REQUIREMENTS<h2>\n<ul>" + m5_1 + m5_2 + m5_3 + m5_4 + m5_5 + m5_6 + "</ul>"
            # print("===modules5: ", modules5)
            modules_en = remove_class(clear_lianxu_space([modules1]))+ remove_class(clear_lianxu_space([modules2])) + \
                                 remove_class(clear_lianxu_space([modules3])) + remove_class(clear_lianxu_space([modules4])) + remove_class(clear_lianxu_space([modules5]))
            # print("item['modules_en']: ", item['modules_en'])


            entry0 = informationDict.get("handbook_detail_data").get("AdditionalMetaData").get("DegAtarInternational")
            if entry0 is None:
                entry0 = ""
            entry0 = "<h2>Entry Requirements</h2>\n" + entry0
            # print("===entry0: ", entry0)

            entry1 = informationDict.get("course_finder_data").get("entry_req_desc").get("content").get("default")
            # print("overview1: ", overview1)
            if entry1 is not None:
                if "<p" in entry1:
                    delFu = re.findall(r"&\w+;", entry1)
                    # print(delFu)
                    if len(delFu) != 0:
                        for d in delFu:
                            entry1 = entry1.replace(d, " ")
                    # pageHtml = '<!DOCTYPE html><html><body>' + entry1 + '</body></html>'
                    # html = etree.fromstring(pageHtml)
                    # entry1 = html.xpath("//p//text()")
            elif entry1 is None:
                entry1 = ""
            # print("===entry1: ", entry1)
            entry11 = informationDict.get("handbook_detail_data").get("AdditionalMetaData").get("AdmissionRequirement")
            if entry11 is None:
                entry11 = ""
            entry11 = "<h2>MINIMUM ADMISSION REQUIREMENT</h2>\n<p>" + entry11 + "</p>"
            # print("===entry11: ", entry11)
            entry2 = informationDict.get("course_finder_data").get("assumed_knowledge").get("content").get("override")
            if entry2 is not None:
                if "<p" in entry2:
                    delFu = re.findall(r"&\w+;", entry2)
                    # print(delFu)
                    if len(delFu) != 0:
                        for d in delFu:
                            entry2 = entry2.replace(d, " ")
                    # pageHtml = '<!DOCTYPE html><html><body>' + entry2 + '</body></html>'
                    # html = etree.fromstring(pageHtml)
                    # entry2 = html.xpath("//p//text()")
                entry2 = "<h2>ASSUMED KNOWLEDGE</h2>\n<p>" + entry2 + "</p>"
            elif entry2 is None:
                entry2 = ""
            # print("===entry2: ", entry2)
            entry3 = informationDict.get("course_finder_data").get("alt_entry").get("content").get("default")
            # print("overview1: ", overview1)
            if entry3 is not None:
                if "<p" in entry3:
                    delFu = re.findall(r"&\w+;", entry3)
                    # print(delFu)
                    if len(delFu) != 0:
                        for d in delFu:
                            entry3 = entry3.replace(d, " ")
                    # pageHtml = '<!DOCTYPE html><html><body>' + entry3 + '</body></html>'
                    # html = etree.fromstring(pageHtml)
                    # entry3 = html.xpath("//p//text()")
            elif entry3 is None:
                entry3 = ""
            # print("===entry3: ", entry3)
            rntry_requirements_en = remove_class(clear_lianxu_space([entry0])) + remove_class(clear_lianxu_space([entry1])) + remove_class(clear_lianxu_space([entry11]))+ \
                                            remove_class(clear_lianxu_space([entry2])) + remove_class(clear_lianxu_space([entry3]))
            # print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])


            ielts = informationDict.get("handbook_detail_data").get("AdditionalMetaData").get("EnglishProficiency")
            if ielts is None:
                ielts = ""
            ielts_desc = ielts.strip()
            # print("===item['ielts_desc']: ", item['ielts_desc'])



            how_to_apply1 = informationDict.get("course_finder_data").get("how_to_apply").get("content").get("override")
            # print("overview1: ", overview1)
            if how_to_apply1 is not None:
                if "<p" in how_to_apply1:
                    delFu = re.findall(r"&\w+;", how_to_apply1)
                    # print(delFu)
                    if len(delFu) != 0:
                        for d in delFu:
                            how_to_apply1 = how_to_apply1.replace(d, " ")
                    # pageHtml = '<!DOCTYPE html><html><body>' + how_to_apply1 + '</body></html>'
                    # html = etree.fromstring(pageHtml)
                    # how_to_apply1 = html.xpath("//p//text()")
                    how_to_apply1 = "<h2>What you'll need to apply</h2>\n" + ''.join(how_to_apply1)
            elif how_to_apply1 is None:
                how_to_apply1 = ""

            apply_desc_en = remove_class(clear_lianxu_space([how_to_apply1]))
            # print("item['apply_desc_en']: ", item['apply_desc_en'])

            programme_dict_all = {"degree_name": degree_name, "programme_en": programme_en, "department": department,
                                  "duration": duration, "location": location, "start_date": start_date,
                                  "tuition_fee": tuition_fee, "overview_en": overview_en, "career_en": career_en,
                                  "modules_en": modules_en, "rntry_requirements_en": rntry_requirements_en,
                                  "ielts_desc": ielts_desc, "apply_desc_en": apply_desc_en}
            return programme_dict_all