#!/usr/local/bin/python env
# coding:utf-8

import requests
import json


class TestGoHomePage:
    def test_CheckNumWithAuth(self):
        url = "https://functest.junhuahomes.com/imapi/user/checkNum"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentCommunityId": "",
            "currentVer": "3.0.0",
            "dscd": "",
            "login": "",
            "mobile": "13718591270",
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS",
            "validatecode": "1234",
            "xgToken": "191e35f7e0731cc5080"
        }
        request = requests.post(url, data=para, verify=False)
        res = json.loads(request.text)
        token = request.headers['login']
        # print(res)
        return token

    # 根据houseID获取
    def test_defaultaddress(self):
        url = "https://functest.junhuahomes.com/imapi/provider/goHomePage"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "communityId": "22206",
            "currentVer": "3.0.0",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS",
            "xgToken": "191e35f7e0731cc5080"
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert res['canPay'] == True

        # 根据houseID获取

    def test_communityidisnone(self):
        url = "https://functest.junhuahomes.com/imapi/provider/goHomePage"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "communityId": "",
            "currentVer": "3.0.0",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS",
            "xgToken": "191e35f7e0731cc5080"
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        # print(res)
        assert res['message'] == '小区不存在！'

    def test_communityidisnull(self):
        url = "https://functest.junhuahomes.com/imapi/provider/goHomePage"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "communityId": "null",
            "currentVer": "3.0.0",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS",
            "xgToken": "191e35f7e0731cc5080"
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        # print(res)
        assert res['message'] == '该小区还没有服务中心！'

    def test_communityidiserror(self):
        url = "https://functest.junhuahomes.com/imapi/provider/goHomePage"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "communityId": "00000",
            "currentVer": "3.0.0",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS",
            "xgToken": "191e35f7e0731cc5080"
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        # print(res)
        assert res['message'] == '该小区还没有服务中心！'
