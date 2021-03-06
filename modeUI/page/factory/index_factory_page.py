from selenium.webdriver.common.by import By

'''工厂主页元素'''


class Index_factory_page:
    wait_pass_orders = ('待审订单', By.XPATH, '//*[contains(text(), "待审订单")]')
    batch_management = ('批次管理', By.XPATH, '//*[contains(text(), "批次管理")]')

    system_configuration = ('系统设置', By.XPATH, '//*[contains(text(), "系统设置")]')
