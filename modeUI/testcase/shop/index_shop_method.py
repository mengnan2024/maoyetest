from time import sleep

from modeUI.base.baseMethod import BaseMethod
from modeUI.page.shop.order_management.create_order_page import Create_order_page
from modeUI.page.shop.order_management.index_order_management_page import Index_page
from modeUI.page.shop.order_management.manual_order_page import Manual_order_page
from modeUI.page.shop.order_management.more_operate_page import More_operate
from utils.config_yaml import YamlHandler

'''主页操作'''


class Index_page_method(BaseMethod):

    # 手动创建订单
    def create_order_method(self):
        self.click_until_visiable(Index_page.create_order_button)  # 点击创建订单按钮
        self.send_keys_until_visiable(Create_order_page.name, '自动化脚本创建的订单')  # 收货人
        self.send_keys_until_visiable(Create_order_page.mobile, '99999999')  # 收货人手机
        self.click_until_visiable(Create_order_page.area_province)
        self.select_option(Create_order_page.area_province_ul, 1)  # 选择省份
        self.click_until_visiable(Create_order_page.area_city)
        self.select_option(Create_order_page.area_city_ul, 1)  # 选择城市
        self.click_until_visiable(Create_order_page.area_county)
        self.select_option(Create_order_page.area_county_ul, 1)  # 选择区县
        self.send_keys_until_visiable(Create_order_page.street, '测试街道' + self.add_random())  # 填写街道
        self.send_keys_until_visiable(Create_order_page.seller_note, '------------autoTest----------')  # 卖家备注
        self.click_until_visiable(Create_order_page.express_selection)
        self.select_option(Create_order_page.express_selection_ul, 1)  # 选择快递
        self.send_keys_until_visiable(Create_order_page.buyer_id, '2333333333333')  # 买家id
        sleep(2)
        self.click_until_visiable(Create_order_page.texture)
        self.select_option(Create_order_page.texture_ul, 1)  # 选择材质
        self.click_until_visiable(Create_order_page.color)
        self.select_option(Create_order_page.color_ul, 3)  # 选择颜色
        self.click_until_visiable(Create_order_page.mobile_mode)
        self.send_keys_until_visiable(Create_order_page.mobile_mode, 'iphone12')
        self.select_option(Create_order_page.mobile_mode_ul, 1)  # 选择型号'''
        self.click_until_visiable(Create_order_page.picture_num)
        self.send_keys_until_visiable(Create_order_page.picture_num, '骑车奥特曼')
        self.select_option(Create_order_page.picture_num_ul, 1)  # 选择图片编码

        self.turn_down_element(Create_order_page.confirm_button)  # 下滑至确定按钮出现
        self.click_until_visiable(Create_order_page.confirm_button)  # 确定

    # 手动拉单
    def manual_order_method(self):
        self.click_until_visiable(Index_page.manual_pull_button)  # 手动拉单
        # self.click_until_visiable(Index_page.order_num_radio)  # 电商订单号
        self.click_until_visiable(Manual_order_page.shop_type_selectBox)  # 点击店铺类型
        self.select_option(Manual_order_page.shop_type_ul, 1)  # 选择店铺类型
        self.click_until_visiable(Manual_order_page.download_shop_selectBox)  # 点击下载店铺
        self.select_option(Manual_order_page.download_shop_ul, 1)  # 选择下载店铺
        self.click_fixed_area(800, 300)  # 点击其他区域
        # self.click_until_visiable(Manual_order_page.close_download_button)  # 点击关闭
        self.click_until_visiable(Manual_order_page.start_download_button)  # 点击开始
        sleep(40)  # 等待执行40s
        self.element_text_is(Manual_order_page.start_download_button,
                             '完成')  # 判断按钮文字【完成】                                                          #判断按钮文字是不是【完成】
        self.click_until_visiable(Manual_order_page.start_download_button)  # 点击完成

    # 搜索订单
    def search_list_order(self, file_path):
        data = self.split_text(Index_page.search_list_order_num, 4, -1)  # 获取第一条的订单号
        YamlHandler(file_path).write_yaml({'order_num': data})  # 单号写入yaml

        self.send_keys_until_visiable(Index_page.paste_order_num, data)  # 填入搜索框
        sleep(2)

        self.click_until_visiable(Index_page.search_button)  # 点击搜索
        # self.get_text_is(actual_text=self.split_text(Index_page.search_list_order_num))  # 判断搜索

    # 订单推送
    def push_order(self):
        self.click_until_visiable(Index_page.order_checkBox1)  # 选中订单
        self.click_until_visiable(Index_page.push_order_button)  # 订单推送
        self.click_until_visiable(Index_page.confirm_button)  # 确认

    # 更多操作
    ##  1. 预发货
    def pre_shipping_method(self):
        self.click_until_visiable(Index_page.order_checkBox1)  # 选中订单
        self.click_until_visiable(Index_page.more_operate)  # 更多操作
        self.click_until_visiable(More_operate.pre_shipping)  # 预发货
        self.click_until_visiable(Index_page.confirm_button)  # 确认

    ##  2. 合并订单
    def merge_order_method(self):
        self.click_until_visiable(Index_page.order_checkBox1)  # 选中两个合并订单
        self.click_until_visiable(Index_page.order_checkBox2)
        self.click_until_visiable(Index_page.more_operate)  # 更多操作
        self.click_until_visiable(More_operate.merge_order)  # 合并订单
        self.click_until_visiable(Index_page.confirm_button)  # 确认

    ##  3. 刷新编码
    def refresh_code_page(self):
        self.click_until_visiable(Index_page.order_checkBox1)  # 选中订单
        self.click_until_visiable(Index_page.more_operate)  # 更多操作
        self.click_until_visiable(More_operate.refresh_code)  # 刷新编码
        self.click_until_visiable(Index_page.confirm_button)  # 确认
