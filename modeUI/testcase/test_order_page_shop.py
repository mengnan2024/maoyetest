from time import sleep
from modeUI.base.baseMethod import BaseMethod
from modeUI.testcase.index_page_method import Index_page_method
from modeUI.testcase.login_shop import Login_shop

'''订单管理'''


class Test_order_page(BaseMethod):

    def test_order_page(self):
        '''登录'''
        Login_shop.login_shop(self)

        '''手动拉单'''
        Index_page_method.manual_order_method(self)

        '''创建订单'''
        Index_page_method.create_order_method(self)

        '''订单搜索'''

        Index_page_method.search_list_order(self)

        '''预发货'''
        Index_page_method.pre_shipping_method(self)

        '''推单'''
        Index_page_method.push_order(self)

        '''修改收货地址'''

        '''手动合并订单'''
        Index_page_method.merge_order_method(self)

        '''刷新编码'''
        Index_page_method.refresh_code_page(self)

        sleep(5)
        self.driver.quit()
