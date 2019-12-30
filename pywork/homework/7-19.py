# Python 0715 吕佳

#逻辑运算符：and/or/not
# stu=True
# if not stu:
#     print('你不是学生')
# else:
#     print('是学生，请进校')

'''
短路逻辑
 x or y
 若x不成立，返回y的值
 若x成立，返回True
'''
# a=5
# b=a>7 or 4
# print(b)
#
# a=5
# b=a>3 or 7
# print(b)

'''
短路逻辑
x and y
若x成立，返回y的值
若x不成立，返回False
'''
# a=6
# b=a>7 and 5
# print(b)

'''
三元表达式
满足if条件，值为前面的值
不满足则为后面的值
'''
# b=9
# a=7 if b>10 else 8
# print(a)

'''
while/for...else...
else只在循环正常结束后执行
'''
# i=1
# while i<5:
#     if i==4:
#         break
#     print(i)
#     i+=1
# else:
#     print('好像不成立了')

#质数
# n=int(input('请输入一个数：'))
# i=2
# while i<n:
#     if n%i==0:
#         print(n,'不是质数')
#         break
#     i+=1
# else:
#     print(n,'是质数')

# n=int(input('请输入一个数：'))
# for i in range(2,n):
#     if n%i==0:
#         print(n,'不是质数')
#         break
# else:
#     print(n,'是质数')

#2--100间所有指数放入列表
# s=[]
# for n in range(2,101):
#     for i in range(2,n):
#         if n%i==0:
#             break
#     else:
#         s.append(n)
# print(s)

# a=[]
# i=2
# while i<100:
#     j=2
#     while j<i:
#         if i%j==0:
#             break
#         j+=1
#     else:
#         a.append(i)
#     i+=1
# print(a)

'''
循环嵌套
'''
#矩形
# j=1
# while j<=5:
#     i=1
#     while i<=5:
#         print('*',end='')
#         i+=1
#     print()
#     j+=1

# for i in range(1,6):
#     for j in range(1,6):
#         print('*',end='')
#     print()

# 正三角
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print('*',end='')
#         j+=1
#     print()
#     i+=1

# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()

# 倒三角
# i=1
# while i<6:
#     j=1
#     while j<i:
#         print(' ',end='')
#         j+=1
#     j=1
#     while j<=6-i:
#         print('*',end='')
#         j+=1
#     print()
#     i+=1

# for i in range(1,6):
#     for j in range(1,6-i+1):
#         print('*',end='')
#     print()

# 99乘法表
# j=1
# while j<=9:
#     i=1
#     while i<=j:
#         print(i,'*',j,'=',i*j,end='\t')
#         i+=1
#     print()
#     j+=1

# for j in range(1,10):
#     for i in range(1,j+1):
#         print(i,'*',j,'=',i*j,end='\t')
#     print()

# 空心矩阵
# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or i==5 or j==1 or j==5:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()

# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         if i==1 or i==5 or j==1 or j==5:
#             print('*',end='')
#         else:
#             print(' ',end='')
#         j+=1
#     print()
#     i+=1

# 字典--键值对
# 无序，可修改
'''
字典的key必须是不可修改的类型
'''

# 添加
'''
不存在，添加
存在，覆盖
'''
# a={'name':'张三','age':19,'sex':'男'}
# print(a)
# print(a['name'])
# a['score']=99
# print(a)
# a['age']=18
# print(a)

'''
setdefault()函数
存在，不操作
不存在，添加
'''
# a={'name':'张三','age':19,'sex':'男'}
# a.setdefault('age',20)
# print(a)
# a.setdefault('score',90)
# print(a)

# 删除
'''
pop()--弹出指定键对应的值
不同于列表中的pop()，必须有参数
返回值为一个value
'''
# a={'name':'张三','age':19,'sex':'男'}
# b=a.pop('name')
# print(b)
# print(a)

'''
popitem()函数--随机弹出一个键值元组，随机是因为字典是无序的
返回值为一个键值对元组
'''
# a={'name':'张三','age':19,'sex':'男'}
# b=a.popitem()
# print(b)
# print(a)

'''
clear()函数--清空
'''
# a={'name':'张三','age':19,'sex':'男'}
# a.clear()
# print(a)

