import json
import requests

from modeAPI.utils.get_excel import readFromExcel

'''请求的公共方法，仅封装了GET和POST请求方式'''
def requests_method(file_path, sheet_name, row_num):
    data = readFromExcel(file_path, sheet_name, row_num)
    url = data[3]
    headers = {
        'authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImMyZTM4YjY0LTQzYTUtNDIxNy05NGNiLWU5MjAxMzU4MTMzNSJ9.sP1qbXHpxTzq_lKF3rcvyrQIhPIkqFZ8eD2Dj-GniiShOoswMj4fin6HdjvddKW3sZMGYSudHXnPLc7CpF26Cw'
    }
    params = json.loads(data[6])
    global res
    if data[4] == 'get':
        res = requests.get(url=url, headers=headers)
    elif data[4] == 'post':
        res = requests.post(url=url, headers=headers, params=params)
    return res
