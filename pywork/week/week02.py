'''
函数
def 函数名():
    代码段
组织好的，可重复使用的，用来实现独立功能的代码段。
可以提高程序的代码重用率。
只在调用的时候执行
函数必须先定义后调用
参数--argument：
定义的时候，称为形参，因为没有实际的值
调用的时候，称为实参，你给它什么值，它就是什么值
'''
# 函数调用的本质是函数名对应的内存地址
# def qiuhe3(a,b,c):
#     s=a+b+c
#     print(s)
# qiuhe3(1,2,3)
# print(qiuhe3)    # <function qiuhe3 at 0x0000000002062EA0>
# qiuhe=qiuhe3
# # 同
# print(id(qiuhe))
# print(id(qiuhe3))
# qiuhe(1,2,3)

'''
参数的定义方式：
1.位置参数
2.关键字参数
!!!关键字参数和位置参数同时使用时，调用时关键字参数必须是在位置参数后面的
3.默认参数
!!!默认参数只能放在后面
'''
# 关键字参数
# 无视参数顺序
# def cha(a,b):
#     print(a-b)
# cha(b=1,a=2)

# 关键字参数和位置参数同时使用时，关键字参数必须在位置参数后面定义
# def hs(a,b,c):
#     print(a,b,c)
# hs(2,3,c=7)

# 默认参数
# def dengji(name,age,sex='男'):
#     print(name,age,sex)
# dengji('张三',19)
# dengji('李四',20,'男')
# dengji('王五',21,'女')

'''
可变参数
'*'
1.'*'使参数变为了一个元组，所有传递的参数变为元组的元素
2.'*'具有打散序列的功能
'''
# def kb(*a):
#     print(a)
# x=(1,2,3)
# kb(*x)
# kb(x)

# 打散序列
# def func(a,b,c):
#     print(a,b,c)
# tup=(1,2,3)
# func(*tup)
# lst=[1,2,3]
# func(*lst)

'''
'**'
1.'**'使参数变成一个字典，所有传递的参数变为字典的键值对
!!!这里传参要求是键=值的形式
2.'**'有打散字典的功能，实参的key值必须与形参名相同，否则报错
3.'**kwargs'必须放在'*args'后面
'''
# def kb(**kwargs):
#     print(kwargs,type(kwargs))
# kb(name='张三',sge=18)
# kb()

# 打散字典
# 这里实参的key值，必须与与形参名相同，否则报错
# def kb(name,age):
#     print(name,age)
# a={'name':'张三','age':20}
# kb(**a)

# def kb(*a,**b):
#     print(a,b)
# a={'name':'张三','age':18}
# kb(1,2,3,**a)    # (1, 2, 3) {'name': '张三', 'age': 18}
# kb(1,2,3,*a)    # (1, 2, 3, 'name', 'age') {}

'''
!!!总结：
定义函数时，参数的位置：位置参数，元组参数，默认参数，字典参数
'''
# def kb(a,*b,c=9,**d):
#     print('a=',a)
#     print('b=',b)
#     print('c=',c)
#     print('d=',d)
# kb(1,2,3,4,5)
# kb(1,2,3,name='张三')
# kb(1,2,c=3,age=18)

'''
返回值
没有return的函数，均返回空值None
python中可以返回多个值--元组类型
return的两个作用：1.返回内容 2.结束此方法
'''
# a=[1,2,30]
# x=a.remove(30)
# print(x)
# print(a)

# 返回多个值
# def hs(a,b):
#     c=a+b
#     d=a-b
#     e=a*b
#     return c,d,e
# x=hs(1,2)
# print(x)
# c,d,e=hs(2,3)
# print(c,d,e)

'''
函数间的调用
'''
# def total(price,num):
#     return price*num
# def pd():
#     t=total(price,num)
#     if t>300:
#         return t*0.8
#     else:
#         return int(t)-int(t%10)
# price = float(input('请输入西红柿单价：'))
# num = float(input('请输入数量：'))
# print('最终价格为：',pd())

'''
递归三大件：
1.递归前进
2.递归后退--return值
3.递归边界
当递归边界成立时，递归后退，不成立时递归前进
'''
# 阶乘
# def jiecheng(n):
#     if n==1:
#         return 1
#     else:
#         return n*jiecheng(n-1)
# x=jiecheng(6)
# print(x)

