#!/usr/local/bin/python env
# coding:utf-8

import requests
import json


class TestFeedback:
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

        # # 打开意见反馈页
        # def test_openfeedback(self):
        #     url = "https://functest.junhuahomes.com/imapi/h5/index.html"
        #     para = {
        #         "time": "1499323842752",
        #         "version": "3.0.0",
        #         "login": self.test_CheckNumWithAuth(),
        #         "communityId": "22206"
        #     }
        #     req = requests.get(url, data=para, verify=False)
        #     res = json.loads(req.content)
        #     print(res)
