#!/usr/local/bin/python env
# coding:utf-8


import pytest
import requests
import allure


class TestFindTreeServiceItem:
    # 根据houseID获取
    @allure.Title("This is our cool test suite")
    @allure.Discription("In this cool suite we will test only cool discription")
    def test_displayhomepage(self):
        url = "https://functest.junhuahomes.com/gtw/provider/findTreeServiceItem"
        para = {
            "houseId": "22575",
            "communityId": "22206"
        }
        r = requests.post(url, data=para, verify=False)
        print(r.status_code)
        assert r.status_code == 404
