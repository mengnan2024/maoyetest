from selenium.webdriver.common.by import By


class Index_factory_page:
    wait_pass_orders = ('待审订单', By.XPATH, '//*[contains(text(), "待审订单")]')
    batch_management = ('批次管理', By.XPATH, '//*[contains(text(), "批次管理")]')

