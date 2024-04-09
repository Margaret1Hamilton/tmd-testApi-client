import pytest

from utils.login import login

from utils.login import login


@pytest.fixture(scope="module")
def rest_client():
    yield login(account='Lena.liu@spotec.net', password='abc123').get('rest_client_func')


class Test_user_wallet_api:
    def test_string_only1(self, rest_client):
        account_value = rest_client.request(method="get", path="/api/h5/userWallet/asset/web")
        print('2222', account_value)
        assert ['adasdfasfd'] == ['adasdfasfd']

