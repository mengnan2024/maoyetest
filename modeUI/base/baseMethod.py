'''封装selenium的公共方法'''
from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC


class BaseMethod():
    '''浏览器的常用封装操作'''

    #打开浏览器
    def open_browser(self,browser_name,url):
        if browser_name == 'Chrome':
            self.driver = webdriver.Chrome()
            self.driver.get(url)
        elif browser_name == 'Opera':
            self.driver = webdriver.Opera()
            self.driver.get(url)
        elif browser_name == 'firefox':
            self.driver = webdriver.firefox()
            self.driver.get(url)
        self.driver.maximize_window()
        return self.driver


    #等待元素出现
    def wait_element_visiable(self,locate):
        try:
            ele = wait.WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((locate[1],locate[2]))
            )
            return ele
        except:
            print(locate[0] + '的' + locate[2] + '元素未找到')

    #元素出现点击
    def click_until_visiable(self, locate):
        # try:
            self.wait_element_visiable(locate).click()
        # except:
        #     print(locate[0] + '无法点击')

    #元素出现时输入
    def send_keys_until_visiable(self, locate, content):
        try:
            self.wait_element_visiable(locate).send_keys(content)
        except AttributeError:
            print('无输入属性')

    #判断当前页面标题
    def page_title_is(self, title_name):
        try:
            ele = wait.WebDriverWait(self.driver, 2).until(
                EC.title_is(title_name[1])
            )
            return ele
        except:
            print('【' + title_name[0] + '】与标题不符')

    #刷新当前页面
    def refresh_page(self):
        self.driver.refresh()


