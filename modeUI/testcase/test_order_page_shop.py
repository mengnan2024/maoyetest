from time import sleep
from modeUI.base.baseMethod import BaseMethod
from modeUI.page.shop.create_order_page import Create_order_page
from modeUI.page.shop.login_page import Login_page
from modeUI.page.shop.manual_order_page import Manual_order_page
from modeUI.page.shop.index_page import Index_page


class Test_order_page(BaseMethod):
    def test_order_page(self):
        '''登录'''
        self.open_browser('Chrome', 'https://tcshop.jzm2c.com/login')  # 打开页面
        self.send_keys_until_visiable(Login_page.username_input, '时涛')  # 输入用户名
        self.send_keys_until_visiable(Login_page.password_input, '123456')  # 输入密码
        self.click_until_visiable(Login_page.password_hidden)  # 点击隐藏密码按钮
        self.click_until_visiable(Login_page.remember_password)  # 点击记住密码
        self.click_until_visiable(Login_page.login_button)  # 点击登录
        self.page_title_is(Index_page.order_page_title)  # 判断标题

        # '''手动拉单'''
        # self.click_until_visiable(Index_page.manual_pull_button)  # 手动拉单
        # # self.click_until_visiable(Order_page.order_num_radio)  # 电商订单号
        # self.click_until_visiable(Manual_order_page.shop_type_selectBox)  # 点击店铺类型
        # self.select_option(Manual_order_page.shop_type_ul, 1)  # 选择店铺类型
        # self.click_until_visiable(Manual_order_page.download_shop_selectBox)  # 点击下载店铺
        # self.select_option(Manual_order_page.download_shop_ul, 1)  # 选择下载店铺
        # self.click_fixed_area(800, 300)  # 点击其他区域
        # # self.click_until_visiable(Manual_order_page.close_download_button)  # 点击关闭
        # self.click_until_visiable(Manual_order_page.start_download_button)  # 点击开始
        # sleep(40)  # 等待执行40s
        # self.element_text_is(Manual_order_page.start_download_button,
        #                      '完成')  # 判断按钮文字【完成】                                                          #判断按钮文字是不是【完成】
        # self.click_until_visiable(Manual_order_page.start_download_button)  # 点击完成

        '''创建订单'''
        self.click_until_visiable(Index_page.create_order_button) #点击创建订单按钮
        self.send_keys_until_visiable(Create_order_page.name,'自动化脚本创建的订单') #收货人
        self.send_keys_until_visiable(Create_order_page.mobile, '99999999') #收货人手机
        self.click_until_visiable(Create_order_page.area_province)
        self.select_option(Create_order_page.area_province_ul, 1) #选择省份
        self.click_until_visiable(Create_order_page.area_city)
        self.select_option(Create_order_page.area_city_ul, 1) # 选择城市
        self.click_until_visiable(Create_order_page.area_county)
        self.select_option(Create_order_page.area_county_ul, 1) # 选择区县
        self.send_keys_until_visiable(Create_order_page.street, '测试街道') #填写街道
        self.send_keys_until_visiable(Create_order_page.seller_note, '------------autoTest----------')

        self.click_until_visiable(Create_order_page.texture)
        self.select_option(Create_order_page.texture_ul, 1)  # 选择材质
        self.click_until_visiable(Create_order_page.color)
        self.select_option(Create_order_page.color_ul, 3)  # 选择颜色
        self.click_until_visiable(Create_order_page.mobile_mode)
        self.select_option(Create_order_page.mobile_mode_ul, 1)  # 选择型号





