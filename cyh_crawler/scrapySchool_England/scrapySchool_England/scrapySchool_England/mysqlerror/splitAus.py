import pymysql

conn=pymysql.connect('192.168.1.115', 'shiqiyu', 'hooli888', 'hooli_school', charset='utf8')
corsur=conn.cursor()
results=corsur.execute('select * from tmp_school_au_ben where university="The University of Adelaide"')
text=corsur.fetchall()
#插入数据
insert_sql='insert into tmp_school_au_ben(sid,university,location,major_type1,major_type2,department,degree_type,degree_name,degree_overview_en,degree_overview_cn,programme_en,programme_cn,overview_en,overview_cn,start_date,duration,duration_per,modules_en,modules_cn,career_en,career_cn,application_open_date,deadline,apply_pre,apply_fee,tuition_fee_pre,tuition_fee,rntry_requirements_en,rntry_requirements_cn,degree_requirements,major_requirements,professional_background,average_score,ielts_desc,ielts,ielts_l,ielts_s,ielts_r,ielts_w,toefl_code,toefl_desc,toefl,toefl_l,toefl_s,toefl_r,toefl_w,china_score_requirements,interview_desc_en,interview_desc_cn,portfolio_desc_en,portfolio_desc_cn,apply_documents_en,apply_documents_cn,apply_desc_en,apply_desc_cn,apply_proces_en,apply_proces_cn,other,url,gatherer,batch_number,finishing,create_time,update_time,import_status) VALUES ' \
           '(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
nums=len(text)

#思路，首先通过sql查询获取要操作的数据，查询结果是元组，通过元组的索引将数据逐条取出并转成列表
#通过列表的索引确定要拆开的字段，将字段通过特定规则拆开
#遍历拆开的结果,逐条存入数据库
#ziduan_index(用于定位要拆分的字段)
#guize(拆分的标志，例如',')
#chaxunjieguo(要拆分的学校数据)
def chaiziduan(ziduan_index,guize,chaxunjieguo):
    n=0
    while n<len(chaxunjieguo):
        yitiaoshuju=list(chaxunjieguo[n])
        n=n+1
        #定义一个变量接收数据，用于修改，最后入库
        date=yitiaoshuju
        #要拆的字段
        ziduan=yitiaoshuju[ziduan_index].split(guize)
        if len(ziduan)!=1:
            for i in ziduan:
                date[ziduan_index]=i
                try:
                    corsur.execute(insert_sql, date[1:])
                    conn.commit()
                    print('插入成功')
                    # print(split_date)
                except Exception as e:
                    conn.rollback()
                    print('插入失败 %s' % (str(e)))

n = 0
while n<nums:
    #接受一条数据，转成列表，通过索引可以进行定位和修改
    date=list(text[n])
    n=n+1
    #定义一个变量split_date接收数据，并进行修改，最后用于存库
    split_date=date
    #专业名在列表中的索引是11，通过索引进行定位，然后遍历
    progremme=date[11].split(',')
    start_date=date[15].split(',')
    url=date[-7]
    if len(progremme)!=1:
        for i in progremme:
            #其他的数据不变，只改变列表中专业名的内容
            split_date[11]=i
            # print(split_date[11])
            if len(start_date)==2:
                for j in  start_date:
                    split_date[15]=j
                    # print(split_date[15])
                    if split_date[15]=='2月':
                        split_date[23]='12月1日'
                    elif split_date[15]=='7月':
                        split_date[23]='5月1日'
                    try:
                        corsur.execute(insert_sql, split_date[1:])
                        conn.commit()
                        print('插入成功')
                        # print(split_date)
                    except Exception as e:
                        conn.rollback()
                        print('插入失败 %s' % (str(e)))
    else:
        split_date[11]=''.join(progremme)
        if len(start_date) == 2:
            for j in start_date:
                split_date[15] = j
                # print(split_date[15])
                if split_date[15] == '2月':
                    split_date[23] = '12月1日'
                elif split_date[15] == '7月':
                    split_date[23] = '5月1日'
                try:
                    corsur.execute(insert_sql, split_date[1:])
                    conn.commit()
                    print('插入成功')
                    # print(split_date)
                except Exception as e:
                    conn.rollback()
                    print('插入失败 %s' % (str(e)))
conn.close()