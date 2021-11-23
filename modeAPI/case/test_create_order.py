import pytest

from modeAPI.common.requests_method import requests_method
from utils.get_excel import readFromExcel


class TestCreateOrder:
    '''
    成功创建的订单，会先返回"data":"121111615025923001"， 这串数字对应sql中order_info表的order_no字段，通过order_no找到original_order_no【订单号】
    '''


@pytest.mark.parametrize('file_path', [r'C:\Users\Administrator\Desktop\order_date.xls'])  # 数据来源
@pytest.mark.parametrize('row_num', [0])  # 读取行
@pytest.mark.parametrize('sheet_name', ['manualAddOrder'])  # 表名
def test_AllOrder(self, file_path, sheet_name, row_num, get_token):
    self.data = readFromExcel(file_path, sheet_name, row_num)
    res = requests_method(file_path, sheet_name, row_num, get_token)
    print(res.text)
    assert res.status_code == 200
    assert res.json()['code'] == self.data[7]
    assert res.json()['message'] == self.data[9]
