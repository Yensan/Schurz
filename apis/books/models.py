#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from utils.db_tool import db

# https://www.cnblogs.com/wupeiqi/articles/8259356.html
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False, comment='question text')
    pub_date = db.Column(db.DATETIME, nullable=False, default=datetime.utcnow,)

    def __str__(self):
        return '<Question %r>' % self.question_text


class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # question = db.ForeignKey(Question, on_delete=models.CASCADE)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    question = db.relationship('Question', backref='choices')

    # choice_text = models.CharField(max_length=200)
    choice_text = db.Column(db.String(200))
    # votes = models.IntegerField(default=0)
    votes = db.Column(db.Integer(), default=18)

