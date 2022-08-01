import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
LANGUAGE_CODE = 'zh-hans'


# 配置Redis缓存信息
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 腾讯cos储存
TENCENT_COS_ID = "AKID73i7F6gz1mFSP5TaR1JK5ZlgLiodARN2"
TENCENT_COS_KEY = "RcW9UZMs75mBJAl58uPdZEcjZ8PQAdoi"

# 阿里沙箱环境
ALI_APPID = 2021000119658187
ALI_NOTIFY_URL = 'http://127.0.0.1:8000/pay/notify/'
ALI_RETURN_URL = 'http://127.0.0.1:8000/pay/notify/'
ALI_PRI_KEY_PATH = os.path.join(BASE_DIR, r'keys\app_private_key.pem')
ALI_PUB_KEY_PATH = os.path.join(BASE_DIR, r'keys\alipay_public_key.pem')
ALI_GATEWAY = 'https://openapi.alipaydev.com/gateway.do'
