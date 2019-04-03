# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

# 2018/06/12    表tmp_school_major_uk
# class ScrapyschoolEnglandPipeline(object):
#     db = pymysql.connect('192.168.0.125', 'root', '123456', 'hoolischool', charset='utf8')
#     cursor = db.cursor()
#     def process_item(self, item, spider):
#         # 如果是第一次抓取这所学校，抓取批次batch_number默认为 1 插入数据库
#         # 不是第一次抓取，根据学校名和url查询这个数据库的表，
#         # select_sql = "select batch_number from tmp_school_major_uk where tmp_school_major_uk.university=" + '"' + item['university'] +'" AND tmp_school_major_uk.url='+ '"' + item['url'] +'"'
#         # print(select_sql)
#         select_max_sql = "select max(batch_number) from tmp_school_major_uk where tmp_school_major_uk.university=" + '"' + item[
#             'university'] + '" AND tmp_school_major_uk.url=' + '"' + item['url'] + '"'
#         # print(select_max_sql)
#         insert_sql = "insert into tmp_school_major_uk(university, country, location, website, department, programme, " \
#               "major_type, degree_level, degree_type, full_time, taught, ucas_code, application_date, deadline, " \
#               "start_date, overview, duration, modules, application_fee, tuition_fee, teaching_assessment, career, " \
#               "academic_requirements, entry_requirements, chinese_requirements, accredited_university, Alevel, IB, " \
#               "GRE, GMAT, IELTS, IELTS_L, IELTS_S, IELTS_R, IELTS_W, TOEFL_code, TOEFL, TOEFL_L, TOEFL_S, TOEFL_R, " \
#               "TOEFL_W, interview, portfolio, application_documents, how_to_apply, school_test, SATRelated, other, " \
#               "working_experience, url, teacher_name, create_time, create_person, spiderman, update_person, " \
#               "status, import_status, sid, did, pid, batch_number) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
#               "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
#               "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#         try:
#             self.cursor.execute(select_max_sql)
#             batch_number_max_list = self.cursor.fetchall()
#             # print("查询出来最大的batch_number数据：", batch_number_max_list)
#             for i in batch_number_max_list:
#                 # print(i[0] is not None)
#                 if i[0] is not None:
#                     item['batch_number'] = i[0] + 1
#             # print("item['batch_number']: ", item['batch_number'])
#             self.cursor.execute(insert_sql, (item["university"], item["country"], item["location"], item["website"],
#                                       item["department"], item["programme"], item["major_type"], item["degree_level"],
#                                       item["degree_type"], item["full_time"], item["taught"], item["ucas_code"],
#                                       item["application_date"], item["deadline"], item["start_date"], item["overview"],
#                                       item["duration"], item["modules"], item["application_fee"], item["tuition_fee"],
#                                       item["teaching_assessment"], item["career"], item["academic_requirements"],
#                                       item["entry_requirements"], item["chinese_requirements"], item["accredited_university"],
#                                       item["Alevel"], item["IB"], item["GRE"], item["GMAT"], item["IELTS"], item["IELTS_L"],
#                                       item["IELTS_S"], item["IELTS_R"], item["IELTS_W"], item["TOEFL_code"], item["TOEFL"],
#                                       item["TOEFL_L"], item["TOEFL_S"], item["TOEFL_R"], item["TOEFL_W"], item["interview"],
#                                       item["portfolio"], item["application_documents"], item["how_to_apply"], item["school_test"],
#                                       item["SATRelated"], item["other"], item["working_experience"], item["url"], item["teacher_name"],
#                                       item["create_time"], item["create_person"], item["spiderman"],
#                                       item["update_person"], item["status"], item["import_status"], item["sid"], item["did"],
#                                       item["pid"], item["batch_number"]))
#             self.db.commit()
#             print("数据插入成功")
#         except Exception as e:
#             self.db.rollback()
#             print("数据插入失败：%s" % (str(e)))
#             with open("./mysqlerror/" + item['university'] + str(item['degree_level']) + ".txt", 'a', encoding="utf-8") as f:
#                 f.write(str(e) + "\n"+item['url']+"\n========================"+str(item['create_time'])+"\n")
#         # self.cursor.close()
#         # self.db.close()
#         return item

