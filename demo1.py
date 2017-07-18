#!/usr/local/bin/python env
# coding:utf-8
import requests
import pytest
import all

# 解决httpsWarning
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import json


class Test:
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
    mysession = requests.Session()
    myrequest = mysession.post(url, data=para, verify=False)
    print(myrequest.headers)
    print(myrequest.cookies)
    print(myrequest.content.decode('utf-8'))

    print(mysession.headers)
    print(mysession.cookies)


# 获取token
def test_gettoken():
    # print(Test.myrequest.headers['login'])
    print(type(Test.myrequest.request))
    return Test.myrequest.headers['login']


def test_getsesseion():
    # print(Test.mysession)
    return Test.mysession


if __name__ == "__main__":
    pytest.main()
