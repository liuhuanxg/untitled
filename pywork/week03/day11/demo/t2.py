'''
反射导入模块中的属性、函数、类
'''
import t1

x=getattr(t1,'d')
print(x)

f=getattr(t1,'func')
f('张三')

cls=getattr(t1,'A')
a=cls('张三')
print(a.name)