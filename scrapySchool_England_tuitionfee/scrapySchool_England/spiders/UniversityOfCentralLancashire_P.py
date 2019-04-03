# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getDuration import getIntDuration, getTeachTime

class UniversityOfCentralLancashire_PSpider(scrapy.Spider):
    name = "UniversityOfCentralLancashire_P"
    start_urls = ["https://www.uclan.ac.uk/courses/index.php?q=postgraduate"]


    def parse(self, response):
        print(response.url)
        links = response.xpath("//h4[contains(text(),'Postgraduate')]/following-sibling::ul[1]/li/a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))

        # 2018/8/17修改
        links = ["https://www.uclan.ac.uk/courses/ma_teaching_english_to_speakers_of_other_languages_with_linguistics_elearn.php",
"https://www.uclan.ac.uk/courses/msc-advanced-pharmacy-practice.php",
"https://www.uclan.ac.uk/courses/msc_human_resources_management_development.php",
"https://www.uclan.ac.uk/courses/msc_pgdip_pgcert_food_safety_management.php",
"https://www.uclan.ac.uk/courses/ma_pgdip_integrative_psychotherapy.php",
"https://www.uclan.ac.uk/courses/msc-child-and-adolescent-mental-health.php",
"https://www.uclan.ac.uk/courses/msc_pgdip_pgcert_forensic_anthropology.php",
"https://www.uclan.ac.uk/courses/msc_pgdip_oral_surgery.php",
"https://www.uclan.ac.uk/courses/ma_pgdip_pgcert_fashion_design.php",
"https://www.uclan.ac.uk/courses/msc-dental-education.php",
"https://www.uclan.ac.uk/courses/msc-psychosexual-therapy.php",
"https://www.uclan.ac.uk/courses/msc_strength_conditioning.php",
"https://www.uclan.ac.uk/courses/msc-pgdip-pgcert-transforming-integrated-health-and-social-care.php",
"https://www.uclan.ac.uk/courses/msc_financial_investigation.php",
"https://www.uclan.ac.uk/courses/ma-professional-development-and-practice.php",
"https://www.uclan.ac.uk/courses/msc-nursing-general-practice.php",
"https://www.uclan.ac.uk/courses/msc_midwifery.php",
"https://www.uclan.ac.uk/courses/msc-emergency-management-high-hazard-industries.php",
"https://www.uclan.ac.uk/courses/msc-advanced-restorative-and-periodontal-practice.php",
"https://www.uclan.ac.uk/courses/msc_musculoskeletal_management.php",
"https://www.uclan.ac.uk/courses/ma_human_resources_management_development.php",
"https://www.uclan.ac.uk/courses/msc_pgdip_personality_disorder_research.php",
"https://www.uclan.ac.uk/courses/msc_safeguarding_international_context.php",
"https://www.uclan.ac.uk/courses/msc-agile-leadership.php",
"https://www.uclan.ac.uk/courses/msc_advanced_practice_health_and_social_care.php",
"https://www.uclan.ac.uk/courses/ma_antiques.php",
"https://www.uclan.ac.uk/courses/msc-drug-discovery-and-development.php",
"https://www.uclan.ac.uk/courses/msc_pgdip_pgcert_clinical_periodontology.php",
"https://www.uclan.ac.uk/courses/msc-accounting-fast-track.php",
"https://www.uclan.ac.uk/courses/msc-clinical-implantology.php",
"https://www.uclan.ac.uk/courses/ma_dance_and_somatic_wellbeing.php",
"https://www.uclan.ac.uk/courses/msc_pgdip_personality_disorder_practice_development.php",
"https://www.uclan.ac.uk/courses/ma_games_design_distance_learning.php",
"https://www.uclan.ac.uk/courses/ma_pgdip_pgcert_philosophy_and_mental_health.php",
"https://www.uclan.ac.uk/courses/msc_finance_and_management.php",
"https://www.uclan.ac.uk/courses/med_professional_practice_education.php",
"https://www.uclan.ac.uk/courses/msc_pgdip_health_informatics.php",
"https://www.uclan.ac.uk/courses/msc_pgdip_endodontology.php",
"https://www.uclan.ac.uk/courses/msc_pgdip_pgcert_construction_law_dispute_resolution.php",
"https://www.uclan.ac.uk/courses/msc_prosthodontics.php",
"https://www.uclan.ac.uk/courses/msc-cognitive-behavioural-psychotherapy.php",
"https://www.uclan.ac.uk/courses/msc-sustainability-health-wellbeing.php",
"https://www.uclan.ac.uk/courses/mres-pharmaceutical-sciences.php",
"https://www.uclan.ac.uk/courses/ma_accounting_finance_cima.php",
"https://www.uclan.ac.uk/courses/msc-healthcare-practice.php",
"https://www.uclan.ac.uk/courses/ma_pgdip_community_leadership.php",
"https://www.uclan.ac.uk/courses/msc-community-health-practice.php",
"https://www.uclan.ac.uk/courses/msc-football-science-rehabilitation.php",
"https://www.uclan.ac.uk/courses/mba_master_of_business_administration_part_time.php",
"https://www.uclan.ac.uk/courses/msc_pgdip_pgcert_fire_investigation.php",
"https://www.uclan.ac.uk/courses/msc_dental_implantology.php",
"https://www.uclan.ac.uk/courses/outdoor-practice-ma.php",
"https://www.uclan.ac.uk/courses/ma_pgdip_british_sign_language_english_interpreting_and_translation.php",]
        for url in links:
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.uclan.ac.uk/"
        item['university'] = "University of Central Lancashire"
        item['url'] = response.url
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        # item['location'] = 'Hope Park, Liverpool, L16 9JD'
        print("===========================")
        print(response.url)
        try:
            # 专业、学位类型
            programme = response.xpath(
                "//div[@id='TopGraphic']/div[@class='twelvecol last']/h2/text()").extract()
            if len(programme) == 0:
                programme = response.xpath(
                    "//div[@class='marketing-version']/div[@class='course-title']/h1/text()").extract()
            clear_space(programme)
            item['programme_en'] = ''.join(programme)
            print("item['programme_en']: ", item['programme_en'])

            degree_type = response.xpath(
                "//div[@id='TopGraphic']/div[@class='twelvecol last']/h2/span/text()").extract()
            if len(degree_type) == 0:
                degree_type = response.xpath(
                    "//div[@class='marketing-version']/div[@class='course-title']/h1/span/text()").extract()
            clear_space(degree_type)
            item['degree_name'] = ''.join(degree_type)
            print("item['degree_name']: ", item['degree_name'])

            department = response.xpath(
                "//div[@id='TopGraphic']/div[@class='twelvecol last']/h4//text()").extract()
            item['department'] = ''.join(department)
            # print("item['department']: ", item['department'])

            duration = response.xpath(
                "//h4[contains(text(), 'Duration:')]/..//text()").extract()
            clear_space(duration)
            print("duration: ", duration)
            duration_str = ''.join(duration)

            item['teach_time'] = getTeachTime(duration_str)
            duration_list = getIntDuration(duration_str)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            print("item['teach_time'] = ", item['teach_time'])
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            teach_time = response.xpath(
                "//strong[contains(text(),'Full-time:')]/..//text()").extract()
            clear_space(teach_time)
            print("teach_time: ", teach_time)
            item['other'] = ','.join(teach_time)
            if ''.join(teach_time).strip() == "Full-time:" or teach_time[teach_time.index("Full-time:")+1] == "N/A" or\
                    teach_time[teach_time.index("Full-time:")+1] == "" or "part-time" in item['programme_en']:
                item['teach_time'] = "parttime"
            elif item['teach_time'] == "":
                item['teach_time'] = "fulltime"
            print("item['teach_time'] = ", item['teach_time'])


            location = response.xpath(
                "//h4[contains(text(), 'Campus')]/following-sibling::p[1]//text()").extract()
            item['location'] = ''.join(location)
            # print("item['location']", item['location'])

            start_date = response.xpath(
                "//h4[contains(text(), 'Start Date:')]/following-sibling::p[1]//text()").extract()
            # print(start_date)
            item['start_date'] = getStartDate(''.join(start_date))
            # print("item['start_date']", item['start_date'])

            overview = response.xpath(
                "//div[@id='FullCourse']/div[@class='eightcol']/div[@class='sixcol last']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']", item['overview_en'])

            # //div[@id='EntryReq']
            entry_requirements = response.xpath(
                "//div[@id='EntryReq']//text()").extract()
            entry_requirements_str = ''.join(entry_requirements).strip()
            item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']", item['rntry_requirements'])

            # ielts = response.xpath("//div[@id='EntryReq']//p[last()-1]//text() | //div[@id='EntryReq']//ul[last()]//text()").extract()
            # clear_space(ielts)

            # //div[@id='caag']
            modules = response.xpath("//div[@id='caag']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']", item['modules_en'])

            # //h3[contains(text(),'Learning Environment and Assessment')]/..
            assessment_en = response.xpath(
                "//h3[contains(text(),'Learning Environment and Assessment')]/..").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']", item['assessment_en'])

            # //div[@class='ug-course-2017']/div[@class='container gap-bottom'][2]/div[@class='row']/div[@class='twelvecol last']/div
            career_en = response.xpath(
                "//h3[contains(text(),'Graduate Careers')]/..|//h3[contains(text(),'Opportunities')]/..").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career_en))
            # print("item['career_en']", item['career_en'])

            # //h3[@id='applynow']/..
            apply_proces_en = response.xpath(
                "//h3[@id='applynow']/..").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(apply_proces_en))
            # print("item['apply_proces_en']", item['apply_proces_en'])

            # https://www.uclan.ac.uk/study_here/fees_and_finance/international_tuition_fees.php#international
            item['tuition_fee'] = '12950'
            if item['department'] == "School of Forensic and Applied Sciences" or item['department'] == "School of Physical Sciences and Computing" \
                    or item['department'] == "School of Pharmacy and Biomedical Sciences" or item['department'] == "School of Engineering":
                item['tuition_fee'] = '13950'
            item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee']", item['tuition_fee'])
            # School of Forensic and Applied Sciences
            # School of Physical Sciences and Computing
            # School of Pharmacy and Biomedical Sciences
            # School of Engineering

            ieltsList = re.findall(r'.{1,50}IELTS.{1,80}', entry_requirements_str)
            print("ieltslist: ", ieltsList)
            item['ielts_desc'] = ''.join(ieltsList)
            # print("item['ielts_desc']", item['ielts_desc'])

            ielts_list = re.findall(r"[5-9]\.\d\s|[5-9]\.\d,|[5-9]\.\d\.|[5-9]\.\d$|[5-9]\s|[5-9]\.", item['ielts_desc'])
            # print(ielts_list)
            if len(ielts_list) == 1:
                item['ielts'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                item['ielts_l'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                item['ielts_s'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                item['ielts_r'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                item['ielts_w'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
            elif len(ielts_list) == 2:
                item['ielts'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                item['ielts_l'] = ielts_list[1].strip().strip('.').replace(',', '').strip()
                item['ielts_s'] = ielts_list[1].strip().strip('.').replace(',', '').strip()
                item['ielts_r'] = ielts_list[1].strip().strip('.').replace(',', '').strip()
                item['ielts_w'] = ielts_list[1].strip().strip('.').replace(',', '').strip()
            elif len(ielts_list) == 3:
                item['ielts'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                item['ielts_l'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                item['ielts_s'] = ielts_list[0].strip().strip('.').replace(',', '').strip()
                item['ielts_r'] = ielts_list[1].strip().strip('.').replace(',', '').strip()
                item['ielts_w'] = ielts_list[2].strip().strip('.').replace(',', '').strip()
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
            #         item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            item['require_chinese_en'] = "<p>4-year Bachelors degree with grades of 70% or above</p>"
            yield item
        except Exception as e:
            with open(item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

