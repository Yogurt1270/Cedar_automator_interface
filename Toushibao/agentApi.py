#!/usr/local/bin/python
# coding:utf-8

import requests
import json


def agentApi():
    myurl = "https://seagull-data.toushibao.com/mobile_rum/agentApi"
    mydata = {
        "type": "ios",
        "version": "v2",
        "rumData": [{"execute_time": 1499676105917.279,
                     "url": "https:\/\/functest.junhuahomes.com\/imapi\/base\/checkIOSVersion", "dns_dur": 0,
                     "first_packet_time": 606.1059832572937, "resh": "", "receive": 49,
                     "request_id": "cf61402b-914b-4c15-a344-98634c8ebf35", "http_body": "",
                     "response_time": 610.6969714164734, "error_code": "", "error_info": "", "error_type": "x",
                     "http_method": "POST", "send": 159, "excs": "", "ssl_dur": 333, "is_error": 0,
                     "event_tag": "startup", "resb": "", "collect_time": 1499676106527.976, "tcp_dur": 448,
                     "target_name": "startupPage", "request_trace": 1},
                    {"execute_time": 1499676106025.639, "url": "https:\/\/stats.jpush.cn\/v2\/report", "dns_dur": 0,
                     "first_packet_time": 581.8690061569214, "resh": "", "receive": 0,
                     "request_id": "6118ef3f-536a-4d41-a32f-f35aaa6d7437", "http_body": "",
                     "response_time": 581.9519758224487, "error_code": "", "error_info": "", "error_type": "x",
                     "http_method": "POST", "send": 203, "excs": "", "ssl_dur": 0, "is_error": 0,
                     "event_tag": "startup", "resb": "", "collect_time": 1499676106607.591, "tcp_dur": 0,
                     "target_name": "startupPage", "request_trace": 0}, {"execute_time": 1499676106314.836,
                                                                         "url": "https:\/\/functest.junhuahomes.com\/gtw\/activity\/getADList4C",
                                                                         "dns_dur": 0,
                                                                         "first_packet_time": 315.6789541244507,
                                                                         "resh": "", "receive": 548,
                                                                         "request_id": "e86de5d4-a585-4e14-a9be-ad8608ef346d",
                                                                         "http_body": "",
                                                                         "response_time": 316.2269592285156,
                                                                         "error_code": "", "error_info": "",
                                                                         "error_type": "x", "http_method": "POST",
                                                                         "send": 167, "excs": "", "ssl_dur": 50,
                                                                         "is_error": 0, "event_tag": "startup",
                                                                         "resb": "", "collect_time": 1499676106631.063,
                                                                         "tcp_dur": 221, "target_name": "startupPage",
                                                                         "request_trace": 0},
                    {"execute_time": 1499676106029.237, "url": "https:\/\/stats.jpush.cn\/v2\/report", "dns_dur": 0,
                     "first_packet_time": 712.6060128211975, "resh": "", "receive": 0,
                     "request_id": "0cf62822-a358-4f03-8298-edb22a76fbf1", "http_body": "",
                     "response_time": 712.755024433136, "error_code": "", "error_info": "", "error_type": "x",
                     "http_method": "POST", "send": 220, "excs": "", "ssl_dur": 0, "is_error": 0,
                     "event_tag": "startup", "resb": "", "collect_time": 1499676106741.992, "tcp_dur": 0,
                     "target_name": "startupPage", "request_trace": 0}], "is_tracking": True, "nest_socket": [],
        "nest_sessions": [
            {"durationMicro": 50140.61767578125, "start_milli": 1499675975170.596, "end_milli": 1499676025311.214,
             "is_setup": 1}],
        "basic": {"os_enum": 1, "access": "WiFi", "sdk_c": "cw", "os_version": "10.3.2", "lon": "", "dump_energy": 100,
                  "app_key": "wS0n2SF8WRA6pp871oldJ\/7NbCalsKsQfj6VeI0u6cFSaWvfGwFf91AOT8KKrCrp0SmoVfYvKAk!!",
                  "app_name": "雪松家园", "locale": "zh_CN", "is_new": 0, "operator": "中国移动", "version": "3.0.0",
                  "orientation": 1, "branch": "10.3.2", "cpu_used": 0.3, "mem_free": 5.028741e+08,
                  "device_version": "iPhone 6", "channel": "", "platform_model": "iPhone7,2", "cpu_model": "16777228_1",
                  "is_setup": 1, "root": 0, "ud_id": "be7faff4f79baaf9ad62db1cd26053eccd184674",
                  "useful_space": 3229274112, "mem_total": 3.607265e+09, "device_type": 0, "os": "iOS", "lat": "",
                  "mem_used": 3.314074e+07, "sdk_v": "1.5.4", "resolution": "750x1334", "device_name": "iPhone 6",
                  "timestamp": 1499676111354.681}, "needDecode": "1", "nest_event_tracking": [], "nest_anr": [],
        "nest_resource_tracking": [],
        "nest_startups": [{"start_milli": 1499676105667.292, "durationMicro": 587, "end_milli": 1499676106254.497}],
        "nest_ajax_tracking": [], "crash_infos": [], "nest_view_tracking": [
            {"view_event": "viewDidDisappear", "event_tag": "startup", "extra_info": "",
             "view_class": "XHLaunchAdController", "target_name": "XHLaunchAdController", "duration": 528.86376953125,
             "timestamp": 1499676106196.156},
            {"view_event": "viewDidAppear", "event_tag": "startup", "extra_info": "", "duration": 218.89306640625,
             "target_name": "DSLoginTableViewController", "view_class": "DSLoginTableViewController",
             "timestamp": 1499676106035.554}]
    }
    r = requests.post(url=myurl, data=mydata, verify=False)
    j = json.loads(r.content.decode('utf-8'))
