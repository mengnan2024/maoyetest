from time import sleep

from modeUI.base.baseMethod import BaseMethod
from modeUI.page.shop.order_management.index_order_management_page import Index_page
from modeUI.page.shop.login_page import Login_page


class Login_shop(BaseMethod):
    def login_shop(self):
        self.open_browser('Chrome', 'https://tcshop.jzm2c.com/login')  # 打开页面
        self.send_keys_until_visiable(Login_page.username_input, 'AutoTest')  # 输入用户名
        self.send_keys_until_visiable(Login_page.password_input, '123456')  # 输入密码
        self.click_until_visiable(Login_page.password_hidden)  # 点击隐藏密码按钮
        self.click_until_visiable(Login_page.remember_password)  # 点击记住密码
        self.click_until_visiable(Login_page.login_button)  # 点击登录
        sleep(2)
        self.page_title_is(Index_page.order_page_title)  # 判断标题
