"""
__foo__ 和_foo  和__foo有什么区别
"""

class Test(object):
    def __foo__(self,_foo):
        self._foo=_foo
        pass

"""
__foo__:定义的是特殊方法，一般是系统定义的名字，类似__init__()之类的

_foo:以单下划线开头的表示的是protected类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于from module import *

__foo:双下划线的表示的是私有类型的变量，只能用于该类进行访问

"""