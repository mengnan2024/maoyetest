import pytest
import requests

@pytest.fixture(scope="session")
def get_token():
    url = 'https://test-api.hmhyg.com/tp5/api/UserLogin/webLogin'
    params = {
        "phone": 13955557777,
        "sjyzm": 999999,
        "tg": "",
        "format": "json",
        "hmcode": "webmall",
        "terminal": "webmall"}
    data = requests.post(url, params)

    return data.json()["data"]["access_token"]