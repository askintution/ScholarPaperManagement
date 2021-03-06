# MONGODB_SETTINGS = {'db': 'test_11',
#                     'host': 'mongodb://dds-wz9f23f0cffe4b341504-pub.mongodb.rds.aliyuncs.com:3717,dds-wz9f23f0cffe4b342338-pub.mongodb.rds.aliyuncs.com:3717',
#                     'username': 'root',
#                     'password': 'qwerty2019()-=',
#                     'authentication_source': 'admin',
#                     'authentication_mechanism': 'SCRAM-SHA-1',
#                     'replicaset':'mgset-15064123',
#                     }  # 设置mongodb的数据库
MONGODB_DB = 'test_11'

PASSWORD_SECRET = 'secret_for_ensure_password_security'
TOKEN_SECRET = 'secret_for_ensure_token_security'
JWT_TOKEN_LOCATION = 'cookies'
JWT_ACCESS_TOKEN_EXPIRES = 86400    # 1天的期限
JWT_BLACKLIST_ENABLED = True        # 设置黑名单以完成logout功能
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
JWT_COOKIE_CSRF_PROTECT = False     # CSRF保护
