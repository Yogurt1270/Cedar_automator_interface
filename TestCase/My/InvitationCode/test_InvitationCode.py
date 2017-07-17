#!/usr/local/bin/pthone env
# coding:utf=8

import requests
import json


class TestInvitationCode:
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

    # 输入错误的邀请码并保存
    def test_save_invitationcode_error(self):
        url = "https://functest.junhuahomes.com/imapi/user/saveInvitationCode"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "invitationCode": "0000",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS"
        }
        req = requests.post(url=url, data=para, verify=False)
        res = json.loads(req.text)
        print(res)
        assert 'message'

    #   输入自己的邀请码并保存
    def test_save_invitationcode_self(self):
        url = "https://functest.junhuahomes.com/imapi/user/saveInvitationCode"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "invitationCode": "00015242",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS"
        }
        req = requests.post(url=url, data=para, verify=False)
        res = json.loads(req.text)
        print(res)
        assert 'message'

    #   输入正确的邀请码并保存,提示"邀请码已生效"服务端无返回response
    def test_save_invitationcode_correct(self):
        url = "https://functest.junhuahomes.com/imapi/user/saveInvitationCode"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "invitationCode": "00015242",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS"
        }
        req = requests.post(url=url, data=para, verify=False)
        res = json.loads(req.text)
        print(res)
        assert 'message'
