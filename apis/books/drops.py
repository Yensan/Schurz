#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import request, jsonify


def check_ContentType():
    """
    HowTo make Pre-Processing for all requests.
    But: it also can be managed in View Class, just like django-rest-framework
    """
    if request.method != 'GET':
        if (not request.content_type) or ('application/json' not in request.content_type):
            msg = jsonify(
                {"error": "content_type:'%s' not supported, please use 'application/json'." % request.content_type}
            )
            return msg, 400

def cross_domain(response):
    """ HowTO change all response's header """
    response.headers['Access-Control-Allow-Origin'] = '*'  # cross domain
    return response

def csrf_token():
    """ HowTO inject data into all templates(just as csrf_token) """
    token = '123' # must use isdangerous module generate a csrf token
    return {'csrf_token': token}
