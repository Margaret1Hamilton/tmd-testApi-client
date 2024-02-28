import os

class RedisConfig:
  host = '192.168.0.126'
  port = '6380'
  password = '123456'
  db = 11


baseHost = os.getenv('BASE_HOST') if os.getenv('BASE_HOST') else 'http://192.168.0.129:31000'