# 斐波那契序列
# 递归
# def fib(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(6))
# for n in range(1,11):
#     print(fib(n))

# 循环
# def fib(n):
#     i=1
#     a,b=1,1
#     while i<=n:
#         print(a)
#         a,b=b,a+b
#         i+=1
# fib(10)

# def p_n(n):
#     print(n)
#     if n==1:
#         return
#     p_n(n-1)
#     print('--heihei')
# p_n(4)

# 折半查找
# 递归
# def binary(a,start,end,key):
#     if start>end:
#         return -1
#     middle=(start+end)//2
#     if key<a[middle]:
#         return binary(a,start,middle-1,key)
#     elif key>a[middle]:
#         return binary(a,middle+1,end,key)
#     else:
#         return middle
# a=[1,2,3,4,5,6,7,8,9,10]
# x=binary(a,0,9,5)
# if x!=-1:
#     print(x)
# else:
#     print('没有找到')

# 循环
# def binary(a,start,end,key):
#     while start<=end:
#         middle=(start+end)//2
#         if key<a[middle]:
#             end=middle-1
#         elif key>a[middle]:
#             start=middle+1
#         else:
#             return middle
#     return -1
# a=[1,2,3,4,5,6,7,8,9,10]
# x=binary(a,0,9,6)
# if x==-1:
#     print('没找到')
# else:
#     print(x)

# day 06------------------------------------------------------------------------
'''
不可变类型的参数：数字、字符串、元组
函数hs(a)内部修改a的值，只是修改了一个副本，不会对a本身造成影响
可变类型的参数：列表、字典、集合
fun(la)将la真正的传过去，修改后fun外部的la也会受影响
'''
# 不可变
# def hs(a):
#     a+=3
#     print('函数内部a=',a)
# x=10
# hs(x)
# print('函数外部x=',x)

# 可变
# def hs(a):
#     a.append(3)
#     print(a)
# x=[1,2]
# hs(x)
# print(x)

# def hs(a=[]):
#     a.append(10)
#     print(a)
# hs()
# b=[9]
# hs(b)
# hs()
# hs(b)
# hs([])
# hs([])

# !!!这不叫修改
# def hs(a):
#     a=[1,2]    # 重新赋值
#     print(a)
# b=[3,4]
# hs(b)
# print(b)

'''
全局 局部
'''
# def hs():
#     b=3
#     print(a)
#     print(b)
# a=6
# hs()
# print(b)    # 报错 name 'b' is not defined

# 局部变量与全局变量同名，函数内以局部变量为准
# def hs():
#     a=7
#     print(a)
# a=9
# hs()
# print(a)

# 全局变量和局部变量，不可共存
# 局部变量有，不去外面找
# def hs():
#     # print(a)    # 报错 local variable 'a' referenced before assignment
#     a=9
#     print(a)
# a=10
# hs()
# print(a)

# 原因同上
# def hs():
#     a+=3    # 报错 local variable 'a' referenced before assignment
#     print(a)
# a=10
# hs()

'''
global关键字可以将局部变量变成一个全局变量
nonlocal关键字可以修改外层（非全局）变量
'''
# global关键字
# def hs():
#     global a
#     a+=10
#     print('函数内部：%d' % a)
# a=20
# hs()
# print('函数外部：%d' % a)

# def hs():
#     global a
#     a=10
# hs()
# print(a)

# def hs():
#     global a
#     a=10
# print(a)    # 报错 name 'a' is not defined
# hs()
# print(a)

# nonlocal关键字
# a=9
# def out():
#     def inside():
#         nonlocal a    # no binding for nonlocal 'a' found
#         a=98
#         print(a)
#     inside()
# out()

# def out():
#     a=9
#     def inside():
#         nonlocal a
#         a=98
#         print('我是内部',a)
#     inside()
#     print('我是外部',a)
# out()

# a=9
# def out():
#     a=7
#     def inside():
#         nonlocal a
#         a=999
#         print(a)
#     inside()
#     print('-------------',a)
# out()
# print(a)

'''
函数嵌套 enclosing
原理同局部变量
'''
# def outside():
#     def inside():
#         print('我是内部')
#     inside()
#     print('我是外部')
# outside()

# def out():
#     a=9
#     def inside():
#         a=98
#         print('我是内部',a)
#     inside()
#     print('我是外部',a)
# out()

