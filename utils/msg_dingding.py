import json

import requests


def sendmessage(message):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=d5c48fbc83063c840810fe79ea15ae2adfc49dd9adc0fcfc07712b651fe1e820'  # 这里填写你自定义机器人的webhook地址
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8"
    }
    String_textMsg = {
        "msgtype": "text",
        "text": {"content": message},
        "at": {
            "atMobiles": [
                "130xxxxxxxx"  # 如果需要@某人，这里写他的手机号
            ],
            "isAtAll": 0  # 如果需要@所有人，这里写1
        }
    }
    String_textMsg = json.dumps(String_textMsg)
    res = requests.post(url, data=String_textMsg, headers=HEADERS)
    print(res.text)
