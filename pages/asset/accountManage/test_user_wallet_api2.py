import pytest

from utils.login import login


@pytest.fixture(scope="module")
def rest_client():
    yield login(account='jason.chen@spotec.net', password='abc123').get('rest_client_func')


def test_string_only(rest_client):
    res = rest_client.request(method="get", path="/api/h5/userWallet/asset/web")
    code = res['header']['code']
    currency = res['body']['currency']
    print('res1', res)
    assert code == '0000'
    assert currency == '0.00'


