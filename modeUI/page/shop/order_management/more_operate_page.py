from selenium.webdriver.common.by import By


class More_operate():
    pre_shipping = ('预发货', By.XPATH, '//*[contains(text(),"预发货")]')
    refresh_code = ('刷新编码', By.XPATH, '//*[contains(text(),"刷新编码)]')
    merge_order = ('合并订单', By.XPATH, '//*[contains(text(), "合并订单")')
