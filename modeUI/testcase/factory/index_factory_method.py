from modeUI.base.baseMethod import BaseMethod
from modeUI.testcase.factory.batch_management_method import Batch_management_method
from modeUI.testcase.factory.wait_pass_order_method import Pass_order_method
from modeUI.testcase.factory.scan_code_shipped_method import Scan_code_shipped_method
from modeUI.testcase.factory.system_configuration_method import System_configuration_method


class Index_factory_method(BaseMethod):
    '''主页方法'''

    '''待审订单'''

    def wait_pass_order(self, file_path):
        Pass_order_method.pass_order(self, file_path)

    '''批次管理-合成批次'''

    def batch_management(self, file_path):
        Batch_management_method.merge_batch(self, file_path)  # 合批次

    '''打标签'''

    def print_tag(self):
        Batch_management_method.print_tag(self)  # 打标签

    '''扫码发货'''

    def scan_code_shipped(self, file_path):
        Scan_code_shipped_method.scan_code(self, file_path)  # 扫码发货

    '''系统设置'''

    def system_configuration(self):
        System_configuration_method.printer_configuration(self)
