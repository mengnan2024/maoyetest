'''数据组合'''
from random import randint


class DataCombo:
    def create_more_order(self, file_path, num, buyer_id):  # file_path 文件路径，  num 生成条数
        from utils.get_excel import writeToExcel
        for i in range(num):
            content = {
                # 线上环境 UI脚本的店铺  S16371997324510411 , 代发厂1040
                # 测试环境 金泽的淘宝店  S16073217218440554, 代发厂1003
                # 测试环境 UI脚本    S16372954322749701 ， 代发厂1043
                '所属店铺*': 'S16375619093589416',
                '代发厂*': '1043',
                '订单号': 'TG211116164223' + str(randint(1000000000000000, 9999999999999999)),
                '商品SKU编码*': 'BLK-XM5-DQ-OF0029',
                '材质': '玻璃壳',
                '颜色': '淡青',
                '型号': '小米5',
                '收件人姓名*': 'xxx',
                '收件人联系方式*': '11',
                '省*': '广东',
                '市*': '深圳',
                '区*': 'xx区',
                '收件人详细地址*': 'xx单元xx号' + str(randint(1000000000000000, 9999999999999999)),
                '发货快递': 'YTO',
                '买家ID': buyer_id

            }
            writeToExcel(file_path, sheet_name='Sheet1', content=content)
