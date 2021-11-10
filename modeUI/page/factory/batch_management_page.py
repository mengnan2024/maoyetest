from selenium.webdriver.common.by import By


class Batch_management:
    goods_id = ('商品ID', By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div/form/div[2]/div/div/input')
    search_button = ('搜索按钮', By.XPATH, '//*[contains(text(), "搜索")]')
    order_selected = ('选择订单', By.XPATH,
                      '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span')
    merge_batch = ('合成批次', By.XPATH, '//*[contains(text(), "合成批次")]')
    wait_create_tag = ('待生成', By.XPATH, '//*[contains(text(), "待生成")]')
    already_create_tag = ('已生成', By.XPATH, '//*[contains(text(), "已生成")]')

    batch_num = ('批次号', By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div/form/div[2]/div/div/input')
