'''待审订单'''
from time import sleep

from modeUI.base.baseMethod import BaseMethod
from modeUI.page.factory.index_factory_page import Index_factory_page
from modeUI.page.factory.wait_pass_orders_page import Wait_pass_orders_page
from utils.config_yaml import YamlHandler

'''待审订单'''


class Pass_order_method(BaseMethod):
    '''审批单个订单'''

    def pass_order(self, file_path):
        self.click_until_visiable(Index_factory_page.wait_pass_orders)  # 点击待审订单
        data = YamlHandler(file_path).read_yaml()  # 读取刚才创建的订单
        sleep(3)
        self.send_keys_until_visiable(Wait_pass_orders_page.order_num_input, data['order_num'])  # 填入订单号

        self.click_until_visiable(Wait_pass_orders_page.search_button)  # 搜索
        self.click_until_visiable(Wait_pass_orders_page.expand_all)  # 展开所有
        sleep(2)
        data_goods_num = self.split_text(Wait_pass_orders_page.goods_num, 4, 14)  # 获取商品ID
        YamlHandler(file_path).write_yaml({'goods_id': data_goods_num})  # 单号写入yaml
        self.click_until_visiable(Wait_pass_orders_page.order_selected)  # 选择该订单
        self.click_until_visiable(Wait_pass_orders_page.pass_button)  # 通过
        #self.click_until_visiable(Wait_pass_orders_page.confirm_button)  # 确认
        sleep(5)
        self.click_until_visiable(Wait_pass_orders_page.close_progress)  # 关闭进度弹窗

    '''审批全部订单'''

    def pass_more_order(self, file_path):
        self.click_until_visiable(Index_factory_page.wait_pass_orders)  # 点击待审订单
        self.click_until_visiable(Wait_pass_orders_page.data_limit)
        self.select_option(Wait_pass_orders_page.data_limit_ul, 6)  # 选中1000条展示
        sleep(5)
        self.click_until_visiable(Wait_pass_orders_page.expand_all)  # 展开所有
        sleep(8)
        data_goods_num = self.split_text(Wait_pass_orders_page.goods_num, 4, 14)  # 获取商品ID
        YamlHandler(file_path).write_yaml({'goods_id': data_goods_num})  # 单号写入yaml
        self.click_until_visiable(Wait_pass_orders_page.all_orders_checkbox)  # 全选
        self.click_until_visiable(Wait_pass_orders_page.pass_button)  # 通过
        self.click_until_visiable(Wait_pass_orders_page.close_progress)  # 关闭进度弹窗
