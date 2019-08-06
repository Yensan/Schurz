#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import json
from os import path

from flask import session, request, Response, jsonify, flash, make_response
from flask import views, url_for, current_app

from .models import *
from utils.log import logger




class QuestionListView(views.MethodView):
    def post(self):
        question_text = request.json.get('question_text', None)
        q = Question(question_text=question_text, pub_date=datetime.now())
        options = request.json.get('options', [])
        q.choices = [
            Choice(choice_text=i['choice'], votes=0) for i in options
        ]
        db.session.add(q)
        db.session.commit()
        return 'success'

    def get(self):
        questions = Question.query.all()
        res = {}
        for i in questions:
            res[str(i.id)] = {
                'question_text': i.question_text,
                'publish': i.pub_date.strftime("%Y-%m-%d %H:%M:%S")
            }
            res[str(i.id)]['options'] = [
                {'choice': c.choice_text, 'votes': c.votes}
                for c in i.choices
            ]
        logger.warning(json.dumps(res, ensure_ascii=False))
        return json.dumps(res, ensure_ascii=False)

