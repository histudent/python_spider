import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space, clear_space_str
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getIELTS import get_ielts, get_toefl
from scrapySchool_England_Ben.getTuition_fee import getTuition_fee
import requests
from lxml import etree

class TheUniversityofManchester_USpider(scrapy.Spider):
    name = "TheUniversityofManchester_U"
    start_urls = ["http://www.manchester.ac.uk/study/undergraduate/courses/2019/xml/"]
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    def parse(self, response):
        links = response.xpath("//ul/li//a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))

#         links = ["http://www.manchester.ac.uk/study/undergraduate/courses/2019/11163/ba-politics-and-german/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11534/bsc-educational-psychology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06247/bsc-information-technology-management-for-business-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11784/ba-world-literatures/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00353/ba-politics-and-modern-history/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00230/ba-french-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11793/ba-film-studies-and-history/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/07052/ba-criminology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03858/meng-civil-and-structural-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00216/ba-english-literature-and-a-modern-language-italian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10123/msci-molecular-biology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09673/llb-law-with-criminology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00237/ba-german-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00456/biosciences-with-a-foundation-year/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11785/ba-film-studies-and-arabic/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/12037/ba-american-studies-3-years/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09663/bsc-fashion-marketing/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00612/bsc-molecular-biology-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00608/bsc-microbiology-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06246/bsc-information-technology-management-for-business/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06625/bsc-developmental-biology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00314/ba-italian-and-spanish/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11790/ba-film-studies-and-english-literature/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10110/msci-biochemistry/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03333/beng-aerospace-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09767/bass-social-anthropology-and-quantitative-methods/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10111/msci-biology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10972/bnurs-childrens-nursing/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10292/bsc-immunology-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08165/bsc-biology-with-science-and-society-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10007/ba-english-language-and-arabic/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03520/bsc-management-accounting-and-finance/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/07101/bsc-mathematics-and-statistics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00638/bsc-physics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08846/bass-social-anthropology-and-sociology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00643/bsc-medical-physiology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00091/ba-german-and-portuguese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00499/bsc-mathematics-with-financial-mathematics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00512/bsc-anatomical-sciences-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00257/ba-history-and-french/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00592/bsc-mathematics-and-physics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/12053/msci-master-of-science-cognitive-neuroscience-and-psychology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10352/ba-english-language-and-english-literature/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00531/bsc-biomedical-sciences-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00232/ba-geography/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09672/llb-law/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00078/ba-modern-language-and-business-and-management-russian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11786/ba-film-studies-and-archaeology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00090/ba-french-and-portuguese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09966/bsc-management-human-resources-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03971/msci-optometry/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/07730/ba-modern-language-and-business-and-management-arabic/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03340/beng-chemical-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00485/bsc-biology-with-science-and-society/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/01430/mbchb-medicine-6-years-including-foundation-year/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11787/ba-film-studies-and-chinese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00289/ba-linguistics-and-sociology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10114/msci-biotechnology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03848/meng-chemical-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10355/ba-archaeology-and-history/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03827/meng-aerospace-engineering-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00584/bsc-life-sciences-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00261/ba-history-and-spanish/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00184/ba-classics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00626/bsc-oral-health-science/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00495/bsc-mathematics-with-finance/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00647/bsc-plant-science-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00544/bsc-chemistry/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00088/ba-english-language-and-spanish/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03514/bsc-international-management-with-american-business-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10284/bsc-immunology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00199/ba-drama-and-screen-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00095/ba-history-and-portuguese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00642/bsc-physics-with-theoretical-physics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00675/bsocsc-politics-and-international-relations/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08832/bass-politics-and-criminology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11796/ba-film-studies-and-japanese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00235/ba-german-and-linguistics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03919/meng-mechanical-engineering-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/05134/baecon-economics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10121/msci-medical-biochemistry/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10008/ba-arabic-and-a-modern-european-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11806/ba-american-studies-4-years/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00550/bsc-cognitive-neuroscience-and-psychology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03527/bsc-management-international-business-economics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00341/ba-music-and-drama/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00292/ba-linguistics-and-russian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00526/bsc-biology-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08851/bass-philosophy-and-criminology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08847/bass-sociology-and-philosophy/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11431/mspchlangther-speech-and-language-therapy/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03869/meng-civil-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00595/bsc-mathematics-and-philosophy/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11159/llb-law-with-criminology-and-international-study/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00532/bsc-biomedical-sciences/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00212/ba-english-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03364/beng-electrical-and-electronic-engineering-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00059/ba-english-language-and-chinese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00063/ba-french-and-chinese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00631/bsc-pharmacology-and-physiology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09766/bass-politics-and-quantitative-methods/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09970/bsc-management-marketing-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00560/bsc-computer-science/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00585/bsc-life-sciences/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03928/meng-mechatronic-engineering-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11788/ba-film-studies-and-east-asian-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00590/bsc-mathematics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03390/beng-mechanical-engineering-with-management/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10254/beng-computer-systems-engineering-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00633/bsc-pharmacology-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09631/mpre-master-of-planning-with-real-estate/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00066/ba-italian-and-chinese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03528/bsc-management-marketing/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11795/ba-film-studies-and-italian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00068/ba-portuguese-and-chinese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06627/bsc-developmental-biology-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06751/ba-japanese-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10127/msci-medical-physiology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/12111/mearthsci-earth-and-planetary-sciences-with-year-abroad/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06819/ba-linguistics-and-japanese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09173/ba-english-language-for-education/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00510/bsc-physics-with-philosophy/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00198/ba-drama/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/01443/mchem-chemistry-with-medicinal-chemistry/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00290/ba-linguistics-and-spanish/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11157/ba-politics-and-arabic/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09894/bsc-materials-science-and-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09694/bsc-computer-science-human-computer-interaction/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00607/bsc-microbiology-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00646/bsc-medical-physiology-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00490/bsc-computer-science-and-mathematics-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06245/bsc-biomedical-sciences-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/07102/mmath-mathematics-and-statistics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00103/ba-russian-and-portuguese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06865/ba-chinese-and-japanese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11242/bsc-management-innovation-strategy-and-entrepreneurship-with-industrial---professional-experience-bschons/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06517/bsc-software-engineering-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00104/ba-spanish-and-portuguese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00639/bsc-physics-with-astrophysics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08829/bass-politics-and-sociology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/12106/bsc-earth-and-planetary-sciences/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/05153/baecon-finance/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00259/ba-history-and-italian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10129/msci-zoology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00214/ba-english-literature-and-a-modern-language-french/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00102/ba-modern-language-and-business-and-management-portuguese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09104/bsc-healthcare-science-audiology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09937/bsc-accounting-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08811/baecon-economics-and-philosophy/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/12319/menvsci-menvsci-hons-environmental-science-with-a-year-in-industry/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00519/bsc-biochemistry-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00524/bsc-biology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03850/meng-chemical-engineering-with-study-in-europe/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11546/ba-development-studies-and-social-statistics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10128/msci-plant-science/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00527/bsc-biology-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11801/ba-film-studies-and-russian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10224/bsc-economics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00587/meng-computer-science/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11164/ba-politics-and-italian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10120/msci-genetics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00572/bsc-genetics-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03363/beng-electrical-and-electronic-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00069/ba-russian-and-chinese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09665/bsc-fashion-buying-and-merchandising/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/12322/menvsci-menvsci-hons-environmental-science-with-a-year-abroad/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/12105/bsc-planning-and-real-estate/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06820/ba-modern-language-and-business-and-management-japanese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03343/beng-civil-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10250/bsc-management-sustainable-and-ethical-business-with-industrial---professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00583/bsc-life-sciences-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/02397/musb-music/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08848/bass-sociology-and-criminology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/02029/mphys-physics-with-theoretical-physics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00260/ba-history-and-sociology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00676/bsocsc-social-anthropology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10973/bnurs-mental-health-nursing/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09898/meng-materials-science-and-engineering-with-metallurgy/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10247/bsc-management-sustainable-and-ethical-business/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03389/beng-mechanical-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00268/ba-italian-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11792/ba-film-studies-and-german/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09913/meng-computer-science-human-computer-interaction/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03395/beng-mechatronic-engineering-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10115/msci-cell-biology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10253/beng-computer-systems-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11162/ba-politics-and-french/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00664/bsc-zoology-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06810/ba-french-and-japanese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00558/bsc-computer-science-and-mathematics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/02020/mphys-physics-with-philosophy/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00663/bsc-zoology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10122/msci-microbiology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09896/meng-materials-science-and-engineering-with-biomaterials/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10112/msci-biomedical-sciences/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08587/meng-electronic-engineering-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00616/bsc-neuroscience-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00517/bsc-artificial-intelligence/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10256/meng-computer-systems-engineering-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09224/bsc-international-business-finance-and-economics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09050/meng-chemical-engineering-with-energy-and-environment/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03571/bsc-optometry/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00617/bsc-neuroscience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03519/bsc-management/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03826/meng-aerospace-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10054/ba-history-and-arabic/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00613/bsc-molecular-biology-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00645/bsc-medical-physiology-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08830/bass-politics-and-social-anthropology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08662/bsc-biotechnology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/01450/mchem-chemistry-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/01695/mpharm-pharmacy/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00249/ba-spanish-portuguese-and-latin-american-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/02026/mphys-physics-with-study-in-europe/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/05123/ba-modern-language-and-business-and-management-chinese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00632/bsc-pharmacology-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10229/ba-latin-and-french/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00602/bsc-medical-biochemistry/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00086/ba-english-language-and-portuguese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00075/ba-modern-language-and-business-and-management-french/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09662/bsc-fashion-management/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10971/bnurs-adult-nursing/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00169/ba-ancient-history/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11158/llb-law-with-politics-and-international-study/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11660/bmidwif-midwifery/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11799/ba-film-studies-and-music/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00291/ba-linguistics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03921/meng-mechanical-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00573/bsc-genetics-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11161/ba-politics-and-chinese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09453/mchem-chemistry-with-international-study/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00310/ba-german-and-spanish/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00653/bsc-psychology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03894/meng-electrical-and-electronic-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/05124/meng-software-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00549/bsc-cognitive-neuroscience-and-psychology-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00305/ba-french-and-russian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/05136/baecon-economics-and-finance/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00303/ba-french-and-german/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08208/ba-geography-with-international-study/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10125/msci-pharmacology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00357/ba-russian-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00306/ba-french-and-spanish/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08586/meng-electronic-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00183/ba-classical-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00648/bsc-plant-science/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/07913/ba-history-and-american-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00043/ba-archaeology-and-anthropology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09967/bsc-management-international-business-economics-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00539/bsc-chemistry-with-medicinal-chemistry/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00058/ba-chinese-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00534/bsc-cell-biology-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/07383/bsc-actuarial-science-and-mathematics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03512/bsc-international-management/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00175/ba-archaeology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/12109/mearthsci-earth-and-planetary-sciences-with-year-in-industry/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09768/bass-philosophy-and-quantitative-methods/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11165/ba-politics-and-japanese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/12124/bsc-environmental-science/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00365/ba-religions-and-theology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00533/bsc-cell-biology-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00678/bsocsc-sociology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11797/ba-film-studies-and-linguistics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06814/ba-russian-and-japanese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/12385/bsc-environmental-management/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00615/bsc-neuroscience-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09931/mplan-master-of-planning/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06811/ba-german-and-japanese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00518/bsc-artificial-intelligence-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10356/ba-art-history-and-history/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10116/msci-developmental-biology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00101/ba-linguistics-and-portuguese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/07914/ba-english-literature-and-american-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00308/ba-german-and-italian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/07808/bsc-accounting/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11789/ba-film-studies-and-english-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06818/ba-spanish-and-japanese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08831/bass-philosophy-and-politics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00398/bds-dentistry-first-year-entry/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00571/bsc-genetics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08850/bass-social-anthropology-and-criminology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09248/ba-english-literature-with-creative-writing/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00350/ba-philosophy/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00521/bsc-biochemistry/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00228/ba-french-and-linguistics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08584/beng-electronic-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00071/ba-spanish-and-chinese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00173/ba-arabic-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00597/bsc-mathematics-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09765/bass-sociology-and-quantitative-methods/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00634/bsc-pharmacology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/12107/mearthsci-earth-and-planetary-sciences/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00255/ba-history/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11166/ba-politics-and-portuguese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10255/meng-computer-systems-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10353/ba-ancient-history-and-history/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00309/ba-german-and-russian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11160/ba-criminology-with-international-study/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10063/ba-management-leadership-and-leisure/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00559/bsc-computer-science-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00628/bsc-pharmacology-and-physiology-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09674/llb-law-with-politics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03927/meng-mechatronic-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/05151/baecon-accounting-and-finance/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11156/llb-law-with-international-study/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10124/msci-neuroscience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11547/ba-economics-and-social-statistics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03525/bsc-management-human-resources/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00079/ba-modern-language-and-business-and-management-spanish/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11167/ba-politics-and-russian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00318/ba-russian-and-spanish/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00535/bsc-cell-biology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10113/bsc-international-disaster-management-and-humanitarian-response/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00218/ba-english-literature-and-a-modern-language-spanish/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00575/bsc-geography/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06809/ba-english-language-and-japanese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00178/ba-architecture/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00258/ba-history-and-german/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08507/ba-theological-studies-in-philosophy-and-ethics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00279/ba-latin-and-italian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06613/ba-drama-and-english-literature/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09914/meng-computer-science-human-computer-interaction-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/05130/baecon-development-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03922/meng-mechanical-engineering-with-management/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00304/ba-french-and-italian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00154/ba-politics-philosophy-and-economics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11168/ba-politics-and-spanish/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/01687/mmath-mathematics-with-financial-mathematics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03875/meng-civil-engineering-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00064/ba-german-and-chinese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09627/meng-software-engineering-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/12182/bsc-fashion-technology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09964/bsc-management-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/05139/baecon-economics-and-sociology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00277/ba-latin-and-spanish/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09628/meng-artificial-intelligence-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/01594/meng-artificial-intelligence/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10282/msci-immunology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/05137/baecon-economics-and-politics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09695/bsc-computer-science-human-computer-interaction-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06813/ba-portuguese-and-japanese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/12316/menvsci-menvsci-hons-environmental-science/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00167/ba-ancient-history-and-archaeology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/12152/ba-art-history-and-english-literature/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00087/ba-english-language-and-russian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00077/ba-modern-language-and-business-and-management-italian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00097/ba-italian-and-portuguese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09963/bsc-international-business-finance-and-economics-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00084/ba-english-language-and-german/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00199/ba-drama-and-screen-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00288/ba-linguistics-and-social-anthropology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00340/ba-modern-history-with-economics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09965/bsc-management-accounting-and-finance-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00609/bsc-microbiology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10006/ba-linguistics-and-arabic/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11791/ba-film-studies-and-french/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00278/ba-latin-and-english-literature/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/07958/mpharm-pharmacy-with-a-foundation-year/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11245/bsc-management-innovation-strategy-and-entrepreneurship-bschons/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11798/ba-film-studies-and-middle-eastern-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08209/bsc-geography-with-international-study/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03829/meng-aerospace-engineering-with-management/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11794/ba-film-studies-and-history-of-art/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09769/bass-criminology-and-quantitative-methods/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00275/ba-latin-and-linguistics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11802/ba-film-studies-and-spanish/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06812/ba-italian-and-japanese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09735/ba-east-asian-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03873/meng-civil-engineering-enterprise/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09897/meng-materials-science-and-engineering-with-polymers/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00096/ba-history-and-russian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03849/meng-chemical-engineering-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/07729/ba-middle-eastern-studies/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06817/ba-chinese-and-linguistics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/01684/mmathphys-mathematics-and-physics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03893/meng-electrical-and-electronic-engineering-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00060/ba-english-literature/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00515/bsc-plant-science-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10109/msci-anatomical-sciences/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00267/ba-italian-and-linguistics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08585/beng-electronic-engineering-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10357/ba-english-literature-and-history-3-years/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/03394/beng-mechatronic-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08669/bsc-biotechnology-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09900/meng-materials-science-and-engineering-with-textiles-technology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10291/bsc-immunology-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/02024/mphys-physics-with-astrophysics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00614/bsc-molecular-biology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/10211/ba-religion-and-anthropology/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/01688/mmath-mathematics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/01428/mbchb-medicine/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00215/ba-english-literature-and-a-modern-language-german/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00076/ba-modern-language-and-business-and-management-german/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/01449/mchem-chemistry/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00665/bsc-zoology-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11331/bsc-speech-and-language-therapy/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00520/bsc-biochemistry-with-a-modern-language/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09895/meng-materials-science-and-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00600/bsc-medical-biochemistry-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/11800/ba-film-studies-and-portuguese/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00251/ba-history-of-art/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/06626/bsc-developmental-biology-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09616/meng-computer-science-with-industrial-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00313/ba-italian-and-russian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/02021/mphys-physics/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/05125/bsc-software-engineering/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/09899/meng-materials-science-and-engineering-with-corrosion/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00514/bsc-anatomical-sciences/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00511/bsc-anatomical-sciences-with-industrial-professional-experience/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00085/ba-english-language-and-italian/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/00083/ba-english-language-and-french/all-content/",
# "http://www.manchester.ac.uk/study/undergraduate/courses/2019/08849/bass-social-anthropology-and-philosophy/all-content/", ]
        for link in links:
            url = "http://www.manchester.ac.uk/study/undergraduate/courses/2019/" + link + "all-content/"
            # url = link
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "https://www.manchester.ac.uk/"
        item['university'] = "The University of Manchester"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        item['location'] = "Oxford Rd, Manchester, M13 9PL, UK"
        print("===============================")
        print(response.url)
        try:
            # print(response.url)
            # 专业、学位类型
            programmeDegree = response.xpath("//div[@id='course-profile']/div[@class='heading']/h1//text()").extract()
            clear_space(programmeDegree)
            programmeDegreeStr = ''.join(programmeDegree)
            # print(programmeDegreeStr)
            degree_type = list(re.findall(r"^(\w{0,6})|(\w{0,6}/\w{0,6})\s", programmeDegreeStr)[0])
            # print("degree_type = ", degree_type)
            item['degree_name'] = ''.join(degree_type)
            programme = programmeDegreeStr.split(''.join(degree_type))
            item['programme_en'] = programme[-1].strip()
            print("item['degree_name'] = ", item['degree_name'])
            print("item['programme_en'] = ", item['programme_en'])

            ucascode = response.xpath(
                "//dt[@class='ucas-course-code']/following-sibling::dd[1]//text()").extract()
            clear_space(ucascode)
            if len(ucascode) > 0:
                item['ucascode'] = ''.join(ucascode[0]).strip()
            # print("item['ucascode']: ", item['ucascode'])

            start_date = response.xpath("//*[contains(text(), 'Year of entry:')]//text()").extract()
            item['start_date'] = ''.join(start_date).replace("Year of entry:", "").strip()
            # print("item['start_date'] = ", item['start_date'])

            duration = response.xpath("//div[@id='course-profile']/div[@class='course-profile-content full-page']/div[@class='fact-file']/dl/dd[2]//text()").extract()
            durationStr = ''.join(duration)
            # print("durationStr = ", durationStr)
            duration_re = re.findall(r"([a-zA-Z0-9\.]+\s)(year|month|week|yr|yft){1}|([0-9\.]+)(yr|yft|\-month){1}", durationStr, re.I)
            # print("duration_re = ", duration_re)
            d_dict = {"One": "1",
                      "Two": "2",
                      "Three": "3",
                      "Four": "4",
                      "Five": "5",
                      "Six": "6",
                      "Seven": "7",
                      "Eight": "8",
                      "Nine": "9",
                      "Ten": "10",
                      "one": "1",
                      "two": "2",
                      "three": "3",
                      "four": "4",
                      "five": "5",
                      "six": "6",
                      "seven": "7",
                      "eight": "8",
                      "nine": "9",
                      "ten": "10",
                      }
            if len(duration_re) > 0:
                d_int = re.findall(r"\d+", ''.join(duration_re[0]))
                if len(d_int) > 0:
                    item['duration'] = int(''.join(d_int))
                else:
                    d = re.findall(
                        r"(One)|(Two)|(Three)|(Four)|(Five)|(Six)|(Seven)|(Eight)|(Nine)|(Ten)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(ten)",
                        ', '.join(duration_re[0]))
                    print("d = ", d)
                    item['duration'] = int(d_dict.get(''.join(d[0]).strip()))
                if "y" in ''.join(duration_re[0]) or "Y" in ''.join(duration_re[0]):
                    item['duration_per'] = 1
                elif "m" in ''.join(duration_re[0]) or "M" in ''.join(duration_re[0]):
                    item['duration_per'] = 3
                elif "w" in ''.join(duration_re[0]) or "W" in ''.join(duration_re[0]):
                    item['duration_per'] = 4
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            department = response.xpath(
                "//*[contains(text(), 'Academic department')]/following-sibling::*[1]//text()").extract()
            clear_space(department)
            # print(department)
            if len(department) > 0:
                item['department'] = department[0]
            # print("item['department'] = ", item['department'])

            # 专业描述，雅思托福，就业方向, 学术要求，How To Apply
            overview = response.xpath('//h3[@id="course-overview"]/following-sibling::div[1]').extract()
            overview1 = response.xpath(
                '//h3[@id="course-description"]/following-sibling::div[1]').extract()
            print('===', len(overview1))
            if len(overview1) == 2:
                overview1 = [overview1[0]]
            item['overview_en'] = remove_class(clear_lianxu_space(overview)) + remove_class(
                clear_lianxu_space((overview1)))
            print("item['overview_en'] = ", item['overview_en'])

            # Entry requirements
            rntry_requirements = response.xpath(
                '//h2[@id="entry-requirements"]/following-sibling::*[position()<9]//text()').extract()
            # item['rntry_requirements'] = clear_lianxu_space(rntry_requirements)
            # print("item['rntry_requirements'] = ", item['rntry_requirements'])

            # alevel = response.xpath(
            #     "//h3[@id='a-level']/following-sibling::*[1]//text()").extract()
            alevel = response.xpath(
                "//dt[contains(text(),'Typical A-level offer')]/following-sibling::dd[1]//text()").extract()
            clear_space(alevel)
            # print(alevel)
            # if len(alevel) > 0:
            item['alevel'] = ''.join(alevel).strip()
            print("item['alevel'] = ", item['alevel'])
            # if len(item['alevel']) > 160:
            #     item['alevel'] = ''.join(item['alevel'][:161])
            # print("item['alevel']1 = ", item['alevel'])

            ib = response.xpath(
                "//h3[@id='international-baccalaureate']/following-sibling::*[1]//text()").extract()
            clear_space(ib)
            # if len(ib) > 0:
            item['ib'] = ''.join(ib).strip()

            # if len(item['ib']) > 160:
            #     item['ib'] = ''.join(item['ib'][:161])
            print("item['ib'] = ", item['ib'])

            ielts_toefl_desc = response.xpath(
                "//h3[contains(text(), 'English language')]/following-sibling::div[1]//text()").extract()
            clear_space(ielts_toefl_desc)
            print("ielts_toefl_desc: ", ielts_toefl_desc)

            # ielts_desc = response.xpath("//h3[contains(text(), 'English language')]/following-sibling::div[1]//*[contains(text(), 'IELTS')]//text()").extract()
            # clear_space(ielts_desc)
            # if ''.join(ielts_desc).strip() == "IELTS":
            #     ielts_desc = response.xpath(
            #         "//h3[contains(text(), 'English language')]/following-sibling::div[1]//*[contains(text(), 'IELTS')]/..//text()").extract()

            ielts_desc = re.findall(r"IELTS.{1,80}", ''.join(ielts_toefl_desc))
            toefl_desc = re.findall(r"TOEFL.{1,80}", ''.join(ielts_toefl_desc))

            # toefl_desc = response.xpath("//h3[contains(text(), 'English language')]/following-sibling::div[1]//*[contains(text(), 'TOEFL')]//text()").extract()
            # clear_space(toefl_desc)
            # if ''.join(toefl_desc).strip() == "IBT TOEFL:":
            #     toefl_desc = response.xpath(
            #         "//h3[contains(text(), 'English language')]/following-sibling::div[1]//*[contains(text(), 'TOEFL')]/..//text()").extract()
            item['ielts_desc'] = ' '.join(ielts_desc).strip()
            item['toefl_desc'] = ' '.join(toefl_desc).strip()
            print("item['ielts_desc']: ", item['ielts_desc'])
            print("item['toefl_desc']: ", item['toefl_desc'])

            ielts_list = re.findall(r"\d\.\d|[567]", item['ielts_desc'])# \d[\d\.]{0,2}
            if len(ielts_list) == 1:
                item['ielts'] = ielts_list[0]
                item['ielts_l'] = ielts_list[0]
                item['ielts_s'] = ielts_list[0]
                item['ielts_r'] = ielts_list[0]
                item['ielts_w'] = ielts_list[0]
            elif len(ielts_list) == 2:
                item['ielts'] = ielts_list[0]
                item['ielts_l'] = ielts_list[1]
                item['ielts_s'] = ielts_list[1]
                item['ielts_r'] = ielts_list[1]
                item['ielts_w'] = ielts_list[1]
            elif len(ielts_list) == 3:
                item['ielts'] = ielts_list[0]
                item['ielts_l'] = ielts_list[2]
                item['ielts_s'] = ielts_list[2]
                item['ielts_r'] = ielts_list[2]
                item['ielts_w'] = ielts_list[1]
            print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                    item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            toefl_list = re.findall(r"1[0-1]\d|[12789]\d", item['toefl_desc'])
            print(toefl_list)
            if len(toefl_list) == 1:
                item['toefl'] = toefl_list[0]
                # item['toefl_l'] = toefl_list[0]
                # item['toefl_r'] = toefl_list[0]
                # item['toefl_s'] = toefl_list[0]
                # item['toefl_w'] = toefl_list[0]
            elif len(toefl_list) == 2:
                item['toefl'] = toefl_list[0]
                item['toefl_l'] = toefl_list[1]
                item['toefl_r'] = toefl_list[1]
                item['toefl_s'] = toefl_list[1]
                item['toefl_w'] = toefl_list[1]
            elif len(toefl_list) == 3:
                item['toefl'] = toefl_list[0]
                item['toefl_l'] = toefl_list[2]
                item['toefl_r'] = toefl_list[2]
                item['toefl_s'] = toefl_list[2]
                item['toefl_w'] = toefl_list[1]
            elif len(toefl_list) == 4:
                item['toefl'] = toefl_list[0]
                item['toefl_l'] = toefl_list[1]
                item['toefl_r'] = toefl_list[2]
                item['toefl_s'] = toefl_list[1]
                item['toefl_w'] = toefl_list[3]
            elif len(toefl_list) == 5:
                item['toefl'] = toefl_list[0]
                item['toefl_l'] = toefl_list[1]
                item['toefl_r'] = toefl_list[3]
                item['toefl_s'] = toefl_list[4]
                item['toefl_w'] = toefl_list[2]
            print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
                                        item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))

            apply_proces_en = response.xpath(
                '//h2[@id="application-and-selection"]/following-sibling::*[position()<15]').extract()
            apply_proces_en_str = remove_class(clear_lianxu_space(apply_proces_en))
            # print(apply_proces_en_str.index("<h2>Course details</h2>"))
            if apply_proces_en_str.find("<h2>Course details</h2>") == -1:
                apply_proces_en_s1 = apply_proces_en_str[0:len(apply_proces_en_str)]
            else:
                apply_proces_en_s1 = apply_proces_en_str[:apply_proces_en_str.find("<h2>Course details</h2>")-1]
            item['apply_proces_en'] = apply_proces_en_s1
            # print("item['apply_proces_en'] = ", item['apply_proces_en'])

            interview_desc_en = response.xpath(
                '//h3[contains(text(), "Interview requirements")]/following-sibling::div[1]').extract()
            item['interview_desc_en'] = remove_class(clear_lianxu_space(interview_desc_en))
            # print("item['interview_desc_en'] = ", item['interview_desc_en'])


            assessment_en = response.xpath(
                '//*[@id="teaching-and-learning"]/following-sibling::*[position()<4]').extract()
            if len(assessment_en) == 0:
                assessment_en = response.xpath(
                    '//*[@id="coursework-and-assessment"]/following-sibling::*[position()<4]').extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en'] = ", item['assessment_en'])

            career_en = response.xpath(
                '//*[@id="careers"]/following-sibling::*').extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            # print("item['career_en'] = ", item['career_en'])


            fee1 = response.xpath("//h3[@id='fees']/following-sibling::p[1]//text()").extract()
            # print(fee1)
            fee = clear_lianxu_space(fee1)
            # fee_re = re.findall(r"International\sstudents\s\(per\sannum\):\s£[\d,]+", fee)
            fee_re1 = re.findall(r"£[\d,]+", ''.join(fee))
            # print("fee_re1: ", fee_re1)
            # f = ''.join(fee_re1).replace("£", "").replace(",", "").strip()
            if len(fee_re1) != 0:
                item['tuition_fee'] = getTuition_fee(''.join(fee_re1))
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee'] = ", item['tuition_fee'])
            # print("item['tuition_fee_pre'] = ", item['tuition_fee_pre'])

            modules_url = response.url.replace("all-content", "course-details")
            # print("modules_url: ", modules_url)
            item['modules_en'] = self.parse_modules_en(modules_url)
            print("item['modules_en'] = ", item['modules_en'])

            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<h2 class="flag-title">China <span class="flag-icon china"></span></h2>
    <div class="flag-content"><p>For applicants who have not followed the UK education system, we require three years high school study followed by a recognised <a href="/study/undergraduate/entry-requirements/foundation-year-courses/">UK-based foundation course</a>. In some cases we students may be considered after 1 year in highly ranked Chinese University in lieu of an IFY, this will be considered on a case by case basis based on the institution and content of the first year of study. We also require you to meet our <a href="/study/undergraduate/entry-requirements/language-requirements/">English language requirements</a>. We also accept the NCUK International Foundation Year.</p></div>
"""]))
            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_modules_en(self, modulesUrl):
        data = requests.get(modulesUrl, headers=self.headers)
        response = etree.HTML(data.text)
        modules1 = response.xpath("//h2[@id='course-unit-details']/preceding-sibling::*[1]/following-sibling::*[position()<20]|"
                                  "//h2[@id='course-content-year-1']/preceding-sibling::*[1]/following-sibling::*[position()<20]|"
                                  "//h3[@id='course-units-year-3']/preceding-sibling::*[1]/following-sibling::*[position()<20]")
        m2 = ""
        if len(modules1) > 0:
            for m in modules1:
                m2 += etree.tostring(m, encoding='unicode', pretty_print=False, method='html')
        m2 = remove_class(clear_space_str(m2))
        return m2
