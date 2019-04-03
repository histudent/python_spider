# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.clearSpace import clear_same_s
from scrapySchool_England.middlewares import clear_duration

class UniversityofglasgowSpider(scrapy.Spider):
    name = 'UniversityOfGlasgow_P'
    allowed_domains = ['gla.ac.uk']
    start_urls = ['https://www.gla.ac.uk/postgraduate/taught/']
    pro_lis = []
    start_urlss=['https://www.gla.ac.uk/postgraduate/taught/adulteducationcommunitydevelopmentyouthstudies/',
'https://www.gla.ac.uk/postgraduate/taught/adulteducationcommunitydevelopmentyouthwork/',
'https://www.gla.ac.uk/postgraduate/taught/adulteducationforsocialchangeinternationalmaster/',
'https://www.gla.ac.uk/postgraduate/taught/advancednursingsciences/',
'https://www.gla.ac.uk/postgraduate/taught/advancedstatistics/',
'https://www.gla.ac.uk/postgraduate/taught/aerospaceengineering/',
'https://www.gla.ac.uk/postgraduate/taught/aerospaceengineeringmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/ancientcultures/',
'https://www.gla.ac.uk/postgraduate/taught/animalwelfarescience/',
'https://www.gla.ac.uk/postgraduate/taught/appliedneuropsychology/',
'https://www.gla.ac.uk/postgraduate/taught/artcollectingprovenance/',
'https://www.gla.ac.uk/postgraduate/taught/arthistory/',
'https://www.gla.ac.uk/postgraduate/taught/arthistoryrenaissance/',
'https://www.gla.ac.uk/postgraduate/taught/assetpricinginvestment/',
'https://www.gla.ac.uk/postgraduate/taught/astrophysics/',
'https://www.gla.ac.uk/postgraduate/taught/bankingfinancialservices/',
'https://www.gla.ac.uk/postgraduate/taught/bioinformatics/',
'https://www.gla.ac.uk/postgraduate/taught/biomedicalengineering/',
'https://www.gla.ac.uk/postgraduate/taught/biomedicalsciencemsc/',
'https://www.gla.ac.uk/postgraduate/taught/biomedicalsciencesmres/',
'https://www.gla.ac.uk/postgraduate/taught/biostatistics/',
'https://www.gla.ac.uk/postgraduate/taught/biotechnology/',
'https://www.gla.ac.uk/postgraduate/taught/biotechnologyandmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/businessadministration/',
'https://www.gla.ac.uk/postgraduate/taught/cancersciences/',
'https://www.gla.ac.uk/postgraduate/taught/cardiovascularsciences/',
'https://www.gla.ac.uk/postgraduate/taught/celticstudies/',
'https://www.gla.ac.uk/postgraduate/taught/celticvikingarchaeology/',
'https://www.gla.ac.uk/postgraduate/taught/centraleasteuropeanrussianeurasianstudies/',
'https://www.gla.ac.uk/postgraduate/taught/chemistry/',
'https://www.gla.ac.uk/postgraduate/taught/chemistrywithmedicinalchemistry/',
'https://www.gla.ac.uk/postgraduate/taught/childrensliteratureandliteracies/',
'https://www.gla.ac.uk/postgraduate/taught/childrensliteraturemediaculture/',
'https://www.gla.ac.uk/postgraduate/taught/chinesestudies/',
'https://www.gla.ac.uk/postgraduate/taught/cityplanning/',
'https://www.gla.ac.uk/postgraduate/taught/cityplanningrealestatedevelopment/',
'https://www.gla.ac.uk/postgraduate/taught/civilengineering/',
'https://www.gla.ac.uk/postgraduate/taught/civilengineeringmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/classics/',
'https://www.gla.ac.uk/postgraduate/taught/clinicalgenetics/',
'https://www.gla.ac.uk/postgraduate/taught/clinicalneuropsychology/',
'https://www.gla.ac.uk/postgraduate/taught/clinicalnutrition/',
'https://www.gla.ac.uk/postgraduate/taught/clinicalpharmacology/',
'https://www.gla.ac.uk/postgraduate/taught/clinicaltrialsstratifiedmedicine/',
'https://www.gla.ac.uk/postgraduate/taught/comparativeliterature/',
'https://www.gla.ac.uk/postgraduate/taught/compositioncreativepractice/',
'https://www.gla.ac.uk/postgraduate/taught/computersystemsengineering/',
'https://www.gla.ac.uk/postgraduate/taught/computingsciencemsc/',
'https://www.gla.ac.uk/postgraduate/taught/conflictarchaeology/',
'https://www.gla.ac.uk/postgraduate/taught/conservationmanagementafricanecosystems/',
'https://www.gla.ac.uk/postgraduate/taught/corporateandfinanciallaw/',
'https://www.gla.ac.uk/postgraduate/taught/creativeindustriesandculturalpolicy/',
'https://www.gla.ac.uk/postgraduate/taught/creativewritingmlitt/',
'https://www.gla.ac.uk/postgraduate/taught/criminology/',
'https://www.gla.ac.uk/postgraduate/taught/criminologycriminaljustice/',
'https://www.gla.ac.uk/postgraduate/taught/criticalcare/',
'https://www.gla.ac.uk/postgraduate/taught/curatorialpractice/',
'https://www.gla.ac.uk/postgraduate/taught/dataanalytics/',
'https://www.gla.ac.uk/postgraduate/taught/datascience/',
'https://www.gla.ac.uk/postgraduate/taught/developmentstudies/',
'https://www.gla.ac.uk/postgraduate/taught/dresstextilehistories/',
'https://www.gla.ac.uk/postgraduate/taught/earlymodernhistory/',
'https://www.gla.ac.uk/postgraduate/taught/earlymodernliteratureculture/',
'https://www.gla.ac.uk/postgraduate/taught/ecologyenvironmentalbiology/',
'https://www.gla.ac.uk/postgraduate/taught/ecologyepidemiologyconservationbiology/',
'https://www.gla.ac.uk/postgraduate/taught/economicdevelopment/',
'https://www.gla.ac.uk/postgraduate/taught/economics/',
'https://www.gla.ac.uk/postgraduate/taught/economicsbankingfinance/',
'https://www.gla.ac.uk/postgraduate/taught/educationalstudiesmed/',
'https://www.gla.ac.uk/postgraduate/taught/educationalstudiesmsc/',
'https://www.gla.ac.uk/postgraduate/taught/educationpublicpolicyequity/',
'https://www.gla.ac.uk/postgraduate/taught/electronicselectricalengineering/',
'https://www.gla.ac.uk/postgraduate/taught/electronicselectricalengineeringmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/electronicsmanufacturing/',
'https://www.gla.ac.uk/postgraduate/taught/endodontics/',
'https://www.gla.ac.uk/postgraduate/taught/englishlanguagelinguistics/',
'https://www.gla.ac.uk/postgraduate/taught/englishliterature/',
'https://www.gla.ac.uk/postgraduate/taught/enhancedpracticeineducation/',
'https://www.gla.ac.uk/postgraduate/taught/environmentalchangesociety/',
'https://www.gla.ac.uk/postgraduate/taught/environmentalstatistics/',
'https://www.gla.ac.uk/postgraduate/taught/environmentculturecommunication/',
'https://www.gla.ac.uk/postgraduate/taught/environmentsociety/',
'https://www.gla.ac.uk/postgraduate/taught/environmentsustainabledevelopment/',
'https://www.gla.ac.uk/postgraduate/taught/equalityhumanrightsmres/',
'https://www.gla.ac.uk/postgraduate/taught/equalityhumanrightsmsc/',
'https://www.gla.ac.uk/postgraduate/taught/fantasy/',
'https://www.gla.ac.uk/postgraduate/taught/filmcuration/',
'https://www.gla.ac.uk/postgraduate/taught/filmmaking/',
'https://www.gla.ac.uk/postgraduate/taught/filmtelevisionstudies/',
'https://www.gla.ac.uk/postgraduate/taught/financeeconomicdevelopment/',
'https://www.gla.ac.uk/postgraduate/taught/financemanagement/',
'https://www.gla.ac.uk/postgraduate/taught/financialeconomics/',
'https://www.gla.ac.uk/postgraduate/taught/financialforecastinginvestment/',
'https://www.gla.ac.uk/postgraduate/taught/financialmodelling/',
'https://www.gla.ac.uk/postgraduate/taught/financialriskmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/foodsecurity/',
'https://www.gla.ac.uk/postgraduate/taught/forensictoxicology/',
'https://www.gla.ac.uk/postgraduate/taught/genderhistory/',
'https://www.gla.ac.uk/postgraduate/taught/geneticandgenomiccounsellingwithworkplacement/',
'https://www.gla.ac.uk/postgraduate/taught/geoinformationtechnologyandcartography/',
'https://www.gla.ac.uk/postgraduate/taught/geomaticsmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/geospatialandmappingsciences/',
'https://www.gla.ac.uk/postgraduate/taught/globaleconomy/',
'https://www.gla.ac.uk/postgraduate/taught/globalhealth/',
'https://www.gla.ac.uk/postgraduate/taught/globalmarketslocalcreativities/',
'https://www.gla.ac.uk/postgraduate/taught/globalmentalhealth/',
'https://www.gla.ac.uk/postgraduate/taught/globalmigrationssocialjusticemres/',
'https://www.gla.ac.uk/postgraduate/taught/globalmigrationssocialjusticemsc/',
'https://www.gla.ac.uk/postgraduate/taught/globalsecurity/',
'https://www.gla.ac.uk/postgraduate/taught/globalsecuritymres/',
'https://www.gla.ac.uk/postgraduate/taught/governanceaccountability/',
'https://www.gla.ac.uk/postgraduate/taught/healthcare/',
'https://www.gla.ac.uk/postgraduate/taught/historicallyinformedperformancepractice/',
'https://www.gla.ac.uk/postgraduate/taught/history/',
'https://www.gla.ac.uk/postgraduate/taught/historywithanemphasisonthehistoryofmedicine/',
'https://www.gla.ac.uk/postgraduate/taught/housingstudies/',
'https://www.gla.ac.uk/postgraduate/taught/humangeographyspacespoliticsecologies/',
'https://www.gla.ac.uk/postgraduate/taught/humannutrition/',
'https://www.gla.ac.uk/postgraduate/taught/humanrightsinternationalpolitics/',
'https://www.gla.ac.uk/postgraduate/taught/humanrightsinternationalpoliticsmres/',
'https://www.gla.ac.uk/postgraduate/taught/immunologyinflammatorydisease/',
'https://www.gla.ac.uk/postgraduate/taught/inclusiveeducationresearchpolicypracticemed/',
'https://www.gla.ac.uk/postgraduate/taught/infectionbiologywithspecialisms/',
'https://www.gla.ac.uk/postgraduate/taught/infectiousdiseasesantimicrobialresistance/',
'https://www.gla.ac.uk/postgraduate/taught/informationmanagementpreservation/',
'https://www.gla.ac.uk/postgraduate/taught/informationsecuritymsc/',
'https://www.gla.ac.uk/postgraduate/taught/informationtechnology/',
'https://www.gla.ac.uk/postgraduate/taught/intellectualproperty/',
'https://www.gla.ac.uk/postgraduate/taught/internationalaccountingfinancialmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/internationalbankingfinance/',
'https://www.gla.ac.uk/postgraduate/taught/internationalbusinessentrepreneurship/',
'https://www.gla.ac.uk/postgraduate/taught/internationalcommerciallaw/',
'https://www.gla.ac.uk/postgraduate/taught/internationalcompetitionlawpolicy/',
'https://www.gla.ac.uk/postgraduate/taught/internationalcorporatefinancebanking/',
'https://www.gla.ac.uk/postgraduate/taught/internationaleconomiclaw/',
'https://www.gla.ac.uk/postgraduate/taught/internationalfinance/',
'https://www.gla.ac.uk/postgraduate/taught/internationalfinancialanalysis/',
'https://www.gla.ac.uk/postgraduate/taught/internationalhumanresourcemanagementdevelopment/',
'https://www.gla.ac.uk/postgraduate/taught/internationallaw/',
'https://www.gla.ac.uk/postgraduate/taught/internationallawandsecurity/',
'https://www.gla.ac.uk/postgraduate/taught/internationalmanagementanddesigninnovation/',
'https://www.gla.ac.uk/postgraduate/taught/internationalrealestatemanagement/',
'https://www.gla.ac.uk/postgraduate/taught/internationalrelations/',
'https://www.gla.ac.uk/postgraduate/taught/internationalrelationsresearch/',
'https://www.gla.ac.uk/postgraduate/taught/internationalsecurity/',
'https://www.gla.ac.uk/postgraduate/taught/internationalstrategicmarketing/',
'https://www.gla.ac.uk/postgraduate/taught/inventingmodernart/',
'https://www.gla.ac.uk/postgraduate/taught/investmentbankingfinance/',
'https://www.gla.ac.uk/postgraduate/taught/investmentfundmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/itcybersecurity/',
'https://www.gla.ac.uk/postgraduate/taught/landhydrographicsurveying/',
'https://www.gla.ac.uk/postgraduate/taught/law/',
'https://www.gla.ac.uk/postgraduate/taught/lawmres/',
'https://www.gla.ac.uk/postgraduate/taught/management/',
'https://www.gla.ac.uk/postgraduate/taught/managementmres/',
'https://www.gla.ac.uk/postgraduate/taught/managementsustainabletourism/',
'https://www.gla.ac.uk/postgraduate/taught/managementwithenterprise/',
'https://www.gla.ac.uk/postgraduate/taught/managementwithhumanresources/',
'https://www.gla.ac.uk/postgraduate/taught/managementwithinternationalfinance/',
'https://www.gla.ac.uk/postgraduate/taught/materialcultureartefactstudies/',
'https://www.gla.ac.uk/postgraduate/taught/mathematicsappliedmathematics/',
'https://www.gla.ac.uk/postgraduate/taught/mechanicalengineering/',
'https://www.gla.ac.uk/postgraduate/taught/mechanicalengineeringmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/mechatronics/',
'https://www.gla.ac.uk/postgraduate/taught/mediacommunicationsinternationaljournalism/',
'https://www.gla.ac.uk/postgraduate/taught/mediamanagement/',
'https://www.gla.ac.uk/postgraduate/taught/medicalgeneticsandgenomics/',
'https://www.gla.ac.uk/postgraduate/taught/medicalphysics/',
'https://www.gla.ac.uk/postgraduate/taught/medicalvisualisation/',
'https://www.gla.ac.uk/postgraduate/taught/medievalhistory/',
'https://www.gla.ac.uk/postgraduate/taught/modernhistory/',
'https://www.gla.ac.uk/postgraduate/taught/modernities/',
'https://www.gla.ac.uk/postgraduate/taught/modernmaterialartefacts/',
'https://www.gla.ac.uk/postgraduate/taught/museumeducation/',
'https://www.gla.ac.uk/postgraduate/taught/museumstudiesartefactsmaterialculture/',
'https://www.gla.ac.uk/postgraduate/taught/museumstudiescollectingcollections/',
'https://www.gla.ac.uk/postgraduate/taught/museumstudiestheorypractice/',
'https://www.gla.ac.uk/postgraduate/taught/musicindustries/',
'https://www.gla.ac.uk/postgraduate/taught/musicology/',
'https://www.gla.ac.uk/postgraduate/taught/nanosciencenanotechnology/',
'https://www.gla.ac.uk/postgraduate/taught/oralmaxillofacialsurgery/',
'https://www.gla.ac.uk/postgraduate/taught/oralsciences/',
'https://www.gla.ac.uk/postgraduate/taught/philosophy/',
'https://www.gla.ac.uk/postgraduate/taught/philosophymlitt/',
'https://www.gla.ac.uk/postgraduate/taught/physicsadvancedmaterials/',
'https://www.gla.ac.uk/postgraduate/taught/physicsenergyandtheenvironment/',
'https://www.gla.ac.uk/postgraduate/taught/physicsnucleartechnology/',
'https://www.gla.ac.uk/postgraduate/taught/playwritingdramaturgy/',
'https://www.gla.ac.uk/postgraduate/taught/politicalcommunicationmres/',
'https://www.gla.ac.uk/postgraduate/taught/politicalcommunicationmscpgdip/',
'https://www.gla.ac.uk/postgraduate/taught/productdesignengineering/',
'https://www.gla.ac.uk/postgraduate/taught/psychologicalscienceconversion/',
'https://www.gla.ac.uk/postgraduate/taught/psychologicalscienceresearchmethodsof/',
'https://www.gla.ac.uk/postgraduate/taught/psychologicalstudiesconversion/',
'https://www.gla.ac.uk/postgraduate/taught/publicandurbanpolicy/',
'https://www.gla.ac.uk/postgraduate/taught/publichealth/',
'https://www.gla.ac.uk/postgraduate/taught/publicpolicymanagement/',
'https://www.gla.ac.uk/postgraduate/taught/publicpolicyresearch/',
'https://www.gla.ac.uk/postgraduate/taught/quantitativefinance/',
'https://www.gla.ac.uk/postgraduate/taught/quantumtechnology/',
'https://www.gla.ac.uk/postgraduate/taught/realestate/',
'https://www.gla.ac.uk/postgraduate/taught/religionliteratureculture/',
'https://www.gla.ac.uk/postgraduate/taught/romanticworlds/',
'https://www.gla.ac.uk/postgraduate/taught/russiancentraleasteuropeanstudiesmres/',
'https://www.gla.ac.uk/postgraduate/taught/russiancentraleasteuropeanstudiesmsc/',
'https://www.gla.ac.uk/postgraduate/taught/scottishhistory/',
'https://www.gla.ac.uk/postgraduate/taught/sensorandimagingsystems/',
'https://www.gla.ac.uk/postgraduate/taught/sociolegalstudies/',
'https://www.gla.ac.uk/postgraduate/taught/sociology/',
'https://www.gla.ac.uk/postgraduate/taught/sociologyresearchmethods/',
'https://www.gla.ac.uk/postgraduate/taught/softwaredevelopment/',
'https://www.gla.ac.uk/postgraduate/taught/sounddesignaudiovisualpractice/',
'https://www.gla.ac.uk/postgraduate/taught/southeuropeanstudies/',
'https://www.gla.ac.uk/postgraduate/taught/speechlanguageandsociolinguistics/',
'https://www.gla.ac.uk/postgraduate/taught/sportandexercisesciencemedicine/',
'https://www.gla.ac.uk/postgraduate/taught/statistics/',
'https://www.gla.ac.uk/postgraduate/taught/stemcellengineering/',
'https://www.gla.ac.uk/postgraduate/taught/structuralengineering/',
'https://www.gla.ac.uk/postgraduate/taught/sustainableenergy/',
'https://www.gla.ac.uk/postgraduate/taught/sustainablewaterenvironments/',
'https://www.gla.ac.uk/postgraduate/taught/teachingadults/',
'https://www.gla.ac.uk/postgraduate/taught/technicalarthistory/',
'https://www.gla.ac.uk/postgraduate/taught/tesolmed/',
'https://www.gla.ac.uk/postgraduate/taught/tesolmsc/',
'https://www.gla.ac.uk/postgraduate/taught/theatrepractices/',
'https://www.gla.ac.uk/postgraduate/taught/theatrestudies/',
'https://www.gla.ac.uk/postgraduate/taught/theoreticalphysics/',
'https://www.gla.ac.uk/postgraduate/taught/tourismdevelopmentculture/',
'https://www.gla.ac.uk/postgraduate/taught/tourismheritagedevelopment/',
'https://www.gla.ac.uk/postgraduate/taught/tourismheritagesustainability/',
'https://www.gla.ac.uk/postgraduate/taught/translationalmedicine/',
'https://www.gla.ac.uk/postgraduate/taught/translationstudiesprofessionalpractice/',
'https://www.gla.ac.uk/postgraduate/taught/transnationalcrime/',
'https://www.gla.ac.uk/postgraduate/taught/urbananalytics/',
'https://www.gla.ac.uk/postgraduate/taught/urbanresearch/',
'https://www.gla.ac.uk/postgraduate/taught/urbantransport/',
'https://www.gla.ac.uk/postgraduate/taught/victorianliterature/',
'https://www.gla.ac.uk/postgraduate/taught/warstudies/',]
    def parse(self, response):
        urls=['https://www.gla.ac.uk/postgraduate/taught/adulteducationcommunitydevelopmentyouthstudies/',
'https://www.gla.ac.uk/postgraduate/taught/adulteducationcommunitydevelopmentyouthwork/',
'https://www.gla.ac.uk/postgraduate/taught/adulteducationforsocialchangeinternationalmaster/',
'https://www.gla.ac.uk/postgraduate/taught/advancednursingsciences/',
'https://www.gla.ac.uk/postgraduate/taught/advancedstatistics/',
'https://www.gla.ac.uk/postgraduate/taught/aerospaceengineering/',
'https://www.gla.ac.uk/postgraduate/taught/aerospaceengineeringmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/ancientcultures/',
'https://www.gla.ac.uk/postgraduate/taught/animalwelfarescience/',
'https://www.gla.ac.uk/postgraduate/taught/appliedneuropsychology/',
'https://www.gla.ac.uk/postgraduate/taught/artcollectingprovenance/',
'https://www.gla.ac.uk/postgraduate/taught/arthistory/',
'https://www.gla.ac.uk/postgraduate/taught/arthistoryrenaissance/',
'https://www.gla.ac.uk/postgraduate/taught/assetpricinginvestment/',
'https://www.gla.ac.uk/postgraduate/taught/astrophysics/',
'https://www.gla.ac.uk/postgraduate/taught/bankingfinancialservices/',
'https://www.gla.ac.uk/postgraduate/taught/bioinformatics/',
'https://www.gla.ac.uk/postgraduate/taught/biomedicalengineering/',
'https://www.gla.ac.uk/postgraduate/taught/biomedicalsciencemsc/',
'https://www.gla.ac.uk/postgraduate/taught/biomedicalsciencesmres/',
'https://www.gla.ac.uk/postgraduate/taught/biostatistics/',
'https://www.gla.ac.uk/postgraduate/taught/biotechnology/',
'https://www.gla.ac.uk/postgraduate/taught/biotechnologyandmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/businessadministration/',
'https://www.gla.ac.uk/postgraduate/taught/cancersciences/',
'https://www.gla.ac.uk/postgraduate/taught/cardiovascularsciences/',
'https://www.gla.ac.uk/postgraduate/taught/celticstudies/',
'https://www.gla.ac.uk/postgraduate/taught/celticvikingarchaeology/',
'https://www.gla.ac.uk/postgraduate/taught/centraleasteuropeanrussianeurasianstudies/',
'https://www.gla.ac.uk/postgraduate/taught/chemistry/',
'https://www.gla.ac.uk/postgraduate/taught/chemistrywithmedicinalchemistry/',
'https://www.gla.ac.uk/postgraduate/taught/childrensliteratureandliteracies/',
'https://www.gla.ac.uk/postgraduate/taught/childrensliteraturemediaculture/',
'https://www.gla.ac.uk/postgraduate/taught/chinesestudies/',
'https://www.gla.ac.uk/postgraduate/taught/cityplanning/',
'https://www.gla.ac.uk/postgraduate/taught/cityplanningrealestatedevelopment/',
'https://www.gla.ac.uk/postgraduate/taught/civilengineering/',
'https://www.gla.ac.uk/postgraduate/taught/civilengineeringmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/classics/',
'https://www.gla.ac.uk/postgraduate/taught/clinicalgenetics/',
'https://www.gla.ac.uk/postgraduate/taught/clinicalneuropsychology/',
'https://www.gla.ac.uk/postgraduate/taught/clinicalnutrition/',
'https://www.gla.ac.uk/postgraduate/taught/clinicalpharmacology/',
'https://www.gla.ac.uk/postgraduate/taught/clinicaltrialsstratifiedmedicine/',
'https://www.gla.ac.uk/postgraduate/taught/comparativeliterature/',
'https://www.gla.ac.uk/postgraduate/taught/compositioncreativepractice/',
'https://www.gla.ac.uk/postgraduate/taught/computersystemsengineering/',
'https://www.gla.ac.uk/postgraduate/taught/computingsciencemsc/',
'https://www.gla.ac.uk/postgraduate/taught/conflictarchaeology/',
'https://www.gla.ac.uk/postgraduate/taught/conservationmanagementafricanecosystems/',
'https://www.gla.ac.uk/postgraduate/taught/corporateandfinanciallaw/',
'https://www.gla.ac.uk/postgraduate/taught/creativeindustriesandculturalpolicy/',
'https://www.gla.ac.uk/postgraduate/taught/creativewritingmlitt/',
'https://www.gla.ac.uk/postgraduate/taught/criminology/',
'https://www.gla.ac.uk/postgraduate/taught/criminologycriminaljustice/',
'https://www.gla.ac.uk/postgraduate/taught/criticalcare/',
'https://www.gla.ac.uk/postgraduate/taught/curatorialpractice/',
'https://www.gla.ac.uk/postgraduate/taught/dataanalytics/',
'https://www.gla.ac.uk/postgraduate/taught/datascience/',
'https://www.gla.ac.uk/postgraduate/taught/developmentstudies/',
'https://www.gla.ac.uk/postgraduate/taught/dresstextilehistories/',
'https://www.gla.ac.uk/postgraduate/taught/earlymodernhistory/',
'https://www.gla.ac.uk/postgraduate/taught/earlymodernliteratureculture/',
'https://www.gla.ac.uk/postgraduate/taught/ecologyenvironmentalbiology/',
'https://www.gla.ac.uk/postgraduate/taught/ecologyepidemiologyconservationbiology/',
'https://www.gla.ac.uk/postgraduate/taught/economicdevelopment/',
'https://www.gla.ac.uk/postgraduate/taught/economics/',
'https://www.gla.ac.uk/postgraduate/taught/economicsbankingfinance/',
'https://www.gla.ac.uk/postgraduate/taught/educationalstudiesmed/',
'https://www.gla.ac.uk/postgraduate/taught/educationalstudiesmsc/',
'https://www.gla.ac.uk/postgraduate/taught/educationpublicpolicyequity/',
'https://www.gla.ac.uk/postgraduate/taught/electronicselectricalengineering/',
'https://www.gla.ac.uk/postgraduate/taught/electronicselectricalengineeringmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/electronicsmanufacturing/',
'https://www.gla.ac.uk/postgraduate/taught/endodontics/',
'https://www.gla.ac.uk/postgraduate/taught/englishlanguagelinguistics/',
'https://www.gla.ac.uk/postgraduate/taught/englishliterature/',
'https://www.gla.ac.uk/postgraduate/taught/enhancedpracticeineducation/',
'https://www.gla.ac.uk/postgraduate/taught/environmentalchangesociety/',
'https://www.gla.ac.uk/postgraduate/taught/environmentalstatistics/',
'https://www.gla.ac.uk/postgraduate/taught/environmentculturecommunication/',
'https://www.gla.ac.uk/postgraduate/taught/environmentsociety/',
'https://www.gla.ac.uk/postgraduate/taught/environmentsustainabledevelopment/',
'https://www.gla.ac.uk/postgraduate/taught/equalityhumanrightsmres/',
'https://www.gla.ac.uk/postgraduate/taught/equalityhumanrightsmsc/',
'https://www.gla.ac.uk/postgraduate/taught/fantasy/',
'https://www.gla.ac.uk/postgraduate/taught/filmcuration/',
'https://www.gla.ac.uk/postgraduate/taught/filmmaking/',
'https://www.gla.ac.uk/postgraduate/taught/filmtelevisionstudies/',
'https://www.gla.ac.uk/postgraduate/taught/financeeconomicdevelopment/',
'https://www.gla.ac.uk/postgraduate/taught/financemanagement/',
'https://www.gla.ac.uk/postgraduate/taught/financialeconomics/',
'https://www.gla.ac.uk/postgraduate/taught/financialforecastinginvestment/',
'https://www.gla.ac.uk/postgraduate/taught/financialmodelling/',
'https://www.gla.ac.uk/postgraduate/taught/financialriskmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/foodsecurity/',
'https://www.gla.ac.uk/postgraduate/taught/forensictoxicology/',
'https://www.gla.ac.uk/postgraduate/taught/genderhistory/',
'https://www.gla.ac.uk/postgraduate/taught/geneticandgenomiccounsellingwithworkplacement/',
'https://www.gla.ac.uk/postgraduate/taught/geoinformationtechnologyandcartography/',
'https://www.gla.ac.uk/postgraduate/taught/geomaticsmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/geospatialandmappingsciences/',
'https://www.gla.ac.uk/postgraduate/taught/globaleconomy/',
'https://www.gla.ac.uk/postgraduate/taught/globalhealth/',
'https://www.gla.ac.uk/postgraduate/taught/globalmarketslocalcreativities/',
'https://www.gla.ac.uk/postgraduate/taught/globalmentalhealth/',
'https://www.gla.ac.uk/postgraduate/taught/globalmigrationssocialjusticemres/',
'https://www.gla.ac.uk/postgraduate/taught/globalmigrationssocialjusticemsc/',
'https://www.gla.ac.uk/postgraduate/taught/globalsecurity/',
'https://www.gla.ac.uk/postgraduate/taught/globalsecuritymres/',
'https://www.gla.ac.uk/postgraduate/taught/governanceaccountability/',
'https://www.gla.ac.uk/postgraduate/taught/healthcare/',
'https://www.gla.ac.uk/postgraduate/taught/historicallyinformedperformancepractice/',
'https://www.gla.ac.uk/postgraduate/taught/history/',
'https://www.gla.ac.uk/postgraduate/taught/historywithanemphasisonthehistoryofmedicine/',
'https://www.gla.ac.uk/postgraduate/taught/housingstudies/',
'https://www.gla.ac.uk/postgraduate/taught/humangeographyspacespoliticsecologies/',
'https://www.gla.ac.uk/postgraduate/taught/humannutrition/',
'https://www.gla.ac.uk/postgraduate/taught/humanrightsinternationalpolitics/',
'https://www.gla.ac.uk/postgraduate/taught/humanrightsinternationalpoliticsmres/',
'https://www.gla.ac.uk/postgraduate/taught/immunologyinflammatorydisease/',
'https://www.gla.ac.uk/postgraduate/taught/inclusiveeducationresearchpolicypracticemed/',
'https://www.gla.ac.uk/postgraduate/taught/infectionbiologywithspecialisms/',
'https://www.gla.ac.uk/postgraduate/taught/infectiousdiseasesantimicrobialresistance/',
'https://www.gla.ac.uk/postgraduate/taught/informationmanagementpreservation/',
'https://www.gla.ac.uk/postgraduate/taught/informationsecuritymsc/',
'https://www.gla.ac.uk/postgraduate/taught/informationtechnology/',
'https://www.gla.ac.uk/postgraduate/taught/intellectualproperty/',
'https://www.gla.ac.uk/postgraduate/taught/internationalaccountingfinancialmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/internationalbankingfinance/',
'https://www.gla.ac.uk/postgraduate/taught/internationalbusinessentrepreneurship/',
'https://www.gla.ac.uk/postgraduate/taught/internationalcommerciallaw/',
'https://www.gla.ac.uk/postgraduate/taught/internationalcompetitionlawpolicy/',
'https://www.gla.ac.uk/postgraduate/taught/internationalcorporatefinancebanking/',
'https://www.gla.ac.uk/postgraduate/taught/internationaleconomiclaw/',
'https://www.gla.ac.uk/postgraduate/taught/internationalfinance/',
'https://www.gla.ac.uk/postgraduate/taught/internationalfinancialanalysis/',
'https://www.gla.ac.uk/postgraduate/taught/internationalhumanresourcemanagementdevelopment/',
'https://www.gla.ac.uk/postgraduate/taught/internationallaw/',
'https://www.gla.ac.uk/postgraduate/taught/internationallawandsecurity/',
'https://www.gla.ac.uk/postgraduate/taught/internationalmanagementanddesigninnovation/',
'https://www.gla.ac.uk/postgraduate/taught/internationalrealestatemanagement/',
'https://www.gla.ac.uk/postgraduate/taught/internationalrelations/',
'https://www.gla.ac.uk/postgraduate/taught/internationalrelationsresearch/',
'https://www.gla.ac.uk/postgraduate/taught/internationalsecurity/',
'https://www.gla.ac.uk/postgraduate/taught/internationalstrategicmarketing/',
'https://www.gla.ac.uk/postgraduate/taught/inventingmodernart/',
'https://www.gla.ac.uk/postgraduate/taught/investmentbankingfinance/',
'https://www.gla.ac.uk/postgraduate/taught/investmentfundmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/itcybersecurity/',
'https://www.gla.ac.uk/postgraduate/taught/landhydrographicsurveying/',
'https://www.gla.ac.uk/postgraduate/taught/law/',
'https://www.gla.ac.uk/postgraduate/taught/lawmres/',
'https://www.gla.ac.uk/postgraduate/taught/management/',
'https://www.gla.ac.uk/postgraduate/taught/managementmres/',
'https://www.gla.ac.uk/postgraduate/taught/managementsustainabletourism/',
'https://www.gla.ac.uk/postgraduate/taught/managementwithenterprise/',
'https://www.gla.ac.uk/postgraduate/taught/managementwithhumanresources/',
'https://www.gla.ac.uk/postgraduate/taught/managementwithinternationalfinance/',
'https://www.gla.ac.uk/postgraduate/taught/materialcultureartefactstudies/',
'https://www.gla.ac.uk/postgraduate/taught/mathematicsappliedmathematics/',
'https://www.gla.ac.uk/postgraduate/taught/mechanicalengineering/',
'https://www.gla.ac.uk/postgraduate/taught/mechanicalengineeringmanagement/',
'https://www.gla.ac.uk/postgraduate/taught/mechatronics/',
'https://www.gla.ac.uk/postgraduate/taught/mediacommunicationsinternationaljournalism/',
'https://www.gla.ac.uk/postgraduate/taught/mediamanagement/',
'https://www.gla.ac.uk/postgraduate/taught/medicalgeneticsandgenomics/',
'https://www.gla.ac.uk/postgraduate/taught/medicalphysics/',
'https://www.gla.ac.uk/postgraduate/taught/medicalvisualisation/',
'https://www.gla.ac.uk/postgraduate/taught/medievalhistory/',
'https://www.gla.ac.uk/postgraduate/taught/modernhistory/',
'https://www.gla.ac.uk/postgraduate/taught/modernities/',
'https://www.gla.ac.uk/postgraduate/taught/modernmaterialartefacts/',
'https://www.gla.ac.uk/postgraduate/taught/museumeducation/',
'https://www.gla.ac.uk/postgraduate/taught/museumstudiesartefactsmaterialculture/',
'https://www.gla.ac.uk/postgraduate/taught/museumstudiescollectingcollections/',
'https://www.gla.ac.uk/postgraduate/taught/museumstudiestheorypractice/',
'https://www.gla.ac.uk/postgraduate/taught/musicindustries/',
'https://www.gla.ac.uk/postgraduate/taught/musicology/',
'https://www.gla.ac.uk/postgraduate/taught/nanosciencenanotechnology/',
'https://www.gla.ac.uk/postgraduate/taught/oralmaxillofacialsurgery/',
'https://www.gla.ac.uk/postgraduate/taught/oralsciences/',
'https://www.gla.ac.uk/postgraduate/taught/philosophy/',
'https://www.gla.ac.uk/postgraduate/taught/philosophymlitt/',
'https://www.gla.ac.uk/postgraduate/taught/physicsadvancedmaterials/',
'https://www.gla.ac.uk/postgraduate/taught/physicsenergyandtheenvironment/',
'https://www.gla.ac.uk/postgraduate/taught/physicsnucleartechnology/',
'https://www.gla.ac.uk/postgraduate/taught/playwritingdramaturgy/',
'https://www.gla.ac.uk/postgraduate/taught/politicalcommunicationmres/',
'https://www.gla.ac.uk/postgraduate/taught/politicalcommunicationmscpgdip/',
'https://www.gla.ac.uk/postgraduate/taught/productdesignengineering/',
'https://www.gla.ac.uk/postgraduate/taught/psychologicalscienceconversion/',
'https://www.gla.ac.uk/postgraduate/taught/psychologicalscienceresearchmethodsof/',
'https://www.gla.ac.uk/postgraduate/taught/psychologicalstudiesconversion/',
'https://www.gla.ac.uk/postgraduate/taught/publicandurbanpolicy/',
'https://www.gla.ac.uk/postgraduate/taught/publichealth/',
'https://www.gla.ac.uk/postgraduate/taught/publicpolicymanagement/',
'https://www.gla.ac.uk/postgraduate/taught/publicpolicyresearch/',
'https://www.gla.ac.uk/postgraduate/taught/quantitativefinance/',
'https://www.gla.ac.uk/postgraduate/taught/quantumtechnology/',
'https://www.gla.ac.uk/postgraduate/taught/realestate/',
'https://www.gla.ac.uk/postgraduate/taught/religionliteratureculture/',
'https://www.gla.ac.uk/postgraduate/taught/romanticworlds/',
'https://www.gla.ac.uk/postgraduate/taught/russiancentraleasteuropeanstudiesmres/',
'https://www.gla.ac.uk/postgraduate/taught/russiancentraleasteuropeanstudiesmsc/',
'https://www.gla.ac.uk/postgraduate/taught/scottishhistory/',
'https://www.gla.ac.uk/postgraduate/taught/sensorandimagingsystems/',
'https://www.gla.ac.uk/postgraduate/taught/sociolegalstudies/',
'https://www.gla.ac.uk/postgraduate/taught/sociology/',
'https://www.gla.ac.uk/postgraduate/taught/sociologyresearchmethods/',
'https://www.gla.ac.uk/postgraduate/taught/softwaredevelopment/',
'https://www.gla.ac.uk/postgraduate/taught/sounddesignaudiovisualpractice/',
'https://www.gla.ac.uk/postgraduate/taught/southeuropeanstudies/',
'https://www.gla.ac.uk/postgraduate/taught/speechlanguageandsociolinguistics/',
'https://www.gla.ac.uk/postgraduate/taught/sportandexercisesciencemedicine/',
'https://www.gla.ac.uk/postgraduate/taught/statistics/',
'https://www.gla.ac.uk/postgraduate/taught/stemcellengineering/',
'https://www.gla.ac.uk/postgraduate/taught/structuralengineering/',
'https://www.gla.ac.uk/postgraduate/taught/sustainableenergy/',
'https://www.gla.ac.uk/postgraduate/taught/sustainablewaterenvironments/',
'https://www.gla.ac.uk/postgraduate/taught/teachingadults/',
'https://www.gla.ac.uk/postgraduate/taught/technicalarthistory/',
'https://www.gla.ac.uk/postgraduate/taught/tesolmed/',
'https://www.gla.ac.uk/postgraduate/taught/tesolmsc/',
'https://www.gla.ac.uk/postgraduate/taught/theatrepractices/',
'https://www.gla.ac.uk/postgraduate/taught/theatrestudies/',
'https://www.gla.ac.uk/postgraduate/taught/theoreticalphysics/',
'https://www.gla.ac.uk/postgraduate/taught/tourismdevelopmentculture/',
'https://www.gla.ac.uk/postgraduate/taught/tourismheritagedevelopment/',
'https://www.gla.ac.uk/postgraduate/taught/tourismheritagesustainability/',
'https://www.gla.ac.uk/postgraduate/taught/translationalmedicine/',
'https://www.gla.ac.uk/postgraduate/taught/translationstudiesprofessionalpractice/',
'https://www.gla.ac.uk/postgraduate/taught/transnationalcrime/',
'https://www.gla.ac.uk/postgraduate/taught/urbananalytics/',
'https://www.gla.ac.uk/postgraduate/taught/urbanresearch/',
'https://www.gla.ac.uk/postgraduate/taught/urbantransport/',
'https://www.gla.ac.uk/postgraduate/taught/victorianliterature/',
'https://www.gla.ac.uk/postgraduate/taught/warstudies/',]
        for u in urls:
            yield scrapy.Request(url=u,callback=self.tuition,meta={'url':u})
    def tuition(self,response):
        item=get_item1(ScrapyschoolEnglandItem1)
        item['url']=response.meta['url']
        item['university'] = 'University of Glasgow'
        print(response.url)
        programme=response.xpath('//div[@id="prog-title"]/h1/text()').extract()
        # print(programme)
        item['programme_en']=''.join(programme).strip()
        tuition=response.xpath('//h4[contains(text(),"nternationa")]/following-sibling::ul/li/strong[contains(text(),"ull")]/following-sibling::text()[1]').extract()
        print(tuition)
        # yield item
        if tuition!=[]:
            item['tuition_fee']=tuition[0].replace('£','').strip()
            yield item

    def parsess(self, response):
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university'] = 'University of Glasgow'
        item['url'] = response.url
        overview1=response.xpath('//p[@class="intro-sentence"]').extract()
        overview = response.xpath('//h2[contains(text(),"Why this programme")]/following-sibling::*').extract()
        overview = remove_class(overview)
        if overview1!=[]:
            overview1=remove_class(overview1)
            item['overview_en']=overview1+overview
        else:
            item['overview_en']=overview
        yield item
    def parses(self, response):
        urllist=response.xpath('//ul[@id="jquerylist"]/li/a/@href').extract()
        for i in urllist:
            fullurl='https://www.gla.ac.uk%s' % i
            self.pro_lis.append(fullurl)
            yield scrapy.Request(fullurl,callback=self.parse_main)
            # print(len(self.pro_lis))
    def parse_main(self,response):
        item=get_item1(ScrapyschoolEnglandItem1)
        print(response.url)
        item['teach_time'] = 'fulltime'
        item['university'] = 'University of Glasgow'
        item['url'] = response.url
        item['location'] = 'Glasgow'
        item['start_date'] = '2018-9'
        item['deadline'] = '2018-7'
        item["tuition_fee_pre"] = "£"
        item['teach_type']='taught'

        programme=response.xpath('//div[@id="prog-title"]/h1/text()').extract()
        programme=''.join(programme)
        item['programme_en'] = programme
        degree_type=response.xpath('//div[@id="prog-title"]/h1/span/text()').extract()
        degree_type=''.join(degree_type)
        item['degree_name'] = degree_type
        duration=response.xpath('//li[contains(text(),"full-time")]/text()').extract()
        duration=clear_duration(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']
        # print(durations)

        overview=response.xpath('//h2[contains(text(),"Why this programme")]/following-sibling::*').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        modules=response.xpath('//h2[contains(text(),"Programme str")]/following-sibling::*').extract()
        modules=clear_same_s(modules)
        modules=remove_class(modules)
        item['modules_en'] = modules
        # print(modules)

        career=response.xpath('//h2[contains(text(),"Career")]/following-sibling::*').extract()
        career=clear_same_s(career)
        career=remove_class(career)
        item['career_en'] = career

        fees=response.xpath('//h2[contains(text(),"Fees and")]/following-sibling::div//text()').extract()
        fees=response.xpath('//div[@id="fees"]//text()').extract()
        # print(fees)
        tuition_fee=getTuition_fee(fees)
        # print(tuition_fee)
        if tuition_fee==2018:
            tuition_fee='0'
        # print(tuition_fee)
        item['tuition_fee'] = tuition_fee

        IELTS=response.xpath('//*[contains(text(),"IELTS")]/../following-sibling::ul[1]//text()').extract()
        # print(IELTS)
        ielts=get_ielts(IELTS)
        if ielts!={} and ielts!=[]:
            item['ielts_l'] = ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            item['ielts'] = ielts['IELTS']
        TOEFL=response.xpath('//*[contains(text(),"TOEFL")]/..//text()').extract()
        # print(TOEFL)
        toefl=get_toefl(TOEFL)
        if toefl!=[]:
            try:
                item['toefl_r'] = toefl[1]
                item['toefl_l'] = toefl[2]
                item['toefl_s'] = toefl[3]
                item['toefl_w'] = toefl[4]
                item['toefl'] = toefl[0]
            except:
                pass

        entry=response.xpath('//h2[contains(text(),"Entry requirements")]/following-sibling::*').extract()
        entry=clear_same_s(entry)
        entry=remove_class(entry)
        item['rntry_requirements'] = entry

        apply_d=response.xpath('//h3[contains(text(),"Documents")]/following-sibling::ul[1]').extract()
        apply_d=clear_same_s(apply_d)
        item['apply_proces_en'] = remove_class(apply_d)

        if programme!='':
            yield item

        # print(item)
        # yield item
