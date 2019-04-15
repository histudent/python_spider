# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/8 14:33'
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
class UniversityofExeterSpider(scrapy.Spider):
    name = 'UniversityofExeter_u'
    allowed_domains = ['exeter.ac.uk/']
    start_urls = []
    C= [
        'https://www.exeter.ac.uk/undergraduate/degrees/accounting/businessacc/',
        'https://www.exeter.ac.uk/undergraduate/degrees/accounting/businessacceu/',
        'https://www.exeter.ac.uk/undergraduate/degrees/accounting/businessaccexp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/accounting/businessaccint/',
        'https://www.exeter.ac.uk/undergraduate/degrees/accounting/accountfin/',
        'https://www.exeter.ac.uk/undergraduate/degrees/accounting/accountfineu/',
        'https://www.exeter.ac.uk/undergraduate/degrees/accounting/accountfinexp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/accounting/accountfinint/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/ancient/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/ancientarch/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/ancientarch-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/ancientarch-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/ancient-history-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/ancient-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/animal/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/animalmsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/animalwpp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/animalwsa/',
        'https://www.exeter.ac.uk/undergraduate/degrees/anthropology/anthropologyba/',
        'https://www.exeter.ac.uk/undergraduate/degrees/anthropology/anthropologyba-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geology/applied/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geology/appliedmgeol/',
        'https://www.exeter.ac.uk/undergraduate/degrees/psychology/msciapppsy/',
        'https://www.exeter.ac.uk/undergraduate/degrees/arabislamic/marabic/',
        'https://www.exeter.ac.uk/undergraduate/degrees/archaeology/arch/',
        'https://www.exeter.ac.uk/undergraduate/degrees/archaeology/archanth/',
        'https://www.exeter.ac.uk/undergraduate/degrees/archaeology/archanth-experience/',
        'https://www.exeter.ac.uk/undergraduate/degrees/archaeology/archanth-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/archaeology/arch-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/archaeology/forensic/',
        'https://www.exeter.ac.uk/undergraduate/degrees/archaeology/forensic-experience/',
        'https://www.exeter.ac.uk/undergraduate/degrees/archaeology/forensic-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/archaeology/arch-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/arthist/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/arthistclassics/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/classics-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/arthistclassics-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/drama/dramavc/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/drama-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/drama/dramavc-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/arthistenglish/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/english-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/arthistenglish-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/arthistfilm/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/arthistfilm-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/arthistfilmabroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/arthisthistory/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/history-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/arthisthistory-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/arthistmodlang/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/arthist-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/art/arthist-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/law/bbllaw/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/biochem/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/biochemexp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/biochemwsa/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/biosci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/biosciprof/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/biosciwsa/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/biomed/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/biomedexp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/biomedwsa/',
        'https://www.exeter.ac.uk/undergraduate/degrees/business/businessbsc/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/busecon/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/buseconeu/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/buseconexp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/buseconint/',
        'https://www.exeter.ac.uk/undergraduate/degrees/business/businessman/',
        'https://www.exeter.ac.uk/undergraduate/degrees/business/businessmaneu/',
        'https://www.exeter.ac.uk/undergraduate/degrees/business/businessmanexp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/business/businessmanint/',
        'https://www.exeter.ac.uk/undergraduate/degrees/business/businesseu/',
        'https://www.exeter.ac.uk/undergraduate/degrees/business/businessexp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/business/businessint/',
        'https://www.exeter.ac.uk/undergraduate/degrees/business/manager-degree-apprenticeship/',
        'https://www.exeter.ac.uk/undergraduate/degrees/languages/modlang/chinese/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/civil/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/civil-engineering/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/civilmeng/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/environmental/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/classical/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/classics-english/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/classics-english-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/classics-english-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/classics-modlang/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/classics-philosophy/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/classics-philosophy-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/classics-philosophy-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/classics-theology/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/classics-theology-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/classics-theology-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/classical-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/classical-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/classics/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/classics-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/classics/classics-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/computerscience/comsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/computerscience/comscimsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/computerscience/comscimaths/',
        'https://www.exeter.ac.uk/undergraduate/degrees/computerscience/comscimathsmsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/computerscience/comscimaths-placement/',
        'https://www.exeter.ac.uk/undergraduate/degrees/computerscience/comsci-placement/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/conservation/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/conservationmsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/conservationwpp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/conservationwsa/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/cornwall/',
        'https://www.exeter.ac.uk/undergraduate/degrees/sociology/criminologybsc/',
        'https://www.exeter.ac.uk/undergraduate/degrees/sociology/criminologybsc-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/computerscience/digital-technology-apprenticeship/',
        'https://www.exeter.ac.uk/undergraduate/degrees/drama/drama/',
        'https://www.exeter.ac.uk/undergraduate/degrees/drama/drama-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/drama/dramawsa/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/economics/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/finance/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/financeeu/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/financeexp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/financeint/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/politics/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/politicseu/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/politicsexp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/politicsint/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/econometrics/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/econometricseu/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/econometricsexp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/econometricsint/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/economicseu/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/economicsexp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/economics/economicsint/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/electronic/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/electronicmeng/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/eleccomp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/eleccompmeng/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/engineering/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geology/engineering/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geology/engineeringmgeol/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/engineeringmeng/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/entrepreneurshipbeng/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/engineering-entrepreneurship/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/management/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/managementmeng/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/english/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/baenglish/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/engdrama/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/englishdrama-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/engdrama-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/film/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/film-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/film-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/history/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/history-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/history-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/english-modlang/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/english-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/baenglish-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/english-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/baenglish-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/english/englishna/',
        'https://www.exeter.ac.uk/undergraduate/degrees/envsci/envscimsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/envsci/envsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/envsci/envsciwpp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/envsci/envsciwsa/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/evobiology/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/evobiologymsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/evobiologywpp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/evobiologywsa/',
        'https://www.exeter.ac.uk/undergraduate/degrees/sport/exsport/',
        'https://www.exeter.ac.uk/undergraduate/degrees/sport/exsportmsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/film/film/',
        'https://www.exeter.ac.uk/undergraduate/degrees/film/film-modlang/',
        'https://www.exeter.ac.uk/undergraduate/degrees/film/film-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/film/film-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/flexible/cornwall/',
        'https://www.exeter.ac.uk/undergraduate/degrees/flexible/exeter/',
        'https://www.exeter.ac.uk/undergraduate/degrees/flexible/cornwall-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/flexible/exeter-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/flexible/cornwall-studyworkabroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/flexible/exeter-studyworkabroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/flexible/cornwall-experience/',
        'https://www.exeter.ac.uk/undergraduate/degrees/flexible/exeter-experience/',
        'https://www.exeter.ac.uk/undergraduate/degrees/flexible/cornwall-work-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/flexible/exeter-work-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/foundation/foundation/',
        'https://www.exeter.ac.uk/undergraduate/degrees/languages/modlang/french/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geography/exegeogba/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geography/corngeogbabsc/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geography/exegeogbsc/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geography/geography-gis/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geography/geography-gis-eu/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geography/geography-gis-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geography/exegeogba-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geography/exegeogbsc-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geography/corngeogbabscwpp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geography/exegeogbawsa/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geography/corngeogbabscwsa/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geography/exegeogbscwsa/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geology/geology/',
        'https://www.exeter.ac.uk/undergraduate/degrees/geology/geologymgeol/',
        'https://www.exeter.ac.uk/undergraduate/degrees/languages/modlang/german/',
        'https://www.exeter.ac.uk/undergraduate/degrees/law/gradllb/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/historyexe/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/bahistory/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/history-ancient/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/history-ancient-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/history-ancient-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/hist-arch/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/history-arch-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/hist-arch-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/history-intrel/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/intrel-corn/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/intrel-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/hist-intrel-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/intrel-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/intrel-corn-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/history-modlang/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/history-politics-corn/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/hist-pol-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/histpol-abroad-corn/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/historyexe-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/bahistory-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/historyexeabroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/bahistoryabroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/sport/humanbio/',
        'https://www.exeter.ac.uk/undergraduate/degrees/humansciences/humansciences/',
        'https://www.exeter.ac.uk/undergraduate/degrees/humansciences/humansciwpp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/humansciences/humansciwsa/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/intrelations/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/cornwallir/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/intlrel_modlang/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/intrelations-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/cornwallir-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/foundation/internationalyearone/',
        'https://www.exeter.ac.uk/undergraduate/degrees/languages/modlang/italian/',
        'https://www.exeter.ac.uk/undergraduate/degrees/law/master1/',
        'https://www.exeter.ac.uk/undergraduate/degrees/law/lawbusiness/',
        'https://www.exeter.ac.uk/undergraduate/degrees/law/law/',
        'https://www.exeter.ac.uk/undergraduate/degrees/law/laweurostudy/',
        'https://www.exeter.ac.uk/undergraduate/degrees/libarts/liberal/',
        'https://www.exeter.ac.uk/undergraduate/degrees/libarts/liberal-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/libarts/liberal-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/business/marketing/',
        'https://www.exeter.ac.uk/undergraduate/degrees/business/marketingeu/',
        'https://www.exeter.ac.uk/undergraduate/degrees/business/marketingexp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/business/marketingint/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/marinebio/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/marinebiomsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/marinebiowpp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/marinebiowsa/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/materials/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/materialsmeng/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathsmsci-ecology/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathsmsci-energy/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathsmsci-environment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathematical-sciences-bsc/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathsmsci-climate/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathssci-geophysical/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathsmsci-biology/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathsbsc/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathsmm/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/maths-physics/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathsaccounting/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathsaccountingmsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathseconomics/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathseconomicsmsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathsfinance/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathsfinancemsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/internationalmm/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathsmanage/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/mathsmanagemsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mathematics/professionalmm/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/mechanical/',
        'https://www.exeter.ac.uk/undergraduate/degrees/engineering/mechanicalmeng/',
        'https://www.exeter.ac.uk/undergraduate/degrees/medical-imaging/imaging/',
        'https://www.exeter.ac.uk/undergraduate/degrees/medicalsci/environment-health-msci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/medicalsci/human-genomics-msci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/medicalsci/medicalsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/medicalsci/medicalscipty/',
        'https://www.exeter.ac.uk/undergraduate/degrees/medicinehealth/medicine/',
        'https://www.exeter.ac.uk/undergraduate/degrees/medicine/medicine/',
        'https://www.exeter.ac.uk/undergraduate/degrees/arabislamic/mideast/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mining/miningb/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mining/miningb/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mining/miningm/',
        'https://www.exeter.ac.uk/undergraduate/degrees/mining/miningm/',
        'https://www.exeter.ac.uk/undergraduate/degrees/languages/modlang/',
        'https://www.exeter.ac.uk/undergraduate/degrees/languages/modlang-arabic/',
        'https://www.exeter.ac.uk/undergraduate/degrees/languages/latin/',
        'https://www.exeter.ac.uk/undergraduate/degrees/natural-sciences/bsc/',
        'https://www.exeter.ac.uk/undergraduate/degrees/natural-sciences/msci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/neuroscience/neuroscience/',
        'https://www.exeter.ac.uk/undergraduate/degrees/neuroscience/neurosciencepty/',
        'https://www.exeter.ac.uk/undergraduate/degrees/nursing/nursingmsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/philosophy/philosophy/',
        'https://www.exeter.ac.uk/undergraduate/degrees/philosophy/combined/',
        'https://www.exeter.ac.uk/undergraduate/degrees/philosophy/history/',
        'https://www.exeter.ac.uk/undergraduate/degrees/philosophy/history-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/philosophy/modlang/',
        'https://www.exeter.ac.uk/undergraduate/degrees/philosophy/politics/',
        'https://www.exeter.ac.uk/undergraduate/degrees/philosophy/politics-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/philosophy/sociology/',
        'https://www.exeter.ac.uk/undergraduate/degrees/philosophy/sociology-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/philosophy/theology/',
        'https://www.exeter.ac.uk/undergraduate/degrees/philosophy/theology-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/philosophy/philosophy-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/physics/physicbsc/',
        'https://www.exeter.ac.uk/undergraduate/degrees/physics/physicsmphys/',
        'https://www.exeter.ac.uk/undergraduate/degrees/physics/astrobsc/',
        'https://www.exeter.ac.uk/undergraduate/degrees/physics/astromphys/',
        'https://www.exeter.ac.uk/undergraduate/degrees/physics/physicsaustrmphys/',
        'https://www.exeter.ac.uk/undergraduate/degrees/physics/physicsusa/',
        'https://www.exeter.ac.uk/undergraduate/degrees/physics/professional/',
        'https://www.exeter.ac.uk/undergraduate/degrees/physics/physicsnz/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/politics/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/combined/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/cornwallpolir/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/politicsir/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/cornwallpolir-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/politicsir-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/modlang/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/sociology/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/sociology-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/politics-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/ppe/',
        'https://www.exeter.ac.uk/undergraduate/degrees/politics/ppe-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/languages/modlang/portuguese/',
        'https://www.exeter.ac.uk/undergraduate/degrees/accounting/exemptions/',
        'https://www.exeter.ac.uk/undergraduate/degrees/psychology/psychbsc/',
        'https://www.exeter.ac.uk/undergraduate/degrees/psychology/psychsport/',
        'https://www.exeter.ac.uk/undergraduate/degrees/psychology/psycbsc-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/energy/energybsc/',
        'https://www.exeter.ac.uk/undergraduate/degrees/energy/energy-engineering-beng/',
        'https://www.exeter.ac.uk/undergraduate/degrees/energy/energy-engineering-beng/',
        'https://www.exeter.ac.uk/undergraduate/degrees/energy/energy-engineering-meng/',
        'https://www.exeter.ac.uk/undergraduate/degrees/energy/energy-engineering-meng/',
        'https://www.exeter.ac.uk/undergraduate/degrees/energy/energy-engineering-ind-meng/',
        'https://www.exeter.ac.uk/undergraduate/degrees/energy/energy-engineering-ind-meng/',
        'https://www.exeter.ac.uk/undergraduate/degrees/languages/modlang/russian/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/scitechsoc/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/scitechsoc-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/history/scitechsocabroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/sociology/sociology/',
        'https://www.exeter.ac.uk/undergraduate/degrees/sociology/sociologybsc/',
        'https://www.exeter.ac.uk/undergraduate/degrees/sociology/combined/',
        'https://www.exeter.ac.uk/undergraduate/degrees/sociology/anthropology/',
        'https://www.exeter.ac.uk/undergraduate/degrees/sociology/anthropology-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/sociology/criminology/',
        'https://www.exeter.ac.uk/undergraduate/degrees/sociology/criminology-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/sociology/modlang/',
        'https://www.exeter.ac.uk/undergraduate/degrees/sociology/sociology-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/sociology/sociologybsc-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/languages/modlang/spanish/',
        'https://www.exeter.ac.uk/undergraduate/degrees/medicalsci/sport-exercise/',
        'https://www.exeter.ac.uk/undergraduate/degrees/medicalsci/sport-exercisepty/',
        'https://www.exeter.ac.uk/undergraduate/degrees/theology/theology/',
        'https://www.exeter.ac.uk/undergraduate/degrees/theology/theology-employment/',
        'https://www.exeter.ac.uk/undergraduate/degrees/theology/theology-abroad/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/zoology/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/zoologymsci/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/zoologywpp/',
        'https://www.exeter.ac.uk/undergraduate/degrees/biosciences/zoologywsa/'
    ]
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Exeter'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="left-col"]/h1/span').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en).replace('&amp; ','').strip()
        if len(programme_en)==0:
            programme_en_a = response.xpath('//*[@id="left-col"]/h1').extract()
            programme_en_a = ''.join(programme_en_a)
            programme_en_a = remove_tags(programme_en_a).replace('&amp; ', '').strip()
            if 'BA' in programme_en_a:
                programme_en = programme_en.replace('BA','').strip()
            else:
                programme_en = programme_en_a
        # print(programme_en)

        #4.degree_type
        degree_type = 1

        #5.degree_name
        degree_name = response.xpath('//*[@id="left-col"]/h1/text()').extract()
        degree_name = ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        if 'BA/' in degree_name:
            degree_name = degree_name
        elif 'BA' in degree_name:
            degree_name = 'BA'
        else:pass
        # print(degree_name)

        #6.duration
        duration = response.xpath("//*[contains(text(),'Duration')]//following-sibling::*").extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        # print(duration)

        #7.location
        location = response.xpath("//*[contains(text(),'Location')]//following-sibling::*").extract()
        location = ''.join(location)
        location = remove_tags(location).strip()
        if len(location)>300:
            location ="Streatham (Exeter),St Luke's (Exeter)"
        # print(location)

        #8.alevel
        try:
            alevel_list = response.xpath("//*[contains(text(),'Typical offer')]//following-sibling::*").extract()[0]
            alevel_list = ''.join(alevel_list)
            alevel_list = remove_tags(alevel_list)
        except:
            alevel_list = ''
        # print(alevel_list)
        try:
            alevel = re.findall('[ABC\*\-]+;',alevel_list)[0]
        except:
            alevel=''
        alevel = alevel.replace(';','').strip()
        # print(alevel)

        #9.ib
        try:
            ib = re.findall('IB[\s:\d+\-]+;',alevel_list)[0]
        except:
            ib = ''
        ib = ib .replace(';','').strip()
        # print(ib)

        #10.overview_en
        overview_en = response.xpath('//*[@id="Overview"]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #11.modules_en
        modules_en = response.xpath('//*[@id="Programme-structure"]').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #12.apply_desc_en
        apply_desc_en = response.xpath('//*[@id="Entry-requirements"]').extract()
        apply_desc_en = ''.join(apply_desc_en)
        apply_desc_en = remove_class(apply_desc_en)
        # print(apply_desc_en)

        #13.assessment_en
        assessment_en = response.xpath("//*[contains(text(),'Assessment')]//following-sibling::*").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        # print(assessment_en)

        #14.career_en
        career_en = response.xpath('//*[@id="Careers"]').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        #15.deadline
        deadline = '2019-1-15,2019-6-30'

        #16.ielts 17181920  21.toefl 22232425
        if 'Accounting' in programme_en:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
            toefl = 90
            toefl_w =21
            toefl_l =21
            toefl_r =22
            toefl_s =23
        elif 'Business' in programme_en:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
            toefl = 90
            toefl_w = 21
            toefl_l = 21
            toefl_r = 22
            toefl_s = 23
        elif 'Economics' in programme_en:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
            toefl = 90
            toefl_w = 21
            toefl_l = 21
            toefl_r = 22
            toefl_s = 23
        elif 'English' in programme_en:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
            toefl = 90
            toefl_w = 21
            toefl_l = 21
            toefl_r = 22
            toefl_s = 23
        elif 'History' in programme_en:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
            toefl = 90
            toefl_w = 21
            toefl_l = 21
            toefl_r = 22
            toefl_s = 23
        elif 'Psychology' in programme_en:
            ielts = 6.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_s = 6.0
            ielts_l = 6.0
            toefl = 90
            toefl_w = 21
            toefl_l = 21
            toefl_r = 22
            toefl_s = 23
        elif 'Medical Imaging' in programme_en:
            ielts = 7.0
            ielts_r = 6.5
            ielts_w = 6.5
            ielts_s = 6.5
            ielts_l = 6.5
            toefl = 100
            toefl_w = 25
            toefl_l = 21
            toefl_r = 22
            toefl_s = 23
        elif 'Medicine' in programme_en:
            ielts = 7.5
            ielts_r = 6.0
            ielts_w = 6.0
            ielts_s = 7.0
            ielts_l = 7.0
            toefl = 110
            toefl_w = 21
            toefl_l = 25
            toefl_r = 22
            toefl_s = 25
        elif 'Biosciences' in programme_en:
            ielts = 6.5
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
            toefl = 90
            toefl_w = 21
            toefl_l = 18
            toefl_r = 18
            toefl_s = 18
        elif 'Environmental Science' in programme_en:
            ielts = 6.5
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
            toefl = 90
            toefl_w = 21
            toefl_l = 18
            toefl_r = 18
            toefl_s = 18
        elif 'Geography' in programme_en:
            ielts = 6.5
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
            toefl = 90
            toefl_w = 21
            toefl_l = 18
            toefl_r = 18
            toefl_s = 18
        elif 'Natural Sciences' in programme_en:
            ielts = 6.5
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
            toefl = 90
            toefl_w = 21
            toefl_l = 18
            toefl_r = 18
            toefl_s = 18
        elif 'Sport Sciences' in programme_en:
            ielts = 6.5
            ielts_r = 5.5
            ielts_w = 5.5
            ielts_s = 5.5
            ielts_l = 5.5
            toefl = 90
            toefl_w = 21
            toefl_l = 18
            toefl_r = 18
            toefl_s = 18
        else:
            ielts = 6.5
            ielts_r = 5.5
            ielts_w = 6.0
            ielts_s = 5.5
            ielts_l = 5.5
            toefl = 90
            toefl_w = 21
            toefl_l = 21
            toefl_r = 22
            toefl_s = 23

        #26.ucascode
        ucascode = response.xpath("//*[contains(text(),'UCAS code')]//following-sibling::*").extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode)
        # print(ucascode)

        #27.tuition_fee
        if 'Business' in programme_en:
            tuition_fee = 16900
        elif 'Economics' in programme_en:
            tuition_fee = 16900
        elif 'Geography' in programme_en:
            tuition_fee = 16900
        elif 'Law' in programme_en:
            tuition_fee = 16900
        elif 'Arts' in programme_en:
            tuition_fee = 16900
        elif 'Biosciences' in programme_en:
            tuition_fee = 19700
        elif 'Medical Sciences' in programme_en:
            tuition_fee = 19700
        elif 'Psychology' in programme_en:
            tuition_fee = 19700
        elif 'Sport Sciences' in programme_en:
            tuition_fee = 19700
        elif 'Combined' in programme_en:
            tuition_fee = 17995
        elif 'Accounting and Finance' in programme_en:
            tuition_fee = 17500
        elif 'Accounting and Business' in programme_en:
            tuition_fee = 17500
        elif 'Computer Science' in programme_en:
            tuition_fee = 22500
        elif 'Engineering' in programme_en:
            tuition_fee = 22500
        elif 'Physics' in programme_en:
            tuition_fee = 22500
        elif 'Geology' in programme_en:
            tuition_fee = 22500
        elif 'Mining' in programme_en:
            tuition_fee = 22500
        elif 'Mathematics' in programme_en:
            tuition_fee = 20500
        else:
            tuition_fee = 16900

        #28.apply_proces_en
        apply_proces_en = '<p>International applicants If you live outside the UK, you should also apply via UCAS using Apply online. Advice is available from British Council offices and other centres overseas, such as your school or one of our local representatives. You can obtain contact details for your local British Council Office. Details of approved University representatives can be obtained from the ‘In Your Country’ section of our International Students website.We encourage you to apply as early as possible and before 15 January but will continue to consider applications from international students until 30 June if places are available. After this date we will consider applications through Clearing or Adjustment for any vacancies we may still have.If you think you may be assessed as a ‘Home/EU’ student for tuition fees purposes, then you should apply by 15 January.English language requirements If English is not your first language and you have not completed your education in an English-speaking country (ie, the UK, Anglophone Canada, USA, Australia or New Zealand), you will need to submit evidence of a good command of English before starting your degree programme. Further information can be found on our English language requirements page. Study abroad Applicants wanting to study at the University for only one or two semesters under our Study Abroad programme should apply direct to the University. Application forms are available from the Study Abroad website.</p>'

        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['duration'] = duration
        item['location'] = location
        item['alevel'] = alevel
        item['ib'] = ib
        item['overview_en'] = overview_en
        item['modules_en'] = modules_en
        item['apply_desc_en'] = apply_desc_en
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['deadline'] = deadline
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl'] = toefl
        item['toefl_w'] = toefl_w
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['tuition_fee'] = tuition_fee
        item['apply_proces_en'] = apply_proces_en

        ucascode_a = response.xpath("//*[contains(text(),'UCAS code')]//following-sibling::*").extract()
        ucascode_a = ''.join(ucascode_a)
        ucascode_a = remove_tags(ucascode_a)
        if '/' in ucascode_a:
            response_ucascode = ucascode_a.split('/')
            for i in response_ucascode:
                response_ucascode = i
                response_ucascode = response_ucascode.strip()
                item['ucascode'] = response_ucascode
                yield item
        else:
            item['ucascode'] = ucascode
            yield item
