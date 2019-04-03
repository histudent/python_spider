# -*- coding: utf-8 -*-
import scrapy
import re, json, requests
from scrapySchool_England.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from w3lib.html import remove_tags
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts
from lxml import etree
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.getDuration import getIntDuration


class TheUniversityOfSheffield_USpider(scrapy.Spider):
    name = "TheUniversityOfSheffield_P"
    start_urls = ["https://www.sheffield.ac.uk/postgraduate/taught/courses/all"]
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    def parse(self, response):
        links = ["https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/material/polymers-composite-science-engineering-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/chemistry/polymers-advanced-technologies-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/chempro/process-safety-loss-prevention-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/psychology/psychological",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/psychology/psychological-research-methods-advanced-statistics-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/education/psychology-education-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/education/psychology-education-conversion-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/music/psychology-music-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/physastron/quantum-photonics-nanomaterials-mres",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/architecture/real-estate-planning-development-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/human-metabolism/reproductive-developmental-medicine-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/autosys/robotics-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/science-communication-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/somlal/screen-translation-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/electronic/semiconductor",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/sociology/social-research-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/sociology/social-work-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/compscience/software-systems-internet-technology-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/music/sonic-arts-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/communication/speech-language-therapy-mmedsci",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/civstruc/steel-construction-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/biomedical/stem-cell-regenerative-medicine-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/civstruc/structural-concrete-engineering-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/civstruc/structural-engineering-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/architecture/sustainable-architecture-studies-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/english/theatre-performance-studies-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/architecture/town-regional-planning-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/somlal/translation-studies-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/translational-neuropathology-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/translational-neuroscience-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/oncology/translational-oncology-msc-res",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/architecture/urban-design-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/architecture/urban-design-planning-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/civstruc/water-engineering-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/electronic/wireless-communication-systems-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/management/work-psychology-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/aps/sustainable-agricultural-technologies-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/physastron/biological-imaging-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/autosys/advanced-control-systems-engineering-mres",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/dentistry/international-dental-public-health",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/physastron/particle-physics-mres",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/scharr/master-public-health-mph",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/advanced-aerospace-technologies-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/mathstats/statistics-financial-mathematics-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/law/legal-practice-course-diploma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/mathstats/statistics-medical-applications-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/aps/practical-entomology-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/education/language-and-education-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/law/llm",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/architecture/march-collaborative-practice",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/english/literature-culture-society-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/autosys/autonomous-intelligent-systems-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/biomedical/molecular-medicine-clinical-applications-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/aerospace-engineering-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/mathstats/statistics-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/management/accounting-governance-financial-management-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/communication/acquired-communication-disorders",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/mechanical/additive-manufacturing-advanced-manufacturing-technologies-msc-res",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/compscience/advanced-computer-science-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/autosys/advanced-control-systems-engineering-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/autosys/advanced-control-systems-industrial-management-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/autosys/advanced-control-systems-engineering-with-industry-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/electronic/advanced-electrical-machines-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/mechanical/advanced-manufacturing-technologies-amrc-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/mechanical/mechanical-engineering-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/material/advanced-metallurgy-mmet",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/compscience/advanced-software-engineering-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/archaeology/aegean-archaeology-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/mechanical/aerodynamics-aerostructures-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/material/aerospace-materials-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/history/american-history-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/architecture/applied-gis",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/english/applied-linguistics-tesol",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/archaeology/archaeology-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/archaeology/classical-mediterranean",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/architecture/architectural-design-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/civstruc/architectural-engineering-design-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/architecture/architecture-march",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/architecture/architecture-landscape-march",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/chempro/biochemical-engineering-industrial-management-msc-eng",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/electronic/bioengineering-msceng",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/chempro/biological-bioprocess-engineering-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/material/biomaterials-regenerative-medicine-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/biomedical/biomedical-science-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/journalism/broadcast-journalism-ma-diploma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/economics/business-finance-economics-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/iicd/cardiovascular-medicine",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/somlal/catalan-studies-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/chemistry/chemistry-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/chemistry/msc-res",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/architecture/cities-global-development-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/civstruc/civil-engineering-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/clinical-neurology-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/scharr/clinical-research-msc-diploma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/psychology/cognitive-computational-neuroscience-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/psychology/mres-cognitive-neuroscience-human-neuroimaging",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/philosophy/cognitive-studies-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/architecture/commercial-real-estate-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/music/composition-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/computational-medicine-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/compscience/computer-science-speech-language-processing-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/management/management-creative-cultural-industries-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/english/english-literature-creative-writing-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/somlal/crossways-cultural-narratives-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/archaeology/cultural-heritage-management-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/archaeology/cultural-materials-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/compscience/cybersecurity-artificial-intelligence-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/compscience/data-analytics-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/electronic/data-communications-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/is/data-science",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/nurse/dementia-studies-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/dentistry/dental-materials-science-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/dentistry/dental-public-health",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/dentistry/dental-technology",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/dentistry/diagnostic-oral-pathology-mmedsci",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/architecture/digital-design-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/is/electronic-digital-library-management-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/sociology/digital-media-society-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/education/ma-early-childhood-education-full-time",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/history/early-modern-history-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/civstruc/earthquake-civil-engineering-dynamics-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/eastasian/east-asian-business-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/aps/ecology-environment-mres",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/economics/economics-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/economics/economics-health-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/economics/public-policy-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/education/education-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/electronic/electronic-electrical-engineering-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/chempro/energy-engineering-industrial-management-msc-eng",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/english/english-language-studies-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/english/english-literature-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/chempro/environmental-energy-engineering-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/archaeology/environmental-archaeology-palaeoeconomy-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/geography/environmental-change-international-development-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/music/ethnomusicology-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/politics/european-and-global-affairs-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/aps/evolution-behaviour-mres",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/economics/finance-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/management/finance-accounting-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/economics/financial-economics-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/somlal/french-studies-research-track-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/biomedical/genomic-approaches-drug-discovery-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/genomic-medicine-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/somlal/germanic-studies-ma-programme",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/somlal/germanic-studies-ma-research",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/history/global-history-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/journalism/global-journalism-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/management/global-marketing-management-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/politics/global-political-economy-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/education/globalising-education-policy-practice-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/scharr/health-economics-decision-modelling-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/somlal/hispanic-studies-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/history/historical-research-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/biomedical/human-anatomy-education-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/biology/human-molecular-genetics-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/biomedical/human-nutrition-mmedsci-diploma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/archaeology/human-osteology-funerary-archaeology-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/management/human-resource-management-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/is/information-management-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/is/information-systems-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/management/information-systems-management-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/somlal/intercultural-communication-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/somlal/intercultural-communication-international-development",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/biblical/interdisciplinary-biblical-studies-mres",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/law/international-criminology-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/geography/international-development-mph",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/geography/international-development-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/economics/international-finance-economics-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/management/international-management-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/management/international-management-marketing-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/journalism/international-political-communication-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/politics/international-relations-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/sociology/international-social-change-policy-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/journalism/journalism-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/archaeology/landscape-archaeology-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/architecture/landscape-architecture-ma-diploma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/architecture/landscape-management-ma-diploma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/architecture/landscape-studies-ma-diploma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/somlal/latin-american-studies-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/law/law-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/is/librarianship-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/management/logistics-supply-chain-management-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/journalism/magazine-journalism-ma-diploma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/management/management-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/management/management-international-business-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/management/marketing-management-practice-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/management/business-administration-mba",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/scharr/master-public-health-services-research",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/scharr/master-public-health-management-leadership",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/material/materials-science-engineering-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/mathstats/mathematics-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/mechanical/mechanical-engineering-industrial-management-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/iicd/medicine-society-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/archaeology/medieval-archaeology-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/history/medieval-history-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/material/nuclear-science-technology-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/history/modern-history-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/biomedical/molecular-cellular-basis-human-disease-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/biology/molecular-biology-biotechnology-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/biomedical/molecular-medicine-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/economics/money-banking-finance-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/somlal/multilingual-information-management-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/human-metabolism/musculoskeletal-ageing-mres",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/music/music-management-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/music/music-performance-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/music/musicology-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/engineering/material/materials-science-nanomaterials-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/biomedical/neuroscience-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/management/occupational-psychology-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/dentistry/orthodontics-mclindent",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/archaeology/osteoarchaeology-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/medicine/dentistry/paediatric-dentistry-mclindent",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/archaeology/palaeoanthropology-msc",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/philosophy/philosophy-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/purescience/aps/plant-microbial-biology-mres",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/geography/polar-alpine-change-msc-res",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/arts/philosophy/political-theory-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/politics/politics-governance-public-policy-ma",
"https://www.sheffield.ac.uk/postgraduate/taught/courses/sscience/eastasian/politics-media-east-asia-ma", ]
        print(len(links))
        links = list(set(links))
        print(len(links))

        for link in links:
            url = link
            yield scrapy.Request(url, callback=self.parse_data, meta={'url': url})

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "The University of Sheffield"
        item['url'] = response.meta['url']
        print("===========================")
        print(response.url)
        print(response.meta['url'])
        try:

            tuition_fee_str = re.findall(r'course=.+"', response.text)
            tuition_fee_str = ''.join(tuition_fee_str).replace("course=", '').replace('"', '')
            # print("tuition_fee_str: ", tuition_fee_str)
            tuition_fee_url = "https://ssd.dept.shef.ac.uk/fees/pgt/api/lookup.php?year=2019&status=Overseas&course=" + tuition_fee_str
            # print("tuition_fee_url: ", tuition_fee_url)
            r = requests.get(tuition_fee_url, headers=self.headers)
            # print(r.text)
            tuition_fee = re.findall(r"&pound;\d+", r.text)
            # print(tuition_fee, "*******")
            if len(tuition_fee) != 0:
                item['tuition_fee'] = int(''.join(tuition_fee).replace('&pound;', ''))
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee']: ", item['tuition_fee'])

            yield item
        except Exception as e:
            with open("scrapySchool_England/error/" + item['university'] + str(item['degree_type']) + ".txt", 'a',
                      encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

