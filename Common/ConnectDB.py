#!/usr/local/bin/python
# coding:utf-8


import pymysql

# 创建数据库连接
db = pymysql.connect("localhost", "root", "yangyang0216", "new_test")

# config = {
#     "host": "localhost",
#     "port": "3306",
#     "user": "root",
#     "password": "yangyang0216",
#     "db": "new_test"
# }
# db = pymysql.connect()

cursor = db.cursor()

# # 创建表
# cursor.execute("DROP TABLE IF EXISTS Version")
#
# sql = """create table Version(
# currentVer char(20),
# Imei char(50),
# phoneName char(20),
# platform char(20),
# platformVersion char(20),
# system char(20)
# )"""
#
# cursor.execute(sql)

sql = "SELECT age FROM new_test.EMPLOYEE \
    WHERE age >= '%d'" % 20
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    version = row[0]

    print(("%s" % version))
print(version)

# cursor.execute("SELECT VERSION()")
#
# data = cursor.fetchone()
#
# print("Database version : %s" % data)

# 关闭数据库连接
db.close()
