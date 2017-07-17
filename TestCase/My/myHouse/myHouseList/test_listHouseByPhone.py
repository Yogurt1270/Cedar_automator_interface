#!/usr/lacal/bin/python env
# coding:utf-8

import requests
import json


class TestListHouseByPhone:
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

    # 我的房屋列表接口
    # Testcase001_"已认证"手机号查看"我的房屋"
    def test_listhousebyphone(self):
        reqeest_url = "https://functest.junhuahomes.com/imapi/house/listHouseByPhone"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "login": self.test_CheckNumWithAuth(),
            "numPerPage": "100",
            "pageNum": "1",
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS",
            "userPhone": "13718591270"
        }
        req = requests.post(reqeest_url, data=para, verify=False)
        res = json.loads(req.text)
        print(res)
        assert res['totalCount']
