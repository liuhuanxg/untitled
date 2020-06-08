#-*-coding:utf-8 -*-
"""
@project:untitled
@File: fib.py
@Time: 2020/5/29 20:39
@user：liuhuan   
"""
def fib(n):
    if n==0:
        print("111")
        return 1
    if n==1:
        print("2222")
        return 1
    return fib(n-1)+fib(n-2)

fib(6)