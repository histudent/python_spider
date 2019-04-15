# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/21 18:47'
import os
import pymysql
conn = pymysql.connect(
    host='192.168.1.115',port=3306,user='shuju_qx',passwd='123456',db='hooli_study_gather',charset='utf8')
cur = conn.cursor()

cur.execute('select * from au_ben_chai')
data = cur.fetchall()
for i in data:

    if ',' in i[3] and ',' in i[12] :
        location_i = i[3].split(',')
        programme_en = i[12].split(',')
        programme_cn = i[13].split(',')
        for m  in location_i:
            location_ss1 = m.strip()
            for j,k in zip(programme_en,programme_cn):
                programme_en_ss1 = j.strip()
                programme_cn_ss1 = k.strip()
                # print(location_ss1,programme_en_ss1)
                insert_sql1 = "insert into au_ben_chai_copy(id,sid,university,location,major_type1,major_type2,department,degree_type,degree_name_en,degree_name_cn,degree_overview_en,degree_overview_cn,programme_en,programme_cn,overview_en,overview_cn,start_date,duration,duration_per,modules_en,modules_cn,career_en,career_cn,application_open_date,deadline,apply_pre,apply_fee,tuition_fee_pre,tuition_fee,rntry_requirements_en,rntry_requirements_cn,degree_requirements,major_requirements,professional_background,average_score,ielts_desc,ielts,ielts_l,ielts_s,ielts_r,ielts_w,toefl_code,toefl_desc,toefl,toefl_l,toefl_s,toefl_r,toefl_w,china_score_requirements,interview_desc_en,interview_desc_cn,portfolio_desc_en,portfolio_desc_cn,apply_documents_en,apply_documents_cn,apply_desc_en,apply_desc_cn,apply_proces_en,apply_proces_cn,other,url,gatherer,batch_number,finishing,create_time,update_time,import_status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cur.execute(insert_sql1,(i[0],i[1],i[2],location_ss1,i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],programme_en_ss1,programme_cn_ss1,i[14],i[15],i[16],i[17],i[18],i[19],i[20],i[21],i[22],i[23],i[24],i[25],i[26],i[27],i[28],i[29],i[30],i[31],i[32],i[33],i[34],i[35],i[36],i[37],i[38],i[39],i[40],i[41],i[42],i[43],i[44],i[45],i[46],i[47],i[48],i[49],i[50],i[51],i[52],i[53],i[54],i[55],i[56],i[57],i[58],i[59],i[60],i[61],i[62],i[63],i[64],i[65],i[66]))
                conn.commit()
                print('插入成功from1')
    elif ',' in i[3]:
        location_i = i[3].split(',')
        for m in location_i:
            location_ss2 = m.strip()
            insert_sql2 = "insert into au_ben_chai_copy(id,sid,university,location,major_type1,major_type2,department,degree_type,degree_name_en,degree_name_cn,degree_overview_en,degree_overview_cn,programme_en,programme_cn,overview_en,overview_cn,start_date,duration,duration_per,modules_en,modules_cn,career_en,career_cn,application_open_date,deadline,apply_pre,apply_fee,tuition_fee_pre,tuition_fee,rntry_requirements_en,rntry_requirements_cn,degree_requirements,major_requirements,professional_background,average_score,ielts_desc,ielts,ielts_l,ielts_s,ielts_r,ielts_w,toefl_code,toefl_desc,toefl,toefl_l,toefl_s,toefl_r,toefl_w,china_score_requirements,interview_desc_en,interview_desc_cn,portfolio_desc_en,portfolio_desc_cn,apply_documents_en,apply_documents_cn,apply_desc_en,apply_desc_cn,apply_proces_en,apply_proces_cn,other,url,gatherer,batch_number,finishing,create_time,update_time,import_status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(insert_sql2, (i[0],i[1],i[2],location_ss2,i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17],i[18],i[19],i[20],i[21],i[22],i[23],i[24],i[25],i[26],i[27],i[28],i[29],i[30],i[31],i[32],i[33],i[34],i[35],i[36],i[37],i[38],i[39],i[40],i[41],i[42],i[43],i[44],i[45],i[46],i[47],i[48],i[49],i[50],i[51],i[52],i[53],i[54],i[55],i[56],i[57],i[58],i[59],i[60],i[61],i[62],i[63],i[64],i[65],i[66]))
            conn.commit()
            print('插入成功from2')

    elif ',' in i[12]:
        programme_en = i[12].split(',')
        programme_cn = i[13].split(',')
        for m,k in zip(programme_en,programme_cn):
            programme_en_ss3 = m.strip()
            programme_cn_ss3 = k.strip()
            insert_sql3 = "insert into au_ben_chai_copy(id,sid,university,location,major_type1,major_type2,department,degree_type,degree_name_en,degree_name_cn,degree_overview_en,degree_overview_cn,programme_en,programme_cn,overview_en,overview_cn,start_date,duration,duration_per,modules_en,modules_cn,career_en,career_cn,application_open_date,deadline,apply_pre,apply_fee,tuition_fee_pre,tuition_fee,rntry_requirements_en,rntry_requirements_cn,degree_requirements,major_requirements,professional_background,average_score,ielts_desc,ielts,ielts_l,ielts_s,ielts_r,ielts_w,toefl_code,toefl_desc,toefl,toefl_l,toefl_s,toefl_r,toefl_w,china_score_requirements,interview_desc_en,interview_desc_cn,portfolio_desc_en,portfolio_desc_cn,apply_documents_en,apply_documents_cn,apply_desc_en,apply_desc_cn,apply_proces_en,apply_proces_cn,other,url,gatherer,batch_number,finishing,create_time,update_time,import_status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(insert_sql3, (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],programme_en_ss3,programme_cn_ss3,i[14],i[15],i[16],i[17],i[18],i[19],i[20],i[21],i[22],i[23],i[24],i[25],i[26],i[27],i[28],i[29],i[30],i[31],i[32],i[33],i[34],i[35],i[36],i[37],i[38],i[39],i[40],i[41],i[42],i[43],i[44],i[45],i[46],i[47],i[48],i[49],i[50],i[51],i[52],i[53],i[54],i[55],i[56],i[57],i[58],i[59],i[60],i[61],i[62],i[63],i[64],i[65],i[66]))
            conn.commit()
            print('插入成功from3')
    else:pass
