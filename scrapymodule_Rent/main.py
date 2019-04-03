# -*- coding: utf-8 -*-
from scrapy import cmdline
# cmdline.execute("scrapy crawl rentAgencyKornRealEstate".split())
# cmdline.execute("scrapy crawl rentAgencyJJRealEstate".split())
# cmdline.execute("scrapy crawl rentAgencyNewTechcomMarketingEnterprisesPtyLtd".split())
# cmdline.execute("scrapy crawl rentAgency".split())

# 2018.6.21
# cmdline.execute("scrapy crawl rentZoopla".split())
# cmdline.execute("scrapy crawl rentRightmove".split())
cmdline.execute("scrapy crawl rentOpenRent".split())
# cmdline.execute("scrapy crawl rentCityRoomRentals".split())


from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from scrapymodule_Rent.mysqlyang import YangSql
import pymysql

def main():
    setting = get_project_settings()
    process = CrawlerProcess(setting)
    didntWorkSpider = ['sample']

    for spider_name in process.spiders.list():
        if spider_name in didntWorkSpider:
            continue
        print("Running spider %s" % (spider_name))
        process.crawl(spider_name)
    process.start()

# 将从数据库中取得的数据转成列表形式
def getDatalist(datatuplemode):
    datatuplemode = list(datatuplemode)
    for i in range(len(datatuplemode)):
        datatuplemode[i] = ''.join(datatuplemode[i])
    return datatuplemode

# 删除的房源信息
def rentDel(datalist1, datalist2):
    # rent中有而rent_copy中没有的  del
    deldata = list(set(datalist1).difference(set(datalist2)))
    return deldata

# 新增的房源信息
def rentAdd(datalist1, datalist2):
    # rent_copy中有而rent中没有的  add
    adddata = list(set(datalist2).difference(set(datalist1)))
    return adddata

# 处理获得的删除和增加数据，并修改各条数据字段status的值
def handle_data1():
    yang = YangSql("localhost", "root", "123456", "rentinformation")
    datatuple = yang.find_all("select url from rent")
    datatuple1 = yang.find_all("select url from rent_copy_copy")
    datalist1 = getDatalist(datatuple)
    datalist2 = getDatalist(datatuple1)
    # print("datalist1: ", datalist1)
    # print(len(datalist1))
    # print("datalist2: ", datalist2)
    # print(len(datalist2))
    print("============================================")
    deldata = rentDel(datalist1, datalist2)
    adddata = rentAdd(datalist1, datalist2)
    print("deldata: ", deldata)
    print(len(deldata))
    print("adddata: ", adddata)
    print(len(adddata))
    # 修改rent表中需要删除的数据的字段status设置为3
    delcondition = ""
    for l1 in deldata:
        if l1 == deldata[-1]:
            delcondition += "rent.url = " + "'" + l1 + "'"
        else:
            delcondition += "rent.url = " + "'" + l1 + "' or "
    print("delcondition: ", delcondition)
    # update rent set status = '3' where rent.url = "" or rent.url = ""
    delsql = "update rent set status = '3' where " + delcondition
    # yang.update(delsql)
    # 以rent_copy中新增的数据url为条件，插入的数据字段status设置为2
        # 一、需要先查询出rent_copy_copy表中新增的数据
        # 二、然后将这些新数据插入rent_copy表中
    addcondition = ""
    for a1 in adddata:
        if a1 == adddata[-1]:
            addcondition += "rent_copy_copy.url = " + "'" + a1 + "'"
        else:
            addcondition += "rent_copy_copy.url = " + "'" + a1 + "' or "
    # print("addcondition: ", addcondition)
    newAdddataCon = "select housing_type, available_time, house_name, room_type, car_spaces, lease, address, detaile_address, supporting_facilities, price, isRent, postal_code, picture, housing_introduce, supplier_type, supplier_name, supplier_logo, country, city, contact_name, contact_phone, contact_email, url, status from rent_copy_copy where " + addcondition
    newAdddata = yang.find_all(newAdddataCon)
    # print("newAdddata: ", newAdddata)
    newStr = ""
    for new in newAdddata:
        isnew = new
        new = list(new)
        new.insert(0, 0)
        new[-1] = '2'
        new = tuple(new)
        if isnew == newAdddata[-1]:
            newStr += str(new)
        else:
            newStr += str(new) +", "
    # print("newStr: ", newStr)
    # insert into rent_copy values(0,"tom",19,1,"北京",0);
    addsql = "insert into rent values" + newStr
    yang.insert(addsql)
    print("=========111==========")

