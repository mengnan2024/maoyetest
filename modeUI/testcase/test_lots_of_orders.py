'''批量订单测试'''
import pytest

from modeUI.base.baseMethod import BaseMethod
from modeUI.testcase.factory.index_factory_method import Index_factory_method
from modeUI.testcase.factory.login_factory import Login_page

from modeUI.testcase.shop.import_orders_method import Import_orders_method
from modeUI.testcase.shop.index_shop_method import Index_page_method
from modeUI.testcase.shop.login_shop import Login_shop


class Test_lots_of_orders(BaseMethod):
    '''登录>批量导入订单>推送到工厂'''

    # @pytest.mark.run(order=1)
    # @pytest.mark.parametrize(
    #     'orders_data,'  # 订单数据的路径，存放批量生成的订单数据，用于导入订单到店铺端
    #     'num,'  # 批量生成多少条订单
    #     'buyer_id',  # 批量生成的数据，暂时使用买家id来区分数据批次
    #     [(
    #             r'C:\Users\Administrator\[AutoTest]import_mode.xlsx',
    #             5,
    #             'autotest12'
    #     )])
    # def test_shop_01(self, orders_data, num, buyer_id):
    #     '''店铺端登录'''
    #     Login_shop.login_shop(self)
    #
    #     '''批量导入订单'''
    #     Import_orders_method.import_orders_by_excel(self, file_path=orders_data, num=num, buyer_id=buyer_id)
    #
    #     '''通过买家ID搜索'''
    #     Index_page_method.search_list_order_by_buyerID(self, buyer_id)
    #
    #     '''推送'''
    #     Index_page_method.push_order(self)
    #
    #     '''关闭浏览器'''
    #     self.quit_browser()

    '''审批>合批次>打标签>扫码发货'''

    @pytest.mark.run(order=2)
    def test_factory_02(self):
        # 登录
        Login_page.login_page(self)

        # 批量通过订单
        Index_factory_method.wait_pass_more_orders(self)
