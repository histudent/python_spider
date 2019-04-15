# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/26 15:21'
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
from scrapySchool_England.TranslateMonth import translate_month
class UniversityofNottinghamSpider(scrapy.Spider):
    name = 'UniversityofNottingham_u'
    allowed_domains = ['nottingham.ac.uk/']
    start_urls = []
    C= [
        'https://www.nottingham.ac.uk/ugstudy/courses/architectureandbuiltenvironment/architecture-and-environmental-design-meng.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mathematicalsciences/mmath-mathematics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mechanicalmaterialsandmanufacturingengineering/beng-mechanical-engineering-including-an-industrial-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mechanicalmaterialsandmanufacturingengineering/meng-mechanical-engineering-including-an-industrial-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physicsandastronomy/bsc-physics-european-language.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mechanicalmaterialsandmanufacturingengineering/meng-mechanical-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mechanicalmaterialsandmanufacturingengineering/beng-mechanical-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/medicalphysiologyandtherapeutics/medical-physiology-and-therapeutics-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemistry/bsc-medicinal-biological-chemistry.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mechanicalmaterialsandmanufacturingengineering/meng-mechanical-engineering-with-study-abroad.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mechanicalmaterialsandmanufacturingengineering/beng-mechanical-engineering-with-study-abroad.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemistry/medicinal-biological-chemistry-year-industry.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mechanicalmaterialsandmanufacturingengineering/meng-mechanical-engineering-with-study-abroad-year-3.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/medicine/bmbs-medicine-lincoln.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemistry/msci-medicinal-biological-chemistry.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/medicine/bmbs-medicine-nott-derby.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/medicine/medicine-with-a-foundation-year-bmbs-lincoln.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/medicine/medicine-with-a-foundation-year-bmbs-nott-derby.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/microbiology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/midwifery/bsc-midwifery.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/modernlanguages/modern-languages-business.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/modernlanguages/modern-language.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemistry/msci-chemistry-molecular-physics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/modernlanguages/modern-languages-with-translation.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/music/music-and-music-technology-ba.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/music/music-philosophy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemistry/bsc-chemistry-molecular-physics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/agricultural-and-livestock-science-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/aerospace/meng-aerospace-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/music/ba-music.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/aerospace/beng-aerospace-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/modernlanguages/modern-european.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/aerospace/meng-aerospace-engineering-including-an-industrial-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/naturalsciences/natural-sciences-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/aerospace/aerospace-engineering-including-an-industrial-year-beng.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/naturalsciences/natural-sciences-msci.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/politicsandinternationalrelations/politics-economics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/agricultural-and-crop-science-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/cancersciences/cancer-sciences-msci.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/nursing/nursing-child.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/politicsandinternationalrelations/politics-american.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/business/accountancy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/cancersciences/cancer-sciences-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/integrated-agricultural-business-management-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/frenchandfrancophonestudies/french-politics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/neuroscience/bsc-neuroscience.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemicalandenvironmentalengineering/beng-chemical-engineering-including-industrial-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/integrated-agricultural-business-management-industrial-placement-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/politicsandinternationalrelations/ba-politics-international-relations.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/neuroscience/msci-neuroscience.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemicalandenvironmentalengineering/beng-chemical-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/americanandcanadianstudies/american-canadian-literature-history-culture.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biologyandzoology/msci-biology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/americanandcanadianstudies/american-canadian-literature-history-culture-international.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/modernlanguages/modernlanguagesba.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/food-science-and-nutrition-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemicalandenvironmentalengineering/beng-chemical-engineering-environmental.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/agriculture.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/culturefilmandmedia/portuguese-international-media-communications.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/food-science-nutrition-msci.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemicalandenvironmentalengineering/meng-chemical-engineering-including-industrial-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/americanandcanadianstudies/american-history.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/international-agricultural-science-bsc-.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemicalandenvironmentalengineering/meng-chemical-engineering-environmental.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/nutrition.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/culturefilmandmedia/film-television-american.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/nutrition-dietetics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/history/ancient-history-history.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemistry/bsc-chemistry.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/pharmacy/msci-pharmaceutical-sciences-year-in-industry.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/classics-and-archaeology/ancient-history-archaeology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemistry/msci-chemistry.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/pharmacy/mpharm-pharmacy-with-integrated-pre-registration-scheme.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/modernlanguages/modernlanguagesba.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/animal-science.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemistry/bsc-chemistry-molecular-physics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/nursing/nursing-mental-health.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/psychology/psychology-cognitive-neuroscience-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/americanandcanadianstudies/american-latin-american.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemicalandenvironmentalengineering/meng-chemical-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/classics-and-archaeology/archaeology-geography.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemicalandenvironmentalengineering/beng-chemical-engineering-with-environmental-engineering-including-industrial-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/pharmacy/mpharm-pharmacy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/psychology/msci-psychology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/classics-and-archaeology/ba-archaeology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemicalandenvironmentalengineering/meng-chemical-engineering-with-environmental-engineering-including-industrial-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/philosophy/philosophy-theology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/theologyandreligiousstudies/religion-culture-and-ethics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/classics-and-archaeology/bsc-archaeology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemistry/chemistry-year-industry.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/philosophy/english-philosophy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/classics-and-archaeology/ancient-history.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemistry/chemistry-international-study.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/frenchandfrancophonestudies/french-philosophy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/philosophy/psychology-philosophy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/history/archaeology-history.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/civilengineering/beng-civil-engineering-industrial-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/philosophy/ba-philosophy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/psychology/psychology-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/civilengineering/beng-civil-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/theologyandreligiousstudies/religion-philosophy-and-ethics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/russianandslavonicstudies/ba-russian.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/civilengineering/meng-civil-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/russianandslavonicstudies/history-russian.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/philosophy/classical-civilisation-philosophy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/faculty-of-science/science-with-foundation-year-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/psychology/psychology-cognitive-neuroscience-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/sociologyandsocialpolicy/sociology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/english/classics-and-english-ba.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/sociologyandsocialpolicy/social-work.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/civilengineering/meng-civil-engineering-industrial-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/computerscience/bsc-computer-science.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/computerscience/bsc-computer-science-and-artificial-intelligence-with-year-in-industry.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/computerscience/msci-computer-science-including-international-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/sociologyandsocialpolicy/sociology-social-policy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/computerscience/msci-computer-science.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/faculty-of-science/science-with-foundation-year-msci.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/computerscience/bsc-computer-science-artificial-intelligence.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/spanishportugueseandlatinamericanstudies/spanish-contemporary-chinese.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/computerscience/msci-computer-science-artificial-intelligence-including-international-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/culturefilmandmedia/spanish-international-media-communications.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/computerscience/msci-computer-science-artificial-intelligence.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/computerscience/bsc-computer-science-with-year-in-industry.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/americanandcanadianstudies/american-latin-american.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/consumer-behaviour-food-and-nutrition-msci.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mathematicalsciences/statistics-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/germanstudies/german-contemporary-chinese.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/veterinarymedicineandscience/veterinary-medicine-surgery-preliminary-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/consumer-behaviour-food-and-nutrition-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/sportandexercisescience/sport-and-exercise-science-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/russianandslavonicstudies/russian-contemporary-chinese.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physiotherapyandrehabilitationsciences/bsc-sport-rehabilitation.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/spanishportugueseandlatinamericanstudies/spanish-contemporary-chinese.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/veterinarymedicineandscience/veterinary-medicine-surgery-gateway-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/sociologyandsocialpolicy/criminology-and-social-policy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biologyandzoology/bsc-tropical-biology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/frenchandfrancophonestudies/french-contemporary-chinese.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/theologyandreligiousstudies/theology-and-religious-studies.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/sociologyandsocialpolicy/criminology-and-sociology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/veterinarymedicineandscience/veterinary-medicine-surgery.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/nutrition-dietetics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biologyandzoology/msci-zoology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/sociologyandsocialpolicy/criminology-ba.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biologyandzoology/bsc-zoology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/computerscience/bsc-data-science.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/philosophy/philosophy-theology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/russianandslavonicstudies/history-russian-east-european-civilisations.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/economics/economics-econometrics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/economics/economics-hispanic.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mathematicalsciences/bsc-mathematics-economics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/economics/economics-philosophy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/economics/economics-russian.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/economics/bsc-economics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/economics/economics-german.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/education/education-ba.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/economics/economics-french.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/electricalandelectronicengineering/beng-electrical-electronic-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/politicsandinternationalrelations/politics-economics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/electricalandelectronicengineering/beng-electrical-and-electronic-engineering-including-an-industrial-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/education/education-marts.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/electricalandelectronicengineering/meng-electrical-and-electronic-engineering-including-an-industrial-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/electricalandelectronicengineering/meng-electrical-electronic-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/electricalandelectronicengineering/beng-electrical-electronic-engineering-year-abroad.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/electricalandelectronicengineering/meng-electrical-electronic-engineering-year-abroad.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/electricalandelectronicengineering/beng-electrical-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/electricalandelectronicengineering/meng-electronic-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/faculty-of-engineering/engineering-and-physical-sciences-foundation-programme.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/electricalandelectronicengineering/beng-electronic-computer-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/electricalandelectronicengineering/meng-electronic-computer-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/electricalandelectronicengineering/beng-electronic-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/electricalandelectronicengineering/meng-electrical-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/americanandcanadianstudies/american-english.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/english/classics-and-english-ba.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/historyofart/history-of-art-english.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/english/english-ba.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/english/english-history.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/spanishportugueseandlatinamericanstudies/english-hispanic.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/english/english-language-literature.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/english/english-creative-writing.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemicalandenvironmentalengineering/beng-environmental-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/architectureandbuiltenvironment/architecture-and-environmental-design-meng.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemicalandenvironmentalengineering/beng-environmental-engineering-including-industrial-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemicalandenvironmentalengineering/meng-environmental-engineering.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemicalandenvironmentalengineering/meng-environmental-engineering-including-industrial-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/geography/environmental-geoscience-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/environmental-biology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/environmental-science-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/culturefilmandmedia/film-television-american.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/environmental-science-msci.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/business/finance-accounting-management.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/culturefilmandmedia/film-television.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mathematicalsciences/financial-mathematics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/food-science-and-nutrition-bsc.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/food-science-nutrition-msci.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/food-science.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/frenchandfrancophonestudies/french-contemporary-chinese.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/food-science-msci.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/germanstudies/english-german.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/frenchandfrancophonestudies/english-french.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/frenchandfrancophonestudies/english-french.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/frenchandfrancophonestudies/french-history.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/philosophy/english-philosophy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/frenchandfrancophonestudies/french-philosophy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/frenchandfrancophonestudies/french.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/frenchandfrancophonestudies/french-politics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biochemistry/bsc-biochemistry-genetics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biologyandzoology/msci-genetics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biochemistry/msci-biochemistry-genetics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biologyandzoology/bsc-genetics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/classics-and-archaeology/archaeology-geography.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/geography/geography-business.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/geography/ba-geography.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/geography/bsc-geography.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/germanstudies/english-german.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/germanstudies/german-history.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/germanstudies/german-contemporary-chinese.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/germanstudies/german.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/germanstudies/german-politics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/spanishportugueseandlatinamericanstudies/hispanic-history.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/politicsandinternationalrelations/international-relations-global-issues.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/spanishportugueseandlatinamericanstudies/hispanic.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/spanishportugueseandlatinamericanstudies/english-hispanic.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/classics-and-archaeology/historical-archaeology-ba.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/americanandcanadianstudies/american-history.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/history/ancient-history-history.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/classics-and-archaeology/archaeology-classical-civilisation.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physicsandastronomy/bsc-physics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/classics-and-archaeology/archaeology-history-of-art.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/economics/philosophy-politics-and-economics-ba.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/architectureandbuiltenvironment/architectural-environment-engineering-beng.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/economics/economics-philosophy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physicsandastronomy/msci-physics-astronomy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physicsandastronomy/msci-physics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/history/history-history-of-art.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physicsandastronomy/physics-philosophy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physicsandastronomy/msci-physics-european-language.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/architectureandbuiltenvironment/barch-architecture.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physicsandastronomy/bsc-physics-medical-physics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/theologyandreligiousstudies/biblical-studies-and-theology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physicsandastronomy/bsc-physics-astronomy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physicsandastronomy/bsc-physics-nanoscience.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/historyofart/history-of-art.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/plant-science.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biochemistry/msci-biochemistry-genetics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physicsandastronomy/msci-physics-nanoscience.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biochemistry/bsc-biochemistry-genetics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physicsandastronomy/msci-physics-medical-physics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biochemistry/msci-biochemistry-biological-chemistry.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physicsandastronomy/bsc-physics-theoretical-astrophysics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biochemistry/msci-biochemistry-molecular-medicine.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physicsandastronomy/msci-physics-theoretical-astrophysics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biochemistry/msci-biochemistry.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physicsandastronomy/bsc-physics-theoretical-physics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biochemistry/bsc-biochemistry-biological-chemistry.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physicsandastronomy/msci-physics-theoretical-physics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biochemistry/bsc-biochemistry.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/physiotherapyandrehabilitationsciences/bsc-physiotherapy.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biologyandzoology/bsc-biology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/germanstudies/german-politics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/americanandcanadianstudies/american-english.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/history/history-politics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biochemistry/bsc-biochemistry-molecular-medicine.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/nursing/nursing-adult.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/biosciences/biotechnology.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mechanicalmaterialsandmanufacturingengineering/beng-product-design-manufacture.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mechanicalmaterialsandmanufacturingengineering/beng-product-design-manufacture-including-industrial-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/chemistry/msci-chemistry-molecular-physics.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mechanicalmaterialsandmanufacturingengineering/meng-product-design-manufacture-including-industrial-year.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mechanicalmaterialsandmanufacturingengineering/beng-product-design-manufacture-with-study-abroad.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mechanicalmaterialsandmanufacturingengineering/meng-product-design-manufacture.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/mechanicalmaterialsandmanufacturingengineering/meng-product-design-manufacture-with-study-abroad.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/classics-and-archaeology/classics-ba.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/russianandslavonicstudies/russian-contemporary-chinese.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/classics-and-archaeology/classical-civilisation.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/classics-and-archaeology/archaeology-classical-civilisation.aspx',
        'https://www.nottingham.ac.uk/ugstudy/courses/liberal-arts/liberal-arts-ba.aspx'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Nottingham'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en_a = response.xpath('//*[@id="pageTitle"]/h1').extract()
        # print(programme_en)
        programme_en_a = ''.join(programme_en_a)
        programme_en_a = remove_tags(programme_en_a)
        programme_en = programme_en_a.split()[:-1]
        programme_en = ' '.join(programme_en)
        # print(programme_en)

        #4.degree_type
        degree_type = 1

        #5.degree_name
        try:
            degree_name = programme_en_a.split()[-1]
        except:
            degree_name = ''
        # print(degree_name)

        #6.duration #7.duration_per #8.ucascode
        duration_list = response.xpath("//*[contains(text(),'Duration')]//following-sibling::*").extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        # print(duration)
        try:
            duration = re.findall('\d+',duration_list)[0]
        except:
            duration = None
        # print(duration)
        duration_per = 1
        ucascode = response.xpath('//*[@id="ugStudyFactfile"]/div[2]/div[2]').extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode).strip()
        if len(ucascode)>35:
            ucascode = 'N/A'
        # print(ucascode)

        #9.alevel
        alevel = response.xpath('//*[@id="ugStudyFactfile"]/div[4]/div[2]').extract()
        alevel = ''.join(alevel)
        alevel = remove_tags(alevel).strip()
        # print(alevel)

        #10.ielts 11121314
        ielts_list = response.xpath("//*[contains(text(),'language requirements')]//following-sibling::*[1]").extract()
        ielts_list = ''.join(ielts_list)
        ielts_list = remove_tags(ielts_list)
        try:
            ielts= re.findall('[567]\.\d',ielts_list)
        except:
            ielts = None
        # print(ielts)
        if len(ielts)==0:
            ielts_list = response.xpath('//*[@id="EntryRequirements"]/div[2]').extract()
            ielts_list = ''.join(ielts_list)
            ielts_list = remove_tags(ielts_list)
            try:
                ielts = re.findall('[567]\.\d', ielts_list)
            except:
                ielts = None
        # print(ielts)
        if len(ielts) >1:
            a = ielts[0]
            b = ielts[1]
            ielts = a
            ielts_r = b
            ielts_w = b
            ielts_s = b
            ielts_l = b
        elif len(ielts)==1:
            a = ielts[0]
            ielts = a
            ielts_r = float(a)-0.5
            ielts_w = float(a)-0.5
            ielts_s = float(a)-0.5
            ielts_l = float(a)-0.5
        else:
            ielts = 6.5
            ielts_r =  6.0
            ielts_w =  6.0
            ielts_s =  6.0
            ielts_l =  6.0
        # print(ielts,ielts_r,ielts_w,ielts_s,ielts_l)

        #15.ib
        ib = response.xpath("//*[contains(text(),'IB score')]//following-sibling::*").extract()
        ib = ''.join(ib)
        ib = remove_tags(ib).strip()
        # print(ib)

        #16.department
        department = response.xpath("//*[contains(text(),'School/department')]//following-sibling::*").extract()
        department = ''.join(department)
        department = remove_tags(department)
        department = clear_space_str(department)
        # print(department)

        #17.location
        location = response.xpath("//div[contains(text(),'location')]//following-sibling::*").extract()
        location = ''.join(location)
        location = remove_tags(location)
        location = clear_space_str(location)
        # print(location)

        #18.overview_en
        overview_en = response.xpath('//*[@id="CourseOverview"]').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #19.modules_en
        modules_en = response.xpath('//*[@id="Modules"]/div').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)

        # print(modules_en)

        #20.career_en
        career_en = response.xpath('//*[@id="Skills"]/div/p[1]/text()').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        career_en = '<p>'+career_en+'</p>'
        # print(career_en)

        #21.tuition_fee
        tuition_fee = 9250

        #22.tuition_fee_pre
        tuition_fee_pre = '£'


        #24.apply_proces_en
        apply_proces_en = 'https://www.nottingham.ac.uk/ugstudy/applying/applicationprocess.aspx'

        #25.deadline
        deadline = '2019-6-30'

        #26.require_chinese_en
        require_chinese_en = '<p>Applicants who have taken foundation courses are normally considered on a case by case basis.Students who have completed one or two years of university study may be eligible for bachelors admission, if relevant subjects have been studied and strong grades achieved. Again,applications are considered on a case by case basis. Students taking A levels or the IB should refer to the online undergraduate prospectus for entry requirements.Students taking APs or SATIIs should refer to entry requirements for the USA.</p>'

        #27.apply_fee
        apply_fee = 40

        item['ib'] = ib
        item['alevel'] = alevel
        item['ucascode'] = ucascode
        item['apply_proces_en'] =apply_proces_en
        item['deadline'] = deadline
        item['require_chinese_en'] = require_chinese_en
        item['apply_fee'] = apply_fee
        item['tuition_fee'] = tuition_fee
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['ielts_w'] = ielts_w
        item['department'] = department
        item['location'] = location
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['career_en'] = career_en
        item['tuition_fee_pre'] = tuition_fee_pre
        yield item