#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask_admin.contrib.sqla import ModelView

from utils.admin import admin
from utils.db_tool import db

from .models import Choice, Question


admin.add_view(ModelView(Question, db.session, name='Question Manager'))
admin.add_view(ModelView(Choice, db.session, name='Choice Manager'))
