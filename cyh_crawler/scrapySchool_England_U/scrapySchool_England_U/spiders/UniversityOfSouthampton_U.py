# -*- coding: utf-8 -*-
import scrapy
import re
# from scrapySchool_England_U.getItem import get_item1
# from scrapySchool_England_U.getTuition_fee import getTuition_fee
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
# from scrapySchool_England_U.remove_tags import remove_class
# from scrapySchool_England_U.getIELTS import get_ielts, get_toefl
# from scrapySchool_England_U.clearSpace import clear_same_s
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.middlewares import clear_duration
import requests, json
from lxml import etree

class UniversityofsouthamptonUSpider(scrapy.Spider):
    name = 'UniversityOfSouthampton_U'
    allowed_domains = ['southampton.ac.uk']
    start_urls = ['https://www.southampton.ac.uk/courses/undergraduate.page']
    # respon = requests.get(
    #     'https://www.southampton.ac.uk/uni-life/fees-funding/ug-fees-funding/ug-fees/ug-fees-table.page').content
    # respon = etree.HTML(respon)

    def parse(self, response):
        urls=['https://www.southampton.ac.uk/economics/undergraduate/courses/nl41_bsc_accounting_and_economics.page',
'https://www.southampton.ac.uk/business-school/undergraduate/courses/n400-bsc-accounting-finance.page',
'https://www.southampton.ac.uk/business-school/undergraduate/courses/n401-bsc-accounting-and-finance-placement-year-4-years.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/acoustical_engineering/h722_meng_acoustical_engineering.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/acoustical_engineering/h722_meng_acoustical_engineering.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/acoustical_engineering/hw73_bsc_acoustics_with_music.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/aerospace/h422_beng_aeronautics_and_astronautics.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/aerospace/h401_meng_aeronautics_and_astronautics.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/aerospace/h490_meng_aeronautics_and_astronautics_aerodynamics.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/aerospace/h491_meng_aeronautics_and_astronautics_airvehicle_systems_design.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/aerospace/09f4_meng_aeronautics_and_astronautics_computational_engineering_design.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/aerospace/hn42_meng_aeronautics_and_astronautics_engineering_management.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/aerospace/7t32_meng_aeronautics_and_astronautics_materials_and_structures.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/aerospace/39c5_meng_aeronautics_and_astronautics_semester_abroad.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/aerospace/32f4_meng_aeronautics_and_astronautics_semester_in_industry.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/aerospace/h493_meng_aeronautics_and_astronautics_spacecraft_engineering.page',
'https://www.ecs.soton.ac.uk/programmes/meng-aerospace-electronic-engineering',
'https://www.ecs.soton.ac.uk/programmes/beng-aerospace-electronic-engineering',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/history/v102-ba-ancient-history.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/history/v103-ba-ancient-history-and-archaeology.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/history/v1v4-ba-ancient-history-and-archaeology-with-year-abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_french_studies/v105-ba-ancient-history-and-french.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_german_studies/v106-ba-ancient-history-and-german.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/history/v107-ba-ancient-history-and-history.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/history/v1v1-ba-ancient-history-and-history-with-year-abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/v108-ba-ancient-history-and-philosophy.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/history/v1v5-ba-ancient-history-and-philosophy-with-year-abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/v109-ba-ancient-history-and-spanish.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/history/v1v6-ba-ancient-history-with-year-abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_linguistic_studies/q310_ba_applied_english_language_studies.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/archaeology/V400_ba_archaeology.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/archaeology/vv40-msci-archaeology-masters.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/archaeology/F400_bsc_archaeology.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/archaeology/v401_ba_archaeology_with_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/archaeology/f401_bsc_archaeology_with_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/archaeology/v402_ba_archaeology_and_anthropology.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/archaeology/v403_ba_archaeology_and_anthropology_with_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/archaeology/vl47_ba_archaeology_and_geography.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/archaeology/vl48_ba_archaeology_and_geography_with_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/history/vv41_ba_archaeology_and_history.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/history/vv42_ba_archaeology_and_history_with_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/archaeology/v405-march-archaeology-masters.page',
'https://www.phys.soton.ac.uk/programmes/f3fm-mphys-astronomy-year-abroad-4-yrs',
'https://www.southampton.ac.uk/biosci/undergraduate/courses/c701_master_of_biochemistry.page',
'https://www.southampton.ac.uk/biosci/undergraduate/courses/c700_bsc_biochemistry.page',
'https://www.southampton.ac.uk/biosci/undergraduate/courses/c100_bsc_biology.page',
'https://www.southampton.ac.uk/biosci/undergraduate/courses/c101-msci-biology.page',
'https://www.southampton.ac.uk/biosci/undergraduate/courses/7n16_biology_and_marine_biology.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/marine_biology/7n15-bsc-biology-and-marine-biology.page',
'https://www.ecs.soton.ac.uk/programmes/meng-biomedical-electronic-engineering',
'https://www.ecs.soton.ac.uk/programmes/beng-biomedical-electronic-engineering',
'https://www.southampton.ac.uk/biosci/undergraduate/courses/b991_master_of_biomedical_sciences.page',
'https://www.southampton.ac.uk/biosci/undergraduate/courses/b940_bsc_biomedical_sciences.page',
'https://www.southampton.ac.uk/business-school/undergraduate/courses/n100-bsc-business-analytics.page',
'https://www.southampton.ac.uk/business-school/undergraduate/courses/n101-bsc-business-analytics-with-placement-year.page',
'https://www.southampton.ac.uk/business-school/undergraduate/courses/n102-bsc-business-entrepreneurship.page',
'https://www.southampton.ac.uk/business-school/undergraduate/courses/n103-bsc-business-entrepreneurship-with-placement-year.page',
'https://www.southampton.ac.uk/business-school/undergraduate/courses/n202-bsc-business-management.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_french_studies/n1r1-bsc-business-management-and-french.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_german_studies/n1r2-business-management-and-german.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/n1r4-bsc-business-management-and-spanish.page',
'https://www.southampton.ac.uk/business-school/undergraduate/courses/n203-business-management-with-placement-year.page',
'https://www.southampton.ac.uk/chemistry/undergraduate/courses/f100_bsc_chemistry.page',
'https://www.southampton.ac.uk/chemistry/undergraduate/courses/f103_mchem_chemistry.page',
'https://www.southampton.ac.uk/chemistry/undergraduate/courses/fc17_chemistry_and_biochemistry.page',
'https://www.southampton.ac.uk/chemistry/undergraduate/courses/f1gc_mchem_chemistry_maths_combined.page',
'https://www.southampton.ac.uk/chemistry/undergraduate/courses/f1bc_mchem_chemistry_with_medicinal.page',
'https://www.southampton.ac.uk/chemistry/undergraduate/courses/f101_mchem_with_6_month.page',
'https://www.southampton.ac.uk/chemistry/undergraduate/courses/f102-mchem-chemistry-with-a-one-year-placement.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/civil_engineering/4sy8_meng_environmental_engineering.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/civil_engineering/h201_meng_civil_engineering.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/civil_engineering/h200_beng_civil_engineering.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/civil_engineering/hk21_meng_civil_engineering_and_architecture.page',
'https://www.ecs.soton.ac.uk/programmes/bsc-computer-science',
'https://www.ecs.soton.ac.uk/programmes/g401-meng-computer-science-4-yrs',
'https://www.ecs.soton.ac.uk/programmes/g4gr-meng-computer-science-artificial-intelligence-4-yrs',
'https://www.ecs.soton.ac.uk/programmes/meng-computer-science-with-cyber-security',
'https://www.southampton.ac.uk/sociology/undergraduate/courses/l611_bsc_criminology.page',
'https://www.southampton.ac.uk/sociology/undergraduate/courses/lc68_bsc_criminology_and_psychology.page',
'https://www.southampton.ac.uk/biosci/undergraduate/courses/c181-bsc-ecology.page',
'https://www.southampton.ac.uk/biosci/undergraduate/courses/c180_mecol_ecology.page',
'https://www.southampton.ac.uk/economics/undergraduate/courses/l100_bsc_economics.page',
'https://www.southampton.ac.uk/economics/undergraduate/courses/l101_mecon_master_in_economics.page',
'https://www.southampton.ac.uk/economics/undergraduate/courses/l1n3_bsc_economics_and_actuarial_science.page',
'https://www.southampton.ac.uk/economics/undergraduate/courses/l1nh_bsc_economics_and_finance.page',
'https://www.southampton.ac.uk/economics/undergraduate/courses/l112_bsc_economics_and_management_sciences.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/vl51_ba_economics_and_philosophy.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/vl54_ba_economics_and_philosophy_year_abroad.page',
'https://www.southampton.ac.uk/education/undergraduate/courses/x300_bsc_education.page',
'https://www.southampton.ac.uk/education/undergraduate/courses/cx83_bsc_education_and_psychology.page',
'https://www.ecs.soton.ac.uk/programmes/h600-beng-electrical-and-electronic-engineering-3-yrs',
'https://www.ecs.soton.ac.uk/programmes/h602-meng-electrical-and-electronic-engineering',
'https://www.ecs.soton.ac.uk/programmes/beng-electrical-engineering',
'https://www.ecs.soton.ac.uk/programmes/h601-meng-electrical-engineering-4-yrs',
'https://www.ecs.soton.ac.uk/programmes/h603-meng-electronic-engineering-4-yrs',
'https://www.ecs.soton.ac.uk/programmes/h610-beng-electronic-engineering-3-yrs',
'https://www.ecs.soton.ac.uk/programmes/meng-electronic-engineering-artificial-intelligence',
'https://www.ecs.soton.ac.uk/programmes/meng-electronic-engineering-computer-systems',
'https://www.ecs.soton.ac.uk/programmes/h691-meng-electronic-engineering-mobile-and-secure-systems-4-yrs',
'https://www.ecs.soton.ac.uk/programmes/h611-meng-electronic-engineering-nanotechnology',
'https://www.ecs.soton.ac.uk/programmes/h680-meng-electronic-engineering-photonics',
'https://www.ecs.soton.ac.uk/programmes/h641-meng-electronic-engineering-wireless-communications',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/english/q300_ba_english.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/english/q301_ba_english_with_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_french_studies/qr31_ba_english_and_french.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_german_studies/qr32_ba_english_and_german.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/history/qv31_ba_english_and_history.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/english/qv32_ba_english_and_history_with_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/music/qw33_ba_english_and_music.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/english/qw34_ba_english_and_music_with_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/qr34_ba_english_and_spanish.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_english_language_studies/q311-ba-english-language-and-linguistics.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_english_language_studies/qq13-ba-english-language-and-linguistics-with-year-abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/english/q391_ba_english_literature_language_and_linguistics.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/english/q392_ba_english_literature_language_and_linguistics_with_year_abroad.page',
'https://www.southampton.ac.uk/geography/undergraduate/courses/f750-bsc-environmental-management-with-business.page',
'https://www.southampton.ac.uk/geography/undergraduate/courses/f902-menvsci-environmental-sciences.page',
'https://www.southampton.ac.uk/geography/undergraduate/courses/f900-bsc-environmental-sciences.page',
'https://www.southampton.ac.uk/law/undergraduate/courses/m125-llb-european.page',
'https://www.southampton.ac.uk/wsa/undergraduate/courses/wj24_ba_fashion_and_textile_design.page',
'https://www.southampton.ac.uk/wsa/undergraduate/courses/fd23-ba-fashion-design.page',
'https://www.southampton.ac.uk/wsa/undergraduate/courses/wn25_ba_fashion_marketing_management.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/film_studies/qw36_ba_film_and_english.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/film_studies/qw37_ba_film_and_english_with_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_french_studies/rw16_ba_film_and_french.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_german_studies/rw26_ba_film_and_german.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/history/wv61_ba_film_and_history.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/history/wv64_ba_film_and_history_with_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/wv65_ba_film_and_philosophy.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/film_studies/pv35-ba-film-and-philosophy-with-year-abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/wr46_ba_film_and_spanish.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/film_studies/p303_ba_film_studies.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/film_studies/p304_ba_film_studies_with_year_abroad.page',
'https://www.southampton.ac.uk/business-school/undergraduate/courses/f97c-bsc-finance.page',
'https://www.southampton.ac.uk/business-school/undergraduate/courses/f98c-bsc-finance-with-placement-year.page',
'https://www.southampton.ac.uk/wsa/undergraduate/courses/w190_ba_fine_art.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_french_studies/r120_ba_french.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_french_studies/1c72_mlang_french.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_german_studies/rr12_ba_french_and_german.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_german_studies/5xp9_mlang_french_and_german.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_linguistic_studies/rrc2_ba_french_and_german_linguistsic_studies.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_linguistic_studies/31c7_mlang_french_and_german_linguistic_studies.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_french_studies/rv11_ba_french_and_history.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_linguistic_studies/r101_ba_french_linguistic_studies.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_linguistic_studies/5a9v_mlang_french_linguistics_studies.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/music/rw13_ba_french_and_music.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/rv15_ba_french_and_philosophy.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/rr15_ba_french_and_portuguese.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/5f98_mlang_french_and_portuguese.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/rr14_ba_french_and_spanish.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/5y87_mlang_french_and_spanish.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/rrc4_ba_french_and_spanish_linguistic_studies.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/1t67_mlang_french_and_spanish_linguistic_studies.page',
'https://www.southampton.ac.uk/wsa/undergraduate/courses/ba_games_design.page',
'https://www.southampton.ac.uk/geography/undergraduate/courses/l700_ba_geography.page',
'https://www.southampton.ac.uk/geography/undergraduate/courses/f800_bsc_geography.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/geology/f601_msci_geology.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/geology/f600_bsc_geology.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/geology/f6f8_bsc_geology_with_physical_geography.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/geology/f603_msci_geology_with_study_abroad.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/geophysics/f640_bsc_geophysical_sciences.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/geophysics/f660_msci_geophysics.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/geophysics/f662_geophysics_with_foundation_year.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/geophysics/f661_msci_geophysics_with_study_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_german_studies/r220_ba_german.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_german_studies/5r24_mlang_german.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_german_studies/rv21_ba_german_and_history.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_linguistic_studies/r201_ba_german_linguistic_studies.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/5d7h_mlang_german_linguistics_studies.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/music/rw23_ba_german_and_music.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/rv25_ba_german_and_philosophy.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_german_studies/5b75_mlang_german_and_spanish.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_german_studies/rr24_ba_german_and_spanish.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/rrf4_ba_german_and_spanish_linguistic_studies.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_linguistic_studies/1r57_mlang_german_spanish_linguistic_studies.page',
'https://www.southampton.ac.uk/wsa/undergraduate/courses/w210_ba_graphic_arts.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/history/v100_ba_history.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/history/v101_ba_history_with_year_abroad.page',
'https://www.southampton.ac.uk/law/undergraduate/courses/m130-llb-international.page',
'https://www.southampton.ac.uk/politics/undergraduate/courses/l250_bsc-international_relations.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/r900_ba_languages_and_contemporary_european_studies.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/r9q3_ba_languages_and_contemporary_european_studies_english.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/1e45_mlang_languages_and_contemporary_european_studies.page',
'https://www.southampton.ac.uk/law/undergraduate/courses/m200-llb-law-with-psychology.page',
'https://www.southampton.ac.uk/law/undergraduate/courses/m100-llb-bachelor.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_french_studies/nrf1_bsc_management_sciences_and_french.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_german_studies/nr22_bsc_management_sciences_and_german.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/nr24_bsc_management_sciences_and_spanish.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/marine_biology/f703_msci_marine_biology.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/marine_biology/f713-bsc-marine-biolgy.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/oceanography/f7c2-msci-marine-biology-with-oceanography.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/oceanography/f7c1_bsc_marine_biology_with_oceanography.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/marine_biology/f704_msci_marine_biology_with_study_abroad.page',
'https://www.southampton.ac.uk/law/undergraduate/courses/m1m2-llb-maritime.page',
'https://www.southampton.ac.uk/business-school/undergraduate/courses/n501-bsc-marketing.page',
'https://www.southampton.ac.uk/business-school/undergraduate/courses/n500-bsc-marketing-with-placement-year.page',
'https://www.southampton.ac.uk/business-school/undergraduate/courses/n550-bsc-marketing-with-study-abroad.page',
'https://www.southampton.ac.uk/maths/undergraduate/courses/mathematical-physics.page',
'https://www.southampton.ac.uk/maths/undergraduate/courses/g120_mathematical_studies.page',
'https://www.southampton.ac.uk/maths/undergraduate/courses/g103_mmath.page',
'https://www.southampton.ac.uk/maths/undergraduate/courses/g100_mathematics.page',
'https://www.southampton.ac.uk/maths/undergraduate/courses/g1n3_maths_with_actuarial_science.page',
'https://www.southampton.ac.uk/maths/undergraduate/courses/g1g4_maths_with_computer_science.page',
'https://www.southampton.ac.uk/maths/undergraduate/courses/g1nh_maths_with_finance.page',
'https://www.southampton.ac.uk/maths/undergraduate/courses/g1r1_maths_with_french.page',
'https://www.southampton.ac.uk/maths/undergraduate/courses/g1r2_maths_with_german.page',
'https://www.southampton.ac.uk/maths/undergraduate/courses/g1w3_maths_with_music.page',
'https://www.southampton.ac.uk/maths/undergraduate/courses/g1r4_maths_with_spanish.page',
'https://www.southampton.ac.uk/maths/undergraduate/courses/g1g3_maths_with_statistics.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/mechanical_engineering/h300_beng_mechanical_engineering.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/mechanical_engineering/h301_meng_mechanical_engineering.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/mechanical_engineering/4r23_meng_mechanical_engineering_acoustical_engineering.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/mechanical_engineering/hj35_meng_mechanical_engineering_advanced_materials.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/mechanical_engineering/hh34_meng_mechanical_engineering_aerospace.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/mechanical_engineering/h390_meng_mechanical_engineering_automotive.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/mechanical_engineering/4R29_meng_mechanical_engineering_biomedical_engineering.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/mechanical_engineering/5p01_meng_mechanical_engineering_computational_engineering_and_design.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/mechanical_engineering/hn32_meng_mechanical_engineering_engineering_management.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/mechanical_engineering/hh37_meng_mechanical_engineering_mechatronics.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/mechanical_engineering/hh35_meng_mechanical_engineering_naval_engineering.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/mechanical_engineering/hh32_meng_mechanical_engineering_sustainable_energy_systems.page',
'https://www.ecs.soton.ac.uk/programmes/meng-mechatronic-engineering',
'https://www.ecs.soton.ac.uk/programmes/beng-mechatronic-engineering',
'https://www.southampton.ac.uk/medicine/undergraduate/courses/bm4_a101.page',
'https://www.southampton.ac.uk/medicine/undergraduate/courses/bm6_a102.page',
'https://www.southampton.ac.uk/medicine/undergraduate/courses/bm5_a100.page',
'https://www.southampton.ac.uk/maths/undergraduate/courses/mmorse.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/history/vl12_ba_modern_history_and_politics.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/history/vl13-ba-modern-history-and-politics-year-abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/r990_ba_modern_languages.page',
'https://www.southampton.ac.uk/maths/undergraduate/courses/gl12_morse.page',
'https://www.phys.soton.ac.uk/programmes/f3fm-mphys-astronomy-4-yrs',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/music/w300_ba_music.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/music/w301_ba_music_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/music/w3n1-ba-music-business-management.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/music/wn31-ba-music-and-business-management-year-abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/music/wb32_ba_music_and_management_sciences.page',
'https://www.southampton.ac.uk/natsci/find_course/msci_natural_sciences.page',
'https://www.southampton.ac.uk/biosci/undergraduate/courses/master-of-neuroscience.page',
'https://www.southampton.ac.uk/healthsciences/undergraduate/courses/mn-nursing-adult-child.page',
'https://www.southampton.ac.uk/healthsciences/undergraduate/courses/mn-nursing-adult-mental-health.page',
'https://www.southampton.ac.uk/healthsciences/undergraduate/courses/mn-nursing-child-mental-health.page',
'https://www.southampton.ac.uk/healthsciences/undergraduate/courses/bsc-nursing-adult-2019.page',
'https://www.southampton.ac.uk/healthsciences/undergraduate/courses/bn-nursing-child-mental-health.page',
'https://www.southampton.ac.uk/healthsciences/undergraduate/courses/bsc-nursing-child-2019.page',
'https://www.southampton.ac.uk/healthsciences/undergraduate/courses/bsc-nursing-mental-health-2019.page',
'https://www.southampton.ac.uk/healthsciences/undergraduate/courses/bsc_occupational_therapy.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/oceanography/f700_msci_oceanography.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/oceanography/f710_bsc_oceanography_single_honours.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/oceanography/f7r1_msci_oceanography_with_french.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/oceanography/f7f8_bsc_oceanography_with_physical_geography.page',
'https://www.southampton.ac.uk/oes/undergraduate/courses/oceanography/f702_msci_oceanography_with_study_abroad.page',
'https://www.phys.soton.ac.uk/programmes/f303-mphys-particle-physics-4-yrs',
'https://www.southampton.ac.uk/biosci/undergraduate/courses/b210_bsc_pharmacology.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/v500_ba_philosophy.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/v501_ba_philosophy_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/qv35-ba-philosophy-and-english.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/qv36_ba_philosophy_and_english_with_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/vv51_ba_philosophy_and_history.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/vv52_ba_philosophy_and_history_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/vg51_philosophy_and_mathematics.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/vg52_ba_philosophy_and_mathematics_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/vw53_philosophy_and_music.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/vw54_ba_philosophy_and_music_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/vl52_philosophy_and_politics.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/vl54_ba_philosophy_and_politics_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/vl53_philosophy_and_sociology.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/vl36_ba_philosophy_and_sociology_year_abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/v504-ba-philosophy-ethics-and-religion.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/vv56-ba-philosophy-ethics-and-religion-year-abroad.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/philosophy/v5l2-ba-philosophy-politics-and-economics-with-year-abroad.page',
'https://www.phys.soton.ac.uk/programmes/f300-bsc-physics-3-yrs',
'https://www.phys.soton.ac.uk/programmes/f303-mphys-physics-4-yrs',
'https://www.phys.soton.ac.uk/programmes/f303-mphys-physics-year-experimental-research-4-yrs',
'https://www.phys.soton.ac.uk/programmes/F303-mphys-physics-with-industrial-placement',
'https://www.phys.soton.ac.uk/programmes/f3gc-mphys-physics-mathematics-4-yrs',
'https://www.phys.soton.ac.uk/programmes/f390-mphys-physics-nanotechnology',
'https://www.phys.soton.ac.uk/programmes/f369-mphys-physics-photonics-4-yrs',
'https://www.phys.soton.ac.uk/programmes/f3fx-mphys-physics-space-science-4-yrs',
'https://www.southampton.ac.uk/healthsciences/undergraduate/courses/bsc_physiotherapy.page',
'https://www.southampton.ac.uk/healthsciences/undergraduate/courses/bsc_podiatry.page',
'https://www.southampton.ac.uk/politics/undergraduate/courses/l200_bsc-politics.page',
'https://www.southampton.ac.uk/politics/undergraduate/courses/ll12_bsc_politics_and_economics.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_french_studies/lr21_ba_politics_and_french.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_german_studies/lr22_ba_politics_and_german.page',
'https://www.southampton.ac.uk/politics/undergraduate/courses/l260_bsc_politics_and_international_relations.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/rl42_ba_politics_and_spanish.page',
'https://www.southampton.ac.uk/demography/undergraduate/courses/l701_bsc_population_and_geography.page',
'https://www.southampton.ac.uk/psychology/undergraduate/courses/c800_bsc_psychology.page',
'https://www.southampton.ac.uk/psychology/undergraduate/courses/c801-bsc-psychology-with-law.page',
'https://www.southampton.ac.uk/demography/undergraduate/courses/l90b-bsc-quantitative-social-science.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/maritime_engineering/j641_meng_ship_science.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/maritime_engineering/j640_beng_ship_science.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/maritime_engineering/j644_meng_ship_science_advanced_materials.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/maritime_engineering/jn62_meng_ship_science_engineering_management.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/maritime_engineering/j642_meng_ship_science_naval_architecture.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/maritime_engineering/h500_meng_ship_science_naval_engineering.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/maritime_engineering/3s28_meng_ship_science_offshore_engineering.page',
'https://www.southampton.ac.uk/engineering/undergraduate/courses/maritime_engineering/j643_meng_ship_science_yacht_and_small_craft.page',
'https://www.southampton.ac.uk/sociology/undergraduate/courses/ll64_bsc_social_policy_and_criminology.page',
'https://www.southampton.ac.uk/sociology/undergraduate/courses/l300_bsc_sociology.page',
'https://www.southampton.ac.uk/sociology/undergraduate/courses/ll63_bsc_sociology_and_criminology.page',
'https://www.southampton.ac.uk/sociology/undergraduate/courses/ll34_bsc_sociology_and_social_policy.page',
'https://www.southampton.ac.uk/sociology/undergraduate/courses/l3l6_bsc_sociology_with_anthropology.page',
'https://www.ecs.soton.ac.uk/programmes/g4g6-beng-software-engineering',
'https://www.ecs.soton.ac.uk/programmes/g600-meng-software-engineering-4-yrs',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/r400_ba_spanish.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/5t2a_mlang_spanish.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/rtk7_ba_spanish_latin_american_studies.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/rv41_ba_spanish_and_history.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/1g1s_mlang_spanish_and_latin_american_studies.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/r401_ba_spanish_linguistic_studies.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/1b6s_mlang_spanish_linguistic_studies.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/1jt6_mlang_spanish_and_portuguese.page',
'https://www.southampton.ac.uk/humanities/undergraduate/courses/modern_languages_spanish_portuguese_latin_american_studies/rr45_ba_spanish_and_portuguese_studies.page',
'https://www.southampton.ac.uk/wsa/undergraduate/courses/td23-ba-textile-design.page',
'https://www.southampton.ac.uk/biosci/undergraduate/courses/c300_bsc_zoology.page',
'https://www.southampton.ac.uk/biosci/undergraduate/courses/c301-msci-zoology.page',]
        for u in urls:
            yield scrapy.Request(url=u,callback=self.parsess,meta={'url':u})
    #补抓
    def parsess(self,response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.meta['url']
        item['university']='University of Southampton'
        print(response.url)
        alevel = response.xpath(
            "//td[contains(text(),'GCE A-level')]/following-sibling::td/p[position()<=4]//text()").extract()
        if alevel == []:
            alevel = response.xpath('//td[contains(text(),"evel")]/..//text()').extract()
        if alevel == []:
            alevel = response.xpath('//h5[contains(text(),"evel")]/following-sibling::*[1]//text()').extract()
        if alevel == []:
            alevel = response.xpath('//h4[contains(text(),"evel")]/following-sibling::*[1]//text()').extract()
        alevel = remove_class(alevel)
        # print(alevel)
        item['alevel']=alevel
        ib = response.xpath(
            "//td[contains(text(),'International Baccalaureate')]/following-sibling::td//text()").extract()
        if ib == []:
            ib = response.xpath('//*[contains(text(),"IB:")]/following-sibling::*[1]//text()').extract()
        if ib==[]:
            ib='Between 28 and 38 points '
        ib = remove_class(ib)
        item['ib'] = ib.strip()
        yield item
    def parses(self,response):
        # print(response.url)
        item = get_item1(ScrapyschoolEnglandItem)
        item['university'] = "University of Southampton"
        item['url'] = response.url
        item['location'] = 'Southampton'
        programme=response.xpath('//h1[@class="uos-page-title uos-main-title"]/text()|//h1[@class="uos-page-title uos-main-title uos-sighted"]/text()|//h1[@class="uos-page-title uos-main-title"]/text()').extract()
        # print(programme)
        degreetype=response.xpath('//dt[contains(text(),"Degree Awarded")]/following-sibling::dd[1]/text()').extract()
        degreetype=''.join(degreetype)
        programme=''.join(programme).strip()
        duration=re.findall('\(.*?\)$',programme)
        duration=''.join(duration)
        # print("duration: ", duration)
        duration_end = duration
        programme=programme.replace(degreetype,'').replace(duration,'').strip().strip('in').strip()
        # duration=duration.replace('(','').replace(')','')
        item['programme_en'] = programme
        if "(with a Year Abroad)" in duration_end:
            item['programme_en'] = item['programme_en'] + " (with a Year Abroad)"
        if "(with Year Abroad)" in duration_end:
            item['programme_en'] = item['programme_en'] + " (with Year Abroad)"
        # print(programme)
        duration=clear_duration(duration)
        if duration['duration']!=None:
            item['duration'] = duration['duration']
            item['duration_per'] = duration['duration_per']
        else:
            item['duration']=1
            item['duration_per']=1
        item['degree_name'] = degreetype.replace("(Hons)", "").strip()
        item['degree_type'] = 1
        # print("item['programme_en']: ", item['programme_en'])
        # print("item['degree_name']: ", item['degree_name'])
        # print("item['duration']: ", item['duration'])
        # print("item['duration_per']: ", item['duration_per'])
        duration_per_0 = item['duration_per']

        ucascode = response.xpath('//dt[contains(text(),"UCAS Course Code")]/following-sibling::dd[1]//text()').extract()
        ucascode = clear_same_s(ucascode)
        ucascode = remove_class(ucascode)
        item['ucascode'] = ucascode
        # print("item['ucascode']: ", item['ucascode'])

        overview=response.xpath('//div[@data-target="tabset-1"]').extract()
        overview=clear_same_s(overview)
        overview=remove_class(overview)
        item['overview_en'] = overview
        # print("item['overview_en']: ", item['overview_en'])

        entry_requirements=response.xpath('//div[@data-target="tabset-2"]').extract()
        entry_requirements=clear_same_s(entry_requirements).strip()
        entry_requirements=remove_class(entry_requirements)
        # item['rntry_requirements'] = entry_requirements
        # print("item['ucascode']: ", item['ucascode'])

        modules=response.xpath('//div[@data-target="tabset-3"]').extract()
        modules = ''.join(modules)
        modules=clear_same_s([modules]).strip()
        modules=remove_class(modules)
        item['modules_en'] = modules
        clear_class1 = re.findall('<script>.*?</script>', item['modules_en'])
        for i1 in clear_class1:
            item['modules_en'] = item['modules_en'].replace(i1, '')
        # print("item['modules_en']: ", item['modules_en'])

        # tuition_fee=self.get_tuitionfee(item['ucascode'])
        # print(tuition_fee)
        # item['tuition_fee']=tuition_fee
        # print("item['tuition_fee']: ", item['tuition_fee'])
        fee=response.xpath('//h4[contains(text(),"Tuition fees")]/following-sibling::*').extract()
        if fee==[]:
            print(response.url)
        else:
            # print(fee)
            fee=getTuition_fee(fee)
            # print(fee)
            item['tuition_fee']=fee

        career=response.xpath('//h3[contains(text(),"Career Opportunities")]|//h3[contains(text(),"Career Opportunities")]/following-sibling::div[1]').extract()
        career=clear_same_s(career)
        career=remove_class(career)
        item['career_en'] = career
        # print("item['career_en']: ", item['career_en'])

        assessment=response.xpath('//h3[contains(text(),"Learning & Assessment")]|//h3[contains(text(),"Learning & Assessment")]/following-sibling::div[1]').extract()
        assessment=clear_same_s(assessment)
        assessment=remove_class(assessment)
        item['assessment_en'] = assessment
        # print("item['assessment_en']: ", item['assessment_en'])

        department=response.xpath('//nav[@typeof="BreadcrumbList"]/a/following-sibling::div[1]//text()').extract()
        department=''.join(department)
        item['department'] = department
        # print(department)

        howtoapply=["""<div class="uos-tier uos-tier-secondary"><div class="uos-tier-inner"><div class="accordion-1" id="uos-component-accordion-applicationsteps"><h3 class="uos-component-accordion-title js-accordion" tabindex="0" data-group=".accordion-1" data-target="#uos-component-accordion-applicationsteps">Application steps </h3><div class="uos-component-accordion-container"><p>Applying to university is an exciting time with lots to think about. With this in mind, we have created these steps as a guide to simplify the process.</p></div></div><div class="accordion-1 uos-js-triggered" id="uos-component-accordion-step1keydatesanddeadlines"><h3 class="uos-component-accordion-title js-accordion" tabindex="0" data-group=".accordion-1" data-target="#uos-component-accordion-step1keydatesanddeadlines">Step 1: Key dates and deadlines </h3><div class="uos-component-accordion-container"><h5><strong>Starting study in September 2018</strong></h5>
<p>Applications for 2018 entry close on 30 June 2018 though you may still be able to apply through Clearing and Adjustment. Find out if you are eligible to apply through Clearing and Adjustment, how to apply, and all of the key dates through our <a title="Clearing and Adjustment details" href="https://www.southampton.ac.uk/courses/clearing.page">Clearing and Adjustment pages</a>.</p>
<p>UCAS opens Clearing and Adjustment 2018 on 5 July 2018.</p>
<h5>Starting study in September 2019</h5>
<p><strong>UCAS Undergraduate Apply is open for 2019 entry. You can start your application now, but completed applications cannot be submitted to us until 5 September 2018.</strong></p>
<p>If you're applying through your school/college, please check their deadline, and follow this&nbsp;to get your application in on time. This&nbsp;gives them enough time to read your application, check you've&nbsp;entered your qualifications correctly, write and attach your reference, and submit your&nbsp;application to us.</p></div></div><div class="accordion-1 uos-js-triggered" id="uos-component-accordion-step2beforeyouapply"><h3 class="uos-component-accordion-title js-accordion" tabindex="0" data-group=".accordion-1" data-target="#uos-component-accordion-step2beforeyouapply">Step 2: Before you apply</h3><div class="uos-component-accordion-container"><h5>Make sure the course is right for you</h5>
<p>Making sure the course is right for you is essential. Review the <a title="Look at your course details " href="https://www.southampton.ac.uk/courses/undergraduate.page">course details </a> and don't be afraid to&nbsp;<a title="Contact the faculty " href="https://www.southampton.ac.uk/about/departments/faculties.page">contact the faculty</a> if you have any questions, we are always happy to help.</p>
<h5>Entry requirements and qualifications</h5>
<p>It is important that you check that your&nbsp;<a title="Accepted qualifications " href="/courses/how-to-apply/undergraduate-applications/requirements.page">qualifications</a> are accepted and your grades are in line with the course <a title="Check your course entry requirements " href="https://www.southampton.ac.uk/courses/undergraduate.page">entry requirements</a>. If you are an international student please also advise check the <a title="English language requirements " href="https://www.southampton.ac.uk/studentadmin/admissions/admissions-policies/language.page">English language requirements</a> before applying.</p></div></div><div class="accordion-1 uos-js-triggered" id="uos-component-accordion-step3preparingforyourapplication"><h3 class="uos-component-accordion-title js-accordion" tabindex="0" data-group=".accordion-1" data-target="#uos-component-accordion-step3preparingforyourapplication">Step 3: Preparing for your application</h3><div class="uos-component-accordion-container"><h5>UCAS information</h5>
<p>When you apply through UCAS, you will be asked for an institution name and number and course code. Having the UCAS information ready will make things quicker:</p>
<ul>
<li>our code name is <strong>SOTON</strong></li>
<li>our number is <strong>S27</strong></li>
<li>course code can be found on the&nbsp;<a title="course details " href="https://www.southampton.ac.uk/courses/undergraduate.page">course page</a> under 'Course facts'</li>
<li>the application fee is &pound;23 if you are applying to more than one college, university or programme of study</li>
<li>the fee will be &pound;12 if you are just applying to one programme of study at one institution</li>
</ul>
<h5>Personal statement</h5>
<p>Start preparing your personal statement before you apply. For some inspiration and expert advice, check out 'Top tips for writing a <a title="Expert advice for writing a top personal statement " href="/courses/how-to-apply/undergraduate-applications/personal-statement.page">personal statement</a>' from our Head of Admissions.</p></div></div><div class="accordion-1 uos-js-triggered" id="uos-component-accordion-step4applyingandresponsetimes"><h3 class="uos-component-accordion-title js-accordion" tabindex="0" data-group=".accordion-1" data-target="#uos-component-accordion-step4applyingandresponsetimes">Step 4: Applying and response times</h3><div class="uos-component-accordion-container"><h5>Submitting an application</h5>
<p>All undergraduate applicants, including international students will need to&nbsp;<a title="Apply online with UCAS" href="https://www.ucas.com/ucas/undergraduate/ucas-undergraduate-apply-and-track">apply online with UCAS</a>. Once you have applied, UCAS will send you an acknowledgement email and forward your application to us. We will let you know that your application has been received and is being processed.</p>
<h5>Application response</h5>
<p>You will receive a response within two to six weeks, depending on your course. As well as a notification in UCAS Track, we will send you an email with our response. If you live in the UK you will also receive a printed copy by post.</p></div></div><div class="accordion-1 uos-js-triggered" id="uos-component-accordion-step5whathappensnext"><h3 class="uos-component-accordion-title js-accordion" tabindex="0" data-group=".accordion-1" data-target="#uos-component-accordion-step5whathappensnext">Step 5: What happens next?</h3><div class="uos-component-accordion-container"><h5><a title="Register for Clearing and Adjustment updates" href="https://app-eu.geckoform.com/public/?_ga=2.140998898.1170143111.1529309469-37377793.1520435869#/modern/FOEU0232p4qfVJRI">Register for Clearing updates </a>After you apply</h5>
<p>You will be sent an invitation to an Applicant Visit Day* either after you apply or if you are made an offer to study, depending on your course and the time of year that you apply. This will allow you to talk to academics and tour the labs, studios and lecture theatres in which you'll be studying.</p>
<p>For some subjects you may be required to attend an interview. If this is the case, you will be contacted directly by the faculty.</p>
<p>*Please note Applicant Visit Days do not generally take place from May - October but there are other ways you can <a title="Visit us " href="https://www.southampton.ac.uk/about/visit.page">visit us</a>.</p>
<h5>If you are made an offer</h5>
<p>Congratulations if you have been made an offer to study with us. Depending on when you applied, you will have a deadline to reply to your offers by. All decision deadlines can be found on the <a title="UCAS decision deadlines" href="https://www.ucas.com/ucas/events/find/cycle/2018/scheme/undergraduate/type/key-date">UCAS website</a>.</p>
<h5>Deferred entry</h5>
<p>If you wish to take a gap year, your application will be considered in the normal way, but for entry in 2019 the conditions must have been met in the summer of 2018.</p>
<p>Please note, Winchester School of Art does not accept deferred applications. However, in exceptional circumstances WSA can defer entry to the following year once you have been offered a place, have accepted it as your firm choice, and met all your conditions.</p></div></div></div></div>"""]
        howtoapply='\n'.join(howtoapply)
        item['apply_proces_en'] = remove_class(howtoapply)
        # print("item['apply_proces_en']: ", item['apply_proces_en'])

        require_chinese_en = ["""<h4>Undergraduate entry requirements</h4>
<p>To be considered for&nbsp;a place on&nbsp;one of our undergraduate (bachelors) degrees, you will need:</p>
<table class="responsivetable">
<tbody>
<tr>
<td>UK A levels obtained in China&nbsp;</td>
</tr>
<tr>
<td>International Baccalaureate (IB): Between 28 and 38 points&nbsp;</td>
</tr>
<tr>
<td>First year of a relevant degree from a high ranked Chinese university, with an average grade of at least 70-80%&nbsp;</td>
</tr>
</tbody>
</table>"""]
        item['require_chinese_en'] = remove_class(require_chinese_en)

        alevel = response.xpath(
            "//td[contains(text(),'GCE A-level')]/following-sibling::td/p[position()<=4]//text()").extract()
        if alevel==[]:
            alevel=response.xpath('//td[contains(text(),"evel")]/..//text()').extract()
        if alevel==[]:
            alevel=response.xpath('//h5[contains(text(),"evel")]/following-sibling::*[1]//text()').extract()
        if alevel==[]:
            alevel=response.xpath('//h4[contains(text(),"evel")]/following-sibling::*[1]//text()').extract()
        alevel = remove_class(alevel)
        item['alevel'] = alevel.strip()
        # print("item['alevel']: ", item['alevel'])

        ib = response.xpath("//td[contains(text(),'International Baccalaureate')]/following-sibling::td//text()").extract()
        if ib==[]:
            ib=response.xpath('//*[contains(text(),"IB:")]/following-sibling::*[1]//text()').extract()
        ib = remove_class(ib)
        item['ib'] = ib.strip()
        # print("item['ib']: ", item['ib'])

        ielts = response.xpath('//*[contains(text(),"IELTS")]|//h5[contains(text(),"International applications")]/following-sibling::p[1]|'
                                       '//h5[contains(text(),"English language")]/following-sibling::*[1]|'
                               '//h5[contains(text(),"International Applications")]/following-sibling::*[1]|'
                               '//h5[contains(text(),"International applicants")]/following-sibling::p[1]|'
                               '//h5[contains(text(),"English Language")]/following-sibling::*[1]|'
                               '//h5[contains(text(),"Non-native English speakers only")]/following-sibling::*[1]|'
                               '//h5[contains(text(),"International Applicants")]/following-sibling::*[1]').extract()
        if ielts==[]:
            print(response.url)
        item['ielts_desc']=''.join(ielts)
        # if ielts!='':
        #     print(response.url)
        iel=re.findall('\d\.?\d?',item['ielts_desc'])
        # print(iel)
        if len(iel)==3:
            item['ielts']=iel[0]
            item['ielts_r']=iel[1]
            item['ielts_w']=iel[1]
            item['ielts_l']=iel[2]
            item['ielts_s']=iel[2]
        elif len(iel)==1:
            item['ielts'] = iel[0]
            item['ielts_r'] = iel[0]
            item['ielts_w'] = iel[0]
            item['ielts_l'] = iel[0]
            item['ielts_s'] = iel[0]
        elif len(iel)==2:
            iel=list(map(float,iel))
            item['ielts'] = max(iel)
            item['ielts_r'] = min(iel)
            item['ielts_w'] = min(iel)
            item['ielts_l'] = min(iel)
            item['ielts_s'] = min(iel)


        # ielts=get_ielts(ielts)
        toefl=get_toefl(''.join(response.xpath('//*[contains(text(),"TOEFL")]//text()').extract()))
        # if ielts!={} and ielts!=[]:
        #     item['ielts_l']= ielts['IELTS_L']
        #     item['ielts_s'] = ielts['IELTS_S']
        #     item['ielts_r'] = ielts['IELTS_R']
        #     item['ielts_w'] = ielts['IELTS_W']
        #     item['ielts'] = ielts['IELTS']


        if "/" in item['ucascode']:
            # print("///////////////")
            ucascode_0 = item['ucascode'].split("/")
            if "/" in item['degree_name']:
                degree_name_0 = item['degree_name'].split('/')
                if "/" in duration_end:
                    duration_end_0 = duration_end.split('/')
                    # print(ucascode_0)
                    # print(degree_name_0)
                    # print(duration_end_0)
                    for u in range(len(ucascode_0)):
                        item['ucascode'] = ucascode_0[u]
                        item['degree_name'] = degree_name_0[u]
                        item['duration'] = int(''.join(re.findall(r"\d+", duration_end_0[u])))
                        yield item
        else:
            yield item


        # if programme!='':
        #     yield item
            # print(item)

    def get_tuitionfee(self,programme):
        # print(response.url)
        try:
            fee_xpath='//td[contains(text(),"%s")]/following-sibling::td[contains(text(),"£")]//text()' % programme
            fee=self.respon.xpath(fee_xpath)
            tuition_fee=getTuition_fee(fee)
            return tuition_fee
        except:
            return None

