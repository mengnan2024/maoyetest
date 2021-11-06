from modeUI.base.baseMethod import BaseMethod
from modeUI.page.shop.login_page import Login_page
from modeUI.page.shop.index_page import Order_page

"""测试登录"""
class TestLogin(BaseMethod):
    def test_login(self):
        self.open_browser('Chrome', 'https://tcshop.jzm2c.com/login')  # 打开页面
        self.send_keys_until_visiable(Login_page.username_input, '时涛') # 输入用户名
        self.send_keys_until_visiable(Login_page.password_input, '123456') # 输入密码
        self.click_until_visiable(Login_page.password_hidden) # 点击隐藏密码按钮
        self.click_until_visiable(Login_page.remember_password) # 点击记住密码
        self.click_until_visiable(Login_page.login_button) # 点击登录
        self.page_title_is(Order_page.order_page_title) # 判断标题
