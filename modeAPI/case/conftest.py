import pytest
import requests
"""获取token"""
@pytest.fixture(scope='session')
def get_token():
    url = ''
    params = ''
    data = requests.post(url,params)

    return data