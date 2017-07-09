#!/usr/local/bin/python env
# coding:utf-8

from Common.GetMyToken import CedarRequest
import requests
import json


class TestLogout:
    mytoken = CedarRequest.myrequest.headers['login']
    print(CedarRequest.myrequest.headers)
    mysession = CedarRequest.mysession.cookies

    # 退出
    def test_logout(self):
        reqeest_url = "https://functest.junhuahomes.com/imapi/user/logout"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "Login": TestLogout.mytoken,
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS",
            "xgToken": "191e35f7e0731cc5080"
        }
        myrequest = requests.post(reqeest_url, data=para,
                                  verify=False, cookies=TestLogout.mysession)
        request_result = json.loads(myrequest.content.decode('utf-8'))
        # print(request_result['code'])
        assert request_result['message'] != '没有登录信息.'
