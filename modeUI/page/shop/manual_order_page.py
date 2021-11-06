from selenium.webdriver.common.by import By

'''手动拉单'''
class Manual_order_page():
    shop_order_radio = ('店铺订单', By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div[1]/fieldset[1]/form/div[1]/div/div/label[1]/span[2]')
    order_num_radio = ('电商订单号', By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/fieldset/form/div[1]/div/div/label[2]/span[2]')
    shop_type_selectBox = ('店铺类型', By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/fieldset[1]/form/div[2]/div/div/div/input')
    shop_type_ul = ('店铺', By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul')
    download_shop_selectBox = ('选择下载店铺', By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div[1]/fieldset[1]/form/div[3]/div/div[1]/div[1]/input')
    download_shop_ul = ('具体店铺', By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul')
    close_download_button = ('【关闭】', By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/button[1]')
    start_download_button = ('【开始】', By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/button[2]')
