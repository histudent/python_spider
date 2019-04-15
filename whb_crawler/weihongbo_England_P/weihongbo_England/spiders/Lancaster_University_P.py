import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'Lancaster_University_P'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['http://www.lancaster.ac.uk/study/undergraduate/courses/biomedicine-placement-year-bsc-hons-c708/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biomedicine-bsc-hons-c701/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biomedicine-msci-hons-c703/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biomedical-science-bsc-hons-b990/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biology-with-psychology-bsc-hons-c1c8/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biology-with-psychology-placement-year-bsc-hons-c1c9/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biology-msci-hons-c109/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biology-study-abroad-bsc-hons-c103/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biology-bsc-hons-c101/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biological-sciences-with-biomedicine-bsc-hons-c1b9/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biological-sciences-with-biomedicine-placement-year-bsc-hons-c1b8/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biological-sciences-bsc-hons-c100/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biological-sciences-msci-hons-1m66/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biological-sciences-placement-year-bsc-hons-c104/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biological-sciences-study-abroad-bsc-hons-c102/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biochemistry-with-genetics-bsc-hons-c7c4/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biochemistry-with-genetics-placement-year-bsc-hons-c7c5/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biochemistry-with-biomedicine-bsc-hons-bc79/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biochemistry-with-biomedicine-placement-year-bsc-hons-bc80/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biochemistry-bsc-hons-c700/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biochemistry-study-abroad-bsc-hons-c702/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biochemistry-msci-hons-c706/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biochemistry-placement-year-bsc-hons-c707/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/advertising-and-marketing-ba-hons-n501/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/accounting-finance-and-mathematics-bsc-hons-ng41/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/accounting-and-management-studies-bsc-hons-nn24/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/accounting-finance-and-mathematics-industry-bsc-hons-ng42/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/accounting-and-finance-industry-bsc-hons-n401/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/accounting-and-finance-bsc-hons-n400/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/accounting-and-management-studies-industry-bsc-hons-nn25/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/accounting-and-economics-bsc-hons-nl41/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/accounting-and-economics-industry-bsc-hons-nl42/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/theoretical-physics-with-mathematics-msci-hons-f3g1/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/theoretical-physics-with-mathematics-study-abroad-msci-hons-f3g5/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/theoretical-physics-with-mathematics-bsc-hons-f3gc/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/marketing-with-psychology-bsc-hons-n5c8/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/mathematics-placement-year-bsc-hons-g102/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/mathematics-study-abroad-msci-hons-g103/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/mathematics-bsc-hons-g100/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/mathematics-msci-hons-g101/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/mathematics-and-philosophy-ba-hons-gv15/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/mathematics-with-statistics-placement-year-bsc-hons-gcg3/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/mathematics-with-statistics-study-abroad-msci-hons-g1gh/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/mathematics-with-statistics-bsc-hons-g1g3/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/mathematics-with-statistics-msci-hons-g1gj/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/mathematics-operational-research-statistics-and-economics-morse-industry-bsc-hons-gln1/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/mathematics-operational-research-statistics-and-economics-morse-bsc-hons-gln0/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/mechanical-engineering-beng-hons-h300/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/mechanical-engineering-meng-hons-h303/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/mechatronic-engineering-beng-hons-hh63/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/mechatronic-engineering-meng-hons-hhh6/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/media-and-cultural-studies-placement-year-ba-hons-lp64/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/media-and-cultural-studies-ba-hons-lp63/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/medicine-and-surgery-mbchb-a100/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/medieval-and-renaissance-studies-ba-hons-v125/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/modern-languages-ba-hons-r800/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/modern-languages-and-cultures-mlang-hons-r810/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/natural-sciences-study-abroad-bsc-hons-cfg0/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/natural-sciences-study-abroad-msci-hons-cfg1/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/natural-sciences-bsc-hons-gfc0/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/natural-sciences-msci-hons-fcf3/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/nuclear-engineering-beng-hons-h820/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/nuclear-engineering-meng-hons-h821/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/peace-studies-and-international-relations-ba-hons-ll92/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/philosophy-placement-year-ba-hons-v501/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/philosophy-ba-hons-v500/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/philosophy-and-politics-ba-hons-vl52/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/philosophy-and-religious-studies-ba-hons-vv65/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/philosophy-with-chinese-ba-hons-1a22/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/marketing-and-design-bsc-hons-nw52/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/philosophy-politics-and-economics-placement-year-ba-hons-l0v1/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/marketing-management-bsc-hons-n503/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/philosophy-politics-and-economics-ba-hons-l0v0/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/marketing-management-study-abroad-bsc-hons-n504/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/physical-geography-study-abroad-bsc-hons-f847/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/marketing-bsc-hons-n500/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/physical-geography-study-abroad-msci-hons-4r64/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/management-politics-and-international-relations-industry-bsc-hons-n230/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/physical-geography-bsc-hons-f840/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/marketing-study-abroad-bsc-hons-n502/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/physical-geography-msci-hons-4r63/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/management-and-spanish-studies-ba-hons-rn22/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/physics-study-abroad-mphys-hons-f305/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/management-and-psychology-ba-hons-cn82/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/physics-bsc-hons-f300/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/management-and-sociology-ba-hons-nl23/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/physics-mphys-hons-f303/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/management-and-organisational-behaviour-bsc-hons-n215/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/physics-with-particle-physics-and-cosmology-bsc-hons-f372/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/management-and-organisational-behaviour-study-abroad-bsc-hons-n227/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/physics-with-particle-physics-and-cosmology-mphys-hons-f373/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/management-and-organisational-behaviour-industry-bsc-hons-n228/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/physics-astrophysics-and-cosmology-bsc-hons-f3fm/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/management-and-human-resources-bsc-hons-n600/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/physics-astrophysics-and-cosmology-mphys-hons-f3f5/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/management-and-information-technology-bsc-hons-gn52/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/politics-placement-year-ba-hons-l202/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/management-and-human-resources-study-abroad-bsc-hons-n601/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/politics-study-abroad-ba-hons-l201/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/management-and-human-resources-industry-bsc-hons-n602/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/politics-ba-hons-l200/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/management-and-german-studies-ba-hons-rn41/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/politics-and-international-relations-placement-year-ba-hons-l251/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/management-and-french-studies-ba-hons-rn12/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/politics-and-international-relations-ba-hons-l250/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/linguistics-with-chinese-ba-hons-q1t1/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/politics-and-religious-studies-ba-hons-lv26/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/linguistics-and-psychology-ba-hons-cq81/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/politics-and-sociology-ba-hons-ll23/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/linguistics-and-philosophy-ba-hons-qv15/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/politics-with-chinese-ba-hons-1t33/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/linguistics-ba-hons-q100/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/politics-international-relations-and-management-bsc-hons-ln30/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/linguistics-study-abroad-ba-hons-q102/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/psychology-mpsych-hons-c804/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/law-with-criminology-llb-hons-mm12/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/psychology-study-abroad-ba-hons-c803/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/law-llb-hons-m100/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/psychology-study-abroad-bsc-hons-c801/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/law-study-abroad-llb-hons-m101/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/psychology-ba-hons-c802/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/law-international-law-llb-hons-m102/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/psychology-bsc-hons-c800/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/law-clinical-learning-llb-hons-m103/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/religious-studies-ba-hons-v627/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/international-relations-in-contemporary-china-ba-hons-l260/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/religious-studies-and-sociology-ba-hons-vl63/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/international-relations-and-religious-diversity-ba-hons-6b71/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/religious-studies-with-chinese-ba-hons-1c19/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/international-relations-ba-hons-6t99/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/social-work-ba-hons-l500/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/international-management-bsc-hons-n120/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/social-work-ethics-and-religion-msocial-work-hons-l5v6/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/international-management-in-contemporary-china-ba-hons-l280/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/sociology-placement-year-ba-hons-l301/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/international-management-study-abroad-bsc-hons-n121/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/sociology-ba-hons-l300/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/international-management-industry-bsc-hons-n122/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/software-engineering-with-industrial-experience-msci-hons-g601/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/international-business-management-spain-bba-hons-n2r4/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/software-engineering-bsc-hons-g602/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/international-business-management-mexico-bba-hons-n2r5/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/spanish-studies-ba-hons-r410/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/international-business-management-germany-bba-hons-n2r2/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/spanish-studies-and-computing-bsc-hons-gr44/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/international-business-management-italy-bba-hons-n2r3/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/spanish-studies-and-english-literature-ba-hons-rq43/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/international-business-management-france-bba-hons-n2r1/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/spanish-studies-and-film-ba-hons-r4p3/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/international-business-management-america-bba-hons-n202/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/spanish-studies-and-geography-ba-hons-lr74/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/human-geography-ba-hons-l720/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/spanish-studies-and-history-ba-hons-rv41/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/history-philosophy-and-politics-ba-hons-v0l0/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/spanish-studies-and-linguistics-ba-hons-qr14/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/human-geography-study-abroad-ba-hons-l721/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/spanish-studies-and-mathematics-ba-hons-gr14/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/history-and-religious-studies-ba-hons-vv16/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/spanish-studies-and-philosophy-ba-hons-rv45/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/history-and-politics-ba-hons-lv21/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/history-and-philosophy-ba-hons-vvc5/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/spanish-studies-and-psychology-ba-hons-cr84/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/history-and-international-relations-ba-hons-vl12/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/spanish-studies-and-theatre-ba-hons-wr44/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/history-ba-hons-v100/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/spanish-studies-with-chinese-ba-hons-1t66/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/german-studies-with-italian-ba-hons-r2r3/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/german-studies-with-chinese-ba-hons-1c44/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/sports-and-exercise-science-bsc-hons-c600/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/german-studies-and-theatre-ba-hons-wr42/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/statistics-placement-year-bsc-hons-g302/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/german-studies-and-spanish-studies-ba-hons-rr24/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/statistics-study-abroad-msci-hons-g301/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/german-studies-and-psychology-ba-hons-cr82/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/statistics-bsc-hons-g300/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/german-studies-and-politics-ba-hons-rl22/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/statistics-msci-hons-g303/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/german-studies-and-philosophy-ba-hons-rv25/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/theatre-and-creative-writing-ba-hons-ww48/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/german-studies-and-mathematics-ba-hons-gr12/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/theatre-and-english-literature-placement-year-ba-hons-wq44/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/german-studies-and-linguistics-ba-hons-qr12/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/theatre-and-english-literature-ba-hons-wq43/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/german-studies-and-history-ba-hons-rv21/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/theoretical-physics-bsc-hons-f340/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/german-studies-and-geography-ba-hons-lr72/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/theoretical-physics-mphys-hons-f321/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/german-studies-and-film-ba-hons-r2p3/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/german-studies-and-english-literature-ba-hons-rq23/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/german-studies-and-computing-bsc-hons-gr42/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/german-studies-ba-hons-r220/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/geography-msci-hons-4r61/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/geography-ba-hons-l700/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/geography-bsc-hons-f800/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/geography-marts-hons-l702/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/geography-study-abroad-msci-hons-4r62/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/geography-professional-experience-msci-hons-4r60/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/geography-study-abroad-ba-hons-l701/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/geography-study-abroad-bsc-hons-f802/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/geography-study-abroad-marts-hons-l703/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/french-studies-with-italian-ba-hons-r1r3/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/french-studies-with-chinese-ba-hons-1s62/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/french-studies-and-theatre-ba-hons-wr41/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/french-studies-and-spanish-studies-ba-hons-rr14/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/french-studies-and-psychology-ba-hons-cr81/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/french-studies-and-politics-ba-hons-rl12/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/french-studies-and-philosophy-ba-hons-rv15/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/french-studies-and-mathematics-ba-hons-gr11/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/french-studies-and-linguistics-ba-hons-qr11/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/french-studies-and-history-ba-hons-rv11/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/french-studies-and-german-studies-ba-hons-rr12/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/french-studies-and-geography-ba-hons-lr71/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/french-studies-and-film-ba-hons-r1p3/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/french-studies-and-english-literature-ba-hons-rq13/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/french-studies-and-computing-bsc-hons-gr41/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/french-studies-ba-hons-r120/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/fine-art-and-theatre-ba-hons-ww14/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/fine-art-and-film-ba-hons-wp13/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/fine-art-and-creative-writing-ba-hons-ww18/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/fine-art-placement-year-ba-hons-w101/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/fine-art-ba-hons-w100/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/financial-mathematics-msci-hons-gn1h/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/financial-mathematics-industry-bsc-hons-gn1j/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/financial-mathematics-bsc-hons-gn13/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/finance-and-economics-bsc-hons-nl31/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/finance-bsc-hons-n300/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/finance-and-economics-industry-bsc-hons-nl32/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/film-media-and-cultural-studies-ba-hons-pl36/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/finance-industry-bsc-hons-n301/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/film-media-and-cultural-studies-placement-year-ba-hons-pl37/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/film-and-sociology-ba-hons-pl33/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/film-and-theatre-ba-hons-pw34/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/film-and-sociology-placement-year-ba-hons-pl34/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/film-and-english-literature-ba-hons-pq33/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/film-and-philosophy-ba-hons-pv35/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/film-and-english-literature-placement-year-ba-hons-pq34/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/film-and-creative-writing-ba-hons-pw38/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/ethics-philosophy-and-religion-ba-hons-vv56/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/film-studies-ba-hons-p303/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/environmental-sustainability-in-contemporary-china-ba-hons-l270/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/environmental-science-bsc-hons-f750/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/environmental-science-msci-hons-f850/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/environmental-science-study-abroad-bsc-hons-f754/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/environmental-science-study-abroad-msci-hons-f851/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/entrepreneurship-and-management-bsc-hons-n1n2/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/entrepreneurship-and-management-study-abroad-industry-bsc-hons-n222/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-literature-creative-writing-and-practice-ba-hons-qw38/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-literature-with-creative-writing-ba-hons-q3w8/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-literature-and-philosophy-ba-hons-qv35/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-literature-and-religious-studies-ba-hons-qv36/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-literature-and-linguistics-ba-hons-qq13/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-literature-and-history-ba-hons-qv31/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-literature-ba-hons-q300/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-language-with-chinese-ba-hons-q3t1/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-language-in-the-media-ba-hons-qp33/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-language-in-the-media-study-abroad-ba-hons-qp3h/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-language-and-spanish-studies-ba-hons-qr34/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-language-and-literature-ba-hons-q302/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-language-and-linguistics-ba-hons-qqc3/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-language-and-german-studies-ba-hons-qr32/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-language-and-french-studies-ba-hons-qr31/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-language-and-creative-writing-ba-hons-q3wv/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-language-ba-hons-q304/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/engineering-study-abroad-meng-hons-h104/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/english-language-study-abroad-ba-hons-q310/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/engineering-beng-hons-h100/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/engineering-study-abroad-beng-hons-h101/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/electronic-and-electrical-engineering-beng-hons-h607/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/electronic-and-electrical-engineering-meng-hons-h606/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/economics-and-mathematics-bsc-hons-gl11/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/economics-and-politics-ba-hons-ll21/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/economics-and-mathematics-industry-bsc-hons-gl12/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/economics-and-international-relations-ba-hons-ll12/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/economics-bsc-hons-l100/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/economics-and-geography-ba-hons-ll71/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/economics-study-abroad-bsc-hons-l101/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/economics-industry-bsc-hons-l105/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/ecology-and-conservation-bsc-hons-c180/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/ecology-and-conservation-study-abroad-bsc-hons-c182/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/ecology-and-conservation-professional-experience-msci-hons-0x48/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/earth-and-environmental-science-bsc-hons-ff68/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/earth-and-environmental-science-msci-hons-4r71/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/earth-and-environmental-science-study-abroad-bsc-hons-ff6v/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/drama-theatre-and-performance-ba-hons-w440/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/earth-and-environmental-science-study-abroad-msci-hons-ff86/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/design-ba-hons-w281/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/drama-theatre-and-performance-placement-year-ba-hons-w441/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/criminology-and-sociology-ba-hons-lm39/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/criminology-and-psychology-ba-hons-cl86/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/criminology-and-french-studies-ba-hons-mr91/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/criminology-ba-hons-m930/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/computer-science-and-mathematics-bsc-hons-gg14/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/computer-science-and-mathematics-msci-hons-gg1k/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/computer-science-with-industrial-experience-msci-hons-g404/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/computer-science-bsc-hons-g400/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/computer-science-study-abroad-bsc-hons-g402/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/chemistry-mchem-hons-f101/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/chemistry-bsc-hons-f100/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/chemical-engineering-beng-hons-h800/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/business-management-bsc-hons-n102/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/chemical-engineering-meng-hons-h811/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/business-management-study-abroad-bsc-hons-n103/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/business-management-industry-bsc-hons-n104/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/business-analytics-bsc-hons-n2n1/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/business-economics-industry-bsc-hons-4v11/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/business-analytics-study-abroad-bsc-hons-n1n4/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/business-administration-bba-hons-n200/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/business-analytics-industry-bsc-hons-n1n3/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/business-administration-study-abroad-bba-hons-n201/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/bioscience-with-entrepreneurship-bsc-hons-c1n2/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biomedicine-study-abroad-bsc-hons-c704/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/bioscience-with-entrepreneurship-placement-year-bsc-hons-c1n3/',
'http://www.lancaster.ac.uk/study/undergraduate/courses/biomedicine-study-abroad-msci-c705/']

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'Lancaster University'
        try:
            location = 'Lancaster'
            #location = remove_tags(location)
            #print(location)
        except:
            location = 'N/A'
            #print(location)
        try:
            department = response.xpath('//*[@id="main"]/div[3]/section[1]/div[2]/div/div/div/div[2]/aside/div[2]/div/div/ul/li[1]/a/strong').extract()[0]
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
            degree_name = response.xpath('//*[@id="main"]/div[1]/section[1]/div/div[2]/div/div/h1/span').extract()[0]
            degree_name = remove_tags(degree_name)
            #degree_name =re.findall('.*- (.*)',degree_name)[0]

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
            programme_en = response.xpath('//h1').extract()[0]
            programme_en = remove_tags(programme_en)
            programme_en = programme_en.replace(degree_name,'')
            programme_en = re.findall('(.*)-.*',programme_en)[0]
            #programme_en = programme_en.replace(' - University of Winchester ','')
            #programme_en = programme_en.split()[1]
            #programme_en = re.findall(' (.*)',programme_en)[0]
            #programme_en = programme_en.replace(degree_name,'')
            #programme_en = programme_en.replace('  ','')
            #programme_en = programme_en.replace('\n', '')
            #programme_en = re.findall(('                    '),'')[0]
            #programme_en = re.findall("\(.*\)(.*)",programme_en)[0]
            #programme_en = programme_en.replace('\n','')
            #programme_en = programme_en.replace('				','')
            #programme_en = programme_en.replace(' -','')
            #print(programme_en)
        except:
            programme_en = 'N/A'
            #print(programme_en)

        try:
            overview_en = response.xpath('//*[@id="overview"]').extract()[0]
            overview_en = remove_tags(overview_en)
            #overview_en = re.findall('COURSE OVERVIEW(.*)',overview_en)[0]
            overview_en = overview_en.replace('  ','')
            overview_en = overview_en.replace('\n\n','\n')
            overview_en = overview_en.replace('\n\n','')
            overview_en = overview_en.replace('\r\n','')
            overview_en = overview_en.replace('\n','')
            #overview_en = re.findall('COURSE OVERVIEW(.*)Careers',overview_en)[0]
            overview_en = '<div>' + overview_en + '</div>'

            #overview_en = remove_tags(overview_en)
            #print(overview_en)
        except:
            overview_en = 'N/A'
            #print(overview_en)


        try:
            start_date = response.xpath('//*[@id="main_content"]/div[2]/div[2]/div[3]/ul/li[2]/ul/li').extract()[0]
            start_date = remove_tags(start_date)

            if 'September or January' in start_date:
                start_date = '1,9'
            elif 'September' in start_date:
                start_date = '9'
            elif 'January' in start_date:
                start_date = '9'
            else:
                start_date = '10'
            #print(start_date)
        except:
            start_date = '10'
            #print(start_date)


        try:
            #modules_en = response.xpath('//div[4]/div/div/div[1]/div[5]/div/div[2]/p').extract()[0]
            modules_en = response.xpath('//*[@id="structure"]/div/div').extract()[0]
            modules_en = remove_tags(modules_en)
            # overview_en = re.findall('COURSE OVERVIEW(.*)',overview_en)[0]
            modules_en = modules_en.replace('  ', ' ')
            modules_en = modules_en.replace('\n\n', '\n')
            modules_en = modules_en.replace('\n\n', '')
            modules_en = modules_en.replace('\r\n', '')
            modules_en = modules_en.replace('\n', '')
            #modules_en = re.findall('Year 1(.*)in Year 1', modules_en)[0]
            modules_en = '<div>' + modules_en + '</div>'
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
            rntry_requirements_en = response.xpath('//*[@id="course-key-information"]').extract()[0]
            rntry_requirements_en = remove_tags(rntry_requirements_en)
            rntry_requirements_en = rntry_requirements_en.replace('\n\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\r\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('  ',' ')
            #rntry_requirements_en = re.findall('ENTRY REQUIREMENTS(.*)Visit us',rntry_requirements_en)[0]
            #rntry_requirements_en = "<div>"+rntry_requirements_en+"</div>"

            #rntry_requirements_en =rntry_requirements_en.replace('		                        ','')
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
            ielts_desc = ''
            ielts_desc = remove_tags(ielts_desc)
            #print(ielts_desc)

        except:
            ielts_desc = 'N/A'

            #print(ielts_desc)

        try:
            ielts = rntry_requirements_en
            ielts = re.findall('(\d\.\d)', ielts)[0]
            #ielts =remove_tags(ielts)
            #ielts = re.findall('IELTS(.*)',ielts)[0]
            #ielts = re.findall('(\d\.\d)',ielts)[0]
            #print(ielts)
        except:
            ielts = 0
            #print(ielts)

        try:
            ielts_l = '5.5'
            ielts = re.findall('(\d\.\d)', ielts)[1]
            #print(ielts_l)
            #ielts_l = remove_tags(ielts_l)
        except:
            ielts_l = 0
           #print(ielts_l)

        try:
            ielts_s = ielts_l

        except:
            ielts_s = ielts_l

        try:
            ielts_r = ielts_l
        except:
            ielts_r = ielts_l

        try:
            ielts_w = ielts_l
        except:
            ielts_w = ielts_l

        try:
            toefl_desc = response.xpath('').extract()
            toefl_desc = remove_tags(toefl_desc)
        except:
            toefl_desc = 0

        try:
            toefl = response.xpath('').extract()
            toefl = remove_tags(toefl)

        except:
            toefl = 0

        try:
            toefl_l = response.xpath('').extrcat()
            toefl_l = remove_tags(toefl_l)

        except:
            toefl_l = 0

        try:
            toefl_s = response.xpath('').extract()
            toefl_s = remove_tags(toefl_s)

        except:
            toefl_s = 0

        try:
            toefl_r = response.xpath('').extract()
            toefl_r = remove_tags(toefl_r)
        except:
            toefl_r = 0

        try:
            toefl_w = response.xpath('').extract()
            toefl_w = remove_tags(toefl_w)
        except:
            toefl_w = 0




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
            career_en = response.xpath('//*[@id="careers"]').extract()[0]
            career_en = remove_tags(career_en)
            career_en = career_en.replace('\r\n','')
            career_en = career_en.replace('  ','')
            career_en = career_en.replace('\n','')
            career_en = "<div><span>" + career_en + "</span></div>"
            #print(career_en)
        except:
            career_en = ''
            #print(career_en)
        try:
            apply_desc_en = '<div>You can apply directly to the University for admission to postgraduate taught courses using My Applications website. If your native language is not English you will be asked for a recognised English language qualification. Most postgraduate taught courses start in October.</div>'
            #apply_desc_en = remove_tags(apply_desc_en)
            #apply_desc_en = "<div>" + apply_desc_en + "</div>"
            #print(apply_desc_en)
        except:
            apply_desc_en = ''

        try:
            apply_documents_en = ''
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
            ib = response.xpath('//*[@id="tab-Entry_Requirements"]/div/div[1]/div[1]/table[1]/tbody/tr[11]/td[2]').extract()[0]
            ib = remove_tags(ib)
            #print(ib)
        except:
            ib = ''
            #print(ib)

        try:
            alevel = response.xpath('//*[@id="tab-Entry_Requirements"]/div/div[1]/div/table[1]').extract()[0]
            alevel = remove_tags(alevel)
            alevel = re.findall("(\w\w\w) at A Level",alevel)[0]
            #print(alevel)
        except:
            alevel = 'CC'
            #print(alevel)
        try:
            ucascode = response.xpath('/html/body/div[3]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[2]').extract()[0]
            ucascode = remove_tags(ucascode)

            #print(ucascode)
        except:
            ucascode = ''
            #print(ucascode)

        try:
            tuition_fee = response.xpath('//*[@id="fees"]/div/div/table/tbody/tr[3]/td[1]').extract()[0]
            # tuition_fee = remove_tags(tuition_fee)
            # tuition_fee = tuition_fee.replace('£','')
            tuition_fee = tuition_fee.replace(',','')
            # tuition_fee = tuition_fee.replace('*','')
            # tuition_fee = tuition_fee.replace(' ','')
            # tuition_fee = tuition_fee.replace('\r\n','')
            # tuition_fee = tuition_fee.replace('\n','')
            # #
            tuition_fee = re.findall('(\d\d\d\d\d)',tuition_fee)[0]

            # tuition_fee = tuition_fee.replace('  ','')
            # tuition_fee = tuition_fee.replace('\n','')
            # tuition_fee = re.findall('Full-time international students: £(.*) paStudents',tuition_fee)[0]
            # tuition_fee = int(tuition_fee)
            print(tuition_fee)
        except:
            tuition_fee = 0
            print(tuition_fee)

        try:
            assessment_en = response.xpath('//*[@id="structure"]/section[2]/section[1]').extract()[0]
            assessment_en = remove_tags(assessment_en)
            assessment_en = assessment_en.replace('\r\n', '')
            assessment_en = assessment_en.replace('  ', '')
            assessment_en = assessment_en.replace('\n', '')
            assessment_en = assessment_en.replace('			','')
            assessment_en = assessment_en.replace('		','')
            assessment_en = "<div>"+assessment_en+'</div>'
            #print(assessment_en)
        except:
            assessment_en = 'N/A'
            #print(assessment_en)
        try:
            teach_time = response.xpath('//*[@id="tab-overview1"]/section/div[2]/div').extract()[0]
            teach_time = remove_tags(teach_time)
            if 'full' in teach_time:
                teach_time = 'fulltime'
            elif 'Full' in teach_time:
                teach_time = 'fulltime'
            else:
                teach_time = 'parttime'
            #print(teach_time)
        except:
            teach_time = 'N/A'
            #print(teach_time)

        teach_type = 'taught'

        item["university"] = university
        item["location"] = location
        item["department"] = department
        item["degree_type"] = 2
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
        item["ielts"] = ielts
        item["ielts_l"] = ielts_l
        item["ielts_s"] = ielts_s
        item["ielts_r"] = ielts_r
        item["ielts_w"] = ielts_w
        item["toefl_code"] = ''
        item["toefl_desc"] = toefl_desc
        item["toefl_l"] = toefl_l
        item["toefl"] = toefl
        item["toefl_s"] = toefl_s
        item["toefl_r"] = toefl_r
        item["toefl_w"] = toefl_w
        item["work_experience_desc_en"] = work_experience_desc_en
        item["interview_desc_en"] = interview_desc_en
        item["portfolio_desc_en"] = portfolio_desc_en
        item["apply_desc_en"] = apply_desc_en
        item["apply_documents_en"] = apply_documents_en
        item["other"] = other
        item["url"] = response.url
        item["gatherer"] = 'weihongbo'
        item["apply_proces_en"] = apply_proces_en
        item["batch_number"] = 2
        item["finishing"] = 0
        stime = time.time()
        create_time = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(float(stime)))
        #print(create_time)
        item["create_time"] = create_time
        item["import_status"] = 0
        item["duration"] = duration
        item["tuition_fee"] = tuition_fee
        item["update_time"] = create_time
        #item["alevel"] = alevel
        #item["ib"] = ib
        #item["ucascode"] = ucascode
        item["rntry_requirements"] = rntry_requirements_en
        item["require_chinese_en"] = '<p>For entry to a Kent postgraduate degree programme (Master’s), Chinese students typically need to have completed a Bachelor Degree (Xueshi) at a recognised institution. Exact requirements will depend on the postgraduate degree you are applying for and the undergraduate degree you have studied.  For programmes that require a 2:1 we usually ask for a Bachelor degree (Xueshi) from a 211 university with a final grade of 70%. For Bachelor degrees from other recognised institutions you will need to achieve a final grade of 75%  For programmes that require a 2:2 we usually ask for a Bachelor degree (Xueshi) from a 211 university with a final grade of 65%. For Bachelor degrees from other recognised institutions you will need to achieve a final grade of 70%  Applicants with relevant work experience may be considered with lower grades.  Some, but not all, postgraduate programmes require your undergraduate degree to have a related major. Some postgraduate programmes may require work experience in a relevant field or at a certain level.</p>'
        item["assessment_en"] = assessment_en
        item["teach_time"] = teach_time
        item["teach_type"] = teach_type
        #item["apply_pre"] = ''
        yield item


