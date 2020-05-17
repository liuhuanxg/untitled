#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 1、单例模式.py
"""
"""
单例模式(Singleton Pattern)是一个常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在，当希望在某个系统中只出现一个实例时，单例对象就能派上用场
"""

class Singleton():
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not  cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(id(s1),id(s2))