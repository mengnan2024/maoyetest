from modeUI.base.baseMethod import BaseMethod
from modeUI.page.factory.login_page import LoginPage

class TestLoginPage(BaseMethod):
    def test_login_page(self):

        self.open_browser('Chrome','https://tcfactory.jzm2c.com/login')
        self.page_title_is(LoginPage.login_page_title)
        self.send_keys_until_visiable(LoginPage.login_page_username ,'时涛')
        self.send_keys_until_visiable(LoginPage.login_page_password,'123456')
        self.click_until_visiable(LoginPage.login_page_loginButton)