'''
全局变量是不可变数据类型，函数无法修改全局变量的值
全局变量是可变数据类型，函数可以修改全局变量的值
'''
# 此时外部的a，与内部的a没有任何关系
# a=10
# b=[]
# def x():
#     a=8
#     b.append(9)
#     print(a)
# x()
# print(a)
# print(b)

# 此时外部的b，与内部的b没有任何关系
# !!!这不是修改，是重新赋值
# b=[]
# def x():
#     b=[9]
#     print(b)
# x()
# print(b)

# 修改
# b=[]
# def x():
#     b.append(9)
# x()
# print(b)

'''
命名空间
locals()--访问局部命名空间
它记录了函数的变量，包括函数的参数和局部定义的变量
globals()--访问全局命名空间
它记录了模块的变量，包括函数、类、其他导入的模块
内置命名空间
命名空间加载顺序：
内置命名空间->全局命名空间->局部命名空间
!!! globals()和locals()返回值都是字典
'''
# a=3
# b=4
# def hs(x):
#     c=5
#     d=6
#     print(locals())
# print(globals())
# hs(6)

'''
变量作用域：
Local（函数内部）
Enclosing（嵌套函数的外层函数内部）
Global（模块全局）
Built-in（内建）
'''
'''
命名空间查找顺序
（1）先在local中搜索
（2）然后在父函数的命名空间enclosing中搜索
（3）接着在模块命名空间global中搜索
（4）最后在内置命名空间built-in搜索
'''
# a=3
# b=30
# c=300
# def out():
#     a=4
#     b=40
#     def inside():
#         a=5
#         print(a)#L  local 优先使用本地的
#         print(b)#E  enclosing 本地没有找嵌套作用域
#         print(c)#G  globle 本地嵌套都没有，找全局
#         print(__name__)#B built-in 全局也没有，找内置
#     inside()
# out()

'''
模块、类、函数会产生新的作用域，其他代码不会
比如条件判断、循环语句、异常捕捉等的变量是可以全局使用的
'''
# x=18
# if x<25:
#     b=20
# print(b)

'''
abs()--绝对值
max()--求最大值，key=函数名称--指定求最大值的规则
注意变量名不要叫max！否则调用max()会出错
'''
# a=[-1,-3,-2,-5,-4]
# b=max(a)
# print(b)

# a=[-1,-3,-2,-5,-4]
# b=max(a,key=abs)
# print(b)

# def hanshu(x):
#     print('---')
#     return abs(x)
# a=[-1,-3,-2,-5,-4]
# # 把函数名作为一个参数换地给了max()，max()内部执行了hanshu()
# b=max(a,key=hanshu)
# print(b)

# 字典与字典之间不能比较，但可以通过某个value进行比较
# lst=[{'name':'Tom','age':19},{'name':'jerry','age':29},{'name':'mary','age':39}]
# def getAge(x):
#     return x['age']
# b=max(lst,key=getAge)
# print(b)

# a=[-1,-3,-2,-5,-4]
# # 升序排序
# a.sort()
# print(a)
# # 按照绝对值，升序排序
# a.sort(key=abs)
# print(a)

'''
map()--映射  函数会依次作用在迭代内容的每一个元素上进行计算，然后返回一个新的可迭代对象
第一个参数--函数名（返回的是加工过的值）
第二个参数--序列
'''
# def hs(x):
#     return x*x
# a=[1,2,3]
# b=map(hs,a)
# print(b)    # <map object at 0x0000000002142860>
# # for x in b:
# #     print(x)
# b=list(b)
# print(b)

'''
filter()--过滤序列  过滤掉不符合条件的元素，返回由符合条件元素组成的可迭代对象
第一个参数--函数名（返回True或False）
第二个参数--序列
'''
# def gl(a):
#     if a%3==0 or a%7==0:
#         return True
#     else:
#         return False
# a=[1,2,3,4,5,6,7,8,9]
# b=filter(gl,a)
# print(b)
# print(list(b))

'''
zip()--接收任意多个可迭代对象作为参数
将对象中对应元素，打包成一个元组，然后返回一个可迭代的zip对象
若长度不同，以最短的为准
'''
# a=[1,2,3]
# b=['a','b','c','d']
# c=zip(a,b)
# print(c)
# for x in c:
#     print(x)

# a=[1,2,3]
# b=['a','b','c']
# def hs(x):
#     return {x[0]:x[1]}
# x=map(hs,zip(a,b))
# print(list(x))

