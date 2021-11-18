import json
import requests

from utils.get_excel import readFromExcel

'''请求的公共方法，仅封装了GET和POST请求方式'''


def requests_method(file_path, sheet_name, row_num, get_token):
    data_from = readFromExcel(file_path, sheet_name, row_num)
    url = data_from[3]
    headers = {
        'Authorization': get_token
    }
    data = json.loads(data_from[6])
    global res
    if data_from[4] == 'get':
        res = requests.get(url=url, headers=headers)
    elif data_from[4] == 'post':
        res = requests.post(url=url, headers=headers, json=data)
    return res
