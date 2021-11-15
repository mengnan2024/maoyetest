import requests


class Test_logger:
    def test_01(self):
        res = requests.get(
            'https://cn.bing.com/search?q=pytest+%E6%97%A5%E5%BF%97%E5%AD%98%E5%82%A8&qs=n&form=QBRE&sp=-1&pq=pytest+%E6%97%A5%E5%BF%97cunchu&sc=0-15&sk=&cvid=CA4B6713DCB34B86A2FD610F781BA4EE')

        assert res.status_code == 200
        res.close()

    def test_02(self):
        assert 1 == 2
