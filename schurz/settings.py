#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.cnblogs.com/wupeiqi/p/7552008.html
import os, sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
# sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ba(*72n&q!i5-qo*e$g10_7cep_sqo@+ocee0png_b$0x#p#_!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if DEBUG:
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True
ALLOWED_HOSTS = []

# SERVER_PORT = 5000
# SERVER_HOST = '127.0.0.1'
#
# SERVER_NAME = '{}:{}'.format(SERVER_HOST, SERVER_PORT)


# Database
DATABASES = {
        'test': {
            'ENGINE': 'sqlite',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
        'default': {
            'ENGINE': 'mysql',
            'OPTIONS': {'charset': 'utf8', 'init_command': "SET default_storage_engine=INNODB;"},
            'NAME': 'testdb',
            'USER': 'root',
            'PASSWORD': 'root',
            "PORT": "3306",
            "HOST": "192.168.1.173"
        }
    }
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"
# 'mysql://username:password@server/db'
from utils.db_tool import make_DATABASE_URI
# SQLALCHEMY_DATABASE_URI = make_DATABASE_URI(DATABASES['test'])


MONGODB_SETTINGS = {
    'connect': False, # `True` will connect as `init_app`; `False` will not connect until use mongo
    'host': '127.0.0.1',
    'port': 27017,
    'db': 'test',
    # 'username': 'root',
    # 'password': 'root'
}

# STATIC_URL = '/static/'
STATIC_URL = '/static'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
MEDIA_DIR = os.path.join(BASE_DIR, 'static', 'media')


# Flask-Admin
FLASK_ADMIN_SWATCH = 'cerulean'

# Compress
COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml',
                      'application/json', 'application/javascript']
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 512

# Internationalization
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

