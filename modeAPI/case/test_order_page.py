import json

import pytest
import requests

from modeAPI.utils.get_excel import readFromExcel

file_path = r'C:\Users\Administrator\Desktop\order_api.xlsx'


class TestOrderPage():
    '''先获取token， 传参'''

    @pytest.mark.parametrize('row_num', [1, 2])
    @pytest.mark.parametrize('sheet_name', ['订单相关'])
    def test_AllOrder(self, sheet_name, row_num):
        self.data = readFromExcel(file_path, sheet_name, row_num)
        url = self.data[3]
        headers = {
            'authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImI4ZTI3N2JkLThkNjAtNDkxOC04MGJkLTdjNTM3MjY1YzIyZiJ9.GTZtBclRmgAzTWwhjppHSEMjqdhV2ffGSuTBWsWC6e5Dr1KHHPo2oSzo2e9bnHJ6CG0TABRdqMZB2wi0xfzwng'
        }

        params = json.loads(self.data[6])

        if self.data[4] == 'post':
            res = requests.post(url=url, params=params, headers=headers)
        if self.data[4] == 'get':
            res = requests.get(url=url,headers=headers)
        assert res.status_code == 200
        assert res.json()['code'] == self.data[7]
        assert res.json()['message'] == self.data[9]
        assert res.json()['data'][0]['orderNum'] == self.data[10]