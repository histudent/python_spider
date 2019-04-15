# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class Test1Pipeline(object):
    def process_item(self, item, spider):
        return item
class MysqlPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect('192.168.1.115','shiqiyu','hooli888','hooli_school',charset='utf8')
        self.cursor = self.conn.cursor()

    # def __init__(self):
    #     self.conn = pymysql.connect('192.168.0.125', 'root', '123456', 'hoolischool', charset='utf8')
    #     self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        pass
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
class ENSCPipeline(MysqlPipeline):
    def process_item(self,item,spider):
        sql = "insert into tmp_school_uk_ben( university, location, department,programme_en, degree_type, degree_name, start_date, overview_en, duration, modules_en,career_en, tuition_fee_pre, tuition_fee,ielts_desc, ielts, ielts_l, ielts_s, ielts_r, ielts_w, toefl_code, toefl_desc, toefl, toefl_l, toefl_s, toefl_r, toefl_w, application_open_date, deadline, apply_pre, apply_fee, interview_desc_en, portfolio_desc_en, apply_desc_en, apply_documents_en, apply_proces_en, other, url, gatherer, batch_number, update_time,alevel,ib,ucascode,assessment_en) values( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)"
        data = (item["university"], item["location"], item["department"], item["programme_en"],item["degree_type"], item['degree_name'], item["start_date"], item["overview_en"],
                                 item["duration"], item["modules_en"],
                                 item["career_en"], item["tuition_fee_pre"], item["tuition_fee"],
                                 item["ielts_desc"], item["ielts"], item["ielts_l"], item["ielts_s"], item["ielts_r"],
                                 item["ielts_w"], item["toefl_code"], item["toefl_desc"], item["toefl"],
                                 item["toefl_l"],
                                 item["toefl_s"], item["toefl_r"], item["toefl_w"],
                                 item["application_open_date"],
                                 item["deadline"], item["apply_pre"], item["apply_fee"], item["interview_desc_en"],
                                 item["portfolio_desc_en"], item["apply_desc_en"], item["apply_documents_en"],
                                 item["apply_proces_en"],
                                 item["other"], item["url"], item["gatherer"], item["batch_number"],
                                 item["update_time"],item["alevel"],item['ib'],item['ucascode'],item["assessment_en"])

    #def process_item(self, item, spider):
        # sql = "insert into tmp_school_uk_yan( university, location, department,programme_en, degree_type, degree_name, start_date, overview_en, duration, modules_en,career_en, tuition_fee_pre, tuition_fee,ielts_desc, ielts, ielts_l, ielts_s, ielts_r, ielts_w, toefl_code, toefl_desc, toefl, toefl_l, toefl_s, toefl_r, toefl_w, application_open_date, deadline, apply_pre, apply_fee, interview_desc_en, portfolio_desc_en, apply_desc_en, apply_documents_en, apply_proces_en, other, url, gatherer, batch_number, update_time,rntry_requirements,require_chinese_en,assessment_en,teach_type,teach_time) values( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s)"
        # data = (item["university"], item["location"], item["department"], item["programme_en"], item["degree_type"],
        #         item['degree_name'], item["start_date"], item["overview_en"],
        #         item["duration"], item["modules_en"],
        #         item["career_en"], item["tuition_fee_pre"], item["tuition_fee"],
        #         item["ielts_desc"], item["ielts"], item["ielts_l"], item["ielts_s"], item["ielts_r"],
        #         item["ielts_w"], item["toefl_code"], item["toefl_desc"], item["toefl"],
        #         item["toefl_l"],
        #         item["toefl_s"], item["toefl_r"], item["toefl_w"],
        #         item["application_open_date"],
        #         item["deadline"], item["apply_pre"], item["apply_fee"], item["interview_desc_en"],
        #         item["portfolio_desc_en"], item["apply_desc_en"], item["apply_documents_en"],
        #         item["apply_proces_en"],
        #         item["other"], item["url"], item["gatherer"], item["batch_number"],
        #         item["update_time"], item["rntry_requirements"], item["require_chinese_en"],item["assessment_en"],item["teach_type"],item["teach_time"])

    # def process_item(self, item, spider):
    #     sql = "insert into weihongbo_url(name_name,url) values(%s, %s)"
    #     data = (item["name_name"], item["url"])

        try:
            self.cursor.execute(sql,data)
            self.conn.commit()
        except Exception as e:
            print('插入失败',e)
            self.conn.rollback()


        return item
