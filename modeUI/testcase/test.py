'./data/temp_data.yaml'
import datetime
import time
from datetime import date

import pytest

from modeUI.base.baseMethod import BaseMethod
from utils.config_yaml import YamlHandler

# file_path = '../data/temp_data.yaml'
# data = 'SG21111009503048000'
# YamlHandler(file_path).write_yaml(data)

# data = YamlHandler('../data/temp_data.yaml').read_yaml()
# print(data)

# f = open(file_path, 'r+')
# f.truncate()
# dataA = {'2': '3'}
# dataB = {'1': '2'}
# dataC = ['12':'1']
# data = YamlHandler('../data/temp_data.yaml').write_yaml(dataC)
# from utils.msg_dingding import sendmessage
#
from utils.msg_dingding import sendmessage

mes = (
    str('#店铺端 - - - - - -【推单成功】' + '\n' + '\n' +'订单号：' + '\n' + '\n' + time.strftime('%Y-%m-%d %H:%M:%S',
                                                                                  time.localtime())))

sendmessage(mes)
# class TestDemo(BaseMethod):
#     @pytest.mark.run(order=2)
#     def test_03(self):
#         self.open_browser('Chrome', 'https://www.baidu.com')  # 打开页面
#         self.quit_browser()
#
#     @pytest.mark.run(order=1)
#     def test_02(self):
#         self.open_browser('Chrome', 'https://www.cnblogs.com/ff-gaofeng/p/12090688.html')  # 打开页面
#         self.driver.quit()
