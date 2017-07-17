#!/usr/local/bin/python env
# coding:utf-8

import requests


class CedarRequest:
    url = "https://functest.junhuahomes.com/imapi/user/checkNum"
    para = {
        "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
        "apiVersion": "1.3.0",
        "channel": "",
        "currentCommunityId": "",
        "currentVer": "3.0.0",
        "dscd": "",
        "Login": "",
        "mobile": "13718591270",
        "phoneName": "iPhone",
        "platform": "ios",
        "platformVersion": "10.3.2",
        "system": "iOS",
        "validatecode": "1234",
        "xgToken": "191e35f7e0731cc5080"
    }

    def setup(self):
        print("------test start------")
        self.req = requests.post(CedarRequest.url, data=CedarRequest.para, verify=False)
        return req

    def teardown(self):
        print("------test end------")

        # 获取token

    def gettoken(self):
        print(CedarRequest.headers['login'])
        return CedarRequest.headers['login']
        # 获取JSESSIONID

#
# def getjsessionid(self):
#     # print(type(CedarRequest.myrequest.cookies))
#     aa = requests.utils.dict_from_cookiejar(CedarRequest.myrequest.cookies)
#     # print(aa['JSESSIONID'])
#     return aa['JSESSIONID']

#
# def getsesseion():
#     print(CedarRequest.mysession.cookies)
#     return CedarRequest.mysession
