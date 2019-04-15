import datetime


# 2018/07/18   表tmp_school_au_yan
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
    item["duration"] = None           # tinyint
    item["duration_per"] = None       # tinyint
    item["modules_en"] = ""
    item["career_en"] = ""
    item["tuition_fee_pre"] = ""
    item["tuition_fee"] = None            # int
    item["rntry_requirements_en"] = ""
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
    item['average_score'] = ''
    item["update_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    item["china_score_requirements"] = ''
    item["degree_overview_en"] = ''
    return item