#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 6、修饰器模式.py
@Time: 2020/5/16 11:36
@user：liuhuan   
"""

"""
修饰器虽然名为修饰器，但并不意味着它应该只用于让产品看起来更加漂亮。
修饰器模式通常用于扩展一个对象的功能。这类扩展的实际例子有：给枪加一个消音器、使用不同的照相机镜头
"""
from functools import wraps

def memoize(fn):
    known = dict()
    @wraps(fn)
    def memeoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]
    return memeoizer

@memoize
def nsum(n):
    """返回前n个数字的和"""
    assert (n>=0)
    return 0 if n==0 else n+nsum(n-1)

@memoize
def fibonacci(n):
    """返回斐波那契数列的第n个数"""
    assert (n>=0)
    return n if n==0 or n==1 else fibonacci(n-1)+fibonacci(n-2)

if __name__ == "__main__":
    from timeit import Timer
    measure = [
        {'exec':'fibonacci(100)', 'import':'fibonacci', 'func':fibonacci},
        {'exec':'nsum(200)', 'import':'nsum', 'func':nsum}
    ]
    for m in measure:
        t = Timer("{}".format(m["exec"]),"from __main__ import {}".format(m["import"]))
        print("name:{},doc:{},executing:{},time:{}".format(m["func"].__name__,m["func"].__doc__,m["exec"],t.timeit()))