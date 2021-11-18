from selenium.webdriver.common.by import By


class Import_orders_page:
    import_orders_list_button = (
        '创建订单入口', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[1]/div/div/form/div[1]/div/div/button[2]')
    import_orders_button = ('批量导入订单', By.XPATH, '//*[contains(text(),"批量导入订单")]')
    import_orders_data = ('导入数据按钮', By.XPATH, '//*[contains(text(),"导入数据")]')
