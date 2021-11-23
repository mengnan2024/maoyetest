from selenium.webdriver.common.by import By

'''系统设置'''


class System_configuration_page:
    printer_conf = ('打印机设置', By.XPATH, '//*[contains(text(),"打印机设置")]')
    tag_configuration = ('标签设置', By.XPATH, '//*[contains(text(),"标签设置")]')
    rotas_conf = ('面单设置', By.XPATH, '//*[contains(text(),"面单设置")]')

    # 标签设置
    printer_name = (
        '打印机名称', By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/form/div[1]/div/div/div[1]')
    printer_name_ul = ('打印机选项', By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul')
    template_radio = ('模板', By.XPATH,
                      '//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/form/div[2]/div/div/div[1]/div/label/span[1]/span')
    save_btn = ('保存按钮', By.XPATH, '//*[contains(text(), "保 存")]')

    # 面单设置
    add_rotas_configuration = ('新增面单设置', By.XPATH, '//*[contains(text(), "新增")]')
    express_selection = ('快递公司', By.XPATH, '/html/body/div[4]/div/div[2]/form/div[1]/div/div/div')
    express_selection_ul = ('选择快递公司', By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul')
    printer_name_rotas = ('面单的打印机名称', By.XPATH, '/html/body/div[3]/div/div[2]/form/div[2]/div/div/div')
    printer_name_rotas_ul = ('面单的打印机选项', By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul')
    confirm_button = ('确定', By.XPATH, '//*[contains(text(),"确 定")]')
