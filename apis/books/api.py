#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Blueprint
from utils.webcore import register_url

from .urls import urlpatterns
from .drops import *
from . import admin  # noqa  这样才能激活后台。

books = Blueprint(
    name='books', import_name=__name__,
    # template_folder='templates', static_folder='static'
)

books.before_request(check_ContentType)

books.after_request(cross_domain)

books.context_processor(csrf_token)

register_url(books, urlpatterns)
