import datetime as dt
import requests


class OrderPage:
    '''先获取token， 传参'''
    def AllOrder(self):
        url = 'https://tcshop.jzm2c.com/shop/statistics/order/count'
        headers = {
           'authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImVkNWU4MGRjLTlkNDMtNDFjZi04ZGNkLTI5ODM0MmVhZDU2MSJ9.LhG8kCEq0IaBENPkswcIPQ9V5iN83RiZOBePT7ezYxw4kx83qRJdVFsqxgjcUQ90fo1kkRHaffRAD8JvLKdxWg'
        }
        fromTime = ''
        endtime = ''
        params = {
            'associateSplit': '1',
            'fromTime': '2021-10-25 00:00:00',
            'endTime': '2021-11-01 23:59:59',
            'pageSize':'500',
            'pageNum':'1',
            'status':'0'
        }
        res = requests.post(url=url,params=params,headers=headers)
        print(res.text)
        print(fromTime)
        print(endtime)
        assert res.status_code == 200


OrderPage().AllOrder()