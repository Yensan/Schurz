#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def make_DATABASE_URI(DBdict):
    # dialect+driver://username:password@host:port/database
    # engine://auth@server/db
    auth = server = db = ''
    dbdict = {k.lower() : v for k, v in DBdict.items()}
    engine = dbdict.get('engine')
    if not engine: raise RuntimeError('Database settings wrong.')
    user = dbdict.get('user')
    if user:
        password = dbdict.get('password')
        if not password: raise RuntimeError('Database settings wrong.')
        auth = user + ':' + password
    host = dbdict.get('host')
    if host:
        port = dbdict.get('port')
        if not port: raise RuntimeError('Database settings wrong.')
        server = '@' + host + ':' + port
    if engine != 'sqlite' and not (server and auth):
        raise RuntimeError('Database settings wrong.')
    db = dbdict.get('name')
    return '{}://{}{}/{}'.format(engine, auth, server, db)



if __name__ == '__main__':
    import os, sys

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    DATABASES = {
        'test': {
            'ENGINE': 'sqlite',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
        'default': {
            'ENGINE': 'mysql',
            'OPTIONS': {'charset': 'utf8', 'init_command': "SET default_storage_engine=INNODB;"},
            'NAME': 'wxrobot',
            'USER': 'root',
            'PASSWORD': 'root',
            "PORT": "3306",
            "HOST": "192.168.1.173"
        }
    }
    a = make_DATABASE_URI(DBdict=DATABASES['default'])
    b = make_DATABASE_URI(DBdict=DATABASES['test'])
    print(b)

