from time import sleep

from modeAPI.case.create_lots_of_orders import DataCombo
from modeUI.base.baseMethod import BaseMethod
from modeUI.page.shop.order_management.import_orders_page import Import_orders_page
from utils.keyboard_method import Keyboard_method
from utils.get_excel import delete_more_rows


class Import_orders_method(BaseMethod):
    def import_orders_by_excel(self, file_path, num, buyer_id):
        delete_more_rows(file_path=file_path, num=num + 1)
        DataCombo.create_more_order(self, file_path, num, buyer_id)  # 创建指定条数的订单数据
        self.click_until_visiable(Import_orders_page.import_orders_list_button)  # 点击导入列表
        self.click_until_visiable(Import_orders_page.import_orders_button)  # 点击导入按钮
        self.click_until_visiable(Import_orders_page.import_orders_data)  # 点击导入数据
        sleep(2)
        BaseMethod.set_text(self=self, text='[AutoTest]import_mode.xlsx')  # 文件名写入剪切板
        sleep(2)
        Keyboard_method.ctrl_v(self)  # 粘贴文件名
        sleep(1)
        Keyboard_method.keyboard_enter(self)  # 确定
