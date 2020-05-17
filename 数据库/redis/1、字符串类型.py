#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 1、字符串类型.py
@Time: 2020/5/8 13:13
@user：liuhuan   
"""

# import redis
#
# conn = redis.Redis(host="127.0.0.1",port="6379",db=0)
#
# result = conn.set("首富","马云")
# result1 = conn.setex("总统",20,"特朗普")
#
# print(result)
# print(result1)

list1 = [1, 2, 3, 4]
list2 = list1[:]
print(list2 is list1)
print(id(list1))
print(id(list1[:]))