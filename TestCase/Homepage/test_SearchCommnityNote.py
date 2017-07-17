#!/usr/local/bin/python env
# coding:utf-8


import requests
import allure


class TestSearchCommnityNote:
    # 获取社区公告

    @allure.Ignored
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
            "Login": "b42c9f51ed3e4accbf54efbda3aa5de7",
            "numPerPage": "15",
            "pageNum": "1",
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "system": "iOS"
        }
        r = requests.post(url, data=para, verify=False)
        print(r.status_code)
        assert r.status_code == 200