'''
lambda--匿名函数
用来快捷定义一个小函数
不能包含循环、return，可以包含if...else...
表达式计算的结果直接返回
'''
# x=lambda a,b:a if a>b else b
# print(x(2,3))

# lst=[{'name':'Tom','age':19},{'name':'jerry','age':29},{'name':'mary','age':39}]
# getAge=lambda x:x['age']
# l=max(lst,key=getAge)
# print(l)

# hs=lambda x:True if x%2==0 else False
# a=[1,2,3,4,5,6,7,8,9,10]
# b=filter(hs,a)
# print(list(b))

# a=[1,2,3]
# b=['a','b','c']
# hs=lambda x:{x[0]:x[1]}
# x=map(hs,zip(a,b))
# print(list(x))

'''
凡是内部嵌套函数用了外部资源时形成了闭包
资源就不会被回收，在函数运行完之后还存储在内存中
'''
# def hs():
#     a=[]
#     for i in range(3):
#         b=lambda y:y*i
#         a.append(b)
#     return a
# z=hs()
# print(z)
# i=9
# print(z[0](2))
# print(z[1](2))
# print(z[2](2))

'''
加载函数时，没有调用，函数内的语句不会执行
但因为已经加载，所以默认参数已经赋值了
'''
# i=6
# def x1(x=i):
#     print(x)
# i=7
# def x2(x=i):
#     print(x)
# x1()
# x2()

# def hs():
#     a=[]
#     for i in range(3):
#         b=lambda y,i=i:y*i
#         a.append(b)
#     return a
# z=hs()
# print(z)
# i=9
# print(z[0](2))
# print(z[1](2))
# print(z[2](2))

# day07-------------------------------------------------------------------------
'''
字符串
以引号包围的，不可修改的有序序列
'''
# 逆序
# a='123abc'
# for i in range(-1,-len(a)-1,-1):
#     print(a[i],end='')
# print()
# i=-1
# while i>=-len(a):
#     print(a[i],end='')
#     i-=1
# print()
# print(a[::-1])

'''
字符串的切片：
从字符串复制出一份指定的内容，存储在另一个变量中
不会对原字符串有影响
前闭后开 步长默认为1
'''

# a,*b='123'
# print(a)
# print(b)    # 变为列表类型

'''
format格式化
'''
# a='我叫{}，年龄{}'.format('张三',29)
# print(a)

# 索引
# a='我叫{0}，姓名{0}  年龄{1}'.format('李四',29)
# print(a)

# 关键字
# print('我叫{name}，年龄{age}，姓名{name}'.format(name='张三',age=30))

'''
填充格式：
:[填充字符][对齐方式][宽度]
字符$--填充字符
对齐方式：
<--左对齐
^--居中对齐
>--右对齐
数字8--宽度
'''
# a='我叫{:$^7}'.format('赵六')
# print(a)
#
# a='我叫{:*<5}'.format('赵六')
# print(a)
#
# a='我叫{:' '>3}'.format('赵六')
# print(a)

'''
进制转换
'''
# a='二进制{:b}'.format(10)
# print(a,type(a))
# x=bin(10)
# print(x,type(x))
#
# a='八进制{:o}'.format(10)
# print(a,type(a))
# x=oct(10)
# print(x,type(x))
#
# a='十六进制{:x}'.format(10)
# print(a,type(a))
# x=hex(10)
# print(x,type(x))

# %
# name='张三'
# age=18
# height=1.75
# x='我叫%s，身高%.2f，年龄%d'%(name,height,age)
# print(x)
#
# x=0.25
# a='成材率%.0f%%'%(x)
# print(a)

'''
find()--从左往右找
rfind()--从右往左找
返回找到的，开头位置的索引
找不到时，返回-1
index()--功能与find()相同
rindex()--功能与rfind()相同
找不到报错
count()--寻找参数字符串存在的个数
'''

'''
partiton()--分隔
参数为一个字符串，以参数分隔长字符串
只能分割为三部分，包括自身，且以第一次出现的为准
返回值为一个元组
'''
# x='123ab456ab789'
# print(x.partition('ab'))    # ('123', 'ab', '456ab789')

