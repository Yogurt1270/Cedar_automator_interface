#!/usr/local/bin/pyton
# coding:utf-8

import requests
import json

url = "https://seagull.toushibao.com/api/v1/getMobileSetting"
para = {"appKey": "wS0n2SF8WRA6pp871oldJ/7NbCalsKsQfj6VeI0u6cFSaWvfGwFf91AOT8KKrCrp0SmoVfYvKAk!!", "appVer": "3.0.0"}

# mycookie = {
#     "tsb_session": "eyJpdiI6InBYamlBVzZPbDJhZVFNWWJ2Rld1b3hLaTR6NFJ4SUY1Q2YxK0g3b0trdkU9IiwidmFsdWUiOiJucnVRTmZBVkVCQkRLZHR4K1crYUEzNHpuRFNvaE11SjllQWNPaDg0M0RJRGl4SmtFXC9GU3ZVWVFzZmJTaXJaNjNaT1BtbUNsZ3BvZkp5ZHloWkdnOEE9PSIsIm1hYyI6IjA5Njg2YTRmMDdmZjk5ZjcwZjU3ZDEzOThmMzFlMjBlNWU0MTkwNTk4YTg2YWY0OThhMTRmMzFmNGZkNmU2MTcifQ%3D%3D"
# }
myheader = {
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "propertyApp/221 CFNetwork/811.5.4 Darwin/16.6.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

r = requests.post(url=url, data=para, verify=False)
j = json.loads(r.text)
print(j)
print(r.url)
# assert j['msg'] == "success"
