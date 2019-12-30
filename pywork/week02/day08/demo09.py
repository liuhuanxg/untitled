'''
用from model import *时
在model中加入__all__=[变量1，变量2,...]只能导入__all__列表中的名字
_开头的名字也可以用from model import *导入
'''
__all__=['hs1','hs2','_hs3']
def hs1(a,b):
    return a+b
def hs2(a,b):
    return a*b
def _hs3(a,b):
    return a-b