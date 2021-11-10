from time import sleep

from modeUI.base.baseMethod import BaseMethod
from modeUI.page.factory.scan_code_shipped_page import Scan_code_shipped_page
from utils.config_yaml import YamlHandler
from utils.keyboard_method import Keyboard_method

'''扫码发货'''


class Scan_code_shipped_method(BaseMethod):
    def scan_code(self, file_path):
        self.click_until_visiable(Scan_code_shipped_page.scan_code_shipped_button)  # 点扫码发货
        data = YamlHandler(file_path).read_yaml()  # 获取商品ID
        self.send_keys_until_visiable(Scan_code_shipped_page.goods_code_input, data['goods_id'])  # 填入商品ID  # 填入商品ID
        sleep(2)
        self.click_until_visiable(Scan_code_shipped_page.confirm_button)  # 确定

        sleep(3)
        Keyboard_method().keyboard_enter()  # 保存打印好的pdf文件
        sleep(4)
        Keyboard_method().close_wps()  # 关闭wps
        sleep(3)
        Keyboard_method().close_wps()  # 关闭打印窗口
