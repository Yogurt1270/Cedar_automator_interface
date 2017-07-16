#!/usr/local/bin/python
# coding:utf-8

import requests
import json


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


def test_newVersion():
    res = json.loads(setup().text)
    print(res)
    assert res['message'] == "已经是最新版本", "新版本更新失败"


def test_oldVersio():
    res = json.loads(setup().text)
    print(res)
    assert res['updatePlan'] == "PROMPT_UPDATE", "新版本更新失败"


if cv.para['currentVer'] == '3.0.0':
    test_newVersion()
else:
    test_oldVersio()
