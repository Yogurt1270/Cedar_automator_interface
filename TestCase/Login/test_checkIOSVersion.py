#!/usr/local/bin/python
# coding:utf-8

import requests
import json
import pymysql


class CheckIOSVersion:
    requrl = "https://functest.junhuahomes.com/imapi/base/checkIOSVersion"
    para = {
        "Imei": "be7faff4f79bsetupf9ad62db1cd26053eccd184674",
        "apiVersion": "1.3.0",
        "channel": "",
        "currentVer": "3.0.0",
        "Login": "",
        "phoneName": "iPhone",
        "platform": "ios",
        "platformVersion": "10.3.2",
        "system": "iOS"
    }


cv = CheckIOSVersion()


def setup():
    print("------test start------")
    print(cv.para['currentVer'])
    req = requests.post(url=cv.requrl, data=cv.para, verify=False)
    return req


def teardown():
    print("------test end------")


# 从数据库返回需要进行参数化的参数
# def query():
#     db = pymysql.connect("localhost", "root", "yangyang0216", "new_test")
#
#     cursor = db.cursor()
#     sql = "SELECT age FROM new_test.EMPLOYEE \
#         WHERE age >= '%d'" % 20
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     for row in results:
#         version = row[0]
#
#         print(type("%s" % version))
#     return results
#
#     db.close()

def test_newVersion():
    res = json.loads(setup().text)
    # print(res)
    assert res['message'] == "已经是最新版本", "新版本更新失败"


def test_oldVersio():
    res = json.loads(setup().text)
    # print(res)
    assert res['updatePlan'] == "PROMPT_UPDATE", "新版本更新失败"


if cv.para['currentVer'] == "3.0.0":
    test_newVersion()
else:
    test_oldVersio()


# 根据参数判断调用哪个接口
# for i in cv.para['currentVer']:
# try:
#     if cv.para['currentVer'] == '3.0.0':
#         test_newVersion()
#     else:
#         test_oldVersio()
# except KeyError:
#     print("currentVer is abnormal")
