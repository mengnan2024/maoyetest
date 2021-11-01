import datetime
import datetime as dt

import requests

from modeAPI.utils.get_excel import readFromExcel


class TestOrderPage():
    '''先获取token， 传参'''
    data = readFromExcel()

    def test_AllOrder(self):
        url = self.data[3]
        headers = {
            'authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImVkNWU4MGRjLTlkNDMtNDFjZi04ZGNkLTI5ODM0MmVhZDU2MSJ9.LhG8kCEq0IaBENPkswcIPQ9V5iN83RiZOBePT7ezYxw4kx83qRJdVFsqxgjcUQ90fo1kkRHaffRAD8JvLKdxWg'
        }

        params = {
            'associateSplit': '1',
            'fromTime': '2021-10-25 00:00:00',
            'endTime': '2021-11-01 23:59:59',
            'pageSize': '500',
            'pageNum': '1',
            'status': '0'
        }
        res = requests.post(url=url, params=params, headers=headers)

        assert res.status_code == 200
        assert res.json()['code'] == 0
        assert res.json()['message'] == 'successful'
        assert res.json()['data'][0]['orderNum'] == 227
