# _*_ coding:utf-8 _*_
import datetime

# 2018/10/15    表tmp_school_major_ca_ben
# 初始化item字典
def get_item(itemClass):
    item = itemClass()
    item['school_code'] = None
    item['school_name'] = None
    item['degree_level'] = None
    item['location'] = None
    item['campus'] = None
    item['major_type1'] = None
    item['major_type2'] = None
    item['department'] = None
    item['degree_name'] = None
    item['degree_cname'] = None
    item['degree_name_desc'] = None
    item['major_name_en'] = None
    item['major_name_cn'] = None
    item['programme_code'] = None
    item['overview_en'] = None
    item['overview_cn'] = None
    item['start_date'] = None
    item['duration'] = None
    item['duration_per'] = None
    item['modules_en'] = None
    item['modules_cn'] = None
    item['career_en'] = None
    item['career_cn'] = None
    item['deadline'] = None
    item['apply_pre'] = None
    item['apply_fee'] = None
    item['tuition_fee_pre'] = None
    item['tuition_fee'] = None
    item['tuition_fee_per'] = None
    item['entry_requirements_en'] = None
    item['entry_requirements_cn'] = None
    item['require_chinese_en'] = None
    item['require_chinese_cn'] = None
    item['specific_requirement_en'] = None
    item['specific_requirement_cn'] = None
    item['average_score'] = None
    item['current_state'] = None
    item['gaokao_desc'] = None
    item['gaokao_zs'] = None
    item['huikao_desc'] = None
    item['huikao_zs'] = None
    item['ielts_desc'] = None
    item['ielts'] = None
    item['ielts_l'] = None
    item['ielts_s'] = None
    item['ielts_r'] = None
    item['ielts_w'] = None
    item['toefl_code'] = None
    item['toefl_desc'] = None
    item['toefl'] = None
    item['toefl_l'] = None
    item['toefl_s'] = None
    item['toefl_r'] = None
    item['toefl_w'] = None
    item['interview_desc_en'] = None
    item['interview_desc_cn'] = None
    item['portfolio_desc_en'] = None
    item['portfolio_desc_cn'] = None
    item['other'] = None
    item['url'] = None
    item['gatherer'] = "yangyaxia"
    item['batch_number'] = 1
    item['update_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return item