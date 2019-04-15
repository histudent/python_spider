import datetime

# 2018/06/12    表tmp_school_major_uk
# 初始化item字典
def get_item(itemClass):
    item = itemClass()
    item["university"] = ""
    item["country"] = ""
    item["location"] = ""
    item["website"] = ""
    item["department"] = ""
    item["programme"] = ""
    item["major_type"] = 0
    item["degree_level"] = 0
    item["degree_type"] = ""
    item["full_time"] = ""
    item["taught"] = ""
    item["ucas_code"] = ""
    item["application_date"] = ""
    item["deadline"] = ""
    item["start_date"] = ""
    item["overview"] = ""
    item["duration"] = ""
    item["modules"] = ""
    item["application_fee"] = ""
    item["tuition_fee"] = ""
    item["teaching_assessment"] = ""
    item["career"] = ""
    item["academic_requirements"] = ""
    item["entry_requirements"] = ""
    item["chinese_requirements"] = ""
    item["accredited_university"] = ""
    item["Alevel"] = ""
    item["IB"] = ""
    item["GRE"] = ""
    item["GMAT"] = ""
    item["IELTS"] = ""
    item["IELTS_L"] = ""
    item["IELTS_S"] = ""
    item["IELTS_R"] = ""
    item["IELTS_W"] = ""
    item["TOEFL_code"] = ""
    item["TOEFL"] = ""
    item["TOEFL_L"] = ""
    item["TOEFL_S"] = ""
    item["TOEFL_R"] = ""
    item["TOEFL_W"] = ""
    item["interview"] = ""
    item["portfolio"] = ""
    item["application_documents"] = ""
    item["how_to_apply"] = ""
    item["school_test"] = ""
    item["SATRelated"] = ""
    item["other"] = ""
    item["working_experience"] = ""
    item["url"] = ""
    item["teacher_name"] = ""
    item["create_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    item["create_person"] = ""
    # item["update_time"] = ""
    item["spiderman"] = ""
    item["update_person"] = ""
    item["status"] = 0
    item["import_status"] = 0
    item["sid"] = 0
    item["did"] = 0
    item["pid"] = 0
    item["batch_number"] = 1

    return item

# 2018/06/26    表tmp_school_uk_yan
# 初始化item字典
def get_item1(itemClass):
    item = itemClass()
    item["university"] = ""
    item["location"] = ""
    item["department"] = ""
    item["programme_en"] = ""
    item["degree_type"] = None
    item['degree_name'] = ""
    item["start_date"] = None         # date
    item["overview_en"] = ""
    item["teach_time"] = ""
    item["teach_type"] = ""
    item["duration"] = None           # tinyint
    item["duration_per"] = None       # tinyint
    item["modules_en"] = ""
    item["assessment_en"] = ""
    item["career_en"] = ""
    item["tuition_fee_pre"] = ""
    item["tuition_fee"] = None            # int
    item["require_chinese_en"] = ""
    item["require_chinese_school_en"] = ""
    item["rntry_requirements"] = ""
    item["degree_requirements"] = ""
    item["major_requirements"] = ""
    item["professional_background"] = ""
    item["ielts_desc"] = ""
    item["ielts"] = None              # float
    item["ielts_l"] = None            # float
    item["ielts_s"] = None            # float
    item["ielts_r"] = None            # float
    item["ielts_w"] = None            # float
    item["toefl_code"] = ""
    item["toefl_desc"] = ""
    item["toefl"] = None              # float
    item["toefl_l"] = None            # float
    item["toefl_s"] = None            # float
    item["toefl_r"] = None            # float
    item["toefl_w"] = None            # float
    item["gre"] = ""
    item["gmat"] = ""
    item["gre_sub"] = ""
    item["lsat"] = ""
    item["mcat"] = ""
    item["work_experience_desc_en"] = ""
    item["application_open_date"] = None      # date
    item["deadline"] = None                       # date
    item["apply_pre"] = ""
    item["apply_fee"] = None                      # int
    item["interview_desc_en"] = ""
    item["portfolio_desc_en"] = ""
    item["apply_desc_en"] = ""
    item["apply_documents_en"] = ""
    item["apply_proces_en"] = ""
    item["other"] = ""
    item["url"] = ""
    item["gatherer"] = "zhangjianlin"
    item['batch_number'] = 1
    #如果是研究生请注释掉
    item['ib'] = ''
    item['alevel'] = ''
    item['major_type1'] = ''
    # item["create_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    item["update_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return item