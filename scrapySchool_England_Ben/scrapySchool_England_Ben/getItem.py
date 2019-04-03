import datetime

# 2018/06/26    表tmp_school_uk_ben
# 初始化item字典
def get_item(itemClass):
    item = itemClass()
    item["university"] = ""
    item["location"] = ""
    item["department"] = ""
    item["degree_type"] = None
    item["degree_name"] = ""
    item["major_type1"] = ""
    item["major_type2"] = ""
    item["programme_en"] = ""
    item["overview_en"] = ""
    item["ucascode"] = ""
    item["start_date"] = ""
    item["duration"] = None
    item["duration_per"] = None
    item["modules_en"] = ""
    item["assessment_en"] = ""
    item["career_en"] = ""
    item["tuition_fee_pre"] = "£"
    item["tuition_fee"] = None
    item["require_chinese_en"] = ""
    item["ielts_desc"] = ""
    item["ielts"] = None
    item["ielts_l"] = None
    item["ielts_s"] = None
    item["ielts_r"] = None
    item["ielts_w"] = None
    item["toefl_code"] = ""
    item["toefl_desc"] = ""
    item["toefl"] = None
    item["toefl_l"] = None
    item["toefl_s"] = None
    item["toefl_r"] = None
    item["toefl_w"] = None
    item["alevel"] = ""
    item["ib"] = ""
    item["require_sat_en"] = ""
    item["interview_desc_en"] = ""
    item["portfolio_desc_en"] = ""
    item["application_open_date"] = None
    item["deadline"] = ""
    item["apply_pre"] = ""
    item["apply_fee"] = None
    item["apply_desc_en"] = ""
    item["apply_documents_en"] = ""
    item["apply_proces_en"] = ""
    item["other"] = ""
    item["url"] = ""
    item["gatherer"] = "yangyaxia"
    item['batch_number'] = 1
    # item["create_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    item["update_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return item