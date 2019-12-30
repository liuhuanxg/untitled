'''
反射自己模块中的属性和函数
'''
import sys

zhutou=299
def func():
    print('aaaaaaaaaaaaaaaaa')

# 查看所有模块
print(sys.modules)

# 反射当前模块
print(sys.modules['__main__'])

# 反射当前模块中的zhutou变量
x=getattr(sys.modules['__main__'],'zhutou')
print(x)
x=getattr(sys.modules['__main__'],'func')
x()

'''
反射内置模块
'''
import time
print(time.time())
t=getattr(time,'time')
print(t())