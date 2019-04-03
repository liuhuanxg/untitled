#1、  select * from a inner join b
'''
import re
a='abbbccc'
print(re.sub(r'b+','b',a))
'''

# py2和py3的区别
'''
1、
py2：源码重复量多，臃肿，源码语法不清晰，掺杂着c，php，java的一些陋习，
py3：ss，规范，清晰，优美

2、
py2:默认不能识别中文。需要加#--encoding:utf-8--
py3:默认的编码方式就是utf-8

3、
py2：用户输入用：raw_input
py3:用户交互用：input

4、unicode
py2:编译安装时可以通过参数–enable-unicode=ucs2或4分别指定2、4字节的表示一个unicode字符。 
py3:默认使用ucs4

5、
py2：int有限定长度，超过限定长度自动变成long型
py3：只有int没有long

6、range
py2、常用xrange实现range功能
py3、没有xrange只有range。

'''

#redis里面list内容的长度
#len key_name

def func(func3):
    def inner():
        func3()
    return inner
def func2():
    print('测试1')
c=func(func2)
c()

def deco(func1):
    def inner():
        func1()
        print('测试2')
    return inner
def cc():
    print('测试1')
deco(cc)
