# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 2018/07/16    表tmp_school_uk_ben
class ScrapyschoolEnglandBenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    university = scrapy.Field()
    location = scrapy.Field()
    department = scrapy.Field()
    degree_type = scrapy.Field()
    degree_name = scrapy.Field()
    major_type1 = scrapy.Field()
    major_type2 = scrapy.Field()
    programme_en = scrapy.Field()
    overview_en = scrapy.Field()
    ucascode = scrapy.Field()
    start_date = scrapy.Field()
    duration = scrapy.Field()
    duration_per = scrapy.Field()
    modules_en = scrapy.Field()
    assessment_en = scrapy.Field()
    career_en = scrapy.Field()
    tuition_fee_pre = scrapy.Field()
    tuition_fee = scrapy.Field()
    require_chinese_en = scrapy.Field()
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
    alevel = scrapy.Field()
    ib = scrapy.Field()
    require_sat_en = scrapy.Field()
    interview_desc_en = scrapy.Field()
    portfolio_desc_en = scrapy.Field()
    application_open_date = scrapy.Field()
    deadline = scrapy.Field()
    apply_pre = scrapy.Field()
    apply_fee = scrapy.Field()
    apply_desc_en = scrapy.Field()
    apply_documents_en = scrapy.Field()
    apply_proces_en = scrapy.Field()
    other = scrapy.Field()
    url = scrapy.Field()
    gatherer = scrapy.Field()
    batch_number = scrapy.Field()
    update_time = scrapy.Field()