'''
split()--分隔
参数为一个字符串，以参数分隔长字符串，不包括自身
若出现多次，可选用第二个参数maxsplit，设置分隔几次
返回值为一个列表
'''
# a='123a456a789a0'
# print(a.split('a'))    # ['123', '456', '789', '0']
#
# a='2019-07-24'
# print(a.split('-'))
#
# a='123ab456ab789ab000'
# print(a.split('ab',maxsplit=1))
# print(a.split('ab',maxsplit=2))
# print(a.split('ab',maxsplit=3))

'''
splitlines()--按照行分隔
返回值为列表
'''
# a='abc\n123\n45'
# print(a.splitlines())

'''
字符串的替换
replace()--从左到右替换指定的元素
可以选用第三个参数指定替换的个数，默认全部替换
原字符串不变
'''
# a='123abc456abc'
# b=a.replace('abc','xy')
# print(b)
# b=a.replace('abc','xy',1)
# print(b)
# print(a)

'''
translate()--按照对应关系来替代内容
maketrans()--用于创建字符映射的转换表
第一个参数是字符串，第二个参数也是字符串，表示转换的目标
两个字符串的长度必须相同（否则报错），为一一对应的关系
'''
# s='12345678901111'
# a='1234567'
# b='abcdefg'
# table=str.maketrans(a,b)
# c=s.translate(table)
# print(c)

'''
字符串的装饰
center()--居中，可以指定填充内容，默认空格
ljust()--在指定长度左齐，可以指定填充内容，默认空格
rjust()--在指定长度右齐，可以指定填充内容，默认空格
zfill()--将字符串填充到指定长度，不足用0从左开始补充
strip()--去除空格，也可指定去除内容，可选左右
'''
# a='123'
# b=a.center(7,'*')
# print(b)
# print(a)

# 填充
# a='123'
# b=a.ljust(10,'$')
# print(b)
# b=a.rjust(10,'$')
# print(b)

# a='123'
# print(a.zfill(10))

# a='     123     '
# print(a.lstrip(),end='$')    # 去左
# print()
# print(a.rstrip(),end='$')    # 去右
# print()
# print(a.strip(),end='$')    # 左右都去

# a='###123####'
# print(a.lstrip('#'))
# print(a.rstrip('#'))
# print(a.strip('#'))

'''
upper()--转换为大写
lower()--转换为小写
swapcase()--大小写互换
'''
# a='abcABC12'
# print(a.upper())
# print(a.lower())
# print(a.swapcase())

'''
title()--将字符串中每个单词的首字母大写，以非字母划分
'''
# a='what is your name?'
# print(a.title())

'''
capitalize()--只有字符串的首字母大写
'''
# a='what is your name?'
# print(a.capitalize())

'''
expandtabs()--将tab或\t转换为空格
空格数=8-字符数
'''
# a='234123\t45\t78'
# print(a.expandtabs())

# 判断是否完全由数字组成
# a='123d'
# b=a.isdigit()
# print(b)

# 判断是否完全由字母组成
# a='azAz_'
# print(a.isalpha())

# 判断是否完全由数字或字母组成
# a='123aZ'
# print(a.isalnum())

# 判断字符串中所有字母是否完全为小写
# a='ac123sd'
# print(a.islower())

# 判断字符串中所有字母是否完全为大写
# a='12JAKSa'
# print(a.isupper())

# 判断是否满足title格式
# a="What Is Your Name?"
# print(a.istitle())

# 判断是否完全由空格组成
# a='        '
# print(a.isspace())

# 判断字符串的开头字符，也可以截取判断
# 范围同样左闭右开
# a='aadsKJLA123'
# print(a.startswith('123'))
# print(a.startswith('123',8,11))

# 判断字符串的结尾字符，也可以截取判断
# a='aadsKJLA'
# print(a.endswith('L'))
# print(a.endswith('L',0,7))

'''
dir()--可以列出字符串对象中所有的方法的名称
help()--可查看某个方法的具体介绍
'''
# s='aa'
# print(dir(s))
# print(help(str.replace))

'''
\转义字符
'''
# a='tom\'s cat'
# print(a)
# b="tom's cat"
# print(b)
#
# a='E:\test\nex.txt'
# print(a)
# a='E:\\test\\nex.txt'
# print(a)

# 判断条件换行时可用\
# a=19
# b=20
# c=22
# d=33
# if a>33 and b>44 and c>55 and c<100 and d>200 and d<=300 \
#     and a<300:
#     print('判断成功')
# else:
#     print('判断失败')

