# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 2018/10/15    表tmp_school_ca_ben
class ScrapyschoolCanadaBenItem(scrapy.Item):
    school_name = scrapy.Field()
    location = scrapy.Field()
    campus = scrapy.Field()
    major_type1 = scrapy.Field()
    department = scrapy.Field()
    degree_name = scrapy.Field()
    degree_cname = scrapy.Field()
    degree_name_desc = scrapy.Field()
    degree_overview_en = scrapy.Field()
    degree_overview_cn = scrapy.Field()
    major_name_en = scrapy.Field()
    major_name_cn = scrapy.Field()
    overview_en = scrapy.Field()
    overview_cn = scrapy.Field()
    start_date = scrapy.Field()
    duration = scrapy.Field()
    duration_per = scrapy.Field()
    modules_en = scrapy.Field()
    modules_cn = scrapy.Field()
    career_en = scrapy.Field()
    career_cn = scrapy.Field()
    deadline = scrapy.Field()
    apply_pre = scrapy.Field()
    apply_fee = scrapy.Field()
    tuition_fee_pre = scrapy.Field()
    tuition_fee = scrapy.Field()
    entry_requirements_en = scrapy.Field()
    entry_requirements_cn = scrapy.Field()
    require_chinese_en = scrapy.Field()
    require_chinese_cn = scrapy.Field()
    average_score = scrapy.Field()
    current_state = scrapy.Field()
    gaokao_desc = scrapy.Field()
    gaokao_zs = scrapy.Field()
    gaokao_score_wk = scrapy.Field()
    gaokao_score_lk = scrapy.Field()
    huikao_desc = scrapy.Field()
    huikao_zs = scrapy.Field()
    is_language = scrapy.Field()
    min_language_require = scrapy.Field()
    ielts_desc = scrapy.Field()
    ielts = scrapy.Field()
    ielts_l = scrapy.Field()
    ielts_s = scrapy.Field()
    ielts_r = scrapy.Field()
    ielts_w = scrapy.Field()
    toefl_code = scrapy.Field()
    toefl_desc = scrapy.Field()
    toefl = scrapy.Field()
    toefl_l = scrapy.Field()
    toefl_s = scrapy.Field()
    toefl_r = scrapy.Field()
    toefl_w = scrapy.Field()
    sat_code = scrapy.Field()
    sat1_desc = scrapy.Field()
    sat2_desc = scrapy.Field()
    act_code = scrapy.Field()
    act_desc = scrapy.Field()
    alevel = scrapy.Field()
    ib = scrapy.Field()
    ap = scrapy.Field()
    interview_desc_en = scrapy.Field()
    interview_desc_cn = scrapy.Field()
    portfolio_desc_en = scrapy.Field()
    portfolio_desc_cn = scrapy.Field()
    is_diploma_certification = scrapy.Field()
    is_graduation_card = scrapy.Field()
    is_report_code = scrapy.Field()
    is_gaokao_score = scrapy.Field()
    is_huikao_score = scrapy.Field()
    other = scrapy.Field()
    url = scrapy.Field()
    gatherer = scrapy.Field()
    batch_number = scrapy.Field()
    finishing = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    import_status = scrapy.Field()
    specific_requirement_cn = scrapy.Field()
    specific_requirement_en = scrapy.Field()
