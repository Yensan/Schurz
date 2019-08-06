#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import path

from flask import Flask, Config

from utils.webcore import register_url
from utils.log import logger, console_handler

from .urls import urlpatterns



class Applicaltion(Flask):
    def __init__(self, import_name):
        config = Config(root_path=path.dirname(path.abspath(__file__)))

        # get config from settings file
        config.from_pyfile(filename='settings.py', silent=False)

        # super init with basic info
        base_dir = getattr(config, 'BASE_DIR', path.dirname(path.dirname(path.abspath(__file__))))
        template = getattr(config, 'TEMPLATES', None)
        template = template[0]['DIRS'][0] if template else path.join(base_dir, 'templates')
        static = getattr(config, 'STATICFILES_DIRS', None)
        static = static[0] if static else path.join(base_dir, 'static')
        static_url = getattr(config, 'STATIC_URL', None)

        super(Applicaltion, self).__init__(
            import_name,
            template_folder=template,
            root_path=base_dir,
            static_folder=static,
            static_url_path=static_url,
            static_host=None,
        )

        # If settings not have item, keep it, otherwise replace it. Please don't use `self.config=config`
        for k in config: self.config[k] = config[k]

        # register URL from base URL patterns
        register_url(self, urlpatterns)

        # init Database with app settings
        from utils.db_tool import db
        db.init_app(self)

        # init Flask-Admin extension
        from utils.admin import admin
        admin.init_app(self)

        # Use Flask-Session instead of Flask default session.
        if self.config.get('SESSION_TYPE'):
            from flask_session import Session
            Session().init_app(self)

        # Use Flask-DebugToolbar: pip install flask-debugtoolbar
        # if self.debug:
        #     from flask_debugtoolbar import DebugToolbarExtension
        #     DebugToolbarExtension().init_app(self)

        # set logging Handler
        if not self.debug:
            logger.removeHandler(console_handler)
        self.logger = logger

app = Applicaltion(__name__)

# from aiohttp import web
# from aiohttp_wsgi import WSGIHandler
# wsgi_handler = WSGIHandler(app)
# app = web.Application()
# app.router.add_route('*', '/{path_info:.*}', wsgi_handler)


# insert functions into template engine
# app.add_template_global(UrlManager.buildStaticUrl,'buildStaticUrl')
# app.add_template_global(UrlManager.buildUrl,'buildUrl')