# 2018/06/26    表tmp_school_uk_yan
class ScrapyschoolEnglandPipeline1(object):
    # db = pymysql.connect('192.168.0.125', 'root', '123456', 'hoolischool', charset='utf8')
    # 192.168.1.115     shiqiyu    hooli888
    db = pymysql.connect('172.16.10.71', 'shiqiyu', 'hooli888', 'hooli_school', charset='utf8')
    cursor = db.cursor()

    count = 1  # 控制最大的批次号不变
    batch_number = 1
    def process_item(self, item, spider):
        # 如果是第一次抓取这所学校，抓取批次batch_number默认为 1 插入数据库
        # 不是第一次抓取，根据学校名和url查询这个数据库的表，
        # select_max_sql = "select max(batch_number) from tmp_school_uk_yan where tmp_school_uk_yan.university=" + '"' + item[
        #     'university'] + '" AND tmp_school_uk_yan.url=' + '"' + item['url'] + '"'
        select_max_sql = "select max(batch_number) from tmp_school_uk_yan where tmp_school_uk_yan.university=" + '"' + \
                         item['university'] + '"'
        # print(select_max_sql)
        insert_sql = "insert into tmp_school_uk_yan(university, location, department, programme_en, degree_type, degree_name, " \
                     "start_date, overview_en, teach_time, teach_type, duration, duration_per, modules_en, assessment_en, " \
                     "career_en, tuition_fee_pre, tuition_fee, require_chinese_en, require_chinese_school_en, rntry_requirements, " \
                     "degree_requirements, major_requirements, professional_background, ielts_desc, ielts, ielts_l, ielts_s, " \
                     "ielts_r, ielts_w, toefl_code, toefl_desc, toefl, toefl_l, toefl_s, toefl_r, toefl_w, gre, gmat, gre_sub, " \
                     "lsat, mcat, work_experience_desc_en, application_open_date, deadline, apply_pre, apply_fee, interview_desc_en, " \
                     "portfolio_desc_en, apply_desc_en, apply_documents_en, apply_proces_en, other, url, gatherer, batch_number, " \
                     "update_time) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                     "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                     "%s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
            self.cursor.execute(insert_sql, (item["university"], item["location"], item["department"], item["programme_en"],
                                             item["degree_type"], item['degree_name'], item["start_date"], item["overview_en"], item["teach_time"],
                                             item["teach_type"], item["duration"], item["duration_per"], item["modules_en"],
                                             item["assessment_en"], item["career_en"], item["tuition_fee_pre"], item["tuition_fee"],
                                             item["require_chinese_en"], item["require_chinese_school_en"], item["rntry_requirements"],
                                             item["degree_requirements"], item["major_requirements"], item["professional_background"],
                                             item["ielts_desc"], item["ielts"], item["ielts_l"], item["ielts_s"], item["ielts_r"],
                                             item["ielts_w"], item["toefl_code"], item["toefl_desc"], item["toefl"], item["toefl_l"],
                                             item["toefl_s"], item["toefl_r"], item["toefl_w"], item["gre"], item["gmat"], item["gre_sub"],
                                             item["lsat"], item["mcat"], item["work_experience_desc_en"], item["application_open_date"],
                                             item["deadline"], item["apply_pre"], item["apply_fee"], item["interview_desc_en"],
                                             item["portfolio_desc_en"], item["apply_desc_en"], item["apply_documents_en"], item["apply_proces_en"],
                                             item["other"], item["url"], item["gatherer"], item["batch_number"],
                                             item["update_time"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
            with open("scrapySchool_England/mysqlerror/" + item['university'] + str(item['degree_type']) + "_sql.txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n"+item['url']+"\n========================\n")
        # self.cursor.close()
        # self.db.close()
        return item
