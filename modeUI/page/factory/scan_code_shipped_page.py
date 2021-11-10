from selenium.webdriver.common.by import By

'''扫码发货'''


class Scan_code_shipped_page:
    scan_code_shipped_tab = ('扫码发货tab', By.XPATH, '//*[@id="tab-ShipmentIndex"]/div')
    scan_code_shipped_button = ('扫码发货', By.XPATH, '//*[contains(text(),"扫码发货")]')
    goods_code_input = ('商品号输入框', By.XPATH, '//input')
    confirm_button = ('确定', By.XPATH, '//*[contains(text(),"确定")]')
