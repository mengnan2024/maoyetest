from time import sleep

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from modeUI.base.baseMethod import BaseMethod
from modeUI.page.shop.create_order_page import Create_order_page
from modeUI.page.shop.login_page import Login_page
from modeUI.page.shop.manual_order_page import Manual_order_page
from modeUI.page.shop.index_page import Index_page

'''订单管理'''
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
        self.warning_tip(Index_page.close_tip)  # 关闭提示按钮


        '''手动拉单'''
        # self.click_until_visiable(Index_page.manual_pull_button)  # 手动拉单
        # #self.click_until_visiable(Index_page.order_num_radio)  # 电商订单号
        # self.click_until_visiable(Manual_order_page.shop_type_selectBox)  # 点击店铺类型
        # self.select_option(Manual_order_page.shop_type_ul, 1)  # 选择店铺类型
        # self.click_until_visiable(Manual_order_page.download_shop_selectBox)  # 点击下载店铺
        # self.select_option(Manual_order_page.download_shop_ul, 1)  # 选择下载店铺
        # self.click_fixed_area(800, 300)  # 点击其他区域
        # #self.click_until_visiable(Manual_order_page.close_download_button)  # 点击关闭
        # self.click_until_visiable(Manual_order_page.start_download_button)  # 点击开始
        # sleep(40)  # 等待执行40s
        # self.element_text_is(Manual_order_page.start_download_button,
        #                      '完成')  # 判断按钮文字【完成】                                                          #判断按钮文字是不是【完成】
        # self.click_until_visiable(Manual_order_page.start_download_button)  # 点击完成
        #
        # # '''创建订单'''
        # self.click_until_visiable(Index_page.create_order_button) #点击创建订单按钮
        # self.send_keys_until_visiable(Create_order_page.name,'自动化脚本创建的订单') #收货人
        # self.send_keys_until_visiable(Create_order_page.mobile, '99999999') #收货人手机
        # self.click_until_visiable(Create_order_page.area_province)
        # self.select_option(Create_order_page.area_province_ul, 1) #选择省份
        # self.click_until_visiable(Create_order_page.area_city)
        # self.select_option(Create_order_page.area_city_ul, 1) # 选择城市
        # self.click_until_visiable(Create_order_page.area_county)
        # self.select_option(Create_order_page.area_county_ul, 1) # 选择区县
        # self.send_keys_until_visiable(Create_order_page.street, '测试2街道') # 填写街道
        # self.send_keys_until_visiable(Create_order_page.seller_note, '------------autoTest----------') # 卖家备注
        # self.click_until_visiable(Create_order_page.express_selection)
        # self.select_option(Create_order_page.express_selection_ul, 1) # 选择快递
        # self.send_keys_until_visiable(Create_order_page.buyer_id, '2333333333333')  # 买家id
        #
        #
        # self.click_until_visiable(Create_order_page.texture)
        # self.select_option(Create_order_page.texture_ul, 1)  # 选择材质
        # self.click_until_visiable(Create_order_page.color)
        # self.select_option(Create_order_page.color_ul, 3)  # 选择颜色
        # self.click_until_visiable(Create_order_page.mobile_mode)
        # self.send_keys_until_visiable(Create_order_page.mobile_mode, 'iphone12')
        # self.select_option(Create_order_page.mobile_mode_ul, 1)  # 选择型号'''
        # self.click_until_visiable(Create_order_page.picture_num)
        # self.send_keys_until_visiable(Create_order_page.picture_num, '骑车奥特曼')
        # self.select_option(Create_order_page.picture_num_ul, 1)   # 选择图片编码
        #
        # self.turn_down_element(Create_order_page.confirm_button) # 下滑至确定按钮出现
        # self.click_until_visiable(Create_order_page.confirm_button) # 确定
        #
        # sleep(1)
        # # '''订单搜索'''
        # self.click_until_visiable(Index_page.copy_order_num)  # 复制刚才生成的订单号
        # self.send_keyborad(Index_page.paste_order_num)  # 粘贴订单号
        # self.click_until_visiable(Index_page.search_button)  # 点击搜索
        # self.get_text_is(actual_text=self.split_text(Index_page.search_list_order_num)) # 判断搜索结果匹配

        '''预发货'''
        self.click_until_visiable(Index_page.order_checkBox) # 选中订单
        self.click_until_visiable(Index_page.more_operate) # 更多操作
        sleep(4)
        self.click_until_visiable(Index_page.pre_shipping) # 预发货
        sleep(4)
        self.click_until_visiable(Index_page.confirm_express_button) # 确认预发货
        # '''推单'''

        '''修改收货地址'''

        '''合并订单？？？？'''

        '''刷新编码'''

        sleep(5)
        self.driver.quit()
