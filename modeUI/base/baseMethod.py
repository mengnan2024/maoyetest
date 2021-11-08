'''封装selenium的公共方法'''
import time

import win32con
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC
import win32clipboard as w


class BaseMethod():
    '''浏览器的常用封装操作'''

    # 打开浏览器
    def open_browser(self, browser_name, url):
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

    # 等待元素出现
    def wait_element_visiable(self, locate):
        try:
            ele = wait.WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((locate[1], locate[2]))
            )
            return ele
        except:
            print(locate[0] + '的' + locate[2] + '元素未找到')

    # 元素出现点击
    def click_until_visiable(self, locate):
        # try:
        self.wait_element_visiable(locate).click()

    # except:
    #     print(locate[0] + '无法点击')

    # 元素出现时输入
    def send_keys_until_visiable(self, locate, content):
        try:
            self.wait_element_visiable(locate).send_keys(content)
        except AttributeError:
            print('无输入属性')
    # 多个class取其中一个
    def more_class_click(self,locate):
        self.driver.find_elements(locate[1],locate[2],)[locate[3]].click()

    # 动态下拉框，通过ul找li
    def select_option(self, ul_locate, option_num):
        self.wait_element_visiable(ul_locate).find_elements_by_xpath('li')[option_num - 1].click()

    # 点击空白/指定区域
    def click_fixed_area(self, xoffset, yoffset):
        # 左键点击（x，y）坐标位置
        ActionChains(self.driver).move_by_offset(xoffset, yoffset).click().perform()
        # 鼠标右键点击 （x，y）坐标位置
        # ActionChains(self.driver).move_by_offset(xoffset,yoffset).context_click().perform()

    # 页面下划
    def down_turn(self):
        self.driver.execute_script('var q=document.documentElement.scrollTop=10000')
        time.sleep(1)

    # 物理按键END
    def send_keyborad(self,locate):
        self.driver.find_element(locate[1],locate[2]).send_keys(locate[3])

    # 判断当前页面标题
    def page_title_is(self, title_name):
        # try:
            ele = wait.WebDriverWait(self.driver, 2).until(
                EC.title_is(title_name[1])
            )
            return ele
        # except:
        #     print('【' + title_name[0] + '】与标题不符')

    # 判断元素内的文字
    def element_text_is(self, locate, element_text):
        #try:
            text = self.driver.find_element(locate[1], locate[2]).get_attribute('innerText')
            print(text)
            assert text == element_text
        #except:
           # print('文本不符，检查相关业务流程')

    # 获取剪切板
    def get_text(self):
        #打开剪切板
        w.OpenClipboard()
        # 获取剪切板内容
        board_string = w.GetClipboardData(win32con.CF_UNICODETEXT)
        # 关闭剪切板
        w.CloseClipboard()
        print(board_string)
        return board_string


    # 拼接字段
    def splice_text(self,text):
        print('%s%s'%('订单： ', text))
        return  '%s%s'%('订单： ', text)

    # 拆分字符串
    def split_text(self, text):
        print(text.split(':'))
        return text.split(':')

    # 刷新当前页面
    def refresh_page(self):
        self.driver.refresh()

    # 判断弹窗
    def warning_tip(self,locate):
        try:
            self.driver.find_element(locate[1]).click()
        except:
            pass


