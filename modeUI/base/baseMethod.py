'''封装selenium的公共方法'''
import random
import win32con
from pandas.io.clipboard import set_clipboard
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC
import win32clipboard as w

from utils.config_yaml import YamlHandler


class BaseMethod(object):
    '''浏览器的常用封装操作'''

    # 打开浏览器
    # @pytest.fixture(scope='session')
    def open_browser(self, browser_name, url):
        try:
            if browser_name == 'Chrome':
                self.driver = webdriver.Chrome()
                self.driver.get(url)
            if browser_name == 'Opera':
                self.driver = webdriver.Opera()
                self.driver.get(url)
            if browser_name == 'firefox':
                self.driver = webdriver.firefox()
                self.driver.get(url)
            self.driver.maximize_window()
            return self.driver

        except Exception as e:
            print('cant open the browser!')
            raise e

    def quit_browser(self):
        try:
            self.driver.quit()
        except Exception as e:
            print('no driver!')
            raise e

    # 等待元素出现
    def wait_element_visiable(self, locate):
        try:
            ele = wait.WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((locate[1], locate[2]))
            )
            return ele
        except Exception as e:
            print(locate[0] + '的' + locate[2] + '元素未找到')
            raise e

    # 元素出现点击
    def click_until_visiable(self, locate):
        try:
            self.wait_element_visiable(locate).click()
        except Exception as e:
            print(locate[0] + 'cant click!')
            raise e

    # 加随机数 12位
    def add_random(self):
        data = random.randint(10000000000, 99999999999)
        return str(data)

    # 元素出现时输入
    def send_keys_until_visiable(self, locate, content):
        try:
            self.wait_element_visiable(locate).send_keys(content)
        except AttributeError as e:
            print('无输入属性')
            raise e

    # 清空文件内容
    def clear_file_content(self, file_path):
        f = open(file_path, 'r+')
        f.truncate()

    # 多个class取其中一个
    def more_class_click(self, locate):
        print(self.driver.find_elements(locate[1], locate[2], ))
        # self.driver.find_elements(locate[1], locate[2], )[locate[3]].click()

    # 动态下拉框，通过ul找li
    def select_option(self, ul_locate, option_num):
        self.wait_element_visiable(ul_locate).find_elements_by_xpath('li')[option_num - 1].click()

    # 点击空白/指定区域
    def click_fixed_area(self, xoffset, yoffset):
        # 左键点击（x，y）坐标位置
        ActionChains(self.driver).move_by_offset(xoffset, yoffset).click().perform()
        # 鼠标右键点击 （x，y）坐标位置
        # ActionChains(self.driver).move_by_offset(xoffset,yoffset).context_click().perform()

    # 页面下滑
    def down_turn(self):
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

    # 滑动至底部
    def dibu(self):
        js = "window.scrollTo(0,-document.body.scrollHeight)"
        self.driver.execute_script(js)

    # 滑动至元素可见
    def turn_down_element(self, locate):
        element = self.driver.find_element(locate[1], locate[2])
        self.driver.execute_script('arguments[0].scrollIntoView()', element)

    # 物理按键END
    def send_keyborad(self, locate):
        self.driver.find_element(locate[1], locate[2]).send_keys(locate[3])

    # 判断当前页面标题
    def page_title_is(self, title_name):
        # try:
        ele = wait.WebDriverWait(self.driver, 2).until(
            EC.title_is(title_name[1])
        )
        return ele

    # except:
    #     print('【' + title_name[0] + '】与标题不符')

    # 获取元素内文字
    def element_text_content(self, locate):
        text = self.driver.find_element(locate[1], locate[2]).get_attribute('innerText')
        return text

    # 判断元素内的文字
    def element_text_is(self, locate, element_text):
        # try:
        content = self.element_text_content(locate)
        print('操作人：' + content)
        assert content == element_text

    # except:
    # print('文本不符，检查相关业务流程')

    # 判断拆分后的字符串与剪切板
    def get_text_is(self, actual_text):
        assert self.get_text() == actual_text

    # 剪切板内容写入文件
    def from_copy_to_file(self, file):
        YamlHandler(file).write_yaml(self.get_text())

    # 写入剪切板
    def set_text(self, text):
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardText(text)
        w.CloseClipboard()

    # 获取剪切板
    def get_text(self):
        # 打开剪切板
        w.OpenClipboard()
        # 获取剪切板内容
        board_string = w.GetClipboardData(win32con.CF_UNICODETEXT)
        # 关闭剪切板
        w.CloseClipboard()
        return board_string

    # 拼接字段
    def splice_text(self, text):
        return '%s%s' % ('订单： ', text)

    # 拆分字符串
    def split_text(self, locate, start_num, end_num):
        text = self.driver.find_element(locate[1], locate[2]).get_attribute('innerText')
        print(text)
        a = text[start_num:end_num]  # -1 去掉空格

        return a

    # 刷新当前页面
    def refresh_page(self):
        self.driver.refresh()

    # 判断弹窗
    def warning_tip(self, locate):
        try:
            self.driver.find_element(locate[1]).click()
        except:
            pass
