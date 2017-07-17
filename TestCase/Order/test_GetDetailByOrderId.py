#!/usr/local/bin/python env
# coding:utf-8

import requests
import json


class TestGetDetailByOrderId:
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
        return token

    # 获取订单详情
    def test_oderdetail(self):
        url = "https://functest.junhuahomes.com/imapi/homeRepair/getDetailByOrderId"
        para = {
            "login": self.test_CheckNumWithAuth(),
            "orderId": "741824fa4b3549f3bfa05ffd86b75e1c"
        }
        req = requests.post(url=url, data=para, verify=False)
        res = json.loads(req.text)
        assert res['orderId']
