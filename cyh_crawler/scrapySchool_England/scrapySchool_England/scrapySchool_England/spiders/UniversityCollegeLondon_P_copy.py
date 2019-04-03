# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
# from scrapySchool_England.middlewares import clear_duration,tracslateDate
from scrapySchool_England.clearSpace import clear_same_s
import requests
from lxml import etree
class UniversitycollegelondonPSpider(scrapy.Spider):
    name = 'UniversityCollegeLondon_P'
    allowed_domains = ['ucl.ac.uk']
    start_urls = ['https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/english-education-ma']
    # count=1
    # start_urls = []
    def parse(self, response):
        urls=['https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/engineering-international-development-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/english-education-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/environment-politics-society-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/environmental-modelling-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/ethnographic-documentary-film-practical-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/european-culture-thought-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/european-history-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/modern-european-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/experimental-pharmacology-therapeutics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/financial-systems-engineering-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/genetics-human-disease-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/geography-education-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/geospatial-sciences-geographic-information-science-computing-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/global-migration-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-humanities-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-psychology-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-wellbeing-sustainable-buildings-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/higher-education-management-mba',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/higher-education-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/history-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/human-evolution-behaviour-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/human-rights-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/human-tissue-repair-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/human-computer-interaction-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/infection-immunity-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/information-science-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/information-studies-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/infrastructure-planning-appraisal-development-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/photonics-systems-development-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/inter-disciplinary-urban-design-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/international-public-policy-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/landscape-architecture-mla',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-sciences-development-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-sciences-linguistics-neuroscience-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-sciences-neuroscience-communication-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-sciences-sign-language-studies-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-sciences-speech-hearing-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/late-antique-byzantine-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/leadership-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/legal-political-theory-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/management-complex-projects-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/materials-energy-environment-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/mathematical-modelling-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/medicinal-natural-products-phytochemistry-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/mediterranean-archaeology-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/mental-health-sciences-research-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/modelling-biological-complexity-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/molecular-modelling-materials-science-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/museums-galleries-education-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/neuromuscular-diseases-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/neuroscience-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/ophthalmology-clinical-practice-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/oral-surgery-mclindent',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/oral-surgery-advanced-training-mclindent',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/paediatrics-child-health-clinical-practice-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/child-health-advanced-paediatrics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/paediatrics-child-health-molecular-genomic-paediatrics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/palaeoanthropology-palaeolithic-archaeology-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/philosophy-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/philosophy-politics-economics-health-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/physical-therapy-musculoskeletal-healthcare-rehabilitation-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/physics-engineering-medicine-biomedical-imaging-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/physiotherapy-studies-paediatrics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/politics-violence-crime-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/prenatal-genetics-fetal-medicine-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/primary-education-policy-practice-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/professional-education-training-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/public-archaeology-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/public-diplomacy-global-communication-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/quantum-technologies-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/reproductive-science-womens-health-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/research-methods-archaeology-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/risk-disaster-reduction-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/risk-disaster-science-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/russian-east-european-literature-culture-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/russian-post-soviet-politics-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/russian-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/scientific-computing-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/smart-cities-urban-analytics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/social-cognition-research-applications-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/social-research-methods-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/sociology-education-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/space-risk-disaster-reduction-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/space-science-engineering-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/spatial-syntax-architecture-cities-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/spatial-data-science-visualisation-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/spatial-planning-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/special-inclusive-education-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/special-care-dentistry-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/speech-language-communication-needs-schools-advanced-practice-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/strategic-management-projects-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/synthetic-biology-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/technology-management-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/telecommunications-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/telecommunications-business-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/translation-translation-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/transnational-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/united-states-studies-history-politics-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-economic-development-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-innovation-policy-mpa',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-studies-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/web-science-big-data-analytics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-physiotherapy-paediatrics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/anthropology-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/applied-analytical-chemistry-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/applied-research-human-communication-disorders-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/aquatic-science-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/architectural-computation-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/architectural-history-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/architecture-historic-urban-environments-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/architecture-march-arb-riba-2',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/art-design-education-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/astrophysics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/audiological-science-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/biointegrated-design-march',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/biochemical-engineering-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/biological-physics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/brain-mind-sciences-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/burns-plastic-reconstructive-surgery-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/business-administration-mba',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/cancer-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/cardiovascular-science-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/caribbean-latin-american-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/central-south-east-european-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/chemical-research-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/child-health-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/chinese-health-humanity-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/civil-engineering-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/civil-engineering-infrastructure-planning-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/civil-engineering-seismic-design-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-drug-development-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-drug-development-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-mental-health-sciences-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-neuroscience-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/cognitive-neuroscience-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/comparative-literature-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/computational-finance-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/computational-statistics-machine-learning-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/computer-graphics-vision-imaging-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/computer-science-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/countering-organised-crime-terrorism-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/curriculum-pedagogy-assessment-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/data-science-machine-learning-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/dementia-causes-treatments-research-neuroscience-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/dental-public-health-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/design-manufacture-march',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/development-technology-innovation-policy-mpa',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/developmental-neuroscience-psychopathology-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/digital-innovation-built-asset-management-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/drug-design-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/drug-discovery-development-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/early-modern-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/early-years-education-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/eating-disorders-clinical-nutrition-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/economy-state-society-politics-security-international-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-psychology-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-gender-international-development-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/educational-assessment-ma',]
        for u in urls:
            yield scrapy.Request(url=u,callback=self.parses,meta={'url':u})
    def parses(self,response):
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university'] = 'University College London'
        item['url'] = response.meta['url']
        print(response.url)
        tuition=response.xpath('//strong[contains(text(),"Overseas")]/following-sibling::span[1]/text()').extract()
        print(tuition)
        tui=re.findall('\d{2}\,\d{3}',''.join(tuition))
        item['tuition_fee']=''.join(tui).replace(',','').strip()
        if tui!=[]:
            yield item

    def parsess(self, response):
        url_list=['https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-physiotherapy-paediatrics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/anthropology-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/applied-analytical-chemistry-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/applied-research-human-communication-disorders-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/aquatic-science-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/architectural-computation-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/architectural-history-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/architecture-historic-urban-environments-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/architecture-march-arb-riba-2',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/art-design-education-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/astrophysics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/audiological-science-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/biointegrated-design-march',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/biochemical-engineering-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/biological-physics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/brain-mind-sciences-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/burns-plastic-reconstructive-surgery-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/business-administration-mba',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/cancer-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/cardiovascular-science-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/caribbean-latin-american-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/central-south-east-european-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/chemical-research-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/child-health-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/chinese-health-humanity-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/civil-engineering-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/civil-engineering-infrastructure-planning-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/civil-engineering-seismic-design-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-drug-development-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-drug-development-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-mental-health-sciences-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-neuroscience-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/cognitive-neuroscience-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/comparative-literature-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/computational-finance-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/computational-statistics-machine-learning-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/computer-graphics-vision-imaging-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/computer-science-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/countering-organised-crime-terrorism-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/curriculum-pedagogy-assessment-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/data-science-machine-learning-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/dementia-causes-treatments-research-neuroscience-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/dental-public-health-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/design-manufacture-march',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/development-technology-innovation-policy-mpa',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/developmental-neuroscience-psychopathology-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/digital-innovation-built-asset-management-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/drug-design-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/drug-discovery-development-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/early-modern-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/early-years-education-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/eating-disorders-clinical-nutrition-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/economy-state-society-politics-security-international-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-psychology-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-gender-international-development-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/educational-assessment-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/engineering-international-development-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/english-education-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/environment-politics-society-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/environmental-modelling-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/ethnographic-documentary-film-practical-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/european-culture-thought-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/european-history-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/modern-european-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/experimental-pharmacology-therapeutics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/financial-systems-engineering-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/genetics-human-disease-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/geography-education-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/geospatial-sciences-geographic-information-science-computing-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/global-migration-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-humanities-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-psychology-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-wellbeing-sustainable-buildings-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/higher-education-management-mba',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/higher-education-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/history-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/human-evolution-behaviour-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/human-rights-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/human-tissue-repair-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/human-computer-interaction-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/infection-immunity-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/information-science-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/information-studies-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/infrastructure-planning-appraisal-development-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/photonics-systems-development-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/inter-disciplinary-urban-design-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/international-public-policy-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/landscape-architecture-mla',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-sciences-development-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-sciences-linguistics-neuroscience-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-sciences-neuroscience-communication-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-sciences-sign-language-studies-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-sciences-speech-hearing-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/late-antique-byzantine-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/leadership-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/legal-political-theory-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/management-complex-projects-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/materials-energy-environment-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/mathematical-modelling-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/medicinal-natural-products-phytochemistry-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/mediterranean-archaeology-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/mental-health-sciences-research-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/modelling-biological-complexity-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/molecular-modelling-materials-science-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/museums-galleries-education-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/neuromuscular-diseases-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/neuroscience-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/ophthalmology-clinical-practice-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/oral-surgery-mclindent',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/oral-surgery-advanced-training-mclindent',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/paediatrics-child-health-clinical-practice-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/child-health-advanced-paediatrics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/paediatrics-child-health-molecular-genomic-paediatrics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/palaeoanthropology-palaeolithic-archaeology-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/philosophy-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/philosophy-politics-economics-health-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/physical-therapy-musculoskeletal-healthcare-rehabilitation-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/physics-engineering-medicine-biomedical-imaging-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/physiotherapy-studies-paediatrics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/politics-violence-crime-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/prenatal-genetics-fetal-medicine-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/primary-education-policy-practice-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/professional-education-training-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/public-archaeology-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/public-diplomacy-global-communication-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/quantum-technologies-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/reproductive-science-womens-health-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/research-methods-archaeology-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/risk-disaster-reduction-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/risk-disaster-science-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/russian-east-european-literature-culture-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/russian-post-soviet-politics-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/russian-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/scientific-computing-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/smart-cities-urban-analytics-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/social-cognition-research-applications-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/social-research-methods-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/sociology-education-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/space-risk-disaster-reduction-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/space-science-engineering-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/spatial-syntax-architecture-cities-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/spatial-data-science-visualisation-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/spatial-planning-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/special-inclusive-education-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/special-care-dentistry-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/speech-language-communication-needs-schools-advanced-practice-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/strategic-management-projects-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/synthetic-biology-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/technology-management-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/telecommunications-mres',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/telecommunications-business-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/translation-translation-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/transnational-studies-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/united-states-studies-history-politics-ma',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-economic-development-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-innovation-policy-mpa',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-studies-msc',
'https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/web-science-big-data-analytics-msc',]
        url_list=['https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/crime-forensic-science-msc','https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/geoscience-msc']
        for u in url_list:
            data = requests.get(u)
            response=etree.HTML(data.content)
            item = get_item1(ScrapyschoolEnglandItem1)
            item['university'] = 'University College London'
            item['url'] = data.url
            item['tuition_fee_pre'] = '£'
            location = response.xpath('//div/strong[contains(text(),"Location")]/../text()')
            location = ''.join(location).strip()
            item['location'] = location
            programme = response.xpath('//h1[@class="heading"]//text()')
            programme = ''.join(programme)
            degree_name = re.findall('[MB][A-Z]{1,2}[a-z]*', programme)
            degree_name = ''.join(set(degree_name)).strip()
            programme = programme.replace(degree_name, '')
            item['programme_en'] = programme
            item['degree_name'] = degree_name
            item['degree_type'] = '2'

            mode = response.xpath('//*[contains(text(),"FT")]//text()')
            if mode != []:
                item['teach_time'] = 1
            else:
                item['teach_time'] = 2

            department = response.xpath(
                '//h5[contains(text(),"Department website")]/following-sibling::p/a/text()')
            department = ''.join(department).strip()
            item['department'] = department

            overview = response.xpath('//article[@class="article"]/h1/following-sibling::article/p[1]')
            overview = self.takeTag(overview)
            overview = remove_class(overview)
            item['overview_en'] = overview

            application_open_date = response.xpath('//div[contains(text(),"Open")]/text()')
            application_open_date = tracslateDate(application_open_date)
            application_open_date = ','.join(set(application_open_date))
            item['application_open_date'] = application_open_date

            deadline = response.xpath('//div[contains(text(),"Close")]/text()')
            deadline = tracslateDate(deadline)
            deadline = ','.join(set(deadline))
            item['deadline'] = deadline

            tuition_fee = getTuition_fee(response.xpath('//*[contains(text(),"£")]//text()'))
            item['tuition_fee'] = tuition_fee

            duration = response.xpath('//h4[contains(text(),"uration")]/following-sibling::div/text()')
            duration = clear_duration(duration)
            item['duration'] = duration['duration']
            item['duration_per'] = duration['duration_per']

            start_date = response.xpath('//h4[contains(text(),"tarts")]/following-sibling::p//text()')
            start_date = tracslateDate(start_date)
            start_date = ','.join(set(start_date))
            item['start_date'] = start_date

            item['apply_fee'] = '75'
            item['apply_pre'] = '£'

            eng_level = response.xpath('//p[contains(text(),"English language")]/strong/text()')
            eng_level = ''.join(eng_level).strip()
            if eng_level == 'Standard':
                ielts = 'Overall grade of 6.5 with a minimum of 6.0 in each of the subtests.'
                toefl = 'Overall score of 92 with 24/30 in reading and writing and 20/30 in speaking and listening.'
            elif eng_level == 'Good':
                ielts = 'Overall grade of 7.0 with a minimum of 6.5 in each of the subtests.'
                toefl = 'Overall score of 100 with 24/30 in reading and writing and 20/30 in speaking and listening.'
            elif eng_level == 'Advanced':
                ielts = 'Overall grade of 7.5 with a minimum of 6.5 in each of the subtests.'
                toefl = 'Overall score of 109 with 24/30 in reading and writing and 20/30 in speaking and listening.'
            else:
                ielts = ''
                toefl = ''
            ieltss = get_ielts(ielts)
            if ieltss != {} and ieltss != []:
                item['ielts_l'] = ieltss['IELTS_L']
                item['ielts_s'] = ieltss['IELTS_S']
                item['ielts_r'] = ieltss['IELTS_R']
                item['ielts_w'] = ieltss['IELTS_W']
                item['ielts'] = ieltss['IELTS']
            toefls = re.findall('\d{1,3}', ''.join(toefl))
            if len(toefls) == 5:
                item['toefl'] = toefls[0]
                item['toefl_l'] = toefls[4]
                item['toefl_w'] = toefls[2]
                item['toefl_r'] = toefls[1]
                item['toefl_s'] = toefls[3]
            elif len(toefls) == 2:
                toefls = list(map(int, toefls))
                item['toefl'] = max(toefls)
                item['toefl_l'] = min(toefls)
                item['toefl_w'] = min(toefls)
                item['toefl_r'] = min(toefls)
                item['toefl_s'] = min(toefls)
            item['ielts_desc'] = ielts
            item['toefl_desc'] = toefl

            rntry_requirements = response.xpath('//h4[contains(text(),"ntry")]/following-sibling::p[1]')
            rntry_requirements = self.takeTag(rntry_requirements)
            rntry_requirements = remove_class(rntry_requirements)
            # print(rntry_requirements)
            item['rntry_requirements'] = rntry_requirements

            chinese_reuqirement = ["<div>Equivalent qualifications for China",
                                   "Bachelor's degree with a minimum overall average mark of 80%. Please note that a number of programmes / departments will require higher marks.",
                                   "ALTERNATIVE QUALIFICATIONS",
                                   "Medical/ Dental/ Master's degree; Doctorate.</div>", ]
            chinese_reuqirement = '\n'.join(chinese_reuqirement)
            item['require_chinese_en'] = chinese_reuqirement

            modules = response.xpath('//h2[contains(text(),"About this")]/following-sibling::div')
            modules=self.takeTag(modules)
            modules = remove_class(modules)
            item['modules_en'] = modules

            career = response.xpath('//h2[contains(text(),"Career")]/following-sibling::div')
            career = self.takeTag(career)
            career = remove_class(career)
            item['career_en'] = career
            yield item
    def takeTag(self,text):
        var=''
        for i in text:
            var+=etree.tostring(i,method='html',encoding='unicode')
        return var


