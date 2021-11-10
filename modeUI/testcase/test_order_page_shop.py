from time import sleep
from modeUI.base.baseMethod import BaseMethod
from modeUI.testcase.index_page_method import Index_page_method
from modeUI.testcase.login_shop import Login_shop

'''订单管理'''


class Test_order_page(BaseMethod):

    def test_order_page(self):
        '''店铺端登录'''
        Login_shop.login_shop(self)

        '''创建订单'''
        Index_page_method.create_order_method(self)

        '''订单搜索'''

        Index_page_method.search_list_order(self, file_path='../data/temp_data.yaml')

        sleep(5)
        self.driver.quit()
