import datetime

# 2018/07/18    表tmp_school_au_yan
# 初始化item字典
def get_item(itemClass):
    item = itemClass()
    item["university"] = None
    item["location"] = None
    item["major_type1"] = None
    item["major_type2"] = None
    item["department"] = None
    item["degree_type"] = None
    item["degree_name"] = None
    item["degree_overview_en"] = None
    item["programme_en"] = None
    item["overview_en"] = None
    item["start_date"] = None
    item["duration"] = None
    item["duration_per"] = None
    item["modules_en"] = None
    item["career_en"] = None
    item["application_open_date"] = None
    item["deadline"] = None
    item["apply_pre"] = None
    item["apply_fee"] = None
    item["tuition_fee_pre"] = "AUD$"
    item["tuition_fee"] = None
    item["rntry_requirements_en"] = None
    item["degree_requirements"] = None
    item["major_requirements"] = None
    item["professional_background"] = None
    item["average_score"] = None
    item["ielts_desc"] = None
    item["ielts"] = None
    item["ielts_l"] = None
    item["ielts_s"] = None
    item["ielts_r"] = None
    item["ielts_w"] = None
    item["toefl_code"] = None
    item["toefl_desc"] = None
    item["toefl"] = None
    item["toefl_l"] = None
    item["toefl_s"] = None
    item["toefl_r"] = None
    item["toefl_w"] = None
    item["china_score_requirements"] = None
    item["interview_desc_en"] = None
    item["portfolio_desc_en"] = None
    item["apply_documents_en"] = None
    item["apply_desc_en"] = None
    item["apply_proces_en"] = None
    item["other"] = None
    item["url"] = None
    item["gatherer"] = "yangyaxia"
    item['batch_number'] = 1
    # item["create_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    item["update_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return item