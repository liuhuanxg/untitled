#-*-coding:utf-8 -*-
"""
@project:untitled
@File: demo1-单例模式.py
@Time: 2020/3/16 10:41
@user：python-刘欢    
"""

class Single():
    _instance = None

    def __new__(cls,*args,**kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Single()
s2 = Single()
print(id(s1),id(s2))


def quick_sort(lst):

    if len(lst)<=2:
        return lst

    number = lst[0]
    left = [i for i in lst[1:] if i<number]
    right = [j for j in lst[1:] if j>=number]

    return quick_sort(left)+[number]+quick_sort(right)

lst = [6,10,7,11,9]
print(quick_sort(lst))
