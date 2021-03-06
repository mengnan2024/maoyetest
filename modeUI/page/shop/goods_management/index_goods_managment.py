from selenium.webdriver.common.by import By


class Index_goods_management:
    goods_management_tag = ('商品管理标签', By.XPATH, '//*[contains(text(), "商品管理")]')
    goods_page_title = ('商品管理页面标题', 'SKU全映射 - m2c店铺端')
    goods_mapping_tag = ('商品映射管理', By.XPATH, '//*[contains(text(), "商品映射管理")]')
    all_mapping_tag = ('全映射管理', By.XPATH, '//*[contains(text(), "全映射管理")]')
    all_order_selected = ('全部商品', By.XPATH,
                          '//*[@id="app"]/div/div/section/div/div[2]/div/div[3]/div/div[2]/div/div[2]/table/thead/tr/th[1]/div/label/span/span')
    batch_decode = ('批量解码', By.XPATH, '//*[contains(text(), "批量解码")]')
    confirm_button = ('确认', By.XPATH, '//*[contains(text(), "确定")]')
    batch_decode_page_text = ('批量解码', By.XPATH, '/html/body/div[4]/div/div[1]/span', '批量解码')
    end_process = ('强制终止', By.XPATH, '//*[contains(text(), "强制终止")]')

    batch_clear_decode = ('批量清除解码', By.XPATH, '//*[contains(text(), "批量清除解码")]')
    download_goods_button = ('下载商品按钮', By.XPATH, '//*[contains(text(), "下载商品")]')
    download_goods_page_text = ('商品下载', By.XPATH, '//*[@id="app"]/div/div/section/div/div[3]/div/div[1]/span', '商品下载')
    all_shop_selected = ('全选', By.XPATH, '//*[@id="app"]/div/div/section/div/div[3]/div/div[2]/div[1]/fieldset[1]/form/div[2]/div/label/span[1]')
    download_button = ('下载', By.XPATH, '//*[contains(text(), "下载")]')

