import pytest

from modeAPI.common.requests_method import requests_method
from modeAPI.log.logger import Logger
from utils import readFromExcel

file_path = r'C:\Users\Administrator\Desktop\order_api.xlsx'


class TestOrderPage():
    '''先获取token， 传参'''

    @pytest.mark.parametrize('file_path', [r'C:\Users\Administrator\Desktop\order_api.xlsx'])
    @pytest.mark.parametrize('row_num', [1, 2])
    @pytest.mark.parametrize('sheet_name', ['订单相关'])
    def test_AllOrder(self, file_path, sheet_name, row_num):
        self.data = readFromExcel(file_path, sheet_name, row_num)
        res = requests_method(file_path, sheet_name, row_num)
        test_log = Logger()
        test_log.war(self, '警告信息')
        assert res.status_code == 200
        assert res.json()['code'] == self.data[7]
        assert res.json()['message'] == self.data[9]
        assert res.json()['data'][0]['orderNum'] == self.data[10]

