#!/usr/local/bin/python env
# coding:utf-8

import pytest
import requests
import json
import Common


# 发送验证码接口
# 发送短信验证码
def test_sendsms():
    mycookie = {
        "JSESSIONID": Common.GetMyToken.getjsessionid(),
        "cloudwise_client_id": "7c80d1db-a61f-56f5-9787-8cf7d528705c",
        "gr_user_id": "7ed06d26-a6e4-4045-9cde-5fe914dd6f8d"
    }
    myheader = {
        "User-Agent": "propertyApp/3.0.0(iPhone;iOS 10.3.2;Scale/2.00)"
    }
    url = "https://functest.junhuahomes.com/imapi/user/sendCheckSms"
    para = {
        "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
        "apiVersion": "1.3.0",
        "channel": "",
        "currentVer": "3.0.0",
        "Login": "",
        "mobile": "13718591270",
        "phoneName": "iPhone",
        "platform": "ios",
        "platformVersion": "10.3.2",
        "system": "iOS"
    }
    myrequest = requests.post(url, data=para, verify=False,
                              cookies=mycookie, headers=myheader)
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
