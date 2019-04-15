import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'text1'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['https://warwick.ac.uk/study/postgraduate/courses-2018/be',
'https://warwick.ac.uk/study/postgraduate/courses-2018/bbbm',
'https://warwick.ac.uk/study/postgraduate/courses-2018/bespsy',
'https://warwick.ac.uk/study/postgraduate/courses-2018/bes',
'https://warwick.ac.uk/study/postgraduate/courses-2018/bddfmsc',
'https://warwick.ac.uk/study/postgraduate/courses-2018/asai',
'https://warwick.ac.uk/study/postgraduate/courses-2018/avmc',
'https://warwick.ac.uk/study/postgraduate/courses-2018/aed',
'https://warwick.ac.uk/study/postgraduate/courses-2018/ame',
'https://warwick.ac.uk/study/postgraduate/courses-2018/analyticalscience',
'https://warwick.ac.uk/study/postgraduate/courses-2018/accfin',
'https://warwick.ac.uk/study/postgraduate/courses-2018/als',
'https://warwick.ac.uk/study/postgraduate/courses-2018/writing',
'https://warwick.ac.uk/study/postgraduate/courses-2018/vmcgreece',
'https://warwick.ac.uk/study/postgraduate/courses-2018/vmcrome',
'https://warwick.ac.uk/study/postgraduate/courses-2018/wl',
'https://warwick.ac.uk/study/postgraduate/courses-2018/tus',
'https://warwick.ac.uk/study/postgraduate/courses-2018/usfp',
'https://warwick.ac.uk/study/postgraduate/courses-2018/uia',
'https://warwick.ac.uk/study/postgraduate/courses-2018/translationcultures',
'https://warwick.ac.uk/study/postgraduate/courses-2018/sae',
'https://warwick.ac.uk/study/postgraduate/courses-2018/scp',
'https://warwick.ac.uk/study/postgraduate/courses-2018/set',
'https://warwick.ac.uk/study/postgraduate/courses-2018/sclm',
'https://warwick.ac.uk/study/postgraduate/courses-2018/statistics',
'https://warwick.ac.uk/study/postgraduate/courses-2018/sw',
'https://warwick.ac.uk/study/postgraduate/courses-2018/soc',
'https://warwick.ac.uk/study/postgraduate/courses-2018/sr',
'https://warwick.ac.uk/study/postgraduate/courses-2018/smartcav',
'https://warwick.ac.uk/study/postgraduate/courses-2018/spt',
'https://warwick.ac.uk/study/postgraduate/courses-2018/smd',
'https://warwick.ac.uk/study/postgraduate/courses-2018/mscscientificresearchcommunication',
'https://warwick.ac.uk/study/postgraduate/courses-2018/italian',
'https://warwick.ac.uk/study/postgraduate/courses-2018/cer',
'https://warwick.ac.uk/study/postgraduate/courses-2018/hs',
'https://warwick.ac.uk/study/postgraduate/courses-2018/french',
'https://warwick.ac.uk/study/postgraduate/courses-2018/gs',
'https://warwick.ac.uk/study/postgraduate/courses-2018/rseislamic',
'https://warwick.ac.uk/study/postgraduate/courses-2018/ftsresearch',
'https://warwick.ac.uk/study/postgraduate/courses-2018/pp',
'https://warwick.ac.uk/study/postgraduate/courses-2018/qsr',
'https://warwick.ac.uk/fac/med/study/cpd/phealth/b902/',
'https://warwick.ac.uk/study/postgraduate/courses-2018/pdbqm',
'https://warwick.ac.uk/study/postgraduate/courses-2018/psyedu',
'https://warwick.ac.uk/study/postgraduate/courses-2018/plt',
'https://warwick.ac.uk/study/postgraduate/courses-2018/phil',
'https://warwick.ac.uk/study/postgraduate/courses-2018/philarts',
'https://warwick.ac.uk/study/postgraduate/courses-2018/polymerscience/',
'https://warwick.ac.uk/study/postgraduate/courses-2018/ppm/',
'https://warwick.ac.uk/study/postgraduate/courses-2018/chemistryscientificwriting/',
'https://warwick.ac.uk/study/postgraduate/courses-2018/polymerchemistry',
'https://warwick.ac.uk/study/postgraduate/courses-2018/mh',
'https://warwick.ac.uk/study/postgraduate/courses-2018/mas',
'https://warwick.ac.uk/study/postgraduate/courses-2018/mbbm',
'https://warwick.ac.uk/study/postgraduate/courses-2018/maths',
'https://warwick.ac.uk/study/postgraduate/courses-2018/mos',
'https://warwick.ac.uk/study/postgraduate/courses-2018/mktgstgy',
'https://warwick.ac.uk/study/postgraduate/courses-2018/ms',
'https://warwick.ac.uk/study/postgraduate/courses-2018/mbexc',
'https://warwick.ac.uk/study/postgraduate/courses-2018/msem',
'https://warwick.ac.uk/study/postgraduate/courses-2018/mgmt',
'https://warwick.ac.uk/study/postgraduate/courses-2018/misdi',
'https://warwick.ac.uk/study/postgraduate/courses-2018/lts',
'https://warwick.ac.uk/study/postgraduate/courses-2018/tesol',
'https://warwick.ac.uk/study/postgraduate/courses-2018/itso',
'https://warwick.ac.uk/study/postgraduate/courses-2018/itm',
'https://warwick.ac.uk/study/postgraduate/courses-2018/is',
'https://warwick.ac.uk/study/postgraduate/courses-2018/ipe',
'https://warwick.ac.uk/study/postgraduate/courses-2018/ipea',
'https://warwick.ac.uk/study/postgraduate/courses-2018/ipeurope',
'https://warwick.ac.uk/study/postgraduate/courses-2018/ir',
'https://warwick.ac.uk/study/postgraduate/courses-2018/inteconlaw',
'https://warwick.ac.uk/study/postgraduate/courses-2018/intdev',
'http://www2.warwick.ac.uk/study/postgraduate/courses-2018/idl',
'https://warwick.ac.uk/study/postgraduate/courses-2018/icgfp',
'https://warwick.ac.uk/study/postgraduate/courses-2018/icpm',
'https://warwick.ac.uk/study/postgraduate/courses-2018/ib',
'https://warwick.ac.uk/study/postgraduate/courses-2018/icl',
'https://warwick.ac.uk/study/postgraduate/courses-2018/imaths',
'https://warwick.ac.uk/study/postgraduate/courses-2018/innent',
'https://warwick.ac.uk/study/postgraduate/courses-2018/intcom',
'https://warwick.ac.uk/study/postgraduate/courses-2018/humengsust',
'https://warwick.ac.uk/study/postgraduate/courses-2018/humengman',
'https://warwick.ac.uk/study/postgraduate/courses-2018/humeng',
'https://warwick.ac.uk/study/postgraduate/courses-2018/hom',
'https://warwick.ac.uk/study/postgraduate/courses-2018/humanresource',
'https://warwick.ac.uk/study/postgraduate/courses-2018/gmc',
'https://warwick.ac.uk/study/postgraduate/courses-2018/hopm',
'https://warwick.ac.uk/study/postgraduate/courses-2018/fs',
'https://warwick.ac.uk/study/postgraduate/courses-2018/gintdev',
'https://warwick.ac.uk/study/postgraduate/courses-2018/gch',
'https://warwick.ac.uk/study/postgraduate/courses-2018/geid',
'https://warwick.ac.uk/study/postgraduate/courses-2018/finm',
'https://warwick.ac.uk/study/postgraduate/courses-2018/filmts',
'https://warwick.ac.uk/study/postgraduate/courses-2018/fin',
'https://warwick.ac.uk/study/postgraduate/courses-2018/finecon',
'https://warwick.ac.uk/study/postgraduate/courses-2018/ebcc',
'https://warwick.ac.uk/study/postgraduate/courses-2018/egrs',
'https://warwick.ac.uk/study/postgraduate/courses-2018/englit',
'https://warwick.ac.uk/study/postgraduate/courses-2018/epe',
'https://warwick.ac.uk/study/postgraduate/courses-2018/engbm',
'https://warwick.ac.uk/study/postgraduate/courses-2018/elm',
'https://warwick.ac.uk/study/postgraduate/courses-2018/edus',
'https://warwick.ac.uk/study/postgraduate/courses-2018/emh',
'https://warwick.ac.uk/study/postgraduate/courses-2018/econmres',
'https://warwick.ac.uk/study/postgraduate/courses-2018/econmsc',
'https://warwick.ac.uk/study/postgraduate/courses-2018/eife',
'https://warwick.ac.uk/study/postgraduate/courses-2018/deelt',
'https://warwick.ac.uk/study/postgraduate/courses-2018/ebm',
'https://warwick.ac.uk/study/postgraduate/courses-2018/dst',
'https://warwick.ac.uk/study/postgraduate/courses-2018/dmc',
'https://warwick.ac.uk/study/postgraduate/courses-2018/dte',
'https://warwick.ac.uk/study/postgraduate/courses-2018/da',
'https://warwick.ac.uk/study/postgraduate/courses-2018/dstphd',
'https://warwick.ac.uk/study/postgraduate/courses-2018/csm',
'https://warwick.ac.uk/study/postgraduate/courses-2018/cse',
'https://warwick.ac.uk/study/postgraduate/courses-2018/compscience',
'https://warwick.ac.uk/study/postgraduate/courses-2018/cp',
'https://warwick.ac.uk/study/postgraduate/courses-2018/cme',
'https://warwick.ac.uk/study/postgraduate/courses-2018/cdcs',
'https://warwick.ac.uk/study/postgraduate/courses-2018/chemistryscientificwriting/',
'https://warwick.ac.uk/study/postgraduate/courses-2018/cie',
'https://warwick.ac.uk/study/postgraduate/courses-2018/bm',
'https://warwick.ac.uk/study/postgraduate/courses-2018/bc',
'https://warwick.ac.uk/study/postgraduate/courses-2018/ba',
'https://warwick.ac.uk/study/postgraduate/courses-2018/baf',
'https://warwick.ac.uk/study/undergraduate/courses-2019/accountingandfinance',
'https://warwick.ac.uk/study/undergraduate/courses-2019/accountingandfinancefoundation',
'https://warwick.ac.uk/study/undergraduate/courses-2019/ancienthistoryandclassicalarchaeology',
'https://warwick.ac.uk/study/undergraduate/courses-2019/ancienthistoryandclassicalarchaeologysie',
'https://warwick.ac.uk/study/undergraduate/courses-2019/automotiveengineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/automotiveengineeringmeng',
'http://www2.warwick.ac.uk/study/undergraduate/courses-2019/biochemistry',
'http://www2.warwick.ac.uk/study/undergraduate/courses-2019/biochemistrymbio',
'http://www2.warwick.ac.uk/study/undergraduate/courses-2019/biosciences',
'http://www2.warwick.ac.uk/study/undergraduate/courses-2019/biosciencesmbio',
'http://www2.warwick.ac.uk/study/undergraduate/courses-2019/biomedicalscience',
'http://www2.warwick.ac.uk/study/undergraduate/courses-2019/biomedicalsciencembio',
'https://warwick.ac.uk/study/undergraduate/courses-2019/biomedicalsystemsengineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/biomedicalsystemsengineeringmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/management',
'https://warwick.ac.uk/study/undergraduate/courses-2019/managementfoundation',
'https://warwick.ac.uk/study/undergraduate/courses-2019/internationalbusinesswithfrench',
'https://warwick.ac.uk/study/undergraduate/courses-2019/chemistry',
'https://warwick.ac.uk/study/undergraduate/courses-2019/chemistrymchem',
'https://warwick.ac.uk/study/undergraduate/courses-2019/chemindustrialmchem',
'https://warwick.ac.uk/study/undergraduate/courses-2019/cheminternationalmchem',
'https://warwick.ac.uk/study/undergraduate/courses-2019/chemmedicinalchem',
'https://warwick.ac.uk/study/undergraduate/courses-2019/chemmedicinalmchem',
'https://warwick.ac.uk/study/undergraduate/courses-2019/civilengineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/civilengineeringmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/classicalcivilisation',
'https://warwick.ac.uk/study/undergraduate/courses-2019/classicalcivilisationSIE',
'https://warwick.ac.uk/study/undergraduate/courses-2019/classics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/classicsandenglish',
'https://warwick.ac.uk/study/undergraduate/courses-2019/classicsancientgreek',
'https://warwick.ac.uk/study/undergraduate/courses-2019/classicslatin',
'https://warwick.ac.uk/study/undergraduate/courses-2019/computersciencebusiness',
'https://warwick.ac.uk/study/undergraduate/courses-2019/computerscience',
'https://warwick.ac.uk/study/undergraduate/courses-2019/computersciencemeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/compsyseng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/compsysengmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/cybersecurity',
'https://warwick.ac.uk/study/undergraduate/courses-2019/datascience',
'https://warwick.ac.uk/study/undergraduate/courses-2019/discretemaths',
'https://warwick.ac.uk/study/undergraduate/courses-2019/discretemathsmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/economics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/economicsgsd',
'https://warwick.ac.uk/study/undergraduate/courses-2019/economicsindustrialorg',
'https://warwick.ac.uk/study/undergraduate/courses-2019/economicspoliticsinternational',
'https://warwick.ac.uk/study/undergraduate/courses-2019/educationstudies',
'https://warwick.ac.uk/study/undergraduate/courses-2019/electricalandelectronicengineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/electricalandelectronicengineeringmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/electronicengineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/electronicengineeringmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/engineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/engineeringmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/engineeringbusinessmanagement',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishandfrench',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishandgerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishandhispanicstudies',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishhistory',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishanditalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishlanguagelinguistics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishlit',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishlitcreativewriting',
'https://warwick.ac.uk/study/undergraduate/courses-2019/englishtheatre',
'https://warwick.ac.uk/study/undergraduate/courses-2019/filmandliterature',
'https://warwick.ac.uk/study/undergraduate/courses-2019/filmstudies',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frencheconomics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchandgerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchandhistory',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchanditalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchandlinguistics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchandtheatre',
'https://warwick.ac.uk/study/undergraduate/courses-2019/french',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwitharabic',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwithchinese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwithfilm',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwithgerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwithitalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwithjapanese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwithportuguese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwithrussian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/frenchwithspanish',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanandbusiness',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanandeconomics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanandhistory',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germananditalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanandlinguistics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanandtheatre',
'https://warwick.ac.uk/study/undergraduate/courses-2019/german',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwitharabic',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwithchinese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwithfilm',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwithfrench',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwithitalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwithjapanese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwithPORTUGUESE',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwithrussian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/germanwithspanish',
'https://warwick.ac.uk/study/undergraduate/courses-2019/gsd',
'https://warwick.ac.uk/study/undergraduate/courses-2019/gsdbusiness',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudiesandeconomics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudiesandfrench',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudiesandgerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudiesandhistory',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudiesanditalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudiesandlinguistics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudiesandtheatre',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswitharabic',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswithchinese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswithfilmstudies',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswithfrench',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswithgerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswithitalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswithjapanese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswithportuguese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/hispanicstudieswithrussian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/historyba',
'https://warwick.ac.uk/study/undergraduate/courses-2019/historyanditalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/historygsd',
'https://warwick.ac.uk/study/undergraduate/courses-2019/historyandphilosophy',
'https://warwick.ac.uk/study/undergraduate/courses-2019/historyandpoliticsba',
'https://warwick.ac.uk/study/undergraduate/courses-2019/historyandsociology',
'http://www2.warwick.ac.uk/study/undergraduate/courses-2019/historyofart',
'https://warwick.ac.uk/study/undergraduate/courses-2019/historyofartitalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/internationalbusinesswithgerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/internationalbusinesswithitalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/internationalbusinesswithspanish',
'https://warwick.ac.uk/study/undergraduate/courses-2019/internationalmanagement',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianandclassics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianandeconomics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianhistoryofart',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianandlinguistics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italiantheatre',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianstudies',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianarabic',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianchinese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianfilmstudies',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianfrench',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italiangerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianjapanese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianportuguese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianrussian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/italianspanish',
'https://warwick.ac.uk/study/undergraduate/courses-2019/languageculturecommunication',
'https://warwick.ac.uk/study/undergraduate/courses-2019/law',
'https://warwick.ac.uk/study/undergraduate/courses-2019/law4years',
'https://warwick.ac.uk/study/undergraduate/courses-2019/lawstudyabroadenglish',
'https://warwick.ac.uk/study/undergraduate/courses-2019/lawwithfrenchlaw',
'https://warwick.ac.uk/study/undergraduate/courses-2019/lawwithgermanlaw',
'https://warwick.ac.uk/study/undergraduate/courses-2019/lawbusinessstudies',
'https://warwick.ac.uk/study/undergraduate/courses-2019/lawandsociology',
'https://warwick.ac.uk/study/undergraduate/courses-2019/lawwithhumanities',
'https://warwick.ac.uk/study/undergraduate/courses-2019/lawwithsocialsciences',
'https://warwick.ac.uk/study/undergraduate/courses-2019/liberalarts',
'https://warwick.ac.uk/study/undergraduate/courses-2019/lifesciencesgsd',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswitharabic',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswithchinese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswithfrench',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswithgerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswithitalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswithjapanese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswithportuguese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswithrussian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/linguisticswithspanish',
'https://warwick.ac.uk/study/undergraduate/courses-2019/manufacturingandmechanicalengineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/manufacturingandmechanicalengineeringmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mathsbsc',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mathematicsmmath',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mathematicsandphilosophy',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mathsphysicsbsc',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mmathsphysics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mathsstatsbsc',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mmathstat',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mechanicalengineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mechanicalengineeringmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/modernlang',
'https://warwick.ac.uk/study/undergraduate/courses-2019/modernlanguagesandeconomics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/modernlanguagesandlinguistics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/modernlanguageswithlinguistics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/mmorse',
'https://warwick.ac.uk/study/undergraduate/courses-2019/morse',
'https://warwick.ac.uk/study/undergraduate/courses-2019/philosophy',
'https://warwick.ac.uk/study/undergraduate/courses-2019/philosophygsd',
'https://warwick.ac.uk/study/undergraduate/courses-2019/philosophyliterature',
'https://warwick.ac.uk/study/undergraduate/courses-2019/philosophywithpsychology',
'http://www2.warwick.ac.uk/study/undergraduate/courses-2019/ppe',
'https://warwick.ac.uk/study/undergraduate/courses-2019/physicsbsc',
'https://warwick.ac.uk/study/undergraduate/courses-2019/physicsmphys',
'https://warwick.ac.uk/study/undergraduate/courses-2019/physicsbusiness',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politicsinternational',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politicsinternationalchinese',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politicsinternationalfrench',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politicsinternationalgerman',
'https://warwick.ac.uk/study/undergraduate/courses-2019/paisgsd',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politicsinternationalhispanic',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politicsinternationalitalian',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politicsinternationalstudiesquantitative',
'https://warwick.ac.uk/study/undergraduate/courses-2019/ppl',
'https://warwick.ac.uk/study/undergraduate/courses-2019/politicssociology',
'https://warwick.ac.uk/study/undergraduate/courses-2019/psychology',
'https://warwick.ac.uk/study/undergraduate/courses-2019/psychologyeducation',
'https://warwick.ac.uk/study/undergraduate/courses-2019/paisgsd/psychologygsd',
'https://warwick.ac.uk/study/undergraduate/courses-2019/psychologylinguistics',
'https://warwick.ac.uk/study/undergraduate/courses-2019/sociology',
'https://warwick.ac.uk/study/undergraduate/courses-2019/sociologygsd',
'https://warwick.ac.uk/study/undergraduate/courses-2019/sociologyquantitativemethods',
'https://warwick.ac.uk/study/undergraduate/courses-2019/systemsengineering',
'https://warwick.ac.uk/study/undergraduate/courses-2019/systemsengineeringmeng',
'https://warwick.ac.uk/study/undergraduate/courses-2019/theatrestudies',
'https://warwick.ac.uk/study/undergraduate/courses-2019/theatregsd',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)

    def parse(self, response):
        pass
        #print()
        # print(response.url)
        item = UcasItem()
        university = 'susaikesi123'
        try:
            location = response.xpath('//*[@id="main_content"]/div[2]/div[1]/div/div[1]/div[1]/span').extract()[0]
            location = remove_tags(location)
            #print(location)
        except:
            location = 'N/A'
            #print(location)
        try:
            department = response.xpath('//*[@id="main_content"]/div[2]/div[2]/div[3]/ul/li[4]/ul/li').extract()[0]
            department = remove_tags(department)
            department = department.replace('\n\n', '\n')
            department = department.replace('\r\n', '')
            department = department.replace('	', '')
            #department = department.replace('  ', '')
            department = department.replace('\n', '')
            #department = department.replace('Our Staff', '')
            #print(department)
        except:
            department = ''
            #print(department)


        try:
            degree_name = response.xpath('//*[@id="main_content"]/div[1]/div/div[2]/h1').extract()[0]
            degree_name = remove_tags(degree_name)
            degree_name =re.findall('.*- (.*)',degree_name)[0]

            #degree_name = re.findall('\((.*)\).*',degree_name)[0]
            #degree_name = re.findall('(.*)                    .*',degree_name)[0]
            #degree_name = re.findall('\((.*)\)',degree_name)[0]
            #degree_name = degree_name.replace('\n',degree_name)
            #degree_name = degree_name.replace(' ','')
            #print(degree_name)
        except:
            degree_name = 'N/A'
            #print(degree_name)

        try:
            degree_overview_en = ''
            degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = "<div><p>" + degree_overview_en + "</p></div>"
            #print(degree_overview_en)
        except:
            degree_overview_en = ''

        try:
            programme_en = response.xpath('//*[@id="main"]/div[1]/section[1]/div/div[2]/div/div/h1').extract()[0]
            programme_en = remove_tags(programme_en)
            programme_en = programme_en.replace(degree_name,'')
            #programme_en = programme_en.replace(' - University of Winchester ','')
            #programme_en = programme_en.split()[1]
            #programme_en = re.findall(' (.*)',programme_en)[0]
            #programme_en = programme_en.replace(degree_name,'')
            #programme_en = programme_en.replace('  ','')
            #programme_en = programme_en.replace('\n', '')
            #programme_en = re.findall(('                    '),'')[0]
            #programme_en = re.findall("\(.*\)(.*)",programme_en)[0]
            programme_en = programme_en.replace('\n','')
            programme_en = programme_en.replace('				','')
            programme_en = programme_en.replace(' -','')
            #print(programme_en)
        except:
            programme_en = 'N/A'
            #print(programme_en)

        try:
            overview_en = response.xpath('//*[@id="course-tab-1"]/section/p').extract()[0]
            overview_en = remove_tags(overview_en)
            #overview_en = re.findall('COURSE OVERVIEW(.*)',overview_en)[0]
            overview_en = overview_en.replace('  ','')
            overview_en = overview_en.replace('\n\n','\n')
            overview_en = overview_en.replace('\n\n','')
            overview_en = overview_en.replace('\r\n','')
            #overview_en = overview_en.replace('\n','')
            #overview_en = re.findall('COURSE OVERVIEW(.*)Careers',overview_en)[0]
            overview_en = '<div>' + overview_en + '</div>'

            #overview_en = remove_tags(overview_en)
            #print(overview_en)
        except:
            overview_en = 'N/A'
            #print(overview_en)


        try:
            start_date = '2019-9'



            #print(start_date)
        except:
            start_date = '11'
            #print(start_date)


        try:
            #modules_en = response.xpath('//div[4]/div/div/div[1]/div[5]/div/div[2]/p').extract()[0]
            modules_en = response.xpath('//*[@id="structure"]').extract()[0]
            #modules_en = re.findall('str.replace(/<([a-zA-Z]+)\s*[^><]*>/g,"<$1>")',aa)[0]
            #modules_en = aa.replace(modules_en,'')
            modules_en = remove_tags(modules_en)
            #modules_en = remove_tags(modules_en,keep=('div','p','span','ul','p','li'))
            #modules_en = modules_en.replace(' class="tabs-panel is-active" id="tab-content-year-1"','')
            modules_en = modules_en.replace('  ',' ')
            #modules_en = modules_en.replace('\n\n','')
            #modules_en = modules_en.replace('\n','')
            modules_en = modules_en.replace('\r\n',' ')
            modules_en = '<div><p>' + modules_en + "</p></div>"

            # overview_en = re.findall('COURSE OVERVIEW(.*)',overview_en)[0]
            # modules_en = modules_en.replace('  ', ' ')
            # modules_en = modules_en.replace('\n\n', '\n')
            # modules_en = modules_en.replace('\n\n', '')
            # modules_en = modules_en.replace('\r\n', '')
            # modules_en = modules_en.replace('\n', '')
            #modules_en = re.findall('Year 1(.*)in Year 1', modules_en)[0]

            #modules_en = '<div>' + modules_en + '</div>'
            #print(modules_en)
        except:
            modules_en = 'N/A'
            #print(modules_en)



        try:
            degree_requirements = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[2]/div[2]/div[1]/div[2]').extract()[0]
            degree_requirements = remove_tags(degree_requirements)
            degree_requirements = degree_requirements.replace('  ','')
            #print(degree_requirements)
        except:
            degree_requirements = ''
            #print(degree_requirements)

        try:
            rntry_requirements_en = response.xpath('//*[@id="entry-requirements"]').extract()[0]
            rntry_requirements_en = remove_tags(rntry_requirements_en)
            rntry_requirements_en = re.findall('\d\d',rntry_requirements_en)[0]
            rntry_requirements_en = rntry_requirements_en.replace('\n\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\r\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('  ','')
            #rntry_requirements_en = re.findall('ENTRY REQUIREMENTS(.*)Visit us',rntry_requirements_en)[0]
            #rntry_requirements_en = "<div>"+rntry_requirements_en+"</div>"

            #rntry_requirements_en =rntry_requirements_en.replace('		                        ','')
            if '79' in rntry_requirements_en:
                rntry_requirements_en = '79'

            else:
                rntry_requirements_en = 'N/A'
            #print(rntry_requirements_en)
        except:
            rntry_requirements_en = 'N/A'
            #print(rntry_requirements_en)

        try:
            professional_background = response.xpath('').extract()
            professional_background = remove_tags(professional_background)
        except:
            professional_background = ''

        try:
            require_chinese_en = ''
        except:
            require_chinese_en = ''
        try:
            ielts_desc = response.xpath('//tr[1]/td[2]').extract()[0]
            ielts_desc = remove_tags(ielts_desc)
            #print(ielts_desc)

        except:
            ielts_desc = 'N/A'
            #print(ielts_desc)

        try:
            #ielts = '6.5'
            #ielts =remove_tags(ielts)
            if 'MSc' in degree_name:
                ielts = '7.0'
                ielts_s = '7.0'
                ielts_l = '6.0'
                ielts_r = '6.0'
                ielts_w = '6.0'
                toefl = '95'
                toefl_s = ''
                toefl_l = ''
                toefl_r = 22
                toefl_w = 21
            else:
                toefl = ''
            #ielts =
            #print(ielts)
        except:
            ielts = 0
            #print(ielts)



        try:
            interview_desc_en = response.xpath('//*[@id="entry-requirements-accordion-0"]/div[1]').extract()[0]
            interview_desc_en = remove_tags(interview_desc_en)
            interview_desc_en = interview_desc_en.replace('\n\n', '\n')
            interview_desc_en = interview_desc_en.replace('\r\n', '')
            interview_desc_en = interview_desc_en.replace('	', '')
            interview_desc_en = interview_desc_en.replace('  ', '')
            interview_desc_en = interview_desc_en.replace('\n', '')
            interview_desc_en = "<div>" + interview_desc_en + "</div>"
            #print(interview_desc_en)
        except:
            interview_desc_en = 'N/A'
            #print(interview_desc_en)
        try:
            work_experience_desc_en = response.xpath('').extract()
            work_experience_desc_en = remove_tags(work_experience_desc_en)
        except:
            work_experience_desc_en = ''

        try:
            portfolio_desc_en = response.xpath('').extract()
            portfolio_desc_en = remove_tags(portfolio_desc_en)
        except:
            portfolio_desc_en = ''

        try:
            career_en = response.xpath('//*[@id="tab-Employability"]/div/div[2]/div[2]').extract()[0]
            career_en = remove_tags(career_en)
            career_en = career_en.replace('\r\n','')
            career_en = career_en.replace('  ','')
            career_en = career_en.replace('\n','')
            career_en = "<div><span>" + career_en + "</span></div>"
            print(career_en)
        except:
            career_en = ''
            print(career_en)
        try:
            apply_desc_en = '<p>Undergraduate applicants Applications for full-time undergraduate courses must be made through UCAS Apply. International students can also apply through UCAS with the assistance of one of Kent\'s overseas representatives. See how to apply for undergraduate study. If you are applying for a subject-specific foundation programme, you apply in the same way as for a three-year undergraduate degree. Applications for our International Foundation Programme (IFP) can be made: directly to Kent via the International Foundation Programme site via one of Kent\'s overseas representatives via UCAS. If you are submitting other applications to Kent through UCAS, your IFP application must also be made through UCAS. Important dates Students from the EU are advised to apply by 15 January Students from outside the EU should aim for 15 January to guarantee consideration. However, if places are left, we may consider applications up to 30 June. Late applications A process called \'Clearing\' takes place in July and August, running from 1st July annually. We will provide an updated list all of the Kent degrees that still have places available once Clearing opens – this can give you another chance to apply. For more information on how the Clearing process works and how to apply, please see Clearing at Kent for details. Postgraduate applicants See how to apply for postgraduate study.</p>'
            #apply_desc_en = remove_tags(apply_desc_en)
            #apply_desc_en = "<div>" + apply_desc_en + "</div>"
            #print(apply_desc_en)
        except:
            apply_desc_en = ''

        try:
            apply_documents_en = '<p>For entry to a Kent postgraduate degree programme (Master’s), Chinese students typically need to have completed a Bachelor Degree (Xueshi) at a recognised institution. Exact requirements will depend on the postgraduate degree you are applying for and the undergraduate degree you have studied. For programmes that require a 2:1 we usually ask for a Bachelor degree (Xueshi) from a 211 university with a final grade of 70%. For Bachelor degrees from other recognised institutions you will need to achieve a final grade of 75% For programmes that require a 2:2 we usually ask for a Bachelor degree (Xueshi) from a 211 university with a final grade of 65%. For Bachelor degrees from other recognised institutions you will need to achieve a final grade of 70% Applicants with relevant work experience may be considered with lower grades. Some, but not all, postgraduate programmes require your undergraduate degree to have a related major. Some postgraduate programmes may require work experience in a relevant field or at a certain level.</p>'
            #apply_documents_en = remove_tags(apply_documents_en)
        except:
            apply_documents_en = ''


        apply_fee = 0


        #other = ''
        try:
            apply_proces_en = response.xpath('').extract()
        except:
            apply_proces_en = ''


        try:
            duration = response.xpath('//*[@id="main_content"]/div[2]/div[2]/div[3]/ul/li[3]/ul/li').extract()[0]
            duration = remove_tags(duration)
            #duration = remove_tags(duration)
            #duration = re.findall('(\d) Years',duration)[0]
            if 'One' in duration:
                duration = '1'
            elif '1' in duration:
                duration = '1'
            elif '12' in duration:
                duration = '1'
            elif 'Two' in duration:
                duration = '2'
            elif '2' in duration:
                duration = '2'
            elif '1' in duration:
                duration = '1'
            elif 'two' in duration:
                duration = '2'

            else:
                duration = '1'
            #print(duration)
        except:
            duration = 1
            #print(duration)



        try:
            other = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/a').extract()[0]
            other = remove_tags(other)
            #print('成功'+ other + response.url)
        except:
            other = ''
           #print('失败' + other)

        try:
            ib = response.xpath('//*[@id="tab-Entry_Requirements"]').extract()[0]
            ib = remove_tags(ib)
            ib = re.findall('(\d\d) points overall. ',ib)[0]
            ib = ib + ' points overall. '
            #print(ib)
        except:
            ib = 'N/A'
           # print(ib)

        try:
            alevel = response.xpath('//*[@id="primary-content"]/div[3]/div[1]/div[1]/div[2]/p[1]/span').extract()[0]
            alevel = remove_tags(alevel)
            #alevel = re.findall("(\w\w\w) at A Level",alevel)[0]
            #print(alevel)
        except:
            alevel = 'N/A'
            #print(alevel)
        try:
            ucascode = response.xpath('//*[@id="primary-content"]/div[3]/div[1]/div[2]/ul[1]/li[1]/span').extract()[0]
            ucascode = remove_tags(ucascode)

            #print(ucascode)
        except:
            ucascode = 'N/A'
            #print(ucascode)

        try:
            tuition_fee = response.xpath('//*[@id="fees"]/table/tbody/tr/td[3]').extract()[0]
            # tuition_fee = remove_tags(tuition_fee)
            # tuition_fee = tuition_fee.replace('£','')
            # tuition_fee = tuition_fee.replace(',','')
            # tuition_fee = tuition_fee.replace('*','')
            # tuition_fee = tuition_fee.replace(' ','')
            # tuition_fee = tuition_fee.replace('\r\n','')
            # tuition_fee = tuition_fee.replace('\n','')
            #
            tuition_fee = re.findall('(\d\d\d\d\d)',tuition_fee)[0]

            # tuition_fee = tuition_fee.replace('  ','')
            # tuition_fee = tuition_fee.replace('\n','')
            # tuition_fee = re.findall('Full-time international students: £(.*) paStudents',tuition_fee)[0]
            # tuition_fee = int(tuition_fee)
            #print(tuition_fee)
        except:
            tuition_fee = 0
            #(tuition_fee)

        try:
            assessment_en = response.xpath('//*[@id="detail"]/div/div/div[3]').extract()[0]
            assessment_en = remove_tags(assessment_en)
            assessment_en = assessment_en.replace('\r\n', '')
            assessment_en = assessment_en.replace('  ', '')
            assessment_en = assessment_en.replace('\n', '')
            assessment_en = assessment_en.replace('			','')
            assessment_en = assessment_en.replace('		','')
            #assessment_en = re.findall('Assessment:(.*)Entry Requirements:',assessment_en)[0]
            assessment_en = "<div>"+ assessment_en+"</div>"
            #print(assessment_en)
        except:
            assessment_en = 'N/A'
            #print(assessment_en)

        item["university"] = university
        item["location"] = location
        item["department"] = department
        item["degree_type"] = 1
        item["degree_name"] = degree_name
        #item["degree_overview_en"] = degree_overview_en
        item["programme_en"] = programme_en
        item["overview_en"] = overview_en
        item["teach_time"] = 1
        item["start_date"] = start_date
        item["modules_en"] = modules_en
        item["career_en"] = career_en
        item["application_open_date"] = '9'
        item["deadline"] = '7-31'
        item["apply_pre"] = '£'
        item["apply_fee"] = apply_fee
        #item["rntry_requirements_en"] = rntry_requirements_en
        item["degree_requirements"] = degree_requirements
        item["tuition_fee_pre"] = '£'
        #item["major_requirements"] = rntry_requirements_en
        item["professional_background"] = professional_background
        item["ielts_desc"] = ielts_desc
        item["ielts"] = '6.5'
        item["ielts_l"] = '5.5'
        item["ielts_s"] = '5.5'
        item["ielts_r"] = '6.0'
        item["ielts_w"] = '6.0'
        item["toefl_code"] = '0826'
        item["toefl_desc"] = 'General postgraduate programmes 6.5 overall (with a minimum of 6.0 in R&W; 5.5 in S&L)90 overall (with a minimum of 22 in R; 21 in W; 17 in L; 20 in S)'
        item["toefl_l"] = '17'
        item["toefl"] = '90'
        item["toefl_s"] = '20'
        item["toefl_r"] = '22'
        item["toefl_w"] = '21'
        item["work_experience_desc_en"] = work_experience_desc_en
        item["interview_desc_en"] = interview_desc_en
        item["portfolio_desc_en"] = portfolio_desc_en
        item["apply_desc_en"] = apply_desc_en
        item["apply_documents_en"] = apply_documents_en
        item["other"] = other
        item["url"] = response.url
        item["gatherer"] = 'weihongbo'
        item["apply_proces_en"] = apply_proces_en
        item["batch_number"] = 3
        item["finishing"] = 0
        stime = time.time()
        create_time = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(float(stime)))
        #print(create_time)
        item["create_time"] = create_time
        item["import_status"] = 0
        item["duration"] = duration
        item["tuition_fee"] = tuition_fee
        item["update_time"] = create_time
        item["alevel"] = alevel
        item["ib"] = ''
        item["ucascode"] = ucascode
        item["rntry_requirements"] = rntry_requirements_en
        item["require_chinese_en"] = '<p>For entry to a Kent postgraduate degree programme (Master’s), Chinese students typically need to have completed a Bachelor Degree (Xueshi) at a recognised institution. Exact requirements will depend on the postgraduate degree you are applying for and the undergraduate degree you have studied.  For programmes that require a 2:1 we usually ask for a Bachelor degree (Xueshi) from a 211 university with a final grade of 70%. For Bachelor degrees from other recognised institutions you will need to achieve a final grade of 75%  For programmes that require a 2:2 we usually ask for a Bachelor degree (Xueshi) from a 211 university with a final grade of 65%. For Bachelor degrees from other recognised institutions you will need to achieve a final grade of 70%  Applicants with relevant work experience may be considered with lower grades.  Some, but not all, postgraduate programmes require your undergraduate degree to have a related major. Some postgraduate programmes may require work experience in a relevant field or at a certain level.</p>'
        item["assessment_en"] = assessment_en
        item["teach_time"] = ''
        item["teach_type"] = ''
        #item["require_chinese_en"] = ''
        #item["assessment_en"] = ''
        #item["apply_pre"] = ''
        #yield item


