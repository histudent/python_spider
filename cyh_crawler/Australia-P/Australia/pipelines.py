# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class AustraliaPipeline(object):
    db = pymysql.connect(host='172.16.10.71', user='python_team', passwd='shiqiyu', db='hooli_school', charset='utf8')
    cursor = db.cursor()
    count = 1  # 控制最大的批次号不变
    batch_number = 1
    def process_item(self, item, spider):
        # 如果是第一次抓取这所学校，抓取批次batch_number默认为 1 插入数据库
        # 不是第一次抓取，根据学校名和url查询这个数据库的表，
        # select_max_sql = "select max(batch_number) from tmp_school_uk_yan where tmp_school_uk_yan.university=" + '"' + item[
        #     'university'] + '" AND tmp_school_uk_yan.url=' + '"' + item['url'] + '"'
        select_max_sql = "select max(batch_number) from tmp_school_au_yan where tmp_school_au_yan.university=" + '"' + \
                         item['university'] + '"'
        # print(select_max_sql)
        insert_sql = "insert into tmp_school_au_yan(university,location,major_type1,major_type2,department,degree_type,degree_name,degree_overview_en,degree_overview_cn,programme_en,programme_cn,overview_en,overview_cn,start_date,duration,duration_per,modules_en,modules_cn,career_en,career_cn,application_open_date,deadline,apply_pre,apply_fee,tuition_fee_pre,tuition_fee,rntry_requirements_en,rntry_requirements_cn,degree_requirements,major_requirements,professional_background,average_score,ielts_desc,ielts,ielts_l,ielts_s,ielts_r,ielts_w,toefl_code,toefl_desc,toefl,toefl_l,toefl_s,toefl_r,toefl_w,interview_desc_en,interview_desc_cn,portfolio_desc_en,portfolio_desc_cn,apply_documents_en,apply_documents_cn,apply_desc_en,apply_desc_cn,apply_proces_en,apply_proces_cn,other,url,gatherer,batch_number,finishing,create_time,update_time,import_status) " \
                     "values(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s," \
                     "%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s," \
                     "%s, %s, %s, %s, %s,%s, %s, %s)"
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
            self.cursor.execute(insert_sql, (item['university'],item['location'],item['major_type1'],item['major_type2'],item['department'],item['degree_type'],item['degree_name'],item['degree_overview_en'],item['degree_overview_cn'],item['programme_en'],item['programme_cn'],item['overview_en'],item['overview_cn'],item['start_date'],item['duration'],item['duration_per'],item['modules_en'],item['modules_cn'],item['career_en'],item['career_cn'],item['application_open_date'],item['deadline'],item['apply_pre'],item['apply_fee'],item['tuition_fee_pre'],item['tuition_fee'],item['rntry_requirements_en'],item['rntry_requirements_cn'],item['degree_requirements'],item['major_requirements'],item['professional_background'],item['average_score'],item['ielts_desc'],item['ielts'],item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w'],item['toefl_code'],item['toefl_desc'],item['toefl'],item['toefl_l'],item['toefl_s'],item['toefl_r'],item['toefl_w'],item['interview_desc_en'],item['interview_desc_cn'],item['portfolio_desc_en'],item['portfolio_desc_cn'],item['apply_documents_en'],item['apply_documents_cn'],item['apply_desc_en'],item['apply_desc_cn'],item['apply_proces_en'],item['apply_proces_cn'],item['other'],item['url'],item['gatherer'],item['batch_number'],item['finishing'],item['create_time'],item['update_time'],item['import_status']))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
            with open("./" + item['university'] + ".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n"+item['url']+"\n========================\n")
        # self.cursor.close()
        # self.db.close()
        return item


# class MysqlDB(object):
#     def __init__(self):
#         try:
#             self.conn = pymysql.connect('192.168.0.125','root','123456','hoolischool',charset='utf8')
#             self.cursor = self.conn.cursor()
#         except Exception as e:
#             print('连接数据库失败：%s'% str(e))
#
#     def close(self):
#         self.cursor.close()
#         self.conn.close()

# class ScrapyschoolEnglandPipeline1(MysqlDB):
#     def process_item(self, item, spider):
#         sql = 'insert into gaokaopai(zhuangye,xuekeleibie,zhuangyeleibie,zhuangyedaima,kaishekecheng,school_name)' \
#               'VALUES (%s,%s,%s,%s,%s,%s) '
#               # 'on duplicate key update department = values (department),type=VALUES (type),modules = values (modules),entry_requirements = values(entry_requirements),location = values(location),programme = values(programme),teaching_assessment = values(teaching_assessment),degree_type = values(degree_type),tuition_fee= values(tuition_fee),duration= VALUES (duration),start_date=VALUES (start_date),IELTS=VALUES (IELTS),TOEFL = values(TOEFL),start_date=VALUES (start_date),ucas_code=VALUES (ucas_code)'
#         try:
#             self.cursor.execute(sql, (
#                 item['zhuanye'],item['xuekeleibie'],item['zhuanyeleibie'],item['zhuanyedaima'],item['kaishekecheng'],item['schoolname']
#             ))
#             self.conn.commit()
#         except Exception as e:
#             self.conn.rollback()
#             print(e)
#             print("执行sql语句失败")
#
#         return item