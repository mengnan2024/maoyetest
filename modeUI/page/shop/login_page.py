'''登录页面元素'''
from selenium.webdriver.common.by import By

'''[元素统一格式为：'元素名称', 定位方式，'元素值' ]'''


class Login_page:
    username_input = ('用户名输入框', By.XPATH, '//*[@id="app"]/div/div[2]/form/div[1]/div/div/div[1]/input')
    password_input = ('密码输入框', By.XPATH, '//*[@id="app"]/div/div[2]/form/div[2]/div/div/input')
    password_hidden = ('密码隐藏按钮', By.XPATH, '//*[@id="app"]/div/div[2]/form/div[2]/div/div/span/span/button/span')
    remember_password = ('记住密码选择框', By.XPATH, '//*[@id="app"]/div/div[2]/form/div[3]/label/span[1]')
    login_button = ('登录按钮', By.XPATH, '//*[@id="app"]/div/div[2]/form/button')
