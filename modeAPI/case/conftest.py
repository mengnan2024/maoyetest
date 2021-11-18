import pytest
import requests


# 在调用的方法参数中写入方法名即可调用，不需要实例化

@pytest.fixture(scope="session")
def get_token():
    url = 'https://tcshop.jzm2c.com/shop/login'
    data_params = {
        "username": "AutoTest",
        "password": "f1eee8efd4d339bb0b21e8be4f786b12"
    }
    data = requests.post(url=url, json=data_params)
    print(data.text)
    return data.json()["token"]
