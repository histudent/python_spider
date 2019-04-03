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
import requests, json
from lxml import etree

class UniversityofsouthamptonPSpider(scrapy.Spider):
    name = 'UniversityOfSouthampton_P'
    allowed_domains = ['southampton.ac.uk']
    start_urls = []
    pro_url=['https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-accounting-and-finance.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-accounting-and-management.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-finance.page',
'https://www.southampton.ac.uk/economics/postgraduate/taught_courses/msc-finance-and-econometrics.page',
'https://www.southampton.ac.uk/economics/postgraduate/taught_courses/msc_finance_and_economics.page',
'https://www.southampton.ac.uk/maths/postgraduate/taught_courses/msc_diploma_in_operational_research_and_finance.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-international-banking-and-financial-studies.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-international-financial-markets.page',
'https://www.southampton.ac.uk/maths/postgraduate/taught_courses/msc_pgdip_actuarial_science.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_sound_and_vibration_studies.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_aerodynamics_aerodynamics_and_computation.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_aerodynamics_race_car_aerodynamics.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_space_systems_engineering.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_unmanned_aircraft_systems_design.page',
'https://www.southampton.ac.uk/ageing/postgraduate/taught_courses/mSc_gerontology.page',
'https://www.southampton.ac.uk/ageing/postgraduate/taught_courses/msc_gerontology_dl.page',
'https://www.southampton.ac.uk/ageing/postgraduate/taught_courses/msc_gerontology_research.page',
'https://www.southampton.ac.uk/ageing/postgraduate/taught_courses/msc_global_ageing_and_policy_dl.page',
'https://www.southampton.ac.uk/ageing/postgraduate/taught_courses/pg_cert_gerontology.page',
'https://www.southampton.ac.uk/ageing/postgraduate/taught_courses/pg_cert_gerontology_dl.page',
'https://www.southampton.ac.uk/ageing/postgraduate/taught_courses/pg_cert_global_ageing_and_policy_dl.page',
'https://www.southampton.ac.uk/ageing/postgraduate/taught_courses/pg_diploma_gerontology_dl.page',
'https://www.southampton.ac.uk/ageing/postgraduate/taught_courses/pg_dip_global_ageing_and_policy_dl.page',
'https://www.southampton.ac.uk/ageing/postgraduate/taught_courses/short_courses_in_gerontology.page',
'https://www.southampton.ac.uk/ageing/postgraduate/taught_courses/short_courses_in_gerontology_dl.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/archaeology/v400_ma_osteoarchaeology.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/archaeology/v400_ma_msc_maritime_archaeology.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/archaeology/v400-msc-archaeology.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/archaeology/v400-msc-archaeology-bioarchaeology.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/archaeology/v400-msc-archaeology-higher-archaeological-practice.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/archaeology/v400-msc-archaeology-maritime-archaeology.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/archaeology/v400-msc-archaeology-paleoanthropology.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/archaeology/v404_msc_business_and_heritage_management.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/audiology/msc_audiology.page',
'https://www.southampton.ac.uk/biosci/postgraduate/taught_courses/mres-advanced-biological-sciences-degree.page',
'https://www.southampton.ac.uk/biosci/postgraduate/taught_courses/mres-evolution.page',
'https://www.southampton.ac.uk/biosci/postgraduate/taught_courses/mres-advanced-biological-sciences-degree.page',
'https://www.southampton.ac.uk/biosci/postgraduate/taught_courses/wildlife_conservation.page',
'https://www.southampton.ac.uk/biosci/postgraduate/taught_courses/msc-neurosciences.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc-biomedical-engineering.page',
'https://www.southampton.ac.uk/biosci/postgraduate/taught_courses/mres-advanced-biological-sciences-degree.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/mba.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-business-analytics-and-finance.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-business-strategy-and-innovation.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-cyber-security-risk-management.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-digital-business.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-digital-business.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-entrepreneurship-and-management.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-human-resource-management.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-international-management.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-knowledge-information-systems-management.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-marketing-management.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-project-management.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-risk-and-finance.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-risk-management.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-supply-chain-management-and-logistics.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/mba-part-time.page',
'https://www.southampton.ac.uk/chemistry/postgraduate/taught_courses/msc-chemistry.page',
'https://www.southampton.ac.uk/chemistry/postgraduate/taught_courses/msc_research.page',
'https://www.southampton.ac.uk/chemistry/postgraduate/taught_courses/msc-electrochemistry-and-battery-technologies.page',
'https://www.southampton.ac.uk/chemistry/postgraduate/taught_courses/instrumental_analytical_chemistry.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_civil_engineering.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_coastal_and_marine_engineering_and_management.page',
'https://www.southampton.ac.uk/oes/postgraduate/taught_courses/msc_engineering_in_the_coastal_environment.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_transportation_planning_and_engineering.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc-transportation-plan-eng-infrastructure.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc-transportation-plan-eng-operations.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc-transportation-plan-eng-behaviour.page',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-artificial-intelligence ',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc_computer_science ',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-cyber-security ',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-data-science ',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-embedded-systems ',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-software-engineering ',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-web-technology ',
'https://www.southampton.ac.uk/sociology/postgraduate/taught_courses/msc_criminology.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/modern_languages_spanish_portuguese_latin_american_studies/r900_ma_transnational_studies.page',
'https://www.southampton.ac.uk/demography/postgraduate/taught_courses/msc-social-statistics-statistical-pathway.page',
'https://www.southampton.ac.uk/demography/postgraduate/taught_courses/pgdip_msc_demography.page',
'https://www.southampton.ac.uk/demography/postgraduate/taught_courses/msc_global_health.page',
'https://www.southampton.ac.uk/demography/postgraduate/taught_courses/msc-social-statistics-research-methods-pathway.page',
'https://www.southampton.ac.uk/demography/postgraduate/taught_courses/msc_official_statistics.page',
'https://www.southampton.ac.uk/wsa/postgraduate/taught_courses/ma_communication_design.page',
'https://www.southampton.ac.uk/wsa/postgraduate/taught_courses/ma-global-advertising-and-branding.page',
'https://www.southampton.ac.uk/wsa/postgraduate/taught_courses/ma_design_management.page',
'https://www.southampton.ac.uk/wsa/postgraduate/taught_courses/ma_global_media_management.page',
'https://www.southampton.ac.uk/wsa/postgraduate/taught_courses/ma_luxury_brand_management.page',
'https://www.southampton.ac.uk/biosci/postgraduate/taught_courses/mres-advanced-biological-sciences-degree.page',
'https://www.southampton.ac.uk/biosci/postgraduate/taught_courses/wildlife_conservation.page',
'https://www.southampton.ac.uk/economics/postgraduate/taught_courses/msc_economics.page',
'https://www.southampton.ac.uk/economics/postgraduate/taught_courses/msc-finance-and-econometrics.page',
'https://www.southampton.ac.uk/economics/postgraduate/taught_courses/msc_finance_and_economics.page',
'https://www.southampton.ac.uk/economics/postgraduate/research_degrees/courses/integrated-phd-in-economics.page',
'https://www.southampton.ac.uk/education/postgraduate/itt_courses/ske_computer_science.page',
'https://www.southampton.ac.uk/education/postgraduate/itt_courses/ske_mathematics.page',
'https://www.southampton.ac.uk/education/postgraduate/itt_courses/ske_science.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/modern_languages_spanish_portuguese_latin_american_studies/q100_ma_applied_linguistics_for_language_teaching.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/modern_languages/r900_ma_elt_tesol_studies.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/modern_languages_spanish_portuguese_latin_american_studies/r900_ma_english_language_teaching.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/modern_languages_linguistic_studies/r900_ma_english_language_teaching_online.page',
'https://www.southampton.ac.uk/education/postgraduate/taught_courses/ma_ed_dissertation_through_flexible_study.page',
'https://www.southampton.ac.uk/education/postgraduate/taught_courses/msc_education.page',
'https://www.southampton.ac.uk/education/postgraduate/taught_courses/msc_education_management_and_leadership.page',
'https://www.southampton.ac.uk/education/postgraduate/taught_courses/msc-education-online.page',
'https://www.southampton.ac.uk/education/postgraduate/taught_courses/msc_education_practice_and_innovation.page',
'https://www.southampton.ac.uk/education/postgraduate/itt_courses/pgce-english.page',
'https://www.southampton.ac.uk/education/postgraduate/itt_courses/pgce_fe_learning_and_skills_sector.page',
'https://www.southampton.ac.uk/education/postgraduate/itt_courses/pgce_geography.page',
'https://www.southampton.ac.uk/education/postgraduate/itt_courses/pgce_history.page',
'https://www.southampton.ac.uk/education/postgraduate/itt_courses/pgce_information_technology_and_computer_science.page',
'https://www.southampton.ac.uk/education/postgraduate/itt_courses/pgce_mathematics.page',
'https://www.southampton.ac.uk/education/postgraduate/itt_courses/pgce_modern_languages.page',
'https://www.southampton.ac.uk/education/postgraduate/itt_courses/pgce_pe.page',
'https://www.southampton.ac.uk/education/postgraduate/itt_courses/pgce_physics_mathematics.page',
'https://www.southampton.ac.uk/education/postgraduate/itt_courses/pgce_primary.page',
'https://www.southampton.ac.uk/education/postgraduate/itt_courses/pgce_sciences.page',
'https://www.southampton.ac.uk/education/postgraduate/itt_courses/pgce_secondary.page',
'https://www.southampton.ac.uk/education/postgraduate/research_degrees/degrees/integrated_phd_in_education.page',
'https://www.southampton.ac.uk/education/postgraduate/research_degrees/degrees/phd_education.page',
'https://www.southampton.ac.uk/education/postgraduate/itt_courses/pgce_school_direct.page',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/european-masters-embedded-computing-systems-emecs ',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-energy-and-sustainability-electrical-power-engineering ',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-micro-and-nanotechnology',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-microelectronics-systems-design ',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-system-chip ',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-systems-control-and-signal-processing ',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-wireless-communications ',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/european-masters-embedded-computing-systems-emecs ',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-electronic-engineering',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-micro-and-nanotechnology',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-microelectronics-systems-design ',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-system-chip ',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-systems-control-and-signal-processing ',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-wireless-communications ',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/english/w800_ma_creative_writing.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/english/q320-ma-english-literary-studies.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/english/q320-ma-english-literary-studies-eighteenth-century.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/english/q320-ma-english-literary-studies-nineteenth-century.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/english/q320-ma-english-literary-studies-postcolonial-and-world-literatures.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/english/q320-ma-english-literary-studies-twentieth-century.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/modern_languages/r900_ma_global_englishes.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/music/v300_ma_medieval_and_renaissance_culture.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/english/q322-ma-jane-austen.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_coastal_and_marine_engineering_and_management.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_energy_and_sustainability_buildings.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_energy_and_sustainability_climate.page',
'https://www.southampton.ac.uk/oes/postgraduate/taught_courses/msc_engineering_in_the_coastal_environment.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_marine_technology.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_maritime_engineering_science_advanced_materials.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_maritime_engineering_science_marine_engineering.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_maritime_engineering_science_maritime_computational_fluid_dynamics.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_maritime_engineering_science_naval_architecture.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_maritime_engineering_science_offshore_engineering.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_maritime_engineering_science_yacht_and_small_craft.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_sustainable_energy_technologies.page',
'https://www.southampton.ac.uk/biosci/postgraduate/taught_courses/mres-advanced-biological-sciences-degree.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/emp/msc_biodiversity_and_conservation.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/emp/msc_environmental_monitoring_and_assessment.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/emp/msc_environmental_pollution_control.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/emp/msc_integrated_environmental_studies.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/emp/msc_water_resources_management.page',
'https://www.southampton.ac.uk/wsa/postgraduate/taught_courses/ma_fashion_design.page',
'https://www.southampton.ac.uk/wsa/postgraduate/taught_courses/ma_fashion_management.page',
'https://www.southampton.ac.uk/wsa/postgraduate/taught_courses/ma_fashion_and_textile_marketing.page',
'https://www.southampton.ac.uk/wsa/postgraduate/taught_courses/ma_fashion_marketing_and_branding.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/film_studies/p300_ma_film_and_cultural_management.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/film_studies/p300_ma_film.page',
'https://www.southampton.ac.uk/wsa/postgraduate/taught_courses/ma_contemporary_curation.page',
'https://www.southampton.ac.uk/wsa/postgraduate/taught_courses/ma-fine-art.page',
'https://www.southampton.ac.uk/geography/postgraduate/taught_courses/msc_applied_gis_and_remote_sensing.page',
'https://www.southampton.ac.uk/oes/postgraduate/taught_courses/msc_engineering_in_the_coastal_environment.page',
'https://www.southampton.ac.uk/geography/postgraduate/taught_courses/msc_gis_online.page',
'https://www.southampton.ac.uk/geography/postgraduate/taught_courses/msc_sustainability.page',
'https://www.southampton.ac.uk/oes/postgraduate/taught_courses/mres_marine_geology_and_geophysics.page',
'https://www.southampton.ac.uk/oes/postgraduate/taught_courses/mres_marine_geology_and_geophysics.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/mres_clinical_research.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc-adv-clin-practice-adv-crit-care-prac.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc_adv_clin_practice_crit_care.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc_adv_clin_practice_standard.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc_clinical_leadership_cpeol_care.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc-complex-care-in-older-people.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc-health-sciences-amputation-prosthetic-rehabilitation.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc_leadership_management.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc-midwifery-with-advanced-standing.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc-neonatology.page',
'https://www.southampton.ac.uk/medicine/postgraduate/taught_courses/msc_public_health_pathways.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc-trauma-sciences.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc-psycholoigcal-therapies-and-mental-health.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/postgraduate-cert-low-intensity-cbt.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/history/v900_ma_history.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/history/v300_ma_jewish_history_and_culture.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/music/v300_ma_medieval_and_renaissance_culture.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/modern_languages_spanish_portuguese_latin_american_studies/r900_ma_transnational_studies.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/modern_languages_spanish_portuguese_latin_american_studies/q100_ma_applied_linguistics_research_methodology.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/modern_languages_spanish_portuguese_latin_american_studies/q100_ma_applied_linguistics_for_language_teaching.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/modern_languages_spanish_portuguese_latin_american_studies/r900_ma_english_language_teaching.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/modern_languages_linguistic_studies/r900_ma_english_language_teaching_online.page',
'https://www.southampton.ac.uk/law/postgraduate/taught_courses/courses/LLM_general.page',
'https://www.southampton.ac.uk/law/postgraduate/taught_courses/courses/llm-general.page',
'https://www.southampton.ac.uk/law/postgraduate/taught_courses/courses/LLM-commercial-and-corporate-law.page',
'https://www.southampton.ac.uk/law/postgraduate/taught_courses/courses/llm-commercial-and-corporate-law.page',
'https://www.southampton.ac.uk/law/postgraduate/taught_courses/courses/LLM_information_technology_commerce.page',
'https://www.southampton.ac.uk/law/postgraduate/taught_courses/courses/llm-information-technology-commerce.page',
'https://www.southampton.ac.uk/law/postgraduate/taught_courses/courses/llm_insurance_law.page',
'https://www.southampton.ac.uk/law/postgraduate/taught_courses/courses/LLM_international_business_law.page',
'https://www.southampton.ac.uk/law/postgraduate/taught_courses/courses/llm-international-business-law.page',
'https://www.southampton.ac.uk/law/postgraduate/taught_courses/courses/LLM_international_law.page',
'https://www.southampton.ac.uk/law/postgraduate/taught_courses/courses/llm-international-law.page',
'https://www.southampton.ac.uk/law/postgraduate/taught_courses/courses/LLM_maritime_law.page',
'https://www.southampton.ac.uk/law/postgraduate/taught_courses/courses/llm-maritime-law.page',
'https://www.southampton.ac.uk/law/postgraduate/research_degrees/law-phd.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-business-analytics-management-sciences.page',
'https://www.southampton.ac.uk/education/postgraduate/taught_courses/msc_education_management_and_leadership.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc_leadership_management.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_coastal_and_marine_engineering_and_management.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_marine_technology.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_maritime_engineering_science_advanced_materials.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_maritime_engineering_science_marine_engineering.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_maritime_engineering_science_maritime_computational_fluid_dynamics.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_maritime_engineering_science_naval_architecture.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_maritime_engineering_science_offshore_engineering.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_maritime_engineering_science_yacht_and_small_craft.page',
'https://www.southampton.ac.uk/wsa/postgraduate/taught_courses/ma_fashion_and_textile_marketing.page',
'https://www.southampton.ac.uk/wsa/postgraduate/taught_courses/ma_fashion_marketing_and_branding.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-digital-marketing.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-marketing-analytics.page',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-marketing-management.page',
'https://www.southampton.ac.uk/maths/postgraduate/taught_courses/msc-data-decision-analytics.page',
'https://www.southampton.ac.uk/maths/postgraduate/taught_courses/msc_diploma_in_operational_research.page',
'https://www.southampton.ac.uk/maths/postgraduate/taught_courses/msc_diploma_in_operational_research_and_finance.page',
'https://www.southampton.ac.uk/maths/postgraduate/taught_courses/diploma_msc_in_statistics_with_applications_in_medicine.page',
'https://www.southampton.ac.uk/maths/postgraduate/taught_courses/msc-operational-research-and-statistics.page',
'https://www.southampton.ac.uk/maths/postgraduate/taught_courses/msc_in_statistics.page',
'https://www.southampton.ac.uk/maths/postgraduate/taught_courses/msc_pgdip_actuarial_science.page',
'https://www.southampton.ac.uk/maths/postgraduate/research_degrees/degrees/integrated-phd-in-mathematical-sciences.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc-biomedical-engineering.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_advanced_mechanical_engineering_science_computational_engin_design.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_advanced_mechanical_engineering_science_engineering_materials.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_advanced_mechanical_engineering_science_mechatronics.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_advanced_mechanical_engineering_sciences_propulsion.page',
'https://www.southampton.ac.uk/engineering/postgraduate/taught_courses/engineering/msc_advanced_mechanical_engineering_sciences_surface_engineering.page',
'https://www.southampton.ac.uk/medicine/postgraduate/research_degrees/degrees/mres-in-stem-cells-development-and-regenerative-medicine.page',
'https://www.southampton.ac.uk/medicine/postgraduate/taught_courses/msc_allergy.page',
'https://www.southampton.ac.uk/medicine/postgraduate/taught_courses/msc-diabetes-best-practice.page',
'https://www.southampton.ac.uk/medicine/postgraduate/taught_courses/msc-genomic-medicine.page',
'https://www.southampton.ac.uk/maths/postgraduate/taught_courses/diploma_msc_in_statistics_with_applications_in_medicine.page',
'https://www.southampton.ac.uk/medicine/postgraduate/taught_courses/msc_public_health_pathways.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc_midwifery_studies.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/music/w300_mmus_music.page',
'https://www.southampton.ac.uk/biosci/postgraduate/taught_courses/mres-advanced-biological-sciences-degree.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/postgraduate-cert-low-intensity-cbt.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc_adv_clin_practice_practitioner.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc_adv_clin_practice_neonatal.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc_adv_clin_practice_specialist.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/top_ups/msc_top_up.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/pgdip_adult_nursing.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/pgdip_child_nursing.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/pgdip_mental_nursing.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/pgdip_specialist_community_public_health_nursing.page',
'https://www.southampton.ac.uk/oes/postgraduate/taught_courses/mres_marine_geology_and_geophysics.page',
'https://www.southampton.ac.uk/oes/postgraduate/taught_courses/mres_ocean_science.page',
'https://www.southampton.ac.uk/oes/postgraduate/taught_courses/msc_engineering_in_the_coastal_environment.page',
'https://www.southampton.ac.uk/oes/postgraduate/taught_courses/msc_marine_environment_and_resources.page',
'https://www.southampton.ac.uk/oes/postgraduate/taught_courses/msc_oceanography.page',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-optical-fibre-technologies',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-photonic-technologies',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/philosophy/v500_ma_philosophy.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc_physiotherapy.page',
'https://www.southampton.ac.uk/law/postgraduate/taught_courses/courses/LLM_international_business_law.page',
'https://www.southampton.ac.uk/law/postgraduate/taught_courses/courses/llm-international-business-law.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/modern_languages_spanish_portuguese_latin_american_studies/r900_ma_transnational_studies.page',
'https://www.southampton.ac.uk/politics/postgraduate/taught_courses/master-of-public-administration.page',
'https://www.southampton.ac.uk/politics/postgraduate/taught_courses/msc_governance_and_policy_research.page',
'https://www.southampton.ac.uk/politics/postgraduate/taught_courses/msc-international-politics-research.page',
'https://www.southampton.ac.uk/politics/postgraduate/taught_courses/msc-international-security-and-risk.page',
'https://www.southampton.ac.uk/politics/postgraduate/taught_courses/msc_governance_and_policy.page',
'https://www.southampton.ac.uk/politics/postgraduate/taught_courses/msc-international-politics.page',
'https://www.southampton.ac.uk/psychology/postgraduate/taught_courses/msc_foundations_of_clinical_psychology.page',
'https://www.southampton.ac.uk/psychology/postgraduate/taught_courses/msc_health_psychology.page',
'https://www.southampton.ac.uk/psychology/postgraduate/taught_courses/msc_research_methods_in_psychology.page',
'https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/postgraduate-cert-low-intensity-cbt.page',
'https://www.southampton.ac.uk/psychology/postgraduate/taught_courses/postgraduate_diploma_in_cbt.page',
'https://www.southampton.ac.uk/psychology/postgraduate/taught_courses/postgraduate_certificate_in_cbt_advanced_level_practice.page',
'https://www.southampton.ac.uk/psychology/cpd/courses/postgraduate_in_cbt_introduction.page',
'https://www.southampton.ac.uk/psychology/postgraduate/taught_courses/postgraduate_diploma_in_cbt_for_anxiety_and_depression.page',
'https://www.southampton.ac.uk/demography/cpd/courses/official_statistics_short_course.page',
'https://www.southampton.ac.uk/demography/cpd/courses/courses_in_applied_social_surveys.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/modern_languages_spanish_portuguese_latin_american_studies/r900_ma_transnational_studies.page',
'https://www.southampton.ac.uk/demography/postgraduate/taught_courses/msc-data-analytics-for-government.page',
'https://www.southampton.ac.uk/sociology/postgraduate/taught_courses/msc_international_social_policy.page',
'https://www.southampton.ac.uk/medicine/postgraduate/taught_courses/msc_public_health_pathways.page',
'https://www.southampton.ac.uk/sociology/postgraduate/taught_courses/msc_sociology_and_social_policy.page',
'https://www.southampton.ac.uk/sociology/postgraduate/taught_courses/msc_sociology_and_social_research.page',
'https://www.southampton.ac.uk/wsa/postgraduate/taught_courses/ma_textile_design.page',
'https://www.southampton.ac.ukhttp://www.ecs.soton.ac.uk/programmes/msc-web-science ',
'https://www.southampton.ac.uk/biosci/postgraduate/taught_courses/mres-advanced-biological-sciences-degree.page',
'https://www.southampton.ac.uk/biosci/postgraduate/taught_courses/wildlife_conservation.page',]
    pro_url=['https://www.ecs.soton.ac.uk/programmes/msc-artificial-intelligence%20',
'https://www.ecs.soton.ac.uk/programmes/msc_computer_science%20',
'https://www.ecs.soton.ac.uk/programmes/msc-cyber-security%20',
'https://www.ecs.soton.ac.uk/programmes/msc-cyber-security%20',
'https://www.ecs.soton.ac.uk/programmes/msc-data-science%20',
'https://www.southampton.ac.uk/business-school/postgraduate/taught_courses/msc-digital-marketing.page',
'https://www.southampton.ac.uk/economics/postgraduate/taught_courses/msc_economics.page',
'https://www.southampton.ac.uk/chemistry/postgraduate/taught_courses/electrochemistry.page',
'https://www.ecs.soton.ac.uk/programmes/msc-electronic-engineering',
'https://www.ecs.soton.ac.uk/programmes/msc-embedded-systems%20',
'https://www.ecs.soton.ac.uk/programmes/msc-energy-and-sustainability-electrical-power-engineering%20',
'https://www.ecs.soton.ac.uk/programmes/european-masters-embedded-computing-systems-emecs%20',
'https://www.southampton.ac.uk/wsa/postgraduate/taught_courses/ma-games-design.page',
'https://www.southampton.ac.uk/ageing/postgraduate/taught_courses/mSc_gerontology.page',
'https://www.southampton.ac.uk/humanities/postgraduate/taught_courses/taught_courses/modern_languages_spanish_portuguese_latin_american_studies/q100_ma_applied_linguistics_for_language_teaching.page',
'https://www.southampton.ac.uk/law/postgraduate/taught_courses/courses/llm-international-law.page',
'https://www.ecs.soton.ac.uk/programmes/msc-micro-and-nanotechnology',
'https://www.ecs.soton.ac.uk/programmes/msc-microelectronics-systems-design%20',
'https://www.ecs.soton.ac.uk/programmes/msc-optical-fibre-technologies',
'https://www.ecs.soton.ac.uk/programmes/msc-photonic-technologies',
'https://www.southampton.ac.uk/demography/postgraduate/taught_courses/msc-social-research-methods-with-applied-statistics.page',
'https://www.southampton.ac.uk/demography/postgraduate/taught_courses/msc-social-research-methods-with-applied-statistics.page',
'https://www.ecs.soton.ac.uk/programmes/msc-software-engineering%20',
'https://www.ecs.soton.ac.uk/programmes/msc-system-chip%20',
'https://www.ecs.soton.ac.uk/programmes/msc-systems-control-and-signal-processing%20',
'https://www.ecs.soton.ac.uk/programmes/msc-web-science%20',
'https://www.ecs.soton.ac.uk/programmes/msc-web-technology%20',
'https://www.ecs.soton.ac.uk/programmes/msc-wireless-communications%20',]
    pro_url=['https://www.southampton.ac.uk/healthsciences/postgraduate/taught_courses/msc_health_sciences.page']
    for i in pro_url:
        start_urls.append(i)
    # def parse(self, response):
        # urllist=response.xpath('//div[@id="js-course-list"]/dl[@class="uos-course-group"]/dd/a/@href').extract()
        # print(urllist)
        # baseurl='https://www.southampton.ac.uk%s'
        # for i in urllist:
            # fullurls=baseurl % i
            # print(fullurls)
            # yield scrapy.Request(fullurls,callback=self.parse_date)
    def parse(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university'] = "University of Southampton"
        item['url'] = response.url
        item['location'] = 'Southampton'
        programme=response.xpath('//h1[@class="uos-page-title uos-main-title"]/text()').extract()
        # print(programme)
        degreetype=response.xpath('//dt[contains(text(),"Degree Awarded")]/following-sibling::dd[1]/text()').extract()
        degreetype=''.join(degreetype)
        programme=''.join(programme).strip()
        duration=re.findall('\(.*\)',programme)
        duration=''.join(duration)
        programme=programme.replace(degreetype,'').replace(duration,'').replace(' in ',' ').strip()
        # duration=duration.replace('(','').replace(')','')
        item['programme_en'] = programme
        # print(programme)
        duration=clear_duration(duration)
        if duration['duration']!=None:
            item['duration'] = duration['duration']
            item['duration_per'] = duration['duration_per']
        else:
            item['duration']=1
            item['duration_per']=1
        item['degree_name'] = degreetype
        item['degree_type'] = 2
        overview=response.xpath('//div[@data-target="tabset-1"]').extract()
        overview=clear_same_s(overview)
        overview=remove_class(overview)
        item['overview_en'] = overview

        entry_requirements=response.xpath('//div[@data-target="tabset-2"]').extract()
        entry_requirements=clear_same_s(entry_requirements).strip()
        entry_requirements=remove_class(entry_requirements)
        item['rntry_requirements'] = entry_requirements

        modules=response.xpath('//div[@data-target="tabset-3"]').extract()
        modules=clear_same_s(modules).strip()
        modules=remove_class(modules)
        item['modules_en'] = modules
        # print(modules)

        tuition_fee=self.get_tuitionfee(programme)
        # print(tuition_fee)
        item['tuition_fee']=tuition_fee

        career=response.xpath('//h3[contains(text(),"Career Opportunities")]/following-sibling::div[1]').extract()
        career=clear_same_s(career)
        career=remove_class(career)
        item['career_en'] = career
        # print(career)

        assessment=response.xpath('//h3[contains(text(),"Learning & Assessment")]/following-sibling::div[1]').extract()
        assessment=clear_same_s(assessment)
        assessment=remove_class(assessment)
        item['assessment_en'] = assessment
        # print(assessment)

        department=response.xpath('//nav[@typeof="BreadcrumbList"]/a/following-sibling::div[1]//text()').extract()
        department=''.join(department)
        item['department'] = department
        # print(department)

        howtoapply=["1. Identify the course you would like to apply for. Visit the postgraduate taught courses page.",
"2. Check you meet the general entry requirements, and, if relevant, make sure you meet any special requirements for international students. See more information about entry requirements.",
"3. Find out about scholarships and sources of funding. Visit our postgraduate funding page.",
"4. Apply online",]
        howtoapply='\n'.join(howtoapply)
        item['apply_proces_en'] = howtoapply

        application_documents=['your CV',
'your degree certificate(s) (and translated version if necessary)',
'degree transcript(s)(and translated version if necessary)',
'English language qualification (if applicable)',
'two references',]
        application_documents='\n'.join(application_documents)
        item['apply_documents_en']=application_documents

        ielts=get_ielts(''.join(response.xpath('//*[contains(text(),"IELTS")]//text()').extract()))
        toefl=get_toefl(''.join(response.xpath('//*[contains(text(),"TOEFL")]//text()').extract()))
        if ielts!={} and ielts!=[]:
            item['ielts_l']= ielts['IELTS_L']
            item['ielts_s'] = ielts['IELTS_S']
            item['ielts_r'] = ielts['IELTS_R']
            item['ielts_w'] = ielts['IELTS_W']
            item['ielts'] = ielts['IELTS']
        if programme!='':
            yield item
            # print(item)
    def get_tuitionfee(self,programme):
        # print(response.url)
        try:
            responses=requests.get('https://www.southampton.ac.uk/uni-life/fees-funding/pg-fees-funding/pg-fees/postgraduate-taught.page').content
            responses=etree.HTML(responses)
            fee_xpath='//td[contains(text(),"%s")]/following-sibling::td[contains(text(),"£")]//text()' % programme
            fee=responses.xpath(fee_xpath)
            tuition_fee=getTuition_fee(fee)
            return tuition_fee
        except:
            return None

