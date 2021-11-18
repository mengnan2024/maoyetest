from time import sleep

from modeUI.base.baseMethod import BaseMethod
from modeUI.page.factory.index_factory_page import Index_factory_page
from modeUI.page.factory.system_configuration_page import System_configuration_page


class System_configuration_method(BaseMethod):
    '''打印机设置'''

    def printer_configuration(self):
        self.click_until_visiable(Index_factory_page.system_configuration)  # 系统设置
        self.click_until_visiable(System_configuration_page.printer_conf)  # 点击打印机设置
        sleep(7)

        # 设置标签
        self.click_until_visiable(System_configuration_page.printer_name)
        sleep(3)
        self.select_option(System_configuration_page.printer_name_ul, 4)  # 选中打印机
        self.click_until_visiable(System_configuration_page.template_radio)  # 选中第一个模板
        self.click_until_visiable(System_configuration_page.save_btn)  # 点击保存

        # 设置面单
        self.click_until_visiable(System_configuration_page.rotas_conf)  # 切到面单设置
        self.click_until_visiable(System_configuration_page.add_rotas_configuration)  # 新增面单设置
        self.click_until_visiable(System_configuration_page.express_selection)
        self.select_option(System_configuration_page.express_selection_ul, 10)  # 选择面单快递公司
        self.click_until_visiable(System_configuration_page.printer_name_rotas)
        self.select_option(System_configuration_page.printer_name_rotas_ul, 4)  # 选中面单打印机
        self.click_until_visiable(System_configuration_page.confirm_button)  # 确定
