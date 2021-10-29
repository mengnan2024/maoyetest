from time import sleep

from modeUI.base.baseMethod import BaseMethod
from modeUI.page.shop.order_page import Order_page


class Test_order_page(BaseMethod):
    def test_order_page(self):
        sleep(3)
        self.refresh_page()
        self.click_until_visiable(Order_page.all_order_button)
        self.click_until_visiable(Order_page.wait_manual_button)
