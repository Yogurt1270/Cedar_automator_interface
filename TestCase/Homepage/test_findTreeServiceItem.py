#!/usr/local/bin/python env
# coding:utf-8

import requests
import json
import allure


class TestFindTreeServiceItem:
    @allure.Step({0})
    def gettoken(self):
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
        # print(res)
        token = request.headers['login']
        return token

    # 根据houseID和communityId获取
    @allure.Step({1})
    def test_displayhomepage(self):
        url = "https://functest.junhuahomes.com/gtw/provider/findTreeServiceItem"
        para = {
            "houseId": "22575",
            "communityId": "22206"
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        # print(res)
        assert res['data'][0]['layoutType'] == 'BIG_BANNER'

    # houseId为空时
    def test_houseidisNone(self):
        url = "https://functest.junhuahomes.com/gtw/provider/findTreeServiceItem"
        para = {
            "houseId": "",
            "communityId": "22206"
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        # print(res)
        assert res['data'][0]['layoutType'] == 'BIG_BANNER'

    # communityId为空
    def test_communityIdisNone(self):
        url = "https://functest.junhuahomes.com/gtw/provider/findTreeServiceItem"
        para = {
            "houseId": "22575",
            "communityId": ""
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        # print(res)
        assert res['message'] == '小区ID不能为空!'

    # 参数异常时
    def test_paraisNull(self):
        url = "https://functest.junhuahomes.com/gtw/provider/findTreeServiceItem"
        para = {
            "houseId": "null",
            "communityId": "null"
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        # print(res)
        assert res['message'] == '小区不存在!'
