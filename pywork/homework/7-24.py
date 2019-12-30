# Python0715 吕佳

'''
字符串
以引号包围的，不可修改的有序序列
'''
# a='123abc'
# print(a[0])
# print(a[3])
# i=0
# while i<len(a):
#     print(a[i])
#     i+=1

# a='123abc'
# for i in range(len(a)):
#     print(a[i])

# a='123ab'
# for i in range(-1,-len(a)-1,-1):
#     print(a[i])

# a='123abc'
# i=-1
# while i>=-len(a):
#     print(a[i])
#     i-=1

'''
切片：
从字符串复制出一份指定的内容，存储在另一个变量中
不会对原字符串有影响
前闭后开，步长默认为1
'''
# a='123abc'
# print(a[0:5])
# print(a[0:5:2])

# a='123abcd'
# print(a[0:])
# print(a[3:])
# print(a[:5])
# print(a[:])
# print(a[::3])

# a='123abc'
# #输出ad
# print(a[3::3])
# print(a[::3][1:])

# a='123abc'
# #输出la
# print(a[0:4:3])
#
# print(a[0:5:-1])    # 无结果
# print(a[::-1])    # 逆向输出
# print(a[-1:-5:-2])

# a='123456789'
# print(a[-8:5])
# print(a[0:7])
# print(a[-7:0])    # 无结果
# print(a[-7:0:-1])
# print(a[-1:-5])    # 无结果
# print(a[-1:-5:-1])

'''
拼接、重复
'''
# a='我爱你'
# b='北京'
# print(a+b)
# print('你好'*3)

'''
赋值
可变赋值*b，b的类型为列表类型
'''
# a,b,c='123'
# print(a)
# print(b)
# print(c)

# a,*b='123'
# print(a)
# print(b)

'''
格式化输出
'''
# a='我叫{}，年龄{}'.format('张三',29)
# print(a)

# 索引
# a='我叫{0}姓名{0} 年龄{1}姓名{1}'.format('李四',29)
# print(a)

# 关键字
# print('我叫{name}，年龄{age}，姓名{name}'.format(name='张三',age=19))

'''
填充
格式：
:[填充字符][对齐方式][宽度]
字符$--填充字符
对齐方式：
<--左对齐
^--居中对齐
>--右对齐
数字8--宽度
'''
# a='我叫{:$^8}'.format('赵六')
# print(a)
#
# a='我叫{:*<5}'.format('赵四')
# print(a)
#
# a='我叫{:' '>6}'.format('赵四')
# print(a)

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

# name='张三'
# age=18
# height=1.75
# x='我叫%s，身高%.2f，年龄%d'%(name,height,age)
# print(x)
#
# x=0.25
# a='成材率%.0f%%'%x
# print(a)

'''
find()--从左往右找
rfind()--从右往左找
返回找到的，开头位置的索引
找不到时，返回-1
'''
# a='abcdef'
# b='cd'
# x=a.find(b)
# print(x)
# print(a.find('zz'))

# a='abcdefcdg'
# b='cd'
# print(a.rfind(b))

'''
index()--功能与find()相同
rindex()--功能与rfind()相同
找不到报错
count()--寻找参数字符串存在的个数
'''
# a='abcdefcdg'
# b='cd'
# print(a.index(b))
# # print(a.index('cda'))    # 报错

# a='1bcdefcdg'
# b='cd'
# print(a.rindex(b))
# b='cda'
# # print(a.rindex(b))    # 报错

# a='1bcdefcdgcd'
# b='cd'
# print(a.count(b))

'''
开发find()函数
'''
# a=input('请输入一个长字符串：')
# b=input('请输入想要查询的子字符串：')
# def find(b):
#     for i in range(len(a)-len(b)+1):
#         for j in range(len(b)):
#             if a[i+j]!=b[j]:
#                 break
#         else:
#             return i
#     else:
#         return -1
# print(find(b))

'''
partiton()--分隔
参数为一个字符串，以参数分隔长字符串
只能分割为三部分，包括自身，且以第一次出现的为准
返回值为一个元组
'''
# x='123ab456ab789'
# print(x.partition('ab'))

'''
split()--分隔
参数为一个字符串，以参数分隔长字符串，不包括自身
若出现多次，可选用第二个参数maxsplit，设置分隔几次
返回值为一个列表
'''
# a='123a456a789a0'
# print(a.split('a'))
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
# a='abc\n123\n5'
# print(a.splitlines())

'''
用split()实现splitlines()
'''
# a='abc\n12\n45'
# print(a.split('\n'))