'''
del--可删除字典中的一个键值对，也可删除整个字典
'''
# a={'name':'张三','age':19,'sex':'男'}
# del a['name']
# print(a)
# del a
# print(a)    # 报错，a不存在

'''
update()函数--以字典的形式更新指定字典的内容
如果键不存在，创建
如果存在，覆盖
'''
# a={'name':'张三','age':19,'sex':'男'}
# b={'name':'李四','score':89}
# a.update(b)
# print(a)

'''
get()--以键取值
若指定键不存在，默认返回None，返回值可指定
'''
# info={'name':'张三','age':10,'sex':'男'}
# name=info.get('name')
# print(name)
# a=info.get('aaa')
# print(a)
# a=info.get('aaa','不存在')
# print(a)

'''
in a/not in a--判断指定的键是否在字典中，与值无关
in a功能与in a.keys()相同，但不可完全划等号
要判断值是否存在可用in a.values()
'''
# a={'name':'张三','age':19,'sex':'男'}
# if 'name' in a:
#     print('name存在')
# if 'score' not in a:
#     print('score不存在')
# if '张三' in a:    # 不成立
#     print('张三在')

'''
字典-->内含元组的列表
内含元组的列表-->字典
'''
# a={'name':'张三','age':19,'sex':'男'}
# b=[]
# c={}
# for k,v in a.items():
#     b.append((k,v))
# print(b)
# for x in b:
#     y,z=x
#     c[y]=z
# print(c)

'''
键重复时，后面的会覆盖前面的--以后面的为准
'''
# a={'name':'张三','age':19,'sex':'男','age':90}
# print(a)

'''
以num:001,name=张三,age:18,sex:男格式打印
'''
a={
    '001':{'name':'张三','age':18,'sex':'男'},
    '002':{'name':'李四','age':28,'sex':'男'},
    '003':{'name':'王五','age':38,'sex':'女'},
    '004':{'name':'赵六','age':48,'sex':'男'}
}
# for x,y in a.items():
#     print('num:%s'%x,end=' ')
#     for k,v in y.items():
#         print('%s:%s'%(k,v),end='')
#     print()

# for k1 in a.keys():
#     print('num:%s'%k1,end=' ')
#     for k2 in a[k1].keys():
#         print('%s:%s'%(k2,a[k1][k2]),end=' ')
#     print()

# 给所有性别为男的添加1000元工资
# for k,v in a.items():
#     if v['sex']=='男':
#         v['salary']=1000
#     print(k,':',v)

# 集合
# 无序，唯一，不可改变

# 值唯一
# a={1,2,3,3,3,3,3}
# print(a)    # 自动去重

# 无序
# a={1,2,3,3,3,3,3}
# print(a[1])    # 报错，不支持索引

'''
定义空集合只能用set()
'''
# b={}
# print(type(b))
# b=set()
# print(type(b))

'''
add()--添加，重复时不进行任何操作
'''
# a={1,2,3,3,3,3,3}
# print(a)
# a.add(9)
# print(a)
# a.add(9)
# print(a)

'''
set()
'''
# a=[1,2,3]
# b=set(a)
# print(b)
# a='1234'
# b=set(a)
# print(b)    # 无序

# b={'name':'张三','age':19}
# a=set(b)
# print(a)    # {'age','name'},只有键没有值

'''
update()--添加，不重
'''
# a={1,2,3,4}
# a.update([1,2,5,6])
# print(a)

# 删除
'''
pop()--随机弹出一个
'''
# a={1,2,3,4}
# b=a.pop()
# print(b)
# print(a)

'''
remove()--移除指定值
'''
# a={10,20,30,40}
# a.remove(20)
# print(a)

'''
clear()--清空
'''
# a={10,20,30,40}
# a.clear()
# print(a)

'''
del--删除整个集合
'''
# a={1,2,3,4}
# del a
# print(a)   # 报错，a不存在

# 求出a中每个元素的个数
# a=[1,2,3,1,2,3,1,1,3,3,3,3]
# b=set()
# for i in set(a):
#     b.add(i)
# for n in b:
#     print(n,'出现的次数为：',a.count(n))

# 集合数学运算
'''
交集
&或intersection()--取公共部分
'''
# a={1,2,3,4}
# b={3,4,5,6}
# c=a.intersection(b)
# print(c)
# d=a&b
# print(d)