'''
元字符串
加r，所有转义字符都不进行转义操作
'''
# a=r'E:\test\nex.txt'
# print(a)

'''
encode()--编码
decode()--解码
'''
# a='la我'
# b=a.encode()    # 编码 字符串转换为字节码
# print(b)
# c=b.decode()    # 解码 字节码转换为字符串
# print(c)

# day08-------------------------------------------------------------------------
'''
列表推导式
'''
# a=[1,2,3,4,5,6]
# def qiupf(x):
#     return x*x
# b=[qiupf(i) for i in a]
# print(b)

'''
字典推导式
'''
# a={'a':'b',1:2}
# b={v:k for k,v in a.items()}
# print(b)

# a={k:v for k,v in zip('abc','123')}
# print(a)

# a={'a':1,'A':3,'b':4,'B':9,'c':10,'d':99}
# x=['a','A','B','b','c']
# b={k.lower():a.get(k.lower(),0)+a.get(k.upper(),0) for k in a.keys() if k in x}
# print(b)

'''
集合推导式
'''
# a=[1,2,3,4,1,2,3,4]
# b={i*i for i in a}
# print(b)

'''
模块
一个包括了python代码的文件就是一个模块
作用：
1.方便维护与管理
2.增加代码的重用率
模块只有被第一次导入的时候执行，多次导入没有用

模块导入：
1.模块导入会将导入的文件执行一遍
2.导入的名称就是我们定义的脚本或包的名称
3.导入的过程：
在指定范围内搜索指定名称的python脚本或者包，将其运行，获取其中的方法
'''

'''
模块导入的方式：
1.import 模块名
2.import 模块名 as 别名
3.import 模块名1，模块名2，...--一行导入多个模块
4.from...import...--局部导入
5.from...import...as 别名
6.from...import 功能1，功能2,...
7.from...import *--导入所有
!!! from...import *不能导入_开头的变量
'''

# 就近原则
# x=9
# print(x)    # 9
# from demo04 import *
# print(x)    # 100

# from demo04 import *
# x=9
# print(x)    # 9

'''
用from model import *时
在model中加入__all__=[变量1，变量2,...]只能导入__all__列表中的名字
_开头的名字也可以用from model import *导入
'''

'''
包的导入：
关于包的导入语句也分为import和from...import...两种
!!!凡是在导入时带点的，点左边都必须是一个包，否则非法
导入后就没有这种限制了
'''

'''
不同包的导入
搜索顺序：
1.当前目录
2.搜索在shell变量pythonPATH下的每个目录，由sys模块的sys.path方法来规定
'''

'''
通过模块的全局变量__name__查看模块名
当做脚本运行：
__name__=__main__
当做模块导入：
__name__的值等于模块名
'''

'''
random模块
random()--产生大于0且小于1之间的小数
uniform(a,b)--产生指定范围内的随机小数
randint(a,b)--产生范围内的随机整数，包含头和尾
randrange(s,e,[step])--产生范围内的随机整数，左闭右开
choice(lst)--参数为列表，随机返回序列中的一个数据
shuffle()--打乱列表顺序，直接修改原列表
'''
import random
# print(random.random())
# print(random.uniform(2,3))

# a=[random.randint(1,10) for i in range(10)]
# print(a)

# a=random.randrange(1,13,2)
# print(a)
# a=[random.randrange(1,10,3) for i in range(10)]
# print(a)

# a=[10,20,30,40]
# b=random.choice(a)
# print(b)

# a=[10,20,30,40]
# random.shuffle(a)
# print(a)

'''
生成随机验证码
'''
# import random
# def verify_code():
#     code=''
#     for i in range(4):
#         sz=random.randint(0,9)
#         xzm=chr(random.randint(97,122))
#         dzm=chr(random.randint(65,90))
#         c=random.choice([sz,xzm,dzm])
#         code=code+str(c)
#     return code
# print(verify_code())

'''
sys.version--返回解释器的版本号
sys.path--返回模块的搜索路径
sys.argv--接收命令行下的参数
'''
import sys
# print(sys.version)    # 版本

# argv--接受命令行下的参数
# ret=sys.argv
# path=sys.argv[0]
# name=sys.argv[1]
# pwd=sys.argv[2]
# if name=='zs' and pwd=='123':
#     print('登录成功')
# else:
#     print('失败')

