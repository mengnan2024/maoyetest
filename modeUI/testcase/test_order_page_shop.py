import time

import pytest

from modeUI.base.baseMethod import BaseMethod
from modeUI.testcase.factory.index_factory_method import Index_factory_method
from modeUI.testcase.factory.login_factory import Login_page
from modeUI.testcase.shop.import_orders_method import Import_orders_method
from modeUI.testcase.shop.index_shop_method import Index_page_method
from modeUI.testcase.shop.login_shop import Login_shop
from utils.config_yaml import YamlHandler
from utils.msg_dingding import sendmessage

'''单一订单全流程操作'''


# @pytest.mark.flaky(reruns=3, reruns_delay=2)
class Test_order_page(BaseMethod):
    '''登录>创建手工订单>推送到工厂'''

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(
        # 临时表的路径，存放生成的电商订单号和对应的商品id
        temp_data_yaml=r'C:\Users\Administrator\Desktop\pythonProject1\modeUI\data\temp_data.yaml',

    )
    def test_shop_page(self, temp_data_yaml):
        '''重置临时表的数据'''
        self.clear_file_content(temp_data_yaml)

        '''店铺端登录'''
        Login_shop.login_shop(self)

        '''创建订单'''
        Index_page_method.create_order_method(self)

        '''通过电商订单号搜索订单'''
        Index_page_method.search_list_order_by_orderID(self, file_path=temp_data_yaml)

        '''推送'''
        Index_page_method.push_order(self)

        '''发消息'''
        data = YamlHandler(temp_data_yaml).read_yaml()

        self.quit_browser()

        sendmessage(
            str('#店铺端 - - - - - -【推单成功】' + '\n' + '\n' + '订单号：' + data['order_num'] + '\n' + '\n' + time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime())))

    '''审批>合批次>打标签>扫码发货'''

    @pytest.mark.run(order=2)
    def test_factory(self):
        file_path = r'C:\Users\Administrator\Desktop\pythonProject1\modeUI\data\temp_data.yaml'
        # 登录
        Login_page.login_page(self)
        # 设置打印机
        Index_factory_method.system_configuration(self)

        # 审批订单

        Index_factory_method.wait_pass_order(self, file_path)

        # 合批次
        Index_factory_method.batch_management(self, file_path)

        # 打标签
        Index_factory_method.print_tag(self)

        # 扫码发货
        Index_factory_method.scan_code_shipped(self, file_path)

        '''发消息'''
        data = YamlHandler(file_path).read_yaml()
        sendmessage('#工厂端 - - - - - -【发货成功】' + '\n' + '\n' + '商品号：' + data[
            'goods_id'] + '\n' + '订单号：' + data['order_num'] + '\n' + '\n' + str(
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
        self.quit_browser()
