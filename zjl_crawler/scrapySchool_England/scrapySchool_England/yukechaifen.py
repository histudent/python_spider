# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/22 14:13'
import os
import pymysql
conn = pymysql.connect(
    host='192.168.1.115',port=3306,user='zhangjianlin',passwd='zhangjianlin',db='yuke_next',charset='utf8')
cur = conn.cursor()

cur.execute('select next_id from tmp_uk_ben_yuke_61 where next_id is not NULL ')
data = cur.fetchall()
list1= []
for Next_id_a in data:
    Next_id_num = Next_id_a
    Next_id_num = Next_id_num[0].split(',')
    for i in Next_id_num:
        list1.append(i)

# for j in list1:

# cur.execute('select * from tmp_yuke')
# data2 = cur.fetchall()
# next_major = []
#
# for k in list_id:
#     id_index = k
#
#     for j in data2:
#         if j[0] == id_index:
#             next_major.append(j[5])
#
# list_major = []
# for next_major_a in next_major:
#     # print(next_major_a)
#     if ',' in next_major_a:
#         next_major_num = next_major_a.split(',')
#         for q in next_major_num:
#             print(q)
#
#


