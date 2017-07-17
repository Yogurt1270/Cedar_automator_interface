#!/usr/local/bin/python env
# coding:utf-8


import pytest
import allure
import requests
import json


class TestGoHomePage:
    # 根据houseID获取
    def test_defaultaddress(self):
        url = "https://functest.junhuahomes.com/imapi/provider/goHomePage"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "communityId": "22206",
            "currentVer": "3.0.0",
            "Login": "b42c9f51ed3e4accbf54efbda3aa5de7",
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS",
            "xgToken": "191e35f7e0731cc5080"
        }
        r = requests.post(url, data=para, verify=False)
        j = json.loads(r.text)
        print(r.content.decode('utf-8'))
        # assert r.status_code == 200
        assert j['canPay'] == 'true'
