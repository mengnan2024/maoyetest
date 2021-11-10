from modeUI.base.baseMethod import BaseMethod
from modeUI.page.factory.login_page import LoginPage

class TestLoginPage(BaseMethod):
    def test_login_page(self):

        self.open_browser('Chrome','https://tcfactory.jzm2c.com/login') #打开页面
        self.page_title_is(LoginPage.login_page_title) #判断标题
        self.send_keys_until_visiable(LoginPage.login_page_username ,'时涛') #输入账号
        self.send_keys_until_visiable(LoginPage.login_page_password,'123456') #输入密码
        self.click_until_visiable(LoginPage.login_page_loginButton) #点击登录


