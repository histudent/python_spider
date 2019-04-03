# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ScrapyschoolEnglandUPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    db = pymysql.connect(host='172.16.10.71', user='python_team', passwd='shiqiyu', db='hooli_school', charset='utf8')
    cursor = db.cursor()
    count = 1  # 控制最大的批次号不变
    batch_number = 1
    def process_item(self, item, spider):
        # 如果是第一次抓取这所学校，抓取批次batch_number默认为 1 插入数据库
        # 不是第一次抓取，根据学校名和url查询这个数据库的表，
        # select_max_sql = "select max(batch_number) from tmp_school_uk_yan where tmp_school_uk_yan.university=" + '"' + item[
        #     'university'] + '" AND tmp_school_uk_yan.url=' + '"' + item['url'] + '"'
        select_max_sql = "select max(batch_number) from tmp_school_uk_ben where tmp_school_uk_ben.university=" + '"' + \
                         item['university'] + '"'
        # print(select_max_sql)
        insert_sql = "insert into tmp_school_uk_ben(university, location, department,programme_en, degree_type, degree_name, " \
                     "start_date, overview_en, duration, duration_per, modules_en, assessment_en, " \
                     "career_en, tuition_fee_pre, tuition_fee, require_chinese_en,ucascode, " \
                     "ielts_desc, ielts, ielts_l, ielts_s, " \
                     "ielts_r, ielts_w, toefl_code, toefl_desc, toefl, toefl_l, toefl_s, toefl_r, toefl_w, application_open_date, deadline, apply_pre, apply_fee, interview_desc_en, " \
                     "portfolio_desc_en, apply_desc_en, apply_documents_en, apply_proces_en, other, url, gatherer, batch_number, " \
                     "update_time,ib,alevel,major_type1) values(%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                     "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                     "%s,%s,%s,%s)"
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
                                (item["university"], item["location"], item["department"], item["programme_en"],
                                 item["degree_type"], item['degree_name'], item["start_date"], item["overview_en"],
                                 item["duration"], item["duration_per"], item["modules_en"],
                                 item["assessment_en"], item["career_en"], item["tuition_fee_pre"], item["tuition_fee"],
                                 item["require_chinese_en"],item['ucascode'],
                                 item["ielts_desc"], item["ielts"], item["ielts_l"], item["ielts_s"], item["ielts_r"],
                                 item["ielts_w"], item["toefl_code"], item["toefl_desc"], item["toefl"],
                                 item["toefl_l"],
                                 item["toefl_s"], item["toefl_r"], item["toefl_w"],
                                 item["application_open_date"],
                                 item["deadline"], item["apply_pre"], item["apply_fee"], item["interview_desc_en"],
                                 item["portfolio_desc_en"], item["apply_desc_en"], item["apply_documents_en"],
                                 item["apply_proces_en"],
                                 item["other"], item["url"], item["gatherer"], item["batch_number"],
                                 item["update_time"],item['ib'],item['alevel'],item['major_type1']))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
            # with open("./" + item['university'] + ".txt", 'a', encoding="utf-8") as f:
            #     f.write(str(e) + "\n" + item['url'] + "\n========================\n")
        # self.cursor.close()
        # self.db.close()
        return item
