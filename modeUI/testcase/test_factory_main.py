from modeUI.base.baseMethod import BaseMethod
from modeUI.page.factory.batch_management_page import Batch_management
from modeUI.page.factory.index_factory_page import Index_factory_page
from modeUI.page.factory.wait_pass_orders_page import Wait_pass_orders_page
from modeUI.testcase.login_factory import Login_page
from utils.config_yaml import YamlHandler

'''审批 > 合批次 > 打标签 > 扫码发货'''


class Test_factory_main(BaseMethod):

    def test_factory_main(self):
        Login_page.login_page(self)  # 登录
        file_path = '../data/temp_data.yaml'
        self.click_until_visiable(Index_factory_page.wait_pass_orders)  # 点击待审订单
        data = YamlHandler(file_path).read_yaml()  # 读取刚才创建的订单
        self.send_keys_until_visiable(Wait_pass_orders_page.order_num_input, data['order_num'])  # 填入订单号
        self.click_until_visiable(Wait_pass_orders_page.search_button)  # 搜索
        self.click_until_visiable(Wait_pass_orders_page.expand_all)  # 展开所有

        data_goods_num = self.split_text(Wait_pass_orders_page.goods_num)  # 获取商品ID
        YamlHandler(file_path).write_yaml({'order_num': data_goods_num})  # 单号写入yaml
        self.click_until_visiable(Wait_pass_orders_page.order_selected)  # 选择该订单
        self.click_until_visiable(Wait_pass_orders_page.pass_button)  # 通过
        self.click_until_visiable(Wait_pass_orders_page.confirm_button)  # 确认

        self.click_until_visiable(Index_factory_page.batch_management)  # 批次管理
        self.send_keys_until_visiable(Batch_management.goods_id)  # 填入商品ID
        self.click_until_visiable(Batch_management.search_button)  # 点击搜索
        self.click_until_visiable(Batch_management.order_selected)  # 选中订单
        self.click_until_visiable(Batch_management.merge_batch)  # 合成批次

        self.click_until_visiable(Batch_management.already_create_tag) # 点击已生成
