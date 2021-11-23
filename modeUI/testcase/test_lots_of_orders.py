'''批量订单测试'''
from time import sleep

import pytest

from modeUI.base.baseMethod import BaseMethod
from modeUI.testcase.factory.index_factory_method import Index_factory_method
from modeUI.testcase.factory.login_factory import Login_page

from modeUI.testcase.shop.import_orders_method import Import_orders_method
from modeUI.testcase.shop.index_shop_method import Index_page_method
from modeUI.testcase.shop.login_shop import Login_shop


class Test_lots_of_orders(BaseMethod):
    '''登录>批量导入订单>推送到工厂'''

    # 执行顺序从小到大
    @pytest.mark.run(order=1)
    # 店铺端登录参数
    @pytest.mark.parametrize(
        'browser_name, login_url, username, password', [(
                'Chrome',
                'https://tcshop.jzm2c.com/login',  # 测试环境
                'ceshixinhao1119',
                '123456'
        )])
    # 订单数据参数
    @pytest.mark.parametrize(
        'orders_data,num,buyer_id',
        [(
                r'C:\Users\Administrator\[AutoTest]import_mode.xlsx',  # 订单数据的路径，存放批量生成的订单数据，用于导入订单到店铺端
                100,  # 批量生成多少条订单
                'auddaaassw1o'  # 批量生成的数据，暂时使用买家id来区分数据批次
        )])
    def test_shop_01(self, browser_name, login_url, username, password, orders_data, num, buyer_id):
        '''店铺端登录'''
        Login_shop.login_shop(self, browser_name, login_url, username, password)  # 登录参数支持切换环境，参数可共用

        '''批量导入订单'''
        Import_orders_method.import_orders_by_excel(self, file_path=orders_data, num=num,
                                                    buyer_id=buyer_id)  # 通过pytest注解传入文件地址，订单条数，唯一码可变（现在是买家id），用于区分生成的订单

        '''通过买家ID搜索'''
        Index_page_method.search_list_order_by_buyerID(self, buyer_id)

        '''推送'''
        Index_page_method.push_order(self)

        sleep(10)
        '''关闭浏览器'''
        self.quit_browser()

    '''【审批>合批次>打标签>扫码发货】'''

    @pytest.mark.run(order=2)
    # 工厂端登录参数
    @pytest.mark.parametrize('browser_name, login_url,username, password',
                             [('Chrome',
                               'https://tcfactory.jzm2c.com/login',
                               'ceshixinhao1119',
                               '123456'
                               )])
    # 临时表的路径，存放生成发的电商订单号和对应的商品id
    @pytest.mark.parametrize(
        # 临时表的路径，存放生成的电商订单号和对应的商品id
        'temp_data_yaml', [(r'C:\Users\Administrator\Desktop\pythonProject1\modeUI\data\temp_data.yaml')]
    )
    def test_factory_02(self, temp_data_yaml, browser_name, login_url, username, password):
        # 清空临时数据
        self.clear_file_content(temp_data_yaml)

        # 登录
        Login_page.login_page(self, browser_name, login_url, username, password)

        # 设置打印机
        Index_factory_method.system_configuration(self)

        # 批量通过订单
        Index_factory_method.wait_pass_more_orders(self, temp_data_yaml)

        # 全部订单合批次
        Index_factory_method.batch_all_management(self)

        # 打标签
        Index_factory_method.print_tag(self)

        sleep(10)
        # 扫码发货
        Index_factory_method.scan_code_shipped(self, temp_data_yaml)

        self.quit_browser()
