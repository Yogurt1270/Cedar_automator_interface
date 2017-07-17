#!/usr/local/bin/python env
# coding:utf-8

import requests
import json


class TestGetUnpaidBill:
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
        # self.assertIsNotNone(res['userPhone'], "用户手机号不能为空")
        return token

    # 获取费用列表
    # 获取未缴清费用列表
    def test_unpay(self):
        url = "https://functest.junhuahomes.com/imapi/fee/getUnpaidBill"
        para = {
            "login": self.test_CheckNumWithAuth(),
            "houseID": "16697",
            "paymentType": "COMMON",
            "shouldChargeDateStart": "",
            "shouldChargeDateEnd": "",
            "apiVersion": "1.3.0"
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert res['houseID']

    # 获取可预缴费用列表
    def test_prepay(self):
        url = "https://functest.junhuahomes.com/imapi/fee/getUnpaidBill"
        para = {
            "login": self.test_CheckNumWithAuth(),
            "houseID": "16697",
            "paymentType": "ADVANCE",
            "shouldChargeDateStart": "",
            "shouldChargeDateEnd": "",
            "apiVersion": "1.3.0"
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert res['houseID']

    # 按起止时间获取未缴清费用列表
    def test_prepaybydate(self):
        url = "https://functest.junhuahomes.com/imapi/fee/getUnpaidBill"
        para = {
            "login": self.test_CheckNumWithAuth(),
            "houseID": "16697",
            "paymentType": "COMMON",
            "shouldChargeDateStart": "2017-07",
            "shouldChargeDateEnd": "2017-08",
            "apiVersion": "1.3.0"
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert res['houseID']

    # 按起止日期获取可预缴费用列表
    def test_prepay(self):
        url = "https://functest.junhuahomes.com/imapi/fee/getUnpaidBill"
        para = {
            "login": self.test_CheckNumWithAuth(),
            "houseID": "16697",
            "paymentType": "ADVANCE",
            "shouldChargeDateStart": "",
            "shouldChargeDateEnd": "",
            "apiVersion": "1.3.0"
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        print(res)
        assert res['houseID']
