# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_Australian_yan.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_yan.getItem import get_item
from scrapySchool_Australian_yan.getTuition_fee import getTuition_fee
from scrapySchool_Australian_yan.items import ScrapyschoolAustralianYanItem
from scrapySchool_Australian_yan.remove_tags import remove_class
from scrapySchool_Australian_yan.getStartDate import getStartDate, getStartDateMonth
from scrapySchool_Australian_yan.getDuration import getIntDuration
from lxml import etree
import requests
from urllib import parse
from selenium import webdriver


class TheUniversityOfMelbourne_P_update201903Spider(scrapy.Spider):
    name = "TheUniversityOfMelbourne_P_update201903"
#     start_urls = ["https://study.unimelb.edu.au/find/courses/graduate/master-of-architectural-engineering/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-architecture/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-construction-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-construction-management/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-design-for-performance/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-civil-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-civil/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-structural/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-management/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-structures/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-landscape-architecture/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-architecture-building-and-planning/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-property/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-and-cultural-heritage/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-design/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-horticulture/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-planning/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-linguistics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-art-curatorship/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-arts-advanced-seminar-shorter-thesis/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-arts-professional-and-applied-ethics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-arts-thesis-only/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-arts-and-cultural-management/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-creative-writing-publishing-and-editing/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-criminology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-cultural-materials-conservation/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-development-studies/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-global-media-communication/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-international-journalism/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-international-relations/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-journalism/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-marketing-communications/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-public-policy-and-management/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-publishing-and-communications/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-social-policy/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-translation/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-translation-enhanced/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-actuarial-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-econometrics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-arts-thesis-only/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-business-administration/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-business-administration-part-time/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-business-analytics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-commerce-actuarial-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-economics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biomedical-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-chemical-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-civil-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-electrical-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-mechanical-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-software-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-management/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-enterprise/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-entrepreneurship/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-evaluation/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-finance/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-international-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-management/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-management-accounting-and-finance/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-management-accounting/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-management-finance/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-management-human-resources/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-management-marketing/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-marketing/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-marketing-communications/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-public-administration/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-public-administration-enhanced/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-public-policy-and-management/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-supply-chain-management/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-tax/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/executive-master-of-business-administration/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/senior-executive-master-of-business-administration/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-agribusiness/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-agricultural-sciences/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-food-and-packaging-innovation/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-food-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-agricultural-sciences/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-veterinary-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-veterinary-public-health/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-veterinary-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-veterinary-science-clinical/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-veterinary-studies/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing-practice/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing-practice-mental-health/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing-practice-nurse-practitioner/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-social-work/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-social-work-research/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-econometrics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-positive-psychology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-psychology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-biomedical-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-biostatistics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-biotechnology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-audiology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-research/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-computational-biology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-data-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-economics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-forest-ecosystem-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-educational-psychology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-energy-systems/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biochemical/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biomedical-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biomedical/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-chemical-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-chemical/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-civil/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-structures/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-environment/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-finance/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-genomics-and-health/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-geography/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-geoscience/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-health-and-human-services/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-health-and-medical-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-information-systems/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-information-technology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-nursing-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-mdhs-biomedical-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-mdhs-health-sciences/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-mdhs-medicine/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-mdhs-psychological-sciences/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-psychology-clinical-neuropsychology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-psychology-clinical-psychology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-rehabilitation-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-bioinformatics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-biosciences/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-chemistry/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-computer-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-earth-sciences/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-ecosystem-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-epidemiology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-mathematics-and-statistics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-physics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-social-work/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-speech-pathology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-sports-medicine/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-sports-rehabilitation/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-tax/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-art-curatorship/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-arts-and-cultural-management/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-contemporary-art/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-creative-writing-publishing-and-editing/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-cultural-materials-conservation/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-dance/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-design-for-performance/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-directing-for-performance/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-dramaturgy/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-film-and-television/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-fine-arts-dance/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-fine-arts-film-and-television/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-fine-arts-music-theatre/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-music-composition/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-music-interactive-composition/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-music-jazz-improvisation/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-music-music-performance/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-music-music-psychology-performance-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-music-music-therapy/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-music-musicology-ethnomusicology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-music-opera-performance/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-music-orchestral-performance/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-music-performance-teaching/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-music-therapy/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-producing/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-production-design-for-screen/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-screenwriting/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-writing-for-performance/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-banking-and-finance-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-commercial-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-competition-and-consumer-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-construction-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-employment-and-labour-relations-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-energy-and-resources-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-global-competition-and-consumer-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-health-and-medical-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-human-rights-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-intellectual-property-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-international-tax/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-law-and-development/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-laws-global-competition-and-consumer-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-laws/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-private-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-public-and-international-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-tax/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-computational-biology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-data-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-software-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-software/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-spatial/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-information-systems/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-information-systems-executive/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-information-technology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-engineering/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-bioinformatics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-computer-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-epidemiology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-mathematics-and-statistics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-adolescent-health-and-wellbeing/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing-practice/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing-practice-mental-health/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing-practice-nurse-practitioner/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-social-work/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-social-work-research/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-ageing/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-positive-psychology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-psychology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-biomedical-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-biostatistics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-biotechnology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-audiology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-education/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-research/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-teaching/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-ultrasound/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-educational-psychology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biomedical-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biomedical/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-epidemiology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-genetic-counselling/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-genomics-and-health/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-health-and-human-services/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-health-and-medical-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-medicine/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-medicine-radiology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-nursing-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-mdhs-biomedical-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-mdhs-dental-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-mdhs-health-sciences/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-mdhs-psychological-sciences/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-primary-health-care/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-psychiatry-online/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-psychology-clinical-neuropsychology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-psychology-clinical-psychology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-public-health/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-rehabilitation-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-bioinformatics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-biosciences/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-chemistry/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-epidemiology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-social-work/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-speech-pathology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-sports-medicine/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-sports-rehabilitation/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-surgery/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-surgical-education/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-surgical-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-forest-ecosystem-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-energy-systems/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-environmental/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-environment/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-engineering/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-geography/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-geoscience/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-landscape-architecture/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-laws/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-architecture-building-and-planning/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-engineering/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-law/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-biosciences/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-computer-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-earth-sciences/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-ecosystem-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-physics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-and-cultural-heritage/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-horticulture/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-architectural-engineering/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-energy-systems/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biochemical/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biomedical-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biomedical/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-chemical-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-chemical/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-civil-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-civil/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-electrical-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-electrical/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-environmental/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-materials/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-mechanical-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-mechanical/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-mechatronics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-software-with-business/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-software/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-spatial/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-structural/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-management/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-structures/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-environment/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-engineering/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-geoscience/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-information-technology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-engineering/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-computer-science/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-earth-sciences/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-science-physics/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-positive-psychology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-teaching/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-education/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-education-research/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-educational-psychology/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-english-in-a-global-context/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-evaluation/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-instructional-leadership/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-international-education-international-baccalaureate/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-learning-intervention/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-modern-languages-education/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-music-performance-teaching/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-education/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-early-childhood-and-primary/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-early-childhood/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-primary/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-secondary/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-secondary-internship/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-tertiary-education-management/where-will-this-take-me/",
# "https://study.unimelb.edu.au/find/courses/graduate/master-of-tesol/where-will-this-take-me/",]
    start_urls = ["https://study.unimelb.edu.au/find/interests/architecture-building-planning-and-design",
"https://study.unimelb.edu.au/find/interests/arts-humanities-and-social-sciences",
"https://study.unimelb.edu.au/find/interests/business-and-economics",
"https://study.unimelb.edu.au/find/interests/education",
"https://study.unimelb.edu.au/find/interests/engineering",
"https://study.unimelb.edu.au/find/interests/environment",
"https://study.unimelb.edu.au/find/interests/health",
"https://study.unimelb.edu.au/find/interests/information-technology-and-computer-science",
"https://study.unimelb.edu.au/find/interests/law",
"https://study.unimelb.edu.au/find/interests/music-and-visual-and-performing-arts",
"https://study.unimelb.edu.au/find/interests/science",
"https://study.unimelb.edu.au/find/interests/veterinary-agricultural-and-food-sciences", ]
    allow_domains = ["https://study.unimelb.edu.au"]
    # print(len(start_urls))
    headers_base = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    def parse(self, response):
        links = response.xpath("//span[contains(text(),'Coursework')]/../@href").extract()
        # print("links: ", links)
        department_dict = {"https://study.unimelb.edu.au/find/interests/architecture-building-planning-and-design/": "Architecture, Building and Planning",
"https://study.unimelb.edu.au/find/interests/arts-humanities-and-social-sciences/": "Arts, humanities and social sciences",
"https://study.unimelb.edu.au/find/interests/business-and-economics/": "Business and Economics",
"https://study.unimelb.edu.au/find/interests/education/": "Education",
"https://study.unimelb.edu.au/find/interests/engineering/": "Engineering",
"https://study.unimelb.edu.au/find/interests/environment/": "Environment",
"https://study.unimelb.edu.au/find/interests/health/": "Health",
"https://study.unimelb.edu.au/find/interests/information-technology-and-computer-science/": "Information Technology and Computer Science",
"https://study.unimelb.edu.au/find/interests/law/": "Law",
"https://study.unimelb.edu.au/find/interests/music-and-visual-and-performing-arts/": "Music and Visual and Performing arts",
"https://study.unimelb.edu.au/find/interests/science/": "Science",
"https://study.unimelb.edu.au/find/interests/veterinary-agricultural-and-food-sciences/": "Veterinary and Agricultural Sciences",}
        department = department_dict.get(response.url)
        # print(response.url)
        # print("dep: ", department)
        if links:
            for url in links:
                # url = "" + link
                # 使用urllib里面的parse拼接链接
                yield scrapy.Request(parse.urljoin(response.url, url), callback=self.parse_data, meta={"department": department})


    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianYanItem)
        item['university'] = "The University of Melbourne"
        print("================================================")
        print(response.url)
        item['url'] = response.url
        item['teach_time'] = 'coursework'
        item['degree_type'] = 2
        item['department'] = response.meta.get('department')
        print("item['department']: ", item['department'])
        try:
            degree_name = response.xpath("//div[@class='headline']/h1/text()|//h1[@id='page-header']//text()").extract()
            item['degree_name'] = ''.join(degree_name).strip()
            print("item['degree_name']: ", item['degree_name'])

            programme = re.findall(r"\(.*\)|\-.*", item['degree_name'])
            print(programme)
            if len(programme) > 0:
                item['degree_name'] = item['degree_name'].replace(''.join(programme), '').strip()
                item['programme_en'] = ''.join(programme).replace("(", "").replace(")", "").replace("-", "").strip()
            else:
                item['programme_en'] = item['degree_name'].replace("Master of", "").strip()
            print("item['degree_name']=: ", item['degree_name'])
            print("item['programme_en']: ", item['programme_en'])

            duration = response.xpath(
                "//div[@class='course-length icn icn-duration']/text()|//li[contains(text(),'full time')]//text()").extract()
            clear_space(duration)
            # print("duration:", duration)
            duration_list = getIntDuration(''.join(duration))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration']: ", item['duration'])
            # print("item['duration_per']: ", item['duration_per'])

            location = response.xpath(
                "//li[@id='course-overview-campus']//text()|//li[contains(text(),'Campus')]//text()").extract()
            # print(location, '==')
            item['location'] = ''.join(location).replace("On Campus", "").replace("(", "").replace(")", "").strip()
            # print("item['location']: ", item['location'])

            start_date = response.xpath(
                "//li[@id='course-overview-entryPeriods']//text()").extract()
            # print(start_date, '==')
            start_date_str = getStartDateMonth(''.join(start_date))
            item['start_date'] = start_date_str
            # print("item['start_date']: ", item['start_date'])

            overview_en = response.xpath("//div[@class='course-content']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
            # print("item['overview_en']: ", item['overview_en'])

            # 匹配跳转之后获取modules
            modules_url = response.xpath("//a[contains(text(),'What will I study?')]/@href").extract_first()
            if modules_url:
                item['modules_en'] = self.parse_modules(parse.urljoin(response.url,modules_url))
            # print("item['modules_en']: ", item['modules_en'])

            career_url = response.xpath("//a[contains(text(),'Where will this take me?')]/@href").extract_first()
            if career_url:
                item['career_en'] = self.parse_career(parse.urljoin(response.url, career_url))
            # print("item['career_en']: ", item['career_en'])

            entry_url = response.xpath("//a[contains(text(),'Entry requirements')]/@href").extract_first()
            if entry_url:
                item['rntry_requirements_en'] = self.parse_entry(parse.urljoin(response.url, entry_url))
            print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

            fee_url = response.xpath("//a[contains(text(),'Fees & scholarships')]/@href").extract_first()
            if fee_url:
                item['tuition_fee'] = self.parse_fee(parse.urljoin(response.url, fee_url))
            print("item['tuition_fee']: ", item['tuition_fee'])

            item['ielts_desc'] = "https://study.unimelb.edu.au/how-to-apply/english-language-requirements/graduate-english-language-requirements/course-specific-requirements"
            if item['department'] == "Architecture, Building and Planning":
                print("aaaaaaaaaaaaaaa")
                if "Master of Philosophy" in item['degree_name'] or "Doctor of Philosophy" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '27'
                else:
                    item["ielts"] = '6.5'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '6'
                    item["toefl"] = '79'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '21'
            elif item['department'] == "Arts, humanities and social sciences":
                if "Master of Publishing and Communications" in item[
                    'degree_name'] or "Master of Creative Writing, Publishing and Editing" in item['degree_name'] \
                        or "Master of Journalism" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '27'
                elif "Master by Research" in item['degree_name'] or "Doctor of Philosophy" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '27'
                else:
                    item["ielts"] = '6.5'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '6'
                    item["toefl"] = '79'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '21'
            elif item['department'] == "Business and Economics":
                print("bbbbbbbbbbbbbbbbbbbbbbbbbb")
                if "Master of Business Analytics" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '7'
                    item["ielts_s"] = '7'
                    item["ielts_r"] = '7'
                    item["ielts_w"] = '7'
                    item["toefl"] = '102'
                    item["toefl_l"] = '21'
                    item["toefl_s"] = '21'
                    item["toefl_r"] = '21'
                    item["toefl_w"] = '24'
                elif "Master of Business Administration" in item['degree_name'] or "Master of Marketing" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '6.5'
                    item["ielts_s"] = '6.5'
                    item["ielts_r"] = '6.5'
                    item["ielts_w"] = '6.5'
                    item["toefl"] = '102'
                    item["toefl_l"] = '21'
                    item["toefl_s"] = '21'
                    item["toefl_r"] = '21'
                    item["toefl_w"] = '24'
                elif "Master of Entrepreneurship" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '6'
                    item["toefl"] = '94'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '27'
                elif "Master of Philosophy" in item['degree_name'] or "Master of Commerce" in item['degree_name']:
                    item["ielts"] = '6.5'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '6'
                    item["toefl"] = '79'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '21'
                elif "Doctor of Philosophy" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '27'
                else:
                    item["ielts"] = '6.5'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '6'
                    item["toefl"] = '79'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '21'
            elif item['department'] == "Education":
                if "Master of Teaching" in item['degree_name'] or "Master of Educational Psychology" in item[
                    'degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '7'
                    item["ielts_s"] = '7'
                    item["ielts_r"] = '7'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '24'
                    item["toefl_s"] = '24'
                    item["toefl_r"] = '24'
                    item["toefl_w"] = '27'
                elif "Master of English in a Global Context" in item['degree_name']:
                    item["ielts"] = '6.5'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '6'
                    item["toefl"] = '79'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '21'
                else:
                    item["ielts"] = '7'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '21'
            elif item['department'] == "Engineering" or item['department'] == "Information Technology and Computer Science":
                item["ielts"] = '6.5'
                item["ielts_l"] = '6'
                item["ielts_s"] = '6'
                item["ielts_r"] = '6'
                item["ielts_w"] = '6'
                item["toefl"] = '79'
                item["toefl_l"] = '13'
                item["toefl_s"] = '18'
                item["toefl_r"] = '13'
                item["toefl_w"] = '21'
            elif "Law" in item['department']:
                if "Master of Philosophy" in item['degree_name'] or "Doctor of Philosophy" in item[
                    'degree_name'] or "JD" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '27'
                else:
                    item["ielts"] = '6.5'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '6'
                    item["toefl"] = '79'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '21'
            elif item['department'] == "Medicine, Dentistry and Health Sciences":
                if "Doctor of Clinical Dentistry" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '7'
                    item["ielts_s"] = '7'
                    item["ielts_r"] = '7'
                    item["ielts_w"] = '7'
                elif "Doctor of Dental Surgery" in item['degree_name'] or "Doctor of Medicine" in item[
                    'degree_name'] or "Doctor of Physiotherapy" in item['degree_name'] \
                        or "Master of Genetic Counselling" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '27'
                elif "Doctor of Optometry" in item['degree_name']:
                    item["ielts"] = '6.5'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '6'
                    item["toefl"] = '79'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '27'
                elif "Master of Clinical Audiology" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '7'
                    item["ielts_s"] = '7'
                    item["ielts_r"] = '7'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '24'
                    item["toefl_s"] = '24'
                    item["toefl_r"] = '24'
                    item["toefl_w"] = '27'
                elif "Master of Clinical Education" in item['degree_name'] or "Master of Clinical Ultrasound" in item[
                    'degree_name'] \
                        or "Master in Surgical Education" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '7'
                    item["ielts_s"] = '7'
                    item["ielts_r"] = '7'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '27'
                elif "Master of Medicine" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '7'
                    item["ielts_s"] = '7'
                    item["ielts_r"] = '7'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '27'
                elif "Master of Nursing Science" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '6.5'
                    item["ielts_s"] = '6.5'
                    item["ielts_r"] = '6.5'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '20'
                    item["toefl_s"] = '20'
                    item["toefl_r"] = '20'
                    item["toefl_w"] = '27'
                elif "Master of Psychiatry" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '7'
                    item["ielts_s"] = '7'
                    item["ielts_r"] = '7'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '24'
                    item["toefl_s"] = '24'
                    item["toefl_r"] = '24'
                    item["toefl_w"] = '27'
                elif "Master of Psychology" in item['degree_name'] or "Doctor of Philosophy" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '7'
                    item["ielts_s"] = '7'
                    item["ielts_r"] = '7'
                    item["ielts_w"] = '7'
                elif "Master of Social Work" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '7'
                    item["ielts_s"] = '7'
                    item["ielts_r"] = '7'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '24'
                    item["toefl_s"] = '24'
                    item["toefl_r"] = '24'
                    item["toefl_w"] = '27'
                elif "Master of Speech Pathology" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '7'
                    item["ielts_s"] = '7'
                    item["ielts_r"] = '7'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '24'
                    item["toefl_s"] = '24'
                    item["toefl_r"] = '24'
                    item["toefl_w"] = '27'
                elif "Master of Sports Medicine" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '7'
                    item["ielts_s"] = '7'
                    item["ielts_r"] = '7'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '24'
                    item["toefl_s"] = '24'
                    item["toefl_r"] = '24'
                    item["toefl_w"] = '27'
                elif "Master of Rehabilitation Science" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '7'
                    item["ielts_s"] = '7'
                    item["ielts_r"] = '7'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '24'
                    item["toefl_s"] = '24'
                    item["toefl_r"] = '24'
                    item["toefl_w"] = '27'
                elif "Masters by Research" in item['degree_name'] or "Research Doctorates" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '27'
                else:
                    item["ielts"] = '6.5'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '6'
                    item["toefl"] = '79'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '21'
            elif "Science" in item['department']:
                item["ielts"] = '6.5'
                item["ielts_l"] = '6'
                item["ielts_s"] = '6'
                item["ielts_r"] = '6'
                item["ielts_w"] = '6'
                item["toefl"] = '79'
                item["toefl_l"] = '13'
                item["toefl_s"] = '18'
                item["toefl_r"] = '13'
                item["toefl_w"] = '21'
            elif item['department'] == "Veterinary and Agricultural Sciences":
                if "Doctor of Veterinary Medicine" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '7'
                    item["toefl"] = '94'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '27'
                else:
                    item["ielts"] = '6.5'
                    item["ielts_l"] = '6'
                    item["ielts_s"] = '6'
                    item["ielts_r"] = '6'
                    item["ielts_w"] = '6'
                    item["toefl"] = '79'
                    item["toefl_l"] = '13'
                    item["toefl_s"] = '18'
                    item["toefl_r"] = '13'
                    item["toefl_w"] = '21'
            elif item['department'] == "Music and Visual and Performing arts":
                item["ielts"] = '6.5'
                item["ielts_l"] = '6'
                item["ielts_s"] = '6'
                item["ielts_r"] = '6'
                item["ielts_w"] = '6'
                item["toefl"] = '79'
                item["toefl_l"] = '13'
                item["toefl_s"] = '18'
                item["toefl_r"] = '13'
                item["toefl_w"] = '21'

            print("ielts: ", item['ielts'], ' - ', item['ielts_l'], ' - ', item['ielts_s'], ' - ', item['ielts_r'], ' - ', item['ielts_w'],)
            print("toefl: ", item['toefl'], ' - ', item['toefl_l'], ' - ', item['toefl_s'], ' - ', item['toefl_r'], ' - ', item['toefl_w'], )
            yield item
            # print("=====111")

        except Exception as e:
            with open("scrapySchool_Australian_yan/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)


    def parse_career(self, career_url):
        print("career_url: ", career_url)
        data = requests.get(career_url, headers=self.headers_base)
        response = etree.HTML(data.text)
        career = response.xpath("//div[@class='with-jumpnav']//div[@class='course-content']")
        # clear_space(modules)
        career_str = ""
        if len(career) > 0:
            for m in career:
                career_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
        career_en = remove_class(clear_lianxu_space([career_str]))
        return career_en

    def parse_modules(self, modulesUrl):
        print("modulesUrl: ", modulesUrl)
        data = requests.get(modulesUrl, headers=self.headers_base)
        response = etree.HTML(data.text)
        # print("response.url: ", data.url)
        # modules = response.xpath("//div[@id='degree-structure']")
        modules = response.xpath("//section[@id='available-subjects']")
        # clear_space(modules)
        modules_str = ""
        if len(modules) > 0:
            for m in modules:
                modules_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
        # modulesRe = re.findall(r"Next.*<", modules_str)
        # print("===", modulesRe)
        modules_en = remove_class(clear_lianxu_space([modules_str]))
        # item['modules'] = ''.join(modules)
        # if len(modulesRe) > 0:
        #     item['modules_en'] = item['modules_en'].replace(''.join(modulesRe), '<').strip()
        # print("跳转获得：modules_en: ", modules_en)
        return modules_en

    def parse_entry(self, entryUrl):
        print("entryUrl: ", entryUrl)
        data = requests.get(entryUrl, headers=self.headers_base)
        response = etree.HTML(data.text)
        driver = webdriver.Chrome(r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Lib\site-packages\selenium\chromedriver (2).exe")
        cookiedict = {"_ga": "GA1.1.1809461699.1534918500",
"uom": "00000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
"studentone_faculty": "",
"studentone_ccode": "",
"_gid": "GA1.1.634631721.1552461942",
"_fbp": "fb.2.1552461964657.625675355",
"SQ_SYSTEM_SESSION": "6o6qop02nor8m8n20jecnvdvbntg5aavi8rpqfmrlgqrbbn10vn07cp5iisjhn72p43rt5824rova88hcgvftvear6s8v864ombvhk0",
"fac": "{%22profile%22:{%22open%22:false%2C%22loggedin%22:false%2C%22qualification%22:%22postgrad%22%2C%22entry%22:%2275%22%2C%22residency%22:%22international%22%2C%22persona%22:%22secondary%22}%2C%22favourites%22:[]}",
"liveagent_oref": "",
"liveagent_ptid": "a7725fa7-d619-41cd-8a3a-5d076f70e38b",
"internal_source":"https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-secondary-internship/what-will-i-study/:",
"CONSENTMGR": "ts:1552628190791%7Cconsent:true",
"traffic_source": "(none)",
"liveagent_sid": "9a79ac41-a5c2-4d14-a927-a192e8e9573c",
"liveagent_vc": "4",
"utag_main": "v_id:0165604592d9000346cead476abf0306d005706500978$_sn:11$_ss:0$_st:1552636279696$_pn:10%3Bexp-session$ses_id:1552632639470%3Bexp-session",}
        driver.implicitly_wait(30)
        driver.get(entryUrl)
        import time
        # time.sleep(10)
        # driver.tim
        # driver.add_cookie(cookie_dict=cookiedict)
        handle = driver.current_window_handle
        entry_requirements = driver.find_element_by_xpath("//div[@class='course-content']").get_attribute('innerHTML')
        # entry_requirements = response.xpath("//div[@class='course-content']").innerhtml()

        # print("===",entry_requirements)
        # entry_requirements_str = ""
        # if len(entry_requirements) > 0:
        #     for m in [entry_requirements]:
        #         entry_requirements_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
        # entry_requirementsRe = re.findall(r"Next.*", entry_requirements_str)
        # print("entry_requirementsRe===", entry_requirementsRe)
        entry_requirements_en = remove_class(entry_requirements)
        # if len(entry_requirementsRe) > 0:
        #     entry_requirements_en = entry_requirements_en.replace(''.join(entry_requirementsRe), '<').strip()
        # driver.close()
        driver.quit()
        return entry_requirements_en

    def parse_fee(self, feeUrl):
        print("feeUrl: ", feeUrl)
        data = requests.get(feeUrl, headers=self.headers_base)
        # response = etree.HTML(data.text)
        # print("response.url: ", data.url)
        # tuition_fee = response.xpath("//span[contains(text(),'Typical annual course fee')]/following-sibling::span[1]//text()")
        tuition_fee0 = re.findall(r"""\"international\"\:\{\"ff\-indicative\":\"\$[\d,]*?\",\"ff\-year\"\:\"\$[\d,]*""", data.text)
        tuition_fee1 = re.findall(r"\"ff\-year\"\:\"\$[\d,]*", ''.join(tuition_fee0))
        print("tuition_feetmp: ", tuition_fee1)
        clear_space(tuition_fee1)
        tuition_fee = getTuition_fee(''.join(tuition_fee1).replace("$", "").replace("AUD", ""))
        # if tuition_fee == 0:
        #     item['tuition_fee'] = None
        # else:
        #     item['tuition_fee_pre'] = "AUD$"
        return tuition_fee

    def parse_apply(self, applyUrl, item):
        print("applyUrl: ", applyUrl)
        data = requests.get(applyUrl, headers=self.headers_base)
        response = etree.HTML(data.text)
        # print("response.url: ", data.url)
        how_to_apply = response.xpath("//div[@id='apply-now']|//div[@id='how-to-apply']")
        # clear_space(how_to_apply)
        how_to_apply_str = ""
        if len(how_to_apply) > 0:
            for m in how_to_apply:
                how_to_apply_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
        item['apply_desc_en'] = remove_class(clear_lianxu_space([how_to_apply_str]))
        print("跳转获得：item['apply_desc_en']: ", item['apply_desc_en'])

        deadline = response.xpath(
            "//*[contains(text(),'Application closing dates')]/../following-sibling::*[1]//text()|"
            "//strong[contains(text(),'Application Deadlines')]/../following-sibling::*[position()<3]//text()")
        item['deadline'] =clear_lianxu_space(deadline)
        print("跳转获得：item['deadline']: ", item['deadline'])

        apply_documents_en = response.xpath(
            "//h2[contains(text(),'Application Checklist')]/..")
        doc = ""
        if len(apply_documents_en) > 0:
            for a in apply_documents_en:
                doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
        item['apply_documents_en'] = remove_class(clear_lianxu_space([doc]))
        print("跳转获得：item['apply_documents_en']: ", item['apply_documents_en'])

