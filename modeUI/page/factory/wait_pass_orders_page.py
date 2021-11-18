from selenium.webdriver.common.by import By

'''待审订单'''


class Wait_pass_orders_page:
    order_num_input = (
        '电商订单号输入框', By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[3]/div/div/input')

    search_button = ('搜索按钮', By.XPATH, '//*[contains(text(), "搜索")]')
    order_selected = ('选择订单', By.XPATH,
                      '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[1]/label/span')
    pass_button = ('搜索按钮', By.XPATH, '//*[contains(text(), "通过")]')
    expand_all = ('展开所有', By.XPATH, '//*[contains(text(), "展开所有")]')
    goods_num = ('商品号', By.XPATH, '//*[contains(text(), "商品号")]')
    confirm_button = ('确定按钮', By.XPATH, '//*[contains(text(), "确定")]')
    data_limit = (
        '展示条数', By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/div/span[1]/div/div/input')
    data_limit_ul = ('选中1000条', By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul')

    all_orders_checkbox = (
        '选中全部订单', By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[2]/div[1]/div[1]/label/span')
