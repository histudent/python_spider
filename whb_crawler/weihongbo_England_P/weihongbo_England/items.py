# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#import datetime

class UcasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sid = scrapy.Field()
    university = scrapy.Field()
    location = scrapy.Field()
    department = scrapy.Field()
    major_type1 = scrapy.Field()#专业方向，一级分类（自定义大方向）
    major_type2 = scrapy.Field()#专业方向，二级分类（自定义小方向）
    programme_en = scrapy.Field()
    degree_type = scrapy.Field()#授课方式：1,taught/2,research/3,phd
    degree_name = scrapy.Field()
    start_date = scrapy.Field()
    overview_en = scrapy.Field()
    teach_time = scrapy.Field()
    teach_type = scrapy.Field()
    duration = scrapy.Field()
    duration_per = scrapy.Field()
    modules_en = scrapy.Field()
    assessment_en = scrapy.Field() #评估方式
    career_en = scrapy.Field()
    tuition_fee_pre = scrapy.Field()
    tuition_fee = scrapy.Field()
    require_chinese_en = scrapy.Field() #中国学生要求
    require_chinese_school_en = scrapy.Field() #认可中国院校
    rntry_requirements = scrapy.Field() #学术要求
    degree_requirements = scrapy.Field() #学位等级要求
    major_requirements = scrapy.Field() #专业方向要求
    professional_background = scrapy.Field() #专业背景要求
    ielts_desc = scrapy.Field()     #ielts_desc 雅思要求描述
    ielts = scrapy.Field()
    ielts_l = scrapy.Field()
    ielts_s = scrapy.Field()
    ielts_r = scrapy.Field()
    ielts_w = scrapy.Field()
    toefl_code = scrapy.Field()   #托福代码
    toefl_desc = scrapy.Field()   #托福要求描述
    toefl = scrapy.Field()          #托福总分
    toefl_l = scrapy.Field()
    toefl_s = scrapy.Field()
    toefl_r = scrapy.Field()
    toefl_w = scrapy.Field()
    gre = scrapy.Field()
    gmat = scrapy.Field()
    gre_sub = scrapy.Field()
    lsat = scrapy.Field()
    mcat = scrapy.Field()
    work_experience_desc_en = scrapy.Field() #工作要求
    application_open_date = scrapy.Field()   #申请开放日期
    deadline = scrapy.Field()               #申请截止日期
    apply_pre = scrapy.Field()
    apply_fee = scrapy.Field()
    interview_desc_en = scrapy.Field()  #面试描述
    portfolio_desc_en = scrapy.Field() #作品集描述
    apply_desc_en = scrapy.Field()  #申请要求
    apply_documents_en = scrapy.Field()#申请材料
    apply_proces_en = scrapy.Field() #申请过程
    other = scrapy.Field()
    url = scrapy.Field()
    batch_number = scrapy.Field()
    gatherer = scrapy.Field()
    finishing = scrapy.Field()
    create_time  = scrapy.Field()
    import_status = scrapy.Field()
    update_time = scrapy.Field()
    alevel = scrapy.Field()
    ucascode = scrapy.Field()
    ib = scrapy.Field()
    require_chinese_en = scrapy.Field()
    assessment_en = scrapy.Field()
    teach_type = scrapy.Field()
    teach_time = scrapy.Field()
    #application_open_date = scrapy.Field()

    # other = scrapy.Field()
    # other = scrapy.Field()
    # other = scrapy.Field()
    # other = scrapy.Field()
    # other = scrapy.Field()
    # other = scrapy.Field()
    #
    #
    #
    #
    #
    #
    # professional_background





