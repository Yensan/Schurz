#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .settings import *

DATABASES = {
        'test': {
            'ENGINE': 'sqlite',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

SQLALCHEMY_DATABASE_URI = make_DATABASE_URI(DATABASES['test'])
DEBUG = True






