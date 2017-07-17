#!/usr/local/bin/python env
# coding:utf-8
from Common.GetMyToken import CedarRequest

import requests
import json


class TestMyOrderList:
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
        return token

    # 获取订单列表全部分类
    def test_alloderlist(self):
        url = "https://functest.junhuahomes.com/imapi/homeRepair/myOrderList"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "numPerPage": "15",
            "pageNum": "1",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairStatus": "",
            "repairType": "",
            "system": "iOS",
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        print(res)
        assert 'recordList'

    #
    # 获取订单列表室内报修，全部
    def test_homerepair_oderlist_all(self):
        url = "https://functest.junhuahomes.com/imapi/homeRepair/myOrderList"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "numPerPage": "15",
            "pageNum": "1",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairStatus": "",
            "repairType": "HOME_REPAIR",
            "system": "iOS",
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert 'recordList'

    #
    # 获取订单列表室内报修，待受理
    def test_homerepair_oderlist_waitfor(self):
        url = "https://functest.junhuahomes.com/imapi/homeRepair/myOrderList"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "numPerPage": "15",
            "pageNum": "1",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairStatus": "WAIT_FOR_PROCESS",
            "repairType": "HOME_REPAIR",
            "system": "iOS",
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert 'recordList'

    #
    # 获取订单列表室内报修，处理中
    def test_homerepair_oderlist_processing(self):
        url = "https://functest.junhuahomes.com/imapi/homeRepair/myOrderList"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "numPerPage": "15",
            "pageNum": "1",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairStatus": "PROCESSING",
            "repairType": "HOME_REPAIR",
            "system": "iOS",
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert 'recordList'

    #
    # 获取订单列表室内报修，维修完成
    def test_homerepair_oderlist_repaircompleted(self):
        url = "https://functest.junhuahomes.com/imapi/homeRepair/myOrderList"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "numPerPage": "15",
            "pageNum": "1",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairStatus": "REPAIR_COMPLETED",
            "repairType": "HOME_REPAIR",
            "system": "iOS",
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert 'recordList'

    #
    # 获取订单列表室内报修，订单完成
    def test_homerepair_oderlist_completed(self):
        url = "https://functest.junhuahomes.com/imapi/homeRepair/myOrderList"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "numPerPage": "15",
            "pageNum": "1",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairStatus": "COMPLETED",
            "repairType": "HOME_REPAIR",
            "system": "iOS",
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert 'recordList'

    #
    # 获取订单列表公区报修
    def test_publicrepair_oderlist_all(self):
        url = "https://functest.junhuahomes.com/imapi/homeRepair/myOrderList"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "numPerPage": "15",
            "pageNum": "1",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairStatus": "",
            "repairType": "PUBLIC_REPAIR",
            "system": "iOS",
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert 'recordList'

    #
    # 获取订单列表公区报修, 待受理
    def test_publicrepair_oderlist_waitfor(self):
        url = "https://functest.junhuahomes.com/imapi/homeRepair/myOrderList"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "numPerPage": "15",
            "pageNum": "1",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairStatus": "WAIT_FOR_PROCESS",
            "repairType": "PUBLIC_REPAIR",
            "system": "iOS",
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert 'recordList'

    #
    # 获取订单列表公区报修, 处理中
    def test_publicrepair_oderlist_process(self):
        url = "https://functest.junhuahomes.com/imapi/homeRepair/myOrderList"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "numPerPage": "15",
            "pageNum": "1",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairStatus": "PROCESSING",
            "repairType": "PUBLIC_REPAIR",
            "system": "iOS",
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert 'recordList'

    #
    # 获取订单列表公区报修, 待验收
    def test_publicrepair_oderlist_waitcheck(self):
        url = "https://functest.junhuahomes.com/imapi/homeRepair/myOrderList"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "numPerPage": "15",
            "pageNum": "1",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairStatus": "WAITFORCHECK",
            "repairType": "PUBLIC_REPAIR",
            "system": "iOS",
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert 'recordList'

    #
    # 获取订单列表公区报修, 订单完成
    def test_publicrepair_oderlist_complete(self):
        url = "https://functest.junhuahomes.com/imapi/homeRepair/myOrderList"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "numPerPage": "15",
            "pageNum": "1",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairStatus": "COMPLETED",
            "repairType": "PUBLIC_REPAIR",
            "system": "iOS",
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert res['recordList']

    #
    # 获取订单列表通用订单
    def test_commonoderlist(self):
        url = "https://functest.junhuahomes.com/imapi/homeRepair/myOrderList"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "numPerPage": "15",
            "pageNum": "1",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairStatus": "",
            "repairType": "COMMON_ORDER",
            "system": "iOS",
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert 'recordList'

    #
    # 获取订单列表送件订单
    def test_appointmentorderlist(self):
        url = "https://functest.junhuahomes.com/imapi/homeRepair/myOrderList"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "numPerPage": "15",
            "pageNum": "1",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairStatus": "",
            "repairType": "EXPRESS_APPOINTMENT",
            "system": "iOS",
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert 'recordList'

    # 获取订单列表寄件订单
    def test_sendorderlist(self):
        url = "https://functest.junhuahomes.com/imapi/homeRepair/myOrderList"
        para = {
            "Imei": "be7faff4f79baaf9ad62db1cd26053eccd184674",
            "apiVersion": "1.3.0",
            "channel": "",
            "currentVer": "3.0.0",
            "numPerPage": "15",
            "pageNum": "1",
            "login": self.test_CheckNumWithAuth(),
            "phoneName": "iPhone",
            "platform": "ios",
            "platformVersion": "10.3.2",
            "repairStatus": "",
            "repairType": "EXPRESS_SEND",
            "system": "iOS",
        }
        req = requests.post(url, data=para, verify=False)
        res = json.loads(req.text)
        assert 'recordList'
