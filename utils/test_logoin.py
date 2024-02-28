import os
import pytest
import redis
import requests

from utils.logger import logger

@pytest.fixture(scope="session")
def redis_client():
    host = '192.168.0.126'
    port = 6380
    requests.post

    client = redis.Redis(host=host, port=port, password='', encoding="utf-8", decode_responses=True, db=11)
    # tmd=client.get('tmd')
    # client.set('foo', 'bar')
    a = client.get('tmd:admin_login:code::Jason.chen@spotec.net2024-02-22')
    logger.info('2222222')
    logger.info(a)

    yield client



# def test_login_and_request_api(redis_client):
    # 从 Redis 中读取验证码
    # redis_client.set('foo', 'bar')
    # a = redis_client.get('foo')
    # openapi_client.api.comment_api.CommentApi()
    # logger.info('a')
    # verification_code = redis_client.hgetall('tmd:area')
    # logger.info(verification_code)

    # # 模拟登录请求，提交验证码并获取 token
    # login_response = requests.post('https://example.com/login', data={'code': verification_code})
    # assert login_response.status_code == 200
    # token = login_response.json()['token']

    # # 使用获取的 token 请求其他 API
    # headers = {'Authorization': f'Bearer {token}'}
    # api_response = requests.get('https://example.com/api', headers=headers)
    # assert api_response.status_code == 200


