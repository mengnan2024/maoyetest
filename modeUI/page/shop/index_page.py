from selenium.webdriver.common.by import By


class Index_page():
    order_page_title = ('订单管理页面标题', '订单管理 - m2c店铺端')
    all_order_button = ('全部订单按钮', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[1]/div/div/div/div/div[1]/div')
    wait_manual_button = ('待手工解码', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[1]/div/div/div/div/div[2]/div/sup')
    manual_pull_button = ('手动拉单' , By.XPATH, '//*[@id="app"]/div/div/div/div/div[1]/div/div[2]/button')
    create_order_button = ('创建订单', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[1]/div/div/form/div[1]/div/div/button[1]')