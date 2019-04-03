# -*- coding: utf-8 -*-
import scrapy
from Australia.items import AustraliaItem
from Australia.middlewares import *
import requests
from lxml import etree
class LatrobeuniversityPSpider(scrapy.Spider):
    name = 'LaTrobeUniversity_P'
    # allowed_domains = ['a.b']
    start_urls = ['https://www.latrobe.edu.au/courses/master-of-biotechnology-management',
'https://www.latrobe.edu.au/courses/master-of-business-administration',
'https://www.latrobe.edu.au/courses/master-of-business-analytics',
'https://www.latrobe.edu.au/courses/master-of-cybersecurity-business-operations',
'https://www.latrobe.edu.au/courses/master-of-cybersecurity-computer-science',
'https://www.latrobe.edu.au/courses/master-of-cybersecurity-law',
'https://www.latrobe.edu.au/courses/master-of-digital-marketing-communications',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis-financial-risk-management',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis-investment',
'https://www.latrobe.edu.au/courses/master-of-management',
'https://www.latrobe.edu.au/courses/master-of-management-human-resource-management',
'https://www.latrobe.edu.au/courses/master-of-management-project-management',
'https://www.latrobe.edu.au/courses/master-of-management-sport-management',
'https://www.latrobe.edu.au/courses/master-of-marketing',
'https://www.latrobe.edu.au/courses/master-of-professional-accounting',
'https://www.latrobe.edu.au/courses/master-of-professional-accounting-business-analytics',
'https://www.latrobe.edu.au/courses/master-of-professional-accounting-cpa-australia-extension',
'https://www.latrobe.edu.au/courses/master-of-professional-accounting-information-systems-management',
'https://www.latrobe.edu.au/courses/master-of-accounting-and-financial-management',
'https://www.latrobe.edu.au/courses/master-of-arts2',
'https://www.latrobe.edu.au/courses/master-of-business-research',
'https://www.latrobe.edu.au/courses/master-of-business-administration-advanced',
'https://www.latrobe.edu.au/courses/master-of-business-administration-and-master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-business-information-management-and-systems',
'https://www.latrobe.edu.au/courses/master-of-commerce-research',
'https://www.latrobe.edu.au/courses/master-of-economics-research',
'https://www.latrobe.edu.au/courses/master-of-engineering-management',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis-master-of-business-administration',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis-master-of-international-business',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis-master-of-professional-accounting',
'https://www.latrobe.edu.au/courses/master-of-international-business',
'https://www.latrobe.edu.au/courses/master-of-management-entrepreneurship-and-innovation',
'https://www.latrobe.edu.au/courses/master-of-biotechnology-management',
'https://www.latrobe.edu.au/courses/master-of-business-administration',
'https://www.latrobe.edu.au/courses/master-of-business-analytics',
'https://www.latrobe.edu.au/courses/master-of-cybersecurity-business-operations',
'https://www.latrobe.edu.au/courses/master-of-cybersecurity-computer-science',
'https://www.latrobe.edu.au/courses/master-of-cybersecurity-law',
'https://www.latrobe.edu.au/courses/master-of-digital-marketing-communications',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis-financial-risk-management',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis-investment',
'https://www.latrobe.edu.au/courses/master-of-management',
'https://www.latrobe.edu.au/courses/master-of-management-human-resource-management',
'https://www.latrobe.edu.au/courses/master-of-management-project-management',
'https://www.latrobe.edu.au/courses/master-of-management-sport-management',
'https://www.latrobe.edu.au/courses/master-of-marketing',
'https://www.latrobe.edu.au/courses/master-of-professional-accounting',
'https://www.latrobe.edu.au/courses/master-of-professional-accounting-business-analytics',
'https://www.latrobe.edu.au/courses/master-of-professional-accounting-cpa-australia-extension',
'https://www.latrobe.edu.au/courses/master-of-professional-accounting-information-systems-management',
'https://www.latrobe.edu.au/courses/master-of-accounting-and-financial-management',
'https://www.latrobe.edu.au/courses/master-of-arts2',
'https://www.latrobe.edu.au/courses/master-of-business-research',
'https://www.latrobe.edu.au/courses/master-of-business-administration-advanced',
'https://www.latrobe.edu.au/courses/master-of-business-administration-and-master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-business-information-management-and-systems',
'https://www.latrobe.edu.au/courses/master-of-commerce-research',
'https://www.latrobe.edu.au/courses/master-of-economics-research',
'https://www.latrobe.edu.au/courses/master-of-engineering-management',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis-master-of-business-administration',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis-master-of-international-business',
'https://www.latrobe.edu.au/courses/master-of-financial-analysis-master-of-professional-accounting',
'https://www.latrobe.edu.au/courses/master-of-international-business',
'https://www.latrobe.edu.au/courses/master-of-management-entrepreneurship-and-innovation',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-dietetic-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-occupational-therapy-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-physiotherapy-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-speech-pathology',
'https://www.latrobe.edu.au/courses/bachelor-of-exercise-science-and-master-of-exercise-physiology',
'https://www.latrobe.edu.au/courses/bachelor-of-human-services-and-master-of-social-work',
'https://www.latrobe.edu.au/courses/master-of-art-therapy',
'https://www.latrobe.edu.au/courses/master-of-clinical-audiology',
'https://www.latrobe.edu.au/courses/master-of-dietetic-practice',
'https://www.latrobe.edu.au/courses/master-of-disability-practice',
'https://www.latrobe.edu.au/courses/master-of-ergonomics-safety-and-health',
'https://www.latrobe.edu.au/courses/master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-health-information-management',
'https://www.latrobe.edu.au/courses/master-of-healthcare-analytics',
'https://www.latrobe.edu.au/courses/master-of-mental-health',
'https://www.latrobe.edu.au/courses/master-of-mental-health-nursing',
'https://www.latrobe.edu.au/courses/master-of-midwifery',
'https://www.latrobe.edu.au/courses/master-of-nursing',
'https://www.latrobe.edu.au/courses/master-of-nursing-nurse-practitioner',
'https://www.latrobe.edu.au/courses/master-of-nursing-science',
'https://www.latrobe.edu.au/courses/master-of-occupational-therapy-practice',
'https://www.latrobe.edu.au/courses/master-of-physiotherapy-practice',
'https://www.latrobe.edu.au/courses/master-of-public-health',
'https://www.latrobe.edu.au/courses/master-of-speech-pathology',
'https://www.latrobe.edu.au/courses/master-of-sports-analytics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-clinical-audiology',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-clinical-prosthetics-and-orthotics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-orthoptics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-podiatric-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-health-sciences-in-dentistry-master-of-dentistry',
'https://www.latrobe.edu.au/courses/master-of-applied-science',
'https://www.latrobe.edu.au/courses/master-of-business-administration-and-master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-clinical-family-therapy',
'https://www.latrobe.edu.au/courses/master-of-clinical-prosthetics-and-orthotics',
'https://www.latrobe.edu.au/courses/master-of-exercise-physiology',
'https://www.latrobe.edu.au/courses/master-of-health-sciences',
'https://www.latrobe.edu.au/courses/master-of-musculoskeletal-physiotherapy',
'https://www.latrobe.edu.au/courses/master-of-nursing-research',
'https://www.latrobe.edu.au/courses/master-of-orthoptics',
'https://www.latrobe.edu.au/courses/master-of-podiatric-practice',
'https://www.latrobe.edu.au/courses/master-of-public-health-and-master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-science',
'https://www.latrobe.edu.au/courses/master-of-social-work',
'https://www.latrobe.edu.au/courses/master-of-social-work-research',
'https://www.latrobe.edu.au/courses/master-of-sports-physiotherapy',
'https://www.latrobe.edu.au/courses/master-of-teaching-english-to-speakers-of-other-languages-tesol',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-dietetic-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-occupational-therapy-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-physiotherapy-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-speech-pathology',
'https://www.latrobe.edu.au/courses/bachelor-of-exercise-science-and-master-of-exercise-physiology',
'https://www.latrobe.edu.au/courses/bachelor-of-human-services-and-master-of-social-work',
'https://www.latrobe.edu.au/courses/master-of-art-therapy',
'https://www.latrobe.edu.au/courses/master-of-clinical-audiology',
'https://www.latrobe.edu.au/courses/master-of-dietetic-practice',
'https://www.latrobe.edu.au/courses/master-of-disability-practice',
'https://www.latrobe.edu.au/courses/master-of-ergonomics-safety-and-health',
'https://www.latrobe.edu.au/courses/master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-health-information-management',
'https://www.latrobe.edu.au/courses/master-of-healthcare-analytics',
'https://www.latrobe.edu.au/courses/master-of-mental-health',
'https://www.latrobe.edu.au/courses/master-of-mental-health-nursing',
'https://www.latrobe.edu.au/courses/master-of-midwifery',
'https://www.latrobe.edu.au/courses/master-of-nursing',
'https://www.latrobe.edu.au/courses/master-of-nursing-nurse-practitioner',
'https://www.latrobe.edu.au/courses/master-of-nursing-science',
'https://www.latrobe.edu.au/courses/master-of-occupational-therapy-practice',
'https://www.latrobe.edu.au/courses/master-of-physiotherapy-practice',
'https://www.latrobe.edu.au/courses/master-of-public-health',
'https://www.latrobe.edu.au/courses/master-of-speech-pathology',
'https://www.latrobe.edu.au/courses/master-of-sports-analytics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-clinical-audiology',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-clinical-prosthetics-and-orthotics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-orthoptics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-podiatric-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-health-sciences-in-dentistry-master-of-dentistry',
'https://www.latrobe.edu.au/courses/master-of-applied-science',
'https://www.latrobe.edu.au/courses/master-of-business-administration-and-master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-clinical-family-therapy',
'https://www.latrobe.edu.au/courses/master-of-clinical-prosthetics-and-orthotics',
'https://www.latrobe.edu.au/courses/master-of-exercise-physiology',
'https://www.latrobe.edu.au/courses/master-of-health-sciences',
'https://www.latrobe.edu.au/courses/master-of-musculoskeletal-physiotherapy',
'https://www.latrobe.edu.au/courses/master-of-nursing-research',
'https://www.latrobe.edu.au/courses/master-of-orthoptics',
'https://www.latrobe.edu.au/courses/master-of-podiatric-practice',
'https://www.latrobe.edu.au/courses/master-of-public-health-and-master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-science',
'https://www.latrobe.edu.au/courses/master-of-social-work',
'https://www.latrobe.edu.au/courses/master-of-social-work-research',
'https://www.latrobe.edu.au/courses/master-of-sports-physiotherapy',
'https://www.latrobe.edu.au/courses/master-of-teaching-english-to-speakers-of-other-languages-tesol',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-dietetic-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-occupational-therapy-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-physiotherapy-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-speech-pathology',
'https://www.latrobe.edu.au/courses/bachelor-of-exercise-science-and-master-of-exercise-physiology',
'https://www.latrobe.edu.au/courses/bachelor-of-human-services-and-master-of-social-work',
'https://www.latrobe.edu.au/courses/master-of-art-therapy',
'https://www.latrobe.edu.au/courses/master-of-clinical-audiology',
'https://www.latrobe.edu.au/courses/master-of-dietetic-practice',
'https://www.latrobe.edu.au/courses/master-of-disability-practice',
'https://www.latrobe.edu.au/courses/master-of-ergonomics-safety-and-health',
'https://www.latrobe.edu.au/courses/master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-health-information-management',
'https://www.latrobe.edu.au/courses/master-of-healthcare-analytics',
'https://www.latrobe.edu.au/courses/master-of-mental-health',
'https://www.latrobe.edu.au/courses/master-of-mental-health-nursing',
'https://www.latrobe.edu.au/courses/master-of-midwifery',
'https://www.latrobe.edu.au/courses/master-of-nursing',
'https://www.latrobe.edu.au/courses/master-of-nursing-nurse-practitioner',
'https://www.latrobe.edu.au/courses/master-of-nursing-science',
'https://www.latrobe.edu.au/courses/master-of-occupational-therapy-practice',
'https://www.latrobe.edu.au/courses/master-of-physiotherapy-practice',
'https://www.latrobe.edu.au/courses/master-of-public-health',
'https://www.latrobe.edu.au/courses/master-of-speech-pathology',
'https://www.latrobe.edu.au/courses/master-of-sports-analytics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-clinical-audiology',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-clinical-prosthetics-and-orthotics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-orthoptics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-podiatric-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-health-sciences-in-dentistry-master-of-dentistry',
'https://www.latrobe.edu.au/courses/master-of-applied-science',
'https://www.latrobe.edu.au/courses/master-of-business-administration-and-master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-clinical-family-therapy',
'https://www.latrobe.edu.au/courses/master-of-clinical-prosthetics-and-orthotics',
'https://www.latrobe.edu.au/courses/master-of-exercise-physiology',
'https://www.latrobe.edu.au/courses/master-of-health-sciences',
'https://www.latrobe.edu.au/courses/master-of-musculoskeletal-physiotherapy',
'https://www.latrobe.edu.au/courses/master-of-nursing-research',
'https://www.latrobe.edu.au/courses/master-of-orthoptics',
'https://www.latrobe.edu.au/courses/master-of-podiatric-practice',
'https://www.latrobe.edu.au/courses/master-of-public-health-and-master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-science',
'https://www.latrobe.edu.au/courses/master-of-social-work',
'https://www.latrobe.edu.au/courses/master-of-social-work-research',
'https://www.latrobe.edu.au/courses/master-of-sports-physiotherapy',
'https://www.latrobe.edu.au/courses/master-of-teaching-english-to-speakers-of-other-languages-tesol',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-dietetic-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-occupational-therapy-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-physiotherapy-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-speech-pathology',
'https://www.latrobe.edu.au/courses/bachelor-of-exercise-science-and-master-of-exercise-physiology',
'https://www.latrobe.edu.au/courses/bachelor-of-human-services-and-master-of-social-work',
'https://www.latrobe.edu.au/courses/master-of-art-therapy',
'https://www.latrobe.edu.au/courses/master-of-clinical-audiology',
'https://www.latrobe.edu.au/courses/master-of-dietetic-practice',
'https://www.latrobe.edu.au/courses/master-of-disability-practice',
'https://www.latrobe.edu.au/courses/master-of-ergonomics-safety-and-health',
'https://www.latrobe.edu.au/courses/master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-health-information-management',
'https://www.latrobe.edu.au/courses/master-of-healthcare-analytics',
'https://www.latrobe.edu.au/courses/master-of-mental-health',
'https://www.latrobe.edu.au/courses/master-of-mental-health-nursing',
'https://www.latrobe.edu.au/courses/master-of-midwifery',
'https://www.latrobe.edu.au/courses/master-of-nursing',
'https://www.latrobe.edu.au/courses/master-of-nursing-nurse-practitioner',
'https://www.latrobe.edu.au/courses/master-of-nursing-science',
'https://www.latrobe.edu.au/courses/master-of-occupational-therapy-practice',
'https://www.latrobe.edu.au/courses/master-of-physiotherapy-practice',
'https://www.latrobe.edu.au/courses/master-of-public-health',
'https://www.latrobe.edu.au/courses/master-of-speech-pathology',
'https://www.latrobe.edu.au/courses/master-of-sports-analytics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-clinical-audiology',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-clinical-prosthetics-and-orthotics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-orthoptics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-podiatric-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-health-sciences-in-dentistry-master-of-dentistry',
'https://www.latrobe.edu.au/courses/master-of-applied-science',
'https://www.latrobe.edu.au/courses/master-of-business-administration-and-master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-clinical-family-therapy',
'https://www.latrobe.edu.au/courses/master-of-clinical-prosthetics-and-orthotics',
'https://www.latrobe.edu.au/courses/master-of-exercise-physiology',
'https://www.latrobe.edu.au/courses/master-of-health-sciences',
'https://www.latrobe.edu.au/courses/master-of-musculoskeletal-physiotherapy',
'https://www.latrobe.edu.au/courses/master-of-nursing-research',
'https://www.latrobe.edu.au/courses/master-of-orthoptics',
'https://www.latrobe.edu.au/courses/master-of-podiatric-practice',
'https://www.latrobe.edu.au/courses/master-of-public-health-and-master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-science',
'https://www.latrobe.edu.au/courses/master-of-social-work',
'https://www.latrobe.edu.au/courses/master-of-social-work-research',
'https://www.latrobe.edu.au/courses/master-of-sports-physiotherapy',
'https://www.latrobe.edu.au/courses/master-of-teaching-english-to-speakers-of-other-languages-tesol',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-dietetic-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-occupational-therapy-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-physiotherapy-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-speech-pathology',
'https://www.latrobe.edu.au/courses/bachelor-of-exercise-science-and-master-of-exercise-physiology',
'https://www.latrobe.edu.au/courses/bachelor-of-human-services-and-master-of-social-work',
'https://www.latrobe.edu.au/courses/master-of-art-therapy',
'https://www.latrobe.edu.au/courses/master-of-clinical-audiology',
'https://www.latrobe.edu.au/courses/master-of-dietetic-practice',
'https://www.latrobe.edu.au/courses/master-of-disability-practice',
'https://www.latrobe.edu.au/courses/master-of-ergonomics-safety-and-health',
'https://www.latrobe.edu.au/courses/master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-health-information-management',
'https://www.latrobe.edu.au/courses/master-of-healthcare-analytics',
'https://www.latrobe.edu.au/courses/master-of-mental-health',
'https://www.latrobe.edu.au/courses/master-of-mental-health-nursing',
'https://www.latrobe.edu.au/courses/master-of-midwifery',
'https://www.latrobe.edu.au/courses/master-of-nursing',
'https://www.latrobe.edu.au/courses/master-of-nursing-nurse-practitioner',
'https://www.latrobe.edu.au/courses/master-of-nursing-science',
'https://www.latrobe.edu.au/courses/master-of-occupational-therapy-practice',
'https://www.latrobe.edu.au/courses/master-of-physiotherapy-practice',
'https://www.latrobe.edu.au/courses/master-of-public-health',
'https://www.latrobe.edu.au/courses/master-of-speech-pathology',
'https://www.latrobe.edu.au/courses/master-of-sports-analytics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-clinical-audiology',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-clinical-prosthetics-and-orthotics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-orthoptics',
'https://www.latrobe.edu.au/courses/bachelor-of-applied-science-and-master-of-podiatric-practice',
'https://www.latrobe.edu.au/courses/bachelor-of-health-sciences-in-dentistry-master-of-dentistry',
'https://www.latrobe.edu.au/courses/master-of-applied-science',
'https://www.latrobe.edu.au/courses/master-of-business-administration-and-master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-clinical-family-therapy',
'https://www.latrobe.edu.au/courses/master-of-clinical-prosthetics-and-orthotics',
'https://www.latrobe.edu.au/courses/master-of-exercise-physiology',
'https://www.latrobe.edu.au/courses/master-of-health-sciences',
'https://www.latrobe.edu.au/courses/master-of-musculoskeletal-physiotherapy',
'https://www.latrobe.edu.au/courses/master-of-nursing-research',
'https://www.latrobe.edu.au/courses/master-of-orthoptics',
'https://www.latrobe.edu.au/courses/master-of-podiatric-practice',
'https://www.latrobe.edu.au/courses/master-of-public-health-and-master-of-health-administration',
'https://www.latrobe.edu.au/courses/master-of-science',
'https://www.latrobe.edu.au/courses/master-of-social-work',
'https://www.latrobe.edu.au/courses/master-of-social-work-research',
'https://www.latrobe.edu.au/courses/master-of-sports-physiotherapy',
'https://www.latrobe.edu.au/courses/master-of-teaching-english-to-speakers-of-other-languages-tesol',]
    start_urls = set(start_urls)
    def parse(self, response):
        # print(response.url)
        pro_url=re.findall('https?://www.latrobe.edu.au/courses/data/2019/international/[a-z\-/]+',response.text,re.S)
        if pro_url!=[]:
            for pu in pro_url:
                # print(pu)
                yield scrapy.Request(url=pu,callback=self.parses)
    def parses(self, response):
        print(response.url)
        item=get_item(AustraliaItem)
        item['university']='La Trobe University'
        item['url']=response.url
        degree_name=response.xpath('//h1/text()').extract()
        degree_name=''.join(degree_name)
        # print(degree_name)
        item['degree_name']=degree_name
        modules_url = response.xpath('//ul[@class="list-arrows"]/li[1]/a/@href').extract()
        if modules_url != []:
            try:
                modules = self.getResponse(modules_url[0]).xpath(
                    '//h3[contains(text(),"Course structure")]/following-sibling::div/div/table//tr/td/text()')
                item['modules_en'] = clear_long_text(modules)
            except:
                pass
        location=response.xpath('//ul[@class="list-arrows"]/li[1]/a/text()').extract()
        location=''.join(location).strip()
        item['location']=location

        overview = response.xpath('//section[@id="overview"]/div[@class="block"]').extract()
        # print('overview', overview)
        item['degree_overview_en']=remove_class(overview)
        rntry=response.xpath('//section[@id="entry-requirements"]').extract()
        # print('rntry',rntry)
        item['rntry_requirements_en']=remove_class(rntry)
        career=response.xpath('//section[@id="career-outcomes"]').extract()
        # print('career',career)
        item['career_en']=remove_class(career)
        htp=response.xpath('//section[@id="how-to-apply"]').extract()
        # print('htp',htp)
        item['apply_proces_en']=remove_class(htp)
        fee=response.xpath('//h3[contains(text(),"tuition fee")]/following-sibling::p[1]/text()').extract()
        # print('fee',fee)
        fee=''.join(fee).strip()
        tuition=fee.replace(' ','')
        # print('tuition_fee',tuition)
        item['tuition_fee']=tuition
        item['tuition_fee_pre']='AUD'
        duration=response.xpath('//div[contains(text(),"uration")]/following-sibling::div//text()').extract()
        # print('duration',duration)
        dura=re.findall('\d\.?\d?',''.join(duration))
        if dura!=[]:
            dura=list(map(float,dura))
            item['duration']=min(dura)
            item['duration_per']=1
        else:
            duration=clear_duration(duration)
            item['duration']=duration['duration']
            item['duration_per']=duration['duration_per']
        start_date=response.xpath('//div[contains(text(),"tart")]/following-sibling::div//text()').extract()
        # print('start_date',start_date)
        start_date=tracslateDate(start_date)
        # print(start_date)
        item['start_date']=','.join(start_date)
        ielts=response.xpath('//p[contains(text(),"IELTS")]/text()').extract()
        ielts=get_ielts(ielts)
        if ielts!=[]:
            item['ielts'] = ielts['IELTS']
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
        # degree_name_list=response.xpath('//p[contains(text(),"Our Majors are:")]/following-sibling::ul/li//a/@href|//p[contains(text(),"Choose from five majors")]/following-sibling::ul[1]/li//a/@href|//h3[contains(text(),"Specialisations, majors and minors")]/following-sibling::table/tbody/tr/td[1]//a/@href').extract()
        degree_name_list = response.xpath(
            '//p[contains(text(),"Our Majors are:")]/following-sibling::ul/li//text()|//p[contains(text(),"Choose from five majors")]/following-sibling::ul[1]/li//text()|//h3[contains(text(),"Specialisations, majors and minors")]/following-sibling::table/tbody/tr/td[1]//text()').extract()
        major_xpaths = '//section[@id="overview"]//a[contains(text(),"%s")]/@href'
        if degree_name_list != []:
            # print(degree_name_list)
            for name in degree_name_list:
                major_xpath = major_xpaths % name
                major_url = response.xpath(major_xpath).extract()
                # print(major_url)
                item['programme_en'] = name.strip()
                if major_url != []:
                    URL = major_url[0]
                    majRep = self.getResponse(URL)
                    modules = majRep.xpath('//div[@id="overview"]|//div[@id="why_study"]')
                    mod = ''
                    for i in modules:
                        mod += etree.tostring(i, method='html', encoding='unicode')
                    item['overview_en'] = remove_class(mod)
                print(item['degree_name'],'的专业')
                yield item
        else:
                programme = re.findall('\(.*\)', degree_name.replace('(Honours)',''))
                programme = ''.join(programme).replace('(', '').replace(')', '').strip()
                if programme != '':
                    item['programme_en'] = programme
                else:
                    item['programme_en'] = degree_name.replace('Bachelor of', '').replace('Master of', '').strip()
                print(item['degree_name'],'没有专业')
                yield item
    def getResponse(self,url):
        try:
            res=requests.get(url).content
            res=etree.HTML(res)
            return res
        except:
            return ''