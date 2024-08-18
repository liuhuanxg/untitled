# -*-coding:utf-8 -*-
"""
@project:untitled
@File: 面试题.py
@Time: 2020/6/5 23:09
@user：liuhuan   
"""
d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
d1 = {x[0]: x[1] for x in sorted(d.items(), key=lambda x: x[1])}
print(d1)
