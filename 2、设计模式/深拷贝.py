#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 深拷贝.py
"""
from collections import OrderedDict
class A():

    def __init__(self):
        self.age = 30
        self.__name = 20

a = A()
a.length = 10
print(OrderedDict(sorted(a.__dict__.items())))
