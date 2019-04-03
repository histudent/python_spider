# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_Australian_yan.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_yan.getItem import get_item
from scrapySchool_Australian_yan.getTuition_fee import getTuition_fee
from scrapySchool_Australian_yan.items import ScrapyschoolAustralianYanItem
from scrapySchool_Australian_yan.remove_tags import remove_class
from scrapySchool_Australian_yan.getStartDate import getStartDate
from scrapySchool_Australian_yan.getDuration import getIntDuration
from lxml import etree
import requests

class TheUniversityOfMelbourne_P_updateSpider(scrapy.Spider):
    name = "TheUniversityOfMelbourne_P_update"
    start_urls = ["https://study.unimelb.edu.au/find/courses/graduate/master-of-architectural-engineering/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-architecture/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-construction-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-construction-management/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-design-for-performance/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-civil-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-civil/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-structural/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-management/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-structures/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-landscape-architecture/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-architecture-building-and-planning/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-property/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-and-cultural-heritage/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-design/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-horticulture/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-planning/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-linguistics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-art-curatorship/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-arts-advanced-seminar-shorter-thesis/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-arts-professional-and-applied-ethics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-arts-thesis-only/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-arts-and-cultural-management/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-creative-writing-publishing-and-editing/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-criminology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-cultural-materials-conservation/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-development-studies/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-global-media-communication/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-international-journalism/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-international-relations/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-journalism/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-marketing-communications/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-public-policy-and-management/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-publishing-and-communications/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-social-policy/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-translation/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-translation-enhanced/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-actuarial-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-econometrics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-arts-thesis-only/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-business-administration/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-business-administration-part-time/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-business-analytics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-commerce-actuarial-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-economics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biomedical-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-chemical-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-civil-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-electrical-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-mechanical-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-software-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-management/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-enterprise/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-entrepreneurship/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-evaluation/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-finance/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-international-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-management/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-management-accounting-and-finance/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-management-accounting/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-management-finance/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-management-human-resources/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-management-marketing/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-marketing/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-marketing-communications/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-public-administration/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-public-administration-enhanced/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-public-policy-and-management/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-supply-chain-management/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-tax/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/executive-master-of-business-administration/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/senior-executive-master-of-business-administration/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-agribusiness/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-agricultural-sciences/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-food-and-packaging-innovation/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-food-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-agricultural-sciences/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-veterinary-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-veterinary-public-health/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-veterinary-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-veterinary-science-clinical/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-veterinary-studies/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing-practice/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing-practice-mental-health/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing-practice-nurse-practitioner/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-social-work/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-social-work-research/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-econometrics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-positive-psychology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-psychology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-biomedical-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-biostatistics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-biotechnology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-audiology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-research/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-computational-biology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-data-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-economics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-forest-ecosystem-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-educational-psychology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-energy-systems/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biochemical/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biomedical-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biomedical/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-chemical-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-chemical/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-civil/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-structures/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-environment/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-finance/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-genomics-and-health/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-geography/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-geoscience/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-health-and-human-services/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-health-and-medical-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-information-systems/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-information-technology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-nursing-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-mdhs-biomedical-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-mdhs-health-sciences/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-mdhs-medicine/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-mdhs-psychological-sciences/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-psychology-clinical-neuropsychology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-psychology-clinical-psychology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-rehabilitation-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-bioinformatics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-biosciences/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-chemistry/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-computer-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-earth-sciences/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-ecosystem-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-epidemiology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-mathematics-and-statistics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-physics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-social-work/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-speech-pathology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-sports-medicine/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-sports-rehabilitation/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-tax/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-art-curatorship/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-arts-and-cultural-management/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-contemporary-art/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-creative-writing-publishing-and-editing/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-cultural-materials-conservation/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-dance/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-design-for-performance/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-directing-for-performance/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-dramaturgy/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-film-and-television/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-fine-arts-dance/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-fine-arts-film-and-television/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-fine-arts-music-theatre/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-music-composition/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-music-interactive-composition/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-music-jazz-improvisation/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-music-music-performance/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-music-music-psychology-performance-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-music-music-therapy/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-music-musicology-ethnomusicology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-music-opera-performance/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-music-orchestral-performance/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-music-performance-teaching/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-music-therapy/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-producing/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-production-design-for-screen/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-screenwriting/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-writing-for-performance/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-banking-and-finance-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-commercial-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-competition-and-consumer-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-construction-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-employment-and-labour-relations-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-energy-and-resources-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-global-competition-and-consumer-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-health-and-medical-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-human-rights-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-intellectual-property-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-international-tax/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-law-and-development/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-laws-global-competition-and-consumer-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-laws/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-private-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-public-and-international-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-tax/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-computational-biology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-data-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-software-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-software/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-spatial/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-information-systems/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-information-systems-executive/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-information-technology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-engineering/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-bioinformatics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-computer-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-epidemiology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-mathematics-and-statistics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-adolescent-health-and-wellbeing/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing-practice/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing-practice-mental-health/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing-practice-nurse-practitioner/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-social-work/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-social-work-research/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-ageing/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-positive-psychology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-psychology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-biomedical-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-biostatistics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-biotechnology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-audiology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-education/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-research/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-teaching/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-ultrasound/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-educational-psychology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biomedical-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biomedical/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-epidemiology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-genetic-counselling/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-genomics-and-health/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-health-and-human-services/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-health-and-medical-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-medicine/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-medicine-radiology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-nursing-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-mdhs-biomedical-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-mdhs-dental-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-mdhs-health-sciences/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-mdhs-psychological-sciences/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-primary-health-care/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-psychiatry-online/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-psychology-clinical-neuropsychology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-psychology-clinical-psychology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-public-health/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-rehabilitation-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-bioinformatics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-biosciences/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-chemistry/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-epidemiology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-social-work/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-speech-pathology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-sports-medicine/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-sports-rehabilitation/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-surgery/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-surgical-education/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-surgical-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-forest-ecosystem-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-energy-systems/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-environmental/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-environment/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-engineering/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-geography/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-geoscience/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-landscape-architecture/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-laws/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-architecture-building-and-planning/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-engineering/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-law/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-biosciences/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-computer-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-earth-sciences/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-ecosystem-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-physics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-and-cultural-heritage/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-horticulture/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-architectural-engineering/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-energy-systems/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biochemical/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biomedical-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-biomedical/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-chemical-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-chemical/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-civil-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-civil/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-electrical-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-electrical/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-environmental/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-materials/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-mechanical-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-mechanical/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-mechatronics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-software-with-business/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-software/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-spatial/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-structural/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-management/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-structures/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-environment/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-engineering/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-geoscience/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-information-technology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-engineering/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-computer-science/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-earth-sciences/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-science-physics/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-positive-psychology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-teaching/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-education/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-education-research/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-educational-psychology/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-english-in-a-global-context/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-evaluation/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-instructional-leadership/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-international-education-international-baccalaureate/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-learning-intervention/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-modern-languages-education/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-music-performance-teaching/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-education/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-early-childhood-and-primary/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-early-childhood/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-primary/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-secondary/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-teaching-secondary-internship/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-tertiary-education-management/where-will-this-take-me/",
"https://study.unimelb.edu.au/find/courses/graduate/master-of-tesol/where-will-this-take-me/",]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))
    headers_base = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    def parse(self, response):
        item = get_item(ScrapyschoolAustralianYanItem)
        item['university'] = "The University of Melbourne"
        # item['country'] = 'Australia'
        # item['website'] = 'http://www.unimelb.edu.au/'
        print("================================================")
        print(response.url)
        item['url'] = response.url
        item['teach_time'] = 'coursework'
        item['degree_type'] = 2
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

            career = response.xpath("//div[@class='with-jumpnav']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            print("item['career_en']: ", item['career_en'])
            yield item
            print("=====111")
            # duration = response.xpath(
            #     "//div[@class='course-length icn icn-duration']/text()|//li[contains(text(),'full time')]//text()").extract()
            # clear_space(duration)
            # print("duration:", duration)
            # duration_list = getIntDuration(''.join(duration))
            # if len(duration_list) == 2:
            #     item['duration'] = duration_list[0]
            #     item['duration_per'] = duration_list[-1]
            # print("item['duration']: ", item['duration'])
            # print("item['duration_per']: ", item['duration_per'])
            #
            # location = response.xpath(
            #     "//div[@class='course-location icn icn-location']//text()|//li[contains(text(),'campus')]//text()").extract()
            # item['location'] = ''.join(location).strip()
            # print("item['location']: ", item['location'])
        except Exception as e:
            with open("scrapySchool_Australian_yan/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

        # for link in links:
        #     url = "https://coursesearch.unimelb.edu.au" + link
        #     yield scrapy.Request(url, callback=self.parse_url)

    def parse_url(self, response):
        degree_description = response.xpath("//div[@class='description']").extract()
        degree_description = remove_class(clear_lianxu_space(degree_description))
        # print("degree_description: ", degree_description)

        duration = response.xpath("//div[@class='course-length icn icn-duration']//text()").extract()
        clear_space(duration)
        duration = ''.join(duration)
        # print("duration: ", duration)

        degree_name = response.xpath("//div[@class='headline']/h1//text()").extract()
        clear_space(degree_name)
        degree_name = ''.join(degree_name)
        # print("degree_name: ", degree_name)

        location = response.xpath("//div[@class='course-location icn icn-location']//text()").extract()
        clear_space(location)
        location = ''.join(location)
        # print("location: ", location)

        start_date = response.xpath("//div[@class='course-entry']//text()").extract()
        clear_space(start_date)
        start_date = ''.join(start_date)
        # print("start_date: ", start_date)

        category = response.xpath("//span[@class='category']//text()").extract()
        category = ''.join(category).strip()
        # print("category: ", category)
        teach_time = ""
        degree_type = None
        if category == "Doctors/Masters Level":
            teach_time = 'coursework'
            degree_type = 2
        # elif category == "Research":
        #     teach_time = 'research'
        #     degree_type = 3
        link = response.xpath("//a[@class='button']/@href").extract()
        link = ''.join(link)
        if len(teach_time) != "" and degree_type != None:
#             links = ["https://law.unimelb.edu.au/study/masters/courses/502cw",
# "https://online.unimelb.edu.au/education/international-baccalaureate/master-of-education-international-baccalaureate",
# "https://commercial.unimelb.edu.au/custom-education/search-courses/optometry/clinicaloptometry",
# "https://online.unimelb.edu.au/business-and-management/ageing-in-society/master-of-ageing",
# "https://online.unimelb.edu.au/medicine-and-public-health/rehabilitation-science/master-of-rehabilitation-science",
# "https://online.unimelb.edu.au/medicine-and-public-health/psychiatry/master-of-psychiatry",
# "https://mbs.edu/education-development/degreeprograms/fulltimemba",
# "https://online.unimelb.edu.au/education/clinical-teaching/master-of-clinical-teaching",
# "https://online.unimelb.edu.au/law-courses/global-competition-and-consumer-law/llm-global-competition-and-consumer-law",
# "https://mbs.edu/education-development/degreeprograms/ftmom",
# "https://online.unimelb.edu.au/information-technology/information-systems-executive/master-of-information-systems-executive",
# "https://online.unimelb.edu.au/business-and-management/evaluation/master-of-evaluation",
# "https://online.unimelb.edu.au/medicine-and-public-health/sports-rehabilitation/master-of-sports-rehabilitation",
# "https://online.unimelb.edu.au/medicine-and-public-health/sports-medicine/master-of-sports-medicine",
# "https://online.unimelb.edu.au/medicine-and-public-health/health-and-human-services/master-of-health-and-human-services",
# "https://law.unimelb.edu.au/study/masters/courses/277aa",
# "https://online.unimelb.edu.au/medicine-and-public-health/social-work/master-of-advanced-social-work",
# "https://online.unimelb.edu.au/education/tertiary-education-management/master-of-tertiary-education",
# "https://online.unimelb.edu.au/law-courses/global-competition-and-consumer-law/master-of-global-competition-and-consumer-law",
# "https://commercial.unimelb.edu.au/custom-education/search-courses/health-medical/youthmentalhealthm",
# "https://law.unimelb.edu.au/study/masters/courses/742ab",
# "https://commercial.unimelb.edu.au/custom-education/courses/narrativetherapy",
# "https://law.unimelb.edu.au/study/jd",
# "https://law.unimelb.edu.au/study/masters/courses/504aa",]
#             for link in links:
            yield scrapy.Request(link, callback=self.parse_data,
                                 meta={"degree_description": degree_description, "duration": duration, "location": location,
                                       "degree_name": degree_name, "start_date": start_date, "degree_type": degree_type,"teach_time": teach_time})

    def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianYanItem)
        item['university'] = "The University of Melbourne"
        # item['country'] = 'Australia'
        # item['website'] = 'http://www.unimelb.edu.au/'
        item['url'] = response.url
        print("===========================")
        print(response.url)
        degree_type = response.meta['degree_type']
        item['degree_type'] = degree_type
        print("item['degree_type']: ", item['degree_type'])

        teach_time = response.meta['teach_time']
        item['teach_time'] = teach_time
        print("item['teach_time']: ", item['teach_time'])

        degree_description = response.meta['degree_description']
        item['degree_overview_en'] = degree_description
        # print("item['degree_overview_en']: ", item['degree_overview_en'])

        duration = response.meta['duration']
        if len(duration) == 0:
            duration = response.xpath("//h1[@class='page-title']/following-sibling::*[1]//text()|"
                                      "//p[contains(text(), 'full-time')]//text()|//p[contains(text(), 'full time')]//text()").extract()
        durationList = re.findall(r".{1,15}full.{1}time", duration)
        print(durationList)
        dur_re = re.findall(r".{1,15}year", ''.join(durationList))
        if len(dur_re) != 0:
            item['duration'] = ','.join(dur_re).strip().strip(',').strip()
        print("item['duration']: ", item['duration'])
        # duration_list = getIntDuration(''.join(durationList))
        # if len(duration_list) == 2:
        #     item['duration'] = duration_list[0]
        #     item['duration_per'] = duration_list[-1]
        # print("item['duration_per']: ", item['duration_per'])

        location = response.meta['location']
        item['location'] = location
        print("item['location']: ", item['location'])

        degree_name = response.meta['degree_name']
        item['degree_name'] = degree_name
        print("item['degree_name']: ", item['degree_name'])

        programme =re.findall(r"Teaching\s\(.+\)$|\(.+\)$", item['degree_name'])
        clear_space(programme)
        if "Teaching" in ''.join(programme):
            item['programme_en'] = ''.join(programme).strip()
        else:
            item['programme_en'] = ''.join(programme).replace("(", "").replace(")", "").strip()
        if item['programme_en'] == "":
            item['programme_en'] = item['degree_name'].replace("Master of", "").replace("Doctor of", "").strip()
        print("item['programme_en']: ", item['programme_en'])

        # start_date = response.meta['start_date']
        # print("start_date: ", start_date)
        # item['start_date'] = start_date
        # print("item['start_date']: ", item['start_date'])
        try:
            department = response.xpath("//li[@class='root']/a/span/text()|//img[@src='https://education.unimelb.edu.au/__data/assets/image/0006/1675995/Horizontal-180mm-new.png']/@alt|//a[@class='page-header-home']//text()").extract()
            clear_space(department)
            item['department'] = ''.join(department).replace("Courses -", "").replace(", shaping minds shaping the world", "").strip()
            if item['department'] == "":
                if "mbs.edu" in response.url:
                    item['department'] = "Melbourne Business School"
            print("item['department']: ", item['department'])

            overview = response.xpath("//div[@id='overview']//p[@class='course-ctas']/preceding-sibling::*|"
                                      "//div[@class='article']//p[@class='course-ctas']/preceding-sibling::*|//div[@class='lead']|"
                                      "//div[@class='lead']/following-sibling::div[1]|//section[@class='lead']/..|"
                                      "//section[@class='lead']/../following-sibling::div[1]|"
                                      "//a[contains(text(),'Calendar')]/../preceding-sibling::*[position()<last()-1]").extract()
            clear_space(overview)
            if len(overview) == 0:
                # //html//tr[5]
                overview = response.xpath("//html//tr[5]|//div[@id='overview']").extract()
                clear_space(overview)
            overviewRe = re.findall(r"Next.*?<", ''.join(overview))
            # print("===", overviewRe)
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            if len(overviewRe) > 0:
                item['overview_en'] = item['overview_en'].replace(''.join(overviewRe),'<').strip()
            print("item['overview_en']: ", item['overview_en'])

            career = response.xpath("//h2[contains(text(),'Career outcomes')]/preceding-sibling::*[1]/following-sibling::*|"
                                    "//h2[contains(text(),'Career outcomes')]/preceding-sibling::*[1]/following-sibling::*[position()<6]|"
                                    "//strong[contains(text(),'Career opportunities')]/../preceding-sibling::*[1]/following-sibling::*[position()<13]").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            print("item['career_en']: ", item['career_en'])

            modules = response.xpath("//div[@id='course-structure']|//div[@id='subjects']|"
                                     "//a[contains(text(),'Subjects and structure')]/../preceding-sibling::*[1]/following-sibling::*[position()<3]|"
                                     "//div[@id='course-structure']|//h2[contains(text(),'Course structure')]/preceding-sibling::*[1]/following-sibling::*[position()<8]").extract()
            clear_space(modules)
            if len(modules) == 0:
                modules = response.xpath("//html//tr[9]").extract()
                clear_space(modules)
            modulesRe = re.findall(r"Next.*<", ''.join(modules))
            # print("===", modulesRe)
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            if len(modulesRe) > 0:
                item['modules_en'] = item['modules_en'].replace(''.join(modulesRe),'<').strip()
            print("item['modules_en']: ", item['modules_en'])

            entry_requirements = response.xpath("//div[@id='entry-requirements']|"
                                                "//h2[contains(text(),'Entry requirements')]/preceding-sibling::*[1]/following-sibling::*[position()<5]").extract()
            if len(entry_requirements) == 0:
                entry_requirements = response.xpath("//html//tr[13]").extract()
            entry_requirementsRe = re.findall(r"Next.*", ''.join(entry_requirements))
            # print("entry_requirementsRe===", entry_requirementsRe)
            item['rntry_requirements_en'] = remove_class(clear_lianxu_space(entry_requirements))
            if len(entry_requirementsRe) > 0:
                item['rntry_requirements_en'] = item['rntry_requirements_en'].replace(''.join(entry_requirementsRe),'<').strip()
            print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

            item['ielts_desc'] = "https://futurestudents.unimelb.edu.au/admissions/entry-requirements/language-requirements/graduate-toefl-ielts"
            if item['department'] == "Melbourne School of Design":
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
            elif item['department'] == "Faculty of Arts" or item['department'] == "Graduate School of Humanities and Social Sciences":
                if "Master of Publishing and Communications" in item['degree_name'] or "Master of Creative Writing, Publishing and Editing" in item['degree_name'] \
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
            elif item['department'] == "Melbourne Business School":
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
            elif item['department'] == "Melbourne Graduate School of Education":
                if "Master of Teaching" in item['degree_name'] or "Master of Educational Psychology" in item['degree_name']:
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
            elif item['department'] == "Melbourne School of Engineering" or item['department'] == "Melbourne School of Information":
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
            elif "Melbourne Law School" in item['department'] or item['department'] == "Melbourne School of Government":
                if "Master of Philosophy" in item['degree_name'] or "Doctor of Philosophy" in item['degree_name'] or "JD" in item['degree_name']:
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
            elif item['department'] == "Faculty of Medicine, Dentistry and Health Sciences":
                if "Doctor of Clinical Dentistry" in item['degree_name']:
                    item["ielts"] = '7'
                    item["ielts_l"] = '7'
                    item["ielts_s"] = '7'
                    item["ielts_r"] = '7'
                    item["ielts_w"] = '7'
                elif "Doctor of Dental Surgery" in item['degree_name'] or "Doctor of Medicine" in item['degree_name'] or "Doctor of Physiotherapy" in item['degree_name'] \
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
                elif "Master of Clinical Education" in item['degree_name'] or "Master of Clinical Ultrasound" in item['degree_name'] \
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
            elif "Faculty of Science" in item['department'] or item['department'] == "Melbourne Graduate School of Science" or "Faculty of Fine Arts and Music" in item['department'] or item['department'] == "Victorian College of the Arts" or item['department'] == "Melbourne Conservatorium of Music":
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
            elif item['department'] == "Faculty of Veterinary and Agricultural Sciences":
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

            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #                     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))
            # print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
            #                     item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))


            how_to_apply = response.xpath("//div[@id='apply-now']|"
                                          "//a[contains(text(),'Applying')]/../preceding-sibling::*[1]/following-sibling::*[position()<3]|"
                                          "//div[@id='how-to-apply']").extract()
            item['apply_desc_en'] = remove_class(clear_lianxu_space(how_to_apply))
            print("item['apply_desc_en']: ", item['apply_desc_en'])

            # //h3[contains(text(),'Application closing dates')]/following-sibling::*[1]
            deadline = response.xpath(
                "//h3[contains(text(),'Application closing dates')]/following-sibling::*[1]//text()|"
                "//h2[contains(text(),'Application deadlines')]/following-sibling::ul[1]//text()").extract()
            if len(deadline) == 0:
                deadline = response.xpath(
                    "//div[@id='how-to-apply']//h5[contains(text(),'International')]/following-sibling::p[1]//text()").extract()
                if len(deadline) > 0:
                    deadline = [getStartDate(deadline[0])]
            item['deadline'] = clear_lianxu_space(deadline)
            print("item['deadline']: ", item['deadline'])

            apply_documents_en = response.xpath(
                "//strong[contains(text(),'To apply, you will need to provide:')]/../preceding-sibling::*[1]/following-sibling::*[position()<3]|"
                "//h3[contains(text(),'To apply, you will need to provide:')]/preceding-sibling::*[1]/following-sibling::*[position()<3]|"
                "//div[@class='ct-checklist']|//h3[contains(text(),'Supporting documentation')]/preceding-sibling::*[1]/following-sibling::*").extract()
            item['apply_documents_en'] = remove_class(clear_lianxu_space(apply_documents_en))
            print("item['apply_documents_en']: ", item['apply_documents_en'])

            # //h3[@id='application-process']/preceding-sibling::*[1]/following-sibling::*[position()<9]
            apply_proces_en = response.xpath(
                "//h3[@id='application-process']/preceding-sibling::*[1]/following-sibling::*[position()<9]").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(apply_proces_en))
            print("item['apply_proces_en']: ", item['apply_proces_en'])

            tuition_fee =response.xpath("//div[@id='entry-requirements']/following-sibling::div[1]//table/tbody/tr/td[1]//text()|"
                                        "//div[@id='fees-and-scholarships']//td[contains(text(),'International')]/following-sibling::td[last()]//text()|"
                                        "//h2[contains(text(),'Fees')]/..//th[@id='course']/following-sibling::*[last()]//text()|"
                                        "//td[@data-label='Cost']//text()|"
                                        "//strong[contains(text(),'TOTALS')]/../../following-sibling::*[last()]//text()|"
                                        "//td[@data-label='Cost']//text()").extract()
            clear_space(tuition_fee)
            if len(tuition_fee) == 0:
                tuition_fee = response.xpath("//html//tr[14]//text()").extract()
                clear_space(tuition_fee)
            print("tuition_fee: ", tuition_fee)

            # for feeIndex in range(len(tuition_fee)):
            #     feeRe = re.findall(r"\d+,\d+", tuition_fee[feeIndex])
            #     if len(feeRe) != 0:
            #         tuition_fee[feeIndex] = ''.join(feeRe).replace(",", "")
            #     print("***tuition_fee: ", tuition_fee)
            #     maxfee = 0
            #     for fee in tuition_fee:
            #         if fee >= maxfee:
            #             maxfee = int(fee)
            #     if maxfee != 0:
            #         item['tuition_fee'] = maxfee
            #         item['tuition_fee_pre'] = "AUD$"
            if len(tuition_fee) > 0:
                item['tuition_fee'] = getTuition_fee(''.join(tuition_fee))
                item['tuition_fee_pre'] = "AUD$"
            if item['tuition_fee'] == 0:
                item['tuition_fee'] = None
            print("item['tuition_fee']: ", item['tuition_fee'])

            if item['department'] == "Melbourne Law School" and item['modules_en'] == "":
                law_url = response.xpath("//a[@href='https://law.unimelb.edu.au/study/masters']/@href").extract()
                if len(law_url) > 0:
                    self.parse_law_mes(law_url[0], item)

            urlCom = re.findall("/overview$", response.url)
            # print("urLCom：", urlCom)
            urlRes = ''.join(urlCom)
            if len(urlCom) != 0:
                urlRes = ''.join(response.url.split(''.join(urlCom)))
            print("urlRes：", urlRes)

            if urlRes:
                # print("==============11")
                modulesUrl = urlRes + "/degree-structure"
                # print(modulesUrl,"------")
                self.parse_modules(modulesUrl, item)
                entryUrl = urlRes + "/entry-requirements"
                self.parse_entry(entryUrl, item)
                applyUrl = urlRes + "/apply-now"
                self.parse_apply(applyUrl, item)
                feeUrl = urlRes + "/fees-scholarships"
                self.parse_fee(feeUrl, item)

            if len(item['deadline']) > 150:
                item['deadline'] = item['deadline'][:151]
            yield item
        except Exception as e:
            with open("scrapySchool_Australian_yan/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_law_mes(self, law_url, item):
        print("law_url: ", law_url)
        data = requests.get(law_url, headers=self.headers_base)
        response = etree.HTML(data.text)
        overview_en = response.xpath("//div[@id='new_content_container_1634204']")
        overview_en_str = ""
        if len(overview_en) > 0:
            for m in overview_en:
                overview_en_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
        item['overview_en'] = remove_class(clear_lianxu_space([overview_en_str]))

        modules = response.xpath("//div[@id='courses']")
        modules_str = ""
        if len(modules) > 0:
            for m in modules:
                modules_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
        modulesRe = re.findall(r"Next.*<", modules_str)
        # print("===", modulesRe)
        item['modules_en'] = remove_class(clear_lianxu_space([modules_str]))
        if len(modulesRe) > 0:
            item['modules_en'] = item['modules_en'].replace(''.join(modulesRe), '<').strip()
        print("跳转获得：item['modules_en']1: ", item['modules_en'])

    def parse_modules(self, modulesUrl, item):
        print("modulesUrl: ", modulesUrl)
        data = requests.get(modulesUrl, headers=self.headers_base)
        response = etree.HTML(data.text)
        # print("response.url: ", data.url)
        # modules = response.xpath("//div[@id='degree-structure']")
        modules = response.xpath("//div[@class='layout-sidebar__main__inner box']/div[1]")
        # clear_space(modules)
        modules_str = ""
        if len(modules) > 0:
            for m in modules:
                modules_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
        modulesRe = re.findall(r"Next.*<", modules_str)
        # print("===", modulesRe)
        item['modules_en'] = remove_class(clear_lianxu_space([modules_str]))
        # item['modules'] = ''.join(modules)
        if len(modulesRe) > 0:
            item['modules_en'] = item['modules_en'].replace(''.join(modulesRe), '<').strip()
        print("跳转获得：item['modules_en']1: ", item['modules_en'])

    def parse_entry(self, entryUrl, item):
        print("entryUrl: ", entryUrl)
        data = requests.get(entryUrl, headers=self.headers_base)
        response = etree.HTML(data.text)
        # print("response.url: ", data.url)
        entry_requirements = response.xpath("//div[@id='entry-requirements']")
        entry_requirements_str = ""
        if len(entry_requirements) > 0:
            for m in entry_requirements:
                entry_requirements_str += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
        entry_requirementsRe = re.findall(r"Next.*", entry_requirements_str)
        # print("entry_requirementsRe===", entry_requirementsRe)
        item['rntry_requirements_en'] = remove_class(clear_lianxu_space([entry_requirements_str]))
        if len(entry_requirementsRe) > 0:
            item['rntry_requirements_en'] = item['rntry_requirements_en'].replace(''.join(entry_requirementsRe), '<').strip()
        # item['entry_requirements'] = ''.join(entry_requirements)
        print("跳转获得：item['rntry_requirements_en']1: ", item['rntry_requirements_en'])

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

    def parse_fee(self, feeUrl, item):
        print("feeUrl: ", feeUrl)
        data = requests.get(feeUrl, headers=self.headers_base)
        response = etree.HTML(data.text)
        # print("response.url: ", data.url)
        tuition_fee = response.xpath("//div[@class='pricing']/h3//text()")
        clear_space(tuition_fee)
        item['tuition_fee'] = getTuition_fee(''.join(tuition_fee).replace("$", "").replace("AUD", ""))
        if item['tuition_fee'] == 0:
            item['tuition_fee'] = None
        else:
            item['tuition_fee_pre'] = "AUD$"
        print("跳转获得：item['tuition_fee']1: ", item['tuition_fee'])
