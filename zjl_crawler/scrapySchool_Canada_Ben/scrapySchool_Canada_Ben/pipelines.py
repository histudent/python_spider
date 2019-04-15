# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

# 2018/10/15    表tmp_school_ca_ben
class ScrapyschoolCanadaBenPipeline(object):
    db = pymysql.connect('192.168.1.115', 'shiqiyu', 'hooli888', 'hooli_school', charset='utf8')
    cursor = db.cursor()
    count = 1  # 控制最大的批次号不变
    batch_number = 1


    def process_item(self, item, spider):
        # 如果是第一次抓取这所学校，抓取批次batch_number默认为 1 插入数据库
        # 不是第一次抓取，根据学校名和url查询这个数据库的表，
        select_max_sql = "select max(batch_number) from tmp_school_ca_ben where tmp_school_ca_ben.school_name=" + '"' + \
                         item['school_name'] + '"'
        insert_sql = "insert into tmp_school_ca_ben(school_name,location,campus,major_type1,department," \
                     "degree_name,degree_cname,degree_name_desc,degree_overview_en,degree_overview_cn," \
                     "major_name_en,major_name_cn,overview_en,overview_cn,start_date,duration,duration_per," \
                     "modules_en,modules_cn,career_en,career_cn,deadline,apply_pre,apply_fee,tuition_fee_pre," \
                     "tuition_fee,entry_requirements_en,entry_requirements_cn,require_chinese_en,require_chinese_cn," \
                     "average_score,current_state,gaokao_desc,gaokao_zs,gaokao_score_wk,gaokao_score_lk,huikao_desc," \
                     "huikao_zs,is_language,min_language_require,ielts_desc,ielts,ielts_l,ielts_s,ielts_r,ielts_w," \
                     "toefl_code,toefl_desc,toefl,toefl_l,toefl_s,toefl_r,toefl_w,sat_code,sat1_desc,sat2_desc," \
                     "act_code,act_desc,alevel,ib,ap,interview_desc_en,interview_desc_cn,portfolio_desc_en," \
                     "portfolio_desc_cn,is_diploma_certification,is_graduation_card,is_report_code,is_gaokao_score," \
                     "is_huikao_score,other,url,gatherer,batch_number,finishing,update_time,import_status," \
                     "specific_requirement_en,specific_requirement_cn) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        try:
            if self.count == 1:
                self.cursor.execute(select_max_sql)
                batch_number_max_list = self.cursor.fetchall()
                print("查询出来最大的batch_number数据：", batch_number_max_list)
                # for i in batch_number_max_list:
                # print(i[0] is not None)
                # if i[0] is not None:
                b = batch_number_max_list[0][0]
                if batch_number_max_list[0][0] == None:
                    b = 0
                self.batch_number = b + 1
            item['batch_number'] = self.batch_number
            print("item['batch_number']: ", item['batch_number'])
            self.count += 1
            self.cursor.execute(insert_sql,
                                (item["school_name"],item["location"],item["campus"],item["major_type1"],item["department"],
                                 item["degree_name"],item["degree_cname"],item["degree_name_desc"],item["degree_overview_en"],
                                 item["degree_overview_cn"],item["major_name_en"],item["major_name_cn"],item["overview_en"],
                                 item["overview_cn"],item["start_date"],item["duration"],item["duration_per"],item["modules_en"],
                                 item["modules_cn"],item["career_en"],item["career_cn"],item["deadline"],item["apply_pre"],
                                 item["apply_fee"],item["tuition_fee_pre"],item["tuition_fee"],item["entry_requirements_en"],
                                 item["entry_requirements_cn"],item["require_chinese_en"],item["require_chinese_cn"],item["average_score"],
                                 item["current_state"],item["gaokao_desc"],item["gaokao_zs"],item["gaokao_score_wk"],item["gaokao_score_lk"],
                                 item["huikao_desc"],item["huikao_zs"],item["is_language"],item["min_language_require"],item["ielts_desc"],
                                 item["ielts"],item["ielts_l"],item["ielts_s"],item["ielts_r"],item["ielts_w"],item["toefl_code"],
                                 item["toefl_desc"],item["toefl"],item["toefl_l"],item["toefl_s"],item["toefl_r"],item["toefl_w"],
                                 item["sat_code"],item["sat1_desc"],item["sat2_desc"],item["act_code"],item["act_desc"],item["alevel"],
                                 item["ib"],item["ap"],item["interview_desc_en"],item["interview_desc_cn"],item["portfolio_desc_en"],
                                 item["portfolio_desc_cn"],item["is_diploma_certification"],item["is_graduation_card"],item["is_report_code"],
                                 item["is_gaokao_score"],item["is_huikao_score"],item["other"],item["url"],item["gatherer"],
                                 item["batch_number"],item["finishing"],item["update_time"],item["import_status"],
                                 item["specific_requirement_en"],item["specific_requirement_cn"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
            with open("./mysqlerror/" + item['school_name'] + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + item['url'] + "\n========================\n")
                # self.cursor.close()
                # self.db.close()
        return item