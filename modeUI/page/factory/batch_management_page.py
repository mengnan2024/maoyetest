from selenium.webdriver.common.by import By

'''批次管理'''


class Batch_management_page:
    wait_create_tag = ('待生成', By.XPATH, '//*[contains(text(), "待生成")]')
    already_create_tag = ('已生成', By.XPATH, '//*[contains(text(), "已生成")]')
    goods_id = ('商品ID', By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div/form/div[2]/div/div/input')
    search_button = ('搜索按钮', By.XPATH, '//*[contains(text(), "搜索")]')
    order_selected = ('选择订单', By.XPATH,
                      '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[1]/div/label/span')
    merge_batch = ('合成批次', By.XPATH, '//*[contains(text(), "合成批次")]')

    batch_num = (
        '批次号输入框', By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div/form/div[2]/div/div/input')
    batch_first = ('第一个批次', By.XPATH,
                   '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span')
    operate_er = ('操作人', By.XPATH,
                  '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div')
    current_username = ('当前账号用户名', By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[3]/div[2]/div')

    print_tag_button = ('打印标签', By.XPATH,
                        '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[14]/div/div/button[1]')
    set_printer = ('设置打印机', By.XPATH, '//*[contains(text(), "设置打印机")]')

    batch_management_tab = ('批次管理标签', By.XPATH, '//*[@id="tab-ProductionBatch"]/div')


class Batch_management:
    goods_id = ('商品ID', By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div/form/div[2]/div/div/input')
    search_button = ('搜索按钮', By.XPATH, '//*[contains(text(), "搜索")]')
    order_selected = ('选择订单', By.XPATH,
                      '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span')
    merge_batch = ('合成批次', By.XPATH, '//*[contains(text(), "合成批次")]')
    wait_create_tag = ('待生成', By.XPATH, '//*[contains(text(), "待生成")]')
    already_create_tag = ('已生成', By.XPATH, '//*[contains(text(), "已生成")]')

    batch_num = ('批次号', By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div/form/div[2]/div/div/input')
