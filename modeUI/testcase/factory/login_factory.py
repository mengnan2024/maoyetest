from modeUI.base.baseMethod import BaseMethod
from modeUI.page.factory.login_page import Login_Page


class Login_page(BaseMethod):
    def login_page(self, browser_name, login_url, username, password):
        self.open_browser(browser_name, login_url)  # 打开页面
        self.page_title_is(Login_Page.login_page_title)  # 判断标题
        self.send_keys_until_visiable(Login_Page.login_page_username, username)  # 输入账号
        self.send_keys_until_visiable(Login_Page.login_page_password, password)  # 输入密码
        self.click_until_visiable(Login_Page.login_page_loginButton)  # 点击登录
