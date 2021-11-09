from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Index_page():
    close_tip = ('提示关闭按钮', By.XPATH, '/html/body/div[3]/div/div[3]/div/button[1]')
    order_page_title = ('订单管理页面标题', '订单管理 - m2c店铺端')
    all_order_button = ('全部订单按钮', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[1]/div/div/div/div/div[1]/div')
    wait_manual_button = ('待手工解码', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[1]/div/div/div/div/div[2]/div/sup')
    manual_pull_button = ('手动拉单' , By.XPATH, '//*[@id="app"]/div/div/div/div/div[1]/div/div[2]/button')
    create_order_button = ('创建订单', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[1]/div/div/form/div[1]/div/div/button[1]')

    search_button = ('搜索按钮', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[1]/div/div/form/button[1]')
    order_num_input = ('订单号输入框', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[1]/div/div/form/div[2]/div/div[2]/input')
    buyer_id_input = ('买家ID', By.CLASS_NAME, 'flex_1 ml-5 el-input el-input--mini el-input--suffix')

    copy_order_num = ('复制订单号', By.CSS_SELECTOR, 'span.order>i','0')
    paste_order_num = ('Ctrl+V', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[1]/div/div/form/div[2]/div/div[2]/input', (Keys.CONTROL, 'v'))
    search_list_order_num = ('订单列表', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span[3]')

    order_checkBox = ('订单选中框', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/label/span[1]')
    confirm_express_button = ('确认选择快递', By.XPATH, '/html/body/div[12]/div/div[3]/button[2]')
    more_operate = ('更多操作', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[2]/div[2]/div[3]/div/div[7]/button/span')
    pre_shipping = ('预发货', By.XPATH, '//*/li[2]/button[1]')