# 时间字符串格式化
# import time
# s=time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())
# print(s,type(s))
# # 时间元组转换为字符串
# s=time.strftime('%Y/%m/%d %H-%M-%S',time.localtime())
# print(s,type(s))
# # 字符串转换为时间元组 UTC时间 比北京时间少8小时
# t=time.strptime(s,'%Y/%m/%d %H-%M-%S')
# print(t)
# t=time.localtime(time.time())
# print(t)
# # 时间元组转换为时间戳
# x=time.mktime(t)
# print(x)

'''
锁卡7天倒计时
'''
# import time
# a='2019-07-24 17:04:00'
# at=time.strptime(a,'%Y-%m-%d %H:%M:%S')
# ac=time.mktime(at)
# while True:
#     bc=time.mktime(time.localtime())
#     cc=bc-ac
#     d=7*24*3600-cc
#     days=int(d//(24*3600))
#     hours=int(d%(24*3600)//3600)
#     minutes=int(d%(3600)//60)
#     seconds=int(d%60)
#     print('\r','您还有{}天{}小时{}分钟{}秒解冻'.format(days,hours,minutes,seconds),end='')
#     time.sleep(1)

'''
self--对象本身
哪个对象调用方法或属性，self就是这个对象（id相同）

__init__()在创建对象的时候自动执行
在__init__()中做初始化操作
'''

'''
在类的外部增加属性（不推荐使用）
'''
# class Teacher():
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(self.name,self.age)
# zs=Teacher('张三')
# zs.age=29
# zs.show()
#
# ls=Teacher('李四')
# ls.show()    # 报错

# class Student():
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def show(self):
#         print(self.name,self.age,self.sex)
#     def setAge(self):
#         self.age=19
# zs=Student('张三',29,'男')
# zs.show()
# zs.setAge()
# zs.show()

'''
__str__()函数--打印对象名称时默认调用__str__()方法，默认返回的是对象的内存地址
可重写__str__()打印对象保存的信息
'''
# from math import pi
# class Circle():
#     def __init__(self,radis):
#         self.radis=radis
#     def area(self):
#         return pi*self.radis*self.radis
#     def c(self):
#         return 2*pi*self.radis
#     def __str__(self):
#         return '我的半径是%d,周长为%.2f,面积为%.2f'%(self.radis,self.area(),self.c())
# a=Circle(5)
# print(a)

'''
添加家具
'''
# class House():
#     def __init__(self,info,area,address):
#         self.info=info
#         self.area=area
#         self.address=address
#         self.furnitures=[]
#     def addFurniture(self,obj):
#         self.area-=obj.area
#         self.furnitures.append(obj.name)
#     def __str__(self):
#         s1='户型{}，面积{}，地址{}，'.format(self.info,self.area,self.address)
#         s2='室内家具有：'
#         for f in self.furnitures:
#             s2+=f+' '
#         return s1+s2
# class Furniture():
#     def __init__(self,name,area):
#         self.name=name
#         self.area=area
# h1=House('三室一厅',138,'北京大兴')
# bed=Furniture('床',6)
# h1.addFurniture(bed)
# print(h1)
# table=Furniture('桌子',3)
# h1.addFurniture(table)
# print(h1)
# sofa=Furniture('沙发',10)
# h1.addFurniture(sofa)
# print(h1)

'''
类属性和实例属性
不可修改类型
'''
# class People():
#     tax=0.01
#     def __init__(self,salary):
#         self.salary=salary
#     def pay(self):
#         return self.salary*People.tax
# a=People(10000)
# b=People(20000)
#
# # 只要有=，就是一个新开辟的变量了，与类变量无关了
# # a.tax=a.tax+1 混合使用，前面的tax是对象属性，后边的那个是类属性
# a.tax+=0.01
# print(a.tax,id(a.tax))
# print(People.tax,id(People.tax))
#
# # 类变量变了，他也不变
# People.tax=200
# print(a.tax)    # 0.02
#
# # 删除a的属性，就使用类的
# delattr(a,'tax')
# print(a.tax)    # 200

'''
可修改类型
'''
# class A():
#     books=['三国','西游记']
#     def __init__(self,name):
#         self.name=name
# x=A('张三')
# y=A('李四')
# x.books[0]='水浒传'
# print(x.books)
# print(y.books)
# print(A.books)
#
# x.books=['红楼梦','大秦帝国']
# print(x.books)
# print(y.books)
# print(A.books)