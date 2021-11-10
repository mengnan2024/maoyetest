import pytest
from modeUI.testcase.factory.index_factory_method import Index_factory_method
from modeUI.testcase.factory.login_factory import Login_page

'''审批 > 合批次 > 打标签 > 扫码发货'''

file_path = '../data/temp_data.yaml'


class Test_factory_main(Index_factory_method):
    #def setup(self):
        #Login_page.login_page(self)

    def test_factory_main(self):
        # 登录
        Login_page.login_page(self)
        # 设置打印机
        self.system_configuration()

        # 审批订单
        self.wait_pass_order(file_path)

        # 打标签>合批次
        self.batch_management(file_path)

        # 扫码发货
        self.scan_code_shipped(file_path)
