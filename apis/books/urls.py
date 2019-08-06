#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from utils.webcore import url, include
from .views import *

urlpatterns = [
    # url('/counter/', CounterAPI.as_view('counter')),
    url('/questions', QuestionListView.as_view('counter')),
    url('/test/', test, name='test'),


]