'''
差集
-或different
'''
# a={1,2,3,4}
# b={3,4,5,6}
# c=a-b
# print(c)
# c=b-a
# print(c)

'''
反交集
^或symmetric_difference()
'''
# a={1,2,3,4}
# b={3,4,5,6}
# c=a^b
# print(c)
# c=a.symmetric_difference(b)
# print(c)
#-------------------------------------------------------------------------------
# 作业题

# 99乘法表
# i=1
# while i<10:
#     j=1
#     while j<=i:
#         print(j,'*',i,'=',j*i,end='\t')
#         j+=1
#     print()
#     i+=1

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'*',i,'=',j*i,end='\t')
#     print()

# 百钱买百鸡
"""
百钱买百鸡的问题算是一套非常经典的不定方程的问题，题目很简单：公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱，

用100文钱买一百只鸡,其中公鸡，母鸡，小鸡都必须要有，问公鸡，母鸡，小鸡要买多少只刚好凑足100文钱。

分析：估计现在小学生都能手工推算这套题，只不过我们用计算机来推算，我们可以设公鸡为x，母鸡为y，小鸡为z，那么我们

         可以得出如下的不定方程，

         x+y+z=100,

         5x+3y+z/3=100，

        下面再看看x，y，z的取值范围。

        由于只有100文钱，则5x<100 => 0<x<20, 同理  0<y<33,那么z<300

由于此处我们不是数学上研究不等式解法，而是让计算机为我们计算结果，所有暂不考虑效率问题。于是，从变量上我们便可以看出可以在三个循环中，逐个选出匹配条件。
"""
# for x in range(1,20):
#     for y in range(1,33):
#         z=100-x-y
#         if z%3==0 and (x*5+y*3+z/3==100):
#             print('买%d只公鸡，%d只母鸡，%d只小鸡满足'%(x,y,z))

# 获取2--100之间的所有素数
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

# 点歌系统
while True:
    print('点歌系统已启动！')
    print('***************')
    print('请选择点歌方式')
    print('通过地区点歌点击1')
    print('通过歌手点歌点击2')
    a=int(input('请选择您的点歌方式：'))
    if a==1:
        print('港澳台地区请选择1')
        print('大陆地区请选择2')
        #曲库
        quku = {'1': {'邓紫琪': {'我的秘密', '泡沫', 'ANNY'},
                      '刘德华': {"忘情水", '世界第一等', '来生缘'}},
                '2': {'张碧晨': {'不要忘记我爱你', '年轮', '白芍花开'},
                      '赵雷': {'成都', '三十岁的女人', '理想'}}}
        where_name=input('请输入您喜欢的歌手所属地区：')
        if where_name!='1' and where_name!='2':
            print('输入有误！请重新输入！我们将重新启动该系统')
            continue
        print('根据您的选择，我们找到以下歌手：')
        for i in list(quku[where_name].keys()):
            print(i,end=' ')
            print()
        songer_name=input('请输入您喜欢的歌手：')
        if songer_name not in list(quku[where_name].keys()):
            print('您的输入有误！我们将重新启动程序！')
            continue
        print('根据您的选择我们找到以下歌曲：')
        for j in list(quku[where_name].get(songer_name)):
            print(j,end=' ')
            print()
        song_name=input('请输入您喜欢的歌名：')
        print('请稍等：')
        print('播放开始！请开始你的表演！')
        break
    if a==2:
        quku = {'邓紫棋': {'我的秘密', '泡沫'}, '刘德华': {"忘情水", '世界第一等'},
                '张碧晨': {'不要忘记我爱你', '年轮'}, '赵雷': {'成都', '三十岁的女人'}}  # 字典
        print('曲库的歌手有：')
        for i in list(quku.keys()):
            print(i,end=' ')
            print()
        songer_name=input('请输入你喜欢的歌手：')
        if songer_name not in list(quku.keys()):
            print('您的输入错误！我们将重新启动程序！')
            continue
        print('根据您的选择我们找到：')
        for j in list(quku.get(songer_name)):
            print(j,end=' ')
            print()
        song_name=input('请输入您喜欢的歌名')
        print('请稍等。。。')
        print('播放开始！请开始你的表演')
        break
    else:
        print('您的选择有误！请按照屏幕上的规定重新选择！')
        continue