# 2018/4/20修改
def handle_data():
    yang = YangSql("localhost", "root", "123456", "hoolirent")
    datatuple = yang.find_all("select url from py_rent")
    datatuple1 = yang.find_all("select url from py_rent_copy_copy")
    datalist1 = getDatalist(datatuple)
    datalist2 = getDatalist(datatuple1)
    # print("datalist1: ", datalist1)
    # print(len(datalist1))
    # print("datalist2: ", datalist2)
    # print(len(datalist2))
    print("============================================")
    deldata = rentDel(datalist1, datalist2)
    adddata = rentAdd(datalist1, datalist2)
    print("deldata: ", deldata)
    print(len(deldata))
    print("adddata: ", adddata)
    print(len(adddata))
    # 修改rent表中需要删除的数据的字段status设置为3
    delcondition = ""
    for l1 in deldata:
        if l1 == deldata[-1]:
            delcondition += "py_rent.url = " + "'" + l1 + "'"
        else:
            delcondition += "py_rent.url = " + "'" + l1 + "' or "
    # print("delcondition: ", delcondition)
    # update rent set status = '3' where rent.url = "" or rent.url = ""
    delsql = "update rent set status = '3' where " + delcondition
    # yang.update(delsql)
    # 以rent_copy中新增的数据url为条件，插入的数据字段status设置为2
        # 一、需要先查询出rent_copy_copy表中新增的数据
        # 二、然后将这些新数据插入rent_copy表中
    addcondition = ""   # 新增数据的url（查询数据库rent_copy_copy表的条件）
    for a1 in adddata:
        if a1 == adddata[-1]:
            addcondition += "py_rent_copy_copy.url = " + "'" + a1 + "'"
        else:
            addcondition += "py_rent_copy_copy.url = " + "'" + a1 + "' or "
    print("addcondition: ", addcondition)
    # with open("./mysqlerror/addcondition.txt", 'w', encoding="utf-8") as f:
    #     f.write(addcondition)
    newAdddataCon = "select housing_type, available_time, house_name, room_type, car_spaces, lease, address, detaile_address, supporting_facilities, price, isRent, postal_code, picture, housing_introduce, supplier_type, supplier_name, supplier_logo, country, city, contact_name, contact_phone, contact_email, url, status,deposit,area,floor,price_include from py_rent_copy_copy where " + addcondition
    yang = YangSql("localhost", "root", "123456", "hoolirent")
    # newAdddata = yang.find_all(newAdddataCon)
    count = 0   # 计数判断加第几条数据以及总共插入多少条数据
    # 通过find_one一条一条获取从rent_copy_copy表中查询到的新增的数据，然后一条一条的写入rent表中，就是新增的数据
    try:
        # 新建数据库连接，一条一条的查询py_rent_copy_copy中新增的数据
        db = pymysql.connect("localhost", "root", "123456", "hoolirent")
        cursor = db.cursor()
        sql = newAdddataCon
        cursor.execute(sql)

        newAdddata = cursor.fetchone()
        # print("-----", newAdddata)
        # newAdddata = cursor.fetchone()
        # print("-----1", newAdddata)
        while count < len(adddata):
            # print("newAdddata: ", newAdddata)
            count += 1
            newAdddata = list(newAdddata)
            newAdddata.insert(0, 0)
            newAdddata = str(tuple(newAdddata))
            print("newAdddata: ", newAdddata)
            addsql = "insert into py_rent values" + newAdddata
            yang.insert(addsql)
            newAdddata = cursor.fetchone()
            print("=========插入%d条=========="%(count))
        cursor.close()
        db.close()
    except Exception as e:
        print("----没有更新的数据----\n异常：", e)
    # 转换成字符串形式插入数据库
    newStr = ""
    # for new in newAdddata:
    #     isnew = new
    #     new = list(new)
    #     new.insert(0, 0)
    #     new[-1] = '2'
    #     new = tuple(new)
    #     if isnew == newAdddata[-1]:
    #         newStr += str(new)
    #     else:
    #         newStr += str(new) +", "
    # print("newStr: ", newStr)
    # addsql = "insert into rent values" + newAdddata
    # yang = YangSql("localhost", "root", "123456", "rentinformation")
    # yang.insert(addsql)
    print("=========111==========")

def deleteRentCopyCopy():
    yang = YangSql("localhost", "root", "123456", "hoolirent")
    yang.delete("delete from py_rent_copy_copy")
    print("---------------表py_rent_copy_copy数据删除成功---------------")

if __name__ == '__main__':
    # deleteRentCopyCopy()
    # main()
    # cmdline.execute("scrapy crawl rentAgency".split())
    # handle_data()
    pass
