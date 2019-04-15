import pymysql

class YangSql():
    def __init__(self, host, username, passwd, dbName):
        self.host = host
        self.username = username
        self.passwd = passwd
        self.dbName = dbName

    def connect(self):
        self.db = pymysql.connect(self.host, self.username, self.passwd, self.dbName)
        self.cursor = self.db.cursor()


    def close(self):
        self.cursor.close()
        self.db.close()

    # 查询数据,返回一个元组，一个一个的获取
    def find_one(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            self.row = self.cursor.fetchone()
            self.row1 = self.cursor.fetchone()
            print("---", self.row1)
            self.close()
        except Exception as e:
            print("查询失败")
            with open("./mysqlerror/rentFind_one.txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n========================")
        return self.row

    # def conn(self, sql):
    #     self.connect()
    # 查询数据,返回一个元组，一个一个的获取
    def find_many(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            self.row = self.cursor.fetchmany(10)
            # self.row1 = self.cursor.fetchmany(10)
            self.close()
        except Exception as e:
            print("查询失败")
            with open("./mysqlerror/rentFind_many.txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n========================")
        return self.row

    # 查询数据返回整个的返回的行
    def find_all(self, sql):
        rowtuple =()
        try:
            self.connect()
            self.cursor.execute(sql)
            rowtuple = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print("查询失败")
            with open("./mysqlerror/rentFind_all.txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n========================")
        return rowtuple

    def insert(self, sql):
        return self.__edit(sql)
    def delete(self, sql):
        return self.__edit(sql)
    def update(self, sql):
        return self.__edit(sql)

    def __edit(self, sql):
        count = 0
        try:
            self.connect()
            # count影响了多少行，即返回execute()方法影响的行数
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except Exception as e:
            print("事物提交失败")
            with open("./mysqlerror/rentUpdate.txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n========================")
            self.db.rollback()
        return count