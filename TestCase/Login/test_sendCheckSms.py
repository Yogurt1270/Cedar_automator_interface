#!/usr/local/bin/python env
# coding:utf-8

import requests
import json


class TestSendsms:
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

# 发送验证码接口
# 发送短信验证码
    def test_sendsms(self):
        url = "https://functest.junhuahomes.com/imapi/user/sendCheckSms"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "login": self.test_CheckNumWithAuth(),
            "mobile": "13718591270",
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS"
        }
        myrequest = requests.post(url, data=para, verify=False)
        myjson = json.loads(myrequest.text)
        assert myjson['message'] == "验证码已发送", "未收到短信验证码!"

        # # 发送语音验证码
        # def test_sendvoicesms(self):
        #     url = "https://functest.junhuahomes.com/imapi/user/sendCheckSms"
        #     para = {
        #         "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
        #         "apiVersion": "1.3.0",
        #         "channel": "",
        #         "currentVer": "3.0.0",
        #         "isVoice": "1",
        #         "Login": "",
        #         "mobile": "13718591270",
        #         "phoneName": "iPhone",
        #         "platform": "ios",
        #         "platformVersion": "10.3.2",
        #         "system": "iOS"
        #     }
        #     myrequest = requests.post(url, data=para, verify=False)
        #     myjson = json.loads(myrequest.text)
        #     assert myjson['message'] == "验证码已发送", "未收到短信验证码!"
