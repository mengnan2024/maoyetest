from selenium.webdriver.common.by import By

'''登录页面'''


class Login_Page:
    login_page_title = ('登录页面标题', '工厂端')
    login_page_username = ('用户名', By.XPATH, '//*[@id="app"]/div/form/div[1]/div/div/input')
    login_page_password = ('密码', By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div/input')
    login_page_loginButton = ('登录按钮', By.XPATH, '//*[@id="app"]/div/form/div[3]/div/button')
