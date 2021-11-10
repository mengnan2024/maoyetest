from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Create_order_page:
    name = ('收货人', By.XPATH,'//*[@id="app"]/div/div/section/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/form/div[3]/div[1]/div/div/input')
    mobile = ('收货人手机', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/form/div[3]/div[2]/div/div/input')
    area_province = ('省份', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/form/div[4]/div[1]/div/div/div/input')
    area_province_ul = ('选择省份', By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul')
    area_city = ('城市', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/form/div[4]/div[2]/div/div/div[1]/input')
    area_city_ul = ('选择城市', By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul')
    area_county = ('区县', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/form/div[4]/div[3]/div/div/div[1]/input')
    area_county_ul = ('选择区县', By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul')
    street = ('街道地址', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/form/div[5]/div/div/div/input')
    seller_note = ('卖家备注', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/form/div[6]/div/div/div/input')
    express_selection = ('快递公司', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/form/div[7]/div/div/div/div')
    express_selection_ul = ('选择快递公司', By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul')
    buyer_id = ('买家ID', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/form/div[8]/div/div/div/input')

    texture = ('材质', By.XPATH, '//*[@id="pane-1"]/div/div[2]/div[1]/div/div/div/input')
    texture_ul = ('选材质', By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul')
    color = ('颜色', By.XPATH, '//*[@id="pane-1"]/div/div[2]/div[2]/div/div/div/input')
    color_ul = ('选颜色', By.XPATH, '/html/body/div[8]/div[1]/div[1]/ul')
    mobile_mode = ('手机型号', By.XPATH, '//*[@id="pane-1"]/div/div[3]/div[1]/div/div/div[1]/input')
    mobile_mode_ul = ('选手机型号', By.XPATH, '/html/body/div[9]/div[2]/div[1]/ul')
    picture_num = ('图案编码', By.XPATH, '//*[@id="pane-1"]/div/div[4]/div/div/div/div[1]/input')
    picture_num_ul = ('选图案编码', By.XPATH, '/html/body/div[10]/div[1]/div[1]/ul')
    confirm_button = ('确定按钮', By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/button[2]')
