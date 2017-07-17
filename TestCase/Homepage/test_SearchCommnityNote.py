#!/usr/local/bin/python env
# coding:utf-8


import requests
import json


class TestSearchCommnityNote:
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


    # 获取社区公告
    def test_getcommnitynote(self):
        url = "https://functest.junhuahomes.com/gtw/provider/searchCommnityNote"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "bizType": "COMMUNITY_BULLETIN",
            "channel": "",
            "communityId": "22206",
            "currentVer": "3.0.0",
            "houseId": "22575",
            "login": self.test_CheckNumWithAuth(),
            "numPerPage": "15",
            "pageNum": "1",
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS"
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        print(res)
        assert 'messageId'
