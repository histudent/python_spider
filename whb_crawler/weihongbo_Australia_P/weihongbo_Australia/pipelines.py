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
        self.conn = pymysql.connect('172.16.10.71','shiqiyu','hooli888','hooli_school',charset='utf8')
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
    # def process_item(self,item,spider):
    #     sql = "insert into tmp_school_au_ben(university,location,department,degree_type,degree_name_en,degree_overview_en,programme_en,overview_en,start_date,duration,duration_per,modules_en,career_en,application_open_date,deadline,apply_pre,apply_fee,tuition_fee_pre,tuition_fee,rntry_requirements_en,degree_requirements,major_requirements,professional_background,average_score,ielts_desc,ielts,ielts_l,ielts_s,ielts_r,ielts_w,toefl_code,toefl_desc,toefl,toefl_l,toefl_s,toefl_r,toefl_w,china_score_requirements,interview_desc_en,portfolio_desc_en,apply_documents_en,apply_desc_en,apply_proces_en,other,url,gatherer,batch_number,finishing,create_time,update_time,) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #     data = ( item["university"], item["location"], item["department"], item["degree_type"], item["degree_name_en"], item["degree_overview_en"], item["programme_en"], item["overview_en"], item["start_date"], item["duration"], item["duration_per"], item["modules_en"], item["career_en"], item["application_open_date"], item["deadline"], item["apply_pre"], item["apply_fee"], item["tuition_fee_pre"], item["tuition_fee"], item["rntry_requirements_en"], item["degree_requirements"], item["major_requirements"], item["professional_background"], item["average_score"], item["ielts_desc"], item["ielts"], item["ielts_l"], item["ielts_s"], item["ielts_r"], item["ielts_w"], item["toefl_code"], item["toefl_desc"], item["toefl"], item["toefl_l"], item["toefl_s"], item["toefl_r"], item["toefl_w"], item["china_score_requirements"], item["interview_desc_en"], item["portfolio_desc_en"], item["apply_documents_en"], item["apply_desc_en"], item["apply_proces_en"], item["other"], item["url"], item["gatherer"], item["batch_number"], item["finishing"], item["create_time"], item["update_time"],)

    def process_item(self, item, spider):
        sql = "insert into tmp_school_au_yan(university,location,department,degree_type,degree_name_en,degree_overview_en,programme_en,overview_en,teach_time,start_date,duration,duration_per,modules_en,career_en,application_open_date,deadline,apply_pre,apply_fee,tuition_fee_pre,tuition_fee,rntry_requirements_en,degree_requirements,major_requirements,professional_background,average_score,ielts_desc,ielts,ielts_l,ielts_s,ielts_r,ielts_w,toefl_code,toefl_desc,toefl,toefl_l,toefl_s,toefl_r,toefl_w,is_work_experience,work_experience_years,work_experience_desc_en,interview_desc_en,portfolio_desc_en,apply_desc_en,apply_documents_en,apply_proces_en,other,url,gatherer,batch_number,finishing,create_time,update_time,) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)"
        data = (item["university"],item["location"],item["department"],item["degree_type"],item["degree_name_en"],item["degree_overview_en"],item["programme_en"],item["overview_en"],item["teach_time"],item["start_date"],item["duration"],item["duration_per"],item["modules_en"],item["career_en"],item["application_open_date"],item["deadline"],item["apply_pre"],item["apply_fee"],item["tuition_fee_pre"],item["tuition_fee"],item["rntry_requirements_en"],item["degree_requirements"],item["major_requirements"],item["professional_background"],item["average_score"],item["ielts_desc"],item["ielts"],item["ielts_l"],item["ielts_s"],item["ielts_r"],item["ielts_w"],item["toefl_code"],item["toefl_desc"],item["toefl"],item["toefl_l"],item["toefl_s"],item["toefl_r"],item["toefl_w"],item["is_work_experience"],item["work_experience_years"],item["work_experience_desc_en"],item["interview_desc_en"],item["portfolio_desc_en"],item["apply_desc_en"],item["apply_documents_en"],item["apply_proces_en"],item["other"],item["url"],item["gatherer"],item["batch_number"],item["finishing"],item["create_time"],item["update_time"],)

        try:
            self.cursor.execute(sql,data)
            self.conn.commit()
        except Exception as e:
            print('插入失败',e)
            self.conn.rollback()


        return item
