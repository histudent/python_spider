# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/8/23 10:05'
import numpy as np
import pandas as pd
import os
import pymysql

conn = pymysql.connect(
    host='localhost', port=3306, user='root', passwd='123456', db='hoolischool', charset='utf8'
)
cur = conn.cursor()
sql_order = "SELECT programme_en from au_ben_chai"
cur.execute(sql_order)
data = cur.fetchall()
flag = 0
for i in data:
    print(i)
    flag +=1
    print(flag)
list1= []
for data_column in data:
    list1.append(data_column[0])

flag_chai = 0
for values in list1:
    if ',' in values:
        values = values.split(',')
        for value in values:
            value = value.strip()
            flag_chai +=1
            print(value)
            print(flag_chai)



# if __name__ == '__main__':
#     cur = conn.cursor()
#     sql_order = "SELECT * from au_ben_chai"
#     cur.execute(sql_order)
#     tidy_split()

