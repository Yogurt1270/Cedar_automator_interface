#!/usr/local/bin/python
# coding:utf-8

import requests


def clock():
    url = "https://seagull-data.toushibao.com/server_clock"

    r = requests.get(url=url, verify=False)
    print(r.text)


clock()
