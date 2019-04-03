# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


# 2018/07/16    表tmp_school_au_yan
class ScrapyschoolAustralianYanPipeline(object):
    # db = pymysql.connect('localhost', 'root', '123456', 'hooli_school', port=3302,charset='utf8')
    # 192.168.1.115     shiqiyu    hooli888
    # db = pymysql.connect('192.168.1.115', 'shiqiyu', 'hooli888', 'hooli_school', charset='utf8')
    db = pymysql.connect('172.16.10.71', 'shiqiyu', 'hooli888', 'hooli_school', charset='utf8')
    cursor = db.cursor()

    count = 1  # 控制最大的批次号不变
    batch_number = 1
    def process_item(self, item, spider):
        # 如果是第一次抓取这所学校，抓取批次batch_number默认为 1 插入数据库
        # 不是第一次抓取，根据学校名和url查询这个数据库的表，
        select_max_sql = "select max(batch_number) from tmp_school_au_yan where tmp_school_au_yan.university=" + '"' + \
                         item['university'] + '"'
        # print(select_max_sql)
        insert_sql = "insert into tmp_school_au_yan(university, location, major_type1, major_type2, department, degree_type, degree_name, " \
                     "degree_overview_en, programme_en, overview_en, teach_time, start_date, duration, duration_per, modules_en, career_en, " \
                     "application_open_date, deadline, apply_pre, apply_fee, tuition_fee_pre, tuition_fee, rntry_requirements_en, degree_requirements, " \
                     "major_requirements, professional_background, average_score, ielts_desc, ielts, ielts_l, ielts_s, ielts_r, ielts_w, toefl_code, " \
                     "toefl_desc, toefl, toefl_l, toefl_s, toefl_r, toefl_w, work_experience_desc_en, interview_desc_en, portfolio_desc_en, apply_desc_en, " \
                     "apply_documents_en, apply_proces_en, other, url, gatherer, batch_number, update_time) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                     "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                     "%s, %s, %s, %s, %s, %s, %s, %s)"
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
            self.cursor.execute(insert_sql, (item["university"], item["location"], item["major_type1"], item["major_type2"], item["department"], item["degree_type"],
                                             item["degree_name"], item["degree_overview_en"], item["programme_en"], item["overview_en"], item["teach_time"],
                                             item["start_date"], item["duration"], item["duration_per"], item["modules_en"], item["career_en"],
                                             item["application_open_date"], item["deadline"], item["apply_pre"], item["apply_fee"], item["tuition_fee_pre"],
                                             item["tuition_fee"], item["rntry_requirements_en"], item["degree_requirements"], item["major_requirements"],
                                             item["professional_background"], item["average_score"], item["ielts_desc"], item["ielts"], item["ielts_l"], item["ielts_s"],
                                             item["ielts_r"], item["ielts_w"], item["toefl_code"], item["toefl_desc"], item["toefl"], item["toefl_l"], item["toefl_s"],
                                             item["toefl_r"], item["toefl_w"], item["work_experience_desc_en"], item["interview_desc_en"], item["portfolio_desc_en"],
                                             item["apply_desc_en"], item["apply_documents_en"], item["apply_proces_en"], item["other"], item["url"], item["gatherer"],
                                             item["batch_number"], item["update_time"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
            with open("scrapySchool_Australian_yan/mysqlerror/"+item['university'] + str(item['degree_type']) + "_sql.txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n"+item['url']+"\n========================\n")
        # self.cursor.close()
        # self.db.close()
        return item
