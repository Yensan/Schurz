#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import path
import logging
from logging.handlers import RotatingFileHandler

from colorlog import ColoredFormatter


#  logging config: console log for DEBUG
console_handler = logging.StreamHandler()
console_handler.setFormatter(
    ColoredFormatter(
        fmt="%(log_color)s%(asctime)s %(levelname)-8s %(filename)s:%(lineno)d %(white)s %(message)s%(reset)s",
        log_colors={
            'DEBUG': 'white',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        },
        datefmt=None, reset=True, style='%',
    )
)
console_handler.setLevel(logging.INFO)


#  logging config: RotatingFileHandler for deployment
file_handler = RotatingFileHandler(
    filename=path.join(path.dirname(path.dirname(path.dirname(__file__))),
                       'flask.log'),
    maxBytes=100 * 1024 * 1024,  # if file size is bigger than it, will touch a new file
    backupCount=10  # backup files is 10
)
file_handler.setFormatter(
    logging.Formatter(
        fmt='%(asctime)s %(pathname)s %(levelname)s '
            '[P%(process)d T%(thread)d L%(lineno)s] %(message)s',
        datefmt='%Y%m%d %H:%M:%S'
    )
)
file_handler.setLevel(logging.DEBUG)


logger = logging.getLogger()
logger.propagate = False
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
