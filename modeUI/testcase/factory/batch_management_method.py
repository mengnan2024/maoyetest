from time import sleep

from modeUI.base.baseMethod import BaseMethod
from modeUI.page.factory.batch_management_page import Batch_management_page
from modeUI.page.factory.index_factory_page import Index_factory_page
from utils.config_yaml import YamlHandler
from utils.keyboard_method import Keyboard_method

'''批次管理'''


class Batch_management_method(BaseMethod):
    '''合批次'''

    def merge_batch(self, file_path):
        self.click_until_visiable(Index_factory_page.batch_management)  # 批次管理
        data = YamlHandler(file_path).read_yaml()  # 获取商品ID
        self.send_keys_until_visiable(Batch_management_page.goods_id, data['goods_id'])  # 填入商品ID
        self.click_until_visiable(Batch_management_page.search_button)  # 点击搜索
        self.click_until_visiable(Batch_management_page.order_selected)  # 选中订单
        self.click_until_visiable(Batch_management_page.merge_batch)  # 合成批次

    '''全部合批次'''

    def merge_all_batch(self):
        self.click_until_visiable(Index_factory_page.batch_management)  # 批次管理
        sleep(5)
        self.click_until_visiable(Batch_management_page.all_order_selected)  # 选中全部订单
        self.click_until_visiable(Batch_management_page.merge_batch)  # 合成批次

    '''打标签'''

    def print_tag(self):
        self.click_until_visiable(Index_factory_page.batch_management)  # 批次管理
        self.click_until_visiable(Batch_management_page.already_create_tag)  # 点击已生成
        # self.click_fixed_area(1000, 600)  # 点击空白处
        sleep(20)
        self.click_until_visiable(Batch_management_page.all_batch)  # 选中全部订单
        self.click_until_visiable(Batch_management_page.print_tag_button)  # 打印标签
        sleep(20)
        Keyboard_method().keyboard_enter()  # 保存打印好的pdf文件
        sleep(4)
        Keyboard_method().close_wps()  # 关闭wps
