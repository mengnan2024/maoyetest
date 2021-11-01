import pytest
import requests

@pytest.fixture(scope='session')
def get_token():
    url = ''
    params = ''
    data = requests.post(url,params)

    return data