# a='abc\n456\n45'
# i=0
# while i<len(a):
#     if a[i]=='\n':
#         print()
#     else:
#         print(a[i],end='')
#     i+=1

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
第一个参数是字符串，第二个参数也是字符串表示转换的目标
两个字符串的长度必须相同，为一一对应的关系
'''
# s='12345678901111'
# # a,b长度必须相同
# a='1234567'
# b='abcdefg'
# table=str.maketrans(a,b)
# b=s.translate(table)
# print(b)


'''
字符串的装饰
center()--居中，可以指定填充内容，默认空格
ljust()--在指定长度左齐，可以指定填充内容，默认空格
rjust()--在指定长度右齐，可以指定填充内容，默认空格
zfill()--将字符串填充到指定长度，不足用0从左开始补充
strip()--去除空格，也可指定去除内容，可选左右
'''
# a='123'
# print(a.center(7,'*'))
# print(a)

# a='123'
# b=a.ljust(10,'$')
# print(b)
# b=a.rjust(10,'$')
# print(b)

# a='123'
# print(a.zfill(10))

# a='     123      '
# print(a.lstrip(),end='$')
# print()
# print(a.rstrip(),end='$')
# print()
# print(a.strip(),end='$')

# a='####123####'
# print(a.lstrip('#'))
# print(a.rstrip('#'))
# print(a.strip('#'))

# a='abcABD'
# print(a.upper())
# print(a.lower())
# print(a.swapcase())

'''
title()--将字符串中每个单词的首字母大写，以非字母划分
'''
# a='what is your name？'
# print(a.title())

'''
capitalize()--只有字符串的首字母大写
'''
# a='what is your name?'
# print(a.capitalize())

'''
expendtabs()--将tab或\t转换为空格
空格数=8-字符数
'''
# a='234321\t45\t78'
# print(a.expandtabs())

# 判断是否完全由数字组成
# a='123d'
# print(a.isdigit())
#
# a='al;k'
# print(a.isalpha())
#
# a='123az'
# print(a.isalnum())

# a='adklKJ'
# print(a.islower())
#
# a='123LKAS;L'
# print(a.isupper())

# a='What is your name？'
# print(a.istitle())
#
# a='              '
# print(a.isspace())

# a='aadsKJLA123'
# print(a.startswith('123'))
# print(a.startswith('123',8,11))
#
# a='aadsKJLA'
# print(a.startswith('L'))
# print(a.startswith('L',0,8))

'''
dir()--可以列出字符串对象中所有的方法的名称
help()--可查看某个方法的具体介绍
'''
# s='aa'
# print(dir(s))
# print(dir(str))
#
# print(help(s.replace))

# a='tom\'s cat'
# print(a)
# b="tom's cat"
# print(b)

# a='E:\test\net.txt'
# print(a)
# a='E:\\test\\net.txt'
# print(a)

# a=19
# b=20
# c=22
# d=33
# if a>33 and \
#     b<40:
#     print('判断成功')
# else:
#     print('判断失败')

# print('\c')
# print('\n')
# print('\t')
# print('\\')
# print('\'')
# print("\"")

'''
元字符串
加r，所有转义字符都不进行转义操作
'''
# a=r'E:\test\nex.txt'
# print(a)

# a='la我'
# b=a.encode()
# print(b)
# c=b.decode()
# print(c)
# ------------------------------------------------------------------------------
# 测试 字符串切片
# 1.判断一个数是否是回文数。例如：输入：121，输出也是121，像这样的数就是回文数
# num=input('请输入一个数：')
# if num==num[::-1]:
#     print(num,'是回文数')
# else:
#     print(num,'不是回文数')

# 测试 字符串方法
# 2.查找字符串中每个字符最后出现的位置。
text = """
东边来了个喇嘛，西边来了个哑巴，喇嘛手里拎着五斤挞嘛，哑巴腰里别着个喇叭，
别着喇叭的要用喇叭换手里拎着挞嘛的哑巴的挞嘛，
拎着挞嘛的哑巴不愿意用挞嘛换手里拎着喇叭的喇嘛的喇叭。
拎着喇叭的喇嘛用喇叭打了拎着挞嘛的哑巴，
拎着挞嘛的哑巴也用挞嘛打了拎着喇叭的喇嘛。
"""
# for index,char in enumerate(text):
#     if index==text.rindex(char):
#         print(index,':',char)

# 3.‘2018-11-12’去掉‘-’输出
# a='2018-11-12'
# print(a.replace('-',''))

# 4.统计数字，字母，下划线个数
# s='12321KAJDLks___'
# a=0
# b=0
# c=0
# for i in s:
#     if i.isdigit():
#         a+=1
#     elif i.isalpha():
#         b+=1
#     elif i=='_':
#         c+=1
# print('数字：',a,'；字母：',b,'；下划线：',c)

# 5.编写一个函数，接收传入的字符串，统计大写字母的个数、小写字母的个数、数字的个数、
# 其它字符的个数，并以元组的方式返回这些数，然后调用该函数。

def data(s):
    lst=[]
    upper=0
    lower=0
    num=0
    other=0
    for i in s:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        elif i.isdigit():
            num+=1
        else:
            other+=1
    lst.append(upper)
    lst.append(lower)
    lst.append(num)
    lst.append(other)
    return tuple(lst)
s=input('请输入一个字符串：')
print(data(s))