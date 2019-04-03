import datetime

# 2018/07/18    表tmp_school_au_yan
# 初始化item字典
def get_item(itemClass):
    item = itemClass()
    item["university"] = ""
    item["location"] = ""
    item["major_type1"] = ""
    item["major_type2"] = ""
    item["department"] = ""
    item["degree_type"] = None
    item["degree_name"] = ""
    item["degree_overview_en"] = ""
    item["programme_en"] = ""
    item["overview_en"] = ""
    item["teach_time"] = ""
    item["start_date"] = ""
    item["duration"] = None
    item["duration_per"] = None
    item["modules_en"] = ""
    item["career_en"] = ""
    item["application_open_date"] = ""
    item["deadline"] = ""
    item["apply_pre"] = ""
    item["apply_fee"] = None
    item["tuition_fee_pre"] = "AUD$"
    item["tuition_fee"] = None
    item["rntry_requirements_en"] = ""
    item["degree_requirements"] = ""
    item["major_requirements"] = ""
    item["professional_background"] = ""
    item["average_score"] = ""
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
    item["work_experience_desc_en"] = ""
    item["interview_desc_en"] = ""
    item["portfolio_desc_en"] = ""
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