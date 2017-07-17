#!/usr/local/bin/python env
# coding:utf-8

import requests
import json


class CheckNum:
    request_url = "https://functest.junhuahomes.com/imapi/user/checkNum"
    para = {
        "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
        "apiVersion": "1.3.0",
        "channel": "",
        "currentCommunityId": "",
        "currentVer": "3.0.0",
        "dscd": "",
        "Login": "",
        "mobile": "15901293186",
        "phoneName": "iPhone",
        "platform": "ios",
        "platformVersion": "10.3.2",
        "system": "iOS",
        "validatecode": "1234",
        "xgToken": "191e35f7e0731cc5080"
    }


cn = CheckNum()


def setup():
    print("------test start------")
    req = requests.post(url=cn.request_url, data=cn.para, verify=False)
    return req


def teardown():
    print("------test end------")


# 使用已认证手机号登录APP
def test_login():
    res = json.loads(setup().text)
    assert res['userPhone'] == '13718591270'


# 使用"未认证"手机号登录APP
def test_login_001():
    res = json.loads(setup().text)
    assert res['communityId']
