from time import sleep

from modeUI.base.baseMethod import BaseMethod
from modeUI.page.shop.goods_management.index_goods_managment import Index_goods_management
from modeUI.testcase.shop.login_shop import Login_shop

"""测试商品管理"""


class Test_goods_management(BaseMethod):

    def test_goods_management(self):
        '''登录'''
        Login_shop.login_shop(self)

        '''批量解码-正常进度'''
        self.click_until_visiable(Index_goods_management.goods_management_tag)  # 点击商品管理标签
        self.click_until_visiable(Index_goods_management.all_order_selected)  # 选中全部订单
        self.click_until_visiable(Index_goods_management.batch_decode)  # 点击批量解码
        self.click_until_visiable(Index_goods_management.confirm_button)  # 弹出提示后，确认
        self.element_text_is(Index_goods_management.batch_decode_page_text, '批量解码')  # 判断进度弹出框的文字内容
        sleep(25)

        '''批量解码-强制终止解码'''
        self.click_until_visiable(Index_goods_management.all_order_selected)  # 选中全部订单
        self.click_until_visiable(Index_goods_management.batch_decode)  # 点击批量解码
        self.click_until_visiable(Index_goods_management.confirm_button)  # 弹出提示后，确认
        self.element_text_is(Index_goods_management.batch_decode_windows_text, '批量解码')  # 判断进度弹出框的文字内容
        sleep(1)  # 等1s
        self.click_until_visiable(Index_goods_management.end_process)  # 强制终止
        self.click_until_visiable(Index_goods_management.confirm_button)  # 弹出提示后，确认

        '''批量清除解码'''
        self.click_until_visiable(Index_goods_management.all_order_selected)  # 选中全部订单
        self.click_until_visiable(Index_goods_management.batch_clear_decode)  # 点击批量清除解码
        self.click_until_visiable(Index_goods_management.confirm_button)  # 弹出提示后，确认
