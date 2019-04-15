# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/25 16:09'
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
from scrapySchool_England.TranslateMonth import  translate_month
import urllib.request
class UniversityofAberdeenSpider(scrapy.Spider):
    name = 'UniversityofAberdeen_u'
    allowed_domains = ['abdn.ac.uk/']
    start_urls = []
    C = [
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/432/LV61/anthropology-and-history/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/433/LLP2/anthropology-and-international-relations/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/719/RQ41/hispanic-studies-and-language-linguistics-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/427/LL67/anthropology-and-geography/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/421/LQ63/anthropology-and-english/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/423/LW66/anthropology-and-film-visual-culture/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/434/LV65/anthropology-and-philosophy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/420/LF64/anthropology-and-archaeology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/431/LR64/anthropology-and-hispanic-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/426/LQ65/anthropology-and-gaelic-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/549/L100/economics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/424/RL16/anthropology-and-french/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/534/A201/dentistry/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/425/LR61/anthropology-and-french-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/842/K437/real-estate/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/536/V600/divinity/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/593/Q314/english-and-scottish-literature/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/576/H300/engineering-mechanical/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/616/W690/film-visual-culture/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/573/H620/engineering-electrical-and-electronic/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/834/C802/psychology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/570/H220/engineering-civil-and-environmental/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/428/RL26/anthropology-and-german/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/811/H851/petroleum-engineering/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/595/3500/english-with-creative-writing/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/575/H3H8/engineering-mechanical-with-oil-and-gas-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/419/L600/anthropology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/568/H100/engineering/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/525/G402/computing/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/518/H813/chemical-engineering/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/535/V605/theology-and-religious-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/904/H6H4/engineering-electronic-and-software/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/577/Q300/english/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/574/HH36/engineering-mechanical-and-electrical/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/496/5Q28/celtic-anglo-saxon-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/802/W300/music/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/474/N200/business-management/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/572/H200/engineering-civil/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/532/G405/computing-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/571/H221/engineering-civil-and-structural/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/446/C801/behavioural-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/804/XW13/music-education/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/653/R120/french-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/680/F602/geology-and-petroleum-geology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/652/R101/french-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/681/FF63/geology-and-physics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/783/G102/mathematics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/781/C350/marine-biology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/797/V500/philosophy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/602/C603/exercise-and-health-science/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/805/F301/natural-philosophy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/746/CC71/human-embryology-and-developmental-biology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/832/X120/primary-education/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/600/F900/environmental-science/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/440/G122/applied-mathematics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/803/W390/music-and-communities/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/758/Q190/language-linguistics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/597/F142/environmental-chemistry/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/743/V350/history-of-art/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/782/G100/mathematics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/735/V100/history/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/667/C400/genetics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/442/F421/archaeology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/800/CC74/molecular-biology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/672/L700/geography/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/668/C450/genetics-immunology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/829/L240/politics-and-international-relations/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/849/C600/sports-and-exercise-science/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/705/R220/german-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/749/BC25/immunology-and-pharmacology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/436/LC68/anthropology-and-psychology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/671/F800/geography/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/656/Q530/gaelic-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1183/C605/applied-sports-science/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/711/R410/hispanic-studies-spain-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/852/C300/zoology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/515/7Q1V/celtic-anglo-saxon-studies-and-theology-religious-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/833/C800/psychology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/511/7QV2/celtic-anglo-saxon-studies-and-history-of-art/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/488/GN54/business-management-and-information-systems/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/550/LN13/economics-and-finance/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1115/F610/geoscience/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/526/IW13/computing-and-music/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/418/C349/animal-behaviour/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/516/5LQ2/celtic-anglo-saxon-studies-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/828/CD27/plant-and-soil-science/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/547/LVJ6/sociology-and-theology-religious-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/529/GGK1/computing-science-and-mathematics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/437/LV66/anthropology-and-theology-religious-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/530/IF13/computing-science-and-physics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/579/RQ13/english-and-french/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/826/B120/physiology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/578/QW36/english-and-film-visual-culture/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/798/C500/microbiology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/504/52Q8/celtic-anglo-saxon-studies-and-gaelic-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/673/FF68/geography-and-geoscience/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/503/5R8Q/celtic-anglo-saxon-studies-and-french-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/821/F300/physics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/507/7QR2/celtic-anglo-saxon-studies-and-german-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/812/B210/pharmacology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/580/QR31/english-and-french-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/820/F302/physical-sciences/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1140/L111/financial-economics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/785/FG31/mathematics-and-physics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/551/RL11/economics-and-french/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/839/C8QN/psychology-with-gaelic/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/508/5R29/celtic-anglo-saxon-studies-and-hispanic-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/470/B9B1/biomedical-sciences-physiology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/560/LLC2/economics-and-international-relations/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/809/F111/oil-and-gas-chemistry/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/510/5V1Q/celtic-anglo-saxon-studies-and-history/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/519/F100/chemistry/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/709/T711/hispanic-studies-latin-america-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/806/B170/neuroscience-with-psychology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/559/LV11/economics-and-history/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/836/C8R1/psychology-with-french/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/552/LR11/economics-and-french-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/472/J700/biotechnology-applied-molecular-biology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/561/LM19/economics-and-legal-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/468/B9B2/biomedical-sciences-pharmacology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/558/LR14/economics-and-hispanic-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/787/G1Q5/mathematics-with-gaelic/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/557/RL41/economics-and-hispanic-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/823/F3F6/physics-with-geology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/566/LL13/economics-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/447/C803/behavioural-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/563/LV15/economics-and-philosophy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/445/C859/behavioural-biology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/565/LC18/economics-and-psychology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/748/C552/immunology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/562/LG11/economics-and-mathematics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/825/F3V5/physics-with-philosophy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/556/LR12/economics-and-german-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/459/C901/biological-sciences/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/554/LL17/economics-and-geography/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/840/C8R2/psychology-with-german/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/553/QL51/economics-and-gaelic-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/462/B9BC/biomedical-sciences-anatomy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/564/LL12/economics-and-politics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/460/C100/biology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/490/MN92/business-management-and-legal-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/439/G120/applied-mathematics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/555/RL21/economics-and-german/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/464/B9C1/biomedical-sciences-developmental-biology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/514/7V52/celtic-anglo-saxon-studies-and-philosophy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/466/B9C7/biomedical-sciences-molecular-biology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/491/GN12/business-management-and-mathematics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/527/G400/computing-science/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/492/LN22/business-management-and-politics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/548/D430/ecology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/479/RN12/business-management-and-french-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/456/C700/biochemistry/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/486/NV21/business-management-and-history/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/441/F420/archaeology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/487/GN52/business-management-and-information-systems/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/480/QN52/business-management-and-gaelic-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/581/QQ53/english-and-gaelic-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/502/7Q83/celtic-anglo-saxon-studies-and-french/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/533/C161/conservation-biology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/485/RN42/business-management-and-hispanic-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/851/V612/theology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/482/NR22/business-management-and-german/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/478/NR21/business-management-and-french/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/483/RN22/business-management-and-german-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/786/G1R1/mathematics-with-french/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/481/LN72/business-management-and-geography/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/775/M1W3/law-with-options-in-music/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/498/5V6Q/archaeology-and-celtic-anglo-saxon-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/771/M1L1/law-with-options-in-economics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/477/NN32/business-management-and-finance/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/773/M128/law-with-options-in-gaelic-language/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/443/FV41/archaeology-and-history/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/772/M125/law-with-options-in-french/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/489/LNF2/business-management-and-international-relations/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1165/MT10/law-with-options-in-mandarin-llb/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/501/7PQ9/celtic-anglo-saxon-studies-and-film-visual-culture/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1101/VL51/philosophy-politics-and-economics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/765/M121/law-and-french-law-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/500/7Q5Q/celtic-anglo-saxon-studies-and-english/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/639/MRX1/french-and-legal-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/776/M122/law-with-options-in-spanish/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/494/K438/business-management-and-real-estate/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/640/MR91/french-and-legal-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1146/M1G1/bachelor-of-laws-with-computing-science/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/495/LN32/business-management-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/417/NM49/accountancy-and-legal-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/449/CL13/behavioural-studies-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/774/M124/law-with-options-in-german/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/475/LNC2/business-management-and-economics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/977/M117/law-with-english-law-and-european-legal-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1177/N1R4/mbus-international-business-with-spanish-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/444/FV43/archaeology-and-history-of-art/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/769/M1N4/law-with-options-in-accountancy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/448/CV15/behavioural-studies-and-philosophy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1174/N1Q5/mbus-international-business-with-gaelic-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/767/M126/law-and-spanish-law-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/493/CN28/business-management-and-psychology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/768/M2M1/law-with-english-law/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1145/N125/international-business-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/764/M127/law-and-european-legal-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/476/QN32/business-management-and-english/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/645/RV15/french-and-philosophy-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1176/NT25/mbus-international-business-with-mandarin-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/644/VR51/french-and-philosophy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1173/N1R1/mbus-international-business-with-french-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/762/M114/law/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/438/LL63/anthropology-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/770/M1N2/law-with-options-in-business-management/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/796/A100/medicine-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/643/RG11/french-and-mathematics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1175/N1R2/mbus-international-business-with-german-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/666/QL53/gaelic-studies-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/522/H225/civil-and-structural-engineering-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/665/VQ65/gaelic-studies-and-theology-religious-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/808/F110/oil-and-gas-chemistry-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/766/M123/law-and-german-law-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/567/H605/electrical-and-electronic-engineering-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/649/VR61/french-and-theology-religious-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/528/I101/computing-science-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/664/QL52/gaelic-studies-and-politics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/903/H6H3/engineering-in-electronic-and-software-engineering/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/675/LR74/geography-and-hispanic-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/569/H104/engineering-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/678/LL73/geography-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/524/H229/civil-engineering-with-subsea-technology-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/662/QQ51/gaelic-studies-and-language-linguistics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/517/H810/chemical-engineering/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/674/LR72/geography-and-german/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/810/H850/petroleum-engineering-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/661/QV53/gaelic-studies-and-history-of-art/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/598/F143/environmental-chemistry-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/647/RL12/french-and-politics-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/794/H309/mechanical-engineering-with-subsea-technologies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/660/QV51/gaelic-studies-and-history/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/902/H6H6/electrical-and-electronic-engineering-with-renewable-energy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/650/RLC3/french-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/793/H3N2/mechanical-engineering-with-business-management/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/651/RL13/french-and-sociology-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/792/H305/mechanical-engineering/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/659/QR54/gaelic-studies-and-hispanic-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/523/H205/civil-engineering-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/676/LV71/geography-and-history/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/458/C900/biological-sciences/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/638/RQ11/french-and-language-linguistics-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/465/B9CC/biomedical-sciences-developmental-biology-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/677/LL72/geography-and-international-relations/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/473/J701/biotechnology-applied-molecular-biology-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/632/RV11/french-and-history-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/807/B1C8/neuroscience-with-psychology-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/622/RN43/finance-and-hispanic-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/679/F600/geology-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/646/LR21/french-and-politics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/747/CC7C/human-embryology-and-developmental-biology-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/648/RV16/french-and-theology-religious-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/791/HHH6/mechanical-and-electrical-engineering-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/618/NR31/finance-and-french-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/799/C501/microbiology-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/658/QR52/gaelic-studies-and-german/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/521/H255/civil-and-environmental-engineering-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/605/WR6C/film-visual-culture-and-french-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/463/B9BD/biomedical-sciences-anatomy-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/657/QL57/gaelic-studies-and-geography/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/813/B211/pharmacology-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/586/QV31/english-and-history/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/750/BC2M/immunology-and-pharmacology-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/587/QV33/english-and-history-of-art/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/850/C602/sports-and-exercise-science-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/615/LW36/film-visual-culture-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/467/B9CR/biomedical-sciences-molecular-biology-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/617/RN13/finance-and-french/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/457/C701/biochemistry-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/613/WL62/film-visual-culture-and-international-relations/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/801/CC47/molecular-biology-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/611/WV61/film-visual-culture-and-history/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/827/B121/physiology-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/620/NR32/finance-and-german-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/670/C401/genetics-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/612/WV63/film-visual-culture-and-history-of-art/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/520/F105/chemistry-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/610/WR6K/film-visual-culture-and-hispanic-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/603/C601/exercise-and-health-science-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/623/NLH2/finance-and-international-relations/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/469/B9BF/biomedical-sciences-pharmacology-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/588/QL32/english-and-international-relations/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/531/G401/computing-science-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/594/QL33/english-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/751/C550/immunology-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/608/WR6F/film-visual-culture-and-german-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/669/C451/genetics-immunology-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/614/WV65/film-visual-culture-and-philosophy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/471/B9BA/biomedical-sciences-physiology-with-industrial-placement/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/633/VR31/french-and-history-of-art/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/606/QW56/film-visual-culture-and-gaelic-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/634/RV13/french-and-history-of-art-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/631/VR11/french-and-history/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/635/LRF1/french-and-international-relations/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/592/QVH6/english-and-theology-and-religious-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/585/QR34/english-and-hispanic-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/629/RR12/french-and-german/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/627/QR51/french-and-gaelic-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/624/NK32/finance-and-real-estate/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/589/QQ31/english-and-language-linguistics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/630/RR14/french-and-hispanic-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/604/WR61/film-visual-culture-and-french/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/637/RQC1/french-and-language-linguistics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/591/QV35/english-and-philosophy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/815/VL52/philosophy-and-politics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/814/VF53/philosophy-and-physics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/784/GV15/mathematics-and-philosophy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/755/MLC2/international-relations-and-legal-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/816/VC58/philosophy-and-psychology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/830/LVG6/politics-and-theology-religious-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/636/RLC2/french-and-international-relations-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/779/CM89/legal-studies-and-psychology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/818/VL53/philosophy-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/757/LLF3/international-relations-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/628/LR71/french-and-geography/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/756/VL62/international-relations-and-theology-religious-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/759/QV15/language-linguistics-and-philosophy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/583/QR32/english-and-german-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/778/ML12/legal-studies-and-politics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/817/VV65/philosophy-and-theology-religious-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/745/V1W3/history-with-music-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/777/VM51/legal-studies-and-philosophy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/831/LL23/politics-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/707/R2W3/german-with-music-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/760/QL13/language-linguistics-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/734/R4W3/hispanic-studies-with-music-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/837/C8RC/psychology-with-french/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/841/C8RF/psychology-with-german/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/838/C8QM/psychology-with-gaelic/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1170/NR20/international-business-with-german/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/788/G1Q8/mathematics-with-gaelic/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/654/R1WH/french-with-music-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/655/R1W3/french-with-music-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/754/LQ21/international-relations-and-language-linguistics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1168/NR10/international-business-with-french/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/596/Q3W3/english-with-music-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1171/NT12/international-business-with-mandarin/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/835/LC38/psychology-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/744/VV36/history-of-art-and-theology-religious-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/700/RV26/german-and-theology-religious-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/697/RV25/german-and-philosophy-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1172/NR14/international-business-with-spanish/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1169/NQ15/international-business-with-gaelic/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/712/VR14/hispanic-studies-and-history/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/703/RL23/german-and-sociology-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/702/RLF3/german-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/684/RV21/german-and-history-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/699/RL22/german-and-politics-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/692/MR92/german-and-legal-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/698/LR22/german-and-politics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/687/LRF2/german-and-international-relations/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/695/RG21/german-and-mathematics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/689/RQF1/german-and-language-linguistics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/715/RV43/hispanic-studies-and-history-of-art-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/690/RQ21/german-and-language-linguistics-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/683/VR12/german-and-history/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/713/RV41/hispanic-studies-and-history-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/736/VV13/history-and-history-of-art/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/737/VLC2/history-and-international-relations/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/740/VL12/history-and-politics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/742/VL13/history-and-sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/739/VV15/history-and-philosophy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/741/VV16/history-and-theology-religious-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/732/RL43/hispanic-studies-and-sociology-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/738/VM12/history-and-legal-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/688/RLF2/german-and-international-relations-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/730/VR64/hispanic-studies-and-religious-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/728/RL42/hispanic-studies-and-politics-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/716/LRF4/hispanic-studies-and-international-relations/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/724/RG41/hispanic-studies-and-mathematics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/717/RLK2/hispanic-studies-and-international-relations-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/512/71Q1/celtic-anglo-saxon-studies-and-language-linguistics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/412/NL41/accountancy-and-economics/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/582/RQ23/english-and-german/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/411/NN24/accountancy-and-business-management/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/415/NR42/accountancy-and-german/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1139/N120/international-business-management/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/721/MR94/hispanic-studies-and-legal-studies-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/413/NN34/accountancy-and-finance/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/682/RR24/german-and-hispanic-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/848/L300/sociology/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/414/NR41/accountancy-and-french/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1138/N300/finance/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/847/V210/scottish-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1137/N400/accountancy/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/429/LR62/anthropology-and-german-5-years/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/416/NR44/accountancy-and-hispanic-studies/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/950/C8B9/psychology-with-counselling-skills/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/1060/RR98/european-studies-and-modern-languages/',
        'https://www.abdn.ac.uk/study/undergraduate/degree-programmes/435/LL62/anthropology-and-politics/'
    ]
    for i in C:
        start_urls.append(i)

    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'University of Aberdeen'
        # print(university)

        #2.url
        url = response.url
        # print(response.url)

        #3.programme_en
        programme_en = response.xpath('//*[@id="top"]/div[3]/div/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_tags(programme_en)
        if ',' in programme_en:
            programme_en = re.findall('(.*?),',programme_en)[0]
        else:
            programme_en = programme_en
        # print(programme_en)

        #4.degree_type
        degree_type = 1

        #5.overview_en
        overview_en = response.xpath('//*[@id="overview"]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #6.degree_name
        degree_name= response.xpath('//*[@id="top"]/div[3]/div/h1/sub/abbr').extract()
        degree_name= ''.join(degree_name)
        degree_name = remove_tags(degree_name)
        # print(degree_name)

        #7.ucascode
        ucascode = response.xpath('//*[@id="programme_overview"]/div[2]/div[2]/div[1]/dl/dd[6]').extract()
        ucascode = ''.join(ucascode)
        ucascode = remove_tags(ucascode).strip()
        if'Aberdeen' in ucascode:
            ucascode = response.xpath('//*[@id="programme_overview"]/div[2]/div[2]/div[1]/dl/dd[7]').extract()
            ucascode = ''.join(ucascode)
            ucascode = remove_tags(ucascode).strip()
        # print(ucascode)

        #8.duration
        duration = response.xpath('//*[@id="programme_overview"]/div/div[2]/div[1]/dl/dd[3]').extract()
        duration = ''.join(duration)
        duration = remove_tags(duration)
        duration = clear_space_str(duration)
        # print(duration)
        try:
            duration = re.findall('\d+',duration)[0]
        except:
            duration = None
        # print(duration)

        #9.duration_per
        duration_per = 3

        #10.alevel
        try:
            alevel = response.xpath("//*[contains(text(),'Standard Offer')]|//*[contains(text(),'Standard offer')]").extract()[-1]
            alevel = ''.join(alevel)
            alevel = remove_tags(alevel)
        except:
            alevel = ''
        if len(alevel)==0:
            alevel = response.xpath('//*[@id="entry_requirements"]/section[1]/p[3]/text()[2]').extract()
            if len(alevel)==0:
                alevel = response.xpath("//*[@id='session_y_21']/div/p[1]/text()[2]").extract()
                alevel = ''.join(alevel)
                alevel = remove_tags(alevel)
        # print(alevel)



        #11.start_date
        start_date = '2019-9'
        # print(start_date)

        #12.modules_en
        modules_en = response.xpath('//*[@id="what_you_study"]').extract()

        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # modules_en = clear_space_str(modules_en)

        # print(modules_en)

        #13.assessment_en
        assessment_en =response.xpath("//*[contains(text(),'Assessment Methods')]//following-sibling::*").extract()
        assessment_en = ''.join(assessment_en)
        assessment_en = remove_class(assessment_en)
        assessment_en = clear_space_str(assessment_en)
        # print(assessment_en)

        #14.ib
        try:
            ib = response.xpath("//*[contains(text(),'points') and  contains(text(),'including') and contains(text(),'*')]|//*[contains(text(),'points') and  contains(text(),'including')]").extract()[-1]
            if len(ib)==0:
                ib = response.xpath("//*[contains(text(),'International Baccalaureate')]/../.").extract()

            ib = ''.join(ib)
            ib = remove_tags(ib)
        except:
            ib = ''
        if 'International Baccalaureate' in ib:
            ib = ib.replace('International Baccalaureate','')
        # print(ib,url)

        #15.require_chinese_en
        require_chinese_en = '<p>University Entrance Examination (GAOKAO) Arts and Social Sciences: Students with overall scores of 80% and above in the Senior High School Diploma will be considered for entry.  Alternatively, good scores in the GAOKAO will also beconsidered.Science: Students with overall scores of 80% and above in the Senior High School Diploma will be considered for entry. Students must score 80% or above in two science subjects.  Alternatively, good scores in the GAOKAO will also be considered.Engineering: Students with overall scores of 80% and above in the Senior High School Diploma will be considered for entry. Students must score 80% or above in Maths and Physics science subjects.   Alternatively, good scores in the GAOKAO will also be considered.Law: Students with overall scores of 85% and above in the Senior High School Diploma will be considered for entry. Alternatively, good scores in the GAOKAO will also be considered.</p>'

        #16.ielts 17.18.19.20
        ielts = response.xpath("//*[contains(text(),'IELTS Academic:')]/../following-sibling::*[1]").extract()
        ielts = ''.join(ielts)
        ielts = remove_tags(ielts)
        ielts =clear_space_str(ielts)
        if len(ielts) != 0:
            a = re.findall('\d\.\d',ielts)[0]
            b = re.findall('\d\.\d',ielts)[1]
            c = re.findall('\d\.\d', ielts)[2]
            d = re.findall('\d\.\d', ielts)[3]
            e = re.findall('\d\.\d', ielts)[4]
            ielts = a
            ielts_l = b
            ielts_r = c
            ielts_s = d
            ielts_w = e
        else:
            ielts = 6.0
            ielts_w = 6.0
            ielts_r = 5.5
            ielts_l = 5.5
            ielts_s = 5.5
        # print(ielts,ielts_w,ielts_r,ielts_l,ielts_s)

        #21.toefl 22.23.24.25
        toefl = response.xpath("//*[contains(text(),'TOEFL iBT:')]/../following-sibling::*[1]").extract()
        toefl = ''.join(toefl)
        toefl = remove_tags(toefl)
        toefl = clear_space_str(toefl)
        if len(toefl) !=0:
            a = re.findall('\d+', toefl)[0]
            b = re.findall('\d+', toefl)[1]
            c = re.findall('\d+', toefl)[2]
            d = re.findall('\d+', toefl)[3]
            e = re.findall('\d+', toefl)[4]
            toefl = a
            toefl_l = b
            toefl_r = c
            toefl_s = d
            toefl_w = e
        else:
            toefl = 78
            toefl_l = 17
            toefl_r = 18
            toefl_s = 20
            toefl_w = 21
        # print(toefl,toefl_l,toefl_r,toefl_w,toefl_s)

        #26.career_en
        career_en = response.xpath('//*[@id="careers"]/*').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        career_en = clear_space_str(career_en)
        # print(career_en)

        #27.tuition_fee
        tuition_fee = response.xpath("//*[contains(text(),'                               International Students                                ')]//following-sibling::*").extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = clear_space_str(tuition_fee)
        tuition_fee = remove_class(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #28.tuition_fee_pre
        tuition_fee_pre = '£'

        #29.apply_proces_en
        apply_proces_en = 'https://www.abdn.ac.uk/study/enquire.php'

        #30.location
        location = 'Aberdeen'
        #31.apply_pre
        apply_pre = '£'

        #32.apply_documents_en
        apply_documents_en = '<p>In order to submit the completed application, you must upload the following documents: Your final, official academic transcript/s (if you have not completed your studies yet, please upload a copy of your transcript of studies to date) with an official English translation (if the original language is not English).   A personal statement. We suggest that you prepare the personal statement before you start the online application. The personal statement should be between 250 to 500 words in total and should answer the following three questions: Why have you chosen to apply to the University of Aberdeen to study this subject? Which personal qualities do you possess that will help you to successfully complete this programme of study? How will studying this programme help you when you return home and in your future career? Other documents that may be required but which can be uploaded later include: Degree Certificate For international applicants, document/s to demonstrate your proficiency in English - refer to our English Language requirements page for further information Academic References For Research programmes (PhD) two confidential references. You can uploaded these to your applicant portal or, your referee can send them by e-mail to pgadmissions@abdn.ac.uk. Please ask your referee to include your full name, date of birth, and Applicant Personal ID For Taught programmes (MBA, MSc, MLitt, MRes etc), if you have a first degree from an institution outside the UK, a small number of our degrees may require you to provide one reference. Please refer to the individual programme web page for more details. You can search our degrees here  A Research Proposal should usually be uploaded with applications for PhD and Masters by Research programmes. Some programmes or disciplines require an extended Research Profile, and applicants should refer to individual school websites for details before submitting an application</p>'


        item['ucascode'] = ucascode
        item['ib'] = ib
        item['alevel'] = alevel
        item['apply_documents_en'] =apply_documents_en
        item['apply_pre'] = apply_pre
        item['location'] = location
        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['overview_en'] = overview_en
        item['degree_name'] = degree_name
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['start_date'] = start_date
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['require_chinese_en'] = require_chinese_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['apply_proces_en'] = apply_proces_en
        yield  item