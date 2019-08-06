#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import os

class FileMange(ABC):
    def __init__(self, path):
        self.path = path
    @abstractmethod
    def read(self):
        """ read file from some file system. """
        pass

    @abstractmethod
    def write(self):
        """ write data in some file system. """
        pass



def recurs_find(baseDIR, substr):
    result = []
    listdir = [os.path.join(baseDIR, i) for i in os.listdir(baseDIR)]
    for item in listdir:
        if substr in item and os.path.isfile(item):
            result.append(item)
        elif os.path.isdir(item):
            result.extend(recurs_find(item, substr))
    return result




